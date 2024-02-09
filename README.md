# Orientation Decoding of Neuron
Repository for analysis of the Stringer dataset for Neuromatch Spring 2024.

## Abstract

The visual cortex of all studied mammals contain neurons that respond selectively to edges lying at a certain orientation. The mammalian visual cortex has a defined architecture consisting of six layers, which vary in their input and local connectivity. Incoming visual stimulation reaches layer 4 (L4) through thalamic inputs first, is projected to upper layers L2/3, and further transmitted to the lower layers, L5 and L6. Standard two-photon microscopy techniques allow the visualization of local neuronal activity within small cortical regions. Recent advances in mesoscopic imaging have enabled the recording of larger neuronal networks, enabling us to answer questions such as: is orientation selectivity differently encoded in different layers? Which layers contain the most information about stimulus orientations? Do orientation selective neurons in different layers have specific activation patterns?  

Variations in input and local connectivity across visual cortical layers ⅔, 4, and 5 may bias neurons in each layer to respond with differing sensitivity and precision to stimulus orientations. To quantify each cortical layer’s stimulus selectivity properties, we leveraged an openly available dataset of 2-photon calcium imaging neural responses across ~20,000 mouse visual cortical neurons in response to visual stimuli differing in the orientation of drifting gratings. We propose to fit one random forest classifier per visual cortical layer to decode visual stimulus orientations. We will then compare each model’s classification accuracy across layers, assessing how each model’s false positive and negative errors distribute across the visual stimulus classes. We anticipate that cortical layers with wider orientation tuning will exhibit larger misclassifications adjacent to the diagonal of a confusion matrix. A thorough characterization of differences in visual stimulus representations across layers will improve our understanding of the role of intrinsic connectivity and input patterns in shaping visual stimulus processing across sensory cortices. 

# Setup

Ensure that Python is installed in your system. In the project directory, open the terminal and execute:

```
python -m venv env
```

to create a Python virtual environment. Then you can activate the virtual environment by running

```
.\env\Script\activate
```

in Windows. For Linux machines, you can run

```
source ./env/bin/activate
```

Now that the virtual environment is activated, you can start installing the libraries by running:

```
pip install -r requirements.txt
```

Setup is then done! You can execute the notebooks using the virtual environment as the Python kernel.
