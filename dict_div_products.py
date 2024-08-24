dev_str = """
        <div class="col-md-6 col-lg-4 col-xl-3">
                <div class="rounded position-relative fruite-item">
                    <div class="fruite-img">
                        <img src="img/{}" class="img-fluid w-100 rounded-top" alt="">
                    </div>
                    <div class="text-white bg-secondary px-3 py-1 rounded position-absolute" style="top: 10px; left: 10px;">{}</div>
                    <div class="p-4 border border-secondary border-top-0 rounded-bottom">
                        <h4>{}</h4>
                        <p>{}</p>
                        <div class="d-flex justify-content-between flex-lg-wrap">
                            <!--<p class="text-dark fs-5 fw-bold mb-0">$4.99 </p>-->
                            <!-- <a href="#" class="btn border border-secondary rounded-pill px-3 text-primary"><i class="fa fa-shopping-bag me-2 text-primary"></i> Add to cart</a>-->
                        </div>
                    </div>
                </div>
        </div>
        """

extract_dict = [{
            "id": 1,
            "name": "Andrographis Paniculata Extract",
            "ingredients": 'Total bitters as andrographolides 5-50%',
            "benefit": 'Treatment of common cold, Hepato protective effects, Anti-bacterial and Anti- parasitic, Supports Healthy Inflammatory Response.',
            "img": "AndrographisPaniculata"
        },{
            "id": 2,
            "name": "Ashwagandha Extract",
            "ingredients": "Withanolide glycosides 1.5 -8%, Saponins 2.5%",
            "benefit": "Antioxidant, anti-stress, rejuvenating effect, immunomodulatory effect",
            "img": "Ashwagandha"
        },{
            "id": 3,
            "name": "Boswellia Serratta Extract",
            "ingredients": "Boswellic Acid 65%-85%",
            "benefit": "Supports Healthy Inflammatory Response, Supports Joint Health",
            "img": "BoswelliaSerratta"
        },{
            "id": 4,
            "name": "Black Pepper Extract",
            "ingredients": "Caryophyllene(24.42%), Limonene(15.10%)",
            "benefit": "Used for the treatment of epilepsy and pain in traditional medicine",
            "img": "BlackPepper"
        },{
            "id": 5,
            "name": "Brahmi Extract",
            "ingredients": "Bacosides 25%",
            "benefit": "Memory Booster",
            "img": "Brahmi"
        },{
            "id": 6,
            "name": "Cinnamon Extract",
            "ingredients": "Total Polyphenols 10-30%",
            "benefit": "Memory Booster",
            "img": "Cinnamon"
        },{
            "id": 7,
            "name": "Curcumin - Effervescent",
            "ingredients": "Curcuminiods 37.5%",
            "benefit": "Free flowing effervescent granules",
            "img": "CurcuminEffervescen"
        },{
            "id": 8,
            "name": "Curcumin Ethanol",
            "ingredients": "Curcuminiods 95%",
            "benefit": "Extraction Solvent- Ethanol",
            "img": "CurcuminEthanol"
        },{
            "id": 9,
            "name": "Curcumin Oil Soluble",
            "ingredients": "Curcuminiods 28.5%",
            "benefit": "Easily soluble with MCT oil or Hemp oil",
            "img": "CurcuminOilSoluble"
        },{
            "id": 10,
            "name": "Curcumin Powder",
            "ingredients": "Curcuminiods 95%",
            "benefit": "Powder",
            "img": "CurcuminPowder"
        },{
            "id": 11,
            "name": "Curcumin Powder(Water Dispersible)",
            "ingredients": "Curcuminiods 45%",
            "benefit": "Water dispersible powder",
            "img": "CurcuminPowderWaterDispersible"
        },{
            "id": 12,
            "name": "Curcumin – Stain Free",
            "ingredients": "Curcuminiods 95%",
            "benefit": "Easy free flowing Stain Free granules",
            "img": "CurcuminStainFree"
        },{
            "id": 13,
            "name": "Curcumin - High Density",
            "ingredients": "Curcuminiods 95%",
            "benefit": "Easy to fill in capsules, maximum loading ensured. Low wastage during encapsulation.",
            "img": "CurcuminHighDensity"
        },{
            "id": 14,
            "name": "Essential Oil of Mustard",
            "ingredients": "AITC 95% , BITC 85%",
            "benefit": "Flavouring Agent",
            "img": "Mustard"
        },{
            "id": 15,
            "name": "Fenugreek Extract",
            "ingredients": "Saponins 30-60%",
            "benefit": "Supports immune system, lowers blood glucose, Supports healthy cholesterol levels",
            "img": "Fenugreek"
        },{
            "id": 16,
            "name": "Garcinia Cambogia Extract",
            "ingredients": "HCA 50-60% powder, granules",
            "benefit": "Weight control, obesity satiety",
            "img": "GarciniaCambogia"
        },{
            "id": 17,
            "name": "Ginger Extract",
            "ingredients": "Gingerol 5-10%",
            "benefit": "Supports Healthy Inflammatory Response, improves digestion, anti-emetic",
            "img": "Ginger"
        },{
            "id": 18,
            "name": "Green Coffee Extract",
            "ingredients": "Chlorogenic acid 45%-50%",
            "benefit": "Weight loss agent, effective antioxidant reduces the risk of diabetes",
            "img": "GreenCoffee"
        },{
            "id": 19,
            "name": "Green Tea Extract",
            "ingredients": "30% EGCG, 75% polyphenols,15% EGCG & 50% polyphenols(water soluble)",
            "benefit": "Weight control, antioxidant, anti-carcinogenic",
            "img": "GreenTea"
        },{
            "id": 20,
            "name": "Guggul Lipid Extract",
            "ingredients": "Guggul Sterones 2.5-10%",
            "benefit": "Inhibits platelet aggregation",
            "img": "Guggul"
        },{
            "id": 21,
            "name": "Gymnema Sylvestre Extract",
            "ingredients": "Gymnemic Acid 25% & 75%",
            "benefit": "Support healthy blood glucose levels",
            "img": "Gymnema"
        },{
            "id": 22,
            "name": "Mustard Seed Extract",
            "ingredients": "Total lignans 70%",
            "benefit": "Antioxidant, healthy blood glucose, enhances the metabolism of omega-3 fatty acids, protects liver from alcohol toxicity, reduces hangover",
            "img": "Mustard"
        },{
            "id": 23,
            "name": "Pterocarpus Marsupium Extract",
            "ingredients": "Pterostilbene 5%",
            "benefit": "Support healthy blood glucose levels",
            "img": "Pterocarpus"
        },{
            "id": 24,
            "name": "Sesame Seed Extract",
            "ingredients": "Total lignans 70%",
            "benefit": "Antioxidant, healthy blood glucose, enhances the metabolism of omega-3 fatty acids, protects liver from alcohol toxicity, reduces hangover",
            "img": "Sesame"
        },{
            "id": 25,
            "name": "Tribulus Terrestris",
            "ingredients": "Saponins 40%-90%",
            "benefit": "Sports medicine, libido enhancer, suitable for beverages",
            "img": "Tribulus"
        }]

finished_prod = [
        {
            "id": 1,
            "category": "capsules",
            "name": "BELLY HEALTH",
            "ingredients": "Potent combination of Herbs",
            "benefits": "Helps promote overall gut health, Helps reduce abdominal bloating, Helps improve gut microbiome, Supports Healthy Digestion",
            "extra_info": "Each vegetarian capsules contains blend of 14 different herbs",
            "product_img": "GUTEAZE"
        }, {
            "id": 2,
            "category": "capsules",
            "name": "BRAHMI",
            "ingredients": "Brahmi Extract (Bacopa)",
            "benefits": "Supports cognitive Health, Helps in reducing stress & anxiety, Helps to promote mind wellness",
            "extra_info": "Each vegetarian capsules contains pure Brahmi Extract",
            "product_img": "BRAHMI"
        }, {
            "id": 3,
            "category": "capsules",
            "name": "DAILY BREATH",
            "ingredients": "Boswellia Serrata Extract",
            "benefits": "Support respiratory health, Helps improve overall lung health, Helps in reducing coughing and wheezing, Regulate chest tightness and breathlessness",
            "extra_info": "Each Vegetarian capsule contains Pure Boswellia extract",
            "product_img": "BOSWELLIA"
        }, {
            "id": 4,
            "category": "capsules",
            "name": "DAILY GRENADE",
            "ingredients": "Pomegranate Extract",
            "benefits": "Supports overall heart health, Helps manage blood pressure, Helps slow arterial wall thickening, Powerful antioxidant",
            "extra_info": "Each vegetarian capsules contains Pomegranate Extract",
            "product_img": "POMEGRANATE"
        }, {
            "id": 5,
            "category": "capsules",
            "name": "DAILY GUARD",
            "ingredients": "Purified turmeric Extract",
            "benefits": "Strengthen body’s defence system naturally, Protect body from detrimental free radicals, Build strong immunity from inside out",
            "extra_info": "each vegetable contains purified turmeric extract",
            "product_img": "DEFENCE"
        }, {
            "id": 6,
            "category": "capsules",
            "name": "DAILY SLUMBER",
            "ingredients": "Ashwagandha Extract",
            "benefits": "Helps improve sleep quality, Helps in reducing Stress & Anxiety, Helps in mood regulation, Helps in rejuvenating mind & body, Helps enhance alertness",
            "extra_info": "Each vegetarian capsules contains pure Ashwagandha Extract",
            "product_img": "ASHWAGANDHA"
        }, {
            "id": 7,
            "category": "capsules",
            "name": "EVERDAY AMLA",
            "ingredients": "Amla Extract",
            "benefits": "Maintain a healthy triglycerides level, Improve overall heart health, Helps reduce visceral fat, Reduce the risk of cardiac disease",
            "extra_info": "Each vegetarian capsules contains Amla Extract",
            "product_img": "AMLA"
        }, {
            "id": 8,
            "category": "capsules",
            "name": "EVERDAY BRAHMI",
            "ingredients": "Brahmi Extract (Bacopa)",
            "benefits": "Supports cognitive Health, Helps in reducing stress & anxiety, Helps to promote mind wellness",
            "extra_info": "Each vegetarian capsules contains pure Brahmi Extract",
            "product_img": "BRAHMI"
        }, {
            "id": 9,
            "category": "capsules",
            "name": "EVERDAY GREEN TEA",
            "ingredients": "Green Tea Extract",
            "benefits": "Helps in weight management, Support cardiovascular health, Support healthy metabolism, Powerful antioxidant",
            "extra_info": "Each vegetarian capsules contains Green Tea Extract",
            "product_img": "GREENTEA"
        }, {
            "id": 10,
            "category": "capsules",
            "name": "EVERDAY MORINGA",
            "ingredients": "Moringa leaf Extract",
            "benefits": "Supports eye health, Supports skin and hair care, supports in weight management, Supports overall health, metabolism and immunity",
            "extra_info": "Each vegetarian capsules contains Moringa Extract",
            "product_img": "MORINGA"
        }, {
            "id": 11,
            "category": "capsules",
            "name": "EVERYDAY STAMINA",
            "ingredients": "Red Spinach Extract",
            "benefits": "Supports enhanced nitric oxide level in the body, Improved Athletic performance, Enhanced Blood Circulation",
            "extra_info": "Each vegetarian capsules contains Red Spinach Extract",
            "product_img": "NDURANCE"
        }, {
            "id": 12,
            "category": "capsules",
            "name": "EVERYDAY TRIPHALA",
            "ingredients": "Amla Extract",
            "benefits": "Promote overall gut health, Helps promote bowel wellness, Helps to promote metabolism",
            "extra_info": "Each vegetarian capsules contains Triphala Extract",
            "product_img": "TRIPHALA"
        }, {
            "id": 19,
            "category": "softgels",
            "name": "FLAX OMEGA",
            "ingredients": "Omega 3 Flaxseed oil",
            "benefits": "Supports overall health, Anti-oxidant and anti-inflammatory, Helps to maintain liver & heart health, Helps Brain, Join, Skin & Hair Health",
            "extra_info": "each softgel contains flaxseed oil",
            "product_img": "OMEGAFLAX"
        }, {
            "id": 13,
            "category": "capsules",
            "name": "FORTY WINKS POWER NAP",
            "ingredients": "Ashwagandha Extract",
            "benefits": "Restful sleep, Helps manage stress, Wake-Up Refreshed",
            "extra_info": "Each vegetarian capsules contains Ashwagandha Extract",
            "product_img": "SLEEPNREST"
        }, {
            "id": 14,
            "category": "capsules",
            "name": "JOINT COMFORT",
            "ingredients": "Boswellia Serrata Extract",
            "benefits": "Supports joint health, Improve joint mobility & flexibility, Supports Healthy Cartilage function, Helps reduce inflammation",
            "extra_info": "each Vegetarian capsule contains Turmeric and Boswellia extract",
            "product_img": "JOINTRECUE"
        }, {
            "id": 20,
            "category": "softgels",
            "name": "JOINT RELIEF",
            "ingredients": "Blend of Turmeric, Boswellia and Sesame oil",
            "benefits": "Supports pain relief, helps reduce inflammation, Help improve flexibility, Supports Musculoskeletal mobility",
            "extra_info": "each softgel contains Turmeric & Boswellia extract with Sesame oil",
            "product_img": "RHULIEF"
        }, {
            "id": 15,
            "category": "capsules",
            "name": "OMEGA & CUMIN",
            "ingredients": "Omega 3 Flaxseed oil",
            "benefits": "Improve immunity, supports skin & hair health, supports brain health, anti-oxidant & anti-inflammatory",
            "extra_info": "Each softgel contains Flaxseed oil and black cumin seed extract",
            "product_img": "FLAXNCUMIN"
        }, {
            "id": 16,
            "category": "capsules",
            "name": "OMEGA DOUBLE ACTION",
            "ingredients": "Omega 3 Fish oil",
            "benefits": "Improve overall heart health, Boost overall immunity, Boost eye, Brain and Nerve function, Promote Liver health",
            "extra_info": "each softgel contains fish oil",
            "product_img": "OMEGADOUBLE"
        }, {
            "id": 17,
            "category": "capsules",
            "name": "OMEGA TRIPLE ACTION",
            "ingredients": "Omega 3 Fish oil",
            "benefits": "Improve overall heart health, Boost overall immunity, Boost eye, Brain and Nerve function, Promote Liver health",
            "extra_info": "each softgel contains vitamin D, E & K",
            "product_img": "OMEGATRIPLE"
        }, {
            "id": 18,
            "category": "capsules",
            "name": "SUGAR CONTROL",
            "ingredients": "Amla Extract",
            "benefits": "Promote healthy blood sugar metabolism, regulate blood sugar levels, support normal insulin response",
            "extra_info": "Each vegetarian capsules contains turmeric, amla and pterocarpus marsupium extract",
            "product_img": "GLUCOBALANCE"
        }
    ]

fopen = open('extracts_covert.txt', 'w')
for i in extract_dict:
    body_text = 'Ingredients : ' + i['ingredients'] + ' Benefits : ' + i['benefit']
    pic_name = 'products/Extract/' + i['img'] + '.jpg'
    new_div_string = dev_str.format(pic_name, 'Extracts', i['name'], body_text)
    fopen.writelines(new_div_string)
    fopen.writelines('\n')

fopen = open('options_extact.txt', 'w')
for i in extract_dict:
    string_convert = '<option value="{}">{}</option>'
    new_string = string_convert.format(i['name'], i['name'])
    fopen.writelines(new_string)
    fopen.writelines('\n')

fopen = open('finshed_covert.txt', 'w')
for i in finished_prod:
    body_text = 'Ingredients : ' + i['ingredients'] + ' Benefits : ' + i['benefits']
    pic_name = 'products/Finished_Product/' + i['product_img'] + '.jpg'
    new_div_string = dev_str.format(pic_name, 'Finished Products', i['name'], body_text)
    fopen.writelines(new_div_string)
    fopen.writelines('\n')

fopen = open('options_finshed.txt', 'w')
for i in finished_prod:
    string_convert = '<option value="{}">{}</option>'
    new_string = string_convert.format(i['name'], i['name'])
    fopen.writelines(new_string)
    fopen.writelines('\n')
