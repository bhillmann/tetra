$(document).ready(function() {
	 $(window).scroll(function(){
		 if ($(this).scrollTop() > 400) {
			 $('.btn-scroll-to-top').fadeIn();
		 } else {
			 $('.btn-scroll-to-top').fadeOut();
		 }
	 });
});