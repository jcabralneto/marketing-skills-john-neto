# Protocolo e cálculo

| Decisão | Hipótese | Unidade e público | Controle/variante | Métrica e janela | Efeito mínimo | Método/amostra/parada | Guardrails |
| --- | --- | --- | --- | --- | --- | --- | --- |

Registre também o responsável e a evidência de implementação. Um clique pode ser métrica primária de um teste de mensagem, mas não substitui venda ou margem em uma conclusão comercial.

Para proporções, taxa = conversões / elegíveis. Diferença em pontos percentuais = 100 × (taxa B − taxa A). Variação relativa = (taxa B / taxa A − 1) × 100; fica indefinida quando A = 0.

O script usa intervalos de Wilson para cada proporção e combina os limites pelo método de Newcombe sem correção de continuidade para a diferença B−A. Recebe contagens inteiras, exige elegíveis positivos e conversões entre zero e elegíveis. Não calcula tamanho amostral nem corrige espiadas ou múltiplos testes. Seu intervalo assume duas amostras independentes com resultado binário e um horizonte de avaliação definido. É uma descrição calculada, não autorização para declarar vencedor.

A fórmula foi conferida na [implementação de referência do statsmodels 0.14.3](https://www.statsmodels.org/v0.14.3/_modules/statsmodels/stats/proportion.html), funções `proportion_confint` (Wilson) e `confint_proportions_2indep` (Newcombe). O script usa apenas a biblioteca padrão de Python; não requer statsmodels instalado.

Exemplo sintético: A tem 60 conversões em 1.000 elegíveis; B tem 75 em 1.000. As taxas são 6% e 7,5%, diferença de 1,5 ponto percentual e aumento relativo de 25%. A incerteza deve ser reportada; não chamar “25 pontos percentuais”.

Execução: `python3 scripts/comparar_taxas.py --a-conversoes 60 --a-total 1000 --b-conversoes 75 --b-total 1000`. Use o caminho do script relativo à pasta desta skill ou resolva seu caminho absoluto. Resultado em JSON, sem rede ou efeitos em campanhas.
