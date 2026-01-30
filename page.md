<p> If you want a landing page that has documented the projects work flow and has project explanation 
 copy the code below and paste it in templates/page.html then render it in @app.route("/") 
 return render_template (page.html) </p>

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management API Documentation</title>
    <style>
        :root {
            --bg-color: #f0f4f8;
            --primary: #6366f1;
            --text-main: #1f2937;
            --text-light: #6b7280;
            --clay-shadow: 
                8px 8px 16px 0 rgba(118, 134, 165, 0.2), 
                -8px -8px 16px 0 rgba(255, 255, 255, 0.8), 
                inset 2px 2px 4px 0 rgba(255, 255, 255, 0.5);
            --clay-card-bg: #f0f4f8;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
            min-height: 100vh;
        }

        .container {
            max-width: 900px;
            width: 100%;
        }

        /* Claymorphism Header */
        .header {
            background: var(--clay-card-bg);
            border-radius: 30px;
            padding: 40px;
            box-shadow: var(--clay-shadow);
            margin-bottom: 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s ease;
        }

        .header:hover {
            transform: translateY(-5px);
        }

        h1 { margin: 0; font-size: 2.5rem; color: var(--primary); }
        .subtitle { color: var(--text-light); margin-top: 10px; font-size: 1.1rem; }
        .badge {
            display: inline-block;
            background: #d1fae5;
            color: #065f46;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
            margin-top: 15px;
            box-shadow: inset 2px 2px 5px rgba(0,0,0,0.05);
        }

        /* Navigation Tabs */
        .tabs {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .tab-btn {
            background: var(--clay-card-bg);
            border: none;
            padding: 15px 30px;
            border-radius: 20px;
            box-shadow: var(--clay-shadow);
            color: var(--text-light);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .tab-btn:hover { color: var(--primary); transform: translateY(-2px); }
        
        .tab-btn.active {
            color: var(--primary);
            box-shadow: inset 5px 5px 10px rgba(163, 177, 198, 0.3), 
                        inset -5px -5px 10px rgba(255, 255, 255, 0.8);
        }

        /* Content Sections */
        .content-card {
            background: var(--clay-card-bg);
            border-radius: 30px;
            padding: 40px;
            box-shadow: var(--clay-shadow);
            display: none; /* Hidden by default */
            animation: fadeIn 0.5s ease;
        }

        .content-card.active-content {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 { color: var(--primary); border-bottom: 2px solid #e5e7eb; padding-bottom: 10px; }
        p, li { line-height: 1.7; color: #4b5563; }
        
        /* Tech Stack Grid */
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .tech-item {
            background: rgba(255,255,255,0.5);
            padding: 15px;
            border-radius: 15px;
            border-left: 5px solid var(--primary);
        }

        /* Code Blocks */
        pre {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            border-radius: 15px;
            overflow-x: auto;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        }
        code { font-family: 'Consolas', monospace; }

        /* Tables */
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th { text-align: left; padding: 15px; color: var(--primary); border-bottom: 2px solid #e5e7eb; }
        td { padding: 15px; border-bottom: 1px solid #e5e7eb; }
        .method { font-weight: bold; }
        .GET { color: #059669; }
        .POST { color: #2563eb; }
        .PATCH { color: #d97706; }
        .DELETE { color: #dc2626; }

    </style>
</head>
<body>

    <div class="container">
        
        <div class="header">
            <h1>User Management API</h1>
            <div class="subtitle">A Robust RESTful Backend built with Flask</div>
            <div class="badge">🟢 System Online</div>
        </div>

        <div class="tabs">
            <button class="tab-btn active" onclick="openTab(event, 'tech')">Architecture</button>
            <button class="tab-btn" onclick="openTab(event, 'endpoints')">API Endpoints</button>
            <button class="tab-btn" onclick="openTab(event, 'local')">Run Locally</button>
        </div>

        <div id="tech" class="content-card active-content">
            <h2>🧱 Architecture & Tech Stack</h2>
            <p>This project demonstrates a scalable REST API structure, moving away from monolithic scripts to a modular "Real World" architecture.</p>
            
            <div class="grid-2">
                <div class="tech-item">
                    <strong>⚡ Core Framework</strong><br>
                    Flask + Flask-RESTful (Class-Based Views)
                </div>
                <div class="tech-item">
                    <strong>🗄️ Database</strong><br>
                    SQLite + SQLAlchemy ORM
                </div>
                <div class="tech-item">
                    <strong>🛠️ Tools</strong><br>
                    VS Code + Thunder Client
                </div>
                <div class="tech-item">
                    <strong>🔐 Validation</strong><br>
                    ReqParser (Input) + Marshal (Output)
                </div>
            </div>

            <h3>Why these Imports?</h3>
            <ul>
                <li><strong>Api (flask_restful):</strong> Automatically routes URLs to our classes.</li>
                <li><strong>Resource:</strong> The parent class that maps HTTP verbs (GET, POST) to Python methods.</li>
                <li><strong>marshal_with:</strong> The "Filter" that ensures we only send safe JSON data back (hiding private DB fields).</li>
            </ul>
        </div>

        <div id="endpoints" class="content-card">
            <h2>📡 API Endpoints</h2>
            <p>Use <strong>Thunder Client</strong> to test these routes.</p>
            
            <table>
                <thead>
                    <tr>
                        <th>Method</th>
                        <th>Endpoint</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="method GET">GET</td>
                        <td>/api/users/</td>
                        <td>Fetch all registered users.</td>
                    </tr>
                    <tr>
                        <td class="method POST">POST</td>
                        <td>/api/users/</td>
                        <td>Register a new user.<br><small>Requires: <code>{"name": "...", "email": "..."}</code></small></td>
                    </tr>
                    <tr>
                        <td class="method GET">GET</td>
                        <td>/api/users/&lt;id&gt;</td>
                        <td>Get details of a specific user.</td>
                    </tr>
                    <tr>
                        <td class="method PATCH">PATCH</td>
                        <td>/api/users/&lt;id&gt;</td>
                        <td>Update user details (Partial update).</td>
                    </tr>
                    <tr>
                        <td class="method DELETE">DELETE</td>
                        <td>/api/users/&lt;id&gt;</td>
                        <td>Remove a user permanently.</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div id="local" class="content-card">
            <h2>💻 Run This Locally</h2>
            <p>Follow these steps to deploy the API on your machine.</p>

            <h3>1. Setup Environment</h3>
            <pre><code># Install Dependencies
pip install flask flask-restful flask-sqlalchemy</code></pre>

            <h3>2. Initialize Database</h3>
            <p>The application automatically detects if <code>database.db</code> is missing and creates it using <code>db.create_all()</code> on the first run.</p>

            <h3>3. Run Server</h3>
            <pre><code>python app.py</code></pre>
            <p>The API will launch at <code>http://127.0.0.1:5000/</code>.</p>
        </div>

    </div>

    <script>
        function openTab(evt, tabName) {
            // 1. Hide all content cards
            var i, content, tablinks;
            content = document.getElementsByClassName("content-card");
            for (i = 0; i < content.length; i++) {
                content[i].classList.remove("active-content");
            }

            // 2. Remove "active" class from all buttons
            tablinks = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].classList.remove("active");
            }

            // 3. Show the current tab, and add an "active" class to the button that opened the tab
            document.getElementById(tabName).classList.add("active-content");
            evt.currentTarget.classList.add("active");
        }
    </script>
</body>
</html>
```
