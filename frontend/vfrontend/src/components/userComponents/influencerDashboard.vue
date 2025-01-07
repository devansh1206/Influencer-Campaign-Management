<template>
    <div>
      <div class="dashboard">
        
        <!-- Main Section -->
        <div class="content">
          <!-- Profile Section -->
          <div class="profile-section">
            <div class="profile-pic">Profile Pic</div>
            <div class="profile-info">
              <p><strong>Rating:</strong> 5</p>
              <p><strong>Earnings this month:</strong> $500</p>
            </div>
          </div>
    
          <!-- Welcome Message -->
          <h2>Welcome,  {{ user.influencer.full_name }} </h2>
    
          <!-- Active Campaigns -->
          <div class="campaigns">
            <h3>Active Campaigns:</h3>
            <div v-for="(campaign, index) in user.active_campaigns" :key="index" class="campaign-card">
              <span>{{ campaign.name }} | Progress {{ campaign.progress }}%</span>
              <button class="view-button" @click="viewCampaign(campaign.id)">View</button>
            </div>
            <p v-if="user.active_campaigns.length==0"> No active campaign! </p>
          </div>
    
          <!-- New Requests -->
          <div class="new-requests">
            <h3>New Requests:</h3>
            <div v-for="(request, index) in user.new_requests" :key="index" class="request-card">
              <span>{{ request.name }} | {{ request.company }}</span>
              <button class="view-button" @click="viewRequest(request.id)">View</button>
              <button class="accept-button" @click="acceptRequest(request.id)">Accept</button>
              <button class="reject-button" @click="rejectRequest(request.id)">Reject</button>
            </div>
            <p v-if="user.new_requests.length==0"> No new request! </p>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    neme: "influencerDashboard",
    data () {
        return {
          // activeCampaigns: [
          //   { id: 1, name: "Campaign 01", progress: 10 },
          //   { id: 2, name: "Campaign 02", progress: 40 },
          // ],
          // newRequests: [
          //   { id: 3, name: "Campaign 04", company: "Company 01" },
          //   { id: 4, name: "Campaign 05", company: "Company 01" },
          // ],
        }
    },
    methods : {
      viewCampaign(id) {
        // alert("Viewing details for campaign with ID: ", ${id});
        // Implement view logic here (e.g., routing or modal)
      },
      viewRequest(id) {
        // alert("Viewing request details with ID: ", ${id});
        // Implement view logic here (e.g., routing or modal)
      },
      acceptRequest(id) {
        // alert("Accepted request with ID: ", ${id});
        // Implement accept logic here (e.g., API call or state update)
        this.newRequests = this.newRequests.filter((request) => request.id !== id);
      },
      rejectRequest(id) {
        // alert("Rejected request with ID: ", ${id});
        // Implement reject logic here (e.g., API call or state update)
        this.newRequests = this.newRequests.filter((request) => request.id !== id);
      },

    },
    computed :{
        user(){
            return this.$store.state.user;
        },
    },
    mounted(){
      this.user;
    }
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