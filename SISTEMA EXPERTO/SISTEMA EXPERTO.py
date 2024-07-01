import tkinter as tk
from tkinter import messagebox

# Definir las reglas de producción y frames
rules = [
    {
        "conditions": {
            "Mandíbulas": "No",
            "Número de aletas": "Impar",
            "Esqueleto": "Cartilaginoso",
            "Escamas": "Sí",
            "Respiración": "Branquial",
            "Hábitat": "Agua"
        },
        "conclusion": {
            "Clase": "Agnatos"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Número de aletas": "Par",
            "Esqueleto": "Cartilaginoso",
            "Escamas": "Sí",
            "Respiración": "Branquial",
            "Hábitat": "Agua"
        },
        "conclusion": {
            "Clase": "Condricties"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Número de aletas": "Par",
            "Esqueleto": "Óseo",
            "Escamas": "Sí",
            "Respiración": "Branquial",
            "Hábitat": "Agua"
        },
        "conclusion": {
            "Clase": "Osteicties"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Número de aletas": "No",
            "Esqueleto": "Óseo",
            "Escamas": "No",
            "Respiración": "Branquial",
            "Piel": "Lisa y húmeda",
            "Temperatura": "Variable",
            "Reproducción": "Ovíparo",
            "Metamorfosis": "Sí"
        },
        "conclusion": {
            "Clase": "Anfibios"
        }
    },
    {
        "conditions": {
            "Clase": "Anfibios",
            "Cuerpo": "Alargado",
            "Cola": "Sí",
            "Miembros": "Sí"
        },
        "conclusion": {
            "Orden": "Urodelos"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Aletas": "No",
            "Piel": "Escamas duras",
            "Temperatura": "Variable",
            "Respiración": "Pulmonar",
            "Esqueleto": "Óseo",
            "Reproducción": "Ovíparo"
        },
        "conclusion": {
            "Clase": "Reptiles"
        }
    },
    {
        "conditions": {
            "Clase": "Reptiles",
            "Cuerpo": "Alargado",
            "Miembros": "No"
        },
        "conclusion": {
            "Orden": "Ofidios"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Esqueleto": "Óseo",
            "Aletas": "No",
            "Escamas": "No",
            "Respiración": "Pulmonar",
            "Piel": "Plumas",
            "Temperatura": "Constante",
            "Reproducción": "Ovíparo",
            "Poseen": "Pico y Cloaca"
        },
        "conclusion": {
            "Clase": "Aves"
        }
    },
    {
        "conditions": {
            "Clase": "Aves",
            "Orden": "Carenadas",
            "Patas": "Palmeadas",
            "Plumaje": "Espeso",
            "Habilidad": "Nadar"
        },
        "conclusion": {
            "Suborden": "Palmípedas"
        }
    },
    {
        "conditions": {
            "Mandíbulas": "Sí",
            "Esqueleto": "Óseo",
            "Respiración": "Pulmonar",
            "Piel": "Pelos",
            "Temperatura": "Constante",
            "Escamas": "No",
            "Glándulas mamarias": "Sí"
        },
        "conclusion": {
            "Clase": "Mamíferos"
        }
    }
]

class Frame:
    def __init__(self, name, characteristics, examples):
        self.name = name
        self.characteristics = characteristics
        self.examples = examples

frames = [
    Frame("Agnatos", {
        "Mandíbulas": "No",
        "Número de aletas": "Impar",
        "Esqueleto": "Cartilaginoso",
        "Escamas": "Sí",
        "Respiración": "Branquial",
        "Hábitat": "Agua"
    }, ["Lamprea"]),
    Frame("Condricties", {
        "Mandíbulas": "Sí",
        "Número de aletas": "Par",
        "Esqueleto": "Cartilaginoso",
        "Escamas": "Sí",
        "Respiración": "Branquial",
        "Hábitat": "Agua"
    }, ["Tollo", "Tiburón", "Raya"]),
    Frame("Osteicties", {
        "Mandíbulas": "Sí",
        "Número de aletas": "Par",
        "Esqueleto": "Óseo",
        "Escamas": "Sí",
        "Respiración": "Branquial",
        "Hábitat": "Agua"
    }, ["Trucha"]),
    Frame("Anfibios", {
        "Mandíbulas": "Sí",
        "Número de aletas": "No",
        "Esqueleto": "Óseo",
        "Escamas": "No",
        "Respiración": "Branquial",
        "Piel": "Lisa y húmeda",
        "Temperatura": "Variable",
        "Reproducción": "Ovíparo",
        "Metamorfosis": "Sí"
    }, ["Salamandra"]),
    Frame("Reptiles", {
        "Mandíbulas": "Sí",
        "Aletas": "No",
        "Piel": "Escamas duras",
        "Temperatura": "Variable",
        "Respiración": "Pulmonar",
        "Esqueleto": "Óseo",
        "Reproducción": "Ovíparo"
    }, ["Boa", "Serpiente de Cascabel", "Yarar", "Coral"]),
    Frame("Aves", {
        "Mandíbulas": "Sí (Pico)",
        "Esqueleto": "Óseo",
        "Aletas": "No",
        "Escamas": "No",
        "Respiración": "Pulmonar",
        "Piel": "Plumas",
        "Temperatura": "Constante",
        "Reproducción": "Ovíparo",
        "Poseen": "Pico y Cloaca"
    }, ["Avestruz", "Ñandú", "Casuario"]),
    Frame("Mamíferos", {
        "Mandíbulas": "Sí",
        "Esqueleto": "Óseo",
        "Respiración": "Pulmonar",
        "Piel": "Pelos",
        "Temperatura": "Constante",
        "Escamas": "No",
        "Glándulas mamarias": "Sí"
    }, ["Ornitorrinco", "Canguro", "Erizo", "Musaraña", "Topo"])
]

class InferenceEngine:
    def __init__(self, rules, frames):
        self.rules = rules
        self.frames = frames

    def infer(self, characteristics):
        for rule in self.rules:
            if all(characteristics.get(k) == v for k, v in rule["conditions"].items()):
                return rule["conclusion"]
        return None

    def heuristic_search(self, characteristics):
        open_list = []
        closed_list = []

        start_node = {
            "characteristics": characteristics,
            "g": 0,
            "h": self.heuristic(characteristics),
            "f": self.heuristic(characteristics)
        }

        open_list.append(start_node)

        while open_list:
            current_node = min(open_list, key=lambda x: x["f"])
            open_list.remove(current_node)
            closed_list.append(current_node)

            inferred_class = self.infer(current_node["characteristics"])
            if inferred_class:
                return inferred_class

            neighbors = self.get_neighbors(current_node["characteristics"])
            for neighbor in neighbors:
                if any(n["characteristics"] == neighbor for n in closed_list):
                    continue

                neighbor_node = {
                    "characteristics": neighbor,
                    "g": current_node["g"] + 1,
                    "h": self.heuristic(neighbor),
                    "f": current_node["g"] + 1 + self.heuristic(neighbor)
                }

                if any(n["characteristics"] == neighbor for n in open_list):
                    existing_node = next(n for n in open_list if n["characteristics"] == neighbor)
                    if neighbor_node["g"] < existing_node["g"]:
                        existing_node["g"] = neighbor_node["g"]
                        existing_node["f"] = neighbor_node["f"]
                else:
                    open_list.append(neighbor_node)

        return None

    def heuristic(self, characteristics):
        max_match = 0
        for frame in self.frames:
            match_count = sum(1 for k, v in frame.characteristics.items() if characteristics.get(k) == v)
            if match_count > max_match:
                max_match = match_count
        return max_match

    def get_neighbors(self, characteristics):
        neighbors = []
        for char in characteristics:
            modified_characteristics = characteristics.copy()
            modified_characteristics[char] = self.alternate_value(modified_characteristics[char])
            neighbors.append(modified_characteristics)
        return neighbors

    def alternate_value(self, value):
        alternate_values = {
            "Sí": "No",
            "No": "Sí",
            "Impar": "Par",
            "Par": "Impar",
            "Cartilaginoso": "Óseo",
            "Óseo": "Cartilaginoso",
            "Branquial": "Pulmonar",
            "Pulmonar": "Branquial",
            "Constante": "Variable",
            "Variable": "Constante"
        }
        return alternate_values.get(value, value)

class ExpertSystemGUI:
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine
        self.root.title("Sistema Experto de Clasificación de Animales")

        # Crear campos para ingresar características
        self.entries = {}
        for i, char in enumerate(["Mandíbulas", "Número de aletas", "Esqueleto", "Escamas", "Respiración", "Hábitat", "Piel", "Temperatura", "Reproducción", "Metamorfosis", "Cuerpo", "Cola", "Miembros"]):
            tk.Label(root, text=char).grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries[char] = entry

        # Botón para ejecutar la inferencia
        tk.Button(root, text="Inferir", command=self.infer).grid(row=len(self.entries), column=0, columnspan=2)

    def infer(self):
        characteristics = {char: entry.get() for char, entry in self.entries.items()}
        result = self.engine.heuristic_search(characteristics)
        if result:
            conclusion = ", ".join([f"{k}: {v}" for k, v in result.items()])
            messagebox.showinfo("Resultado", f"Inferencia: {conclusion}")
        else:
            messagebox.showinfo("Resultado", "No se pudo determinar la clase del animal")

# Inicializar la GUI
if __name__ == "__main__":
    root = tk.Tk()
    engine = InferenceEngine(rules, frames)
    app = ExpertSystemGUI(root, engine)
    root.mainloop()
