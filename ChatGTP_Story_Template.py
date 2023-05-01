# This tool helps easily add escapes (\n,\t,\r,\", etc) to your paragraphs (it's for JavaScript, but it'll work for Python, too):
# https://www.freeformatter.com/javascript-escape.html

import openai

openai.api_key = "your_key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": "You are a [genre] author. Your task is to write [genre] stories in a vivid and intriguing writing style."},
        
        # Line 14 can be filled out by you or by ChatGPT.  If it's filled out by you, head to line 20, when you're done. If it'll be filled out by ChatGPT, head to line 16 for further instructions.
        {"role": "user", "content": "Prompt: ; Title: ; Setting: ; Progagonist: ; Antagonist: ; Conflict: ; Dialog: ; Theme: ; Tone: ; Pacing: ; Optional: [Insert any additional details or requirements for the story, such as a specific word count or genre constraints]"},
        
        # If the story is to be completely written by ChatGPT, uncomment line 17, run the program, put the results into line 18 and un-comment line 18, and then comment out lines 14-17.  Continue on with line 20.
        # {"role": "user", "content": "Fill out the template above for a [genre] story"},
        # {"role": "assistant", "content": ""},

        # Follow the same basic idea relayed on line 13 of un-commenting and commenting out for the rest of the program (ex: uncomment line 22, run the program, put the results into line 23 and un-comment line 23, and then comment out line 22 again).

        # {"role": "user", "content": "Build a story outline from the factors above."},
        # {"role": "assistant", "content": ""},

        # {"role": "user", "content": "Create story chapters from the outline above."},
        # {"role": "assistant", "content": ""},

        # {"role": "user", "content": "Write chapter [chapter#] in depth and in great detail with lots of dialog, in an intriguing writing style."},
        # {"role": "assistant", "content": ""},
        
        # extra blank ones for further refinement
        # {"role": "user", "content": ""},
        # {"role": "assistant", "content": ""},
    ]
)
# response['choices'][0]['message']['content']
print(completion.choices[0].message.content)