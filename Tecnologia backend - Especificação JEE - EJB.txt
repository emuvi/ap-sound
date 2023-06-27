Capítulo. Tecnologia backend - Especificação JEE - EJB.


A especificação JEE (Java Enterprise Edition) inclui a tecnologia EJB (Enterprise JavaBeans), que é um componente de negócio usado para desenvolver aplicativos empresariais em Java. Os EJBs são executados no servidor de aplicativos JEE e fornecem serviços como persistência de dados, transações, segurança e gerenciamento de concorrência.

Aqui estão alguns conceitos e recursos chave relacionados aos EJBs:

Item. 1. Componentes EJB: Os EJBs são componentes de negócio que encapsulam a lógica de negócio de um aplicativo. Existem três tipos principais de EJBs:

- Session Beans: São EJBs responsáveis pela lógica de negócio do aplicativo. Eles podem ser de dois tipos: Stateless Session Beans, que não mantêm estado entre as chamadas do cliente, e Stateful Session Beans, que mantêm estado para um cliente específico.

- Entity Beans: São EJBs que representam entidades persistentes no banco de dados. Eles fornecem um meio de mapear objetos Java para tabelas do banco de dados.

- Message-Driven Beans: São EJBs usados para processar mensagens assíncronas em um aplicativo. Eles são acionados pela recepção de mensagens em uma fila JMS (Java Message Service) ou em um tópico JMS.

Item. 2. Container EJB: Os EJBs são executados dentro de um container EJB, que é uma parte do servidor de aplicativos JEE. O container EJB gerencia o ciclo de vida dos EJBs, incluindo a criação, destruição, pooling e transações. Ele também fornece serviços adicionais, como segurança, controle de acesso e gerenciamento de concorrência.

Item. 3. Anotações: Os EJBs são configurados usando anotações Java, que fornecem informações ao container EJB sobre o comportamento do componente. As anotações são usadas para definir transações, segurança, ciclo de vida, mapeamento para banco de dados e outras configurações específicas do EJB.

Item. 4. Transações: Os EJBs suportam transações declarativas, o que significa que as transações podem ser gerenciadas automaticamente pelo container EJB. Você pode definir anotações para especificar os requisitos de transação de um EJB, como requerimento de transação, isolamento e propagação.

Item. 5. Segurança: Os EJBs suportam recursos de segurança, permitindo a configuração de autenticação, autorização e controle de acesso para proteger o acesso aos componentes de negócio. É possível definir regras de segurança nas anotações ou por meio de configurações no arquivo de implantação do aplicativo.

Os EJBs fornecem uma maneira poderosa e escalável de implementar a lógica de negócio em aplicativos empresariais Java. Eles abstraem a complexidade dos serviços de infraestrutura, como persistência de dados, transações e segurança, permitindo que os desenvolvedores se concentrem na lógica de negócio essencial do aplicativo.
