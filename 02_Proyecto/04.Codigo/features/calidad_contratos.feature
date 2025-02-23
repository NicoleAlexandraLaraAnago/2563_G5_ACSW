Feature: Probar calidad y formalizar contratos con proveedores

  Scenario: Probar la calidad de productos o servicios
    Given una solicitud de proveedor con productos o servicios
    When el sistema prueba la calidad de los productos o servicios
    Then se debe verificar que la calidad cumple con los estándares

  Scenario: Formalizar los términos y condiciones
    Given una solicitud de proveedor aprobada
    When el sistema formaliza los términos y condiciones
    Then se debe generar un acuerdo con los términos y condiciones

  Scenario: Revisar, ajustar y formalizar el contrato
    Given un acuerdo con términos y condiciones
    When el sistema revisa y ajusta el contrato
    Then se debe formalizar el contrato con el proveedor