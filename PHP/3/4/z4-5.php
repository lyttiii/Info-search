<?php

if (isset($_POST["site"]) && !empty($_POST["site"])) {
    $site = $_POST["site"];
    header("Location: http://" . $site);
    exit;
} else {

?>

<html> <head>
<title>Lab3.5</title> 
</head> <body>

<?php
print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";

$list_sites = array("www.yandex.ru", "www.rambler.ru", "www.google.com", "www.yahoo.com", "www.altavista.com");

print "<select name='site'>";
print "<option value = ''disabled selected>Поисковые системы:</option>";

foreach ($list_sites as $site) {
    print "<option value='$site'>$site</option>";
}

print "</select>";
?>

<input type="submit" value="Перейти">
</form>

<?php
     } 
?>
</body> </html>