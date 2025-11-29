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

### Comandos

$ docker --version

$ docker run hello-world 
//instalar container 'hello-world'

$ docker ps 
//visualizar os containers rodando

$ docker ps -a 
//visualizar os containers que foram rodados e estão rodando

$ docker run ubuntu

$ docker run -it ubuntu bash 
//it - iterator
//serve para rodar o ubuntu, especificadamente bash

$ docker run -it -d ubuntu bash
//para rodar (-it) com processo em segundo plano (-d) no formato bash (bash)

$ docker exec -it (codigo_id_ubuntu) bash
// para executar o ubuntu bash

$ docker stop a2a
// paramos o container
// podemos verificar com "docker ps" 

---

- instalar um repositorio

$ git --version
// checagem da verson

$ git clone (link_repositorio)
// para puxar o repositorio para nosso docker

$ ls
//

$ cd Docker-Course-Exemple-Api-Spring/
//

##### Criando um Dockerfile

FROM maven:4.0.0-rc-5-eclipse-temurin-17 AS build

COPY src/app/src
COPY pom.xml/app

WORKDIR /app
RUN mvn install

FROM openjdk:17-ea-slim
COPY --from=build/app/target/${app-name-snapshot}.jar /app/app.jar
# no java o $(app-name) é composto pelo ${artifactid)-${version}
# ele concatena isso com traço ' - '

WORKDIR /app
EXPOSE 8080
# vou utilizar a porta 8080 


# devemos especificar que, a porta 8080 vai apontar -> para a porta 'x' docker


CMD["java,"-jar","app.ja"]
# espeficicar os comando que vão ser rodados para funcionamento da aplicação

### Comandos

$ git pull origin main

$ docker build -t hello-world:1.0 .
//

$ docker run -it -d hello-world:1.0
//hello-worl:1.0  == name-tag

$ docker image ls
//

$ docker rmi -f (id_image)
//rmi - remove image
//-f -para forçar execução

$ docker stop (id)
// parando o run para configurar a porta

$ docker run -it -d -p 8080:8080 hello-world:1.0
//configurada a porta 

---
nao sei mais me perdi 

















