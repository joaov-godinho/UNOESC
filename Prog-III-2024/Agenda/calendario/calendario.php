<!DOCTYPE html>
<html>
<head>
    <title>Calendario Anual</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        .red {
            color: red;
        }
        .current-day {
            font-weight: bold; /* Deixa o texto em negrito */
        }
        .mes {
            margin-bottom: 20px;
        }
        .titulo-mes {
            font-weight: bold;
            font-size: 18px;
            text-align: center;
            padding: 10px 0;
            background: aqua;
        }
        .nome-dia {
            font-weight: bold;
            text-align: center;
            background: lightgray;
        }
    </style>
</head>
<body>
    <?php
    // Função para gerar as linhas do calendário
    function linha($semana) {
        $linha = '<tr>';
        foreach ($semana as $dia) {
            $class = ($dia === '') ? '' : '';
            $class .= ($dia !== '' && date('N', strtotime("2024-{$GLOBALS['mes']}-$dia")) == 7) ? ' red' : '';
            $currentDayClass = ($dia == date('j') && $GLOBALS['mes'] == date('n')) ? ' current-day' : '';
            $linha .= "<td class='$class$currentDayClass'>{$dia}</td>";
        }
        $linha .= '</tr>';
        return $linha;
    }

    // Função para gerar um calendário para um mês específico
    function calendarioMensal($mes) {
        $GLOBALS['mes'] = $mes;
        $calendario = '';

        $calendario .= '<table class="mes" border="1">';
        $calendario .= '<tr><td colspan="7" class="titulo-mes">' . date('F', strtotime("2024-$mes-01")) . '</td></tr>';
        $calendario .= '<tr class="nome-dia">';
        $calendario .= '<th>Seg</th><th>Ter</th><th>Qua</th><th>Qui</th><th>Sex</th><th>Sáb</th><th class="red">Dom</th>';
        $calendario .= '</tr>';

        $dia = 1;
        $semana = [];

        $primeiroDiaSemana = (date('N', strtotime("2024-$mes-01")) + 6) % 7;

        // Preenche a primeira semana do mês começando em 1
        for ($i = 0; $i < $primeiroDiaSemana; $i++) {
            array_push($semana, '');  // Preenche espaços vazios antes do primeiro dia do mês
        }
        //cal_days_in_month(CAL_GREGORIAN, $mes, 2024))calcula quantos dias tem o $mes de 2024
        //enquanto $dia for menor que os dias calculados para cada mes ela adiconara no calendario mensal
        while ($dia <= cal_days_in_month(CAL_GREGORIAN, $mes, 2024)) {
            array_push($semana, $dia);

            if (count($semana) == 7) {
                $calendario .= linha($semana);  // Adiciona uma linha de dias ao calendário
                $semana = [];
            }
            $dia++;
        }

        while (count($semana) < 7) {
            array_push($semana, '');  // Preenche espaços vazios restantes no final do mês
        }

        $calendario .= linha($semana);  // Adiciona a última linha de dias ao calendário
        $calendario .= '</table>';

        return $calendario;
    }

    // Loop para cada mês do ano e gera o calendário
    for ($mes = 1; $mes <= 12; $mes++) {
        echo calendarioMensal($mes);  // Gera e exibe o calendário para cada mês
    }
    ?>
</body>
</html>

