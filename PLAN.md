# Master Plan

We are creating a static site web app, hosted on GitHub Pages.

This repository is a git repository.

Most pages of this app will be single-purpose pages (Cards) that are, for example, something I'd show to a Japanese taxi driver who doesn't speak English.

We want a local build step that takes screenshots of each 'card' itself, so that a user can rapidly save the 'card' for offline usage, to their phone. That local build step is run before we push the code to github. It could be a pre-commit hook.

## Address Card Format

```
Header: [Icon representing type] Hi, I need to go to this address! (こんにちは、この住所へ行きたいです)

Type: HOTEL / ホテル (Prominent)

Layout: Side-by-side columns (Left: Japanese, Right: English)

Column Headers: Japanese | English

destination (<small gray hint>)
<Japanese Name> | <English Name>

Address (<small gray hint>)
<Japanese Address> | <English Address>

[Google Maps Link] (Prominent link below header)
```

## Itinerary Integration

We process itinerary PDFs (`call_iteniary.pdf`, `edwards_iteniary.pdf`) into a consolidated `iteniary.md` database. This data drives the list of addresses.

## Site Structure

*   **Home:** 'The Call and Edwards 2025 Japan Trip!', with a cherry-blossom graphic.
*   **Itinerary:** A table listing key locations from the itinerary, associated family (Call, Edwards, or Both), dates, and a direct Google Maps link.
    *   **Table Columns:** Location (Type: Name), Family, Date(s).
    *   **Links:** Clicking the location name (if a card exists) goes to the detailed Address Card.
    *   **Google Maps:** Each row has a direct link to Google Maps.
*   **Suggestions:** A table listing suggested activities and locations not strictly on the scheduled itinerary.
    *   **Table Columns:** Location, Description (with Google Maps link in Location column).

## Current Status

*   Project scaffolded with HTML/CSS.
*   `call_iteniary.pdf` and `edwards_iteniary.pdf` converted to Markdown.
*   `iteniary.md` created as a consolidated database of locations and map links.
*   `src/itinerary.html` (formerly addresses.html) displays the itinerary table.
*   `src/suggestions.html` created to display suggestions (e.g., Akihabara Arcade).
*   Existing cards (`prince-park-tower.html`, `laundry-mammaciao.html`) updated with Google Maps links.
*   Screenshot generation script exists (`scripts/generate-screenshots.js`).

## Next Steps

*   Create more Address Cards for other key locations in `iteniary.md` and `suggestions.html`.
*   Refine the screenshot generation to handle the new map links (ensure they look good or are excluded if needed).
*   Verify mobile responsiveness of the new table.