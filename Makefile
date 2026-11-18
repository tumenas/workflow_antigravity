.PHONY: all env analysis paper slides clean

PYTHON = .venv/Scripts/python.exe
PIP = .venv/Scripts/pip.exe

all: env analysis paper

env:
	python -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

analysis:
	$(PYTHON) src/00_master.py

paper:
	quarto render manuscript/manuscript.qmd

slides:
	quarto render presentations/slides.qmd

clean:
	@echo Limpando arquivos temporarios...
	@if exist .quarto rmdir /s /q .quarto
	@if exist manuscript\manuscript_files rmdir /s /q manuscript\manuscript_files
