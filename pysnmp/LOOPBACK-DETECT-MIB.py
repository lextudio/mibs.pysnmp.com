# SNMP MIB module (LOOPBACK-DETECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LOOPBACK-DETECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:21 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swLoopDetectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwLoopDetectCtrl_ObjectIdentity = ObjectIdentity
swLoopDetectCtrl = _SwLoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1)
)


class _SwLoopDetectAdminState_Type(Integer32):
    """Custom type swLoopDetectAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwLoopDetectAdminState_Type.__name__ = "Integer32"
_SwLoopDetectAdminState_Object = MibScalar
swLoopDetectAdminState = _SwLoopDetectAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 1),
    _SwLoopDetectAdminState_Type()
)
swLoopDetectAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectAdminState.setStatus("current")


class _SwLoopDetectInterval_Type(Integer32):
    """Custom type swLoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SwLoopDetectInterval_Type.__name__ = "Integer32"
_SwLoopDetectInterval_Object = MibScalar
swLoopDetectInterval = _SwLoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 2),
    _SwLoopDetectInterval_Type()
)
swLoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectInterval.setStatus("current")


class _SwLoopDetectRecoverTime_Type(Integer32):
    """Custom type swLoopDetectRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwLoopDetectRecoverTime_Type.__name__ = "Integer32"
_SwLoopDetectRecoverTime_Object = MibScalar
swLoopDetectRecoverTime = _SwLoopDetectRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 3),
    _SwLoopDetectRecoverTime_Type()
)
swLoopDetectRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectRecoverTime.setStatus("current")


class _SwLoopDetectMode_Type(Integer32):
    """Custom type swLoopDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 2),
          ("vlan-based", 1))
    )


_SwLoopDetectMode_Type.__name__ = "Integer32"
_SwLoopDetectMode_Object = MibScalar
swLoopDetectMode = _SwLoopDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 4),
    _SwLoopDetectMode_Type()
)
swLoopDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectMode.setStatus("current")


class _SwLoopDetectTrapMode_Type(Integer32):
    """Custom type swLoopDetectTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("loop-cleared", 3),
          ("loop-detected", 2),
          ("none", 1))
    )


_SwLoopDetectTrapMode_Type.__name__ = "Integer32"
_SwLoopDetectTrapMode_Object = MibScalar
swLoopDetectTrapMode = _SwLoopDetectTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 5),
    _SwLoopDetectTrapMode_Type()
)
swLoopDetectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectTrapMode.setStatus("current")


class _SwLoopDetectLogState_Type(Integer32):
    """Custom type swLoopDetectLogState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwLoopDetectLogState_Type.__name__ = "Integer32"
_SwLoopDetectLogState_Object = MibScalar
swLoopDetectLogState = _SwLoopDetectLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 6),
    _SwLoopDetectLogState_Type()
)
swLoopDetectLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectLogState.setStatus("current")
_SwLoopDetectInfo_ObjectIdentity = ObjectIdentity
swLoopDetectInfo = _SwLoopDetectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 2)
)
_SwLoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swLoopDetectPortMgmt = _SwLoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3)
)
_SwLoopDetectPortTable_Object = MibTable
swLoopDetectPortTable = _SwLoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1)
)
if mibBuilder.loadTexts:
    swLoopDetectPortTable.setStatus("current")
_SwLoopDetectPortEntry_Object = MibTableRow
swLoopDetectPortEntry = _SwLoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1)
)
swLoopDetectPortEntry.setIndexNames(
    (0, "LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"),
)
if mibBuilder.loadTexts:
    swLoopDetectPortEntry.setStatus("current")


class _SwLoopDetectPortIndex_Type(Integer32):
    """Custom type swLoopDetectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwLoopDetectPortIndex_Type.__name__ = "Integer32"
_SwLoopDetectPortIndex_Object = MibTableColumn
swLoopDetectPortIndex = _SwLoopDetectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 1),
    _SwLoopDetectPortIndex_Type()
)
swLoopDetectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoopDetectPortIndex.setStatus("current")


class _SwLoopDetectPortState_Type(Integer32):
    """Custom type swLoopDetectPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwLoopDetectPortState_Type.__name__ = "Integer32"
_SwLoopDetectPortState_Object = MibTableColumn
swLoopDetectPortState = _SwLoopDetectPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 2),
    _SwLoopDetectPortState_Type()
)
swLoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectPortState.setStatus("current")
_SwLoopDetectPortLoopVLAN_Type = DisplayString
_SwLoopDetectPortLoopVLAN_Object = MibTableColumn
swLoopDetectPortLoopVLAN = _SwLoopDetectPortLoopVLAN_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 3),
    _SwLoopDetectPortLoopVLAN_Type()
)
swLoopDetectPortLoopVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoopDetectPortLoopVLAN.setStatus("current")


class _SwLoopDetectPortLoopStatus_Type(Integer32):
    """Custom type swLoopDetectPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("loop", 2),
          ("normal", 1))
    )


_SwLoopDetectPortLoopStatus_Type.__name__ = "Integer32"
_SwLoopDetectPortLoopStatus_Object = MibTableColumn
swLoopDetectPortLoopStatus = _SwLoopDetectPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 4),
    _SwLoopDetectPortLoopStatus_Type()
)
swLoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoopDetectPortLoopStatus.setStatus("current")
_SwLoopDetectNotify_ObjectIdentity = ObjectIdentity
swLoopDetectNotify = _SwLoopDetectNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10)
)
_SwLoopDetectNotifyPrefix_ObjectIdentity = ObjectIdentity
swLoopDetectNotifyPrefix = _SwLoopDetectNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0)
)
_SwLoopDetectNotificationBidings_ObjectIdentity = ObjectIdentity
swLoopDetectNotificationBidings = _SwLoopDetectNotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 1)
)
_SwVlanLoopDetectVID_Type = Integer32
_SwVlanLoopDetectVID_Object = MibScalar
swVlanLoopDetectVID = _SwVlanLoopDetectVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 1, 1),
    _SwVlanLoopDetectVID_Type()
)
swVlanLoopDetectVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swVlanLoopDetectVID.setStatus("current")

# Managed Objects groups


# Notification objects

swPortLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 1)
)
swPortLoopOccurred.setObjects(
    ("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swPortLoopOccurred.setStatus(
        "current"
    )

swPortLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 2)
)
swPortLoopRestart.setObjects(
    ("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swPortLoopRestart.setStatus(
        "current"
    )

swVlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 3)
)
swVlanLoopOccurred.setObjects(
      *(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"),
        ("LOOPBACK-DETECT-MIB", "swVlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swVlanLoopOccurred.setStatus(
        "current"
    )

swVlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 4)
)
swVlanLoopRestart.setObjects(
      *(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"),
        ("LOOPBACK-DETECT-MIB", "swVlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swVlanLoopRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOOPBACK-DETECT-MIB",
    **{"swLoopDetectMIB": swLoopDetectMIB,
       "swLoopDetectCtrl": swLoopDetectCtrl,
       "swLoopDetectAdminState": swLoopDetectAdminState,
       "swLoopDetectInterval": swLoopDetectInterval,
       "swLoopDetectRecoverTime": swLoopDetectRecoverTime,
       "swLoopDetectMode": swLoopDetectMode,
       "swLoopDetectTrapMode": swLoopDetectTrapMode,
       "swLoopDetectLogState": swLoopDetectLogState,
       "swLoopDetectInfo": swLoopDetectInfo,
       "swLoopDetectPortMgmt": swLoopDetectPortMgmt,
       "swLoopDetectPortTable": swLoopDetectPortTable,
       "swLoopDetectPortEntry": swLoopDetectPortEntry,
       "swLoopDetectPortIndex": swLoopDetectPortIndex,
       "swLoopDetectPortState": swLoopDetectPortState,
       "swLoopDetectPortLoopVLAN": swLoopDetectPortLoopVLAN,
       "swLoopDetectPortLoopStatus": swLoopDetectPortLoopStatus,
       "swLoopDetectNotify": swLoopDetectNotify,
       "swLoopDetectNotifyPrefix": swLoopDetectNotifyPrefix,
       "swPortLoopOccurred": swPortLoopOccurred,
       "swPortLoopRestart": swPortLoopRestart,
       "swVlanLoopOccurred": swVlanLoopOccurred,
       "swVlanLoopRestart": swVlanLoopRestart,
       "swLoopDetectNotificationBidings": swLoopDetectNotificationBidings,
       "swVlanLoopDetectVID": swVlanLoopDetectVID}
)
