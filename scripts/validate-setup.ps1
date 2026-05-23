# =============================================================================
# validate-setup.ps1 — Verifica as dependências do fluxo de trabalho acadêmico no Windows
#
# Execute este script para confirmar se o seu ambiente possui as ferramentas instaladas.
# =============================================================================

$OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "Validação do Ambiente Acadêmico"

Write-Host ""
Write-Host "Validando o Fluxo de Trabalho Acadêmico com Claude Code..." -ForegroundColor Cyan -Style Bold
Write-Host ""

$pass = 0
$warn = 0
$fail = 0

function Test-Command {
    param (
        [string]$Name,
        [string]$Cmd,
        [string]$InstallUrl,
        [bool]$Required = $true
    )

    $path = Get-Command $Cmd -ErrorAction SilentlyContinue
    if ($path) {
        # Tenta rodar com --version para exibir a versão instalada
        $version = ""
        try {
            if ($Cmd -eq "python3" -or $Cmd -eq "python") {
                $version = & $Cmd --version 2>&1 | Select-Object -First 1
            } else {
                $version = & $Cmd --version 2>&1 | Select-Object -First 1
            }
            $version = $version.ToString().Trim()
        } catch {
            $version = "instalado"
        }
        
        Write-Host "  [✓] $Name encontrado: $version" -ForegroundColor Green
        $script:pass++
        return $true
    } else {
        if ($Required) {
            Write-Host "  [✗] $Name NÃO ENCONTRADO — instale em: $InstallUrl" -ForegroundColor Red
            $script:fail++
        } else {
            Write-Host "  [!] $Name não encontrado (opcional) — instale em: $InstallUrl" -ForegroundColor Yellow
            $script:warn++
        }
        return $false
    }
}

Write-Host "Ferramentas Obrigatórias:" -Style Bold
$hasClaude = Test-Command "Claude Code CLI" "claude" "https://claude.ai/install" -Required $true
$hasQuarto = Test-Command "Quarto CLI" "quarto" "https://quarto.org/docs/get-started/" -Required $true
$hasGit = Test-Command "Git" "git" "https://git-scm.com/downloads" -Required $true

# Trata python no Windows que pode ser 'python' ou 'python3'
$pythonCmd = "python"
if (Get-Command "python3" -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
}
$hasPython = Test-Command "Python 3" $pythonCmd "https://python.org" -Required $true
Write-Host ""

Write-Host "Ferramentas Recomendadas (Opcionais):" -Style Bold
$hasR = Test-Command "R Language" "R" "https://www.r-project.org/" -Required $false
$hasXeLaTeX = Test-Command "XeLaTeX (LaTeX)" "xelatex" "https://tug.org/texlive/" -Required $false
$hasGitHubCLI = Test-Command "GitHub CLI" "gh" "https://cli.github.com/" -Required $false
Write-Host ""

Write-Host "Configuração do Git:" -Style Bold
if ($hasGit) {
    $gitName = git config user.name 2>$null
    $gitEmail = git config user.email 2>$null
    if ($gitName -and $gitEmail) {
        Write-Host "  [✓] Usuário Git configurado: $gitName <$gitEmail>" -ForegroundColor Green
        $pass++
    } else {
        Write-Host "  [!] Nome ou Email do Git não configurados" -ForegroundColor Yellow
        Write-Host "      Execute: git config --global user.name `"Seu Nome`"" -ForegroundColor Gray
        Write-Host "      Execute: git config --global user.email `"seu-email@exemplo.com`"" -ForegroundColor Gray
        $warn++
    }
} else {
    Write-Host "  [!] Pulado (Git não instalado)." -ForegroundColor Yellow
    $warn++
}
Write-Host ""

Write-Host "Status dos Hooks do Claude Code:" -Style Bold
if (Test-Path ".claude/hooks") {
    Write-Host "  [✓] Pasta .claude/hooks/ detectada." -ForegroundColor Green
    $pass++
} else {
    Write-Host "  [!] Pasta .claude/hooks/ não encontrada na raiz." -ForegroundColor Yellow
    $warn++
}
Write-Host ""

Write-Host "Resumo: $pass passados, $warn avisos, $fail falhas" -ForegroundColor (If ($fail -gt 0) { "Red" } ElseIf ($warn -gt 0) { "Yellow" } Else { "Green" })
Write-Host ""

if ($fail -gt 0) {
    Write-Host "Algumas ferramentas obrigatórias estão ausentes." -ForegroundColor Red
    Write-Host "Por favor, instale as ferramentas indicadas acima com [✗] e execute este script novamente."
    exit 1
} else {
    Write-Host "Tudo pronto! Próximos passos:" -ForegroundColor Green
    Write-Host "  1. Abra o Claude Code na pasta do projeto:  claude"
    Write-Host "  2. Teste o manuscrito rodando no chat:      /qa-quarto"
    Write-Host "  3. Peça uma revisão científica do artigo:    /review-paper"
    Write-Host ""
    exit 0
}
