Write-Host "[1/3] Django system check..."
python manage.py check

Write-Host "[2/3] Syntax lint (compileall)..."
python -m compileall apps config common

Write-Host "[3/3] Running test suite..."
python manage.py test

Write-Host "Backend verification completed."