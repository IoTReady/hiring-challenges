You are testing an embedded system based on the esp32 chip to determine which build options give you the fastest start-up time.
The embedded system, on power-up will print various logging messages.
When the system has booted, it will print “Pro cpu start user code” in the log

A sample boot log is shown below

    entry 0x40080698
    I (27) boot: ESP-IDF v4.4.4 2nd stage bootloader
    I (27) boot: compile time 19:43:33
    I (27) boot: chip revision: v3.0
    I (30) boot_comm: chip revision: 3, min. bootloader chip revision: 0
    I (37) boot.esp32: SPI Speed      : 80MHz
    I (42) boot.esp32: SPI Mode       : DIO
    I (47) boot.esp32: SPI Flash Size : 8MB
    I (51) boot: Enabling RNG early entropy source...
    I (57) boot: Partition Table:
    I (60) boot: ## Label            Usage          Type ST Offset   Length
    I (67) boot:  0 nvs              WiFi data        01 02 00009000 00004000
    I (75) boot:  1 otadata          OTA data         01 00 0000d000 00002000
    I (82) boot:  2 phy_init         RF data          01 01 0000f000 00001000
    I (90) boot:  3 factory          factory app      00 00 00010000 00100000
    I (97) boot:  4 ota_0            OTA app          00 10 00110000 00100000
    I (105) boot:  5 ota_1            OTA app          00 11 00210000 00100000
    I (112) boot:  6 storage          Unknown data     01 82 00310000 000a0000
    I (120) boot: End of partition table
    I (124) boot: Defaulting to factory image
    I (129) boot_comm: chip revision: 3, min. application chip revision: 0
    I (136) esp_image: segment 0: paddr=00010020 vaddr=3f400020 size=2fb0ch (195340) map
    I (204) esp_image: segment 1: paddr=0003fb34 vaddr=3ff80063 size=00008h (     8) load
    I (204) esp_image: segment 2: paddr=0003fb44 vaddr=3ffb0000 size=004d4h (  1236) load
    I (210) esp_image: segment 3: paddr=00040020 vaddr=400d0020 size=96868h (616552) map
    I (404) esp_image: segment 4: paddr=000d6890 vaddr=3ffb04d4 size=03330h ( 13104) load
    I (409) esp_image: segment 5: paddr=000d9bc8 vaddr=40080000 size=15468h ( 87144) load
    I (441) esp_image: segment 6: paddr=000ef038 vaddr=400c0000 size=00064h (   100) load
    I (441) esp_image: segment 7: paddr=000ef0a4 vaddr=00000000 size=00edch (  3804) 
    I (458) boot: Loaded app from partition at offset 0x10000
    I (458) boot: Disabling RNG early entropy source...
    I (471) cpu_start: Pro cpu up.
    I (471) cpu_start: Starting app cpu, entry point is 0x400813ec
    0x400813ec: call_start_cpu1 at /home/nuc/esp/esp-idf/components/esp_system/port/cpu_start.c:148

    I (0) cpu_start: App cpu up.
    I (487) cpu_start: Pro cpu start user code
    I (487) cpu_start: cpu freq: 160000000

1) Write a python regular expression to determine when the system has booted.
2) Extra credit: write a test in PyTest that reports the start up time. Assume there exists plugin called "embedded" that provides a DUT class that provides the log above. the DUT class supports an expect() method.