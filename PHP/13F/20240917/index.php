<?php
    //echo "<pre>";

    $parsed = parse_url($_SERVER["REQUEST_URI"]);
    $path = $parsed["path"];

    switch ($path) {
        case '/13F/20240917/penzvaltas':
            $mennyit = (int)($_GET["mennyit"] ?? 1);
            $mirol = $_GET["mirol"] ?? "USD";
            $mire = $_GET["mire"] ?? "HUF";

            $adatok = file_get_contents("https://kodbazis.hu/api/exchangerates?base=$mirol");
            $atalakitott_adatok = json_decode($adatok, true);

            $eredmeny = $mennyit * $atalakitott_adatok["rates"][$mire];
            $select_adatok = json_decode(file_get_contents("./currencies.json"), true);
            require_once "./views/valto.php";
            break;
        
        case '/13F/20240917/':
            require_once "./views/cimlap.html";
            break;
        default:
            $errorMsg = <<<html
                404 - Az oldal nem létezik!<br>
                Visza a <a href="./">címlapra</a>.
            html;
            
            echo $errorMsg;
            break;
    }
?>