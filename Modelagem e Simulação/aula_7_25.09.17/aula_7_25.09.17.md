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
  - A ➔ Processo de chegada ( M = Markoviano, D = Determinístico, G = Geral )
  - B ➔ Tempo de serviço ( M = Markoviano, D = Determinístico, G = Geral )
  - c ➔ número de servidores
  - K ➔ capacidade máxima do sistema
  - N ➔ Tamanho da população fonte
  - D ➔ Disciplina da fila
 
- M ➔ quando as chegadas são espontâneas, irregulares e a taxa é aproximadamente constante no período
- D ➔ quando há agenda/ritmo fixo
- G ➔ quando os dados mostram padrão diferentes ➔ exemeplo: rajadas, variação grande, horários muito distintos

- Formato simplificado A/B/c quando K = ∞, N = ∞, D = FIFO

---

## M/M/1 

Formato Simplificado da notação de kendall
- É M/M/1 quando:
  - A = Markoviano
  - B = Markoviano
  - c = 1
  - K = ∞
  - N = ∞
  - D = FIFO

- Primeira letra M
  - processo de chegada Markoviano, sem memória ➔ chegadas seguem processo de Poisson com taxa λ constante
- Segunda letra M
  - tempo de serviço Markoviano, sem memória ➔ tempos de serviço seguem distribuição exponencial com taxa μ
- Número 1
  - sistema possui exatamente um servidor ➔ apenas um cliente pode ser atendido por vez
- Premissa implícitas: capacidade infinita, população infinita, disciplina FIFO
  - **M/M/1 ➔ (M)Sistema com chegadas Poisson, (M)serviço exponencial, (1)um servidor**
- MARKOVIANO ➔ processo sem memória, o futuro depende apenas do estado presente

### Primeiro M - CHEGADAS (processo de Poisson)

- chegadas independentes e aleatórias
- taxa de chegada (λ) constante ao longo do tempo
- intervalos entre chegadas seguem distribuição exponencial
- probabilidade de chegada não depende do histórico (sem memória)

### Segundo M - SERVIÇOS (distribuição exponencial)

- tempos de serviço independentes
- taxa de atendimento (μ) constante
- tempo restante de serviço não depende do tempo já decorrido
- propriedade 'sem memória' simplifica a análise matemática

OBS: na prática assumimos aleatoriedade total em CHEGADAS e ATENDIMENTOS

### Número 1 - Um Servidor

- sistema possui exatamente um único canal de atendimento, apenas 1 cliente pode ser atendido ao mesmo tempo

### Hipóteses Fundamentais do M/M/1

- chegadas independentes seguindo processo de Poisson (taxa λ) é um modelo para chegadas 'ao acaso' com taxa média constante λ
- tempo de serviço independente e exponencial (taxa μ)
- capacidade infinita da fila, sem rejeição de clientes
- fonte da população infinita, sempre há potenciais clientes
- disciplina FIFO, primeiro a chegar é o primeiro a ser atendido
- sistema em regime permanente, steady-state (estado estacionário)
  - steady-state é o conceito de estado de fila que o sistema:
    - Se estabiliza
    - Não cresce nem diminui sem parar
    - Suas medidas estatísticas se repetem e ficam previsíveis
- CONDIÇÃO DE ESTABILIDADE
  - ρ = λ/μ < 1
  - se p >= 1, a fila cresce indefinidamente e o sistema fica instável

---
 
 ### QUANDO USAR M/M/1
 
- chegadas realmente aleatórias, sem padrões sazonais
- tempos de serviço muito variáveis
- sistema com um ponto de atendimento
- análise inicial ou aproximação rápida
- sistema sem limitações de capacidade

#### VANTANGENS

- fórmulas analitícas simples e diretas
- cálculos rápidos para análise inicial
- base teórica sólida e bem estabelecida
- fácil implementação em planilhas ou programas

#### LIMITAÇÕES

- pressupóe distribuições exponenciais ➔ alta variabilidade
- não considera prioridade entre clientes, todos iguais
- assume capacidade infinita ➔ irrealista
- pode superestimar tempos de espera
- **Não adequado para sistemas com padrões regulares** por ser aleatório

### EXEMPLOS PRÁTICOS DE APLICAÇÃO

- Sistema de computação
  - fila de requisições
  - CPU processando requisições
  - servidor web atendendo requisições HTTP
  - banco de dados executando queries
- Redes e Telecomunicações
  - fila de pacotes
  - roteador processando pacotes
  - central telefônica atendeno chamadas 
- Outros Domínios
  - caixa de banco ou supermercado
  - call center com atendentes
 
## O QUE MEDIR (parâmetros) EM UMA FILA

- Para avaliar desempenho e otimizar sistemas, precisamos medir características quantitativas
   - Objetivo: entender como o sistema se comporta e identificar gargalos
 
### Parâmetros Básicos do Sistema

- taxa de chegada (λ), quantos clientes chegam por unidade de tempo
- taxa de atendimento (μ), quantos clientes podem ser servidores por unidade de tempo
- utilização do sistema (ρ), fração do tempo que o servidor está ocupado

### Métricas de Desempenho

- Número médio de clientes no sistema (L)
- Número médio de clientes na fila (Lq)
- Tempo médio no sistema (W)
- Tempo médio na fila (Wq)

### UTILIZAÇÃO DO SISTEMA (ρ)

- representa a fração de tempo que o servidor está ocupado
- $ρ = \frac{λ}{μ}$
- **FUNDAMENTAL PARA ESTABILIDADE** ➔ ρ DEVE ses < 1

### Interpretação

- ρ = 0.5 ➔ servidor ocupado 50% do tempo (SISTEMA ESTÁVEL)
- ρ = 0.8 ➔ servidor ocupado 80% do tempo (SISTEMA SOB PRESSÃO)
- ρ = 0.95 ➔ servidor ocupado 95% do tempo (SISTEMA CRÍTICO)

### Impacto no Desempenho

- ρ < 0.7 ➔ baixo tempo de espera
- 0.7 <=ρ < 0.9 ➔ tempo de espera cresce
- ρ >= 0.9 ➔ alto tempo de espera

## NÚMERO MÉDIO NO SISTEMA E NA FILA

### Número médio no sitema (L)

- quantidade média de clientes no sistema ➔ sendo atendidos + esperando
- $L = \frac{ρ}{1 - ρ} $

### Número médio na Fila (Lq)

- quantidade média de clientes aguardando na fila ➔ exclui quem está sendo atendido
- $Lq = \frac{ρ²}{1-ρ}$

- Relação: $L = Lq + ρ$ ➔ sempre há ' ' clientes sendo atendidos em média
- Comportamento : quando 'p' aumenta, L e Lq crescem rapidamente
- SE ρ = 1, tanto L quanto Lq = ∞

### Tempo Médio no Sistema (W)

- tempo total que um cliente passa no sistema ➔ espera + atendimento
- $W = \frac{1}{μ - λ} $

### Tempo Médio na Fila (Wq)

- tempo que um cliente passa esperando antes de ser atendido, tempo de espera para ser atendido
- $Wq = \frac{λ}{μ(μ - λ)}$

### Lei de Little

- Conecta quantidades médias com tempos médios
- $L = λ * W$
- $Lq = λ * Wq$

## FÓRMULAS PRINCIPAIS DO M/M/1

aqui segue o recapítulo das fórmulas

- Básico
  - λ = taxa de chegada
  - μ = taxa de atendimento
  - ρ = λ/μ (utilização)
- Tempo Médio
  - W = 1/(μ-λ) (no sistema)
  - Wq = λ/(μ(μ-λ)) (na fila)
- Quantidade Média
  - L = ρ/(1-ρ) (no sistema)
  - Lq = ρ²/(1-ρ) (na fila)
- Relações
  - L = Lq+ρ (clientes sendo atendidos em média, ocupação média do servidor)
  - W = Wq+1/μ (tempo total = espera + atendimento)
  - L = λ×W(Lei de Little) 
  - Lq = λ×Wq(Lei de Little)

## Exemplo M/M/1



![WIN_20250701_13_01_48_Pro](https://github.com/user-attachments/assets/667651e0-bd11-483f-91e8-14c764e2af6e)







 
