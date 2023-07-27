"use-strict";

const inputOtp = document.getElementById("security_code");
const verifyOtp = document.getElementById("verify-otp");

const submitBtn = document.getElementById("submit");

const checkInput = (input) => {
  const event = input ? input : window.event;
  const charCode = event.which ? event.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
    return false;
  }
  return true;
};

const ValidateOTP = () => {
  if (inputOtp.value.length === 6) {
    submitBtn.removeAttribute("disabled");
  } else {
    submitBtn.setAttribute("disabled", "");
  }
};

inputOtp.addEventListener("input", ValidateOTP);
