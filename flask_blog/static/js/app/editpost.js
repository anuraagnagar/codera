"use strict";

const postTitle = document.getElementById("title");
const postSubTitle = document.getElementById("subtitle");

const titleLength = document.getElementById("title-length");
const subTitleLength = document.getElementById("subtitle-length");

const submitBtn = document.getElementById("submit");

const titleTextLimit = 100;
const subtitleTextLimit = 150;

titleLength.textContent = postTitle.value.length;
subTitleLength.textContent = postSubTitle.value.length;

/**
 * Event listener for the post title input field.
 * Displays the character count and hides/shows the character count element.
 */
postTitle.addEventListener("input", () => {
  titleLength.textContent = `${postTitle.value.length}`;

  // If the post title is empty, hide the character count element; otherwise, show it.
  if (postTitle.value.length === 0) {
    titleLength.setAttribute("hidden", "");
  } else {
    titleLength.removeAttribute("hidden");
  }
});

/**
 * Event listener for the post sub-title input field.
 * Displays the character count and hides/shows the character count element.
 */
postSubTitle.addEventListener("input", () => {
  subTitleLength.textContent = `${postSubTitle.value.length}`;

  // If the post title is empty, hide the character count element; otherwise, show it.
  if (postSubTitle.value.length === 0) {
    subTitleLength.setAttribute("hidden", "");
  } else {
    subTitleLength.removeAttribute("hidden");
  }
});

/**
 * Set the source of the target image element 
 * to the loaded image data.
 **/
const setCoverImage = (e, image) => {
  document.getElementById("loader").style.display = "none";
  document.getElementById("show-image").removeAttribute("hidden");
  image.src = e.target.result;
}


/**
 * Display a preview of the selected cover image 
 * with loading animation.
 **/
const coverImageChange = (input, element) => {

  let loadingTime = 2500;
  let selectedFile = input.files[0];
  let fileReader = new FileReader();
  let coverImage = document.querySelector(element);

  coverImage.title = selectedFile.name;

  fileReader.onload = (input) => {
    document.getElementById("show-image").setAttribute("hidden", "");
    document.getElementById("loader").style.display = "flex";
    // Set a timeout to replace the image source with the loaded image after the loadingTime.
    setTimeout(() => setCoverImage(input, coverImage), loadingTime);
  };

  // Read the selected image file as a data URL.
  fileReader.readAsDataURL(selectedFile);
};
