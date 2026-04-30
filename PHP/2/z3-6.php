<!DOCTYPE html>
<html>
<head>
    <title>Lab2.7</title>
</head>
<body>
    <?php
        $cust = array(
            'cnum' => 2001,
            'cname' => "Hoffman",
            'city' => "London",
            'snum' => 1001,
            'rating' => 100
        );

        print "<b>cust:</b> <br>";    
        foreach ($cust as $key=>$value) {
            print "$key = $value <br>";
        }

        asort($cust);
        print "<br> <b>cust asort:</b> <br>";    
        foreach ($cust as $key=>$value) {
            print "$key = $value <br>";
        }
        
        ksort($cust);
        print "<br> <b>cust ksort:</b> <br>";    
        foreach ($cust as $key=>$value) {
            print "$key = $value <br>";
        }

        sort($cust);
        print "<br> <b>cust sort:</b> <br>";    
        foreach ($cust as $key=>$value) {
            print "$key = $value <br>";
        }
    ?>
</body>
</html>