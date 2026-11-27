import react from "@vitejs/plugin-react";
import { defineConfig } from "vitest/config";

export default defineConfig({
  base: process.env.GITHUB_ACTIONS === "true" ? "/EratoFun/" : "/",
  plugins: [react()],
  test: {
    environment: "node",
  },
});
