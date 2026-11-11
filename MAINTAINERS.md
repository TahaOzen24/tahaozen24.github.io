# Content and release review

## Terms of Service ? 2026-11-11

Added bilingual app-specific terms, keeping mandatory consumer rights and avoiding exclusive jurisdiction, blanket liability waivers, paid purchases or active ranked-service promises. Developer identity/contact reuse the existing public site. Terms have their own update date; privacy policy content/date is unchanged. Terms do not replace consent, privacy disclosures or legal review. Before shipping the new account/ranked build, separately update the older privacy/deletion statements to reflect actual UGS identity and storage.

Reference: https://support.google.com/googleplay/android-developer/answer/17594752


## iOS beta disclosure update - 2026-11-09

The existing Android disclosure now also covers advertising-enabled iOS builds.
The signed iOS 1.0.1 (4) test build uses Google sample ad units with real native
app identification; resolved GMA 13.11.0 and UMP 3.1.0 privacy manifests were
inspected in the IPA. The earlier iOS 1.0.0 (3) build has AdMob disabled. Policy
scope states this distinction and the iOS ATT/IDFA system permission controls.
Test ads do not establish that SDK data processing is off. This is source/native
configuration evidence, not an actual iPhone/network/consent pass. App Store
privacy declarations for the later advertising release still require review.
The website update does not fix or diagnose Apple's generic TestFlight 422.

References: https://developers.google.com/admob/ios/privacy/idfa and
https://developers.google.com/admob/ios/privacy/data-disclosure (the latter
currently describes SDK 13.12.0; do not mislabel the resolved 13.11.0 binary).

## Historical Android review

Content reviewed against the Android game configuration on **2026-10-27** and the providers' current primary documentation. The public developer name and contact email were supplied for this site. Use the same developer identity in the store listing, or update the policy before release.

## Inspected facts

- No developer-operated player login or cloud-save backend. Game board, progress, settings, statistics and a guest profile identifier are stored locally, with local backup files.
- Optional score sharing invokes the operating-system share sheet. It is not an automatic developer upload.
- Android has Google Mobile Ads and UMP integration. The current development build selects Google sample ad units; the policy covers the configured advertising processing and the intended release path.
- Separate Unity Analytics gameplay tracking and Cloud Diagnostics are disabled. Engine-level technical/usage settings can remain distinct; therefore the policy does not claim that the engine processes no technical data.
- Support email is Gmail. The website is hosted by GitHub Pages. These providers' data handling must not be omitted from the policy.
- The current age/audience direction is a general puzzle game, not a child-specific product. Confirm the actual store target audience and SDK age settings before release; change the policy if that direction changes.

## Required checks before a store release

- Confirm public developer name, contact address, actual features and retention practices.
- Keep the privacy policy directly accessible without login, and add its link inside the app as well as to the store listing.
- Publish required AdMob UMP messages using the policy URL. Test consent required/not-required/error and preference-change paths on devices.
- Complete Data safety from actual SDK behavior. Do not declare that no data is collected merely because game progress stays local.
- Link the developer website in the public store listing and complete AdMob's app-ads.txt/app-readiness review.
- Confirm target audience, age-related ad settings and any additional child/teen protections. Do not use this site's wording as a substitute for that configuration.
- Recheck platform-specific SDKs and notices before an iOS release. The initial advertising section is scoped to Android.
- Process privacy requests through the published address; review retained support messages when no longer needed, subject to applicable obligations.

## Primary references

- [Google Play user-data and privacy requirements](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Google Mobile Ads data disclosure](https://developers.google.com/admob/android/privacy/play-data-disclosure)
- [Google UMP integration](https://developers.google.com/admob/unity/privacy)
- [AdMob app-ads.txt setup](https://support.google.com/admob/answer/9363762)
- [Google Privacy Policy](https://policies.google.com/privacy)
- [Unity Game Player and App User Privacy Policy](https://unity.com/legal/game-player-and-app-user-privacy-policy)
- [GitHub Pages privacy and hosting](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
