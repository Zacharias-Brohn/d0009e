console.log("Script Loaded");
// Toggle the visibility of the dropdown
function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    dropdown.classList.toggle("show");
    console.log("Clicked")
    // Close the dropdown if the user clicks outside of it
}
window.onclick = function(event) {
  var dropdown = document.getElementById("dropdown");
  // Check if the click target is not the button or dropdown
  if (!event.target.matches('button') && !dropdown.contains(event.target)) {
      if (dropdown.classList.contains('show')) {
          dropdown.classList.remove('show');
      }
  }
};