"use-strict";

// Get references to input elements from HTML documents.
const usernameInput = document.getElementById("username");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
// Get references to error message elements from HTML documents.
const usernameError = document.getElementById("username-error");
const emailError = document.getElementById("email-error");
const passwordError = document.getElementById("password-error");
// Get references to other UI elements from HTML documents.
const showPassword = document.getElementById("show-password");
const submitBtn = document.getElementById("submit");

// RegEx pattern string for user email input.
const emailRegEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

// Defining the field length constants.
const USERNAME_MIN_LENGTH = 6;
const USERNAME_MAX_LENGTH = 30;
const PASSWORD_MIN_LENGTH = 8;
const PASSWORD_MAX_LENGTH = 20;

/**
 * Validates the username input field and updates the UI accordingly.
 * - If the username is within the valid length range.
 * - Enables or disables the submit button based on the validity
 * - of the email, password, and username.
 */
const usernameValidator = () => {
  if (
    usernameInput.value.length >= USERNAME_MIN_LENGTH &&
    usernameInput.value.length <= USERNAME_MAX_LENGTH
  ) {
    usernameInput.classList.remove("error");
    usernameError.setAttribute("hidden", "");
    usernameError.textContent = "";
    if (
      emailInput.value.match(emailRegEx) &&
      passwordInput.value.length >= PASSWORD_MIN_LENGTH &&
      passwordInput.value.length <= PASSWORD_MAX_LENGTH
    ) {
      submitBtn.removeAttribute("disabled");
    } else {
      submitBtn.setAttribute("disabled", "");
    }
  } else {
    usernameInput.classList.add("error");
    usernameError.removeAttribute("hidden");
    usernameError.textContent = "Username must between 6 to 30 characters.";
    submitBtn.setAttribute("disabled", "");
  }
};

/**
 * Validates the email input field and updates the UI accordingly.
 * - If the email is valid, it checks the username and password inputs field also.
 * - Enables or disables the submit button based on the validity
 * - of the username, password, and email.
 */
const emailValidator = () => {
  if (emailInput.value.match(emailRegEx)) {
    emailInput.classList.remove("error");
    emailError.setAttribute("hidden", "");
    emailError.textContent = "";
    if (
      usernameInput.value.length >= USERNAME_MIN_LENGTH &&
      usernameInput.value.length <= USERNAME_MAX_LENGTH &&
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
    submitBtn.setAttribute("disabled", "");
  }
};

/**
 * Validates the password input field and updates the UI accordingly.
 * - If the password is within the valid length range.
 * - Enables or disables the submit button based on the validity
 * - of the username, email, and password field.
 */
const passwordValidator = () => {
  if (passwordInput.value.length > 0) {
    showPassword.removeAttribute("hidden");
    if (
      passwordInput.value.length >= PASSWORD_MIN_LENGTH &&
      passwordInput.value.length <= PASSWORD_MAX_LENGTH
    ) {
      passwordInput.classList.remove("error");
      passwordError.setAttribute("hidden", "");
      passwordError.textContent = "";
      if (
        usernameInput.value.length >= USERNAME_MIN_LENGTH &&
        usernameInput.value.length <= USERNAME_MAX_LENGTH &&
        emailInput.value.match(emailRegEx)
      ) {
        submitBtn.removeAttribute("disabled");
      } else {
        submitBtn.setAttribute("disabled", "");
      }
    } else {
      passwordInput.classList.add("error");
      passwordError.removeAttribute("hidden");
      passwordError.textContent = "Password must between 8 to 20 characters.";
      submitBtn.setAttribute("disabled", "");
    }
  } else {
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

usernameInput.addEventListener("input", usernameValidator);
emailInput.addEventListener("input", emailValidator);
passwordInput.addEventListener("input", passwordValidator);
showPassword.addEventListener("click", checkPassword);
