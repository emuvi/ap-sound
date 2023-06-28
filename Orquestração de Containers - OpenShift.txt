Capítulo. Orquestração de Containers - OpenShift.


O OpenShift é uma plataforma de contêineres baseada no Kubernetes, desenvolvida pela Red Hat. Ele fornece recursos adicionais e uma experiência aprimorada em relação ao Kubernetes padrão. O OpenShift adiciona camadas extras de abstração e automação, facilitando a implantação, o gerenciamento e a escala de aplicativos em contêineres.

Aqui estão alguns aspectos-chave da orquestração de contêineres com o OpenShift:

Item. 1. Construção e Implantação: O OpenShift oferece recursos integrados para compilar e implantar aplicativos em contêineres. Ele suporta várias opções de build, incluindo a criação de imagens Docker, builds baseados em código-fonte e integração com sistemas de controle de versão, como o Git. Além disso, o OpenShift permite a implantação automatizada de aplicativos em contêineres usando implantações declarativas.

Item. 2. Gerenciamento de Imagens: O OpenShift possui seu próprio registro de imagens, chamado de OpenShift Container Registry. Ele permite armazenar, compartilhar e gerenciar imagens de contêineres em um ambiente seguro. O registro de imagens também suporta a construção de imagens internamente, bem como integração com registros externos, como o Docker Hub.

Item. 3. Projetos e Multitenancy: O OpenShift permite a criação de projetos, que são espaços isolados para equipes ou aplicativos. Os projetos fornecem isolamento de recursos, controle de acesso e segregação de rede entre os aplicativos implantados no cluster do OpenShift. Isso facilita a implantação de vários aplicativos em um único cluster, fornecendo recursos de multitenancy.

Item. 4. CI/CD: O OpenShift suporta pipelines de integração contínua e entrega contínua (CI/CD). Ele permite a configuração de pipelines automatizados para construir, testar e implantar aplicativos em contêineres. Os pipelines podem ser configurados para serem acionados automaticamente em resposta a eventos, como alterações no código-fonte ou em um repositório Git.

Item. 5. Monitoramento e Logs: O OpenShift possui recursos integrados de monitoramento e registro de logs. Ele oferece suporte a várias soluções de monitoramento, como Prometheus, Grafana e Elastic Stack, para ajudar a coletar métricas e monitorar o desempenho dos aplicativos em contêineres. Além disso, o OpenShift permite o envio de logs de aplicativos para soluções de centralização de logs, como o Elasticsearch e o Splunk.

Item. 6. Operações e Escalabilidade: O OpenShift fornece recursos avançados de operações e escalabilidade. Ele suporta a escalabilidade automática com base em métricas, permitindo que os aplicativos se adaptem dinamicamente às demandas de carga. O OpenShift também oferece recursos de implantação e rollback de aplicativos, além de permitir a aplicação de políticas de acesso e segurança granulares.

Esses são apenas alguns dos recursos e benefícios que o OpenShift oferece para a orquestração de contêineres. Ele simplifica a implantação e o gerenciamento de aplicativos em contêineres, fornecendo uma camada adicional de abstração e automação em cima do Kubernetes.


O OpenShift é uma ferramenta muito poderosa que além de orquestrar e gerenciar containers, oferece segurança, monitoramento e controle. Com o OpenShift podemos criar um ambiente baseado em containers e colocar aplicações construídas em diversas linguagens como: Java, Python, Ruby, e PHP, para rodar e escalar facilmente, trazendo maior agilidade no desenvolvimento utilizando metodologias DevOps, atendendo mais rapidamente e com menor esforço as demandas de negócio.
A containerização é fator fundamental aqui no OpenShift, já que ele monitora os status dos clusters. Se lembrar do funcionamento do Kubernetes vai perceber que temos containers como serviço basicamente, que em essência nada mais é que a automatização do dimensionamento das operações com as aplicações. Obviamente também temos automonitoramento, balanceamento, orquestração, armazenamento, etc.

Dito isso, no OpenShift a Red Hat buscou ampliar esse conceito, enquanto que o Kubernetes é o Kernel dos sistemas distribuídos em containers, o OpenShift é uma plataforma de containers Kubernetes baseada em nuvem, literalmente um legitimo PAAS (Plataform as a service), além de parcialmente ser construído em Docker também.
Logo, o OpenShift oferece segurança consistente, monitoramento integrado, gerenciamento centralizado de políticas e compatibilidade com cargas de trabalho de contêiner do Kubernetes. É rápido, permite o provisionamento de autoatendimento e se integra a uma variedade de ferramentas. Em outras palavras, não há dependência de fornecedor.
Tanto o Kubernetes quanto o OpenShift apresentam uma arquitetura robusta e escalável que permite o desenvolvimento, a implantação e o gerenciamento de aplicativos rápidos e em larga escala. Temos então algumas diferenças fundamentais aqui, principalmente no tocante a implantação, vejamos:

O Kubernetes oferece mais flexibilidade como uma estrutura de código aberto e pode ser instalado em praticamente qualquer plataforma — como Microsoft Azure e AWS — bem como em qualquer
distribuição Linux, incluindo Ubuntu e Debian. O OpenShift, por outro lado, requer o Red Hat Enterprise Linux Atomic Host (RHELAH), Fedora ou CentOS proprietário da Red Hat. Isso restringe as opções para muitas empresas, especialmente se elas ainda não estiverem usando essas plataformas. As imagens no OpenShift são armazenadas no componente registry.
Enquanto que o Kubernetes contém uma interface web complexa que pode confundir os novatos.

Os usuários que desejam acessar a interface gráfica do usuário (GUI) da Web do Kubernetes devem instalar o painel do Kubernetes e usar o kube-proxy para enviar a porta de sua máquina para o servidor de cluster. Já o OpenShift, por outro lado, apresenta um console web intuitivo que inclui uma página de login com um toque. O console oferece uma interface simples e baseada em formulário, permitindo que os usuários adicionem, excluam e modifiquem recursos. As imagens dos contêineres no OpenShift podem ser armazenadas no componente denominado registry. No OpenShift o estado persistente do master é armazenado no componente etcd.

Logo, tanto o Kubernetes quanto o OpenShift são sistemas populares de gerenciamento de contêineres e cada um tem seus recursos e benefícios exclusivos. Enquanto o Kubernetes ajuda a automatizar a implantação, o dimensionamento e as operações de aplicativos, o OpenShift é a plataforma de contêiner que funciona com o Kubernetes para ajudar os aplicativos a serem executados com mais eficiência.

