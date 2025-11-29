# Docker

### Maquina Virtual

- 1960
  - Desenvolvimento da máquina CP40 pelo centro ciêntifico de Cambdridge da IBM
  - Surgiu então este objetivo de simular outras máquinas dentro de uma só
-  1967
  - Fabricação do protótipo 
- 1998
  - Ideia chega aos PCs comuns

Atualmente as mais populares IaaS (Infrastructure As A Service):
- Azure VMs
- EC2 (amazon)

## E o Docker?

Criado por Solomon Hykes enquanto trabalhava na dotCloud em 2013, a ideia é armazenar nossa aplicação + uma lista de requisitos
necessários para rodar, o Docker carrega tudo.

Objetivo de criar uma ferramente que permitisse que desenvolvedores criassem, testassem e executassem aplicações em diferentes
plataformas de maneira consistente.

### oque é?
- Serviço de Virtualização
- Deploy da aplicação contendo todas as dependências necessárias para a execução da aplicação
- Separa as aplicações em containers
- Utiliza o Sistema Operacional hospedeiro  
  - por isso o Docker tecnicamente NÃO é uma máquina virtual, pois faz uso de Sistema Operacional alheio 

### Funcionamento

Docker File -> Docker Image (cópia) -> Docker Container (armazenamento fechado da aplicação em container)

### Para que usar?

Para evitar o "na minha máquina funciona" tornando a aplicação flexivel para trasnporte de máquinas já que carrega consigo 
tudo que é necessário para rodar

## Prática

#### Docker Hub

Básicamente o Github do Docker































