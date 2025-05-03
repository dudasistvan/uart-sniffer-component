#pragma once

#include "esphome.h"

namespace esphome {
namespace uart_sniffer {

class UARTSnifferTextSensor : public TextSensor {
 public:
  UARTSnifferTextSensor(UARTComponent *uart);
  void setup() override;
  void dump_config() override;

 protected:
  UARTComponent *uart_;
};

}  // namespace uart_sniffer
}  // namespace esphome
