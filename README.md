# PoC folder for Zero Trust RfP

1. Open Google Cloud console: console.cloud.google.com
2. Open Cloud Shell
3. Clone this repository: git clone ...
4. Activate APIs ...
    ````bash
    gcloud services enable compute.googleapis.com
    gcloud services enable container.googleapis.com
    gcloud services enable iap.googleapis.com
    gcloud services enable cloudresourcemanager.googleapis.com
    gcloud services enable appengine.googleapis.com
    ````
5. Create new service account and bind it to the __project editor__ role:
    ````bash 
    PROJECT_ID=$(gcloud config get-value core/project)
    SA="bce-project-editor@$PROJECT_ID.iam.gserviceaccount.com"

    gcloud iam service-accounts create bce-project-editor --description="Project Editor SA for Beyond Corp Enterprise" --display-name="bce_project_editor"

    gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SA" --role="roles/editor"
    ````

6. Create a __Cloud AI Platform notebook__:
    ````bash 
    export INSTANCE_NAME="bce-notebook"
    export VM_IMAGE_PROJECT="deeplearning-platform-release"
    export VM_IMAGE_FAMILY="common-cpu"
    export MACHINE_TYPE="n1-standard-2"
    export LOCATION="europe-west1-b"

    gcloud beta notebooks instances create $INSTANCE_NAME --vm-image-project=$VM_IMAGE_PROJECT --vm-image-family=$VM_IMAGE_FAMILY --machine-type=$MACHINE_TYPE --location=$LOCATION --service-account=$SA
    ````

7. Open the Notebook app in your browser:
    ````bash
    URL=$(gcloud beta notebooks instances describe $INSTANCE_NAME --location=$LOCATION --format="value(metadata.proxy-url)")

    echo $URL
    ````
8. Install the bash Kernel in the notebook:
    
    7.1 Open the Terminal in the notebook app
    
    7.2 Install the bash kernel
    ````bash 
    pip install bash_kernel
    python -m bash_kernel.install
    ````
    7.3 Refresh the browser
9. Clone the repository by clicking on the Git icon and the "Clone a Repository" button. Use the following URL: https://github.com/Hermi999/bce.git
10. Open the folder "bce" in the File Browser and open the File "instructions.ipynb"
11. Follow the instructions there