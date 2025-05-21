def get_query():
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
