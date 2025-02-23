# features/crud_productos.feature

Feature: CRUD de Productos

  Scenario: Crear un nuevo producto
    Given un nuevo producto con nombre "Producto A" y precio 100
    When el sistema registra el producto
    Then el producto debe ser guardado en la base de datos

  Scenario: Leer información de un producto
    Given un producto con ID 1 registrado en el sistema
    When el sistema consulta la información del producto
    Then se debe mostrar la información del producto

  Scenario: Actualizar información de un producto
    Given un producto con ID 1 registrado en el sistema
    When el sistema actualiza el precio del producto a 150
    Then la información del producto debe ser actualizada en la base de datos

  Scenario: Eliminar un producto
    Given un producto con ID 1 registrado en el sistema
    When el sistema elimina el producto
    Then el producto debe ser eliminado de la base de datos