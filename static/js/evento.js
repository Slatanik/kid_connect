document.addEventListener("DOMContentLoaded", function() {
  var currentDate = new Date();
  var currentMonth = currentDate.getMonth();
  var currentYear = currentDate.getFullYear();

  displayCalendar(currentMonth, currentYear);

  var prevBtn = document.getElementById("prev-btn");
  var nextBtn = document.getElementById("next-btn");

  prevBtn.addEventListener("click", function() {
    currentMonth--;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear--;
    }
    displayCalendar(currentMonth, currentYear);
  });

  nextBtn.addEventListener("click", function() {
    currentMonth++;
    if (currentMonth > 11) {
      currentMonth = 0;
      currentYear++;
    }
    displayCalendar(currentMonth, currentYear);
  });

  function displayCalendar(month, year) {
    var calendarBody = document.getElementById("calendar-body");
    var monthYear = document.getElementById("month-year");
    monthYear.innerHTML = getMonthName(month) + " " + year;

    var firstDay = new Date(year, month, 1).getDay();
    var daysInMonth = new Date(year, month + 1, 0).getDate();
    calendarBody.innerHTML = "";

    var date = 1;
    for (var i = 0; i < 6; i++) {
      var row = document.createElement("tr");

      for (var j = 0; j < 7; j++) {
        if (i === 0 && j < firstDay) {
          var cell = document.createElement("td");
          row.appendChild(cell);
        } else if (date > daysInMonth) {
          break;
        } else {
          var cell = document.createElement("td");
          cell.textContent = date;
          if (date === currentDate.getDate() && year === currentDate.getFullYear() && month === currentDate.getMonth()) {
            cell.classList.add("today");
          }
          row.appendChild(cell);
          date++;
        }
      }

      calendarBody.appendChild(row);
    }
  }

  function getMonthName(month) {
    var monthNames = [
      "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ];
    return monthNames[month];
  }
}); 