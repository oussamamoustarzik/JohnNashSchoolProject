describe("Modules should be loaded by AMD", () => {
  beforeAll(loadGlobals);
  it("jsPDF", () => {
    expect(window.jsPDF).toBeDefined();
  });
  it("canvg", () => {
    expect(window.Canvg).toBeDefined();
  });
});
