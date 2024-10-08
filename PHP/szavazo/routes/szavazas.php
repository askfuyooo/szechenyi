<?php

//Eredmények beolvasása
$votesPath = __DIR__ . "/../53.json";
$voteDatas = json_decode(file_get_contents($votesPath), true);
$answers = $voteDatas["answers"];
$votes = $voteDatas["votes"];

//Szavazás esetén
if (isset($_POST["vote"])) {
    $voted = $_POST["vote"];
    $newValue = $votes[$voted] + 1;
    $votes[$voted] = $newValue;

    //Fájl mentése
    $voteDatas["votes"] = $votes;
    file_put_contents($votesPath, json_encode($voteDatas));
}

//Százalék leosztása 1 főre
$votersCount = array_sum($votes);
$percentPerVoter = round(100 / $votersCount, 1);

require_once __DIR__ . "/../views/template.php";