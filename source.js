let days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];

let months = [
  "January",
  "Feburary",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

let day = days[new Date().getDay()];
let month = months[new Date().getMonth()];
document.getElementById("date").innerHTML = "Today is " + day + " " + month;

// console.dir(Date.prototype);

const button = document.getElementById('yes');

button.addEventListener('click', () => {
  alert('If yes, fill the form')
});

const button2 = document.getElementById('no');

button2.addEventListener('click', () => {
  alert('If no, have a great day!')
});

