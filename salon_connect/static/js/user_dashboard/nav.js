
function myFunction() {
    var x = document.getElementById("Topnav");
    if (x.className === "nav") {
      x.className += " responsive";
    } else {
      x.className = "nav";
    }
  }