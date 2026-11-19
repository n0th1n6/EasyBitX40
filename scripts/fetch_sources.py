#!/usr/bin/env python3
"""Download Easy BITX public documentation and optional v1.3 firmware for local reference."""
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "docs" / "downloaded"
FILES = {
    "Building-Easy-Bitx-Ver-1.pdf": "https://amateurradiokits.in/wp-content/uploads/2020/04/Building-Easy-Bitx-Ver-1.pdf",
    "Easy_BITX_Firmware_vu3gao.pdf": "https://amateurradiokits.in/wp-content/uploads/2021/10/Easy_BITX_Firmware_vu3gao.pdf",
    "Easy-Bitx-Coils1.pdf": "https://amateurradiokits.in/wp-content/uploads/2021/09/Easy-Bitx-Coils1.pdf",
}

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for name, url in FILES.items():
        target = DEST / name
        try:
            request = Request(url, headers={"User-Agent": "Mozilla/5.0 (EasyBitX40 reference archive)"})
            with urlopen(request, timeout=30) as response:
                data = response.read()
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            target.write_bytes(data)
            print(f"Downloaded: {target} ({len(data)} bytes)")
        except Exception as exc:
            print(f"Unable to download {name}: {exc}")
            print(f"  Source: {url}")

    # Fetch v1.3 for local study. The upstream repository has no declared
    # redistribution license, so the file is not committed in this archive.
    url = "https://raw.githubusercontent.com/vu3sua/EasyBitx_v1.3/main/EasyBitx_v1.3.ino"
    target = ROOT / "firmware" / "upstream-local" / "EasyBitx_v1.3.ino"
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 (EasyBitX40 reference archive)"})
        with urlopen(request, timeout=30) as response:
            data = response.read()
        if b"#include" not in data:
            raise ValueError("response does not look like Arduino source")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f"Downloaded upstream firmware for local study: {target}")
    except Exception as exc:
        print(f"Unable to retrieve v1.3 source: {exc}")
        print(f"  Source: {url}")

if __name__ == "__main__":
    main()
