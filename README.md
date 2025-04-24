# Setup in VS Code
## Backend
In a *Command Prompt*, install *Python* using `winget`.

Run the following to get the available versions of *Python*.
```
winget search --id Python.Python
```
```
C:\Users\ricky\code\AzureStorageTableDemoSite> winget search --id Python.Python
Name        Id                 Version   Source
------------------------------------------------
Python 2    Python.Python.2    2.7.18150 winget
Python 3.0  Python.Python.3.0  3.0.1     winget
Python 3.1  Python.Python.3.1  3.1.4     winget
Python 3.10 Python.Python.3.10 3.10.11   winget
Python 3.11 Python.Python.3.11 3.11.9    winget
Python 3.12 Python.Python.3.12 3.12.10   winget
Python 3.13 Python.Python.3.13 3.13.3    winget
Python 3.2  Python.Python.3.2  3.2.5     winget
Python 3.3  Python.Python.3.3  3.3.5     winget
Python 3.4  Python.Python.3.4  3.4.4     winget
Python 3.5  Python.Python.3.5  3.5.4     winget
Python 3.6  Python.Python.3.6  3.6.8     winget
Python 3.7  Python.Python.3.7  3.7.9     winget
Python 3.8  Python.Python.3.8  3.8.10    winget
Python 3.9  Python.Python.3.9  3.9.13    winget
```

Run the following to install *Python*.
```
winget install -e --id Python.Python.3.13
```

In a *Command Prompt*, run the following in the `Backend` folder to create a *Python virtual environment*.
```
python -m venv .venv
```

Run the following to activate the virtual environment.
```
.venv\Scripts\activate
```

Run the following to restore all packages in the virtual environment.
```
pip install -r .\requirements.txt
```

Open *VS Code* in the `Backend` folder.
```
C:\Users\ricky\code\AzureStorageTableDemoSite\Backend> code .
```

In *VS Code*, install the `Python` extension. 

Start debugging in *VS Code*. Select a *Python* interpreter and select the option to run a *FastAPI* web application. You can now navigate to `http://localhost:8000` to browse the app.
