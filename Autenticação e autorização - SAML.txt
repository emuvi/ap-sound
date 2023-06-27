Capítulo. Autenticação e autorização - SAML.

SAML (Security Assertion Markup Language) é um padrão de troca de informações de autenticação e autorização entre provedores de identidade (IdPs) e provedores de serviços (SPs). Ele permite que um usuário autenticado em um provedor de identidade acesse serviços ou aplicativos oferecidos por provedores de serviços sem precisar fazer login novamente.

O SAML opera com base em uma arquitetura de confiança entre o provedor de identidade e o provedor de serviço. Aqui estão os principais componentes e conceitos do SAML:

Item. 1. Provedor de Identidade (Identity Provider - IdP): É o serviço responsável por autenticar usuários e emitir afirmações de segurança (assertions) sobre a identidade do usuário. O IdP autentica o usuário e gera um token de afirmação de segurança, que contém informações como o ID do usuário, atributos de perfil e outras informações relevantes.

Item. 2. Provedor de Serviço (Service Provider - SP): É o serviço que fornece um aplicativo, serviço ou recurso que o usuário deseja acessar. O SP confia nas afirmações de segurança emitidas pelo IdP para permitir o acesso aos seus serviços. Ele atua como o destino final para o usuário após a autenticação.

Item. 3. Assertion (Afirmação): É um conjunto de informações estruturadas em XML que é emitido pelo IdP para o SP após uma autenticação bem-sucedida. Essas afirmações contêm informações sobre a identidade do usuário, como seu ID, nome, atributos de perfil e outras informações relevantes. O SP confia nas afirmações de segurança para tomar decisões de autorização.

Item. 4. Protocolo SAML: É o conjunto de mensagens e interações entre o IdP e o SP para autenticação e troca de informações. O protocolo SAML inclui mensagens como "AuthnRequest" (solicitação de autenticação) enviada pelo SP para o IdP, "Response" (resposta) contendo as afirmações de segurança emitidas pelo IdP e outras
mensagens relacionadas à autenticação e autorização.

Item. 5. Metadata: É um documento XML que contém informações sobre o IdP e o SP. Ele descreve detalhes como a localização dos endpoints SAML, chaves públicas, URLs de retorno, atributos suportados e outras informações relevantes. O metadata é usado para estabelecer a confiança entre o IdP e o SP.

O SAML é amplamente utilizado em cenários de Federação de Identidade, onde várias organizações ou serviços colaboram para permitir o compartilhamento seguro de recursos. Ele oferece benefícios como autenticação única (SSO), onde os usuários podem acessar vários serviços com um único login, maior controle sobre o acesso aos recursos, interoperabilidade entre diferentes provedores de identidade e provedores de serviço, e suporte para cenários de negócios complexos.

No entanto, a implementação do SAML pode ser complexa e requer configuração adequada tanto no IdP quanto no SP. Além disso, o SAML opera principalmente em ambientes baseados em navegador e não é adequado para todas as aplicações. Novas tecnologias, como o OpenID Connect, têm ganhado popularidade como alternativas ao SAML para cenários de autenticação e autorização.
