<!DOCTYPE html>
<html lang="hu">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Szavazó alkalmazás</title>
  <link rel="preconnect" href="https://fonts.gstatic.com" />
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap" rel="stylesheet" />
  <script src="https://kit.fontawesome.com/7f8f824712.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="./public/css/style.css">
</head>

<body>
  <header>
    <h1><i class="fas fa-comment-dots"></i> VoteR</h1>
  </header>
  <main>
    <section>
      <h2><?= $answers ?></h2>
      <form method="POST" id="votesForm">
        <ul>
          <?php foreach ($votes as $key => $value): ?>
            <li>
              <label><input type="radio" name="vote" value="<?= $key ?>"><?= $key ?></label>
              <span><i class="fas fa-heart"></i><?= $value * $percentPerVoter ?>%</span>
            </li>
          <?php endforeach ?>
        </ul>
        <input type="submit" value="Szavazok">
      </form>
    </section>
    <p>Vissza a <a href="./" draggable="false">címlapra</a>.</p>
  </main>
<script src="./public/js/main.js"></script>
</body>
</html>