from django.contrib import admin
from django.core.cache import cache
from goods.models import GoodsType, IndexPromotionBanner,IndexGoodsBanner, IndexTypeGoodsBanner
# Register your models here.

# 基类 注重对象的重写 多态 父类拥有 让子类继承，那样就不用每个子类进行重写
# 传承：一对多的情况
# 继承：认爸爸的过程
class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """新增或更新表中的数据时调用 方法重写多态"""
        super().save_model(request, obj, form, change)

        # 发出任务, 让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """删除表中的数据时调用"""
        super().delete_model(request, obj)
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')


class GoodsTypeAdmin(BaseModelAdmin):
    pass

class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass

class IndexTypeGoodsBannerAdmini(BaseModelAdmin):
    pass

class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmini)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
