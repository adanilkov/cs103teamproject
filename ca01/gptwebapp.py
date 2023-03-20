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

@app.route('/')
def opticode():
    return render_template('index.html')
        
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team(): 
    return render_template('team.html')
    
@app.route('/optimizecode', methods=['GET', 'POST'])
def optimizecode():

    added_prompt = "Return a list of optimizations that could be made to the following piece of code:\n"

    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    prompt = ""

    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(added_prompt + prompt)
        return render_template('optimizecode.html', prompt=prompt, answer=answer)
    return render_template('optimizecode.html', prompt=prompt, answer='')
    
@app.route('/javadoc', methods=['GET', 'POST'])
def javadoc():

    added_prompt = "Create java doc comments for this piece of java code:\n"

    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    prompt = ""

    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(added_prompt + prompt)
        return render_template('javadoc.html', prompt=prompt, answer=answer) 
    return render_template('javadoc.html', prompt=prompt, answer='') 

@app.route('/bigO', methods=['GET', 'POST'])
def bigOanalysis():
    added_prompt = """Perform a line-by-line Big-O runtime analysis for the provided code below.
    For example, let's say I have a for loop that runs n times, and in the loop, I have a line that runs in constant time. 
    The answer I am expecting is: "The first line runs in a for loop, and it runs in O(n) time. The second line runs in O(1) time. 
    Because the second line is a statement in the for loop, the program run in O(n) time."\nCode: """

    prompt = ""

    if request.method == 'POST':
        prompt = request.form['prompt']
        temp = prompt
        answer = gptAPI.getResponse(added_prompt + prompt)
        return render_template('bigO.html', prompt=temp, answer=answer)

    return render_template('bigO.html', prompt=prompt, answer='') 

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
