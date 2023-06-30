Capítulo. Desenvolvimento de Software - Padrões de frontend. SPA. PWA. Ajax. Angular, VueJS e React. NodeJS, Express.


Índice

1) AJAX- Teoria

2) AJAX - Questões Comentadas.

3) AJAX - Lista de Questões.

4) SPA - Teoria

5) Vue.JS -100% - Teoria

6) Vue.JS -100% - Questões Comentadas.

7) Vue.JS -100% - Lista de Questões.

8) ReactJS - Teoria

9) ReactJS - Questões Comentadas.

10) ReactJS - Lista de Questões.

11) AngularJS

12) AngularJS - Questões Comentadas.

13) AngularJS - Lista de Questões.

14) NodeJS - Teoria

15) WebPackJS - Teoria

16) WebPackJS - Questões Comentadas.

17) WebPackJS - Lista de Questões.

18) WebSocket - Teoria

19) WebSocket - Questões Comentadas.

20) WebSocket - Lista de Questões.

21) PWA-Teoria

22) PWA - Questões Comentadas.

23) PWA - Lista de Questões.

*


Conceitos Básicos

AJAX

INCIDÊNCIA EM PROVA: MÉDIA

O desenvolvimento de aplicações desktop apresenta uma riqueza que, por muito
tempo,
pareceu fora do alcance das aplicações web, gerando um gap no nível de experiência do usuário
com a aplicação. A riqueza de interação e o grau de responsividade das aplicações
desktop davam
um banho nas aplicações web, mas esse gap diminuiu com a criação do AJAX!

Professor, AJAXé uma tecnologia? Não, é um conjunto de tecnologias, cada uma com seu
propósito,
que se juntam harmonicamente para melhorar a experiência do usuário, tornando
páginas web
mais ricas e interativas. Professor, que tecnologias são essas? Jessé Garret, criador
do AJAX,
afirmou em um artigo que ela incorpora as seguintes tecnologias:

Apresentação: utiliza XHTML e CSS;

Interação e Exibição dinâmicas: utiliza DOM;

Manipulação e Intercâmbio de Dados: utiliza XML e XSLT;

Recuperação Assíncrona de Dados: utiliza XMLHttpRequest;

e JavaScript para reunir todas essas tecnologias.

Vamos ver rapidamente cada uma dessas tecnologias:

TECNOLOGIAS | DESCRIÇÃO
|

XHTML Trata-se de uma linguagem de marcação que estende o HTML para criação de páginas web de
forma mais acessível e interoperável.

CSS Trata-se de uma linguagem de folhas de estilo utilizada para definir a
apresentação de
documentos escritos em uma linguagem de marcação.

DOM Trata-se de um modelo de objetos de documentos para criação de interfaces
dinâmicas e
editáveis independentes de linguagem e plataforma.

XML Trata-se de uma linguagem de marcação para propósitos especiais de
intercâmbio e
compartilhamento de dados.

XSLT Trata-se de uma linguagem de marcação usada para transformar documentos XML em outros
documentos ou objetos.

XMLHTTPREQUEST Trata-se de um objeto utilizado para enviar e receber requisições HTTP
assincronamente.

JAVASCRIPT Trata-se de uma linguagem de programação de scripts interpretada e client-side.

Galera, um modelo de aplicação web clássica funciona mais ou menos assim: o usuário
envia
uma Requisição HTTP ao Servidor Web. Esse realiza algum tipo de processamento (recupera
dados, manipula números, etc) e retorna uma Página HTML ao cliente. Essa abordagem faz
muito
sentido, mas não oferece uma boa experiência ao usuário.

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)


user interface

JavaScript call 1 I

| HTML+CSS data
user interface

HTTP r cquest

HTML+CSS data

▼

Ajax engine


HTTP rcqucst

XML data

V


web server
i f
datastoces, backend
processing. legacy systems
classic
web application model
web and/or XML server
datastores, backend
proccssing, legacy systems

Ajax
web application model

O que faz o usuário enquanto o servidor está realizando seus processamentos? Nada, só espera! E, a
cada nova tarefa, espera novamente. Quem aí gosta de esperar? Quem curte um belo chá-de-cadeira?
Ninguém! Por que toda vez que o usuário requisitar algo é obrigatório que haja uma
interrupção na
interface? Ora, uma vez que a interface foi carregada, o usuário está pouco se
importando com
o resto.

As Aplicações AJAX eliminam esse inicia-interrompe-inicia-interrompe ao introduzir
uma camada
chamada Engine AJAX entre o usuário e o servidor! Em vez de carregar uma página web,
ao iniciar
a sessão, o navegador carrega a Engine AJAX (escrita em JavaScript). Ela permite que
a interação
do usuário com a aplicação ocorra de forma assíncrona - independente de comunicação
com o
servidor.

Portanto, o usuário jamais fica olhando para uma tela branca do navegador, sem fazer
nada e
esperando que o servidor faça seu trabalho. Toda ação do usuário que normalmente gera
uma
Requisição HTTP se transforma em uma chamada JavaScript à Engine AJAX. Qualquer resposta
que não requeira uma viagem de volta ao servidor (Ex: validação de dados, etc) é
manipulada
pela própria Engine AJAX.

Se ela necessitar de alguma coisa do servidor, a Engine AJAX realiza as
requisições
assincronamente, geralmente utilizando XML - sem enrolar a interação do usuário
com a
aplicação. A imagem abaixo apresenta a diferença entre uma aplicação web clássica que
utiliza uma
comunicação síncrona com o servidor e uma aplicação web AJAX que utiliza uma
comunicação
assíncrona com o servidor.


classic web application model (synchronous)

Ajax web application model (asynchronous)

processmg proccsslng proccssing processog

O Objeto XMLHttpRequest é utilizado para trocar dados com o servidor de forma
assíncrona.
Alguns dizem que ele é o sonho de um desenvolvedor, porque pode-se atualizar uma
parte de uma
página web sem precisar recarregar a página inteira; é possível requerer e receber
dados do servidor
após a página ser carregada; e é possível enviar dados ao servidor em background.

Todos os navegadores modernos (IE7+, Firefox, Chrome, Safari e Opera) possuem uma
Objeto
XMLHttpRequest embutido. A sintaxe para criá-lo é bem simples:

xmlhttp = new XMLHttpRequest();

Todos os navegadores modernos possuem um Parser XML! Ele converte um documento XML
em um DOM, que pode ser manipulado com JavaScript. Ele define uma forma padrão de
acessar
e manipular documentos XML de maneira hierárquica. Dessa forma, todos os elementos
podem ser
acessados por meio da Árvore DOM!

Para capturar a resposta do servidor, existem duas possibilidades: utilizar as
propriedades
responseXML ou responseText. O segundo recupera dados como uma string, em forma de
texto; e o
primeiro recupera dados como um Objeto DOM, em formato XML! É possível, ainda, capturar
dados em outros formatos, tais como: HTML e JSON!


No AJAX, o objeto XMLHttpRequest possui diversas propriedades importantes para realizar a
comunicação com o servidor. Quando uma solicitação para um servidor é enviada,
normalmente
deseja-se executar algumas ações com base na resposta. Existe um
evento chamado
onreadystatechange, responsável por especificar o que vai acontecer quando o servidor
processar a
resposta. Há três propriedades:

Onreadystatechange: armazena uma função a ser chamada de forma automática cada vez
que a propriedade readyState mudar;

readyState: armazena o status do XMLHttpRequest.

o o: Requisição não iniciada;

o i: Conexão com servidor estabelecida;

o 2: Requisição recebida;

o 3: Requisição processada;

o 4: Requisição finalizada e resposta pronta.

Status:

o 200: "Ok".

o 404: Página não-encontrada.

AJAX apresenta uma grande desvantagem: se o usuário desativar o JavaScript de
seu
navegador, a aplicação pode parar de funcionar. No entanto, há diversas vantagens:
executa
processos em paralelo às requisições/respostas; manipula XML nas aplicações para
desktop de
forma simples; troca mensagens de forma assíncrona; entre outras.

Por fim, alguns desenvolvedores utilizam iFrames para embutir aplicações interativas em
páginas
web, incluindo aquelas que empregam AJAX (Ex: Google Maps). O iFrame é utilizado para
embutir
um Documento HTML em outro Documento HTML. Ele é frequentemente utilizado também para
inserir conteúdo de outra fonte (como uma propaganda) em uma página web.

(UFRJ -2012) Considere o desenvolvimento de aplicações web com Ajax (Asynchronous
Javascript and XML).

I - O objeto XMLHttpRequest desempenha importante papel, estando relacionado à
comunicação assíncrona com o servidor web.

II - Para utilizar Ajax é preciso antes instalar e configurar um servidor Ajax, o qual
interage com o servidor web.

III - Uma das características de Ajax é a exibição dinâmica de dados e uso do modelo de
objetos DOM (Document Object Model).


Podemos afirmar que:

a) somente as alternativas I e II estão corretas.

b) somente a alternativa I está correta.

c) somente a alternativa II está correta.

d) somente as alternativas I e III estão corretas.

e) somente as alternativas II e III estão corretas.

Comentários: para solicitar dados de um servidor web, utiliza o objeto XMLHttpRequest, logo a I
está correta. A II está errada,
porque não temos esse requisito em momento algum. A III está correta, o AJAX usa exibição dinâmica
de dados e emprega o
DOM (Document Object Model) (Letra D).

(CCV - 2019) Uma das formas de desenvolver uma página dinâmica é através do uso de
AJAX (Asynchronous JavaScript and XML), onde ele é utilizado para atualizar apenas
parte da página Web. Sobre o AJAX, é correto afirmar:

a) o AJAX baseia-se em tecnologias já disponíveis no lado cliente da navegação Web,
entre elas a linguagem JavaScript.

b) para que o cliente usufrua dos benefícios do AJAX, é necessária a instalação de um
programa AJAX específico para cada tipo de plataforma.

c) quando o AJAX é utilizado, todas as requisições enviadas ao servidor são assíncronas
devido a limitação imposta pelo protocolo da camada de aplicação.

d) o AJAX utiliza um protocolo proprietário para a troca de informações do cliente com
o servidor, não sendo possível saber como esse procedimento é realizado.

e) para mantero conteúdo da página atualizado, o servidormantém uma sessão síncrona
com o cliente utilizando o protocolo SMTP (Simple Mail Transfer Protocol), permitindo
a troca mais rápida de informações.

Comentários: vamos por partes: (a) Correto. AJAX baseia-se em tecnologias do lado cliente,
entre elas 0 Javascript, conforme
vimos; (b) Errado. Não existe isso de instalar um programa AJAX, os navegadores que utilizam 0
AJAX; (c) Errado. AJAX suporte
requisição síncrona, logo não faz sentido essa alternativa; (d) Errado. AJAX utiliza
tecnologias não proprietárias, como XML,
Javascript. etc foram que falar em usar protocolo proprietário não faz 0 menor sentido; (e) Errado.
AJAX não usa SMTP, não faz
sentido também falar do protocolo SMTP e do AJAX, são coisa distintas (Letra A).


QUESTõES CoMENTADAS - AJAX

í. (FCC/ TRE-MS 2007) Asynchronous Javascript and XML (Ajax) é uma
técnica de
desenvolvimento de aplicações web cujo objetivo é a troca de pequenas porções de dados
entre
um browser e um servidor web de modo a evitar a recarga de toda a página cada vez
que um
cliente solicita uma mudança. Sobre Ajax considere as afirmativas abaixo.

I. É uma técnica indicada para melhorar a experiência do usuário, reduzir a utilização
de banda
e claramente separar dados, formatação, estilo e funcionalidade.

II. O modelo de objetos html/xml (DOM) é acessado e transformado por linguagens de
script
como JavaScript.

III. O objeto XMLHttpRequest e/ou o objeto iFrame são utilizados para troca
de dados
assíncrona com o servidor.

É correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e III, apenas.

e) I, lie III.

Comentários:

(I) Perfeito, perfeito, perfeito, nada a acrescentar; (II) Sim, item perfeito também;
(III) Também está
correto! Pode-se utilizar o iFrame (Inline Frame) para embarcar aplicações interativas
em páginas
web.

Gabarito: Letra E

Item. 2. (FCC / MPE-RS - 2008) Para capturar as respostas de uma aplicação Web dinâmica
em AJAX
básico utiliza-se somente:

a) responseText e responseXML.

b) responseText e responseHTML.

c) responseText.

d) responseXML.

e) responseHTML

Comentários:


Trata-se da primeira opção: responseText e responseXML Respectivamente para
capturar as
respostas de uma aplicação Web dinâmica em AJAX básico utiliza-se somente
responseText e
respondeXML.

Gabarito: Letra A

Item. 3. (FCC / MPE-RS - 2008) Dentre as tecnologias que compõem o AJAX, aquelas que têm
como
principal função fazer o intercâmbio e a manipulação de dados são:

a) JavaScript e XMLHttpRequest.

b) XML e XSLT.

c) HTML e XHTML.

d) JavaScript e CSS.

e) DOM e CSS.

Comentários:

- Apresentação: HTML/XHTML e CSS;

- Exposição e Interação Dinâmica: DOM;

- Intercâmbio de Dados: XML ou JSON;

- Manipulação de Dados: XSLT;

- Recuperação Assíncrona de Dados: XMLHttpRequest;

* JavaScript é o responsável por reunir todas essas tecnologias.

Gabarito: Letra B

Item. 4. (FCC / MPE-RS - 2008) Para fazer o intercâmbio e a manipulação de dados em uma
aplicação
Web, o modelo AJAX normalmente utiliza:

a) XML e XSLT.

b) HTML, XHTMLeCSS.

c) XMLHttpRequest.

d) JavaScript.

e) DOM.

Comentários:

- Apresentação: HTML/XHTML e CSS;

- Exposição e Interação Dinâmica: DOM;

- Intercâmbio de Dados: XML ou JSON;

- Manipulação de Dados: XSLT;

- Recuperação Assíncrona de Dados: XMLHttpRequest;


/ 114

/


* JavaScript é o responsável por reunirtodas essas tecnologias.

Gabarito: Letra A

Item. 5. (FCC / TJ-PE - 2012) Esse objeto é o ponto chave do AJAX. Pode ser considerado
um objeto
Javascript que torna possível a comunicação assíncrona com o servidor. O objeto citado
é do
tipo:

a) XMLRequest.

b) XMLAjaxActiveXObject.

c) HttpServIetResponse.

d) HttpServIetRequest.

e) XMLHttpRequest

Comentários:

O objeto responsável pela comunicação assíncrona com o servidor é chamado: XMLHttpRequest.

Gabarito: Letra E

Item. 6. (FCC / TCE-PR - 2011) No AJAX, o objeto XMLHttpRequest possui diversas
propriedades
importantes para realizar a comunicação com o servidor. Quando uma solicitação
para um
servidor é enviada, normalmente deseja-se executar algumas ações com base na resposta. O
evento utilizado para especificar o que vai acontecer quando a resposta do servidor
está pronta
para ser processada é o:

a) oncompletedrequest.

b) onserverreturn.

c) onendstatus.

d) onreadystatechange.

e) onreadystate.

Comentários:

Trata-se do onreadystatechange. O evento utilizado para especificar o que vai acontecer
quando a
resposta do servidor está pronta para ser processada é onreadystatechang.

Gabarito: Letra D

Item. 7. (FCC / INFRAERO - 2011) Representa uma desvantagem do uso de AJAX:


/ 114

/


a) Troca mensagens entre o cliente e o servidor de forma assíncrona, ou seja, envia
requisições
e continua o processamento sem precisar aguardar a resposta.

b) Trata-se principalmente de JavaScript que executa no navegador do usuário.
Se for
desativado o processamento do JavaScript no navegador, a aplicação pode falhar.

c) Recebe respostas às requisições na mesma página sem a necessidade de refresh.

d) Executa os processos em paralelo às requisições/respostas.

e) Manipula o conteúdo XML nas aplicações para desktop de forma simples.

Comentários:

Todas apresentam vantagens, exceto a segunda opção! De fato, se o usuário desativar o
JavaScript
em seu navegador, a aplicação pode falhar e essa é uma grande desvantagem do AJAX.

Gabarito: Letra B

Item. 8. (FCC/TRE-RN-2011) Agrega um conjunto de tecnologias conhecidas trabalhando
juntas para
tornar páginas Web mais interativas com o usuário, utilizando-se de solicitações
assíncronas de
informações:

a) XML.

b) JavaScript.

c) XHTML.

d) AJAX.

e) CSS.

Comentários:

Trata-se obviamente do AJAX! Conforme estudamos, logo o AJAX agrega um
conjunto de
tecnologias conhecidas trabalhando juntas para tornar páginas Web mais interativas com o
usuário,
utilizando-se de solicitações assíncronas de informações.

Gabarito: Letra D

Item. 9. (FGV / FIOCRUZ - 2010) Asynchronous JavaScript and XML (AJAX) é um
termo criado
recentemente para duas características poderosas dos browsers que existem há anos mas
tem
sido ignoradas por muitos criadores de páginas web até recentemente, quando aplicações
como
Gmail, Google suggest e Google Maps foram lançadas. AJAX não é uma tecnologia, na
verdade,
envolve várias, cada uma atuando da sua própria maneira, tornando-se juntas uma poderosa
ferramenta. Nesse contexto, além de suporte à Javascript, analise as
afirmativas abaixo,
associadas às tecnologias incorporadas pelo AJAX.

I. Troca e manipulação de dados usando XML e XSLT.

II. Retorno de dados assincronamente usando XMLHttpRequest.


/ 114

/


III. Apresentação baseada nas Web Standards usando XHTML e CSS.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

Todos os itens estão corretos. Assim: O AJAX realiza a troca e manipulação de dados
usando XML
e XSLT. O retorno de dados assincronamente usando XMLHttpRequest e a apresentação
baseada
nas Web Standards usando XHTML e CSS.

Gabarito: Letra E

io.(CESGRANRIO / DNMP - 2006) AJAX é um termo que se refere a um conjunto de
tecnologias
para desenvolvimento de aplicações WEB. Assinale a opção que contempla uma
dessas
tecnologias.

a) Ant
b) XML

c) WiMAX

d) VolP

e) Jakarta

Comentários:

AJAX contempla JavaScript e XML, conforme estudamos ao longo da aula, logo a
alternativa B está
correta.

Gabarito: Letra B

II.(CESPE/TJ-R0-2012) Que conjunto de tecnologias é utilizado em aplicações WEB
na Internet
para propiciar forte interatividade e dinamismo?

a) CSS

b) SMTP

c) AJAX

d) FTP

e) UTF-8


/ 114

/


Comentários:

Trata-se do AJAX! Ele é um conjunto de tecnologias que propiciam forte
interatividade e
dinamismo.

Gabarito: Letra C

i2.(CESPE / MEC -2011) AJAX (do inglês Asynchronous Javascript And XML) tem sido
largamente
utilizado no desenvolvimento de aplicações WEB. Um dos conceitos centrais do
AJAX é a
possibilidade de serem feitas requisições ao servidor através de código Javascript,
rodando no
navegador do usuário. Esse recurso é empregado principalmente para permitir que:

a) o processamento das regras de negócio da aplicação seja distribuído aos
clientes,
minimizando a carga do servidor.

b) o usuário envie uma requisição assíncrona e verifique o resultado da mesma mais
tarde, sem
precisar aguardar pela resposta imediata do servidor.

c) as páginas carreguem mais rapidamente, pois as requisições são paralelizadas e
compactadas
durante o trânsito.

d) as páginas compostas diretamente em XML, ao invés de XHTML ou HTML,
sejam
apresentadas no navegador do usuário.

e) partes de uma página web sejam atualizadas, sem que o browser recarregue a página
inteira
do servidor, proporcionando uma interface com melhor usabilidade

Comentários:

(a) Não, o processamento das regras de negócio continua sendo no Servidor; (b) Não há
nada de
errado com esse item, no entanto o recurso não é empregado principalmente para isso!
Eu posso
verificar o resultado mais tarde? Sim, mas o Ajax é utilizado principalmente para que
eu possa
verificar o resultado imediatamente sem a necessidade de recarregar a página inteira;
(c) Não, é
para que partes das páginas recarreguem de forma dinâmica e interativa; (d) Não, são
apresentadas
como XHTML ou HTML; (e) Perfeito, é exatamente isso!

Gabarito: Letra E

Item. 13. (CESGRANRIO / IBGE - 2010) O código HTML, em construção, abaixo demonstra a
utilização
de AJAX.

<html>


/ 114

/


<head>

<script language="3avaScri pt">
function submi tForm()

{

var xhr=null;
try

{ xhr = new object(); }
catch(e) {}

xhr.onreadystatechange = function()

{

document.ajax.dyn.value="Wait server..
if(xhr.readyState == 4)

{

if(xhr.status == 200)

{ document.ajax.dyn.value="Recebido:" + xhr.responseText; }
else

{ document.ajax.dyn.value="Erro: " + xhr.status + " " + xhr.statusText; }

}

};

xhr.open("GET", "data.xml", true);
xhr.send(null);

}

</scri pt>

</head>

<body>

<FORM method="POST" name="ajax" action="">

CINPUT type = "submi t" value="Submi t" ONCLICK="subrrri tForm() ">
CINPUT type="text" name="dyn" value="">

</FORM>

</body>

</html>

Para que esse código possa utilizar a tecnologia AJAX, na linha "xhr = new
object();", "xhr" deve
receber um objeto Javascript que torna possível a comunicação assíncrona com o
servidor, sem
a necessidade de recarregar a página por completo. Para tanto, no código acima,
"object" deve
ser substituído por:

a) responseXML

b) MIME.

c) XMLHttpRequest.

d) DOMParser.

e) setRequestReader.

Comentários:

O objeto JS para comunicação assíncrona em questão,
trata-se do Objeto
XMLHttpRequest. XMLHttpRequest é um objeto que fornece funcionalidade ao
cliente para
transferir dados entre um cliente e um servidor.


/ 114

/


Gabarito: Letra C

i4.(CESPE / PREVIC - 2011) Ajax não é meramente uma tecnologia. É uma abordagem
moderna
para desenvolvimento de sites iterativos. A abordagem de desenvolvimento
tradicional tem
semelhanças e diferenças em relação ao Ajax. Uma característica exclusiva de Ajax em
relação
à abordagem tradicional é que:

a) executa as requisições através do protocolo HTTP.

b) usa javascript como linguagem para desenvolver código no lado do cliente.

c) usa (x)html / css para definir o aspecto visual da página.

d) permite recuperação assíncrona de dados usando XMLHttpRequest.

e) representa os objetos no lado cliente com DOM.

Comentários:

A única opção que apresenta uma característica de fato exclusiva em relação
à abordagem
tradicional é quarta opção: permite recuperação assíncrona de dados usando XMLHttpRequest.

Gabarito: Letra D

Item. 15. (CESGRANRIO/ LIQUIGÁS - 2011) Duas das tecnologias que compõem o Ajax são:

a) DOM e CSS

b) ASPeXML

c) Java e XML

d) Java e CSS

e) JavaScript e ASP

Comentários:

DOM? Sim! CSS? Sim! ASP? Não! XML? Sim! Java? Não! JavaScript? Sim! Portanto, é a
primeira
opção: DOM e CSS!

Gabarito: Letra A

16.(CESGRANRIO / LIQUIGÁS - 2013) Considere as afirmativas a seguir sobre a tecnologia AJAX.

I - Uma das aplicações mais frequentes da tecnologia AJAX é na atualização assíncrona
do
conteúdo de páginas HTML.

II - Boa parte da funcionalidade da tecnologia AJAX é viabilizada pelo objeto
XMLHttpRequest,
que é capaz de transmitir requisições HTTP de modo assíncrono.


III - Atecnologia AJAX utiliza código Java para a manipulação do conteúdo de páginas HTML.
Está correto o que se afirma em:

a) I, apenas
b) II, apenas
c) I e II, apenas
d) II e III, apenas
e) I, lie III

Comentários:

(I) Sim, perfeito! (II) Sim, perfeito! (III) Não, utiliza DOM! Logo, a alternativa C
com I e II, apenas está
aderente ao que estudamos na aula.

Gabarito: Letra C

Item. 17. (CESGRANRIO / IBGE - 2014) Com o objetivo de criar páginas
dinâmicas para o
desenvolvimento de aplicações web, AJAX é um termo que descreve um(a):

a) protocolo
b) banco de dados
c) coleção de tecnologias
d) linguagem de programação
e) linguagem de marcação

Comentários:

AJAX é um conjunto de tecnologias, tais como: XML, JSON, XSTL, HTML, XHTML,
DOM,
JavaScript, CSS e XMLHttpRequest

Gabarito: Letra C

Item. 18. (FGV/TCM-SP-2015) Considere a requisição AJAX construída, no cliente, através da
chamada
à seguinte função em Javascript:


function send (msg)

{

var message = "GET=' " + msg + 11 * 11;
var ajax = new XMLHttpReqnest ();

ajax. onreadystateahange = function ()

{

if (this. readyState == 4 &&

this.status = 200)
alert (this.responseText);

}

ajax.open ("POST", "PUT.PHP", true) ;

ajax. setReques tHeader ("Content-type" f

,rapplication/x-www-f onn-urlencoded1') ;
ajax. setReques tHeader ("Content-length" r
message.length);

aj ax.se tReque s tHeader ("Connection"f
"dose") ;

ajax.send (message);

}

O método HTTP utilizado na requisição ao servidor será, neste caso:

a) PUT;

b) POST;
C)GET;

d) HEAD;

e) SEND.

Comentários:

Neste caso, a requisição ao servidor está representada na variável ajax = new
XMLHttpRequest() e
sua chamada em ajax.open("POST", "PUT.PHP", true);

O protótipo do método open, neste caso, é XMLHttpRequest.open(method, uri,
async), logo o
método HTTP a ser utilizado é o POST.

Vale notar que as strings GET e PUT foram usadas apenas para confundir o aluno,
sendo elas,
apenas, parte da mensagem e uri de envio, respectivamente.

Gabarito: Letra B


00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de
software - 2023 (Pós-Edital)


Item. 19. (UFRJ / UFRJ - 2012) Para utilizar Ajax é preciso antes instalar e configurar
um servidor Ajax, o
qual interage com o servidor web.

Comentários:

Não existe essa dependência de que para utilizar Ajax é preciso antes instalar e
configurar um
servidor Ajax, o qual interage com o servidor web.

Gabarito: Errado

2o.(CESGRANRIO / LIQUIGÁS - 2013) Uma das aplicações mais frequentes da tecnologia AJAX
é
na atualização assíncrona do conteúdo de páginas HTML.

Comentários:

Perfeito! Uma das aplicações mais frequentes da tecnologia AJAX é na atualização
assíncrona do
conteúdo de páginas HTML.

Gabarito: Correto

Item. 21. (CESGRANRIO / LIQUIGÁS - 2013) A tecnologia AJAX utiliza código Java para a
manipulação do
conteúdo de páginas HTML.

Comentários:

No AJAX, o JAVA é utilizado para manipulação do conteúdo de páginas HTML.

Gabarito: Correto

22.(FUNCAB / PRODAM - 2014) A utilização de Ajax em uma página permite a recuperação
de
dados de uma URL sem a necessidade de recarregar a página inteira. O objeto
JavaScript que
foi adotado pelos principais navegadores para realizar operações Ajax é
chamado
XMLHttpRequest.

Comentários:

Perfeito! Conforme vimos, o objeto JavaScript que foi adotado pelos principais
navegadores para
realizar operações Ajax é chamado de XMLHttpRequest.

Gabarito: Correto


23.(CESPE / MPE-RS - 2012) AJAX é uma técnica de construção de páginas web, e sua
principal
vantagem é permitir a atualização de partes da página web.

Comentários:

Perfeito! De fato, AJAX é uma técnica de construção de páginas web, e sua principal
vantagem é
permitir a atualização de partes da página web.

Gabarito: Correto

24.(CESGRANRIO / PETROBRÁS - 2010) Ajax não é meramente uma tecnologia. É
uma
abordagem moderna para desenvolvimento de sites iterativos. A
abordagem de
desenvolvimento tradicional tem semelhanças e diferenças em relação ao
Ajax. Uma
característica exclusiva de Ajax em relação à abordagem tradicional é que permite
recuperação
assíncrona de dados usando XMLHttpRequest.

Comentários:

De fato, o Objeto XMLHttpRequest é utilizado para trocar dados com o
servidor de forma
assíncrona.

Gabarito: Correto

25.(AOCP / FUNPRESP-JUD - 2021) JavaScript é uma linguagem que sofre
muito com
compatibilidade entre navegadores. A jQuery sofre com o mesmo problema.
Animações,
manipulação de DOM e outra tarefas corriqueiras são mais complexas e menos produtivas
ao
usar o jQuery.

Comentários:

É exatamente tudo ao contrário do que está escrito. JS não sofre de
compatibilidade com
navegadores e JQuery tbm não, logo manipulação de DOM são menos complexas e mais
produtivas
ao utilizar Jquery.

Gabarito: Errado

26.(IFS / IFS - 2021) O JavaScript possui características de uma linguagem
funcional, portanto
pode-se passar funções como parâmetros para outras funções, algo comumente
encontrado
nos códigos em JavaScript e Node.

Sabendo disso, analise as afirmativas abaixo:


/ 114

/


I. function somaCajb)!
return a -» b;

}

function executâr(funcac,a,b){
return funcao(a,b)

}

let resultado executar(soma.1,2)
console.log(resultado)


II.

function executar(a,b,funcao){

return funcao(a.b)

}

let resultado executar(l,2»function(a,b){

return a+b

})

console.log(resultado)

III. var funcao - function(a,b){

return a+b

}

function executar(a,b,funcao){

return funcao(a,b)

}

let resultado - executar(1,2,funcao)

console.log(resultado)

Está(ão) correta(s) a(s) afirmativa(s)

a) I, Apenas.

b) II, Apenas.

c) III, Apenas.

d) I, lie III.

Comentários:


No item I temos a declaração da função, que soma e passa os argumentos para
execução. No item
II, a função executar recebe uma função anônima e no item III, temos a atribuição da
variável funcao
à uma função anônima, para porfim realizar a execução.

Gabarito: Letra D

Item. 27. (IFS / IFS - 2021) A linguagem JavaScript provê uma série de métodos que facilitam a
manipulação de arrays. Sobre o método de manipulação de array of, é correto afirmar que:

a) cria um novo array a partir de um array existente.

b) preenche o array com um valor estático.

c) devolve @@iterator, contendo os valores do array.

d) cria um novo array a partir dos argumentos passados para o método.

Comentários:

O método Array.of() cria uma nova instância de Array a partir de um
número variável de
argumentos.

Gabarito: Letra D

28.(IFS / IFS - 2021) Considere o seguinte código JavaScript:

let o = {one:1,two:2,three:3};
for(let p in o) console.log(p);

Ao final da execução, quais valores serão impressos?
a) 1, 2, 3

b) one:i, two: 2, three: 3

c) P, p, P

d) 'one', 'two', 'three'

Comentários:

Para imprimir os valores em vez das chaves, é necessário utilizar o console.Iog(
o[p]), como temos:
console.log (p), nossa saída será: 'one', 'two', 'three'.

Gabarito: Letra D

29.(IFS / IFS - 2021) Considere o seguinte código JavaScript:

var a = [1,2,3,4,5] ;

a.slice(0,3);


/ 114

/


a.splíce(l₅l);
a.pop();

Qual o valor da variável a ao término da execução do código?

a) [i,3,4l
b) [1,3,4,5l
c) [1,3]

d) [3,4,5]

Comentários:

Array inicial = "[1,2,3,4,5]" e o índice começa em zero, teremos:

a.slice(o,3);

-> Retorna uma lista com os elementos de o a 3 (não incluso)

-> Essa função não altera a lista original, apenas retorna uma nova lista, então não irá
influenciar no
código.

a.splice(i,i);

-> Essa função altera a lista original

-> A partir da posição 1, remove 1 elemento

-> Sobra: [1,3,4,5]

a.pop();

-> Remove o último elemento do array, sobra: [1,3,4]

Gabarito: Letra A

3o.(IFS / IFS - 2021) Em JavaScript, o operador new cria e inicializa um novo objeto.
Qual operador NÃO representa a criação de um objeto de tipo nativo JavaScript?

a) var o = new Object();

b) var I = new ArrayList();

c) var a - new Array();

d) var d = new Date();

Comentários:

Para se criar um array no JS, a única forma das citadas que não serve é var I -
new ArrayList ();
ArrayList é utilizado na linguagem JAVA e não no JS.

Gabarito: Letra B


/ 114

/


Item. 31. (IUDS / IF-RJ - 2021) Em javascript, o que faz a função Math.roundO?

a) Retorna o valor decimal, mais próximo.

b) Retorna o valor de um número arredondado para o inteiro, mais próximo.

c) Retorna o valor de um número arredondado para o inteiro, logo abaixo.

d) Retorna o valor de um número arredondado para o inteiro, logo acima.

Comentários:

A função Math.roundO retorna o valor arredondado para o inteiro mais próximo.

Gabarito: Letra B

32.(QUADRIX / CFT - 2021) Na linguagem de programação JavaScript, por meio do operador
+
(adição), é permitido que uma nova variável de texto (string) possua valor igual à
justaposição
dos valores de outras variáveis.

Comentários:

Perfeito! No JS, por meio do operador + (adição), é permitido que uma nova variável
de texto (string)

possua valor igual à justaposição dos valores de outras variáveis.

Gabarito: Correto

Item. 33. (QUADRIX / CFT - 2021) O comprimento máximo de uma linha de código no JavaScript
é de
128 caracteres.

Comentários:

Em tese, não existe uma limite de extensão (comprimento) de uma linha de código no JS.

Gabarito: Errado

Item. 34. (QUADRIX / CFT - 2021) As variáveis, em JavaScript, possuem um tipo definido, por
isso
um array não pode conter valores de tipos diferentes.

Comentários:

JS não tem tipo definido. A atribuição de tipos é dinâmica, logo o array pode sim
conter valores de
tipos diferentes.

Gabarito: Errado


/ 114

/


Item. 35. (QUADRIX / CFT - 2021) Como toda linguagem de programação, a JavaScript também
possui
limitações. Sua maior limitação é não permitir que determinados objetos gráficos
apresentados
na página (imagem, botão etc.) respondam dinamicamente às ações do usuário.

Comentários:

No JS, o DOM representa todos os elementos da página web. Assim, os scripts em JS
podem
manipular os elementos da página, logo é possível que os mesmos respondam dinamicamente
às
ações do usuário.

Gabarito: Errado


/ 114

/


LISTA DE QUESTõES - AJAX

í. (FCC/ TRE-MS 2007) Asynchronous Javascript and XML (Ajax) é uma
técnica de
desenvolvimento de aplicações web cujo objetivo é a troca de pequenas porções de dados
entre
um browser e um servidor web de modo a evitar a recarga de toda a página cada vez
que um
cliente solicita uma mudança. Sobre Ajax considere as afirmativas abaixo.

I. É uma técnica indicada para melhorar a experiência do usuário, reduzir a utilização
de banda
e claramente separar dados, formatação, estilo e funcionalidade.

II. O modelo de objetos html/xml (DOM) é acessado e transformado por linguagens de
script
como JavaScript.

III. O objeto XMLHttpRequest e/ou o objeto iFrame são utilizados para troca
de dados
assíncrona com o servidor.

É correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e III, apenas.

e) I, lie III.

Item. 2. (FCC / MPE-RS - 2008) Para capturar as respostas de uma aplicação Web dinâmica
em AJAX
básico utiliza-se somente:

a) responseText e responseXML.

b) responseText e responseHTML.

c) responseText.

d) responseXML.

e) responseHTML

Item. 3. (FCC / MPE-RS - 2008) Dentre as tecnologias que compõem o AJAX, aquelas que têm
como
principal função fazer o intercâmbio e a manipulação de dados são:

a) JavaScript e XMLHttpRequest.

b) XMLeXSLT.

c) HTML e XHTML.

d) JavaScript e CSS.

e) DOMeCSS.

Item. 4. (FCC / MPE-RS - 2008) Para fazer o intercâmbio e a manipulação de dados em uma
aplicação
Web, o modelo AJAX normalmente utiliza:


a) XML e XSLT.

b) HTML, XHTML e CSS.

c) XMLHttpRequest.

d) JavaScript.

e) DOM.

Item. 5. (FCC / TJ-PE - 2012) Esse objeto é o ponto chave do AJAX. Pode ser considerado
um objeto
Javascript que torna possível a comunicação assíncrona com o servidor. O objeto citado
é do
tipo:

a) XMLRequest.

b) XMLAjaxActiveXObject.

c) HttpServIetResponse.

d) HttpServIetRequest.

e) XMLHttpRequest

Item. 6. (FCC / TCE-PR - 2011) No AJAX, o objeto XMLHttpRequest possui diversas
propriedades
importantes para realizar a comunicação com o servidor. Quando uma solicitação
para um
servidor é enviada, normalmente deseja-se executar algumas ações com base na resposta. O
evento utilizado para especificar o que vai acontecer quando a resposta do servidor
está pronta
para ser processada é o:

a) oncompletedrequest.

b) onserverreturn.

c) onendstatus.

d) onreadystatechange.

e) onreadystate.

Item. 7. (FCC / INFRAERO - 2011) Representa uma desvantagem do uso de AJAX:

a) Troca mensagens entre o cliente e o servidor de forma assíncrona, ou seja, envia
requisições
e continua o processamento sem precisar aguardar a resposta.

b) Trata-se principalmente de JavaScript que executa no navegador do usuário.
Se for
desativado o processamento do JavaScript no navegador, a aplicação pode falhar.

c) Recebe respostas às requisições na mesma página sem a necessidade de refresh.

d) Executa os processos em paralelo às requisições/respostas.

e) Manipula o conteúdo XML nas aplicações para desktop de forma simples.

Item. 8. (FCC/TRE-RN-2011) Agrega um conjunto de tecnologias conhecidas trabalhando
juntas para
tornar páginas Web mais interativas com o usuário, utilizando-se de solicitações
assíncronas de
informações:

a) XML.


b) JavaScript.

c) XHTML.

d) AJAX.

e) CSS.

Item. 9. (FGV / FIOCRUZ - 2010) Asynchronous JavaScript and XML (AJAX) é um
termo criado
recentemente para duas características poderosas dos browsers que existem há anos mas
tem
sido ignoradas por muitos criadores de páginas web até recentemente, quando aplicações
como
Gmail, Google suggest e Google Maps foram lançadas. AJAX não é uma tecnologia, na
verdade,
envolve várias, cada uma atuando da sua própria maneira, tornando-se juntas uma poderosa
ferramenta. Nesse contexto, além de suporte à Javascript, analise as
afirmativas abaixo,
associadas às tecnologias incorporadas pelo AJAX.

I. Troca e manipulação de dados usando XML e XSLT.

II. Retorno de dados assincronamente usando XMLHttpRequest.

III. Apresentação baseada nas Web Standards usando XHTML e CSS.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Item. 10. (CESGRANRIO / DNMP - 2006) AJAX é um termo que se refere a um conjunto de
tecnologias
para desenvolvimento de aplicações WEB. Assinale a opção que contempla uma
dessas
tecnologias.

a) Ant
b) XML

c) WiMAX

d) VolP

e) Jakarta
n.(CESPE /TJ-RO-2012) Que conjunto de tecnologias é utilizado em aplicações WEB na
Internet
para propiciar forte interatividade e dinamismo?

a) CSS

b) SMTP

c) AJAX

d) FTP

e) UTF-8


i2.(CESPE / MEC -2011) AJAX (do inglês Asynchronous Javascript And XML) tem sido
largamente
utilizado no desenvolvimento de aplicações WEB. Um dos conceitos centrais do
AJAX é a
possibilidade de serem feitas requisições ao servidor através de código Javascript,
rodando no
navegador do usuário. Esse recurso é empregado principalmente para permitir que:

a) o processamento das regras de negócio da aplicação seja distribuído aos
clientes,
minimizando a carga do servidor.

b) o usuário envie uma requisição assíncrona e verifique o resultado da mesma mais
tarde, sem
precisar aguardar pela resposta imediata do servidor.

c) as páginas carreguem mais rapidamente, pois as requisições são paralelizadas e
compactadas
durante o trânsito.

d) as páginas compostas diretamente em XML, ao invés de XHTML ou HTML,
sejam
apresentadas no navegador do usuário.

e) partes de uma página web sejam atualizadas, sem que o browser recarregue a página
inteira
do servidor, proporcionando uma interface com melhor usabilidade

Item. 13. (CESGRANRIO / IBGE - 2010) O código HTML, em construção, abaixo demonstra a
utilização
de AJAX.

<html>

<head>

<scri pt language="0avaScri pt">
function submitForm()

{

var xhr=null;
try

{ xhr = new object(); }
catch(e) {}

xhr.onreadystatechange = function()

{

document.ajax.dyn.value="Wait server..
if(xhr.readyState == 4)

{

if(xhr.status == 200)

{ document.ajax.dyn.value="Recebido: " + xhr.responseText; }
else

{ document.ajax.dyn.value="Erro: " + xhr.status + " "
+ xhr.statusText; }

}

};

xhr.open("GET", "data.xml", true);
xhr.send(null);

}


/ 114

/


</scri pt>

</head>

<body>

<FORM method="POST" name="ajax" action="">

CINPUT type="submit" value="Submit" ONCLICK="submitForm()">
CINPUT type="text" name="dyn" value="">

</FORM>

</body>

</html>

Para que esse código possa utilizar a tecnologia AJAX, na linha "xhr = new
object();", "xhr" deve
receber um objeto Javascript que torna possível a comunicação assíncrona com o
servidor, sem
a necessidade de recarregar a página por completo. Para tanto, no código acima,
"object" deve
ser substituído por:

a) responseXML.

b) MIME.

c) XMLHttpRequest.

d) DOMParser.

e) setRequestReader.

Item. 14. (CESPE / PREVIC - 2011) Ajax não é meramente uma tecnologia. É uma abordagem
moderna
para desenvolvimento de sites iterativos. A abordagem de desenvolvimento
tradicional tem
semelhanças e diferenças em relação ao Ajax. Uma característica exclusiva de Ajax em
relação
à abordagem tradicional é que:

a) executa as requisições através do protocolo HTTP.

b) usa javascript como linguagem para desenvolver código no lado do cliente.

c) usa (x)html / css para definir o aspecto visual da página.

d) permite recuperação assíncrona de dados usando XMLHttpRequest.

e) representa os objetos no lado cliente com DOM.

Item. 15. (CESGRANRIO/ LIQUIGÁS - 2011) Duas das tecnologias que compõem o Ajax são:

a) DOM e CSS

b) ASPeXML

c) Java e XML

d) Java e CSS

e) JavaScript e ASP

Item. 16. (CESGRANRIO / LIQUIGÁS - 2013) Considere as afirmativas a seguir sobre a tecnologia AJAX.

I - Uma das aplicações mais frequentes da tecnologia AJAX é na atualização
assíncrona do
conteúdo de páginas HTML.


/ 114

/


II - Boa parte da funcionalidade da tecnologia AJAX é viabilizada pelo objeto
XMLHttpRequest,
que é capaz de transmitir requisições HTTP de modo assíncrono.

III - Atecnologia AJAX utiliza código Java para a manipulação do conteúdo de páginas HTML.
Está correto o que se afirma em:

a) I, apenas
b) II, apenas
c) I e II, apenas
d) II e III, apenas
e) I, lie III

Item. 17. (CESGRANRIO / IBGE - 2014) Com o objetivo de criar páginas dinâmicas para o
desenvolvimento de aplicações web, AJAX é um termo que descreve um(a):

a) protocolo
b) banco de dados
c) coleção de tecnologias
d) linguagem de programação
e) linguagem de marcação

Item. 18. (FGV/TCM-SP- 2015) Considere a requisição AJAX construída, no cliente, através da chamada
à seguinte função em Javascript:


function send (msg)

{

var message = "GET=' " + msg + 11 * 11;
var ajax = new XMLHttpReqnest ();

ajax. onreadystateahange = function ()

{

if (this. readyState == 4 &&

this.status = 200)
alert (this.responseText);

}

ajax.open ("POST", "PUT.PHF1', true) ;

ajax. setReques tHeader ("Content-type" f

,rapplication/x-www-f onn-urlencoded1') ;
ajax. setReques tHeader ("Content-length" r
message.length);

aj ax.se tReque s tHeader ("Connection"f
"dose") ;

ajax.send (message);

}

O método HTTP utilizado na requisição ao servidor será, neste caso:

a) PUT;

b) POST;
C)GET;

d) HEAD;

e) SEND.

Item. 19. (UFRJ / UFRJ - 2012) Para utilizar Ajax é preciso antes instalar e configurar um servidor
Ajax, o
qual interage com o servidor web.

Item. 20. (CESGRANRIO / LIQUIGÁS - 2013) Uma das aplicações mais frequentes da tecnologia AJAX é
na atualização assíncrona do conteúdo de páginas HTML.

Item. 21. (CESGRANRIO / LIQUIGÁS - 2013) A tecnologia AJAX utiliza código Java para a manipulação do
conteúdo de páginas HTML.

Item. 22. (FUNCAB / PRODAM - 2014) A utilização de Ajax em uma página permite a recuperação de
dados de uma URL sem a necessidade de recarregar a página inteira. O objeto JavaScript que
foi adotado pelos principais navegadores para realizar operações Ajax é
chamado
XMLHttpRequest.

Item. 23. (CESPE / MPE-RS - 2012) AJAX é uma técnica de construção de páginas web, e sua
principal
vantagem é permitir a atualização de partes da página web.

Item. 24. (CESGRANRIO / PETROBRÁS - 2010) Ajax não é meramente uma tecnologia. É
uma
abordagem moderna para desenvolvimento de sites iterativos. A
abordagem de
desenvolvimento tradicional tem semelhanças e diferenças em relação ao
Ajax. Uma
característica exclusiva de Ajax em relação à abordagem tradicional é que permite
recuperação
assíncrona de dados usando XMLHttpRequest.

Item. 25. (AOCP / FUNPRESP-JUD - 2021) JavaScript é uma linguagem que sofre muito
com
compatibilidade entre navegadores. A jQuery sofre com o mesmo problema.
Animações,
manipulação de DOM e outra tarefas corriqueiras são mais complexas e menos produtivas
ao
usar o jQuery.

Item. 26. (IFS / IFS - 2021) O JavaScript possui características de uma linguagem funcional,
portanto
pode-se passar funções como parâmetros para outras funções, algo comumente
encontrado
nos códigos em JavaScript e Node.

Sabendo disso, analise as afirmativas abaixo:


/ 114

/


I. function somaCajb)!
return a -» b;

}

function executâr(funcac,a,b){
return funcao(a,b)

}

let resultado executar(soma.1,2)
console.log(resultado)


II.

function executar(a,b,funcao){
return funcao(a.b)

}

let resultado executar(l,2»function(a,b){
return a+b

))

console.log(resultado)

III. var funcao - function(a,b){
return a+b

}

function executar(a,b,funcao){
return funcao(a,b)

}

let resultado - executar(1,2,funcao)
console.log(resultado)

Está(ão) correta(s) a(s) afirmativa(s)

a) I, Apenas.

b) II, Apenas.

c) III, Apenas.

d) I, lie III.

27.(IFS / IFS - 2021) A linguagem JavaScript provê uma série de métodos que facilitam a
manipulação de arrays. Sobre o método de manipulação de arrayof, é correto afirmar que:


a) cria um novo array a partir de um array existente.

b) preenche o array com um valor estático.

c) devolve @@iterator, contendo os valores do array.

d) cria um novo array a partir dos argumentos passados para o método.

28.(IFS / IFS - 2021) Considere o seguinte código JavaScript:

let o = {one:1,two:2,three:3};
forClet p in o) console.log(p);

Ao final da execução, quais valores serão impressos?
a) 1, 2, 3

b) one:i, two: 2, three: 3

c) P, p, P

d) 'one', 'two', 'three'

29.(IFS / IFS - 2021) Considere o seguinte código JavaScript:

var a = [1,2,3,4,5] ;

a.slice(0,3);

a.spli ce(l,1);

a.pop();

Qual o valor da variável a ao término da execução do código?

a) [1,3,41

b) [i,3,4,5l
c) [1,3]

d) [3,4,5]

Item. 30. (IFS / IFS - 2021) Em JavaScript, o operador new cria e inicializa um novo objeto.
Qual operador NÃO representa a criação de um objeto de tipo nativo JavaScript?

a) var o = new Object();

b) var I - new Arrayl_ist();

c) vara = newArrayO;

d) var d = new Date();

Item. 31. (IUDS / IF-RJ - 2021) Em javascript, o que faz a função Math.round()?

a) Retorna o valor decimal, mais próximo.

b) Retorna o valor de um número arredondado para o inteiro, mais próximo.

c) Retorna o valor de um número arredondado para o inteiro, logo abaixo.


/ 114

/


d) Retorna o valor de um número arredondado para o inteiro, logo acima.

32.(QUADRIX / CFT - 2021) Na linguagem de programação JavaScript, por meio do operador
+
(adição), é permitido que uma nova variável de texto (string') possua valor igual à
justaposição
dos valores de outras variáveis.

Item. 33. (QUADRIX / CFT - 2021) O comprimento máximo de uma linha de código no
JavaScript é de
128 caracteres.

Item. 34. (QUADRIX / CFT - 2021) As variáveis, em JavaScript, possuem um tipo definido, por
isso
um array não pode conter valores de tipos diferentes.

Item. 35. (QUADRIX / CFT - 2021) Como toda linguagem de programação, a JavaScript também
possui
limitações. Sua maior limitação é não permitir que determinados objetos gráficos
apresentados
na página (imagem, botão etc.) respondam dinamicamente às ações do usuário.

x35


/ 114

/


GABARITo - AJAX

Item. 1. CORRETO 13- LETRA E 25-
ERRADO

Item. 2. LETRA E 14. LETRA C
Item. 26. ERRADO

3- LETRA A 15- LETRA D
27- LETRA D

4- LETRA B i6. LETRA A
Item. 28. LETRA D

5- LETRA A 17- LETRA C
Item. 29. LETRA D

Item. 6. LETRA E i8. LETRA C
Item. 30. LETRA A

7- LETRA D 19- ERRADO
3i- LETRA B

Item. 8. LETRA B 20. CORRETO
Item. 32. LETRA B

9- LETRA D 21. CORRETO
33- CORRETO

Item. 10. LETRA E 22. ERRADO
34- ERRADO

íi. LETRA B 23- CORRETO
35- ERRADO

Item. 12. LETRA C 24- CORRETO


Single Page Application (SPA)

Em um paradigma de requisição/resposta, quando utilizamos um navegador web, nós
enviamos
uma requisição ao servidor, ele processa essa requisição e retorna uma página HTML.
Pois bem...
vocês já se perguntaram porque é necessário que o servidor processe as informações e
me retorne
à página pronta? Ora, porque ele não me retorna apenas as informações e eu mesmo
monto a
página?

Eu economizo dados, diminuo o tráfego, desonero o servidor e posso fazer uma aplicação
muito
mais rápida. E uma maneira de equilibrar a carga entre o cliente e o servidor, além
de melhorar a
experiência proporcionada ao usuário da aplicação por meio de maior ênfase
nas técnicas de
desenvolvimento de front-end. O que é isso, professor? Grosso modo, é a apresentação
visual do
site.

Galera, não é só isso! O JavaScript evoluiu muito desde sua integração nos browsers.
Inicialmente
ele era visto apenas como uma ferramenta para fazer botões funcionarem ou para a
criação de
menus a pedido de web designers. Com a evolução dos browsers e da
linguagem HTML, o
JavaScript ganhou força e muito poder de processamento.

A Web 2.0 veio trazer o JavaScript para uma posição de destaque. E adivinhe de que
lado roda
JavaScript? Cliente, oras! Em outras palavras, tudo parece nos levar a um
aprimoramento da
experiência do usuário, com transferência de dados em background (AJAX,
WebSocket, etc) e
aplicações cada vez mais interativas. Vocês conseguem perceber isso?

Com mais e mais profissionais estudando e utilizando JavaScript, grandes empresas como
Google,
Yahool, Apple e Microsoft passaram a desenvolver padrões e técnicas para
incrementar a
performance de seus scripts, separar e isolar porções de código, e fazer uso de
orientação à objeto
mais avançada na linguagem. O que aconteceu a partir daí?

Foram criadas aplicações inteiramente contidas no navegador e que não
precisam fazer
requisições de novas páginas ao servidor. Foram compiladas as melhores práticas e
criado, então,
o conceito de Single Page Application (SPA). São aplicações completas,
desenvolvidas em
JavaScript, que funcionam quase como se estivessem sendo executadas nativamente no desktop.

Vocês devem ter percebido que a tradução do conceito para português é
Aplicação de Única
Página. O nome leva a crer que estamos desenvolvendo um site inteiro em uma única
página com
todas as funcionalidades - uma abaixo da outra. Não é isso! Tem esse nome porque
geralmente
todo código (HTML, CSS e JavaScript) é recuperado em uma única carga inicial - o
navegador
utiliza apenas uma URL.


/ 114

/


Após essa página inicial ser carregada, toda a lógica de apresentação está no cliente.
Eu sei, vocês
devem estar achando um pouco complexo. Querem ver um exemplo? Abram o GMail, loguem-se
em suas contas e clique em uma mensagem na Caixa de Entrada. Observem que o navegador
continua na mesma página, mas o código JavaScript esconde a caixa de
entrada e traz a
mensagem para a tela.

Modo de exibição do Gmail: padrão | HTML básico Saiba mais

Não sei se vocês se lembram de como era antigamente, então - para ver claramente a
diferença

- mudem agora o Modo de Exibição de Padrão para Básico! Repitam a mesma operação,
i.e.,
entrem na Caixa de Entrada e cliquem em um e-mail qualquer. Observem, dessa vez, que
uma
nova página é carregada com o corpo da mensagem que você clicou.

Vocês percebem a diferença de velocidade? No primeiro caso, é quase instantâneo -
parece até
uma aplicação desktop. O SPA oferece dois benefícios principais aos usuários:
remover aquela
mudança brusca de página quando você clica em um link - em geral, os principais
controles de
navegação e interface permanecem na página e apenas o pedaço de conteúdo que você
deseja
alterar que realmente muda.

Além disso, há um aumento significativo de velocidade da carga de dados de resposta
vinda de
um servidor mais leve, visto que se trata de uma parte da página e, não, da página
inteira. Uma
carga de dados mais leve pode ser transmitida pela rede mais rapidamente e o
navegador pode
incorporar o novo conteúdo de forma mais rápida do que redesenhar uma
página inteiramente
nova.

Vamos resumir nosso papo? Single Page Application é apenas um website em que uma
página
não é, de fato, carregada. Em uma metodologia tradicional, um cliente faz uma
requisição a um
servidor, que retorna uma Página HTML (+CSS, JavaScript, etc) que é carregada no
cliente. Se
você clicar em outro link ou fizer qualquer outra requisição, esse processo se repetirá.

Nessa abordagem alternativa, acontece um pouco diferente! Uma requisição é feita ao
servidor e
a página retornada é renderizada no cliente. A partir daí, o cliente faz requisições
apenas de dados
ao servidor, que rapidamente os busca e retorna de volta ao cliente, que recebe, faz
o que quiser
com os dados e modifica apenas as partes da página que precisam ser modificadas. É
isso, vamos
às questões...


Conceitos Básicos

VUEJS

INCIDÊNCIA EM PROVA: MÉDIA

O VueJS é um framework JS (Javascript) utilizado para construção de interfaces de
usuário (views).
Galera, basicamente o VueJS utiliza HTML, CSS e Javascript, para fornecer um
modelo de
programação declarativo, baseado em componentes com objetivo de criar interfaces
de usuário,
com eficiência, de forma simples e rápido.

Vue.js

Tem um exemplo bem interessante no https://vuejs.org/, caso alguém tenha interesse em
navegar
por lá. Onde temos:

import { createApp } from 'vue'
createApp({

data() {

return {

count: 0

}

}

}).mount('#app')


<div id="app">

<button @click="count++">
Count is: {{ count }}

</button>

</div>

O que acabamos de ver é a demonstração de dois recursos do VueJS, com código
javascript, são
eles:

RECURSOS VUEJS I DESCRIÇÃO

RENDERIZAÇÃO DECLARATIVA Vue estende o HTML padrão com uma sintaxe de modelo que nos permite
descrever
declarativamente a saída HTML com base no estado do JavaScript


REATIVIDADE

O Vue rastreia automaticamente as mudanças de estado do JavaScript e atualiza o
DOM de forma eficiente quando as mudanças acontecem.

Podemos então perceber que o Vue é uma estrutura e ecossistema que cobre a maioria
dos recursos
comuns necessários no desenvolvimento de front-end. Todavia, o ambiente web é
extremamente
diversificado, logo as coisas que construímos na web podem variar drasticamente
em forma e
escala. Professor, como assim?

Com isso que acabei de dizer em mente, afirmo para vocês que o Vue foi projetado
para ser flexível
e adotável de forma incremental. Dependendo de cada caso de uso, o Vue pode ser
usado de
diferentes maneiras, dentre elas:

* Aprimorando HTML estático sem uma etapa de compilação

* Incorporando como Web Components em qualquer página

* Aplicativos de página única (SPA)

* Renderização do lado do servidor (SSR)

* Geração de Site Estático (SSG)

* Segmentação de desktop, celular e WebGL

Se você achou intimidante esses conceitos, fique tranquilo! Dificilmente VueJS vai cair
na sua prova,
extrapolando o velho e bom: HTML, CSS e Javascript. Por fim, no Vue para renderizar
uma lista de
elementos com base nos dados de um determinado Array basta utilizar o comando v-for.


/ 114

/


QUESTõES CoMENTADAS - VUEJS

í. (CCV / UFC - 2019) Sobre o framework Vue.js, assinale a alternativa correta.

a) Vue.js é um framework escrito em Java.

b) Templates são instâncias reutilizáveis do Vue com um nome.

c) Vue.js é considerado um framework de backend (server side).

d) Vue.js possui estruturas que possibilitam utilizar condicionais, mas não possui
estruturas de
laço.

e) Os templates do Vue.js são compostos por HTML válido que podem ser compilados por
navegadores compatíveis com as especificações e também por compiladores HTML.

Comentários:

(a) Errado. Vue é JS e, não, Java; (b) Errado. Não tem nada a ver essa definição
de Template; (c)
Errado, Vue é front end; (d) Errado, possui estruturas de laço, iguais ao JS; (e)
Correto, foi o que
vimos ao longo da aula.

Gabarito: Letra E

Item. 2. (FUNDATEC / CIGA-SC - 2020) Analise o trecho de código apresentado na Figura 5
abaixo,
retirado de uma aplicação VueJS:

<html>

<head>

<script
src="https://cdn.jsdelivr.net/npm/vue/dist/vue. js"x/script>

</head>

<body>

<div id="app">

<input type="radio" id="A" value="A" v-model="escolhida" >

<label for="one">A</label>

<br>

<input type="radio" id="B" value="B" v-model="escolhida">
clabel for="B''>B</label>

<br>

<lnput type="radio" id=*C* value="C" v-model=''escolhida">

<label for="C">C</label>

<brxbr>

<span> Alternativa escolhida:

<strong>{{ escolhida }}<strongx/span>

</div>

<script>

var app new Vue({
el: '#app',

data: {

escolhida: 'Nenhuma*

}

})

</script>

</html>

* Figura 5


00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)


É correto afirmar que:

a) Para que uma mensagem apareça corretamente no navegador com o valor do "radio
button"
selecionado, é necessário implementar um "listener" vinculado ao evento "onchange".

b) VueJS faz uma ligação unidirecional entre o valor e o banco de dados por meio da
diretiva
"vmodel".

c) VueJS faz uma ligação bidirecional entre o valor e a camada de acesso ao banco de dados
por
meio da diretiva "v-model".

d) VueJS faz uma ligação bidirecional entre o valor dos elementos "input" e os dados,
ao mesmo
tempo em que mostra o valor na tela utilizando sintaxe de template.

e) VueJS faz uma ligação bidirecional entre o valor e os dados e os elementos
"input", mas é
necessário utilizar a propriedade "computed" do componente "app" no lugar da
propriedade
"data".

Comentários:

Pessoal, apesar da questão parecer complexa, a alternativa D está tão correta
que basta
analisarmos o código: VueJS faz uma ligação bidirecional entre o valor e os dados e
os elementos
"input", mas é necessário utilizar a propriedade "computed" do componente "app"
no lugar da
propriedade "data"? Sim. Utiliza a sintaxe de template e mostra o valor na tela? Sim.

Gabarito: Letra D

Item. 3. (AOCP / PRODEB - 2018) Com base no Framework VueJS, qual é uma das diretivas
possíveis
utilizada para renderizar uma lista de elementos com base nos dados de um determinado Array?

a) v-for
b) track-by
c) concat()

d) slice()

e) data

Comentários:

Conforme vimos, uma das diretrizes para renderizar uma lista de elementos com base nos
dados
de um determinado Array é o v-for.

Gabarito: Letra A


Item. 4. (CCV / UFC - 2019) Sobre Vue.Js, assinale a alternativa correta.

a) Mixins geralmente acrescentam funcionalidade ao Vue em nível global.

b) O Vue.js permite definir filtros que podem ser usados para aplicar
formatação de texto
comum.

c) Pipes permitem que sejam declaradas as transformações de valor de
exibição em
seu template HTML

d) Plugins são uma forma flexível de distribuir funcionalidade
reutilizável em diversos
componentes Vue.

e) O trabalho de um Slot é aplicar efeitos colaterais de maneira reativa ao DOM
quando o valor
de sua expressão é alterado.

Comentários:

Pessoal, o Vue.js permite definir filtros que podem ser usados para aplicar formatação
de texto
comum, nada de novo não é verdade, afinal estamos falando de um framework javascript
focado
em interfaces de usuário.

Gabarito: Letra B

Item. 5. (CCV / UFC - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo
contém
apenas frameworks/bibliotecas/plataformas que foram desenvolvidas ou que dependem de
JavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

Comentários:

Só para nos lembrar que VueJS é um framework JS (Javascript) utilizado para
construção de
interfaces de usuário (views).

Gabarito: Letra C

Item. 6. (QUESTÃO INÉDITA) O framework Vue.js estende o HTML padrão com uma sintaxe de
modelo
que nos permite descrever declarativamente a saída HTML com base no estado do JavaScript.

Comentários:


/ 114

/


Perfeito! Foi o que vimos, que o framework Vue.js estende o HTML padrão com uma
sintaxe de
modelo que nos permite descrever declarativamente a saída HTML com base no
estado do
JavaScript.

Gabarito: Correto

Item. 7. (QUESTÃO INÉDITA) O VueJS não rastreia automaticamente as mudanças de
estado do
JavaScript e atualiza o DOM de forma eficiente quando as mudanças acontecem.

Comentários:

Ao contrário, o VueJS rastreia automaticamente as mudanças de estado do JavaScript e
atualiza o
DOM de forma eficiente quando as mudanças acontecem.

Gabarito: Errado

Item. 8. (QUESTÃO INÉDITA) O VueJS é uma estrutura e ecossistema que cobre a maioria dos
recursos
comuns necessários no desenvolvimento de front-end.

Comentários:

Perfeito! O VueJS é uma estrutura e ecossistema que cobre a maioria dos
recursos comuns
necessários no desenvolvimento de front-end.

Gabarito: Correto

Item. 9. (QUESTÃO INÉDITA) O VueJS é um framework JS (Javascript) utilizado para construção
de
interfaces de usuário (views).

Comentários:

Perfeito! O VueJS é um framework JS (Javascript) utilizado para construção de
interfaces de usuário
(views).

Gabarito: Correto

10.(QUESTÃO INÉDITA) O VueJS foi projetado para ser flexível e
adotável de forma
incremental. Dependendo de cada caso de uso, o Vue pode ser usado de diferentes
maneiras,
dentre elas, aprimorando HTML estático sem uma etapa de compilação.

Comentários:


/ 114

/


Exato! O VueJS foi projetado para ser flexível e adotável de forma incremental.
Dependendo de
cada caso de uso, o Vue pode ser usado de diferentes maneiras, dentre elas,
aprimorando HTML
estático sem uma etapa de compilação.

Gabarito: Correto


/ 114

/


LISTA DE QUESTõES - VUEJS

í. (CCV / UFC - 2019) Sobre o framework Vue.js, assinale a alternativa correta.

a) Vue.js é um framework escrito em Java.

b) Templates são instâncias reutilizáveis do Vue com um nome.

c) Vue.js é considerado um framework de backend (server side).

d) Vue.js possui estruturas que possibilitam utilizar condicionais, mas não possui
estruturas de
laço.

e) Os templates do Vue.js são compostos por HTML válido que podem ser compilados por
navegadores compatíveis com as especificações e também por compiladores HTML.

Item. 2. (FUNDATEC / CIGA-SC - 2020) Analise o trecho de código apresentado na Figura 5 abaixo,
retirado de uma aplicação VueJS:

<html>

<head>

<script
src="https://cdn.jsdelivr.net/npm/vue/dist/vue. js"x/script>

</head>

<body>

<div id="app">

<input type="radio" id="A" value="A" v-model="escolhida" >

<label for="one">A</label>

<br>

<input type="radio" id="B" value="B" v-model="escolhida">

<label for="B">B</label>

<br>

<input type="radio" id="C" value="C" v-model="escolhida">

<label for="C">C</label>

<brxbr>

<span> Alternativa escolhida:

<strong>{{ escolhida }}<strongx/span>

</div>

<script>

var app = new Vue({
el: '#app',

data: {

escolhida: 'Nenhuma'

}

})

</script>

</html>

Figura 5

É correto afirmar que:

a) Para que uma mensagem apareça corretamente no navegador com o valor do "radio
button"
selecionado, é necessário implementar um "listener" vinculado ao evento "onchange".

b) VueJS faz uma ligação unidirecional entre o valor e o banco de dados por meio da
diretiva
"vmodel".


c) VueJS faz uma ligação bidirecional entre o valor e a camada de acesso ao banco de
dados por
meio da diretiva "v-model".

d) VueJS faz uma ligação bidirecional entre o valor dos elementos "input" e os dados,
ao mesmo
tempo em que mostra o valor na tela utilizando sintaxe de template.

e) VueJS faz uma ligação bidirecional entre o valor e os dados e os elementos
"input", mas é
necessário utilizar a propriedade "computed" do componente "app" no lugar da
propriedade
"data".

Item. 3. (AOCP / PRODEB - 2018) Com base no Framework VueJS, qual é uma das diretivas
possíveis
utilizada para renderizar uma lista de elementos com base nos dados de um determinado Array?

a) v-for
b) track-by
c) concat()

d) slice()

e) data

Item. 4. (CCV / UFC - 2019) Sobre Vue.Js, assinale a alternativa correta.

a) Mixins geralmente acrescentam funcionalidade ao Vue em nível global.

b) O Vue.js permite definir filtros que podem ser usados para aplicar
formatação de texto
comum.

c) Pipes permitem que sejam declaradas as transformações de valor de
exibição em
seu template HTML

d) Pluginssão uma forma flexível de distribuir funcionalidade
reutilizável em diversos
componentes Vue.

e) O trabalho de um Slot é aplicar efeitos colaterais de maneira reativa ao DOM
quando o valor
de sua expressão é alterado.

Item. 5. (CCV / UFC - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo
contém
apenas frameworks/bibliotecas/plataformas que foram desenvolvidas ou que dependem de
JavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

Item. 6. (QUESTÃO INÉDITA) O framework Vue.js estende o HTML padrão com uma sintaxe de
modelo
que nos permite descrever declarativamente a saída HTML com base no estado do JavaScript.


/ 114

/


Item. 7. (QUESTÃO INÉDITA) O VueJS não rastreia automaticamente as mudanças de
estado do
JavaScript e atualiza o DOM de forma eficiente quando as mudanças acontecem.

Item. 8. (QUESTÃO INÉDITA) O VueJS é uma estrutura e ecossistema que cobre a maioria dos
recursos
comuns necessários no desenvolvimento de front-end.

Item. 9. (QUESTÃO INÉDITA) O VueJS é um framework JS (Javascript) utilizado para construção
de
interfaces de usuário (views).

Item. 10. (QUESTÃO INÉDITA) O VueJS foi projetado para ser flexível e
adotável de forma
incremental. Dependendo de cada caso de uso, o Vue pode ser usado de diferentes
maneiras,
dentre elas, aprimorando HTML estático sem uma etapa de compilação.


/ 114

/


GABARITo - VUEJS


Item. 1. LETRA E 5- LETRA C

Item. 2. LETRA D 6. CORRETO

3- LETRA A 7- ERRADO

4- LETRA B 8. CORRETO

Item. 9. CORRETO
ío.CORRETO


Conceitos Básicos

REACTJS

INCIDÊNCIA EM PROVA: MÉDIA

O React ou ReactJS nada mais é que uma biblioteca para construir interfaces de
usuários com
JavaScript. Uma coisa interessante é que essa biblioteca foi criada pela galera do
Facebook e
Instagram. É interessante notar que a documentação oficial coloca o ReactJS como o V
(Visão) do
Modelo MVC, isto é, permitindo a criação de seus próprios componentes reutilizáveis de
interface.
Como assim?

Em uma aplicação em React, recomenda-se quebrar seus diferentes elementos em
pequenos
componentes reutilizáveis. Em outras palavras, cada vez que tivermos que
desenvolver algo for
muito complexo, recomenda-se quebrá-lo em pequenas partes e desenvolver em componentes -é
o chamado Component-Driven Development.

Professor, eu conheço o AngularJS - ReactJS é a mesma coisa? Não, o AngularJS é um
framework,
ou seja, um conjunto de ferramentas para resolver vários tipos de coisas. Já uma
biblioteca serve
para resolver uma coisa específica - no caso do React é renderizar componentes. Como
ele foi
desenvolvido para resolver um problema particular, ele é extremamente performático. Vamos
ver
algumas de suas vantagens:

FACILIDADE DE SE CRIAR COMPONENTES PEQUENOS E REUTILIZÁVEIS

Não esqueça disso, porque é fundamental entender que estamos afinal de contas tratando
de uma
biblioteca para construir interfaces de usuários com JS. Ok? E o que mais temos:

UTILIZA A ABORDAGEM VIRTUAL DOM E PODE RODAR DO LADO SERVIDOR

Galera, o que você acabou de ler é uma super vantagem do ponto de vista de SEO
(Search Engine
Optimization), para quem não sabe, o SEO é um conjunto de estratégias com
o objetivo de
potencializar e melhorar o posicionamento de um site nas páginas de resultados naturais
nos sites
de busca.

O ReactJS não depende exclusivamente do DOM (document object model) do navegador, uma
vez
que mantém um DOM virtual próprio.

UNIFICA 0 MARKUP E A LÓGICA DA VIEW, FACILITANDO A EXTENSÃO E MANUTENÇÃO


Pois é, a grande sacada do ReactJS é o Virtual DOM! Todo mundo sabe que manipular o
DOM da
página é muito custoso e lento. Costuma-se evitar ao máximo manipulá-lo em excesso,
porque isso
exige bastante do navegador. O ReactJS minimiza a quantidade de manipulação
do DOM
mantendo seu próprio DOM virtual e somente renderizando quando necessário.

Quando um componente é inicializado, o método render é chamado, gerando uma
representação
da view. Quando algum dado muda, o método render é chamado novamente e para que
tenhamos
uma atualização mais eficiente possível, o React faz uma diferenciação (diff) do valor
novo com o
valorvelho e aplica no DOM somente a nova mudança.

São características do React ser uma biblioteca declarativa, que gerencia seu próprio
virtual DOM
e permite a criação de aplicativos móveis.

Pessoal, não confundam ReactJS com React Native, o React Native é uma biblioteca
Javascript
criada pelo Facebook. É usada para desenvolver aplicativos para os sistemas Android e
IOS de
forma nativa.

O que vocês precisam de fato saber é que o DOM da página raramente é manipulado
diretamente.
Opta-se por manipular um DOM virtual e aplicam-se apenas as mudanças no DOM real.
Como isso
se relaciona com a componentização? Bem, todo componente React possui dois atributos
principais:
estado (state) e propriedades (props) - no React, tudo precisa ser subclasse da classe Component.

Toda vez que o estado de um componente é alterado, ele é renderizado — este é o
famoso
JavaScript reativo (que dá nome à biblioteca). Da mesma forma que criamos nossas
Classes e
Métodos, devemos pensar o mesmo para os nossos componentes e seguir o
princípio da
responsabilidade única. Onde uma classe deve fazer apenas uma coisa, deve fazê-la bem
e deve
fazer somente ela.

No ReactJS, os componentes são máquinas de estado, sendo que o fluxo de informações
tende a
ser unidirecional no ReactJS. Por fim, cabe salientar que os componentes ReactJS são
tipicamente
escritos em JSX (uma sintaxe de extensão Javascript que permite escrever tags HTML
dentro do
JavaScript para renderizar subcomponentes). Porfim, no ReactJS temos algumas funções básicas:

FUNÇÕES | DESCRIÇÃO

Refs fornecem uma forma de acessar os nós do DOM ou elementos React criados


REFS

no método render.


PROPS

Props é uma palavra-chave especial no React, que significa propriedades e está
sendo usada para passar dados de um componente para outro.


STATE

State é gerenciado de dentro do componente (como variáveis declaradas dentro
de uma função.

x


/ 114

/


Key são úteis ao trabalhar com componentes criados dinamicamente ou quando
suas listas são alteradas pelos usuários. A definição do valor da chave manterá seus
componentes identificados de maneira única após a alteração.

Elementsum elemento é um objeto simples que descreve uma instância de
componente ou nó DOM e suas propriedades desejadas.

(TRE-RS - 2015) Na escolha de um framework e bibliotecas para apoiar a utilização do
JavaScript, uma empresa levou em consideração algumas afirmações apresentadas por
sua equipe técnica. Com base nesse contexto, assinale a opção correta.

a) O ReactJS não depende exclusivamente do DOM (document object model) do
navegador, uma vez que mantém um DOM virtual próprio.

b) O AngularJS está baseado na manipulação pelo desenvolvedor da sincronização entre
a camada de visão, fornecida pelo código HTML, e o modelo, e vice-versa.

c) Segundo os princípios adotados pelo AngularJS, o código declarativo é melhor para
expressara lógica do negócio.

d) A forma primária de organizar as interfaces no Ember.js são os templates escritos em
JavaScript que definem o seu comportamento.

e) Os projetos Ember.js podem ser criados e gerenciados por uma ferramenta de linha
de comando denominada Ember Loc.

Comentários: Não cabe aqui analisar matéria estranha ao nosso caso em específico, que é 0 REACJS,
todavia já conseguimos
ver 0 que acabamos de estudar, não é verdade? Logo, 0 ReactJS - conforme vimos - não depende
exclusivamente do DOM do
navegador, já que tem um DOM virtual própria (Letra A).


/ 114

/


QUESTõES CoMENTADAS - REACTJS

í. (UFC / CCV-UFC - 2019) Em React.Js, como são chamadas as entradas que são
passadas na
criação dos componentes React, usando uma convenção de nomenclatura semelhante
aos
atributos de tag HTML.

a) Refs
b) Props
c) State
d) Keys
e) Elements

Comentários:

Basta lembrar do que vimos não é verdade:

FUNÇÕES | DESCRIÇÃO
|

Refs fornecem uma forma de acessar os nós do DOM ou elementos React criados


REFS

no método render.


PROPS

Props é uma palavra-chave especial no React, que significa propriedades e está
sendo usada para passar dados de um componente para outro.


STATE

State é gerenciado de dentro do componente (como variáveis declaradas dentro
de uma função.


KEY

ELEMENTS

Key são úteis ao trabalhar com componentes criados dinamicamente ou quando
suas listas são alteradas pelos usuários. A definição do valor da chave manterá seus
componentes identificados de maneira única após a alteração.

Elements um elemento é um objeto simples que descreve uma instância de
componente ou nó DOM e suas propriedades desejadas.

Gabarito: Letra B

Item. 2. (COMPERVE / TJ-RN - 2020) O React é uma biblioteca JavaScript de
código aberto e,
atualmente, é uma das ferramentas mais populares entre os desenvolvedores web.
São
características do React ser uma biblioteca:

a) declarativa, que não gerencia seu próprio virtual DOM e não permite a criação de
aplicativos
móveis.

b) imperativa, que não gerencia seu próprio virtual DOM e não dá suporte a
componentes
reutilizáveis.

x53


/ 114

/


c) declarativa, que gerencia seu próprio virtual DOM e permite a criação de aplicativos móveis.

d) imperativa, que gerencia seu próprio virtual DOM e dá suporte a componentes reutilizáveis.

Comentários:

Só lembrar o que estudamos, logo React é uma biblioteca declarativa, que gerencia seu
próprio
virtual DOM e permite a criação de aplicativos móveis.

Gabarito: Letra C

Item. 3. (CESPE / SLU-DF - 2019) Julgue o próximo item, relativos à linguagem
de programação
JavaScript e às ferramentas Node e React.

O JSX (JavaScript Syntax Extension) é de uso obrigatório no React e permite inserir a
interface
do usuário no código JavaScript

Comentários:

Não existe isso de "uso obrigatório no React". React não requer JSX. Lembre-se: O
React (também
denominado React. js ou ReactJS) é uma biblioteca JavaScript de código aberto com foco
em criar
interfaces de usuário (frontend) em páginas web.

Gabarito: Errado

Item. 4. (CESPE / SLU-DF - 2019) Julgue o próximo item, relativos à linguagem
de programação
JavaScript e às ferramentas Node e React.

O Node.js é capaz de gerar conteúdos dinâmicos rodando JavaScript no servidor, porém
não
tem a capacidade de acessar banco de dados.

Comentários:

Professor, mas o tema não era ReactJS ao invés de NodeJS? Sim, porém coloquei essa questão para
vocês perceberem essa sutil diferença, veja o NodeJS pode ser utilizado para consulta
em banco de
dados, dai já tiramos que a questão está errada. A diferença entre o NodeJS e o
ReactJS, mora no
fato de que o NodeJS é um interpretador, com código aberto, de código
JavaScript de modo
assíncrono e orientado a eventos, focado em migrara programação do Javascript do lado
do cliente
para os servidores, criado assim aplicações de alta escalabilidade.

Gabarito: Errado

Item. 5. (AOCP / PRODEB - 2018) Qual é a linguagem utilizada no desenvolvimento da
biblioteca de
frontend chamada React?


/ 114

/


a) Java
b) Ruby on Rails
c) CSS

d) .NET

e) JS

Comentários:

Temos obviamente o Javascript (JS) como linguagem utilizada para o
desenvolvimento da
biblioteca frontend React.

Gabarito: Letra E

Item. 6. (CCV / UFC - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo
contém
apenas/ramewo/Trs/bibliotecas/plataformas que foram desenvolvidas ou que dependem
de
JavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

Comentários:

Seguindo a ordem framework, biblioteca e plataforma, temos: Angular -
Framework, React -
Biblioteca e Vue.JS - Plataforma.

Gabarito: Letra C

Item. 7. (CESPE / SLU-DF-2019) React Native utiliza componentes nativos em vez de
componentes da
Web como blocos de construção, existindo dois tipos de dados que controlam um
componente:
state, definido pelo pai e fixado durante todo o tempo de vida de um componente; e
props,
utilizado para os dados que irão mudar.

Comentários:

Até aqui tudo correto: React Native utiliza componentes nativos em vez de componentes
da Web
como blocos de construção, existindo dois tipos de dados que controlam um componente.

A partir daqui temos o seguinte: State (Estado): É o estado interno do componente. É
definido e
controlado pelo próprio componente e muda ao longo de sua vida e Props (Propriedades): São
recebidas pelo componente pai, são fixas (imutáveis) por toda vida do
componente. Na dúvida
basta lembrar:

FUNÇÕES | DESCRIÇÃO

Refs fornecem uma forma de acessar os nós do DOM ou elementos React criados


REFS

no método render.


PROPS

Props é uma palavra-chave especial no React, que significa propriedades e está
sendo usada para passar dados de um componente para outro.


STATE

State é gerenciado de dentro do componente (como variáveis declaradas dentro
de uma função.


KEY

ELEMENTS

Key são úteis ao trabalhar com componentes criados dinamicamente ou quando
suas listas são alteradas pelos usuários. A definição do valor da chave manterá seus
componentes identificados de maneira única após a alteração.

Elementsum elemento é um objeto simples que descreve uma instância de
componente ou nó DOM e suas propriedades desejadas.

Gabarito: Errado

Item. 8. (FCC / METRO-SP - 2019) Um Analista precisa desenvolver um aplicativo móvel para
celulares
com sistemas operacionais Android e iOS. Para isso, poderá utilizar o framework
desenvolvido
pela equipe do Facebook, que possibilita o desenvolvimento de aplicações mobile
utilizando
bibliotecas JavaScript para criar interfaces de usuário. Esse framework é conhecido como:

a) lonic Builder.

b) Flutter Script.

c) Cordova.

d) Xamarín Core.

e) React Native.

Comentários:

Conforme estudamos, trata-se do framework React Native. Lembre-se: React Native
é uma
biblioteca Javascript criada pelo Facebook. É usada para desenvolver aplicativos para os
sistemas
Android e IOS de forma nativa.

Gabarito: Letra E

Item. 9. (UEPB / CPCON - 2018) De acordo com o ciclo de vida de um componente no
React.js, assinale
a alternativa em que todos os métodos são considerados como Updating:

a) getStateQ, forceUpdateQ e renderQ

x


/ 114

/


b) constructor() e componentWillMount()

c) componentDidMount() e componentWillUnmount()

d) componentWillReceiveProps(), static getDerivedStateFromProps() e render()

e) componentDidCatch(), constructor() e render()

Comentários:

Pessoal, os métodos considerados Updating são
componentWillReceiveProps(), static
getDerivedStateFromPropsO e render().

Gabarito: Letra D

io.(AOCP / PRODEB - 2018) O React é uma biblioteca utilizada para
desenvolvimento de
interfaces (frontend) que tem como base o princípio do desenvolvimento de componentes. O
React utiliza-se de uma técnica de dividir as estruturas complexas em partes
menores e
desenvolver para cada uma delas um componente. Como é o nome dessa técnica?

a) Component Driven Development.

b) Component Development Structured.

c) Driven Component Divided.

d) Work Driven Structured.

e) Development React Structured.

Comentários:

Conforme estudamos, o React é uma biblioteca CDD (Component Driven Development).

Gabarito: Letra A

n.(ASP / Câmara de Sorocaba - 2022) Considere que foi criado um projeto
padrão em react
utilizando o create-react-app. Onde, por padrão, ficarão armazenadas todas as
dependências
de bibliotecas utilizadas?

a) Na pasta src.

b) No arquivo .gitignore
c) No arquivo package.json
d) No arquivo index.

e) Na pasta node_modules.

Comentários:

Questão fora da curva, mas por padrão, os projetos no react, ficam
armazenados na pasta
node_modules.

x


/ 114

/


Gabarito: Letra E

i2.(FEPESE / CELESC - 2022) Assinale a alternativa que apresenta um framework open
source,
escrito em Java, que permita a geração de relatórios na plataforma Java.

a) REACT

b) DJANGO

c) NODEJS

d) CRISTALREPORTS

e) JASPERREPORTS

Comentários:

Trata-se do JasperReports! Obviamente o React nada tem aver, além de ser escrito em
Javascript
e, não, em Java.

Gabarito: Letra E

Item. 13. (AOCP / UFFS - 2019) Um SGBD é um sistema responsável por realizar o gerenciamento de
um
banco de dados, com recursos que permitem a manipulação das informações e a interação
com
os usuários do sistema. Dentre as seguintes alternativas, qual apresenta apenas
sistemas
específicos de SGBD?

a) SQL Server, Oracle, REST e GIT.

b) React, .NET, MySQL e SQL Server.

c) Acess, CSS, Oracle e VueJS.

d) MySQL, Oracle, SQL Server e Acess.

e) GIT, REST, VueJS e Oracle.

Comentários:

Como podemos ver, a banca pode e vai misturar temas diferentes, neste caso a única
opção de
SGBDs é MySQL, Oracle, SQL Server e Acess. Obviamente, React não é SGBD.

Gabarito: Letra D


LISTA DE QUESTõES - REACTJS

í. (UFC / CCV-UFC - 2019) Em React.Js, como são chamadas as entradas que são
passadas na
criação dos componentes React, usando uma convenção de nomenclatura semelhante
aos
atributos de tag HTML.

a) Refs
b) Props
c) State
d) Keys
e) Elements

Item. 2. (COMPERVE / TJ-RN - 2020) O React é uma biblioteca JavaScript de
código aberto e,
atualmente, é uma das ferramentas mais populares entre os desenvolvedores web.
São
características do React ser uma biblioteca:

a) declarativa, que não gerencia seu próprio virtual DOM e não permite a criação de
aplicativos
móveis.

b) imperativa, que não gerencia seu próprio virtual DOM e não dá suporte a
componentes
reutilizáveis.

c) declarativa, que gerencia seu próprio virtual DOM e permite a criação de aplicativos móveis.

d) imperativa, que gerencia seu próprio virtual DOM e dá suporte a componentes reutilizáveis.

Item. 3. (CESPE / SLU-DF - 2019) Julgue o próximo item, relativos à linguagem
de programação
JavaScript e às ferramentas Node e React.

O JSX (JavaScript Syntax Extension) é de uso obrigatório no React e permite inserir a
interface
do usuário no código JavaScript

Item. 4. (CESPE / SLU-DF - 2019) Julgue o próximo item, relativos à linguagem
de programação
JavaScript e às ferramentas Node e React.

O Node.js é capaz de gerar conteúdos dinâmicos rodando JavaScript no servidor, porém
não
tem a capacidade de acessar banco de dados.

Item. 5. (AOCP / PRODEB - 2018) Qual é a linguagem utilizada no desenvolvimento da
biblioteca de
frontend chamada React?

a) Java
b) Ruby on Rails
c) CSS

d) .NET


e)JS

Item. 6. (CCV / UFC - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo
contém
apenas/rameworÁrs/bibliotecas/plataformas que foram desenvolvidas ou que dependem
de
JavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

Item. 7. (CESPE/SLU-DF-2019) React Native utiliza componentes nativos em vez de componentes
da
Web como blocos de construção, existindo dois tipos de dados que controlam um
componente:
state, definido pelo pai e fixado durante todo o tempo de vida de um componente; e
props,
utilizado para os dados que irão mudar.

Item. 8. (FCC / METRO-SP - 2019) Um Analista precisa desenvolver um aplicativo móvel para
celulares
com sistemas operacionais Android e iOS. Para isso, poderá utilizar o framework
desenvolvido
pela equipe do Facebook, que possibilita o desenvolvimento de aplicações mobile
utilizando
bibliotecas JavaScript para criar interfaces de usuário. Esse framework é conhecido como
a) lonic Buiider.

b) Flutter Script.

c) Cordova.

d) Xamarin Core.

e) React Native.

Item. 9. (UEPB / CPCON - 2018) De acordo com o ciclo de vida de um componente no
React.js, assinale
a alternativa em que todos os métodos são considerados como Updating:

a) getState(), forceUpdate() e render()

b) constructor() e componentWillMount()

c) componentDidMount() e componentWillUnmount()

d) componentWillReceivePropsO, static getDerivedStateFromProps() e render()

e) componentDidCatchO, constructor() e renderQ

io.(AOCP / PRODEB - 2018) O React é uma biblioteca utilizada para
desenvolvimento de
interfaces (frontend) que tem como base o princípio do desenvolvimento de componentes. O
React utiliza-se de uma técnica de dividir as estruturas complexas em partes
menores e
desenvolver para cada uma delas um componente. Como é o nome dessa técnica?

a) Component Driven Development.

b) Component Development Structured.


/ 114

/


c) Driven Component Divided.

d) Work Driven Structured.

e) Deveiopment React Structured.

n.(ASP / Câmara de Sorocaba - 2022) Considere que foi criado um projeto
padrão em react
utilizando o create-react-app. Onde, por padrão, ficarão armazenadas todas as
dependências
de bibliotecas utilizadas?

a) Na pasta src.

b) No arquivo .gitignore
c) No arquivo package.json
d) No arquivo index.

e) Na pasta node_modules.

Item. 12. (FEPESE / CELESC - 2022) Assinale a alternativa que apresenta um framework open
source,
escrito em Java, que permita a geração de relatórios na plataforma Java.

a) REACT

b) DJANGO

c) NODEJS

d) CRISTALREPORTS

e) JASPERREPORTS

Item. 13. (AOCP / UFFS - 2019) Um SGBD é um sistema responsável por realizar o
gerenciamento de um
banco de dados, com recursos que permitem a manipulação das informações e a interação
com
os usuários do sistema. Dentre as seguintes alternativas, qual apresenta apenas
sistemas
específicos de SGBD?

a) SQL Server, Oracle, REST e GIT.

b) React, .NET, MySQL e SQL Server.

c) Acess, CSS, Oracle e VueJS.

d) MySQL, Oracle, SQL Server e Acess.

e) GIT, REST, VueJS e Oracle.


GABARITo - REACTOS

Item. 1. LETRA B 6. LETRA C
li. LETRA E

Item. 2. LETRA C 7. ERRADO
Item. 12. LETRA E

Item. 3. ERRADO 8. LETRA E
Item. 13. LETRA D

Item. 4. ERRADO 9. LETRA D

Item. 5. LETRA E io. LETRA A


0 0


Conceitos Básicos

ANGULARJS

INCIDÊNCIA EM PROVA: MÉDIA

Pessoal, antes de apresentar os dois frameworks, vou contar um pouco da história de
como eles
começaram. Galera, quem nasceu antes dos anos 90, vai lembrar que o início da
internet aconteceu
com páginas HTML estáticas, ou com pouquíssimo nível de dinamicidade (um contador de
cliques
aqui, um nome de usuário em tela ali...). Nessa época a internet era lenta, e os
navegadores
extremamente simples.

O tempo passa, e a capacidade de processamento do seu computador pessoal
aumenta
exponencialmente, junto com a velocidade da internet. Mais ou menos nesse período, o
Google
ganha muita força, e começa a expandir sua presença na internet, não só como
mecanismo de
busca, mas como um fornecedor de serviços completamente hospedados na web - Gmail,
Orkut
(quem se lembra desse?), Google Calendar, etc.

Pessoal, um dos grandes fatores que fez o Google bombarfoi porque eles pensaram: oras,
podemos
fazer aplicações inteiras rodarem dentro dos navegadores! Isso é uma maneira
completamente
diferente de pensar na arquitetura server-side, onde você processa a página inteira do
lado servidor,
e retorna somente um HTML para ser mostrado no navegador do cliente.

A arquitetura proposta pelo Google foi enviartodo HTML (na verdade HTML, Javascript e
CSS) para
o navegador do cliente na primeira requisição, e através de códigos Javascript, o
próprio navegador
vai montando a página. O navegador só precisa pedir os dados (normalmente
JSON) para
preencher a parte de conteúdo. Perceba a diferença: ao invés de pedir HTML montado e
só mostrar
o resultado, o navegador passou a pedir dados JSON, e ele mesmo montar a tela.

Galera, esse modelo de receber todo layout/estrutura na primeira requisição (e
depois só pedir
dados) é o que se chama de SPA-Single Page Aplication. Por um lado, ele é muito
mais responsivo
e eficiente (o cliente consulta só dados, ao invés de dados+html), mas por outro lado
existe muito
mais processamento do lado cliente (exige-se muito mais do navegador). Nesse contexto
surgiu o
AngularJS - O primeiro framework SPA "endossado" pelo Google.

Caros alunos (as), vocês já devem conhecer o Modelo MVC! Ele é bastante
utilizado por
desenvolvedores back-end com o intuito de separar o código de maneira mais organizada
e facilitar
a manutenção! Já os desenvolvedores front-end tinham mais dificuldades de organizar seu
código.
Dessa forma, alguém teve a ideia de também utilizar o mesmo modelo para o
desenvolvimento
front-end.

A partir daí, foram lançados um bocado de frameworks de desenvolvimento front-end que
utilizam
o Modelo MVC. Quais, professor? Knockout, Backbone.js, Ember, batman.js, e... AngularJS! Trata-


se de um framework JavaScript (MVC), criado pela Google, cujo objetivo é construir
aplicações web
client-side simples e fáceis de manter por meio de componentes reusáveis e modulares.

O AngularJS é escrito inteiramente em JavaScript! Ele é um potencializador para
aplicações HTML

- ele adota uma abordagem mais ligada à sintaxe HTML, funcionando como uma
extensão da
linguagem e enriquecendo seu vocabulário. Além disso, ele é extremamente
modularizado,
facilitando a automação de testes (ngMock)! Ele oferece suporte a Single Page
Applications (SPA)
e Web Mobile.

Ele fornece a infraestrutura necessária para integrar com o back-end por meio de Ajax
- tudo isso
embarcado no framework, sem necessidade de outras ferramentas ou bibliotecas. O
AngularJS não
é uma biblioteca JavaScript (como JQuery); ele não é uma plataforma (como Java ou
.Net); ele não
é uma linguagem (como C#); ele não é um plug-in; e ele também não é uma extensão do navegador.

Ele se encaixa melhor na definição de um framework, mesmo que seja muito mais leve
do que um
framework típico e é por isso que muitos o confundem com uma biblioteca.
Ele é totalmente
JavaScript, totalmente client-side e é compatível com desktop e navegadores móveis.
Dessa forma,
ele definitivamente não é um plug-in ou alguma outra extensão do navegador nativo.

No parágrafo anterior eu escrevi algo que deve ter deixado uma pulga atrás da orelha
de vocês:
AngularJS é totalmente client-side! Pois é! A aplicação roda inteiramente no navegador
do cliente.
Professor, funciona em todos os navegadores? Em geral, sim - tanto desktop
quanto mobile.
Professor, e a performance? Bem, pesa um pouquinho o cliente, mas em geral são aplicações leves.

Pessoal, uma das coisas mais legais do AngularJS é uma coisa chamada
Two-Way Databind
(Associação de Dados e Mão-Dupla). Com essa forma, podemos associar uma variável
Javascript a
um campo HTML, de tal forma que se a variável mudar, o HTML será atualizado, e vice-versa.

Existem alguns mecanismos para fazer isso acontecer. Veja o exemplo abaixo, associando
a variável
firstname ao conteúdo que será mostrado dentro de <p> no HTML:

Código Javascript
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {

$scope.firstname = "João";

$scope.lastname = "Pedro";

});

Pessoal, veja no exemplo acima duas formas de fazer o Two-Way Databind. Ambas precisam
que
exista a variável firstname dentro de $scope no Javascript. Mas podemos fazer a
associação de 2
formas no HTML: via ng-bind, ou via interpolação de string. O ng-bind utiliza o nome
da variável, e
modifica o conteúdo da tag <p> com o valor da variável. O segundo chama-se
interpolação de


/ 114

/


strings, mas tem como apelido "bigodes" (por causa das chaves {{}}). Nesse segundo,
AngularJS vai
tentar resolver o que estiver entre os bigodes, e retornará o resultado para aparecer
no HTML. São
formas semelhantes de obter o mesmo resultado.

Código HTML (versão ng-bind)

<p ng-bind="firstname"x/p>

Código HTML (versão "bigodes" - interpolação de strings)

<p>First name: {{firstname}}</p>

E quanto à segurança? Pois é, seu código trafega abertamente até o front-end, no
entanto é
possível minificar o código, isto é, remover todos os caracteres desnecessários do
código-fonte
sem modificar sua funcionalidade. Torna-se impossível roubar um código? Não, mas
dificulta um
bocado! Vejam a imagem abaixo como é complicado entender alguma coisa assim:

runccxon var q = \ vercicax; rtx; sv
nitCallback: null, setupCallback: null, reloadCallt
temLastOutCallback: null, itemVisiblelnCallback: ni
iv>", buttonNextEvent: "click", buttonPrevEvent: "
"load.jcarousel", function () { m = !0 }); g.jcarot
his.buttonPrevState = this.buttonNextState = this.L
his.options.rtl = (g(a).attr("dir") || g("html").a
his.options.vertical ? this.options.rtl ? "right"

kin") != -1) { g(a).removeClass(d[f]); b = d[f); b
his.list.parents(".jcarousel-clip"), this.containe
his.clip = this.container.find(".jcarousel-clip"))
his.container = this.clip.wrap("<div></div>").parer
lass=" ' + b + *"></div>*); this.buttonPrev « g(".
his.buttonPrev = g(this.options.buttonPrevHTML).apf
ext", this.container); if (this.buttonNext.size()

this. buttonNext. addClass (this. classNameí ""jcarousel

MAS AFINAL DE CONTAS, POR QUE USAR ANGULAR?

Pessoal, utiliza-se o Angular porque se ganha muito em produtividade por conta dos
componentes
reusáveis; porque o risco de ele ser descontinuado é muito baixo - lembrem-se que ele
é mantido
pelo Google; a comunidade é absurdamente ativa, auxiliando os desenvolvedores; porque a
curva
de aprendizado é relativamente baixa; entre tantas outras vantagens.

Mas e as evoluções do Angular? O que aconteceu foi que, apesar de todos os motivos
para o
AngularJS dar certo, ele não deu. Começaram a aparecer grandes concorrentes
"roubando" o
mercado do desenvolvimento WEB, como o Vue.js, React e Ember. Foi aí que surgiu o Angular 2.0.

E 0 que é 0 Angular 2.0? Ele é um framework JavaScript e foi completamente
reescrito, guardando
poucas coisas do AngularJS. De fato, AngularJS e Angular 2 estão tão próximos como
Java e
Javascript... O Framework perdeu o ".js" no final, e passou a ser conhecido apenas
como Angular.
Um ponto a ressaltar é que, a partir da versão 2, todas as versões seguintes são
evoluções naturais


/ 114

/


da anteriores. Assim, Angular 2 evoluiu para o Angular 3, depois para o Angular 4, e
assim por
diante. A única mudança que rompeu completamente com a estrutura anterior foi do
Angular.JS
para Angular 2. Para fins de nomenclatura, chamaremos sempre que você vir Angular sem
o JS,
entenda que são as versões 2+.

Aplicações Angular são desenvolvidas, por padrão, em TypeScript. TypeScript é uma
linguagem de
programação que pode ser vista como uma evolução do Javascript. De fato, TypeScript
permite
fazer tudo que Javascript faz, mas inclui diversos outros recursos como Tipagem Forte,
Orientação
a Objetos, e, além de tudo isso, o código TypeScript ainda é compilado para Javascript no final.

A utilização TypeScript, ainda que padrão, não é obrigatória. Podemos usartambém
JavaScript ou
Dart. Apesar de ser bem diferente, com algum esforço, é possível conectar o
Angular com
aplicações Angular JS.

O código do framework Angular é composto de módulos (trata-se de um arquivo por
módulo), que
são combinados em bibliotecas, que - por sua vez - são agrupadas logicamente em
pacotes (ufa!).
Alguns pacotes são os @angular/core e ©angular/common. A aplicação Angular deve
carregar
esses pacotes antes do código em si. Beleza até aqui?

Um módulo Angular é um contêiner para um grupo de componentes, serviços e
diretivas
relacionados entre si. Podemos pensar num módulo como sendo uma biblioteca de
componentes
e serviços que implementa uma certa funcionalidade de negócio da aplicação, como um
módulo de
entregas de produto, ou de pagamento num site e-commerce.

Todos os elementos de uma aplicação mais simples podem estar localizados em um módulo
(o
módulo root, obrigatório), mas nada impede de haver mais módulos, o que é comum em
aplicações
mais complexas. Em termos de sintaxe, um módulo é uma classe anotada com um
decorador
NgModule. A peça chave de uma aplicação Angular são os componentes. Atenção aqui!

Cada componente consiste em duas partes: uma visão que define a interface do usuário
e a classe
que implementa a lógica por trás da visualização. Qualquer aplicação Angular é
representada por
uma hierarquia de componentes "empacotadas" em módulos. Uma aplicação deve
conter ao
menos um módulo com um componente, o componente root. O Angulartambém permite a escrita
em formato: ng-bind = "expression.".

O componente root não tem nada de especial, qualquer componente marcado com a
propriedade
"bootstrap" do módulo se torna um componente root. Galerinha, tudo muito legal, mas
que tal ver
0 código na prática? Pois é, para criar um componente é só declararmos uma classe
e anotar com
@Component (espero que todos saibam o que é uma anotação).

Cada anotação @Component deve definir as propriedades selector e template (ou
templateUrl),
que determinam como o componente deve ser descoberto e renderizado na
página,
respectivamente. Como nós já vimos na aula, cada componente deve definir uma visão,
que é
especificada pelo atributo template ou templateUrl:


/ 114

/


@Component({

selector: 'app-component',

template: '<hl>App Component</hl>' })
class AppComponent {}

Para aplicações web, o template contém código HTML. Podemos utilizar outras
linguagens de
marcação para diferentes tipos de renderização (para aplicações móveis, por exemplo).
Galerinha,
nós podemos definir estilos para os componentes com CSS. Podemos utilizar a propriedade
styles
para definir o estilo na forma inline e a propriedade styleUrls para referenciar
arquivos externos com
estilo CSS.

O decorador @Directive nos permite incluir comportamentos customizados aos elementos HTML.
Um exemplo é incluir autocomplete em elementos do tipo <input>. Cada
componente é
basicamente uma diretiva que tem uma visão associada, sendo que a última não possui
uma visão.
Pessoal, não caiu nada em prova, mas quando cair imagino que serão cobradas as
diferenças entre
o AngularJS e Angular.

Porfim, seguem algumas diretivas do Angular JS, que podem ajudar:

DIRETIVAS ANGULARJS | DESCRIÇÃO

NG-APP Declara um elemento como o elemento raiz da aplicação, ocasionando a mudança
do comportamento padrão da tag.

NG-BIND Muda o texto de um elemento HTML automaticamente, de acordo com o seu
resultado, vindo das regras de negócio.

NG-MODEL É similar ao ng-bind, mas permite ligação direta bidirecional (two-way data
binding) entre a view e o escopo do aplicativo.

NG-CLASS Permite atributos de classe serem carregados dinamicamente.

NG-CLICK Permite instanciar o evento de click, semelhante ao onclick.

NG-CONTROLLER Especifica um controller JavaScript para aquele HTML em questão.

NG-REPEAT Instancia um elemento por item de um array.

NG-SHOW E NG-HIDE Mostra ou esconde um elemento HTML de acordo com o resultado de uma
expressão booleana.

NG-SWITCH Instancia um template, em uma lista de escolhas, dependendo do valor obtido pela
expressão.

NG-VIEW A diretiva base para manipulação de rotas, resolvendo um JSON antes de
renderizar os modelos acionados por controladores especificados.

NG-IF Declaração básica de um 1 if que permite mostrar um elemento se a condição for
verdadeira.

NG-CSP Altera a política de segurança do conteúdo.


/ 114

/


SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I


QUESTõES CoMENTADAS - ANGULAR JS

í. (CESPE / STM - 2018) O serviço Angular JS $http é usado para fazer uma chamada
Ajax para o
servidor.

Comentários:

Pessoal, o serviço $http permite fazer chamadas Ajax para uma URL, usando os métodos
HTTP. É
exatamente essa sua função no framework

Gabarito: Correto

Item. 2. (CESPE/ BASA - 2018) É um exemplo de uma expressão Angular (Angular Expression) em
AngularJS:

a) <p>Candidato aprovado: candidato.nome }}</p>

b) <p>Candidato aprovado: [[ candidato.nome ]]</p>

c) <p>Candidato aprovado: <%- candidato.nome %></p>

d) <p>Candidato aprovado: <?= candidato.nome ?> </p>

e) <p>Candidato aprovado: <js:angular value="candidato.nome"/x/p>

Comentários:

Pessoal, lembre-se dos "bigodes" - {{}}. É uma das formas de fazer a análise de
expressões em
AngularJS.

Gabarito: Letra A

Item. 3. (CESPE / STM - 2018) Após ser executada, a expressão Angular JS

<div ng-app="">

<p>Resultado: {(5 + 12 )}</p>

</div>

produzirá, como resultado, Resultado: 17

Comentários:

Mais uma vez, lembre-se dos "bigodes" - {{}}. Na questão, ao invés de colocar chaves
duplas, o
examinador colocou chaves e parêntesis {()}, e isso não é nada na arquitetura
AngularJS. Portanto,
item errado


/ 114

/


Gabarito: Errado

Item. 4. (FCC / DPE-RS - 2017) AngularJS é umframework JavaScript, também referenciado como uma
biblioteca escrita em JavaScript. Esse framework permite o uso de
a) expressões escritas dentro de uma diretiva no formato: ng-bind = "expression".

b) expressões escritas dentro de colchetes duplos, no formato [[expression.]].

c) filtros que devem ser adicionados às expressões por meio do caractere cerquilha (#).

d) XML com diretivas xsd, como xsd-app, xsd-model e xsd-bind.

e) expressões que suportam condicionais, loops e exceções, mas não suportam filtros.

Comentários:

Pessoal, conforme vimos no finalzainho da nossa aula, o Angular também permite a
escrita em
formato: ng-bind = "expression."

Gabarito: Letra A

Item. 5. (CESNGRARIO / BANCO DA AMAZÔNIA - 2018) É um exemplo de uma expressão Angular
(Angular Expression) em AngularJS:

a) <p>Candidato aprovado: {{candidato.nome }}</p>.

b) <p>Candidato aprovado: [[ candidato.nome ]]</p>.

c) <p>Candidato aprovado: <%= candidato.nome %></p>.

d) <p>Candidato aprovado: <?= candidato.nome ?> </p>.

e( <p>Candidato aprovado: <js:angular value="candidato. nome"/x/p>.

Comentários:

Conforme a sintaxe do Angular, o correto seria:

<p>

Candidato aprovado: {{candidato.nome }]

</p>.

Gabarito: Letra A

Item. 6. (FCC / TRT2 - 2018) Considere a página web abaixo, que utiliza o Angular JS versão 1.6.9.


< IDOCTYPE htral>

<html>

<head>

TRT

<script arc="angular-mm.js">

</script>

</head>

<body>

«div ng-app="" ng-init="a=5;b=4">

<p>Total: <spán ng-bind=*a * b**></fipan></p>

< /div>

< /body >

</html>

O resultado do cálculo envolvendo as variáveis a e b é mostrado pela instrução
<p>Total:<span ng-
bind="a * b"x/spanx/p> . Outra forma de realizar o mesmo procedimento é usando a instrução
a) <p>Total: <span ng-calc="a * b"x/spanx/p>.

b) <p>Total: {{a * b }}</p>

c) <p>Total: javascript.calc(a * b)</p>

d) <p>Total: <script>Math.calc(a * b)</scriptx/p>

e) <p>Total: <script ng-math="a * b"x/scriptx/p>

Comentários:

Pessoal, lembrem-se sempre dos bigodes que vimos: - {{Logo, <p>Total: {{a * b }}</p>
é nossa
alternativa correta. Quando aparecer {{text}} já pode ter certeza que está falando em
exibir dados
no Angular.

Gabarito: Letra B

Item. 7. (COPERV / UFSC - 2018) Considere a página web abaixo que utiliza Angular.


«IDOCTYPE html>

<head>

<acript src=* angular,min.j a * ></acript»

</head>

<body>

<div ng-app="*>

< forno

<p>Nome: <input type="text" ng-model="nome"></p>
c/fom>

I

</div>

</body>

Considere os comandos:

I. <p ng-bind="nome"x/p>

II. <p>{{nome}}</p>

III. <p ng-print="nome"x/p>

IV. <p>{$nome}</p>

Para que o que for digitado no campo nome seja exibido simultaneamente em um
parágrafo, na
lacuna I podem ser utilizados os comandos que constam APENAS nos itens
a) III e IV.

b) I e III.

c) II e IV.

d) I e IV.

e) I e II.

Comentários:

Galera, o comando ng-bind diz ao Angular para substituir o conteúdo de um elemento
HTML com
o valor de uma dada variável, ou expressão. Logo, < p>{{nome}}< /p> já sabemos que é
Angular, o
que temos agora é uma nova variável chamada "nome", que está ligada ao {{nome}}. No
mais, o
item III está errado, pois não existe ng-print e o item IV está errado pois $ trata-se de PHP.

Gabarito: Letra E

Item. 8. (IBFC /TJ-PE - 2017) Abaixo são apresentadas algumas das principais diretivas no AngularJS:

(1) ng-model


(2) ng-app

(3) ng-loop

(4) ng-controller

Selecione a alternativa tecnicamente correta:

a) da relação apresentada somente são aplicadas o i, 2 e 3

b) da relação apresentada somente são aplicadas o 1, 2 e 4

c) da relação apresentada somente são aplicadas o 2, 3 e 4

d) da relação apresentada somente são aplicadas o 1, 3 e 4

e) da relação apresentada todas diretivas podem ser aplicadas

Comentários:

As principais diretrizes do AngularJS:

DIRETIVAS ANGULARJS | DESCRIÇÃO

NG-APP Declara um elemento como o elemento raiz da aplicação, ocasionando a mudança
do comportamento padrão da tag.

NG-BIND Muda o texto de um elemento HTML automaticamente, de acordo com o seu
resultado, vindo das regras de negócio.

NG-MODEL É similar ao ng-bind, mas permite ligação direta bidirecional (two-way data
binding) entre a view e o escopo do aplicativo.

NG-CLASS Permite atributos de classe serem carregados dinamicamente.

NG-CLICK Permite instanciar o evento de click, semelhante ao onclick.

NG-CONTROLLER Especifica um controller JavaScript para aquele HTML em questão.

NG-REPEAT Instancia um elemento por item de um array.

NG-SHOW E NG-HIDE Mostra ou esconde um elemento HTML de acordo com o resultado de uma
expressão booleana.

NG-SWITCH Instancia umtemplate, em uma lista de escolhas, dependendo do valor obtido pela
expressão.

NG-VIEW A diretiva base para manipulação de rotas, resolvendo um JSON antes de
renderizar os modelos acionados por controladores especificados.

NG-IF Declaração básica de um 'if que permite mostrar um elemento se a condição for
verdadeira.

NG-CSP Altera a política de segurança do conteúdo.

Gabarito: Letra B

x


/ 114

/


Item. 9. (CESPE / SEDF - 2017) AngularJS, Ajax, JQuery, Less e PHP são tecnologias para
desenvolvimento webfront-end.

Comentários:

AngularJS - tecnologias para desenvolvimento webfront-end
Ajax, - tecnologias para desenvolvimento webfront-end
JQuery - tecnologias para desenvolvimento webfront-end
Less - tecnologias para desenvolvimento webfront-end

PHP - tecnologias para desenvolvimento web back-end ou server-side

Gabarito: Errado
io.(FGV / IBGE - 2016) Com relação ao AngularJS, analise as afirmativas a seguir:

I. É capaz de estender o HTML graças às diretivas do tipo ng-init e ng-app.

II. Suas expressões podem ser escritas dentro de chaves duplas.

III. Não oferece validação de forms do lado do cliente.

Está correto somente o que se afirma em:
a) l
b) II

c) III

d) I e II

e) I e III

Comentários:

Conforme verificamos, em AngularJS as expepressões podem ser escritas dentro de chaves
duplas
e podemos estender o HTML graças às diretivas do tipo ng-init e ng-app. Vale destacar
que oferece
sim validação de forms do lado do cliente.

Gabarito: Letra D

Item. 11. (FCC / TRT11 - 2017) Considere o fragmento de código HTML abaixo.

<body> <div> <label>processo N°:</label> <input
types="text" ng-
model="processo"> <p>o número do processo é {{processo}}. </p> </div> </body>

Este fragmento evidencia o uso de:

a) QueryJS.


/ 114

/


b) Facelets.

c) AngularJS.

d) Portlets.

e) PrimeFaces.

Comentários:

Simples, não é? Estamos estudando aqui o AngularJS, e o fragmento a seguir é do
AngularJS:

<body> <div> <label>processo N°:</label>
<input types="text" ng-
model="processo"> <p>o número do processo é {{processo}} . </p> </div> </body>

Lembre-se do {{ }}! Se existir, 99% de chance de ser Angular.

Gabarito: Letra C

12.(VUNESP/ FUNDUNESP - 2016) No AngularJS, a diretiva ng-model é utilizada para:

a) inicializar dados do modelo.

b) ativar o AngularJS na página HTML.

c) vincular o conteúdo de um controlador HTML a um dado do modelo.

d) indicar o nome do controlador que determinará o comportamento de um elemento HTML.

e) indicar que os dados contidos em um elemento HTML não devem ser obtidos a partir
do
escopo raiz.

Comentários:

DIRETIVAS ANGULARJS | DESCRIÇÃO

NG-APP Declara um elemento como o elemento raiz da aplicação, ocasionando a mudança
do comportamento padrão da tag.

NG-RIND Muda o texto de um elemento HTML automaticamente, de acordo com o seu
resultado, vindo das regras de negócio.

NG-MODEL É similar ao ng-bind, mas permite ligação direta bidirecional (two-way data
binding) entre a view e o escopo do aplicativo.

NG-CLASS Permite atributos de classe serem carregados dinamicamente.

NG-CLICK Permite instanciar o evento de click, semelhante ao onclick.

NG-CDNTROLLER Especifica um controller JavaScript para aquele HTML em questão.

NG-REPEAT Instancia um elemento por item de um array.

NG-SHOW E NG-HIDE Mostra ou esconde um elemento HTML de acordo com o resultado de uma
expressão booleana.

x


/ 114

/


Instancia umtemplate, em uma lista de escolhas, dependendo do valor obtido
expressão.

A diretiva base para manipulação de rotas, resolvendo um JSON antes
renderizar os modelos acionados por controladores especificados.

Declaração básica de um 'if que permite mostrar um elemento se a condição
verdadeira.

Altera a política de segurança do conteúdo.

Gabarito: Letra C

Item. 13. (CESPE / FUB - 2018) Com relação ao uso dos frameworks AngularJS e Hibernate, julgue o item
a seguir.

Eventos do AngularJS podem ser usados para associar diferentes ações a diferentes
elementos
HTML; por exemplo, um evento AngularJS pode ser usado para associar uma ação
relacionada
à seleção de um elemento HTML por meio do uso de um mouse.

Comentários:

Perfeito! Eventos do AngularJS podem ser usados para associar diferentes ações
a diferentes
elementos HTML; por exemplo, um evento AngularJS pode ser usado para associar
uma ação
relacionada à seleção de um elemento HTML por meio do uso de um mouse.

Gabarito: Correto
i4-(FGV / IBGE - 2016) Mantido pelo Google, o AngularJS é um framework popular usado para:

a) ampliar as funções do CSS, estendendo a biblioteca da linguagem com novos comandos
e
oferecendo recursos dinâmicos para exibição de dados;

b) substituir o JavaScript na programação de recursos interativos através da oferta de
uma
biblioteca de comandos multimidiáticos;

c) declarar visualizações dinâmicas em aplicações web, estendendo as bibliotecas de
linguagens
dinâmicas como PHP e ASP;

d) substituir o HTML como linguagem de marcação para hierarquização mais
eficiente do
conteúdo;

e) declarar visualizações dinâmicas em aplicações web, estendendo atributos do
HTML com
diretivas e vinculando dados ao HTML através de expressões.

Comentários:


/ 114

/


AngularJS visa declarar visualizações dinâmicas em aplicações web, estendendo atributos
do HTML
com diretivas e vinculando dados ao HTML através de expressões.

Gabarito: Letra E

Item. 15. (CESPE / STJ - 2015) AngularJS segue um modelo MVC. Qual a diretiva correta em
AngularJS
para ligar um elemento de entrada de dados da visão, como um campo input dotipo
texto, a um
elemento do modelo, como uma variável do tipo string?

a) ngView
b) ngValue
c) ngBind
d) ngModel
e) ngLink

Comentários:

Só lembrar:

DIRETIVAS ANGULARJS | DESCRIÇÃO

NG-APP Declara um elemento como 0 elemento raiz da aplicação, ocasionando a mudança
do comportamento padrão da tag.

NG-BIND Muda 0 texto de um elemento HTML automaticamente, de acordo com 0 seu
resultado, vindo das regras de negócio.

NG-MODEL É similar ao ng-bind, mas permite ligação direta bidirecional (two-way data
binding) entre a view e 0 escopo do aplicativo.

NG-CLASS Permite atributos de classe serem carregados dinamicamente.

NG-CLICK Permite instanciar 0 evento de click, semelhante ao onclick.

NG-CONTROLLER Especifica um controller JavaScript para aquele HTML em questão.

NG-REPEAT Instancia um elemento por item de um array.

NG-SHOW E NG-HIDE Mostra ou esconde um elemento HTML de acordo com 0 resultado de uma
expressão booleana.

NG-SWITCH Instancia umtemplate, em uma lista de escolhas, dependendo do valor obtido pela
expressão.

NG-VIEW A diretiva base para manipulação de rotas, resolvendo um JSON antes de
renderizar os modelos acionados por controladores especificados.

NG-IF Declaração básica de um 'if que permite mostrar um elemento se a condição for
verdadeira.

NG-CSP Altera a política de segurança do conteúdo.

x


/ 114

/


Gabarito: Letra D

i6.(CESPE / STJ - 2015) O atributo ngBind informa ao AngularJS para atualizar o conteúdo do
texto, quando o valor da expressão for alterado.

Comentários:

Perfeito! Galera, é inviável que vocês decorem cada função do AngularJS (são dezenas!).
Vamos
comentá-las apenas se houver exercícios. Bem, o ngBind diz para o AngularJS substituir
o conteúdo
textual de um elemento HTML com o valor da expressão dada, e manter o conteúdo
atualizado
sempre que o valor da expressão mudar.

Gabarito: Correto


/ 114

/


LISTA DE QUESTõES - ANGULARJS

í. (CESPE / STM - 2018) O serviço Angular JS $http é usado para fazer uma chamada Ajax para o
servidor.

Item. 2. (CESPE/ BASA - 2018) É um exemplo de uma expressão Angular (Angular Expression) em
AngularJS:

a) <p>Candidato aprovado: [{candidato.nome ]}</p>

b) <p>Candidato aprovado: [[ candidato.nome ]]</p>

c) <p>Candidato aprovado: <%= candidato.nome %></p>

d) <p>Candidato aprovado: <?= candidato.nome ?> </p>

e) <p>Candidato aprovado: <js:angular value="candidato.nome"/x/p>

Item. 3. (CESPE / STM - 2018) Após ser executada, a expressão Angular JS

<div ng-app="">

<p>Resultado: {(5 + 12 )}</p>

</div>

produzirá, como resultado, Resultado: 17

Item. 4. (FCC / DPE-RS - 2017) AngularJS é umframework JavaScript, também referenciado como uma
biblioteca escrita em JavaScript. Esse framework permite o uso de
a) expressões escritas dentro de uma diretiva no formato: ng-bind - "expression".

b) expressões escritas dentro de colchetes duplos, no formato [[expression.]].

c) filtros que devem ser adicionados às expressões por meio do caractere cerquilha (#).

d) XML com diretivas xsd, como xsd-app, xsd-model e xsd-bind.

e) expressões que suportam condicionais, loops e exceções, mas não suportam filtros.

Item. 5. (CESNGRARIO / BANCO DA AMAZÔNIA - 2018) É um exemplo de uma expressão Angular
(Angular Expression) em AngularJS:

a) <p>Candidato aprovado: [{candidato.nome ]}</p>.

b) <p>Candidato aprovado: [[ candidato.nome ]]</p>.

c) <p>Candidato aprovado: <%- candidato.nome %></p>.

d) <p>Candidato aprovado: <?= candidato.nome ?> </p>.

e) <p>Candidato aprovado: <js:angular value="candidato. nome"/x/p>.

Item. 6. (FCC / TRT2 - 2018) Considere a página web abaixo, que utiliza o Angular JS versão 1.6.9.


< IDOCTYPE htral>

<html>

<head>

TRT

<script arc="angular-mm.js">

</script>

</head>

<body>

«div ng-app="" ng-init="a=5;b=4">

<p>Total: <spán ng-bind=*a * b*></fipan></p>

< /div>

< /body >

</html>

O resultado do cálculo envolvendo as variáveis a e b é mostrado pela instrução
<p>Total:<span ng-
bind="a * b"x/spanx/p> . Outra forma de realizar o mesmo procedimento é usando a instrução
a) <p>Total: <span ng-calc="a * b"x/spanx/p>.

b) <p>Total: {{a * b }}</p>

c) <p>Total: javascript.calc(a * b)</p>

d) <p>Total: <script>Math.calc(a * b)</scriptx/p>

e) <p>Total: <script ng-math="a * b"x/scriptx/p>

Item. 7. (COPERV/ UFSC 2018) Considere a página web abaixo que utiliza Angular.

<!DOCTYPE html>

<ht!TLl>

<head>

<âcript src= '*angular,min. J s * ></script>

</head>

<body>

<div ng-app="">

< fortn>

<p>Nome: <input type='text" ng*módel="nome"></p>

I

</dív>

</body>

Considere os comandos:

I. <p ng-bind="nome,,x/p>

II. <p>{{nomeH</p>


III. <p ng-print="nome"x/p>

IV. <p>{$nome}</p>

Para que o que for digitado no campo nome seja exibido simultaneamente em um
parágrafo, na
lacuna I podem ser utilizados os comandos que constam APENAS nos itens
a) III e IV.

b) I e III.

c) II e IV.

d) Ie IV.

e) I e II.

Item. 8. (IBFC /TJ-PE - 2017) Abaixo são apresentadas algumas das principais diretivas no AngularJS:

(1) ng-model

(2) ng-app

(3) ng-loop

(4) ng-controller

Selecione a alternativa tecnicamente correta:

a) da relação apresentada somente são aplicadas o 1, 2 e 3

b) da relação apresentada somente são aplicadas o 1, 2 e 4

c) da relação apresentada somente são aplicadas o 2, 3 e 4

d) da relação apresentada somente são aplicadas o 1, 3 e 4

e) da relação apresentada todas diretivas podem ser aplicadas

Item. 9. (CESPE / SEDF - 2017) AngularJS, Ajax, JQuery, Less e PHP são
tecnologias para
desenvolvimento webfront-end.

Item. 10. (FGV / IBGE - 2016) Com relação ao AngularJS, analise as afirmativas a seguir:

I. É capaz de estender o HTML graças às diretivas do tipo ng-init e ng-app.

II. Suas expressões podem ser escritas dentro de chaves duplas.

III. Não oferece validação de forms do lado do cliente.

Está correto somente o que se afirma em:
a) l
b) II

c) III

d) I e II

e) I e III


Item. 11. (FCC / TRT ii - 2017) Considere o fragmento de código HTML abaixo.

<body> <div> <label>processo N°:</label> <input
types="text" ng-
model="processo"> <p>o número do processo é {{processo}}. </p> </div> </body>

Este fragmento evidencia o uso de:

a) QueryJS.

b) Facelets.

c) AngularJS.

d) Portlets.

e) PrimeFaces.

Item. 12. (VUNESP/ FUNDUNESP - 2016) No AngularJS, a diretiva ng-model é utilizada para:

a) inicializar dados do modelo.

b) ativar o AngularJS na página HTML.

c) vincular o conteúdo de um controlador HTML a um dado do modelo.

d) indicar o nome do controlador que determinará o comportamento de um elemento HTML.

e) indicar que os dados contidos em um elemento HTML não devem ser obtidos a partir
do
escopo raiz.

Item. 13. (CESPE / FUB - 2018) Com relação ao uso dos frameworks AngularJS e Hibernate, julgue o item
a seguir.

Eventos do AngularJS podem ser usados para associar diferentes ações a diferentes
elementos
HTML; por exemplo, um evento AngularJS pode ser usado para associar uma ação
relacionada
à seleção de um elemento HTML por meio do uso de um mouse.

Item. 14. (FGV / IBGE - 2016) Mantido pelo Google, o AngularJS é um framework popular usado para:

a) ampliar as funções do CSS, estendendo a biblioteca da linguagem com novos comandos
e
oferecendo recursos dinâmicos para exibição de dados;

b) substituir o JavaScript na programação de recursos interativos através da oferta de
uma
biblioteca de comandos multimidiáticos;

c) declarar visualizações dinâmicas em aplicações web, estendendo as bibliotecas de
linguagens
dinâmicas como PHP e ASP;

d) substituir o HTML como linguagem de marcação para hierarquização mais
eficiente do
conteúdo;


e) declarar visualizações dinâmicas em aplicações web, estendendo atributos do
HTML com
diretivas e vinculando dados ao HTML através de expressões.

Item. 15. (CESPE / STJ - 2015) AngularJS segue um modelo MVC. Qual a diretiva correta em
AngularJS
para ligar um elemento de entrada de dados da visão, como um campo input do tipo
texto, a um
elemento do modelo, como uma variável do tipo string?

a) ngView
b) ngValue
c) ngBind
d) ngModel
e) ngLink

Item. 16. (CESPE / STJ - 2015) O atributo ngBind informa ao AngularJS para atualizar o
conteúdo do
texto, quando o valor da expressão for alterado.


/ 114

/


GABARITo - ANGULARJS

Item. 1. CORRETO 7. LETRA E
Item. 13. CORRETO

Item. 2. LETRA A 8. LETRA B
Item. 14. LETRA E

Item. 3. ERRADO 9. ERRADO
Item. 15. LETRA D

Item. 4. LETRA A io. LETRA D
16.CORRETO

Item. 5. LETRA A li. LETRA C

Item. 6. LETRA B 12. LETRA C


NoDEJS

Coé, rapaziada! Vamos falar um pouquinho sobre NodeJS! Galera, um matemático chamado
Ryan
Dahl terminou seu doutorado e começou a trabalhar com programação desenvolvendo
páginas
web. Certo dia, ele foi fazer o upload de umas fotos no Flickr e observou que,
enquanto as fotos,
subiam uma barra de progresso mostrava gradativamente o progresso do upload.

Multi Threaded Server


Request

Request _

Request $

I —H

—>

Thread Pool

O

©o

©©o

>

o Thread Processing Thread Waiting

Para quem quiser conhecê-lo: https://www.youtube.com/watch?v=SAc0vQCC6UQ


Ele imaginou como aquilo era implementado e descobriu que, como o navegador não sabia,
ele
frequentemente perguntava ao servidor web: "Quanto de upload já foi
realizado?"; e o servidor
respondia: "5%", "20%", "50%", etc. E aí, ele percebeu que as tecnologias
existentes não
trabalhavam muito bem com l/O (Entrada/Saída) de dados. Beleza?

Como funcionava? Os servidores (imagem anterior) tinham várias threads esperando
requisições
do cliente; ao receber, ele fazia seu processamento e retornava o que o cliente havia
requisitado;
porém, quando o fluxo de requisições era baixo, várias threads ficavam ociosas, i.e.,
havia vários
recursos alocados (como memória, etc) e que não eram utilizados para nada quando não
havia
requisições.

No entanto, nem sempre é necessário todo o recurso computacional aplicado para executar
uma
nova thread. Pessoal, voltando ao desenho, nós temos uma requisição que vira uma
thread; outra
requisição que vira outra thread; a terceira requisição precisa realizar várias ações
independentes
entre si, mas como elas se tornam uma thread, a entrada/saída de dados fica
bloqueada (Blocking
IO).

Isso por vezes não é interessante, porque não permite o processamento assíncrono da
requisição,
e é esse o grande problema que o Ryan Dhal queria resolver.

Node.js Server

O Thread Processing Thread Waiting

Qual foi a solução dele? Ele criou um Event Loop que roda em uma única thread - e
é por isso que
dizem que o NodeJS é single-threaded. Isso quer dizer que ele não utiliza threads
internamente?
Não, ele utiliza threads internamente. O Servidor NodeJS recebe requisições que entram
em uma
fila. A primeira requisição entra no Event Loop e o servidor delega a requisição para
alguma thread
assíncrona.


/ 114

/


Dessa forma, a entrada/saída de dados será não-bloqueante, ou seja, se uma
atividade não
depender de outra, não há por que ela ser bloqueada. Seguindo... muita gente se
pergunta se o
NodeJS é uma linguagem de programação. Nope, nada disso... NodeJS é um
ambiente de
execução e um conjunto de bibliotecas para rodar JavaScript - é simplesmente uma plataforma.

Além disso, como já foi dito acima, ele é server-side, logo não precisa
rodar no navegador,
portanto podemos dizer que ele é independente de browser. O que mais? Ele é
multiplataforma
(Linux, Windows, Mac, etc) e open-source. O NodeJS é excelente para aplicações
que utilizam
comunicação em tempo real, serviços de rede customizados, Web Services JSON, interfaces
web
focadas no cliente, etc.

Porém, ele é ruim para aplicações que tenham processamento intenso, como codificação de
vídeo,
etc. Além disso, o NodeJS pode gerar conteúdo dinâmico para páginas web; pode criar,
abrir, ler,
escrever, deletar e fechar arquivos no servidor; pode coletar dados de formulários;
pode adicionar,
deletar e modificar dados em uma base de dados, entre outros.

Agora uma coisa importante! Galera, onde roda o JavaScript? Todo mundo tem
que saber
responder essa: roda no cliente! No entanto, o Ryan Dahl pensou: ora, por
que não rodar o
JavaScript no servidor? Pois é, o NodeJS roda na Engine V8, que não precisa estar no
navegador,
ela apenas executa o Javascript. Galera, é possível escrever livros sobre isso, mas
nunca caiu em
prova, então vamos parar por aqui...


/ 114

/


Conceitos Básicos

WEBPACkJS

INCIDÊNCIA EM PROVA: MÉDIA

OWebpackJS ou Webpack nada mais é que um empacotador para Javascript. Como
assim?
Basicamente, o webpack realiza o empacotamento de módulo estático processando as
aplicações
em pacotes, que são ativos estáticos que visam servir de conteúdo. Vamos dar uma
olhada na figura
abaixo para entender melhor:

T *js


.hbs

T .sass

.cjs

*png

*jpg

*js .css

*jpg *png


.sass

.sass

STATICASSETS

MODULES WITH DEPENDENCIES

O que estamos vendo acima é o agrupamento (empacotamento) de módulos
estáticos para
aplicações javascript. O que o webpack faz é processar aplicações, empacotar e a
partir disso, gerar
um gráfico que mapeia cada módulo e as dependências de um ou mais pacotes.

Dito isso, temos alguns conceitos principais a serem explorados. Dentre eles o ENTRY,
o ENTRY
nada mais é que o ponto de entrada que vai indicar qual módulo do webpack deverá
ser utilizado
para começar a construção do gráfico de dependências.

Quanto um ponto de entrada é definido, o webpack encontra as dependências e
realiza a
importação. Por padrão o ponto de entrada é o arquivo ,/src/index.js, porém é possível
definir outro
arquivo ou até multiplus arquivos como ponto de entrada no arquivo
de configuração
webpack.config.js.

Outro conceito importante é o OUTPUT, o OUTPUT diz respeito a propriedade que define
o nome
e o local do pacote gerado pelo webpack. O diretório em questão é o ,/dist e o
arquivo é o

.dist/main.js.

Os LOADERS são módulos que são instalados de forma separada e que possibilitam que o
webpack
realize a conversão desdes arquivos em módulos com gráficos de dependência. Por fim
temos o
MODE que realizam a execução do webpack em produção.


QUESTõES CoMENTADAS - WEBPACkOS

í. (QUESTÃO INÉDITA) Webpack é um empacotador javascript que realiza a conversão de
aplicações em módulos com gráficos.

Comentários:

Perfeito! Basicamente, o webpack realiza o empacotamento de módulo estático
processando as
aplicações em pacotes, que são ativos estáticos que visam servir de conteúdo

Gabarito: Correto

Item. 2. (QUESTÃO INÉDITA) O webpackjs realiza o empacotamento de módulo dinâmico convertendo
as aplicações em pacotes.

Comentários:

O webpackjs realiza o empacotamento de módulo estático e não dinâmico,
processando as
aplicações em pacotes.

Gabarito: Errado

Item. 3. (QUESTÃO INÉDITA) O agrupamento ou empacotamento de módulos
estáticos para
aplicações javascript é a principal finalidade do webpackjs.

Comentários:

Perfeito! O agrupamento ou empacotamento de módulos estáticos para aplicações javascript
é a
principal finalidade do webpackjs.

Gabarito: Correto

Item. 4. (QUESTÃO INÉDITA) O webpack realiza o processamento das aplicações, empacotamento e a
partir disso, gerar um gráfico que mapeia cada módulo e as dependências de um ou mais pacotes

Comentários:

Perfeito! O webpack realiza o processamento das aplicações, empacotamento e a partir
disso, gerar
um gráfico que mapeia cada módulo e as dependências de um ou mais pacotes

Gabarito: Correto


Item. 5. (QUESTÃO INÉDITA) O ENTRY é uma das funcionalidades do webpack e é responsável
por
indicar qual a aplicação do webpack deverá ser utilizado para começar a construção do
gráfico
de dependências.

Comentários:

O ENTRY é uma das funcionalidades do webpack e é responsável por indicar qual o
módulo e não a
aplicação do webpack deverá ser utilizado para começar a construção do gráfico de dependências.

Gabarito: Errado

Item. 6. (QUESTÃO INÉDITA) Através do ENTRY quanto um ponto de entrada é definido, o
webpack
encontra as dependências e realiza a importação.

Comentários:

Perfeito! Através do ENTRY quanto um ponto de entrada é definido, o webpack
encontra as
dependências e realiza a importação.

Gabarito: Correto

Item. 7. (QUESTÃO INÉDITA) Por padrão no webpack o ponto de entrada é o arquivo
./src/index.config,
porém é possível definir outro arquivo ou até multiplus arquivos como ponto de entrada
no
arquivo de configuração webpack.config.js.

Comentários:

Pessoal, o ponto de entrada por padrão é o ./src/index.js e não ./src/index.config.
Logo, o correto
seria: Por padrão no webpack o ponto de entrada é o arquivo ./src/index.js, porém é
possível definir
outro arquivo ou até multiplus arquivos como ponto de entrada no arquivo de
configuração
webpack.config.js.

Gabarito: Errado

Item. 8. (QUESTÃO INÉDITA) O OUTPUT no webpack, diz respeito a propriedade que define o
nome e
o local do pacote gerado pelo webpack.

Comentários:

Perfeito! O OUTPUT no webpack, diz respeito a propriedade que define o nome e o
local do pacote
gerado pelo webpack.

Gabarito: Correto


/ 114

/


Item. 9. (QUESTÃO INÉDITA) Os LOADERS são módulos que são instalados de forma separada no
webpack e que possibilitam que o webpack realize a conversão desdes arquivos em módulos
com gráficos de dependência.

Comentários:

Perfeito! Os LOADERS são módulos que são instalados de forma separada no webpack e que
possibilitam que o webpack realize a conversão desdes arquivos em módulos com
gráficos de
dependência.

Gabarito: Correto

Item. 10. (QUESTÃO INÉDITA) No webpack, o MODE realiza a execução em desenvolvimento e não
em
produção.

Comentários:

Ao contrário, o MODE no webpack realiza a execução em produção e não em desenvolvimento.

Gabarito: Errado


/ 114

/


LISTA DE QUESTõES - WEBPACkJS

í. (QUESTÃO INÉDITA) Webpack é um empacotador javascript que realiza a
conversão de
aplicações em módulos com gráficos.

Item. 2. (QUESTÃO INÉDITA) O webpackjs realiza o empacotamento de módulo dinâmico convertendo
as aplicações em pacotes.

Item. 3. (QUESTÃO INÉDITA) O agrupamento ou empacotamento de módulos
estáticos para
aplicações javascript é a principal finalidade do webpackjs.

Item. 4. (QUESTÃO INÉDITA) O webpack realiza o processamento das aplicações, empacotamento e
a
partir disso, gerar um gráfico que mapeia cada módulo e as dependências de um ou mais pacotes

Item. 5. (QUESTÃO INÉDITA) O ENTRY é uma das funcionalidades do webpack e é responsável
por
indicar qual a aplicação do webpack deverá ser utilizado para começar a construção do
gráfico
de dependências.

Item. 6. (QUESTÃO INÉDITA) Através do ENTRY quanto um ponto de entrada é definido, o
webpack
encontra as dependências e realiza a importação.

Item. 7. (QUESTÃO INÉDITA) Por padrão no webpack o ponto de entrada é o arquivo
./src/index.config,
porém é possível definir outro arquivo ou até multiplus arquivos como ponto de entrada
no
arquivo de configuração webpack.config.js.

Item. 8. (QUESTÃO INÉDITA) O OUTPUT no webpack, diz respeito a propriedade que define o
nome e
o local do pacote gerado pelo webpack.

Item. 9. (QUESTÃO INÉDITA) Os LOADERS são módulos que são instalados de forma separada no
webpack e que possibilitam que o webpack realize a conversão desdes arquivos em módulos
com gráficos de dependência.

Item. 10. (QUESTÃO INÉDITA) No webpack, o MODE realiza a execução em desenvolvimento e não
em
produção.


GABARITo - WEBPACkJS

Item. 1. CORRETO

Item. 2. ERRADO

Item. 3. CORRETO

Item. 4. CORRETO

Item. 5. ERRADO

Item. 6. CORRETO

Item. 7. ERRADO

Item. 8. CORRETO

Item. 9. CORRETO

Item. 10. ERRADO


/ 114

/


Conceitos Básicos

WEBSoCkET

INCIDÊNCIA EM PROVA: MÉDIA

Fala, galera! Bom, todo mundo sabe que o alicerce, o sustentáculo, o baluarte da web
se encontra
no paradigma de requisição/resposta do Protocolo HTTP. Como assim? Bem, um cliente
carrega
uma página web. Enquanto ele não fizer qualquer outra ação, nada acontece! O AJAX
melhorou um
pouco essa interação cliente/servidor ao permitirfazer requisições assíncronas.

Dito isso, podemos definir que o WebSockets é uma tecnologia avançada que torna
possível abrir
uma sessão de comunicação interativa entre o navegador do usuário e um servidor. Com
esta API,
você pode enviar mensagens para um servidor e receber respostas orientadas a eventos
sem ter
que consultar o servidor para obter uma resposta.

Ainda assim, toda comunicação é direcionada pelo cliente, exigindo uma interação do
usuário ou
sondagem periódica para carregar novos dados do servidor. A especificação WebSocket
define uma
API para estabelecer conexões entre um navegador e um servidor. Em outras palavras,
há uma
conexão persistente entre cliente/servidor e as duas partes podem enviar dados
a qualquer
momento.


/ 114

/


Galera, demorou muito até essa tecnologia chegar! Navegadores são excelentes em
fazer
requisições ao servidor, mas o coitado do servidor não era capaz de enviar dados para
o navegador
arbitrariamente. Claro, programadores já fizeram muita gambiarra por aí com
Reverse AJAX,
Comet, Polling, entre outros. No entanto, o HTML5 já trouxe essa novidade nativamente.

WebSockets permitem abrir uma conexão com o servidor remoto e trafegar dados
arbitrariamente
do servidor para o cliente e vice-versa. É possível fazer muita coisa com essa
tecnologia: um chat
em tempo real; um mecanismo de sincronização; e até streaming de dados binários. Em
termos
mais técnicos, trata-se de uma comunicação bidirecional full-duplex sobre um único Soquete TCP.

Vamos analisar dois cenários! Imaginem que eu estou ministrando uma aula ao vivo para
vocês por
meio da página do Estratégia Concursos e resolvendo questões no aplicativo de perguntas
mobile.
No primeiro cenário, cada vez que eu responder uma pergunta, vocês teriam que
responder no
aplicativo de vocês imediatamente para que nós fiquemos perfeitamente sincronizados.

Em um segundo cenário, poderíamos utilizar WebSockets para sincronizar o meu
aplicativo de
perguntas com o aplicativo de vocês de forma que, a cada vez que eu responder uma
pergunta,
passe imediatamente para a próxima pergunta tanto no meu aplicativo quanto no
aplicativo de
vocês. Em outras palavras, meu aplicativo envia para o servidor a pergunta atual e
distribuía para
vocês em tempo real.

Vocês percebem que houve uma resposta para 0 dispositivo de vocês mesmo sem ter
havido uma
requisição? Pois é, WebSocket. Use o WebSocket sempre que precisar de uma conexão
quase em
tempo real de baixa latência entre o cliente e o servidor. Tenha em mente que isso
pode envolver a
reformulação do modo como você cria os aplicativos de servidor com um novo foco em
tecnologias
como filas de eventos.

Para utilizar o WebSocket, você utiliza uma URL de conexão com protocolo ws:. Veja um
exemplo
abaixo:

1: // estabelece o WebSocket

2: letws = new WebSocket("ws://meuservico.com.br/alguma");

3:

4: // comunicação servidor -> cliente
5: ws.onmessage = function() {

6: //faça uma coisa genial

7:1

8:

9: // comunicação cliente -> servidor
10: ws.send("Enviando algo...")

A linha 2 abre um WebSocket com o serviço disponível em "ws://meuservico.com.br/alguma".
Essa
conexão usa a própria conexão HTTP da página, e mantém o canal aberto enquanto o socket não


/ 114

/


forfechado. As linhas 5-7 registram uma função para ser chamada sempre que uma
mensagem for
enviada do servidor. Por último, na linha 10, enviamos uma mensagem textual
para o socket:
"Enviando algo...". Importante destacar que para fins de prova que o handshake
WebSocket usa o
cabeçalho HTTP Upgrade para mudar do protocolo HTTP para o protocolo WebSocket, com uma
requisição de Upgrade, guarde isso. Lembre-se também o protocolo WebSocket usa a porta
80 para
conexões WebSocket regulares e a porta 443 para conexões WebSocket tuneladas
sobre TLS
(Jransport LayerSecurity).

As principais funcionalidades do objeto WebSocket são:

* new WebSocket(url) Abre o WebSocket

* ws.closeO Fecha o WebSocket

* ws.onmessage -> Callback de Mensagem Recebida

* ws.onopen -> Callback de canal aberto

* ws.onerror Callback para quando houver erro

Alguns exemplos de casos de uso do WebSocket: jogos on-line de vários jogadores;
aplicativos de
chat; links para esportes ao vivo; atualização em tempo real de redes sociais. O
WebSocket é uma
tecnologia moderna, e já está disponível em todos os navegadores atuais (exceto aqueles
que foram
descontinuados, como o Internet Explorer). Esse tema é novo e começou a aparecer em
editais,
mas ainda não foi cobrado em prova.

Por isso, entenda bem os conceitos desse tópico, pois seu examinador provavelmente fará
uma
questão simples sobre o que o WebSocket é (ou tentar te enganar, falando coisas que ele não é).


QUESTõES CoMENTADAS - WEBSoCkET

í. (UFC / CCV- 2019) Sobre WebSockets, assinale a alternativa correta.

a) WebSockets utiliza AJAX para possibilitar a comunicação RESTful.

b) WebSockets e Sockets de rede são sinônimos, representando o mesmo
protocolo e
especificação.

c) De acordo com a RFC 6455 que descreve o protocolo WebSocket, não é
possível
utilizar WebSockets em ambientes que possuam um servidor proxy.

d) O handshake WebSocket usa o cabeçalho HTTP Upgrade para mudar do protocolo HTTP
para
o protocolo WebSocket, com uma requisição de Upgrade.

e) Por padrão, o protocolo WebSocket usa a porta 8080 para conexões WebSocket comuns
e a
porta 443 para conexões WebSocket encapsuladas porTLS (Jransport Layer Security).

Comentários:

Lembre-se time: WebSockets é uma tecnologia avançada que torna possível abrir uma
sessão de
comunicação interativa entre o navegador do usuário e um servidor. Com esta API, você
pode
enviar mensagens para um servidor e receber respostas orientadas a eventos sem ter que
consultar
o servidor para obter uma resposta. Indo mais fundo, foi literalmente o que vimos: o
handshake
WebSocket usa o cabeçalho HTTP Upgrade para mudar do protocolo HTTP
para o
protocolo WebSocket, com uma requisição de Upgrade, guarde isso.

Gabarito: Letra D

Item. 2. (CESPE / TCE-PA - 2016) O WebSocket permite o desenvolvimento de diversas
aplicações em
tempo real como, por exemplo, aplicações de bate-papo, jogos online com múltiplos
jogadores
e mapas interativos.

Comentários:

Perfeito! O WebSocket permite o desenvolvimento de diversas aplicações em tempo real
como,
por exemplo, aplicações de bate-papo, jogos online com múltiplos jogadores e mapas interativos.

Gabarito: Correto

Item. 3. (COVEST / UFPE - 2019) Considerando os browsers mais populares (Chrome, Safari e
Firefox),
que dão vasto suporte à linguagem JavaScript, é correto afirmar que:

a) esses browsers por questões de segurança, não permitem que scripts manipulem o conteúdo
HTML que foi renderizado na página.


b) eles dão suporte nativo à comunicação bidirecional com aplicações remotas
através de
WebSockets.

c) além do suporte à biblioteca XMLHttpRequest para requisições com XML, eles
fornecem
suporte nativo ao objeto JSONHttpRequest para fazerem requisições AJAX com JSON.

d) esses browsers dão suporte à API EventSource do HTML5, que ainda não é nativa e
depende
de instalação de plugin ou extensão para tal.

e) o código escrito em JavaScript é incompatível com as versões desses
browsers para
smartphones.

Comentários:

Galera, só a alternativa B fala de websocket e está perfeitamente correta, os
respectivos browsers
dão suporte nativo à comunicação bidirecional com aplicações remotas através de WebSockets.

Gabarito: Letra B

Item. 4. (CCV - UFC - 2018) Sobre WebSocket assinale a afirmativa correta.

a) WebSocket não funciona na presença deum servidor proxy.

b) WebSocket é atualmente parte da especificação HTML5.

c) WebSocket permite a comunicação bidirecional por canais full-duplex sobre uma
conexão
UDP.

d) A especificação WebSocketdefine dois esquemas de URI: ws (WebSocket) and
ws-tls
(WebSocket Secure).

e) Por padrão, o protocolo WebSocket usa a porta 80 para conexões WebSocket regulares
e a
porta 443 para conexões WebSocket tuneladas sobre TLS (Jransport Layer Security).

Comentários:

Conforme vimos, o protocolo WebSocket usa a porta 80 para conexões WebSocket regulares
e a
porta 443 para conexões WebSocket tuneladas sobre TLS (Jransport Layer Security).

Gabarito: Letra E

Item. 5. (QUESTÃO INÉDITA) O WebSockets é uma tecnologia avançada que torna possível abrir
uma
sessão de comunicação interativa entre o navegador do usuário e um servidor

Comentários:


/ 114

/


Perfeito! O WebSockets é uma tecnologia avançada que torna possível abrir uma
sessão de
comunicação interativa entre o navegador do usuário e um servidor.

Gabarito: Correto

Item. 6. (QUESTÃO INÉDITA) WebSockets permitem abrir uma conexão com o servidor
remoto e
trafegar dados arbitrariamente do servidor para o cliente, mas não do cliente para o servidor.

Comentários:

Pode tanto ser do servidor para o cliente, como também do cliente para o
servidor. Logo,
WebSockets permitem abrir uma conexão com o servidor remoto e trafegar dados
arbitrariamente
do servidor para o cliente, vice-versa.

Gabarito: Errado

Item. 7. (QUESTÃO INÉDITA) Websocket utiliza uma comunicação bidirecional full-duplex
sobre um
único Soquete TCP.

Comentários:

Exato! Foi o que vimos, Websocket utiliza uma comunicação bidirecional full-duplex sobre
um único
Soquete TCP.

Gabarito: Correto

Item. 8. (QUESTÃO INÉDITA) É possível utilizar o WebSockets para sincronizar o meu
aplicativo de
perguntas com o aplicativo de vocês de forma que, a cada vez que eu responder uma
pergunta,
passe imediatamente para a próxima pergunta tanto no meu aplicativo quanto no
aplicativo de
vocês

Comentários:

Perfeito! É possível utilizar o WebSockets para sincronizar o meu aplicativo de
perguntas com o
aplicativo de vocês de forma que, a cada vez que eu responder uma pergunta, passe
imediatamente
para a próxima pergunta tanto no meu aplicativo quanto no aplicativo de vocês.

Gabarito: Correto

Item. 9. (QUESTÃO INÉDITA) Para utilizar o WebSocket, utilizamos uma URL de
conexão com
protocolo https.

Comentários:


/ 114

/


Utilizamos o protocolo ws e não o https. Logo, o correto seria: Para utilizar o
WebSocket, utilizamos
uma URL de conexão com protocolo ws. Exemplo:

let ws = new WebSocket("ws://meuservico.com.br/alguma");

Gabarito: Errado

Item. 10. (QUESTÃO INÉDITA) Entre as funcionalidades do websocket, temos o new
WebSocket(url),
que é responsável por abrir o websocket.

Comentários:

Perfeito! Entre as funcionalidades do websocket, temos o new WebSocket(url), que é
responsável
por abrir o websocket.

Gabarito: Correto

Item. 11. (QUESTÃO INÉDITA) Entre as funcionalidades do websocket, temos o ws.onerror, que
é o
callback de quando ocorrer um erro.

Comentários:

Perfeito! Entre as funcionalidades do websocket, temos o ws.onerror, que é o callback
de quando
ocorrer um erro.

Gabarito: Correto


/ 114

/


(Profs. Paolla Ramos e Raphael L

í. (UFC / CCV- 2019) Sobre WebSockets, assinale a alternativa correta.

a) WebSockets utiliza AJAX para possibilitar a comunicação RESTful.

b) WebSockets e Sockets de rede são sinônimos, representando o mesmo
protocolo e
especificação.

c) De acordo com a RFC 6455 que descreve o protocolo WebSocket, não é
possível
utilizar WebSockets em ambientes que possuam um servidor proxy.

d) O handshake WebSocket usa o cabeçalho HTTP Upgrade para mudar do protocolo HTTP
para
o protocolo WebSocket, com uma requisição de Upgrade.

e) Por padrão, o protocolo WebSocket usa a porta 8080 para conexões WebSocket comuns
e a
porta 443 para conexões WebSocket encapsuladas porTLS (Jransport Layer Security).

Item. 2. (CESPE / TCE-PA - 2016) O WebSocket permite o desenvolvimento de diversas
aplicações em
tempo real como, por exemplo, aplicações de bate-papo, jogos online com múltiplos
jogadores
e mapas interativos.

Item. 3. (COVEST / UFPE - 2019) Considerando os browsers mais populares (Chrome, Safari e
Firefox),
que dão vasto suporte à linguagem JavaScript, é correto afirmar que:

a) esses browsers por questões de segurança, não permitem que scripts manipulem o
conteúdo
HTMLquefoi renderizado na página.

b) eles dão suporte nativo à comunicação bidirecional com aplicações remotas
através de
WebSockets.

c) além do suporte à biblioteca XMLHttpRequest para requisições com XML, eles
fornecem
suporte nativo ao objeto JSONHttpRequest para fazerem requisições AJAX com JSON.

d) esses browsers dão suporte à API EventSource do HTML5, que ainda não é nativa e
depende
de instalação de plugin ou extensão para tal.

e) o código escrito em JavaScript é incompatível com as versões desses
browsers para
smartphones.

Item. 4. (CCV - UFC - 2018) Sobre WebSocket assinale a afirmativa correta.

a) WebSocket não funciona na presença deum servidor proxy.

b) WebSocket é atualmente parte da especificação HTML5.

c) WebSocket permite a comunicação bidirecional por canais full-duplex sobre uma
conexão
UDP.


d) A especificação WebSocketdefine dois esquemas de URI: ws (WebSocket) and
ws-tls
(WebSocket Secure).

e) Por padrão, o protocolo WebSocket usa a porta 8o para conexões WebSocket regulares
e a
porta 443 para conexões Vl/ebSoc/cettuneladas sobre TLS (Transport Layer Security').

Item. 5. (QUESTÃO INÉDITA) O WebSockets é uma tecnologia avançada que torna possível abrir
uma
sessão de comunicação interativa entre o navegador do usuário e um servidor

Item. 6. (QUESTÃO INÉDITA) WebSockets permitem abrir uma conexão com o servidor
remoto e
trafegar dados arbitrariamente do servidor para o cliente, mas não do cliente para o servidor.

Item. 7. (QUESTÃO INÉDITA) Websocket utiliza uma comunicação bidirecional full-duplex
sobre um
único Soquete TCP.

Item. 8. (QUESTÃO INÉDITA) É possível utilizar o WebSockets para sincronizar o meu
aplicativo de
perguntas com o aplicativo de vocês de forma que, a cada vez que eu responder uma
pergunta,
passe imediatamente para a próxima pergunta tanto no meu aplicativo quanto no
aplicativo de
vocês

Item. 9. (QUESTÃO INÉDITA) Para utilizar o WebSocket, utilizamos uma URL de
conexão com
protocolo https.

Item. 10. (QUESTÃO INÉDITA) Entre as funcionalidades do websocket, temos o new
WebSocket(url),
que é responsável por abrir o websocket.

Item. 11. (QUESTÃO INÉDITA) Entre as funcionalidades do websocket, temos o ws.onerror, que
é o
callback de quando ocorrer um erro.


/ 114

/


GABARITo - WEBSoCkET

Item. 1. LETRA D

Item. 2. CORRETO

Item. 3. LETRA B

Item. 4. LETRA E

Item. 5. CORRETO

Item. 6. ERRADO

Item. 7. CORRETO

Item. 8. CORRETO

Item. 9. ERRADO
ío.CORRETO

Item. 11. CORRETO

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I


PWA (PRoCRESSIvE WEB APPS)

Conceitos Básicos

INCIDÊNCIA EM PROVA: MÉDIA

Galera esse assunto ainda está em evolução, como quase tudo na TI, mas esse em
específico, dada
a sua relevância no atual cenário das plataformas como serviço, se encontra
literalmente em
evolução. Como assim, professor?

Os PWAs (Progressive Web Apps), caracterizam-se por serem progressivos,
responsivos e
semelhantes a aplicativos. São o novo horizonte na construção de plataformas, sendo uma
das
metodologias mais empregadas, quando o assunto é a criação de aplicações nativas, em
especial
de smarthphones, web 3.0, etc.

A ideia é simples, a internet evolui e as plataformas também evoluem e a orientação
a serviço é
cada vez mais presente, nas nossas vidas. Os PWAs oferecem através de navegadores,
design de
aplicações (apps) independente de plataforma, ou seja, não importa se você está
acessando da sua
smartTV ou do seu smartphone, a experiência do usuário será semelhante.

Vamos explorar isso com os sites, para ficar mais aderente. Imagina que você acessou
o Chrome ou
Mozilla Firefox e quer acesso o Google Maps.


Onde entra o PWA? Simples: Se através de uma página web, você conseguir acessar uma
função
nativa de um app, teremos Progressive Web Apps em ação.

O que você acabe de ver é uma versão do Google Maps, que está disponível na versão
PWA, assim
como outros aplicativos comuns, como Twitter e Instagram. Logo, podemos derivar que um
PWA
é um meio para extender aplicações nativas de apps, para websites tradicionais.

Bom, agora imagino que esteja bem claro que todos nós utilizamos
PWA diariamente,
principalmente quando visitamos marketplaces. As funcionalidades disponíveis nos
navegadores
mais modernos, tornam os PWAs rivais de peso dos aplicativos comuns (apps). Exemplo:

RECURSOS PWA | DESCRIÇÃO

NOTIFICAÇÃO EM PUSH os famosos alertas dos aplicativos podem ser executados a partir
dos PWAs,
mesmo após fechar o navegador;

SPLASHSCREEN os PWAs atuais também podem exibir telas de abertura para apresentara marca e
sua identidade visual;

ÍCONENAHOMEDOSMARTPHONE assim como os apps tradicionais, os PWAs podem guardar ícones
na home do
celular com link direto para o site ou uma área específica dele;

PROCESSOS EMBACKGROUND também é possível rodar serviços e funções em segundo plano, sem
interferir na
experiência do usuário;

SUPORTE OFFLINE como dito, os PWAs são capazes de manter funcionalidades disponíveis
sem
internet, utilizando o cache do navegador;


ACESSO À CÂMERA, ARQUIVOS,
CONTATOS EGEOLOCALIZAÇÃO

As aplicações PWA podem acessar recursos do dispositivo para aprimorar a
experiência no app.


SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I


QUESTõES CoMENTADAS - PWA

í. (CESPE / DPE-RO - 2022) Uma das vantagens do PWA em relação a outros front-ends é
a) a utilização de NFC.

b) a disponibilidade em lojas de aplicativos.

c) o funcionamento offline.

d) o suporte cross-browser.

e) a utilização de bluetooth.

Comentários:

Galera, conforme vimos, funcionar offiline é uma das vantagens dos PWAs. Só lembrar:

RECURSOS PWA | DESCRIÇÃO

NOTIFICAÇÃO EM PUSH os famosos alertas dos aplicativos podem ser executados a partir
dos PWAs,
mesmo após fechar 0 navegador;


SPLASHSCREEN
ÍCONENAHOMEDOSMARTPHONE

PROCESSOS EMBACKGROUND

os PWAs atuais também podem exibir telas de abertura para apresentara marca e
sua identidade visual;

assim como os apps tradicionais, os PWAs podem guardar ícones na home do
celular com link direto para o site ou uma área específica dele;

também é possível rodar serviços e funções em segundo plano, sem interferir na
experiência do usuário;

SUPORTE OFFLINE como dito, os PWAs são capazes de manter funcionalidades disponíveis
sem
internet, utilizando o cache do navegador;


ACESSO À CÂMERA, ARQUIVOS,
CONTATOS EGEOLOCALIZAÇÃO

As aplicações PWA podem acessar recursos do dispositivo para aprimorar a
experiência no app.

Gabarito: Letra C

Item. 2. (IADES / BRB - 2019) O desenvolvimento de uma PWA pressupõe:

a) Utilização de tecnologias comuns da Web, incluindo HTML, CSS e JavaScript.

b) Codificação nativa na plataforma de destino (seja ela iOS ou Android).

c) Desenvolvimento de uma aplicação considerada híbrida, pois será executada
em uma
Webview e terá acesso a recursos nativos do dispositivo via uma API JavaScript.

d) Necessidade de disponibilidade ininterrupta de conectividade com a internet por se
tratar de
uma aplicação Web.

e) Nenhum tipo de acesso aos recursos nativos do dispositivo, pois a aplicação será
executada
em um ambiente de navegador.

Comentários:


/ 114

/


A questão afirma o óbvio: HTML, CSS e JS são fundamentais em conteúdo,
aparência e
interatividade de qualquer página web, logo pressupor isso para PWA é essencial.

Gabarito: Letra A

Item. 3. (COMPERVE / UFRN - 2019) Progressive Web Apps são experiências que combinam a web
com
os aplicativos. Eles são acessados por usuários por meio de um navegador sem exigir
instalações
e, conforme o usuário desenvolve uma relação com o aplicativo, ele se torna cada vez
mais
eficaz. Um progressive web app caracteriza-se por ser
a) descobrível, nativo e independente de conectividade.

b) progressivo, nativo e semelhante a aplicativos.

c) descobrível, responsivo e acessível por lojas de aplicativos.

d) progressivo, responsivo e semelhante a aplicativos.

Comentários:

Conforme estudamos, um PWA caracteriza-se por ser progressivo, responsivo e
semelhante a
aplicativos.

Gabarito: Letra D

Item. 4. (QUESTÃO INÉDITA) Os PWAs encerram um dos maiores desafios envolvidos na criação
de
apps: as limitações e regras definidas pelas grandes lojas, como o Google Play e a
Apple Store,
que podem tornar os projetos muito mais caros e complexos.

Comentários:

Perfeito! Os PWAs batem de frente com os apps quanto as limitações das Stores, como
Google Play
ou Apple Store, são mais simples e fáceis de elaboração.

Gabarito: Correto

Item. 5. (QUESTÃO INÉDITA) Em relação ao acesso do usuário, os PWAs são uma solução mais
simples,
afinal, todos serviços podem ser usados, simplesmente, entrando em um site e
baixando a
aplicação. Com os apps tradicionais, é necessário acessar a loja do sistema, baixar a
aplicação,
abrir e ainda conceder uma série de permissões para, finalmente, utilizá-los.

Comentários:

Basta acessar a web em um site que já seja compatível com PWA, não precisa baixar
nenhuma
aplicação, este é o erro da questão.


/ 114

/


Gabarito: Errado

Item. 6. (QUESTÃO INÉDITA) Ao criar um PWA para sua empresa, seus desenvolvedores
poderão
fornecer updates normal mente. A diferença, aqui, é que o usuário não precisará
realizar nenhum
download de pacotes adicionais, pois todos os processos se mantêm vinculados ao site.

Comentários:

Exato! Ao criar um PWA para sua empresa, seus desenvolvedores poderão
fornecer updates
normalmente. A diferença, aqui, é que o usuário não precisará realizar nenhum
download de
pacotes adicionais, pois todos os processos se mantêm vinculados ao site.

Gabarito: Correto

Item. 7. (QUESTÃO INÉDITA) Os PWAs têm o potencial de ampliar significativamente os acessos
a
aplicações web, mas não oferecem redução de custos com desenvolvimento web.

Comentários:

Claramente oferecem redução de custos com desenvolvimento web, uma vez que a manutenção
de apps exige diferentes equipes especializadas para cada tipo e geração de sistema
operacional.
Logo, PWAs são economicamente mais viáveis.

Gabarito: Errado

Item. 8. (QUESTÃO INÉDITA) As grandes redes sociais da atualidade oferecem PWAs em quase
todas
as funções dos seus apps oficiais.

Comentários:

Como dito, as redes sociais são sem duvida um dos principais cases de utilização de PWAs.

Gabarito: Correto

Item. 9. (QUESTÃO INÉDITA) Os Progressive Web Apps podem favorecer blogse portais de
notícias
gerando tráfego contínuo às suas páginas.

Comentários:

Além disso, os PWAs ainda podem incentivar a leitura de novos conteúdos nas redes
sociais e
newsletters, oferecendo acesso rápido pela home e por notificações, sem precisar
convencer o seu
público a baixar um app ou realizarqualquertipo de cadastro.


Gabarito: Correto
io.(QUESTÃO INÉDITA) Os PWAs podem ser adicionados às homes dos smartphones,
dispensando a necessidade de abrir o navegador e digitar uma URL.

Comentários:

Conforme vimos, os PWAs podem ser adicionados às homes dos smartphones,
dispensando a
necessidade de abrir o navegador e digitar uma URL.

Gabarito: Correto


/ 114

/


LISTA DE QUESTõES - PWA

í. (CESPE / DPE-RO - 2022) Uma das vantagens do PWA em relação a outros front-ends é
a) a utilização de NFC.

b) a disponibilidade em lojas de aplicativos.

c) o funcionamento offline.

d) o suporte cross-browser.

e) a utilização de bluetooth.

Item. 2. (IADES/BRB-2019) O desenvolvimento de uma PWA pressupõe:

a) Utilização de tecnologias comuns da Web, incluindo HTML, CSS e JavaScript.

b) Codificação nativa na plataforma de destino (seja ela iOS ou Android).

c) Desenvolvimento de uma aplicação considerada híbrida, pois será executada
em uma
Webview e terá acesso a recursos nativos do dispositivo via uma API JavaScript.

d) Necessidade de disponibilidade ininterrupta de conectividade com a internet por se
tratar de
uma aplicação Web.

e) Nenhum tipo de acesso aos recursos nativos do dispositivo, pois a aplicação será
executada
em um ambiente de navegador.

Item. 3. (COMPERVE / UFRN - 2019) Progressive Web Apps são experiências que combinam a
web com
os aplicativos. Eles são acessados por usuários por meio de um navegadorsem exigir
instalações
e, conforme o usuário desenvolve uma relação com o aplicativo, ele se torna cada vez
mais
eficaz. Um progressive web app caracteriza-se por ser
a) descobrível, nativo e independente de conectividade.

b) progressivo, nativo e semelhante a aplicativos.

c) descobrível, responsivo e acessível por lojas de aplicativos.

d) progressivo, responsivo e semelhante a aplicativos.

Item. 4. (QUESTÃO INÉDITA) Os PWAs encerram um dos maiores desafios envolvidos na criação
de
apps: as limitações e regras definidas pelas grandes lojas, como o Google Play e a
Apple Store,
que podem tornar os projetos muito mais caros e complexos.

Item. 5. (QUESTÃO INÉDITA) Em relação ao acesso do usuário, os PWAs são uma solução mais simples,
afinal, todos serviços podem ser usados, simplesmente, entrando em um site e
baixando a
aplicação. Com os apps tradicionais, é necessário acessar a loja do sistema, baixar a
aplicação,
abrir e ainda conceder uma série de permissões para, finalmente, utilizá-los.


Item. 6. (QUESTÃO INÉDITA) Ao criar um PWA para sua empresa, seus desenvolvedores
poderão
fornecer updates normal mente. A diferença, aqui, é que o usuário não precisará
realizar nenhum
download de pacotes adicionais, pois todos os processos se mantêm vinculados ao site.

Item. 7. (QUESTÃO INÉDITA) Os PWAs têm o potencial de ampliar significativamente os acessos
a
aplicações web, mas não oferecem redução de custos com desenvolvimento web.

Item. 8. (QUESTÃO INÉDITA) As grandes redes sociais da atualidade oferecem PWAs em quase
todas
as funções dos seus apps oficiais.

Item. 9. (QUESTÃO INÉDITA) Os Progressive Web Apps podem favorecer blogs e portais de
notícias
gerando tráfego contínuo às suas páginas.

Item. 10. (QUESTÃO INÉDITA) Os PWAs podem ser adicionados às homes dos
smartphones,
dispensando a necessidade de abrir o navegador e digitar uma URL.


/ 114

/


GABARITo - PWA


Item. 1. LETRA C 5- ERRADO

Item. 2. LETRA A 6. CORRETO

3- LETRA D 7- ERRADO

4- CORRETO 8. CORRETO

Item. 9. CORRETO

Item. 10. CORRETO


/ 1


