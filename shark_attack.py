#!/usr/bin/env python
# coding: utf-8

# In[95]:


#Importing the dataset

import pandas as pd
sharks_df = pd.read_excel("https://www.sharkattackfile.net/spreadsheets/GSAF5.xls")
sharks_df


# # Examining the data 

# In[96]:


sharks_df.nunique()


# In[97]:


sharks_df["Country"].value_counts().head(20)


# In[98]:


sharks_df["Activity"].value_counts()


# In[99]:


sharks_df["Location"].value_counts()


# In[100]:


sharks_df["Year"].value_counts()


# In[101]:


sharks_df["Type"].value_counts()


# In[102]:


sharks_df["Year"].value_counts().head(20)


# In[103]:


sharks_usa_df = sharks_df.loc[sharks_df['Country'] == "USA"]
sharks_usa_df["Location"].value_counts()


# In[104]:


sharks_df["State"].value_counts()


# In[105]:


sharks_df.isna().any()


# In[106]:


sharks_df.isna().sum()


# In[107]:


sharks_df.shape


# # Cleaning the data

# In[108]:


# Droping empty rows

sharks_df.dropna(how = "all", inplace = True)


# In[109]:


sharks_df.shape


# In[110]:


# Dropping rows with less than 2 values populated

sharks_df.dropna(thresh = 2, inplace = True)


# In[111]:


sharks_df.duplicated().sum()


# In[112]:


sharks_df.shape


# In[113]:


sharks_df['original order'].value_counts()


# In[114]:


sharks_df['Case Number.1'].value_counts()


# In[115]:


sharks_df.dtypes


# In[116]:


#Dropping un-important columns

columns_to_drop = ['Unnamed: 21', 'Unnamed: 22', 'href', 'pdf', 'href formula', 'Source', 'Name', 'Unnamed: 11', 'Case Number.1']
sharks_df.drop(columns_to_drop, axis=1, inplace=True)


# In[118]:


sharks_df


# In[119]:


sharks_df.isna().sum()


# In[120]:


sharks_df.dtypes


# # Cleaning data

# In[121]:


# Cleaning Age column

sharks_df['Age'].unique()


# In[122]:


age_dict = {"30s": 35, "20": 25, "!2": 2, "50s": 50, "40s": 40, "teen": 15, "Teen": 15, "M": 20, "!6": 6, "60s": 65,"a": 20, "!!": 20, "Teens": 15, "\xa0": 20, "": 20, "mid": 30, "Elderly": 60, "Ca.": 20, ">50": 55, "adult": 20,"(adult)": 20, "X": 20, "middle": 30, "MAKE": 20, "F": 20, "Both": 20, "young": 10, "A.M.": 20}


# In[123]:


sharks_df['Age'] = sharks_df['Age'].map(age_dict).fillna(sharks_df['Age'])


# In[124]:


age_dict = {
    'teen': 15,
    'a minor': 10,
    'Elderly': 70,
    'mid-30s': 35,
    '30s': 35,
    '20s': 25,
    '20/30': 25,
    '40s': 40,
    '50s': 50,
    '60s': 60,
    'mid-20s': 25,
    '18 months': 2,
    '18 or 20': 19,
    '20\'s': 25,
    '21 & ?': 21,
    '30 or 36': 33,
    '6½': 6,
    '60\'s': 60,
    '2 to 3 months': 0,
    'MAKE LINE GREEN': 20,
    '\xa0 ': 20,
    ' ': 20,
    'X': 20,
    '"middle-age"': 35,
    '"young"': 10,
    'Both 11': 11,
    '7 or 8': 7,
    '9 or 10': 9,
    '10 or 12': 11,
    '31 or 33': 32,
    '2½': 2,
    '1': 1,
    '13 or 14': 13
}


# In[125]:


sharks_df['Age'] = sharks_df['Age'].map(age_dict).fillna(sharks_df['Age'])


# In[126]:


sharks_df['Age'].unique()


# In[127]:


cleaning_dict = {
    'teen': 15,
    'M': 20,
    '!2': 2,
    '!!': 20,
    '!6': 6,
    'Teen': 15,
    '45 and 15': 30, 
    '28 & 22': 25,  
    '22, 57, 31': 36,  
    'Teens': 15,
    '9 & 60': 34.5, 
    '23': 23,
    '12': 12,
    '36': 36,
    '63': 63,
    '71': 71,
    '48': 48,
    '70': 70,
    '57': 57,
    '7': 7,
    '28': 28,
    '33': 33,
    '61': 61,
    '74': 74,
    '27': 27,
    '3': 3,
    '56': 56,
    '28 & 26': 27,  
    '5': 5,
    '54': 54,
    '12 or 13': 12.5,  
    '46 & 34': 40, 
    '28, 23 & 30': 27, 
    '36 & 26': 31,  
    '8 or 10': 9,  
    '33 or 37': 35, 
    '23 & 20': 21.5,  
    ' 30': 30,
    '7      &    31': 19,  
    '20?': 20,
    '32 & 30': 31,  
    '16 to 18': 17, 
    'Ca. 33': 33,
    '74 ': 74,
    '45 ': 45,
    '21 or 26': 23.5, 
    '20 ': 20,
    '>50': 55,
    '18 to 22': 20,  
    'adult': 20,
    '9 & 12': 10.5, 
    '? & 19': 19,
    '9 months': 0.75,  
    '25 to 35': 30,  
    '23 & 26': 24.5, 
    '(adult)': 20,
    '33 & 37': 35,  
    '25 or 28': 26.5, 
    '37, 67, 35, 27,  ? & 27': 38.6,
    '21, 34,24 & 35': 28.5,  
    '30 & 32': 31,  
    '50 & 30': 40,  
    '17 & 35': 26,  
    '13 or 18': 15.5,  
    '34 & 19': 26.5,  
    '33 & 26': 29.5,  
    '4': 4,
    ' 43': 43,
    '17 & 16': 16.5,  
    'F': 20,
    'young': 10,
    '36 & 23': 29.5,  
    '  ': 20,
    'A.M.': 20,
    '?    &   14': 14
}


# In[128]:


sharks_df['Age'] = sharks_df['Age'].map(cleaning_dict).fillna(sharks_df['Age'])


# In[129]:


sharks_df['Age'].unique()


# In[130]:


sharks_df['Age'] = sharks_df['Age'].apply(float) 


# In[131]:


sharks_df['Age'].unique()


# In[132]:


filtered_df['Age'].value_counts().head(10)


# In[133]:


sharks_df['Age'].isna().sum()


# ### FILL NULL VALUES FOR AGE

# In[134]:


sharks_df['Sex'].unique()


# In[135]:


sharks_df['Sex'].value_counts()


# In[136]:


sex_dict = {"M":"M", "F":"F", " M":"M", "M ":"M", "lli":"M", "M x 2":"M", ".":"M"}


# In[137]:


sharks_df['Sex'] = sharks_df['Sex'].map(sex_dict)


# In[138]:


sharks_df['Sex'].unique()


# In[139]:


sharks_df['Sex'].value_counts()


# In[140]:


sharks_df['Sex'].isna().sum()


# ### FILL NULL VALUES FOR SEX

# In[141]:


sharks_df['Country'].isna().sum()


# In[142]:


cleaning_dict_countries = {
    'AUSTRALIA': 'AUSTRALIA',
    'USA': 'USA',
    'INDIA': 'INDIA',
    'TRINIDAD': 'TRINIDAD & TOBAGO',
    'BAHAMAS': 'BAHAMAS',
    'SOUTH AFRICA': 'SOUTH AFRICA',
    'MEXICO': 'MEXICO',
    'NEW ZEALAND': 'NEW ZEALAND',
    'EGYPT': 'EGYPT',
    'Mexico': 'MEXICO',
    'BELIZE': 'BELIZE',
    'PHILIPPINES': 'PHILIPPINES',
    'Coral Sea': 'AUSTRALIA',
    'SPAIN': 'SPAIN',
    'PORTUGAL': 'PORTUGAL',
    'SAMOA': 'SAMOA',
    'COLOMBIA': 'COLOMBIA',
    'ECUADOR': 'ECUADOR',
    'FRENCH POLYNESIA': 'FRENCH POLYNESIA',
    'NEW CALEDONIA': 'NEW CALEDONIA',
    'TURKS and CaICOS': 'TURKS & CAICOS',    ######## atlantic / carribean
    'CUBA': 'CUBA',
    'BRAZIL': 'BRAZIL',
    'SEYCHELLES': 'SEYCHELLES',
    'ARGENTINA': 'ARGENTINA',
    'FIJI': 'FIJI',
    'MeXICO': 'MEXICO',
    'Maldives': 'MALDIVES',
    'South Africa': 'SOUTH AFRICA',
    'ENGLAND': 'ENGLAND',
    'JAPAN': 'JAPAN',
    'INDONESIA': 'INDONESIA',
    'JAMAICA': 'JAMAICA',
    'MALDIVES': 'MALDIVES',
    'THAILAND': 'THAILAND',
    'COLUMBIA': 'COLOMBIA',
    'COSTA RICA': 'COSTA RICA',
    'New Zealand': 'NEW ZEALAND',
    'British Overseas Territory': 'British Overseas Territory',
    'CANADA': 'CANADA',
    'JORDAN': 'JORDAN',
    'ST KITTS / NEVIS': 'ST KITTS / NEVIS', ###### atlantic / carribean
    'ST MARTIN': 'ST MARTIN',      ############# carribean
    'PAPUA NEW GUINEA': 'PAPUA NEW GUINEA',  #######  australia
    'REUNION ISLAND': 'REUNION ISLAND',
    'ISRAEL': 'ISRAEL',
    'CHINA': 'CHINA',
    'IRELAND': 'IRELAND',
    'ITALY': 'ITALY',
    'MALAYSIA': 'MALAYSIA',
    'LIBYA': 'LIBYA',
    'MAURITIUS': 'MAURITIUS',
    'SOLOMON ISLANDS': 'SOLOMON ISLANDS',   ########## Australia
    'ST HELENA, British overseas territory': 'ST HELENA, British overseas territory',
    'COMOROS': 'COMOROS',
    'REUNION': 'REUNION',
    'UNITED KINGDOM': 'UNITED KINGDOM',
    'UNITED ARAB EMIRATES': 'UNITED ARAB EMIRATES',
    'CAPE VERDE': 'CAPE VERDE',
    'DOMINICAN REPUBLIC': 'DOMINICAN REPUBLIC',
    'CAYMAN ISLANDS': 'CAYMAN ISLANDS',    ############# carribean
    'ARUBA': 'ARUBA',      ############# carribean
    'MOZAMBIQUE': 'MOZAMBIQUE',
    'PUERTO RICO': 'PUERTO RICO',
    'ATLANTIC OCEAN': 'ATLANTIC OCEAN',
    'GREECE': 'GREECE',
    'ST. MARTIN': 'ST. MARTIN',    ############# carribean
    'FRANCE': 'FRANCE',
    'TRINIDAD & TOBAGO': 'TRINIDAD & TOBAGO',
    'KIRIBATI': 'KIRIBATI',        
    'DIEGO GARCIA': 'DIEGO GARCIA',
    'TAIWAN': 'TAIWAN',
    'PALESTINIAN TERRITORIES': 'PALESTINIAN TERRITORIES',
    'GUAM': 'GUAM',
    'NIGERIA': 'NIGERIA',
    'TONGA': 'TONGA',
    'SCOTLAND': 'SCOTLAND',
    'CROATIA': 'CROATIA',
    'SAUDI ARABIA': 'SAUDI ARABIA',
    'CHILE': 'CHILE',
    'ANTIGUA': 'ANTIGUA',
    'KENYA': 'KENYA',
    'RUSSIA': 'RUSSIA',
    'TURKS & CAICOS': 'TURKS & CAICOS',
    'UNITED ARAB EMIRATES (UAE)': 'UNITED ARAB EMIRATES',
    'AZORES': 'AZORES',
    'SOUTH KOREA': 'SOUTH KOREA',
    'MALTA': 'MALTA',
    'VIETNAM': 'VIETNAM',
    'MADAGASCAR': 'MADAGASCAR',
    'PANAMA': 'PANAMA',
    'SOMALIA': 'SOMALIA',
    'NEVIS': 'NEVIS',
    'BRITISH VIRGIN ISLANDS': 'BRITISH VIRGIN ISLANDS',
    'NORWAY': 'NORWAY',
    'SENEGAL': 'SENEGAL',
    'YEMEN': 'YEMEN',
    'GULF OF ADEN': 'GULF OF ADEN',
    'Sierra Leone': 'Sierra Leone',
    'ST. MAARTIN': 'ST MARTIN',          ############# carribean
    'GRAND CAYMAN': 'GRAND CAYMAN',      ############# carribean
    'Seychelles': 'SEYCHELLES',
    'LIBERIA': 'LIBERIA',
    'VANUATU': 'VANUATU',
    'MEXICO ': 'MEXICO',
    'HONDURAS': 'HONDURAS',
    'VENEZUELA': 'VENEZUELA',
    'SRI LANKA': 'SRI LANKA',
    ' TONGA': 'TONGA',
    'URUGUAY': 'URUGUAY',
    'MICRONESIA': 'MICRONESIA',
    'CARIBBEAN SEA': 'CARIBBEAN SEA', ###### carribean
    'OKINAWA': 'OKINAWA',
    'TANZANIA': 'TANZANIA',
    'MARSHALL ISLANDS': 'MARSHALL ISLANDS',      ###### pacific
    'EGYPT / ISRAEL': 'EGYPT',
    'NORTHERN ARABIAN SEA': 'NORTHERN ARABIAN SEA',
    'HONG KONG': 'HONG KONG',
    'EL SALVADOR': 'EL SALVADOR',
    'ANGOLA': 'ANGOLA',
    'BERMUDA': 'BERMUDA',
    'MONTENEGRO': 'MONTENEGRO',
    'IRAN': 'IRAN',
    'TUNISIA': 'TUNISIA',
    'NAMIBIA': 'NAMIBIA',
    'NORTH ATLANTIC OCEAN': 'NORTH ATLANTIC OCEAN',      ####### atlantic
    'SOUTH CHINA SEA': 'SOUTH CHINA SEA',
    'BANGLADESH': 'BANGLADESH',
    'PALAU': 'PALAU',
    'WESTERN SAMOA': 'SAMOA',
    'PACIFIC OCEAN ': 'PACIFIC OCEAN',     ###### pacific
    'BRITISH ISLES': 'BRITISH ISLES',
    'GRENADA': 'GRENADA',
    'IRAQ': 'IRAQ',
    'TURKEY': 'TURKEY',
    'SINGAPORE': 'SINGAPORE',
    'NEW BRITAIN': 'NEW BRITAIN',
    'SUDAN': 'SUDAN',
    'JOHNSTON ISLAND': 'JOHNSTON ISLAND',
    'SOUTH PACIFIC OCEAN': 'SOUTH PACIFIC OCEAN',     #### pacific
    'NEW GUINEA': 'NEW GUINEA',
    'RED SEA': 'EGYPT',
    'NORTH PACIFIC OCEAN': 'NORTH PACIFIC OCEAN',         ########pacific
    'FEDERATED STATES OF MICRONESIA': 'MICRONESIA',        ####### pacific
    'MID ATLANTIC OCEAN': 'MID ATLANTIC OCEAN',        ####### atlantic
    'ADMIRALTY ISLANDS': 'ADMIRALTY ISLANDS',         ######### South Pacific Ocean
    'BRITISH WEST INDIES': 'BRITISH WEST INDIES',      ##### Atlantic 
    'SOUTH ATLANTIC OCEAN': 'SOUTH ATLANTIC OCEAN',  ######  Atlantic 
    'PERSIAN GULF': 'ARAB GULF',
    'RED SEA / INDIAN OCEAN': 'EGYPT',
    'PACIFIC OCEAN': 'PACIFIC OCEAN', ############ pacific
    'NORTH SEA': 'NORTH SEA',
    'NICARAGUA ': 'NICARAGUA',   ######### carribean
    'MALDIVE ISLANDS': 'MALDIVE ISLANDS',    ###### carribean
    'AMERICAN SAMOA': 'SAMOA',       ####### pacific
    'ANDAMAN / NICOBAR ISLANDAS': 'ANDAMAN / NICOBAR ISLANDAS',
    'GABON': 'GABON',
    'MAYOTTE': 'MADAGASCAR',
    'NORTH ATLANTIC OCEAN ': 'NORTH ATLANTIC OCEAN', ########### atlantic
    'THE BALKANS': 'GREECE',
    'SUDAN?': 'SUDAN',
    'MARTINIQUE': 'MARTINIQUE',  ###### carribean
    'INDIAN OCEAN': 'INDIAN OCEAN',   ########### indian
    'GUATEMALA': 'GUATEMALA',
    'NETHERLANDS ANTILLES': 'NETHERLANDS ANTILLES', ###### carribean
    'NORTHERN MARIANA ISLANDS': 'NORTHERN MARIANA ISLANDS',   ####### pacific
    'IRAN / IRAQ': 'IRAN',
    'JAVA': 'JAVA',    ######### indian
    'SIERRA LEONE': 'SIERRA LEONE',
    ' PHILIPPINES': 'PHILIPPINES',
    'NICARAGUA': 'NICARAGUA',          ######### carribean
    'CENTRAL PACIFIC': 'CENTRAL PACIFIC',   ########## pacific
    'SOLOMON ISLANDS / VANUATU': 'SOLOMON ISLANDS / VANUATU',
    'SOUTHWEST PACIFIC OCEAN': 'SOUTHWEST PACIFIC OCEAN',   ##### pacific
    'BAY OF BENGAL': 'BAY OF BENGAL',       ##########   indidan 
    'MID-PACIFC OCEAN': 'MID-PACIFC OCEAN',   ##### pacific
    'SLOVENIA': 'SLOVENIA',
    'CURACAO': 'CURACAO',  ######### caribean
    'ICELAND': 'ICELAND',
    'ITALY / CROATIA': 'CROATIA',
    'BARBADOS': 'BARBADOS',  ############ caribean
    'MONACO': 'MONACO',
    'GUYANA': 'GUYANA',
    'HAITI': 'HAITI', ############# caribean
    'SAN DOMINGO': 'SAN DOMINGO',        ############# caribean
    'KUWAIT': 'KUWAIT',
    'YEMEN ': 'YEMEN',
    'FALKLAND ISLANDS': 'FALKLAND ISLANDS',
    'CRETE': 'GREECE',
    'CYPRUS': 'CYPRUS',
    'EGYPT ': 'EGYPT',
    'WEST INDIES': 'WEST INDIES',          ########### caribean
    'BURMA': 'BAY OF BENGAL',
    'LEBANON': 'LEBANON',
    'PARAGUAY': 'PARAGUAY',
    'BRITISH NEW GUINEA': 'PAPUA NEW GUINEA',
    'CEYLON': 'SRI LANKA',
    'OCEAN': 'OCEAN',
    'GEORGIA': 'GEORGIA',
    'SYRIA': 'SYRIA',
    'TUVALU': 'TUVALU',               #########   ocenia
    'INDIAN OCEAN?': 'INDIAN OCEAN',
    'GUINEA': 'GUINEA',
    'ANDAMAN ISLANDS': 'BAY OF BENGAL',
    'EQUATORIAL GUINEA / CAMEROON': 'EQUATORIAL GUINEA',
    'COOK ISLANDS': 'COOK ISLANDS',    ##### Oceania  
    'TOBAGO': 'TRINIDAD AND TOBAGO', ######### caribean
    'PERU': 'PERU',
    'AFRICA': 'SOUTH AFRICA',
    'ALGERIA': 'ALGERIA',
    'Coast of AFRICA': 'Coast of AFRICA',
    'TASMAN SEA': 'AUSTRALIA',
    'GHANA': 'GHANA',
    'GREENLAND': 'GREENLAND',
    'MEDITERRANEAN SEA': 'MEDITERRANEAN SEA',
    'SWEDEN': 'SWEDEN',
    'ROATAN': 'ROATAN',    ######### CARRIBEAN
    'Between PORTUGAL & INDIA': 'INDIA',
    'DJIBOUTI': 'DJIBOUTI',
    'BAHREIN': 'BAHREIN',
    'KOREA': 'KOREA',
    'RED SEA?': 'EGYPT',
    'ASIA?': 'BAY OF BENGAL',
    'CEYLON (SRI LANKA)': 'SRI LANKA'
}


# In[143]:


country_dict = {
    'AUSTRALIA': 'AUSTRALIA',
    'USA': 'USA',
    'INDIA': 'INDIA',
    'TRINIDAD': 'CARIBBEAN SEA',
    'BAHAMAS': 'CARIBBEAN SEA',
    'SOUTH AFRICA': 'SOUTH AFRICA',
    'MEXICO': 'MEXICO',
    'NEW ZEALAND': 'NEW ZEALAND',
    'EGYPT': 'EGYPT',
    'Mexico': 'MEXICO',
    'BELIZE': 'CARIBBEAN SEA',
    'PHILIPPINES': 'PHILIPPINES',
    'Coral Sea': 'AUSTRALIA',
    'SPAIN': 'SPAIN',
    'PORTUGAL': 'PORTUGAL',
    'SAMOA': 'OCEANIA ISLANDS',
    'COLOMBIA': 'COLOMBIA',
    'ECUADOR': 'ECUADOR',
    'FRENCH POLYNESIA': 'OCEANIA ISLANDS',
    'NEW CALEDONIA': 'OCEANIA ISLANDS',
    'TURKS and CaICOS': 'CARIBBEAN SEA',   
    'CUBA': 'CARIBBEAN SEA',
    'BRAZIL': 'BRAZIL',
    'SEYCHELLES': 'SEYCHELLES',
    'ARGENTINA': 'ARGENTINA',
    'FIJI': 'OCEANIA ISLANDS',
    'MeXICO': 'MEXICO',
    'Maldives': 'MALDIVES',
    'South Africa': 'SOUTH AFRICA',
    'ENGLAND': 'ENGLAND',
    'JAPAN': 'JAPAN',
    'INDONESIA': 'INDONESIA',
    'JAMAICA': 'CARIBBEAN SEA',
    'MALDIVES': 'MALDIVES',
    'THAILAND': 'THAILAND',
    'COLUMBIA': 'COLOMBIA',
    'COSTA RICA': 'CARIBBEAN SEA',
    'New Zealand': 'NEW ZEALAND',
    'British Overseas Territory': 'British Overseas Territory',
    'CANADA': 'CANADA',
    'JORDAN': 'JORDAN',
    'ST KITTS / NEVIS': 'CARIBBEAN SEA', 
    'ST MARTIN': 'CARIBBEAN SEA',      
    'PAPUA NEW GUINEA': 'OCEANIA ISLANDS', 
    'REUNION ISLAND': 'REUNION ISLAND',
    'ISRAEL': 'ISRAEL',
    'CHINA': 'CHINA',
    'IRELAND': 'IRELAND',
    'ITALY': 'ITALY',
    'MALAYSIA': 'MALAYSIA',
    'LIBYA': 'LIBYA',
    'MAURITIUS': 'MAURITIUS',
    'SOLOMON ISLANDS': 'OCEANIA ISLANDS',  
    'ST HELENA, British overseas territory': 'ST HELENA, British overseas territory',
    'COMOROS': 'COMOROS',
    'REUNION': 'REUNION',
    'UNITED KINGDOM': 'UNITED KINGDOM',
    'UNITED ARAB EMIRATES': 'UNITED ARAB EMIRATES',
    'CAPE VERDE': 'CAPE VERDE',
    'DOMINICAN REPUBLIC': 'CARIBBEAN SEA',
    'CAYMAN ISLANDS': 'CARIBBEAN SEA',    
    'ARUBA': 'CARIBBEAN SEA',      
    'MOZAMBIQUE': 'MOZAMBIQUE',
    'PUERTO RICO': 'CARIBBEAN SEA',
    'ATLANTIC OCEAN': 'ATLANTIC OCEAN',
    'GREECE': 'GREECE',
    'ST. MARTIN': 'CARIBBEAN SEA',   
    'FRANCE': 'FRANCE',
    'TRINIDAD & TOBAGO': 'CARIBBEAN SEA',
    'KIRIBATI': 'OCEANIA ISLANDS',        
    'DIEGO GARCIA': 'DIEGO GARCIA',
    'TAIWAN': 'TAIWAN',
    'PALESTINIAN TERRITORIES': 'PALESTINIAN TERRITORIES',
    'GUAM': 'GUAM',
    'NIGERIA': 'NIGERIA',
    'TONGA': 'OCEANIA ISLANDS',
    'SCOTLAND': 'SCOTLAND',
    'CROATIA': 'CROATIA',
    'SAUDI ARABIA': 'SAUDI ARABIA',
    'CHILE': 'CHILE',
    'ANTIGUA': 'CARIBBEAN SEA',
    'KENYA': 'KENYA',
    'RUSSIA': 'RUSSIA',
    'TURKS & CAICOS': 'CARIBBEAN SEA',
    'UNITED ARAB EMIRATES (UAE)': 'UNITED ARAB EMIRATES',
    'AZORES': 'NORTH ATLANTIC OCEAN',
    'SOUTH KOREA': 'SOUTH KOREA',
    'MALTA': 'MALTA',
    'VIETNAM': 'VIETNAM',
    'MADAGASCAR': 'MADAGASCAR',
    'PANAMA': 'PANAMA',
    'SOMALIA': 'SOMALIA',
    'NEVIS': 'CARIBBEAN SEA',
    'BRITISH VIRGIN ISLANDS': 'BRITISH VIRGIN ISLANDS',
    'NORWAY': 'NORWAY',
    'SENEGAL': 'SENEGAL',
    'YEMEN': 'YEMEN',
    'GULF OF ADEN': 'YEMEN',
    'Sierra Leone': 'Sierra Leone',
    'ST. MAARTIN': 'CARIBBEAN SEA',        
    'GRAND CAYMAN': 'CARIBBEAN SEA',     
    'Seychelles': 'SEYCHELLES',
    'LIBERIA': 'LIBERIA',
    'VANUATU': 'OCEANIA ISLANDS',
    'MEXICO ': 'MEXICO',
    'HONDURAS': 'CARIBBEAN SEA',
    'VENEZUELA': 'VENEZUELA',
    'SRI LANKA': 'SRI LANKA',
    ' TONGA': 'TONGA',
    'URUGUAY': 'URUGUAY',
    'MICRONESIA': 'OCEANIA ISLANDS',
    'CARIBBEAN SEA': 'CARIBBEAN SEA',
    'OKINAWA': 'OKINAWA',
    'TANZANIA': 'TANZANIA',
    'MARSHALL ISLANDS': 'OCEANIA ISLANDS',      
    'EGYPT / ISRAEL': 'EGYPT',
    'NORTHERN ARABIAN SEA': 'NORTHERN ARABIAN SEA',
    'HONG KONG': 'HONG KONG',
    'EL SALVADOR': 'EL SALVADOR',
    'ANGOLA': 'ANGOLA',
    'BERMUDA': 'BERMUDA',
    'MONTENEGRO': 'MONTENEGRO',
    'IRAN': 'IRAN',
    'TUNISIA': 'TUNISIA',
    'NAMIBIA': 'NAMIBIA',
    'NORTH ATLANTIC OCEAN': 'NORTH ATLANTIC OCEAN',   
    'SOUTH CHINA SEA': 'SOUTH CHINA SEA',
    'BANGLADESH': 'BANGLADESH',
    'PALAU': 'PALAU',
    'WESTERN SAMOA': 'OCEANIA ISLANDS',
    'PACIFIC OCEAN ': 'PACIFIC OCEAN',  
    'BRITISH ISLES': 'BRITISH ISLES',
    'GRENADA': 'CARIBBEAN SEA',
    'IRAQ': 'IRAQ',
    'TURKEY': 'TURKEY',
    'SINGAPORE': 'SINGAPORE',
    'NEW BRITAIN': 'NEW BRITAIN',
    'SUDAN': 'SUDAN',
    'JOHNSTON ISLAND': 'JOHNSTON ISLAND',
    'SOUTH PACIFIC OCEAN': 'SOUTH PACIFIC OCEAN',   
    'NEW GUINEA': 'NEW GUINEA',
    'RED SEA': 'EGYPT',
    'NORTH PACIFIC OCEAN': 'NORTH PACIFIC OCEAN',       
    'FEDERATED STATES OF MICRONESIA': 'OCEANIA ISLANDS',        
    'MID ATLANTIC OCEAN': 'MID ATLANTIC OCEAN',     
    'ADMIRALTY ISLANDS': 'ADMIRALTY ISLANDS',       
    'BRITISH WEST INDIES': 'CARIBBEAN SEA', 
    'SOUTH ATLANTIC OCEAN': 'SOUTH ATLANTIC OCEAN', 
    'PERSIAN GULF': 'ARAB GULF',
    'RED SEA / INDIAN OCEAN': 'EGYPT',
    'PACIFIC OCEAN': 'PACIFIC OCEAN', 
    'NORTH SEA': 'NORTH SEA',
    'NICARAGUA ': 'CARIBBEAN SEA', 
    'MALDIVE ISLANDS': 'CARIBBEAN SEA',   
    'AMERICAN SAMOA': 'OCEANIA ISLANDS',      
    'ANDAMAN / NICOBAR ISLANDAS': 'BAY OF BENGAL',
    'GABON': 'GABON',
    'MAYOTTE': 'MADAGASCAR',
    'NORTH ATLANTIC OCEAN ': 'NORTH ATLANTIC OCEAN', 
    'THE BALKANS': 'GREECE',
    'SUDAN?': 'SUDAN',
    'MARTINIQUE': 'CARIBBEAN SEA',  
    'INDIAN OCEAN': 'INDIAN OCEAN',   
    'GUATEMALA': 'GUATEMALA',
    'NETHERLANDS ANTILLES': 'CARIBBEAN SEA',
    'NORTHERN MARIANA ISLANDS': 'NORTHERN MARIANA ISLANDS',
    'IRAN / IRAQ': 'IRAN',
    'JAVA': 'JAVA',  
    'SIERRA LEONE': 'SIERRA LEONE',
    ' PHILIPPINES': 'PHILIPPINES',
    'NICARAGUA': 'CARIBBEAN SEA',         
    'CENTRAL PACIFIC': 'OCEANIA ISLANDS',   
    'SOLOMON ISLANDS / VANUATU': 'OCEANIA ISLANDS',
    'SOUTHWEST PACIFIC OCEAN': 'SOUTHWEST PACIFIC OCEAN',   
    'BAY OF BENGAL': 'BAY OF BENGAL',      
    'MID-PACIFC OCEAN': 'MID-PACIFC OCEAN', 
    'SLOVENIA': 'SLOVENIA',
    'CURACAO': 'CARIBBEAN SEA',  
    'ICELAND': 'ICELAND',
    'ITALY / CROATIA': 'CROATIA',
    'BARBADOS': 'CARIBBEAN SEA', 
    'MONACO': 'MONACO',
    'GUYANA': 'GUYANA',
    'HAITI': 'CARIBBEAN SEA',
    'SAN DOMINGO': 'CARIBBEAN SEA',      
    'KUWAIT': 'KUWAIT',
    'YEMEN ': 'YEMEN',
    'FALKLAND ISLANDS': 'FALKLAND ISLANDS',
    'CRETE': 'GREECE',
    'CYPRUS': 'CYPRUS',
    'EGYPT ': 'EGYPT',
    'WEST INDIES': 'CARIBBEAN SEA',        
    'BURMA': 'BAY OF BENGAL',
    'LEBANON': 'LEBANON',
    'PARAGUAY': 'PARAGUAY',
    'BRITISH NEW GUINEA': 'PAPUA NEW GUINEA',
    'CEYLON': 'SRI LANKA',
    'OCEAN': 'OCEAN',
    'GEORGIA': 'GEORGIA',
    'SYRIA': 'SYRIA',
    'TUVALU': 'OCEANIA ISLANDS',            
    'INDIAN OCEAN?': 'INDIAN OCEAN',
    'GUINEA': 'GUINEA',
    'ANDAMAN ISLANDS': 'BAY OF BENGAL',
    'EQUATORIAL GUINEA / CAMEROON': 'EQUATORIAL GUINEA',
    'COOK ISLANDS': 'OCEANIA ISLANDS',   
    'TOBAGO': 'CARIBBEAN SEA', 
    'PERU': 'PERU',
    'AFRICA': 'SOUTH AFRICA',
    'ALGERIA': 'ALGERIA',
    'Coast of AFRICA': 'Coast of AFRICA',
    'TASMAN SEA': 'AUSTRALIA',
    'GHANA': 'GHANA',
    'GREENLAND': 'GREENLAND',
    'MEDITERRANEAN SEA': 'MEDITERRANEAN SEA',
    'SWEDEN': 'SWEDEN',
    'ROATAN': 'CARIBBEAN SEA',   
    'Between PORTUGAL & INDIA': 'INDIA',
    'DJIBOUTI': 'DJIBOUTI',
    'BAHREIN': 'BAHREIN',
    'KOREA': 'KOREA',
    'RED SEA?': 'EGYPT',
    'ASIA?': 'BAY OF BENGAL',
    'CEYLON (SRI LANKA)': 'SRI LANKA'
}


# In[144]:


sharks_df['Country'] = sharks_df['Country'].map(country_dict).fillna(sharks_df['Country'])


# In[145]:


sharks_df['Country'].unique()


# In[146]:


sharks_df['Country'].value_counts().head(20)


# In[147]:


sharks_df['Country'].isna().sum()


# In[148]:


sharks_df[sharks_df['Country'].isna()]


# In[149]:


#sharks_df['Country'].fillna(method = 'bfill', inplace = True)


# ### FILL NULL VALUES FOR COUNTRY

# In[150]:


sharks_df.columns


# In[154]:


sharks_df.columns = ['Date', 'Year', 'Type', 'Country', 'State', 'Location', 'Activity',
       'Sex', 'Age', 'Injury', 'Time', 'Species', 'Case Number',
       'original order']


# In[155]:


sharks_df.columns


# In[156]:


sharks_df


# In[157]:


sharks_df.Species.value_counts()


# In[158]:


sharks_df.Species.value_counts().head(60)


# # Conclusions based on the 4 columns

# - **AGE** regarding the age, almost half of the data is missing, which means we can't draw conclusion based on filling the rest of the data with assumptions
# - **COUNTRY** regarding the country, there are 50 rows which are missing the country, and it wouldn't matter because it's obvious that sharks attacks have been mainly happening in 5 areas, USA, AUSTRALIA, SOUTH AFRICA, OCEANIA CONTINENT, and CARIBBEAN SEA islands and countries. these 5 areas almost share the same hot weather for the summer. 
# - **SEX** regarding the sex, there are 581 rows which have NaN values, which can be filled using the mode.
# - **SPECIES** 
# 
# Shark involvement prior to death was not confirmed  
# Invalid                                             
# Shark involvement not confirmed                      
# Shark involvement prior to death unconfirmed       
# Questionable incident 
# Questionable  
# No shark involvement
# Shark involvement prior to death not confirmed

# In[159]:


dropped_values = ['Shark involvement prior to death was not confirmed','Invalid','Shark involvement not confirmed','Shark involvement prior to death unconfirmed','Questionable incident','Questionable','No shark involvement','Shark involvement prior to death not confirmed']


# In[160]:


x = sharks_df['Species'].isin(dropped_values)
x


# In[161]:


df = sharks_df.copy()
df


# In[162]:


mask = df['Species'].isin(dropped_values)


# In[163]:


filtered_df = df[~mask]


# In[164]:


filtered_df


# In[165]:


filtered_df['Species'].value_counts().head(20)


# In[166]:


filtered_df = filtered_df.reset_index(drop=True)


# In[167]:


filtered_df


# In[168]:


filtered_df.dtypes


# In[169]:


filtered_df['Time'].unique()


# In[170]:


fixed_times = {
    "Early Morning": "05h45",
    "Afternoon": "16h30",
    '"Midday"': "13h00",
    "Night": "23h45",
    "Morning": "08h00",
    "Evening": "20h00",
    "Before 10h00": "08h00",
    "Late afternoon": "17h50",
    "19h00, Dusk": "19h00",
    "Midday": "12h00",
    "Shortly before 12h00": "11h45",
    "After noon": "15h00",
    "Morning ": "08h00",
    "18h15-18h30": "18h23",
    "09h00 - 09h30": "09h15",
    "0830": "08h30",
    "1600": "16h00",
    "Early afternoon": "13h45",
    "15j45": "15h45",
    "Before 07h00": "06h00",
    "Dusk": "23h00",
    '"Just before 11h00"': "10h45",
    "11h115": "11h15",
    "Just before sundown": "20h30",
    "17h00 or 17h40": "17h20",
    ">08h00": "07h00",
    "--": "12h00",
    "Just after 12h00": "12h30",
    " ": "09h30",
    "Shortly after midnight": "00h45",
    "\xa0 ": "15h30",
    "09h00 -10h00": "09h30",
    "20h45 (Sunset)": "20h45",
    "Sunset": "20h30",
    "Late morning": "11h00",
    "Shortly before 13h00": "12h45",
    "8:04 pm": "20h04",
    "2 hours after Opperman": "20h45",
    "09h30 ": "09h30",
    "11h00 / 11h30": "11h15",
    '"Night"': "00h00",
    "18h30?": "18h30",
    "A.M.": "09h00",
    ">06h45": "06h00",
    "Between 06h00 & 07h20": "06h45",
    "X": "07h05",
    "P.M.": "18h00",
    "Mid-morning": "10h00",
    "16h30 or 18h00": "17h20",
    "Daytime": "13h00",
    "10h00 / 11h00": "10h30",
    '"After lunch"': "14h00",
    "15h00 or 15h45": "15h22",
    ">17h00": "18h30",
    "12h45 / 13h45": "13h15",
    "14h00 - 15h00": "14h30",
    "09h30 / 15h30": "14h10",
    "08h00 / 09h30": "08h45",
    "10h30 or 13h30": "11h30",
    '"After dark"': "22h00",
    1500: "15h00",
    "Between 11h00 & 12h00": "11h30",
    "After dusk": "22h30",
    "Before 10h30": "09h45",
    '9h00': "09h00",
    'Early morning': "06h45",
    '"Evening"': "19h35",
    "06j00": "06h00",
    " 14h00": "14h00", '-16h30':'16h30'
}


# In[171]:


filtered_df['Time'].replace(fixed_times, inplace = True)
filtered_df['Time'].unique()


# In[172]:


time_mapping = {
    '16h00': '16h00', 
    'nan': '21h00', 
    '13h30': '13h30', 
    '11h30': '11h30', 
    '06h30': '06h30', 
    '20h00': '20h00', 
    '13h00': '13h00', 
    '11h12': '11h12',
    '16h30': '16h30', 
    '15h00': '15h00', 
    '02h00': '02h00', 
    '09h15': '09h15', 
    '05h45': '05h45', 
    '16h32': '16h32', 
    '11h00': '11h00', 
    '08h00': '08h00', 
    '10h30': '10h30', 
    '13h20': '13h20', 
    '14h00': '14h00', 
    '09h00': '09h00', 
    '10h20': '10h20', 
    '15h05': '15h05',
    '17h00': '17h00', 
    '15h45': '15h45', 
    '07h45': '07h45', 
    '10h40': '10h40', 
    '07h50': '07h50', 
    '01h00': '01h00', 
    '10h00': '10h00',
    '19h30': '19h30', 
    '17h50': '17h50', 
    '09h30': '09h30', 
    '15h30': '15h30', 
    '08h45': '08h45', 
    '16h25': '16h25', 
    '13h55': '13h55', 
    '13h50': '13h50', 
    '17h20': '17h20', 
    '13h45': '13h45', 
    '10h10': '10h10', 
    '14h35': '14h35', 
    '23h45': '23h45', 
    '19h15': '19h15',
    '11h20': '11h20', 
    '07h15': '07h15', 
    '07h00': '07h00', 
    '18h00': '18h00', 
    '12h30': '12h30', 
    '14h20': '14h20', 
    '17h30': '17h30', 
    '07h20': '07h20', 
    '14h50': '14h50', 
    '12h00': '12h00', 
    '17h17': '17h17', 
    '11h15': '11h15', 
    '19h00': '19h00',
    '07h53': '07h53', 
    '16h10': '16h10', 
    '11h17': '11h17', 
    '17h45': '17h45', 
    'Early  morning': '06h00', 
    '13h12': '13h12', 
    '07h30': '07h30',
    '11hoo': '11h00', 
    '11h43': '11h43', 
    '10h15': '10h15', 
    '14h09': '14h09', 
    '12h15': '12h15', 
    '19h12': '19h12', 
    '15h20': '15h20',
    '16h40': '16h40', 
    '11h24': '11h24', 
    '12h50': '12h50', 
    '07h31': '07h31', 
    '14h45': '14h45', 
    '19h20': '19h20', 
    '23h00': '23h00', 
    '11h45': '11h45',
    '06h40': '06h40', 
    '`17h00': '17h00', 
    '07h51': '07h51', 
    '11h46': '11h46', 
    '20h30': '20h30', 
    '12h23': '12h23', 
    '07h07': '07h07', 
    '16h39': '16h39', 
    '15h57': '15h57',
    '14h30': '14h30', 
    '16h45': '16h45', 
    '10j30': '10h30', 
    '08h15': '08h15', 
    '08h56': '08h56', 
    '15h40': '15h40', 
    '18h30': '18h30', 
    '07h58': '07h58', 
    '17h40': '17h40', 
    '09h00-10h00': '09h00',
    '17h10': '17h10', 
    '09h36': '09h36', 
    '08h40': '08h40', 
    '06h00': '06h00', 
    '10h45': '10h45', 
    1415: '14h15', 
    '14h00-15h00': '14h00',
    '14h15': '14h15', 
    '09h08': '09h08', 
    '15h59': '15h59', 
    '08h30': '08h30', 
    '12h20': '12h20', 
    '10h50': '10h50', 
    '09h40': '09h40',
    '14h33': '14h33', 
    '12h58': '12h58', 
    '19h35': '19h35', 
    '16h15': '16h15', 
    '06h50': '06h50', 
    '12h45': '12h45', 
    '11h55': '11h55', 
    '22h20': '22h20',
    '08h48': '08h48', 
    '16h21': '16h21', 
    '16h26': '16h26', 
    '18h45': '18h45', 
    '03h00': '03h00', 
    '13h40': '13h40', 
    '06h15': '06h15', 
    '06h45': '06h45', 
    '06h55': '06h55',
    '13h42': '13h42', 
    '13h15': '13h15', 
    '09h29': '09h29', 
    '10h47': '10h47', 
    '14h11': '14h11', 
    '15h35': '15h35', 
    '14h40': '14h40', 
    '14h00  -15h00': '14h00', 
    '16h50': '16h50', 
    '21h50': '21h50',
    '17h35': '17h35', 
    '15h01': '15h01', 
    '23h30': '23h30', 
    '10h44': '10h44', 
    '13h19': '13h19', 
    '17h34': '17h34', 
    '09h50': '09h50',
    '10h43': '10h43', 
    '15h15': '15h15', 
    '19h05': '19h05', 
    1300: '13h00', 
    '14h30 / 15h30': '14h30', 
    '22h00': '22h00', 
    '16h20': '16h20',
    '14h34': '14h34', 
    '15h25': '15h25', 
    '14h55': '14h55', 
    '17h46': '17h46', 
    '15h49': '15h49', 
    'Midnight': '00h00', 
    '09h30 / 10h00': '09h30', 
    '18h15': '18h15', 
    '04h00': '04h00',
    '10h25': '10h25', 
    '10h45-11h15': '10h45', 
    '15h52': '15h52', 
    '12h10': '12h10', 
    '18h05': '18h05', 
    '11h41': '11h41', 
    '12h25': '12h25', 
    '17h51': '17h51', 
    '16h12': '16h12',
    '09h45': '09h45', 
    '05h00': '05h00', 
    '03h30': '03h30', 
    'Sometime between 06h00 & 08hoo': '06h00', 
    '11h10': '11h10',
    '07h00 - 08h00': '07h00', 
    '18h23': '18h23', 
    '17h01': '17h01', 
    '09h57': '09h57', 
    '08h20': '08h20', 
    '17h58': '17h58',
    '15h19': '15h19', 
    '10h55': '10h55', 
    '15h55': '15h55', 
    '12h40': '12h40', 
    '16h05': '16h05', 
    '14h10': '14h10', 
    '13h24': '13h24', 
    '11h40': '11h40', 
    '08h10': '08h10',
    '15h56': '15h56', 
    'Just before noon': '11h50', 
    '07h56': '07h56', 
    '16h35': '16h35', 
    '09h05': '09h05', 
    '19h45': '19h45', 
    '19h28': '19h28', 
    '12h38': '12h38', 
    '05h50': '05h50',
    '15h50': '15h50', 
    '11h05': '11h05', 
    'Dawn': '05h00', 
    '13h25': '13h25', 
    '13h26': '13h26', 
    '09h11': '09h11', 
    '18h20': '18h20', 
    'AM': '01h00', 
    '13h51': '13h51', 
    '08h50': '08h50',
    '08h05': '08h05', 
    '10h35': '10h35', 
    '15h44': '15h44', 
    'Lunchtime': '12h00', 
    '09h35': '09h35', 
    '10h27': '10h27', 
    '10h16': '10h16',
    '0500': '05h00', 
    '09h20': '09h20', 
    '10h00 -- 11h00': '10h00', 
    '12h05': '12h05', 
    '14h21': '14h21', 
    '18h50': '18h50', 
    '15h53': '15h53', 
    '20h15': '20h15',
    '12h39': '12h39', 
    '07h05': '07h05', 
    '  ': '21h00', 
    '13h05': '13h05', 
    'N': '21h00', 
    '11h50': '11h50', 
    '17h55': '17h55', 
    '22h30': '22h30', 
    '17h15': '17h15', 
    '11h30 ': '11h30',
    '06h10': '06h10', 
    'Between 05h00 and 08h00': '06h00', 
    '07h08': '07h08', 
    '12h02': '12h02', 
    '12h55': '12h55', 
    '16h14': '16h14',
    '17h11': '17h11', 
    '14h37': '14h37', 
    '10h07': '10h07', 
    '13h53': '13h53', 
    '13h23': '13h23', 
    '02h30': '02h30', 
    '11h56': '11h56',
    '00h45': '00h45', 
    '14h25': '14h25', 
    '13h345': '13h45', 
    '06h47': '06h47', 
    '20h45': '20h45', 
    '18h40': '18h40', 
    '13h14': '13h14',
    '13h06': '13h06', 
    '12h34': '12h34', 
    '11h53': '11h53', 
    '20h04': '20h04', 
    '12h46': '12h46', 
    '12h48': '12h48', 
    '17h42': '17h42', 
    '12h35': '12h35',
    'Possibly same incident as 2000.08.21': '12h35', 
    'After Dusk': '18h00', 
    '11h57': '11h57', 
    'Noon': '12h00', 
    '11h25': '11h25', 
    '18h25': '18h25', 
    '10h28': '10h28', 
    '14h16': '14h16',
    '09h55': '09h55', 
    'Mid afternoon': '15h00', 
    'Mid morning': '10h00', 
    '11h48': '11h48', 
    '07h19': '07h19', 
    '13h37': '13h37', 
    '11h06': '11h06',
    '00h00': '00h00', 
    '11h58': '11h58', 
    '11h51': '11h51', 
    '18h12': '18h12', 
    '07h10': '07h10', 
    '07h40': '07h40', 
    '12h33': '12h33',
    '30 minutes after 1992.07.08.a': '08h30', 
    '15h06': '15h06', 
    '12h54': '12h54', 
    '16h55': '16h55', 
    '05h40': '05h40', 
    '<07h30': '07h00', 
    '21h30': '21h30', 
    '17h00 Sunset': '17h00',
    'Nightfall': '18h00', 
    '08h57': '08h57', 
    '18h30 (Sunset)': '18h30', 
    '08h35': '08h35', 
    '10h22': '10h22', 
    'Prior to 10h37': '10h00', 
    'Daybreak': '06h00',
    '18h10': '18h10', 
    '>12h00': '12h00', 
    '08h55': '08h55', 
    'Just before dawn': '05h00', 
    'Dark': '18h00', 
    '15h22': '15h22', 
    '19h00 / 20h00': '19h00',
    '21h00': '21h00', 
    'night': '21h00', 
    '03h45 - 04h00': '03h45', 
    '13h35': '13h35', 
    'Late night': '00h00', 
    '16h23': '16h23', 
    '15h00j': '15h00', 
    'Midday.': '12h00',
    '10h00 or 14h00': '10h00', 
    '19h10': '19h10', 
    '2 hrs before sunset': '16h00', 
    '18h15 to 21h30': '21h30',
    '"shortly before dusk"': '18h00', 
    '>17h30': '17h30', 
    '>14h30': '14h30', 
    'After 04h00': '04h00',
    '11h01 -time of ship sinking': '11h01', 
    'Ship aban-doned at 03h10': '03h10', 
    '19h55': '19h55',
    'FATAL  (Wire netting installed at local beaches after this incident.)': '03h10',
    '01h30': '01h30', 
    'After midnight': '00h00', 
    'Late afternon': '18h00', 
    '05h30': '05h30', 
    '08h58': '08h58',
    '"Early evening"': '18h00', 
    'Late Afternoon': '18h00', 
    'Before daybreak': '06h00',
    '06h00 -- 07h00': '06h00', 
    '01h50': '01h50', 
    '17h00-18h00': '17h00', 
    '19h00-20h00': '19h00'
}


# In[173]:


filtered_df['Time'].replace(time_mapping, inplace = True)
filtered_df['Time'].unique()


# In[174]:


filtered_df['Time'] = pd.to_datetime(filtered_df['Time'], format='%Hh%M')
filtered_df['Time'] = filtered_df['Time'].dt.time
filtered_df['Time'].isna().sum()


# In[175]:


filtered_df['Date'] = filtered_df['Date'].astype(str)
filtered_df['Date'] = [i.replace('-', ' ').replace('  ', ' ') for i in filtered_df['Date']]
pd.to_datetime(filtered_df['Date'], errors='coerce', format='%d %b %Y')
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], errors='coerce', format='%d %b %Y')
filtered_df['Date']
filtered_df['Date'].fillna(filtered_df['Date'].mean(), inplace = True)
filtered_df['Date'] = filtered_df['Date'].dt.date


# In[176]:


filtered_df['Date'].unique()


# In[177]:


from datetime import datetime

def standardize_date(date_str):
    # Try parsing the date with the format 'dd.mm.yyyy'
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        return date_obj.strftime('%d-%m-%Y')  # Or any other desired format
    except ValueError:
        pass  # Continue to the next format

    # Try parsing the date with the format 'dd Mon yyyy'
    try:
        date_obj = datetime.strptime(date_str, '%d %b %Y')
        return date_obj.strftime('%d-%m-%Y')  # Or any other desired format
    except ValueError:
        pass  # Continue to the next format

    # If none of the formats match, return None or handle it according to your needs
    return None

# Example usage:
date_str = '12.03.2024'
standardized_date = standardize_date(date_str)
print(standardized_date)  # Output: 12-03-2024


# In[178]:


sharks_cleaned[‘Month’] = pd.to_datetime(sharks_cleaned[‘Date’]).dt.month


# In[179]:


filtered_df['Date'].isna().sum()


# In[180]:


filtered_df


# In[181]:


filtered_df['Location'].value_counts().head()


# In[182]:


filtered_df['State'].value_counts().head()


# In[ ]:




