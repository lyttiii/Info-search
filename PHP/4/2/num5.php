<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Добавление записей</title>
</head>
<body>
<?php
$user = "study";  
$mysql_password = "123";
$db = "study";
$table = "notebook";

$conn = mysqli_connect("localhost", $user, $mysql_password);
if (!$conn) {
    print "Нет соединения с сервером";
    exit;
}

if (!mysqli_select_db($conn, $db)) {
    print "Не удалось открыть базу данных $db";
    mysqli_close($conn);
    exit;
}

$query = "INSERT INTO `$table` (name, city, address, birthday, mail) VALUES
    ('Алексей', 'Москва', 'Ленинский проспект 12', '1990-05-15', 'alex90@mail.ru'),
    ('Марина', 'Санкт-Петербург', 'Невский проспект 45', '1985-11-30', 'marina85@gmail.com'),
    ('Дмитрий', 'Казань', 'Баумана 7', '2000-07-08', 'dmitry00@yandex.ru')";

if (!mysqli_query($conn, $query)) {
    print "Ошибка при вставке данных";
    mysqli_close($conn);
    exit;
}

print "Три записи успешно добавлены в таблицу!";

mysqli_close($conn);
?>
</body>
</html>
