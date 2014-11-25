import datetime
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="HP Envy"
__date__ ="$Nov 19, 2014 2:17:51 PM$"

from rootio.radio.models import ScheduledProgram, Program
from datetime import datetime
from RadioProgram import RadioProgram
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

class ProgramHandler:
    __db = None
    __radio_station = None
    __scheduled_programs = []
    __running_program = None
    __scheduler = None
    
    def __init__(self, db, radio_station):
        self.__db = db
        self.__radio_station = radio_station
        self.__load_programs()
        #self.__get_current_program()
        self.__scheduler = BackgroundScheduler()
        return
    
    def run(self):
        #self.__running_program = self.__get_current_program()
        #self.__run_program(program);
        self.__schedule_programs()
        self.__scheduler.start()
        pass
    
    def stop(self):
        self.__stop_program()
        #any clean up goes here
        return
    
    def __schedule_programs(self):
        for scheduled_program in self.__scheduled_programs:#throw all the jobs into AP scheduler and have it rain down alerts
            if not self.__is_program_expired(scheduled_program):
                program = RadioProgram(self.__db, scheduled_program)
                self.__scheduler.add_job(getattr(program,'start'), 'date', None, None, None, 'scheduled_program', 1, 0, 1, scheduled_program.start)
                 #  __scheduler.add_job(scheduled_program.run, scheduled_program.start) 
       #return 
    
    def __stop_program(self):
        __running_program.stop()
        return
    
    def __run_program(self):
        __running_program.run()
        return
    
    def __load_programs(self):
        self.__scheduled_programs = self.__db.session.query(ScheduledProgram).filter().all()
        print self.__scheduled_programs
    
    """
    Gets the program to run from the current list of programs that are lined up for the day
    """
    def __get_current_program(self):
        for program in self.__scheduled_programs:
            if not self.__is_program_expired(program):
                print "we found one!! starting at " + str(program.start)
                return program
            
    
    """
    Returns whether or not the time for a particular program has passed
    """
    def __is_program_expired(self, program):
        original_program = self.__db.session.query(Program).filter(Program.id == program.program_id).one()
        now = pytz.utc.localize(datetime.utcnow())
        return program.start + original_program.duration < now 
    
