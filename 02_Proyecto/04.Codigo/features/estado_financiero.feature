Feature: Analizar el estado financiero del proveedor

  Scenario: Analizar el estado financiero del proveedor
    Given una solicitud de proveedor con estado financiero
    When el sistema analiza el estado financiero del proveedor
    Then se debe verificar que el proveedor es financieramente estable