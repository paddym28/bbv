setTimeout( function(){
  $('#message').fadeOut('slow')
}, 3000);


setTimeout( function(){
  $('.welcomeMessage').fadeOut('slow')
}, 3000);

const date  = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

AOS.init({
        offset:300,
        duration:500,
});




var swiper = new Swiper(".video-slider", {
   spaceBetween: 20,
   grabCursor:true,
   autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
   loop:true,
   pagination: {
     el: ".swiper-pagination",
     clickable: true,
   },
   breakpoints: {
      540: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
   },
});