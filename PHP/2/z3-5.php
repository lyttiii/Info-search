<!DOCTYPE html>
<html>
<head>
    <title>Lab2.6</title>
</head>
<body>
    <?php
        function print_arr($array) {
            foreach($array as $ind) {
                print "$ind  ";
            }
        }
        
        print("treug: <br>");
        $treug = array();
        for ($n = 1; $n <= 10; $n++) {
            $treug[] = ($n * ($n + 1) / 2);
        }
        print_arr($treug);

        print" <br> kvd: <br>";
        $kvd = array();
        for ($n = 1; $n <= 10; ++$n) {
            $kvd[] = $n * $n;
        }
        print_arr($kvd);

        print" <br> rez: <br>";
        $rez = array_merge($treug, $kvd);
        print_arr($rez);

        print" <br> sort rez: <br>";
        sort($rez);
        print_arr($rez);

        print" <br> shift rez: <br>";
        array_shift($rez);
        print_arr($rez);

        print" <br> unique rez: <br>";
        $rez1 = array_unique($rez);
        print_arr($rez1);

    ?>
</body>
</html>