Feature: Evaluar portafolio y capacidad operativa de proveedores

  Scenario: Evaluar el portafolio del proveedor
    Given una solicitud de proveedor con portafolio
    When el sistema evalúa el portafolio del proveedor
    Then se debe verificar que el portafolio cumple con los requisitos

  Scenario: Revisar la capacidad operativa
    Given una solicitud de proveedor con capacidad operativa
    When el sistema revisa la capacidad operativa del proveedor
    Then se debe verificar que el proveedor tiene la capacidad necesaria