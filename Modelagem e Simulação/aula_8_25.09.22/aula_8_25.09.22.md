# M/M/C

### Definição

semelhante ao modelo de fila M/M/1, entretanto agora com múltiplos servidores. Então é uma fila ÚNICA descarregada em diversos servidores

- exemplo:
    - call center: vários atendentes para uma fila de chamadas
    - supermercado: sistema de fila única para vários caixas

### Vantagens de Múltiplos Servidores

- redução significativa do tempo de espera
- melhor aproveitamente da capacidade total
- maior flexibilidade operacional
- menor variabilidade nos tempos de espera
- no geral, mais rápido

### Hipóteses do Modelo M/M/c

- chegadas seguem processo de Poisson (taxa λ)
- tempos de serviço exponenciais (taxa μ por servidor)
- c servidores idênticos e independentes
- fila única alimentando todos os servidores
- Disciplina FIFO, primeiro a chegar, primeiro a ser atendido
- capacidade infinita da fila
- população fonte infinita
- capacidade total: ${c*μ}$

### Condição de Estabilidade
- $ρ=\frac{λ}{c*μ} < 1$
- Taxa de chegada < capacidade total do sistema ➔ λ < c×μ 
- se ρ > = 1, a fila cresce indefinidamente

### Utilização do Sistema M/M/c

- utilização do sistema : $ρ=\frac{λ}{c*μ}
  - ρ = 0.6 ➔ cada servidor ocupado 60% do tempo em média
  - ρ = 0.8 ➔ cada servidor ocupado 80% do tempo
  - ρ = 0.9 ➔ sistema sob alta pressão

---

## Fórmula de Erlang C

- calcula a probabilidade de um cliente ter que esperar:
  - $$P(\text{wait}) = \frac{ \left( \frac{a^c}{c!} \times \frac{c}{c - a} \right) }{ \sum (\frac{a^n}{n!}) + \left( \frac{a^c}{c!}) \times (\frac{c}{c - a} \right) }$$
  - P(wait) = {tempo extra} / {somatório} + {tempo extra}
  - somatório vai de n = 0 até n = c-1
  - Legenda:
      - $a = \frac{λ}{μ}$ ➔ tráfego oferecido, em Erlangs
      - c = números de servidores
      - $ρ = \frac{a}{c} = \frac{λ}{c*μ}$ ➔ utilização média por servidor
      - P(wait) = probabilidade de esperar na fila

### Interpretando Erlang C

- P(wait) = probabilidade de esperar na fila
    - P(wait) = 0.10 ➔ 10% dos clientes esperam na fila
    - P(wait) = 0.25 ➔ 25% dos clientes esperam na fila
    - P(wait) = 0.50 ➔ 50% dos clientes esperam na fila
    - 
#### Fatores que influenciam P(wait)

- Utilização (ρ) ➔ quanto maior, maior P(wait)
- Número de servidores (c) ➔ quanto maior, menor P(wait)
- Variabilidade do serviço (incerteza dos tempos de atendimento) ➔ exponencial gera mais espera

---

## Métricas de Desempenho M/M/c

- a partir do P(wait) se calcula todas as outras métricas
  - Tempo médio de espera na fila
    - (Wq) ➔ $Wq =\frac{P(Wait) * 1}{(c*μ - λ)}$
  - Número médio na Fila
    - (Lq) ➔ $Lq = λ * Wq$
  - Tempo médio no Sistema
    - (W) ➔ $W = Wq + \frac{1}{μ}$
  - Número Médio no Sistema
    - (L) ➔ $L = λ * W$
  - Lei de Little (verificação)
    - $L = λ * W$
    - $Lq = λ * Wq$
   
## VANTAGENS DO M/M/c

### Pooling Effect (efeito de agrupamento)

* variabilidade individual é absorvida pelo grupo
* servidores ociosos compensam os ocupados
* redução dramática da variabilidade total

### Melhor Utilização de Recursos

* não há servidores completamente ociosos
* carga distribuida automaticamente
* economia de escala no dimensionamento

### Justiça no Atendimento

* todos esperam na mesma fila ➔ não há 'escolha errada' de fila
* tempo de espera mais previsível

### Flexibilidade Operacional

* fácil ajuste do número de servidores
* adaptação rápida a variações de demanda

## Quando usar M/M/c?

- há múltiplos servidores idênticos
- existe uma fila única alimentando todos
- servidores podem atender qualquer cliente (sem especialização)
- chegadas são independente e aleatórias
- tempo de serviços são variáveis

#### NÃO usar quando

- se cada servidor tem especialização diferente
- se há filas separadas por servidor
- serviços têm prioridades diferentes

###





