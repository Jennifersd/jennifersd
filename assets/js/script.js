// Menu 
window.onload = function(){ 

	(function() {
	    var burger = document.querySelector(".burger-container"),
	    	header_content = document.querySelector(".header-wrap"),
	        header = document.querySelector(".header-container");
	    
	
	    burger.onclick = function() {
	        header.classList.toggle("menu-opened");
	        header_content.classList.toggle("header-opened");
	    };
	})();
	

};

// Desplegable categorias
$(document).ready(function(){
	(function() {
		$('.blocks-container > h3').click(function() {
			    $( ".blocks-container > ul" ).slideToggle( "slow" );
		});

	})();
	
	(function() {
	  function fixDiv() {
	    var $cache = $('#social-fixed');
	    if ($(window).scrollTop() > 750){
	      
	      $cache.addClass("fixed-nav");

		} else {
			$cache.removeClass("fixed-nav");
		}
	     
	      
	  }
	  $(window).scroll(fixDiv);
	  fixDiv();
	})();

	
});



