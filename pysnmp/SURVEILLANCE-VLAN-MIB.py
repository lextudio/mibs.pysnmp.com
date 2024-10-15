# SNMP MIB module (SURVEILLANCE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SURVEILLANCE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:42 2024
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

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

swSurveillanceVLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSurveillanceVLANNotifications_ObjectIdentity = ObjectIdentity
swSurveillanceVLANNotifications = _SwSurveillanceVLANNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 0)
)
_SwSurveillanceVLANMIBObjects_ObjectIdentity = ObjectIdentity
swSurveillanceVLANMIBObjects = _SwSurveillanceVLANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1)
)
_SwSurveillanceVlanCtrl_ObjectIdentity = ObjectIdentity
swSurveillanceVlanCtrl = _SwSurveillanceVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1)
)
_SwSurveillanceVlanId_Type = VlanIdOrNone
_SwSurveillanceVlanId_Object = MibScalar
swSurveillanceVlanId = _SwSurveillanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1, 1),
    _SwSurveillanceVlanId_Type()
)
swSurveillanceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanId.setStatus("current")


class _SwSurveillanceVlanGlobalState_Type(Integer32):
    """Custom type swSurveillanceVlanGlobalState based on Integer32"""
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


_SwSurveillanceVlanGlobalState_Type.__name__ = "Integer32"
_SwSurveillanceVlanGlobalState_Object = MibScalar
swSurveillanceVlanGlobalState = _SwSurveillanceVlanGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1, 2),
    _SwSurveillanceVlanGlobalState_Type()
)
swSurveillanceVlanGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanGlobalState.setStatus("current")


class _SwSurveillanceVlanPriority_Type(Integer32):
    """Custom type swSurveillanceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwSurveillanceVlanPriority_Type.__name__ = "Integer32"
_SwSurveillanceVlanPriority_Object = MibScalar
swSurveillanceVlanPriority = _SwSurveillanceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1, 3),
    _SwSurveillanceVlanPriority_Type()
)
swSurveillanceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanPriority.setStatus("current")


class _SwSurveillanceVlanAgingTime_Type(Integer32):
    """Custom type swSurveillanceVlanAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwSurveillanceVlanAgingTime_Type.__name__ = "Integer32"
_SwSurveillanceVlanAgingTime_Object = MibScalar
swSurveillanceVlanAgingTime = _SwSurveillanceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1, 4),
    _SwSurveillanceVlanAgingTime_Type()
)
swSurveillanceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanAgingTime.setStatus("current")


class _SwSurveillanceVlanLogState_Type(Integer32):
    """Custom type swSurveillanceVlanLogState based on Integer32"""
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


_SwSurveillanceVlanLogState_Type.__name__ = "Integer32"
_SwSurveillanceVlanLogState_Object = MibScalar
swSurveillanceVlanLogState = _SwSurveillanceVlanLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 1, 5),
    _SwSurveillanceVlanLogState_Type()
)
swSurveillanceVlanLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanLogState.setStatus("current")
_SwSurveillanceVlanInfo_ObjectIdentity = ObjectIdentity
swSurveillanceVlanInfo = _SwSurveillanceVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2)
)
_SwSurveillanceVlanMemberPortlist_Type = PortList
_SwSurveillanceVlanMemberPortlist_Object = MibScalar
swSurveillanceVlanMemberPortlist = _SwSurveillanceVlanMemberPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 1),
    _SwSurveillanceVlanMemberPortlist_Type()
)
swSurveillanceVlanMemberPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanMemberPortlist.setStatus("current")
_SwSurveillanceVlanDynamicPortlist_Type = PortList
_SwSurveillanceVlanDynamicPortlist_Object = MibScalar
swSurveillanceVlanDynamicPortlist = _SwSurveillanceVlanDynamicPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 2),
    _SwSurveillanceVlanDynamicPortlist_Type()
)
swSurveillanceVlanDynamicPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanDynamicPortlist.setStatus("current")
_SwSurveillanceVlanDeviceTable_Object = MibTable
swSurveillanceVlanDeviceTable = _SwSurveillanceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3)
)
if mibBuilder.loadTexts:
    swSurveillanceVlanDeviceTable.setStatus("current")
_SwSurveillanceVlanDeviceEntry_Object = MibTableRow
swSurveillanceVlanDeviceEntry = _SwSurveillanceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3, 1)
)
swSurveillanceVlanDeviceEntry.setIndexNames(
    (0, "SURVEILLANCE-VLAN-MIB", "swSurveillanceVlanDevPort"),
    (0, "SURVEILLANCE-VLAN-MIB", "swSurveillanceVlanDevAddr"),
)
if mibBuilder.loadTexts:
    swSurveillanceVlanDeviceEntry.setStatus("current")
_SwSurveillanceVlanDevPort_Type = Integer32
_SwSurveillanceVlanDevPort_Object = MibTableColumn
swSurveillanceVlanDevPort = _SwSurveillanceVlanDevPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3, 1, 1),
    _SwSurveillanceVlanDevPort_Type()
)
swSurveillanceVlanDevPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanDevPort.setStatus("current")
_SwSurveillanceVlanDevAddr_Type = MacAddress
_SwSurveillanceVlanDevAddr_Object = MibTableColumn
swSurveillanceVlanDevAddr = _SwSurveillanceVlanDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3, 1, 2),
    _SwSurveillanceVlanDevAddr_Type()
)
swSurveillanceVlanDevAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanDevAddr.setStatus("current")


class _SwSurveillanceVlanDevComponentType_Type(Integer32):
    """Custom type swSurveillanceVlanDevComponentType based on Integer32"""
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
        *(("network-storage", 4),
          ("other", 5),
          ("video-encoder", 3),
          ("vms", 1),
          ("vms-client", 2))
    )


_SwSurveillanceVlanDevComponentType_Type.__name__ = "Integer32"
_SwSurveillanceVlanDevComponentType_Object = MibTableColumn
swSurveillanceVlanDevComponentType = _SwSurveillanceVlanDevComponentType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3, 1, 3),
    _SwSurveillanceVlanDevComponentType_Type()
)
swSurveillanceVlanDevComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSurveillanceVlanDevComponentType.setStatus("current")
_SwSurveillanceVlanDevStartTime_Type = DateAndTime
_SwSurveillanceVlanDevStartTime_Object = MibTableColumn
swSurveillanceVlanDevStartTime = _SwSurveillanceVlanDevStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 2, 3, 1, 4),
    _SwSurveillanceVlanDevStartTime_Type()
)
swSurveillanceVlanDevStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanDevStartTime.setStatus("current")
_SwSurveillanceVlanMgmt_ObjectIdentity = ObjectIdentity
swSurveillanceVlanMgmt = _SwSurveillanceVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3)
)
_SwSurveillanceVlanOuiTable_Object = MibTable
swSurveillanceVlanOuiTable = _SwSurveillanceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiTable.setStatus("current")
_SwSurveillanceVlanOuiEntry_Object = MibTableRow
swSurveillanceVlanOuiEntry = _SwSurveillanceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1)
)
swSurveillanceVlanOuiEntry.setIndexNames(
    (0, "SURVEILLANCE-VLAN-MIB", "swSurveillanceVlanOuiAddr"),
)
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiEntry.setStatus("current")
_SwSurveillanceVlanOuiAddr_Type = MacAddress
_SwSurveillanceVlanOuiAddr_Object = MibTableColumn
swSurveillanceVlanOuiAddr = _SwSurveillanceVlanOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1, 1),
    _SwSurveillanceVlanOuiAddr_Type()
)
swSurveillanceVlanOuiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiAddr.setStatus("current")
_SwSurveillanceVlanOuiMask_Type = MacAddress
_SwSurveillanceVlanOuiMask_Object = MibTableColumn
swSurveillanceVlanOuiMask = _SwSurveillanceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1, 2),
    _SwSurveillanceVlanOuiMask_Type()
)
swSurveillanceVlanOuiMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiMask.setStatus("current")


class _SwSurveillanceVlanOuiComponentType_Type(Integer32):
    """Custom type swSurveillanceVlanOuiComponentType based on Integer32"""
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
        *(("network-storage", 4),
          ("other", 5),
          ("video-encoder", 3),
          ("vms", 1),
          ("vms-client", 2))
    )


_SwSurveillanceVlanOuiComponentType_Type.__name__ = "Integer32"
_SwSurveillanceVlanOuiComponentType_Object = MibTableColumn
swSurveillanceVlanOuiComponentType = _SwSurveillanceVlanOuiComponentType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1, 3),
    _SwSurveillanceVlanOuiComponentType_Type()
)
swSurveillanceVlanOuiComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiComponentType.setStatus("current")
_SwSurveillanceVlanOuiDes_Type = DisplayString
_SwSurveillanceVlanOuiDes_Object = MibTableColumn
swSurveillanceVlanOuiDes = _SwSurveillanceVlanOuiDes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1, 4),
    _SwSurveillanceVlanOuiDes_Type()
)
swSurveillanceVlanOuiDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiDes.setStatus("current")
_SwSurveillanceVlanOuiRowStatus_Type = RowStatus
_SwSurveillanceVlanOuiRowStatus_Object = MibTableColumn
swSurveillanceVlanOuiRowStatus = _SwSurveillanceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 1, 1, 5),
    _SwSurveillanceVlanOuiRowStatus_Type()
)
swSurveillanceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSurveillanceVlanOuiRowStatus.setStatus("current")
_SwSurveillanceVlanPortTable_Object = MibTable
swSurveillanceVlanPortTable = _SwSurveillanceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 2)
)
if mibBuilder.loadTexts:
    swSurveillanceVlanPortTable.setStatus("current")
_SwSurveillanceVlanPortEntry_Object = MibTableRow
swSurveillanceVlanPortEntry = _SwSurveillanceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 2, 1)
)
swSurveillanceVlanPortEntry.setIndexNames(
    (0, "SURVEILLANCE-VLAN-MIB", "swSurveillanceVlanPortNumber"),
)
if mibBuilder.loadTexts:
    swSurveillanceVlanPortEntry.setStatus("current")
_SwSurveillanceVlanPortNumber_Type = Integer32
_SwSurveillanceVlanPortNumber_Object = MibTableColumn
swSurveillanceVlanPortNumber = _SwSurveillanceVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 2, 1, 1),
    _SwSurveillanceVlanPortNumber_Type()
)
swSurveillanceVlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSurveillanceVlanPortNumber.setStatus("current")


class _SwSurveillanceVlanPortState_Type(Integer32):
    """Custom type swSurveillanceVlanPortState based on Integer32"""
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


_SwSurveillanceVlanPortState_Type.__name__ = "Integer32"
_SwSurveillanceVlanPortState_Object = MibTableColumn
swSurveillanceVlanPortState = _SwSurveillanceVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 102, 1, 3, 2, 1, 2),
    _SwSurveillanceVlanPortState_Type()
)
swSurveillanceVlanPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSurveillanceVlanPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SURVEILLANCE-VLAN-MIB",
    **{"swSurveillanceVLANMIB": swSurveillanceVLANMIB,
       "swSurveillanceVLANNotifications": swSurveillanceVLANNotifications,
       "swSurveillanceVLANMIBObjects": swSurveillanceVLANMIBObjects,
       "swSurveillanceVlanCtrl": swSurveillanceVlanCtrl,
       "swSurveillanceVlanId": swSurveillanceVlanId,
       "swSurveillanceVlanGlobalState": swSurveillanceVlanGlobalState,
       "swSurveillanceVlanPriority": swSurveillanceVlanPriority,
       "swSurveillanceVlanAgingTime": swSurveillanceVlanAgingTime,
       "swSurveillanceVlanLogState": swSurveillanceVlanLogState,
       "swSurveillanceVlanInfo": swSurveillanceVlanInfo,
       "swSurveillanceVlanMemberPortlist": swSurveillanceVlanMemberPortlist,
       "swSurveillanceVlanDynamicPortlist": swSurveillanceVlanDynamicPortlist,
       "swSurveillanceVlanDeviceTable": swSurveillanceVlanDeviceTable,
       "swSurveillanceVlanDeviceEntry": swSurveillanceVlanDeviceEntry,
       "swSurveillanceVlanDevPort": swSurveillanceVlanDevPort,
       "swSurveillanceVlanDevAddr": swSurveillanceVlanDevAddr,
       "swSurveillanceVlanDevComponentType": swSurveillanceVlanDevComponentType,
       "swSurveillanceVlanDevStartTime": swSurveillanceVlanDevStartTime,
       "swSurveillanceVlanMgmt": swSurveillanceVlanMgmt,
       "swSurveillanceVlanOuiTable": swSurveillanceVlanOuiTable,
       "swSurveillanceVlanOuiEntry": swSurveillanceVlanOuiEntry,
       "swSurveillanceVlanOuiAddr": swSurveillanceVlanOuiAddr,
       "swSurveillanceVlanOuiMask": swSurveillanceVlanOuiMask,
       "swSurveillanceVlanOuiComponentType": swSurveillanceVlanOuiComponentType,
       "swSurveillanceVlanOuiDes": swSurveillanceVlanOuiDes,
       "swSurveillanceVlanOuiRowStatus": swSurveillanceVlanOuiRowStatus,
       "swSurveillanceVlanPortTable": swSurveillanceVlanPortTable,
       "swSurveillanceVlanPortEntry": swSurveillanceVlanPortEntry,
       "swSurveillanceVlanPortNumber": swSurveillanceVlanPortNumber,
       "swSurveillanceVlanPortState": swSurveillanceVlanPortState}
)
