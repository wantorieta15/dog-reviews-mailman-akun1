"""The Dog Reviews the Mailman -- make.fun program/v1 entry (Akun 1).

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

REVISI (reviser, 26 Nov 2026): teks builder DIPERTAHANKAN. Alasan:
- Suara anjing orang pertama, adegan konkret (enam tahun menggonggong,
  lalu tukang pos melambai balik), dan putaran di kata-kata terakhir --
  seluruh identitas anjing runtuh. Itu keluhan kecil yang berbalik jadi
  kekalahan, persis kriteria 2 juri (grievance / small triumph).
- Premisnya BEDA dari Akun 2 (ulasan bintang soal suap biskuit): Akun 1
  memakai krisis identitas, Akun 2 memakai format rating bintang.
  Dua akun tidak boleh berbagi premis yang sama.
- Alternatif yang dipertimbangkan (format "Five stars..."/"Zero stars,
  would bark again") sama kuatnya tapi tidak JELAS lebih kuat, dan
  format bintang justru bertabrakan dengan premis Akun 2.
- 103 karakter, di dalam gate 1-200.

Stdlib saja. Tulis LANGSUNG ke entry.txt (tanpa atomic-write) lalu
os.chmod 0o644, supaya file hasil run bisa dibaca grader.
"""

import os


def build_entry():
    """Return the review text."""
    return (
        "I barked at the mailman for six years straight. "
        "Yesterday he waved back. I don't know who I am anymore."
    )


def main():
    text = build_entry()
    # Gate check: entry must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(text) <= 200 and text.strip(), "entry violates gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
