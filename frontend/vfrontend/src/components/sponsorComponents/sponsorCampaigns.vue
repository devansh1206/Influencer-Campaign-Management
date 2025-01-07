<template>
    <div class="dashboard">

        <!-- Search and Filter Section -->
        <div class="search-filter">
            <input type="text" placeholder="Search" v-model="searchQuery" @input="filterCampaigns" />
            <button class="filter-button" @click="applyFilter">Filter</button>
        </div>

        <!-- Campaign Cards -->
        <div class="campaign-cards">
            <div v-for="(campaign, index) in filteredCampaigns" :key="index" class="campaign-card"
                @click="viewDetails(campaign)">
                <div class="card-header">
                    <h3>{{ campaign.name }}</h3>
                </div>
                <div class="card-body">
                    <p>{{ campaign.description }}</p>
                </div>
                <div class="card-footer">
                    <span>Start: {{ campaign.start_date }}</span>
                    <span>End: {{ campaign.end_date }}</span>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import changeTab from './sponsorHome.vue';
export default {
    name: "sponsorCampaigns",
    data() {
        return {
            searchQuery: "",
            campaigns: this.$store.state.user.sponsor_campaign,
            filteredCampaigns: [],
        };
    },
    mounted() {
        this.filteredCampaigns = this.campaigns; // Initialize with all campaigns
    },
    methods: {
        filterCampaigns() {
            this.filteredCampaigns = this.campaigns.filter((campaign) =>
                campaign.name.toLowerCase().includes(this.searchQuery.toLowerCase())
            );
        },
        applyFilter() {
            alert("Filter function triggered!");
        },
        viewDetails(campaign) {
            alert(`Viewing details for ${campaign.name}`);
        },
    },
};
</script>

<style scoped>
/* General Styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Search and Filter Section */
.search-filter {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin: 20px;
}

.search-filter input {
    padding: 10px;
    width: 250px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.filter-button {
    padding: 10px 20px;
    background-color: #8bd88b;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Campaign Cards */
.campaign-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive card grid */
    gap: 20px;
    padding: 20px;
}

.campaign-card {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
    cursor: pointer;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 300px; /* Fixed height for consistent card size */
}

.campaign-card:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.card-header {
    background-color: #f5f5f5;
    padding: 15px;
    border-bottom: 1px solid #ddd;
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
}

.card-body {
    padding: 15px;
    flex-grow: 1;
    font-size: 0.95rem;
    color: #333;
}

.card-footer {
    background-color: #f5f5f5;
    padding: 10px 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #ddd;
    font-size: 0.85rem;
    color: #777;
}

/* Add Button */
.add-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    background-color: #ffcc00;
    border: none;
    border-radius: 50%;
    font-size: 24px;
    color: #fff;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s, box-shadow 0.2s;
}

.add-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}
</style>
