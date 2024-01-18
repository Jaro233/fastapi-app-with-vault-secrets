async function fetchBooks() {
  const response = await fetch("/books");
  const data = await response.json();
  const booksTable = document.getElementById("books");
  booksTable.innerHTML = "";
  data.books.forEach((book) => {
    console.log(book);
    booksTable.innerHTML += `
                    <tr>
                        <td>${book.title}</td>
                        <td>${book.author}</td>
                        <td>${book.genre}</td>
                        <td>${book.status}</td>
                        <td>${book.user_rating}</td>
                        <td>
                            <button class="edit-btn" onclick="editBook(${book.id})">Edit</button>
                            <button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
                        </td>
                    </tr>
                `;
  });
}
async function deleteBook(bookId) {
  try {
    const response = await fetch(`/books/${bookId}`, { method: "DELETE" });
    const result = await response.json();
    if (response.ok) {
      alert(`${result.message}`);
      fetchBooks();
    } else {
      alert(`${result.message}`);
    }
  } catch (error) {
    alert(`Error: ${error}`);
  }
}

function editBook(bookId) {
  window.location.href = `/edit-book?id=${bookId}`;
}

fetchBooks();
