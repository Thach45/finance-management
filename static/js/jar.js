// function calculateJars() {
//     const income = parseFloat(document.getElementById('income-input').value);
//     if (isNaN(income)) return;

//     const percentages = [55, 10, 10, 10, 10, 5];
//     const jarAmounts = document.querySelectorAll('.jar-amount');

//     jarAmounts.forEach((jarAmount, index) => {
//         const amount = (income * percentages[index] / 100).toLocaleString('vi-VN', { style: 'currency', currency: 'VND' });
//         jarAmount.textContent = amount;
//     });
// }

// function addCategory(event, jarIndex) {
//     event.preventDefault();
//     const input = event.target.querySelector('input');
//     const category = input.value.trim();
//     if (category) {
//         const ul = document.getElementById(`categories-${jarIndex}`);
//         const li = document.createElement('li');
//         li.textContent = category;
//         ul.appendChild(li);
//         input.value = '';
//     }
// }


