// Menu 
window.onload = function(){ 

	(function() {
	    var burger = document.querySelector(".burger-container"),
	        header = document.querySelector(".header-container");
	
	    burger.onclick = function() {
	        header.classList.toggle("menu-opened");
	    };
	})();
};

//
$(document).ready(function(){
	(function() {
		$('.blocks-container > h3').click(function() {
			    $( ".blocks-container > ul" ).slideToggle( "slow" );
		});

	})();

});