# ocrus

Aka OC-R-US, aka (OCR)US aka OC(RUS).

Simple Python script that takes in images (screenshots of text) and uses
Tesseract OCR to spit out recognizable text. The text is then parsed so we can
use the corpus for several things, including but not limited to:

- Creates word frequency list
- Matches words with Anki flashcard files
- Allows for quick dictionary look-ups

Currently this focuses on Russian, but it could be used for any language in the
[tessdata](https://github.com/tesseract-ocr/tessdata) repo.
