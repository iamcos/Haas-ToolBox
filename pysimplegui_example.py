import PySimpleGUI as sg      
"""      
Demonstrates using a "tight" layout with a Dark theme.      
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled      
states for buttons and changes the text color to show greyed-out (disabled) buttons      
"""      

sg.ChangeLookAndFeel('Dark')      
sg.SetOptions(element_padding=(0,0))      

layout = [[sg.T('User:', pad=((3,0),0)), sg.OptionMenu(values = ('User 1', 'User 2'), size=(20,1)), sg.T('0', size=(8,1))],      
          [sg.T('Customer:', pad=((3,0),0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20,1)), sg.T('1', size=(8,1))],      
          [sg.T('Notes:', pad=((3,0),0)), sg.In(size=(44,1), background_color='white', text_color='black')],      
          [sg.Button('Start', button_color=('white', 'black'), key='Start'),      
            sg.Button('Stop', button_color=('white', 'black'), key='Stop'),      
            sg.Button('Reset', button_color=('white', 'firebrick3'), key='Reset'),      
            sg.Button('Submit', button_color=('white', 'springgreen4'), key='Submit')]      
          ]      

window = sg.Window("Time Tracker", layout, default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False, default_button_element_size=(12,1), finalize=True)      

window['Stop'].update(disabled=True)      
window['Reset'].update(disabled=True)      
window['Submit'].update(disabled=True)      
recording = have_data = False      
while True:      
    event, values = window.read()      
    print(event)      
    if event == sg.WIN_CLOSED:
        exit(69)      
    if event is 'Start':      
        window['Start'].update(disabled=True)      
        window['Stop'].update(disabled=False)      
        window['Reset'].update(disabled=False)      
        window['Submit'].update(disabled=True)      
        recording = True      
    elif event is 'Stop'  and recording:      
        window['Stop'].update(disabled=True)      
        window['Start'].update(disabled=False)      
        window['Submit'].update(disabled=False)      
        recording = False      
        have_data = True      
    elif event is 'Reset':      
        window['Stop'].update(disabled=True)      
        window['Start'].update(disabled=False)      
        window['Submit'].update(disabled=True)      
        window['Reset'].update(disabled=False)      
        recording = False      
        have_data = False      
    elif event is 'Submit'  and have_data:      
        window['Stop'].update(disabled=True)      
        window['Start'].update(disabled=False)      
        window['Submit'].update(disabled=True)      
        window['Reset'].update(disabled=False)      
        recording = False  