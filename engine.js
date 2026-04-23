const Game = {

  tickSpeed: 1500,

  chains: {
    A: { name: "Alpha", type: "POS", health: 80, forked: false },
    B: { name: "Beta", type: "POW", health: 70, forked: false }
  },

  global: {
    day: 1,
    chaos: 10,
    globalStability: 75,
    events: [],
  },

  start() {
    this.log("🌌 L1 Reality Engine Activated");
    setInterval(() => this.tick(), this.tickSpeed);
    setInterval(() => this.chaosEvent(), 4000);
  },

  // =========================
  // MAIN SIMULATION LOOP
  // =========================
  tick() {
    this.global.day++;

    Object.keys(this.chains).forEach(id => {
      let c = this.chains[id];

      // BASE DECAY
      c.health -= this.global.chaos * 0.05;

      // CONSENSUS BEHAVIOR
      if (c.type === "POS") {
        c.health += 0.5;
      } else {
        c.health -= 0.3;
      }

      // FORK INSTABILITY
      if (c.health < 40 && !c.forked) {
        this.forkChain(id);
      }

      if (c.health < 0) c.health = 0;
    });

    // GLOBAL STABILITY
    let avg = Object.values(this.chains)
      .reduce((a, b) => a + b.health, 0) / Object.keys(this.chains).length;

    this.global.globalStability = avg - this.global.chaos;

    this.log(`📦 Day ${this.global.day} | Stability: ${this.global.globalStability.toFixed(1)}`);

    this.render();
  },

  // =========================
  // FORK SYSTEM (INSANE FEATURE)
  // =========================
  forkChain(id) {
    let newId = id + "_FORK_" + Math.floor(Math.random() * 1000);

    this.chains[newId] = {
      name: this.chains[id].name + " Fork",
      type: this.chains[id].type === "POS" ? "POW" : "POS",
      health: 60,
      forked: true
    };

    this.log(`🧬 FORK CREATED: ${newId}`);
  },

  // =========================
  // CHAOS ENGINE
  // =========================
  chaosEvent() {
    const events = [
      () => this.global.chaos += 2,
      () => this.global.chaos -= 1,
      () => Object.values(this.chains)[0].health -= 10,
      () => this.log("⚠️ Validator rebellion detected"),
      () => this.log("🔥 Mempool congestion spike"),
      () => this.log("💣 51% attack simulation triggered")
    ];

    let ev = events[Math.floor(Math.random() * events.length)];
    ev();
  },

  // =========================
  // ACTIONS
  // =========================
  stabilize() {
    this.global.chaos -= 5;
    this.log("🛠 Global stabilization protocol executed");
  },

  upgradeChain(id) {
    if (this.chains[id]) {
      this.chains[id].health += 10;
      this.log(`⬆️ Chain ${id} upgraded`);
    }
  },

  // =========================
  // LOG SYSTEM
  // =========================
  log(msg) {
    if (!this.global.events) this.global.events = [];
    this.global.events.unshift(msg);
    if (this.global.events.length > 12) this.global.events.pop();
  },

  // =========================
  // RENDER HOOK
  // =========================
  render() {
    if (typeof updateUI === "function") {
      updateUI(this);
    }
  }
};
