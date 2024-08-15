document.addEventListener('DOMContentLoaded', function () {
    var deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget; // Botón que activa el modal
            var productName = button.getAttribute('data-product-name'); // Obtiene el nombre del producto
            var productCategory = button.getAttribute('data-product-category'); // Obtiene la categoría del producto
            var url = button.getAttribute('data-url'); // Obtiene la URL de eliminación

            // Actualiza el contenido del modal
            var modalBody = deleteModal.querySelector('.modal-body');
            modalBody.textContent = `¿Estás seguro de que deseas eliminar el producto ${productName} de la lista ${productCategory}?`;

            // Actualiza la URL de eliminación en el formulario
            var form = deleteModal.querySelector('#deleteForm');
            form.action = url;
        });
    }
});