#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b10),
    on Mon Nov 12 12:30:35 2018
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
    originPath='/Users/jag/work/nisten/attention_switching_demo/test_switching_task_v5_lastrun.py',
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
    monitor='testMonitor', color='#E8F7F7', colorSpace='hex',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruct_switch1"
instruct_switch1Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='In this test, you will see either a BLUE or an ORANGE arrow. \n\nIf you see a BLUE arrow, press the left or right key \nbased on the LOCATION of the arrow.\n\nPress "N"  if the BLUE arrow is on the left.\nPress "M" if the BLUE arrow is on the right.\n\nIf you see an ORANGE arrow, press the left or right key\nbased on the direction it is pointing.\n\nPress "N" if the ORANGE arrow points left.\nPress "M" if the ORANGE arrow points right.\n\nPress the space key to continue.',
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
number_correct = 0
msg = ' '

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
msg=' '

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
    color='black', colorSpace='rgb', opacity=0, 
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
    if t >= 0 and key_resp_7.status == NOT_STARTED:
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
    if t >= 0 and key_resp_8.status == NOT_STARTED:
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
    if t >= 0 and key_resp_5.status == NOT_STARTED:
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
endSwitchPractice = data.TrialHandler(nReps=1, method='sequential', 
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
    number_correct = 0
    
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
        trialList=data.importConditions('switch_practice.xlsx'),
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
    routineTimer.add(0.110000)
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
        frameRemains = 0.0 + .11- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    
# completed 1 repeats of 'endSwitchPractice'


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
    if t >= 0 and key_resp_9.status == NOT_STARTED:
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
