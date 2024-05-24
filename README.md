# FactSetHackathon
Created an AI LLM specializing in personal finance and budgeting
# Mesh Hackathon

Greetings! This repo is designed to be a jumping-off point for the MESH program's hackathon project.

This year we will be building our very own AI Expert on top of openapi's GPT-4

## Project Description: Creating an AI Expert

Your hackathon project will be creating an AI Expert in a subject of your choice. Perhaps you would like an AI to write poetry on any subject. Maybe you want an AI to guide you on an epic fantasy adventure. Or perhaps you just want your AI to tell you terrible knock knock jokes. Whatever it is, GenAI can do it!

Throughout your hackathon, you will be building a *streamlit* application from scratch to build an AI Expert. You will start by building your own ChatGPT user interface using the openai API. Then, you will learn how to customize prompts to tailor your expert into a masterpiece of your own creation.

Example project: [AI Dungeon Master](https://mesh-streamlit-demo.factset.io/)

## Prerequisites

You should already have these things done - but just in case...

- Download VSCode for Windows [here](https://code.visualstudio.com/download)
    - Set up VSCode profile
        - Download the VSCode profile [vscodeProfile\Mesh-Python.code-profile](vscodeProfile\Mesh-Python.code-profile)
        - Within VSCode, Navigate to `File > Preferences > Profiles (default) > Import Profile`
        - Select profile file

- [Git Setup](https://github.factset.com/FactSet/training-us-core/blob/master/presentations/fds-configuration/configuration.md#git-setup)
    - Make sure to clone *this* repository with `git clone git@github.factset.com:FactSet/mesh-hackathon-ai.git`
- Install Python
    - This can be done through the [python download site](https://www.python.org/downloads/), windows store, or wherever python can be found

## MESH Hackathon Environment Set-Up Guide

Welcome. Before you get hacking, you'll need to set up your environment. If you haven't already done so, clone this repo into your `C:\Users\{user}\git\` folder. Once in the correct location via terminal, use the command `git clone git@github.factset.com:FactSet/mesh-hackathon-ai.git`. Open up VS Code and open the new folder that was created.

The following commands will be typed into your console down below. If you don't see a console, ``Ctrl + Shift + ` `` will open one up. Double check that you are in the `git\mesh-hackathon-ai` folder.


### 1. Create your own python environment

You should only ever have to run this command once: `python -m venv env`

### 2. Make sure VSCode acknowledges the environment

1. Press `Ctrl + Shift + P`
2. Navigate to `Python: Select Interpreter`
3. Select `Python 3.12 ('env':venv)`

### 3. Activate your environment

This can be done by either typing `.\env\Scripts\activate` or by opening up a new powershell terminal (The shortcut to open a new terminal is ``Ctrl + Shift + ` ``).

Either way, your console should now have a green `(env)` on your current line:

![env_activated](doc_images/env_activated.png)

### 4. Install the requirements of your environment

run `pip install -r requirements.txt`. This might take a few seconds.

### 5. Create a new team branch

First, decide on a team name. Then, run the following:

`git checkout -b mesh<YYYY>/<your_team_name_here>`

Where 
- `<YYYY>` is the current year. (ex `2024`) and 
- `<your_team_name_here>` is your team name. (ex `dogs_are_cool`)

### 6. Run your new project!

`streamlit run app.py`

Click the `localhost` link in the console to see your project. Take 10 minutes to mess around with the project on your own. 

Challenges:
- [ ] Can change the chat message without reloading the page? 
- [ ] Can you add a second message?

## Making the First Updates to Your Project

From here on out, all team members will be working through your team leader's machine. Nominate one person to "drive" VSCode. Other team members will either pair program or use the live share extension to add their changes live.

### Documentation

Documentation is super important. For that reason, the very first thing you'll need to do is edit your [our-project.md](our-project.md). For right now, complete the following:

- Update Team Name
- Update Team Members
- Update the Date

The hardest thing after *creating* documentation is *updating* documentation. Don't forget to update your `our-project.md` file once your know more about your hackathon project. Feel free to add more sections and screenshots. For right now, feel free to leave it as is.

### Making Your First Commit

After updating your `our-project.md` file, it's time to commit the changes. 

**First, double check you are own your own branch!**

In the bottom left of your VSCode, it should look like the following:

![correct_branch](doc_images/correct_branch.png)

It should *not* say `main`. If it does, click it and change it to your team branch.

**Next**, go to the version control tab of VSCode and...
1) Stage the changes

    ![stage_changes](doc_images/stage_changes.png)

2) Add a commit message and commit the changes

    ![commit_changes](doc_images/commit_changes.png)

3) Finally, sync the changes by pressing the button

    ![sync_changes](doc_images/sync_changes.png)

You'll have to do this every time you make changes before you can share your app with others. Try to commit every hour. In case something goes wrong, you can always revert your code to a previous commit. If it is your first time committing, ask a FactSetter for your project's URL. Fill in the below URL with your team-specific URL:

Our internal project URL is: [mesh-hackathon-pr-XX.factset.io](https://mesh-hackathon-pr-XX.factset.io)

## Creating a LLM Chat App

Your hackathon officially starts now! For the first half of the hackathon, you will be following a guide to get you started. That guide is here: [Build a Basic LLM Chat App](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps). 

Read through the guide with your team and use its examples to build a basic chat app. The article has example code to guide you, but you will need to understand the platform if you want to build a cool, personalized hackathon project!

### Changes

There are a small amount of changes you will need to make in the latter half of the project.

- Imports should already be handled for you. You shouldn't need to add them again.
- In the Step "**Add OpenAI API key to Streamlit secrets**" section, we will be adding our `OPENAI_API_KEY` to our `.env` file instead. Ask a FactSetter for your API Key. Once the key is added, add '`.env`' to your `.gitignore` file.

- In the step: "**Write the App**", replace the code
    ```
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    ```
    with the following
    ```
    client = AzureOpenAI(
        api_version="2024-02-01",
        azure_endpoint=os.getenv("OPENAI_API_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    ```
    This is specific to how FactSet gets openapi keys

## Creating Your Own AI Expert

The most simple thing to do to customize your AI model is to add a *system prompt*. A system prompt is sent along with chat history to provide additional instruction to guide the model's behavior. It is intended to be shared across all prompts of a similar nature.

By this time, you are likely already familiar with "assistant" and "user" prompts. Similarly, you also can provide a "system prompt"

```python
messages = [
    {
        "role": "system",
        "content": "You are a dog - and as a dog, you are unable to speak normally. Instead, respond in appropriate dog noises to reflect your answer"
    },{
        "role": "user",
        "content" "How are you doing today?"
    },{
        "role": "assistant",
        "content": "*Wags tail happily and barks twice*"
    },{
        "role": "user",
        "content" "Who's a good boy?"
    }
]
```

Give your AI a system prompt. Experiment with different phrasing and detail. You can always use the [chat.factset.io playground](https://chat.factset.io/playground) to test your prompt for your intended output.

## Stretch Goals

- Customize your Streamlit Page
    - Page Title
    - Icons
    - Sound
    - Updating Documentation
    - ([Streamlit cheatsheet](https://cheat-sheet.streamlit.app/))
- Advanced Prompt Engineering
- Prompt Robustness


## Helpful Resources:

Streamlit cheatsheet:
 - https://cheat-sheet.streamlit.app/
