<?php

echo "<pre>";
var_dump($_POST);
echo "</pre>";

$json = file_get_contents('todo.json');
$json_array = json_decode($json, true);
// check if file and post exist (!)

$task_name = $_POST['task_name'];
$json_array[$task_name]['completed'] = !$json_array[$task_name]['completed'];

file_put_contents('todo.json', json_encode($json_array, JSON_PRETTY_PRINT));

header('location: index.php');
