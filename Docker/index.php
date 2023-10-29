<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Básica</title>
</head>
<body>
    <h1>Calculadora Básica</h1>
    <form method="post">
        <input type="text" name="num1" placeholder="Número 1" required>
        <select name="operation">
            <option value="add">Sumar (+)</option>
            <option value="subtract">Restar (-)</option>
            <option value="multiply">Multiplicar (*)</option>
            <option value="divide">Dividir (/)</option>
        </select>
        <input type="text" name="num2" placeholder="Número 2" required>
        <input type="submit" value="Calcular">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = $_POST["num1"];
        $num2 = $_POST["num2"];
        $operation = $_POST["operation"];

        if (!is_numeric($num1) || !is_numeric($num2)) {
            echo "Por favor, ingresa números válidos.";
        } else {
            switch ($operation) {
                case "add":
                    $result = $num1 + $num2;
                    break;
                case "subtract":
                    $result = $num1 - $num2;
                    break;
                case "multiply":
                    $result = $num1 * $num2;
                    break;
                case "divide":
                    if ($num2 == 0) {
                        echo "No es posible dividir por cero.";
                    } else {
                        $result = $num1 / $num2;
                    }
                    break;
                default:
                    echo "Operación no válida.";
                    break;
            }
            echo "Resultado: $result";
        }
    }
    ?>
</body>
</html>
