<?php

/*
利用正则表达式判断邮箱格式是否正确
 */
function valid_email($email)
{
    if (preg_match('/^([0-9A-Za-z\\-_\\.]+)@([0-9a-z]+\\.[a-z]{2,3}(\\.[a-z]{2})?)$/i', $email)) {
        return true;
    }
    return false;
}
function valid_phone($phone)
{
    if (preg_match('/^\d{7,11}$/', $phone)) {
        return true;
    }
    return false;
}
function valid_realname($realname)
{
    if(empty($realname) || !preg_match("/^\p{Han}+$/u", $realname))
    {
        return false;
    }
    return true;
}
function valid_username($username)
{
    if(preg_match('/^[a-zA-Z\d_]{3,50}$/i', $username))
    {
        return true;
    }
    return false;
}
function valid_passwd($passwd)
{
    if(empty($passwd))
    {
        return false;
    }
    return true;
}
/*
alert
 */
function alert($type, $content)
{
    echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>';
    echo "<script language='javascript'>alert('$type: $content');history.back();</script>";
}
/*
back and refresh
 */
function returnAndRefresh()
{
    echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>';
    echo "<script language='javascript'>history.go(-2);window.location.reload(true);</script>";
}
/*
 * @param $m 模型，引用传递
 * @param $where 查询条件
 * @param int $pagesize 每页查询条数
 * @return \Think\Page
 */
function getpage(&$m,$where,$pagesize=20){
    $m1=clone $m;//浅复制一个模型
    $count = $m->where($where)->count();//连惯操作后会对join等操作进行重置
    $m=$m1;//为保持在为定的连惯操作，浅复制一个模型
    $p=new Think\Page($count,$pagesize);
    $p->rollPage=10;
    $p->lastSuffix=false;//如果为true那么末页不起作用，显示的是最后一页的页码 
    $p->setConfig('header','<li class="rows">共<b>%TOTAL_ROW%</b>条记录，第<b>%NOW_PAGE%</b>页/共<b>%TOTAL_PAGE%</b>页</li>');
    $p->setConfig('prev','上一页');
    $p->setConfig('next','下一页');
    $p->setConfig('first','首页');
    $p->setConfig('last','末页');
    $p->setConfig('theme','%FIRST% %UP_PAGE% %LINK_PAGE% %DOWN_PAGE% %END% %HEADER%');
    $m->limit($p->firstRow,$p->listRows);
    return $p;
}
/*
读取config.php返回一个数组
 */
function getConfig()
{
    $config = require(COMMON_CONFIG_PATH.'/config.php');
    return $config;
}
/*
更新配置
 */
function update_config($ini, $value){
    $file=COMMON_CONFIG_PATH.'/config.php';
    $str = file_get_contents($file);
    $str2="";
    $str2 = preg_replace("/'".preg_quote($ini)."'(\s+)=>(\s+)(.*),/", "'".$ini."'"." => ".$value." ,", $str);
    if(file_put_contents($file, $str2)>0)
        return true;
    return false;
}
/*
清空缓存，使得配置生效
 */
function clearCache()
{
    $cachedir=RUNTIME_PATH.'/Cache/';//Cache文件的路径;
    return deldir($cachedir);
}   
  /*
  删除文件夹
   */
  function deldir($dir) {
//先删除目录下的文件： 
    $dh=opendir($dir); 
    while ($file=readdir($dh)) {
        if($file!="." && $file!="..") { 
            $fullpath=$dir."/".$file; 
            if(!is_dir($fullpath)) { 
                unlink($fullpath); 
            } else { 
                deldir($fullpath); 
            } 
        } 
    } 
    closedir($dh); 
    //删除当前文件夹： 
    if(rmdir($dir)) { 
        return true; 
    } else { 
        return false; 
    } 
}
?>