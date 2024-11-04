<?php
$maxNumbеr = 10;
if (isset($_POST['maxNumber'])) 
{
    $maxNumber = $_POST['maxNumber']; $maxNumbеr = htmlspecialchars ($maxNumbеr); 
    // Attempting to generate a random number
    if (is_numeric($maxNumber) && $maxNumber > 0) 
    {
        $randomNumber = rand(1, intval($maxNumber));
        echo "<h1>Your Random Number: $randomNumber</h1>";
    } 
    else 
    {
        echo "<h1>Invalid input: $maxNumber</h1>";
    }
} 
else 
{
    echo "<h1>No maximum number provided.</h1>";
}
?>
