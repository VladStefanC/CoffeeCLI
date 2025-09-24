# recipes.py

recipes = [
    {
        "id": 1,
        "method": "AeroPress",
        "name": "Classic AeroPress",
        "ingredients": "15g medium-fine coffee, 220ml water",
        "steps": "Add coffee, bloom 30s with 50ml water, stir, add rest of water, press after 2:30",
        "brew_time": "2:30-3:00"
    },
    {
        "id": 2,
        "method": "AeroPress",
        "name": "Inverted AeroPress",
        "ingredients": "17g medium coffee, 240ml water",
        "steps": "Assemble upside-down, add coffee + water, stir, steep 1:30, flip and press",
        "brew_time": "2:00-2:30"
    },
    {
        "id": 3,
        "method": "Cold Brew",
        "name": "Overnight Cold Brew",
        "ingredients": "60g coarse coffee, 1L cold water",
        "steps": "Mix coffee + water in jar, steep 12–16 hours, strain through filter",
        "brew_time": "12h-16h"
    },
    {
        "id": 4,
        "method": "Cold Brew",
        "name": "Japanese Iced Coffee (Flash Brew)",
        "ingredients": "20g medium coffee, 150ml hot water, 150g ice",
        "steps": "Brew coffee directly over ice in Chemex or V60, stir, serve",
        "brew_time": "3:00-4:00"
    },
    {
        "id": 5,
        "method": "French Press",
        "name": "Classic French Press",
        "ingredients": "30g coarse coffee, 500ml water",
        "steps": "Add coffee + water, stir, steep 4 min, plunge slowly",
        "brew_time": "4:00"
    },
    {
        "id": 6,
        "method": "French Press",
        "name": "French Press Bloom Method",
        "ingredients": "18g coarse coffee, 300ml water",
        "steps": "Bloom with 60ml for 30s, add rest of water, steep 3:30, plunge",
        "brew_time": "4:00"
    },
    {
        "id": 7,
        "method": "V60",
        "name": "Standard V60",
        "ingredients": "15g medium-fine coffee, 250ml water",
        "steps": "Bloom 30s with 50ml, pour in circles in 3 stages, finish ~2:30-3:00",
        "brew_time": "2:30-3:00"
    },
    {
        "id": 8,
        "method": "V60",
        "name": "Light Roast V60",
        "ingredients": "18g coffee, 300ml water",
        "steps": "Bloom 45s with 60ml, pour in 4 stages, finish ~3:30",
        "brew_time": "3:30-4:00"
    },
    {
        "id": 9,
        "method": "AeroPress",
        "name": "Competition Style AeroPress",
        "ingredients": "18g medium-fine coffee, 230ml water at 92°C",
        "steps": "Preheat brewer, bloom 30s with 60ml, stir 10x, add remaining water, plunge starting at 1:45 over 45s",
        "brew_time": "2:30"
    },
    {
        "id": 10,
        "method": "AeroPress",
        "name": "AeroPress Short Concentrate",
        "ingredients": "20g fine coffee, 120ml water",
        "steps": "Bloom 20s with 40ml, stir, add rest, steep 1:00, press firmly for syrupy shot",
        "brew_time": "1:30"
    },
    {
        "id": 11,
        "method": "AeroPress",
        "name": "AeroPress Bypass Brew",
        "ingredients": "17g medium coffee, 120ml brew water, 80ml bypass water",
        "steps": "Bloom 30s with 40ml, stir 8x, plunge at 1:20, top up with bypass water in mug",
        "brew_time": "2:00"
    },
    {
        "id": 12,
        "method": "AeroPress",
        "name": "AeroPress Metal Filter Brew",
        "ingredients": "16g medium coffee, 220ml water",
        "steps": "Use metal filter, bloom 30s with 50ml, steep 1:30, swirl, press lightly over 45s",
        "brew_time": "2:30"
    },
    {
        "id": 13,
        "method": "V60",
        "name": "V60 Bloom & Pulse",
        "ingredients": "17g medium-fine coffee, 255ml water at 94°C",
        "steps": "Bloom 40s with 45ml, pulse pour 40ml every 20s, finish by 2:50 with gentle swirl",
        "brew_time": "3:00"
    },
    {
        "id": 14,
        "method": "V60",
        "name": "V60 Rao Spin Method",
        "ingredients": "20g medium coffee, 300ml water",
        "steps": "Bloom 45s with 60ml, add remaining water in two 120ml pours with Rao spins, finish at 3:15",
        "brew_time": "3:15"
    },
    {
        "id": 15,
        "method": "V60",
        "name": "V60 Bypass Sweet",
        "ingredients": "16g medium coffee, 220ml brew water, 30ml bypass water",
        "steps": "Bloom 30s with 40ml, pour to 220ml by 2:30, add bypass water to cup, swirl before serving",
        "brew_time": "2:45"
    },
    {
        "id": 16,
        "method": "V60",
        "name": "V60 Iced Concentrate",
        "ingredients": "24g medium-fine coffee, 200ml hot water, 120g ice",
        "steps": "Place ice in server, bloom 30s with 50ml, finish pours by 2:50, swirl to chill",
        "brew_time": "3:00"
    },
    {
        "id": 17,
        "method": "French Press",
        "name": "French Press 3-Stage Stir",
        "ingredients": "28g coarse coffee, 450ml water at 96°C",
        "steps": "Bloom 45s with 100ml, break crust at 2:00, skim foam, steep to 4:30 then plunge slowly",
        "brew_time": "4:30"
    },
    {
        "id": 18,
        "method": "French Press",
        "name": "French Press No-Stir Sweet",
        "ingredients": "32g coarse coffee, 500ml water",
        "steps": "Add coffee then water gently, steep 6 min without stirring, use spoon to break crust, plunge at 6:30",
        "brew_time": "6:30"
    },
    {
        "id": 19,
        "method": "French Press",
        "name": "French Press Metal Mesh Double Filter",
        "ingredients": "30g coarse coffee, 480ml water",
        "steps": "Bloom 30s with 80ml, add rest, steep 4 min, plunge, pour through paper filter for clean cup",
        "brew_time": "4:30"
    },
    {
        "id": 20,
        "method": "French Press",
        "name": "French Press Bold Roast",
        "ingredients": "34g coarse coffee, 520ml water",
        "steps": "Stir after pouring water, steep 5 min, plunge halfway, wait 30s, finish plunge",
        "brew_time": "5:30"
    },
    {
        "id": 21,
        "method": "Cold Brew",
        "name": "Cold Brew Concentrate",
        "ingredients": "120g coarse coffee, 1L cold water",
        "steps": "Combine coffee + water in jar, stir, steep 16-18 hours refrigerated, strain and dilute 1:1",
        "brew_time": "16h-18h"
    },
    {
        "id": 22,
        "method": "Cold Brew",
        "name": "Cold Brew with Citrus",
        "ingredients": "70g coarse coffee, 1L water, 2 strips orange zest",
        "steps": "Add coffee + zest + water, steep 14 hours in fridge, strain, serve over ice",
        "brew_time": "14h"
    },
    {
        "id": 23,
        "method": "Cold Brew",
        "name": "Nitro-Style Cold Brew",
        "ingredients": "80g coarse coffee, 900ml water",
        "steps": "Steep 18 hours, strain, shake vigorously or use whipped cream dispenser for texture",
        "brew_time": "18h"
    },
    {
        "id": 24,
        "method": "Cold Brew",
        "name": "Quick Steep Cold Brew",
        "ingredients": "50g coarse coffee, 600ml water",
        "steps": "Steep 8 hours at room temp, strain through paper filter, chill before serving",
        "brew_time": "8h"
    }
]
