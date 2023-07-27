"use strict";

// -=-=-=-=  Add dark | light theme mode. -=-=-=-=- //
const setTheme = () => {
  if (window.localStorage.getItem("theme")) {
    if (window.localStorage.getItem("theme") === "dark") {
      document.getElementsByTagName("html")[0].classList.add("dark");
    } else {
      document.getElementsByTagName("html")[0].classList.remove("dark");
    }
  } else {
    window.localStorage.setItem("theme", "dark");
    document.getElementsByTagName("html")[0].classList.add("dark");
  }
};

setTheme();
