function openModal() {
  document.getElementById('myModal').style.display = "block";
  $('body').addClass('modal-open');
}

function closeModal() {
  document.getElementById('myModal').style.display = "none";
  $('body').removeClass('modal-open');
}

var slideIndex = 1;
showSlides(slideIndex);

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var captions = document.getElementsByClassName("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < captions.length; i++) {
    captions[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
  captions[slideIndex-1].style.display = "block";
}
