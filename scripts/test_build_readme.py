import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_readme import blurb, first_image, version

assert blurb("Plan Sunday, review Saturday: an agent skill that fits") == "Plan Sunday, review Saturday."
assert blurb("Disciplined multi-agent execution for Claude UltraCode — one leader") == "Disciplined multi-agent execution for Claude UltraCode."
assert blurb("Short: but head too short to cut here ok") == "Short: but head too short to cut here ok."
assert blurb(None) == ""
assert first_image("x ![a b](media/h.png) y", "o", "r", "main") == "https://raw.githubusercontent.com/o/r/main/media/h.png"
assert first_image('<img src="https://x/y.png">', "o", "r", "main") == "https://x/y.png"
assert first_image("no picture", "o", "r", "main") is None
assert version("# Changelog\n\n## [0.2.0] - 2026-11-12\n## 0.1.0") == "0.2.0"
assert version("nothing") is None
print("ok")
