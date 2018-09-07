#!/usr/bin/env/python2.7
from datadog import initialize, api
 # keys added here for convenience, in production they should probably be passed as environment variables
 options = {"api_key": "11b754188d6483e3ba6ae2f45904d195", "app_key":"a0b58f80a40093ae29366191f796b52c0bf34ee2" }
 initialize(**options)
 title = “MyMetric”
description = ""
graphs = [{
    "definition": {
        "events": [],
        "viz": "timeseries",
  	"status": "done",
  	"requests": [
    		{
      		"q": "avg:my_metric{*}",
      		"type": "line",
      		"style": {
        		"palette": "dog_classic",
        		"type": "solid",
        		"width": "normal"
      		},
      		"conditional_formats": [],
      		"aggregator": "avg"
    		}
  	],
  	"autoscale": true
    },
    "title": “Average of My_Metric"
},


{
    "definition": {
        "events": [],
        "viz": "timeseries",
  	"status": "done",
  	"requests": [
    		{
      		"q": "anomalies(avg:system.cpu.idle{*}, 'agile', 2, direction='both', alert_window='last_15m', interval=60, count_default_zero='true', seasonality='hourly')",
      		"type": "line",
      		"style": {
        		"palette": "dog_classic",
        		"type": "solid",
        		"width": "normal"
      		},
      		"conditional_formats": [],
      		"aggregator": "avg"
    		}
  	],
  	"autoscale": true
    },
    "title": “Avg of system.cpu.idle.over *”
}

{
    "definition": {
        "events": [],
        "viz": "timeseries",
  	"status": "done",
  	"requests": [
    	{
      		"q": "avg:my_metric{*}.rollup(sum, 3600)",
      		"type": "line",
      		"style": {
        		"palette": "dog_classic",
        		"type": "solid",
        		"width": "normal"
      		},
      		"conditional_formats": [],
      		"aggregator": "avg"
    	}
  	],
  	"autoscale": true
    },
    "title": “Rollup of the Average of My_Metric”
},


 ]
 template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]
 read_only = True
 api.Timeboard.create(title=title,
                     description=description,
                     graphs=graphs,
                     template_variables=template_variables,
                     read_only=read_only)
