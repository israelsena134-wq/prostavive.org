import os

file_path = r'c:\Users\Guga\Downloads\prostavive.org\index.html'

flow_track_script = """<!-- Flow Tracking: Prostavive -->
<script src="https://flow-tracking-cdn-production.up.railway.app/v2/loader.js"
        data-track="87607e14-8d9f-4ddb-8522-cc35bf6246d7"
        data-endpoint="https://api.flowtrackingtool.com/"
        data-cdn-base="https://flow-tracking-cdn-production.up.railway.app/"
        data-api-base="https://api.flowtrackingtool.com/"
        data-token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja0lkIjoiODc2MDdlMTQtOGQ5Zi00ZGRiLTg1MjItY2MzNWJmNjI0NmQ3IiwiYXVkIjoiZmxvd3RyazplbWJlZCIsImlzcyI6ImZsb3d0cmsiLCJraWQiOiI5NjZlMmZjNDM5NGU1ZGJjIiwiaWF0IjoxNzc4ODIzNzA3LCJleHAiOjE4MTAzNTk3MDd9.PFx4niI5hXVe3zGoNPwrMdE5Plwn2Q8yl3WuEH5hM2s"
        async crossorigin="anonymous"></script>"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix residual corruption if any
content = content.replace('index.html* offline: ensure content is visible regardless of JS init state *index.html', '/* offline: ensure content is visible regardless of JS init state */')

# Add the script before </head>
if '</head>' in content:
    content = content.replace('</head>', flow_track_script + '\n</head>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("FlowTrack script added and corruption fixed.")
