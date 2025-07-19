import json
import sys
from pathlib import Path

def validate_topology(file_path):
    data = json.load(open(file_path))
    nodes = {n["node_id"] for n in data.get("topology", [])}
    errors = []
    for link in data.get("links", []):
        for endpoint in link["nodes"]:
            node = endpoint.split(":", 1)[0]
            if node not in nodes:
                errors.append(f"Link refere nó inválido: {endpoint}")
    if len(nodes) != len(data.get("topology")):
        errors.append("IDs de nodes duplicados detectados")
    return errors

def main():
    base = Path(__file__).parent.parent / "gns3" / "topologies"
    for topo in base.rglob("*.gns3"):
        print(f"Validando {topo.relative_to(base.parent)}")
        errs = validate_topology(topo)
        if errs:
            print(" Erros encontrados:")
            for e in errs:
                print("  -", e)
        else:
            print(" OK")

if __name__ == "__main__":
    main()