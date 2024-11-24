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

const filterSelect = document.querySelector('.filter-select');
const searchInput = document.querySelector('.search-input');
const deleteBtn = document.querySelector('.delete-btn');
const editBtn = document.querySelector('.edit-btn');
const editAccountModal = document.querySelector('.edit-account-modal');
const closeEditAccountBtn = document.querySelector('.close-edit-account-btn');
const cancelEditBtn = document.querySelector('.cancel-edit-btn');

if (filterSelect && searchInput) {
    filterSelect.addEventListener('change', () => {
        window.location.href = `/account?filter=${filterSelect.value}`;
    });

    searchInput.addEventListener("keyup", (event) => {
        if (event.key === "Enter") {
            window.location.href = `/account?search=${searchInput.value}`;
            }
        });
} else {
    console.error('Xem lỗi ở file account.js line 47-51');
}


if (deleteBtn && editBtn && closeEditAccountBtn && cancelEditBtn) {
    deleteBtn.addEventListener('click', () => {
        console.log('delete');
    });

    editBtn.addEventListener('click', () => {
        editAccountModal.classList.add('active');
    });

    closeEditAccountBtn.addEventListener('click', () => {
        editAccountModal.classList.remove('active');
    });

    cancelEditBtn.addEventListener('click', () => {
        editAccountModal.classList.remove('active');
    });
} else {
    console.error('Xem lỗi ở file account.js line 66-71');
}

