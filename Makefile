# Makefile para orquestração do Research Compendium
# Executa a pipeline de dados e compila o manuscrito.
#
# Comandos principais:
#   make env       - Cria ambiente virtual e instala dependências
#   make analysis  - Executa toda a sequência de scripts Python
#   make paper     - Compila o manuscrito Quarto para PDF/HTML
#   make clean     - Remove arquivos temporários e compilados
#   make all       - Executa todos os passos (ambiente, análise, manuscrito)

.PHONY: all env analysis paper clean

# Interpretadores do ambiente virtual (compatível com Windows/PowerShell)
PYTHON = .venv/Scripts/python.exe
PIP = .venv/Scripts/pip.exe

all: env analysis paper

env:
	python -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

analysis:
	$(PYTHON) analysis/01_clean_data.py
	$(PYTHON) analysis/02_analysis.py
	$(PYTHON) analysis/03_plots.py

paper:
	quarto render manuscript/manuscript.qmd

clean:
	@echo Limpando arquivos temporarios...
	@if exist .quarto rmdir /s /q .quarto
	@if exist manuscript\manuscript_files rmdir /s /q manuscript\manuscript_files
	@if exist manuscript\manuscript.pdf del /q /f manuscript\manuscript.pdf
	@if exist manuscript\manuscript.html del /q /f manuscript\manuscript.html
