boolean b = false;
b = true;

boolean toBe = false;
b = toBe || !toBe;
if (b) {
    System.out.println(toBe);
}

int children = 0;
b = children; // Will not work
if (children) { // Will not work
    // Will not work
}