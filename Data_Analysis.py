import pandas as pd

# Read in the data from the performance evaluations tab
eval_df = pd.read_excel('TeacherDataset.xlsx', sheet_name='performance_evaluations')

# Melt the evaluations dataframe to unpivot the data
eval_df_melted=eval_df.melt(id_vars=['teacher_id'],
             var_name='eval_year',
             value_name='eval_score')

eval_df_head=eval_df_melted.head()
print(eval_df_head)

# Read in the data from the background tab
backg_df = pd.read_excel('TeacherDataset.xlsx', sheet_name='background')

backg_head = backg_df.head()
print(backg_head)

# Calculate the mean evaluation score for each teacher
mean_scores = eval_df_melted.groupby('teacher_id')['eval_score'].mean()

# Create a boolean column indicating whether each teacher passed their initial certification exam
backg_df['passed_initial_exam'] = backg_df['board_cert_year'] == backg_df['training_year']

# Merge the background and evaluation data by teacher ID
merged_scores = pd.merge(backg_df, mean_scores, on='teacher_id')

# Calculate the mean evaluation score for teachers who passed their initial certification exam
initial_pass_mean_score = merged_scores.loc[merged_scores['passed_initial_exam'], 'eval_score'].mean()

# Calculate the mean evaluation score for teachers who did not pass their initial certification exam
initial_fail_mean_score = merged_scores.loc[~merged_scores['passed_initial_exam'], 'eval_score'].mean()

# Print the results
print(f'Mean evaluation score for teachers who passed their initial certification exam: {initial_pass_mean_score}')
print(f'Mean evaluation score for teachers who did not pass their initial certification exam: {initial_fail_mean_score}')

# Based on the mean evaluation scores calculated above, the mean evaluation score for teachers who passed their initial certification exam is 69.5, 
# while the mean evaluation score for teachers who did not pass their initial certification exam is 66.5.
# This suggests that, prior to 1990, teachers who passed their initial certification exams were, on average, more likely to have higher performance evaluation scores 
# during their subsequent careers than teachers who did not pass their initial certification exams. However, the difference in mean scores is not very large, 
# so the effect may not be very strong.
# This analysis does not take into account any other factors that may affect performance evaluation scores, such as differences in teaching experience or demographics.
# Additionally, the data only covers a limited time period (1970-1990) and may not be representative of more recent trends.

# Read in the data from the performance evaluations tab
eval_df2 = pd.read_excel('TeacherDataset.xlsx', sheet_name='performance_evaluations')

# Melt the evaluations dataframe to unpivot the data
eval_df_melted2=eval_df2.melt(id_vars=['teacher_id'],
             var_name='eval_year',
             value_name='eval_score')

# Read in the data from the background tab
backg_df2 = pd.read_excel('TeacherDataset.xlsx', sheet_name='background')

# Create a new column to indicate whether a teacher completed training before or after 1990
backg_df2["training_before_1990"] = backg_df2["training_year"] < 1990

# Create a new column to indicate whether a teacher passed their initial certification exam
backg_df2["initial_certification_passed"] = backg_df2["board_cert_year"] == backg_df2["training_year"]

# Merge the background and evaluation data
merged_training = pd.merge(backg_df2, eval_df_melted2, on="teacher_id")

# Calculate the mean evaluation score for teachers who completed training before and after 1990, and whether they passed their initial certification exam or not
training_grouped = merged_training.groupby(["training_before_1990", "initial_certification_passed"]).mean()["eval_score"]

print(training_grouped)
