Capítulo. Engenharia de Software e Sistemas - Engenharia de requisitos. Gestão de backlog. Gestão de Dívida Técnica.


Índice

1) Engenharia de Requisitos

2) Engenharia de Requisitos - Classificação de Requisitos

3) Engenharia de Requisitos - Engenharia de Requisitos

4) Resumo - Engenharia de Requisitos

5) Questões Comentadas - Engenharia de Requisitos - CESPE

6) Questões Comentadas - Engenharia de Requisitos - FCC

7) Questões Comentadas - Engenharia de Requisitos - FGV

8) Questões Comentadas - Engenharia de Requisitos - Diversos ...

9) Lista de Questões - Engenharia de Requisitos - CESPE

10) Lista de Questões - Engenharia deRequisitos - FCC

11) Lista de Questões - Engenharia deRequisitos - FGV

12) Lista de Questões - Engenharia deRequisitos - Diversas

13) Débito Técnico


APRESENTAçÃo

Seus maravilhosos, essa aula é essencial para todos os concursos! Eu não consigo descrever a
importância
desse conteúdo - é absolutamente importantíssimo que vocês dominem esse assunto. Se esse conteúdo
está no edital, há 99,999999999999% de chances de ele cair na prova. Por que? Porque não é
possível
pensar em software algum sem pensar nos requisitos. Bacana? Então vamos lá, não quero
ver ninguém
desanimado:)

PROFESSOR DIEGO CARVALHO - WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

Galera, todos os tópicos da aula possuem Faixas de Incidência, que indicam se o
assunto cai
muito ou pouco em prova. Diego, se cai pouco para que colocar em aula? Cair pouco
não significa
que não cairá justamente na sua prova! A ideia aqui é: se você está com pouco tempo
e precisa ver
somente aquilo que cai mais, você pode filtrar pelas incidências média, alta e
altíssima; se você tem
tempo sobrando e quer ver tudo, vejam também as incidências baixas e baixíssimas. Fechado?

Além disso, essas faixas não são por banca - é baseado tanto na quantidade de vezes que caiu em
prova independentemente da banca e também em minhas avaliações sobre cada assunto...


fATENÇÃO

Avisos
Importantes

O curso abrange todos os níveis de conhecimento...

Esse curso foi desenvolvido para ser acessível a alunos com diversos níveis de
conhecimento diferentes. Temos alunos mais avançados que têm
conhecimento prévio ou têm facilidade com o assunto. Por outro lado, temos
alunos iniciantes, que nunca tiveram contato com a matéria ou até mesmo que
têm trauma dessa disciplina. A ideia aqui é tentar atingir ambos os públicos -

iniciantes e avançados - da melhor maneira possível..

Por que estou enfatizando isso?

O material completo é composto de muitas histórias, exemplos, metáforas, piadas, memes, questões,
desafios, esquemas, diagramas, imagens, entre outros. Já o material simplificado possui exatamente o
mesmo núcleo do material completo, mas ele é menor e bem mais objetivo. Professor, eu devo estudar
por
qual material? Se você quiser se aprofundar nos assuntos ou tem dificuldade com a matéria,
necessitando
de um material mais passo-a-passo, utilize o material completo. Se você não quer se aprofundar nos
assuntos ou tem facilidade com a matéria, necessitando de um material mais direto ao ponto, utilize
o
material simplificado.

Por fim...

O curso contém diversas questões espalhadas em meio à teoria. Essas
questões possuem um comentário mais simplificado porque têm o único
objetivo de apresentar ao aluno como bancas de concurso cobram o
assunto previamente administrado. A imensa maioria das questões para
que o aluno avalie seus conhecimentos sobre a matéria estão dispostas ao
final da aula na lista de exercícios e possuem comentários bem mais
completos, abrangentes e direcionados.


I


Conceitos Básicos

REQUISIToS

INCIDÊNCIA EM PROVA: BAIXA

Pessoal, vamos começar beeeeeeeem o básico do básico! O que significa o verbo
"requisitar"? De
acordo com o dicionário, requisitar é pedir ou requerer algo ou alguém de modo
oficial ou
formal. É solicitar alguma coisa, geralmente de forma temporária; é exigir.
Já o substantivo
"requisito" é aquilo que é necessário e indispensável; uma condição indispensável; uma
exigência.
Beleza, isso é o básico - agora nós vamos ver alguns exemplos.


COMPUTAÇÃO
BÁSICA

ESTRUTURAS
DE DADOS

ORGANIZAÇÃO
DE ARQUIVOS

LINGUAGENS DE
PROGRAMAÇÃO

Vamos imaginar um exemplo da saudosa época de faculdade! Início de semestre, é a hora
de
fazer a matrícula. Vejam o fluxo de disciplinas apresentado acima do curso
de Ciência da
Computação da Universidade de Brasília (UnB), onde eu fiz a minha graduação! Galera,
no currículo
do curso, terfeito a disciplina de Computação Básica é requisito para fazer a
disciplina de Estrutura
de Dados.

Assim como ter feito a disciplina de Estrutura de Dados é requisito para fazer a
disciplina de
Organização de Arquivos; e ter feito a Organização de Arquivos é requisito para fazer
Linguagens
de Programação. Se você estiver no primeiro semestre, você não pode fazer a
disciplina de
Organização de Arquivos, porque você obrigatoriamente precisa ter feito
Computação Básica e
Estrutura de Dados. Notem que uma matéria é exigência para outra.

Na verdade, no momento da matrícula de uma determinada matéria, é possível verificar
quais são
os pré-requisitos exigidos para fazê-la. Querem outro exemplo? Vamos para a área jurídica! Algum
de vocês quer mudar o Brasil e decide se candidatar à Presidente da República! No entanto, não
é simples assim... é necessário cumprir uma série de requisitos para poder sequer
concorrer a esse
cargo-como mostra a imagem a anterior.

Para ser candidato você deve ser brasileiro nato; ter idade superior a trinta a cinco
anos; estar em
pleno exercício dos direitos políticos; ser eleitor e ter domicílio eleitoral no
Brasil; ser filiado a uma
agremiação ou partido político; e não ter substituído o atual presidente nos seis
meses antes da
eleição. Satisfeitos esses requisitos, você - revolucionário que irá mudar nossa nação
- poderá
ser candidato à presidência. Bacana, pessoal?

Viram como é tranquilo de compreender o que é um requisito? É um conceito comum que faz parte
do nosso cotidiano! No contexto de Engenharia, costuma-se defini-lo como uma propriedade
ou
um comportamento que um produto ou serviço deve atender. Já no contexto de Engenharia
de
Software, costuma-se defini-lo como uma condição que deve ser satisfeita para se
alcançar um
objetivo, ou a qualidade do sistema que deve ser provida para ser útil a seus usuários.


Classificação de Requisitos

Galera, existem diversas maneiras diferentes de se classificar requisitos de software!
Veremos a
seguir algumas dessas classificações:


Classificação quanto ao nível de abstração

INCIDÊNCIA EM PROVA: BAIXA

Vamos iniciar falando sobre a classificação quanto ao nível de abstração. O que é
abstração? Em
resumo, é a subtração de detalhes. Logo, se algo é muito abstrato, então é pouco
detalhado;
se algo é pouco abstrato, então é muito detalhado. Bacana? Essa classificação se
divide em
Requisitos de Usuário e Requisitos de Sistema-evidentemente que o primeiro é mais
abstrato que
o segundo. Vejam só...

Requisitos de Usuário: descrições, em linguagem natural e com diagramas, de quais
serviços o
sistema deve fornecer e as restrições sob as quais deve operar. São requisitos com
alto nível de
abstração e poucos detalhes, feitos para serem lidos por pessoas leigas - podem ser
funcionais
ou não funcionais (veremos essa classificação mais à frente).

Exemplo: o sistema deve gerar um relatório de acompanhamento mensal e enviar para os
usuários
por e-mail - notem que há poucos detalhes e nada muito técnico.

Requisitos de Sistema: descrições detalhadas sobre as funções, operações e
restrições de
sistema que definem exatamente o que deve ser implementado. São requisitos com baixo
nível
de abstração e muitos detalhes, feitos para serem lidos por pessoas experientes -
podem ser
funcionais ou não funcionais (veremos essa classificação mais à frente).

Exemplo: o sistema deve gerar um relatório com índices a partir de views
materializadas gerados a
partir de um banco multidimensional - bem mais detalhes e bem mais técnico.

Professor, isso é só para complicar a minha vida? Não, pessoal - por incrível que
pareça, isso tem a
sua utilidade! Ao escrever requisitos, deve-se considerar quem serão seus leitores, uma
vez que
eles possuem níveis diferentes de conhecimento, portanto os requisitos devem
ter níveis
diferentes de detalhamento. Usuários geralmente não dão a mínima para como o sistema
será
implementado; já programadores necessitam de detalhes maistécnicos e precisos.

(TCE/PR - 2011) No processo de engenharia de requisitos, os tipos de requisitos de
usuário e de sistema podem ser, respectivamente,

a) apenas funcionais; apenas não funcionais.

b) apenas não funcionais; apenas funcionais.

c) apenas funcionais; funcionais e não funcionais.

d) funcionais e não funcionais; apenas não funcionais.


e) funcionais e não funcionais; funcionais e não funcionais.

Comentários: ambos podem sertanto funcionais quanto não-funcionais (Letra E).

(MEC - 2015) Os requisitos de usuários são mais específicos que os
requisitos de
sistemas, uma vez que estes últimos são utilizados para expressar o que o sistema deve
implementar.

Comentários: na verdade, os requisitos de sistema são mais específicos e detalhados que os
requisitos de usuário - 0 primeiro
são descrições mais detalhadas das funções, serviços e restrições operacionais do
sistema de software; e 0 segundo são
declarações, em uma linguagem natural com diagramas, de quais serviços 0 sistema deverá
fornecer a seus usuários e as
restrições com as quais este deve operar (Errado).

(SERPRO - 2013) Um exemplo de requisito de sistema bem descrito é: "O sistema deve
fornecer um gráfico comparativo entre as vendas previstas e as realizadas".

Comentários: esse é um exemplo de requisitos de usuário e, não, de sistema (Errado).

(MEC-2011) A documentação de requisitos deve conter duas perspectivas: uma voltada
para o cliente, em linguagem compreensível por ele, e outra voltada
para o
desenvolvedor, em uma linguagem técnica de modelagem.

Comentários: a questão trata respectivamente dos requisitos de usuário e dos requisitos de sistema
(Correto).

(IPHAN - 2018) Situação hipotética: Ao efetuar a especificação de requisitos,
um
analista abrangeu os requisitos de usuário e os de sistema, tendo incluído
entre os
requisitos de usuário os funcionais e os não funcionais. Assertiva: A
especificação
realizada pelo analista está correta, pois os requisitos não funcionais podem ser
inseridos
nos requisitos de usuário.

Comentários: requisitos de usuário e de sistema podem ser funcionais ou não-funcionais (Correto).


Classificação quanto à qualidade

INCIDÊNCIA EM PROVA: BAIXA

Vamos falar sobre a classificação quanto à qualidade, mas antes nós vamos
ver um conceito
importante: Quality Function Deployment (QFD). Traduzido como Disponibilização da
Função de
Qualidade, trata-se de uma técnica de gestão da qualidade aplicada ao
levantamento de
requisitos que traduz as necessidades do cliente em requisitos técnicos buscando
maximizar a
satisfação do cliente e enfatizando o entendimento do que é valioso para o cliente.

Requisitos Normais: refletem os objetivos e metas estabelecidos para um produto ou
sistema
durante reuniões com o cliente. Se esses requisitos estiverem presentes, o cliente fica
satisfeito.
Exemplos de Requisitos Normais poderiam sertipos de displays gráficos solicitados,
funções de
sistema específicas e níveis de desempenho definidos.

Requisitos normais são exatamente o que a palavra diz: são aqueles requisitos
normais,
comuns, corriqueiros, etc. Imaginem que vocês estão levantando requisitos para um
sistema de
livros de uma biblioteca. Considerando esse contexto, um requisito normal
poderia ser por
exemplo: "cadastrar livros recebidos" ou "permitir buscar um livro pelo seu
título". Enfim... são
requisitos completamente normais para o contexto do negócio.

Requisitos Esperados: estão implícitos no produto ou sistema e podem sertão
fundamentais
que o cliente não os declara explicitamente. Sua ausência será causa de grande
insatisfação.
Exemplos de Requisitos Esperados: facilidade na interação homem-máquina,
confiabilidade e
correção operacional global e facilidade na instalação do software.

Nós vimos que um requisito normal seria permitir a busca por um livro a partir do
seu título. Agora
imaginem que essa busca retorne que encontrou dezenas de livros com o título que eu
inseri, mas
não informa quais-apenas diz que encontrou Galera, é evidente que eu não quero saber
apenas
que livros foram encontrados a partir de um título, eu também quero saber quais
livros foram
encontrados. Então, o que seria um requisito esperado?

Um requisito esperado seria um relatório com todos os livros encontrados a partir do
título de
entrada. Se o sistema simplesmente diz que encontrou livros com o título
inserido, mas não
apresenta nenhum relatório com os livros encontrados, isso pode gerar uma grande
insatisfação no
cliente, porque esse é um requisito esperado que ele sequer precisa
especificar para os
desenvolvedores. Entenderam agora?

Requisitos Fascinantes: esses recursos vão além da expectativa dos clientes e
demonstram ser
muito satisfatórios quando presentes. Por exemplo, o software para um novo celular vem
com
recursos-padrão, mas junto vem um conjunto de capacidades não esperadas.
Exemplos de
Requisitos Fascinantes: tecla multitoque e correio de voz visual.

Imaginem que o programador implementou o cadastro dos livros, implementou um filtro
para que
você possa buscá-los com diversos parâmetros diferentes, implementou também o relatório dos
livros encontrados, mas - pensando que se trata de uma biblioteca - ele implementou
tudo isso
funcionando com tecnologia assistiva que pode ajudar portadores de necessidades especiais,
por exemplo com um leitor de tela para cegos, por exemplo.

Notem que, por vezes, nem o usuário tinha pensado em pedir isso, mas o programador
foi lá e
implementou - isso é um requisito fascinante, porque ele supera as expectativas dos clientes.

(SINESP - 2015) A disponibilização da função de qualidade (Quality
Function
Deployment, QFD) é uma técnica aplicável à atividade de levantamento de requisitos a
qual traduz as necessidades do cliente para requisitos técnicos de software. Esta
técnica
classifica as necessidades em requisitos:

a) essenciais, reais e complexos.

b) reais, complexos e normais.

c) complexos, fascinantes e essenciais.

d) fascinantes, esperados e reais.

e) normais, esperados e fascinantes.

Comentários: trata-se dos requisitos normais, esperados e fascinantes (Letra E).


Classificação quanto à evolução

INCIDÊNCIA EM PROVA: BAIXA

Agora nós vamos falar sobre a classificação de requisitos quanto à evolução. Galera,
essa
classificação divide os requisitos em requisitos permanentes e requisitos voláteis. Vejamos...

Requisitos Permanentes: também chamados de Requisitos Estáveis, estão
diretamente
ligados a atividade principal da organização. São concebidos com a essência de um
sistema e
seu domínio da aplicação, e mudam mais lentamente que requisitos voláteis. Em geral,
eles são
derivados do Modelo de Domínio.

Eu particularmente não gosto muito desse nome e preferia que fosse chamado de
requisitos estáveis
em vez de requisitos permanentes, porque o termo permanente dá a impressão de que os
requisitos
não mudam e nós sabemos que requisitos sempre mudam. Os requisitos permanentes são mais
estáveis e que mudar pouco ou demoram bastante para mudar. Diego, você pode dar um exemplo
de requisito permanente? Claro, vamos lá...

Imaginem um domínio de aplicação (Ex: Bolsa de Valores). Ora, é natural que - em um
sistema da
Bolsa de Valores - existam sempre requisitos relacionados a ações, câmbio, cotações,
índices, etc.
Se, daqui vinte anos, um outro sistema for feito para a Bolsa de Valores, é bem
provável que
continue existindo requisitos relacionados a ações, câmbio, cotações, índices,
etc. Pode mudar
uma coisa ou outra, mas esses requisitos são mais estáveis com o passar do tempo.

Requisitos Voláteis: também chamados de Requisitos Instáveis, são específicos
para a
instanciação de um sistema em um ambiente ou um cliente particular e são mais
propensos a
mudança. Se modificam quando o sistema está em desenvolvimento ou em uso. Podem ser
subclassificados em mutáveis, emergentes, consequentes ou de compatibilidade:

o Mutáveis: são os requisitos que se modificam em função de mudanças no ambiente no
qual
o sistema opera. Por exemplo, os requisitos para um sistema que calcula taxas de
dedução
que evoluem conforme as leis fiscais são atualizadas (muito comum no Brasil).

o Emergentes: são os requisitos que não podem ser completamente definidos
quando o
sistema é especificado e emergem (olha a dica!) à medida que a compreensão do cliente
sobre o sistema se desenvolve. Em geral, eles só aparecerão durante o desenvolvimento.

o Consequentes: são os requisitos baseados em suposições de como o sistema será
utilizado,
isto é, são resultado da introdução do sistema no ambiente do usuário. O usuário
percebe as
necessidades enquanto utiliza sistema e esses requisitos são uma consequência do uso.

o De Compatibilidade: são os requisitos que dependem de outro equipamento,
processo,
componente ou elemento. Conforme outros elementos mudam, esses requisitos também
mudam. Esses são requisitos menos comuns, mas que também ocorrem.


Imaginem que, no desenvolvimento do sistema, deseja-se que o índice IBOV da Bovespa
fique
posicionado no canto inferior direito da tela, mas depois eu percebo que esse é um
dado muito
importante para ficar isolado no canto, então eu mudo o meu requisito para que essa
informação
fique bem grande no centro da tela. Vocês percebem como esse é um requisito mais
instável? Outra
pessoa pode achar que o índice não é tão importante para ficar no centro da tela.

(UNEAL-2009) São requisitos relativamente estáveis derivados da atividade central
da
organização e que se relacionam diretamente ao domínio do sistema. Qual opção abaixo
corresponde à descrição anterior?

a) Requisitos mutáveis
b) Requisitos emergentes
c) Requisitos conseqüentes
d) Requisitos permanentes
e) Requisitos de compatibilidade

Comentários: requisitos relativamente estáveis são os requisitos permanentes (Letra D).

(SEFAZ/BA - 2014) Segundo Sommerville (2004), os requisitos são divididos em duas
classes. São elas:

a) requisitos voláteis e requisitos funcionais.

b) requisitos permanentes e requisitos voláteis.

c) requisitos de compatibilidade e requisitos mutáveis.

d) requisitos mutáveis e requisitos emergentes.

e) requisitos emergentes e requisitos consequentes.

Comentários: os requisitos podem ser divididos em permanentes e voláteis (Letra B).

(BAHIAGÁS - 2016 - Item IV) Requisitos permanentes são requisitos que irão mudar
durante o processo de desenvolvimento do sistema ou depois que o sistema estiver em
operação.

Comentários: a questão trata dos requisitos voláteis (Errado).


Classificação quanto à funcionalidade

INCIDÊNCIA EM PROVA: ALTÍSSIMA

Percebam o seguinte: podemos classificar requisitos de diversas maneiras. No
entanto, não se
discute que a classificação de requisitos quanto a sua funcionalidade é, com total e
absoluta
certeza, a classificação mais tradicional e mais frequentemente cobrada em provas.
Galera, se
eu tivesse que apostar em algum assunto para cair na prova, eu apostaria nesse! No
entanto, fiquem
tranquilos porque é fácil;)

Requisitos Funcionais: são ações ou funcionalidades que o sistema deve fornecer para
atingir
seus objetivos. Eles dependem do tipo de software, dos usuários esperados e do tipo
de sistema
onde o software será implantado e fazem parte da arquitetura de um sistema. Grosso
modo,
pode-se dizer que eles tratam de o que o sistema deve fazer enquanto os requisitos
não-
funcionais tratam de como o sistema deve fazer.

REQUISITOS FUNCIONAIS

Declarações de serviços que o sistema deve fornecer.
Como o sistema deve reagir a entradas específicas.

Como o sistema deve comportarem determinadas situações.
Podem estabelecer explicitamente o que o sistema não deve fazer.
Podem ser descritos como requisitos de usuário (abstrato).

Em regra, descrevem a função do sistema detalhadamente, com entradas, saídas, exceções, etc.
Em princípio, sua especificação deve ser completa e consistente.

Problemas dos Requisitos Funcionais: frequentemente, requisitos funcionais
não são
estabelecidos precisamente. Há descrições de requisitos ambíguos, que
permitem diversas
interpretações; há também requisitos incompletos, que não descrevem toda a
funcionalidade do
serviço; e há requisitos inconsistentes, que contradizem outros requisitos do sistema.

Exemplos de Requisitos Funcionais:

Pensemos em um Requisito do Outlook: Sistema deverá fornecer opção de filtrar
e-mails por
Assunto e Anexos.

Pensemos em um Requisito do Youtube: Sistema deverá reagir com suspensão de
vídeos que
ferem direito autoral.

Pensemos em um Requisito do GoogleMaps: Sistema deverá procurar rua mais próxima,
caso
não encontre a desejada.

Requisitos Não-Funcionais: são restrições ou condições estipuladas sobre as quais o
sistema
deve funcionar. Não estão diretamente relacionados às funções específicas do sistema,
mas às
gerais-e podem incluir restrições de tempo, restrições de processo de desenvolvimento,
restrições
impostas por padrões, entre outras. Podem ser mais críticos que os funcionais e sempre
devem ser
verificáveis. Eles fazem parte da arquitetura técnica de um sistema.


REQUISITOS NÃO-FUNCIONAIS

Definem restrições globais e fazem parte da arquitetura técnica de um sistema.
Não se preocupam diretamente com a funcionalidade em si.

Colocam restrições sobre a qualidade e os atributos do sistema.

Incluem características como confiabilidade, segurança, usabilidade, performance, custos, robustez,
etc.

Problemas de Requisitos Não-Funcionais: frequentemente, requisitos não-funcionais
são
bastante difíceis de se especificar objetivamente. Para tal, utilizam-se medidas
que possam ser
testadas ou mensuradas. No entanto, o problema mais comum são os requisitos
conflitantes.
Exemplo: o cliente deseja um desempenho altíssimo, mas quer que o sistema tenha baixo custo.

Exemplos de Requisitos Não-Funcionais:

Pensemos em um Requisito do Whatsapp: Sistema deverá fornecer disponibilidade
mínima de
99,8%.

Pensemos em um Requisito do Facebook: Sistema deverá ser desenvolvido
utilizando a
linguagem Java.

Pensemos em um Requisito do Android: Sistema deverá ser capaz de rodar com apenas
íGb de
RAM.

Requisitos de Domínio: são requisitos derivados do domínio da aplicação e
refletem
características de sua área de negócio. Eles podem ser requisitos funcionais ou
não-funcionais e,
caso não sejam satisfeitos, o sistema pode não ser realizável. Por exemplo, um avião
que não
atende aos requisitos de confiabilidade, não será certificado para voo.

Pessoal, requisitos de domínio nada mais são que requisitos relacionados a um
domínio de
aplicação específico, sendo funcional ou não-funcional. Sinceramente, galera... essa
classificação
não tem a menor utilidade. A boa notícia é que ela não cai muito e que, na última
edição do
Sommerville, ele até retirou todo o destaque dessa classificação - colocando de forma
bastante
isolada no livro. Vamos seguir...

Problemas de Requisitos de Domínio: frequentemente, requisitos de domínio são
descritos na
linguagem ou jargão do domínio da aplicação. Especialistas de domínio
compreendem tão
profundamente assuntos sobre a sua área que eventualmente eles deixam de detalhar
informações
importantes, por acharem que são óbvias demais ou que já estão subentendidas.

Exemplos de Requisitos de Domínio:

Pensemos em um Requisito da USP: Sistema deverá calculara nota final da prova de
mestrado
segundo a fórmula (1.74^+3.17^ + 2-5gN₃)/3 * IRA (Aluno).

Pensemos em um Requisito da STN: Sistema deverá calcular o valor do Título
Público NTN-B
multiplicado pelo valor da Taxa SELIC do mês corrente.


Pensemos em um Requisito da NASA: Sistema deverá funcionar em uma Câmera 4K captando
infravermelho e resistente a variações de temperatura.

De acordo com Sommerville: a distinção entre esses diferentes tipos de requisitos não
é tão clara
como sugere essas definições. Um requisito pode parecer-se inicialmente não
funcional, mas
quando desenvolvido com mais detalhes pode dar origem a uma série de novos
requisitos
funcionais. Ao discutirmos sobre requisitos devemos levar em conta que na
realidade a
distinção entre eles é artificial.

Nosso autor ainda diz que os requisitos não funcionais estão
raramente associados às
características individuais do sistema. Trata-se de qualidades globais de um
software, como
manutenibilidade, usabilidade, desempenho, custos e várias outras. Normalmente
estes requisitos
são descritos de maneira informal e, segundo ele, geralmente afetam a arquitetura do
sistema.
Fechado? A questão abaixo é o nosso desafio... tentem fazer sem olhar o gabarito!

(SEFAZ/SP - 2013) Dentre os requisitos obtidos para a construção do software
constavam:

Item. 1. O software deve permitir as funções de cadastro, consultas diversas, alteração de
dados e exclusão de alunos, professores e demais colaboradores.

Item. 2. O sistema deve ser fácil de usar, fácil de encontrar o que se procura e fácil
de
memorizar os passos para executar as operações mais comuns.

Item. 3. O sistema deve ter seu funcionamento baseado nas tecnologias web.

Item. 4. Todas as operações disponibilizadas no sistema devem contemplar a legislação
vigente.

Item. 5. O sistema deve fazer interface com o sistema da Receita Federal por
meio de
requisições/respostas utilizando XML.

Item. 6. Os alunos devem poder obter por meio do sistema informações sobre suas faltas e
notas em cada disciplina.

Item. 7. O boletim e o histórico do aluno poderão serconsultados e visualizados pelos
gestores,
funcionários da secretaria e pelo próprio aluno.

Item. 8. Ao clicar em uma opção para gerar o boletim do aluno, deve ser apresentada ao
solicitante uma tabela com todas as disciplinas que o aluno cursou, bem como as notas
das provas e o número total de faltas em cada disciplina.


Item. 9. O sistema deve responder à solicitação de geração do boletim de um aluno em no
máximo 10 segundos.

Item. 10. O sistema deve calcular a média aritmética das duas maiores dentre três notas de
cada disciplina no final do semestre.

Item. 11. Quando o sistema constatar que o aluno tem mais que 25% de faltas em uma
disciplina do semestre, deve ser exibida no boletim do aluno a informação "Reprovado".

Item. 12. O sistema deverá suportar a execução em qualquer plataforma de hardware e/ou
sistema operacional.

Item. 13. O sistema deve enviar automaticamente para o e-mail dos gestores autorizados um
relatório com o número de alunos inadimplentes por curso.

Item. 14. O sistema não deve revelar quaisquer dados pessoais dos alunos aos professores,
exceto informações sobre notas e faltas no curso em que o professor leciona.

Item. 15. O sistema deve permitir que o professor inclua ou modifique as notas de seus alunos
durante o semestre letivo.

Item. 16. A quantidade de memória necessária para que um terminal possa executar o sistema

, nas condições mínimas aceitáveis é de 1 gigabyte.

Item. 17. A taxa aceitável de falhas nas operações realizadas pelo usuário no sistema deve ser
de 1 falha para cada 200 operações.

Item. 18. O sistema e sua respectiva documentação deverão ser entregues em um ano a partir
da data atual.

Item. 19. O sistema não deve permitir operações que beneficiem alguns usuários em
detrimento de outros.

Item. 20. A interface do usuário deve ser construída utilizando HTML5 e CSS.

Item. 21. Se a média do aluno por disciplina, calculada no final do semestre, for menor do que
7, deve ser exibido no boletim do aluno a informação "Reprovado".

Baseado nos requisitos apresentados, é correto afirmar que são requisitos funcionais os
de números:

a) 1, 2, 6,10,11,14,15,16 e 21.

b) 1, 6, 8,10,11,13,14,17,18 e 19.

c) 1, 6, 7, 8,10,11,13,15 e 21.


d) í, 3, 4, 8, io, li, 12,13,15,18 e 21.

e) 2, 3, 4, 5, 9,12,14,16,17,18,19 e 20.

Comentários: Requisitos Funcionais (RF): 1, 6, j, 8, 10, 11, 13,15, 21; Requisitos Não-Funcionais
(RNF): 2, 3, 4, 5, 9,12,14,16,17,
18,19, 20. Não era necessário analisar todos os requisitos, era possível fazer por eliminação. Como
assim? 1 é RF, elimina-se a
Letra E; 2 é RNF, elimina-se a Letra A; 3 é RNF, elimina-se a Letra D; 7 é RF, elimina-se a Letra B
(Letra C).

(TRF4 - 2019) Suponha que um Analista de TI, participando da etapa de análise de
requisitos de um sistema de emissão de certidão negativa para o TRF4, tenha elencado
os requisitos apresentados abaixo:

Item. 1. Utilizar interface responsiva para que possa ser executado em dispositivos móveis e
na
web.

Item. 2. Validar 0 tipo de certidão solicitado.

Item. 3. Emitir certidão negativa após verificação de situação do requerente.

Item. 4. Solicitar 0 CPFdo requerente.

Item. 5. Responder ao clique único do usuário em qualquer botão da interface.

Item. 6. Validar 0 CPF do requerente.

Item. 7. Restaurar os dados automaticamente após falhas não programadas.

Item. 8. Solicitar o nome do requerente.

g. Oferecer dois tipos de certidão: para fins gerais e para fins eleitorais.

Item. 10. Emitir aviso de impossibilidade de emissão da certidão.

Sobre os requisitos, é correto afirmar que
a) todos são funcionais.

b) todos são não funcionais.

c) 1, 5 e 7 são não funcionais.

d) apenas 3, 4, 8, 9 e 10 são funcionais.

e) apenas 2, 6 e 7 são não funcionais.

Comentários: Requisitos Funcionais (RF): 2,3, 4, 6, 8, 9,10; e Requisitos Não-Funcionais (RNF): 1,
5 e 7 (Letra C).

(STJ - 2018) Os requisitos funcionais especificam o que o software deverá fazer. Esses
requisitos incluem tempo de resposta, utilização de volumetria estática,
escalabilidade,
disponibilidade, segurança e usabilidade.

Comentários: a primeira parte da questão está perfeita! No entanto, são os requisitos
não-funcionais que incluem tempo de
resposta, utilização de volumetria estática, escalabilidade, disponibilidade, segurança e
usabilidade (Errado).


Classificação quanto à origem

INCIDÊNCIA EM PROVA: MÉDIA

Agora vamos partir para outra classificação um pouquinho menos importante, mas que -
vez ou
outra - cai em prova! Pesquisadores observaram que os requisitos não-funcionais
também
podiam ser agrupados por meio de suas características comuns. Para tanto,
criou-se a
subclassificação dos requisitos não-funcionais em: requisitos de produto, requisitos
organizacionais
e requisitos externos.

Requisitos de Produto: especificam o comportamento do produto. Entre os
exemplos, estão
requisitos de desempenho quanto à rapidez com que o sistema deve operar e
quanto de
memória ele requer, requisitos de confiabilidade que definem a taxa aceitável
de falhas,
requisitos de portabilidade e requisitos de usabilidade.

Requisitos Organizacionais: são derivados de políticas e procedimentos da
organização do
cliente e do desenvolvedor. Entre os exemplos, estão padrões de processo que
devem ser
usados, linguagem de programação ou o método de projeto usado, e requisitos de entrega
que
especificam quando o produto e a sua documentação devem ser entregues.

Requisitos Externos: abrange todos os requisitos derivados de fatores externos ao
sistema e
seu processo de desenvolvimento. Entre os exemplos, estão a interoperabilidade
que define
como o sistema interage com outros sistemas, requisitos legais que devem ser
seguidos,
requisitos éticos sistema para assegurar que ele será aceito portodos.

IMPORTANTE

A INTEROPERABILIDADE É UM REQUISITO DE PRODUTO, ORGANIZACIONAL OU EXTERNO? ESTOU CITANDO
ESSA FUNCIONA DADE
ESPECÍFICA, PORQUE JÁ VI DIVERSAS PESSOAS PENSANDO QUE É DE PRODUTO. NA VERDADE, ELA
É UM REQUISITO EXTERNO,
PORQUE DEPENDE DE PADRONIZAÇÕES FORA DE SEU CONTROLE.

Acabaram as classificações, professor? Infelizmente, não! Cada uma dessas três
subclassificações
se divide também em várias outras, como mostra a imagem seguinte. Cabe salientar que
essa
classificação está em conformidade com a ga Edição do livro do lan
Sommerville, em que há
pequenas diferenças quanto à mesma imagem de edições anteriores. Vamos lá...

REQUISITOS EXEMPLOS


REQUISITOS DE
CONFIABILIDADE
REQUISITOS DE

PROTEÇÃO

REQUISITOS DE
DESEMPENHO

O sistema não deve ficar fora do ar por mais de cinco segundos durante o dia.

O sistema não deve permitirque os usuários modifiquem senhas de acesso que eles não criaram.

O sistema deverá ser capaz de processar oitocentas requisições por segundo.


(MPE/MA - 2013) O escopo de um projeto é determinado pelo levantamento de
requisitos funcionais e não funcionais. Dentre os requisitos não funcionais se enquadram
os requisitos organizacionais, que podem ser divididos em:

a) reguladores e éticos.

b) ambientais, operacionais e de desenvolvimento.

c) contábeis e de segurança.

d) de desempenho e de espaço.

e) de eficiência, de confiança e de proteção.

Comentários: os requisitos organizacionais se dividem em ambientais, operacionais e de
implementação (ou desenvolvimento)
(Letra B).


Engenharia de Requisitos

INCIDÊNCIA EM PROVA: ALTÍSSIMA

Vamos começar pelo histórico! O termo engenharia de software foi utilizado pela
primeira vez
na década de 70 em um relatório técnico da TRW Inc., mas não chegou a se tornar um
jargão.
Ele só ficou de fato mais conhecido na década de noventa com a publicação de um
tutorial da IEEE
e a criação de uma série de conferências sobre esse assunto. Ok, professor... mas
qual é a definição
de Engenharia de Requisitos?

Bem, ela pode ser definida como uma abordagem sistemática para a formulação,
análise,
documentação e manutenção de requisitos de um sistema. Em outras palavras,
também
podemos defini-la como um processo formal que engloba todas as atividades que
contribuem para
a produção de um documento de requisitos. Vocês percebem que são duas
visões um pouco
diferentes de engenharia de requisitos, mas que elas possuem um detalhe em comum. Qual é?

/\ primeira trata de uma abordagem sistemática e a segunda trata de um processo
formal. Pessoal,
porque essas são as palavras-chave da definição? Porque sempre que a palavra engenharia
aparece,
você já pode considerar que se trata de uma abordagem ou processo formal e
sistemático. Então
se uma prova discursiva te pergunta o que é Engenharia de Requisitos, você já sabe
que se trata de
algo formal, metodológico, sistemático, processual, repetível, etc.

Vou provar para vocês! O que é a Engenharia Civil? É o processo formal para
concepção, projeto,
construção e manutenção de diversas infraestruturas. A Engenharia Mecânica é o processo
formal
para a concepção, análise, fabricação e manutenção de sistemas mecânicos. Logo, qual é
a definição
de Engenharia de Software? É o processo formal para o levantamento, análise,
especificação,
validação, gerenciamento e manutenção de requisitos.

E o que essas definições querem dizer com "processo formal"? Elas querem dizer que se trata de uma
sequência de passos repetíveis e documentados de modo que seja possível construir um
carro no
México ou na Holanda que o resultado será semelhante. Vindo para o mundo da
engenharia de
requisitos, isso significa que duas empresas diferentes podem levantar os requisitos de
um sistema
de software que provavelmente obterão resultados semelhantes.

Galera, qual é a importância da engenharia de requisitos? Bem, essa é a fase mais
crítica no
desenvolvimento de um software, tendo em vista que erros durante esse estágio
conduzem
inevitavelmente a problemas posteriores no projeto e na implementação do sistema.
Professor, isso
não é simples de resolver? Basta eu contratar um bom engenheiro de requisitos, ele
vai até a
organização, levanta os requisitos corretos e fim - problema resolvido.

Galera, quem dera se fosse assim... a verdade é que tudo bem mais complicado do que parece.
Por essa razão, nós temos a disciplina de engenharia de requisitos: para que ela nos
oriente sobre
como formular, elicitar, analisar, documentar, manutenir e gerir os requisitos de um sistema de
software. Quem já trabalhou com isso sabe que às vezes o usuário pede uma coisa, mas
na verdade
ele quer outra coisa completamente diferente do que ele disse.

Sim, pessoal! Há usuários que não sabem expressar muito bem em palavras o que ele
deseja.
Em outras ocasiões, um mesmo usuário pede dois requisitos totalmente
contraditórios sem
perceber. Há também o conflito de requisitos entre usuários diferentes de uma mesma
empresa,
uma vez que - em uma organização - podem existir diferentes visões sobre um mesmo
produto de
software. Galera, rola umas tretas sinistras por conta disso...

Acontece também de a organização não ter um processo de trabalho muito maduro e
implantado
causando problemas sérios no levantamento de requisitos, uma vez que os
requisitos acabam
sendo modificados durante o próprio levantamento ou a especificação dos
requisitos. Então, a
engenharia de requisitos nos traz ferramentas e técnicas para ajudara mitigar esses
problemas,
mas tenham certeza: mesmo com tudo que isso, ela não consegue resolver todos os problemas.

Por outro lado, um sólido processo de engenharia de requisitos é capaz de encontrar a
melhor
solução viável no momento. Na prática, é praticamente impossível satisfazer
absolutamente
todas as expectativas dos clientes, na medida em que requisitos podem ser bastante
complexos e
voláteis. Lembrem-se que requisitos são entidades vivas que vão mudando o
tempo todo por
diversos motivos - a engenharia de requisitos faz o melhor que ela pode!

Na prática, os requisitos de sistema se modificam. Isso ocorre, porque as
pessoas envolvidas desenvolvem uma compreensão maiordo que desejam
que o software faça; a própria organização que está comprando o sistema
muda; modificações são feitas no hardware, software e no ambiente
organizacional do sistema; entre outros.

O Engenheiro de Software da IBM, Fred Brooks, diz: "A parte mais árdua
na construção de um sistema de software consiste em decidir o que construir!
Nenhuma outra fase do processo de desenvolvimento compromete tanto o
resultado finai do sistema se feita errada e nenhuma outra dificulta tanto as
correções posteriores".

SEGUNDO MIRANDA (2002 APUD SANTOS, 2007, P.12):

50% dos principais defeitos de software são oriundos da fase de especificação de software.
12% das principais causas de fracassos em projetos são oriundos de requisitos incompletos.
12% das principais causas de sucesso em projetos são oriundos de requisitos consistentes.

De modo geral, a engenharia de requisitos fornece um mecanismo adequado para
compreender o
que o cliente deseja, para analisar as suas necessidades, para
avaliar a viabilidade da
implementação, para negociar uma solução razoável com os usuários, para especificar uma
solução
não-ambígua, para validar a especificação e para gerenciar os requisitos à medida que
eles são
transformados em um sistema operacionalizável.


Enfim, chegamos à nossa última pergunta! Quais são as fases do processo de
Engenharia de
Requisitos? Bem, há duas respostas para essa pergunta! Como assim, professor? É que há
uma
divergência entre os principais autores. Nós vamos nos aprofundar nas fases
do Sommerville,
porque ele é o autor mais cobrado em provas nesse quesito, porém não custa nada ver
também
as fases do Pressman abaixo:

FASES | DESCRIÇÃO

Após uma necessidade de o negócio ser identificada, busca-se estabelecer um entendimento


CONCEPÇÃO

LEVANTAMENTO

ELABORAÇÃO

NEGOCIAÇÃO

básico do problema. Trata-se da concepção inicial do software e busca entender o problema,
quem são os envolvidos, a natureza da solução e iniciar o processo de comunicação
entre
clientes e colaboradores.

Etapa crítica, utiliza uma abordagem organizada para descobrir o que o cliente deseja em seu
sistema. Envolve intensa participação do stakeholders e faz três perguntas: Qual o objetivo do
produto? Como o produto se enquadra nas necessidades do negócio? Como o produto será
utilizado?

Por vezes chamada Análise, informações obtidas do cliente durante a concepção
e
levantamento são expandidas e refinadas em um modelo, definindo o domínio do problema.
Incluem-se modelagens de cenários de interação do usuário com o sistema e modelagens das
classes envolvidas.

Tem por objetivo chegar a um consenso sobre os conflitos entre clientes e usuários,
por
intermédio de um processo de negociação. Os requisitos são avaliados junto ao cliente e podem
se combinar, excluir ou até mesmo inserir novos requisitos.

ESPECIFICAÇÃO Por vezes chamada Documentação, produto final do engenheiro de
requisitos, pode ser um
documento escrito, um modelo gráfico, cenários de uso, protótipos, etc. Trata-se da
apresentação formal dos dados obtidos até o momento de modo que possa guiar
o
desenvolvimento futuro do software.

Os produtos de trabalho resultantes da engenharia de requisitos são avaliados quanto a s
qualidade por todos os envolvidos (clientes, colaboradores e usuários). Buscam-se erros
interpretação, ambiguidades e omissões.

conjunto de atividades que auxiliam a equipe de projeto a identificar, controlar e
requisitos e mudanças nos requisitos a qualquer momento . Para projetos de grande porte, é
uma fase essencial na medida em que mudanças em um requisito podem afetar diversos outn
requisitos.

Em resumo: na fase de concepção, tenta-se entender o problema a ser resolvido e
cria-se uma uma
concepção do software que resolverá esse problema; na fase de levantamento de
requisitos, busca-
se descobrir os requisitos que sistema terá; na fase de elaboração, também chamada de
análise de
requisitos, busca-se expandir e refinar esses requisitos - adicionando mais detalhes; na
fase de
negociação, busca-se um consenso sobre requisitos contraditórios, diferentes, etc.

Já na fase de especificação de requisitos, também chamada de documentação de
requisitos, cria-se o
documento de requisitos; na fase de validação de requisitos, realiza-se uma revisão do
documento
de requisitos e avalia-se a sua qualidade; e, porfim, na fase de gestão, busca-se
manter um controle
e rastreabilidade dos requisitos do sistema de software. Se vocês compreenderam
tudo isso,
podemos seguir para as fases de acordo com o Sommerville!

POR SOMMERVILLE | PORPRESSMAN

ESTUDO DE VIABILIDADE CONCEPÇÃO
ELICITAÇÃO E ANÁLISE DE REQUISITOS LEVANTAMENTO

ELABORAÇÃO

Obtenção de Requisitos
Classificação e Organização

Priorização e Negociação NEGOCIAÇÃO
Documentação de Requisitos
tbrtCIrlCAçAU
VALIDAÇÃO

tcbcrDtCcrIriIrCirAçrÃAnU
VALIDAÇÃO

GESTÃO GESTÃO

Na tabela acima, podemos ver uma tabela comparativa entre as fases de acordo com cada
autor.
Como decorar, professor? Bem, chegou a hora de eu ganhar alguns inimigos! Quando eu
estudava
esse assunto, eu criei mnemónicos para decorar as fases de cada autor. Eu já levei
um sapo de um
aluno no fórum de dúvidas por usar o Vasco como exemplo - Vascaínos, peço que não
se sintam
ofendidos. Mnemónicos devem ser absurdos mesmo para ajudar na memorização, ok?


Onefootball

Alexandre Fernandes * 10 de out de 2019

Cenas lamentáveis em
novo empate do Vasco da
Gama

FASES DE ACORDO COM IAN SOMMERVILLE

FASES DE ACORDO COM ROGER PRESSMAN

ENAS AMENTÁVEIS M OVO MPATEDO ASCO DA AMA

ONCEPÇÃO> EVANTAMENTO > LABORAÇÃO > EGOCIAÇÃO > SPECIFICAÇÃO > ALIDAÇÃO > ESTÃO

A imagem a seguir apresenta graficamente as fases da Engenharia de Requisitos de acordo com
Sommerville. São elas: Estudo de Viabilidade, Elicitação e Análise de Requisitos,
Especificação de
Requisitos e Validação de Requisitos. Por fim, há uma última fase que não está
representada na
imagem, mas que envolve e suporta todas as fases anteriores e também é de suma
importância:
Gestão/Gerenciamento de Requisitos.

Sommerville afirma que o objetivo da engenharia de requisitos é criar e manter um
documento
de requisitos de sistema. Assim, note que o resultado do Estudo de Viabilidade é o
Relatório de
Viabilidade; o resultado da Elicitação e Análise de Requisitos é um conjunto de
Modelos do Sistema;
o resultado da Especificação de Requisitos são os Requisitos de Usuário e de Sistema; e o resultado
da
Validação de Requisitos é o famoso Documento de Requisitos.


Todos esses artefatos servem de insumo para construir o Documento de Requisitos! Além disso,
percebam que as setas vão e voltam entre as fases. Então, no momento de validar os
requisitos, por
exemplo, se eu encontrar algo incorreto, eu posso retornar à Especificação de
Requisitos. Bacana?
Então, agora é o momento de entrar em mais detalhes sobre cada uma dessas fases que
nós
acabamos de ver. Vem comigo...


Estudo de Viabilidade

A fase de Estudo de Viabilidade trata da realização de uma avaliação relativamente
rápida e barata
para verificar se as necessidades identificadas dos usuários podem ser satisfeitas por
meio das
tecnologias atuais de sistemas de software e hardware. O resultado dessa avaliação deve
fornecer
informações para que a alta direção da organização tome uma decisão mais embasada
quanto
a prosseguir para uma análise mais detalhada ou não.

Esse é o momento de fazer diversos questionamentos importantes: o sistema
realmente
agregará valor ao negócio? Ele será útil para a empresa? Ele será rentável? Qual é o
retorno de
investimento que ele será capaz de realizar? É viável tecnologicamente e
financeiramente? Imaginem
um sistema de software que automatiza algum processo de negócio de uma organização,
mas que
custa R$10 milhões para implementar e economiza apenas R$5.ooo/mês.

De uma outra forma, pode ser descrita como atividade inicial do processo de
engenharia de
requisitos, consistindo em um conjunto preliminar de requisitos de negócio, um
esboço da
descrição do sistema e da forma como o sistema pretende apoiar os processos de
negócios da
organização. A fase seguinte utiliza as informações do estudo de viabilidade como base
para o
levantamento de requisitos.

Além disso, ele deve ser um estudo curto, bem focado e
preferencialmente barato, devendo ser realizado no início do
processo de engenharia de requisitos e, ao final, deverá
entregar um relatório de viabilidade. Por que? Porque se você
perder muito tempo desenvolvendo o estudo ou se ele for caro
demais, pode acabar não valendo a pena sequer fazê-lo. Com
o resultado do estudo em mãos, a alta direção pode dar o
famoso go/no-go {vamos ou não vamos seguir?).

Por fim, o Estudo de Viabilidade deve responder três questões em que - caso alguma
delas tenha
uma resposta negativa - o projeto não deve seguir adiante. São elas:

Item. 1. O sistema contribui para os objetivos gerais da organização?

Item. 2. O sistema pode ser implementado com tecnologia atual e dentro do custo e prazo?

Item. 3. O sistema pode ser integrado a outros sistemas já implantados?

As respostas para essas três questões não é algo tão simples de ser
obtido, visto que
geralmente a empresa não tem a exata definição de seus objetivos. Para ajudar nesta
definição,
questões podem ser levantadas às partes interessadas e, com as respostas em mãos,
pode-se
concluir se o desenvolvimento do sistema deve prosseguir ou não; pode-se propor
alterações de
escopo, orçamento, prazo; etc. Segue uma lista de questionamentos possíveis:

Item. 1. Se o sistema não fosse implementado, qual seria o rumo da organização?

Item. 2. Quais são as falhas dos processos atuais e quais soluções o novo sistema traria?


Item. 3. Quanto aos objetivos e requisitos, qual a contribuição direta do novo sistema?

Item. 4. Existe a possibilidade de integração com outros sistemas?

Item. 5. Quais das tecnologias serão novas?

Item. 6. O que o novo sistema irá apoiar?

(FUB - 2011) O estudo de viabilidade, uma atividade inicial do processo de engenharia
de requisitos, consiste em um conjunto preliminar de requisitos de negócio, um esboço
da descrição do sistema e da forma como o sistema pretende apoiar os processos de
negócios.

Comentários: em todos os sistemas novos, o processo de engenharia de requisitos deve começar com um
estudo de viabilidade.
A entrada para o estudo de viabilidade consiste em um conjunto preliminar de requisitos de
negócios, um esboço da descrição
do sistema e como o sistema pretende apoiar os processos de negócios (Correto).

(CHESF - 2012) O processo de engenharia de requisitos engloba todas as atividades
necessárias para criar e manter um documento de requisitos do sistema e compreender
os elementos de negócio que serão atendidos pelo software a ser desenvolvido,
pertencendo a uma sequência lógica de atividades que culminam em um documento de
requisitos correto que inclui todas as necessidades do cliente.

O primeiro passo necessário no processo de criação desse documento de requisitos deve
sera(o):

a) análise de viabilidade
b) prototipagem do sistema
c) geração de casos de teste
d) design da aplicação
e) documento de gerenciamento de mudanças

Comentários: em todos os sistemas novos, o processo de engenharia de requisitos deve começar com um
estudo de viabilidade
(Letra A).


Elicitação e Análise de Requisitos

O verbo Elicitar não é muito utilizado em nosso cotidiano, mas significa o mesmo que descobrir,
identificar, deduzir, extrair, evocar, obter informações sobre uma questão específica.
Para tal,
os engenheiros de software trabalham com os clientes e usuários finais do sistema para
aprender
sobre o domínio da aplicação, quais serviços o sistema deve fornecer, o desempenho
esperado,
restrições de hardware, entre outros quesitos.

A fase de Elicitação e Análise de Requisitos trata do processo de levantamento e
derivação de
requisitos de sistema através da observação de sistemas existentes, discussões com
usuários e
compradores potenciais, análise de tarefas, entre outros. Isso pode envolver o
desenvolvimento de
um ou mais modelos de sistema e protótipos, que ajudam o analista a compreender o
sistema a ser
especificado.


Como o cliente
explicou

Como o lider de
projeto entendeu

Como o analista
planejou

Como o programador
codificou

Como o consultor de
negocios descreveu


Valor que o cliente
pagou

Como o projeto foi
documentado

O que a assistência
técnica instalou

Como foi suportado Quando foi entregue O que o cliente
realmente
necessitava

Pessoal, porque é tão difícil levantar requisitos? Nós já discutimos um pouco sobre
isso, mas agora
nós vamos ver em detalhes. A imagem acima é uma das figuras mais clássicas da
engenharia de
software. O que ela quer dizer? É o seguinte: o cliente explica uma coisa, o líder
de projeto entende
outra, o analista planeja outra, o programador codifica outra, os beta
testers testam outra e o
consultor de negócios descreve outra também totalmente diferente.

Não acabou! Aí o cliente acaba pagando muito mais caro do que devia, o projeto não
é bem
documentado, a assistência técnica instala errado, não há suporte, demora mais que o programado
e, no fim, já estamos em outra estação do ano quando o sistema é entregue. Observem
no último
quadrinho que o cliente também não descreveu bem o que ele queria - e é por isso
que a
engenharia de requisitos e suas técnicas são tão importantes.

Galera, quem já trabalhou com isso sabe! Às vezes, os
próprios clientes não sabem o que querem; às vezes, eles
querem automatizar um processo que ainda não está
efetivamente maduro; às vezes, eles esquecem de
mencionar um requisito bastante importante porque para
eles era óbvio para a área de tecnologia não era. Enfim...
a engenharia de requisitos está aqui para nos ajudar a
descobrir requisitos implícitos, contraditórios,
inconsistentes, incompletos, entre outros.

As principais atividades do processo de elicitação e análise de requisitos são:

a. Obtenção de Requisitos: processo de interação com os stakeholders para coletar
requisitos. Os
requisitos de domínio também são descobertos durante essa atividade.

b. Classificação e organização de requisitos: esta atividade envolve a coleção de
requisitos não
estruturados, agrupa os requisitos relacionados e os organiza em conjuntos coerentes.

cr Priorização e negociação de requisitos: inevitavelmente, os requisitos serão
conflitantes.

Assim, busca-se priorizar os requisitos e resolver conflitos por meio da negociação.

d. Documentação de requisitos: os requisitos são documentados e colocados na próxima
volta da
espiral. Podem ser produzidos documentos de requisitos formais ou informais.


Em suma: (1) Obtenção/Descoberta de Requisitos - atividade de interação com
as partes
interessadas justamente para obter, descobrir e coletar os requisitos do sistema; (2)
Classificação
e Organização de Requisitos - momento de organizar os requisitos - eventualmente existe
mais
de um engenheiro de requisitos trabalhando em áreas diferentes de uma organização e,
ao fim, eles
apresentam seus requisitos, logo é preciso organizá-los.

Vocês se lembram que nós vimos várias classificações de requisitos? Pois é, os
engenheiros de
requisitos podem decidir classificá-los em requisitos funcionais ou não
funcionais, em requisitos
permanentes ou voláteis, em requisitos normais, esperados ou fascinantes, em
requisitos de
usuário ou de sistema, entre outras classificações. O importante é classificar
os requisitos,
agrupá-los de acordo com algum critério e organizá-los em conjuntos que façam sentido.

Além disso, nessa atividade serão realizadas algumas verificações
preliminares de conflito,
consistência, omissão e ambiguidade de requisitos. (3) Priorização e Negociação de
Requisitos -
como eu mencionei, são vários engenheiros de requisitos levantando requisitos com várias
pessoas
diferentes de uma organização e essas pessoas podem ter visões diferentes do produto,
então é
comum que os requisitos acabem entrando em conflito.

Essa atividade busca consolidar as visões diferentes dos clientes em uma reunião e
fazer com
que elas conversem e cheguem a um consenso sobre os requisitos. Então, esse é o momento de
priorizar alguns requisitos em detrimento de outros e também de negociar para
chegar a um
acordo. Bacana? Saibam - de antemão - que é impossível satisfazer todos os
stakeholders. Logo,
não tem jeito, sempre haverá alguém insatisfeito.

(4) Documentação de Requisitos - trata-se da atividade de organizar os
requisitos em um
documento de maneira organizada, classificada, priorizada e negociada. Essa documentação
é uma
documentação para os engenheiros de requisitos e, não, para clientes e stakeholders.
Bem, a fase
de elicitação e análise de requisitos é campeã em frequência nas provas, principalmente
a atividade
de descoberta.

(TRT/19 - 2011) De acordo com Sommerville, são atividades do processo de elicitação
de requisitos, pela ordem:

a) casos de uso; análise; projeto; arquitetura.

b) etnografia; casos de uso; análise; validação; arquitetura.

c) entrevista; etnografia; documentação; registro.

d) cenários; classificação; organização; priorização; documentação.

e) obtenção; classificação e organização; priorização e negociação; documentação

Comentários: trata-se da obtenção, classificação e organização, priorização e negociação, e
documentação (Letra E).

Para auxiliar a assegurar uma cobertura ampla dos requisitos de um sistema de
software,

utilizam-se as seguintes técnicas (as sublinhadas são as que caem mais em prova):


í. Entrevistas

Entrevistas formais ou informais com os stakeholders do sistema fazem parte
da maioria dos
processos de engenharia de requisitos. Nessas entrevistas, a equipe de engenharia de
requisitos
formula questões para os stakeholders sobre o sistema que eles usam e o
sistema a ser
desenvolvido. Os requisitos são derivados a partir das respostas dessas questões. As
entrevistas
podem ser abertas ou fechadas.

As entrevistas abertas ocorrem quando não há um roteiro predefinido e as entrevistas
fechadas
ocorrem quando há um roteiro predefinido. Na prática, as entrevistas com os
stakeholders são,
geralmente, uma combinação desses tipos. As respostas a algumas perguntas podem levar a
outros assuntos discutidos de maneira menos estruturada. As discussões completamente
abertas
raramente funcionam bem.

Em regra, a maioria das entrevistas requeralgumas perguntas como ponto de partida e
para manter
o foco no sistema a ser desenvolvido. As entrevistas são úteis para obter um
entendimento geral
sobre o que os stakeholders fazem, como eles podem interagir com o sistema e as dificuldades
que enfrentam com os sistemas atuais. As pessoas gostam de falar sobre seu
trabalho e,
normalmente, ficam felizes em participar de entrevistas.

No entanto, as entrevistas não são tão úteis para compreender os requisitos
do domínio da
aplicação. Não é eficiente para elicitação de conhecimentos sobre os requisitos
e as restrições
organizacionais, pois existem relacionamentos sutis de poder e influência entre
os stakeholders.
Em geral, a maioria das pessoas é relutante em discutir questões políticas e organizacionais que
podem afetar os requisitos.

Por fim, existem três tipos de Entrevistas Formais: Pirâmide, Funil e Diamante. A
primeira
começa com perguntas mais detalhadas e termina com questões mais genéricas; a
segunda
começa com perguntas mais genéricas e termina com perguntas mais detalhadas; e a
terceira que
é mescla de ambos -começa com perguntas mais detalhadas, depois são feitas perguntas
mais
genéricas e termina com perguntas mais detalhadas novamente.

Item. 2. Etnografia

Técnica de observação utilizada para compreender os requisitos organizacionais e sociais.
Coloca-se o analista dentro do campo de atuação dos usuários, observando o
trabalho diário
anotando as tarefas reais em que os participantes estão envolvidos. Em geral, essa é
uma técnica
utilizada em conjunto com outras técnicas. Como ela é uma técnica de observação,
isoladamente
ela não é muito eficaz na elicitação.

O valor da técnica de etnografia está na ajuda que presta aos analistas em descobrir
os requisitos
implícitos de sistema que refletem os processos reais, e não os processos formais, com
os quais as
pessoas estão realmente envolvidas. As pessoas frequentemente consideram muito difícil
articular detalhes de seu trabalho rotineiro, visto que muitos passos são
secundários e
irrelevantes para elas.

É claro que elas compreendem seu próprio trabalho, mas podem não compreender
seu
relacionamento com o trabalho de outros na organização. Os fatores sociais e
organizacionais,
que afetam o trabalho, mas que não são claros e óbvios para as pessoas, podem
somente se tornar
claros quando examinados por um observador imparcial - por isso, a etnografia é importante!

Item. 3. Cenários

As pessoas geralmente consideram mais fácil relatar exemplos da vida real do
que abstrair
descrições. Elas podem compreender e criticar um cenário de como interagiriam
com um
sistema de software. Os engenheiros de requisitos podem usar as informações
obtidas nessa
discussão para elaborar os requisitos reais do sistema de software. Os
cenários podem ser
particularmente úteis para adicionar detalhes a um esboço da descrição de requisitos.

Eles são descrições de exemplos das sessões de interação. Cada cenário abrange uma ou
mais
interações possíveis. Diversos tipos de cenários foram desenvolvidos, cada
um dos quais
fornecendo diferentes tipos de informações sobre o sistema em diferentes níveis de
detalhamento.
O uso de cenários para descrever requisitos é parte integrante dos métodos ágeis, como
a
Extreme Programming.

O cenário começa com um esboço da interação e, durante a elicitação, os detalhes são
adicionados
para criar uma descrição completa dessa interação. A elicitação baseada em cenários
pode ser
realizada também de informalmente. Os engenheiros de requisitos trabalham com os
stakeholders
para identificar cenários e captar seus detalhes em forma de textos, diagramas,
imagens, eventos,
casos de uso, etc.

Item. 4. Questionários

Formulários distribuídos aos stakeholders com questões pré-definidas. Torna-se útil quando
a
quantidade de stakeholders é muito grande. Tem baixo custo, é fácil de aplicar, pode
atingir
várias pessoas, demanda menos tempo e fornece rápido feedback. No entanto, há uma
tonelada
de problemas, como falta de interação, perguntas pouco objetivas, difícil
compreensão das
perguntas, entre outros.

Diferentemente da entrevista, essa técnica é interessante quando temos uma
quantidade
muito grande de pessoas para extrair as mesmas informações, que não seria viável por meio de
entrevistas individuais. As questões são dirigidas por escrito aos participantes com o
objetivo de
ter conhecimento sobre opiniões das mesmas questões - são autoaplicáveis, pois
o próprio
informante responde.

Item. 5. Workshop de Requisitos


Reunião estruturada e intensiva entre analistas e usuários com o intuito de obter um
conjunto
de requisitos bem definidos. Possui um faciIitador neutro responsável pelas atividades
de logística
e promoção de momentos de descontração, como forma de dinamizar o trabalho
em equipe.
Permite utilizar outras técnicas em conjunto como brainstorming ou interpretação de papéis.

Devem fazer parte do grupo uma equipe de analistas e uma seleção/amostra dos
stakeholders que
melhor representam a organização e o contexto em que o sistema será utilizado, obtendo
assim
um conjunto de requisitos bem definidos. Por ser realizado por convocação por dia e
horário,
pode ocasionar problemas por conta da presença física dos stakeholders, mas isso tem
mudado
pós-pandemia.

Item. 6. Brainstorming (Tempestade de Ideias)

É uma abordagem de elicitação ocorrida em grupo em ambientes informais durante cerca
de 15
minutos em que toda a ideia deve ser levada em consideração, sendo proibida a crítica
a qualquer
sugestão dada, e encorajada, inclusive, a criação de ideias que pareçam estranhas ou
exóticas.
Busca-se explorar a potencialidade criativa de um grupo - um facilitador organiza e
prioriza os
resultados.

Dentre suas vantagens, podemos afirmar que várias pessoas pensam melhor do que uma.
Além
disso, a técnica de tempestade de ideias democratiza a participação de membros do
grupo.
Uma pequena desvantagem é que ela depende da disponibilidade dos integrantes.
O
brainstorming muitas vezes é utilizado em conjunto com outras técnicas, tais como
workshops de
requisitos.

Item. 7. Leitura de Documentos

A técnica de leitura de documentos é responsável por coletar informações que são
geralmente
mais difíceis de se obter por meio de entrevistas, questionários e observações sociais,
como -
por exemplo - histórico da organização, cultura e hábitos internos,
relacionamentos setoriais,
informações financeiras e direcionamentos futuros. São muito utilizadas no
contexto de sistemas
legados.

Estudo e reutilização de documentação de diferentes naturezas, para a
identificação de
requisitos a serem implementados no sistema que se está modelando, podem ser utilizados.
Uma grande variedade de documentação pode ser analisada incluindo estrutura
organizacional da
empresa, padrões de mercado, leis, manuais de usuário, relatório de pesquisas
de mercado,
glossário de termos de negócio, etc.

Item. 8. JAD (Joint Application Design)

Similar à técnica de workshop de requisitos e registrada pela IBM, ela busca reunir
os usuários e
desenvolvedores em um workshop estruturado para levantar requisitos e promover a tomada
de
decisões por meio de diversos tipos de dinâmicas de grupo, técnicas visuais, processos racionais e
até documentação. É bastante interativa e promove a participação ativa dos
envolvidos -
inclusive dos tímidos.

O processo consiste em três fases principais: customização, sessões e
agrupamento. Na
customização, o analista prepara as tarefas para as sessões como organizar os times,
preparar o
material, entre outros. Na fase de sessões, o analista marca uma ou mais reuniões com
os
stakeholders. No início da sessão, o engenheiro de requisitos provê uma visão genérica
sobre o
sistema.

A discussão com os stakeholders continua até o fim do levantamento de requisitos. Na
fase de
agrupamento todos os requisitos levantados nas fases anteriores são convertidos
em
documentos de especificação de requisitos. As discussões que ocorrem na fase de sessões
são
altamente produtivas, porque resolvem dificuldades entre as partes enquanto
se dá o
desenvolvimento do sistema para a empresa.

Item. 9. Prototipação

Técnica de elicitação, independente de tecnologia, utilizada no estágio inicial
do projeto,
ajudando stakeholders a desenvolverem uma forte noção sobre a aplicação
a ser
implementada. Por meio da visualização de um esboço da aplicação, podem-se
identificar
requisitos reais e fluxos de trabalho do sistema. São frequentemente utilizadas quando
os usuários
são incapazes de expressar suas necessidades.

Permite alcançar um feedback antecipado dos stakeholders e reduzir o tempo e
o custo de
desenvolvimento devido a detecção dos erros em uma fase inicial do projeto. Ela
fornece também
alto nível de satisfação dos usuários devido a sensação de segurança ao ver algo
próximo do
real. No entanto, há um alto custo de investimento em relação a outra técnicas estudadas.

Item. 10. Reúso de Requisitos

O reuso de requisitos trata do estudo e reutilização de especificações e glossários
referentes a
projetos de sistemas legados ou sistemas de mesma família ou com funcionalidades de
negócio
similares. Estudos mostram que sistemas similares podem reutilizar mais de 80%
de seus
requisitos. Dessa forma, eles têm chances maiores de serem compreendidos pelos
stakeholders -
o que é uma excelente vantagem.

Além disso, essa técnica economiza tempo e dinheiro! Estudos têm mostrado que
sistemas
similares podem reutilizar acima de 80% de seus requisitos. Pode levartambém a uma
reutilização
adicional de outros itens em outras atividades do ciclo de vida de desenvolvimento.
Além disso,
reduz riscos, visto que requisitos reutilizados têm uma chance maior de serem
compreendidos
pelos stakeholders.

Item. 11. Histórias de Usuários


Introduzida inicialmente pela Metodologia XP (Extreme Programming'), nada mais é do que
uma
história contada na linguagem do usuário final, que deve ser capaz de capturar aquilo
que o usuário
de fato necessita fazer para realizar seu trabalho. Deve ser concisa o suficiente para
caber em um
post-it. Um padrão seria: "Como um <papel>, eu quero <meta> de modo que <benefício>".
Vamos
supor que você está planejando uma viagem de férias.

Você tem em mente alguns lugares que gostaria de visitar, atividades que quer fazer e
uma ideia
geral de quanto tempo gostaria de ficar em cada lugar. A história do usuário é como se
fosse uma
dessas atividades específicas que você quer fazer em um determinado lugar, e que
contribuirá
para atingir o objetivo final da viagem. Por exemplo, se você estiver planejando uma
viagem para
a praia, uma história do usuário pode ser:

"COMO UM TURISTA, EU QUERO ALUGAR UM EQUIPAMENTO DE SNORKEL PARA PODER
EXPLORAR 0 FUNDO 00 MAR E TER UMA EXPERIÊNCIA ÚNICA"

Assim como na viagem, as histórias de usuário são pequenas partes do todo que ajudam
a alcançar
o objetivo final do projeto de software. Elas são detalhadas o
suficiente para que os
desenvolvedores possam entendê-las e implementá-las, mastambém sãoflexíveis o suficiente
para
permitir ajustes e mudanças à medida que o projeto avança. Essa é uma das técnicas
mais
utilizadas e mais cobradas em prova (apesar de ser bem mais cobrada no contexto de XP).

Item. 12. Participação Ativa de Usuários

A técnica de participação ativa de usuários permite a incorporação dos usuários e
clientes ao
grupo de engenharia de requisitos. Os usuários precisam aprenderas linguagens de
modelagem
utilizadas para ser capaz de ler as descrições e criticá-las. Permite uma interação
real entre clientes
e usuários, no entanto necessita de um certo treinamento aos usuários participantes.

Item. 13. Encenação

É uma abordagem que implica usar uma ferramenta para ilustrar para os usuários
(atores) como o
sistema se ajustará à organização e também indicar como ele se comportará.
Um facilitador
mostra uma encenação para o grupo e este último faz comentários. Ajuda a restringir
requisitos,
estimula soluções mais criativas e a revisão em equipe, facilita o processo de
entrevista, entre
outros.

Item. 14. Interpretação de Papeis

A técnica de interpretação de papeis é uma abordagem que atribui a cada membro do
grupo
um papel de interesse para o sistema. O grupo inspecionará então como o sistema é
usado. Ao
longo do caminho, haverá discussões sobre quem é responsável por o quê. O Analista de
Sistemas
interpreta o papel do usuário, o que o ajuda a obter um discernimento real do domínio do problema.


Item. 15. Grupo Focal

A técnica de grupo focal trata de um grupo de discussão informal e de
tamanho reduzido
(geralmente até 12 pessoas), com o propósito de obter informação qualitativa em
profundidade. As
pessoas são convidadas para participar da discussão sobre determinado assunto. Possui
baixo
custo, resposta rápida e flexibilidade, obtendo informações de qualidade em um curto prazo.

Ele é muito eficiente para esclarecer questões complexas no desenvolvimento de projetos.
Por
outro lado, exige facilitador/moderador com experiência para conduzir o grupo. Além
disso, essa
técnica não garante total anonimato - que é relevante em algumas ocasiões. Por fim,
ele depende
da seleção criteriosa dos participantes e as informações obtidas não podem ser generalizadas.

Item. 16. Análise de Protocolos

Essa técnica consiste em analisar o trabalho de determinada pessoa por meio de
verbalização,
estabelecendo a racionalidade utilizada na execução de tarefas. É feita por meio da
pergunta "O
que você faria se...?1' e, assim, possibilita elicitar fatos não facilmente
observáveis e permite melhor
entendimento dos fatos. Galera, funciona como um protocolo passo a passo.

Item. 17. Pontos de Vista (Viewpoint-Oriented Requirements Definition - VORD)

A técnica de pontos de vista (também chamada de VORD) considera as perspectivas de diversas
partes interessadas sobre os requisitos do sistema de software. Ela reconhece os pontos de
vista
dos stakeholders e fornece um framework para se tentar descobrir conflitos
nos requisitos
propostos por cada um deles. Eles podem ser de três tipos principais: interação,
indiretos e de
domínio.

Galera, é possível se aprofundar bastante em cada uma dessas técnicas. No entanto, eu
acredito
que dentro do contexto de Engenharia de Requisitos, basta saber uma breve
descrição.
Aprofundar-se em cada uma é inviável e pouco eficiente. Ademais, é possível aprender
mais dentro
do contexto em que são mais utilizadas (Ex: Histórias de Usuário, no contexto de
XP; Casos de Uso,
no contexto de UML; entre outros). Fechou? V


Especificação de Requisitos

Trata-se da atividade de traduzir as informações coletadas durante a atividade de
elicitação e
análise em um documento que define um conjunto de requisitos. No entanto, essa fase se
diferencia da documentação de requisitos da fase anterior - o objetivo lá
era criar uma
documentação preliminar dos requisitos que serviria apenas para os engenheiros de
requisitos; o
objetivo aqui é criar uma documentação que sirva como um contrato entre as partes.

Dessa forma, essa documentação deve servir tanto para engenheiros de requisitos quanto
para
os clientes. Esse documento contém requisitos de usuário e requisitos de sistema, logo
ambas as
partes podem consultá-lo de maneira sistemática para verificar o que foi levantado, a
análise de
viabilidade, os requisitos mais abstratos, os requisitos mais técnicos, o que foi
acordado entre as
partes, entre outros. Entendido?

Na parte de requisitos de usuário, o documento pode utilizar uma linguagem natural,
com tabelas
simples, diagramas ou imagens; na parte de requisitos de sistema, o documento
pode utilizar
modelos matemáticos formais, cenários de casos de uso, entre outras
técnicas. Galera,
idealmente, requisitos de usuário e sistema devem ser claros, não-ambíguos,
fáceis de
entender, completos e consistentes. Diego, porque idealmente?

Porque é praticamente impossível garantir que tudo será claro, que não haverá
nenhuma
ambiguidade, que todos que lerem entenderão facilmente, que será bastante completo e não
faltará nada, e que o documento não possui nenhuma inconsistência. Além disso, mesmo
que
encontremos um cliente que concordo com tudo isso sobre o documento, podemos
ter outro
cliente da mesma organização que tem uma opinião totalmente diferente.

Clientes podem interpretar requisitos de maneiras diferentes. Bacana? Agora, um detalhe:
essa não
é a fase responsável por verificar se os requisitos estão claros, não-ambíguos,
consistentes, fáceis
de entender, etc - ela busca apenas escrever um documento de requisitos de forma
clara, não-
ambígua, consistente, fáceis de entender, etc. Por outro lado, a fase
responsável por
efetivamente verificar esses atributos é a fase de Validação de Requisitos.

Vamos resumir? Essa é a fase que buscará escrever os requisitos em um Documento
de
Requisitos1. Idealmente, requisitos de usuário e sistema devem ser claros, não-ambíguos,
fáceis de
entender, completos e consistentes. Na prática, isso é extremamente difícil de se
atingir, na medida
em que as partes interessadas interpretam os requisitos de maneiras diferentes e,
frequentemente,
há conflitos e inconsistências.

Deve-se descrever os requisitos de usuário em linguagem mais simples,
especificando somente
características externas, evitando características do projeto de sistema. Já os
requisitos de sistemas

1 Esse artefato pode ser um documento escrito (Ex: Textos), um modelo
gráfico (Ex: Diagramas), um modelo matemático formal (Ex: Autômatos),
cenários de casos de uso (em geral, para sistemas menores).


são extensões dos requisitos de usuário e são usados como ponto de partida para o
projeto do
sistema. Eles adicionam detalhes e explicam como os requisitos do usuário
devem ser
fornecidos pelo sistema.

Por fim, essa fase gera o conjunto de requisitos que, na próxima fase, apenas será validada. Ele
apresenta uma visão do sistema e é bastante útil em diversas áreas de engenharia,
descrevendo as
funcionalidades de um sistema de software e suas limitações. Ademais, permite
detalhar as
informações de entrada e saída do sistema, de modo que se implemente uma arquitetura
confiável
do sistema.

(MPU - 2010) A especificação de requisitos permite, em determinado momento, revelar
o que o sistema irá realizar no que se refere às funcionalidades, sem definir, nesse
momento, como as funcionalidades serão implementadas.

Comentários: a especificação de requisitos busca criar o documento de requisitos e revelar apenas o
que sistema realizará, mas
não como ele o fará com detalhes de projeto, de tecnologias, etc (Correto).

(TCE/PR-2016- Letra A) O documento de especificação de requisitos é um documento
restrito à equipe de desenvolvimento de software.

Comentários: é um documento que serve tanto para a equipe de desenvolvimento de software quanto
para o cliente (Errado).

(TSE - 2011 - Item IV) Na especificação de requisitos, pode-se construir um documento
que descreva o sistema em termos gerais. Esse documento apresenta uma visão do
sistema e pode capturar as necessidades dos usuários.

Comentários: a especificação de requisitos realmente constrói um documento que descreve de forma
geral o sistema por meio
de uma visão sobre as necessidades dos usuários. A redação da questão peca um pouco
por utilizar "termos gerais", porque
pode dar a entender que se trata de um documento mais abstrato, sendo que o documento de
especificação de requisitos é um
documento que apresenta mais detalhes (Correto).


Validação de Requisitos

A atividade de Validação de Requisitos é responsável por verificar os requisitos em
relação ao
realismo, consistência, abrangência, validade, completude, etc. Durante esse
processo, erros no
documento de requisitos são inevitavelmente descobertos. Devem, então, ser feitas
modificações
para corrigir esses problemas. Também se busca demonstrar se os requisitos definem, de
fato,
o que o usuário deseja em seu sistema.

Este estágio é focado no cliente e está relacionado à descoberta de problemas com
requisitos.
A validação de requisitos é extremamente importante porque os erros em um
documento de
requisitos podem levar a custos excessivos de retrabalho quando são descobertos
durante o
desenvolvimento ou depois que o sistema está em operação. O custo de correção de um
problema
ocorrido na fase de requisitos é muito maiordo que aquele ocorrido na fase de projeto e
codificação.

A razão disso é que uma mudança de requisitos significa geralmente que o
projeto e a
implementação do sistema devem também ser mudados e o sistema deve ser
novamente
testado. Não se deve subestimar os problemas de validação de requisitos. É difícil
demonstrar que
um conjunto de requisitos atende às necessidades do usuário. Os usuários
devem imaginar o
sistema em operação e avaliar sua adequação ao trabalho.

É difícil para profissionais de informática habilidosos realizarem esse tipo de análise
abstrata e é
ainda mais difícil para os usuários do sistema. Como resultado, raramente encontram-se
todos os
problemas de requisitos durante o processo de validação. É inevitável que haja mudanças
de
requisitos posteriores para corrigir omissões e mal-entendidos depois da
aprovação do
documento de requisitos.

Enfim, uma série de técnicas de validação de requisitos pode ser usada, tais como:
Revisão de
Requisitos, Prototipação e Geração de Casos de Teste.

í. Revisão de Requisitos (Revisão Técnica):

Requisitos são analisados sistematicamente por uma equipe de revisores. Em revisões
informais, a
equipe pode simplesmente ter uma conversa, envolvendo o maior número
possível de
representantes dos stakeholders, acerca dos requisitos produzidos. Em revisões formais, a
equipe
de revisores deve confirmar junto do cliente um conjunto de critérios que todos os
requisitos
devem cumprir.

Em uma revisão formal de requisitos, a equipe de desenvolvimento deve 'conduzir' o
cliente
pelos requisitos de sistema, explicando as implicações de cada um dos requisitos. A
revisão
ocorre sob quais critérios, Diego? A equipe de revisão deve verificar cada requisito
em termos de
consistência (para evitar ambiguidade), bem como verificar os requisitos como um todo
em termos
de completeza.


Conflitos, contradições, erros e omissões nos requisitos devem ser apontados e
registrados
formalmente no relatório de revisão. É, portanto, de responsabilidade dos usuários, do
adquirente
do sistema e do desenvolvedor de sistema negociar uma solução para esses
problemas. Os
revisores podem verificar a facilidade de verificação e compreensão,
rastreabilidade e
adaptabilidade dos requisitos.

Neste planejamento, devem ser preparadas checklists genéricos de revisão que não deverão
incidir
sobre requisitos individuais, mas sobre as relações entre requisitos, assim como as
propriedades de
qualidade do documento. Os seguintes atributos devem ser levados em
consideração:
Compreensibilidade; Redundância; Completude; Consistência; Organização; Conformidade; e
Rastreabilidade.

ATRIBUTOS | DESCRIÇÃO

VALIDADE Examina se as partes interessadas que contribuíram com o levantamento de
requisitos
aceitam a especificação final obtida.

CONSISTÊNCIA Examina se existem conflitos entre os requisitos identificados.

COMPREENSIBILIDADE Examina se os requisitos são compreendidos de forma
inequívoca pelas partes
interessadas.

COMPLETUDE Examina se todas as funcionalidades pretendidas fazem parte da
especificação do
sistema.

REALISMO Examina se, dadas as restrições do projeto (tecnológicas, financeiras e
temporais), o
sistema especificado é implementável.

VERIFICABILIDADE Examina se os requisitos foram descritos de forma que seja possível
verificar se foram
ou não implementados.

RASTREABILIDADE Examina se a origem de cada requisito está claramente identificada.

ADAPTABILIDADE Examina se os requisitos podem sofrer alterações sem produzir
efeitos em outros
requisitos.


CONFORMIDADE COM

NORMAS

Examina se a especificação obedece às normas técnicas utilizadas para
o
desenvolvimento do sistema.

Ademais, podemos dizer que a Revisão Técnica se divide em Comentários,
Inspeções e
Walkthroughs. No primeiro caso, os requisitos são repassados e são realizados
comentários; no
segundo caso, busca-se antecipar a descoberta de falhas, lendo, entendendo o
documento e
checando por meio de um checklist de modo que não se propaguem para o passo seguinte
do
processo de software.

Por fim, os Walkthroughs são realizados através de uma execução passo a passo de um
procedimento ou programa (no papel), com a finalidade de encontrar erros. São realizadas
simulações da execução por cada revisor, controlada por um testador que
durante a reunião
disponibiliza um conjunto de casos de teste e monitora os resultados obtidos
de cada revisor.
Interessante, não?


De acordo com Stephen R. Schach, de forma superficial, a diferença entre uma inspeção
e um
walkthrough é que a equipe de inspeção usa uma lista de verificação de questões
levantadas para
ajudá-la a encontrar as imperfeições. No entanto, a diferença vai muito além disso!
Walkthrough
é um processo de duas etapas: preparação, seguida de análise do documento pela equipe.

Inspeção é um processo de cinco etapas: visão geral, preparação, inspeção,
reformulação e
acompanhamento; o procedimento a ser seguido em cada etapa é formalizado. Exemplos dessa
formalização são a categorização metódica das falhas e o emprego dessas informações na
inspeção dos documentos dos fluxos de trabalho seguintes bem como nas inspeções de futuros
produtos.

Item. 2. Prototipação:

Um modelo executável do sistema é apresentado para usuários finais e
clientes. Eles podem
experimentar o modelo para verificar se atende às suas necessidades reais.
Também há
desvantagens: o tempo gasto na sua implementação pode não justificar o seu uso, pode
enviesar
os usuários e pode ainda levar os programadores a cair na tentação de usar o
protótipo para
continuar o desenvolvimento do sistema.

Professor, me ajuda! Qual a diferença entre a técnica de prototipação
mencionada na fase de
Elicitação de Requisitos e a técnica de prototipação mencionada agora na fase de
Validação de
Requisitos? Bem, no primeiro caso, o objetivo é descobrir, levantar, elicitar novos
requisitos do
sistema. No segundo caso, é validar-por meio de um protótipo-se os requisitos
elicitados são
realmente o que o usuário pensava.

Item. 3. Geração de Casos de Teste:

É importante destacar que os requisitos devem ser testáveis. Se os testes dos
requisitos forem
criados como parte do processo de validação, eles frequentemente revelarão
problemas de
requisitos. Se um teste for difícil demais ou impossível de ser projetado, significa
geralmente que
os requisitos serão difíceis de serem implementados e devem ser
reconsiderados para
implementação.

A diferença entre Verificação e Validação de Requisitos é, em geral, ignorada em
prova-ambos
são chamados apenas de Validação de Requisitos. Caso cobrem, eis a diferença: a
Verificação de
Requisitos tem o objetivo de descobrir se os requisitos são claros, precisos,
completos e
consistentes, e tem por objetivo analisar se os modelos construídos estão de
acordo com os
requisitos definidos.

Professor, e a validação de requisitos? Ela se ocupa de mostrar que os requisitos
realmente
definem o sistema que o cliente deseja, isto é, visa assegurar que as necessidades do
cliente
estão sendo atendidas por tais requisitos. Entenderam um pouco melhor? No entanto,
conforme
eu disse, é comum que as provas tratem ambos simplesmente como Validação de Requisitos.


Durante o processo de validação de requisitos, devem ser realizadas verificações nos
requisitos do
documento de requisitos. Essas verificações incluem:

TIPO DE VERIFICAÇÃO I DESCRIÇÃO

Estudos e análises podem identificar que funções adicionais e diferentes
daquelas


VERIFICAÇÃO DE

VALIDADE

VERIFICAÇÃO DE
CONSISTÊNCIA

VERIFICAÇÃO DE
COMPLETEZA

VERIFICAÇÃO DE

REALISMO

FACILIDADE DE
VERIFICAÇÃO

levantadas pelos usuários são necessárias. Os sistemas têm diversos stakeholders com
necessidades diferentes e qualquer conjunto de requisitos é, inevitavelmente, um
compromisso.

Os requisitos em um documento não devem ser conflitantes e contraditórios.
Isso
significa que não devem existir restrições ou descrições contraditórias para a mesma
função do sistema, porque isso gera problemas sérios de inconsistência.

O documento de requisitos deve incluir requisitos que definam todas as funções e as
restrições desejadas pelo usuário do sistema. Isso torna o documento de requisitos
bastante verboso e pesado, no entanto é um requisito para alcançar a completeza do
requisito.

Usando o conhecimento da tecnologia existente, os requisitos devem ser verificados
quanto a se realmente podem ser implementados. Essas verificações também devem
levar em consideração o orçamento e o prazo para o desenvolvimento do sistema - caiu
questão de prova recente sobre isso!

Para reduzir o potencial de divergências entre cliente e fornecedor, os requisitos do
sistema devem sempre ser escritos de modo que sejam verificáveis. Isso significa que
você deve ser capaz de escrever um conjunto de testes que possa demonstrar que o
sistema entregue atende a cada requisito especificado.

O que vocês precisam memorizar sobre a validação de requisitos? Vocês devem saber que se trata de
uma etapa para verificar duas coisas: se os requisitos atendem, de fato, às
necessidades dos
usuários; e se os requisitos são válidos, consistentes, completos, reais, abrangentes,
etc. Para isso,
existem diversas técnicas que podem ser utilizadas isoladamente ou em
conjunto.
Fechado? Então vamos para a nossa última fase...


Gerenciamento de Requisitos

Enfim, finalizamos as etapas de Engenharia de Requisitos. No entanto, há um
processo
extremamente importante que envolve todas as fases estudadas: Gerenciamento
de
Requisitos. Sabe-se que os requisitos estão em constante evolução. Portanto, esse é o
processo
responsável por compreender, acompanhar e controlar as mudanças dos requisitos
de sistema,
identificando inconsistências.

É necessário manter o acompanhamento dos requisitos individuais e manter as ligações
entre os
requisitos dependentes, de modo que seja possível avaliar o impacto das mudanças de requisitos
(rastreabilidade). É necessário, também, estabelecer um processo formal para fazer
propostas de
mudança e ligá-las aos requisitos. O processo de gerenciamento de requisitos deve se
iniciar assim
que uma versão inicial do documento de requisitos esteja disponível.

No entanto, o planejamento das mudanças de requisitos deve ser iniciado durante o
processo
de elicitação de requisitos. A evolução de requisitos, durante o processo de
engenharia de
requisitos e após a entrada de um sistema em operação, é inevitável. O
desenvolvimento de
requisitos de software enfoca as capacidades de software, objetivos da empresa e outros
sistemas
da empresa.

À medida que a definição dos requisitos se desenvolve, uma compreensão maior das
necessidades
dos usuários é obtida. Isso realimenta as informações do usuário que pode, então,
propor uma
mudança nos requisitos. Existem vários relacionamentos entre os requisitos em
si, entre os
requisitos e componentes e entre requisitos e o projeto do sistema. Há também
ligações entre
requisitos e os motivos básicos de porque esses requisitos foram propostos.

Quando as mudanças são propostas, deve-se rastrear seu impacto em outros requisitos e
no
projeto do sistema. A rastreabilidade é a propriedade de uma especificação de
requisitos que
reflete a facilidade de encontrar os requisitos relacionados. Ela é frequentemente
representada por
meio de matrizes de rastreabilidade que relacionam os requisitos aos
stakeholders, aos outros
requisitos, aos módulos de projeto, aos artefatos ou subprodutos, entre outros.

Em uma matriz de rastreabilidade de requisitos, cada requisito é introduzido em uma
linha e uma
coluna da matriz. As dependências entre diferentes requisitos são registradas
na célula
correspondente à intersecção de linha e coluna. Existem três tipos de
informações de
rastreabilidade que podem ser mantidas na matriz - elas são apresentadas como pode ser
visto a
seguir:

Informações de rastreabilidade da origem: ligam os requisitos aos
stakeholders que
propuseram os requisitos e aos motivos desses requisitos. Quando uma mudança é proposta,
usam-se essas informações para consultar os stakeholders sobre a mudança.


Informações de rastreabilidade de requisitos: ligam os requisitos dependentes
dentro do
documento de requisitos. Usam-se essas informações para avaliar quantos
requisitos serão
afetados pela mudança e a extensão das mudanças de requisitos necessárias.

Informações de rastreabilidade de projeto: ligam os requisitos aos módulos de
projeto, nos
quais esses requisitos são implementados. Você usa essas informações para avaliar o
impacto
das mudanças de requisitos propostas no projeto e na implementação do sistema.

As matrizes de rastreabilidade podem ser usadas quando um pequeno número de requisitos
deve
ser gerenciado, mas para sistemas de grande porte, com muitos requisitos, tornam-se
muito
difíceis de serem gerenciadas e sua manutenção é dispendiosa. Para esses sistemas,
deve-se
captar as informações de rastreabilidade em um banco de dados de requisitos - é algo
bem mais
complexo.

Por falar nisso, um de nossos autores favoritos (Roger Pressman) afirma que o
gerenciamento
formal de requisitos é iniciado somente para grandes projetos com centenas de
requisitos
identificáveis. Para projetos pequenos, essa função de engenharia de
requisitos é
consideravelmente menos formal e, na prática, dispensável. Bacana? Fim, galera...
podem
comemorar que agora é só exercício;)


RESUMo


REQUISITOS DE USUÁRIO

REQUISITOS DE SISTEMA

CLASSIFICAÇÃO QUANTO AO NÍVEL DE ABSTRAÇÃO

Descrições, em linguagem natural e com diagramas, de quais serviços o sistema
deve fornecer e as restrições sob as quais deve operar. São requisitos com alto nível
de abstração e poucos detalhes, feitos para serem lidos por pessoas leigas - podem
serfuncionais ou não funcionais.

Descrições detalhadas sobre as funções, operações e restrições de sistema que
definem exatamente o que deve ser implementado. São requisitos com baixo nível
de abstração e muitos detalhes, feitos para serem lidos por pessoas experientes -
podem serfuncionais ou não funcionais.


REQUISITOS NORMAIS

REQUISITOS ESPERADOS

REQUISITOS FASCINANTES

REQUISITOS PERMANENTES

CLASSIFICAÇÃO QUANTO À QUALIDADE

Refletem os objetivos e metas estabelecidos para um produto ou sistema durante
reuniões com o cliente. Se esses requisitos estiverem presentes, o cliente fica
satisfeito. Exemplos de Requisitos Normais poderiam sertipos de displays gráficos
solicitados, funções de sistema específicas e níveis de desempenho definidos.

Estão implícitos no produto ou sistema e podem sertão fundamentais que o cliente
não os declara explicitamente. Sua ausência será causa de grande insatisfação.
Exemplos de Requisitos Esperados: facilidade na interação homem-máquina,
confiabilidade e correção operacional global e facilidade na instalação do software.

Esses recursos vão além da expectativa dos clientes e demonstram ser muito
satisfatórios quando presentes. Porexemplo, o software para um novo celularvem
com recursos-padrão, mas junto vem um conjunto de capacidades não esperadas.
Exemplos de Requisitos Fascinantes: tecla multitoque e correio de voz visual.

CLASSIFICAÇÃO QUANTO À EVOLUÇÃO

Também chamados de Requisitos Estáveis, estão diretamente ligados a atividade
principal da organização. São concebidos com a essência de um sistema e seu
domínio da aplicação, e mudam mais lentamente que requisitos voláteis. Em geral,
eles são derivados do Modelo de Domínio.


REQUISITOS VOLÁTEIS

REQUISITOS FUNCIONAIS

Também chamados de Requisitos Instáveis, são específicos para a instanciação de
um sistema em um ambiente ou um cliente particular e são mais propensos a
mudança. Se modificam quando o sistema está em desenvolvimento ou em uso.
Podem ser subclassificados em mutáveis, emergentes, consequentes ou de
compatibilidade.

CLASSIFICAÇÃO QUANTO À FUNCIONALIDADE

São ações ou funcionalidades que o sistema deve fornecer para atingir seus
objetivos. Eles dependem do tipo de software, dos usuários esperados e do tipo de
sistema onde o software será implantado e fazem parte da arquitetura de um
sistema. Grosso modo, pode-se dizerque eles tratam de o que o sistema deve fazer
enquanto os requisitos não-funcionais tratam de como o sistema deve fazer.


REQUISITOS NÃO-FUNCIONAIS

REQUISITOS DE DOMÍNIO

REQUISITOS DE PRODUTO

São restrições ou condições estipuladas sobre as quais o sistema deve funcionar.
Não estão diretamente relacionados às funções específicas do sistema, mas às
gerais - e podem incluir restrições de tempo, restrições de processo de
desenvolvimento, restrições impostas por padrões, entre outras. Podem ser mais
críticos que os funcionais e sempre devem ser verificáveis. Eles fazem parte da
arquitetura técnica de um sistema.

são requisitos derivados do domínio da aplicação e refletem características de sua
área de negócio. Eles podem ser requisitos funcionais ou não-funcionais e, caso não
sejam satisfeitos, o sistema pode não ser realizável. Por exemplo, um avião que não
atende aos requisitos de confiabilidade, não será certificado para voo.

CLASSIFICAÇÃO QUANTO À ORIGEM

Especificam o comportamento do produto. Entre os exemplos, estão requisitos de
desempenho quanto à rapidez com que o sistema deve operar e quanto de
memória ele requer, requisitos de confiabilidade que definem a taxa aceitável de
falhas, requisitos de portabilidade e requisitos de usabiIidade.


REQUISITOS ORGANIZACIONAIS

REQUISITOS EXTERNOS

São derivados de políticas e procedimentos da organização do cliente e do
desenvolvedor. Entre os exemplos, estão padrões de processo que devem ser
usados, linguagem de programação ou o método de projeto usado, e requisitos de
entrega que especificam quando o produto e a sua documentação devem ser
entregues.

Abrange todos os requisitos derivados de fatores externos ao sistema e seu
processo de desenvolvimento. Entre os exemplos, estão a interoperabilidade que
define como o sistema interage com outros sistemas, requisitos legais que devem
serseguidos, requisitos éticos sistema para assegurarque ele será aceito portodos.

REQUISITOS NÃO-FUNCIONAIS | EXEMPLOS


REQUISITOS DE
CONFIABILIDADE

REQUISITOS DE
PROTEÇÃO

REQUISITOS DE
DESEMPENHO
REQUISITOS DE

ESPAÇO

REQUISITOS DE
USABILIDADE

REQUISITOS DE
SEGURANÇA

O sistema não deve ficarfora do ar por mais de cinco segundos durante o dia.

O sistema não deve permitir que os usuários modifiquem senhas de acesso que eles
não criaram.

O sistema deverá ser capaz de processar oitocentas requisições por segundo.

Também chamado de Requisitos de Armazenamento, o sistema deverá ocupar, no
máximo, 8oMb da memória interna do dispositivo.

Os usuários deverão operar todas as funcionalidades do sistema após 2 horas de
treino.

O sistema não deve permitira ativação simultânea de mais de três sinais de alarme.

REQUISITOS O sistema não apresentará aos usuários quaisquer dados de natureza
confidencial
de outrem.


ÉTICOS
REQUISITOS DE
IMPLEMENTAÇÃO

A interface de usuário deve ser implementada em HTML e não se deve utili
Applets de Java.


Requisitos de
Contabilidade

Requisitos de
Segurança

FASES | DESCRIÇÃO

Após uma necessidade de o negócio ser identificada, busca-se estabelecer um entendimento


CONCEPÇÃO

LEVANTAMENTO

ELABORAÇÃO

NEGOCIAÇÃO

básico do problema. Trata-se da concepção inicial do software e busca entender o
problema,
quem são os envolvidos, a natureza da solução e iniciar o processo de comunicação
entre
clientes e colaboradores.

Etapa crítica, utiliza uma abordagem organizada para descobrir o que o cliente deseja
em seu
sistema. Envolve intensa participação do stakeholders e faz três perguntas: Qual o
objetivo do
produto? Como o produto se enquadra nas necessidades do negócio? Como o produto será
utilizado?

Por vezes chamada Análise, informações obtidas do cliente durante a
concepção e
levantamento são expandidas e refinadas em um modelo, definindo o domínio do problema.
Incluem-se modelagens de cenários de interação do usuário com o sistema e modelagens
das
classes envolvidas.

Tem por objetivo chegar a um consenso sobre os conflitos entre clientes e
usuários, por
intermédio de um processo de negociação. Os requisitos são avaliados junto ao cliente
e podem
se combinar, excluir ou até mesmo inserir novos requisitos.


ESPECIFICAÇÃO

VALIDAÇÃO

Por vezes chamada Documentação, produto final do engenheiro de requisitos, pode ser um
documento escrito, um modelo gráfico, cenários de uso, protótipos, etc.
Trata-se da
apresentação formal dos dados obtidos até o momento de modo que possa guiar
o
desenvolvimento futuro do software.

Os produtos de trabalho resultantes da engenharia de requisitos são avaliados quanto a
sua
qualidade por todos os envolvidos (clientes, colaboradores e usuários). Buscam-se erros
de
interpretação, ambiguidades e omissões.

GESTÃO conjunto de atividades que auxiliam a equipe de projeto a identificar,
controlar e rastrear
requisitos e mudanças nos requisitos a qualquer momento . Para projetos de grande porte, é
uma fase essencial na medida em que mudanças em um requisito podem afetar diversos
requisitos.

POR SOMMERVILLE | POR PRESSMAN

ESTUDO DE VIABILIDADE CONCEPÇÃO

ELICITAÇÃO E ANÁLISE DE REQUISITOS
LEVANTAMENTO
ELABORAÇÃO

nOnBTmTEmNÃÇn ÃnrOnrDniEunRiTEnQn UISITOS _ _

CLASSIFICAÇÃO E ORGANIZAÇÃO

PRIORIZAÇÃOE NEGOCIAÇÃO NEGOCIAÇÃO

DOCUMENTAÇÃO DE REQUISITOS

CtoCrDtbClPrlILCAIPUAAPUÃO
CtoCrDtbClPrlIUCAIP^AAPUÃn

VALIDAÇÃO VALIDAÇÃO

GESTÃO GESTÃO

Onefootball

Alexandre Fernandes * 10 de out de 2019

Cenas lamentáveis em
novo empate do Vasco da
Gama

FASES DE ACORDO COM IAN SOMMERVILLE

ÃO VIABILIZANDO ANA ALMENTENO SCODA AMA

UDO DE DADE > CITAÇÃO E ANÁLISE DE REQUISITOS > FICAÇÃO > LICAÇÃO > ESTÃO

FASES DE ACORDO COM ROGER PRESSMAN

ENAS AMENTÁVEIS M OVO MPATEDO ASCO DA AMA


ONCEPÇÃO> EVANTAMENTO > LABORAÇÃO > EGOCIAÇÃO > SPECIFICAÇÃO > ALIDAÇÃO > ESTÃO

Relatório de
Viabilidade


PRINCIPAIS
TÉCNICAS

ENTREVISTA

ETNOGRAFIA

CENÁRIOS

QUESTIONÁRIOS

WORKSHOPDE
REQUISITOS

DESCRIÇÃO

Entrevistas formais ou informais com os stakeholders do sistema fazem parte da maioria
dos
processos de engenharia de requisitos. Nessas entrevistas, a equipe de engenharia de
requisitos
formula questões para os stakeholders sobre o sistema que eles usam e o sistema a ser
desenvolvido. Os requisitos são derivados a partirdas respostas dessas questões. As
entrevistas
podem ser abertas ou fechadas.

Técnica de observação utilizada para compreender os requisitos organizacionais e
sociais.
Coloca-se o analista dentro do campo de atuação dos usuários, observando o trabalho
diário
anotando as tarefas reais em que os participantes estão envolvidos. Em geral, essa é
uma
técnica utilizada em conjunto com outras técnicas. Como ela é uma técnica de
observação,
isoladamente ela não é muito eficaz na elicitação.

As pessoas geralmente consideram mais fácil relatar exemplos da vida real do que
abstrair
descrições. Elas podem compreender e criticar um cenário de como interagiriam
com um
sistema de software. Os engenheiros de requisitos podem usar as informações obtidas
nessa
discussão para elaborar os requisitos reais do sistema de software. Os cenários podem
ser
particularmente úteis para adicionar detalhes a um esboço da descrição de requisitos.

Formulários distribuídos aos stakeholders com questões pré-definidas. Torna-se útil quando
a
quantidade de stakeholders é muito grande. Tem baixo custo, é fácil de aplicar, pode
atingir
várias pessoas, demanda menos tempo e fornece rápido feedback. No entanto, há
uma
tonelada de problemas, como falta de interação, perguntas pouco
objetivas, difícil
compreensão das perguntas, entre outros.

Reunião estruturada e intensiva entre analistas e usuários com o intuito de obter um
conjunto
de requisitos bem definidos. Possui um facilitador neutro responsável pelas
atividades de
logística e promoção de momentos de descontração, como forma de dinamizar o trabalho em
equipe. Permite utilizar outras técnicas em conjunto como brainstorming ou interpretação
de
papéis.

É uma abordagem de elicitação ocorrida em grupo em ambientes informais durante cerca
de 15
minutos em que toda a ideia deve ser levada em consideração, sendo proibida a crítica
a
qualquer sugestão dada, e encorajada, inclusive, a criação de ideias que pareçam
estranhas ou
exóticas. Busca-se explorar a potencialidade criativa de um grupo - um facilitador
organiza e
prioriza os resultados.

Similaràtécnica de workshopde requisitose registrada pela IBM, ela busca reuniros
usuáriose
desenvolvedores em um workshop estruturado para levantar requisitos e promover a tomada
de decisões por meio de diversos tipos de dinâmicas de grupo, técnicas visuais,
processos
racionais e até documentação. É bastante interativa e promove a participação
ativa dos
envolvidos- inclusive dos tímidos.

Técnica de elicitação, independente de tecnologia, utilizada no estágio inicial
do projeto,
ajudando stakeholders a desenvolverem uma forte noção sobre a aplicação a ser
implementada.
Por meio da visualização de um esboço da aplicação, podem-se identificar requisitos
reais e
fluxos de trabalho do sistema. São frequentemente utilizadas quando os usuários são
incapazes
de expressar suas necessidades.

O reúso de requisitos trata do estudo e reutilização de especificações e glossários
referentes a
projetos de sistemas legados ou sistemas de mesma família ou com funcionalidades de
negócio
similares. Estudos mostram que sistemas similares podem reutilizar mais de 80%
de seus
requisitos. Dessa forma, eles têm chances maiores de serem compreendidos pelos
stakeholders

- 0 que é uma excelente vantagem.

Introduzida inicialmente pela Metodologia XP (Extreme Programming), nada mais é do que
uma
história contada na linguagem do usuário final, que deve ser capaz de capturar aquilo
que 0
usuário de fato necessita fazer para realizar seu trabalho. Deve ser concisa 0
suficiente para
caber em um post-it. Um padrão seria: "Como um <papel>, eu quero <meta> de modo que

<benefício>".

® PARA MAIS DICAS: WWW.INSTA6RAM.COM/PROFESSORDIEGOCARVALHO


QUESTõES CoMENTADAS - CESPE

í. (CESPE / BANRISUL - 2022) Requisitos não funcionais de um sistema descrevem seu
objetivo
e dependem do tipo de software a ser desenvolvido, dos usuários esperados para o
software e
da abordagem geral adotada pela organização ao escrever os requisitos.

Comentários:

Requisitos Não Funcionais (RNF) são requisitos que não estão diretamente relacionados
com os
serviços específicos oferecidos pelo software a seus usuários. A descrição da questão
trata dos
Requisitos Funcionais (RF).

Gabarito: Errado

Item. 2. (CESPE / BANRISUL - 2022) Requisitos organizacionais são requisitos de
sistema amplos,
derivados das políticas e dos procedimentos nas organizações do cliente e do
desenvolvedor,
cujas funções incluem definir como o sistema será utilizado e especificar a
linguagem de
programação.

Comentários:

Requisitos Organizacionais são derivados de políticas e procedimentos da organização do
cliente e
do desenvolvedor. Entre os exemplos, estão padrões de processo que devem ser usados,
linguagem
de programação ou o método de projeto usado, e requisitos de entrega que especificam
quando o
produto e a sua documentação devem ser entregues.

Gabarito: Correto

Item. 3. (CESPE / BANRISUL - 2022) Os requisitos do sistema devem descrever os comportamentos
interno e externo do sistema, devendo-se preocupar com a forma como ele deve ser
projetado
ou implementado.

Comentários:

Os requisitos do sistema devem descrever apenas o comportamento externo do sistema e
suas
restrições operacionais. Eles não devem se preocupar com a forma como o
sistema deve ser
projetado ou implementado.

Gabarito: Errado

Item. 4. (CESPE / BANRISUL - 2022) A especificação de requisitos é frequentemente
composta de
vários tipos de documentos e não raro abrange: visão geral; glossário; modelos do sistema; lista
de requisitos funcionais e lista de requisitos não funcionais; especificação
detalhada de
requisitos.

Comentários:

A Especificação de Requisitos é um documento importante que descreve os requisitos
específicos
de um projeto. Esta especificação inclui vários documentos para garantir que
todas as partes
interessadas estejam cientes do que se espera do projeto. Estes documentos incluem uma
visão
geral, glossário, modelos do sistema, lista de requisitos funcionais e não funcionais,
e especificação
detalhada de requisitos.

Gabarito: Correto

Item. 5. (CESPE / BANRISUL - 2022) O objetivo principal da especificação é
documentar todas as
necessidades dos clientes e obter um aceite quanto às entregas de produto propostas.

Comentários:

A especificação tem como objetivo fornecer aos clientes um documento detalhado que
descreva
todas as suas necessidades e requisitos, além de obter um acordo entre as partes
envolvidas quanto
às entregas esperadas. Esta documentação pode ajudar a evitar erros e mal-entendidos
entre as
partes, garantindo que os requisitos do cliente sejam atendidos.

Gabarito: Correto

Item. 6. (CESPE / BANRISUL - 2022) Na execução da técnica de apprenticing
(aprendizado), o
engenheiro de requisitos deve questionar procedimentos operacionais complexos e
pouco
claros do domínio do sistema que os stakeholders desejam preservar.

Comentários:

O engenheiro de requisitos deve entender como os stakeholders gostariam de
preservar os
procedimentos operacionais complexos e pouco claros do sistema. A técnica de
apprenticing
permite que o engenheiro de requisitos questione os stakeholders sobre o que eles
querem que seja
preservado e sobre como o sistema deve ser construído para atender a essas
necessidades. Ao
questionar os stakeholders, o engenheiro de requisitos pode ajudá-los a compreender
melhor como
os procedimentos operacionais complexos e pouco claros devem ser implementados e
gerenciados
pelo sistema.

Gabarito: Correto

Item. 7. (CESPE / BANRISUL - 2022) Em situações em que alguma das partes interessadas não
consiga
expressar de forma oral as suas necessidades com clareza, recomenda-se o emprego da
técnica
da etnografia para o levantamento de requisitos.


Comentários:

A etnografia é uma abordagem qualitativa de pesquisa que permite o
aprofundamento de
conhecimento sobre o contexto de determinada situação. Ela permite a
compreensão das
necessidades das partes interessadas, mesmo que elas não consigam expressá-las de forma
verbal.
Ao seguir essa abordagem, é possível identificar os interesses, motivações e
comportamentos que
estão por trás do problema, permitindo assim a construção de soluções mais
adequadas ao
contexto.

Gabarito: Correto

Item. 8. (CESPE / BANRISUL-2022) O levantamento de requisitos com casos de uso é muito
eficaz para
a elicitação de requisitos não funcionais.

Comentários:

O levantamento de requisitos com casos de uso é eficaz para a elicitação de
requisitos funcionais,
pois fornece detalhes sobre como um sistema deve se comportar. Os requisitos não
funcionais,
como aspectos de desempenho e segurança, são melhor identificados por meio de técnicas
de
análise de requisitos como entrevistas, questionários, estudos de caso, brainstorming, etc.

Gabarito: Errado

Item. 9. (CESPE / BANRISUL-2022) A analogia é uma técnica pouco recomendada quando é
necessário
identificar requisitos novos, inovadores ou atrativos, em um ambiente cujo objetivo é
encontrar
soluções criativas.

Comentários:

A analogia pode ser uma ferramenta extremamente útil para identificar
novos requisitos,
inovadores ou atrativos. Ela é especialmente útil quando se trata de encontrar soluções
criativas,
pois permite que os usuários comparem elementos já existentes com outros que podem ser
usados
para criar algo novo. Ela também pode ajudar os desenvolvedores a visualizar o
problema de forma
diferente, o que pode apontar para soluções que eles não teriam encontrado de outra forma.

Gabarito: Errado

10.(CESPE / BANRISUL-2022) A arqueologia é uma técnica apropriada quando se busca
preservar
todas as funcionalidades de um sistema legado em um novo sistema que reutilize as
soluções e
experiências existentes.

Comentários:


A arqueologia é uma ótima ferramenta para modernizar sistemas legados, pois ajuda a
preservar o
conhecimento e as funcionalidades existentes. Ela ajuda a extrair informações úteis
sobre o sistema
legado, permitindo que os desenvolvedores entendam melhor como ele está estruturado e
como
ele pode ser melhorado. Além disso, ela ajuda a preservar as soluções e experiências
existentes,
ajudando a evitara necessidade de se reinventara roda durante o processo de modernização.

Gabarito: Correto
íi. (CESPE / MPC-SC - 2022) A etnografia é o processo de elicitação por meio do
qual o analista de
requisitos realiza uma imersão no ambiente de trabalho em que o sistema será utilizado
para
tornar compreensíveis os processos operacionais e auxiliar na extração dos requisitos de
apoio
de tais processos.

Comentários:

A etnografia é uma técnica de observação que pode ser utilizada para
entender os processos
operacionais e para ajudar a derivar os requisitos do software que apoia esses
processos. Um
analista deve ficar imerso no ambiente de trabalho em que o sistema será utilizado
com o objetivo
de observar o dia a dia e tomar nota das tarefas reais nas quais os participantes
estão envolvidos. A
vantagem da etnografia é que ela ajuda a descobrir requisitos implícitos do
sistema, os quais
refletem o verdadeiro modo de trabalho das pessoas, em vez dos processos formais
definidos pela
organização. Logo, a questão está correta, mas foi anulada porque o conteúdo extrapolava o edital.

Gabarito: Anulado

Item. 12. (CESPE / BNB - 2022) Para capturar os requisitos da interface de um sistema, os
protótipos
podem ser desenhados como mockups, mesmo que estes não permitam interações do usuário
com a execução das funcionalidades.

Comentários:

Perfeito! Mockups são protótipos estáticos que fornecem uma visão geral da interface de
usuário e
ajudam os desenvolvedores a entender melhor os requisitos de design. Embora os mockups
não
permitam interações do usuário, eles são úteis para garantir que o design seja
consistente e fácil de
usar. Os mockups podem ajudar os designers a entender como os elementos de interface
devem se
conectar para criar uma experiência de usuário agradável. Eles podem também
ajudar os
desenvolvedores a construir a interface de usuário corretamente e fornecem aos
desenvolvedores
uma visão geral da aparência do produto final, possibilitando que eles criem os
recursos corretos e
que sejam adequados para a interface de usuário.

Gabarito: Correto
i3-(CESPE / BNB - 2022) Um dos critérios de boa qualidade para uma história de
usuário é o
denominado critério pequeno, ou seja, aquele cujo desenvolvimento da
história deve
representar um trabalho desenvolvido dentro de um limite de tempo de duração específica.

Comentários:

Um princípio de boa qualidade para histórias de usuário que estabelece que
elas devem ser
pequenas o suficiente para serem concluídas em uma única iteração. Isso significa que
elas não
devem ser tão grandes ou complexas a ponto de não poder ser concluídas em um único
ciclo de
desenvolvimento. Histórias muito grandes devem ser divididas para que
elas possam ser
desenvolvidas e concluídas mais facilmente. Além disso, as histórias de usuário também
devem ser
pequenas o suficiente para que possam ser priorizadas de forma eficiente.

O gabarito definitivo foi errado, então eu presumo que a banca entenda que não se
trata de um
limite de tempo de duração específico e, sim, um limite de tempo de duração pequeno
(um limite
específico poderia ser um limite grande, por exemplo, o que não satisfaz no critério).

Gabarito: Errado
i4.(CESPE/ BNB-2022) Em uma história de usuário, em que se deseja fazer login com a
impressão
digital do cliente para o seu acesso à sua conta bancária, um exemplo correto de
critério de
aceitação é: dado que estou realizando login com minha digital, quando eu
colocar o dedo
cadastrado no leitor, então consigo acessar minha conta.

Comentários:

O critério de aceitação de uma história de usuário é um conjunto de condições que
devem ser
atendidas para que uma história de usuário seja considerada concluída. Estas condições
podem
incluir testes de aceitação, listas de verificação, requisitos de qualidade, documentação
e outros
critérios estabelecidos pelo time. O critério de aceitação deve ser acordado e
documentado pelo
time antes do início do desenvolvimento da história.

Dito isso, a questão está perfeita! Esse critério de aceitação define que, se o
usuário estiverfazendo
login com a impressão digital, então ele deve conseguir acessar sua conta ao
colocar o dedo
cadastrado no leitorde impressão digital. Isso significa que a função de login com
impressão digital
está funcionando corretamente e que o usuário pode acessar sua conta mediante o
uso desta
funcionalidade.

Gabarito: Correto
i5.(CESPE / BNB - 2022) No gerenciamento de requisitos, uma adequada
configuração, em
particular, de uma especificação tem a propriedade de ser imutável.

Comentários:


Questão polêmica! O gabarito definitivo foi correto, mas eu acho quase
impossível existir uma
documentação imutável mesmo com a mais adequada configuração. Para mim, a questão
caberia
recurso.

Gabarito: Correto
i6.(CESPE / BANRISUL-2022) O levantamento de requisitos com casos de uso é muito
eficaz para
a elicitação de requisitos não funcionais.

Comentários:

Não, o levantamento de requisitos com casos de uso é muito eficaz para e elicitação
de requisitos
rwe funcionais.

Gabarito: Errado

Item. 17. (CESPE / BANRISUL - 2022) Em situações em que alguma das partes interessadas não
consiga
expressar de forma oral as suas necessidades com clareza, recomenda-se o emprego da
técnica
da etnografia para o levantamento de requisitos.

Comentários:

Perfeito! A etnografia é uma técnica de observação que pode ser utilizada para
compreender os
requisitos sociais e organizacionais, ou seja, entender a política organizacional bem
como a cultura
de trabalho com objetivo de familiarizar-se com o sistema e sua história.

Gabarito: Correto

18.(CESPE / BANRISUL - 2022) A acessibilidade está relacionada à
facilidade com que
determinada informação é assimilada por pessoas com alguma deficiência.

Comentários:

Perfeito! A acessibilidade está completamente relacionada à facilidade de utilização para
pessoas
com necessidades especiais.

Gabarito: Correto

19.(CESPE/ BANRISUL-2022) A usabilidade é um atributo de qualidade de um projeto que
avalia
se ele fornece os recursos que os usuários precisam.

Comentários:


Não, a usabilidade é um atributo de qualidade que avalia quão fácil uma interface é de usar.

Gabarito: Errado

2o.(CESPE / FUNPRESP-EXE - 2022) As verificações de validade, consistência e completeza
são
técnicas fundamentais do processo de validação de requisitos.

Comentários:

Perfeito! A equipe de revisão deve verificar cada requisito em termos de consistência
(para evitar
ambiguidade), bem como verificar os requisitos como um todo em termos de completeza.

Gabarito: Correto

2i.(CESPE / FUNPRESP-EXE - 2022) Dentre as técnicas existentes de elicitação
de requisitos
baseadas em cenários, os casos de uso são modelos que ajudam a identificar
agentes e
interações do sistema.

Comentários:

Casos de Uso são uma técnica para captar os requisitos funcionais de um sistema. Eles
servem para
descrever as interações de usuários com o sistema, fornecendo uma narrativa sobre como
o sistema
é utilizado.

Gabarito: Correto

22.(CESPE / FUNPRESP-EXE - 2022) A técnica Quality Function Deplyment tem como
objetivo
traduzir os requisitos técnicos em requisitos do cliente.

Comentários:

Na verdade, Quality Function Deployment (QFD) é uma técnica da gestão de qualidade que
traduz
as necessidades do cliente para requisitos de software. É o contrário do que diz a questão.

Gabarito: Errado

23.(CESPE / FUNPRESP-EXE - 2022) O protótipo de interface do usuário é o produto
final da
técnica de prototipação da engenharia de requisitos.

Comentários:

O produto final da engenharia de requisitos é a documento de requisitos.


Gabarito: Errado

24.(CESPE / FUNPRESP-EXE - 2022) Brainstorming é uma técnica utilizada para o
levantamento
de requisitos; para facilitar o registro, essa técnica deve ser feita por meio de questionário.

Comentários:

Brainstorming é uma técnica que utiliza uma abordagem informal, logo ela não pode ser
feita por
meio de questionários. Relembrando: Brainstorming é uma abordagem de elicitação
ocorrida em
grupo em ambientes informais durante cerca de isminutos em que toda a ideia deve ser
levada em
consideração.

Gabarito: Errado

25.(CESPE / Petrobrás - 2022) Ferramentas automatizadas para armazenamento de
requisitos,
gerenciamento de mudanças e gerenciamento de rastreabilidade são indicadas para apoio ao
processo de gerenciamento de requisitos.

Comentários:

De acordo com Sommerville, o gerenciamento de requisitos precisa de apoio automatizado,
sendo
que esse apoio é provido por meio de ferramentas automatizadas que são escolhidas
durante a fase
de planejamento. Desse modo, as ferramentas de apoio são úteis para o
armazenamento de
requisitos, o gerenciamento de mudanças e o gerenciamento de rastreabilidade.

Gabarito: Correto

26.(CESPE / Petrobrás - 2022) Histórias de usuário são ferramentas para a definição de
escopo de
produtos de software voltadas a fornecer uma análise detalhada sobre a atividade do
usuário e
a viabilizar a retenção de conhecimento em longo prazo.

Comentários:

As Histórias de Usuário (User Stories) são artefatos de desenvolvimento
utilizados em sistemas
geridos segundo metodologias ágeis. Elas são uma descrição resumida de alguma
funcionalidade
fornecida pelo sistema do ponto de vista de um usuário desse sistema. Importante
ressaltar que se
trata de uma descrição de uma pequena parte de uma funcionalidade, e não de uma
funcionalidade
completa. Vejam, portanto, que a questão não se trata da definição das histórias de usuário.

Gabarito: Errado


27.(CESPE / Petrobrás - 2022) Os critérios de aceitação descrevem um conjunto
mínimo de
requisitos que precisam ser atendidos para que valha a pena implementar uma
solução
específica.

Comentários:

Exato! Os critérios de aceitação estão relacionados aos requisitos que devem ser
atendidos para
que seja possível executar um projeto. Esses critérios são as condições, normalmente
dadas pelo
cliente, que trazem os requisitos mínimos que devem ser alcançados.

Gabarito: Correto

28.(CESPE / Petrobrás - 2022) Entrevistas e questionários são técnicas comumente usadas
para
obter informações relacionadas às necessidades de grupos de usuários
representados por
personas, que exemplificam como um usuário típico interage com um produto.

Comentários:

Uma persona é uma pessoa fictícia que está interessada no sistema. Dessa forma, é
comum utilizar-
se entrevistas e questionários para se extrair de tais pessoas suas necessidades
relacionadas a um
produto, pois isso irá exemplificar como será a interação entre eles.

Gabarito: Correto

2g.(CESPE/ Petrobrás - 2022) No contexto de storytelling, é fundamental mitigaras
possibilidades
de navegação por meio das interfaces e impor à experiência do usuário o
sequenciamento
estrito das atividades que constituem a sua história.

Comentários:

Storytelling trata-se do ato de contar histórias. Dessa forma, pode-se transmitir
conhecimentos e
compartilhar experiências. Dessa forma, Storytelling nada tem a ver com mitigar
possibilidades ou
impor experiências aos usuários.

Gabarito: Errado

3o.(CESPE / TJ-RJ - 2021) Na engenharia de requisitos, por estar mais aderente às
características
dessa técnica, a etnografia é recomendada:

a) na elicitação da forma como o fluxo dos processos deveria ser feito.

b) na descoberta dos requisitos organizacionais.

c) quando se deseja obter uma visão do funcionamento do sistema na forma
prevista,
independentemente das interferências de seu contexto.


d) na descoberta de requisitos derivados do conhecimento das atividades de outras
pessoas que
realizam trabalhos adjacentes ao analisado.

e) como uma alternativa aos casos de uso para a descoberta dos requisitos explícitos.

Comentários:

O principal objetivo da etnografia é que ela ajuda a descobrir requisitos de sistema
implícitos, que
refletem os processos reais, em vez de os processos formais, onde as pessoas estão
envolvidas. São
os requisitos derivados da maneira como as pessoas realmente trabalham, em vez da
maneira pelas
quais as definições de processo dizem como elas deveriam trabalhar. Além disso, essa
abordagem
é recomendada para levantar requisitos derivadas da cooperação e interação entre pessoas
em seu
ambiente natural. A redação é meio estranha, mas foi isso que o item (d) quis dizer
com descoberta
de requisitos derivados do conhecimento das atividades de outras pessoas que realizam
trabalhos
adjacentes ao analisado.

Gabarito: Letra D

Item. 31. (CESPE / TJ-RJ - 2021) Para os propósitos da modelagem dos requisitos com base em
cenários,
um suporte apropriado é o uso de
a) diagrama de casos de uso e histórias de usuários.

b) diagrama de sequência e diagrama de atividades.

c) diagramas que representem eventos ou estados.

d) diagrama de classes e histórias de usuário.

e) modelagem com cartões CRC e casos de uso.

Comentários:

Os diagramas de casos de uso e as histórias de usuários são técnicas baseadas em
cenários para a
obtenção de requisitos, que identificam os atores envolvidos em uma interação e que
descrevem a
interação em si.

Gabarito: Letra A

Item. 32. (CESPE / TELEBRÁS - 2021) No âmbito da engenharia de software, o principal
produto da
engenharia de requisitos é o documento de especificação de requisitos de software.

Comentários:

Perfeito! De acordo com Sommerville, o objetivo da engenharia de requisitos é criar e
manter um
documento de requisitos de sistema.

Gabarito: Correto


33-(CESPE / TCE-RJ - 2021) O gerenciamento de requisitos trata do
desenvolvimento
de software por meio da metodologia ágil; isso permite o isolamento entre o
desenvolvedor e o
usuário, já que é comum ocorrer problema de mudanças de requisitos ao longo do curso
do
projeto devido ao interfaceamento do usuário com o desenvolvedor.

Comentários:

O gerenciamento de requisitos é o processo responsável porcompreender, acompanhare
controlar
as mudanças nos requisitos de um sistema, identificando as inconsistências -
não existe essa
relação direta com metodologia ágil. Além disso, não é recomendável haver um isolamento
entre
o desenvolvedor e o usuário - e os requisitos mudarem não é necessariamente um problema.

Gabarito: Errado

34.(CESPE / TCE-RJ - 2021) Em um processo de desenvolvimento de software, a elicitação
de
requisitos serve para identificar os fatos que compõem os requisitos do sistema.

Comentários:

Elicitar significa descobrir, identificar, extrair. A fase Elicitação, portanto,
trata do processo de
levantamento e derivação de requisitos de sistema por meio de diversas técnicas.

Gabarito: Correto

35.(CESPE / Ministério da Economia - 2020) Um dos princípios em que se baseia a
técnica de
dinâmica de grupo conhecida como brainstorm é o atraso de julgamento, que
possibilita a
geração de muitas ideias antes de se decidir por uma.

Comentários:

O atraso de julgamento está relacionado à criação de ideias sem que se importe se
tal ideia é boa
ou ruim, ou seja, sem fazer um julgamento da ideia. É o que, de fato, se busca em
uma tempestade
de ideias: gerar um grande número de ideias, sem se preocupar com elas.

Gabarito: Correto

36.(CESPE / Ministério da Economia - 2020) Os requisitos do software mudam com
frequência,
mas é sempre possível acomodá-los no sistema, pois o software é flexível.

Comentários:

A fase da Engenharia de Requisitos é de extrema importância no desenvolvimento de um
software.
Erros nesse estágio podem ocasionar grandes problemas nas etapas posteriores do projeto e na
implementação do sistema. Dessa forma, é um erro afirmar que é sempre possível
acomodar novos
requisitos.

Gabarito: Errado

Item. 37. (CESPE / Ministério da Economia - 2020) Requisitos funcionais envolvem as
características de
confiabilidade e de desempenho de um sistema.

Comentários:

Na verdade, requisitos não-funcionais, que incluem características como confiabilidade,
segurança,
usabilidade, performance, custos, robustez, etc.

Gabarito: Errado

38.(CESPE / Ministério da Economia - 2020) Elicitar requisitos não inclui somente
necessidades
dos usuários, mas também extrair informações que surgem de padrões
organizacionais,
governamentais e industriais em geral, para atender necessidades.

Comentários:

Perfeito! Por exemplo: uma técnica usada na Elicitação de Requisitos é a de
Etnografia, que é
utilizada para compreender os requisitos organizacionais e sociais. Além disso,
a Leitura de
Documentos é outro exemplo - ela coleta informações como: histórico da organização,
cultura e
hábitos internos, relacionamentos setoriais, informações financeiras e direcionamentos futuros.

Gabarito: Correto

39.(CESPE / TJ-AM - 2019) A validação dos requisitos exclui diversas considerações,
entre elas, a
que verifica o impacto da implementação dos requisitos identificados sobre o
orçamento do
sistema.

Comentários:

Nós vimos que durante o processo de validação de requisitos, devem ser realizadas
verificações nos
requisitos do documento de requisitos, que incluem as verificações de realismo:

Verificações de realismo: usando o conhecimento da tecnologia existente, os requisitos
devem ser
verificados quanto a se realmente podem ser implementados. Essas verificações também
devem
levar em consideração o orçamento e o prazo para o desenvolvimento do sistema - caiu
questão
de prova recente sobre isso! Logo, o impacto orçamentário é considerado.

Gabarito: Errado


4O.(CESPE / TJ-AM - 2019) Na gerência de requisitos, as mudanças no documento de
requisitos
devem aumentar as referências a outros documentos e aprimorar a interdependência entre
suas
próprias seções.

Comentários:

Na gerência de requisitos, os requisitos devem ser rastreáveis. Não há nenhuma
obrigação de se
aumentar as referências a outros documentos.

Gabarito: Errado

Item. 41. (CESPE / TJ-AM -2019) Uma especificação de requisitos é inconsistente quando, por
exemplo,
em um de seus subconjuntos conste que o pagamento será feito antes do
fechamento da
compra e, em outro subconjunto, conste que o pagamento será feito depois do fechamento
da
compra.

Comentários:

Perfeito! Isso atenta contra a consistência dos requisitos. Lembrem-se de que requisitos
de devem
ser claros, não-ambíguos, fáceis de entender, completos e consistentes - logo, não
podem ser
ambíguos ou contraditórios.

Gabarito: Correto

Item. 42. (CESPE/TJ-AM-2019) Em um protótipo para validar os requisitos de um software, é
admissível
deixar de fora os requisitos não funcionais ou reduzir seus padrões.

Comentários:

Perfeito! Um protótipo é um modelo ou esboço de funcionalidades, logo é razoável
admitir que
requisitos não funcionais estejam fora de seu escopo assim como uma reduçãço em seus
padrões
de qualidade.

Gabarito: Correto

43-(CESPE / SLU-DF - 2019) A interoperabilidade entre um software que
esteja em
desenvolvimento e outros sistemas existentes é considerada um requisito funcional.

Comentários:

A interoperabilidade é evidentemente um requisito não-funcional, uma vez que
trata de uma
restrição de uma funcionalidade.


Gabarito: Errado

44.(CESPE / STM - 2018) Requisitos de domínio são relativos ao que o sistema deve
fornecer, como
ele deve reagir a entradas específicas e se comportar em determinadas situações,
enquanto os
requisitos funcionais são restrições sobre os serviços ou as funções oferecidas pelo sistema.

Comentários:

Requisitos de Domínio podem ser funcionais ou não-funcionais. Restrições nos serviços ou
funções
oferecidas pelo sistema são Requisitos Não-Funcionais.

Gabarito: Errado

45.(CESPE / STM - 2018) O processo de verificação visa assegurar que o sistema
atende as
expectativas e necessidades do cliente por meio da utilização de técnicas de entrevista
como
brainstorming, grupos focais ou Delft, a partir das quais são extraídos os
requisitos não
funcionais.

Comentários:

Quem visa assegurar que o sistema atenda as expectativas e necessidades do cliente é
o processo
de validação e, não, verificação. Além disso, essas são técnicas de
levantamento de requisitos
(funcionais).

Gabarito: Errado

46.(CESPE/CGM-PB-2018) A atividade de gerência de requisitos é a responsável por
garantir que
mudanças nos requisitos sejam feitas de maneira controlada e documentada, administrando
os
relacionamentos entre os requisitos e as dependências entre o documento de requisitos e
os
demais artefatos produzidos no processo de software.

Comentários:

Galera, que item maravilhoso! É a definição perfeita e impecável da Gerência/Gestão de
Requisitos.
Ele realmente é o responsável por garantir que mudanças nos requisitos sejam feitas de
maneira
controlada e documentada, administrando os relacionamentos entre os
requisitos e as
dependências entre o documento de requisitos e os demais artefatos produzidos no
processo de
software.

Gabarito: Correto


47-(CESPE / ABIN - 2018) Ao se aplicar a rastreabilidade bidirecional, é possível
determinar se
todos os requisitos-fonte foram completamente tratados e se todos os requisitos
do produto
atendem aos requisitos do cliente.

Comentários:

Esse é um conceito trazido pelo livro do Kechi Hirama, que afirma que a
rastreabilidade bidirecional
auxilia a determinar se todos os requisitos fonte foram completamente tratados
e se todos os
requisitos de mais baixo nível podem ser rastreados para uma fonte válida. Eu sei, é
realmente
complicado ficar estudando bibliografias nada consagradas :(

Gabarito: Errado

48.(CESPE / ABIN - 2018) Definir e manter matriz de rastreabilidade dos
requisitos permite
controlar e tratar as mudanças em requisitos durante o processo de elicitação e
especificação
do produto.

Comentários:

Definir e manter matriz de rastreabilidade dos requisitos realmente permite
controlar e tratar as
mudanças em requisitos, no entanto ela ocorre durante a atividade de gerenciamento de
requisitos
e, não, elicitação e especificação de requisitos.

Gabarito: Errado

4g.(CESPE / ABIN - 2018) Para que os requisitos sejam refinados e sejam gerados
modelos de
análise e projeto para codificação, apenas a avaliação e a aprovação por parte do
cliente —
mesmo após o entendimento dos requisitos — não são suficientes.

Comentários:

Cuidado com esse tipo de questão! Ela parece ser referente ao Pressman ou Sommerville,
mas trata
do MPS.BR. O Processo de Gerência de Requisitos (GRE) afirma literalmente que a
avaliação e
aprovação por parte do cliente após o entendimento dos requisitos por si só não é
suficiente para
que os requisitos sejam refinados e refletidos em modelos de análise e projeto para a
codificação

Gabarito: Correto

5o.(CESPE / ABIN - 2018) De acordo com as técnicas facilitadoras de especificação de
aplicação,
recomenda-se que a descrição de requisitos e regras seja feita diretamente pela equipe
técnica,
sem a participação do cliente.

Comentários:


Na verdade, é obrigatória e fundamental a participação do cliente na especificação de requisitos.

Gabarito: Errado

5i.(CESPE / ABIN - 2018) No processo de elicitação de requisitos, há atividades
relacionadas a
identificação, rastreabilidade e mudanças em requisitos.

Comentários:

Na verdade, rastreabilidade e mudança de requisitos são atividades
relacionadas ao
Gerenciamento de Requisitos e, não, Elicitação de Requisitos.

Gabarito: Errado

52.(CESPE / EBSERH - 2018) Na especificação de requisitos, são estabelecidos uma escala
de
medição e os valores aceitáveis para cada requisito de usuário, tornando-o mensurável,
ou seja,
adicionando a ele um critério de aceitação.

Comentários:

No livro Mastering the Requirements Process (Robertson; Robertson, 2006), temos que:
"Assim, na
descrição de requisitos de usuário pode ser suficiente capturar a intenção e depois, na
especificação de
requisitos de sistema, transformar essa intenção em um requisito mensurável, adicionando
a ele um
critério de ajuste. É muito comum que, neste processo, um requisito não funcional de usuário dê
origem
a vários requisitos não funcionais de sistema".

Esse critério de ajuste seria o que a questão chama da escala de medição. No
entanto, essa não é
uma bibliografia consagrada - eu não gosto desse tipo de questão!

Gabarito: Correto

53-(CESPE / EBSERH - 2018) Requisitos externos são derivados de
metas, políticas e
procedimentos das organizações, do cliente e do desenvolvedor e incluem
requisitos de
processo, requisitos de implementação, restrições de entrega e restrições orçamentárias.

Comentários:

Metas, políticas e procedimentos são requisitos organizacionais e, não,
externos. Ademais,
requisitos externos não incluem requisitos de processo, de implementação, de entrega e
restrições
orçamentárias - os requisitos externos são regulatórios, éticos ou legais.

Gabarito: Errado


54-(CESPE / IPHAN - 2018) Tanto a etnografia quanto o protótipo podem ser
utilizados para
validação e elicitação de requisitos, contudo a aplicação de um elimina a possibilidade
de uso do
outro no mesmo cenário, pois se tratam de técnicas excludentes.

Comentários:

Elas não são excludentes - pelo contrário, elas são complementares. A etnografia é
utilizada para
capturar requisitos que o cliente não consegue descrever com clareza; já o protótipo
poderia ser
utilizado para validar os requisitos descobertos na etnografia, por exemplo.

Gabarito: Errado

Item. 55. (CESPE / IPHAN - 2018) A validação de requisitos se sobrepõe à análise de
requisitos, pois tem
a finalidade de encontrar eventuais problemas nos requisitos e
validá-los conforme as
necessidades dos usuários do sistema.

Comentários:

Perfeito! Ela se sobrepõe no sentido de que ela é capaz de descobrir problemas com
requisitos
quanto à ambiguidade, conflitos, contradições, entre outros - mostrando que os
requisitos obtidos
definem realmente o sistema que o usuário necessita. Esta fase sobrepõe à
análise, pois
compreende a descoberta de problemas com os requisitos. A atividade de validação de
requisitos é
fundamental para o processo de engenharia de requisitos porque ela procura diminuir os
custos
com a identificação de erros no documento de requisitos, quando eles são
encontrados apenas na
fase de desenvolvimento do sistema ou quando o sistema já está em operação.

Gabarito: Correto

56.(CESPE / IPHAN - 2018) Situação hipotética: Como forma de obter os requisitos de
apoio para
desenvolver um sistema a ser implementado em determinado setor de uma organização, um
analista propôs que se observasse o trabalho do dia a dia, anotando-se as tarefas
realizadas no
referido setor. Assertiva: Para o cenário proposto, é ideal a utilização da técnica de
caso de uso
alinhada à entrevista.

Comentários:

Observasse 0 trabalho do dia a dia? Anotando as tarefas realizadas no setor? Só pode
estar se
referindo à técnica de etnografia e, não, entrevista.

Gabarito: Errado


57- (CESPE / IPHAN - 2018) Situação hipotética: Na metodologia de desenvolvimento de
software
customizada para uma organização, o analista propôs o uso da prototipação na
fase de
engenharia de requisitos, contudo julgou inviável a utilização da prototipação na fase
de projeto
de sistemas. Assertiva: Nessa situação, a proposta do analista está incorreta, pois a
prototipação
tanto pode ser utilizada no processo de engenharia de requisitos, para ajudar na
elicitação de
requisitos, quanto no projeto de sistema, para apoiar o projeto de interface de usuário.

Comentários:

Vamos lá! O examinador foi bastante descuidado. É possível entender que ele
quis dizer que
realmente é possível utilizar a prototipação tanto na fase de requisitos
quanto de projeto. No
entanto, ele afirma que a proposta do analista está incorreta porque a prototipação
tanto pode ser
utilizada no processo de engenharia de requisitos, para ajudar na elicitação de
requisitos, quanto
no projeto de sistema, para apoiar o projeto de interface de usuário. Ora, não há
nenhuma relação
direta de causalidade. O fato de o analista julgar inviável a utilização da
prototipação na fase de
projeto de sistemas em nenhum momento implica que ele tenha feito essa avaliação por
achar que
não é possível aplicá-la - pode ser por achar que o custo seja alto, seja muito
trabalho, entre outras
possibilidades. Dessa forma, discordo veementemente do gabarito definitivo!

Gabarito: Correto

58.(CESPE / PF-2018) No desenvolvimento de um sistema de informação, a fase de
levantamento
de requisitos consiste em compreender o problema, dando aos desenvolvedores e usuários a
mesma visão do que deve ser construído para resolvê-lo, e a fase de
projeto consiste na
realização da descrição computacional, incluindo a arquitetura do sistema, a
linguagem de
programação utilizada e o sistema gerenciador de banco de dados (SGBD) utilizado.

Comentários:

De fato, a fase de levantamento de requisitos consiste em compreender o problema dando
aos
desenvolvedores e usuários a mesma visão do que deve ser construído. Mesma visão,
Diego? Sim,
aqui visão está sendo utilizando em um sentido amplo como o de um Documento de
Visão. Porfim,
lembrem-se que - no projeto - nós desenhamos a solução para o problema,
já incluindo a
arquitetura do sistema, linguagem de programação, sistema gerenciador de banco de dados, etc.

Gabarito: Correto

59.(CESPE / MPE-PI - 2018) A análise de requisitos consiste na área responsável pela
identificação
das reais necessidades dos clientes de TI. Por meio da análise de requisitos, em
conjunto com o
cliente, é possível construir uma solução que atenda essas necessidades e
desenvolver os
requisitos funcionais elencados.

Comentários:


Questão simples! A análise de requisitos realmente permite identificaras necessidades dos
clientes
e construir uma solução que atenda essas necessidades.

Gabarito: Correto

6o.(CESPE / MPE-PI - 2018) Situação hipotética: Ao se iniciar a especificação de
requisitos de um
software para controlar o gasto de folhas impressas de um setor, o analista
de requisitos,
juntamente com o gestor, definiu um cenário de teste em que, ao se comandar a
impressão, a
chave do usuário autenticado no sistema que comandar uma impressão acionará o contador
de
impressões do setor de locação desse usuário. Assertiva: Nessa situação, o teste
validará o
cenário do requisito definido junto com o gestor.

Comentários:

Perfeito! Lembrem-se de que uma das técnicas de validação de requisitos é a geração
de casos de
teste. Logo, nesse caso, o teste validará o cenário do requisito especificado
inicialmente junto ao
gestor.

Gabarito: Correto

6i.(CESPE / SE-DF - 2017) Para auxiliar na gerência de riscos e prevenir insatisfações
das partes
interessadas, deve-se dificultar as modificações na especificação dos requisitos.

Comentários:

Hahaha... essa questão é engraçada! Como assim, cara? Você vai dificultar as
modificações na
específica dos requisitos do produto de um cliente? Imaginem vocês chegarem em um
pedreiro e
falarem: "Amigão, eu tinha falado que queria essa lâmpada aqui, mas eu mudei de ideia
e agora eu
quero ela ali". E o pedreiro dificultar a modificação que você quer fazer na sua
própria casa. Isso não
faz sentido - você é o cliente! E como isso previne insatisfação das partes interessadas? Com
certeza,
você vai ficar irritadíssimo!

Gabarito: Letra E

Ô2.(CESPE / SE-DF - 2017) Um dos objetivos da engenharia de requisitos é
integrar tarefas,
técnicas, orientações, responsabilidades e papéis em fluxos de trabalho.

Comentários:

Isso foi retirado do livro Engenharia de Requisitos: Software Orientado ao
Negócio, de Carlos
Eduardo Vazquez e Guilherme Siqueira. Segue o trecho: "A Engenharia de Requisitos
facilita a
interação com 0 cliente em termos de identificar e entender suas necessidades e na obtenção de um
acordo da solução que será entregue. Ela descreve e integra tarefas, técnicas,
orientações, papeis
e responsabilidade em fluxos de trabalho que: tem início com o entendimento da
necessidade do
cliente; e passam pelo acordo sobre a solução que será construída".

Galera, vou ser sincero com vocês! Eu errei esse item - achei essa descrição
absurdamente abstrata
e genérica. No entanto, lendo no contexto do livro, faz todo sentido mesmo. Não se
martirizem,
caso tenham errado essa questão :P

Gabarito: Correto

63.(CESPE / SE-DF - 2017) É comum que uma especificação de requisitos inclua as
interfaces
externas do software.

Comentários:

Isso foi retirado do livro Engenharia de Requisitos: Software Orientado ao
Negócio, de Carlos
Eduardo Vazquez e Guilherme Siqueira. Segue o trecho: "Lista de Requisitos Funcionais:
descreve
tarefas e serviços que serão fornecidos pelo sistema aos seus usuários (Exemplo: lista de casos de
uso,
histórias do usuário). Incluir também as interfaces externas do software".

E isso realmente faz todo sentido. A especificação de requisitos deve
contemplar as interfaces
externas do software.

Gabarito: Correto

6/j.(CESPE / TRE-PE - 2017) No contexto da análise de requisitos, confiabilidade e
usabilidade são
atributos de qualidade classificados como:

a) requisitos funcionais.

b) requisitos de domínio.

c) requisitos não funcionais.

d) dependências.

e) regras de negócio.

Comentários:


Requisitos Não-
Funcionais


Requisitos de
Confiabilidade

Requisitos de
Proteção

Requisitos de
Eficiência

Requisitos de
Usabilidade

Requisitos
Ambientais

Requisitos
Operacionais

Requisitos de
Implementação


Requisitos de
Desempenho

Requisitos de
Armazenamento

A questão trata dos requisitos não-funcionais.

Gabarito: Letra C

6s.(CESPE /TCE-PR-2016) Com relação aos requisitos de software, assinale a opção correta.

a) O documento de especificação de requisitos é um documento restrito à
equipe de
desenvolvimento de software.

b) As necessidades do usuário são informações que substituem os requisitos do software.

c) Os requisitos de produto e os requisitos organizacionais são tipos de requisitos funcionais.

d) Os requisitos funcionais descrevem as funcionalidades, os recursos e as
características do
software.

e) Os requisitos não funcionais referem-se diretamente às características do software.

Comentários:

(a) Errado, é um documento que abrange qualquer parte interessada (inclusive,
serve como
contrato); (b) Errado, elas não substituem, na verdade elas substanciam os requisitos
do software;

(c) Errado, na verdade, são requisitos não-funcionais; (d) Correto, eles descrevem
funcionalidades,
recursos e características do software; (e) Errado, esses são os requisitos funcionais.

Gabarito: Letra D

Item. 66. (CESPE / TRT-PR - 2016 - Letra D) Durante a fase de levantamento de requisitos
para a
construção de um software, compete aos desenvolvedores organizaras necessidades em ordem
de prioridade.


Comentários:

Na verdade, não compete aos desenvolvedores - compete aos usuários. Eles devem
organizar a
prioridade das necessidades.

Gabarito: Errado

67.(CESPE / TRT-PR - 2016 - Letra E) O QFD (quality function deployment)
identifica como
requisitos fascinantes os recursos que extrapolam as expectativas dos clientes.

Comentários:

Requisitos Fascinantes são recursos que vão além da expectativa dos clientes e
demonstram ser
muito satisfatórios quando presentes. Por exemplo, o software para um novo
celular vem com
recursos-padrão, mas junto vem um conjunto de capacidades não esperadas.
Exemplos de
Requisitos Fascinantes: tecla multitoque e correio de voz visual.

Gabarito: Correto

Item. 68. CESPE / MPOG-ATI - 2015) Tão logo exista uma versão do documento de
requisitos, o
processo de gerenciamento de requisitos deverá ser iniciado.

Comentários:

O processo de gerenciamento de requisitos deve se iniciar assim que uma
versão inicial do
documento de requisitos esteja disponível, mas o planejamento das mudanças de requisitos
deve
ser iniciado durante o processo de elicitação de requisitos. A evolução de requisitos,
durante o
processo de engenharia de requisitos e após a entrada de um sistema em operação, é
inevitável.
Logo, a questão está corretíssima.

Gabarito: Correto

Item. 69. (CESPE / MPOG-ATI - 2015) As informações de rastreabilidade de requisitos
possibilitam a
realização de estimativa do custo de mudanças em requisitos.

Comentários:

A rastreabilidade permite avaliar impacto e possibilita estimar o custo de mudanças em
requisitos.
Galera, observem que a questão utiliza 'possibilita'. Sempre que a banca faz
isso, ela está te
ajudando, porque para essa questão estar errada, não deveria haver
absolutamente nenhuma
possibilidade de estimar custos de mudanças em requisitos por meio de
informações de
rastreabilidade.


Gabarito: Correto

7o.(CESPE / MPOG-ATI - 2015) As mudanças de requisitos em processos
ágeis de
desenvolvimento não seguem um processo formal de gerenciamento de requisitos.

Comentários:

De fato, as mudanças de requisitos em processos ágeis de desenvolvimento seguem um
processo
mais informal de gerenciamento. Não há, por exemplo, documentação extensa ou
matrizes de
rastreabilidade! Em geral, metodologias ágeis não recomendam a utilização de
processos muito
formais.

Gabarito: Correto

Item. 71. (CESPE / MPOG-ATI - 2015) Para a elicitação dos requisitos, é indicada à empresa
a realização
de um workshop de requisitos, em que seja determinado um facilitador, mesmo que sem
grande
experiência com os processos de gerenciamento de requisitos.

Comentários:

Essa questão foi bastante polêmica! Alguns podem argumentar que não é técnica mais
indicada.
No entanto, a questão não afirma isso, ela apenas afirma que é indicada - e, de
fato, ela é indicada
para elicitação de requisitos. Além disso, conforme eu disse em aula, o facilitador
deve ser neutro e
responsável por atividades de logística, organização, etc.

Muitas vezes, ele não precisa ser sequer um cara da área de tecnologia, pode ser um
cara da área
de gestão de pessoas, porexemplo. Seu papel é facilitar o workshop, mas-similarao Scrum
Master
no contexto de Gestão de Projetos de Desenvolvimento de Software - não precisa ter
nenhuma
experiência específica no gerenciamento de requisitos.

A questão poderia até ser passível de recurso se falasse 'sem experiência alguma', mas
como ela
disse apenas 'sem grande experiência', eu a avalio como correta.

Gabarito: Correto

Item. 72. (CESPE / MPOG-ATI - 2015) Os requisitos não funcionais a serem especificados
estabelecerão
restrições que devem ser seguidas portodo o sistema da referida empresa, podendo até
mesmo
levar à necessidade de definição de requisitos funcionais.

Comentários:

Os requisitos não funcionais estabelecem restrições? Sim! Eles podem levar à necessidade de
definição
de requisitos funcionais? Também! O que a questão quer dizer é que, ao levantar e especificar os
requisitos funcionais, pode-se acabar percebendo a necessidade de se estabelecer novos
requisitos
funcionais (ou modificá-los).

Percebam outro detalhe: a questão afirma "podendo até" - sempre que a questão usar o
verbo
poder, ela já te ajuda! Por que? Porque, para a questão estar errada, não poderia
haver nenhuma
possibilidade de se chegar à requisitos funcionais a partir da especificação
dos requisitos não-
funcionais. Entenderam isso? Caiu de novo a mesma coisa!

Gabarito: Correto

Item. 73. (CESPE / MPOG-ATI - 2015) A definição de um protótipo para a validação dos
requisitos pode
tornar o processo de requisitos mais barato e mais simplificado, já que ele vai
corresponder à
real forma de uso do sistema a ser construído.

Comentários:

De novo, de novo e de novo! Observem que a questão afirma que "pode tornar 0
processo mais
barato e simplificado". E, sim, ele pode tornar o processo mais barato e simplificado.
No entanto, o
protótipo não necessariamente vai corresponder à real forma de uso do sistema a ser
construído.
Na verdade, o protótipo, em geral, é utilizado para validar requisitos de alto nível,
logo ele não vai
contemplar diversas funcionalidades que estarão no sistema real. Pressman afirma:

"Yet, prototyping can be problematicfor thefollowing reasons: 1. Stakeholders see what
appears to be
a working version ofthe software, unaware that the prototype is held together
haphazardly, unaware
that in the rush to get it working you haven't considered overall software
quality or long-term
maintainability. When informed that the product must be rebuilt so that high leveis of
quality can be
maintained, stakeholders cryfoul and demand that "afewfixes"be applied to make the
prototype a
working product. Too often, software development management relents".

Gabarito: Errado

74.(CESPE / MPOG-ATI - 2015) Uma forma de validação dos requisitos é a geração de
casos de
teste para os requisitos documentados.

Comentários:

Existem três técnicas de validação de requisitos: Revisão de Requisitos, Prototipação e
Geração de
Casos de Teste.

Gabarito: Correto


75.(CESPE / MPOG-ATI - 2015) No ciclo de vida do software, o congelamento dos
requisitos do
software garante que este, quando em desenvolvimento, atenda à expectativa do
usuário,
desde que tudo que tenha sido requisitado seja implementado.

Comentários:

Requisitos não são estáticos, são dinâmicos e precisam ser refinados constantemente. O
processo
de definição de requisitos gera um feedback que pode acabar modificando os próprios
requisitos.
Dessa forma, é evidente que o congelamento de requisitos não garante o
atendimento à
expectativa do usuário. Em geral, usuários não sabem o que querem; aqueles que sabem,
mudam
de opinião durante o processo de desenvolvimento de software. Logo, mesmo que tudo que
foi
requisitado tenha sido implementado, pode não atenderás expectativas do usuário, tendo
em vista
que, logo após o congelamento dos requisitos, o usuário pode muito bem querer modificá-lo.

Gabarito: Errado

76.(CESPE/ STJ - 2015) Os requisitos ambientais, operacionais e de
desenvolvimento são
organizacionais e não funcionais.

Comentários:

Requisitos Não-
Funcionais


Requisitos de
Confiabilidade

Requisitos de
Proteção

Requisitos de
Eficiência

Requisitos de
Usabilidade

Requisitos
Ambientais

Requisitos
Operacionais

Requisitos de
Implementação


Requisitos de
Desempenho

Requisitos de
Armazenamento


Requisitos
Regulatórios

Requisitos
Legais

Requisitos
Éticos

Bastava lembrar da parte superior direita do quadrinho!

Gabarito: Correto

Item. 77. (CESPE / STJ - 2015) Os requisitos reguladores, legais e éticos são externos e não
funcionais.

Comentários:


Requisitos Não-
Funcionais

Requisitos de
Produtos


Requisitos de
Confiabilidade

Requisitos de
Proteção

Requisitos de

Requisitos de
Usabilidade

Requisitos
Ambientais

Requisitos
Operacionais

Requisitos de
Implementação


Requisitos de
Desempenho

Requisitos de
Armazenamento

Requisitos
Externos

Bastava lembrar da parte inferior do quadrinho! No entanto, vamos tentar resolver por
lógica? Faz
sentido pensar em requisitos reguladores, legais e éticos como externos? Sim! E eles são funcionais
ou
não funcionais? Ora, não-funcionais. Logo, era possível matara questão!

Gabarito: Correto

78.(CESPE / TJDFT- 2015) O uso de protótipo auxilia a descoberta e a validação dos
requisitos de
software.

Comentários:

Perfeito! A prototipação é uma técnica tanto de Elicitação de Requisitos quanto a
Validação de
Requisitos.

Gabarito: Correto

7g.(CESPE / TJDFT - 2015) As técnicas de elicitação e especificação de
requisitos incluem a
etnografia, a qual é utilizada para compreender os requisitos sociais e
organizacionais para
determinado projeto.

Comentários:

Na verdade, o correto seria: as técnicas de elicitação e especificação análise de
requisitos incluem a
etnografia, a qual é utilizada para compreender os requisitos sociais e
organizacionais para
determinado projeto. A banca considerou a questão como correta - não entendo o porquê!

Gabarito: Correto

8o.(CESPE / TJDFT - 2015) É caracterizada como requisito funcional a
exigência de que, em
determinado projeto, o software desenvolvido funcione no sistema operacional Linux, uma
vez
que essa exigência está diretamente ligada ao software.


Comentários:

Trata-se de um requisito não-funcional. Por que? Porque funcionar no Sistema Operacional
Linux
não trata de uma funcionalidade em si, mas uma restrição aos serviços oferecidos.

Gabarito: Errado

8i.(CESPE / MPU - 2013) As atividades do gerenciamento de requisitos incluem a análise
e a
negociação, a qual visa garantir que todos os requisitos do sistema tenham sido
declarados de
modo não ambíguo, sem inconsistências, omissões e erros.

Comentários:

Galera, olhem a bagunça! De acordo com Sommerville, a Análise (junto com a Elicitação)
é uma
fase da Engenharia de Requisitos. De acordo com Pressman, a Negociação é
uma fase da
Engenharia de Requisitos. Nenhuma das duas é atividade do Gerenciamento de Requisitos,
que
também é uma fase da Engenharia de Requisitos (de acordo com Sommerville). Para piorar
tudo,
quem visa garantir que todos os requisitos tenham sido declarados de modo não ambíguo,
sem
inconsistências, omissões e erros, é a Validação de Requisitos. Então, está tudo errado!

Gabarito: Letra E

82.(CESPE / MPE-PI - 2012) Identificada facilidade do cliente em entender uma
especificação
matemática, é correto utilizar, também, na especificação dos requisitos, notações
baseadas em
máquinas de estado finito, uma vez que elas podem reduzir a ambiguidade de um
documento
de requisitos.

Comentários:

Bem, se o cliente tem facilidade em entender uma especificação matemática, notações
baseadas
em máquinas de estado finito serão bastante intuitivas, uma vez que são bastante
formais. Para
quem não sabe, as máquinas são modelos utilizados para representar diversas situações
(Ex: uma
lâmpada ligada ou desligada).

Gabarito: Correto

83-(CESPE / EBC - 2011) No processo de construção e (ou) manutenção de um
produto de
software, o termo requisito pode ser definido da seguinte forma: uma condição,
característica
ou capacidade, determinada no universo das necessidades do negócio do usuário, que deve
ser
atendida por um software na forma de aspectos funcionais e não funcionais.

Comentários:


Trata-se de uma boa definição de requisitos. Ele realmente é uma condição,
característica ou
capacidade, determinada no universo das necessidades do negócio do usuário, que
deve ser
atendida por um software na forma de aspectos funcionais e não funcionais.

Gabarito: Correto

84.CESPE / EBC - 2011) O principal artefato elaborado no processo de produção de
requisitos do
sistema, segundo a ER, é o documento de requisitos. Por sua vez, o documento de
requisitos é
uma declaração formal dos requisitos para os stakeholders, que podem ser clientes,
usuários
finais ou a equipe de desenvolvimento do software.

Comentários:

Perfeito! Stakeholders são as partes interessadas, dentre elas há os clientes, usuários
finais e a
própria equipe de desenvolvimento.

Gabarito: Correto

85.(CESPE / BRB - 2011) O levantamento de requisitos de software privilegia
a visão do
desenvolvedor em relação aos requisitos de um produto. Já a análise dos requisitos
prioriza a
visão que o cliente e os usuários têm dos requisitos de um produto.

Comentários:

Vejam as pegadinhas do CESPE - está invertido! O Levantamento de Requisitos
evidentemente
privilegia a visão do usuário/cliente; por outro lado, a Análise de Requisitos
privilegia a visão do
desenvolvedor.

Gabarito: Errado

Item. 86. (CESPE / FUB - 2011) A etnografia, uma técnica de levantamento de
requisitos, é uma
abordagem completa para elicitação, utilizada para compreender os
requisitos sociais e
organizacionais e que identifica novas características a serem acrescentadas em um sistema.

Comentários:

Na verdade, ela não apresenta uma abordagem completa! Em geral, essa é uma técnica
utilizada
em conjunto com outras técnicas. Como ela é uma técnica de observação, isoladamente
ela não é
muito eficaz na elicitação.

Gabarito: Errado


Item. 87. (CESPE/ EBC-2011) Uma das principais técnicas de verificação é a prototipação. Um
protótipo
é um produto parcialmente desenvolvido, que possibilita aos clientes e
desenvolvedores
examinarem certos aspectos do sistema proposto e decidir se eles são ou não
apropriados ou
adequados para o produto acabado.

Comentários:

A prototipação é uma técnica de validação de requisitos e, não, verificação de requisitos.

Gabarito: Errado

Item. 88. (CESPE / TJ-ES - 2011) Assim como o software, os requisitos também devem ser
avaliados
quanto à qualidade. A validação, atividade da engenharia de requisitos, é
responsável por
garantir que os requisitos tenham sido declarados de forma clara e precisa.
Além disso, a
validação busca detectar inconsistências, erros e omissões, objetivando alinhar os
requisitos às
normas estabelecidas para o projeto, produto e processo.

Comentários:

Os produtos de trabalho criados como consequência da engenharia de requisitos realmente
devem
ser validados quanto à qualidade durante o passo de validação de requisitos.
Esta validação
examina a especificação para garantir que todos os requisitos do sistema foram
estruturados de
maneira não ambígua, que as inconsistências, omissões e erros foram apagados e
corrigidos, e que
os produtos de trabalho estão em conformidade com os padrões estabelecidos para o
processo,
para o projeto e para o produto. Logo, questão perfeita!

Gabarito: Correto

Item. 89. (CESPE / STM - 2011) São consideradas técnicas de validação de requisitos:
revisões de
requisitos, prototipação e geração de casos de teste.

Comentários:

De fato, durante a validação de requisitos, uma série de técnicas pode ser utilizada,
tais como:
Revisão de Requisitos, Prototipação e Geração de Casos de Teste.

Gabarito: Correto

90.(CESPE / TJ-ES - 2011) Verificação e validação são atividades da análise
de software,
necessárias para se identificar o que o software precisa executar, seguida de uma
avaliação do
usuário quanto às atividades definidas.

Comentários:


Vamos por partes: de fato, são atividades da análise de software (eu disse análise de
software e,
não, requisitos). Ela faz parte da Engenharia de Requisitos, que busca entender o que
o software
precisa executar e de uma posterior avaliação do usuário. A redação da questão está
bem confusa,
pois dá a entender que a verificação identifica o que o software precisa executar.

Gabarito: Correto

9i.(CESPE / MEC - 2011) A rastreabilidade de requisitos ocorre apenas na
relação entre os
requisitos propriamente ditos e os artefatos ou subprodutos de desenvolvimento gerados.

Comentários:

A rastreabilidade é a propriedade de uma especificação de requisitos que reflete a
facilidade de
encontrar os requisitos relacionados. Ela é frequentemente representada por meio de
matrizes de
rastreabilidade que relacionam os requisitos aos stakeholders, aos outros requisitos, aos
módulos
de projeto, aos artefatos ou subprodutos, etc. Para responder à questão, bastava
lembrar que os
requisitos se relacionam também entre si.

Gabarito: Errado

92.CESPE / ABIN - 2010) Requisitos não funcionais são restrições sobre os serviços ou
as funções
oferecidas pelo sistema, e podem ser, também, declarações de serviços que o sistema
deve
fornecer, como o sistema deve reagir a entradas específicas e como deve comportar-se em
diversas situações.

Comentários:

A segunda parte da questão está incorreta! Na verdade, declarações de serviços que o
sistema deve
fornecer, como o sistema deve reagir a entradas específicas e como deve comportar-se
em diversas
situações, trata-se de requisitos funcionais.

Gabarito: Errado

93-(CESPE / MPU - 2010) Os requisitos normativos, geralmente oriundos da análise das
regras de
negócio a que está submetido um sistema, nunca podem ser considerados requisitos
funcionais,
por estarem fora do sistema, ou seja, do domínio do negócio.

Comentários:


Requisitos Não-
Funcionais


Requisitos de
Confiabilidade

Requisitos de
Proteção

Requisitos de
Eficiência

Requisitos de
Usabilidade

Requisitos
Ambientais

Requisitos
Operacionais

Requisitos de
Implementação


Requisitos de
Desempenho

Requisitos de
Armazenamento

Bem, a questão disse que nunca pode ser considerado um requisito funcional. De fato,
geralmente
ele é um requisito não-funcional (como podemos ver na imagem), mas pode haver casos
em que
esse requisito normativo faça parte do domínio do negócio e deva ser implementado como
uma
funcionalidade. Vamos pensar em um exemplo? Um software de RH de um órgão público deve
implementar funcionalidades de acordo com a Lei 8.112/90. Nesse caso, trata-se de um
requisito
tanto funcional quanto não-funcional (depende do ponto de vista).

Gabarito: Errado

94.(CESPE / ABIN - 2010) Se os requisitos forem organizados de acordo com os diversos
pontos
de vista relativos a grupos de usuários do sistema, é possível identificar aqueles
comuns a todos
ou à maioria dos pontos de vista. Esses requisitos comuns podem estar relacionados a
assuntos
separados, implementados como extensões da funcionalidade central.

Comentários:

Essa não precisava nem saber o conteúdo. Como requisitos comuns podem ser implementados
como
extensões dafuncionalidade central? Se são requisitos comuns, devem fazer parte da
funcionalidade
central! Logo, não faz sequer sentido!

Gabarito: Errado

95.(CESPE / MPU - 2010) O levantamento de requisitos é realizado ao final da primeira
versão de
um protótipo, para se definir, junto aos envolvidos no processo, quais são as
premissas básicas
para o início do entendimento das funcionalidades desejadas.

Comentários:

Essa questão não faz sentido, uma vez que-para se fazer um protótipo-é necessário
levantar uma
certa quantidade de requisitos! Como se pode começar a levantar requisitos no final da
primeira
versão do protótipo?Também não faz sentido!


Gabarito: Errado

Item. 96. (CESPE / MPU - 2010) Embora a criação de uma sequência ilustrada de telas
por meio de
programas de desenho gráfico seja útil para a identificação de alguns requisitos do
software, ela
não é considerada uma atividade de prototipação por não envolver o uso de uma
linguagem de
programação.

Comentários:

Na verdade, a identificação de requisitos é independente de linguagem de programação.
Logo, essa
sequência ilustrada de telas por meio de programas pode - sim - ser considerada uma
atividade de
prototipação!

Gabarito: Errado

97.(CESPE / DETRAN-ES - 2010) A técnica de brainstorm é adequada para a
produção de
especificações de requisitos para um sistema de informação em desenvolvimento.

Comentários:

A técnica de brainstorm é adequada para a elicitação ou levantamento de requisitos e,
não, para a
especificação de requisitos.

Gabarito: Errado

Item. 98. (CESPE / MPU - 2010) A verificação de requisitos tem por objetivo analisar se os
modelos
construídos estão de acordo com os requisitos definidos. Por sua vez, a validação de
requisitos
visa assegurar que as necessidades do cliente estão sendo atendidas portais requisitos.

Comentários:

A diferença entre Verificação e Validação de Requisitos é, em geral, ignorada em
prova-ambos são
chamados apenas de Validação de Requisitos. No entanto, via de regra, a verificação de
requisitos
tem o objetivo de descobrir se os requisitos são claros, precisos, completos e
consistentes, e tem
por objetivo analisar se os modelos construídos estão de acordo com os requisitos definidos.

Já a Validação de Requisitos se ocupa em mostrar que os requisitos realmente definem
o sistema
que o cliente deseja, isto é, visa assegurar que as necessidades do cliente estão
sendo atendidas por
tais requisitos. Logo, questão perfeita!

Gabarito: Correto


Item. 99. (CESPE / TCU - 2010) Por se tratar de função essencial da engenharia de requisitos, a
gestão
formal de requisitos é indispensável mesmo para projetos de pequeno porte, com apenas
duas
ou três dezenas de requisitos identificáveis.

Comentários:

A gestão formal de requisitos é iniciada somente para grandes projetos. Para pequenos
projetos,
essa função de engenharia de requisitos é consideravelmente menos formal e,
muitas vezes,
dispensável.

Gabarito: Errado

Item. 100. (CESPE / DETRAN-DF - 2009) Requisitos funcionais são restrições sobre as
funções ou
serviços oferecidos pelo sistema. Esses requisitos consideram as declarações de
serviços, a
forma do sistema reagir e como ele deve se comportar em determinadas situações.
Cenários e
casos de uso são técnicas eficazes para elicitação de requisitos funcionais segundo
pontos de
vista de interação.

Comentários:

A questão fez uma mistureba! Requisitos não-funcionais são restrições sobre as funções
ou serviços
oferecidos pelo sistema.

Gabarito: Errado

Item. 101. (CESPE / IPEA - 2009) Elicitação envolve a identificação sistemática de
requisitos nem
sempre explicitados pelos clientes. Protótipos, pesquisas estruturadas, testes-beta,
análise de
casos de negócio, walkthroughs, QFD, grupos de trabalho são exemplos de técnicas
utilizadas
para elicitar necessidades, expectativas, restrições e interfaces dos stakeholders para
todas as
fases do ciclo de vida do produto.

Comentários:

A definição de elicitação de requisitos está correta - lembrem-se da técnica de
etnografia, utilizada
para elicitar requisitos implícitos. Um aluno já me perguntou: "Professor, Testes-beta
também?". De
fato, não é nada usual! No entanto, imaginemos a realização de um Teste-beta (aquele
que ocorre
no ambiente real de utilização do usuário) e descobrimos um problema.

Esse problema pode se transformar em um novo requisito, concordam? Portanto, eu posso
utilizá-lo
como uma técnica para descobrir novos requisitos. Porém, é preciso ter aquela
experiência de
concurseiro (adquirida quando se faz várias questões e provas) para saber quando esse
é o foco da
questão e quando não é! Nesse caso, não era o foco da questão.


Gabarito: Correto

Item. 102. (CESPE / TCE-RN - 2009) A etnografia é uma técnica utilizada para a
descoberta de
requisitos de sistemas de software na qual, por meio de observações, procura-se
compreender
os requisitos sociais e organizacionais do ambiente onde o sistema será usado.

Comentários:

Essa é realmente a função da técnica de etnografia. Em geral, essa é uma técnica
utilizada em
conjunto com outras técnicas. Como ela é uma técnica de observação, isoladamente ela
não é
muito eficaz na elicitação.

Gabarito: Correto

Item. 103. (CESPE/IPEA-2009) A política organizacional para o planejamento e execução do
processo
de gerenciamento de requisitos reflete as expectativas organizacionais para
processos de
gestão de requisitos e para que seja possível identificar inconsistências entre os
requisitos e os
planos do projeto.

Comentários:

A gestão ou gerenciamento de requisitos permite identificar inconsistências entre o
projeto inicial
e os requisitos. Ele é o processo responsável por compreender, acompanhar e
controlar as
mudanças dos requisitos de sistema, identificando inconsistências.

Gabarito: Correto

Item. 104. (CESPE / STJ - 2008) Os requisitos de um sistema podem ser
descrições dos serviços
fornecidos ou restrições operacionais. Requisitos podem ainda ser
classificados como
funcionais, não funcionais, ou de domínio. A engenharia de requisitos visa compreender
e definir
os requisitos. Um processo de engenharia de requisitos pode envolver o estudo de
viabilidade,
a análise, a especificação e a validação de requisitos.

Comentários:

Vejam que o início é idêntico ao da questão anterior! Sim, algumas bancas copiam
outras bancas e
algumas bancas copiam a si mesmas. Tudo correto na questão...

Gabarito: Correto

Item. 105. (CESPE / SERPRO - 2008) O levantamento de requisitos é importante,
porém não é
fundamental, pois recomenda-se avançar o quanto antes para as demais atividades
que
permitam uma visualização do software e reduzam a ansiedade do cliente em ver algo pronto.


Comentários:

Galera, podem rir à vontade! Essa questão é hilária... não é fundamental? O
Levantamento de
Requisitos é importante, fundamental, essencial, básico, determinante,
substancial, crucial e
indispensável e vários outros sinônimos.

Gabarito: Errado

Item. 106. CESPE / MPE-RR- 2008) Os requisitos de um sistema são descrições dos serviços
fornecidos
pelo sistema e suas restrições operacionais. O processo de descobrir, analisar,
documentar e
verificar esses serviços e restrições é denominado engenharia de requisitos. Requisitos
de um
sistema de software podem ser funcionais, não funcionais ou de domínio.

Comentários:

Questão muito bem escrita! A definição de requisitos está correta, a definição de
engenharia de
requisitos está correta e a classificação de requisitos também está correta.

Gabarito: Correto

Item. 107. (CESPE / MPU - 2007) A especificação de requisitos permite, em determinado
momento,
revelar o que o sistema irá realizar no que se refere às funcionalidades, sem
definir, nesse
momento, como as funcionalidades serão implementadas.

Comentários:

Ela realmente não revela como asfuncionalidades serão implementadas, este tipo de
requisito deve
simplesmente definir o que o sistema deve fazer e não como ele deve ser implementado,
ou seja,
os requisitos de sistema devem simplesmente descrever o comportamento externo do sistema
e
suas restrições operacionais.

Gabarito: Correto

Item. 108. (CESPE / MPU - 2007) Na validação de requisitos — parte integrante da
especificação
desses requisitos —, é correto o uso de diagramas da UML, tais como diagrama de
classes, de
casos de uso e de interação.

Comentários:

Galera, questão um pouco polêmica! Por que? Porque a Validação de Requisitos não é
parte da
Especificação de Requisitos - são fases distintas. De todo modo, a questão foi dada
como certa!
Outra parte que gera alguma dúvida é dizerque é correta a utilização de diagramas da UML! Alguns
afirmam que não faz sentido o uso de Diagramas de Classes na validação de requisitos.
Galera, de
fato, o Diagrama de Casos de Uso é o mais adequado, mas não há nada de incorreto
utilizartambém
o Diagrama de Classes para auxiliar na validação junto ao cliente.

Gabarito: Correto

Item. 109. (CESPE / SERPRO - 2005) O gerenciamento de requisitos inclui, entre outras, as
seguintes
atividades: levantar, analisar, especificar, validar e prototipar requisitos
funcionais e não-
funcionais.

Comentários:

A questão trata claramente de engenharia de requisitos e, não, de gerenciamento de
requisitos. Eu
não sei se não entraram com recurso contra essa questão ou se entraram e o CESPE o
ignorou. O
fato é que essa questão é absurdamente errada, mas o gabarito foi mantido como correto.

Gabarito: Correto

Item. 110. (CESPE / SERPRO - 2005) Uma das principais atividades relacionadas à
engenharia de
software é o levantamento dos requisitos. Nesse contexto, foi introduzida, na década de
80 do
século XX, uma técnica de entrevista conhecida como JAD (Joint Application Development),
que
consistia em uma rápida entrevista e um processo acelerado de coleta de dados em que
todos
os principais usuários e o pessoal da análise de sistemas agrupavam-se em uma única e
intensiva
reunião.

Comentários:

Galera, eu não sei porque essa questão foi dada como certa! JAD não consiste em uma
rápida
entrevista, mas em uma intensa reunião. Ademais, não se trata necessariamente de uma
única
reunião. Acredito que caberia recurso!

Gabarito: Correto

Item. 111. (CESPE / AGE-ES - 2004) A engenharia de requisitos fornece mecanismos que
permitem
entender e analisar a necessidade de o cliente avaliar a exequibilidade, negociar uma
solução
razoável e especificá-la de maneira não-ambígua, validar a especificação e
administrar os
requisitos.

Comentários:

Galera, discordo dessa questão! A redação dela é extremamente confusa -ela diz que o
cliente deve
avaliar a exequibilidade. Uma redação correta seria: A engenharia de requisitos fornece
mecanismos
que permitem entender e analisar a necessidade do cliente, avaliar a exequibilidade, negociar uma
solução razoável e especificá-la de maneira não-ambígua, validar a especificação e
administrar os
requisitos. Contudo, o CESPE considerou-a como correta.

Gabarito: Correto

Item. 112. (CESPE / Prefeitura de Boa Vista - 2004) Requisitos adequadamente definidos
constituem
base importante sobre a qual um sistema poderá ser bem desenvolvido. No
processo de
engenharia de requisitos, o estudo de viabilidade utiliza as informações do
processo de
levantamento de requisitos para gerar um relatório que recomenda se é viável ou não
realizar o
processo de desenvolvimento do sistema.

Comentários:

Opa... calma aí! Estudo de Viabilidade vem antes do processo de Levantamento de
Requisitos.

Como ele poderia utilizar as informações do processo de levantamento de requisitos? Impossível!

Gabarito: Errado

Item. 113. (CESPE / COHAB - 2004) O QFD (Quality Function Deployment) tem uma
abordagem
embasada na criação de uma equipe formada por clientes e desenvolvedores, que trabalham
juntos para identificar o problema, propor elementos da solução,
negociar diferentes
abordagens e especificar um conjunto de requisitos da solução.

Comentários:

Essa questão foi retirada do Pressman:

"O levantamento de requisitos (também chamado elicitação de requisitos) combina elementos
de
solução de problemas, elaboração, negociação e especificação. Para estimular uma
abordagem
colaborativa e orientada a equipes em relação ao levantamento de requisitos, os
envolvidos trabalham
juntos para identificar o problema, propor elementos de solução, negociar diferentes
abordagens e
especificar um conjunto preliminar de requisitos de solução".

No livro, o autor cita algumas abordagens de levantamento de requisitos, tais
como: Coleta
Colaborativa de Requisitos e o QFD. A questão trata da primeira abordagem e, não, da
segunda -
e, por isso, está errada.

Gabarito: Errado

Item. 114. (CESPE / COHAB - 2004) As atividades de análise de requisitos resultam na
especificação
das características operacionais do software, na indicação da interface do software com
outros
elementos do sistema e no estabelecimento de restrições que o software deve satisfazer.


Comentários:

Essa questão foi retirada do Pressman:

"A Análise de Requisitos resulta na especificação das características operacionais do
software, indica
a interface do software com outros elementos do sistema e estabelece restrições a que o software
deve
atender. Permite ainda que você amplie os requisitos básicos estabelecidos durante as
tarefas de
concepção, levantamento e negociação, que são parte da engenharia de requisitos".

Logo, está perfeita! Atentem-se: a Análise de Requisitos é bastante semelhante à
Elaboração, ou
seja, expansão, refinamento e detalhamento de requisitos - sob a perspectiva do
desenvolvedor e,
não, do usuário.

Gabarito: Correto

Item. 115. (CESPE / COHAB - 2004) À medida que os requisitos são elucidados, o analista de
software
pode criar um conjunto de cenários, ou seja, casos de uso, que identificam uma linha
de uso para
o sistema a ser construído.

Comentários:

Questão linda! Pode-se modelar os requisitos de um sistema por meio da técnica de
casos de uso
(lembrando que um cenário é um conjunto de casos de uso).

Gabarito: Correto


QUESTõES CoMENTADAS - FCC

í. (FCC / SEFAZ-AP - 2022) Considere as seguintes especificações de requisitos de software:

I. O sistema deve calcular a dívida do contribuinte aplicando a alíquota de 15%
quando o lucro
ultrapassar o teto de contribuição.

II. O tempo de resposta da consulta à dívida ativa da empresa não deve ultrapassar os 13
ms em
situações normais de processamento.

III. O SLA (Acordo de Nível de Serviço) com o contribuinte consulente deve prever
jornada de 24
horas/dia x 7 dias por semana.

IV. A tela de consulta à dívida ativa só pode ser acessada mediante login e senha
corretos
correspondentes àqueles designados ao CNPJ do contribuinte consulente.

Esses requisitos são, correta e respectivamente, dos tipos
a) funcional, técnico, de usuário e não funcional.

b) funcional, não funcional, não funcional e funcional.

c) funcional, técnico, de sistema e não funcional.

d) não funcional, não funcional, técnico e de sistema.

e) não funcional, de usuário, técnico e funcional.

Comentários:

(I) Requisito Funcional, dado que representa uma funcionalidade do sistema; (II)
Requisito Não
Funcional, dado que se trata de uma restrição a uma funcionalidade do sistema
relacionada ao
tempo de resposta; (III) Requisito Não Funcional, dado que se trata de uma
restrição a uma
funcionalidade do sistema relacionada ao acordo de nível de serviço; (IV) Requisito
Funcional, dado
que se trata de uma funcionalidade do sistema.

Gabarito: Letra B

Item. 2. (FCC/ AL-AP - 2020) Considere a lista abaixo, elaborada durante um
levantamento de
requisitos na Assembleia Legislativa do Amapá, para um sistema hipotético de
avaliações
internas:

Item. 1. Registrar avaliação de colaborador por parlamentar: O sistema deve permitir ao
parlamentar,
em uma única tela, a avaliação de todos os seus colaboradores.


Item. 2. Considerar Aspectos Legais: O sistema deve seguir orientações elencadas na
Resolução
ogg/XXXX do Conselho Legislativo do Estado.

Item. 3. Registrar autoavaliação de parlamentar: O sistema deve permitir ao
parlamentar sua
autoavaliação em relação às disposições legais sob as quais atuou no período.

Item. 4. Atentar à Segurança: O sistema deve fornecer mecanismos de segurança e autenticação
alinhados com os adotados pelo processo XPTO.

Item. 5. Impedir acesso direto ao processo XPTO: O sistema deverá mostrar ao usuário que
existem
formulários de avaliação a serem respondidos e dará a opção de respondê-los depois.

Adotando RFU para requisitos funcionais e RNF para não-funcionais, a classificação
correta e
respectiva da lista ias acima é:

a) RFU, RFU, RFU, RNF e RNF.

b) RFU, RNF, RFU, RNF e RNF.

c) RFU, RNF, RFU, RNF e RFU.

d) RNF, RNF, RFU, RNF e RFU.

e) RNF, RFU, RFU, RNF e RNF.

Comentários:

(1) Trata-se de um requisito funcional pois descreve o que o sistema deve fazer
(RFU); (2) Trata-se
de um requisito não-funcional, mais especificamente um Requisito Externo,
relacionado a um
aspecto legal, que deve ser seguido (RNF); (3) Trata-se de um requisito funcional pois
descreve o
que o sistema deve fazer (RFU); (4) Trata-se de um requisito não-funcional
pois descreve um
comportamento do produto. Além disso, também pode ser classificado como um
Requisito de
Produto (RNF); (5) Trata-se de um requisito funcional pois descreve o que o sistema
deve fazer;
(RFU).

Gabarito: Letra C

Item. 3. (FCC / TRT-19 - 2019) A Engenharia de Requisitos utiliza algumas técnicas que
apoiam as
atividades de levantamento de requisitos, sendo a entrevista uma das mais
utilizadas. Uma
entrevista pode ser estruturada de formas diferentes, como na estrutura em:

a) diamante, que envolve sessões de workshop com os usuários os quais assumem papéis
de
documentadores, escrevendo os requisitos em flipcharts.

b) brainstorming, em que inicia-se com perguntas mais genéricas sobre o sistema e
finaliza-se
com perguntas mais específicas, sendo geralmente utilizada com usuários que desconhecem o
assunto.


c) funil, na qual procura-se manter o usuário interessado no assunto e para isto
utilizam-se
perguntas variadas sobre o sistema, sorteadas com um dado.

d) diamante, na qual os usuários escrevem os requisitos em papel, todos ao mesmo
tempo, em
uma tempestade de ideias, para estimular requisitos criativos.

e) pirâmide, em que inicia-se com perguntas mais específicas sobre o sistema e
finaliza-se com
perguntas mais genéricas, sendo geralmente utilizada com usuários mais relutantes.

Comentários:

(a) Errado, isso está mais próximo da técnica de Interpretação de Papeis; (b) Errado,
essa técnica
não é uma estrutura de entrevista e essa descrição trata claramente da estrutura em
diamante,
porque começa com perguntas mais genéricas e termina com perguntas mais
específicas; (c)
Errado, essa não é a descrição de uma entrevista do tipo funil, essa é a descrição
de uma entrevista
não estruturada; (d) Errado, essa não é a descrição de uma entrevista do tipo
diamante, essa é uma
descrição da técnica de brainstorming; (e) Correto, basta lembrar do formato da
pirâmide. Inicia-se
com perguntas mais específicas e termina com perguntas mais genéricas.

Gabarito: Letra E

Item. 4. (FCC / AFAP - 2019) Um Analista de Informática levantou os requisitos para
desenvolver um
sistema de gestão. Dentre os requisitos levantados,

I. o sistema deve apresentar a tela de login e senha antes de cada transação e validar o acesso
com base nas políticas de segurança organizacional.

II. o sistema deve estar disponível para a diretoria em tempo integral, ou seja, 24 x 7.

III. o tempo de resposta de uma consulta da alta administração não pode
exceder a 5
milissegundos.

IV. cada Diretor que usa o sistema deve ser identificado apenas por sua matrícula de
cinco
dígitos seguidos do código de segurança.

V. o sistema deverá gravar um log de autenticação a cada transação completada,
contendo a
identificação do usuário, data e equipamento utilizado.

VI. os backups do sistema deverão ser feitos diariamente a fim de evitar a eventual
perda de
dados sem capacidade de recuperação.

Contêm um requisito funcional e um requisito não funcional, respectivamente, APENAS os itens
a) II e I.

b) Vel.

c) IV e VI.

d) lie III.

e) VI eV.

Comentários:

Lembremos que os requisitos funcionais especificam o que o software deve fornecer, como
deve
reagir a entradas específicas e como se comportar em determinadas situações. Já os
requisitos não
funcionais são restrições aos serviços ou funções oferecidas pelo software (exemplos:
desempenho,
confiabilidade, segurança, processo de desenvolvimento, etc).

(I) Requisito Funcional, visto que se trata de uma funcionalidade ou serviço oferecido pelo
sistema;

(II) Requisito Não-Funcional, visto que se trata de uma restrição de uma funcionalidade
do sistema
em relação a sua disponibilidade;

(III) Requisito Não-Funcional, visto que se trata de uma restrição de uma
funcionalidade do sistema
em relação ao tempo de resposta;

(IV) Requisito Funcional, visto que se trata de uma funcionalidade ou serviço oferecido pelo
sistema;

(V) Requisito Não-Funcional, visto que se trata de uma restrição de uma funcionalidade
do sistema
em relação à auditoria e segurança;

(VI) Requisito Não-Funcional, visto que se trata de uma restrição de uma funcionalidade
do sistema
em relação à integridade e segurança.

Gabarito: Letra C

Item. 5. (FCC / TRF4 - 2019) Suponha que um Analista de TI, participando da etapa de
análise de
requisitos de um sistema de emissão de certidão negativa para o TRF4, tenha elencado
os
requisitos apresentados abaixo:

Item. 1. Utilizar interface responsiva para que possa ser executado em dispositivos móveis e na web.

Item. 2. Validar o tipo de certidão solicitado.

Item. 3. Emitir certidão negativa após verificação de situação do requerente.

Item. 4. Solicitar o CPF do requerente.

Item. 5. Responder ao clique único do usuário em qualquer botão da interface.

Item. 6. Validar o CPF do requerente.

Item. 7. Restaurar os dados automaticamente após falhas não programadas.


Item. 8. Solicitar o nome do requerente.

Item. 9. Oferecer dois tipos de certidão: para fins gerais e para fins eleitorais.

Item. 10. Emitir aviso de impossibilidade de emissão da certidão.

Sobre os requisitos, é correto afirmar que:

a) todos são funcionais.

b) todos são não funcionais.

c) 1, 5 e 7 são não funcionais.

d) apenas 3, 4, 8, 9 e 10 são funcionais.

e) apenas 2, 6 e 7 são não funcionais.

Comentários:

(l) RNF; (2) RF; (3) RF; (4) RF; (5) RNF; (6) RF; (7) RNF; (8) RF; (9) RF; (10) RF.

Gabarito: Letra C

Item. 6. (FCC / SAMASA Campinas - 2019) O diagrama faz referência à QFD -

a) Quality Function Deployment, uma técnica da gestão de qualidade
que traduz as
necessidades do cliente para requisitos de software, buscando maximizar a sua satisfação.

b) Questionário de Funcionalidades para Desenvolvimento, uma técnica para
priorização de
requisitos que facilita a criação de casos de uso.


c) Questionnaire For Diagram, uma lista de perguntas que ajudam a entender
melhor o
problema e permitem que o cliente expresse os requisitos essenciais para a criação de
diagramas
de caso de uso.

d) Quality Function Development, uma técnica para priorização de requisitos,
especializada
para a criação de casos de uso.

e) Questionário de Funcionalidades para Desenvolvimento, uma técnica da gestão de
qualidade
que traduz as necessidades do cliente para as funcionalidades a serem
incorporadas no
software.

Comentários:

QFD é a sigla para Quality Function Deployment - técnica da gestão de qualidade que
traduz as
necessidades do cliente para requisitos de software, buscando maximizar a sua satisfação.

Gabarito: Letra A

Item. 7. (FCC / SEFAZ-BA - 2019) Um profissional da área administrativa de certa
instituição recebeu
um Analista de Sistemas que estava fazendo o levantamento de requisitos para a
construção de
um novo software. Ao informar ao Analista um requisito não funcional para seu
departamento,
o profissional corretamente disse que:

a) a resposta a uma consulta de dados deveria durar no máximo dois segundos para não
atrasar
seu trabalho.

b) o sistema deveria permitir a alteração de dados incluídos de forma equivocada.

c) o acesso ao sistema deveria ser por meio de uma senha composta por letras e
números e não
apenas por números.

d) o sistema deveria permitir a exclusão de registros de pessoas que deixaram de ser
clientes da
instituição.

e) o sistema, após consultar os dados de um cliente, deveria permitir a impressão dos dados.

Comentários:

(a) Correto, tempo de resposta é um RNF; (b) Errado, permitir alteração de dados
incluídos deforma
equivocada é um RF; (c) Errado, o acesso por meio de senha e sua composição é um RF; (d) Errado,
permitir exclusão de registros de pessoas que deixaram de ser clientes é um RF; (e)
Errado, permitir
a impressão de dados é um RF.


Gabarito: Letra A

Item. 8. (FCC / SEFAZ-BA - 2019) Um Auditor Fiscal da área de Tecnologia da
Informação está
participando do processo de levantamento de requisitos para o desenvolvimento de um novo
software. Os requisitos a seguirforam elencados:

I. Um usuário deve ser capaz de pesquisar a lista de contribuintes devedores.

II. O sistema deve gerar a lista de contribuintes com atendimento agendado naquele dia.

III. O sistema deve se adequar às leis que garantem o sigilo das informações.

IV. Cada usuário do sistema deverá ser identificado por um número de 8 dígitos.

V. O Sistema deve ter suporte para os sistemas operacionais Linux e Windows.

VI. A alteração dos dados de um contribuinte só poderá ser concretizada após confirmação.

VII. Toda consulta deve retornar os valores solicitados em até 20 segundos.

VIII. A gravação dos dados só deverá ser efetuada após o preenchimento de todos os
campos de
preenchimento obrigatório.

IX. Os dados devem ser armazenados em servidores em cluster para garantir a
disponibilidade.

São requisitos funcionais os que constam APENAS em:

a) I, II, III, IV, V, VI e VII.

b) II, IV, VII e VIII.

c) I, II, IV, VI e VIII.

d) IV, VI, VIII e IX.

e) II, IV, V, VI e VIII.

Comentários:

(I) RF; (II) RF; (III) RNF; (IV) RF; (V) RNF; (VI) RF; (VII) RNF; (VIII) RF; (IX) RNF;

Gabarito: Letra C

Item. 9. (FCC / SEMEF-AM - 2019) Considerando que a Fazenda Municipal emprega o
gerenciamento
de requisitos, ganha importância o cuidado com os chamados requisitos voláteis, dentre os
quais fazem parte os requisitos que surgem à medida que o cliente vai
aprimorando sua
compreensão do sistema, denominados requisitos:

a) mutantes.

b) de compatibilidade
c) emergentes
d) adaptativos
e) secundários

Comentários:

A questão trata dos Requisitos Emergentes, que são aqueles que não podem ser
completamente
definidos quando o sistema é especificado e emergem (olha a dica!) à medida que a
compreensão
do cliente sobre o sistema se desenvolve.

Gabarito: Letra C

io.(FCC / SEMEF-AM - 2019) Ao fazer uso da engenharia de requisitos em
projetos, deve-se
analisar o processo de elicitação e análise de requisitos, o qual pode ser dividido
nas seguintes
atividades:

I. Documentação de Requisitos.

II. Classificação e Organização de Requisitos.

III. Obtenção de Requisitos.

IV. Priorização e Negociação de Requisitos.

A ordem sequencial correta para a execução dessas atividades é:

a) 1,111, IV e II.

b) II, IV, III el.

c) III, II, IVel.

d) IV, I, lie III.

e) III, I, lie IV.

Comentários:

POR SOMMERVILLE POR PRESSMAN


ESTUDO DE VIABILIDADE
ELICITAÇÃO E ANÁLISE DE REQUISITOS

OBTENÇÃO DE REQUISITOS
CLASSIFICAÇÃO E ORGANIZAÇÃO
PRIORIZAÇÃO E NEGOCIAÇÃO
DOCUMENTAÇÃO DE REQUISITOS

CONCEPÇÃO
LEVANTAMENTO
ELABORAÇÃO

NEGOCIAÇÃO


ESPECIFICAÇÃO
VALIDAÇÃO
GESTÃO

ESPECIFICAÇÃO
VALIDAÇÃO
GESTÃO

A ordem correta é: (III) Obtenção de Requisitos; (II) Classificação e Organização de
Requisitos; (IV)
Priorização e Negociação de Requisitos; e (I) Documentação de Requisitos.

Gabarito: Letra C

íi. (FCC / SEMEF-AM - 2019) O processo de validação de requisitos de software deve
ser utilizado
em um projeto da Fazenda Municipal, sendo que seus técnicos de TI, devem, nesse
processo de
validação, efetuar revisões de requisitos, atentando que a propriedade:

a) facilidade de compreensão analisa se o requisito pode ser excluído sem prejuízo ao sistema.

b) adaptabilidade verifica se o requisito pode ser alterado sem afetar, de forma
significativa, os
demais requisitos.

c) rastreabilidade verifica se o requisito pode ser testado, de forma completa.

d) facilidade de verificação examina se requisito pode ser excluído sem prejuízo ao sistema.

e) facilidade de compreensão analisa se o requisito tem sua origem diretamente estabelecida.

Comentários:

ATRIBUTOS | DESCRIÇÃO

VALIDADE Examina se as partes interessadas que contribuíram com o levantamento de requisitos
aceitam a especificação final obtida.

CONSISTÊNCIA Examina se existem conflitos entre os requisitos identificados.

COMPREENSIBILIDADE Examina se os requisitos são compreendidos de forma inequívoca pelas
partes
interessadas.

COMPLETUDE Examina se todas as funcionalidades pretendidas fazem parte da especificação
do
sistema.

REALISMO Examina se, dadas as restrições do projeto (tecnológicas, financeiras e temporais), o
sistema especificado é implementável.

VERIFICABILIDADE Examina se os requisitos foram descritos de forma que seja possível verificar
se foram
ou não implementados.

RASTREABILIDADE Examina se a origem de cada requisito está claramente identificada.

ADAPTABILIDADE Examina se os requisitos podem sofrer alterações sem produzir efeitos
em outros
requisitos.


CONFORMIDADE COM

NORMAS

Examina se a especificação obedece às normas técnicas utilizadas para o
desenvolvimento do sistema.

(a) Errado, examina se os requisitos são compreendidos de forma inequívoca
pelas partes
interessadas; (b) Correto, está perfeita a definição da propriedade; (c) Errado, examina
se a origem
de cada requisito está claramente identificada; (d) Errado, examina se os requisitos foram
descritos
de forma que seja possível verificar se foram ou não implementados; (e)
Errado, essa é a
propriedade da rastreabilidade.

Gabarito: Letra B

i2.(FCC / Prefeitura de Manaus-AM - 2019) Considerando a análise de requisitos, as
informações
de rastreabilidade desempenham papel de grande importância. Assim, a equipe responsável
da
Fazenda Municipal deve estar ciente de que a rastreabilidade de projeto significa:

a) definir o mapeamento entre os requisitos de projeto e os usuários do sistema.

b) listar os compiladores utilizados no desenvolvimento de cada módulo de software.

c) determinar o mapeamento entre os requisitos de projeto e os locais onde o sistema
será
utilizado.

d) determinar o desempenho de cada um dos requisitos do sistema.

e) possuir o mapeamento entre os requisitos e os módulos de projeto que implementam
os
requisitos.

Comentários:

A rastreabilidade é a propriedade de uma especificação de requisitos que reflete a
facilidade de
encontrar os requisitos relacionados. Ela é frequentemente representada por meio de
matrizes de
rastreabilidade que mapeiam os requisitos aos stakeholders, aos outros requisitos, aos
módulos de
projeto, aos artefatos ou subprodutos, entre outros. Logo, a rastreabilidade de
projeto significa
possuir o mapeamento entre os requisitos e os módulos de projeto que implementam os requisitos.

Gabarito: Letra E

Item. 13. (FCC / SEFAZ-SC - 2018) A definição de contextos para que os usuários possam agir de maneira
semelhante, entendendo melhor quais informações precisam fornecer durante a
atividade de
elicitação de requisitos, pode ser obtida por meio da aplicação de duas técnicas de
elicitação
denominadas:

a) cenários e protótipos.

b) entrevistas e observação.

c) protótipos e observação.

d) cenários e histórias de usuários.

e) reuniões com facilitadores e histórias de usuários.

Comentários:

A questão deseja saber duas técnicas que definem contextos para que os usuários possam
agir de
maneira semelhante, isto é, que definem ambientes próximos ao da realidade. Com esse
foco, a as
técnicas que mais "simulam" a realidade são: cenários e protótipos.


Gabarito: Letra A

i4-(FCC / SEFAZ-SC - 2018) Durante o processo de validação, diferentes tipos
de verificação
podem ser efetuados com os requisitos registrados nos documentos de requisitos. O tipo
de
verificações de consistência é realizado para:

a) identificar, por meio de análise mais aprofundada, outras funções necessárias,
adicionais ou
diferentes, além daquelas que um usuário pensava que fossem as necessárias para o
sistema
executar determinadas funções.

b) evitar que requisitos, no documento, entrem em conflito uns com outros, ou seja,
não deve
haver restrições contraditórias ou descrições diferentes para mesma função do sistema.

c) garantir que o documento de requisitos contenha os requisitos que definem todas as
funções
e as restrições pretendidas pelos usuários do sistema.

d) assegurar, usando o conhecimento das tecnologias existentes, que os requisitos
verificados
possam ser realmente implementados, considerando o orçamento e o cronograma
para o
desenvolvimento do sistema.

e) reduzir o potencial de conflito entre o cliente e o contratante por meio de
um conjunto de
testes que demonstre que o sistema entregue atende a cada requisito especificado.

Comentários:

(a) Errado, trata-se de verificação de validade;

(b) Correto, trata-se de verificação de consistência;

(c) Errado, trata-se de verificação de completude;

(d) Errado, trata-se de verificação de realismo;

(e) Errado, trata-se da facilidade de verificação.

Gabarito: Letra B

Item. 15. (FCC / SABESP - 2018) Um Analista necessita levantar os requisitos de um sistema
junto aos
usuários. São técnicas de levantamento:

a) Cenários e Peer Review.

b) Product Owner e Brainstorming.

c) Overview e Use Cases.

d) Joint Application Design (ou Development) - JAD e Etnografia.

e) Prototipação e Sprint.


Comentários:

(a) Errado, Peer Review não é uma técnica de levantamento de requisitos;

(b) Errado, Product Owner não é uma técnica de levantamento de requisitos;

(c) Errado, Overview não é uma técnica de levantamento de requisitos;

(d) Correto, JAD e Etnografia são ambas técnicas de levantamento de requisitos;

(e) Errado, Sprint não é uma técnica de levantamento de requisitos.

Gabarito: Letra D

i6.(FCC / FUB - 2018) O documento de requisitos deve ser elaborado a
partir da análise de
viabilidade do software, seguida de análise, especificação e validação de requisitos.

Comentários:

O processos de Engenharia de Requisitos inclui quatro atividades de alto
nível: Estudo de
Viabilidade; Elicitação e Análise; Especificação e Validação. Logo, a ordem apresentada
na questão
está perfeita!

Gabarito: Correto

Item. 17. (FCC / BNB - 2018) A revisão técnica é um procedimento utilizado para validar
os requisitos de
um projeto, com o objetivo de identificar eventuais inconsistências e verificar se os
artefatos
estão de acordo com o padrão esperado.

Comentários:

Em uma revisão formal de requisitos, a equipe de desenvolvimento conduz o cliente
pelos requisitos
de sistema, explicando as implicações de cada requisito. A equipe de revisão verifica
cada requisito
de acordo com diversos critérios para evitar conflitos, contradições, erros e omissões
nos requisitos
apontados e registrados formalmente no relatório de revisão. Logo, a revisão técnica é
realmente
um procedimento utilizado para validar os requisitos de um projeto, com o objetivo de
identificar
eventuais inconsistências e verificar se os artefatos estão de acordo com o padrão esperado.

Gabarito: Correto

18.(FCC / DPE-AM - 2018) Considere, por hipótese, que uma equipe de Analistas de
Sistemas da
Defensoria elencou a lista de requisitos para um novo sistema:

- O sistema não deverá revelar aos usuários nenhuma informação pessoal sobre os
cidadãos,
além do número do processo, em respeito à legislação de privacidade.


- Em razão das restrições referentes aos direitos autorais, alguns documentos
devem ser
excluídos imediatamente ao serem fornecidos pelos cidadãos em seus processos.

- O sistema deve implementar interfaces utilizando as normas de usabilidade vigentes
para o
serviço público.

A lista apresenta exemplos de requisitos:

a) funcionais do tipo proteção e do tipo regulação.

b) funcionais de usabilidade.

c) não-funcionais de proteção.

d) funcionais internos de legislação.

e) não-funcionais externos do tipo legal e do tipo regulador.

Comentários:

O primeiro é um RNF Externo do tipo Legal; o segundo é um RNF Externo do tipo
Legal; e o
terceiro é um RNF Externo do tipo Regulador.

Gabarito: Letra E

ig.(FCC / BNB - 2018) No levantamento de informações, os requisitos dos
solicitantes são
classificados como normais e conceituais. Os requisitos normais refletem os
objetivos e as
metas do produto, ao passo que os conceituais estão implícitos no produto ou
extrapolam as
expectativas do cliente.

Comentários:

No levantamento de informações, os requisitos dos solicitantes são classificados como
normais e
conceituais, esperados e fascinantes. Os requisitos normais refletem os objetivos e as
metas do
produto, ao passo que os conceituais esperados estão implícitos no produto eu e os
requisitos
fascinante extrapolam as expectativas do cliente.

Gabarito: Errado

2O.(FCC / BNB - 2018) O protótipo operacional serve para aprimorar o entendimento de
como o
sistema deve funcionar, por meio da elucidação dos requisitos do usuário e da
compreensão de
suas necessidades.

Comentários:


Perfeito! O protótipo operacional realmente serve para aprimorar o entendimento
de como o
sistema deve funcionar, por meio da elucidação dos requisitos do usuário e da
compreensão de suas
necessidades. Ele pode ser utilizado tanto na elicitação quanto na validação de requisitos.

Gabarito: Correto

2i.(FCC/ MPE-MA-2013) O escopo de um projeto é determinado pelo levantamento de
requisitos
funcionais e não funcionais. Dentre os requisitos não funcionais se enquadram
os requisitos
organizacionais, que podem ser divididos em:

a) reguladores e éticos.

b) ambientais, operacionais e de desenvolvimento.

c) contábeis e de segurança.

d) de desempenho e de espaço.

e) de eficiência, de confiança e de proteção.

Comentários:

Os Requisitos Organizacionais podem ser divididos em Requisitos Ambientais, Operacionais
e de
Desenvolvimento (ou Implementação).

Gabarito: Letra B

Item. 22. (FCC / DPE-SP - 2013) Em uma das etapas da Engenharia de Requisitos há a
preocupação em
se observar a especificação produzida, visando verificar que os requisitos
tenham sido
declarados, por exemplo, sem ambiguidades.

O texto refere-se à etapa de:

a) gestão dos requisitos.

b) elicitação dos requisitos.

c) negociação dos requisitos.

d) levantamento dos requisitos.

e) validação dos requisitos.

Comentários:

Galera, os produtos de trabalho resultantes da engenharia de requisitos são avaliados
quanto a
qualidade no processo de validação. A validação dos requisitos examina a
especificação para
garantir que todos os requisitos do software tenham sido declarados de modo não ambíguo.

Gabarito: Letra E


23- (FCC / TST- 2012) Na Engenharia de Requisitos, o gerente de requisitos:

a) acompanha e monitora ações durante a verificação do software, sendo este o processo
que
garante o atendimento aos requisitos informados pelo usuário final.

b) possui autonomia para realizar alterações no projeto para garantir que o software
seja bem
construído e atenda às necessidades da equipe de desenvolvimento.

c) mantém atualizados os requisitos junto ao usuário final e a equipe de
desenvolvimento, a fim
de obter sucesso no processo de homologação do software, atendendo as
necessidades e
expectativas.

d) classifica os requisitos em diferentes tipos, sendo os do tipo funcional
relacionados com o
custo e confiabilidade do software e os do tipo não-funcional relacionados com os casos de uso.

e) obtém o comprometimento dos integrantes da equipe de desenvolvimento de software para
o cumprimento do processo de software.

Comentários:

(a) Errado, ele trata da validação e, não, da verificação; (b) Errado, para que
atenda às necessidades
do usuário e, não, da equipe de desenvolvimento; (c) Correto, essa é uma de suas
responsabilidades!

(d) Errado, a questão inverteu os conceitos; (e) Errado, essa não é uma função do
Gerente de
Requisitos.

Gabarito: Letra C

24.(FCC /TCE-AP-2012) Em relação a requisitos de sistemas, considere:

I. O modo como um sistema deve reagir a certas entradas e o comportamento em que o
sistema
deve ter em certas situações e, em alguns casos, especificar o que o sistema não deve
fazer, são
chamados de requisitos não-funcionais.

II. As restrições aos serviços ou funções de um sistema, como, por exemplo, processos
de
desenvolvimento ou utilização de padrões, são requisitos de funcionamento do
sistema ou
requisitos funcionais.

III. Requisitos que vem do domínio da aplicação do sistema e refletem
características ou
restrições para aquele domínio são chamados de requisitos de domínio e podem ser
requisitos
funcionais e/ou não-funcionais.

Está correto o que se afirma em:


a) III, apenas.

b) I, lie III.

c) I e II, apenas.

d) II e III, apenas.

e) I, apenas.

Comentários:

(a) Errado, esses são chamados de Requisitos Funcionais; (b) Errado, esses são
Requisitos Não-
Funcionais; (c) Correto, esses são os chamados requisitos de domínio.

Gabarito: Letra A

Item. 25. (FCC / MPE-PE - 2012) Os requisitos não funcionais não estão diretamente ligados
aos serviços
específicos oferecidos pelo sistema a seus usuários. Eles podem estar
relacionados às
propriedades emergentes do sistema, como confiabilidade, tempo de resposta e ocupação de
área, entre outros. Dentre os tipos de requisitos não funcionais, é possível destacar
os requisitos
de produto, organizacionais e externos. Dentre os requisitos de produto,
podemos citar os
requisitos:

a) de eficiência e de confiança.

b) contábeis e de desempenho.

c) legais e de usabilidade.

d) reguladores e de proteção.

e) legais e contábeis.

Comentários:

Os Requisitos de Produto são: Desempenho, Confiabilidade,
Portabilidade, Eficiência,
Performance e Espaço (8a Edição); ou Usabilidade, Eficiência, Desempenho, Espaço,
Proteção e
Confiabilidade (9a Edição).

Gabarito: Letra A

26.(FCC / TRE-CE - 2012) Considere:

I. Para cada cliente deve ser aplicado um identificador único.

II. O tempo de resposta entre a requisição e a informação não pode exceder a 2 ms.

III. Clientes têm filiais que devem "carregar", na base de dados, o
identificador do cliente
principal.


IV. O sistema não deve ferir as leis de proteção ambiental.

São requisitos não funcionais os que constam em
a) I e II, apenas.

b) II e III, apenas.

c) II e IV, apenas.

d) I, III e IV, apenas.

e) 1,11, III e IV.

Comentários:

Galera, essa questão é bastante polêmica. Porque? Eu acho que é bem claro que os itens II (que fala
de desempenho) e IV (que fala de leis externas) são requisitos não-funcionais. O
problema são os
itens I e III - o primeiro, na minha opinião, também é claramente um RNF e o único
que pode gerar
alguma dúvida é o último, que eu também considero como RNF. Ou seja, para mim, todos
são RNF,
mas a banca considerou que apenas os itens II e IV são RNF -discordo veementemente!

Gabarito: Letra C

Item. 27. (FCC / TST- 2012) Na Engenharia de Requisitos, o gerente de requisitos:

a) acompanha e monitora ações durante a verificação do software, sendo este o processo
que
garante o atendimento aos requisitos informados pelo usuário final.

b) possui autonomia para realizar alterações no projeto para garantir que o software
seja bem
construído e atenda às necessidades da equipe de desenvolvimento.

c) mantém atualizados os requisitos junto ao usuário final e a equipe de
desenvolvimento, a fim
de obter sucesso no processo de homologação do software, atendendo as
necessidades e
expectativas.

d) classifica os requisitos em diferentes tipos, sendo os do tipo funcional
relacionados com o
custo e confiabilidade do software e os do tipo não-funcional relacionados com os casos de uso.

e) obtém o comprometimento dos integrantes da equipe de desenvolvimento de software para
o cumprimento do processo de software.

Comentários:

(a) Errado. Não é durante a Verificação, mas Validação de Software; (b)
Errado. Não são as
necessidades da Equipe de Desenvolvimento, mas dos usuários; (c) Correto. É exatamente isso; (d)


Errado. Estão invertidos, custo e confiabilidade são RNF e Casos de Uso são RF; (e)
Errado. Isso é
responsabilidade do Gerente de Projetos e, não, do Gerente de Requisitos.

Gabarito: Letra C

28.(FCC / TJ-PE - 2012) Na engenharia de requisitos trata-se de uma técnica de
elicitação que
ocorre em ambiente mais informal em que toda a idéia deve ser levada em consideração
para a
solução de um problema, sendo proibida a crítica a qualquer sugestão dada, e
encorajada,
inclusive, a criação de ideias que pareçam estranhas ou exóticas:

a) Prototipação.

b) Entrevista.

c) Questionário.

d) Brainstorming.

e) Análise de protocolos.

Comentários:

A questão trata da Técnica de Brainstorming, isto é, uma abordagem de elicitação
ocorrida em
grupo em ambientes informais durante cerca de quinze minutos em que toda a ideia deve
ser levada
em consideração, sendo proibida a crítica a qualquer sugestão dada, e encorajada,
inclusive, a
criação de ideias que pareçam estranhas ou exóticas.

Gabarito: Letra D

2g.(FCC / INFRAERO-2011- Letra D) No contexto de levantamento de requisitos,
funcionalidade
é um dos aspectos que deve ser levado em conta na abordagem dos requisitos funcionais.

Comentários:

Ué, claro! A funcionalidade é evidentemente um dos aspectos na abordagem dos
requisitos
funcionais.

Gabarito: Correto

3o.(FCC / INFRAERO - 2011) A engenharia de requisitos ajuda os engenheiros de
software a
compreender melhor o problema que eles vão trabalhar para resolver. Ela inclui um
conjunto de
tarefas que levam a um entendimento de qual será o impacto do software sobre o
negócio, do
que o cliente quer e de como os usuários finais vão interagir com o software. A
função de
negociação no processo de engenharia de requisitos:

a) especifica, revisa e valida o problema de modo a garantir que seu
entendimento e o
entendimento do cliente sobre o problema coincidam.


b) refina e modifica os requisitos. É uma ação de modelagem de análise composta de
várias
tarefas de modelagem e refinamento.

c) define quais são as prioridades, o que é essencial, o que é necessário. Clientes,
usuários e
outros interessados são solicitados a ordenar os requisitos e depois discutir
os conflitos de
prioridade.

d) ajuda o cliente a definir o que é necessário.

e) define o escopo e a natureza do problema a ser resolvido.

Comentários:

Galera... falou em Negociação, tem que lembrar de consenso entre as partes
interessadas. E para
chegar a um consenso, deve-se definir prioridades. Na atividade de priorização e
negociação, o
engenheiro de requisitos deve conciliar os conflitos por meio de uma negociação entre
clientes,
usuários e partes interessadas. Pergunta-se a eles quais são seus requisitos
prioritários. Então,
utiliza-se uma abordagem iterativa que avalia custos e riscos de modo a
balancear todas as
demandas.

Gabarito: Letra C

Item. 31. (FCC / TRTi - 2011) A técnica utilizada na compreensão de requisitos sociais e
organizacionais
por observação das rotinas dos envolvidos é a:

a) prototipação.

b) por pontos de vista.

c) por cenário.

d) entrevista.

e) etnografia.

Comentários:

Observação de Rotinas?Trata-se de Etnografia-técnica de observação utilizada para
compreender
os requisitos organizacionais e sociais. Coloca-se o analista dentro do campo
de atuação dos
usuários, observando o trabalho diário anotando as tarefas reais em que os
participantes estão
envolvidos.

Gabarito: Letra E


Item. 32. (FCC / INFRAERO - 2011) Os produtos de trabalho resultantes da engenharia de
requisitos são
avaliados quanto à qualidade durante a etapa de validação de requisitos. Analise os
itens a seguir
referentes a essa etapa:

I. Um dos principais mecanismos de validação de requisitos é a avaliação técnica formal.

II. O modelo de análise pode garantir que os requisitos foram consistentemente declarados.

III. É frequentemente útil examinar cada requisito em face de um conjunto de questões
do tipo
checklist.

IV. Aequipe de revisão que avalia os requisitos inclui apenas pessoas com conhecimento
técnico
na área de TI, como engenheiros de softwares, desenvolvedores etc.

Está correto o que consta em:

a) I, II, III e IV.

b) II e IV, apenas.

c) I, II e IV, apenas.

d) II, III e IV, apenas.

e) I, II e III, apenas.

Comentários:

(I) Correto! Um dos principais mecanismos de validação de requisitos é a
avaliação/revisão técnica
formal; (II) Correto! Como eu sempre falo, quando uma questão usa "pode", ela só
estará errada se
não existir nenhuma outra hipótese. Ora, não há nenhuma hipótese de um
modelo de análise
garantir que os requisitos foram consistentemente declarados? Não, é possível,
logo questão
perfeita; (III) Correto! Embora a revisão para validação dos requisitos possa
ser conduzida de
qualquer maneira desde que possibilite a descoberta de erros nos requisitos, é útil
examinar cada
requisito contra um checklist. (IV) O time de revisão inclui os engenheiros de
sistema, clientes,
usuários e outros stakeholders que examinam a especificação do sistema à procura de
erros de
conteúdo ou interpretação, pontos onde pode ser necessário esclarecimento,
perda de
informações, inconsistências (um dos maiores problemas da engenharia de grandes
produtos),
requisitos conflitantes, ou requisitos irreais (de desenvolvimento impossível).

Gabarito: Letra E

Item. 33. (FCC / TRT19 - 2011) A avaliação do impacto de mudança de um requisito, muitas
vezes, faz
com que seja necessário retornar à sua fonte. Na validação dos requisitos, a equipe
deve estar
atenta, portanto, à:

a) rastreabilidade.


b) adaptabilidade.

c) qualidade.

d) facilidade de compreensão.

e) facilidade de verificação.

Comentários:

Trata-se da Rastreabilidade, isto é, avaliar impacto no projeto da mudança em um
requisito. É a
propriedade de uma especificação de requisitos que reflete a facilidade de encontrar os
requisitos
relacionados. Ela é frequentemente representada por meio de matrizes de
rastreabilidade que
relacionam os requisitos aos stakeholders, aos outros requisitos, aos módulos
de projeto, aos
artefatos ou subprodutos, etc.

Gabarito: Letra A

34-(FCC / TRT23 - 2011) Tabelas de rastreamento para relacionar os requisitos
identificados a um
ou mais aspectos do sistema ou do seu ambiente devem ser desenvolvidas, segundo
Pressman,
na engenharia de requisitos por meio da função de:

a) gestão.

b) especificação.

c) elaboração.

d) negociação.

e) validação.

Comentários:

De acordo com Pressman, a gestão de requisitos começa com a identificação. A cada
requisito é
atribuído um modo identificador. Uma vez identificados os requisitos, tabelas de
rastreamento são
desenvolvidas. Lembrando que a rastreabilidade é a propriedade de uma
especificação de
requisitos que reflete a facilidade de encontrar os requisitos relacionados

Gabarito: Letra A

35.(FCC / BAHIAGÁS - 2010) É uma restrição sobre os serviços ou as funções oferecidos
pelo
sistema. Pode ser uma restrição de timing, sobre o processo de
desenvolvimento, sobre o
desempenho ou sobre a confiabilidade do sistema, entre outras. Trata-se de:

a) requisito não funcional.

b) requisto funcional.

c) especificação de risco.

d) iteração de processo.

e) etnografia.


Comentários:

A questão trata de Requisito Não-Funcional, isto é, são restrições nos
serviços ou funções
oferecidas pelo sistema.

Gabarito: Letra A

36.(FCC / DPE-SP- 2010) Sobre análise de requisitos da engenharia de software, considere:

I. Os requisitos de usuário podem descrever tanto requisitos funcionais quanto
requisitos não-
funcionais.

II. Os requisitos de sistema podem descrever apenas requisitos não funcionais.

III. Os requisitos não-funcionais podem ser divididos em requisitos de produto,
organizacionais
e externos.

Está correto o que se afirma em:

a) III, apenas.

b) I e II, apenas.

c) I e III, apenas.

d) II e III, apenas.

e) I, lie III.

Comentários:

(a) Correto! É exatamente isso. Lembrando que Requisitos de Usuários são
descrições, em
linguagem natural e com diagramas, de quais serviços o sistema deve fornecer e as
restrições sob
as quais deve operar. São requisitos com alto nível de abstração e poucos detalhes,
feitos para
serem lidos por pessoas leigas, (b) Errado! Requisitos de Sistema, de fato, podem ser
funcionais ou
não-funcionais. No entanto, o cerne dos requisitos de sistema são os requisitos
funcionais. Não vejo
a possibilidade de um documento de requisitos de sistema conterem apenas
requisitos não-
funcionais - o inverso talvez seja possível, isto é, um documento de requisitos de
sistema com
apenas requisitos funcionais, (c) Correto! Ele se divide nessas três categorias.

Gabarito: Letra C

Item. 37. (FCC / DPE-SP - 2010) No contexto da Engenharia de Requisitos, considere:

I. O sistema deve fornecer uma entrada de dados que possibilite a inclusão de
atributos de
permissão de acesso às dependências da corporação por técnicos, supervisores e chefes.


II. Algumas permissões de acesso deverão ter tratamento especial para a entrada de
atributos.
Para este tipo de permissão, atributos excedentes a uma faixa predeterminada só poderão
ser
incluídos por chefes de seção.

Em relação às assertivas acima, é correto afirmar:

a) O item I trata de um requisito funcional e a ele está associado o requisito não
funcional,
contido no item II.

b) O item I trata de um requisito não funcional e a ele está associado o requisito
funcional,
contido no item II.

c) Ambos referem-se a requisitos funcionais.

d) A assertiva contida no item II é uma condição restritiva do requisito não
funcional do item I.
Por si só, não constitui um requisito, tanto funcional quanto não funcional.

e) A assertiva contida no item II é uma condição restritiva do requisito funcional do
item I. Por si
só, não constitui um requisito, tanto funcional quanto não funcional.

Comentários:

Galera, o primeiro item trata de um possível serviço do sistema, logo é um Requisito
Funcional. Já
o segundo item, da maneira que está escrito, trata-se de uma Regra de Negócio, isto é,
não é sequer
um Requisito. Épossível transformá-lo em um Requisito? Sim, percebam:

II. O Sistema deve permitir um tratamento especial para indivíduos com determinada
permissão de
acesso, isto é, atributos excedentes só poderão ser incluídos por chefes de sessão.

Pronto, nós transformamos a Regra de Negócio em um Requisito Funcional. Sommerville
afirma
que eles definem como o sistema deve reagir em condições e até o que o sistema não
deve fazer
(restrições). Portanto, acredito que a resposta é a Letra E, mas a banca entendeu que
o segundo
item é um Requisito Não-Funcional.

Gabarito: Letra A

38.(FCC / MPE-RN - 2010) Na engenharia de software, etnografia é:

a) uma fase do processo de software aplicada no modelo em cascata.

b) uma fase do processo de software aplicada no modelo em espiral.


c) uma técnica de observação que pode ser usada para compreender os requisitos
sociais e
organizacionais.

d) uma técnica aplicada na engenharia de requisitos cujo objetivo é definir, a priori,
as classes
que contém elementos gráficos (BLOB).

e) um projeto cujo principal objetivo é criar interfaces gráficas, que facilitam o
acesso do usuário
(GUI).

Comentários:

A técnico de Etnografia é uma Técnica de observação utilizada para compreender os
requisitos
organizacionais e sociais. Coloca-se o analista dentro do campo de atuação
dos usuários,
observando o trabalho diário anotando as tarefas reais em que os participantes estão
envolvidos.
Em geral, essa é uma técnica utilizada em conjunto com outras técnicas. Como ela é
uma técnica
de observação, isoladamente ela não é muito eficaz na elicitação.

Gabarito: Letra C

3g.(FCC / MPE-RN - 2010) As políticas de rastreabilidade de requisitos são decididas
durante o
estágio de:

a) agregação dos requisitos funcionais, apenas.

b) implementação do sistema, apenas.

c) implementação do sistema
d) eliminação dos requisitos não funcionais.

e) gerenciamento de requisitos.

Comentários:

As políticas de rastreabilidade de requisitos são decididas durante o estágio de
Gerenciamento de
Requisitos.

Gabarito: Letra E

ZfO.(FCC / SEFAZ-SP - 2009) É necessário que 0 software calcule os salários dos
diaristas e
mensalistas e emita relatórios mensais sumariados por tipo de salário. Entretanto, a base de dados
deve estar protegida e com acesso restrito aos usuários autorizados. De qualquer forma,
0 tempo
de resposta das consultas não deve superar os quinze segundos, pois
inviabilizaria todo 0
investimento nesse sistema. Devo lembrar que os relatórios individuais dos departamentos,
nos
quais constam os salários dos funcionários, devem ser emitidos quinzenalmente em razão
dos
adiantamentos e vales que recebem. Éfundamental que o software seja operacionalizado
usando
código aberto. Necessito, ainda, forte gerenciamento de risco, prazo e custo, porque a entrega do
produto final não pode ultrapassar o prazo de oito meses a contar da data de início
do projeto. No
texto, são requisitos funcionais:

a) Calcule os salários dos diaristas e mensalistas e os relatórios individuais dos departamentos,
nos quais constam os salários dos funcionários, devem ser emitidos quinzenalmente.

b) Necessito, ainda, forte gerenciamento de risco, prazo e custo e a base de dados deve estar
protegida e com acesso restrito aos usuários autorizados.

c) É fundamental que o software seja operacionalizado usando código aberto e emita relatórios
mensais sumariados portipo de salário.

d) Emita relatórios mensais sumariados por tipo de salário e necessito, ainda, forte
gerenciamento de risco, prazo e custo.

e) A base de dados deve estar protegida e com acesso restrito aos usuários autorizados e
entrega do produto final não pode ultrapassar o prazo de oito meses.

Comentários:

a) Calcular os salários dos diaristas e mensalistas? RF, visto que é uma possível funcionalidade
que o
sistema deve apresentar; Emitir relatórios individuais quinzenalmente? RF, visto que
também é uma
possível funcionalidade que o sistema deve apresentar.

b) Gerenciamento de Risco, Prazo e Custo? RNF, visto que é uma restrição do sistema; Base de dados
protegida e com acesso restrito? RNF, visto que é uma restrição do sistema.

c) Operacionalizar o software com código aberto? RNF, visto que é uma restrição do
sistema; Emitir
relatórios mensais sumarizados? RF, é uma possível funcionalidade que o sistema deve apresentar.

d) Emitir relatórios mensais sumarizados? RF, visto que é uma possível funcionalidade
que o sistema
deve apresentar. Gerenciamento de Risco, Prazo e Custo? RNF, visto que é uma restrição do sistema.

e) Base de dados protegida e com acesso restrito? RNF, visto que é uma restrição do
sistema;

Restrição de 8 meses quanto ao prazo? RNF, visto que é uma restrição do sistema.

Observe que os Requisitos Funcionais estão mais relacionados a possíveis utilizações do
usuário,
em sua interação com o sistema e como o sistema vai realizar alguma atividade. Já os
Requisitos
Não Funcionais estão mais relacionados a aspectos qualitativos do sistema, de seu
processo de
desenvolvimento e de suas restrições. Logo, percebe-se que somente a Letra A possui
ambos os
Requisitos Funcionais!

Gabarito: Letra A


Item. 41. (FCC /TRT3 -2009) Com relação aos requisitos de software, considere:

I. funcionais são somente requisitos de usuário.

II. funcionais e não-funcionais podem ser requisitos de usuário.

III. funcionais e não-funcionais podem ser requisitos de sistema.

Está correto o que se afirma APENAS em
a) l.

b) II.

c) III.

d) I e III.

e) lie III.

Comentários:

Requisitos funcionais e não-funcionais podem ser tanto requisitos de usuário quanto
requisitos de
sistema.

Gabarito: Letra E

42.(FCC /TRT7-2009) No processo de engenharia de requisitos, é uma técnica de
observação que
pode ser usada para compreender os requisitos sociais e organizacionais. Trata-se de:

a) Workshop.

b) Brainstorming.

c) Scrum.

d) Análise de ponto de vista.

e) Etnografia.

Comentários:

Já viram quantas vezes essa técnica caiu em provas? De novo, Etnografia - técnica de
observação
utilizada para compreender os requisitos organizacionais e sociais.

Gabarito: Letra E

Item. 43. (FCC / TRT3 - 2009) São técnicas e abordagens utilizadas na obtenção dos requisitos:

a) estresse, cenários e workshop.

b) workshop, etnografia e estresse.

c) etnografia, questionários e validação.


d) pontos de vista, cenários e entrevista.

e) pontos de vista, casos de uso e validação.

Comentários:

(a) Errado, estresse não é uma técnica de obtenção de requisitos;

(b) Errado, estresse não é uma técnica de obtenção de requisitos;

(c) Errado, validação não é uma técnica de obtenção de requisitos;

(d) Correto, todas são técnicas de obtenção de requisitos;

(e) Errado, validação não é uma técnica de obtenção de requisitos;

Gabarito: Letra D

Item. 44. (FCC / PGE-RJ - 2009) No âmbito da Engenharia de Requisitos, uma revisão técnica formal é:

a) um teste de desempenho.

b) uma técnica de elicitação.

c) um instrumento de rastreamento.

d) o resultado do escopo.

e) um mecanismo de validação.

Comentários:

A revisão técnica formal (revisão de requisitos) é uma técnica ou mecanismo
de validação de
requisitos - assim como a prototipação e a geração de casos de teste.

Gabarito: Letra E


QUESTõES CoMENTADAS - FCV

í. (FGV / TCE-TO - 2022) A Equipe de Desenvolvimento de Soluções (EDS) recebeu a
solicitação
de que um dos campos utilizados para entrada de dados da aplicação Web em construção
apresente sugestões de palavras dinamicamente, conforme o usuário for digitando
novos
caracteres.

A EDS recebeu a solicitação de um requisito de:

a) confiança;

b) eficiência;

c) desempenho;

d) usabilidade;

e) desenvolvimento.

Comentários:

Trata-se claramente de um requisito de usabilidade, dado que as sugestões dinâmicas que
surgem
enquanto o usuário digita caracteres atuam diretamente na usabilidade no sentido de
facilidade de
uso do sistema.

Gabarito: Letra D

Item. 2. (FGV / TCE-TO - 2022) Carlos é uma parte interessada em uma aplicação Web e
solicitou à
equipe de desenvolvimento uma funcionalidade capaz de emitir relatórios com
cabeçalhos
padronizados. Assim, os cabeçalhos devem ter cor de fundo, paleta de cores
e tipografia,
seguindo o padrão adotado em outros documentos emitidos pelo departamento
responsável
pela aplicação.

A solicitação de Carlos refere-se a um requisito:

a) funcional regulador;

b) não funcional organizacional;

c) funcional do processo operacional;

d) não funcional de usabilidade;

e) funcional de desenvolvimento.

Comentários:


Padronização estética claramente não são requisitos funcionais, logo se trata de um
requisito não
funcional. Especificamente, trata-se de um requisito organizacional: aqueles são
derivados de
políticas e procedimentos da organização do cliente e do desenvolvedor. Entre os
exemplos,
estão padrões de processo que devem ser usados, linguagem de programação ou o método
de
projeto usado, e requisitos de entrega que especificam quando o produto e a sua
documentação
devem ser entregues.

Gabarito: Letra B

Item. 3. (FGV / TCE-TO - 2022) A Equipe de Desenvolvimento de Soluções (EDS) recebeu a
solicitação
de que um dos campos utilizados para entrada de dados da aplicação Web em construção
apresente sugestões de palavras dinamicamente, conforme o usuário for digitando
novos
caracteres. A EDS recebeu a solicitação de um requisito de:

a) confiança;

b) eficiência;

c) desempenho;

d) usabilidade;

e) desenvolvimento.

Comentários:

Notem que se trata de uma solicitação que facilita a navegação intuitiva do usuário,
logo se trata
de um requisito de usabilidade.

Gabarito: Letra D

Item. 4. (FGV / TCE-TO - 2022) Carlos é uma parte interessada em uma aplicação Web e
solicitou à
equipe de desenvolvimento uma funcionalidade capaz de emitir relatórios com
cabeçalhos
padronizados. Assim, os cabeçalhos devem ter cor de fundo, paleta de cores e tipografia,


seguindo o padrão adotado em outros documentos emitidos pelo departamento
responsável
pela aplicação:

A solicitação de Carlos refere-se a um requisito:

a) funcional regulador;

b) não funcional organizacional;

c) funcional do processo operacional;

d) não funcional de usabiIidade;

e) funcional de desenvolvimento.

Comentários:

A solicitação de Carlos não tem nenhuma relação com a funcionalidade da aplicação web,
logo se
trata de um requisito não funcional. Essa solicitação tem o intuito de
facilitar a navegação na
aplicação web? Não, tem o intuito de padronizar os relatórios da organização, logo se
trata de um
requisito não funcional organizacional.

Gabarito: Letra B

Item. 5. (FGV/TCE-TO -2022) As credenciais de acesso dos usuários de um aplicativo são
armazenadas
em um banco de dados e são utilizadas unicamente para acesso àsfuncionalidades do
aplicativo.
A equipe de desenvolvimento definiu como requisito não funcional que o sistema deve
evitar
que as senhas sejam obtidas por um invasor mesmo que o aplicativo ou banco de dados
esteja
comprometido.

Para implementar o requisito não funcional, um modo de proteger as senhas dos usuários é:

a) ocultar o algoritmo utilizado para proteção das senhas;

b) armazenar as senhas cifradas por meio de um algoritmo de chaves assimétricas;

c) utilizar um algoritmo hash com salt antes de persistir as senhas no banco de dados;

d) codificar um algoritmo próprio para cifrar as senhas com base em uma chave
randômica
segura;

e) usar uma chave randômica gerada pelo aplicativo para cifrar as senhas por meio de
um
algoritmo de chave simétrica.

Comentários:

(a) Errado, o algoritmo pode ser público - é a chave que deve ser privada; (b)
Errado, deve-se
armazenar o hashing das senhas e, não, a senha cifrada por algoritmo assimétrico; (c)
Correto, deve
se utilizar um algoritmo de hash com salt* para persistir os dados no banco; (d)
Errado, codificar
um algoritmo próprio é uma péssima ideia - o ideal é que o algoritmo seja pública
para que sua
segurança seja testada e validade; (e) Errado, não é um bom modo para
proteger senhas de
usuários.


* Salt é é uma string aleatória de dados adicionada à entrada de uma função hash
cujo objetivo é
dificultar a "pré-computação" de um conjunto de entradas que gerará uma determinada
saída de
hash. Como resultado, fica mais difícil para os invasores decifrar senhas ou outras
informações
confidenciais ao tentar adivinhar as entradas de uma função de hash.

Agora sendo rigoroso, eu acho que a questão poderia ser anulada. Todos esses são
modos de
proteger as senhas de usuário - alguns são péssimos, mas ainda assim são modos.
Acredito que o
enunciado da questão poderia questionar qual é a maneira mais adequada de proteger
senhas de
usuários.

Gabarito: Letra C

Item. 6. (FGV / TCE-TO - 2022) A Equipe de Tecnologia (ETi) de um tribunal de contas
está levantando
as necessidades para um novo sistema junto às partes interessadas. Uma das
partes
interessadas solicitou que o novo sistema seja fácil de usar, como requisito não funcional.

Para que o requisito não funcional "fácil de usar" seja objetivamente
testado, a ETi deve
considerara métrica:

a) eficiência;

b) disponibilidade;

c) tempo de treinamento;

d) taxa de ocorrência de falhas;

e) tempo de atualização de tela.

Comentários:

O usuário deseja que o sistema seja fácil de usar, logo está relacionado ao tempo de
treinamento.
Essa métrica descreve quanto tempo é necessário para treinar um usuário para
usar as
funcionalidades de um sistema. Em geral, os tempos de treinamento estimados são
baseados nas
habilidades do usuário e no nível de complexidade do sistema.

Gabarito: Letra C

Item. 7. (FGV / ALERJ - 2017) O Analista de Sistemas Pedro está realizando um
levantamento de
requisitos por meio da prototipação. Sua intenção com esse protótipo é proporcionar uma
visão
geral do sistema com todas as suas funcionalidades, sem entrar em detalhes específicos
de cada
funcionalidade, de forma que a interface como um todo possa sercriticada pelos
usuários. Nesse
caso, o tipo de protótipo mais adequado é o (a):

a) vertical;

b) tridimensional;

c) prototipação rápida;


d) textual;

e) horizontal.

Comentários:

Pessoal, a prototipação horizontal prototipação horizontal consiste em montar uma
interface
completa em termos de elementos, permitindo uma visão geral do usuário por todo
o sistema,
assim como uma pessoa observa o horizonte, em um protótipo horizontal, o usuário obtém
uma
visão geral de tudo. A Prototipação Vertical é focada nas funcionalidades.
Dessa forma, um
protótipo do sistema pode ser reduzido a um módulo isolado, onde o usuário
poderá ver em
detalhes um pedaço limitado do sistema. A prototipação textual é aquela feita
por meio da
descrição (texto) das funcionalidades do sistema. Eu desconheço o conceito de
Prototipação
Rápida ocorre quando um software é construído rapidamente que apresenta a
funcionalidade
básico do produto desejado. O ponto-chave é que um protótipo rápido reflita a
funcionalidade que
o cliente vê, como telas de entrada e a geração de relatórios, mas omita aspectos
não aparentes.
Por fim, eu desconheço o conceito de prototipação tridimensional. Logo, nota-se que a
questão
trata da Prototipação Horizontal.

Gabarito: Letra E

Item. 8. (FGV / BADESC - 2010) Analise o fragmento a seguir:

"A base de dados deve ser protegida para acesso apenas de usuários autorizados".
O fragmento acima apresenta um exemplo do seguinte requisito:

a) funcional.

b) de usuário.

c) de sistema.

d) de domínio.

e) não-funcional.

Comentários:

A questão trata de um Requisito Não-Funcional! Por que? Porque isso não é uma
funcionalidade a
ser implementada por um programador e disponibilizada ao usuário. É, na verdade, uma
restrição
tecnológica exigida no sistema. Lembrando que os requisitos não funcionais
estão raramente
associados às características individuais do sistema. Trata-se de qualidades globais de
um software,
como manutenibilidade, usabilidade, desempenho, custos e várias outras.

Gabarito: Letra E


Item. 9. (FGV / FIOCRUZ - 2010) Sobre os processos de engenharia de requisitos, na
elicitação e na
análise ocorre total interação com os stakeholders no sistema, sendo o principal objetivo:

a) a obtenção dos requisitos.

b) a homologação do sistema.

c) a elaboração do manual do usuário.

d) a conversão de especificações em requisitos.

e) a execução do estudo de viabilidade do sistema.

Comentários:

Nessa atividade, os engenheiros de software trabalham com os clientes e os usuários
finais do
sistema para aprender sobre o domínio da aplicação, quais serviços o sistema deve
fornecer, o
desempenho esperado do sistema, restrições de hardware, etc. O objetivo principal dessa
fase é a
obtenção dos requisitos!

Gabarito: Letra A

10.(FGV/ MEC-2009) Requisitos não-funcionais estão diretamente relacionados com a
satisfação
dos usuários. Assinale a alternativa que não indique um requisito não-funcional:

a) O sistema de arquivos deve ser protegido, para acesso, apenas, de usuários autorizados.

b) O software deve ser implementado usando os conceitos de orientação a objetos.

c) O tempo de desenvolvimento do software não deve ultrapassar seis meses.

d) O software poderá ser executado em plataforma windows e linux.

e) O software deve emitir relatórios de vendas a cada quinze dias.

Comentários:

Todos, exceto o último, são requisitos não-funcionais - restrições sobre o sistema. Já
o último é
uma funcionalidade a ser oferecida pelo sistema.

Gabarito: Letra E

Item. 11. (FGV / MEC - 2009) As declarações de serviços que o sistema deve fornecer, de
como ele deve
reagir a entradas específicas ou se comportar em determinadas situações, são chamadas de
requisitos:

a) não-funcionais.

b) de domínio.

c) de sistema.

d) funcionais.

e) de usuário.


Comentários:

A questão trata dos Requisitos Funcionais, isto é, declarações de serviços que um
sistema deve
fornecer, como o sistema deve reagir a entradas específicas e como o sistema deve (ou
não) se
comportar em situações particulares.

Gabarito: Letra D

Item. 12. (FGV / MEC - 2009) Existem técnicas que são usadas na fase de levantamento de requisitos para
coletar conhecimento dos usuários sobre os requisitos. Assinale a alternativa
que indique
apenas técnicas utilizadas na fase de levantamento de requisitos.

a) JAD, WFMS, WBS, cenários e brainstorming.

b) JAD, cenários, WFMS, questionários e intercepting.

c) cenários, entrevistas, protótipos, workshop, brainstorming.

d) leitura de documentos, protótipos, workshop, WBS e workflow.

e) brainstorming, protótipos, workflow, leitura de documentos e intercepting.

Comentários:

A única opção que apresenta apenas técnicas de levantamento de requisitos é:
Cenários,
Entrevistas, Protótipos, Workshop e Brainstorm!

Gabarito: Letra C

Item. 13. FGV / Senado Federal - 2008) Entre as atividades listadas a seguir, uma não faz
parte da
Engenharia de Requisitos. Assinale-a.

a) estudo de viabilidade.

b) análise de risco.

c) levantamento de necessidades do cliente.

d) verificação.

e) gerenciamento.

Comentários:


Pessoal, questão complicada! Essas fases não existem exatamente dessa maneira em nenhuma
bibliografia, então temos que fazer algumas associações. Estudo de Viabilidade é a
primeira fase;
Análise de Riscos não está em nenhum lugar; Levantamento de Necessidades do Cliente
pode ser
entendido como Elicitação de Requisitos; Verificação pode ser incluída na fase de
Validação (apesar
de eu não concordar); por fim, gerenciamento percorre de fato todas essas fases.

Gabarito: Letra B


QUESTõES CoMENTADAS - DIvERSAS BANCAS

í. (IBFC / IBGE - 2021) A etapa de levantamento de requisitos é composta por
diversas técnicas
que visam obter do cliente as informações necessárias para desenvolver o projeto do
sistema de
informação. Sobre essas técnicas, analise as afirmativas abaixo, dê valores Verdadeiro
(V) ou
Falso (F).

() Entrevistas não estruturadas: Informal ou sem agenda pré-definida.

() Brainstorming: Reunião com várias pessoas onde todos discutem um tema central.
() Prototipagem: Desenvolvimento de um modelo que simulará o sistema real.

a) F-F-F

b) F - F - V

c) V - F - V

d) V-V-F

e) V-V-V

Comentários:

(V) Correto. Essas entrevistas são úteis para obter um entendimento geral
sobre o que os
stakeholders fazem; (V) Correto. Brainstorming (também conhecida como Tempestade
de Ideias)
ocorre em um ambiente informal, buscando explorar a potencialidade criativa de
um grupo; (V)
Correto. É uma técnica que é utilizada no estágio inicial do projeto e ajuda os
stakeholders a
desenvolverem uma noção sobre a aplicação que irá ser implementada.

Gabarito: Letra E

Item. 2. (IDIB / CRF - MS - 2021) Em qual etapa do processo de desenvolvimento de
requisitos de
software mais comumente costuma acontecer a identificação de gaps nos
requisitos ou a
identificação de requisitos desnecessários, conforme eles se relacionam com o escopo definido?

a) Elicitação de requisitos.

b) Análise de requisitos.

c) Especificação de requisitos.

d) Validação de requisitos.

Comentários:

Bem, o nome das fases vai variar de autor para autor (e, às vezes, eles mesmos
mudam de ideia
entre um livro e outro), mas dá para responder por bom senso. A etapa
do processo de
desenvolvimento de requisitos de software mais comumente costuma acontecer a identificação de
gaps nos requisitos ou a identificação de requisitos desnecessários é a Análise de
Requisitos. Ela
ocorre logo após a Elicitação de Requisitos, que é responsável por identificar os requisitos.

Gabarito: Letra B

Item. 3. (IDIB / CRF - MS - 2021) "Uma descrição de uma propriedade ou característica que
um sistema
deve exibir ou uma restrição que ele deve respeitar". Tal definição se adequa a qual
tipo de
requisito de informação em um processo de software?

a) Requisito Funcional.

b) Requisito Não-Funcional.

c) Atributo de Qualidade.

d) Requisito do Usuário.

Comentários:

Os requisitos não-funcionais são restrições ou condições estipuladas sobre as quais o
sistema deve
funcionar. Além disso, eles podem descrever características do sistema como
confiabilidade,
segurança, usabilidade, performance, etc.

Gabarito: Letra B

Item. 4. (VUNESP / EBSERH - 2020) Considerando as técnicas utilizadas para a avaliação de
requisitos,
é correto afirmar que, na:

a) facilidade de verificação, deve-se verificar se não há requisitos conflitantes entre si.

b) verificação de consistência, deve-se verificar se os requisitos podem ser
implementados,
considerando a tecnologia existente.

c) verificação de realismo, deve-se verificar se todas as funções e restrições
planejadas estão
contempladas.

d) verificação de validade, deve-se verificar se não há requisitos conflitantes entre si.

e) verificação de completeza, deve-se verificar se todas as funções e restrições
planejadas estão
contempladas.

Comentários:

(a) Errado, essa é a definição da verificação de consistência; (b) Errado, essa é a
definição de
verificação de realismo; (c) Errado, essa é a definição de verificação de completeza;
(d) Errado, essa
é a definição de verificação de consistência; (e) Correto, é a definição correta de
verificação de
completeza.

Gabarito: Letra E


5- (VUNESP/ EBSERH -2020) Na engenharia de requisitos, um fator importante são os
requisitos
não funcionais, que se classificam em organizacionais, de produto e externos. Os requisitos
a) de produto têm origem em políticas e procedimentos da organização do cliente.

b) de produto compreendem fatores oriundos de fatores externos ao sistema e seu
processo de
desenvolvimento.

c) externos especificam o comportamento do produto, tais como o desempenho e a memória
requerida.

d) organizacionaistêm origem em políticas e procedimentos da organização do cliente.

e) organizacionais especificam o comportamento do produto, tais como o
desempenho e a
memória requerida.

Comentários:

(a) Errado, trata-se da definição de requisitos organizacionais; (b) Errado, trata-se da
definição de
requisitos externos; (c) Errado, trata-se da definição de requisitos de
produto; (d) Correto, os
requisitos organizacionais são derivados de políticas e procedimentos da organização do
cliente e
do desenvolvedor; (e) Errado, trata-se da definição de requisitos de produto.

Gabarito: Letra D

Item. 6. (COPESE - UFPI/ ALEPI- 2020) Um técnico de TI da ALEPI que gerencia
uma equipe de
desenvolvimento de software na Assembleia, eventualmente necessita fazer
levantamento de
requisitos da aplicação que está sendo desenvolvida. Sobre
os Requisitos
de Software, considere as seguintes afirmativas:

I. Requisitos funcionais são aqueles que definem parte da funcionalidade do sistema e podem
ser categorizados em três tipos: requisitos de produtos, requisitos organizacionais e
requisitos
externos.

II. Requisitos não-funcionais dizem respeito a restrições, aspectos de desempenho,
interfaces
com o usuário, confiabilidade, segurança, portabilidade e padrões.

III. Requisitos organizacionais estão relacionados às metas da empresa, suas
políticas
estratégicas adotadas, assim como assuntos relacionados aos empregados da empresa
com
seus respectivos objetivos.

IV. Requisitos de produto estão relacionados as restrições impostas por fatores
externos ao
sistema tais como restrições de interoperabilidade, éticas e legais.

Marque a opção que corresponde somente às afirmativas verdadeiras.

a) Apenas I, III e IV.


b) Apenas I, II e III.

c) Apenas I e III.

d) Apenas II e III.

e) Apenas II, III e IV.

Comentários:

(I) Errado. Apesar de a primeira parte da afirmação estar correta, a parte final
refere-se a Requisitos
Não-Funcionais; (II) Correto. Requisitos Não-Funcionais são restrições ou condições
estipuladas
sobre as quais o sistema deve funcionar; (III) Correto. Esse item define corretamente
os Requisitos
Organizacionais; (IV) Errado. Na verdade, a definição é de Requisitos Externos.

Gabarito: Letra D

Item. 7. (FAFIPA/ Prefeitura de Arapongas - PR - 2020) A Engenharia de Requisitos
é um termo
cunhado para descrever as atividades relacionadas à investigação e definição de escopo
de um
sistema de software, ou seja, trata-se do processo de descobrir, analisar, documentar e
verificar
as funções e restrições do sistema. Para auxiliar o levantamento de
requisitos, existe um
conjunto de técnicas de levantamento de dados que podem ser aplicadas em
conjunto ou
isoladamente, a depender das características do projeto. Assinale a alternativa que
apresenta
somente técnicas para descoberta de requisitos:

a) Sprint; Caso de Uso; Etnografia.

b) Entrevista; Caso de Uso; Etnografia.

c) Sprint; Refatoração; Etnografia.

d) JAD; Refatoração; Etnografia.

e) Entrevista; JAD; Refatoração.

Comentários:

De todos os itens citados, apenas Sprint e Refatoração não são técnicas
para descoberta de
requisitos.

Gabarito: Letra B

Item. 8. (IBFC / EBSERH - 2020) Requisitos são as bases para todo projeto, definindo o que
as partes
interessadas de um novo sistema necessitam e também o que o sistema deve
fazer para
satisfazer as suas necessidades. Antes do processo, propriamente dito, da
Engenharia de
Requisitos deve-se ter:

a) entrevistas e questionários com os usuários
b) a documentação dos requisitos
c) a revisão dos requisitos funcionais e não-funcionais
d) os estudos de viabilidade técnica/financeira
e) a revisão dos requisitos pelos usuários

Comentários:

(a) Errado, as entrevistas ocorrem na fase de Elicitação; (b) Errado, a documentação
ocorre na fase
de Elicitação; (c) Errado, a revisão dos requisitos ocorre na fase de Validação dos
Requisitos; (d)
Correto, os estudos de viabilidade ocorrem na primeira fase da Engenharia de
Requisitos, nela
ocorre uma avaliação rápida e de baixo custo para verificar se as necessidades dos
usuários podem
ser satisfeitas; (e) Errada, a revisão de requisitos ocorre na fase de Validação dos Requisitos.

Gabarito: Letra D

Item. 9. (INSTITUTO AOCP / Prefeitura de Betim - MG - 2020) A engenharia de requisitos
estabelece
uma ponte entre o projeto e a construção do software. Assinale a alternativa que
representa a
etapa na qual as metas de negócio são estabelecidas.

a) Levantamento.

b) Concepção.

c) Negociação.

d) Revisão.

e) Gestão.

Comentários:

Pessoal, é na etapa de Levantamento de Requisitos que se busca saber os requisitos
que o sistema
deve ter, ou seja, o que o cliente deseja que tenha em seu sistema. Além disso, os
stakeholders que
participam da etapa perguntam ao cliente qual é o objetivo do produto, como
o produto se
enquadra nas necessidades do negócio e como o produto será utilizado. A
partir disso são
estabelecidas as metas do negócio.

Gabarito: Letra A

io.(FAURGS /TJ-RS -2018) Requisitos não funcionais - como o nome sugere - são
requisitos que
não estão diretamente relacionados com os serviços específicos oferecidos pelo sistema a
seus
usuários. Podem ser provenientes das características requeridas para o
software, da
organização que desenvolve o software ou de fontes externas. Os requisitos não
funcionais que
especificam ou restringem o comportamento do software - como por
exemplo o seu
desempenho, seus requisitos de proteção, seus requisitos de usabilidade e a taxa
aceitável de
falhas-são denominados requisitos:

a) organizacionais.

b) de produto.


c) externos.

d) éticos.

e) ambientais.

Comentários:

Requisitos Não-
Funcionais


Requisitos de
Produtos

Requisitos de || Requisitos de | | Requisitos de
Requisitos de

Confiabilidade |I Proteção Ij Eficiência
Usabilidade

Requisitos
Ambientais

Requisitos
Operacionais

Requisitos de
Implementação


São os Requisitos de Produto: Confiabilidade, Proteção, Eficiência
Armazenamento) e Usabilidade.

(Desempenho e

Gabarito: Letra B

II.(FAURGS/TJ-RS-2oI8) Técnicas de descoberta de requisitos (às vezes chamada de
elicitação
de requisitos) é o processo de reunir informações sobre o sistema requerido e os
sistemas
existentes e separar dessas informações os requisitos do usuário e de sistema; o uso
destas
técnicas faz parte da maioria dos processos de engenharia de
requisitos.é o nome
dado a uma técnica em que o stakeholder responde a um conjunto predefinido de
perguntas
sobre o sistema usado no momento e sobre o sistema que será desenvolvido; os
requisitos
surgem a partir das respostas a essas perguntas.

A alternativa que contém o termo que completa corretamente a lacuna do texto acima é:

a) Entrevista fechada.

b) Entrevista aberta.

c) Etnografia.

d) Cenários.

e) Casos de uso.

Comentários:


A palavra-chave pra essa questão é "predefinido". Se é um conjunto de
perguntas a serem
respondidas por um stakeholder, é uma entrevista. Se essa entrevista já
possui um conjunto
predefinido de perguntas, ela é uma entrevista fechada.

Gabarito: Letra A

i2.(FAURGS/TJ-RS-2Oi8) Qual alternativa abaixo apresenta um requisito funcional de software?

a) A base de dados deve ser protegida para acesso apenas a usuários autorizados.

b) O tempo de resposta do sistema não deve ultrapassar 30 segundos..

c) O software deve ser operacionalizado no Sistema Operacional Windows.

d) O software deve emitir relatórios de vendas.

e) O tempo de desenvolvimento não deve ultrapassar três meses.

Comentários:

(a) Errado, isso é uma restrição a uma funcionalidade, logo é um RNF; (b) Errado,
isso é uma
restrição a uma funcionalidade, logo é um RNF; (c) Errado, isso é uma
restrição a uma
funcionalidade, logo é um RNF; (d) Correto, isso é uma funcionalidade a ser oferecida
pelo sistema,
logo é um RF; (e) Errado, isso é uma restrição a uma funcionalidade, logo é um RNF;

Gabarito: Letra D

i3.(FAURGS / TJ-RS - 2018) Considerando que, durante o processo de validação de
requisitos,
estes são submetidos a diferentes tipos de verificação, assinale a alternativa cuja
verificação
indica que no documento de requisitos não existem descrições diferentes para
uma mesma
função do sistema.

a) Verificação de consistência.

b) Verificação de completude.

c) Verificações de realismo.

d) Verificações de validade.

e) Prototipação.

Comentários:

Galera, essa dá para responder por bom senso! Se a questão diz que é uma verificação
de que não
existem descrições diferentes para uma mesma função, só pode ser uma
verificação de
consistência.

Gabarito: Letra A


iZj.(UFG / SANEAGO - 2017) Com relação à qualidade de software, é um exemplo de
requisito de
software não funcional:

a) calcular o valor do desconto conforme o perfil do cliente.

b) processar até 100 pedidos por segundo.

c) produzir o software em até dois anos e ter custo inferior a R$100.000,00.

d) limitar o cadastro de usuários ao Departamento de Pessoal.

Comentários:

(a) Errado, isso é uma funcionalidade, logo se trata de um RF; (b) Correto, isso é
uma restrição a
uma funcionalidade, logo é um RNF; (c) Errado, isso é um requisito de projeto e,
não, de software;

(d) Errado, isso é uma configuração e, não, um requisito de software.

Gabarito: Letra B

15.(UFG / SANEAGO - 2017) Alguns usuários estão insatisfeitos com um
software. Uma
investigação revelou que a origem da insatisfação decorre de uma omissão
(requisito não
especificado) na especificação de requisitos de software. Que atividade da
engenharia de
requisitos precisa ser revista para evitar problemas semelhantes?

a) Análise de viabilidade.

b) Validação.

c) Construção.

d) Elaboração do Termo de Abertura.

Comentários:

A atividade a ser revista é a Validação! Essa é a atividade responsável por encontrar
erros de
interpretação, ambiguidades e omissões.

Gabarito: Letra B

i6.(UFG / SANEAGO - 2017) São atributos de requisito de software:

a) custo (para implementar) e complexidade ciclomática.

b) prioridade e linguagem de implementação.

c) complexidade ciclomática e risco.

d) risco e identificador.

Comentários:


Honestamente, não sei de onde essa questão foi retirada, mas é possível responder por
eliminação:

(a) Errado, Complexidade Ciclomática é uma métrica; (b) Errado, requisitos são
independentes de
linguagem de programação; (c) Complexidade Ciclomática é uma métrica; (d)
Correto, risco e
identificador.

Gabarito: Letra D

i7.(UFG / SANEAGO - 2017) Uma Engenharia de Requisitos (ER) bem estruturada
garante
qualidade, confiabilidade e integridade ao produto de software a ser desenvolvido. O
conjunto
de atributos que evidencia o esforço necessário para fazer modificações
especificadas no
software é uma característica de:

a) portabilidade.

b) confiabilidade.

c) manutenibilidade.

d) eficiência.

Comentários:

Em engenharia de software, manutenibilidade é um aspecto da qualidade de software que
se refere
à facilidade de um software de ser modificado a fim de corrigir defeitos,
adequar-se a novos
requisitos, aumentar a suportabilidade ou se adequar a um ambiente novo. Era possível
responder
essa por bom senso!:)

Gabarito: Letra C

Item. 18. (IBFC / EBSERH - 2017) Quanto aos vários tipos de requisitos assinale, das
alternativas abaixo,
a única que NÃO identifica corretamente um clássico requisito não-funcional:

a) requisito de implementação da arquitetura do sistema
b) requisitos de funcionalidades do sistema
c) requisito de interoperabilidade da arquitetura do sistema
d) requisitos de confiabilidade da arquitetura do sistema
e) requisitos de portabilidade da arquitetura do sistema

Comentários:

(a) Errado, requisitos de arquitetura realmente são não-funcionais; (b) Correto,
requisitos de
funcionalidades do sistema definitivamente não são requisitos não-funcionais;
(c) Errado,
requisitos de interoperabilidade realmente são não-funcionais; (d)
Errado, requisitos de
confiabilidade da arquitetura realmente são não-funcionais; (e) Errado, requisitos
de portabilidade
da arquitetura realmente são não-funcionais.


Gabarito: Letra B

ig.(IBFC / EBSERH - 2017) A Análise de Requisitos é a primeira fase de
desenvolvimento de
software dividido em Requisitos funcionais e Requisitos não-funcionais. Os
Requisitos não-
funcionais possuem vários tipos diferentes de classificação tais como:

(1) Requisitos de confiabilidade.

(2) Requisitos de produtos.

(3) Requisitos éticos.

(4) Requisitos de portabilidade.

a) da relação apresentada existem somente o 2, 3 e 4

b) da relação apresentada existem somente o i, 3 e 4

c) da relação apresentada existem somente o 1, 2 e 4

d) da relação apresentada existem somente o 1, 2 e 3

e) da relação apresentada existem todos.

Comentários:

(1) Requisitos de Confiabilidade são RNF; (2) Requisitos de Produtos são RNF; (3)
Requisitos Éticos
são RNF; (4) Requisitos de Portabilidade são RNF. Logo, todos eles são RNF.

Gabarito: Letra E

2O.(CESGRANRIO / IBGE-2016) Um dos objetivos da disciplina de requisitos é:

a) criar um esboço inicial da arquitetura do sistema a ser desenvolvido.

b) adaptar e configurar o processo de desenvolvimento de modo a atender às
especificidades
do sistema a ser desenvolvido.

c) fornecer uma base para estimar o custo e o tempo de desenvolvimento de um sistema.

d) assegurar que os clientes, os usuários e os desenvolvedores tenham um
entendimento
comum da organização na qual um sistema será implantado.

e) entender a estrutura e a dinâmica da organização na qual um sistema será implantado.

Comentários:

(a) Errada. A arquitetura do sistema só é esboçada após os requisitos terem sido
colhidos com os
steakholders; (b) Errada. A adaptação e configuração do sistema são uma coisa maiorque
em parte
utiliza as especificidades do sistema e se baseia nos requisitos colhidos do sistema, contudo isso
não é objetivo da engenharia de requisitos; (c) Correta. Custo e Tempo são uma das
preocupações
principais de quem desenvolve e necessita de software, e os requisitos ajudam a
fornecer uma boa
base para essa estimativa; (d) Errada. Pessoal, entender como a organização não é um
objetivo da
disciplina de requisitos; (e) Errada. Esse talvez seja um dos objetivos da disciplina
de análise de
negócio.

Gabarito: Letra C

2i.(IBFC / MGS - 2015) A definição: "descrevem as funcionalidades que se espera que o
sistema
disponibilize, de uma forma completa e consistente. É aquilo que o usuário espera que
o sistema
ofereça, atendendo aos propósitos para qual o sistema será desenvolvido.",
corresponde
tipicamente aos:

a) Requisitos Funcionais.

b) Requisitos Externos.

c) Requisitos não-Funcionais.

d) Requisitos da Aplicação.

Comentários:

Funcionalidades que se espera que 0 sistema disponibiliza? Já podemos dizer que se
trata de
requisitos funcionais.

Gabarito: Letra A

22.CESGRANRIO / IBGE-2014) Solicitado para fazer o levantamento dos requisitos para um
novo
software a ser desenvolvido, um analista de sistemas identificou a necessidade de
descobrir
todos aqueles que se beneficiariam de forma direta ou indireta do sistema a ser desenvolvido.

Essas pessoas são conhecidas como:

a) clientes
b) partes interessada
c) patrocinadores
d) usuários
e) usuários finais

Comentários:

Pessoal, só atentem para o fato de que o conceito de Partes Interessadas
(Stakeholders) é mais
amplo que o de Patrocinadores, uma vez que os Patrocinadores são envolvidos que tem
benefícios
diretos e influenciam diretamente o projeto, já as Partes Interessadas consideram mesmo aqueles
que não tem qualquer influência sobre o projeto, mas mesmo de
forma indireta são
beneficiados/prejudicados.

Gabarito: Letra B

Item. 23. (ESAF / CVM - 2010) Assinale a opção correta.

a) Gestão de requisitos preocupa-se com a documentação, atualização e
controle de
stakeholders envolvidos na fase de identificação da demanda.

b) Engenharia de requisitos compreende: identificar, analisar, especificar
e definir as
necessidades de negócio que um aplicativo deve prover para solução do problema levantado.

c) Engenharia de requisitos compreende: planejar, especificar e desenvolver as
necessidades de
negócio que um aplicativo deve prover para minimização dos problemas levantados.

d) Engenharia de requisitos compreende: identificar, analisar, programar e testar os
programas
das necessidades de solução de problemas que um negócio deve prover para satisfazer usuários.

e) Gestão de requisitos preocupa-se com a documentação, direcionamento,
controle de
definição e acesso aos requisitos levantados na fase de planejamento de escopo.

Comentários:

(a) Errado, documentação, atualização e controle de stakeholders não é gestão de
requisitos; (b)
Correto, trata das necessidades para solucionar um problema; (c) Errado, na
engenharia de
requisitos não se desenvolve as necessidades de negócio, entre outros erros; (d)
Errado, programar
não é uma das atividades, entre outros erros; (e) Errado, planejamento de escopo não
é foco da
engenharia de requisitos.

Gabarito: Letra B

24.(ESAF / MPOG -2010) As áreas de esforços da Análise de Requisitos são:

a) reconhecimento dos objetivos, avaliação e controle, modelagem, estruturação e revisão.

b) reconhecimento do problema, avaliação e síntese, modelagem, especificação e revisão.

c) reengenharia, planejamento, avaliação e controle, modelagem e conclusão.

d) reconhecimento do problema, análise e síntese, reengenharia, especificação e
análise de
resultados.


e) reconhecimento do problema, modelagem, especificação de entidades,
estruturação e
revisão.

Comentários:

Essa questão foi retirada do livro do Denis Alcides Rezendo, que afirma que, a partir
do relato e
necessidades, a análise de requisitos possibilita que o Engenheiro de Software
especifique as
funções, o desempenho, interfaces, restrições, etc do software. Proporciona avaliar a
qualidade de
atendimento e satisfação, podendo ser dividido em cinco áreas de esforço:
reconhecimento do
problema, avaliação e síntese, modelagem, especificação e revisão.

Gabarito: Letra B

25.(ESAF / AFRFB - 2005) Durante a análise de requisitos, são especificados
a função e o
desempenho do software, bem como a sua interface com outros elementos do sistema. Nessa
etapa, também, são estabelecidas as restrições de projeto, a que o software deve atender.

Comentários:

Pessoal, o que essa questão quis dizer? Especificar função = Requisitos Funcionais;
Especificar
Desempenho e Restrições = Requisitos Não-Funcionais.

Gabarito: Correto

26.(ESAF / AFRFB - 2005 - Letra E) Durante a especificação dos requisitos, são
estabelecidos os
critérios que permitirão ao desenvolvedor e ao cliente avaliar a qualidade, assim que
o software
for construído.

Comentários:

Perfeito! A partir da especificação de requisitos que se avalia a qualidade.

Gabarito: Correto


LISTA DE QUESTõES - CESPE

í. (CESPE / BANRISUL - 2022) Requisitos não funcionais de um sistema descrevem seu
objetivo
e dependem do tipo de software a ser desenvolvido, dos usuários esperados para o
software e
da abordagem geral adotada pela organização ao escrever os requisitos.

Item. 2. (CESPE / BANRISUL - 2022) Requisitos organizacionais são requisitos de
sistema amplos,
derivados das políticas e dos procedimentos nas organizações do cliente e do
desenvolvedor,
cujas funções incluem definir como o sistema será utilizado e especificar a
linguagem de
programação.

Item. 3. (CESPE / BANRISUL - 2022) Os requisitos do sistema devem descrever os
comportamentos
interno e externo do sistema, devendo-se preocupar com a forma como ele deve ser
projetado
ou implementado.

Item. 4. (CESPE / BANRISUL - 2022) A especificação de requisitos é frequentemente
composta de
vários tipos de documentos e não raro abrange: visão geral; glossário; modelos do
sistema; lista
de requisitos funcionais e lista de requisitos não funcionais; especificação
detalhada de
requisitos.

Item. 5. (CESPE / BANRISUL - 2022) O objetivo principal da especificação é documentar
todas as
necessidades dos clientes e obter um aceite quanto às entregas de produto propostas.

Item. 6. (CESPE / BANRISUL - 2022) Na execução da técnica de apprenticing
(aprendizado), o
engenheiro de requisitos deve questionar procedimentos operacionais complexos e
pouco
claros do domínio do sistema que os stakeholders desejam preservar.

Item. 7. (CESPE / BANRISUL - 2022) Em situações em que alguma das partes interessadas não
consiga
expressar de forma oral as suas necessidades com clareza, recomenda-se o emprego da
técnica
da etnografia para o levantamento de requisitos.

Item. 8. (CESPE / BANRISUL-2022) O levantamento de requisitos com casos de uso é muito
eficaz para
a elicitação de requisitos não funcionais.

Item. 9. (CESPE/BANRISUL-2022) A analogia é uma técnica pouco recomendada quando é necessário
identificar requisitos novos, inovadores ou atrativos, em um ambiente cujo objetivo é
encontrar
soluções criativas.

Item. 10. (CESPE / BANRISUL-2022) A arqueologia é uma técnica apropriada quando se busca
preservar
todas as funcionalidades de um sistema legado em um novo sistema que reutilize as
soluções e
experiências existentes.

Item. 11. (CESPE / MPC-SC - 2022) A etnografia é o processo de elicitação por meio do qual
o analista de
requisitos realiza uma imersão no ambiente de trabalho em que o sistema será utilizado para
tornar compreensíveis os processos operacionais e auxiliar na extração dos requisitos de
apoio
de tais processos.

Item. 12. (CESPE / BNB - 2022) Para capturar os requisitos da interface de um sistema, os
protótipos
podem ser desenhados como mockups, mesmo que estes não permitam interações do usuário
com a execução das funcionalidades.

Item. 13. (CESPE / BNB - 2022) Um dos critérios de boa qualidade para uma história de
usuário é o
denominado critério pequeno, ou seja, aquele cujo desenvolvimento da
história deve
representar um trabalho desenvolvido dentro de um limite de tempo de duração específica.

Item. 14. (CESPE/ BNB-2022) Em uma história de usuário, em que se deseja fazer login com a
impressão
digital do cliente para o seu acesso à sua conta bancária, um exemplo correto de
critério de
aceitação é: dado que estou realizando login com minha digital, quando eu
colocar o dedo
cadastrado no leitor, então consigo acessar minha conta.

Item. 15. (CESPE / BNB - 2022) No gerenciamento de requisitos, uma adequada
configuração, em
particular, de uma especificação tem a propriedade de ser imutável.

Item. 16. (CESPE / BANRISUL-2022) O levantamento de requisitos com casos de uso é muito
eficaz para
a elicitação de requisitos não funcionais.

Item. 17. (CESPE / BANRISUL-2022) Em situações em que alguma das partes interessadas não
consiga
expressar de forma oral as suas necessidades com clareza, recomenda-se o emprego da
técnica
da etnografia para o levantamento de requisitos.

Item. 18. (CESPE / BANRISUL - 2022) A acessibilidade está relacionada à facilidade
com que
determinada informação é assimilada por pessoas com alguma deficiência.

ig.(CESPE / BANRISUL-2022) A usabilidade é um atributo de qualidade de um projeto que
avalia
se ele fornece os recursos que os usuários precisam.

Item. 20. (CESPE / FUNPRESP-EXE - 2022) As verificações de validade, consistência e
completeza são
técnicas fundamentais do processo de validação de requisitos.

Item. 21. (CESPE / FUNPRESP-EXE - 2022) Dentre as técnicas existentes de elicitação de
requisitos
baseadas em cenários, os casos de uso são modelos que ajudam a identificar
agentes e
interações do sistema.

Item. 22. (CESPE / FUNPRESP-EXE - 2022) A técnica Quality Function Deplyment tem como
objetivo
traduzir os requisitos técnicos em requisitos do cliente.

Item. 23. (CESPE / FUNPRESP-EXE - 2022) O protótipo de interface do usuário é o produto
final da
técnica de prototipação da engenharia de requisitos.


Item. 24. (CESPE / FUNPRESP-EXE - 2022) Brainstorming é uma técnica utilizada para o
levantamento
de requisitos; para facilitar o registro, essa técnica deve ser feita por meio de questionário.

Item. 25. (CESPE / Petrobrás - 2022) Ferramentas automatizadas para armazenamento de
requisitos,
gerenciamento de mudanças e gerenciamento de rastreabilidade são indicadas para apoio ao
processo de gerenciamento de requisitos.

Item. 26. (CESPE / Petrobrás - 2022) Histórias de usuário são ferramentas para a definição
de escopo de
produtos de software voltadas a fornecer uma análise detalhada sobre a atividade do
usuário e
a viabilizar a retenção de conhecimento em longo prazo.

Item. 27. (CESPE / Petrobrás - 2022) Os critérios de aceitação descrevem um
conjunto mínimo de
requisitos que precisam ser atendidos para que valha a pena implementar uma
solução
específica.

Item. 28. (CESPE / Petrobrás - 2022) Entrevistas e questionários são técnicas comumente
usadas para
obter informações relacionadas às necessidades de grupos de usuários
representados por
personas, que exemplificam como um usuário típico interage com um produto.

2g.(CESPE / Petrobrás - 2022) No contexto de storytelling, é fundamental mitigar as
possibilidades
de navegação por meio das interfaces e impor à experiência do usuário o
sequenciamento
estrito das atividades que constituem a sua história.

Item. 30. (CESPE / TJ-RJ - 2021) Na engenharia de requisitos, por estar mais aderente às
características
dessa técnica, a etnografia é recomendada:

a) na elicitação da forma como o fluxo dos processos deveria ser feito.

b) na descoberta dos requisitos organizacionais.

c) quando se deseja obter uma visão do funcionamento do sistema na forma
prevista,
independentemente das interferências de seu contexto.

d) na descoberta de requisitos derivados do conhecimento das atividades de outras
pessoas que
realizam trabalhos adjacentes ao analisado.

e) como uma alternativa aos casos de uso para a descoberta dos requisitos explícitos.

Item. 31. (CESPE / TJ-RJ -2021) Para os propósitos da modelagem dos requisitos com base em
cenários,
um suporte apropriado é o uso de
a) diagrama de casos de uso e histórias de usuários.

b) diagrama de sequência e diagrama de atividades.

c) diagramas que representem eventos ou estados.

d) diagrama de classes e histórias de usuário.

e) modelagem com cartões CRC e casos de uso.


Item. 32. (CESPE / TELEBRÁS - 2021) No âmbito da engenharia de software, o principal
produto da
engenharia de requisitos é o documento de especificação de requisitos de software.

Item. 33. (CESPE / TCE-RJ - 2021) O gerenciamento de requisitos trata do
desenvolvimento
de software por meio da metodologia ágil; isso permite o isolamento entre o
desenvolvedor e o
usuário, já que é comum ocorrer problema de mudanças de requisitos ao longo do curso
do
projeto devido ao interfaceamento do usuário com o desenvolvedor.

Item. 34. (CESPE / TCE-RJ - 2021) Em um processo de desenvolvimento de software, a
elicitação de
requisitos serve para identificar os fatos que compõem os requisitos do sistema.

Item. 35. (CESPE / Ministério da Economia - 2020) Um dos princípios em que se baseia a
técnica de
dinâmica de grupo conhecida como brainstorm é o atraso de julgamento, que
possibilita a
geração de muitas ideias antes de se decidir por uma.

Item. 36. (CESPE / Ministério da Economia - 2020) Os requisitos do software mudam com
frequência,
mas é sempre possível acomodá-los no sistema, pois o software é flexível.

Item. 37. (CESPE / Ministério da Economia - 2020) Requisitos funcionais envolvem as
características de
confiabilidade e de desempenho de um sistema.

Item. 38. (CESPE / Ministério da Economia - 2020) Elicitar requisitos não inclui somente
necessidades
dos usuários, mas também extrair informações que surgem de padrões
organizacionais,
governamentais e industriais em geral, para atender necessidades.

Item. 39. (CESPE / TJ-AM - 2019) A validação dos requisitos exclui diversas considerações,
entre elas, a
que verifica o impacto da implementação dos requisitos identificados sobre o
orçamento do
sistema.

Item. 40. (CESPE / TJ-AM - 2019) Na gerência de requisitos, as mudanças no documento de
requisitos
devem aumentaras referências a outros documentos e aprimorara interdependência entre suas
próprias seções.

Item. 41. (CESPE / TJ-AM - 2019) Uma especificação de requisitos é inconsistente quando, por
exemplo,
em um de seus subconjuntos conste que o pagamento será feito antes do
fechamento da
compra e, em outro subconjunto, conste que o pagamento será feito depois do fechamento
da
compra.

Item. 42. (CESPE/TJ-AM -2019) Em um protótipo para validar os requisitos de um software, é
admissível
deixar de fora os requisitos não funcionais ou reduzir seus padrões.

Item. 43. (CESPE / SLU-DF - 2019) A interoperabilidade entre um software
que esteja em
desenvolvimento e outros sistemas existentes é considerada um requisito funcional.


44-(CESPE/STM-2oI8) Requisitos de domínio são relativos ao que o sistema deve fornecer,
como
ele deve reagir a entradas específicas e se comportar em determinadas situações,
enquanto os
requisitos funcionais são restrições sobre os serviços ou as funções oferecidas pelo sistema.

45.(CESPE / STM - 2018) O processo de verificação visa assegurar que o
sistema atende as
expectativas e necessidades do cliente por meio da utilização de técnicas de entrevista
como
brainstorming, grupos focais ou Delft, a partir das quais são extraídos os
requisitos não
funcionais.

Zj6.(CESPE/CGM-PB-20i8) A atividade de gerência de requisitos é a responsável por
garantir que
mudanças nos requisitos sejam feitas de maneira controlada e documentada, administrando
os
relacionamentos entre os requisitos e as dependências entre o documento de requisitos e
os
demais artefatos produzidos no processo de software.

Item. 47. (CESPE / ABIN - 2018) Ao se aplicar a rastreabilidade bidirecional, é possível
determinar se
todos os requisitos-fonte foram completamente tratados e se todos os requisitos
do produto
atendem aos requisitos do cliente.

Item. 48. (CESPE / ABIN - 2018) Definir e manter matriz de rastreabilidade dos
requisitos permite
controlar e tratar as mudanças em requisitos durante o processo de elicitação e
especificação
do produto.

4g.(CESPE / ABIN - 2018) Para que os requisitos sejam refinados e sejam gerados
modelos de
análise e projeto para codificação, apenas a avaliação e a aprovação por parte do
cliente —
mesmo após o entendimento dos requisitos — não são suficientes.

Item. 50. (CESPE / ABIN - 2018) De acordo com as técnicas facilitadoras de especificação de
aplicação,
recomenda-se que a descrição de requisitos e regras seja feita diretamente pela equipe
técnica,
sem a participação do cliente.

Item. 51. (CESPE / ABIN - 2018) No processo de elicitação de requisitos, há atividades
relacionadas a
identificação, rastreabilidade e mudanças em requisitos.

Item. 52. (CESPE / EBSERH - 2018) Na especificação de requisitos, são estabelecidos uma
escala de
medição e os valores aceitáveis para cada requisito de usuário, tornando-o mensurável,
ou seja,
adicionando a ele um critério de aceitação.

Item. 53. (CESPE / EBSERH - 2018) Requisitos externos são derivados de metas,
políticas e
procedimentos das organizações, do cliente e do desenvolvedor e incluem
requisitos de
processo, requisitos de implementação, restrições de entrega e restrições orçamentárias.

Item. 54. (CESPE / IPHAN - 2018) Tanto a etnografia quanto o protótipo podem ser
utilizados para
validação e elicitação de requisitos, contudo a aplicação de um elimina a possibilidade de uso do
outro no mesmo cenário, pois se tratam de técnicas excludentes.


55- (CESPE / IPHAN - 2018) A validação de requisitos se sobrepõe à análise de
requisitos, pois tem
a finalidade de encontrar eventuais problemas nos requisitos e
validá-los conforme as
necessidades dos usuários do sistema.

56.(CESPE / IPHAN - 2018) Situação hipotética: Como forma de obter os requisitos de
apoio para
desenvolver um sistema a ser implementado em determinado setor de uma organização, um
analista propôs que se observasse o trabalho do dia a dia, anotando-se as tarefas
realizadas no
referido setor. Assertiva: Para o cenário proposto, é ideal a utilização da técnica de
caso de uso
alinhada à entrevista.

Item. 57. (CESPE / IPHAN - 2018) Situação hipotética: Na metodologia de desenvolvimento de
software
customizada para uma organização, o analista propôs o uso da prototipação na
fase de
engenharia de requisitos, contudo julgou inviável a utilização da prototipação na fase
de projeto
de sistemas. Assertiva: Nessa situação, a proposta do analista está incorreta, pois a
prototipação
tanto pode ser utilizada no processo de engenharia de requisitos, para ajudar na
elicitação de
requisitos, quanto no projeto de sistema, para apoiar o projeto de interface de usuário.

Item. 58. (CESPE / PF-2018) No desenvolvimento de um sistema de informação, a fase de
levantamento
de requisitos consiste em compreender o problema, dando aos desenvolvedores e usuários a
mesma visão do que deve ser construído para resolvê-lo, e a fase de
projeto consiste na
realização da descrição computacional, incluindo a arquitetura do sistema, a
linguagem de
programação utilizada e o sistema gerenciador de banco de dados (SGBD) utilizado.

Item. 59. (CESPE / MPE-PI - 2018) A análise de requisitos consiste na área responsável pela
identificação
das reais necessidades dos clientes de TI. Por meio da análise de requisitos, em
conjunto com o
cliente, é possível construir uma solução que atenda essas necessidades e
desenvolver os
requisitos funcionais elencados.

Item. 60. (CESPE / MPE-PI - 2018) Situação hipotética: Ao se iniciar a especificação de
requisitos de um
software para controlar o gasto de folhas impressas de um setor, o analista
de requisitos,
juntamente com o gestor, definiu um cenário de teste em que, ao se comandar a
impressão, a
chave do usuário autenticado no sistema que comandar uma impressão acionará o contador
de
impressões do setor de locação desse usuário. Assertiva: Nessa situação, o teste
validará o
cenário do requisito definido junto com o gestor.

Item. 61. (CESPE / SE-DF - 2017) Para auxiliar na gerência de riscos e prevenir
insatisfações das partes
interessadas, deve-se dificultar as modificações na especificação dos requisitos.

62.(CESPE / SE-DF - 2017) Um dos objetivos da engenharia de requisitos é
integrar tarefas,
técnicas, orientações, responsabilidades e papéis em fluxos de trabalho.

63.(CESPE / SE-DF - 2017) É comum que uma especificação de requisitos inclua as
interfaces
externas do software.


64-(CESPE / TRE-PE - 2017) No contexto da análise de requisitos, confiabilidade e usa b i I ida d e
são
atributos de qualidade classificados como:

a) requisitos funcionais.

b) requisitos de domínio.

c) requisitos não funcionais.

d) dependências.

e) regras de negócio.

Item. 65. (CESPE /TCE-PR-2016) Com relação aos requisitos de software, assinale a opção correta.

a) O documento de especificação de requisitos é um documento restrito à
equipe de
desenvolvimento de software.

b) As necessidades do usuário são informações que substituem os requisitos do software.

c) Os requisitos de produto e os requisitos organizacionais são tipos de requisitos funcionais.

d) Os requisitos funcionais descrevem as funcionalidades, os recursos e as
características do
software.

e) Os requisitos não funcionais referem-se diretamente às características do software.

Item. 66. (CESPE / TRT-PR - 2016 - Letra D) Durante a fase de levantamento de
requisitos para a
construção de um software, compete aos desenvolvedores organizar as necessidades em ordem
de prioridade.

Item. 67. (CESPE / TRT-PR - 2016 - Letra E) O QFD (quality function deployment)
identifica como
requisitos fascinantes os recursos que extrapolam as expectativas dos clientes.

Item. 68. CESPE / MPOG-ATI - 2015) Tão logo exista uma versão do documento de
requisitos, o
processo de gerenciamento de requisitos deverá ser iniciado.

Item. 69. (CESPE / MPOG-ATI - 2015) As informações de rastreabilidade de requisitos
possibilitam a
realização de estimativa do custo de mudanças em requisitos.

Item. 70. (CESPE / MPOG-ATI - 2015) As mudanças de requisitos em
processos ágeis de
desenvolvimento não seguem um processo formal de gerenciamento de requisitos.

Item. 71. (CESPE / MPOG-ATI - 2015) Para a elicitação dos requisitos, é indicada à empresa
a realização
de um workshop de requisitos, em que seja determinado um facilitador, mesmo que sem
grande
experiência com os processos de gerenciamento de requisitos.


ji.(CESPE / MPOG-ATI - 2015) Os requisitos não funcionais a serem especificados
estabelecerão
restrições que devem ser seguidas portodo o sistema da referida empresa, podendo até
mesmo
levar à necessidade de definição de requisitos funcionais.

Item. 73. (CESPE / MPOG-ATI - 2015) A definição de um protótipo para a validação dos
requisitos pode
tornar o processo de requisitos mais barato e mais simplificado, já que ele vai
corresponder à
real forma de uso do sistema a ser construído.

Item. 74. (CESPE / MPOG-ATI - 2015) Uma forma de validação dos requisitos é a geração de
casos de
teste para os requisitos documentados.

Item. 75. (CESPE / MPOG-ATI - 2015) No ciclo de vida do software, o congelamento dos
requisitos do
software garante que este, quando em desenvolvimento, atenda à expectativa do
usuário,
desde que tudo que tenha sido requisitado seja implementado.

Item. 76. (CESPE/ STJ - 2015) Os requisitos ambientais, operacionais e de
desenvolvimento são
organizacionais e não funcionais.

Item. 77. (CESPE / STJ - 2015) Os requisitos reguladores, legais e éticos são externos e não funcionais.

Item. 78. (CESPE / TJDFT- 2015) O uso de protótipo auxilia a descoberta e a validação dos
requisitos de
software.

Item. 79. (CESPE / TJDFT - 2015) As técnicas de elicitação e especificação de requisitos
incluem a
etnografia, a qual é utilizada para compreender os requisitos sociais e
organizacionais para
determinado projeto.

Item. 80. (CESPE / TJDFT - 2015) É caracterizada como requisito funcional a exigência de
que, em
determinado projeto, o software desenvolvido funcione no sistema operacional Linux, uma
vez
que essa exigência está diretamente ligada ao software.

Item. 81. (CESPE / MPU - 2013) As atividades do gerenciamento de requisitos incluem a
análise e a
negociação, a qual visa garantir que todos os requisitos do sistema tenham sido
declarados de
modo não ambíguo, sem inconsistências, omissões e erros.

Item. 82. (CESPE / MPE-PI - 2012) Identificada facilidade do cliente em entender
uma especificação
matemática, é correto utilizar, também, na especificação dos requisitos, notações
baseadas em
máquinas de estado finito, uma vez que elas podem reduzir a ambiguidade de um
documento
de requisitos.

Item. 83. (CESPE / EBC - 2011) No processo de construção e (ou) manutenção de um produto
de
software, o termo requisito pode ser definido da seguinte forma: uma condição, característica
ou capacidade, determinada no universo das necessidades do negócio do usuário, que deve
ser
atendida por um software na forma de aspectos funcionais e não funcionais.

84.CESPE / EBC - 2011) O principal artefato elaborado no processo de produção de
requisitos do
sistema, segundo a ER, é o documento de requisitos. Por sua vez, o documento de
requisitos é
uma declaração formal dos requisitos para os stakeholders, que podem ser clientes,
usuários
finais ou a equipe de desenvolvimento do software.

8s.(CESPE / BRB - 2011) O levantamento de requisitos de software privilegia
a visão do
desenvolvedor em relação aos requisitos de um produto. Já a análise dos requisitos
prioriza a
visão que o cliente e os usuários têm dos requisitos de um produto.

Item. 86. (CESPE / FUB - 2011) A etnografia, uma técnica de levantamento de
requisitos, é uma
abordagem completa para elicitação, utilizada para compreender os
requisitos sociais e
organizacionais e que identifica novas características a serem acrescentadas em um sistema.

Item. 87. (CESPE / EBC -2011) Uma das principais técnicas de verificação é a prototipação.
Um protótipo
é um produto parcialmente desenvolvido, que possibilita aos clientes e
desenvolvedores
examinarem certos aspectos do sistema proposto e decidir se eles são ou não
apropriados ou
adequados para o produto acabado.

Item. 88. (CESPE / TJ-ES - 2011) Assim como o software, os requisitos também devem
ser avaliados
quanto à qualidade. A validação, atividade da engenharia de requisitos, é
responsável por
garantir que os requisitos tenham sido declarados de forma clara e precisa.
Além disso, a
validação busca detectar inconsistências, erros e omissões, objetivando alinhar os
requisitos às
normas estabelecidas para o projeto, produto e processo.

Item. 89. (CESPE / STM - 2011) São consideradas técnicas de validação de requisitos:
revisões de
requisitos, prototipação e geração de casos de teste.

Item. 90. (CESPE / TJ-ES - 2011) Verificação e validação são atividades da
análise de software,
necessárias para se identificar o que o software precisa executar, seguida de uma
avaliação do
usuário quanto às atividades definidas.

Item. 91. (CESPE / MEC - 2011) A rastreabilidade de requisitos ocorre apenas na
relação entre os
requisitos propriamente ditos e os artefatos ou subprodutos de desenvolvimento gerados.

Item. 92. CESPE / ABIN - 2010) Requisitos não funcionais são restrições sobre os serviços
ou as funções
oferecidas pelo sistema, e podem ser, também, declarações de serviços que o sistema
deve
fornecer, como o sistema deve reagir a entradas específicas e como deve comportar-se em
diversas situações.


93.(CESPE / MPU - 2010) Os requisitos normativos, geralmente oriundos da análise das
regras de
negócio a que está submetido um sistema, nunca podem ser considerados requisitos
funcionais,
por estarem fora do sistema, ou seja, do domínio do negócio.

94.(CESPE IABIN -2010) Se os requisitos forem organizados de acordo com os diversos
pontos de
vista relativos a grupos de usuários do sistema, é possível identificar aqueles comuns
a todos ou
à maioria dos pontos de vista. Esses requisitos comuns podem estar relacionados a
assuntos
separados, implementados como extensões da funcionalidade central.

Item. 95. (CESPE / MPU - 2010) O levantamento de requisitos é realizado ao final da
primeira versão de
um protótipo, para se definir, junto aos envolvidos no processo, quais são as
premissas básicas
para o início do entendimento das funcionalidades desejadas.

Item. 96. (CESPE / MPU - 2010) Embora a criação de uma sequência ilustrada de telas
por meio de
programas de desenho gráfico seja útil para a identificação de alguns requisitos do
software, ela
não é considerada uma atividade de prototipação por não envolver o uso de uma
linguagem de
programação.

Item. 97. (CESPE / DETRAN-ES - 2010) A técnica de brainstorm é adequada para a
produção de
especificações de requisitos para um sistema de informação em desenvolvimento.

Item. 98. (CESPE / MPU - 2010) A verificação de requisitos tem por objetivo analisar se os modelos
' construídos estão de acordo com os requisitos definidos. Por sua vez, a validação de requisitos
visa assegurar que as necessidades do cliente estão sendo atendidas portais requisitos.

Item. 99. (CESPE/TCU-2010) Por se tratar de função essencial da engenharia de
requisitos, a gestão
formal de requisitos é indispensável mesmo para projetos de pequeno porte, com apenas
duas
ou três dezenas de requisitos identificáveis.

Item. 100. (CESPE / DETRAN-DF - 2009) Requisitos funcionais são restrições sobre as
funções ou
serviços oferecidos pelo sistema. Esses requisitos consideram as declarações de
serviços, a
forma do sistema reagir e como ele deve se comportar em determinadas situações.
Cenários e
casos de uso são técnicas eficazes para elicitação de requisitos funcionais segundo
pontos de
vista de interação.

Item. 101. (CESPE / IPEA - 2009) Elicitação envolve a identificação sistemática de
requisitos nem
sempre explicitados pelos clientes. Protótipos, pesquisas estruturadas, testes-beta,
análise de
casos de negócio, walkthroughs, QFD, grupos de trabalho são exemplos de técnicas
utilizadas
para elicitar necessidades, expectativas, restrições e interfaces dos stakeholders para
todas as
fases do ciclo de vida do produto.

Item. 102. (CESPE / TCE-RN - 2009) A etnografia é uma técnica utilizada para a
descoberta de
requisitos de sistemas de software na qual, por meio de observações, procura-se
compreender
os requisitos sociais e organizacionais do ambiente onde o sistema será usado.


103- (CESPE / IPEA-2009) A política organizacional para o planejamento e execução do
processo
de gerenciamento de requisitos reflete as expectativas organizacionais para
processos de
gestão de requisitos e para que seja possível identificar inconsistências entre os
requisitos e os
planos do projeto.

Item. 104. (CESPE / STJ - 2008) Os requisitos de um sistema podem ser descrições dos
serviços
fornecidos ou restrições operacionais. Requisitos podem ainda ser
classificados como
funcionais, não funcionais, ou de domínio. A engenharia de requisitos visa compreendere
definir
os requisitos. Um processo de engenharia de requisitos pode envolver o estudo de
viabilidade,
a análise, a especificação e a validação de requisitos.

Item. 105. (CESPE / SERPRO - 2008) O levantamento de requisitos é importante,
porém não é
fundamental, pois recomenda-se avançar o quanto antes para as demais atividades
que
permitam uma visualização do software e reduzam a ansiedade do cliente em ver algo pronto.

Item. 106. CESPE / MPE-RR-2008) Os requisitos de um sistema são descrições dos serviços
fornecidos
pelo sistema e suas restrições operacionais. O processo de descobrir, analisar,
documentar e
verificar esses serviços e restrições é denominado engenharia de requisitos. Requisitos
de um
sistema de software podem ser funcionais, não funcionais ou de domínio.

Item. 107. (CESPE / MPU - 2007) A especificação de requisitos permite, em determinado
momento,
revelar o que o sistema irá realizar no que se refere às funcionalidades, sem
definir, nesse
momento, como as funcionalidades serão implementadas.

Item. 108. (CESPE / MPU - 2007) Na validação de requisitos — parte integrante da
especificação
desses requisitos —, é correto o uso de diagramas da UML, tais como diagrama de
classes, de
casos de uso e de interação.

Item. 109. (CESPE / SERPRO - 2005) O gerenciamento de requisitos inclui, entre outras,
as seguintes
atividades: levantar, analisar, especificar, validar e prototipar requisitos
funcionais e não-
funcionais.

Item. 110. (CESPE / SERPRO - 2005) Uma das principais atividades relacionadas à
engenharia de
software é o levantamento dos requisitos. Nesse contexto, foi introduzida, na década de
80 do
século XX, uma técnica de entrevista conhecida como JAD (Joint Application Development),
que
consistia em uma rápida entrevista e um processo acelerado de coleta de dados em que
todos
os principais usuários e o pessoal da análise de sistemas agrupavam-se em uma única e
intensiva
reunião.

Item. 111. (CESPE / AGE-ES - 2004) A engenharia de requisitos fornece mecanismos que
permitem
entender e analisar a necessidade de o cliente avaliar a exequibilidade, negociar uma
solução
razoável e especificá-la de maneira não-ambígua, validar a especificação e
administrar os
requisitos.


Item. 112. (CESPE / Prefeitura de Boa Vista - 2004) Requisitos adequadamente definidos
constituem
base importante sobre a qual um sistema poderá ser bem desenvolvido. No
processo de
engenharia de requisitos, o estudo de viabilidade utiliza as informações do
processo de
levantamento de requisitos para gerar um relatório que recomenda se é viável ou não
realizar o
processo de desenvolvimento do sistema.

Item. 113. (CESPE / COHAB - 2004) O QFD (Quality Function Deployment) tem uma
abordagem
embasada na criação de uma equipe formada por clientes e desenvolvedores, que trabalham
juntos para identificar o problema, propor elementos da solução,
negociar diferentes
abordagens e especificar um conjunto de requisitos da solução.

Item. 114. (CESPE / COHAB - 2004) As atividades de análise de requisitos resultam na
especificação
das características operacionais do software, na indicação da interface do software com
outros
elementos do sistema e no estabelecimento de restrições que o software deve satisfazer.

Item. 115. (CESPE / COHAB - 2004) À medida que os requisitos são elucidados, o analista
de software
pode criar um conjunto de cenários, ou seja, casos de uso, que identificam uma linha
de uso para
o sistema a ser construído.


GABARITo

Item. 1. ERRADO 41. CORRETO
Item. 81. LETRA E

Item. 2. CORRETO 42. CORRETO
Item. 82. CORRETO

3- ERRADO 43- ERRADO
83- CORRETO

4- CORRETO 44. ERRADO
Item. 84. CORRETO

5- CORRETO 45- ERRADO
Item. 85. ERRADO

Item. 6. CORRETO 46. CORRETO
Item. 86. ERRADO

7- CORRETO 47- ERRADO
Item. 87. ERRADO

Item. 8. ERRADO 48. ERRADO
Item. 88. CORRETO

9- ERRADO 49- CORRETO
Item. 89. CORRETO

Item. 10. CORRETO 50. ERRADO
9°. CORRETO

li. ANULADO 51- ERRADO
Item. 91. ERRADO

Item. 12. CORRETO 52. CORRETO 92.
ERRADO

13- ERRADO 53- ERRADO
93- ERRADO

14- CORRETO 54- ERRADO
94- ERRADO

x5- CORRETO 55- CORRETO 95-
ERRADO

i6. ERRADO 56. ERRADO
Item. 96. ERRADO

17- CORRETO 57- CORRETO 97-
ERRADO

i8. CORRETO 58. CORRETO
Item. 98. CORRETO

Item. 19. ERRADO 59- CORRETO
99- ERRADO

Item. 20. CORRETO 60. CORRETO
Item. 100. ERRADO

Item. 21. CORRETO 61. LETRA E
Item. 101. CORRETO

Item. 22. ERRADO 62. CORRETO
Item. 102. CORRETO

23- ERRADO 63. CORRETO
Item. 103. CORRETO

Item. 24. ERRADO 64. LETRA C
Item. 104. CORRETO

25- CORRETO 65. LETRA D
Item. 105. ERRADO

Item. 26. ERRADO 66. ERRADO
Item. 106. CORRETO

27- CORRETO 67. CORRETO
Item. 107. CORRETO

Item. 28. CORRETO 68. CORRETO
Item. 108. CORRETO

Item. 29. ERRADO 69. CORRETO
Item. 109. CORRETO

Item. 30. LETRA D 70. CORRETO
Item. 110. CORRETO

31- LETRA A 71- CORRETO
Item. 111. CORRETO

Item. 32. CORRETO 72. CORRETO
Item. 112. ERRADO

33- ERRADO 73- ERRADO
Item. 113. ERRADO

34- CORRETO 74- CORRETO 114.
CORRETO

35- CORRETO 75- ERRADO
Item. 115. CORRETO

Item. 36. ERRADO 76. CORRETO

37- ERRADO 77- CORRETO

Item. 38. CORRETO 78. CORRETO

39- ERRADO 79- CORRETO

Item. 40. ERRADO 80. ERRADO


LISTA DE QUESTõES - FCC

í. (FCC / SEFAZ-AP - 2022) Considere as seguintes especificações de requisitos de software:

I. O sistema deve calcular a dívida do contribuinte aplicando a alíquota de 15%
quando o lucro
ultrapassar o teto de contribuição.

II. O tempo de resposta da consulta à dívida ativa da empresa não deve ultrapassar os
13 ms em
situações normais de processamento.

III. O SLA (Acordo de Nível de Serviço) com o contribuinte consulente deve prever
jornada de 24
horas/dia x 7 dias por semana.

IV. A tela de consulta à dívida ativa só pode ser acessada mediante login e senha
corretos
correspondentes àqueles designados ao CNPJ do contribuinte consulente.

Esses requisitos são, correta e respectivamente, dos tipos
a) funcional, técnico, de usuário e não funcional.

b) funcional, não funcional, não funcional e funcional.

c) funcional, técnico, de sistema e não funcional.

d) não funcional, não funcional, técnico e de sistema.

e) não funcional, de usuário, técnico e funcional.

Item. 2. (FCC/ AL-AP - 2020) Considere a lista abaixo, elaborada durante um
levantamento de
requisitos na Assembleia Legislativa do Amapá, para um sistema hipotético de
avaliações
internas:

Item. 1. Registrar avaliação de colaborador por parlamentar: O sistema deve permitir ao
parlamentar,
em uma única tela, a avaliação de todos os seus colaboradores.

Item. 2. Considerar Aspectos Legais: O sistema deve seguir orientações elencadas na
Resolução
099/XXXX do Conselho Legislativo do Estado.

Item. 3. Registrar autoavaliação de parlamentar: O sistema deve permitir ao
parlamentar sua
autoavaliação em relação às disposições legais sob as quais atuou no período.

Item. 4. Atentar à Segurança: O sistema deve fornecer mecanismos de segurança e autenticação
alinhados com os adotados pelo processo XPTO.

Item. 5. Impedir acesso direto ao processo XPTO: O sistema deverá mostrar ao usuário que
existem
formulários de avaliação a serem respondidos e dará a opção de respondê-los depois.


Adotando RFU para requisitos funcionais e RNF para não-funcionais, a classificação
correta e
respectiva da lista 1 a 5 acima é:

a) RFU, RFU, RFU, RNF e RNF.

b) RFU, RNF, RFU, RNF e RNF.

c) RFU, RNF, RFU, RNF e RFU.

d) RNF, RNF, RFU, RNF e RFU.

e) RNF, RFU, RFU, RNF e RNF.

Item. 3. (FCC / TRT-19 - 2019) A Engenharia de Requisitos utiliza algumas técnicas que
apoiam as
atividades de levantamento de requisitos, sendo a entrevista uma das mais
utilizadas. Uma
entrevista pode ser estruturada de formas diferentes, como na estrutura em:

a) diamante, que envolve sessões de workshop com os usuários os quais assumem papéis
de
documentadores, escrevendo os requisitos em flipcharts.

b) brainstorming, em que inicia-se com perguntas mais genéricas sobre o sistema e
finaliza-se
com perguntas mais específicas, sendo geralmente utilizada com usuários que desconhecem o
assunto.

c) funil, na qual procura-se manter o usuário interessado no assunto e para isto
utilizam-se
perguntas variadas sobre o sistema, sorteadas com um dado.

d) diamante, na qual os usuários escrevem os requisitos em papel, todos ao mesmo
tempo, em
uma tempestade de ideias, para estimular requisitos criativos.

e) pirâmide, em que inicia-se com perguntas mais específicas sobre o sistema e
finaliza-se com
perguntas mais genéricas, sendo geralmente utilizada com usuários mais relutantes.

Item. 4. (FCC / AFAP - 2019) Um Analista de Informática levantou os requisitos para
desenvolver um
sistema de gestão. Dentre os requisitos levantados,

I. o sistema deve apresentar a tela de login e senha antes de cada transação e validar o acesso
com base nas políticas de segurança organizacional.

II. o sistema deve estar disponível para a diretoria em tempo integral, ou seja, 24 x 7.

III. o tempo de resposta de uma consulta da alta administração não pode
exceder a 5
milissegundos.

IV. cada Diretor que usa o sistema deve ser identificado apenas por sua matrícula de
cinco dígitos
seguidos do código de segurança.


V. o sistema deverá gravar um log de autenticação a cada transação completada, contendo a
identificação do usuário, data e equipamento utilizado.

VI. os backups do sistema deverão ser feitos diariamente a fim de evitar a eventual perda de
dados sem capacidade de recuperação.

Contêm um requisito funcional e um requisito não funcional, respectivamente, APENAS os itens
a) II e I.

b) Vel.

c) IVeVI.

d) lie III.

e) VI e V.

Item. 5. (FCC / TRF4 - 2019) Suponha que um Analista de TI, participando da etapa de
análise de
requisitos de um sistema de emissão de certidão negativa para o TRF4, tenha elencado
os
requisitos apresentados abaixo:

Item. 1. Utilizar interface responsiva para que possa ser executado em dispositivos móveis e na web.

Item. 2. Validar o tipo de certidão solicitado.

Item. 3. Emitir certidão negativa após verificação de situação do requerente.

Item. 4. Solicitar o CPF do requerente.

Item. 5. Responder ao clique único do usuário em qualquer botão da interface.

Item. 6. Validar o CPF do requerente.

Item. 7. Restaurar os dados automaticamente após falhas não programadas.

Item. 8. Solicitar o nome do requerente.

Item. 9. Oferecer dois tipos de certidão: para fins gerais e para fins eleitorais.

Item. 10. Emitir aviso de impossibilidade de emissão da certidão.

Sobre os requisitos, é correto afirmar que:

a) todos são funcionais.

b) todos são não funcionais.

c) 1, 5 e 7 são não funcionais.

d) apenas 3, 4, 8, 9 e 10 são funcionais.

e) apenas 2, 6 e 7 são não funcionais.

Item. 6. (FCC / SAMASA Campinas - 2019) O diagrama faz referência à QFD -


a) Quality Function Deployment, uma técnica da gestão de qualidade
que traduz as
necessidades do cliente para requisitos de software, buscando maximizar a sua satisfação.

b) Questionário de Funcionalidades para Desenvolvimento, uma técnica para
priorização de
requisitos que facilita a criação de casos de uso.

c) Questionnaire For Diagram, uma lista de perguntas que ajudam a entender
melhor o
problema e permitem que o cliente expresse os requisitos essenciais para a criação de
diagramas
de caso de uso.

d) Quality Function Development, uma técnica para priorização de requisitos,
especializada
para a criação de casos de uso.

e) Questionário de Funcionalidades para Desenvolvimento, uma técnica da gestão de
qualidade
que traduz as necessidades do cliente para as funcionalidades a serem
incorporadas no
software.

Item. 7. (FCC / SEFAZ-BA - 2019) Um profissional da área administrativa de certa
instituição recebeu
um Analista de Sistemas que estava fazendo o levantamento de requisitos para a
construção de
um novo software. Ao informar ao Analista um requisito não funcional para seu
departamento,
o profissional corretamente disse que:

a) a resposta a uma consulta de dados deveria durar no máximo dois segundos para não atrasar
seu trabalho.


b) o sistema deveria permitir a alteração de dados incluídos de forma equivocada.

c) o acesso ao sistema deveria ser por meio de uma senha composta por letras e
números e não
apenas por números.

d) o sistema deveria permitir a exclusão de registros de pessoas que deixaram de ser
clientes da
instituição.

e) o sistema, após consultar os dados de um cliente, deveria permitir a impressão dos dados.

Item. 8. (FCC / SEFAZ-BA - 2019) Um Auditor Fiscal da área de Tecnologia da
Informação está
participando do processo de levantamento de requisitos para o desenvolvimento de um novo
software. Os requisitos a seguirforam elencados:

I. Um usuário deve ser capaz de pesquisar a lista de contribuintes devedores.

II. O sistema deve gerar a lista de contribuintes com atendimento agendado naquele dia.

III. O sistema deve se adequar às leis que garantem o sigilo das informações.

IV. Cada usuário do sistema deverá ser identificado por um número de 8 dígitos.

V. O Sistema deve ter suporte para os sistemas operacionais Linux e Windows.

VI. A alteração dos dados de um contribuinte só poderá ser concretizada após confirmação.

VII. Toda consulta deve retornar os valores solicitados em até 20 segundos.

VIII. A gravação dos dados só deverá ser efetuada após o preenchimento de todos os
campos de
preenchimento obrigatório.

IX. Os dados devem ser armazenados em servidores em cluster para garantir a
disponibilidade.

São requisitos funcionais os que constam APENAS em:

a) I, II, III, IV, V, VI e VII.

b) II, IV, VII e VIII.

c) I, II, IV, VI e VIII.

d) IV, VI, VIII e IX.

e) II, IV, V, VI e VIII.

Item. 9. (FCC / SEMEF-AM - 2019) Considerando que a Fazenda Municipal emprega o
gerenciamento
de requisitos, ganha importância o cuidado com os chamados requisitos voláteis, dentre os
quais fazem parte os requisitos que surgem à medida que o cliente vai
aprimorando sua
compreensão do sistema, denominados requisitos:

a) mutantes.

b) de compatibilidade
c) emergentes
d) adaptativos
e) secundários
io.(FCC / SEMEF-AM - 2019) Ao fazer uso da engenharia de requisitos em
projetos, deve-se
analisar o processo de elicitação e análise de requisitos, o qual pode ser dividido
nas seguintes
atividades:

I. Documentação de Requisitos.

II. Classificação e Organização de Requisitos.

III. Obtenção de Requisitos.

IV. Priorização e Negociação de Requisitos.

A ordem sequencial correta para a execução dessas atividades é:

a) 1,111, IV e II.

b) II, IV, III el.

c) III, II, IV el.

d) IV, I, lie III.

e) III, I, lie IV.

Item. 11. (FCC / SEMEF-AM - 2019) O processo de validação de requisitos de software deve
ser utilizado
em um projeto da Fazenda Municipal, sendo que seus técnicos de TI, devem, nesse
processo de
validação, efetuar revisões de requisitos, atentando que a propriedade:

a) facilidade de compreensão analisa se o requisito pode ser excluído sem prejuízo ao sistema.

b) adaptabilidade verifica se o requisito pode ser alterado sem afetar, de forma
significativa, os
demais requisitos.

c) rastreabilidade verifica se o requisito pode ser testado, de forma completa.

d) facilidade de verificação examina se requisito pode ser excluído sem prejuízo ao sistema.

e) facilidade de compreensão analisa se o requisito tem sua origem diretamente estabelecida.

Item. 12. (FCC / Prefeitura de Manaus-AM - 2019) Considerando a análise de requisitos, as
informações
de rastreabilidade desempenham papel de grande importância. Assim, a equipe responsável
da
Fazenda Municipal deve estar ciente de que a rastreabilidade de projeto significa:

a) definir o mapeamento entre os requisitos de projeto e os usuários do sistema.

b) listar os compiladores utilizados no desenvolvimento de cada módulo de software.


c) determinar o mapeamento entre os requisitos de projeto e os locais onde o sistema
será
utilizado.

d) determinar o desempenho de cada um dos requisitos do sistema.

e) possuir o mapeamento entre os requisitos e os módulos de projeto que implementam
os
requisitos.

Item. 13. (FCC / SEFAZ-SC - 2018) A definição de contextos para que os usuários possam agirde maneira
semelhante, entendendo melhor quais informações precisam fornecer durante a
atividade de
elicitação de requisitos, pode ser obtida por meio da aplicação de duas técnicas de
elicitação
denominadas:

a) cenários e protótipos.

b) entrevistas e observação.

c) protótipos e observação.

d) cenários e histórias de usuários.

e) reuniões com facilitadores e histórias de usuários.

14.(FCC / SEFAZ-SC - 2018) Durante o processo de validação, diferentes tipos
de verificação
podem ser efetuados com os requisitos registrados nos documentos de requisitos. O tipo
de
verificações de consistência é realizado para:

a) identificar, por meio de análise mais aprofundada, outras funções necessárias,
adicionais ou
diferentes, além daquelas que um usuário pensava que fossem as necessárias para o
sistema
executar determinadas funções.

b) evitar que requisitos, no documento, entrem em conflito uns com outros, ou seja,
não deve
haver restrições contraditórias ou descrições diferentes para mesma função do sistema.

c) garantir que o documento de requisitos contenha os requisitos que definem todas as
funções
e as restrições pretendidas pelos usuários do sistema.

d) assegurar, usando o conhecimento das tecnologias existentes, que os requisitos
verificados
possam ser realmente implementados, considerando o orçamento e o cronograma
para o
desenvolvimento do sistema.

e) reduzir o potencial de conflito entre o cliente e o contratante por meio de
um conjunto de
testes que demonstre que o sistema entregue atende a cada requisito especificado.

Item. 15. (FCC / SABESP - 2018) Um Analista necessita levantar os requisitos de um sistema
junto aos
usuários. São técnicas de levantamento:

a) Cenários e Peer Review.

b) Product Owner e Brainstorming.

c) Overview e Use Cases.


d) Joint Application Design (ou Development) - JAD e Etnografia.

e) Prototipação e Sprint.

Item. 16. (FCC / FUB - 2018) O documento de requisitos deve ser elaborado a partir da
análise de
viabilidade do software, seguida de análise, especificação e validação de requisitos.

Item. 17. (FCC / BNB - 2018) A revisão técnica é um procedimento utilizado para validar os
requisitos de
um projeto, com o objetivo de identificar eventuais inconsistências e verificar se os
artefatos
estão de acordo com o padrão esperado.

Item. 18. (FCC / DPE-AM - 2018) Considere, por hipótese, que uma equipe de Analistas de
Sistemas da
Defensoria elencou a lista de requisitos para um novo sistema:

- O sistema não deverá revelar aos usuários nenhuma informação pessoal sobre os
cidadãos,
além do número do processo, em respeito à legislação de privacidade.

- Em razão das restrições referentes aos direitos autorais, alguns documentos
devem ser
excluídos imediatamente ao serem fornecidos pelos cidadãos em seus processos.

- O sistema deve implementar interfaces utilizando as normas de usabilidade vigentes
para o
serviço público.

A lista apresenta exemplos de requisitos:

a) funcionais do tipo proteção e do tipo regulação.

b) funcionais de usabilidade.

c) não-funcionais de proteção.

d) funcionais internos de legislação.

e) não-funcionais externos do tipo legal e do tipo regulador.

Item. 19. (FCC / BNB - 2018) No levantamento de informações, os requisitos dos
solicitantes são
classificados como normais e conceituais. Os requisitos normais refletem os
objetivos e as
metas do produto, ao passo que os conceituais estão implícitos no produto ou
extrapolam as
expectativas do cliente.

Item. 20. (FCC / BNB - 2018) O protótipo operacional serve para aprimorar o entendimento de
como o
sistema deve funcionar, por meio da elucidação dos requisitos do usuário e da
compreensão de
suas necessidades.

21.(FCC/ MPE-MA-2013) O escopo de um projeto é determinado pelo levantamento de
requisitos
funcionais e não funcionais. Dentre os requisitos não funcionais se enquadram
os requisitos
organizacionais, que podem ser divididos em:

a) reguladores e éticos.


b) ambientais, operacionais e de desenvolvimento.

c) contábeis e de segurança.

d) de desempenho e de espaço.

e) de eficiência, de confiança e de proteção.

Item. 22. (FCC / DPE-SP - 2013) Em uma das etapas da Engenharia de Requisitos há a
preocupação em
se observar a especificação produzida, visando verificar que os requisitos
tenham sido
declarados, por exemplo, sem ambiguidades.

O texto refere-se à etapa de:

a) gestão dos requisitos.

b) elicitação dos requisitos.

c) negociação dos requisitos.

d) levantamento dos requisitos.

e) validação dos requisitos.

Item. 23. (FCC / TST- 2012) Na Engenharia de Requisitos, o gerente de requisitos:

a) acompanha e monitora ações durante a verificação do software, sendo este o processo
que
garante o atendimento aos requisitos informados pelo usuário final.

b) possui autonomia para realizar alterações no projeto para garantir que o software
seja bem
construído e atenda às necessidades da equipe de desenvolvimento.

c) mantém atualizados os requisitos junto ao usuário final e a equipe de
desenvolvimento, a fim
de obter sucesso no processo de homologação do software, atendendo as
necessidades e
expectativas.

d) classifica os requisitos em diferentes tipos, sendo os do tipo funcional
relacionados com o
custo e confiabilidade do software e os do tipo não-funcional relacionados com os casos de uso.

e) obtém o comprometimento dos integrantes da equipe de desenvolvimento de software para
o cumprimento do processo de software.

24.(FCC /TCE-AP-2012) Em relação a requisitos de sistemas, considere:

I. O modo como um sistema deve reagir a certas entradas e o comportamento em que o
sistema
deve ter em certas situações e, em alguns casos, especificar o que o sistema não deve
fazer, são
chamados de requisitos não-funcionais.

II. As restrições aos serviços ou funções de um sistema, como, por exemplo, processos
de
desenvolvimento ou utilização de padrões, são requisitos de funcionamento do
sistema ou
requisitos funcionais.


III. Requisitos que vem do domínio da aplicação do sistema e refletem
características ou
restrições para aquele domínio são chamados de requisitos de domínio e podem ser
requisitos
funcionais e/ou não-funcionais.

Está correto o que se afirma em:

a) III, apenas.

b) I, lie III.

c) I e II, apenas.

d) II e III, apenas.

e) I, apenas.

Item. 25. (FCC / MPE-PE - 2012) Os requisitos não funcionais não estão diretamente ligados
aos serviços
específicos oferecidos pelo sistema a seus usuários. Eles podem estar
relacionados às
propriedades emergentes do sistema, como confiabilidade, tempo de resposta e ocupação de
área, entre outros. Dentre os tipos de requisitos não funcionais, é possível destacar
os requisitos
de produto, organizacionais e externos. Dentre os requisitos de produto,
podemos citar os
requisitos:

a) de eficiência e de confiança.

b) contábeis e de desempenho.

c) legais e de usabilidade.

d) reguladores e de proteção.

e) legais e contábeis.

Item. 26. (FCC / TRE-CE - 2012) Considere:

I. Para cada cliente deve ser aplicado um identificador único.

II. O tempo de resposta entre a requisição e a informação não pode exceder a 2 ms.

III. Clientes têm filiais que devem "carregar", na base de dados, o
identificador do cliente
principal.

IV. O sistema não deve ferir as leis de proteção ambiental.

São requisitos não funcionais os que constam em
a) I e II, apenas.

b) II e III, apenas.

c) II e IV, apenas.

d) I, III e IV, apenas.

e) I, II, III e IV.


T]. (FCC / TST - 2012) Na Engenharia de Requisitos, o gerente de requisitos:

a) acompanha e monitora ações durante a verificação do software, sendo este o processo
que
garante o atendimento aos requisitos informados pelo usuário final.

b) possui autonomia para realizar alterações no projeto para garantir que o software
seja bem
construído e atenda às necessidades da equipe de desenvolvimento.

c) mantém atualizados os requisitos junto ao usuário final e a equipe de
desenvolvimento, a fim
de obter sucesso no processo de homologação do software, atendendo as
necessidades e
expectativas.

d) classifica os requisitos em diferentes tipos, sendo os do tipo funcional
relacionados com o
custo e confiabilidade do software e os do tipo não-funcional relacionados com os casos de uso.

e) obtém o comprometimento dos integrantes da equipe de desenvolvimento de software para
o cumprimento do processo de software.

28.(FCC / TJ-PE - 2012) Na engenharia de requisitos trata-se de uma técnica de
elicitação que
ocorre em ambiente mais informal em que toda a idéia deve ser levada em consideração
para a
solução de um problema, sendo proibida a crítica a qualquer sugestão dada, e
encorajada,
inclusive, a criação de ideias que pareçam estranhas ou exóticas:

a) Prototipação.

b) Entrevista.

c) Questionário.

d) Brainstorming.

e) Análise de protocolos.

Item. 29. (FCC / INFRAERO-2011- Letra D) No contexto de levantamento de requisitos,
funcionalidade
é um dos aspectos que deve ser levado em conta na abordagem dos requisitos funcionais.

Item. 30. (FCC / INFRAERO - 2011) A engenharia de requisitos ajuda os engenheiros de
software a
compreender melhor o problema que eles vão trabalhar para resolver. Ela inclui um
conjunto de
tarefas que levam a um entendimento de qual será o impacto do software sobre o
negócio, do
que o cliente quer e de como os usuários finais vão interagir com o software. A
função de
negociação no processo de engenharia de requisitos:

a) especifica, revisa e valida o problema de modo a garantir que seu
entendimento e o
entendimento do cliente sobre o problema coincidam.

b) refina e modifica os requisitos. É uma ação de modelagem de análise composta de
várias
tarefas de modelagem e refinamento.


c) define quais são as prioridades, o que é essencial, o que é necessário. Clientes,
usuários e
outros interessados são solicitados a ordenar os requisitos e depois discutir
os conflitos de
prioridade.

d) ajuda o cliente a definir o que é necessário.

e) define o escopo e a natureza do problema a ser resolvido.

Item. 31. (FCC / TRTi - 2011) A técnica utilizada na compreensão de requisitos sociais e
organizacionais
por observação das rotinas dos envolvidos é a:

a) prototipação.

b) por pontos de vista.

c) por cenário.

d) entrevista.

e) etnografia.

Item. 32. (FCC / INFRAERO - 2011) Os produtos de trabalho resultantes da engenharia de
requisitos são
avaliados quanto à qualidade durante a etapa de validação de requisitos. Analise os
itens a seguir
referentes a essa etapa:

I. Um dos principais mecanismos de validação de requisitos é a avaliação técnica formal.

II. O modelo de análise pode garantir que os requisitos foram consistentemente declarados.

III. É frequentemente útil examinar cada requisito em face de um conjunto de questões
do tipo
checklist.

IV. A equipe de revisão que avalia os requisitos inclui apenas pessoas com
conhecimento técnico
na área de TI, como engenheiros de softwares, desenvolvedores etc.

Está correto o que consta em:

a) I, II, III e IV.

b) II e IV, apenas.

c) I, II e IV, apenas.

d) II, III e IV, apenas.

e) I, II e III, apenas.

Item. 33. (FCC / TRT19 - 2011) A avaliação do impacto de mudança de um requisito, muitas
vezes, faz
com que seja necessário retornar à sua fonte. Na validação dos requisitos, a equipe
deve estar
atenta, portanto, à:


a) rastreabilidade.

b) adaptabilidade.

c) qualidade.

d) facilidade de compreensão.

e) facilidade de verificação.

34- (FCC / TRT23 - 2011) Tabelas de rastreamento para relacionar os requisitos
identificados a um
ou mais aspectos do sistema ou do seu ambiente devem ser desenvolvidas, segundo
Pressman,
na engenharia de requisitos por meio da função de:

a) gestão.

b) especificação.

c) elaboração.

d) negociação.

e) validação.

35- (FCC / BAHIAGÁS - 2010) É uma restrição sobre os serviços ou as funções
oferecidos pelo
sistema. Pode ser uma restrição de timing, sobre o processo de
desenvolvimento, sobre o
desempenho ou sobre a confiabilidade do sistema, entre outras. Trata-se de:

a) requisito não funcional.

b) requisto funcional.

c) especificação de risco.

d) iteração de processo.

e) etnografia.

36.(FCC / DPE-SP- 2010) Sobre análise de requisitos da engenharia de software, considere:

I. Os requisitos de usuário podem descrever tanto requisitos funcionais quanto
requisitos não-
funcionais.

II. Os requisitos de sistema podem descrever apenas requisitos não funcionais.

III. Os requisitos não-funcionais podem ser divididos em requisitos de produto,
organizacionais
e externos.

Está correto o que se afirma em:

a) III, apenas.

b) I e II, apenas.

c) I e III, apenas.

d) II e III, apenas.

e) I, lie III.


37- (FCC / DPE-SP - 2010) No contexto da Engenharia de Requisitos, considere:

I. O sistema deve fornecer uma entrada de dados que possibilite a inclusão de
atributos de
permissão de acesso às dependências da corporação por técnicos, supervisores e chefes.

II. Algumas permissões de acesso deverão ter tratamento especial para a entrada de
atributos.
Para este tipo de permissão, atributos excedentes a uma faixa predeterminada só poderão
ser
incluídos por chefes de seção.

Em relação às assertivas acima, é correto afirmar:

a) O item I trata de um requisito funcional e a ele está associado o
requisito não funcional,
contido no item II.

b) O item I trata de um requisito não funcional e a ele está associado o
requisito funcional,
contido no item II.

c) Ambos referem-se a requisitos funcionais.

d) A assertiva contida no item II é uma condição restritiva do requisito não
funcional do item I.
Por si só, não constitui um requisito, tanto funcional quanto não funcional.

e) A assertiva contida no item II é uma condição restritiva do requisito funcional do
item I. Por si
só, não constitui um requisito, tanto funcional quanto não funcional.

38.(FCC / MPE-RN - 2010) Na engenharia de software, etnografia é:

a) uma fase do processo de software aplicada no modelo em cascata.

b) uma fase do processo de software aplicada no modelo em espiral.

c) uma técnica de observação que pode ser usada para compreender os requisitos
sociais e
organizacionais.

d) uma técnica aplicada na engenharia de requisitos cujo objetivo é definir, a priori,
as classes
que contém elementos gráficos (BLOB).

e) um projeto cujo principal objetivo é criar interfaces gráficas, que facilitam o
acesso do usuário
(GUI).

39.(FCC / MPE-RN - 2010) As políticas de rastreabilidade de requisitos são decididas durante o
estágio de:

a) agregação dos requisitos funcionais, apenas.


b) implementação do sistema, apenas.

c) implementação do sistema
d) eliminação dos requisitos não funcionais.

e) gerenciamento de requisitos.

Item. 40. (FCC / SEFAZ-SP - 2009) Énecessário que 0 software calcule os salários dos diaristas e
mensalistas
e emita relatórios mensais sumariados por tipo de salário. Entretanto, a base de dados
deve estar
protegida e com acesso restrito aos usuários autorizados. De qualquerforma, 0 tempo de
resposta
das consultas não deve superar os quinze segundos, pois inviabilizaria todo o
investimento nesse
sistema. Devo lembrar que os relatórios individuais dos departamentos, nos quais constam
os
salários dos funcionários, devem ser emitidos quinzenalmente em razão dos adiantamentos e
vales
que recebem. É fundamental que 0 software seja operacionalizado usando código
aberto.
Necessito, ainda, forte gerenciamento de risco, prazo e custo, porque a entrega do produto final não
pode ultrapassar 0 prazo de oito meses a contar da data de início do projeto. No
texto, são
requisitos funcionais:

a) Calcule os salários dos diaristas e mensalistas e os relatórios individuais dos departamentos,
nos quais constam os salários dos funcionários, devem ser emitidos quinzenalmente.

b) Necessito, ainda, forte gerenciamento de risco, prazo e custo e a base de dados deve estar
protegida e com acesso restrito aos usuários autorizados.

c) É fundamental que o software seja operacionalizado usando código aberto e emita relatórios
mensais sumariados portipo de salário.

d) Emita relatórios mensais sumariados por tipo de salário e necessito, ainda, forte
gerenciamento de risco, prazo e custo.

e) A base de dados deve estar protegida e com acesso restrito aos usuários autorizados e
entrega do produto final não pode ultrapassar o prazo de oito meses.

Item. 41. (FCC / TRT3 - 2009) Com relação aos requisitos de software, considere:

I. funcionais são somente requisitos de usuário.

II. funcionais e não-funcionais podem ser requisitos de usuário.

III. funcionais e não-funcionais podem ser requisitos de sistema.

Está correto o que se afirma APENAS em
a) l.

b) II.

c) III.

d) I e III.

e) lie III.


Item. 42. (FCC /TRT7-2009) No processo de engenharia de requisitos, é uma técnica de observação que
pode ser usada para compreender os requisitos sociais e organizacionais. Trata-se de:

a) Workshop.

b) Brainstorming.

c) Scrum.

d) Análise de ponto de vista.

e) Etnografia.

Item. 43. (FCC / TRT3 - 2009) São técnicas e abordagens utilizadas na obtenção dos requisitos:

a) estresse, cenários e workshop.

b) workshop, etnografia e estresse.

c) etnografia, questionários e validação.

d) pontos de vista, cenários e entrevista.

e) pontos de vista, casos de uso e validação.

Item. 44. (FCC / PGE-RJ - 2009) No âmbito da Engenharia de Requisitos, uma revisão técnica formal é:

a) um teste de desempenho.

b) uma técnica de elicitação.

c) um instrumento de rastreamento.

d) o resultado do escopo.

e) um mecanismo de validação.


GABARITo

Item. 1. LETRA B i6. CORRETO
31- LETRA E

Item. 2. LETRA C 17- CORRETO
Item. 32. LETRA E

3- LETRA E i8. LETRA E
33- LETRA A

4- LETRA C 19- ERRADO
34- LETRA A

5- LETRA C 20. CORRETO
35- LETRA A

Item. 6. LETRA A 21. LETRA B
Item. 36. LETRA C

7- LETRA A 22. LETRA E
37- LETRA A

Item. 8. LETRA C 23- LETRA C
Item. 38. LETRAC

9- LETRA C 24. LETRA A
39- LETRA E

Item. 10. LETRAC 25- LETRA A
Item. 40. LETRA A

íi. LETRA B 26. LETRA C
Item. 41. LETRA E

Item. 12. LETRA E 27- LETRA C
Item. 42. LETRA E

13- LETRA A 28. LETRA D
43- LETRA D

14- LETRA B 29. CORRETO
44- LETRA E

15- LETRA D 30. LETRA C


LISTA DE QUESTõES - FCV

í. (FGV / TCE-TO - 2022) A Equipe de Desenvolvimento de Soluções (EDS) recebeu a
solicitação
de que um dos campos utilizados para entrada de dados da aplicação Web em construção
apresente sugestões de palavras dinamicamente, conforme o usuário for digitando
novos
caracteres.

A EDS recebeu a solicitação de um requisito de:

a) confiança;

b) eficiência;

c) desempenho;

d) usabilidade;

e) desenvolvimento.

Item. 2. (FGV / TCE-TO - 2022) Carlos é uma parte interessada em uma aplicação Web e
solicitou à
equipe de desenvolvimento uma funcionalidade capaz de emitir relatórios com
cabeçalhos
padronizados. Assim, os cabeçalhos devem ter cor de fundo, paleta de cores
e tipografia,
seguindo o padrão adotado em outros documentos emitidos pelo departamento
responsável
pela aplicação.

A solicitação de Carlos refere-se a um requisito:

a) funcional regulador;

b) não funcional organizacional;

c) funcional do processo operacional;

d) não funcional de usabilidade;

e) funcional de desenvolvimento.

Item. 3. (FGV / TCE-TO - 2022) A Equipe de Desenvolvimento de Soluções (EDS) recebeu a
solicitação
de que um dos campos utilizados para entrada de dados da aplicação Web em construção
apresente sugestões de palavras dinamicamente, conforme o usuário for digitando
novos
caracteres. A EDS recebeu a solicitação de um requisito de:

a) confiança;

b) eficiência;

c) desempenho;

d) usabilidade;

e) desenvolvimento.

Item. 4. (FGV / TCE-TO - 2022) Carlos é uma parte interessada em uma aplicação Web e
solicitou à
equipe de desenvolvimento uma funcionalidade capaz de emitir relatórios com
cabeçalhos
padronizados. Assim, os cabeçalhos devem ter cor de fundo, paleta de cores e tipografia,


seguindo o padrão adotado em outros documentos emitidos pelo departamento
responsável
pela aplicação:

A solicitação de Carlos refere-se a um requisito:

a) funcional regulador;

b) não funcional organizacional;

c) funcional do processo operacional;

d) não funcional de usabiIidade;

e) funcional de desenvolvimento.

Item. 5. (FGV/TCE-TO-2022) As credenciais de acesso dos usuários de um aplicativo são
armazenadas
em um banco de dados e são utilizadas unicamente para acesso às funcionalidades do
aplicativo.
A equipe de desenvolvimento definiu como requisito não funcional que o sistema deve
evitar
que as senhas sejam obtidas por um invasor mesmo que o aplicativo ou banco de dados
esteja
comprometido.

Para implementar o requisito não funcional, um modo de proteger as senhas dos usuários é:

a) ocultar o algoritmo utilizado para proteção das senhas;

b) armazenar as senhas cifradas por meio de um algoritmo de chaves assimétricas;

c) utilizar um algoritmo hash com salt antes de persistir as senhas no banco de dados;

d) codificar um algoritmo próprio para cifrar as senhas com base em uma chave
randômica
segura;

e) usar uma chave randômica gerada pelo aplicativo para cifrar as senhas por meio de
um
algoritmo de chave simétrica.

Item. 6. (FGV / TCE-TO - 2022) A Equipe de Tecnologia (ETi) de um tribunal de contas
está levantando
as necessidades para um novo sistema junto às partes interessadas. Uma das
partes
interessadas solicitou que o novo sistema seja fácil de usar, como requisito não funcional.

Para que o requisito não funcional "fácil de usar" seja objetivamente
testado, a ETi deve
considerar a métrica:

a) eficiência;

b) disponibilidade;

c) tempo de treinamento;

d) taxa de ocorrência de falhas;

e) tempo de atualização de tela.

Item. 7. (FGV / ALERJ - 2017) O Analista de Sistemas Pedro está realizando um
levantamento de
requisitos por meio da prototipação. Sua intenção com esse protótipo é proporcionar uma
visão
geral do sistema com todas as suas funcionalidades, sem entrar em detalhes específicos de cada
funcionalidade, deforma que a interface como um todo possa ser criticada pelos
usuários. Nesse
caso, o tipo de protótipo mais adequado é o (a):

a) vertical;

b) tridimensional;

c) prototipação rápida;

d) textual;

e) horizontal.

Item. 8. (FGV / BADESC - 2010) Analise o fragmento a seguir:

"A base de dados deve ser protegida para acesso apenas de usuários autorizados".
O fragmento acima apresenta um exemplo do seguinte requisito:

a) funcional.

b) de usuário.

c) de sistema.

d) de domínio.

e) não-funcional.

Item. 9. (FGV / FIOCRUZ - 2010) Sobre os processos de engenharia de requisitos, na elicitação e na
análise ocorre total interação com os stakeholders no sistema, sendo o principal objetivo:

a) a obtenção dos requisitos.

b) a homologação do sistema.

c) a elaboração do manual do usuário.

d) a conversão de especificações em requisitos.

e) a execução do estudo de viabilidade do sistema.

Item. 10. (FGV/ MEC-2009) Requisitos não-funcionais estão diretamente relacionados com a satisfação
dos usuários. Assinale a alternativa que não indique um requisito não-funcional:

a) O sistema de arquivos deve ser protegido, para acesso, apenas, de usuários autorizados.

b) O software deve ser implementado usando os conceitos de orientação a objetos.

c) O tempo de desenvolvimento do software não deve ultrapassar seis meses.

d) O software poderá ser executado em plataforma windows e linux.

e) O software deve emitir relatórios de vendas a cada quinze dias.

Item. 11. (FGV / MEC - 2009) As declarações de serviços que o sistema deve fornecer, de
como ele deve
reagir a entradas específicas ou se comportar em determinadas situações, são chamadas de
requisitos:

a) não-funcionais.


b) de domínio.

c) de sistema.

d) funcionais.

e) de usuário.

Item. 12. (FGV / MEC-2009) Existem técnicas que são usadas na fase de levantamento de
requisitos para
coletar conhecimento dos usuários sobre os requisitos. Assinale a alternativa que
indique apenas
técnicas utilizadas na fase de levantamento de requisitos.

a) JAD, WFMS, WBS, cenários e brainstorming.

b) JAD, cenários, WFMS, questionários e intercepting.

c) cenários, entrevistas, protótipos, workshop, brainstorming.

d) leitura de documentos, protótipos, workshop, WBS e workflow.

e) brainstorming, protótipos, workflow, leitura de documentos e intercepting.

Item. 13. FGV / Senado Federal - 2008) Entre as atividades listadas a seguir, uma não faz
parte da
Engenharia de Requisitos. Assinale-a.

a) estudo de viabilidade.

b) análise de risco.

c) levantamento de necessidades do cliente.

d) verificação.

e) gerenciamento.


GABARITo

Item. 1. LETRA D 6. LETRA C
Item. 11. LETRA D

Item. 2. LETRA B 7- LETRA E
Item. 12. LETRAC

3- LETRA D 8. LETRA E
13- LETRA B

4- LETRA B 9- LETRA A

5- LETRA C 10. LETRA E


LISTA DE QUESTõES - DIvERSAS BANCAS

í. (IBFC / IBGE - 2021) A etapa de levantamento de requisitos é composta por
diversas técnicas
que visam obter do cliente as informações necessárias para desenvolver o projeto do
sistema de
informação. Sobre essas técnicas, analise as afirmativas abaixo, dê valores Verdadeiro
(V) ou
Falso (F).

() Entrevistas não estruturadas: Informal ou sem agenda pré-definida.

() Brainstorming: Reunião com várias pessoas onde todos discutem um tema central.
() Prototipagem: Desenvolvimento de um modelo que simulará o sistema real.

a) F-F-F

b) F - F - V

c) V - F - V

d) V-V-F

e) V-V-V

Item. 2. (IDIB / CRF - MS - 2021) Em qual etapa do processo de desenvolvimento de
requisitos de
software mais comumente costuma acontecer a identificação de gaps nos
requisitos ou a
identificação de requisitos desnecessários, conforme eles se relacionam com o escopo definido?

a) Elicitação de requisitos.

b) Análise de requisitos.

c) Especificação de requisitos.

d) Validação de requisitos.

Item. 3. (IDIB / CRF - MS - 2021) "Uma descrição de uma propriedade ou característica
que um sistema
deve exibir ou uma restrição que ele deve respeitar". Tal definição se adequa a qual
tipo de
requisito de informação em um processo de software?

a) Requisito Funcional.

b) Requisito Não-Funcional.

c) Atributo de Qualidade.

d) Requisito do Usuário.

Item. 4. (VUNESP / EBSERH - 2020) Considerando as técnicas utilizadas para a avaliação de
requisitos,
é correto afirmar que, na:

a) facilidade de verificação, deve-se verificar se não há requisitos conflitantes entre si.

b) verificação de consistência, deve-se verificar se os requisitos podem ser
implementados,
considerando a tecnologia existente.


c) verificação de realismo, deve-se verificar se todas as funções e restrições
planejadas estão
contempladas.

d) verificação de validade, deve-se verificar se não há requisitos conflitantes entre si.

e) verificação de completeza, deve-se verificar se todas as funções e restrições
planejadas estão
contempladas.

Item. 5. (VUNESP/ EBSERH -2020) Na engenharia de requisitos, um fator importante são os
requisitos
não funcionais, que se classificam em organizacionais, de produto e externos. Os requisitos
a) de produto têm origem em políticas e procedimentos da organização do cliente.

b) de produto compreendem fatores oriundos de fatores externos ao sistema e seu
processo de
desenvolvimento.

c) externos especificam o comportamento do produto, tais como o desempenho e a memória
requerida.

d) organizacionais têm origem em políticas e procedimentos da organização do cliente.

e) organizacionais especificam o comportamento do produto, tais como o
desempenho e a
memória requerida.

Item. 6. (COPESE - UFPI/ ALEPI- 2020) Um técnico de TI da ALEPI que gerencia uma equipe
de
desenvolvimento de software na Assembleia, eventualmente necessita fazer
levantamento de
requisitos da aplicação que está sendo desenvolvida. Sobre
os Requisitos
de Software, considere as seguintes afirmativas:

I. Requisitos funcionais são aqueles que definem parte da funcionalidade do sistema e
podem
ser categorizados em três tipos: requisitos de produtos, requisitos organizacionais e
requisitos
externos.

II. Requisitos não-funcionais dizem respeito a restrições, aspectos de desempenho,
interfaces
com o usuário, confiabilidade, segurança, portabilidade e padrões.

III. Requisitos organizacionais estão relacionados às metas da empresa, suas
políticas
estratégicas adotadas, assim como assuntos relacionados aos empregados da empresa
com
seus respectivos objetivos.

IV. Requisitos de produto estão relacionados as restrições impostas por fatores
externos ao
sistema tais como restrições de interoperabilidade, éticas e legais.

Marque a opção que corresponde somente às afirmativas verdadeiras.

a) Apenas I, III e IV.

b) Apenas I, II e III.

c) Apenas I e III.

d) Apenas II e III.

e) Apenas II, III e IV.


7- (FAFIPA / Prefeitura de Arapongas - PR - 2020) A Engenharia de Requisitos é um
termo
cunhado para descrever as atividades relacionadas à investigação e definição de escopo
de um
sistema de software, ou seja, trata-se do processo de descobrir, analisar, documentar e
verificar
as funções e restrições do sistema. Para auxiliar o levantamento de
requisitos, existe um
conjunto de técnicas de levantamento de dados que podem ser aplicadas em
conjunto ou
isoladamente, a depender das características do projeto. Assinale a alternativa que
apresenta
somente técnicas para descoberta de requisitos:

a) Sprint; Caso de Uso; Etnografia.

b) Entrevista; Caso de Uso; Etnografia.

c) Sprint; Refatoração; Etnografia.

d) JAD; Refatoração; Etnografia.

e) Entrevista; JAD; Refatoração.

Item. 8. (IBFC / EBSERH - 2020) Requisitos são as bases para todo projeto, definindo o
que as partes
interessadas de um novo sistema necessitam e também o que o sistema deve
fazer para
satisfazer as suas necessidades. Antes do processo, propriamente dito, da
Engenharia de
Requisitos deve-se ter:

a) entrevistas e questionários com os usuários
b) a documentação dos requisitos
c) a revisão dos requisitos funcionais e não-funcionais
d) os estudos de viabilidade técnica/financeira
e) a revisão dos requisitos pelos usuários

Item. 9. (INSTITUTO AOCP / Prefeitura de Betim - MG - 2020) A engenharia de requisitos
estabelece
uma ponte entre o projeto e a construção do software. Assinale a alternativa que
representa a
etapa na qual as metas de negócio são estabelecidas.

a) Levantamento.

b) Concepção.

c) Negociação.

d) Revisão.

e) Gestão.

Item. 10. (FAURGS /TJ-RS-2018) Requisitos não funcionais-como o nome sugere-são
requisitos que
não estão diretamente relacionados com os serviços específicos oferecidos pelo sistema a
seus
usuários. Podem ser provenientes das características requeridas para o
software, da
organização que desenvolve o software ou de fontes externas. Os requisitos não
funcionais que
especificam ou restringem o comportamento do software - como por
exemplo o seu
desempenho, seus requisitos de proteção, seus requisitos de usabilidade e a taxa
aceitável de
falhas-são denominados requisitos:


a) organizacionais.

b) de produto.

c) externos.

d) éticos.

e) ambientais.

n.(FAURGS / TJ-RS -2018) Técnicas de descoberta de requisitos (às vezes chamada de
elicitação
de requisitos) é o processo de reunir informações sobre o sistema requerido e os
sistemas
existentes e separar dessas informações os requisitos do usuário e de sistema; o uso
destas
técnicas faz parte da maioria dos processos de engenharia de
requisitos.é o nome
dado a uma técnica em que o stakeholder responde a um conjunto predefinido de
perguntas
sobre o sistema usado no momento e sobre o sistema que será desenvolvido; os
requisitos
surgem a partir das respostas a essas perguntas.

A alternativa que contém o termo que completa corretamente a lacuna do texto acima é:

a) Entrevista fechada.

b) Entrevista aberta.

c) Etnografia.

d) Cenários.

e) Casos de uso.

Item. 12. (FAURGS/TJ-RS-2oi8) Qual alternativa abaixo apresenta um requisito funcional de software?

a) A base de dados deve ser protegida para acesso apenas a usuários autorizados.

b) O tempo de resposta do sistema não deve ultrapassar 30 segundos..

c) O software deve ser operacionalizado no Sistema Operacional Windows.

d) O software deve emitir relatórios de vendas.

e) O tempo de desenvolvimento não deve ultrapassar três meses.

Item. 13. (FAURGS / TJ-RS - 2018) Considerando que, durante o processo de validação de
requisitos,
estes são submetidos a diferentes tipos de verificação, assinale a alternativa cuja
verificação
indica que no documento de requisitos não existem descrições diferentes para
uma mesma
função do sistema.

a) Verificação de consistência.

b) Verificação de completude.

c) Verificações de realismo.

d) Verificações de validade.

e) Prototipação.

Item. 14. (UFG / SANEAGO - 2017) Com relação à qualidade de software, é um exemplo de
requisito de
software não funcional:


a) calcular o valor do desconto conforme o perfil do cliente.

b) processar até 100 pedidos por segundo.

c) produzir o software em até dois anos e ter custo inferior a R$100.000,00.

d) limitar o cadastro de usuários ao Departamento de Pessoal.

Item. 15. (UFG / SANEAGO - 2017) Alguns usuários estão insatisfeitos com um
software. Uma
investigação revelou que a origem da insatisfação decorre de uma omissão
(requisito não
especificado) na especificação de requisitos de software. Que atividade da
engenharia de
requisitos precisa ser revista para evitar problemas semelhantes?

a) Análise de viabilidade.

b) Validação.

c) Construção.

d) Elaboração do Termo de Abertura.

Item. 16. (UFG / SANEAGO - 2017) São atributos de requisito de software:

a) custo (para implementar) e complexidade ciclomática.

b) prioridade e linguagem de implementação.

c) complexidade ciclomática e risco.

d) risco e identificador.

i7-(UFG / SANEAGO - 2017) Uma Engenharia de Requisitos (ER) bem estruturada
garante
qualidade, confiabilidade e integridade ao produto de software a ser desenvolvido. O
conjunto
de atributos que evidencia o esforço necessário para fazer modificações
especificadas no
software é uma característica de:

a) portabilidade.

b) confiabilidade.

c) manutenibilidade.

d) eficiência.

Item. 18. (IBFC / EBSERH - 2017) Quanto aos vários tipos de requisitos assinale, das
alternativas abaixo,
a única que NÃO identifica corretamente um clássico requisito não-funcional:

a) requisito de implementação da arquitetura do sistema
b) requisitos de funcionalidades do sistema
c) requisito de interoperabilidade da arquitetura do sistema
d) requisitos de confiabilidade da arquitetura do sistema
e) requisitos de portabilidade da arquitetura do sistema

19.(IBFC / EBSERH - 2017) A Análise de Requisitos é a primeira fase de
desenvolvimento de
software dividido em Requisitos funcionais e Requisitos não-funcionais. Os
Requisitos não-
funcionais possuem vários tipos diferentes de classificação tais como:


(í) Requisitos de confiabilidade.

(2) Requisitos de produtos.

(3) Requisitos éticos.

(4) Requisitos de portabilidade.

a) da relação apresentada existem somente o 2, 3 e 4

b) da relação apresentada existem somente o 1, 3 e 4

c) da relação apresentada existem somente o 1, 2 e 4

d) da relação apresentada existem somente o 1, 2 e 3

e) da relação apresentada existem todos.

2O.(CESGRANRIO / IBGE -2016) Um dos objetivos da disciplina de requisitos é:

a) criar um esboço inicial da arquitetura do sistema a ser desenvolvido.

b) adaptar e configurar o processo de desenvolvimento de modo a atender às
especificidades
do sistema a ser desenvolvido.

c) fornecer uma base para estimar o custo e o tempo de desenvolvimento de um sistema.

d) assegurar que os clientes, os usuários e os desenvolvedores tenham um
entendimento
comum da organização na qual um sistema será implantado.

e) entender a estrutura e a dinâmica da organização na qual um sistema será implantado.

2i.(IBFC / MGS - 2015) A definição: "descrevem as funcionalidades que se espera que o
sistema
disponibilize, de uma forma completa e consistente. É aquilo que o usuário espera que
o sistema
ofereça, atendendo aos propósitos para qual o sistema será desenvolvido.",
corresponde
tipicamente aos:

a) Requisitos Funcionais.

b) Requisitos Externos.

c) Requisitos não-Funcionais.

d) Requisitos da Aplicação.

Item. 22. CESGRANRIO / IBGE - 2014) Solicitado para fazer o levantamento dos requisitos
para um novo
software a ser desenvolvido, um analista de sistemas identificou a necessidade de
descobrir
todos aqueles que se beneficiariam de forma direta ou indireta do sistema a ser desenvolvido.

Essas pessoas são conhecidas como:

a) clientes
b) partes interessada
c) patrocinadores
d) usuários
e) usuários finais

Item. 23. (ESAF / CVM - 2010) Assinale a opção correta.

a) Gestão de requisitos preocupa-se com a documentação, atualização e
controle de
stakeholders envolvidos na fase de identificação da demanda.

b) Engenharia de requisitos compreende: identificar, analisar, especificar
e definir as
necessidades de negócio que um aplicativo deve prover para solução do problema levantado.

c) Engenharia de requisitos compreende: planejar, especificar e desenvolver as
necessidades de
negócio que um aplicativo deve prover para minimização dos problemas levantados.

d) Engenharia de requisitos compreende: identificar, analisar, programar e testar os
programas
das necessidades de solução de problemas que um negócio deve prover para satisfazer usuários.

e) Gestão de requisitos preocupa-se com a documentação, direcionamento,
controle de
definição e acesso aos requisitos levantados na fase de planejamento de escopo.

Item. 24. (ESAF / MPOG -2010) As áreas de esforços da Análise de Requisitos são:

a) reconhecimento dos objetivos, avaliação e controle, modelagem, estruturação e revisão.

b) reconhecimento do problema, avaliação e síntese, modelagem, especificação e revisão.

c) reengenharia, planejamento, avaliação e controle, modelagem e conclusão.

d) reconhecimento do problema, análise e síntese, reengenharia, especificação e
análise de
resultados.

e) reconhecimento do problema, modelagem, especificação de entidades,
estruturação e
revisão.

Item. 25. (ESAF / AFRFB - 2005) Durante a análise de requisitos, são especificados
a função e o
desempenho do software, bem como a sua interface com outros elementos do sistema. Nessa
etapa, também, são estabelecidas as restrições de projeto, a que o software deve atender.

Item. 26. (ESAF / AFRFB - 2005 - Letra E) Durante a especificação dos requisitos, são
estabelecidos os
critérios que permitirão ao desenvolvedor e ao cliente avaliar a qualidade, assim que
o software
for construído.


GABARITo

Item. 1. LETRA E 10. LETRA B
Item. 19. LETRA E

Item. 2. LETRA B li. LETRA A
Item. 20. LETRAC

3- LETRA B 12. LETRA D
Item. 21. LETRA A

4- LETRA E 13- LETRA A
Item. 22. LETRA B

5- LETRA D 14- LETRA B
23- LETRA B

Item. 6. LETRA D 15- LETRA B
Item. 24. LETRA B

7- LETRA B i6. LETRA D
25- CORRETO

Item. 8. LETRA D 17- LETRA C
Item. 26. CORRETO

9- LETRA A i8. LETRA B


Conceitos Básicos

DÉBITo TÉCNICo

INCIDÊNCIA EM PROVA: BAIXA

Imagine que você seja um cara bastante procrastinador (muito comum entre concurseiros)
e tenha
uma tarefa para fazer, mas decide deixá-la para depois porque está ocupado com outras
coisas.
Esse adiamento pode gerar uma dívida para você, que terá que lidar com a tarefa mais
tarde e
possivelmente em um momento menos conveniente. De maneira semelhante, o débito técnico
no desenvolvimento de software é como uma dívida do desenvolvedor.

O desenvolvedor a assume ao deixar de realizar tarefas importantes, como refatorar o
código,
realizar testes adequados ou atualizar bibliotecas. Essas omissões podem levar a
problemas
futuros, como bugs, mau desempenho ou problemas de segurança. Assim como uma
dívida
financeira, o débito técnico precisa ser pago mais tarde, muitas vezes com juros, na
forma de
correções de emergência, retrabalho ou atrasos no cronograma.

É importante que os desenvolvedores e equipes de software gerenciem e controlem o
débito
técnico para garantir que o software seja robusto, de alta qualidade e fácil de
manter. Isso
envolve identificar as áreas de dívida técnica, priorizar o pagamento de
débitos e investir em
práticas de desenvolvimento saudáveis para minimizara criação de novas dívidas. No meu
trabalho,
nós mantemos um backlog dos principais débitos técnicos para ir "pagando" sempre que possível.

Enfim, o débito técnico é basicamente o custo a longo prazo de desenvolver um
software com
baixa qualidade. Quando você escreve um código de má qualidade ou deixa de seguir
boas práticas
de programação, você acumula um débito técnico. Mais cedo ou mais tarde, você
precisará corrigir
esses problemas para manter o software funcionando corretamente ou
adicionar novas
funcionalidades.

As consequências do débito técnico são muitas e variadas. Quando você acumula débito
técnico,
o software se torna mais difícil de entender, de modificar e de manter. Isso pode
levar a
problemas de desempenho, segurança e escalabilidade, além de dificultar a
adição de novas
funcionalidades no futuro. Logo, é importante destacar a relação intrínseca entre débito
técnico no
desenvolvimento de software e refatoração de software.

Além disso, acumular débito técnico pode ser muito caro a longo prazo. A correção de problemas
de qualidade geralmente é demorada e cara, o que pode afetar negativamente o orçamento
e o
cronograma do projeto. Por isso, é importante gerenciar o débito técnico de
forma eficaz.
Identificar, priorizar e corrigir o débito técnico acumulado pode ajudar a melhorar a
qualidade do
software, a reduzir custos e a garantir que o software esteja preparado para as demandas futuras.

Identificar o débito técnico pode ser um pouco complicado, mas existem algumas formas
de se
fazer isso. Geralmente, o débito técnico pode ser identificado a partir de sintomas comuns, como
atrasos no projeto, problemas de qualidade, bugs frequentes, entre outros. Além disso,
uma das
melhores maneiras de identificar o débito técnico é realizar revisões regulares do
código, seja
por meio de revisões de código (code review) ou testes de software.

Durante essas revisões, é possível encontrar problemas comuns de qualidade de software,
tais
como código duplicado, falta de documentação, uso inadequado de variáveis e funções,
entre
outros. Quanto às categorias de débito técnico, existem várias maneiras de categorizar
o débito
técnico, mas uma das mais comuns é a divisão entre débito técnico
"intencional" e "não
intencional".

O débito técnico intencional ocorre quando você toma uma decisão consciente
de priorizar a
entrega rápida do software em detrimento da qualidade. Por outro lado, o
débito técnico não
intencional ocorre quando você não percebe que está acumulando débito técnico,
geralmente por
falta de conhecimento ou tempo limitado. Também é importante medir o débito técnico
para ter
uma ideia clara da quantidade de trabalho necessário para corrigi-lo.

Existem várias ferramentas que podem ajudar a medir o débito técnico, como o SonarQube
e o
CodeClimate, que analisam o código-fonte em busca de problemas comuns e geram
relatórios
sobre o débito técnico acumulado. A métrica mais comum para medir o débito técnico é
o tempo
necessário para corrigir os problemas encontrados, geralmente medido em dias ou semanas.
Gerenciar o débito técnico também é uma parte essencial do desenvolvimento de software.

Para priorizar o tratamento do débito técnico, você deve primeiro avaliar os riscos
associados a cada
problema identificado. Problemas mais críticos, como problemas de segurança ou problemas
que afetam o desempenho do software, devem ser tratados com mais urgência
do que
problemas menos críticos. Outra forma de priorizar o tratamento do débito técnico é
avaliar o
impacto que cada problema tem no projeto como um todo.

Problemas que afetam mais áreas do software ou que afetam a capacidade de adicionar
novas
funcionalidades devem ter uma prioridade maior do que problemas que afetam apenas uma
parte
específica do software. Para planejar e executar a correção do débito técnico, é
importante ter um
processo claro e bem definido. Isso envolve identificar os problemas, avaliar a
prioridade de cada
problema e planejar as etapas necessárias para corrigi-los.

Uma das melhores práticas para gerenciar o débito técnico é estabelecer um processo contínuo
de revisão e correção. Isso significa que você deve realizar revisões regulares do
código, identificar
os problemas e corrigi-los o mais rápido possível. Além disso, é importante envolver
toda a equipe
no processo de gerenciamento do débito técnico, para garantir que todos
estejam cientes dos
problemas e trabalhem juntos para resolvê-los.

Outra prática importante é manter um registro de todos os problemas de
débito técnico
identificados e corrigidos. Isso pode ajudar a identificar padrões e tendências ao
longo do tempo e
a avaliara eficácia do processo de gerenciamento do débito técnico. Porfim, é importante terem
mente que o gerenciamento do débito técnico é um processo contínuo e nunca termina: sempre
haverá novos problemas e desafios a serem enfrentados.

No entanto, com um processo claro e uma equipe comprometida, é possível gerenciar o
débito
técnico de forma eficaz e garantir a qualidade e a escalabilidade do software ao
longo do tempo.
Prevenir a acumulação de débito técnico é a melhor forma de garantir que seu software
seja
eficiente, escalável e fácil de manter a longo prazo. Aqui estão algumas estratégias
para evitar o
acúmulo de débito técnico:

ESTRATÉGIAS | DESCRIÇÃO


ESTABELEÇA PADRÕES DE
CÓDIGO E BOAS PRÁTICAS DE

DESENVOLVIMENTO

FAÇA REVISÕES DE CÓDIGO

REGULARES

INVISTA EM TESTES DE

QUALIDADE

Ter padrões de código claros e boas práticas de desenvolvimento estabelecidos desde
o início é uma ótima maneira de garantir que o código seja claro, fácil de entender e
fácil de manter.

Revisões de código regulares ajudam a identificar problemas de qualidade do código
antes que eles se tornem problemas maiores. Além disso, elas promovem a
colaboração da equipe e ajudam a garantir que todos estejam trabalhando dentro dos
mesmos padrões e práticas.

Testes automatizados e manuais são uma ótima maneira de garantir que o software
esteja funcionando corretamente e atendendo às necessidades dos usuários.


PLANEJE PARA
ESCALABILIDADE

USE FERRAMENTAS DE

AUTOMAÇÃO

Ao desenvolver um software, é importante pensar em como ele pode ser escalável no
futuro. Isso significa pensar em como o software pode lidar com grandes quantidades
de dados e usuários, bem como garantir que ele possa ser facilmente mantido e
atualizado.

Ferramentas de automação podem ajudar a reduzir o tempo necessário para realizar
tarefas repetitivas e propensas a erros. Isso pode incluir ferramentas de integração
contínua, ferramentas de análise de código e ferramentas de teste automatizado.


MANTENHA UM REGISTRO DE

DÍVIDA TÉCNICA

Manter um registro de dívida técnica pode ajudar a garantir que os problemas sejam
identificados e tratados o mais rápido possível.

(Câmara de Goiânia/GO - 2018) Leia o texto a seguir extraído da Internet.

Se 0 débito técnico não é pago, ele pode acumular, tomando mais difícil implementar
mudanças posteriores.

No contexto desta informação, o débito técnico:

a) pode ser eliminado durante a construção de software sem dependência do projeto
(design) do software.

b) pode ser eliminado por alteração no projeto (design) sem repercussão na
implementação.


c) é uma questão de projeto (design) com repercussão na funcionalidade do software.

e) tem impacto na evolução do software.

Comentários: no contexto desta informação, o débito técnico tem impacto na evolução do
software. Quando o débito técnico
não é tratado, ele se acumula e pode tornar mais difícil a implementação de mudanças
posteriores. Isso pode afetar
negativamente a evolução do software, levando a atrasos no lançamento, custos adicionais e,
possivelmente, um produto final
de menor qualidade. Logo, é importante gerenciar o débito técnico de maneira eficaz para
garantir que o software possa evoluir
de maneira consistente e sem problemas (Letra D).

(TJ/PE - 2012) No contexto de programação ágil XP, um débito técnico é descrito como
o:

a) número de pontos funcionais não entregues no último período.

b) custo homem/hora da equipe técnica para um determinado projeto.

c) método de modificação do código fonte, com alteração do seu comportamento,
porém sem alteração de seu significado.

d) dispêndio relacionado ao desenvolvimento, teste ou entrega da parte
funcional do
sistema.

e) total de desenvolvimento feito de maneira rápida e simples sem, às vezes, levar em
consideração testes e arquitetura do sistema.

Comentários: 0 débito técnico em XP é entendido como uma dívida técnica que é
adquirida quando 0 desenvolvimento é
realizado de forma rápida e simplificada, muitas vezes sem levar em consideração os
testes e a arquitetura adequados do
sistema. Essa dívida técnica pode se acumular e, se não for tratada, pode levar a
problemas futuros no projeto. Logo, é
importante gerenciar 0 débito técnico para garantir que ele não se acumule a ponto de
afetar negativamente o projeto (Letra
E).


