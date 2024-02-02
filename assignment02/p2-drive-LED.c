#include <stdint.h>

//define state globally and as a volitile char bc it can be changed by external factors
//make bytes correct lengths for what we need
volatile uint8_t* input_state = (volatile __uint8_t*)0x100A;
volatile uint32_t* output_state = (volatile __uint32_t*)0x100B;

void driveTurnSignal() {
  //read input
  uint8_t input = *input_state;

  //switch statement for input
  switch(input) {
    case 0:
      //everything off
      *output_state = 0x00;
      break;
    case 0b01:
      //turn on right turn signal
      *output_state = (*output_state & 0x0F) | 0x01;
      break;
    case 0b10:
      //turn on left turn signal
      *output_state = (*output_state & 0xF0) | 0x10;
      break;
    case 0b11:
      //turn on hazard
      *output_state = 0xFF;
      break;
  }
}



