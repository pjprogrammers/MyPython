for i in range (140,249):
    p = ('''<div class="item" style="background-image: url(Anime/{}.jpeg);">
                <div class="content">
                    <div class="name">Switzerland</div>
                    <div class="des">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ab, eum!</div>
                    <button>See More</button>
                </div>
            </div>''')
    print(p.format(i))