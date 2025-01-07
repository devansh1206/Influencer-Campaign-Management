<template>
    <div class="add-campaign">
        <h1>Add New Campaign</h1>

        <form @submit.prevent="submitForm">
            <div>
                <label for="name">Campaign Name:</label>
                <input v-model="campaign.name" type="text" id="name" required />
            </div>

            <div>
                <label for="description">Description:</label>
                <textarea v-model="campaign.description" id="description" required></textarea>
            </div>

            <div>
                <label for="start_date">Start Date:</label>
                <input v-model="campaign.start_date" type="date" id="start_date" required />
            </div>

            <div>
                <label for="end_date">End Date:</label>
                <input v-model="campaign.end_date" type="date" id="end_date" required />
            </div>

            <div>
                <label for="budget">Budget:</label>
                <input v-model="campaign.budget" type="number" id="budget" required />
            </div>

            <div>
                <label for="visibility">Visibility:</label>
                <select v-model="campaign.visibility" id="visibility" required>
                    <option value="public">Public</option>
                    <option value="private">Private</option>
                </select>
            </div>

            <div>
                <label for="goals">Goals:</label>
                <input v-model="campaign.goals" type="text" id="goals" />
            </div>

            <button type="submit">Add Campaign</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "addCampaign",
    data() {
        return {
            campaign: {
                name: "",
                description: "",
                start_date: "",
                end_date: "",
                budget: 0,
                visibility: "public",
                goals: "",
                sponsor_id: this.$store.state.user.sponsor.id,
            },
        };
    },
    methods: {
        // Fetch sponsors to populate the sponsor dropdown
        // async fetchSponsors() {
        //     try {
        //         const response = await axios.get("http://localhost:5000/api/sponsors", {
        //             headers: {
        //                 Authorization: `Bearer ${localStorage.getItem('token')}`,
        //             },
        //         });
        //         if (response.data.success) {
        //             this.sponsors = response.data.sponsors;
        //         }
        //     } catch (error) {
        //         console.error("Error fetching sponsors:", error);
        //     }
        // },
        // Submit form to add a new campaign
        async submitForm() {
            try {
                const response = await axios.post("http://localhost:5000/api/add_campaign", this.campaign, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    },
                });
                if (response.data.success) {
                    alert("Campaign added successfully!");

                    this.update_campaigns();
                    // this.$router.push('/sponsorHome'); // Navigate to campaign list or another page after adding
                } else {
                    alert("Error adding campaign: " + response.data.message);
                }
            } catch (error) {
                console.error("Error adding campaign:", error);
            }
        },
        async update_campaigns(){
            const id = this.$store.state.user.sponsor.id;
            const res = await axios.get(`http://localhost:5000/api/get_sponsor_campaign/${id}`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            })
            console.log(res);
            this.$store.commit("set_sponsor_campaigns", res.data.sponsor_campaigns)
        }
    },
};
</script>

<style scoped>
.add-campaign {
    padding: 20px;
}

form div {
    margin-bottom: 10px;
}

label {
    display: block;
    font-weight: bold;
}

input, textarea, select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}

button {
    padding: 10px 20px;
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}
</style>
