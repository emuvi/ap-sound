Capítulo. Resiliência de aplicações - Técnica de Fallback.


A técnica de fallback é uma estratégia utilizada para aumentar a resiliência de aplicações, fornecendo uma alternativa quando um componente principal não está disponível. É uma forma de lidar com falhas e garantir que a aplicação continue operando mesmo em situações de degradação ou ausência de recursos essenciais.

Quando um componente principal não está disponível, seja por falha, manutenção ou qualquer outro motivo, a técnica de fallback permite que a aplicação utilize uma funcionalidade alternativa ou um recurso substituto para continuar sua operação. Isso ajuda a minimizar o impacto nas operações e a garantir que os usuários possam continuar utilizando a aplicação de forma parcial ou reduzida.

Algumas formas comuns de implementar a técnica de fallback incluem:

Item. 1. Funcionalidade alternativa: É possível ter uma funcionalidade ou fluxo alternativo que seja ativado quando o componente principal não está disponível. Por exemplo, em um sistema de pagamento online, se o provedor de pagamentos estiver fora do ar, a aplicação pode alternar para um provedor de pagamento de reserva.

Item. 2. Cache de dados: Quando um recurso externo não está disponível, a aplicação pode utilizar um cache de dados previamente armazenados como uma alternativa. Por exemplo, se um serviço de terceiros para obtenção de informações não está funcionando, a aplicação pode utilizar uma versão em cache dessas informações até que o serviço seja restaurado.

Item. 3. Mensagens de erro adequadas: Em vez de exibir mensagens de erro genéricas quando ocorre uma falha, é possível fornecer mensagens específicas e orientações para os usuários, indicando que uma funcionalidade alternativa está disponível ou que a aplicação está em um modo degradado temporário.

A escolha da estratégia de fallback adequada depende do contexto e dos requisitos da aplicação. É importante avaliar os recursos críticos, identificar os pontos de falha potenciais e definir a abordagem de fallback apropriada para cada um deles. Além disso, é fundamental testar e validar a funcionalidade de fallback para garantir que ela esteja funcionando corretamente e cumprindo o objetivo de manter a aplicação em operação mesmo em situações adversas.
