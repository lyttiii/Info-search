<!DOCTYPE html>
<html> <head>
<title>Lab2.3</title>
</head> <body>

<?php
    const COLOR = "gray";
    const BORDER = 1;
    const PADDING = 5;
    
    print "<table border='" . BORDER . "' cellpadding='" . PADDING . "'>\n";
    
    $y = 1;
    while ($y <= 10) {
        print "<tr>\n";
        $x = 1;
        while ($x <= 10) {
            if ($x == $y) {
                print "\t<td bgcolor='" . COLOR . "'>";
            } else {
                print "\t<td>";
            } 
            print ($x * $y);
            print "</td>\n";
            $x++;
        }
        print "</tr>\n";
        $y++;
    }
    print "</table>";
?>
</body> </html>