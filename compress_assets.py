#!/usr/bin/env python3
"""
JC Botelho — Image Asset Compression & Optimization Tool
Adaptado a partir da ferramenta do Clã do Terror (cladoterror.com)

Otimiza imagens PNG, JPEG e JPG com compressão inteligente, mantendo
alta fidelidade visual e reduzindo o peso para carregamento ultrarrápido na Web.
"""

import os
import sys
import shutil
import argparse

# Configura codificação de saída para consoles Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from PIL import Image, ImageOps
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def compress_single_image(src_path, dest_path, max_width=1920, jpeg_quality=82, png_optimize=True):
    """Otimiza uma única imagem e salva se o tamanho for menor."""
    original_size = os.path.getsize(src_path)
    ext = os.path.splitext(src_path)[1].lower()
    
    if original_size < 10 * 1024:
        # Arquivos minúsculos (< 10KB), copia diretamente
        if src_path != dest_path:
            shutil.copy2(src_path, dest_path)
        return 0, False

    try:
        with Image.open(src_path) as img:
            # Corrige rotação baseada em EXIF se houver
            img = ImageOps.exif_transpose(img)
            
            # Redimensiona se ultrapassar a largura máxima
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int(float(img.height) * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Cria pasta de destino se não existir
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            temp_dest = dest_path + ".tmp_opt"
            
            if ext == '.png':
                # Otimização de PNG
                if img.mode == 'RGBA':
                    alpha = img.split()[-1]
                    if alpha.getextrema() == (255, 255):
                        img = img.convert('RGB')
                
                img.save(temp_dest, format='PNG', optimize=png_optimize)
            
            elif ext in ('.jpg', '.jpeg'):
                # Otimização de JPEG
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(temp_dest, format='JPEG', optimize=True, quality=jpeg_quality, progressive=True)
            
            else:
                # Outros formatos (SVG, WEBP, etc.)
                if src_path != dest_path:
                    shutil.copy2(src_path, dest_path)
                return 0, False
            
            new_size = os.path.getsize(temp_dest)
            
            # Se a compressão reduziu o tamanho, adota o novo arquivo
            if new_size < original_size:
                shutil.move(temp_dest, dest_path)
                saved = original_size - new_size
                return saved, True
            else:
                if os.path.exists(temp_dest):
                    os.remove(temp_dest)
                if src_path != dest_path:
                    shutil.copy2(src_path, dest_path)
                return 0, False

    except Exception as e:
        print(f"[!] Erro ao processar {os.path.basename(src_path)}: {e}")
        if src_path != dest_path and not os.path.exists(dest_path):
            shutil.copy2(src_path, dest_path)
        return 0, False

def process_directory(src_directory, dest_directory=None, in_place=False, max_width=1920, jpeg_quality=82):
    """Varre e comprime todas as imagens do diretório."""
    if not os.path.exists(src_directory):
        print(f"[!] Diretorio nao encontrado: {src_directory}")
        return
    
    if in_place:
        dest_directory = src_directory
        print(f"[*] Otimizando imagens diretamente em: {src_directory}")
    else:
        dest_directory = dest_directory or os.path.join(os.path.dirname(src_directory), ".compressed_images")
        print(f"[*] Lendo de: {src_directory}")
        print(f"[*] Salvando em: {dest_directory}")

    total_original = 0
    total_saved = 0
    optimized_count = 0
    total_files = 0
    
    extensions = ('.jpg', '.jpeg', '.png')

    for root, _, files in os.walk(src_directory):
        rel_path = os.path.relpath(root, src_directory)
        target_root = os.path.join(dest_directory, rel_path) if not in_place else root
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_root, file) if not in_place else src_file
            
            if file.lower().endswith(extensions):
                total_files += 1
                orig_size = os.path.getsize(src_file)
                total_original += orig_size
                
                saved, success = compress_single_image(
                    src_file, dest_file, max_width=max_width, jpeg_quality=jpeg_quality
                )
                
                if success and saved > 0:
                    optimized_count += 1
                    total_saved += saved
                    percent = (saved / orig_size) * 100
                    print(f"  [OK] {file} -> Economia: {saved / 1024:.1f} KB (-{percent:.1f}%)")
            else:
                if not in_place and src_file != dest_file:
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                    shutil.copy2(src_file, dest_file)

    print("\n" + "="*50)
    print("RESUMO DA COMPRESSAO DE ASSETS")
    print("="*50)
    print(f"Imagens verificadas: {total_files}")
    print(f"Imagens otimizadas: {optimized_count}")
    if total_original > 0:
        total_percent = (total_saved / total_original) * 100
        print(f"Tamanho original total: {total_original / 1024 / 1024:.2f} MB")
        print(f"Espaco total economizado: {total_saved / 1024 / 1024:.2f} MB (-{total_percent:.1f}%)")
    print("="*50 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comprime e otimiza imagens do projeto jcbotelho.com")
    parser.add_argument("--dir", default=None, help="Diretorio de origem das imagens (padrao: assets)")
    parser.add_argument("--out", default=None, help="Diretorio de destino")
    parser.add_argument("--in-place", action="store_true", help="Sobrescreve as imagens originais diretamente se ficarem menores")
    parser.add_argument("--max-width", type=int, default=1920, help="Largura maxima em pixels (padrao: 1920)")
    parser.add_argument("--quality", type=int, default=82, help="Qualidade JPEG 1-100 (padrao: 82)")
    
    args = parser.parse_args()
    
    if not HAS_PIL:
        print("[!] A biblioteca Pillow nao esta instalada.")
        print("Para instalar execute: pip install pillow")
        sys.exit(1)
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = args.dir or os.path.join(base_dir, "assets")
    
    process_directory(
        target_dir, 
        dest_directory=args.out, 
        in_place=args.in_place or (args.out is None),
        max_width=args.max_width,
        jpeg_quality=args.quality
    )
