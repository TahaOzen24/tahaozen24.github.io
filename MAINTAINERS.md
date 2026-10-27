# Content and release review

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
