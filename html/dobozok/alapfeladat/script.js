let state = {
  x: 150,
  y: 300,
  isDragged: false,
};

// 1. Készíts renderelő függvényt, ami megjeleníti a dobozt a state-ből kiolvasott adatok alapján

// 2. A dobozt úgy rajzold ki, hogy az element-nek a position style attribútuma "absolute", a 
//    left és a top attribútuma pedig a state-ből származó x és y érték

// 3. A doboz mousedown eseményre reagálva módosítsd a state isDragged értékét true-ra

// 4. A doboz mouseup és mouseleave eseményre reagálva módosítsd a state isDragged értékét false-ra

/* 5. A doboz mousemove eseménykor vizsgáld meg, hogy a state.isDragged értéke true-e
Amennyiben igen, írd be a state x és y kulcsa alá az egér aktuális x,y pozícióját */

// 7. Az állapotváltozások után hívd meg a renderelő függvényt
