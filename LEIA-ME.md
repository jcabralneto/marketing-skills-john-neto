# 11 skills de marketing — John Neto

Instruções para orientar uma IA em tarefas de marketing. Desenvolvi este pacote depois do curso presencial de IA e marketing que fiz em Harvard, combinando os estudos com critérios de aplicação e revisão.

## Escolha pela tarefa

| Skill | Para que usar |
|---|---|
| marketing-orquestrador | Organizar objetivo, oferta, prioridades e próximas etapas. |
| marketing-publico-alvo | Comparar segmentos e escolher quem atender. |
| marketing-personas | Entender necessidades, objeções e critérios de compra. |
| marketing-conteudo | Planejar e escrever com a voz da marca. |
| marketing-criativos | Preparar roteiros e materiais visuais. |
| marketing-seo | Planejar conteúdo e páginas para buscas relevantes. |
| marketing-geo | Avaliar presença em respostas de IA e priorizar melhorias. |
| marketing-personalizacao | Definir mensagens e próximas ações conforme o contexto. |
| marketing-analise-preditiva | Analisar históricos e critérios de priorização de leads. |
| marketing-experimentos | Planejar testes e interpretar seus resultados. |
| marketing-martech | Mapear integrações e avaliar custos e benefícios. |

## Primeiro uso

Extraia o ZIP. Se você já usa um ambiente com suporte a skills, peça ao assistente para instalar as pastas de `skills/` no local previsto por esse ambiente, preservando qualquer versão diferente que já exista. Para o Codex, o pacote inclui o instalador opcional `scripts/instalar_skills.py`, que verifica conflitos antes de copiar para a pasta de skills do usuário; ele não sobrescreve arquivos diferentes. A disponibilidade na conversa deve ser conferida após a instalação.

Também é possível usar o texto como orientação: em uma conversa que aceite arquivos, forneça o `SKILL.md` da especialidade e as referências necessárias da mesma pasta. Isso não equivale a uma instalação nem acrescenta ferramentas ao assistente.

Comece com um pedido concreto:

> Use marketing-publico-alvo para comparar os segmentos que posso atender. Minha oferta é [...], meus clientes atuais são [...] e os dados disponíveis estão anexados. Separe o que os dados mostram das hipóteses e das perguntas que ainda precisam ser respondidas.

Depois de escolher um segmento, use marketing-personas para aprofundar a decisão de compra. Para escrever, forneça à marketing-conteudo a oferta, o público e exemplos aprovados da voz da marca.

Se você ainda não sabe por onde começar:

> Use marketing-orquestrador para organizar o marketing deste negócio. Quero alcançar [...], tenho [...] de capacidade e estas informações [...]. Escolha apenas as especialidades necessárias.

## Como avaliar a resposta

Forneça fatos do negócio e confira o resultado. Dados insuficientes devem aparecer como hipóteses ou perguntas; uma persona não substitui entrevistas e uma projeção não comprova ganho. SEO e GEO não garantem posição, citação ou vendas. A disponibilidade de ferramentas define o que pode ser executado.

Este é um material autoral de aplicação, sem afiliação ou endosso institucional de Harvard. As apresentações, gravações, transcrições e o caderno do curso não integram o pacote. Referências privadas foram mantidas apenas como identificação bibliográfica, sem links de acesso. Publicação, envio de mensagens e outras ações externas dependem de autorização própria.

Edição de compartilhamento: 14/10/2026. Revalide regras de plataformas quando for implementar.
