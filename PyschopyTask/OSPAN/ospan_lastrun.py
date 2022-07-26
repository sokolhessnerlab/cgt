#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Tue Jul 26 13:01:54 2022
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
blankText = visual.TextStim(win=win, name='blankText',
    text=' \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "selectLetters" ---

# --- Initialize components for Routine "LetterPrac" ---
# Run 'Begin Experiment' code from Rand_Letter
import random

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

#practiceSetSize = [2,2,3,3]
#practiceSetSize = random.choices(practiceSetSize, k=4)
letters = ['F','K','P','S','H','L','Q','T','J','N', 'R', 'Y']
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

recallTextLoc = [col2,screensize[1]*-.4]
P = visual.Rect(
    win=win, name='P',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Pboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
N = visual.Rect(
    win=win, name='N',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Nboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
S = visual.Rect(
    win=win, name='S',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Sboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
K = visual.Rect(
    win=win, name='K',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Kboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
H = visual.Rect(
    win=win, name='H',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Hboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
F = visual.Rect(
    win=win, name='F',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Fboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
Q = visual.Rect(
    win=win, name='Q',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Qboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
L = visual.Rect(
    win=win, name='L',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Lboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
R = visual.Rect(
    win=win, name='R',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Rboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
T = visual.Rect(
    win=win, name='T',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Tboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
Y = visual.Rect(
    win=win, name='Y',
    width=boxSize[0], height=boxSize[1],
    ori=0.0, pos=Yboxloc, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
J = visual.Rect(
    win=win, name='J',
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
Ptext = visual.TextStim(win=win, name='Ptext',
    text='P',
    font='Open Sans',
    pos=Pboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Ftext = visual.TextStim(win=win, name='Ftext',
    text='F',
    font='Open Sans',
    pos=Fboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
Htext = visual.TextStim(win=win, name='Htext',
    text='H',
    font='Open Sans',
    pos=Hboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Stext = visual.TextStim(win=win, name='Stext',
    text='S',
    font='Open Sans',
    pos=Sboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
Ktext = visual.TextStim(win=win, name='Ktext',
    text='K',
    font='Open Sans',
    pos=Kboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Ntext = visual.TextStim(win=win, name='Ntext',
    text='N',
    font='Open Sans',
    pos=Nboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
Ltext = visual.TextStim(win=win, name='Ltext',
    text='L',
    font='Open Sans',
    pos=Lboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
Qtext = visual.TextStim(win=win, name='Qtext',
    text='Q',
    font='Open Sans',
    pos=Qboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
Rtext = visual.TextStim(win=win, name='Rtext',
    text='R',
    font='Open Sans',
    pos=Rboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
Jtext = visual.TextStim(win=win, name='Jtext',
    text='J',
    font='Open Sans',
    pos=Jboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
Ytext = visual.TextStim(win=win, name='Ytext',
    text='Y',
    font='Open Sans',
    pos=Yboxloc, height=boxTextHeight, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
Ttext = visual.TextStim(win=win, name='Ttext',
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
# Run 'Begin Experiment' code from mouserecall
myClock = core.Clock()
showRecall = visual.TextStim(win=win, name='showRecall',
    text='',
    font='Open Sans',
    pos=recallTextLoc, height=textHeight, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);

# --- Initialize components for Routine "LetterScore" ---
recallScore = visual.TextStim(win=win, name='recallScore',
    text='',
    font='Open Sans',
    pos=(0, 0), height=boxTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "MathPracticeInst1" ---

# --- Initialize components for Routine "MathPracticeInst2" ---

# --- Initialize components for Routine "MathPracticeInst3" ---

# --- Initialize components for Routine "selectMathProbs" ---
# Run 'Begin Experiment' code from selectMathCode
percrand =[1,1,1,1,1,2,2,2,2,2]
mathCorr =[True,True,True,True,True,False, False, False, False,False]
op2 = [1,2,3,4,5,6,7,8,9]
sign = ["+","-"]
sum2 = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]

mathPractCount = 0

# --- Initialize components for Routine "Blank1" ---
blankText = visual.TextStim(win=win, name='blankText',
    text=' \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "MathPrac" ---
showMathProblemPractice = visual.TextStim(win=win, name='showMathProblemPractice',
    text='',
    font='Open Sans',
    pos=(0, 0), height=textHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyboard_moveToTF = keyboard.Keyboard()

# --- Initialize components for Routine "isiPracMath" ---
isiPracMath2 = visual.TextStim(win=win, name='isiPracMath2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=textHeight, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "TF" ---
TrueBoxPractice = visual.Rect(
    win=win, name='TrueBoxPractice',
    width=(150, 100)[0], height=(150, 100)[1],
    ori=0.0, pos=(-200, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='Green',
    opacity=None, depth=0.0, interpolate=True)
TrueTextPractice = visual.TextStim(win=win, name='TrueTextPractice',
    text='TRUE',
    font='Open Sans',
    units='pix', pos=(-200, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FalseBoxPractice = visual.Rect(
    win=win, name='FalseBoxPractice',
    width=(150, 100)[0], height=(150, 100)[1],
    ori=0.0, pos=(200, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=None, depth=-2.0, interpolate=True)
FalseTextPractice = visual.TextStim(win=win, name='FalseTextPractice',
    text='FALSE',
    font='Open Sans',
    units='pix', pos=(200, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

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
Blank1Components = [blankText]
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
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blankText* updates
    if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blankText.frameNStart = frameN  # exact frame index
        blankText.tStart = t  # local t and not account for scr refresh
        blankText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blankText.started')
        blankText.setAutoDraw(True)
    if blankText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blankText.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            blankText.tStop = t  # not accounting for scr refresh
            blankText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blankText.stopped')
            blankText.setAutoDraw(False)
    
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
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
bigLetterLoop = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('setSizeLetterPractice.xlsx'),
    seed=None, name='bigLetterLoop')
thisExp.addLoop(bigLetterLoop)  # add the loop to the experiment
thisBigLetterLoop = bigLetterLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBigLetterLoop.rgb)
if thisBigLetterLoop != None:
    for paramName in thisBigLetterLoop:
        exec('{} = thisBigLetterLoop[paramName]'.format(paramName))

for thisBigLetterLoop in bigLetterLoop:
    currentLoop = bigLetterLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBigLetterLoop.rgb)
    if thisBigLetterLoop != None:
        for paramName in thisBigLetterLoop:
            exec('{} = thisBigLetterLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectLetters" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectLetters_2
    lettersShown = [];
    
    while len(lettersShown) < setSize:
        singleLetter = random.choice(letters)
    
        if not singleLetter in lettersShown:
           lettersShown.append(singleLetter)
            
       
    # keep track of which components have finished
    selectLettersComponents = []
    for thisComponent in selectLettersComponents:
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
    
    # --- Run Routine "selectLetters" ---
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
        for thisComponent in selectLettersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectLetters" ---
    for thisComponent in selectLettersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from selectLetters_2
    thisExp.addData('lettersShown', lettersShown)
    # the Routine "selectLetters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=setSize, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        #import random
        #lettersShown = random.choices(letters,k=setSize,replace=False)
        tmpLetter = lettersShown[trials.thisN]
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
                letterDisp.setText(tmpLetter, log=False)
            
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
        
    # completed setSize repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    recall = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='recall')
    thisExp.addLoop(recall)  # add the loop to the experiment
    thisRecall = recall.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
    if thisRecall != None:
        for paramName in thisRecall:
            exec('{} = thisRecall[paramName]'.format(paramName))
    
    for thisRecall in recall:
        currentLoop = recall
        # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
        if thisRecall != None:
            for paramName in thisRecall:
                exec('{} = thisRecall[paramName]'.format(paramName))
        
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
        timeAfterClick = 0
        
        F.color = "white" #and then reset our shapes to have white boxes
        K.color = "white"
        P.color = "white"
        S.color = "white"
        H.color = "white"
        L.color = "white"
        Q.color = "white"
        T.color = "white"
        J.color = "white"
        N.color = "white"
        R.color = "white"
        Y.color = "white"
        
        myClock.reset()
        t = myClock.getTime()
        
        
        # keep track of which components have finished
        Recall_Letters1Components = [P, N, S, K, H, F, Q, L, R, T, Y, J, letterPractText, Ptext, Ftext, Htext, Stext, Ktext, Ntext, Ltext, Qtext, Rtext, Jtext, Ytext, Ttext, CLEAR, ClearText, BLANK, BlankText, ENTER, EnterText, mouse, showRecall]
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
            
            # *F* updates
            if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                F.frameNStart = frameN  # exact frame index
                F.tStart = t  # local t and not account for scr refresh
                F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'F.started')
                F.setAutoDraw(True)
            
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
            
            # *T* updates
            if T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T.frameNStart = frameN  # exact frame index
                T.tStart = t  # local t and not account for scr refresh
                T.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T.started')
                T.setAutoDraw(True)
            
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
            
            # *Ptext* updates
            if Ptext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ptext.frameNStart = frameN  # exact frame index
                Ptext.tStart = t  # local t and not account for scr refresh
                Ptext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ptext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ptext.started')
                Ptext.setAutoDraw(True)
            
            # *Ftext* updates
            if Ftext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ftext.frameNStart = frameN  # exact frame index
                Ftext.tStart = t  # local t and not account for scr refresh
                Ftext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ftext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ftext.started')
                Ftext.setAutoDraw(True)
            
            # *Htext* updates
            if Htext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Htext.frameNStart = frameN  # exact frame index
                Htext.tStart = t  # local t and not account for scr refresh
                Htext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Htext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Htext.started')
                Htext.setAutoDraw(True)
            
            # *Stext* updates
            if Stext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stext.frameNStart = frameN  # exact frame index
                Stext.tStart = t  # local t and not account for scr refresh
                Stext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stext.started')
                Stext.setAutoDraw(True)
            
            # *Ktext* updates
            if Ktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ktext.frameNStart = frameN  # exact frame index
                Ktext.tStart = t  # local t and not account for scr refresh
                Ktext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ktext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ktext.started')
                Ktext.setAutoDraw(True)
            
            # *Ntext* updates
            if Ntext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ntext.frameNStart = frameN  # exact frame index
                Ntext.tStart = t  # local t and not account for scr refresh
                Ntext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ntext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ntext.started')
                Ntext.setAutoDraw(True)
            
            # *Ltext* updates
            if Ltext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ltext.frameNStart = frameN  # exact frame index
                Ltext.tStart = t  # local t and not account for scr refresh
                Ltext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ltext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ltext.started')
                Ltext.setAutoDraw(True)
            
            # *Qtext* updates
            if Qtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Qtext.frameNStart = frameN  # exact frame index
                Qtext.tStart = t  # local t and not account for scr refresh
                Qtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Qtext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Qtext.started')
                Qtext.setAutoDraw(True)
            
            # *Rtext* updates
            if Rtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Rtext.frameNStart = frameN  # exact frame index
                Rtext.tStart = t  # local t and not account for scr refresh
                Rtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Rtext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Rtext.started')
                Rtext.setAutoDraw(True)
            
            # *Jtext* updates
            if Jtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Jtext.frameNStart = frameN  # exact frame index
                Jtext.tStart = t  # local t and not account for scr refresh
                Jtext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Jtext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Jtext.started')
                Jtext.setAutoDraw(True)
            
            # *Ytext* updates
            if Ytext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ytext.frameNStart = frameN  # exact frame index
                Ytext.tStart = t  # local t and not account for scr refresh
                Ytext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ytext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ytext.started')
                Ytext.setAutoDraw(True)
            
            # *Ttext* updates
            if Ttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Ttext.frameNStart = frameN  # exact frame index
                Ttext.tStart = t  # local t and not account for scr refresh
                Ttext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Ttext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ttext.started')
                Ttext.setAutoDraw(True)
            
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
            if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouse.started')
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
            clickables = [F, K, P, S, H, L, Q, T, J, N, R, Y, BLANK, CLEAR]
            
            #check if the mouse is pressed in any of the boxes
            for clickable in clickables: # for our shapes that can be clicked on
                #timeAfterClick += 1
                if mouse.isPressedIn(clickable) and t > timeAfterClick:
                    timeAfterClick = t + .5
                    clicked_things.append(clickable.name) #add the name of the shape that was clicked
                    mouse.clickReset() #resets mouse click
                   
                    if clickable == CLEAR: # if the clear button was pressed
                        clicked_things = [] # reset our clicked_thing variable
                        F.color = "white" #and then reset our shapes to have white boxes
                        K.color = "white"
                        P.color = "white"
                        S.color = "white"
                        H.color = "white"
                        L.color = "white"
                        Q.color = "white"
                        T.color = "white"
                        J.color = "white"
                        N.color = "white"
                        R.color = "white"
                        Y.color = "white"
                        
            #change box to blue if clicked unless its the blank box
            # clickedN = 0 
            for clickable in clickables: 
                if clickable.name in clicked_things and not clickable.name == 'BLANK': 
                    clickable.color = 'blue' 
            
            # prep the text that shows participant's responses (letters)
            responseText='' 
            for l in range(len(clicked_things)):
                  if clicked_things[l] == "BLANK":
                    clicked_things[l] = "*"
                  responseText = "%s %s " % (responseText, clicked_things[l])
                  
                  
            #print(timeAfterClick)
            
            # *showRecall* updates
            if showRecall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                showRecall.frameNStart = frameN  # exact frame index
                showRecall.tStart = t  # local t and not account for scr refresh
                showRecall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(showRecall, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'showRecall.started')
                showRecall.setAutoDraw(True)
            if showRecall.status == STARTED:  # only update if drawing
                showRecall.setText(responseText, log=False)
            
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
        # store data for recall (TrialHandler)
        recall.addData('mouse.x', mouse.x)
        recall.addData('mouse.y', mouse.y)
        recall.addData('mouse.leftButton', mouse.leftButton)
        recall.addData('mouse.midButton', mouse.midButton)
        recall.addData('mouse.rightButton', mouse.rightButton)
        recall.addData('mouse.time', mouse.time)
        recall.addData('mouse.clicked_name', mouse.clicked_name)
        # Run 'End Routine' code from mouserecall
        thisExp.addData("letterRecall", clicked_things)
        # the Routine "Recall_Letters1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "LetterScore" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from scoring
        correctCount = 0
        
        if len(clicked_things) >= setSize:
            for l in range(setSize):
                if clicked_things[l] == lettersShown[l]:
                    correctCount +=1
        elif len(clicked_things) ==0:
            correctCount = 0
        elif len(clicked_things)==1:
                if clicked_things[0] == lettersShown[0]:
                    correctCount +=1
            
        
        # keep track of which components have finished
        LetterScoreComponents = [recallScore]
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
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recallScore* updates
            if recallScore.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recallScore.frameNStart = frameN  # exact frame index
                recallScore.tStart = t  # local t and not account for scr refresh
                recallScore.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recallScore, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recallScore.started')
                recallScore.setAutoDraw(True)
            if recallScore.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recallScore.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    recallScore.tStop = t  # not accounting for scr refresh
                    recallScore.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recallScore.stopped')
                    recallScore.setAutoDraw(False)
            if recallScore.status == STARTED:  # only update if drawing
                recallScore.setText("You recalled " + str(correctCount) + " letters correctly out of " + str(setSize), log=False)
            
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
        # Run 'End Routine' code from scoring
        thisExp.addData("correctCount", correctCount)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'recall'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'bigLetterLoop'


# --- Prepare to start Routine "MathPracticeInst1" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPracticeInst1Components = []
for thisComponent in MathPracticeInst1Components:
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

# --- Run Routine "MathPracticeInst1" ---
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
    for thisComponent in MathPracticeInst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPracticeInst1" ---
for thisComponent in MathPracticeInst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPracticeInst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MathPracticeInst2" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPracticeInst2Components = []
for thisComponent in MathPracticeInst2Components:
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

# --- Run Routine "MathPracticeInst2" ---
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
    for thisComponent in MathPracticeInst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPracticeInst2" ---
for thisComponent in MathPracticeInst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPracticeInst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MathPracticeInst3" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
MathPracticeInst3Components = []
for thisComponent in MathPracticeInst3Components:
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

# --- Run Routine "MathPracticeInst3" ---
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
    for thisComponent in MathPracticeInst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MathPracticeInst3" ---
for thisComponent in MathPracticeInst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MathPracticeInst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mathPracticeTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('operationSet1_noParen.xlsx'),
    seed=None, name='mathPracticeTrials')
thisExp.addLoop(mathPracticeTrials)  # add the loop to the experiment
thisMathPracticeTrial = mathPracticeTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMathPracticeTrial.rgb)
if thisMathPracticeTrial != None:
    for paramName in thisMathPracticeTrial:
        exec('{} = thisMathPracticeTrial[paramName]'.format(paramName))

for thisMathPracticeTrial in mathPracticeTrials:
    currentLoop = mathPracticeTrials
    # abbreviate parameter names if possible (e.g. rgb = thisMathPracticeTrial.rgb)
    if thisMathPracticeTrial != None:
        for paramName in thisMathPracticeTrial:
            exec('{} = thisMathPracticeTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectMathProbs" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectMathCode
    import random
    
    tmpMathOp2 = str(random.choice(op2))
    tmpSign = random.choice(sign)
    suggestedAns = str(random.choice(sum2))
    
    
    # keep track of which components have finished
    selectMathProbsComponents = []
    for thisComponent in selectMathProbsComponents:
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
    
    # --- Run Routine "selectMathProbs" ---
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
        for thisComponent in selectMathProbsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectMathProbs" ---
    for thisComponent in selectMathProbsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from selectMathCode
    mathPractCount +=1
    if mathPractCount > 14:
        mathPracticeTrials.finished = True
    
    thisExp.addData("operation1", problem)
    thisExp.addData("sign", tmpSign)
    thisExp.addData("operation2",tmpMathOp2)
    thisExp.addData("suggestedAnswer", suggestedAns)
    # the Routine "selectMathProbs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Blank1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank1Components = [blankText]
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
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankText* updates
        if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankText.frameNStart = frameN  # exact frame index
            blankText.tStart = t  # local t and not account for scr refresh
            blankText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blankText.started')
            blankText.setAutoDraw(True)
        if blankText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blankText.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blankText.tStop = t  # not accounting for scr refresh
                blankText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankText.stopped')
                blankText.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "MathPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from MathProb_2
    qMark = " = ?"
    
    showMathProblem = "(" + problem + ")"  + tmpSign + tmpMathOp2 + qMark
    keyboard_moveToTF.keys = []
    keyboard_moveToTF.rt = []
    _keyboard_moveToTF_allKeys = []
    # keep track of which components have finished
    MathPracComponents = [showMathProblemPractice, keyboard_moveToTF]
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
        
        # *showMathProblemPractice* updates
        if showMathProblemPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            showMathProblemPractice.frameNStart = frameN  # exact frame index
            showMathProblemPractice.tStart = t  # local t and not account for scr refresh
            showMathProblemPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showMathProblemPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'showMathProblemPractice.started')
            showMathProblemPractice.setAutoDraw(True)
        if showMathProblemPractice.status == STARTED:  # only update if drawing
            showMathProblemPractice.setText(showMathProblem + "\n\n\n\n\nWhen you have solved the math problem, click 'enter' to continue.", log=False)
        
        # *keyboard_moveToTF* updates
        waitOnFlip = False
        if keyboard_moveToTF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyboard_moveToTF.frameNStart = frameN  # exact frame index
            keyboard_moveToTF.tStart = t  # local t and not account for scr refresh
            keyboard_moveToTF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboard_moveToTF, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyboard_moveToTF.started')
            keyboard_moveToTF.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyboard_moveToTF.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyboard_moveToTF.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyboard_moveToTF.status == STARTED and not waitOnFlip:
            theseKeys = keyboard_moveToTF.getKeys(keyList=['return'], waitRelease=False)
            _keyboard_moveToTF_allKeys.extend(theseKeys)
            if len(_keyboard_moveToTF_allKeys):
                keyboard_moveToTF.keys = _keyboard_moveToTF_allKeys[-1].name  # just the last key pressed
                keyboard_moveToTF.rt = _keyboard_moveToTF_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # check responses
    if keyboard_moveToTF.keys in ['', [], None]:  # No response was made
        keyboard_moveToTF.keys = None
    mathPracticeTrials.addData('keyboard_moveToTF.keys',keyboard_moveToTF.keys)
    if keyboard_moveToTF.keys != None:  # we had a response
        mathPracticeTrials.addData('keyboard_moveToTF.rt', keyboard_moveToTF.rt)
    # the Routine "MathPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "isiPracMath" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiPracMathComponents = [isiPracMath2]
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
    while continueRoutine and routineTimer.getTime() < 0.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiPracMath2* updates
        if isiPracMath2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiPracMath2.frameNStart = frameN  # exact frame index
            isiPracMath2.tStart = t  # local t and not account for scr refresh
            isiPracMath2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiPracMath2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiPracMath2.started')
            isiPracMath2.setAutoDraw(True)
        if isiPracMath2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiPracMath2.tStartRefresh + .200-frameTolerance:
                # keep track of stop time/frame for later
                isiPracMath2.tStop = t  # not accounting for scr refresh
                isiPracMath2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiPracMath2.stopped')
                isiPracMath2.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.200000)
    
    # --- Prepare to start Routine "TF" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    TFComponents = [TrueBoxPractice, TrueTextPractice, FalseBoxPractice, FalseTextPractice, mouse_2]
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
        
        # *TrueBoxPractice* updates
        if TrueBoxPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrueBoxPractice.frameNStart = frameN  # exact frame index
            TrueBoxPractice.tStart = t  # local t and not account for scr refresh
            TrueBoxPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrueBoxPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrueBoxPractice.started')
            TrueBoxPractice.setAutoDraw(True)
        
        # *TrueTextPractice* updates
        if TrueTextPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrueTextPractice.frameNStart = frameN  # exact frame index
            TrueTextPractice.tStart = t  # local t and not account for scr refresh
            TrueTextPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrueTextPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrueTextPractice.started')
            TrueTextPractice.setAutoDraw(True)
        
        # *FalseBoxPractice* updates
        if FalseBoxPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FalseBoxPractice.frameNStart = frameN  # exact frame index
            FalseBoxPractice.tStart = t  # local t and not account for scr refresh
            FalseBoxPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FalseBoxPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FalseBoxPractice.started')
            FalseBoxPractice.setAutoDraw(True)
        
        # *FalseTextPractice* updates
        if FalseTextPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FalseTextPractice.frameNStart = frameN  # exact frame index
            FalseTextPractice.tStart = t  # local t and not account for scr refresh
            FalseTextPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FalseTextPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FalseTextPractice.started')
            FalseTextPractice.setAutoDraw(True)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(TrueBoxPractice)
                        clickableList = TrueBoxPractice
                    except:
                        clickableList = [TrueBoxPractice]
                    for obj in clickableList:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
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
    # store data for mathPracticeTrials (TrialHandler)
    mathPracticeTrials.addData('mouse_2.x', mouse_2.x)
    mathPracticeTrials.addData('mouse_2.y', mouse_2.y)
    mathPracticeTrials.addData('mouse_2.leftButton', mouse_2.leftButton)
    mathPracticeTrials.addData('mouse_2.midButton', mouse_2.midButton)
    mathPracticeTrials.addData('mouse_2.rightButton', mouse_2.rightButton)
    mathPracticeTrials.addData('mouse_2.time', mouse_2.time)
    mathPracticeTrials.addData('mouse_2.clicked_name', mouse_2.clicked_name)
    # the Routine "TF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mathPracticeTrials'


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
