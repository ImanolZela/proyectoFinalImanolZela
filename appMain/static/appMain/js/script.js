document.addEventListener('DOMContentLoaded', function () {
    var deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget;
            var productName = button.getAttribute('data-product-name'); 
            var productCategory = button.getAttribute('data-product-category');
            var url = button.getAttribute('data-url');

            var modalBody = deleteModal.querySelector('.modal-body');
            modalBody.textContent = `¿Estás seguro de que deseas eliminar el producto ${productName} de la lista ${productCategory}?`;
            var form = deleteModal.querySelector('#deleteForm');
            form.action = url;
        });
    }
});