# train args
class TRAIN_ARGS:
    INDEX_OF = {
        'examples': 1,
        'hypothesisOut': 2,
        'learning-type': 3
    }
    COUNT = len(INDEX_OF)

# test args
class TEST_ARGS:
    INDEX_OF = {
        'hypothesis': 1,
        'file': 2
    }
    COUNT = len(INDEX_OF)

# language shorthand
LANGUAGE = {
    'ENGLISH': 'en', 
    'DUTCH': 'nl'
}

# learning types
LEARNING_TYPE = {
    'DECISION_TREE': 'dt',
    'ADABOOST': 'ada'
}

# file paths
EN_PRE_TRAINING_DATA_FILE_PATH = f"./input/pre_train/{LANGUAGE['ENGLISH']}_pre_train.txt"
NL_PRE_TRAINING_DATA_FILE_PATH = f"./input/pre_train/{LANGUAGE['DUTCH']}_pre_train.txt"
TRAINING_DATA_FILE_PATH = './input/train/train.dat'

# Feature constants
class FEATURES:
    class FEATURE_0:
        NAME = 'Atleast 2 words contain \"ij\"'
        IJ = 'ij'
        IJ_COUNT_THRESHOLD = 2

    class FEATURE_1:
        NAME = 'Atleast one word is \"de\" or \"het\"'
        STRINGS = ['de', 'het']
    
    class FEATURE_2:
        NAME = 'Atleast one word is \"en\"'
        EN = 'en'

    class FEATURE_3:
        NAME = 'Atleast one word is \"and\"'
        AND = 'and'

    class FEATURE_4:
        NAME = 'Is one of dutch common words'
        COMMON_NL_WORDS = ['ik', 'je', 'het', 'de', 'dat', 'een', 'niet',\
            'en', 'wat', 'van', 'ze', 'op', 'te', 'hij', 'zijn', 'er' ,\
            'maar', 'die', 'heb', 'voor' , 'met', 'als', 'ben', 'mijn' ,'u' ,\
            'dit' ,'aan' ,'om' ,'hier' ,'naar' ,'dan' ,'jij' ,'zo' ,'weet' ,\
            'ja' ,'kan' ,'geen' ,'nog' ,'wel' ,'wil' ,'moet' ,'goed' ,'hem',\
            'hebben' ,'nee' ,'heeft' ,'waar' ,'nu' ,'hoe' ,'ga' ,'kom' ,'uit',\
            'gaan' ,'bent' ,'haar' ,'doen' ,'ook' ,'mij', 'daar' , 'zou' ,\
            'al' , 'jullie' , 'zal' , 'bij' , 'ons' , 'gaat' , 'hebt', 'meer',\
            'waarom' , 'iets' , 'deze' ,'laat', 'doe', 'm', 'moeten', 'wie',\
            'jou', 'alles' , 'denk' , 'kunnen' , 'eens' , 'echt' , 'weg',\
            'toch' , 'zien' , 'oké' , 'alleen' , 'nou', 'dus', 'nooit',\
            'terug' , 'laten' , 'mee', 'hou' , 'komt' , 'niets' , 'zei' ,\
            'misschien' , 'kijk' , 'iemand' , 'komen' , 'tot' , 'veel' ,\
            'worden' , 'onze' , 'mensen' , 'zeg' , 'leven' , 'zeggen' ,'weer',\
            'gewoon' , 'nodig' , 'wij' , 'twee' , 'tijd' , 'tegen' , 'uw' ,\
            'toen' , 'zit' , 'net' , 'weten' , 'heel' , 'maken' , 'wordt' ,\
            'dood' , 'mag' , 'altijd' , 'af' , 'wacht' , 'geef' , 'z' , 'lk',\
            'dag' , 'omdat' , 'zeker' , 'zie' , 'allemaal' , 'gedaan' , 'oh' ,\
            'dank' , 'huis' , 'hé' , 'zij' , 'jaar' , 'vader', 'doet','zoals',\
            'jouw' , 'vrouw' , 'geld' , 'hun']
        
    class FEATURE_5:
        NAME = 'Is one of english common words'
        COMMON_EN_WORDS = ['a' ,'about' ,'all' ,'also' ,'and' ,'as','at','be',\
            'because' ,'but' ,'by' ,'can' ,'come' ,'could' ,'day' ,'do','even',\
            'find' ,'first' ,'for' ,'from' ,'get' ,'give' ,'go','have','he',\
            'her','here' ,'him' ,'his' ,'how' ,'I' ,'if' ,'in' ,'into','it',\
            'its','just','know' ,'like' ,'look' ,'make' ,'man','many','me',\
            'more' ,'my' ,'new' ,'no' ,'not' ,'now' ,'of' ,'on','one','only',\
            'or' ,'other','our' ,'out','people','say','see','she','so','some',\
            'take' ,'tell' ,'than','that','the','their','them','then','there',\
            'these' ,'they' ,'thing' ,'think' ,'this' ,'those' ,'time' ,'to' ,\
            'two' ,'up' ,'use' ,'very' ,'want' ,'way' ,'we' ,'well' ,'what' ,\
            'when' ,'which' ,'who' ,'will' ,'with' ,'would' ,'year' ,'you' ,'your']

    class FEATURE_6:
        NAME = 'Average word length'
        AVG_WORD_LENGTH = 4.25

    class FEATURE_7:
        NAME = '2 letter word freq.'
        AVG_FREQ = 0.2

    class FEATURE_8:
        NAME = 'Has common bigrams'
        COMMON_BIGRAMS = ['th', 'er', 'on', 'an']

    class FEATURE_9:
        NAME = 'Has common trigrams'
        COMMON_TRIGRAMS = [
            'the',
            'and',
            'tha',
            'ent',
            'ing',
            'ion',
            'tio',
            'for',
            'nde',
            'has',
            'nce',
            'edt',
            'tis',
            'oft',
            'sth',
            'men'
        ]