#include "dal.h"
#include <math.h>

void sleep(int time) { pause(time); }         // POWER
int sum(int a, int b, int c) { return a+b+c; } // COMPILER SUPPORT





void setup()
{
    microbug_setup();
}

void user_program()
{
    while(1) {// Forever
scroll_string_image( StringImage( "HELLO LOADER" ),50 );
delay( 70 );
scroll_string_image( StringImage( "[:]" ),50 );
delay( 30 );
}
;
}

int main(void)
{
        init();

#if defined(USBCON)
//        USBDevice.attach();
#endif
        setup(); // Switches on "eyes", and switches to bootloader if required
        enable_power_optimisations();
set_eye('L', LOW);  // Switch off eyes if bootloader not required
set_eye('R', LOW);
        pause(dal_pre_pause_time);
        user_program();
        //        if (serialEventRun) serialEventRun();
        if (dal_screen_hold_time) { 
            pause(dal_screen_hold_time);
            clear_display();
            eye_off("A");
            eye_off("B");
            while (true) {
                sleep(1000);
            }
            return 0;
        } else {
            while(1) {
                pause(dal_screen_hold_time);
                }
        }
}


