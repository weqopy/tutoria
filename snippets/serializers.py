from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "linenos", "language", "style")

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # # 控制 serializer 的显示
    # code = serializers.CharField(style={"base_template": "textarea.html"})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.code = validated_data.get("code", instance.code)
    #     instance.linenos = validated_data.get("linenos", instance.linenos)
    #     instance.language = validated_data.get("language", instance.language)
    #     instance.style = validated_data.get("style", instance.style)
    #     instance.save()
    #     return instance


# ---------- 示例 ----------
#
"""
python manage.py shell 进入 Django shell

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

snippet = Snippet(code='print "hello, the third snippet"\n')
serializer.save()

# 实例序列化
# 模型实例转换为 Python 原生数据类型
serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 3, 'title': '', 'code': 'print "hello, the third snippet"\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
# 完成序列化，将数据转换为 json
content = JSONRenderer().render(serializer.data)
content
# b'{"id":3,"title":"","code":"print \\"hello, the third snippet\\"\\n","linenos":false,"language":"python","style":"friendly"}'

# 反序列化
# 将一个流解析为 Python 原生数据类型
from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
# 将 Python 原生数据类型恢复为正常的对象实例
serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, the third snippet"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object (4)>

# 序列化查询结果集（querysets），只需添加`many=True`
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print "hello, the third snippet"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 4), ('title', ''), ('code', 'print "hello, the third snippet"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
"""
