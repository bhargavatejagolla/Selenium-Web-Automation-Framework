@echo off
echo 🚀 Starting Cross-Browser Test Execution...
echo =========================================

for %%b in (chrome edge firefox) do (
    echo ▶️ Running tests on: %%b
    echo -----------------------------------------
    pytest --browser=%%b -m regression --html=reports/report_%%b.html --self-contained-html
    if errorlevel 1 (
        echo ❌ Tests FAILED on %%b
    ) else (
        echo ✅ Tests PASSED on %%b
    )
    echo.
)

echo =========================================
echo ✅ Cross-browser execution complete!
echo Reports saved to:
echo   - reports\report_chrome.html
echo   - reports\report_edge.html
echo   - reports\report_firefox.html
pause
