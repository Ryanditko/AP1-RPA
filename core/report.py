import pandas as pd
from datetime import datetime


def gerar_relatorio(resultados, caminho_saida, tempo_total):

    df = pd.DataFrame(resultados)
    resumo = {
        "Data de Execução": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Total de Tarefas": len(df),
        "Tempo Total (s)": round(tempo_total, 2),
        "Sucessos": (df["Status"] == "SUCESSO").sum(),
        "Falhas": (df["Status"] == "FALHA").sum()
    }

    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Detalhes", index=False)
        pd.DataFrame([resumo]).to_excel(writer, sheet_name="Resumo", index=False)