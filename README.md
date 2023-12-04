# Teste Tradex
Desafio técnico para processo seletivo para vaga de Desenvolvedor Fullstack na Tradex

## Objetivos
Desenvolver API usando Python e Django capaz de:
*  Realizar CRUD de produtos
*  Visualizar a variação de preço dos produtos com o tempo

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
