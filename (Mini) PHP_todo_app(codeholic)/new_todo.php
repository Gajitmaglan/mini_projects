<?php
// echo "<pre>";
// print_r($_POST);
// echo "</pre>";


// if (isset($_POST['todo_name'])) { ... }
$todo_name = $_POST['todo_name'] ?? '';
$todo_name = trim($todo_name);

if ($todo_name) {
    if (file_exists('todo.json')) {
        $json = file_get_contents('todo.json');
        $json_array = json_decode($json, true);
    } else {
        $json_array = [];
    }
    $json_array[$todo_name] = ['completed' => false];
    // convert to json string and save to file in a pretty print
    file_put_contents('todo.json', json_encode($json_array, JSON_PRETTY_PRINT));

    echo "<pre>";
    var_dump($json_array);
    echo "</pre>";
}

header('location: index.php'); // redirect the user