"use-strict";

const usernameInput = document.getElementById("username");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");

const usernameError = document.getElementById("username-error");
const emailError = document.getElementById("email-error");
const passwordError = document.getElementById("password-error");

const showPassword = document.getElementById("show");
const submitBtn = document.getElementById("submit");

const regEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const usernameValidator = () => {
  if (usernameInput.value.length >= 6 && usernameInput.value.length <= 25) {
    usernameInput.classList.remove("error");
    usernameError.setAttribute("hidden", "");
    usernameError.textContent = "";
    if (
      emailInput.value.match(regEx) &&
      passwordInput.value.length >= 8 &&
      passwordInput.value.length <= 15
    ) {
      submitBtn.removeAttribute("disabled");
    } else {
      submitBtn.setAttribute("disabled", "");
    }
  } else {
    usernameInput.classList.add("error");
    usernameError.removeAttribute("hidden");
    usernameError.textContent = "Username must between 6 to 25 character.";
    submitBtn.setAttribute("disabled", "");
  }
};

const emailValidator = () => {
  if (emailInput.value.match(regEx)) {
    emailInput.classList.remove("error");
    emailError.setAttribute("hidden", "");
    emailError.textContent = "";
    if (
      usernameInput.value.length >= 6 &&
      usernameInput.value.length <= 25 &&
      passwordInput.value.length >= 8 &&
      passwordInput.value.length <= 15
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

const passwordValidator = () => {
  if (passwordInput.value.length > 0) {
    showPassword.removeAttribute("hidden");
    if (passwordInput.value.length >= 8 && passwordInput.value.length <= 15) {
      passwordInput.classList.remove("error");
      passwordError.setAttribute("hidden", "");
      passwordError.textContent = "";
      if (
        usernameInput.value.length >= 6 &&
        usernameInput.value.length <= 25 &&
        emailInput.value.match(regEx)
      ) {
        submitBtn.removeAttribute("disabled");
      } else {
        submitBtn.setAttribute("disabled", "");
      }
    } else {
      passwordInput.classList.add("error");
      passwordError.removeAttribute("hidden");
      passwordError.textContent = "Password between 8 to 15 Character.";
      submitBtn.setAttribute("disabled", "");
    }
  } else {
    showPassword.setAttribute("hidden", "");
  }
};

const checkPassword = () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPassword.innerHTML = `<i class="bi bi-eye-slash me-1 fs-4-150"></i>hide`;
  } else {
    passwordInput.type = "password";
    showPassword.innerHTML = `<i class="bi bi-eye me-1 fs-4-150"></i>show`;
  }
};

usernameInput.addEventListener("input", usernameValidator);

emailInput.addEventListener("input", emailValidator);

passwordInput.addEventListener("input", passwordValidator);

showPassword.addEventListener("click", checkPassword);
