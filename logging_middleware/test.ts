import Log from "./logger";

Log("frontend", "info", "config", "Logging middleware initialized successfully")
  .then(() => console.log("Log sent successfully!"))
  .catch((err) => console.log("Error:", err));