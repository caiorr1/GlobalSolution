Olá, seja bem vindo!

Esse projeto está sendo criado para uma entrega da faculdade.

Nossa ideia é cadastrar Pessoas Fisicas e Empresas que estejam dispostas a doar alimentos.
E também cadastrar ONGs, que receberiam esses alimentos.
Além de termos a IA integrada para falar um pouco sobre a agricultura sustentável!
-------------------------------------------------------------------------------------------

O programa está organizado por pastas. Na pasta "Json" estão os arquivos Jsons que são usados para o cadastro dos usuários e posteriormente acessados.
Na pasta "Doadores" existem os arquivos .py das Empresas, ONGs e PessooaFisica separados, dentro deles existem outras chamadas para funções que estão em outra pasta.
Na pasta "funcoes" acontece todo funcionamento do programa. Dentro dessa pasta tem diversos arquivos com o nome de "autodefs", dentro desses arquivos existem funções
que são essenciais para o programa rodar. Seguindo pelo padrão de nome, "autodefs_empresas" seriam as funcoes das empresas, que são chamadas no empresas.py, e assim sucessivamente.
Isso tudo foi separado dessa forma pois acreditei que o programa ficaria mais organizado e entendivel. 
Dentro de cada arquivo .py na pasta "funcoes" existem funções com funcionalidades especificas para separar caso o usuário seja uma ONG, Empresa ou PessoaFisica, e executarem o que é preciso.
Ainda na pasta "funcoes" existem alguns arquivos diferentes. Seriam eles "formatacao.py" -> usado somente para formatar alguns textos de forma mais rápida; E
"iachat.py" -> esse arquivo roda todo o funcionamento da requisição na API do ChatGPT. QUANDO FOR USA-LA, ABRA O ARQUIVO "api_key.txt" E COLOQUE A SUA API_KEY, NADA MAIS!.
E por último o arquivo "admin.py" -> basicamente esse arquivo serve para fazer um match entre os jsons.
Para rodar o programa você deve inicia-lo pelo arquivo "main.py" e correr para o abraço! 

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Não se esqueça, caso queira utilizar a IA, você deve preencher o txt "api_key"
com a sua chave. Caso não preencha, o mesmo não conseguirá rodar o código.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

----------------------------------------
Integrantes do Grupo: 
Caio Ribeiro Rodrigues, RM 99759 
Henrique Lopes, RM 550279 
Eduardo Jablinski, RM 550975
Natalia Scigliano, RM 98430
Felipe Sieiro Paim dos Santos, RM 98349


