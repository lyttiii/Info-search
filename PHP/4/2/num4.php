<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Редактирование таблицы</title>
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


if (isset($_POST['id'], $_POST['field_name'], $_POST['field_value'])) {
    $id = intval($_POST['id']);
    $field_name = $_POST['field_name'];
    $field_value = mysqli_real_escape_string($conn, $_POST['field_value']);

    $query = "UPDATE `$table` SET `$field_name`='$field_value' WHERE id=$id";
    if (mysqli_query($conn, $query)) {
        print "Обновление прошло успешно<br>";
        print "<a href='num3.php'>Посмотреть результат</a>";
    } else {
        print "Ошибка обновления";
    }
}

else if (isset($_POST['id'])) {
    $id = intval($_POST['id']);
    $result = mysqli_query($conn, "SELECT * FROM `$table` WHERE id=$id");
    if ($a_row_assoc = mysqli_fetch_assoc($result)) {
        $fields = array_keys($a_row_assoc);
        print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
        print "<input type='hidden' name='id' value='$id'>";
        print "<select name='field_name'>";
        foreach ($fields as $field) {
            if ($field === 'id') continue; // id не редактируем
            $value = htmlspecialchars($a_row_assoc[$field]);
            print "<option value='$field'>$field: $value</option>";
        }
        print "</select>";
        print " <input type='text' name='field_value' placeholder='Новое значение'>";
        print " <input type='submit' value='Заменить'>";
        print "</form>";
    }
}
else {
    $result = mysqli_query($conn, "SELECT * FROM `$table`");
    $num_fields = mysqli_num_fields($result);

    print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
    print "<table border='1'>";
    print "<tr>";
    for ($i=0; $i<$num_fields; $i++) {
        $col = mysqli_fetch_field_direct($result, $i)->name;
        print "<th>$col</th>";
    }
    print "<th>Выбрать для редактирования</th>";
    print "</tr>";

    while ($a_row = mysqli_fetch_assoc($result)) {
        print "<tr>";
        foreach ($a_row as $value) {
            print "<td>" . htmlspecialchars($value) . "</td>";
        }
        print "<td><input type='radio' name='id' value='" . $a_row['id'] . "'></td>";
        print "</tr>";
    }

    print "</table>";
    print "<p><input type='submit' value='Редактировать выбранную строку'></p>";
    print "</form>";
}

mysqli_close($conn);
?>
</body>
</html>
