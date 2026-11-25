#!/usr/bin/env python3
"""Build practical_test_<lang>.html for one or all languages.
Usage: python3 build_html.py [lang]   (lang: en, it, ru, ja, zh, zh-tw — default: all)
"""
import json, subprocess, os, sys

# utils/ is one level inside the project root
UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR  = os.path.dirname(UTILS_DIR)

LANG_TITLES = {
    "en": "Claude Certified Architect \u2014 Practical Test",
    "ru": "Claude Certified Architect \u2014 \u041f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442",
    "ja": "Claude Certified Architect \u2014 \u7df4\u7fd2\u30c6\u30b9\u30c8",
    "zh": "Claude Certified Architect \u2014 \u6a21\u62df\u6d4b\u8bd5",
    "it": "Claude Certified Architect \u2014 Test Pratico",
    "zh-tw": "Claude Certified Architect \u2014 \u6a21\u64ec\u6e2c\u9a57",
    "pt-br": "Claude Certified Architect \u2014 Teste Prático",
    "es": "Claude Certified Architect \u2014 Test Práctico",
    "uk": "Claude Certified Architect \u2014 Практичний тест",
}

def get_questions(lang):
    result = subprocess.run(
        ["python3", "extract_question.py", lang, "all"],
        capture_output=True, text=True, cwd=ROOT_DIR
    )
    return json.loads(result.stdout)

BUILD_LANGS = sys.argv[1:] if len(sys.argv) > 1 else list(LANG_TITLES.keys())

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  background: #f0f2f5;
  color: #1a1a2e;
  min-height: 100vh;
}

.shell { display: flex; height: 100vh; overflow: hidden; }

/* Sidebar */
.sidebar {
  width: 260px; min-width: 260px;
  background: #1a1a2e; color: #cdd3de;
  display: flex; flex-direction: column; overflow: hidden;
}
.sidebar-header {
  padding: 20px 16px 14px;
  font-size: 13px; font-weight: 700;
  letter-spacing: .06em; text-transform: uppercase;
  color: #7f8fa6; border-bottom: 1px solid #2c2c4a; flex-shrink: 0;
}
.sidebar-progress {
  padding: 10px 16px; font-size: 12px; color: #7f8fa6;
  border-bottom: 1px solid #2c2c4a; flex-shrink: 0;
}
.sidebar-progress span { color: #e2e8f0; font-weight: 600; }
.sidebar-scroll { overflow-y: auto; flex: 1; padding: 8px 0; }
.sidebar-scroll::-webkit-scrollbar { width: 4px; }
.sidebar-scroll::-webkit-scrollbar-thumb { background: #2c2c4a; border-radius: 2px; }

.scenario-group { margin-bottom: 4px; }
.scenario-label {
  padding: 6px 16px 4px; font-size: 10.5px; font-weight: 700;
  letter-spacing: .08em; text-transform: uppercase; color: #4a5568;
}
.q-btn {
  display: flex; align-items: center; gap: 8px;
  width: 100%; padding: 6px 16px;
  background: none; border: none; cursor: pointer;
  font-size: 13.5px; color: #a0aec0; text-align: left;
  transition: background .15s, color .15s;
  border-left: 3px solid transparent;
}
.q-btn:hover { background: #242447; color: #e2e8f0; }
.q-btn.active { background: #1e3a5f; color: #63b3ed; border-left-color: #63b3ed; }
.q-btn.answered-correct { color: #68d391; }
.q-btn.answered-correct .q-dot { background: #68d391; }
.q-btn.answered-wrong { color: #fc8181; }
.q-btn.answered-wrong .q-dot { background: #fc8181; }
.q-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #4a5568; flex-shrink: 0; transition: background .2s;
}

/* Main */
.main { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.topbar {
  background: #fff; border-bottom: 1px solid #e2e8f0;
  padding: 12px 32px; display: flex; align-items: center;
  justify-content: space-between; flex-shrink: 0;
  box-shadow: 0 1px 3px rgba(0,0,0,.06);
}
.topbar-title { font-size: 15px; font-weight: 600; color: #2d3748; }
.topbar-nav { display: flex; gap: 10px; align-items: center; }
.nav-btn {
  padding: 7px 18px; border-radius: 8px;
  border: 1.5px solid #cbd5e0; background: #fff;
  font-size: 14px; cursor: pointer; color: #4a5568; font-weight: 500;
  transition: all .15s;
}
.nav-btn:hover { background: #edf2f7; border-color: #a0aec0; }
.nav-btn:disabled { opacity: .35; cursor: default; }
.nav-btn.finish { background: #2b6cb0; color: #fff; border-color: #2b6cb0; }
.nav-btn.finish:hover { background: #2c5282; }
.q-counter { font-size: 13px; color: #718096; font-weight: 500; }

.content { flex: 1; overflow-y: auto; padding: 36px 48px; }
.content::-webkit-scrollbar { width: 6px; }
.content::-webkit-scrollbar-thumb { background: #cbd5e0; border-radius: 3px; }

/* Question card */
.q-card { max-width: 820px; margin: 0 auto; }
.q-scenario {
  display: inline-block; background: #ebf8ff; color: #2b6cb0;
  font-size: 12px; font-weight: 700; letter-spacing: .05em;
  text-transform: uppercase; padding: 4px 12px;
  border-radius: 20px; margin-bottom: 16px;
}
.q-number { font-size: 13px; color: #a0aec0; margin-bottom: 6px; font-weight: 600; }
.q-situation {
  font-size: 16.5px; color: #1a202c;
  font-weight: 500; line-height: 1.7;
  background: #fff;
  border: 1.5px solid #d0dff0;
  border-radius: 10px;
  padding: 16px 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
  margin-bottom: 22px;
}
.q-situation code, .opt-text code, .explanation code {
  background: #e2e8f0; padding: 1px 5px; border-radius: 4px;
  font-family: "SF Mono", Menlo, Monaco, monospace;
  font-size: 13.5px; color: #2d3748;
}
.explanation code { background: #feebc8; }
.q-prompt { font-size: 17px; font-weight: 700; color: #1a202c; margin-bottom: 20px; }

/* Options */
.options { display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px; }
.option {
  display: flex; align-items: flex-start; gap: 14px;
  padding: 14px 18px; border: 2px solid #e2e8f0;
  border-radius: 12px; cursor: pointer; background: #fff;
  transition: border-color .15s, background .15s, transform .1s;
}
.option:hover:not(.locked) {
  border-color: #90cdf4; background: #ebf8ff; transform: translateX(2px);
}
.option.locked { cursor: default; }
.opt-letter {
  width: 30px; height: 30px; min-width: 30px; border-radius: 50%;
  background: #edf2f7; display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 14px; color: #4a5568;
  transition: background .2s, color .2s; flex-shrink: 0;
}
.opt-text { font-size: 15px; color: #2d3748; line-height: 1.55; padding-top: 3px; }

.option.correct { border-color: #48bb78; background: #f0fff4; }
.option.correct .opt-letter { background: #48bb78; color: #fff; }
.option.wrong { border-color: #fc8181; background: #fff5f5; }
.option.wrong .opt-letter { background: #fc8181; color: #fff; }
.option.dimmed { opacity: .55; }

/* Explanation */
.explanation {
  margin-top: 4px; padding: 14px 18px;
  background: #fffbeb; border-left: 4px solid #f6ad55;
  border-radius: 0 10px 10px 0;
  font-size: 14.5px; color: #744210; line-height: 1.65; display: none;
}
.explanation.show { display: block; }
.explanation strong { color: #744210; }

/* Summary */
.summary { max-width: 820px; margin: 0 auto; display: none; }
.summary.show { display: block; }
.summary h1 { font-size: 26px; font-weight: 800; color: #1a202c; margin-bottom: 6px; }
.summary-subtitle { color: #718096; font-size: 15px; margin-bottom: 28px; }
.score-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; margin-bottom: 32px; }
.score-card {
  background: #fff; border-radius: 14px; padding: 20px;
  text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,.07);
}
.score-card .big { font-size: 38px; font-weight: 800; line-height: 1; margin-bottom: 6px; }
.score-card .label { font-size: 13px; color: #718096; font-weight: 600; text-transform: uppercase; letter-spacing: .05em; }
.score-card.total .big { color: #2b6cb0; }
.score-card.correct-c .big { color: #38a169; }
.score-card.wrong-c .big { color: #e53e3e; }

.section-title {
  font-size: 18px; font-weight: 700; color: #2d3748;
  margin-bottom: 12px; padding-bottom: 6px; border-bottom: 2px solid #e2e8f0;
}
.group-block {
  background: #fff; border-radius: 12px; padding: 18px 20px;
  margin-bottom: 16px; box-shadow: 0 1px 4px rgba(0,0,0,.06);
}
.group-title {
  font-size: 15px; font-weight: 700; color: #2d3748;
  margin-bottom: 12px; display: flex; align-items: center; gap: 10px;
}
.group-badge {
  font-size: 11px; padding: 2px 10px; border-radius: 20px;
  font-weight: 700; background: #fff5f5; color: #c53030;
}
.wrong-item {
  display: flex; gap: 10px; align-items: flex-start;
  padding: 12px 0; border-bottom: 1px solid #f0f0f0;
  font-size: 14px; color: #4a5568;
}
.wrong-item:last-child { border-bottom: none; }
.wrong-item .wi-n { min-width: 32px; font-weight: 700; color: #a0aec0; font-size: 12px; padding-top: 2px; }
.wrong-item .wi-q { flex: 1; }
.wrong-item .wi-situation { font-size: 13.5px; color: #2d3748; font-weight: 500; margin-bottom: 4px; line-height: 1.5; }
.wrong-item .wi-situation code { background: #e2e8f0; padding: 1px 4px; border-radius: 3px; font-family: "SF Mono", Menlo, Monaco, monospace; font-size: 12.5px; }
.wrong-item .wi-prompt { font-size: 13px; color: #718096; font-style: italic; margin-bottom: 4px; }
.wrong-item .wi-ans { font-size: 12px; margin-top: 3px; color: #718096; }
.wi-wrong-tag { color: #e53e3e; font-weight: 700; }
.wi-correct-tag { color: #38a169; font-weight: 700; }

.restart-btn {
  margin-top: 28px; padding: 12px 32px;
  background: #2b6cb0; color: #fff; border: none;
  border-radius: 10px; font-size: 15px; font-weight: 700;
  cursor: pointer; transition: background .15s;
}
.restart-btn:hover { background: #2c5282; }

.screen { display: none; }
.screen.active { display: block; }
"""

JS = r"""
const QUESTIONS = __DATA__;

const state = { current: 0, answers: {} };

function md(text) {
  if (!text) return '';
  return text
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, ' ');
}

function buildSidebar() {
  const list = document.getElementById('sidebarList');
  document.getElementById('totalCount').textContent = QUESTIONS.length;
  let currentScenario = null;
  let groupEl = null;
  QUESTIONS.forEach((q, idx) => {
    if (q.scenario !== currentScenario) {
      currentScenario = q.scenario;
      const sg = document.createElement('div');
      sg.className = 'scenario-group';
      const lbl = document.createElement('div');
      lbl.className = 'scenario-label';
      lbl.textContent = q.scenario;
      sg.appendChild(lbl);
      groupEl = sg;
      list.appendChild(sg);
    }
    const btn = document.createElement('button');
    btn.className = 'q-btn';
    btn.id = 'sb-' + idx;
    btn.onclick = () => goto(idx);
    btn.innerHTML = '<span class="q-dot"></span> Q' + q.global_n;
    groupEl.appendChild(btn);
  });
}

function updateSidebar() {
  QUESTIONS.forEach((q, idx) => {
    const btn = document.getElementById('sb-' + idx);
    if (!btn) return;
    btn.className = 'q-btn';
    if (idx === state.current) btn.classList.add('active');
    const ans = state.answers[q.global_n];
    if (ans !== undefined) {
      btn.classList.add(ans === q.correct ? 'answered-correct' : 'answered-wrong');
    }
  });
  document.getElementById('answeredCount').textContent = Object.keys(state.answers).length;
}

function renderQuestion(idx) {
  const q = QUESTIONS[idx];
  const chosen = state.answers[q.global_n];
  const locked = chosen !== undefined;

  document.getElementById('qCounter').textContent = (idx + 1) + ' / ' + QUESTIONS.length;
  document.getElementById('prevBtn').disabled = idx === 0;
  document.getElementById('nextBtn').disabled = idx === QUESTIONS.length - 1;

  const optionsHtml = q.options.map(opt => {
    let cls = 'option';
    if (locked) {
      cls += ' locked';
      if (opt.correct) cls += ' correct';
      else if (opt.letter === chosen) cls += ' wrong';
      else cls += ' dimmed';
    }
    return '<div class="' + cls + '" data-letter="' + opt.letter + '" onclick="answer(' + q.global_n + ', \'' + opt.letter + '\')">' +
      '<div class="opt-letter">' + opt.letter + '</div>' +
      '<div class="opt-text">' + md(opt.text) + '</div></div>';
  }).join('');

  const expl = locked
    ? '<div class="explanation show"><strong>Why ' + q.correct + ':</strong> ' + md(q.explanation) + '</div>'
    : '<div class="explanation"></div>';

  document.getElementById('qCard').innerHTML =
    '<div class="q-number">Question ' + q.global_n + '</div>' +
    '<div class="q-scenario">' + q.scenario + '</div>' +
    '<div class="q-situation">' + md(q.situation) + '</div>' +
    '<div class="q-prompt">' + md(q.question) + '</div>' +
    '<div class="options">' + optionsHtml + '</div>' +
    expl;
}

function answer(globalN, letter) {
  if (state.answers[globalN] !== undefined) return;
  state.answers[globalN] = letter;
  renderQuestion(state.current);
  updateSidebar();
}

function navigate(dir) { goto(state.current + dir); }

function goto(idx) {
  if (idx < 0 || idx >= QUESTIONS.length) return;
  document.getElementById('questionScreen').classList.add('active');
  document.getElementById('summaryScreen').classList.remove('active');
  state.current = idx;
  renderQuestion(idx);
  updateSidebar();
}

function showSummary() {
  document.getElementById('questionScreen').classList.remove('active');
  document.getElementById('summaryScreen').classList.add('active');

  const total = QUESTIONS.length;
  const answered = Object.keys(state.answers).length;
  let correct = 0;
  const wrongByScenario = {};

  QUESTIONS.forEach(q => {
    const ans = state.answers[q.global_n];
    if (ans === undefined) return;
    if (ans === q.correct) {
      correct++;
    } else {
      if (!wrongByScenario[q.scenario]) wrongByScenario[q.scenario] = [];
      wrongByScenario[q.scenario].push({ q: q, chosen: ans });
    }
  });

  const wrong = answered - correct;
  const pct = answered > 0 ? Math.round(correct / answered * 100) : 0;
  const unanswered = total - answered;

  let wrongGroupsHtml = '';
  for (const scenario in wrongByScenario) {
    const items = wrongByScenario[scenario];
    const rows = items.map(item => {
      const chosenOpt = item.q.options.find(o => o.letter === item.chosen);
      const correctOpt = item.q.options.find(o => o.letter === item.q.correct);
      return '<div class="wrong-item">' +
        '<div class="wi-n">Q' + item.q.global_n + '</div>' +
        '<div class="wi-q">' +
          '<div class="wi-situation">' + md(item.q.situation) + '</div>' +
          '<div class="wi-prompt">' + md(item.q.question) + '</div>' +
          '<div class="wi-ans">' +
            'Your answer: <span class="wi-wrong-tag">' + item.chosen + '</span> — ' + md(chosenOpt ? chosenOpt.text : '') + '<br>' +
            'Correct: <span class="wi-correct-tag">' + item.q.correct + '</span> — ' + md(correctOpt ? correctOpt.text : '') +
          '</div>' +
        '</div></div>';
    }).join('');
    wrongGroupsHtml +=
      '<div class="group-block">' +
        '<div class="group-title">' + scenario +
          '<span class="group-badge">' + items.length + ' incorrect</span></div>' +
        rows +
      '</div>';
  }

  const unansweredNote = unanswered > 0
    ? '<p style="color:#e53e3e;font-size:14px;margin-bottom:20px;font-weight:600;">&#9888; ' + unanswered + ' question(s) not answered.</p>'
    : '';

  document.getElementById('summaryContent').innerHTML =
    '<h1>Exam Complete</h1>' +
    '<p class="summary-subtitle">You answered ' + answered + ' of ' + total + ' questions.</p>' +
    unansweredNote +
    '<div class="score-grid">' +
      '<div class="score-card total"><div class="big">' + pct + '%</div><div class="label">Score</div></div>' +
      '<div class="score-card correct-c"><div class="big">' + correct + '</div><div class="label">Correct</div></div>' +
      '<div class="score-card wrong-c"><div class="big">' + wrong + '</div><div class="label">Incorrect</div></div>' +
    '</div>' +
    (wrong > 0
      ? '<div class="section-title">Incorrect answers by scenario</div>' + wrongGroupsHtml
      : '<p style="color:#38a169;font-weight:700;font-size:17px;">All answered questions correct!</p>') +
    '<button class="restart-btn" onclick="restart()">Restart Exam</button>';
}

function restart() {
  state.answers = {};
  state.current = 0;
  document.getElementById('questionScreen').classList.add('active');
  document.getElementById('summaryScreen').classList.remove('active');
  renderQuestion(0);
  updateSidebar();
}

buildSidebar();
renderQuestion(0);
updateSidebar();
"""

def build(lang):
    questions = get_questions(lang)
    js_data = json.dumps(questions, ensure_ascii=False)
    title = LANG_TITLES[lang]
    js = JS.replace('__DATA__', js_data)

    HTML = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="shell">
  <nav class="sidebar">
    <div class="sidebar-header">Questions</div>
    <div class="sidebar-progress">Answered: <span id="answeredCount">0</span> / <span id="totalCount">0</span></div>
    <div class="sidebar-scroll" id="sidebarList"></div>
  </nav>
  <div class="main">
    <div class="topbar">
      <div class="topbar-title">{title}</div>
      <div class="topbar-nav">
        <span class="q-counter" id="qCounter"></span>
        <button class="nav-btn" id="prevBtn" onclick="navigate(-1)" disabled>&#8592; Prev</button>
        <button class="nav-btn" id="nextBtn" onclick="navigate(1)">Next &#8594;</button>
        <button class="nav-btn finish" id="finishBtn" onclick="showSummary()">Finish &amp; Review</button>
      </div>
    </div>
    <div class="content">
      <div class="screen active" id="questionScreen">
        <div class="q-card" id="qCard"></div>
      </div>
      <div class="screen" id="summaryScreen">
        <div class="summary show" id="summaryContent"></div>
      </div>
    </div>
  </div>
</div>
<script>{js}</script>
</body>
</html>"""

    out = os.path.join(ROOT_DIR, f'practical_test_{lang}.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(HTML)
    print(f"Written: practical_test_{lang}.html  ({len(HTML):,} bytes, {len(questions)} questions)")


for lang in BUILD_LANGS:
    build(lang)
