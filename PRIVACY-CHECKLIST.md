# Before publishing any map

Run through this every time before pushing to GitHub or adding a map to the website.

- [ ] **No personal data** in the notebook, data files or image: no names, IDs, phone numbers, emails, home addresses.
- [ ] **No secrets:** no API keys or tokens in the code (use a git-ignored `.env` if a key is ever needed).
- [ ] **Image metadata stripped:** export with `save_clean_png()` (in the notebook), which saves without EXIF/text chunks.
- [ ] **No large raw data committed:** the notebook downloads its data; `data/` stays git-ignored.
- [ ] **Sources credited** in the map caption and the folder README.
- [ ] **Honest caption:** say what the map shows, the data's limits, and that I'm learning.
- [ ] `git status` shows only the files I meant to add.
