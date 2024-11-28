
{{/*
Generate a name with no chart name.
*/}}
{{- define "myChart.name" -}}
{{- printf "%s" .Release.Name -}}
{{- end -}}

{{/*
Generate a fully qualified name.
*/}}
{{- define "myChart.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" | lower -}}
{{- end -}}

