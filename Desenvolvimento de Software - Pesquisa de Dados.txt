Capítulo. Desenvolvimento de Software - Pesquisa de Dados.


No desenvolvimento de software, a pesquisa de dados refere-se à busca eficiente por informações específicas em um conjunto de dados. A pesquisa de dados desempenha um papel fundamental em muitos aplicativos, desde a busca em bancos de dados até a filtragem de resultados em interfaces de usuário.

Existem diferentes algoritmos e estruturas de dados que podem ser utilizados para realizar pesquisas eficientes. Alguns dos métodos mais comuns incluem:

Item. 1. Pesquisa Linear: Também conhecida como busca sequencial, é o método mais simples de pesquisa. Ele percorre cada elemento do conjunto de dados, um por um, até encontrar o elemento desejado ou determinar que ele não está presente. A pesquisa linear possui complexidade de tempo O(n), onde n é o número de elementos no conjunto de dados.

Item. 2. Pesquisa Binária: É um método eficiente aplicável apenas em conjuntos de dados ordenados. A pesquisa binária divide repetidamente o conjunto de dados pela metade, descartando metade dos elementos a cada iteração. Dessa forma, a busca converge rapidamente para o elemento desejado. A pesquisa binária possui complexidade de tempo O(log n), onde n é o número de elementos no conjunto de dados.

Item. 3. Árvores de Busca: Estruturas de dados como árvores binárias de busca e árvores balanceadas, como a árvore AVL e a árvore vermelha-preta, são utilizadas para realizar pesquisas eficientes em conjuntos de dados ordenados. Essas estruturas de dados permitem uma busca rápida com complexidade de tempo O(log n).

Item. 4. Tabelas de Hash: Uma tabela de hash é uma estrutura de dados que mapeia chaves para valores. Ela utiliza uma função de hash para converter a chave em um índice de acesso direto à tabela. A pesquisa em tabelas de hash pode ser extremamente rápida, com complexidade de tempo médio O(1). No entanto, o desempenho pode ser degradado em casos de colisões de hash.

Item. 5. Pesquisa em Texto: Para pesquisas em textos, são comumente utilizadas técnicas como o algoritmo de Boyer-Moore e o algoritmo de Knuth-Morris-Pratt. Esses algoritmos permitem buscar eficientemente padrões em um texto, levando em consideração técnicas como pré-processamento de padrões e aproveitamento de informações prévias.

A escolha do algoritmo de pesquisa mais adequado depende do contexto específico, como o tamanho do conjunto de dados, a ordem dos dados, a frequência de pesquisas e as restrições do sistema. É importante considerar a complexidade de tempo, o consumo de memória e outros fatores relevantes para determinar a melhor abordagem.

Além disso, também é possível utilizar índices, otimizações de consultas e técnicas de pesquisa avançadas para melhorar a eficiência das pesquisas, especialmente em bancos de dados complexos e grandes volumes de dados.


Uma das tarefas de maior importância na computação é a pesquisa de informações contidas em coleções de dados. Em geral, desejamos que essa tarefa seja executada sem que haja a necessidade de inspecionar toda a coleção de dados. Existem algumas maneiras de realizar pesquisas, tais como: Pesquisa Sequencial, Pesquisa Binária, Tabelas de Dispersão (Hashing), Árvores AVL, Árvores B e Árvores B+.

Busca Sequencial

Galera, imaginem que eu estou à procura de um valor X em um vetor L [ ]! Para tal, posso inspecionar as posições sequenciais de L[ ] a partir da primeira posição: se eu encontrar X, minha busca tem êxito; se eu alcanço a última posição e não encontro X, concluímos que esse valor não ocorre no vetor L [ ]. Como é chamada essa busca em que eu inspeciono uma estrutura posição por posição? Sequencial ou Linear.
Considerando que o vetor L [ ] contém N elementos, ordenados ou não, é fácil verificar que a busca sequencial requer tempo linearmente proporcional ao tamanho do vetor, i.e., da ordem O ( n ). Por conta disso, é comum dizer que a busca sequencial é uma Busca Linear.
Entenderam? Quanto maior o vetor, maior o tempo em média para buscar um elemento! Quanto mais ao final, mais demorado.

A Busca Sequencial é muito lenta para grandes quantidades de dados, mas aceitável para listas pequenas e que mudam constantemente. Observa-se que no Melhor Caso, X está na primeira posição, logo necessita apenas de uma comparação; no Pior Caso, X está na última posição, logo necessita de N comparações; e no Caso Médio, X é encontrado após ( n + 1 ) / 2 comparações.

A seguir, encontram-se dois algoritmos para realização de uma Busca Sequencial: o primeiro ocorre de forma simples e o segundo ocorre de forma recursiva. Galera, para vetores de médio ou grande porte, o tempo de busca sequencial é considerado completamente inaceitável, dado que existem técnicas mais eficientes! Professor, me dá um exemplo? Claro, veremos adiante: Busca Binária!

Busca Binária

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e- conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O ( log 2 n ), em que N é o tamanho do vetor de busca.

Quando o Vetor L [ ] estiver em ordem crescente, podemos determinar se X ocorre em L [ ] de forma mais rápida da seguinte forma: inspeciona-se a posição central do vetor! Se essa posição já contiver X, a busca para! Por que, professor? Porque nós já encontramos X! Se X for menor que esse elemento central, passamos a procurar X, recursivamente, no intervalo de L [ ] que se encontra à esquerda da posição central.

Se X for maior do que o elemento central, continuamos a procurar X, recursivamente, no intervalo de L que está à direita da posição central. Se o intervalo se tornar vazio, a busca para, tendo sido malsucedida. Esse procedimento é conhecido como Busca Binária e, facilmente, pode-se adaptar a busca em ordem decrescente.

Na imagem abaixo, estamos à procura do valor 23! Em vermelho, encontra-se o elemento inicial L [ 0 ] = 2 e, em amarelo, encontra-se o elemento final L [ N - 1 ] = 57. Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 7 / 2 = 3 , 5 = 3 (Arredonda-se para baixo). Ora, L [ 3 ] = 19! Encontramos? Não, 23 > 19! Sendo assim, L [ 0 ] = 19 e L [ 4 ] = 57.

Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 4 / 2 = 2. Ora, L [ 2 ] = 51! Encontramos? Não, 23 < 51! Sendo assim, L [ 0 ] = 19 e L [ 2 ] = 51. Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 2 / 2 = 1. Ora, L [ 1 ] = 23! Encontramos? Sim! Então, nossa busca obteve êxito e encontramos o que buscávamos.

