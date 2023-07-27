"use strict";

// window.addEventListener("DOMContentLoaded", () => {
//   let scrollPos = 0;
//   const mainNav = document.getElementById("mainNav");
//   const headerHeight = mainNav.clientHeight;
//   window.addEventListener("scroll", function () {
//     const currentTop = document.body.getBoundingClientRect().top * -1;
//     if (currentTop < scrollPos) {
//       // Scrolling Up
//       if (currentTop > 0 && mainNav.classList.contains("is-fixed")) {
//         mainNav.classList.add("is-visible");
//       } else {
//         mainNav.classList.remove("is-visible", "is-fixed");
//       }
//     } else {
//       // Scrolling Down
//       mainNav.classList.remove(["is-visible"]);
//       if (
//         currentTop > headerHeight &&
//         !mainNav.classList.contains("is-fixed")
//       ) {
//         mainNav.classList.add("is-fixed");
//       }
//     }
//     scrollPos = currentTop;
//   });
// });

const darkLighttheme = () => {
  if (window.localStorage.getItem("theme") === "dark") {
    if (document.getElementById("theme-mode")) {
      document.getElementById(
        "theme-mode"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high-fill me-2"></i>Light Mode`;
    }
    if (document.getElementById("theme")) {
      document.getElementById(
        "theme"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high-fill"></i>`;
    }
  } else {
    if (document.getElementById("theme-mode")) {
      document.getElementById(
        "theme-mode"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high me-2"></i>Dark Mode`;
    }
    if (document.getElementById("theme")) {
      document.getElementById(
        "theme"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high"></i>`;
    }
  }
};

darkLighttheme();

const themeToggle = () => {
  if (window.localStorage.getItem("theme") === "light") {
    document.getElementsByTagName("html")[0].classList.add("dark");
    window.localStorage.setItem("theme", "dark");
    if (document.getElementById("theme-mode")) {
      document.getElementById(
        "theme-mode"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high-fill me-2"></i>Light Mode`;
    }
    if (document.getElementById("theme")) {
      document.getElementById(
        "theme"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high-fill"></i>`;
    }
  } else {
    document.getElementsByTagName("html")[0].classList.remove("dark");
    window.localStorage.setItem("theme", "light");
    if (document.getElementById("theme-mode")) {
      document.getElementById(
        "theme-mode"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high me-2"></i>Dark Mode`;
    }
    if (document.getElementById("theme")) {
      document.getElementById(
        "theme"
      ).children[0].innerHTML = `<i class="bi bi-brightness-high"></i>`;
    }
  }
};
