<?php
    if ($_FILES["imagen"]["size"] < 2000000 && in_array($_FILES["imagen"]["type"], ["image/png", "image/jpeg"])) {
        move_uploaded_file($_FILES["imagen"]["tmp_name"], "uploads/" . $_FILES["imagen"]["name"]);
    }   
?>