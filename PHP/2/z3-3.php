<!DOCTYPE html>
<html>
<head>
    <title>Lab2.5</title>
</head>
<body>

<?php
    function Ru($color) {
        print "<p style=\"color: $color;\">Здравствуйте!</p>";
    }
    function En($color) {
        print "<p style=\"color: $color;\">Hello!</p>";
    }
    function Fr($color) {
        print "<p style=\"color: $color;\">Bonjour!</p>";
    }
    function De($color) {
        print "<p style=\"color: $color;\">Guten Tag!</p>";
    }

    $lang = $_GET["lang"];
    $color = $_GET["color"];

    if ($lang === 'Ru') {
        Ru($color);
    } elseif ($lang === 'En') {
        En($color);
    } elseif ($lang === 'Fr') {
        Fr($color);
    } elseif ($lang === 'De') {
        De($color);
    } else {
        print "<p style=\"color: red;\">Ошибка, неизвестный язык!</p>";
    }
?>
</body>
</html>

