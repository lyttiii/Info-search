<!DOCTYPE html>
<html>
<head>
    <title>Lab2.2</title>
</head>
<body>
    <?php
        $lang = $_GET["lang"];

        if ($lang == "ru") {
            print "Русский";
        } elseif ($lang == "en") {
            print "Английский";
        } elseif ($lang == "de") {
            print "Немецкий";
        } elseif ($lang == "fr") {
            print "Французский";
        } else {
            print "Ошибка, неизвестный язык.";
        }

    ?>
</body>
</html>