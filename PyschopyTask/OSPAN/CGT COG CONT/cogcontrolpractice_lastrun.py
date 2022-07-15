#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Jun 22 20:56:46 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'cogcontrolpractice'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/annarini/Downloads/CGT COG CONT/cogcontrolpractice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "CogConIns"
CogConInsClock = core.Clock()
CogIns = visual.TextStim(win=win, name='CogIns',
    text='Now you will particapte in a second task. In this task you will be asked to remember a series of letters followed by a random series of math equations. Please do your best to quickly and accuratley do the simple math problems. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "PracStart"
PracStartClock = core.Clock()
MathProb = visual.TextStim(win=win, name='MathProb',
    text='(link to chioceset?)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Ans = visual.TextStim(win=win, name='Ans',
    text='(alternate between right and wrong answers (ranomdly assing these?)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TorF = visual.TextStim(win=win, name='TorF',
    text="True or False\n\nPress 'V' for True and 'N' for False",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
T = keyboard.Keyboard()
F = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "CogConIns"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
CogConInsComponents = [CogIns, key_resp]
for thisComponent in CogConInsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CogConInsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CogConIns"-------
while continueRoutine:
    # get current time
    t = CogConInsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CogConInsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CogIns* updates
    if CogIns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CogIns.frameNStart = frameN  # exact frame index
        CogIns.tStart = t  # local t and not account for scr refresh
        CogIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CogIns, 'tStartRefresh')  # time at next scr refresh
        CogIns.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CogConInsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CogConIns"-------
for thisComponent in CogConInsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('CogIns.started', CogIns.tStartRefresh)
thisExp.addData('CogIns.stopped', CogIns.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "CogConIns" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracStart"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
T.keys = []
T.rt = []
_T_allKeys = []
F.keys = []
F.rt = []
_F_allKeys = []
# keep track of which components have finished
PracStartComponents = [MathProb, Ans, TorF, T, F]
for thisComponent in PracStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracStart"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PracStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MathProb* updates
    if MathProb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MathProb.frameNStart = frameN  # exact frame index
        MathProb.tStart = t  # local t and not account for scr refresh
        MathProb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MathProb, 'tStartRefresh')  # time at next scr refresh
        MathProb.setAutoDraw(True)
    if MathProb.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MathProb.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            MathProb.tStop = t  # not accounting for scr refresh
            MathProb.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MathProb, 'tStopRefresh')  # time at next scr refresh
            MathProb.setAutoDraw(False)
    
    # *Ans* updates
    if Ans.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        Ans.frameNStart = frameN  # exact frame index
        Ans.tStart = t  # local t and not account for scr refresh
        Ans.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ans, 'tStartRefresh')  # time at next scr refresh
        Ans.setAutoDraw(True)
    if Ans.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Ans.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            Ans.tStop = t  # not accounting for scr refresh
            Ans.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Ans, 'tStopRefresh')  # time at next scr refresh
            Ans.setAutoDraw(False)
    
    # *TorF* updates
    if TorF.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        TorF.frameNStart = frameN  # exact frame index
        TorF.tStart = t  # local t and not account for scr refresh
        TorF.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TorF, 'tStartRefresh')  # time at next scr refresh
        TorF.setAutoDraw(True)
    if TorF.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > TorF.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            TorF.tStop = t  # not accounting for scr refresh
            TorF.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TorF, 'tStopRefresh')  # time at next scr refresh
            TorF.setAutoDraw(False)
    
    # *T* updates
    waitOnFlip = False
    if T.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        T.frameNStart = frameN  # exact frame index
        T.tStart = t  # local t and not account for scr refresh
        T.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
        T.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(T.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(T.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if T.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > T.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            T.tStop = t  # not accounting for scr refresh
            T.frameNStop = frameN  # exact frame index
            win.timeOnFlip(T, 'tStopRefresh')  # time at next scr refresh
            T.status = FINISHED
    if T.status == STARTED and not waitOnFlip:
        theseKeys = T.getKeys(keyList=['v'], waitRelease=False)
        _T_allKeys.extend(theseKeys)
        if len(_T_allKeys):
            T.keys = _T_allKeys[-1].name  # just the last key pressed
            T.rt = _T_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *F* updates
    waitOnFlip = False
    if F.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        F.frameNStart = frameN  # exact frame index
        F.tStart = t  # local t and not account for scr refresh
        F.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
        F.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(F.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(F.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if F.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > F.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            F.tStop = t  # not accounting for scr refresh
            F.frameNStop = frameN  # exact frame index
            win.timeOnFlip(F, 'tStopRefresh')  # time at next scr refresh
            F.status = FINISHED
    if F.status == STARTED and not waitOnFlip:
        theseKeys = F.getKeys(keyList=['n'], waitRelease=False)
        _F_allKeys.extend(theseKeys)
        if len(_F_allKeys):
            F.keys = _F_allKeys[-1].name  # just the last key pressed
            F.rt = _F_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracStart"-------
for thisComponent in PracStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('MathProb.started', MathProb.tStartRefresh)
thisExp.addData('MathProb.stopped', MathProb.tStopRefresh)
thisExp.addData('Ans.started', Ans.tStartRefresh)
thisExp.addData('Ans.stopped', Ans.tStopRefresh)
thisExp.addData('TorF.started', TorF.tStartRefresh)
thisExp.addData('TorF.stopped', TorF.tStopRefresh)
# check responses
if T.keys in ['', [], None]:  # No response was made
    T.keys = None
thisExp.addData('T.keys',T.keys)
if T.keys != None:  # we had a response
    thisExp.addData('T.rt', T.rt)
thisExp.addData('T.started', T.tStartRefresh)
thisExp.addData('T.stopped', T.tStopRefresh)
thisExp.nextEntry()
# check responses
if F.keys in ['', [], None]:  # No response was made
    F.keys = None
thisExp.addData('F.keys',F.keys)
if F.keys != None:  # we had a response
    thisExp.addData('F.rt', F.rt)
thisExp.addData('F.started', F.tStartRefresh)
thisExp.addData('F.stopped', F.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
