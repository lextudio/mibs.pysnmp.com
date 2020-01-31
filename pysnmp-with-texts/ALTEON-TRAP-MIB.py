#
# PySNMP MIB module ALTEON-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTEON-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ipCurCfgGwIndex, altswitchTraps, slbCurCfgVirtServiceRealPort, fltCurCfgPortIndx, slbCurCfgRealServerIpAddr, slbCurCfgRealServerIndex, fltCurCfgIndx, ipCurCfgGwAddr, slbCurCfgRealServerName = mibBuilder.importSymbols("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex", "altswitchTraps", "slbCurCfgVirtServiceRealPort", "fltCurCfgPortIndx", "slbCurCfgRealServerIpAddr", "slbCurCfgRealServerIndex", "fltCurCfgIndx", "ipCurCfgGwAddr", "slbCurCfgRealServerName")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, sysContact, sysLocation = mibBuilder.importSymbols("SNMPv2-MIB", "sysName", "sysContact", "sysLocation")
Counter64, Integer32, NotificationType, Bits, Counter32, Unsigned32, IpAddress, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "Bits", "Counter32", "Unsigned32", "IpAddress", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altSwPrimaryPowerSuppylFailure = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,1))
if mibBuilder.loadTexts: altSwPrimaryPowerSuppylFailure.setDescription('A altSwPrimaryPowerSuppylFailure trap signifies that the primary power supply failed.')
altSwRedunPowerSuppylFailure = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,2))
if mibBuilder.loadTexts: altSwRedunPowerSuppylFailure.setDescription('A altSwRedunPowerSuppylFailure trap signifies that the redundant power supply failed.')
altSwDefGwUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,3)).setObjects(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"), ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwDefGwUp.setDescription('A altSwDefGwUp trap signifies that the default gateway is alive.')
altSwDefGwDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,4)).setObjects(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"), ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwDefGwDown.setDescription('A altSwDefGwDown trap signifies that the default gateway is down.')
altSwDefGwInService = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,5)).setObjects(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"), ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwDefGwInService.setDescription('A altSwDefGwEnabled trap signifies that the default gateway is up and in service.')
altSwDefGwNotInService = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,6)).setObjects(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"), ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwDefGwNotInService.setDescription('A altSwDefGwDisabled trap signifies that the default gateway is alive but not in service.')
altSwSlbRealServerUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,7)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbRealServerUp.setDescription('A altSwSlbRealServerUp trap signifies that the real server is up and operational.')
altSwSlbRealServerDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,8)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbRealServerDown.setDescription('A altSwSlbRealServerDown trap signifies that the real server is down and out of service.')
altSwSlbRealServerMaxConnReached = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,9)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbRealServerMaxConnReached.setDescription('A altSwSlbRealServerMaxConnReached trap signifies that the real server has reached maximum connections.')
altSwSlbBkupRealServerAct = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,10)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbBkupRealServerAct.setDescription('A altSwSlbBkupRealServerAct trap signifies that the backup real server is activated due to availablity of the primary real server.')
altSwSlbBkupRealServerDeact = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,11)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbBkupRealServerDeact.setDescription('A altSwSlbBkupRealServerDeact trap signifies that the backup real server is deactivated due to the primary real server is available.')
altSwSlbBkupRealServerActOverflow = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,12)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbBkupRealServerActOverflow.setDescription('A altSwSlbBkupRealServerActOverflow trap signifies that the backup real server is deactivated due to the primary real server is overflowed.')
altSwSlbBkupRealServerDeactOverflow = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,13)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbBkupRealServerDeactOverflow.setDescription('A altSwSlbBkupRealServerDeactOverflow trap signifies that the backup real server is deactivated due to the primary real server is out from overflow situation.')
altSwSlbFailoverStandby = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,14))
if mibBuilder.loadTexts: altSwSlbFailoverStandby.setDescription('A altSwSlbFailoverStandby trap signifies that the switch is now a standby switch.')
altSwSlbFailoverActive = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,15))
if mibBuilder.loadTexts: altSwSlbFailoverActive.setDescription('A altSwSlbFailoverActive trap signifies that the switch is now an active switch.')
altSwSlbFailoverSwitchUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,16))
if mibBuilder.loadTexts: altSwSlbFailoverSwitchUp.setDescription('A altSwSlbFailoverSwitchUp trap signifies that the failover switch is alive.')
altSwSlbFailoverSwitchDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,17))
if mibBuilder.loadTexts: altSwSlbFailoverSwitchDown.setDescription('A altSwSlbFailoverSwitchDown trap signifies that the failover switch is down.')
altSwfltFilterFired = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,18)).setObjects(("ALTEON-PRIVATE-MIBS", "fltCurCfgIndx"), ("ALTEON-PRIVATE-MIBS", "fltCurCfgPortIndx"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwfltFilterFired.setDescription('A altSwfltFilterFired trap signifies that the packet received on a switch port matches the filter rule.')
altSwSlbRealServerServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,19)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServiceRealPort"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbRealServerServiceUp.setDescription('A altSwSlbRealServerServiceUp trap signifies that the service port of the real server is up and operational.')
altSwSlbRealServerServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 1, 13) + (0,20)).setObjects(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"), ("ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServiceRealPort"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysContact"))
if mibBuilder.loadTexts: altSwSlbRealServerServiceDown.setDescription('A altSwSlbRealServerServiceDown trap signifies that the service port of the real server is down and out of service.')
mibBuilder.exportSymbols("ALTEON-TRAP-MIB", altSwDefGwUp=altSwDefGwUp, altSwSlbBkupRealServerActOverflow=altSwSlbBkupRealServerActOverflow, altSwSlbFailoverSwitchDown=altSwSlbFailoverSwitchDown, altSwSlbRealServerServiceDown=altSwSlbRealServerServiceDown, altSwSlbFailoverActive=altSwSlbFailoverActive, altSwDefGwInService=altSwDefGwInService, altSwDefGwNotInService=altSwDefGwNotInService, altSwSlbRealServerMaxConnReached=altSwSlbRealServerMaxConnReached, altSwSlbBkupRealServerDeact=altSwSlbBkupRealServerDeact, altSwSlbRealServerUp=altSwSlbRealServerUp, altSwSlbBkupRealServerDeactOverflow=altSwSlbBkupRealServerDeactOverflow, altSwSlbRealServerServiceUp=altSwSlbRealServerServiceUp, altSwRedunPowerSuppylFailure=altSwRedunPowerSuppylFailure, altSwSlbFailoverStandby=altSwSlbFailoverStandby, altSwPrimaryPowerSuppylFailure=altSwPrimaryPowerSuppylFailure, altSwSlbRealServerDown=altSwSlbRealServerDown, altSwDefGwDown=altSwDefGwDown, altSwSlbBkupRealServerAct=altSwSlbBkupRealServerAct, altSwfltFilterFired=altSwfltFilterFired, altSwSlbFailoverSwitchUp=altSwSlbFailoverSwitchUp)