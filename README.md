# Teste Tradex
Desafio técnico para processo seletivo para vaga de Desenvolvedor Fullstack na Tradex

## Objetivos
Desenvolver API usando Python e Django capaz de:
*  Realizar CRUD de produtos
*  Visualizar a variação de preço dos produtos com o tempo

## Execução do ambiente de desenvolvimento
### Utilizando o Docker
Faça o pull ou build da imagem
```bash
docker pull 0xb074/tradex-backend
```
Clone o repositório e rode o container com o comando:
```bash
git clone https://github.com/thiago4455/test-tradex/
cd test-tradex/
docker run --rm -ti -p 8000:8000 -e UID=$(id -u) -e GID=$(id -g) -v "$PWD":/home/tradex/work 0xb074/tradex-backend
```
Ele já iniciará um terminal rodando a aplicação. Caso precise rodar algo dentro do ambiente do container, basta dar um Ctrl-C e acessar a linha de comando.
O banco de dados é importado durante o build da imagem, e as alterações são apagadas juntamente com o encerramento do container. Para persistir os dados do banco, crie um volume no docker, e rode com o seguinte termo adicional:
```bash
docker volume create postgres_data
docker run --rm -ti -p 8000:8000 -e UID=$(id -u) -e GID=$(id -g) -v "$PWD":/home/tradex/work -v postgres_data:/var/lib/postgresql/14/main 0xb074/tradex-backend
```

### Utilizando venv
Instale a versão correta to python e postgres:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.11 python3.11-venv postgresql
sudo systemctl enable postgresql --now
```
Crie uma env para o projeto, e instale os requirements:
```bash
mkdir ~/.venv/ && cd ~/.venv/
python3.11 -m venv tradex
source tradex/bin/activate
cd /diretorio/do/repositorio/clonado
pip install -r /tmp/requirements/requirements.txt
```

Crie um banco de dados e importe o dump:
```bash
sudo -u postgres createdb tradex
cat /tmp/dump.db | sudo -u postgres psql tradex
```
Inicie o projeto
```
python manage.py 0.0.0.0:8000
```

## Implementação
Além das operações básicas de CRUD, para que fosse possível realizar o controle da variação de preço, as ofertas são definidas em uma tabela separada das informações do produto.

O cadastro de produtos e ofertas pode ser feito pelo painel de admin (pela rota `/admin`), assim como via API.

### Painel de administração
![image](https://github.com/thiago4455/test-tradex/assets/29243304/632f6158-5d9d-4561-87af-a4e152e3ddaf)

Através desse painel também é possível visualizar a variação de preço de um produto especifico
![image](https://github.com/thiago4455/test-tradex/assets/29243304/f9c79f47-fd1b-414d-ab17-f725612544fc)



### Documentação da API
Documentação Swagger da API através da rota `/api/docs`

### Dump do banco de dados
Dados de teste disponíveis em [dump.db](https://github.com/thiago4455/test-tradex/blob/master/dump.db)

(Usuário e senha do `/admin`: admin:admin)


### Modelo dos dados
![image](https://github.com/thiago4455/test-tradex/assets/29243304/b77a0f3e-99ed-4520-ae46-b45a01cb4e06)
