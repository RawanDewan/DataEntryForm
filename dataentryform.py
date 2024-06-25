import tkinter
from tkinter import ttk
from tkinter import messagebox
def save_data():
    fname=fnameentry.get()
    lname = lnameentry.get()
    if fname!='' and lname!='':
        title=titlecombo.get()
        age=agespinbox.get()
        nationality=nationalitycombo.get()
        registered=reg_status.get()

        print('First Name:',fname,'\tLast Name:',lname)
        print('Title:',title,'\tAge:',age,'\tNationality:',nationality)
        print(registered)

        with open('students.txt','a') as fwrite:
            fwrite.write(fname+' '+lname+' '+title+' '+str(age)+' '+nationality+' '+registered+'\n')

        print('Saved')
    else:
        tkinter.messagebox.showwarning(title='Error: Missing Data',message='First Name and Last Name required to save data!')

window= tkinter.Tk()
window.title('Data Entry Form')

frame= tkinter.Frame(window)
frame.pack()

userinfoframe=tkinter.LabelFrame(frame,text='User Information')
userinfoframe.grid(row=0,column=0)

fnamelabel=tkinter.Label(userinfoframe,text='First Name')
fnamelabel.grid(row=0,column=0)

fnameentry=tkinter.Entry(userinfoframe)
fnameentry.grid(row=0,column=1)

lnamelabel=tkinter.Label(userinfoframe,text='Last Name')
lnamelabel.grid(row=0,column=2)

lnameentry=tkinter.Entry(userinfoframe)
lnameentry.grid(row=0,column=3)

titlelabel=tkinter.Label(userinfoframe,text='Title')
titlecombo=ttk.Combobox(userinfoframe,values=["","Mr",'Mrs','Ms','Dr'])
titlelabel.grid(row=1,column=0)
titlecombo.grid(row=1,column=1)

agelabel=tkinter.Label(userinfoframe,text='Age')
agespinbox=tkinter.Spinbox(userinfoframe,from_=18,to=50)
agelabel.grid(row=1,column=2)
agespinbox.grid(row=1,column=3)

countries=['AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA', 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA AND HERZEGOVINA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL', 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS', 'CONGO', 'CONGO, THE DEMOCRATIC REPUBLIC OF', 'COOK ISLANDS', 'COSTA RICA', "CÃ”TE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'DENMARK', 'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES', 'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS', 'HONDURAS', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN, ISLAMIC REPUBLIC OF', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'KOREA, REPUBLIC OF', 'KUWAIT', 'KYRGYZSTAN', "LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYAN ARAB JAMAHIRIYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA, REPUBLIC OF', 'MONACO', 'MONGOLIA', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PALESTINIAN TERRITORY, OCCUPIED', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'RÃ‰UNION', 'ROMANIA', 'RUSSIAN FEDERATION', 'RWANDA', 'SAINT HELENA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS', 'SPAIN', 'SRI LANKA', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIAN ARAB REPUBLIC', 'TAIWAN, PROVINCE OF CHINA', 'TAJIKISTAN', 'TANZANIA, UNITED REPUBLIC OF', 'THAILAND', 'TIMOR', 'TOGO', 'TOKELAU', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VIET NAM', 'VIRGIN ISLANDS, BRITISH', 'VIRGIN ISLANDS, U.S.', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZIMBABWE']
nationalitylabel=tkinter.Label(userinfoframe,text='Nationality')
nationalitycombo=ttk.Combobox(userinfoframe,values=countries)
nationalitylabel.grid(row=2,column=0)
nationalitycombo.grid(row=2,column=1)


courseframe=tkinter.LabelFrame(frame,text='Registration')
courseframe.grid(row=1,column=0)

registeredlabel=tkinter.Label(courseframe,text='Registered?')
reg_status=tkinter.StringVar()
regcheck=tkinter.Checkbutton(courseframe,text='Currently Registered',variable=reg_status,onvalue='Registered',
                             offvalue='Not Registered')
registeredlabel.grid(row=0,column=0)
regcheck.grid(row=0,column=1)

savebtn=tkinter.Button(frame,text='Save',command=save_data)
savebtn.grid(row=2,column=0)
window.mainloop()
