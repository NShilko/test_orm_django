
# Test ORM Django


Проектное задание


## Команды для выполнения поставленных задач

```bash
from publication.models import *

User.objects.create_user('pablo')
User.objects.create_user('zeleboba')

Author.objects.create(name_id=User.objects.get(username='zeleboba').id)
Author.objects.create(name_id=User.objects.get(username='pablo').id)

Category.objects.create(name='Спорт')
Category.objects.create(name='Красота')
Category.objects.create(name='Недвижимость')
Category.objects.create(name='Технологии')

Post.objects.create(title='Прощай, Бразилия! Хорватия снова выиграла серию пенальти и сотворила гиперсенсацию', main_text='Сами южноамериканцы, конечно, публично не высказывали пренебрежения в адрес оппонентов. А вот к животным они относились хуже: на предматчевой пресс-конференции Винисиуса пресс-атташе сборной схватил за шиворот запрыгнувшего на стол кота и бросил его на пол, чем моментально вызвал гнев в соцсетях. Винисиус в этот момент только неловко улыбался, хотя, наверное, понимал, что так лучше не делать. В футболе мелочей не бывает: этот инцидент создал негативный фон вокруг бразильцев, и многие даже писали, что намеренно будут болеть за хорватов.', isAuthor_id=Author.get_user_id('pablo'), kind='NEWS')
Post.objects.create(title='О каких заболеваниях и проблемах со здоровьем говорят волосы', main_text='Нервные потрясения и хронический стресс напрямую отражаются на состоянии волос. Например, сухие и ломкие волосы с секущимися кончиками говорят о проблеме в работе желчного пузыря, дефиците жирорастворимых витаминов и Омега-3 жирных кислот.', isAuthor_id=Author.get_user_id('pablo'), kind='PUBL')
Post.objects.create(title='В Москве будет новый стадион. Гандболисты и регбисты нашли точки соприкосновения', main_text='Долгое время в Москве остро стоял вопрос со стадионом «Фили» и прилегающей к нему территории. На ней собирались построить новый спорткомплекс, и строить собиралась группа компаний «Дело», которой владеет президент Федерации гандбола России Сергей Шишкарев. Регбисты возмутились. Хоть стадион со времен последних побед «Филей» в 1970-х не особо менялся, место намоленное. Подписывались петиции, проводились акции протеста. Хотя сам клуб сейчас играет не в высшей лиге чемпионата России и потерял былую славу.', isAuthor_id=Author.get_user_id('zeleboba'), kind='NEWS')

Post.add_category(1, [1,2,3])
Post.add_category(2, [2,4])
Post.add_category(3, [1,2,3,4])

Comment.objects.create(isPost_id=1, isUser_id=User.objects.get(username='pablo').id, main_text = 'Это веселый комментарий #1')
Comment.objects.create(isPost_id=1, isUser_id=User.objects.get(username='zeleboba').id, main_text = 'Это грустный комментарий #2')
Comment.objects.create(isPost_id=2, isUser_id=User.objects.get(username='zeleboba').id, main_text = 'Это нейтральный комментарий #1')
Comment.objects.create(isPost_id=3, isUser_id=User.objects.get(username='pablo').id, main_text = 'Это агрессивный комментарий #1')

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()

Author.get_best_author()

Author.update_rating()

Post.show_best_post()
Post.show_best_post(True)
```