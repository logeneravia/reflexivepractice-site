#!/usr/bin/env python3
"""Build script for reflexivepractice.com static replacement.

All body text is verbatim from the WordPress archive (wp-archive/json/),
with WordPress block markup stripped. Regenerates every page in place.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("/coach/", "About Paul"),
    ("/experience/", "Experience"),
    ("/inspiration/", "Inspiration"),
    ("/testimonials/", "Testimonials"),
    ("/writing/", "Notes"),
    ("/good-conversations-with-paul/", "Good Conversations"),
]

TAGLINE = "helping people find paths to their ideal identity and life"


def page(path, title, body, desc=TAGLINE, active=None):
    depth = path.count("/")
    nav_items = []
    for href, label in NAV:
        cls = ' class="active"' if active == href else ""
        podcast = ' data-podcast=""' if "good-conversations" in href else ""
        nav_items.append(f'<a href="{href}"{cls}{podcast}>{label}</a>')
    nav_html = "\n        ".join(nav_items)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/jpeg" href="/img/favicon.jpeg">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="wordmark" href="/">Reflexive&nbsp;Practice</a>
    <nav class="site-nav">
        {nav_html}
        <a class="btn-nav" href="/getstarted/">Get started</a>
    </nav>
  </div>
</header>

<main>
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <p class="footer-name">Reflexive Practice</p>
    <p class="footer-tag">{TAGLINE}</p>
    <p class="footer-meta">Paul Harris &middot; <a href="/good-conversations-with-paul/">Good Conversations with Paul</a> &middot; <a href="https://www.youtube.com/@reflexivepractice">YouTube</a></p>
  </div>
</footer>
</body>
</html>
"""
    out = os.path.join(ROOT, path.lstrip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    print("wrote", out)


# ---------------------------------------------------------------- home
home = """
<div class="banner-strip"><img src="/img/practice-banner.png" alt="Reflexive Practice"></div>

<figure class="full-bleed"><img src="/img/ocean-at-sunrise.jpg" alt="Ocean at sunrise"></figure>

<section class="wrap narrow hero-statement">
  <h1>Our unwavering interconnectedness is our greatest source of power and our deepest weakness.</h1>
  <p class="center"><a class="btn" href="/coach/">Learn More</a></p>
</section>

<section class="wrap duo-images">
  <figure><img src="/img/home-image-2.jpg" alt=""></figure>
  <figure><img src="/img/ph-portrait.jpg" alt="Portrait of Paul Harris"></figure>
</section>

<section class="wrap two-col">
  <div class="col-quote">
    <blockquote>
      <p>To achieve our best future we must become skilled at getting out of our own way.</p>
      <cite>Paul Harris, Reflexive Practitioner</cite>
    </blockquote>
  </div>
  <div class="col-text">
    <p><strong>Reflexive Practice</strong> is a way of being in the world that invites thoughtful framing of all relationships to create meaning that is generative and life-giving.</p>
    <p>Relationships define us, hold us, shape us, and transform us. They exist with everything around us &#8211; the people we bump against daily, the activities we participate in, the things we think about, and the places we go.</p>
    <p>It is a wonder that we feel we have any ability to be our own person in this chaotic and influential world.</p>
    <p>The greatest shift we can make in our thinking is to deeply realise that we too can transform, shape, and define everything around us in exactly the way we are influenced.</p>
    <p>To harness our greatest strength is to become a practitioner of self, to learn how to frame, reframe, and create artefacts that draws a better life toward us with every waking moment.</p>
    <p><a class="btn" href="/getstarted/">Book an appointment</a></p>
  </div>
</section>

<figure class="full-bleed"><img src="/img/ocean.jpg" alt="Ocean"></figure>
"""
page("/", "Reflexive Practice &#8211; " + TAGLINE, home, active=None)

# ---------------------------------------------------------------- coach / About Paul
coach = """
<article class="wrap narrow page-body">
  <p class="kicker">Paul Harris</p>
  <p>&#8230; is passionate about personal and community transformation and seeks to understand the complex issues that interconnect all of us.&nbsp;His theories about identity and transformation have helped individuals and organisations discover ways to navigate and harness the complexity of the world and have helped them find paths to better futures.</p>
  <p>His belief is that our relationships with people, places, ideas, activities, and things are the most powerful influences on our decision making, but that we are never without power to change all of these in ways to realise our deepest ambitions, hopes, and aspirations for the future.</p>
  <p>For several years now Paul Harris has worked as a mentor with individuals seeking control and agency in their professional and personal lives. Paul&#8217;s unique holistic approach opens up possibilities for deep change for individuals and organisation for sustainable growth in all these disparate areas of work.</p>
  <p>He is a well-known community and business leader, based in Red Deer, Alberta, who has many years of success in directing and nurturing successful retail and hospitality businesses, non-profit organisations and in local government. With experience at national and international levels, Paul has synthesised his postgraduate study in Canada, USA, and Europe, with innovative development practice across the fields of personal growth, community development, the arts, and organisational innovation.</p>
</article>

<section class="wrap gallery-3">
  <figure><img src="/img/paul-harris-selfie.jpg" alt="Paul Harris"></figure>
  <figure><img src="/img/gallery-image-8.jpg" alt=""></figure>
  <figure><img src="/img/shadow.jpg" alt=""></figure>
</section>
"""
page("/coach/", "About Paul &#8211; Reflexive Practice", coach, active="/coach/")

# ---------------------------------------------------------------- experience
experience = """
<article class="wrap narrow page-body">
  <h1>Experience</h1>
  <p>I think of myself as a skilled generalist, I may even say a specialised generalist. Throughout my personal and professional life, I have developed skills in multiple disciplines, ranging from writing, cooking, and painting, to computer programming, community planning, and architecture. I started my first business at the age of 12 and haven&#8217;t looked back.</p>
  <p>I began my career in retail and hospitality in the mid 1980s. Since then, I have grown several businesses, and helped incubate numerous others. In Red Deer I am a partner in Sunworks Living, a business which provides specialised retail experience, business development, and quality accommodation. Sunworks also owns Tribe, one of Red Deer&#8217;s best restaurants.</p>
  <p>I have been a mentor to many would-be entrepreneurs. In the early 1990s I branched into property and housing development with a focus on sustainable, affordable, and healthy living.</p>
  <p>For the past 15 years I have worked in community development, designing policies and practices that help cities and organisations achieve their goals. I have facilitated visioning and planning which supports culture, housing, business, social diversity, and physical social infrastructure.</p>
  <p>My work has always been focused on the creation of healthy oganisations, systems and spaces that improve well-being.</p>
  <p>From 2010 through 2017 I worked as an elected city councillor in Red Deer, and served municipalities and Canada as a board and community member with the Federation of Canadian Municipalities. In addition to policy development promoting healthy communities I have taken a keen interest in promoting good governance within organisations.</p>
  <p>As has been a life long learner, I have studied linguistics, writing, business, computer science, music, arts, psychology, leadership, and philosophy. Currently I continue my learning in the fields of social constructionism, relational leadership, and coaching. My current work explores personal identity through the lens of relationships with the outside world.</p>
</article>

<div class="banner-strip"><img src="/img/practice-banner.png" alt="Reflexive Practice"></div>
"""
page("/experience/", "Experience &#8211; Reflexive Practice", experience, active="/experience/")

# ---------------------------------------------------------------- getstarted
getstarted = """
<article class="wrap narrow page-body">
  <h1>Get started</h1>
  <p>I will guide you to explore and make positive changes, to recognise what holds you back and propels you forward. Together, we&#8217;ll explore how relationships transform you. We&#8217;ll identify artefacts and habits in your life that continue to exert influence and help you become skilled at making new and better ones.</p>
  <p>We&#8217;ll look at how you create and participate in relationships and how to make shifts for the better.</p>
  <p>Together we&#8217;ll map who you are today and visualise who you would like to be, and we&#8217;ll create paths to help you transition over time.</p>
  <p>I will help you become your own guide on your journey to become a more fulfilling you.</p>
  <p>On your schedule, at your pace, I suggest that we work together for a minimum of eight, one hour sessions. Each session you&#8217;ll discover insights about yourself. You&#8217;ll leave with tools and ideas about how to find and take our own path to a better life.</p>
  <p>My goal is to help you break through existing patterns of being to discover new ways of thinking about yourself and the world, in ways that promote happiness and well-being.</p>
  <p>Get in touch if you&#8217;d like to have an initial conversation about my services and your goals.</p>
  <p class="contact-cta"><a class="btn" href="mailto:paul@sunworks.ca?subject=Reflexive%20Practice%20%E2%80%94%20getting%20started">Contact me</a></p>
  <figure class="logo-figure"><img src="/img/logo.jpg" alt="Reflexive Practice logo"></figure>
</article>
"""
page("/getstarted/", "Get started &#8211; Reflexive Practice", getstarted, active=None)

# ---------------------------------------------------------------- podcast
podcast = """
<article class="wrap narrow page-body">
  <h1>Good Conversations with Paul</h1>
  <p>These are conversations for good &#8212; not merely pleasant conversations, but conversations that do good. Conversations that strengthen communities, deepen understanding, and remind us that disagreement need not mean division, but an invitation to curiosity and exploration.</p>
  <div class="video-embed">
    <iframe title="Good Conversations Episode 1: Erin Peden" src="https://www.youtube.com/embed/jOghLRtmqkA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <h2>Good Conversations Episode 1 &#8212; Erin Peden</h2>
  <p>We do not become ourselves in isolation. Our identities are shaped in relationship &#8212; by the people we associate with, the places we inhabit, the things we cherish, the ideas we explore, and the actions we take. In this first conversation, Paul sits down with Erin Peden to explore what it means to be truly present in dialogue &#8212; and what becomes possible when we listen with curiosity and courage.</p>
  <p><a class="btn" href="https://www.youtube.com/@reflexivepractice">Subscribe on YouTube</a></p>
</article>
"""
page("/good-conversations-with-paul/", "Good Conversations with Paul &#8211; Reflexive Practice", podcast, active="/good-conversations-with-paul/")

# ---------------------------------------------------------------- testimonials
testimonials = """
<article class="wrap narrow page-body">
  <h1>Testimonials</h1>
  <div class="testimonial">
    <p>Paul supported me in completing and writing up my PhD. My focus was on leadership and gender, but I was finding it really difficult to plan the writing, as well as apply myself to the task day-by-day. Paul demonstrated some simple tools to help me with self-organising and encouraged me to make progress one day at a time. He also ensured that I recognised my own insights and encouraged me to express those clearly: the result was a thesis that passed first time, with no amendments, of which I remain extremely proud. My career was transformed and I still use those techniques fifteen years later.</p>
    <p class="attribution">&#8212;&nbsp; Dr Alan Taylor</p>
  </div>
  <div class="testimonial">
    <p>Paul&#8217;s acute insights into the relational &#8212; building connection among and between people &#8212; greatly helped me consider not only my own personal and social relationships, but also how to see the world differently.</p>
    <p class="attribution">&#8212; Derek Gladwin, author of Rewriting Our Stories: Education, Empowerment, and Well-being</p>
  </div>
  <div class="testimonial">
    <p>I first met Paul many years ago as a colleague working at the municipal level of government and collaborating at the national level. He was always creative&nbsp; and inspirational in the way he worked with people, facilitating positive approaches and outcomes.&nbsp;&nbsp; He brought a sort of magic to the room when a group of people were together, not only making our work productive but joyful. Knowing Paul has changed how I see the world, expanding my thinking and bringing new understanding and much inspiration.</p>
    <p class="attribution">&#8212; Jenny Gerbasi, Former Winnipeg City Councillor,&nbsp; Former President Federation of Canadian Municipalities</p>
  </div>
</article>
"""
page("/testimonials/", "Testimonials &#8211; Reflexive Practice", testimonials, active="/testimonials/")

# ---------------------------------------------------------------- inspiration
inspiration = """
<article class="wrap page-body">
  <h1>Inspiration</h1>
  <div class="inspiration-grid">
    <div class="insp-col">
      <p class="insp-quote">The day when you wake in the morning and your first thought is, &#8216;Huzzah, this one is going to be awesome!</p>
      <figure class="insp-img"><img src="/img/img-4177.jpg" alt=""></figure>
      <p class="insp-quote">Some days the thing you need to say to yourself the most is, &#8216;it&#8217;s okay to take a break from life and have a nap.&#8217;</p>
      <figure class="insp-img"><img src="/img/img-0974.jpg" alt=""></figure>
      <p class="insp-quote">Finding a personal balance between caring for one&#8217;s self and caring for others is one of the most complicated and intriguing conundrums of complex modern life &#8211; particularly in a world that&#8217;s full of constantly shifting relationships which continue to influence our identities.</p>
    </div>
    <div class="insp-col">
      <figure class="insp-img"><img src="/img/img-1852.jpg" alt=""></figure>
      <p class="insp-quote">The space in between is where we work together to create meaning.&nbsp; To be changed through our meaning-making we must practice ways of engaging in our partnership or co-creators.</p>
      <figure class="insp-img"><img src="/img/img-0294.jpg" alt=""></figure>
      <p class="insp-quote">Every conversation changes the future in some way.</p>
      <figure class="insp-img"><img src="/img/img-1512.jpg" alt=""></figure>
    </div>
    <div class="insp-col">
      <p class="insp-quote">Friends make a difference.</p>
      <figure class="insp-img"><img src="/img/img-0151.jpg" alt=""></figure>
      <p class="insp-quote">It&#8217;s only the future that can judge the past. Be very careful what you create in the present.</p>
      <figure class="insp-img"><img src="/img/img-0106.jpg" alt=""></figure>
      <p class="insp-quote">If you want to know where your heart is, pay attention to where your mind goes when it wanders off.</p>
      <figure class="insp-img"><img src="/img/painting-2.jpg" alt=""></figure>
    </div>
  </div>
</article>
"""
page("/inspiration/", "Inspiration &#8211; Reflexive Practice", inspiration, active="/inspiration/")

# ---------------------------------------------------------------- writing index (Notes)
writing = """
<article class="wrap narrow page-body">
  <div class="banner-strip in-page"><img src="/img/practice-banner.png" alt="Reflexive Practice"></div>
  <h1>Notes</h1>
  <ul class="post-list">
    <li>
      <p class="post-date">5 November 2022</p>
      <h2><a href="/writing/myopic-spirals/">Myopic spirals</a></h2>
      <p>There are days that the difficult situations we must deal with cloud our broader image of life.</p>
    </li>
    <li>
      <p class="post-date">27 April 2022</p>
      <h2><a href="/writing/small-reflexive-moments/">Small reflexive moments</a></h2>
      <p>In a chaotic world we can be swept away by everything swirling around us.</p>
    </li>
  </ul>
</article>
"""
page("/writing/", "Notes &#8211; Reflexive Practice", writing, active="/writing/")

# ---------------------------------------------------------------- posts
myopic = """
<article class="wrap narrow page-body post">
  <p class="post-date">5 November 2022</p>
  <h1>Myopic spirals</h1>
  <p>There are days that the difficult situations we must deal with cloud our broader image of life. This week a colleague encountered a serious and even life threatening issue at their place of employment. Handling it the best way they could for the staff and company was perceived by some as irresponsible, who took to social media to express their opinion. As you might imagine, the pressure that short-sighted action put on my colleague was tremendously stressful. They took it very personally and began questioning their own response to the situation.</p>
  <p>When we have difficult issues to deal with we can often lose sight of our own bigger life picture. We can become myopic in our view of ourselves particularly. We might replay the story or circumstances again and again in our heads as if there were some hidden door to the past, that if found, we could go back and try a different approach&#8230; even if our original approach may well have been the very best one. We look to improve our present feelings by replaying that which can not be undone.</p>
  <p>And, in this spiral of story-telling we become so narrowly focused that everything else that makes up who we are seems to slip into the backseat. We let doom and gloom become the drivers.</p>
  <p>Reflexivity can help us break this downward spiral. By examining our own thoughts, motives and actions we can see how they are influencing how we feel about the present. This gives us the opportunity to consider more carefully the relationships that are helpful and life-giving and those that are not. New framing can certainly help us think through the challenges we face but sometimes our focus is so narrow that we miss the opportunity to situate our present troubles in the grander context of our lives.</p>
  <p>Without broad context we run the risk of giving our challenges more influence than they should have. It&#8217;s important to remember our past successes, our good nature, and our desire for improvement. All that we have accomplished so far, and the direction that we are headed are so important to add texture to our present situation, no matter how dire. Ignoring life context doesn&#8217;t help us navigate our current challenges with grace and sure-footedness.</p>
  <p>Reflexivity applied broadly on a whole life and all of its hiccups raises our confidence to handle today&#8217;s challenges, respect and appreciate yesterday&#8217;s learnings and successes, and helps us keep our eyes on the horizon for better times ahead.</p>
  <p>When my colleague was able to step back from the negativity that weighed them down and place it in the context with entirety of their impressive life, their good heart, and well-meaning actions, they were better able to navigate the horror of situation and determine the best way to proceed.</p>
  <p class="back-link"><a href="/writing/">&#8592; Notes</a></p>
</article>
"""
page("/writing/myopic-spirals/", "Myopic spirals &#8211; Reflexive Practice", myopic, active="/writing/")

small = """
<article class="wrap narrow page-body post">
  <p class="post-date">27 April 2022</p>
  <h1>Small reflexive moments</h1>
  <p>In a chaotic world we can be swept away by everything swirling around us. It&#8217;s important to hold time aside to gently quiet all of the relationships that pull us in. This may be as brief as a minute or two.</p>
  <p>During this time, be deliberate about your thoughts. Try not to dwell on what has needed immediate attention so far in the day. Instead, think about things that attract you to a better future. Try to look at them from all angles. Choose words that open up further exploration. Describe what you see to yourself, and perhaps others later. Notice how you feel. Breathe steadily and calmly.</p>
  <p>Take a moment during your stillness to write a few words or sentences about what you see in your deliberate moments of quiet. You need not write a lot, micro-journalling will help you shift ever so slightly in a better direction for yourself.</p>
  <p class="back-link"><a href="/writing/">&#8592; Notes</a></p>
</article>
"""
page("/writing/small-reflexive-moments/", "Small reflexive moments &#8211; Reflexive Practice", small, active="/writing/")

print("done")
