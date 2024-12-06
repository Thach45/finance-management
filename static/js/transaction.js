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

const accountFilter = document.getElementById('accountFilter');
const timeFilter = document.getElementById('timeFilter');
const typeFilter = document.getElementById('typeFilter');
if(accountFilter){
    accountFilter.addEventListener('change', () => {
    window.location.href = "/transaction?account=" + accountFilter.value;
    })
}
if(typeFilter){
    typeFilter.addEventListener('change', () => {
         window.location.href = "/transaction?type=" + typeFilter.value;
    })
}
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

    // btnEdit.forEach(btn => {
    //     btn.addEventListener('click', () => {
    //         editModal.classList.add('active');
    //         const transactionId = btn.getAttribute('data-id');
    //     })
    // })
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


const typeSelect = document.querySelector('.typeTransaction');
    const categoryIncome = document.querySelector('.categoryIncome');
    const categoryExpense = document.querySelector('.categoryExpense');
    const categoryTransfer = document.querySelector('.categoryTransfer');

    typeSelect.addEventListener('change', () => {
        // Reset tất cả danh mục
        categoryIncome.classList.add('hidden');
        categoryExpense.classList.add('hidden');
        categoryTransfer.classList.add('hidden');
        categoryIncome.disabled = true;
        categoryExpense.disabled = true;
        categoryTransfer.disabled = true;

        // Hiển thị danh mục phù hợp
        const selectedType = typeSelect.value;
        if (selectedType === 'income') {
            categoryIncome.classList.remove('hidden');
            categoryIncome.disabled = false;
        } else if (selectedType === 'expense') {
            categoryExpense.classList.remove('hidden');
            categoryExpense.disabled = false;
        } else if (selectedType === 'transfer') {
            categoryTransfer.classList.remove('hidden');
            categoryTransfer.disabled = false;
        }
    });

let accountSelect = document.querySelector('.accountSelect');
const typeTransaction = document.querySelector('.typeTransaction');
accountSelect.addEventListener('change', () => {
    // Lấy thuộc tính `balance` từ tùy chọn được chọn
    let selectedOption = accountSelect.options[accountSelect.selectedIndex];
    console.log(selectedOption);
    let buget = parseInt(selectedOption.getAttribute('balance')) || 0;
    // Cập nhật thuộc tính `max` cho trường nhập liệu
    let amountInput = document.querySelector('.amountAccount');
    console.log(typeof buget);
    if(typeTransaction.value === 'expense'){
        amountInput.setAttribute('max', buget);
        if(amountInput.value > buget){
            amountInput.value = buget;
        }
    }
});




