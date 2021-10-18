import re
from pprint import pprint

from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-64495-1', { 'anonymize_ip': true, 'forceSSL': true });
    </script>
    <title>
	Voedingswaarde van voedingsmiddelen met de beginletter A
</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="robots" content="index,follow" /><meta id="ctl00_mtaLang" http-equiv="Content-Language" content="NL" /><meta name="Author" content="Seoptics - R. van der Voort" /><meta name="copyright" content="Copyright Seoptics | R. van der Voort" /><meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" /><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" /><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" /><link rel="manifest" href="/manifest.json" /><link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" /><meta name="apple-mobile-web-app-title" content="Voedingswaarde" /><meta name="application-name" content="Voedingswaarde" /><meta name="msapplication-TileColor" content="#da532c" /><meta name="theme-color" content="#ffffff" /><link rel="shortcut icon" href="/_lib/img/favicon.ico" type="image/x-icon" /><link rel="Stylesheet" href="https://cdn.voedingswaardetabel.nl/css/cssmain.min.css" media="all" />
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-64495-1"></script>
        <script type="text/javascript" src="https://massariuscdn.com/pubs/voedingswaardetabel/voedingswaardetabel_hb_setup.js"></script>
        <script>
            var msTag = {
                site: 'voedingswaardetabel',
                page: 'ros'
            }
        </script>
    
    <link href="/Content/AjaxControlToolkit/Styles/Bundle?v=" rel="stylesheet"/>
<link href="../App_Themes/vwDefault/nutritions.css" type="text/css" rel="stylesheet" /><meta name="description" content="Overzicht van de voedingswaarde van producten die beginnen met de letter A" /><meta name="keywords" content="voedingswaarde,vitamines,mineralen,kcal,kjoule,eiwitten,koolhydraten,vet" /></head>
<body>
    <span id="ctl00_lblStat"></span>
    <form method="post" action="/voedingswaarde/" onsubmit="javascript:return WebForm_OnSubmit();" id="aspnetForm" class="mainform">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTE2NjgzNTgxOWQYAgUbY3RsMDAkY3BoTWFpbiRkdHBOdXRyaXRpb25zDxQrAARkZAKvAQI1ZAUaY3RsMDAkY3BoTWFpbiRsdHZOdXRyaXRpb24PFCsADmRkZGRkZGQ8KwA1AAI1ZGRkZgKvAWTXVkSq+YWYnfsGwGNFqMn4h3khxcddKv6jsMkD7GryKA==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="https://ajax.aspnetcdn.com/ajax/4.6/1/WebForms.js" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
window.WebForm_PostBackOptions||document.write('<script type="text/javascript" src="/WebResource.axd?d=cMAgWDaWeA7ymAcKBIetQyKIEm7yA-C_j6PiImvY3Av1KJVv9K_98ZmmC6_lBIA3Ojs2DQiHMTyBlBV9C_SHMdbe7srqdipGg2FqhpycC581&amp;t=637454104939909757"><\/script>');//]]>
</script>



<script src="https://ajax.aspnetcdn.com/ajax/4.6/1/WebUIValidation.js" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
var __cultureInfo = {"name":"nl-NL","numberFormat":{"CurrencyDecimalDigits":2,"CurrencyDecimalSeparator":",","IsReadOnly":true,"CurrencyGroupSizes":[3],"NumberGroupSizes":[3],"PercentGroupSizes":[3],"CurrencyGroupSeparator":".","CurrencySymbol":"€","NaNSymbol":"NaN","CurrencyNegativePattern":12,"NumberNegativePattern":1,"PercentPositivePattern":0,"PercentNegativePattern":0,"NegativeInfinitySymbol":"-Infinity","NegativeSign":"-","NumberDecimalDigits":2,"NumberDecimalSeparator":",","NumberGroupSeparator":".","CurrencyPositivePattern":2,"PositiveInfinitySymbol":"Infinity","PositiveSign":"+","PercentDecimalDigits":2,"PercentDecimalSeparator":",","PercentGroupSeparator":".","PercentSymbol":"%","PerMilleSymbol":"‰","NativeDigits":["0","1","2","3","4","5","6","7","8","9"],"DigitSubstitution":1},"dateTimeFormat":{"AMDesignator":"","Calendar":{"MinSupportedDateTime":"\/Date(-62135596800000)\/","MaxSupportedDateTime":"\/Date(253402297199999)\/","AlgorithmType":1,"CalendarType":1,"Eras":[1],"TwoDigitYearMax":2029,"IsReadOnly":true},"DateSeparator":"-","FirstDayOfWeek":1,"CalendarWeekRule":2,"FullDateTimePattern":"dddd d MMMM yyyy HH:mm:ss","LongDatePattern":"dddd d MMMM yyyy","LongTimePattern":"HH:mm:ss","MonthDayPattern":"d MMMM","PMDesignator":"","RFC1123Pattern":"ddd, dd MMM yyyy HH\u0027:\u0027mm\u0027:\u0027ss \u0027GMT\u0027","ShortDatePattern":"d-M-yyyy","ShortTimePattern":"HH:mm","SortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd\u0027T\u0027HH\u0027:\u0027mm\u0027:\u0027ss","TimeSeparator":":","UniversalSortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd HH\u0027:\u0027mm\u0027:\u0027ss\u0027Z\u0027","YearMonthPattern":"MMMM yyyy","AbbreviatedDayNames":["zo","ma","di","wo","do","vr","za"],"ShortestDayNames":["zo","ma","di","wo","do","vr","za"],"DayNames":["zondag","maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag"],"AbbreviatedMonthNames":["jan","feb","mrt","apr","mei","jun","jul","aug","sep","okt","nov","dec",""],"MonthNames":["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december",""],"IsReadOnly":true,"NativeCalendarName":"Gregoriaanse kalender","AbbreviatedMonthGenitiveNames":["jan","feb","mrt","apr","mei","jun","jul","aug","sep","okt","nov","dec",""],"MonthGenitiveNames":["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december",""]},"eras":[1,"n.Chr.",null,0]};//]]>
</script>

<script src="https://ajax.aspnetcdn.com/ajax/4.6/1/MicrosoftAjax.js" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
(window.Sys && Sys._Application && Sys.Observer)||document.write('<script type="text/javascript" src="/ScriptResource.axd?d=dkKK16T5kgcjD5IQ5OAqTyUjVMApRzAcC_GSzHJu_FzUH7O7K6WF62AVEpRop1box7tPkD1ljoQGAQI8moAYpfNWqHU1uWGd__AeJD6YqJEWWUqN4TKofFV-kNeIQ7erPJgDx3qg7HjTunyYoaFgpLZPKhp8fuGx-2Iey9dZ-QU1&t=2fe674eb"><\/script>');//]]>
</script>

<script src="https://ajax.aspnetcdn.com/ajax/4.6/1/MicrosoftAjaxWebForms.js" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
(window.Sys && Sys.WebForms)||document.write('<script type="text/javascript" src="/ScriptResource.axd?d=oZgt0ygTbEYG6F3aWq3xAk36WtnVFqFGcs8Apox0UOnpOQrJqNL4EWmbIUXFU-T6r1JNg3EIgd1zwt7So8iPHfmgJENABwHLMosnTz8xrXgatoB7-PP21p0bGh5lhqNatRC1SKkPNU2DjZci33yYppDOS33l3Wj5caCEHdH3zvy1EdsgwyeRi9fSsndNkB230&t=2fe674eb"><\/script>');function WebForm_OnSubmit() {
null;if (typeof(ValidatorOnSubmit) == "function" && ValidatorOnSubmit() == false) return false;
return true;
}
//]]>
</script>

<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="11D43DC7" />
	<input type="hidden" name="__SCROLLPOSITIONX" id="__SCROLLPOSITIONX" value="0" />
	<input type="hidden" name="__SCROLLPOSITIONY" id="__SCROLLPOSITIONY" value="0" />
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAK4BgJTFPZL/opuwNoj/vl3VjVoBFzFunCCR6qpXvgB4V5S0sNuJFoURkRGU+S0tvj4knn3BNoncP/lsVKFwet4Yai8+1D82cjhAv1IQu7vdpyXZlRip/5UnqkvsFtjZubu6lMRBx1LH+o1XPDkN8hr1jo3L5vCuNGqhpWUxuwl2PsTW5C60H5x2+iossRA5xmGvDQa2Nd8x7kb1sELqps0ByAf9QYv29btZAlGKp7Le4v0ZmHh/1AH1rhIwyh8RvWHgVhpOUNnAMpAkY22K3xFOkCYjFL3RqAWAXh+7lb7k8pJtPZ+4q7EX6l55fYmm4MiQ+VA9lgH5hXMtpGi8rZFkXYPXfU3ZV2lHipwo1bOVjhcUMQk+JebG25/KRByHZ3NOMrKktIeVYg0J12m0Vzb0SBp6BoSl0w2gkwUIZ4x/LnvpZ9vFPz4k45At/BjG1jFfVa7LQ2RZXajuYYXafwxl6wbKtMypwiuY7QZVYpo9d0jXACeWG/NFLuKM2fQENvgT+2HLjQdYw62RhamLGbhzGmeaGjRO8OjubzYOQeAzCFeF80vq45zHumK3rkDpzJhkj3p16lhiNp1N2gLEMSeLlcvrbyZSICXcLoypGhBfzrjdjy4nhZo796b/EZpkIBu6QF4pMSJtL6BdhyEyO1i5siEbj+2e/uF65+uZ5UDK/21Vl7Ld5gyNcKMcWao2bbplagEXXCc8I9sAuo86ZN3WCGykyqixaUIFcM1cOY9XGM00ARPNRE0sa6NEtZ0chQ+YxfRS6V/0P0BKk4cCnpOou/T2236x+T7BQTeMnYs09mXxnzm0/WtatjNFbrZDGfv0ScuP0lYdtDUjR4F8HPf+QITLtGoi0+bjtcZmwGub3kao2fftvKtgj17Mw6M5ACZOFHgBKDbajdSpeC+ymAcDLwjVpRzPt5hIcwM1df6BimRkJ1dn3xq2nz/8tETD886RzGZU9FfOUqQ0cqc6eayzAQfA2+7oGjQlKP3UVwjPWn2ITH9V1uU6MTA+xyoXFer++NKoUUkxz8ns/l59whOTxT/0D/PQfwYGG+Ozm8gGhLb2B+tN6vYjlMz9lWU1Lp+N1BUToqpFVfWE1jz5T9oBwgIr6lkRW5N6/fQsFiEERq+TSE9B9NvW+37AV9FP48agln2uHou4UFlJUTzvm93s8IO+eH4pTqeXr9U5ZLgvypLd93+zHEB6VfqleKJr5i1YX2ea+0Ao0VmOh733EenOyiWV8Y3aiA5sLDZPDYvCWljJMNik+YC7e3kXPcewF+KDB1Exmx55yIw02nwadVX3WLtYViNEi3yIVkVJdq9eUlIKnUwQQjsBrv7B0aja3G28HnufYcKYV714VztpkXwJiAUlvx+FpkOsCJ0JE029GbdBJ/uOZ2xeTXQXC6P1tY46QQPt/sUvnrHMggSDkHURmL79JmVLmzzIZYGGrrb7tc01i6BqAlbzNBgfw4jHUPkNUyqeosBPNB3w0EVpK/y6rtLnuhHIt1FYQm+KbuFenZmrNK6kaJ4ktcgMBMjePwBmwFVx1n3KTZdzk8TBv9s5mh38QD2xN2WlbFIF/L6ZNzOLfNPc5JfrM2JpvmOJBv2vW5pBPFVawcS9+cIMX0XvdDBKqV8iJSH+WL71j5/fMarAyFhm/qTBvb1TcPJPWZ15GYiAk2z6OXoDGtwcAFiwgLwHiFLgHuTuKY/ri0IBaTRmwQHq4m/Wg1dDdY5ftl1PeIZq9zk7LYrrLxOhfMTuhs1KL6MpWQTwdOWLN4btrp2r1rmQqGuSr7QskhRV2OtTPyXBrFIoWKQAiybdq4nxPponIt/swS3f6AzB9MRQTcDj7dallA1vzavOzYqdPeuHkI4tSEQkiOxNdsXEOQQx1FV6RkAfufrqJa6LpqnGFgtCpfaGWfSzqQvv15UNPCoc7H14TvBIQtLAzgliKSbX5DNSyegeKisaiL4WNUPJ0w+PFGdd5HcGATBLKDquDMiR05XC+DmObGx/ZlB0vVXTtdYCQH0GC9RNB1FM1S2PYkAo6Ir29bcvo5iygwr1T0/rBXJ9GckZtxKbEs+fg3x3YdD8BIQEfuW1cQJyeOvDpNcqtaDs+1IBYiw8kJ9chBkxybuDvhyYVFnlTesrdhRGgmH1Ozi5vb6mmmliTuPWDEnjIuhMpaGtOWXyuwaVL23xcQM67iW8q279VqCXKRI41aDRjEA+P04PCkJM/QmXi6dLV6AKvHnRDPgfem+LA+SXf5//7vG5m/U7A0QZeIAycnOA45g9Bzbw+y95Ly+Y2NGzp8x4PfBEl2KNZGKVWVBXFVHw1PRkmfnr8W9ADdtv82DjVWdbWtEN46F7AtIiMMw4++u6nJa/oEY5f/Uyg7s9+bKiVxPxI+Smlg9IY/2N1CWlpnzwteT70XmdLWVU0G2ePvI4AM5iSmiLxdQo/0JgOGPWpE1NwLA7wb0cmfGf20vUczLgLGMfMfn1lzSX+mBULL2IbJ3fRCFsoEfs6NfvJ/S624HabNFkk1xZ/NS/rYpZgl7+FYLInWUEXGzSsh+VrKcpxZhJ5VmMblLHah5M0TlCBQaF3C5EZbrkEx89WGlIPta3BTJ1Uv68L4BFSboOI8Nv5D/CSyeqvOlbu770eEgoA8+S/L4Kr6IJHC6DrUzFjCjD/UxDCN/iSOBesWSD4ySBNnWelvus776vVKFQxzIeH4x+a/oybAO4rwyBAT2sqXNIV2d1oMMIhOMuFyxoZ/OMdJR8XaDBKn0FNC8Awdd6+Xoie7NEfOeqEukNz6UgZj54WLBNIzAvirKpsyNUcDpCh9wxfX4r5i7M6BcIa+He1YDHMSV/HWYC/vZbJ8ivhPOaxxU1+KOBsrDBV1s3rFeRnwSytHHduXiyi+f2GirkgkYKJQiZyPjxp9k1L6UBOyeW+dBf5nZJAaLa2dMJ8kZx3G2JIGOUbwfAncd15+0Fy2gWGOLTDw1IDmgaEW+iTXlRfEkR30ZYR3ugLqNuDpoc8VFb0+YbjzwOIbwruBgH8aQWNG5N9/kXL4sLqHLznlOJP2I55r7oSpd6hJ1lGjPLKmejfGnpJOxk0fVbr6j4I32xUtIX5ceyNZCIsyMRpWSoC8tN/6Rr2FA4wM1/Ubt2IO383FyL5HeXy4/Lh0dg0J8kRSaLymRCAzP90//ZndTtT6Z+MkgUMcWcFyKIurx0ksdLvxAgAO5nRt55roXDWtR//nitLTJvUe9jcDkd09wGOZyXjTo8d2wSGsM94lWh2MarqO0VlatGiWCT5We2RHOikAwPwkU/mQe3pMTJKk+9erVNNd2d4RuJPNGdYTiQ3WYopQjMCz1NYreDSvqI38Tq6j6P3e9jo4FMub5WtMKJcEEGiXxIfV0ofG2cOKkE5LP9RK+Ms0EUyF1xwgMWk7XypkwbHahMvUPDkYvlyN8GZEjISsYEOkME2w05qiSfFjaWcKquSkiOLsUqmxEcnySN7KDbxjf+URRkRfzgxFUti1fV8lL/Cig09YUD4Z6YV4y3U6Hf6D8rx3AIoua3pFQiLtb1Ic0f3RS7CVU2D1fknsbHD1nAqIfQ+LVj5x3QfBIP4jTU/co3EV5yiflpSkCKouGAxjhNVgaec/tqnRCliNOEOxQuYiSZ9gqe6FNvaIqlC8/DE85F6f959DAcEJ9GKI9GOBFQ4h3l0BgA76KkTV9ZKqkPjJP7X0BCv+g8LDs8MyBj1SYkpc8L26j7PxnFtbzylsz3QOGCsqf6kxzblCKfRJezXxDNqPQ=" />
</div>
        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$scriptmanager1', 'aspnetForm', [], [], [], 90, 'ctl00');
//]]>
</script>

        <div id="outercontainer">
            <div id="container">
                <div id="header">
                    <div class="headerTop">
                        <div id="pnlHeaderTopSocial" class="headerTopSocial">
                            <a id="ctl00_hplMsrfb" title="Voedingswaardetabel op Facebook" href="https://www.facebook.com/voedingswaardetabel" target="_blank"><span class="socialiconfacebook socialiconfacebookTop"></span></a>
                            <a id="ctl00_hplMstrtt" title="Voedingswaardetabel op Twitter" href="https://twitter.com/onsvoedsel" target="_blank"><span class="socialicontwitter socialicontwitterTop"></span></a>
                        </div>
                        <div class="headerTopRight"></div>
                        <div class="headerTopOlive"></div>
                        <div class="headerTopColors"></div>
                        <div class="headerLogo">
                            <a id="ctl00_hplMsrlogo" title="Voedingswaardetabel" href="/"><img id="ctl00_imgMsrLogo" title="Voedingswaardetabel" src="/_lib/img/headerlogo.png" alt="Voedingswaardetabel" /></a>
                        </div>
                        <div id="RandomProd" class="randomprod">
                            <img src="https://cdn.voedingswaardetabel.nl/img/vwt-account.jpg" alt="Maak een VWT-Account aan" class="book" width="46" height="60" />Zien wat je echt eet?<br />Maak nu je persoonlijke VWT-Account aan.<br /><a href="/leden/registreren/" title="Maak gratis een VWT-Account aan">Registreren</a>
                        </div>
                    </div>
                    <div id="headerWhiteBar">
                        
                        <div class="breadcrumb">
                            <a id="ctl00_hplBCHome" title="Voedingswaardetabel" href="/">Home</a>
                             &gt; <a href="/voedingswaarde/" title="Voedingswaarde">Voedingswaarde</a> 
                        </div>
                    </div>
                    <div id="ctl00_pnlHeaderAmGray" class="amgrayT">
	
                        
                        <div id="ctl00_gAmGrayTop_pnlL7x9Top">
		

    <div id="pnlL7x9Topam" class="am-ht">
			
        <!-- 13436254/Voedingswaardetabel_HEADER -->
        <div id="div-gpt-ad-1546418606238-0" style="display:block";>
            <script>
                googletag.cmd.push(function() { googletag.display('div-gpt-ad-1546418606238-0'); });
            </script>
        </div>
    
		</div>

	</div>








                    
</div>
                    <div id="headerMenuContainer">
                        <div class="headerMenu">
                            <div id="Sidenav" class="sidenav">
                                <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                                <div class="sidenavinner">
                                    <ul><li class="topmenu"><a href="/voedingswaarde/" title="Voedingswaarde" onclick="submenuopen('39');return false;"><i id="mainmenu39" class="floatright arrow rotate45"></i>Voedingswaarde</a><ul id="submenu39" class="hidden submenus"><li><a href="/voedingswaarde/" title="Verwijderd alle ingestelde filters op de tabel">Voedingswaarde</a></li><li><a href="/voedingswaarde/vitamines/" title="Overzicht van vitamines">Vitamines</a></li><li><a href="/voedingswaarde/mineralen/" title="Overzicht van mineralen">Mineralen</a></li><li><a href="/voedingswaarde/top10/" title="Overzicht van top 10 voedingsmiddelen">Top 10</a></li><li><a href="/voedingswaarde/per-portie/" title="Voedingswaarde per portie">Per portie</a></li></ul><ul id="submenu39" class="hidden submenus"><li><a href="/voedingswaarde/" title="Verwijderd alle ingestelde filters op de tabel">Voedingswaarde</a></li><li><a href="/voedingswaarde/vitamines/" title="Overzicht van vitamines">Vitamines</a></li><li><a href="/voedingswaarde/mineralen/" title="Overzicht van mineralen">Mineralen</a></li><li><a href="/voedingswaarde/top10/" title="Overzicht van top 10 voedingsmiddelen">Top 10</a></li><li><a href="/voedingswaarde/per-portie/" title="Voedingswaarde per portie">Per portie</a></li></ul></li><li><a href="/watiswat/" title="Wat is wat?" onclick="submenuopen('2');return false;"><i id="mainmenu2" class="floatright arrow rotate45"></i>Wat is wat?</a><ul id="submenu2" class="hidden submenus"><li><a href="/watiswat/" title="Wat is wat pagina's">Overzicht pagina</a></li><li><a href="/watiswat/energie/" title="Energie">Energie</a></li><li><a href="/watiswat/water/" title="Water">Water</a></li><li><a href="/watiswat/eiwitten/" title="Eiwitten">Eiwitten</a></li><li><a href="/watiswat/vetten/" title="Vetten">Vetten</a></li><li><a href="/watiswat/cholesterol/" title="Cholesterol">Cholesterol</a></li><li><a href="/watiswat/koolhydraten/" title="Koolhydraten">Koolhydraten</a></li><li><a href="/watiswat/voedingsvezels/" title="Voedingsvezels">Voedingsvezels</a></li><li><a href="/watiswat/vitamines/" title="Vitamines">Vitamines</a></li><li><a href="/watiswat/mineralen/" title="Mineralen">Mineralen</a></li><li><a href="/watiswat/alcohol/" title="Alcohol">Alcohol</a></li><li><a href="/watiswat/onderzoekswaarde/" title="Goed gevoel of gezonde keuze?">Onderzoekwaarde</a></li><li><a href="/e-nummers/" title="Overzicht van de E-nummers">E-nummers</a></li></ul><ul id="submenu2" class="hidden submenus"><li><a href="/watiswat/" title="Wat is wat pagina's">Overzicht pagina</a></li><li><a href="/watiswat/energie/" title="Energie">Energie</a></li><li><a href="/watiswat/water/" title="Water">Water</a></li><li><a href="/watiswat/eiwitten/" title="Eiwitten">Eiwitten</a></li><li><a href="/watiswat/vetten/" title="Vetten">Vetten</a></li><li><a href="/watiswat/cholesterol/" title="Cholesterol">Cholesterol</a></li><li><a href="/watiswat/koolhydraten/" title="Koolhydraten">Koolhydraten</a></li><li><a href="/watiswat/voedingsvezels/" title="Voedingsvezels">Voedingsvezels</a></li><li><a href="/watiswat/vitamines/" title="Vitamines">Vitamines</a></li><li><a href="/watiswat/mineralen/" title="Mineralen">Mineralen</a></li><li><a href="/watiswat/alcohol/" title="Alcohol">Alcohol</a></li><li><a href="/watiswat/onderzoekswaarde/" title="Goed gevoel of gezonde keuze?">Onderzoekwaarde</a></li><li><a href="/e-nummers/" title="Overzicht van de E-nummers">E-nummers</a></li></ul></li><li><a href="/ons-voedsel/" title="Informatie over ons voedsel" onclick="submenuopen('71');return false;"><i id="mainmenu71" class="floatright arrow rotate45"></i>Ons voedsel</a><ul id="submenu71" class="hidden submenus"><li><a href="/ons-voedsel/" title="Ons voedsel">Overzicht ons voedsel</a></li><li><a href="/ons-voedsel/voedselveiligheid/" title="Voedselveiligheid">Voedselveiligheid</a></li><li><a href="/ons-voedsel/pro-en-prebiotica/" title="Pro- en prebiotica">Pro- en prebiotica</a></li><li><a href="/ons-voedsel/voedingssupplementen/" title="Voedingssupplementen">Voedingssupplementen</a></li><li><a href="/ons-voedsel/voedselallergie/" title="Voedselallergie">Voedselallergie</a></li><li><a href="/ons-voedsel/het-etiket/" title="Het etiket">Het etiket</a></li></ul><ul id="submenu71" class="hidden submenus"><li><a href="/ons-voedsel/" title="Ons voedsel">Overzicht ons voedsel</a></li><li><a href="/ons-voedsel/voedselveiligheid/" title="Voedselveiligheid">Voedselveiligheid</a></li><li><a href="/ons-voedsel/pro-en-prebiotica/" title="Pro- en prebiotica">Pro- en prebiotica</a></li><li><a href="/ons-voedsel/voedingssupplementen/" title="Voedingssupplementen">Voedingssupplementen</a></li><li><a href="/ons-voedsel/voedselallergie/" title="Voedselallergie">Voedselallergie</a></li><li><a href="/ons-voedsel/het-etiket/" title="Het etiket">Het etiket</a></li></ul></li><li><a href="/bereken/" title="Bereken" onclick="submenuopen('16');return false;"><i id="mainmenu16" class="floatright arrow rotate45"></i>Bereken</a><ul id="submenu16" class="hidden submenus"><li><a href="/bereken/" title="Calculator pagina">Overzicht calculators</a></li><li><a href="/bereken/bmi/" title="Body Mass Index">Body Mass Index</a></li><li><a href="/bereken/energieverbruik/" title="Energieverbruik">Energieverbruik</a></li><li><a href="/bereken/basaal-metabolisme-ratio/" title="Basaal metabolisme (BMR)">Ruststofwisseling</a></li><li><a href="/bereken/bloedalcoholgehalte/" title="Bloedalcoholgehalte">Bloedalcoholgehal</a></li><li><a href="/bereken/pral/" title="Bereken de pral waarde van een voedingsmiddel">PRAL-waarde</a></li></ul><ul id="submenu16" class="hidden submenus"><li><a href="/bereken/" title="Calculator pagina">Overzicht calculators</a></li><li><a href="/bereken/bmi/" title="Body Mass Index">Body Mass Index</a></li><li><a href="/bereken/energieverbruik/" title="Energieverbruik">Energieverbruik</a></li><li><a href="/bereken/basaal-metabolisme-ratio/" title="Basaal metabolisme (BMR)">Ruststofwisseling</a></li><li><a href="/bereken/bloedalcoholgehalte/" title="Bloedalcoholgehalte">Bloedalcoholgehal</a></li><li><a href="/bereken/pral/" title="Bereken de pral waarde van een voedingsmiddel">PRAL-waarde</a></li></ul></li><li><a href="/nieuws/" title="Nieuws">Nieuws</a></li><li><a href="/boeken/" title="Boeken van voedingswaardetabel">Boeken</a></li><li><a href="/leden/" title="Ga naar je persoonlijke voedingsdagboek" onclick="submenuopen('64');return false;"><i id="mainmenu64" class="floatright arrow rotate45"></i>Inloggen</a><ul id="submenu64" class="hidden submenus"><li><a href="/leden/login/" title="Leden gedeelte">Inloggen</a></li><li><a href="/leden/login/reset/" title="Reset je wachtwoord">Wachtwoord vergeten</a></li></ul><ul id="submenu64" class="hidden submenus"><li><a href="/leden/login/" title="Leden gedeelte">Inloggen</a></li><li><a href="/leden/login/reset/" title="Reset je wachtwoord">Wachtwoord vergeten</a></li></ul></li><li><a href="/leden/registreren/" title="Maak een vwt-account aan">Registreren</a></li><li><a href="/contact/" title="Contact">Contact</a></li><li><a href="/" title="Voedingswaardetabel" onclick="submenuopen('1');return false;"><i id="mainmenu1" class="floatright arrow rotate45"></i>Informatie</a><ul id="submenu1" class="hidden submenus"><li><a href="/faq/" title="Faq">Veel gestelde vragen</a></li><li><a href="/uitleg-voedingswaardetabel/" title="Hoe de tabel te gebruiken">Uitleg tabel</a></li><li><a href="/over/" title="Over / Wie is?">Over / Wie is?</a></li><li><a href="/links/" title="Links">Links</a></li></ul><ul id="submenu1" class="hidden submenus"><li><a href="/faq/" title="Faq">Veel gestelde vragen</a></li><li><a href="/uitleg-voedingswaardetabel/" title="Hoe de tabel te gebruiken">Uitleg tabel</a></li><li><a href="/over/" title="Over / Wie is?">Over / Wie is?</a></li><li><a href="/links/" title="Links">Links</a></li></ul></li><li><a href="/disclaimer/" title="Disclaimer & Privacy" onclick="submenuopen('51');return false;"><i id="mainmenu51" class="floatright arrow rotate45"></i>Disclaimer</a><ul id="submenu51" class="hidden submenus"><li><a href="/disclaimer/" title="Disclaimer en algemene voorwaarden">Algemene voorwaarden</a></li><li><a href="/disclaimer/privacy/" title="Privacybeleid">Privacyverklaring</a></li><li><a href="/disclaimer/cookies/" title="Cookiebeleid">Cookiebeleid</a></li></ul><ul id="submenu51" class="hidden submenus"><li><a href="/disclaimer/" title="Disclaimer en algemene voorwaarden">Algemene voorwaarden</a></li><li><a href="/disclaimer/privacy/" title="Privacybeleid">Privacyverklaring</a></li><li><a href="/disclaimer/cookies/" title="Cookiebeleid">Cookiebeleid</a></li></ul></li></ul>
                                </div>
                            </div>
                            <div class="innerheadermenu">
                                <div class="hammenu hand" onclick="openNav()"><div></div><div></div><div></div></div>
                                <div id="searchmenu" class="searchmenu hand">
                                    <picture>
                                        <source media="(max-width:1024px)" srcset="https://cdn.voedingswaardetabel.nl/img/gmagnifyg.png">
                                        <img src="https://cdn.voedingswaardetabel.nl/img/gmagnify.png" alt="Zoek producten in de voedingswaardetabel" title="Zoek producten in de voedingswaardetabel" />
                                    </picture>
                                </div>
                                <ul>
                                    
                                        <li class="sss600"><a href="/watiswat/" title="Wat is wat?">Wat is wat</a></li>
                                        <li class="sss600"><a href="/ons-voedsel/" title="Ons voedsel">Ons voedsel</a></li>
                                        
                                            <li><a href="/leden/login/" title="Leden inloggen">Inloggen</a></li>
                                            <li><a href="/leden/registreren/" title="Registreren op Voedingswaardetabel">Registreren</a></li>
                                        
                                        <li><a href="/nieuws/" title="(W)etenswaardigheden en nieuws">Nieuws</a></li>
                                    
                                    
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div id="headertitle">
                        <h1>Voedingswaarde van voedingsmiddelen</h1>
                        <div class="sets">
                            <div id="ctl00_set01" class="set set01">
	
                                <a id="ctl00_hplBeginwaarde" title="Beginwaarde voedingswaardetabel / verwijderd alle filters" href="/voedingswaarde/"><span id="ctl00_lblset01">Beginwaarde</span></a>
                            
</div>
                            <div id="ctl00_set02" class="set set02">
	
                                <a id="ctl00_hplVoedingswaarde" title="Voedingswaarde" href="/voedingswaarde/"><span id="ctl00_lblset02">Voedingswaarde</span></a>
                            
</div>
                            <div id="ctl00_set03" class="set set03">
	
                                <a id="ctl00_hplVitamines" title="Vitamines" href="/voedingswaarde/vitamines/"><span id="ctl00_lblset03">Vitamines</span></a>
                            
</div>
                            <div id="ctl00_set04" class="set set04">
	
                                <a id="ctl00_hplMineralen" title="Mineralen" href="/voedingswaarde/mineralen/"><span id="ctl00_lblset04">Mineralen</span></a>
                            
</div>
                        </div>
                        <div class="smallText letterinfo">
                            <span id="ctl00_lblVW100" class="tblue"><a id="ctl00_hplVW100" title="Voedingswaarde per 100 gram" class="hplVW100" href="/voedingswaarde/">per 100 gram</a></span> | <span id="ctl00_lblVWpp" class="tgray"><a id="ctl00_hplVWpp" title="Voedingswaarde per portie" class="hplVWpp" href="/voedingswaarde/per-portie/">per portie</a></span>
                        </div>
                        <div class="lettersborder"></div>
                        <div class="mobspano"><div id="ctl00_pnlHeaderLetters" class="headerLetters">
	<a id="ctl00_hplLettersA" title="Voedingswaarde van voedingsmiddelen met de beginletter A" href="/voedingswaarde/">A</a><a id="ctl00_hplLettersB" title="Voedingswaarde van voedingsmiddelen met de beginletter B" href="/voedingswaarde/B/">B</a><a id="ctl00_hplLettersC" title="Voedingswaarde van voedingsmiddelen met de beginletter C" href="/voedingswaarde/C/">C</a><a id="ctl00_hplLettersD" title="Voedingswaarde van voedingsmiddelen met de beginletter D" href="/voedingswaarde/D/">D</a><a id="ctl00_hplLettersE" title="Voedingswaarde van voedingsmiddelen met de beginletter E" href="/voedingswaarde/E/">E</a><a id="ctl00_hplLettersF" title="Voedingswaarde van voedingsmiddelen met de beginletter F" href="/voedingswaarde/F/">F</a><a id="ctl00_hplLettersG" title="Voedingswaarde van voedingsmiddelen met de beginletter G" href="/voedingswaarde/G/">G</a><a id="ctl00_hplLettersH" title="Voedingswaarde van voedingsmiddelen met de beginletter H" href="/voedingswaarde/H/">H</a><a id="ctl00_hplLettersI" title="Voedingswaarde van voedingsmiddelen met de beginletter I" href="/voedingswaarde/I/">I</a><a id="ctl00_hplLettersJ" title="Voedingswaarde van voedingsmiddelen met de beginletter J" href="/voedingswaarde/J/">J</a><a id="ctl00_hplLettersK" title="Voedingswaarde van voedingsmiddelen met de beginletter K" href="/voedingswaarde/K/">K</a><a id="ctl00_hplLettersL" title="Voedingswaarde van voedingsmiddelen met de beginletter L" href="/voedingswaarde/L/">L</a><a id="ctl00_hplLettersM" title="Voedingswaarde van voedingsmiddelen met de beginletter M" href="/voedingswaarde/M/">M</a><a id="ctl00_hplLettersN" title="Voedingswaarde van voedingsmiddelen met de beginletter N" href="/voedingswaarde/N/">N</a><a id="ctl00_hplLettersO" title="Voedingswaarde van voedingsmiddelen met de beginletter O" href="/voedingswaarde/O/">O</a><a id="ctl00_hplLettersP" title="Voedingswaarde van voedingsmiddelen met de beginletter P" href="/voedingswaarde/P/">P</a><a id="ctl00_hplLettersQ" title="Voedingswaarde van voedingsmiddelen met de beginletter Q" href="/voedingswaarde/Q/">Q</a><a id="ctl00_hplLettersR" title="Voedingswaarde van voedingsmiddelen met de beginletter R" href="/voedingswaarde/R/">R</a><a id="ctl00_hplLettersS" title="Voedingswaarde van voedingsmiddelen met de beginletter S" href="/voedingswaarde/S/">S</a><a id="ctl00_hplLettersT" title="Voedingswaarde van voedingsmiddelen met de beginletter T" href="/voedingswaarde/T/">T</a><a id="ctl00_hplLettersU" title="Voedingswaarde van voedingsmiddelen met de beginletter U" href="/voedingswaarde/U/">U</a><a id="ctl00_hplLettersV" title="Voedingswaarde van voedingsmiddelen met de beginletter V" href="/voedingswaarde/V/">V</a><a id="ctl00_hplLettersW" title="Voedingswaarde van voedingsmiddelen met de beginletter W" href="/voedingswaarde/W/">W</a><a id="ctl00_hplLettersX" title="Voedingswaarde van voedingsmiddelen met de beginletter X" href="/voedingswaarde/X/">X</a><a id="ctl00_hplLettersY" title="Voedingswaarde van voedingsmiddelen met de beginletter Y" href="/voedingswaarde/Y/">Y</a><a id="ctl00_hplLettersZ" title="Voedingswaarde van voedingsmiddelen met de beginletter Z" href="/voedingswaarde/Z/">Z</a>
</div></div>
                        <div class="lettersborder"></div>
                    </div>
                </div>
                <div id="headerprint">
                    <img src="https://cdn.voedingswaardetabel.nl/img/header.jpg" alt="" />
                    <span id="ctl00_lblHeaderPrintName" class="headerprintname"></span>
                </div>
                <div id="body">
	
                    
    <div class="mobspano">
        <div id="ctl00_cphMain_pnlVwtContainer" class="vwtContainer widthContainer">
		
            
            
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlSortingExtra" class="ColumnHeaders">
			<div id="ctl00_cphMain_ltvNutrition_ctrl0_extraRowW0" class="vwRowExtra">
				<div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlUnitWordEmpty0" class="rowHeaderWordEmpty">

				</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_rowHeaderWords0">
					<div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW0" class="rowHeaderWord">
						<div title="Kcal" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW1" class="rowHeaderWord">
						<div title="Kjoule" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW2" class="rowHeaderWord">
						<div title="Water" class="rowHeaderWordInnerDiv">
							<span class="cBlue">water</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW3" class="rowHeaderWord">
						<div title="Eiwit" class="rowHeaderWordInnerDiv">
							<span class="cBlue">eiwit</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW4" class="rowHeaderWord">
						<div title="Koolhydraten" class="rowHeaderWordInnerDiv">
							<span class="cBlue">koolhydraten</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW5" class="rowHeaderWord">
						<div title="Suikers" class="rowHeaderWordInnerDiv">
							<span class="cBlue">suikers</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW6" class="rowHeaderWord">
						<div title="Vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW7" class="rowHeaderWord">
						<div title="Verzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">verzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW8" class="rowHeaderWord">
						<div title="Enkelvoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">enkelvoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW9" class="rowHeaderWord">
						<div title="Meervoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">meervoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW10" class="rowHeaderWord">
						<div title="Cholesterol" class="rowHeaderWordInnerDiv">
							<span class="cBlue">cholesterol</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW11" class="rowHeaderWord">
						<div title="Voedingsvezel" class="rowHeaderWordInnerDiv">
							<span class="cBlue">voedingsvezels</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW13" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gevoelswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gevoelswaarde</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unitwordW14" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gezondheidswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gezondheidswaarde</span>
						</div>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlUnit0" class="rowUnit">
				<div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlUnitPer0" class="rowUnitProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblValue0">Eenheid per 100 gram</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlUnits0">
					<div id="ctl00_cphMain_ltvNutrition_ctrl0_unit0" class="rowUnitItems">
						<span title="kilocalorieën">kcal</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit1" class="rowUnitItems">
						<span title="kilojoules">kJ</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit2" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit3" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit4" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit5" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit6" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit7" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit8" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit9" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit10" class="rowUnitItems">
						<span title="milligram">mg</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit11" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit13" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_unit14" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlSort0" class="rowSort">
				<div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlProdSort0" class="rowSortProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblprodsort0">Sorteren</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlSorting0">
					<div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort0" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown0" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown0" title="Kcal aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp0" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp0" title="Kcal oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort1" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown1" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown1" title="Kjoule aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp1" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp1" title="Kjoule oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort2" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown2" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown2" title="Water aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp2" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp2" title="Water oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort3" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown3" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown3" title="Eiwit aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp3" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp3" title="Eiwit oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort4" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown4" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown4" title="Koolhydraten aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp4" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp4" title="Koolhydraten oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort5" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown5" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown5" title="Suikers aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp5" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp5" title="Suikers oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort6" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown6" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown6" title="Vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp6" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp6" title="Vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort7" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown7" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown7" title="Verzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp7" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp7" title="Verzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort8" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown8" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown8" title="Enkelvoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp8" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp8" title="Enkelvoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort9" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown9" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown9" title="Meervoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp9" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp9" title="Meervoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort10" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown10" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown10" title="Cholesterol aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp10" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp10" title="Cholesterol oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort11" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown11" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown11" title="Voedingsvezel aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp11" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp11" title="Voedingsvezel oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlItemSpacerS13" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort13" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown13" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown13" title="Gevoelswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp13" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp13" title="Gevoelswaarde oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlItemSpacerS14" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl0_Sort14" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortDown14" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortDown14" title="Gezondheidswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl0$SortUp14" value="" id="ctl00_cphMain_ltvNutrition_ctrl0_SortUp14" title="Gezondheidswaarde oplopend sorteren" class="ontop btndown hand" />
					</div>
				</div>
			</div>
		</div>
                    <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl0_hplProdname0" title="Voedingswaarde van aal" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=26">Aal</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl0_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblKcal">213</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblKjoule">893</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblWater">66,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblEiwit">16,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblKoolh">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblVet">16,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblVerz">4,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblEov">11,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblMov">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblChol">220,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlFeeling" title="5,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblFeeling">5,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl0_pnlHealty" title="6,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl0_lblHealty">6,7</span><img id="ctl00_cphMain_ltvNutrition_ctrl0_prodImg14" title="Aal" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/aal.jpg" alt="Aal" /><img id="ctl00_cphMain_ltvNutrition_ctrl0_prodImgHolder14" title="Aal" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Aal" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl1_hplProdname1" title="Voedingswaarde van aalbes, rode bes" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=604">Aalbes, rode bes</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl1_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblKcal">51</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblKjoule">213</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblWater">82,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblEiwit">1,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblKoolh">7,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblSuikers">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblVoedv">7,9</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlFeeling" title="6,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblFeeling">6,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl1_pnlHealty" title="6,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl1_lblHealty">6,1</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl2_hplProdname2" title="Voedingswaarde van aardappel, zoet, bataat" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1071">Aardappel, zoet, bataat</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl2_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblKcal">96</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblKjoule">402</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblWater">74,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblEiwit">1,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblKoolh">21,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblSuikers">3,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblVoedv">2,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlFeeling" title="6,1 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblFeeling">6,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl2_pnlHealty" title="7,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl2_lblHealty">7,1</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl3_hplProdname3" title="Voedingswaarde van aardappel, zoet, bataat, gekookt" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1323">Aardappel, zoet, bataat, gekookt</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl3_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblKcal">85</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblKjoule">356</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblWater">76,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblEiwit">1,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblKoolh">19,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblSuikers">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblVet">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblVerz">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblVoedv">2,4</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl3_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl3_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl4_hplProdname4" title="Voedingswaarde van aardappelen, gebakken" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=606">Aardappelen, gebakken</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl4_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblKcal">126</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblKjoule">529</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblWater">73,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblEiwit">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblKoolh">16,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblSuikers">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblVet">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblVerz">2,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblEov">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblMov">1,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblVoedv">2,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlFeeling" title="7,9 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblFeeling">7,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl4_pnlHealty" title="5,8 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl4_lblHealty">5,8</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl5_hplProdname5" title="Voedingswaarde van aardappelen, gekookt" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=605">Aardappelen, gekookt</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl5_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblKcal">82</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblKjoule">346</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblWater">77,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblEiwit">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblKoolh">17,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblVoedv">2,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlFeeling" title="7,6 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblFeeling">7,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl5_pnlHealty" title="7,9 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl5_lblHealty">7,9</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl6_hplProdname6" title="Voedingswaarde van aardappelen, rauw" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1153">Aardappelen, rauw</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl6_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblKcal">85</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblKjoule">357</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblWater">76,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblEiwit">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblKoolh">17,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblVoedv">2,6</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlFeeling" title="6,5 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblFeeling">6,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl6_pnlHealty" title="7,5 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl6_lblHealty">7,5</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl7_hplProdname7" title="Voedingswaarde van aardappelkroketjes" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=524">Aardappelkroketjes</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl7_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblKcal">223</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblKjoule">936</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblWater">55,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblEiwit">3,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblKoolh">27,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblSuikers">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblVet">11,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblVerz">3,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblEov">6,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblMov">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblChol">1,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblVoedv">2,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlFeeling" title="6,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblFeeling">6,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl7_pnlHealty" title="5,5 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl7_lblHealty">5,5</span><img id="ctl00_cphMain_ltvNutrition_ctrl7_prodImg14" title="Aardappelkroketjes" class="prodImgB2" src="https://cdn.voedingswaardetabel.nl/img/prod/aardappelkroket.jpg" alt="Aardappelkroketjes" /><img id="ctl00_cphMain_ltvNutrition_ctrl7_prodImgHolder14" title="Aardappelkroketjes" class="prodImgHolderB2" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig2.png" alt="Aardappelkroketjes" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl8_hplProdname8" title="Voedingswaarde van aardappelpuree (instant, bereid)" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=513">Aardappelpuree (instant, bereid)</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl8_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblKcal">99</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblKjoule">418</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblWater">79,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblEiwit">3,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblKoolh">12,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblVet">4,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblVerz">1,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblEov">0,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblMov">1,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblChol">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlFeeling" title="6,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblFeeling">6,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl8_pnlHealty" title="5,5 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl8_lblHealty">5,5</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl9_hplProdname9" title="Voedingswaarde van aardappelschijfjes, gemiddeld" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=528">Aardappelschijfjes, gemiddeld</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl9_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblKcal">141</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblKjoule">591</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblWater">68,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblEiwit">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblKoolh">20,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblSuikers">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblVet">5,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblVerz">2,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblEov">1,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblMov">0,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblChol">0,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblVoedv">3,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlFeeling" title="7,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblFeeling">7,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl9_pnlHealty" title="6,4 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl9_lblHealty">6,4</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl10_hplProdname10" title="Voedingswaarde van aardappelzetmeel" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1001">Aardappelzetmeel</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl10_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblKcal">329</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblKjoule">1378</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblWater">17,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblEiwit">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblKoolh">81,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblSuikers">5,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl10_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl10_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl11_hplProdname11" title="Voedingswaarde van aardbei, vers" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=27">Aardbei, vers</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl11_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblKcal">36</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblKjoule">154</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblWater">89,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblEiwit">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblKoolh">6,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblSuikers">5,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblVet">0,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblVoedv">2,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlFeeling" title="9,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblFeeling">9,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl11_pnlHealty" title="9,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl11_lblHealty">9,1</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl12_hplProdname12" title="Voedingswaarde van aardpeer (topinamboer)" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1000">Aardpeer (topinamboer)</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl12_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblKcal">81</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblKjoule">343</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblWater">78,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblEiwit">2,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblKoolh">17,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblVoedv">18,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlFeeling" title="5,4 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblFeeling">5,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl12_pnlHealty" title="6,8 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl12_lblHealty">6,8</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl13_hplProdname13" title="Voedingswaarde van abrikoos, blik" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=42">Abrikoos, blik</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl13_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblKcal">74</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblKjoule">310</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblWater">80,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblEiwit">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblKoolh">17,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblSuikers">16,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblVoedv">1,1</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlFeeling" title="5,9 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblFeeling">5,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl13_pnlHealty" title="5,9 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl13_lblHealty">5,9</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl14_hplProdname14" title="Voedingswaarde van abrikoos,vers" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=607">Abrikoos,vers</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl14_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblKcal">60</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblKjoule">252</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblWater">83,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblEiwit">1,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblKoolh">11,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblSuikers">7,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblVet">0,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblVoedv">2,3</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlFeeling" title="7,4 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblFeeling">7,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl14_pnlHealty" title="8,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl14_lblHealty">8,7</span><img id="ctl00_cphMain_ltvNutrition_ctrl14_prodImg14" title="Abrikoos,vers" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/abrikoos.jpg" alt="Abrikoos,vers" /><img id="ctl00_cphMain_ltvNutrition_ctrl14_prodImgHolder14" title="Abrikoos,vers" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Abrikoos,vers" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl15_hplProdname15" title="Voedingswaarde van abrikozen, gedroogd" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=608">Abrikozen, gedroogd</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl15_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblKcal">274</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblKjoule">1151</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblWater">26,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblEiwit">5,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblKoolh">58,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblSuikers">55,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblVoedv">8,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlFeeling" title="6,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblFeeling">6,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl15_pnlHealty" title="7,8 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl15_lblHealty">7,8</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl16_hplProdname16" title="Voedingswaarde van achterham" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=133">Achterham</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl16_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblKcal">129</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblKjoule">542</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblWater">72,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblEiwit">18,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblKoolh">1,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblVet">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblVerz">2,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblEov">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblMov">2,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblChol">38,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlFeeling" title="7,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblFeeling">7,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl16_pnlHealty" title="6,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl16_lblHealty">6,1</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl17_hplProdname17" title="Voedingswaarde van achterham, gegrild" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=134">Achterham, gegrild</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl17_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblKcal">116</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblKjoule">488</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblWater">75,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblEiwit">19,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblKoolh">0,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblVet">4,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblVerz">1,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblEov">1,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblMov">0,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblChol">38,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlFeeling" title="7,6 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblFeeling">7,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl17_pnlHealty" title="7,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl17_lblHealty">7,0</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl18_hplProdname18" title="Voedingswaarde van adukibonen, gekookt" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=610">Adukibonen, gekookt</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl18_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblKcal">131</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblKjoule">548</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblWater">65,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblEiwit">7,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblKoolh">24,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblSuikers"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblVoedv"></span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlFeeling" title="5,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblFeeling">5,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl18_pnlHealty" title="6,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl18_lblHealty">6,0</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl19_hplProdname19" title="Voedingswaarde van advocaat, 14 % v/v" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=609">Advocaat, 14 % v/v</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl19_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblKcal">240</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblKjoule">1006</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblWater">54,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblEiwit">3,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblKoolh">24,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblSuikers">24,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblVet">3,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblVerz">1,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblEov">2,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblChol">150,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlFeeling" title="5,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblFeeling">5,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl19_pnlHealty" title="4,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl19_lblHealty">4,0</span>
			</div>
                    
		</div>
                
                    <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlSortingExtra" class="ColumnHeaders">
			<div id="ctl00_cphMain_ltvNutrition_ctrl20_extraRowW20" class="vwRowExtra">
				<div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlUnitWordEmpty20" class="rowHeaderWordEmpty">

				</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_rowHeaderWords20">
					<div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW0" class="rowHeaderWord">
						<div title="Kcal" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW1" class="rowHeaderWord">
						<div title="Kjoule" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW2" class="rowHeaderWord">
						<div title="Water" class="rowHeaderWordInnerDiv">
							<span class="cBlue">water</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW3" class="rowHeaderWord">
						<div title="Eiwit" class="rowHeaderWordInnerDiv">
							<span class="cBlue">eiwit</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW4" class="rowHeaderWord">
						<div title="Koolhydraten" class="rowHeaderWordInnerDiv">
							<span class="cBlue">koolhydraten</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW5" class="rowHeaderWord">
						<div title="Suikers" class="rowHeaderWordInnerDiv">
							<span class="cBlue">suikers</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW6" class="rowHeaderWord">
						<div title="Vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW7" class="rowHeaderWord">
						<div title="Verzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">verzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW8" class="rowHeaderWord">
						<div title="Enkelvoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">enkelvoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW9" class="rowHeaderWord">
						<div title="Meervoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">meervoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW10" class="rowHeaderWord">
						<div title="Cholesterol" class="rowHeaderWordInnerDiv">
							<span class="cBlue">cholesterol</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW11" class="rowHeaderWord">
						<div title="Voedingsvezel" class="rowHeaderWordInnerDiv">
							<span class="cBlue">voedingsvezels</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW13" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gevoelswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gevoelswaarde</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unitwordW14" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gezondheidswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gezondheidswaarde</span>
						</div>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlUnit20" class="rowUnit">
				<div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlUnitPer20" class="rowUnitProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblValue20">Eenheid per 100 gram</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlUnits20">
					<div id="ctl00_cphMain_ltvNutrition_ctrl20_unit0" class="rowUnitItems">
						<span title="kilocalorieën">kcal</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit1" class="rowUnitItems">
						<span title="kilojoules">kJ</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit2" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit3" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit4" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit5" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit6" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit7" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit8" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit9" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit10" class="rowUnitItems">
						<span title="milligram">mg</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit11" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit13" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_unit14" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlSort20" class="rowSort">
				<div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlProdSort20" class="rowSortProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblprodsort20">Sorteren</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlSorting20">
					<div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort0" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown0" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown0" title="Kcal aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp0" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp0" title="Kcal oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort1" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown1" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown1" title="Kjoule aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp1" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp1" title="Kjoule oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort2" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown2" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown2" title="Water aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp2" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp2" title="Water oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort3" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown3" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown3" title="Eiwit aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp3" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp3" title="Eiwit oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort4" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown4" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown4" title="Koolhydraten aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp4" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp4" title="Koolhydraten oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort5" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown5" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown5" title="Suikers aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp5" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp5" title="Suikers oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort6" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown6" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown6" title="Vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp6" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp6" title="Vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort7" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown7" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown7" title="Verzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp7" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp7" title="Verzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort8" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown8" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown8" title="Enkelvoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp8" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp8" title="Enkelvoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort9" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown9" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown9" title="Meervoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp9" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp9" title="Meervoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort10" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown10" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown10" title="Cholesterol aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp10" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp10" title="Cholesterol oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort11" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown11" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown11" title="Voedingsvezel aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp11" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp11" title="Voedingsvezel oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlItemSpacerS13" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort13" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown13" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown13" title="Gevoelswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp13" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp13" title="Gevoelswaarde oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlItemSpacerS14" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl20_Sort14" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortDown14" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortDown14" title="Gezondheidswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl20$SortUp14" value="" id="ctl00_cphMain_ltvNutrition_ctrl20_SortUp14" title="Gezondheidswaarde oplopend sorteren" class="ontop btndown hand" />
					</div>
				</div>
			</div>
		</div>
                    <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl20_hplProdname20" title="Voedingswaarde van agar-agar, droog poeder" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=29">Agar-agar, droog poeder</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl20_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblKcal">365</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblKjoule">1529</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblWater">4,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblEiwit">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblKoolh">80,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblVoedv">8,4</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl20_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl20_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl21_hplProdname21" title="Voedingswaarde van agar-agar, vers (zeewier)" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1363">Agar-agar, vers (zeewier)</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl21_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblKcal">37</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblKjoule">155</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblWater">91,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblEiwit">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblKoolh">6,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblSuikers">0,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblVoedv">0,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl21_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl21_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl22_hplProdname22" title="Voedingswaarde van ahornsiroop" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=999">Ahornsiroop</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl22_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblKcal">365</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblKjoule">1530</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblWater">9,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblEiwit">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblKoolh">90,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblSuikers">89,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlFeeling" title="5,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblFeeling">5,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl22_pnlHealty" title="6,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl22_lblHealty">6,1</span><img id="ctl00_cphMain_ltvNutrition_ctrl22_prodImg14" title="Ahornsiroop" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/ahornsiroop.jpg" alt="Ahornsiroop" /><img id="ctl00_cphMain_ltvNutrition_ctrl22_prodImgHolder14" title="Ahornsiroop" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Ahornsiroop" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl23_hplProdname23" title="Voedingswaarde van alaska pollak" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=173">Alaska pollak</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl23_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblKcal">75</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblKjoule">314</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblWater">81,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblEiwit">16,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblKoolh">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblVet">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblMov">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblChol">80,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlFeeling" title="5,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblFeeling">5,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl23_pnlHealty" title="6,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl23_lblHealty">6,2</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl24_hplProdname24" title="Voedingswaarde van alfalfa" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=611">Alfalfa</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl24_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblKcal">43</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblKjoule">181</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblWater">87,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblEiwit">4,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblKoolh">3,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblSuikers"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblVet">0,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblVerz"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblEov"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblMov"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblVoedv">2,4</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlFeeling" title="6,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblFeeling">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl24_pnlHealty" title="7,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl24_lblHealty">7,2</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl25_hplProdname25" title="Voedingswaarde van amandelbroodje" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1273">Amandelbroodje</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl25_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblKcal">490</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblKjoule">2054</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblWater">9,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblEiwit">7,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblKoolh">50,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblSuikers">28,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblVet">28,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblVerz">11,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblEov">8,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblMov">3,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblChol">30,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblVoedv">3,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlFeeling" title="6,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblFeeling">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl25_pnlHealty" title="3,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl25_lblHealty">3,7</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl26_hplProdname26" title="Voedingswaarde van amandelen" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=612">Amandelen</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl26_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblKcal">609</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblKjoule">2548</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblWater">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblEiwit">19,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblKoolh">10,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblSuikers">3,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblVet">52,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblVerz">3,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblEov">34,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblMov">12,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblVoedv">10,6</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlFeeling" title="7,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblFeeling">7,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl26_pnlHealty" title="7,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl26_lblHealty">7,7</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl27_hplProdname27" title="Voedingswaarde van amandelmeel" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1346">Amandelmeel</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl27_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblKcal">632</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblKjoule">2644</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblWater">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblEiwit">21,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblKoolh">15,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblSuikers">4,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblVet">51,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblVerz">4,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblEov"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblMov"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblVoedv">10,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl27_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl27_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl28_hplProdname28" title="Voedingswaarde van amandelmelk " class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1347">Amandelmelk </a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl28_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblKcal">53</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblKjoule">222</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblWater">88,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblEiwit">3,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblKoolh">3,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblSuikers">2,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblVet">2,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblVerz">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblEov">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblMov">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblVoedv">0,8</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlFeeling" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblFeeling"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl28_pnlHealty" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl28_lblHealty"></span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl29_hplProdname29" title="Voedingswaarde van amandelolie" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=924">Amandelolie</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl29_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblKcal">882</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblKjoule">3693</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblWater">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblEiwit">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblKoolh">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblVet">99,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblVerz">8,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblEov">61,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblMov">26,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlFeeling" title="5,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblFeeling">5,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl29_pnlHealty" title="7,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl29_lblHealty">7,1</span><img id="ctl00_cphMain_ltvNutrition_ctrl29_prodImg14" title="Amandelolie" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/amandelolie.jpg" alt="Amandelolie" /><img id="ctl00_cphMain_ltvNutrition_ctrl29_prodImgHolder14" title="Amandelolie" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Amandelolie" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl30_hplProdname30" title="Voedingswaarde van amandelspijs" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=30">Amandelspijs</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl30_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblKcal">458</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblKjoule">1916</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblWater">13,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblEiwit">10,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblKoolh">47,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblSuikers">43,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblVet">24,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblVerz">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblEov">14,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblMov">4,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblChol">35,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblVoedv">3,9</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlFeeling" title="6,3 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblFeeling">6,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl30_pnlHealty" title="3,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl30_lblHealty">3,7</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl31_hplProdname31" title="Voedingswaarde van amsoi" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=31">Amsoi</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl31_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblKcal">31</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblKjoule">132</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblWater">90,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblEiwit">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblKoolh">5,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblVoedv">1,1</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlFeeling" title="4,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblFeeling">4,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl31_pnlHealty" title="5,9 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl31_lblHealty">5,9</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl32_hplProdname32" title="Voedingswaarde van ananas, vers" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=32">Ananas, vers</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl32_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblKcal">61</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblKjoule">256</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblWater">83,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblEiwit">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblKoolh">13,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblSuikers">12,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblVet">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblVoedv">1,4</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlFeeling" title="8,4 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblFeeling">8,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl32_pnlHealty" title="8,8 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl32_lblHealty">8,8</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl33_hplProdname33" title="Voedingswaarde van ananassap" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1023">Ananassap</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl33_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblKcal">50</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblKjoule">211</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblWater">86,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblEiwit">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblKoolh">11,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblSuikers">11,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblVoedv">0,3</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlFeeling" title="7,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblFeeling">7,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl33_pnlHealty" title="7,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl33_lblHealty">7,2</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl34_hplProdname34" title="Voedingswaarde van andijvie, rauw" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=33">Andijvie, rauw</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl34_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblKcal">16</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblKjoule">70</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblWater">93,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblEiwit">1,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblKoolh">1,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblVoedv">3,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlFeeling" title="7,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblFeeling">7,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl34_pnlHealty" title="8,8 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl34_lblHealty">8,8</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl35_hplProdname35" title="Voedingswaarde van anijszaad" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=925">Anijszaad</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl35_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblKcal">425</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblKjoule">1780</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblWater">4,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblEiwit">10,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblKoolh">55,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblSuikers"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblVet">15,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblVerz"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblEov"></span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblMov">5,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblVoedv">15,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlFeeling" title="5,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblFeeling">5,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl35_pnlHealty" title="6,4 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl35_lblHealty">6,4</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl36_hplProdname36" title="Voedingswaarde van ansjovis, vers" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=67">Ansjovis, vers</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl36_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblKcal">102</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblKjoule">427</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblWater">76,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblEiwit">20,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblKoolh">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblVet">2,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblVerz">0,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblEov">0,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblMov">0,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblChol">68,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlFeeling" title="5,5 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblFeeling">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl36_pnlHealty" title="6,5 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl36_lblHealty">6,5</span><img id="ctl00_cphMain_ltvNutrition_ctrl36_prodImg14" title="Ansjovis, vers" class="prodImgB2" src="https://cdn.voedingswaardetabel.nl/img/prod/ansjovis.jpg" alt="Ansjovis, vers" /><img id="ctl00_cphMain_ltvNutrition_ctrl36_prodImgHolder14" title="Ansjovis, vers" class="prodImgHolderB2" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig2.png" alt="Ansjovis, vers" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl37_hplProdname37" title="Voedingswaarde van appel" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=69">Appel</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl37_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblKcal">54</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblKjoule">229</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblWater">84,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblEiwit">0,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblKoolh">12,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblSuikers">11,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblVoedv">2,3</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlFeeling" title="8,4 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblFeeling">8,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl37_pnlHealty" title="9,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl37_lblHealty">9,2</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl38_hplProdname38" title="Voedingswaarde van appelflap" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1073">Appelflap</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl38_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblKcal">388</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblKjoule">1627</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblWater">26,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblEiwit">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblKoolh">40,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblSuikers">23,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblVet">22,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblVerz">13,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblEov">5,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblMov">1,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblChol">50,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblVoedv">5,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlFeeling" title="7,7 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblFeeling">7,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl38_pnlHealty" title="4,3 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl38_lblHealty">4,3</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl39_hplProdname39" title="Voedingswaarde van appelmoes" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=70">Appelmoes</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl39_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblKcal">81</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblKjoule">341</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblWater">78,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblEiwit">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblKoolh">19,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblSuikers">19,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblVoedv">1,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlFeeling" title="7,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblFeeling">7,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl39_pnlHealty" title="6,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl39_lblHealty">6,2</span>
			</div>
                    
		</div>
                
                    <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlSortingExtra" class="ColumnHeaders">
			<div id="ctl00_cphMain_ltvNutrition_ctrl40_extraRowW40" class="vwRowExtra">
				<div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlUnitWordEmpty40" class="rowHeaderWordEmpty">

				</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_rowHeaderWords40">
					<div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW0" class="rowHeaderWord">
						<div title="Kcal" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW1" class="rowHeaderWord">
						<div title="Kjoule" class="rowHeaderWordInnerDiv">
							<span class="cBlue">energie</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW2" class="rowHeaderWord">
						<div title="Water" class="rowHeaderWordInnerDiv">
							<span class="cBlue">water</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW3" class="rowHeaderWord">
						<div title="Eiwit" class="rowHeaderWordInnerDiv">
							<span class="cBlue">eiwit</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW4" class="rowHeaderWord">
						<div title="Koolhydraten" class="rowHeaderWordInnerDiv">
							<span class="cBlue">koolhydraten</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW5" class="rowHeaderWord">
						<div title="Suikers" class="rowHeaderWordInnerDiv">
							<span class="cBlue">suikers</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW6" class="rowHeaderWord">
						<div title="Vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW7" class="rowHeaderWord">
						<div title="Verzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">verzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW8" class="rowHeaderWord">
						<div title="Enkelvoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">enkelvoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW9" class="rowHeaderWord">
						<div title="Meervoudig onverzadigd vet" class="rowHeaderWordInnerDiv">
							<span class="cBlue">meervoudig onverzadigd vet</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW10" class="rowHeaderWord">
						<div title="Cholesterol" class="rowHeaderWordInnerDiv">
							<span class="cBlue">cholesterol</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW11" class="rowHeaderWord">
						<div title="Voedingsvezel" class="rowHeaderWordInnerDiv">
							<span class="cBlue">voedingsvezels</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW13" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gevoelswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gevoelswaarde</span>
						</div>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unitwordW14" class="rowHeaderWord rowHeaderWordExtra">
						<div title="Gezondheidswaarde" class="rowHeaderWordInnerDiv">
							<span class="cBlue">gezondheidswaarde</span>
						</div>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlUnit40" class="rowUnit">
				<div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlUnitPer40" class="rowUnitProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblValue40">Eenheid per 100 gram</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlUnits40">
					<div id="ctl00_cphMain_ltvNutrition_ctrl40_unit0" class="rowUnitItems">
						<span title="kilocalorieën">kcal</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit1" class="rowUnitItems">
						<span title="kilojoules">kJ</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit2" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit3" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit4" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit5" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit6" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit7" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit8" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit9" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit10" class="rowUnitItems">
						<span title="milligram">mg</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit11" class="rowUnitItems">
						<span title="gram">g</span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit13" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_unit14" class="rowUnitItems rowUnitItemsExtra">
						<span></span>
					</div>
				</div>
			</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlSort40" class="rowSort">
				<div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlProdSort40" class="rowSortProdName">
					<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblprodsort40">Sorteren</span>
				</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlSorting40">
					<div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort0" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown0" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown0" title="Kcal aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp0" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp0" title="Kcal oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort1" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown1" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown1" title="Kjoule aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp1" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp1" title="Kjoule oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort2" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown2" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown2" title="Water aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp2" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp2" title="Water oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort3" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown3" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown3" title="Eiwit aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp3" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp3" title="Eiwit oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort4" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown4" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown4" title="Koolhydraten aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp4" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp4" title="Koolhydraten oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort5" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown5" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown5" title="Suikers aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp5" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp5" title="Suikers oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort6" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown6" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown6" title="Vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp6" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp6" title="Vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort7" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown7" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown7" title="Verzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp7" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp7" title="Verzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort8" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown8" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown8" title="Enkelvoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp8" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp8" title="Enkelvoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort9" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown9" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown9" title="Meervoudig onverzadigd vet aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp9" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp9" title="Meervoudig onverzadigd vet oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort10" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown10" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown10" title="Cholesterol aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp10" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp10" title="Cholesterol oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort11" class="rowSortItem">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown11" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown11" title="Voedingsvezel aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp11" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp11" title="Voedingsvezel oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlItemSpacerS13" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort13" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown13" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown13" title="Gevoelswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp13" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp13" title="Gevoelswaarde oplopend sorteren" class="ontop btndown hand" />
					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlItemSpacerS14" class="vwtItemSpacer">

					</div><div id="ctl00_cphMain_ltvNutrition_ctrl40_Sort14" class="rowSortItem rowSortItemExtra">
						<input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortDown14" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortDown14" title="Gezondheidswaarde aflopend sorteren" class="ontop btnup hand" /><input type="submit" name="ctl00$cphMain$ltvNutrition$ctrl40$SortUp14" value="" id="ctl00_cphMain_ltvNutrition_ctrl40_SortUp14" title="Gezondheidswaarde oplopend sorteren" class="ontop btndown hand" />
					</div>
				</div>
			</div>
		</div>
                    <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl40_hplProdname40" title="Voedingswaarde van appelsap" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=613">Appelsap</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl40_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblKcal">42</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblKjoule">180</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblWater">88,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblEiwit">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblKoolh">10,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblSuikers">10,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlFeeling" title="6,7 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblFeeling">6,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl40_pnlHealty" title="7,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl40_lblHealty">7,0</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl41_hplProdname41" title="Voedingswaarde van appelstroop, rinse" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=614">Appelstroop, rinse</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl41_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblKcal">274</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblKjoule">1150</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblWater">29,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblEiwit">3,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblKoolh">63,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblSuikers">52,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblVoedv">3,1</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlFeeling" title="6,9 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblFeeling">6,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl41_pnlHealty" title="7,3 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl41_lblHealty">7,3</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl42_hplProdname42" title="Voedingswaarde van appeltaart" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1072">Appeltaart</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl42_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblKcal">248</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblKjoule">1041</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblWater">48,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblEiwit">4,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblKoolh">35,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblSuikers">22,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblVet">9,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblVerz">3,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblEov">3,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblMov">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblChol">50,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblVoedv">1,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlFeeling" title="7,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblFeeling">7,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl42_pnlHealty" title="5,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl42_lblHealty">5,1</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl43_hplProdname43" title="Voedingswaarde van appelwijn, cider 5 % v/v" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=615">Appelwijn, cider 5 % v/v</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl43_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblKcal">10</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblKjoule">42</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblWater">96,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblEiwit">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblKoolh">2,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblSuikers">2,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlFeeling" title="5,9 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblFeeling">5,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl43_pnlHealty" title="5,1 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl43_lblHealty">5,1</span><img id="ctl00_cphMain_ltvNutrition_ctrl43_prodImg14" title="Appelwijn, cider 5 % v/v" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/cider.jpg" alt="Appelwijn, cider 5 % v/v" /><img id="ctl00_cphMain_ltvNutrition_ctrl43_prodImgHolder14" title="Appelwijn, cider 5 % v/v" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Appelwijn, cider 5 % v/v" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl44_hplProdname44" title="Voedingswaarde van arachideolie, pindaolie" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=616">Arachideolie, pindaolie</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl44_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblKcal">879</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblKjoule">3682</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblWater">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblEiwit">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblKoolh">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblSuikers">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblVet">99,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblVerz">16,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblEov">53,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblMov">30,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblChol">1,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlFeeling" title="5,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblFeeling">5,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl44_pnlHealty" title="6,3 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl44_lblHealty">6,3</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl45_hplProdname45" title="Voedingswaarde van artisjok" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=73">Artisjok</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl45_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblKcal">52</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblKjoule">218</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblWater">85,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblEiwit">2,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblKoolh">9,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblSuikers">9,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblVoedv">1,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlFeeling" title="5,6 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblFeeling">5,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl45_pnlHealty" title="7,6 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl45_lblHealty">7,6</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl46_hplProdname46" title="Voedingswaarde van artisjok, harten" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1201">Artisjok, harten</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl46_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblKcal">46</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblKjoule">195</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblWater">87,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblEiwit">2,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblKoolh">7,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblSuikers">7,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblVet">0,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblVoedv">1,1</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlFeeling" title="6,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblFeeling">6,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl46_pnlHealty" title="7,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl46_lblHealty">7,7</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl47_hplProdname47" title="Voedingswaarde van asperges, blik" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=34">Asperges, blik</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl47_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblKcal">22</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblKjoule">94</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblWater">93,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblEiwit">1,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblKoolh">3,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblSuikers">1,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblVet">0,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblVoedv">0,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlFeeling" title="5,8 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblFeeling">5,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl47_pnlHealty" title="6,3 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl47_lblHealty">6,3</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl48_hplProdname48" title="Voedingswaarde van asperges, vers" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=617">Asperges, vers</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl48_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblKcal">17</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblKjoule">73</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblWater">94,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblEiwit">1,9</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblKoolh">1,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblSuikers">1,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblVet">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblVoedv">1,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlFeeling" title="8,0 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblFeeling">8,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl48_pnlHealty" title="8,7 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl48_lblHealty">8,7</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl49_hplProdname49" title="Voedingswaarde van aubergine" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=71">Aubergine</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl49_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblKcal">25</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblKjoule">107</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblWater">91,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblEiwit">1,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblKoolh">3,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblSuikers">1,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblVet">0,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblVoedv">2,5</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlFeeling" title="6,2 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblFeeling">6,2</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl49_pnlHealty" title="8,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl49_lblHealty">8,0</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl50_hplProdname50" title="Voedingswaarde van augurken, zoetzuur" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=618">Augurken, zoetzuur</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl50_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblKcal">14</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblKjoule">62</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblWater">94,7</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblEiwit">1,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblKoolh">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblSuikers">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblVoedv">1,2</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlFeeling" title="7,6 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblFeeling">7,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl50_pnlHealty" title="7,0 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl50_lblHealty">7,0</span><img id="ctl00_cphMain_ltvNutrition_ctrl50_prodImg14" title="Augurken, zoetzuur" class="prodImgB1" src="https://cdn.voedingswaardetabel.nl/img/prod/augurk.jpg" alt="Augurken, zoetzuur" /><img id="ctl00_cphMain_ltvNutrition_ctrl50_prodImgHolder14" title="Augurken, zoetzuur" class="prodImgHolderB1" src="https://cdn.voedingswaardetabel.nl/img/vwprodImgBig1.png" alt="Augurken, zoetzuur" />
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlRowContainer" class="vwRow1">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl51_hplProdname51" title="Voedingswaarde van avocado" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=1135">Avocado</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl51_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblKcal">188</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblKjoule">790</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblWater">70,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblEiwit">2,6</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblKoolh">1,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblSuikers">1,4</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblVet">18,1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblVerz">3,8</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblEov">11,3</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblMov">2,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblVoedv">6,4</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlFeeling" title="6,5 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblFeeling">6,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl51_pnlHealty" title="8,2 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl51_lblHealty">8,2</span>
			</div>
                    
		</div>
                
                    
                    <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlRowContainer" class="vwRow">
			
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlProdName" class="vwtProdName">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblprodName"></span><a id="ctl00_cphMain_ltvNutrition_ctrl52_hplProdname52" title="Voedingswaarde van azijn" class="prodNameLink" href="/voedingswaarde/voedingsmiddel/?id=619">Azijn</a>
			</div>
                        <span id="ctl00_cphMain_ltvNutrition_ctrl52_lblProd_pk"></span>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlKcal" title="Kcal (kcal)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblKcal">1</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlKjoule" title="Kjoule (kJ)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblKjoule">5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlWater" title="Water (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblWater">98,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlEiwit" title="Eiwit (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblEiwit">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlKoolh" title="Koolhydraten (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblKoolh">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlSuikers" title="Suikers (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblSuikers">0,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlVet" title="Vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblVet">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlVerz" title="Verzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblVerz">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlEov" title="Enkelvoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblEov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlMov" title="Meervoudig onverzadigd vet (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblMov">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlChol" title="Cholesterol (mg)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblChol">0,0</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlVoedv" title="Voedingsvezel (g)" class="vwtItem">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblVoedv">0,0</span>
			</div>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlProdSpacer" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlFeeling" title="6,5 (Gevoelswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblFeeling">6,5</span>
			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlSpacer1" class="vwtItemSpacer">

			</div>
                        <div id="ctl00_cphMain_ltvNutrition_ctrl52_pnlHealty" title="6,3 (Gezondheidswaarde)" class="vwtItemExtra">
				<span id="ctl00_cphMain_ltvNutrition_ctrl52_lblHealty">6,3</span>
			</div>
                    
		</div>
                
                
            <span id="ctl00_cphMain_dtpNutritions"></span>
        
	</div>
    </div>
    <div id="ctl00_cphMain_pnlContantMain" class="contentMain">
		
        <div id="ctl00_cphMain_BottomLinks_bottomlinks" class="bottomlinks">
			

    <div id="ctl00_cphMain_BottomLinks_pnlBottomGoTop" class="pnlgotop">
				
        <a href="#top">TOP <img id="imgBlTop" src="/_lib/img/icons/icon_bullet_arrow_top.png" class="iconsetpmt" /></a>
    
			</div>
    
    <div id="ctl00_cphMain_BottomLinks_pnlHome">
				
        <a id="ctl00_cphMain_BottomLinks_hplHome01" title="Voedingswaardetabel" href="/">Home</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome02" title="Voedingswaardetabel per 100 gram" href="/voedingswaarde/">Voedingswaarde</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome03" title="Voedingswaardetabel per portie" href="/voedingswaarde/per-portie/">Voedingswaarde per portie</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome04" title="Top 10 gezondste producten" href="/voedingswaarde/top10/">Top 10</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome05" title="Over voedingswaardetabel" href="/over/">Over / Wie is?</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome07" title="Bereken" href="/bereken/">Bereken</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome08" title="Veel gestelde vragen" href="/faq/">Faq</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome09" title="Waardevolle links naar andere websites" href="/links/">Links</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome06" title="(W)etenswaardigheden en nieuws" href="/nieuws/">Nieuws</a> |
        <a id="ctl00_cphMain_BottomLinks_hplHome10" title="Boeken" href="/boeken/">Boeken</a>
    
			</div>

    

    

    

    


    


		</div>
    
	</div>
    <input type="hidden" name="ctl00$cphMain$hdfVwtTable" id="hdfVwtTable" value="vw" />
    
    

                    <div id="footerprint">
                        <img id="ctl00_imgVwtFooterPrint" class="icon" src="https://cdn.voedingswaardetabel.nl/img/stripes-small.png" alt=" " />
                        &copy; <span id="ctl00_lblFooterBottomYearPrint">Voedingswaardetabel.nl</span>
                    </div>
                
</div>
                <div id="amgray" class="amgrayB">
	
                    



<div id="ctl00_gAmGrayBottom_pnlL7x9Bottom">
		

    <div id="pnlL7x9Bottomam">
			
        <!-- 13436254/Voedingswaardetabel_Bottom -->
        <div id="div-gpt-ad-1546418814619-0" style="display:block";>
            <script>
                googletag.cmd.push(function() { googletag.display('div-gpt-ad-1546418814619-0'); });
            </script>
        </div>
    
		</div>

	</div>




                
</div>
                <div id="footer">
	
                    <div class="footerBottom">
                            <div class="footerBottomInner">
                            <p><a href="/" title="Voedingswaardetabel"><img src="https://cdn.voedingswaardetabel.nl/img/headerlogo.png" alt="Voedingswaardetabel" title="Voedingswaardetabel" /></a></p>
                            <p>
                                &copy; <span id="ctl00_lblFooterBottomYear">2021</span> &nbsp; <a id="ctl00_hplFooterBottomVW" title="Voedingswaarde" href="/">Voedingswaardetabel.nl</a>
                                <a id="ctl00_hplMsrfbB" href="/" target="_blank"><span class="socialiconfacebook"></span></a>
                                <a id="ctl00_hplMstrttB" target="_blank"><span class="socialicontwitter"></span></a>

                            </p>
                            <p>
                                <a id="ctl00_hplFooterBottomDisc" title="Disclaimer" href="/disclaimer/">Disclaimer</a>
                                <a id="ctl00_hplFooterBottomCont" title="Contact" href="/contact/">Contact</a>
                                <a id="ctl00_HplCookieConsense" title="Pas je cookieinstellingen aan" onclick="showConsentManager()" href="../#">Cookieinstellingen</a>
                                
                            </p>
                            <p>
                                <a id="ctl00_hplFooterBottomJAgd" title="Design by JAgd graphic design" href="http://www.jagd.nl" target="_blank">Graphic design by JAgd</a>
                                <a id="ctl00_hplFooterBottomSeo" title="Hosting &amp;amp; webdesign by Seoptics" href="http://www.seoptics.nl" target="_blank">Hosting &amp; webdesign by Seoptics</a>
                                







<a href="https://www.voedingswaardetabel.nl/leden/registreren/" target="_blank" title="Account maken">Account maken</a>
                                <a href="https://www.voedingswaardetabel.nl" title="Voedingswaardetabel"><img src="https://cdn.voedingswaardetabel.nl/img/icons/nl.png" class="iconsetr" alt="Voedingswaardetabel - Nederlands" /></a>
                                <a href="http://www.nutritiontable.com" title="Nutrition Table"><img src="https://cdn.voedingswaardetabel.nl/img/icons/us.png" class="iconsetr" alt="Nutrition Table - English" /></a>
                            </p>
                        </div>
                    </div>
                
</div>
                
<div id="popup_iconinfo" class="popup_block">
    <script type="text/javascript">
        function showInfo(infoid) {
            getIconInfoAjax(infoid)
        }
        function getIconInfoAjax(infoid) {
            $.ajax({
                type: "Get",
                url: "/_lib/ajax/iconinfo.aspx",
                cache: false,
                data: {
                    inid: infoid,
                    acall: $("#hdfAjaxcall").val()
                },
                success: function (data) {
                    if (data != "") {
                        setIconInfo(data);
                    }
                },
                error: function () {
                    //alert('Err; No Info');
                }
            });
        }
        function setIconInfo(inp) {
            var arrInfo = inp.split("||");
            $("#iiTitle").html("<img src='/_lib/img/pixel.gif' class='iconsetbig icon_info_big' alt='' /> &nbsp; " + arrInfo[0]);
            $("#iiDesc").html(arrInfo[1]);
        }
    </script>
    <div class="popup_block_text">
        <h2 id="iiTitle"></h2>
        <hr class="hr" />
        <div id="iiDesc"></div>
    </div>
</div>
            </div>
        </div>
        <div id="searcProdContainer" class="hidden">
            <div id="searcProdInnerContainer">
                <div class="col-12 col-t-15">
                    <span class="closebtn hand" onclick="closeSearch()">&times;</span>
                    <input name="ctl00$txtSearch" type="text" maxlength="20" id="txtSearch" class="input" />
                    <input type="hidden" name="ctl00$tbwSearch_ClientState" id="ctl00_tbwSearch_ClientState" />
                    <input type="submit" name="ctl00$btnSearch" value="Zoeken in de tabel" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$btnSearch&quot;, &quot;&quot;, true, &quot;searchprods&quot;, &quot;&quot;, false, false))" id="ctl00_btnSearch" class="button buttongreen hand" />
                    <span id="rfvSearch" class="errormessage" style="display:none;">Geen zoekterm ingevuld</span>
                    <span id="ctl00_revSearch" class="errormessage" style="display:none;">Ongeldige of te weinig karakters gebruikt</span>
                    <div class="clearmargin"></div>
                    <hr class="hr" />
                    <h1>Uitgebreide opties</h1>
                    <span id="ctl00_lblFilGroup">Productgroep</span>:<br />
                        <select name="ctl00$ddlProdGroup" id="ddlProdGroup" class="select-css W300m">
	<option selected="selected" value="-1">-- kies een productgroep --</option>
	<option value="99">Alle groepen (max. 60 producten)</option>
	<option value="9">Aardappels en aardappelproducten</option>
	<option value="25">Alcoholische dranken</option>
	<option value="2">Brood en broodproducten</option>
	<option value="7">Desserts</option>
	<option value="27">Diversen</option>
	<option value="24">Dranken</option>
	<option value="15">Eieren en eiproducten</option>
	<option value="11">Fruit</option>
	<option value="26">Gemaksvoeding</option>
	<option value="1">Granen</option>
	<option value="10">Groente en peulvruchten</option>
	<option value="21">Hartige snacks</option>
	<option value="8">IJs</option>
	<option value="6">Kaas</option>
	<option value="4">Koek en gebak</option>
	<option value="22">Kruiden en specerijen</option>
	<option value="5">Melk en melkproducten</option>
	<option value="12">Noten en zaden</option>
	<option value="19">Oli&#235;n en vetten</option>
	<option value="3">Ontbijtgranen</option>
	<option value="18">Schaal- en schelpdieren</option>
	<option value="20">Soep en sauzen</option>
	<option value="17">Vis en visproducten</option>
	<option value="13">Vlees</option>
	<option value="16">Vleesvervangers</option>
	<option value="14">Vleeswaren en worst</option>
	<option value="23">Zoetwaren</option>

</select>
                    <div class="clearmargin"></div>
                    <span id="ctl00_lblFilSrchIn">Zoeken in</span>:<br />
                    <div id="divrblVW">
                        <table id="rblVW" class="radiobuttons">
	<tr>
		<td><input id="rblVW_0" type="radio" name="ctl00$rblVW" value="vw" checked="checked" /><label for="rblVW_0">voedingswaarde</label></td>
	</tr><tr>
		<td><input id="rblVW_1" type="radio" name="ctl00$rblVW" value="vm" /><label for="rblVW_1">vitamines</label></td>
	</tr><tr>
		<td><input id="rblVW_2" type="radio" name="ctl00$rblVW" value="mn" /><label for="rblVW_2">mineralen</label></td>
	</tr>
</table>
                    </div>
                    <div class="clearmargin"></div>
                    <span id="ctl00_lblFilSrt">Sorteren</span>:<br />
                    <div id="filtersortVW">
	
                        <select name="ctl00$ddlProdSortVW" id="ddlProdSortVW" class="select-css W300m">
		<option selected="selected" value="-1">-- kies sorteren --</option>
		<option value="product">Voedingsmiddel</option>
		<option value="kcal">kcal</option>
		<option value="kjoule">kjoule</option>
		<option value="water">Water</option>
		<option value="eiwit">Eiwit</option>
		<option value="koolh">Koolhydraten</option>
		<option value="suikers">Suikers</option>
		<option value="vet">Vet</option>
		<option value="verz">Verzadigd vet</option>
		<option value="eov">Enkelvoudig onverzadigd vet</option>
		<option value="mov">Meervoudig onverzadigd vet</option>
		<option value="chol">Cholesterol</option>
		<option value="voedv">Voedingsvezels</option>
		<option value="prodfeeling">Gevoelswaarde</option>
		<option value="prodhealty">Gezondheidswaarde</option>

	</select>
                    
</div>
                    <div id="filtersortVM" class="hidden">
	
                        <select name="ctl00$ddlProdSortVM" id="ddlProdSortVM" disabled="disabled" class="aspNetDisabled select-css W300m">
		<option selected="selected" value="-1">-- kies sorteren --</option>
		<option value="product">Voedingsmiddel</option>
		<option value="vita">Vitamine A</option>
		<option value="vitb1">Vitamine B1</option>
		<option value="vitb2">Vitamine B2</option>
		<option value="vitb6">Vitamine B6</option>
		<option value="vitb11">Vitamine B11</option>
		<option value="vitb12">Vitamine B12</option>
		<option value="vitc">Vitamine C</option>
		<option value="vitd">Vitamine D</option>
		<option value="prodfeeling">Gevoelswaarde</option>
		<option value="prodhealty">Gezondheidswaarde</option>

	</select>
                    
</div>
                    <div id="filtersortMN" class="hidden">
	
                        <select name="ctl00$ddlProdSortMN" id="ddlProdSortMN" disabled="disabled" class="aspNetDisabled select-css W300m">
		<option selected="selected" value="-1">-- kies sorteren --</option>
		<option value="product">Voedingsmiddel</option>
		<option value="minna">Natrium</option>
		<option value="mink">Kalium</option>
		<option value="minca">Calcium</option>
		<option value="minp">Fosfor</option>
		<option value="minfe">IJzer</option>
		<option value="minmg">Magnesium</option>
		<option value="mincu">Koper</option>
		<option value="minzn">Zink</option>
		<option value="prodfeeling">Gevoelswaarde</option>
		<option value="prodhealty">Gezondheidswaarde</option>

	</select>
                    
</div>
                    <div class="clearmargin"></div>
                    <span id="rblSort" class="radiobuttons"><input id="rblSort_0" type="radio" name="ctl00$rblSort" value="desc" /><label for="rblSort_0">Aflopend</label><input id="rblSort_1" type="radio" name="ctl00$rblSort" value="asc" /><label for="rblSort_1">Oplopend</label></span>
                    <div class="clearmargin"></div>
                    <span id="ctl00_lblFilShowper">Voedingswaarde</span>:<br />
                    <span id="rbl100PP" class="radiobuttons"><input id="rbl100PP_0" type="radio" name="ctl00$rbl100PP" value="100" /><label for="rbl100PP_0">per 100 gram</label><input id="rbl100PP_1" type="radio" name="ctl00$rbl100PP" value="pp" /><label for="rbl100PP_1">per portie</label></span>
                </div>
            </div>
        </div>
        <input type="hidden" name="ctl00$hdfBookAd" id="hdfBookAd" value="1" />
        <input type="hidden" name="ctl00$hdfPP" id="hdfPP" value="0" />
        <input type="hidden" name="ctl00$hdfAjaxcall" id="hdfAjaxcall" value="VnrHvf8Th1D4QM0bjcM/X3Cy6p1KsJDK" />
        <input type="hidden" name="ctl00$hdfFilterClose" id="hdfFilterClose" value="Zoekfilters sluiten" />
        <input type="hidden" name="ctl00$hdfFilterOpen" id="hdfFilterOpen" value="Zoekfilters openen" />
        <input type="hidden" name="ctl00$hdfFilterAct" id="hdfFilterAct" value="Zoekterm niet mogelijk" />
        
        <script type="text/javascript" src="https://cdn.voedingswaardetabel.nl/jav/jquery-3.5.1.min.js"></script>
        <script type="text/javascript" src="https://cdn.voedingswaardetabel.nl/jav/jquery.v1.min.js"></script>
        <script type="text/javascript" src="/_lib/jav/jsall.v1.js"></script>
        
    <script type="text/javascript">
        function goCompare() { window.location.href = "/voedingswaarde/vergelijk/"; }
    </script>

    
<script type="text/javascript">
//<![CDATA[
var Page_Validators =  new Array(document.getElementById("rfvSearch"), document.getElementById("ctl00_revSearch"));
//]]>
</script>

<script type="text/javascript">
//<![CDATA[
var rfvSearch = document.all ? document.all["rfvSearch"] : document.getElementById("rfvSearch");
rfvSearch.controltovalidate = "txtSearch";
rfvSearch.errormessage = "Geen zoekterm ingevuld";
rfvSearch.display = "Dynamic";
rfvSearch.validationGroup = "searchprods";
rfvSearch.evaluationfunction = "RequiredFieldValidatorEvaluateIsValid";
rfvSearch.initialvalue = "";
var ctl00_revSearch = document.all ? document.all["ctl00_revSearch"] : document.getElementById("ctl00_revSearch");
ctl00_revSearch.controltovalidate = "txtSearch";
ctl00_revSearch.errormessage = "Ongeldige of te weinig karakters gebruikt";
ctl00_revSearch.display = "Dynamic";
ctl00_revSearch.validationGroup = "searchprods";
ctl00_revSearch.evaluationfunction = "RegularExpressionValidatorEvaluateIsValid";
ctl00_revSearch.validationexpression = "[\\.\\,0-9a-zA-Z\\xA1-\\xFF\\s]{3,20}";
//]]>
</script>


<script type="text/javascript">
//<![CDATA[

var Page_ValidationActive = false;
if (typeof(ValidatorOnLoad) == "function") {
    ValidatorOnLoad();
}

function ValidatorOnSubmit() {
    if (Page_ValidationActive) {
        return ValidatorCommonOnSubmit();
    }
    else {
        return true;
    }
}
        //]]>
</script>

<script src="/Scripts/AjaxControlToolkit/Bundle?v=8DXPDBEvJujdA4qnP54BbERNqobWj5mwdTEzSytCRF41" type="text/javascript"></script>
<script src="../Scripts/AjaxControlToolkit/Release/Common.js" type="text/javascript"></script>
<script src="../Scripts/AjaxControlToolkit/Release/ComponentSet.js" type="text/javascript"></script>
<script src="../Scripts/AjaxControlToolkit/Release/BaseScripts.js" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=cGdF70MPUJJclxXAbXeqIrf2-TjYFaWtJpzhi8F8OtIDGr6vWObKJmqGaLkTwZG_g_zNyP5Ey0XXFNTpEvN1bVCocUrfx_Y-4Y71oRAA8AiHRxlgqRSKG7T53q3i_ubu1_r-D2XRAqczTHywzeJQMQ2&amp;t=17b84382" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[

theForm.oldSubmit = theForm.submit;
theForm.submit = WebForm_SaveScrollPositionSubmit;

theForm.oldOnSubmit = theForm.onsubmit;
theForm.onsubmit = WebForm_SaveScrollPositionOnSubmit;
Sys.Application.add_init(function() {
    $create(Sys.Extended.UI.TextBoxWatermarkBehavior, {"ClientStateFieldID":"ctl00_tbwSearch_ClientState","id":"ctl00_tbwSearch","watermarkCssClass":"inputwatermark","watermarkText":"product"}, null, null, $get("txtSearch"));
});

document.getElementById('rfvSearch').dispose = function() {
    Array.remove(Page_Validators, document.getElementById('rfvSearch'));
}

document.getElementById('ctl00_revSearch').dispose = function() {
    Array.remove(Page_Validators, document.getElementById('ctl00_revSearch'));
}
//]]>
</script>
</form>
    <script>
    function openNav() {
        if ($("#Sidenav").hasClass("SideNavWidth")) {
            closeNav()
        } else {
            $("#Sidenav").addClass("SideNavWidth");
            $("#outercontainer").addClass("menutrans");
            $(".headerMenu").css('left','initial');
        }
    }
    function closeNav() {
        $("#Sidenav").removeClass("SideNavWidth");
        $("#outercontainer").removeClass("menutrans");
        $(".headerMenu").css('left','0');
    }
    function closeSearch() {    
        $("#searcProdContainer").addClass("hidden");
    }
    //if('serviceWorker' in navigator) {
    //    navigator.serviceWorker.register('/service-worker.js');
        //}
        $("#CkbProMem").change(function () {
            __doPostBack("__Page", 'switchProMem||' + $("#CkbProMem").prop("checked"))
        });
    </script>
    
        <script type="text/javascript" src="https://massariuscdn.com/prod/massarius.js"></script>
    
</body>
</html>
"""


def dictify(div):
    result = {}
    for li in div.find_all("div", recursive=False):
        ul = li.find("span")
        if ul:
            key = ul.get('id')
            result[key] = li.text.replace('\n', '')
    return result


soup = BeautifulSoup(html_doc, 'html.parser')
for linkText in soup.find_all("div", id=re.compile('.*pnlRowContainer')):
    pprint(dictify(linkText))

