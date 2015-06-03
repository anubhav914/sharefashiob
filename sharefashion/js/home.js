$(window).scroll(function() {
if ($(this).scrollTop() > 20){  
    $('#navbar-example').addClass("shrink");
  }
  else{
    $('#navbar-example').removeClass("shrink");
  }
});