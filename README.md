# Project 3 Generative Audio

Winson Luk, wluk@ucsd.edu

## Abstract

Include your abstract here. This should be one paragraph clearly describing your concept, method, and results. This should tell us what architecture/approach you used. Also describe your creative goals, and whether you were successful in achieving them. Also could describe future directions.

## Model/Data

Model: https://storage.googleapis.com/magentadata/models/music_vae/checkpoints/hierdec-trio_16bar.tar
Sample MIDI output: [hierdec_trio_16bar_sample_4.mid](midi/hierdec_trio_16bar_sample_4.mid)
Logic Pro X project files: [logic_pro_projects](logic_pro_projects)

## Code

- Python: [trio.py](python/trio.py)
- Jupyter notebook: [trio_notebook.ipynb](python/trio_notebook.ipynb)

## Results

- [Breed - Nirvana](https://soundcloud.com/user-604304255/breed_magenta)
- [Logic - Everybody](https://soundcloud.com/user-604304255/everybody_magenta)
- [Bad Guy - Billie Eilish](https://soundcloud.com/user-604304255/badguy_magenta)
- [Childish Gambino - Bonfire](https://soundcloud.com/user-604304255/bonfire_magenta)

## Technical Notes

- Install Fluidsynth for Mac: `brew install fluidsynth && pip install pyfluidsynth`
- Save and extract the [hierdec-trio_16bar model](https://storage.googleapis.com/magentadata/models/music_vae/checkpoints/hierdec-trio_16bar.tar) into `python/content`.
- After installing `pyfluidsynth`, `magenta`, `jupyter`, and other required Python packages, run the notebook with `$ jupyter notebook`.

## Reference

- [Music VAE](https://magenta.tensorflow.org/music-vae)
- [Music VAE Github](https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae)
- [Music VAE Colab](https://colab.research.google.com/notebooks/magenta/music_vae/music_vae.ipynb)
- [Logic Pro X](https://www.apple.com/logic-pro/)
- [Logic Pro X vocal extraction](https://www.youtube.com/watch?v=imv1BvaGp-s)
- [Song BPM](https://songbpm.com)
- [Thomas the Bonfire](https://soundcloud.com/macoos1337/thomas-the-bonfire)
