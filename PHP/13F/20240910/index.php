<?php
    declare(strict_types=1);
    function sorTores() {
        echo "<br>";
    }

    //1. Feladat
    function parosParatlan(int $szam): string {
        return ($szam % 2 == 0) ? "páros" : "páratlan";
    }

    $szam = 7;
    echo "A(z) $szam szám " . parosParatlan($szam) . "!";
    sorTores();


    //2. Feladat
    function melyikNagyobb(int $szam1, int $szam2): int {
        return ($szam1 > $szam2) ? $szam1 : $szam2;
    }

    $szam1 = 5;
    $szam2 = 8;
    echo "A(z) $szam1 és $szam2 számok közül " . melyikNagyobb($szam1, $szam2) . " nagyobb.";
    sorTores();


    //3. Feladat
    $szamtomb = [8, 6, 5, 3, 5];
    sort($szamtomb);

    foreach ($szamtomb as $szam) {
        echo $szam . " ";
    }
    sorTores();

    
    //4. Feladat - associative, 1 ingatlan
    $ingatlan = [
        "id" => 1,
        "leiras" => "családi ház",
        "ar" => 3400000000,
        "hdatum" => "2024_04_03",
        "tehermentes" => true
    ];

    echo "Az ingatlan ára: {$ingatlan["ar"]} Ft-,";
    sorTores();


    //5. Feladat - több ingatlan
    $ingatlanok = [
        [
            "id" => 1,
            "leiras" => "családi ház",
            "ar" => 34000000,
            "hdatum" => "2024_04_03",
            "tehermentes" => true
        ],
        [
            "id" => 2,
            "leiras" => "panel ház",
            "ar" => 50000000,
            "hdatum" => "2024_09_07",
            "tehermentes" => false
        ],
        [
            "id" => 3,
            "leiras" => "kertes ház",
            "ar" => 35000000,
            "hdatum" => "2024_01_01",
            "tehermentes" => false
        ],
        [
            "id" => 4,
            "leiras" => "híd alatt",
            "ar" => 0,
            "hdatum" => "2000_01_01",
            "tehermentes" => true
        ]
    ];
    //első ingatlan hírdetési dátum
    echo "Az első ingatlan hírdetési dátuma: {$ingatlanok[0]["hdatum"]}";
    sorTores();

    //6. Feladat - 40M alatti házak
    echo "<h2>Ingatlanok 40 millió Forint alatt:</h2>";
    foreach ($ingatlanok as $ingatlan) {
        if ($ingatlan["ar"] < 40000000) {
            echo "id: {$ingatlan["id"]} <br>";
            echo "leírás: {$ingatlan["leiras"]} <br>";
            echo "ár: {$ingatlan["ar"]} Ft-, <br>";
            echo "hírdetés dátuma: {$ingatlan["hdatum"]} <br>";
            echo "tehermentes: " . ($ingatlan["tehermentes"] ? "igen" : "nem") . "<br>";
            sorTores();
        }
    }


    //7. Feladat
    echo "<h2>Minden ingatlan kiíratva, kicsit máshogy:</h2>";
    foreach ($ingatlanok as $ingatlan) {
        foreach ($ingatlan as $key => $value) {
            echo "$key: $value";
            sorTores();
        }
        sorTores();
    }


    //8. Feladat
    echo json_encode($ingatlanok);
?>