package CollatzServer;

module mkTb(Empty);

  rule run();
    ifc.collatz_submit(989345275647);
  endrule

endmodule: mkTb

endpackage: CollatzServer
