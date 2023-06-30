Capítulo. Resiliência de aplicações.


A resiliência de aplicações é a capacidade de uma aplicação de se manter operacional mesmo diante de falhas ou interrupções em sua infraestrutura ou serviços subjacentes. Trata-se de um princípio importante no desenvolvimento de sistemas que visa garantir a disponibilidade, a confiabilidade e o desempenho adequado das aplicações, mesmo em situações adversas.

A resiliência de aplicações envolve a implementação de estratégias e práticas que permitem lidar com falhas e se recuperar delas de forma rápida e eficiente. Alguns dos principais aspectos relacionados à resiliência de aplicações incluem:

Item. 1. Tolerância a falhas: As aplicações resilientes são projetadas para lidar com falhas em componentes ou serviços. Isso pode envolver a implementação de mecanismos de recuperação automática, como a detecção de falhas e a reconfiguração de serviços, a fim de minimizar o impacto em toda a aplicação.

Item. 2. Redundância: A utilização de redundância em diferentes níveis da aplicação é uma prática comum para aumentar a resiliência. Isso pode incluir a replicação de servidores, bancos de dados ou outros componentes críticos, de modo que uma falha em um único componente não cause a indisponibilidade da aplicação como um todo.

Item. 3. Escalabilidade: A capacidade de escalar a aplicação de forma horizontal ou vertical é fundamental para lidar com picos de tráfego, demanda crescente ou falhas em componentes individuais. Ao projetar uma aplicação resiliente, é importante considerar a escalabilidade para que ela possa se adaptar a essas situações.

Item. 4. Recuperação de desastres: Em situações extremas, como desastres naturais ou falhas catastróficas, é importante ter um plano de recuperação de desastres. Isso envolve a criação de cópias de segurança dos dados, a utilização de data centers secundários ou a migração para serviços em nuvem, garantindo a continuidade da aplicação em cenários adversos.

Item. 5. Monitoramento e observabilidade: A capacidade de monitorar e diagnosticar o estado da aplicação é essencial para a resiliência. Isso inclui o uso de ferramentas de monitoramento em tempo real, registros de eventos e métricas, permitindo identificar problemas e agir rapidamente para corrigi-los.

Item. 6. Testes de resiliência: Realizar testes de resiliência é uma prática importante para garantir que a aplicação seja capaz de lidar com diferentes cenários de falha. Isso pode envolver testes de carga, testes de estresse e simulações de falhas, a fim de avaliar o desempenho e a estabilidade da aplicação sob condições adversas.

Em resumo, a resiliência de aplicações é uma abordagem que visa garantir a disponibilidade contínua e o bom desempenho das aplicações, mesmo diante de falhas ou interrupções. Ao adotar práticas e estratégias de resiliência, é possível aumentar a confiabilidade e a capacidade de recuperação das aplicações, oferecendo uma melhor experiência para os usuários finais.


Tópico. Técnicas de Cache, Fallback, Circuitbrake, Disaster Recovery, Contingência, Balanceamento de Carga Global de Servidores (GSLB), Site Ativo X Ativo.


Técnicas de Cache:
A técnica de cache é usada para armazenar temporariamente os dados ou resultados de computações frequentemente acessados, de forma a reduzir o tempo de acesso e melhorar o desempenho. O cache pode ser implementado em vários níveis, como no nível do aplicativo, no nível do banco de dados ou no nível da infraestrutura de rede.

Fallback:
A técnica de fallback é usada para fornecer uma alternativa quando um componente ou serviço principal não está disponível. Quando o componente principal falha, o sistema utiliza uma funcionalidade de fallback para manter a operação contínua ou fornecer um comportamento reduzido, mas funcional, aos usuários.

Circuit Breaker:
O circuit breaker é uma técnica usada para melhorar a resiliência de um sistema. Ele monitora as falhas de um serviço ou componente e interrompe temporariamente as solicitações para esse serviço quando ocorrem falhas excessivas. Isso evita o efeito cascata de falhas e permite que o sistema se recupere antes de retomar as solicitações.

Disaster Recovery (Recuperação de Desastres):
A recuperação de desastres é uma estratégia para lidar com eventos catastróficos que podem causar interrupção significativa nos sistemas e operações de uma organização. Isso envolve a implementação de medidas de prevenção, preparação e resposta para garantir a continuidade dos negócios e a recuperação rápida após um desastre.

Contingência:
A contingência é uma estratégia para lidar com falhas ou interrupções não relacionadas a desastres. Isso envolve a criação de planos e procedimentos para lidar com falhas de sistemas, falhas de energia, falhas de rede, erros humanos e outros eventos que possam afetar as operações normais de uma organização.

Balanceamento de Carga Global de Servidores (GSLB):
O GSLB é uma técnica usada para distribuir o tráfego de rede entre vários servidores localizados em diferentes locais geográficos. Isso ajuda a melhorar o desempenho e a disponibilidade de um serviço, direcionando os usuários para o servidor mais próximo ou mais adequado com base em critérios como latência, capacidade do servidor ou localização geográfica.

Site Ativo X Ativo:
O site ativo x ativo é uma técnica usada para criar uma arquitetura de alta disponibilidade, na qual dois ou mais sites ou data centers estão em operação simultânea e tratam do tráfego de rede. Nessa abordagem, todos os sites estão ativos e compartilham a carga de trabalho, proporcionando redundância e tolerância a falhas. Se um site falhar, o tráfego é automaticamente redirecionado para os sites restantes, garantindo a continuidade do serviço.
