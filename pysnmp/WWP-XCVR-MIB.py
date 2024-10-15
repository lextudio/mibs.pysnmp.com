# SNMP MIB module (WWP-XCVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-XCVR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:28 2024
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpXcvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14)
)
wwpXcvrMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpXcvrMIBObjects_ObjectIdentity = ObjectIdentity
wwpXcvrMIBObjects = _WwpXcvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1)
)
_WwpXcvr_ObjectIdentity = ObjectIdentity
wwpXcvr = _WwpXcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1)
)
_WwpXcvrTable_Object = MibTable
wwpXcvrTable = _WwpXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpXcvrTable.setStatus("current")
_WwpXcvrEntry_Object = MibTableRow
wwpXcvrEntry = _WwpXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1)
)
wwpXcvrEntry.setIndexNames(
    (0, "WWP-XCVR-MIB", "wwpXcvrPortXcvrId"),
    (0, "WWP-XCVR-MIB", "wwpXcvrId"),
)
if mibBuilder.loadTexts:
    wwpXcvrEntry.setStatus("current")


class _WwpXcvrPortXcvrId_Type(Integer32):
    """Custom type wwpXcvrPortXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpXcvrPortXcvrId_Type.__name__ = "Integer32"
_WwpXcvrPortXcvrId_Object = MibTableColumn
wwpXcvrPortXcvrId = _WwpXcvrPortXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 1),
    _WwpXcvrPortXcvrId_Type()
)
wwpXcvrPortXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrPortXcvrId.setStatus("current")


class _WwpXcvrId_Type(Integer32):
    """Custom type wwpXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WwpXcvrId_Type.__name__ = "Integer32"
_WwpXcvrId_Object = MibTableColumn
wwpXcvrId = _WwpXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 2),
    _WwpXcvrId_Type()
)
wwpXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrId.setStatus("current")


class _WwpXcvrFiberType_Type(Integer32):
    """Custom type wwpXcvrFiberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cx", 3),
          ("lx", 1),
          ("sx", 2),
          ("t", 4),
          ("unknown", 5))
    )


_WwpXcvrFiberType_Type.__name__ = "Integer32"
_WwpXcvrFiberType_Object = MibTableColumn
wwpXcvrFiberType = _WwpXcvrFiberType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 3),
    _WwpXcvrFiberType_Type()
)
wwpXcvrFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrFiberType.setStatus("current")
_WwpXcvrVendorName_Type = DisplayString
_WwpXcvrVendorName_Object = MibTableColumn
wwpXcvrVendorName = _WwpXcvrVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 4),
    _WwpXcvrVendorName_Type()
)
wwpXcvrVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrVendorName.setStatus("current")
_WwpXcvrPartNum_Type = DisplayString
_WwpXcvrPartNum_Object = MibTableColumn
wwpXcvrPartNum = _WwpXcvrPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 5),
    _WwpXcvrPartNum_Type()
)
wwpXcvrPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrPartNum.setStatus("current")
_WwpXcvrPartRev_Type = DisplayString
_WwpXcvrPartRev_Object = MibTableColumn
wwpXcvrPartRev = _WwpXcvrPartRev_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 6),
    _WwpXcvrPartRev_Type()
)
wwpXcvrPartRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrPartRev.setStatus("current")


class _WwpXcvrTxEnabled_Type(Integer32):
    """Custom type wwpXcvrTxEnabled based on Integer32"""
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


_WwpXcvrTxEnabled_Type.__name__ = "Integer32"
_WwpXcvrTxEnabled_Object = MibTableColumn
wwpXcvrTxEnabled = _WwpXcvrTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 7),
    _WwpXcvrTxEnabled_Type()
)
wwpXcvrTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpXcvrTxEnabled.setStatus("current")


class _WwpXcvrRxSignalStatus_Type(Integer32):
    """Custom type wwpXcvrRxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notDetected", 2))
    )


_WwpXcvrRxSignalStatus_Type.__name__ = "Integer32"
_WwpXcvrRxSignalStatus_Object = MibTableColumn
wwpXcvrRxSignalStatus = _WwpXcvrRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 8),
    _WwpXcvrRxSignalStatus_Type()
)
wwpXcvrRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrRxSignalStatus.setStatus("current")


class _WwpXcvrTxFaultStatus_Type(Integer32):
    """Custom type wwpXcvrTxFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("noFault", 2))
    )


_WwpXcvrTxFaultStatus_Type.__name__ = "Integer32"
_WwpXcvrTxFaultStatus_Object = MibTableColumn
wwpXcvrTxFaultStatus = _WwpXcvrTxFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 1, 1, 9),
    _WwpXcvrTxFaultStatus_Type()
)
wwpXcvrTxFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrTxFaultStatus.setStatus("current")
_WwpXcvrPortTable_Object = MibTable
wwpXcvrPortTable = _WwpXcvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpXcvrPortTable.setStatus("current")
_WwpXcvrPortEntry_Object = MibTableRow
wwpXcvrPortEntry = _WwpXcvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1)
)
wwpXcvrPortEntry.setIndexNames(
    (0, "WWP-XCVR-MIB", "wwpXcvrPortId"),
)
if mibBuilder.loadTexts:
    wwpXcvrPortEntry.setStatus("current")


class _WwpXcvrPortId_Type(Integer32):
    """Custom type wwpXcvrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpXcvrPortId_Type.__name__ = "Integer32"
_WwpXcvrPortId_Object = MibTableColumn
wwpXcvrPortId = _WwpXcvrPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 1),
    _WwpXcvrPortId_Type()
)
wwpXcvrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrPortId.setStatus("current")


class _WwpXcvrPortHoldDownTime_Type(Integer32):
    """Custom type wwpXcvrPortHoldDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WwpXcvrPortHoldDownTime_Type.__name__ = "Integer32"
_WwpXcvrPortHoldDownTime_Object = MibTableColumn
wwpXcvrPortHoldDownTime = _WwpXcvrPortHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 2),
    _WwpXcvrPortHoldDownTime_Type()
)
wwpXcvrPortHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpXcvrPortHoldDownTime.setStatus("deprecated")


class _WwpXcvrPortRedOrDiagMode_Type(Integer32):
    """Custom type wwpXcvrPortRedOrDiagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpXcvrPortRedOrDiagMode_Type.__name__ = "Integer32"
_WwpXcvrPortRedOrDiagMode_Object = MibTableColumn
wwpXcvrPortRedOrDiagMode = _WwpXcvrPortRedOrDiagMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 3),
    _WwpXcvrPortRedOrDiagMode_Type()
)
wwpXcvrPortRedOrDiagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpXcvrPortRedOrDiagMode.setStatus("current")


class _WwpXcvrPortPreferredXcvr_Type(Integer32):
    """Custom type wwpXcvrPortPreferredXcvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpXcvrPortPreferredXcvr_Type.__name__ = "Integer32"
_WwpXcvrPortPreferredXcvr_Object = MibTableColumn
wwpXcvrPortPreferredXcvr = _WwpXcvrPortPreferredXcvr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 4),
    _WwpXcvrPortPreferredXcvr_Type()
)
wwpXcvrPortPreferredXcvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpXcvrPortPreferredXcvr.setStatus("current")


class _WwpXcvrPortActiveXcvr_Type(Integer32):
    """Custom type wwpXcvrPortActiveXcvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpXcvrPortActiveXcvr_Type.__name__ = "Integer32"
_WwpXcvrPortActiveXcvr_Object = MibTableColumn
wwpXcvrPortActiveXcvr = _WwpXcvrPortActiveXcvr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 1, 2, 1, 5),
    _WwpXcvrPortActiveXcvr_Type()
)
wwpXcvrPortActiveXcvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrPortActiveXcvr.setStatus("current")
_WwpXcvrNotif_ObjectIdentity = ObjectIdentity
wwpXcvrNotif = _WwpXcvrNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2)
)


class _WwpXcvrEventType_Type(Integer32):
    """Custom type wwpXcvrEventType based on Integer32"""
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
        *(("down", 2),
          ("none", 0),
          ("select", 3),
          ("up", 1))
    )


_WwpXcvrEventType_Type.__name__ = "Integer32"
_WwpXcvrEventType_Object = MibScalar
wwpXcvrEventType = _WwpXcvrEventType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2, 1),
    _WwpXcvrEventType_Type()
)
wwpXcvrEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrEventType.setStatus("current")


class _WwpXcvrErrorType_Type(Integer32):
    """Custom type wwpXcvrErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chksumFailed", 1),
          ("none", 0),
          ("opticalFault", 2))
    )


_WwpXcvrErrorType_Type.__name__ = "Integer32"
_WwpXcvrErrorType_Object = MibScalar
wwpXcvrErrorType = _WwpXcvrErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 1, 2, 2),
    _WwpXcvrErrorType_Type()
)
wwpXcvrErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpXcvrErrorType.setStatus("current")
_WwpXcvrMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpXcvrMIBNotificationPrefix = _WwpXcvrMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 2)
)
_WwpXcvrMIBNotifications_ObjectIdentity = ObjectIdentity
wwpXcvrMIBNotifications = _WwpXcvrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0)
)
_WwpXcvrMIBConformance_ObjectIdentity = ObjectIdentity
wwpXcvrMIBConformance = _WwpXcvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 3)
)
_WwpXcvrMIBCompliances_ObjectIdentity = ObjectIdentity
wwpXcvrMIBCompliances = _WwpXcvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 3, 1)
)
_WwpXcvrMIBGroups_ObjectIdentity = ObjectIdentity
wwpXcvrMIBGroups = _WwpXcvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpXcvrLinkStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0, 4)
)
wwpXcvrLinkStateChangeNotification.setObjects(
      *(("WWP-XCVR-MIB", "wwpXcvrPortId"),
        ("WWP-XCVR-MIB", "wwpXcvrId"),
        ("WWP-XCVR-MIB", "wwpXcvrEventType"))
)
if mibBuilder.loadTexts:
    wwpXcvrLinkStateChangeNotification.setStatus(
        "current"
    )

wwpXcvrErrorTypeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 14, 2, 0, 5)
)
wwpXcvrErrorTypeNotification.setObjects(
      *(("WWP-XCVR-MIB", "wwpXcvrPortId"),
        ("WWP-XCVR-MIB", "wwpXcvrId"),
        ("WWP-XCVR-MIB", "wwpXcvrErrorType"))
)
if mibBuilder.loadTexts:
    wwpXcvrErrorTypeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-XCVR-MIB",
    **{"wwpXcvrMIB": wwpXcvrMIB,
       "wwpXcvrMIBObjects": wwpXcvrMIBObjects,
       "wwpXcvr": wwpXcvr,
       "wwpXcvrTable": wwpXcvrTable,
       "wwpXcvrEntry": wwpXcvrEntry,
       "wwpXcvrPortXcvrId": wwpXcvrPortXcvrId,
       "wwpXcvrId": wwpXcvrId,
       "wwpXcvrFiberType": wwpXcvrFiberType,
       "wwpXcvrVendorName": wwpXcvrVendorName,
       "wwpXcvrPartNum": wwpXcvrPartNum,
       "wwpXcvrPartRev": wwpXcvrPartRev,
       "wwpXcvrTxEnabled": wwpXcvrTxEnabled,
       "wwpXcvrRxSignalStatus": wwpXcvrRxSignalStatus,
       "wwpXcvrTxFaultStatus": wwpXcvrTxFaultStatus,
       "wwpXcvrPortTable": wwpXcvrPortTable,
       "wwpXcvrPortEntry": wwpXcvrPortEntry,
       "wwpXcvrPortId": wwpXcvrPortId,
       "wwpXcvrPortHoldDownTime": wwpXcvrPortHoldDownTime,
       "wwpXcvrPortRedOrDiagMode": wwpXcvrPortRedOrDiagMode,
       "wwpXcvrPortPreferredXcvr": wwpXcvrPortPreferredXcvr,
       "wwpXcvrPortActiveXcvr": wwpXcvrPortActiveXcvr,
       "wwpXcvrNotif": wwpXcvrNotif,
       "wwpXcvrEventType": wwpXcvrEventType,
       "wwpXcvrErrorType": wwpXcvrErrorType,
       "wwpXcvrMIBNotificationPrefix": wwpXcvrMIBNotificationPrefix,
       "wwpXcvrMIBNotifications": wwpXcvrMIBNotifications,
       "wwpXcvrLinkStateChangeNotification": wwpXcvrLinkStateChangeNotification,
       "wwpXcvrErrorTypeNotification": wwpXcvrErrorTypeNotification,
       "wwpXcvrMIBConformance": wwpXcvrMIBConformance,
       "wwpXcvrMIBCompliances": wwpXcvrMIBCompliances,
       "wwpXcvrMIBGroups": wwpXcvrMIBGroups}
)
