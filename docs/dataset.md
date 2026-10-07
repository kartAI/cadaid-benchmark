# Dataset

The benchmark data is the drawing-type dataset built for **CADAid**, a bachelor thesis at the University of Agder (UiA, 2024) carried out with Norkart as part of the KartAi innovation project (Kristiansand kommune, Norkart, Kartverket, UiA et al.). The thesis builds on earlier work by Julia Jørstad during an internship at Norkart in autumn 2023, and the dataset was later extended by Norkart's research projects.

> Austeid, Jørstad and Thorjussen, *CADAid: Validation of Architectural Drawings Powered by Machine Learning*, HPR/D-24-005, supervisor Sondre Glimsdal, University of Agder, 2024.

This repository holds version 1.0.0: 1134 page images. Details that were not recorded are marked as such.

## Source

- **Motivation.** In November 2023 the Norwegian Building Authority (DiBK) reported that on average 35 % of building applications are deficient, and that about 25 % of those deficiencies relate to architectural drawings (missing or wrong drawing types, site plans). The dataset exists to train a model that recognises which drawing types an applicant has uploaded.
- **Origin.** Building applications and their drawings are public data. The images were collected manually from the publicly available digital archives of Norwegian municipalities: Kristiansand, Sarpsborg, Sandnes and Stavanger.
- **Content.** Pages from building applications: the four drawing types normally required (below), plus other documents in the same applications. Drawings include CAD exports, scans and, occasionally, hand-drawn floor plans.
- **Time period.** The data was collected between autumn 2023 and spring 2024.

## Assembly

1. A first dataset came from the preliminary internship work (autumn 2023).
2. It was expanded with further applications downloaded by hand from the municipal archives.
3. Pages that contain none of the four classes were deliberately kept as **background images** (other technical drawings, text documents, photos). They reduce false positives, i.e. a model calling something a drawing when it is not.

The images are page images (JPEG), one per page, named `<application>_page_<n>.jpg`. Page sizes vary a lot; most are between about 1500 and 4500 px wide.

Not recorded: the exact PDF-to-image conversion settings, any deduplication, and the exact filtering rules. Collection was manual and time-consuming.

## Labeling

- **Tool.** LabelImg, a locally installed annotation program.
- **Annotators.** The project's student authors. No labeling guidelines or review step were recorded.
- **Guideline.** Draw a tight bounding box around each drawing on the page and assign one of four classes. A page can hold several drawings, including several of the same class. Elevation sheets typically show four facades, so one `fasade` page often has four boxes (one per side of the building). Pages with no drawing of the four types get no boxes.
- **Original format.** One YOLO `.txt` file per image (class id and normalised box). In this repository the boxes are stored as pixel `[x1, y1, x2, y2]` (see [Format](#format)).
- **Quality control.** No manual second pass was recorded. Annotation was done under time pressure.

## Classes

| id | class | description |
|----|-------|-------------|
| 0 | fasade | Elevation drawing. A 2D view of the building's exterior from one side. Required to show cardinal directions. Usually four per sheet. |
| 1 | plantegning | Floor plan. A 2D top-down drawing of the room layout of one storey. Required to show room types. Includes hand-drawn plans. |
| 2 | situasjonskart | Site plan. A map of the property and its surroundings (neighbouring buildings, parcel boundaries, building placement). Visually very uniform, often a municipal map extract. |
| 3 | snitt | Section drawing. A building "sliced" vertically to show floors and internal and external heights, with roof ridge (mønehøyde) and cornice height (gesimshøyde). |

The application rules also require a scale (målestokk) on every drawing. Scale, cardinal direction and room types are **not** labeled here.

## Format

`data/labels.json` is a list with one record per image:
`{"image", "split", "width", "height", "labels": [{"label", "text", "bbox"}]}`.
Images with an empty `labels` list contain none of the four classes.

- `label` is the class id from the table above, `text` the class name.
- `bbox` is pixel `[x1, y1, x2, y2]` in the coordinates of the image at `width` × `height`.

## Limitations, license and privacy

- **Class imbalance.** `fasade` dominates (680 boxes) because one elevation sheet gives about four boxes. `situasjonskart` is rarest (195), but it is easy anyway: large boxes and very similar appearance.
- **Hard class.** `snitt` is the weakest class. A technical (non-building) section drawing was misclassified as a building section, which is why background images matter.
- **Box scale.** Boxes vary a lot in size, from a single facade to a whole-page site plan, so box size varies as well as class frequency.
- **Label noise.** Labeled by hand with no second-pass review. Expect some inconsistent box tightness and borderline cases (several drawings on one page, partial drawings). The small model overfit in some cross-validation folds, which is consistent with a small dataset.
- **Size.** About 1100 images, below the 1000-1500 images per class often recommended for image recognition.
- **Geography.** Four Norwegian municipalities, mostly in southern Norway. Local drawing conventions and templates are over-represented.
- **License.** Not stated. The source documents are public records from municipal archives.
- **Privacy.** The images are real building applications. Some filenames carry street addresses, and the images may show property identifiers (gnr/bnr), names or hand-written notes. No anonymisation was recorded. Do not assume the data is anonymised.
