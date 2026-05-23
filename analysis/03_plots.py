"""
Script 03: Geração de Figuras e Gráficos.
Lê os dados limpos de `data/processed/` e gera gráficos científicos de alta resolução.
Salva as figuras geradas em `results/figures/`.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminhos dos arquivos
PROCESSED_DATA_PATH = os.path.join("data", "processed", "dados_processados.csv")
FIGURES_DIR = os.path.join("results", "figures")

def configurar_estilo_cientifico():
    """Configura o Matplotlib/Seaborn para gerar gráficos profissionais."""
    # Usar tema limpo e adequado para artigos
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    plt.rcParams["font.family"] = "sans-serif"
    # Cores harmoniosas (Paleta de cores moderna e discreta)
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#0f4c81", "#f58220", "#32a852"])

def main():
    # 1. Carregar dados limpos
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Dados limpos não encontrados em {PROCESSED_DATA_PATH}. Rode o script 01_clean_data.py primeiro.")
        
    df = pd.read_csv(PROCESSED_DATA_PATH)
    print("Dados carregados com sucesso para geração de gráficos.")
    
    # Garantir que a pasta de figuras existe
    os.makedirs(FIGURES_DIR, exist_ok=True)
    
    # Configurar estilo
    configurar_estilo_cientifico()
    
    # 2. Criar Gráfico 1: Boxplot de Marcador Biológico por Grupo
    print("Gerando Boxplot (marcador_biologico por grupo)...")
    plt.figure(figsize=(8, 5))
    ax = sns.boxplot(x="grupo", y="marcador_biologico", data=df, palette="Set2")
    
    # Customizações estéticas
    plt.title("Distribuição do Marcador Biológico por Grupo de Tratamento", fontsize=14, weight="bold", pad=15)
    plt.xlabel("Grupo de Tratamento", fontsize=12)
    plt.ylabel("Nível do Marcador Biológico (u/mL)", fontsize=12)
    
    # Salvar em alta resolução (300 DPI) para impressão científica
    plot_1_path = os.path.join(FIGURES_DIR, "boxplot_marcador_grupo.png")
    plt.savefig(plot_1_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    # 3. Criar Gráfico 2: Dispersão com Regressão (Idade vs Pressão Arterial por Grupo)
    print("Gerando Scatter Plot com Regressão (idade vs pressao_arterial)...")
    
    # Usando o lmplot do Seaborn para retas de regressão por grupo
    g = sns.lmplot(
        x="idade", 
        y="pressao_arterial", 
        hue="grupo", 
        data=df, 
        palette="muted", 
        height=5, 
        aspect=1.4,
        legend=False
    )
    
    # Customizações
    plt.title("Relação entre Idade e Pressão Arterial por Grupo", fontsize=14, weight="bold", pad=15)
    plt.xlabel("Idade (anos)", fontsize=12)
    plt.ylabel("Pressão Arterial Sistólica (mmHg)", fontsize=12)
    
    # Legenda elegante
    plt.legend(title="Grupo", bbox_to_anchor=(1.05, 1), loc="upper left")
    
    # Salvar em alta resolução (300 DPI)
    plot_2_path = os.path.join(FIGURES_DIR, "dispersao_pressao_idade.png")
    g.savefig(plot_2_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"Gráficos salvos com sucesso em: {FIGURES_DIR}")

if __name__ == "__main__":
    main()
