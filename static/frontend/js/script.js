(function ($) {
    "use strict";

    /*=== Menu Fixed ===*/
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 50) {
            $('.vHeaderNav').addClass('navbar-fixed');
        } else {
            $('.vHeaderNav').removeClass('navbar-fixed');
        }
    });
    /*=== Menu Fixed ===*/

    /*=== meanmenu===*/
    jQuery('.vMenu').meanmenu({
        meanScreenWidth: "1200",
        meanMenuContainer: '.mobile-menu-active',
        meanRevealPosition: "right",
    });
    /*=== meanmenu===*/

    /*=== slider ===*/
    $('.vSliderActive').owlCarousel({
        loop: true,
        nav: true,
        autoplay: true,
        autoplayTimeout: 15000,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            767: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })

    /*=== slider ===*/
    /*=== video play ===*/
    $(document).ready(function () {
        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,

            fixedContentPos: false
        });
    });
    /*=== video play ===*/

})(jQuery);	