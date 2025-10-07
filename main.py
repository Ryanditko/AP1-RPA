from core import executar_tarefas

if __name__ == "__main__":
    print('Iniciando o executor de tarefas...')
    executar_tarefas(
        caminho_tarefas='data/tasks.csv',
        caminho_posicoes='data/positions.json',
        caminho_relatorio='data/output/report_execucao.xlsx'
    )