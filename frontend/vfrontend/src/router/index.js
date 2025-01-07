import { createRouter, createWebHistory } from "vue-router";
import Shark from "../components/Shark.vue";
import userLogin from "../components/userLogin.vue";
import HelloWorld from "../components/HelloWorld.vue";
import userHome from "@/components/userComponents/userHome.vue";
import sponsorHome from "@/components/sponsorComponents/sponsorHome.vue";
import { compile } from "vue";
import sponsorRegister from "@/components/sponsorRegister.vue";
import influencerRegister from "@/components/influencerRegister.vue";
import Home from "@/components/landing.vue";
import adminDashboard from "@/components/adminComponents/adminDashboard.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/userLogin",
    name: "userLogin",
    component: userLogin,
  },
  {
    path: "/adminHome",
    name: "adminHome",
    component: adminDashboard,
  },
  {
    path: "/userHome",
    name: "userHome",
    component: userHome,
  },
  {
    path: "/sponsorHome",
    name: "sponsorHome",
    component: sponsorHome,
  },
  {
    path: "/influencerRegister",
    name : "influencerRegister",
    component: influencerRegister,
  },
  {
    path: "/sponsorRegister",
    name: "sponsorRegister",
    component: sponsorRegister,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
