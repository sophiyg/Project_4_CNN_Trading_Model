document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    // Prevent the default HTML form submission/page reload
    e.preventDefault(); 
    
    const imageInput = document.getElementById('imageInput');
    const predictionText = document.getElementById('predictionText');
    
    // Ensure a file was actually selected
    if (imageInput.files.length === 0) {
        alert("Please select an image first!");
        return;
    }
    
    const imageFile = imageInput.files[0];
    
    // Put the image inside a FormData object (essential for binary/file data)
    const formData = new FormData();
    formData.append('image', imageFile);
    
    predictionText.innerText = "FINAL PREDICTION HERE (1 for increase and 0 for same or decrease).";
  /*
    try {
        // Replace this URL with your actual AI backend endpoint
        const response = await fetch('https://your-api-endpoint.com', {
            method: 'POST',
            body: formData // No Headers needed; fetch sets multipart/form-data automatically
        });
        
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        
        // Assume the backend returns JSON like: { "prediction": "Golden Retriever", "confidence": 0.94 }
        const data = await response.json();
        
        // Display the prediction to the user
        predictionText.innerHTML = `<strong>Result:</strong> ${data.prediction} <br> <strong>Confidence:</strong> ${(data.confidence * 100).toFixed(2)}%`;
        
    } catch (error) {
        console.error("Error making prediction:", error);
        predictionText.innerText = "Failed to get prediction. Check your console or server connection.";
    }
    */
});
