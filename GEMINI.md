# Development Guidelines

## Building the Project
After making any UI changes in the `src` directory, you must synchronize them to the `docs` directory to see them in the final output.

To do this efficiently (skipping the slow image generation step), always run:

```bash
npm run build:quick
```

Use the standard `npm run build` only when you specifically need to regenerate the card screenshots.
