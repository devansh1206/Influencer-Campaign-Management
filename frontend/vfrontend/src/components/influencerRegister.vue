<template>
    <div class="container mt-5">
        <div class="card shadow-sm">
            <div class="card-header bg-primary text-white text-center">
                <h2>Register as Influencer</h2>
            </div>
            <div class="card-body">
                <form @submit.prevent="registerInfluencer">
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" v-model="form.email" required class="form-control" id="email" placeholder="Enter email" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="password">Password</label>
                        <input type="password" v-model="form.password" required class="form-control" id="password" placeholder="Enter password" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="fullName">Full Name</label>
                        <input type="text" v-model="form.full_name" required class="form-control" id="fullName" placeholder="Enter your full name" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="phone">Phone</label>
                        <input type="text" v-model="form.phone" class="form-control" id="phone" placeholder="Enter phone number" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="address">Address</label>
                        <input type="text" v-model="form.address" class="form-control" id="address" placeholder="Enter your address" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="category">Category</label>
                        <input type="text" v-model="form.category" class="form-control" id="category" placeholder="Enter category" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="niche">Niche</label>
                        <input type="text" v-model="form.niche" class="form-control" id="niche" placeholder="Enter your niche" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="profilePicture">Profile Picture URL</label>
                        <input type="text" v-model="form.profile_picture" class="form-control" id="profilePicture" placeholder="Enter profile picture URL" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="twitterHandle">Twitter Handle</label>
                        <input type="text" v-model="form.twitter_handle" class="form-control" id="twitterHandle" placeholder="Enter Twitter handle" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="twitterFollowers">Twitter Followers</label>
                        <input type="number" v-model="form.twitter_followers" class="form-control" id="twitterFollowers" placeholder="Enter Twitter follower count" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="instagramHandle">Instagram Handle</label>
                        <input type="text" v-model="form.instagram_handle" class="form-control" id="instagramHandle" placeholder="Enter Instagram handle" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="instagramFollowers">Instagram Followers</label>
                        <input type="number" v-model="form.instagram_followers" class="form-control" id="instagramFollowers" placeholder="Enter Instagram follower count" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="facebookHandle">Facebook Handle</label>
                        <input type="text" v-model="form.facebook_handle" class="form-control" id="facebookHandle" placeholder="Enter Facebook handle" />
                    </div>

                    <div class="form-group mt-3">
                        <label for="facebookFollowers">Facebook Followers</label>
                        <input type="number" v-model="form.facebook_followers" class="form-control" id="facebookFollowers" placeholder="Enter Facebook follower count" />
                    </div>

                    <button type="submit" class="btn btn-primary w-100 mt-4">Register as Influencer</button>
                </form>

                <!-- Display message -->
                <div v-if="message" class="alert mt-3" :class="{'alert-success': success, 'alert-danger': !success}">
                    {{ message }}
                </div>

                <!-- Links to other pages -->
                <div class="d-flex justify-content-between mt-3">
                    <button @click="toSponsorRegister" class="btn btn-outline-success">Register as Sponsor</button>
                    <button @click="toLogin" class="btn btn-outline-secondary">Already a User? Login</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "influencerRegister",
    data() {
        return {
            form: {
                email: '',
                password: '',
                full_name: '',
                phone: '',
                address: '',
                category: '',
                niche: '',
                profile_picture: '',
                twitter_handle: '',
                twitter_followers: 0,
                instagram_handle: '',
                instagram_followers: 0,
                facebook_handle: '',
                facebook_followers: 0
            },
            message: '',
            success: false
        };
    },
    methods: {
        async registerInfluencer() {
            try {
                const payload = { ...this.form, role: 'influencer' };
                const response = await axios.post('http://localhost:5000/influencerRegister', payload);
                
                this.message = response.data.message;
                this.success = response.data.success;

                if (this.success) {
                    this.form = {
                        email: '',
                        password: '',
                        full_name: '',
                        phone: '',
                        address: '',
                        category: '',
                        niche: '',
                        profile_picture: '',
                        twitter_handle: '',
                        twitter_followers: 0,
                        instagram_handle: '',
                        instagram_followers: 0,
                        facebook_handle: '',
                        facebook_followers: 0
                    };
                }
            } catch (error) {
                console.error(error);
                this.message = error.response.data.message || 'Registration failed';
                this.success = false;
            }
        },
        toSponsorRegister() {
            this.$router.push('/sponsorRegister');
        },
        toLogin() {
            this.$router.push('/userLogin');
        }
    }
};
</script>

<style scoped>
.register-influencer {
    max-width: 500px;
    margin: 0 auto;
}

.card {
    border-radius: 10px;
}

.card-header {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

button {
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0d6efd !important;
}
</style>
