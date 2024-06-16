const currentDate = new Date();
const currentYear = currentDate.getFullYear();
const yearElement = document.getElementById('year-now');
yearElement.textContent = currentYear;