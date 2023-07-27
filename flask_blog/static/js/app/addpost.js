"use strict";

const postTitle = document.getElementById("title");
const postSubTitle = document.getElementById("subtitle");

const titleLength = document.getElementById("title-length");
const subTitleLength = document.getElementById("subtitle-length");

const submitButton = document.getElementById("submit");

const titleTextLimit = 100;
const subtitleTextLimit = 150;

postTitle.addEventListener("input", () => {
  titleLength.textContent = `${postTitle.value.length} / ${titleTextLimit}`;
  if (postTitle.value.length == 0) {
    titleLength.setAttribute("hidden", "");
  } else {
    titleLength.removeAttribute("hidden");
  }
});

postSubTitle.addEventListener("input", () => {
  subTitleLength.textContent = `${postSubTitle.value.length} / ${subtitleTextLimit}`;
  if (postSubTitle.value.length == 0) {
    subTitleLength.setAttribute("hidden", "");
  } else {
    subTitleLength.removeAttribute("hidden");
  }
});

const coverImagePreview = (input, element) => {
  let selectedFile = input.files[0];
  let fileReader = new FileReader();
  let image = document.querySelector(element);

  image.title = selectedFile.name;
  fileReader.onload = (input) => {
    document.getElementById("show-cover-image").removeAttribute("hidden");
    image.src = input.target.result;
  };
  fileReader.readAsDataURL(selectedFile);
};
