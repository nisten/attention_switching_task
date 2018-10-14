#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b10),
    on October 10, 2018, at 22:36
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test_switching_task_v5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\danie\\Dropbox\\Kris\\Projects\\nisten_dynamic_selective_inspect\\test_switching_task_v5.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1463, 823], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruc_location"
instruc_locationClock = core.Clock()
instruct1 = visual.TextStim(win=win, name='instruct1',
    text='In this test, you will see a BLUE arrow on your screen. Pay attention to the LOCATION of the arrow.\nIt will be on the left or right side of the screen.\n\nPress the "N" key if the BLUE arrow is on the left side\n\nPress the "M" key if the BLUE arrow is on the right side\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "location_practice_2"
location_practice_2Clock = core.Clock()
location_practice_text = visual.TextStim(win=win, name='location_practice_text',
    text='You will do some practice trials before the real test. \n\nRemember, press the "N" key if the BLUE arrow is on the left side.\n\nPress the "M" key if the BLUE arrow is on the right side.\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready_practice"
ready_practiceClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='The practice test will start in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
number_correct = 0;


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "location_practice_trial"
location_practice_trialClock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation2_2 = visual.TextStim(win=win, name='fixation2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.333, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "feedback_location"
feedback_locationClock = core.Clock()
msg=' '
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MorePractice"
MorePracticeClock = core.Clock()

repeat_instructions_location = visual.TextStim(win=win, name='repeat_instructions_location',
    text='Let\'s practice some more.\n\nRemember, when you see a BLUE arrow:\n \npress "N" if the arrow is on the Left side of the screen\n\npress "M" if the arrow is on the Right side of the screen\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "do_your_best"
do_your_bestClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Now you will start the real test.\n\nTry to answer as fast as you can without making mistakes.\n\nIt is ok if you make some mistakes or lose track, just do your best.\n\nPress space key to start the test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "location_trials"
location_trialsClock = core.Clock()
arrow_3 = visual.ImageStim(
    win=win, name='arrow_3',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_3 = visual.TextStim(win=win, name='fixation_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instructions_dir1"
instructions_dir1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Now, you will do a different task. You will see an ORANGE arrow on the screen. Pay attention to which way the arrow is pointing. \nIt will point to the left or the right.\n\nPress the "N" key if the ORANGE arrow points to the left.\n\nPress the "M" key if the ORANGE arrow points to the right.\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready_practice"
ready_practiceClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='The practice test will start in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
number_correct = 0;


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "direction_practice_trial"
direction_practice_trialClock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation2_3 = visual.TextStim(win=win, name='fixation2_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "feedback_direction"
feedback_directionClock = core.Clock()
msg=' '
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MorePractice2"
MorePractice2Clock = core.Clock()

more_direction_practice = visual.TextStim(win=win, name='more_direction_practice',
    text='Let\'s do some more practice.\nRemember: when you see the ORANGE arrows,\n\npress "N" if the ORANGE arrow points to the left,\n\npress "M" is the ORANGE arrow points to the right.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "do_your_best"
do_your_bestClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Now you will start the real test.\n\nTry to answer as fast as you can without making mistakes.\n\nIt is ok if you make some mistakes or lose track, just do your best.\n\nPress space key to start the test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "direction_trial"
direction_trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_switch1"
instruct_switch1Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Now you will see either a BLUE or an ORANGE arrow.\n\nIf you see a BLUE arrow, press the left or right key \nbased on the LOCATION of the arrow.\n\nPress "N"  if the BLUE arrow is on the left.\nPress "M" if the BLUE arrow is on the right.\n\nIf you see an ORANGE arrow, press the left or right key\nbased on the direction it is pointing.\n\nPress "N" if the ORANGE arrow points left.\nPress "M" if the ORANGE arrow points right.\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_switch2"
instruct_switch2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Remember, if you see a BLUE arrow, answer based on the LOCATION of the arrow on the screen.\n\nIf you see an ORANGE arrow, answer based on the DIRECTION the arrow is pointing.\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_switch_practice"
instruct_switch_practiceClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='You will do a short practice trial before the real test. \n\n\nPress the space key to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready_practice"
ready_practiceClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='The practice test will start in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
number_correct = 0;


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "switch_trial"
switch_trialClock = core.Clock()
fixation3 = visual.TextStim(win=win, name='fixation3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "switch_feedback"
switch_feedbackClock = core.Clock()
msg=' ';

text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MorePractice3"
MorePractice3Clock = core.Clock()

text_16 = visual.TextStim(win=win, name='text_16',
    text='Let\'s do some more practice.\nRemember, pay attention to the COLOUR of the arrows.\n\nIf the arrow is BLUE, press "N" or "M" based on the LOCATION of the arrow\n\nIf the arrow is ORANGE, press "N" or "M" based on the DIRECTION of the arrow',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "do_your_best"
do_your_bestClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Now you will start the real test.\n\nTry to answer as fast as you can without making mistakes.\n\nIt is ok if you make some mistakes or lose track, just do your best.\n\nPress space key to start the test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "switch_trial"
switch_trialClock = core.Clock()
fixation3 = visual.TextStim(win=win, name='fixation3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "switch_ready2"
switch_ready2Clock = core.Clock()
switch_block2 = visual.TextStim(win=win, name='switch_block2',
    text="Now you will do the same task again. \nIf the arrow is BLUE, pay attention to the location of the arrow.\nIf the arrow is ORANGE, pay attention to the direction of the arrow.\n\nRespond as fast as you can.\nTry not to make mistakes. \n\nPress 'space' to start",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "switch_trial"
switch_trialClock = core.Clock()
fixation3 = visual.TextStim(win=win, name='fixation3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "direct2_ready"
direct2_readyClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Now you will see ORANGE arrows.\n\nJust like before, answer based on what DIRECTION the arrow is pointing.\nIf the ORANGE arrow points left, press the "N" key\nIf the arrow points right, press the "M" key\n\nPress \'space\' to start the test',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "direction_trial"
direction_trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "locate2_ready"
locate2_readyClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Now you will see BLUE arrows.\n\nAnswer based on the LOCATION of the arrows on the screen.\nIf the BLUE arrow is on the left side, press the "N" key.\nIf the arrow is on the right side, press the "M" key.\n\nPress \'space\' to start',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Ready?\n\nThe test starts in 5 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "location_trials"
location_trialsClock = core.Clock()
arrow_3 = visual.ImageStim(
    win=win, name='arrow_3',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=0.5,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_3 = visual.TextStim(win=win, name='fixation_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.33, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='The test is now finished.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruc_location"-------
t = 0
instruc_locationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
instruc_locationComponents = [instruct1, key_resp_3]
for thisComponent in instruc_locationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc_location"-------
while continueRoutine:
    # get current time
    t = instruc_locationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct1* updates
    if t >= 0.0 and instruct1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct1.tStart = t
        instruct1.frameNStart = frameN  # exact frame index
        instruct1.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.2 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc_locationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc_location"-------
for thisComponent in instruc_locationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instruc_location" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "location_practice_2"-------
t = 0
location_practice_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
location_practice_2Components = [location_practice_text, key_resp_11]
for thisComponent in location_practice_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "location_practice_2"-------
while continueRoutine:
    # get current time
    t = location_practice_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *location_practice_text* updates
    if t >= 0.0 and location_practice_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        location_practice_text.tStart = t
        location_practice_text.frameNStart = frameN  # exact frame index
        location_practice_text.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.2 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in location_practice_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "location_practice_2"-------
for thisComponent in location_practice_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "location_practice_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
endLocationPractice = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='endLocationPractice')
thisExp.addLoop(endLocationPractice)  # add the loop to the experiment
thisEndLocationPractice = endLocationPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEndLocationPractice.rgb)
if thisEndLocationPractice != None:
    for paramName in thisEndLocationPractice:
        exec('{} = thisEndLocationPractice[paramName]'.format(paramName))

for thisEndLocationPractice in endLocationPractice:
    currentLoop = endLocationPractice
    # abbreviate parameter names if possible (e.g. rgb = thisEndLocationPractice.rgb)
    if thisEndLocationPractice != None:
        for paramName in thisEndLocationPractice:
            exec('{} = thisEndLocationPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_practice"-------
    t = 0
    ready_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    ready_practiceComponents = [text_7]
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ready_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ready_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_practice"-------
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    repeat_location_practice = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('location_practice.xlsx'),
        seed=None, name='repeat_location_practice')
    thisExp.addLoop(repeat_location_practice)  # add the loop to the experiment
    thisRepeat_location_practice = repeat_location_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_location_practice.rgb)
    if thisRepeat_location_practice != None:
        for paramName in thisRepeat_location_practice:
            exec('{} = thisRepeat_location_practice[paramName]'.format(paramName))
    
    for thisRepeat_location_practice in repeat_location_practice:
        currentLoop = repeat_location_practice
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_location_practice.rgb)
        if thisRepeat_location_practice != None:
            for paramName in thisRepeat_location_practice:
                exec('{} = thisRepeat_location_practice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "location_practice_trial"-------
        t = 0
        location_practice_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        image_3.setPos((PositionX, PositionY))
        image_3.setImage(File)
        response_location3 = event.BuilderKeyResponse()
        if repeat_location_practice.thisN == 0:
            number_correct = 0
        
        # keep track of which components have finished
        location_practice_trialComponents = [image_3, fixation2_2, response_location3]
        for thisComponent in location_practice_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "location_practice_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = location_practice_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if t >= 0.25 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_3.status == STARTED and t >= frameRemains:
                image_3.setAutoDraw(False)
            
            # *fixation2_2* updates
            if t >= 0.0 and fixation2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation2_2.tStart = t
                fixation2_2.frameNStart = frameN  # exact frame index
                fixation2_2.setAutoDraw(True)
            frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation2_2.status == STARTED and t >= frameRemains:
                fixation2_2.setAutoDraw(False)
            
            # *response_location3* updates
            if t >= 0.1 and response_location3.status == NOT_STARTED:
                # keep track of start time/frame for later
                response_location3.tStart = t
                response_location3.frameNStart = frameN  # exact frame index
                response_location3.status = STARTED
                # keyboard checking is just starting
                response_location3.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response_location3.status == STARTED and t >= frameRemains:
                response_location3.status = STOPPED
            if response_location3.status == STARTED:
                theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response_location3.keys == []:  # then this was the first keypress
                        response_location3.keys = theseKeys[0]  # just the first key pressed
                        response_location3.rt = response_location3.clock.getTime()
                        # was this 'correct'?
                        if (response_location3.keys == str(CorrAns)) or (response_location3.keys == CorrAns):
                            response_location3.corr = 1
                        else:
                            response_location3.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in location_practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "location_practice_trial"-------
        for thisComponent in location_practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response_location3.keys in ['', [], None]:  # No response was made
            response_location3.keys=None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               response_location3.corr = 1;  # correct non-response
            else:
               response_location3.corr = 0;  # failed to respond (incorrectly)
        # store data for repeat_location_practice (TrialHandler)
        repeat_location_practice.addData('response_location3.keys',response_location3.keys)
        repeat_location_practice.addData('response_location3.corr', response_location3.corr)
        if response_location3.keys != None:  # we had a response
            repeat_location_practice.addData('response_location3.rt', response_location3.rt)
        if response_location3.corr:
            number_correct = number_correct + 1
        
        if (repeat_location_practice.thisN + 1) == repeat_location_practice.nTotal:   
            if number_correct/repeat_location_practice.nTotal >= 0.75:
                endLocationPractice.finished = True
        
        
        # ------Prepare to start Routine "feedback_location"-------
        t = 0
        feedback_locationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if response_location3.corr:
            msg="Correct, good job!\n" + 'repeat_location_practice.nTotal: %d\n, repeat_location_practice.thisN: %d, number_correct: %d' % (repeat_location_practice.nTotal, repeat_location_practice.thisN, number_correct)
        else:
            msg="Wrong, try again"
        text_8.setText(msg)
        # keep track of which components have finished
        feedback_locationComponents = [text_8]
        for thisComponent in feedback_locationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback_location"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_locationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_8* updates
            if t >= 0.0 and text_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_8.tStart = t
                text_8.frameNStart = frameN  # exact frame index
                text_8.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_8.status == STARTED and t >= frameRemains:
                text_8.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_locationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback_location"-------
        for thisComponent in feedback_locationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [text]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'repeat_location_practice'
    
    
    # ------Prepare to start Routine "MorePractice"-------
    t = 0
    MorePracticeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    if endLocationPractice.finished:
        continueRoutine = False
    #don't show this screen if the loop is finishing
    # keep track of which components have finished
    MorePracticeComponents = [repeat_instructions_location]
    for thisComponent in MorePracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "MorePractice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MorePracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *repeat_instructions_location* updates
        if t >= 0.0 and repeat_instructions_location.status == NOT_STARTED:
            # keep track of start time/frame for later
            repeat_instructions_location.tStart = t
            repeat_instructions_location.frameNStart = frameN  # exact frame index
            repeat_instructions_location.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if repeat_instructions_location.status == STARTED and t >= frameRemains:
            repeat_instructions_location.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MorePracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MorePractice"-------
    for thisComponent in MorePracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 999 repeats of 'endLocationPractice'


# ------Prepare to start Routine "do_your_best"-------
t = 0
do_your_bestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
do_your_bestComponents = [text_4, key_resp_9]
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "do_your_best"-------
while continueRoutine:
    # get current time
    t = do_your_bestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 2 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in do_your_bestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "do_your_best"-------
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "do_your_best" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.750000)
# update component parameters for each repeat
# keep track of which components have finished
ISIComponents = [text]
for thisComponent in ISIComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
locate1_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('location_conditions.xlsx'),
    seed=None, name='locate1_trial')
thisExp.addLoop(locate1_trial)  # add the loop to the experiment
thisLocate1_trial = locate1_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLocate1_trial.rgb)
if thisLocate1_trial != None:
    for paramName in thisLocate1_trial:
        exec('{} = thisLocate1_trial[paramName]'.format(paramName))

for thisLocate1_trial in locate1_trial:
    currentLoop = locate1_trial
    # abbreviate parameter names if possible (e.g. rgb = thisLocate1_trial.rgb)
    if thisLocate1_trial != None:
        for paramName in thisLocate1_trial:
            exec('{} = thisLocate1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "location_trials"-------
    t = 0
    location_trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    arrow_3.setPos((PositionX, PositionY))
    arrow_3.setImage(File)
    response_location_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    location_trialsComponents = [arrow_3, response_location_2, fixation_3]
    for thisComponent in location_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "location_trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = location_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *arrow_3* updates
        if t >= 0.25 and arrow_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            arrow_3.tStart = t
            arrow_3.frameNStart = frameN  # exact frame index
            arrow_3.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if arrow_3.status == STARTED and t >= frameRemains:
            arrow_3.setAutoDraw(False)
        
        # *response_location_2* updates
        if t >= 0.1 and response_location_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_location_2.tStart = t
            response_location_2.frameNStart = frameN  # exact frame index
            response_location_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_location_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_location_2.status == STARTED and t >= frameRemains:
            response_location_2.status = STOPPED
        if response_location_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_location_2.keys == []:  # then this was the first keypress
                    response_location_2.keys = theseKeys[0]  # just the first key pressed
                    response_location_2.rt = response_location_2.clock.getTime()
                    # was this 'correct'?
                    if (response_location_2.keys == str(CorrAns)) or (response_location_2.keys == CorrAns):
                        response_location_2.corr = 1
                    else:
                        response_location_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *fixation_3* updates
        if t >= 0.0 and fixation_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_3.tStart = t
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_3.status == STARTED and t >= frameRemains:
            fixation_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in location_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "location_trials"-------
    for thisComponent in location_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_location_2.keys in ['', [], None]:  # No response was made
        response_location_2.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_location_2.corr = 1;  # correct non-response
        else:
           response_location_2.corr = 0;  # failed to respond (incorrectly)
    # store data for locate1_trial (TrialHandler)
    locate1_trial.addData('response_location_2.keys',response_location_2.keys)
    locate1_trial.addData('response_location_2.corr', response_location_2.corr)
    if response_location_2.keys != None:  # we had a response
        locate1_trial.addData('response_location_2.rt', response_location_2.rt)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'locate1_trial'


# ------Prepare to start Routine "instructions_dir1"-------
t = 0
instructions_dir1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions_dir1Components = [text_2, key_resp_6]
for thisComponent in instructions_dir1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions_dir1"-------
while continueRoutine:
    # get current time
    t = instructions_dir1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 3 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_dir1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_dir1"-------
for thisComponent in instructions_dir1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instructions_dir1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
endDirectionPractice = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='endDirectionPractice')
thisExp.addLoop(endDirectionPractice)  # add the loop to the experiment
thisEndDirectionPractice = endDirectionPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEndDirectionPractice.rgb)
if thisEndDirectionPractice != None:
    for paramName in thisEndDirectionPractice:
        exec('{} = thisEndDirectionPractice[paramName]'.format(paramName))

for thisEndDirectionPractice in endDirectionPractice:
    currentLoop = endDirectionPractice
    # abbreviate parameter names if possible (e.g. rgb = thisEndDirectionPractice.rgb)
    if thisEndDirectionPractice != None:
        for paramName in thisEndDirectionPractice:
            exec('{} = thisEndDirectionPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_practice"-------
    t = 0
    ready_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    ready_practiceComponents = [text_7]
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ready_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ready_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_practice"-------
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    repeat_direction_practice = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('direction_practice.xlsx'),
        seed=None, name='repeat_direction_practice')
    thisExp.addLoop(repeat_direction_practice)  # add the loop to the experiment
    thisRepeat_direction_practice = repeat_direction_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_direction_practice.rgb)
    if thisRepeat_direction_practice != None:
        for paramName in thisRepeat_direction_practice:
            exec('{} = thisRepeat_direction_practice[paramName]'.format(paramName))
    
    for thisRepeat_direction_practice in repeat_direction_practice:
        currentLoop = repeat_direction_practice
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_direction_practice.rgb)
        if thisRepeat_direction_practice != None:
            for paramName in thisRepeat_direction_practice:
                exec('{} = thisRepeat_direction_practice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "direction_practice_trial"-------
        t = 0
        direction_practice_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        image_4.setPos((PositionX, PositionY))
        image_4.setImage(File)
        response_direction2 = event.BuilderKeyResponse()
        if repeat_direction_practice.thisN == 0: 
            number_correct = 0
        
        # keep track of which components have finished
        direction_practice_trialComponents = [image_4, fixation2_3, response_direction2]
        for thisComponent in direction_practice_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "direction_practice_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = direction_practice_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_4* updates
            if t >= 0.25 and image_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_4.tStart = t
                image_4.frameNStart = frameN  # exact frame index
                image_4.setAutoDraw(True)
            frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_4.status == STARTED and t >= frameRemains:
                image_4.setAutoDraw(False)
            
            # *fixation2_3* updates
            if t >= 0.0 and fixation2_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation2_3.tStart = t
                fixation2_3.frameNStart = frameN  # exact frame index
                fixation2_3.setAutoDraw(True)
            frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation2_3.status == STARTED and t >= frameRemains:
                fixation2_3.setAutoDraw(False)
            
            # *response_direction2* updates
            if t >= 0.1 and response_direction2.status == NOT_STARTED:
                # keep track of start time/frame for later
                response_direction2.tStart = t
                response_direction2.frameNStart = frameN  # exact frame index
                response_direction2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response_direction2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response_direction2.status == STARTED and t >= frameRemains:
                response_direction2.status = STOPPED
            if response_direction2.status == STARTED:
                theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response_direction2.keys == []:  # then this was the first keypress
                        response_direction2.keys = theseKeys[0]  # just the first key pressed
                        response_direction2.rt = response_direction2.clock.getTime()
                        # was this 'correct'?
                        if (response_direction2.keys == str(CorrAns)) or (response_direction2.keys == CorrAns):
                            response_direction2.corr = 1
                        else:
                            response_direction2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in direction_practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "direction_practice_trial"-------
        for thisComponent in direction_practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response_direction2.keys in ['', [], None]:  # No response was made
            response_direction2.keys=None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               response_direction2.corr = 1;  # correct non-response
            else:
               response_direction2.corr = 0;  # failed to respond (incorrectly)
        # store data for repeat_direction_practice (TrialHandler)
        repeat_direction_practice.addData('response_direction2.keys',response_direction2.keys)
        repeat_direction_practice.addData('response_direction2.corr', response_direction2.corr)
        if response_direction2.keys != None:  # we had a response
            repeat_direction_practice.addData('response_direction2.rt', response_direction2.rt)
        if response_direction2.corr:
            number_correct = number_correct + 1
        
        if (repeat_direction_practice.thisN + 1) == repeat_direction_practice.nTotal:   
            if number_correct/repeat_direction_practice.nTotal >= 0.75:
                endDirectionPractice.finished = True
        
        
        # ------Prepare to start Routine "feedback_direction"-------
        t = 0
        feedback_directionClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if response_direction2.corr:
            msg="Correct, good job!"
        else:
            msg="Wrong, try again"
        text_10.setText(msg)
        # keep track of which components have finished
        feedback_directionComponents = [text_10]
        for thisComponent in feedback_directionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback_direction"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_directionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_10* updates
            if t >= 0.0 and text_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_10.tStart = t
                text_10.frameNStart = frameN  # exact frame index
                text_10.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_10.status == STARTED and t >= frameRemains:
                text_10.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_directionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback_direction"-------
        for thisComponent in feedback_directionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [text]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'repeat_direction_practice'
    
    
    # ------Prepare to start Routine "MorePractice2"-------
    t = 0
    MorePractice2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    if endDirectionPractice.finished:
        continueRoutine = False
    
    # keep track of which components have finished
    MorePractice2Components = [more_direction_practice]
    for thisComponent in MorePractice2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "MorePractice2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MorePractice2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *more_direction_practice* updates
        if t >= 0.0 and more_direction_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            more_direction_practice.tStart = t
            more_direction_practice.frameNStart = frameN  # exact frame index
            more_direction_practice.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if more_direction_practice.status == STARTED and t >= frameRemains:
            more_direction_practice.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MorePractice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MorePractice2"-------
    for thisComponent in MorePractice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 999 repeats of 'endDirectionPractice'


# ------Prepare to start Routine "do_your_best"-------
t = 0
do_your_bestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
do_your_bestComponents = [text_4, key_resp_9]
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "do_your_best"-------
while continueRoutine:
    # get current time
    t = do_your_bestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 2 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in do_your_bestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "do_your_best"-------
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "do_your_best" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.750000)
# update component parameters for each repeat
# keep track of which components have finished
ISIComponents = [text]
for thisComponent in ISIComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
direct1_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('direction_conditions.xlsx'),
    seed=None, name='direct1_trial')
thisExp.addLoop(direct1_trial)  # add the loop to the experiment
thisDirect1_trial = direct1_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDirect1_trial.rgb)
if thisDirect1_trial != None:
    for paramName in thisDirect1_trial:
        exec('{} = thisDirect1_trial[paramName]'.format(paramName))

for thisDirect1_trial in direct1_trial:
    currentLoop = direct1_trial
    # abbreviate parameter names if possible (e.g. rgb = thisDirect1_trial.rgb)
    if thisDirect1_trial != None:
        for paramName in thisDirect1_trial:
            exec('{} = thisDirect1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "direction_trial"-------
    t = 0
    direction_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    image.setPos((PositionX, PositionY))
    image.setImage(File)
    response_direction = event.BuilderKeyResponse()
    # keep track of which components have finished
    direction_trialComponents = [image, fixation2, response_direction]
    for thisComponent in direction_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "direction_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = direction_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.25 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *fixation2* updates
        if t >= 0.0 and fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation2.tStart = t
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation2.status == STARTED and t >= frameRemains:
            fixation2.setAutoDraw(False)
        
        # *response_direction* updates
        if t >= 0.1 and response_direction.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_direction.tStart = t
            response_direction.frameNStart = frameN  # exact frame index
            response_direction.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_direction.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_direction.status == STARTED and t >= frameRemains:
            response_direction.status = STOPPED
        if response_direction.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_direction.keys == []:  # then this was the first keypress
                    response_direction.keys = theseKeys[0]  # just the first key pressed
                    response_direction.rt = response_direction.clock.getTime()
                    # was this 'correct'?
                    if (response_direction.keys == str(CorrAns)) or (response_direction.keys == CorrAns):
                        response_direction.corr = 1
                    else:
                        response_direction.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in direction_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "direction_trial"-------
    for thisComponent in direction_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_direction.keys in ['', [], None]:  # No response was made
        response_direction.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_direction.corr = 1;  # correct non-response
        else:
           response_direction.corr = 0;  # failed to respond (incorrectly)
    # store data for direct1_trial (TrialHandler)
    direct1_trial.addData('response_direction.keys',response_direction.keys)
    direct1_trial.addData('response_direction.corr', response_direction.corr)
    if response_direction.keys != None:  # we had a response
        direct1_trial.addData('response_direction.rt', response_direction.rt)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'direct1_trial'


# ------Prepare to start Routine "instruct_switch1"-------
t = 0
instruct_switch1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
instruct_switch1Components = [text_3, key_resp_7]
for thisComponent in instruct_switch1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct_switch1"-------
while continueRoutine:
    # get current time
    t = instruct_switch1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 3 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_switch1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_switch1"-------
for thisComponent in instruct_switch1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "instruct_switch1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_switch2"-------
t = 0
instruct_switch2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
instruct_switch2Components = [text_5, key_resp_8]
for thisComponent in instruct_switch2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct_switch2"-------
while continueRoutine:
    # get current time
    t = instruct_switch2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 3 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_switch2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_switch2"-------
for thisComponent in instruct_switch2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "instruct_switch2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_switch_practice"-------
t = 0
instruct_switch_practiceClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
instruct_switch_practiceComponents = [text_11, key_resp_5]
for thisComponent in instruct_switch_practiceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct_switch_practice"-------
while continueRoutine:
    # get current time
    t = instruct_switch_practiceClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 2.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_switch_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_switch_practice"-------
for thisComponent in instruct_switch_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instruct_switch_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
endSwitchPractice = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='endSwitchPractice')
thisExp.addLoop(endSwitchPractice)  # add the loop to the experiment
thisEndSwitchPractice = endSwitchPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEndSwitchPractice.rgb)
if thisEndSwitchPractice != None:
    for paramName in thisEndSwitchPractice:
        exec('{} = thisEndSwitchPractice[paramName]'.format(paramName))

for thisEndSwitchPractice in endSwitchPractice:
    currentLoop = endSwitchPractice
    # abbreviate parameter names if possible (e.g. rgb = thisEndSwitchPractice.rgb)
    if thisEndSwitchPractice != None:
        for paramName in thisEndSwitchPractice:
            exec('{} = thisEndSwitchPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_practice"-------
    t = 0
    ready_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    ready_practiceComponents = [text_7]
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ready_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ready_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_practice"-------
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    repeat_switch_practice = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('switch_condition1.xlsx'),
        seed=None, name='repeat_switch_practice')
    thisExp.addLoop(repeat_switch_practice)  # add the loop to the experiment
    thisRepeat_switch_practice = repeat_switch_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_switch_practice.rgb)
    if thisRepeat_switch_practice != None:
        for paramName in thisRepeat_switch_practice:
            exec('{} = thisRepeat_switch_practice[paramName]'.format(paramName))
    
    for thisRepeat_switch_practice in repeat_switch_practice:
        currentLoop = repeat_switch_practice
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat_switch_practice.rgb)
        if thisRepeat_switch_practice != None:
            for paramName in thisRepeat_switch_practice:
                exec('{} = thisRepeat_switch_practice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "switch_trial"-------
        t = 0
        switch_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        image_2.setPos((PositionX, PositionY))
        image_2.setImage(File)
        response_switch = event.BuilderKeyResponse()
        if repeat_switch_practice.thisN == 0:
            number_correct = 0
        
        # keep track of which components have finished
        switch_trialComponents = [fixation3, image_2, response_switch]
        for thisComponent in switch_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "switch_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = switch_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation3* updates
            if t >= 0.0 and fixation3.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation3.tStart = t
                fixation3.frameNStart = frameN  # exact frame index
                fixation3.setAutoDraw(True)
            frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation3.status == STARTED and t >= frameRemains:
                fixation3.setAutoDraw(False)
            
            # *image_2* updates
            if t >= 0.25 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # *response_switch* updates
            if t >= 0.1 and response_switch.status == NOT_STARTED:
                # keep track of start time/frame for later
                response_switch.tStart = t
                response_switch.frameNStart = frameN  # exact frame index
                response_switch.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response_switch.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response_switch.status == STARTED and t >= frameRemains:
                response_switch.status = STOPPED
            if response_switch.status == STARTED:
                theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response_switch.keys == []:  # then this was the first keypress
                        response_switch.keys = theseKeys[0]  # just the first key pressed
                        response_switch.rt = response_switch.clock.getTime()
                        # was this 'correct'?
                        if (response_switch.keys == str(CorrAns)) or (response_switch.keys == CorrAns):
                            response_switch.corr = 1
                        else:
                            response_switch.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in switch_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "switch_trial"-------
        for thisComponent in switch_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response_switch.keys in ['', [], None]:  # No response was made
            response_switch.keys=None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               response_switch.corr = 1;  # correct non-response
            else:
               response_switch.corr = 0;  # failed to respond (incorrectly)
        # store data for repeat_switch_practice (TrialHandler)
        repeat_switch_practice.addData('response_switch.keys',response_switch.keys)
        repeat_switch_practice.addData('response_switch.corr', response_switch.corr)
        if response_switch.keys != None:  # we had a response
            repeat_switch_practice.addData('response_switch.rt', response_switch.rt)
        if response_switch.corr:
            number_correct = number_correct + 1
        
        if (repeat_switch_practice.thisN + 1) == repeat_switch_practice.nTotal:   
            if number_correct/repeat_switch_practice.nTotal >= 0.75:
                endSwitchPractice.finished = True
        
        
        # ------Prepare to start Routine "switch_feedback"-------
        t = 0
        switch_feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if response_switch.corr:
            msg="Correct, good job!"
        else:
            msg="Wrong, try again"
        text_12.setText(msg)
        # keep track of which components have finished
        switch_feedbackComponents = [text_12]
        for thisComponent in switch_feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "switch_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = switch_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_12* updates
            if t >= 0.0 and text_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_12.tStart = t
                text_12.frameNStart = frameN  # exact frame index
                text_12.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_12.status == STARTED and t >= frameRemains:
                text_12.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in switch_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "switch_feedback"-------
        for thisComponent in switch_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [text]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'repeat_switch_practice'
    
    
    # ------Prepare to start Routine "MorePractice3"-------
    t = 0
    MorePractice3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    if endSwitchPractice.finished:
        continueRoutine = False
    
    # keep track of which components have finished
    MorePractice3Components = [text_16]
    for thisComponent in MorePractice3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "MorePractice3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MorePractice3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_16.status == STARTED and t >= frameRemains:
            text_16.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MorePractice3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MorePractice3"-------
    for thisComponent in MorePractice3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 999 repeats of 'endSwitchPractice'


# ------Prepare to start Routine "do_your_best"-------
t = 0
do_your_bestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
do_your_bestComponents = [text_4, key_resp_9]
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "do_your_best"-------
while continueRoutine:
    # get current time
    t = do_your_bestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 2 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in do_your_bestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "do_your_best"-------
for thisComponent in do_your_bestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "do_your_best" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.750000)
# update component parameters for each repeat
# keep track of which components have finished
ISIComponents = [text]
for thisComponent in ISIComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
switch1_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('switch_condition1.xlsx'),
    seed=None, name='switch1_trial')
thisExp.addLoop(switch1_trial)  # add the loop to the experiment
thisSwitch1_trial = switch1_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSwitch1_trial.rgb)
if thisSwitch1_trial != None:
    for paramName in thisSwitch1_trial:
        exec('{} = thisSwitch1_trial[paramName]'.format(paramName))

for thisSwitch1_trial in switch1_trial:
    currentLoop = switch1_trial
    # abbreviate parameter names if possible (e.g. rgb = thisSwitch1_trial.rgb)
    if thisSwitch1_trial != None:
        for paramName in thisSwitch1_trial:
            exec('{} = thisSwitch1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "switch_trial"-------
    t = 0
    switch_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    image_2.setPos((PositionX, PositionY))
    image_2.setImage(File)
    response_switch = event.BuilderKeyResponse()
    if repeat_switch_practice.thisN == 0:
        number_correct = 0
    
    # keep track of which components have finished
    switch_trialComponents = [fixation3, image_2, response_switch]
    for thisComponent in switch_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "switch_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = switch_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation3* updates
        if t >= 0.0 and fixation3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation3.tStart = t
            fixation3.frameNStart = frameN  # exact frame index
            fixation3.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation3.status == STARTED and t >= frameRemains:
            fixation3.setAutoDraw(False)
        
        # *image_2* updates
        if t >= 0.25 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *response_switch* updates
        if t >= 0.1 and response_switch.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_switch.tStart = t
            response_switch.frameNStart = frameN  # exact frame index
            response_switch.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_switch.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_switch.status == STARTED and t >= frameRemains:
            response_switch.status = STOPPED
        if response_switch.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_switch.keys == []:  # then this was the first keypress
                    response_switch.keys = theseKeys[0]  # just the first key pressed
                    response_switch.rt = response_switch.clock.getTime()
                    # was this 'correct'?
                    if (response_switch.keys == str(CorrAns)) or (response_switch.keys == CorrAns):
                        response_switch.corr = 1
                    else:
                        response_switch.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in switch_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "switch_trial"-------
    for thisComponent in switch_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_switch.keys in ['', [], None]:  # No response was made
        response_switch.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_switch.corr = 1;  # correct non-response
        else:
           response_switch.corr = 0;  # failed to respond (incorrectly)
    # store data for switch1_trial (TrialHandler)
    switch1_trial.addData('response_switch.keys',response_switch.keys)
    switch1_trial.addData('response_switch.corr', response_switch.corr)
    if response_switch.keys != None:  # we had a response
        switch1_trial.addData('response_switch.rt', response_switch.rt)
    if response_switch.corr:
        number_correct = number_correct + 1
    
    if (repeat_switch_practice.thisN + 1) == repeat_switch_practice.nTotal:   
        if number_correct/repeat_switch_practice.nTotal >= 0.75:
            endSwitchPractice.finished = True
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'switch1_trial'


# ------Prepare to start Routine "switch_ready2"-------
t = 0
switch_ready2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
switch_ready2Components = [switch_block2, key_resp_10]
for thisComponent in switch_ready2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "switch_ready2"-------
while continueRoutine:
    # get current time
    t = switch_ready2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *switch_block2* updates
    if t >= 0.0 and switch_block2.status == NOT_STARTED:
        # keep track of start time/frame for later
        switch_block2.tStart = t
        switch_block2.frameNStart = frameN  # exact frame index
        switch_block2.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 2 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in switch_ready2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "switch_ready2"-------
for thisComponent in switch_ready2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "switch_ready2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
switch2_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('switch_condition2.xlsx'),
    seed=None, name='switch2_trial')
thisExp.addLoop(switch2_trial)  # add the loop to the experiment
thisSwitch2_trial = switch2_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSwitch2_trial.rgb)
if thisSwitch2_trial != None:
    for paramName in thisSwitch2_trial:
        exec('{} = thisSwitch2_trial[paramName]'.format(paramName))

for thisSwitch2_trial in switch2_trial:
    currentLoop = switch2_trial
    # abbreviate parameter names if possible (e.g. rgb = thisSwitch2_trial.rgb)
    if thisSwitch2_trial != None:
        for paramName in thisSwitch2_trial:
            exec('{} = thisSwitch2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "switch_trial"-------
    t = 0
    switch_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    image_2.setPos((PositionX, PositionY))
    image_2.setImage(File)
    response_switch = event.BuilderKeyResponse()
    if repeat_switch_practice.thisN == 0:
        number_correct = 0
    
    # keep track of which components have finished
    switch_trialComponents = [fixation3, image_2, response_switch]
    for thisComponent in switch_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "switch_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = switch_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation3* updates
        if t >= 0.0 and fixation3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation3.tStart = t
            fixation3.frameNStart = frameN  # exact frame index
            fixation3.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation3.status == STARTED and t >= frameRemains:
            fixation3.setAutoDraw(False)
        
        # *image_2* updates
        if t >= 0.25 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *response_switch* updates
        if t >= 0.1 and response_switch.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_switch.tStart = t
            response_switch.frameNStart = frameN  # exact frame index
            response_switch.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_switch.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_switch.status == STARTED and t >= frameRemains:
            response_switch.status = STOPPED
        if response_switch.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_switch.keys == []:  # then this was the first keypress
                    response_switch.keys = theseKeys[0]  # just the first key pressed
                    response_switch.rt = response_switch.clock.getTime()
                    # was this 'correct'?
                    if (response_switch.keys == str(CorrAns)) or (response_switch.keys == CorrAns):
                        response_switch.corr = 1
                    else:
                        response_switch.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in switch_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "switch_trial"-------
    for thisComponent in switch_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_switch.keys in ['', [], None]:  # No response was made
        response_switch.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_switch.corr = 1;  # correct non-response
        else:
           response_switch.corr = 0;  # failed to respond (incorrectly)
    # store data for switch2_trial (TrialHandler)
    switch2_trial.addData('response_switch.keys',response_switch.keys)
    switch2_trial.addData('response_switch.corr', response_switch.corr)
    if response_switch.keys != None:  # we had a response
        switch2_trial.addData('response_switch.rt', response_switch.rt)
    if response_switch.corr:
        number_correct = number_correct + 1
    
    if (repeat_switch_practice.thisN + 1) == repeat_switch_practice.nTotal:   
        if number_correct/repeat_switch_practice.nTotal >= 0.75:
            endSwitchPractice.finished = True
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'switch2_trial'


# ------Prepare to start Routine "direct2_ready"-------
t = 0
direct2_readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
direct2_readyComponents = [text_14, key_resp_12]
for thisComponent in direct2_readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "direct2_ready"-------
while continueRoutine:
    # get current time
    t = direct2_readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 1 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in direct2_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "direct2_ready"-------
for thisComponent in direct2_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys=None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "direct2_ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
direct2_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('direction_conditions2.xlsx'),
    seed=None, name='direct2_trial')
thisExp.addLoop(direct2_trial)  # add the loop to the experiment
thisDirect2_trial = direct2_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDirect2_trial.rgb)
if thisDirect2_trial != None:
    for paramName in thisDirect2_trial:
        exec('{} = thisDirect2_trial[paramName]'.format(paramName))

for thisDirect2_trial in direct2_trial:
    currentLoop = direct2_trial
    # abbreviate parameter names if possible (e.g. rgb = thisDirect2_trial.rgb)
    if thisDirect2_trial != None:
        for paramName in thisDirect2_trial:
            exec('{} = thisDirect2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "direction_trial"-------
    t = 0
    direction_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    image.setPos((PositionX, PositionY))
    image.setImage(File)
    response_direction = event.BuilderKeyResponse()
    # keep track of which components have finished
    direction_trialComponents = [image, fixation2, response_direction]
    for thisComponent in direction_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "direction_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = direction_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.25 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *fixation2* updates
        if t >= 0.0 and fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation2.tStart = t
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation2.status == STARTED and t >= frameRemains:
            fixation2.setAutoDraw(False)
        
        # *response_direction* updates
        if t >= 0.1 and response_direction.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_direction.tStart = t
            response_direction.frameNStart = frameN  # exact frame index
            response_direction.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_direction.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_direction.status == STARTED and t >= frameRemains:
            response_direction.status = STOPPED
        if response_direction.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_direction.keys == []:  # then this was the first keypress
                    response_direction.keys = theseKeys[0]  # just the first key pressed
                    response_direction.rt = response_direction.clock.getTime()
                    # was this 'correct'?
                    if (response_direction.keys == str(CorrAns)) or (response_direction.keys == CorrAns):
                        response_direction.corr = 1
                    else:
                        response_direction.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in direction_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "direction_trial"-------
    for thisComponent in direction_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_direction.keys in ['', [], None]:  # No response was made
        response_direction.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_direction.corr = 1;  # correct non-response
        else:
           response_direction.corr = 0;  # failed to respond (incorrectly)
    # store data for direct2_trial (TrialHandler)
    direct2_trial.addData('response_direction.keys',response_direction.keys)
    direct2_trial.addData('response_direction.corr', response_direction.corr)
    if response_direction.keys != None:  # we had a response
        direct2_trial.addData('response_direction.rt', response_direction.rt)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'direct2_trial'


# ------Prepare to start Routine "locate2_ready"-------
t = 0
locate2_readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
locate2_readyComponents = [text_15, key_resp_13]
for thisComponent in locate2_readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "locate2_ready"-------
while continueRoutine:
    # get current time
    t = locate2_readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if t >= 0.0 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 1 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in locate2_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "locate2_ready"-------
for thisComponent in locate2_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "locate2_ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
readyComponents = [text_6]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
locate2_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('location_conditions2.xlsx'),
    seed=None, name='locate2_trial')
thisExp.addLoop(locate2_trial)  # add the loop to the experiment
thisLocate2_trial = locate2_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLocate2_trial.rgb)
if thisLocate2_trial != None:
    for paramName in thisLocate2_trial:
        exec('{} = thisLocate2_trial[paramName]'.format(paramName))

for thisLocate2_trial in locate2_trial:
    currentLoop = locate2_trial
    # abbreviate parameter names if possible (e.g. rgb = thisLocate2_trial.rgb)
    if thisLocate2_trial != None:
        for paramName in thisLocate2_trial:
            exec('{} = thisLocate2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "location_trials"-------
    t = 0
    location_trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    arrow_3.setPos((PositionX, PositionY))
    arrow_3.setImage(File)
    response_location_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    location_trialsComponents = [arrow_3, response_location_2, fixation_3]
    for thisComponent in location_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "location_trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = location_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *arrow_3* updates
        if t >= 0.25 and arrow_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            arrow_3.tStart = t
            arrow_3.frameNStart = frameN  # exact frame index
            arrow_3.setAutoDraw(True)
        frameRemains = 0.25 + 7.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if arrow_3.status == STARTED and t >= frameRemains:
            arrow_3.setAutoDraw(False)
        
        # *response_location_2* updates
        if t >= 0.1 and response_location_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_location_2.tStart = t
            response_location_2.frameNStart = frameN  # exact frame index
            response_location_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_location_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 7.9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_location_2.status == STARTED and t >= frameRemains:
            response_location_2.status = STOPPED
        if response_location_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['n', 'm', 'None'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response_location_2.keys == []:  # then this was the first keypress
                    response_location_2.keys = theseKeys[0]  # just the first key pressed
                    response_location_2.rt = response_location_2.clock.getTime()
                    # was this 'correct'?
                    if (response_location_2.keys == str(CorrAns)) or (response_location_2.keys == CorrAns):
                        response_location_2.corr = 1
                    else:
                        response_location_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *fixation_3* updates
        if t >= 0.0 and fixation_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_3.tStart = t
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.setAutoDraw(True)
        frameRemains = 0.0 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_3.status == STARTED and t >= frameRemains:
            fixation_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in location_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "location_trials"-------
    for thisComponent in location_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_location_2.keys in ['', [], None]:  # No response was made
        response_location_2.keys=None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response_location_2.corr = 1;  # correct non-response
        else:
           response_location_2.corr = 0;  # failed to respond (incorrectly)
    # store data for locate2_trial (TrialHandler)
    locate2_trial.addData('response_location_2.keys',response_location_2.keys)
    locate2_trial.addData('response_location_2.corr', response_location_2.corr)
    if response_location_2.keys != None:  # we had a response
        locate2_trial.addData('response_location_2.rt', response_location_2.rt)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'locate2_trial'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_13]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_13.status == STARTED and t >= frameRemains:
        text_13.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)














# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
