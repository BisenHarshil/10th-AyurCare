symptoms_remedies = {
    "headache": {
        "remedies": ["Peppermint oil massage on temples", "Ginger tea with honey", "Brahmi powder with warm milk"],
        "herbs": ["Brahmi", "Ginger", "Peppermint"],
        "lifestyle": "Avoid screen time, rest in a dark room, stay hydrated"
    },
    "cold": {
        "remedies": ["Tulsi and ginger kadha", "Steam inhalation with eucalyptus", "Turmeric milk before bed"],
        "herbs": ["Tulsi", "Ginger", "Turmeric"],
        "lifestyle": "Stay warm, avoid cold drinks, rest well"
    },
    "fever": {
        "remedies": ["Giloy juice twice daily", "Tulsi and black pepper tea", "Neem leaf paste on forehead"],
        "herbs": ["Giloy", "Tulsi", "Neem"],
        "lifestyle": "Rest, drink warm water, avoid heavy food"
    },
    "acidity": {
        "remedies": ["Amla juice on empty stomach", "Fennel seeds after meals", "Cold milk with cardamom"],
        "herbs": ["Amla", "Fennel", "Cardamom"],
        "lifestyle": "Eat on time, avoid spicy food, walk after meals"
    },
    "stress": {
        "remedies": ["Ashwagandha powder with warm milk", "Brahmi tea before bed", "Chamomile and tulsi tea"],
        "herbs": ["Ashwagandha", "Brahmi", "Chamomile"],
        "lifestyle": "Meditate daily, sleep by 10pm, avoid caffeine"
    },
    "joint pain": {
        "remedies": ["Turmeric and ginger paste on joints", "Dashmool oil massage", "Boswellia supplement"],
        "herbs": ["Turmeric", "Ginger", "Boswellia"],
        "lifestyle": "Light exercise, warm water intake, avoid cold exposure"
    },
    "skin problems": {
        "remedies": ["Neem face pack", "Aloe vera gel application", "Turmeric and sandalwood paste"],
        "herbs": ["Neem", "Aloe Vera", "Turmeric"],
        "lifestyle": "Drink 8 glasses of water, avoid processed food, sleep well"
    },
    "digestion": {
        "remedies": ["Triphala powder with warm water at night", "Jeera water after meals", "Ajwain with warm water"],
        "herbs": ["Triphala", "Jeera", "Ajwain"],
        "lifestyle": "Eat slowly, avoid overeating, walk 10 mins after meals"
    }
}

herbs_database = {
    "Tulsi": {
        "description": "Queen of herbs in Ayurveda. Known for its powerful healing properties.",
        "benefits": ["Boosts immunity", "Fights infections", "Reduces stress", "Improves digestion"],
        "uses": "Make tea, chew fresh leaves, use in kadha",
        "treats": ["cold", "fever", "stress", "cough"]
    },
    "Ashwagandha": {
        "description": "Ancient medicinal herb known as Indian Ginseng. Powerful adaptogen.",
        "benefits": ["Reduces stress and anxiety", "Boosts energy", "Improves sleep", "Builds strength"],
        "uses": "Mix powder in warm milk, take capsules, add to smoothies",
        "treats": ["stress", "fatigue", "anxiety", "weakness"]
    },
    "Turmeric": {
        "description": "Golden spice of India. Powerful anti-inflammatory and antioxidant.",
        "benefits": ["Reduces inflammation", "Boosts immunity", "Improves skin", "Aids digestion"],
        "uses": "Add to milk, use in cooking, apply as paste on skin",
        "treats": ["joint pain", "skin problems", "fever", "digestion"]
    },
    "Ginger": {
        "description": "Universal medicine in Ayurveda. Warming and healing.",
        "benefits": ["Aids digestion", "Reduces nausea", "Fights cold", "Reduces pain"],
        "uses": "Make tea, add to food, chew fresh piece",
        "treats": ["cold", "headache", "digestion", "joint pain"]
    },
    "Neem": {
        "description": "Village pharmacy of India. Bitter but incredibly powerful.",
        "benefits": ["Purifies blood", "Fights bacteria", "Clears skin", "Boosts immunity"],
        "uses": "Chew leaves, apply paste, use neem oil",
        "treats": ["skin problems", "fever", "infections", "diabetes"]
    },
    "Brahmi": {
        "description": "Brain tonic of Ayurveda. Enhances memory and reduces stress.",
        "benefits": ["Improves memory", "Reduces anxiety", "Promotes sleep", "Sharpens focus"],
        "uses": "Mix powder in milk, make tea, take as supplement",
        "treats": ["stress", "headache", "anxiety", "poor memory"]
    },
    "Amla": {
        "description": "Richest natural source of Vitamin C. Rejuvenating superfruit.",
        "benefits": ["Boosts immunity", "Improves hair", "Aids digestion", "Anti-ageing"],
        "uses": "Eat raw, drink juice, take powder with honey",
        "treats": ["acidity", "hair loss", "digestion", "weak immunity"]
    },
    "Giloy": {
        "description": "Miracle herb of Ayurveda. Powerful immunity booster.",
        "benefits": ["Boosts immunity", "Reduces fever", "Detoxifies body", "Manages diabetes"],
        "uses": "Drink juice, make kadha, take as supplement",
        "treats": ["fever", "infections", "diabetes", "weak immunity"]
    }
}

daily_tips = [
    {"tip": "Start your day with warm water and lemon to activate digestion.", "category": "Digestion"},
    {"tip": "Practice Anulom Vilom pranayama for 10 minutes every morning.", "category": "Breathing"},
    {"tip": "Eat your largest meal at lunch when digestive fire is strongest.", "category": "Diet"},
    {"tip": "Avoid eating after 7pm — give your body time to rest.", "category": "Diet"},
    {"tip": "Oil pull with sesame oil for 5 minutes to detoxify your mouth.", "category": "Detox"},
    {"tip": "Massage your feet with warm sesame oil before bed for better sleep.", "category": "Sleep"},
    {"tip": "Drink Tulsi tea in the evening to reduce daily stress.", "category": "Stress"},
    {"tip": "Eat seasonal and local fruits — they carry the energy your body needs.", "category": "Diet"},
    {"tip": "Walk barefoot on grass in the morning to ground your energy.", "category": "Wellness"},
    {"tip": "Avoid cold water — always drink water at room temperature or warm.", "category": "Digestion"},
    {"tip": "Practice gratitude before sleeping — it calms Vata dosha.", "category": "Mental Health"},
    {"tip": "Add a pinch of turmeric to your morning milk for daily immunity.", "category": "Immunity"},
]

weather_tips = {
    "cold": {"tip": "It's cold today — drink warm ginger tea and avoid cold foods to balance Vata dosha.", "category": "Seasonal"},
    "hot": {"tip": "It's hot today — drink coconut water and eat cooling foods like cucumber to balance Pitta dosha.", "category": "Seasonal"},
    "rainy": {"tip": "Rainy weather increases Kapha — favor light, warm, freshly cooked meals and avoid heavy or oily food.", "category": "Seasonal"},
    "normal": {"tip": "Pleasant weather today — a good day for outdoor walks and fresh seasonal fruits.", "category": "Seasonal"}
}