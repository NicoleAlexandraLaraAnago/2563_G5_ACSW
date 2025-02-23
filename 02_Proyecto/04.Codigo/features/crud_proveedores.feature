# features/crud_proveedores.feature

Feature: CRUD de Proveedores

  Scenario: Crear un nuevo proveedor
    Given un nuevo proveedor con nombre "Proveedor A" y contacto "contacto@proveedora.com"
    When el sistema registra el proveedor
    Then el proveedor debe ser guardado en la base de datos

  Scenario: Leer información de un proveedor
    Given un proveedor con ID 1 registrado en el sistema
    When el sistema consulta la información del proveedor
    Then se debe mostrar la información del proveedor

  Scenario: Actualizar información de un proveedor
    Given un proveedor con ID 1 registrado en el sistema
    When el sistema actualiza el contacto del proveedor a "nuevo_contacto@proveedora.com"
    Then la información del proveedor debe ser actualizada en la base de datos

  Scenario: Eliminar un proveedor
    Given un proveedor con ID 1 registrado en el sistema
    When el sistema elimina el proveedor
    Then el proveedor debe ser eliminado de la base de datos