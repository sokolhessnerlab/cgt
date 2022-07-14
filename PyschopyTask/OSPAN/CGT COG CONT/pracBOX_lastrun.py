#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed Jul 13 22:02:05 2022
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
expName = 'pracBOX'  # from the Builder filename that created this script
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
    originPath='/Users/annarini/Downloads/CGT COG CONT/pracBOX_lastrun.py',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
PBox = visual.Rect(
    win=win, name='PBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(-0.25,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
NBox = visual.Rect(
    win=win, name='NBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
SBox = visual.Rect(
    win=win, name='SBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
KBox = visual.Rect(
    win=win, name='KBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
HBox = visual.Rect(
    win=win, name='HBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0.25,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
FBox = visual.Rect(
    win=win, name='FBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
QBox = visual.Rect(
    win=win, name='QBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
LBox = visual.Rect(
    win=win, name='LBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(-.25, -0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
RBox = visual.Rect(
    win=win, name='RBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0.25,-0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
TBox = visual.Rect(
    win=win, name='TBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0.25,-0.30), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
YBox = visual.Rect(
    win=win, name='YBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(0.0, -0.30), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
JBox = visual.Rect(
    win=win, name='JBox',
    width=(0.10, 0.10)[0], height=(0.10, 0.10)[1],
    ori=0.0, pos=(-0.25,-0.30), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
clicked_things = []
RecallINS = visual.TextStim(win=win, name='RecallINS',
    text='Select the letters in the order presented but pressing the corresponding keys on your keyboard. Use the space button to fill in forgotten letters.',
    font='Open Sans',
    pos=(0, .30), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
P = visual.TextStim(win=win, name='P',
    text='P',
    font='Open Sans',
    pos=(-.25,0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
F = visual.TextStim(win=win, name='F',
    text='F',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
H = visual.TextStim(win=win, name='H',
    text='H',
    font='Open Sans',
    pos=(0.25, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
S = visual.TextStim(win=win, name='S',
    text='S',
    font='Open Sans',
    pos=(-0.25,0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
K = visual.TextStim(win=win, name='K',
    text='K',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
N = visual.TextStim(win=win, name='N',
    text='N',
    font='Open Sans',
    pos=(0.25, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
L = visual.TextStim(win=win, name='L',
    text='L',
    font='Open Sans',
    pos=(-0.25, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
Q = visual.TextStim(win=win, name='Q',
    text='Q',
    font='Open Sans',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
R = visual.TextStim(win=win, name='R',
    text='R',
    font='Open Sans',
    pos=(0.25,-0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
J = visual.TextStim(win=win, name='J',
    text='J',
    font='Open Sans',
    pos=(-.25, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
Y = visual.TextStim(win=win, name='Y',
    text='Y',
    font='Open Sans',
    pos=(0,-0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
T = visual.TextStim(win=win, name='T',
    text='T',
    font='Open Sans',
    pos=(0.25, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
clicked_thinks = [] 


waiting = False
# keep track of which components have finished
trialComponents = [PBox, NBox, SBox, KBox, HBox, FBox, QBox, LBox, RBox, TBox, YBox, JBox, mouse, RecallINS, P, F, H, S, K, N, L, Q, R, J, Y, T]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
        PBox.setAutoDraw(True)
    
    # *NBox* updates
    if NBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NBox.frameNStart = frameN  # exact frame index
        NBox.tStart = t  # local t and not account for scr refresh
        NBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NBox, 'tStartRefresh')  # time at next scr refresh
        NBox.setAutoDraw(True)
    
    # *SBox* updates
    if SBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SBox.frameNStart = frameN  # exact frame index
        SBox.tStart = t  # local t and not account for scr refresh
        SBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SBox, 'tStartRefresh')  # time at next scr refresh
        SBox.setAutoDraw(True)
    
    # *KBox* updates
    if KBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KBox.frameNStart = frameN  # exact frame index
        KBox.tStart = t  # local t and not account for scr refresh
        KBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KBox, 'tStartRefresh')  # time at next scr refresh
        KBox.setAutoDraw(True)
    
    # *HBox* updates
    if HBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HBox.frameNStart = frameN  # exact frame index
        HBox.tStart = t  # local t and not account for scr refresh
        HBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HBox, 'tStartRefresh')  # time at next scr refresh
        HBox.setAutoDraw(True)
    
    # *FBox* updates
    if FBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FBox.frameNStart = frameN  # exact frame index
        FBox.tStart = t  # local t and not account for scr refresh
        FBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FBox, 'tStartRefresh')  # time at next scr refresh
        FBox.setAutoDraw(True)
    
    # *QBox* updates
    if QBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        QBox.frameNStart = frameN  # exact frame index
        QBox.tStart = t  # local t and not account for scr refresh
        QBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(QBox, 'tStartRefresh')  # time at next scr refresh
        QBox.setAutoDraw(True)
    
    # *LBox* updates
    if LBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LBox.frameNStart = frameN  # exact frame index
        LBox.tStart = t  # local t and not account for scr refresh
        LBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LBox, 'tStartRefresh')  # time at next scr refresh
        LBox.setAutoDraw(True)
    
    # *RBox* updates
    if RBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RBox.frameNStart = frameN  # exact frame index
        RBox.tStart = t  # local t and not account for scr refresh
        RBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RBox, 'tStartRefresh')  # time at next scr refresh
        RBox.setAutoDraw(True)
    
    # *TBox* updates
    if TBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TBox.frameNStart = frameN  # exact frame index
        TBox.tStart = t  # local t and not account for scr refresh
        TBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TBox, 'tStartRefresh')  # time at next scr refresh
        TBox.setAutoDraw(True)
    
    # *YBox* updates
    if YBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YBox.frameNStart = frameN  # exact frame index
        YBox.tStart = t  # local t and not account for scr refresh
        YBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YBox, 'tStartRefresh')  # time at next scr refresh
        YBox.setAutoDraw(True)
    
    # *JBox* updates
    if JBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        JBox.frameNStart = frameN  # exact frame index
        JBox.tStart = t  # local t and not account for scr refresh
        JBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(JBox, 'tStartRefresh')  # time at next scr refresh
        JBox.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    clickables = [FBox, KBox, PBox, SBox, HBox, LBox, QBox, TBox, JBox, NBox, RBox, YBox]
    
    #check if the mouse is pressed in any of the boxes
    for clickable in clickables: 
        if mouse.isPressedIn(clickable):
            clicked_things.append(clickable.name)
            
    #change box to blue if clicked 
    clickedN = 0 
    for clickable in clickables: 
        if clickable.name in clicked_things: 
            clickable.color = 'blue' 
            clickedN += 1
            
    if clickedN == 3 and not waiting: 
        waiting = True
        startTime = t 
      
    if clickedN == 3 and not waiting: 
        if t > startTime + 0.05: 
            continueRoutine = False 
       
    
    # *RecallINS* updates
    if RecallINS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RecallINS.frameNStart = frameN  # exact frame index
        RecallINS.tStart = t  # local t and not account for scr refresh
        RecallINS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RecallINS, 'tStartRefresh')  # time at next scr refresh
        RecallINS.setAutoDraw(True)
    
    # *P* updates
    if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P.frameNStart = frameN  # exact frame index
        P.tStart = t  # local t and not account for scr refresh
        P.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
        P.setAutoDraw(True)
    
    # *F* updates
    if F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F.frameNStart = frameN  # exact frame index
        F.tStart = t  # local t and not account for scr refresh
        F.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F, 'tStartRefresh')  # time at next scr refresh
        F.setAutoDraw(True)
    
    # *H* updates
    if H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        H.frameNStart = frameN  # exact frame index
        H.tStart = t  # local t and not account for scr refresh
        H.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(H, 'tStartRefresh')  # time at next scr refresh
        H.setAutoDraw(True)
    
    # *S* updates
    if S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        S.frameNStart = frameN  # exact frame index
        S.tStart = t  # local t and not account for scr refresh
        S.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S, 'tStartRefresh')  # time at next scr refresh
        S.setAutoDraw(True)
    
    # *K* updates
    if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        K.frameNStart = frameN  # exact frame index
        K.tStart = t  # local t and not account for scr refresh
        K.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
        K.setAutoDraw(True)
    
    # *N* updates
    if N.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        N.frameNStart = frameN  # exact frame index
        N.tStart = t  # local t and not account for scr refresh
        N.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(N, 'tStartRefresh')  # time at next scr refresh
        N.setAutoDraw(True)
    
    # *L* updates
    if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L.frameNStart = frameN  # exact frame index
        L.tStart = t  # local t and not account for scr refresh
        L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
        L.setAutoDraw(True)
    
    # *Q* updates
    if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q.frameNStart = frameN  # exact frame index
        Q.tStart = t  # local t and not account for scr refresh
        Q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
        Q.setAutoDraw(True)
    
    # *R* updates
    if R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        R.frameNStart = frameN  # exact frame index
        R.tStart = t  # local t and not account for scr refresh
        R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R, 'tStartRefresh')  # time at next scr refresh
        R.setAutoDraw(True)
    
    # *J* updates
    if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        J.frameNStart = frameN  # exact frame index
        J.tStart = t  # local t and not account for scr refresh
        J.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
        J.setAutoDraw(True)
    
    # *Y* updates
    if Y.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Y.frameNStart = frameN  # exact frame index
        Y.tStart = t  # local t and not account for scr refresh
        Y.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Y, 'tStartRefresh')  # time at next scr refresh
        Y.setAutoDraw(True)
    
    # *T* updates
    if T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        T.frameNStart = frameN  # exact frame index
        T.tStart = t  # local t and not account for scr refresh
        T.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(T, 'tStartRefresh')  # time at next scr refresh
        T.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PBox.started', PBox.tStartRefresh)
thisExp.addData('PBox.stopped', PBox.tStopRefresh)
thisExp.addData('NBox.started', NBox.tStartRefresh)
thisExp.addData('NBox.stopped', NBox.tStopRefresh)
thisExp.addData('SBox.started', SBox.tStartRefresh)
thisExp.addData('SBox.stopped', SBox.tStopRefresh)
thisExp.addData('KBox.started', KBox.tStartRefresh)
thisExp.addData('KBox.stopped', KBox.tStopRefresh)
thisExp.addData('HBox.started', HBox.tStartRefresh)
thisExp.addData('HBox.stopped', HBox.tStopRefresh)
thisExp.addData('FBox.started', FBox.tStartRefresh)
thisExp.addData('FBox.stopped', FBox.tStopRefresh)
thisExp.addData('QBox.started', QBox.tStartRefresh)
thisExp.addData('QBox.stopped', QBox.tStopRefresh)
thisExp.addData('LBox.started', LBox.tStartRefresh)
thisExp.addData('LBox.stopped', LBox.tStopRefresh)
thisExp.addData('RBox.started', RBox.tStartRefresh)
thisExp.addData('RBox.stopped', RBox.tStopRefresh)
thisExp.addData('TBox.started', TBox.tStartRefresh)
thisExp.addData('TBox.stopped', TBox.tStopRefresh)
thisExp.addData('YBox.started', YBox.tStartRefresh)
thisExp.addData('YBox.stopped', YBox.tStopRefresh)
thisExp.addData('JBox.started', JBox.tStartRefresh)
thisExp.addData('JBox.stopped', JBox.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('RecallINS.started', RecallINS.tStartRefresh)
thisExp.addData('RecallINS.stopped', RecallINS.tStopRefresh)
thisExp.addData('P.started', P.tStartRefresh)
thisExp.addData('P.stopped', P.tStopRefresh)
thisExp.addData('F.started', F.tStartRefresh)
thisExp.addData('F.stopped', F.tStopRefresh)
thisExp.addData('H.started', H.tStartRefresh)
thisExp.addData('H.stopped', H.tStopRefresh)
thisExp.addData('S.started', S.tStartRefresh)
thisExp.addData('S.stopped', S.tStopRefresh)
thisExp.addData('K.started', K.tStartRefresh)
thisExp.addData('K.stopped', K.tStopRefresh)
thisExp.addData('N.started', N.tStartRefresh)
thisExp.addData('N.stopped', N.tStopRefresh)
thisExp.addData('L.started', L.tStartRefresh)
thisExp.addData('L.stopped', L.tStopRefresh)
thisExp.addData('Q.started', Q.tStartRefresh)
thisExp.addData('Q.stopped', Q.tStopRefresh)
thisExp.addData('R.started', R.tStartRefresh)
thisExp.addData('R.stopped', R.tStopRefresh)
thisExp.addData('J.started', J.tStartRefresh)
thisExp.addData('J.stopped', J.tStopRefresh)
thisExp.addData('Y.started', Y.tStartRefresh)
thisExp.addData('Y.stopped', Y.tStopRefresh)
thisExp.addData('T.started', T.tStartRefresh)
thisExp.addData('T.stopped', T.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
