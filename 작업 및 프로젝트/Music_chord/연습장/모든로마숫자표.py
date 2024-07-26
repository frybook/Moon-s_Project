import pandas as pd

KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Db_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
Chrods_name = {"1" : ["C","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "2" : ["C#,Db","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "3" : ["D","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "4" : ["D#,Eb","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "5" : ["E","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "6" : ["F","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "7" : ["F#,Gb","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "8" : ["G","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "9" : ["G#,Ab","G",  "C",  "F",  "Bb", "Eb", "Ab","C#","F#","B", "E", "A"],
               "10" : ["A","A",  "D",  "G",  "C",  "F",  "Bb","D#","G#","C#","F#","B"],
               "11" : ["A#,Bb","Bb", "Eb", "Ab", "Db", "Gb", "B", "E", "A", "D", "G", "C"],
               "12" : ["B",    "C",  "F",  "Bb", "Eb", "Ab", "Db","F#","B", "E" ,"A", "D"]}
Frame = pd.DataFrame(Chrods_name,index = KEY)
#%%
import pandas as pd

KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Db_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
Chrods_name = {"Ⅰ" : ["C"    ,"F"    ,  "Bb,A#" , "Eb,D#" ,"Ab,G#", "Db,C#", "Gb,F#", "B" ,   "E"    , "A"    ,"D"    , "G"],
               "#Ⅰ": ["C#,Db","F#,Gb",  "B"    ,  "E"    , "A"    , "D" ,    "G" ,    "C" ,   "F"    , "A#,Bb","D#,Eb", "G#,Ab"],
               "ⅱ" : ["D"    ,"G"    ,  "C"    ,  "F"    , "Bb,A#", "Eb,D#", "Ab,G#", "C#,Db","F#,Gb", "B"    ,"E"    , "A"],
               "#ⅱ": ["D#,Eb","G#,Ab",  "Db,C#",  "Gb,F#", "B"    , "E" ,    "A" ,    "D"    ,"G",     "C",    "F"    , "A#,Bb"],
               "ⅲ" : ["E"    ,"A"    ,  "D"    ,  "G"    , "C"    , "F" ,    "Bb,A#", "D#,Eb","G#,Ab", "C#,Db","F#,Gb", "B"],
               "Ⅳ" : ["F"    ,"A#,Bb" , "Eb,D#" , "Ab,G#", "Db,C#", "Gb,F#", "B" ,    "E" ,   "A"    , "D"    ,"G"    , "C"],
               "#Ⅳ": ["F#,Gb","B"    ,  "E"     , "A"    , "D"    , "G" ,    "C" ,    "F" ,   "A#,Bb", "D#,Eb","G#,Ab", "C#,Db"],
               "Ⅴ" : ["G"    ,"C"    ,  "F"    ,  "Bb,A#", "Eb,D#", "Ab,G#", "Db,C#", "F#,Gb","B"    , "E"    ,"A"    , "D"],
               "#Ⅴ": ["G#,Ab","C#,Db",  "Gb,F#",  "B"    , "E"    , "A" ,    "D" ,    "G"    ,"C"    , "F"    ,"A#,Bb", "D#,Eb"],
               "ⅵ" : ["A"    ,"D"    ,  "G"    ,  "C"    , "F"    , "Bb,A#", "Eb,D#", "G#,Ab","C#,Db", "F#,Gb","B"    , "E"],
               "#ⅵ": ["A#,Bb","D#,Eb",  "Ab,G#",  "Db,C#", "Gb,F#", "B" ,    "E" ,    "A" ,   "D"    , "G"    ,"C"    , "F"],
               "ⅶ" : ["B"    ,"E"    ,  "A"    ,  "D"    , "G"    , "C" ,    "F" ,    "A#,Bb","D#,Eb", "G#,Ab","C#,Db" ,"F#,Gb"]}
Frame = pd.DataFrame(Chrods_name,index = KEY)
Frame.to_csv("All_Major_scale.csv", index_label='KEY')
