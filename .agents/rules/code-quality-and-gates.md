# Portões de Qualidade & Padrões de Código — JC Botelho

---

## 1. Verificações Obrigatórias Pré-Deploy

Antes de executar `./publish.sh`:

1. **Validação Visual e Responsiva:**
   Checar navegação mobile (< 768px) e desktop (> 1200px) garantindo que nenhum elemento quebre o layout horizontal.

2. **Integridade de Links Internos:**
   Todos os links para páginas do site devem apontar com precisão para `curriculo.html`, `revista-aterrorizante.html`, `index.html` ou âncoras válidas (`#sobre`, `#cases`).

3. **Execução de Compressão de Imagens:**
   Certificar-se de rodar `python3 compress_assets.py --in-place` caso tenha adicionado ou alterado qualquer arquivo em `assets/images/`.

4. **Invalidação no CloudFront:**
   Garantir que a distribuição `EFTEVO3P436H1` receba o comando de invalidação ao final do deploy.

