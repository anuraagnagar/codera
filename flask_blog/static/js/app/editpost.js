"use strict";

const postTitle = document.getElementById("title");
const postSubtitle = document.getElementById("subtitle");
const titleLength = document.getElementById("title-length");
const subtitleLength = document.getElementById("subtitle-length");

const submitBtn = document.getElementById("submit");
const titleTextLimit = 100;
const subtitleTextLimit = 150;

titleLength.textContent = postTitle.value.length + "/" + titleTextLimit;
subtitleLength.textContent =
  postSubtitle.value.length + "/" + subtitleTextLimit;

const coverImageChange = (input) => {
  let selectedFile = input.files[0];
  let fileReader = new FileReader();
  let coverImage = document.querySelector('#cover-image-show');

  coverImage.title = selectedFile.name;
  fileReader.onload = (input) => {
    document.getElementById("show-cover-image").removeAttribute("hidden");
    coverImage.src = input.target.result;
  };
  fileReader.readAsDataURL(selectedFile);
};