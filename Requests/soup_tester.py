import re
from pprint import pprint
from typing import List

import requests
from bs4 import Tag, BeautifulSoup

string_value = """
<div class="topbar">
    <a href="/" class="topbar__logo"><img src="/assets/img/logo-sevenstars.png" alt="Seven Stars"></a>
    <div class="topbar__desktopnav">
        <nav>
    <ul>

        <li class="">
            <a href="/opdrachtgever" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Opdrachtgever</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="active">
            <a href="/professional" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Professional</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/partner" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Partner</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/team" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Team</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/wemakeitspark" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">We make IT Spark</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/updates" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Updates</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/contact" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Contact</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>

        <li class="">
            <a href="/werkenbij" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible" style="color: #0FB239">
                                Werken Bij
                                <span id="internalVacancyAmount" class="nav-amount-circle" style="color: white"></span>
                            </div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="separator"></li>

    </ul>
</nav>

<script>
    fetch('/api/vacatures')
        .then(response => response.json())
        .then(data => { document.getElementById('internalVacancyAmount').innerHTML = data; });

</script>
    </div>

    <a href="//mijn.sevenstars.nl" class="startime-indicator">
        <div class="startime-label">
            Inloggen
        </div>
        <div class="avatar"></div>
    </a>

    <a href="#" class="topbar__mobile-toggle">
        <span id="hamburger-menu-text">menu</span>
        <div id="hamburger">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
    </a>


    
            <a href="#history-back" class="back-btn"><span class="icon icon-indent-arrow"></span></a>
</div>
<div class="mobilenav">
    <div class="mobilenav__bg"></div>
    <nav>
    <ul>
            <li class="">
                <a href="/" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                    <div class="reveal-mask__mask">
                        <div class="reveal-mask__line">
                            <div class="reveal-block reveal-block--gray">
                                <div class="reveal-block__line visible">Home</div>
                                <div class="reveal-block__block"></div>
                            </div>
                        </div>
                    </div>
                </a>
            </li>

        <li class="">
            <a href="/opdrachtgever" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Opdrachtgever</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="active">
            <a href="/professional" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Professional</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/partner" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Partner</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/team" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Team</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/wemakeitspark" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">We make IT Spark</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/updates" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Updates</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="">
            <a href="/contact" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible">Contact</div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>

        <li class="">
            <a href="/werkenbij" class="reveal-mask">
                <div class="reveal-mask__mask">
                    <div class="reveal-mask__line">
                        <div class="reveal-block reveal-block--gray">
                            <div class="reveal-block__line visible" style="color: #0FB239">
                                Werken Bij
                                <span id="internalVacancyAmount" class="nav-amount-circle" style="color: white"></span>
                            </div>
                            <div class="reveal-block__block"></div>
                        </div>
                    </div>
                </div>
            </a>
        </li>
        <li class="separator"></li>

            <li>
                <a href="//mijn.sevenstars.nl" class="reveal-mask" data-page-transition='{"transition": "slide"}'>
                    <div class="reveal-mask__mask">
                        <div class="reveal-mask__line">
                            <div class="reveal-block reveal-block--gray">
                                <div class="reveal-block__line visible startime-indicator startime-indicator-mobile">Inloggen StarTime</div>
                                <div class="reveal-block__block"></div>
                            </div>
                        </div>
                    </div>
                </a>
            </li>
    </ul>
</nav>

<script>
    fetch('/api/vacatures')
        .then(response => response.json())
        .then(data => { document.getElementById('internalVacancyAmount').innerHTML = data; });

</script>
</div>

<div class="site-container__inner">
    <div class="topbar-spacer"></div>

    <section class="vacature-header">
        <div class="vacature-header__content">
            <h1>Senior Testengineer</h1>

            <span class="status">Open</span>

            <div class="status-dots status-dots--dark">
                <div class="status-dots__holder">
                    <ul>
                        <li class="status-dots__dot-holder dot-holder dot-holder__active">
                            <p>Open</p>
                        </li>
                        <li class="status-dots__dot-holder dot-holder ">
                            <p>Kandidaten voorgesteld</p>
                        </li>
                        <li class="status-dots__dot-holder dot-holder ">
                            <p>Gesprekken gepland</p>
                        </li>
                        <li class="status-dots__dot-holder dot-holder  ">
                            <p>Ingevuld</p>
                        </li>
                    </ul>
                </div>
            </div>
            <a onclick="window.history.replaceState({}, '', 'senior-testengineer?reageer-direct=top');" class="btn vacancy-cta__btn vacancy-top-btn" id="show-vacature-form-top">Reageer direct</a>
        </div>
    </section>
    <div class="divided-sections">
        <section class="divided-sections__section article-content article-content--bg-gray">
            <div class="article-content__content">
                <h2>Functieomschrijving</h2>
                <span class="vacancy-icons">
                    <span>Tijdelijk</span>
                    <span class="icon icon-align-middle icon-clock"></span><span>36 uur/week</span>
                    <span class="icon icon-align-middle icon-contact-mapmarker"></span><span>Groningen</span>
                    <span class="icon icon-align-middle --offset icon-calendar"></span><span>Start 22 maart 2021</span>
                </span>
                <p>Team HO2 bestaat uit 2 ontwerpers, 2 bouwers, 2 testers en ongeveer 2 OPS’ers. Een mix van meer en minder ervaren teamleden, met&nbsp;gezamenlijk veel domeinkennis. Als devops-team werken we nauw en veel samen met onze functioneel beheerders.&nbsp;Samen ontwikkelen en beheren zij de applicaties van domein BRON HO en van 2BRON. Dit is een mix van oude, wat oudere en splinternieuwe&nbsp;applicaties.&nbsp;Momenteel moeten alle schermen van de applicatie worden omgebouwd van jsf naar Angular, in 2021 gaat dat een grote klus zijn. Verder zijn er&nbsp;altijd vernieuwingen, wetswijzigingen, en her en der een kleine aanpassing. Ook komt er een conversie naar RIO aan.</p><p><strong>Opdrachtomschrijving<br /></strong>Voor het Moderniseren van onze applicatie zijn we op zoek naar een ervaren tester met veel affiniteit voor testautomatisering zowel op het gebied&nbsp;van frontend, als ook backend. De bestaande testen zijn opgezet middels java/cucumber. Het is tijd om nu de testen voor alle applicaties&nbsp;gestructureerd in te zetten, en waar nodig te moderniseren naar nieuwe verbeterde methodes. Hiervoor zoeken we een ervaren tester met&nbsp;java/cucumber-ervaring. Naast die technische bagage zoeken we iemand die goed kan overleggen met alle betrokkenen (van analist tot&nbsp;functioneel beheerder, product owner en bouwers en ops), om een goede risico-analyse te kunnen maken en op basis daarvan advies te geven&nbsp;over testbreedte en -diepte. En daarna die tests natuurlijk ook maken/uitvoeren en onderhouden.&nbsp;Bron HO zoekt een tester<br /></p><ul><li>met affiniteit voor het testen van front-end en backend applicaties;</li><li>die kennis heeft van testautomatisering (Serenity, Cucumber, Java en eventueel voor de frontend Protractor, Cypress of Karma);</li><li>die een trekkersrol binnen het team kan vervullen op testgebied en hierin ook adviserend optreedt richting de productowner en andere&nbsp;stakeholders.</li><li>die kennis heeft van accessibility, user experience, security testing en continuous delivery.</li><li>die kennis en werkervaring heeft met REST, SQL en Kibana;</li><li>die kennis en werkervaring heeft met JIRA;</li></ul>

                <h2>Functie-eisen</h2>
                <ul><li>Minimaal 4 jaar werkervaring met Testen</li><li>Relevante werkervaring in een Agile / Scrum omgeving&nbsp;</li><li>HBO werk- en denkniveau</li><li>Minimaal 2 jaar aantoonbare ervaring met geautomatiseerd testen</li></ul><p><strong>Competenties<br /></strong></p><ul><li>Je bent eigenzinnig, denkt graag mee met allerhande team- en ontwikkelprocessen en handelt pro-actief.</li><li>Je bent leergierig en je hebt de moed om snel zelfstandig taken op te pakken.</li><li>Je vindt het leuk om met anderen samen te werken en uitleg te geven over je werk.</li><li>Je durft verder te kijken dan alleen de testtaken.</li><li>Je staat stevig in je schoenen</li></ul><p><strong>Aanvullende Kennis<br /></strong></p><ul><li>Kennis van back-end en met name front-end development.</li><li>Kennis en werkervaring met geautomatiseerd testen middels Cucumber, Java en Karma, Protractor of Cypress;</li><li>Kennis van accessibility, user experience, security testing en continuous delivery.</li><li>Kennis en werkervaring met REST, SQL en Kibana;</li><li>Kennis en werkervaring met JIRA;</li></ul><p><strong>Overige functiewensen</strong></p><p></p><p></p><p></p><ul><li>Werkervaring met het oplossen van productie incidenten.</li><li>Werkervaring met springboot, deliverystraat en diverse testtools</li></ul><p></p>

            </div>

            
            
            <div class="article-content__content article-content__content--multiple-no-embed">

                <h2>Overige informatie</h2>

                <p><strong>Startdatum:</strong> Start 22 maart 2021</p>

                <p><strong>Inzet:</strong> 36 uur/week</p>
                <p><strong>Duur:</strong> 12 maanden met optie op verlenging</p>
                <p><strong>Locatie:</strong> Groningen</p>

                <div class="vacancy-cta">
                    <h3>Reageer direct!</h3>
                    <p>
                        Net zo enthousiast als wij? Reageer dan direct op deze vacature.
                        Je kan je cv toevoegen, of er voor kiezen om je LinkedIn profiel te gebruiken.
                        Wel zo makkelijk!
                    </p>
                    <div>
                        <a onclick="window.history.replaceState({}, '', 'senior-testengineer?reageer-direct=bottom');" class="btn vacancy-cta__btn" id="show-vacature-form">Reageer direct</a>
                    </div>
                </div>

                <div id="vacature-form">
                    <form class="panel ajax-form" action="/vacature/aanmelden/direct/5239" enctype="multipart/form-data" method="post" novalidate="novalidate">
                        <input type="hidden" name="vacancyid" value="5239" />
                        <h2>Reageer direct</h2>
                        <fieldset>
                            <div class="fieldrow" style="display: none;">
                                <label for="placeholderField">Placeholder veld *</label>
                                <input name="placeholderField" type="text">
                            </div>
                            <div class="fieldrow">
                                <label for="firstname">Voornaam *</label>
                                <ul class="errors" data-errorgroup="node_name"> </ul>
                                <input name="firstname" type="text">
                                <span class="form-validation"></span>
                            </div>
                            <div class="fieldrow">
                                <label for="lastname">Achternaam *</label>
                                <ul class="errors" data-errorgroup="node_name"> </ul>
                                <input name="lastname" type="text">
                                <span class="form-validation"></span>
                            </div>
                        </fieldset>
                        <fieldset>
                            <div class="fieldrow">
                                <label for="email">E-mailadres *</label>
                                <ul class="errors" data-errorgroup="node_email"> </ul>
                                <input name="email" type="text">
                            </div>
                            <div class="fieldrow">
                                <label for="phonenumber">Telefoonnummer *</label>
                                <ul class="errors" data-errorgroup="node_phone"> </ul>
                                <input name="phonenumber" type="text">
                            </div>
                        </fieldset>
                        <fieldset>
                            <label>Cv</label>
                            <div class="formfield fieldrow--upload inline-file">
                                <ul class="errors" data-errorgroup="node_cv"> </ul>
                                <input type="file" name="cv" id="cv" />
                                <label for="cv">
                                    <i class="icon-check"></i>
                                    <div class="label-text">
                                        Kies een bestand...
                                        <span>Selecteren</span>
                                    </div>
                                </label>
                            </div>

                            <div class="fieldrow">
                                <label for="linkedin">LinkedIn profiel</label>
                                <ul class="errors" data-errorgroup="node_linkedin"> </ul>
                                <input name="linkedin" type="text">
                            </div>

                            <div class="fieldrow">
                                <label for="motivation">Motivatie</label>
                                <ul class="errors" data-errorgroup="node_text"> </ul>
                                <textarea rows="3" cols="50" name="motivation"></textarea>
                            </div>

                            <div class="fieldrow">
                                <label for="custom-select">Hoe heb je deze vacature gevonden?</label>
                                <select required class="select-css" id="foundthrough" name="foundthrough" onchange="if (this.value=='other'){this.form['foundthroughcustom'].style.visibility='visible'}else {this.form['foundthroughcustom'].style.visibility='hidden'};">
                                    <option selected value="Niet ingevuld">Kies een optie</option>
                                    <option value="LinkedIn">Via LinkedIn</option>
                                    <option value="Mijn netwerk">Via mijn netwerk</option>
                                    <option value="Een zoekmachine">Via een zoekmachine</option>
                                    <option value="other">Anders</option>
                                </select><br />
                                <input id="foundtroughcustom" type="text" name="foundthroughcustom" placeholder="Hoe heb je deze vacature gevonden?" style="visibility:hidden;" />

                                <span class="form-validation"></span>
                            </div>

                            <div class="formfield">
                                <label>
                                    <input type="checkbox" name="consent" id="consent" value="true" required />
                                    <span class="label-desc">
                                        <span class="text">
                                            Ja, ik geef toestemming aan Seven Stars om mijn
                                            persoonsgegevens te verwerken en ga akkoord met het
                                            <a href="/privacy" target="_blank" rel="noopener noreferrer"> privacystatement</a>
                                        </span>
                                    </span>
                                </label>
                                <ul class="errors" data-errorgroup="node_consent"></ul>
                                <span class="form-validation"></span>
                            </div>
                            <div class="g-recaptcha" name="captcha" id="captcha" data-sitekey="6Ld1m8cUAAAAAEVjd5fSNwU-A9OIwdhqVMhSaaoA"></div>
                        </fieldset>
                        <div class="wrap">
                            <span style="float: right; opacity: 0.5;">* verplichte velden</span>
                            <button class="btn">Verzenden</button>
                            <div class="ajax-form__loader">
                            </div>
                        </div>
                    </form>
                </div>



                <div class="vacancy-contact">
                    <span class="label__vacancy-contact">Contact Martijn</span>
                    <div class="vacancy-container">
                        <div class="vacancy-container__btns --white">

                            <div class="vacancy-btn"><a href="mailto:?subject=opdracht%3A%20Senior%20Testengineer&amp;body=Hi Martijn, ik heb interesse in de functie Senior Testengineer te Groningen." class="icon icon-btn-mail"></a></div>
                            <div class="tooltip">
                                <div class="vacancy-btn --small"><a href="tel:" class="icon icon-phone"></a></div>
                                <span class="tooltiptext"></span>
                            </div>
                            <div class="vacancy-btn --small"><a target="_blank" class="icon icon-whatsapp"></a></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="contact-block divided-sections__section">
    <div class="contact-block__content">
        <div class="contact-block__content__inner">
            <div class="silhouette silhouette--bg-white">
                <figure reveal-fade class="silhouette__figure
                        silhouette__figure--right">
                    <img src="/assets/img/silhouettes/profile-martijn.png" alt="">
                </figure>
                <div class="silhouette__content">
                    <div class="silhouette__text">
                        <figure reveal-fade class="silhouette__figure-mobile rounded-image" style="background-image: url('/assets/img/silhouettes/profile-martijn-small.png')">
                            <img src="/assets/img/silhouettes/profile-martijn-small.png" alt="">
                        </figure>
                        <h3 reveal-mask class="reveal-mask">
                            Meer weten?<br>Bel Martijn
                        </h3>
                        <p reveal-fade>
                            <span class="arrow-indent icon icon-indent-arrow"></span>
                            <span class="text-indent">
                                Op zoek naar een opdracht die bij jou past? Stop! Martijn is een echte doorpakker die jou met veel enthousiasme helpt naar een nieuwe opdracht. Neem contact met hem op en ga samen aan de slag!
                            </span>
                        </p>



                        <div class="vacancy-container">
                            <div class="vacancy-container__btns">
                                <div class="vacancy-btn"><a href="mailto:?subject=Vacature%3A%20Senior%20Testengineer&amp;body=Hi Martijn, ik heb interesse in de functie Senior Testengineer te Groningen." class="icon icon-btn-mail"></a></div>

                                <div class="tooltip">
                                    <div class="vacancy-btn --small"><a href="tel:" class="icon icon-phone"></a></div>
                                    <span class="tooltiptext"></span>
                                </div>

                                <div class="vacancy-btn --small"><a target="_blank" class="icon icon-whatsapp"></a></div>
                            </div>
                            <a onclick="window.history.replaceState({}, '', 'senior-testengineer?reageer-direct=right');" class="btn vacancy-btn-react" id="show-vacature-form-contact">REAGEER DIRECT</a>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


        <section class="article-bar">
    <div class="article-bar__mask">
            <a href="/vacature/6588/product-owner" class="article-bar__article article-item">
                <div class="item-border item-border--top"></div>
                <div class="item-border item-border--right"></div>
                <div class="item-border item-border--bottom"></div>
                <div class="item-border item-border--left"></div>
                <div class="article-item__content">
                    <div class="article-item__text">
                        <span class="label">Opdracht</span>
                        <h2>Product owner</h2>
                        <p>Voor onze opdrachtgever de Belastingdienst zijn wij op zoek naar een Product owner ketendashboard Loonheffingen Op deze aanvraag mogen geen freelancers worden aangeboden • Je bent verantwoordelijk voor het ophalen, identificeren en analyseren van de...</p>

                        <span class="vacancy-icons">
                            <span>Tijdelijk</span>
                            <span class="icon icon-align-middle icon-clock"></span><span>36 uur/week</span>
                            <span class="icon icon-align-middle icon-contact-mapmarker"></span><span>Utrecht</span>
                            <span class="icon icon-align-middle --offset icon-calendar"></span><span>Start 1 november 2021</span>
                        </span>
                    </div>
                </div>
            </a>
            <a href="/vacature/6587/medewerker-servicedesk" class="article-bar__article article-item">
                <div class="item-border item-border--top"></div>
                <div class="item-border item-border--right"></div>
                <div class="item-border item-border--bottom"></div>
                <div class="item-border item-border--left"></div>
                <div class="article-item__content">
                    <div class="article-item__text">
                        <span class="label">Opdracht</span>
                        <h2>Medewerker Servicedesk</h2>
                        <p>Voor onze opdrachtgever Justiti&#235;le ICT Organisatie i.o. zijn wij op zoek naar een Medewerker Servicedesk Het verlenen van 1e en 2e lijns ondersteuning per telefoon en het verzorgen van de registratie en bewaking van de per diverse kanalen...</p>

                        <span class="vacancy-icons">
                            <span>Tijdelijk</span>
                            <span class="icon icon-align-middle icon-clock"></span><span>36 uur/week</span>
                            <span class="icon icon-align-middle icon-contact-mapmarker"></span><span>Soesterberg</span>
                            <span class="icon icon-align-middle --offset icon-calendar"></span><span>Start 1 november 2021</span>
                        </span>
                    </div>
                </div>
            </a>
            <a href="/vacature/6586/medior-senior-backend-developer" class="article-bar__article article-item">
                <div class="item-border item-border--top"></div>
                <div class="item-border item-border--right"></div>
                <div class="item-border item-border--bottom"></div>
                <div class="item-border item-border--left"></div>
                <div class="article-item__content">
                    <div class="article-item__text">
                        <span class="label">Opdracht</span>
                        <h2>Medior/Senior Backend Developer</h2>
                        <p>Voor onze klant in de regio Zwolle zijn wij op zoek naar een ervaren Backend Developer. Aks Developer ben je onderdeel van het klantteam en help je mee om de klantomgevingen en webshops van onze opdrachtgever te optimaliseren. Binnen de agile...</p>

                        <span class="vacancy-icons">
                            <span>Tijdelijk</span>
                            <span class="icon icon-align-middle icon-clock"></span><span>40 uur/week</span>
                            <span class="icon icon-align-middle icon-contact-mapmarker"></span><span>Zwolle</span>
                            <span class="icon icon-align-middle --offset icon-calendar"></span><span>z.s.m.</span>
                        </span>
                    </div>
                </div>
            </a>
    </div>
</section>

    </div>

    <footer class="main-footer">
    <ul class="main-footer__nav">
        <li>&copy; 2021 Seven Stars</li>
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/proclaimer">Proclaimer</a></li>
        <li><a href="/werkenbij" target="_blank">Werken Bij</a></li>
        <li><a href="/faq">FAQ</a></li>
    </ul>
    <ul class="main-footer__social">
        <li><a href="https://www.facebook.com/SevenStarsNL/" target="_blank" class="icon icon-facebook"></a></li>
        <li><a href="https://twitter.com/SevenStars" target="_blank" class="icon icon-twitter"></a></li>
        <li><a href="https://www.linkedin.com/company/121272/" target="_blank" class="icon icon-linkedin"></a></li>
        <li><a href="https://www.instagram.com/sevenstarsnl/" target="_blank" class="icon icon-instagram-logo"></a></li>
        <li><a href="https://www.youtube.com/channel/UCOLwUXKHlPrAmn7unv6-UOg" target="_blank" class="icon icon-youtube"></a></li>
    </ul>
</footer>

</div>
"""

html_doc = string_value
soup = BeautifulSoup(html_doc, 'html.parser')


def sanitize_string(in_text):
    return str(in_text.replace('\n', '')).strip()


for divs in soup.find_all("div", class_='site-container__inner'):
    for li in divs.find_all("div", recursive=False):
        span = li.find("span")
        if span:
            pprint(sanitize_string(li.text))
