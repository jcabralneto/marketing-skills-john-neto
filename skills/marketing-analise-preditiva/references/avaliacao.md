# Avaliação e encaminhamento

Documente o dicionário dos campos e o instante de decisão. Preserve transformações e exclusões para que outra pessoa consiga reproduzir a análise.

| Métrica | Definição | Limite |
| --- | --- | --- |
| Precisão | Verdadeiros positivos / todos os classificados positivos | Depende do limiar e da população |
| Recall | Verdadeiros positivos / todos os positivos observados | Exige conhecer os desfechos, inclusive dos não priorizados |
| Lift | Taxa de conversão da faixa / taxa da base comparável | Não é efeito causal do contato |
| Cobertura no SLA | Leads elegíveis atendidos no prazo / leads elegíveis | Exige eventos e relógio de negócio definidos |

Denominador zero ou não conhecido gera resultado indisponível, não zero. Para ordenar uma fila limitada, considere métricas nos primeiros K casos e informe K e a capacidade que o motivou.

A saída operacional separa: critérios de fit; sinais de intent; dados ausentes; prioridade; justificativas; ação; responsável; prazo; revisão. Exponha regras em uma forma que a equipe consiga seguir e contestar.

O acervo apresenta 1.000 leads históricos e 120 abertos em M03 página 11, e 2.500 em M05 página 2. Preserve a divergência. A planilha original da TeamPulse não está no conjunto de PDFs; o pequeno CSV preparatório local é outro exercício. Pesos e resultados do curso não são parâmetros de produção.
