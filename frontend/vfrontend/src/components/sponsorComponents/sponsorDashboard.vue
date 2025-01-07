<template>

    <!-- Main Section -->
    <div class="content">

        <!-- Welcome Message -->
        <h2 class="welcome-message">Welcome, {{ user.sponsor.full_name }}</h2>

        <!-- Active Campaigns -->
        <div class="campaigns">
            <h3 class="section-title">Active Campaigns:</h3>
            <div v-for="(campaign, index) in activeCampaigns" :key="index" class="campaign-card">
                <div class="campaign-info">
                    <h4>{{ campaign.name }}</h4>
                    <p>Budget: ₹ {{ campaign.budget }}</p>
                </div>
                <button class="view-button">View</button>
            </div>
        </div>

        <!-- New Requests -->
        <div class="new-requests">
            <h3 class="section-title">New Requests:</h3>
            <div v-for="(request, index) in newRequests" :key="index" class="request-card">
                <div class="request-info">
                    <h4>{{ request.campaign.name }}</h4>
                    <p>From: {{ request.campaign.sponsor.full_name }}</p>
                </div>
                <div class="request-actions">
                    <button class="view-button" @click="viewRequest(request.id)">View</button>
                    <button class="accept-button" @click="acceptRequest(request.id)">Accept</button>
                    <button class="reject-button" @click="rejectRequest(request.id)">Reject</button>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "influencerDashboard",
    data() {
        return {
            activeCampaigns: [],  // Start with an empty array
        }
    },
    computed: {
        user() {
            return this.$store.state.user;  // Access user from Vuex store
        },
        activeCampaigns() {
            return this.user && this.user.sponsor_campaign ? this.user.sponsor_campaign : [];  // Check if campaigns exist
        }
    },
    mounted() {
        this.user;  // Access the user data on mount
    }
}
</script>

<style scoped>
/* Overall Page Styling */
.content {
    padding: 20px;
    max-width: 900px;
    margin: 0 auto;
    font-family: 'Arial', sans-serif;
}

/* Welcome Message */
.welcome-message {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
}

/* Section Title */
.section-title {
    font-size: 20px;
    margin-bottom: 15px;
}

/* Campaign and Request Cards */
.campaign-card,
.request-card {
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: transform 0.2s ease;
}

.campaign-card:hover,
.request-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* Campaign Info Styling */
.campaign-info,
.request-info {
    display: flex;
    flex-direction: column;
}

.campaign-info h4,
.request-info h4 {
    margin: 0;
    font-size: 18px;
    color: #333;
}

.campaign-info p,
.request-info p {
    margin: 5px 0 0 0;
    color: #666;
    font-size: 14px;
}

/* Request Actions */
.request-actions {
    display: flex;
    gap: 10px;
}

/* Buttons */
button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    color: #fff;
    transition: background-color 0.2s ease;
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

button:hover {
    opacity: 0.9;
}
</style>
