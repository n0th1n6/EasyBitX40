# EasyBitX40 — source and design reference archive

A collection of firmware and design-document references for the **INKITS Easy BITX** amateur-radio SSB transceiver, with special interest in the 40 m version.

This is an independent reference archive, not an official INKITS distribution. Original designers and authors retain credit and rights.

## Collected source material

| Item | Location or link | Notes |
| --- | --- | --- |
| Arduino VFO/BFO firmware v1.5 | [firmware/EasyBitx_vu3gao_v1.5.ino](firmware/EasyBitx_vu3gao_v1.5.ino) | Original source from VU3GAO |
| Firmware GPL-3.0 license | [firmware/LICENSE](firmware/LICENSE) | Original upstream license |
| Upstream firmware repository | https://github.com/saqks-ahm/Easy_Bitx_Mono_Band | Original maintained source |
| Easy BITX version 1 construction manual | https://amateurradiokits.in/wp-content/uploads/2020/04/Building-Easy-Bitx-Ver-1.pdf | Schematics and assembly guidance |
| Easy BITX VU3GAO firmware manual | https://amateurradiokits.in/wp-content/uploads/2021/10/Easy_BITX_Firmware_vu3gao.pdf | Configuration and calibration |
| Toroid and RFC winding guide | https://amateurradiokits.in/wp-content/uploads/2021/09/Easy-Bitx-Coils1.pdf | Coil information |

**PCB and editable CAD status:** Original KiCad/Eagle schematic projects, board-layout sources, and Gerber packages have **not been located or verified**. The construction manual includes circuit schematic illustrations but is not editable CAD data.

**Version warning:** The construction manual covers Easy BITX version 1; the linked VU3GAO firmware guide concerns a later version. Check circuitry, IF frequencies and GPIO assignments against the actual hardware revision before combining them.

## Directory structure

- `firmware/`: original Arduino sketch and its upstream GPL license.
- `hardware/`: inventory and notes on what circuit design files have and have not been located.
- `docs/`: source manifest and download references for manuals.
- `scripts/`: helper to download documentation files locally.

## Download construction documentation

Run `python3 scripts/fetch_sources.py` from the repository root. The script retrieves the linked PDFs into `docs/downloaded/` for local study; PDFs are not redistributed by this repository without separate permission review.

## Arduino notes

The original sketch targets an Arduino Nano and Si5351 clock generator. Examine the sketch for dependencies including `Wire`, `EEPROMex`, and `Rotary`. This archive does not claim the firmware has been built or validated against a particular board revision.

## Authors and provenance

Original firmware: Nitin William (VU3GAO), derived in part from earlier J. CesarSound work, per source header. Original Easy BITX kit documentation: INKITS / Sunil Lakhani (VU3SUA). Preserve original authorship notices.

The firmware is distributed under the upstream GPL-3.0 license. That firmware license does **not** imply that INKITS PDFs, artwork, or unrelated hardware designs are GPL-licensed.

## Additional collected materials (November 2026)

- [VU3SUA EasyBitx v1.3 firmware](firmware/EasyBitx_v1.3.ino), supplied by the user and preserved with original source credits. The upstream v1.3 repository does not declare a redistribution license; GPL-3.0 of the separate v1.5 upstream is not asserted to cover it.
- [Easy BITX Version 2.0 hardware archive](hardware/): full schematic, schematic sections 1–7, full PCB drawing, PCB sections 1–7, and the original Excel BOM. These PDFs are drawings, not editable CAD or Gerbers.

Refer to [hardware/README.md](hardware/README.md) for the files and hardware/firmware compatibility notes.
