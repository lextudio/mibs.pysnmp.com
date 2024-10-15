# SNMP MIB module (MCAST-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MCAST-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:41 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swMcastVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 64)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwMcastVlanCtrl_ObjectIdentity = ObjectIdentity
swMcastVlanCtrl = _SwMcastVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 1)
)


class _SwISMVlanGlobalState_Type(Integer32):
    """Custom type swISMVlanGlobalState based on Integer32"""
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


_SwISMVlanGlobalState_Type.__name__ = "Integer32"
_SwISMVlanGlobalState_Object = MibScalar
swISMVlanGlobalState = _SwISMVlanGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 1),
    _SwISMVlanGlobalState_Type()
)
swISMVlanGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanGlobalState.setStatus("current")


class _SwMSMVlanGlobalState_Type(Integer32):
    """Custom type swMSMVlanGlobalState based on Integer32"""
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


_SwMSMVlanGlobalState_Type.__name__ = "Integer32"
_SwMSMVlanGlobalState_Object = MibScalar
swMSMVlanGlobalState = _SwMSMVlanGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 2),
    _SwMSMVlanGlobalState_Type()
)
swMSMVlanGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanGlobalState.setStatus("current")


class _SwISMVlanForwardUnmatchedState_Type(Integer32):
    """Custom type swISMVlanForwardUnmatchedState based on Integer32"""
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


_SwISMVlanForwardUnmatchedState_Type.__name__ = "Integer32"
_SwISMVlanForwardUnmatchedState_Object = MibScalar
swISMVlanForwardUnmatchedState = _SwISMVlanForwardUnmatchedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 3),
    _SwISMVlanForwardUnmatchedState_Type()
)
swISMVlanForwardUnmatchedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanForwardUnmatchedState.setStatus("current")


class _SwMSMVlanForwardUnmatchedState_Type(Integer32):
    """Custom type swMSMVlanForwardUnmatchedState based on Integer32"""
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


_SwMSMVlanForwardUnmatchedState_Type.__name__ = "Integer32"
_SwMSMVlanForwardUnmatchedState_Object = MibScalar
swMSMVlanForwardUnmatchedState = _SwMSMVlanForwardUnmatchedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 1, 4),
    _SwMSMVlanForwardUnmatchedState_Type()
)
swMSMVlanForwardUnmatchedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanForwardUnmatchedState.setStatus("current")
_SwMcastVlanInfo_ObjectIdentity = ObjectIdentity
swMcastVlanInfo = _SwMcastVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 2)
)
_SwMcastVlanMgmt_ObjectIdentity = ObjectIdentity
swMcastVlanMgmt = _SwMcastVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3)
)
_SwISMVlanTable_Object = MibTable
swISMVlanTable = _SwISMVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1)
)
if mibBuilder.loadTexts:
    swISMVlanTable.setStatus("current")
_SwISMVlanEntry_Object = MibTableRow
swISMVlanEntry = _SwISMVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1)
)
swISMVlanEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swISMVlanID"),
)
if mibBuilder.loadTexts:
    swISMVlanEntry.setStatus("current")


class _SwISMVlanID_Type(Integer32):
    """Custom type swISMVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SwISMVlanID_Type.__name__ = "Integer32"
_SwISMVlanID_Object = MibTableColumn
swISMVlanID = _SwISMVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 1),
    _SwISMVlanID_Type()
)
swISMVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanID.setStatus("current")


class _SwISMVlanName_Type(DisplayString):
    """Custom type swISMVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwISMVlanName_Type.__name__ = "DisplayString"
_SwISMVlanName_Object = MibTableColumn
swISMVlanName = _SwISMVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 2),
    _SwISMVlanName_Type()
)
swISMVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanName.setStatus("current")
_SwISMVlanSourcePort_Type = PortList
_SwISMVlanSourcePort_Object = MibTableColumn
swISMVlanSourcePort = _SwISMVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 3),
    _SwISMVlanSourcePort_Type()
)
swISMVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanSourcePort.setStatus("current")
_SwISMVlanMemberPort_Type = PortList
_SwISMVlanMemberPort_Object = MibTableColumn
swISMVlanMemberPort = _SwISMVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 4),
    _SwISMVlanMemberPort_Type()
)
swISMVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanMemberPort.setStatus("current")
_SwISMVlanTagMemberPort_Type = PortList
_SwISMVlanTagMemberPort_Object = MibTableColumn
swISMVlanTagMemberPort = _SwISMVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 5),
    _SwISMVlanTagMemberPort_Type()
)
swISMVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanTagMemberPort.setStatus("current")
_SwISMVlanUntagSourcePort_Type = PortList
_SwISMVlanUntagSourcePort_Object = MibTableColumn
swISMVlanUntagSourcePort = _SwISMVlanUntagSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 6),
    _SwISMVlanUntagSourcePort_Type()
)
swISMVlanUntagSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanUntagSourcePort.setStatus("current")


class _SwISMVlanState_Type(Integer32):
    """Custom type swISMVlanState based on Integer32"""
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


_SwISMVlanState_Type.__name__ = "Integer32"
_SwISMVlanState_Object = MibTableColumn
swISMVlanState = _SwISMVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 7),
    _SwISMVlanState_Type()
)
swISMVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanState.setStatus("current")
_SwISMVlanRepSourceAddrType_Type = InetAddressType
_SwISMVlanRepSourceAddrType_Object = MibTableColumn
swISMVlanRepSourceAddrType = _SwISMVlanRepSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 8),
    _SwISMVlanRepSourceAddrType_Type()
)
swISMVlanRepSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanRepSourceAddrType.setStatus("current")
_SwISMVlanRepSourceAddr_Type = InetAddress
_SwISMVlanRepSourceAddr_Object = MibTableColumn
swISMVlanRepSourceAddr = _SwISMVlanRepSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 9),
    _SwISMVlanRepSourceAddr_Type()
)
swISMVlanRepSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanRepSourceAddr.setStatus("current")


class _SwISMVlanRemapPriority_Type(Integer32):
    """Custom type swISMVlanRemapPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwISMVlanRemapPriority_Type.__name__ = "Integer32"
_SwISMVlanRemapPriority_Object = MibTableColumn
swISMVlanRemapPriority = _SwISMVlanRemapPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 10),
    _SwISMVlanRemapPriority_Type()
)
swISMVlanRemapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanRemapPriority.setStatus("current")


class _SwISMVlanReplacePriority_Type(Integer32):
    """Custom type swISMVlanReplacePriority based on Integer32"""
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


_SwISMVlanReplacePriority_Type.__name__ = "Integer32"
_SwISMVlanReplacePriority_Object = MibTableColumn
swISMVlanReplacePriority = _SwISMVlanReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 11),
    _SwISMVlanReplacePriority_Type()
)
swISMVlanReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanReplacePriority.setStatus("current")
_SwISMVlanProfileIDList_Type = DisplayString
_SwISMVlanProfileIDList_Object = MibTableColumn
swISMVlanProfileIDList = _SwISMVlanProfileIDList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 12),
    _SwISMVlanProfileIDList_Type()
)
swISMVlanProfileIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swISMVlanProfileIDList.setStatus("current")
_SwISMVlanRowStatus_Type = RowStatus
_SwISMVlanRowStatus_Object = MibTableColumn
swISMVlanRowStatus = _SwISMVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 1, 1, 13),
    _SwISMVlanRowStatus_Type()
)
swISMVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanRowStatus.setStatus("current")
_SwISMVlanGroupProfTable_Object = MibTable
swISMVlanGroupProfTable = _SwISMVlanGroupProfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2)
)
if mibBuilder.loadTexts:
    swISMVlanGroupProfTable.setStatus("current")
_SwISMVlanGroupProfEntry_Object = MibTableRow
swISMVlanGroupProfEntry = _SwISMVlanGroupProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1)
)
swISMVlanGroupProfEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfName"),
)
if mibBuilder.loadTexts:
    swISMVlanGroupProfEntry.setStatus("current")
_SwISMVlanGroupProfName_Type = DisplayString
_SwISMVlanGroupProfName_Object = MibTableColumn
swISMVlanGroupProfName = _SwISMVlanGroupProfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 1),
    _SwISMVlanGroupProfName_Type()
)
swISMVlanGroupProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanGroupProfName.setStatus("current")
_SwISMVlanGroupProfID_Type = Integer32
_SwISMVlanGroupProfID_Object = MibTableColumn
swISMVlanGroupProfID = _SwISMVlanGroupProfID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 2),
    _SwISMVlanGroupProfID_Type()
)
swISMVlanGroupProfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanGroupProfID.setStatus("current")
_SwISMVlanGroupProfStatus_Type = RowStatus
_SwISMVlanGroupProfStatus_Object = MibTableColumn
swISMVlanGroupProfStatus = _SwISMVlanGroupProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 2, 1, 3),
    _SwISMVlanGroupProfStatus_Type()
)
swISMVlanGroupProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanGroupProfStatus.setStatus("current")
_SwISMVlanGroupProfAddrTable_Object = MibTable
swISMVlanGroupProfAddrTable = _SwISMVlanGroupProfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3)
)
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrTable.setStatus("current")
_SwISMVlanGroupProfAddrEntry_Object = MibTableRow
swISMVlanGroupProfAddrEntry = _SwISMVlanGroupProfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1)
)
swISMVlanGroupProfAddrEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfName"),
    (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrType"),
    (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrStart"),
    (0, "MCAST-VLAN-MIB", "swISMVlanGroupProfAddrEnd"),
)
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrEntry.setStatus("current")
_SwISMVlanGroupProfAddrType_Type = InetAddressType
_SwISMVlanGroupProfAddrType_Object = MibTableColumn
swISMVlanGroupProfAddrType = _SwISMVlanGroupProfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 1),
    _SwISMVlanGroupProfAddrType_Type()
)
swISMVlanGroupProfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrType.setStatus("current")
_SwISMVlanGroupProfAddrStart_Type = InetAddress
_SwISMVlanGroupProfAddrStart_Object = MibTableColumn
swISMVlanGroupProfAddrStart = _SwISMVlanGroupProfAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 2),
    _SwISMVlanGroupProfAddrStart_Type()
)
swISMVlanGroupProfAddrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrStart.setStatus("current")
_SwISMVlanGroupProfAddrEnd_Type = InetAddress
_SwISMVlanGroupProfAddrEnd_Object = MibTableColumn
swISMVlanGroupProfAddrEnd = _SwISMVlanGroupProfAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 3),
    _SwISMVlanGroupProfAddrEnd_Type()
)
swISMVlanGroupProfAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrEnd.setStatus("current")
_SwISMVlanGroupProfAddrStatus_Type = RowStatus
_SwISMVlanGroupProfAddrStatus_Object = MibTableColumn
swISMVlanGroupProfAddrStatus = _SwISMVlanGroupProfAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 3, 1, 4),
    _SwISMVlanGroupProfAddrStatus_Type()
)
swISMVlanGroupProfAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swISMVlanGroupProfAddrStatus.setStatus("current")
_SwMSMVlanTable_Object = MibTable
swMSMVlanTable = _SwMSMVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4)
)
if mibBuilder.loadTexts:
    swMSMVlanTable.setStatus("current")
_SwMSMVlanEntry_Object = MibTableRow
swMSMVlanEntry = _SwMSMVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1)
)
swMSMVlanEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swMSMVlanID"),
)
if mibBuilder.loadTexts:
    swMSMVlanEntry.setStatus("current")


class _SwMSMVlanID_Type(Integer32):
    """Custom type swMSMVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SwMSMVlanID_Type.__name__ = "Integer32"
_SwMSMVlanID_Object = MibTableColumn
swMSMVlanID = _SwMSMVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 1),
    _SwMSMVlanID_Type()
)
swMSMVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanID.setStatus("current")


class _SwMSMVlanName_Type(DisplayString):
    """Custom type swMSMVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMSMVlanName_Type.__name__ = "DisplayString"
_SwMSMVlanName_Object = MibTableColumn
swMSMVlanName = _SwMSMVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 2),
    _SwMSMVlanName_Type()
)
swMSMVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanName.setStatus("current")
_SwMSMVlanSourcePort_Type = PortList
_SwMSMVlanSourcePort_Object = MibTableColumn
swMSMVlanSourcePort = _SwMSMVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 3),
    _SwMSMVlanSourcePort_Type()
)
swMSMVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanSourcePort.setStatus("current")
_SwMSMVlanMemberPort_Type = PortList
_SwMSMVlanMemberPort_Object = MibTableColumn
swMSMVlanMemberPort = _SwMSMVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 4),
    _SwMSMVlanMemberPort_Type()
)
swMSMVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanMemberPort.setStatus("current")
_SwMSMVlanTagMemberPort_Type = PortList
_SwMSMVlanTagMemberPort_Object = MibTableColumn
swMSMVlanTagMemberPort = _SwMSMVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 5),
    _SwMSMVlanTagMemberPort_Type()
)
swMSMVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanTagMemberPort.setStatus("current")
_SwMSMVlanUntagSourcePort_Type = PortList
_SwMSMVlanUntagSourcePort_Object = MibTableColumn
swMSMVlanUntagSourcePort = _SwMSMVlanUntagSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 6),
    _SwMSMVlanUntagSourcePort_Type()
)
swMSMVlanUntagSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanUntagSourcePort.setStatus("current")


class _SwMSMVlanState_Type(Integer32):
    """Custom type swMSMVlanState based on Integer32"""
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


_SwMSMVlanState_Type.__name__ = "Integer32"
_SwMSMVlanState_Object = MibTableColumn
swMSMVlanState = _SwMSMVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 7),
    _SwMSMVlanState_Type()
)
swMSMVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanState.setStatus("current")
_SwMSMVlanRepSourceAddrType_Type = InetAddressType
_SwMSMVlanRepSourceAddrType_Object = MibTableColumn
swMSMVlanRepSourceAddrType = _SwMSMVlanRepSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 8),
    _SwMSMVlanRepSourceAddrType_Type()
)
swMSMVlanRepSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanRepSourceAddrType.setStatus("current")
_SwMSMVlanRepSourceAddr_Type = InetAddress
_SwMSMVlanRepSourceAddr_Object = MibTableColumn
swMSMVlanRepSourceAddr = _SwMSMVlanRepSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 9),
    _SwMSMVlanRepSourceAddr_Type()
)
swMSMVlanRepSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanRepSourceAddr.setStatus("current")


class _SwMSMVlanRemapPriority_Type(Integer32):
    """Custom type swMSMVlanRemapPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwMSMVlanRemapPriority_Type.__name__ = "Integer32"
_SwMSMVlanRemapPriority_Object = MibTableColumn
swMSMVlanRemapPriority = _SwMSMVlanRemapPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 10),
    _SwMSMVlanRemapPriority_Type()
)
swMSMVlanRemapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanRemapPriority.setStatus("current")


class _SwMSMVlanReplacePriority_Type(Integer32):
    """Custom type swMSMVlanReplacePriority based on Integer32"""
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


_SwMSMVlanReplacePriority_Type.__name__ = "Integer32"
_SwMSMVlanReplacePriority_Object = MibTableColumn
swMSMVlanReplacePriority = _SwMSMVlanReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 11),
    _SwMSMVlanReplacePriority_Type()
)
swMSMVlanReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanReplacePriority.setStatus("current")
_SwMSMVlanProfileIDList_Type = DisplayString
_SwMSMVlanProfileIDList_Object = MibTableColumn
swMSMVlanProfileIDList = _SwMSMVlanProfileIDList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 12),
    _SwMSMVlanProfileIDList_Type()
)
swMSMVlanProfileIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSMVlanProfileIDList.setStatus("current")
_SwMSMVlanRowStatus_Type = RowStatus
_SwMSMVlanRowStatus_Object = MibTableColumn
swMSMVlanRowStatus = _SwMSMVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 4, 1, 13),
    _SwMSMVlanRowStatus_Type()
)
swMSMVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanRowStatus.setStatus("current")
_SwMSMVlanGroupProfTable_Object = MibTable
swMSMVlanGroupProfTable = _SwMSMVlanGroupProfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5)
)
if mibBuilder.loadTexts:
    swMSMVlanGroupProfTable.setStatus("current")
_SwMSMVlanGroupProfEntry_Object = MibTableRow
swMSMVlanGroupProfEntry = _SwMSMVlanGroupProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1)
)
swMSMVlanGroupProfEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfName"),
)
if mibBuilder.loadTexts:
    swMSMVlanGroupProfEntry.setStatus("current")
_SwMSMVlanGroupProfName_Type = DisplayString
_SwMSMVlanGroupProfName_Object = MibTableColumn
swMSMVlanGroupProfName = _SwMSMVlanGroupProfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 1),
    _SwMSMVlanGroupProfName_Type()
)
swMSMVlanGroupProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfName.setStatus("current")
_SwMSMVlanGroupProfID_Type = Integer32
_SwMSMVlanGroupProfID_Object = MibTableColumn
swMSMVlanGroupProfID = _SwMSMVlanGroupProfID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 2),
    _SwMSMVlanGroupProfID_Type()
)
swMSMVlanGroupProfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfID.setStatus("current")
_SwMSMVlanGroupProfStatus_Type = RowStatus
_SwMSMVlanGroupProfStatus_Object = MibTableColumn
swMSMVlanGroupProfStatus = _SwMSMVlanGroupProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 5, 1, 3),
    _SwMSMVlanGroupProfStatus_Type()
)
swMSMVlanGroupProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfStatus.setStatus("current")
_SwMSMVlanGroupProfAddrTable_Object = MibTable
swMSMVlanGroupProfAddrTable = _SwMSMVlanGroupProfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6)
)
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrTable.setStatus("current")
_SwMSMVlanGroupProfAddrEntry_Object = MibTableRow
swMSMVlanGroupProfAddrEntry = _SwMSMVlanGroupProfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1)
)
swMSMVlanGroupProfAddrEntry.setIndexNames(
    (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfName"),
    (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrType"),
    (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrStart"),
    (0, "MCAST-VLAN-MIB", "swMSMVlanGroupProfAddrEnd"),
)
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrEntry.setStatus("current")
_SwMSMVlanGroupProfAddrType_Type = InetAddressType
_SwMSMVlanGroupProfAddrType_Object = MibTableColumn
swMSMVlanGroupProfAddrType = _SwMSMVlanGroupProfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 1),
    _SwMSMVlanGroupProfAddrType_Type()
)
swMSMVlanGroupProfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrType.setStatus("current")
_SwMSMVlanGroupProfAddrStart_Type = InetAddress
_SwMSMVlanGroupProfAddrStart_Object = MibTableColumn
swMSMVlanGroupProfAddrStart = _SwMSMVlanGroupProfAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 2),
    _SwMSMVlanGroupProfAddrStart_Type()
)
swMSMVlanGroupProfAddrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrStart.setStatus("current")
_SwMSMVlanGroupProfAddrEnd_Type = InetAddress
_SwMSMVlanGroupProfAddrEnd_Object = MibTableColumn
swMSMVlanGroupProfAddrEnd = _SwMSMVlanGroupProfAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 3),
    _SwMSMVlanGroupProfAddrEnd_Type()
)
swMSMVlanGroupProfAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrEnd.setStatus("current")
_SwMSMVlanGroupProfAddrStatus_Type = RowStatus
_SwMSMVlanGroupProfAddrStatus_Object = MibTableColumn
swMSMVlanGroupProfAddrStatus = _SwMSMVlanGroupProfAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 64, 3, 6, 1, 4),
    _SwMSMVlanGroupProfAddrStatus_Type()
)
swMSMVlanGroupProfAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSMVlanGroupProfAddrStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAST-VLAN-MIB",
    **{"PortList": PortList,
       "swMcastVlanMIB": swMcastVlanMIB,
       "swMcastVlanCtrl": swMcastVlanCtrl,
       "swISMVlanGlobalState": swISMVlanGlobalState,
       "swMSMVlanGlobalState": swMSMVlanGlobalState,
       "swISMVlanForwardUnmatchedState": swISMVlanForwardUnmatchedState,
       "swMSMVlanForwardUnmatchedState": swMSMVlanForwardUnmatchedState,
       "swMcastVlanInfo": swMcastVlanInfo,
       "swMcastVlanMgmt": swMcastVlanMgmt,
       "swISMVlanTable": swISMVlanTable,
       "swISMVlanEntry": swISMVlanEntry,
       "swISMVlanID": swISMVlanID,
       "swISMVlanName": swISMVlanName,
       "swISMVlanSourcePort": swISMVlanSourcePort,
       "swISMVlanMemberPort": swISMVlanMemberPort,
       "swISMVlanTagMemberPort": swISMVlanTagMemberPort,
       "swISMVlanUntagSourcePort": swISMVlanUntagSourcePort,
       "swISMVlanState": swISMVlanState,
       "swISMVlanRepSourceAddrType": swISMVlanRepSourceAddrType,
       "swISMVlanRepSourceAddr": swISMVlanRepSourceAddr,
       "swISMVlanRemapPriority": swISMVlanRemapPriority,
       "swISMVlanReplacePriority": swISMVlanReplacePriority,
       "swISMVlanProfileIDList": swISMVlanProfileIDList,
       "swISMVlanRowStatus": swISMVlanRowStatus,
       "swISMVlanGroupProfTable": swISMVlanGroupProfTable,
       "swISMVlanGroupProfEntry": swISMVlanGroupProfEntry,
       "swISMVlanGroupProfName": swISMVlanGroupProfName,
       "swISMVlanGroupProfID": swISMVlanGroupProfID,
       "swISMVlanGroupProfStatus": swISMVlanGroupProfStatus,
       "swISMVlanGroupProfAddrTable": swISMVlanGroupProfAddrTable,
       "swISMVlanGroupProfAddrEntry": swISMVlanGroupProfAddrEntry,
       "swISMVlanGroupProfAddrType": swISMVlanGroupProfAddrType,
       "swISMVlanGroupProfAddrStart": swISMVlanGroupProfAddrStart,
       "swISMVlanGroupProfAddrEnd": swISMVlanGroupProfAddrEnd,
       "swISMVlanGroupProfAddrStatus": swISMVlanGroupProfAddrStatus,
       "swMSMVlanTable": swMSMVlanTable,
       "swMSMVlanEntry": swMSMVlanEntry,
       "swMSMVlanID": swMSMVlanID,
       "swMSMVlanName": swMSMVlanName,
       "swMSMVlanSourcePort": swMSMVlanSourcePort,
       "swMSMVlanMemberPort": swMSMVlanMemberPort,
       "swMSMVlanTagMemberPort": swMSMVlanTagMemberPort,
       "swMSMVlanUntagSourcePort": swMSMVlanUntagSourcePort,
       "swMSMVlanState": swMSMVlanState,
       "swMSMVlanRepSourceAddrType": swMSMVlanRepSourceAddrType,
       "swMSMVlanRepSourceAddr": swMSMVlanRepSourceAddr,
       "swMSMVlanRemapPriority": swMSMVlanRemapPriority,
       "swMSMVlanReplacePriority": swMSMVlanReplacePriority,
       "swMSMVlanProfileIDList": swMSMVlanProfileIDList,
       "swMSMVlanRowStatus": swMSMVlanRowStatus,
       "swMSMVlanGroupProfTable": swMSMVlanGroupProfTable,
       "swMSMVlanGroupProfEntry": swMSMVlanGroupProfEntry,
       "swMSMVlanGroupProfName": swMSMVlanGroupProfName,
       "swMSMVlanGroupProfID": swMSMVlanGroupProfID,
       "swMSMVlanGroupProfStatus": swMSMVlanGroupProfStatus,
       "swMSMVlanGroupProfAddrTable": swMSMVlanGroupProfAddrTable,
       "swMSMVlanGroupProfAddrEntry": swMSMVlanGroupProfAddrEntry,
       "swMSMVlanGroupProfAddrType": swMSMVlanGroupProfAddrType,
       "swMSMVlanGroupProfAddrStart": swMSMVlanGroupProfAddrStart,
       "swMSMVlanGroupProfAddrEnd": swMSMVlanGroupProfAddrEnd,
       "swMSMVlanGroupProfAddrStatus": swMSMVlanGroupProfAddrStatus}
)
