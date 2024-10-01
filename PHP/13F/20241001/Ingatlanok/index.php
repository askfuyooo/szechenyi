<?php
/*
Feladat:
A főoldalon vegyünk fel egy select elemet, amelyet a kategoriak.json fájlból töltsünk fel
Legyen egy submit gomb amire kattintva a selectben kiválasztott ingatlanok adatai jelennek meg
az ingatlanok.json fájl tartalma alapján.

Elérési utak:
/13F/20241001/Ingatlanok/ingatlanok --> főoldal
/13F/20241001/Ingatlanok/ --> címlap
minden más esetben: az oldal nem található - ugrás a címlapra
*/

const DEFAULT_PATH = "/13F/20241001/Ingatlanok";

$url = $_SERVER["REQUEST_URI"];
$path = parse_url($url, PHP_URL_PATH);
$render = NULL;

switch ($path) {
    case DEFAULT_PATH . "/": {
        $render = "cimlap";
        break;
    }

    case DEFAULT_PATH ."/ingatlanok": {
        $kategoriak = json_decode(file_get_contents("kategoriak.json"), true);
        $ingatlanok = json_decode(file_get_contents("ingatlanok.json"), true);

        $kategoriaSelected = isset($_GET["kategoriak"]) ? $_GET["kategoriak"] : NULL;

        $render = "ingatlanok";
        break;
    }

    default: {
        $render = "error";
        break;
    }
}
require_once "./views/$render.php";