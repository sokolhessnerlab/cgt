#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Sun Jul 31 19:04:29 2022
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
expName = 'CGTriskyDMtask'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/shlab/Documents/GitHub/cgt/PyschopyTask/riskyDM/CGTbothTasks_lastrun.py',
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
    size=[1024, 576], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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

# --- Initialize components for Routine "instructions" ---

# --- Initialize components for Routine "pracStart" ---

# --- Initialize components for Routine "practiceTask" ---

# --- Initialize components for Routine "isiPrac" ---

# --- Initialize components for Routine "feedback" ---

# --- Initialize components for Routine "itiPrac_2" ---

# --- Initialize components for Routine "postPrac" ---

# --- Initialize components for Routine "choiceWindow" ---

# --- Initialize components for Routine "isi" ---

# --- Initialize components for Routine "showOutcome" ---

# --- Initialize components for Routine "iti" ---

# --- Initialize components for Routine "computeEstimates" ---

# --- Initialize components for Routine "choiceWindow" ---

# --- Initialize components for Routine "isi" ---

# --- Initialize components for Routine "showOutcome" ---

# --- Initialize components for Routine "iti" ---

# --- Initialize components for Routine "selectOutcome" ---

# --- Initialize components for Routine "rdmToSpanTransition" ---
breaktxt = visual.TextStim(win=win, name='breaktxt',
    text='You have sucessfully completed the first task in this experiment!\n\nPlease take a brief break. The option to continue will appear on the screen in about 30 seconds, if you feel ready to move on, click the continue button. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
BreakEndMouse = event.Mouse(win=win)
x, y = [None, None]
BreakEndMouse.mouseClock = core.Clock()
cont_buttonBreak = visual.ImageStim(
    win=win,
    name='cont_buttonBreak', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "SpanGeneralInstructions" ---
GenInsText = visual.TextStim(win=win, name='GenInsText',
    text='In this task you will be asked to memorize a series of numbers and recall them. You will do this twice, once recalling the numbers as they are presented on the screen and once recalling the numbers in the reverse order presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. Click the continue button when you are ready. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
cont_buttonGEN = visual.ImageStim(
    win=win,
    name='cont_buttonGEN', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "FSInstructions" ---
FSGenInsText = visual.TextStim(win=win, name='FSGenInsText',
    text='You are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall two out of three lists you will proceed to longer list trials. \n\nType out your answer when "Recall" screen appears using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nIf you make a mistake you can use backspace to correct it.  Do not use spaces. Feedback will be provided.\n\nClick the continue button to begin a few practice trials.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
FSMouse = event.Mouse(win=win)
x, y = [None, None]
FSMouse.mouseClock = core.Clock()
cont_buttonFSIns = visual.ImageStim(
    win=win,
    name='cont_buttonFSIns', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "ShowNumbersPractice" ---
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_practice = visual.TextStim(win=win, name='pres_text_practice',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "RecallPractice" ---
recall_txtPractice = visual.TextStim(win=win, name='recall_txtPractice',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice',
     autoLog=True,
)
cont_buttonPractice = visual.ImageStim(
    win=win,
    name='cont_buttonPractice', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice = event.Mouse(win=win)
x, y = [None, None]
mousePractice.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackPractice" ---
feedbac_textPractice = visual.TextStim(win=win, name='feedbac_textPractice',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "StartRealFS" ---
praccomplete = visual.TextStim(win=win, name='praccomplete',
    text='Practice complete. \n\nWhen you are ready to start the real task, click the continue button.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cont_buttonFSReal = visual.ImageStim(
    win=win,
    name='cont_buttonFSReal', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "selectNumbers" ---
# Run 'Begin Experiment' code from selectNumbersFS
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitFS = 3;
maxDigitFS = 16;
#minDigitBS = 2;
#maxDigitBS = 15;
nTrialsFS = 0;
#nTrialsBS = 0;
correct = [];
incorrectCount = 0;


# --- Initialize components for Routine "ShowNumbers" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_text = visual.TextStim(win=win, name='presentation_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall" ---
recall_txt = visual.TextStim(win=win, name='recall_txt',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
cont_button = visual.ImageStim(
    win=win,
    name='cont_button', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "InstructionsBS" ---
BSGenInsText = visual.TextStim(win=win, name='BSGenInsText',
    text='You are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall two out of three lists you will proceed to longer list trials. \n\nType out your answer when the "Recall" screen appears using the numbers at the top of the keyboard making sure to type out the answers in the REVERSE order than they are presented on the screen. For example if you see 3,2,1 you should answer 1,2,3. \n\nIf you make a mistake you can use backspace to correct it. Do not use spaces. Feedback will be provided.\n\nClick the continue button to begin a few practice trials.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
BSMouse = event.Mouse(win=win)
x, y = [None, None]
BSMouse.mouseClock = core.Clock()
cont_buttonBSIns = visual.ImageStim(
    win=win,
    name='cont_buttonBSIns', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "showNumbersPracticeBS" ---
fixation_3 = visual.TextStim(win=win, name='fixation_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_practice_2 = visual.TextStim(win=win, name='pres_text_practice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recallPracticeBS" ---
recall_txtPractice_2 = visual.TextStim(win=win, name='recall_txtPractice_2',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice_2',
     autoLog=True,
)
cont_buttonPractice_2 = visual.ImageStim(
    win=win,
    name='cont_buttonPractice_2', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice_2 = event.Mouse(win=win)
x, y = [None, None]
mousePractice_2.mouseClock = core.Clock()

# --- Initialize components for Routine "feedbackPracticeBS" ---
feedbac_textPractice_2 = visual.TextStim(win=win, name='feedbac_textPractice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "startRealBS" ---
praccompleteBS = visual.TextStim(win=win, name='praccompleteBS',
    text='Practice complete. \n\nWhen you are ready to start the real task, click the continue button.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cont_buttonBSReal = visual.ImageStim(
    win=win,
    name='cont_buttonBSReal', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# --- Initialize components for Routine "selectNumbersBS" ---
# Run 'Begin Experiment' code from selectNumbersBScode
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitBS = 2;
maxDigitBS = 15;
nTrialsBS = 0;
correct = [];
incorrectCount = 0;

# --- Initialize components for Routine "showNumbersBS" ---
fixationBS = visual.TextStim(win=win, name='fixationBS',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_textBS = visual.TextStim(win=win, name='presentation_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "RecallBS" ---
recall_txtBS = visual.TextStim(win=win, name='recall_txtBS',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxBS = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxBS',
     autoLog=True,
)
cont_buttonBS = visual.ImageStim(
    win=win,
    name='cont_buttonBS', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouseBS = event.Mouse(win=win)
x, y = [None, None]
mouseBS.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackBS" ---
feedback_textBS = visual.TextStim(win=win, name='feedback_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this experiment. \n\nYou will now be automatically redirected to Qualtrics to take a breif end of task survey. ',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructionsComponents = []
for thisComponent in instructionsComponents:
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

# --- Run Routine "instructions" ---
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
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pracStart" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
pracStartComponents = []
for thisComponent in pracStartComponents:
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

# --- Run Routine "pracStart" ---
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
    for thisComponent in pracStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pracStart" ---
for thisComponent in pracStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgtPractice.xlsx'),
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
    
    # --- Prepare to start Routine "practiceTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    practiceTaskComponents = []
    for thisComponent in practiceTaskComponents:
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
    
    # --- Run Routine "practiceTask" ---
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
        for thisComponent in practiceTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceTask" ---
    for thisComponent in practiceTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "isiPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiPracComponents = []
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
    # the Routine "isiPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = []
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "itiPrac_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiPrac_2Components = []
    for thisComponent in itiPrac_2Components:
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
    
    # --- Run Routine "itiPrac_2" ---
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
        for thisComponent in itiPrac_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "itiPrac_2" ---
    for thisComponent in itiPrac_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "itiPrac_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials'


# --- Prepare to start Routine "postPrac" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
postPracComponents = []
for thisComponent in postPracComponents:
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

# --- Run Routine "postPrac" ---
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
    for thisComponent in postPracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postPrac" ---
for thisComponent in postPracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "postPrac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
staticRDM = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CGT-choice-set.csv'),
    seed=None, name='staticRDM')
thisExp.addLoop(staticRDM)  # add the loop to the experiment
thisStaticRDM = staticRDM.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStaticRDM.rgb)
if thisStaticRDM != None:
    for paramName in thisStaticRDM:
        exec('{} = thisStaticRDM[paramName]'.format(paramName))

for thisStaticRDM in staticRDM:
    currentLoop = staticRDM
    # abbreviate parameter names if possible (e.g. rgb = thisStaticRDM.rgb)
    if thisStaticRDM != None:
        for paramName in thisStaticRDM:
            exec('{} = thisStaticRDM[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "choiceWindow" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    choiceWindowComponents = []
    for thisComponent in choiceWindowComponents:
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
    
    # --- Run Routine "choiceWindow" ---
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
        for thisComponent in choiceWindowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choiceWindow" ---
    for thisComponent in choiceWindowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "choiceWindow" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = []
    for thisComponent in isiComponents:
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
    
    # --- Run Routine "isi" ---
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
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isi" ---
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    showOutcomeComponents = []
    for thisComponent in showOutcomeComponents:
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
    
    # --- Run Routine "showOutcome" ---
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
        for thisComponent in showOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "showOutcome" ---
    for thisComponent in showOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "showOutcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiComponents = []
    for thisComponent in itiComponents:
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
    
    # --- Run Routine "iti" ---
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
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iti" ---
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'staticRDM'


# --- Prepare to start Routine "computeEstimates" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
computeEstimatesComponents = []
for thisComponent in computeEstimatesComponents:
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

# --- Run Routine "computeEstimates" ---
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
    for thisComponent in computeEstimatesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "computeEstimates" ---
for thisComponent in computeEstimatesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "computeEstimates" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
dynamicRDM = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='dynamicRDM')
thisExp.addLoop(dynamicRDM)  # add the loop to the experiment
thisDynamicRDM = dynamicRDM.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDynamicRDM.rgb)
if thisDynamicRDM != None:
    for paramName in thisDynamicRDM:
        exec('{} = thisDynamicRDM[paramName]'.format(paramName))

for thisDynamicRDM in dynamicRDM:
    currentLoop = dynamicRDM
    # abbreviate parameter names if possible (e.g. rgb = thisDynamicRDM.rgb)
    if thisDynamicRDM != None:
        for paramName in thisDynamicRDM:
            exec('{} = thisDynamicRDM[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "choiceWindow" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    choiceWindowComponents = []
    for thisComponent in choiceWindowComponents:
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
    
    # --- Run Routine "choiceWindow" ---
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
        for thisComponent in choiceWindowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choiceWindow" ---
    for thisComponent in choiceWindowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "choiceWindow" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = []
    for thisComponent in isiComponents:
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
    
    # --- Run Routine "isi" ---
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
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isi" ---
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    showOutcomeComponents = []
    for thisComponent in showOutcomeComponents:
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
    
    # --- Run Routine "showOutcome" ---
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
        for thisComponent in showOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "showOutcome" ---
    for thisComponent in showOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "showOutcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiComponents = []
    for thisComponent in itiComponents:
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
    
    # --- Run Routine "iti" ---
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
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iti" ---
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'dynamicRDM'


# --- Prepare to start Routine "selectOutcome" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
selectOutcomeComponents = []
for thisComponent in selectOutcomeComponents:
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

# --- Run Routine "selectOutcome" ---
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
    for thisComponent in selectOutcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "selectOutcome" ---
for thisComponent in selectOutcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "selectOutcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "rdmToSpanTransition" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the BreakEndMouse
BreakEndMouse.x = []
BreakEndMouse.y = []
BreakEndMouse.leftButton = []
BreakEndMouse.midButton = []
BreakEndMouse.rightButton = []
BreakEndMouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
rdmToSpanTransitionComponents = [breaktxt, BreakEndMouse, cont_buttonBreak]
for thisComponent in rdmToSpanTransitionComponents:
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

# --- Run Routine "rdmToSpanTransition" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breaktxt* updates
    if breaktxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breaktxt.frameNStart = frameN  # exact frame index
        breaktxt.tStart = t  # local t and not account for scr refresh
        breaktxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breaktxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'breaktxt.started')
        breaktxt.setAutoDraw(True)
    # *BreakEndMouse* updates
    if BreakEndMouse.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        BreakEndMouse.frameNStart = frameN  # exact frame index
        BreakEndMouse.tStart = t  # local t and not account for scr refresh
        BreakEndMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BreakEndMouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('BreakEndMouse.started', t)
        BreakEndMouse.status = STARTED
        BreakEndMouse.mouseClock.reset()
        prevButtonState = BreakEndMouse.getPressed()  # if button is down already this ISN'T a new click
    if BreakEndMouse.status == STARTED:  # only update if started and not finished!
        buttons = BreakEndMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = BreakEndMouse.getPos()
                BreakEndMouse.x.append(x)
                BreakEndMouse.y.append(y)
                buttons = BreakEndMouse.getPressed()
                BreakEndMouse.leftButton.append(buttons[0])
                BreakEndMouse.midButton.append(buttons[1])
                BreakEndMouse.rightButton.append(buttons[2])
                BreakEndMouse.time.append(BreakEndMouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # *cont_buttonBreak* updates
    if cont_buttonBreak.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonBreak.frameNStart = frameN  # exact frame index
        cont_buttonBreak.tStart = t  # local t and not account for scr refresh
        cont_buttonBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonBreak, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonBreak.started')
        cont_buttonBreak.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rdmToSpanTransitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rdmToSpanTransition" ---
for thisComponent in rdmToSpanTransitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('BreakEndMouse.x', BreakEndMouse.x)
thisExp.addData('BreakEndMouse.y', BreakEndMouse.y)
thisExp.addData('BreakEndMouse.leftButton', BreakEndMouse.leftButton)
thisExp.addData('BreakEndMouse.midButton', BreakEndMouse.midButton)
thisExp.addData('BreakEndMouse.rightButton', BreakEndMouse.rightButton)
thisExp.addData('BreakEndMouse.time', BreakEndMouse.time)
thisExp.nextEntry()
# the Routine "rdmToSpanTransition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "SpanGeneralInstructions" ---
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
SpanGeneralInstructionsComponents = [GenInsText, mouse_2, cont_buttonGEN]
for thisComponent in SpanGeneralInstructionsComponents:
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

# --- Run Routine "SpanGeneralInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GenInsText* updates
    if GenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GenInsText.frameNStart = frameN  # exact frame index
        GenInsText.tStart = t  # local t and not account for scr refresh
        GenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GenInsText.started')
        GenInsText.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0-frameTolerance:
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
                    iter(cont_buttonGEN)
                    clickableList = cont_buttonGEN
                except:
                    clickableList = [cont_buttonGEN]
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
    
    # *cont_buttonGEN* updates
    if cont_buttonGEN.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonGEN.frameNStart = frameN  # exact frame index
        cont_buttonGEN.tStart = t  # local t and not account for scr refresh
        cont_buttonGEN.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonGEN, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonGEN.started')
        cont_buttonGEN.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SpanGeneralInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SpanGeneralInstructions" ---
for thisComponent in SpanGeneralInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
thisExp.nextEntry()
# the Routine "SpanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "FSInstructions" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the FSMouse
FSMouse.x = []
FSMouse.y = []
FSMouse.leftButton = []
FSMouse.midButton = []
FSMouse.rightButton = []
FSMouse.time = []
FSMouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
FSInstructionsComponents = [FSGenInsText, FSMouse, cont_buttonFSIns]
for thisComponent in FSInstructionsComponents:
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

# --- Run Routine "FSInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FSGenInsText* updates
    if FSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FSGenInsText.frameNStart = frameN  # exact frame index
        FSGenInsText.tStart = t  # local t and not account for scr refresh
        FSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FSGenInsText.started')
        FSGenInsText.setAutoDraw(True)
    # *FSMouse* updates
    if FSMouse.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        FSMouse.frameNStart = frameN  # exact frame index
        FSMouse.tStart = t  # local t and not account for scr refresh
        FSMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FSMouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('FSMouse.started', t)
        FSMouse.status = STARTED
        FSMouse.mouseClock.reset()
        prevButtonState = FSMouse.getPressed()  # if button is down already this ISN'T a new click
    if FSMouse.status == STARTED:  # only update if started and not finished!
        buttons = FSMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(cont_buttonFSIns)
                    clickableList = cont_buttonFSIns
                except:
                    clickableList = [cont_buttonFSIns]
                for obj in clickableList:
                    if obj.contains(FSMouse):
                        gotValidClick = True
                        FSMouse.clicked_name.append(obj.name)
                x, y = FSMouse.getPos()
                FSMouse.x.append(x)
                FSMouse.y.append(y)
                buttons = FSMouse.getPressed()
                FSMouse.leftButton.append(buttons[0])
                FSMouse.midButton.append(buttons[1])
                FSMouse.rightButton.append(buttons[2])
                FSMouse.time.append(FSMouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *cont_buttonFSIns* updates
    if cont_buttonFSIns.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonFSIns.frameNStart = frameN  # exact frame index
        cont_buttonFSIns.tStart = t  # local t and not account for scr refresh
        cont_buttonFSIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonFSIns, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonFSIns.started')
        cont_buttonFSIns.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FSInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "FSInstructions" ---
for thisComponent in FSInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('FSMouse.x', FSMouse.x)
thisExp.addData('FSMouse.y', FSMouse.y)
thisExp.addData('FSMouse.leftButton', FSMouse.leftButton)
thisExp.addData('FSMouse.midButton', FSMouse.midButton)
thisExp.addData('FSMouse.rightButton', FSMouse.rightButton)
thisExp.addData('FSMouse.time', FSMouse.time)
thisExp.addData('FSMouse.clicked_name', FSMouse.clicked_name)
thisExp.nextEntry()
# the Routine "FSInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TrialFSPractice = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='TrialFSPractice')
thisExp.addLoop(TrialFSPractice)  # add the loop to the experiment
thisTrialFSPractice = TrialFSPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
if thisTrialFSPractice != None:
    for paramName in thisTrialFSPractice:
        exec('{} = thisTrialFSPractice[paramName]'.format(paramName))

for thisTrialFSPractice in TrialFSPractice:
    currentLoop = TrialFSPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
    if thisTrialFSPractice != None:
        for paramName in thisTrialFSPractice:
            exec('{} = thisTrialFSPractice[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    DigitLoopPractice = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DigitLoopPractice')
    thisExp.addLoop(DigitLoopPractice)  # add the loop to the experiment
    thisDigitLoopPractice = DigitLoopPractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
    if thisDigitLoopPractice != None:
        for paramName in thisDigitLoopPractice:
            exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
    
    for thisDigitLoopPractice in DigitLoopPractice:
        currentLoop = DigitLoopPractice
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
        if thisDigitLoopPractice != None:
            for paramName in thisDigitLoopPractice:
                exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbersPractice" ---
        continueRoutine = True
        # update component parameters for each repeat
        pres_text_practice.setText(str(digits)[DigitLoopPractice.thisN])
        # keep track of which components have finished
        ShowNumbersPracticeComponents = [fixation_2, pres_text_practice]
        for thisComponent in ShowNumbersPracticeComponents:
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
        
        # --- Run Routine "ShowNumbersPractice" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    fixation_2.setAutoDraw(False)
            
            # *pres_text_practice* updates
            if pres_text_practice.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice.frameNStart = frameN  # exact frame index
                pres_text_practice.tStart = t  # local t and not account for scr refresh
                pres_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice.started')
                pres_text_practice.setAutoDraw(True)
            if pres_text_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice.tStop = t  # not accounting for scr refresh
                    pres_text_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice.stopped')
                    pres_text_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbersPractice" ---
        for thisComponent in ShowNumbersPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'DigitLoopPractice'
    
    
    # --- Prepare to start Routine "RecallPractice" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxPractice.reset()
    # setup some python lists for storing info about the mousePractice
    mousePractice.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallPracticeComponents = [recall_txtPractice, textboxPractice, cont_buttonPractice, mousePractice]
    for thisComponent in RecallPracticeComponents:
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
    
    # --- Run Routine "RecallPractice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice* updates
        if recall_txtPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice.frameNStart = frameN  # exact frame index
            recall_txtPractice.tStart = t  # local t and not account for scr refresh
            recall_txtPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice.started')
            recall_txtPractice.setAutoDraw(True)
        
        # *textboxPractice* updates
        if textboxPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice.frameNStart = frameN  # exact frame index
            textboxPractice.tStart = t  # local t and not account for scr refresh
            textboxPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice.started')
            textboxPractice.setAutoDraw(True)
        
        # *cont_buttonPractice* updates
        if cont_buttonPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice.frameNStart = frameN  # exact frame index
            cont_buttonPractice.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice.started')
            cont_buttonPractice.setAutoDraw(True)
        # *mousePractice* updates
        if mousePractice.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice.frameNStart = frameN  # exact frame index
            mousePractice.tStart = t  # local t and not account for scr refresh
            mousePractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice.started', t)
            mousePractice.status = STARTED
            mousePractice.mouseClock.reset()
            prevButtonState = mousePractice.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice)
                        clickableList = cont_buttonPractice
                    except:
                        clickableList = [cont_buttonPractice]
                    for obj in clickableList:
                        if obj.contains(mousePractice):
                            gotValidClick = True
                            mousePractice.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallPractice" ---
    for thisComponent in RecallPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TrialFSPractice.addData('textboxPractice.text',textboxPractice.text)
    # Run 'End Routine' code from code_3practice
    #for r in range(len(digitsForTrial)):
    #    digitsForTrial[r] = str(digitsForTrial[r])
    
    #digitsForTrial = ''.join(digitsForTrial)
    
    if textboxPractice.text == str(digits):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for TrialFSPractice (TrialHandler)
    x, y = mousePractice.getPos()
    buttons = mousePractice.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice)
            clickableList = cont_buttonPractice
        except:
            clickableList = [cont_buttonPractice]
        for obj in clickableList:
            if obj.contains(mousePractice):
                gotValidClick = True
                mousePractice.clicked_name.append(obj.name)
    TrialFSPractice.addData('mousePractice.x', x)
    TrialFSPractice.addData('mousePractice.y', y)
    TrialFSPractice.addData('mousePractice.leftButton', buttons[0])
    TrialFSPractice.addData('mousePractice.midButton', buttons[1])
    TrialFSPractice.addData('mousePractice.rightButton', buttons[2])
    if len(mousePractice.clicked_name):
        TrialFSPractice.addData('mousePractice.clicked_name', mousePractice.clicked_name[0])
    # the Routine "RecallPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackPractice" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedbac_textPractice.setText(fbTxt)
    # keep track of which components have finished
    FeedbackPracticeComponents = [feedbac_textPractice]
    for thisComponent in FeedbackPracticeComponents:
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
    
    # --- Run Routine "FeedbackPractice" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice* updates
        if feedbac_textPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice.frameNStart = frameN  # exact frame index
            feedbac_textPractice.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice.started')
            feedbac_textPractice.setAutoDraw(True)
        if feedbac_textPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice.tStop = t  # not accounting for scr refresh
                feedbac_textPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice.stopped')
                feedbac_textPractice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackPractice" ---
    for thisComponent in FeedbackPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'TrialFSPractice'


# --- Prepare to start Routine "StartRealFS" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.x = []
mouse_5.y = []
mouse_5.leftButton = []
mouse_5.midButton = []
mouse_5.rightButton = []
mouse_5.time = []
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
StartRealFSComponents = [praccomplete, cont_buttonFSReal, mouse_5]
for thisComponent in StartRealFSComponents:
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

# --- Run Routine "StartRealFS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccomplete* updates
    if praccomplete.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccomplete.frameNStart = frameN  # exact frame index
        praccomplete.tStart = t  # local t and not account for scr refresh
        praccomplete.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccomplete, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccomplete.started')
        praccomplete.setAutoDraw(True)
    
    # *cont_buttonFSReal* updates
    if cont_buttonFSReal.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonFSReal.frameNStart = frameN  # exact frame index
        cont_buttonFSReal.tStart = t  # local t and not account for scr refresh
        cont_buttonFSReal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonFSReal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonFSReal.started')
        cont_buttonFSReal.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_5.started', t)
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(cont_buttonFSReal)
                    clickableList = cont_buttonFSReal
                except:
                    clickableList = [cont_buttonFSReal]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                x, y = mouse_5.getPos()
                mouse_5.x.append(x)
                mouse_5.y.append(y)
                buttons = mouse_5.getPressed()
                mouse_5.leftButton.append(buttons[0])
                mouse_5.midButton.append(buttons[1])
                mouse_5.rightButton.append(buttons[2])
                mouse_5.time.append(mouse_5.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartRealFSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StartRealFS" ---
for thisComponent in StartRealFSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.x', mouse_5.x)
thisExp.addData('mouse_5.y', mouse_5.y)
thisExp.addData('mouse_5.leftButton', mouse_5.leftButton)
thisExp.addData('mouse_5.midButton', mouse_5.midButton)
thisExp.addData('mouse_5.rightButton', mouse_5.rightButton)
thisExp.addData('mouse_5.time', mouse_5.time)
thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name)
thisExp.nextEntry()
# the Routine "StartRealFS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber copy.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbers" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersFS
    import random
    
    nTrialsFS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsFS ==1:
        digitSpan = minDigitFS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitFS:
        digitSpan = minDigitFS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersComponents = []
    for thisComponent in selectNumbersComponents:
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
    
    # --- Run Routine "selectNumbers" ---
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
        for thisComponent in selectNumbersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbers" ---
    for thisComponent in selectNumbersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoop = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoop')
    thisExp.addLoop(digitLoop)  # add the loop to the experiment
    thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
    if thisDigitLoop != None:
        for paramName in thisDigitLoop:
            exec('{} = thisDigitLoop[paramName]'.format(paramName))
    
    for thisDigitLoop in digitLoop:
        currentLoop = digitLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                exec('{} = thisDigitLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbers" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeFS
        tmpNumber = digitsForTrial[digitLoop.thisN]
        presentation_text.setText(tmpNumber)
        # keep track of which components have finished
        ShowNumbersComponents = [fixation, presentation_text]
        for thisComponent in ShowNumbersComponents:
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
        
        # --- Run Routine "ShowNumbers" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *presentation_text* updates
            if presentation_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_text.frameNStart = frameN  # exact frame index
                presentation_text.tStart = t  # local t and not account for scr refresh
                presentation_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_text.started')
                presentation_text.setAutoDraw(True)
            if presentation_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_text.tStop = t  # not accounting for scr refresh
                    presentation_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_text.stopped')
                    presentation_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbers" ---
        for thisComponent in ShowNumbersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeFS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoop'
    
    
    # --- Prepare to start Routine "Recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallComponents = [recall_txt, textbox, cont_button, mouse_3]
    for thisComponent in RecallComponents:
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
    
    # --- Run Routine "Recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txt* updates
        if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txt.frameNStart = frameN  # exact frame index
            recall_txt.tStart = t  # local t and not account for scr refresh
            recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txt.started')
            recall_txt.setAutoDraw(True)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            textbox.setAutoDraw(True)
        
        # *cont_button* updates
        if cont_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_button.frameNStart = frameN  # exact frame index
            cont_button.tStart = t  # local t and not account for scr refresh
            cont_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_button.started')
            cont_button.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_button)
                        clickableList = cont_button
                    except:
                        clickableList = [cont_button]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall" ---
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('textbox.text',textbox.text)
    # Run 'End Routine' code from code_3
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textbox.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trials2 (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_button)
            clickableList = cont_button
        except:
            clickableList = [cont_button]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    trials2.addData('mouse_3.x', x)
    trials2.addData('mouse_3.y', y)
    trials2.addData('mouse_3.leftButton', buttons[0])
    trials2.addData('mouse_3.midButton', buttons[1])
    trials2.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        trials2.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback_text.setText(fbTxt)
    # keep track of which components have finished
    FeedbackComponents = [feedback_text]
    for thisComponent in FeedbackComponents:
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
    
    # --- Run Routine "Feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials2'


# --- Prepare to start Routine "InstructionsBS" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the BSMouse
BSMouse.x = []
BSMouse.y = []
BSMouse.leftButton = []
BSMouse.midButton = []
BSMouse.rightButton = []
BSMouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsBSComponents = [BSGenInsText, BSMouse, cont_buttonBSIns]
for thisComponent in InstructionsBSComponents:
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

# --- Run Routine "InstructionsBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BSGenInsText* updates
    if BSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSGenInsText.frameNStart = frameN  # exact frame index
        BSGenInsText.tStart = t  # local t and not account for scr refresh
        BSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BSGenInsText.started')
        BSGenInsText.setAutoDraw(True)
    # *BSMouse* updates
    if BSMouse.status == NOT_STARTED and t >= 5-frameTolerance:
        # keep track of start time/frame for later
        BSMouse.frameNStart = frameN  # exact frame index
        BSMouse.tStart = t  # local t and not account for scr refresh
        BSMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSMouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('BSMouse.started', t)
        BSMouse.status = STARTED
        BSMouse.mouseClock.reset()
        prevButtonState = BSMouse.getPressed()  # if button is down already this ISN'T a new click
    if BSMouse.status == STARTED:  # only update if started and not finished!
        buttons = BSMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = BSMouse.getPos()
                BSMouse.x.append(x)
                BSMouse.y.append(y)
                buttons = BSMouse.getPressed()
                BSMouse.leftButton.append(buttons[0])
                BSMouse.midButton.append(buttons[1])
                BSMouse.rightButton.append(buttons[2])
                BSMouse.time.append(BSMouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # *cont_buttonBSIns* updates
    if cont_buttonBSIns.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonBSIns.frameNStart = frameN  # exact frame index
        cont_buttonBSIns.tStart = t  # local t and not account for scr refresh
        cont_buttonBSIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonBSIns, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonBSIns.started')
        cont_buttonBSIns.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsBS" ---
for thisComponent in InstructionsBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('BSMouse.x', BSMouse.x)
thisExp.addData('BSMouse.y', BSMouse.y)
thisExp.addData('BSMouse.leftButton', BSMouse.leftButton)
thisExp.addData('BSMouse.midButton', BSMouse.midButton)
thisExp.addData('BSMouse.rightButton', BSMouse.rightButton)
thisExp.addData('BSMouse.time', BSMouse.time)
thisExp.nextEntry()
# the Routine "InstructionsBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsPracticeBS = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='trialsPracticeBS')
thisExp.addLoop(trialsPracticeBS)  # add the loop to the experiment
thisTrialsPracticeBS = trialsPracticeBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
if thisTrialsPracticeBS != None:
    for paramName in thisTrialsPracticeBS:
        exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))

for thisTrialsPracticeBS in trialsPracticeBS:
    currentLoop = trialsPracticeBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
    if thisTrialsPracticeBS != None:
        for paramName in thisTrialsPracticeBS:
            exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    digitLoopPracticeBS = data.TrialHandler(nReps=digitSpan, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopPracticeBS')
    thisExp.addLoop(digitLoopPracticeBS)  # add the loop to the experiment
    thisDigitLoopPracticeBS = digitLoopPracticeBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
    if thisDigitLoopPracticeBS != None:
        for paramName in thisDigitLoopPracticeBS:
            exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
    
    for thisDigitLoopPracticeBS in digitLoopPracticeBS:
        currentLoop = digitLoopPracticeBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
        if thisDigitLoopPracticeBS != None:
            for paramName in thisDigitLoopPracticeBS:
                exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersPracticeBS" ---
        continueRoutine = True
        # update component parameters for each repeat
        pres_text_practice_2.setText(str(digits)[digitLoopPracticeBS.thisN])
        # keep track of which components have finished
        showNumbersPracticeBSComponents = [fixation_3, pres_text_practice_2]
        for thisComponent in showNumbersPracticeBSComponents:
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
        
        # --- Run Routine "showNumbersPracticeBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_3* updates
            if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_3.frameNStart = frameN  # exact frame index
                fixation_3.tStart = t  # local t and not account for scr refresh
                fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.started')
                fixation_3.setAutoDraw(True)
            if fixation_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_3.tStop = t  # not accounting for scr refresh
                    fixation_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                    fixation_3.setAutoDraw(False)
            
            # *pres_text_practice_2* updates
            if pres_text_practice_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice_2.frameNStart = frameN  # exact frame index
                pres_text_practice_2.tStart = t  # local t and not account for scr refresh
                pres_text_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice_2.started')
                pres_text_practice_2.setAutoDraw(True)
            if pres_text_practice_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice_2.tStop = t  # not accounting for scr refresh
                    pres_text_practice_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice_2.stopped')
                    pres_text_practice_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersPracticeBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersPracticeBS" ---
        for thisComponent in showNumbersPracticeBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoopPracticeBS'
    
    
    # --- Prepare to start Routine "recallPracticeBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxPractice_2.reset()
    # setup some python lists for storing info about the mousePractice_2
    mousePractice_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallPracticeBSComponents = [recall_txtPractice_2, textboxPractice_2, cont_buttonPractice_2, mousePractice_2]
    for thisComponent in recallPracticeBSComponents:
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
    
    # --- Run Routine "recallPracticeBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice_2* updates
        if recall_txtPractice_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice_2.frameNStart = frameN  # exact frame index
            recall_txtPractice_2.tStart = t  # local t and not account for scr refresh
            recall_txtPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice_2.started')
            recall_txtPractice_2.setAutoDraw(True)
        
        # *textboxPractice_2* updates
        if textboxPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice_2.frameNStart = frameN  # exact frame index
            textboxPractice_2.tStart = t  # local t and not account for scr refresh
            textboxPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice_2.started')
            textboxPractice_2.setAutoDraw(True)
        
        # *cont_buttonPractice_2* updates
        if cont_buttonPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice_2.frameNStart = frameN  # exact frame index
            cont_buttonPractice_2.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice_2.started')
            cont_buttonPractice_2.setAutoDraw(True)
        # *mousePractice_2* updates
        if mousePractice_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice_2.frameNStart = frameN  # exact frame index
            mousePractice_2.tStart = t  # local t and not account for scr refresh
            mousePractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice_2.started', t)
            mousePractice_2.status = STARTED
            mousePractice_2.mouseClock.reset()
            prevButtonState = mousePractice_2.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice_2.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice_2)
                        clickableList = cont_buttonPractice_2
                    except:
                        clickableList = [cont_buttonPractice_2]
                    for obj in clickableList:
                        if obj.contains(mousePractice_2):
                            gotValidClick = True
                            mousePractice_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recallPracticeBS" ---
    for thisComponent in recallPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsPracticeBS.addData('textboxPractice_2.text',textboxPractice_2.text)
    # Run 'End Routine' code from code_3practice_2
    #for r in range(len(digitsForTrial)):
    #    digitsForTrial[r] = str(digitsForTrial[r])
    
    #digitsForTrial = ''.join(digitsForTrial)
    
    
    if textboxPractice_2.text == str(digitsReverse):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsPracticeBS (TrialHandler)
    x, y = mousePractice_2.getPos()
    buttons = mousePractice_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice_2)
            clickableList = cont_buttonPractice_2
        except:
            clickableList = [cont_buttonPractice_2]
        for obj in clickableList:
            if obj.contains(mousePractice_2):
                gotValidClick = True
                mousePractice_2.clicked_name.append(obj.name)
    trialsPracticeBS.addData('mousePractice_2.x', x)
    trialsPracticeBS.addData('mousePractice_2.y', y)
    trialsPracticeBS.addData('mousePractice_2.leftButton', buttons[0])
    trialsPracticeBS.addData('mousePractice_2.midButton', buttons[1])
    trialsPracticeBS.addData('mousePractice_2.rightButton', buttons[2])
    if len(mousePractice_2.clicked_name):
        trialsPracticeBS.addData('mousePractice_2.clicked_name', mousePractice_2.clicked_name[0])
    # the Routine "recallPracticeBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedbackPracticeBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedbac_textPractice_2.setText(fbTxt)
    # keep track of which components have finished
    feedbackPracticeBSComponents = [feedbac_textPractice_2]
    for thisComponent in feedbackPracticeBSComponents:
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
    
    # --- Run Routine "feedbackPracticeBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice_2* updates
        if feedbac_textPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice_2.frameNStart = frameN  # exact frame index
            feedbac_textPractice_2.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.started')
            feedbac_textPractice_2.setAutoDraw(True)
        if feedbac_textPractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice_2.tStop = t  # not accounting for scr refresh
                feedbac_textPractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.stopped')
                feedbac_textPractice_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedbackPracticeBS" ---
    for thisComponent in feedbackPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsPracticeBS'


# --- Prepare to start Routine "startRealBS" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.x = []
mouse_4.y = []
mouse_4.leftButton = []
mouse_4.midButton = []
mouse_4.rightButton = []
mouse_4.time = []
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
startRealBSComponents = [praccompleteBS, cont_buttonBSReal, mouse_4]
for thisComponent in startRealBSComponents:
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

# --- Run Routine "startRealBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccompleteBS* updates
    if praccompleteBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccompleteBS.frameNStart = frameN  # exact frame index
        praccompleteBS.tStart = t  # local t and not account for scr refresh
        praccompleteBS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccompleteBS, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccompleteBS.started')
        praccompleteBS.setAutoDraw(True)
    
    # *cont_buttonBSReal* updates
    if cont_buttonBSReal.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cont_buttonBSReal.frameNStart = frameN  # exact frame index
        cont_buttonBSReal.tStart = t  # local t and not account for scr refresh
        cont_buttonBSReal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_buttonBSReal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cont_buttonBSReal.started')
        cont_buttonBSReal.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_4.started', t)
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(cont_buttonBSReal)
                    clickableList = cont_buttonBSReal
                except:
                    clickableList = [cont_buttonBSReal]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                x, y = mouse_4.getPos()
                mouse_4.x.append(x)
                mouse_4.y.append(y)
                buttons = mouse_4.getPressed()
                mouse_4.leftButton.append(buttons[0])
                mouse_4.midButton.append(buttons[1])
                mouse_4.rightButton.append(buttons[2])
                mouse_4.time.append(mouse_4.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startRealBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startRealBS" ---
for thisComponent in startRealBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_4.x', mouse_4.x)
thisExp.addData('mouse_4.y', mouse_4.y)
thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
thisExp.addData('mouse_4.midButton', mouse_4.midButton)
thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
thisExp.addData('mouse_4.time', mouse_4.time)
thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name)
thisExp.nextEntry()
# the Routine "startRealBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsBS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber copy.xlsx'),
    seed=None, name='trialsBS')
thisExp.addLoop(trialsBS)  # add the loop to the experiment
thisTrialsBS = trialsBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
if thisTrialsBS != None:
    for paramName in thisTrialsBS:
        exec('{} = thisTrialsBS[paramName]'.format(paramName))

for thisTrialsBS in trialsBS:
    currentLoop = trialsBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
    if thisTrialsBS != None:
        for paramName in thisTrialsBS:
            exec('{} = thisTrialsBS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbersBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersBScode
    import random
    
    nTrialsBS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsBS ==1:
        correct = [];
        digitSpan = minDigitBS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitBS:
        digitSpan = minDigitBS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersBSComponents = []
    for thisComponent in selectNumbersBSComponents:
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
    
    # --- Run Routine "selectNumbersBS" ---
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
        for thisComponent in selectNumbersBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbersBS" ---
    for thisComponent in selectNumbersBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoopBS = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopBS')
    thisExp.addLoop(digitLoopBS)  # add the loop to the experiment
    thisDigitLoopBS = digitLoopBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
    if thisDigitLoopBS != None:
        for paramName in thisDigitLoopBS:
            exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
    
    for thisDigitLoopBS in digitLoopBS:
        currentLoop = digitLoopBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
        if thisDigitLoopBS != None:
            for paramName in thisDigitLoopBS:
                exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersBS" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeBS
        tmpNumber = digitsForTrial[digitLoopBS.thisN]
        presentation_textBS.setText(tmpNumber)
        # keep track of which components have finished
        showNumbersBSComponents = [fixationBS, presentation_textBS]
        for thisComponent in showNumbersBSComponents:
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
        
        # --- Run Routine "showNumbersBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationBS* updates
            if fixationBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationBS.frameNStart = frameN  # exact frame index
                fixationBS.tStart = t  # local t and not account for scr refresh
                fixationBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationBS.started')
                fixationBS.setAutoDraw(True)
            if fixationBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationBS.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationBS.tStop = t  # not accounting for scr refresh
                    fixationBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationBS.stopped')
                    fixationBS.setAutoDraw(False)
            
            # *presentation_textBS* updates
            if presentation_textBS.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_textBS.frameNStart = frameN  # exact frame index
                presentation_textBS.tStart = t  # local t and not account for scr refresh
                presentation_textBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_textBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_textBS.started')
                presentation_textBS.setAutoDraw(True)
            if presentation_textBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_textBS.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_textBS.tStop = t  # not accounting for scr refresh
                    presentation_textBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_textBS.stopped')
                    presentation_textBS.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersBS" ---
        for thisComponent in showNumbersBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeBS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoopBS'
    
    
    # --- Prepare to start Routine "RecallBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxBS.reset()
    # setup some python lists for storing info about the mouseBS
    mouseBS.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallBSComponents = [recall_txtBS, textboxBS, cont_buttonBS, mouseBS]
    for thisComponent in RecallBSComponents:
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
    
    # --- Run Routine "RecallBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtBS* updates
        if recall_txtBS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtBS.frameNStart = frameN  # exact frame index
            recall_txtBS.tStart = t  # local t and not account for scr refresh
            recall_txtBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtBS.started')
            recall_txtBS.setAutoDraw(True)
        
        # *textboxBS* updates
        if textboxBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxBS.frameNStart = frameN  # exact frame index
            textboxBS.tStart = t  # local t and not account for scr refresh
            textboxBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxBS.started')
            textboxBS.setAutoDraw(True)
        
        # *cont_buttonBS* updates
        if cont_buttonBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonBS.frameNStart = frameN  # exact frame index
            cont_buttonBS.tStart = t  # local t and not account for scr refresh
            cont_buttonBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonBS.started')
            cont_buttonBS.setAutoDraw(True)
        # *mouseBS* updates
        if mouseBS.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseBS.frameNStart = frameN  # exact frame index
            mouseBS.tStart = t  # local t and not account for scr refresh
            mouseBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseBS.started', t)
            mouseBS.status = STARTED
            mouseBS.mouseClock.reset()
            prevButtonState = mouseBS.getPressed()  # if button is down already this ISN'T a new click
        if mouseBS.status == STARTED:  # only update if started and not finished!
            buttons = mouseBS.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonBS)
                        clickableList = cont_buttonBS
                    except:
                        clickableList = [cont_buttonBS]
                    for obj in clickableList:
                        if obj.contains(mouseBS):
                            gotValidClick = True
                            mouseBS.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallBS" ---
    for thisComponent in RecallBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsBS.addData('textboxBS.text',textboxBS.text)
    # Run 'End Routine' code from code_3BS
    digitsForTrial.reverse(); # reverse order for backward span
    
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textboxBS.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsBS (TrialHandler)
    x, y = mouseBS.getPos()
    buttons = mouseBS.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonBS)
            clickableList = cont_buttonBS
        except:
            clickableList = [cont_buttonBS]
        for obj in clickableList:
            if obj.contains(mouseBS):
                gotValidClick = True
                mouseBS.clicked_name.append(obj.name)
    trialsBS.addData('mouseBS.x', x)
    trialsBS.addData('mouseBS.y', y)
    trialsBS.addData('mouseBS.leftButton', buttons[0])
    trialsBS.addData('mouseBS.midButton', buttons[1])
    trialsBS.addData('mouseBS.rightButton', buttons[2])
    if len(mouseBS.clicked_name):
        trialsBS.addData('mouseBS.clicked_name', mouseBS.clicked_name[0])
    # the Routine "RecallBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback_textBS.setText(fbTxt)
    # keep track of which components have finished
    FeedbackBSComponents = [feedback_textBS]
    for thisComponent in FeedbackBSComponents:
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
    
    # --- Run Routine "FeedbackBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_textBS* updates
        if feedback_textBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_textBS.frameNStart = frameN  # exact frame index
            feedback_textBS.tStart = t  # local t and not account for scr refresh
            feedback_textBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_textBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_textBS.started')
            feedback_textBS.setAutoDraw(True)
        if feedback_textBS.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_textBS.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_textBS.tStop = t  # not accounting for scr refresh
                feedback_textBS.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_textBS.stopped')
                feedback_textBS.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackBS" ---
    for thisComponent in FeedbackBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsBS'


# --- Prepare to start Routine "END" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [ThankYou]
for thisComponent in ENDComponents:
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

# --- Run Routine "END" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.tStart = t  # local t and not account for scr refresh
        ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ThankYou.started')
        ThankYou.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "END" ---
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
