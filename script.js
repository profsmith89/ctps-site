document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Displaying a simple alert on form submission. You could replace this with actual form submission functionality.
        alert('Thank you for your message. I will get back to you soon!');
        form.reset();
    });
});
