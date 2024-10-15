# SNMP MIB module (LLDP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:49 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifGeneralInformationGroup")

(LldpV2ChassisId,
 LldpV2ChassisIdSubtype,
 LldpV2DestAddressTableIndex,
 LldpV2ManAddrIfSubtype,
 LldpV2ManAddress,
 LldpV2PortId,
 LldpV2PortIdSubtype,
 LldpV2SystemCapabilitiesMap,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2ChassisId",
    "LldpV2ChassisIdSubtype",
    "LldpV2DestAddressTableIndex",
    "LldpV2ManAddrIfSubtype",
    "LldpV2ManAddress",
    "LldpV2PortId",
    "LldpV2PortIdSubtype",
    "LldpV2SystemCapabilitiesMap",
    "ieee802dot1mibs")

(TimeFilter,
 ZeroBasedCounter32) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter",
    "ZeroBasedCounter32")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

lldpV2MIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13)
)
lldpV2MIB.setRevisions(
        ("2016-03-11 00:00",
         "2015-02-16 00:00",
         "2009-06-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpV2Notifications_ObjectIdentity = ObjectIdentity
lldpV2Notifications = _LldpV2Notifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 0)
)
_LldpV2NotificationPrefix_ObjectIdentity = ObjectIdentity
lldpV2NotificationPrefix = _LldpV2NotificationPrefix_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 0, 0)
)
_LldpV2Objects_ObjectIdentity = ObjectIdentity
lldpV2Objects = _LldpV2Objects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1)
)
_LldpV2Configuration_ObjectIdentity = ObjectIdentity
lldpV2Configuration = _LldpV2Configuration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1)
)


class _LldpV2MessageTxInterval_Type(Unsigned32):
    """Custom type lldpV2MessageTxInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpV2MessageTxInterval_Type.__name__ = "Unsigned32"
_LldpV2MessageTxInterval_Object = MibScalar
lldpV2MessageTxInterval = _LldpV2MessageTxInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 1),
    _LldpV2MessageTxInterval_Type()
)
lldpV2MessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2MessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2MessageTxInterval.setUnits("seconds")


class _LldpV2MessageTxHoldMultiplier_Type(Unsigned32):
    """Custom type lldpV2MessageTxHoldMultiplier based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpV2MessageTxHoldMultiplier_Type.__name__ = "Unsigned32"
_LldpV2MessageTxHoldMultiplier_Object = MibScalar
lldpV2MessageTxHoldMultiplier = _LldpV2MessageTxHoldMultiplier_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 2),
    _LldpV2MessageTxHoldMultiplier_Type()
)
lldpV2MessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2MessageTxHoldMultiplier.setStatus("current")


class _LldpV2ReinitDelay_Type(Unsigned32):
    """Custom type lldpV2ReinitDelay based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpV2ReinitDelay_Type.__name__ = "Unsigned32"
_LldpV2ReinitDelay_Object = MibScalar
lldpV2ReinitDelay = _LldpV2ReinitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 3),
    _LldpV2ReinitDelay_Type()
)
lldpV2ReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2ReinitDelay.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2ReinitDelay.setUnits("seconds")


class _LldpV2NotificationInterval_Type(Unsigned32):
    """Custom type lldpV2NotificationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_LldpV2NotificationInterval_Type.__name__ = "Unsigned32"
_LldpV2NotificationInterval_Object = MibScalar
lldpV2NotificationInterval = _LldpV2NotificationInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 4),
    _LldpV2NotificationInterval_Type()
)
lldpV2NotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2NotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2NotificationInterval.setUnits("seconds")


class _LldpV2TxCreditMax_Type(Unsigned32):
    """Custom type lldpV2TxCreditMax based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LldpV2TxCreditMax_Type.__name__ = "Unsigned32"
_LldpV2TxCreditMax_Object = MibScalar
lldpV2TxCreditMax = _LldpV2TxCreditMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 5),
    _LldpV2TxCreditMax_Type()
)
lldpV2TxCreditMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2TxCreditMax.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2TxCreditMax.setUnits("PDUs")


class _LldpV2MessageFastTx_Type(Unsigned32):
    """Custom type lldpV2MessageFastTx based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_LldpV2MessageFastTx_Type.__name__ = "Unsigned32"
_LldpV2MessageFastTx_Object = MibScalar
lldpV2MessageFastTx = _LldpV2MessageFastTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 6),
    _LldpV2MessageFastTx_Type()
)
lldpV2MessageFastTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2MessageFastTx.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2MessageFastTx.setUnits("seconds")


class _LldpV2TxFastInit_Type(Unsigned32):
    """Custom type lldpV2TxFastInit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LldpV2TxFastInit_Type.__name__ = "Unsigned32"
_LldpV2TxFastInit_Object = MibScalar
lldpV2TxFastInit = _LldpV2TxFastInit_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 7),
    _LldpV2TxFastInit_Type()
)
lldpV2TxFastInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2TxFastInit.setStatus("current")
_LldpV2PortConfigTable_Object = MibTable
lldpV2PortConfigTable = _LldpV2PortConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8)
)
if mibBuilder.loadTexts:
    lldpV2PortConfigTable.setStatus("deprecated")
_LldpV2PortConfigEntry_Object = MibTableRow
lldpV2PortConfigEntry = _LldpV2PortConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1)
)
lldpV2PortConfigEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2PortConfigIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2PortConfigDestAddressIndex"),
)
if mibBuilder.loadTexts:
    lldpV2PortConfigEntry.setStatus("deprecated")
_LldpV2PortConfigIfIndex_Type = InterfaceIndex
_LldpV2PortConfigIfIndex_Object = MibTableColumn
lldpV2PortConfigIfIndex = _LldpV2PortConfigIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 1),
    _LldpV2PortConfigIfIndex_Type()
)
lldpV2PortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2PortConfigIfIndex.setStatus("deprecated")
_LldpV2PortConfigDestAddressIndex_Type = LldpV2DestAddressTableIndex
_LldpV2PortConfigDestAddressIndex_Object = MibTableColumn
lldpV2PortConfigDestAddressIndex = _LldpV2PortConfigDestAddressIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 2),
    _LldpV2PortConfigDestAddressIndex_Type()
)
lldpV2PortConfigDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2PortConfigDestAddressIndex.setStatus("deprecated")


class _LldpV2PortConfigAdminStatus_Type(Integer32):
    """Custom type lldpV2PortConfigAdminStatus based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_LldpV2PortConfigAdminStatus_Type.__name__ = "Integer32"
_LldpV2PortConfigAdminStatus_Object = MibTableColumn
lldpV2PortConfigAdminStatus = _LldpV2PortConfigAdminStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 3),
    _LldpV2PortConfigAdminStatus_Type()
)
lldpV2PortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigAdminStatus.setStatus("deprecated")


class _LldpV2PortConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpV2PortConfigNotificationEnable based on TruthValue"""


_LldpV2PortConfigNotificationEnable_Object = MibTableColumn
lldpV2PortConfigNotificationEnable = _LldpV2PortConfigNotificationEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 4),
    _LldpV2PortConfigNotificationEnable_Type()
)
lldpV2PortConfigNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigNotificationEnable.setStatus("deprecated")


class _LldpV2PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpV2PortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_LldpV2PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpV2PortConfigTLVsTxEnable_Object = MibTableColumn
lldpV2PortConfigTLVsTxEnable = _LldpV2PortConfigTLVsTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 5),
    _LldpV2PortConfigTLVsTxEnable_Type()
)
lldpV2PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigTLVsTxEnable.setStatus("deprecated")
_LldpV2DestAddressTable_Object = MibTable
lldpV2DestAddressTable = _LldpV2DestAddressTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9)
)
if mibBuilder.loadTexts:
    lldpV2DestAddressTable.setStatus("current")
_LldpV2DestAddressTableEntry_Object = MibTableRow
lldpV2DestAddressTableEntry = _LldpV2DestAddressTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1)
)
lldpV2DestAddressTableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2AddressTableIndex"),
)
if mibBuilder.loadTexts:
    lldpV2DestAddressTableEntry.setStatus("current")
_LldpV2AddressTableIndex_Type = LldpV2DestAddressTableIndex
_LldpV2AddressTableIndex_Object = MibTableColumn
lldpV2AddressTableIndex = _LldpV2AddressTableIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1, 1),
    _LldpV2AddressTableIndex_Type()
)
lldpV2AddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2AddressTableIndex.setStatus("current")
_LldpV2DestMacAddress_Type = MacAddress
_LldpV2DestMacAddress_Object = MibTableColumn
lldpV2DestMacAddress = _LldpV2DestMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1, 2),
    _LldpV2DestMacAddress_Type()
)
lldpV2DestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2DestMacAddress.setStatus("current")
_LldpV2ManAddrConfigTxPortsTable_Object = MibTable
lldpV2ManAddrConfigTxPortsTable = _LldpV2ManAddrConfigTxPortsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10)
)
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigTxPortsTable.setStatus("current")
_LldpV2ManAddrConfigTxPortsEntry_Object = MibTableRow
lldpV2ManAddrConfigTxPortsEntry = _LldpV2ManAddrConfigTxPortsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1)
)
lldpV2ManAddrConfigTxPortsEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigDestAddressIndex"),
    (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigLocManAddrSubtype"),
    (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigLocManAddr"),
)
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigTxPortsEntry.setStatus("current")
_LldpV2ManAddrConfigIfIndex_Type = InterfaceIndex
_LldpV2ManAddrConfigIfIndex_Object = MibTableColumn
lldpV2ManAddrConfigIfIndex = _LldpV2ManAddrConfigIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 1),
    _LldpV2ManAddrConfigIfIndex_Type()
)
lldpV2ManAddrConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigIfIndex.setStatus("current")
_LldpV2ManAddrConfigDestAddressIndex_Type = LldpV2DestAddressTableIndex
_LldpV2ManAddrConfigDestAddressIndex_Object = MibTableColumn
lldpV2ManAddrConfigDestAddressIndex = _LldpV2ManAddrConfigDestAddressIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 2),
    _LldpV2ManAddrConfigDestAddressIndex_Type()
)
lldpV2ManAddrConfigDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigDestAddressIndex.setStatus("current")
_LldpV2ManAddrConfigLocManAddrSubtype_Type = AddressFamilyNumbers
_LldpV2ManAddrConfigLocManAddrSubtype_Object = MibTableColumn
lldpV2ManAddrConfigLocManAddrSubtype = _LldpV2ManAddrConfigLocManAddrSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 3),
    _LldpV2ManAddrConfigLocManAddrSubtype_Type()
)
lldpV2ManAddrConfigLocManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigLocManAddrSubtype.setStatus("current")
_LldpV2ManAddrConfigLocManAddr_Type = LldpV2ManAddress
_LldpV2ManAddrConfigLocManAddr_Object = MibTableColumn
lldpV2ManAddrConfigLocManAddr = _LldpV2ManAddrConfigLocManAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 4),
    _LldpV2ManAddrConfigLocManAddr_Type()
)
lldpV2ManAddrConfigLocManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigLocManAddr.setStatus("current")


class _LldpV2ManAddrConfigTxEnable_Type(TruthValue):
    """Custom type lldpV2ManAddrConfigTxEnable based on TruthValue"""


_LldpV2ManAddrConfigTxEnable_Object = MibTableColumn
lldpV2ManAddrConfigTxEnable = _LldpV2ManAddrConfigTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 5),
    _LldpV2ManAddrConfigTxEnable_Type()
)
lldpV2ManAddrConfigTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigTxEnable.setStatus("current")
_LldpV2ManAddrConfigRowStatus_Type = RowStatus
_LldpV2ManAddrConfigRowStatus_Object = MibTableColumn
lldpV2ManAddrConfigRowStatus = _LldpV2ManAddrConfigRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 6),
    _LldpV2ManAddrConfigRowStatus_Type()
)
lldpV2ManAddrConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2ManAddrConfigRowStatus.setStatus("current")
_LldpV2PortConfigTableV2_Object = MibTable
lldpV2PortConfigTableV2 = _LldpV2PortConfigTableV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11)
)
if mibBuilder.loadTexts:
    lldpV2PortConfigTableV2.setStatus("current")
_LldpV2PortConfigEntryV2_Object = MibTableRow
lldpV2PortConfigEntryV2 = _LldpV2PortConfigEntryV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1)
)
lldpV2PortConfigEntryV2.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2PortConfigIfIndexV2"),
    (0, "LLDP-V2-MIB", "lldpV2PortConfigDestAddressIndexV2"),
)
if mibBuilder.loadTexts:
    lldpV2PortConfigEntryV2.setStatus("current")
_LldpV2PortConfigIfIndexV2_Type = InterfaceIndex
_LldpV2PortConfigIfIndexV2_Object = MibTableColumn
lldpV2PortConfigIfIndexV2 = _LldpV2PortConfigIfIndexV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 1),
    _LldpV2PortConfigIfIndexV2_Type()
)
lldpV2PortConfigIfIndexV2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2PortConfigIfIndexV2.setStatus("current")
_LldpV2PortConfigDestAddressIndexV2_Type = LldpV2DestAddressTableIndex
_LldpV2PortConfigDestAddressIndexV2_Object = MibTableColumn
lldpV2PortConfigDestAddressIndexV2 = _LldpV2PortConfigDestAddressIndexV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 2),
    _LldpV2PortConfigDestAddressIndexV2_Type()
)
lldpV2PortConfigDestAddressIndexV2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2PortConfigDestAddressIndexV2.setStatus("current")


class _LldpV2PortConfigAdminStatusV2_Type(Integer32):
    """Custom type lldpV2PortConfigAdminStatusV2 based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_LldpV2PortConfigAdminStatusV2_Type.__name__ = "Integer32"
_LldpV2PortConfigAdminStatusV2_Object = MibTableColumn
lldpV2PortConfigAdminStatusV2 = _LldpV2PortConfigAdminStatusV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 3),
    _LldpV2PortConfigAdminStatusV2_Type()
)
lldpV2PortConfigAdminStatusV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigAdminStatusV2.setStatus("current")


class _LldpV2PortMessageTxInterval_Type(Unsigned32):
    """Custom type lldpV2PortMessageTxInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpV2PortMessageTxInterval_Type.__name__ = "Unsigned32"
_LldpV2PortMessageTxInterval_Object = MibTableColumn
lldpV2PortMessageTxInterval = _LldpV2PortMessageTxInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 4),
    _LldpV2PortMessageTxInterval_Type()
)
lldpV2PortMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortMessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2PortMessageTxInterval.setUnits("seconds")


class _LldpV2PortMessageTxHoldMultiplier_Type(Unsigned32):
    """Custom type lldpV2PortMessageTxHoldMultiplier based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpV2PortMessageTxHoldMultiplier_Type.__name__ = "Unsigned32"
_LldpV2PortMessageTxHoldMultiplier_Object = MibTableColumn
lldpV2PortMessageTxHoldMultiplier = _LldpV2PortMessageTxHoldMultiplier_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 5),
    _LldpV2PortMessageTxHoldMultiplier_Type()
)
lldpV2PortMessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortMessageTxHoldMultiplier.setStatus("current")


class _LldpV2PortReinitDelay_Type(Unsigned32):
    """Custom type lldpV2PortReinitDelay based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpV2PortReinitDelay_Type.__name__ = "Unsigned32"
_LldpV2PortReinitDelay_Object = MibTableColumn
lldpV2PortReinitDelay = _LldpV2PortReinitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 6),
    _LldpV2PortReinitDelay_Type()
)
lldpV2PortReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortReinitDelay.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2PortReinitDelay.setUnits("seconds")


class _LldpV2PortNotificationInterval_Type(Unsigned32):
    """Custom type lldpV2PortNotificationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_LldpV2PortNotificationInterval_Type.__name__ = "Unsigned32"
_LldpV2PortNotificationInterval_Object = MibTableColumn
lldpV2PortNotificationInterval = _LldpV2PortNotificationInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 7),
    _LldpV2PortNotificationInterval_Type()
)
lldpV2PortNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2PortNotificationInterval.setUnits("seconds")


class _LldpV2PortTxCreditMax_Type(Unsigned32):
    """Custom type lldpV2PortTxCreditMax based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LldpV2PortTxCreditMax_Type.__name__ = "Unsigned32"
_LldpV2PortTxCreditMax_Object = MibTableColumn
lldpV2PortTxCreditMax = _LldpV2PortTxCreditMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 8),
    _LldpV2PortTxCreditMax_Type()
)
lldpV2PortTxCreditMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortTxCreditMax.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2PortTxCreditMax.setUnits("PDUs")


class _LldpV2PortMessageFastTx_Type(Unsigned32):
    """Custom type lldpV2PortMessageFastTx based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_LldpV2PortMessageFastTx_Type.__name__ = "Unsigned32"
_LldpV2PortMessageFastTx_Object = MibTableColumn
lldpV2PortMessageFastTx = _LldpV2PortMessageFastTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 9),
    _LldpV2PortMessageFastTx_Type()
)
lldpV2PortMessageFastTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortMessageFastTx.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2PortMessageFastTx.setUnits("seconds")


class _LldpV2PortTxFastInit_Type(Unsigned32):
    """Custom type lldpV2PortTxFastInit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LldpV2PortTxFastInit_Type.__name__ = "Unsigned32"
_LldpV2PortTxFastInit_Object = MibTableColumn
lldpV2PortTxFastInit = _LldpV2PortTxFastInit_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 10),
    _LldpV2PortTxFastInit_Type()
)
lldpV2PortTxFastInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortTxFastInit.setStatus("current")


class _LldpV2PortConfigNotificationEnableV2_Type(TruthValue):
    """Custom type lldpV2PortConfigNotificationEnableV2 based on TruthValue"""


_LldpV2PortConfigNotificationEnableV2_Object = MibTableColumn
lldpV2PortConfigNotificationEnableV2 = _LldpV2PortConfigNotificationEnableV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 11),
    _LldpV2PortConfigNotificationEnableV2_Type()
)
lldpV2PortConfigNotificationEnableV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigNotificationEnableV2.setStatus("current")


class _LldpV2PortConfigTLVsTxEnableV2_Type(Bits):
    """Custom type lldpV2PortConfigTLVsTxEnableV2 based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_LldpV2PortConfigTLVsTxEnableV2_Type.__name__ = "Bits"
_LldpV2PortConfigTLVsTxEnableV2_Object = MibTableColumn
lldpV2PortConfigTLVsTxEnableV2 = _LldpV2PortConfigTLVsTxEnableV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 11, 1, 12),
    _LldpV2PortConfigTLVsTxEnableV2_Type()
)
lldpV2PortConfigTLVsTxEnableV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2PortConfigTLVsTxEnableV2.setStatus("current")
_LldpV2Statistics_ObjectIdentity = ObjectIdentity
lldpV2Statistics = _LldpV2Statistics_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2)
)
_LldpV2StatsRemTablesLastChangeTime_Type = TimeStamp
_LldpV2StatsRemTablesLastChangeTime_Object = MibScalar
lldpV2StatsRemTablesLastChangeTime = _LldpV2StatsRemTablesLastChangeTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 1),
    _LldpV2StatsRemTablesLastChangeTime_Type()
)
lldpV2StatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesLastChangeTime.setStatus("current")
_LldpV2StatsRemTablesInserts_Type = ZeroBasedCounter32
_LldpV2StatsRemTablesInserts_Object = MibScalar
lldpV2StatsRemTablesInserts = _LldpV2StatsRemTablesInserts_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 2),
    _LldpV2StatsRemTablesInserts_Type()
)
lldpV2StatsRemTablesInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesInserts.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesInserts.setUnits("table entries")
_LldpV2StatsRemTablesDeletes_Type = ZeroBasedCounter32
_LldpV2StatsRemTablesDeletes_Object = MibScalar
lldpV2StatsRemTablesDeletes = _LldpV2StatsRemTablesDeletes_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 3),
    _LldpV2StatsRemTablesDeletes_Type()
)
lldpV2StatsRemTablesDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesDeletes.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesDeletes.setUnits("table entries")
_LldpV2StatsRemTablesDrops_Type = ZeroBasedCounter32
_LldpV2StatsRemTablesDrops_Object = MibScalar
lldpV2StatsRemTablesDrops = _LldpV2StatsRemTablesDrops_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 4),
    _LldpV2StatsRemTablesDrops_Type()
)
lldpV2StatsRemTablesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesDrops.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesDrops.setUnits("table entries")
_LldpV2StatsRemTablesAgeouts_Type = ZeroBasedCounter32
_LldpV2StatsRemTablesAgeouts_Object = MibScalar
lldpV2StatsRemTablesAgeouts = _LldpV2StatsRemTablesAgeouts_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 5),
    _LldpV2StatsRemTablesAgeouts_Type()
)
lldpV2StatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesAgeouts.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRemTablesAgeouts.setUnits("table entries")
_LldpV2StatsTxPortTable_Object = MibTable
lldpV2StatsTxPortTable = _LldpV2StatsTxPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6)
)
if mibBuilder.loadTexts:
    lldpV2StatsTxPortTable.setStatus("current")
_LldpV2StatsTxPortEntry_Object = MibTableRow
lldpV2StatsTxPortEntry = _LldpV2StatsTxPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1)
)
lldpV2StatsTxPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2StatsTxIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2StatsTxDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2StatsTxPortEntry.setStatus("current")
_LldpV2StatsTxIfIndex_Type = InterfaceIndex
_LldpV2StatsTxIfIndex_Object = MibTableColumn
lldpV2StatsTxIfIndex = _LldpV2StatsTxIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 1),
    _LldpV2StatsTxIfIndex_Type()
)
lldpV2StatsTxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2StatsTxIfIndex.setStatus("current")
_LldpV2StatsTxDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2StatsTxDestMACAddress_Object = MibTableColumn
lldpV2StatsTxDestMACAddress = _LldpV2StatsTxDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 2),
    _LldpV2StatsTxDestMACAddress_Type()
)
lldpV2StatsTxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2StatsTxDestMACAddress.setStatus("current")
_LldpV2StatsTxPortFramesTotal_Type = Counter32
_LldpV2StatsTxPortFramesTotal_Object = MibTableColumn
lldpV2StatsTxPortFramesTotal = _LldpV2StatsTxPortFramesTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 3),
    _LldpV2StatsTxPortFramesTotal_Type()
)
lldpV2StatsTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsTxPortFramesTotal.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsTxPortFramesTotal.setUnits("LLDP frames")
_LldpV2StatsTxLLDPDULengthErrors_Type = Counter32
_LldpV2StatsTxLLDPDULengthErrors_Object = MibTableColumn
lldpV2StatsTxLLDPDULengthErrors = _LldpV2StatsTxLLDPDULengthErrors_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 4),
    _LldpV2StatsTxLLDPDULengthErrors_Type()
)
lldpV2StatsTxLLDPDULengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsTxLLDPDULengthErrors.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsTxLLDPDULengthErrors.setUnits("LLDP frames")
_LldpV2StatsRxPortTable_Object = MibTable
lldpV2StatsRxPortTable = _LldpV2StatsRxPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7)
)
if mibBuilder.loadTexts:
    lldpV2StatsRxPortTable.setStatus("current")
_LldpV2StatsRxPortEntry_Object = MibTableRow
lldpV2StatsRxPortEntry = _LldpV2StatsRxPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1)
)
lldpV2StatsRxPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2StatsRxDestIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2StatsRxDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2StatsRxPortEntry.setStatus("current")
_LldpV2StatsRxDestIfIndex_Type = InterfaceIndex
_LldpV2StatsRxDestIfIndex_Object = MibTableColumn
lldpV2StatsRxDestIfIndex = _LldpV2StatsRxDestIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 1),
    _LldpV2StatsRxDestIfIndex_Type()
)
lldpV2StatsRxDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2StatsRxDestIfIndex.setStatus("current")
_LldpV2StatsRxDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2StatsRxDestMACAddress_Object = MibTableColumn
lldpV2StatsRxDestMACAddress = _LldpV2StatsRxDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 2),
    _LldpV2StatsRxDestMACAddress_Type()
)
lldpV2StatsRxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2StatsRxDestMACAddress.setStatus("current")
_LldpV2StatsRxPortFramesDiscardedTotal_Type = Counter32
_LldpV2StatsRxPortFramesDiscardedTotal_Object = MibTableColumn
lldpV2StatsRxPortFramesDiscardedTotal = _LldpV2StatsRxPortFramesDiscardedTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 3),
    _LldpV2StatsRxPortFramesDiscardedTotal_Type()
)
lldpV2StatsRxPortFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesDiscardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesDiscardedTotal.setUnits("LLDP frames")
_LldpV2StatsRxPortFramesErrors_Type = Counter32
_LldpV2StatsRxPortFramesErrors_Object = MibTableColumn
lldpV2StatsRxPortFramesErrors = _LldpV2StatsRxPortFramesErrors_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 4),
    _LldpV2StatsRxPortFramesErrors_Type()
)
lldpV2StatsRxPortFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesErrors.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesErrors.setUnits("LLDP frames")
_LldpV2StatsRxPortFramesTotal_Type = Counter32
_LldpV2StatsRxPortFramesTotal_Object = MibTableColumn
lldpV2StatsRxPortFramesTotal = _LldpV2StatsRxPortFramesTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 5),
    _LldpV2StatsRxPortFramesTotal_Type()
)
lldpV2StatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesTotal.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesTotal.setUnits("LLDP frames")
_LldpV2StatsRxPortTLVsDiscardedTotal_Type = Counter32
_LldpV2StatsRxPortTLVsDiscardedTotal_Object = MibTableColumn
lldpV2StatsRxPortTLVsDiscardedTotal = _LldpV2StatsRxPortTLVsDiscardedTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 6),
    _LldpV2StatsRxPortTLVsDiscardedTotal_Type()
)
lldpV2StatsRxPortTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortTLVsDiscardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortTLVsDiscardedTotal.setUnits("TLVs")
_LldpV2StatsRxPortTLVsUnrecognizedTotal_Type = Counter32
_LldpV2StatsRxPortTLVsUnrecognizedTotal_Object = MibTableColumn
lldpV2StatsRxPortTLVsUnrecognizedTotal = _LldpV2StatsRxPortTLVsUnrecognizedTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 7),
    _LldpV2StatsRxPortTLVsUnrecognizedTotal_Type()
)
lldpV2StatsRxPortTLVsUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortTLVsUnrecognizedTotal.setStatus("current")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortTLVsUnrecognizedTotal.setUnits("TLVs")
_LldpV2StatsRxPortAgeoutsTotal_Type = ZeroBasedCounter32
_LldpV2StatsRxPortAgeoutsTotal_Object = MibTableColumn
lldpV2StatsRxPortAgeoutsTotal = _LldpV2StatsRxPortAgeoutsTotal_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 8),
    _LldpV2StatsRxPortAgeoutsTotal_Type()
)
lldpV2StatsRxPortAgeoutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortAgeoutsTotal.setStatus("current")
_LldpV2LocalSystemData_ObjectIdentity = ObjectIdentity
lldpV2LocalSystemData = _LldpV2LocalSystemData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3)
)
_LldpV2LocChassisIdSubtype_Type = LldpV2ChassisIdSubtype
_LldpV2LocChassisIdSubtype_Object = MibScalar
lldpV2LocChassisIdSubtype = _LldpV2LocChassisIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 1),
    _LldpV2LocChassisIdSubtype_Type()
)
lldpV2LocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocChassisIdSubtype.setStatus("current")
_LldpV2LocChassisId_Type = LldpV2ChassisId
_LldpV2LocChassisId_Object = MibScalar
lldpV2LocChassisId = _LldpV2LocChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 2),
    _LldpV2LocChassisId_Type()
)
lldpV2LocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocChassisId.setStatus("current")


class _LldpV2LocSysName_Type(SnmpAdminString):
    """Custom type lldpV2LocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2LocSysName_Type.__name__ = "SnmpAdminString"
_LldpV2LocSysName_Object = MibScalar
lldpV2LocSysName = _LldpV2LocSysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 3),
    _LldpV2LocSysName_Type()
)
lldpV2LocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocSysName.setStatus("current")


class _LldpV2LocSysDesc_Type(SnmpAdminString):
    """Custom type lldpV2LocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2LocSysDesc_Type.__name__ = "SnmpAdminString"
_LldpV2LocSysDesc_Object = MibScalar
lldpV2LocSysDesc = _LldpV2LocSysDesc_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 4),
    _LldpV2LocSysDesc_Type()
)
lldpV2LocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocSysDesc.setStatus("current")
_LldpV2LocSysCapSupported_Type = LldpV2SystemCapabilitiesMap
_LldpV2LocSysCapSupported_Object = MibScalar
lldpV2LocSysCapSupported = _LldpV2LocSysCapSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 5),
    _LldpV2LocSysCapSupported_Type()
)
lldpV2LocSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocSysCapSupported.setStatus("current")
_LldpV2LocSysCapEnabled_Type = LldpV2SystemCapabilitiesMap
_LldpV2LocSysCapEnabled_Object = MibScalar
lldpV2LocSysCapEnabled = _LldpV2LocSysCapEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 6),
    _LldpV2LocSysCapEnabled_Type()
)
lldpV2LocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocSysCapEnabled.setStatus("current")
_LldpV2LocPortTable_Object = MibTable
lldpV2LocPortTable = _LldpV2LocPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7)
)
if mibBuilder.loadTexts:
    lldpV2LocPortTable.setStatus("current")
_LldpV2LocPortEntry_Object = MibTableRow
lldpV2LocPortEntry = _LldpV2LocPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1)
)
lldpV2LocPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2LocPortEntry.setStatus("current")
_LldpV2LocPortIfIndex_Type = InterfaceIndex
_LldpV2LocPortIfIndex_Object = MibTableColumn
lldpV2LocPortIfIndex = _LldpV2LocPortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 1),
    _LldpV2LocPortIfIndex_Type()
)
lldpV2LocPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocPortIfIndex.setStatus("current")
_LldpV2LocPortIdSubtype_Type = LldpV2PortIdSubtype
_LldpV2LocPortIdSubtype_Object = MibTableColumn
lldpV2LocPortIdSubtype = _LldpV2LocPortIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 2),
    _LldpV2LocPortIdSubtype_Type()
)
lldpV2LocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocPortIdSubtype.setStatus("current")
_LldpV2LocPortId_Type = LldpV2PortId
_LldpV2LocPortId_Object = MibTableColumn
lldpV2LocPortId = _LldpV2LocPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 3),
    _LldpV2LocPortId_Type()
)
lldpV2LocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocPortId.setStatus("current")


class _LldpV2LocPortDesc_Type(SnmpAdminString):
    """Custom type lldpV2LocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2LocPortDesc_Type.__name__ = "SnmpAdminString"
_LldpV2LocPortDesc_Object = MibTableColumn
lldpV2LocPortDesc = _LldpV2LocPortDesc_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 4),
    _LldpV2LocPortDesc_Type()
)
lldpV2LocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocPortDesc.setStatus("current")
_LldpV2LocManAddrTable_Object = MibTable
lldpV2LocManAddrTable = _LldpV2LocManAddrTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8)
)
if mibBuilder.loadTexts:
    lldpV2LocManAddrTable.setStatus("current")
_LldpV2LocManAddrEntry_Object = MibTableRow
lldpV2LocManAddrEntry = _LldpV2LocManAddrEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1)
)
lldpV2LocManAddrEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocManAddrSubtype"),
    (0, "LLDP-V2-MIB", "lldpV2LocManAddr"),
)
if mibBuilder.loadTexts:
    lldpV2LocManAddrEntry.setStatus("current")
_LldpV2LocManAddrSubtype_Type = AddressFamilyNumbers
_LldpV2LocManAddrSubtype_Object = MibTableColumn
lldpV2LocManAddrSubtype = _LldpV2LocManAddrSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 1),
    _LldpV2LocManAddrSubtype_Type()
)
lldpV2LocManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocManAddrSubtype.setStatus("current")
_LldpV2LocManAddr_Type = LldpV2ManAddress
_LldpV2LocManAddr_Object = MibTableColumn
lldpV2LocManAddr = _LldpV2LocManAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 2),
    _LldpV2LocManAddr_Type()
)
lldpV2LocManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2LocManAddr.setStatus("current")
_LldpV2LocManAddrLen_Type = Unsigned32
_LldpV2LocManAddrLen_Object = MibTableColumn
lldpV2LocManAddrLen = _LldpV2LocManAddrLen_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 3),
    _LldpV2LocManAddrLen_Type()
)
lldpV2LocManAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocManAddrLen.setStatus("current")
_LldpV2LocManAddrIfSubtype_Type = LldpV2ManAddrIfSubtype
_LldpV2LocManAddrIfSubtype_Object = MibTableColumn
lldpV2LocManAddrIfSubtype = _LldpV2LocManAddrIfSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 4),
    _LldpV2LocManAddrIfSubtype_Type()
)
lldpV2LocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocManAddrIfSubtype.setStatus("current")
_LldpV2LocManAddrIfId_Type = Unsigned32
_LldpV2LocManAddrIfId_Object = MibTableColumn
lldpV2LocManAddrIfId = _LldpV2LocManAddrIfId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 5),
    _LldpV2LocManAddrIfId_Type()
)
lldpV2LocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocManAddrIfId.setStatus("current")
_LldpV2LocManAddrOID_Type = ObjectIdentifier
_LldpV2LocManAddrOID_Object = MibTableColumn
lldpV2LocManAddrOID = _LldpV2LocManAddrOID_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 6),
    _LldpV2LocManAddrOID_Type()
)
lldpV2LocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocManAddrOID.setStatus("current")
_LldpV2RemoteSystemsData_ObjectIdentity = ObjectIdentity
lldpV2RemoteSystemsData = _LldpV2RemoteSystemsData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4)
)
_LldpV2RemTable_Object = MibTable
lldpV2RemTable = _LldpV2RemTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpV2RemTable.setStatus("current")
_LldpV2RemEntry_Object = MibTableRow
lldpV2RemEntry = _LldpV2RemEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1)
)
lldpV2RemEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2RemEntry.setStatus("current")
_LldpV2RemTimeMark_Type = TimeFilter
_LldpV2RemTimeMark_Object = MibTableColumn
lldpV2RemTimeMark = _LldpV2RemTimeMark_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 1),
    _LldpV2RemTimeMark_Type()
)
lldpV2RemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemTimeMark.setStatus("current")
_LldpV2RemLocalIfIndex_Type = InterfaceIndex
_LldpV2RemLocalIfIndex_Object = MibTableColumn
lldpV2RemLocalIfIndex = _LldpV2RemLocalIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 2),
    _LldpV2RemLocalIfIndex_Type()
)
lldpV2RemLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLocalIfIndex.setStatus("current")
_LldpV2RemLocalDestMACAddress_Type = LldpV2DestAddressTableIndex
_LldpV2RemLocalDestMACAddress_Object = MibTableColumn
lldpV2RemLocalDestMACAddress = _LldpV2RemLocalDestMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 3),
    _LldpV2RemLocalDestMACAddress_Type()
)
lldpV2RemLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemLocalDestMACAddress.setStatus("current")


class _LldpV2RemIndex_Type(Unsigned32):
    """Custom type lldpV2RemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemIndex_Type.__name__ = "Unsigned32"
_LldpV2RemIndex_Object = MibTableColumn
lldpV2RemIndex = _LldpV2RemIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 4),
    _LldpV2RemIndex_Type()
)
lldpV2RemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemIndex.setStatus("current")
_LldpV2RemChassisIdSubtype_Type = LldpV2ChassisIdSubtype
_LldpV2RemChassisIdSubtype_Object = MibTableColumn
lldpV2RemChassisIdSubtype = _LldpV2RemChassisIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 5),
    _LldpV2RemChassisIdSubtype_Type()
)
lldpV2RemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemChassisIdSubtype.setStatus("current")
_LldpV2RemChassisId_Type = LldpV2ChassisId
_LldpV2RemChassisId_Object = MibTableColumn
lldpV2RemChassisId = _LldpV2RemChassisId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 6),
    _LldpV2RemChassisId_Type()
)
lldpV2RemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemChassisId.setStatus("current")
_LldpV2RemPortIdSubtype_Type = LldpV2PortIdSubtype
_LldpV2RemPortIdSubtype_Object = MibTableColumn
lldpV2RemPortIdSubtype = _LldpV2RemPortIdSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 7),
    _LldpV2RemPortIdSubtype_Type()
)
lldpV2RemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemPortIdSubtype.setStatus("current")
_LldpV2RemPortId_Type = LldpV2PortId
_LldpV2RemPortId_Object = MibTableColumn
lldpV2RemPortId = _LldpV2RemPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 8),
    _LldpV2RemPortId_Type()
)
lldpV2RemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemPortId.setStatus("current")


class _LldpV2RemPortDesc_Type(SnmpAdminString):
    """Custom type lldpV2RemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2RemPortDesc_Type.__name__ = "SnmpAdminString"
_LldpV2RemPortDesc_Object = MibTableColumn
lldpV2RemPortDesc = _LldpV2RemPortDesc_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 9),
    _LldpV2RemPortDesc_Type()
)
lldpV2RemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemPortDesc.setStatus("current")


class _LldpV2RemSysName_Type(SnmpAdminString):
    """Custom type lldpV2RemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2RemSysName_Type.__name__ = "SnmpAdminString"
_LldpV2RemSysName_Object = MibTableColumn
lldpV2RemSysName = _LldpV2RemSysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 10),
    _LldpV2RemSysName_Type()
)
lldpV2RemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemSysName.setStatus("current")


class _LldpV2RemSysDesc_Type(SnmpAdminString):
    """Custom type lldpV2RemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2RemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpV2RemSysDesc_Object = MibTableColumn
lldpV2RemSysDesc = _LldpV2RemSysDesc_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 11),
    _LldpV2RemSysDesc_Type()
)
lldpV2RemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemSysDesc.setStatus("current")
_LldpV2RemSysCapSupported_Type = LldpV2SystemCapabilitiesMap
_LldpV2RemSysCapSupported_Object = MibTableColumn
lldpV2RemSysCapSupported = _LldpV2RemSysCapSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 12),
    _LldpV2RemSysCapSupported_Type()
)
lldpV2RemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemSysCapSupported.setStatus("current")
_LldpV2RemSysCapEnabled_Type = LldpV2SystemCapabilitiesMap
_LldpV2RemSysCapEnabled_Object = MibTableColumn
lldpV2RemSysCapEnabled = _LldpV2RemSysCapEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 13),
    _LldpV2RemSysCapEnabled_Type()
)
lldpV2RemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemSysCapEnabled.setStatus("current")
_LldpV2RemRemoteChanges_Type = TruthValue
_LldpV2RemRemoteChanges_Object = MibTableColumn
lldpV2RemRemoteChanges = _LldpV2RemRemoteChanges_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 14),
    _LldpV2RemRemoteChanges_Type()
)
lldpV2RemRemoteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemRemoteChanges.setStatus("current")
_LldpV2RemTooManyNeighbors_Type = TruthValue
_LldpV2RemTooManyNeighbors_Object = MibTableColumn
lldpV2RemTooManyNeighbors = _LldpV2RemTooManyNeighbors_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 15),
    _LldpV2RemTooManyNeighbors_Type()
)
lldpV2RemTooManyNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemTooManyNeighbors.setStatus("current")
_LldpV2RemManAddrTable_Object = MibTable
lldpV2RemManAddrTable = _LldpV2RemManAddrTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lldpV2RemManAddrTable.setStatus("current")
_LldpV2RemManAddrEntry_Object = MibTableRow
lldpV2RemManAddrEntry = _LldpV2RemManAddrEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1)
)
lldpV2RemManAddrEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemManAddrSubtype"),
    (0, "LLDP-V2-MIB", "lldpV2RemManAddr"),
)
if mibBuilder.loadTexts:
    lldpV2RemManAddrEntry.setStatus("current")
_LldpV2RemManAddrSubtype_Type = AddressFamilyNumbers
_LldpV2RemManAddrSubtype_Object = MibTableColumn
lldpV2RemManAddrSubtype = _LldpV2RemManAddrSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 1),
    _LldpV2RemManAddrSubtype_Type()
)
lldpV2RemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemManAddrSubtype.setStatus("current")
_LldpV2RemManAddr_Type = LldpV2ManAddress
_LldpV2RemManAddr_Object = MibTableColumn
lldpV2RemManAddr = _LldpV2RemManAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 2),
    _LldpV2RemManAddr_Type()
)
lldpV2RemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemManAddr.setStatus("current")
_LldpV2RemManAddrIfSubtype_Type = LldpV2ManAddrIfSubtype
_LldpV2RemManAddrIfSubtype_Object = MibTableColumn
lldpV2RemManAddrIfSubtype = _LldpV2RemManAddrIfSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 3),
    _LldpV2RemManAddrIfSubtype_Type()
)
lldpV2RemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemManAddrIfSubtype.setStatus("current")
_LldpV2RemManAddrIfId_Type = Unsigned32
_LldpV2RemManAddrIfId_Object = MibTableColumn
lldpV2RemManAddrIfId = _LldpV2RemManAddrIfId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 4),
    _LldpV2RemManAddrIfId_Type()
)
lldpV2RemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemManAddrIfId.setStatus("current")
_LldpV2RemManAddrOID_Type = ObjectIdentifier
_LldpV2RemManAddrOID_Object = MibTableColumn
lldpV2RemManAddrOID = _LldpV2RemManAddrOID_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 5),
    _LldpV2RemManAddrOID_Type()
)
lldpV2RemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemManAddrOID.setStatus("current")
_LldpV2RemUnknownTLVTable_Object = MibTable
lldpV2RemUnknownTLVTable = _LldpV2RemUnknownTLVTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lldpV2RemUnknownTLVTable.setStatus("current")
_LldpV2RemUnknownTLVEntry_Object = MibTableRow
lldpV2RemUnknownTLVEntry = _LldpV2RemUnknownTLVEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1)
)
lldpV2RemUnknownTLVEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemUnknownTLVType"),
)
if mibBuilder.loadTexts:
    lldpV2RemUnknownTLVEntry.setStatus("current")


class _LldpV2RemUnknownTLVType_Type(Unsigned32):
    """Custom type lldpV2RemUnknownTLVType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 126),
    )


_LldpV2RemUnknownTLVType_Type.__name__ = "Unsigned32"
_LldpV2RemUnknownTLVType_Object = MibTableColumn
lldpV2RemUnknownTLVType = _LldpV2RemUnknownTLVType_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1, 1),
    _LldpV2RemUnknownTLVType_Type()
)
lldpV2RemUnknownTLVType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemUnknownTLVType.setStatus("current")


class _LldpV2RemUnknownTLVInfo_Type(OctetString):
    """Custom type lldpV2RemUnknownTLVInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LldpV2RemUnknownTLVInfo_Type.__name__ = "OctetString"
_LldpV2RemUnknownTLVInfo_Object = MibTableColumn
lldpV2RemUnknownTLVInfo = _LldpV2RemUnknownTLVInfo_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1, 2),
    _LldpV2RemUnknownTLVInfo_Type()
)
lldpV2RemUnknownTLVInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemUnknownTLVInfo.setStatus("current")
_LldpV2RemOrgDefInfoTable_Object = MibTable
lldpV2RemOrgDefInfoTable = _LldpV2RemOrgDefInfoTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfoTable.setStatus("current")
_LldpV2RemOrgDefInfoEntry_Object = MibTableRow
lldpV2RemOrgDefInfoEntry = _LldpV2RemOrgDefInfoEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1)
)
lldpV2RemOrgDefInfoEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoOUI"),
    (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoSubtype"),
    (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoIndex"),
)
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfoEntry.setStatus("current")


class _LldpV2RemOrgDefInfoOUI_Type(OctetString):
    """Custom type lldpV2RemOrgDefInfoOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LldpV2RemOrgDefInfoOUI_Type.__name__ = "OctetString"
_LldpV2RemOrgDefInfoOUI_Object = MibTableColumn
lldpV2RemOrgDefInfoOUI = _LldpV2RemOrgDefInfoOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 1),
    _LldpV2RemOrgDefInfoOUI_Type()
)
lldpV2RemOrgDefInfoOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfoOUI.setStatus("current")


class _LldpV2RemOrgDefInfoSubtype_Type(Unsigned32):
    """Custom type lldpV2RemOrgDefInfoSubtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LldpV2RemOrgDefInfoSubtype_Type.__name__ = "Unsigned32"
_LldpV2RemOrgDefInfoSubtype_Object = MibTableColumn
lldpV2RemOrgDefInfoSubtype = _LldpV2RemOrgDefInfoSubtype_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 2),
    _LldpV2RemOrgDefInfoSubtype_Type()
)
lldpV2RemOrgDefInfoSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfoSubtype.setStatus("current")


class _LldpV2RemOrgDefInfoIndex_Type(Unsigned32):
    """Custom type lldpV2RemOrgDefInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemOrgDefInfoIndex_Type.__name__ = "Unsigned32"
_LldpV2RemOrgDefInfoIndex_Object = MibTableColumn
lldpV2RemOrgDefInfoIndex = _LldpV2RemOrgDefInfoIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 3),
    _LldpV2RemOrgDefInfoIndex_Type()
)
lldpV2RemOrgDefInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfoIndex.setStatus("current")


class _LldpV2RemOrgDefInfo_Type(OctetString):
    """Custom type lldpV2RemOrgDefInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 507),
    )


_LldpV2RemOrgDefInfo_Type.__name__ = "OctetString"
_LldpV2RemOrgDefInfo_Object = MibTableColumn
lldpV2RemOrgDefInfo = _LldpV2RemOrgDefInfo_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 4),
    _LldpV2RemOrgDefInfo_Type()
)
lldpV2RemOrgDefInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemOrgDefInfo.setStatus("current")
_LldpV2Extensions_ObjectIdentity = ObjectIdentity
lldpV2Extensions = _LldpV2Extensions_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5)
)
_LldpV2Conformance_ObjectIdentity = ObjectIdentity
lldpV2Conformance = _LldpV2Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 2)
)
_LldpV2Compliances_ObjectIdentity = ObjectIdentity
lldpV2Compliances = _LldpV2Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 1)
)
_LldpV2Groups_ObjectIdentity = ObjectIdentity
lldpV2Groups = _LldpV2Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2)
)

# Managed Objects groups

lldpV2ConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 1)
)
lldpV2ConfigGroup.setObjects(
    ("LLDP-V2-MIB", "lldpV2PortConfigAdminStatusV2")
)
if mibBuilder.loadTexts:
    lldpV2ConfigGroup.setStatus("current")

lldpV2ConfigRxGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 2)
)
lldpV2ConfigRxGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2NotificationInterval"),
        ("LLDP-V2-MIB", "lldpV2PortConfigNotificationEnableV2"))
)
if mibBuilder.loadTexts:
    lldpV2ConfigRxGroup.setStatus("current")

lldpV2ConfigTxGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 3)
)
lldpV2ConfigTxGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2MessageTxInterval"),
        ("LLDP-V2-MIB", "lldpV2MessageTxHoldMultiplier"),
        ("LLDP-V2-MIB", "lldpV2ReinitDelay"),
        ("LLDP-V2-MIB", "lldpV2PortConfigTLVsTxEnableV2"),
        ("LLDP-V2-MIB", "lldpV2ManAddrConfigTxEnable"),
        ("LLDP-V2-MIB", "lldpV2ManAddrConfigRowStatus"),
        ("LLDP-V2-MIB", "lldpV2TxCreditMax"),
        ("LLDP-V2-MIB", "lldpV2MessageFastTx"),
        ("LLDP-V2-MIB", "lldpV2TxFastInit"),
        ("LLDP-V2-MIB", "lldpV2DestMacAddress"),
        ("LLDP-V2-MIB", "lldpV2PortMessageTxInterval"),
        ("LLDP-V2-MIB", "lldpV2PortMessageTxHoldMultiplier"),
        ("LLDP-V2-MIB", "lldpV2PortReinitDelay"),
        ("LLDP-V2-MIB", "lldpV2PortNotificationInterval"),
        ("LLDP-V2-MIB", "lldpV2PortTxCreditMax"),
        ("LLDP-V2-MIB", "lldpV2PortMessageFastTx"),
        ("LLDP-V2-MIB", "lldpV2PortTxFastInit"))
)
if mibBuilder.loadTexts:
    lldpV2ConfigTxGroup.setStatus("current")

lldpV2StatsRxGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 4)
)
lldpV2StatsRxGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2StatsRemTablesLastChangeTime"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesInserts"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesDeletes"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesDrops"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesAgeouts"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesDiscardedTotal"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesErrors"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesTotal"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortTLVsDiscardedTotal"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortTLVsUnrecognizedTotal"),
        ("LLDP-V2-MIB", "lldpV2StatsRxPortAgeoutsTotal"))
)
if mibBuilder.loadTexts:
    lldpV2StatsRxGroup.setStatus("current")

lldpV2StatsTxGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 5)
)
lldpV2StatsTxGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2StatsTxPortFramesTotal"),
        ("LLDP-V2-MIB", "lldpV2StatsTxLLDPDULengthErrors"))
)
if mibBuilder.loadTexts:
    lldpV2StatsTxGroup.setStatus("current")

lldpV2LocSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 6)
)
lldpV2LocSysGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2LocChassisIdSubtype"),
        ("LLDP-V2-MIB", "lldpV2LocChassisId"),
        ("LLDP-V2-MIB", "lldpV2LocPortIdSubtype"),
        ("LLDP-V2-MIB", "lldpV2LocPortId"),
        ("LLDP-V2-MIB", "lldpV2LocPortDesc"),
        ("LLDP-V2-MIB", "lldpV2LocSysDesc"),
        ("LLDP-V2-MIB", "lldpV2LocSysName"),
        ("LLDP-V2-MIB", "lldpV2LocSysCapSupported"),
        ("LLDP-V2-MIB", "lldpV2LocSysCapEnabled"),
        ("LLDP-V2-MIB", "lldpV2LocManAddrLen"),
        ("LLDP-V2-MIB", "lldpV2LocManAddrIfSubtype"),
        ("LLDP-V2-MIB", "lldpV2LocManAddrIfId"),
        ("LLDP-V2-MIB", "lldpV2LocManAddrOID"))
)
if mibBuilder.loadTexts:
    lldpV2LocSysGroup.setStatus("current")

lldpV2RemSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 7)
)
lldpV2RemSysGroup.setObjects(
      *(("LLDP-V2-MIB", "lldpV2RemChassisIdSubtype"),
        ("LLDP-V2-MIB", "lldpV2RemChassisId"),
        ("LLDP-V2-MIB", "lldpV2RemPortIdSubtype"),
        ("LLDP-V2-MIB", "lldpV2RemPortId"),
        ("LLDP-V2-MIB", "lldpV2RemPortDesc"),
        ("LLDP-V2-MIB", "lldpV2RemSysName"),
        ("LLDP-V2-MIB", "lldpV2RemSysDesc"),
        ("LLDP-V2-MIB", "lldpV2RemSysCapSupported"),
        ("LLDP-V2-MIB", "lldpV2RemSysCapEnabled"),
        ("LLDP-V2-MIB", "lldpV2RemRemoteChanges"),
        ("LLDP-V2-MIB", "lldpV2RemTooManyNeighbors"),
        ("LLDP-V2-MIB", "lldpV2RemManAddrIfSubtype"),
        ("LLDP-V2-MIB", "lldpV2RemManAddrIfId"),
        ("LLDP-V2-MIB", "lldpV2RemManAddrOID"),
        ("LLDP-V2-MIB", "lldpV2RemUnknownTLVInfo"),
        ("LLDP-V2-MIB", "lldpV2RemOrgDefInfo"))
)
if mibBuilder.loadTexts:
    lldpV2RemSysGroup.setStatus("current")


# Notification objects

lldpV2RemTablesChange = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 13, 0, 0, 1)
)
lldpV2RemTablesChange.setObjects(
      *(("LLDP-V2-MIB", "lldpV2StatsRemTablesInserts"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesDeletes"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesDrops"),
        ("LLDP-V2-MIB", "lldpV2StatsRemTablesAgeouts"))
)
if mibBuilder.loadTexts:
    lldpV2RemTablesChange.setStatus(
        "current"
    )


# Notifications groups

lldpV2NotificationsGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 8)
)
lldpV2NotificationsGroup.setObjects(
    ("LLDP-V2-MIB", "lldpV2RemTablesChange")
)
if mibBuilder.loadTexts:
    lldpV2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lldpV2TxRxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2TxRxCompliance.setStatus(
        "current"
    )

lldpV2TxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lldpV2TxCompliance.setStatus(
        "current"
    )

lldpV2RxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lldpV2RxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-V2-MIB",
    **{"lldpV2MIB": lldpV2MIB,
       "lldpV2Notifications": lldpV2Notifications,
       "lldpV2NotificationPrefix": lldpV2NotificationPrefix,
       "lldpV2RemTablesChange": lldpV2RemTablesChange,
       "lldpV2Objects": lldpV2Objects,
       "lldpV2Configuration": lldpV2Configuration,
       "lldpV2MessageTxInterval": lldpV2MessageTxInterval,
       "lldpV2MessageTxHoldMultiplier": lldpV2MessageTxHoldMultiplier,
       "lldpV2ReinitDelay": lldpV2ReinitDelay,
       "lldpV2NotificationInterval": lldpV2NotificationInterval,
       "lldpV2TxCreditMax": lldpV2TxCreditMax,
       "lldpV2MessageFastTx": lldpV2MessageFastTx,
       "lldpV2TxFastInit": lldpV2TxFastInit,
       "lldpV2PortConfigTable": lldpV2PortConfigTable,
       "lldpV2PortConfigEntry": lldpV2PortConfigEntry,
       "lldpV2PortConfigIfIndex": lldpV2PortConfigIfIndex,
       "lldpV2PortConfigDestAddressIndex": lldpV2PortConfigDestAddressIndex,
       "lldpV2PortConfigAdminStatus": lldpV2PortConfigAdminStatus,
       "lldpV2PortConfigNotificationEnable": lldpV2PortConfigNotificationEnable,
       "lldpV2PortConfigTLVsTxEnable": lldpV2PortConfigTLVsTxEnable,
       "lldpV2DestAddressTable": lldpV2DestAddressTable,
       "lldpV2DestAddressTableEntry": lldpV2DestAddressTableEntry,
       "lldpV2AddressTableIndex": lldpV2AddressTableIndex,
       "lldpV2DestMacAddress": lldpV2DestMacAddress,
       "lldpV2ManAddrConfigTxPortsTable": lldpV2ManAddrConfigTxPortsTable,
       "lldpV2ManAddrConfigTxPortsEntry": lldpV2ManAddrConfigTxPortsEntry,
       "lldpV2ManAddrConfigIfIndex": lldpV2ManAddrConfigIfIndex,
       "lldpV2ManAddrConfigDestAddressIndex": lldpV2ManAddrConfigDestAddressIndex,
       "lldpV2ManAddrConfigLocManAddrSubtype": lldpV2ManAddrConfigLocManAddrSubtype,
       "lldpV2ManAddrConfigLocManAddr": lldpV2ManAddrConfigLocManAddr,
       "lldpV2ManAddrConfigTxEnable": lldpV2ManAddrConfigTxEnable,
       "lldpV2ManAddrConfigRowStatus": lldpV2ManAddrConfigRowStatus,
       "lldpV2PortConfigTableV2": lldpV2PortConfigTableV2,
       "lldpV2PortConfigEntryV2": lldpV2PortConfigEntryV2,
       "lldpV2PortConfigIfIndexV2": lldpV2PortConfigIfIndexV2,
       "lldpV2PortConfigDestAddressIndexV2": lldpV2PortConfigDestAddressIndexV2,
       "lldpV2PortConfigAdminStatusV2": lldpV2PortConfigAdminStatusV2,
       "lldpV2PortMessageTxInterval": lldpV2PortMessageTxInterval,
       "lldpV2PortMessageTxHoldMultiplier": lldpV2PortMessageTxHoldMultiplier,
       "lldpV2PortReinitDelay": lldpV2PortReinitDelay,
       "lldpV2PortNotificationInterval": lldpV2PortNotificationInterval,
       "lldpV2PortTxCreditMax": lldpV2PortTxCreditMax,
       "lldpV2PortMessageFastTx": lldpV2PortMessageFastTx,
       "lldpV2PortTxFastInit": lldpV2PortTxFastInit,
       "lldpV2PortConfigNotificationEnableV2": lldpV2PortConfigNotificationEnableV2,
       "lldpV2PortConfigTLVsTxEnableV2": lldpV2PortConfigTLVsTxEnableV2,
       "lldpV2Statistics": lldpV2Statistics,
       "lldpV2StatsRemTablesLastChangeTime": lldpV2StatsRemTablesLastChangeTime,
       "lldpV2StatsRemTablesInserts": lldpV2StatsRemTablesInserts,
       "lldpV2StatsRemTablesDeletes": lldpV2StatsRemTablesDeletes,
       "lldpV2StatsRemTablesDrops": lldpV2StatsRemTablesDrops,
       "lldpV2StatsRemTablesAgeouts": lldpV2StatsRemTablesAgeouts,
       "lldpV2StatsTxPortTable": lldpV2StatsTxPortTable,
       "lldpV2StatsTxPortEntry": lldpV2StatsTxPortEntry,
       "lldpV2StatsTxIfIndex": lldpV2StatsTxIfIndex,
       "lldpV2StatsTxDestMACAddress": lldpV2StatsTxDestMACAddress,
       "lldpV2StatsTxPortFramesTotal": lldpV2StatsTxPortFramesTotal,
       "lldpV2StatsTxLLDPDULengthErrors": lldpV2StatsTxLLDPDULengthErrors,
       "lldpV2StatsRxPortTable": lldpV2StatsRxPortTable,
       "lldpV2StatsRxPortEntry": lldpV2StatsRxPortEntry,
       "lldpV2StatsRxDestIfIndex": lldpV2StatsRxDestIfIndex,
       "lldpV2StatsRxDestMACAddress": lldpV2StatsRxDestMACAddress,
       "lldpV2StatsRxPortFramesDiscardedTotal": lldpV2StatsRxPortFramesDiscardedTotal,
       "lldpV2StatsRxPortFramesErrors": lldpV2StatsRxPortFramesErrors,
       "lldpV2StatsRxPortFramesTotal": lldpV2StatsRxPortFramesTotal,
       "lldpV2StatsRxPortTLVsDiscardedTotal": lldpV2StatsRxPortTLVsDiscardedTotal,
       "lldpV2StatsRxPortTLVsUnrecognizedTotal": lldpV2StatsRxPortTLVsUnrecognizedTotal,
       "lldpV2StatsRxPortAgeoutsTotal": lldpV2StatsRxPortAgeoutsTotal,
       "lldpV2LocalSystemData": lldpV2LocalSystemData,
       "lldpV2LocChassisIdSubtype": lldpV2LocChassisIdSubtype,
       "lldpV2LocChassisId": lldpV2LocChassisId,
       "lldpV2LocSysName": lldpV2LocSysName,
       "lldpV2LocSysDesc": lldpV2LocSysDesc,
       "lldpV2LocSysCapSupported": lldpV2LocSysCapSupported,
       "lldpV2LocSysCapEnabled": lldpV2LocSysCapEnabled,
       "lldpV2LocPortTable": lldpV2LocPortTable,
       "lldpV2LocPortEntry": lldpV2LocPortEntry,
       "lldpV2LocPortIfIndex": lldpV2LocPortIfIndex,
       "lldpV2LocPortIdSubtype": lldpV2LocPortIdSubtype,
       "lldpV2LocPortId": lldpV2LocPortId,
       "lldpV2LocPortDesc": lldpV2LocPortDesc,
       "lldpV2LocManAddrTable": lldpV2LocManAddrTable,
       "lldpV2LocManAddrEntry": lldpV2LocManAddrEntry,
       "lldpV2LocManAddrSubtype": lldpV2LocManAddrSubtype,
       "lldpV2LocManAddr": lldpV2LocManAddr,
       "lldpV2LocManAddrLen": lldpV2LocManAddrLen,
       "lldpV2LocManAddrIfSubtype": lldpV2LocManAddrIfSubtype,
       "lldpV2LocManAddrIfId": lldpV2LocManAddrIfId,
       "lldpV2LocManAddrOID": lldpV2LocManAddrOID,
       "lldpV2RemoteSystemsData": lldpV2RemoteSystemsData,
       "lldpV2RemTable": lldpV2RemTable,
       "lldpV2RemEntry": lldpV2RemEntry,
       "lldpV2RemTimeMark": lldpV2RemTimeMark,
       "lldpV2RemLocalIfIndex": lldpV2RemLocalIfIndex,
       "lldpV2RemLocalDestMACAddress": lldpV2RemLocalDestMACAddress,
       "lldpV2RemIndex": lldpV2RemIndex,
       "lldpV2RemChassisIdSubtype": lldpV2RemChassisIdSubtype,
       "lldpV2RemChassisId": lldpV2RemChassisId,
       "lldpV2RemPortIdSubtype": lldpV2RemPortIdSubtype,
       "lldpV2RemPortId": lldpV2RemPortId,
       "lldpV2RemPortDesc": lldpV2RemPortDesc,
       "lldpV2RemSysName": lldpV2RemSysName,
       "lldpV2RemSysDesc": lldpV2RemSysDesc,
       "lldpV2RemSysCapSupported": lldpV2RemSysCapSupported,
       "lldpV2RemSysCapEnabled": lldpV2RemSysCapEnabled,
       "lldpV2RemRemoteChanges": lldpV2RemRemoteChanges,
       "lldpV2RemTooManyNeighbors": lldpV2RemTooManyNeighbors,
       "lldpV2RemManAddrTable": lldpV2RemManAddrTable,
       "lldpV2RemManAddrEntry": lldpV2RemManAddrEntry,
       "lldpV2RemManAddrSubtype": lldpV2RemManAddrSubtype,
       "lldpV2RemManAddr": lldpV2RemManAddr,
       "lldpV2RemManAddrIfSubtype": lldpV2RemManAddrIfSubtype,
       "lldpV2RemManAddrIfId": lldpV2RemManAddrIfId,
       "lldpV2RemManAddrOID": lldpV2RemManAddrOID,
       "lldpV2RemUnknownTLVTable": lldpV2RemUnknownTLVTable,
       "lldpV2RemUnknownTLVEntry": lldpV2RemUnknownTLVEntry,
       "lldpV2RemUnknownTLVType": lldpV2RemUnknownTLVType,
       "lldpV2RemUnknownTLVInfo": lldpV2RemUnknownTLVInfo,
       "lldpV2RemOrgDefInfoTable": lldpV2RemOrgDefInfoTable,
       "lldpV2RemOrgDefInfoEntry": lldpV2RemOrgDefInfoEntry,
       "lldpV2RemOrgDefInfoOUI": lldpV2RemOrgDefInfoOUI,
       "lldpV2RemOrgDefInfoSubtype": lldpV2RemOrgDefInfoSubtype,
       "lldpV2RemOrgDefInfoIndex": lldpV2RemOrgDefInfoIndex,
       "lldpV2RemOrgDefInfo": lldpV2RemOrgDefInfo,
       "lldpV2Extensions": lldpV2Extensions,
       "lldpV2Conformance": lldpV2Conformance,
       "lldpV2Compliances": lldpV2Compliances,
       "lldpV2TxRxCompliance": lldpV2TxRxCompliance,
       "lldpV2TxCompliance": lldpV2TxCompliance,
       "lldpV2RxCompliance": lldpV2RxCompliance,
       "lldpV2Groups": lldpV2Groups,
       "lldpV2ConfigGroup": lldpV2ConfigGroup,
       "lldpV2ConfigRxGroup": lldpV2ConfigRxGroup,
       "lldpV2ConfigTxGroup": lldpV2ConfigTxGroup,
       "lldpV2StatsRxGroup": lldpV2StatsRxGroup,
       "lldpV2StatsTxGroup": lldpV2StatsTxGroup,
       "lldpV2LocSysGroup": lldpV2LocSysGroup,
       "lldpV2RemSysGroup": lldpV2RemSysGroup,
       "lldpV2NotificationsGroup": lldpV2NotificationsGroup}
)
