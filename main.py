from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Html(
            Head(
                Meta(charset='UTF-8'),
                Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
                Title('Service Request Form'),
                Style(':root {\r\n    --bg: #FAFBFA;\r\n    --panel: #FFFFFF;\r\n    --ink: #1C2321;\r\n    --ink-soft: #5B6663;\r\n    --line: #DDE3E0;\r\n    --accent: #3D6B66;\r\n    --accent-soft: #E7EFEE;\r\n    --error: #A5433A;\r\n  }\r\n\r\n  * { box-sizing: border-box; }\r\n\r\n  body {\r\n    margin: 0;\r\n    background: var(--bg);\r\n    color: var(--ink);\r\n    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;\r\n    -webkit-font-smoothing: antialiased;\r\n  }\r\n\r\n  .topbar { height: 4px; background: var(--accent); }\r\n\r\n  .wrap {\r\n    max-width: 640px;\r\n    margin: 0 auto;\r\n    padding: 48px 24px 80px;\r\n  }\r\n\r\n  header.page-header {\r\n    margin-bottom: 40px;\r\n  }\r\n\r\n  header.page-header h1 {\r\n    font-size: 26px;\r\n    font-weight: 600;\r\n    margin: 0 0 6px;\r\n    letter-spacing: -0.01em;\r\n  }\r\n\r\n  header.page-header p {\r\n    margin: 0;\r\n    color: var(--ink-soft);\r\n    font-size: 15px;\r\n  }\r\n\r\n  fieldset {\r\n    border: none;\r\n    margin: 0 0 36px;\r\n    padding: 0;\r\n  }\r\n\r\n  legend {\r\n    font-size: 13px;\r\n    font-weight: 600;\r\n    color: var(--accent);\r\n    padding-bottom: 8px;\r\n    margin-bottom: 18px;\r\n    border-bottom: 1px solid var(--line);\r\n    width: 100%;\r\n  }\r\n\r\n  .field {\r\n    margin-bottom: 18px;\r\n  }\r\n\r\n  .row {\r\n    display: grid;\r\n    grid-template-columns: 1fr 1fr;\r\n    gap: 16px;\r\n  }\r\n\r\n  label {\r\n    display: block;\r\n    font-size: 14px;\r\n    font-weight: 500;\r\n    margin-bottom: 6px;\r\n  }\r\n\r\n  label .req {\r\n    color: var(--accent);\r\n    margin-left: 2px;\r\n  }\r\n\r\n  input[type="text"],\r\n  input[type="email"],\r\n  input[type="tel"],\r\n  input[type="number"] {\r\n    width: 100%;\r\n    padding: 10px 12px;\r\n    font-size: 15px;\r\n    font-family: inherit;\r\n    color: var(--ink);\r\n    background: var(--panel);\r\n    border: 1px solid var(--line);\r\n    border-radius: 6px;\r\n    outline: none;\r\n    transition: border-color 0.15s ease;\r\n  }\r\n\r\n  input:focus {\r\n    border-color: var(--accent);\r\n  }\r\n\r\n  input:invalid:not(:placeholder-shown) {\r\n    border-color: var(--error);\r\n  }\r\n\r\n  .hint {\r\n    font-size: 12px;\r\n    color: var(--ink-soft);\r\n    margin-top: 5px;\r\n  }\r\n\r\n  .segmented {\r\n    display: flex;\r\n    gap: 10px;\r\n    flex-wrap: wrap;\r\n  }\r\n\r\n  .segmented input {\r\n    position: absolute;\r\n    opacity: 0;\r\n    pointer-events: none;\r\n  }\r\n\r\n  .segmented label {\r\n    margin: 0;\r\n    padding: 10px 18px;\r\n    font-size: 14px;\r\n    font-weight: 500;\r\n    border: 1px solid var(--line);\r\n    border-radius: 6px;\r\n    cursor: pointer;\r\n    background: var(--panel);\r\n    transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;\r\n  }\r\n\r\n  .segmented input:checked + label {\r\n    background: var(--accent-soft);\r\n    border-color: var(--accent);\r\n    color: var(--accent);\r\n  }\r\n\r\n  .segmented input:focus-visible + label {\r\n    outline: 2px solid var(--accent);\r\n    outline-offset: 2px;\r\n  }\r\n\r\n  .actions {\r\n    display: flex;\r\n    gap: 12px;\r\n    margin-top: 8px;\r\n  }\r\n\r\n  button {\r\n    font-family: inherit;\r\n    font-size: 15px;\r\n    font-weight: 600;\r\n    padding: 12px 22px;\r\n    border-radius: 6px;\r\n    border: none;\r\n    cursor: pointer;\r\n    transition: opacity 0.15s ease;\r\n  }\r\n\r\n  button.primary {\r\n    background: var(--accent);\r\n    color: #fff;\r\n  }\r\n\r\n  button.secondary {\r\n    background: transparent;\r\n    color: var(--ink-soft);\r\n    border: 1px solid var(--line);\r\n  }\r\n\r\n  button:hover { opacity: 0.9; }\r\n\r\n  .error-banner {\r\n    display: none;\r\n    background: #FBEDEA;\r\n    border: 1px solid var(--error);\r\n    color: var(--error);\r\n    padding: 10px 14px;\r\n    border-radius: 6px;\r\n    font-size: 14px;\r\n    margin-bottom: 24px;\r\n  }\r\n\r\n  .error-banner.show { display: block; }\r\n\r\n  #summary {\r\n    display: none;\r\n  }\r\n\r\n  #summary h2 {\r\n    font-size: 20px;\r\n    margin: 0 0 4px;\r\n  }\r\n\r\n  #summary .sub {\r\n    color: var(--ink-soft);\r\n    font-size: 14px;\r\n    margin-bottom: 28px;\r\n  }\r\n\r\n  .summary-grid {\r\n    display: grid;\r\n    grid-template-columns: 180px 1fr;\r\n    row-gap: 14px;\r\n    column-gap: 16px;\r\n    font-size: 15px;\r\n    margin-bottom: 32px;\r\n  }\r\n\r\n  .summary-grid dt {\r\n    color: var(--ink-soft);\r\n  }\r\n\r\n  .summary-grid dd {\r\n    margin: 0;\r\n    font-weight: 500;\r\n  }\r\n\r\n  body.showing-summary #request-form { display: none; }\r\n  body.showing-summary #summary { display: block; }\r\n\r\n  @media print {\r\n    .topbar { display: none; }\r\n    body:not(.showing-summary) .wrap { display: none; }\r\n    .actions { display: none; }\r\n    header.page-header p { display: none; }\r\n  }\r\n\r\n  @media (max-width: 560px) {\r\n    .row { grid-template-columns: 1fr; }\r\n    .summary-grid { grid-template-columns: 140px 1fr; }\r\n  }')
            ),
            Body(
                Div(cls='topbar'),
                Div(
                    Header(
                        H1('Service Request Form'),
                        P('Complete all fields below to submit a sample processing request.'),
                        cls='page-header'
                    ),
                    Div('Please fill in all required fields before submitting.', id='error-banner', cls='error-banner'),
                    Form(
                        Fieldset(
                            Legend('Your details'),
                            Div(
                                Label(
                                    'Full name',
                                    Span('*', cls='req'),
                                    fr='fullName'
                                ),
                                Input(type='text', id='fullName', name='fullName', required='', placeholder='e.g. Jordan Reyes'),
                                cls='field'
                            ),
                            Div(
                                Div(
                                    Label(
                                        'Email',
                                        Span('*', cls='req'),
                                        fr='email'
                                    ),
                                    Input(type='email', id='email', name='email', required='', placeholder='you@example.com'),
                                    cls='field'
                                ),
                                Div(
                                    Label(
                                        'Phone number',
                                        Span('*', cls='req'),
                                        fr='phone'
                                    ),
                                    Input(type='tel', id='phone', name='phone', required='', placeholder='04xx xxx xxx'),
                                    cls='field'
                                ),
                                cls='row'
                            )
                        ),
                        Fieldset(
                            Legend('Supervisor details'),
                            Div(
                                Label(
                                    "Supervisor's full name",
                                    Span('*', cls='req'),
                                    fr='supName'
                                ),
                                Input(type='text', id='supName', name='supName', required='', placeholder='e.g. Dr. Alex Chen'),
                                cls='field'
                            ),
                            Div(
                                Label(
                                    "Supervisor's email",
                                    Span('*', cls='req'),
                                    fr='supEmail'
                                ),
                                Input(type='email', id='supEmail', name='supEmail', required='', placeholder='supervisor@example.com'),
                                cls='field'
                            )
                        ),
                        Fieldset(
                            Legend('Request details'),
                            Div(
                                Label(
                                    'General Ledger Code (GLC)',
                                    Span('*', cls='req'),
                                    fr='glc'
                                ),
                                Input(type='text', id='glc', name='glc', required='', placeholder='e.g. GLC-000000'),
                                cls='field'
                            ),
                            Div(
                                Label(
                                    'Type of service request',
                                    Span('*', cls='req')
                                ),
                                Div(
                                    Input(type='radio', id='prepUser', name='serviceType', value='User Prep', required=''),
                                    Label('User Prep', fr='prepUser'),
                                    Input(type='radio', id='prepCore', name='serviceType', value='Core Prep'),
                                    Label('Core Prep', fr='prepCore'),
                                    cls='segmented'
                                ),
                                cls='field'
                            ),
                            Div(
                                Div(
                                    Label(
                                        'Number of samples to be submitted',
                                        Span('*', cls='req'),
                                        fr='numSamples'
                                    ),
                                    Input(type='number', id='numSamples', name='numSamples', min='1', step='1', required='', placeholder='e.g. 12'),
                                    cls='field'
                                ),
                                Div(
                                    Label(
                                        'Is this a resubmission?',
                                        Span('*', cls='req')
                                    ),
                                    Div(
                                        Input(type='radio', id='resubYes', name='resubmission', value='Yes', required=''),
                                        Label('Yes', fr='resubYes'),
                                        Input(type='radio', id='resubNo', name='resubmission', value='No'),
                                        Label('No', fr='resubNo'),
                                        cls='segmented'
                                    ),
                                    cls='field'
                                ),
                                cls='row'
                            )
                        ),
                        Div(
                            Button('Review request', type='submit', cls='primary'),
                            cls='actions'
                        ),
                        id='request-form',
                        novalidate=''
                    ),
                    Section(
                        H2('Request summary'),
                        P('Check the details below, then print or edit.', cls='sub'),
                        Dl(id='summary-fields', cls='summary-grid'),
                        Div(
                            Button('Edit', type='button', id='edit-btn', cls='secondary'),
                            Button('Print', type='button', id='print-btn', cls='primary'),
                            cls='actions'
                        ),
                        id='summary'
                    ),
                    cls='wrap'
                ),
                Script('const form = document.getElementById(\'request-form\');\r\n  const errorBanner = document.getElementById(\'error-banner\');\r\n  const summaryFields = document.getElementById(\'summary-fields\');\r\n\r\n  const labels = {\r\n    fullName: "Full name",\r\n    email: "Email",\r\n    phone: "Phone number",\r\n    supName: "Supervisor\'s full name",\r\n    supEmail: "Supervisor\'s email",\r\n    glc: "General Ledger Code (GLC)",\r\n    serviceType: "Type of service request",\r\n    numSamples: "Number of samples",\r\n    resubmission: "Resubmission"\r\n  };\r\n\r\n  form.addEventListener(\'submit\', function (e) {\r\n    e.preventDefault();\r\n\r\n    if (!form.checkValidity()) {\r\n      errorBanner.classList.add(\'show\');\r\n      form.reportValidity();\r\n      return;\r\n    }\r\n    errorBanner.classList.remove(\'show\');\r\n\r\n    const data = new FormData(form);\r\n    summaryFields.innerHTML = \'\';\r\n    Object.keys(labels).forEach(function (key) {\r\n      const dt = document.createElement(\'dt\');\r\n      dt.textContent = labels[key];\r\n      const dd = document.createElement(\'dd\');\r\n      dd.textContent = data.get(key);\r\n      summaryFields.appendChild(dt);\r\n      summaryFields.appendChild(dd);\r\n    });\r\n\r\n    document.body.classList.add(\'showing-summary\');\r\n    window.scrollTo(0, 0);\r\n  });\r\n\r\n  document.getElementById(\'edit-btn\').addEventListener(\'click\', function () {\r\n    document.body.classList.remove(\'showing-summary\');\r\n  });\r\n\r\n  document.getElementById(\'print-btn\').addEventListener(\'click\', function () {\r\n    window.print();\r\n  });')
            ),
            lang='en'
        )

serve()