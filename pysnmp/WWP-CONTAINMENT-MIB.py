# SNMP MIB module (WWP-CONTAINMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-CONTAINMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:36 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpContainmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpContainmentMIBObjects_ObjectIdentity = ObjectIdentity
wwpContainmentMIBObjects = _WwpContainmentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1)
)
_WwpContainment_ObjectIdentity = ObjectIdentity
wwpContainment = _WwpContainment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1)
)
_WwpContainmentBroadcastTable_Object = MibTable
wwpContainmentBroadcastTable = _WwpContainmentBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpContainmentBroadcastTable.setStatus("current")
_WwpContainmentBroadcastEntry_Object = MibTableRow
wwpContainmentBroadcastEntry = _WwpContainmentBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1)
)
wwpContainmentBroadcastEntry.setIndexNames(
    (0, "WWP-CONTAINMENT-MIB", "wwpContainmentBroadcastPortId"),
)
if mibBuilder.loadTexts:
    wwpContainmentBroadcastEntry.setStatus("current")


class _WwpContainmentBroadcastPortId_Type(Integer32):
    """Custom type wwpContainmentBroadcastPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpContainmentBroadcastPortId_Type.__name__ = "Integer32"
_WwpContainmentBroadcastPortId_Object = MibTableColumn
wwpContainmentBroadcastPortId = _WwpContainmentBroadcastPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 1),
    _WwpContainmentBroadcastPortId_Type()
)
wwpContainmentBroadcastPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastPortId.setStatus("current")


class _WwpContainmentBroadcastAction_Type(Integer32):
    """Custom type wwpContainmentBroadcastAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("monitor", 2),
          ("throttle", 3))
    )


_WwpContainmentBroadcastAction_Type.__name__ = "Integer32"
_WwpContainmentBroadcastAction_Object = MibTableColumn
wwpContainmentBroadcastAction = _WwpContainmentBroadcastAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 2),
    _WwpContainmentBroadcastAction_Type()
)
wwpContainmentBroadcastAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastAction.setStatus("current")


class _WwpContainmentBroadcastHighMark_Type(Integer32):
    """Custom type wwpContainmentBroadcastHighMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpContainmentBroadcastHighMark_Type.__name__ = "Integer32"
_WwpContainmentBroadcastHighMark_Object = MibTableColumn
wwpContainmentBroadcastHighMark = _WwpContainmentBroadcastHighMark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 3),
    _WwpContainmentBroadcastHighMark_Type()
)
wwpContainmentBroadcastHighMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastHighMark.setStatus("current")


class _WwpContainmentBroadcastLowMark_Type(Integer32):
    """Custom type wwpContainmentBroadcastLowMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpContainmentBroadcastLowMark_Type.__name__ = "Integer32"
_WwpContainmentBroadcastLowMark_Object = MibTableColumn
wwpContainmentBroadcastLowMark = _WwpContainmentBroadcastLowMark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 4),
    _WwpContainmentBroadcastLowMark_Type()
)
wwpContainmentBroadcastLowMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastLowMark.setStatus("current")


class _WwpContainmentBroadcastTrapsEnable_Type(TruthValue):
    """Custom type wwpContainmentBroadcastTrapsEnable based on TruthValue"""


_WwpContainmentBroadcastTrapsEnable_Object = MibTableColumn
wwpContainmentBroadcastTrapsEnable = _WwpContainmentBroadcastTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 5),
    _WwpContainmentBroadcastTrapsEnable_Type()
)
wwpContainmentBroadcastTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastTrapsEnable.setStatus("current")


class _WwpContainmentBroadcastState_Type(Integer32):
    """Custom type wwpContainmentBroadcastState based on Integer32"""
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
        *(("engaged", 3),
          ("idle", 1),
          ("starting", 2),
          ("stopping", 4))
    )


_WwpContainmentBroadcastState_Type.__name__ = "Integer32"
_WwpContainmentBroadcastState_Object = MibTableColumn
wwpContainmentBroadcastState = _WwpContainmentBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 1, 1, 6),
    _WwpContainmentBroadcastState_Type()
)
wwpContainmentBroadcastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpContainmentBroadcastState.setStatus("current")
_WwpContainmentMulticastTable_Object = MibTable
wwpContainmentMulticastTable = _WwpContainmentMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpContainmentMulticastTable.setStatus("current")
_WwpContainmentMulticastEntry_Object = MibTableRow
wwpContainmentMulticastEntry = _WwpContainmentMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1)
)
wwpContainmentMulticastEntry.setIndexNames(
    (0, "WWP-CONTAINMENT-MIB", "wwpContainmentMulticastPortId"),
)
if mibBuilder.loadTexts:
    wwpContainmentMulticastEntry.setStatus("current")


class _WwpContainmentMulticastPortId_Type(Integer32):
    """Custom type wwpContainmentMulticastPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpContainmentMulticastPortId_Type.__name__ = "Integer32"
_WwpContainmentMulticastPortId_Object = MibTableColumn
wwpContainmentMulticastPortId = _WwpContainmentMulticastPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 1),
    _WwpContainmentMulticastPortId_Type()
)
wwpContainmentMulticastPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpContainmentMulticastPortId.setStatus("current")


class _WwpContainmentMulticastAction_Type(Integer32):
    """Custom type wwpContainmentMulticastAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("monitor", 2),
          ("throttle", 3))
    )


_WwpContainmentMulticastAction_Type.__name__ = "Integer32"
_WwpContainmentMulticastAction_Object = MibTableColumn
wwpContainmentMulticastAction = _WwpContainmentMulticastAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 2),
    _WwpContainmentMulticastAction_Type()
)
wwpContainmentMulticastAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentMulticastAction.setStatus("current")


class _WwpContainmentMulticastHighMark_Type(Integer32):
    """Custom type wwpContainmentMulticastHighMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpContainmentMulticastHighMark_Type.__name__ = "Integer32"
_WwpContainmentMulticastHighMark_Object = MibTableColumn
wwpContainmentMulticastHighMark = _WwpContainmentMulticastHighMark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 3),
    _WwpContainmentMulticastHighMark_Type()
)
wwpContainmentMulticastHighMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentMulticastHighMark.setStatus("current")


class _WwpContainmentMulticastLowMark_Type(Integer32):
    """Custom type wwpContainmentMulticastLowMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpContainmentMulticastLowMark_Type.__name__ = "Integer32"
_WwpContainmentMulticastLowMark_Object = MibTableColumn
wwpContainmentMulticastLowMark = _WwpContainmentMulticastLowMark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 4),
    _WwpContainmentMulticastLowMark_Type()
)
wwpContainmentMulticastLowMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentMulticastLowMark.setStatus("current")


class _WwpContainmentMulticastTrapsEnable_Type(TruthValue):
    """Custom type wwpContainmentMulticastTrapsEnable based on TruthValue"""


_WwpContainmentMulticastTrapsEnable_Object = MibTableColumn
wwpContainmentMulticastTrapsEnable = _WwpContainmentMulticastTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 5),
    _WwpContainmentMulticastTrapsEnable_Type()
)
wwpContainmentMulticastTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpContainmentMulticastTrapsEnable.setStatus("current")


class _WwpContainmentMulticastState_Type(Integer32):
    """Custom type wwpContainmentMulticastState based on Integer32"""
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
        *(("engaged", 3),
          ("idle", 1),
          ("starting", 2),
          ("stopping", 4))
    )


_WwpContainmentMulticastState_Type.__name__ = "Integer32"
_WwpContainmentMulticastState_Object = MibTableColumn
wwpContainmentMulticastState = _WwpContainmentMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 1, 1, 2, 1, 6),
    _WwpContainmentMulticastState_Type()
)
wwpContainmentMulticastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpContainmentMulticastState.setStatus("current")
_WwpContainmentMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpContainmentMIBNotificationPrefix = _WwpContainmentMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 2)
)
_WwpContainmentMIBNotifications_ObjectIdentity = ObjectIdentity
wwpContainmentMIBNotifications = _WwpContainmentMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 2, 0)
)
_WwpContainmentMIBConformance_ObjectIdentity = ObjectIdentity
wwpContainmentMIBConformance = _WwpContainmentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 3)
)
_WwpContainmentMIBCompliances_ObjectIdentity = ObjectIdentity
wwpContainmentMIBCompliances = _WwpContainmentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 3, 1)
)
_WwpContainmentMIBGroups_ObjectIdentity = ObjectIdentity
wwpContainmentMIBGroups = _WwpContainmentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpContainmentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 55, 2, 0, 1)
)
wwpContainmentNotification.setObjects(
      *(("WWP-CONTAINMENT-MIB", "wwpContainmentBroadcastState"),
        ("WWP-CONTAINMENT-MIB", "wwpContainmentMulticastState"))
)
if mibBuilder.loadTexts:
    wwpContainmentNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-CONTAINMENT-MIB",
    **{"wwpContainmentMIB": wwpContainmentMIB,
       "wwpContainmentMIBObjects": wwpContainmentMIBObjects,
       "wwpContainment": wwpContainment,
       "wwpContainmentBroadcastTable": wwpContainmentBroadcastTable,
       "wwpContainmentBroadcastEntry": wwpContainmentBroadcastEntry,
       "wwpContainmentBroadcastPortId": wwpContainmentBroadcastPortId,
       "wwpContainmentBroadcastAction": wwpContainmentBroadcastAction,
       "wwpContainmentBroadcastHighMark": wwpContainmentBroadcastHighMark,
       "wwpContainmentBroadcastLowMark": wwpContainmentBroadcastLowMark,
       "wwpContainmentBroadcastTrapsEnable": wwpContainmentBroadcastTrapsEnable,
       "wwpContainmentBroadcastState": wwpContainmentBroadcastState,
       "wwpContainmentMulticastTable": wwpContainmentMulticastTable,
       "wwpContainmentMulticastEntry": wwpContainmentMulticastEntry,
       "wwpContainmentMulticastPortId": wwpContainmentMulticastPortId,
       "wwpContainmentMulticastAction": wwpContainmentMulticastAction,
       "wwpContainmentMulticastHighMark": wwpContainmentMulticastHighMark,
       "wwpContainmentMulticastLowMark": wwpContainmentMulticastLowMark,
       "wwpContainmentMulticastTrapsEnable": wwpContainmentMulticastTrapsEnable,
       "wwpContainmentMulticastState": wwpContainmentMulticastState,
       "wwpContainmentMIBNotificationPrefix": wwpContainmentMIBNotificationPrefix,
       "wwpContainmentMIBNotifications": wwpContainmentMIBNotifications,
       "wwpContainmentNotification": wwpContainmentNotification,
       "wwpContainmentMIBConformance": wwpContainmentMIBConformance,
       "wwpContainmentMIBCompliances": wwpContainmentMIBCompliances,
       "wwpContainmentMIBGroups": wwpContainmentMIBGroups}
)
