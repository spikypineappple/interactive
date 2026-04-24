#!/usr/bin/env python3
"""Build self-contained HTML for the ASG Cold Email Autopsy lead magnet."""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).parent / "interactive.html"

def b64(rel):
    p = ROOT / rel
    return base64.b64encode(p.read_bytes()).decode("ascii")

def read(rel):
    return (ROOT / rel).read_text()

LOGO_SVG = read("tenants/asg/assets/logo.svg")
EMAIL_CHAT_B64 = b64("assets/product/coaches/keenan/email-chat.png")

EMAIL_CHAT_CAPTION = "Keenan drafts an outbound email in seconds — and critiques the user's own idea when it's weak."

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Cold Email Autopsy — A Sales Growth Company</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {
    --asg-blue: #2098D1;
    --asg-red: #D10000;
    --asg-black: #000000;
    --asg-paper: #FFFFFF;
    --asg-grey: #F4F4F4;
    --asg-line: #1A1A1A;
    --asg-muted: #6E6E6E;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--asg-paper); color: var(--asg-black); font-family: 'Archivo', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
  body { overflow-x: hidden; }
  h1, h2, h3, .display { font-family: 'Archivo Black', 'Archivo', sans-serif; font-weight: 900; letter-spacing: -0.01em; line-height: 0.95; }
  .mono { font-family: 'JetBrains Mono', ui-monospace, Menlo, monospace; }
  .container { max-width: 1180px; margin: 0 auto; padding: 0 32px; }

  /* HEADER */
  header.topbar { display: flex; align-items: center; justify-content: space-between; padding: 22px 32px; border-bottom: 2px solid var(--asg-black); position: sticky; top: 0; background: #fff; z-index: 50; }
  .topbar .logo { width: 140px; height: auto; display: block; }
  .topbar .topright { font-family: 'Archivo', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: 0.05em; text-transform: uppercase; }
  .topbar .topright a { color: var(--asg-black); text-decoration: none; border-bottom: 2px solid var(--asg-red); padding-bottom: 2px; }

  /* HERO */
  .hero { padding: 80px 32px 60px; border-bottom: 2px solid var(--asg-black); position: relative; overflow: hidden; }
  .hero::before { content: ""; position: absolute; right: -120px; top: -120px; width: 480px; height: 480px; background: var(--asg-blue); border-radius: 50%; opacity: 0.08; }
  .hero::after { content: ""; position: absolute; left: -80px; bottom: -100px; width: 280px; height: 280px; background: var(--asg-red); border-radius: 50%; opacity: 0.08; }
  .hero-eyebrow { font-family: 'Archivo', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--asg-red); margin-bottom: 22px; }
  .hero h1 { font-size: clamp(48px, 8vw, 120px); margin: 0 0 28px; }
  .hero h1 .red { color: var(--asg-red); }
  .hero h1 .blue { color: var(--asg-blue); }
  .hero p.lede { font-size: clamp(18px, 1.6vw, 22px); max-width: 720px; line-height: 1.45; font-weight: 500; margin: 0 0 14px; }
  .hero p.lede strong { background: var(--asg-blue); color: #fff; padding: 1px 8px; }
  .hero .credit { font-family: 'Archivo', sans-serif; font-size: 13px; letter-spacing: 0.05em; text-transform: uppercase; color: var(--asg-muted); font-weight: 700; }

  /* TOOL */
  .tool { padding: 60px 32px 80px; background: var(--asg-grey); border-bottom: 2px solid var(--asg-black); }
  .tool-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  @media (max-width: 900px) { .tool-grid { grid-template-columns: 1fr; } }
  .tool-section h2 { font-size: 30px; margin: 0 0 14px; }
  .tool-section h2 .num { color: var(--asg-red); margin-right: 14px; }
  .tool-section p.muted { color: var(--asg-muted); font-size: 14px; margin: 0 0 18px; }

  .preset-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }
  .chip { font-family: 'Archivo', sans-serif; font-weight: 700; font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; padding: 9px 14px; border: 2px solid var(--asg-black); background: #fff; cursor: pointer; transition: all 0.15s; }
  .chip:hover { background: var(--asg-black); color: #fff; }
  .chip.active { background: var(--asg-red); color: #fff; border-color: var(--asg-red); }

  textarea.email-input { width: 100%; min-height: 260px; padding: 18px 18px; border: 2px solid var(--asg-black); background: #fff; font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.55; resize: vertical; outline: none; transition: border-color 0.2s; }
  textarea.email-input:focus { border-color: var(--asg-red); }
  .run-btn { display: inline-flex; align-items: center; gap: 12px; margin-top: 14px; padding: 18px 28px; background: var(--asg-red); color: #fff; border: 2px solid var(--asg-red); font-family: 'Archivo Black', sans-serif; font-size: 16px; letter-spacing: 0.06em; text-transform: uppercase; cursor: pointer; transition: transform 0.15s, background 0.15s; }
  .run-btn:hover { background: var(--asg-black); border-color: var(--asg-black); transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--asg-red); }
  .run-btn:active { transform: translate(0,0); box-shadow: none; }
  .run-btn .arrow { font-size: 22px; }

  /* GAUGE */
  .gauge-wrap { background: #fff; border: 2px solid var(--asg-black); padding: 26px 26px 22px; min-height: 100%; display: flex; flex-direction: column; }
  .gauge-svg { width: 100%; max-width: 460px; margin: 0 auto; display: block; }
  .gauge-label { display: flex; justify-content: space-between; font-family: 'Archivo Black', sans-serif; font-size: 13px; letter-spacing: 0.1em; margin-top: -8px; padding: 0 6px; }
  .gauge-label .pitch { color: var(--asg-red); }
  .gauge-label .probe { color: var(--asg-blue); }
  .score-readout { text-align: center; margin: 18px 0 8px; }
  .score-readout .num { font-family: 'Archivo Black', sans-serif; font-size: 56px; line-height: 1; transition: color 0.3s; }
  .score-readout .num.bad { color: var(--asg-red); }
  .score-readout .num.good { color: var(--asg-blue); }
  .score-readout .num.neutral { color: var(--asg-black); }
  .score-readout .label { font-family: 'Archivo', sans-serif; font-weight: 700; font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--asg-muted); margin-top: 4px; }

  .feed { margin-top: 14px; border-top: 1px solid #e5e5e5; padding-top: 14px; min-height: 110px; }
  .feed-empty { color: var(--asg-muted); font-size: 13px; font-style: italic; }
  .ann { display: flex; gap: 10px; padding: 9px 0; border-bottom: 1px dashed #e5e5e5; animation: pop 0.4s cubic-bezier(.2,.8,.2,1.2); }
  .ann:last-child { border-bottom: none; }
  .ann .badge { flex: 0 0 auto; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Archivo Black', sans-serif; font-size: 12px; line-height: 1; color: #fff; margin-top: 2px; }
  .ann .badge.bad { background: var(--asg-red); }
  .ann .badge.good { background: var(--asg-blue); }
  .ann .badge.neu { background: #999; }
  .ann .text { font-size: 14px; line-height: 1.4; }
  .ann .text .quote { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--asg-muted); display: block; margin-top: 2px; }
  @keyframes pop { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }

  /* HIGHLIGHTING in textarea — handled with overlay */
  .editor-stack { position: relative; }
  .editor-overlay { position: absolute; inset: 0; padding: 18px 18px; pointer-events: none; font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.55; white-space: pre-wrap; word-wrap: break-word; color: transparent; overflow: hidden; }
  .editor-overlay mark { padding: 1px 3px; margin: -1px -3px; border-radius: 2px; }
  .editor-overlay mark.bad { background: rgba(209, 0, 0, 0.18); border-bottom: 2px solid var(--asg-red); color: transparent; }
  .editor-overlay mark.good { background: rgba(32, 152, 209, 0.18); border-bottom: 2px solid var(--asg-blue); color: transparent; }
  .editor-overlay mark.scan { background: rgba(0,0,0,0.12); animation: scan 0.5s ease; }
  @keyframes scan { 0% { background: rgba(0,0,0,0); } 50% { background: rgba(0,0,0,0.3); } 100% { background: rgba(0,0,0,0.12); } }

  /* VERDICT */
  .verdict { padding: 60px 32px; border-bottom: 2px solid var(--asg-black); display: none; }
  .verdict.show { display: block; }
  .verdict-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; }
  @media (max-width: 900px) { .verdict-grid { grid-template-columns: 1fr; } }
  .verdict-card { background: var(--asg-black); color: #fff; padding: 36px 36px; border: 2px solid var(--asg-black); }
  .verdict-card .label { color: var(--asg-red); font-family: 'Archivo Black', sans-serif; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; margin-bottom: 16px; }
  .verdict-card h3 { font-size: clamp(28px, 3vw, 42px); margin: 0 0 18px; line-height: 1.05; }
  .verdict-card p { font-size: 16px; line-height: 1.55; margin: 0 0 8px; opacity: 0.92; }
  .verdict-card p strong { color: var(--asg-blue); font-weight: 700; }
  .verdict-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; margin-top: 26px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 22px; }
  .verdict-stats .stat { padding-right: 14px; }
  .verdict-stats .stat .v { font-family: 'Archivo Black', sans-serif; font-size: 30px; color: var(--asg-blue); line-height: 1; }
  .verdict-stats .stat .v.red { color: var(--asg-red); }
  .verdict-stats .stat .l { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.7; margin-top: 6px; }

  .rewrite-cta { background: #fff; border: 2px solid var(--asg-black); padding: 32px; }
  .rewrite-cta .label { font-family: 'Archivo Black', sans-serif; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--asg-red); margin-bottom: 12px; }
  .rewrite-cta h3 { margin: 0 0 14px; font-size: 26px; }
  .rewrite-cta p { font-size: 15px; line-height: 1.55; color: var(--asg-line); margin: 0 0 22px; }
  .rewrite-btn { display: inline-flex; align-items: center; gap: 10px; padding: 16px 22px; background: var(--asg-blue); color: #fff; border: 2px solid var(--asg-blue); font-family: 'Archivo Black', sans-serif; font-size: 14px; letter-spacing: 0.06em; text-transform: uppercase; cursor: pointer; transition: all 0.15s; }
  .rewrite-btn:hover { background: var(--asg-black); border-color: var(--asg-black); transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--asg-blue); }

  /* REWRITE PANE */
  .rewrite { padding: 60px 32px; background: var(--asg-paper); border-bottom: 2px solid var(--asg-black); display: none; }
  .rewrite.show { display: block; }
  .rewrite h2 { font-size: clamp(36px, 5vw, 64px); margin: 0 0 12px; }
  .rewrite h2 .red { color: var(--asg-red); }
  .rewrite-sub { color: var(--asg-muted); font-size: 15px; margin: 0 0 36px; max-width: 720px; line-height: 1.5; }
  .rewrite-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }
  @media (max-width: 900px) { .rewrite-cols { grid-template-columns: 1fr; } }
  .rewrite-col { border: 2px solid var(--asg-black); padding: 28px; background: #fff; min-height: 360px; }
  .rewrite-col.before { background: #FFF5F5; }
  .rewrite-col.after { background: #F2FAFD; }
  .rewrite-col .stamp { font-family: 'Archivo Black', sans-serif; font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; padding: 5px 10px; display: inline-block; margin-bottom: 16px; }
  .rewrite-col.before .stamp { background: var(--asg-red); color: #fff; }
  .rewrite-col.after .stamp { background: var(--asg-blue); color: #fff; }
  .rewrite-col .body { font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.6; white-space: pre-wrap; min-height: 240px; }
  .rewrite-col.before .body { color: #4A0000; opacity: 0.6; text-decoration: line-through; text-decoration-color: rgba(209,0,0,0.4); }
  .rewrite-col.after .body { color: var(--asg-black); }
  .rewrite-col.after .cursor { display: inline-block; width: 8px; height: 18px; background: var(--asg-blue); vertical-align: text-bottom; animation: blink 0.7s steps(2) infinite; }
  @keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }

  .why-it-works { background: var(--asg-black); color: #fff; padding: 80px 32px; }
  .why-it-works h2 { font-size: clamp(36px, 5vw, 60px); margin: 0 0 14px; }
  .why-it-works h2 .blue { color: var(--asg-blue); }
  .why-it-works .sub { color: rgba(255,255,255,0.7); max-width: 680px; margin: 0 0 50px; line-height: 1.5; font-size: 16px; }
  .principles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border: 2px solid #fff; }
  @media (max-width: 900px) { .principles { grid-template-columns: 1fr; } }
  .principle { padding: 36px 30px; border-right: 2px solid #fff; }
  .principles .principle:last-child { border-right: none; }
  @media (max-width: 900px) { .principle { border-right: none; border-bottom: 2px solid #fff; } .principles .principle:last-child { border-bottom: none; } }
  .principle .num { font-family: 'Archivo Black', sans-serif; font-size: 56px; color: var(--asg-red); line-height: 1; margin-bottom: 18px; }
  .principle h3 { font-size: 24px; margin: 0 0 14px; line-height: 1.1; }
  .principle p { font-size: 14px; line-height: 1.55; color: rgba(255,255,255,0.85); margin: 0 0 12px; }
  .principle .source { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--asg-blue); letter-spacing: 0.04em; }

  /* PRODUCT MOMENT */
  .product { padding: 80px 32px; border-bottom: 2px solid var(--asg-black); }
  .product-head { display: flex; align-items: end; justify-content: space-between; gap: 30px; flex-wrap: wrap; margin-bottom: 32px; }
  .product h2 { font-size: clamp(34px, 4vw, 56px); margin: 0; max-width: 700px; line-height: 1.05; }
  .product h2 .red { color: var(--asg-red); }
  .product .lead { color: var(--asg-muted); max-width: 360px; font-size: 15px; line-height: 1.5; }
  .screenshot-frame { border: 2px solid var(--asg-black); padding: 14px; background: var(--asg-grey); }
  .screenshot-frame img { width: 100%; display: block; }
  .screenshot-frame .cap { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--asg-muted); padding: 14px 4px 0; line-height: 1.5; }

  /* CTA */
  .cta-section { padding: 80px 32px; background: var(--asg-blue); color: #fff; text-align: center; }
  .cta-section h2 { font-size: clamp(40px, 6vw, 80px); margin: 0 0 24px; }
  .cta-section p { font-size: 18px; max-width: 580px; margin: 0 auto 36px; opacity: 0.95; line-height: 1.5; }
  .cta-btn { display: inline-block; padding: 22px 46px; background: var(--asg-black); color: #fff; font-family: 'Archivo Black', sans-serif; font-size: 18px; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; transition: all 0.15s; border: 2px solid var(--asg-black); }
  .cta-btn:hover { background: var(--asg-red); border-color: var(--asg-red); transform: translate(-3px, -3px); box-shadow: 8px 8px 0 var(--asg-black); }

  /* FOOTER */
  footer.foot { padding: 36px 32px; border-top: 2px solid var(--asg-black); display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap; }
  footer .foot-left { display: flex; align-items: center; gap: 16px; }
  footer .foot-left svg { width: 110px; height: auto; }
  footer .foot-left .by { font-family: 'Archivo Black', sans-serif; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; }
  footer .foot-right { font-family: 'Archivo', sans-serif; font-size: 12px; color: var(--asg-muted); }
  footer .foot-right a { color: var(--asg-black); text-decoration: none; border-bottom: 2px solid var(--asg-red); }

  /* SCROLL REVEAL */
  .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.7s cubic-bezier(.2,.8,.2,1), transform 0.7s cubic-bezier(.2,.8,.2,1); }
  .reveal.in { opacity: 1; transform: translateY(0); }
</style>
</head>
<body>

<header class="topbar">
  <div class="logo">__LOGO_SVG__</div>
  <div class="topright"><a href="https://salesgrowth.com" target="_blank" rel="noopener">salesgrowth.com</a></div>
</header>

<section class="hero">
  <div class="container">
    <div class="hero-eyebrow">An interactive teardown · Gap Prospecting™ in motion</div>
    <h1>The Cold Email<br><span class="red">Autopsy</span>.</h1>
    <p class="lede">Drop in your cold email. Watch a Gap Prospecting diagnostic <strong>tear it apart line by line</strong>.</p>
    <p class="lede">Then watch it get rebuilt — the way buyers actually want to be sold.</p>
    <div class="credit">Prepared by A Sales Growth Company</div>
  </div>
</section>

<section class="tool">
  <div class="container">
    <div class="tool-grid">
      <div class="tool-section">
        <h2><span class="num">01.</span>The Email</h2>
        <p class="muted">Pick a sample below — or paste your own outbound and run it.</p>
        <div class="preset-row" id="presets">
          <button class="chip active" data-preset="0">The Feature Dump</button>
          <button class="chip" data-preset="1">Just Checking In</button>
          <button class="chip" data-preset="2">Fake Personalization</button>
          <button class="chip" data-preset="3">Pitch Sandwich</button>
        </div>
        <div class="editor-stack">
          <textarea id="email" class="email-input" spellcheck="false"></textarea>
          <div class="editor-overlay" id="overlay" aria-hidden="true"></div>
        </div>
        <button class="run-btn" id="run">Run the Autopsy <span class="arrow">→</span></button>
      </div>

      <div class="tool-section">
        <h2><span class="num">02.</span>The Diagnostic</h2>
        <p class="muted">Pitch on the left. Probe on the right. Where does this email land?</p>
        <div class="gauge-wrap">
          <svg class="gauge-svg" viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="arc" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#D10000"/>
                <stop offset="50%" stop-color="#999"/>
                <stop offset="100%" stop-color="#2098D1"/>
              </linearGradient>
            </defs>
            <path d="M 40 200 A 160 160 0 0 1 360 200" fill="none" stroke="url(#arc)" stroke-width="22" stroke-linecap="butt"/>
            <path d="M 40 200 A 160 160 0 0 1 360 200" fill="none" stroke="#000" stroke-width="2" stroke-dasharray="2 6" opacity="0.3"/>
            <text x="50" y="225" font-family="Archivo Black" font-size="13" fill="#D10000">PITCH</text>
            <text x="320" y="225" font-family="Archivo Black" font-size="13" fill="#2098D1">PROBE</text>
            <line id="needle" x1="200" y1="200" x2="200" y2="55" stroke="#000" stroke-width="5" stroke-linecap="round" style="transform-origin: 200px 200px; transform: rotate(0deg); transition: transform 0.7s cubic-bezier(.34,1.4,.6,1);"/>
            <circle cx="200" cy="200" r="14" fill="#000"/>
            <circle cx="200" cy="200" r="5" fill="#fff"/>
          </svg>
          <div class="score-readout">
            <div class="num neutral" id="score">0</div>
            <div class="label" id="scoreLabel">Awaiting input</div>
          </div>
          <div class="feed" id="feed">
            <div class="feed-empty">Annotations will appear here as the autopsy runs.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="verdict" id="verdict">
  <div class="container">
    <div class="verdict-grid">
      <div class="verdict-card">
        <div class="label">Verdict</div>
        <h3 id="verdictHead">—</h3>
        <p id="verdictBody">—</p>
        <div class="verdict-stats">
          <div class="stat"><div class="v red" id="vPitch">0</div><div class="l">Pitch flags</div></div>
          <div class="stat"><div class="v" id="vProbe">0</div><div class="l">Probe signals</div></div>
          <div class="stat"><div class="v red" id="vWeFocus">0</div><div class="l">"We" mentions</div></div>
        </div>
      </div>
      <div class="rewrite-cta">
        <div class="label">The Rewrite</div>
        <h3>Now watch Gap Prospecting fix it.</h3>
        <p>The autopsy tells you what's broken. The rewrite shows you the pattern Keenan teaches in <em>Gap Prospecting</em> — observation, gap, probe. No pitch, no platform name, no demo ask.</p>
        <button class="rewrite-btn" id="rewriteBtn">Watch the rewrite →</button>
      </div>
    </div>
  </div>
</section>

<section class="rewrite" id="rewriteSection">
  <div class="container">
    <h2>Same prospect. <span class="red">Different rep.</span></h2>
    <p class="rewrite-sub">The Gap Prospecting cold email doesn't sell the platform. It opens an information gap the buyer can't ignore. The frameworks: <strong>Trojan Horse</strong> opener (specific, observable), <strong>implied gap</strong> (the cost of the current state), <strong>probing question</strong> (no demo ask).</p>
    <div class="rewrite-cols">
      <div class="rewrite-col before">
        <div class="stamp">Before · Pitch-shaped</div>
        <div class="body" id="beforeBody"></div>
      </div>
      <div class="rewrite-col after">
        <div class="stamp">After · Probe-shaped</div>
        <div class="body" id="afterBody"></div>
      </div>
    </div>
  </div>
</section>

<section class="why-it-works reveal">
  <div class="container">
    <h2>Why it works.<br><span class="blue">Three principles, one pattern.</span></h2>
    <p class="sub">Cold outreach doesn't fail because reps aren't friendly enough. It fails because reps lead with their future state instead of the buyer's current one. Gap Prospecting flips it.</p>
    <div class="principles">
      <div class="principle">
        <div class="num">01</div>
        <h3>The buyer doesn't care about your future state until you've named theirs.</h3>
        <p>Pitches describe a destination the buyer never agreed they were heading to. Probes describe where the buyer already lives — and what staying there is costing them.</p>
        <div class="source">Source · Gap Selling, Keenan</div>
      </div>
      <div class="principle">
        <div class="num">02</div>
        <h3>The deal lives in the gap. Not in the demo.</h3>
        <p>The space between Current State and Future State is the only thing a buyer will spend money on. If your cold email never names the gap, you're asking them to pay for a feature instead of an outcome.</p>
        <div class="source">Source · Gap Prospecting, Keenan</div>
      </div>
      <div class="principle">
        <div class="num">03</div>
        <h3>Curiosity is a deficit. Pitches fill it. Probes open it.</h3>
        <p>Information-gap theory: people seek information when they perceive a gap between what they know and what they want to know. Reps who name a possible blind spot create that gap. Reps who pitch close someone else's.</p>
        <div class="source">Source · Golman &amp; Loewenstein, "The Information-Gap Theory of Curiosity," Psychological Bulletin, 2018 (orig. Loewenstein 1994)</div>
      </div>
    </div>
  </div>
</section>

<section class="product reveal">
  <div class="container">
    <div class="product-head">
      <h2>This is what an <span class="red">AI Gap Prospecting coach</span> looks like.</h2>
      <p class="lead">Reps don't fix outbound by reading a book. They fix it by writing, getting torn apart, rewriting, and shipping. Every time.</p>
    </div>
    <div class="screenshot-frame">
      <img src="data:image/png;base64,__EMAIL_CHAT_B64__" alt="Keenan critiquing a cold email inside Replicate Labs">
      <div class="cap">__EMAIL_CHAT_CAPTION__</div>
    </div>
  </div>
</section>

<section class="cta-section reveal">
  <div class="container">
    <h2>Stop pitching.<br>Start diagnosing.</h2>
    <p>Gap Prospecting and Gap Selling are taught by A Sales Growth Company — Keenan's firm, and the source of the methodology used in this autopsy.</p>
    <a href="https://salesgrowth.com" target="_blank" rel="noopener" class="cta-btn">See ASG's training →</a>
  </div>
</section>

<footer class="foot">
  <div class="foot-left">
    <div>__LOGO_SVG_SMALL__</div>
    <div class="by">Prepared by A Sales Growth Company</div>
  </div>
  <div class="foot-right">
    <a href="https://salesgrowth.com" target="_blank" rel="noopener">salesgrowth.com</a> &nbsp;·&nbsp;
    <a href="https://salesgrowth.com/privacy-policy" target="_blank" rel="noopener">Privacy</a> &nbsp;·&nbsp;
    <a href="https://salesgrowth.com/terms" target="_blank" rel="noopener">Terms</a>
  </div>
</footer>

<script>
// =========================================================
// SAMPLES + REWRITES
// =========================================================
const SAMPLES = [
  {
    name: "Feature Dump",
    text: `Hi Sarah,

I'm Mark from FlowMetric. We're an AI-powered revenue analytics platform that helps RevOps leaders like you get full pipeline visibility.

Our cutting-edge ML models surface deal risk in real time, and our integrations span Salesforce, HubSpot and Outreach. Customers like Acme Corp have seen 40% improvements in win rates with our solution.

Got 15 minutes for a quick demo this week?

Thanks,
Mark`,
    rewrite: `Hi Sarah,

3 of your last 6 board updates flagged "pipeline coverage." That number normally moves when AEs are calling deals committed at stage 3 that don't survive stage 4 — which shows up as cycle slippage before it shows up as a missed quarter.

If FlowMetric's pipeline is doing the same, the cost isn't a forecasting tool — it's the attainment gap that opens once your AEs are protecting deals they should be qualifying out.

What's your AE attainment looking like for AEs in months 6–12 vs. months 12+ ?

Mark`
  },
  {
    name: "Just Checking In",
    text: `Hi Sarah,

Just checking in to see if you saw my email last week.

Wanted to circle back on the demo. Any thoughts? Happy to find a time that works for you.

Thanks!
Mark`,
    rewrite: `Hi Sarah,

Skipping the "checking in" — that's wallpaper.

Last note I sent was about pipeline coverage. Since then, I noticed FlowMetric posted 4 BDR roles. Hiring 4 BDRs while coverage sits below 3x usually means leadership is treating coverage as a volume problem when it's a conversation problem.

If your BDRs are pitching the platform in cold outreach, the coverage gap closes for one quarter and reopens the next. Want to see a 60-second teardown of one of your team's outbound emails?

Mark`
  },
  {
    name: "Fake Personalization",
    text: `Hi Sarah,

Loved your recent LinkedIn post on scaling sales teams. Congrats on the new role at FlowMetric!

I work with sales leaders to help them improve rep productivity through our platform. Would love to introduce you to our AI-powered coach — companies like yours are seeing huge wins.

Open to a quick chat next week?

Best,
Mark`,
    rewrite: `Hi Sarah,

You took the CRO seat 6 months in. The pattern at your stage of growth (mid-market, post-Series B, 60+ AEs) is that attainment drops 15–20 points in Q2 because the playbook that worked at $20M ARR doesn't survive at $45M.

If your AE attainment is sitting near 40% in H1, the root cause is almost never the rep — it's that they're still selling the product instead of the buyer's gap.

Curious: are your AEs running discovery or running demos in first calls?

Mark`
  },
  {
    name: "Pitch Sandwich",
    text: `Hi Sarah,

I noticed FlowMetric is hiring 12 BDRs this quarter. We help fast-growing teams ramp BDRs 2x faster with our world-class onboarding platform.

Companies like Workday and Zendesk use our solution. Interested in a 30-minute demo to see if we're a fit?

Thanks,
Mark`,
    rewrite: `Hi Sarah,

12 BDR hires this quarter is a coverage bet — the math only works if those reps are productive in 90 days, not 180.

The trap: when ramp is slow, leadership reaches for content and tooling. The actual lever is what BDRs say in the first 15 seconds of a cold call. If they pitch the product, prospects hang up. If they open a gap, prospects engage.

What's the average days-to-first-meeting for your last cohort of new BDRs?

Mark`
  }
];

// =========================================================
// DETECTION RULES
// =========================================================
const PITCH_PATTERNS = [
  // we-focused / introducing
  { rx: /\bwe(?:'re| are|)\s+(?:an?\s+)?(?:ai-powered|cutting-edge|world-class|industry-leading|best-in-class|next-gen|innovative|leading)/i, weight: -10, label: 'Feature dump', kind: 'bad' },
  { rx: /\bAI[- ]powered\b/i, weight: -8, label: 'Buzzword', kind: 'bad' },
  { rx: /\bcutting[- ]edge\b/i, weight: -7, label: 'Buzzword', kind: 'bad' },
  { rx: /\bworld[- ]class\b/i, weight: -7, label: 'Buzzword', kind: 'bad' },
  { rx: /\bbest[- ]in[- ]class\b/i, weight: -7, label: 'Buzzword', kind: 'bad' },
  { rx: /\bindustry[- ]leading\b/i, weight: -7, label: 'Buzzword', kind: 'bad' },
  { rx: /\bnext[- ]gen(?:eration)?\b/i, weight: -6, label: 'Buzzword', kind: 'bad' },
  { rx: /\binnovative\b/i, weight: -5, label: 'Buzzword', kind: 'bad' },
  { rx: /\bleverage\b/i, weight: -5, label: 'Buzzword', kind: 'bad' },
  { rx: /\bsynergy\b/i, weight: -8, label: 'Buzzword', kind: 'bad' },
  // platform/solution
  { rx: /\bour\s+(?:platform|solution|tool|software|product)\b/i, weight: -8, label: '"Our platform"', kind: 'bad' },
  { rx: /\b(?:platform|solution)\b/i, weight: -3, label: 'Platform language', kind: 'bad' },
  // checking in
  { rx: /\bjust\s+checking\s+in\b/i, weight: -15, label: '"Just checking in"', kind: 'bad' },
  { rx: /\bcircling?\s+back\b/i, weight: -12, label: '"Circling back"', kind: 'bad' },
  { rx: /\bfollowing?\s+up\b/i, weight: -8, label: '"Following up"', kind: 'bad' },
  { rx: /\bany\s+thoughts\?/i, weight: -10, label: 'No-stakes ask', kind: 'bad' },
  { rx: /\bdid\s+you\s+(?:see|get)\s+my/i, weight: -10, label: 'Self-centered nudge', kind: 'bad' },
  // demo asks
  { rx: /\b(?:15|30|20)\s*[- ]?\s*minute(?:s)?\b/i, weight: -8, label: 'Time-asking demo', kind: 'bad' },
  { rx: /\bquick\s+(?:demo|chat|call|meeting)\b/i, weight: -8, label: '"Quick demo"', kind: 'bad' },
  { rx: /\bschedule\s+a\s+(?:demo|call|meeting)\b/i, weight: -10, label: 'Premature ask', kind: 'bad' },
  { rx: /\b(?:hop|jump)\s+on\s+a\s+(?:call|chat)\b/i, weight: -8, label: '"Hop on a call"', kind: 'bad' },
  // fake personalization
  { rx: /\bloved\s+your\s+(?:recent|last)?\s*(?:post|article)\b/i, weight: -12, label: 'Fake personalization', kind: 'bad' },
  { rx: /\bcongrats?\s+on\s+(?:the|your)\s+new\s+(?:role|job)\b/i, weight: -12, label: 'Templated open', kind: 'bad' },
  { rx: /\bsaw\s+your\s+(?:post|article)\b/i, weight: -8, label: 'Fake personalization', kind: 'bad' },
  // we help
  { rx: /\bwe\s+help\b/i, weight: -7, label: '"We help"', kind: 'bad' },
  { rx: /\bwe\s+work\s+with\b/i, weight: -7, label: 'Generic positioning', kind: 'bad' },
  { rx: /\bwould\s+love\s+to\s+(?:introduce|share|chat|connect)/i, weight: -8, label: 'Premature ask', kind: 'bad' },
  { rx: /\bcompanies?\s+like\b/i, weight: -6, label: 'Logo-dropping', kind: 'bad' },
  { rx: /\bcustomers?\s+like\b/i, weight: -6, label: 'Logo-dropping', kind: 'bad' },
  { rx: /\bhuge\s+wins?\b/i, weight: -6, label: 'Vague claim', kind: 'bad' },
  { rx: /\b\d+%\s+(?:improvement|increase|boost|uplift|reduction|faster)\b/i, weight: -5, label: 'Unverified stat', kind: 'bad' },
  { rx: /\b\dx\s+(?:faster|better)\b/i, weight: -5, label: 'Unverified claim', kind: 'bad' },
  // see if we're a fit
  { rx: /\bif\s+we(?:'re| are)\s+a\s+fit\b/i, weight: -7, label: 'Vague qualifier', kind: 'bad' },
];

const PROBE_PATTERNS = [
  // questions about current state / measurable
  { rx: /\bwhat(?:'s| is)\s+your\s+(?:current|attainment|coverage|ramp|cycle|win\s+rate|renewal)/i, weight: 12, label: 'Current-state probe', kind: 'good' },
  { rx: /\bare\s+your\s+(?:AEs?|BDRs?|reps?)\s+(?:running|pitching|opening)/i, weight: 14, label: 'Behavior probe', kind: 'good' },
  { rx: /\bwhat\s+happens\s+when\b/i, weight: 10, label: 'Impact probe', kind: 'good' },
  { rx: /\bcurious(?::| —|,)\s+(?:are|is|how|what|when|why)/i, weight: 10, label: 'Open question', kind: 'good' },
  // specific observation (Trojan horse)
  { rx: /\b\d+\s+(?:of\s+your\s+last\s+)?\d*\s*(?:board|earnings|updates?|hires?|roles?|BDRs?|AEs?)\b/i, weight: 12, label: 'Trojan-horse opener', kind: 'good' },
  { rx: /\bI\s+noticed\s+\w+\s+(?:posted|hired|launched|announced|is\s+hiring)/i, weight: 8, label: 'Specific observation', kind: 'good' },
  // gap language
  { rx: /\bcurrent\s+state\b/i, weight: 8, label: 'Current state language', kind: 'good' },
  { rx: /\bthe\s+gap\b/i, weight: 10, label: 'Gap language', kind: 'good' },
  { rx: /\bthe\s+cost\s+of\b/i, weight: 8, label: 'Cost-of-inaction frame', kind: 'good' },
  { rx: /\broot\s+cause\b/i, weight: 10, label: 'Diagnostic frame', kind: 'good' },
  { rx: /\battainment\s+(?:gap|drop|sits?|drops?)/i, weight: 10, label: 'Specific metric', kind: 'good' },
  { rx: /\bcoverage\s+(?:gap|drop|sits?|below)/i, weight: 10, label: 'Specific metric', kind: 'good' },
  { rx: /\bthe\s+actual\s+lever\b/i, weight: 8, label: 'Diagnostic phrasing', kind: 'good' },
  { rx: /\bthe\s+root\s+cause\s+is\b/i, weight: 10, label: 'Root-cause frame', kind: 'good' },
  // skipping the cliché
  { rx: /\bskipping\s+the\b/i, weight: 8, label: 'Pattern-break', kind: 'good' },
];

// =========================================================
// STATE
// =========================================================
const $ = (id) => document.getElementById(id);
const emailEl = $('email');
const overlay = $('overlay');
let activePreset = 0;
let isRunning = false;
let lastResults = null;

function loadPreset(i) {
  activePreset = i;
  emailEl.value = SAMPLES[i].text;
  resetState();
  syncOverlay();
}

function resetState() {
  $('score').textContent = '0';
  $('score').className = 'num neutral';
  $('scoreLabel').textContent = 'Awaiting input';
  $('feed').innerHTML = '<div class="feed-empty">Annotations will appear here as the autopsy runs.</div>';
  setNeedle(0);
  $('verdict').classList.remove('show');
  $('rewriteSection').classList.remove('show');
  overlay.innerHTML = '';
}

function syncOverlay() {
  // mirror the textarea's content into the overlay (no marks until run)
  overlay.innerHTML = escapeHtml(emailEl.value);
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

document.querySelectorAll('#presets .chip').forEach((c) => {
  c.addEventListener('click', () => {
    document.querySelectorAll('#presets .chip').forEach((x) => x.classList.remove('active'));
    c.classList.add('active');
    loadPreset(parseInt(c.dataset.preset, 10));
  });
});

emailEl.addEventListener('input', () => {
  syncOverlay();
});

// =========================================================
// AUTOPSY RUN
// =========================================================
function setNeedle(score) {
  // score range -100 .. +100 → -90deg .. +90deg
  const clamped = Math.max(-100, Math.min(100, score));
  const deg = (clamped / 100) * 90;
  document.getElementById('needle').style.transform = `rotate(${deg}deg)`;
}

function detectAll(text) {
  const hits = [];
  let pitchCount = 0, probeCount = 0, weCount = 0;
  PITCH_PATTERNS.forEach((p) => {
    let m;
    const rx = new RegExp(p.rx.source, p.rx.flags.includes('g') ? p.rx.flags : p.rx.flags + 'g');
    while ((m = rx.exec(text)) !== null) {
      hits.push({ start: m.index, end: m.index + m[0].length, text: m[0], weight: p.weight, label: p.label, kind: p.kind });
      pitchCount += 1;
      if (m[0].toLowerCase().startsWith('we')) weCount += 1;
      if (m.index === rx.lastIndex) rx.lastIndex++;
    }
  });
  PROBE_PATTERNS.forEach((p) => {
    let m;
    const rx = new RegExp(p.rx.source, p.rx.flags.includes('g') ? p.rx.flags : p.rx.flags + 'g');
    while ((m = rx.exec(text)) !== null) {
      hits.push({ start: m.index, end: m.index + m[0].length, text: m[0], weight: p.weight, label: p.label, kind: p.kind });
      probeCount += 1;
      if (m.index === rx.lastIndex) rx.lastIndex++;
    }
  });
  // count standalone "we " mentions even if not pattern-matched (cap)
  const weMatches = text.match(/\bwe(?:'re| are|'ve|\s)/gi) || [];
  if (weMatches.length > weCount) weCount = weMatches.length;
  // sort by start index, dedupe overlaps
  hits.sort((a,b) => a.start - b.start);
  const filtered = [];
  let lastEnd = -1;
  for (const h of hits) {
    if (h.start >= lastEnd) {
      filtered.push(h);
      lastEnd = h.end;
    }
  }
  return { hits: filtered, pitchCount, probeCount, weCount };
}

function buildOverlayWith(text, hits, scanIndex) {
  // build HTML with marks
  let out = '';
  let cursor = 0;
  hits.forEach((h, i) => {
    if (h.start > cursor) out += escapeHtml(text.slice(cursor, h.start));
    const cls = h.kind === 'bad' ? 'bad' : 'good';
    const scan = (i === scanIndex) ? ' scan' : '';
    out += `<mark class="${cls}${scan}">${escapeHtml(text.slice(h.start, h.end))}</mark>`;
    cursor = h.end;
  });
  if (cursor < text.length) out += escapeHtml(text.slice(cursor));
  return out;
}

function addAnnotation(h) {
  const feed = $('feed');
  if (feed.querySelector('.feed-empty')) feed.innerHTML = '';
  const a = document.createElement('div');
  a.className = 'ann';
  const sym = h.kind === 'bad' ? '✕' : '✓';
  const cls = h.kind === 'bad' ? 'bad' : 'good';
  a.innerHTML = `
    <div class="badge ${cls}">${sym}</div>
    <div class="text">
      <strong>${h.label}</strong> ${h.weight > 0 ? '+' : ''}${h.weight}
      <span class="quote">"${escapeHtml(h.text)}"</span>
    </div>`;
  feed.appendChild(a);
  feed.scrollTop = feed.scrollHeight;
}

function setScore(s) {
  $('score').textContent = (s > 0 ? '+' : '') + s;
  $('score').className = 'num ' + (s < -10 ? 'bad' : s > 10 ? 'good' : 'neutral');
  $('scoreLabel').textContent = s < -30 ? 'Pure Pitch' : s < -10 ? 'Mostly Pitch' : s < 10 ? 'Borderline' : s < 30 ? 'Mostly Probe' : 'Strong Probe';
  setNeedle(s);
}

function showVerdict(score, pitchCount, probeCount, weCount) {
  $('vPitch').textContent = pitchCount;
  $('vProbe').textContent = probeCount;
  $('vWeFocus').textContent = weCount;
  let head = '', body = '';
  if (score < -30) {
    head = "It's a pitch in a trench coat.";
    body = "<strong>You're selling the future state.</strong> The buyer hasn't agreed there's a problem with their current state — and you've already asked for the demo. Reps lose this email before the second sentence.";
  } else if (score < -10) {
    head = "Mostly pitch. Mostly ignored.";
    body = "<strong>There's a flicker of a probe</strong> in here, but it's smothered by feature language and a premature ask. The buyer's mental model: another rep selling another platform.";
  } else if (score < 10) {
    head = "Borderline. Forgettable.";
    body = "<strong>Not bad. Not memorable either.</strong> No clear pitch flags, but no clear gap either. Cold email is binary: open the gap or get archived. This one gets archived.";
  } else if (score < 30) {
    head = "There's a probe in here. Sharpen it.";
    body = "<strong>Good instincts.</strong> You're naming the buyer's current state and pointing at a gap. Tighten the question, drop any leftover platform language, and you've got something.";
  } else {
    head = "That's a probe.";
    body = "<strong>This is what Gap Prospecting reads like.</strong> Specific observation, named gap, root-cause framing, single open question. No demo ask. The buyer leans in.";
  }
  $('verdictHead').textContent = head;
  $('verdictBody').innerHTML = body;
  $('verdict').classList.add('show');
}

async function runAutopsy() {
  if (isRunning) return;
  isRunning = true;
  resetState();
  const text = emailEl.value;
  const result = detectAll(text);
  const hits = result.hits;
  let runningScore = 0;
  // sequential reveal
  for (let i = 0; i < hits.length; i++) {
    overlay.innerHTML = buildOverlayWith(text, hits.slice(0, i+1), i);
    runningScore += hits[i].weight;
    setScore(runningScore);
    addAnnotation(hits[i]);
    await sleep(280);
  }
  if (hits.length === 0) {
    setScore(0);
  }
  // final
  overlay.innerHTML = buildOverlayWith(text, hits, -1);
  showVerdict(runningScore, result.pitchCount, result.probeCount, result.weCount);
  lastResults = { score: runningScore, ...result };
  isRunning = false;
  // smooth scroll to verdict
  setTimeout(() => $('verdict').scrollIntoView({ behavior: 'smooth', block: 'start' }), 200);
}

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

$('run').addEventListener('click', runAutopsy);

// =========================================================
// REWRITE ANIMATION
// =========================================================
$('rewriteBtn').addEventListener('click', async () => {
  const sample = SAMPLES[activePreset];
  const before = sample.text;
  const after = sample.rewrite;
  $('beforeBody').textContent = before;
  const afterEl = $('afterBody');
  afterEl.innerHTML = '<span class="cursor"></span>';
  $('rewriteSection').classList.add('show');
  setTimeout(() => $('rewriteSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 200);
  await sleep(700);
  // type effect
  let typed = '';
  for (let i = 0; i < after.length; i++) {
    typed += after[i];
    afterEl.innerHTML = escapeHtml(typed) + '<span class="cursor"></span>';
    // speed up; pause briefly on line breaks
    const ch = after[i];
    const delay = ch === '\n' ? 100 : 14;
    await sleep(delay);
  }
  afterEl.innerHTML = escapeHtml(typed);
});

// =========================================================
// INIT
// =========================================================
loadPreset(0);

// Scroll reveal
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) e.target.classList.add('in'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
</script>
</body>
</html>
"""

# substitute
LOGO_SVG_SMALL = LOGO_SVG.replace('width="315"', 'width="110"').replace('height="160"', 'height="56"')
out = (HTML
       .replace("__LOGO_SVG__", LOGO_SVG)
       .replace("__LOGO_SVG_SMALL__", LOGO_SVG_SMALL)
       .replace("__EMAIL_CHAT_B64__", EMAIL_CHAT_B64)
       .replace("__EMAIL_CHAT_CAPTION__", EMAIL_CHAT_CAPTION))

OUT.write_text(out)
print(f"Wrote {OUT} ({len(out):,} bytes)")
