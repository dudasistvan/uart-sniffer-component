#include "esphome.h"
#include "uart_sniffer.h"

namespace esphome {
namespace uart_sniffer {

class UARTSnifferTextSensor : public TextSensor {
 public:
  UARTSnifferTextSensor(UARTComponent *uart) : uart_(uart) {}

  void setup() override {
    this->uart_->add_on_data_received_callback(
        [this](const uint8_t *data, size_t len) {
          std::string str_data(reinterpret_cast<const char *>(data), len);
          this->publish_state(str_data);  // Frissíti az állapotot a UART adatával
        });
  }

  void dump_config() override {
    ESP_LOGCONFIG(TAG, "UART Sniffer Text Sensor:");
    ESP_LOGCONFIG(TAG, "  UART ID: %u", this->uart_->get_id());
  }

 protected:
  UARTComponent *uart_;
};

}  // namespace uart_sniffer
}  // namespace esphome
