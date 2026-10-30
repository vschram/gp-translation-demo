# Predicting translation quality with a Gaussian process

An interactive teaching demo: a Gaussian process predicts how well an Indonesian→English translation model will score (ChrF) at a training-set size it hasn't been trained on, and shows how uncertain that prediction is.

**Open the demo:** https://vschram.github.io/gp-translation-demo/

- Click the chart to run an experiment at that dataset size; the real measured score appears.
- Drag a measurement up or down to ask "what if it had scored this?"
- Hover to see the prediction. With one measurement, the tooltip shows the conditioning rule: expected + similarity × surprise.

The page is a single self-contained `index.html` with no dependencies. `index.html?shot=<frame>` renders fixed frames for slides (`decision`, `prior`, `kernel`, `rule`, `reveal`, `band`, `quiz1`, `quiz2`), and `capture_shots.py` saves them as PNGs with headless Edge.

Data: mBART-50 fine-tuned on Indonesian→English, from [vschram/ZeroShot_for_PSL](https://github.com/vschram/ZeroShot_for_PSL).
