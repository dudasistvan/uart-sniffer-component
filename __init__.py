import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, text_sensor
from esphome.const import CONF_ID, CONF_UART_ID

CODEOWNERS = ["@your-github-name"]
DEPENDENCIES = ["uart"]

uart_sniffer_ns = cg.esphome_ns.namespace("uart_sniffer")
UARTSnifferTextSensor = uart_sniffer_ns.class_(
    "UARTSnifferTextSensor", text_sensor.TextSensor, cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = text_sensor.text_sensor_schema().extend(
    {
        cv.GenerateID(): cv.declare_id(UARTSnifferTextSensor),
        cv.GenerateID(CONF_UART_ID): cv.use_id(uart.UARTComponent),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await text_sensor.register_text_sensor(var, config)
    parent = await cg.get_variable(config[CONF_UART_ID])
    cg.add(var.set_parent(parent))
