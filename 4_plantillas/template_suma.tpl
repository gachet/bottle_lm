<!DOCTYPE html>
<html lang="es">
<head>
<title>Suma</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Suma {{numero1}}+{{numero2}}</h1>
    </header>
    <%
      suma=int(numero1)+int(numero2)
      if suma>0:
        resultado="positivo"
      else:
        resultado="negativo"
    %>
    <p> La suma es<strong>{{suma}}</strong> el resultado es {{resultado}}</p>
    
</body>
</html>