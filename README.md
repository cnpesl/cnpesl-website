# cnpesl.com

Website of CNP Engineering Services Ltd, served from HostGator cPanel.

## How it is organised

- `public_html/` is the live website. Everything in it is copied to the server's `public_html` folder on deploy.
- `tools/build.py` holds the page content (projects, team, text) and generates the HTML in `public_html/`.
- `.cpanel.yml` tells cPanel's Git Version Control how to deploy.

## Updating the site

1. Edit the content in `tools/build.py` (for example add a project to `DESIGN_PROJECTS` or `SURVEYS`) and put any new image, resized to about 1400 px wide, in `public_html/assets/img/`.
2. Run `python3 tools/build.py`.
3. Commit and push to `main`.
4. In cPanel, open Git Version Control, choose this repository, click **Update from Remote**, then **Deploy HEAD Commit**.

Every change is also logged in the "CNP IT Change Log" sheet on Google Drive.
