# Atividade Ponderada - Projeto em Flask com interface de controle do robô

Desenvolvido por Isabelle Beatriz Vasquez Oliveira

## Como executar o programa

&emsp;Para acessar a interface e executar cada uma das rotas, você deve instalar todos os requisitos do arquivo "requirements.txt" por meio do terminal com o comando "pip install -r requirements".

&emsp;Depois de garantir que todas as instalações foram realizadas, o usuário deve executar o arquivo app.py, onde terá acesso à interface que comanda as rotas do projeto. Nele, o primeiro botão que o usuário vai encontrar é o "Clique aqui para ver os Logs do sistema", que redireciona para a rota "/logs" que mostra todos os comandos utilizados por usuários e salvos no banco de dados, como "home" e coordenadas em geral. O segundo botão é o "Home", que redireciona para a rota "/home" e executa as coordenadas para movimentação até a posição de segurança, home. A terceira interação com o dashboard é um tipo de "form" que necessita que o usuário insira as coordenadas para X, Y, Z e R e clique no botão "Mover" para iniciar a movimentação do robô para essas coordenadas.

&emsp;Essa aplicação foi desenvolvida utilizando as seguintes ferramentas: TinyDB, JSON, Flask, HTML, HTMX e CSS, além da biblioteca do PyDobot para movimentação do robô.

&emsp;O HTMX foi utilizado para chamada de rotas no HTML e para a criação de um componente "log", para acessar as informações do banco de dados e devolvê-las na interface quando a rota for requisitada.

&emsp;O vídeo de demostração da aplicação funcionando pode ser encontrado no link a seguir: [Vídeo de demonstração](https://youtu.be/8lyCWapT27o?si=vcvPwo94jI0iOizm). 




