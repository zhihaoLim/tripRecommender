document.querySelectorAll('.response-options .option input').forEach(input => {
    input.addEventListener('change', function() {
        // Get the parent 'question-container' of the clicked input
        let parentContainer = this.closest('.question-container');

        // Reset the buttons within the same 'question-container' to grey
        parentContainer.querySelectorAll('.button').forEach(button => {
            button.style.backgroundColor = '#ddd';
        });

        // Change the style of the clicked button
        this.nextElementSibling.style.backgroundColor = this.nextElementSibling.getAttribute('data-color');
    });
});
