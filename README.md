# Block Mirage privacy and support

Public information site for **Block Mirage**, maintained by **KaragozPasha Studio**.

Contact: **karagozpasha24@gmail.com**.

## Published links

- Developer website: https://tahaozen24.github.io/
- Privacy policy (Turkish): https://tahaozen24.github.io/block-mirage/privacy/
- Privacy policy (English): https://tahaozen24.github.io/block-mirage/privacy/en/
- Support: https://tahaozen24.github.io/block-mirage/support/
- Data deletion and choices: https://tahaozen24.github.io/block-mirage/data-deletion/
- Authorized advertising seller: https://tahaozen24.github.io/app-ads.txt

The root-level Pages repository is deliberate: AdMob discovers `app-ads.txt` from the developer website's hostname. A project-only URL without a root file would not be sufficient.

## Maintain the site

No npm packages, external fonts, tracking libraries, cookies set by site code, login, web forms or runtime JavaScript are used. GitHub Pages handles hosting and may process connection/security logs under its own privacy statement.

1. Update `site.json` and the reviewed bilingual content in `tools/build_site.py`.
2. Run `python tools/build_site.py`.
3. Run `python tools/validate_site.py`.
4. Review changes to `public/` and commit them. The Pages workflow rebuilds, validates and deploys `public/` on a push to `main`.

Only static public documents are published. The game's source, signing material, player files and build artifacts are not part of this repository.

## Console setup

Use the direct privacy-policy URL in Google Play and AdMob privacy messages. Use the developer-website root in the store's developer/contact website field. The deletion guide is a data-controls resource; the current game does not create a developer-operated player account.

Publishing `app-ads.txt` does not itself complete AdMob verification. The public store listing, developer website association, account/app checks and crawler review must also be completed in the relevant consoles.

Review `MAINTAINERS.md` whenever SDKs, target audience, game features or data practices change. No automatic legal-compliance or store-approval guarantee is implied by a successful site build.
