"use strict";

const submitBtn = document.getElementById("submit");

const changeHandler = () => {
  if (submitBtn.hasAttribute("disabled")) {
    submitBtn.removeAttribute("disabled");
  }
};

const ImagePreview = (input, element) => {
  let selectedFile = input.files[0];
  let fileReader = new FileReader();
  let image = document.querySelector(element);

  image.title = selectedFile.name;
  fileReader.onload = (input) => {
    image.src = input.target.result;
  };
  fileReader.readAsDataURL(selectedFile);
};
