<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Frutas</h1>
    </header>
    <ul>
    % for fruta in lista:
      <li> {{fruta}} </li>
    % end    
</body>
</html>