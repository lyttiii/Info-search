<!DOCTYPE html>
<html> <head>
<title>Lab2.4</title>
</head> <body>

<?php
    const COLOR_LINE = "blue";
    const COLOR_PLUS = "red";
    const BORDER = 1;
    const PADDING = 5;
    
    print "<table border='" . BORDER . "' cellpadding='" . PADDING . "'>\n";
    
    for ($y = 0; $y <= 10; $y++)
    {
        print "<tr>\n";
        for ($x = 0; $x <= 10; $x++)
        {
            if ($x == 0 && $y == 0) {
                print "\t<td style='color:" . COLOR_PLUS . "'>+</td>\n";
            }
            elseif ($y == 0 && $x > 0) {
                print "\t<td style='color:" . COLOR_LINE . "'>" . $x . "</td>\n";
            }
            elseif ($x == 0 && $y > 0) {
                print "\t<td style='color:" . COLOR_LINE . "'>" . $y . "</td>\n";
            }
            else {
                $sum = $x + $y;
                print "\t<td>" . $sum . "</td>\n";
            }
        }
        print "</tr>\n";
    }
    print "</table>";
?>
</body> </html>