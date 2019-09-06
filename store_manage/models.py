import uuid

from django.db import models


class StoreInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 品牌
    brand = models.CharField(max_length=10)
    # 店铺编号
    code = models.CharField(max_length=10, null=True)
    # 店铺名称
    name = models.CharField(max_length=100, null=True)
    # 地址
    address = models.CharField(max_length=300, null=True)
    # IP
    ip = models.GenericIPAddressField(protocol='IPv4', null=True)
    # AP 数量
    ap = models.PositiveSmallIntegerField(null=True)
    # 联系人
    contacts = models.TextField(null=True)
    # 设备到店日期
    equipment_arrival_date = models.DateField(null=True)
    # 工程完工日期
    completion_date = models.DateField(null=True)
    # 预计安装日期
    expected_installation_date = models.DateField(null=True)
    # 开店日期
    Opening_date = models.DateField(null=True)
    # 工程部负责人
    engineering_head = models.CharField(max_length=100, null=True)
    # 防火墙类型
    firewall_type = models.CharField(max_length=20)
    # 状态：1，筹备 2，正常 3，护肤 4，闭店
    status = models.CharField(max_length=10)
    # 备注
    ps = models.TextField(max_length=300, null=True)