<?php
//include_once('../lib/session.php');
include_once('../lib/dbcon_AIG.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');

$user_num = isset($_GET['user_num']) ? $_GET['user_num'] : 3;

$temps = array(
	array('김선영','초등','보통','5/1','초등_6/2'),
	array('이선영','초등','주의','5/1','초등_2/2'),
	array('지선영','초등','보통','5/1','중등_3/1'),
	array('최선영','초등','요주의','5/1','초등_4/2')



);








?>
		<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					

		<div class="row">
			<div class="col-lg-12">
				<h1 class="page-header"><?php echo $temps[$user_num ][0]?> 학습 이력</h1>
				
			</div>
		</div><!--/.row-->



	

		<div class="row">
			<div class="col-lg-12">
			<div class="panel panel-default">
					<div class="panel-heading">
					<?php echo $temps[$user_num ][0]?> 의 현재 진행 로드맵
					</div>
					<div class="panel-body">
			※ 이런식으로 로드맵


			<div id="sankey_multiple" style="width: 900px; height: 300px;"></div>
			</div>
			</div><!--/.row-->
			</div><!--/.row-->
 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>



<script type="text/javascript">
  google.charts.load("current", {packages:["sankey"]});
  google.charts.setOnLoadCallback(drawChart);
   function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'From');
    data.addColumn('string', 'To');
    data.addColumn('number', 'Weight');
    data.addRows([
		[ '세자리 수 개념', '받아 올림 없는 두 자리 수의 덧셈', 3 ],		
		[ '세자리 수 개념', '받아 내림 없는 두 자리 수의 뺄셈', 3 ],

		[ '받아 올림 없는 두 자리 수의 덧셈','받아 올림이 없는 세자리수의 덧셈', 1 ],
		[ '받아 올림 없는 두 자리 수의 덧셈','받아 올림 없는 세 자리 수의 덧셈', 2 ],
		
		[ '받아 내림 없는 두 자리 수의 뺄셈','받아 올림 없는 세 자리 수의 덧셈',  1 ],


		


		
       
    ]);

    // Set chart options
	var options = {
	  width: '100%',
      height: '100%',
      sankey: {
        node: { colors: [ '#a61d4c' ] },
        link: { color: { stroke: 'black', strokeWidth: 0 } },
      }
    };

	

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.Sankey(document.getElementById('sankey_multiple'));
    chart.draw(data, options);
   }
</script>





</div><!--/.row-->



			<div class="row">
				<div class="col-lg-12">
					<div class="panel panel-default">
						<div class="panel-heading">
							<?php echo $temps[$user_num ][0]?> 의 학습 결과
						</div>
						<div class="panel-body">

						</div>
					</div><!--/.row-->
				</div><!--/.row-->
			</div><!--/.row-->

<!--Modal-->
<?php include_once('../contents_footer.php');


?>

