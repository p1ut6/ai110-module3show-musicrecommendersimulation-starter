code = open("README.md", encoding="utf-8").read()

cutoff = "## 7. `model_card_template.md`"
if cutoff in code:
    code = code[:code.index(cutoff)].rstrip() + "\n"
    print("Removed template section.")
else:
    print("Section not found.")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(code)
print("Done!")