# EasyBitX40

A reference archive for the **Easy BITX** mono-band HF SSB transceiver, with emphasis on the 40-meter version. It brings together Arduino VFO/BFO firmware, circuit schematics, PCB drawings, a bill of materials, and links to supporting documentation.

This is an independent archive and is not an official INKITS release.

**Acknowledgement:** The hardware documentation in this archive was kindly shared by **Saquib Ahmed**.

## Repository contents

| Location | Contents |
| --- | --- |
| [firmware/EasyBitx_v1.3.ino](firmware/EasyBitx_v1.3.ino) | Easy BITX VFO/BFO firmware v1.3, from the VU3SUA repository |
| [firmware/EasyBitx_vu3gao_v1.5.ino](firmware/EasyBitx_vu3gao_v1.5.ino) | VU3GAO VFO/BFO firmware v1.5 |
| [hardware/FULL SCH.pdf](hardware/FULL%20SCH.pdf) | Complete Easy BITX Version 2.0 schematic drawing |
| [hardware/FULL PCB.pdf](hardware/FULL%20PCB.pdf) | Complete Easy BITX Version 2.0 PCB drawing |
| [hardware/](hardware/) | Individual schematic and PCB drawings, sections 1–7 |
| [hardware/BOM.xlsx](hardware/BOM.xlsx) | Bill of materials |
| [docs/SOURCES.md](docs/SOURCES.md) | Original documentation links and source references |
| [scripts/fetch_sources.py](scripts/fetch_sources.py) | Optional helper for retrieving linked documentation |

The PCB PDFs are reference drawings, **not** verified editable CAD design files or manufacturing Gerbers.

## Firmware and hardware

The Easy BITX control system uses an **Arduino Nano** and **Si5351** clock generator for VFO/BFO generation, together with a 16×2 LCD and rotary encoder. The firmware source describes a 10 MHz intermediate frequency.

Two firmware versions are included:

- **v1.3:** From the [VU3SUA repository](https://github.com/vu3sua/EasyBitx_v1.3), with source credit to Nitin William (VU3GAO). The code includes a 40-meter tuning range of 7.000–7.300 MHz.
- **v1.5:** From the [VU3GAO repository](https://github.com/saqks-ahm/Easy_Bitx_Mono_Band), adding features including EEPROM support and S-meter functionality.

Hardware revisions and firmware versions may differ in their wiring, oscillator settings and other configuration details. Verify compatibility with the actual board before programming the Arduino or operating the radio.

## Additional documentation

- [Easy BITX Version 1 construction manual](https://amateurradiokits.in/wp-content/uploads/2020/04/Building-Easy-Bitx-Ver-1.pdf)
- [Easy BITX firmware and calibration guide](https://amateurradiokits.in/wp-content/uploads/2021/10/Easy_BITX_Firmware_vu3gao.pdf)
- [Easy BITX coil winding guide](https://amateurradiokits.in/wp-content/uploads/2021/09/Easy-Bitx-Coils1.pdf)

The linked Version 1 construction manual is not necessarily applicable to the Version 2.0 PCB drawings included here.

## Credits and licensing

Easy BITX kit and hardware design: **INKITS / Sunil Lakhani (VU3SUA)**. **Hardware documentation shared by Saquib Ahmed.** Firmware: **Nitin William (VU3GAO)**, with acknowledgement of earlier work by J. CesarSound as described in the source code.

The upstream v1.5 firmware repository includes the [GNU GPL-3.0 license](firmware/LICENSE). The VU3SUA v1.3 repository does not declare a separate license. Licensing for third-party documentation and hardware drawings should not be inferred from the firmware license. All original author notices are retained.
