<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Emotions</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
</head>
<body>
</body>
</html>

<?php
$a= file_get_contents("file.txt");
$c=$a*100;
$d=100-$c;
if ($a>0.5) 
{
    echo "<img class='center' src='happy.png' alt='Happy'>";
    echo "<p class='text'>% Agree = $c %</p>";
    echo "<p class='text'>% Disagree = $d %</p>";
}
else
{
    echo "<img class='center' src='sad.png' alt='Sad'>";
    echo "<p class='text'>% Agree = $c %</p>";
    echo "<p class='text'>% Disagree = $d %</p>";
}
$b= file_get_contents("file1.txt");
echo "<p class='text'>Number of Faces Analysed = $b</p>";
?> 