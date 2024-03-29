from django.db import models

# Create your models here.

#会自动生成一个自增的id字段，在model里不用定义
class TestSummary(models.Model):
 
    create_time = models.CharField(max_length=50, default="")
    start_time = models.CharField(max_length=50, default="")
    end_time = models.CharField(max_length=50, default="")
    user = models.CharField(max_length=50)
    runningIP = models.CharField(max_length=50, default="")
    errorlog = models.TextField(default="")
    #status：任务的状态   0:未开始(waiting) 1:已分配(ready)  2正在运行(running) 3:出错停止(error) 4:已完成(finished) 5:任务取消(canceled) 6:准备取消(canceling)
    status = models.IntegerField(default=0)
    testitem = models.CharField(max_length=500, default="")  #选择的执行项目
        
    #step =  models.IntegerField(default=-1)
   
    testsvn = models.TextField(default="")
    basesvn = models.TextField(default="")
    newdataip = models.CharField(max_length=500, default="")
    newdatauser = models.CharField(max_length=500, default="")
    newdatapassw = models.CharField(max_length=500, default="")
    newdatapath = models.CharField(max_length=500, default="")
    newconfip = models.CharField(max_length=500, default="")
    newconfuser = models.CharField(max_length=500, default="")
    newconfpassw = models.CharField(max_length=500, default="")
    newconfpath = models.CharField(max_length=500, default="")
    remarks = models.TextField(default="")
    
    performance_base = models.TextField(default="")
    performance_test = models.TextField(default="")
    code_gcov_result = models.TextField(default="")
    code_cppcheck_result = models.TextField(default="")
     
    # cost_test = models.TextField(default="")
    # cost_base = models.TextField(default="")
    # result_diff_precent = models.TextField(default="")
    # test_cpu_performance = models.TextField(default="")
    # base_cpu_performance = models.TextField(default="")
    # regression_test_result = models.TextField(default="")
    # cache_compatibility = models.TextField(default="")
    # probe_result = models.TextField(default="")
    # exceptions = models.TextField(default="")
    # pvscheck_block_num = models.IntegerField(default=-1)
    # pvscheck_result_link = models.TextField(default="")


#这里task也可以使用外键，用TestSummary的id作为外键，将diff结果与任务关联起来
#实际上直接存入任务id也可以，比较简单，采用此方法
class SummaryDiff(models.Model):
 
    task_id = models.IntegerField(default=-1)
    storage_time = models.CharField(max_length=50, default="")
    base_res = models.TextField(default="")
    test_res = models.TextField(default="")