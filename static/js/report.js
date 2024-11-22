// Biểu đồ doanh thu
const revenueChart = new Chart(document.getElementById('revenueChart'), {
    type: 'line',
    data: {
      labels: ['T1', 'T2', 'T3', 'T4', 'T5', 'T6'],
      datasets: [{
        label: 'Doanh Thu',
        data: [650, 590, 800, 810, 560, 550],
        fill: true,
        backgroundColor: 'rgba(37, 99, 235, 0.1)',
        borderColor: '#2563eb',
        tension: 0.4
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        }
      },
      interaction: {
        intersect: false,
        mode: 'index'
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  
  // Biểu đồ chi phí
  const expenseChart = new Chart(document.getElementById('expenseChart'), {
    type: 'doughnut',
    data: {
      labels: ['Marketing', 'Vận Hành', 'Nhân Sự', 'Khác'],
      datasets: [{
        data: [30, 25, 25, 20],
        backgroundColor: [
          '#2563eb',
          '#10b981',
          '#f59e0b',
          '#64748b'
        ]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom'
        }
      }
    }
  });
  
  // Biểu đồ sản phẩm
  const productsChart = new Chart(document.getElementById('productsChart'), {
    type: 'bar',
    data: {
      labels: ['SP1', 'SP2', 'SP3', 'SP4', 'SP5'],
      datasets: [{
        label: 'Doanh Số',
        data: [120, 190, 300, 150, 200],
        backgroundColor: '#2563eb'
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });