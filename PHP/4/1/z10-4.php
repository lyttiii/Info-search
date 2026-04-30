<?php
    $username = "lyttiii";
    $password = "hello12345";
    $database = "sample";
    $hostname = "localhost";
    $conn = mysqli_connect($hostname, $username, $password, $database);

    if (!$conn) {
        die("Нет соединения с базой данных.");
    }
?>
