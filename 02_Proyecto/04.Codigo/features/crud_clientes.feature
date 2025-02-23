# features/crud_clientes.feature

Feature: CRUD de Clientes

  Scenario: Crear un nuevo cliente
    Given un nuevo cliente con nombre "Cliente A" y correo "cliente@example.com"
    When el sistema registra el cliente
    Then el cliente debe ser guardado en la base de datos

  Scenario: Leer información de un cliente
    Given un cliente con ID 1 registrado en el sistema
    When el sistema consulta la información del cliente
    Then se debe mostrar la información del cliente

  Scenario: Actualizar información de un cliente
    Given un cliente con ID 1 registrado en el sistema
    When el sistema actualiza el correo del cliente a "nuevo_correo@example.com"
    Then la información del cliente debe ser actualizada en la base de datos

  Scenario: Eliminar un cliente
    Given un cliente con ID 1 registrado en el sistema
    When el sistema elimina el cliente
    Then el cliente debe ser eliminado de la base de datos