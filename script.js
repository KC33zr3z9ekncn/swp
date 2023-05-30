
function toggleRectangle() {
  var infoBox = document.getElementById('infoBox');
  infoBox.classList.toggle('hidden');
}
function toggleRectangle2() {
  var infoBox = document.getElementById('infoBoxrechts');
  infoBox.classList.toggle('hidden');
}

    function toggleButton(button) {
            if (button.textContent.trim() === "Done") {
                button.textContent = "Close";
                button.classList.remove("done");
                button.classList.add("close");
            } else {
                button.textContent = "Done";
                button.classList.remove("close");
                button.classList.add("done");
            }
        }
