# EasyBitX40

Reference archive for the **Easy BITX** mono-band HF SSB amateur radio transceiver, with an emphasis on the 40-meter version. The repository brings together Arduino VFO/BFO firmware, construction documentation, circuit and PCB drawings, and a bill of materials.

This is an independent archive, not an official INKITS release.

## Contents

| Section | Description |
| --- | --- |
| [Documentation](docs/README.md) | Construction manual, coils, AGC, voltage readings, and enclosure notes |
| [Hardware](hardware/README.md) | Easy BITX Version 2.0 schematic and PCB reference drawings, and component BOM |
| [Firmware v1.3](firmware/EasyBitx_v1.3.ino) | Arduino Nano / Si5351 VFO/BFO sketch hosted by VU3SUA |
| [Firmware v1.5](firmware/EasyBitx_vu3gao_v1.5.ino) | VU3GAO's later VFO/BFO sketch |
| [Sources](docs/SOURCES.md) | Source repositories, external references, and provenance |
| [Retrieval script](scripts/fetch_sources.py) | Optional utility for retrieving upstream files |

## Construction documentation

The documents below are available directly in this repository:

| Document | File |
| --- | --- |
| Easy BITX Version 1 construction manual | [Building-Easy-Bitx-Ver-1.pdf](docs/Building-Easy-Bitx-Ver-1.pdf) |
| Coil reference | [Easy-Bitx-Coils.pdf](docs/Easy-Bitx-Coils.pdf) |
| Automatic gain control (AGC) reference | [AGC.pdf](docs/AGC.pdf) |
| Voltage readings | [Voltage-Readings.pdf](docs/Voltage-Readings.pdf) |
| Boxing / enclosure reference | [Boxing-Easy-Bitx.pdf](docs/Boxing-Easy-Bitx.pdf) |

See the [documentation index](docs/README.md) for a complete directory guide.

## Hardware

The [hardware directory](hardware/README.md) contains:

- A complete Easy BITX Version 2.0 circuit schematic and seven individual schematic sections
- A complete PCB drawing and seven individual PCB drawing sections
- A bill of materials in Excel format

The schematic and PCB PDFs are **reference drawings**, not verified native CAD source files or PCB-manufacturing Gerbers. The Version 1 construction manual and Version 2.0 hardware drawings are identified separately because their circuit details may differ.

## Firmware

Both included sketches describe an **Arduino Nano** and **Si5351** VFO/BFO arrangement using a 16×2 character LCD, rotary encoder, and 10 MHz IF.

- **v1.3** — [original source](https://github.com/vu3sua/EasyBitx_v1.3), credits Nitin William (VU3GAO), with a 7.000–7.300 MHz 40-meter tuning range.
- **v1.5** — [original source](https://github.com/saqks-ahm/Easy_Bitx_Mono_Band), with additional firmware functionality, including EEPROM and S-meter-related features.

Check the board revision, pin connections, IF/BFO frequencies, and calibration settings before using either sketch with a particular board.

## Acknowledgements

- **Sunil Lakhani (VU3SUA) / INKITS** — Easy BITX kit and hardware design
- **Nitin William (VU3GAO)** — Easy BITX firmware, which also credits earlier work by J. CesarSound
- **Saquib Ahmed** — kindly shared the hardware documentation archived here

Thanks to the original contributors for making these materials available to the amateur radio community.

## Licensing

The v1.5 upstream firmware includes a [GNU GPL-3.0 license](firmware/LICENSE). The v1.3 upstream repository does not explicitly declare a license. Do not assume the firmware license also covers schematic drawings, PCB artwork, construction manuals, or other third-party materials. Original attributions remain with the respective authors.
