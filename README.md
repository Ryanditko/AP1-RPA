# AP1 - RPA: Projeto de Automação com Python

## Descrição
Este projeto implementa um assistente virtual automatizado que lê uma lista de tarefas de um arquivo CSV e executa ações automatizadas no computador, como clicar, digitar, pressionar teclas e aguardar.

## Estrutura do Projeto
```
automacao_RPA/
├── main.py                  # Script principal
├── requirements.txt         # Dependências do projeto
├── README.md               # Este arquivo
├── exemplo.md              # Exemplo de documentação
├── core/                   # Módulos principais
│   ├── __init__.py
│   ├── actions.py          # Implementação das ações
│   ├── conditions.py       # Condições de execução
│   ├── executor.py         # Executor principal
│   ├── report.py           # Geração de relatórios
│   └── utils.py            # Utilitários diversos
├── data/                   # Dados e configurações
│   ├── tasks.csv           # Arquivo com lista de tarefas
│   ├── positions.json      # Mapeamento de posições na tela
│   └── output/             # Relatórios gerados
├── tools/                  # Ferramentas auxiliares
│   ├── capture_pos.py      # Captura de posições do mouse
│   └── test_clicks.py      # Testes de cliques
└── docs/                   # Documentação adicional
    └── AP1 - RPA.pdf
```

## Instalação
1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

### 1. Configurar posições de clique
Para configurar posições de clique, execute:
```bash
python tools/capture_pos.py
```
Use esta ferramenta para capturar posições do mouse em tempo real e salve no arquivo `data/positions.json`.

### 2. Executar o projeto
```bash
python main.py
```

### 3. Formato do arquivo de tarefas
O arquivo `data/tasks.csv` deve conter as colunas:
- **Tarefa**: Descrição da ação
- **Tipo**: Tipo de ação (`click`, `texto`, `tecla`, `espera`)
- **Dado**: Dados para a ação (nome da posição, texto, tecla ou tempo)
- **Condicional**: Condição para executar ou não as terefas (opcional)
- **Nota**: Detalhamento das ações (opcional)

Exemplo de arquivo CSV:
```csv
Tarefa,Tipo,Dado
Abrir navegador,click,navegador_icone
Aguardar carregamento,espera,3
Clicar na barra de endereço,click,barra_endereco
Digitar URL,texto,https://www.google.com
Pressionar Enter,tecla,enter
Aguardar página carregar,espera,2
Clicar na caixa de pesquisa,click,caixa_pesquisa
Digitar termo de pesquisa,texto,Python RPA
Pressionar Enter para pesquisar,tecla,enter
Aguardar resultados,espera,3
```

### 4. Tipos de ação suportados
- **click**: Clica em uma posição mapeada no arquivo `positions.json`
- **texto**: Digita o texto especificado
- **tecla**: Pressiona uma tecla específica
- **espera**: Aguarda o tempo especificado (em segundos)

### 5. Relatório de Execução
Após a execução, um relatório é gerado em `data/output/report_execucao.xlsx` contendo:
- Tarefa executada
- Status (Sucesso/Falha/Erro)
- Tempo de execução
- Detalhes de erro (se houver)

## Ferramentas Auxiliares

### Captura de Posições (`tools/capture_pos.py`)
Ferramenta para capturar coordenadas de elementos na tela em tempo real. 

### Teste de Cliques (`tools/test_clicks.py`)
Ferramenta para testar as posições configuradas no arquivo `positions.json`.

## Módulos do Sistema

### Core (`core/`)
- **executor.py**: Módulo principal que coordena a execução das tarefas
- **actions.py**: Implementa as diferentes ações (click, texto, tecla, espera)
- **conditions.py**: Define condições e validações para execução
- **report.py**: Responsável pela geração de relatórios
- **utils.py**: Funções utilitárias compartilhadas

## Configuração de Posições
O arquivo `data/positions.json` deve conter um mapeamento de nomes para coordenadas:
```json
{
    "navegador_icone": {"x": 100, "y": 50},
    "barra_endereco": {"x": 400, "y": 100},
    "caixa_pesquisa": {"x": 500, "y": 200}
}
```

## Requisitos Técnicos Atendidos
- [x] Estruturas condicionais (if, elif, else) e laços de repetição (for)
- [x] Criação e uso de funções personalizadas
- [x] Leitura de arquivos CSV com pandas
- [x] Geração de relatórios em Excel com openpyxl
- [x] Uso do PyAutoGUI para automação
- [x] Captura de posições de elementos na tela
- [x] Arquitetura modular com separação de responsabilidades

## Dependências
- **pandas**: Manipulação de dados e arquivos CSV
- **openpyxl**: Geração de relatórios Excel
- **pyautogui**: Automação de mouse e teclado

## Observações
- Ajuste as posições no arquivo `data/positions.json` conforme a resolução da sua tela
- O projeto utiliza uma arquitetura modular para facilitar manutenção e extensão
- Teste sempre as posições capturadas antes de executar automações importantes
- O projeto é para fins didáticos e pode ser adaptado para outros fluxos de automação

## Solução de Problemas
- Verifique se todas as dependências estão instaladas corretamente
- Certifique-se de que as posições em `positions.json` estão corretas para sua tela
- Execute `tools/test_clicks.py` para verificar se os cliques estão funcionando
- Consulte os logs de erro no relatório gerado em `data/output/`