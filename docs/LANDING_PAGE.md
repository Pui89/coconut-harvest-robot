# Landing Page Banner

A polished landing page banner for the coconut harvest robot project.

```svg name=coconut_harvest_landing.svg
<svg width="1400" height="500" viewBox="0 0 1400 500" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad_bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="grad_accent" x1="0" x2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="grad_highlight" x1="0" x2="1">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="1400" height="500" fill="url(#grad_bg)"/>

  <!-- Decorative background elements -->
  <circle cx="100" cy="100" r="150" fill="url(#grad_accent)" opacity="0.1"/>
  <circle cx="1300" cy="400" r="200" fill="url(#grad_highlight)" opacity="0.08"/>

  <!-- Left content -->
  <g>
    <text x="60" y="80" font-size="56" font-weight="bold" fill="#f1f5f9" font-family="Arial, sans-serif">
      Coconut Harvest
    </text>
    <text x="60" y="145" font-size="56" font-weight="bold" fill="#f1f5f9" font-family="Arial, sans-serif">
      Robot
    </text>

    <text x="60" y="190" font-size="20" fill="#cbd5e1" font-family="Arial, sans-serif">
      Vision-based autonomous harvesting for high-canopy trees
    </text>

    <!-- Features -->
    <g>
      <circle cx="80" cy="250" r="6" fill="url(#grad_accent)"/>
      <text x="105" y="256" font-size="16" fill="#e2e8f0" font-family="Arial, sans-serif">Real-time coconut detection</text>

      <circle cx="80" cy="290" r="6" fill="url(#grad_highlight)"/>
      <text x="105" y="296" font-size="16" fill="#e2e8f0" font-family="Arial, sans-serif">3D spatial reasoning &amp; planning</text>

      <circle cx="80" cy="330" r="6" fill="url(#grad_accent)"/>
      <text x="105" y="336" font-size="16" fill="#e2e8f0" font-family="Arial, sans-serif">Collision-free motion control</text>

      <circle cx="80" cy="370" r="6" fill="url(#grad_highlight)"/>
      <text x="105" y="376" font-size="16" fill="#e2e8f0" font-family="Arial, sans-serif">Production-ready PyTorch code</text>
    </g>

    <!-- CTA Button -->
    <rect x="60" y="430" width="200" height="50" rx="8" fill="url(#grad_accent)" filter="url(#glow)"/>
    <text x="160" y="465" text-anchor="middle" font-size="18" fill="#0f172a" font-weight="bold" font-family="Arial, sans-serif">Get Started</text>
  </g>

  <!-- Right side: simple robot diagram -->
  <g>
    <!-- Tree -->
    <rect x="1080" y="120" width="40" height="180" rx="12" fill="#7e4f2a"/>
    <circle cx="1100" cy="100" r="50" fill="#34d399"/>
    <circle cx="1130" cy="120" r="50" fill="#2dbf71"/>
    <circle cx="1060" cy="130" r="48" fill="#1fb36b"/>

    <!-- Coconuts -->
    <circle cx="1100" cy="155" r="12" fill="#f9c464"/>
    <circle cx="1130" cy="180" r="14" fill="#f9c464"/>
    <circle cx="1070" cy="190" r="12" fill="#f9c464"/>

    <!-- Robot -->
    <rect x="920" y="310" width="140" height="60" rx="12" fill="#64748b"/>
    <rect x="975" y="270" width="60" height="45" rx="8" fill="#dfe7f2"/>
    <circle cx="960" cy="375" r="20" fill="#1f2937"/>
    <circle cx="1020" cy="375" r="20" fill="#1f2937"/>

    <!-- Arm -->
    <path d="M 1005 280 L 1080 180" stroke="#64748b" stroke-width="10" stroke-linecap="round" fill="none"/>
    <circle cx="1080" cy="180" r="8" fill="#fbbf24"/>
  </g>

  <!-- Stats bar at bottom -->
  <rect x="0" y="460" width="1400" height="40" fill="#0f172a" opacity="0.8"/>
  <g font-family="Arial, sans-serif">
    <text x="100" y="490" font-size="14" fill="#cbd5e1">92% Detection Accuracy</text>
    <text x="400" y="490" font-size="14" fill="#cbd5e1">~24s per Coconut</text>
    <text x="750" y="490" font-size="14" fill="#cbd5e1">Production Ready</text>
    <text x="1100" y="490" font-size="14" fill="#cbd5e1">Real Orchard Support</text>
  </g>
</svg>
```

## GitHub README Banner (1200x400)

```svg name=coconut_harvest_readme_banner.svg
<svg width="1200" height="400" viewBox="0 0 1200 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg_banner" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="accent_banner" x1="0" x2="1">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="400" fill="url(#bg_banner)"/>

  <!-- Title section -->
  <text x="60" y="70" font-size="48" font-weight="bold" fill="#f1f5f9" font-family="Arial, sans-serif">
    Coconut Harvest Robot
  </text>
  <text x="60" y="130" font-size="22" fill="#cbd5e1" font-family="Arial, sans-serif">
    Vision-based autonomous harvesting • Real orchard support • Production code
  </text>

  <!-- Key features -->
  <g font-family="Arial, sans-serif" font-size="16" fill="#cbd5e1">
    <text x="60" y="190">✓ Real-time coconut detection (92% mAP)</text>
    <text x="60" y="225">✓ 3D spatial planning &amp; collision avoidance</text>
    <text x="60" y="260">✓ Trajectory generation for robot arm</text>
    <text x="60" y="295">✓ RGB-D and LiDAR data support</text>
  </g>

  <!-- Right side accent -->
  <rect x="900" y="0" width="300" height="400" fill="url(#accent_banner)" opacity="0.15"/>
  <text x="1000" y="180" text-anchor="middle" font-size="60" fill="#06b6d4" opacity="0.3" font-family="Arial, sans-serif">🤖</text>
</svg>
```

You can embed these in your GitHub README like:

```markdown
![Coconut Harvest Robot Banner](docs/images/coconut_harvest_landing.svg)
```
