# SNMP MIB module (FORTINET-TRAP-MIB-280) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-TRAP-MIB-280
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:38 2024
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

(fnIpsSigId,
 fnIpsSigSrcIp,
 fnSysSerial,
 fnTraps) = mibBuilder.importSymbols(
    "FORTINET-MIB-280",
    "fnIpsSigId",
    "fnIpsSigSrcIp",
    "fnSysSerial",
    "fnTraps")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
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

fnTrapCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 101)
)
fnTrapCpuHigh.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapCpuHigh.setStatus(
        "current"
    )

fnTrapMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 102)
)
fnTrapMemLow.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapMemLow.setStatus(
        "current"
    )

fnTrapLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 103)
)
fnTrapLogFull.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapLogFull.setStatus(
        "current"
    )

fnTrapIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 201)
)
fnTrapIpChange.setObjects(
      *(("FORTINET-MIB-280", "fnSysSerial"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    fnTrapIpChange.setStatus(
        "current"
    )

fnTrapVpnTunUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 301)
)
fnTrapVpnTunUp.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapVpnTunUp.setStatus(
        "current"
    )

fnTrapVpnTunDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 302)
)
fnTrapVpnTunDown.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapVpnTunDown.setStatus(
        "current"
    )

fnTrapHaSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 401)
)
fnTrapHaSwitch.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaSwitch.setStatus(
        "current"
    )

fnTrapHaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 402)
)
fnTrapHaStateChange.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaStateChange.setStatus(
        "current"
    )

fnTrapIdsSynFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 501)
)
fnTrapIdsSynFlood.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapIdsSynFlood.setStatus(
        "current"
    )

fnTrapIdsPortScan = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 502)
)
fnTrapIdsPortScan.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapIdsPortScan.setStatus(
        "current"
    )

fnTrapIpsSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 503)
)
fnTrapIpsSignature.setObjects(
      *(("FORTINET-MIB-280", "fnSysSerial"),
        ("FORTINET-MIB-280", "fnIpsSigId"),
        ("FORTINET-MIB-280", "fnIpsSigSrcIp"))
)
if mibBuilder.loadTexts:
    fnTrapIpsSignature.setStatus(
        "current"
    )

fnTrapIpsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 504)
)
fnTrapIpsAnomaly.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapIpsAnomaly.setStatus(
        "current"
    )

fnTrapAvEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 601)
)
fnTrapAvEvent.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapAvEvent.setStatus(
        "current"
    )

fnTrapBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 701)
)
fnTrapBridge.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapBridge.setStatus(
        "current"
    )

fnTrapImTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 801)
)
fnTrapImTableFull.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapImTableFull.setStatus(
        "current"
    )

fnTrapFlgEventCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 901)
)
fnTrapFlgEventCount.setObjects(
    ("FORTINET-MIB-280", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapFlgEventCount.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-TRAP-MIB-280",
    **{"fnTrapCpuHigh": fnTrapCpuHigh,
       "fnTrapMemLow": fnTrapMemLow,
       "fnTrapLogFull": fnTrapLogFull,
       "fnTrapIpChange": fnTrapIpChange,
       "fnTrapVpnTunUp": fnTrapVpnTunUp,
       "fnTrapVpnTunDown": fnTrapVpnTunDown,
       "fnTrapHaSwitch": fnTrapHaSwitch,
       "fnTrapHaStateChange": fnTrapHaStateChange,
       "fnTrapIdsSynFlood": fnTrapIdsSynFlood,
       "fnTrapIdsPortScan": fnTrapIdsPortScan,
       "fnTrapIpsSignature": fnTrapIpsSignature,
       "fnTrapIpsAnomaly": fnTrapIpsAnomaly,
       "fnTrapAvEvent": fnTrapAvEvent,
       "fnTrapBridge": fnTrapBridge,
       "fnTrapImTableFull": fnTrapImTableFull,
       "fnTrapFlgEventCount": fnTrapFlgEventCount}
)
