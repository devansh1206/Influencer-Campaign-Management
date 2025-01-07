<template>
    <div class="admin-dashboard">
        <!-- Navbar for switching tabs -->
        <nav class="navbar">
            <ul>
                <li :class="{ active: activeTab === 'info' }" @click="activeTab = 'info'">Users</li>
                <li :class="{ active: activeTab === 'campaigns' }" @click="activeTab = 'campaigns'">Campaigns</li>
                <li :class="{ active: activeTab === 'find' }" @click="activeTab = 'find'">Find</li>
                <li :class="{ active: activeTab === 'stats' }" @click="activeTab = 'stats'">Stats</li>
                <li @click="logout">Logout</li>
            </ul>
        </nav>

        <!-- Display content based on the selected tab -->
        <div class="content">
            <div v-if="activeTab === 'info'">
                <!-- Info tab content (User details) -->
                <h1>Manage Users</h1>
                <div v-if="users.length > 0">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Username</th>
                                <th>Email</th>
                                <th>Status</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="user in users" :key="user.id">
                                <td>{{ user.id }}</td>
                                <td>{{ user.username }}</td>
                                <td>{{ user.email }}</td>
                                <td>
                                    Approved: {{ user.is_active ? 'Yes' : 'No' }} | 
                                    Flagged: {{ user.flagged ? 'Yes' : 'No' }}
                                </td>
                                <td>
                                    <button v-if="!user.is_active" @click="approveUser(user.id)">Approve</button>
                                    <button style="background-color:red;" v-else @click="unapproveUser(user.id)">Unapprove</button>
                                    &emsp;
                                    <button style="background-color:red;" v-if="!user.flagged" @click="flagUser(user.id)">Flag</button>
                                    <button v-else @click="unflagUser(user.id)">Unflag</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-else>
                    <p>No users found.</p>
                </div>
            </div>

            <div v-if="activeTab === 'campaigns'">
                <adminCampaigns></adminCampaigns>
                
            </div>
            <div v-if="activeTab === 'find'">
                <!-- Find tab content -->
                <h1>Find Section</h1>
                <p>This could be a search for campaigns, users, or other data.</p>
            </div>

            <div v-if="activeTab === 'stats'">
                <!-- Stats tab content -->
                <h1>Statistics</h1>
                <p>Here you can display various stats such as number of users, campaigns, etc.</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import adminCampaigns from "./adminCampaigns.vue";
export default {
    name: "adminDashboard",
    data() {
        return {
            activeTab: "info", // Default tab is 'info'
            users: [], // User data will be fetched and stored here
        };
    },
    components:{
        adminCampaigns,
    },
    methods: {
        // Fetch all users
        async fetchUsers() {
            try {
                const response = await axios.get("http://localhost:5000/api/users", {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`, // Assuming auth_token is stored in localStorage
                    },
                });
                if (response.data.success) {
                    this.users = response.data.users;
                } else {
                    console.error("Error fetching users:", response.data.message);
                }
            } catch (error) {
                console.error("Error fetching users:", error);
            }
        },

        // Approve user
        async approveUser(user_id) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/approve_user/${user_id}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );

                if (response.data.success) {
                    console.log(response.data.message);
                    this.updateUserStatus(user_id, 'is_active', true);
                    alert(`User with ID: ${user_id} approved successfully!`);
                } else {
                    alert(`Failed to approve user: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error approving user:", error);
            }
        },

        // Unapprove user
        async unapproveUser(userId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/unapprove_user/${userId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateUserStatus(userId, 'is_active', false);
                    alert(`User with ID: ${userId} unapproved successfully!`);
                } else {
                    alert(`Failed to unapprove user: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error unapproving user:", error);
            }
        },

        // Flag user
        async flagUser(userId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/flag_user/${userId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateUserStatus(userId, 'flagged', true);
                    alert(`User with ID: ${userId} flagged successfully!`);
                } else {
                    alert(`Failed to flag user: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error flagging user:", error);
            }
        },

        // Unflag user
        async unflagUser(userId) {
            try {
                const response = await axios.post(
                    `http://localhost:5000/api/unflag_user/${userId}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                if (response.data.success) {
                    this.updateUserStatus(userId, 'flagged', false);
                    alert(`User with ID: ${userId} unflagged successfully!`);
                } else {
                    alert(`Failed to unflag user: ${response.data.message}`);
                }
            } catch (error) {
                console.error("Error unflagging user:", error);
            }
        },

        // Update the status of a user in the users array
        updateUserStatus(userId, field, value) {
            const userIndex = this.users.findIndex((user) => user.id === userId);
            if (userIndex !== -1) {
                // this.$set(this.users[userIndex], field, value);
                this.users[userIndex][field] = value;
            }
        },

        // Logout function
        logout() {
            this.$store.dispatch('logout'); // Dispatch the logout action
            this.$router.push('/userLogin'); // Redirect to login page after logout
        }
    },
    mounted() {
        this.fetchUsers();
    },
};
</script>

<style scoped>
.admin-dashboard {
    padding: 20px;
}

.navbar {
    background-color: #333;
    padding: 10px;
}

.navbar ul {
    display: flex;
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.navbar ul li {
    color: #fff;
    padding: 10px 20px;
    cursor: pointer;
    background-color: #444;
    margin-right: 10px;
    border-radius: 5px;
}

.navbar ul li.active {
    background-color: #ff8c00;
}

.navbar ul li:hover {
    background-color: #666;
}

.content {
    margin-top: 20px;
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
