# Nano Banana - Image Generation Integration

**System #18 of 26 - CRM Build**

Nano Banana integrates Google Gemini's image generation API to create, edit, and compose images on demand.

## Features

✨ **Text-to-Image Generation**
- Create images from text prompts
- Support for multiple resolutions (512x512 to 4K 3840x2160)
- Generate 1-4 images at once
- PNG and JPEG output formats

🎨 **Image Editing**
- Edit existing images with text instructions
- Optional mask support for precise edits
- Maintain or change resolution

🖼️ **Image Composition**
- Combine up to 14 images at once
- Grid, collage, or overlay layouts
- Intelligent composition via AI

📐 **Upscaling**
- Upscale images to higher resolutions
- AI-enhanced upscaling (up to 4K)
- Fallback to standard resize

## Installation

```bash
# Run the installation script
./install_image_gen.sh
```

This will:
- Create necessary directories
- Copy `image_gen.py` to `~/.openclaw/bin/`
- Copy `gemini.json` config to `~/.openclaw/workspace/config/`
- Install Python dependencies (google-generativeai, Pillow, requests)

## Configuration

Edit `~/.openclaw/workspace/config/gemini.json`:

```json
{
  "api_key": "YOUR_GEMINI_API_KEY_HERE",
  "model": "gemini-2.0-flash-exp-image-generation",
  "default_resolution": "1024x1024",
  "default_format": "png"
}
```

Get your API key from: https://ai.google.dev/

## CLI Usage

### Generate Image

```bash
# Basic
~/.openclaw/bin/image_gen.py generate "A sunset over mountains"

# With resolution
~/.openclaw/bin/image_gen.py generate "A cyberpunk city" --resolution 1920x1080

# Multiple images
~/.openclaw/bin/image_gen.py generate "Abstract art" --count 4 --resolution 1024x1024

# Different format
~/.openclaw/bin/image_gen.py generate "Portrait of a woman" --format jpeg
```

### Edit Image

```bash
# Basic edit
~/.openclaw/bin/image_gen.py edit photo.jpg "Make it look like winter"

# With mask for precise editing
~/.openclaw/bin/image_gen.py edit photo.jpg "Replace the sky with clouds" --mask mask.png

# With resolution change
~/.openclaw/bin/image_gen.py edit photo.jpg "Enhance details" --resolution 2048x2048
```

### Compose Images

```bash
# Compose two images
~/.openclaw/bin/image_gen.py compose img1.jpg img2.jpg "Create a side-by-side comparison"

# Collage multiple images
~/.openclaw/bin/image_gen.py compose *.jpg "Create a grid collage" --layout grid

# Overlay composition
~/.openclaw/bin/image_gen.py compose base.jpg overlay.png "Blend images together" --layout overlay
```

### Upscale Image

```bash
# Upscale to 1080p
~/.openclaw/bin/image_gen.py upscale photo.jpg 1920x1080

# Upscale to 4K
~/.openclaw/bin/image_gen.py upscale photo.jpg 3840x2160

# Upscale with format change
~/.openclaw/bin/image_gen.py upscale photo.png 2048x2048 --format jpeg
```

## Supported Resolutions

- `512x512` - Small thumbnails
- `768x768` - Medium size
- `1024x1024` - Standard (default)
- `1280x720` - HD landscape
- `1920x1080` - Full HD
- `2048x2048` - High-res square
- `3840x2160` - 4K UHD

## Output Files

All generated images are saved to:
```
~/.openclaw/workspace/generated/images/
```

Filename format: `[prefix]_[timestamp]_[resolution].[format]`

Examples:
- `gen_20260217_201730_1920x1080.png`
- `edited_20260217_201745_2048x2048.png`
- `composed_20260217_201800_1024x768.png`

## Use Cases

### Thumbnails
```bash
~/.openclaw/bin/image_gen.py generate "Professional product photography" --resolution 512x512
```

### Social Media Posts
```bash
~/.openclaw/bin/image_gen.py generate "Engaging social media graphic" --resolution 1920x1080
```

### Visual Assets
```bash
# Generate custom illustrations
~/.openclaw/bin/image_gen.py generate "Minimalist logo design" --resolution 2048x2048

# Edit existing assets
~/.openclaw/bin/image_gen.py edit banner.png "Add holiday theme"

# Create composites
~/.openclaw/bin/image_gen.py compose hero1.jpg hero2.jpg hero3.jpg "Landing page banner"
```

## API Usage (Python)

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path.home() / '.openclaw' / 'bin'))
from image_gen import NanoBanana

# Initialize
nb = NanoBanana()

# Generate image
paths = nb.generate_image(
    prompt="A serene mountain landscape at sunset",
    resolution="1920x1080",
    count=1
)

# Edit image
edited = nb.edit_image(
    image_path="photo.jpg",
    prompt="Add snow to the mountains",
    resolution="2048x2048"
)

# Compose images
composed = nb.compose_images(
    image_paths=["img1.jpg", "img2.jpg", "img3.jpg"],
    prompt="Create a balanced grid layout",
    resolution="1920x1080"
)

# Upscale to 4K
upscaled = nb.upscale_image(
    image_path="photo.jpg",
    target_resolution="3840x2160"
)
```

## Dependencies

- `google-generativeai` - Gemini API client
- `Pillow` - Image processing
- `requests` - HTTP requests

## Troubleshooting

### "API key not found"
- Add your Gemini API key to `~/.openclaw/workspace/config/gemini.json`
- Get key from https://ai.google.dev/

### "Missing dependency"
- Run: `pip3 install google-generativeai Pillow requests`

### "Unsupported resolution"
- Check supported resolutions in config file
- Use one of: 512x512, 768x768, 1024x1024, 1280x720, 1920x1080, 2048x2048, 3840x2160

### Image generation fails
- Check your internet connection
- Verify API key is valid
- Ensure you have API quota remaining

## Performance Tips

- Use lower resolutions for faster generation during testing
- Batch multiple image requests when possible
- Cache generated images for reuse
- Use composition instead of multiple generations when combining images

## License

Part of the 26-system CRM build. Internal use.

---

**Built for CRM System Integration • System #18**
