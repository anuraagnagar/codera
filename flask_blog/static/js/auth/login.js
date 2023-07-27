"use-strict";

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const submitBtn = document.getElementById("submit");

const emailError = document.getElementById("email-error");
const showPassword = document.getElementById("show");

const regEx =
  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const emailValidator = () => {
  if (emailInput.value.match(regEx)) {
    emailInput.classList.remove("error");
    emailError.setAttribute("hidden", "");
    emailError.textContent = "";
    submitBtn.removeAttribute("disabled");
  } else {
    emailInput.classList.add("error");
    emailError.removeAttribute("hidden");
    emailError.textContent = "Invalid email address.";
    submitBtn.setAttribute("disabled", "");
  }
};

passwordInput.addEventListener("input", () => {
  if (passwordInput.value.length > 0) {
    showPassword.removeAttribute("hidden");
  } else {
    showPassword.setAttribute("hidden", "");
  }
});

const checkPassword = () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPassword.innerHTML = `<i class="bi bi-eye-slash me-1 fs-4-150"></i>hide`;
  } else {
    passwordInput.type = "password";
    showPassword.innerHTML = `<i class="bi bi-eye me-1 fs-4-150"></i>show`;
  }
};

emailInput.addEventListener("input", emailValidator);
showPassword.addEventListener("click", checkPassword);
