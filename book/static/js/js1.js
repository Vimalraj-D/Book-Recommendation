function fetchRecommendations() {
    const bookName = document.getElementById('book-name').value;

    if (!bookName) {
        alert("Please enter a book name!");
        return;
    }

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `book_name=${bookName}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recommendations').innerHTML = '';

        if (data.error) {
            document.getElementById('recommendations').innerHTML = `<p>${data.error}</p>`;
        } else {
            data.recommendations.forEach((rec) => {
                const bookCard = document.createElement('div');
                bookCard.classList.add('book-card');
                bookCard.innerHTML = `
                    <div class="info">
                        <h3>${rec.Title}</h3>
                        <p>by ${rec.Author}</p>
                        <p>Rating: ${rec.Rating}</p>
                        <a href="${rec.URLs}" target="_blank">More Info</a>
                    </div>
                `;
                document.getElementById('recommendations').appendChild(bookCard);
            });
        }
    })
    .catch(error => {
        alert("An error occurred while fetching recommendations. Please try again.");
    });
}