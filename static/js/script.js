$(document).ready(function(){
	/*
	===============================================================================================
	<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LIGHTBOX FUNCTIONALITY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	===============================================================================================
	*/
	var item, img, title, large_img;
	var CW, CH, CL, CT, hpadding, vpadding, imgtag;
	// Flag for preventing multiple image display
	var lb_loading = false;
	var doc = $(document);

	$('#lightbox li').click(function(){
		if(lb_loading) return false;
		lb_loading = true;

		item = $(this);
		img = item.find('img');
		title = item.find('.title').html();

		// Remove active class from previous clicked LI
		$('#lightbox li.active').removeClass('active');
		// Mark the clicked LI as active for later use
		item.addClass('active');

		// The Large Image
		large_img = new Image();
		// Use data-large or the src itself if large image url is not available
		large_img.src = img.attr("data-large") ? img.attr("data-large") : img.attr("src");
		

		// Adding aditional HTML 
		if ($('.lb_backdrop').length < 1) {
			var lb_backdrop = '<div class="lb_backdrop"></div>';
			var lb_canvas = '<div class="lb_canvas"></div>';
			var lb_previous = '<span class="lb_previous"><</span>';
			var lb_title = '<span class="lb_title"></span>';
			var lb_next = '<span class="lb_next">></span>';
			var lb_controls = '<div class="lb_controls">' + lb_previous + lb_title + lb_next + '</div>';
			var total_html = lb_backdrop + lb_canvas + lb_controls;

			$(total_html).appendTo('body');
		}
		//Fade in lightboc element if they are hidden due to previous exits
		if ($('.lb_backdrop:visible').length == 0){
			$('.lb_backdrop, .lb_canvas, .lb_controls').fadeIn("slow");
		}

		// Display Preloader until the large image and make the previous images translucent so that the loader in BG is visible
		if(!large_img.complete)
			$('.lb_canvas').addClass('loading').children().css("opacity", "0.5")
		
		// disable left/right controls on first / last 
		if(item.prev().length == 0)
			$('.lb_previous').addClass('inactive');
		else 
			$('.lb_previous').removeClass('inactive');
		
		if(item.next().length == 0)
			$('.lb_next').addClass('inactive');
		else 
			$('.lb_next').removeClass('inactive');
		

		// centering .lb_canvas
		CW = $('.lb_canvas').outerWidth();
		CH = $('.lb_canvas').outerHeight();
		// top and left coordination
		CL = ($(window).width() - CW)/2
		CT = ($(window).height() - CH)/2
		$('.lb_canvas').css({top: CT, left: CL});

		// Inserting Large image into .lb_canvas once it's loaded
		$(large_img).load(function(){
			// Recentering .lb_canvas with new dimensions
			CW = large_img.width;
			CH = large_img.height;

			if (CW > 1200 || CH > 1000){
				CW = CW / 2;
				CH = CH / 2;
			}

			// .lb_canvas padding to be added to image width/height to get the total dimension
			hpadding = parseInt($('.lb_canvas').css("paddingLeft")) + parseInt($('.lb_canvas').css("paddingRight"));
			vpadding = parseInt($('.lb_canvas').css("paddingTop")) + parseInt($('.lb_canvas').css("paddingBottom"));
			CL = ($(window).width() - CW - hpadding)/2;
			CT = ($(window).height() - CH - vpadding)/2;

			//animating .lb_canvas to new dimensions and position
			$('.lb_canvas').html("").animate({width: CW, height: CH, top: CT, left: CL}, 500, function(){
				// inserting the image but keeping it hidden
				imgtag = '<img src="' + large_img.src + '" style="opacity: 0;" />';
				$('.lb_canvas').html(imgtag);
				$('.lb_canvas img').fadeTo("slow", 1);
				// displaying the image title
				$('.lb_title').html(title);

				lb_loading = false;
				$('.lb_canvas').removeClass('loading');
			})
		})
	})

	// Click base navigation
	doc.on("click", ".lb_previous", function(){navigate(-1)});
	doc.on("click", ".lb_next", function(){navigate(1)});
	doc.on("click", ".lb_backdrop", function(){navigate(0)});

	// Keyboard navigation
	doc.keyup(function(e){
		// keyboard navigation should work only if lightbox is active which means backdrop is visible
		if($('.lb_backdrop:visible').length == 1){
			// left
			if(e.keyCode == "37") navigate(-1);
			// right
			if(e.keyCode == "39") navigate(1);
			// Esc
			if(e.keyCode == "27") navigate(0);
		}
	});
	// Navigation function
	function navigate(direction){
		if (direction == -1) //left
			$("#lightbox li.active").prev().trigger("click");
		else if (direction == 1) //right
			$('#lightbox li.active').next().trigger("click");
		else if (direction == 0){
			$("#lightbox li.active").removeClass('active');
			$('.lb_canvas').removeClass('loading');
			// Fade out the lightbox elements
			$('.lb_backdrop, .lb_canvas, .lb_controls').fadeOut("slow", function(){
				// empty canvas and title
				$('.lb_canvas, .lb_title').html("");
			})
			lb_loading = false;
		}
	}
	/*
	=======================
	=====LIGHTBOX END======
	=======================
	*/
	/*$(window).scroll(function(){
		if ($(this).scrollTop() > parseInt($('.jumbotron').outerHeight(true))){
			$('.navbar-inverse').addClass('navbar-fixed-top');
			$('.navbar-inverse').css('paddingTop', '0px');
			$('.navbar-inverse').css('paddingBottom', '0px');
		} else {
			$('.navbar-inverse').removeClass('navbar-fixed-top');
			$('.navbar-inverse').css('paddingTop', '10px');
			$('.navbar-inverse').css('paddingBottom', '10px');
		}
	}) */
			// Javascript to enable link to tab
		var url = document.location.toString();
		if (url.match('#')) {
		    $('.nav-tabs a[href="#' + url.split('#')[1] + '"]').tab('show');
		} 

		// Change hash for page-reload
		$('.nav-tabs a').on('shown.bs.tab', function (e) {
		    window.location.hash = e.target.hash;
		})

	// Services from the index page
	var $window = $(window);
	var $desktop = $('#desktop-services');
	var $mobile = $('#mobile-services');
	if($window.innerWidth() < 768){
		$desktop.hide();
		$mobile.show();
	} else {
		$desktop.show();
		$mobile.hide();
	}
	
})

