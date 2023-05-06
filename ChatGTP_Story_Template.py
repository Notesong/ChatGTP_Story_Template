# This template helps to provide a completely customizable (and totally manual) way to create or edit a story using OpenAI ChatGTP and Python. Instead of using ChatGTP's simple prompt/reply website, you choose what the AI 'remembers', giving you more control over input, output, tokens, and such. The template is set up to use GTP 3.5 Turbo, but you can edit the template to use any version you wish. To obtain an OpenAI account, you can head here:  https://openai.com/  To set up your system for Python and/or OpenAI and to get a basic outline of how this Python program works, check out this tutorial: https://www.youtube.com/watch?v=e9pCg_QSezU

# Read through the comments in this template step-by-step to receive the most guidance. Whenever you see a [], fill in whatever it's asking for and be sure to remove the []'s. Everything in comments (including the lines of code) are suggestions. You're free to accomplish these tasks in any way you see fit. 

# On that note: This is not a programming tutorial. A basic understanding of Python is recommended, but not necessary as long as the template is followed. If you plan on making big changes, get brushed up on your Python!

# I strongly advise putting every AI response into a document of some type so that the response is not lost, in case the terminal history gets corrupted, etc. Furthermore, sometimes things will get weird or just go in a direction you don't like. Don't be afraid to try the request (or edit the request) again if you get something that doesn't fit your vision. These AI's simply don't have a human's level of attention to details and abstract thinking (nor have a true understanding of real life) and do make mistakes or write something that's just a plain mess. You can (and really should) edit responses yourself, too, to fix any inconsistencies, redundancies, or oddities and to add your own style to get precisely what you're looking for!  

# To help you along the way: This tool easily adds escapes (\n,\t,\r,\", etc) to your paragraphs (it's for JavaScript, but it'll work for Python, too) You'll want to use these escapes on pretty much all of the paragraphs you send to the AI because Python can't handle breaks in strings, nor will it understand you actually want that " in there if it's not written like \".  Using this tool is the easiest way I found to format the strings properly. And "buy him a coffee" if you find the website useful :) :

# https://www.freeformatter.com/javascript-escape.html



import openai

# Replace your_key (and keep the quotes there, otherwise it'll no longer be a string) below with the key you obtained in your OpenAI account (https://openai.com/). Your key can be found here: https://platform.openai.com/account/api-keys

openai.api_key = "your_key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # You can change this based on your needs.
    messages=[

        # Replace [genre] with the genre you'd like the AI to write in (ex. Fantasy, Science Fiction, Biographical, etc.)

        {"role": "system", "content": "You are a [genre] author. Your task is to write [genre] stories in a vivid and intriguing writing style."},


        #####################
        ### Story Details ### (Filled out either by you or ChatGTP)
        #####################
        
        # Line 36 can be filled out either by you or by ChatGPT. If it's filled out by you, head to line 48, when you're done. Be as specific as possible! If it's be filled out by ChatGPT, head to line 38 for further instructions.

        {"role": "user", "content": "Genre: ; Prompt: ; Title: ; Setting: ; Protagonist: ; Antagonist: ; Conflict: ; Dialog: [Instructions for using dialogue to advance the plot, reveal character, and provide information to the user] ; Theme: ; Tone: ; Pacing: ; Optional: [Insert any additional details or requirements for the story, such as a specific word count or genre constraints]"},
        
        # If the story details are to be written by ChatGPT, un-comment line 40 (to un-comment a line, simply remove the "#" at the front of the line), run the program. The result will come back in paragraphs. You'll need to use escapes to make the paragraphs into a string.  Do so, then insert the result into the empty "" in line 41 and un-comment line 41, and then comment out lines 36-40.  Continue on with "Story Outline".

        #{"role": "user", "content": "Fill out the template above for a story. Don't write the story yet."},
        #{"role": "assistant", "content": ""},


        # From here on, follow the same basic idea relayed in "Story Details" of un-commenting and commenting out for the rest of the program, based on your needs.  In general, you will be commenting out your prompts after the AI responds so that it doesn't try to answer them again.


        #####################
        ### Story Outline ###
        #####################

        #{"role": "user", "content": "Build a story outline from the factors above. Give it a heading called: \"Story Outline\""},
        #{"role": "assistant", "content": ""},


        ##############################################
        ### Chapter Creation with Minimal Content ###
        ##############################################

        # This will write all the chapters at once, although they'll be very short at this point.

        #{"role": "user", "content": "Create story chapters from the outline above."},
        #{"role": "assistant", "content": ""},


        ################################
        ### 1 by 1 Expanded Chapters ###
        ################################

        # Change [chapter#] to whatever chapter you're currently working on (ex. 1). Run through this section as many times as you need to get all of the individual chapters. Each time, you will copy and paste the AI created chapters into your document for safe keeping. You can either feed the AI all or the last part of the previous chapter or not. I've found that there can be a repeating of ideas, if no starting point is given outside of the outline, and the story as a whole can lack good flow. 

        # However, remember that you can only send the AI a limited amount of information (4096 tokens) in each request. You'll receive an error message if the request becomes too large. Furthermore, the more tokens you use, the more costly the story will become to write. Tokens are extremely cheap, but it's something to keep in mind. You can keep an eye on your usage here: https://platform.openai.com/account/usage

        #{"role": "user", "content": "With chapter [chapter#], begin or continue the story, as appropriate, in depth and in great detail with inner thoughts and dialog, in an intriguing writing style. If included below, continue off of the content of the last chapter."},
        #{"role": "assistant", "content": ""},

        # ...And you're done! Or are you? Continue on to "Edit the Story", if you so desire (if you do, be sure to comment out the prompt above).


        ################################
        ### Optional: Edit the story ### (for the best results, do this)
        ################################

        # In the following edit options, "content" could be anything from a word or two or three, to a sentence, to a paragraph, or to multiple paragraphs. Feel free to edit the prompts to get exactly what you're looking for. You can be as specific or as general as you like. Don't be afraid to try the request again if you get something that doesn't work. 

        # And, again, AI isn't perfect, so you always have the option to edit by hand! And really probably should, especially when AI is writing whole chapters at once since the wording can become odd, redundant, and lack good flow. 

        # On that note, this section can also be used to help write something you've already started on your own. In doing so, you'll maintain better control over your story and, in the end, it'll probably suit your needs just that much better. For instance, you can write the story bit by bit instead of whole chapters, molding the storyline as you go. From you, that can come as a single sentence, or paragraphs, or even just asking the AI to continue something in a specific (you can summarize the exact things you want it to write and then let it fly) or non-specific way (giving it free reign).

        
        ###################
        # Expanding Content

        #{"role": "user", "content": "Expand this section to include great detail, inner thoughts, and dialog: [insert the content here]"},
       
        ####################
        # Inserting Content
       
        #{"role": "user", "content": "Write more content between this section: \"[insert the point you want the story to be continued off of.]\" and this section: \"[insert the tail end of the new content]\""},

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