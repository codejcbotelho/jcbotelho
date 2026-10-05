# Backlog & Status de Implementação

1. [x] **Fonte Profissional & Tipografia Executiva**
   - Substituída a fonte caricata/arredondada (`Nunito`) pela combinação moderna e executiva de **Plus Jakarta Sans** (títulos, números, botões e labels técnicos) e **Inter** (corpo de texto com alta legibilidade), com tracking refinado e pesos geométricos.

2. [x] **Remoção de referências ao Itaú Unibanco da Home**
   - Removidas todas as menções diretas na página inicial (`index.html`), mantendo títulos e badges voltados para *Liderança Técnica & Engenharia de Software* e *Sistemas Críticos*.
   - A linha do tempo completa e a experiência continuam documentadas detalhadamente em `curriculo.html`.

3. [x] **Diagramação Equilibrada dos Cards de Produções (Home)**
   - Reformulada a grade de produções para um layout simétrico **2x2** no desktop (`grid-template-columns: repeat(2, 1fr)`), eliminando o card órfão e garantindo harmonia visual.

4. [x] **Estilo Quadrado, Agressivo & Nova Identidade Visual**
   - Implementado o novo monograma **JC** (vetorizado e ajustado como ícone na navbar e no favicon).
   - Eliminados cantos arredondados e bordas tipo pílula: adotado raio quadrado agressivo (`--radius: 0px`), bordas técnicas de 1px, paleta obsidian/dark luxury, alto contraste e visual executivo premium.

5. [x] **Formulário de Contato Seguro & Backend Unificado**
   - Construído formulário de contato completo na Home com campos de Nome, E-mail, Assunto, Mensagem (com contador dinâmico de caracteres) e dropzone opcional para anexos (PDF, DOCX, ZIP, imagens até 25MB).
   - E-mail pessoal protegido contra robôs/spammers.
   - Endpoint unificado e backend adaptado para suportar `origem` dinâmica (`jcbotelho.com`), despachando via AWS SES com formatação executiva.