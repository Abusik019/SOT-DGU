import { useState } from 'react';
import styles from './style.module.css';

function Main() {
  const [hoveredIndex, setHoveredIndex] = useState(null);

  const listItems = [
    "Разработка, обоснование, апробация и внедрение новых образовательных технологий.",
    "Выявление инноваторов университета и помощь им в разработке, организации и оформлении мастер-классов и инновационных технологий.",
    "Поиск инновационных технологий в педагогических исследованиях, периодической печати и интернет ресурсах и адаптация к их условиям работы университета.",
    "Создание школы педагогического мастерства для молодых препадавателей.",
    "Организация научно-методических конференций и семинаров для преподавателей университета и других вузов.",
    "Обмен опытом инновационной деятельности с другими вузами Республики Дагестан и России."
  ];

  const getFirstThreeWords = (text) => {
    const words = text.split(' ');
    return words.slice(0, 3).join(' ') + '...';
  };

  return (
    <div className={styles.main}>
      <div className={styles.mainInfo}>
        <img src='https://www.iqconsultancy.ru/upload/medialibrary/572/mit.jpeg' alt="ЦСОТ"/>
        <h1>Центр образовательных технологий<br/>имени С.М.Омарова</h1>
      </div>
      <div className={styles.mainContent}>
        <h2>Основные направления работы ЦСОТ<br />им.С.М.Омарова</h2>
        <ul>
          {listItems.map((item, index) => (
            <li
              key={index}
              onMouseEnter={() => setHoveredIndex(index)}
              onMouseLeave={() => setHoveredIndex(null)}
            >
              {hoveredIndex === index ? item : getFirstThreeWords(item)}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Main;
