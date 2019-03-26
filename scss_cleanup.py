
# coding: utf-8

# # Find unused classes in page to for better performance

# Put your scss code here in text or read from file

# In[ ]:


scss="""

.introduction {
  background: url("../images/landing/pattern.png") repeat, url("../images/landing/bg-intro.png");
  background-position: bottom, top;
  background-size: auto, cover;
  margin-top: -70px;
  padding: 64px 32px;
  position: relative; }
  @media screen and (max-width: 1300px) {
    .introduction {
      padding-top: 100px; } }
  .introduction strong {
    color: #333333; }
  .introduction h1 {
    margin-top: -8px; }
  .introduction .introduction-holder {
    margin: auto;
    position: relative;
    width: 740px; }
  .introduction .design-system-img {
    margin-top: 3em; }
    .introduction .design-system-img .divider-tool-and-pencil {
      width: 130px; }
    .introduction .design-system-img .divider-tool {
      margin: 1.3em 1.3em 0; }
    .introduction .design-system-img .divider-tool-and-pencil,
    .introduction .design-system-img .ruler-and-keyboard,
    .introduction .design-system-img .mouse {
      display: inline-block;
      vertical-align: bottom; }
    .introduction .design-system-img .ruler-and-keyboard {
      margin-left: 24px;
      width: 400px; }
    .introduction .design-system-img .ruler {
      margin-bottom: 16px;
      width: 310px; }
    .introduction .design-system-img .mouse {
      height: 110px;
      margin-left: 24px;
      width: 90px; }
    .introduction .design-system-img .svg-line-to-consistency {
      position: absolute;
      right: 28px;
      top: 93px; }
  .introduction .consistency-autonomy-img {
    margin-top: 13em; }
    .introduction .consistency-autonomy-img .mobile-phone,
    .introduction .consistency-autonomy-img .laptop,
    .introduction .consistency-autonomy-img .title,
    .introduction .consistency-autonomy-img .laptop-mobile {
      display: inline-block; }
    .introduction .consistency-autonomy-img .mobile-phone,
    .introduction .consistency-autonomy-img .laptop {
      vertical-align: bottom; }
    .introduction .consistency-autonomy-img .mobile-phone {
      margin-right: 16px;
      width: 50px; }
    .introduction .consistency-autonomy-img .laptop {
      width: 310px; }
    .introduction .consistency-autonomy-img .laptop-mobile {
      width: 380px; }
    .introduction .consistency-autonomy-img .laptop-mobile,
    .introduction .consistency-autonomy-img .title {
      vertical-align: top; }
    .introduction .consistency-autonomy-img .title {
      margin-left: 32px;
      width: 320px; }
    .introduction .consistency-autonomy-img h1 {
      display: flex;
      flex-direction: column;
      margin-top: 0; }
    .introduction .consistency-autonomy-img .svg-line-to-market {
      left: 19px;
      position: absolute;
      top: 214px; }
  .introduction .fast-market-img {
    margin-top: 11em;
    padding-bottom: 80px; }
    .introduction .fast-market-img .title,
    .introduction .fast-market-img .monitor {
      display: inline-block;
      vertical-align: top; }
    .introduction .fast-market-img .title {
      width: 370px; }
    .introduction .fast-market-img .monitor {
      margin-left: 2.4em;
      margin-top: -30px;
      width: 300px; }
  
  @media screen and (max-width: 769px) {
    .features {
      padding: 120px 0 45px 0; } }
  .features h2 {
    color: #ff420a;
    letter-spacing: 1em;
    margin-left: 24px;
    text-transform: uppercase; }
  .features .btn:not(:first-of-type) {
    margin-left: 16px; }
  .features .feature-holder {
    align-items: center;
    display: flex;
    padding-top: 8em; }
    @media screen and (max-width: 1336px) {
      .features .feature-holder {
        flex-direction: column; } }
    .features .feature-holder .features-btn-group {
      display: flex;
      justify-content: start; }
  @media screen and (max-width: 1336px) {
    .features .feature-holder-reverse {
      flex-direction: column-reverse; } }
  .features .bubble {
    align-items: center;
    display: flex;
    flex: 0 0 420px;
    height: 390px;
    justify-content: center;
    position: relative;
    width: 420px; }
    .features .bubble h3 {
      letter-spacing: 1em;
      margin-right: -1em;
      margin-top: -15px;
      text-align: center;
      z-index: 5; }
  .features .bubble-dark-orange,
  .features .bubble-light-orange,
  .features .bubble-pink,
  .features .bubble-blue {
    border-radius: 50%;
    height: 330px;
    position: absolute;
    width: 330px; }
  .features .bubble-dark-orange {
    background-color: rgba(255, 66, 10, 0.4); }
    .features .bubble-dark-orange.bubble-3 {
      background-color: rgba(255, 66, 10, 0.7); }
  .features .bubble-blue {
    background-color: rgba(53, 185, 171, 0.4); }
    .features .bubble-blue.bubble-3 {
      background-color: rgba(53, 185, 171, 0.7); }
  .features .bubble-light-orange {
    background-color: rgba(255, 152, 10, 0.4); }
    .features .bubble-light-orange.bubble-3 {
      background-color: rgba(255, 152, 10, 0.7); }
  .features .bubble-pink {
    background-color: rgba(188, 2, 137, 0.4); }
    .features .bubble-pink.bubble-3 {
      background-color: rgba(188, 2, 137, 0.7); }
  .features .bubble-1 {
    left: 0;
    top: 0; }
  .features .bubble-2 {
    right: 0;
    top: 0; }
  .features .bubble-3 {
    left: 45px;
    top: 15px; }
  .features .bubble-4 {
    bottom: 0;
    left: 45px; }
    @media screen and (max-width: 1336px) {
      .features .bubble-4 {
        bottom: 20px; } }
  .features .bubble-text {
    padding: 4em; }
    .features .bubble-text p {
      line-height: 1.4em;
      padding: 1.3em 0; }
    .features .bubble-text h3 {
      text-transform: uppercase; }
  @media screen and (min-width: 770px) {
    .features .feature-holder
.bubble
"""



# HTML code goes here

# In[105]:


t="""<!DOCTYPE html><html><head><title>EOS Design System</title><meta name="description" content="EOS Design System is SUSE's solution for cohesive UX/UI in Open Source enterprise products. It helps developers to autonomously deliver consistent UX and engaging interfaces."><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0"><meta property="og:title" content="EOS Open Source Design System"><meta property="og:type" content="website"><meta property="og:url" content="http://www.eosdesignsystem.com"><meta property="og:image" content="https://res.cloudinary.com/eosdesignsystem/image/upload/v1550833469/EOS/Social/eos-design-system.jpg"><link rel="stylesheet" href="/build/css/vendors.min.css"><link rel="stylesheet" href="/stylesheets/application-landing.css"><script src="/build/js/vendors.min.js"></script><script src="/javascripts/application-landing.min.js"></script><script src="/javascripts/shared/gtm-head.js"></script></head><body><div class="cookies-alert js-cookies-alert"><div class="cookies-alert-body"><p>The EOS Design System uses cookies to help us learn more about how we can improve the design system.<br><a href="/cookies-policy">Learn more about our cookie policy</a></p></div><div class="cookies-alert-buttons"><button class="btn btn-primary js-cookies-accept">Accept</button><a class="btn btn-default change-preference" href="/cookies-policy">Edit preferences</a></div></div><nav class="main-menu js-main-menu"><div class="row"><div class="col-md-4 col-sd-12"><img class="logo" src="/images/landing/logo-colors.svg"><img class="logo" src="/images/landing/logo-white.svg"><a class="landing-mobile-burger js-landing-mobile-burger"><i class="material-icons md-18">menu</i></a></div><div class="col-md-8 col-sd-12 text-right mobile-submenu-landing js-mobile-submenu-landing"><a class="btn btn-link smoothScroll" data-linkto="js-eos">What is EOS</a><a class="btn btn-link smoothScroll" data-linkto="js-features">Features</a><a class="btn btn-link smoothScroll" data-linkto="js-contact">Contact</a><a class="btn btn-default get-started" href="/dashboard">Check out SUSE DS</a></div></div></nav><section class="introduction" id="js-eos"><article class="container-fluid"><h1 class="text-center"><strong>ONE DESIGN SYSTEM </strong>ENDLESS POSSIBILITIES</h1><h3 class="text-center">The open source solution for cohesive UX/UI across products.</h3><div class="introduction-holder design-system-img"><div class="divider-tool-and-pencil"><img class="divider-tool wow fadeInUp" src="images/landing/divider-tool.svg"><img class="pencil wow fadeInUp" src="images/landing/pencil.svg" data-wow-delay="0.1s"></div><div class="ruler-and-keyboard"><img class="ruler wow fadeInUp" src="images/landing/ruler.svg" data-wow-delay="0.2s"><img class="keyboard wow fadeInUp" src="images/landing/keyboard.svg" data-wow-delay="0.3s"></div><img class="mouse wow fadeInUp" src="images/landing/mouse.svg" data-wow-delay="0.4s"><svg class="svg-line-to-consistency" xmlns="http://www.w3.org/2000/svg" width="372px" height="540px"><path class="path-to-consistency" fill="none" stroke="rgb(255, 255, 255)" stroke-width="3px" stroke-linecap="butt" stroke-linejoin="miter" d="M282.000,23.000 L282.000,2.000 L368.000,2.000 L368.000,277.361 L36.266,277.361 L36.266,535.401 L2.000,535.401"></path></svg></div><div class="introduction-holder consistency-autonomy-img"><div class="laptop-mobile"><img class="mobile-phone wow fadeInUp" src="images/landing/mobile-phone.svg" data-wow-offset="200"><img class="laptop wow fadeInUp" src="images/landing/laptop.svg" data-wow-delay="0.1s" data-wow-offset="200"></div><div class="title"><h1><strong>CONSISTENT,</strong><strong>AUTONOMOUS,</strong>AND<strong>BEAUTIFUL UIs</strong></h1><h3>EOS helps developers and designers to autonomously deliver consistent UX and engaging interfaces.</h3></div><svg class="svg-line-to-market" xmlns="http://www.w3.org/2000/svg" width="553px" height="484px"><path class="path-to-market" fill="none" stroke="rgb(255, 255, 255)" stroke-width="3px" stroke-linecap="butt" stroke-linejoin="miter" d="M6.000,2.000 L6.000,170.000 L373.000,170.000 L373.000,476.000 L545.000,476.000 L545.000,418.000"></path></svg></div><div class="introduction-holder fast-market-img"><div class="title"><h1>HELPING A FAST<br>MOVING MARKET <strong>MOVE FASTER</strong></h1><h3>The EOS Design System helps open source companies deliver bleeding edge software without losing focus on the user experience.</h3></div><img class="monitor wow fadeInUp" src="images/landing/monitor.svg" data-wow-offset="200"></div></article></section><section class="features" id="js-features"><article class="container container-fluid"><h2 class="text-center">features</h2><h3 class="text-center">The EOS Design System at a glance</h3><div class="feature-holder"><div class="bubble"><h3>Open <br>source</h3><div class="bubble-blue bubble-1 js-move-bubble wow bubble-fadeinupleft" data-wow-offset="0"></div><div class="bubble-blue bubble-2 js-move-bubble wow bubble-fadeinupright" data-wow-offset="0"></div><div class="bubble-blue bubble-3"></div><div class="bubble-blue bubble-4 js-move-bubble wow bubble-fadeindown" data-wow-offset="0"></div></div><div class="bubble-text"><h3>OPEN SOURCE DNA</h3><p>EOS offers an easily customizable Design System for any company or project to use. 
We created guides that are adjustable and applicable in any open source project. We appreciate your contribution to EOS and look forward to hearing more about how it helps your products and projects.</p><div class="features-btn-group"><a class="btn btn-default" href="https://gitlab.com/SUSE-UIUX/eos/issues" target="_blank">Contribute to EOS</a><a class="btn btn-default" href="https://gitlab.com/SUSE-UIUX/eos" target="_blank">Fork EOS</a></div></div></div><div class="feature-holder feature-holder-reverse"><div class="bubble-text"><h3>Color palette</h3><p>Text, call-to-action, status colors, and more. Using our example of 
SUSE colors, you can easily define and generate your product’s colors in 
a meaningful way to help developers and designers apply them consistently.</p><div class="features-btn-group"><a class="btn btn-default" href="/colors">Go to Color guide</a></div></div><div class="bubble"><h3>Colors</h3><div class="bubble-dark-orange bubble-1 js-move-bubble wow bubble-fadeinupleft" data-wow-offset="0"></div><div class="bubble-dark-orange bubble-2 js-move-bubble wow bubble-fadeinupright" data-wow-offset="0"></div><div class="bubble-dark-orange bubble-3"></div><div class="bubble-dark-orange bubble-4 js-move-bubble wow bubble-fadeindown" data-wow-offset="0"></div></div></div><div class="feature-holder"><div class="bubble"><h3>Icons</h3><div class="bubble-pink bubble-1 js-move-bubble wow bubble-fadeinupleft" data-wow-offset="300"></div><div class="bubble-pink bubble-2 js-move-bubble wow bubble-fadeinupright" data-wow-offset="300"></div><div class="bubble-pink bubble-3"></div><div class="bubble-pink bubble-4 js-move-bubble wow bubble-fadeindown" data-wow-offset="300"></div></div><div class="bubble-text"><h3>A handcrafted icons set and guideline</h3><p>We have created the EOS icon set, made to cover special use cases 
 and perfectly coexist with Material Design icons, our recommended iconic font.</p><div class="features-btn-group"><a class="btn btn-default" href="/icons">Go to icons</a><a class="btn btn-default" href="/icons/eos-icons-set">Go to EOS icon set</a></div></div></div><div class="feature-holder feature-holder-reverse"><div class="bubble-text"><h3>Unified communication standards to reach your audience</h3><p>Deliver clear, concise and useful messages, while keeping a 
consistent voice and tone across products. Write content that puts 
users first and helps your products sound like one unified 
brand. Follow the SUSE brand tone and voice to help you identify how your products 
should communicate with their users.</p><div class="features-btn-group"> <a class="btn btn-default" href="/writing">Go to writing guides</a></div></div><div class="bubble"><h3>Writing guide</h3><div class="bubble-light-orange bubble-1 js-move-bubble wow bubble-fadeinupleft" data-wow-offset="300"></div><div class="bubble-light-orange bubble-2 js-move-bubble wow bubble-fadeinupright" data-wow-offset="300"></div><div class="bubble-light-orange bubble-3"></div><div class="bubble-light-orange bubble-4 js-move-bubble wow bubble-fadeindown" data-wow-offset="300"></div></div></div></article></section><section class="bottom-links text-center" id="js-contact"><article class="container-fluid"><h3>Get in touch with us</h3><div class="bottom-links-items row"><div class="col-md-3"><h4><img class="bottom-links-icon" src="/images/landing/mail-min.svg">Feedback</h4><p>Got some ideas or something nice to say to us?</p><a class="btn btn-secondary" href="/cdn-cgi/l/email-protection#97f2f8e4baf3f2e4fef0f9bae4eee4e3f2fad7f0f8f8f0fbf2f0e5f8e2e7e4b9f4f8fa">Send us feedback</a></div><div class="col-md-3"><h4><img class="bottom-links-icon" src="/images/landing/forum.svg">Mailing list</h4><p>Join our mailing list to receive more information.</p><a class="btn btn-secondary" href="https://groups.google.com/forum/#!forum/eos-design-system" target="_blank">Subscribe</a></div><div class="col-md-3"><h4><img class="bottom-links-icon" src="/images/landing/gitlab-min.svg">Repository</h4><p>Do you want to fork EOS, contribute, or report an issue?</p><div class="btn-group-footer"><a class="btn btn-secondary" href="https://gitlab.com/SUSE-UIUX/eos/" target="_blank">Repository</a><a class="btn btn-secondary" href="https://gitlab.com/SUSE-UIUX/eos/issues/new?issue%5Bassignee_id%5D=&amp;issue%5Bmilestone_id%5D=" target="_blank">Report issue</a></div></div><div class="col-md-3"><h4><img class="bottom-links-icon" src="/images/landing/twitter.svg">Twitter</h4><p>Get the latest news, meet the team, and more</p><a class="btn btn-secondary" href="https://twitter.com/eosdesignsystem" target="_blank">EOS in Twitter</a></div></div></article></section><footer class="text-center">Made by UX/UI SUSE Team /<a class="landing-cookie-link" href="/cookies-policy">Cookie policy</a></footer><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body></html>"""


# In[106]:


from bs4 import BeautifulSoup


# In[107]:


soup = BeautifulSoup(t)


# In[108]:


soup
import re


# In[129]:


classes = [value 
           for element in soup.find_all(class_=True) 
           for value in element["class"]]


# In[110]:


not_use=[]
for i in classes:
    temp="." + i
    if scss.find(temp)==-1:
        not_use.append(i)


# In[122]:


class_names = re.findall(r'\.\w+(?:\w|-)+\s',scss)


# In[124]:


for i in range(0,len(class_names)):
    class_names[i]=class_names[i][1:-1]


# In[126]:


class_names=list(dict.fromkeys(class_names))


# ## Printing class names that are not used

# In[133]:


for i in class_names:
    if i not in classes:
        print(i)

