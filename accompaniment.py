from midiutil import MIDIFile

note_to_midi = {
    "C": 0,
    "C#": 1, "Db": 1,
    "D": 2,
    "D#": 3, "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6, "Gb": 6,
    "G": 7,
    "G#": 8, "Ab": 8,
    "A": 9,
    "A#": 10, "Bb": 10,
    "B": 11
}

# convert note name (ex: "C4") to corresponding MIDI value (ex: 60) 
def note_to_midi_value(note_name):

    note = note_name[:-1]  # Remove the octave number
    octave = int(note_name[-1]) + 1

    return note_to_midi[note] + 12 * octave

# test
# print(note_to_midi_value("C4"))  # 60
# print(note_to_midi_value("A#3")) # 58

# create a MIDIFile object with 1 track
mf = MIDIFile(2)
track_drum = 0
channel_drum = 9 # required to use percussion
track_piano = 1
channel_piano = 0

# tempo track
tempo = 120  # BPM
mf.addTempo(track_drum, 0, tempo)

# define drum notes
SNARE = 38
BASS_DRUM = 36
HI_HAT_CLOSED = 42
SIDE_STICK = 37
LOW_TOM = 45
MID_TOM1 = 47
MID_TOM2 = 48
HIGH_TOM = 50
HI_HAT_OPEN = 46
RIDE_CYMBAL = 51
CRASH_CYMBAL = 49

# MIDIFile.addNote(track, channel, pitch,  time, duration, volume[0-127], annotation=None)

# HH_OPEN is stopped on CLOSED. "choke group"?

drum_volume = 50

# count-in beats
mf.addNote(track_drum, channel_drum, SIDE_STICK, 0, 2, drum_volume)
mf.addNote(track_drum, channel_drum, SIDE_STICK, 1, 2, drum_volume)
mf.addNote(track_drum, channel_drum, SIDE_STICK, 2, 2, drum_volume)
mf.addNote(track_drum, channel_drum, SIDE_STICK, 3, 2, drum_volume)

for i in range(1, 33):
    m = 4*i
    mf.addNote(track_drum, channel_drum, HI_HAT_OPEN, m + 0, 2, drum_volume)
    mf.addNote(track_drum, channel_drum, HI_HAT_CLOSED, m + 1, 1, drum_volume)
    mf.addNote(track_drum, channel_drum, HI_HAT_CLOSED, m + 1.66, 1, drum_volume)
    mf.addNote(track_drum, channel_drum, HI_HAT_OPEN, m + 2, 2, drum_volume)
    mf.addNote(track_drum, channel_drum, HI_HAT_CLOSED, m + 3, 1, drum_volume)
    mf.addNote(track_drum, channel_drum, HI_HAT_CLOSED, m + 3.66, 1, drum_volume)

# octave change at C[N]

# instrument constants
PIANO = 0
VIOLIN = 40
STRINGS = 48
TRUMPET = 56
FLUTE = 73

mf.addProgramChange(1, 0, 0, PIANO)

chord_volume = 60

Cmaj7 = ["C3", "E3", "G3", "B3"]
Amin7 = ["A2", "C3", "E3", "G3"]
Dmin7 = ["D3", "F3", "A3", "C4"]
G7    = ["G2", "B2", "D3", "F3"]
E7    = ["E3", "G#3", "B3", "D4"]
A7    = ["A2", "C#3", "E3", "G3"]
D7    = ["D3", "F#3", "A3", "C4"]
C     = ["C3", "E3", "G3", "C2", "C4"]

def addChord( chord_note_list, start_time, duration, volume=100):
    for chord_note in chord_note_list: 
        midi_value = note_to_midi_value(chord_note)
        mf.addNote(track_piano, channel_piano, midi_value, start_time, duration, volume)

# standard jazz chord progression 1-6-5-2

for i in [0, 1, 3]:
    addChord( Cmaj7, 32*i + 4, 0.25, chord_volume)
    addChord( Cmaj7, 32*i + 5.66, 2, chord_volume)

    addChord( Cmaj7, 32*i + 8, 0.25, chord_volume)
    addChord( Cmaj7, 32*i + 9.66, 2, chord_volume)

    addChord( Amin7, 32*i + 12, 0.25, chord_volume)
    addChord( Amin7, 32*i + 13.66, 2, chord_volume)

    addChord( Amin7, 32*i + 16, 0.25, chord_volume)
    addChord( Amin7, 32*i + 17.66, 2, chord_volume)

    addChord( Dmin7, 32*i + 20, 0.25, chord_volume)
    addChord( Dmin7, 32*i + 21.66, 2, chord_volume)

    addChord( Dmin7, 32*i + 24, 0.25, chord_volume)
    addChord( Dmin7, 32*i + 25.66, 2, chord_volume)

    addChord( G7, 32*i + 28, 0.25, chord_volume)
    addChord( G7, 32*i + 29.66, 2, chord_volume)

    addChord( G7, 32*i + 32, 0.25, chord_volume)
    addChord( G7, 32*i + 33.66, 2, chord_volume)

for i in [2]:
    addChord( E7, 32*i + 4, 0.25, chord_volume)
    addChord( E7, 32*i + 5.66, 2, chord_volume)

    addChord( E7, 32*i + 8, 0.25, chord_volume)
    addChord( E7, 32*i + 9.66, 2, chord_volume)

    addChord( A7, 32*i + 12, 0.25, chord_volume)
    addChord( A7, 32*i + 13.66, 2, chord_volume)

    addChord( A7, 32*i + 16, 0.25, chord_volume)
    addChord( A7, 32*i + 17.66, 2, chord_volume)

    addChord( D7, 32*i + 20, 0.25, chord_volume)
    addChord( D7, 32*i + 21.66, 2, chord_volume)

    addChord( D7, 32*i + 24, 0.25, chord_volume)
    addChord( D7, 32*i + 25.66, 2, chord_volume)

    addChord( G7, 32*i + 28, 0.25, chord_volume)
    addChord( G7, 32*i + 29.66, 2, chord_volume)

    addChord( G7, 32*i + 32, 0.25, chord_volume)
    addChord( G7, 32*i + 33.66, 2, chord_volume)

# ending
addChord(C, 132, 4, chord_volume)
mf.addNote(track_drum, channel_drum, HI_HAT_OPEN, m + 132, 4, drum_volume)

# Write the MIDI file to disk
with open("accompaniment.midi", 'wb') as output_file:
    mf.writeFile(output_file)

# play music
import pygame
pygame.init()
pygame.mixer.music.load("accompaniment.midi")
pygame.mixer.music.play()
# keep program running while music plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)