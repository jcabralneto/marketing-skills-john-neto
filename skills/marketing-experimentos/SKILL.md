---
name: marketing-experimentos
description: Desenhar e interpretar testes A/B ou multivariados de marketing com hipótese, população, métricas, regra de parada e limites de inferência. Use para decidir o que testar ou avaliar resultados; uma taxa maior isoladamente não comprova vitória.
---

# Experimentos de marketing

Conecte o teste a uma decisão. Diferencie um experimento aleatório de uma comparação histórica ou observacional e limite a conclusão ao desenho efetivamente usado.

## Planejar

Use o [protocolo](references/protocolo.md) para registrar hipótese, controle e intervenção, unidade de randomização, população elegível, alocação, métrica principal, guardrails, baseline, efeito mínimo relevante, método estatístico, amostra e duração propostas.

Para testes multivariados, verifique tráfego, número de combinações, interações e ajuste de comparações. Um A/B simples costuma esclarecer uma decisão antes de um desenho mais complexo, mas preserve a escolha explícita do usuário quando viável.

Defina janela de atribuição, tratamento de repetição/contaminação, eventos e regra de parada antes de analisar. Ausência de baseline impede calcular uma amostra precisa; entregue a informação faltante ou cenários com premissas explícitas. Não declare que um prazo fixo, como sete dias, sempre basta.

## Interpretar

Confira período, alocação, denominadores, unidade, integridade dos eventos e se o teste seguiu o protocolo. Diferencie usuários únicos de sessões e contagens de conversão de taxas por pessoa. Investigue diferenças de composição, perda de dados e alterações durante o teste.

Reporte taxas, diferença em pontos percentuais, variação relativa, tamanho das amostras e incerteza compatível com o desenho. Use cálculo reproduzível. Para duas proporções independentes, o helper [comparar_taxas.py](scripts/comparar_taxas.py) calcula estatísticas descritivas e um intervalo de Wilson/Newcombe; leia suas limitações no protocolo. Não o use para receita média, medidas repetidas ou testes sequenciais sem adaptação.

Não escolha vencedor apenas por p-valor, pelo painel favorável do dia ou por diferença positiva. Considere efeito mínimo relevante, guardrails e regra de parada. Um intervalo que inclui zero deixa a direção incerta; isso não prova igualdade. Uma diferença sem incerteza não prova significância.

Se o teste não foi randomizado ou a integridade falhou, relate associação ou resultado exploratório. Não atribua causalidade à IA nem declare receita incremental a partir de cliques. Recomendação de lançar uma variante exige também avaliar custo, qualidade e capacidade.

## Entregar

Forneça protocolo pronto para revisão ou leitura dos resultados com: observações, cálculos, limitações e decisão sustentada. A proposta não ativa teste nem altera tráfego por conta própria. Respeite autorizações vigentes para execução e confirme configuração e resultado no sistema usado.

## Base do curso

G11; caderno, capítulo 15; agenda A01, segundo dia. A demonstração não fornece um protocolo estatístico completo. O desenho, as fórmulas e o helper são complementos operacionais identificados como tais.

Consulte [origem e limites](references/origem-do-curso.md) quando precisar auditar a atribuição ao curso.
