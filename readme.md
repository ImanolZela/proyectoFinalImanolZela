user: imanol
Password: i02381792

{% for producto in productos %}
    {% if producto.categoria == 'Componentes' %}
        <!-- Mostrar productos de la categoría Componentes -->
    {% elif producto.categoria == 'Laptops' %}
        <!-- Mostrar productos de la categoría Laptops -->
    {% elif producto.categoria == 'Periféricos' %}
        <!-- Mostrar productos de la categoría Periféricos -->
    {% elif producto.categoria == 'Monitores' %}
        <!-- Mostrar productos de la categoría Monitores -->
    {% elif producto.categoria == 'Electrónica' %}
        <!-- Mostrar productos de la categoría Electrónica -->
    {% endif %}
{% endfor %}
