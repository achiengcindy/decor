'use strict';

/*
 * Open the drawer when the menu ison is clicked.
 */

var menu = document.querySelector('#menu');
var main = document.querySelector('main');
var drawer = document.querySelector('.nav');

menu.addEventListener('click', function (e) {
  drawer.classList.toggle('open');
  e.stopPropagation();
});

main.addEventListener('click', function () {
  drawer.classList.remove('open');
});

function myFunction(x) {
  x.classList.toggle("change");
}

// if ('serviceWorker' in navigator) {
//   navigator.serviceWorker.register('/sw.js', {
//     scope: '/'
//   })
//     .then(function (reg) {
//       if (!navigator.serviceWorker.controller) {
//         return;
//       }
//       // there is updated service worker ready and waiting to to take over
//       if (reg.waiting) {
//         updateReady(reg.waiting)
//         return;
//       }
//       // there is update on the way. Although may be  be thrown away if installation fails we will listen to the stat

//       if (reg.installing) {
//         trackInstalling(reg.installing)
//         return;
//       }

//       reg.addEventListener('updatefound', function () {
//         trackInstalling(reg.installing)
//       });
//     });
//   console.log("service worker registered?");
// }
// function prepareDocument() {
//   jQuery("form#search").submit(function () {
//     text = jQuery("#id_q").val();
//     if (text == "" || text == "Search") {
//       // if empty, pop up alert
//       alert("Enter a search term.");
//       // halt submission of form
//       return false;
//     }
//   });
// }
// jQuery(document).ready(prepareDocument);


function userAction(evt, userChoice) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(userChoice).style.display = "block";
  evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();