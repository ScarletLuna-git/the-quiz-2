import random
import webbrowser
import tempfile

QUESTIONS = [
  {"q": "Which of the following is NOT part of preparing for data collection?", "correct": "Plan your programs after you arrive at the client's session", "wrong": ["Read data from last session", "Determine what programs you will run", "Gather materials for programs"]},
  {"q": "Which best describes permanent product recording?", "correct": "Mary asked a substitute to give a quiz while she was sick, then graded it the next day.", "wrong": ["Dianne checks on her kids' rooms 10 minutes after telling them to clean.", "John set up cameras to monitor work progress when away.", "Glen asks his kids if they brushed their teeth after they come downstairs."]},
  {"q": "Your BCBA designs a behavior plan for aggression. After two weeks you think it's ineffective. What should you do?", "correct": "Communicate with your BCBA immediately and share your thoughts.", "wrong": ["Change the plan immediately — don't implement an ineffective plan.", "Wait for further guidance before saying anything.", "Start training the parents — the plan isn't being implemented at home."]},
  {"q": "Which does NOT accurately represent extinction?", "correct": "Extinction works as a punishment procedure", "wrong": ["Extinction works to reduce behavior", "Extinction can involve planned ignoring", "Extinction should be implemented 100% of opportunities"]},
  {"q": "Whenever his mother-in-law plans a visit, Bill immediately books a golf outing. What is the hypothesized function?", "correct": "Escape/Avoidance", "wrong": ["Attention", "Tangible", "Automatic"]},
  {"q": "Your friend ignores BCBA feedback and doesn't implement it. What has she failed to do?", "correct": "Respond appropriately to feedback", "wrong": ["Actively seek clinical direction in a timely manner", "Communicate with stakeholders", "Maintain professional boundaries to avoid dual relationships"]},
  {"q": "Miranda hid her wine bottle before her siblings visited. What type of intervention is this?", "correct": "Antecedent", "wrong": ["Consequence", "Avoidance", "Differential reinforcement"]},
  {"q": "Your BCBA wants you to identify what your client can and can't do in terms of skills. What procedure will you implement?", "correct": "Probing procedures", "wrong": ["Task analysis procedures", "Generalization procedures", "Maintenance procedures"]},
  {"q": "What should NOT be included in session notes?", "correct": "The client was visibly frustrated at this point", "wrong": ["When I arrived the client was eating breakfast", "Mom asked him 3 times to pick up his trash with no response", "I prompted the client and provided reinforcement upon completion"]},
  {"q": "Your BCBA instructs you to provide tokens every 3-5 correct responses. What reinforcement schedule is this?", "correct": "VR4", "wrong": ["FI4", "VI4", "FR4"]},
  {"q": "You want to measure the time between setting off one firework and the next. What measurement is most appropriate?", "correct": "IRT", "wrong": ["Frequency", "Rate", "Latency"]},
  {"q": "Jen gives attention when her husband puts shoes in the closet and ignores him when he puts them on the floor. What procedure is this?", "correct": "DRA", "wrong": ["DRI", "DRO", "DRL"]},
  {"q": "Which of the following is NOT the role of an RBT?", "correct": "Design reinforcement systems", "wrong": ["Implement behavior plans", "Conduct indirect assessments", "Assist with parent training"]},
  {"q": "A BCBA asks a new client basic knowledge questions. What is the BCBA most likely doing?", "correct": "Probing", "wrong": ["Shaping", "Reinforcing", "Communication training"]},
  {"q": "You notice you and another RBT are running programs differently. What is the most appropriate action?", "correct": "Tell your BCBA and ask for clarification for yourself and the other RBT", "wrong": ["Report the other RBT to the BCBA", "Ask the client's parents how the other RBT does things", "Ignore it — it was only one week of data"]},
  {"q": "What measurement system in ABA captures every instance a behavior occurs?", "correct": "Continuous measurement", "wrong": ["Discontinuous measurement", "Interval recording", "Permanent product recording"]},
  {"q": "During FCT you reinforce successive approximations of desired communication. What is this called?", "correct": "Shaping", "wrong": ["Probing", "Task analysis", "Receptive instruction"]},
  {"q": "Your client screams with no clear antecedents or consequences. Which would NOT be the function?", "correct": "Control", "wrong": ["Attention", "Tangible", "Sensory"]},
  {"q": "If you work 100 hours in April, what is the minimum required supervision hours?", "correct": "5 hours", "wrong": ["1 hour", "10 hours", "20 hours"]},
  {"q": "In which scenario would duration be the most appropriate measurement?", "correct": "Reducing the time it takes for a client to respond after mom calls their name", "wrong": ["Tracking time between meals for a client with an eating disorder", "Betting your driving route to the beach is faster", "Tracking the number of attempts to solve 10 math problems"]},
  {"q": "Jim recorded a detailed description of how a client physically responded. What is Jim describing?", "correct": "The topography of the behavior", "wrong": ["The function of the behavior", "The frequency of the behavior", "The magnitude of the behavior"]},
  {"q": "A skill is identified, a goal created, and a measurement procedure identified. What is the NEXT step?", "correct": "Gather baseline data", "wrong": ["Implement the procedures", "Collect and review intervention data", "Modify the plan if necessary"]},
  {"q": "A client can watch TV for 20 minutes if they get ready for school on time. This establishes a ___?", "correct": "Contingency", "wrong": ["Punisher", "Preference", "Function"]},
  {"q": "Tommy's teacher stopped responding to his noises and now he makes them louder and more often. What best describes this?", "correct": "Extinction burst", "wrong": ["Extinction", "Resistance to Extinction", "Extinction failure"]},
  {"q": "Your new client is a 13-year-old with severe aggression. What should be established before starting?", "correct": "Crisis/emergency plan", "wrong": ["DRO intervention", "Parent training", "Extinction procedures"]},
  {"q": "You only eat Krispy Kreme on Saturdays when the hot and fresh sign is on. What is the SD?", "correct": "The hot and fresh sign", "wrong": ["The diet", "It is Saturday morning", "The donut shop"]},
  {"q": "Why is it crucial to understand the function of each behavior?", "correct": "Function tells us why the behavior is occurring", "wrong": ["Function tells us what measurement system to use", "Function tells us how often to reinforce or punish", "Function tells us what the behavior looks like"]},
  {"q": "Fill in the blanks: Negative reinforcement involves ___ a stimulus which ___ behavior. Positive punishment involves ___ a stimulus which ___ behavior.", "correct": "removing; increases; adding; decreases", "wrong": ["adding; decreases; adding; increases", "removing; decreases; removing; increases", "removing; decreases; adding; increases"]},
  {"q": "Duration data for one hour: 5 min, 10 min, 8 min, 12 min. What percentage was the client talking to peers?", "correct": "58%", "wrong": ["50%", "54%", "41%"]},
  {"q": "To stay within ethical standards, who should you discuss specific case details with?", "correct": "RBTs and BCBAs involved with the case", "wrong": ["Only RBTs on the case and outside BCBAs not involved", "RBTs not on the case who know the client, and BCBAs involved", "Only BCBAs involved with the case"]},
  {"q": "If your BCBA asks you to graph frequency of insults per session, where would you record that data?", "correct": "Y-axis", "wrong": ["X-axis", "Condition change line", "Graph legend"]},
  {"q": "Your client requests you stop using food reinforcers. After talking with your BCBA, what is the best course of action?", "correct": "Pair the food with other unconditioned reinforcers to establish new reinforcers", "wrong": ["Continue using food — it's the only thing that works", "Refer the client to a dietician", "Immediately discontinue food and try new items until something works"]},
  {"q": "Bobby lets the client do checkout independently and only teaches the steps the client doesn't know. What type of task chain teaching is this?", "correct": "Backwards chaining", "wrong": ["Forward chaining", "Total task chaining", "Behavior chain interruption strategy"]},
  {"q": "A new BCBA corrects how you deliver reinforcement on their first visit. What is the most appropriate response?", "correct": "Accept the feedback and implement changes; communicate any questions immediately.", "wrong": ["Report the BCBA — they shouldn't give feedback after only one session", "Say you understand, but continue doing it your way when they leave", "Explain your way has worked in the past, so you should continue"]},
  {"q": "Which answer choice best describes behavior in observable and measurable terms?", "correct": "Sydney pulled her sister's hair. Her sibling pinched her back. Mom told them both no dessert.", "wrong": ["Ryen kicked students — probably because he failed a test earlier.", "Jimmy has been stressed; he declined lunch and a snack.", "Susy had an episode due to bipolar. Mom scheduled a med adjustment."]},
  {"q": "It took Devin 6 minutes to start walking to the table when peers asked him to play. What does this represent?", "correct": "Latency — 6 minutes", "wrong": ["Duration — 11 minutes", "IRT — 5 minutes", "Rate — 2 minutes"]},
  {"q": "Jim was taught to order from a menu at home. At the restaurant, he ordered a hamburger himself. What did Jim exhibit?", "correct": "Generalization", "wrong": ["Naturalistic Teaching", "Maintenance", "Differential reinforcement"]},
  {"q": "Differential reinforcement can lead to ___?", "correct": "All of the above", "wrong": ["Discrimination only", "Differentiation only", "Alternative behaviors only"]},
  {"q": "Which is the best example of automatic punishment?", "correct": "You buy a sweatshirt but it is too tight and itchy, so you stop wearing it.", "wrong": ["The sushi place is out of salmon so you order tuna.", "You take away your brothers' Xbox when they fight and they stop fighting.", "You try a faster route to work and now always take it."]},
  {"q": "Which is true about stimulus preference assessments?", "correct": "Certain stimulus preference assessments can establish a hierarchy", "wrong": ["They identify reinforcers for a client", "They should be conducted indirectly", "You should not run one more than once a month"]},
  {"q": "Your client screamed 6 times in a 2-hour session. What was the rate of screaming per hour?", "correct": "3 times per hour", "wrong": ["6 times per hour", "2 times per hour", "4 times per hour"]},
  {"q": "John's client says fruit when seeing apples, grapes, bananas, and pears. What is the client demonstrating?", "correct": "Stimulus generalization", "wrong": ["Response generalization", "Maintenance", "Overgeneralization"]},
  {"q": "Sarah hears the garbage truck and rushes to put out the trash. The sound of the garbage truck is a ___?", "correct": "Discriminative Stimulus", "wrong": ["Motivating Operation", "Prompt", "Reinforcer"]},
  {"q": "Your BCBA asks you to conduct an initial indirect assessment. Which is most appropriate?", "correct": "Interview", "wrong": ["Event recording", "Functional analysis", "Narrative recording"]},
  {"q": "Bonnie's parents give her cookies after dinner only if she did not eat a cookie before dinner. What type of intervention is this?", "correct": "Differential reinforcement of other behaviors (DRO)", "wrong": ["Differential reinforcement of alternative behaviors (DRA)", "Generalization training", "Punishment"]},
  {"q": "Which is NOT a way you should prepare for your session as an RBT?", "correct": "Discuss changes with other RBTs and supervisors after each session", "wrong": ["Have all materials before arriving", "Communicate with your supervisor when unsure how to implement an intervention", "Review prior session notes and plan your day upon arrival"]},
  {"q": "Chris's mom gives him a chore list. What is the best way to measure whether he completed it all?", "correct": "Permanent product recording", "wrong": ["Direct assessment", "Event recording", "Ask Chris when she gets home"]},
  {"q": "Your BCBA gives Jake attention every 3 minutes during dad's work calls regardless of Jake's behavior. What intervention is this?", "correct": "Non-contingent Reinforcement (NCR)", "wrong": ["Punishment", "VI3", "FR3"]},
  {"q": "During forced-choice assessments, your client always chooses the item on the right. What is most appropriate?", "correct": "Conduct a multiple-stimulus preference assessment instead", "wrong": ["Continue but prompt the client to occasionally choose from the left", "Switch to a single-stimulus preference assessment", "Select reinforcers without a preference assessment"]},
  {"q": "Partial interval recording across 6 thirty-second intervals with data: 1, 8, 0, 5, 9, 11 instances. How many responses are recorded?", "correct": "5", "wrong": ["6", "34", "0"]},
  {"q": "Money, tokens, and praise are examples of what type of reinforcement?", "correct": "Secondary", "wrong": ["Positive", "Primary", "Unconditioned"]},
  {"q": "Ben learned to order a California roll, then started ordering other menu items. This is an example of ___?", "correct": "Response Generalization", "wrong": ["Stimulus Generalization", "Maintenance", "Tacting"]},
  {"q": "Your BCBA instructs you to praise a client every 2 minutes he does not throw food. What type of intervention is this?", "correct": "DRO", "wrong": ["DRI", "DRA", "DRL"]},
  {"q": "Whenever mom says time for bed, Micah cries and begs to stay up late. What is the most likely function?", "correct": "Access to a tangible", "wrong": ["Escape/Avoidance", "Attention", "Automatic"]},
  {"q": "Glen provides the SD, waits for a response, provides a prompt, gives feedback, then pauses. What did Glen do wrong?", "correct": "Provided the prompt after the response", "wrong": ["Paused before the next SD", "Provided feedback after the response", "Waited for a response from the learner"]},
  {"q": "You prompt a client through every step of boiling noodles and provide reinforcement at the end. What type of task chaining is this?", "correct": "Total task", "wrong": ["Forward chaining", "Backward chaining", "Interruption strategy"]},
  {"q": "A client's parents buy Jen a jersey for her favorite team. If Jen accepts, this most likely represents a ___?", "correct": "Conflict of interest", "wrong": ["Lack of communication", "Acceptable scenario", "Illegal activity"]},
  {"q": "Which best represents an example of discontinuous measurement?", "correct": "During a 2-hour movie you take data for only 15 minutes on your client's attending.", "wrong": ["Recording how many times a client engages with others during recess", "Recording how long it takes your son to complete homework each night", "Recording how many times a client elopes during a 3-hour session"]},
  {"q": "Susie's sister draws on her paper less after Susie says she is done drawing with her. Susie's response is an example of ___?", "correct": "Negative punishment", "wrong": ["Positive reinforcement", "Negative reinforcement", "Positive punishment"]},
  {"q": "You count how many Olympic medals the USA has won. This is what type of measurement?", "correct": "Frequency", "wrong": ["Partial interval recording", "IRT", "Duration"]},
  {"q": "Every 60 seconds you check if the client is engaging in the target behavior and mark it down. What type of measurement is this?", "correct": "Momentary time sampling", "wrong": ["Frequency", "Partial interval recording", "Continuous measurement"]},
  {"q": "A parent asks your opinion on whether to enroll their child in school or homeschool. What is the best response?", "correct": "Recommend she consults your supervisor, and decline to give your opinion", "wrong": ["Give your honest opinion on schooling", "Ignore her and change the subject", "Ask to come off the case — this is a conflict of interest"]},
  {"q": "Which example best demonstrates a shaping procedure?", "correct": "Give a cookie for the c sound; progress to only giving the cookie as verbal attempts come closer to saying cookie.", "wrong": ["Give the cookie only when the client says cookie", "Give tokens for target behaviors; exchange for a cookie at 6 tokens", "Hold a note card with cookie please; gradually fade the words"]},
  {"q": "Grace uses a response cost procedure. What type of procedure is a response cost?", "correct": "Negative punishment", "wrong": ["Positive punishment", "Time-out", "Reprimand"]},
  {"q": "While showing friends photos, a video of your clearly visible client plays on your iPhone. Have you maintained client dignity?", "correct": "No, you violated the client's privacy.", "wrong": ["Yes — your friends do not know who the client is", "Yes — your BCBA gave you permission to film", "No — you should never film a client even when instructed to"]},
  {"q": "Which best represents discrimination training?", "correct": "Working with a client to identify healthy vs. unhealthy foods at a restaurant", "wrong": ["Providing Dr. Pepper only after 5 protest-free answers", "Ignoring screaming behavior and focusing elsewhere", "Leaving water and snacks to evoke spontaneous communication"]},
  {"q": "How often do RBTs need to retake the competency assessment as part of renewal?", "correct": "Every year", "wrong": ["Every 6 months", "Every 5 years", "As needed"]},
  {"q": "A client prefers a punishment-based treatment over a non-punishment option. What is the best course of action?", "correct": "Use the punishment procedure, but include a reinforcement component as well", "wrong": ["Use the punishment procedure by itself without reinforcement", "Deny the request — do not use punishment when other options exist", "Deny the request — clients do not have a say in treatment decisions"]},
  {"q": "Another name for the y-axis on a line graph is the ___?", "correct": "Ordinate", "wrong": ["Abscissa", "Baseline", "Trend Line"]},
  {"q": "What is the RBT's primary role in service delivery?", "correct": "Implementation", "wrong": ["Parent Training", "Behavior Management", "Functional Communication Training"]},
  {"q": "You have a bag of items and want to run a preference assessment using all items at once. What method is most appropriate?", "correct": "Multiple stimulus assessment", "wrong": ["Single stimulus assessment", "Forced choice assessment", "Reinforcer assessment"]},
  {"q": "Dave delivers a token every couple of problems his client completes independently. What best describes this reinforcement?", "correct": "Intermittent", "wrong": ["Continuous", "Natural", "Non-contingent"]},
  {"q": "What is the distinction between a task analysis and a behavior chain?", "correct": "Task analysis breaks down complex behavior. You teach the behavior chain.", "wrong": ["There is no distinction", "Task analysis are forward chains and behavior chains are backward chains", "The two are unrelated"]},
  {"q": "Tina's seat-leaving went away with extinction but returned last week. What is the most likely explanation?", "correct": "Spontaneous Recovery", "wrong": ["Extinction burst", "Tina is automatically reinforced", "Tina is bored in class"]},
  {"q": "You accidentally reinforce a behavior. What is the best course of action?", "correct": "Let your supervisor know as soon as possible", "wrong": ["Let the parents know immediately", "Do not report it, but correct your mistake", "Overcorrect by punishing the reinforced behavior"]},
  {"q": "Which describes a potential problem with punishment?", "correct": "All of the above", "wrong": ["Behavior returns if punishment stops", "Punishment does not teach a replacement behavior", "Clients may resist, leading to harsher forms"]},
  {"q": "Brynn stops playing a disliked song only when her daughter says please stop. Stopping the song is ___?", "correct": "Negative Reinforcement", "wrong": ["Positive Reinforcement", "Positive Punishment", "Negative Punishment"]},
  {"q": "A client's dad reports 4 hours of sleep per night for 3 sessions. What should you do as the RBT?", "correct": "Report this to your BCBA and make a note in your session notes", "wrong": ["Offer advice to the dad on sleep techniques", "Modify your treatment on poor-sleep days", "Allow the client to nap if they request it"]},
  {"q": "Using Chad's elopement graph (sessions 1-5 values: 4, 6, 5, 4, 6), what is the average frequency per session?", "correct": "5", "wrong": ["6", "4", "25"]},
  {"q": "AJ now waits for a physical prompt before selecting a color when given an SD. What best describes AJ in relation to prompting?", "correct": "AJ is prompt dependent", "wrong": ["AJ is resistant to prompts", "AJ is manipulating the RBTs", "AJ is too old to receive physical prompts"]},
]


def build_html(questions: list) -> str:
    import json
    q_json = json.dumps(questions, ensure_ascii=False)

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RBT Exam 3 Practice Quiz</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:       #0d0b14;
    --surface:  #13101f;
    --surface2: #1a1630;
    --border:   #2d2550;
    --p1:       #a855f7;
    --p2:       #7c3aed;
    --p3:       #c084fc;
    --p4:       #e879f9;
    --correct:  #86efac;
    --wrong:    #f87171;
    --text:     #ede9fe;
    --muted:    #7c6fa0;
    --radius:   14px;
  }
  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  body::before {
    content:'';
    position:fixed; inset:0; z-index:0;
    background:
      radial-gradient(ellipse 80% 60% at 10% 0%,  rgba(124,58,237,.18) 0%, transparent 60%),
      radial-gradient(ellipse 60% 50% at 90% 100%, rgba(168,85,247,.14) 0%, transparent 60%),
      radial-gradient(ellipse 40% 40% at 50% 50%,  rgba(232,121,249,.06) 0%, transparent 70%);
    pointer-events:none;
  }

  body::after {
    content:'';
    position:fixed; inset:0; z-index:0;
    background-image: radial-gradient(rgba(168,85,247,.15) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events:none;
  }

  #app { position:relative; z-index:1; max-width:760px; margin:0 auto; padding:40px 20px 80px; }

  .screen { display:none; }
  .screen.active { display:block; }

  /* START */
  #start-screen { text-align:center; padding-top:60px; animation:fadeUp .6s ease both; }

  .badge {
    display:inline-block;
    background: linear-gradient(135deg, rgba(168,85,247,.2), rgba(232,121,249,.12));
    border: 1px solid rgba(168,85,247,.45);
    color: var(--p3);
    font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase;
    padding:6px 18px; border-radius:100px; margin-bottom:28px;
  }

  h1 {
    font-family:'Syne', sans-serif;
    font-size: clamp(2.6rem, 7vw, 4.2rem);
    font-weight:800; line-height:1.05; margin-bottom:14px;
    background: linear-gradient(135deg, #e9d5ff 0%, #a855f7 45%, #e879f9 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  }

  .subtitle {
    color:var(--muted); font-size:.95rem; line-height:1.65;
    max-width:420px; margin:0 auto 52px;
  }

  .mode-grid {
    display:grid; grid-template-columns:1fr 1fr;
    gap:12px; max-width:500px; margin:0 auto 40px;
  }

  .mode-card {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:26px 22px; cursor:pointer;
    transition:all .22s ease; text-align:left; position:relative; overflow:hidden;
  }
  .mode-card::after {
    content:''; position:absolute; inset:0; opacity:0;
    background: linear-gradient(135deg, rgba(168,85,247,.1), transparent);
    transition:opacity .22s;
  }
  .mode-card:hover { border-color:rgba(168,85,247,.6); transform:translateY(-3px); box-shadow:0 12px 32px rgba(124,58,237,.25); }
  .mode-card:hover::after { opacity:1; }

  .mode-icon { font-size:1.7rem; margin-bottom:12px; }
  .mode-title { font-family:'Syne',sans-serif; font-weight:700; font-size:.95rem; margin-bottom:4px; }
  .mode-desc { color:var(--muted); font-size:.77rem; }
  .mode-count {
    position:absolute; top:14px; right:14px;
    font-size:.68rem; color:var(--p3); font-weight:700; letter-spacing:1px;
    background:rgba(168,85,247,.12); border:1px solid rgba(168,85,247,.25);
    padding:3px 9px; border-radius:100px;
  }

  /* QUIZ */
  #quiz-screen { animation:fadeUp .4s ease both; }

  .quiz-header {
    display:flex; align-items:center; justify-content:space-between;
    margin-bottom:28px; gap:16px;
  }

  .progress-wrap { flex:1; }
  .progress-label {
    font-size:.72rem; color:var(--muted); margin-bottom:8px;
    display:flex; justify-content:space-between;
  }
  .progress-bar { height:5px; background:var(--border); border-radius:100px; overflow:hidden; }
  .progress-fill {
    height:100%;
    background: linear-gradient(90deg, var(--p2), var(--p1), var(--p4));
    border-radius:100px; transition:width .4s ease;
  }

  .score-pill {
    background:rgba(168,85,247,.12);
    border:1px solid rgba(168,85,247,.3);
    border-radius:100px; padding:6px 18px;
    font-size:.8rem; color:var(--p3); font-weight:600; white-space:nowrap;
  }

  .question-card {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:20px; padding:36px 32px;
    margin-bottom:16px; position:relative; overflow:hidden;
  }
  .question-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:2px;
    background: linear-gradient(90deg, var(--p2), var(--p1), var(--p4));
  }
  .question-card::after {
    content:''; position:absolute; top:-60px; right:-60px;
    width:200px; height:200px;
    background:radial-gradient(circle, rgba(168,85,247,.08) 0%, transparent 70%);
    pointer-events:none;
  }

  .q-number {
    font-size:.68rem; color:var(--p3); font-weight:700;
    letter-spacing:2.5px; text-transform:uppercase; margin-bottom:14px;
  }
  .q-text {
    font-family:'Syne',sans-serif; font-size:1.08rem;
    font-weight:600; line-height:1.6; color:var(--text);
  }

  .choices-grid { display:grid; gap:10px; }

  .choice-btn {
    background:var(--surface);
    border:1.5px solid var(--border);
    border-radius:12px; padding:15px 20px;
    text-align:left; cursor:pointer;
    color:var(--text); font-family:'Inter',sans-serif;
    font-size:.88rem; line-height:1.45;
    transition:all .18s ease;
    display:flex; align-items:flex-start; gap:14px;
    position:relative;
  }
  .choice-btn:hover:not(:disabled) {
    border-color:rgba(168,85,247,.6);
    background:rgba(168,85,247,.07);
    transform:translateX(5px);
    box-shadow:0 0 20px rgba(124,58,237,.15);
  }
  .choice-btn:disabled { cursor:default; }

  .choice-letter {
    width:30px; height:30px; border-radius:8px; flex-shrink:0;
    background:var(--surface2); border:1px solid var(--border);
    display:flex; align-items:center; justify-content:center;
    font-size:.73rem; font-weight:700; color:var(--muted);
    transition:all .18s ease; font-family:'Syne',sans-serif;
  }
  .choice-btn:hover:not(:disabled) .choice-letter {
    background:rgba(168,85,247,.2); border-color:rgba(168,85,247,.5); color:var(--p3);
  }

  .choice-btn.correct { border-color:var(--correct); background:rgba(134,239,172,.07); animation:pop .35s ease; }
  .choice-btn.correct .choice-letter { background:var(--correct); border-color:var(--correct); color:#0d0b14; }

  .choice-btn.wrong { border-color:var(--wrong); background:rgba(248,113,113,.07); }
  .choice-btn.wrong .choice-letter { background:var(--wrong); border-color:var(--wrong); color:#0d0b14; }

  .choice-btn.reveal-correct { border-color:var(--correct); background:rgba(134,239,172,.04); }
  .choice-btn.reveal-correct .choice-letter { background:rgba(134,239,172,.2); border-color:var(--correct); color:var(--correct); }

  .feedback-bar {
    border-radius:12px; padding:13px 18px; margin-bottom:14px;
    font-size:.86rem; font-weight:500;
    display:none; align-items:center; gap:10px;
    animation:fadeUp .3s ease both;
  }
  .feedback-bar.show { display:flex; }
  .correct-fb { background:rgba(134,239,172,.08); border:1px solid rgba(134,239,172,.3); color:var(--correct); }
  .wrong-fb   { background:rgba(248,113,113,.07); border:1px solid rgba(248,113,113,.28); color:var(--wrong); }

  .next-btn {
    width:100%; padding:16px;
    background: linear-gradient(135deg, var(--p2), var(--p1), var(--p4));
    border:none; border-radius:12px;
    color:#fff; font-family:'Syne',sans-serif;
    font-size:.95rem; font-weight:700; cursor:pointer;
    display:none; transition:all .2s ease; letter-spacing:.4px;
  }
  .next-btn:hover { opacity:.9; transform:translateY(-2px); box-shadow:0 10px 28px rgba(124,58,237,.35); }
  .next-btn.show { display:block; animation:fadeUp .3s ease both; }

  /* RESULTS */
  #results-screen { text-align:center; animation:fadeUp .6s ease both; padding-top:40px; }

  .result-ring { width:170px; height:170px; margin:0 auto 32px; position:relative; }
  .result-ring svg { transform:rotate(-90deg); width:100%; height:100%; }
  .ring-bg   { fill:none; stroke:var(--border); stroke-width:8; }
  .ring-fill {
    fill:none; stroke-width:8; stroke-linecap:round;
    stroke:url(#rg); transition:stroke-dashoffset 1.1s cubic-bezier(.4,0,.2,1);
  }
  .result-center {
    position:absolute; inset:0;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
  }
  .result-pct {
    font-family:'Syne',sans-serif; font-size:2.5rem; font-weight:800; line-height:1;
    background: linear-gradient(135deg, #e9d5ff, #a855f7, #e879f9);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  }
  .result-pct-label { font-size:.68rem; color:var(--muted); margin-top:4px; }

  .result-title { font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; margin-bottom:10px; }
  .result-msg { color:var(--muted); margin-bottom:40px; line-height:1.65; }

  .stats-row { display:flex; justify-content:center; gap:14px; margin-bottom:40px; flex-wrap:wrap; }
  .stat-box {
    background:var(--surface); border:1px solid var(--border);
    border-radius:12px; padding:16px 28px; min-width:100px;
  }
  .stat-val { font-family:'Syne',sans-serif; font-size:1.7rem; font-weight:800; color:var(--p3); }
  .stat-label { font-size:.68rem; color:var(--muted); margin-top:4px; letter-spacing:.8px; text-transform:uppercase; }

  .btn-row { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }

  .btn {
    padding:13px 26px; border-radius:12px;
    font-family:'Syne',sans-serif; font-size:.88rem; font-weight:700;
    cursor:pointer; transition:all .2s; border:none;
  }
  .btn-primary { background: linear-gradient(135deg, var(--p2), var(--p1), var(--p4)); color:#fff; }
  .btn-primary:hover { opacity:.9; transform:translateY(-2px); box-shadow:0 10px 28px rgba(124,58,237,.35); }
  .btn-ghost { background:var(--surface); border:1.5px solid var(--border); color:var(--text); }
  .btn-ghost:hover { border-color:rgba(168,85,247,.5); background:rgba(168,85,247,.06); }

  #review-section { margin-top:48px; text-align:left; display:none; }
  #review-section.show { display:block; }

  .review-title {
    font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700;
    margin-bottom:18px; display:flex; align-items:center; gap:10px; color:var(--p3);
  }
  .missed-card {
    background:var(--surface); border:1px solid var(--border);
    border-left:3px solid rgba(248,113,113,.7);
    border-radius:12px; padding:20px; margin-bottom:12px;
  }
  .missed-q { font-size:.85rem; color:var(--muted); margin-bottom:10px; line-height:1.5; }
  .missed-answer { font-size:.85rem; display:flex; align-items:flex-start; gap:8px; }
  .missed-answer .label { color:var(--correct); font-weight:600; white-space:nowrap; }

  @keyframes fadeUp {
    from { opacity:0; transform:translateY(18px); }
    to   { opacity:1; transform:translateY(0); }
  }
  @keyframes pop {
    0%  { transform:scale(1); }
    50% { transform:scale(1.015); }
    100%{ transform:scale(1); }
  }

  @media(max-width:520px) {
    .mode-grid { grid-template-columns:1fr; }
    .question-card { padding:24px 18px; }
    .q-text { font-size:.96rem; }
  }
</style>
</head>
<body>
<div id="app">

  <div id="start-screen" class="screen active">
    <div class="badge">RBT Exam Prep</div>
    <h1>Exam 3<br>Practice Quiz</h1>
    <p class="subtitle">80 questions covering ABA principles, data collection, ethics, and behavior intervention. Pick a mode to begin.</p>
    <div class="mode-grid">
      <div class="mode-card" onclick="startQuiz('full')">
        <div class="mode-icon">📋</div>
        <div class="mode-title">Full Exam</div>
        <div class="mode-desc">All questions, shuffled</div>
        <div class="mode-count">80 Qs</div>
      </div>
      <div class="mode-card" onclick="startQuiz('ordered')">
        <div class="mode-icon">📖</div>
        <div class="mode-title">In Order</div>
        <div class="mode-desc">Original question order</div>
        <div class="mode-count">80 Qs</div>
      </div>
      <div class="mode-card" onclick="startQuiz('quick20')">
        <div class="mode-icon">⚡</div>
        <div class="mode-title">Quick 20</div>
        <div class="mode-desc">Random practice set</div>
        <div class="mode-count">20 Qs</div>
      </div>
      <div class="mode-card" onclick="startQuiz('quick10')">
        <div class="mode-icon">🎯</div>
        <div class="mode-title">Speed Round</div>
        <div class="mode-desc">Fast practice set</div>
        <div class="mode-count">10 Qs</div>
      </div>
    </div>
  </div>

  <div id="quiz-screen" class="screen">
    <div class="quiz-header">
      <div class="progress-wrap">
        <div class="progress-label">
          <span id="q-counter">Question 1 of 80</span>
          <span id="q-pct">0%</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
      </div>
      <div class="score-pill">✓ <span id="live-score">0</span></div>
    </div>
    <div class="question-card">
      <div class="q-number" id="q-number">QUESTION 1</div>
      <div class="q-text"  id="q-text"></div>
    </div>
    <div class="choices-grid" id="choices-grid"></div>
    <div class="feedback-bar" id="feedback-bar"></div>
    <button class="next-btn" id="next-btn" onclick="nextQuestion()">Next Question →</button>
  </div>

  <div id="results-screen" class="screen">
    <div class="result-ring">
      <svg viewBox="0 0 170 170">
        <defs>
          <linearGradient id="rg" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%"   stop-color="#7c3aed"/>
            <stop offset="50%"  stop-color="#a855f7"/>
            <stop offset="100%" stop-color="#e879f9"/>
          </linearGradient>
        </defs>
        <circle class="ring-bg"   cx="85" cy="85" r="72"/>
        <circle class="ring-fill" id="ring-fill" cx="85" cy="85" r="72"
          stroke-dasharray="452" stroke-dashoffset="452"/>
      </svg>
      <div class="result-center">
        <div class="result-pct" id="result-pct">0%</div>
        <div class="result-pct-label">Score</div>
      </div>
    </div>
    <div class="result-title" id="result-title">Great Work!</div>
    <p class="result-msg" id="result-msg"></p>
    <div class="stats-row">
      <div class="stat-box"><div class="stat-val" id="stat-correct">0</div><div class="stat-label">Correct</div></div>
      <div class="stat-box"><div class="stat-val" id="stat-wrong">0</div><div class="stat-label">Missed</div></div>
      <div class="stat-box"><div class="stat-val" id="stat-time">0:00</div><div class="stat-label">Time</div></div>
    </div>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="restartQuiz()">Try Again</button>
      <button class="btn btn-ghost"   onclick="goHome()">Change Mode</button>
      <button class="btn btn-ghost"   id="review-btn" onclick="toggleReview()">Review Missed</button>
    </div>
    <div id="review-section">
      <div class="review-title">📝 Missed Questions</div>
      <div id="missed-list"></div>
    </div>
  </div>

</div>
<script>
const QUESTIONS = """ + q_json + """;
let quiz=[],current=0,score=0,missed=[],startTime,lastMode='full',answered=false;

function shuffle(a){
  const b=[...a];
  for(let i=b.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[b[i],b[j]]=[b[j],b[i]];}
  return b;
}

function startQuiz(mode){
  lastMode=mode; score=0; missed=[]; current=0;
  if(mode==='full')        quiz=shuffle(QUESTIONS);
  else if(mode==='ordered') quiz=[...QUESTIONS];
  else if(mode==='quick20') quiz=shuffle(QUESTIONS).slice(0,20);
  else                      quiz=shuffle(QUESTIONS).slice(0,10);
  showScreen('quiz-screen'); startTime=Date.now(); renderQuestion();
}

function renderQuestion(){
  answered=false;
  const q=quiz[current],total=quiz.length;
  document.getElementById('q-counter').textContent='Question '+(current+1)+' of '+total;
  const pct=Math.round((current/total)*100);
  document.getElementById('q-pct').textContent=pct+'%';
  document.getElementById('progress-fill').style.width=pct+'%';
  document.getElementById('live-score').textContent=score;
  document.getElementById('q-number').textContent='QUESTION '+(current+1);
  document.getElementById('q-text').textContent=q.q;
  const letters=['A','B','C','D'];
  const choices=shuffle([q.correct,...q.wrong]);
  const grid=document.getElementById('choices-grid');
  grid.innerHTML='';
  choices.forEach((c,i)=>{
    const btn=document.createElement('button');
    btn.className='choice-btn'; btn.dataset.choice=c;
    btn.innerHTML='<span class="choice-letter">'+letters[i]+'</span><span>'+c+'</span>';
    btn.onclick=()=>selectAnswer(c,btn,q.correct);
    grid.appendChild(btn);
  });
  const fb=document.getElementById('feedback-bar');
  fb.className='feedback-bar'; fb.textContent='';
  const nb=document.getElementById('next-btn');
  nb.className='next-btn';
  nb.textContent=current===quiz.length-1?'See Results →':'Next Question →';
}

function selectAnswer(choice,btn,correct){
  if(answered)return; answered=true;
  const btns=document.querySelectorAll('.choice-btn');
  btns.forEach(b=>b.disabled=true);
  const fb=document.getElementById('feedback-bar');
  if(choice===correct){
    btn.classList.add('correct'); score++;
    document.getElementById('live-score').textContent=score;
    fb.className='feedback-bar correct-fb show';
    fb.innerHTML='&#x2705; Correct!';
  }else{
    btn.classList.add('wrong');
    btns.forEach(b=>{ if(b.dataset.choice===correct) b.classList.add('reveal-correct'); });
    missed.push(quiz[current]);
    fb.className='feedback-bar wrong-fb show';
    fb.innerHTML='&#x274C; Incorrect &#x2014; correct answer: <strong style="margin-left:6px">'+correct+'</strong>';
  }
  document.getElementById('next-btn').classList.add('show');
}

function nextQuestion(){
  current++;
  if(current>=quiz.length) showResults();
  else renderQuestion();
}

function showResults(){
  const elapsed=Math.round((Date.now()-startTime)/1000);
  const total=quiz.length, pct=Math.round((score/total)*100);
  document.getElementById('result-pct').textContent=pct+'%';
  document.getElementById('stat-correct').textContent=score;
  document.getElementById('stat-wrong').textContent=missed.length;
  const m=Math.floor(elapsed/60),s=elapsed%60;
  document.getElementById('stat-time').textContent=m+':'+(s+'').padStart(2,'0');
  let title,msg;
  if(pct>=90){title='🌟 Excellent!';msg="You're ready for the RBT exam. Outstanding performance!";}
  else if(pct>=75){title='👍 Good Job!';msg="Solid foundation — review the missed questions to sharpen your knowledge.";}
  else if(pct>=60){title='📚 Keep Studying';msg="You're getting there! Focus on the topics you missed and try again.";}
  else{title='💪 Keep Going!';msg="Review the core concepts and give it another shot. You've got this!";}
  document.getElementById('result-title').textContent=title;
  document.getElementById('result-msg').textContent=msg;
  const circ=452,offset=circ-(pct/100)*circ;
  setTimeout(()=>{document.getElementById('ring-fill').style.strokeDashoffset=offset;},300);
  document.getElementById('review-btn').style.display=missed.length?'inline-block':'none';
  showScreen('results-screen');
}

function toggleReview(){
  const sec=document.getElementById('review-section');
  const btn=document.getElementById('review-btn');
  if(sec.classList.contains('show')){sec.classList.remove('show');btn.textContent='Review Missed';return;}
  const list=document.getElementById('missed-list');
  list.innerHTML='';
  missed.forEach((q,i)=>{
    list.innerHTML+='<div class="missed-card"><div class="missed-q">'+(i+1)+'. '+q.q+'</div><div class="missed-answer"><span class="label">&#x2713; Correct:</span><span>'+q.correct+'</span></div></div>';
  });
  sec.classList.add('show'); btn.textContent='Hide Review';
  sec.scrollIntoView({behavior:'smooth',block:'start'});
}

function restartQuiz(){document.getElementById('review-section').classList.remove('show');startQuiz(lastMode);}
function goHome(){document.getElementById('review-section').classList.remove('show');showScreen('start-screen');}
function showScreen(id){document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));document.getElementById(id).classList.add('active');window.scrollTo(0,0);}
</script>
</body>
</html>"""


def main():
    questions = [dict(q) for q in QUESTIONS]
    random.shuffle(questions)

    html = build_html(questions)

    tmp = tempfile.NamedTemporaryFile(
        delete=False, suffix=".html",
        mode="w", encoding="utf-8"
    )
    tmp.write(html)
    tmp.close()

    print("=" * 55)
    print("  RBT Exam 3 Practice Quiz")
    print("=" * 55)
    print(f"  Opening quiz in your browser...")
    print(f"  File: {tmp.name}")
    print("=" * 55)
    webbrowser.open(f"file://{tmp.name}")


if __name__ == "__main__":
    main()