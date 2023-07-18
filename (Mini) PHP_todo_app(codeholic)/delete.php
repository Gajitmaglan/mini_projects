<?php
echo "<pre>";
print_r($_POST);
echo "</pre>";

$json = file_get_contents('todo.json');
$json_array = json_decode($json, true);
// check if file and post exist (!)

$task_name = $_POST['task_name'];
unset($json_array[$task_name]);

file_put_contents('todo.json', json_encode($json_array, JSON_PRETTY_PRINT));

header('location: index.php');
