Capítulo. Resiliência de aplicações - Técnica de Site Ativo X Ativo.


A técnica de Site Ativo X Ativo (Active-Active) é uma abordagem utilizada na resiliência de aplicações para garantir alta disponibilidade e escalabilidade. Nessa técnica, múltiplos sites ou data centers são configurados e operam simultaneamente, atendendo às solicitações dos usuários de forma distribuída.

Na arquitetura de Site Ativo X Ativo, cada site é capaz de processar as solicitações dos usuários de forma independente e completa. Isso significa que todos os sites têm uma cópia completa da aplicação e dos dados associados. Cada site é considerado ativo e pode receber e processar as solicitações dos usuários em tempo real.

A distribuição das solicitações entre os sites é geralmente realizada por meio de um balanceador de carga global ou outro mecanismo de roteamento, que direciona as solicitações dos usuários para o site mais próximo ou com menor carga, com base em fatores como latência de rede, capacidade do servidor, localização geográfica, entre outros.

As principais vantagens da abordagem Site Ativo X Ativo são:

Item. 1. Alta disponibilidade: Com vários sites ativos simultaneamente, se um site ou data center falhar, os outros sites continuarão a atender as solicitações dos usuários. Isso garante a disponibilidade contínua da aplicação, mesmo em caso de falhas pontuais.

Item. 2. Escalabilidade: A abordagem Active-Active permite que a aplicação seja dimensionada horizontalmente, adicionando mais sites ou data centers conforme necessário para lidar com aumentos no tráfego ou demanda dos usuários. Isso proporciona uma melhor capacidade de escalabilidade e distribuição de carga.

Item. 3. Redução de latência: Ao ter sites distribuídos em diferentes localidades geográficas, os usuários são direcionados para o site mais próximo, o que ajuda a reduzir a latência de rede e melhorar a experiência do usuário.

Item. 4. Balanceamento de carga: A distribuição das solicitações entre os sites é feita por um balanceador de carga global, garantindo uma distribuição equilibrada e eficiente do tráfego.

Item. 5. Recuperação rápida de falhas: Em caso de falha em um site, o balanceador de carga global redireciona automaticamente as solicitações para os sites restantes, permitindo uma rápida recuperação e continuidade do serviço.

No entanto, a implementação do Site Ativo X Ativo requer cuidadosa consideração e planejamento, especialmente em relação à sincronização de dados entre os sites e à consistência dos dados em tempo real. A replicação de dados entre os sites e a garantia de que todas as alterações sejam refletidas em todos os sites são desafios importantes a serem enfrentados.

Além disso, o Site Ativo X Ativo também pode envolver custos adicionais de infraestrutura, pois cada site deve estar totalmente equipado e dimensionado para atender às demandas dos usuários.

Portanto, ao adotar a abordagem Site Ativo X Ativo, é essencial realizar testes abrangentes, implementar mecanismos adequados de sincronização e replicação de dados, e monitorar constantemente o desempenho e a disponibilidade dos sites para garantir uma resiliência eficaz da aplicação.
