import logins
import time
from datetime import datetime
from swissparts import *
from millparts import *
from latheparts import *
from tkinter import *
from PIL import ImageTk,Image
loginlogfile = 'logs/logins/logintimesanddates.txt'
checks = 'logs/checks/checks.txt'

#initialize the root home center window, make it go away and bring up the login screen
root = Tk()
root.withdraw()
log = Toplevel()



#define the protocol for the user closing the window using OS window manager, and kill the program after its clicked
log.protocol("WM_DELETE_WINDOW", root.destroy)



#Authorization check, making sure username and password are valid
# writing into the logintimesanddates file the time and date login was executed and by who



def check_auth():
	"""Authenticating username and password, then bring user to Home Center """
	global checkuser #THE ONE AND ONLY GLOBAL VARIABLE IN THE WHOLE PROGRAM.
	checkuser = user.get()
	
	
	checkpass = password.get()
	if checkuser.strip() in logins.logins: 
		if checkpass.strip() in logins.logins.values():
			logtimedate = datetime.now()
			with open(loginlogfile,'r') as checksizefile:
				checksize = len(checksizefile.readlines())
				print(f'Login count:{checksize}')
				checksizefile.close()
			if checksize > 1000:
				with open(loginlogfile,'w') as clear:
					clearpad = clear.write('')
					checksize = 0
					clear.close()

			with open(loginlogfile, 'a') as f:
				enterlogtime = f.write(f'User:{checkuser} LogOn:{logtimedate}\n')
				f.close()
			loginbutton = Button(log,text='Success!', state=DISABLED, pady=12,padx=9)
			loginbutton.place(x=516,y=250)
			
			log.destroy()
			root.title(f'Home Center - User: {checkuser}')
			root.deiconify()
	
#define the screen login windows attributes, define all buttons used on login screen
log.title('SuperiorLog')
log.geometry('850x500+500+200')
log.resizable(False, False)
log.configure(bg='#b8b7b6')
logo = ImageTk.PhotoImage(Image.open('imgs/logo.png'))
placelogo = Label(log,image=logo, bg='#b8b7b6')
placelogo.place(x=285,y=150)

userlab = Label(log,text ='Employee ID:',bg='#dedcdb')
passlab = Label(log,text ='Password:',bg='#dedcdb')

loginbutton = Button(log,text='Login',bg='#dedcdb',command=check_auth,pady=12,padx=9)
user = Entry(log,width='30',bg='#dedcdb')
password = Entry(log,width='30',bg='#dedcdb')
user.place(x=330,y=250)
password.place(x=330, y=275)
userlab.place(x=254,y=248)
passlab.place(x=270,y=273)
loginbutton.place(x=516,y=250)





#END OF LOGIN SCREEN
#--------------------------------------------------------------------


#the cnc panel 'screen'
screen = ImageTk.PhotoImage(Image.open('imgs/screen.png'))
coffee_break = ImageTk.PhotoImage(Image.open('imgs/coffee.png'))
assist_james = ImageTk.PhotoImage(Image.open('imgs/assist.jpg'))
ncguiswiss = ImageTk.PhotoImage(Image.open('imgs/ncguiswissfinal.png'))
ncguilathe = ImageTk.PhotoImage(Image.open('imgs/ncguilathefinal.png'))
ncguimill = ImageTk.PhotoImage(Image.open('imgs/ncguimillfinal.png'))
ncguiblast = ImageTk.PhotoImage(Image.open('imgs/ncguiblastfinal.png'))
ncguiother = ImageTk.PhotoImage(Image.open('imgs/ncguiotherfinal.png'))

#class for cnc session windows
class SessionWindow:
	"""PARENT CLASS FOR CNC PANEL WINDOWS"""
	def __init__(self, master):
		"""Initialize all buttons and screen on panels"""
		self.master = master
		def disable_close():
			pass
		def ask_exit_if_sure():
			confirm_exit_window = Toplevel(self.master)
			self.master.protocol("WM_DELETE_WINDOW", disable_close)
			confirm_exit_window.geometry('260x120+850+450')
			confirm_exit_window.title(f'User: {checkuser}')
			confirm_exit_window.resizable(False,False)
			confirm_exit_window.configure(bg='#b8b7b6')
			exit_desc = Label(confirm_exit_window, font=('Yu Gothic UI Light',13),bg='#b8b7b6',text= 'Are you sure you want to exit?\nAll unsaved progress will be lost.').place(x=9,y=10)
			def user_wants_to_stay():
				confirm_exit_window.destroy()
				self.master.protocol("WM_DELETE_WINDOW", ask_exit_if_sure)

			exit_yes = Button(confirm_exit_window, text = 'Yes',font=('Yu Gothic UI Light',13),bg='#dedcdb', command = lambda:self.master.destroy(), padx=12,pady=1,borderwidth=3).place(x=60,y=70)
			exit_no = Button(confirm_exit_window, text='Cancel', command = user_wants_to_stay,font=('Yu Gothic UI Light',13),bg='#dedcdb',borderwidth=3).place(x=140,y=70)
			confirm_exit_window.protocol("WM_DELETE_WINDOW", user_wants_to_stay)
		
		#initialize cnc panel window dimensions and protocol for red x button
		self.master.protocol("WM_DELETE_WINDOW", ask_exit_if_sure)
		self.master.geometry('1000x550+50+50')
		self.master.resizable(False, False)
		
		
		
		
		self.screen_position= Label(self.master, image=screen)
		
		
		#self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
		#self.notreadyscreen = Label(self.master, text = 'NOT READY', font = ('System', 16),fg='orange',bg='#464047')
		#self.setupscreen = Label(self.master, text = 'SETUP',font = ('System', 16),fg='green', bg='#464047')
		#self.break_screen = Label(self.master, text = f'BREAK',font = ('System', 16),fg='green', bg='#464047')
		#self.assist_screen = Label(self.master, text = f'ASSISTING',font = ('System', 16),fg='green', bg='#464047')
		#self.check_screen = Label(self.master, text = 'CHECK ACTIVE',font = ('System', 16),fg='green', bg='#464047')
		#self.maint_screen = Label(self.master, text='MAINT.',font = ('System', 16),fg='green', bg='#464047')
		#self.prod_screen = Label(self.master, text = '!RUNNING', font = ('System', 16),fg='green', bg='#464047')
		


			
			#cnc panel buttons
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED)
		self.prod_pause_button = Button(self.master, text = ';', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='red',fg='white',state = DISABLED)
		self.home_button = Button(self.master, text = 'i', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state = DISABLED)

		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state=NORMAL)
		
		self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
		self.report_bug_button = Button(self.master, text = 's', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, command=lambda: self.report_a_bug())



#function for submitting your bug report.
	def submit_bug_report(self, bugentry):
		"""Check to see if anything was entered, if not: just close the window. If so: log the date of the entry and then put the entry and date in bug report file """
		try:
			self.bugreportfile = 'logs/admintools/bug_reports.txt'
			self.reportdate = datetime.now().date()
			self.bugentry = bugentry
		
			if not len(self.bugentry):
				self.bugreportwind.destroy()
			else:
			
				with open(self.bugreportfile, 'a') as bug:
					self.writereport = bug.write(f'{self.reportdate}: {bugentry}\n\n')
					bug.close()
					self.bugreportwind.destroy()
		except :
			print('Error: Report already submitted')
			
			self.bugreporterror = Toplevel()
			self.bugreporterror.protocol("WM_DELETE_WINDOW", self.bugreporterror.destroy)
			self.bugreporterror.geometry('270x120+700+500')
			self.bugreporterror.configure(bg='#b8b7b6')
			self.bugreporterror.title('Error')
			self.bugreporterrormessage = Label(self.bugreporterror,bg='#b8b7b6',text="\nError: Report already submitted.\n\nPlease close all 'Report an Issue or Bug' \nwindows, and try again.\n")
			self.bugreporterrormessage.pack()
			self.bugreporterrorbutton = Button(self.bugreporterror,bg='#dedcdb',text='OK', command =self.bugreporterror.destroy,padx=20,pady=40)
			self.bugreporterrorbutton.pack()
		finally:
			self.report_bug_button.destroy()
			self.report_bug_button = Button(self.master, text = 's', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, command=lambda: self.report_a_bug())
			self.report_bug_button.place(x=895, y=30)
		


		
	

#defining the bug report window for the machine panel
	def report_a_bug(self):
		"""Make bug report window so user can report any bugs that they encounter"""
		self.report_bug_button.destroy()
		self.report_bug_button = Button(self.master, text = 's', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state=DISABLED)
		self.report_bug_button.place(x=895, y=30)
		self.bugreportwind = Toplevel(self.master) #define the window
		def restore_report():
			self.bugreportwind.destroy()
			self.report_bug_button = Button(self.master, text = 's', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, command=lambda: self.report_a_bug())
			self.report_bug_button.place(x=895, y=30)
		self.bugreportwind.protocol("WM_DELETE_WINDOW", restore_report) 
		self.bugreportwind.title(f'Report an Issue or Bug - User: {checkuser}')
		self.bugreportwind.geometry('1000x300+450+400')
		self.bugreportwind.configure(bg='#b8b7b6')
		self.bugreportwind.resizable(False, False)
		self.bugreportgreet = Label(self.bugreportwind, text= 'SuperiorLog apologizes for interrupting your productivity.',bg='#b8b7b6', font=('Yu Gothic UI Semibold',20))
		self.bugreportgreet.place(x=15,y=30)
		self.bugreportgreetsub = Label(self.bugreportwind,bg='#b8b7b6', text="Below, give a descriptive report of your problem or suggestion. Keep your entry brief, but don't exclude any important details!\n*Note: All user entries are anonymous.",font=('Yu Gothic UI Light',12), justify = 'left')
		self.bugreportgreetsub.place(x=15,y=80)
		self.bugreportinput = Entry(self.bugreportwind, width=165, relief= SUNKEN, borderwidth=2, bg='#dedcdb')
		self.bugreportinput.place(x=1, y=148)
		self.bugreportgreetconclude = Label(self.bugreportwind,bg='#b8b7b6', text='Thank you for sharing your feedback. Reporting any issues, bugs, and even suggestions \nhelps SuperiorLog become a better serving tool for the user.', justify='left',font=('Yu Gothic UI Semilight',12))
		self.bugreportgreetconclude.place(x=20,y=200)
		self.submitreportbugbutton = Button(self.bugreportwind,bg='#dedcdb',text='Submit Report', padx=20, pady=5, command =lambda:self.submit_bug_report(self.bugreportinput.get()))
		self.submitreportbugbutton.place(x=800,y=200)


	def load_number(self,userentry):
		"""Match part number with part on list then bring up info for that part"""
		for i in partnumbers:
			if userentry == i:
				placehold = partnumbers.index(userentry)
				timecycle = cycletimes[placehold]
				
				timesetup = setuptimes[placehold]

				formatpartinfolist = [userentry,timecycle,timesetup]
				print(f'\nPart {userentry} successfully loaded!')
				print(f'Cycle: {timecycle} seconds')
				print(f'Setup: {timesetup} minutes')
				try:
					self.new_part_window.destroy()
					self.clear_panel_buttons()
					self.restore_panel_buttons()
					
				except:
					print('Error: Bad session target. USER: IF WINDOW REFUSES TO CLOSE, EXIT SUPERIORLOG AND RUN SOFTWARE AGAIN.')

				finally:
				
					return formatpartinfolist
					
				



				

	#window to enter new part number during set up operation
	def new_part(self):
		"""Open a window to prompt user to input part number"""
		self.setup_button.destroy()
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state=DISABLED)
		self.setup_button.place(x=670, y=275)
		self.new_part_window = Toplevel(self.master)
		self.new_part_window.geometry('350x200+700+400')
		self.new_part_window.title(f'Load New Part - User: {checkuser}')
		self.new_part_window.configure(bg='#b8b7b6')
		self.new_part_window.resizable(False,False)
		def restore_setup():
			"""Allow the set up button to become functional again after closing the new part window"""
			self.setup_button.destroy()
			self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state=NORMAL, command = lambda:self.new_part())
			self.new_part_window.destroy()
			self.setup_button.place(x=670, y=275)
		self.new_part_window.protocol("WM_DELETE_WINDOW", restore_setup)
		self.explainusernewpart = Label(self.new_part_window, text='Enter part number:', font=('Yu Gothic UI Light',20),bg='#b8b7b6')
		self.explainusernewpart.place(x=3,y=5)

		self.userenterpartnum = Entry(self.new_part_window, borderwidth=2,)
		self.userenterpartnum.place(x=112,y=90)
		
		
		self.submitpartnum = Button(self.new_part_window,text='Submit and begin set-up',command=lambda:self.load_number(self.userenterpartnum.get()))
		self.submitpartnum.place(x=106,y=127)

	def set_up(self): 
		"""define the function for the setup button"""
		self.set_up_time = time.time()
		self.setup_window = Toplevel(self.master)
		self.setup_button.destroy()
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state=DISABLED)
		self.setup_button.place(x=670, y=275)
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED)
		self.prod_start_button.place(x=725, y=450)
		self.setupscreen = Label(self.master, text = 'SETUP',font = ('System', 16),fg='green', bg='#464047')
		self.setupscreen.place(x=105,y=260)
		
		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
		self.assist_button.place(x=895, y=200)
		self.readyscreen.destroy()
		self.notreadyscreen = Label(self.master, text = 'NOT READY', font = ('System', 16),fg='orange',bg='#464047')
		self.notreadyscreen.place(x=370,y=220)

		self.setup_window.configure(bg='#b8b7b6')
		self.setup_window.resizable(False,False)
		self.setup_window.title(f'Set-up - User: {checkuser} ')
		self.setup_window.geometry('340x395+475+400')
		def setup_button_restore():
			try:
				self.leave_set_up = time.time()
				setup_calc = self.leave_set_up - self.set_up_time
				addsetup2 = self.session_setup_time + setup_calc
				self.session_setup_time = addsetup2
				print(f'Time in set-up (seconds): {self.session_setup_time}')
				self.setupscreen.destroy()	
				self.setup_window.destroy()
				self.setup_button.destroy()
				
				self.prod_start_button.destroy()
				self.break_button.destroy()
				self.assist_button.destroy()
				self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up())
				self.setup_button.place(x=670, y=275)
				self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = NORMAL,command = lambda:self.start_production())
				self.prod_start_button.place(x=725, y=450)
				self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL,command = lambda:self.break_time())
				self.break_button.place(x=825, y=200)
				self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = NORMAL,command=lambda: self.assist_time())
				self.assist_button.place(x=895, y=200)
				self.notreadyscreen.destroy()
				self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
				self.readyscreen.place(x=310,y=220)


			except:
				print('Error: Bad session target. USER: IF WINDOW REFUSES TO CLOSE, EXIT SUPERIORLOG AND RUN SOFTWARE AGAIN.')
			
		self.setup_window.protocol("WM_DELETE_WINDOW", setup_button_restore)
	
	def home_show_info(self):
		"""Show part information for current session"""
		self.info1 = self.load_number(formatpartinfolist[0])
		self.info2 = self.load_number(formatpartinfolist[1])
		self.info3 = self.load_number(formatpartinfolist[2])
		self.welcomescreen = Label(self.master, text=f'Part: {self.info1}\n Cycle (seconds): {self.info2}\n Set-up (minutes): {self.info3}', font=('System',16), fg='green')


		self.welcomescreen.place(x=236,y=200)
	
	def start_production(self):
		self.production_go = time.time()
		self.prod_start_button.destroy()
		self.prod_pause_button.destroy()
		self.setup_button.destroy()
		self.break_button.destroy()
		self.assist_button.destroy()
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED)
		self.prod_start_button.place(x=725, y=450)
		self.prod_pause_button = Button(self.master, text = ';', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='red',fg='white',state = NORMAL, command = lambda:self.pause_production())
		self.prod_pause_button.place(x=850, y=450)
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
		self.setup_button.place(x=670, y=275)
		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
		self.assist_button.place(x=895, y=200)
		self.setupscreen.destroy()
		self.readyscreen.destroy()
		self.prod_screen = Label(self.master, text = '$PROD. GO', font = ('System', 18),fg='green', bg='#464047')
		self.prod_screen.place(x=310,y=200)
		print(self.production_go)

	def pause_production(self):
		self.production_stop = time.time()
		calc_work_time = self.production_stop - self.production_go
		print(self.production_stop)
		print(f'production time:{calc_work_time}')
		add_work = self.session_work_count + calc_work_time
		self.session_work_count = add_work
		print(f'Time in production (seconds): {self.session_work_count}')
		self.production_go = 0
		self.production_stop = 0
		self.prod_start_button.destroy()
		self.prod_pause_button.destroy()
		self.setup_button.destroy()
		self.break_button.destroy()
		self.assist_button.destroy()
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = NORMAL,command=lambda:self.start_production())
		self.prod_start_button.place(x=725, y=450)
		self.prod_pause_button = Button(self.master, text = ';', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='red',fg='white',state = DISABLED, command = lambda:self.pause_production())
		self.prod_pause_button.place(x=850, y=450)
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=NORMAL)
		self.setup_button.place(x=670, y=275)
		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL,command = lambda:self.break_time())
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = NORMAL,command=lambda: self.assist_time())
		self.assist_button.place(x=895, y=200)
		
		self.prod_screen.destroy()
		self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
		self.readyscreen.place(x=310,y=220)

	def assist_time(self):
		self.assist_start = time.time()
		self.assist_window = Toplevel(self.master)
		self.break_button.destroy()
		self.assist_button.destroy()
		self.setup_button.destroy()
		self.prod_start_button.destroy()
		self.readyscreen.destroy()
		self.notreadyscreen = Label(self.master, text = 'NOT READY', font = ('System', 16),fg='orange',bg='#464047')
		self.notreadyscreen.place(x=370,y=220)
		self.assist_screen = Label(self.master, text = f'ASSISTING',font = ('System', 16),fg='green', bg='#464047')
		self.assist_screen.place(x=240,y=260)
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
		self.setup_button.place(x=670, y=275)

		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED, command = lambda:self.break_time())
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
		self.assist_button.place(x=895, y=200)
		
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED, command = lambda:self.start_production())
		self.prod_start_button.place(x=725, y=450)
		self.assist_window.title(f'Assist in Other Task - User: {checkuser}')
		self.assist_window.geometry('650x300+600+450')
		self.enter_assist_user = Entry(self.assist_window, width = 50,font=('Yu Gothic UI Light',14),borderwidth=3,bg='#dedcdb')
		def end_assist():
			self.assist_stop = time.time()
			self.calc_assist = self.assist_stop - self.assist_start
			add_assist = self.session_assist_time + self.calc_assist
			self.session_assist_time = add_assist
			
			print(self.calc_assist)
			print(f'Assisting time (seconds): {self.session_assist_time}')
			
			self.assist_start = 0
			self.assist_stop = 0
			self.assist_window.destroy()
			self.assist_screen.destroy()
			self.notreadyscreen.destroy()
			self.break_button.destroy()
			self.assist_button.destroy()
			self.setup_button.destroy()
			self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=NORMAL)
			self.setup_button.place(x=670, y=275)
			self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda:self.break_time())
			self.break_button.place(x=825, y=200)
			self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = NORMAL,command=lambda: self.assist_time())
			self.assist_button.place(x=895, y=200)
			self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = NORMAL, command = lambda:self.start_production())
			self.prod_start_button.place(x=725, y=450)
			
			self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
			self.readyscreen.place(x=310,y=220)
			
		self.assist_window.protocol("WM_DELETE_WINDOW", end_assist)
		self.assist_window.configure(bg='#b8b7b6')
		self.assist_window.resizable(False,False)
		show_assist = Label(self.assist_window,image = assist_james,bg='#b8b7b6')
		show_assist.place(x=420, y=35)
		desc_assist = Label(self.assist_window, text='Your skills are needed\non a different task!',font=('Yu Gothic UI Light',26),bg='#b8b7b6', justify='left')
		desc_assist.place(x=15,y=20)
		desc_action = Label(self.assist_window, text="When finished: Write a brief statement\nabout the task, then click the 'Submit' button\nor close this window.",font=('Yu Gothic UI Light',14),bg='#b8b7b6', justify = 'left')
		desc_action.place(x=20,y=115)
		end_assist_button = Button(self.assist_window, text = 'Submit', padx=20,pady=5 ,command = end_assist)
		end_assist_button.place(x=535,y=234)
		self.enter_assist_user.place(x=12,y=234)

	def break_time(self):
		self.break_start = time.time()
		self.break_window = Toplevel(self.master)
		self.break_button.destroy()
		self.assist_button.destroy()
		self.setup_button.destroy()
		self.prod_start_button.destroy()
		self.readyscreen.destroy()
		self.notreadyscreen = Label(self.master, text = 'NOT READY', font = ('System', 16),fg='orange',bg='#464047')
		self.notreadyscreen.place(x=370,y=220)
		self.break_screen = Label(self.master, text = f'BREAK',font = ('System', 16),fg='green', bg='#464047')
		self.break_screen.place(x=170,y=260)
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
		self.setup_button.place(x=670, y=275)

		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED, command = lambda:self.break_time())
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
		self.assist_button.place(x=895, y=200)
		
		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED, command = lambda:self.start_production())
		self.prod_start_button.place(x=725, y=450)
		self.break_window.title(f'Take a Break - User: {checkuser}')
		self.break_window.geometry('650x300+600+450')

		def end_break():
			self.break_stop = time.time()
			self.calc_break = self.break_stop - self.break_start
			add_break = self.session_break_time + self.calc_break
			self.session_break_time = add_break
			print(self.calc_break)
			print(f'Total break time amount: {self.session_break_time}')
			
			self.break_start = 0
			self.break_stop = 0
			self.break_window.destroy()
			self.break_screen.destroy()
			self.notreadyscreen.destroy()
			self.break_button.destroy()
			self.assist_button.destroy()
			self.setup_button.destroy()
			self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=NORMAL)
			self.setup_button.place(x=670, y=275)
			self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda:self.break_time())
			self.break_button.place(x=825, y=200)
			self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = NORMAL,command=lambda: self.assist_time())
			self.assist_button.place(x=895, y=200)
			self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = NORMAL, command = lambda:self.start_production())
			self.prod_start_button.place(x=725, y=450)
			
			self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
			self.readyscreen.place(x=310,y=220)
			
		self.break_window.protocol("WM_DELETE_WINDOW", end_break)
		self.break_window.configure(bg='#b8b7b6')
		self.break_window.resizable(False,False)
		show_coffee = Label(self.break_window,image = coffee_break)
		show_coffee.place(x=445, y=50)
		desc_break = Label(self.break_window, text='Enjoy the break!',font=('Yu Gothic UI Light',36),bg='#b8b7b6')
		desc_break.place(x=15,y=30)
		desc_action = Label(self.break_window, text="When finished: Click the 'Finish Break' button, \nor close this window.",font=('Yu Gothic UI Light',16),bg='#b8b7b6', justify = 'left')
		desc_action.place(x=15,y=110)
		end_break_button = Button(self.break_window, text = 'Finish Break', padx=20,pady=10 ,command = end_break)
		end_break_button.place(x=500,y=230)




	def open_session(self):
		"""Function to load in all buttons and screen for cnc panels"""
		self.master.deiconify()
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, command=lambda: self.new_part())
		
		self.setup_button.place(x=670, y=275)
		self.screen_position.place(x=20,y=50)
		
		self.prod_start_button.place(x=725, y=450)
		self.prod_pause_button.place(x=850, y=450)
		self.home_button.place(x=600, y=275)
		self.check_button.place(x=740, y=275)
		self.break_button.place(x=825, y=200)
		self.assist_button.place(x=895, y=200)
		self.report_bug_button.place(x=895, y=30)
		self.notreadyscreen = Label(self.master, text = 'NOT READY', font = ('System', 16),fg='orange',bg='#464047')
		#REFER TO THESE WHEN PLACING INFO ON PANEL SCREEN
		#self.readyscreen.place(x=310,y=220)
		self.notreadyscreen.place(x=370,y=220)
		#self.setupscreen.place(x=105,y=260)
		#self.break_screen.place(x=170,y=260)
		#self.assist_screen.place(x=240,y=260)
		#self.check_screen.place(x=330,y=260)
		#self.maint_screen.place(x=120,y=285)
		#self.prod_screen.place(x=310,y=200)
		
		self.prod_start_button_title.place(x=729,y=424)
		self.prod_pause_button_title.place(x=863, y=424)
		self.info_button_title.place(x=611, y=250)
		self.setup_button_title.place(x=673, y=250)
		self.check_button_title.place(x=747, y=250)
		self.break_button_title.place(x=832, y=175)
		self.assist_button_title.place(x=899, y=175)
		self.report_bug_button_title.place(x=912, y=7)

		self.ncgui_logo.place(x=19,y=398)




		self.session_work_count = 0
		self.session_not_work_count = 0
		self.session_break_time = 0
		self.session_assist_time = 0
		self.session_setup_time = 0
		self.session_start = time.time()

	def restore_panel_buttons(self):
		"""After loading new part, all buttons stop being disabled"""

		def firstprodstart():
			self.setupend = time.time()
			beggining_setup_time = self.setupend - self.setupstart
			addsetup1 = self.session_setup_time + beggining_setup_time
			self.session_setup_time = addsetup1
			print(f'Time in set-up (seconds): {self.session_setup_time}')
			self.production_go = time.time()
			self.prod_start_button.destroy()
			self.prod_pause_button.destroy()
			self.setup_button.destroy()
			self.break_button.destroy()
			self.assist_button.destroy()
			self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = DISABLED)
			self.prod_start_button.place(x=725, y=450)
			self.prod_pause_button = Button(self.master, text = ';', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='red',fg='white',state = NORMAL, command = lambda:self.pause_production())
			self.prod_pause_button.place(x=850, y=450)
			self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
			self.setup_button.place(x=670, y=275)
			self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
			self.break_button.place(x=825, y=200)
			self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
			self.assist_button.place(x=895, y=200)
			self.setupscreen.destroy()
			self.readyscreen.destroy()
			self.prod_screen = Label(self.master, text = '$PROD. GO', font = ('System', 18),fg='green', bg='#464047')
			self.prod_screen.place(x=310,y=200)
			print(self.production_go)


		self.prod_start_button = Button(self.master, text = '`', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='green',fg='white', state = NORMAL, command = firstprodstart)
		self.prod_start_button.place(x=725, y=450)
		self.prod_pause_button = Button(self.master, text = ';', font=('Webdings', 28), padx=5, pady=5, borderwidth=4, bg='red',fg='white',state = DISABLED, command = lambda:self.pause_production())
		self.prod_pause_button.place(x=850, y=450)
		self.home_button = Button(self.master, text = 'i', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state = NORMAL, command=lambda: self.home_show_info())
		self.home_button.place(x=600, y=275)
		self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=NORMAL)
		self.setup_button.place(x=670, y=275)
		self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda: self.do_a_check())
		self.check_button.place(x=740, y=275)
		self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda:self.break_time())
		self.break_button.place(x=825, y=200)
		self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = NORMAL,command=lambda: self.assist_time())
		self.assist_button.place(x=895, y=200)
		self.report_bug_button = Button(self.master, text = 's', font=('Webdings', 18), padx=1, pady=1, borderwidth=2, state = NORMAL, command=lambda: self.report_a_bug())
		self.report_bug_button.place(x=895, y=30)


	def clear_panel_buttons(self):
		self.prod_start_button.destroy()
		self.prod_pause_button.destroy()
		self.home_button.destroy()
		self.setup_button.destroy()
		self.check_button.destroy()
		self.break_button.destroy()
		self.assist_button.destroy()
		self.report_bug_button.destroy()

	
	


class SwissWindow(SessionWindow):
	"""Child class for swiss window. different part numbers"""

	def __init__(self, master):
		super().__init__(master)
		self.welcomescreen = Label(self.master, text=f"{checkuser.title()}'s New Swiss Session.\nClick the Set-up button to begin.", font=('System',16), fg='green', justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)
		self.master.configure(bg='#0b2c4f')

		self.prod_start_button_title = Label(self.master, text = 'CYCLE START', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.prod_pause_button_title = Label(self.master, text = 'FEED HOLD', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.info_button_title = Label(self.master, text = 'INFO', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.setup_button_title = Label(self.master, text = 'SET UP', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.check_button_title = Label(self.master, text = 'CHECK', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.break_button_title = Label(self.master, text = 'BREAK', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.assist_button_title = Label(self.master, text = 'ASSIST', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')
		self.report_bug_button_title = Label(self.master, text = 'BUG', font=('@SimSun',12), bg = '#0b2c4f', fg = 'white')

		self.ncgui_logo = Label(self.master,image = ncguiswiss,bg='#0b2c4f')



	def load_number(self,userentry):
		"""Initialize from the swiss part number list"""
		self.userentry = userentry.strip()
		for i in swisspartnumbers:
			if self.userentry == i:
				placehold = swisspartnumbers.index(self.userentry)
				timecycle = swisscycletimes[placehold]
				callfordims = swissparts[placehold]
				with open(callfordims) as dim:
					read_dims = dim.readlines()
					swisskeydim1 = read_dims[7]
					swisskeydim2 = read_dims[9]
					swisskeydim3 = read_dims[11]
					swisskeydim4 = read_dims[13]
					swisskeydim5 = read_dims[15]
					dim.close()
					self.swisskeydims = [swisskeydim1.strip(), swisskeydim2.strip(), swisskeydim3.strip(), swisskeydim4.strip(), swisskeydim5.strip()]
					self.skeycheck = []
					for dim in self.swisskeydims:
						if dim != 'none':
							self.skeycheck.append(dim)
					print(self.skeycheck)
					timesetup = swiss_setuptimes[placehold]

				self.swissformatpartinfolist = [self.userentry,timecycle,timesetup]
				print(f'\nPart {self.userentry} successfully loaded!')
				print(f'Cycle: {timecycle} seconds')
				print(f'Setup: {timesetup} minutes')
				print(f'KEY DIMENSIONS:')
				for key in self.skeycheck:
					print(f'{key.strip()}')
				try:
					self.new_part_window.destroy()
					self.welcomescreen.destroy()
					self.notreadyscreen.destroy()
					self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
					self.setupscreen = Label(self.master, text = 'SETUP',font = ('System', 16),fg='green', bg='#464047')
					self.readyscreen.place(x=310,y=220)
					self.setupscreen.place(x=105,y=260)
					self.setupstart = time.time()
					self.clear_panel_buttons()
					self.restore_panel_buttons()
					self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED, command = lambda:self.break_time())
					self.break_button.place(x=825, y=200)
					self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
					self.assist_button.place(x=895, y=200)
					self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
					self.setup_button.place(x=670, y=275)			
				except:
					print('Error: Bad session target. USER: IF WINDOW REFUSES TO CLOSE, EXIT SUPERIORLOG AND RUN SOFTWARE AGAIN.')

	def home_show_info(self):
		"""show swiss part info on screen"""
		
		self.swisspartinfo1 = self.swissformatpartinfolist[0]
		self.swisscycleinfo2 = self.swissformatpartinfolist[1]
		self.swiss_setupinfo3 = self.swissformatpartinfolist[2]
		self.welcomescreen = Label(self.master, text=f'Part: {self.swisspartinfo1}\n Cycle (seconds): {self.swisscycleinfo2}\n Set-up (minutes): {self.swiss_setupinfo3}', font=('System',16), fg='green',justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)


	def do_a_check(self):
		"""do a check on swiss part"""
		self.check_button.destroy()
		self.check_screen = Label(self.master, text = 'CHECK ACTIVE',font = ('System', 16),fg='green', bg='#464047')
		self.check_screen.place(x=330,y=260)
		self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.check_button.place(x=740, y=275)
		self.check_window = Toplevel(self.master)
		self.check_window.geometry('+700+400')
		self.check_window.configure(bg='#b8b7b6')
		self.check_window.resizable(False,False)
		self.check_window.title(f'Check a Part - User: {checkuser}')
		
		
		
		def restore_check():
			"""If window closes, make set up button not disabled again"""
			self.check_button.destroy()
			self.check_screen.destroy()
			self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command = lambda: self.do_a_check(),state = NORMAL)
			self.check_button.place(x=740, y=275)
			self.check_window.destroy()

		self.check_window.protocol("WM_DELETE_WINDOW", restore_check)
		
		check_boxes = []
		for check_dim in self.skeycheck:
			check_dim = Label(self.check_window,text=f'{check_dim}',font=('Yu Gothic UI Light',24),padx=35,pady=5,bg='#b8b7b6')
			check_dim.pack()
			check_boxes.append(check_dim)

			
		self.usercheckentrylist = []	
		for box in check_boxes:
			
			box = Entry(self.check_window, width=15, font=('Yu Gothic UI Light',24),borderwidth=3,bg='#dedcdb')
			self.usercheckentrylist.append(box)
			box.pack()
			
		def gather_check_entries():
			"""Gather up entries in boxes and initialize them"""
			self.finalized_user_checks = []
			for check in self.usercheckentrylist:
				showcheck = check.get()
				self.finalized_user_checks.append(showcheck)
			checktimestamp = datetime.now() 
			with open(checks, 'a') as writechecks:
				make_buffer1 = writechecks.write(f'-----------------------------------------------------------------------------------------------\n')
				express_userinfo = writechecks.write(f'Part: {self.swissformatpartinfolist[0]}\tUser: {checkuser}\tTime&Date: {checktimestamp}\n')
				for c in self.skeycheck:
					p = self.skeycheck.index(c)
					put_check_info = writechecks.write(f'\n{c}\t--->\t{self.finalized_user_checks[p]}\n')
				writechecks.close()
				self.check_screen.destroy()
				self.check_window.destroy()
				self.check_button.destroy()
				self.check_screen.destroy()
				self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda: self.do_a_check())
				self.check_button.place(x=740, y=275)
		self.submit_check_button = Button(self.check_window, text='Submit Part Check',padx=60,pady=25,borderwidth=3,bg='#dedcdb',command=lambda: gather_check_entries())
		self.submit_check_button.pack()






class MillWindow(SessionWindow):
	def __init__(self, master):
		super().__init__(master)
		self.welcomescreen = Label(self.master, text=f"{checkuser.title()}'s New Mill Session.\nClick the Set-up button to begin.", font=('System',16), fg='green', justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)
		self.master.configure(bg='#4f0000')
		self.ncgui_logo = Label(self.master,image = ncguimill,bg='#4f0000')


		self.prod_start_button_title = Label(self.master, text = 'CYCLE START', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.prod_pause_button_title = Label(self.master, text = 'FEED HOLD', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.info_button_title = Label(self.master, text = 'INFO', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.setup_button_title = Label(self.master, text = 'SET UP', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.check_button_title = Label(self.master, text = 'CHECK', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.break_button_title = Label(self.master, text = 'BREAK', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.assist_button_title = Label(self.master, text = 'ASSIST', font=('@SimSun',12), bg = '#4f0000', fg='white')
		self.report_bug_button_title = Label(self.master, text = 'BUG', font=('@SimSun',12), bg = '#4f0000', fg='white')
		
	def load_number(self,userentry):
		"""Load lathe part from lathe part list"""
		self.userentry = userentry.strip()
		for i in millpartnumbers:
			if self.userentry == i:
				placehold = millpartnumbers.index(self.userentry)
				timecycle = millcycletimes[placehold]
				callfordims = millparts[placehold]
				with open(callfordims) as dim:
					read_dims = dim.readlines()
					millkeydim1 = read_dims[7]
					millkeydim2 = read_dims[9]
					millkeydim3 = read_dims[11]
					millkeydim4 = read_dims[13]
					millkeydim5 = read_dims[15]
					dim.close()
				self.millkeydims = [millkeydim1.strip(), millkeydim2.strip(), millkeydim3.strip(), millkeydim4.strip(), millkeydim5.strip()]
				self.mkeycheck = []
				for dim in self.millkeydims:
					if dim != 'none':
						self.mkeycheck.append(dim)
				print(self.mkeycheck)
				timesetup = millsetuptimes[placehold]

				self.millformatpartinfolist = [self.userentry,timecycle,timesetup]
				print(f'\nPart {self.userentry} successfully loaded!')
				print(f'Cycle: {timecycle} seconds')
				print(f'Setup: {timesetup} minutes')
				print(f'KEY DIMENSIONS:')
				for key in self.mkeycheck:
					print(f'{key.strip()}')
				try:
					self.new_part_window.destroy()
					self.welcomescreen.destroy()
					self.notreadyscreen.destroy()
					self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
					self.setupscreen = Label(self.master, text = 'SETUP',font = ('System', 16),fg='green', bg='#464047')
					self.readyscreen.place(x=310,y=220)
					self.setupscreen.place(x=105,y=260)
					self.setupstart = time.time()
					self.clear_panel_buttons()
					self.restore_panel_buttons()
					self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED, command = lambda:self.break_time())
					self.break_button.place(x=825, y=200)
					self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
					self.assist_button.place(x=895, y=200)
					self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
					self.setup_button.place(x=670, y=275)			
				except:
						print('Error: Bad session target. USER: IF WINDOW REFUSES TO CLOSE, EXIT SUPERIORLOG AND RUN SOFTWARE AGAIN.')


	def home_show_info(self):
		"""Show part info for lathe"""
		
		self.millpartinfo1 = self.millformatpartinfolist[0]
		self.millcycleinfo2 = self.millformatpartinfolist[1]
		self.millsetupinfo3 = self.millformatpartinfolist[2]
		self.welcomescreen = Label(self.master, text=f'Part: {self.millpartinfo1}\n Cycle (seconds): {self.millcycleinfo2}\n Set-up (minutes): {self.millsetupinfo3}', font=('System',16), fg='green',justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)



	def do_a_check(self):
		"""Do a check for lathe part"""
		self.check_button.destroy()
		self.check_screen = Label(self.master, text = 'CHECK ACTIVE',font = ('System', 16),fg='green', bg='#464047')
		self.check_screen.place(x=330,y=260)
		self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.check_button.place(x=740, y=275)
		self.check_window = Toplevel(self.master)
		self.check_window.geometry('+700+400')
		self.check_window.configure(bg='#b8b7b6')
		self.check_window.resizable(False,False)
		self.check_window.title(f'Check a Part - User: {checkuser}')
			
		
		def restore_check():
			"""If window is closed, make set up button not disabled again"""
			self.check_screen.destroy()
			self.check_button.destroy()
			self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command = lambda: self.do_a_check(),state = NORMAL)
			self.check_button.place(x=740, y=275)
			self.check_window.destroy()

		self.check_window.protocol("WM_DELETE_WINDOW", restore_check)
		check_boxes = []
		for check_dim in self.mkeycheck:
			check_dim = Label(self.check_window,text=f'{check_dim}',font=('Yu Gothic UI Light',24),padx=35,pady=5,bg='#b8b7b6')
			check_dim.pack()
			check_boxes.append(check_dim)

		self.usercheckentrylist = []	
		for box in check_boxes:
			
			box = Entry(self.check_window, width=15, font=('Yu Gothic UI Light',24),borderwidth=3,bg='#dedcdb')
			self.usercheckentrylist.append(box)
			box.pack()
		
		self.finalized_user_checks = []
		def gather_check_entries():
			"""Gather entries for lathe check and initialize them"""
			for check in self.usercheckentrylist:
				showcheck = check.get()
				print(showcheck)
				self.finalized_user_checks.append(showcheck)
			
			checktimestamp = datetime.now() 
			with open(checks, 'a') as writechecks:
				make_buffer1 = writechecks.write(f'-----------------------------------------------------------------------------------------------\n')
				express_userinfo = writechecks.write(f'Part: {self.millformatpartinfolist[0]}\tUser: {checkuser}\tTime&Date: {checktimestamp}\n')
				for c in self.mkeycheck:
					p = self.mkeycheck.index(c)
					put_check_info = writechecks.write(f'\n{c}\t--->\t{self.finalized_user_checks[p]}\n')
				writechecks.close()
				self.check_screen.destroy()
				self.check_window.destroy()
				self.check_button.destroy()
				self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda: self.do_a_check())
				self.check_button.place(x=740, y=275)


			
		self.submit_check_button = Button(self.check_window, text='Submit Part Check',padx=60,pady=25,borderwidth=3,bg='#dedcdb',command=lambda: gather_check_entries())
		self.submit_check_button.pack()





class LatheWindow(SessionWindow):
	"""Lathe child class different part numbers"""
	def __init__(self, master):
		super().__init__(master)
		self.welcomescreen = Label(self.master, text=f"{checkuser.title()}'s New Lathe Session.\nClick the Set-up button to begin.", font=('System',16), fg='green', justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)
		self.master.configure(bg='#0babdc')
		self.ncgui_logo = Label(self.master,image = ncguilathe,bg='#0babdc')


		self.prod_start_button_title = Label(self.master, text = 'CYCLE START', font=('@SimSun',12), bg = '#0babdc')
		self.prod_pause_button_title = Label(self.master, text = 'FEED HOLD', font=('@SimSun',12), bg = '#0babdc')
		self.info_button_title = Label(self.master, text = 'INFO', font=('@SimSun',12), bg = '#0babdc')
		self.setup_button_title = Label(self.master, text = 'SET UP', font=('@SimSun',12), bg = '#0babdc')
		self.check_button_title = Label(self.master, text = 'CHECK', font=('@SimSun',12), bg = '#0babdc')
		self.break_button_title = Label(self.master, text = 'BREAK', font=('@SimSun',12), bg = '#0babdc')
		self.assist_button_title = Label(self.master, text = 'ASSIST', font=('@SimSun',12), bg = '#0babdc')
		self.report_bug_button_title = Label(self.master, text = 'BUG', font=('@SimSun',12), bg = '#0babdc')
		
	def load_number(self,userentry):
		"""Load lathe part from lathe part list"""
		self.userentry = userentry.strip()
		for i in lathepartnumbers:
			if self.userentry == i:
				placehold = lathepartnumbers.index(self.userentry)
				timecycle = lathecycletimes[placehold]
				callfordims = latheparts[placehold]
				with open(callfordims) as dim:
					read_dims = dim.readlines()
					lathekeydim1 = read_dims[7]
					lathekeydim2 = read_dims[9]
					lathekeydim3 = read_dims[11]
					lathekeydim4 = read_dims[13]
					lathekeydim5 = read_dims[15]
					dim.close()
				self.lathekeydims = [lathekeydim1.strip(), lathekeydim2.strip(), lathekeydim3.strip(), lathekeydim4.strip(), lathekeydim5.strip()]
				self.lkeycheck = []
				for dim in self.lathekeydims:
					if dim != 'none':
						self.lkeycheck.append(dim)
				print(self.lkeycheck)
				timesetup = lathesetuptimes[placehold]

				self.latheformatpartinfolist = [self.userentry,timecycle,timesetup]
				print(f'\nPart {self.userentry} successfully loaded!')
				print(f'Cycle: {timecycle} seconds')
				print(f'Setup: {timesetup} minutes')
				print(f'KEY DIMENSIONS:')
				for key in self.lkeycheck:
					print(f'{key.strip()}')
				try:
					self.new_part_window.destroy()
					self.welcomescreen.destroy()
					self.notreadyscreen.destroy()
					self.readyscreen = Label(self.master, text = 'READY', font=('System',16), fg='yellow', bg='#464047')
					self.setupscreen = Label(self.master, text = 'SETUP',font = ('System', 16),fg='green', bg='#464047')
					self.readyscreen.place(x=310,y=220)
					self.setupscreen.place(x=105,y=260)
					self.setupstart = time.time()
					self.clear_panel_buttons()
					self.restore_panel_buttons()
					self.break_button = Button(self.master, text = 'ä', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED, command = lambda:self.break_time())
					self.break_button.place(x=825, y=200)
					self.assist_button = Button(self.master, text = 'I', font=('Wingdings', 18), padx=6, pady=1, borderwidth=2,state = DISABLED)
					self.assist_button.place(x=895, y=200)
					self.setup_button = Button(self.master,text = '@', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command=lambda:self.set_up(), state=DISABLED)
					self.setup_button.place(x=670, y=275)			
				except:
						print('Error: Bad session target. USER: IF WINDOW REFUSES TO CLOSE, EXIT SUPERIORLOG AND RUN SOFTWARE AGAIN.')


	def home_show_info(self):
		"""Show part info for lathe"""
		
		self.lathepartinfo1 = self.latheformatpartinfolist[0]
		self.lathecycleinfo2 = self.latheformatpartinfolist[1]
		self.lathesetupinfo3 = self.latheformatpartinfolist[2]
		self.welcomescreen = Label(self.master, text=f'Part: {self.lathepartinfo1}\n Cycle (seconds): {self.lathecycleinfo2}\n Set-up (minutes): {self.lathesetupinfo3}', font=('System',16), fg='green',justify='left',bg='#464047')
		self.welcomescreen.place(x=55,y=100)



	def do_a_check(self):
		"""Do a check for lathe part"""
		self.check_button.destroy()
		self.check_screen = Label(self.master, text = 'CHECK ACTIVE',font = ('System', 16),fg='green', bg='#464047')
		self.check_screen.place(x=330,y=260)
		self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = DISABLED)
		self.check_button.place(x=740, y=275)
		self.check_window = Toplevel(self.master)
		self.check_window.geometry('+700+400')
		self.check_window.configure(bg='#b8b7b6')
		self.check_window.resizable(False,False)
		self.check_window.title(f'Check a Part - User: {checkuser}')
			
		
		def restore_check():
			"""If window is closed, make set up button not disabled again"""
			self.check_screen.destroy()
			self.check_button.destroy()
			self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,command = lambda: self.do_a_check(),state = NORMAL)
			self.check_button.place(x=740, y=275)
			self.check_window.destroy()

		self.check_window.protocol("WM_DELETE_WINDOW", restore_check)
		check_boxes = []
		for check_dim in self.lkeycheck:
			check_dim = Label(self.check_window,text=f'{check_dim}',font=('Yu Gothic UI Light',24),padx=35,pady=5,bg='#b8b7b6')
			check_dim.pack()
			check_boxes.append(check_dim)

		self.usercheckentrylist = []	
		for box in check_boxes:
			
			box = Entry(self.check_window, width=15, font=('Yu Gothic UI Light',24),borderwidth=3,bg='#dedcdb')
			self.usercheckentrylist.append(box)
			box.pack()
		
		self.finalized_user_checks = []
		def gather_check_entries():
			"""Gather entries for lathe check and initialize them"""
			for check in self.usercheckentrylist:
				showcheck = check.get()
				print(showcheck)
				self.finalized_user_checks.append(showcheck)
			
			checktimestamp = datetime.now() 
			with open(checks, 'a') as writechecks:
				make_buffer1 = writechecks.write(f'-----------------------------------------------------------------------------------------------\n')
				express_userinfo = writechecks.write(f'Part: {self.latheformatpartinfolist[0]}\tUser: {checkuser}\tTime&Date: {checktimestamp}\n')
				for c in self.lkeycheck:
					p = self.lkeycheck.index(c)
					put_check_info = writechecks.write(f'\n{c}\t--->\t{self.finalized_user_checks[p]}\n')
				writechecks.close()
				self.check_screen.destroy()
				self.check_window.destroy()
				self.check_button.destroy()
				self.check_button = Button(self.master, text = 'a', font=('Webdings', 18), padx=1, pady=1, borderwidth=2,state = NORMAL, command = lambda: self.do_a_check())
				self.check_button.place(x=740, y=275)


			
		self.submit_check_button = Button(self.check_window, text='Submit Part Check',padx=60,pady=25,borderwidth=3,bg='#dedcdb',command=lambda: gather_check_entries())
		self.submit_check_button.pack()






class BlastWindow(SessionWindow):
	"""Sandblaster child class"""
	def __init__(self, master):
		super().__init__(master)
















#END OF DEPARTMENT PANEL WINDOW CLASSES
#-----------------------------------------------------------------------------------------------------

def start_swiss():
	"""Load in the swiss cnc panel for production"""
	spanel = Toplevel()
	spanel.title(f'New Swiss Session - User: {checkuser}')
	swiss_session = SwissWindow(spanel)
	swiss_session.open_session()
def start_lathe():
	"""Load in the lathe panel for production"""
	lpanel= Toplevel()
	lpanel.title(f'New Lathe Session - User: {checkuser}')
	lathe_session = LatheWindow(lpanel)
	lathe_session.open_session()
def start_mill():
	"""Load in the mill panel for production"""
	mpanel= Toplevel()
	mpanel.title(f'New Mill Session - User: {checkuser}')
	mill_session = MillWindow(mpanel)
	mill_session.open_session()

#initialize size, background, and resizablility for the root home center window
root.geometry('1750x850+50+50')
root.configure(bg='#b8b7b6')
root.resizable(False, False)
#define images to use as buttons on department selection and open them
latheimg=ImageTk.PhotoImage(Image.open('imgs/lathe.jpg'))
swissimg=ImageTk.PhotoImage(Image.open('imgs/swiss.jpg'))
millimg=ImageTk.PhotoImage(Image.open('imgs/mill.jpg'))
sandimg = ImageTk.PhotoImage(Image.open('imgs/sand.png'))

#HOME CENTER put opened files into a list and define the images as buttons
deptchimglist = (latheimg,swissimg,millimg)

swissd = Button(root,text='Swiss',image=swissimg, compound=BOTTOM, command=lambda: start_swiss())
swissd.place(x=50,y=658)
lathed = Button(root,text='Lathe',image=latheimg, compound=BOTTOM, command=lambda: start_lathe())
lathed.place(x=400,y=658)
milld = Button(root,text='Mill',image=millimg, compound=BOTTOM, command=lambda: start_mill())
milld.place(x=750,y=658)
sandd = Button(root,image=sandimg, text='Sandblaster', compound=BOTTOM)
sandd.place(x=1100,y=658)
otherd = Button(root,text='Other',padx=100, pady=83)
otherd.place(x=1450,y=658)
greeting = Label(root,text=f'Welcome to the Home Center! Click on a department to start a session.', font=('Yu Gothic UI Semibold',36), bg='#b8b7b6', borderwidth=3)
greeting.place(x=10,y=22)
importantmessagesbox = LabelFrame(root, text='Important Updates & Announcements:',font=('Yu Gothic UI Medium',20),padx=20,pady=20,bg='#dedcdb',relief=RAISED)

importantmessagesbox.place(x=25,y=150)
messagesupdates = 'logs/admintools/home_center_important_messages.txt'
#read the important messages and updates and display in the home center
with open(messagesupdates) as file:
	readmessages = file.read()
importantinfoinside = Label(importantmessagesbox, text=readmessages,bg='#dedcdb',justify='left',font=('Yu Gothic UI Light',12)).pack(anchor =E)
file.close()
def disable_close():
	pass
def ask_exit_if_sure():
	confirm_exit_window = Toplevel(root)
	root.protocol("WM_DELETE_WINDOW", disable_close)
	confirm_exit_window.geometry('260x120+850+450')
	confirm_exit_window.title(f'User: {checkuser}')
	confirm_exit_window.resizable(False,False)
	confirm_exit_window.configure(bg='#b8b7b6')
	exit_desc = Label(confirm_exit_window, font=('Yu Gothic UI Light',13),bg='#b8b7b6',text= 'Are you sure you want to exit?\nAll windows will be closed.').place(x=15,y=10)
	
	def user_wants_to_stay():
		confirm_exit_window.destroy()
		root.protocol("WM_DELETE_WINDOW", ask_exit_if_sure)

	exit_yes = Button(confirm_exit_window, text = 'Yes',font=('Yu Gothic UI Light',13),bg='#dedcdb', command = root.destroy, padx=12,pady=1,borderwidth=3).place(x=60,y=70)
	exit_no = Button(confirm_exit_window, text='Cancel', command = user_wants_to_stay,font=('Yu Gothic UI Light',13),bg='#dedcdb',borderwidth=3,pady=1).place(x=140,y=70)
	confirm_exit_window.protocol("WM_DELETE_WINDOW", user_wants_to_stay)
		
root.protocol("WM_DELETE_WINDOW", ask_exit_if_sure)

#program run
if __name__ == '__main__':

	root.mainloop()






		