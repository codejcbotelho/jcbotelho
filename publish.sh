#!/bin/bash

echo "🚀 Iniciando publicação para S3 e CloudFront..."

# Otimização e compressão automática de imagens
echo "🖼️  Otimizando imagens e assets..."
python compress_assets.py --in-place || python3 compress_assets.py --in-place || true

# Sincroniza arquivos para o S3
aws s3 sync ./ s3://jcbotelho.com --acl public-read \
  --exclude ".git/*" \
  --exclude ".gitignore" \
  --exclude "publish.sh" \
  --exclude "compress_assets.py" \
  --exclude "plan.md" \
  --exclude "README.md" \
  --exclude "docs/*" \
  --exclude "replaces/*" \
  --exclude "clone.sh" \
  --exclude "replaces.sh" \
  --exclude "run.sh" \
  --exclude "css/scss/*" \
  --exclude "exemple/*"

# Garante upload explícito dos arquivos essenciais
aws s3 cp styles.css s3://jcbotelho.com/styles.css --acl public-read
aws s3 cp site.webmanifest s3://jcbotelho.com/site.webmanifest --acl public-read

# Invalida o cache do CloudFront
echo "🔄 Invalidando cache do CloudFront..."
aws cloudfront create-invalidation --distribution-id EFTEVO3P436H1 --paths "/*"

echo "✅ Publicação concluída com sucesso!"
