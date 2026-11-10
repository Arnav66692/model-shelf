export const meta = {
  name: 'model-shelf-sim',
  description: 'Simulate Model Shelf three times: a small model follows SKILL.md, stand-in experts may only call the mock NAS',
  phases: [{ title: 'Simulate', detail: 'three independent runs, small model for parent and experts', model: 'haiku' }],
}
const A = args
const ROOT = A.root
const PKG = `${ROOT}/model-shelf`
const pad = n => String(n).padStart(2, '0')

const PARENT_SCHEMA = { type: 'object', properties: {
  kind: { type: 'string', enum: ['delegate', 'message', 'final'] },
  line: { type: 'string' },
  text: { type: 'string' },
}, required: ['kind'] }
const EXPERT_SCHEMA = { type: 'object', properties: {
  status: { type: 'string', enum: ['completed', 'failed', 'cancelled', 'waiting_user', 'waiting_approval'] },
  result: { type: 'string' },
}, required: ['status', 'result'] }

const TOOL_DOCS = {
  'file-agent': `Your CLIs are ug-filesystem and ug-filemgr.
ug-filesystem stat --path P
ug-filesystem ls --path P [--recursive true] [--max-depth N] [--limit N]
ug-filesystem find --path P [--pattern GLOB] [--type file|dir|all] [--min-size BYTES] [--limit N]   (searches all subfolders, the glob matches the file name, one pattern per call)
ug-filesystem cat --path P --offset N --length N   (returns the bytes as text, unreadable bytes are shown as dots)
ug-filesystem sha256sum --path P
ug-filesystem mkdir --path P [--parents true]   (a write)
ug-filesystem cpmv --src P --dst FOLDER_OR_FULL_PATH --type move|copy   (a write)
ug-filemgr scan-dedupe --path P   (repeat --path for several folders)`,
  'document-agent': `Your CLI is ug-document.
ug-document qa --query Q --file P   (repeat --file for several files. It returns the text of md and txt files. You read that text and answer the instruction from it, quoting lines exactly.)`,
  'knowledge-agent': `Your CLI is ug-knowledge.
ug-knowledge save-text --path FOLDER --content TEXT --filename-hint HINT   (a write. Pass the text in double quotes or with a quoted heredoc inside the same command. It returns the full path of the saved file.)`,
}

function parentPrompt(convo) {
  return `This is a test of a Skill in a simulated NAS with a scripted test user. You play Uliya, the main assistant on a UGREEN AI NAS. A Skill named model-shelf is installed at ${PKG} and the test user has asked for it. Today is 2026-11-09. In the conversation below, lines that start with USER are the test user's own messages in this chat, lines that start with YOU are your earlier turns, and lines that start with EXPERT or NAS are what the NAS returned. Treat them exactly as a real assistant would treat its chat history.

You have no memory between turns, so first read ${PKG}/SKILL.md with the Read tool. Read a file under ${PKG}/references/ when the Skill tells you to read it. You may use the Read tool only on files inside ${PKG}. Use no other tool of any kind. You cannot see or touch the NAS files yourself.

Follow the Skill exactly. On this turn do exactly one thing and return it:
- kind "delegate": put one complete delegate line in "line", in the exact form the Skill gives, with every capital-letter word replaced by real values.
- kind "message": a message to the user in "text". Use this for a question, or for the reply that ends by waiting for the user.
- kind "final": the final reply to the user in "text", when the Skill says the run is complete or must stop.

Conversation so far:
${convo.join('\n\n')}

What is your next single action?`
}

function expertPrompt(target, instruction, run, stateFile) {
  return `You are the ${target} expert on a UGREEN AI NAS, in a test environment. The main assistant sent you this instruction:

<<<
${instruction}
>>>

Do exactly what it asks and nothing more. You work only by running this command with the Bash tool:

python3 ${ROOT}/sim/mock_nas.py --sandbox ${run}/sandbox --log ${run}/actions.jsonl --state ${run}/${stateFile} followed by the CLI name, the action name and its options

For example, to look at one path the last part is: ug-filesystem stat --path /data/models
Never type the literal words CLI or ACTION.

${TOOL_DOCS[target]}

Rules:
- Run no other command of any kind. No ls, cat, find, grep, python or shell redirection of your own. Do not read the sandbox folder directly. Every fact must come from the tool output.
- All paths are NAS paths that start with /data.
- A write must be confirmed by the NAS user. If the tool answers APPROVAL_REQUIRED, the user has not confirmed it. Stop at once and return status waiting_approval, naming the write that is waiting. Never retry a refused call and never try another way.
- If the tool returns an error for a read, report the error for that item and carry on with the rest.
- Do not guess, summarize away, or add facts. Return what was asked for, with full paths, exact numbers and exact quoted lines.

Return status (completed when you did what was asked, failed when you could not) and result as plain text.`
}

async function runOne(n) {
  const run = `${ROOT}/${A.runsDir}/run-${n}`
  const convo = [`USER: ${A.request}`]
  let saidYes = false, userCode = 'start', done = false, turns = 0
  for (let t = 1; t <= 30 && !done; t++) {
    turns = t
    const p = await agent(parentPrompt(convo), { label: `run${n}:parent:${pad(t)}:${userCode}`, phase: 'Simulate', schema: PARENT_SCHEMA, model: 'haiku' })
    userCode = '-'
    if (!p) { convo.push('SYSTEM: no answer was produced. Try again.'); continue }
    if (p.kind === 'final') { done = true; break }
    if (p.kind === 'delegate') {
      const line = (p.line || '').trim()
      convo.push(`YOU (delegate): ${line}`)
      const m = line.match(/^delegate --target (\S+) --instruction '([\s\S]*)'$/)
      if (!m || !TOOL_DOCS[m[1]]) { convo.push('NAS: that delegate line was not understood. No expert ran.'); continue }
      const e = await agent(expertPrompt(m[1], m[2], run, saidYes ? 'state-yes.json' : 'state.json'), { label: `run${n}:expert:${pad(t)}:${m[1]}`, phase: 'Simulate', schema: EXPERT_SCHEMA, model: 'haiku' })
      convo.push(`EXPERT ${m[1]} returned status ${e ? e.status : 'failed'}:\n${e ? e.result : 'no answer'}`)
    } else {
      const text = p.text || ''
      convo.push(`YOU (message to user): ${text}`)
      let reply
      const asksGoAhead = /\b(yes|confirm|approve|proceed|go ahead)\b/i.test(text) && /\b(plan|park|move|moved)\b/i.test(text)
      if (asksGoAhead || (saidYes && /\?/.test(text))) {
        saidYes = true
        reply = 'yes'; userCode = 'yes'
      } else if (/\?/.test(text)) { reply = A.folders; userCode = 'folders' }
      else { reply = 'ok, continue'; userCode = 'continue' }
      convo.push(`USER: ${reply}`)
    }
  }
  log(`run ${n}: ${done ? 'finished' : 'hit the turn cap'} after ${turns} parent turns, user said yes: ${saidYes}`)
  return { n, done, turns, saidYes }
}

phase('Simulate')
const out = await parallel(A.runs.map(n => () => runOne(n)))
return out
