# Master Plan

We are creating a static site web app, that uses github pages to publish.  

This repository is a github repositiory. 

Most pages of this app will be single-purpose pages that are, for example, something I'd show to a Japanese taxi driver who doesn't speak English.

We want a local build step that takes screenshots of each 'card' itself, so that a user can rapidly save the the 'card' for offline usage, to their phone.  That local build step is run before we push the code to github.   It could be a pre-commit hook.

Here's the first card, the 'Address' card format.  This description will mix an example address, along with the general format we should always use for a address card'.

```
At the top of the card, title it with this, in Japanase!  

'Hi, I need to go to this address!'

And then the actual name and address in this format:

Location: The Prince Park Tower Tokyo
Address: Japanese: 4-8-1 Shibakoen, Minato City, Tokyo 105-8563, Japan,


I believe this is the name of the hotel (location) The Prince Park Tower Tokyo ザ・プリンス パークタワー東京


I want the format to be:

Header: [Icon representing type] Hi, I need to go to this address!

Type: HOTEL / ホテル (Prominent)

Layout: Side-by-side columns (Left: Japanese, Right: English)

Column Headers: Japanese | English

destination (<small gray hint>)
<Japanese Name> | <English Name>

Address (<small gray hint>)
<Japanese Address> | <English Address>
```


## First Prompt

So let's generate the project using this; the left nav should have 'Addresses', and when you select it, all Address Cards available show up on a list in the main content window, and finally we have the one option. Prince Park Toyko as an option, and when you click it, you should have the 'Address Card' format, and, too, an image you can download that an image capture of the exact contents of the address card.

The main page of the site, in Enlgish, and then Japanese, should say:

'The Call and Edwards 2025 Japan Trip!', with a cherry-blossom graphic.