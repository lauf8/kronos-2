# Kronos
Kronos é uma rede social de gestão de tempo desenvolvida como projeto de TCC. Esta aplicação permite criar rotinas e compartilhá-las com um grupo de pessoas, facilitando a organização e o gerenciamento do tempo.

# Tecnologias Utilizadas
Linguagem de Programação: Python
Framework Web: Django
Banco de Dados: PostgreSQL
Containerização: Docker, Docker Compose

# Funcionalidades Principais
1. Criação de rotinas personalizadas
2. Compartilhamento de rotinas com grupos de pessoas
3. Interface amigável e intuitiva para gerenciamento de tempo

# Instruções de Instalação
Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

Instalação do Dokcer:
<https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04>

Passos para Instalação
Clone este repositório:

```git
git clone https://github.com/lauf8/calendar-django
```
```bash
cd kronos
```

Execute o Docker Compose para iniciar os containers:

```dockerfile
docker-compose up -d
```

Acesse o container do PostgreSQL e crie o banco de dados:

```dockerfile
docker exec -it <nome-do-container-postgres> psql -U postgres
```

```postgresql
psql -h localhost -p 5432 -U myuser -d mydatabase
```
Coloca a senha que foi definida.

```postgresql
CREATE DATABASE kronos;
exit;
```

Acesse o container do Django e execute as migrações e a coleta dos arquivos estáticos:

```dockerfile
docker exec -it <nome-do-container-django> /bin/bash
```

```py
python manage.py migrate
python manage.py collectstatic
exit
```

A aplicação estará disponível em http://localhost:8000.

# Instruções de Uso
Acesse a aplicação no navegador através do endereço http://localhost:8000.
Crie uma conta e faça login.
Navegue até a seção de rotinas para criar novas rotinas.
Compartilhe suas rotinas com outras pessoas e gerencie seu tempo de forma eficiente.
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

# Licença
Este projeto está licenciado sob a MIT License.