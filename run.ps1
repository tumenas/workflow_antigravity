<#
.SYNOPSIS
  Script de orquestração do projeto de artigo científico (Research Compendium).
.DESCRIPTION
  Permite configurar o ambiente virtual, rodar scripts Python e compilar o manuscrito Quarto no Windows.
.EXAMPLE
  .\run.ps1 env
.EXAMPLE
  .\run.ps1 analysis
.EXAMPLE
  .\run.ps1 paper
.EXAMPLE
  .\run.ps1 all
#>

param (
    [Parameter(Mandatory=$false)]
    [ValidateSet("all", "env", "analysis", "paper", "clean")]
    [string]$Task = "all"
)

$VENV_DIR = ".venv"
$PYTHON_BIN = "$VENV_DIR\Scripts\python.exe"
$PIP_BIN = "$VENV_DIR\Scripts\pip.exe"

function Setup-Environment {
    Write-Host "==> Criando ambiente virtual Python..." -ForegroundColor Green
    if (-not (Test-Path $VENV_DIR)) {
        python -m venv $VENV_DIR
    }
    Write-Host "==> Atualizando pip e instalando dependências..." -ForegroundColor Green
    & $PIP_BIN install --upgrade pip
    & $PIP_BIN install -r requirements.txt
}

function Run-Analysis {
    Write-Host "==> Executando scripts de análise..." -ForegroundColor Green
    if (-not (Test-Path $PYTHON_BIN)) {
        Write-Error "Ambiente virtual não encontrado. Execute primeiro: .\run.ps1 env"
        return
    }
    Write-Host "-> Executando 01_clean_data.py..." -ForegroundColor Blue
    & $PYTHON_BIN analysis/01_clean_data.py
    
    Write-Host "-> Executando 02_analysis.py..." -ForegroundColor Blue
    & $PYTHON_BIN analysis/02_analysis.py
    
    Write-Host "-> Executando 03_plots.py..." -ForegroundColor Blue
    & $PYTHON_BIN analysis/03_plots.py
}

function Build-Paper {
    Write-Host "==> Compilando o manuscrito com Quarto..." -ForegroundColor Green
    if (-not (Get-Command quarto -ErrorAction SilentlyContinue)) {
        Write-Warning "Quarto CLI não encontrado no sistema. Por favor, instale o Quarto (https://quarto.org/)."
        return
    }
    quarto render manuscript/manuscript.qmd
}

function Clean-Project {
    Write-Host "==> Limpando arquivos temporários..." -ForegroundColor Green
    $targets = @(
        ".quarto",
        "manuscript/manuscript_files",
        "manuscript/manuscript.pdf",
        "manuscript/manuscript.html",
        "manuscript/manuscript.docx",
        "results/figures/exemplo_grafico.png",
        "data/processed/dados_processados.csv"
    )
    foreach ($target in $targets) {
        if (Test-Path $target) {
            Remove-Item -Recurse -Force $target
            Write-Host "Removido: $target" -ForegroundColor Yellow
        }
    }
}

switch ($Task) {
    "env" { Setup-Environment }
    "analysis" { Run-Analysis }
    "paper" { Build-Paper }
    "clean" { Clean-Project }
    "all" {
        Setup-Environment
        Run-Analysis
        Build-Paper
    }
}
