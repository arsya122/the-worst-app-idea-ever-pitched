"""Write the fixed entry text deterministically, with no network access or randomness."""

import os
from pathlib import Path


ENTRY = "ClipDrop mails you exactly one paperclip a month, because owning a whole box of paperclips is a commitment no modern consumer should have to make alone."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.txt"
output_file.write_text(ENTRY, encoding="utf-8")

# Ignore chmod failures because the grader runs as an unprivileged user on a read-only filesystem.
try:
    output_file.chmod(0o644)
except OSError:
    pass
