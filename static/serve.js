document.addEventListener('DOMContentLoaded', function() {
    // Attach event listeners to all "Get Chart" buttons
    document.querySelectorAll('.getChartButton').forEach(function(button, index) {
        button.addEventListener('click', function() {
            getChart(index);
        });
    });
});

function getChart(trackerIndex) {
    // Use the trackerIndex to find the corresponding inputs and image within the same .column
    const column = document.querySelectorAll('.column')[trackerIndex];
    const symbol = column.querySelector('.symbolInput').value.toUpperCase(); // Convert symbol to uppercase
    const currencySelect = column.querySelector('.currencySelect').value; // Get selected currency, corrected variable name here

    const interval = column.querySelector('.intervalSelect').value;
    const limit = column.querySelector('.limitInput').value;
    const chartImage = column.querySelector('.chartImage');

    // Corrected the variable name in the fetch URL
    fetch(`/get_chart?symbol=${encodeURIComponent(symbol)}${currencySelect}&interval=${encodeURIComponent(interval)}&limit=${encodeURIComponent(limit)}`)
        .then(response => response.json())
        .then(data => {
            if(data.status === 'success') {
                // Update the src of the image within the same column
                chartImage.src = data.chartUrl + `?t=${new Date().getTime()}`; // Cache busting
            } else {
                console.error('Failed to get the chart:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}

