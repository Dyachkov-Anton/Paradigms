const hoursElement = document.querySelector(".hours");
const minutesElement = document.querySelector(".minutes");
const secondsElement = document.querySelector(".seconds");
const milisecondsElement = document.querySelector(".miliseconds");

const startButton = document.querySelector(".start");
const pauseButton = document.querySelector(".pause");
const stopButton = document.querySelector(".stop");
const roundButton = document.querySelector(".breakpoint");

startButton.addEventListener("click", () => {
  clearInterval(interval);
  interval = setInterval(startTimer, 10);
});
pauseButton.addEventListener("click", () => {
  clearInterval(interval);
});
stopButton.addEventListener("click", () => {
  clearInterval(interval);
  hours = 0;
  minutes = 0;
  seconds = 0;
  miliseconds = 0;
  hoursElement.innerText = "00";
  minutesElement.innerText = "00";
  secondsElement.innerText = "00";
  milisecondsElement.innerText = "00";
  const results = document.querySelector(".rounds");
  results.innerHTML = "";
  counter = 0;
});
roundButton.addEventListener("click", () => {
  counter++;
  const results = document.querySelector(".rounds");
  const block = document.createElement("li");
  block.innerText = `Round ${counter} - ${hours} : ${minutes} : ${seconds} : ${miliseconds}`;
  results.append(block);
});

let hours = 0,
  minutes = 0,
  seconds = 0,
  miliseconds = 0,
  interval,
  counter = 0;

function startTimer() {
  miliseconds++;
  if (miliseconds < 9) {
    milisecondsElement.innerText = "0" + miliseconds;
  }
  if (miliseconds > 9) {
    milisecondsElement.innerText = miliseconds;
  }
  if (miliseconds > 99) {
    seconds++;
    secondsElement.innerText = "0" + seconds;
    miliseconds = 0;
    milisecondsElement.innerText = "0" + miliseconds;
  }

  if (seconds < 9) {
    secondsElement.innerText = "0" + seconds;
  }
  if (seconds > 9) {
    secondsElement.innerText = seconds;
  }
  if (seconds > 59) {
    minutes++;
    minutesElement.innerText = "0" + minutes;
    seconds = 0;
  }

  if (minutes < 9) {
    minutesElement.innerText = "0" + minutes;
  }
  if (minutes > 9) {
    minutesElement.innerText = minutes;
  }
  if (minutes > 59) {
    hours++;
    hoursElement.innerText = "0" + hours;
    minutes = 0;
  }
}
