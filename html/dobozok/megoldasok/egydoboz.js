let state = {
  x: 150,
  y: 300,
  isDragged: false,
};

// 1. Készíts renderelő függvényt, ami megjeleníti a dobozt a state-ből kiolvasott adatok alapján

const render = () => {
  const doboz = `
    <div
      id="doboz"
      style="top: ${state.y}px; left: ${state.x}px"
      class="position-absolute card box p-3 ${(state.isDragged ? "grabbed" : "not-grabbed")}"

      onmousedown="enableDragging()"
      onmouseup="disableDragging()"
      onmouseleave="disableDragging()"
      onmousemove="mouseMove(window.event)"
    >
      <div class="card-title">
        Húzd
      </div>
    </div>
  `;

  document.getElementById("drag-and-drop-app").innerHTML = doboz;
}

// 2. A dobozt úgy rajzold ki, hogy az element-nek a position style attribútuma "absolute", a 
//    left és a top attribútuma pedig a state-ből származó x és y érték

// 3. A doboz mousedown eseményre reagálva módosítsd a state isDragged értékét true-ra

const enableDragging = () => {
  state.isDragged = true;
  render();
}

// 4. A doboz mouseup és mouseleave eseményre reagálva módosítsd a state isDragged értékét false-ra

const disableDragging = () => {
  state.isDragged = false;
  render();
}

/* 5. A doboz mousemove eseménykor vizsgáld meg, hogy a state.isDragged értéke true-e
Amennyiben igen, írd be a state x és y kulcsa alá az egér aktuális x,y pozícióját */

const mouseMove = (e) => {
  if (state.isDragged) {
    const doboz = document.getElementById("doboz");
    
    if (!doboz) return;

    state.x = document.documentElement.scrollLeft + e.clientX - doboz.offsetWidth / 2;
    state.y = document.documentElement.scrollTop + e.clientY - doboz.offsetHeight / 2;
    render();
  }
}

// 7. Az állapotváltozások után hívd meg a renderelő függvényt

window.onload = render;