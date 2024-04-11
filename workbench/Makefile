install:
	pip install -r requirements.txt
run-caddy:
	bash run_caddy.sh
run:
	# streamlit run main.py --theme.base light
	bash run_service_local.sh
package:
	docker buildx build --network=host --platform linux/amd64 -f docker/Dockerfile -t registry.dp.tech/mlops/workbench/retro-synthesis-v2:lp-0.0.7 . --push
deploy:
	kubectl --kubeconfig ~/.kube/mlops_zjk apply -f k8s-manifest/deploy.yaml -n launching-workload-service
	kubectl --kubeconfig ~/.kube/mlops_zjk rollout restart deploy -n launching-workload-service retro-synthesis-v2

test:
	pytest
