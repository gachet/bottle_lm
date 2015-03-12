% include('header.tpl')
	<form action="calcular" method="post">
            Numero 1: <input name="num1" type="text" /><br/>
            Numero 2: <input name="num2" type="text" /><br/>
            Operación:
            <select name="op">
            	<option value="Sumar">Sumar</option>
            	<option value="Restar">Restar</option>
            	<option value="Multiplicar">Multiplicar</option>
            	<option value="Dividir">Dividir</option>
            </select>

            <input value="Calcular" type="submit" />
     </form>
% include('footer.tpl')