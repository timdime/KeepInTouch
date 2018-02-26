#!/bin/bash
ProgramName="Keep in Touch"
                                                                                                
dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd):imessage.png"
dir=${dir////:}

group=$1
name=$2
number=$3
sentence=$4

osascript <<EOD                                                                                                                                                                           
 tell application "Finder"
        activate
                (display dialog "To: $name @$number\niMessage: $sentence" ¬
                        with title "$ProgramName with $group" ¬
                        with icon file "$dir" ¬
                        buttons {"Send", "Retry", "Exit"} ¬
                        default button 1)
 end tell
                if result = {button returned:"Send"} then
                        tell application "Messages"
                          set targetService to 1st service whose service type = iMessage
                          set targetBuddy to buddy "$number" of targetService
                          send "$sentence" to targetBuddy
                        end tell
                else if result = {button returned:"Retry"} then
                        do shell script "python ./KeepInTouch.py ~"
                else
                        (display dialog "$ProgramName Canceled. Exiting..." ¬
                        with title "$ProgramName" ¬
                        buttons {"OK"} ¬
                        giving up after 2)
                end if
EOD


