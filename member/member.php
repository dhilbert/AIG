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
				<h1 class="page-header">학생 관리</h1>
				
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
							<div class="large">4</div>
							<div class="text-muted">총 학생수</div>
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
							<div class="large">1</div>
							<div class="text-muted">요주의</div>
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
							<div class="large">1</div>
							<div class="text-muted">주의</div>
						</div>
					</div>
				</div>
			</div>


			<a href='/AIG/member/member.php?search=5'>
			<div class="col-xs-12 col-md-6 col-lg-3">
				<div class="panel panel-red panel-widget">
					<div class="row no-padding">
						<div class="col-sm-3 col-lg-5 widget-left">
							<svg class="glyph stroked app-window-with-content"><use xlink:href="#stroked-app-window-with-content"></use></svg>
						</div>
						<div class="col-sm-9 col-lg-7 widget-right">
							<div class="large">2</div>
							<div class="text-muted">보통</div>
						</div>
					</div>
				</div>
			</div></a>




		</div><!--/.row-->
		





		 
  

		<div class="row">
			<div class="col-lg-12">
				<div class="panel panel panel-success">
					<div class="panel-heading">학생 관리</div>
					<div class="panel-body">

					※ 여기에 학생 정보
						<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" 
						data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						    <thead>
						    <tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="성명";hd_thead_th($num,$name);$num+=1;
									$name="상태";hd_thead_th($num,$name);$num+=1;
									$name="구분";hd_thead_th($num,$name);$num+=1;
									$name="학년/학기";hd_thead_th($num,$name);$num+=1;
									$name="진행중 수업";hd_thead_th($num,$name);$num+=1;
									$name="상세보기";hd_thead_th($num,$name);$num+=1;
								?>
							
						    </tr>
						    </thead>
							<tbody>
							<?php 
							
									  $total =0;
									  $temps = array(
											array('김선영','초등','보통','5/1','초등_6/2'),
											array('이선영','초등','주의','5/1','초등_2/2'),
											array('지선영','초등','보통','5/1','중등_3/1'),
											array('최선영','초등','요주의','5/1','초등_4/2')



									  );
									  for($i =0 ; $i <count($temps);$i++){
										$temp_want = $temps[$i];
										$total += 1;
										echo "<tr>";
											$name = $total ;hd_tbody_td($num,$name);$num+=1;
											$name = $temp_want[0] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $temp_want[2] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $temp_want[1] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $temp_want[3] ;	hd_tbody_td($num,$name);$num+=1;									
											$name = $temp_want[4] ;	hd_tbody_td($num,$name);$num+=1;									
											$name = "<a href='/AIG/member/detail.php?user_num=".$i."'> 상세보기</a>" ;	hd_tbody_td($num,$name);$num+=1;									
											  
				  
											  
			  
											  
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

