# features/feature1_proveedores.feature

Feature: Receptar y gestionar solicitudes de proveedores

  Scenario: Receptar una solicitud de proveedor
    Given un proveedor envía una solicitud
    When el sistema recibe la solicitud
    Then la solicitud debe ser registrada en el sistema

  Scenario: Revisar el estado de una solicitud
    Given una solicitud de proveedor registrada
    When el sistema consulta el estado de la solicitud
    Then se debe mostrar el estado actual de la solicitud