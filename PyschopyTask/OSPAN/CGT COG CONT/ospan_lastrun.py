﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Thu Jul 14 14:54:26 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
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
psychopyVersion = '2022.2.1'
expName = 'ospan'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/shlab/Documents/GitHub/cgt/PyschopyTask/OSPAN/CGT COG CONT/ospan_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1120, 700], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "CogConIns1" ---

# --- Initialize components for Routine "CogConIns2" ---

# --- Initialize components for Routine "CogConIns3" ---

# --- Initialize components for Routine "Blank1" ---

# --- Initialize components for Routine "LetterPrac" ---
# Run 'Begin Experiment' code from Rand_Letter
# set location of the boxes and text
screensize = [1120,700]

col1 = screensize[0]*-.3
col2 = screensize[0]*-.1
col3 = screensize[0]*.1
row1 = screensize[1]*.3
row2 = screensize[1]*.15
row3 = screensize[1]*0
row4 = screensize[1]*-.15

specialBoxXaxis = screensize[0]*.4
blankBoxLoc = [specialBoxXaxis,screensize[1]*.35]
clearBoxLoc = [specialBoxXaxis, screensize[1]*0]
enterBoxLoc = [specialBoxXaxis, screensize[1]*-.35]
letterPractTextLoc = [0,screensize[1]*.4]

boxSize = [90,90]
specialBoxSize = [250,115]
textHeight = 45
boxTextHeight = 80
wrap = screensize[0]*.9

Fboxloc = [col1, row1]
Hboxloc = [col2, row1]
Jboxloc = [col3, row1]
Kboxloc = [col1, row2]
Lboxloc = [col2, row2]
Nboxloc = [col3, row2]
Pboxloc = [col1, row3]
Qboxloc = [col2, row3]
Rboxloc = [col3, row3]
Sboxloc = [col1, row4]
Tboxloc = [col2, row4]
Yboxloc = [col3, row4]
letterDisp = visual.TextStim(win=win, name='letterDisp',
    text='',
    font='Open Sans',
    pos=(0, 0), height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "isiPrac" ---
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=textHeight, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "itiPrac" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=textHeight, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Recall_Letters1" ---
# Run 'Begin Experiment' code from stimuliLocationSize
# set location of the boxes and text
screensize = [1120,700]

col1 = screensize[0]*-.3
col2 = screensize[0]*-.1
col3 = screensize[0]*.1
row1 = screensize[1]*.2
row2 = screensize[1]*.05
row3 = screensize[1]*-.1
row4 = screensize[1]*-.25

specialBoxXaxis = screensize[0]*.35
blankBoxLoc = [specialBoxXaxis,screensize[1]*.2]
clearBoxLoc = [specialBoxXaxis, screensize[1]*0]
enterBoxLoc = [specialBoxXaxis, screensize[1]*-.2]
letterPractTextLoc = [0,screensize[1]*.4]

boxSize = [90,90]
specialBoxSize = [250,115]
textHeight = 40
boxTextHeight = 70
wrap = screensize[0]*.9

Fboxloc = [col1, row1]
Hboxloc = [col2, row1]
Jboxloc = [col3, row1]
Kboxloc = [col1, row2]
Lboxloc = [col2, row2]
Nboxloc = [col3, row2]
Pboxloc = [col1, row3]
Qboxloc = [col2, row3]
Rboxloc = [col3, row3]
Sboxloc = [col1, row4]
Tboxloc = [col2, row4]
Yboxloc = [col3, row4]
PBox = visual.Rect(
    win=win, name='PBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Pboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
NBox2 = visual.Rect(
    win=win, name='NBox2',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Nboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
SBox2 = visual.Rect(
    win=win, name='SBox2',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Sboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
KBox2 = visual.Rect(
    win=win, name='KBox2',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Kboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
HBox = visual.Rect(
    win=win, name='HBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Hboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
FBox = visual.Rect(
    win=win, name='FBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Fboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
QBox = visual.Rect(
    win=win, name='QBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Qboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
LBox = visual.Rect(
    win=win, name='LBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Lboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
RBox = visual.Rect(
    win=win, name='RBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Rboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
TBox = visual.Rect(
    win=win, name='TBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Tboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
YBox = visual.Rect(
    win=win, name='YBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Yboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
JBox = visual.Rect(
    win=win, name='JBox',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Jboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)
letterPractText = visual.TextStim(win=win, name='letterPractText',
    text='Select the letters in the order presented. \nUse the blank button to fill in forgotten letters.',
    font='Open Sans',
    pos=letterPractTextLoc, height=textHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
P = visual.TextStim(win=win, name='P',
    text='P',
    font='Open Sans',
    pos=Pboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
F_2 = visual.TextStim(win=win, name='F_2',
    text='F',
    font='Open Sans',
    pos=Fboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
H = visual.TextStim(win=win, name='H',
    text='H',
    font='Open Sans',
    pos=Hboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
S = visual.TextStim(win=win, name='S',
    text='S',
    font='Open Sans',
    pos=Sboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
K = visual.TextStim(win=win, name='K',
    text='K',
    font='Open Sans',
    pos=Kboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
N = visual.TextStim(win=win, name='N',
    text='N',
    font='Open Sans',
    pos=Nboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
L = visual.TextStim(win=win, name='L',
    text='L',
    font='Open Sans',
    pos=Lboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Q = visual.TextStim(win=win, name='Q',
    text='Q',
    font='Open Sans',
    pos=Qboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
R = visual.TextStim(win=win, name='R',
    text='R',
    font='Open Sans',
    pos=Rboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
J = visual.TextStim(win=win, name='J',
    text='J',
    font='Open Sans',
    pos=Jboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
Y = visual.TextStim(win=win, name='Y',
    text='Y',
    font='Open Sans',
    pos=Yboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
T_2 = visual.TextStim(win=win, name='T_2',
    text='T',
    font='Open Sans',
    pos=Tboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
CLEAR = visual.Rect(
    win=win, name='CLEAR',
    width=specialBoxSize[0], height=specialBoxSize[1],
    ori=0.0, pos=clearBoxLoc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=None, depth=-26.0, interpolate=True)
ClearText = visual.TextStim(win=win, name='ClearText',
    text='CLEAR',
    font='Open Sans',
    pos=clearBoxLoc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-27.0);
BLANK = visual.Rect(
    win=win, name='BLANK',
    width=specialBoxSize[0], height=specialBoxSize[1],
    ori=0.0, pos=blankBoxLoc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-28.0, interpolate=True)
BlankText = visual.TextStim(win=win, name='BlankText',
    text='BLANK',
    font='Open Sans',
    pos=blankBoxLoc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='Black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-29.0);
ENTER = visual.Rect(
    win=win, name='ENTER',
    width=specialBoxSize[0], height=specialBoxSize[1],
    ori=0.0, pos=enterBoxLoc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='green',
    opacity=None, depth=-30.0, interpolate=True)
EnterText = visual.TextStim(win=win, name='EnterText',
    text='ENTER',
    font='Open Sans',
    pos=enterBoxLoc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-31.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "LetterScore" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='You recalled ___ letters correctly out of ___.',
    font='Open Sans',
    pos=(0, 0), height=boxTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "MathPracIns" ---

# --- Initialize components for Routine "MathPracIns2" ---

# --- Initialize components for Routine "MathPrac3" ---

# --- Initialize components for Routine "Blank1" ---

# --- Initialize components for Routine "MathPrac" ---

# --- Initialize components for Routine "isiPracMath" ---

# --- Initialize components for Routine "TF" ---
# Run 'Begin Experiment' code from code_2
#call right or wrong answer (some if then loop if correct maybe we need an excel sheet wiht the possible answers presented and true or false ? ( just maybe make it?) 

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "CogConIns1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
CogConIns1Components = []
for thisComponent in CogConIns1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CogConIns1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CogConIns1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CogConIns1" ---
for thisComponent in CogConIns1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CogConIns1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "CogConIns2" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
CogConIns2Components = []
for thisComponent in CogConIns2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CogConIns2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CogConIns2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CogConIns2" ---
for thisComponent in CogConIns2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CogConIns2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "CogConIns3" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
CogConIns3Components = []
for thisComponent in CogConIns3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CogConIns3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CogConIns3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CogConIns3" ---
for thisComponent in CogConIns3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CogConIns3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Blank1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank1Components = []
for thisComponent in Blank1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Blank1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Blank1" ---
for thisComponent in Blank1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Blank1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practiceletters.xlsx', selection='1'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "LetterPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Rand_Letter
    #import string
    #import random
    #string.ascii_letters
    #'FPQJHKTSNRYL'
    
    #random.choice(string.ascii_letters)
    #'F'
    # keep track of which components have finished
    LetterPracComponents = [letterDisp]
    for thisComponent in LetterPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LetterPrac" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letterDisp* updates
        if letterDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letterDisp.frameNStart = frameN  # exact frame index
            letterDisp.tStart = t  # local t and not account for scr refresh
            letterDisp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterDisp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letterDisp.started')
            letterDisp.setAutoDraw(True)
        if letterDisp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letterDisp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                letterDisp.tStop = t  # not accounting for scr refresh
                letterDisp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'letterDisp.stopped')
                letterDisp.setAutoDraw(False)
        if letterDisp.status == STARTED:  # only update if drawing
            letterDisp.setText(letters, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LetterPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LetterPrac" ---
    for thisComponent in LetterPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "isiPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiPracComponents = [isiText]
    for thisComponent in isiPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "isiPrac" ---
    while continueRoutine and routineTimer.getTime() < 0.25:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiText* updates
        if isiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiText.frameNStart = frameN  # exact frame index
            isiText.tStart = t  # local t and not account for scr refresh
            isiText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiText.started')
            isiText.setAutoDraw(True)
        if isiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiText.tStartRefresh + 0.250-frameTolerance:
                # keep track of stop time/frame for later
                isiText.tStop = t  # not accounting for scr refresh
                isiText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiText.stopped')
                isiText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isiPrac" ---
    for thisComponent in isiPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.250000)
    
    # --- Prepare to start Routine "itiPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiPracComponents = [text_2]
    for thisComponent in itiPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "itiPrac" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "itiPrac" ---
    for thisComponent in itiPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Recall_Letters1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stimuliLocationSize
    # set location of the boxes and text
    
    
    col1 = -200
    col2 = 0
    col3 = 200
    row1 = 200
    row2 = 100
    row3 = 0
    row4 = -100
    
    specialBoxXaxis = 275
    blankBoxLoc = [specialBoxXaxis,-175]
    clearBoxLoc = [specialBoxXaxis, 0]
    enterBoxLoc = [specialBoxXaxis, 175]
    
    boxSize = [80,80]
    specialBoxSize = [200,115]
    
    Fboxloc = [col1, row1]
    Hboxloc = [col2, row1]
    Jboxloc = [col3, row1]
    Kboxloc = [col1, row2]
    Lboxloc = [col2, row2]
    Nboxloc = [col3, row2]
    Pboxloc = [col1, row3]
    Qboxloc = [col2, row3]
    Rboxloc = [col3, row3]
    Sboxloc = [col1, row4]
    Tboxloc = [col2, row4]
    Yboxloc = [col3, row4]
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from mouserecall
    clicked_things = [] 
    
    # keep track of which components have finished
    Recall_Letters1Components = [PBox, NBox2, SBox2, KBox2, HBox, FBox, QBox, LBox, RBox, TBox, YBox, JBox, letterPractText, P, F_2, H, S, K, N, L, Q, R, J, Y, T_2, CLEAR, ClearText, BLANK, BlankText, ENTER, EnterText, mouse]
    for thisComponent in Recall_Letters1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Recall_Letters1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PBox* updates
        if PBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PBox.frameNStart = frameN  # exact frame index
            PBox.tStart = t  # local t and not account for scr refresh
            PBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PBox.started')
            PBox.setAutoDraw(True)
        
        # *NBox2* updates
        if NBox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NBox2.frameNStart = frameN  # exact frame index
            NBox2.tStart = t  # local t and not account for scr refresh
            NBox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NBox2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NBox2.started')
            NBox2.setAutoDraw(True)
        
        # *SBox2* updates
        if SBox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SBox2.frameNStart = frameN  # exact frame index
            SBox2.tStart = t  # local t and not account for scr refresh
            SBox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SBox2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SBox2.started')
            SBox2.setAutoDraw(True)
        
        # *KBox2* updates
        if KBox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            KBox2.frameNStart = frameN  # exact frame index
            KBox2.tStart = t  # local t and not account for scr refresh
            KBox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KBox2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KBox2.started')
            KBox2.setAutoDraw(True)
        
        # *HBox* updates
        if HBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HBox.frameNStart = frameN  # exact frame index
            HBox.tStart = t  # local t and not account for scr refresh
            HBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HBox.started')
            HBox.setAutoDraw(True)
        
        # *FBox* updates
        if FBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FBox.frameNStart = frameN  # exact frame index
            FBox.tStart = t  # local t and not account for scr refresh
            FBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FBox.started')
            FBox.setAutoDraw(True)
        
        # *QBox* updates
        if QBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QBox.frameNStart = frameN  # exact frame index
            QBox.tStart = t  # local t and not account for scr refresh
            QBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'QBox.started')
            QBox.setAutoDraw(True)
        
        # *LBox* updates
        if LBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LBox.frameNStart = frameN  # exact frame index
            LBox.tStart = t  # local t and not account for scr refresh
            LBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'LBox.started')
            LBox.setAutoDraw(True)
        
        # *RBox* updates
        if RBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RBox.frameNStart = frameN  # exact frame index
            RBox.tStart = t  # local t and not account for scr refresh
            RBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RBox.started')
            RBox.setAutoDraw(True)
        
        # *TBox* updates
        if TBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TBox.frameNStart = frameN  # exact frame index
            TBox.tStart = t  # local t and not account for scr refresh
            TBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TBox.started')
            TBox.setAutoDraw(True)
        
        # *YBox* updates
        if YBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YBox.frameNStart = frameN  # exact frame index
            YBox.tStart = t  # local t and not account for scr refresh
            YBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'YBox.started')
            YBox.setAutoDraw(True)
        
        # *JBox* updates
        if JBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            JBox.frameNStart = frameN  # exact frame index
            JBox.tStart = t  # local t and not account for scr refresh
            JBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(JBox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'JBox.started')
            JBox.setAutoDraw(True)
        
        # *letterPractText* updates
        if letterPractText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letterPractText.frameNStart = frameN  # exact frame index
            letterPractText.tStart = t  # local t and not account for scr refresh
            letterPractText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterPractText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letterPractText.started')
            letterPractText.setAutoDraw(True)
        
        # *P* updates
        if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P.frameNStart = frameN  # exact frame index
            P.tStart = t  # local t and not account for scr refresh
            P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P.started')
            P.setAutoDraw(True)
        
        # *F_2* updates
        if F_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_2.frameNStart = frameN  # exact frame index
            F_2.tStart = t  # local t and not account for scr refresh
            F_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'F_2.started')
            F_2.setAutoDraw(True)
        
        # *H* updates
        if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H.frameNStart = frameN  # exact frame index
            H.tStart = t  # local t and not account for scr refresh
            H.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'H.started')
            H.setAutoDraw(True)
        
        # *S* updates
        if S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S.frameNStart = frameN  # exact frame index
            S.tStart = t  # local t and not account for scr refresh
            S.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'S.started')
            S.setAutoDraw(True)
        
        # *K* updates
        if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K.frameNStart = frameN  # exact frame index
            K.tStart = t  # local t and not account for scr refresh
            K.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'K.started')
            K.setAutoDraw(True)
        
        # *N* updates
        if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N.frameNStart = frameN  # exact frame index
            N.tStart = t  # local t and not account for scr refresh
            N.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'N.started')
            N.setAutoDraw(True)
        
        # *L* updates
        if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L.frameNStart = frameN  # exact frame index
            L.tStart = t  # local t and not account for scr refresh
            L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L.started')
            L.setAutoDraw(True)
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q.started')
            Q.setAutoDraw(True)
        
        # *R* updates
        if R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R.frameNStart = frameN  # exact frame index
            R.tStart = t  # local t and not account for scr refresh
            R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R.started')
            R.setAutoDraw(True)
        
        # *J* updates
        if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J.frameNStart = frameN  # exact frame index
            J.tStart = t  # local t and not account for scr refresh
            J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'J.started')
            J.setAutoDraw(True)
        
        # *Y* updates
        if Y.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y.frameNStart = frameN  # exact frame index
            Y.tStart = t  # local t and not account for scr refresh
            Y.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Y.started')
            Y.setAutoDraw(True)
        
        # *T_2* updates
        if T_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T_2.frameNStart = frameN  # exact frame index
            T_2.tStart = t  # local t and not account for scr refresh
            T_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'T_2.started')
            T_2.setAutoDraw(True)
        
        # *CLEAR* updates
        if CLEAR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CLEAR.frameNStart = frameN  # exact frame index
            CLEAR.tStart = t  # local t and not account for scr refresh
            CLEAR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CLEAR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CLEAR.started')
            CLEAR.setAutoDraw(True)
        
        # *ClearText* updates
        if ClearText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ClearText.frameNStart = frameN  # exact frame index
            ClearText.tStart = t  # local t and not account for scr refresh
            ClearText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ClearText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ClearText.started')
            ClearText.setAutoDraw(True)
        
        # *BLANK* updates
        if BLANK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BLANK.frameNStart = frameN  # exact frame index
            BLANK.tStart = t  # local t and not account for scr refresh
            BLANK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BLANK, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BLANK.started')
            BLANK.setAutoDraw(True)
        
        # *BlankText* updates
        if BlankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlankText.frameNStart = frameN  # exact frame index
            BlankText.tStart = t  # local t and not account for scr refresh
            BlankText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankText.started')
            BlankText.setAutoDraw(True)
        
        # *ENTER* updates
        if ENTER.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ENTER.frameNStart = frameN  # exact frame index
            ENTER.tStart = t  # local t and not account for scr refresh
            ENTER.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ENTER, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ENTER.started')
            ENTER.setAutoDraw(True)
        
        # *EnterText* updates
        if EnterText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EnterText.frameNStart = frameN  # exact frame index
            EnterText.tStart = t  # local t and not account for scr refresh
            EnterText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EnterText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EnterText.started')
            EnterText.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(ENTER)
                        clickableList = ENTER
                    except:
                        clickableList = [ENTER]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        # Run 'Each Frame' code from mouserecall
        clickables = [FBox, KBox2, PBox, SBox2, HBox, LBox, QBox, TBox, JBox, NBox2, RBox, YBox, BLANK, CLEAR]
        
        #check if the mouse is pressed in any of the boxes
        for clickable in clickables: # for our shapes that can be clicked on
            if mouse.isPressedIn(clickable): #if the mouse is clikced on one of the shapes
                clicked_things.append(clickable.name) #add the name of the shape that was clicked
                mouse.clickReset() #resets mouse click
               
                if clickable == CLEAR: # if the clear button was pressed
                    clicked_things = [] # reset our clicked_thing variable
                    FBox.color = "white" #and then reset our shapes to have white boxes
                    KBox2.color = "white"
                    PBox.color = "white"
                    SBox2.color = "white"
                    HBox.color = "white"
                    LBox.color = "white"
                    QBox.color = "white"
                    TBox.color = "white"
                    JBox.color = "white"
                    NBox2.color = "white"
                    RBox.color = "white"
                    YBox.color = "white"
                    
        #change box to blue if clicked unless its the blank box
        # clickedN = 0 
        for clickable in clickables: 
            if clickable.name in clicked_things and not clickable.name == BLANK: 
                clickable.color = 'blue' 
                
         #clickedN += 1
                
        
        #if mouse.isPressedIn(ENTER):
        #    continueRoutine=False
            
        #if clickedN == 3 and not waiting: 
        #    waiting = True
        #    startTime = t 
          
        #if clickedN == 3 and not waiting: 
        #    if t > startTime + 0.05: 
        #        continueRoutine = False 
           
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recall_Letters1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall_Letters1" ---
    for thisComponent in Recall_Letters1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse.x', mouse.x)
    trials_2.addData('mouse.y', mouse.y)
    trials_2.addData('mouse.leftButton', mouse.leftButton)
    trials_2.addData('mouse.midButton', mouse.midButton)
    trials_2.addData('mouse.rightButton', mouse.rightButton)
    trials_2.addData('mouse.time', mouse.time)
    trials_2.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "Recall_Letters1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LetterScore" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    LetterScoreComponents = [text_3]
    for thisComponent in LetterScoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LetterScore" ---
    while continueRoutine and routineTimer.getTime() < 4.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LetterScoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LetterScore" ---
    for thisComponent in LetterScoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "MathPracIns" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPracInsComponents = []
for thisComponent in MathPracInsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MathPracIns" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MathPracInsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPracIns" ---
for thisComponent in MathPracInsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPracIns" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MathPracIns2" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPracIns2Components = []
for thisComponent in MathPracIns2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MathPracIns2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MathPracIns2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPracIns2" ---
for thisComponent in MathPracIns2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPracIns2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MathPrac3" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPrac3Components = []
for thisComponent in MathPrac3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MathPrac3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MathPrac3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPrac3" ---
for thisComponent in MathPrac3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPrac3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Blank1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Blank1Components = []
for thisComponent in Blank1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Blank1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Blank1" ---
for thisComponent in Blank1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Blank1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MathPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from MathProb_2
    # show problem on screen
    # keep track of which components have finished
    MathPracComponents = []
    for thisComponent in MathPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "MathPrac" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MathPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MathPrac" ---
    for thisComponent in MathPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MathPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "isiPracMath" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiPracMathComponents = []
    for thisComponent in isiPracMathComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "isiPracMath" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiPracMathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isiPracMath" ---
    for thisComponent in isiPracMathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isiPracMath" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TF" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    TFComponents = []
    for thisComponent in TFComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TF" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TF" ---
    for thisComponent in TFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "TF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_3'


# --- End experiment ---
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