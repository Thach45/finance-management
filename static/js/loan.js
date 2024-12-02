const loanBtn = document.querySelector('.loan-btn');
const lendingBtn = document.querySelector('.lending-btn');
const loanView = document.querySelectorAll('.loan-view');
const lendingView = document.querySelectorAll('.lending-view');
const addLoanBtn = document.querySelector('.add-loan-btn');
const addLendingBtn = document.querySelector('.add-lending-btn');
const formLoan = document.querySelector('.modal');
const typeLoan = document.querySelector('.status-loan');
const typeLending = document.querySelector('.status-lending');
const closeBtn = document.querySelector('.close-btn');
const form = document.querySelector('.loan-form');
const cancelBtn = document.querySelector('.cancel');
const cancelPaymentBtn = document.querySelector('.cancel-payment-btn');
const closePaymentBtn = document.querySelector('.close-payment-btn');
const modalPayment = document.querySelector('.modal-payment');
const paymentBtn = document.querySelector('.pay-loan-btn');
if(loanBtn){
    loanBtn.addEventListener('click', () => {
        loanBtn.classList.add('active');
        lendingBtn.classList.remove('active');
        loanView.forEach(view => view.classList.add('active'));
        lendingView.forEach(view => view.classList.remove('active'));
        addLoanBtn.classList.add('active');
        addLendingBtn.classList.remove('active');
    });
}
if(lendingBtn){
    lendingBtn.addEventListener('click', () => {
        lendingBtn.classList.add('active');
        loanBtn.classList.remove('active');
        lendingView.forEach(view => view.classList.add('active'));
        loanView.forEach(view => view.classList.remove('active'));
        addLendingBtn.classList.add('active');
        addLoanBtn.classList.remove('active');
    });
}
if(addLoanBtn){
    addLoanBtn.addEventListener('click', () => {
        formLoan.classList.add('active');
        typeLoan.classList.add('active');
    });
}
if(addLendingBtn){
    addLendingBtn.addEventListener('click', () => {
        formLoan.classList.add('active');
        typeLending.classList.add('active');
    });
}
if(closeBtn){
    closeBtn.addEventListener('click', () => {
        formLoan.classList.remove('active');
        typeLoan.classList.remove('active');
        typeLending.classList.remove('active');
        form.classList.remove('loan-content');
        form.classList.remove('lending-content');
    });
}

if(addLoanBtn){
    addLoanBtn.addEventListener('click', () => {
        form.classList.add('loan-content');
    })
}
if(addLendingBtn){
    addLendingBtn.addEventListener('click', () => {
        form.classList.add('lending-content');
    })
}
if(cancelBtn){
    cancelBtn.addEventListener('click', () => {
        form.classList.remove('loan-content');
        form.classList.remove('lending-content');
        form.reset();
        formLoan.classList.remove('active');

        typeLoan.classList.remove('active');
        typeLending.classList.remove('active');

    })
}

form.addEventListener('submit', (e) => {
    e.preventDefault(); // Ngăn form submit mặc định
    
    if (form.classList.contains('loan-content')) {
        form.action = '/loan/create';
    } else if (form.classList.contains('lending-content')) {
        form.action = '/lending/create';
    }
    
    form.submit();
});

if(cancelPaymentBtn){
    cancelPaymentBtn.addEventListener('click', () => {
        window.location.href = '/loan';
    })
}
if(closePaymentBtn){
    closePaymentBtn.addEventListener('click', () => {
        window.location.href = '/loan';
    })
}