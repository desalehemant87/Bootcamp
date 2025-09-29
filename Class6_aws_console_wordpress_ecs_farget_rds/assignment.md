# AWS ECS WordPress Deployment Assignment

Refrence: https://livingdevops.com/aws/deploying-a-3-tier-production-application-on-aws-ecs-a-complete-guide/

## Objective
Deploy a WordPress application on AWS ECS Fargate with RDS MySQL database using the AWS Console.

## What You'll Learn
- Create ECS clusters and task definitions
- Deploy containers using AWS Fargate
- Configure Application Load Balancer
- Set up RDS MySQL database
- Connect WordPress to database

## Assignment Tasks

### Step 1: Create ECS Cluster
1. Go to AWS ECS Console
2. Create a new cluster
3. Choose AWS Fargate as capacity provider
4. Name your cluster: `wordpress-cluster`

**Screenshot Required:** ECS cluster creation page

### Step 2: Create Task Definition
1. Create new task definition
2. Use these settings:
   - Family name: `wordpress-task`
   - Launch type: Fargate
   - CPU: 1 vCPU
   - Memory: 3 GB
   - Container name: `wordpress`
   - Image: `wordpress:latest`
   - Port: 80

**Screenshot Required:** Task definition configuration

### Step 3: Create RDS Database
1. Go to RDS Console
2. Create MySQL database with:
   - Engine: MySQL
   - Template: Free tier
   - DB name: `wordpress`
   - Master username: `admin`
   - Use AWS Secrets Manager for password
   - Disable public access

**Screenshot Required:** RDS instance details

### Step 4: Create ECS Service
1. Create new service in your cluster
2. Settings:
   - Launch type: Fargate
   - Task definition: Select your wordpress-task
   - Desired tasks: 2
   - Create Application Load Balancer
   - Configure security groups (allow HTTP port 80)

**Screenshot Required:** Running ECS service

### Step 5: Connect WordPress to Database
1. Access WordPress via ALB DNS name
2. Complete WordPress setup with:
   - Database host: Your RDS endpoint
   - Database name: `wordpress`
   - Username: `admin`
   - Password: From AWS Secrets Manager

**Screenshot Required:** Working WordPress site

## Submission Requirements
1. **6 Screenshots** as specified above
2. **Brief report** (1-2 pages) including:
   - What you learned
   - Any problems you faced
   - Your custom domain name
   - ALB DNS name for comparison

## Important Notes
- Make sure ECS and RDS are in the same VPC
- Configure security groups properly
- Buy domain from any cheap provider ($1-5 domains available)
- DNS propagation can take 5-30 minutes
- Don't forget to clean up resources after submission

## Due Date
[Insert date here]

## Grading
- All 6 screenshots: 60%
- Working WordPress site with custom domain: 30%
- Report: 10%