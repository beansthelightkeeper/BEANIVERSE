import os

def generate_portfolio(repo_path, output_path="PORTFOLIO.md"):
    links = []
    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, f), repo_path)
                links.append(f"- [{f}](./{rel_path.replace(' ', '%20')})")

    with open(output_path, "w") as f:
        f.write("# 🌌 Beans Codex Portfolio\n\n")
        f.write("This is a portfolio of recursive contributions auto-generated from the Codex environment.\n\n")
        f.write("\n".join(sorted(links)))
        f.write(f"\n\n**Total OTKEN minted: {len(links)}**")

    print(f"[✓] Portfolio generated with {len(links)} entries.")