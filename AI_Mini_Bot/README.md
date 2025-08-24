# AI minibot is a  random mini-project of Farhaz Khondoker. 
Here are the steps to run and execute the program -
# MiniBot -- Run via Command Prompt (Windows)

This guide explains how to set up and run the **MiniBot** project
locally on your PC using **Command Prompt (CMD)**.

------------------------------------------------------------------------

## 1. Extract the Project

1.  Locate the file: **`minibot_web.zip`**
2.  Right-click → **Extract All** → Choose a folder (e.g.,
    `C:\Users\YourName\Documents\minibot_web`)

------------------------------------------------------------------------

## 2. Open Command Prompt

1.  Press **Win + S** → type `cmd` → press **Enter**
2.  Navigate to the project folder:

``` cmd
cd C:\Users\YourName\Documents\minibot_web
```

------------------------------------------------------------------------

## 3. Set Up Python Environment (Recommended)

### Create a virtual environment:

``` cmd
python -m venv .venv
```

### Activate it:

``` cmd
.venv\Scripts\activate
```

(You'll see `(.venv)` appear before your prompt)

------------------------------------------------------------------------

## 4. Install Required Packages

``` cmd
pip install -r requirements.txt
```

This installs: - **Flask** -- for the web server\
- **Flask-Session** -- to store memory in sessions

------------------------------------------------------------------------

## 5. Run the MiniBot

``` cmd
python app.py
```

You should see something like:

    * Running on http://127.0.0.1:5000

------------------------------------------------------------------------

## 6. Open the Web App

-   Open your browser\
-   Go to: **http://127.0.0.1:5000**

Start chatting! Type messages in the input box, press **Enter**, and
MiniBot will reply.
![Mini Bot running in Web](AI_Mini_Bot/static/minibot.png)

------------------------------------------------------------------------

## 7. Stop the Server

-   Go back to the CMD window\
-   Press **Ctrl + C** to stop the bot.

------------------------------------------------------------------------

## Extra (Optional)

-   To run in the background:\

``` cmd
python app.py &
```

-   To deactivate the virtual environment:\

``` cmd
deactivate
```

------------------------------------------------------------------------

### Project Files

-   **`app.py`** -- Main Flask app handling chatbot logic and routes\
-   **`templates/index.html`** -- Frontend interface for chatting\
-   **`static/styles.css`** -- Basic styling for the chat interface\
-   **`static/script.js`** -- Manages chat interactions via AJAX

------------------------------------------------------------------------

Your **MiniBot** is now ready to chat locally --- like a mini ChatGPT!

