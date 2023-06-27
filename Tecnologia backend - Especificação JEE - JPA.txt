Capítulo. Tecnologia backend - Especificação JEE - JPA.


A especificação JEE (Java Enterprise Edition) inclui a Java Persistence API (JPA), que é uma API para mapeamento objeto-relacional em aplicativos Java. A JPA facilita o armazenamento e a recuperação de objetos Java em bancos de dados relacionais de forma transparente, simplificando o acesso e a manipulação dos dados.

Aqui estão alguns conceitos e recursos chave relacionados à JPA:

Item. 1. Mapeamento Objeto-Relacional: A JPA permite que você mapeie objetos Java para tabelas em um banco de dados relacional e vice-versa. Isso é feito por meio de anotações ou arquivos de mapeamento XML, que especificam como os objetos estão relacionados às tabelas e aos campos do banco de dados.

Item. 2. Entidades: As entidades são classes Java que representam objetos persistentes, que são armazenados em um banco de dados. Cada entidade está associada a uma tabela no banco de dados e seus atributos correspondem aos campos da tabela.

Item. 3. EntityManager: O EntityManager é uma interface da JPA que fornece métodos para gerenciar entidades, como persistir, atualizar, recuperar e excluir objetos do banco de dados. Ele é responsável por realizar operações de persistência e manipulação de objetos persistentes.

Item. 4. Consultas JPQL: A JPA introduz a linguagem de consulta JPQL (Java Persistence Query Language), que é semelhante à SQL, mas opera em objetos persistentes em vez de tabelas de banco de dados. Com JPQL, você pode realizar consultas complexas e recuperar dados específicos do banco de dados.

Item. 5. Relacionamentos: A JPA permite definir relacionamentos entre entidades, como relacionamentos um-para-um, um-para-muitos e muitos-para-muitos. Isso é feito por meio de anotações ou configurações XML que especificam como as entidades estão relacionadas umas com as outras.

Item. 6. Transações: A JPA inclui suporte a transações, permitindo que você gerencie operações de banco de dados em um contexto transacional. Você pode definir transações usando anotações ou programaticamente usando a API de transações da JPA.

Item. 7. Provedores JPA: A JPA é apenas uma especificação e requer um provedor JPA real para ser executada. Alguns exemplos populares de provedores JPA incluem Hibernate, EclipseLink e OpenJPA.

A JPA simplifica o desenvolvimento de aplicativos que requerem acesso a um banco de dados relacional, permitindo que você trabalhe com objetos Java em vez de lidar diretamente com consultas SQL e operações de banco de dados. Ela abstrai os detalhes de baixo nível do mapeamento objeto-relacional e fornece uma API consistente e padronizada para interagir com o banco de dados.
