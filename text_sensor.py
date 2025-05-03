import esphome.codegen as cg
from esphome.components.text_sensor import TextSensor
from esphome import gpio

# Regisztráljuk az új komponenst
UARTSnifferTextSensor = cg.esphome_ns.class_("UARTSnifferTextSensor", TextSensor)

async def to_code(config):
    var = cg.new_Pvariable(config["id"])
    await cg.register_component(var, config)
    cg.add(var.set_uart(config["uart_id"]))
