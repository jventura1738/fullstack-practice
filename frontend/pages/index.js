import Head from "next/head";
import styles from "../styles/Home.module.css";
import { useState } from "react";

export default function Home() {
  const [img, setImg] = useState("");
  const [isSet, setIsSet] = useState(false);
  const generatePokemonImg = () => {
    fetch("http://localhost:5000/get-random-pokemon").then((response) =>
      response.text().then((text) => {
        if (text != null || text != "") {
          setImg(text);
          setIsSet(true);
        } else {
          setIsSet(false);
        }
      })
    );
  };
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <button onClick={generatePokemonImg} className={styles.button}>
        Encounter Pokemon!
      </button>
      <div className={isSet ? styles.show : styles.hidden}>
        <img src={img} height={500} width={500} />
      </div>
    </div>
  );
}
