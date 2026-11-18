\documentclass[lighthipster]{simplehipstercv}
\usepackage[utf8]{inputenc}
\usepackage[default]{raleway}
\usepackage[margin=1cm, a4paper]{geometry}
\usepackage{hyperref}

%------------------------------------------------------------------ Variablen
\newlength{\rightcolwidth}
\newlength{\leftcolwidth}
\setlength{\leftcolwidth}{0.23\textwidth}
\setlength{\rightcolwidth}{0.75\textwidth}

%------------------------------------------------------------------
\title{Platform Engineer Resume}
\author{Jason Mansfield}
\date{December 2024}

\pagestyle{empty}
\begin{document}

\thispagestyle{empty}

\simpleheader{headercolour}{Jason N}{Mansfield}{Platform Engineer | Senior Ops Lead}{white}

\vspace{4em}

\setlength{\columnsep}{1.5cm}
\columnratio{0.26}[0.75]
\begin{paracol}{2}
\hbadness5000

\footnotesize
{\setasidefontcolour
\flushright
\begin{center}
    \roundpic{id.jpg}
\end{center}

\bg{cvgreen}{white}{About me}\\[0.5em]
\begin{itemize}
\item \textbf{Platform Architect:} Expert in multi-repo GitOps using \textbf{Harness}, \textbf{Terraform}, and \textbf{Kustomize}.
\item \textbf{The Fixer:} Uses \textbf{AI (Gemini)} to rapidly remediate errors in Maven, .NET, and IaC.
\item \textbf{DevSecOps Specialist:} Engineered custom \textbf{Anchore API} gates to isolate app vulnerabilities.
\item \textbf{Clearance:} Active \textbf{TS/SCI w/ CI Poly}.
\end{itemize}

\bigskip

\bg{cvgreen}{white}{Bluf} \\[0.5em]
Jason Mansfield \\
USN 2001 - 2005 \\
USCG 2005 - 2023

\bigskip

\bg{cvgreen}{white}{Clearance}\\[0.5em]
\textbf{TS/SCI w CI Poly}

\begin{flushleft}
\vspace{2em}
\infobubble{\faEnvelope}{cvgreen}{white}{\scriptsize{trentonknight@gmail.com}}
\infobubble{\faLinkedin}{cvgreen}{white}{\href{https://www.linkedin.com/in/trentonknight/}{trentonknight}}
\infobubble{\faMobile}{cvgreen}{white}{(757)753-0085}
\infobubble{\faCompass}{cvgreen}{white}{Clayton, NC}
\end{flushleft}
}

\switchcolumn
\small

\section*{Degrees}
\begin{tabular}{r p{0.55\textwidth} c}
    \cvdegree{2013}{B.S.}{Computer Science}{Regis University}{NSA-listed Center of Academic Excellence.}{regis.png} 
\end{tabular}

\section*{Engineering Proficiency}
\begin{tabular}{r @{\hspace{0.5em}}l}
     \bg{skilllabelcolour}{iconcolour}{Kubernetes/OCI} &  \barrule{0.55}{0.5em}{cvpurple}\\
     \bg{skilllabelcolour}{iconcolour}{Harness/CI-CD} &  \barrule{0.55}{0.5em}{cvgreen}\\
     \bg{skilllabelcolour}{iconcolour}{Anchore API} & \barrule{0.50}{0.5em}{cvpurple} \\
     \bg{skilllabelcolour}{iconcolour}{Python/Bash/jq} & \barrule{0.50}{0.5em}{cvpurple} \\
     \bg{skilllabelcolour}{iconcolour}{Terraform/IaC} & \barrule{0.45}{0.5em}{cvpurple} \\
\end{tabular}

\section*{Certifications}
\begin{tabular}{r| p{0.5\textwidth} c}
\cvevent{2020}{CompTIA}{Security+ ce}{Exp 02/2025}{Core security functions and IT career baseline.}{logosecurityplus.png} \\
\cvevent{2022}{CompTIA}{CySA+ ce}{Exp 02/2025}{Cybersecurity Analyst for incident response.}{logocysa.png} \\
\end{tabular}

\section*{Professional Experience}
\begin{tabular}{r| p{0.45\textwidth} c}
\cvevent{2024--Pres}{24x7Systems}{Ops Lead / Platform Eng}{Remote}{
\begin{itemize}
\item \textbf{Security Engineering:} Designed a custom \textbf{Anchore} REST API integration for Harness to isolate app-layer CVEs from base-image ancestry.
\item \textbf{Incident Automation:} Engineering a \textbf{Python} bridge between Prometheus and \textbf{AWS Connect} for automated voice-paging alerts.
\item \textbf{Orchestration:} Managed 3-repo architecture (Source, IaC, Artifacts) via \textbf{Harness} and \textbf{Terraform}.
\item \textbf{AI Diagnostics:} Leveraged \textbf{Gemini} to remediate Maven, .NET, and IaC errors, reducing downtime by 70\%.
\end{itemize}}{24x7sys.png}\\

\cvevent{2023--2024}{CACI Int.}{DevOps Engineer}{Fort Bragg}{
\begin{itemize}
\item SRE for \textbf{GitLab} and secondary for \textbf{Hashicorp Vault}; managed identity via Keycloak and IaC via Terraform.
\item Developed Python/Bash automation to enhance GitOps workflows.
\end{itemize}}{caci.jpg}\\
\end{tabular}

\section*{Military History}
\begin{tabular}{r| p{0.45\textwidth} c}
\cvevent{2021--23}{USCG}{IT Specialist 1st Class}{CGCYBER}{Blue Team analyst; developed mission "Ruck kits" and led assessment missions.}{blueteam.jpg} \\
\cvevent{2017--21}{USCG}{IT Specialist 1st Class}{CGCYBER}{Watch Supervisor; led DODIN briefs to Leadership and managed incident response.}{cgcyber.png}\\
\end{tabular}

\vfill
\begin{center}
\footnotesize Jason N Mansfield | Clayton, NC | (757)753-0085 | \href{mailto:trentonknight@gmail.com}{trentonknight@gmail.com}
\end{center}

\end{paracol}
\end{document}
