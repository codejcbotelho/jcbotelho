# SEO, Performance & Metadados — JC Botelho

---

## 1. Metatags Obrigatórias por Página

Toda página HTML deve conter:
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Tags OpenGraph (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`)
- Twitter Cards (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`)
- Link canônico apontando para `https://jcbotelho.com/...`
- Vínculo com `site.webmanifest` e `favicon.svg`.

---

## 2. Otimização de Imagens

- Todas as imagens de logos, fotos e capas devem ser comprimidas usando o script `compress_assets.py --in-place`.
- Utilize atributos `loading="lazy"` em imagens abaixo da dobra e `alt="..."` descritivo em todas as tags `<img>`.

