import sys, os, pygame, pygame.midi
pygame.init()
pygame.midi.init()

i = pygame.midi.Input(5)

While True:
  if i.poll():
    signal = i.read(10)[0][0]
    if signal[0] == 144 and signal[1] == 36
      print('13')
    elif
del i
pygame.midi.quit()
