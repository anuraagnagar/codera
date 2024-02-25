"use-strict";

// Get references to elements from HTML documents.
const emailInput = document.getElementById("email");
const submitBtn = document.getElementById("submit");
const emailError = document.getElementById("error");

// RegEx pattern string for user email input.
const emailRegEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

(function () {
  if (emailInput.value.match(emailRegEx)) {
    submitBtn.removeAttribute("disabled");
  }
})();

/**
 * Validates an email address and updates the UI accordingly.
 * If the email is invalid, adds error styling, displays an error message,
 * and disables the submit button.
 */
const emailValidator = () => {
  if (emailInput.value.length > 0) {
    if (emailInput.value.match(emailRegEx)) {
      emailInput.classList.remove("error");
      emailError.setAttribute("hidden", "true");
      emailError.textContent = "";
      submitBtn.removeAttribute("disabled");
    } else {
      emailInput.classList.add("error");
      emailError.removeAttribute("hidden");
      emailError.textContent = "Invalid email address.";
      submitBtn.setAttribute("disabled", "true");
    }
  } else {
    emailInput.classList.remove("error");
    emailError.textContent = "";
  }
};

emailInput.addEventListener("input", emailValidator);
