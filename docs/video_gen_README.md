# Veo 3 Video Generation Integration

Part of 26-system CRM build - System #19

## Overview

Integrates Google's Veo 3 API for AI-powered video generation from text prompts or images.

**Use Cases:**
- Thumbnails and teaser videos
- Social media content
- Visual assets on demand
- Product showcases
- Marketing materials

## Setup

### 1. Install Dependencies

```bash
pip install requests
```

### 2. Configure API Key

Create `~/.openclaw/config/gemini.json` with your Veo API key:

```json
{
  "api_key": "your-veo-api-key-here",
  "model": "veo-3.0",
  "endpoint": "https://generativelanguage.googleapis.com/v1beta/models",
  "max_duration": 4,
  "default_resolution": "1080p",
  "supported_resolutions": ["720p", "1080p", "4k"],
  "generation_options": {
    "aspect_ratio": "16:9",
    "style": "realistic",
    "motion": "smooth"
  }
}
```

**Note:** Veo 3 API is currently in preview. Get access at https://ai.google.dev/veo

### 3. Deploy Script

```bash
cp video_gen.py ~/.openclaw/bin/video_gen.py
chmod +x ~/.openclaw/bin/video_gen.py
```

### 4. Ensure Output Directory Exists

```bash
mkdir -p ~/.openclaw/workspace/generated/videos
```

## Usage

### Text to Video

Generate video from text prompt:

```bash
~/.openclaw/bin/video_gen.py --prompt "A serene sunset over mountains with birds flying"
```

With custom settings:

```bash
~/.openclaw/bin/video_gen.py \
  --prompt "Cyberpunk city at night with neon lights" \
  --duration 3 \
  --resolution 720p \
  --style cinematic
```

### Image to Video

Animate an existing image:

```bash
~/.openclaw/bin/video_gen.py \
  --image input.png \
  --prompt "Zoom in slowly on the main subject"
```

Image to video with specific style:

```bash
~/.openclaw/bin/video_gen.py \
  --image thumbnail.jpg \
  --prompt "Add smooth cinematic camera movement" \
  --duration 4 \
  --style cinematic \
  --output-prefix thumbnail_anim
```

### List Generated Videos

```bash
~/.openclaw/bin/video_gen.py --list-output
```

## Options

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `--prompt`, `-p` | Text prompt for video | Required | - |
| `--image`, `-i` | Input image path | Optional | - |
| `--duration`, `-d` | Duration in seconds | 4 | 1, 2, 3, 4 |
| `--resolution`, `-r` | Video resolution | 1080p | 720p, 1080p, 4k |
| `--aspect-ratio` | Aspect ratio | 16:9 | 16:9, 9:16, 1:1 |
| `--style` | Generation style | realistic | Any text |
| `--output-prefix` | Filename prefix | veo | - |
| `--list-output` | List all generated videos | - | - |

## Output

Videos are saved to: `~/.openclaw/workspace/generated/videos/`

Filenames use timestamp format: `{prefix}_{YYYYMMDD_HHMMSS}.mp4`

Example: `veo_20260217_201845.mp4`

## Integration Notes

### API Status

⚠️ **Veo 3 API Integration Pending**

The current implementation includes placeholder API calls. Once Google releases the official Veo 3 API endpoints, update the following methods in `video_gen.py`:

- `_call_veo_api()` - Text-to-video generation
- `_call_veo_api_image()` - Image-to-video generation

Reference: https://ai.google.dev/veo

### Example API Integration Pattern

```python
def _call_veo_api(self, config: Dict[str, Any]) -> bytes:
    headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{self.endpoint}/veo-3.0:generateVideo",
        json=config,
        headers=headers,
        timeout=120
    )
    response.raise_for_status()

    # Parse response and extract video data
    return response.content
```

## System Requirements

- Python 3.7+
- Veo 3 API access (Google AI)
- Network connectivity
- Storage space for video files

## Troubleshooting

### "API key not found in config"

Check that `~/.openclaw/config/gemini.json` exists and contains a valid `api_key`.

### "Config file not found"

Create the config directory and file:

```bash
mkdir -p ~/.openclaw/config
# Add your config to gemini.json
```

### "Image not found"

Verify the image path is correct and the file exists.

## Development Notes

**Status:** Ready for API integration
**Priority:** High (CRM System #19)
**Dependencies:** requests
**Output:** MP4 video files

---

Built for the 26-system CRM project.
