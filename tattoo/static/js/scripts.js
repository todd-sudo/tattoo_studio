(function ($) {
 "use strict";

	/*----------------------------
	 wow js active
	------------------------------ */
	 new WOW().init();

	/*------------- preloader js --------------*/
	$(window).on('load',function() { // makes sure the whole site is loaded
		$('.preloder-wrap').fadeOut(); // will first fade out the loading animation
		$('.loader').delay(150).fadeOut('slow'); // will fade out the white DIV that covers the website.
		$('body').delay(150).css({'overflow':'visible'})
	})

    // search
	$(".search-wrap ul li a").on("click", function(){
		$(".search-area").addClass("active");
	});
	$(".search-area span.closs-btn ").on("click", function(){
		$(".search-area").removeClass("active");
	});
	// // stickey menu
	$(window).on('scroll',function() {
		var scroll = $(window).scrollTop(),
			mainHeader = $('#sticky-header'),
			mainHeaderHeight = mainHeader.innerHeight();

		// console.log(mainHeader.innerHeight());
		if (scroll > 2) {
			$("#sticky-header").addClass("sticky");
		}else{
			$("#sticky-header").removeClass("sticky");
		}
	});

    // slicknav
	$('ul#navigation').slicknav({
		prependTo:".responsive-menu-wrap"
	});


	// slider-active
	$('.slider-active').owlCarousel({
		smartSpeed:1000,
		margin:0,
		animateOut: 'fadeOut',
		animateIn: 'fadepIn',
		nav:false,
		autoplay:true,
		autoplayTimeout:3000,
		loop:true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			450:{
				items:1
			},
			678:{
				items:1
			},
			1000:{
				items:1
			}
		}
	})

	//slider-area background setting
    function sliderBgSetting() {
        if ($(".slider-area .slider-items").length) {
            $(".slider-area .slider-items").each(function() {
                var $this = $(this);
                var img = $this.find(".slider").attr("src");

                $this.css({
                    backgroundImage: "url("+ img +")",
                    backgroundSize: "cover",
                    backgroundPosition: "center center"
                })
            });
        }
    }

	// slider-active
	$(".slider-active").on('translate.owl.carousel', function(){
		$('.single-slider h2').removeClass('fadeInUp animated').hide();
		$('.single-slider p').removeClass('fadeInUp animated').hide();
		$('.single-slider a').removeClass('fadeInUp animated').hide();
	});

	$(".slider-active").on('translated.owl.carousel', function(){
		$('.owl-item.active .single-slider h2').addClass('fadeInUp animated').show();
		$('.owl-item.active .single-slider p').addClass('slideInUp animated').show();
		$('.owl-item.active .single-slider a').addClass('fadeInUp animated').show();
	});


	/*==========================================================================
        WHEN DOCUMENT LOADING
    ==========================================================================*/
	$(window).on('load', function() {

		sliderBgSetting();

	});

    // Parallax background
    function bgParallax() {
        if ($(".parallax").length) {
            $(".parallax").each(function() {
                var height = $(this).position().top;
                var resize     = height - $(window).scrollTop();
                var parallaxSpeed = $(this).data("speed");
                var doParallax = -(resize / parallaxSpeed);
                var positionValue   = doParallax + "px";
                var img = $(this).data("bg-image");

                $(this).css({
                    backgroundImage: "url(" + img + ")",
                    backgroundPosition: "50%" + positionValue,
                    backgroundSize: "cover",
                });

                if ( window.innerWidth < 768) {
                    $(this).css({
                        backgroundPosition: "center center"
                    });
                }
            });
        }
    }
	$(window).on("scroll", function() {
		bgParallax();
	});


	// // stickey menu
	$(window).on('scroll',function() {
		var scroll = $(window).scrollTop(),
			mainHeader = $('#sticky-header'),
			mainHeaderHeight = mainHeader.innerHeight();

		// console.log(mainHeader.innerHeight());
		if (scroll > 1) {
			$("#sticky-header").addClass("sticky");
		}else{
			$("#sticky-header").removeClass("sticky");
		}
	});

	/*--------------------------
	 scrollUp
	---------------------------- */
	$.scrollUp({
		scrollText: '<i class="flaticon-heart"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});

	/*--
	Magnific Popup
	------------------------*/
	$('.popup').magnificPopup({
		type: 'image',
		gallery:{
			enabled:true
		}

	});

	/* magnificPopup video view */
	$('.video-popup').magnificPopup({
		type: 'iframe',
		gallery:{
			enabled:true
		}
	});

	// counter up
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});

	// test-active
	$('.test-active').owlCarousel({
		smartSpeed:1000,
		margin:0,
		nav:false,
		center:true,
		autoplay:true,
		autoplayTimeout:3000,
		loop:true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			450:{
				items:1
			},
			678:{
				items:1
			},
			1000:{
				items:1
			}
		}
	})
	// brand-active
	$('.brand-active').owlCarousel({
		smartSpeed:1000,
		margin:0,
		nav:false,
		autoplay:true,
		autoplayTimeout:3000,
		loop:true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			450:{
				items:2
			},
			678:{
				items:3
			},
			1000:{
				items:4
			}
		}
	})
	/*-------------------------------------------------------
        blog details
    -----------------------------------------------------*/
    if ($(".about-area,.single-team-area").length) {
        var post = $(".about-area .about-img,.single-team-area .single-team-img");

        post.each(function() {
            var $this = $(this);
            var entryMedia = $this.find("img");
			var entryMediaPic = entryMedia.attr("src");

            $this.css({
                backgroundImage: "url("+ entryMediaPic +")",
                backgroundSize: "cover",
                backgroundPosition: "center center",
            })
        })
    }

    function setTwoColEqHeight($col1, $col2) {
        var firstCol = $col1,
            secondCol = $col2,
            firstColHeight = $col1.innerHeight(),
            secondColHeight = $col2.innerHeight();

        if (firstColHeight > secondColHeight) {
            secondCol.css({
                "height": firstColHeight + 1 + "px"
            })
        } else {
            firstCol.css({
                "height": secondColHeight + 1 + "px"
            })
        }
    }


	$(window).on("load", function() {
		setTwoColEqHeight($(".about-area .about-img,.single-team-area .single-team-img"), $(".about-area .about-wrap,.single-team-area .single-team-wrap"));
	});

    $('.grid').imagesLoaded( function() {

	// filter items on button click
	$('.project-menu').on( 'click', 'button', function() {
    	  var filterValue = $(this).attr('data-filter');
    	  $grid.isotope({ filter: filterValue });
    	});

    	// init Isotope
    	var $grid = $('.grid').isotope({
    	  itemSelector: '.project',
    	  percentPosition: true,
    	  masonry: {
    		// use outer width of grid-sizer for columnWidth
    		columnWidth: '.project',
    	  }
    	});
	});

	$('.project-menu button').on('click', function(event) {
		$(this).siblings('.active').removeClass('active');
		$(this).addClass('active');
		event.preventDefault();
	});

    /*---------------------
	 countdown
	--------------------- */
	$('[data-countdown]').each(function() {
		  var $this = $(this), finalDate = $(this).data('countdown');
		  $this.countdown(finalDate, function(event) {
			$this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hour</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>Min</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>Sec</p></span>'));
		});
	});


	/*-- price range start --*/
	function collision($div1, $div2) {
		var x1 = $div1.offset().left;
		var w1 = 40;
		var r1 = x1 + w1;
		var x2 = $div2.offset().left;
		var w2 = 40;
		var r2 = x2 + w2;

		if (r1 < x2 || x1 > r2) return false;
		return true;
      
    }

	// pricing-slider
	$('#slider').slider({
		range: true,
		min: 0,
		max: 500,
		values: [ 75, 300 ],
		slide: function(event, ui) {
			
			$('.ui-slider-handle:eq(0) .price-range-min').html('$' + ui.values[ 0 ]);
			$('.ui-slider-handle:eq(1) .price-range-max').html('$' + ui.values[ 1 ]);
			$('.price-range-both').html('<i>$' + ui.values[ 0 ] + ' - </i>$' + ui.values[ 1 ] );
			
			//
			
			if ( ui.values[0] == ui.values[1] ) {
				$('.price-range-both i').css('display', 'none');
			} else {
				$('.price-range-both i').css('display', 'inline');
			}
				
				//
				
			if (collision($('.price-range-min'), $('.price-range-max')) == true) {
				$('.price-range-min, .price-range-max').css('opacity', '0');	
				$('.price-range-both').css('display', 'block');		
			} else {
				$('.price-range-min, .price-range-max').css('opacity', '1');	
				$('.price-range-both').css('display', 'none');		
			}
			
		}
	});

	$('.ui-slider-range').append('<span class="price-range-both value"><i>$' + $('#slider').slider('values', 0 ) + ' - </i>' + $('#slider').slider('values', 1 ) + '</span>');

	$('.ui-slider-handle:eq(0)').append('<span class="price-range-min value">$' + $('#slider').slider('values', 0 ) + '</span>');

	$('.ui-slider-handle:eq(1)').append('<span class="price-range-max value">$' + $('#slider').slider('values', 1 ) + '</span>');


	/*---------------------
	// Ajax Contact Form
	--------------------- */

	$('.cf-msg').hide();
		$('form#cf button#submit').on('click', function() {
			var fname = $('#fname').val();
			var subject = $('#subject').val();
			var email = $('#email').val();
			var msg = $('#msg').val();
			var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

			if (!regex.test(email)) {
				alert('Please enter valid email');
				return false;
			}

			fname = $.trim(fname);
			subject = $.trim(subject);
			email = $.trim(email);
			msg = $.trim(msg);

			if (fname != '' && email != '' && msg != '') {
				var values = "fname=" + fname + "&subject=" + subject + "&email=" + email + " &msg=" + msg;
				$.ajax({
					type: "POST",
					url: "mail.php",
					data: values,
					success: function() {
						$('#fname').val('');
						$('#subject').val('');
						$('#email').val('');
						$('#msg').val('');

						$('.cf-msg').fadeIn().html('<div class="alert alert-success"><strong>Success!</strong> Email has been sent successfully.</div>');
						setTimeout(function() {
							$('.cf-msg').fadeOut('slow');
						}, 4000);
					}
				});
			} else {
				$('.cf-msg').fadeIn().html('<div class="alert alert-danger"><strong>Warning!</strong> Please fillup the informations correctly.</div>')
			}
			return false;
	});

})(jQuery);
