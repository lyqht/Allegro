These notes are made for fellow beginner programmers by a layman who only has the knowledge from 10.009 The Digital World course in SUTD, which introduces students to Python. Thus, it will not be very comprehensive as it will skip over a lot on how Kivy does its modularity and abstraction to achieve its current form of code architecture. If you are interested though, headover here to read indepth.

# Intro to Graphic User Interface (GUI)

As a coder, you know that we write programmes based on conditionals and loops. Similarly, here, Kivy has a main loop that runs during its application lifetime, which only quits upon closing the app. In this main loop, user inputs, hardware sensors etc are rendered to the display. Within the main loop, there are nested loops happening as well, and as usual avoid infinite/long loops, and also sleeping. Otherwise your app can't do other stuff and might just die.
```
def on_touch_down(self, touch):
    for child in self.children[:]:
        if child.dispatch('on_touch_down', touch):
            return True
```
# Touch

Interaction with the GUI is made through Touch Instances, which are initialized by motion events such as clicking, hovering of the mouse over the screen or even swiping in the case of a touch screen. You can consider the Touch to be a sort of state machine, where it has 3 states.

State 1. Down For mouse and keyboard input interfaces, it happens when you click or tap on the keyboard key.

State 2 : Move Whenever the 2D position of a touch changes *Note: You can categorize almost any interaction with the GUI by referring to its coordinates. This will become very relevant later on.

State 3 : Up For touch screen interfaces, it happens where there is literally nothing touching the screen aka your finger is up. For mouse and keyboard input interfaces, this is when you are afk-ing / not doing shit on your com.

#### Customizing touch-able area
For restricting the area for touch instances, use the collide_point(). True if within area. False otherwise.

# Events

An event will be formed based on the touch instance: on_touch_down, on_touch_move or on_touch_up. This event is first received by the root widget of the widget tree, and which will be passed down from there on, until it reaches the target widget. Widgets are objects that receive input events.

translating this to code:
```
def on_touch_down(self, touch):
    for child in self.children[:]:
        if child.dispatch('on_touch_down', touch):
            return True
```
### Callbacks

To use events, you have to bind callbacks to them.

### Types of Events

There are various types of events, those that you can see the changes immediately and those that you don't.

Custom: u make the call. make ur own eventdispatcher class and the methods it can employ.
Property: When widget changes its position or size.
Widget-defined which then results in Window Events that you can see.
You can specify these events and their target widgets via the EventDispatcher class. Examples of the event dispatchers:

- Widget
- Animation
- Clock

### Event Frequency
For events to happen only once, use Clock.schedule_once(some_func, t). The second arguement here is the amount of time to wait before calling the function in seconds.

- if t > 0, the func is called in t seconds.
- elif t == 0, the func is called after next frame.
- elif t == -1, the func is called before next frame. This is usually used when you are already in a scheduled event.

For events that you need them to be happening repetitively, use this code within your function : 
```
event_name = Clock.schedule_interval(some_func, t / times_to_be_repeated_persec).
```
You can unschedule these events as well by:

event_name.cancel() OR
Clock.unschedule() OR
return False once a certain counter is reached e.g. stop repitition after 5 times:
        
```
count = 0
def some_func(inp):
	global count
	count += 1
	if count == 5:
		print "terminating broken radio mode."
		return False
	print 'The com nags at you to do something.'
Clock.schedule_interval(some_func, 1/20)
```
BUT preferably use trigger(), which prevents duplicate calls.
