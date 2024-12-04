const modal = document.getElementById('transactionModal');
const closeBtn = modal.querySelector('.close-btn');
const cancelBtn = modal.querySelector('.cancel-btn');
const addTransactionBtn = document.querySelector('.add-transaction-btn');
if(addTransactionBtn){
    addTransactionBtn.addEventListener('click', () => {
        modal.classList.add('active');
    })
}
if(closeBtn){
    closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    })
}
if(cancelBtn){
    cancelBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    })
}

// const accountFilter = document.getElementById('accountFilter');
// const timeFilter = document.getElementById('timeFilter');
// const typeFilter = document.getElementById('typeFilter');
// const tableBody = document.getElementById('transactionTableBody'); // ID của tbody trong bảng

// async function fetchAndRenderTransactions() {
//     const url = new URL(window.location.href);

//     // Lấy giá trị từ các bộ lọc
//     const time = timeFilter ? timeFilter.value : 'all';
//     const type = typeFilter ? typeFilter.value : 'all';
//     const account = accountFilter ? accountFilter.value : 'all';

//     // Cập nhật tham số vào URL
//     url.searchParams.set('time', time);
//     url.searchParams.set('type', type);
//     url.searchParams.set('account', account);

//     // Cập nhật URL trên trình duyệt mà không reload trang
//     history.replaceState(null, '', url.toString());

//     // Gọi API để lấy dữ liệu
//     const response = await fetch(url.toString());
//     const transactions = await response.json();

//     // Xóa dữ liệu cũ trong bảng
//     tableBody.innerHTML = "";

//     // Cập nhật bảng với dữ liệu mới
//     transactions.forEach(transaction => {
//         const row = `
//             <tr>
//                 <td>${transaction.date}</td>
//                 <td><span class="badge ${transaction.type}">${transaction.type}</span></td>
//                 <td>${transaction.account}</td>
//                 <td>${transaction.category}</td>
//                 <td>${transaction.description}</td>
//                 <td class="amount ${transaction.type}">${transaction.amount}</td>
//                 <td>
//                     <a class="action-btn edit" href="/transaction/edit/${transaction._id}"><i class="fas fa-edit"></i></a>
//                     <form class="delete-form" action="/transaction/delete/${transaction._id}" method="post">
//                         <button type="submit" class="action-btn delete"><i class="fas fa-trash"></i></button>
//                     </form>
//                 </td>
//             </tr>
//         `;
//         tableBody.innerHTML += row;
//     });
// }

// // Gắn sự kiện thay đổi cho các bộ lọc
// if (accountFilter) {
//     accountFilter.addEventListener('change', fetchAndRenderTransactions);
// }
// if (timeFilter) {
//     timeFilter.addEventListener('change', fetchAndRenderTransactions);
// }
// if (typeFilter) {
//     typeFilter.addEventListener('change', fetchAndRenderTransactions);
// }

// // Gọi API lần đầu để hiển thị dữ liệu mặc định
// fetchAndRenderTransactions();

// Đặt giá trị hiện tại cho các bộ lọc khi tải trang
const accountFilter = document.getElementById('accountFilter');
const timeFilter = document.getElementById('timeFilter');
const typeFilter = document.getElementById('typeFilter');
const filterButton = document.getElementById('filterButton');

// Lắng nghe sự kiện nút Lọc
if (filterButton) {
    filterButton.addEventListener('click', () => {
        const url = new URL(window.location.href);
        url.searchParams.set('account', accountFilter.value);
        url.searchParams.set('time', timeFilter.value);
        url.searchParams.set('type', typeFilter.value);

        // Xóa các giá trị "all" khỏi URL
        if (accountFilter.value === 'all') url.searchParams.delete('account');
        if (timeFilter.value === 'all') url.searchParams.delete('time');
        if (typeFilter.value === 'all') url.searchParams.delete('type');

        window.location.href = url.toString();
    });
}




// const accountFilter = document.getElementById('accountFilter');
// const timeFilter = document.getElementById('timeFilter');
// const typeFilter = document.getElementById('typeFilter');

// if(accountFilter){
//     accountFilter.addEventListener('change', () => {
//         const url = new URL(window.location.href);
//         url.searchParams.set('account', accountFilter.value);
//         window.location.href = url.toString();
//     })
// }
// if(timeFilter){
//     timeFilter.addEventListener('change', () => {
//         const url = new URL(window.location.href);
//         url.searchParams.set('time', timeFilter.value);
//         window.location.href = url.toString();
//     })
// }
// if(typeFilter){
//     typeFilter.addEventListener('change', () => {
//         const url = new URL(window.location.href);
//         url.searchParams.set('type', typeFilter.value);
//         window.location.href = url.toString();
//     })
// }

const editCloseBtn = document.querySelector('.edit-close-btn');

const editModal = document.getElementById('editTransactionModal');
const btnEdit = document.querySelectorAll('.edit');
if(btnEdit){
    btnEdit.forEach(btn => {
    btn.addEventListener('click', () => {
        const transactionId = btn.getAttribute('data-id');
        editModal.classList.add('active');

        // Fetch thông tin giao dịch từ backend
        fetch(`/api/transaction/${transactionId}`)
            .then(response => response.json())
            .then(data => {
                if (data) {
                    // Điền dữ liệu vào form sửa
                    document.querySelector('#editTransactionModal [name="type"]').value = data.type;
                    document.querySelector('#editTransactionModal [name="account"]').value = data.account;
                    document.querySelector('#editTransactionModal [name="category"]').value = data.category;
                    document.querySelector('#editTransactionModal [name="amount"]').value = data.amount;
                    document.querySelector('#editTransactionModal [name="date"]').value = data.date.split('T')[0];
                    document.querySelector('#editTransactionModal [name="description"]').value = data.description;
                }
            })
            .catch(err => console.error('Error fetching transaction:', err));
    });
});


}
if(editCloseBtn){
    editCloseBtn.addEventListener('click', () => {
        editModal.classList.remove('active');
    })
}
const formatCurrency = (amount) => {
    if (isNaN(amount)) {
        console.error('Invalid amount:', amount);
        return 'Invalid amount';
    }
    return amount.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' });
}

const amounts = document.querySelectorAll('.amount');
amounts.forEach(amount => {
    let value = parseInt(amount.textContent);
    if (!isNaN(value)) {
        amount.textContent = formatCurrency(value);
        if(amount.classList.contains('income')){
            amount.style.color = 'green';
            amount.textContent = '+' + amount.textContent;
        }else if(amount.classList.contains('expense')){
            amount.style.color = 'red';
            amount.textContent = '-' + amount.textContent;
        }else if(amount.classList.contains('transfer')){
            amount.style.color = '#004085';
            amount.textContent = '+' + amount.textContent;
        }
    } else {
        console.error('Invalid number in textContent:', amount.textContent);
    }
});





