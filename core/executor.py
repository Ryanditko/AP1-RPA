import pandas as pd
import time
from datetime import datetime
import traceback
from core import carregar_posicoes, gerar_relatorio, clicar, digitar_texto, pressionar_tecla, esperar, rolar_tela, avaliar_condicao

def executar_tarefas(caminho_tarefas, caminho_posicoes, caminho_relatorio):
    
    posicoes = carregar_posicoes(caminho_posicoes)
    tarefas = pd.read_csv(caminho_tarefas)
    resultados = []
    ultimo_sucesso = True

    inicio_total = datetime.now()

    for i, linha in tarefas.iterrows():
        nome = linha.get('Tarefa', f'tarefa_{i}')
        tipo = str(linha.get('Tipo', '')).strip().lower()
        dado = linha.get('Dado', '')
        cond = linha.get('Condicional', '')
        nota = linha.get('Nota', '')
        inicio = datetime.now()

        status = False
        mensagem = ''
        tempo_exec = 0

        try:
            if not avaliar_condicao(cond, ultimo_sucesso):
                mensagem = f'Tarefa ignorada por condição: {cond}'
                print(f'[IGNORADO] {nome}')
            else:
                print(f'[EXECUTANDO] {nome} (tipo={tipo})')

                if tipo == 'click':
                    status, mensagem = clicar(dado, posicoes)
                elif tipo == 'texto':
                    status, mensagem = digitar_texto(dado)
                elif tipo == 'tecla':
                    status, mensagem = pressionar_tecla(dado)
                elif tipo == 'espera':
                    status, mensagem = esperar(dado)
                elif tipo == 'scroll':
                    status, mensagem = rolar_tela(dado)
                else:
                    mensagem = f'Tipo de tarefa desconhecido: {tipo}'

            tempo_exec = (datetime.now() - inicio).total_seconds()

        except Exception as e:
            mensagem = f'Erro: {e}\n{traceback.format_exc()}'
            tempo_exec = (datetime.now() - inicio).total_seconds()

        ultimo_sucesso = status

        resultados.append({
            'Tarefa': nome,
            'Tipo': tipo,
            'Dado': str(dado),
            'Condicional': str(cond),
            'Status': 'SUCESSO' if status else 'FALHA',
            'Mensagem': mensagem,
            'Tempo': round(tempo_exec, 2)
        })

        time.sleep(0.3)
    
    tempo_total = (datetime.now() - inicio_total).total_seconds()
    gerar_relatorio(resultados, caminho_relatorio, tempo_total)
    print(f'\nExecução concluída. Relatório salvo em: {caminho_relatorio}')