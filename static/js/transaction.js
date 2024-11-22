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