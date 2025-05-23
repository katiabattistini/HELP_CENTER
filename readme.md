# Indicadores de Atendimento ao Cliente

Este projeto visa o desenvolvimento de indicadores de atendimento ao cliente para uma empresa que fornece soluções de diagnóstico por imagem em nuvem. 
A principal meta é otimizar o serviço de suporte ao cliente, garantindo um atendimento mais eficiente e baseado em dados.
**Este case é real que impactou diretamente na dinâmica da área com interações entre outros departamentos e permitiu elucidar GAPS e problemas, para manter a confidencialidade dos dados sensíveis, a base disponilizada foi alterada.**

## Descrição do Problema

Antes da implementação deste projeto, o atendimento ao cliente não possuía indicadores estabelecidos. Todo o processo era centrado na resolução imediata de problemas, sem análises que permitissem melhorias contínuas. A solução proposta integra uma plataforma de atendimento multicanal, facilitando a gestão de diferentes áreas por meio de indicadores de desempenho.

## Fonte de Dados

Os dados são extraídos de uma API de plataforma de atendimento ao cliente, fornecendo informações detalhadas sobre cada ticket de atendimento. As colunas incluídas no processo são:

- **protocol**: Identificador único do ticket de atendimento.
- **updatedAt**: Data e hora da última atualização do ticket.
- **startedAt**: Data e hora em que o atendimento foi iniciado.
- **endedAt**: Data e hora em que o atendimento foi concluído.
- **contact_name**: Nome do contato do cliente.
- **user_name**: Nome do usuário que atendeu o ticket.
- **department_name**: Nome do departamento responsável pelo atendimento.
- **ticket_topic_name**: Tópico do ticket, indicando o tipo de problema ou solicitação.
- **contact_tags_label**: Etiquetas associadas ao contato, usadas para categorização.
- **contact_customFieldValues_customField_name**: Valores dos campos personalizados associados ao contato.
- **user_email**: E-mail do usuário responsável pelo ticket.

## Processo ETL

O pipeline ETL em Python foi utiilzado para fazer as primeiras análises exploratórias e posteriormente, foi aprimorado para também ser utilizado como fonte de dados no Power BI e assim, permitir atualizações periódicas diretamente pelo Power BI.

1. **Extração**: Conecta à API utilizando requests para obter os dados.
2. **Transformação**: Utiliza pandas para limpeza, normalização e preenchimento de dados ausentes, garantindo a integridade das informações.
3. **Carregamento**: Os dados processados são armazenados em arquivos CSV para fácil integração com o Power BI.

**Os dados disponibilizados foram gerados utilizando a biblioteca Faker seguindo as mesmas proporções da base original**

## Dashboard

O resultado do processo ETL é utilizado para gerar dashboards no Power BI, permitindo visualizações  e insights  para a equipe de atendimento, como:

- Total de atendimento por período selecionado;
- Média de atendimento por mês e por área;
- Distribuição de atendimento por período;
- Análise de carga de trabalho por departamento;
- Ranking de atendimento por assunto;
- Ranking de atendimento por cliente;
- Ranking de atendimento por Atendente;
- Tempo Médio de atendimento por cliente, assunto e atendente;
- Distribuição de chamados por hora do dia  no periodo selecionado;
- Distribuição de tempo de atendimento por grupos de dias

## Principais insights

1. **Dias com maior quantidade de atendimentos são os mesmos dias em que houveram atualizações no produto ("dia de deploy")**

    Impactos: Sobrecarga na área de atendimento e maior índice de insatisfação de clientes.

    Ações: Melhoria de comunicação entre as áreas de desenvolvimento, treinamento e atendimento. Melhoria nos processos na área de desenvolvimento com melhor aplicação de metodologia Ágil.

2. **Subcontagem de reincidência de atendimentos do mesmo cliente por falha no processo de padronização de contatos**

    Impactos: Atendentes diferentes atendiam o mesmo cliente, falhas no entendimento de necessidade de melhorias de processo do produto.

    Ações: Padronização de base de contatos por clientes, melhorias no fluxo de atendimentos para permitir continuidade e alinhamento de informações.

3. **Sobrecarga e/ ou ociosidade de atendentes por distribuição de pessoas desalinhado com horários de maiores demandas** 

    Impactos: Atendentes mais experientes atendiam mais chamados para cobrir demandas, horários com menos chamados eram subnotificados.

    Ações: Redistribuição de atendentes equilibrando capacidade e demanda e melhor equilíbrio de senioridade.

4.  **Principais assuntos de atendimentos estavam relacionadados a falha de treinamento de clientes**

    Impactos: Ocupação de atendentes e treinamentos sem entendimento das necessidades do cliente.

    Ações: Melhoria de processos nas áreas de Vendas , remodelagem de Onboarding de Clientes e execução de treinamentos presenciais.


