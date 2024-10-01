<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css" />
    <title>Terméklista</title>
</head>
    <body>
        <div class="container">
            <?php foreach ($termekek as $termek): ?>
                <div class="card mt-3 p-1">
                    <h2>
                        Név: <?= $termek["name"] ?>
                    </h2>
                    <p>
                        Ár: <?= $termek["price"] ?>Ft.-
                    </p>
                </div>
            <?php endforeach ?>

        <span class="float-right mt-2">Vissza a <a href="<?= FILE_FOLDER ?>">címlapra</a>!</span>
        </div>
    </body>
</html>