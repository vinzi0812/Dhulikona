var menu_btn = document.querySelector("#menu-btn");
var sidebar = document.querySelector("#sidebar");
var container = document.querySelector(".my-container");
menu_btn.addEventListener("click", () => {
  sidebar.classList.toggle("active-nav");
  container.classList.toggle("active-cont");
});

/*==============================table===================================*/

function addRow() {
    var table = document.getElementById("dataTable");
    var newRow = table.insertRow(table.rows.length);
    var columns = 5; // Number of columns in the table

    for (var i = 0; i < columns; i++) {
      var cell = newRow.insertCell(i);

      if (i === 0) {
        // Sno column (integer)
        cell.innerHTML = "1";
      } else if (i === 1) {
        // Issue column (text)
        cell.innerHTML ="abcdefgh";
      } else if (i === 2) {
        // Date column (date picker)
        cell.innerHTML = "<input type='date' value='13-06-2023'>";
      } else if (i === 3) {
        // Status column (dropdown)
        cell.innerHTML =
          "<select ><option value='options'>MUC</option><option value='option2'>G P</option><option value='option3'>Govt.</option></select>";
      } else if (i === 4) {
        // Delete column (checkbox)
        cell.innerHTML =
          "<input type='checkbox' onclick='toggleStrikeThrough(this)'>";
      }
    }
  }

  function toggleStrikeThrough(checkbox) {
    var row = checkbox.parentNode.parentNode;

    if (checkbox.checked) {
      row.classList.add(strike-through);
    } else {
      row.classList.remove("strike-through");
    }
  }

  // Add initial rows
  var initialRowCount = 10;
  for (var i = 0; i < initialRowCount; i++) {
    addRow();
  }