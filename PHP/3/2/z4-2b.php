<html>
<head>
    <title>Lab3.2</title>
</head>
<body>

<?php

const SIZE = 100;

if (isset($_GET['align'])) {
    $align = $_GET['align'];
} else {
    $align = "left";
}

if (isset($_GET['valign'])) {
    $valign_arr = $_GET['valign'];
    if (count($valign_arr) > 1){
        print "<p>Ошибка, выбрано более одного значения у вертикального расположения</p>";
        print "<p><a href='z4-2b.php'>Назад</a></p>";
        exit;
    }
    elseif (count($valign_arr) == 1){
        $valign = $valign_arr[0];
    }
} else {
    $valign = "top";
}

print "<table border='1'><tr>";
print "<td width='". SIZE . "' height='". SIZE . "' align='" . htmlspecialchars($align) . "' valign='" . htmlspecialchars($valign) . "'>";
print "Текст";
print "</td></tr></table>";
print "<form action='{$_SERVER['PHP_SELF']}' method='GET'>";
?>
<h3>Выберите горизонтальное расположение:</h3>
<p><label><input type="radio" name="align" value="left"></label>Слева</p>
<p><label><input type="radio" name="align" value="center"></label>По центру</p>
<p><label><input type="radio" name="align" value="right"></label>Справа</p>

<h3>Выберите вертикальное расположение:</h3>
<p><label><input type="checkbox" name="valign[]" value="top"></label>Сверху</p>
<p><label><input type="checkbox" name="valign[]" value="middle"></label>Посередине</p>
<p><label><input type="checkbox" name="valign[]" value="bottom"></label>Внизу</p>

<p><input type="submit" value="Выполнить"></p>
</form>
</body>
</html>