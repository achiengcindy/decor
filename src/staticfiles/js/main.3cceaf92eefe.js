    /*
     * Open the drawer when the menu ison is clicked.
     */
    var menu = document.querySelector('#menu');
    var main = document.querySelector('main');
    var drawer = document.querySelector('.nav-wrapper');

    menu.addEventListener('click', function(e) {
      drawer.classList.toggle('open');
      e.stopPropagation();
    });
    main.addEventListener('click', function() {
      drawer.classList.remove('open');
    });


    function prepareDocument(){
      jQuery("form#search").submit(function(){
        text = jQuery("#id_q").val();
        if (text == "" || text == "Search"){
        // if empty, pop up alert
        alert("Enter a search term.");
        // halt submission of form
        return false;
        }
        });
      }
      jQuery(document).ready(prepareDocument);


