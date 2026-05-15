<!DOCTYPE html>
<html>
<head>
  <title>privacy</title>
        <meta property="og:url" name="url" content="844b3ad2b33e3130_privacy.php">      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
  <meta charset="utf-8">
 <link rel="icon" type="image/png" href="/images/favicon-pv.png?v4.1" />
  <style> 
    *{
     box-sizing:border-box; 
    }
  body{
    margin:0;
    padding:0;
    }
  </style>


    <script>
      window.__app = {
        visit_id: undefined,
        query: Object.freeze(window.location.search.substr(1).split(/&+/).reduce(function(map,c) {
          var a = c.match(/([^=]+)=(.*)/) || []
          if (a[1]) {
            map[a[1]] = a[2]
          }
          return map
        }, {})),
        cookies: Object.freeze(document.cookie.split(/;\s+/).reduce(function(map,c) {
          var a = c.match(/([^=]+)=(.*)/) || []
          if (a[1]) {
            map[a[1]] = a[2]
          }
          return map
        }, {})),
      }
    </script>
  
        <script defer async>
          (function(script) {
            script.src = "//" + location.hostname
              + "/api/visits?page_id=6&page_version=a&request_id=6817D529%3A4429_C0A85015%3A01BB_6A0695D4_112C81%3A21D7A0"
              + "&querystring=" + encodeURIComponent(window.location.search.substr(1))
              + "&fbclid=" + encodeURIComponent(__app.query.fbclid || "")
              + "&fbp=" + encodeURIComponent(__app.cookies._fbp || "")
              + "&fbc=" + encodeURIComponent(__app.cookies._fbc || "")
              + "&referrer=" + encodeURIComponent(document.referrer);
            document.head.appendChild(script);
          })(document.createElement("script"));
        </script>
      
        <script>
          function recordEmailConversion(email, page_id) {
            return new Promise(function(resolve, reject) {

              const url = "//"
                + location.hostname
                + "/api/email-conversions"
                + location.search

              const xhr = new XMLHttpRequest

              xhr.onreadystatechange = function() {

                if (xhr.readyState !== XMLHttpRequest.DONE) {
                  return
                }

                if (Math.floor(xhr.status / 100) !== 2) {
                  return reject(xhr.responseText || "Network Error")
                }

                try {
                  var response = JSON.parse(xhr.responseText)
                }
                catch (error) {
                  return reject("Failed parsing server response: " + error.toString())
                }

                resolve(response)
              }

              xhr.onerror = reject

              xhr.open("POST", url)
              xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")

              xhr.send(JSON.stringify({
                email,
                page_id: page_id || 6,
                page_version: page_id
                  ? undefined
                  : "a" || undefined,
                referrer: document.referrer,
                request_id: "6817D529:4429_C0A85015:01BB_6A0695D4_112C81:21D7A0" || undefined,
              }))
            })
          }
        </script>
      <script>
      	window.clickbank = {
      		vendor: "provive"
      	}
      </script>
      <script src="https://scripts.clickbank.net/hop.min.js" defer></script></head>
<body>

  
    <link rel='stylesheet' href="a29236eed54ff257_bootstrap.css" type="text/css">
<link rel='stylesheet' href="/css/custom.css?v9" type="text/css">

<section class="banner-sec">
  <div class="container">
    <div class="row">
      <div class="col-md-12"> 
      <a href="../index.html">
      <img src="6ad0acd64218fa26_LOGO-pv.png?v3" alt="img" class="img-responsive center-block logo-white">
      </a> 
      </div>
    </div>
  </div>
</section><section class="main-sec">
    <div class="container">
        <div class="des-box-other">
            <div class="row">
                <div class="col-md-12">
                    <h2>Privacy Policy</h2>
                    <h4>Effective Date: April 2024</h4>
                    <p>The following Privacy Policy governs the online information collection practices of ProstaVive ("we" or "us"). Specifically, it outlines the types of information that we gather about
                        you while you are using the Prostavive.org website (the "Site"), and the ways in which we use
                        this information. This Privacy Policy, including our children's privacy statement, does not
                        apply to any information you may provide to us or that we may collect offline and/or through
                        other means (for example, at a live event, via telephone, or through the mail).</p>
                    <p>Please read this Privacy Policy carefully. By visiting and using the Site, you agree that your
                        use of our Site, and any dispute over privacy, is governed by this Privacy Policy. Because the
                        Web is an evolving medium, we may need to change our Privacy Policy at some point in the future,
                        in which case we'll post the changes to this Privacy Policy on this website and update the
                        Effective Date of the policy to reflect the date of the changes. By continuing to use the Site
                        after we post any such changes, you accept the Privacy Policy as modified.</p>
                    <h3>How We Collect and Use Information</h3>
                    <p>We may collect and store personal or other information that you voluntarily supply to us online
                        while using the Site (e.g., while on the Site or in responding via email to a feature provided
                        on the Site). The Site only contacts individuals who specifically request that we do so or in
                        the event that they have signed up to receive our messaging, attended one of our events, or have
                        purchased one of our products. The Site collects personally identifying information from our
                        users during online registration and online purchasing. Generally, this information includes
                        name and e-mail address for registration or opt-in purposes and name, postal address, and credit
                        card information when registering for our events or purchasing our products. All of this
                        information is provided to us by you.</p>
                    <p>We also collect and store information that is generated automatically as you navigate online
                        through the Site. For example, we may collect information about your computer's connection to
                        the Internet, which allows us, among other things, to improve the delivery of our web pages to
                        you and to measure traffic on the Site. We also may use a standard feature found in browser
                        software called a "cookie" to enhance your experience with the Site. Cookies are small files
                        that your web browser places on your hard drive for record-keeping purposes. By showing how and
                        when visitors use the Site, cookies help us deliver advertisements, identify how many unique
                        users visit us, and track user trends and patterns. They also prevent you from having to
                        re-enter your preferences on certain areas of the Site where you may have entered preference
                        information before. The Site also may use web beacons (single-pixel graphic files also known as
                        "transparent GIFs") to access cookies and to count users who visit the Site or open
                        HTML-formatted email messages.</p>
                    <p>We use the information we collect from you while you are using the Site in a variety of ways,
                        including using the information to customize features; advertising that appear on the Site; and,
                        making other offers available to you via email, direct mail or otherwise. We also may provide
                        your information to third parties, such as service providers, contractors and third-party
                        publishers. Unless you inform us in accordance with the process described below, we reserve the
                        right to use all of the information collected from and about you while you are using the Site
                        such as to enable us to provide you with information about products and services. If you do not
                        wish your information to be used for these purposes, you must send a letter to the Online
                        Privacy Coordinator whose address is listed at the end of this Privacy Policy requesting to be
                        taken off any lists of information that may be used for these purposes or that may be given or
                        sold to third-parties. Your email address will never be shared with any third parties without your explicit permission via an opt-in page.</p>
                    <p>Please keep in mind that whenever you voluntarily make your personal information available for
                        viewing by third parties online - for example on message boards, web logs, through email, or in
                        chat areas - that information can be seen, collected and used by others besides us. We cannot be
                        responsible for any unauthorized third-party use of such information.</p>
                    <p>Some of our third-party advertisers and ad servers that place and present advertising on the Site also may collect
                    information from you via cookies, web beacons or similar technologies. These
                        third-party advertisers and ad servers may use the information they collect to help present
                        their advertisements, to help measure and research the advertisements' effectiveness, or for
                        other purposes. The use and collection of your information by these third-party advertisers and
                        ad servers is governed by the relevant third-party's privacy policy and is not covered by our
                        Privacy Policy. Indeed, the privacy policies of these third-party advertisers and ad servers may
                        be different from ours. If you have any concerns about a third party's use of cookies or web
                        beacons or use of your information, you should visit that party's website and review its privacy
                        policy.</p>
                    <p>The Site also includes links to other websites and provides access to products and services
                        offered by third parties, whose privacy policies we do not control. When you access another
                        website or purchase third-party products or services through the Site, use of any information
                        you provide is governed by the privacy policy of the operator of the site you are visiting or
                        the provider of such products or services.</p>
                    <p>We may also make some content, products and services available through our Site or by emailing
                        messages to you through cooperative relationships with third-party providers, where the brands
                        of our provider partner appear on the Site in connection with such content, products and/or
                        services. We may share with our provider partner any information you provide, or that is
                        collected, in the course of visiting any pages that are made available in cooperation with our
                        provider partner. In some cases, the provider partner may collect information from you directly,
                        in which cases the privacy policy of our provider partner may apply to the provider partner's
                        use of your information. The privacy policy of our provider partners may differ from ours. If
                        you have any questions regarding the privacy policy of one of our provider partners, you should
                        contact the provider partner directly for more information. Your email address will never be shared with any third parties without your explicit permission via an opt-in page.</p>
                    <p>Be aware that we may occasionally release information about our visitors when release is
                        appropriate to comply with law or to protect the rights, property or safety of users of the Site
                        or the public.</p>
                    <p>Please also note that as our business grows, we may buy or sell various assets. In the unlikely
                        event that we sell some or all of our assets, or one or more of our websites is acquired by
                        another company, information about our users may be among the transferred assets.</p>
                    <h3>Google Analytics</h3>
                    <p>We also use Google Analytics Advertiser Features to optimize our business. Advertiser features
                        include:</p>
                    <ul>
                        <li>Remarketing with Google Analytics</li>
                        <li>Google Display Network Impression Reporting</li>
                        <li>DoubleClick Platform integrations</li>
                        <li>Google Analytics Demographics and Interest Reporting</li>
                    </ul>
                    <p>By enabling these Google Analytics Display features, we are required to notify our visitors by
                        disclosing the use of these features and that we and third-party vendors use first-party cookies
                        (such as the Google Analytics cookie) or other first-party identifiers, and third-party cookies
                        (such as the DoubleClick cookie) or other third-party identifiers together to gather data about
                        your activities on our Site. Among other uses, this allows us to contact you if you begin to
                        fill out our check-out form but abandon it before completion with an email reminding you to
                        complete your order. The &ldquo;Remarketing&rdquo; feature allows us to reach people who
                        previously visited our Site, and match the right audience with the right advertising message.
                    </p>
                    <p>You can opt out of Google&rsquo;s use of cookies by visiting Google&rsquo;s ad settings and/or
                        you may opt out of a third-party vendor's use of cookies by visiting the <a
                            href="http://www.networkadvertising.org/managing/opt_out.asp" target="_blank"
                            class="link-href" rel="noopener">Network Advertising Initiative opt-out page</a>.</p>
                    <h3>Facebook</h3>
                    <p>As advertisers on Facebook and through our Facebook page, we, (not Facebook) may collect content
                        or information from a Facebook user and such information may be used in the same manner
                        specified in this Privacy Policy. You consent to our collection of such information.</p>
                    <p>We abide by Facebook&rsquo;s Data Use Restrictions.</p>
                    <ul>
                        <li>Any ad data collected, received or derived from our Facebook ad (&ldquo;Facebook advertising
                            data&rdquo;) is only shared with someone acting on our behalf, such as our service provider.
                            We are responsible for ensuring that our service providers protect any Facebook advertising
                            data or any other information obtained from us, limit our use of all of that information,
                            and keep it confidential and secure.</li>
                        <li>We do not use Facebook advertising data for any purpose (including retargeting, commingling
                            data across multiple advertisers&rsquo; campaigns, or allowing piggybacking or redirecting
                            with tags), except on an aggregate and anonymous basis (unless authorized by Facebook) and
                            only to assess the performance and effectiveness of our Facebook advertising campaigns.</li>
                        <li>We do not use Facebook advertising data, including the targeting criteria for a Facebook ad,
                            to build, append to, edit, influence, or augment user profiles, including profiles
                            associated with any mobile device identifier or other unique identifier that identifies any
                            particular user, browser, computer or device.</li>
                        <li>We do not transfer any Facebook advertising data (including anonymous, aggregate, or derived
                            data) to any ad network, ad exchange, data broker or other advertising or monetization
                            related service.</li>
                    </ul>
                    <h3>General Data Protection Regulation (GDPR)</h3>
                    <p>The GDPR took effect on May 25, 2018, and is intended to protect the data of European Union (EU)
                        citizens.</p>
                    <p>As a company that markets its site, content, products and/or services online we do not
                        specifically target our marketing to the EU or conduct business in or to the EU in any
                        meaningful way. If the data that you provide to us in the course of your use of our site,
                        content, products and/or services is governed by GDPR, we will abide by the relevant portions of
                        the Regulation.</p>
                    <p>If you are a resident of the European Economic Area (EEA), or are accessing this site from within
                        the EEA, you may have the right to request: access to, correction of, deletion of; portability
                        of; and restriction or objection to processing, of your personal data, from us. This includes
                        the &ldquo;right to be forgotten.&rdquo;</p>
                    <p>To make any of these requests, please contact our GDPR contact at <a href="/cdn-cgi/l/email-protection#bef9faeeecfeeeccd1cdcadfc8d7c8db90d1ccd9" class="link-href"><span class="__cf_email__" data-cfemail="89cecdd9dbc9d9fbe6fafde8ffe0ffeca7e6fbee">[email&#160;protected]</span></a>.</p>
                    <h3>California Consumer Privacy Act (CCPA)</h3>
                    <p>The CCPA took effect on January 1, 2020, and is intended to protect the personal information of
                        California residents.</p>
                    <p>The CCPA has certain threshold requirements which a company must meet in order to be required to
                        comply with its provisions. Upon information and belief, our company does not meet those
                        thresholds. In the event of a change in our status, and if the data that you provide in the
                        course of your use of our site, content, products and/or services is governed by CCPA, we will
                        abide by the relevant portions of the Act.</p>
                    <p>If you are a resident of the state of California, you may have the right to: request disclosure
                        of the personal information we have collected about you and the types of third parties with whom
                        it has been shared; request a portable copy of your information; opt out from marketing messages
                        or the sale of your information to third parties; and request deletion of your personal
                        information.</p>
                    <p>To make these requests, please contact our CCPA contact at <a href="/cdn-cgi/l/email-protection#42212132230212302d313623342b34276c2d3025" class="link-href"><span class="__cf_email__" data-cfemail="84e7e7f4e5c4d4f6ebf7f0e5f2edf2e1aaebf6e3">[email&#160;protected]</span></a></p>
                    <h3>Children's Privacy Statement</h3>
                    <p>This children's privacy statement explains our practices with respect to the online collection
                        and use of personal information from children under the age of thirteen, and provides important
                        information regarding their rights under federal law with respect to such information.</p>
                    <ul>
                        <li>This Site is not directed to children under the age of thirteen and we do NOT knowingly
                            collect personally identifiable information from children under the age of thirteen as part
                            of the Site. We screen users who wish to provide personal information in order to prevent
                            users under the age of thirteen from providing such information. If we become aware that we
                            have inadvertently received personally identifiable information from a user under the age of
                            thirteen as part of the Site, we will delete such information from our records. If we change
                            our practices in the future, we will obtain prior, verifiable parental consent before
                            collecting any personally identifiable information from children under the age of thirteen
                            as part of the Site.</li>
                        <li>Because we do not collect any personally identifiable information from children under the
                            age of thirteen as part of the Site, we also do NOT knowingly distribute such information to
                            third parties.</li>
                        <li>We do NOT knowingly allow children under the age of thirteen to publicly post or otherwise
                            distribute personally identifiable contact information through the Site.</li>
                        <li>Because we do not collect any personally identifiable information from children under the
                            age of thirteen as part of the Site, we do NOT condition the participation of a child under
                            thirteen in the Site's online activities on providing personally identifiable information.
                        </li>
                    </ul>
                    <h3>How do we store your information?</h3>
                    <p>Your information is stored at the list server that delivers the Site content and messaging. Your
                        information can only be accessed by those who help manage those lists in order to deliver e-mail
                        to those who would like to receive the Site material.</p>
                    <p>All of the messaging or emails that are sent to you by the Site include an unsubscribe link in
                        them. You can remove yourself at any time from our mailing list by clicking on the unsubscribe
                        link that can be found in every communication that we send you.</p>
                    <h3>Disclaimer</h3>
                    <p>This policy may be changed at any time at our discretion. If we should update this policy, we
                        will post the updates to this page on our Website.</p>
                    <p>If you have any questions or concerns regarding our privacy policy please direct them to: <a href="/cdn-cgi/l/email-protection#e1929491918e9395a1b1938e92958097889784cf8e9386" class="link-href"><span class="__cf_email__" data-cfemail="f685838686998482b6a68499858297809f8093d8998491">[email&#160;protected]</span></a>.</p>
                </div>
            </div>
        </div>
    </div>
</section>
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="/js/jquery.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
  .foot-sec {
    background: #000;
    color: #fff;
    text-align: center;
    padding: 30px 0 30px;
}
.foot-list {
    padding-left: 0;
    margin-bottom: 20px;
}
  
.foot-list li {
    display: inline;
    padding-left: 0;
    list-style-type: none;
}
  
.foot-list li a {
    color: #fff !important;
    padding: 0px 5px;
    font-size: 16px;
    text-decoration: none;
    font-family: 'Montserrat', sans-serif;
}
  
.foot-sec p {
    color: #fff;
    font-size: 15px;
    line-height: 150%;
    font-family: 'Montserrat', sans-serif;
} 
  
.foot-wrapper {
    margin: 0 22%;
}
  
.foot-wrapper p {
    font-size: 11px !important;
    color: #fff !important;
    margin-top: 2%;
    line-height: 150%;
   font-family: 'Montserrat', sans-serif;
}
.p-link {
    margin-top: 10px !important;
}
  
.link-here {
    color: #fff;
    font-weight: bold;
    font-family: 'Montserrat', sans-serif;
}
.link-here:hover {
    color: #fff;
    font-weight: bold;
    text-decoration: underline;
}  
  
@media only screen and (max-width: 480px){
.foot-list {
    font-size: 20px !important;
}
.foot-sec p {
    font-size: 16px !important;
} 
.foot-wrapper {
    margin: 0 5%;
}  
   
}  
</style>




<footer class="foot-sec">
<ul class="foot-list">
        <li><a href="844b3ad2b33e3130_privacy.php" target="_blank" rel="noopener">Privacy</a>|</li>
        <li><a href="3f4778f3e9fc4fbd_terms.php" target="_blank" rel="noopener">Terms and Conditions</a>|</li>
        <li><a href="8f9543aa441b7e12_disclaimer.php" target="_blank" rel="noopener">Disclaimer</a>|</li>
        <li><a href="a5c38e75f0b1c9c6_references.php" target="_blank" rel="noopener">References</a>|</li>
        <li><a href="268908007a902523_contact.php" target="_blank" rel="noopener">Returns</a>|</li>
        <li><a href="83dedddda9046ce9_refunds.php" target="_blank" rel="noopener">Refunds</a>|</li>
        <li><a href="f6cc064843f34b01_contact.php" target="_blank" rel="noopener">Contact</a>|</li>
        <li><a href="2329481c3defa328_shipping.html" target="_blank" rel="noopener">Shipping Policy</a></li>
    </ul>
<p><span id="copy-writer">Copyright ProstaVive. All rights reserved.</span></p>
<div class="foot-wrapper">
  <p>Testimonials, case studies, and examples found on this page are results that have been forwarded to us by users of ProstaVive and related products. They are not intended to represent or guarantee that anyone will achieve the same or similar results.</p>
  <p>Statements on this website have not been evaluated by the Food and Drug Administration. Products are not intended to diagnose, treat, cure or prevent any disease. If you are pregnant, nursing, taking medication, or have a medical condition, consult your physician before using our products.</p>
  <p>The content of this site is for informational purposes only, and is not intended to replace professional medical advice, diagnosis or treatment. Always seek the advice of your doctor or other qualified health care professional about a medical condition, a suspected medical condition, and before starting a diet, exercise, or supplementation program or take or stop a medication.</p>
  <!--<p>The use of any information provided by this site and others appearing on the site is solely at your own risk. The site and its contents are provided "as is". -->

</div>
</footer>

<script src="..//js/jquery.js"></script>
<script src="..//js/bootstrap.js"></script> <!-- Plugin JavaScript -->
<script src="https://display.buygoods.com/v1/disclaimer?id=disclaimer&account_id=8198"></script><script src="js/jquery.js"></script><!-- ClickBank Trust Badge -->


<script defer async>
      document.addEventListener("DOMContentLoaded", function() {

        const augmentedPaymentLinks = [["pay.clickbank.net",{"user_id":"__user_id","page_id":"__page_id","page_version":"__page_version","hostname":"__hostname"}]]
          .sort(function(a,b) { return b[0].length - a[0].length })
          .map(function(entry) {
            return [
              new RegExp("^https?://(.+\\.)?" + entry[0], "i"),
              entry[1],
              Object.keys(entry[1]).reduce(function(map,key) {
                map[key] = new RegExp("[?|&]" + entry[1][key] + "=", "i")
                return map
              }, {})
            ]
          })

        for (let el of document.getElementsByTagName("A")) {
          const href = el.getAttribute("href")
          if (!href || href === "#") {
            continue
          }
          for (let entry of augmentedPaymentLinks) {
            if (!entry[0].test(href)) {
              continue
            }
            const params = []
            if (entry[1].user_id && !entry[2].user_id.test(href)) {
              const user_id = __app.cookies.user_id || ""
              params.push(entry[1].user_id + "=" + encodeURIComponent(user_id))
            }
            if (entry[1].page_id && !entry[2].page_id.test(href)) {
              params.push(entry[1].page_id + "=6")
            }
            if (entry[1].page_version && !entry[2].page_version.test(href)) {
              params.push(entry[1].page_version + "=a")
            }
            if (entry[1].hostname && !entry[2].hostname.test(href)) {
              params.push(entry[1].hostname + "=prostavive.org")
            }
            if (!params.length) {
              continue
            }
            const glue = href.includes("?")
              ? "&"
              : "?"
            el.setAttribute("href", href + glue + params.join("&"))
          }
        }
      })
    </script>
</body>
</html>
