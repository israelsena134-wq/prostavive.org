<!DOCTYPE html>
<html>
<head>
  <title>disclaimer</title>
        <meta property="og:url" name="url" content="8f9543aa441b7e12_disclaimer.php">      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
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
              + "/api/visits?page_id=9&page_version=a&request_id=6817D529%3A4429_C0A85015%3A01BB_6A0695D2_112C61%3A21D7A0"
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
                page_id: page_id || 9,
                page_version: page_id
                  ? undefined
                  : "a" || undefined,
                referrer: document.referrer,
                request_id: "6817D529:4429_C0A85015:01BB_6A0695D2_112C61:21D7A0" || undefined,
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

  
    <!-- Page conternt Start -->
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
</section>    <section class="main-sec">
        <div class="container">
          <div class="des-box-other">
            <div class="row">
              <div class="col-md-12">
                <h2>Disclaimer</h2>
                <p>By using the prostavive.org guide or website, you agree to all terms of the undertaking, assuming full responsibility for your own actions. Authors and publishers will not be held for any loss or injury. Use these resources at your own risk.</p>
                <p>All products of prostavive.org and its related companies are strictly for informational purposes only. While all attempts have been made to verify the accuracy of the information provided on our website and in the publications, neither the authors nor the publishers are responsible for any inaccuracies.</p>
                <p>Authors and publishers are not responsible for the inaccuracy of the content, including but not limited to, errors or omissions. Loss of property, personal injury or otherwise, and even death may occur as a direct or indirect consequence of the use and application of any content therein.</p>
                <p>All information on prostavive.org is for adults over the age of 18 only.</p>
                <p>By choosing to use the information made available by prostavive.org or in one of our publications, you agree to indemnify, defend and exonerate authors, publishers and other affiliated companies from any and all claims, judgments, lawsuits, proceedings, losses, damages, and costs or expenses of any nature whatsoever resulting from the use or misuse of any information provided.</p>
                <p>The contents of this site are not intended to be a substitute for professional medical advice, diagnosis, or treatment. 
                    Always seek the advice of your physician or other qualified health provider regarding a medical condition, suspected medical condition, and before starting any diet, exercise or supplementation program, or before taking or stopping any medication. Reliance on any information provided by this site and others appearing on the site is solely at your own risk.</p>
                <p>The information provided may be downloaded using third-party software, such as Acrobat or Flash Player. It is the responsibility of the user to install the necessary software to display this information. Downloads, whether purchased or given for free through this website, linked websites, or hosting systems, are at the user's own risk. No warranty covers that websites are free to corrupt computer codes with viruses or worms.</p>
                <p>If you are a minor, you may use this service only with the permission and guidance of your parents or guardians. Children are not allowed to use our services without supervision. In addition, prostavive.org expressly denies access to anyone covered by the 1998 Children's Online Privacy Act (COPA).</p>
                <p>The content of the website and the proceeds of the sale are based on the opinion of the author and are provided solely on an "as is" and "AS AVAILABLE" basis. You must do your own research and confirm the information with other sources. <!--You shall not construe ClickBank's sale of this product as an endorsement by ClickBank of the opinions expressed, or any warranty of any strategy, recommendation, action, or application of advice made by the product's author.--></p>
                <p>This exclusion was last updated on 01/08/2024.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

<script src="/js/jquery.js"></script>
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
<script src="https://display.buygoods.com/v1/disclaimer?id=disclaimer&account_id=8198"></script>        
        <link href="https://fonts.googleapis.com/css2?family=Lato:wght@700&amp;display=swap" rel="stylesheet" />
        
    <!-- Page Content End --><!-- ClickBank Trust Badge -->


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
              params.push(entry[1].page_id + "=9")
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
