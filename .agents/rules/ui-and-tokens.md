# Design System "Executive & Sharp" — JC Botelho

---

## 1. Tokens de Design & Geometria

A estética do projeto transmite seriedade executiva, sofisticação técnica e precisão geométrica:

```css
:root {
  --bg-primary: #09090b;       /* Fundo principal profundo */
  --bg-secondary: #111114;     /* Fundo alternado de seções */
  --bg-card: #15151a;          /* Fundo dos cards executivos */
  --bg-card-hover: #1a1a22;    /* Hover nos cards */
  --border-glass: rgba(255, 255, 255, 0.08);
  --border-glass-bright: rgba(255, 255, 255, 0.18);
  
  --text-primary: #f4f4f6;     /* Branco nítido */
  --text-secondary: #a1a1aa;   /* Cinza neutro legível */
  --text-muted: #71717a;       /* Detalhes e metadados */
  
  /* Geometria afiada (Zero Border-Radius) */
  --radius: 0px;
  --radius-sm: 0px;
}
```

---

## 2. Tipografia

- **Títulos e Destaques:** `'Plus Jakarta Sans'`, sans-serif com pesos `600`, `700`, `800`.
- **Corpo e Parágrafos:** `'Inter'`, sans-serif com peso `400` e entrelinha `1.65`.

---

## 3. Ícones Flat SVG vs Emojis

- **Proibição Absoluta de Emojis:** É vedado o uso de emojis coloridos de sistema (ex: 🚀, 💻, 📈) nas páginas corporativas e de currículo.
- **Padrão Flat:** Utilize sempre SVGs inline com classes semânticas (`.feature-icon`, `.tech-icon`), preenchimento ou traço monocromático (`currentColor`, `#ffffff` ou `#a1a1aa`).

