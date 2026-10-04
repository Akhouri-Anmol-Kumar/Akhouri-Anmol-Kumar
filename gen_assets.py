"""AKHOURI SYSTEMS profile README asset generator.
Edit the CONFIG block, run `python gen_assets.py`, commit the files in ./assets to your profile repo."""
import os, sys, textwrap
from xml.sax.saxutils import escape as esc

# ───────────── CONFIG ─────────────
DOWNLOADS = int(os.environ.get("DOWNLOADS", 967))   # auto-set by the GitHub Action; 967 is only the fallback
GOAL      = int(os.environ.get("GOAL", 1000))        # v5 unlocks at this many
PREVIEW   = os.environ.get("PREVIEW") == "1"   # static render for previews
OUT       = "assets"
# ──────────────────────────────────
BG, PANEL, GOLD, BRIGHT, DIM = "#050505", "#0a0a0a", "#B8935F", "#E8C98A", "#8a6c3f"
TEXT, MUTED, GREEN, RED = "#EDE6D6", "#6f685c", "#3fb97a", "#e05c4a"
F = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"
W = 830
os.makedirs(OUT, exist_ok=True)

def save(name, body, w, h, css=""):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{F}">'
           f'<style>{css if not PREVIEW else ""}</style>{body}</svg>')
    open(f"{OUT}/{name}.svg", "w", encoding="utf-8").write(svg)

def fade(delay):  # staggered reveal, disabled for static previews
    return "" if PREVIEW else f'class="rv" style="animation-delay:{delay}s"'

COMMON_CSS = """
.rv{opacity:0;animation:rv .5s ease forwards}
@keyframes rv{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}
.bl{animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}
.pu{animation:pu 3s ease-in-out infinite}@keyframes pu{50%{stroke-opacity:.9}}
"""

def cut_path(w, h, c=14):
    return f"M0.5,0.5 L{w-c},0.5 L{w-0.5},{c} L{w-0.5},{h-0.5} L0.5,{h-0.5} Z"

def brackets(w, h, s=14, col=BRIGHT):
    return (f'<path d="M1,{s} V1 H{s}" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<path d="M{w-s},{h-1} H{w-1} V{h-s}" fill="none" stroke="{col}" stroke-width="2"/>')

DEFS = f"""<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d0c09"/><stop offset="1" stop-color="#060606"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{DIM}"/><stop offset=".5" stop-color="{BRIGHT}"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#B8935F" stroke-opacity=".05"/></pattern>
</defs>"""

# ───────────── HERO ─────────────
def hero():
    h = 340
    css = COMMON_CSS + """
.gl1{animation:g1 5s infinite steps(1)}.gl2{animation:g2 5s infinite steps(1)}
@keyframes g1{0%,92%,100%{transform:translate(-3px,0)}93%{transform:translate(-7px,1px)}95%{transform:translate(2px,-1px)}}
@keyframes g2{0%,92%,100%{transform:translate(3px,0)}93%{transform:translate(8px,-1px)}95%{transform:translate(-2px,1px)}}
.scan{animation:sc 6s linear infinite}@keyframes sc{from{transform:translateY(-20px)}to{transform:translateY(360px)}}
"""
    t = lambda y, txt, d, col=TEXT, size=14, w="normal": f'<text x="44" y="{y}" font-size="{size}" fill="{col}" font-weight="{w}" {fade(d)}>{txt}</text>'
    title = "AKHOURI SYSTEMS"
    body = f"""{DEFS}
<rect width="{W}" height="{h}" fill="{BG}"/><rect width="{W}" height="{h}" fill="url(#grid)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>
{brackets(W,h,18)}
<rect y="0" width="{W}" height="34" fill="{GOLD}" fill-opacity=".07"/>
<line x1="0" y1="34" x2="{W}" y2="34" stroke="{GOLD}" stroke-opacity=".4"/>
<text x="20" y="22" font-size="11" fill="{GOLD}" letter-spacing="1.5">SYS://AKHOURI-SYSTEMS // NODE:RANCHI</text>
<circle cx="{W-318}" cy="17" r="4" fill="{GREEN}"/>
<text x="{W-20}" y="22" font-size="11" fill="{MUTED}" text-anchor="end" letter-spacing="1">ONLINE · OFFLINE-FIRST · 4 APPS SHIPPED</text>
{t(72,"$ whoami",0.2,GREEN)}
<g filter="url(#glow)">
<text class="gl1" x="44" y="148" font-size="58" font-weight="800" fill="{DIM}" letter-spacing="3" opacity=".85">{title}</text>
<text class="gl2" x="44" y="148" font-size="58" font-weight="800" fill="#ffffff" letter-spacing="3" opacity=".35">{title}</text>
<text x="44" y="148" font-size="58" font-weight="800" fill="url(#gold)" letter-spacing="3">{title}</text></g>
{t(196,'<tspan fill="'+GOLD+'">&gt;&gt;</tspan> founder · software engineer · ranchi, india',0.9,TEXT)}
{t(220,'<tspan fill="'+GOLD+'">&gt;&gt;</tspan> building free desktop tools that never phone home',1.3,TEXT)}
{t(244,'<tspan fill="'+GOLD+'">&gt;&gt;</tspan> shipping under <tspan fill="'+BRIGHT+'" font-weight="bold">AKHOURI SYSTEMS</tspan> — we build what others forgot to fix',1.7,TEXT)}
{t(284,'$ <tspan class="bl" fill="'+BRIGHT+'">█</tspan>',2.1,GREEN)}
<rect class="scan" x="1" y="34" width="{W-2}" height="14" fill="{GOLD}" opacity=".035"/>
<text x="{W-24}" y="{h-18}" font-size="10" fill="{MUTED}" text-anchor="end">// your machine · your data · your control</text>"""
    save("hero", body, W, h, css)

# ───────────── SECTION HEADERS ─────────────
def header(name, title, num, cmd):
    h = 70
    body = f"""<text x="2" y="30" font-size="22" font-weight="800" fill="{GOLD}">~/<tspan fill="#ffffff">{title}</tspan></text>
<text x="{W-2}" y="28" font-size="12" fill="{MUTED}" text-anchor="end">// {num}</text>
<line x1="2" y1="42" x2="{W-2}" y2="42" stroke="{GOLD}" stroke-opacity=".25"/>
<line x1="2" y1="42" x2="120" y2="42" stroke="{BRIGHT}" stroke-width="2"/>
<text x="4" y="64" font-size="13" fill="{MUTED}"><tspan fill="{GREEN}">$</tspan> {esc(cmd)}</text>"""
    save(f"h_{name}", body, W, h)

# ───────────── LINK CARDS ─────────────
def link_card(name, label, handle, glyph):
    w, h = 160, 56
    body = f"""{DEFS}<path d="{cut_path(w,h,10)}" fill="url(#g)" stroke="{GOLD}" stroke-opacity=".4" class="pu"/>
{brackets(w,h,8)}
<rect x="14" y="13" width="26" height="26" rx="5" fill="{GOLD}" fill-opacity=".14" stroke="{GOLD}" stroke-opacity=".5"/>
<text x="27" y="31" font-size="12" font-weight="800" fill="{BRIGHT}" text-anchor="middle">{glyph}</text>
<text x="50" y="25" font-size="13" font-weight="800" fill="{TEXT}">{label}</text>
<text x="50" y="42" font-size="9.5" fill="{MUTED}">{esc(handle)}</text>"""
    save(f"l_{name}", body, w, h, COMMON_CSS)

# ───────────── APP CARDS ─────────────
def app_card(name, title, tagline, desc, tags, status, status_col, idx):
    w, h = 408, 204
    lines = textwrap.wrap(desc, 47)[:3]
    d = "".join(f'<text x="22" y="{124+i*18}" font-size="12" fill="{TEXT}" fill-opacity=".85">{esc(l)}</text>' for i, l in enumerate(lines))
    tx, tag_svg = 22, ""
    for tg in tags:
        tw = len(tg) * 6.6 + 18
        tag_svg += (f'<rect x="{tx}" y="172" width="{tw}" height="20" rx="3" fill="none" stroke="{GOLD}" stroke-opacity=".45"/>'
                    f'<text x="{tx+tw/2}" y="186" font-size="9.5" fill="{GOLD}" text-anchor="middle" letter-spacing=".5">{esc(tg.upper())}</text>')
        tx += tw + 8
    sw = len(status) * 6.4 + 20
    body = f"""{DEFS}<path d="{cut_path(w,h,18)}" fill="url(#g)" stroke="{GOLD}" stroke-opacity=".4" class="pu"/>
{brackets(w,h,12)}
<text x="22" y="34" font-size="10" fill="{MUTED}" letter-spacing="2">APP // 0{idx}</text>
<rect x="{w-sw-38}" y="18" width="{sw}" height="20" rx="3" fill="{status_col}" fill-opacity=".12" stroke="{status_col}" stroke-opacity=".6"/>
<text x="{w-sw/2-38}" y="32" font-size="9.5" font-weight="800" fill="{status_col}" text-anchor="middle" letter-spacing="1">{esc(status)}</text>
<text x="22" y="68" font-size="27" font-weight="800" fill="url(#gold)" filter="url(#glow)">{esc(title)} <tspan fill="{GOLD}" font-size="15" fill-opacity=".9">↗</tspan></text>
<text x="22" y="90" font-size="11" fill="{BRIGHT}" fill-opacity=".8">{esc(tagline)}</text>
<line x1="22" y1="102" x2="{w-22}" y2="102" stroke="{GOLD}" stroke-opacity=".15"/>
{d}{tag_svg}"""
    save(f"app_{name}", body, w, h, COMMON_CSS)

# ───────────── STATUS (v5 progress) ─────────────
def status():
    h = 190; pct = min(DOWNLOADS / GOAL, 1); bw = W - 88; left = max(GOAL - DOWNLOADS, 0)
    css = COMMON_CSS + f".bar{{transform-box:fill-box;transform-origin:left;animation:fill 2.2s cubic-bezier(.2,.8,.2,1) forwards}}@keyframes fill{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}"
    done = DOWNLOADS >= GOAL
    togo = "GOAL REACHED" if done else f"{left} to go"
    v5_txt = "v5 UNLOCKED" if done else "v5 LOCKED"
    v5_dot = (f'<circle cx="{W-108}" cy="38" r="4" fill="{GREEN}"/>' if done
              else f'<circle cx="{W-108}" cy="38" r="4" fill="none" stroke="{RED}" stroke-width="1.5"/>')
    msg = (f'<tspan fill="{BRIGHT}">Goal reached. v5 is unlocked. Release incoming.</tspan>' if done
           else f'v5 ships the moment the bar fills. <tspan fill="{BRIGHT}">Be one of the {left}.</tspan>')
    ticks = "".join(f'<line x1="{44+bw*i/10:.1f}" y1="112" x2="{44+bw*i/10:.1f}" y2="120" stroke="{GOLD}" stroke-opacity=".4"/>' for i in range(11))
    body = f"""{DEFS}<rect width="{W}" height="{h}" fill="{BG}"/><rect width="{W}" height="{h}" fill="url(#grid)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>{brackets(W,h,16)}
<text x="44" y="42" font-size="11" fill="{MUTED}" letter-spacing="2">LAUNCH SEQUENCE // ATLOCK v5</text>
<circle cx="{W-196}" cy="38" r="4" fill="{GREEN}"/><text x="{W-186}" y="42" font-size="11" fill="{GOLD}" letter-spacing="1">v4.0 LIVE</text>
{v5_dot}<text x="{W-98}" y="42" font-size="11" fill="{GOLD}" letter-spacing="1">{v5_txt}</text>
<text x="44" y="82" font-size="30" font-weight="800" fill="url(#gold)" filter="url(#glow)">{DOWNLOADS}<tspan fill="{MUTED}" font-size="18"> / {GOAL}</tspan><tspan fill="{TEXT}" font-size="13" font-weight="normal">  downloads</tspan></text>
<text x="{W-44}" y="82" font-size="14" fill="{BRIGHT}" text-anchor="end" font-weight="bold">{togo}</text>
<rect x="44" y="94" width="{bw}" height="14" rx="3" fill="#111" stroke="{GOLD}" stroke-opacity=".35"/>
<rect class="bar" x="44" y="94" width="{bw*pct:.1f}" height="14" rx="3" fill="url(#gold)"/>
{ticks}
<text x="44" y="146" font-size="12.5" fill="{MUTED}"><tspan fill="{GREEN}">$</tspan> ./release --when downloads&gt;={GOAL}</text>
<text x="44" y="168" font-size="12.5" fill="{TEXT}">{msg} <tspan class="bl" fill="{BRIGHT}">█</tspan></text>"""
    save("status", body, W, h, css)

# ───────────── ZERO COUNTERS ─────────────
def zero():
    h = 112; tiles = [("TELEMETRY","0","bytes sent home"),("CLOUD","0","servers required"),("SUBSCRIPTIONS","0","monthly fees"),("ADS","0","trackers and banners"),("PRICE","$0","free to download")]
    tw, gap = 154, 15; body = DEFS
    for i, (a, v, s) in enumerate(tiles):
        x = i * (tw + gap)
        body += (f'<g transform="translate({x},0)"><path d="{cut_path(tw,h,12)}" fill="url(#g)" stroke="{GOLD}" stroke-opacity=".4"/>{brackets(tw,h,8)}'
                 f'<text x="16" y="28" font-size="9.5" fill="{MUTED}" letter-spacing="2">{a}</text>'
                 f'<text x="16" y="70" font-size="38" font-weight="800" fill="url(#gold)" filter="url(#glow)">{v}</text>'
                 f'<text x="16" y="94" font-size="10" fill="{MUTED}">{s}</text></g>')
    save("zero", body, W, h, COMMON_CSS)

# ───────────── STACK ─────────────
def stack():
    rows = [("language", ["Python"]), ("ui", ["CustomTkinter","Tkinter","Pillow"]),
            ("crypto", ["Argon2id","AES-256-GCM","HKDF","TOTP","FIDO2"]),
            ("platform", ["Windows","pywin32","OpenCV","Windows Hello"])]
    h = 24 + len(rows) * 40 + 14; body = ""
    for r, (lab, items) in enumerate(rows):
        y = 24 + r * 40; body += f'<text x="4" y="{y+19}" font-size="12" fill="{MUTED}">{lab}  ›</text>'; x = 118
        for it in items:
            tw = len(it) * 7.4 + 22
            body += (f'<path d="M{x},{y} H{x+tw-7} L{x+tw},{y+7} V{y+28} H{x} Z" fill="{GOLD}" fill-opacity=".07" stroke="{GOLD}" stroke-opacity=".55"/>'
                     f'<text x="{x+tw/2}" y="{y+19}" font-size="12" font-weight="bold" fill="{BRIGHT}" text-anchor="middle">{it}</text>')
            x += tw + 10
    save("stack", body, W, h, COMMON_CSS)

# ───────────── FOOTER ─────────────
def footer():
    h = 110
    body = f"""{DEFS}<rect width="{W}" height="{h}" fill="{BG}"/><rect width="{W}" height="{h}" fill="url(#grid)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>{brackets(W,h,14)}
<text x="44" y="42" font-size="13" fill="{MUTED}"><tspan fill="{GREEN}">$</tspan> echo $PHILOSOPHY</text>
<text x="44" y="78" font-size="22" font-weight="800" fill="url(#gold)" filter="url(#glow)">your machine. your data. your control.<tspan class="bl" fill="{BRIGHT}"> █</tspan></text>"""
    save("footer", body, W, h, COMMON_CSS)

hero()
for n, t, i, c in [("links","links","01","ping akhouri --all-channels"),("apps","apps","02","ls -l ~/apps"),
                   ("status","status","03","systemctl status akhouri-systems"),("stack","stack","04","scan --loadout atlock")]:
    header(n, t, i, c)
for n, l, hd, g in [("website","WEBSITE","akhouri-systems","WWW"),("blog","BLOG","@akhourianmolkumar","DEV"),
                    ("linkedin","LINKEDIN","in/akhourianmolkumar","in"),("peerlist","PEERLIST","@akhourianmol","PL"),
                    ("instagram","INSTAGRAM","@aak31_anmol","IG")]:
    link_card(n, l, hd, g)
app_card("atlock","ATLOCK","Desktop Security Suite","System lockdown, file guard and an Argon2id password vault. All offline, all yours.",["Windows","Vault","2FA"],"v4 LIVE · v5 SOON",GOLD,1)
app_card("apic","APIC","Advanced Image Processing Center","Edit, convert, compress and batch-search images without touching the cloud.",["Edit","Convert","Compress","Batch"],"LIVE",GREEN,2)
app_card("anote","ANOTE","Premium Lightweight Notes","Fast, private note-taking that lives in a single portable window.",["Multi-tab","Syntax","Lock","Auto-save"],"LIVE",GREEN,3)
app_card("acalcu","ACALCU","Most Customizable Calculator","Every button, every layout, every behavior, built to be reshaped by you.",["Custom","Portable","Zero bloat"],"LIVE",GREEN,4)
status(); zero(); stack(); footer()
print("ok", len(os.listdir(OUT)), "files")
