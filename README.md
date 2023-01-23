<h1>Simple Laptop Teleprompter</h1>
<p>A simple Python script to create a teleprompter application for laptops with built-in webcams.</p>
<ul><li>Display text in a GUI window</li><li>Scroll through text using the left and right arrow keys</li><li>Exit program by pressing the ESC key</li><li>Text is positioned at the middle of the top of the screen, making it easier for users to look directly at the camera</li><li>Option to specify the script file to be used and the phrase length for the teleprompter</li></ul>
<h2>Requirements</h2>
<ul><li>Python 3</li><li>Tkinter</li><li>pynput</li></ul>
<h2>Usage</h2>
<ol><li>Clone the repository</li><li>Run the script by entering <code>python teleprompter.py</code> in the command line</li><li>Use the left and right arrow keys to scroll through the text</li><li>Press the ESC key to exit the program</li><li>You can also specify the script file to be used and the phrase length for the teleprompter by using command line arguments:<ul><li><code>-s</code> or <code>--script</code> to specify the script file (default: script.txt)</li><li><code>-p</code> or <code>--phrase</code> to specify the phrase length (default: 3)</li></ul></li></ol>
<h2>Example</h2>
<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre-wrap hljs language-css">python teleprompter<span class="hljs-selector-class">.py</span> -s myscript<span class="hljs-selector-class">.txt</span> -<span class="hljs-selector-tag">p</span> <span class="hljs-number">5</span>
</code></div></div></pre>
<p>This will run the teleprompter with the script file "myscript.txt" and a phrase length of 5.</p>
<h2>Note</h2>
<p>For best results, use a laptop with built-in webcam. The window will position itself the top of the screen, making it easy to look directly at the camera while reading the text.</p>
