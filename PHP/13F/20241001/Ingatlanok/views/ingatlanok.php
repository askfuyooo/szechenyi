<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Ingatlanok</title>
</head>
    <body>
        <div class="container text-center mt-3">
            <div class="row justify-content-center">
                <!--Kategóriák-->
                <h1>Kategóriák</h1>
                <div class="col-sm-2">
                    <form action="" method="get">
                        <select name="kategoriak" id="kategoriak" class="form form-control">
                            <?php foreach ($kategoriak as $kategoria): ?>
                                <option value="<?= $kategoria["id"] ?>" <?= ($kategoriaSelected == $kategoria["id"] ? "selected" : "") ?>><?= $kategoria["nev"] ?></option>
                            <?php endforeach ?>
                        </select>
                        <button type="submit" class="btn btn-primary mt-2">Keresés</button>
                    </form>
                </div>

                <!--Ingatlanok-->
                <?php if ($kategoriaSelected): ?>
                <div class="mt-4 mb-2 justify-content-center row">
                    <h1>Talált ingatlanok</h1>
                    <div class="col-sm-4">
                        <?php foreach ($ingatlanok as $ingatlan): ?>
                            <?php if ($ingatlan["kategoria"]["id"] == $kategoriaSelected): ?>
                                <div class="card m-2" id="<?= $ingatlan["id"] ?>">
                                    <div class="card-body">
                                        <h5 class="card-title"><?= $ingatlan["leiras"] ?></h5>
                                        <p class="card-text"><?= $ingatlan["ar"] ?> Ft.-</p>
                                        <p class="card-subtitle"><?= $ingatlan["hirdetesDatuma"] ?></p>
                                        <p class="card-subtitle">Tehermentes: <?= $ingatlan["tehermentes"] ? "igen" : "nem" ?></p>
                                    </div>
                                </div>
                            <?php endif ?>
                        <?php endforeach ?>
                    </div>
                </div>
                <?php endif ?>
            </div>
            <h5 class="mt-2">Vissza a <a href="./">főoldalra</a>!</h5>
        </div>
    </body>
</html>