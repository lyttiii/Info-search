<?php
$mysql_user = "study";
$mysql_password = "123";

$conn = mysqli_connect("localhost", $mysql_user, $mysql_password); 
if (!$conn) {
    exit("Нет соединения с базой данных.");
}

$database = "study";
if (!mysqli_select_db($conn, $database)) {
    print "Невозможно открыть $database";
    mysqli_close($conn);
    exit;
} 

$new_table_name = "notebook";

$query = "DROP TABLE IF EXISTS $new_table_name";
mysqli_query($conn, $query); 

$query = "CREATE TABLE $new_table_name (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(50),
    city varchar(50),
    address varchar(50),
    birthday date,
    mail varchar(20),
    PRIMARY KEY(id)
)";

$result = mysqli_query($conn, $query);

if (!$result) {
    print "Нельзя создать таблицу $new_table_name";
    mysqli_close($conn);
    exit;
} else { 
    print "Таблица $new_table_name создана удачно!";
}

mysqli_close($conn);
?>
