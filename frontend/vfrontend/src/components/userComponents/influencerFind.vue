<template>
  <div class="dashboard">
    <!-- Search and Filter Section -->
    <div class="search-filter">
      <input
        type="text"
        placeholder="Search"
        v-model="searchQuery"
        @input="filterCampaigns"
      />
      <button class="filter-button" @click="applyFilter">Filter</button>
    </div>

    <!-- Campaign List -->
    <div class="campaign-list">
      <div
        v-for="(campaign, index) in filteredCampaigns"
        :key="index"
        class="campaign-card"
      >
        <span>{{ campaign.name }} | {{ campaign.description }}</span>
        <div class="buttons">
          <button class="view-button" @click="viewCampaign(campaign)">
            View
          </button>
          <button class="request-button" @click="requestCampaign(campaign.id)">
            Request
          </button>
        </div>
      </div>
    </div>

    <!-- Modal for Viewing Campaign -->
    <div v-if="selectedCampaign" class="modal-overlay">
      <div class="modal">
        <h3>Title: {{ selectedCampaign.name }}</h3>
        <p>Description: {{ selectedCampaign.description }}</p>
        <p>Image: {{ selectedCampaign.image || "<Optional>" }}</p>
        <p>Niche: {{ selectedCampaign.niche }}</p>
        <p>Date: {{ selectedCampaign.date }}</p>
        <div class="modal-buttons">
          <button class="cancel-button" @click="closeModal">Cancel</button>
          <button class="add-button" @click="addCampaign">Add</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "influencerFind",
  data() {
    return {
      searchQuery: "",
      campaigns: [], // Store campaigns fetched from the backend
      filteredCampaigns: [],
      selectedCampaign: null,
    };
  },
  mounted() {
    // Fetch campaigns from the backend when the component mounts
    this.fetchCampaigns();
  },
  methods: {
    async fetchCampaigns() {
      try {
        const response = await axios.get('http://localhost:5000/api/campaigns'); // Assuming the API endpoint for campaigns is /api/campaigns
        this.campaigns = response.data.campaigns;
        this.filteredCampaigns = this.campaigns; // Initialize with full list
      } catch (error) {
        console.error("Error fetching campaigns:", error);
      }
    },
    viewCampaign(campaign) {
      // Set selectedCampaign to show in the modal
      // this.selectedCampaign = campaign;
    },
    requestCampaign(id) {
      console.log(`Request sent for campaign with ID: ${id}`);
      // Implement request logic here if necessary
    },
    filterCampaigns() {
      this.filteredCampaigns = this.campaigns.filter((campaign) =>
        campaign.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    applyFilter() {
      console.log("Filter applied");
      // Implement additional filter logic if needed
    },
    closeModal() {
      // Reset selectedCampaign to hide the modal
      this.selectedCampaign = null;
    },
    addCampaign() {
      console.log(`Campaign ${this.selectedCampaign.name} added successfully!`);
      this.selectedCampaign = null;
    },
  },
};
</script>

<style scoped>
/* Search and Filter */
.search-filter {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin: 20px;
}

.search-filter input {
  padding: 10px;
  width: 200px;
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

.filter-button:hover {
  background-color: #76c776;
}

/* Campaign List */
.campaign-list {
  padding: 20px;
}

.campaign-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.buttons {
  display: flex;
  gap: 10px;
}

.view-button {
  padding: 5px 10px;
  background-color: #f8df7a;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.request-button {
  padding: 5px 10px;
  background-color: #8bd88b;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.view-button:hover {
  background-color: #e7cb6c;
}

.request-button:hover {
  background-color: #76c776;
}

/* Modal Styling */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it's above other content */
}

.modal {
  background-color: #fff;
  padding: 20px;
  width: 400px;
  border-radius: 10px;
  text-align: left;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.cancel-button {
  background-color: #f8cccc;
  padding: 10px 20px;
}

.add-button {
  background-color: #8bd88b;
  padding: 10px 20px;
}
</style>
