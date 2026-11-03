# Test Runner & Execução de Ambiente — JC Botelho

---

## 1. Visualização Local

Para testar as páginas localmente sem bloqueios de CORS em assets:
```bash
python3 -m http.server 8080
# Acesse http://localhost:8080 no navegador
```

---

## 2. Otimização de Assets

Para comprimir todas as imagens in-place:
```bash
python3 compress_assets.py --in-place
```

---

## 3. Publicação em Produção

Para sincronizar com o S3 e invalidar o CloudFront:
```bash
./publish.sh
```

