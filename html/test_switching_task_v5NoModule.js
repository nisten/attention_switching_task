/*******************************  
 * Test_Switching_Task_V5 Test *
 *******************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'use prefs'
});

// store info about the experiment session:
let expName = 'test_switching_task_v5';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instruct_switch1RoutineBegin);
flowScheduler.add(instruct_switch1RoutineEachFrame);
flowScheduler.add(instruct_switch1RoutineEnd);
flowScheduler.add(instruct_switch2RoutineBegin);
flowScheduler.add(instruct_switch2RoutineEachFrame);
flowScheduler.add(instruct_switch2RoutineEnd);
flowScheduler.add(instruct_switch_practiceRoutineBegin);
flowScheduler.add(instruct_switch_practiceRoutineEachFrame);
flowScheduler.add(instruct_switch_practiceRoutineEnd);
const endSwitchPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(endSwitchPracticeLoopBegin, endSwitchPracticeLoopScheduler);
flowScheduler.add(endSwitchPracticeLoopScheduler);
flowScheduler.add(endSwitchPracticeLoopEnd);
flowScheduler.add(do_your_bestRoutineBegin);
flowScheduler.add(do_your_bestRoutineEachFrame);
flowScheduler.add(do_your_bestRoutineEnd);
flowScheduler.add(readyRoutineBegin);
flowScheduler.add(readyRoutineEachFrame);
flowScheduler.add(readyRoutineEnd);
flowScheduler.add(ISIRoutineBegin);
flowScheduler.add(ISIRoutineEachFrame);
flowScheduler.add(ISIRoutineEnd);
const switch1_trialLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(switch1_trialLoopBegin, switch1_trialLoopScheduler);
flowScheduler.add(switch1_trialLoopScheduler);
flowScheduler.add(switch1_trialLoopEnd);
flowScheduler.add(EndRoutineBegin);
flowScheduler.add(EndRoutineEachFrame);
flowScheduler.add(EndRoutineEnd);
flowScheduler.add(quitPsychoJS);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);

  return Scheduler.Event.NEXT;
}

var instruct_switch1Clock;
var text_3;
var instruct_switch2Clock;
var text_5;
var instruct_switch_practiceClock;
var text_11;
var ready_practiceClock;
var text_7;
var number_correct;
var msg;
var ISIClock;
var text;
var switch_trialClock;
var fixation3;
var image_2;
var switch_feedbackClock;
var text_12;
var MorePractice3Clock;
var text_16;
var do_your_bestClock;
var text_4;
var readyClock;
var text_6;
var EndClock;
var text_13;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruct_switch1"
  instruct_switch1Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_3',
    text : 'In this test, you will see either a BLUE or an ORANGE arrow.\n\nIf you see a BLUE arrow, press the left or right key \nbased on the LOCATION of the arrow.\n\nPress "N"  if the BLUE arrow is on the left.\nPress "M" if the BLUE arrow is on the right.\n\nIf you see an ORANGE arrow, press the left or right key\nbased on the direction it is pointing.\n\nPress "N" if the ORANGE arrow points left.\nPress "M" if the ORANGE arrow points right.\n\nPress the space key to continue.',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : 1.75, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "instruct_switch2"
  instruct_switch2Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_5',
    text : 'Remember, if you see a BLUE arrow, answer based on the LOCATION of the arrow on the screen.\n\nIf you see an ORANGE arrow, answer based on the DIRECTION the arrow is pointing.\n\nPress the space key to continue',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : 1.75, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "instruct_switch_practice"
  instruct_switch_practiceClock = new util.Clock();
  text_11 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_11',
    text : 'You will do a short practice trial before the real test. \n\n\nPress the space key to continue',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "ready_practice"
  ready_practiceClock = new util.Clock();
  text_7 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_7',
    text : 'The practice test will start in 5 seconds.',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  number_correct = 0;
  msg = ' ';
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text = new visual.TextStim({
    win : psychoJS.window,
    name : 'text',
    text : ' ',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "switch_trial"
  switch_trialClock = new util.Clock();
  fixation3 = new visual.TextStim({
    win : psychoJS.window,
    name : 'fixation3',
    text : '+',
    font : 'Arial',
    pos : [0, 0], height : 0.33,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.5,
    color : new util.Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  
  // Initialize components for Routine "switch_feedback"
  switch_feedbackClock = new util.Clock();
  msg=' ';
  
  text_12 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_12',
    text : 'default text',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : -1.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text = new visual.TextStim({
    win : psychoJS.window,
    name : 'text',
    text : ' ',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "MorePractice3"
  MorePractice3Clock = new util.Clock();
  
  text_16 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_16',
    text : 'Let\'s do some more practice.\nRemember, pay attention to the COLOUR of the arrows.\n\nIf the arrow is BLUE, press "N" or "M" based on the LOCATION of the arrow\n\nIf the arrow is ORANGE, press "N" or "M" based on the DIRECTION of the arrow',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : 1.75, ori: 0,
    color : new util.Color('black'),  opacity : 0,
    depth : -1.0 
  });
  
  // Initialize components for Routine "do_your_best"
  do_your_bestClock = new util.Clock();
  text_4 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_4',
    text : 'Now you will start the real test.\n\nTry to answer as fast as you can without making mistakes.\n\nIt is ok if you make some mistakes or lose track, just do your best.\n\nPress space key to start the test',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "ready"
  readyClock = new util.Clock();
  text_6 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_6',
    text : 'Ready?\n\nThe test starts in 5 seconds',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text = new visual.TextStim({
    win : psychoJS.window,
    name : 'text',
    text : ' ',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "switch_trial"
  switch_trialClock = new util.Clock();
  fixation3 = new visual.TextStim({
    win : psychoJS.window,
    name : 'fixation3',
    text : '+',
    font : 'Arial',
    pos : [0, 0], height : 0.33,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 0.5,
    color : new util.Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text = new visual.TextStim({
    win : psychoJS.window,
    name : 'text',
    text : ' ',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text_13 = new visual.TextStim({
    win : psychoJS.window,
    name : 'text_13',
    text : 'The test is now finished.',
    font : 'Arial',
    pos : [0, 0], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('black'),  opacity : 1,
    depth : 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var key_resp_7;
var instruct_switch1Components;
function instruct_switch1RoutineBegin() {
  //------Prepare to start Routine 'instruct_switch1'-------
  t = 0;
  instruct_switch1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_7 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  instruct_switch1Components = [];
  instruct_switch1Components.push(text_3);
  instruct_switch1Components.push(key_resp_7);
  
  for (const thisComponent of instruct_switch1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instruct_switch1RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_switch1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_switch1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_3* updates
  if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }
  
  // *key_resp_7* updates
  if (t >= 0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_7.tStart = t;  // (not accounting for frame time here)
    key_resp_7.frameNStart = frameN;  // exact frame index
    key_resp_7.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    key_resp_7.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (key_resp_7.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_7.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      key_resp_7.rt = key_resp_7.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instruct_switch1Components)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_switch1RoutineEnd() {
  //------Ending Routine 'instruct_switch1'-------
  for (const thisComponent of instruct_switch1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(key_resp_7.keys) >= 0) {    // No response was made
      key_resp_7.keys = undefined;
  }
  psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
  if (key_resp_7.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
      routineTimer.reset();
      }
  // the Routine "instruct_switch1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_8;
var instruct_switch2Components;
function instruct_switch2RoutineBegin() {
  //------Prepare to start Routine 'instruct_switch2'-------
  t = 0;
  instruct_switch2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_8 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  instruct_switch2Components = [];
  instruct_switch2Components.push(text_5);
  instruct_switch2Components.push(key_resp_8);
  
  for (const thisComponent of instruct_switch2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_switch2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_switch2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_switch2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_5* updates
  if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_5.tStart = t;  // (not accounting for frame time here)
    text_5.frameNStart = frameN;  // exact frame index
    text_5.setAutoDraw(true);
  }
  
  // *key_resp_8* updates
  if (t >= 0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_8.tStart = t;  // (not accounting for frame time here)
    key_resp_8.frameNStart = frameN;  // exact frame index
    key_resp_8.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    key_resp_8.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (key_resp_8.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_8.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      key_resp_8.rt = key_resp_8.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instruct_switch2Components)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_switch2RoutineEnd() {
  //------Ending Routine 'instruct_switch2'-------
  for (const thisComponent of instruct_switch2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(key_resp_8.keys) >= 0) {    // No response was made
      key_resp_8.keys = undefined;
  }
  psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
  if (key_resp_8.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
      routineTimer.reset();
      }
  // the Routine "instruct_switch2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_5;
var instruct_switch_practiceComponents;
function instruct_switch_practiceRoutineBegin() {
  //------Prepare to start Routine 'instruct_switch_practice'-------
  t = 0;
  instruct_switch_practiceClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_5 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  instruct_switch_practiceComponents = [];
  instruct_switch_practiceComponents.push(text_11);
  instruct_switch_practiceComponents.push(key_resp_5);
  
  for (const thisComponent of instruct_switch_practiceComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_switch_practiceRoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_switch_practice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_switch_practiceClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_11* updates
  if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_11.tStart = t;  // (not accounting for frame time here)
    text_11.frameNStart = frameN;  // exact frame index
    text_11.setAutoDraw(true);
  }
  
  // *key_resp_5* updates
  if (t >= 0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_5.tStart = t;  // (not accounting for frame time here)
    key_resp_5.frameNStart = frameN;  // exact frame index
    key_resp_5.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    key_resp_5.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (key_resp_5.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_5.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      key_resp_5.rt = key_resp_5.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instruct_switch_practiceComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_switch_practiceRoutineEnd() {
  //------Ending Routine 'instruct_switch_practice'-------
  for (const thisComponent of instruct_switch_practiceComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(key_resp_5.keys) >= 0) {    // No response was made
      key_resp_5.keys = undefined;
  }
  psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
  if (key_resp_5.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
      routineTimer.reset();
      }
  // the Routine "instruct_switch_practice" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endSwitchPractice;
function endSwitchPracticeLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  endSwitchPractice = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'endSwitchPractice'});
  psychoJS.experiment.addLoop(endSwitchPractice); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisEndSwitchPractice of endSwitchPractice) {
    thisScheduler.add(importTrialAttributes(thisEndSwitchPractice));
    thisScheduler.add(ready_practiceRoutineBegin);
    thisScheduler.add(ready_practiceRoutineEachFrame);
    thisScheduler.add(ready_practiceRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    const repeat_switch_practiceLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(repeat_switch_practiceLoopBegin, repeat_switch_practiceLoopScheduler);
    thisScheduler.add(repeat_switch_practiceLoopScheduler);
    thisScheduler.add(repeat_switch_practiceLoopEnd);
    thisScheduler.add(MorePractice3RoutineBegin);
    thisScheduler.add(MorePractice3RoutineEachFrame);
    thisScheduler.add(MorePractice3RoutineEnd);
    thisScheduler.add(endLoopIteration(thisEndSwitchPractice));
  }

  return Scheduler.Event.NEXT;
}

var repeat_switch_practice;
function repeat_switch_practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  repeat_switch_practice = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'switch_practice.xlsx',
    seed: undefined, name: 'repeat_switch_practice'});
  psychoJS.experiment.addLoop(repeat_switch_practice); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisRepeat_switch_practice of repeat_switch_practice) {
    thisScheduler.add(importTrialAttributes(thisRepeat_switch_practice));
    thisScheduler.add(switch_trialRoutineBegin);
    thisScheduler.add(switch_trialRoutineEachFrame);
    thisScheduler.add(switch_trialRoutineEnd);
    thisScheduler.add(switch_feedbackRoutineBegin);
    thisScheduler.add(switch_feedbackRoutineEachFrame);
    thisScheduler.add(switch_feedbackRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisRepeat_switch_practice));
  }

  return Scheduler.Event.NEXT;
}


function repeat_switch_practiceLoopEnd() {
  psychoJS.experiment.removeLoop(repeat_switch_practice);
  psychoJS.experiment.save({
    attributes: repeat_switch_practice.getAttributes()
  });

  return Scheduler.Event.NEXT;
}


function endSwitchPracticeLoopEnd() {
  psychoJS.experiment.removeLoop(endSwitchPractice);
  psychoJS.experiment.save({
    attributes: endSwitchPractice.getAttributes()
  });

  return Scheduler.Event.NEXT;
}

var switch1_trial;
function switch1_trialLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  switch1_trial = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'switch_condition1.xlsx',
    seed: undefined, name: 'switch1_trial'});
  psychoJS.experiment.addLoop(switch1_trial); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisSwitch1_trial of switch1_trial) {
    thisScheduler.add(importTrialAttributes(thisSwitch1_trial));
    thisScheduler.add(switch_trialRoutineBegin);
    thisScheduler.add(switch_trialRoutineEachFrame);
    thisScheduler.add(switch_trialRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisSwitch1_trial));
  }

  return Scheduler.Event.NEXT;
}


function switch1_trialLoopEnd() {
  psychoJS.experiment.removeLoop(switch1_trial);
  psychoJS.experiment.save({
    attributes: switch1_trial.getAttributes()
  });

  return Scheduler.Event.NEXT;
}

var ready_practiceComponents;
function ready_practiceRoutineBegin() {
  //------Prepare to start Routine 'ready_practice'-------
  t = 0;
  ready_practiceClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  number_correct = 0;
  // keep track of which components have finished
  ready_practiceComponents = [];
  ready_practiceComponents.push(text_7);
  
  for (const thisComponent of ready_practiceComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function ready_practiceRoutineEachFrame() {
  //------Loop for each frame of Routine 'ready_practice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ready_practiceClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_7* updates
  if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_7.tStart = t;  // (not accounting for frame time here)
    text_7.frameNStart = frameN;  // exact frame index
    text_7.setAutoDraw(true);
  }
  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_7.setAutoDraw(false);
  }
  
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of ready_practiceComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ready_practiceRoutineEnd() {
  //------Ending Routine 'ready_practice'-------
  for (const thisComponent of ready_practiceComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  return Scheduler.Event.NEXT;
}

var ISIComponents;
function ISIRoutineBegin() {
  //------Prepare to start Routine 'ISI'-------
  t = 0;
  ISIClock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.750000);
  // update component parameters for each repeat
  // keep track of which components have finished
  ISIComponents = [];
  ISIComponents.push(text);
  
  for (const thisComponent of ISIComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function ISIRoutineEachFrame() {
  //------Loop for each frame of Routine 'ISI'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ISIClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }
  frameRemains = 0.0 + 0.75 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of ISIComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ISIRoutineEnd() {
  //------Ending Routine 'ISI'-------
  for (const thisComponent of ISIComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var response_switch;
var switch_trialComponents;
function switch_trialRoutineBegin() {
  //------Prepare to start Routine 'switch_trial'-------
  t = 0;
  switch_trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(8.000000);
  // update component parameters for each repeat
  image_2.setPos([PositionX, PositionY]);
  image_2.setImage(File);
  response_switch = new core.BuilderKeyResponse(psychoJS);
  console.log(PositionX);
  console.log(File);
  console.log(number_correct);
  console.log(repeat_switch_practice);
  console.log(repeat_switch_practice.thisN);
  if (repeat_switch_practice.thisN == 0) {
      number_correct = 0;
  }
  
  // keep track of which components have finished
  switch_trialComponents = [];
  switch_trialComponents.push(fixation3);
  switch_trialComponents.push(image_2);
  switch_trialComponents.push(response_switch);
  
  for (const thisComponent of switch_trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function switch_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'switch_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = switch_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *fixation3* updates
  if (t >= 0.0 && fixation3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixation3.tStart = t;  // (not accounting for frame time here)
    fixation3.frameNStart = frameN;  // exact frame index
    fixation3.setAutoDraw(true);
  }
  frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixation3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixation3.setAutoDraw(false);
  }
  
  // *image_2* updates
  if (t >= 0.25 && image_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_2.tStart = t;  // (not accounting for frame time here)
    image_2.frameNStart = frameN;  // exact frame index
    image_2.setAutoDraw(true);
  }
  frameRemains = 0.25 + 7.75 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_2.setAutoDraw(false);
  }
  
  // *response_switch* updates
  if (t >= 0.1 && response_switch.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    response_switch.tStart = t;  // (not accounting for frame time here)
    response_switch.frameNStart = frameN;  // exact frame index
    response_switch.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    response_switch.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  frameRemains = 0.1 + 7.9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (response_switch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    response_switch.status = PsychoJS.Status.STOPPED;
  }
  if (response_switch.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'm', 'None']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (response_switch.keys.length == 0) {  // then this was the first keypress
        response_switch.keys = theseKeys[0];  // just the first key pressed
        response_switch.rt = response_switch.clock.getTime();
        // was this 'correct'?
        if (response_switch.keys == CorrAns) {
            response_switch.corr = 1;
        } else {
            response_switch.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of switch_trialComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function switch_trialRoutineEnd() {
  //------Ending Routine 'switch_trial'-------
  for (const thisComponent of switch_trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(response_switch.keys) >= 0) {    // No response was made
      response_switch.keys = undefined;
  }
  // was no response the correct answer?!
  if (response_switch.keys == undefined) {
    if (psychoJS.str(CorrAns).toLowerCase() == 'none') {
       response_switch.corr = 1  // correct non-response
    } else {
       response_switch.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('response_switch.keys', response_switch.keys);
  psychoJS.experiment.addData('response_switch.corr', response_switch.corr);
  if (response_switch.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('response_switch.rt', response_switch.rt);
      routineTimer.reset();
      }
  if (response_switch.corr) {
      number_correct = number_correct + 1;
  }
  
  if (number_correct/repeat_switch_practice.nTotal >= 0.75) {
      endSwitchPractice.finished = true;
  }
  
  
  
  return Scheduler.Event.NEXT;
}

var switch_feedbackComponents;
function switch_feedbackRoutineBegin() {
  //------Prepare to start Routine 'switch_feedback'-------
  t = 0;
  switch_feedbackClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  if (response_switch.corr) {   msg="Correct, good job!"; } else {     msg="Wrong, try again"; }
  text_12.setText(msg);
  // keep track of which components have finished
  switch_feedbackComponents = [];
  switch_feedbackComponents.push(text_12);
  
  for (const thisComponent of switch_feedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function switch_feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'switch_feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = switch_feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  
  // *text_12* updates
  if (t >= 0.0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_12.tStart = t;  // (not accounting for frame time here)
    text_12.frameNStart = frameN;  // exact frame index
    text_12.setAutoDraw(true);
  }
  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_12.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of switch_feedbackComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function switch_feedbackRoutineEnd() {
  //------Ending Routine 'switch_feedback'-------
  for (const thisComponent of switch_feedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  return Scheduler.Event.NEXT;
}

var MorePractice3Components;
function MorePractice3RoutineBegin() {
  //------Prepare to start Routine 'MorePractice3'-------
  t = 0;
  MorePractice3Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.110000);
  // update component parameters for each repeat
  if (endSwitchPractice.finished) {   continueRoutine = false; }
  // keep track of which components have finished
  MorePractice3Components = [];
  MorePractice3Components.push(text_16);
  
  for (const thisComponent of MorePractice3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function MorePractice3RoutineEachFrame() {
  //------Loop for each frame of Routine 'MorePractice3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = MorePractice3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  
  // *text_16* updates
  if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_16.tStart = t;  // (not accounting for frame time here)
    text_16.frameNStart = frameN;  // exact frame index
    text_16.setAutoDraw(true);
  }
  frameRemains = 0.0 + 0.11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_16.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of MorePractice3Components)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function MorePractice3RoutineEnd() {
  //------Ending Routine 'MorePractice3'-------
  for (const thisComponent of MorePractice3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  return Scheduler.Event.NEXT;
}

var key_resp_9;
var do_your_bestComponents;
function do_your_bestRoutineBegin() {
  //------Prepare to start Routine 'do_your_best'-------
  t = 0;
  do_your_bestClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_9 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  do_your_bestComponents = [];
  do_your_bestComponents.push(text_4);
  do_your_bestComponents.push(key_resp_9);
  
  for (const thisComponent of do_your_bestComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function do_your_bestRoutineEachFrame() {
  //------Loop for each frame of Routine 'do_your_best'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = do_your_bestClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_4* updates
  if (t >= 0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
  }
  
  // *key_resp_9* updates
  if (t >= 0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_9.tStart = t;  // (not accounting for frame time here)
    key_resp_9.frameNStart = frameN;  // exact frame index
    key_resp_9.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    key_resp_9.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (key_resp_9.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_9.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      key_resp_9.rt = key_resp_9.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of do_your_bestComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function do_your_bestRoutineEnd() {
  //------Ending Routine 'do_your_best'-------
  for (const thisComponent of do_your_bestComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(key_resp_9.keys) >= 0) {    // No response was made
      key_resp_9.keys = undefined;
  }
  psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
  if (key_resp_9.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
      routineTimer.reset();
      }
  // the Routine "do_your_best" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var readyComponents;
function readyRoutineBegin() {
  //------Prepare to start Routine 'ready'-------
  t = 0;
  readyClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  readyComponents = [];
  readyComponents.push(text_6);
  
  for (const thisComponent of readyComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function readyRoutineEachFrame() {
  //------Loop for each frame of Routine 'ready'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = readyClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_6* updates
  if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_6.tStart = t;  // (not accounting for frame time here)
    text_6.frameNStart = frameN;  // exact frame index
    text_6.setAutoDraw(true);
  }
  frameRemains = 0.0 + 5.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_6.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of readyComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function readyRoutineEnd() {
  //------Ending Routine 'ready'-------
  for (const thisComponent of readyComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var EndComponents;
function EndRoutineBegin() {
  //------Prepare to start Routine 'End'-------
  t = 0;
  EndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  EndComponents = [];
  EndComponents.push(text_13);
  
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function EndRoutineEachFrame() {
  //------Loop for each frame of Routine 'End'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = EndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_13* updates
  if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_13.tStart = t;  // (not accounting for frame time here)
    text_13.frameNStart = frameN;  // exact frame index
    text_13.setAutoDraw(true);
  }
  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_13.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEnd() {
  //------Ending Routine 'End'-------
  for (const thisComponent of EndComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importTrialAttributes(thisTrial) {
  return function () {
    psychoJS.importAttributes(thisTrial);

    return Scheduler.Event.NEXT;
  };
}


function quitPsychoJS() {
  psychoJS.window.close();
  psychoJS.quit();

  return Scheduler.Event.QUIT;
}
