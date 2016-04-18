<!DOCTYPE html>
<html lang="es">
<head>
    <link rel="stylesheet" type="text/css" href="/static/css/bluebliss.css" />
<title>Museos</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Museos</h1>
    </header>
    <ul>
        <%
        for museo in museos:
            for info in museo:
                if info.attrib["name"]=="NOMBRE":
        %>
                <li>{{info.text}}</li>
                 % end
                 % if info.attrib["name"]=="DIRECCION":
                 <ul>
                   
        
                <li>{{info.text}}</li>
                 
                 </ul>
                 % end
        % end
        % end
    </ul>
    
</body>
</html>