@echo off
REM Skip first three lines (header stuff), then pass it to sort so we don't have to hit space in more.
REM (also, sorting is nice).
tasklist | more +3 | sort
