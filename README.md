# Python Resume

Este projeto é um worker que escuta mensagens de um bot do Telegram e gera resumos de diferentes tipos de conteúdo, como textos, vídeos e áudios.

## Estrutura

- **Configuração do Telegram**: A classe `Telegram` configura a comunicação com o bot do Telegram e escuta as mensagens.
- **Estratégia de Mensagens**: Dependendo do tipo de mensagem recebida (texto, áudio, vídeo), diferentes estratégias de processamento são aplicadas.
- **Auditoria**: A classe `Audit` mantém um log de todas as mensagens processadas e seus resultados.
- **Banco de Dados**: Conecta-se a um banco de dados MySQL para armazenar dados relacionados ao processo de mensagens, utilizando o padrão DAO e DTO.
- **Resumo**: Usa uma classe de resumo para gerar resumos de mensagens recebidas.

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Entre na pasta src:
   ```bash
   cd src
   ```

3. Execute o programa:
   ```bash
   python -m worker.__main__
   ```