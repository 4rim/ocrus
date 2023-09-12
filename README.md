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

## Future plans:

- Probably use a better OCR service than Tesseract. I'm thinking of using
  [this](https://huggingface.co/docs/transformers/model_doc/vision-encoder-decoder)
  model, though that would require me to study up a bit on PyTorch - I don't
  mind!
- Make script compatible with Windows/Mac/Linux filesystems - should be a minor
  fix.
- (distant-er future) Add a GUI front-end that works with ShareX/other
  screenshot apps. Could do this with Qt, could do this with
  [Gooey](http://chriskiehl.com/article/gooey-as-a-universal-frontend), which
  looks quite intuitive to use :)
