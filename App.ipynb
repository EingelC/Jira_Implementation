import pandas as pd
from pandas import *
import keras
import numpy as np
import string
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import time
from jira import JIRA
import re
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import simpledialog
import webbrowser

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

class Conectarse:
    def __init__(self):
        self.jira_server = "https://YourCompany.atlassian.net"
        self.jira_email = "Insert mail"
        self.jira_api_token = "Insert your API KEY"
        self.jira = JIRA(server=self.jira_server, basic_auth=(self.jira_email, self.jira_api_token))
        self.get_user_id = self.jira.myself()
        self.user_id = self.get_user_id['accountId']
        self.Archivo = read_csv("VideosDisponibles.csv")

    def ObtenerTicket(self, entry):
        TextoCodigo = entry
        TicketToReview = "ProjectCode-" + TextoCodigo
        TicketCode = self.jira.issue(TicketToReview)
        print(f"https://YourCompany.atlassian.net/browse/"+TicketCode.key)
        return TicketCode
    
    def LeerLocal(self):
        global entry, SiguienteTicket
        CodigoTicket = self.Archivo['ID'].tolist()
        EnlacesVideo = self.Archivo['Url'].tolist()
        EnlacesTicket = self.Archivo['Ticket'].tolist()

        while True:
            ticketcode = self.jira.issue(CodigoTicket[SiguienteTicket])
            persona = getattr(ticketcode.fields, "assignee")
            if persona is None:
                print("No hay persona asignada, usando este ticket")
                break
            else:
                print(f"Persona asignada: {persona.displayName}")
                SiguienteTicket += 1

        Enlace_Video = EnlacesVideo[SiguienteTicket]
        ResolverTicket = CodigoTicket[SiguienteTicket]
        Enlace_Ticket = EnlacesTicket[SiguienteTicket]
        webbrowser.get('chrome').open(Enlace_Ticket)
        webbrowser.get('chrome').open(Enlace_Video)
        entry = ResolverTicket.split("-")[1]
        SiguienteTicket += 1
        TextoID.config(text=f"{entry}")
        return entry

class Variables:
    def __init__(self, user_id):
        self.follow_up_field_id = "customfield_10251" #Forward to Autonomy
        self.driving_mode_id = "customfield_10112" #AP
        self.incident_location_id = "customfield_10313" #sidewalk
        self.vendor_delivery_id = "customfield_10246" #Uber Eats
        self.sev_id = "customfield_11171" #SEV3
        self.severity_id = "customfield_1031" #3
        self.incident_type_id = "customfield_10111" #Moving
        self.session_type_id = "customfield_10275" #On Delivery
        self.flipped_id = "customfield_10317" #No
        self.video_time_id = "customfield_10337" #hh:mm:ss
        self.create_date_id = "customfield_10041" #Creation Date YYYY/MM/DD Time
        self.video_link_id = "customfield_10610"
        self.current_robot = "customfield_10043" #Name + (code)
        self.modify_link_video_id = "customfield_10610" #Current video link
        self.day_or_night_id = "customfield_10339" #Day / Night
        self.video_link_start = "https://VideolinkOfMyCompany"
        self.market_location_id = "customfield_10346" #Codigo lugar ABC
        self.scalation_id = "customfield_10059" #Ticket Not Necessary // Autonomy // etc
        self.timestamp_id = "customfield_10337" #Hora poner manual
        self.incident_parties_id = "customfield_10315" #Object/Pedestrian/Vehicle
        self.ap_incident_category_id = "customfield_10340" #Collision/Fell/etc
        self.user_id = user_id

    def Locacion(self, TicketCode):
        get_location = getattr(TicketCode.fields, self.market_location_id)
        location_str = str(get_location)
        code_location = location_str.split("-")[0]
        return code_location

    def Tiempos(self, TicketCode, entry2):
        get_date_time = getattr(TicketCode.fields, self.create_date_id)
        get_video_time = entry2.get()
        get_robot_number = getattr(TicketCode.fields, self.current_robot)
        is_on_delivery = TicketCode.fields.description

        robot_str = str(get_robot_number)
        video_time_Str = str(get_video_time)
        date_time_str = str(get_date_time)

        robot_number = re.search(r"\((.*?)\)", robot_str)
        serial_number = robot_number.group(1)
        date_number = date_time_str.split("T")[0]

        video_time_dt = datetime.strptime(video_time_Str, "%H:%M:%S")
        date_time_dt = datetime.strptime(date_number, "%Y-%m-%d")

        dt = datetime.combine(date_time_dt.date(), video_time_dt.time())
        dt_new = dt + timedelta(hours=7, seconds=-5)

        new_video_time = dt_new.strftime("%H:%M:%S")
        new_date_time = dt_new.strftime("%Y-%m-%d")

        final_video_link = (self.video_link_start+serial_number+"&start="+new_date_time+"T"+new_video_time+".000Z&duration=300")
        print(final_video_link)
        return video_time_dt, final_video_link, is_on_delivery, video_time_Str

class CambiarCampos:
    def __init__(self, TicketCode, vars, entry2, user_id=None):
        self.TicketCode = TicketCode
        self.vars = vars
        self.video_time_dt, self.final_video_link, self.is_on_delivery, self.video_time_Str = vars.Tiempos(TicketCode, entry2)
        self.user_id = user_id
        transitions = conexion.jira.transitions(TicketCode)
        self.done_transition = next(t for t in transitions if t['name'] == 'Done')
        self.vetting_transition = next(t for t in transitions if t['name'] == 'Vetting')
        conexion.jira.transition_issue(self.TicketCode, self.vetting_transition['id'])

        if "uber eats" in self.is_on_delivery.lower():
            self.TicketCode.update(fields={
                self.vars.vendor_delivery_id: [{"id": "10758"}]
                })
            
    def DiaNoche(self):
        hora = datetime.strptime("18:00:00", "%H:%M:%S").time()
        if self.video_time_dt.time() > hora:
            self.TicketCode.update(fields={self.vars.day_or_night_id: {"value": "Night 🌛"}})
        else:
            self.TicketCode.update(fields={self.vars.day_or_night_id: {"value": "Day ☀️"}})

    def AP_Fell_Treewell(self):
        self.TicketCode.update(fields={
            self.vars.follow_up_field_id: [{"value": "Forward to Autonomy"}],
            "components": [{"id": "10736"},{"id": "12016"},{"id": "12013"}],
            self.vars.driving_mode_id: {"value": "AP"},
            self.vars.incident_location_id: {"value": "sidewalk"},
            self.vars.sev_id: {"value": "SEV3"},
            self.vars.incident_type_id: {"value": "Moving"},
            self.vars.session_type_id: {"value": "On delivery"},
            self.vars.flipped_id: {"value": "No"},
            self.vars.modify_link_video_id: self.final_video_link,
            self.vars.timestamp_id: self.video_time_Str,
            "assignee": {"id": self.vars.user_id},
            self.vars.ap_incident_category_id: [{"id": "15883"}]
        })
        transitions = conexion.jira.transitions(self.TicketCode)
        self.ready_for_revision = next(t for t in transitions if t['name'] == 'Ready for Review')
        conexion.jira.transition_issue(self.TicketCode, self.ready_for_revision['id'])
        transitions = conexion.jira.transitions(self.TicketCode)
        self.ready_for_autonomy_review = next(t for t in transitions if t['name'] == 'Ready for Autonomy Review')
        conexion.jira.transition_issue(self.TicketCode, self.ready_for_autonomy_review['id'])

    def AP_Fell_Walkside(self):
        self.TicketCode.update(fields={
            self.vars.follow_up_field_id: [{"value": "Forward to Autonomy"}],
            "components": [{"id": "10736"},{"id": "12016"},{"id": "12013"}],
            self.vars.driving_mode_id: {"value": "AP"},
            self.vars.incident_location_id: {"value": "sidewalk"},
            self.vars.sev_id: {"value": "SEV3"},
            self.vars.incident_type_id: {"value": "Moving"},
            self.vars.session_type_id: {"value": "On delivery"},
            self.vars.flipped_id: {"value": "No"},
            self.vars.modify_link_video_id: self.final_video_link,
            self.vars.timestamp_id: self.video_time_Str,
            "assignee": {"id": self.vars.user_id},
            self.vars.ap_incident_category_id: [{"id": "15884"}]
            })
        transitions = conexion.jira.transitions(self.TicketCode)
        self.ready_for_revision = next(t for t in transitions if t['name'] == 'Ready for Review')
        conexion.jira.transition_issue(self.TicketCode, self.ready_for_revision['id'])
        transitions = conexion.jira.transitions(self.TicketCode)
        self.ready_for_autonomy_review = next(t for t in transitions if t['name'] == 'Ready for Autonomy Review')
        conexion.jira.transition_issue(self.TicketCode, self.ready_for_autonomy_review['id'])

    def No_Action_change(self):
        self.TicketCode.update(fields={
            self.vars.follow_up_field_id: [{"value": "No Action"}],
            "components": [{"id": "12013"}],
            self.vars.session_type_id: {"value": "On delivery"},
            self.vars.sev_id: {"value": "SEV3"},
            self.vars.flipped_id: {"value": "No"},
            self.vars.scalation_id: {"value": "Ticket Not Necessary"},
            self.vars.timestamp_id: self.video_time_Str,
            self.vars.modify_link_video_id: self.final_video_link,
            "assignee": {"id": self.vars.user_id}
        })

    def AP_Proximity_Static_change(self):
        self.TicketCode.update(fields={
            self.vars.follow_up_field_id: [{"value": "Forward to Autonomy"}],
            "components": [{"id": "10736"},{"id": "12014"},{"id": "12013"}],
            self.vars.driving_mode_id: {"value": "AP"},
            self.vars.incident_location_id: {"value": "sidewalk"},
            self.vars.sev_id: {"value": "SEV3"},
            self.vars.incident_type_id: {"value": "Moving"},
            self.vars.session_type_id: {"value": "On delivery"},
            self.vars.flipped_id: {"value": "No"},
            self.vars.modify_link_video_id: self.final_video_link,
            self.vars.timestamp_id: self.video_time_Str,
            self.vars.incident_parties_id: [{"id": "11403"}],
            self.vars.ap_incident_category_id: [{"id": "13737"}],
            "assignee": {"id": self.vars.user_id}
            })

SiguienteTicket = 0
root = tk.Tk()
root.title("Ticketeros")
root.geometry("600x300")
root.attributes("-topmost", True)

for j in range(5):
    root.columnconfigure(j, weight=1)
    #root.rowconfigure(j, weight=1)

label = tk.Label(root, text="Codigo de Ticket")
label.grid(row=0, column=0)
label2 = tk.Label(root, text="Ingresar hora")
label2.grid(row=1, column=0)
entry = ""
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1)
TextoID = tk.Label(root, text="Presione siguiente para iniciar")
TextoID.grid(row=0, column=1)
ErrorMSG = tk.Label(root, text="Ingresar hora en hh:mm:ss", fg='red')
ErrorMSG.grid(row=1, column=2)

conexion = Conectarse()
vars = Variables(conexion.user_id)

class ProcesadorTickets:
    def __init__(self, vars, entry, entry2, conexion):
        self.vars = vars
        self.entry = entry
        self.entry2 = entry2
        self.conexion = conexion
        self.TicketCode = conexion.ObtenerTicket(self.entry)

    def AP_Fell_Walkside_Bot(self):
        self.vars.Locacion(self.TicketCode)
        campos = CambiarCampos(self.TicketCode, self.vars, self.entry2)
        campos.DiaNoche()
        campos.AP_Fell_Walkside()
        EnlacesTicket = self.conexion.Archivo['Ticket'].tolist()
        Enlace_Ticket = EnlacesTicket[SiguienteTicket-1]
        webbrowser.get('chrome').open(Enlace_Ticket)
        print("Ticket Actualizado")

    def Not_Necessary_Bot(self):
        self.vars.Locacion(self.TicketCode)
        campos = CambiarCampos(self.TicketCode, self.vars, self.entry2)
        campos.DiaNoche()
        campos.No_Action_change()
        EnlacesTicket = self.conexion.Archivo['Ticket'].tolist()
        Enlace_Ticket = EnlacesTicket[SiguienteTicket-1]
        webbrowser.get('chrome').open(Enlace_Ticket)
        print("Ticket Actualizado")

    def AP_Proximity_Static_Bot(self):
        self.vars.Locacion(self.TicketCode)
        campos = CambiarCampos(self.TicketCode, self.vars, self.entry2)
        campos.DiaNoche()
        campos.AP_Proximity_Static_change()
        EnlacesTicket = self.conexion.Archivo['Ticket'].tolist()
        Enlace_Ticket = EnlacesTicket[SiguienteTicket-1]
        webbrowser.get('chrome').open(Enlace_Ticket)
        print("Ticket Actualizado")

    def AP_Fell_Treewell_Bot(self):
        self.vars.Locacion(self.TicketCode)
        campos = CambiarCampos(self.TicketCode, self.vars, self.entry2)
        campos.DiaNoche()
        campos.AP_Fell_Treewell()
        EnlacesTicket = self.conexion.Archivo['Ticket'].tolist()
        Enlace_Ticket = EnlacesTicket[SiguienteTicket-1]
        webbrowser.get('chrome').open(Enlace_Ticket)
        print("Ticket Actualizado")

def Atras():
    print("hola")

BotonFellWalkside = tk.Button(root, text="AP Walkside", command=lambda: ProcesadorTickets(vars, entry, entry2, conexion).AP_Fell_Walkside_Bot())
BotonFellTreewell = tk.Button(root, text="AP Treewell", command=lambda: ProcesadorTickets(vars, entry, entry2, conexion).AP_Fell_Treewell_Bot())
BotonNoNecessary = tk.Button(root, text="Not Necessary", command=lambda: ProcesadorTickets(vars, entry, entry2, conexion).Not_Necessary_Bot())
BotonHitObjectAP = tk.Button(root, text="AP Collision Static", command=lambda: ProcesadorTickets(vars, entry, entry2, conexion).AP_Proximity_Static_Bot())
BotonSiguiente = tk.Button(root, text="Siguiente", command=conexion.LeerLocal)
BotonRetraining = tk.Button(root, text="Retraining")
BotonAtras = tk.Button(root, text="Atras", command=Atras)

BotonFellTreewell.grid(row=2, column=1)
BotonFellWalkside.grid(row=2, column=0)
BotonHitObjectAP.grid(row=2, column=2)
BotonNoNecessary.grid(row=3, column=0)
BotonRetraining.grid(row=4, column=0)
BotonSiguiente.grid(row=9, column=3)
BotonAtras.grid(row=9, column=0)

root.mainloop()
