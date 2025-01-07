
<template>
    <div>
        <div>
            <!-- nav bar -- profile, campaigns, Find, Status, Logout-->
    
            <!-- Welcome sponsor name -->
            <!-- Active campaigns -->
                <!-- Campaign quick info, View button for details -->
            <!-- New Requests -->
                <!-- New requests quick info, view, accept, reject buttons -->
            
        
        </div>
    <div>
        <nav class="navbar">
            <ul>
            <li><a href="#" @click.prevent="changeTab('profile')">Profile</a></li>
            <li><a href="#" @click.prevent="changeTab('campaigns')">Campaigns</a></li>
            <li><a href="#" @click.prevent="changeTab('find')">Find</a></li>
            <li><a href="#" @click.prevent="changeTab('stats')">Stats</a></li>
            <li><a href="#" @click.prevent="changeTab('addCampaign')">addCampaign</a></li>
            <li><a href="#" @click.prevent="logout">Logout</a></li>
            </ul>
        </nav>
    </div>

    <div v-if="selectedTab === 'profile'">
        <sponsorDashboard />
    </div>
    <div v-if="selectedTab === 'campaigns'">
        <sponsorCampaigns></sponsorCampaigns>
    </div>
    <div v-if="selectedTab === 'find'">
        <sponsorFind></sponsorFind>
    </div>
    <div v-if="selectedTab === 'stats'">
        <sponsorStats></sponsorStats>
    </div>
    <div v-if="selectedTab=== 'addCampaign'">
        <addCampaign></addCampaign>
    </div>
    <div v-if="selectedTab === 'logout'">
        <p>logout functionality here</p>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import sponsorCampaigns from './sponsorCampaigns.vue';
import sponsorDashboard from './sponsorDashboard.vue';
import sponsorFind from './sponsorFind.vue';
import sponsorStats from './sponsorStats.vue';
import addCampaign from './addCampaign.vue';

export default {
    neme: "sponsorHome",
    components : {
        sponsorCampaigns,
        sponsorDashboard,
        sponsorFind,
        sponsorStats, 
        addCampaign,
    },
    data () {
        return {
            selectedTab : 'profile',
        }
    },
    methods : {
        changeTab(tab){
            this.selectedTab=tab;
        },
        logout() {
            this.$store.dispatch('logout'); // Dispatch the logout action
            this.$router.push('/userLogin'); // Redirect to login page after logout
        }
    },
    
}
</script>

<style>
.content {
    padding: 20px;
  }
  
  .profile-section {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
  }
  
  .profile-pic {
    width: 100px;
    height: 100px;
    background-color: #b2d4b2;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
  }
  
  .profile-info {
    font-size: 14px;
  }
  
  .campaign-card,
  .request-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  button {
    padding: 5px 10px;
    margin-left: 10px;
    border: none;
    cursor: pointer;
    border-radius: 3px;
  }
  
  .view-button {
    background-color: #f8df7a;
  }
  
  .accept-button {
    background-color: #8bd88b;
  }
  
  .reject-button {
    background-color: #f58a8a;
  }
  </style>