# Sistema de Gestão de Tarefas (ProTask)

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Django](https://img.shields.io/badge/django-5.1-green.svg)

**Trabalho da disciplina Programação Web - GAC116**

**Integrantes:**

* Lislaila Tarsila Pereira
* Lucas Malachias Furtado
* Luiz Filipe Bartelega Penha

**Universidade Federal de Lavras**

---

## 📖 Descrição do projeto

O **ProTask** é um sistema web de Gestão de Tarefas, desenvolvido com o framework **Django**. Ele oferece uma interface simples, moderna e eficiente para criar, gerenciar e acompanhar projetos e tarefas, facilitando a colaboração entre equipes e a organização de atividades pessoais ou profissionais.

O sistema conta com um design responsivo, tema claro/escuro e uma estrutura organizada para proporcionar a melhor experiência ao usuário.

---

## ✨ Funcionalidades

* **Autenticação de Usuários:** login, cadastro e logout.
* **Gerenciamento de Projetos:**

  * Criação, edição e exclusão.
  * Nome, descrição e tags.
  * Associação de membros.
* **Gerenciamento de Tarefas:**

  * Criação, edição e exclusão dentro de um projeto.
  * Atribuição a membros específicos.
  * Status (`To Do`, `Em andamento`, `Feito`) e prazo final.
* **Sistema de Tags:** para categorização e busca.
* **Colaboração:** adição e remoção de membros em projetos.
* **Interface Moderna:**

  * Tema claro/escuro persistente via `localStorage`.
  * Responsividade com **Bootstrap 5**.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
* **Banco de Dados:** SQLite (padrão do Django)

---

## 📦 Estrutura do Projeto

```bash
sistema_gestao_tarefa/
│
├── controle_tarefa/      # App principal: projetos, tarefas e tags
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── usuarios/             # App para autenticação de usuários
│   ├── templates/
│   └── ...
│
├── sistema_gestao_tarefa/ # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── staticfiles/          # Arquivos estáticos (CSS, JS)
└── manage.py
```

---

## 📋 Como Executar o Projeto

### 1. Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/)
* `pip` (gerenciador de pacotes Python)

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/gestao_tarefas.git
cd gestao_tarefas/sistema_gestao_tarefa
```

### 3. Crie e Ative um Ambiente Virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as Dependências

> Recomenda-se criar um `requirements.txt`.
> Por enquanto, instale manualmente:

```bash
pip install Django django-extensions
```

### 5. Aplique as Migrações

```bash
python manage.py migrate
```

### 6. Crie um Superusuário

```bash
python manage.py createsuperuser
```

Preencha usuário, e-mail (opcional) e senha.

### 7. Rode o Servidor

```bash
python manage.py runserver
```

### 8. Acesse no Navegador

```
http://127.0.0.1:8000/
```

---

## 🗃️ Modelo do Banco de Dados
Abaixo está a representação gráfica da estrutura dos modelos do projeto:

![Estrutura dos Modelos](modelo.png)

---

## 📄 Licença

Este projeto está sob a licença **Apache 2.0**.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
