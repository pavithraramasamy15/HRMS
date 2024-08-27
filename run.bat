@echo off
REM Run Behave with specified options
behave --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results
