"use-strict";

// Get references to input elements from HTML documents.
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const submitBtn = document.getElementById("submit");
// Get references to error message elements from HTML documents.
const emailError = document.getElementById("email-error");
const passwordError = document.getElementById("password-error");
const showPassword = document.getElementById("show-password");

// RegEx pattern string for user email input.
const emailRegEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

// Defining the field length constants.
const PASSWORD_MIN_LENGTH = 8;
const PASSWORD_MAX_LENGTH = 20;

(function () {
  if (
    emailInput.value.match(emailRegEx) &&
    passwordInput.value.length >= PASSWORD_MIN_LENGTH
  ) {
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
      if (
        passwordInput.value.length >= PASSWORD_MIN_LENGTH &&
        passwordInput.value.length <= PASSWORD_MAX_LENGTH
      ) {
        submitBtn.removeAttribute("disabled");
      } else {
        submitBtn.setAttribute("disabled", "");
      }
    } else {
      emailInput.classList.add("error");
      emailError.removeAttribute("hidden");
      emailError.textContent = "Invalid email address.";
      submitBtn.setAttribute("disabled", "true");
    }
  } else {
    emailInput.classList.remove("error");
    emailError.setAttribute("hidden", "true");
  }
};

/**
 * Validates a password input field and updates the UI accordingly.
 * - If the password is within the valid length range.
 * - Enables or disables the submit button based on the validity email field.
 */
const passwordValidator = () => {
  if (passwordInput.value.length > 0) {
    showPassword.removeAttribute("hidden");
    if (
      passwordInput.value.length >= PASSWORD_MIN_LENGTH &&
      passwordInput.value.length <= PASSWORD_MAX_LENGTH
    ) {
      passwordInput.classList.remove("error");
      passwordError.setAttribute("hidden", "true");
      passwordError.textContent = "";
      if (emailInput.value.match(emailRegEx)) {
        submitBtn.removeAttribute("disabled");
      } else {
        submitBtn.setAttribute("disabled", "");
      }
    } else {
      passwordInput.classList.add("error");
      passwordError.removeAttribute("hidden");
      passwordError.textContent = "Password must between 8 to 20 characters.";
      submitBtn.setAttribute("disabled", "true");
    }
  } else {
    passwordInput.classList.remove("error");
    passwordError.setAttribute("hidden", "true");
    showPassword.setAttribute("hidden", "");
  }
};

/**
 * Toggles the visibility of the password input
 * and updates the visibility icon.
 */
const checkPassword = () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPassword.innerHTML = `<i class="bi bi-eye-slash me-1"></i>hide`;
  } else {
    passwordInput.type = "password";
    showPassword.innerHTML = `<i class="bi bi-eye me-1"></i>show`;
  }
};

emailInput.addEventListener("input", emailValidator);
passwordInput.addEventListener("input", passwordValidator);
showPassword.addEventListener("click", checkPassword);
