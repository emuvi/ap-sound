Capítulo. Mecanismos de segurança - Criptografia assimétrica.

A criptografia assimétrica, também conhecida como criptografia de chave pública, é um método de criptografia que utiliza um par de chaves relacionadas matematicamente: uma chave pública e uma chave privada. Diferente da criptografia simétrica, onde a mesma chave é usada para criptografar e descriptografar os dados, a criptografia assimétrica utiliza uma chave para criptografar os dados e outra chave para descriptografá-los.
A chave pública é amplamente distribuída e pode ser conhecida por qualquer pessoa. Ela é usada para criptografar os dados pelo remetente antes de serem enviados. Uma vez criptografados com a chave pública, os dados só podem ser descriptografados com a chave privada correspondente, que é mantida em sigilo e conhecida apenas pelo destinatário autorizado.

A criptografia assimétrica oferece algumas vantagens importantes:

Item. 1. Confidencialidade: Como os dados são criptografados com a chave pública, somente o destinatário com a chave privada correspondente pode descriptografá-los e acessar as informações originais. Isso garante a confidencialidade dos dados transmitidos.

Item. 2. Autenticidade: A criptografia assimétrica também é usada para autenticar a origem dos dados. O remetente pode assinar digitalmente os dados usando sua chave privada, o que comprova que a mensagem foi realmente enviada por ele. O destinatário pode verificar a assinatura usando a chave pública correspondente, garantindo que os dados não foram alterados e que foram enviados pelo remetente esperado.

Item. 3. Troca segura de chaves: A criptografia assimétrica permite a troca segura de chaves simétricas. Em uma comunicação segura, os participantes podem usar criptografia assimétrica para estabelecer uma chave de sessão simétrica compartilhada. Uma vez estabelecida a chave de sessão, eles podem usar criptografia simétrica para proteger a comunicação subsequente, que é mais eficiente em termos de recursos computacionais.

Alguns algoritmos de criptografia assimétrica comumente usados incluem:

Item. 1. RSA: É um dos algoritmos assimétricos mais populares e amplamente utilizado. O RSA é baseado na dificuldade de fatoração de números grandes.

Item. 2. ECC (Elliptic Curve Cryptography): É um algoritmo baseado na matemática das curvas elípticas. Ele oferece um nível de segurança semelhante ao RSA com tamanhos de chave menores, tornando-o eficiente em termos de recursos computacionais.

Item. 3. DSA (Digital Signature Algorithm): É um algoritmo utilizado especificamente para assinaturas digitais, garantindo a autenticidade dos dados e a integridade da mensagem.

A criptografia assimétrica é frequentemente combinada com a criptografia simétrica para obter uma solução de segurança mais robusta. Ela é amplamente utilizada em diversos cenários, como comunicação segura na Internet, autenticação de usuários, troca segura de chaves e garantia da integridade dos dados.


Tópico. Como funciona o algoritmo de criptografia assimétrica DH.


O algoritmo de criptografia assimétrica Diffie-Hellman (DH) é amplamente utilizado para estabelecer uma chave de sessão compartilhada entre duas partes que desejam se comunicar de forma segura em um canal inseguro. O DH é um algoritmo de troca de chaves, o que significa que seu objetivo é permitir que duas partes estabeleçam uma chave secreta compartilhada sem que a chave seja transmitida pela rede.

Aqui está um resumo de como funciona o algoritmo de criptografia assimétrica DH:

Item. 1. Parâmetros de chave pública: Antes da comunicação começar, as duas partes concordam em alguns parâmetros comuns, incluindo um número primo grande (p) e um número inteiro (g) chamado de gerador. Esses parâmetros são públicos e podem ser conhecidos por qualquer pessoa.

Item. 2. Geração das chaves privadas: Cada parte gera sua própria chave privada, que é um número aleatório e secreto. Vamos chamar essas chaves privadas de "a" e "b" para as duas partes.

Item. 3. Cálculo das chaves públicas: Com base nas chaves privadas geradas, cada parte calcula sua chave pública. A chave pública é calculada usando a fórmula: A = g^a mod p para a primeira parte e B = g^b mod p para a segunda parte.

Item. 4. Troca das chaves públicas: As partes trocam suas chaves públicas através de um canal inseguro, como a internet.

Item. 5. Cálculo da chave de sessão: Com base nas chaves públicas recebidas, cada parte calcula a chave de sessão compartilhada usando a fórmula: S = B^a mod p para a primeira parte e S = A^b mod p para a segunda parte.

Item. 6. Chave de sessão compartilhada: Agora, as duas partes têm uma chave de sessão compartilhada que pode ser usada para criptografar e descriptografar a comunicação entre elas. A chave de sessão é única para a sessão atual e não é transmitida pela rede.

O algoritmo DH é baseado no problema do logaritmo discreto, que é computacionalmente difícil de resolver. Isso significa que mesmo que um invasor conheça os parâmetros públicos, as chaves públicas trocadas e observe a comunicação, é computacionalmente impraticável para ele calcular a chave de sessão sem a chave privada correta.

O algoritmo DH é amplamente utilizado em criptografia de chave pública, especialmente em protocolos de comunicação segura, como o SSL/TLS. Ele permite que duas partes estabeleçam uma chave de sessão compartilhada sem a necessidade de compartilhar a chave diretamente, tornando a comunicação segura e protegida contra ataques de interceptação e análise criptográfica.


Tópico. Como funciona o algoritmo de criptografia assimétrica RSA.


O algoritmo de criptografia assimétrica RSA (Rivest-Shamir-Adleman) é amplamente utilizado para criptografia e assinatura digital. Ele envolve o uso de um par de chaves, uma chave pública e uma chave privada, que são geradas juntas, mas têm propriedades matemáticas específicas que garantem sua segurança.

Aqui está um resumo de como funciona o algoritmo de criptografia assimétrica RSA:

Item. 1. Geração das chaves: O processo começa com a geração do par de chaves. Isso envolve a seleção de dois números primos grandes e distintos, p e q. A multiplicação desses dois primos produz um número chamado n, que será usado como parte da chave pública e privada. Além disso, é calculado o valor da função totiente de Euler, denotada como φ(n), que é usada para determinar a chave privada. O processo de geração das chaves também envolve a seleção de um número inteiro e primo menor que φ(n), conhecido como e, que será usado como parte da chave pública.

Item. 2. Chave pública: A chave pública consiste no par (n, e). A chave pública é compartilhada com qualquer pessoa que queira enviar uma mensagem criptografada para o proprietário da chave privada. A chave pública é usada para criptografar a mensagem.

Item. 3. Chave privada: A chave privada consiste no par (n, d). O valor de d é calculado usando a função totiente de Euler φ(n), o número primo e e. A chave privada é mantida em segredo e é usada para descriptografar a mensagem criptografada.

Item. 4. Criptografia: Para criptografar uma mensagem usando a chave pública, o remetente converte a mensagem em um número inteiro e aplica uma fórmula matemática para calcular o valor criptografado. O valor criptografado é a mensagem criptografada que será enviada ao destinatário.

Item. 5. Descriptografia: O destinatário recebe a mensagem criptografada e usa sua chave privada para descriptografar a mensagem. O destinatário aplica uma fórmula matemática para obter o valor original da mensagem.

O algoritmo RSA é baseado na dificuldade de fatorar números inteiros grandes em seus fatores primos. A segurança do algoritmo depende da dificuldade de calcular a chave privada d a partir da chave pública (n, e) sem conhecer os fatores primos p e q.

O RSA é amplamente utilizado em sistemas de segurança, como criptografia de dados, assinaturas digitais, autenticação e troca segura de chaves. É um dos algoritmos de criptografia assimétrica mais conhecidos e amplamente adotados na prática.


Tópico. Como funciona o algoritmo de criptografia assimétrica HMAC.


O algoritmo HMAC (Hash-based Message Authentication Code) é uma forma de criptografia assimétrica que combina funções hash criptográficas e chaves secretas para autenticar a integridade e a autenticidade de dados transmitidos. Ele é amplamente utilizado para verificar a integridade de mensagens e proteger contra ataques de falsificação ou modificação de dados.

O HMAC usa uma função hash criptográfica, como o SHA-256 ou o SHA-512, juntamente com uma chave secreta compartilhada entre o remetente e o destinatário. A chave secreta é conhecida apenas por essas partes e é usada para gerar o código de autenticação da mensagem.

Aqui está uma visão geral de como o algoritmo HMAC funciona:

1. Definição da chave: O remetente e o destinatário concordam em uma chave secreta compartilhada que será usada para gerar e verificar o HMAC. Essa chave deve ser mantida em segredo e não deve ser divulgada a terceiros.

2. Divisão da mensagem: O remetente divide a mensagem em blocos de tamanho fixo (geralmente do tamanho do bloco de hash utilizado). Se a mensagem não for um múltiplo do tamanho do bloco, ela será preenchida com bytes adicionais.

3. Geração do HMAC: O remetente aplica a função hash criptográfica (por exemplo, SHA-256) na primeira divisão da mensagem e combina o resultado com a chave secreta. O resultado é passado novamente pela função hash e novamente combinado com a chave secreta. Esse processo é repetido até que todas as divisões da mensagem tenham sido processadas. O resultado final é o HMAC.

4. Transmissão: O remetente envia a mensagem e o HMAC ao destinatário.

5. Verificação do HMAC: O destinatário recebe a mensagem e a chave secreta compartilhada. Ele executa o mesmo processo de geração do HMAC aplicando a função hash criptográfica na mensagem recebida e na chave secreta. O resultado final é comparado com o HMAC recebido do remetente. Se os HMACs coincidirem, isso indica que a mensagem não foi modificada e é autêntica. Caso contrário, pode-se concluir que a mensagem foi modificada ou que a chave secreta não coincide.

O HMAC oferece uma forte garantia de integridade e autenticidade dos dados, pois o HMAC é calculado usando uma chave secreta que só é conhecida pelo remetente e pelo destinatário. Mesmo que um invasor intercepte a mensagem e o HMAC, ele não será capaz de gerar um HMAC válido sem a chave secreta. Isso ajuda a proteger a comunicação contra ataques de falsificação ou modificação.

É importante ressaltar que o HMAC não fornece confidencialidade dos dados, ou seja, não criptografa a mensagem em si. Ele apenas garante a integridade e autenticidade dos dados transmitidos. Se você precisar de confidencialidade, é necessário utilizar criptografia adicional, como criptografia simétrica ou criptografia assimétrica.


Tópico. Como funciona o algoritmo de criptografia assimétrica ECDSA.


O ECDSA (Elliptic Curve Digital Signature Algorithm) é um algoritmo de criptografia assimétrica baseado em curvas elípticas. Ele é usado principalmente para assinaturas digitais, permitindo a verificação da autenticidade e integridade de dados, bem como a não repúdio das mensagens.

Aqui está uma visão geral de como o algoritmo ECDSA funciona:

1. Geração das chaves: O primeiro passo é gerar um par de chaves assimétricas. Isso envolve a escolha de uma curva elíptica e a geração de uma chave privada e uma chave pública correspondente. A chave privada é um número aleatório e secreto, enquanto a chave pública é derivada matematicamente da chave privada e pode ser divulgada publicamente.

2. Assinatura digital: Para assinar uma mensagem, o remetente segue os seguintes passos:

   a) Conversão da mensagem: A mensagem é convertida em um valor numérico adequado para cálculos.

   b) Geração de um valor efêmero: Um valor efêmero aleatório, conhecido como "k", é gerado para cada assinatura.

   c) Cálculo do ponto da curva elíptica: O remetente calcula um ponto na curva elíptica multiplicando o ponto gerador da curva pelo valor efêmero "k".

   d) Derivação da coordenada x: A coordenada "x" do ponto calculado é obtida.

   e) Cálculo do valor "r": O valor "r" é calculado a partir da coordenada "x" do ponto calculado. "r" é uma parte da assinatura digital.

   f) Cálculo do valor "s": O remetente calcula o valor "s" usando a chave privada, a mensagem e o valor "r". "s" é outra parte da assinatura digital.

   g) Combinação da assinatura: A assinatura digital é formada pelos valores "r" e "s".

3. Verificação da assinatura: Para verificar a assinatura, o destinatário segue os seguintes passos:

   a) Recebimento da mensagem e da assinatura.

   b) Extração dos valores "r" e "s" da assinatura.

   c) Conversão da mensagem recebida em um valor numérico adequado para cálculos.

   d) Cálculo do valor "w": O destinatário calcula o valor "w" usando o inverso multiplicativo de "s" (módulo a ordem da curva elíptica).

   e) Cálculo do valor "u1" e "u2": O destinatário calcula os valores "u1" e "u2" multiplicando o valor "w" pelo valor numérico da mensagem e pelo valor "w" pelo valor "r", respectivamente.

   f) Cálculo do ponto da curva elíptica: O destinatário calcula um ponto na curva elíptica somando os pontos geradores da curva multiplicados pelos valores "u1" e "u2", respectivamente.

   g) Derivação da coordenada x: O destinatário obtém a coordenada "x" do ponto calculado.

   h) Verificação da assinatura: A assinatura é considerada válida se o valor "r" calculado anterior

   