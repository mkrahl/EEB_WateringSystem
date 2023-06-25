const LIMIT = 30;
const MIN_MOISTURE = 0; // air moisture
const MAX_MOISTURE = 64000;
let values = [];
let chart = null;

document.getElementById('calibrateBtn')
    .addEventListener('click', function (event) {
        event.preventDefault();
        fetch('http://localhost:5000/calibrate', {
            method: 'POST'
        })
    });

const valveStatusElement = document.getElementById('valveStatus');
const valveIndicatorElement = document.getElementById('valveIndicator');

function openValve() {
    valveStatusElement.textContent = 'Valve Open';
    valveIndicatorElement.classList.add('open');
    valveIndicatorElement.classList.remove('closed');
}

function closeValve() {
    valveStatusElement.textContent = 'Valve Closed';
    valveIndicatorElement.classList.add('closed');
    valveIndicatorElement.classList.remove('open');
}

function mapMoisture(value) {
    return Math.max(MAX_MOISTURE - value, 0);
}

function fetchData() {
    fetch('http://localhost:5000/update')
        .then(response => response.json())
        .then(data => {
            values.push({
                moisture: mapMoisture(data.data.moisture),
                timestamp: data.data.timestamp
            })
            let values_slice = null;
            if (values.length >= LIMIT)
                values_slice = values.slice(values.length - LIMIT, values.length - 1)
            else
                values_slice = values

            if (data.data.valve_is_open) {
                openValve();
            } else {
                closeValve();
            }

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
                            data: Array(values_slice.length).fill(mapMoisture(data.data.threshold)),
                            borderColor: 'red',
                            fill: false
                        }
                    ]

                },
                options: {
                    scales: {
                        y: {
                            min: MIN_MOISTURE,
                            max: MAX_MOISTURE,
                            ticks: {
                                callback: function(value, index, values) {
                                    if (value >= MAX_MOISTURE) 
                                        return "VERY WET";
                                    else if (value <= MIN_MOISTURE)
                                        return "VERY DRY";
                                    else if (value === 50000)
                                        return "WET"
                                    else if (value === 20000)
                                        return "DRY"
                                    else return "";
                                }
                              }
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