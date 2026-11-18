"""
Funções utilitárias compartilhadas pela pipeline empírica.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def winsorize_series(series: pd.Series, lower: float = 0.01, upper: float = 0.99) -> pd.Series:
    """Winsoriza uma série numérica nos quantis especificados."""
    q_low = series.quantile(lower)
    q_high = series.quantile(upper)
    return series.clip(lower=q_low, upper=q_high)


def configure_plot_style() -> None:
    """Configura estilo limpo e padronizado para gráficos científicos."""
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#0f4c81", "#f58220", "#32a852", "#8c564b"])
