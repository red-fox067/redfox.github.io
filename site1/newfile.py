<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Detector de Firmware - Capitão Farofa</title>
    <style>
        body {
            background-color: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        #painel {
            border: 1px solid #00ff00;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 0 20px #00ff00;
            max-width: 90%;
        }
        h1 { font-size: 1.5em; margin-bottom: 20px; }
        #status { margin: 20px 0; font-size: 1em; min-height: 40px; }
        #btnRun {
            display: none; /* Escondido por padrão */
            background-color: #00ff00;
            color: #0a0a0a;
            border: none;
            padding: 12px 30px;
            font-weight: bold;
            font-family: 'Courier New', monospace;
            cursor: pointer;
            border-radius: 5px;
            font-size: 1.1em;
        }
        #btnRun:hover { background-color: #00cc00; }
        .erro { color: #ff3333 !important; }
        .sucesso { color: #00ff00 !important; }
    </style>
</head>
<body>
    <div id="painel">
        <h1>⚡ Detector de Firmware ⚡</h1>
        <p id="status">Iniciando verificação...</p>
        <button id="btnRun" onclick="irParaComando()">RUN</button>
    </div>

    <script>
        // Simulação de detecção de firmware
        // Na vida real, isso seria feito com código que lê o navegador do PS4
        // Aqui, a gente simula o resultado pra você entender a lógica

        var firmwareDetectado = "13.52"; // Pode mudar pra "11.00" ou "9.00" pra testar
        var firmwareSuportado = ["13.52", "13.50", "13.04", "13.02", "12.00", "11.00", "9.00"];
        
        var status = document.getElementById("status");
        var btnRun = document.getElementById("btnRun");

        function verificarFirmware() {
            status.innerText = "> Verificando firmware do console...";
            status.className = "";

            setTimeout(function() {
                status.innerText = "> Firmware detectado: " + firmwareDetectado;

                setTimeout(function() {
                    if (firmwareSuportado.includes(firmwareDetectado)) {
                        status.innerText = "> ✅ Firmware compatível! Botão RUN liberado.";
                        status.className = "sucesso";
                        btnRun.style.display = "inline-block";
                    } else {
                        status.innerText = "> ❌ Firmware " + firmwareDetectado + " NÃO é compatível. Atualize o host.";
                        status.className = "erro";
                        btnRun.style.display = "none";
                    }
                }, 1500);
            }, 1500);
        }

        function irParaComando() {
            // Redireciona para o Site 2 (o arquivo que executa o código)
            window.location.href = "pag2.html";
        }

        // Inicia a verificação automaticamente quando a página carrega
        window.onload = verificarFirmware;
    </script>
</body>
</html>