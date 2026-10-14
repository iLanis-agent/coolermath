// Cooler math - ice retention honesty.
// The 5-day sticker is a lab at 75 F with the lid closed and the cooler
// pre-chilled. The sun, the lid and the warm six-pack all drink from the
// same ice.
// Verdicts judge the unrounded figure; rounding is for display only.
var CoolerMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function num(x) { return typeof x === "number" && isFinite(x) && x >= 0; }
  function r1(x) { return Math.round(x * 10) / 10; }

  function icePlan(stickerDays, ambientF, opensPerDay) {
    if (!pos(stickerDays)) return { error: "the sticker days must be above zero" };
    if (!num(ambientF)) return { error: "the temperature must be a number" };
    if (!num(opensPerDay)) return { error: "the lid opens must be zero or more" };
    // Labeled norms: 8% off per 5 F above 75 (floor 40% kept);
    // each lid open costs 2% of a sticker day.
    var t = Math.max(0.4, 1 - Math.max(0, ambientF - 75) * 0.016);
    var days = stickerDays * t * (1 - 0.02 * opensPerDay);
    if (days <= 0) days = 0.2;
    return { days: r1(days) };
  }

  function renderIce(r, stickerDays, ambientF, opensPerDay) {
    return "Your " + stickerDays + "-day sticker at " + ambientF + " F with the lid up " + opensPerDay
      + " times a day figures about " + r.days + " days - the lab kept the lid closed in a 75-degree room.";
  }

  function loadPlan(contentsLb) {
    if (!pos(contentsLb)) return { error: "the contents weight must be above zero" };
    // Labeled norm: the 2:1 rule, ice to contents by weight.
    var ice = contentsLb * 2;
    return { ice: r1(ice) };
  }

  function renderLoad(r, contentsLb) {
    return "Your " + contentsLb + " lb of food and cans wants about " + r.ice
      + " lb of ice - the 2:1 rule counts the beer too.";
  }

  function blockPlan(cubeDays) {
    if (!pos(cubeDays)) return { error: "the cube days must be above zero" };
    // Labeled norm: a solid block outlasts cubes by half again - fewer edges.
    var days = cubeDays * 1.5;
    return { days: r1(days) };
  }

  function renderBlock(r, cubeDays) {
    return "Your " + cubeDays + " days of cubes becomes about " + r.days
      + " days as one block - same pounds, fewer edges.";
  }

  return {
    icePlan: icePlan, renderIce: renderIce,
    loadPlan: loadPlan, renderLoad: renderLoad,
    blockPlan: blockPlan, renderBlock: renderBlock
  };
})();
if (typeof module !== "undefined") module.exports = CoolerMath;
