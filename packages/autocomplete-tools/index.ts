#! /usr/bin/env node
import { Command } from "commander";

const program = new Command();

program
  .version("1.0.0")
  .command("init", "install one or more packages", {
    executableFile: "scripts/init.sh",
  })
  .command("create-spec [name]", "search with optional query", {
    executableFile: "scripts/create-spec.sh",
  })
  .command("compile", "compile specs in the current directory", {
    executableFile: "scripts/compile",
  })
  .command("dev", "watch for changes and compile specs", {
    executableFile: "scripts/dev.sh",
  });

program.parse(process.argv);
