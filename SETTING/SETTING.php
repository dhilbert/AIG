<?php
//include_once('../lib/session.php');
include_once('../lib/dbcon_AIG.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');











?>
			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					

<div class="row">
			<div class="col-lg-12">
				<h1 class="page-header">총 생성 문제</h1>
				
			</div>
		</div><!--/.row-->

<div class="row">
			<div class="col-xs-12 col-md-6 col-lg-3">
				<div class="panel panel-blue panel-widget ">
					<div class="row no-padding">
						<div class="col-sm-3 col-lg-5 widget-left">
							<svg class="glyph stroked bag"><use xlink:href="#stroked-bag"></use></svg>
						</div>
						<div class="col-sm-9 col-lg-7 widget-right">
							<div class="large">6000</div>
							<div class="text-muted">문항 생성중</div>
						</div>
					</div>
				</div>
			</div>
			<div class="col-xs-12 col-md-6 col-lg-3">
				<div class="panel panel-orange panel-widget">
					<div class="row no-padding">
						<div class="col-sm-3 col-lg-5 widget-left">
							<svg class="glyph stroked empty-message"><use xlink:href="#stroked-empty-message"></use></svg>
						</div>
						<div class="col-sm-9 col-lg-7 widget-right">
							<div class="large">5054</div>
							<div class="text-muted">문항 확인 중</div>
						</div>
					</div>
				</div>
			</div>



			<div class="col-xs-12 col-md-6 col-lg-3">
				<div class="panel panel-teal panel-widget">
					<div class="row no-padding">
						<div class="col-sm-3 col-lg-5 widget-left">
							<svg class="glyph stroked male-user"><use xlink:href="#stroked-male-user"></use></svg>
						</div>
						<div class="col-sm-9 col-lg-7 widget-right">
							<div class="large">45.4k</div>
							<div class="text-muted">등록 대기 중</div>
						</div>
					</div>
				</div>
			</div>
			<div class="col-xs-12 col-md-6 col-lg-3">
				<div class="panel panel-red panel-widget">
					<div class="row no-padding">
						<div class="col-sm-3 col-lg-5 widget-left">
							<svg class="glyph stroked app-window-with-content"><use xlink:href="#stroked-app-window-with-content"></use></svg>
						</div>
						<div class="col-sm-9 col-lg-7 widget-right">
							<div class="large">25.2k</div>
							<div class="text-muted">총 생성 문항</div>
						</div>
					</div>
				</div>
			</div>
		</div><!--/.row-->
		





		 
  

		<div class="row">
			<div class="col-lg-12">
				<div class="panel panel panel-success">
					<div class="panel-heading">학년별 문항 수</div>
					<div class="panel-body">

					※ 기능 넣을거, 숫자가 막 증가한다 => LLM으로 생성된 문항 갯수 눈으로 확인하게 한다.
						<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" 
						data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						    <thead>
						    <tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="구분";hd_thead_th($num,$name);$num+=1;
									$name="학년";hd_thead_th($num,$name);$num+=1;
									$name="학기";hd_thead_th($num,$name);$num+=1;
									$name="차시명";hd_thead_th($num,$name);$num+=1;
									
									
									$name="전체 갯수";hd_thead_th($num,$name);$num+=1;									
								?>
							
						    </tr>
						    </thead>
							<tbody>
							<?php 
							
									  $total =0;
									  $sql	 = "
									  SELECT * from grade_unit where GUNO <9000
";
			  
									  $res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
									  while($info	 = mysqli_fetch_array($res)){
										  $total += 1;
										  echo "<tr>";
											  $name = $total ;hd_tbody_td($num,$name);$num+=1;
											  $name = $info['EDU_GUBN'] ;	hd_tbody_td($num,$name);$num+=1;
											  $name = $info['SCHOOL_YEAR'] ;	hd_tbody_td($num,$name);$num+=1;
											  $name = $info['SEMESTER'] ;	hd_tbody_td($num,$name);$num+=1;
											  $name = $info['UNIT_VALUE'] ;	hd_tbody_td($num,$name);$num+=1;
											  
											  $temp = rand(300,9000)											;
											  $name = $temp ;	hd_tbody_td($num,$name);$num+=1;											
											  
				  
											  
			  
											  
										  echo "</tr>";
									  }
								  
							
								
								?>
						</tbody>

						</table>
					</div>
				</div>
			</div>
		</div><!--/.row-->	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>

