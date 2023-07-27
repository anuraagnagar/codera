"use strict";

const likes = document.getElementById("likes");
const likeButton = document.getElementById("like-button") || "";

const saves = document.getElementById("saves");
const saveButton = document.getElementById("save-button") || "";

const commentLength = document.getElementById("comment-length") || "";
const commentInput = document.getElementById("content") || "";
const commentBtn = document.getElementById("submit-comment") || "";

const maxCommentLength = 500;

const postComment = () => {
  if (commentInput.value.length <= maxCommentLength && commentInput.value.length >= 3) {
    commentBtn.removeAttribute("disabled");
    commentInput.classList.remove("error");
  } else {
    commentBtn.setAttribute("disabled", "true");
    commentInput.classList.add("error");
  }
  commentLength.textContent = commentInput.value.length;
};

const displayLikes = (data) => {
  try {
    if (data.status === "like") {
      likes.textContent = data.likes;
      likeButton.innerHTML = `<i class="bi bi-heart-fill text-red"></i>`;
    } else {
      likes.textContent = data.likes;
      likeButton.innerHTML = `<i class="bi bi-heart"></i>`;
    }
  } catch (error) {
    console.error(data.error);
  }
};

const likePost = async (postId, csrfToken) => {
  let URL = `/like-post/${postId}`;

  try {
    if (postId && csrfToken) {
      await fetch(URL, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": csrfToken,
        },
      })
        .then((res) => res.json())
        .then((data) => displayLikes(data));
    }
  } catch (error) {
    console.error("Something went wrong, ", error);
  }
};

const displaySaves = (data) => {
  try {
    if (data.status === "save") {
      saves.textContent = data.saves;
      saveButton.innerHTML = `<i class="bi bi-bookmarks-fill text-primary mx-1"></i>`;
    } else {
      saves.textContent = data.saves;
      saveButton.innerHTML = `<i class="bi bi-bookmarks mx-1"></i>`;
    }
  } catch (error) {
    console.log(data.error);
  }
};

const savePost = async (postId, csrfToken) => {
  let URL = `/saved/posts`;

  try {
    if (postId && csrfToken) {
      await fetch(URL, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": csrfToken,
        },
        body: JSON.stringify({
          post_id: postId,
        }),
      })
        .then((res) => res.json())
        .then((data) => displaySaves(data));
    }
  } catch (error) {
    console.error("Something went wrong, ", error);
  }
};
