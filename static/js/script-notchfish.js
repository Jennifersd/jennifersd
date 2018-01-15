// button preview notch / notchless
$(document).ready(function(){
	// button show wallpaper
    //var container = $('.phone'),
    //notch = container.find('.notch'),
    //lessnotch = container.find('.lessnotch'),
    button = $('.buttonPreview');

    $('.wallpaper1').hide();

    button.click(function() {

    if ($(this).parent().find('.wallpaper1').is(':visible')) {
        $(this).parent().find('.wallpaper1').hide();
        $(this).parent().find('.wallpaper2').show();
    } else {
        $(this).parent().find('.wallpaper1').show();
        $(this).parent().find('.wallpaper2').hide();
    }

    });

    // scroll // Select all links with hashes
    $('a[href*="#"]')
    .not('[href="#"]')
    .not('[href="#0"]')
    .click(function(event) {
    if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
        && 
        location.hostname == this.hostname
    ) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: target.offset().top
        }, 1000 );
        }
    }
    });
});

