# SNMP MIB module (RBN-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:58 2024
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

(dot1dBasePortEntry,
 dot1dStpPortState) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry",
    "dot1dStpPortState")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnBridgeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42)
)
rbnBridgeMib.setRevisions(
        ("2008-08-27 00:00",
         "2008-02-25 00:00",
         "2007-06-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnBridgeNotifications_ObjectIdentity = ObjectIdentity
rbnBridgeNotifications = _RbnBridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 0)
)
_RbnBridgeObjects_ObjectIdentity = ObjectIdentity
rbnBridgeObjects = _RbnBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1)
)
_RbnBridgeNotify_ObjectIdentity = ObjectIdentity
rbnBridgeNotify = _RbnBridgeNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1)
)


class _RbnBridgeNotifyEnable_Type(TruthValue):
    """Custom type rbnBridgeNotifyEnable based on TruthValue"""


_RbnBridgeNotifyEnable_Object = MibScalar
rbnBridgeNotifyEnable = _RbnBridgeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 1),
    _RbnBridgeNotifyEnable_Type()
)
rbnBridgeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnBridgeNotifyEnable.setStatus("current")


class _RbnBridgeGroupName_Type(SnmpAdminString):
    """Custom type rbnBridgeGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbnBridgeGroupName_Type.__name__ = "SnmpAdminString"
_RbnBridgeGroupName_Object = MibScalar
rbnBridgeGroupName = _RbnBridgeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 2),
    _RbnBridgeGroupName_Type()
)
rbnBridgeGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnBridgeGroupName.setStatus("current")


class _RbnBridgeCircuitDescriptor_Type(SnmpAdminString):
    """Custom type rbnBridgeCircuitDescriptor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RbnBridgeCircuitDescriptor_Type.__name__ = "SnmpAdminString"
_RbnBridgeCircuitDescriptor_Object = MibScalar
rbnBridgeCircuitDescriptor = _RbnBridgeCircuitDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 3),
    _RbnBridgeCircuitDescriptor_Type()
)
rbnBridgeCircuitDescriptor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnBridgeCircuitDescriptor.setStatus("current")


class _RbnBridgeCircuitStatus_Type(Integer32):
    """Custom type rbnBridgeCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("cleared", 2))
    )


_RbnBridgeCircuitStatus_Type.__name__ = "Integer32"
_RbnBridgeCircuitStatus_Object = MibScalar
rbnBridgeCircuitStatus = _RbnBridgeCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 4),
    _RbnBridgeCircuitStatus_Type()
)
rbnBridgeCircuitStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnBridgeCircuitStatus.setStatus("current")


class _RbnBridgeGroupContextName_Type(SnmpAdminString):
    """Custom type rbnBridgeGroupContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBridgeGroupContextName_Type.__name__ = "SnmpAdminString"
_RbnBridgeGroupContextName_Object = MibScalar
rbnBridgeGroupContextName = _RbnBridgeGroupContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 5),
    _RbnBridgeGroupContextName_Type()
)
rbnBridgeGroupContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnBridgeGroupContextName.setStatus("current")


class _RbnBridgePortPreviousState_Type(Integer32):
    """Custom type rbnBridgePortPreviousState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_RbnBridgePortPreviousState_Type.__name__ = "Integer32"
_RbnBridgePortPreviousState_Object = MibScalar
rbnBridgePortPreviousState = _RbnBridgePortPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 6),
    _RbnBridgePortPreviousState_Type()
)
rbnBridgePortPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnBridgePortPreviousState.setStatus("current")
_RbnBridgeBase_ObjectIdentity = ObjectIdentity
rbnBridgeBase = _RbnBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2)
)
_RbnBridgeIdTable_Object = MibTable
rbnBridgeIdTable = _RbnBridgeIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnBridgeIdTable.setStatus("current")
_RbnBridgeIdEntry_Object = MibTableRow
rbnBridgeIdEntry = _RbnBridgeIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1)
)
rbnBridgeIdEntry.setIndexNames(
    (0, "RBN-BRIDGE-MIB", "rbnBridgeName"),
)
if mibBuilder.loadTexts:
    rbnBridgeIdEntry.setStatus("current")


class _RbnBridgeName_Type(SnmpAdminString):
    """Custom type rbnBridgeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbnBridgeName_Type.__name__ = "SnmpAdminString"
_RbnBridgeName_Object = MibTableColumn
rbnBridgeName = _RbnBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1, 1),
    _RbnBridgeName_Type()
)
rbnBridgeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnBridgeName.setStatus("current")


class _RbnBridgeId_Type(Integer32):
    """Custom type rbnBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbnBridgeId_Type.__name__ = "Integer32"
_RbnBridgeId_Object = MibTableColumn
rbnBridgeId = _RbnBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1, 2),
    _RbnBridgeId_Type()
)
rbnBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBridgeId.setStatus("current")
_RbnBridgePortCctDescrTable_Object = MibTable
rbnBridgePortCctDescrTable = _RbnBridgePortCctDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rbnBridgePortCctDescrTable.setStatus("current")
_RbnBridgePortCctDescrEntry_Object = MibTableRow
rbnBridgePortCctDescrEntry = _RbnBridgePortCctDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnBridgePortCctDescrEntry.setStatus("current")


class _RbnBridgePortCctDescr_Type(SnmpAdminString):
    """Custom type rbnBridgePortCctDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnBridgePortCctDescr_Type.__name__ = "SnmpAdminString"
_RbnBridgePortCctDescr_Object = MibTableColumn
rbnBridgePortCctDescr = _RbnBridgePortCctDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2, 1, 1),
    _RbnBridgePortCctDescr_Type()
)
rbnBridgePortCctDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnBridgePortCctDescr.setStatus("current")
_RbnBridgeConformance_ObjectIdentity = ObjectIdentity
rbnBridgeConformance = _RbnBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2)
)
_RbnBridgeCompliances_ObjectIdentity = ObjectIdentity
rbnBridgeCompliances = _RbnBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1)
)
_RbnBridgeGroups_ObjectIdentity = ObjectIdentity
rbnBridgeGroups = _RbnBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("RBN-BRIDGE-MIB",
     "rbnBridgePortCctDescrEntry")
)
rbnBridgePortCctDescrEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

rbnBridgeNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 1)
)
rbnBridgeNotifyObjectGroup.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeNotifyEnable"),
        ("RBN-BRIDGE-MIB", "rbnBridgeGroupName"),
        ("RBN-BRIDGE-MIB", "rbnBridgeCircuitDescriptor"),
        ("RBN-BRIDGE-MIB", "rbnBridgeCircuitStatus"),
        ("RBN-BRIDGE-MIB", "rbnBridgeGroupContextName"))
)
if mibBuilder.loadTexts:
    rbnBridgeNotifyObjectGroup.setStatus("current")

rbnBridgeStateNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 2)
)
rbnBridgeStateNotifyObjectGroup.setObjects(
    ("RBN-BRIDGE-MIB", "rbnBridgePortPreviousState")
)
if mibBuilder.loadTexts:
    rbnBridgeStateNotifyObjectGroup.setStatus("current")

rbnBridgeBaseObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 5)
)
rbnBridgeBaseObjectGroup.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeId"),
        ("RBN-BRIDGE-MIB", "rbnBridgePortCctDescr"))
)
if mibBuilder.loadTexts:
    rbnBridgeBaseObjectGroup.setStatus("current")


# Notification objects

rbnBridgeCctStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 1)
)
rbnBridgeCctStateEvent.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeGroupName"),
        ("RBN-BRIDGE-MIB", "rbnBridgeCircuitDescriptor"),
        ("RBN-BRIDGE-MIB", "rbnBridgeCircuitStatus"),
        ("RBN-BRIDGE-MIB", "rbnBridgeGroupContextName"))
)
if mibBuilder.loadTexts:
    rbnBridgeCctStateEvent.setStatus(
        "current"
    )

rbnBridgeNewRootEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 2)
)
rbnBridgeNewRootEvent.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeId"),
        ("BRIDGE-MIB", "dot1dStpPortState"))
)
if mibBuilder.loadTexts:
    rbnBridgeNewRootEvent.setStatus(
        "current"
    )

rbnBridgeTopologyChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 3)
)
rbnBridgeTopologyChangeEvent.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeId"),
        ("BRIDGE-MIB", "dot1dStpPortState"),
        ("RBN-BRIDGE-MIB", "rbnBridgePortPreviousState"))
)
if mibBuilder.loadTexts:
    rbnBridgeTopologyChangeEvent.setStatus(
        "current"
    )


# Notifications groups

rbnBridgeNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 3)
)
rbnBridgeNotifyGroup.setObjects(
    ("RBN-BRIDGE-MIB", "rbnBridgeCctStateEvent")
)
if mibBuilder.loadTexts:
    rbnBridgeNotifyGroup.setStatus(
        "current"
    )

rbnBridgeStateNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 4)
)
rbnBridgeStateNotifyGroup.setObjects(
      *(("RBN-BRIDGE-MIB", "rbnBridgeNewRootEvent"),
        ("RBN-BRIDGE-MIB", "rbnBridgeTopologyChangeEvent"))
)
if mibBuilder.loadTexts:
    rbnBridgeStateNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnBridgeCompliance.setStatus(
        "deprecated"
    )

rbnBridgeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnBridgeCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-BRIDGE-MIB",
    **{"rbnBridgeMib": rbnBridgeMib,
       "rbnBridgeNotifications": rbnBridgeNotifications,
       "rbnBridgeCctStateEvent": rbnBridgeCctStateEvent,
       "rbnBridgeNewRootEvent": rbnBridgeNewRootEvent,
       "rbnBridgeTopologyChangeEvent": rbnBridgeTopologyChangeEvent,
       "rbnBridgeObjects": rbnBridgeObjects,
       "rbnBridgeNotify": rbnBridgeNotify,
       "rbnBridgeNotifyEnable": rbnBridgeNotifyEnable,
       "rbnBridgeGroupName": rbnBridgeGroupName,
       "rbnBridgeCircuitDescriptor": rbnBridgeCircuitDescriptor,
       "rbnBridgeCircuitStatus": rbnBridgeCircuitStatus,
       "rbnBridgeGroupContextName": rbnBridgeGroupContextName,
       "rbnBridgePortPreviousState": rbnBridgePortPreviousState,
       "rbnBridgeBase": rbnBridgeBase,
       "rbnBridgeIdTable": rbnBridgeIdTable,
       "rbnBridgeIdEntry": rbnBridgeIdEntry,
       "rbnBridgeName": rbnBridgeName,
       "rbnBridgeId": rbnBridgeId,
       "rbnBridgePortCctDescrTable": rbnBridgePortCctDescrTable,
       "rbnBridgePortCctDescrEntry": rbnBridgePortCctDescrEntry,
       "rbnBridgePortCctDescr": rbnBridgePortCctDescr,
       "rbnBridgeConformance": rbnBridgeConformance,
       "rbnBridgeCompliances": rbnBridgeCompliances,
       "rbnBridgeCompliance": rbnBridgeCompliance,
       "rbnBridgeCompliance2": rbnBridgeCompliance2,
       "rbnBridgeGroups": rbnBridgeGroups,
       "rbnBridgeNotifyObjectGroup": rbnBridgeNotifyObjectGroup,
       "rbnBridgeStateNotifyObjectGroup": rbnBridgeStateNotifyObjectGroup,
       "rbnBridgeNotifyGroup": rbnBridgeNotifyGroup,
       "rbnBridgeStateNotifyGroup": rbnBridgeStateNotifyGroup,
       "rbnBridgeBaseObjectGroup": rbnBridgeBaseObjectGroup}
)
