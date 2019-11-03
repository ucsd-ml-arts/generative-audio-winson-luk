import glob

print('Importing libraries and defining some helper functions...')
import magenta.music as mm
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
import numpy as np
import os
import tensorflow as tf

# Necessary until pyfluidsynth is updated (>1.2.5).
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def play(note_sequence):
  mm.play_sequence(note_sequence, synth=mm.fluidsynth)

def interpolate(model, start_seq, end_seq, num_steps, max_length=32,
                assert_same_length=True, temperature=0.5,
                individual_duration=4.0):
  """Interpolates between a start and end sequence."""
  note_sequences = model.interpolate(
      start_seq, end_seq,num_steps=num_steps, length=max_length,
      temperature=temperature,
      assert_same_length=assert_same_length)

  print('Start Seq Reconstruction')
  play(note_sequences[0])
  print('End Seq Reconstruction')
  play(note_sequences[-1])
  print('Mean Sequence')
  play(note_sequences[num_steps // 2])
  print('Start -> End Interpolation')
  interp_seq = mm.sequences_lib.concatenate_sequences(
      note_sequences, [individual_duration] * len(note_sequences))
  play(interp_seq)
  mm.plot_sequence(interp_seq)
  return interp_seq if num_steps > 3 else note_sequences[num_steps // 2]

def download(note_sequence, filename):
  mm.sequence_proto_to_midi_file(note_sequence, filename)

print('Done')

trio_models = {}
hierdec_trio_16bar_config = configs.CONFIG_MAP['hierdec-trio_16bar']
trio_models['hierdec_trio_16bar'] = TrainedModel(hierdec_trio_16bar_config, batch_size=4, checkpoint_dir_or_path='content/hierdec-trio_16bar.ckpt')

trio_sample_model = "hierdec_trio_16bar"
temperature = 0.6

trio_16_samples = trio_models[trio_sample_model].sample(n=16, length=256, temperature=temperature)
for ns in trio_16_samples:
  play(ns)

for i, ns in enumerate(trio_16_samples):
  download(ns, '%s_sample_%d.mid' % (trio_sample_model, i))
