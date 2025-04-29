from flask import Flask, request, jsonify

app = Flask(__name__)

# Pricing dictionary
pricing = {
    "Wardrobes": 500, "Bedside Table": 200, "Chest of Drawers": 300,
    "Single Bed": 400, "Double Bed": 500, "Queen Size Bed": 600, "King Size Bed": 700,
    "Bunk Bed": 650, "Sofa Cum Bed / Diwan": 600, "Baby Cradle": 250,
    "Single Mattress": 300, "Double Mattress": 350, "Queen/King Size Mattress": 400, "Foldable Mattress": 250,
    "TV Unit / Entertainment Unit": 500, "Shoe rack": 200, "Center Table": 250,
    "Coffee Table": 250, "1/2/3/5/7 Seater Sofa": 800, "Recliner Sofa": 850,
    "L-Shape Sofa": 900, "Rocking Chair": 250, "Dining Table (4/6/8 Seater)": 800,
    "Dining Chairs": 150, "Armchair": 200, "Bean Bag / Pouffe": 100,
    "Kitchen Utensils": 200, "Crockery/Glassware": 150, "Cutlery Sets": 100,
    "Washing Machine": 500, "Refrigerator (Single/Dual Door)": 600, "Dishwasher": 500,
    "Kitchen Chimney": 300, "Microwave / OTG": 300, "Water Purifier": 200,
    "Gas Stove / Cooking Range": 400, "Air Conditioner (Window/Split)": 700,
    "Fan / Cooler / Heater": 150, "Television": 500, "Iron / Ironing Board": 150,
    "Vacuum Cleaner": 250, "Tandoor / Barbeque Grill": 250, "Geyser": 300,
    "Bedding / Mattress Protectors": 100, "Pillows / Cushions": 50, "Blankets / Quilts": 100,
    "Books / Magazines": 50, "Files / Stationery": 50, "Toys / Board Games": 75,
    "Decorative Items": 100, "Suitcases / Trolleys": 150, "Storage Boxes": 100, "Bicycle": 300,
    "Small Plant": 50, "Medium Plant": 75, "Large Plant": 100,
    "Pet Accessories": 150, "Gym Equipment": 500, "Baby Items": 400, "Musical Instruments": 600,
    "Hatchback Car": 2500, "Bike - upto 200 cc": 800, "Bike - upto 350 cc": 1000,
    "Luxury Bike": 1500, "Scooty / Scooter": 800, "SUV Car": 3000,
    "Luxury Car": 3500, "Sedan Car": 2800
}

@app.route('/')
def home():
    return "Welcome! This is the relocation quote API. POST to /calculate to get a quote."

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    pickup_floor = int(data.get('pickup_floor', 0))
    drop_floor = int(data.get('drop_floor', 0))
    pickup_lift = data.get('pickup_lift', True)
    drop_lift = data.get('drop_lift', True)
    items = data.get('items', [])

    total = 0
    for item in items:
        name = item.get('name')
        quantity = int(item.get('quantity', 1))
        cost = pricing.get(name, 0)
        total += cost * quantity

    # Calculate floor charges
    floor_charge = 0
    if not pickup_lift:
        floor_charge += pickup_floor * 100
    if not drop_lift:
        floor_charge += drop_floor * 100

    total += floor_charge

    return jsonify({
        'total_estimate': total,
        'floor_charge': floor_charge
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
