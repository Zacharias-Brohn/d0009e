console.log("Script Loaded");
function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    dropdown.classList.toggle("show");
    console.log("Clicked")
}
window.onclick = function(event) {
  var dropdown = document.getElementById("dropdown");
  if (!event.target.matches('button') && !dropdown.contains(event.target)) {
      if (dropdown.classList.contains('show')) {
          dropdown.classList.remove('show');
      }
  }
};