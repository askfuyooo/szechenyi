<?php
    define("FILE_FOLDER", "/13F/20240925/");

    $url = $_SERVER["REQUEST_URI"];
    $path = parse_url($url)["path"];

    switch ($path) {
        case FILE_FOLDER: {
            require_once "views/cimlap.html";
            break;
        }

        case FILE_FOLDER . "termeklista/": {
            $termekek = json_decode(file_get_contents("termeklista/termekek.json"), true);
            require_once "views/termekek.php";
            break;
        }

        default: {
            $errorMsg = <<<html
                <title>Hiba!</title>
                <h1>404 - Hiba!</h1>
                <p>Térjen vissza a <a href="./">címlapra</a>!</p>
            html;
            echo $errorMsg;
            break;
        }
        
    }
?>