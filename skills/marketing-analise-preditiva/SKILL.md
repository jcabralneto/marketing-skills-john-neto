---
name: marketing-analise-preditiva
description: Analisar dados de marketing para lead scoring, propensão, retenção, CLV ou previsão e convertê-los em decisões operacionais. Use para priorizar a partir de históricos ou desenhar uma regra inicial quando a base ainda não permite validar um modelo.
---

# Predição e priorização

Comece pela decisão que o score ou previsão vai mudar. Defina unidade de análise, resultado, horizonte e instante em que a decisão será tomada. Um número sem ação, responsável e prazo não encerra o trabalho.

## Verificar os dados

Inspecione esquema, origem, período, duplicatas, identidade, ausências, definição dos resultados, casos ainda abertos e viés de seleção. Separe base histórica com desfecho da base que receberá a decisão. Verifique quando cada atributo se tornou disponível.

Exclua vazamento do futuro e o próprio desfecho. Demo, proposta e resposta podem ser válidas ou inválidas conforme o momento da previsão; não as remova nem aceite automaticamente. Dados ausentes não significam zero. Leads abertos não equivalem a perdas. Não use características sensíveis ou proxies indevidos para priorização comercial.

Se faltar a base original, entregue o desenho da análise e o que precisa ser coletado. Não recalcule taxas narradas em aula nem apresente resultados sintéticos como resultados do cliente.

## Escolher uma abordagem

Em lead scoring, mantenha fit e intent separados. Explique os critérios de adequação e sinais recentes de interesse, incluindo decaimento quando fizer sentido. Comece com regras justificáveis se faltarem resultados, qualidade ou amostra adequada; nomeie-as hipóteses não validadas. Não existe um número universal de linhas que legitime um modelo.

Quando houver base adequada, escolha um modelo compatível com a pergunta, valide fora do treino e preserve a ordem temporal e a identidade de clientes entre partições. Compare com uma regra simples. Inspecione calibração se reportar probabilidades, estabilidade e desempenho por recortes relevantes. Se o suporte for insuficiente, não forneça uma probabilidade com falsa precisão.

Para retenção, defina o que constitui churn e trate censura/janelas incompletas. Para CLV, explicite horizonte, margem, custos e premissas; faturamento acumulado não é valor futuro. Para previsão, use avaliação temporal e incerteza. Consulte [avaliação e encaminhamento](references/avaliacao.md).

## Transformar em ação

Estabeleça prioridades considerando capacidade comercial, custo dos erros e valor esperado com suporte. Para cada faixa ou regra, indique ação, responsável, SLA proposto, volume esperado quando calculável e caminho para dados insuficientes. Não transplante pesos, limites de empresa ou faixas 70/40 do exercício TeamPulse.

Entregue diagnóstico, critérios/modelo reproduzível quando treinado, avaliação, limites, encaminhamento e revisão por mudança de produto ou dados. Meça precisão entre priorizados, cobertura dos compradores, lift e cumprimento do SLA quando aplicáveis. Associação com rapidez de resposta não demonstra seu efeito causal.

## Base do curso

M03, páginas 2–12; M05, páginas 2 e 4–9; G06–G07; caderno, capítulos 8–10. Avaliação temporal, calibração e censura são complementos técnicos para aplicação responsável.

Consulte [origem e limites](references/origem-do-curso.md) quando precisar auditar a atribuição ao curso.
