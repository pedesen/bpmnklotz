include <./aruco.scad>;
$fn=120;
extrusion_height=1;
coaster_height=5;
name_font="DejaVu Serif:style=Condensed Bold";

id_exclusive = 41;
id_inclusive = 40;
id_start = 0;
id_end = 2;
id_service = 1;
id_user = 3;

module gateway(name, symbol, text_color="black", color="gold", symbol_font="bpmn") {
    s = 58;
    d = s * sqrt(2);
    color(color) rotate(45) minkowski()
    {
        cube([s, s, coaster_height/2]);
        cylinder(r=2, h=coaster_height/2);
    };
    
    color(text_color)
    translate([0, 0, coaster_height]) 
    linear_extrude(extrusion_height) {
        translate([0, d / 2, 0])
            text(symbol, size=24, halign="center", valign="center", font=symbol_font);
        translate([0, d / 2 - 24, 0])
            text(name, size=5.5, halign="center", font=name_font);
        
        translate([0, d / 2 + 26, 0]) rotate(45) scale(0.7) draw_aruco(name);
    }      
}
// test:
// gateway("inclusive", "");

module event(name, symbol, text_color="black", color="gold", symbol_font="bpmn") {
    color(color) cylinder(r=25, h=coaster_height, center=false);
    
    color(text_color)
    translate([0, 0, coaster_height]) {
         linear_extrude(extrusion_height) {
             text(symbol, size=15, halign="center", valign="center", font=symbol_font);
             
             translate([0, -18, 0]) text(name, size=6, halign="center", font=name_font);
             
             translate([0, 17, 0]) scale(0.7) draw_aruco(name);
         }
    }
}

// test:
// event("start", "");

module task(name, symbol, text_color="black", color="gold", symbol_font="bpmn") {
    color(color) minkowski() {
        cube([68, 48, coaster_height/2]);
        cylinder(r=2, h=coaster_height/2);
    }

    color(text_color)
    translate([0, 0, coaster_height]) {
         linear_extrude(extrusion_height) {
             translate([5, 42, 0])
                text(symbol, size=10, halign="center", valign="center", font=symbol_font);
             
             translate([0, 0, 0]) text(name, size=6);
             translate([60, 8, 0]) draw_aruco(name);
         }
    }
}