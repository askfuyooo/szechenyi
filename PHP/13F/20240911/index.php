<?php
//több ingatlan adatának eltárolása
    $ingatlanok = [
        [
            "id" => 1,
            "leiras" => "családi ház",
            "ar" => 35000000,
            "hirdetesDatuma" => "2024-05-06",
            "tehermentes" => true,
            "kategoria" => [
                "id" => 1,
                "nev" => "épület"
            ]
        ],
        [
            "id" => 2,
            "leiras" => "családi ház",
            "ar" => 25000000,
            "hirdetesDatuma" => "2024-05-16",
            "tehermentes" => false,
            "kategoria" => [
                "id" => 1,
                "nev" => "épület"
            ]
        ],
        [
            "id" => 3,
            "leiras" => "garázs",
            "ar" => 7000000,
            "hirdetesDatuma" => "2024-03-06",
            "tehermentes" => true,
            "kategoria" => [
                "id" => 3,
                "nev" => "kültéri terület"
            ]
        ],
        [
            "id" => 4,
            "leiras" => "zárt kert",
            "ar" => 5000000,
            "hirdetesDatuma" => "2024-07-06",
            "tehermentes" => false,
            "kategoria" => [
                "id" => 2,
                "nev" => "földterület"
            ]
        ],
             
    ];

    echo "<h1>Ingatlanok:</h1>";
    foreach ($ingatlanok as $ingatlan) {
        foreach ($ingatlan as $ertek => $kulcs) {
            if (!is_array($kulcs)) {
                echo "$ertek: $kulcs<br>";
            } else {
                echo "$ertek: {$kulcs["nev"]}<br>";
            }
        }
        echo "<br>";
    }
    ?>