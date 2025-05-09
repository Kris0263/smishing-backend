import "dotenv/config";
import express from "express";
import connectDB from "./configs/db.config.js";
import authRoute from "./routes/auth.route.js";
import policyRoute from "./routes/policy.routes.js";
import dashboardRoutes from "./routes/dashboard.route.js";
import authenticate from "./middleware/authenticate.js";

const app = express();
app.use(express.json());

// Connect to MongoDB
connectDB();

app.use("/dashboard", authenticate, dashboardRoutes);

// Mount auth routes at /api/auth
app.use("/api/auth", authRoute);

// Mount auth routes at /api/auth
app.use("/api/auth", authRoute);

// Mount policy routes at /api/policy
app.use("/api/policy", policyRoute); // 👈 mount the router

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

export default app;
