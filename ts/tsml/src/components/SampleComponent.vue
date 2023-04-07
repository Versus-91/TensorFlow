<script lang="ts">
import { defineComponent } from 'vue';
import * as tf from '@tensorflow/tfjs';
export default defineComponent({
    data() {
        return {
            name: '',
            firstArray: '1, 2, 3, 4',
            secondArray: '2, 4, 6, 8',

        }
    },
    methods: {
        addArrays() {
            var firstArray = this.firstArray.split(',').map(Number);
            var secondArray = this.secondArray.split(',').map(Number);

            const firstTensor = tf.tensor(firstArray);
            const secondTensor = tf.tensor(secondArray);
            const model = tf.sequential();
            model.add(tf.layers.dense({ units: 1, inputShape: [1] }));
            model.compile({ loss: 'meanSquaredError', optimizer: 'sgd' });
            model.fit(firstTensor, secondTensor, { epochs: 500 }).then(() => {
                this.name = model.predict(tf.tensor([10])).toString();
            });
        }
    }
});
</script>
<template>
    
    <div class="container">
        <div class="columns is-multiline mt-6">
            <div class="column is-6">
                <div class="control">
                    <label for="firstArray" class="label">Array A :</label>
                    <input name="firstArray" class="input" v-model="firstArray" type="text">
                </div>
            </div>
            <div class="column is-6">
                <div class="control">
                    <label for="secondArray" class="label">Array A :</label>
                    <input name="secondArray" class="input" v-model="secondArray" type="text">
                </div>
            </div>
            <div class="column is-6">
                <div class="field">
                    <div class="control">
                        <button class="button is-info is-light" @click="addArrays">Predict Next</button>
                    </div>
                </div>
                <p> {{ name }}</p>
            </div>
        </div>
    </div>
</template>