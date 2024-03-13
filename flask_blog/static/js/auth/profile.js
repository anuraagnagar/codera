"use strict";

const submitBtn = document.getElementById("submit");
const submitBtnBody = document.getElementById("submit-btn-body");

/**
 * Enable a submit button by removing the "disabled" attribute
 * when some changes in form fields.
 **/
const changeHandler = () => {
  submitBtn.removeAttribute("disabled");
  submitBtnBody.style.position = "sticky";
  submitBtnBody.style.bottom = "0";
  submitBtnBody.style.backgroundColor = "inherit";
  submitBtnBody.style.margin = "2px";
};

/**
 * Set the loader element to hide and update
 * the image source.
 **/
const setImage = (input, image, element) => {
  element.style.display = "none";
  image.src = input.target.result;
};

/**
 * Display an image preview while loading and set
 * the image source.
 **/
const ImagePreview = (input, element) => {
  let loadingTime = 2000;
  let selectedFile = input.files[0];
  let fileReader = new FileReader();
  let image = document.querySelector(element);

  try {
    // Set the image title to the selected file name.
    image.title = selectedFile.name;

    fileReader.onload = (input) => {
      // Clear the image source before loading.
      image.src = "";

      // Display the loader element while loading.
      let loaderElement = document.querySelector(`${element}-loader`);
      loaderElement.style.display = "flex";

      // Delay setting the loader and image source for a smoother experience.
      setTimeout(() => setImage(input, image, loaderElement), loadingTime);
    };

    // Read the selected file as a data URL.
    fileReader.readAsDataURL(selectedFile);
  } catch (err) {
    console.log(err);
  }
};
