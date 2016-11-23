<?php
namespace Home\Controller;
use Think\Controller;
header("Content-type:text/html;charset=utf-8");
set_time_limit(0);//0表示不限时

class IndexController extends Controller {
    public function index()
    {
        $this->display();
    }

    public function symptom()
    {
//        $symptom_list=array();
//        $disease_list=array();
//
//        $query=M('zhanglizhu');
//        $disease_list=$query->distinct(true)->field('disease,department')->select();
//        $symptom_list=$query->distinct(true)->field('symptom')->select();
//        $disease_symptom_relation=$query->field('disease,symptom,probability')->select();
//        //var_dump($disease_list);
//
//        $insert_disease=M('disease');
//        $probability=round(1/(count($disease_list)),3);
//        //var_dump($probability);
//        foreach($disease_list as $disease)
//        {
//            $data['title'] = $disease['disease'];
//            $data['department'] = $disease['department'];
//            $data['probability'] = $probability;
//            $panduan=$insert_disease->add($data);
//            if($panduan)
//                echo "ok";
//        }

//        $insert_symptom=M('symptom');
//        foreach($symptom_list as $symptom)
//        {
//            $data['title'] = $symptom['symptom'];
//            $panduan=$insert_symptom->add($data);
//            if($panduan)
//                echo "ok";
//        }


//        $insert_relation=M('disease_symptom');
//        foreach($disease_symptom_relation as $relation)
//        {
//            $query_disease=M('disease');
//            $disease_id=$query_disease->where('title ="' . $relation['disease'] . '"')->field('id')->select();
//            //var_dump($disease_id);
//
//            $query_stmptom=M('symptom');
//            $symptom_id=$query_stmptom->where('title ="'.$relation['symptom']. '"')->field('id')->select();
//           // var_dump($stmptom_id);
//
//            $data['id_disease'] = $disease_id[0]['id'];
//            $data['id_symptom'] = $symptom_id[0]['id'];
//            $data['probability'] = $relation['probability'];
//            var_dump($data);
//
//            $panduan=$insert_relation->add($data);
//            if($panduan)
//                echo "ok";
//        }


        /*//var_dump(post.symptom);
       $symptom_tmp = I('post.symptom');
       $symptom_z=explode(" ",$symptom_tmp);
       //var_dump($symptom_z);*/


        //zlz：第二次改数据库
//        $disease_set=array();
//        $query_combine1=M('disease');
//        $disease_set=$query_combine1->field('id,title')->select();
//        var_dump($disease_set);
//
//        $disease_both_set=array();
//        $query_combine2=M('neike');
//        foreach($disease_set as $disease_set_item)
//        {
//            $disease_both_set_temp=$query_combine2->where('title ="'.$disease_set_item['title']. '"')->field('id,title')->select();
//            if($disease_both_set_temp)
//            {
//                $disease_both_set_temp[0]['id_disease']=$disease_set_item['id'];
//                array_push($disease_both_set,$disease_both_set_temp);
//            }
//        }
//        var_dump($disease_both_set);
//
//        //zlz：id是一步步传下去的。只需查一次张强数据库的疾病ID，就能一直传下去，并写入相应的数据库
//        $disease_symptom_from_neike_result=array();
//        $query_combine3=M('disease_symptom_from_neike');
//        $count_temp=0;
//        foreach($disease_both_set as $disease_both_set_item)
//        {
////            var_dump($disease_both_set_item);
//            $disease_symptom_from_neike_temp=$query_combine3->where('id_disease ="'.$disease_both_set_item[0]['id']. '"')->field('id_symptom')->select();
//            if($disease_symptom_from_neike_temp)
//            {
//                $count_temp=$count_temp+1;
//                foreach ($disease_symptom_from_neike_temp as $disease_symptom_from_neike_temp_item)
//                {
//                    $disease_symptom_from_neike_temp_item['id_disease']=$disease_both_set_item[0]['id_disease'];
//                    array_push($disease_symptom_from_neike_result,$disease_symptom_from_neike_temp_item);
//                }
//            }
//        }
//        var_dump($disease_symptom_from_neike_result);
//        var_dump($count_temp);
//
//        //zlz：好像也没多少新数据，108条病在温德斯的大数据库中只有56条能查着，但是这些病，在大数据库中这56个疾病交集只有6条具有症状描述，所有这6个有症状描述的疾病的症状综合加起来只有30个症状，可能还包含重复的。
//        //zlz：先查一下这些症状哪些是大数据库中独有的，可以作为补充添加进来的
//        $symptom_new=array();
//        $symptom_set_new=array();
//        $query_combine4=M('symptom_from_neike');
//        foreach($disease_symptom_from_neike_result as $disease_symptom_from_neike_result_item)
//        {
//            $symptom_new_temp=$query_combine4->where('id ="'.$disease_symptom_from_neike_result_item['id_symptom']. '"')->field('title')->select();
//            if($symptom_new_temp)
//            {
//                $symptom_new_temp[0]['id_disease']=$disease_symptom_from_neike_result_item['id_disease'];
//                array_push($symptom_new,$symptom_new_temp);
//                array_push($symptom_set_new,$symptom_new_temp[0]['title']);
//            }
//        }
//        var_dump($symptom_new);
//        var_dump($symptom_set_new);
//        $symptom_set_new=array_unique($symptom_set_new);
//        var_dump($symptom_set_new);
//
//        //zlz：好吧，去重后，温德斯的大数据库中和强哥数据库中所有疾病相关的不同症状有14条。。。。再查一下，这14条是否否出现在强哥的数据库
////        $query_combine5=M('symptom');
////        foreach ($symptom_set_new as $symptom_set_new_item)
////        {
////            $symptom_set_new_temp=$query_combine5->where('title ="'.$symptom_set_new_item. '"')->field('id,title')->select();
////            if($symptom_set_new_temp==null)
////            {
////                $data['title']=$symptom_set_new_item;
////                $data['source']=1;  //zlz：把强哥数据库中没有的症状加到原来的symptom表中，注明source是1 ，即来自温德斯的数据库
////                $query_combine5->add($data);
////            }
////        }
//
//        //zlz：symptom表已经把数据加进去了，现在需要改写下上面那一段了。
//        $query_combine5=M('symptom');
//        foreach ($symptom_new as &$symptom_new_item)
//        {
//            $symptom_new_temp=$query_combine5->where('title ="'.$symptom_new_item[0]['title']. '"')->field('id')->select();
////            var_dump($symptom_new_temp);
//            if($symptom_new_temp)
//            {
//                $symptom_new_item[0]['id_symptom']=$symptom_new_temp[0]['id'];
//            }
//        }
//        var_dump($symptom_new);
//
//        //zlz：先把温德斯的这些数据都加进去
//        $query_combine6=M('disease_symptom_both');
////        foreach($symptom_new as $symptom_new_item1)
////        {
////            $data['id_disease']=$symptom_new_item1[0]['id_disease'];
////            $data['id_symptom']=$symptom_new_item1[0]['id_symptom'];
////            $query_combine6->add($data);
////        }
//        //zlz：已经把数据插进去了，然后呢，group疾病ID，计算每条疾病对应的症状个数，作为0.2的概率均分的基础
////        $unique_disease_symptom_new=$query_combine6->group('id_disease')->field('id_disease,count(id_symptom)')->select();
////        var_dump($unique_disease_symptom_new);
////
////        foreach ($unique_disease_symptom_new as $unique_disease_symptom_new_item)
////        {
////            $unique_disease_symptom_new_tmp=$query_combine6->where('id_disease ="'.$unique_disease_symptom_new_item['id_disease']. '"')->select();
////            $query_combine6->where('id_disease ="'.$unique_disease_symptom_new_item['id_disease']. '"')->delete();
////            foreach($unique_disease_symptom_new_tmp as $unique_disease_symptom_new_tmp_item)
////            {
////                $unique_disease_symptom_new_tmp_item['probability']=0.2/(double)$unique_disease_symptom_new_item['count(id_symptom)'];
////                $unique_disease_symptom_new_tmp_item['source']=1;
////                $query_combine6->add($unique_disease_symptom_new_tmp_item);
////            }
////        }
//        //zlz：好了，新的数据都加进去了，现在把旧数据加进去。旧数据概率变为原来的0.8
//        $query_combine7=M('disease_symptom');
//        $disease_symptom_old_set=$query_combine7->select();
////        var_dump($disease_symptom_old_set);
//        foreach($disease_symptom_old_set as $disease_symptom_old_set_item)
//        {
//            $disease_symptom_old_set_item['probability']=$disease_symptom_old_set_item['probability']*0.8;
//            $disease_symptom_old_set_item['source']=0;
//            $query_combine6->add($disease_symptom_old_set_item);
//        }

        //$query_combine8=M('disease_symptom_both');
//        $query_combine9=M('disease_symptom_apply');
////        $disease_symptom_apply_change_set
//        $disease_symptom_old_set=$query_combine9->group('id_disease,id_symptom')->field('id_disease,id_symptom,count(*),sum(probability)')->select();
//        foreach ($disease_symptom_old_set as $disease_symptom_old_set_item)
//        {
//            if($disease_symptom_old_set_item["count(*)"]>1)
//            {
////                var_dump($disease_symptom_old_set_item);
//                $query_combine9->where('id_disease ="'.$disease_symptom_old_set_item['id_disease'].'" AND id_symptom="'.$disease_symptom_old_set_item['id_symptom']. '"')->delete();
//                $data['id_disease']=$disease_symptom_old_set_item['id_disease'];
//                $data['id_symptom']=$disease_symptom_old_set_item['id_symptom'];
//                $data['probability']=$disease_symptom_old_set_item['sum(probability)'];
//                $data['source']=$disease_symptom_old_set_item['count(*)'];
//                $query_combine9->add($data);
//            }
//        }


        $symptom_temp = I('post.symptom');

        if($symptom_temp==null)
        {
            alert("输入无效");
        }
        //var_dump($symptom_temp);
        //zlz：先不调用Python了
        $this->symptom_input=$symptom_temp;
        $fenci=array();
        $symptom_z=array();

        if(I('post.panduan')=='1')
        {
 //zlz：先把保持不变的传过来
            $this->symptom_input=I('post.symptom_input');
            $this->fenci_result=I('post.fenci_result');
            $this->match_result=I('post.match_result');
            $this->symptom_match=I('post.symptom_match');
            $symptom_old=I('post.symptom_old');
//            var_dump($symptom_old);

            $second_symptom_array= I('post.second_symptom');
//            var_dump($second_symptom_array);
            $symptom_input_qianduan=I('post.symptom_input_qianduan');
            //将更多症状加入到确定症状中
//            $symptom_temp_second = $symptom_input_qianduan.' '.$second_symptom;
//            $symptom_z=explode(' ',$symptom_temp_second);
            foreach($second_symptom_array as $second_symptom_array_item)
            {
                array_push($symptom_old,$second_symptom_array_item);
            }
            $symptom_z=$symptom_old;
//            var_dump($symptom_z);
            $this->symptom_old=$symptom_old;
        }
        else
        {
//            var_dump($symptom_temp);
            $ssc_begin=date('y-m-d h:i:s',time());
            //zlz：解决php向python传参数乱码的问题
            $symptom_temp = mb_convert_encoding($symptom_temp, "UTF-8","ISO-8859-1");
            exec('C:\Python27\python C:\wamp\www\medicine\Application\Home\Controller\Word2Vec\usingWikiAlias.py '.$symptom_temp,$fenci);
//            var_dump($fenci);

            $fenci_result=array();
//            $this->fenci_result=$fenci;
            foreach($fenci as $word)
            {
                $tmp_word=explode(':',$word);
                array_push($fenci_result,trim($tmp_word[0]));
                $temp_symptom=explode(' ',$tmp_word[1]);
                foreach($temp_symptom as $temp_symptom_item)
                {
                    if($temp_symptom_item)
                        array_push($symptom_z,$temp_symptom_item);
                }
            }
//            var_dump($fenci_result);
//            var_dump($symptom_z);


            $ssc_end=date('y-m-d h:i:s',time());
            $this->ssc_begin=$ssc_begin;
            $this->ssc_end=$ssc_end;


            //zlz：暂时的，等司尚春的分词结果
//            $symptom_z=explode(' ',$symptom_temp);
            $this->fenci_result=$fenci_result;
            $this->match_result=$fenci;
        }

        /*xj */


//		$second_symptom = I('post.second_symptom');
//		//将更多症状加入到确定症状中
//		$symptom_temp = $symptom_temp.' '.$second_symptom;
//		$this->symptom_input=$symptom_temp;
        /*xj end*/

//var_dump($symptom_z);
        if ($symptom_z)  //如果输入症状不为空
        {
            //zlz：司尚春给我的匹配词语太少了，几十个词，能用的有时候连一个都没有。打出来给雷总看看
			if(I('post.panduan')==null)
            {
            $symptom_match=array();
            $zlz_count=0;

            $zlz_begin=date('y-m-d h:i:s',time());

            $symptom_idlist = array();
            $symptom_query = M('symptom');
            foreach ($symptom_z as $symptom_zz) {
                //$symptom=$symptom_query->where('title like "%' . $symptom_z . '%"')->field('id')->select();
                $symptom_idlist_tmp = $symptom_query->where('title ="' . $symptom_zz . '"')->field('id')->select();
                if ($symptom_idlist_tmp != null) {
                    $zlz_count++;
                    array_push($symptom_match,$symptom_zz);
                    array_push($symptom_idlist, $symptom_idlist_tmp[0]['id']);
                }
            }
            $this->symptom_match=$symptom_match;
            $this->symptom_match_count=$zlz_count;

            $this->symptom_old=$symptom_match;
        }
		else {
            $zlz_count = 0;
            $symptom_idlist = array();
            $symptom_query = M('symptom');
            foreach ($symptom_z as $symptom_zz) {
                //$symptom=$symptom_query->where('title like "%' . $symptom_z . '%"')->field('id')->select();
//                var_dump($symptom_zz);
                $symptom_idlist_tmp = $symptom_query->where('title ="' . $symptom_zz . '"')->field('id')->select();
                if ($symptom_idlist_tmp != null) {
                    $zlz_count++;
                    array_push($symptom_idlist, $symptom_idlist_tmp[0]['id']);
                }
            }
        }

            //zlz：得到了症状们的ID，这里要考虑有的用户输入的症状数据库里面查不到的情况。。。哦，丝尚春给我的应该都是已经筛选过的肯定存在的症状了，那就不管了
//            var_dump($symptom_idlist);
//            var_dump((int)(5/2));

            $disease_symptom_table = M('disease_symptom_apply');
            $arr = array();
            foreach ($symptom_idlist as $symptomid) {
                //$disease = $symptom_table->where('id_symptom = "' . $symptomid['id'] . '"')->field('id_disease')->select();
                $t = $disease_symptom_table->where('id_symptom = "' . $symptomid . '"')->field('id_disease,probability')->select();
                if ($t != null) {
                    foreach ($t as $tt) {
                        //if($tt[])
                        array_push($arr, $tt);
                    }
                }
            }
//            var_dump($arr);
            //zlz：概率相乘，并去重，（一周后）还需要考虑每个疾病包含症状的个数，哦，其实每个的症状个数我之前也是计算了的，哈哈
            $temp = array();
            $max_count=0;
            foreach ($arr as $item) {
                list($id, $p) = array_values($item);
                $temp[$id]['gailv'] =(array_key_exists($id, $temp) ? $temp[$id]['gailv'] * $p : 1.0* $p);
                $temp[$id]['count'] = array_key_exists($id, $temp) ? $temp[$id]['count'] +1 : 1.0* $p;
                if($temp[$id]['count']>$max_count)
                    $max_count=$temp[$id]['count'];
            }

            //zlz：上一步中概率相乘，其实是一种不公平的现象，考虑为什么同时包含两个症状的疾病反而概率会较低呢？因为只含有一个症状的疾病没有乘以一个小于1是概率，所以我想做一个平滑的过程。
            //zlz：对于每一个疾病，将其包含的症状个数计数，其余疾病即使不包含相同数目的症状，也会乘以0.01
            foreach ($temp as &$item)
            {
                for($i=0;$i<$max_count-$item['count'];$i++)
                {
                    $item['gailv']= $item['gailv']*0.01;
                }

            }
//            var_dump($temp);
//            var_dump($max_count);
            $disease_idlist = array();
            foreach ($temp as $id => $p)
                $disease_idlist[] = array('id_disease' => $id, 'probability' => $p['gailv'],'symptom_count'=>$p['count']);

//            var_dump($disease_idlist);
            //var_dump($disease_idlist);
            //zlz：得到了与症状相关的疾病ID,然后这一步应该把条件概率加进来，可以直接乘这个结果
            //}//zlz：暂时的

            $disease_query = M('disease');
            $disease_list=array();
            $disease_detail_query = M('neike');
            $tiaojian_query=M('zhanglizhu');
            //zlz：这里先不做归一化，确定输出哪些之后再做归一化
//            $probability_fenmu=0.0;
            foreach($disease_idlist as $diseaseid)
            {
                $t1= $disease_query->where('id = "' . $diseaseid['id_disease'] . '"')->field('id,title,department,probability')->select();
                if($t1!=null)
                {
                    $t1[0]['probability']=$t1[0]['probability'] * $diseaseid['probability'];
                    $array['id_disease']= $t1[0]['id'];
                    $array['title']= $t1[0]['title'];
                    $array['department']= $t1[0]['department'];
                    $array['probability']= $t1[0]['probability'];
                    $array['symptom_count']= $diseaseid['symptom_count'];
					$t2= $disease_detail_query->where('title = "' . $t1[0]['title'] . '"')->field('summary')->select();
                    $t3= $tiaojian_query->where('disease = "' . $t1[0]['title'] . '"')->field('symptom,probability')->select();
                    if($t2!=null)
                    {
//                        var_dump($t2);
                        $array['summary']= $t2[0]['summary'];
                    }
                    else{
                        $array['summary']="暂无描述";
                    }
                    $array['tiaojian']=array();
                    if($t3!=null)
                    {
//                        var_dump($t3);
                        foreach($t3 as $tt3)
                        {
                            $array['tiaojian'][$tt3["symptom"]]=$tt3["probability"];
                        }
                    }
                    array_push($disease_list,$array);
                    //zlz：对概率做归一化处理，先确定分母
//                    $probability_fenmu=$probability_fenmu+ $array['probability'];
                }
            }

//            var_dump($probability_fenmu);
            //zlz：按照概率大小给相关疾病排个序
            function my_sort($arrays,$sort_key,$sort_order=SORT_ASC,$sort_type=SORT_NUMERIC){
                if(is_array($arrays)){
                    foreach ($arrays as &$array){
                        if(is_array($array)){
//                            $array[$sort_key]=$array[$sort_key]/$fenmu;
                            $key_arrays[] = $array[$sort_key];
                        }else{
                            return false;
                        }
                    }
                }else{
                    return false;
                }
                array_multisort($key_arrays,$sort_order,$sort_type,$arrays);
                return $arrays;
            }
//            $disease_list = my_sort($disease_list,'probability',SORT_DESC,SORT_NUMERIC,$probability_fenmu );
            $disease_list = my_sort($disease_list,'probability',SORT_DESC,SORT_NUMERIC );
//            var_dump($disease_list);

            //zlz：阈值&&归一化
            $disease_list_final=array();
            $threshold=(int)(count($symptom_idlist)/2);
//            var_dump($threshold);
            $probability_fenmu=0.0;
            foreach($disease_list as $disease_item)
            {
                if($disease_item['symptom_count']>=$threshold)
                {
                    array_push($disease_list_final,$disease_item);
                    $probability_fenmu=$probability_fenmu+ $disease_item['probability'];
                }
                else
                {
                    //zlz：默认只输出4个。如果满足包含症状最小个数的疾病很多，那就都列出来，比如查询 “烧心 , 咽喉疼 , 肚子疼 , 胃里食物反流回口腔 , 咳嗽”  ，满足包含症状不少于5/2的，有5个，最后就输出这5个，不止4个，这样子对包含症状个数均为2的疾病公平些
                    if(count($disease_list_final)<4)                   {
                        array_push($disease_list_final,$disease_item);
                        $probability_fenmu=$probability_fenmu+ $disease_item['probability'];
                    }
                }
            }
//            var_dump($disease_list_final);
//            var_dump($probability_fenmu);
            //zlz：得到了与症状相关的疾病的基本描述
            foreach($disease_list_final as &$disease_idlist_final_item)
            {
                $disease_idlist_final_item['probability']= $disease_idlist_final_item['probability']/$probability_fenmu;
            }
//            var_dump($disease_list_final);
            $this->disease_list=$disease_list_final;  //zlz：得到相关疾病们以及归一化的概率
//            var_dump(count($disease_list));



            $relate_symptomId_query = M('disease_symptom_apply');
            $relate_symptom_idlist=array();
            foreach($disease_list_final as $diseaseid)
            {
                //zlz：疾病是已经按照概率排好序的，再对每一个疾病中的相关症状排序
                $t2= $relate_symptomId_query->where('id_disease = "' . $diseaseid['id_disease'] . '"')->field('id_symptom,probability')->order('probability desc')->select();
                foreach($t2 as $tt2)
                {
                    if(!in_array($tt2['id_symptom'],$symptom_idlist)) //zlz：去掉用户原本输入的症状
                    {
                        if($tt2!=null)
                        {
                            array_push($relate_symptom_idlist,$tt2['id_symptom']);
                        }
                    }
                }
            }
//            var_dump($relate_symptom_idlist);
            $relate_symptom_idlist=array_unique($relate_symptom_idlist);//zlz：获得相关疾病的所有其他症状d ID，并去重
//            var_dump($relate_symptom_idlist);
            //zlz：取数组前20%的数
            //$yuzhi=((int)(count($relate_symptom_idlist)/5));
            //$relate_symptom_idlist=array_slice($relate_symptom_idlist,0,$yuzhi);

            //zlz：疾病那部分想办法收敛了，查出来的相关症状也不多，这里不用再截取什么了，先暂时注释掉
//            $relate_symptom_idlist=array_slice($relate_symptom_idlist,0,5);

//            var_dump($relate_symptom_idlist);


            $relate_symptom_query = M('symptom');
            $relate_symptom_list=array();
            foreach($relate_symptom_idlist as $relate_symptomid)
            {
                $t3= $relate_symptom_query->where('id = "' . $relate_symptomid . '"')->field('id,title')->select();
                if($t3!=null)
                {
                    array_push($relate_symptom_list,$t3);
                }
            }
            //var_dump($relate_symptom_list);
            //zlz：获取相关疾病的所有其他症状的描述


            $this->relate_symptom_list=$relate_symptom_list;
            $zlz_end=date('y-m-d h:i:s',time());
            $this->zlz_begin=$zlz_begin;
            $this->zlz_end=$zlz_end;
            $this->display();

        }
        else
        {
            alert("未匹配到相关症状（ssc）");
            //$this->redirect('Index/index');
        }

    }

}
