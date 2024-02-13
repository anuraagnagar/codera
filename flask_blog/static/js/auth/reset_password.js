"use strict";

// Get references to input elements from HTML documents.
const passwordOne = document.getElementById("password");
const passwordTwo = document.getElementById("confirm_password");
const passwordError = document.getElementById("error");
const submitBtn = document.getElementById("submit");

const PASSWORD_MIN_LENGTH = 8;
const PASSWORD_MAX_LENGTH = 20;

/**
 * Checks the validity of input passwords and updates the submit button accordingly.
 * - If the passwords do not match, it displays an error message and disables the submit button.
 * - If the passwords match, it enables the submit button.
 */
function checkInput() {
  if (passwordOne.value === passwordTwo.value) {
    passwordError.setAttribute("hidden", "");
    passwordError.innerHTML = "";
    if (
      passwordOne.value.length >= PASSWORD_MIN_LENGTH &&
      passwordOne.value.length <= PASSWORD_MAX_LENGTH &&
      passwordTwo.value.length >= PASSWORD_MIN_LENGTH &&
      passwordTwo.value.length <= PASSWORD_MAX_LENGTH
    ) {
      submitBtn.removeAttribute("disabled");
    } else {
      submitBtn.setAttribute("disabled", "");
    }
  } else {
    passwordError.removeAttribute("hidden");
    passwordError.innerHTML =
      "<i class='bi bi-info-circle me-1'></i> Password field's didn't match.";
    submitBtn.setAttribute("disabled", "");
  }
}
