# Tower of Hanoi — RISC-V Code Base Demo
# Language: Python 3 (scripted, no compilation needed)
# Demonstrates: RECURSION

def hanoi(n, source, target, aux, depth=0):
    # ── BASE CASE ────────────────────────────────────────────
    # When n == 0, there's nothing to move. This stops the
    # recursion. Without it, calls would never terminate.
    if n == 0:
        return

    # ── RECURSIVE CALL 1 ─────────────────────────────────────
    # Move the top n-1 disks out of the way (source → aux).
    # This call goes DEEPER in the stack (depth increases).
    hanoi(n - 1, source, aux, target, depth + 1)

    # ── ITERATIVE ACTION ──────────────────────────────────────
    # Move the single largest remaining disk directly.
    # This is the real "work" done at each stack frame.
    indent = "  " * depth
    print(f"{indent}[depth {depth}] Move disk {n}: {source} → {target}")

    # ── RECURSIVE CALL 2 ─────────────────────────────────────
    # Move the n-1 disks from aux onto target (aux → target).
    hanoi(n - 1, aux, target, source, depth + 1)

# ── ENTRY POINT ───────────────────────────────────────────────
N = 4
print(f"Tower of Hanoi | {N} disks | {2**N - 1} total moves\n")
hanoi(N, source="A", target="C", aux="B")