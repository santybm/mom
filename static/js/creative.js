/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    })

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Fit Text Plugin for Main Header
    $("h1").fitText(
        1.2, {
            minFontSize: '35px',
            maxFontSize: '65px'
        }
    );

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })
    
    $(function(){
        $('#searchButton').click(function(){
            $('#searchButton').css({
                'opacity': '1',
                'height': '90px',
                'width': '90px',
                'border-radius': '90px'  
            })
            $('#groceryListButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
                                                                $('#uploadButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
        });
    });
    
        $(function(){
        $('#groceryListButton').click(function(){
            $('#groceryListButton').css({
                'opacity': '1',
                'height': '90px',
                'width': '90px',
                'border-radius': '90px'  
            })
            $('#searchButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
                                                                $('#uploadButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
        });
    });
    
        $(function(){
        $('#uploadButton').click(function(){
            $('#uploadButton').css({
                'opacity': '1',
                'height': '90px',
                'width': '90px',
                'border-radius': '90px'  
            })
                                                                $('#groceryListButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
                                                                $('#searchButton').css({
                'opacity': '0.5',
                'height': '80px',
                'width': '80px',
                'border-radius': '80px'  
            })
        });
    });
    

    // Initialize WOW.js Scrolling Animations
    new WOW().init();

}) (jQuery); // End of use strict
