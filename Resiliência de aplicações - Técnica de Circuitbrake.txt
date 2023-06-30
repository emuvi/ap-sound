Capítulo. Resiliência de aplicações - Técnica de Circuitbrake.


A técnica de Circuit Breaker (disjuntor) é uma estratégia utilizada para aumentar a resiliência de aplicações, protegendo-as contra falhas em serviços externos ou componentes dependentes. O objetivo do circuit breaker é evitar falhas em cascata, interrompendo temporariamente as solicitações a um componente que está apresentando falhas excessivas.

O funcionamento básico do circuit breaker é baseado em um mecanismo de estado que monitora o status do componente ou serviço externo. Ele possui três estados principais:

Item. 1. Estado Fechado (Closed): Nesse estado, todas as solicitações são permitidas a passar normalmente para o componente externo. O circuit breaker monitora as respostas dessas solicitações. Se a taxa de falha ultrapassar um limite predefinido, o circuit breaker muda para o estado Aberto (Open).

Item. 2. Estado Aberto (Open): Nesse estado, todas as solicitações são bloqueadas e não são enviadas ao componente externo. Em vez disso, uma resposta de erro é retornada imediatamente para as solicitações. Durante esse período, o circuit breaker pode ativar uma lógica de fallback ou retornar uma resposta alternativa para os usuários. Após um determinado tempo, o circuit breaker permite uma única solicitação de teste para verificar se o componente externo se recuperou.

Item. 3. Estado Meio-Aberto (Half-Open): Se a solicitação de teste no estado Aberto for bem-sucedida, o circuit breaker muda para o estado Meio-Aberto, permitindo que algumas solicitações sejam enviadas ao componente externo para verificar se ele está realmente funcionando corretamente. Se essas solicitações tiverem sucesso, o circuit breaker volta ao estado Fechado e retoma a operação normal. Caso contrário, ele retorna ao estado Aberto e bloqueia as solicitações novamente.

Ao utilizar o circuit breaker, é possível evitar o envio de solicitações para um componente externo que está falhando continuamente, reduzindo a carga e melhorando a resiliência da aplicação como um todo. Além disso, o circuit breaker fornece uma proteção adicional contra falhas em cascata, isolando os efeitos negativos de um componente com problemas.

É importante configurar adequadamente os limites e timeouts do circuit breaker, de acordo com o comportamento esperado do componente externo e as necessidades da aplicação. Além disso, é recomendável implementar mecanismos de monitoramento e registro de eventos para acompanhar a saúde e o desempenho dos componentes externos. Dessa forma, é possível tomar medidas proativas para lidar com falhas e garantir a resiliência da aplicação.
