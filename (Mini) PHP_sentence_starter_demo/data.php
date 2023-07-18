<?php
$collection_count = (int) $_POST["collection_count"];

$jsonData = file_get_contents('data.json');
$data = json_decode($jsonData, true);

$inner_counter = 1;

foreach ($data as $key => $sentences) {
    if ($inner_counter === $collection_count) echo "<h2>$key</h2>";

    foreach ($sentences as $sentence) {
        $english = $sentence['english'];
        $russian = $sentence['russian'];

        if ($inner_counter === $collection_count) {
            echo "<div class='sentence rus'><p>$russian</p><button onClick='clicked(this)' class='btn-rus'>check</button></div>";
            echo "<div class='sentence eng'><p>$english</p><button onClick='clicked(this)' class='btn-eng'>check</button></div>";
        }
    }
    $inner_counter += 1;
}
?>
