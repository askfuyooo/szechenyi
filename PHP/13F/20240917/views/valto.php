<!DOCTYPE html>
<html lang="hu">

<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css" />
</head>

<body>
    <div class="card w-25 m-auto p-3">
        <form action="/13F/20240917/penzvaltas" method="GET">
            <h2>Mennyit?</h2>
            <input class="form-control mb-2" type="number" name="mennyit" value="<?php echo $mennyit ?>">

            <h2>Miről?</h2>
            <select name="mirol" class="form-control mb-2">
                <?php foreach($select_adatok as $adat): ?>
                    <option value="<?= $adat["label"] ?>" <?= $adat["label"] === $mirol ? "selected" : ""?>>
                        <?= "{$adat["name"]} {$adat["symbol"]}" ?>
                    </option>
                <?php endforeach ?>
            </select>

            <h2>Mire?</h2>
            <select name="mire" class="form-control mb-2">
                <?php foreach($select_adatok as $adat): ?>
                    <option value="<?= $adat["label"] ?>" <?= $adat["label"] === $mire ? "selected" : "" ?>>
                        <?= "{$adat["name"]} {$adat["symbol"]}" ?>
                    </option>
                <?php endforeach ?>
            </select>

            <input type="submit" value="Elküld" class="btn btn-outline-primary">

            <span class="float-right mt-2"><?= $eredmeny ?></span>
        </form>
    </div>
</body>

</html>