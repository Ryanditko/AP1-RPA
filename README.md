# automacao_RPA

Automação simples de tarefas de interface usando Python e PyAutoGUI.

## Visão geral

Este projeto executa uma sequência de ações (cliques, digitação, pressionamento de teclas, esperas e rolagens) definidas em um arquivo CSV (`data/tasks.csv`) e usa um arquivo JSON (`data/positions.json`) para mapear nomes de posições a coordenadas na tela. Ao final da execução é gerado um relatório em formato Excel com os resultados.

O executor principal está em `main.py` e a lógica de ação e execução está no pacote `core/`.

## Pré-requisitos

- Python 3.8+
- Dependências listadas em `requirements.txt` (ex.: pandas, openpyxl, pyautogui, pillow)

Instale as dependências com:

```powershell
pip install -r requirements.txt
```

> Nota: `pyautogui` pode requerer configuração adicional no seu sistema (permissões de acessibilidade no macOS, por exemplo). No Windows, execute scripts responsáveis por interagir com a tela com cuidado.

## Estrutura do projeto

- `main.py` — Ponto de entrada que chama o executor de tarefas.
- `requirements.txt` — Dependências do projeto.
- `data/` — Dados de entrada e posições:
	- `tasks.csv` — Arquivo com as tarefas a executar.
	- `positions.json` — Mapeamento nome -> [x, y].
- `core/` — Módulos principais: carregamento de posições, ações (click, texto, tecla, espera, scroll), executor e utilitários.
- `output/` — Pasta recomendada para arquivos gerados (está no `.gitignore`).
- `tools/` — Scripts auxiliares (captura de posições, testes).
- `docs/` — Documentação (instruções da atividade).

## Formato de `data/tasks.csv`

O CSV deve conter as colunas (nomes exatos esperados):

- `Tarefa` — nome legível da tarefa (opcional).
- `Tipo` — tipo da ação: `click`, `texto`, `tecla`, `espera`, `scroll`.
- `Dado` — dado necessário para a ação. Exemplos:
	- `click`: nome da posição (ex.: `botao_salvar`) ou coordenada no formato `x,y` (ex.: `100,200`).
	- `texto`: texto a ser digitado.
	- `tecla`: tecla única (`enter`, `tab`) ou combinação com `+` (`ctrl+s`).
	- `espera`: número de segundos (ex.: `2.5`).
	- `scroll`: quantidade em unidades (ex.: `-500`).
- `Condicional` — expressão simples para condicionar a execução (o executor suporta lógica básica ligada ao último status de execução). Pode ficar vazia.
- `Nota` — campo livre para comentários.

Exemplo de arquivo CSV:

```csv
Tarefa,Tipo,Dado,Condicional,Nota
Abrir menu,click,menu_principal,,clicar no menu principal
Esperar,espera,1,,aguardar animação
Digitar busca,texto,exemplo de pesquisa,,
Salvar,tecla,ctrl+s,,salvar arquivo
```

## Formato de `data/positions.json`

Arquivo JSON simples com pares nome -> [x, y]. Exemplo:

```json
{
	"menu_principal": [100, 50],
	"botao_salvar": [1200, 800]
}
```

## Como executar

No terminal (PowerShell):

```powershell
python main.py
```

`main.py` chama `executar_tarefas` com os caminhos padrões apontando para `data/tasks.csv` e `data/positions.json`. Você pode modificar `main.py` para alterar caminhos ou chamar `executar_tarefas` diretamente em outro script.

## Segurança e boas práticas

- Teste em uma área controlada antes de rodar automações que podem clicar/teclar em aplicações críticas.
- Considere usar uma máquina/VM de teste.
- Não versionar arquivos de ambiente com segredos (adicione `.env` ao `.gitignore` se usar variáveis de ambiente locais).

## Contribuindo

Issues e pull requests são bem-vindos. Para contribuições menores, descreva o objetivo e abra um PR com testes ou uma demonstração simples.