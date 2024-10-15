# SNMP MIB module (VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VOICE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:04 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swVoiceVLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwVoiceVlanCtrl_ObjectIdentity = ObjectIdentity
swVoiceVlanCtrl = _SwVoiceVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1)
)
_SwVoiceVlanId_Type = VlanIdOrNone
_SwVoiceVlanId_Object = MibScalar
swVoiceVlanId = _SwVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 1),
    _SwVoiceVlanId_Type()
)
swVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanId.setStatus("current")


class _SwVoivceVlanGlobalState_Type(Integer32):
    """Custom type swVoivceVlanGlobalState based on Integer32"""
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


_SwVoivceVlanGlobalState_Type.__name__ = "Integer32"
_SwVoivceVlanGlobalState_Object = MibScalar
swVoivceVlanGlobalState = _SwVoivceVlanGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 2),
    _SwVoivceVlanGlobalState_Type()
)
swVoivceVlanGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoivceVlanGlobalState.setStatus("current")


class _SwVoiceVlanPriority_Type(Integer32):
    """Custom type swVoiceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwVoiceVlanPriority_Type.__name__ = "Integer32"
_SwVoiceVlanPriority_Object = MibScalar
swVoiceVlanPriority = _SwVoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 3),
    _SwVoiceVlanPriority_Type()
)
swVoiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanPriority.setStatus("current")


class _SwVoiceVlanAgingTime_Type(Integer32):
    """Custom type swVoiceVlanAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwVoiceVlanAgingTime_Type.__name__ = "Integer32"
_SwVoiceVlanAgingTime_Object = MibScalar
swVoiceVlanAgingTime = _SwVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 4),
    _SwVoiceVlanAgingTime_Type()
)
swVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanAgingTime.setStatus("current")


class _SwVoiceVlanLogState_Type(Integer32):
    """Custom type swVoiceVlanLogState based on Integer32"""
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


_SwVoiceVlanLogState_Type.__name__ = "Integer32"
_SwVoiceVlanLogState_Object = MibScalar
swVoiceVlanLogState = _SwVoiceVlanLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 1, 5),
    _SwVoiceVlanLogState_Type()
)
swVoiceVlanLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanLogState.setStatus("current")
_SwVoiceVlanInfo_ObjectIdentity = ObjectIdentity
swVoiceVlanInfo = _SwVoiceVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2)
)
_SwVoiceVlanMemberPortlist_Type = PortList
_SwVoiceVlanMemberPortlist_Object = MibScalar
swVoiceVlanMemberPortlist = _SwVoiceVlanMemberPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 1),
    _SwVoiceVlanMemberPortlist_Type()
)
swVoiceVlanMemberPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanMemberPortlist.setStatus("current")
_SwVoiceVlanDynamicPortlist_Type = PortList
_SwVoiceVlanDynamicPortlist_Object = MibScalar
swVoiceVlanDynamicPortlist = _SwVoiceVlanDynamicPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 2),
    _SwVoiceVlanDynamicPortlist_Type()
)
swVoiceVlanDynamicPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanDynamicPortlist.setStatus("current")
_SwVoiceVlanDeviceTable_Object = MibTable
swVoiceVlanDeviceTable = _SwVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3)
)
if mibBuilder.loadTexts:
    swVoiceVlanDeviceTable.setStatus("current")
_SwVoiceVlanDeviceEntry_Object = MibTableRow
swVoiceVlanDeviceEntry = _SwVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1)
)
swVoiceVlanDeviceEntry.setIndexNames(
    (0, "VOICE-VLAN-MIB", "swVoiceVlanPort"),
    (0, "VOICE-VLAN-MIB", "swVoiceVlanDeviceAddr"),
)
if mibBuilder.loadTexts:
    swVoiceVlanDeviceEntry.setStatus("current")
_SwVoiceVlanPort_Type = Integer32
_SwVoiceVlanPort_Object = MibTableColumn
swVoiceVlanPort = _SwVoiceVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 1),
    _SwVoiceVlanPort_Type()
)
swVoiceVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanPort.setStatus("current")
_SwVoiceVlanDeviceAddr_Type = MacAddress
_SwVoiceVlanDeviceAddr_Object = MibTableColumn
swVoiceVlanDeviceAddr = _SwVoiceVlanDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 2),
    _SwVoiceVlanDeviceAddr_Type()
)
swVoiceVlanDeviceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanDeviceAddr.setStatus("current")
_SwVoiceVlanDeviceStartTime_Type = DateAndTime
_SwVoiceVlanDeviceStartTime_Object = MibTableColumn
swVoiceVlanDeviceStartTime = _SwVoiceVlanDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 3),
    _SwVoiceVlanDeviceStartTime_Type()
)
swVoiceVlanDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanDeviceStartTime.setStatus("current")
_SwVoiceVlanDeviceActiveTime_Type = DateAndTime
_SwVoiceVlanDeviceActiveTime_Object = MibTableColumn
swVoiceVlanDeviceActiveTime = _SwVoiceVlanDeviceActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 2, 3, 1, 4),
    _SwVoiceVlanDeviceActiveTime_Type()
)
swVoiceVlanDeviceActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanDeviceActiveTime.setStatus("current")
_SwVoiceVlanMgmt_ObjectIdentity = ObjectIdentity
swVoiceVlanMgmt = _SwVoiceVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3)
)
_SwVoiceVlanOuiTable_Object = MibTable
swVoiceVlanOuiTable = _SwVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1)
)
if mibBuilder.loadTexts:
    swVoiceVlanOuiTable.setStatus("current")
_SwVoiceVlanOuiEntry_Object = MibTableRow
swVoiceVlanOuiEntry = _SwVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1)
)
swVoiceVlanOuiEntry.setIndexNames(
    (0, "VOICE-VLAN-MIB", "swVoiceVlanOuiAddr"),
)
if mibBuilder.loadTexts:
    swVoiceVlanOuiEntry.setStatus("current")
_SwVoiceVlanOuiAddr_Type = MacAddress
_SwVoiceVlanOuiAddr_Object = MibTableColumn
swVoiceVlanOuiAddr = _SwVoiceVlanOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 1),
    _SwVoiceVlanOuiAddr_Type()
)
swVoiceVlanOuiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanOuiAddr.setStatus("current")
_SwVoiceVlanOuiMask_Type = MacAddress
_SwVoiceVlanOuiMask_Object = MibTableColumn
swVoiceVlanOuiMask = _SwVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 2),
    _SwVoiceVlanOuiMask_Type()
)
swVoiceVlanOuiMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVoiceVlanOuiMask.setStatus("current")
_SwVoiceVlanOuiDes_Type = DisplayString
_SwVoiceVlanOuiDes_Object = MibTableColumn
swVoiceVlanOuiDes = _SwVoiceVlanOuiDes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 3),
    _SwVoiceVlanOuiDes_Type()
)
swVoiceVlanOuiDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVoiceVlanOuiDes.setStatus("current")
_SwVoiceVlanOuiRowStatus_Type = RowStatus
_SwVoiceVlanOuiRowStatus_Object = MibTableColumn
swVoiceVlanOuiRowStatus = _SwVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 1, 1, 4),
    _SwVoiceVlanOuiRowStatus_Type()
)
swVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVoiceVlanOuiRowStatus.setStatus("current")
_SwVoiceVlanPortTable_Object = MibTable
swVoiceVlanPortTable = _SwVoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2)
)
if mibBuilder.loadTexts:
    swVoiceVlanPortTable.setStatus("current")
_SwVoiceVlanPortEntry_Object = MibTableRow
swVoiceVlanPortEntry = _SwVoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1)
)
swVoiceVlanPortEntry.setIndexNames(
    (0, "VOICE-VLAN-MIB", "swVoiceVlanPortNumber"),
)
if mibBuilder.loadTexts:
    swVoiceVlanPortEntry.setStatus("current")
_SwVoiceVlanPortNumber_Type = Integer32
_SwVoiceVlanPortNumber_Object = MibTableColumn
swVoiceVlanPortNumber = _SwVoiceVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 1),
    _SwVoiceVlanPortNumber_Type()
)
swVoiceVlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVoiceVlanPortNumber.setStatus("current")


class _SwVoiceVlanPortState_Type(Integer32):
    """Custom type swVoiceVlanPortState based on Integer32"""
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


_SwVoiceVlanPortState_Type.__name__ = "Integer32"
_SwVoiceVlanPortState_Object = MibTableColumn
swVoiceVlanPortState = _SwVoiceVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 2),
    _SwVoiceVlanPortState_Type()
)
swVoiceVlanPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanPortState.setStatus("current")


class _SwVoiceVlanPortMode_Type(Integer32):
    """Custom type swVoiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_SwVoiceVlanPortMode_Type.__name__ = "Integer32"
_SwVoiceVlanPortMode_Object = MibTableColumn
swVoiceVlanPortMode = _SwVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 74, 3, 2, 1, 3),
    _SwVoiceVlanPortMode_Type()
)
swVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVoiceVlanPortMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VOICE-VLAN-MIB",
    **{"swVoiceVLANMIB": swVoiceVLANMIB,
       "swVoiceVlanCtrl": swVoiceVlanCtrl,
       "swVoiceVlanId": swVoiceVlanId,
       "swVoivceVlanGlobalState": swVoivceVlanGlobalState,
       "swVoiceVlanPriority": swVoiceVlanPriority,
       "swVoiceVlanAgingTime": swVoiceVlanAgingTime,
       "swVoiceVlanLogState": swVoiceVlanLogState,
       "swVoiceVlanInfo": swVoiceVlanInfo,
       "swVoiceVlanMemberPortlist": swVoiceVlanMemberPortlist,
       "swVoiceVlanDynamicPortlist": swVoiceVlanDynamicPortlist,
       "swVoiceVlanDeviceTable": swVoiceVlanDeviceTable,
       "swVoiceVlanDeviceEntry": swVoiceVlanDeviceEntry,
       "swVoiceVlanPort": swVoiceVlanPort,
       "swVoiceVlanDeviceAddr": swVoiceVlanDeviceAddr,
       "swVoiceVlanDeviceStartTime": swVoiceVlanDeviceStartTime,
       "swVoiceVlanDeviceActiveTime": swVoiceVlanDeviceActiveTime,
       "swVoiceVlanMgmt": swVoiceVlanMgmt,
       "swVoiceVlanOuiTable": swVoiceVlanOuiTable,
       "swVoiceVlanOuiEntry": swVoiceVlanOuiEntry,
       "swVoiceVlanOuiAddr": swVoiceVlanOuiAddr,
       "swVoiceVlanOuiMask": swVoiceVlanOuiMask,
       "swVoiceVlanOuiDes": swVoiceVlanOuiDes,
       "swVoiceVlanOuiRowStatus": swVoiceVlanOuiRowStatus,
       "swVoiceVlanPortTable": swVoiceVlanPortTable,
       "swVoiceVlanPortEntry": swVoiceVlanPortEntry,
       "swVoiceVlanPortNumber": swVoiceVlanPortNumber,
       "swVoiceVlanPortState": swVoiceVlanPortState,
       "swVoiceVlanPortMode": swVoiceVlanPortMode}
)
