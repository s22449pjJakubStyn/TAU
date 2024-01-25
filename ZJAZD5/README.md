# Load tests on GuidePRO application
Application is my team's Bachelor of engineering project 'Workflex'. Currently, I have a personal repository for implementing and testing the functionalities assigned to me: https://github.com/s22449pjJakubStyn/Workflex_beta

## Test preview:
Our application has requirement to be able to handle 3000 of end users in total. In this set of load tests we are going to send this amount of responses in different periods of time to test capabilities of our back-end service.

### Case 1:
Input Values:
3000 requests in 150 seconds (2.5 min.)
![3000u_150s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/7fc26328-63bf-4f27-88b3-922aead3fb05)

Results values in latency are:
Average - 1ms
Min - 1ms
Max - 10ms
Error % - 0%
![3000u_150s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/a6e88eeb-7cfe-4436-bb0f-8c1bb1f6519f)

### Case 2:
Input Values:
3000 requests in 120 seconds (2 min.)
![3000u_120s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/3beb2997-d9d4-4a1c-a56c-32230cde0264)

Results values in latency are:
Average - 1ms
Min - 1ms
Max - 6ms
Error % - 0%
![3000u_120s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/c437f898-cde0-4751-8dc9-21138f7c74e2)

Conclusions:
We don't see any significant change in latency.

### Case 3:
Input Values:
3000 requests in 90 seconds (1.5 min.)
![3000u_90s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/40bf52d0-b054-46ed-b706-62fb72be69b4)

Results values in latency are:
Average - 1ms
Min - 1ms
Max - 8ms
Error % - 0%
![3000u_90s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/74146fb4-9bf9-4fae-ba83-7716a8914c18)

Conclusions:
We can observe very small increase in maximum latency, to be specific 2ms. This change won't really cause any issue in application.

### Case 4:
Input Values:
3000 requests in 60 seconds (1 min.)
![3000u_60s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/faa38cac-2ca0-46db-99c9-ff1126dec028)

Results values in latency are:
Average - 1ms
Min - 1ms
Max - 14ms
Error % - 0%
![3000u_60s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/7789f250-3c8a-4802-b296-6e874493e2cd)

Conclusions:
We can observe very small increase in maximum latency, to be specific 6ms. This change won't really cause any issue in application.

### Case 5:
Input Values:
3000 requests in 40 seconds
![3000u_40s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/16b73345-2917-4325-bff2-fbc2135260aa)

Results values in latency are:
Average - 1ms
Min - 1ms
Max - 45ms
Error % - 0%
![3000u_40s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/572315ba-f158-4c6e-84f7-6b792e485f2f)

Conclusions:
We can observe bit larger increase in maximum latency, to be specific 31ms. But this change is still too small to cause any issue in application.

### Case 6:
Input Values:
3000 requests in 30 seconds
![3000u_30s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/7e542c76-a0d1-4f9f-bd75-4c9570ef7b38)

Results values in latency are:
Average - 3ms
Min - 1ms
Max - 116ms
Error % - 0%
![3000u_30s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/11b37a5b-b159-4692-a7c2-f0277306122e)

Conclusions:
We can observe bit larger increase in maximum latency, to be specific 31ms. But this change is still too small to cause any issue in application but it could be a 1st sign of reaching 1st limits

### Case 7:
Input Values:
3000 requests in 20 seconds
![3000u_20s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/eb43dad0-55fd-4926-96b0-41511488d0cf)

Results values in latency are:
Average - 2ms
Min - 1ms
Max - 88ms
Error % - 0%
![3000u_20s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/8304463e-c6bf-4ba1-ad20-19cc90d00c5e)


Conclusions:
We can observe a little decreasing in maximum latency and still any eror %.

### Case 8:
Input Values:
3000 requests in 10 seconds
![3000u_10s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/50b61048-14c4-407f-9d94-a1f83ca4bb9d)

Results values in latency are:
Average - 2ms
Min - 1ms
Max - 13ms
Error % - 0%
![3000u_10s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/3be0f383-ebf8-428e-9547-27346e705ff8)

Conclusions:
We can observe a big decreasing in maximum latency and still any eror %.

### Case 9:
Input Values:
3000 requests in 6 seconds
![3000u_6s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/6e6927c6-2807-4fb1-92fd-f92520d10212)

Results values in latency are:
Average - 213ms
Min - 0ms
Max - 354ms
Error % - 11.33%
![3000u_6s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/415b64b8-fc0e-43a5-9387-03a9d9c8eaaa)

Conclusions:
We can see big increase in average and maximum latency. Average latency increase from 2ms to 213ms, and max latency increase from 13ms to 354s. Its second sign of limits.

### Case 10:
Input Values:
3000 requests in 4 seconds
![3000u_4s_input](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/bbd5dc3a-90a2-4bbf-a56a-7e53a0f186b0)

Results values in latency are:
Average - 117ms
Min - 0ms
Max - 333ms
Error % - 55.13%
![3000u_4s_results](https://github.com/s22449pjJakubStyn/TAU/assets/73015474/bdab2ec8-09b4-4a2b-b31d-93249cd56fcb)

Conclusions:
Its final case where average and max latency decrease a bit but error % increase above 5 times from 11.33% to 55.13%. Further tests make no sense because after 4 seconds more than half of the requests have not been processed and this number will only increase
