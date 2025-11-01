#!/bin/bash

# Variables
AWS_REGION="ap-south-1"
AWS_ACCOUNT_ID="059941826920"
environment="dev"
app_name="app"
REPOSITORY_NAME_APP="${environment}-${app_name}-flask"
REPOSITORY_NAME_FRONTEND="${environment}-${app_name}-react"

# Login to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Function to build and push Docker images
build_and_push() {
    local dockerfile_path=$1
    echo "Dockerfile path: $dockerfile_path"
    local ecr_repository=$2
    echo "ECR Repository: $ecr_repository"
    local ecr_base_url=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
    echo "ECR Base URL: $ecr_base_url"
    local tag="latest"
    local image_final_path=$ecr_base_url/$ecr_repository:$tag
    echo "Final image path: $image_final_path"
    

    echo "Building $service image..."
    docker buildx build --platform linux/amd64 -t $image_final_path $dockerfile_path
    if [ $? -ne 0 ]; then
        echo "Docker build failed for $dockerfile_path"
        exit 1
    fi

    echo "Pushing $dockerfile_path image to ECR..."
    docker push $image_final_path
    if [ $? -ne 0 ]; then
        echo "Docker push failed for $image_final_path"
        exit 1
    else
        echo "Successfully pushed $image_final_path"    
    fi
}

# Build and push images
build_and_push "app/backend" $REPOSITORY_NAME_APP
build_and_push "app/frontend" $REPOSITORY_NAME_FRONTEND

echo "All images have been built and pushed successfully."