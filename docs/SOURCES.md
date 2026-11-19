# References and supporting documentation

## Construction and adjustment

- [Easy BITX Version 1 construction manual](https://amateurradiokits.in/wp-content/uploads/2020/04/Building-Easy-Bitx-Ver-1.pdf) — construction, schematic and alignment reference.
- [Easy BITX VU3GAO firmware guide](https://amateurradiokits.in/wp-content/uploads/2021/10/Easy_BITX_Firmware_vu3gao.pdf) — firmware configuration and calibration.
- [Easy BITX coil winding guide](https://amateurradiokits.in/wp-content/uploads/2021/09/Easy-Bitx-Coils1.pdf) — toroidal coils and RF chokes.

The above links point to external materials. This repository also includes [Version 2.0 schematic and PCB drawings](../hardware/). The two hardware versions should not be treated as interchangeable without checking circuit details.

## Firmware sources

- [VU3SUA EasyBitx v1.3](https://github.com/vu3sua/EasyBitx_v1.3) — Arduino firmware source; credits Nitin William (VU3GAO). A copy is available at [firmware/EasyBitx_v1.3.ino](../firmware/EasyBitx_v1.3.ino).
- [VU3GAO Easy BITX mono-band firmware v1.5](https://github.com/saqks-ahm/Easy_Bitx_Mono_Band) — Arduino firmware source, with GPL-3.0 license in the upstream repository. A copy is available at [firmware/EasyBitx_vu3gao_v1.5.ino](../firmware/EasyBitx_vu3gao_v1.5.ino).

The v1.3 source uses a 10 MHz IF and defines a 7.000–7.300 MHz 40-meter tuning range. The firmware versions may differ in pin assignments, settings and features.

The v1.3 upstream repository does not provide an explicit license. Separate licensing should be established for hardware drawings and externally hosted documentation.
