"use strict";

const passwordOne = document.getElementById("password-1");
const passwordTwo = document.getElementById("password-2");
const alertCheck = document.getElementById("alert-check");
const alertCheckIcon = document.getElementById("alert-check-icon");
const changePassword = document.getElementById("change-password");

function checkInput(input) {
  if (
    passwordOne.value.length >= 8 &&
    passwordOne.value.length <= 15 &&
    passwordTwo.value.length >= 8 &&
    passwordTwo.value.length <= 15
  ) {
    if (passwordOne.value == passwordTwo.value) {
      changePassword.removeAttribute("disabled");
      alertCheck.textContent = "Passwords Match";
      alertCheck.style.color = "#008000bf";
    } else {
      changePassword.setAttribute("disabled", "");
      alertCheck.textContent = "Passwords Not Match";
      alertCheck.style.color = "#df3253";
    }
  } else {
    changePassword.setAttribute("disabled", "");
  }
}
