function sendPrompt() {
    const promptInput = document.getElementById("promptInput").value;
    const responseOutput = document.getElementById("responseOutput");

    fetch('YOUR_AZURE_FUNCTION_URL', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-functions-key': 'YOUR_FUNCTION_KEY' // If needed for your function's authentication
        },
        body: JSON.stringify({ body: promptInput })
    })
    .then(response => response.json())
    .then(data => {
        responseOutput.textContent = data.response;
    })
    .catch((error) => {
        console.error('Error:', error);
        responseOutput.textContent = 'Error calling the function';
    });
}
