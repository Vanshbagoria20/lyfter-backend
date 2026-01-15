Param(
    [string]$venvPath = ".venv"
)

if (-not (Test-Path "$venvPath")) {
    python -m venv $venvPath
}

"$venvPath\Scripts\python.exe" -m pip install --upgrade pip
"$venvPath\Scripts\python.exe" -m pip install -r requirements.txt
Write-Host "Installed requirements into $venvPath"
