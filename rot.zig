const std = @import("std");

pub fn main() void {
    var kek = [6]u8{1,2,3,4,5,6};
    const n: u32 = 2;
    var i: u32 = 1;

    while (i <= n) : (i += 1) {

        var j: u32 = 1;
        var first = kek[0];

        while (j < kek.len) : (j += 1) {
            kek[j-1] = kek[j];
        }
            kek[kek.len-1] = first;

    }

    std.debug.print("{any}", .{kek});
}
