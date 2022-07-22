# IFPNI-api
I want to write a PYTHON script which can set up URL and more respond deponds on speical factors.

IFPNI (The INTERNATIONAL FOSSIL PLANT NAMES INDEX) mainly contains plant fossil names from EUROPE. There are more than 60,000 special names included in IFPNI, as well as suprageneric names(1996), generic names(17262), infrageneric names(422) and infraspecies names(2120).

Because there is not an offical API to search or collect FOSSIL NAMES from IFPNI, so i want to do this. And more, IFPNI just one of serval fossil databases, with this api, i could integrate databases and do search name in a single APP or GUI, which may be written by tkinter.

This api just have one CLASS, IFPNI, which requires eight paras: source, name, author, rankID, originalSpelling, yearFrom, yearTo, paleoID
I will introduce these paras:

source: this para is essential, you can choose one from suprageneric, generic, infrageneric, species, infraspecies
        I recommand to use species
name: this para is essential, you can entry the fossil name that you want to search.
author: this para is optinal, you can entry author's name who named the fossil if you want.
rankID: this para is optinal and deponds on source. Here i give a list that contains rankID details.
        you can entry a list that contains rankID nums, like [2, 3, 5].
        'suprageneric': {'Regnum': 2, 'Subregnum': 3, 'Phylum': 5, 'Subphylum': 6, 'Superphylum': 7,
                             'Class': 9, 'Subclass': 10, 'Superclass': 11, 'Infraclass': 12, 'Order': 66,
                             'Superorder': 14, 'Suborder': 15, 'Infraorder': 16, 'Family': 18,
                             'Superfamily': 19,
                             'Subfamily': 20, 'Infrafamily': 21, 'Tribe': 23, 'Supertribe': 24,
                             'Supersubtribe': 25,
                             'Subtribe': 26, 'Infratribe': 27, 'Turma': 67, 'Anteturma': 29,
                             'Supersubturma': 30,
                             'Subturma': 31, 'Infraturma': 32, 'Unranked': 59},
            'generic': {'Genus': 68, 'Supergenus': 43, 'Group': 69, 'Subgroup': 45, 'Unranked': 56},
            'infrageneric': {'Genus': 70, 'Infragenus': 47, 'Subgenus': 48, 'Section': 49, 'Subsection': 50,
                             'Supersection': 51,
                             'Series': 52, 'Subseries': 53, 'Superseries': 54, 'Unranked': 55},
            'species': {'Species': 33, 'Superspecies': 34, 'Unranked': 58},
            'infraspecies': {'Supervarietas': 36, 'Varietas': 37, 'Subvarietas': 38, 'Forma': 39, 'Subforma': 40,
                             'Infraspecies': 41,
                             'Unranked': 57}}
originalSpelling: this para is optinal, you cal entry the original spelling of fossil that you want to search.
yearFrom: this para is optinal, you can entry the year that you want to search from.
yearTo: this para is optinal, you can entry the year that you want to search to.
paleoID:  this para is optinal and works when source is species or infraspecies. Here i give a list that contains paleoID details.
       ifpni_paleoID = {'Africa': 1, 'Africa (East)': 2, 'Africa (Equatorial)': 3, 'Africa (North)': 4,
                         'Africa (South)': 5,
                         'Africa (West)': 6, 'Altaida (Altaides)': 7, 'Altaj': 8, 'America': 122,
                         'America (Caribbean)': 9,
                         'America (North)': 10, 'America (North - Greenland)': 104, 'America (South)': 11,
                         'Anatolia': 12,
                         'Angarida': 13, 'Angarida (Mongolia)': 136, 'Antarctica': 14, 'Arctic': 15,
                         'Australia': 16,
                         'Australia (New Zealand)': 17, 'Avalonia': 18, 'Baltica': 19, 'Cathaysia': 20,
                         'Cathaysia (Kitakamiland)': 21, 'Cathaysia (North)': 22, 'Cathaysia (Sino-Korea)': 105,
                         'Cathaysia (South)': 23, 'Caucasus': 24, 'China (North)': 26, 'China (South)': 25,
                         'Chingiz': 27,
                         'Columbia (Amazonia)': 158, 'Columbia (Australia)': 147, 'Columbia (Baltica)': 156,
                         'Columbia (East Antarctica)': 159, 'Columbia (Greenland)': 157,
                         'Columbia (Indostan)': 137,
                         'Columbia (Kalahari)': 154, 'Columbia (Laurentia)': 151,
                         'Columbia (North Australia)': 164,
                         'Columbia (North China)': 155, 'Columbia (South Australia)': 160,
                         'Columbia (South China)': 153,
                         'Columbia (West Africa)': 152, 'Columbia (West Australia)': 161,
                         'Congo-São Francisco (Congo)': 172,
                         'Eurasia': 28, 'Eurasia (Anatolia)': 29, 'Eurasia (Arabian peninsula)': 30,
                         'Eurasia (Asia)': 32,
                         'Eurasia (Asia Minor)': 31, 'Eurasia (Caucasus)': 33, 'Eurasia (Central Asia)': 36,
                         'Eurasia (Central Asia and Caucasus)': 34, 'Eurasia (Central Asia and Urals)': 35,
                         'Eurasia (China)': 37,
                         'Eurasia (Europe)': 41, 'Eurasia (Europe & Urals)': 38,
                         'Eurasia (Europe and Central Asia)': 39,
                         'Eurasia (Europe and W Siberia)': 40, 'Eurasia (Far East)': 45,
                         'Eurasia (Far East & Central Asia)': 42,
                         'Eurasia (Far East & China)': 43, 'Eurasia (Far East and Japanese Archipelago)': 44,
                         'Eurasia (Greenland)': 46, 'Eurasia (Himalayas)': 47, 'Eurasia (Indochina)': 48,
                         'Eurasia (Indostan)': 49,
                         'Eurasia (Japanese Archipelago)': 51, 'Eurasia (Japanese Archipelago and Sakhalin)': 50,
                         'Eurasia (Java Island)': 52, 'Eurasia (Maritime Southeast Asia)': 53,
                         'Eurasia (Mesopotamian Plain)': 54,
                         'Eurasia (Middle East)': 55, 'Eurasia (Novaja Zemlja Archipelago)': 56,
                         'Eurasia (S Asia)': 123,
                         'Eurasia (S Urals)': 57, 'Eurasia (SE Asia)': 58, 'Eurasia (Siberia)': 61,
                         'Eurasia (Siberia and Central Asia)': 59, 'Eurasia (Siberia and Far East)': 60,
                         'Eurasia (South China)': 62,
                         'Eurasia (South East)': 63, 'Eurasia (Tarim Basin)': 134, 'Eurasia (Tibet)': 64,
                         'Eurasia (Urals)': 65,
                         'Eurasia (W Asia)': 66, 'Eurasia (W Asia & Caucasus)': 67, 'Eurasia (W Siberia)': 69,
                         'Eurasia (W Siberia & Central Asia)': 68, 'Europe': 71, 'Europe (Cis-Caspian)': 72,
                         'Gondwana (Africa)': 73,
                         'Gondwana (Antarctica)': 74, 'Gondwana (Arabia)': 126, 'Gondwana (Armorica)': 75,
                         'Gondwana (Australia)': 76,
                         'Gondwana (Indostan)': 77, 'Gondwana (N Africa)': 78,
                         'Gondwana (N Africa [Tethys palaeocean])': 79,
                         'Gondwana (New Caledonia)': 131, 'Gondwana (New Zealand)': 132, 'Gondwana (Perunica)': 80,
                         'Gondwana (S America)': 81, 'Gondwana (Sardinia)': 113, 'Gondwana (Saxo-Thuringia)': 82,
                         'Gondwana (South Africa)': 124, 'Gondwana (South America)': 83, 'Kazakhstania': 84,
                         'Kazakhstania (Xinjiang)': 85, 'Kenorland (Baltica)': 168, 'Kenorland (Kalaharia)': 169,
                         'Kenorland (Laurentia)': 167, 'Kenorland (Western Australia)': 170, 'Kitakamiland': 86,
                         'Laurentia': 87,
                         'Laurussia': 88, 'Laurussia (Anatolia)': 89, 'Laurussia (Armorica)': 90,
                         'Laurussia (Avalonia)': 93,
                         'Laurussia (Avalonia & Baltica)': 92, 'Laurussia (Baltica)': 94,
                         'Laurussia (Cantabria)': 95,
                         'Laurussia (Iberica)': 96, 'Laurussia (Laurentia)': 97, 'Laurussia (Moesia)': 98,
                         'Laurussia (Moldanubia)': 125, 'Laurussia (Perunica)': 99,
                         'Laurussia (Rhenano-Hercynia)': 100,
                         'Laurussia (Saxo-Thuringia)': 101, 'Moldanubia': 102, 'Mongolia (Western)': 103,
                         'not specified': 106,
                         'Pacific': 107, 'Pamir-Alaj': 108, 'Pannotia (Antarctica)': 174,
                         'Pannotia (Indostan)': 175,
                         'Pannotia (Siberia)': 150, 'Perunica': 109, 'Proangarida': 110, 'Rodinia': 111,
                         'Rodinia (Amazonia)': 141,
                         'Rodinia (Australia)': 146, 'Rodinia (Baltica)': 148, 'Rodinia (Indostan)': 138,
                         'Rodinia (Laurentia)': 140,
                         'Rodinia (North China)': 112, 'Rodinia (Rio Plato)': 142, 'Rodinia (Siberia)': 149,
                         'Rodinia (South China)': 139, 'Siberia': 114, 'Sibumasu': 115,
                         'Superior Craton (Superior Craton)': 171,
                         'Tibet': 116, 'Tien Shan': 117, 'Tien Shan (North)': 118, 'Tien Shan (South)': 133,
                         'Tuva': 119,
                         'unknown': 120, 'Vaalbara (Kaapvaal)': 165, 'Vaalbara (Pilbara)': 166, 'Xinjiang': 121}

Here give you an simplest example:

my = IFPNI(source='species', name='mahonia')

