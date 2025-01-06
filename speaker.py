#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file speaker.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

from pygame import mixer      
import pygame


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
speaker_spec = ["implementation_id", "speaker", 
         "type_name",         "speaker", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.judge", "false",

         "conf.__widget__.judge", "text",

         "conf.__type__.judge", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class speaker
# @brief ModuleDescription
# 
# 
# </rtc-template>
class speaker(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_command_in = OpenRTM_aist.instantiateDataType(RTC.TimedLongSeq)
        """
        """
        self._command_inIn = OpenRTM_aist.InPort("command_in", self._d_command_in)
        self._d_judgement = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
        """
        """
        self._judgementIn = OpenRTM_aist.InPort("judgement", self._d_judgement)
        self._d_command_out = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
        """
        """
        self._command_outOut = OpenRTM_aist.OutPort("command_out", self._d_command_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  judge
         - DefaultValue: false
        """
        self._judge = ['false']
		
        # </rtc-template>

        self.directory="/home/rsdlab/catkin_ws/src/rois_ros/script/voice_kenkou/"
        text ="hello"
        self.file_path = self.directory +"hello.mp3"
		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("judge", self._judge, "false")
		
        # Set InPort buffers
        self.addInPort("command_in",self._command_inIn)
        self.addInPort("judgement",self._judgementIn)
		
        # Set OutPort buffers
        self.addOutPort("command_out",self._command_outOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
 
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	

    def onExecute(self, ec_id):
        if self._command_inIn.isNew(): 
            print("data in")
            print(self.file_path)
            command = self._command_inIn.read()
            print(f"コマンド {command.data}")

            if command.data[1] == 10:
                self.file_path = self.directory + "hello.mp3"
            elif command.data[1] == 11:
                self.file_path = self.directory + "check_measure.mp3"
            elif command.data[1] == 12:
                self.file_path = self.directory + "check_measure2.mp3"
            elif command.data[1] == 13:
                self.file_path = self.directory + "check_measure3.mp3"
            elif command.data[1] == 14:
                self.file_path = self.directory + "yorosiku.mp3"
            elif command.data[1] == 15:
                self.file_path = self.directory + "check_start.mp3"
            elif command.data[1] == 16:
                self.file_path = self.directory + "how_health.mp3"
            elif command.data[1] == 17:
                self.file_path = self.directory + "bad_high.mp3"
            elif command.data[1] == 18:
                self.file_path = self.directory + "bad_low.mp3"
            elif command.data[1] == 19:
                self.file_path = self.directory + "good_low.mp3"
            elif command.data[1] == 20:
                self.file_path = self.directory + "good_high.mp3"
            elif command.data[1] == 21:
                self.file_path = self.directory + "check_hand.mp3"
            elif command.data[1] == 22:
                self.file_path = self.directory + "check_ok.mp3"
            elif command.data[1]  == 23:
                self.file_path = self.directory + "how_health.mp3"
            elif command.data[1]  == 50:
                print(self.file_path)
            else:
                print("no")
            
            if self._judgementIn.isNew(): 
                judge  = self._judgementIn.read()
                print(judge.data)
                self.file_path = self.directory + judge.data + ".mp3"

            speak_result = speak(command.data[0], self.file_path)

            print(f"結果 {speak_result}")


            self._d_command_out.data = speak_result
            self._command_outOut.write()

        
    
        return RTC.RTC_OK
	

def makefile(place):
    from gtts import gTTS
    from pygame import mixer
    import time

    file = 'announce.mp3'
    text='今から' + place + 'へ移動します．ご注意ください'

    tts1 = gTTS(text, lang='ja')
    tts1.save()

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    time.sleep(30)

    return 
	

def speak(state, file_path):
    if state == 1:
        print(state)
        print("音声認識は停止中です。")
        return "ERROR"
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()


        while state == 0:
            time.sleep(0.1)

            if not pygame.mixer.music.get_busy():
                # print("Playback completed.")
                result = "OK"
                return result

    except pygame.error as e:
        print(f"Pygame error occurred: {e}")
        result = "ERROR" 
        return result

    except FileNotFoundError as e:
        print(f"File error: {e}")
        result = "ERROR" 
        return result

    except Exception as e:
        print(f"Unexpected error: {e}")
        result = "ERROR" 
        return result

    
        


def speakerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=speaker_spec)
    manager.registerFactory(profile,
                            speaker,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    speakerInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("speaker" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

