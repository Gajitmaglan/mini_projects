<!DOCTYPE html>
<html lang="en">

<?php

if (file_exists('todo.json')) {
    $json = file_get_contents('todo.json');
    $tasks = json_decode($json, true);
} else {
    $tasks = [];
}


?>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>todo app</title>
</head>

<body>
    <form action="new_todo.php" method="post">
        <input type="text" name="todo_name" placeholder="Enter your todo..." autocomplete="false">
        <button>New task</button>
    </form>

    <?php foreach ($tasks as $task_name => $task) : ?>
        <div>
            <form action="change_status.php" method="POST" style="display: inline-block;">
                <input type="hidden" name="task_name" value="<?php echo $task_name ?>">
                <input type="checkbox" <?php echo $task['completed'] ? 'checked' : ''; ?> />
            </form>
            <?php echo $task_name ?>
            <form action="delete.php" method="post" style="display: inline-block">
                <input type="hidden" name="task_name" value="<?php echo $task_name ?>">
                <button>Delete</button>
            </form>
        </div>
    <?php endforeach; ?>

    <script>
        const checkBoxes = document.querySelectorAll('input[type=checkbox]');
        checkBoxes.forEach(ch => {
            ch.onclick = function() {
                this.parentNode.submit(); // this = checkbox itself
            }
        })
    </script>


</body>

</html>