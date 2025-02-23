Feature: Revisar y validar documentación de proveedores

  Scenario: Revisar la documentación preliminar
    Given una solicitud con documentación completa
    When el sistema revisa la documentación preliminar
    Then se debe verificar que la documentación esté completa

  Scenario: Solicitar documentación faltante
    Given una solicitud con documentación incompleta
    When el sistema identifica la documentación faltante
    Then se debe solicitar la documentación faltante al proveedor