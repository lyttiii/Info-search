<html> 
<head>
    <meta charset="UTF-8">
    <title>Добавление в бд введенной информации</title> 
</head> 
<body>
    <?php

        function Add_to_database($name, $city, $address, $birthday, $mail, &$dberror) {  
            $user = "study";  
            $db = "study";
            $table = "notebook";
            $mysql_password = "123";


            $conn = mysqli_connect("localhost", $user, $mysql_password);
            if (!$conn) {
                $dberror = "Нет соединения с сервером";
                return false;
            }
            if (!mysqli_select_db($conn, $db)) {
                $dberror = mysqli_error($conn);
                mysqli_close($conn);
                return false;
            }
            $query = "INSERT INTO $table (name, city, address, birthday, mail) VALUES('$name', $city, $address, $birthday, '$mail')";
            if (!mysqli_query($conn, $query)) {
                $dberror = mysqli_error($conn);
                mysqli_close($conn);
                return false;
            }
            mysqli_close($conn);
            return true;
        }  

        function Write_form() {
            print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
            print "<p>Введите фамилию и имя [*]:";
            print "<input type='text' name='name'>\n";
            print "<p>Введите город:";
            print "<input type='text' name='city'>\n";
            print "<p>Введите адрес:";
            print "<input type='text' name='address'>\n";
            print "<p>Введите дату рождения в формате ГГГГ-ММ-ДД:";
            print "<input type='text' name='birthday'>\n";
            print "<p>Введите e-mail [*]:";
            print "<input type='text' name='mail'>\n";
            print "<p><input type='submit' value='Записать! '>\n
                </form>\n";
            print "<p>Поля, помеченные [*], являются обязательными для заполнения!";
        } 
        
        if (isset($_POST['name']) && isset($_POST['mail']) && $_POST['name'] != "" && $_POST['mail'] != "") { 
            $dberror = "";

            $city = !empty($_POST['city']) ? "'" . $_POST['city'] . "'" : "NULL";
            $address = !empty($_POST['address']) ? "'" . $_POST['address'] . "'" : "NULL";
            $birthday = !empty($_POST['birthday']) ? "'" . $_POST['birthday'] . "'" : "NULL";

            $ret = Add_to_database($_POST['name'], $city, $address, $birthday, $_POST['mail'], $dberror);

            if (!$ret) {
                echo "Ошибка: $dberror<br>";
            } else {
                echo "Ваши данные были записаны.";
            }
        } else {
            Write_form();
        }

    ?> 
</body>
</html>