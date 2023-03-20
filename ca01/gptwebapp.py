'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''

from flask import request,redirect,url_for,Flask,render_template
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('API_KEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789369uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')
        
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team(): 
    return render_template('team.html')

# @app.route('/index')
# def index():
#     ''' display a link to the general query page '''
#     print('processing / route')
#     return f'''
#         <h1>GPT Demo</h1>
#         <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
#         <h1>Optimize Code</h1>
#         <a href="{url_for('optimizecode')}">Generate a List of Suggestions to Optimize Your Code</a>
#         <h1>Generate Java Docs</h1>
#         <a href="{url_for('javadoc')}">Generate JavaDocs for Your Java Code</a>
#         <h1>Big-O Analysis</h1>
#         <a href="{url_for('bigOanalysis')}">Generate a Line-by-Line Big-O Analysis of your Code</a>
#     '''
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/optimizecode', methods=['GET', 'POST'])
def optimizecode():

    added_prompt = "Return a list of optimizations that could be made to the following piece of code:\n"

    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(added_prompt + prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>Generate Code-optimizing Suggestions</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/javadoc', methods=['GET', 'POST'])
def javadoc():

    added_prompt = "Create java doc comments for this piece of java code:\n"

    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(added_prompt + prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>Create JavaDoc Comments from Code</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/bigOanalysis', methods=['GET', 'POST'])
def bigOanalysis():

    added_prompt = """Perform a line-by-line Big-O runtime analysis for the provided code below.
    For example, let's say I have a for loop that runs n times, and in the loop, I have a line that runs in constant time. 
    The answer I am expecting is: "The first line runs in a for loop, and it runs in O(n) time. The second line runs in O(1) time. 
    Because the second line is a statement in the for loop, the program run in O(n) time."\nCode: """

    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(added_prompt + prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>Generate Big-O Runtime Analysis</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
