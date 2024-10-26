## Updates

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
![fluxwithlora](./WorkflowImages/flux_lora.png)
### Flux LORA LLM Autoprompt
![fluxautopromptllm](./WorkflowImages/flux_lora_autoprompt.png)
### Flux LORA Train
![fluxloratrain](./WorkflowImages/flux_lora_train.png)
## Workflows
 ### txt2img
 ![txt2img](./WorkflowImages/txt2img.png)
 ### txt2imglora
 ![txt2imglora](./WorkflowImages/txt2imglora.png)
 ### txt2img_stablecascade
![txt2img_stablecascade](./WorkflowImages/txt2img_stablecascade.png)
 ### img2img
 ![img2img](./WorkflowImages/img2img.png)
 ### img2imglora
 ![img2imglora](./WorkflowImages/img2imglora.png)
 ### img2img_stablecascade
![img2img_stablecascade](./WorkflowImages/img2img_stablecascade.png)
### imgprompt_stablecascade
![imgprompt_stablecascade](./WorkflowImages/imgprompt_stablecascade.png)
 ### controlnet
 ![controlnet](./WorkflowImages/controlnet.png)
 ### contolnet-multi (2 controlnet models)
 ![controlnetmulti](./WorkflowImages/controlnetmulti.png)
 ### controlnet+t2i_toolkit
 ![controlnet+t2i_toolkit](./WorkflowImages/controlnet+t2i_toolkit.png)
 ### IPAdapter
 ![IPAdapter](./WorkflowImages/ipadapter.png)
 ### IPAdapter+controlnet
 ![IPAdapter+controlnet](./WorkflowImages/ipadapter+controlnet.png)
 ### t2iadapter
 ![t2iadapter](./WorkflowImages/t2iadapter.png)
 ### inpainting
 ![inpainting](./WorkflowImages/inpainting.png)
 ### outpainting
 ![outpainting](./WorkflowImages/outpainting.png)
 ### hiresfix
 ![hiresfix](./WorkflowImages/hiresfix.png)
 ### InstantID
 ![InstantID](./WorkflowImages/instandid.png)
 ### Facedetailer
 ![Facedetailer](./WorkflowImages/facedetailer.png)
 ### promptsfromfile
 ![promptsfromfile](./WorkflowImages/promptsfromfile.png)
 ### xyzplot (for sampler config. Use prompts from file for batch prompts)
 ![xyzplot](./WorkflowImages/xyzplot.png)
 ### upscaleSUPIR
 ![upscaleSUPIR](./WorkflowImages/upscaleSUPIR.png)
 ### InstructPix2Pix
![InstructPix2Pix](./WorkflowImages/instructpix2pix.png)
 ### imagemerge_sdxl_unclip
![imagemerge_sdxl_unclip](./WorkflowImages/imagemerge_sdxl_unclip.png)
 ### imagemerge_unclip
![imagemerge_unclip](./WorkflowImages/imagemerge_unclip.png)
### llava batch file
![llava_batch](./WorkflowImages/llava_batch_questionphoto.png)
### llava file namer
![llava_file_namer](./WorkflowImages/llava_file_namer.png)