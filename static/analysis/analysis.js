// chart
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
   type: 'bar',
   data: {
      labels: ['어', '음', '그'],
      datasets: [{
         label: '# of Value',
         data: [3, 7, 2],
         backgroundColor: [
           'rgba(255, 99, 132, 0.5)',
           'rgba(54, 162, 235, 0.5)',
           'rgba(255, 206, 86, 0.5)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });


