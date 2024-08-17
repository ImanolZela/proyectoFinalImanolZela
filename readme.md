## Resumen del Sitio Web

**Factory** es un marketplace diseñado específicamente para la compra y venta de productos tecnológicos y electrónicos. En este sitio, los usuarios pueden publicar anuncios de sus productos para que otros usuarios interesados puedan verlos y contactar para realizar una transacción.

### ¿Qué se puede hacer en Factory?

- **Publicar Productos**: Los vendedores pueden registrar y publicar productos tecnológicos y electrónicos, especificando detalles como nombre, precio, descripción, y subir imágenes del producto.
  
- **Explorar y Buscar**: Los compradores pueden navegar por las diferentes categorías de productos, como componentes, laptops, monitores, periféricos y electrónica, para encontrar lo que necesitan.
  
- **Entablar Contacto**: Una vez que un comprador encuentra un producto de su interés, puede ponerse en contacto con el vendedor para negociar los detalles de la transacción.

- **Registro y Gestión de Usuarios**: Los usuarios pueden registrarse en el sitio para crear un perfil, que les permitirá gestionar sus publicaciones y realizar compras.

### Explicacion del contenido
  En esta sección se proporcionan detalles clave sobre el proyecto, incluyendo un video explicativo y un enlace a los casos de prueba utilizados para verificar la funcionalidad del sitio.

  - **[Video Explicativo del Sitio](https://youtu.be/4oMaMwalIQw)**: En este video se ofrece una explicacion general del sitio, incluyendo una demostración de sus principales características y funcionalidades.

  - **[Casos de Prueba](https://docs.google.com/spreadsheets/d/1LzyH7IkuY0RAXvbMSutm5OFLngtCm8VPL2OD704ht-4/edit?usp=sharing)**: Acceso a los casos de prueba para validar las diferentes funcionalidades del sitio.

## Usuarios de Prueba

Para facilitar la evaluación del proyecto, se han creado usuarios de prueba con diferentes roles. A continuación, se proporciona una lista de estos usuarios, incluyendo sus credenciales de acceso:

| Nombre de Usuario | Rol            | Correo Electrónico        | Contraseña        |
|-------------------|----------------|---------------------------|-------------------|
| **Imanol**        | Administrador  | imanolza@gmail.com        | r47322071         |
| **userprueba**    |usuario/vendedor| u@p.com                   | i02381792         |

## Composición del Proyecto

El sitio web está desarrollado utilizando el framework Django y se organiza en dos aplicaciones principales: **appMain** y **appCuentas**. A continuación se describe la estructura y los componentes de cada una.

### appMain

La aplicación **appMain** es la encargada de gestionar los productos y las operaciones relacionadas. Aquí se encuentran algunos de los modelos principales del sitio, como **Producto** y **Comentario**. Esta aplicación maneja todo lo relacionado con la creación, actualización, eliminación y visualización de productos.

**Estructura de appMain:**
- **static/appMain/assets/img/products/**: Contiene las imágenes relacionadas con los productos.
- **static/appMain/assets/css/**: Contiene los archivos CSS para el diseño de las páginas relacionadas con los productos, como `detailsProducts.css`, `products.css`, y `style.css`.
- **static/appMain/assets/js/**: Contiene los archivos JavaScript que se utilizan en las páginas de productos.
- **templates/appMain/**: Contiene las plantillas HTML que renderizan las vistas para gestionar los productos, como `createProducts.html`, `updateProducts.html`, `detailsProducts.html`, entre otras.

**Modelos en appMain:**
- **Producto**: Representa un producto tecnológico o electrónico que se puede publicar en el sitio.
- **Comentario**: Permite a los usuarios dejar comentarios en los productos publicados.

### appCuentas

La aplicación **appCuentas** gestiona todo lo relacionado con los usuarios, como el registro, inicio de sesión y la administración del perfil.

**Estructura de appCuentas:**
- **static/appCuentas/assets/img/**: Contiene imágenes utilizadas en la interfaz de usuario, como imágenes predeterminadas para los perfiles.
- **static/appCuentas/assets/css/**: Contiene los archivos CSS para el diseño de las páginas relacionadas con las cuentas de usuario, como `login.css`, `perfil.css`, y `register.css`.
- **static/appCuentas/assets/js/**: Contiene los archivos JavaScript utilizados en las páginas de usuarios.
- **templates/appCuentas/**: Contiene las plantillas HTML que renderizan las vistas para la gestión de cuentas de usuario, como `login.html`, `register.html`, `perfil.html`, y `updatePassword.html`.

**Modelo Principal:**
- **Perfil**: Representa el perfil del usuario, incluyendo información como nombre, dirección, y foto de perfil.

### Estructura General

Ambas aplicaciones están diseñadas para trabajar en conjunto. La appMain se enfoca en el manejo de productos, mientras que la appCuentas maneja todo lo relacionado con los usuarios.

## Modelos y Relaciones

El proyecto se basa en tres modelos principales distribuidos entre las aplicaciones **appMain** y **appCuentas**. A continuación, la descripción cada uno de estos modelos y sus relaciones.

#### 1. Modelo Perfil (en `appCuentas`)
El modelo **Perfil** está relacionado uno a uno con el modelo de usuario estándar de Django (`User`). Este modelo almacena información adicional del usuario que no se incluye por defecto en el modelo de usuario de Django.

- **Relación**: Cada usuario (`User`) tiene un perfil asociado. La relación es `OneToOneField`, lo que significa que un usuario solo puede tener un perfil y viceversa.
- **Campos Principales**:
  - **Teléfono**: Almacena el número de teléfono del usuario.
  - **Ciudad**: Almacena la ciudad del usuario.
  - **Imagen de Perfil**: Almacena la imagen del perfil del usuario, que se sube a un directorio específico, el cual es la carpeta `media/perfil` del proyecto.

#### 2. Modelo Producto (en `appMain`)
El modelo **Producto** representa los productos que los usuarios pueden publicar en el sitio. Cada producto pertenece a un usuario (el vendedor) y tiene información como nombre, precio, categoría, descripción, e imagen.

- **Relación**: Cada producto está relacionado con un usuario (`User`) mediante una `ForeignKey`, lo que significa que un usuario puede tener múltiples productos, pero cada producto solo tiene un vendedor.
- **Campos Principales**:
  - **Nombre**: Almacena el nombre del producto.
  - **Precio**: Almacena el precio del producto con dos decimales.
  - **Categoría**: Especifica la categoría del producto (por ejemplo, componentes, laptops, periféricos).
  - **Descripción**: Proporciona detalles sobre el producto.
  - **Imagen**: Almacena la imagen del producto, que se sube a un directorio específico, el cual es la carpeta `media/productos` del proyecto.

#### 3. Modelo Comentario (en `appMain`)
El modelo **Comentario** permite a los usuarios dejar comentarios en los productos publicados. Cada comentario está asociado a un producto y a un usuario (el autor del comentario).

- **Relación**: 
  - Un producto puede tener múltiples comentarios (`ForeignKey` con `related_name='comentarios'`).
  - Un usuario puede dejar múltiples comentarios, pero cada comentario solo pertenece a un usuario y a un producto específico.
- **Campos Principales**:
  - **Producto**: Relaciona el comentario con un producto específico.
  - **Usuario**: Relaciona el comentario con el autor del comentario.
  - **Texto**: Contiene el contenido del comentario.
  - **Fecha**: Almacena la fecha y hora en que se creó el comentario (se genera automáticamente).

## Vistas (Views)

Las vistas en el proyecto están distribuidas entre dos aplicaciones principales: **appMain** y **appCuentas**. A continuación, se detalla la funcionalidad principal de cada una.

#### Vistas de appMain

1. **inicio**: Renderiza la página de inicio (`index.html`), proporcionando un punto de entrada para los usuarios del sitio.

2. **about**: Renderiza la página "Acerca de" (`about.html`), ofreciendo información sobre el sitio.

3. **createProducts**: Permite a los usuarios autenticados crear y publicar nuevos productos. Antes de permitir la publicación, verifica que el perfil del usuario esté configurado (teléfono y ciudad obligatorios). Si el perfil no está configurado, muestra un mensaje indicativo en la misma página.

4. **products**: Filtra y muestra los productos según su categoría (componentes, laptops, periféricos, monitores, electrónica) en la página `products.html`.

5. **detailsProduct (DetailView)**: Muestra los detalles de un producto específico en la página `detailsProducts.html`.

6. **updateProducts (UpdateView)**: Permite a los usuarios autenticados actualizar la información de un producto existente a través de un formulario en la página `updateProducts.html`.

7. **deleteProducts (DeleteView)**: Permite a los usuarios autenticados eliminar un producto. Tras la eliminación, redirige a la lista de productos.

8. **comentProducts (CreateView)**: Permite a los usuarios autenticados agregar comentarios a los productos en la página `detailsProducts.html`. Los comentarios se asocian con el producto y el usuario que los crea.

#### Vistas de appCuentas

1. **userlogin**: Gestiona el proceso de inicio de sesión de los usuarios. Verifica las credenciales y autentica al usuario. En caso de error, muestra mensajes de error adecuados en la página de inicio de sesión (`login.html`).

2. **register**: Permite a nuevos usuarios registrarse en el sitio. Tras un registro exitoso, se crea automáticamente un perfil para el usuario y se autentica al usuario, redirigiéndolo a la página de inicio.

3. **perfil**: Permite a los usuarios autenticados ver y actualizar su información de perfil, incluyendo teléfono, ciudad e imagen de perfil, a través de un formulario en la página `perfil.html`.

4. **updatePassword (PasswordChangeView)**: Permite a los usuarios autenticados cambiar su contraseña. Tras un cambio exitoso, se muestra un mensaje de confirmación en la misma página (`updatePassword.html`).

### Consideraciones de Seguridad

- **LoginRequiredMixin y @login_required**: Varias vistas están protegidas mediante decoradores y mixins que aseguran que solo los usuarios autenticados puedan acceder a ellas.
- **Mensajes de Error y Confirmación**: Se implementan mensajes de error y confirmación para mejorar la experiencia del usuario, asegurando que los usuarios sean informados adecuadamente durante los procesos de inicio de sesión, registro y actualización de datos.

## Configuración de URLs

El proyecto está organizado con tres archivos principales de configuración de URLs: uno a nivel de proyecto y dos específicos para las aplicaciones **appMain** y **appCuentas**. A continuación, la explicación cómo están estructuradas las rutas en cada archivo.

#### 1. URLs a Nivel de Proyecto

Este archivo es el principal punto de entrada para las rutas de todo el proyecto. Aquí se incluyen las rutas de las aplicaciones principales y la configuración para servir archivos estáticos.

- **Rutas Importantes**:
  - `path('admin/', admin.site.urls)`: Ruta para acceder al panel de administración de Django.
  - `path('', include('appMain.urls'))`: Incluye todas las rutas definidas en la aplicación **appMain**.
  - `path('sesion/', include('appCuentas.urls'))`: Incluye todas las rutas definidas en la aplicación **appCuentas**.
  - `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`: Configura la ruta para servir archivos de medios (imágenes, etc.) en desarrollo.

#### 2. URLs de appMain

Este archivo define las rutas relacionadas con la gestión de productos y la navegación básica del sitio.

- **Rutas Importantes**:
  - `path('', inicio, name='main')`: Ruta para la página de inicio.
  - `path('pagina-about/', about, name='about')`: Ruta para la página "Acerca de".
  - `path('crear-producto/', createProducts, name='createProducts')`: Ruta para crear un nuevo producto.
  - `path('pagina-products/', products, name='products')`: Ruta para ver todos los productos organizados por categoría.
  - `path('details/<pk>/', detailsProduct.as_view(), name='details')`: Ruta para ver los detalles de un producto específico.
  - `path('actualizar-producto/<pk>/', updateProducts.as_view(), name='updateProducts')`: Ruta para actualizar un producto existente.
  - `path('borrar-producto/<pk>/', deleteProducts.as_view(), name='deleteProducts')`: Ruta para eliminar un producto.
  - `path('producto/<pk>/coment/', comentProducts.as_view(), name='comentar')`: Ruta para agregar un comentario a un producto.

#### 3. URLs de appCuentas

Este archivo define las rutas relacionadas con la autenticación y gestión de cuentas de usuario.

- **Rutas Importantes**:
  - `path('pagina-login/', userlogin, name='login')`: Ruta para iniciar sesión.
  - `path('pagina-register/', register, name='register')`: Ruta para registrar un nuevo usuario.
  - `path('pagina-perfil/', perfil, name='perfil')`: Ruta para ver y actualizar el perfil del usuario.
  - `path('updatePassword/', updatePassword.as_view(), name='updatePassword')`: Ruta para cambiar la contraseña del usuario.
  - `path('logout/', LogoutView.as_view(template_name='appMain/index.html'), name='logout')`: Ruta para cerrar sesión, redirigiendo a la página de inicio.

## Conclusión

Factory es un proyecto diseñado para ofrecer un marketplace especializado en productos tecnológicos y electrónicos, destacando por su funcionalidad, seguridad y facilidad de uso. Desarrollado con el framework Django, el proyecto sigue una estructura modular que facilita su mantenimiento y escalabilidad, asegurando que cada componente funcione de manera integrada y eficiente.

El desarrollo de Factory implicó la implementación de funcionalidades clave, como la gestión y autenticación de usuarios, la creación y visualización de productos, y la interacción a través de comentarios. Estas características no solo hacen que el sitio sea intuitivo y práctico para los usuarios finales, sino que también reflejan un enfoque meticuloso en la seguridad y la experiencia de usuario.

La estructura clara del proyecto permite futuras expansiones, lo que hace de Factory una base sólida sobre la cual se pueden construir nuevas funcionalidades. Desde la organización de productos en diferentes categorías hasta la personalización de perfiles de usuario, cada aspecto de Factory ha sido cuidadosamente diseñado para cumplir con los estándares de un marketplace moderno y competitivo.

Este proyecto demuestra la aplicación efectiva de tecnologías web modernas y prácticas de desarrollo, y está preparado para enfrentar las demandas de un entorno de producción real.








