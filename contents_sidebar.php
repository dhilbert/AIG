<?php
function hd_active($input){
	$uri=explode('?',$_SERVER['REQUEST_URI']);
	$uri=$uri[0];


	$uri=explode('/',$uri);
	$temp = count($uri)-1;



		
		if($uri[$temp]==$input){
			echo "class='active'";
		}
	
}


function hd_drop($num,$grobal,$sub_name,$sub_url){
?>

<li class="parent ">
		<a href="#">
		<span data-toggle="collapse" href="#sub-item-<?php echo $num;?>"><svg class="glyph stroked chevron-down"><use xlink:href="#stroked-chevron-down"></use></svg> <?php echo $grobal?> </span>
		</a>
		<ul class="children collapse" id="sub-item-<?php echo $num;?>">
		<?php
		for($i = 0 ; $i <count($sub_name);$i++){
		?>
			<li>
				<a class="" href="<?php echo $sub_url[$i];?>">
					<svg class="glyph stroked chevron-right"><use xlink:href="#stroked-chevron-right"></use></svg> <?php echo $sub_name[$i];?>
				</a>
			</li>
		<?php
		}?>
		</ul>
	</li>
<?php
}
?>


	<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
		<form role="search">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search">
				
			</div>

		</form>

		<ul class="nav menu" >
		<li <?php hd_active("home.php");?>><a href="/AIG/home.php"><svg class="glyph stroked home"><use xlink:href="#stroked-home"/></svg>Home</a></li>
		
		
		<?php
			
			$num		='hq-01';
			$grobal		= '학생 관리';
			$sub_name	= array('반 생성');
			$sub_url	= array(
							""
							
			 					);
			
			
			
			//hd_drop($num,$grobal,$sub_name,$sub_url);

			
		


		?>		
		<li <?php hd_active("member.php");?>><a href="/AIG/member/member.php"><svg class="glyph stroked clipboard with paper"><use xlink:href="#stroked-clipboard-with-paper"/></svg></svg>학생 분석</a></li>
		<li <?php hd_active("SETTING.php");?>><a href="/AIG/SETTING/SETTING.php"><svg class="glyph stroked dashboard dial"><use xlink:href="#stroked-dashboard-dial"/></svg></svg>문항갯수</a></li>
		
		
	


	</ul>
</div>