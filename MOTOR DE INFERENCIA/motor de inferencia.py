# Reglas de Producción
rules = [
    {"IF": [("Mandíbulas", "No"), ("Número de aletas", "Impar"), ("Esqueleto", "Cartilaginoso"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Agnatos")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "Par"), ("Esqueleto", "Cartilaginoso"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Condricties")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "Par"), ("Esqueleto", "Óseo"), 
            ("Escamas", "Sí"), ("Respiración", "Branquial"), ("Hábitat", "Agua")], "THEN": ("Clase", "Osteicties")},
    {"IF": [("Mandíbulas", "Sí"), ("Número de aletas", "No"), ("Esqueleto", "Óseo"), ("Escamas", "No"), 
            ("Respiración", "Branquial"), ("Piel", "Lisa y húmeda"), ("Temperatura", "Variable"), 
            ("Reproducción", "Ovíparo"), ("Metamorfosis", "Sí")], "THEN": ("Clase", "Anfibios")},
    {"IF": [("Clase", "Anfibios"), ("Cuerpo", "Alargado"), ("Cola", "Sí"), ("Miembros", "Sí")], "THEN": ("Orden", "Urodelos")},
    {"IF": [("Mandíbulas", "Sí"), ("Aletas", "No"), ("Piel", "Escamas duras"), ("Temperatura", "Variable"), 
            ("Respiración", "Pulmonar"), ("Esqueleto", "Óseo"), ("Reproducción", "Ovíparo")], "THEN": ("Clase", "Reptiles")},
    {"IF": [("Clase", "Reptiles"), ("Cuerpo", "Alargado"), ("Miembros", "No")], "THEN": ("Orden", "Ofidios")},
    {"IF": [("Mandíbulas", "Sí"), ("Esqueleto", "Óseo"), ("Aletas", "No"), ("Escamas", "No"), 
            ("Respiración", "Pulmonar"), ("Piel", "Plumas"), ("Temperatura", "Constante"), 
            ("Reproducción", "Ovíparo"), ("Poseen", "Pico y Cloaca")], "THEN": ("Clase", "Aves")},
    {"IF": [("Clase", "Aves"), ("Orden", "Carenadas"), ("Patas", "Palmeadas"), 
            ("Plumaje", "Espeso"), ("Habilidad", "Nadar")], "THEN": ("Suborden", "Palmípedas")},
    {"IF": [("Mandíbulas", "Sí"), ("Esqueleto", "Óseo"), ("Respiración", "Pulmonar"), 
            ("Piel", "Pelos"), ("Temperatura", "Constante"), ("Escamas", "No"), 
            ("Glándulas mamarias", "Sí")], "THEN": ("Clase", "Mamíferos")}
]

# Hechos
facts = [
    ("Mandíbulas", "Sí"),
    ("Número de aletas", "Par"),
    ("Esqueleto", "Óseo"),
    ("Escamas", "Sí"),
    ("Respiración", "Branquial"),
    ("Hábitat", "Agua")
]

# Motor de Inferencia
def evaluate_rules(rules, facts):
    for rule in rules:
        if all(condition in facts for condition in rule["IF"]):
            return rule["THEN"]
    return None

result = evaluate_rules(rules, facts)
if result:
    print(f"El animal es de la clase: {result[1]}")
else:
    print("No se pudo clasificar el animal.")

# MOTOR DE INFERENCIA    
def forward_chain(rules, facts):
    inferred = []
    while True:
        new_inferences = []
        for rule in rules:
            if all(fact in facts for fact in rule["IF"]):
                inferred_fact = rule["THEN"]
                if inferred_fact not in facts:
                    new_inferences.append(inferred_fact)
        
        if not new_inferences:
            break
        
        for inference in new_inferences:
            facts.append(inference)
            inferred.append(inference)
    
    return inferred

inferred_facts = forward_chain(rules, facts)
print("Inferred facts:")
for fact in inferred_facts:
    print(fact)


# Función de Encadenamiento Hacia Atrás
def backward_chaining(goal, rules, facts):
    if goal in facts:
        return True

    for rule in rules:
        if rule["THEN"] == goal:
            all_conditions_met = True
            for condition in rule["IF"]:
                if not backward_chaining(condition, rules, facts):
                    all_conditions_met = False
                    break
            if all_conditions_met:
                return True

# Función para agregar un hecho
def add_fact(fact):
    facts.append(fact)

# Función para verificar una hipótesis
def verify_hypothesis(goal):
    return backward_chaining(goal, rules, facts)

if __name__ == "__main__":
    goal = ("Clase", "Osteicties")
    result = verify_hypothesis(goal)
    if result:
        print(f"El objetivo {goal} es verdadero basado en los hechos y reglas dadas.")
    else:
        print(f"El objetivo {goal} no se puede inferir de los hechos y reglas dadas.")

