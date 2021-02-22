package Test;

module mkCollatzServer(Ifc_type);
  method ActionValue#(Int#(64)) collatz_get();
    let count = 5;
  endmethod

endmodule: mkCollatzServer


endpackage: Test
