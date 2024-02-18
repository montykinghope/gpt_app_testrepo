function sendPrompt() {
    const promptInput = document.getElementById("promptInput").value;
    const responseOutput = document.getElementById("responseOutput");

    fetch('https://gpt-test-function.azurewebsites.net/api/gpt_function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-functions-key': 'vNbv0biAuW-AUCvBfAB4-p1DtSQM0Nhfb5XpUTe3H3QxAzFuPYfgNw==' // If needed for your function's authentication
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
