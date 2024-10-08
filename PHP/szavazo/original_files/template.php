<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Szavazó alkalmazás</title>
  <link rel="preconnect" href="https://fonts.gstatic.com" />
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap" rel="stylesheet" />
  <script src="https://kit.fontawesome.com/7f8f824712.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <header>
    <h1><i class="fas fa-comment-dots"></i> VoteR</h1>
  </header>
  <main>
    <section>
      <h2>#53 Melyik a kedvenc frontend JavaScript keretrendszered?</h2>
      <form method="POST">
        <ul>
          <li>
            <label><input type="radio" name="vote" value="Vue">Vue</label>
            <span><i class="fas fa-heart"></i>52%</span>
          </li>
          <li>
            <label><input type="radio" name="vote" value="React">React</label>
            <span><i class="fas fa-heart"></i>18%</span>
          </li>
          <li>
            <label><input type="radio" name="vote" value="Svelte">Svelte</label>
            <span><i class="fas fa-heart"></i>5%</span>
          </li>
          <li>
            <label><input type="radio" name="vote" value="Angular">Angular</label>
            <span><i class="fas fa-heart"></i>14%</span>
          </li>
          <li>
            <label><input type="radio" name="vote" value="jQuery">jQuery</label>
            <span><i class="fas fa-heart"></i>11%</span>
          </li>
        </ul>
        <input type="submit" value="Szavazok">
      </form>
    </section>
  </main>
</body>

</html>