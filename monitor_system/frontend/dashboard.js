const LIMIT = 10;
let values = [];
let chart = null;

document.getElementById('calibrateBtn')
    .addEventListener('click', function (event) {
        event.preventDefault();
        fetch('http://localhost:5000/calibrate', {
            method: 'POST'
        })
    });

function fetchData() {
    fetch('http://localhost:5000/update')
        .then(response => response.json())
        .then(data => {
            console.log(values)
            values.push({
                moisture: data.data.moisture,
                timestamp: data.data.timestamp
            }
            )
            let values_slice = null;
            if (values.length >= LIMIT)
                values_slice = values.slice(values.length - LIMIT, values.length - 1)
            else
                values_slice = values

            if (chart !== null) {
                chart.destroy();
            }

            const chartContext = document.getElementById('moistureChart').getContext('2d');
            chart = new Chart(chartContext, {
                type: 'line',
                data: {
                    labels: values_slice.map(v => v.timestamp),
                    datasets: [
                        {
                            label: 'Moisture',
                            data: values_slice.map(v => v.moisture),
                            borderColor: 'blue',
                            fill: false
                        },
                        {
                            label: 'Threshold',
                            data: Array(values_slice.length).fill(data.data.threshold),
                            borderColor: 'red',
                            fill: false
                        }
                    ]

                },
                options: {
                    scales: {
                        y: {
                            min: 0,
                            max: 68000
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function fetchDataPeriodically() {
    fetchData();

    setInterval(fetchData, 2000);
}

fetchDataPeriodically();