import { useEffect, useState } from 'react'
import './StudentProgress.css'
import useFetch from '../../hooks/useFetch'
import SearchStudent from '../../components/SearchStudent'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios'

const StudentProgress = () =>{
    const [student, setStudent] = useState(null);
    const [performanceData, setPerformanceData] = useState([]);
    const [exercisesScores, setExercisesScores] = useState('');
    const [speakingScores, setSpeakingScores] = useState('');
    const [listeningScores, setListeningScores] = useState('');
    const [classBehaviour, setClassBehaviour] = useState('');
    const [consistency, setConsistency] = useState('');
    const [forumUsage, setForumUsage] = useState('');
    const [formError, setFormError] = useState(null);

    // Fetch students performance
    const { data, loading, error, reFetch } = useFetch(
        student ? `http://127.0.0.1:8000/student/performance/${student.student_id}` : null
    );

    useEffect(() => {
        // Set performance data when the hook fetches it successfully
        if (data) {       
            console.log('D: ', data);
            const transformedData = data.map((item) => ({
                score: item.score,
                date: new Date(item.date).toLocaleDateString('en-GB'), // Format date as DD/MM/YYYY
            }));

            setPerformanceData(transformedData);
        } 
      }, [data]);

    // Handle the student selection from the Search Bar
    const handleStudentSelect = (studentData) => {
        console.log('stud data: ', studentData);
        if (studentData) {
            setStudent(studentData);
            setPerformanceData([]);
            setFormError(null);
        } else {
            // Clear student and performance data on error
            setStudent(null);
            setPerformanceData([]);
        }
    };

    const handleAddPerformance = async (e) =>{
        e.preventDefault();

        try {
            await axios.post('http://127.0.0.1:8000/student/performance', {
                user_id: student.student_id,
                exercises_scores: exercisesScores,  
                speaking_scores: speakingScores,
                listening_scores: listeningScores,
                class_behaviour: classBehaviour,
                consistency: consistency,
                forum_usage: forumUsage
            });

            // Clear the form input
            setExercisesScores('');
            setSpeakingScores('');
            setListeningScores('');
            setClassBehaviour('');
            setConsistency('');
            setForumUsage('');

            // Clear previous errors after successful submission
            setFormError(null);

            // Fetch the updated performance data
            await reFetch(); 
        } catch (error) {
            setFormError('Failed to add performance score. Please try again.');
        }
    };

    return (
        <div className='progressContainer'>
            <h1>Student Progress</h1>
            <SearchStudent onStudentSelect={handleStudentSelect}/>
        
            {student && (
                <div className='infoContainer'>
                    <h2 className='idAndName'>
                        ID: {student.student_id} Name: {student.fname} {student.lname} 
                    </h2>
                    {/* Form to Add Performance */}
                    <h3 className='perfHeader'>Performance Form:</h3>
                    <form onSubmit={handleAddPerformance} className='perfForm'>
                        <div className='form-group'>
                            <label htmlFor='exercisesScores'>Exercises Score:</label>
                            <input
                                type='number'
                                id='exercisesScores'
                                value={exercisesScores}
                                onChange={(e) => setExercisesScores(e.target.value)}
                                min='0'
                                max='100'
                                required
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='speakingScores'>Speaking Score:</label>
                            <input
                                type='number'
                                id='speakingScores'
                                value={speakingScores}
                                onChange={(e) => setSpeakingScores(e.target.value)}
                                min='0'
                                max='100'
                                required
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='listeningScores'>Listening Score:</label>
                            <input
                                type='number'
                                id='listeningScores'
                                value={listeningScores}
                                onChange={(e) => setListeningScores(e.target.value)}
                                min='0'
                                max='100'
                                required
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='classBehaviour'>Class Behaviour:</label>
                            <input
                                type='number'
                                id='classBehaviour'
                                value={classBehaviour}
                                onChange={(e) => setClassBehaviour(e.target.value)}
                                min='0'
                                max='10'
                                required
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='consistency'>Consistency:</label>
                            <input
                                type='number'
                                id='consistency'
                                value={consistency}
                                onChange={(e) => setConsistency(e.target.value)}
                                min='0'
                                max='10'
                                required
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='forumUsage'>Forum Usage:</label>
                            <input
                                type='number'
                                id='forumUsage'
                                value={forumUsage}
                                onChange={(e) => setForumUsage(e.target.value)}
                                min='0'
                                max='10'
                                required
                            />
                        </div>

                        <div className='btnError'>
                            <button className='perfFormBtn' disabled={loading}>Submit</button>
                            {formError && <p className='formErrorMsg'>{formError}</p>}
                        </div>
                        
                    </form>

                    {/* Performance Graph */}
                    {performanceData.length > 0 ? (
                        <div className='perfGraph'>
                            <h3 className='graphHeader'>Performance Over Time:</h3>
                            <ResponsiveContainer width="100%" height={300}>
                                <LineChart
                                    data={performanceData}
                                    margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                                >
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis dataKey="date" />
                                    <YAxis domain={[0, 100]}/>
                                    <Tooltip />
                                    <Legend />
                                    <Line type="monotone" dataKey="score" stroke="#8884d8" />
                                </LineChart>
                            </ResponsiveContainer>
                        </div>
                    ) : (
                        <p className='noDataMsg'>No performance data available for this student.</p>
                    )}
                </div>
            )}
        </div>
    )
}

export default StudentProgress