def get_query_detailstab():
    query = """
        SELECT 
            sm.start_time_utc AS "Date Time",
            s.user_email AS "Email",
            s.operator_code AS "Operator",
            sm.question as "Question",
            sm.system_status as "System Status",
            sm.user_status as "User Feedback",
    		CASE 
        		WHEN EXTRACT(EPOCH FROM sm.end_time_utc - sm.start_time_utc) < 60 
            	THEN EXTRACT(EPOCH FROM sm.end_time_utc - sm.start_time_utc)::INT || ' sec'
        	ELSE 
            	EXTRACT(MINUTE FROM sm.end_time_utc - sm.start_time_utc) || ' min' ||
            	(EXTRACT(SECOND FROM sm.end_time_utc - sm.start_time_utc)::INT) || ' sec'
    		END AS "Response Time"
			FROM session_messages sm
        	JOIN sessions s ON sm.session_id = s.session_id;
    """
    return query

def get_query_metricstab():
    query = """
        SELECT 
        DATE(sm.start_time_utc) AS "Date",
        COUNT(DISTINCT s.operator_code) AS "Active Operators",
        COUNT(DISTINCT s.user_email) AS "Active Users",
        COUNT(DISTINCT sm.session_id) AS "Active Sessions",
        COUNT(sm.question) AS "Total Questions",
        ROUND(COUNT(sm.question) / NULLIF(COUNT(DISTINCT sm.session_id), 0), 2) AS "Questions Per Session"
        FROM session_messages sm
        JOIN sessions s ON sm.session_id = s.session_id
        GROUP BY DATE(sm.start_time_utc)
        ORDER BY DATE(sm.start_time_utc);
    """
    return query