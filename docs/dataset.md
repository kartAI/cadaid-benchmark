# Dataset

> TODO: written after the repo is set up.

## Source
<!-- Where the drawings come from, how they were collected, time period. -->

## Assembly
<!-- Pipeline from raw documents to data/images (PDF -> page images, filtering, deduplication). -->

## Labeling
<!-- Annotation tool, who labeled, guidelines per class, quality control. Bounding boxes are pixel [x1, y1, x2, y2]. -->

## Classes
| id | class | description |
|----|-------|-------------|
| 0 | fasade | |
| 1 | plantegning | |
| 2 | situasjonskart | |
| 3 | snitt | |

## Splits
<!-- How train/val/test were made (see counts in the README). -->

## Format
`data/labels.json` is a list with one record per image:
`{"image", "split", "width", "height", "labels": [{"label", "text", "bbox"}]}`.
Images with an empty `labels` list contain none of the four classes.

## Limitations, license and privacy
<!-- Known label noise, class imbalance, license, anonymisation. -->
