Capítulo. Desenvolvimento de Software - Métodos de Ordenação.


No desenvolvimento de software, os métodos de ordenação são algoritmos que organizam um conjunto de elementos em uma determinada ordem, como crescente ou decrescente. A ordenação é uma operação comum em muitos tipos de aplicativos, desde classificação de dados em bancos de dados até a organização de listas de itens em interfaces de usuário.

Existem diversos métodos de ordenação, cada um com suas características e complexidades. Alguns dos métodos mais conhecidos incluem:

Item. 1. Bubble Sort: É um método simples, porém ineficiente, que compara pares de elementos adjacentes e os troca se estiverem fora de ordem. O processo é repetido até que a lista esteja completamente ordenada. O Bubble Sort possui complexidade de tempo O(n^2), onde n é o número de elementos na lista.

Item. 2. Insertion Sort: Também é um método simples, mas mais eficiente que o Bubble Sort. Ele percorre a lista, inserindo cada elemento em sua posição correta em relação aos elementos já ordenados. O Insertion Sort possui complexidade de tempo O(n^2), mas é mais eficiente que o Bubble Sort em listas parcialmente ordenadas.

Item. 3. Selection Sort: Nesse método, o algoritmo encontra o menor elemento da lista e o coloca na primeira posição. Em seguida, encontra o próximo menor elemento e o coloca na segunda posição, e assim por diante. O Selection Sort possui complexidade de tempo O(n^2) e tem um desempenho similar ao Bubble Sort e ao Insertion Sort.

Item. 4. Merge Sort: É um método de ordenação dividir e conquistar. Ele divide repetidamente a lista em metades menores, ordena cada metade separadamente e, em seguida, combina as metades ordenadas para obter a lista final ordenada. O Merge Sort possui complexidade de tempo O(n log n), o que o torna eficiente em grandes conjuntos de dados.

Item. 5. Quick Sort: Também é um método de ordenação dividir e conquistar. Ele seleciona um elemento chamado de "pivô" e rearranja a lista de forma que todos os elementos menores que o pivô estejam à sua esquerda e todos os elementos maiores estejam à sua direita. Em seguida, o Quick Sort é aplicado recursivamente nas duas partições resultantes. O Quick Sort possui complexidade de tempo O(n log n) em média, mas pode degradar para O(n^2) no pior caso.

Item. 6. Heap Sort: Utiliza uma estrutura de dados chamada heap para organizar os elementos. Primeiro, constrói-se uma heap a partir dos elementos da lista. Em seguida, repete-se a operação de extrair o elemento de maior valor da heap e inseri-lo na posição correta na lista ordenada. O Heap Sort possui complexidade de tempo O(n log n).

Esses são apenas alguns exemplos de métodos de ordenação. Existem outros algoritmos, como o Shell Sort, o Radix Sort, o Counting Sort, entre outros, que podem ser mais adequados dependendo do contexto e dos requisitos do sistema.

A escolha do método de ordenação a ser utilizado depende de diversos fatores, como o tamanho da lista, a distribuição dos elementos, os recursos disponíveis (memória, processamento), entre outros. É importante considerar a eficiência e a estabilidade do algoritmo, bem como as restrições e as necessidades específicas do problema em
questão.


Métodos de Ordenação são algoritmos que têm o objetivo principal de posicionar os elementos de uma estrutura de dados em uma determinada ordem. Para que, professor? Ora, isso possibilita o acesso mais rápido e eficiente aos dados. Existem dezenas de métodos, todavia nessa aula veremos apenas os mais importantes: BubbleSort, QuickSort, InsertionSort, SelectionSort, MergeSort, ShellSort e HeapSort.
Antes de iniciar, vamos falar sobre o conceito de Estabilidade! Um método estável é aquele em que os itens com chaves iguais mantêm-se com a posição inalterada durante o processo de ordenação, i.e., preserva-se a ordem relativa dos itens com chaves duplicadas ou iguais. Métodos Estáveis: Bubble, Insertion e Merge; Métodos Instáveis: Selection, Quick, Heap e Shell. Vejamos um exemplo:
Na imagem acima, foi colocado um sinal de aspas simples e duplas apenas para diferenciá-los, mas trata-se do mesmo número. Um algoritmo estável ordena todo o restante e não perde tempo trocando as posições de elementos que possuam chaves idênticas. Já um algoritmo instável ordena todos os elementos, inclusive aqueles que possuem chaves idênticas (sob algum outro critério).

Índice

Item. 1 BubbleSort (Troca)

Item. 2 InsertionSort (Inserção)

Item. 3 SelectionSort (Seleção)

Item. 4 QuickSort (Troca)

Item. 5 ShellSort (Inserção)

Item. 6 MergeSort (Intercalação)

Item. 7 HeapSort (Seleção)


BubbleSort (Troca)

Esse algoritmo é o primeiro método de ordenação aprendido na faculdade, porque ele é bastante simples e intuitivo. Nesse método, os elementos da lista são movidos para as posições adequadas de forma contínua. Se um elemento está inicialmente em uma posição i e, para que a lista fique ordenada, ele deve ocupar a posição j, então ele terá que passar por todas as posições entre i e j.

Em cada iteração do método, percorremos a lista a partir de seu início comparando cada elemento com seu sucessor, trocando-se de posição se houver necessidade. É possível mostrar que, se a lista tiver n elementos, após no máximo (n-1) iterações, a lista estará em ordem (crescente ou decrescente).

Complexidade do Algoritmo:

Melhor caso: O ( n )

Caso médio: O ( n ao quadrado )

Pior caso: O ( n ao quadrado )


InsertionSort (Inserção)

Esse algoritmo, também conhecido como Inserção Direta, é bastante simples e apresenta um desempenho significativamente melhor que o BubbleSort, em termos absolutos. Além disso, ele é extremamente eficiente para listas que já estejam substancialmente ordenadas e listas com pequeno número de elementos. Observem abaixo o código para a Ordenação de Inserção:
Nesse método, consideramos que a lista está dividida em parte esquerda, já ordenada, e parte direita, em possível desordem. Inicialmente, a parte esquerda contém apenas o primeiro elemento da lista. Cada iteração consiste em inserir o primeiro elemento da parte direta (pivô) na posição adequada da parte esquerda, de modo que a parte esquerda continue ordenada.

É fácil perceber que se a lista possui n elementos, após (n-1) inserções, ela estará ordenada. Para inserir o pivô, percorremos a parte esquerda, da direita para a esquerda, deslocando os elementos estritamente maiores que o pivô uma posição para direita. O pivô deve ser colocado imediatamente à esquerda do último elemento movido.

Complexidade do Algoritmo:

Melhor caso: O ( n )

Caso médio: O ( n ao quadrado )

Pior caso: O ( n ao quadrado )


SelectionSort (Seleção)

Esse algoritmo consiste em selecionar o menorl elemento de um vetor e trocá-lo (swap) pelo item que estiver na primeira posição, i.e., inseri-lo no início do vetor. Essas duas operações são repetidas com os itens restantes até o último elemento. Tem como ponto forte o fato de que realiza poucas operações de swap. Seu desempenho costuma ser superior ao BubbleSort e inferior ao InsertionSort.

Assim como no InsertionSort, considera-se que a lista está dividida em parte esquerda, já ordenada, e parte direita, em possível desordem. Ademais, os elementos da parte esquerda são todos menores ou iguais aos elementos da parte direita. Cada iteração consiste em selecionar o menor elemento da parte direita (pivô) e trocá-lo com o primeiro elemento da parte direita.

Assim, a parte esquerda aumenta, visto que passa a incluir o pivô, e a parte direita diminui. Note que o pivô é maior que todos os demais elementos da parte esquerda, portanto a parte esquerda continua ordenada. Ademais, o pivô era o menor elemento da direita, logo todos os elementos da esquerda continuam sendo menores ou iguais aos elementos da direita. Inicialmente, a parte esquerda é vazia.

Complexidade do Algoritmo:

Melhor caso: O ( n ao quadrado )

Caso médio: O ( n ao quadrado )

Pior caso: O ( n ao quadrado )


QuickSort (Troca)

Esse algoritmo divide um conjunto de itens em conjuntos menores, que são ordenados de forma independente, e depois os resultados são combinados para produzir a solução de ordenação do conjunto maior. Trata-se, portanto, de um algoritmo do tipo Divisão-e-Conquista, i.e., repartindo os dados em subgrupos, dependendo de um elemento chamado pivô.
Talvez seja o método de ordenação mais utilizado! Isso ocorre porque quase sempre ele é significativamente mais rápido do que todos os demais métodos de ordenação baseados em comparação. Ademais, suas características fazem com que ele, assim como o MergeSort, possa ser facilmente paralelizado. Ele também pode ser adaptado para realizar ordenação externa (QuickSort Externo).

Neste método, a lista é dividida em parte esquerda e parte direita, sendo que os elementos da parte esquerda são todos menores que os elementos da parte direita. Essa fase do processo é chamada de partição. Em seguida, as duas partes são ordenadas recursivamente (usando o próprio QuickSort). A lista está, portanto, ordenada corretamente!
Uma estratégia para fazer a partição é escolher um valor como pivô e então colocar na parte esquerda os elementos menores ou iguais ao pivô e na parte direita os elementos maiores que o pivô - galera, a escolha do pivô é crítica! Em geral, utiliza-se como pivô o primeiro elemento da lista, a despeito de existirem maneiras de escolher um "melhor" pivô.

Esse algoritmo é um dos métodos mais rápidos de ordenação, apesar de às vezes partições desequilibradas poderem conduzir a uma ordenação lenta. A eficácia do método depende da escolha do pivô mais adequado ao conjunto de dados que se deseja ordenar. Alguns, por exemplo, utilizam a mediana de três elementos para otimizar o algoritmo.
Alguns autores consideram a divisão em três subconjuntos, sendo o terceiro contendo valores iguais ao pivô. O Melhor Caso ocorre quando o conjunto é dividido em subconjuntos de mesmo tamanho; o Pior Caso ocorre quando o pivô corresponde a um dos extremos (menor ou maior valor). Alguns o consideram um algoritmo frágil e não-estável, com baixa tolerância a erros.

Complexidade do Algoritmo:

Melhor caso: O ( n log de n )

Caso médio: O ( n log de n )

Pior caso: O ( n ao quadrado )


ShellSort (Inserção)

Esse algoritmo é uma extensão ou refinamento do algoritmo do InsertionSort, contornando o problema que ocorre quando o menor item de um vetor está na posição mais à direita. Ademais, difere desse último pelo fato de, em vez de considerar o vetor a ser ordenado como um único segmento, ele considera vários segmentos e aplica o InsertionSort em cada um deles.

É o algoritmo mais eficiente dentre os de ordem quadrática. Nesse método, as comparações e as trocas são feitas conforme determinada distância (gap) entre dois elementos, de modo que, se gap = 6, há comparação entre o 1o e 7o elementos ou entre o 2o e 8o elementos e assim sucessivamente, repetindo até que as últimas comparações e trocas tenham sido efetuadas e o gap tenha chegado a 1.

Complexidade do Algoritmo:

Melhor caso: O ( n log de n )

Caso médio: Depende do gap

Pior caso: O ( n ao quadrado )


MergeSort (Intercalação)

Esse algoritmo é baseado na estratégia de resolução de problemas conhecida como divisão-e- conquista. Essa técnica consiste basicamente em decompor a instância a ser resolvida em instâncias menores do mesmo tipo de problema, resolver tais instâncias (em geral, recursivamente) e por fim utilizar as soluções parciais para obter uma solução da instância original.

Naturalmente, nem todo problema pode ser resolvido através de divisão e conquista. Para que seja viável aplicar essa técnica a um problema, ele deve possuir duas propriedades estruturais. O problema deve ser decomponível, i.e., deve ser possível decompor qualquer instância não trivial do problema em instâncias menores do mesmo tipo de problema.

Além disso, deve ser sempre possível utilizar as soluções obtidas com a resolução das instâncias menores para chegar a uma solução da instância original. No MergeSort, divide-se a lista em duas metades. Essas metades são ordenadas recursivamente (usando o próprio MergeSort) e depois são intercaladas.

Complexidade do Algoritmo:

Melhor caso: O ( n log de n )

Caso médio: O ( n log de n )

Pior caso: O ( n log de n )


HeapSort (Seleção)

Esse algoritmo utiliza uma estrutura de dados chamada heap, para ordenar os elementos à medida que os insere na estrutura. Assim, ao final das inserções, os elementos podem ser sucessivamente removidos da raiz da heap, na ordem desejada. Essa estrutura pode ser representada como uma árvore ou como um vetor. Entenderam? Inicialmente, insere-se os elementos da lista em um heap.

Em seguida, fazemos sucessivas remoções do menor elemento do heap, colocando os elementos removidos do heap de volta na lista - a lista estará então em ordem crescente. O heapsort é um algoritmo de ordenação em que a sua estrutura auxiliar de armazenamento fora do arranjo de entrada é constante durante toda a sua execução.

Complexidade do Algoritmo:

Melhor caso: O ( n log de n )

Caso médio: O ( n log de n )

Pior caso: O ( n log de n )


Tópico. Desenvolvimento de software - Algoritmos de ordenação estáveis.


Os algoritmos de ordenação estáveis são aqueles que preservam a ordem relativa dos elementos com chaves iguais durante o processo de ordenação. Isso significa que se houver dois elementos com a mesma chave, a ordem em que eles aparecem na lista original será mantida na lista ordenada.

A estabilidade dos algoritmos de ordenação é um aspecto importante em várias aplicações. Por exemplo, ao ordenar uma lista de registros com base em um campo específico, é desejável que a ordem original dos registros seja preservada para aqueles que possuem a mesma chave. Isso é especialmente útil quando se trata de classificar por múltiplos critérios, onde a ordem de classificação de um critério não deve afetar a ordem de classificação dos outros critérios.

Aqui estão alguns exemplos de algoritmos de ordenação estáveis comumente utilizados:

Item. 1. Merge Sort: O Merge Sort é um algoritmo de ordenação eficiente e estável que divide a lista em duas metades, ordena cada metade separadamente e, em seguida, combina as duas metades ordenadas em uma única lista ordenada.

Item. 2. Insertion Sort: O Insertion Sort é um algoritmo simples que percorre a lista e, para cada elemento, insere-o na posição correta em relação aos elementos anteriores já ordenados. É um algoritmo estável porque mantém a ordem dos elementos com chaves iguais.

Item. 3. Bubble Sort: O Bubble Sort compara pares de elementos adjacentes e os troca se estiverem fora de ordem. É um algoritmo estável porque não altera a ordem relativa dos elementos com chaves iguais.

Item. 4. Counting Sort: O Counting Sort é um algoritmo de ordenação eficiente para listas com um intervalo limitado de valores. Ele cria um array de contagem para contar a ocorrência de cada valor na lista e, em seguida, usa essas contagens para reconstruir a lista ordenada. O Counting Sort é um algoritmo estável.

Esses são apenas alguns exemplos de algoritmos de ordenação estáveis. Cada algoritmo tem suas vantagens e desvantagens em termos de desempenho e uso de recursos. A escolha do algoritmo depende do tamanho da lista, do tipo de dados e dos requisitos específicos do sistema.


Tópico. Desenvolvimento de software - Algoritmos de ordenação instáveis.


Os algoritmos de ordenação instáveis são aqueles que não garantem a preservação da ordem relativa dos elementos com chaves iguais durante o processo de ordenação. Isso significa que se houver dois elementos com a mesma chave, a ordem em que eles aparecem na lista original pode não ser mantida na lista ordenada.

Embora os algoritmos de ordenação instáveis não sejam adequados para todas as situações, eles ainda podem ser úteis em determinados casos, principalmente quando a ordem relativa dos elementos com chaves iguais não é uma preocupação ou quando a eficiência é um fator crítico. Além disso, alguns algoritmos de ordenação instáveis podem ser mais simples e mais fáceis de implementar.

Aqui estão alguns exemplos de algoritmos de ordenação instáveis comumente utilizados:

Item. 1. Quicksort: O Quicksort é um algoritmo de ordenação eficiente que seleciona um elemento chamado de pivô e rearranja os outros elementos em torno do pivô, de forma que os elementos menores fiquem à esquerda e os elementos maiores fiquem à direita. A ordem relativa dos elementos com chaves iguais pode ser alterada durante o processo de rearranjo.

Item. 2. Heapsort: O Heapsort é um algoritmo de ordenação que utiliza uma estrutura de dados chamada heap para organizar os elementos. Durante o processo de construção do heap e extração dos elementos, a ordem relativa dos elementos com chaves iguais pode ser alterada.

Item. 3. Shellsort: O Shellsort é um algoritmo de ordenação baseado em inserção que divide a lista em várias sublistas e as ordena separadamente. A ordem relativa dos elementos com chaves iguais pode ser alterada durante o processo de ordenação de cada sublista.

Item. 4. Selection Sort: O Selection Sort percorre a lista em busca do menor elemento e o coloca na posição correta. Embora o algoritmo possa ser implementado de forma estável, ele geralmente é implementado de forma instável, o que significa que a ordem relativa dos elementos com chaves iguais pode ser alterada.

É importante considerar a estabilidade ou instabilidade dos algoritmos de ordenação ao escolher o mais adequado para uma determinada tarefa. Em muitos casos, a estabilidade da ordenação é desejável para preservar a ordem relativa dos elementos com chaves iguais. No entanto, em situações em que a ordem relativa não é importante ou quando a eficiência é uma prioridade, os algoritmos de ordenação instáveis podem ser uma opção viável.
