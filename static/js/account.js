// add account
const addAccountBtn = document.querySelector('.add-account-btn');
const addAccountModal = document.querySelector('.add-account-modal');
const closeAddAccountBtn = document.querySelector('.close-add-account-btn');
const cancelAddBtn = document.querySelector('.cancel-add-btn');
if (addAccountBtn && addAccountModal && closeAddAccountBtn && cancelAddBtn) {
    addAccountBtn.addEventListener('click', () => {
        addAccountModal.classList.toggle('active');
    });
    
    closeAddAccountBtn.addEventListener('click', () => {
        addAccountModal.classList.toggle('active');
    });
    
    cancelAddBtn.addEventListener('click', () => {
        addAccountModal.classList.toggle('active');
    });
} else {
    console.error('Xem lỗi ở file account.js line 1-19');
}

// transfer money
const addTransferBtn = document.querySelector('.transfer-btn');
const addTransferModal = document.querySelector('.add-transfer-modal');
const closeTransferBtn = document.querySelector('.close-transfer-btn');
const cancelTransferBtn = document.querySelector('.cancel-transfer-btn');
if (addTransferBtn && addTransferModal && closeTransferBtn && cancelTransferBtn) {
    addTransferBtn.addEventListener('click', () => {
        addTransferModal.classList.toggle('active');
    });
    
    closeTransferBtn.addEventListener('click', () => {
        addTransferModal.classList.toggle('active');
    });

    cancelTransferBtn.addEventListener('click', () => {
        addTransferModal.classList.toggle('active');
    });
} else {
    console.error('Xem lỗi ở file account.js line 25-31');
}