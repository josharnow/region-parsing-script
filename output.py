
AF_STATES = [State(abbr, name) for abbr, name in 
    (('BDS', 'Badakhshān'), ('BGL', 'Baghlān'), ('BAL', 'Balkh'), ('BDG', 'Bādghīs'), ('BAM', 'Bāmyān'), ('DAY', 'Dāykundī'), ('FRA', 'Farāh'), ('FYB', 'Fāryāb'), ('GHA', 'Ghaznī'), ('GHO', 'Ghōr'), ('HEL', 'Helmand'), ('HER', 'Herāt'), ('JOW', 'Jowzjān'), ('KAN', 'Kandahār'), ('KHO', 'Khōst'), ('KNR', 'Kunar'), ('KDZ', 'Kunduz'), ('KAB', 'Kābul'), ('KAP', 'Kāpīsā'), ('LAG', 'Laghmān'), ('LOG', 'Lōgar'), ('NAN', 'Nangarhār'), ('NIM', 'Nīmrōz'), ('NUR', 'Nūristān'), ('PIA', 'Paktiyā'), ('PKA', 'Paktīkā'), ('PAN', 'Panjshayr'), ('PAR', 'Parwān'), ('SAM', 'Samangān'), ('SAR', 'Sar-e Pul'), ('TAK', 'Takhār'), ('URU', 'Uruzgān'), ('WAR', 'Wardak'), ('ZAB', 'Zābul'))
]
AF_STATES_DICT = CapsDict({state.abbr: state.name for state in AF_STATES})
AF_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AF_STATES}

AL_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Berat'), ('09', 'Dibër'), ('02', 'Durrës'), ('03', 'Elbasan'), ('04', 'Fier'), ('05', 'Gjirokastër'), ('06', 'Korçë'), ('07', 'Kukës'), ('08', 'Lezhë'), ('10', 'Shkodër'), ('11', 'Tiranë'), ('12', 'Vlorë'))
]
AL_STATES_DICT = CapsDict({state.abbr: state.name for state in AL_STATES})
AL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AL_STATES}

DZ_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Adrar'), ('16', 'Alger'), ('23', 'Annaba'), ('44', 'Aïn Defla'), ('46', 'Aïn Témouchent'), ('05', 'Batna'), ('07', 'Biskra'), ('09', 'Blida'), ('34', 'Bordj Bou Arréridj'), ('10', 'Bouira'), ('35', 'Boumerdès'), ('08', 'Béchar'), ('06', 'Béjaïa'), ('02', 'Chlef'), ('25', 'Constantine'), ('17', 'Djelfa'), ('32', 'El Bayadh'), ('39', 'El Oued'), ('36', 'El Tarf'), ('47', 'Ghardaïa'), ('24', 'Guelma'), ('33', 'Illizi'), ('18', 'Jijel'), ('40', 'Khenchela'), ('03', 'Laghouat'), ('29', 'Mascara'), ('43', 'Mila'), ('27', 'Mostaganem'), ('28', 'Msila'), ('26', 'Médéa'), ('45', 'Naama'), ('31', 'Oran'), ('30', 'Ouargla'), ('04', 'Oum el Bouaghi'), ('48', 'Relizane'), ('20', 'Saïda'), ('22', 'Sidi Bel Abbès'), ('21', 'Skikda'), ('41', 'Souk Ahras'), ('19', 'Sétif'), ('11', 'Tamanghasset'), ('14', 'Tiaret'), ('37', 'Tindouf'), ('42', 'Tipaza'), ('38', 'Tissemsilt'), ('15', 'Tizi Ouzou'), ('13', 'Tlemcen'), ('12', 'Tébessa'))
]
DZ_STATES_DICT = CapsDict({state.abbr: state.name for state in DZ_STATES})
DZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DZ_STATES}

AD_STATES = [State(abbr, name) for abbr, name in 
    (('07', 'Andorra la Vella'), ('02', 'Canillo'), ('03', 'Encamp'), ('08', 'Escaldes-Engordany'), ('04', 'La Massana'), ('05', 'Ordino'), ('06', 'Sant Julià de Lòria'))
]
AD_STATES_DICT = CapsDict({state.abbr: state.name for state in AD_STATES})
AD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AD_STATES}

AO_STATES = [State(abbr, name) for abbr, name in 
    (('BGO', 'Bengo'), ('BGU', 'Benguela'), ('BIE', 'Bié'), ('CAB', 'Cabinda'), ('CNN', 'Cunene'), ('HUA', 'Huambo'), ('HUI', 'Huíla'), ('CCU', 'Kuando Kubango'), ('CNO', 'Kwanza Norte'), ('CUS', 'Kwanza Sul'), ('LUA', 'Luanda'), ('LNO', 'Lunda Norte'), ('LSU', 'Lunda Sul'), ('MAL', 'Malange'), ('MOX', 'Moxico'), ('NAM', 'Namibe'), ('UIG', 'Uíge'), ('ZAI', 'Zaire'))
]
AO_STATES_DICT = CapsDict({state.abbr: state.name for state in AO_STATES})
AO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AO_STATES}

AG_STATES = [State(abbr, name) for abbr, name in 
    (('10', 'Barbuda'), ('11', 'Redonda'), ('03', 'Saint George'), ('04', 'Saint John'), ('05', 'Saint Mary'), ('06', 'Saint Paul'), ('07', 'Saint Peter'), ('08', 'Saint Philip'))
]
AG_STATES_DICT = CapsDict({state.abbr: state.name for state in AG_STATES})
AG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AG_STATES}

AR_STATES = [State(abbr, name) for abbr, name in 
    (('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Autónoma de Buenos Aires'), ('W', 'Corrientes'), ('X', 'Córdoba'), ('E', 'Entre Ríos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuquén'), ('R', 'Río Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego'), ('T', 'Tucumán'))
]
AR_STATES_DICT = CapsDict({state.abbr: state.name for state in AR_STATES})
AR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AR_STATES}

AM_STATES = [State(abbr, name) for abbr, name in 
    (('AG', 'Aragac̣otn'), ('AR', 'Ararat'), ('AV', 'Armavir'), ('ER', 'Erevan'), ('GR', "Geġark'unik'"), ('KT', "Kotayk'"), ('LO', 'Loṙi'), ('SU', "Syunik'"), ('TV', 'Tavuš'), ('VD', 'Vayoć Jor'), ('SH', 'Širak'))
]
AM_STATES_DICT = CapsDict({state.abbr: state.name for state in AM_STATES})
AM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AM_STATES}

AU_STATES = [State(abbr, name) for abbr, name in 
    (('ACT', 'Australian Capital Territory'), ('NSW', 'New South Wales'), ('NT', 'Northern Territory'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia'))
]
AU_STATES_DICT = CapsDict({state.abbr: state.name for state in AU_STATES})
AU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AU_STATES}

AT_STATES = [State(abbr, name) for abbr, name in 
    (('1', 'Burgenland'), ('2', 'Kärnten'), ('3', 'Niederösterreich'), ('4', 'Oberösterreich'), ('5', 'Salzburg'), ('6', 'Steiermark'), ('7', 'Tirol'), ('8', 'Vorarlberg'), ('9', 'Wien'))
]
AT_STATES_DICT = CapsDict({state.abbr: state.name for state in AT_STATES})
AT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AT_STATES}

AZ_STATES = [State(abbr, name) for abbr, name in 
    (('NX', 'Naxçıvan'),)
]
AZ_STATES_DICT = CapsDict({state.abbr: state.name for state in AZ_STATES})
AZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AZ_STATES}

BS_STATES = [State(abbr, name) for abbr, name in 
    (('AK', 'Acklins'), ('BY', 'Berry Islands'), ('BI', 'Bimini'), ('BP', 'Black Point'), ('CI', 'Cat Island'), ('CO', 'Central Abaco'), ('CS', 'Central Andros'), ('CE', 'Central Eleuthera'), ('FP', 'City of Freeport'), ('CK', 'Crooked Island and Long Cay'), ('EG', 'East Grand Bahama'), ('EX', 'Exuma'), ('GC', 'Grand Cay'), ('HI', 'Harbour Island'), ('HT', 'Hope Town'), ('IN', 'Inagua'), ('LI', 'Long Island'), ('MC', 'Mangrove Cay'), ('MG', 'Mayaguana'), ('MI', 'Moores Island'), ('NO', 'North Abaco'), ('NS', 'North Andros'), ('NE', 'North Eleuthera'), ('RI', 'Ragged Island'), ('RC', 'Rum Cay'), ('SS', 'San Salvador'), ('SO', 'South Abaco'), ('SA', 'South Andros'), ('SE', 'South Eleuthera'), ('SW', 'Spanish Wells'), ('WG', 'West Grand Bahama'))
]
BS_STATES_DICT = CapsDict({state.abbr: state.name for state in BS_STATES})
BS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BS_STATES}

BH_STATES = [State(abbr, name) for abbr, name in 
    (('14', 'Al Janūbīyah'), ('13', 'Al Manāmah'), ('15', 'Al Muḩarraq'), ('16', 'Al Wusţá'), ('17', 'Ash Shamālīyah'))
]
BH_STATES_DICT = CapsDict({state.abbr: state.name for state in BH_STATES})
BH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BH_STATES}

BD_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Barisal'), ('B', 'Chittagong'), ('C', 'Dhaka'), ('D', 'Khulna'), ('E', 'Rajshahi'), ('F', 'Rangpur'), ('G', 'Sylhet'))
]
BD_STATES_DICT = CapsDict({state.abbr: state.name for state in BD_STATES})
BD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BD_STATES}

BB_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Christ Church'), ('02', 'Saint Andrew'), ('03', 'Saint George'), ('04', 'Saint James'), ('05', 'Saint John'), ('06', 'Saint Joseph'), ('07', 'Saint Lucy'), ('08', 'Saint Michael'), ('09', 'Saint Peter'), ('10', 'Saint Philip'), ('11', 'Saint Thomas'))
]
BB_STATES_DICT = CapsDict({state.abbr: state.name for state in BB_STATES})
BB_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BB_STATES}

BY_STATES = [State(abbr, name) for abbr, name in 
    (('BR', "Brestskaya voblasts'"), ('HO', "Homyel'skaya voblasts'"), ('HM', 'Horad Minsk'), ('HR', "Hrodzenskaya voblasts'"), ('MA', "Mahilyowskaya voblasts'"), ('MI', "Minskaya voblasts'"), ('VI', "Vitsyebskaya voblasts'"))
]
BY_STATES_DICT = CapsDict({state.abbr: state.name for state in BY_STATES})
BY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BY_STATES}

BE_STATES = [State(abbr, name) for abbr, name in 
    (('BRU', 'Brussels Hoofdstedelijk Gewest'), ('WAL', 'Région Wallonne'), ('VLG', 'Vlaams Gewest'))
]
BE_STATES_DICT = CapsDict({state.abbr: state.name for state in BE_STATES})
BE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BE_STATES}

BZ_STATES = [State(abbr, name) for abbr, name in 
    (('BZ', 'Belize'), ('CY', 'Cayo'), ('CZL', 'Corozal'), ('OW', 'Orange Walk'), ('SC', 'Stann Creek'), ('TOL', 'Toledo'))
]
BZ_STATES_DICT = CapsDict({state.abbr: state.name for state in BZ_STATES})
BZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BZ_STATES}

BJ_STATES = [State(abbr, name) for abbr, name in 
    (('AL', 'Alibori'), ('AK', 'Atakora'), ('AQ', 'Atlantique'), ('BO', 'Borgou'), ('CO', 'Collines'), ('DO', 'Donga'), ('KO', 'Kouffo'), ('LI', 'Littoral'), ('MO', 'Mono'), ('OU', 'Ouémé'), ('PL', 'Plateau'), ('ZO', 'Zou'))
]
BJ_STATES_DICT = CapsDict({state.abbr: state.name for state in BJ_STATES})
BJ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BJ_STATES}

BT_STATES = [State(abbr, name) for abbr, name in 
    (('33', 'Bumthang'), ('12', 'Chhukha'), ('22', 'Dagana'), ('GA', 'Gasa'), ('13', 'Ha'), ('44', 'Lhuentse'), ('42', 'Monggar'), ('11', 'Paro'), ('43', 'Pemagatshel'), ('23', 'Punakha'), ('45', 'Samdrup Jongkha'), ('14', 'Samtse'), ('31', 'Sarpang'), ('15', 'Thimphu'), ('TY', 'Trashi Yangtse'), ('41', 'Trashigang'), ('32', 'Trongsa'), ('21', 'Tsirang'), ('24', 'Wangdue Phodrang'), ('34', 'Zhemgang'))
]
BT_STATES_DICT = CapsDict({state.abbr: state.name for state in BT_STATES})
BT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BT_STATES}

BO_STATES = [State(abbr, name) for abbr, name in 
    (('H', 'Chuquisaca'), ('C', 'Cochabamba'), ('B', 'El Beni'), ('L', 'La Paz'), ('O', 'Oruro'), ('N', 'Pando'), ('P', 'Potosí'), ('S', 'Santa Cruz'), ('T', 'Tarija'))
]
BO_STATES_DICT = CapsDict({state.abbr: state.name for state in BO_STATES})
BO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BO_STATES}

BA_STATES = [State(abbr, name) for abbr, name in 
    (('BRC', 'Brčko distrikt'), ('BIH', 'Federacija Bosna i Hercegovina'), ('SRP', 'Republika Srpska'))
]
BA_STATES_DICT = CapsDict({state.abbr: state.name for state in BA_STATES})
BA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BA_STATES}

BW_STATES = [State(abbr, name) for abbr, name in 
    (('CE', 'Central'), ('CH', 'Chobe'), ('FR', 'Francistown'), ('GA', 'Gaborone'), ('GH', 'Ghanzi'), ('JW', 'Jwaneng'), ('KG', 'Kgalagadi'), ('KL', 'Kgatleng'), ('KW', 'Kweneng'), ('LO', 'Lobatse'), ('NE', 'North-East'), ('NW', 'North-West'), ('SP', 'Selibe Phikwe'), ('SE', 'South-East'), ('SO', 'Southern'), ('ST', 'Sowa Town'))
]
BW_STATES_DICT = CapsDict({state.abbr: state.name for state in BW_STATES})
BW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BW_STATES}

BR_STATES = [State(abbr, name) for abbr, name in 
    (('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RJ', 'Rio de Janeiro'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins'))
]
BR_STATES_DICT = CapsDict({state.abbr: state.name for state in BR_STATES})
BR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BR_STATES}

BN_STATES = [State(abbr, name) for abbr, name in 
    (('BE', 'Belait'), ('BM', 'Brunei-Muara'), ('TE', 'Temburong'), ('TU', 'Tutong'))
]
BN_STATES_DICT = CapsDict({state.abbr: state.name for state in BN_STATES})
BN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BN_STATES}

BG_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Blagoevgrad'), ('02', 'Burgas'), ('08', 'Dobrich'), ('07', 'Gabrovo'), ('26', 'Haskovo'), ('09', 'Kardzhali'), ('10', 'Kyustendil'), ('11', 'Lovech'), ('12', 'Montana'), ('13', 'Pazardzhik'), ('14', 'Pernik'), ('15', 'Pleven'), ('16', 'Plovdiv'), ('17', 'Razgrad'), ('18', 'Ruse'), ('27', 'Shumen'), ('19', 'Silistra'), ('20', 'Sliven'), ('21', 'Smolyan'), ('23', 'Sofia'), ('22', 'Sofia-Grad'), ('24', 'Stara Zagora'), ('25', 'Targovishte'), ('03', 'Varna'), ('04', 'Veliko Tarnovo'), ('05', 'Vidin'), ('06', 'Vratsa'), ('28', 'Yambol'))
]
BG_STATES_DICT = CapsDict({state.abbr: state.name for state in BG_STATES})
BG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BG_STATES}

BF_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Boucle du Mouhoun'), ('02', 'Cascades'), ('03', 'Centre'), ('04', 'Centre-Est'), ('05', 'Centre-Nord'), ('06', 'Centre-Ouest'), ('07', 'Centre-Sud'), ('08', 'Est'), ('09', 'Hauts-Bassins'), ('10', 'Nord'), ('11', 'Plateau-Central'), ('12', 'Sahel'), ('13', 'Sud-Ouest'))
]
BF_STATES_DICT = CapsDict({state.abbr: state.name for state in BF_STATES})
BF_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BF_STATES}

BI_STATES = [State(abbr, name) for abbr, name in 
    (('BB', 'Bubanza'), ('BM', 'Bujumbura Mairie'), ('BL', 'Bujumbura Rural'), ('BR', 'Bururi'), ('CA', 'Cankuzo'), ('CI', 'Cibitoke'), ('GI', 'Gitega'), ('KR', 'Karuzi'), ('KY', 'Kayanza'), ('KI', 'Kirundo'), ('MA', 'Makamba'), ('MU', 'Muramvya'), ('MY', 'Muyinga'), ('MW', 'Mwaro'), ('NG', 'Ngozi'), ('RT', 'Rutana'), ('RY', 'Ruyigi'))
]
BI_STATES_DICT = CapsDict({state.abbr: state.name for state in BI_STATES})
BI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in BI_STATES}

KH_STATES = [State(abbr, name) for abbr, name in 
    (('2', 'Baat Dambang'), ('1', 'Banteay Mean Chey'), ('3', 'Kampong Chaam'), ('4', 'Kampong Chhnang'), ('5', 'Kampong Spueu'), ('6', 'Kampong Thum'), ('7', 'Kampot'), ('8', 'Kandaal'), ('9', 'Kaoh Kong'), ('10', 'Kracheh'), ('23', 'Krong Kaeb'), ('24', 'Krong Pailin'), ('18', 'Krong Preah Sihanouk'), ('11', 'Mondol Kiri'), ('22', 'Otdar Mean Chey'), ('12', 'Phnom Penh'), ('15', 'Pousaat'), ('13', 'Preah Vihear'), ('14', 'Prey Veaeng'), ('16', 'Rotanak Kiri'), ('17', 'Siem Reab'), ('19', 'Stueng Traeng'), ('20', 'Svaay Rieng'), ('21', 'Taakaev'))
]
KH_STATES_DICT = CapsDict({state.abbr: state.name for state in KH_STATES})
KH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KH_STATES}

CM_STATES = [State(abbr, name) for abbr, name in 
    (('AD', 'Adamaoua'), ('CE', 'Centre'), ('ES', 'East'), ('EN', 'Far North'), ('LT', 'Littoral'), ('NO', 'North'), ('NW', 'North-West'), ('SU', 'South'), ('SW', 'South-West'), ('OU', 'West'))
]
CM_STATES_DICT = CapsDict({state.abbr: state.name for state in CM_STATES})
CM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CM_STATES}

CA_STATES = [State(abbr, name) for abbr, name in 
    (('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('YT', 'Yukon'))
]
CA_STATES_DICT = CapsDict({state.abbr: state.name for state in CA_STATES})
CA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CA_STATES}

CV_STATES = [State(abbr, name) for abbr, name in 
    (('B', 'Ilhas de Barlavento'), ('S', 'Ilhas de Sotavento'))
]
CV_STATES_DICT = CapsDict({state.abbr: state.name for state in CV_STATES})
CV_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CV_STATES}

CF_STATES = [State(abbr, name) for abbr, name in 
    (('BB', 'Bamingui-Bangoran'), ('BGF', 'Bangui'), ('BK', 'Basse-Kotto'), ('KB', 'Gribingui'), ('HM', 'Haut-Mbomou'), ('HK', 'Haute-Kotto'), ('HS', 'Haute-Sangha / Mambéré-Kadéï'), ('KG', 'Kémo-Gribingui'), ('LB', 'Lobaye'), ('MB', 'Mbomou'), ('NM', 'Nana-Mambéré'), ('MP', 'Ombella-Mpoko'), ('UK', 'Ouaka'), ('AC', 'Ouham'), ('OP', 'Ouham-Pendé'), ('SE', 'Sangha'), ('VK', 'Vakaga'))
]
CF_STATES_DICT = CapsDict({state.abbr: state.name for state in CF_STATES})
CF_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CF_STATES}

TD_STATES = [State(abbr, name) for abbr, name in 
    (('BA', 'Al Baṭḩah'), ('LC', 'Al Buḩayrah'), ('BG', 'Baḩr al Ghazāl'), ('BO', 'Būrkū'), ('EN', 'Innīdī'), ('KA', 'Kānim'), ('LO', 'Lūqūn al Gharbī'), ('LR', 'Lūqūn ash Sharqī'), ('ND', 'Madīnat Injamīnā'), ('MA', 'Māndūl'), ('MO', 'Māyū Kībbī al Gharbī'), ('ME', 'Māyū Kībbī ash Sharqī'), ('GR', 'Qīrā'), ('SA', 'Salāmāt'), ('CB', 'Shārī Bāqirmī'), ('MC', 'Shārī al Awsaṭ'), ('SI', 'Sīlā'), ('TI', 'Tibastī'), ('TA', 'Tānjilī'), ('OD', 'Waddāy'), ('WF', 'Wādī Fīrā'), ('HL', 'Ḥajjar Lamīs'))
]
TD_STATES_DICT = CapsDict({state.abbr: state.name for state in TD_STATES})
TD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TD_STATES}

CL_STATES = [State(abbr, name) for abbr, name in 
    (('AI', 'Aisén del General Carlos Ibañez del Campo'), ('AN', 'Antofagasta'), ('AR', 'Araucanía'), ('AP', 'Arica y Parinacota'), ('AT', 'Atacama'), ('BI', 'Bío-Bío'), ('CO', 'Coquimbo'), ('LI', "Libertador General Bernardo O'Higgins"), ('LL', 'Los Lagos'), ('LR', 'Los Ríos'), ('MA', 'Magallanes'), ('ML', 'Maule'), ('RM', 'Región Metropolitana de Santiago'), ('TA', 'Tarapacá'), ('VS', 'Valparaíso'))
]
CL_STATES_DICT = CapsDict({state.abbr: state.name for state in CL_STATES})
CL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CL_STATES}

CN_STATES = [State(abbr, name) for abbr, name in 
    (('45', 'Guangxi'), ('15', 'Nei Mongol'), ('64', 'Ningxia'), ('65', 'Xinjiang'), ('54', 'Xizang'), ('11', 'Beijing'), ('50', 'Chongqing'), ('31', 'Shanghai'), ('12', 'Tianjin'), ('34', 'Anhui'), ('35', 'Fujian'), ('62', 'Gansu'), ('44', 'Guangdong'), ('52', 'Guizhou'), ('46', 'Hainan'), ('13', 'Hebei'), ('23', 'Heilongjiang'), ('41', 'Henan'), ('42', 'Hubei'), ('43', 'Hunan'), ('32', 'Jiangsu'), ('36', 'Jiangxi'), ('22', 'Jilin'), ('21', 'Liaoning'), ('63', 'Qinghai'), ('61', 'Shaanxi'), ('37', 'Shandong'), ('14', 'Shanxi'), ('51', 'Sichuan'), ('71', 'Taiwan'), ('53', 'Yunnan'), ('33', 'Zhejiang'), ('91', 'Hong Kong'), ('92', 'Macao'))
]
CN_STATES_DICT = CapsDict({state.abbr: state.name for state in CN_STATES})
CN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CN_STATES}

CO_STATES = [State(abbr, name) for abbr, name in 
    (('AMA', 'Amazonas'), ('ANT', 'Antioquia'), ('ARA', 'Arauca'), ('ATL', 'Atlántico'), ('BOL', 'Bolívar'), ('BOY', 'Boyacá'), ('CAL', 'Caldas'), ('CAQ', 'Caquetá'), ('CAS', 'Casanare'), ('CAU', 'Cauca'), ('CES', 'Cesar'), ('CHO', 'Chocó'), ('CUN', 'Cundinamarca'), ('COR', 'Córdoba'), ('DC', 'Distrito Capital de Bogotá'), ('GUA', 'Guainía'), ('GUV', 'Guaviare'), ('HUI', 'Huila'), ('LAG', 'La Guajira'), ('MAG', 'Magdalena'), ('MET', 'Meta'), ('NAR', 'Nariño'), ('NSA', 'Norte de Santander'), ('PUT', 'Putumayo'), ('QUI', 'Quindío'), ('RIS', 'Risaralda'), ('SAP', 'San Andrés, Providencia y Santa Catalina'), ('SAN', 'Santander'), ('SUC', 'Sucre'), ('TOL', 'Tolima'), ('VAC', 'Valle del Cauca'), ('VAU', 'Vaupés'), ('VID', 'Vichada'))
]
CO_STATES_DICT = CapsDict({state.abbr: state.name for state in CO_STATES})
CO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CO_STATES}

KM_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Anjouan'), ('G', 'Grande Comore'), ('M', 'Mohéli'))
]
KM_STATES_DICT = CapsDict({state.abbr: state.name for state in KM_STATES})
KM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KM_STATES}

CG_STATES = [State(abbr, name) for abbr, name in 
    (('11', 'Bouenza'), ('BZV', 'Brazzaville'), ('8', 'Cuvette'), ('15', 'Cuvette-Ouest'), ('5', 'Kouilou'), ('7', 'Likouala'), ('2', 'Lékoumou'), ('9', 'Niari'), ('14', 'Plateaux'), ('16', 'Pointe-Noire'), ('12', 'Pool'), ('13', 'Sangha'))
]
CG_STATES_DICT = CapsDict({state.abbr: state.name for state in CG_STATES})
CG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CG_STATES}

CD_STATES = [State(abbr, name) for abbr, name in 
    (('BN', 'Bandundu'), ('BC', 'Bas-Congo'), ('KW', 'Kasai-Occidental'), ('KE', 'Kasai-Oriental'), ('KA', 'Katanga'), ('KN', 'Kinshasa'), ('MA', 'Maniema'), ('NK', 'Nord-Kivu'), ('OR', 'Orientale'), ('SK', 'Sud-Kivu'), ('EQ', 'Équateur'))
]
CD_STATES_DICT = CapsDict({state.abbr: state.name for state in CD_STATES})
CD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CD_STATES}

CR_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Alajuela'), ('C', 'Cartago'), ('G', 'Guanacaste'), ('H', 'Heredia'), ('L', 'Limón'), ('P', 'Puntarenas'), ('SJ', 'San José'))
]
CR_STATES_DICT = CapsDict({state.abbr: state.name for state in CR_STATES})
CR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CR_STATES}

CI_STATES = [State(abbr, name) for abbr, name in 
    (('06', '18 Montagnes'), ('16', 'Agnébi'), ('17', 'Bafing'), ('09', 'Bas-Sassandra'), ('10', 'Denguélé'), ('18', 'Fromager'), ('02', 'Haut-Sassandra'), ('07', 'Lacs'), ('01', 'Lagunes'), ('12', 'Marahoué'), ('19', 'Moyen-Cavally'), ('05', 'Moyen-Comoé'), ('11', 'Nzi-Comoé'), ('03', 'Savanes'), ('15', 'Sud-Bandama'), ('13', 'Sud-Comoé'), ('04', 'Vallée du Bandama'), ('14', 'Worodougou'), ('08', 'Zanzan'))
]
CI_STATES_DICT = CapsDict({state.abbr: state.name for state in CI_STATES})
CI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CI_STATES}

HR_STATES = [State(abbr, name) for abbr, name in 
    (('07', 'Bjelovarsko-bilogorska županija'), ('12', 'Brodsko-posavska županija'), ('19', 'Dubrovačko-neretvanska županija'), ('21', 'Grad Zagreb'), ('18', 'Istarska županija'), ('04', 'Karlovačka županija'), ('06', 'Koprivničko-križevačka županija'), ('02', 'Krapinsko-zagorska županija'), ('09', 'Ličko-senjska županija'), ('20', 'Međimurska županija'), ('14', 'Osječko-baranjska županija'), ('11', 'Požeško-slavonska županija'), ('08', 'Primorsko-goranska županija'), ('03', 'Sisačko-moslavačka županija'), ('17', 'Splitsko-dalmatinska županija'), ('05', 'Varaždinska županija'), ('10', 'Virovitičko-podravska županija'), ('16', 'Vukovarsko-srijemska županija'), ('13', 'Zadarska županija'), ('01', 'Zagrebačka županija'), ('15', 'Šibensko-kninska županija'))
]
HR_STATES_DICT = CapsDict({state.abbr: state.name for state in HR_STATES})
HR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in HR_STATES}

CU_STATES = [State(abbr, name) for abbr, name in 
    (('15', 'Artemisa'), ('09', 'Camagüey'), ('08', 'Ciego de Ávila'), ('06', 'Cienfuegos'), ('12', 'Granma'), ('14', 'Guantánamo'), ('11', 'Holguín'), ('99', 'Isla de la Juventud'), ('03', 'La Habana'), ('10', 'Las Tunas'), ('04', 'Matanzas'), ('16', 'Mayabeque'), ('01', 'Pinar del Río'), ('07', 'Sancti Spíritus'), ('13', 'Santiago de Cuba'), ('05', 'Villa Clara'))
]
CU_STATES_DICT = CapsDict({state.abbr: state.name for state in CU_STATES})
CU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CU_STATES}

CY_STATES = [State(abbr, name) for abbr, name in 
    (('04', 'Ammochostos'), ('06', 'Keryneia'), ('03', 'Larnaka'), ('01', 'Lefkosia'), ('02', 'Lemesos'), ('05', 'Pafos'))
]
CY_STATES_DICT = CapsDict({state.abbr: state.name for state in CY_STATES})
CY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CY_STATES}

CZ_STATES = [State(abbr, name) for abbr, name in 
    (('JM', 'Jihomoravský kraj'), ('JC', 'Jihočeský kraj'), ('KA', 'Karlovarský kraj'), ('KR', 'Královéhradecký kraj'), ('LI', 'Liberecký kraj'), ('MO', 'Moravskoslezský kraj'), ('OL', 'Olomoucký kraj'), ('PA', 'Pardubický kraj'), ('PL', 'Plzeňský kraj'), ('PR', 'Praha, hlavní město'), ('ST', 'Středočeský kraj'), ('VY', 'Vysočina'), ('ZL', 'Zlínský kraj'), ('US', 'Ústecký kraj'))
]
CZ_STATES_DICT = CapsDict({state.abbr: state.name for state in CZ_STATES})
CZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CZ_STATES}

DK_STATES = [State(abbr, name) for abbr, name in 
    (('84', 'Hovedstaden'), ('82', 'Midtjylland'), ('81', 'Nordjylland'), ('85', 'Sjælland'), ('83', 'Syddanmark'))
]
DK_STATES_DICT = CapsDict({state.abbr: state.name for state in DK_STATES})
DK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DK_STATES}

DJ_STATES = [State(abbr, name) for abbr, name in 
    (('AS', 'Ali Sabieh'), ('AR', 'Arta'), ('DI', 'Dikhil'), ('DJ', 'Djibouti'), ('OB', 'Obock'), ('TA', 'Tadjourah'))
]
DJ_STATES_DICT = CapsDict({state.abbr: state.name for state in DJ_STATES})
DJ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DJ_STATES}

DM_STATES = [State(abbr, name) for abbr, name in 
    (('02', 'Saint Andrew'), ('03', 'Saint David'), ('04', 'Saint George'), ('05', 'Saint John'), ('06', 'Saint Joseph'), ('07', 'Saint Luke'), ('08', 'Saint Mark'), ('09', 'Saint Patrick'), ('10', 'Saint Paul'), ('11', 'Saint Peter'))
]
DM_STATES_DICT = CapsDict({state.abbr: state.name for state in DM_STATES})
DM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DM_STATES}

DO_STATES = [State(abbr, name) for abbr, name in 
    (('33', 'Cibao Nordeste'), ('34', 'Cibao Noroeste'), ('35', 'Cibao Norte'), ('36', 'Cibao Sur'), ('37', 'El Valle'), ('38', 'Enriquillo'), ('39', 'Higuamo'), ('40', 'Ozama'), ('41', 'Valdesia'), ('42', 'Yuma'))
]
DO_STATES_DICT = CapsDict({state.abbr: state.name for state in DO_STATES})
DO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DO_STATES}

EC_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Azuay'), ('B', 'Bolívar'), ('C', 'Carchi'), ('F', 'Cañar'), ('H', 'Chimborazo'), ('X', 'Cotopaxi'), ('O', 'El Oro'), ('E', 'Esmeraldas'), ('W', 'Galápagos'), ('G', 'Guayas'), ('I', 'Imbabura'), ('L', 'Loja'), ('R', 'Los Ríos'), ('M', 'Manabí'), ('S', 'Morona-Santiago'), ('N', 'Napo'), ('D', 'Orellana'), ('Y', 'Pastaza'), ('P', 'Pichincha'), ('SE', 'Santa Elena'), ('SD', 'Santo Domingo de los Tsáchilas'), ('U', 'Sucumbíos'), ('T', 'Tungurahua'), ('Z', 'Zamora-Chinchipe'))
]
EC_STATES_DICT = CapsDict({state.abbr: state.name for state in EC_STATES})
EC_STATES_BY_NAME_DICT = {state.name.upper(): state for state in EC_STATES}

EG_STATES = [State(abbr, name) for abbr, name in 
    (('DK', 'Ad Daqahlīyah'), ('BA', 'Al Baḩr al Aḩmar'), ('BH', 'Al Buḩayrah'), ('FYM', 'Al Fayyūm'), ('GH', 'Al Gharbīyah'), ('ALX', 'Al Iskandarīyah'), ('IS', 'Al Ismāٰīlīyah'), ('GZ', 'Al Jīzah'), ('MN', 'Al Minyā'), ('MNF', 'Al Minūfīyah'), ('KB', 'Al Qalyūbīyah'), ('C', 'Al Qāhirah'), ('LX', 'Al Uqşur'), ('WAD', 'Al Wādī al Jadīd'), ('SUZ', 'As Suways'), ('SU', 'As Sādis min Uktūbar'), ('SHR', 'Ash Sharqīyah'), ('ASN', 'Aswān'), ('AST', 'Asyūţ'), ('BNS', 'Banī Suwayf'), ('PTS', 'Būr Saٰīd'), ('DT', 'Dumyāţ'), ('JS', "Janūb Sīnā'"), ('KFS', 'Kafr ash Shaykh'), ('MT', 'Maţrūḩ'), ('KN', 'Qinā'), ('SIN', "Shamāl Sīnā'"), ('SHG', 'Sūhāj'), ('HU', 'Ḩulwān'))
]
EG_STATES_DICT = CapsDict({state.abbr: state.name for state in EG_STATES})
EG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in EG_STATES}

SV_STATES = [State(abbr, name) for abbr, name in 
    (('AH', 'Ahuachapán'), ('CA', 'Cabañas'), ('CH', 'Chalatenango'), ('CU', 'Cuscatlán'), ('LI', 'La Libertad'), ('PA', 'La Paz'), ('UN', 'La Unión'), ('MO', 'Morazán'), ('SM', 'San Miguel'), ('SS', 'San Salvador'), ('SV', 'San Vicente'), ('SA', 'Santa Ana'), ('SO', 'Sonsonate'), ('US', 'Usulután'))
]
SV_STATES_DICT = CapsDict({state.abbr: state.name for state in SV_STATES})
SV_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SV_STATES}

GQ_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Región Continental'), ('I', 'Región Insular'))
]
GQ_STATES_DICT = CapsDict({state.abbr: state.name for state in GQ_STATES})
GQ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GQ_STATES}

ER_STATES = [State(abbr, name) for abbr, name in 
    (('MA', 'Al Awsaţ'), ('DU', 'Al Janūbĩ'), ('AN', 'Ansabā'), ('DK', 'Janūbī al Baḩrī al Aḩmar'), ('GB', 'Qāsh-Barkah'), ('SK', 'Shimālī al Baḩrī al Aḩmar'))
]
ER_STATES_DICT = CapsDict({state.abbr: state.name for state in ER_STATES})
ER_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ER_STATES}

EE_STATES = [State(abbr, name) for abbr, name in 
    (('37', 'Harjumaa'), ('39', 'Hiiumaa'), ('44', 'Ida-Virumaa'), ('51', 'Järvamaa'), ('49', 'Jõgevamaa'), ('59', 'Lääne-Virumaa'), ('57', 'Läänemaa'), ('67', 'Pärnumaa'), ('65', 'Põlvamaa'), ('70', 'Raplamaa'), ('74', 'Saaremaa'), ('78', 'Tartumaa'), ('82', 'Valgamaa'), ('84', 'Viljandimaa'), ('86', 'Võrumaa'))
]
EE_STATES_DICT = CapsDict({state.abbr: state.name for state in EE_STATES})
EE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in EE_STATES}

ET_STATES = [State(abbr, name) for abbr, name in 
    (('BE', 'Bīnshangul Gumuz'), ('DD', 'Dirē Dawa'), ('GA', 'Gambēla Hizboch'), ('HA', 'Hārerī Hizb'), ('OR', 'Oromīya'), ('SO', 'Sumalē'), ('TI', 'Tigray'), ('SN', 'YeDebub Bihēroch Bihēreseboch na Hizboch'), ('AA', 'Ādīs Ābeba'), ('AF', 'Āfar'), ('AM', 'Āmara'))
]
ET_STATES_DICT = CapsDict({state.abbr: state.name for state in ET_STATES})
ET_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ET_STATES}

FJ_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Central'), ('E', 'Eastern'), ('N', 'Northern'), ('R', 'Rotuma'), ('W', 'Western'))
]
FJ_STATES_DICT = CapsDict({state.abbr: state.name for state in FJ_STATES})
FJ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in FJ_STATES}

FI_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Ahvenanmaan maakunta'), ('02', 'Etelä-Karjala'), ('03', 'Etelä-Pohjanmaa'), ('04', 'Etelä-Savo'), ('05', 'Kainuu'), ('06', 'Kanta-Häme'), ('07', 'Keski-Pohjanmaa'), ('08', 'Keski-Suomi'), ('09', 'Kymenlaakso'), ('10', 'Lappi'), ('11', 'Pirkanmaa'), ('12', 'Pohjanmaa'), ('13', 'Pohjois-Karjala'), ('14', 'Pohjois-Pohjanmaa'), ('15', 'Pohjois-Savo'), ('16', 'Päijät-Häme'), ('17', 'Satakunta'), ('18', 'Uusimaa'), ('19', 'Varsinais-Suomi'))
]
FI_STATES_DICT = CapsDict({state.abbr: state.name for state in FI_STATES})
FI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in FI_STATES}

FR_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Alsace'), ('B', 'Aquitaine'), ('C', 'Auvergne'), ('E', 'Brittany'), ('D', 'Burgundy'), ('F', 'Centre-Val de Loire'), ('G', 'Champagne-Ardenne'), ('H', 'Corsica'), ('I', 'Franche-Comté'), ('K', 'Languedoc-Roussillon'), ('L', 'Limousin'), ('M', 'Lorraine'), ('P', 'Lower Normandy'), ('N', 'Midi-Pyrénées'), ('O', 'Nord-Pas-de-Calais'), ('R', 'Pays de la Loire'), ('S', 'Picardy'), ('T', 'Poitou-Charentes'), ('U', "Provence-Alpes-Côte d'Azur"), ('V', 'Rhône-Alpes'), ('Q', 'Upper Normandy'), ('J', 'Île-de-France'))
]
FR_STATES_DICT = CapsDict({state.abbr: state.name for state in FR_STATES})
FR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in FR_STATES}

GA_STATES = [State(abbr, name) for abbr, name in 
    (('1', 'Estuaire'), ('2', 'Haut-Ogooué'), ('3', 'Moyen-Ogooué'), ('4', 'Ngounié'), ('5', 'Nyanga'), ('6', 'Ogooué-Ivindo'), ('7', 'Ogooué-Lolo'), ('8', 'Ogooué-Maritime'), ('9', 'Woleu-Ntem'))
]
GA_STATES_DICT = CapsDict({state.abbr: state.name for state in GA_STATES})
GA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GA_STATES}

GM_STATES = [State(abbr, name) for abbr, name in 
    (('B', 'Banjul'), ('M', 'Central River'), ('L', 'Lower River'), ('N', 'North Bank'), ('U', 'Upper River'), ('W', 'Western'))
]
GM_STATES_DICT = CapsDict({state.abbr: state.name for state in GM_STATES})
GM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GM_STATES}

GE_STATES = [State(abbr, name) for abbr, name in 
    (('AB', 'Abkhazia'), ('AJ', 'Ajaria'), ('GU', 'Guria'), ('IM', 'Imereti'), ('KA', "K'akheti"), ('KK', 'Kvemo Kartli'), ('MM', 'Mtskheta-Mtianeti'), ('RL', "Rach'a-Lechkhumi-Kvemo Svaneti"), ('SZ', 'Samegrelo-Zemo Svaneti'), ('SJ', 'Samtskhe-Javakheti'), ('SK', 'Shida Kartli'), ('TB', 'Tbilisi'))
]
GE_STATES_DICT = CapsDict({state.abbr: state.name for state in GE_STATES})
GE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GE_STATES}

DE_STATES = [State(abbr, name) for abbr, name in 
    (('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'), ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'), ('MV', 'Mecklenburg-Vorpommern'), ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'), ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'), ('SN', 'Sachsen'), ('ST', 'Sachsen-Anhalt'), ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen'))
]
DE_STATES_DICT = CapsDict({state.abbr: state.name for state in DE_STATES})
DE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in DE_STATES}

GH_STATES = [State(abbr, name) for abbr, name in 
    (('AH', 'Ashanti'), ('BA', 'Brong-Ahafo'), ('CP', 'Central'), ('EP', 'Eastern'), ('AA', 'Greater Accra'), ('NP', 'Northern'), ('UE', 'Upper East'), ('UW', 'Upper West'), ('TV', 'Volta'), ('WP', 'Western'))
]
GH_STATES_DICT = CapsDict({state.abbr: state.name for state in GH_STATES})
GH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GH_STATES}

GR_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Anatoliki Makedonia kai Thraki'), ('I', 'Attiki'), ('G', 'Dytiki Ellada'), ('C', 'Dytiki Makedonia'), ('F', 'Ionia Nisia'), ('D', 'Ipeiros'), ('B', 'Kentriki Makedonia'), ('M', 'Kriti'), ('L', 'Notio Aigaio'), ('J', 'Peloponnisos'), ('H', 'Sterea Ellada'), ('E', 'Thessalia'), ('K', 'Voreio Aigaio'))
]
GR_STATES_DICT = CapsDict({state.abbr: state.name for state in GR_STATES})
GR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GR_STATES}

GL_STATES = [State(abbr, name) for abbr, name in 
    (('KU', 'Kommune Kujalleq'), ('SM', 'Kommuneqarfik Sermersooq'), ('QA', 'Qaasuitsup Kommunia'), ('QE', 'Qeqqata Kommunia'))
]
GL_STATES_DICT = CapsDict({state.abbr: state.name for state in GL_STATES})
GL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GL_STATES}

GD_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Saint Andrew'), ('02', 'Saint David'), ('03', 'Saint George'), ('04', 'Saint John'), ('05', 'Saint Mark'), ('06', 'Saint Patrick'), ('10', 'Southern Grenadine Islands'))
]
GD_STATES_DICT = CapsDict({state.abbr: state.name for state in GD_STATES})
GD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GD_STATES}

GT_STATES = [State(abbr, name) for abbr, name in 
    (('AV', 'Alta Verapaz'), ('BV', 'Baja Verapaz'), ('CM', 'Chimaltenango'), ('CQ', 'Chiquimula'), ('PR', 'El Progreso'), ('ES', 'Escuintla'), ('GU', 'Guatemala'), ('HU', 'Huehuetenango'), ('IZ', 'Izabal'), ('JA', 'Jalapa'), ('JU', 'Jutiapa'), ('PE', 'Petén'), ('QZ', 'Quetzaltenango'), ('QC', 'Quiché'), ('RE', 'Retalhuleu'), ('SA', 'Sacatepéquez'), ('SM', 'San Marcos'), ('SR', 'Santa Rosa'), ('SO', 'Sololá'), ('SU', 'Suchitepéquez'), ('TO', 'Totonicapán'), ('ZA', 'Zacapa'))
]
GT_STATES_DICT = CapsDict({state.abbr: state.name for state in GT_STATES})
GT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GT_STATES}

GN_STATES = [State(abbr, name) for abbr, name in 
    (('B', 'Boké'), ('C', 'Conakry'), ('F', 'Faranah'), ('K', 'Kankan'), ('D', 'Kindia'), ('L', 'Labé'), ('M', 'Mamou'), ('N', 'Nzérékoré'))
]
GN_STATES_DICT = CapsDict({state.abbr: state.name for state in GN_STATES})
GN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GN_STATES}

GW_STATES = [State(abbr, name) for abbr, name in 
    (('L', 'Leste'), ('N', 'Norte'), ('S', 'Sul'))
]
GW_STATES_DICT = CapsDict({state.abbr: state.name for state in GW_STATES})
GW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GW_STATES}

GY_STATES = [State(abbr, name) for abbr, name in 
    (('BA', 'Barima-Waini'), ('CU', 'Cuyuni-Mazaruni'), ('DE', 'Demerara-Mahaica'), ('EB', 'East Berbice-Corentyne'), ('ES', 'Essequibo Islands-West Demerara'), ('MA', 'Mahaica-Berbice'), ('PM', 'Pomeroon-Supenaam'), ('PT', 'Potaro-Siparuni'), ('UD', 'Upper Demerara-Berbice'), ('UT', 'Upper Takutu-Upper Essequibo'))
]
GY_STATES_DICT = CapsDict({state.abbr: state.name for state in GY_STATES})
GY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GY_STATES}

HT_STATES = [State(abbr, name) for abbr, name in 
    (('AR', 'Artibonite'), ('CE', 'Centre'), ('GA', 'Grande-Anse'), ('NI', 'Nippes'), ('ND', 'Nord'), ('NE', 'Nord-Est'), ('NO', 'Nord-Ouest'), ('OU', 'Ouest'), ('SD', 'Sud'), ('SE', 'Sud-Est'))
]
HT_STATES_DICT = CapsDict({state.abbr: state.name for state in HT_STATES})
HT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in HT_STATES}

HN_STATES = [State(abbr, name) for abbr, name in 
    (('AT', 'Atlántida'), ('CH', 'Choluteca'), ('CL', 'Colón'), ('CM', 'Comayagua'), ('CP', 'Copán'), ('CR', 'Cortés'), ('EP', 'El Paraíso'), ('FM', 'Francisco Morazán'), ('GD', 'Gracias a Dios'), ('IN', 'Intibucá'), ('IB', 'Islas de la Bahía'), ('LP', 'La Paz'), ('LE', 'Lempira'), ('OC', 'Ocotepeque'), ('OL', 'Olancho'), ('SB', 'Santa Bárbara'), ('VA', 'Valle'), ('YO', 'Yoro'))
]
HN_STATES_DICT = CapsDict({state.abbr: state.name for state in HN_STATES})
HN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in HN_STATES}

HK_STATES = [State(abbr, name) for abbr, name in 
    (('G KONG', 'Hong Kong Island'), ('LOON', 'Kowloon'), (' TERRITORIES', 'New Territories'))
]
HK_STATES_DICT = CapsDict({state.abbr: state.name for state in HK_STATES})
HK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in HK_STATES}

HU_STATES = [State(abbr, name) for abbr, name in 
    (('BA', 'Baranya'), ('BZ', 'Borsod-Abaúj-Zemplén'), ('BU', 'Budapest'), ('BK', 'Bács-Kiskun'), ('BE', 'Békés'), ('BC', 'Békéscsaba'), ('CS', 'Csongrád'), ('DE', 'Debrecen'), ('DU', 'Dunaújváros'), ('EG', 'Eger'), ('FE', 'Fejér'), ('GY', 'Győr'), ('GS', 'Győr-Moson-Sopron'), ('HB', 'Hajdú-Bihar'), ('HE', 'Heves'), ('HV', 'Hódmezővásárhely'), ('JN', 'Jász-Nagykun-Szolnok'), ('KV', 'Kaposvár'), ('KM', 'Kecskemét'), ('KE', 'Komárom-Esztergom'), ('MI', 'Miskolc'), ('NK', 'Nagykanizsa'), ('NY', 'Nyíregyháza'), ('NO', 'Nógrád'), ('PE', 'Pest'), ('PS', 'Pécs'), ('ST', 'Salgótarján'), ('SO', 'Somogy'), ('SN', 'Sopron'), ('SZ', 'Szabolcs-Szatmár-Bereg'), ('SD', 'Szeged'), ('SS', 'Szekszárd'), ('SK', 'Szolnok'), ('SH', 'Szombathely'), ('SF', 'Székesfehérvár'), ('TB', 'Tatabánya'), ('TO', 'Tolna'), ('VA', 'Vas'), ('VE', 'Veszprém'), ('VM', 'Veszprém'), ('ZA', 'Zala'), ('ZE', 'Zalaegerszeg'), ('ER', 'Érd'))
]
HU_STATES_DICT = CapsDict({state.abbr: state.name for state in HU_STATES})
HU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in HU_STATES}

IS_STATES = [State(abbr, name) for abbr, name in 
    (('7', 'Austurland'), ('1', 'Höfuðborgarsvæði utan Reykjavíkur'), ('6', 'Norðurland eystra'), ('5', 'Norðurland vestra'), ('0', 'Reykjavík'), ('8', 'Suðurland'), ('2', 'Suðurnes'), ('4', 'Vestfirðir'), ('3', 'Vesturland'))
]
IS_STATES_DICT = CapsDict({state.abbr: state.name for state in IS_STATES})
IS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IS_STATES}

IN_STATES = [State(abbr, name) for abbr, name in 
    (('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Puducherry'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal'))
]
IN_STATES_DICT = CapsDict({state.abbr: state.name for state in IN_STATES})
IN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IN_STATES}

ID_STATES = [State(abbr, name) for abbr, name in 
    (('JW', 'Jawa'), ('KA', 'Kalimantan'), ('ML', 'Maluku'), ('NU', 'Nusa Tenggara'), ('PP', 'Papua'), ('SL', 'Sulawesi'), ('SM', 'Sumatera'))
]
ID_STATES_DICT = CapsDict({state.abbr: state.name for state in ID_STATES})
ID_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ID_STATES}

IR_STATES = [State(abbr, name) for abbr, name in 
    (('32', 'Alborz'), ('03', 'Ardabīl'), ('06', 'Būshehr'), ('08', 'Chahār Maḩāll va Bakhtīārī'), ('04', 'Eşfahān'), ('14', 'Fārs'), ('27', 'Golestān'), ('19', 'Gīlān'), ('24', 'Hamadān'), ('23', 'Hormozgān'), ('15', 'Kermān'), ('17', 'Kermānshāh'), ('29', 'Khorāsān-e Janūbī'), ('30', 'Khorāsān-e Razavī'), ('31', 'Khorāsān-e Shemālī'), ('10', 'Khūzestān'), ('18', 'Kohgīlūyeh va Būyer Aḩmad'), ('16', 'Kordestān'), ('20', 'Lorestān'), ('22', 'Markazī'), ('21', 'Māzandarān'), ('28', 'Qazvīn'), ('26', 'Qom'), ('12', 'Semnān'), ('13', 'Sīstān va Balūchestān'), ('07', 'Tehrān'), ('25', 'Yazd'), ('11', 'Zanjān'), ('02', 'Āz̄arbāyjān-e Gharbī'), ('01', 'Āz̄arbāyjān-e Sharqī'), ('05', 'Īlām'))
]
IR_STATES_DICT = CapsDict({state.abbr: state.name for state in IR_STATES})
IR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IR_STATES}

IQ_STATES = [State(abbr, name) for abbr, name in 
    (('AN', 'Al Anbār'), ('BA', 'Al Başrah'), ('MU', 'Al Muthanná'), ('QA', 'Al Qādisīyah'), ('NA', 'An Najaf'), ('AR', 'Arbīl'), ('SU', 'As Sulaymānīyah'), ('TS', "At Ta'mīm"), ('BG', 'Baghdād'), ('BB', 'Bābil'), ('DA', 'Dahūk'), ('DQ', 'Dhī Qār'), ('DI', 'Diyālá'), ('KA', "Karbalā'"), ('MA', 'Maysān'), ('NI', 'Nīnawá'), ('WA', 'Wāsiţ'), ('SD', 'Şalāḩ ad Dīn'))
]
IQ_STATES_DICT = CapsDict({state.abbr: state.name for state in IQ_STATES})
IQ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IQ_STATES}

IE_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Connaught'), ('L', 'Leinster'), ('M', 'Munster'), ('U', 'Ulster'))
]
IE_STATES_DICT = CapsDict({state.abbr: state.name for state in IE_STATES})
IE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IE_STATES}

IL_STATES = [State(abbr, name) for abbr, name in 
    (('D', 'HaDarom'), ('M', 'HaMerkaz'), ('Z', 'HaTsafon'), ('HA', 'H̱efa'), ('TA', 'Tel-Aviv'), ('JM', 'Yerushalayim'))
]
IL_STATES_DICT = CapsDict({state.abbr: state.name for state in IL_STATES})
IL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IL_STATES}

IT_STATES = [State(abbr, name) for abbr, name in 
    (('65', 'Abruzzo'), ('77', 'Basilicata'), ('78', 'Calabria'), ('72', 'Campania'), ('45', 'Emilia-Romagna'), ('36', 'Friuli-Venezia Giulia'), ('62', 'Lazio'), ('42', 'Liguria'), ('25', 'Lombardia'), ('57', 'Marche'), ('67', 'Molise'), ('21', 'Piemonte'), ('75', 'Puglia'), ('88', 'Sardegna'), ('82', 'Sicilia'), ('52', 'Toscana'), ('32', 'Trentino-Alto Adige'), ('55', 'Umbria'), ('23', "Valle d'Aosta"), ('34', 'Veneto'))
]
IT_STATES_DICT = CapsDict({state.abbr: state.name for state in IT_STATES})
IT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in IT_STATES}

JM_STATES = [State(abbr, name) for abbr, name in 
    (('13', 'Clarendon'), ('09', 'Hanover'), ('01', 'Kingston'), ('12', 'Manchester'), ('04', 'Portland'), ('02', 'Saint Andrew'), ('06', 'Saint Ann'), ('14', 'Saint Catherine'), ('11', 'Saint Elizabeth'), ('08', 'Saint James'), ('05', 'Saint Mary'), ('03', 'Saint Thomas'), ('07', 'Trelawny'), ('10', 'Westmoreland'))
]
JM_STATES_DICT = CapsDict({state.abbr: state.name for state in JM_STATES})
JM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in JM_STATES}

JP_STATES = [State(abbr, name) for abbr, name in 
    (('23', 'Aiti'), ('05', 'Akita'), ('02', 'Aomori'), ('38', 'Ehime'), ('21', 'Gihu'), ('10', 'Gunma'), ('34', 'Hirosima'), ('01', 'Hokkaidô'), ('18', 'Hukui'), ('40', 'Hukuoka'), ('07', 'Hukusima'), ('28', 'Hyôgo'), ('08', 'Ibaraki'), ('17', 'Isikawa'), ('03', 'Iwate'), ('37', 'Kagawa'), ('46', 'Kagosima'), ('14', 'Kanagawa'), ('43', 'Kumamoto'), ('26', 'Kyôto'), ('39', 'Kôti'), ('24', 'Mie'), ('04', 'Miyagi'), ('45', 'Miyazaki'), ('20', 'Nagano'), ('42', 'Nagasaki'), ('29', 'Nara'), ('15', 'Niigata'), ('33', 'Okayama'), ('47', 'Okinawa'), ('41', 'Saga'), ('11', 'Saitama'), ('25', 'Siga'), ('32', 'Simane'), ('22', 'Sizuoka'), ('12', 'Tiba'), ('36', 'Tokusima'), ('09', 'Totigi'), ('31', 'Tottori'), ('16', 'Toyama'), ('13', 'Tôkyô'), ('30', 'Wakayama'), ('06', 'Yamagata'), ('35', 'Yamaguti'), ('19', 'Yamanasi'), ('44', 'Ôita'), ('27', 'Ôsaka'))
]
JP_STATES_DICT = CapsDict({state.abbr: state.name for state in JP_STATES})
JP_STATES_BY_NAME_DICT = {state.name.upper(): state for state in JP_STATES}

JO_STATES = [State(abbr, name) for abbr, name in 
    (('BA', "Al Balqā'"), ('AQ', 'Al ʽAqabah'), ('AZ', "Az Zarqā'"), ('AT', 'Aţ Ţafīlah'), ('IR', 'Irbid'), ('JA', 'Jerash'), ('KA', 'Karak'), ('MN', "Ma'ān"), ('MA', 'Mafraq'), ('MD', 'Mādabā'), ('AJ', 'ʽAjlūn'), ('AM', '‘Ammān'))
]
JO_STATES_DICT = CapsDict({state.abbr: state.name for state in JO_STATES})
JO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in JO_STATES}

KZ_STATES = [State(abbr, name) for abbr, name in 
    (('ALA', 'Almaty'), ('ALM', 'Almaty oblysy'), ('AKM', 'Aqmola oblysy'), ('AKT', 'Aqtöbe oblysy'), ('AST', 'Astana'), ('ATY', 'Atyraū oblysy'), ('ZAP', 'Batys Qazaqstan oblysy'), ('MAN', 'Mangghystaū oblysy'), ('YUZ', 'Ongtüstik Qazaqstan oblysy'), ('PAV', 'Pavlodar oblysy'), ('KAR', 'Qaraghandy oblysy'), ('KUS', 'Qostanay oblysy'), ('KZY', 'Qyzylorda oblysy'), ('VOS', 'Shyghys Qazaqstan oblysy'), ('SEV', 'Soltüstik Qazaqstan oblysy'), ('ZHA', 'Zhambyl oblysy'))
]
KZ_STATES_DICT = CapsDict({state.abbr: state.name for state in KZ_STATES})
KZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KZ_STATES}

KE_STATES = [State(abbr, name) for abbr, name in 
    (('200', 'Central'), ('300', 'Coast'), ('400', 'Eastern'), ('110', 'Nairobi'), ('500', 'North-Eastern'), ('600', 'Nyanza'), ('700', 'Rift Valley'), ('800', 'Western'))
]
KE_STATES_DICT = CapsDict({state.abbr: state.name for state in KE_STATES})
KE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KE_STATES}

KI_STATES = [State(abbr, name) for abbr, name in 
    (('G', 'Gilbert Islands'), ('L', 'Line Islands'), ('P', 'Phoenix Islands'))
]
KI_STATES_DICT = CapsDict({state.abbr: state.name for state in KI_STATES})
KI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KI_STATES}

KP_STATES = [State(abbr, name) for abbr, name in 
    (('04', 'Chagang'), ('07', 'Kangwon'), ('09', 'North Hamgyong'), ('06', 'North Hwanghae'), ('03', 'North Pyongan'), ('01', 'Pyongyang'), ('13', 'Rason'), ('10', 'Ryanggang'), ('08', 'South Hamgyong'), ('05', 'South Hwanghae'), ('02', 'South Pyongan'))
]
KP_STATES_DICT = CapsDict({state.abbr: state.name for state in KP_STATES})
KP_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KP_STATES}

KR_STATES = [State(abbr, name) for abbr, name in 
    (('26', 'Busan-gwangyeoksi'), ('43', 'Chungcheongbuk-do'), ('44', 'Chungcheongnam-do'), ('27', 'Daegu-gwangyeoksi'), ('30', 'Daejeon-gwangyeoksi'), ('42', 'Gangwon-do'), ('29', 'Gwangju-gwangyeoksi'), ('41', 'Gyeonggi-do'), ('47', 'Gyeongsangbuk-do'), ('48', 'Gyeongsangnam-do'), ('28', 'Incheon-gwangyeoksi'), ('49', 'Jeju-teukbyeoljachido'), ('45', 'Jeollabuk-do'), ('46', 'Jeollanam-do'), ('50', 'Sejong'), ('11', 'Seoul-teukbyeolsi'), ('31', 'Ulsan-gwangyeoksi'))
]
KR_STATES_DICT = CapsDict({state.abbr: state.name for state in KR_STATES})
KR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KR_STATES}

KW_STATES = [State(abbr, name) for abbr, name in 
    (('AH', 'Al Aḩmadi'), ('FA', 'Al Farwānīyah'), ('JA', 'Al Jahrā’'), ('KU', 'Al Kuwayt'), ('MU', 'Mubārak al Kabīr'), ('HA', 'Ḩawallī'))
]
KW_STATES_DICT = CapsDict({state.abbr: state.name for state in KW_STATES})
KW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KW_STATES}

KG_STATES = [State(abbr, name) for abbr, name in 
    (('B', 'Batken'), ('GB', 'Bishkek'), ('C', 'Chü'), ('J', 'Jalal-Abad'), ('N', 'Naryn'), ('O', 'Osh'), ('T', 'Talas'), ('Y', 'Ysyk-Köl'))
]
KG_STATES_DICT = CapsDict({state.abbr: state.name for state in KG_STATES})
KG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KG_STATES}

LA_STATES = [State(abbr, name) for abbr, name in 
    (('AT', 'Attapu'), ('BK', 'Bokèo'), ('BL', 'Bolikhamxai'), ('CH', 'Champasak'), ('HO', 'Houaphan'), ('KH', 'Khammouan'), ('LM', 'Louang Namtha'), ('LP', 'Louangphabang'), ('OU', 'Oudômxai'), ('PH', 'Phôngsali'), ('SL', 'Salavan'), ('SV', 'Savannakhét'), ('VT', 'Vientiane'), ('VI', 'Vientiane'), ('XA', 'Xaignabouli'), ('XN', 'Xaisômboun'), ('XI', 'Xiangkhoang'), ('XE', 'Xékong'))
]
LA_STATES_DICT = CapsDict({state.abbr: state.name for state in LA_STATES})
LA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LA_STATES}

LV_STATES = [State(abbr, name) for abbr, name in 
    (('001', 'Aglonas novads'), ('002', 'Aizkraukles novads'), ('003', 'Aizputes novads'), ('004', 'Aknīstes novads'), ('005', 'Alojas novads'), ('006', 'Alsungas novads'), ('007', 'Alūksnes novads'), ('008', 'Amatas novads'), ('009', 'Apes novads'), ('010', 'Auces novads'), ('012', 'Babītes novads'), ('013', 'Baldones novads'), ('014', 'Baltinavas novads'), ('015', 'Balvu novads'), ('016', 'Bauskas novads'), ('017', 'Beverīnas novads'), ('018', 'Brocēnu novads'), ('019', 'Burtnieku novads'), ('020', 'Carnikavas novads'), ('021', 'Cesvaines novads'), ('023', 'Ciblas novads'), ('022', 'Cēsu novads'), ('024', 'Dagdas novads'), ('DGV', 'Daugavpils'), ('025', 'Daugavpils novads'), ('026', 'Dobeles novads'), ('027', 'Dundagas novads'), ('028', 'Durbes novads'), ('029', 'Engures novads'), ('031', 'Garkalnes novads'), ('032', 'Grobiņas novads'), ('033', 'Gulbenes novads'), ('034', 'Iecavas novads'), ('035', 'Ikšķiles novads'), ('036', 'Ilūkstes novads'), ('037', 'Inčukalna novads'), ('038', 'Jaunjelgavas novads'), ('039', 'Jaunpiebalgas novads'), ('040', 'Jaunpils novads'), ('JEL', 'Jelgava'), ('041', 'Jelgavas novads'), ('JKB', 'Jēkabpils'), ('042', 'Jēkabpils novads'), ('JUR', 'Jūrmala'), ('043', 'Kandavas novads'), ('045', 'Kocēnu novads'), ('046', 'Kokneses novads'), ('048', 'Krimuldas novads'), ('049', 'Krustpils novads'), ('047', 'Krāslavas novads'), ('050', 'Kuldīgas novads'), ('044', 'Kārsavas novads'), ('053', 'Lielvārdes novads'), ('LPX', 'Liepāja'), ('054', 'Limbažu novads'), ('057', 'Lubānas novads'), ('058', 'Ludzas novads'), ('055', 'Līgatnes novads'), ('056', 'Līvānu novads'), ('059', 'Madonas novads'), ('060', 'Mazsalacas novads'), ('061', 'Mālpils novads'), ('062', 'Mārupes novads'), ('063', 'Mērsraga novads'), ('064', 'Naukšēnu novads'), ('065', 'Neretas novads'), ('066', 'Nīcas novads'), ('067', 'Ogres novads'), ('068', 'Olaines novads'), ('069', 'Ozolnieku novads'), ('073', 'Preiļu novads'), ('074', 'Priekules novads'), ('075', 'Priekuļu novads'), ('070', 'Pārgaujas novads'), ('071', 'Pāvilostas novads'), ('072', 'Pļaviņu novads'), ('076', 'Raunas novads'), ('078', 'Riebiņu novads'), ('079', 'Rojas novads'), ('080', 'Ropažu novads'), ('081', 'Rucavas novads'), ('082', 'Rugāju novads'), ('083', 'Rundāles novads'), ('REZ', 'Rēzekne'), ('077', 'Rēzeknes novads'), ('RIX', 'Rīga'), ('084', 'Rūjienas novads'), ('086', 'Salacgrīvas novads'), ('085', 'Salas novads'), ('087', 'Salaspils novads'), ('088', 'Saldus novads'), ('089', 'Saulkrastu novads'), ('091', 'Siguldas novads'), ('093', 'Skrundas novads'), ('092', 'Skrīveru novads'), ('094', 'Smiltenes novads'), ('095', 'Stopiņu novads'), ('096', 'Strenču novads'), ('090', 'Sējas novads'), ('097', 'Talsu novads'), ('099', 'Tukuma novads'), ('098', 'Tērvetes novads'), ('100', 'Vaiņodes novads'), ('101', 'Valkas novads'), ('VMR', 'Valmiera'), ('102', 'Varakļānu novads'), ('104', 'Vecpiebalgas novads'), ('105', 'Vecumnieku novads'), ('VEN', 'Ventspils'), ('106', 'Ventspils novads'), ('107', 'Viesītes novads'), ('108', 'Viļakas novads'), ('109', 'Viļānu novads'), ('103', 'Vārkavas novads'), ('110', 'Zilupes novads'), ('011', 'Ādažu novads'), ('030', 'Ērgļu novads'), ('051', 'Ķeguma novads'), ('052', 'Ķekavas novads'))
]
LV_STATES_DICT = CapsDict({state.abbr: state.name for state in LV_STATES})
LV_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LV_STATES}

LB_STATES = [State(abbr, name) for abbr, name in 
    (('AK', 'Aakkâr'), ('BH', 'Baalbek-Hermel'), ('BA', 'Beyrouth'), ('BI', 'Béqaa'), ('AS', 'Liban-Nord'), ('JA', 'Liban-Sud'), ('JL', 'Mont-Liban'), ('NA', 'Nabatîyé'))
]
LB_STATES_DICT = CapsDict({state.abbr: state.name for state in LB_STATES})
LB_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LB_STATES}

LS_STATES = [State(abbr, name) for abbr, name in 
    (('D', 'Berea'), ('B', 'Butha-Buthe'), ('C', 'Leribe'), ('E', 'Mafeteng'), ('A', 'Maseru'), ('F', "Mohale's Hoek"), ('J', 'Mokhotlong'), ('H', "Qacha's Nek"), ('G', 'Quthing'), ('K', 'Thaba-Tseka'))
]
LS_STATES_DICT = CapsDict({state.abbr: state.name for state in LS_STATES})
LS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LS_STATES}

LR_STATES = [State(abbr, name) for abbr, name in 
    (('BM', 'Bomi'), ('BG', 'Bong'), ('GP', 'Gbarpolu'), ('GB', 'Grand Bassa'), ('CM', 'Grand Cape Mount'), ('GG', 'Grand Gedeh'), ('GK', 'Grand Kru'), ('LO', 'Lofa'), ('MG', 'Margibi'), ('MY', 'Maryland'), ('MO', 'Montserrado'), ('NI', 'Nimba'), ('RG', 'River Gee'), ('RI', 'Rivercess'), ('SI', 'Sinoe'))
]
LR_STATES_DICT = CapsDict({state.abbr: state.name for state in LR_STATES})
LR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LR_STATES}

LY_STATES = [State(abbr, name) for abbr, name in 
    (('BU', 'Al Buţnān'), ('JA', 'Al Jabal al Akhḑar'), ('JG', 'Al Jabal al Gharbī'), ('JI', 'Al Jifārah'), ('JU', 'Al Jufrah'), ('KF', 'Al Kufrah'), ('MJ', 'Al Marj'), ('MB', 'Al Marqab'), ('WA', 'Al Wāḩāt'), ('NQ', 'An Nuqaţ al Khams'), ('ZA', 'Az Zāwiyah'), ('BA', 'Banghāzī'), ('DR', 'Darnah'), ('GT', 'Ghāt'), ('MI', 'Mişrātah'), ('MQ', 'Murzuq'), ('NL', 'Nālūt'), ('SB', 'Sabhā'), ('SR', 'Surt'), ('WD', 'Wādī al Ḩayāt'), ('WS', 'Wādī ash Shāţiʾ'), ('TB', 'Ţarābulus'))
]
LY_STATES_DICT = CapsDict({state.abbr: state.name for state in LY_STATES})
LY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LY_STATES}

LI_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Balzers'), ('02', 'Eschen'), ('03', 'Gamprin'), ('04', 'Mauren'), ('05', 'Planken'), ('06', 'Ruggell'), ('07', 'Schaan'), ('08', 'Schellenberg'), ('09', 'Triesen'), ('10', 'Triesenberg'), ('11', 'Vaduz'))
]
LI_STATES_DICT = CapsDict({state.abbr: state.name for state in LI_STATES})
LI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LI_STATES}

LT_STATES = [State(abbr, name) for abbr, name in 
    (('AL', 'Alytaus Apskritis'), ('KU', 'Kauno Apskritis'), ('KL', 'Klaipėdos Apskritis'), ('MR', 'Marijampolės Apskritis'), ('PN', 'Panevėžio Apskritis'), ('TA', 'Tauragės Apskritis'), ('TE', 'Telšių Apskritis'), ('UT', 'Utenos Apskritis'), ('VL', 'Vilniaus Apskritis'), ('SA', 'Šiaulių Apskritis'))
]
LT_STATES_DICT = CapsDict({state.abbr: state.name for state in LT_STATES})
LT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LT_STATES}

LU_STATES = [State(abbr, name) for abbr, name in 
    (('D', 'Diekirch'), ('G', 'Grevenmacher'), ('L', 'Luxembourg'))
]
LU_STATES_DICT = CapsDict({state.abbr: state.name for state in LU_STATES})
LU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LU_STATES}

MK_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Aerodrom'), ('02', 'Aračinovo'), ('03', 'Berovo'), ('04', 'Bitola'), ('05', 'Bogdanci'), ('06', 'Bogovinje'), ('07', 'Bosilovo'), ('08', 'Brvenica'), ('09', 'Butel'), ('77', 'Centar'), ('78', 'Centar Župa'), ('21', 'Debar'), ('22', 'Debarca'), ('23', 'Delčevo'), ('25', 'Demir Hisar'), ('24', 'Demir Kapija'), ('26', 'Dojran'), ('27', 'Dolneni'), ('28', 'Drugovo'), ('17', 'Gazi Baba'), ('18', 'Gevgelija'), ('29', 'Gjorče Petrov'), ('19', 'Gostivar'), ('20', 'Gradsko'), ('34', 'Ilinden'), ('35', 'Jegunovce'), ('37', 'Karbinci'), ('38', 'Karpoš'), ('36', 'Kavadarci'), ('39', 'Kisela Voda'), ('40', 'Kičevo'), ('41', 'Konče'), ('42', 'Kočani'), ('43', 'Kratovo'), ('44', 'Kriva Palanka'), ('45', 'Krivogaštani'), ('46', 'Kruševo'), ('47', 'Kumanovo'), ('48', 'Lipkovo'), ('49', 'Lozovo'), ('51', 'Makedonska Kamenica'), ('52', 'Makedonski Brod'), ('50', 'Mavrovo i Rostuša'), ('53', 'Mogila'), ('54', 'Negotino'), ('55', 'Novaci'), ('56', 'Novo Selo'), ('58', 'Ohrid'), ('57', 'Oslomej'), ('60', 'Pehčevo'), ('59', 'Petrovec'), ('61', 'Plasnica'), ('62', 'Prilep'), ('63', 'Probištip'), ('64', 'Radoviš'), ('65', 'Rankovce'), ('66', 'Resen'), ('67', 'Rosoman'), ('68', 'Saraj'), ('70', 'Sopište'), ('71', 'Staro Nagoričane'), ('72', 'Struga'), ('73', 'Strumica'), ('74', 'Studeničani'), ('69', 'Sveti Nikole'), ('75', 'Tearce'), ('76', 'Tetovo'), ('10', 'Valandovo'), ('11', 'Vasilevo'), ('13', 'Veles'), ('12', 'Vevčani'), ('14', 'Vinica'), ('15', 'Vraneštica'), ('16', 'Vrapčište'), ('31', 'Zajas'), ('32', 'Zelenikovo'), ('33', 'Zrnovci'), ('79', 'Čair'), ('80', 'Čaška'), ('81', 'Češinovo-Obleševo'), ('82', 'Čučer Sandevo'), ('83', 'Štip'), ('84', 'Šuto Orizari'), ('30', 'Želino'))
]
MK_STATES_DICT = CapsDict({state.abbr: state.name for state in MK_STATES})
MK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MK_STATES}

MG_STATES = [State(abbr, name) for abbr, name in 
    (('T', 'Antananarivo'), ('D', 'Antsiranana'), ('F', 'Fianarantsoa'), ('M', 'Mahajanga'), ('A', 'Toamasina'), ('U', 'Toliara'))
]
MG_STATES_DICT = CapsDict({state.abbr: state.name for state in MG_STATES})
MG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MG_STATES}

MW_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Central Region'), ('N', 'Northern Region'), ('S', 'Southern Region'))
]
MW_STATES_DICT = CapsDict({state.abbr: state.name for state in MW_STATES})
MW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MW_STATES}

MY_STATES = [State(abbr, name) for abbr, name in 
    (('14', 'Wilayah Persekutuan Kuala Lumpur'), ('15', 'Wilayah Persekutuan Labuan'), ('16', 'Wilayah Persekutuan Putrajaya'), ('01', 'Johor'), ('02', 'Kedah'), ('03', 'Kelantan'), ('04', 'Melaka'), ('05', 'Negeri Sembilan'), ('06', 'Pahang'), ('08', 'Perak'), ('09', 'Perlis'), ('07', 'Pulau Pinang'), ('12', 'Sabah'), ('13', 'Sarawak'), ('10', 'Selangor'), ('11', 'Terengganu'))
]
MY_STATES_DICT = CapsDict({state.abbr: state.name for state in MY_STATES})
MY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MY_STATES}

MV_STATES = [State(abbr, name) for abbr, name in 
    (('CE', 'Central'), ('MLE', 'Male'), ('NO', 'North'), ('NC', 'North Central'), ('SU', 'South'), ('SC', 'South Central'), ('UN', 'Upper North'), ('US', 'Upper South'))
]
MV_STATES_DICT = CapsDict({state.abbr: state.name for state in MV_STATES})
MV_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MV_STATES}

ML_STATES = [State(abbr, name) for abbr, name in 
    (('BKO', 'Bamako'), ('7', 'Gao'), ('1', 'Kayes'), ('8', 'Kidal'), ('2', 'Koulikoro'), ('5', 'Mopti'), ('3', 'Sikasso'), ('4', 'Ségou'), ('6', 'Tombouctou'))
]
ML_STATES_DICT = CapsDict({state.abbr: state.name for state in ML_STATES})
ML_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ML_STATES}

MT_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Attard'), ('02', 'Balzan'), ('03', 'Birgu'), ('04', 'Birkirkara'), ('05', 'Birżebbuġa'), ('06', 'Bormla'), ('07', 'Dingli'), ('08', 'Fgura'), ('09', 'Floriana'), ('10', 'Fontana'), ('11', 'Gudja'), ('13', 'Għajnsielem'), ('14', 'Għarb'), ('15', 'Għargħur'), ('16', 'Għasri'), ('17', 'Għaxaq'), ('12', 'Gżira'), ('19', 'Iklin'), ('20', 'Isla'), ('21', 'Kalkara'), ('22', 'Kerċem'), ('23', 'Kirkop'), ('24', 'Lija'), ('25', 'Luqa'), ('26', 'Marsa'), ('27', 'Marsaskala'), ('28', 'Marsaxlokk'), ('29', 'Mdina'), ('30', 'Mellieħa'), ('32', 'Mosta'), ('33', 'Mqabba'), ('34', 'Msida'), ('35', 'Mtarfa'), ('36', 'Munxar'), ('31', 'Mġarr'), ('37', 'Nadur'), ('38', 'Naxxar'), ('39', 'Paola'), ('40', 'Pembroke'), ('41', 'Pietà'), ('42', 'Qala'), ('43', 'Qormi'), ('44', 'Qrendi'), ('45', 'Rabat Għawdex'), ('46', 'Rabat Malta'), ('47', 'Safi'), ('50', 'San Lawrenz'), ('51', 'San Pawl il-Baħar'), ('48', 'San Ġiljan'), ('49', 'San Ġwann'), ('52', 'Sannat'), ('53', 'Santa Luċija'), ('54', 'Santa Venera'), ('55', 'Siġġiewi'), ('56', 'Sliema'), ('57', 'Swieqi'), ('58', "Ta' Xbiex"), ('59', 'Tarxien'), ('60', 'Valletta'), ('61', 'Xagħra'), ('62', 'Xewkija'), ('63', 'Xgħajra'), ('18', 'Ħamrun'), ('64', 'Żabbar'), ('65', 'Żebbuġ Għawdex'), ('66', 'Żebbuġ Malta'), ('67', 'Żejtun'), ('68', 'Żurrieq'))
]
MT_STATES_DICT = CapsDict({state.abbr: state.name for state in MT_STATES})
MT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MT_STATES}

MH_STATES = [State(abbr, name) for abbr, name in 
    (('L', 'Ralik chain'), ('T', 'Ratak chain'))
]
MH_STATES_DICT = CapsDict({state.abbr: state.name for state in MH_STATES})
MH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MH_STATES}

MR_STATES = [State(abbr, name) for abbr, name in 
    (('07', 'Adrar'), ('03', 'Assaba'), ('05', 'Brakna'), ('08', 'Dakhlet Nouâdhibou'), ('04', 'Gorgol'), ('10', 'Guidimaka'), ('01', 'Hodh ech Chargui'), ('02', 'Hodh el Gharbi'), ('12', 'Inchiri'), ('NKC', 'Nouakchott'), ('09', 'Tagant'), ('11', 'Tiris Zemmour'), ('06', 'Trarza'))
]
MR_STATES_DICT = CapsDict({state.abbr: state.name for state in MR_STATES})
MR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MR_STATES}

MU_STATES = [State(abbr, name) for abbr, name in 
    (('AG', 'Agalega Islands'), ('BR', 'Beau Bassin-Rose Hill'), ('BL', 'Black River'), ('CC', 'Cargados Carajos Shoals'), ('CU', 'Curepipe'), ('FL', 'Flacq'), ('GP', 'Grand Port'), ('MO', 'Moka'), ('PA', 'Pamplemousses'), ('PW', 'Plaines Wilhems'), ('PL', 'Port Louis'), ('PU', 'Port Louis'), ('QB', 'Quatre Bornes'), ('RR', 'Rivière du Rempart'), ('RO', 'Rodrigues Island'), ('SA', 'Savanne'), ('VP', 'Vacoas-Phoenix'))
]
MU_STATES_DICT = CapsDict({state.abbr: state.name for state in MU_STATES})
MU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MU_STATES}

MX_STATES = [State(abbr, name) for abbr, name in 
    (('DIF', 'Distrito Federal'), ('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHP', 'Chiapas'), ('CHH', 'Chihuahua'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GUA', 'Guanajuato'), ('GRO', 'Guerrero'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MIC', 'Michoacán'), ('MOR', 'Morelos'), ('MEX', 'México'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'), ('SLP', 'San Luis Potosí'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatán'), ('ZAC', 'Zacatecas'))
]
MX_STATES_DICT = CapsDict({state.abbr: state.name for state in MX_STATES})
MX_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MX_STATES}

FM_STATES = [State(abbr, name) for abbr, name in 
    (('TRK', 'Chuuk'), ('KSA', 'Kosrae'), ('PNI', 'Pohnpei'), ('YAP', 'Yap'))
]
FM_STATES_DICT = CapsDict({state.abbr: state.name for state in FM_STATES})
FM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in FM_STATES}

MD_STATES = [State(abbr, name) for abbr, name in 
    (('AN', 'Anenii Noi'), ('BS', 'Basarabeasca'), ('BR', 'Briceni'), ('BA', 'Bălţi'), ('CA', 'Cahul'), ('CT', 'Cantemir'), ('CU', 'Chişinău'), ('CM', 'Cimişlia'), ('CR', 'Criuleni'), ('CL', 'Călăraşi'), ('CS', 'Căuşeni'), ('DO', 'Donduşeni'), ('DR', 'Drochia'), ('DU', 'Dubăsari'), ('ED', 'Edineţ'), ('FL', 'Floreşti'), ('FA', 'Făleşti'), ('GL', 'Glodeni'), ('GA', 'Găgăuzia, Unitatea teritorială autonomă'), ('HI', 'Hînceşti'), ('IA', 'Ialoveni'), ('LE', 'Leova'), ('NI', 'Nisporeni'), ('OC', 'Ocniţa'), ('OR', 'Orhei'), ('RE', 'Rezina'), ('RI', 'Rîşcani'), ('SO', 'Soroca'), ('ST', 'Străşeni'), ('SN', 'Stînga Nistrului, unitatea teritorială din'), ('SI', 'Sîngerei'), ('TA', 'Taraclia'), ('TE', 'Teleneşti'), ('BD', 'Tighina'), ('UN', 'Ungheni'), ('SD', 'Şoldăneşti'), ('SV', 'Ştefan Vodă'))
]
MD_STATES_DICT = CapsDict({state.abbr: state.name for state in MD_STATES})
MD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MD_STATES}

MC_STATES = [State(abbr, name) for abbr, name in 
    (('FO', 'Fontvieille'), ('JE', 'Jardin Exotique'), ('CL', 'La Colle'), ('CO', 'La Condamine'), ('GA', 'La Gare'), ('SO', 'La Source'), ('LA', 'Larvotto'), ('MA', 'Malbousquet'), ('MO', 'Monaco-Ville'), ('MG', 'Moneghetti'), ('MC', 'Monte-Carlo'), ('MU', 'Moulins'), ('PH', 'Port-Hercule'), ('SR', 'Saint-Roman'), ('SD', 'Sainte-Dévote'), ('SP', 'Spélugues'), ('VR', 'Vallon de la Rousse'))
]
MC_STATES_DICT = CapsDict({state.abbr: state.name for state in MC_STATES})
MC_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MC_STATES}

MN_STATES = [State(abbr, name) for abbr, name in 
    (('073', 'Arhangay'), ('071', 'Bayan-Ölgiy'), ('069', 'Bayanhongor'), ('067', 'Bulgan'), ('037', 'Darhan uul'), ('061', 'Dornod'), ('063', 'Dornogovĭ'), ('059', 'Dundgovĭ'), ('057', 'Dzavhan'), ('065', 'Govĭ-Altay'), ('064', 'Govĭ-Sümber'), ('039', 'Hentiy'), ('043', 'Hovd'), ('041', 'Hövsgöl'), ('035', 'Orhon'), ('049', 'Selenge'), ('051', 'Sühbaatar'), ('047', 'Töv'), ('1', 'Ulaanbaatar'), ('046', 'Uvs'), ('053', 'Ömnögovĭ'), ('055', 'Övörhangay'))
]
MN_STATES_DICT = CapsDict({state.abbr: state.name for state in MN_STATES})
MN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MN_STATES}

ME_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Andrijevica'), ('02', 'Bar'), ('03', 'Berane'), ('04', 'Bijelo Polje'), ('05', 'Budva'), ('06', 'Cetinje'), ('07', 'Danilovgrad'), ('22', 'Gusinje'), ('08', 'Herceg-Novi'), ('09', 'Kolašin'), ('10', 'Kotor'), ('11', 'Mojkovac'), ('12', 'Nikšić'), ('23', 'Petnjica'), ('13', 'Plav'), ('14', 'Pljevlja'), ('15', 'Plužine'), ('16', 'Podgorica'), ('17', 'Rožaje'), ('19', 'Tivat'), ('20', 'Ulcinj'), ('18', 'Šavnik'), ('21', 'Žabljak'))
]
ME_STATES_DICT = CapsDict({state.abbr: state.name for state in ME_STATES})
ME_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ME_STATES}

MA_STATES = [State(abbr, name) for abbr, name in 
    (('09', 'Chaouia-Ouardigha'), ('10', 'Doukhala-Abda'), ('05', 'Fès-Boulemane'), ('02', 'Gharb-Chrarda-Beni Hssen'), ('08', 'Grand Casablanca'), ('14', 'Guelmim-Es Smara'), ('04', "L'Oriental"), ('15', 'Laâyoune-Boujdour-Sakia el Hamra'), ('11', 'Marrakech-Tensift-Al Haouz'), ('06', 'Meknès-Tafilalet'), ('16', 'Oued ed Dahab-Lagouira'), ('07', 'Rabat-Salé-Zemmour-Zaer'), ('13', 'Souss-Massa-Drâa'), ('12', 'Tadla-Azilal'), ('01', 'Tanger-Tétouan'), ('03', 'Taza-Al Hoceima-Taounate'))
]
MA_STATES_DICT = CapsDict({state.abbr: state.name for state in MA_STATES})
MA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MA_STATES}

MZ_STATES = [State(abbr, name) for abbr, name in 
    (('P', 'Cabo Delgado'), ('G', 'Gaza'), ('I', 'Inhambane'), ('B', 'Manica'), ('MPM', 'Maputo'), ('L', 'Maputo'), ('N', 'Nampula'), ('A', 'Niassa'), ('S', 'Sofala'), ('T', 'Tete'), ('Q', 'Zambézia'))
]
MZ_STATES_DICT = CapsDict({state.abbr: state.name for state in MZ_STATES})
MZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MZ_STATES}

MM_STATES = [State(abbr, name) for abbr, name in 
    (('07', 'Ayeyarwady'), ('02', 'Bago'), ('14', 'Chin'), ('11', 'Kachin'), ('12', 'Kayah'), ('13', 'Kayin'), ('03', 'Magway'), ('04', 'Mandalay'), ('15', 'Mon'), ('16', 'Rakhine'), ('01', 'Sagaing'), ('17', 'Shan'), ('05', 'Tanintharyi'), ('06', 'Yangon'))
]
MM_STATES_DICT = CapsDict({state.abbr: state.name for state in MM_STATES})
MM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in MM_STATES}

NA_STATES = [State(abbr, name) for abbr, name in 
    (('ER', 'Erongo'), ('HA', 'Hardap'), ('KA', 'Karas'), ('KE', 'Kavango East'), ('KW', 'Kavango West'), ('KH', 'Khomas'), ('KU', 'Kunene'), ('OW', 'Ohangwena'), ('OH', 'Omaheke'), ('OS', 'Omusati'), ('ON', 'Oshana'), ('OT', 'Oshikoto'), ('OD', 'Otjozondjupa'), ('CA', 'Zambezi'))
]
NA_STATES_DICT = CapsDict({state.abbr: state.name for state in NA_STATES})
NA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NA_STATES}

NR_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Aiwo'), ('02', 'Anabar'), ('03', 'Anetan'), ('04', 'Anibare'), ('05', 'Baiti'), ('06', 'Boe'), ('07', 'Buada'), ('08', 'Denigomodu'), ('09', 'Ewa'), ('10', 'Ijuw'), ('11', 'Meneng'), ('12', 'Nibok'), ('13', 'Uaboe'), ('14', 'Yaren'))
]
NR_STATES_DICT = CapsDict({state.abbr: state.name for state in NR_STATES})
NR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NR_STATES}

NP_STATES = [State(abbr, name) for abbr, name in 
    (('2', 'Madhya Pashchimanchal'), ('1', 'Madhyamanchal'), ('3', 'Pashchimanchal'), ('4', 'Purwanchal'), ('5', 'Sudur Pashchimanchal'))
]
NP_STATES_DICT = CapsDict({state.abbr: state.name for state in NP_STATES})
NP_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NP_STATES}

NL_STATES = [State(abbr, name) for abbr, name in 
    (('DR', 'Drenthe'), ('FL', 'Flevoland'), ('FR', 'Fryslân'), ('GE', 'Gelderland'), ('GR', 'Groningen'), ('LI', 'Limburg'), ('NB', 'Noord-Brabant'), ('NH', 'Noord-Holland'), ('OV', 'Overijssel'), ('UT', 'Utrecht'), ('ZE', 'Zeeland'), ('ZH', 'Zuid-Holland'), ('AW', 'Aruba'), ('CW', 'Curaçao'), ('SX', 'Sint Maarten'), ('BQ1', 'Bonaire'), ('BQ2', 'Saba'), ('BQ3', 'Sint Eustatius'))
]
NL_STATES_DICT = CapsDict({state.abbr: state.name for state in NL_STATES})
NL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NL_STATES}

NZ_STATES = [State(abbr, name) for abbr, name in 
    (('N', 'North Island'), ('S', 'South Island'), ('AUK', 'Auckland'), ('BOP', 'Bay of Plenty'), ('CAN', 'Canterbury'), ('HKB', "Hawke's Bay"), ('MWT', 'Manawatu-Wanganui'), ('NTL', 'Northland'), ('OTA', 'Otago'), ('STL', 'Southland'), ('TKI', 'Taranaki'), ('WKO', 'Waikato'), ('WGN', 'Wellington'), ('WTC', 'West Coast'), ('CIT', 'Chatham Islands Territory'), ('GIS', 'Gisborne District'), ('MBH', 'Marlborough District'), ('NSN', 'Nelson City'), ('TAS', 'Tasman District'))
]
NZ_STATES_DICT = CapsDict({state.abbr: state.name for state in NZ_STATES})
NZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NZ_STATES}

NI_STATES = [State(abbr, name) for abbr, name in 
    (('AN', 'Atlántico Norte'), ('AS', 'Atlántico Sur'), ('BO', 'Boaco'), ('CA', 'Carazo'), ('CI', 'Chinandega'), ('CO', 'Chontales'), ('ES', 'Estelí'), ('GR', 'Granada'), ('JI', 'Jinotega'), ('LE', 'León'), ('MD', 'Madriz'), ('MN', 'Managua'), ('MS', 'Masaya'), ('MT', 'Matagalpa'), ('NS', 'Nueva Segovia'), ('RI', 'Rivas'), ('SJ', 'Río San Juan'))
]
NI_STATES_DICT = CapsDict({state.abbr: state.name for state in NI_STATES})
NI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NI_STATES}

NE_STATES = [State(abbr, name) for abbr, name in 
    (('1', 'Agadez'), ('2', 'Diffa'), ('3', 'Dosso'), ('4', 'Maradi'), ('8', 'Niamey'), ('5', 'Tahoua'), ('6', 'Tillabéri'), ('7', 'Zinder'))
]
NE_STATES_DICT = CapsDict({state.abbr: state.name for state in NE_STATES})
NE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NE_STATES}

NG_STATES = [State(abbr, name) for abbr, name in 
    (('AB', 'Abia'), ('FC', 'Abuja Federal Capital Territory'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BY', 'Bayelsa'), ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NA', 'Nassarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara'))
]
NG_STATES_DICT = CapsDict({state.abbr: state.name for state in NG_STATES})
NG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NG_STATES}

NO_STATES = [State(abbr, name) for abbr, name in 
    (('02', 'Akershus'), ('09', 'Aust-Agder'), ('06', 'Buskerud'), ('20', 'Finnmark'), ('04', 'Hedmark'), ('12', 'Hordaland'), ('22', 'Jan Mayen'), ('15', 'Møre og Romsdal'), ('17', 'Nord-Trøndelag'), ('18', 'Nordland'), ('05', 'Oppland'), ('03', 'Oslo'), ('11', 'Rogaland'), ('14', 'Sogn og Fjordane'), ('21', 'Svalbard'), ('16', 'Sør-Trøndelag'), ('08', 'Telemark'), ('19', 'Troms'), ('10', 'Vest-Agder'), ('07', 'Vestfold'), ('01', 'Østfold'))
]
NO_STATES_DICT = CapsDict({state.abbr: state.name for state in NO_STATES})
NO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in NO_STATES}

OM_STATES = [State(abbr, name) for abbr, name in 
    (('DA', 'Ad Dākhilīyah'), ('BU', 'Al Buraymī'), ('BA', 'Al Bāţinah'), ('WU', 'Al Wusţá'), ('SH', 'Ash Sharqīyah'), ('ZA', 'Az̧ Z̧āhirah'), ('MA', 'Masqaţ'), ('MU', 'Musandam'), ('ZU', 'Z̧ufār'))
]
OM_STATES_DICT = CapsDict({state.abbr: state.name for state in OM_STATES})
OM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in OM_STATES}

PK_STATES = [State(abbr, name) for abbr, name in 
    (('JK', 'Azad Kashmir'), ('BA', 'Balochistan'), ('TA', 'Federally Administered Tribal Areas'), ('GB', 'Gilgit-Baltistan'), ('IS', 'Islamabad'), ('KP', 'Khyber Pakhtunkhwa'), ('PB', 'Punjab'), ('SD', 'Sindh'))
]
PK_STATES_DICT = CapsDict({state.abbr: state.name for state in PK_STATES})
PK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PK_STATES}

PW_STATES = [State(abbr, name) for abbr, name in 
    (('002', 'Aimeliik'), ('004', 'Airai'), ('010', 'Angaur'), ('050', 'Hatobohei'), ('100', 'Kayangel'), ('150', 'Koror'), ('212', 'Melekeok'), ('214', 'Ngaraard'), ('218', 'Ngarchelong'), ('222', 'Ngardmau'), ('224', 'Ngatpang'), ('226', 'Ngchesar'), ('227', 'Ngeremlengui'), ('228', 'Ngiwal'), ('350', 'Peleliu'), ('370', 'Sonsorol'))
]
PW_STATES_DICT = CapsDict({state.abbr: state.name for state in PW_STATES})
PW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PW_STATES}

PS_STATES = [State(abbr, name) for abbr, name in 
    (('BTH', 'Bethlehem'), ('DEB', 'Deir El Balah'), ('GZA', 'Gaza'), ('HBN', 'Hebron'), ('JEN', 'Jenin'), ('JRH', 'Jericho – Al Aghwar'), ('JEM', 'Jerusalem'), ('KYS', 'Khan Yunis'), ('NBS', 'Nablus'), ('NGZ', 'North Gaza'), ('QQA', 'Qalqilya'), ('RFH', 'Rafah'), ('RBH', 'Ramallah'), ('SLT', 'Salfit'), ('TBS', 'Tubas'), ('TKM', 'Tulkarm'))
]
PS_STATES_DICT = CapsDict({state.abbr: state.name for state in PS_STATES})
PS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PS_STATES}

PA_STATES = [State(abbr, name) for abbr, name in 
    (('1', 'Bocas del Toro'), ('4', 'Chiriquí'), ('2', 'Coclé'), ('3', 'Colón'), ('5', 'Darién'), ('EM', 'Emberá'), ('6', 'Herrera'), ('KY', 'Kuna Yala'), ('7', 'Los Santos'), ('NB', 'Ngöbe-Buglé'), ('8', 'Panamá'), ('10', 'Panamá Oeste'), ('9', 'Veraguas'))
]
PA_STATES_DICT = CapsDict({state.abbr: state.name for state in PA_STATES})
PA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PA_STATES}

PG_STATES = [State(abbr, name) for abbr, name in 
    (('NSB', 'Bougainville'), ('CPM', 'Central'), ('CPK', 'Chimbu'), ('EBR', 'East New Britain'), ('ESW', 'East Sepik'), ('EHG', 'Eastern Highlands'), ('EPW', 'Enga'), ('GPK', 'Gulf'), ('MPM', 'Madang'), ('MRL', 'Manus'), ('MBA', 'Milne Bay'), ('MPL', 'Morobe'), ('NCD', 'National Capital District'), ('NIK', 'New Ireland'), ('NPP', 'Northern'), ('SAN', 'Sandaun'), ('SHM', 'Southern Highlands'), ('WBK', 'West New Britain'), ('WPD', 'Western'), ('WHM', 'Western Highlands'))
]
PG_STATES_DICT = CapsDict({state.abbr: state.name for state in PG_STATES})
PG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PG_STATES}

PY_STATES = [State(abbr, name) for abbr, name in 
    (('16', 'Alto Paraguay'), ('10', 'Alto Paraná'), ('13', 'Amambay'), ('ASU', 'Asunción'), ('19', 'Boquerón'), ('5', 'Caaguazú'), ('6', 'Caazapá'), ('14', 'Canindeyú'), ('11', 'Central'), ('1', 'Concepción'), ('3', 'Cordillera'), ('4', 'Guairá'), ('7', 'Itapúa'), ('8', 'Misiones'), ('9', 'Paraguarí'), ('15', 'Presidente Hayes'), ('2', 'San Pedro'), ('12', 'Ñeembucú'))
]
PY_STATES_DICT = CapsDict({state.abbr: state.name for state in PY_STATES})
PY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PY_STATES}

PE_STATES = [State(abbr, name) for abbr, name in 
    (('AMA', 'Amazonas'), ('ANC', 'Ancash'), ('APU', 'Apurímac'), ('ARE', 'Arequipa'), ('AYA', 'Ayacucho'), ('CAJ', 'Cajamarca'), ('CUS', 'Cusco'), ('CAL', 'El Callao'), ('HUV', 'Huancavelica'), ('HUC', 'Huánuco'), ('ICA', 'Ica'), ('JUN', 'Junín'), ('LAL', 'La Libertad'), ('LAM', 'Lambayeque'), ('LIM', 'Lima'), ('LOR', 'Loreto'), ('MDD', 'Madre de Dios'), ('MOQ', 'Moquegua'), ('LMA', 'Municipalidad Metropolitana de Lima'), ('PAS', 'Pasco'), ('PIU', 'Piura'), ('PUN', 'Puno'), ('SAM', 'San Martín'), ('TAC', 'Tacna'), ('TUM', 'Tumbes'), ('UCA', 'Ucayali'))
]
PE_STATES_DICT = CapsDict({state.abbr: state.name for state in PE_STATES})
PE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PE_STATES}

PH_STATES = [State(abbr, name) for abbr, name in 
    (('14', 'Autonomous Region in Muslim Mindanao'), ('05', 'Bicol'), ('02', 'Cagayan Valley'), ('40', 'Calabarzon'), ('13', 'Caraga'), ('03', 'Central Luzon'), ('07', 'Central Visayas'), ('15', 'Cordillera Administrative Region'), ('11', 'Davao'), ('08', 'Eastern Visayas'), ('01', 'Ilocos'), ('41', 'Mimaropa'), ('00', 'National Capital Region'), ('10', 'Northern Mindanao'), ('12', 'Soccsksargen'), ('06', 'Western Visayas'), ('09', 'Zamboanga Peninsula'))
]
PH_STATES_DICT = CapsDict({state.abbr: state.name for state in PH_STATES})
PH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PH_STATES}

PL_STATES = [State(abbr, name) for abbr, name in 
    (('DS', 'Dolnośląskie'), ('KP', 'Kujawsko-pomorskie'), ('LU', 'Lubelskie'), ('LB', 'Lubuskie'), ('MZ', 'Mazowieckie'), ('MA', 'Małopolskie'), ('OP', 'Opolskie'), ('PK', 'Podkarpackie'), ('PD', 'Podlaskie'), ('PM', 'Pomorskie'), ('WN', 'Warmińsko-mazurskie'), ('WP', 'Wielkopolskie'), ('ZP', 'Zachodniopomorskie'), ('LD', 'Łódzkie'), ('SL', 'Śląskie'), ('SK', 'Świętokrzyskie'))
]
PL_STATES_DICT = CapsDict({state.abbr: state.name for state in PL_STATES})
PL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PL_STATES}

PT_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Aveiro'), ('02', 'Beja'), ('03', 'Braga'), ('04', 'Bragança'), ('05', 'Castelo Branco'), ('06', 'Coimbra'), ('08', 'Faro'), ('09', 'Guarda'), ('10', 'Leiria'), ('11', 'Lisboa'), ('12', 'Portalegre'), ('13', 'Porto'), ('30', 'Região Autónoma da Madeira'), ('20', 'Região Autónoma dos Açores'), ('14', 'Santarém'), ('15', 'Setúbal'), ('16', 'Viana do Castelo'), ('17', 'Vila Real'), ('18', 'Viseu'), ('07', 'Évora'))
]
PT_STATES_DICT = CapsDict({state.abbr: state.name for state in PT_STATES})
PT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in PT_STATES}

QA_STATES = [State(abbr, name) for abbr, name in 
    (('DA', 'Ad Dawḩah'), ('KH', 'Al Khawr wa adh Dhakhīrah'), ('WA', 'Al Wakrah'), ('RA', 'Ar Rayyān'), ('MS', 'Ash Shamāl'), ('ZA', 'Az̧ Za̧`āyin'), ('US', 'Umm Şalāl'))
]
QA_STATES_DICT = CapsDict({state.abbr: state.name for state in QA_STATES})
QA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in QA_STATES}

RO_STATES = [State(abbr, name) for abbr, name in 
    (('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Argeș'), ('BC', 'Bacău'), ('BH', 'Bihor'), ('BN', 'Bistrița-Năsăud'), ('BT', 'Botoșani'), ('BV', 'Brașov'), ('BR', 'Brăila'), ('B', 'București'), ('BZ', 'Buzău'), ('CS', 'Caraș-Severin'), ('CJ', 'Cluj'), ('CT', 'Constanța'), ('CV', 'Covasna'), ('CL', 'Călărași'), ('DJ', 'Dolj'), ('DB', 'Dâmbovița'), ('GL', 'Galați'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'), ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomița'), ('IS', 'Iași'), ('IF', 'Ilfov'), ('MM', 'Maramureș'), ('MH', 'Mehedinți'), ('MS', 'Mureș'), ('NT', 'Neamț'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('SJ', 'Sălaj'), ('TR', 'Teleorman'), ('TM', 'Timiș'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VN', 'Vrancea'), ('VL', 'Vâlcea'))
]
RO_STATES_DICT = CapsDict({state.abbr: state.name for state in RO_STATES})
RO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in RO_STATES}

RU_STATES = [State(abbr, name) for abbr, name in 
    (('AMU', "Amurskaya oblast'"), ('ARK', "Arkhangel'skaya oblast'"), ('AST', "Astrakhanskaya oblast'"), ('BEL', "Belgorodskaya oblast'"), ('BRY', "Bryanskaya oblast'"), ('CHE', "Chelyabinskaya oblast'"), ('IRK', "Irkutskaya oblast'"), ('IVA', "Ivanovskaya oblast'"), ('KGD', "Kaliningradskaya oblast'"), ('KLU', "Kaluzhskaya oblast'"), ('KEM', "Kemerovskaya oblast'"), ('KIR', "Kirovskaya oblast'"), ('KOS', "Kostromskaya oblast'"), ('KGN', "Kurganskaya oblast'"), ('KRS', "Kurskaya oblast'"), ('LEN', "Leningradskaya oblast'"), ('LIP', "Lipetskaya oblast'"), ('MAG', "Magadanskaya oblast'"), ('MOS', "Moskovskaya oblast'"), ('MUR', "Murmanskaya oblast'"), ('NIZ', "Nizhegorodskaya oblast'"), ('NGR', "Novgorodskaya oblast'"), ('NVS', "Novosibirskaya oblast'"), ('OMS', "Omskaya oblast'"), ('ORE', "Orenburgskaya oblast'"), ('ORL', "Orlovskaya oblast'"), ('PNZ', "Penzenskaya oblast'"), ('PSK', "Pskovskaya oblast'"), ('ROS', "Rostovskaya oblast'"), ('RYA', "Ryazanskaya oblast'"), ('SAK', "Sakhalinskaya oblast'"), ('SAM', "Samarskaya oblast'"), ('SAR', "Saratovskaya oblast'"), ('SMO', "Smolenskaya oblast'"), ('SVE', "Sverdlovskaya oblast'"), ('TAM', "Tambovskaya oblast'"), ('TOM', "Tomskaya oblast'"), ('TUL', "Tul'skaya oblast'"), ('TVE', "Tverskaya oblast'"), ('TYU', "Tyumenskaya oblast'"), ('ULY', "Ul'yanovskaya oblast'"), ('VLA', "Vladimirskaya oblast'"), ('VGG', "Volgogradskaya oblast'"), ('VLG', "Vologodskaya oblast'"), ('VOR', "Voronezhskaya oblast'"), ('YAR', "Yaroslavskaya oblast'"), ('ALT', 'Altayskiy kray'), ('KAM', 'Kamchatskiy kray'), ('KHA', 'Khabarovskiy kray'), ('KDA', 'Krasnodarskiy kray'), ('KYA', 'Krasnoyarskiy kray'), ('PER', 'Permskiy kray'), ('PRI', 'Primorskiy kray'), ('STA', "Stavropol'skiy kray"), ('ZAB', "Zabaykal'skiy kray"), ('MOW', 'Moskva'), ('SPE', 'Sankt-Peterburg'), ('CHU', 'Chukotskiy avtonomnyy okrug'), ('KHM', 'Khanty-Mansiyskiy avtonomnyy okrug-Yugra'), ('NEN', 'Nenetskiy avtonomnyy okrug'), ('YAN', 'Yamalo-Nenetskiy avtonomnyy okrug'), ('YEV', "Yevreyskaya avtonomnaya oblast'"), ('AD', 'Adygeya, Respublika'), ('AL', 'Altay, Respublika'), ('BA', 'Bashkortostan, Respublika'), ('BU', 'Buryatiya, Respublika'), ('CE', 'Chechenskaya Respublika'), ('CU', 'Chuvashskaya Respublika'), ('DA', 'Dagestan, Respublika'), ('IN', 'Ingushetiya, Respublika'), ('KB', 'Kabardino-Balkarskaya Respublika'), ('KL', 'Kalmykiya, Respublika'), ('KC', 'Karachayevo-Cherkesskaya Respublika'), ('KR', 'Kareliya, Respublika'), ('KK', 'Khakasiya, Respublika'), ('KO', 'Komi, Respublika'), ('ME', 'Mariy El, Respublika'), ('MO', 'Mordoviya, Respublika'), ('SA', 'Sakha, Respublika'), ('SE', 'Severnaya Osetiya-Alaniya, Respublika'), ('TA', 'Tatarstan, Respublika'), ('TY', 'Tyva, Respublika'), ('UD', 'Udmurtskaya Respublika'))
]
RU_STATES_DICT = CapsDict({state.abbr: state.name for state in RU_STATES})
RU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in RU_STATES}

RW_STATES = [State(abbr, name) for abbr, name in 
    (('02', 'Est'), ('03', 'Nord'), ('04', 'Ouest'), ('05', 'Sud'), ('01', 'Ville de Kigali'))
]
RW_STATES_DICT = CapsDict({state.abbr: state.name for state in RW_STATES})
RW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in RW_STATES}

SH_STATES = [State(abbr, name) for abbr, name in 
    (('AC', 'Ascension'), ('HL', 'Saint Helena'), ('TA', 'Tristan da Cunha'))
]
SH_STATES_DICT = CapsDict({state.abbr: state.name for state in SH_STATES})
SH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SH_STATES}

KN_STATES = [State(abbr, name) for abbr, name in 
    (('N', 'Nevis'), ('K', 'Saint Kitts'))
]
KN_STATES_DICT = CapsDict({state.abbr: state.name for state in KN_STATES})
KN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in KN_STATES}

LC_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Anse la Raye'), ('02', 'Castries'), ('03', 'Choiseul'), ('04', 'Dauphin'), ('05', 'Dennery'), ('06', 'Gros Islet'), ('07', 'Laborie'), ('08', 'Micoud'), ('09', 'Praslin'), ('10', 'Soufrière'), ('11', 'Vieux Fort'))
]
LC_STATES_DICT = CapsDict({state.abbr: state.name for state in LC_STATES})
LC_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LC_STATES}

VC_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Charlotte'), ('06', 'Grenadines'), ('02', 'Saint Andrew'), ('03', 'Saint David'), ('04', 'Saint George'), ('05', 'Saint Patrick'))
]
VC_STATES_DICT = CapsDict({state.abbr: state.name for state in VC_STATES})
VC_STATES_BY_NAME_DICT = {state.name.upper(): state for state in VC_STATES}

WS_STATES = [State(abbr, name) for abbr, name in 
    (('AA', "A'ana"), ('AL', 'Aiga-i-le-Tai'), ('AT', 'Atua'), ('FA', "Fa'asaleleaga"), ('GE', "Gaga'emauga"), ('GI', 'Gagaifomauga'), ('PA', 'Palauli'), ('SA', "Satupa'itea"), ('TU', 'Tuamasaga'), ('VF', "Va'a-o-Fonoti"), ('VS', 'Vaisigano'))
]
WS_STATES_DICT = CapsDict({state.abbr: state.name for state in WS_STATES})
WS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in WS_STATES}

SM_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Acquaviva'), ('06', 'Borgo Maggiore'), ('02', 'Chiesanuova'), ('03', 'Domagnano'), ('04', 'Faetano'), ('05', 'Fiorentino'), ('08', 'Montegiardino'), ('07', 'San Marino'), ('09', 'Serravalle'))
]
SM_STATES_DICT = CapsDict({state.abbr: state.name for state in SM_STATES})
SM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SM_STATES}

ST_STATES = [State(abbr, name) for abbr, name in 
    (('P', 'Príncipe'), ('S', 'São Tomé'))
]
ST_STATES_DICT = CapsDict({state.abbr: state.name for state in ST_STATES})
ST_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ST_STATES}

SA_STATES = [State(abbr, name) for abbr, name in 
    (('11', 'Al Bāḩah'), ('12', 'Al Jawf'), ('03', 'Al Madīnah'), ('05', 'Al Qaşīm'), ('08', 'Al Ḩudūd ash Shamālīyah'), ('01', 'Ar Riyāḑ'), ('04', 'Ash Sharqīyah'), ('09', 'Jīzān'), ('02', 'Makkah'), ('10', 'Najrān'), ('07', 'Tabūk'), ('14', 'ٰĀsīr'), ('06', "Ḩā'il"))
]
SA_STATES_DICT = CapsDict({state.abbr: state.name for state in SA_STATES})
SA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SA_STATES}

SN_STATES = [State(abbr, name) for abbr, name in 
    (('DK', 'Dakar'), ('DB', 'Diourbel'), ('FK', 'Fatick'), ('KA', 'Kaffrine'), ('KL', 'Kaolack'), ('KD', 'Kolda'), ('KE', 'Kédougou'), ('LG', 'Louga'), ('MT', 'Matam'), ('SL', 'Saint-Louis'), ('SE', 'Sédhiou'), ('TC', 'Tambacounda'), ('TH', 'Thiès'), ('ZG', 'Ziguinchor'))
]
SN_STATES_DICT = CapsDict({state.abbr: state.name for state in SN_STATES})
SN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SN_STATES}

RS_STATES = [State(abbr, name) for abbr, name in 
    (('KM', 'Kosovo-Metohija'), ('VO', 'Vojvodina'))
]
RS_STATES_DICT = CapsDict({state.abbr: state.name for state in RS_STATES})
RS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in RS_STATES}

SC_STATES = [State(abbr, name) for abbr, name in 
    (('02', 'Anse Boileau'), ('03', 'Anse Etoile'), ('05', 'Anse Royale'), ('01', 'Anse aux Pins'), ('04', 'Au Cap'), ('06', 'Baie Lazare'), ('07', 'Baie Sainte Anne'), ('08', 'Beau Vallon'), ('09', 'Bel Air'), ('10', 'Bel Ombre'), ('11', 'Cascade'), ('16', 'English River'), ('12', 'Glacis'), ('13', 'Grand Anse Mahe'), ('14', 'Grand Anse Praslin'), ('15', 'La Digue'), ('24', 'Les Mamelles'), ('17', 'Mont Buxton'), ('18', 'Mont Fleuri'), ('19', 'Plaisance'), ('20', 'Pointe Larue'), ('21', 'Port Glaud'), ('25', 'Roche Caiman'), ('22', 'Saint Louis'), ('23', 'Takamaka'))
]
SC_STATES_DICT = CapsDict({state.abbr: state.name for state in SC_STATES})
SC_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SC_STATES}

SL_STATES = [State(abbr, name) for abbr, name in 
    (('E', 'Eastern'), ('N', 'Northern'), ('S', 'Southern'), ('W', 'Western Area'))
]
SL_STATES_DICT = CapsDict({state.abbr: state.name for state in SL_STATES})
SL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SL_STATES}

SG_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Central Singapore'), ('02', 'North East'), ('03', 'North West'), ('04', 'South East'), ('05', 'South West'))
]
SG_STATES_DICT = CapsDict({state.abbr: state.name for state in SG_STATES})
SG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SG_STATES}

SK_STATES = [State(abbr, name) for abbr, name in 
    (('BC', 'Banskobystrický kraj'), ('BL', 'Bratislavský kraj'), ('KI', 'Košický kraj'), ('NI', 'Nitriansky kraj'), ('PV', 'Prešovský kraj'), ('TC', 'Trenčiansky kraj'), ('TA', 'Trnavský kraj'), ('ZI', 'Žilinský kraj'))
]
SK_STATES_DICT = CapsDict({state.abbr: state.name for state in SK_STATES})
SK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SK_STATES}

SI_STATES = [State(abbr, name) for abbr, name in 
    (('001', 'Ajdovščina'), ('195', 'Apače'), ('002', 'Beltinci'), ('148', 'Benedikt'), ('149', 'Bistrica ob Sotli'), ('003', 'Bled'), ('150', 'Bloke'), ('004', 'Bohinj'), ('005', 'Borovnica'), ('006', 'Bovec'), ('151', 'Braslovče'), ('007', 'Brda'), ('008', 'Brezovica'), ('009', 'Brežice'), ('152', 'Cankova'), ('011', 'Celje'), ('012', 'Cerklje na Gorenjskem'), ('013', 'Cerknica'), ('014', 'Cerkno'), ('153', 'Cerkvenjak'), ('196', 'Cirkulane'), ('018', 'Destrnik'), ('019', 'Divača'), ('154', 'Dobje'), ('020', 'Dobrepolje'), ('155', 'Dobrna'), ('021', 'Dobrova–Polhov Gradec'), ('156', 'Dobrovnik'), ('022', 'Dol pri Ljubljani'), ('157', 'Dolenjske Toplice'), ('023', 'Domžale'), ('024', 'Dornava'), ('025', 'Dravograd'), ('026', 'Duplek'), ('027', 'Gorenja vas–Poljane'), ('028', 'Gorišnica'), ('207', 'Gorje'), ('029', 'Gornja Radgona'), ('030', 'Gornji Grad'), ('031', 'Gornji Petrovci'), ('158', 'Grad'), ('032', 'Grosuplje'), ('159', 'Hajdina'), ('161', 'Hodoš'), ('162', 'Horjul'), ('160', 'Hoče–Slivnica'), ('034', 'Hrastnik'), ('035', 'Hrpelje-Kozina'), ('036', 'Idrija'), ('037', 'Ig'), ('038', 'Ilirska Bistrica'), ('039', 'Ivančna Gorica'), ('040', 'Izola'), ('041', 'Jesenice'), ('163', 'Jezersko'), ('042', 'Juršinci'), ('043', 'Kamnik'), ('044', 'Kanal'), ('045', 'Kidričevo'), ('046', 'Kobarid'), ('047', 'Kobilje'), ('049', 'Komen'), ('164', 'Komenda'), ('050', 'Koper'), ('197', 'Kosanjevica na Krki'), ('165', 'Kostel'), ('051', 'Kozje'), ('048', 'Kočevje'), ('052', 'Kranj'), ('053', 'Kranjska Gora'), ('166', 'Križevci'), ('054', 'Krško'), ('055', 'Kungota'), ('056', 'Kuzma'), ('057', 'Laško'), ('058', 'Lenart'), ('059', 'Lendava'), ('060', 'Litija'), ('061', 'Ljubljana'), ('062', 'Ljubno'), ('063', 'Ljutomer'), ('208', 'Log-Dragomer'), ('064', 'Logatec'), ('167', 'Lovrenc na Pohorju'), ('065', 'Loška Dolina'), ('066', 'Loški Potok'), ('068', 'Lukovica'), ('067', 'Luče'), ('069', 'Majšperk'), ('198', 'Makole'), ('070', 'Maribor'), ('168', 'Markovci'), ('071', 'Medvode'), ('072', 'Mengeš'), ('073', 'Metlika'), ('074', 'Mežica'), ('169', 'Miklavž na Dravskem Polju'), ('075', 'Miren–Kostanjevica'), ('170', 'Mirna Peč'), ('076', 'Mislinja'), ('199', 'Mokronog–Trebelno'), ('078', 'Moravske Toplice'), ('077', 'Moravče'), ('079', 'Mozirje'), ('080', 'Murska Sobota'), ('081', 'Muta'), ('082', 'Naklo'), ('083', 'Nazarje'), ('084', 'Nova Gorica'), ('085', 'Novo Mesto'), ('086', 'Odranci'), ('171', 'Oplotnica'), ('087', 'Ormož'), ('088', 'Osilnica'), ('089', 'Pesnica'), ('090', 'Piran'), ('091', 'Pivka'), ('172', 'Podlehnik'), ('093', 'Podvelka'), ('092', 'Podčetrtek'), ('200', 'Poljčane'), ('173', 'Polzela'), ('094', 'Postojna'), ('174', 'Prebold'), ('095', 'Preddvor'), ('175', 'Prevalje'), ('096', 'Ptuj'), ('097', 'Puconci'), ('100', 'Radenci'), ('099', 'Radeče'), ('101', 'Radlje ob Dravi'), ('102', 'Radovljica'), ('103', 'Ravne na Koroškem'), ('176', 'Razkrižje'), ('098', 'Rače–Fram'), ('201', 'Renče-Vogrsko'), ('209', 'Rečica ob Savinji'), ('104', 'Ribnica'), ('177', 'Ribnica na Pohorju'), ('107', 'Rogatec'), ('106', 'Rogaška Slatina'), ('105', 'Rogašovci'), ('108', 'Ruše'), ('178', 'Selnica ob Dravi'), ('109', 'Semič'), ('110', 'Sevnica'), ('111', 'Sežana'), ('112', 'Slovenj Gradec'), ('113', 'Slovenska Bistrica'), ('114', 'Slovenske Konjice'), ('179', 'Sodražica'), ('180', 'Solčava'), ('202', 'Središče ob Dravi'), ('115', 'Starše'), ('203', 'Straža'), ('181', 'Sveta Ana'), ('204', 'Sveta Trojica v Slovenskih Goricah'), ('182', 'Sveti Andraž v Slovenskih Goricah'), ('116', 'Sveti Jurij'), ('210', 'Sveti Jurij v Slovenskih Goricah'), ('205', 'Sveti Tomaž'), ('184', 'Tabor'), ('010', 'Tišina'), ('128', 'Tolmin'), ('129', 'Trbovlje'), ('130', 'Trebnje'), ('185', 'Trnovska Vas'), ('186', 'Trzin'), ('131', 'Tržič'), ('132', 'Turnišče'), ('133', 'Velenje'), ('187', 'Velika Polana'), ('134', 'Velike Lašče'), ('188', 'Veržej'), ('135', 'Videm'), ('136', 'Vipava'), ('137', 'Vitanje'), ('138', 'Vodice'), ('139', 'Vojnik'), ('189', 'Vransko'), ('140', 'Vrhnika'), ('141', 'Vuzenica'), ('142', 'Zagorje ob Savi'), ('143', 'Zavrč'), ('144', 'Zreče'), ('015', 'Črenšovci'), ('016', 'Črna na Koroškem'), ('017', 'Črnomelj'), ('033', 'Šalovci'), ('183', 'Šempeter–Vrtojba'), ('118', 'Šentilj'), ('119', 'Šentjernej'), ('120', 'Šentjur'), ('211', 'Šentrupert'), ('117', 'Šenčur'), ('121', 'Škocjan'), ('122', 'Škofja Loka'), ('123', 'Škofljica'), ('124', 'Šmarje pri Jelšah'), ('206', 'Šmarješke Toplice'), ('125', 'Šmartno ob Paki'), ('194', 'Šmartno pri Litiji'), ('126', 'Šoštanj'), ('127', 'Štore'), ('190', 'Žalec'), ('146', 'Železniki'), ('191', 'Žetale'), ('147', 'Žiri'), ('192', 'Žirovnica'), ('193', 'Žužemberk'))
]
SI_STATES_DICT = CapsDict({state.abbr: state.name for state in SI_STATES})
SI_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SI_STATES}

SB_STATES = [State(abbr, name) for abbr, name in 
    (('CT', 'Capital Territory'), ('CE', 'Central'), ('CH', 'Choiseul'), ('GU', 'Guadalcanal'), ('IS', 'Isabel'), ('MK', 'Makira-Ulawa'), ('ML', 'Malaita'), ('RB', 'Rennell and Bellona'), ('TE', 'Temotu'), ('WE', 'Western'))
]
SB_STATES_DICT = CapsDict({state.abbr: state.name for state in SB_STATES})
SB_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SB_STATES}

SO_STATES = [State(abbr, name) for abbr, name in 
    (('AW', 'Awdal'), ('BK', 'Bakool'), ('BN', 'Banaadir'), ('BR', 'Bari'), ('BY', 'Bay'), ('GA', 'Galguduud'), ('GE', 'Gedo'), ('HI', 'Hiiraan'), ('JD', 'Jubbada Dhexe'), ('JH', 'Jubbada Hoose'), ('MU', 'Mudug'), ('NU', 'Nugaal'), ('SA', 'Sanaag'), ('SD', 'Shabeellaha Dhexe'), ('SH', 'Shabeellaha Hoose'), ('SO', 'Sool'), ('TO', 'Togdheer'), ('WO', 'Woqooyi Galbeed'))
]
SO_STATES_DICT = CapsDict({state.abbr: state.name for state in SO_STATES})
SO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SO_STATES}

ZA_STATES = [State(abbr, name) for abbr, name in 
    (('EC', 'Eastern Cape'), ('FS', 'Free State'), ('GT', 'Gauteng'), ('NL', 'KwaZulu-Natal'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'), ('NW', 'North West'), ('NC', 'Northern Cape'), ('WC', 'Western Cape'))
]
ZA_STATES_DICT = CapsDict({state.abbr: state.name for state in ZA_STATES})
ZA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ZA_STATES}

SS_STATES = [State(abbr, name) for abbr, name in 
    (('EC', 'Central Equatoria'), ('EE', 'Eastern Equatoria'), ('JG', 'Jonglei'), ('LK', 'Lakes'), ('BN', 'Northern Bahr el Ghazal'), ('UY', 'Unity'), ('NU', 'Upper Nile'), ('WR', 'Warrap'), ('BW', 'Western Bahr el Ghazal'), ('EW', 'Western Equatoria'))
]
SS_STATES_DICT = CapsDict({state.abbr: state.name for state in SS_STATES})
SS_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SS_STATES}

ES_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'A Coruña'), ('AB', 'Albacete'), ('A', 'Alicante'), ('AL', 'Almería'), ('O', 'Asturias'), ('BA', 'Badajoz'), ('PM', 'Balears'), ('B', 'Barcelona'), ('BU', 'Burgos'), ('S', 'Cantabria'), ('CS', 'Castellón'), ('CR', 'Ciudad Real'), ('CU', 'Cuenca'), ('CC', 'Cáceres'), ('CA', 'Cádiz'), ('CO', 'Córdoba'), ('GI', 'Girona'), ('GR', 'Granada'), ('GU', 'Guadalajara'), ('SS', 'Guipúzcoa'), ('H', 'Huelva'), ('HU', 'Huesca'), ('J', 'Jaén'), ('LO', 'La Rioja'), ('GC', 'Las Palmas'), ('LE', 'León'), ('L', 'Lleida'), ('LU', 'Lugo'), ('M', 'Madrid'), ('MU', 'Murcia'), ('MA', 'Málaga'), ('NA', 'Navarra'), ('OR', 'Ourense'), ('P', 'Palencia'), ('PO', 'Pontevedra'), ('SA', 'Salamanca'), ('TF', 'Santa Cruz de Tenerife'), ('SG', 'Segovia'), ('SE', 'Sevilla'), ('SO', 'Soria'), ('T', 'Tarragona'), ('TE', 'Teruel'), ('TO', 'Toledo'), ('V', 'Valencia'), ('VA', 'Valladolid'), ('BI', 'Vizcaya'), ('ZA', 'Zamora'), ('Z', 'Zaragoza'), ('VI', 'Álava'), ('AV', 'Ávila'), ('CE', 'Ceuta'), ('ML', 'Melilla'), ('AN', 'Andalucía'), ('AR', 'Aragón'), ('AS', 'Asturias, Principado de'), ('CN', 'Canarias'), ('CB', 'Cantabria'), ('CL', 'Castilla y León'), ('CM', 'Castilla-La Mancha'), ('CT', 'Catalunya'), ('EX', 'Extremadura'), ('GA', 'Galicia'), ('IB', 'Illes Balears'), ('RI', 'La Rioja'), ('MD', 'Madrid, Comunidad de'), ('MC', 'Murcia, Región de'), ('NC', 'Navarra, Comunidad Foral de'), ('PV', 'País Vasco'), ('VC', 'Valenciana, Comunidad'))
]
ES_STATES_DICT = CapsDict({state.abbr: state.name for state in ES_STATES})
ES_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ES_STATES}

LK_STATES = [State(abbr, name) for abbr, name in 
    (('2', 'Central Province'), ('5', 'Eastern Province'), ('7', 'North Central Province'), ('6', 'North Western Province'), ('4', 'Northern Province'), ('9', 'Sabaragamuwa Province'), ('3', 'Southern Province'), ('8', 'Uva Province'), ('1', 'Western Province'))
]
LK_STATES_DICT = CapsDict({state.abbr: state.name for state in LK_STATES})
LK_STATES_BY_NAME_DICT = {state.name.upper(): state for state in LK_STATES}

SD_STATES = [State(abbr, name) for abbr, name in 
    (('RS', 'Al Baḩr al Aḩmar'), ('GZ', 'Al Jazīrah'), ('KH', 'Al Kharţūm'), ('GD', 'Al Qaḑārif'), ('NR', 'An Nīl'), ('NW', 'An Nīl al Abyaḑ'), ('NB', 'An Nīl al Azraq'), ('NO', 'Ash Shamālīyah'), ('DW', 'Gharb Dārfūr'), ('DS', 'Janūb Dārfūr'), ('KS', 'Janūb Kurdufān'), ('KA', 'Kassalā'), ('DN', 'Shamāl Dārfūr'), ('KN', 'Shamāl Kurdufān'), ('DE', 'Sharq Dārfūr'), ('SI', 'Sinnār'), ('DC', 'Zalingei'))
]
SD_STATES_DICT = CapsDict({state.abbr: state.name for state in SD_STATES})
SD_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SD_STATES}

SR_STATES = [State(abbr, name) for abbr, name in 
    (('BR', 'Brokopondo'), ('CM', 'Commewijne'), ('CR', 'Coronie'), ('MA', 'Marowijne'), ('NI', 'Nickerie'), ('PR', 'Para'), ('PM', 'Paramaribo'), ('SA', 'Saramacca'), ('SI', 'Sipaliwini'), ('WA', 'Wanica'))
]
SR_STATES_DICT = CapsDict({state.abbr: state.name for state in SR_STATES})
SR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SR_STATES}

SZ_STATES = [State(abbr, name) for abbr, name in 
    (('HH', 'Hhohho'), ('LU', 'Lubombo'), ('MA', 'Manzini'), ('SH', 'Shiselweni'))
]
SZ_STATES_DICT = CapsDict({state.abbr: state.name for state in SZ_STATES})
SZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SZ_STATES}

SE_STATES = [State(abbr, name) for abbr, name in 
    (('K', 'Blekinge län'), ('W', 'Dalarnas län'), ('I', 'Gotlands län'), ('X', 'Gävleborgs län'), ('N', 'Hallands län'), ('Z', 'Jämtlands län'), ('F', 'Jönköpings län'), ('H', 'Kalmar län'), ('G', 'Kronobergs län'), ('BD', 'Norrbottens län'), ('M', 'Skåne län'), ('AB', 'Stockholms län'), ('D', 'Södermanlands län'), ('C', 'Uppsala län'), ('S', 'Värmlands län'), ('AC', 'Västerbottens län'), ('Y', 'Västernorrlands län'), ('U', 'Västmanlands län'), ('O', 'Västra Götalands län'), ('T', 'Örebro län'), ('E', 'Östergötlands län'))
]
SE_STATES_DICT = CapsDict({state.abbr: state.name for state in SE_STATES})
SE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SE_STATES}

CH_STATES = [State(abbr, name) for abbr, name in 
    (('AG', 'Aargau'), ('AR', 'Appenzell Ausserrhoden'), ('AI', 'Appenzell Innerrhoden'), ('BL', 'Basel-Landschaft'), ('BS', 'Basel-Stadt'), ('BE', 'Bern'), ('FR', 'Fribourg'), ('GE', 'Genève'), ('GL', 'Glarus'), ('GR', 'Graubünden'), ('JU', 'Jura'), ('LU', 'Luzern'), ('NE', 'Neuchâtel'), ('NW', 'Nidwalden'), ('OW', 'Obwalden'), ('SG', 'Sankt Gallen'), ('SH', 'Schaffhausen'), ('SZ', 'Schwyz'), ('SO', 'Solothurn'), ('TG', 'Thurgau'), ('TI', 'Ticino'), ('UR', 'Uri'), ('VS', 'Valais'), ('VD', 'Vaud'), ('ZG', 'Zug'), ('ZH', 'Zürich'))
]
CH_STATES_DICT = CapsDict({state.abbr: state.name for state in CH_STATES})
CH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in CH_STATES}

SY_STATES = [State(abbr, name) for abbr, name in 
    (('LA', 'Al Lādhiqīyah'), ('QU', 'Al Qunayţirah'), ('HA', 'Al Ḩasakah'), ('RA', 'Ar Raqqah'), ('SU', "As Suwaydā'"), ('DR', 'Darٰā'), ('DY', 'Dayr az Zawr'), ('DI', 'Dimashq'), ('ID', 'Idlib'), ('RD', 'Rīf Dimashq'), ('TA', 'Ţarţūs'), ('HL', 'Ḩalab'), ('HM', 'Ḩamāh'), ('HI', 'Ḩimş'))
]
SY_STATES_DICT = CapsDict({state.abbr: state.name for state in SY_STATES})
SY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in SY_STATES}

TW_STATES = [State(abbr, name) for abbr, name in 
    (('CHA', 'Changhua'), ('CYQ', 'Chiayi'), ('CYI', 'Chiayi'), ('HSZ', 'Hsinchu'), ('HSQ', 'Hsinchu'), ('HUA', 'Hualien'), ('ILA', 'Ilan'), ('KHQ', 'Kaohsiung'), ('KHH', 'Kaohsiung'), ('KEE', 'Keelung'), ('MIA', 'Miaoli'), ('NAN', 'Nantou'), ('PEN', 'Penghu'), ('PIF', 'Pingtung'), ('TXG', 'Taichung'), ('TXQ', 'Taichung'), ('TNN', 'Tainan'), ('TNQ', 'Tainan'), ('TPE', 'Taipei'), ('TPQ', 'Taipei'), ('TTT', 'Taitung'), ('TAO', 'Taoyuan'), ('YUN', 'Yunlin'))
]
TW_STATES_DICT = CapsDict({state.abbr: state.name for state in TW_STATES})
TW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TW_STATES}

TJ_STATES = [State(abbr, name) for abbr, name in 
    (('DU', 'Dushanbe'), ('KT', 'Khatlon'), ('GB', 'Kŭhistoni Badakhshon'), ('SU', 'Sughd'))
]
TJ_STATES_DICT = CapsDict({state.abbr: state.name for state in TJ_STATES})
TJ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TJ_STATES}

TZ_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Arusha'), ('02', 'Dar es Salaam'), ('03', 'Dodoma'), ('04', 'Iringa'), ('05', 'Kagera'), ('06', 'Kaskazini Pemba'), ('07', 'Kaskazini Unguja'), ('08', 'Kigoma'), ('09', 'Kilimanjaro'), ('10', 'Kusini Pemba'), ('11', 'Kusini Unguja'), ('12', 'Lindi'), ('26', 'Manyara'), ('13', 'Mara'), ('14', 'Mbeya'), ('15', 'Mjini Magharibi'), ('16', 'Morogoro'), ('17', 'Mtwara'), ('18', 'Mwanza'), ('19', 'Pwani'), ('20', 'Rukwa'), ('21', 'Ruvuma'), ('22', 'Shinyanga'), ('23', 'Singida'), ('24', 'Tabora'), ('25', 'Tanga'))
]
TZ_STATES_DICT = CapsDict({state.abbr: state.name for state in TZ_STATES})
TZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TZ_STATES}

TH_STATES = [State(abbr, name) for abbr, name in 
    (('37', 'Amnat Charoen'), ('15', 'Ang Thong'), ('38', 'Bueng Kan'), ('31', 'Buri Ram'), ('24', 'Chachoengsao'), ('18', 'Chai Nat'), ('36', 'Chaiyaphum'), ('22', 'Chanthaburi'), ('50', 'Chiang Mai'), ('57', 'Chiang Rai'), ('20', 'Chon Buri'), ('86', 'Chumphon'), ('46', 'Kalasin'), ('62', 'Kamphaeng Phet'), ('71', 'Kanchanaburi'), ('40', 'Khon Kaen'), ('81', 'Krabi'), ('10', 'Krung Thep Maha Nakhon'), ('52', 'Lampang'), ('51', 'Lamphun'), ('42', 'Loei'), ('16', 'Lop Buri'), ('58', 'Mae Hong Son'), ('44', 'Maha Sarakham'), ('49', 'Mukdahan'), ('26', 'Nakhon Nayok'), ('73', 'Nakhon Pathom'), ('48', 'Nakhon Phanom'), ('30', 'Nakhon Ratchasima'), ('60', 'Nakhon Sawan'), ('80', 'Nakhon Si Thammarat'), ('55', 'Nan'), ('96', 'Narathiwat'), ('39', 'Nong Bua Lam Phu'), ('43', 'Nong Khai'), ('12', 'Nonthaburi'), ('13', 'Pathum Thani'), ('94', 'Pattani'), ('82', 'Phangnga'), ('93', 'Phatthalung'), ('S', 'Phatthaya'), ('56', 'Phayao'), ('67', 'Phetchabun'), ('76', 'Phetchaburi'), ('66', 'Phichit'), ('65', 'Phitsanulok'), ('14', 'Phra Nakhon Si Ayutthaya'), ('54', 'Phrae'), ('83', 'Phuket'), ('25', 'Prachin Buri'), ('77', 'Prachuap Khiri Khan'), ('85', 'Ranong'), ('70', 'Ratchaburi'), ('21', 'Rayong'), ('45', 'Roi Et'), ('27', 'Sa Kaeo'), ('47', 'Sakon Nakhon'), ('11', 'Samut Prakan'), ('74', 'Samut Sakhon'), ('75', 'Samut Songkhram'), ('19', 'Saraburi'), ('91', 'Satun'), ('33', 'Si Sa Ket'), ('17', 'Sing Buri'), ('90', 'Songkhla'), ('64', 'Sukhothai'), ('72', 'Suphan Buri'), ('84', 'Surat Thani'), ('32', 'Surin'), ('63', 'Tak'), ('92', 'Trang'), ('23', 'Trat'), ('34', 'Ubon Ratchathani'), ('41', 'Udon Thani'), ('61', 'Uthai Thani'), ('53', 'Uttaradit'), ('95', 'Yala'), ('35', 'Yasothon'))
]
TH_STATES_DICT = CapsDict({state.abbr: state.name for state in TH_STATES})
TH_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TH_STATES}

TL_STATES = [State(abbr, name) for abbr, name in 
    (('AL', 'Aileu'), ('AN', 'Ainaro'), ('BA', 'Baucau'), ('BO', 'Bobonaro'), ('CO', 'Cova Lima'), ('DI', 'Díli'), ('ER', 'Ermera'), ('LA', 'Lautem'), ('LI', 'Liquiça'), ('MT', 'Manatuto'), ('MF', 'Manufahi'), ('OE', 'Oecussi'), ('VI', 'Viqueque'))
]
TL_STATES_DICT = CapsDict({state.abbr: state.name for state in TL_STATES})
TL_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TL_STATES}

TG_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Centre'), ('K', 'Kara'), ('M', 'Maritime'), ('P', 'Plateaux'), ('S', 'Savannes'))
]
TG_STATES_DICT = CapsDict({state.abbr: state.name for state in TG_STATES})
TG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TG_STATES}

TO_STATES = [State(abbr, name) for abbr, name in 
    (('01', "'Eua"), ('02', "Ha'apai"), ('03', 'Niuas'), ('04', 'Tongatapu'), ('05', "Vava'u"))
]
TO_STATES_DICT = CapsDict({state.abbr: state.name for state in TO_STATES})
TO_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TO_STATES}

TT_STATES = [State(abbr, name) for abbr, name in 
    (('ARI', 'Arima'), ('CHA', 'Chaguanas'), ('CTT', 'Couva-Tabaquite-Talparo'), ('DMN', 'Diego Martin'), ('ETO', 'Eastern Tobago'), ('PED', 'Penal-Debe'), ('PTF', 'Point Fortin'), ('POS', 'Port of Spain'), ('PRT', 'Princes Town'), ('RCM', 'Rio Claro-Mayaro'), ('SFO', 'San Fernando'), ('SJL', 'San Juan-Laventille'), ('SGE', 'Sangre Grande'), ('SIP', 'Siparia'), ('TUP', 'Tunapuna-Piarco'), ('WTO', 'Western Tobago'))
]
TT_STATES_DICT = CapsDict({state.abbr: state.name for state in TT_STATES})
TT_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TT_STATES}

TN_STATES = [State(abbr, name) for abbr, name in 
    (('12', 'Ariana'), ('13', 'Ben Arous'), ('23', 'Bizerte'), ('31', 'Béja'), ('81', 'Gabès'), ('71', 'Gafsa'), ('32', 'Jendouba'), ('41', 'Kairouan'), ('42', 'Kasserine'), ('73', 'Kebili'), ('14', 'La Manouba'), ('33', 'Le Kef'), ('53', 'Mahdia'), ('82', 'Medenine'), ('52', 'Monastir'), ('21', 'Nabeul'), ('61', 'Sfax'), ('43', 'Sidi Bouzid'), ('34', 'Siliana'), ('51', 'Sousse'), ('83', 'Tataouine'), ('72', 'Tozeur'), ('11', 'Tunis'), ('22', 'Zaghouan'))
]
TN_STATES_DICT = CapsDict({state.abbr: state.name for state in TN_STATES})
TN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TN_STATES}

TR_STATES = [State(abbr, name) for abbr, name in 
    (('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('04', 'Ağrı'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkâri'), ('31', 'Hatay'), ('32', 'Isparta'), ('76', 'Iğdır'), ('46', 'Kahramanmaraş'), ('78', 'Karabük'), ('70', 'Karaman'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('79', 'Kilis'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('39', 'Kırklareli'), ('71', 'Kırıkkale'), ('40', 'Kırşehir'), ('44', 'Malatya'), ('45', 'Manisa'), ('47', 'Mardin'), ('33', 'Mersin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('34', 'İstanbul'), ('35', 'İzmir'), ('63', 'Şanlıurfa'), ('73', 'Şırnak'))
]
TR_STATES_DICT = CapsDict({state.abbr: state.name for state in TR_STATES})
TR_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TR_STATES}

TM_STATES = [State(abbr, name) for abbr, name in 
    (('A', 'Ahal'), ('S', 'Aşgabat'), ('B', 'Balkan'), ('D', 'Daşoguz'), ('L', 'Lebap'), ('M', 'Mary'))
]
TM_STATES_DICT = CapsDict({state.abbr: state.name for state in TM_STATES})
TM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TM_STATES}

TV_STATES = [State(abbr, name) for abbr, name in 
    (('FUN', 'Funafuti'), ('NMG', 'Nanumanga'), ('NMA', 'Nanumea'), ('NIT', 'Niutao'), ('NUI', 'Nui'), ('NKF', 'Nukufetau'), ('NKL', 'Nukulaelae'), ('VAI', 'Vaitupu'))
]
TV_STATES_DICT = CapsDict({state.abbr: state.name for state in TV_STATES})
TV_STATES_BY_NAME_DICT = {state.name.upper(): state for state in TV_STATES}

UG_STATES = [State(abbr, name) for abbr, name in 
    (('C', 'Central'), ('E', 'Eastern'), ('N', 'Northern'), ('W', 'Western'))
]
UG_STATES_DICT = CapsDict({state.abbr: state.name for state in UG_STATES})
UG_STATES_BY_NAME_DICT = {state.name.upper(): state for state in UG_STATES}

UA_STATES = [State(abbr, name) for abbr, name in 
    (('43', 'Avtonomna Respublika Krym'), ('71', "Cherkas'ka Oblast'"), ('74', "Chernihivs'ka Oblast'"), ('77', "Chernivets'ka Oblast'"), ('12', "Dnipropetrovs'ka Oblast'"), ('14', "Donets'ka Oblast'"), ('26', "Ivano-Frankivs'ka Oblast'"), ('63', "Kharkivs'ka Oblast'"), ('65', "Khersons'ka Oblast'"), ('68', "Khmel'nyts'ka Oblast'"), ('35', "Kirovohrads'ka Oblast'"), ('30', 'Kyïv'), ('32', "Kyïvs'ka Oblast'"), ('46', "L'vivs'ka Oblast'"), ('09', "Luhans'ka Oblast'"), ('48', "Mykolaïvs'ka Oblast'"), ('51', "Odes'ka Oblast'"), ('53', "Poltavs'ka Oblast'"), ('56', "Rivnens'ka Oblast'"), ('40', "Sevastopol'"), ('59', "Sums'ka Oblast'"), ('61', "Ternopil's'ka Oblast'"), ('05', "Vinnyts'ka Oblast'"), ('07', "Volyns'ka Oblast'"), ('21', "Zakarpats'ka Oblast'"), ('23', "Zaporiz'ka Oblast'"), ('18', "Zhytomyrs'ka Oblast'"))
]
UA_STATES_DICT = CapsDict({state.abbr: state.name for state in UA_STATES})
UA_STATES_BY_NAME_DICT = {state.name.upper(): state for state in UA_STATES}

AE_STATES = [State(abbr, name) for abbr, name in 
    (('AJ', "'Ajmān"), ('AZ', 'Abū Z̧aby'), ('FU', 'Al Fujayrah'), ('SH', 'Ash Shāriqah'), ('DU', 'Dubayy'), ('RK', "Ra's al Khaymah"), ('UQ', 'Umm al Qaywayn'))
]
AE_STATES_DICT = CapsDict({state.abbr: state.name for state in AE_STATES})
AE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in AE_STATES}

GB_STATES = [State(abbr, name) for abbr, name in 
    (('BDG', 'Barking and Dagenham'), ('BNE', 'Barnet'), ('BEX', 'Bexley'), ('BEN', 'Brent'), ('BRY', 'Bromley'), ('CMD', 'Camden'), ('CRY', 'Croydon'), ('EAL', 'Ealing'), ('ENF', 'Enfield'), ('GRE', 'Greenwich'), ('HCK', 'Hackney'), ('HMF', 'Hammersmith and Fulham'), ('HRY', 'Haringey'), ('HRW', 'Harrow'), ('HAV', 'Havering'), ('HIL', 'Hillingdon'), ('HNS', 'Hounslow'), ('ISL', 'Islington'), ('KEC', 'Kensington and Chelsea'), ('KTT', 'Kingston upon Thames'), ('LBH', 'Lambeth'), ('LEW', 'Lewisham'), ('MRT', 'Merton'), ('NWM', 'Newham'), ('RDB', 'Redbridge'), ('RIC', 'Richmond upon Thames'), ('SWK', 'Southwark'), ('STN', 'Sutton'), ('TWH', 'Tower Hamlets'), ('WFT', 'Waltham Forest'), ('WND', 'Wandsworth'), ('WSM', 'Westminster'), ('EAW', 'England and Wales'), ('GBN', 'Great Britain'), ('UKM', 'United Kingdom'), ('LND', 'London, City of'), ('ABE', 'Aberdeen City'), ('ABD', 'Aberdeenshire'), ('ANS', 'Angus'), ('AGB', 'Argyll and Bute'), ('CLK', 'Clackmannanshire'), ('DGY', 'Dumfries and Galloway'), ('DND', 'Dundee City'), ('EAY', 'East Ayrshire'), ('EDU', 'East Dunbartonshire'), ('ELN', 'East Lothian'), ('ERW', 'East Renfrewshire'), ('EDH', 'Edinburgh, City of'), ('ELS', 'Eilean Siar'), ('FAL', 'Falkirk'), ('FIF', 'Fife'), ('GLG', 'Glasgow City'), ('HLD', 'Highland'), ('IVC', 'Inverclyde'), ('MLN', 'Midlothian'), ('MRY', 'Moray'), ('NAY', 'North Ayrshire'), ('NLK', 'North Lanarkshire'), ('ORK', 'Orkney Islands'), ('PKN', 'Perth and Kinross'), ('RFW', 'Renfrewshire'), ('SCB', 'Scottish Borders, The'), ('ZET', 'Shetland Islands'), ('SAY', 'South Ayrshire'), ('SLK', 'South Lanarkshire'), ('STG', 'Stirling'), ('WDU', 'West Dunbartonshire'), ('WLN', 'West Lothian'), ('ENG', 'England'), ('SCT', 'Scotland'), ('WLS', 'Wales'), ('ANT', 'Antrim'), ('ARD', 'Ards'), ('ARM', 'Armagh'), ('BLA', 'Ballymena'), ('BLY', 'Ballymoney'), ('BNB', 'Banbridge'), ('BFS', 'Belfast'), ('CKF', 'Carrickfergus'), ('CSR', 'Castlereagh'), ('CLR', 'Coleraine'), ('CKT', 'Cookstown'), ('CGV', 'Craigavon'), ('DRY', 'Derry'), ('DOW', 'Down'), ('DGN', 'Dungannon and South Tyrone'), ('FER', 'Fermanagh'), ('LRN', 'Larne'), ('LMV', 'Limavady'), ('LSB', 'Lisburn'), ('MFT', 'Magherafelt'), ('MYL', 'Moyle'), ('NYM', 'Newry and Mourne District'), ('NTA', 'Newtownabbey'), ('NDN', 'North Down'), ('OMH', 'Omagh'), ('STB', 'Strabane'), ('BNS', 'Barnsley'), ('BIR', 'Birmingham'), ('BOL', 'Bolton'), ('BRD', 'Bradford'), ('BUR', 'Bury'), ('CLD', 'Calderdale'), ('COV', 'Coventry'), ('DNC', 'Doncaster'), ('DUD', 'Dudley'), ('GAT', 'Gateshead'), ('KIR', 'Kirklees'), ('KWL', 'Knowsley'), ('LDS', 'Leeds'), ('LIV', 'Liverpool'), ('MAN', 'Manchester'), ('NET', 'Newcastle upon Tyne'), ('NTY', 'North Tyneside'), ('OLD', 'Oldham'), ('RCH', 'Rochdale'), ('ROT', 'Rotherham'), ('SLF', 'Salford'), ('SAW', 'Sandwell'), ('SFT', 'Sefton'), ('SHF', 'Sheffield'), ('SOL', 'Solihull'), ('STY', 'South Tyneside'), ('SHN', 'St. Helens'), ('SKP', 'Stockport'), ('SND', 'Sunderland'), ('TAM', 'Tameside'), ('TRF', 'Trafford'), ('WKF', 'Wakefield'), ('WLL', 'Walsall'), ('WGN', 'Wigan'), ('WRL', 'Wirral'), ('WLV', 'Wolverhampton'), ('NIR', 'Northern Ireland'), ('BKM', 'Buckinghamshire'), ('CAM', 'Cambridgeshire'), ('CMA', 'Cumbria'), ('DBY', 'Derbyshire'), ('DEV', 'Devon'), ('DOR', 'Dorset'), ('ESX', 'East Sussex'), ('ESS', 'Essex'), ('GLS', 'Gloucestershire'), ('HAM', 'Hampshire'), ('HRT', 'Hertfordshire'), ('KEN', 'Kent'), ('LAN', 'Lancashire'), ('LEC', 'Leicestershire'), ('LIN', 'Lincolnshire'), ('NFK', 'Norfolk'), ('NYK', 'North Yorkshire'), ('NTH', 'Northamptonshire'), ('NTT', 'Nottinghamshire'), ('OXF', 'Oxfordshire'), ('SOM', 'Somerset'), ('STS', 'Staffordshire'), ('SFK', 'Suffolk'), ('SRY', 'Surrey'), ('WAR', 'Warwickshire'), ('WSX', 'West Sussex'), ('WOR', 'Worcestershire'), ('BAS', 'Bath and North East Somerset'), ('BDF', 'Bedford'), ('BBD', 'Blackburn with Darwen'), ('BPL', 'Blackpool'), ('BGW', 'Blaenau Gwent'), ('BMH', 'Bournemouth'), ('BRC', 'Bracknell Forest'), ('BGE', 'Bridgend'), ('BNH', 'Brighton and Hove'), ('BST', 'Bristol, City of'), ('CAY', 'Caerphilly'), ('CRF', 'Cardiff'), ('CMN', 'Carmarthenshire'), ('CBF', 'Central Bedfordshire'), ('CGN', 'Ceredigion'), ('CHE', 'Cheshire East'), ('CHW', 'Cheshire West and Chester'), ('CWY', 'Conwy'), ('CON', 'Cornwall'), ('DAL', 'Darlington'), ('DEN', 'Denbighshire'), ('DER', 'Derby'), ('DUR', 'Durham, County'), ('ERY', 'East Riding of Yorkshire'), ('FLN', 'Flintshire'), ('GWN', 'Gwynedd'), ('HAL', 'Halton'), ('HPL', 'Hartlepool'), ('HEF', 'Herefordshire'), ('AGY', 'Isle of Anglesey'), ('IOW', 'Isle of Wight'), ('IOS', 'Isles of Scilly'), ('KHL', 'Kingston upon Hull'), ('LCE', 'Leicester'), ('LUT', 'Luton'), ('MDW', 'Medway'), ('MTY', 'Merthyr Tydfil'), ('MDB', 'Middlesbrough'), ('MIK', 'Milton Keynes'), ('MON', 'Monmouthshire'), ('NTL', 'Neath Port Talbot'), ('NWP', 'Newport'), ('NEL', 'North East Lincolnshire'), ('NLN', 'North Lincolnshire'), ('NSM', 'North Somerset'), ('NBL', 'Northumberland'), ('NGM', 'Nottingham'), ('PEM', 'Pembrokeshire'), ('PTE', 'Peterborough'), ('PLY', 'Plymouth'), ('POL', 'Poole'), ('POR', 'Portsmouth'), ('POW', 'Powys'), ('RDG', 'Reading'), ('RCC', 'Redcar and Cleveland'), ('RCT', 'Rhondda, Cynon, Taff'), ('RUT', 'Rutland'), ('SHR', 'Shropshire'), ('SLG', 'Slough'), ('SGC', 'South Gloucestershire'), ('STH', 'Southampton'), ('SOS', 'Southend-on-Sea'), ('STT', 'Stockton-on-Tees'), ('STE', 'Stoke-on-Trent'), ('SWA', 'Swansea'), ('SWD', 'Swindon'), ('TFW', 'Telford and Wrekin'), ('THR', 'Thurrock'), ('TOB', 'Torbay'), ('TOF', 'Torfaen'), ('VGL', 'Vale of Glamorgan, The'), ('WRT', 'Warrington'), ('WBK', 'West Berkshire'), ('WIL', 'Wiltshire'), ('WNM', 'Windsor and Maidenhead'), ('WOK', 'Wokingham'), ('WRX', 'Wrexham'), ('YOR', 'York'))
]
GB_STATES_DICT = CapsDict({state.abbr: state.name for state in GB_STATES})
GB_STATES_BY_NAME_DICT = {state.name.upper(): state for state in GB_STATES}

US_STATES = [State(abbr, name) for abbr, name in 
    (('DC', 'District of Columbia'), ('AS', 'American Samoa'), ('GU', 'Guam'), ('MP', 'Northern Mariana Islands'), ('PR', 'Puerto Rico'), ('UM', 'United States Minor Outlying Islands'), ('VI', 'Virgin Islands, U.S.'), ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))
]
US_STATES_DICT = CapsDict({state.abbr: state.name for state in US_STATES})
US_STATES_BY_NAME_DICT = {state.name.upper(): state for state in US_STATES}

UM_STATES = [State(abbr, name) for abbr, name in 
    (('81', 'Baker Island'), ('84', 'Howland Island'), ('86', 'Jarvis Island'), ('67', 'Johnston Atoll'), ('89', 'Kingman Reef'), ('71', 'Midway Islands'), ('76', 'Navassa Island'), ('95', 'Palmyra Atoll'), ('79', 'Wake Island'))
]
UM_STATES_DICT = CapsDict({state.abbr: state.name for state in UM_STATES})
UM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in UM_STATES}

UY_STATES = [State(abbr, name) for abbr, name in 
    (('AR', 'Artigas'), ('CA', 'Canelones'), ('CL', 'Cerro Largo'), ('CO', 'Colonia'), ('DU', 'Durazno'), ('FS', 'Flores'), ('FD', 'Florida'), ('LA', 'Lavalleja'), ('MA', 'Maldonado'), ('MO', 'Montevideo'), ('PA', 'Paysandú'), ('RV', 'Rivera'), ('RO', 'Rocha'), ('RN', 'Río Negro'), ('SA', 'Salto'), ('SJ', 'San José'), ('SO', 'Soriano'), ('TA', 'Tacuarembó'), ('TT', 'Treinta y Tres'))
]
UY_STATES_DICT = CapsDict({state.abbr: state.name for state in UY_STATES})
UY_STATES_BY_NAME_DICT = {state.name.upper(): state for state in UY_STATES}

UZ_STATES = [State(abbr, name) for abbr, name in 
    (('AN', 'Andijon'), ('BU', 'Buxoro'), ('FA', 'Farg‘ona'), ('JI', 'Jizzax'), ('NG', 'Namangan'), ('NW', 'Navoiy'), ('QA', 'Qashqadaryo'), ('QR', 'Qoraqalpog‘iston Respublikasi'), ('SA', 'Samarqand'), ('SI', 'Sirdaryo'), ('SU', 'Surxondaryo'), ('TO', 'Toshkent'), ('TK', 'Toshkent'), ('XO', 'Xorazm'))
]
UZ_STATES_DICT = CapsDict({state.abbr: state.name for state in UZ_STATES})
UZ_STATES_BY_NAME_DICT = {state.name.upper(): state for state in UZ_STATES}

VU_STATES = [State(abbr, name) for abbr, name in 
    (('MAP', 'Malampa'), ('PAM', 'Pénama'), ('SAM', 'Sanma'), ('SEE', 'Shéfa'), ('TAE', 'Taféa'), ('TOB', 'Torba'))
]
VU_STATES_DICT = CapsDict({state.abbr: state.name for state in VU_STATES})
VU_STATES_BY_NAME_DICT = {state.name.upper(): state for state in VU_STATES}

VE_STATES = [State(abbr, name) for abbr, name in 
    (('Z', 'Amazonas'), ('B', 'Anzoátegui'), ('C', 'Apure'), ('D', 'Aragua'), ('E', 'Barinas'), ('F', 'Bolívar'), ('G', 'Carabobo'), ('H', 'Cojedes'), ('Y', 'Delta Amacuro'), ('W', 'Dependencias Federales'), ('A', 'Distrito Capital'), ('I', 'Falcón'), ('J', 'Guárico'), ('K', 'Lara'), ('M', 'Miranda'), ('N', 'Monagas'), ('L', 'Mérida'), ('O', 'Nueva Esparta'), ('P', 'Portuguesa'), ('R', 'Sucre'), ('T', 'Trujillo'), ('S', 'Táchira'), ('X', 'Vargas'), ('U', 'Yaracuy'), ('V', 'Zulia'))
]
VE_STATES_DICT = CapsDict({state.abbr: state.name for state in VE_STATES})
VE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in VE_STATES}

VN_STATES = [State(abbr, name) for abbr, name in 
    (('44', 'An Giang'), ('43', 'Bà Rịa–Vũng Tàu'), ('57', 'Bình Dương'), ('58', 'Bình Phước'), ('40', 'Bình Thuận'), ('31', 'Bình Định'), ('55', 'Bạc Liêu'), ('54', 'Bắc Giang'), ('53', 'Bắc Kạn'), ('56', 'Bắc Ninh'), ('50', 'Bến Tre'), ('04', 'Cao Bằng'), ('59', 'Cà Mau'), ('CT', 'Cần Thơ'), ('30', 'Gia Lai'), ('03', 'Hà Giang'), ('63', 'Hà Nam'), ('HN', 'Hà Nội'), ('15', 'Hà Tây'), ('23', 'Hà Tĩnh'), ('14', 'Hòa Bình'), ('66', 'Hưng Yên'), ('61', 'Hải Dương'), ('HP', 'Hải Phòng'), ('73', 'Hậu Giang'), ('SG', 'Hồ Chí Minh'), ('34', 'Khánh Hòa'), ('47', 'Kiên Giang'), ('28', 'Kon Tum'), ('01', 'Lai Châu'), ('41', 'Long An'), ('02', 'Lào Cai'), ('35', 'Lâm Đồng'), ('09', 'Lạng Sơn'), ('67', 'Nam Định'), ('22', 'Nghệ An'), ('18', 'Ninh Bình'), ('36', 'Ninh Thuận'), ('68', 'Phú Thọ'), ('32', 'Phú Yên'), ('24', 'Quảng Bình'), ('27', 'Quảng Nam'), ('29', 'Quảng Ngãi'), ('13', 'Quảng Ninh'), ('25', 'Quảng Trị'), ('52', 'Sóc Trăng'), ('05', 'Sơn La'), ('21', 'Thanh Hóa'), ('20', 'Thái Bình'), ('69', 'Thái Nguyên'), ('26', 'Thừa Thiên–Huế'), ('46', 'Tiền Giang'), ('51', 'Trà Vinh'), ('07', 'Tuyên Quang'), ('37', 'Tây Ninh'), ('49', 'Vĩnh Long'), ('70', 'Vĩnh Phúc'), ('06', 'Yên Bái'), ('71', 'Điện Biên'), ('DN', 'Đà Nẵng'), ('33', 'Đắk Lắk'), ('72', 'Đắk Nông'), ('39', 'Đồng Nai'), ('45', 'Đồng Tháp'))
]
VN_STATES_DICT = CapsDict({state.abbr: state.name for state in VN_STATES})
VN_STATES_BY_NAME_DICT = {state.name.upper(): state for state in VN_STATES}

YE_STATES = [State(abbr, name) for abbr, name in 
    (('AD', "'Adan"), ('AM', "'Amrān"), ('AB', 'Abyān'), ('BA', "Al Bayḑā'"), ('JA', 'Al Jawf'), ('MR', 'Al Mahrah'), ('MW', 'Al Maḩwīt'), ('HU', 'Al Ḩudaydah'), ('DA', "Aḑ Ḑāli'"), ('DH', 'Dhamār'), ('IB', 'Ibb'), ('LA', 'Laḩij'), ('MA', "Ma'rib"), ('RA', 'Raymah'), ('SH', 'Shabwah'), ('TA', 'Tā‘izz'), ('SA', "Şan‘ā'"), ('SN', "Şan‘ā'"), ('SD', 'Şā‘dah'), ('HJ', 'Ḩajjah'), ('HD', 'Ḩaḑramawt'))
]
YE_STATES_DICT = CapsDict({state.abbr: state.name for state in YE_STATES})
YE_STATES_BY_NAME_DICT = {state.name.upper(): state for state in YE_STATES}

ZM_STATES = [State(abbr, name) for abbr, name in 
    (('02', 'Central'), ('08', 'Copperbelt'), ('03', 'Eastern'), ('04', 'Luapula'), ('09', 'Lusaka'), ('06', 'North-Western'), ('05', 'Northern'), ('07', 'Southern'), ('01', 'Western'))
]
ZM_STATES_DICT = CapsDict({state.abbr: state.name for state in ZM_STATES})
ZM_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ZM_STATES}

ZW_STATES = [State(abbr, name) for abbr, name in 
    (('BU', 'Bulawayo'), ('HA', 'Harare'), ('MA', 'Manicaland'), ('MC', 'Mashonaland Central'), ('ME', 'Mashonaland East'), ('MW', 'Mashonaland West'), ('MV', 'Masvingo'), ('MN', 'Matabeleland North'), ('MS', 'Matabeleland South'), ('MI', 'Midlands'))
]
ZW_STATES_DICT = CapsDict({state.abbr: state.name for state in ZW_STATES})
ZW_STATES_BY_NAME_DICT = {state.name.upper(): state for state in ZW_STATES}

STATES_BY_COUNTRY = CapsDict(
    {'AF': AF_STATES, 'AL': AL_STATES, 'DZ': DZ_STATES, 'AD': AD_STATES, 'AO': AO_STATES, 'AG': AG_STATES, 'AR': AR_STATES, 'AM': AM_STATES, 'AU': AU_STATES, 'AT': AT_STATES, 'AZ': AZ_STATES, 'BS': BS_STATES, 'BH': BH_STATES, 'BD': BD_STATES, 'BB': BB_STATES, 'BY': BY_STATES, 'BE': BE_STATES, 'BZ': BZ_STATES, 'BJ': BJ_STATES, 'BT': BT_STATES, 'BO': BO_STATES, 'BA': BA_STATES, 'BW': BW_STATES, 'BR': BR_STATES, 'BN': BN_STATES, 'BG': BG_STATES, 'BF': BF_STATES, 'BI': BI_STATES, 'KH': KH_STATES, 'CM': CM_STATES, 'CA': CA_STATES, 'CV': CV_STATES, 'CF': CF_STATES, 'TD': TD_STATES, 'CL': CL_STATES, 'CN': CN_STATES, 'CO': CO_STATES, 'KM': KM_STATES, 'CG': CG_STATES, 'CD': CD_STATES, 'CR': CR_STATES, 'CI': CI_STATES, 'HR': HR_STATES, 'CU': CU_STATES, 'CY': CY_STATES, 'CZ': CZ_STATES, 'DK': DK_STATES, 'DJ': DJ_STATES, 'DM': DM_STATES, 'DO': DO_STATES, 'EC': EC_STATES, 'EG': EG_STATES, 'SV': SV_STATES, 'GQ': GQ_STATES, 'ER': ER_STATES, 'EE': EE_STATES, 'ET': ET_STATES, 'FJ': FJ_STATES, 'FI': FI_STATES, 'FR': FR_STATES, 'GA': GA_STATES, 'GM': GM_STATES, 'GE': GE_STATES, 'DE': DE_STATES, 'GH': GH_STATES, 'GR': GR_STATES, 'GL': GL_STATES, 'GD': GD_STATES, 'GT': GT_STATES, 'GN': GN_STATES, 'GW': GW_STATES, 'GY': GY_STATES, 'HT': HT_STATES, 'HN': HN_STATES, 'HK': HK_STATES, 'HU': HU_STATES, 'IS': IS_STATES, 'IN': IN_STATES, 'ID': ID_STATES, 'IR': IR_STATES, 'IQ': IQ_STATES, 'IE': IE_STATES, 'IL': IL_STATES, 'IT': IT_STATES, 'JM': JM_STATES, 'JP': JP_STATES, 'JO': JO_STATES, 'KZ': KZ_STATES, 'KE': KE_STATES, 'KI': KI_STATES, 'KP': KP_STATES, 'KR': KR_STATES, 'KW': KW_STATES, 'KG': KG_STATES, 'LA': LA_STATES, 'LV': LV_STATES, 'LB': LB_STATES, 'LS': LS_STATES, 'LR': LR_STATES, 'LY': LY_STATES, 'LI': LI_STATES, 'LT': LT_STATES, 'LU': LU_STATES, 'MK': MK_STATES, 'MG': MG_STATES, 'MW': MW_STATES, 'MY': MY_STATES, 'MV': MV_STATES, 'ML': ML_STATES, 'MT': MT_STATES, 'MH': MH_STATES, 'MR': MR_STATES, 'MU': MU_STATES, 'MX': MX_STATES, 'FM': FM_STATES, 'MD': MD_STATES, 'MC': MC_STATES, 'MN': MN_STATES, 'ME': ME_STATES, 'MA': MA_STATES, 'MZ': MZ_STATES, 'MM': MM_STATES, 'NA': NA_STATES, 'NR': NR_STATES, 'NP': NP_STATES, 'NL': NL_STATES, 'NZ': NZ_STATES, 'NI': NI_STATES, 'NE': NE_STATES, 'NG': NG_STATES, 'NO': NO_STATES, 'OM': OM_STATES, 'PK': PK_STATES, 'PW': PW_STATES, 'PS': PS_STATES, 'PA': PA_STATES, 'PG': PG_STATES, 'PY': PY_STATES, 'PE': PE_STATES, 'PH': PH_STATES, 'PL': PL_STATES, 'PT': PT_STATES, 'QA': QA_STATES, 'RO': RO_STATES, 'RU': RU_STATES, 'RW': RW_STATES, 'SH': SH_STATES, 'KN': KN_STATES, 'LC': LC_STATES, 'VC': VC_STATES, 'WS': WS_STATES, 'SM': SM_STATES, 'ST': ST_STATES, 'SA': SA_STATES, 'SN': SN_STATES, 'RS': RS_STATES, 'SC': SC_STATES, 'SL': SL_STATES, 'SG': SG_STATES, 'SK': SK_STATES, 'SI': SI_STATES, 'SB': SB_STATES, 'SO': SO_STATES, 'ZA': ZA_STATES, 'SS': SS_STATES, 'ES': ES_STATES, 'LK': LK_STATES, 'SD': SD_STATES, 'SR': SR_STATES, 'SZ': SZ_STATES, 'SE': SE_STATES, 'CH': CH_STATES, 'SY': SY_STATES, 'TW': TW_STATES, 'TJ': TJ_STATES, 'TZ': TZ_STATES, 'TH': TH_STATES, 'TL': TL_STATES, 'TG': TG_STATES, 'TO': TO_STATES, 'TT': TT_STATES, 'TN': TN_STATES, 'TR': TR_STATES, 'TM': TM_STATES, 'TV': TV_STATES, 'UG': UG_STATES, 'UA': UA_STATES, 'AE': AE_STATES, 'GB': GB_STATES, 'US': US_STATES, 'UM': UM_STATES, 'UY': UY_STATES, 'UZ': UZ_STATES, 'VU': VU_STATES, 'VE': VE_STATES, 'VN': VN_STATES, 'YE': YE_STATES, 'ZM': ZM_STATES, 'ZW': ZW_STATES}
)
