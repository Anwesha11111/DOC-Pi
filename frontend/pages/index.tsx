import React from 'react';
import Head from 'next/head';
import styles from '../styles/Home.module.css';

const Home: React.FC = () => {
  return (
    <>
      <Head>
        <title>Docapi – AI‑Powered Document Search Engine</title>
        <meta name="description" content="Upload documents, search semantically, and explore an interactive knowledge graph." />
      </Head>
      <main className={styles.main}>
        <h1 className={styles.title}>Docapi</h1>
        <p className={styles.description}>
          Next‑generation document AI platform – upload, search, and visualise reasoning.
        </p>
        <section className={styles.hero}>
          {/* Placeholder for future components: UploadPane, SearchBar, GraphViewer */}
        </section>
      </main>
    </>
  );
};

export default Home;
