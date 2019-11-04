# Project 3 Generative Audio

Winson Luk, wluk@ucsd.edu

## Abstract

AI-generated music is still far from replacing human musicians, but this project demonstrates that AI can produce music that is captivating enough to accompany many musicians.

Google Magenta provides a trained Music VAE model to generate 16-bar trios with a lead, bass, and drums. After experimenting with different temperatures and other parameters to optimize for "catchiness," the MIDI can be exported to a DAW such as Logic Pro X to process with vocals.

To exhibit the versitility of Music VAE's MIDI trios, the same repeating MIDI accompanies vocalists across the top three Western music genres: rock, pop, and hip hop. Songs with relatively non-melodic vocals have been chosen since the MIDI is scaleless and keyless. Across the three songs, the AI-generated MIDI remains unchanged - the only human inputs are the choice of instrumentation and occasional track muting, attuned to the original song.

While the resulting songs do not sound as natural as the originals, with further processing, they could potentially pass an auditory Turing test.

## Model/Data

- The model can be downloaded from https://storage.googleapis.com/magentadata/models/music_vae/checkpoints/hierdec-trio_16bar.tar
- A sample MIDI output is in [hierdec_trio_16bar_sample_4.mid](midi/hierdec_trio_16bar_sample_4.mid).
- Logic Pro X project files are in [logic_pro_projects](logic_pro_projects).
- Python and Jupyter files, along with sample MP3 results, are linked in this README below.

## Code

- Python: [trio.py](python/trio.py)
- Jupyter notebook: [trio_notebook.ipynb](python/trio_notebook.ipynb)

## Results

MP3 results are in the `samples` folder and available on Soundcloud below:

- [Breed - Nirvana](https://soundcloud.com/user-604304255/breed_magenta)
- [Logic - Everybody](https://soundcloud.com/user-604304255/everybody_magenta)
- [Bad Guy - Billie Eilish](https://soundcloud.com/user-604304255/badguy_magenta)
- [Childish Gambino - Bonfire](https://soundcloud.com/user-604304255/bonfire_magenta)

## Technical Notes

- Run with Jupyter on macOS.
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
