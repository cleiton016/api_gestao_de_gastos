# API Gestão de Gastos

#### Clone o Repositório

`git clone -b <branch> <link do repositório>`

#### Instale as dependências

`pip install -r requirements.txt`

Caso ocorra algum erro na instalação do `psycopg2` [aqui](https://cursos.alura.com.br/forum/topico-erro-ao-instalar-psycopg2-117198) esta uma possivel solução

#### Criando Arquivo env

Na base do projeto crie uma arquivo chamado `.env`.

Esse é um exemplo de um arquivo env.

> DEBUG=
>
> SECRET_KEY=
>
> DB_NAME=
>
> DB_HOST=
>
> DB_USER=
>
> DB_PASSWORD=
>
> DB_PORT=

#### Criando as Migrações

Abra o terminal na raiz do projeto e execute os seguintes
comandos.

* *Para checar as alterações*

  `python manage.py makemigrations`
* *Para efetuar as migrações*

  `python manage.py migrate`

#### Rodando o Projeto

`python manage.py runserver`

Projeto estará disponível em: [localhost:8000](https://localhost:8000)
