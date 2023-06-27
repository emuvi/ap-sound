Capítulo. Modelagem de banco de dados - lógico.

A modelagem de banco de dados lógico é uma etapa do processo de modelagem em que se cria uma representação abstrata e independente de tecnologia do banco de dados. Nessa fase, o foco está na estrutura lógica dos dados, como as entidades, os relacionamentos e as regras de negócio. O objetivo é criar um modelo que seja compreensível tanto para os desenvolvedores quanto para os usuários finais. Aqui estão os passos envolvidos na modelagem de banco de dados lógico:

Item. 1. Identificar entidades: O primeiro passo é identificar as entidades principais do sistema, que representam os objetos do mundo real que serão armazenados no banco de dados. Por exemplo, em um sistema de vendas, as entidades podem incluir Clientes, Produtos e Pedidos.

Item. 2. Definir atributos: Para cada entidade, é necessário identificar os atributos que descrevem as características dos objetos. Por exemplo, para a entidade Cliente, os atributos podem incluir nome, endereço e número de telefone. Para a entidade Produto, os atributos podem ser nome, preço e quantidade em estoque.

Item. 3. Estabelecer relacionamentos: Após identificar as entidades e seus atributos, é necessário definir os relacionamentos entre elas. Os relacionamentos podem ser do tipo um-para-um, um-para-muitos ou muitos-para-muitos, dependendo da natureza dos dados. Por exemplo, um cliente pode fazer vários pedidos (um-para-muitos) e um pedido pode ter vários produtos (muitos-para-muitos).

Item. 4. Definir cardinalidade e participação: Ao estabelecer os relacionamentos, é importante especificar a cardinalidade e a participação de cada entidade no relacionamento. A cardinalidade define o número mínimo e máximo de ocorrências de uma entidade em um relacionamento. A participação define se a presença de uma entidade no relacionamento é obrigatória (obrigatória) ou opcional (opcional).

Item. 5. Normalização: A normalização é um processo de refinamento do modelo lógico para eliminar redundâncias e anomalias nos dados. Ela envolve a decomposição das entidades em estruturas mais granulares e a definição de chaves primárias para garantir a integridade dos dados. A normalização segue regras específicas, como a forma normal de Boyce-Codd (FNBC) e a terceira forma normal (3NF).

Item. 6. Diagrama de Entidade-Relacionamento (DER): O resultado da modelagem lógica é frequentemente representado por um diagrama de Entidade-Relacionamento (DER). O DER ilustra as entidades, os atributos e os relacionamentos, bem como as cardinalidades e participações. É uma ferramenta visual que facilita a compreensão e a comunicação do modelo com os stakeholders.

A modelagem de banco de dados lógico é uma etapa importante para entender e documentar a estrutura dos dados em um sistema. Ela serve como base para a implementação física do banco de dados em um sistema de gerenciamento de banco de dados específico. Além disso, um modelo lógico bem projetado ajuda a garantir a consistência, a integridade e a eficiência das operações no banco de dados.
