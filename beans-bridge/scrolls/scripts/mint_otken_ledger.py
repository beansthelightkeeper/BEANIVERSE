import os
from datetime import datetime

def mint_otken(repo_path, output_path="OTKEN_LEDGER.md"):
    ledger = []
    total_tokens = 0

    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, f), repo_path)
                ledger.append(f"| {datetime.today().date()} | {f} | +1 OTKEN |")
                total_tokens += 1

    with open(output_path, "w") as f:
        f.write("# 🪙 OTKEN LEDGER\n\n")
        f.write("This is a recursive record of all Codex tokens minted from Beans' contributions.\n\n")
        f.write("| Date | File | Tokens Minted |\n")
        f.write("|------|------|----------------|\n")
        f.write("\n".join(ledger))
        f.write(f"\n\n**Total OTKEN minted: {total_tokens}**")

    print(f"[✓] Ledger generated with {total_tokens} OTKEN entries.")