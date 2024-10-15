# SNMP MIB module (ZYXEL-ERR-DISABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ERR-DISABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:39 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelErrdisable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelErrdisableSetup_ObjectIdentity = ObjectIdentity
zyxelErrdisableSetup = _ZyxelErrdisableSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1)
)
_ZyxelErrdisableRecovery_ObjectIdentity = ObjectIdentity
zyxelErrdisableRecovery = _ZyxelErrdisableRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1)
)
_ZyErrdisableRecoveryState_Type = EnabledStatus
_ZyErrdisableRecoveryState_Object = MibScalar
zyErrdisableRecoveryState = _ZyErrdisableRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 1),
    _ZyErrdisableRecoveryState_Type()
)
zyErrdisableRecoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryState.setStatus("current")
_ZyxelErrdisableRecoveryReasonTable_Object = MibTable
zyxelErrdisableRecoveryReasonTable = _ZyxelErrdisableRecoveryReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelErrdisableRecoveryReasonTable.setStatus("current")
_ZyxelErrdisableRecoveryReasonEntry_Object = MibTableRow
zyxelErrdisableRecoveryReasonEntry = _ZyxelErrdisableRecoveryReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 2, 1)
)
zyxelErrdisableRecoveryReasonEntry.setIndexNames(
    (0, "ZYXEL-ERR-DISABLE-MIB", "zyErrdisableRecoveryReasonType"),
)
if mibBuilder.loadTexts:
    zyxelErrdisableRecoveryReasonEntry.setStatus("current")


class _ZyErrdisableRecoveryReasonType_Type(Integer32):
    """Custom type zyErrdisableRecoveryReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("loopguard", 0))
    )


_ZyErrdisableRecoveryReasonType_Type.__name__ = "Integer32"
_ZyErrdisableRecoveryReasonType_Object = MibTableColumn
zyErrdisableRecoveryReasonType = _ZyErrdisableRecoveryReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 2, 1, 1),
    _ZyErrdisableRecoveryReasonType_Type()
)
zyErrdisableRecoveryReasonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryReasonType.setStatus("current")
_ZyErrdisableRecoveryReasonState_Type = EnabledStatus
_ZyErrdisableRecoveryReasonState_Object = MibTableColumn
zyErrdisableRecoveryReasonState = _ZyErrdisableRecoveryReasonState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 2, 1, 2),
    _ZyErrdisableRecoveryReasonState_Type()
)
zyErrdisableRecoveryReasonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryReasonState.setStatus("current")


class _ZyErrdisableRecoveryReasonInterval_Type(Integer32):
    """Custom type zyErrdisableRecoveryReasonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ZyErrdisableRecoveryReasonInterval_Type.__name__ = "Integer32"
_ZyErrdisableRecoveryReasonInterval_Object = MibTableColumn
zyErrdisableRecoveryReasonInterval = _ZyErrdisableRecoveryReasonInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 1, 2, 1, 3),
    _ZyErrdisableRecoveryReasonInterval_Type()
)
zyErrdisableRecoveryReasonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryReasonInterval.setStatus("current")
_ZyxelErrdisableDetect_ObjectIdentity = ObjectIdentity
zyxelErrdisableDetect = _ZyxelErrdisableDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2)
)
_ZyxelErrdisableDetectReasonTable_Object = MibTable
zyxelErrdisableDetectReasonTable = _ZyxelErrdisableDetectReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelErrdisableDetectReasonTable.setStatus("current")
_ZyxelErrdisableDetectReasonEntry_Object = MibTableRow
zyxelErrdisableDetectReasonEntry = _ZyxelErrdisableDetectReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2, 1, 1)
)
zyxelErrdisableDetectReasonEntry.setIndexNames(
    (0, "ZYXEL-ERR-DISABLE-MIB", "zyErrdisableDetectReasonType"),
)
if mibBuilder.loadTexts:
    zyxelErrdisableDetectReasonEntry.setStatus("current")


class _ZyErrdisableDetectReasonType_Type(Integer32):
    """Custom type zyErrdisableDetectReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_ZyErrdisableDetectReasonType_Type.__name__ = "Integer32"
_ZyErrdisableDetectReasonType_Object = MibTableColumn
zyErrdisableDetectReasonType = _ZyErrdisableDetectReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2, 1, 1, 1),
    _ZyErrdisableDetectReasonType_Type()
)
zyErrdisableDetectReasonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyErrdisableDetectReasonType.setStatus("current")
_ZyErrdisableDetectReasonState_Type = EnabledStatus
_ZyErrdisableDetectReasonState_Object = MibTableColumn
zyErrdisableDetectReasonState = _ZyErrdisableDetectReasonState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2, 1, 1, 2),
    _ZyErrdisableDetectReasonState_Type()
)
zyErrdisableDetectReasonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyErrdisableDetectReasonState.setStatus("current")


class _ZyErrdisableDetectReasonMode_Type(Integer32):
    """Custom type zyErrdisableDetectReasonMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactivePort", 1),
          ("inactiveReason", 2),
          ("rateLimitation", 3))
    )


_ZyErrdisableDetectReasonMode_Type.__name__ = "Integer32"
_ZyErrdisableDetectReasonMode_Object = MibTableColumn
zyErrdisableDetectReasonMode = _ZyErrdisableDetectReasonMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 1, 2, 1, 1, 3),
    _ZyErrdisableDetectReasonMode_Type()
)
zyErrdisableDetectReasonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyErrdisableDetectReasonMode.setStatus("current")
_ZyxelErrdisableStatus_ObjectIdentity = ObjectIdentity
zyxelErrdisableStatus = _ZyxelErrdisableStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2)
)
_ZyxelErrdisableRecoveryTable_Object = MibTable
zyxelErrdisableRecoveryTable = _ZyxelErrdisableRecoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelErrdisableRecoveryTable.setStatus("current")
_ZyxelErrdisableRecoveryEntry_Object = MibTableRow
zyxelErrdisableRecoveryEntry = _ZyxelErrdisableRecoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2, 1, 1)
)
zyxelErrdisableRecoveryEntry.setIndexNames(
    (0, "ZYXEL-ERR-DISABLE-MIB", "zyErrdisableRecoveryType"),
    (0, "ZYXEL-ERR-DISABLE-MIB", "zyErrdisableRecoveryPort"),
)
if mibBuilder.loadTexts:
    zyxelErrdisableRecoveryEntry.setStatus("current")


class _ZyErrdisableRecoveryType_Type(Integer32):
    """Custom type zyErrdisableRecoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("loopguard", 0))
    )


_ZyErrdisableRecoveryType_Type.__name__ = "Integer32"
_ZyErrdisableRecoveryType_Object = MibTableColumn
zyErrdisableRecoveryType = _ZyErrdisableRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2, 1, 1, 1),
    _ZyErrdisableRecoveryType_Type()
)
zyErrdisableRecoveryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryType.setStatus("current")
_ZyErrdisableRecoveryPort_Type = Integer32
_ZyErrdisableRecoveryPort_Object = MibTableColumn
zyErrdisableRecoveryPort = _ZyErrdisableRecoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2, 1, 1, 2),
    _ZyErrdisableRecoveryPort_Type()
)
zyErrdisableRecoveryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryPort.setStatus("current")


class _ZyErrdisableRecoveryTimeToRecover_Type(Integer32):
    """Custom type zyErrdisableRecoveryTimeToRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ZyErrdisableRecoveryTimeToRecover_Type.__name__ = "Integer32"
_ZyErrdisableRecoveryTimeToRecover_Object = MibTableColumn
zyErrdisableRecoveryTimeToRecover = _ZyErrdisableRecoveryTimeToRecover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 2, 1, 1, 3),
    _ZyErrdisableRecoveryTimeToRecover_Type()
)
zyErrdisableRecoveryTimeToRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyErrdisableRecoveryTimeToRecover.setStatus("current")
_ZyxelErrdisableTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelErrdisableTrapInfoObject = _ZyxelErrdisableTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 3)
)
_ZyErrdisableTrapPort_Type = Integer32
_ZyErrdisableTrapPort_Object = MibScalar
zyErrdisableTrapPort = _ZyErrdisableTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 3, 1),
    _ZyErrdisableTrapPort_Type()
)
zyErrdisableTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyErrdisableTrapPort.setStatus("current")


class _ZyErrdisableTrapReasonType_Type(Integer32):
    """Custom type zyErrdisableTrapReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("loopguard", 0))
    )


_ZyErrdisableTrapReasonType_Type.__name__ = "Integer32"
_ZyErrdisableTrapReasonType_Object = MibScalar
zyErrdisableTrapReasonType = _ZyErrdisableTrapReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 3, 2),
    _ZyErrdisableTrapReasonType_Type()
)
zyErrdisableTrapReasonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyErrdisableTrapReasonType.setStatus("current")


class _ZyErrdisableTrapMode_Type(Integer32):
    """Custom type zyErrdisableTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactivePort", 0),
          ("inactiveReason", 1),
          ("rateLimitation", 2))
    )


_ZyErrdisableTrapMode_Type.__name__ = "Integer32"
_ZyErrdisableTrapMode_Object = MibScalar
zyErrdisableTrapMode = _ZyErrdisableTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 3, 3),
    _ZyErrdisableTrapMode_Type()
)
zyErrdisableTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyErrdisableTrapMode.setStatus("current")
_ZyxelErrdisableNotifications_ObjectIdentity = ObjectIdentity
zyxelErrdisableNotifications = _ZyxelErrdisableNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 4)
)

# Managed Objects groups


# Notification objects

zyErrdisableDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 4, 1)
)
zyErrdisableDetect.setObjects(
      *(("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapPort"),
        ("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapReasonType"),
        ("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapMode"))
)
if mibBuilder.loadTexts:
    zyErrdisableDetect.setStatus(
        "current"
    )

zyErrdisableRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 24, 4, 2)
)
zyErrdisableRecovery.setObjects(
      *(("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapPort"),
        ("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapReasonType"),
        ("ZYXEL-ERR-DISABLE-MIB", "zyErrdisableTrapMode"))
)
if mibBuilder.loadTexts:
    zyErrdisableRecovery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ERR-DISABLE-MIB",
    **{"zyxelErrdisable": zyxelErrdisable,
       "zyxelErrdisableSetup": zyxelErrdisableSetup,
       "zyxelErrdisableRecovery": zyxelErrdisableRecovery,
       "zyErrdisableRecoveryState": zyErrdisableRecoveryState,
       "zyxelErrdisableRecoveryReasonTable": zyxelErrdisableRecoveryReasonTable,
       "zyxelErrdisableRecoveryReasonEntry": zyxelErrdisableRecoveryReasonEntry,
       "zyErrdisableRecoveryReasonType": zyErrdisableRecoveryReasonType,
       "zyErrdisableRecoveryReasonState": zyErrdisableRecoveryReasonState,
       "zyErrdisableRecoveryReasonInterval": zyErrdisableRecoveryReasonInterval,
       "zyxelErrdisableDetect": zyxelErrdisableDetect,
       "zyxelErrdisableDetectReasonTable": zyxelErrdisableDetectReasonTable,
       "zyxelErrdisableDetectReasonEntry": zyxelErrdisableDetectReasonEntry,
       "zyErrdisableDetectReasonType": zyErrdisableDetectReasonType,
       "zyErrdisableDetectReasonState": zyErrdisableDetectReasonState,
       "zyErrdisableDetectReasonMode": zyErrdisableDetectReasonMode,
       "zyxelErrdisableStatus": zyxelErrdisableStatus,
       "zyxelErrdisableRecoveryTable": zyxelErrdisableRecoveryTable,
       "zyxelErrdisableRecoveryEntry": zyxelErrdisableRecoveryEntry,
       "zyErrdisableRecoveryType": zyErrdisableRecoveryType,
       "zyErrdisableRecoveryPort": zyErrdisableRecoveryPort,
       "zyErrdisableRecoveryTimeToRecover": zyErrdisableRecoveryTimeToRecover,
       "zyxelErrdisableTrapInfoObject": zyxelErrdisableTrapInfoObject,
       "zyErrdisableTrapPort": zyErrdisableTrapPort,
       "zyErrdisableTrapReasonType": zyErrdisableTrapReasonType,
       "zyErrdisableTrapMode": zyErrdisableTrapMode,
       "zyxelErrdisableNotifications": zyxelErrdisableNotifications,
       "zyErrdisableDetect": zyErrdisableDetect,
       "zyErrdisableRecovery": zyErrdisableRecovery}
)
