Capítulo. Arquitetura de Software - Padrões GRASP.


Os Padrões GRASP (General Responsibility Assignment Software Patterns) são um conjunto de diretrizes para atribuir responsabilidades a classes e objetos em um sistema de software. Eles fornecem princípios orientadores para ajudar os arquitetos de software a tomar decisões de design relacionadas à alocação de responsabilidades. Aqui estão alguns exemplos dos padrões GRASP mais comuns:

Item. 1. Padrão Creator: O padrão Creator aborda a questão de qual classe deve ser responsável pela criação de objetos. Ele sugere que a classe que tem a maior quantidade de informações necessárias para criar um objeto seja responsável por sua criação. Isso ajuda a evitar acoplamento excessivo e garante uma responsabilidade clara pela criação de objetos.

Item. 2. Padrão Controller: O padrão Controller sugere que uma classe (ou objeto) seja designada como o controlador responsável por coordenar e controlar o fluxo de operações do sistema. O controlador é responsável por receber as solicitações externas, tomar decisões e invocar os objetos adequados para realizar as ações necessárias.

Item. 3. Padrão Information Expert: O padrão Information Expert sugere que a responsabilidade seja atribuída à classe ou objeto que possui as informações necessárias para executar uma determinada operação. Isso significa que a classe com o conhecimento mais relevante sobre um determinado domínio ou contexto é a mais apropriada para realizar as ações correspondentes.

Item. 4. Padrão Low Coupling: O padrão Low Coupling visa reduzir o acoplamento entre classes e objetos. Ele sugere que a responsabilidade seja atribuída de forma a minimizar as dependências entre as classes, promovendo um sistema mais flexível e fácil de manter. O objetivo é garantir que as classes dependam o mínimo possível umas das outras.

Item. 5. Padrão High Cohesion: O padrão High Cohesion sugere que as responsabilidades sejam atribuídas de forma a maximizar a coesão em uma classe. Isso significa que uma classe deve ter uma única responsabilidade bem definida e não deve ter responsabilidades conflitantes. Uma alta coesão torna as classes mais fáceis de entender, testar e manter.

Item. 6. Padrão Polymorphism: O padrão Polymorphism incentiva o uso de polimorfismo para lidar com diferentes comportamentos em um sistema. Ele sugere que a responsabilidade seja atribuída a uma classe base ou interface, permitindo que várias implementações diferentes possam ser usadas de forma transparente. Isso promove a flexibilidade e extensibilidade do sistema.

Esses são alguns exemplos dos padrões GRASP, que fornecem orientações para atribuir responsabilidades em um sistema de software. Os padrões GRASP ajudam a melhorar a organização, a manutenibilidade e a escalabilidade do sistema, promovendo uma estrutura clara e uma distribuição adequada de responsabilidades.


O GRASP, acrônimo de General Responsability Assignment Software Patterns (ou Principies), consiste em um conjunto de práticas que descrevem os princípios fundamentais de atribuição de responsabilidade a objetos, expressas na forma de padrões. Ele ajuda a compreender melhor a utilização da orientação a objetos em projetos complexos.
A qualidade de um projeto orientado a objetos está fortemente relacionada à distribuição de responsabilidades, que podem ser divididas em Responsabilidade de Conhecimento (Knowing) e Responsabilidade de Realização (Doing). A primeira refere-se à distribuição das características do sistema entre as classes e a segunda à distribuição do comportamento do sistema entre as classes.
As Responsabilidades do Tipo Realização são realizadas por um único método ou uma coleção de métodos trabalhando em conjunto. Já as Responsabilidades do Tipo Conhecimento são inferidas a partir do modelo conceituai, i.e., são atributos e relacionamentos. Lembram-se da UML? Pois é, os Diagramas de Interação são bastante utilizados para representar responsabilidades.
Galera, para ser bem sincero com vocês, eu considero Padrões GRASP mais como uma filosofia de projeto do que como um conjunto de padrão de projeto. Eles descrevem princípios fundamentais de desenho orientado a objetos e definição de responsabilidades, expressos em padrões. Vocês sabem o que significa o verbo To Grasp? Significa tomar, agarrar, apreender, captar, aferrar, pegar de súbito.
Esse nome foi escolhido com o intuito de sugerir a importância de agarrar ou captar esses princípios para desenhar projetos de software orientados a objetos da melhor forma possível. Os Padrões de Projeto GOF exploram soluções de projeto mais específicas, já os Padrões de Projeto GRASP refletem práticas mais pontuais da aplicação de técnicas orientadas a objetos.
O Padrão GRASP é composto de cinco Padrões Básicos e quatro Padrões Avançados. Os Padrões Básicos são: Information Expert, Creator, High Cohesion, Low Coupling e Controller. Já os Padrões Avançados são: Polymorphism, Pure Fabrication, Indirection e Protected Variations. Assim como os Padrões de Projeto (GOF), para resolver a grande maioria das questões, basta conhecer a descrição básica.

Expert:

Também conhecido como Information Expert, esse padrão é utilizado para determinar para quem delegar as responsabilidades. Essas responsabilidades incluem métodos, campos calculados, etc. Deve-se atribuir a responsabilidade ao especialista da informação, isto é., a classe que possui a informação necessária para satisfazer essa responsabilidade.

Creator:

A criação de objetos é uma das atividades mais comuns em sistemas orientados a objetos. Esse padrão é responsável por criar objetos de classes, sendo uma propriedade fundamental do relacionamento entre objetos em determinadas classes, i.e., possui a responsabilidade unívoca pela criação de uma nova instância de uma classe.

High Cohesion:

Esse padrão busca manter objetos apropriadamente focados, gerenciáveis e compreensíveis. Geralmente é utilizado para suportar o baixo acoplamento, enfatizando que as responsabilidades de um dado elemento são fortemente relacionadas e altamente focadas. Eu sempre decorei assim: "Coesão é a divisão de responsabilidades".

Low Coupling:

Esse padrão é responsável por ditar como atribuir responsabilidades para apoiar baixa dependência entre classes, como suportar mudanças em uma classe que tenham baixo impacto em outras classes, e maior potencial de reúso. O acoplamento está sempre associado à coesão. Eu sempre decorei assim: "Acoplamento é a dependência entre as partes".

Controller:

Esse padrão tem o objetivo de atribuir a responsabilidade de lidar com eventos de sistema a uma classe que não implemente elementos gráficos, e represente um sistema completo ou um cenário de caso de uso. Um objeto Controller não é uma interface com o usuário, trata-se - na verdade - de um objeto responsável por receber e tratar eventos do sistema.

Polymorphism:

Esse padrão atribui a responsabilidade de definir a variação de comportamentos baseado em tipos aos tipos em que essas variações ocorrem. Isso ocorre por meio de operações polimórficas. Em outras palavras, não se deve utilizar a lógica condicional para decidir qual comportamento será realizado, mas utilizar os próprios tipos. Galera, é o polimorfismo comum à orientação a objetos.

Pure Fabrication:

Esse padrão apresenta uma classe que não representa um conceito real, mas artificial, no domínio de problema, sendo utilizada para atingir baixo acoplamento, alta coesão e o potencial reúso. Em outras palavras, ela atribui um conjunto altamente coesivo de responsabilidade a uma classe artificial que não representa um conceito do domínio do problema.

Indirection:

Esse padrão atribui responsabilidade a um objeto intermediário para mediar as mensagens entre outros componentes ou serviços para que não sejam diretamente acoplados. Ele cria uma camada de indireção entre os dois componentes que não mais dependem um do outro, i.e., ambos dependem da indireção. Um exemplo é o Componente Controller no MVC - ele faz a mediação entre Model e View.

Protected Variations:

Esse padrão identifica pontos de variação ou instabilidades potenciais e atribui responsabilidades para criar uma interface estável em volta desses pontos. Dessa forma, ela protege elementos das variações de outros elementos (objetos, sistemas, subsistemas) ao envolver o foco de instabilidade em uma interface e usando o polimorfismo para criar várias implementações desta interface.

