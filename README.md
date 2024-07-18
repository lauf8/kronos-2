# Kronos
Kronos é uma rede social de gestão de tempo desenvolvida como projeto de TCC. Esta aplicação permite criar rotinas e compartilhá-las com um grupo de pessoas, facilitando a organização e o gerenciamento do tempo.

# Tecnologias Utilizadas
Linguagem de Programação: Python
Framework Web: Django
Banco de Dados: PostgreSQL
Containerização: Docker, Docker Compose
Funcionalidades Principais
Criação de rotinas personalizadas
Compartilhamento de rotinas com grupos de pessoas
Interface amigável e intuitiva para gerenciamento de tempo
Instruções de Instalação
Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

Passos para Instalação
Clone este repositório:

git clone https://github.com/lauf8/calendar-django
cd kronos
Execute o Docker Compose para iniciar os containers:

docker-compose up -d
Acesse o container do PostgreSQL e crie o banco de dados:

docker exec -it <nome-do-container-postgres> psql -U postgres
CREATE DATABASE kronos_db;
\q
Acesse o container do Django e execute as migrações e a coleta dos arquivos estáticos:

docker exec -it <nome-do-container-django> /bin/bash
python manage.py migrate
python manage.py collectstatic
exit
A aplicação estará disponível em http://localhost:8000.

# Instruções de Uso
Acesse a aplicação no navegador através do endereço http://localhost:8000.
Crie uma conta e faça login.
Navegue até a seção de rotinas para criar novas rotinas.
Compartilhe suas rotinas com outras pessoas e gerencie seu tempo de forma eficiente.
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a MIT License.