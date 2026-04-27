#!/bin/bash



# Compila o Sass
#sass css/scss/styles.scss css/styles.css

# Publica no S3
aws s3 cp ./ s3://jcbotelho.com --recursive --acl public-read --exclude ".git/*" --exclude ".gitignore" --exclude "publish.sh" --exclude "README.md" --exclude "docs/*" --exclude "replaces/*" --exclude "clone.sh" --exclude "replaces.sh" --exclude "run.sh" --exclude "css/scss/*" --exclude "exemple/*"

# Invalida o cache do CloudFront
aws cloudfront create-invalidation --distribution-id EFTEVO3P436H1 --paths "/*"
