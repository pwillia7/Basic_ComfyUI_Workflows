## Updates

**1/4/24**
Addded audio generation workflows, Added cogvideox workflows, reorganized all workflows. Improved Flux lora training and testing workflows.

**10/26/24**
Added Workflows for Flux w/ LORA, Flux LORA Autoprompt and Flux LORA Training

**6/8/24**
2 new Llava workflows to 1-at-a-time-batch engage with clip vision images to ask questions or rename images.

**5/24/24**
Cleaned up all workflows, added notes, improved IPA and outpaint workflows, changed clip to SDXLclip


New workflows: StableCascade txt2img img2img and imageprompt, InstantID, Instructpix2pix, controlnetmulti, imagemerge_sdxl_unclip, imagemerge_unclip, t2iadapter, controlnet+t2i_toolkit 

## About

This is meant to be a good foundation to start using ComfyUI in a basic way. Should be familiar to those coming from A1111. 

You can import the json files or the pngs into Comfy to use the workflows. Most workflows are built for SDXL by default but can be changed easily to work with other SD versions.

## Flux Workflows
### Flux with LORA
![fluxwithlora](./Flux/WorkflowImages/flux_lora.png)
### Flux LORA LLM Autoprompt
![fluxautopromptllm](./Flux/WorkflowImages/flux_lora_autoprompt.png)
### Flux LORA Train
![fluxloratrain](./Flux/Training/WorkflowImages/flux_lora_train.png)
### Flux LORA Test
![fluxloratest](./Flux/Training/WorkflowImages/loratest.png)

## Stable_Cascade Workflows
### txt2img_stablecascade
![txt2img_stablecascade](./Stable_Cascade/WorkflowImages/txt2img_stablecascade.png)
### img2img_stablecascade
![img2img_stablecascade](./Stable_Cascade/WorkflowImages/img2img_stablecascade.png)
### imgprompt_stablecascade
![imgprompt_stablecascade](./Stable_Cascade/WorkflowImages/imgprompt_stablecascade.png)

## LLM_Llava Workflows
### LLava Batch File
![llava_batch](./LLM_Llava/WorkflowImages/llava_batch_questionphoto.png)
### LLava File Namer
![llava_file_namer](./LLM_Llava/WorkflowImages/llava_file_namer.png)

## Basic Workflows
### txt2img
![txt2img](./Basic/WorkflowImages/txt2img.png)
### txt2img LORA
![txt2imglora](./Basic/WorkflowImages/txt2imglora.png)
### img2img
![img2img](./Basic/WorkflowImages/img2img.png)
### img2img LORA
![img2imglora](./Basic/WorkflowImages/img2imglora.png)
### controlnet
![controlnet](./Basic/WorkflowImages/controlnet.png)
### Controlnet Multi (2 controlnet models)
![controlnetmulti](./Basic/WorkflowImages/controlnetmulti.png)
### Controlnet + T2I Toolkit
![controlnet+t2i_toolkit](./Basic/WorkflowImages/controlnet+t2i_toolkit.png)
### IPAdapter
![IPAdapter](./Basic/WorkflowImages/ipadapter.png)
### IPAdapter + Controlnet
![IPAdapter+controlnet](./Basic/WorkflowImages/ipadapter+controlnet.png)
### T2I Adapter
![t2iadapter](./Basic/WorkflowImages/t2iadapter.png)
### Inpainting
![inpainting](./Basic/WorkflowImages/inpainting.png)
### Outpainting
![outpainting](./Basic/WorkflowImages/outpainting.png)
### Hires Fix
![hiresfix](./Basic/WorkflowImages/hiresfix.png)
### Instant ID
![InstantID](./Basic/WorkflowImages/instantid.png)
### Face Detailer
![Facedetailer](./Basic/WorkflowImages/facedetailer.png)
### Prompts from File
![promptsfromfile](./Basic/WorkflowImages/promptsfromfile.png)
### XYZ Plot (for sampler config; use prompts from file for batch prompts)
![xyzplot](./Basic/WorkflowImages/xyzplot.png)
### Upscale SUPIR
![upscaleSUPIR](./Basic/WorkflowImages/upscaleSUPIR.png)
### InstructPix2Pix
![InstructPix2Pix](./Basic/WorkflowImages/instructpix2pix.png)
### Image Merge SDXL Unclip
![imagemerge_sdxl_unclip](./Basic/WorkflowImages/imagemerge_sdxl_unclip.png)
### Image Merge Unclip
![imagemerge_unclip](./Basic/WorkflowImages/imagemerge_unclip.png)
