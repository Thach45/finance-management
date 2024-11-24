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
        const url = new URL(window.location.href);
        url.searchParams.set('account', accountFilter.value);
        window.location.href = url.toString();
    })
}
if(timeFilter){
    timeFilter.addEventListener('change', () => {
        const url = new URL(window.location.href);
        url.searchParams.set('time', timeFilter.value);
        window.location.href = url.toString();
    })
}
if(typeFilter){
    typeFilter.addEventListener('change', () => {
        const url = new URL(window.location.href);
        url.searchParams.set('type', typeFilter.value);
        window.location.href = url.toString();
    })
}
const editCloseBtn = document.querySelector('.edit-close-btn');

const editModal = document.getElementById('editTransactionModal');
const btnEdit = document.querySelectorAll('.edit');
if(btnEdit){
    btnEdit.forEach(btn => {
        btn.addEventListener('click', () => {
            editModal.classList.add('active');
            const transactionId = btn.getAttribute('data-id');
        })
    })
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