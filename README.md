
<h1>Simple Laptop Teleprompter</h1>

<p>A simple Python script to create a teleprompter application designed for laptops with built-in webcams.</p>

<ul><li>Display text in a GUI window</li><li>Scroll through text using the left and right arrow keys</li><li>Exit program by pressing the ESC key</li><li>Text is positioned at the middle of the top of the screen, making it easier for users to look directly at the camera</li><li>Option to specify the script file to be used and the phrase length for the teleprompter</li></ul>

<h2>Requirements</h2>

<ul><li>Python 3</li><li>Tkinter</li><li>pynput</li></ul>

<h2>Usage</h2>

<ol><li>Clone the repository</li><li>Run the script by entering <code>python teleprompter.py</code> in the command line</li><li>Use the left and right arrow keys to scroll through the text</li><li>Press the ESC key to exit the program</li><li>You can also specify the script file to be used, the phrase length, and the height for the teleprompter by using command line arguments:<ul><li><code>-s</code> or <code>--script</code> to specify the script file (default: script.txt)</li><li><code>-p</code> or <code>--phrase</code> to specify the phrase length (default: 3)</li><li><code>-H</code> or <code>--height</code> to specify the height of the teleprompter window (default: 15)</li></ul></li></ol>

<h2>Example</h2>

<code> python teleprompter.py -s myscript.tx -p 5 -H 15 </code>

<p>This will run the teleprompter with the script file "myscript.txt", a phrase length of 5, and a height of 15.</p>

<h2>Note</h2>

<p>For best results, use a laptop with built-in webcam. The window will position itself the top of the screen, making it easy to look directly at the camera while reading the text.</p>
