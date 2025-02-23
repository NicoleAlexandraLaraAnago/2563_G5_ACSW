# features/crud_compras.feature

Feature: CRUD de Compras

  Scenario: Crear una nueva compra
    Given una nueva compra con proveedor ID 1, producto ID 1 y cantidad 10
    When el sistema registra la compra
    Then la compra debe ser guardada en la base de datos

  Scenario: Leer información de una compra
    Given una compra con ID 1 registrada en el sistema
    When el sistema consulta la información de la compra
    Then se debe mostrar la información de la compra

  Scenario: Actualizar información de una compra
    Given una compra con ID 1 registrada en el sistema
    When el sistema actualiza la cantidad de la compra a 15
    Then la información de la compra debe ser actualizada en la base de datos

  Scenario: Eliminar una compra
    Given una compra con ID 1 registrada en el sistema
    When el sistema elimina la compra
    Then la compra debe ser eliminada de la base de datos