

 Processo seletivo programador - be3 health tech



## Descrição do Projeto 📄

<p>Um usuário deve conseguir cadastrar um novo paciente e editar um paciente existente mas não deve ser
possível excluir um cadastro.</p>

Versão do python utilizada no projeto: ![Python 3](https://img.shields.io/badge/python-3.8-blue.svg)



## Instalação 🛠️

Faça o clone do projeto.

```python
git clone https://github.com/Erickson-lopes-dev/be3-health-tech_Teste
cd be3-health-tech_Teste
```



Crie uma maquina virtual  para rodar o projeto.

```python
python3 -m venv venv
```

Uma vez criado seu ambiente virtual, você deve ativá-lo.

No Unix ou no MacOS, executa:

```
source venv/bin/activate
```

No Windows, execute:

```python
venv\Scripts\activate.bat
```



Com o ambiente virtual ativado, Instale as dependências (certifique-se de que esteja na mesma pasta que o arquivo).

```python
pip install -r requirements.txt
```



Antes de iniciar o projeto é necessário fazer as migrações das tabelas.

```
py manage.py migrate
```



E também criar um usuário !

```python
py manage.py createsuperuser

>>> Usuário (leave blank to use 'ofcer'):
>>> (Digite um nome de usuário apra login)

>>> Endereço de email:
>>> (Digite um enredeço de email)

>>> Password:
>>> (Digite uma senha)

>>> Password (again):
>>> (Digite novamente a senha)
```

Agora  que instalamos tudo, podemos iniciar !

## Exemplo de Funcionamento

Execute o arquivo do programa.

```python
py manage.py runserver

Após, basta clicar no link para ser redirecionado para o navegador
>>> http://127.0.0.1:8000/
```



Digite o nome do usuário e senha que foi criado para logar no sistema e clique em login.

![image](https://user-images.githubusercontent.com/62525983/120267817-18eec800-c27b-11eb-8db8-4b5ade93c1fe.png)


Ao logar podemos nos deparamos com a dashboard do sistema, onde é possível observar a quantidade total de paciente e estatisticas que demostram a porcentagem que convênio tem referente ao todo.

![image](https://user-images.githubusercontent.com/62525983/120267867-32900f80-c27b-11eb-8bc6-ef73534a5203.png)


Clique em qualquer um dos lugares indicado,  você será redirecionado para onde se localiza uma lista que armazenará alguns dados dos pacientes para realizar pesquisas.

![image](https://user-images.githubusercontent.com/62525983/120267915-48053980-c27b-11eb-81e0-36d0e5df952e.png)



Aqui sera exibido a lista com todos os dados disponiveis, onde é possível pelas barras de pesquisa encontrar um paciente digitando qualquer dados da coluna referente ao paciente.

![image](https://user-images.githubusercontent.com/62525983/120267959-60755400-c27b-11eb-95d2-0a13bd0b86c0.png)


Clique em qualquer um dos lugares indicado,  você será redirecionado para página de adicionar novo registro de paciente

![image](https://user-images.githubusercontent.com/62525983/120268013-75ea7e00-c27b-11eb-9f0e-8c52342647d4.png)

(Redimensionei a tela para melhor visualização )

![image-20210601012039835](![image](https://user-images.githubusercontent.com/62525983/120268046-84389a00-c27b-11eb-804b-a5cbb0003be2.png)
)

![image](https://user-images.githubusercontent.com/62525983/120268067-8dc20200-c27b-11eb-9f8c-5bd3d0067a98.png)


Na lista é possível obter todos os dados do paciente clicando no nome

![image](https://user-images.githubusercontent.com/62525983/120268182-c19d2780-c27b-11eb-86ab-713cf40f48f0.png)


![image](https://user-images.githubusercontent.com/62525983/120268231-d5e12480-c27b-11eb-9069-5af0b7252869.png)



E se caso você deseje editar os dados, temos duas opções para isso !

![image](https://user-images.githubusercontent.com/62525983/120268270-e7c2c780-c27b-11eb-87ec-628977a2881d.png)


Basta clicar e você sera redirecionado para o formulario, basta alterar os dados e salvar !

![image](https://user-images.githubusercontent.com/62525983/120268316-f6a97a00-c27b-11eb-8de3-0b430c23fc98.png)


e se olhar a dashboard, toda ação ja começou a acontecer, possível ver quais convênios os clientes mais usam!

![image](https://user-images.githubusercontent.com/62525983/120268352-045eff80-c27c-11eb-9512-641aa92f1053.png)




