const std = @import("std");

const Node = struct {
    data: i32,
    next: ?*Node,
};

fn printList(list: ?*Node) void {

    var it = list;
    while (it) |node| : (it = node.next) {
        std.debug.print("{} ", .{node.data});
    }
    std.debug.print("\n", .{});
}

pub fn main() !void {
    var one   = Node{ .data = 1, .next = null };
    var two   = Node{ .data = 2, .next = null };
    var three = Node{ .data = 3, .next = null };
    var four  = Node{ .data = 4, .next = null };
    var five  = Node{ .data = 5, .next = null };

    one.next = &two;
    two.next = &three;
    three.next = &four;
    four.next = &five;

    var prev: ?*Node= null;
    var curr: ?*Node= &one;
    var next: ?*Node= null;


    printList(curr);
    // 1 2 3 4 5

    while (curr) |_| {
        next = curr.?.next;
        curr.?.next = prev;
        prev = curr;
        curr = next;
    }

    printList(prev);
    // 5 4 3 2 1

}
