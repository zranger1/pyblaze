# pyblaze
A Python library that presents a simple, synchronous interface for communicating with and
controlling one or more Pixelblaze LED controllers. Requires Python 3 and the websocket-client
module.

## Version 0.0.1
Initial release - here be dragons (hopefully not, but bugs are within the realm of possibility)

## Requirements
Python 3.4-3.7 (written and tested on 3.7.7)

websocket-client (installable via pip, or from https://github.com/websocket-client/websocket-client
(Python 3.8 and above are not yet supported by websocket-client module)

## Known Issues
Will not work if you've got the Pixelblaze web UI running on the same computer (actually, the same interface).
Trying to create a Pixelblaze object under those circumstances will generate an exception.  The browser 
does not want to share the socket, and strange things might happen even if it did. 

I've gone to a some length to put an easy-to-program synchronous interface over what is essentially an
asynchronous communication system. At this point, it's good, but not perfect. It may behave oddly if you are 
controlling the same Pixelblaze from multiple computers or multiple programs.  Report bugs of this sort if
you see them -- it may not be fixable, but at least I can take a look.

Detection and Firestorm-style time synchronization are not yet implemented, but are coming soon.

## Installation
Pyblaze consists of a single file -- [pyblaze.py](https://github.com/zranger1/pyblaze/blob/main/pyblaze/pyblaze.py) from this repository.  Drop it into your project
directory and import it into your project.  That's all.  An example -- [example.py](https://github.com/zranger1/pyblaze/blob/main/pyblaze/example.py) -- of setup and
API usage is also provided.

## API Documentation
(roughly alphabetical except for object constructor)

#### PixelBlaze(addr)
Create and open Pixelblaze object. Takes the Pixelblaze's IPv4 address in the
usual 12 digit numeric form (for example, 192.168.1.xxx)  Returns a connected
Pixelblaze object.  To control multiple Pixelblazes, create multiple objects.

#### close()
Close websocket connection on Pixelblaze object.  The connection can be 
reopene by calling open() on the same or a different IP address.

#### getActivePattern()
Returns the ID and name of the pattern currently running on
the Pixelblaze if available.  Otherwise returns an empty dictionary
object

#### getControls(pid)
Returns a JSON object containing the state of all the active pattern's UI controls

#### getHardwareConfig()
Returns a JSON object containing all the available hardware configuration data

#### getPatternList()
Returns a dictionary containing the unique ID and the text name of all
saved patterns on the Pixelblaze

#### getVars()
Returns JSON object containing all vars exported from the active pattern

#### open(addr)
Open websocket connection to given ip address.  Called automatically
when a Pixelblaze object is created - it is not necessary to
explicitly call open to connect unless the websocket has been closed by the
user or by the Pixelblaze.

#### setActivePattern(pid)
Sets the currently running pattern, using either an ID or a text name

#### setBrightness(n)
Set the Pixelblaze's global brightness.  Valid range is 0-1

#### setControl(ctl_name, value, saveFlash = False)
Sets the value of a single UI controls in the active pattern.
to values contained inct in argument json_ctl. To reduce wear on
Pixelblaze's flash memory, the saveFlash parameter is ignored
by default.  See documentation for _enable_flash_save() for
more information.

#### setControls(json_ctl, saveFlash = False)
Sets UI controls in the active pattern to values contained in
the JSON object in argument json_ctl. To reduce wear on
Pixelblaze's flash memory, the saveFlash parameter is ignored
by default.  See documentation for _enable_flash_save() for
more information.

#### setDataspeed(speed, saveFlash = False)
Sets custom bit timing for WS2812-type LEDs.
**CAUTION:** For advanced users only.  If you don't know
exactly why you want to do this, DON'T DO IT.

See discussion in this thread on the Pixelblaze forum:
https://forum.electromage.com/t/timing-of-a-cheap-strand/739

Note that you must call _enable_flash_save() in order to use
the saveFlash parameter to make your new timing (semi) permanent.

#### setSequenceTimer(n)
Sets number of milliseconds the Pixelblaze's sequencer will run each pattern
before switching to the next.

#### startSequencer()
Enable and start the Pixelblaze's internal sequencer

#### stopSequencer()
Stop and disable the Pixelblaze's internal sequencer

#### setVariable(var_name, value)
Sets a single variable to the specified value. Does not check to see if the
variable is actually exported by the current active pattern.

#### setVars(json_vars)
Sets pattern variables contained in the json_vars (JSON object) argument.
Does not check to see if the variables are exported by the current active pattern.

## Utility methods
#### _enable_flash_save()
**IMPORTANT SAFETY TIP:**
To preserve your Pixelblaze's flash memory, which can wear out after a number of
cycles, you must call this method before using setControls() with the
saveFlash parameter set to True.
If this method is not called, setControls() will ignore the saveFlash parameter
and will not save settings to flash memory.

#### _id_from_name(patterns, name)
Utility method: Given the list of patterns and text name of a pattern, returns that pattern's ID

#### _get_pattern_id(pid)
Returns a pattern ID if passed either a valid ID or a text name


