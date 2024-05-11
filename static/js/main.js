const form = document.getElementById('myForm');
const queryInput = document.getElementById('query-input');
const backendUrl = document.getElementById('backendUrl').value;

form.addEventListener('submit', async (event) => {
  event.preventDefault();  // Prevent default form submission behavior
  const userQuery = queryInput.value;

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: userQuery })
    });

    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }

    const data = await response.json();
    console.log('Generated Text:', data.generated_text);
    // Update your frontend to display the generated text (e.g., in a paragraph)
  } catch (error) {
    console.error('Error:', error);
    // Handle errors appropriately (e.g., display an error message to the user)
  }
});
