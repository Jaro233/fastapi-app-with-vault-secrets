// Assume the book ID is passed via a query parameter
const queryParams = new URLSearchParams(window.location.search);
const bookId = queryParams.get("id");

// Fetch book details and populate the form
async function fetchBookDetails() {
  const response = await fetch(`/books/${bookId}`);
  const book = await response.json();

  document.getElementById("title").value = book.title;
  document.getElementById("author").value = book.author;
  document.getElementById("genre").value = book.genre || "";
  document.getElementById("status").value = book.status || "";
  document.getElementById("user_rating").value = book.user_rating || "";
}

if (bookId) {
  fetchBookDetails();
} else {
  console.error("No book ID provided");
}

document
  .getElementById("editBookForm")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const updatedBook = {
      title: document.getElementById("title").value,
      author: document.getElementById("author").value,
      genre: document.getElementById("genre").value,
      status: document.getElementById("status").value,
      user_rating: document.getElementById("user_rating").value,
    };

    try {
      const response = await fetch(`/books/${bookId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedBook),
      });
      const result = await response.json();
      if (response.ok) {
        alert(`${result.message}`);
        window.location.href = "/";
      } else {
        alert(`${result.message}`);
      }
    } catch (error) {
      alert(`Error: ${error}`);
    }
  });
