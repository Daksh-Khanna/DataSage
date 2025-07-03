class SessionQueryBuilder:

    @staticmethod
    def build_details_query(filters):
        base_query = """
            SELECT 
                sm.start_time_utc,
                sm.end_time_utc,
                s.user_email,
                s.operator_code,
                sm.question,
                sm.system_status,
                sm.user_status
            FROM session_messages sm
            JOIN sessions s ON sm.session_id = s.session_id
        """

        where_clauses = []
        params = []

        if "start_date" in filters and "end_date" in filters:
            where_clauses.append("sm.start_time_utc BETWEEN %s AND %s")
            params.extend([filters["start_date"], filters["end_date"]])

        if "operator" in filters and filters["operator"]:
            where_clauses.append("s.operator_code = %s")
            params.append(filters["operator"])

        if "email" in filters and filters["email"]:
            where_clauses.append("s.user_email = %s")
            params.append(filters["email"])

        if "system_status" in filters and filters["system_status"]:
            where_clauses.append("sm.system_status = %s")
            params.append(filters["system_status"] == "Success")

        if "user_feedback" in filters and filters["user_feedback"]:
            where_clauses.append("sm.user_status = %s")
            params.append(filters["user_feedback"])

        if where_clauses:
            base_query += " WHERE " + " AND ".join(where_clauses)

        return base_query, params

    @staticmethod
    def build_metrics_query():
        return """
            SELECT 
                DATE(sm.start_time_utc) AS date,
                COUNT(DISTINCT s.operator_code) AS active_operators,
                COUNT(DISTINCT s.user_email) AS active_users,
                COUNT(DISTINCT sm.session_id) AS active_sessions,
                COUNT(sm.question) AS total_questions,
                ROUND(COUNT(sm.question) / NULLIF(COUNT(DISTINCT sm.session_id), 0), 2) AS questions_per_session
            FROM session_messages sm
            JOIN sessions s ON sm.session_id = s.session_id
            GROUP BY DATE(sm.start_time_utc)
            ORDER BY DATE(sm.start_time_utc);
        """
