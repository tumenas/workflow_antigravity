<#
.SYNOPSIS
  Script de orquestração do projeto de artigo científico (Research Compendium - Economia/Finanças/Administração).
#>

param (
    [Parameter(Mandatory=$false)]
    [ValidateSet("all", "env", "analysis", "paper", "slides", "clean")]
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
    Write-Host "==> Atualizando pip e instalando dependencias..." -ForegroundColor Green
    & $PIP_BIN install --upgrade pip
    & $PIP_BIN install -r requirements.txt
}

function Run-Analysis {
    Write-Host "==> Executando pipeline empirica (src/00_master.py)..." -ForegroundColor Green
    if (-not (Test-Path $PYTHON_BIN)) {
        Write-Error "Ambiente virtual nao encontrado. Execute primeiro: .\run.ps1 env"
        return
    }
    & $PYTHON_BIN src/00_master.py
}

function Build-Paper {
    Write-Host "==> Compilando o manuscrito com Quarto..." -ForegroundColor Green
    if (-not (Get-Command quarto -ErrorAction SilentlyContinue)) {
        Write-Warning "Quarto CLI nao encontrado no sistema."
        return
    }
    quarto render manuscript/manuscript.qmd
}

function Build-Slides {
    Write-Host "==> Compilando apresentacao com Quarto..." -ForegroundColor Green
    if (-not (Get-Command quarto -ErrorAction SilentlyContinue)) {
        Write-Warning "Quarto CLI nao encontrado no sistema."
        return
    }
    quarto render presentations/slides.qmd
}

function Clean-Project {
    Write-Host "==> Limpando arquivos temporarios..." -ForegroundColor Green
    $targets = @(".quarto", "manuscript/manuscript_files", "manuscript/manuscript.pdf", "manuscript/manuscript.html")
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
    "slides" { Build-Slides }
    "clean" { Clean-Project }
    "all" {
        Setup-Environment
        Run-Analysis
        Build-Paper
    }
}
