
      window.__app.visit_id = 10634857
      window.addEventListener("beforeunload", function() {

        var url = ""

        if (document.activeElement) {
          url = document.activeElement.href || ""
          if (!url && document.activeElement.parentElement) {
            url = document.activeElement.parentElement.href || ""
          }
        }

        var path = "/api/exits/10634857?url=" + encodeURIComponent(url)

        var xhr = new XMLHttpRequest
        xhr.open("GET", "//" + location.hostname + path)
        xhr.send()
      })
    