# Extraction of Blood Vessels from Retinal Fundus Images

# See project demo: [Vessels Extraction](https://youtu.be/2kEe2Vs9_N4)

This research project was carried out for the comparative study of Blood Vessels in the retinal images. The segmentation of blood vessels in retina and delineation of different morphological attributes of the retinal blood vessels, such as width, length, branching patterns, tortuosity, and angles are utilized for the screening, treatment, diagnosis, and evaluation of various ophthalmological and cardiovascular diseases such as diabetes, arteriosclerosis, hypertension, and choroidal neovascularization. For retinal image mosaic synthesis and multimodal or temporal image registration, the automatic generation of retinal maps and extraction of branch points have been used. Automatic detection and analysis of the vasculature can assist ophthalmologists in the implementation of screening programs for Diabetic retinopathy and diabetic macular edema. It also can aid research on the relationship between hypertensive retinopathy and vessel tortuosity, computer-assisted laser surgery and vessels diameter measurement in relation to the diagnosis of hypertension. The following tasks were carried out for this project.

• Trained CNN architecture (Modified the famous U-Net: Convolution Networks for Biomedical Image Segmentation) for blood vessel segmentation.

• The retinal vessel segmentation performance was measured by AUC-ROC (Area Under the Receiver Operating Characteristics) performance measurement metric to measure the precision-recall tradeoff of my algorithm and obtained an AUC-ROC score of 0.97.

• Built a web application to deploy trained models by using the Django Framework.
