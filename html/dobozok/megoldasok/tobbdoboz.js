let state = {
  "elemek": {
    "elso": {
      "id": "elso",
      "x": 1040.5,
      "y": 858.5
    },

    "masodik": {
      "id": "masodik",
      "x": 150.5,
      "y": 454.5
    },

    "harmadik": {
      "id": "harmadik",
      "x": 524.5,
      "y": 252.5
    },
  },
  "draggedId": null
}

// 1. Készíts renderelő függvényt, ami megjeleníti a dobozt a state-ből kiolvasott adatok alapján

const render = () => {
  let dobozok = "";

  for (let doboz of Object.values(state.elemek)) {
    dobozok += `
    <div
      style="top: ${doboz.y}px; left: ${doboz.x}px"
      class="position-absolute card box p-3 ${(state.draggedId === doboz.id ? "grabbed" : "not-grabbed")}"
      id="${doboz.id}"
      onmousedown="dragStart(window.event)"
      onmouseup="dragEnd()"
      onmouseleave="dragEnd()"
      onmousemove="mouseMove(window.event)"
    >
      <div class="card-title">
        ${doboz.id}
      </div>
    </div>
  `;
  }

  document.getElementById("drag-and-drop-app").innerHTML = dobozok;
}

// 2. A dobozt úgy rajzold ki, hogy az element-nek a position style attribútuma "absolute", a 
//    left és a top attribútuma pedig a state-ből származó x és y érték
// 3. A doboz mousedown eseményre reagálva módosítsd a state isDragged értékét true-ra

const dragStart = (e) => {
  const box = e.target.closest(".box");
  state.draggedId = box.id
  render();
}
// 4. A doboz mouseup és mouseleave eseményre reagálva módosítsd a state isDragged értékét false-ra
const dragEnd = () => {
  state.draggedId = null;
}
/* 5. A doboz mousemove eseménykor vizsgáld meg, hogy a state.isDragged értéke true-e
Amennyiben igen, írd be a state x és y kulcsa alá az egér aktuális x,y pozícióját */

const mouseMove = (e) => {
  if (state.draggedId) {
    const box = e.target.closest(".box");
    if (!box) return;

    state.elemek[state.draggedId].x = document.documentElement.scrollTop + e.clientX - box.offsetWidth / 2;
    state.elemek[state.draggedId].y = document.documentElement.scrollLeft + e.clientY - box.offsetHeight / 2;
    render();
  }
}

// 7. Az állapotváltozások után hívd meg a renderelő függvényt
document.addEventListener("DOMContentLoaded", () => {
  render();
});