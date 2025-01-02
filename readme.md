# Time-Based Recommender System
# Read more about the Project here: https://pranjal28.hashnode.dev/building-a-time-based-movie-recommendation-system-with-bert4rec

## **Introduction**
This project is a **time-based recommender system** inspired by the research paper [BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer](https://arxiv.org/abs/1904.06690). It is designed to recommend items to users based on their historical interactions, similar to how Amazon’s **"You Might Also Like"** or Netflix’s personalized suggestions work.

## **What is BERT4Rec?**
BERT4Rec leverages the sequential prediction capabilities of the BERT (Bidirectional Encoder Representations from Transformers) model to solve recommendation tasks. It employs a **bidirectional attention mechanism**, enabling it to understand user interaction sequences comprehensively, both from past and future perspectives.

### **How It Works**
- **Input:** User interaction sequences (e.g., movie watch history).
- **Masking Technique:** Randomly masks items in the sequence and trains the model to predict the masked items.
- **Output:** Predicts the next items a user is likely to interact with, generating personalized recommendations.

## **Project Workflow**

### **1. Dataset Preparation**
- **Dataset Used:** [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/).
- **Preprocessing Steps:**
  - Removed duplicate interactions (e.g., multiple watches of the same movie).
  - Sampled sequences based on user watch history.

### **2. Exploratory Data Analysis (EDA)**
- Identified user behavior patterns:
  - **Casual watchers:** Few interactions.
  - **Movie fanatics:** High interaction counts with diverse movies.
- Analyzed distribution of interactions and genres.

### **3. Feature Engineering**
- Created user-item interaction sequences suitable for sequential modeling.
- Ensured balanced representation across different user types.

### **4. Model Training**
- **Architecture:** Adapted BERT4Rec for the recommendation task.
- **Training Objective:** Predict masked items in user interaction sequences.
- **Metrics for Evaluation:**
  - **nDCG@k:** Normalized Discounted Cumulative Gain.
  - **Hit Rate@k:** Measures the proportion of relevant items in recommendations.
  - **Precision@k:** Measures the accuracy of recommendations.

### **5. Evaluation Results**
| Metric            | Value  |
|-------------------|--------|
| nDCG@10          | 0.34   |
| Hit Rate@10      | 0.296  |
| Precision@10     | 0.20   |
| Genre-Based Precision@10 | 0.75   |
| Genre NDCG@10    | 0.60   |

### **6. Deployment**
- **Platform:** Deployed the model as a web app using **Azure App Service**.
- **Front-End:** Built an interactive interface to showcase recommendations to users.

## **Insights and Observations**
- The model performed particularly well in recommending movies within the same genre, achieving:
  - **Genre-Based Precision@10:** 0.75.
  - **Genre NDCG@10:** 0.60.
- This was achieved without explicit genre information, highlighting the power of the BERT-based bidirectional attention mechanism.

## **Future Improvements**
- Fine-tune hyperparameters to improve Precision@k.
- Incorporate explicit genre and user demographic data to enhance recommendations.
- Experiment with larger datasets and hybrid models.

## **How to Run the Project**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Data:**
   - Download the MovieLens 25M dataset.
   - Preprocess the data using the scripts provided.

4. **Train the Model:**
   ```bash
   python train.py
   ```

5. **Run the Web App:**
   ```bash
   python app.py
   ```
   Access the app at `http://localhost:5000`.

## **References**
- [BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer](https://arxiv.org/abs/1904.06690)
- [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/25m/)



