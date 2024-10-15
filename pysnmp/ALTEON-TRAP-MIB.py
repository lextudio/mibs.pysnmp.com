# SNMP MIB module (ALTEON-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:58 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(altswitchTraps,
 fltCurCfgIndx,
 fltCurCfgPortIndx,
 ipCurCfgGwAddr,
 ipCurCfgGwIndex,
 slbCurCfgRealServerIndex,
 slbCurCfgRealServerIpAddr,
 slbCurCfgRealServerName,
 slbCurCfgVirtServiceRealPort) = mibBuilder.importSymbols(
    "ALTEON-PRIVATE-MIBS",
    "altswitchTraps",
    "fltCurCfgIndx",
    "fltCurCfgPortIndx",
    "ipCurCfgGwAddr",
    "ipCurCfgGwIndex",
    "slbCurCfgRealServerIndex",
    "slbCurCfgRealServerIpAddr",
    "slbCurCfgRealServerName",
    "slbCurCfgVirtServiceRealPort")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

altSwPrimaryPowerSuppylFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 1)
)
if mibBuilder.loadTexts:
    altSwPrimaryPowerSuppylFailure.setStatus(
        ""
    )

altSwRedunPowerSuppylFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 2)
)
if mibBuilder.loadTexts:
    altSwRedunPowerSuppylFailure.setStatus(
        ""
    )

altSwDefGwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 3)
)
altSwDefGwUp.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"),
        ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwUp.setStatus(
        ""
    )

altSwDefGwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 4)
)
altSwDefGwDown.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"),
        ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwDown.setStatus(
        ""
    )

altSwDefGwInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 5)
)
altSwDefGwInService.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"),
        ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwInService.setStatus(
        ""
    )

altSwDefGwNotInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 6)
)
altSwDefGwNotInService.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "ipCurCfgGwIndex"),
        ("ALTEON-PRIVATE-MIBS", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwDefGwNotInService.setStatus(
        ""
    )

altSwSlbRealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 7)
)
altSwSlbRealServerUp.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerUp.setStatus(
        ""
    )

altSwSlbRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 8)
)
altSwSlbRealServerDown.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerDown.setStatus(
        ""
    )

altSwSlbRealServerMaxConnReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 9)
)
altSwSlbRealServerMaxConnReached.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerMaxConnReached.setStatus(
        ""
    )

altSwSlbBkupRealServerAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 10)
)
altSwSlbBkupRealServerAct.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerAct.setStatus(
        ""
    )

altSwSlbBkupRealServerDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 11)
)
altSwSlbBkupRealServerDeact.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeact.setStatus(
        ""
    )

altSwSlbBkupRealServerActOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 12)
)
altSwSlbBkupRealServerActOverflow.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerActOverflow.setStatus(
        ""
    )

altSwSlbBkupRealServerDeactOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 13)
)
altSwSlbBkupRealServerDeactOverflow.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbBkupRealServerDeactOverflow.setStatus(
        ""
    )

altSwSlbFailoverStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 14)
)
if mibBuilder.loadTexts:
    altSwSlbFailoverStandby.setStatus(
        ""
    )

altSwSlbFailoverActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 15)
)
if mibBuilder.loadTexts:
    altSwSlbFailoverActive.setStatus(
        ""
    )

altSwSlbFailoverSwitchUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 16)
)
if mibBuilder.loadTexts:
    altSwSlbFailoverSwitchUp.setStatus(
        ""
    )

altSwSlbFailoverSwitchDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 17)
)
if mibBuilder.loadTexts:
    altSwSlbFailoverSwitchDown.setStatus(
        ""
    )

altSwfltFilterFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 18)
)
altSwfltFilterFired.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "fltCurCfgIndx"),
        ("ALTEON-PRIVATE-MIBS", "fltCurCfgPortIndx"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwfltFilterFired.setStatus(
        ""
    )

altSwSlbRealServerServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 19)
)
altSwSlbRealServerServiceUp.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServiceRealPort"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceUp.setStatus(
        ""
    )

altSwSlbRealServerServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 13, 0, 20)
)
altSwSlbRealServerServiceDown.setObjects(
      *(("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIndex"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerIpAddr"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgRealServerName"),
        ("ALTEON-PRIVATE-MIBS", "slbCurCfgVirtServiceRealPort"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    altSwSlbRealServerServiceDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TRAP-MIB",
    **{"altSwPrimaryPowerSuppylFailure": altSwPrimaryPowerSuppylFailure,
       "altSwRedunPowerSuppylFailure": altSwRedunPowerSuppylFailure,
       "altSwDefGwUp": altSwDefGwUp,
       "altSwDefGwDown": altSwDefGwDown,
       "altSwDefGwInService": altSwDefGwInService,
       "altSwDefGwNotInService": altSwDefGwNotInService,
       "altSwSlbRealServerUp": altSwSlbRealServerUp,
       "altSwSlbRealServerDown": altSwSlbRealServerDown,
       "altSwSlbRealServerMaxConnReached": altSwSlbRealServerMaxConnReached,
       "altSwSlbBkupRealServerAct": altSwSlbBkupRealServerAct,
       "altSwSlbBkupRealServerDeact": altSwSlbBkupRealServerDeact,
       "altSwSlbBkupRealServerActOverflow": altSwSlbBkupRealServerActOverflow,
       "altSwSlbBkupRealServerDeactOverflow": altSwSlbBkupRealServerDeactOverflow,
       "altSwSlbFailoverStandby": altSwSlbFailoverStandby,
       "altSwSlbFailoverActive": altSwSlbFailoverActive,
       "altSwSlbFailoverSwitchUp": altSwSlbFailoverSwitchUp,
       "altSwSlbFailoverSwitchDown": altSwSlbFailoverSwitchDown,
       "altSwfltFilterFired": altSwfltFilterFired,
       "altSwSlbRealServerServiceUp": altSwSlbRealServerServiceUp,
       "altSwSlbRealServerServiceDown": altSwSlbRealServerServiceDown}
)
