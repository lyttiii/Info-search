<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Lab3.1</title>
</head>
<body>

<?php
const SIZE = 100;

$align = $_GET['align'] ?? null;
$valign = $_GET['valign'] ?? null;

$errors = [];
if (!$align) $errors[] = "горизонтальное положение не выбрано";
if (!$valign) $errors[] = "вертикальное положение не выбрано";

if ($errors) {
    print "Ошибка: " . implode(" и ", $errors) . ".";
} else {
    print "<table border='1'><tr>";
    print "<td width='". SIZE . "' height='". SIZE . "' align='" . htmlspecialchars($align) . "' valign='" . htmlspecialchars($valign) . "'>";
    print "Текст</td></tr></table>";
}

print "<p><a href='z4-1a.html'>Назад</a></p>";
?>

</body>
</html>