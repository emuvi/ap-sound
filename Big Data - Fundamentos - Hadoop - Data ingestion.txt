Capítulo. Big Data - Fundamentos - Hadoop - Data ingestion.

Data ingestion é o processo de coleta e importação de dados em um sistema de armazenamento ou processamento, como o Hadoop, a fim de tornar esses dados disponíveis para análise, processamento ou armazenamento futuro.

No contexto do Apache Hadoop, a ingestão de dados refere-se à captura e transferência de dados de várias fontes para o ambiente Hadoop, onde eles podem ser armazenados e processados de maneira eficiente. Existem várias formas de realizar a ingestão de dados no Hadoop, incluindo:

Item. 1. Batch ingestion: É a forma mais comum de ingestão de dados no Hadoop. Envolve a transferência de grandes volumes de dados em lotes, geralmente por meio de processos agendados ou programados. Pode-se usar ferramentas como Apache Sqoop ou Apache Flume para importar dados de bancos de dados relacionais, arquivos de log, fontes de streaming, etc.

Item. 2. Streaming ingestion: Também conhecida como ingestão em tempo real, envolve a transferência contínua de dados à medida que eles são gerados pelas fontes. Isso é comumente usado em cenários onde a baixa latência é crítica, como análise de dados em tempo real. O Apache Kafka é uma ferramenta popular para streaming ingestion, permitindo a captura e o processamento de fluxos de dados em tempo real.

Item. 3. Ingestion de dados externos: Além das ferramentas mencionadas acima, o Hadoop também suporta a ingestão de dados externos através de sistemas de arquivos remotos, como o Amazon S3 ou o Google Cloud Storage. Isso permite que você importe dados de fontes externas sem precisar movê-los fisicamente para o cluster Hadoop.

Item. 4. Transformação e pré-processamento de dados: Durante o processo de ingestão, muitas vezes é necessário realizar transformações e pré-processamento nos dados para torná-los adequados para análise posterior. Isso pode envolver filtragem, limpeza, normalização, agregação ou qualquer outra operação necessária para melhorar a qualidade ou a estrutura dos dados.

É importante considerar a escalabilidade, a confiabilidade e a segurança ao projetar e implementar os processos de ingestão de dados no ambiente Hadoop. Isso envolve dimensionar adequadamente o cluster, configurar mecanismos de tolerância a falhas, garantir a integridade dos dados durante a transferência e proteger a segurança e a privacidade dos dados.

Em resumo, a ingestão de dados é um componente fundamental no ecossistema do Hadoop, permitindo a importação eficiente de dados de várias fontes para análise e processamento no ambiente distribuído do Hadoop.
