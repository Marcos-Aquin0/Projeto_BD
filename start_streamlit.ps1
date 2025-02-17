# Ativar ambiente conda se estiver usando
conda activate myenv

# Definir o diretório de trabalho
$projectPath = "C:\Users\Marcos A. (Gelado)\Documents\python\Projeto_BD\Projeto_BD"
Set-Location -Path $projectPath

Write-Host "`nEndereços IP disponíveis:`n" -ForegroundColor Green

# IP Local (na rede)
Write-Host "IPs Locais:" -ForegroundColor Yellow
Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -match 'Ethernet|Wi-Fi' } | ForEach-Object {
    if ($_.InterfaceAlias -match 'Wi-Fi') {
        $wifiIP = $_.IPAddress
    }
    Write-Host "Interface $($_.InterfaceAlias): $($_.IPAddress)"
}

# IP Público (na internet)
Write-Host "`nIP Público:" -ForegroundColor Yellow
try {
    $publicIP = (Invoke-WebRequest -Uri "http://ifconfig.me/ip" -UseBasicParsing).Content
    Write-Host $publicIP
} catch {
    Write-Host "Não foi possível obter o IP público" -ForegroundColor Red
}

Write-Host "`nPara acessar o Streamlit:" -ForegroundColor Green
Write-Host "Local: http://localhost:8501"
Write-Host "Rede Local: http://SEU_IP_LOCAL:8501"
Write-Host "Internet: http://SEU_IP_PUBLICO:8501 (requer configuração do roteador)`n"

# Executar streamlit com configurações de rede
Write-Host "Iniciando Streamlit..."
Write-Host "O aplicativo estará disponível em:"
Write-Host "Local: http://localhost:8501"
Write-Host "Rede: http://${wifiIP}:8501"
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
