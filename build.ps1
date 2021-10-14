try { 
    #.\.venv\Scripts\deactivate.bat
    deactivate
}
catch { }

.\.venv\Scripts\activate.ps1
python -m pip install -r .\requirements.txt