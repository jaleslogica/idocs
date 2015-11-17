jQuery("#simulation")
  .on("click", ".s-2dd17364-5c07-4b39-881b-fa0d65d37315 .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-Label_21")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_2"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Label_22")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_3"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Label_24")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_3"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Label_25")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Label_26")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_2"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Label_28")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      event.data = data;
      jEvent.launchCases(cases);
    }
  })
  .on("click", ".s-2dd17364-5c07-4b39-881b-fa0d65d37315 .toggle", function(event, data) {
    var jEvent, jFirer, cases;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-Label_29")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimSetValue",
                    "parameter": {
                      "target": "#s-Label_30",
                      "value": "-"
                    },
                    "exectype": "serial",
                    "delay": 0
                  },
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_2"
                    },
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_31")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_3"
                    },
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_32")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_5"
                    },
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_33")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_7"
                    },
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_34")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_4"
                    },
                    "exectype": "serial",
                    "delay": 0
                  },
                  {
                    "action": "jimChangeStyle",
                    "parameter": [ {
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_34": {
                        "attributes": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    },{
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_34": {
                        "attributes-ie": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    } ],
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_35")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_8"
                    },
                    "exectype": "serial",
                    "delay": 0
                  },
                  {
                    "action": "jimChangeStyle",
                    "parameter": [ {
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_35": {
                        "attributes": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    },{
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_35": {
                        "attributes-ie": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    } ],
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_36")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_10"
                    },
                    "exectype": "serial",
                    "delay": 0
                  },
                  {
                    "action": "jimChangeStyle",
                    "parameter": [ {
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_36": {
                        "attributes": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    },{
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_36": {
                        "attributes-ie": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    } ],
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    } else if(jFirer.is("#s-Label_37")) {
      if(jFirer.data("jimHasToggle")) {
        jFirer.removeData("jimHasToggle");
        jEvent.undoCases(jFirer);
      } else {
        jFirer.data("jimHasToggle", true);
        event.backupState = true;
        event.target = jFirer;
        cases = [
          {
            "blocks": [
              {
                "actions": [
                  {
                    "action": "jimShow",
                    "parameter": {
                      "target": "#s-Group_12"
                    },
                    "exectype": "serial",
                    "delay": 0
                  },
                  {
                    "action": "jimChangeStyle",
                    "parameter": [ {
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_37": {
                        "attributes": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    },{
                      "#s-2dd17364-5c07-4b39-881b-fa0d65d37315 #s-Label_37": {
                        "attributes-ie": {
                          "border-top-width": "1px",
                          "border-top-style": "solid",
                          "border-top-color": "#000000",
                          "border-right-width": "1px",
                          "border-right-style": "solid",
                          "border-right-color": "#000000",
                          "border-bottom-width": "0px",
                          "border-bottom-style": "none",
                          "border-bottom-color": "#000000",
                          "border-left-width": "1px",
                          "border-left-style": "solid",
                          "border-left-color": "#000000",
                          "border-radius": "0px 0px 0px 0px"
                        }
                      }
                    } ],
                    "exectype": "serial",
                    "delay": 0
                  }
                ]
              }
            ],
            "exectype": "serial",
            "delay": 0
          }
        ];
        jEvent.launchCases(cases);
      }
    }
  });