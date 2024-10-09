//Dobozok dolgozat - Tóth Ádám, 13. F

//container lekérése
const container = document.getElementById("drag-and-drop-app");

//Random szám generálás
const getRandomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

//Random koordináta generálás
const getRandomCoords = () => {
  /*
    Azért 50-től generál, hogy ne a képernyő tetejére / bal szélére generálódjon,
    container.offsetWidth: container szélessége
    container.offsetHeight: container hosszúsága
  */
  const coords = {
    "x": getRandomNumber(50, container.offsetWidth - 150), //Azért -150, hogy ne a képernyő jobb szélére generálja
    "y": getRandomNumber(50, container.offsetHeight)
  }

  return coords;
}

//State beállítása
/*
  boxes: dobozok egyenként inicializálva, egyedi azonosítójuk alapján
    id: doboz egyedi azonosítója
    label: dobozon megjelenő szöveg
    x: doboz x koordinátája
    y: doboz y koordinátája

  draggedId: húzás alatt lévő doboz egyedi azonosítója, ha nincs, akkor null
*/
let state = {
  "boxes": {
    "first": {
      "id": "first",
      "label": "Első doboz",
      "x": getRandomCoords().x,
      "y": getRandomCoords().y
    },

    "second": {
      "id": "second",
      "label": "Második doboz",
      "x": getRandomCoords().x,
      "y": getRandomCoords().y
    },

    "third": {
      "id": "third",
      "label": "Harmadik doboz",
      "x": getRandomCoords().x,
      "y": getRandomCoords().y
    },
  },
  draggedId: null
};

// 1. Készíts renderelő függvényt, ami megjeleníti a dobozt a state-ből kiolvasott adatok alapján
// 2. A dobozt úgy rajzold ki, hogy az element-nek a position style attribútuma "absolute", a 
//    left és a top attribútuma pedig a state-ből származó x és y érték
const render = () => {
  let skeletons = ""; //containerbe kerülő dobozok váza
  for (let box of Object.values(state.boxes)) { //Végigmegy a state.boxes dobozain
    //Doboz vázának létrehozása és hozzáadása a skeletons változóhoz, feladatonként megadva az értékeket
    skeletons += `
      <div
        style="top: ${box.y}px; left: ${box.x}px"
        class="position-absolute box card p-3 ${(state.draggedId === box.id) ? "grabbed" : "not-grabbed"}"
        id="${box.id}"

        onmousedown="enableDragging(window.event)"
        onmouseup="disableDragging()"
        onmouseleave="disableDragging()"
        onmousemove="mouseMove(window.event)"
      >
        <div class="card-title">
          ${box.label}
        </div>
      </div>
    `;
  }

  //A container tartalmának beállítja a skeletons változóból a dobozok vázait
  container.innerHTML = skeletons;
}

// 3. A doboz mousedown eseményre reagálva módosítsd a state isDragged értékét true-ra

const enableDragging = (e) => {
  state.draggedId = e.target.closest(".box").id; //state.draggedId beállítása a függvényt meghívó event legközelebbi dobozára beállítva
  render();
}

// 4. A doboz mouseup és mouseleave eseményre reagálva módosítsd a state isDragged értékét false-ra

const disableDragging = () => {
  state.draggedId = null; //state.draggedId null-ra állítása
  render();
}

/* 5. A doboz mousemove eseménykor vizsgáld meg, hogy a state.isDragged értéke true-e
Amennyiben igen, írd be a state x és y kulcsa alá az egér aktuális x,y pozícióját */

const mouseMove = (e) => {
  if (state.draggedId) { //csak akkor fut le, ha be van állítva egyedi azonosítóval rendelkező doboz a state.draggedId változóban
    const box = e.target.closest(".box"); //függvényt meghívó event legközelebbi dobozának beállítása box változóba
    if (!box) return; //ha hiba lépett fel, és nincs doboz, visszatér a függvény / megszakad
    
    //doboz koordinátáinak beállítása úgy, hogy a doboz közepe a kurzornál legyen
    state.boxes[state.draggedId].x = document.documentElement.scrollTop + e.clientX - box.offsetWidth / 2;
    state.boxes[state.draggedId].y = document.documentElement.scrollLeft + e.clientY - box.offsetHeight / 2;
    render();
  }
}

// 7. Az állapotváltozások után hívd meg a renderelő függvényt
//Document object model betöltésekor (weboldal betöltésekor) meghívja a render() függvényt
document.addEventListener("DOMContentLoaded", render);