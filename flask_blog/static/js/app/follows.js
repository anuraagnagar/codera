"use strict";

// Get elements references to DOM object.
const showFollows = document.getElementById("show-follows");
const followButton = document.getElementById("follow-btn");

const followUser = async () => {
  const URL = `/follows`;

  // Get user ID and CSRF token from data attributes
  const userId = followButton.dataset.userId;
  const csrfTokenId = followButton.dataset.csrfTokenId;

  // Check if user ID and CSRF token are available
  if (userId && csrfTokenId) {
    followButton.setAttribute("disabled", "");
    try {
      // Send a POST request to the server using fetch.
      let response = await fetch(URL, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": csrfTokenId,
        },
        body: JSON.stringify({
          user_id: userId,
        }),
      });

      if (followButton.hasAttribute("disabled")) {
        followButton.removeAttribute("disabled");
      }

      // response not 200 throw an error.
      if (!response.ok) {
        throw Error("Something went wrong!");
      }

      // Parse the response as JSON.
      let data = await response.json();

      // Display the updated follow button.
      displayFollowing(data);
    } catch (error) {
      console.error(error);
    }
  }
};

const displayFollowing = (data) => {
  if (data && data.status === "Following") {
    followButton.classList.replace("btn-primary", "btn-outline-light");
    followButton.innerText = String(data.status).toUpperCase();
    showFollows.innerText = data.followers;
  } else {
    followButton.classList.replace("btn-outline-light", "btn-primary");
    followButton.innerText = String(data.status).toUpperCase();
    showFollows.innerText = data.followers;
  }
};

// Added event-listener to the follow user button.
followButton.addEventListener("click", followUser);
