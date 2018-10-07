import pandas as pd

#data = pd.read_csv("C:\\Users\\Amirulamin\\Dropbox\\SIT\Year1\\Tri1\\1002ProgrammingFundamentals\\Project1\\ProjectDatasets\\listing-of-registered-contractors\\listing-of-registered-contractors.csv", dtype=str)# Read the file

class GaryOpen:
    def __init__(self, data):
        self.df = pd.DataFrame.from_records(data, columns=['company_name', 'street_name', 'postal_code'])#read company_name, street_name and postal_code from the csv file and put it in a dataframe
        self.df = self.df.drop_duplicates(subset="company_name")
        
        self.df.loc[self.df.postal_code.astype(str).str.startswith('01'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('02'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('03'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('04'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('05'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('06'), 'General_Location'] = 'Raffles Place, Cecil, Marina, Peoples Park'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('07'), 'General_Location'] = 'Anson, Tanjong Pagar'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('08'), 'General_Location'] = 'Anson, Tanjong Pagar'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('14'), 'General_Location'] = 'Queenstown, Tiong Bahru'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('15'), 'General_Location'] = 'Queenstown, Tiong Bahru'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('16'), 'General_Location'] = 'Queenstown, Tiong Bahru'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('09'), 'General_Location'] = 'Telok Blangah, Harbourfront'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('10'), 'General_Location'] = 'Telok Blangah, Harbourfront'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('11'), 'General_Location'] = 'Pasir Panjang, Hong Leong Garden, Clementi New Town'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('12'), 'General_Location'] = 'Pasir Panjang, Hong Leong Garden, Clementi New Town'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('13'), 'General_Location'] = 'Pasir Panjang, Hong Leong Garden, Clementi New Town'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('17'), 'General_Location'] = 'High Street, Beach Road'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('18'), 'General_Location'] = 'Middle Road, Golden Mile'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('19'), 'General_Location'] = 'Middle Road, Golden Mile'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('20'), 'General_Location'] = 'Little India'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('21'), 'General_Location'] = 'Little India'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('22'), 'General_Location'] = 'Orchard, Cairnhill, River Valley'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('23'), 'General_Location'] = 'Orchard, Cairnhill, River Valley'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('24'), 'General_Location'] = 'Ardmore, Bukit Timah, Holland Road, Tanglin'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('25'), 'General_Location'] = 'Ardmore, Bukit Timah, Holland Road, Tanglin'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('26'), 'General_Location'] = 'Ardmore, Bukit Timah, Holland Road, Tanglin'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('27'), 'General_Location'] = 'Ardmore, Bukit Timah, Holland Road, Tanglin'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('28'), 'General_Location'] = 'Watten Estate, Novena, Thomson'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('29'), 'General_Location'] = 'Watten Estate, Novena, Thomson'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('30'), 'General_Location'] = 'Watten Estate, Novena, Thomson'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('31'), 'General_Location'] = 'Balestier, Toa Payoh, Serangoon'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('32'), 'General_Location'] = 'Balestier, Toa Payoh, Serangoon'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('33'), 'General_Location'] = 'Balestier, Toa Payoh, Serangoon'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('34'), 'General_Location'] = 'Macpherson, Braddell'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('35'), 'General_Location'] = 'Macpherson, Braddell'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('36'), 'General_Location'] = 'Macpherson, Braddell'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('37'), 'General_Location'] = 'Macpherson, Braddell'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('38'), 'General_Location'] = 'Geylang, Eunos'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('39'), 'General_Location'] = 'Geylang, Eunos'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('40'), 'General_Location'] = 'Geylang, Eunos'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('41'), 'General_Location'] = 'Geylang, Eunos'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('42'), 'General_Location'] = 'Katong, Joo Chiat, Amber Road'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('43'), 'General_Location'] = 'Katong, Joo Chiat, Amber Road'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('44'), 'General_Location'] = 'Katong, Joo Chiat, Amber Road'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('45'), 'General_Location'] = 'Katong, Joo Chiat, Amber Road'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('46'), 'General_Location'] = 'Bedok, Upper East Coast, Eastwood, Kew Drive'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('47'), 'General_Location'] = 'Bedok, Upper East Coast, Eastwood, Kew Drive'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('48'), 'General_Location'] = 'Bedok, Upper East Coast, Eastwood, Kew Drive'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('49'), 'General_Location'] = 'Loyang, Changi'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('50'), 'General_Location'] = 'Loyang, Changi'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('81'), 'General_Location'] = 'Loyang, Changi'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('51'), 'General_Location'] = 'Tampines, Pasir Ris'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('52'), 'General_Location'] = 'Tampines, Pasir Ris'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('53'), 'General_Location'] = 'Serangoon Garden, Hougang, Ponggol'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('54'), 'General_Location'] = 'Serangoon Garden, Hougang, Ponggol'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('55'), 'General_Location'] = 'Serangoon Garden, Hougang, Ponggol'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('82'), 'General_Location'] = 'Serangoon Garden, Hougang, Ponggol'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('56'), 'General_Location'] = 'Bishan, Ang Mo Kio'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('57'), 'General_Location'] = 'Bishan, Ang Mo Kio'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('58'), 'General_Location'] = 'Upper Bukit Timah, Clementi Park, Ulu Pandan'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('59'), 'General_Location'] = 'Upper Bukit Timah, Clementi Park, Ulu Pandan'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('60'), 'General_Location'] = 'Jurong'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('61'), 'General_Location'] = 'Jurong'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('62'), 'General_Location'] = 'Jurong'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('63'), 'General_Location'] = 'Jurong'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('64'), 'General_Location'] = 'Jurong'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('65'), 'General_Location'] = 'Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('66'), 'General_Location'] = 'Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('67'), 'General_Location'] = 'Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('68'), 'General_Location'] = 'Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('69'), 'General_Location'] = 'Lim Chu Kang, Tengah'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('70'), 'General_Location'] = 'Lim Chu Kang, Tengah'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('71'), 'General_Location'] = 'Lim Chu Kang, Tengah'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('72'), 'General_Location'] = 'Kranji, Woodgrove'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('73'), 'General_Location'] = 'Kranji, Woodgrove'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('77'), 'General_Location'] = 'Upper Thomson, Springleaf'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('78'), 'General_Location'] = 'Upper Thomson, Springleaf'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('75'), 'General_Location'] = 'Yishun, Sembawang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('76'), 'General_Location'] = 'Yishun, Sembawang'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('79'), 'General_Location'] = 'Seletar'
        self.df.loc[self.df.postal_code.astype(str).str.startswith('80'), 'General_Location'] = 'Seletar'
        self.df.sort_values("postal_code", inplace=True) #sorting the companies based on their postal code
        self.df2 = pd.DataFrame.from_records(self.df, columns=['company_name', 'General_Location']) #using a new dataframe from the created dataframe above
        
        
    def Gopenfunc (self, input): #First 2 digits of postal code is used to determine their general location
        #input = raw_input("Please State the General Location of the Contractors") #produces the result based on which general location the user has inputted
        if input.lower() == "seletar":
            result = self.df2.loc[self.df2.General_Location.str.contains('Seletar')].reset_index(drop=True)
            return result
        elif input.lower() == "jurong":
            result = self.df2.loc[self.df2.General_Location.str.contains('Jurong')].reset_index(drop=True)
            return result
        elif input.lower() == "yishun" or input.lower() == "sembawang":
            result = self.df2.loc[self.df2.General_Location.str.contains('Yishun, Sembawang')].reset_index(drop=True)
            return result
    
        elif input.lower() == "upper thomson" or input.lower() == "springleaf":
            result = self.df2.loc[self.df2.General_Location.str.contains('Upper Thomson, Springleaf')].reset_index(drop=True)
            return result
        elif input.lower() == "kranji" or input.lower() == "woodgrove":
            result = self.df2.loc[self.df2.General_Location.str.contains('Kranji, Woodgrove')].reset_index(drop=True)
            return result
        elif input.lower() == "lim chu kang" or input.lower() == "tengah":
            result = self.df2.loc[self.df2.General_Location.str.contains('Lim Chu Kang, Tengah')].reset_index(drop=True)
            return result
        elif input.lower() == "hillview" or input.lower() == "bukit panjang" or input.lower() == "choa chu kang":
            result = self.df2.loc[self.df2.General_Location.str.contains('Hillview, Dairy Farm, Bukit Panjang, Choa Chu Kang')].reset_index(drop=True)
            return result
        elif input.lower() == "upper bukit timah" or input.lower() == "clementi park" or input.lower() == "ulu pandan":
            result = self.df2.loc[self.df2.General_Location.str.contains('Upper Bukit Timah, Clementi Park, Ulu Pandan')].reset_index(drop=True)
            return result
        elif input.lower() == "bishan" or input.lower() == "ang mo kio":
            result = self.df2.loc[self.df2.General_Location.str.contains('Bishan, Ang Mo Kio')].reset_index(drop=True)
            return result
        elif input.lower() == "serangoon garden" or input.lower() == "ponggol" or input.lower() == "hougang":
            result = self.df2.loc[self.df2.General_Location.str.contains('Serangoon Garden, Hougang, Ponggol')].reset_index(drop=True)
            return result
        elif input.lower() == "pasir ris" or input.lower() == "tampines":
            result = self.df2.loc[self.df2.General_Location.str.contains('Tampines, Pasir Ris')].reset_index(drop=True)
            return result
        elif input.lower() == "loyang" or input.lower() == "changi":
            result = self.df2.loc[self.df2.General_Location.str.contains('Loyang, Changi')].reset_index(drop=True)
            return result
        elif input.lower() == "eastwood" or input.lower() == "kew drive" or input.lower() == "bedok" or input.lower() == "upper east coast":
            result = self.df2.loc[self.df2.General_Location.str.contains('Bedok, Upper East Coast, Eastwood, Kew Drive')].reset_index(drop=True)
            return result
        elif input.lower() == "joo chiat" or input.lower() == "katong" or input.lower() == "amber road":
            result = self.df2.loc[self.df2.General_Location.str.contains('Katong, Joo Chiat, Amber Road')].reset_index(drop=True)
            return result
        elif input.lower() == "geylang" or input.lower() == "eunos":
            result = self.df2.loc[self.df2.General_Location.str.contains('Geylang, Eunos')].reset_index(drop=True)
            return result
        elif input.lower() == "macpherson" or input.lower() == "braddell":
            result = self.df2.loc[self.df2.General_Location.str.contains('Macpherson, Braddell')].reset_index(drop=True)
            return result
        elif input.lower() == "balestier" or input.lower() == "toa payoh" or input.lower() == "serangoon":
            result = self.df2.loc[self.df2.General_Location.str.contains('Balestier, Toa Payoh, Serangoon')].reset_index(drop=True)
            return result
        elif input.lower() == "watten estate" or input.lower() == "novena" or input.lower() == "thomson":
            result = self.df2.loc[self.df2.General_Location.str.contains('Watten Estate, Novena, Thomson')].reset_index(drop=True)
            return result
        elif input.lower() == "ardmore" or input.lower() == "bukit timah" or input.lower() == "holland road" or input.lower() == "tanglin":
            result = self.df2.loc[self.df2.General_Location.str.contains('Ardmore, Bukit Timah, Holland Road, Tanglin')].reset_index(drop=True)
            return result
        elif input.lower() == "orchard" or input.lower() == "cairnhill" or input.lower() == "river valley":
            result = self.df2.loc[self.df2.General_Location.str.contains('Orchard, Cairnhill, River Valley')].reset_index(drop=True)
            return result
        elif input.lower() == "little india":
            result = self.df2.loc[self.df2.General_Location.str.contains('Little India')].reset_index(drop=True)
            return result
        elif input.lower() == "middle road" or input.lower() == "golden mile":
            result = self.df2.loc[self.df2.General_Location.str.contains('Middle Road, Golden Mile')].reset_index(drop=True)
            return result
        elif input.lower() == "high street" or input.lower() == "beach road":
            result = self.df2.loc[self.df2.General_Location.str.contains('High Street, Beach Road')].reset_index(drop=True)
            return result
        elif input.lower() == "pasir panjang" or input.lower() == "hong leong garden" or input.lower() == "clementi new town":
            result = self.df2.loc[self.df2.General_Location.str.contains('Pasir Panjang, Hong Leong Garden, Clementi New Town')].reset_index(drop=True)
            return result
        elif input.lower() == "harbourfront" or input.lower() == "telok blangah":
            result = self.df2.loc[self.df2.General_Location.str.contains('Telok Blangah, Harbourfront')].reset_index(drop=True)
            return result
        elif input.lower() == "queenstown" or input.lower() == "tiong bahru":
            result = self.df2.loc[self.df2.General_Location.str.contains('Queenstown, Tiong Bahru')].reset_index(drop=True)
            return result
        elif input.lower() == "anson" or input.lower() == "tanjong pagar":
            result = self.df2.loc[self.df2.General_Location.str.contains('Anson, Tanjong Pagar')].reset_index(drop=True)
            return result
        elif input.lower() == "raffles place" or input.lower() == "cecil" or input.lower() == "peoples park":
            result = self.df2.loc[self.df2.General_Location.str.contains('Raffles Place, Cecil, Marina, Peoples Park')].reset_index(drop=True)
            return result
        else:
            return "Please enter a valid General Location!" #if user inputs anything apart from the general location. will prompt the user to input a valid general location

#print GaryOpen().Gopenfunc("Amber Road")








