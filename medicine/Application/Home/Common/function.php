<?php

/*
判断form是否已经填写完整
 */
function filled_form($array)
{
	if(is_array($array))
	{
		foreach($array as $key => $value)
		{
			if( !isset($key) || $value=='' )
				return false;
		}
		return true;
	}
	else{
		throw new Exception('要判断的变量不是一个数组.');
	}
}

/*
构建date_list显示在select组件中，供用户选择
 */
function getDate_list()
{
	$date_list=array();
	$weekarray=array("日","一","二","三","四","五","六");
	$now=time();
	$this_week_usable=false;
	//添加本周日期,今天只能预定明天之后的
	$from=strtotime(date("Y-m-d",$now));
	$from=strtotime('+1 day',$from);
	$to=strtotime('next week Monday');
	$i=0;
	while($from<$to)
	{
		if(date('w',$from)!=0) //zlz：判断明天是不是星期天，如果星期天不能预约，且明天是星期天，这一周就都不能定了
		{
			$this_week_usable=true;
			$date_list[$i]=array();
			$date_list[$i]['date']=date('Y-m-d',$from);
			$date_list[$i]['week']="星期".$weekarray[date("w",$from)];
			$i++;
		}else if(C('IS_SUNDAY_AVAILABLE')==true)//如果星期天可以预约，就显示在列表中 zlz：C()获取和设置配置参数 支持批量定义
		{
			$this_week_usable=true;
			$date_list[$i]=array();
			$date_list[$i]['date']=date('Y-m-d',$from);
			$date_list[$i]['week']="星期".$weekarray[date("w",$from)];
			$i++;
		}
		$from=strtotime('+1 day',$from);
	}
	
	//添加下周日期
	$start_time=getStartTime();  //返回每周开始预定的时间戳
	if($now>=$start_time)   //zlz：如果现在是本周五下午17:00之后，则可以开始预约下周
	{
		//如果本周还有数据就在本周和下周之间插入空行
		if($this_week_usable==true)
		{
			$date_list[$i]=array();
			$date_list[$i]['date']="";
			$date_list[$i]['week']="";
		}
		//合并本周与下周的日期
		$date_list=array_merge($date_list,getNextWeekDate());
	}
	return $date_list;
}
/*
返回每周开始预定的时间戳
 */
function getStartTime()
{
	$weekdayArray=array('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
	//获取本周五日期
	$publish_day = strtotime($weekdayArray[intval(C('PUBLISH_DAY'))].' this week');
	//在周五17:00开始下周的预约
	$start_time=strtotime('+'.C('PUBLISH_TIME').' hours',$publish_day);
	return $start_time;
}
/*
获取下周一到周六的日期列表
 */

function getNextWeekDate()
{
	$weekarray=array("日","一","二","三","四","五","六");
	$date_list=array();
	$from=strtotime("next Monday");
	$to=strtotime("+7 day",$from);
	
	$i=0;
	while($from<$to)
	{
		//如果周日不可预约就退出循环
		if(date("w",$from)==0 && C('IS_SUNDAY_AVAILABLE')==false)
		{
			break;
		}
		$date_list[$i]=array();
		$date_list[$i]['date']=date('Y-m-d',$from);
		$date_list[$i]['week']="星期".$weekarray[date("w",$from)];
		$from=strtotime('+1 day',$from);
		$i++;
	}
	return $date_list;
}
/*
根据Y-m-d格式的日期返回星期几
 */
function getWeek($date)
{
	$weekarray=array("日","一","二","三","四","五","六");
	return "星期".$weekarray[date("w",strtotime($date))];
}
/*
根据用户名查找用户的真实姓名
 */
function getRealName($username)
{
	$user_table=M('user');
	$condition['username']=$username;
	return $user_table->where($condition)->getField('realname');
}
?>