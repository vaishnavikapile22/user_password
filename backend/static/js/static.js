
// Example JavaScript code for real-time updates using Flet
const historyContainer = document.getElementById('historyContainer');

// Function to update history view
function updateHistoryView(data) {
    // Clear existing content
    historyContainer.innerHTML = '';

    // Loop through the data and create HTML elements for each entry
    data.forEach(entry => {
        const div = document.createElement('div');
        div.classList.add('history-entry');
        div.innerHTML = `
            <p>Input Parameters: ${entry.input_parameters}</p>
            <p>Output Results: ${entry.output_results}</p>
            <p>Timestamp: ${entry.timestamp}</p>
        `;
        historyContainer.appendChild(div);
    });
}

// Example code to fetch and update history data periodically
setInterval(() => {
    fetch('/api/history')  // Assuming you have an API endpoint for history data
        .then(response => response.json())
        .then(data => updateHistoryView(data))
        .catch(error => console.error('Error fetching history:', error));
}, 5000);  // Update every 5 seconds (adjust as needed)
