# Free and Open-Source Tools, Funding, Compute and Hardware Support

This guide distinguishes resources that are free to use from competitive grants, credits, loans and donations. **No grant, cloud credit, equipment donation or company response is guaranteed.** Check the linked official program pages for current deadlines, country restrictions, legal-entity requirements and terms before applying. Program rules can change.

## Free software and tools

These tools have free/open-source options; always check each project's license, model/dataset terms, hardware requirements and third-party dependencies before commercial use.

- **ROS 2** — robotics middleware: https://docs.ros.org/
- **Gazebo** — robot and sensor simulation: https://gazebosim.org/
- **Webots** — robot simulation: https://cyberbotics.com/
- **OpenCV** — computer vision: https://opencv.org/
- **PyTorch** — deep learning: https://pytorch.org/
- **Hugging Face** — models, datasets and demos; usage/compute limits apply: https://huggingface.co/
- **Nav2** — ROS 2 navigation: https://nav2.org/
- **SLAM Toolbox** — mapping/localization: https://github.com/SteveMacenski/slam_toolbox
- **Open3D** — 3D data processing: https://www.open3d.org/
- **GitHub Actions** — CI minutes and artifact storage have plan-specific limits: https://github.com/features/actions
- **ONNX Runtime** — model inference: https://onnxruntime.ai/
- **MuJoCo** — physics simulation: https://mujoco.org/

Free software does not mean free physical hardware, unlimited cloud compute, unrestricted model weights, or a guarantee of commercial-use rights.

## Funding, compute and hardware-support leads

These are application routes, not confirmed awards. Tailor every request to the program's current eligibility rules.

| Organization / program | Possible support | Official route |
| --- | --- | --- |
| Thailand National Innovation Agency (NIA) | Eligible Thai innovation grants and commercialization support | https://www.nia.or.th/service/financial-support |
| depa Thailand | Digital startup / digital innovation funding calls | https://www.depa.or.th/th/startup and https://depa.or.th/th/funds |
| AMD University Program | Potential academic research hardware/software support; university eligibility may be required | https://www.amd.com/en/corporate/university-program.html |
| Seeed Studio Academic Support | Possible research collaboration, components or support for eligible applicants | https://academic.seeed.cc/ |
| Stereolabs | Ask about camera loan, research pricing or technical evaluation; donation is not promised | https://www.stereolabs.com/ |
| NVIDIA Inception | Free program membership and potential partner benefits; not a guaranteed GPU donation | https://www.nvidia.com/en-us/startups/ |
| AWS Activate | Potential AWS cloud credits for eligible startups; credits are not cash or hardware | https://aws.amazon.com/startups/ |
| Google for Startups Cloud Program | Potential cloud credits for eligible startups; tier and eligibility restrictions apply | https://cloud.google.com/startup/ |
| Hugging Face community GPU grants | Competitive compute support for qualifying public demos/research | https://github.com/huggingface/skills/blob/main/skills/huggingface-spaces/references/grants.md |
| Qualcomm AI Program for Innovators (APAC) | Cohort-specific hardware/grant support; check eligible countries and current application window | https://www.qualcomm.com/ai-program-for-innovators/apac |
| Open Robotics / ROS community | Open-source tools, community guidance and ecosystem collaboration, not a general cash grant | https://www.openrobotics.org/contact |

### Contacts previously identified — verify before sending

- AMD University Program: `aup@amd.com` — check the official program page for current contact instructions.
- Seeed Studio: `bp@seeed.cc` and `seeed_apac@seeed.cc` — verify current regional/program contacts on Seeed's official site.
- Stereolabs: `support@stereolabs.com` — ask to be routed to research/business development.
- Google Cloud startup support: `cloudstartupsupport@google.com` — confirm that this address is still supported and that your application qualifies.
- Thailand NIA and depa: use the contact details and application instructions displayed on their official sites, as program-specific contacts can change.
- Qualcomm: use the contact channel on the current APAC program page; past cohorts may be closed or country-restricted.

Do not send sensitive personal documents or bank details to an unverified address. Never pay a fee just to be considered for an alleged grant without independently verifying the program.

## Recommended no-hardware-first workflow

1. Build and run the project on the computer you already have.
2. Use simulation and public datasets where their licenses permit the intended use.
3. Add repeatable tests, raw benchmark outputs, system requirements and known limitations.
4. Publish a short demonstration and a one-page hardware request with exact quantities and specifications.
5. Ask for a loan or evaluation kit before requesting a permanent donation.
6. Apply for funding only after checking whether individuals, Thai-registered businesses or university partners are eligible.
7. Keep a support ledger documenting applications, deadlines, contacts, status, promised benefits and any restrictions.

## 2026–2028 support plan

- **2026:** Simulation-first proof of concept, software tests, documented benchmarks, applications to currently open programs.
- **2027:** Use measured results to seek academic collaborators, hardware loans, field-test partners and eligible grant rounds.
- **2028:** Pursue larger grants and commercial pilots only after safety, reliability, legal compliance and field performance are independently evaluated.

## Evidence and integrity rules

- Label each result as a target, simulation result, lab result or field result.
- Do not claim a grant, partnership, hardware donation, certification or benchmark success until it is confirmed and documented.
- Record license obligations for code, models, datasets and generated artifacts.
- Do not represent cloud credits as cash or as physical equipment.

## Project-specific priority: Coconut Harvest Robot

### First free stack to try
- ROS 2 + Gazebo or Webots for orchard and manipulator simulation.
- OpenCV and PyTorch for fruit detection/segmentation experiments.
- Open3D for point-cloud and 3D geometry processing.
- MoveIt 2 for manipulator planning: https://moveit.ros.org/
- GitHub Actions for repeatable tests and benchmark reports.

### Best-fit support requests
1. NIA: ask about current agricultural innovation / robotics funding and eligible prototype costs.
2. depa: ask whether the company or software platform fits a current digital innovation call.
3. Stereolabs: request a depth camera loan or research pricing for fruit localization.
4. Seeed Studio: request embedded AI boards, sensor modules or sample components.
5. AMD University Program: ask about compute support through a qualifying university collaborator.

### Hardware request to scope
Start with a camera/depth sensor, a small compute device and safe bench-scale actuator/manipulator components. For early work, use simulated trees and non-sharp mock fruit. Request loan/demo units with a written return plan; do not promise a successful harvest rate before tests.

### Suggested measurable evidence
Fruit detection precision/recall, 3D localization error, target reachability, grasp/manipulation success rate, cycle time, damage rate, dropped-object rate and emergency-stop tests. Report simulated and physical results separately. Real work at height requires a separate hazard analysis and qualified field validation.
