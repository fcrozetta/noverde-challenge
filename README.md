# noverde-challenge
[Link desafio noverde](https://github.com/noverde/challenge)

## QuickStart
Para testar as funcionalidades, criei um aplicativo simples, sem validação que envia e armazena o id para consulta posterior. para utilizá-lo, [Clique Aqui](https://master.d3d7ytfa9zwsyd.amplifyapp.com/).

Outra forma de usar é realizando as chamadas diretamente para o endpoint realizando chamadas para o endpoint https://5jnri10wlk.execute-api.us-west-2.amazonaws.com/testing

## Organização do repositório
os primeiros níveis de diretório indicam sua função:
  
  - schemas: schemas usados dentro do gateway para validar as requisições
  - openAPI: Documentação para testes usando ferramentas como Postman, ou insomnia.
  - lambdas: Contém diretórios referentes aos diretórios no lambda. Cada diretório dentro de **1.lambdas** se refere a uma function no AWS
  - noverde-frontend: source do PWA sendo executado para testar as funções.

## Workflow

### GET(id)

O endpoint começa na API Gateway, validando se o usuário possui o parâmetro na url. Se não possuir, retorna erro 400. Se possuir, direciona para o lambda noverde-loan-id-get, que executa a busca customer no DB para retornar para o client.

### POST

O endpoint começa com API Gateway validando o schema, de acordo com o arquivo *LoanRequest.json*, localizado no diretório 0.schemas. Se a validação estiver correta, os dados são direcionados para a função lambda *noverde-post*. Nesta função doi eventos ocorrem, a gravação inicial do usuário no banco de dados, e o disparo de uma mensagem no SQS. Apesar de ser possível o envio de todo o conteúdo nas mensagens SQS, a escolha de inserir no banco para consulta foi tomada para evitar conflitos na busca dessa informação, tendo em vista que o SQS esconde as mensagens da fila quando elas estão em processamento.

## Processing

O processamento se inicia com um gatilho do SQS, que envia a mensagem como um parametro em events, na função handler. Como esse gatilho não ocorre em ambientes locais, uma forma alternativa de buscar a mensagem foi implementada. Se não for possível receber a mensagem via parametro, será realizada uma tentativa pela chamada da queue via software.

Devido a essa automação de envio e processamento de informação, não é necessaario implementar ferramentas exteras, como celery.


## Documentação
A Documentação interna no código conta com docstrings, typing e tipos de parâmetros, para facilitar o desenvolvimento com ferramantas para linting e autocomplete.


## Observações

No repositório estão marcadas as alterações realizadas no código com o passar do tempo. Também está marcado em qual commit foi realizado o envio para a AWS.
