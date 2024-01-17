document.getElementById("addBookForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const book = {
    title: document.getElementById("title").value,
    author: document.getElementById("author").value,
    genre: document.getElementById("genre").value,
    status: document.getElementById("status").value,
    user_rating: document.getElementById("user_rating").value,
  };
  try {
    const response = await fetch("/books", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(book),
    });
    const result = await response.json();
    console.log(result);
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
