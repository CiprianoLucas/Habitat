# Centro de Chamados para Condomínios
A aplicação tem como objetivo criar um centro de chamados de manutenção e reclamação para condomínios, utilizando Django Rest Framework para o backend e Vue 3 para o frontend.

## Propósito
O objetivo deste projeto é facilitar a comunicação entre os residentes de um condomínio e os responsáveis pela gestão, permitindo a criação e acompanhamento de chamados de manutenção e reclamação. A aplicação busca agilizar a resolução de problemas, melhorar a organização interna e proporcionar maior transparência no gerenciamento das demandas dos residentes.

## Funcionalidades
- Cadastro e Login de Usuários: Os usuários podem se registrar e fazer login para acessar o sistema.
- Criação de Chamados: Os residentes podem criar chamados de manutenção e reclamação.
- Acompanhamento de Chamados: Os usuários podem visualizar e acompanhar o status de seus chamados.
- Gestão de Chamados: Os gestores do condomínio podem gerenciar e responder aos chamados.
## Tecnologias Utilizadas
- Backend:
    - Django Rest Framework
- Frontend:
    - Vue 3
    - Bootstrap
    - Axios
- Infraestrutura:
    - Docker
    - PostgreSQL

## Instalação
### Pré-requisitos
- Docker

### Clonando o Repositório

```bash
git clone https://github.com/CiprianoLucas/meus-lares.git
cd meus_lares
```

### Fazendo funcionar
Com docker em funcionamento, execute o comando para criar o container
```bash
docker compose up -d --build
```

Na primeira vez será necessário efetuar as migrações, então faça.
```bash
docker exec -it api /bin/bash
python manage.py migrate
```

Se mexer em algum model, será necessário efetuar as configurações dos migrations, então execute

```bash
docker exec -it api /bin/bash
python manage.py makemigrations
python manage.py migrate
```


## Configuração
- Configure as variáveis de ambiente necessárias, como credenciais do banco de dados e chaves secretas, utilize os arquivos .exaple_env para criar um .env

- Certifique-se de que o backend e o frontend estejam apontando para os respectivos servidores e endpoints.

## Como Executar
Após realizar a instalação e configuração, execute o servidor backend e frontend como descrito acima. Acesse a aplicação em http://localhost:{INTERFACE_PORT} para utilizar o frontend e http://localhost:{API_PORT}/admin para gerenciar o backend.

