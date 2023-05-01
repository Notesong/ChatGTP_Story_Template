# This template helps to provide a completely customizable (and totally manual) way to create or edit a story using OpenAI ChatGTP and Python. Instead of using ChatGTP's simple prompt/reply website, you choose what the AI 'remembers', giving you more control over input, output, tokens, and such. The template is set up to use GTP 3.5 Turbo, but you can edit the template to use any version you wish.

# Read through the comments in this template step-by-step to receive the most guidance.  On that note: Everything in comments (including the lines of code) are suggestions. You're free to accomplish these tasks in any way you see fit. Whenever you see a [], fill in whatever it's asking for and be sure to remove the []'s.

# On that note: This is not a programming tutorial. A basic understand of Python is recommended, but not necessary as long as the template is followed. If you plan on making big changes, get brushed up on your Python!

# I strongly advise putting every AI response into a document of some type so that the response is not lost, in case the terminal history gets corrupted, etc. Furthermore, sometimes things will get weird or just go in a direction you don't like. Don't be afraid to try the request (or edit the request) again if you get something that doesn't fit your vision. These AI's simply don't have a human's level of comprehension of details and abstract thinking and do make mistakes. You can (and really should) edit responses by hand, too, to fix any inconsistancies or oddities and to add your own style to get precisely what you're looking for!  

# This tool I found helps easily add escapes (\n,\t,\r,\", etc) to your paragraphs (it's for JavaScript, but it'll work for Python, too) You'll want to use these escapes on pretty much all of the paragraphs you send to the AI because Python can't handle breaks in strings, nor will it understand you actually want that " in there if it's not written like \".  Using this tool is the easiest way I found to format the strings properly. And "buy him a coffee" if you find the website useful :) :
# https://www.freeformatter.com/javascript-escape.html



import openai

# Replace your_key (and keep the quotes there, otherwise it'll no longer be a string) below with the key you obtained in your OpenAI account (https://openai.com/).  You can find instructions on how to find your key here:
# https://www.youtube.com/watch?v=pGOyw_M1mNE&t=2s

openai.api_key = "your_key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # You can change this based on your needs.
    messages=[

        #Replace [genre] with the genre you'd like the AI to write in (ex. Fantasy, Science Fiction, Biographical, etc.)

        {"role": "system", "content": "You are a [genre] author. Your task is to write [genre] stories in a vivid and intriguing writing style."},


        #####################
        ### Story Details ### (Filled out either by you or ChatGTP)
        #####################
        
        # Line 36 can be filled out either by you or by ChatGPT. If it's filled out by you, head to line 48, when you're done. Be as specific as possible! If it's be filled out by ChatGPT, head to line 38 for further instructions.

        {"role": "user", "content": "Genre: ; Prompt: ; Title: ; Setting: ; Progagonist: ; Antagonist: ; Conflict: ; Dialog: [Instructions for using dialogue to advance the plot, reveal character, and provide information to the user] ; Theme: ; Tone: ; Pacing: ; Optional: [Insert any additional details or requirements for the story, such as a specific word count or genre constraints]"},
        
        # If the story details are to be written by ChatGPT, uncomment line 40 (to un-comment a line, simply remove the "#" at the front of the line), run the program. The result will come back in paragraphs. You'll need to use escapes to make the paragraphs into a string.  Do so, then insert the result into the empty "" in line line 41 and un-comment line 41, and then comment out lines 36-40.  Continue on with "Story Outline".

        #{"role": "user", "content": "Fill out the template above for a story."},
        #{"role": "assistant", "content": ""},


        #####################
        ### Story Outline ###
        #####################

        # Follow the same basic idea relayed in "Story Details" of un-commenting and commenting out for the rest of the program, based on your needs.  

        # Here, un-comment line 52, run the program, put the results into line 53 and un-comment line 53, and then comment out line 52 again. Please note: If the results contain the title or any other extra information, also delete that from the response before continuing. And then continue on with "Chapter Creation with Minimal Chapters"

        #{"role": "user", "content": "Build a story outline from the factors above. Give it a heading called: \"Story Chapters\""},
        #{"role": "assistant", "content": ""},


        ##############################################
        ### Chapter Creation with Minimal Chapters ###
        ##############################################

        # Got the idea? Keep going! This will write all the chapters at once, although they'll be very short at this point. Be sure add the repsonse to line 63 and then comment out line 62, after you're done.

        #{"role": "user", "content": "Create story chapters from the outline above."},
        #{"role": "assistant", "content": ""},


        ################################
        ### 1 by 1 Expanded Chapters ###
        ################################

        # Change [chapter#] to whatever chapter you're currently working on (ex. 1). Run through this secion as many times as you need to get all of the individual chapters you need. Each time, you will copy and paste the chapters into your document. There is no need to give them back to the AI. And you're done! Or are you? Continue on to "Edit the Story", if you so desire (if you do, be sure to comment out line 72).

        #{"role": "user", "content": "Write chapter [chapter#] in depth and in great detail with lots of dialog, in an intriguing writing style."},


        ################################
        ### Optional: Edit the story ### (for the best results, do this)
        ################################

        # In the following edit options, 'content' ccould be anything from a word or two or three, to a sentence, to a paragraph, or to multiple paragraphs. You can edit the requests I've provided to include or take out anything you wish. These are only suggestions. You can be as specific or as general as you like. Don't be afraid to try the request again if you get something that doesn't work. And, again, AI isn't perfect, so you always have the option to edit by hand!  Add the changes to your document when you receive the response.
        
        ###################
        # Expanding Content

        #{"role": "user", "content": "Expand this section to include great detail and lots of inner and outer dialog: [insert the content here]"},
       
        ####################
        # Inserting Content
       
        #{"role": "user", "content": "Write more content between this part: \"[insert the point you want the story to be continued off of.]\" and this part: \"[insert the tail end of the new content]\""},

        ####################
        # Continuing Content
       
        #{"role": "user", "content": "Continue this section: [insert the content you want the story to be continued off of.]"},         

        ####################
        # Rephrasing Content
       
        #{"role": "user", "content": "Rephrase this section so that it [explain what you want it to be written like]: [insert the content you want adjusted here]"},

        #####################
        # Simplifying Content
       
        #{"role": "user", "content": "Simplify this section: [insert the content you want adjusted here]"},
        
        ###############
        # Adjust Dialog

        #{"role": "user", "content": "Rephrase this dialog so that it sounds like it was written by/in [ex. Tolkien, the Middle Ages]: [insert the content you want adjusted here]"},

        ############
        # Add Dialog

        #{"role": "user", "content": "Add dialog to this section: [insert the content you want adjusted here]"},


        ##############################################
        ### Extra Blanks for You to Copy and Paste ### (Just in case)
        ##############################################

        #{"role": "user", "content": ""},
        #{"role": "assistant", "content": ""},
    ]
)

print(completion.choices[0].message.content)