import json
from simpleicons.all import icons

requested = [
    ('proxmox', 'Proxmox'),
    ('cloudflare', 'Cloudflare'),
    ('drf', 'Django REST'),
    ('redis', 'Redis'),
    ('celery', 'Celery'),
    ('githubactions', 'GitHub Actions'),
    ('codemagic', 'Codemagic'),
    ('termux', 'Termux')
]

bg_color = "#242938"

for slug, name in requested:
    # Base container
    elem = f'<svg width="48" height="48" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">\n'
    elem += f'    <rect width="256" height="256" fill="{bg_color}" rx="60"/>\n'
    
    # Glossy effect overlay (Glassmorphism highlight)
    elem += f'    <path fill="rgba(255,255,255,0.05)" d="M0 60 Q0 0 60 0 L196 0 Q256 0 256 60 L256 128 Q128 100 0 128 Z"/>\n'
    
    # Inner logo
    if slug == 'drf':
        # Custom DRF Text logo
        elem += f'    <text x="128" y="150" font-family="Arial, sans-serif" font-size="80" font-weight="bold" fill="#A30000" text-anchor="middle">DRF</text>\n'
    elif slug == 'termux':
        # Termux custom >_
        elem += f'    <text x="128" y="150" font-family="Consolas, monospace" font-size="100" font-weight="bold" fill="#FFFFFF" text-anchor="middle">&gt;_</text>\n'
    else:
        # Get from simpleicons
        icon = icons.get(slug)
        if icon:
            color = "#" + icon.hex
            path = icon.path
            # Put the path in a centered nested SVG
            elem += f'    <svg x="48" y="48" width="160" height="160" viewBox="0 0 24 24" fill="{color}">\n'
            elem += f'      <path d="{path}"/>\n'
            elem += f'    </svg>\n'
        else:
            # Fallback
            elem += f'    <text x="128" y="150" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{name}</text>\n'

    elem += f'</svg>\n'
    
    with open(f"m:/mido-ghanam/{slug}_icon.svg", "w", encoding="utf-8") as f:
        f.write(elem)
