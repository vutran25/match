# Match

Your company has decided to diversify into matchmaking. As a first step, it is offering a service to pair people for a first date and asked you to write the software for the pairing. Initial requirements are relatively simple:

* Pairing will be between males and females only for now.
* Each profile will specify the user's country, diet, drinking, language, religion, and smoking as integers representing some values that will be hidden. E.g., a value for language of 0 may mean Engligh and a False for smoking could mean the user doesn't smoke.
* The company expects each user to want to be paired with exactly the same kind. E.g., a user from USA will want to be paired with another also from USA.
* The importance given to each of these matches is indicated in a weight value that accompanies these values. E.g., for country, you may get a (0, 0.3400777564281171) showing the country code and the weight given by the user to the match.
* The company evaluates the compatibility of each pair by combining the weighted match sums for each user of the pair. I.e., say user A finds user B to have a combined match score of X (weighted total for all the fields), and user B has a similar score of Y, the compatibility would be X + Y.

Your job is to pair each female with a male for their first date so the pairs represent the most compatible matching across all the users.

You can get the profiles as an iterable by invoking Profiles(count), where count is the number of profiles to be paired - you are guaranteed to get half males and half females. For this project, pair 100 users (50 females with 50 males).

Also, your manager insists that you write unit tests to confirm that your software indeed satisfies these requirements.