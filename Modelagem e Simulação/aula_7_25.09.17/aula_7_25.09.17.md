## Processo de Chegada e Atendimento

- A relação entre λ e μ determinará se sistema será estável ou não

### Processo de chegadas (λ)

Como e quando os clientes chegam no sistema

- taxa de chegada ➔ número médio de chegads por unidade de tempo
- intervalo entre chegadas ➔ tempo entre uma chegada e a próxima
- padrão das chegadas ➔ regular, aleatório, ou seguindo alguma distribuição

### Processo de atendimento (μ)

Como os clientes são servidos pelo sistema

- taxa de atendimento ➔ número médio de clientes atendidos por unidade de tempo
- tempo de serviço ➔ quanto tempo leva para atender cada cliente
- número de servidores ➔ quantos canais de atendimento existem

## Disciplina e Capacidade da Fila

### Disciplina
Definição: regra que determina qual cliente será atendido primeiro

- FIFO ➔ primeiro a chegar, primeiro a ser atendido
- LIFO ➔ último a chegar, primeiro a ser atendido
- Prioridades ➔ clientes com maior prioridade são atendidos primeiro
- Aleatória ➔ cliente é escolhido ao acaso da fila

### Capacidade

- Limites físicos do sistema
- Capacidade da fila ➔ quantos clientes podem aguardar
- Capacidade total ➔ quantos clientes cabem no sistema ➔ fila + atendimento
- População fonte ➔ quantos clientes podem potencialmente chegar

## Notação de Kendall

sistema padronizado para classificar modelos de fila
- notação:  **A/B/c/K/N/D**

- legenda
  - A ➔ Processo de chegada ➔ M = Markoviano, D = Determinístico, G = Geral
  - B ➔ Tempo de serviço ➔ M = Markoviano, D = Determinístico, G = Geral
  - c ➔ número de servidores
  - K ➔ capacidade máxima do sistema
  - N ➔ Tamanho da população fonte
  - D ➔ Disciplina da fila
- M ➔ quando as chegadas são espontâneas, irregulares e a taxa é aproximadamente constante no período
- D ➔ quando há agenda/ritmo fixo
- G ➔ quando os dados mostram padrão diferentes ➔ exemeplo: rajadas, variação grande, horários muito distintos
- Formato simplificado A/B/c quando K = ∞, N = ∞, D = FIFO


.
.
.
.
.
.

.
.
..
.
.
.
