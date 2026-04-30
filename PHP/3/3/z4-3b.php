<html> 
    <head>
        <title>Lab3.3</title>
    </head> 
    <body>
        <?php
            function countCorrectAnswers($otv, $userAnswers) {
                $result = 0;
                for ($i = 0; $i < 9; $i++) {
                    if ($userAnswers[$i] != '') {         
                        if ($otv[$i] == $userAnswers[$i]) {
                            $result += 1;
                        }
                    }
                }
                return $result;
            }

            function getResultMessage($name, $correctCount) {
                $namePrefix = (!empty($name)) ? $name . ", вы " : "Вы ";
                
                switch ($correctCount) {
                    case 9: 
                        $message = "великолепно знаете географию"; 
                        break;
                    case 8: 
                        $message = "отлично знаете географию"; 
                        break;
                    case 7: 
                        $message = "очень хорошо знаете географию"; 
                        break;
                    case 6:
                        $message = "хорошо знаете географию";
                        break;
                    case 5: 
                        $message = "удовлетворительно знаете географию"; 
                        break;
                    case 4: 
                        $message = "терпимо знаете географию"; 
                        break;
                    case 3: 
                        $message = "плохо знаете географию"; 
                        break;
                    case 2: 
                        $message = "очень плохо знаете географию"; 
                        break;
                    case 1: 
                        $message = "очень плохо знаете географию"; 
                        break;
                    default:
                        $message = "вообще не знаете географию";
                }

                return $namePrefix . $message;
            }

            $name = isset($_POST["user"]) ? trim($_POST["user"]) : "";
            
            $userAnswers = array();
            if (isset($_POST["answers"])) {
                if (is_array($_POST["answers"])) {
                    $userAnswers = $_POST["answers"];
                }
            } else {
                $userAnswers = array_fill(0, 9, '');
            }

            while (count($userAnswers) < 9) {
                $userAnswers[] = '';
            }

            $answeredCount = 0;
            foreach ($userAnswers as $answer) {
                if ($answer != '') {          
                    $answeredCount++;
                }
            }

            $otv = array("6", "9", "4", "1", "3", "2", "5", "8", "7");
            
            $correctCount = countCorrectAnswers($otv, $userAnswers);
            
            $resultMessage = getResultMessage($name, $correctCount);

            print "<h2 align='center'>Результаты теста</h2>";
            print "<p align='center'><strong>$resultMessage</strong></p>";
            print "<p align='center'>Количество верных ответов: $correctCount из 9</p>";
            
            if (empty($name)) {
                print "<p align='center' style='color: red;'>Вы не ввели свое имя, можете это сделать, повторно пройдя тест.</p>";
            }
            
            if ($answeredCount < 9) {
                $notAnswered = 9 - $answeredCount;
                print "<p align='center' style='color: red;'>Ответ дан на $answeredCount из 9 вопросов</p>";
            }
            
            print "<p align='center'><a href='z4-3a.html'>Назад</a></p>";
        ?>
    </body> 
</html>