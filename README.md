## Updates
**8/2/2025**
Basic WAN 2.2 txt2img workflow
**8/1/2025**
Added Video workflows for wan 2.2, upscale, and interpolation
**6/30/2025**
Added Flux Kontext Ultimate Workflow.
**1/5/2025**
Added F5 TTS Workflows. See here: https://youtu.be/SbRAPKAvl_U

## About

This is meant to be a good foundation to start using ComfyUI in a basic way. Should be familiar to those coming from A1111. 

You can import the JSON files or the PNGs into Comfy to use the workflows. Most workflows are built for SDXL by default but can be changed easily to work with other SD versions.

### Using This Repo as a ComfyUI Workflow Template Module

If you'd like these to appear inside ComfyUI’s **Workflow → Browse Templates** interface, simply clone this repo into your ComfyUI `custom_nodes` directory. ComfyUI will automatically detect the `example_workflows/` folder and display categorized workflow templates along with thumbnails (if present).

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/pwillia7/Basic_ComfyUI_Workflows
```

Alternatively, you can copy just the `example_workflows/` folder into any existing custom node directory. This allows you to modularly share curated workflows with or without custom nodes.

---

If you find these helpful, consider buying me a coffee:  
👉 https://buymeacoffee.com/reticulated


## Video
### Wan 2.2 GGUF + lightx2v
![wan22gguf](./Video/WorkflowImages/wan22_lx2v_gguf.jpg)
### Interpolate GIMM-VFI
![interpolate](./Video/WorkflowImages/video_interpolate.jpg)
### Video Upscale
![upscale](./Video/WorkflowImages/video_upscale.jpg)


## Flux Workflows
### Flux Kontext Ultimate Workflow
![fluxultimate](./Flux/WorkflowImages/flux_kontext_Ultimate.jpg)
### Flux with LORA
![fluxwithlora](./Flux/WorkflowImages/flux_lora.jpg)
### Flux LORA LLM Autoprompt
![fluxautopromptllm](./Flux/WorkflowImages/flux_lora_autoprompt.jpg)
### Miaoshouai-Tagger/Captions
![miaocaptions](./Flux/Training/WorkflowImages/MIAO_Captions.jpg)
### Flux LORA Train
![fluxloratrain](./Flux/Training/WorkflowImages/flux_lora_train.jpg)
### Flux LORA Test
![fluxloratest](./Flux/Training/WorkflowImages/loratest.jpg)
### Flux LORA Character Sheet Maker
![fluxcharactersheet](./Flux/WorkflowImages/flux_character_sheet.jpg)
## Stable_Cascade Workflows
### txt2img_stablecascade
![txt2img_stablecascade](./Stable_Cascade/WorkflowImages/stable-cascade-txt2img.jpg)
### img2img_stablecascade
![img2img_stablecascade](./Stable_Cascade/WorkflowImages/Stable-Cascade-image-to-image.jpg)
### imgprompt_stablecascade
![imgprompt_stablecascade](./Stable_Cascade/WorkflowImages/Stable-Cascade-Image-Prompt.jpg)

## LLM_Llava Workflows
### LLava Batch File
![llava_batch](./LLM_Llava/WorkflowImages/llava_batch_questionphoto.jpg)
### LLava File Namer
![llava_file_namer](./LLM_Llava/WorkflowImages/llava_file_namer.jpg)

## Basic Workflows
### WAN2.2 txt2img
![wan22txt2img](./Basic/WorkflowImages/wan_2_2_t2i.jpg)
### txt2img
![txt2img](./Basic/WorkflowImages/txt2img.jpg)
### txt2img LORA
![txt2imglora](./Basic/WorkflowImages/txt2imglora.jpg)
### img2img
![img2img](./Basic/WorkflowImages/img2img.jpg)
### img2img LORA
![img2imglora](./Basic/WorkflowImages/img2imglora.jpg)
### controlnet
![controlnet](./Basic/WorkflowImages/controlnet.jpg)
### Controlnet Multi (2 controlnet models)
![controlnetmulti](./Basic/WorkflowImages/controlnetmulti.jpg)
### Controlnet + T2I Toolkit
![controlnet+t2i_toolkit](./Basic/WorkflowImages/controlnet+t2i_toolkit.jpg)
### IPAdapter
![IPAdapter](./Basic/WorkflowImages/ipadapter.jpg)
### IPAdapter + Controlnet
![IPAdapter+controlnet](./Basic/WorkflowImages/ipadapter+controlnet.jpg)
### T2I Adapter
![t2iadapter](./Basic/WorkflowImages/t2iadapter.jpg)
### Inpainting
![inpainting](./Basic/WorkflowImages/inpainting.jpg)
### Outpainting
![outpainting](./Basic/WorkflowImages/outpainting.jpg)
### Hires Fix
![hiresfix](./Basic/WorkflowImages/hiresfix.jpg)
### Instant ID
![InstantID](./Basic/WorkflowImages/instandid.jpg)
### Face Detailer
![Facedetailer](./Basic/WorkflowImages/facedetailer.jpg)
### Prompts from File
![promptsfromfile](./Basic/WorkflowImages/promptsfromfile.jpg)
### XYZ Plot (for sampler config; use prompts from file for batch prompts)
![xyzplot](./Basic/WorkflowImages/xyzplot.jpg)
### Upscale SUPIR
![upscaleSUPIR](./Basic/WorkflowImages/upscaleSUPIR.jpg)
### InstructPix2Pix
![InstructPix2Pix](./Basic/WorkflowImages/instructpix2pix.jpg)
### Image Merge SDXL Unclip
![imagemerge_sdxl_unclip](./Basic/WorkflowImages/imagemerge_sdxl_unclip.jpg)
### Image Merge Unclip
![imagemerge_unclip](./Basic/WorkflowImages/imagemerge_unclip.jpg)
