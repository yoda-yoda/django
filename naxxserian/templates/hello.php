<html>
<head>
	<title>Hello {{name}}</title>
</head>
<body>
		<h3>Hello {{name}}, This one for templates works as well :)</h3>
		<div id="response"></div>

<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript">
	var data = [];
	var response = $("#response");
	var food = ["rice", "ugali", "mukimo"];
	var i = 0;
	//response.innerHTML = food;
	data.push(food);
	
	response.html(data);
</script>

</body>
</html>