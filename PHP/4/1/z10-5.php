<?php

    function vid_structure($table_name, $conn) {
        print "<h4>Структура таблицы $table_name</h4>\n";
        $query_res = mysqli_query($conn,"SELECT * FROM $table_name");
        $num_fields = mysqli_num_fields($query_res);
        print "<dl><dd>\n";
        for ($x=0; $x < $num_fields; $x++)
        {  
            $properties = mysqli_fetch_field_direct($query_res, $x);
            print "<i>";
            print $properties->type;
            // тип поля
            print "</i> <i>";
            print $properties->length;
            // максимальная длина поля
            print "</i> <b>";
            print $properties->name;
            // имя поля
            print "</b> <i>";
            print $properties->flags;
            // флаги поля 
            print "</i><br>\n";
        }  #2
        print "</dl>\n";
    }

    function vid_content($table_name, $conn) {
        $result = mysqli_query($conn, "SELECT * FROM $table_name");
        $num_fields = mysqli_num_fields($result);
        $rus_names = array(
            "snum" => "Номер продавца",
            "sname" => "Имя продавца",
            "city" => "Город",
            "comm" => "Комиссионные продавца",
            "cnum" => "Номер покупателя",
            "cname" => "Имя покупателя",
            "rating" => "Рейтинг покупателя",
            "onum" => "Номер заказа",
            "amt" => "Сумма заказа",
            "odate" => "Дата заказа"    
        );

        print "<h4>Содержимое таблицы $table_name</h4>\n";
        print "<p><table border=\"1\";>\n";
        print "<tr>\n";
        for ($x = 0; $x < $num_fields; $x++) {
            $name = mysqli_fetch_field_direct($result, $x)->name;
            print "\t<th>$rus_names[$name]<br>$name</th>\n";
        }
        print "</tr>\n";
        while ($a_row = mysqli_fetch_row($result)) {    
            print "<tr>\n";
            foreach ($a_row as $field) 
                print "\t<td>$field</td>\n";
            print "</tr>\n";
        }
        print "</table>\n";
    }


    $tab_res = mysqli_query($conn, "SHOW TABLES");
    $structure = isset($_GET["structure"]) ? $_GET["structure"] : [];
    $content   = isset($_GET["content"]) ? $_GET["content"] : [];

    while ($tables_names = mysqli_fetch_row($tab_res)) {
        $table_name = $tables_names[0];
        
        if (count($structure) != 0 && in_array($table_name, $structure)) {
            vid_structure($table_name, $conn);
        }

        if (count($content) != 0 && in_array($table_name, $content)) {
            vid_content($table_name, $conn);
        }
    }
    print "<p><a href=\"z10-1.html\">Возврат к выбору таблицы</a>"
?>