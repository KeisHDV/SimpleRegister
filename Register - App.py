import tkinter as tk
import csv
import pandas as pd

class CSVEditor:
    def __init__(self, master):
        self.master = master
        master.title("CSV Editor")
        self.root = root
        self.root.geometry("500x500")
        # create input fields
        self.filename_label = tk.Label(master, text="Enter file name:")
        self.filename_entry = tk.Entry(master)
        self.name_label = tk.Label(master, text="Enter Name:")
        self.name_entry = tk.Entry(master)
        self.age_label = tk.Label(master, text="Enter Age:")
        self.age_entry = tk.Entry(master)
        self.DoB_label = tk.Label(master, text="Enter Date of Birth:")
        self.DoB_entry = tk.Entry(master)
        self.gender_label = tk.Label(master, text="Enter the Gender:")
        self.gender_entry = tk.Entry(master)
        self.diet_req_label = tk.Label(master, text="Enter Dietary Requirements:")
        self.diet_req_entry = tk.Entry(master)
        self.medical_cond_label = tk.Label(master, text="Enter any Medical Conditions:")
        self.medical_cond_entry = tk.Entry(master)
        self.medication_label = tk.Label(master, text="Enter any Medication:")
        self.medication_entry = tk.Entry(master)
        self.sen_label = tk.Label(master, text="Enter any SEN:")
        self.sen_entry = tk.Entry(master)
        self.pregnant_label = tk.Label(master, text="Enter whether Pregnant:")
        self.pregnant_entry = tk.Entry(master)
        self.disabled_label = tk.Label(master, text="Enter any Disabilities:")
        self.disabled_entry = tk.Entry(master)
        self.mental_health_cond_label = tk.Label(master, text="Enter any Mental Health Conditions:")
        self.mental_health_cond_entry = tk.Entry(master)
        self.photo_label = tk.Label(master, text="Are they allowed to be in Photos:")
        self.photo_entry = tk.Entry(master)
        self.contact_name_label = tk.Label(master, text="Enter Contact Name:")
        self.contact_name_entry= tk.Entry(master)
        self.emergency_contact_label = tk.Label(master, text="Enter Emergency Contact:")
        self.emergency_contact_entry = tk.Entry(master)
        self.address_label = tk.Label(master, text="Enter Participants Address:")
        self.address_entry = tk.Entry(master)
        self.extra_info_label = tk.Label(master, text="Any Extra Information:")
        self.extra_info_entry = tk.Entry(master)


        # create buttons
        self.create_button = tk.Button(master, text="Create new file", command=self.create_file)
        self.append_button = tk.Button(master, text="Append data", command=self.append_data)
        self.load_all_button = tk.Button(master, text="Load all data", command=self.load_all_data)
        self.filtered_by_name_button = tk.Button(master, text="Load by Name", command=self.filtered_by_name)
        self.filtered_by_diet_req_button = tk.Button(master, text="Load By Diet", command=self.filtered_by_diet_req)
        self.clear_data_button = tk.Button(master, text="Clear Data", command=self.clear_data)
        self.filtered_by_sen_button = tk.Button(master, text="Load by SEN", command=self.filtered_by_sen)
        
        # layout widgets
        self.filename_label.grid(row=0, column=0, sticky="W")
        self.filename_entry.grid(row=0, column=1)
        self.name_label.grid(row=2, column=0, sticky="W")
        self.name_entry.grid(row=2, column=1)
        self.age_label.grid(row=3, column=0, sticky="W")
        self.age_entry.grid(row=3, column=1)
        self.DoB_label.grid(row=4, column=0, sticky="W")
        self.DoB_entry.grid(row=4, column=1)
        self.gender_label.grid(row=5, column=0, sticky="W")
        self.gender_entry.grid(row=5, column=1)
        self.diet_req_label.grid(row=6, column=0, sticky="W")
        self.diet_req_entry.grid(row=6, column=1)
        self.medical_cond_label.grid(row=7, column=0, sticky="W")
        self.medical_cond_entry.grid(row=7, column=1)
        self.medication_label.grid(row=8, column=0, sticky="W")
        self.medication_entry.grid(row=8, column=1)
        self.sen_label.grid(row=9, column=0, sticky="W")
        self.sen_entry.grid(row=9, column=1)
        self.pregnant_label.grid(row=10, column=0, sticky="W")
        self.pregnant_entry.grid(row=10, column=1)
        self.disabled_label.grid(row=11, column=0, sticky="W")
        self.disabled_entry.grid(row=11, column=1)
        self.mental_health_cond_label.grid(row=12, column=0, sticky="W")
        self.mental_health_cond_entry.grid(row=12, column=1)
        self.photo_label.grid(row=13, column=0, sticky="W")
        self.photo_entry.grid(row=13, column=1)
        self.contact_name_label.grid(row=14, column=0, sticky="W")
        self.contact_name_entry.grid(row=14, column=1)
        self.emergency_contact_label.grid(row=15, column=0, sticky="W")
        self.emergency_contact_entry.grid(row=15, column=1)
        self.address_label.grid(row=16, column=0, sticky="W")
        self.address_entry.grid(row=16, column=1)
        self.extra_info_label.grid(row=17, column=0, sticky="W")
        self.extra_info_entry.grid(row=17, column=1)
        self.create_button.grid(row=18, column=0)
        self.append_button.grid(row=18, column=1)
        self.load_all_button.grid(row=19, column=0)
        self.filtered_by_name_button.grid(row=19, column=1)  
        self.filtered_by_diet_req_button.grid(row=20, column=0) 
        self.filtered_by_sen_button.grid(row=20, column=1)
        self.clear_data_button.grid(row=21, column=0) 
        

    def create_file(self):
        filename = self.filename_entry.get() + ".csv"
        header = ['Number', 'Name', 'Age', 'Date of Birth', 'Gender' , 'Dietary Req.' , 'Medical Cond.' , 'Medication' , 'SEN' , 'Pregnancy' , 'Disability' , 'Mental Health Cond.' , 'Photo Perm.' ,'Contact Name', 'Emergency Contact', 'Participants Address', 'Extra Info']
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
        print(f"File {filename} created with header: {header}")
        
    def append_data(self):
        filename = self.filename_entry.get() + ".csv"
        name = self.name_entry.get()
        age = self.age_entry.get()
        DoB = self.DoB_entry.get()
        gender = self.gender_entry.get()
        diet_req = self.diet_req_entry.get()
        medical_cond = self.medical_cond_entry.get()
        medication = self.medication_entry.get()
        sen = self.sen_entry.get()
        pregnant = self.pregnant_entry.get()
        disabled = self.disabled_entry.get()
        mental_health_cond = self.mental_health_cond_entry.get()
        photo = self.photo_entry.get()
        contact_name = self.contact_name_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        address = self.address_entry.get()
        extra_info = self.extra_info_entry.get()
        with open(filename, "a", newline="") as f:
            df = pd.read_csv(filename)
            new_data = pd.DataFrame({'Name': [name], 'Age': [age], 'Date of Birth': [DoB], 'Gender': [gender], 'Dietary Req.': [diet_req], 'Medical Cond.': [medical_cond], 'Medication': [medication], 'SEN': [sen], 'Pregnancy': [pregnant], 'Disability': [disabled], 'Mental Health Cond.': [mental_health_cond], 'Photo Perm.': [photo],'Contact Name': [contact_name] ,'Emergency Contact': [emergency_contact], "Participant's Address": [address], 'Extra Info': [extra_info]})
            
        new_data.to_csv(filename, mode='a', header=False)
        print('Appended Successfully')
        
    def load_all_data(self):
        filename = self.filename_entry.get() + ".csv"
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            
            popup = tk.Toplevel()
            popup.title("Data Output")
            popup.geometry("2200x300")
            # Add Text widget to display data
            output_text = tk.Text(popup, height=100, width=500)
            output_text.pack()

             # Get data from CSV file and display in Text widget
            with open(filename , 'r') as file:
                df = pd.read_csv(filename)
            output_text.insert(tk.END, df.to_string())

    def filtered_by_name(self):
        filename = self.filename_entry.get() + ".csv"     
        name = self.name_entry.get()
        with open(filename, newline="") as f:
             reader = csv.reader(f)
             
             popup = tk.Toplevel()
             popup.title("Data Output")
             popup.geometry("2000x300")
             output_text = tk.Text(popup, height=100, width=500)
             output_text.pack()

        with open(filename , 'r') as file:
            df = pd.read_csv(filename)
            search_value = name
            value_check = df['Name'] == search_value
            pd.set_option('display.max_columns', None)
            output_text.insert(tk.END, df[value_check].to_string())

    def filtered_by_diet_req(self):
        filename = self.filename_entry.get() + ".csv"     
        diet_req = self.diet_req_entry.get()
        with open(filename, newline="") as f:
             reader = csv.reader(f)
             
             popup = tk.Toplevel()
             popup.title("Data Output")
             popup.geometry("2000x300")
             output_text = tk.Text(popup, height=100, width=500)
             output_text.pack()

        with open(filename , 'r') as file:
            df = pd.read_csv(filename)
            search_value = diet_req
            value_check = df['Dietary Req.'] == search_value
            output_text.insert(tk.END, df[value_check].to_string())


    def filtered_by_sen(self):
        filename = self.filename_entry.get() + ".csv"     
        sen = self.sen_entry.get()
        with open(filename, newline="") as f:
             reader = csv.reader(f)
             
             popup = tk.Toplevel()
             popup.title("Data Output")
             popup.geometry("2000x300")
             output_text = tk.Text(popup, height=100, width=500)
             output_text.pack()

        with open(filename , 'r') as file:
            df = pd.read_csv(filename)
            search_value = sen
            value_check = df['SEN'] == search_value
            output_text.insert(tk.END, df[value_check].to_string())


    def clear_data(self):
        name = self.name_entry
        age = self.age_entry
        DoB = self.DoB_entry
        gender = self.gender_entry
        diet_req = self.diet_req_entry
        medical_cond = self.medical_cond_entry
        medication = self.medication_entry
        sen = self.sen_entry
        pregnant = self.pregnant_entry
        disabled = self.disabled_entry
        mental_health_cond = self.mental_health_cond_entry
        photo = self.photo_entry
        contact_name = self.contact_name_entry
        emergency_contact = self.emergency_contact_entry
        address = self.address_entry
        extra_info = self.extra_info_entry
        name.delete(0, tk.END)
        age.delete(0, tk.END)
        DoB.delete(0, tk.END)
        gender.delete(0, tk.END)
        diet_req.delete(0, tk.END)
        medical_cond.delete(0, tk.END)
        medication.delete(0, tk.END)
        sen.delete(0, tk.END)
        pregnant.delete(0, tk.END)
        disabled.delete(0, tk.END)
        mental_health_cond.delete(0, tk.END)
        photo.delete(0, tk.END)
        contact_name.delete(0, tk.END)
        emergency_contact.delete(0, tk.END)
        address.delete(0, tk.END)
        extra_info.delete(0, tk.END)
                    
root = tk.Tk()
app = CSVEditor(root)
root.mainloop()



