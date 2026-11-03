# Checklist de Início de Sessão (5 Minutos) — JC Botelho

> Siga este roteiro no primeiro minuto de qualquer nova sessão com o projeto jcbotelho.com.

1. **Leitura do Entrypoint:**
   - Abra e revise [`/.agents/ENTRYPOINT.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/ENTRYPOINT.md).

2. **Identificação da Modificação:**
   - É alteração de conteúdo ou layout? Cheque [`ui-and-tokens.md`](file:///Users/joaoclaudiobotelhorosa/Desktop/Projects/jcbotelho/.agents/rules/ui-and-tokens.md).
   - É adição de imagens? Lembre-se de rodar a compressão de assets.

3. **Verificação de Regras Críticas:**
   - A geometria está com cantos afiados (`--radius: 0px`)?
   - Nenhum emoji solto foi colocado em cards ou seções técnicas (apenas SVGs flats)?
   - O contraste de cor atende aos critérios de leitura?

4. **Validação Final:**
   - Teste localmente via `python3 -m http.server 8080`.

