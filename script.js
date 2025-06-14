// frontend/script.js

document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.querySelector('input[type="file"]');
  const preview = document.createElement('img');
  const form = document.querySelector('form');
  const button = form.querySelector('button');

  preview.style.display = 'none';
  form.appendChild(preview);

  fileInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
      };
      reader.readAsDataURL(file);
    }
  });

  form.addEventListener('submit', function () {
    button.disabled = true;
    button.textContent = 'Diagnosing...';
  });
});
