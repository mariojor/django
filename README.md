# Django
Iniciando estudo do framework

### 1. Configurando ambiente de desenvolvimento
Instale Python e Django. Você pode fazer isso usando pip:
```
pip install django
```
### 2. Configurando ambiente de desenvolvimento
Para criar um novo projeto Django, use o comando:
```
django-admin startproject meuprojeto
cd meuprojeto
```
### 3. Rodar o Servidor de Desenvolvimento
```
python manage.py runserver
```
Agora, você pode acessar http://127.0.0.1:8000 no seu navegador para ver a página inicial do Django.

### 4. Explorar a Estrutura do Projeto
Django segue o padrão de design MVT (Model-View-Template). Familiarize-se com:

- Models: Definem a estrutura dos dados.
- Views: Controlam o que o usuário final vê.
- Templates: São arquivos HTML que permitem a apresentação de dados na interface do usuário.

### 5. Crie sua Primeira Aplicação
Dentro do seu projeto Django, você pode criar apps separadas para diferentes funcionalidades:
```
python manage.py startapp minhaapp
```
### 6. Modelos e Migrações
Defina modelos em models.py de sua app e realize migrações para criar as tabelas no banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```
### 7. Administração
Utilize o painel administrativo do Django para gerenciar os dados. Primeiro, crie um superusuário:
```
python manage.py createsuperuser
```
Depois, acesse http://127.0.0.1:8000/admin para usar o painel administrativo.

### 8. Trabalhar com Views e Templates
Crie views em views.py para definir a lógica de como os dados são processados e apresentados. Use templates para renderizar informações no navegador.

### Exemplo Simples de Modelo (models.py)
```
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
```
Este exemplo define um modelo Post com título e conteúdo, que representam as colunas na tabela de banco de dados correspondente.

