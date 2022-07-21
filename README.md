# desafio_sci_backend

O primeiro passo após clonar o repositório, é  criar um ambiente virtual para rodar o nosso código, isso não é obrigatório, porém é uma boa pratica e 
evita dor de cabeça com projetos futuros ao instalar as dependencias direto na maquina. Para criar o ambiente virtual eu utilizei virtualenv, 
então, dentro do diretório do projeto iremos rodar:

    virtualenv <nome_do_environment>
    source nome_do_environment/bin/activate

Agora já podemos instalar as dependencias do projeto, para isso existem algumas ferramentas que podem ser utilizadas, eu optei pelo pip o 
gerenciador de pacotes mais utilizado do Python, então, dentro do diretório do projeto iremos utilizar o arquivo requirements.txt com o comando:
    
    pip install -r requirements.txt

Instaladas as dependencias, devemos setar as variaveis de ambiente dentro de um arquivo .env, isso ocorre por questoes de segurança, já que algumas
configurações do projeto não devem ficar expostas direto no código em produção, abaixo segue uma configuração de ambiente local para facilitar

    SECRET_KEY=django-insecure-r=-nia^sb_m@_cugtcn_ej&@ep+i3h#lh0%-zgq5!n#2$r6dsi
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    
Lembrando que não estou passando uma configuração de banco de dados, pois estou utilizando uma configuração que cria um banco sqlite para utilização local 
caso não exista uma configuração previa nas variaveis de ambiente. Após isso podemos rodar os comandos para criar as tabelas do banco:

    python manage.py migrate
    
E em seguida subir o servidor com:

    python manage.py runserver
    
Agora o servidor já está no ar :)
