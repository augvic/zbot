import { Controller } from "./src/cortex/controller";

const controller = new Controller();
await controller.init();
controller.run_process();
