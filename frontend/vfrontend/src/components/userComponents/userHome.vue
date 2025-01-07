<template>
    <div>
        <div>
            <nav class="navbar">
              <ul>
                <li><a href="#" @click.prevent="changeTab('profile')">Profile</a></li>
                <li><a href="#" @click.prevent="changeTab('find')">Find</a></li>
                <li><a href="#" @click.prevent="changeTab('stats')">Stats</a></li>
                <li><a href="#" @click.prevent="logout">Logout</a></li>
              </ul>
            </nav>
        </div>
        
        <div v-if="selectedTab === 'profile'">
            <influencerDashboard />
        </div>
        <div v-if="selectedTab === 'find'">
            <influencerFind></influencerFind>
        </div>
        <div v-if="selectedTab === 'stats'">
            <influencerStats></influencerStats>
        </div>
        <div v-if="selectedTab === 'logout'">
        </div>
    </div>
</template>

<script>
import influencerDashboard from './influencerDashboard.vue';
import influencerFind from './influencerFind.vue';
import influencerStats from './influencerStats.vue';

export default {
    name : "influencerHome",
    components: {
        // influencerNav,
        influencerDashboard,
        influencerFind,
        influencerStats,
    },
    data () {
        return{
            selectedTab: "profile",
        }
    },
    methods:{
        changeTab(tab){
            this.selectedTab = tab;
        },
        logout() {
            this.$store.dispatch('logout'); // Dispatch the logout action
            this.$router.push('/userLogin'); // Redirect to login page after logout
        }
    },
    computed :{
        user(){
            return this.$store.state.user;
        }
    },
    mounted (){
        this.user;
    },
}
</script>

<style>
.navbar {
    display: flex;
    justify-content: space-around;
    background-color: #f4f4f4;
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .navbar ul {
    list-style: none;
    display: flex;
    gap: 20px;
  }
  
  .navbar li {
    display: inline;
  }
  
  .navbar a {
    text-decoration: none;
    color: #333;
  }
</style>