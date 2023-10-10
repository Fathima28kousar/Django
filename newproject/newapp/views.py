from django.shortcuts import render


def home(request):
    context = {'page':'Home'}
    peoples =[
        {'name':'rahul','age':50},
        {'name':'sonia','age':60},
        {'name':'priyanka','age':17},
        {'name':'modi','age':30},
        {'name':'gandhi','age':2},
        {'name':'amit','age':100}
    ]

    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi nostrum quod ipsa aperiam iusto voluptatibus iste ipsum autem qui, hic quam inventore, neque blanditiis. Ratione enim temporibus dolorem fuga dolore.
        Maxime sit corporis nam reiciendis dolor libero ipsa tempore eos! Eligendi possimus inventore molestias illo tempora veniam quisquam ipsum aspernatur reiciendis, doloribus nemo quam, officiis, sapiente pariatur nulla fugit ratione?
        Recusandae, odio corporis? Aspernatur, officia assumenda? Vero maxime sed neque cupiditate tempore. Ratione ipsam tempore quasi natus perferendis dolor voluptatum veritatis totam sint animi ab, nemo impedit iste eius atque.
        Harum in iusto quas dolorem illo deleniti quasi unde aspernatur distinctio, odit aut, ratione eligendi voluptas et nostrum nihil quidem tempore impedit perspiciatis laborum commodi. Maxime animi earum numquam perspiciatis.
        Voluptates sunt blanditiis provident, magni nemo soluta laborum laboriosam accusantium quos iusto tempora. Expedita fugiat cumque, repudiandae nobis officia, dolore excepturi alias deserunt autem optio voluptate quibusdam quaerat repellat unde!
        Odit est quod perspiciatis quia ullam ad quaerat delectus culpa nam, esse nihil unde ut maiores reprehenderit saepe labore illum! Perspiciatis minus quasi consequuntur cupiditate similique laboriosam incidunt quisquam est.
        Quibusdam omnis eos sapiente fuga, illo architecto nemo odit iure placeat pariatur facilis deserunt porro libero ducimus velit delectus esse repudiandae eaque. Voluptatibus nemo perspiciatis recusandae molestias, aspernatur vero dicta?
        Unde, iusto alias voluptatibus vitae vel atque quaerat labore dicta veniam explicabo odit! Sint, a accusantium debitis aliquam natus numquam, voluptates totam necessitatibus repudiandae temporibus dignissimos? Eos doloremque possimus distinctio.
        Eos laboriosam dignissimos dolor maxime numquam excepturi in sapiente quo ex voluptatibus est facilis autem voluptate fugit, ullam recusandae dolorum quod non rem. In et necessitatibus eos explicabo quaerat voluptatibus.
        Accusantium vero sunt officiis autem ex quae, vel porro eaque dignissimos suscipit modi error beatae repudiandae numquam necessitatibus consequatur facilis praesentium, sit inventore dolorum eligendi, repellendus amet. Ea, nemo pariatur?

"""
    return render(request,'index.html',context={'page':'Django page','peoples':peoples,'text':text})

def about(request):
    context = {'page':'About'}
    return render(request,'about.html',context)

def contact(request):
    context = {'page':'contact'}
    return render(request,'contact.html',context)