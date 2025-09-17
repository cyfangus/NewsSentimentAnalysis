from bertopic import BERTopic
import umap.umap_ as umap

def topic_modeling(texts):
    umap_model = umap.UMAP(n_neighbors=5, n_components=5, min_dist=0.0, metric='cosine', random_state=42)

    topic_model = BERTopic(umap_model=umap_model)
    topics, _ = topic_model.fit_transform(texts)

    print("Topics discovered:")
    print(topic_model.get_topic_info().head())
    return topic_model