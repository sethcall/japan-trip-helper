# Development Guidelines

## Building the Project
After making any UI changes in the `src` directory, you must synchronize them to the `docs` directory to see them in the final output.

To do this efficiently (skipping the slow image generation step), always run:

```bash
npm run build:quick
```

Use the standard `npm run build` only when you specifically need to regenerate the card screenshots.

### Walkables Updates
Any update to the Walkables sections should always check @WALKABLES_PRINCE_PARK.md (and any other WALKABLES_ files found in the future) for the core list of what should be added to the walkables around Prince Park Hotel.
