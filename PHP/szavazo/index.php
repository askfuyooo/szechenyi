<?php
//Feladat: 

//htdocs: /Dolgozat/sajatnev/ bemásolni a szavazo mappát a közösből

//A template php fájl a főoldal alapját képezi. Alakítsd át úgy, hogy az 53.json fájl 
//alapján töltse fel az adatokat foreach ciklussal (a ciklusban 1 darab rádió gomb)

//Oldd meg, hogy a szavazás gombra kattintva megfelelően változzanak a százalékos értékek.
//Ehhez felül kell írnod az új adatokkal az 53.json fájlt
//utasítások: 
    // file_put_contents("fájlnév",adatok)
    // array_sum(tömb_neve) összeadja az asszociatív tömb kulcsain lévő értékeket (a százalék számításhoz)
    // round(érték, tizedesek száma) kerekít

//Útvonalak:
    // /Dolgozat/sajatnev/szavazo/szavazas --> szavazó oldal elérése (főoldal)
    // /Dolgozat/sajatnev/szavazo/ --> címlap
    // minden más esetben: 'Az oldal nem található, vissza a címlapra'


//code...

$uri = $_SERVER["REQUEST_URI"];
$fullPath = parse_url($uri, PHP_URL_PATH);
$pathExploded = explode("/szavazo", $fullPath);
$path = $pathExploded[1] ?? $fullPath;
//A __DIR__ és ezek alapján szinte bármilyen elérési útvonallal működni fog

$render = [
    "site" => NULL,
    "hasBackend" => NULL
];

//Útvonalválasztó
switch ($path) {
    case "/": {
        $render["site"] = "cimlap";
        $render["hasBackend"] = false;
        break;
    }

    case "/szavazas": {
        $render["site"] = "szavazas";
        $render["hasBackend"] = true;
        break;
    }

    default: {
        $render["site"] = "error";
        $render["hasBackend"] = false;
        break;
    }
}

//Fájl meghívása, azért így, hogy minél átláthatóbb legyen az index.php, és a fájlok backend része.
$directory = $render["hasBackend"] ? "routes" : "views";
$extension = $render["hasBackend"] ? "php" : "html";

require_once __DIR__ . "/$directory/{$render["site"]}.$extension";