# SNMP MIB module (FD-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:31 2024
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

(epon,) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "epon")

(linkIdExhaust,
 linkOnLineStatus,
 onuIdExhaust) = mibBuilder.importSymbols(
    "FD-OLT-MIB",
    "linkIdExhaust",
    "linkOnLineStatus",
    "onuIdExhaust")

(onuOnLineStatus,
 uniPortLink,
 uniPortRstpState) = mibBuilder.importSymbols(
    "FD-ONU-MIB",
    "onuOnLineStatus",
    "uniPortLink",
    "uniPortRstpState")

(oltTrafficChangeVal,
 onuTrafficChangeVal,
 swSniPortTrafficChangeVal) = mibBuilder.importSymbols(
    "FD-PERFORMANCE-MIB",
    "oltTrafficChangeVal",
    "onuTrafficChangeVal",
    "swSniPortTrafficChangeVal")

(sfpPlugStauts,
 swPortLinkState) = mibBuilder.importSymbols(
    "FD-SWITCH-MIB",
    "sfpPlugStauts",
    "swPortLinkState")

(fanStatusBit,
 nonAuthOnuMac,
 ponCardRunningStatus,
 powerStatusBit) = mibBuilder.importSymbols(
    "FD-SYSTEM-MIB",
    "fanStatusBit",
    "nonAuthOnuMac",
    "ponCardRunningStatus",
    "powerStatusBit")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eponTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EponTrapsPrefix_ObjectIdentity = ObjectIdentity
eponTrapsPrefix = _EponTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0)
)
_FdTrapConformance_ObjectIdentity = ObjectIdentity
fdTrapConformance = _FdTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1)
)
_FdTrapGroups_ObjectIdentity = ObjectIdentity
fdTrapGroups = _FdTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 1)
)
_FdTrapCompliances_ObjectIdentity = ObjectIdentity
fdTrapCompliances = _FdTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 2)
)

# Managed Objects groups


# Notification objects

sniSFPStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 1)
)
sniSFPStatusChange.setObjects(
    ("FD-SWITCH-MIB", "sfpPlugStauts")
)
if mibBuilder.loadTexts:
    sniSFPStatusChange.setStatus(
        "current"
    )

sniPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 2)
)
sniPortLinkChange.setObjects(
    ("FD-SWITCH-MIB", "swPortLinkState")
)
if mibBuilder.loadTexts:
    sniPortLinkChange.setStatus(
        "current"
    )

powerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 3)
)
powerStatusChange.setObjects(
    ("FD-SYSTEM-MIB", "powerStatusBit")
)
if mibBuilder.loadTexts:
    powerStatusChange.setStatus(
        "current"
    )

fanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 4)
)
fanStatusChange.setObjects(
    ("FD-SYSTEM-MIB", "fanStatusBit")
)
if mibBuilder.loadTexts:
    fanStatusChange.setStatus(
        "current"
    )

ponRunningStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 5)
)
ponRunningStatusChange.setObjects(
    ("FD-SYSTEM-MIB", "ponCardRunningStatus")
)
if mibBuilder.loadTexts:
    ponRunningStatusChange.setStatus(
        "current"
    )

onuLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 6)
)
onuLinkStatusChange.setObjects(
    ("FD-OLT-MIB", "linkOnLineStatus")
)
if mibBuilder.loadTexts:
    onuLinkStatusChange.setStatus(
        "current"
    )

onuOnlineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 7)
)
onuOnlineStatusChange.setObjects(
    ("FD-ONU-MIB", "onuOnLineStatus")
)
if mibBuilder.loadTexts:
    onuOnlineStatusChange.setStatus(
        "current"
    )

onuPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 8)
)
onuPortStatusChange.setObjects(
    ("FD-ONU-MIB", "uniPortLink")
)
if mibBuilder.loadTexts:
    onuPortStatusChange.setStatus(
        "current"
    )

swSniPortTrafficChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 9)
)
swSniPortTrafficChange.setObjects(
    ("FD-PERFORMANCE-MIB", "swSniPortTrafficChangeVal")
)
if mibBuilder.loadTexts:
    swSniPortTrafficChange.setStatus(
        "current"
    )

oltTrafficChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 10)
)
oltTrafficChange.setObjects(
    ("FD-PERFORMANCE-MIB", "oltTrafficChangeVal")
)
if mibBuilder.loadTexts:
    oltTrafficChange.setStatus(
        "current"
    )

onuTrafficChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 11)
)
onuTrafficChange.setObjects(
    ("FD-PERFORMANCE-MIB", "onuTrafficChangeVal")
)
if mibBuilder.loadTexts:
    onuTrafficChange.setStatus(
        "current"
    )

linkIdResourceExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 12)
)
linkIdResourceExhaust.setObjects(
    ("FD-OLT-MIB", "linkIdExhaust")
)
if mibBuilder.loadTexts:
    linkIdResourceExhaust.setStatus(
        "current"
    )

onuIdResourceExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 13)
)
onuIdResourceExhaust.setObjects(
    ("FD-OLT-MIB", "onuIdExhaust")
)
if mibBuilder.loadTexts:
    onuIdResourceExhaust.setStatus(
        "current"
    )

illegalRegisterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 14)
)
illegalRegisterAlarm.setObjects(
    ("FD-SYSTEM-MIB", "nonAuthOnuMac")
)
if mibBuilder.loadTexts:
    illegalRegisterAlarm.setStatus(
        "current"
    )

onuPortRstpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 0, 15)
)
onuPortRstpStateChange.setObjects(
    ("FD-ONU-MIB", "uniPortRstpState")
)
if mibBuilder.loadTexts:
    onuPortRstpStateChange.setStatus(
        "current"
    )


# Notifications groups

fdTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 1, 1)
)
fdTrapGroup.setObjects(
      *(("FD-TRAP-MIB", "sniSFPStatusChange"),
        ("FD-TRAP-MIB", "sniPortLinkChange"),
        ("FD-TRAP-MIB", "powerStatusChange"),
        ("FD-TRAP-MIB", "fanStatusChange"),
        ("FD-TRAP-MIB", "ponRunningStatusChange"),
        ("FD-TRAP-MIB", "onuLinkStatusChange"),
        ("FD-TRAP-MIB", "onuOnlineStatusChange"),
        ("FD-TRAP-MIB", "onuPortStatusChange"),
        ("FD-TRAP-MIB", "swSniPortTrafficChange"),
        ("FD-TRAP-MIB", "oltTrafficChange"),
        ("FD-TRAP-MIB", "onuTrafficChange"),
        ("FD-TRAP-MIB", "onuPortRstpStateChange"),
        ("FD-TRAP-MIB", "illegalRegisterAlarm"),
        ("FD-TRAP-MIB", "linkIdResourceExhaust"),
        ("FD-TRAP-MIB", "onuIdResourceExhaust"))
)
if mibBuilder.loadTexts:
    fdTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fdTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fdTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-TRAP-MIB",
    **{"eponTraps": eponTraps,
       "eponTrapsPrefix": eponTrapsPrefix,
       "sniSFPStatusChange": sniSFPStatusChange,
       "sniPortLinkChange": sniPortLinkChange,
       "powerStatusChange": powerStatusChange,
       "fanStatusChange": fanStatusChange,
       "ponRunningStatusChange": ponRunningStatusChange,
       "onuLinkStatusChange": onuLinkStatusChange,
       "onuOnlineStatusChange": onuOnlineStatusChange,
       "onuPortStatusChange": onuPortStatusChange,
       "swSniPortTrafficChange": swSniPortTrafficChange,
       "oltTrafficChange": oltTrafficChange,
       "onuTrafficChange": onuTrafficChange,
       "linkIdResourceExhaust": linkIdResourceExhaust,
       "onuIdResourceExhaust": onuIdResourceExhaust,
       "illegalRegisterAlarm": illegalRegisterAlarm,
       "onuPortRstpStateChange": onuPortRstpStateChange,
       "fdTrapConformance": fdTrapConformance,
       "fdTrapGroups": fdTrapGroups,
       "fdTrapGroup": fdTrapGroup,
       "fdTrapCompliances": fdTrapCompliances,
       "fdTrapCompliance": fdTrapCompliance}
)
