# SNMP MIB module (MERU-CONFIG-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-STATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:10 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAddressAssignmentType,
 MwlApIfModeType,
 MwlDeviceType,
 MwlL2SecurityMode,
 MwlVpnStatus) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAddressAssignmentType",
    "MwlApIfModeType",
    "MwlDeviceType",
    "MwlL2SecurityMode",
    "MwlVpnStatus")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigStation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwStationTable_Object = MibTable
mwStationTable = _MwStationTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mwStationTable.setStatus("current")
_MwStationEntry_Object = MibTableRow
mwStationEntry = _MwStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1)
)
mwStationEntry.setIndexNames(
    (0, "MERU-CONFIG-STATION-MIB", "mwStationTableIndex"),
)
if mibBuilder.loadTexts:
    mwStationEntry.setStatus("current")
_MwStationTableIndex_Type = Integer32
_MwStationTableIndex_Object = MibTableColumn
mwStationTableIndex = _MwStationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 1),
    _MwStationTableIndex_Type()
)
mwStationTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwStationTableIndex.setStatus("current")
_MwStationMacAddress_Type = MacAddress
_MwStationMacAddress_Object = MibTableColumn
mwStationMacAddress = _MwStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 2),
    _MwStationMacAddress_Type()
)
mwStationMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationMacAddress.setStatus("current")
_MwStationIpv6Address_Type = Ipv6Address
_MwStationIpv6Address_Object = MibTableColumn
mwStationIpv6Address = _MwStationIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 3),
    _MwStationIpv6Address_Type()
)
mwStationIpv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpv6Address.setStatus("current")
_MwStationAp_Type = Integer32
_MwStationAp_Object = MibTableColumn
mwStationAp = _MwStationAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 4),
    _MwStationAp_Type()
)
mwStationAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationAp.setStatus("current")
_MwStationApName_Type = DisplayString
_MwStationApName_Object = MibTableColumn
mwStationApName = _MwStationApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 5),
    _MwStationApName_Type()
)
mwStationApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationApName.setStatus("current")
_MwStationL3State_Type = MwlVpnStatus
_MwStationL3State_Object = MibTableColumn
mwStationL3State = _MwStationL3State_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 6),
    _MwStationL3State_Type()
)
mwStationL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationL3State.setStatus("current")
_MwStationVlanTag_Type = Unsigned32
_MwStationVlanTag_Object = MibTableColumn
mwStationVlanTag = _MwStationVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 7),
    _MwStationVlanTag_Type()
)
mwStationVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationVlanTag.setStatus("current")
_MwStationAuthUser_Type = DisplayString
_MwStationAuthUser_Object = MibTableColumn
mwStationAuthUser = _MwStationAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 8),
    _MwStationAuthUser_Type()
)
mwStationAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationAuthUser.setStatus("current")


class _MwStationVlanName_Type(DisplayString):
    """Custom type mwStationVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwStationVlanName_Type.__name__ = "DisplayString"
_MwStationVlanName_Object = MibTableColumn
mwStationVlanName = _MwStationVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 9),
    _MwStationVlanName_Type()
)
mwStationVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationVlanName.setStatus("current")
_MwStationRadioType_Type = MwlApIfModeType
_MwStationRadioType_Object = MibTableColumn
mwStationRadioType = _MwStationRadioType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 10),
    _MwStationRadioType_Type()
)
mwStationRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationRadioType.setStatus("current")
_MwStationL2ModeState_Type = MwlL2SecurityMode
_MwStationL2ModeState_Object = MibTableColumn
mwStationL2ModeState = _MwStationL2ModeState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 11),
    _MwStationL2ModeState_Type()
)
mwStationL2ModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationL2ModeState.setStatus("current")
_MwStationCurrentRssi_Type = Integer32
_MwStationCurrentRssi_Object = MibTableColumn
mwStationCurrentRssi = _MwStationCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 12),
    _MwStationCurrentRssi_Type()
)
mwStationCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationCurrentRssi.setStatus("current")
_MwStationTxThroughput_Type = Unsigned32
_MwStationTxThroughput_Object = MibTableColumn
mwStationTxThroughput = _MwStationTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 13),
    _MwStationTxThroughput_Type()
)
mwStationTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationTxThroughput.setStatus("current")
_MwStationRxThroughput_Type = Unsigned32
_MwStationRxThroughput_Object = MibTableColumn
mwStationRxThroughput = _MwStationRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 14),
    _MwStationRxThroughput_Type()
)
mwStationRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationRxThroughput.setStatus("current")
_MwStationLossPercentage_Type = Integer32
_MwStationLossPercentage_Object = MibTableColumn
mwStationLossPercentage = _MwStationLossPercentage_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 15),
    _MwStationLossPercentage_Type()
)
mwStationLossPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationLossPercentage.setStatus("current")
_MwStationAddrAssignmentType_Type = MwlAddressAssignmentType
_MwStationAddrAssignmentType_Object = MibTableColumn
mwStationAddrAssignmentType = _MwStationAddrAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 16),
    _MwStationAddrAssignmentType_Type()
)
mwStationAddrAssignmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationAddrAssignmentType.setStatus("current")
_MwStationChannelUtilization_Type = Counter64
_MwStationChannelUtilization_Object = MibTableColumn
mwStationChannelUtilization = _MwStationChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 17),
    _MwStationChannelUtilization_Type()
)
mwStationChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationChannelUtilization.setStatus("current")
_MwStationVirtualPort_Type = MacAddress
_MwStationVirtualPort_Object = MibTableColumn
mwStationVirtualPort = _MwStationVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 18),
    _MwStationVirtualPort_Type()
)
mwStationVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationVirtualPort.setStatus("current")
_MwStationDeviceType_Type = MwlDeviceType
_MwStationDeviceType_Object = MibTableColumn
mwStationDeviceType = _MwStationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 20),
    _MwStationDeviceType_Type()
)
mwStationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationDeviceType.setStatus("current")
_MwStationRowStatus_Type = RowStatus
_MwStationRowStatus_Object = MibTableColumn
mwStationRowStatus = _MwStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 29),
    _MwStationRowStatus_Type()
)
mwStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationRowStatus.setStatus("current")
_MwStationIpaddressTable_Object = MibTable
mwStationIpaddressTable = _MwStationIpaddressTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    mwStationIpaddressTable.setStatus("current")
_MwStationIpaddressEntry_Object = MibTableRow
mwStationIpaddressEntry = _MwStationIpaddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1)
)
mwStationIpaddressEntry.setIndexNames(
    (0, "MERU-CONFIG-STATION-MIB", "mwStationIpaddressTableIndex"),
)
if mibBuilder.loadTexts:
    mwStationIpaddressEntry.setStatus("current")
_MwStationIpaddressTableIndex_Type = Integer32
_MwStationIpaddressTableIndex_Object = MibTableColumn
mwStationIpaddressTableIndex = _MwStationIpaddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 1),
    _MwStationIpaddressTableIndex_Type()
)
mwStationIpaddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwStationIpaddressTableIndex.setStatus("current")
_MwStationIpaddressMacAddress_Type = MacAddress
_MwStationIpaddressMacAddress_Object = MibTableColumn
mwStationIpaddressMacAddress = _MwStationIpaddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 2),
    _MwStationIpaddressMacAddress_Type()
)
mwStationIpaddressMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpaddressMacAddress.setStatus("current")
_MwStationIpaddressIpAddress_Type = IpAddress
_MwStationIpaddressIpAddress_Object = MibTableColumn
mwStationIpaddressIpAddress = _MwStationIpaddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 3),
    _MwStationIpaddressIpAddress_Type()
)
mwStationIpaddressIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpaddressIpAddress.setStatus("current")
_MwStationIpaddressAddrAssignmentType_Type = MwlAddressAssignmentType
_MwStationIpaddressAddrAssignmentType_Object = MibTableColumn
mwStationIpaddressAddrAssignmentType = _MwStationIpaddressAddrAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 4),
    _MwStationIpaddressAddrAssignmentType_Type()
)
mwStationIpaddressAddrAssignmentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpaddressAddrAssignmentType.setStatus("current")
_MwStationIpaddressVirtualAddress_Type = MacAddress
_MwStationIpaddressVirtualAddress_Object = MibTableColumn
mwStationIpaddressVirtualAddress = _MwStationIpaddressVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 5),
    _MwStationIpaddressVirtualAddress_Type()
)
mwStationIpaddressVirtualAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpaddressVirtualAddress.setStatus("current")
_MwStationIpaddressRowStatus_Type = RowStatus
_MwStationIpaddressRowStatus_Object = MibTableColumn
mwStationIpaddressRowStatus = _MwStationIpaddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 6),
    _MwStationIpaddressRowStatus_Type()
)
mwStationIpaddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwStationIpaddressRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-STATION-MIB",
    **{"mwConfigStation": mwConfigStation,
       "mwStationTable": mwStationTable,
       "mwStationEntry": mwStationEntry,
       "mwStationTableIndex": mwStationTableIndex,
       "mwStationMacAddress": mwStationMacAddress,
       "mwStationIpv6Address": mwStationIpv6Address,
       "mwStationAp": mwStationAp,
       "mwStationApName": mwStationApName,
       "mwStationL3State": mwStationL3State,
       "mwStationVlanTag": mwStationVlanTag,
       "mwStationAuthUser": mwStationAuthUser,
       "mwStationVlanName": mwStationVlanName,
       "mwStationRadioType": mwStationRadioType,
       "mwStationL2ModeState": mwStationL2ModeState,
       "mwStationCurrentRssi": mwStationCurrentRssi,
       "mwStationTxThroughput": mwStationTxThroughput,
       "mwStationRxThroughput": mwStationRxThroughput,
       "mwStationLossPercentage": mwStationLossPercentage,
       "mwStationAddrAssignmentType": mwStationAddrAssignmentType,
       "mwStationChannelUtilization": mwStationChannelUtilization,
       "mwStationVirtualPort": mwStationVirtualPort,
       "mwStationDeviceType": mwStationDeviceType,
       "mwStationRowStatus": mwStationRowStatus,
       "mwStationIpaddressTable": mwStationIpaddressTable,
       "mwStationIpaddressEntry": mwStationIpaddressEntry,
       "mwStationIpaddressTableIndex": mwStationIpaddressTableIndex,
       "mwStationIpaddressMacAddress": mwStationIpaddressMacAddress,
       "mwStationIpaddressIpAddress": mwStationIpaddressIpAddress,
       "mwStationIpaddressAddrAssignmentType": mwStationIpaddressAddrAssignmentType,
       "mwStationIpaddressVirtualAddress": mwStationIpaddressVirtualAddress,
       "mwStationIpaddressRowStatus": mwStationIpaddressRowStatus}
)
