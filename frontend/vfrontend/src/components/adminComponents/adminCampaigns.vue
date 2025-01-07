<template>
    <div class="campaign-management">
        <!-- Display content for managing campaigns -->
        <h1>Manage Campaigns</h1>
        <div v-if="campaigns.length > 0">
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="campaign in campaigns" :key="campaign.id">
                        <td>{{ campaign.id }}</td>
                        <td>{{ campaign.name }}</td>
                        <td>{{ campaign.description }}</td>
                        <td>
                            Approved: {{ campaign.is_active ? 'Yes' : 'No' }} | 
                            Flagged: {{ campaign.flagged ? 'Yes' : 'No' }}
                        </td>
                        <td>
                            <button v-if="!campaign.is_active" @click="approveCampaign(campaign.id)">Approve</button>
                            <button style="background-color:red;" v-else @click="unapproveCampaign(campaign.id)">Unapprove</button>
                            &emsp;
                            <button style="background-color:red;" v-if="!campaign.flagged" @click="flagCampaign(campaign.id)">Flag</button>
                            <button v-else @click="unflagCampaign(campaign.id)">Unflag</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
            <p>No campaigns found.</p>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "adminCampaigns",
    data() {
        return {
            campaigns: [], // Campaign data will be fetched and stored here
        };
    },
    methods: {
        // Fetch all campaigns
        async fetchCampaigns() {
            try {
                const response = await axios.get("http://localhost:5000/api/campaigns", {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`, // Assuming JWT is stored in localStorage
                    },
                });
                if (response.data.success) {
                    this.campaigns = response.data.campaigns;
                } else {
                    console.error("Error fetching campaigns:", response.data.message);
                }
            } catch (error) {
                console.error("Error fetching campaigns:", error);
            }
        },

        // Approve campaign
        async approveCampaign(campaignId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/approve_campaign/${campaignId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateCampaignStatus(campaignId, 'is_active', true);
                    alert(`Campaign with ID: ${campaignId} approved successfully!`);
                } else {
                    alert(`Failed to approve campaign: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error approving campaign:", error);
            }
        },

        // Unapprove campaign
        async unapproveCampaign(campaignId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/unapprove_campaign/${campaignId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateCampaignStatus(campaignId, 'is_active', false);
                    alert(`Campaign with ID: ${campaignId} unapproved successfully!`);
                } else {
                    alert(`Failed to unapprove campaign: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error unapproving campaign:", error);
            }
        },

        // Flag campaign
        async flagCampaign(campaignId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/flag_campaign/${campaignId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateCampaignStatus(campaignId, 'flagged', true);
                    alert(`Campaign with ID: ${campaignId} flagged successfully!`);
                } else {
                    alert(`Failed to flag campaign: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error flagging campaign:", error);
            }
        },

        // Unflag campaign
        async unflagCampaign(campaignId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/unflag_campaign/${campaignId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateCampaignStatus(campaignId, 'flagged', false);
                    alert(`Campaign with ID: ${campaignId} unflagged successfully!`);
                } else {
                    alert(`Failed to unflag campaign: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error unflagging campaign:", error);
            }
        },

        // Update the status of a campaign in the campaigns array
        updateCampaignStatus(campaignId, field, value) {
            const campaignIndex = this.campaigns.findIndex((campaign) => campaign.id === campaignId);
            if (campaignIndex !== -1) {
                this.campaigns[campaignIndex][field] = value;
            }
        }
    },
    mounted() {
        this.fetchCampaigns();
    },
};
</script>

<style scoped>
.campaign-management {
    padding: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

table,
th,
td {
    border: 1px solid #ddd;
}

th,
td {
    padding: 12px;
    text-align: left;
}

button {
    padding: 5px 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
</style>
