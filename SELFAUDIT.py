from tkinter import * 
import tkinter as tk
from tkinter import messagebox

def TermsAndServices():
    window = Tk()
    window.title("TERMS AND CONDITIONS")    
    window.withdraw()
    if messagebox.askyesno('TERMS AND SERVICES', """
Please read these terms of service carefully before agreeing.

Conditions of Use
SELFAUDIT is subject to the conditions stated below in this document. Every time you use SELFAUDIT, you accept the following conditions by clicking "YES".

Condition
By utilizing SELFAUDIT, you agree that SELFAUDIT does not replace the assurance of information security and regulatory compliance. This tool may be used to better understand the questions your team can potentially ask themselves to minimize risk in each category this tool offers.""", icon='error') == True:

        main()
    else:
        messagebox.showerror("ERROR","This program is not made to be used prior to agreeing to the terms and services.")
        TermsAndServices()
    window.deiconify()
    window.destroy()
    window.quit()

    
def change(*args):
    global var
    if var.get() == "Antivirus":
        AUDITTIME(1)
    elif var.get() == "Backup":
        AUDITTIME(2)
    elif var.get() == "Change/Patch Management":
        AUDITTIME(3)
    elif var.get() == "Cybersecurity":
        AUDITTIME(4)
    elif var.get() == "GLBA Review":
        AUDITTIME(5)
    elif var.get() == "IT Management":
        AUDITTIME(6)
    elif var.get() == "IT Operations":
        AUDITTIME(7)
    elif var.get() == "Network Access Procedure":
        AUDITTIME(8)
    elif var.get() == "Network Architecture":
        AUDITTIME(9)
    elif var.get() == "Network Operating System Security":
        AUDITTIME(10)
    elif var.get() == "Physical Security":
        AUDITTIME(1)
    elif var.get() == "Red Flag Compliance":
        AUDITTIME(12)
    elif var.get() == "Social Engineering (E-MAIL)":
        AUDITTIME(13)
    elif var.get() == "Social Engineering (IN PERSON)":
        AUDITTIME(14)
    elif var.get() == "Social Engineering (VOICE)":
        AUDITTIME(15)
    elif var.get() == "Social Media":
        AUDITTIME(16)
    elif var.get() == "Software Compliance":
        AUDITTIME(17)
    elif var.get() == "Workstations":
        AUDITTIME(18)
    elif var.get() == "Wireless Analysis":
        AUDITTIME(19)
        
def AUDITTIME(choiceMade):
    if (choiceMade == 1):
        currentlyOn = "ANTIVIRUS"
    elif (choiceMade == 2):
        currentlyOn = "BACKUP"
    elif (choiceMade == 3):
        currentlyOn = "ChangePatchManagement"
    elif (choiceMade == 4):
        currentlyOn = "Cybersecurity"
    elif (choiceMade == 5):
        currentlyOn = "GLBAReview"
    elif (choiceMade == 6):
        currentlyOn = "ITManagement"
    elif (choiceMade == 7):
        currentlyOn = "ITOperations"
    elif (choiceMade == 8):
        currentlyOn = "NetworkAccessProcedure"
    elif (choiceMade == 9):
        currentlyOn = "NetworkArchitecture"
    elif (choiceMade == 10):
        currentlyOn = "NetworkOperatingSystemSecurity"
    elif (choiceMade == 11):
        currentlyOn =  "PhysicalSecurity"
    elif (choiceMade == 12):
        currentlyOn = "RedFlagCompliance"
    elif (choiceMade == 13):
        currentlyOn = "SocialEngineeringEMAIL"
    elif (choiceMade == 14):
        currentlyOn = "SocialEngineeringINPERSON"
    elif (choiceMade == 15):
        currentlyOn = "SocialEngineeringVOICE"
    elif (choiceMade == 16):
        currentlyOn = "SocialMedia"
    elif (choiceMade == 17):
        currentlyOn = "SoftwareCompliance"
    elif (choiceMade == 18):
        currentlyOn = "Workstations"
    elif (choiceMade == 19):
        currentlyOn = "WirelessAnalysis"

    TRUE = []
    FALSE = []
    QUESTIONS = []

    file = str('questions/'+currentlyOn+'Questions.txt')
    with open(file) as f:
        QUESTIONS = f.read().splitlines()

        numOfQuestions = len(QUESTIONS)
        TRUE = [False] * numOfQuestions
        FALSE = [False] * numOfQuestions
        clickLength = (numOfQuestions * 2)
        click = list(range(0,clickLength))

    resultFile = str('results/'+currentlyOn+'_RESULTS.txt')
    with open(resultFile, 'w') as file:
        file.write("")
    
    currentClick = 0
    for generate in range(0, numOfQuestions, 1):
        
        follow = str(generate + 1)
        follow2 = str(numOfQuestions)
        TEST = str(currentlyOn+" AUDIT - QUESTION " + follow + " / " + follow2)
        
        QUESTION = str(QUESTIONS[generate])
        generate = str(generate)
        
        if messagebox.askyesno(TEST, QUESTION) == True:

            with open(resultFile, 'a') as file:
                file.write(QUESTION) and file.write("\nYES\n \n")
        else:
            with open(resultFile, 'a') as file:
                file.write(QUESTION) and file.write("\nNO\n \n")
        if (follow == follow2):
            messagebox.showinfo(currentlyOn+" AUDIT", message='Thanks for completing '+currentlyOn+' AUDIT. Test has been saved in: '+ resultFile)


  
def main():
    global var
    global root
    root = tk.Tk()
    root.title("SELF AUDIT")
    theLabel = Label(root, text="""SELF AUDIT
A tool that allows you to focus on critical questions to ask about your operation that minimizes risk.

            
"YES" = PASS
"NO" = FAIL

                     """)
    theLabel.pack()
    OPTIONS = [
        "Antivirus",
        "Backup",
        "Change/Patch Management",
        "Contingency Planning",
        "Cybersecurity",
        "GLBA Review",
        "IT Management",
        "IT Operations",
        "Network Access Procedure",
        "Network Architecture",
        "Network Operating System Security",
        "Physical Security",
        "Red Flag Compliance",
        "Social Engineering (E-MAIL)",
        "Social Engineering (IN PERSON)",
        "Social Engineering (VOICE)",
        "Social Media",
        "Software Compliance",
        "Workstations",
        "Wireless Analysis",
        ]
    var = tk.StringVar(root)
    var.trace("w", change)
    dropDownMenu = tk.OptionMenu(root, var, OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3], OPTIONS[4], OPTIONS[5], OPTIONS[6],OPTIONS[7], OPTIONS[8], OPTIONS[9], OPTIONS[10], OPTIONS[11], OPTIONS[12], OPTIONS[13], OPTIONS[14], OPTIONS[15], OPTIONS[16], OPTIONS[17],OPTIONS[18], OPTIONS[19] )
    dropDownMenu.pack()
    root.mainloop()

TermsAndServices()
