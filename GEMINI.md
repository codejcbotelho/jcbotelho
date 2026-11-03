# Guia do Desenvolvedor & Diretrizes de IA — JC Botelho

> **🚨 INICIALIZAÇÃO DE SESSÃO MANDATÓRIA:**
> Ao iniciar **qualquer nova sessão ou tarefa**, o assistente de IA DEVE começar consultando o arquivo central:
> 📍 [`/.agents/ENTRYPOINT.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/ENTRYPOINT.md)
> e validar mentalmente o checklist de pré-requisitos de qualidade, design system Executive & Sharp (`--radius: 0px`), ícones flats SVG puros, compressão de assets e deploy S3 com CloudFront antes de propor ou executar alterações.

---

## 🏛️ 1. Arquitetura do Projeto

O projeto **jcbotelho.com** é um portfólio executivo e plataforma autoral de altíssima performance estruturado em HTML5 semântico, CSS puro e JavaScript moderno. O ecossistema é servido via **AWS S3** (`jcbotelho.com`) e distribuído globalmente pelo **Amazon CloudFront** (`EFTEVO3P436H1`).

---

## 🗺️ 2. Mapa Rápido de Arquivos (Evite Greps Globais)

Em vez de pesquisar na raiz ou fazer buscas globais recursivas, vá direto ao arquivo responsável:

### 🧠 Base de Conhecimento, Specs & Regras (`.agents/`)
| Recurso | Arquivo |
|---|---|
| Ponto de Partida Obrigatório de Boot | [`/.agents/ENTRYPOINT.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/ENTRYPOINT.md) |
| Arquitetura Geral & Esteira AWS | [`/.agents/specs/core-architecture.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/specs/core-architecture.md) |
| Design System "Executive & Sharp" | [`/.agents/rules/ui-and-tokens.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/rules/ui-and-tokens.md) |
| SEO, Metadados & Performance | [`/.agents/rules/seo-and-performance.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/rules/seo-and-performance.md) |
| Portões de Qualidade & Deploy | [`/.agents/rules/code-quality-and-gates.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/rules/code-quality-and-gates.md) |
| Checklist de Início de Sessão | [`/.agents/skills/session-init-checklist.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/skills/session-init-checklist.md) |
| Execução de Testes & Servidor | [`/.agents/skills/test-runner.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/skills/test-runner.md) |

### 🌐 Páginas & Arquivos Centrais
| Função | Arquivo |
|---|---|
| Página Principal (Home Executiva) | [`index.html`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/index.html) |
| Currículo & Evolução de Carreira | [`curriculo.html`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/curriculo.html) |
| Revista Aterrorizante (Projetos Literários) | [`revista-aterrorizante.html`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/revista-aterrorizante.html) |
| Página 404 Personalizada | [`404.html`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/404.html) |
| Folha de Estilos Global | [`styles.css`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/styles.css) |
| Script de Deploy Automatizado | [`publish.sh`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/publish.sh) |
| Script de Otimização de Imagens | [`compress_assets.py`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/compress_assets.py) |

---

## ⚡ 3. Regras de Ouro de Desenvolvimento

1. **Design System "Executive & Sharp":**
   - Geometria afiada com `--radius: 0px`. Tipografia `Plus Jakarta Sans` para títulos e `Inter` para corpo.
2. **Sem Emojis em Seções Executivas:**
   - Utilize sempre ícones flat em SVG puro.
3. **Compressão Automática de Assets:**
   - Sempre execute `python3 compress_assets.py --in-place` antes do deploy.
4. **Deploy Seguro com CloudFront:**
   - Publique utilizando `./publish.sh` para garantir sync no S3 e invalidação de cache na CDN.
