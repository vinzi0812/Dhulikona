const testimonials = document.querySelectorAll('.testimonial');
let currentIndex = 0;

function showTestimonial(index) {
  testimonials.forEach(testimonial => testimonial.classList.remove('active'));
  testimonials[index].classList.add('active');
}

function nextTestimonial() {
  currentIndex = (currentIndex + 1) % testimonials.length;
  showTestimonial(currentIndex);
}

// Change testimonial every 5 seconds (adjust the interval as needed)
setInterval(nextTestimonial, 5000);

// Show the first testimonial initially
showTestimonial(currentIndex);
