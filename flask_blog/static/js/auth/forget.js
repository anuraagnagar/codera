"use-strict";

const emailInput = document.getElementById("email");
const submitBtn = document.getElementById("submit");
const emailError = document.getElementById("error");
const regEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

// This method is for validate User Email Address.
const emailValidator = () => {
  if (emailInput.value.match(regEx)) {
    emailInput.classList.remove("error");
    submitBtn.removeAttribute("disabled");
    emailError.textContent = "";
  } else {
    emailInput.classList.add("error");
    submitBtn.setAttribute("disabled", "");
    emailError.textContent = "Invalid email address.";
  }
};

emailInput.addEventListener("input", emailValidator);
