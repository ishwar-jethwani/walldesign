/**
*
* -----------------------------------------------------------------------------
*
* Template : Archtek - Architecture Consulting Business HTML Template
* Author : reacthemes
* Author URI : https://reactheme.com/ 
*
* -----------------------------------------------------------------------------
*
**/
(function($) {
	"use strict";
    // sticky menu
    var header = $('.menu-sticky');
    var win = $(window);

    win.on('scroll', function() {
       var scroll = win.scrollTop();
       if (scroll < 1) {
           header.removeClass("sticky");
       } else {
           header.addClass("sticky");
       }

        $("section").each(function() {
        var elementTop = $(this).offset().top - $('#rs-header').outerHeight();
            if(scroll >= elementTop) {
                $(this).addClass('loaded');
            }
        });
    });
	
    //window load
    $(window).on( 'load', function() {
        $("#loading").delay(1500).fadeOut(500);
        $("#loading-center").on( 'click', function() {
        $("#loading").fadeOut(500);
        })
    })
    
    //slider
    var slidercarousel = $('.slider-carousel');
    if(slidercarousel.length){
        $(".slider-carousel").owlCarousel({
            margin: 0,
            nav: false,
            navText:[
                "<i class='fa fa-angle-left'></i>",
                "<i class='fa fa-angle-right'></i>"
            ],
            loop: true,
            dots: true,
            mouseDrag: false,
            items: 1,
            autoplay: true,
            animateOut: 'fadeOut',
            autoplayTimeout: 5000,
            autoplayHoverPause: false,
            responsiveClass: true
        });
    }

    var drowbd = $('.drowbd');
    if(drowbd.length){
        $(document).ready(function(){
            setTimeout(function(){ $('.drowbd').addClass('draw'); },3000); 
        });
    }

    // Slider Custom jQuery
    var nivo_slider = $('#nivoSlider');
        if(nivo_slider.length){
        $('#nivoSlider').nivoSlider({
            effect: 'random',
            slices: 15,
            boxCols: 8,
            boxRows: 4,
            animSpeed: 600,
            pauseTime: 5000000000,
            startSlide: 0,
            directionNav: true,
            controlNavThumbs: false,
            pauseOnHover: true,
            manualAdvance: false
        });
    }

    //Testimonial
    if ($('.testimonial-style1').length) {
        $('.testimonial-style1').slick({
            autoplay: true,
            infinite: true,
            centerMode: false,
            arrows: false,
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            responsive: [
               {
                 breakpoint: 992,
                 settings: {
                   slidesToShow: 1,
                 }
               },
               {
                   breakpoint: 575,
                   settings: {
                     slidesToShow: 1,
                   }
               }
           ]
       });
    }

    //Project Slider
    if ($('.project-style1').length) {
        $('.project-style1').slick({
            autoplay: true,
            infinite: true,
            centerMode: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            responsive: [
               {
                 breakpoint: 992,
                 settings: {
                   slidesToShow: 1,
                 }
               },
               {
                   breakpoint: 575,
                   settings: {
                     slidesToShow: 1,
                   }
               }
           ]
       });
    }

    if ($('.team-style1').length) {
        $('.team-style1').slick({
           autoplay: true,
           autoplaySpeed: 2000,
           centerMode: true,
           speed: 2000,
           slidesToShow: 3,
           slidesToScroll: 1,
           arrows: false,
           dots: false,
           responsive: [
               {
                breakpoint: 1200,
                 settings: {
                   slidesToShow: 2,
                   slidesToScroll: 1,
                 }
               },
               {
                   breakpoint: 768,
                   settings: {
                     slidesToShow: 1,
                     slidesToScroll: 1,
                   }
               }
           ]
       });
    }  

    if ($('.team-style2').length) {
        $('.team-style2').slick({
           autoplay: true,
           autoplaySpeed: 2000,
           centerMode: true,
           speed: 2000,
           slidesToShow: 4,
           slidesToScroll: 1,
           arrows: false,
           dots: false,
           responsive: [
               {
                breakpoint: 1200,
                 settings: {
                   slidesToShow: 2,
                   slidesToScroll: 1,
                 }
               },
               {
                   breakpoint: 768,
                   settings: {
                     slidesToShow: 1,
                     slidesToScroll: 1,
                   }
               }
           ]
       });
    } 
    if ($('.blog-style1').length) {
        $('.blog-style1').slick({
           autoplay: true,
           autoplaySpeed: 2000,
           centerMode: true,
           speed: 2000,
           slidesToShow: 3,
           slidesToScroll: 1,
           arrows: false,
           dots: false,
           responsive: [
               {
                breakpoint: 1200,
                 settings: {
                   slidesToShow: 2,
                   slidesToScroll: 1,
                 }
               },
               {
                   breakpoint: 768,
                   settings: {
                     slidesToShow: 1,
                     slidesToScroll: 1,
                   }
               }
           ]
       });
    }  

    //CountDown Timer
    var CountTimer = $('.CountDownTimer');
    if(CountTimer.length){ 
        $(".CountDownTimer").TimeCircles({
            fg_width: 0.030,
            bg_width: 0.8,
            circle_bg_color: "#eeeeee",
            circle_fg_color: "#eeeeee",
            time: {
                Days:{
                    color: "#032390"
                },
                Hours:{
                    color: "#032390"
                },
                Minutes:{
                    color: "#032390"
                },
                Seconds:{
                    color: "#032390"
                }
            }
        }); 
    }

    var pieChart = $('.chart');
    if(pieChart.length) {
        $('.chart').easyPieChart({
            size: 120,
            barColor: "#baa08f",
            scaleLength: 0,
            lineWidth: 8,
            trackColor: "#eff2f6",
            lineCap: "circle",
            animate: 2000,
        });
    }
    

   // onepage nav
   var navclose = $('#onepage-menu');
   if(navclose.length){
       $(".nav-menu li a").on("click", function () {
           if ($(".showhide").is(":visible")) {
               $(".showhide").trigger("click");
           }
       });
       if ($.fn.onePageNav) {
           $(".nav-menu").onePageNav({
               currentClass: "active-menu"
           });
        }
    }
    var searchParent = $('.search-parent');
    if(searchParent.length){ 
        $( ".search-parent" ).on( "click", function() {
          $( this).toggleClass( "open_add_class", 1000 );
        });
    }

    // collapse hidden  
     var navMain = $(".navbar-collapse");
     navMain.on("click", "a:not([data-toggle])", null, function () {
         navMain.collapse('hide');
     });  

    // wow init
    new WOW().init();
    
    // image loaded portfolio init
    var gridfilter = $('.grid');
        if(gridfilter.length){
        $('.grid').imagesLoaded(function() {
            $('.gridFilter').on('click', 'button', function() {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({
                    filter: filterValue
                });
                console.log(filterValue)
            });
            var $grid = $('.grid').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry: {
                    columnWidth: '.grid-item',
                }
            });
        });
    }   

    // project Filter
    if ($('.gridFilter button').length) {
        var projectfiler = $('.gridFilter button');
            if(projectfiler.length){
            $('.gridFilter button').on('click', function(event) {
                $(this).siblings('.active').removeClass('active');
                $(this).addClass('active');
                event.preventDefault();
            });
        }
    }

    $('.collapse.show').prev('.card-header').addClass('active');
    $('#accordion, #bs-collapse, #accordion1')
    .on('show.bs.collapse', function (a) {
        $(a.target).prev('.card-header').addClass('active');
    })
    .on('hide.bs.collapse', function (a) {
        $(a.target).prev('.card-header').removeClass('active');
    });
    
    // magnificPopup init
    var imagepopup = $('.image-popup');
    if(imagepopup.length){
        $('.image-popup').magnificPopup({
            type: 'image',
            callbacks: {
                beforeOpen: function() {
                   this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure animated zoomInDown');
                }
            },
            gallery: {
                enabled: true
            }
        });
    }

    // Get a quote popup
    var popupquote = $('.popup-quote');
    if(popupquote.length){
        $('.popup-quote').magnificPopup({
            type: 'inline',
            preloader: false,
            focus: '#qname',
            removalDelay: 500,
            callbacks: {
                beforeOpen: function() {
                    this.st.mainClass = this.st.el.attr('data-effect');
                    if(win.width() < 800) {
                        this.st.focus = false;
                    } else {
                        this.st.focus = '#qname';
                    }
                }
            }
        });
    }
    
   //preloader
     $(window).on( 'load', function() {
         $("#archtek-load").delay(0).fadeOut(500);
         $(".archtek-loader").delay(0).fadeOut(500);
         
         if($(window).width() < 992) {
             $('.rs-menu').css('height', '0');
             $('.rs-menu').css('opacity', '0');
             $('.rs-menu').css('z-index', '-1');
             $('.rs-menu-toggle').on( 'click', function(){
                 $('.rs-menu').css('opacity', '1');
                 $('.rs-menu').css('z-index', '1');
             });
         }
     })

    //Videos popup jQuery 
    var popupvideos = $('.popup-videos, .popup-border');
    if(popupvideos.length){
        $('.popup-videos, .popup-border').magnificPopup({
            disableOn: 10,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        }); 
    }

    /*-------------------------------------
        OwlCarousel
    -------------------------------------*/
    $('.rs-carousel').each(function() {
        var owlCarousel = $(this),
        loop = owlCarousel.data('loop'),
        items = owlCarousel.data('items'),
        margin = owlCarousel.data('margin'),
        stagePadding = owlCarousel.data('stage-padding'),
        autoplay = owlCarousel.data('autoplay'),
        autoplayTimeout = owlCarousel.data('autoplay-timeout'),
        smartSpeed = owlCarousel.data('smart-speed'),
        dots = owlCarousel.data('dots'),
        nav = owlCarousel.data('nav'),
        navSpeed = owlCarousel.data('nav-speed'),
        xsDevice = owlCarousel.data('mobile-device'),
        xsDeviceNav = owlCarousel.data('mobile-device-nav'),
        xsDeviceDots = owlCarousel.data('mobile-device-dots'),
        smDevice = owlCarousel.data('ipad-device'),
        smDeviceNav = owlCarousel.data('ipad-device-nav'),
        smDeviceDots = owlCarousel.data('ipad-device-dots'),
        smDevice2 = owlCarousel.data('ipad-device2'),
        smDeviceNav2 = owlCarousel.data('ipad-device-nav2'),
        smDeviceDots2 = owlCarousel.data('ipad-device-dots2'),
        mdDevice = owlCarousel.data('md-device'),
        centerMode = owlCarousel.data('center-mode'),
        HoverPause = owlCarousel.data('hoverpause'),
        mdDeviceNav = owlCarousel.data('md-device-nav'),
        mdDeviceDots = owlCarousel.data('md-device-dots');
        owlCarousel.owlCarousel({
            loop: (loop ? true : false),
            items: (items ? items : 4),
            lazyLoad: true,
            center: (centerMode ? true : false),
            autoplayHoverPause: (HoverPause ? true : false),
            margin: (margin ? margin : 0),
            //stagePadding: (stagePadding ? stagePadding : 0),
            autoplay: (autoplay ? true : false),
            autoplayTimeout: (autoplayTimeout ? autoplayTimeout : 1000),
            smartSpeed: (smartSpeed ? smartSpeed : 250),
            dots: (dots ? true : false),
            nav: (nav ? true : false),
            navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>"],
            navSpeed: (navSpeed ? true : false),
            responsiveClass: true,
            responsive: {
                0: {
                    items: (xsDevice ? xsDevice : 1),
                    nav: (xsDeviceNav ? true : false),
                    dots: (xsDeviceDots ? true : false),
                    center: false,
                },
                768: {
                    items: (smDevice2 ? smDevice2 : 2),
                    nav: (smDeviceNav2 ? true : false),
                    dots: (smDeviceDots2 ? true : false),
                    center: false,
                },
                992: {
                    items: (smDevice ? smDevice : 3),
                    nav: (smDeviceNav ? true : false),
                    dots: (smDeviceDots ? true : false),
                    center: false,
                },
                1200: {
                    items: (mdDevice ? mdDevice : 4),
                    nav: (mdDeviceNav ? true : false),
                    dots: (mdDeviceDots ? true : false),
                }
            }
        });
    });

    // Skill bar 
    var skillbar = $('.skillbar');
    if(skillbar.length) {
        $('.skillbar').skillBars({  
            from: 0,    
            speed: 4000,    
            interval: 100,  
            decimals: 0,    
        });
    }

		
    // Counter Up
    var counter_Up = $('.rs-count');
    if(counter_Up.length) {  
        $('.rs-count').counterUp({
            delay: 20,
            time: 2000
        });
    }
    
    // scrollTop init	
    var totop = $('#scrollUp');    
    win.on('scroll', function() {
        if (win.scrollTop() > 150) {
            totop.fadeIn();
        } else {
            totop.fadeOut();
        }
    });
    totop.on('click', function() {
        $("html,body").animate({
            scrollTop: 0
        }, 500)
    });

    //canvas menu
    var navexpander = $('#nav-expander, #nav-expander2');
    if(navexpander.length){
        $('#nav-expander, #nav-expander2, #nav-close, #nav-close2, .offwrap').on('click',function(e){
            e.preventDefault();
            $('body').toggleClass('nav-expanded');
        });
    }

    // View Course
    $('.course-view-part .view-icons .view-grid').on('click',function(e){
        e.preventDefault();
        $('.rs-popular-courses').removeClass('list-view');
    });
    $('.course-view-part .view-icons .view-list').on('click',function(e){
        e.preventDefault();
        $('.rs-popular-courses').addClass('list-view');
    });
    
	
    // categories btn
    $('.cat-menu-inner').hide();
    $('.cat-btn').on('click',function(){
        $('.cat-menu-inner').slideToggle();
    })

    var tilt = $('.js-tilt');
    if(tilt.length) {
        const tilt = $('.js-tilt').tilt();
    }

    $( ".plus-team" ).on( "click", function( event ) {
        $(this).toggleClass("active_social");
    });
    
    $( ".cls-maker" ).on( "click", function( event ) {
        $(this).toggleClass("active_social");
    });

    /******** Mobile Menu Start ********/
    
    $('.mobile-navbar-menu a').each(function(){
        var href = $(this).attr("href");
        if(href ="#"){
            $(this).addClass('hash');
        }else{
            $(this).removeClass('hash');
        }
    });

    $.fn.menumaker = function(options) {
      var mobile_menu = $(this), settings = $.extend({
        format: "dropdown",
        sticky: false
      }, options);

        return this.each(function() {
        mobile_menu.find('li ul').parent().addClass('has-sub');
        var multiTg = function() {
            mobile_menu.find(".has-sub").prepend('<span class="submenu-button"><em></em></span>');
            mobile_menu.find(".hash").parent().addClass('hash-has-sub');
            mobile_menu.find('.submenu-button').on('click', function() {
                $(this).toggleClass('submenu-opened');
                if ($(this).siblings('ul').hasClass('open-sub')) {
                    $(this).siblings('ul').removeClass('open-sub').hide('fadeIn');
                    $(this).siblings('ul').hide('fadeIn');                                     
                }
                else {
                    $(this).siblings('ul').addClass('open-sub').hide('fadeIn');
                    $(this).siblings('ul').slideToggle().show('fadeIn');
                }
            });
        };

        if (settings.format === 'multitoggle') multiTg();
        else mobile_menu.addClass('dropdown');
        if (settings.sticky === true) mobile_menu.css('position', 'fixed');
       var resizeFix = function() {
            if ($( window ).width() > 991) {
                mobile_menu.find('ul').show('fadeIn');
                mobile_menu.find('ul.sub-menu').hide('fadeIn');
            }          
        };
        resizeFix();
        return $(window).on('resize', resizeFix);
        });
    };

    $(document).ready(function(){
        $("#mobile-navbar-menu").menumaker({
        format: "multitoggle"
        });
    });

     
    var beforeandafter = $('.beforeandafter');
    if(beforeandafter.length){
        bafinstance = new ddbeforeandafter({
            wrapperid: 'rscomprision',
        });
    }

})(jQuery);