from flask import Flask, jsonify

app = Flask(__name__)

# Define dictionaries to store data for different categories
data = {
    'dogs': [
        {
            'name': 'Maltipoo',
            'image_url': 'https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg?crop=0.444xw:1.00xh;0.129xw,0&resize=980:*'
        },
        {
            'name': 'Chow-chow',
            'image_url': 'https://hips.hearstapps.com/hmg-prod/images/chow-chow-portrait-royalty-free-image-1652926953.jpg?crop=0.44455xw:1xh;center,top&resize=980:*'
        },
        {
            'name': 'Border Collie',
            'image_url': 'https://hips.hearstapps.com/hmg-prod/images/happy-dog-outdoors-royalty-free-image-1652927740.jpg?crop=0.447xw:1.00xh;0.187xw,0&resize=980:*'
        },
        {
            'name': 'Siberian Husky',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-464163411.jpg?crop=1.0xw:1xh;center,top&resize=980:*'
        },
        {
            'name': 'Pembroke Welsh Corgi',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/pembroke-welsh-corgi.jpg?crop=1xw:0.9997114829774957xh;center,top&resize=980:*'
        },
        {
            'name': 'Australian Shepherd',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/2560x3839/australian-shepherd.jpg?resize=980:*'
        },
        {
            'name': 'Shetland Sheepdog',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/shetland-sheep-dog.jpg?crop=1.0xw:1xh;center,top&resize=980:*'
        },
        {
            'name': 'Golden Retriever',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-147786673.jpg?crop=0.4444444444444445xw:1xh;center,top&resize=980:*'
        },
        {
            'name': 'Yorkshire Terrier',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/1280x1919/gettyimages-179494696.jpg?resize=980:*'
        },
        {
            'name': 'English Setter',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/1280x1919/gallery-gettyimages-485681215.jpg?resize=980:*'
        },
        {
            'name': 'Labrador Retriever',
            'image_url': 'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/40/3200x4799/labrador-retriever.jpg?resize=980:*'
        }
    ],
    'lions': [
        {
            'name': 'Asiatic Lion',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/Asiatic-Lion.jpg.webp'
        },
        {
            'name': 'African Lion',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/African-Lion.jpg.webp'
        },
        {
            'name': 'White Lion',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/White-Lion.jpg.webp'
        },
        {
            'name': 'Masai Lion',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/Masai-Lion.jpg.webp'
        },
        {
            'name': 'Abyssinian Lion',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/Abyssinian-Lion.jpg.webp'
        }
    ],
    'bears': [
        {
            'name': 'Polar Bear',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/Polar-Bears-300x200.jpg.webp'
        },
        {
            'name': 'North America Black Bear',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/North-America-Black-Bear-300x227.jpg.webp'
        },
        {
            'name': 'Brown Bear',
            'image_url': 'https://www.ourendangeredworld.com/wp-content/uploads/2020/12/Brown-Bear-300x199.jpg.webp'
        }
    ],
    'tigers': [
        {
            'name': 'Bengal Tiger',
            'image_url': 'https://animalsafari.com/wp-content/uploads/2022/01/bengal-tiger-1.jpeg'
        },
        {
            'name': 'White Tiger',
            'image_url': 'https://animalsafari.com/wp-content/uploads/2022/01/white-tiger-2048x1365.jpg'
        },
        {
            'name': 'Siberian Tiger',
            'image_url': 'https://animalsafari.com/wp-content/uploads/2022/01/siberian-tiger.jpg'
        },
        {
            'name': 'Sumatran Tiger',
            'image_url': 'https://animalsafari.com/wp-content/uploads/2022/01/sumatran-tiger-1.jpg'
        },
        {
            'name': 'IndoChinese Tiger',
            'image_url': 'https://animalsafari.com/wp-content/uploads/2022/01/indochinese-tiger.jpg'
        }
    ],
    'deers': [
        {
            'name': 'The Cervinae Subfamily',
            'image_url': 'https://a-z-animals.com/media/2021/09/buck.jpg'
        },
        {
            'name': 'The Capreolinae Subfamily',
            'image_url': 'https://a-z-animals.com/media/2021/09/Roe-deer-herd.jpg'
        },
        {
            'name': 'Elk',
            'image_url': 'https://a-z-animals.com/media/2021/08/elk.jpg'
        },
        {
            'name': 'Red Deer',
            'image_url': 'https://a-z-animals.com/media/animals/images/original/deer5.jpg'
        },
        {
            'name': 'Fallow Deer',
            'image_url': 'https://a-z-animals.com/media/2021/05/Fallow-deer-female.jpg'
        },
        {
            'name': 'Reindeer',
            'image_url': 'https://a-z-animals.com/media/2021/08/Reindeer-Antlers-male-caribou.jpg'
        },
        {
            'name': 'White Tailed Deer',
            'image_url': 'https://a-z-animals.com/media/2021/05/white-tailed-deer-in-meadow.jpg'
        },
        {
            'name': 'Roe Deer',
            'image_url': 'https://a-z-animals.com/media/2021/09/Roe-deer-in-field.jpg'
        },
        {
            'name': 'Moose',
            'image_url': 'https://a-z-animals.com/media/2022/09/iStock-1267859318-1536x1024.jpg'
        }
    ]
}


@app.route('/animals')
def get_animals():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
