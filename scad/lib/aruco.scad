diameter = 50;
aruco_data_height= 1;
tol = 0.15;
white_cube_face_height = 2;
safety_margin = 0.1;

/////////////////////////// no touching
radius = diameter/2;
cw = radius/9;


module aruco_content(black_cube, row, col, color=1){
    if (black_cube == color){
        translate([cw*(row+1), cw*(col+1)])
        square([cw + safety_margin,cw + safety_margin]);
    }
}

module aruco_frame() {
    difference() {
        square([cw*(4+2), cw*(4+2)]); // must fit in face_intrusion
        translate([cw, cw, 0]) square([cw*4, cw*4]);
    }
}

// use https://chev.me/arucogen/ to generate the marker data
module draw_marker(data, color=1) {
    translate([-cw*(4+2)/2, -cw*(4+2)/2, 0]){
        aruco_frame();
        
        idx = [0:3];
        for(row = idx) {
            for(col = idx){
                aruco_content(data[row][col], row, col, color=color);
            }
        }
    }
}