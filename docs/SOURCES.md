# Sources and provenance

## Manuals available locally

The following documents are archived in [docs/](README.md):

- [Easy BITX Version 1 construction manual](Building-Easy-Bitx-Ver-1.pdf)
- [Easy BITX coil reference](Easy-Bitx-Coils.pdf)
- [AGC reference](AGC.pdf)
- [Voltage readings](Voltage-Readings.pdf)
- [Boxing / enclosure reference](Boxing-Easy-Bitx.pdf)

Original publisher links are retained where available:

- [Version 1 construction manual — INKITS](https://amateurradiokits.in/wp-content/uploads/2020/04/Building-Easy-Bitx-Ver-1.pdf)
- [VU3GAO firmware configuration guide — INKITS](https://amateurradiokits.in/wp-content/uploads/2021/10/Easy_BITX_Firmware_vu3gao.pdf)
- [Coil winding guide — INKITS](https://amateurradiokits.in/wp-content/uploads/2021/09/Easy-Bitx-Coils1.pdf)

External URLs may become unavailable. The locally archived coil document and the separately linked upstream coil guide have different filenames; do not assume they are identical without comparison.

## Hardware sources

The [Version 2.0 circuit and PCB drawings and BOM](../hardware/README.md) were shared by **Saquib Ahmed**. The drawings are PDF references; editable EDA design files and manufacturing Gerbers are not included.

The Version 1 construction manual and Version 2.0 PCB documentation are different revision references.

## Firmware sources

| Revision | Upstream repository | Local copy |
| --- | --- | --- |
| 1.3 | [VU3SUA / EasyBitx_v1.3](https://github.com/vu3sua/EasyBitx_v1.3) | [EasyBitx_v1.3.ino](../firmware/EasyBitx_v1.3.ino) |
| 1.5 | [saqks-ahm / Easy_Bitx_Mono_Band](https://github.com/saqks-ahm/Easy_Bitx_Mono_Band) | [EasyBitx_vu3gao_v1.5.ino](../firmware/EasyBitx_vu3gao_v1.5.ino) |

The firmware headers credit **Nitin William (VU3GAO)** and refer to previous work by J. CesarSound. The v1.3 sketch identifies a 10 MHz IF and 7.000–7.300 MHz tuning range for 40 meters.

The v1.5 upstream repository includes GPL-3.0 terms. The v1.3 upstream repository does not declare an explicit license. Licensing of hardware documentation is separate from the firmware.
