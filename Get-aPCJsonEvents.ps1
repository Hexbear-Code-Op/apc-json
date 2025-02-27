$apiKey="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN0YWhtYXhmZmNxYW5raWVudWxoIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTcwNDAzOTUsImV4cCI6MTk3MjYxNjM5NX0.-YZmaNQcoQXbC0_VZYD_jNuOgVbFEu9fbpL_lRDBIH0"

$allEvents = @()
1..12 | ForEach-Object {Invoke-RestMethod -Uri "https://stahmaxffcqankienulh.supabase.co/rest/v1/events?select=*&month=eq.$($_)&order=day,title.asc" -Headers @{apikey= $apikey} | ForEach-Object {$allEvents += $_ }}

$sortedEvents = $allEvents | Sort-Object -Property month,day,title
$sortedEvents | convertTo-Json | Out-File .\aPC.json