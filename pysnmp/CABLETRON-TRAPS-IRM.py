# SNMP MIB module (CABLETRON-TRAPS-IRM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABLETRON-TRAPS-IRM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:18 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(boardIndex,
 boardSrcAddrLocked) = mibBuilder.importSymbols(
    "IRM3-MIB",
    "boardIndex",
    "boardSrcAddrLocked")

(devBroadThreshold,
 devCollsThreshold,
 devErrorSource,
 devErrorThreshold,
 devTrafficThreshold,
 deviceSrcAddrLocked,
 deviceTimeBase) = mibBuilder.importSymbols(
    "REPEATER-MIB-2",
    "devBroadThreshold",
    "devCollsThreshold",
    "devErrorSource",
    "devErrorThreshold",
    "devTrafficThreshold",
    "deviceSrcAddrLocked",
    "deviceTimeBase")

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
 NotificationType,
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
    "NotificationType",
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

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)

# Managed Objects groups


# Notification objects

deviceTrafficThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 268)
)
deviceTrafficThresholdExceeded.setObjects(
      *(("REPEATER-MIB-2", "devTrafficThreshold"),
        ("REPEATER-MIB-2", "deviceTimeBase"))
)
if mibBuilder.loadTexts:
    deviceTrafficThresholdExceeded.setStatus(
        ""
    )

deviceErrorThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 269)
)
deviceErrorThresholdExceeded.setObjects(
      *(("REPEATER-MIB-2", "devErrorThreshold"),
        ("REPEATER-MIB-2", "devErrorSource"),
        ("REPEATER-MIB-2", "deviceTimeBase"))
)
if mibBuilder.loadTexts:
    deviceErrorThresholdExceeded.setStatus(
        ""
    )

deviceCollsionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 270)
)
deviceCollsionThresholdExceeded.setObjects(
      *(("REPEATER-MIB-2", "devCollsThreshold"),
        ("REPEATER-MIB-2", "deviceTimeBase"))
)
if mibBuilder.loadTexts:
    deviceCollsionThresholdExceeded.setStatus(
        ""
    )

lockStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 278)
)
lockStatusChanged.setObjects(
    ("REPEATER-MIB-2", "deviceSrcAddrLocked")
)
if mibBuilder.loadTexts:
    lockStatusChanged.setStatus(
        ""
    )

deviceBroadcastThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 288)
)
deviceBroadcastThresholdExceeded.setObjects(
      *(("REPEATER-MIB-2", "devBroadThreshold"),
        ("REPEATER-MIB-2", "deviceTimeBase"))
)
if mibBuilder.loadTexts:
    deviceBroadcastThresholdExceeded.setStatus(
        ""
    )

srcAddressPortGrpLockStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 0, 308)
)
srcAddressPortGrpLockStatusChange.setObjects(
      *(("IRM3-MIB", "boardIndex"),
        ("IRM3-MIB", "boardSrcAddrLocked"))
)
if mibBuilder.loadTexts:
    srcAddressPortGrpLockStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABLETRON-TRAPS-IRM",
    **{"cabletron": cabletron,
       "deviceTrafficThresholdExceeded": deviceTrafficThresholdExceeded,
       "deviceErrorThresholdExceeded": deviceErrorThresholdExceeded,
       "deviceCollsionThresholdExceeded": deviceCollsionThresholdExceeded,
       "lockStatusChanged": lockStatusChanged,
       "deviceBroadcastThresholdExceeded": deviceBroadcastThresholdExceeded,
       "srcAddressPortGrpLockStatusChange": srcAddressPortGrpLockStatusChange}
)
