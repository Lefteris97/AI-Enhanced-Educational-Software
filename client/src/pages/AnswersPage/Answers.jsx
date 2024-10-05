import './Answers.css';
import { useContext, useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import useFetch from '../../hooks/useFetch';
import AuthContext from '../../context/AuthProvider';
import axios from 'axios';

const Answers = () => {
  const { exerciseId } = useParams();

  const { data, loading, error } = useFetch(`http://localhost:8000/answers/of/${exerciseId}`);

  const { auth } = useContext(AuthContext);
  
  const [answers, setAnswers] = useState([]);
  const [modifiedGrades, setModifiedGrades] = useState({});

  useEffect(() => {
    if (data && data.answers) {
      setAnswers(data.answers);
    }
  }, [data]);

  const handleSaveButton = async () => {
    try {
      // Construct the array of modified grades
      const modifiedGradesArray = Object.entries(modifiedGrades)
        .map(([id, grade]) => ({ id, grade }));
  
      // Send PUT request with modified grades
      const response = await axios.put(
        'http://localhost:8000/answers/grade_answers', 
        modifiedGradesArray,
        {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
            'Content-Type': 'application/json'
          }
        });
  
      if (response.status !== 200) {
        throw new Error('Failed to save grades');
      }
  
      // Reset modified grades state after successful save
      setModifiedGrades({});
      console.log('Grades saved successfully');

    } catch (error) {
      console.error('Error saving grades:', error.message);
    }
  };

  const handleGradeChange = (id, value) => {
    setModifiedGrades((prevGrades) => ({
      ...prevGrades,
      [id]: value,
    }));
  };

  if (loading) {
    return <div>Loading answers...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!answers.length) {
    return <div>No answers available</div>;
  }

  return (
    <>
      <div className="anHeader">
        <h1>Answers for Exercise {exerciseId}</h1>
        <Link to='/dash/exercises' className='saveButton' onClick={() => handleSaveButton()}>Save</Link>
      </div>
      <ul>
        {answers.map((answer) => (
          <li key={answer.id} className='answerItem'>
            <h2>Answer ID: {answer.exercise_id}</h2>
            <h2>User ID: {answer.user_id}</h2>
            <div className="answerFile">
              <h2>File: </h2>
              <a href={`http://localhost:8000/${answer.answer_file_path}`} download>
                {answer.answer_file_path.split('/').pop()}
              </a>
            </div>
            {answer.grade !== null ? (
              <h2>Grade: {answer.grade}</h2>
            ) : (
              <div className="inputGrade">
                <label htmlFor='grade'><h2>Grade:</h2></label>
                <input
                  type="number"
                  min={0}
                  max={10}
                  value={modifiedGrades[answer.id] || ''}
                  onChange={(e) => handleGradeChange(answer.id, e.target.value)}
                />
              </div>
            )}
          </li>
        ))}
      </ul>
    </>
  );
};

export default Answers;
