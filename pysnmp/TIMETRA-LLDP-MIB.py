# SNMP MIB module (TIMETRA-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:48 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpManAddrIfSubtype,
 LldpManAddress,
 LldpPortId,
 LldpPortIdSubtype,
 LldpSystemCapabilitiesMap,
 lldpLocManAddr,
 lldpLocManAddrSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpManAddrIfSubtype",
    "LldpManAddress",
    "LldpPortId",
    "LldpPortIdSubtype",
    "LldpSystemCapabilitiesMap",
    "lldpLocManAddr",
    "lldpLocManAddrSubtype")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxEnabledDisabled,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxEnabledDisabled")


# MODULE-IDENTITY

tmnxLldpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 59)
)
tmnxLldpMIBModule.setRevisions(
        ("1909-02-28 00:00",
         "1902-02-02 02:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLldpDestAddressTableIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxLldpManAddressIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("system", 1)
    )



# MIB Managed Objects in the order of their OIDs

_TmnxLldpConformance_ObjectIdentity = ObjectIdentity
tmnxLldpConformance = _TmnxLldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59)
)
_TmnxLldpCompliances_ObjectIdentity = ObjectIdentity
tmnxLldpCompliances = _TmnxLldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 1)
)
_TmnxLldpGroups_ObjectIdentity = ObjectIdentity
tmnxLldpGroups = _TmnxLldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2)
)
_TmnxLldpObjects_ObjectIdentity = ObjectIdentity
tmnxLldpObjects = _TmnxLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59)
)
_TmnxLldpConfiguration_ObjectIdentity = ObjectIdentity
tmnxLldpConfiguration = _TmnxLldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1)
)


class _TmnxLldpTxCreditMax_Type(Integer32):
    """Custom type tmnxLldpTxCreditMax based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxLldpTxCreditMax_Type.__name__ = "Integer32"
_TmnxLldpTxCreditMax_Object = MibScalar
tmnxLldpTxCreditMax = _TmnxLldpTxCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 1),
    _TmnxLldpTxCreditMax_Type()
)
tmnxLldpTxCreditMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpTxCreditMax.setStatus("current")


class _TmnxLldpMessageFastTx_Type(Integer32):
    """Custom type tmnxLldpMessageFastTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxLldpMessageFastTx_Type.__name__ = "Integer32"
_TmnxLldpMessageFastTx_Object = MibScalar
tmnxLldpMessageFastTx = _TmnxLldpMessageFastTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 2),
    _TmnxLldpMessageFastTx_Type()
)
tmnxLldpMessageFastTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpMessageFastTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLldpMessageFastTx.setUnits("seconds")


class _TmnxLldpMessageFastTxInit_Type(Integer32):
    """Custom type tmnxLldpMessageFastTxInit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxLldpMessageFastTxInit_Type.__name__ = "Integer32"
_TmnxLldpMessageFastTxInit_Object = MibScalar
tmnxLldpMessageFastTxInit = _TmnxLldpMessageFastTxInit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 3),
    _TmnxLldpMessageFastTxInit_Type()
)
tmnxLldpMessageFastTxInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpMessageFastTxInit.setStatus("current")
_TmnxLldpAdminStatus_Type = TmnxEnabledDisabled
_TmnxLldpAdminStatus_Object = MibScalar
tmnxLldpAdminStatus = _TmnxLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 4),
    _TmnxLldpAdminStatus_Type()
)
tmnxLldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpAdminStatus.setStatus("current")
_TmnxLldpPortConfigTable_Object = MibTable
tmnxLldpPortConfigTable = _TmnxLldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxLldpPortConfigTable.setStatus("current")
_TmnxLldpPortConfigEntry_Object = MibTableRow
tmnxLldpPortConfigEntry = _TmnxLldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5, 1)
)
tmnxLldpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpPortCfgDestAddressIndex"),
)
if mibBuilder.loadTexts:
    tmnxLldpPortConfigEntry.setStatus("current")
_TmnxLldpPortCfgDestAddressIndex_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpPortCfgDestAddressIndex_Object = MibTableColumn
tmnxLldpPortCfgDestAddressIndex = _TmnxLldpPortCfgDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5, 1, 1),
    _TmnxLldpPortCfgDestAddressIndex_Type()
)
tmnxLldpPortCfgDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgDestAddressIndex.setStatus("current")


class _TmnxLldpPortCfgAdminStatus_Type(Integer32):
    """Custom type tmnxLldpPortCfgAdminStatus based on Integer32"""
    defaultValue = 4

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


_TmnxLldpPortCfgAdminStatus_Type.__name__ = "Integer32"
_TmnxLldpPortCfgAdminStatus_Object = MibTableColumn
tmnxLldpPortCfgAdminStatus = _TmnxLldpPortCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5, 1, 2),
    _TmnxLldpPortCfgAdminStatus_Type()
)
tmnxLldpPortCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgAdminStatus.setStatus("current")


class _TmnxLldpPortCfgNotifyEnable_Type(TruthValue):
    """Custom type tmnxLldpPortCfgNotifyEnable based on TruthValue"""


_TmnxLldpPortCfgNotifyEnable_Object = MibTableColumn
tmnxLldpPortCfgNotifyEnable = _TmnxLldpPortCfgNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5, 1, 3),
    _TmnxLldpPortCfgNotifyEnable_Type()
)
tmnxLldpPortCfgNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgNotifyEnable.setStatus("current")


class _TmnxLldpPortCfgTLVsTxEnable_Type(Bits):
    """Custom type tmnxLldpPortCfgTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_TmnxLldpPortCfgTLVsTxEnable_Type.__name__ = "Bits"
_TmnxLldpPortCfgTLVsTxEnable_Object = MibTableColumn
tmnxLldpPortCfgTLVsTxEnable = _TmnxLldpPortCfgTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 5, 1, 4),
    _TmnxLldpPortCfgTLVsTxEnable_Type()
)
tmnxLldpPortCfgTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgTLVsTxEnable.setStatus("current")
_TmnxLldpConfigManAddrPortsTable_Object = MibTable
tmnxLldpConfigManAddrPortsTable = _TmnxLldpConfigManAddrPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxLldpConfigManAddrPortsTable.setStatus("current")
_TmnxLldpConfigManAddrPortsEntry_Object = MibTableRow
tmnxLldpConfigManAddrPortsEntry = _TmnxLldpConfigManAddrPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6, 1)
)
tmnxLldpConfigManAddrPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpPortCfgDestAddressIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpPortCfgAddressIndex"),
)
if mibBuilder.loadTexts:
    tmnxLldpConfigManAddrPortsEntry.setStatus("current")
_TmnxLldpPortCfgAddressIndex_Type = TmnxLldpManAddressIndex
_TmnxLldpPortCfgAddressIndex_Object = MibTableColumn
tmnxLldpPortCfgAddressIndex = _TmnxLldpPortCfgAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6, 1, 1),
    _TmnxLldpPortCfgAddressIndex_Type()
)
tmnxLldpPortCfgAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgAddressIndex.setStatus("current")


class _TmnxLldpPortCfgManAddrTxEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxLldpPortCfgManAddrTxEnabled based on TmnxEnabledDisabled"""


_TmnxLldpPortCfgManAddrTxEnabled_Object = MibTableColumn
tmnxLldpPortCfgManAddrTxEnabled = _TmnxLldpPortCfgManAddrTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6, 1, 2),
    _TmnxLldpPortCfgManAddrTxEnabled_Type()
)
tmnxLldpPortCfgManAddrTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgManAddrTxEnabled.setStatus("current")
_TmnxLldpPortCfgManAddrSubtype_Type = AddressFamilyNumbers
_TmnxLldpPortCfgManAddrSubtype_Object = MibTableColumn
tmnxLldpPortCfgManAddrSubtype = _TmnxLldpPortCfgManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6, 1, 3),
    _TmnxLldpPortCfgManAddrSubtype_Type()
)
tmnxLldpPortCfgManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgManAddrSubtype.setStatus("current")
_TmnxLldpPortCfgManAddress_Type = LldpManAddress
_TmnxLldpPortCfgManAddress_Object = MibTableColumn
tmnxLldpPortCfgManAddress = _TmnxLldpPortCfgManAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 6, 1, 4),
    _TmnxLldpPortCfgManAddress_Type()
)
tmnxLldpPortCfgManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpPortCfgManAddress.setStatus("current")
_TmnxLldpDestAddressTable_Object = MibTable
tmnxLldpDestAddressTable = _TmnxLldpDestAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxLldpDestAddressTable.setStatus("current")
_TmnxLldpDestAddressTableEntry_Object = MibTableRow
tmnxLldpDestAddressTableEntry = _TmnxLldpDestAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 7, 1)
)
tmnxLldpDestAddressTableEntry.setIndexNames(
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpAddressTableIndex"),
)
if mibBuilder.loadTexts:
    tmnxLldpDestAddressTableEntry.setStatus("current")
_TmnxLldpAddressTableIndex_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpAddressTableIndex_Object = MibTableColumn
tmnxLldpAddressTableIndex = _TmnxLldpAddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 7, 1, 1),
    _TmnxLldpAddressTableIndex_Type()
)
tmnxLldpAddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpAddressTableIndex.setStatus("current")
_TmnxLldpDestMacAddress_Type = MacAddress
_TmnxLldpDestMacAddress_Object = MibTableColumn
tmnxLldpDestMacAddress = _TmnxLldpDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 1, 7, 1, 2),
    _TmnxLldpDestMacAddress_Type()
)
tmnxLldpDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpDestMacAddress.setStatus("current")
_TmnxLldpStatistics_ObjectIdentity = ObjectIdentity
tmnxLldpStatistics = _TmnxLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2)
)
_TmnxLldpStatsTxPortTable_Object = MibTable
tmnxLldpStatsTxPortTable = _TmnxLldpStatsTxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxLldpStatsTxPortTable.setStatus("current")
_TmnxLldpStatsTxPortEntry_Object = MibTableRow
tmnxLldpStatsTxPortEntry = _TmnxLldpStatsTxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 1, 1)
)
tmnxLldpStatsTxPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpStatsTxDestMACAddress"),
)
if mibBuilder.loadTexts:
    tmnxLldpStatsTxPortEntry.setStatus("current")
_TmnxLldpStatsTxDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpStatsTxDestMACAddress_Object = MibTableColumn
tmnxLldpStatsTxDestMACAddress = _TmnxLldpStatsTxDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 1, 1, 1),
    _TmnxLldpStatsTxDestMACAddress_Type()
)
tmnxLldpStatsTxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpStatsTxDestMACAddress.setStatus("current")
_TmnxLldpStatsTxPortFrames_Type = Counter32
_TmnxLldpStatsTxPortFrames_Object = MibTableColumn
tmnxLldpStatsTxPortFrames = _TmnxLldpStatsTxPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 1, 1, 2),
    _TmnxLldpStatsTxPortFrames_Type()
)
tmnxLldpStatsTxPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsTxPortFrames.setStatus("current")
_TmnxLldpStatsTxLLDPDULengthErrs_Type = Counter32
_TmnxLldpStatsTxLLDPDULengthErrs_Object = MibTableColumn
tmnxLldpStatsTxLLDPDULengthErrs = _TmnxLldpStatsTxLLDPDULengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 1, 1, 3),
    _TmnxLldpStatsTxLLDPDULengthErrs_Type()
)
tmnxLldpStatsTxLLDPDULengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsTxLLDPDULengthErrs.setStatus("current")
_TmnxLldpStatsRxPortTable_Object = MibTable
tmnxLldpStatsRxPortTable = _TmnxLldpStatsRxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortTable.setStatus("current")
_TmnxLldpStatsRxPortEntry_Object = MibTableRow
tmnxLldpStatsRxPortEntry = _TmnxLldpStatsRxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1)
)
tmnxLldpStatsRxPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpStatsRxDestMACAddress"),
)
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortEntry.setStatus("current")
_TmnxLldpStatsRxDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpStatsRxDestMACAddress_Object = MibTableColumn
tmnxLldpStatsRxDestMACAddress = _TmnxLldpStatsRxDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 1),
    _TmnxLldpStatsRxDestMACAddress_Type()
)
tmnxLldpStatsRxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxDestMACAddress.setStatus("current")
_TmnxLldpStatsRxPortFrameDiscard_Type = Counter32
_TmnxLldpStatsRxPortFrameDiscard_Object = MibTableColumn
tmnxLldpStatsRxPortFrameDiscard = _TmnxLldpStatsRxPortFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 2),
    _TmnxLldpStatsRxPortFrameDiscard_Type()
)
tmnxLldpStatsRxPortFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortFrameDiscard.setStatus("current")
_TmnxLldpStatsRxPortFrameErrs_Type = Counter32
_TmnxLldpStatsRxPortFrameErrs_Object = MibTableColumn
tmnxLldpStatsRxPortFrameErrs = _TmnxLldpStatsRxPortFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 3),
    _TmnxLldpStatsRxPortFrameErrs_Type()
)
tmnxLldpStatsRxPortFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortFrameErrs.setStatus("current")
_TmnxLldpStatsRxPortFrames_Type = Counter32
_TmnxLldpStatsRxPortFrames_Object = MibTableColumn
tmnxLldpStatsRxPortFrames = _TmnxLldpStatsRxPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 4),
    _TmnxLldpStatsRxPortFrames_Type()
)
tmnxLldpStatsRxPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortFrames.setStatus("current")
_TmnxLldpStatsRxPortTLVDiscard_Type = Counter32
_TmnxLldpStatsRxPortTLVDiscard_Object = MibTableColumn
tmnxLldpStatsRxPortTLVDiscard = _TmnxLldpStatsRxPortTLVDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 5),
    _TmnxLldpStatsRxPortTLVDiscard_Type()
)
tmnxLldpStatsRxPortTLVDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortTLVDiscard.setStatus("current")
_TmnxLldpStatsRxPortTLVUnknown_Type = Counter32
_TmnxLldpStatsRxPortTLVUnknown_Object = MibTableColumn
tmnxLldpStatsRxPortTLVUnknown = _TmnxLldpStatsRxPortTLVUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 6),
    _TmnxLldpStatsRxPortTLVUnknown_Type()
)
tmnxLldpStatsRxPortTLVUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortTLVUnknown.setStatus("current")
_TmnxLldpStatsRxPortAgeouts_Type = ZeroBasedCounter32
_TmnxLldpStatsRxPortAgeouts_Object = MibTableColumn
tmnxLldpStatsRxPortAgeouts = _TmnxLldpStatsRxPortAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 2, 2, 1, 7),
    _TmnxLldpStatsRxPortAgeouts_Type()
)
tmnxLldpStatsRxPortAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpStatsRxPortAgeouts.setStatus("current")
_TmnxLldpLocalSystemData_ObjectIdentity = ObjectIdentity
tmnxLldpLocalSystemData = _TmnxLldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3)
)
_TmnxLldpLocPortTable_Object = MibTable
tmnxLldpLocPortTable = _TmnxLldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxLldpLocPortTable.setStatus("current")
_TmnxLldpLocPortEntry_Object = MibTableRow
tmnxLldpLocPortEntry = _TmnxLldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1, 1)
)
tmnxLldpLocPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpLocPortDestMACAddress"),
)
if mibBuilder.loadTexts:
    tmnxLldpLocPortEntry.setStatus("current")
_TmnxLldpLocPortDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpLocPortDestMACAddress_Object = MibTableColumn
tmnxLldpLocPortDestMACAddress = _TmnxLldpLocPortDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1, 1, 1),
    _TmnxLldpLocPortDestMACAddress_Type()
)
tmnxLldpLocPortDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpLocPortDestMACAddress.setStatus("current")
_TmnxLldpLocPortIdSubtype_Type = LldpPortIdSubtype
_TmnxLldpLocPortIdSubtype_Object = MibTableColumn
tmnxLldpLocPortIdSubtype = _TmnxLldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1, 1, 2),
    _TmnxLldpLocPortIdSubtype_Type()
)
tmnxLldpLocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpLocPortIdSubtype.setStatus("current")
_TmnxLldpLocPortId_Type = LldpPortId
_TmnxLldpLocPortId_Object = MibTableColumn
tmnxLldpLocPortId = _TmnxLldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1, 1, 3),
    _TmnxLldpLocPortId_Type()
)
tmnxLldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpLocPortId.setStatus("current")


class _TmnxLldpLocPortDesc_Type(SnmpAdminString):
    """Custom type tmnxLldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_TmnxLldpLocPortDesc_Object = MibTableColumn
tmnxLldpLocPortDesc = _TmnxLldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 3, 1, 1, 4),
    _TmnxLldpLocPortDesc_Type()
)
tmnxLldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpLocPortDesc.setStatus("current")
_TmnxLldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
tmnxLldpRemoteSystemsData = _TmnxLldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4)
)
_TmnxLldpRemTable_Object = MibTable
tmnxLldpRemTable = _TmnxLldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxLldpRemTable.setStatus("current")
_TmnxLldpRemEntry_Object = MibTableRow
tmnxLldpRemEntry = _TmnxLldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1)
)
tmnxLldpRemEntry.setIndexNames(
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemTimeMark"),
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemLocalDestMACAddress"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemIndex"),
)
if mibBuilder.loadTexts:
    tmnxLldpRemEntry.setStatus("current")
_TmnxLldpRemTimeMark_Type = TimeFilter
_TmnxLldpRemTimeMark_Object = MibTableColumn
tmnxLldpRemTimeMark = _TmnxLldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 1),
    _TmnxLldpRemTimeMark_Type()
)
tmnxLldpRemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpRemTimeMark.setStatus("current")
_TmnxLldpRemLocalDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TmnxLldpRemLocalDestMACAddress_Object = MibTableColumn
tmnxLldpRemLocalDestMACAddress = _TmnxLldpRemLocalDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 2),
    _TmnxLldpRemLocalDestMACAddress_Type()
)
tmnxLldpRemLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpRemLocalDestMACAddress.setStatus("current")


class _TmnxLldpRemIndex_Type(Integer32):
    """Custom type tmnxLldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxLldpRemIndex_Type.__name__ = "Integer32"
_TmnxLldpRemIndex_Object = MibTableColumn
tmnxLldpRemIndex = _TmnxLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 3),
    _TmnxLldpRemIndex_Type()
)
tmnxLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpRemIndex.setStatus("current")
_TmnxLldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_TmnxLldpRemChassisIdSubtype_Object = MibTableColumn
tmnxLldpRemChassisIdSubtype = _TmnxLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 4),
    _TmnxLldpRemChassisIdSubtype_Type()
)
tmnxLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemChassisIdSubtype.setStatus("current")
_TmnxLldpRemChassisId_Type = LldpChassisId
_TmnxLldpRemChassisId_Object = MibTableColumn
tmnxLldpRemChassisId = _TmnxLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 5),
    _TmnxLldpRemChassisId_Type()
)
tmnxLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemChassisId.setStatus("current")
_TmnxLldpRemPortIdSubtype_Type = LldpPortIdSubtype
_TmnxLldpRemPortIdSubtype_Object = MibTableColumn
tmnxLldpRemPortIdSubtype = _TmnxLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 6),
    _TmnxLldpRemPortIdSubtype_Type()
)
tmnxLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemPortIdSubtype.setStatus("current")
_TmnxLldpRemPortId_Type = LldpPortId
_TmnxLldpRemPortId_Object = MibTableColumn
tmnxLldpRemPortId = _TmnxLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 7),
    _TmnxLldpRemPortId_Type()
)
tmnxLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemPortId.setStatus("current")


class _TmnxLldpRemPortDesc_Type(SnmpAdminString):
    """Custom type tmnxLldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_TmnxLldpRemPortDesc_Object = MibTableColumn
tmnxLldpRemPortDesc = _TmnxLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 8),
    _TmnxLldpRemPortDesc_Type()
)
tmnxLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemPortDesc.setStatus("current")


class _TmnxLldpRemSysName_Type(SnmpAdminString):
    """Custom type tmnxLldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLldpRemSysName_Type.__name__ = "SnmpAdminString"
_TmnxLldpRemSysName_Object = MibTableColumn
tmnxLldpRemSysName = _TmnxLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 9),
    _TmnxLldpRemSysName_Type()
)
tmnxLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemSysName.setStatus("current")


class _TmnxLldpRemSysDesc_Type(SnmpAdminString):
    """Custom type tmnxLldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_TmnxLldpRemSysDesc_Object = MibTableColumn
tmnxLldpRemSysDesc = _TmnxLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 10),
    _TmnxLldpRemSysDesc_Type()
)
tmnxLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemSysDesc.setStatus("current")
_TmnxLldpRemSysCapSupported_Type = LldpSystemCapabilitiesMap
_TmnxLldpRemSysCapSupported_Object = MibTableColumn
tmnxLldpRemSysCapSupported = _TmnxLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 11),
    _TmnxLldpRemSysCapSupported_Type()
)
tmnxLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemSysCapSupported.setStatus("current")
_TmnxLldpRemSysCapEnabled_Type = LldpSystemCapabilitiesMap
_TmnxLldpRemSysCapEnabled_Object = MibTableColumn
tmnxLldpRemSysCapEnabled = _TmnxLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 1, 1, 12),
    _TmnxLldpRemSysCapEnabled_Type()
)
tmnxLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemSysCapEnabled.setStatus("current")
_TmnxLldpRemManAddrTable_Object = MibTable
tmnxLldpRemManAddrTable = _TmnxLldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrTable.setStatus("current")
_TmnxLldpRemManAddrEntry_Object = MibTableRow
tmnxLldpRemManAddrEntry = _TmnxLldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1)
)
tmnxLldpRemManAddrEntry.setIndexNames(
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemTimeMark"),
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemLocalDestMACAddress"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemIndex"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemManAddrSubtype"),
    (0, "TIMETRA-LLDP-MIB", "tmnxLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrEntry.setStatus("current")
_TmnxLldpRemManAddrSubtype_Type = AddressFamilyNumbers
_TmnxLldpRemManAddrSubtype_Object = MibTableColumn
tmnxLldpRemManAddrSubtype = _TmnxLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1, 1),
    _TmnxLldpRemManAddrSubtype_Type()
)
tmnxLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrSubtype.setStatus("current")
_TmnxLldpRemManAddr_Type = LldpManAddress
_TmnxLldpRemManAddr_Object = MibTableColumn
tmnxLldpRemManAddr = _TmnxLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1, 2),
    _TmnxLldpRemManAddr_Type()
)
tmnxLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLldpRemManAddr.setStatus("current")
_TmnxLldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_TmnxLldpRemManAddrIfSubtype_Object = MibTableColumn
tmnxLldpRemManAddrIfSubtype = _TmnxLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1, 3),
    _TmnxLldpRemManAddrIfSubtype_Type()
)
tmnxLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrIfSubtype.setStatus("current")
_TmnxLldpRemManAddrIfId_Type = Integer32
_TmnxLldpRemManAddrIfId_Object = MibTableColumn
tmnxLldpRemManAddrIfId = _TmnxLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1, 4),
    _TmnxLldpRemManAddrIfId_Type()
)
tmnxLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrIfId.setStatus("current")
_TmnxLldpRemManAddrOID_Type = ObjectIdentifier
_TmnxLldpRemManAddrOID_Object = MibTableColumn
tmnxLldpRemManAddrOID = _TmnxLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 59, 4, 2, 1, 5),
    _TmnxLldpRemManAddrOID_Type()
)
tmnxLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrOID.setStatus("current")
_TmnxLldpNotifications_ObjectIdentity = ObjectIdentity
tmnxLldpNotifications = _TmnxLldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 59)
)

# Managed Objects groups

tmnxLldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 1)
)
tmnxLldpConfigGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpTxCreditMax"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpMessageFastTx"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpMessageFastTxInit"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpAdminStatus"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgAdminStatus"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgNotifyEnable"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgTLVsTxEnable"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgManAddrTxEnabled"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgManAddrSubtype"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpPortCfgManAddress"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpDestMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxLldpConfigGroup.setStatus("current")

tmnxLldpStatsRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 2)
)
tmnxLldpStatsRxGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortFrameDiscard"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortFrameErrs"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortFrames"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortTLVDiscard"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortTLVUnknown"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsRxPortAgeouts"))
)
if mibBuilder.loadTexts:
    tmnxLldpStatsRxGroup.setStatus("current")

tmnxLldpStatsTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 3)
)
tmnxLldpStatsTxGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpStatsTxPortFrames"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpStatsTxLLDPDULengthErrs"))
)
if mibBuilder.loadTexts:
    tmnxLldpStatsTxGroup.setStatus("current")

tmnxLldpLocSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 4)
)
tmnxLldpLocSysGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpLocPortIdSubtype"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpLocPortId"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpLocPortDesc"))
)
if mibBuilder.loadTexts:
    tmnxLldpLocSysGroup.setStatus("current")

tmnxLldpRemSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 5)
)
tmnxLldpRemSysGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpRemChassisIdSubtype"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemChassisId"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemPortIdSubtype"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemPortId"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemPortDesc"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemSysName"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemSysDesc"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemSysCapSupported"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemSysCapEnabled"))
)
if mibBuilder.loadTexts:
    tmnxLldpRemSysGroup.setStatus("current")

tmnxLldpRemManAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 2, 6)
)
tmnxLldpRemManAddrGroup.setObjects(
      *(("TIMETRA-LLDP-MIB", "tmnxLldpRemManAddrIfSubtype"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemManAddrIfId"),
        ("TIMETRA-LLDP-MIB", "tmnxLldpRemManAddrOID"))
)
if mibBuilder.loadTexts:
    tmnxLldpRemManAddrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxLldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 59, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxLldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LLDP-MIB",
    **{"TmnxLldpDestAddressTableIndex": TmnxLldpDestAddressTableIndex,
       "TmnxLldpManAddressIndex": TmnxLldpManAddressIndex,
       "tmnxLldpMIBModule": tmnxLldpMIBModule,
       "tmnxLldpConformance": tmnxLldpConformance,
       "tmnxLldpCompliances": tmnxLldpCompliances,
       "tmnxLldpCompliance": tmnxLldpCompliance,
       "tmnxLldpGroups": tmnxLldpGroups,
       "tmnxLldpConfigGroup": tmnxLldpConfigGroup,
       "tmnxLldpStatsRxGroup": tmnxLldpStatsRxGroup,
       "tmnxLldpStatsTxGroup": tmnxLldpStatsTxGroup,
       "tmnxLldpLocSysGroup": tmnxLldpLocSysGroup,
       "tmnxLldpRemSysGroup": tmnxLldpRemSysGroup,
       "tmnxLldpRemManAddrGroup": tmnxLldpRemManAddrGroup,
       "tmnxLldpObjects": tmnxLldpObjects,
       "tmnxLldpConfiguration": tmnxLldpConfiguration,
       "tmnxLldpTxCreditMax": tmnxLldpTxCreditMax,
       "tmnxLldpMessageFastTx": tmnxLldpMessageFastTx,
       "tmnxLldpMessageFastTxInit": tmnxLldpMessageFastTxInit,
       "tmnxLldpAdminStatus": tmnxLldpAdminStatus,
       "tmnxLldpPortConfigTable": tmnxLldpPortConfigTable,
       "tmnxLldpPortConfigEntry": tmnxLldpPortConfigEntry,
       "tmnxLldpPortCfgDestAddressIndex": tmnxLldpPortCfgDestAddressIndex,
       "tmnxLldpPortCfgAdminStatus": tmnxLldpPortCfgAdminStatus,
       "tmnxLldpPortCfgNotifyEnable": tmnxLldpPortCfgNotifyEnable,
       "tmnxLldpPortCfgTLVsTxEnable": tmnxLldpPortCfgTLVsTxEnable,
       "tmnxLldpConfigManAddrPortsTable": tmnxLldpConfigManAddrPortsTable,
       "tmnxLldpConfigManAddrPortsEntry": tmnxLldpConfigManAddrPortsEntry,
       "tmnxLldpPortCfgAddressIndex": tmnxLldpPortCfgAddressIndex,
       "tmnxLldpPortCfgManAddrTxEnabled": tmnxLldpPortCfgManAddrTxEnabled,
       "tmnxLldpPortCfgManAddrSubtype": tmnxLldpPortCfgManAddrSubtype,
       "tmnxLldpPortCfgManAddress": tmnxLldpPortCfgManAddress,
       "tmnxLldpDestAddressTable": tmnxLldpDestAddressTable,
       "tmnxLldpDestAddressTableEntry": tmnxLldpDestAddressTableEntry,
       "tmnxLldpAddressTableIndex": tmnxLldpAddressTableIndex,
       "tmnxLldpDestMacAddress": tmnxLldpDestMacAddress,
       "tmnxLldpStatistics": tmnxLldpStatistics,
       "tmnxLldpStatsTxPortTable": tmnxLldpStatsTxPortTable,
       "tmnxLldpStatsTxPortEntry": tmnxLldpStatsTxPortEntry,
       "tmnxLldpStatsTxDestMACAddress": tmnxLldpStatsTxDestMACAddress,
       "tmnxLldpStatsTxPortFrames": tmnxLldpStatsTxPortFrames,
       "tmnxLldpStatsTxLLDPDULengthErrs": tmnxLldpStatsTxLLDPDULengthErrs,
       "tmnxLldpStatsRxPortTable": tmnxLldpStatsRxPortTable,
       "tmnxLldpStatsRxPortEntry": tmnxLldpStatsRxPortEntry,
       "tmnxLldpStatsRxDestMACAddress": tmnxLldpStatsRxDestMACAddress,
       "tmnxLldpStatsRxPortFrameDiscard": tmnxLldpStatsRxPortFrameDiscard,
       "tmnxLldpStatsRxPortFrameErrs": tmnxLldpStatsRxPortFrameErrs,
       "tmnxLldpStatsRxPortFrames": tmnxLldpStatsRxPortFrames,
       "tmnxLldpStatsRxPortTLVDiscard": tmnxLldpStatsRxPortTLVDiscard,
       "tmnxLldpStatsRxPortTLVUnknown": tmnxLldpStatsRxPortTLVUnknown,
       "tmnxLldpStatsRxPortAgeouts": tmnxLldpStatsRxPortAgeouts,
       "tmnxLldpLocalSystemData": tmnxLldpLocalSystemData,
       "tmnxLldpLocPortTable": tmnxLldpLocPortTable,
       "tmnxLldpLocPortEntry": tmnxLldpLocPortEntry,
       "tmnxLldpLocPortDestMACAddress": tmnxLldpLocPortDestMACAddress,
       "tmnxLldpLocPortIdSubtype": tmnxLldpLocPortIdSubtype,
       "tmnxLldpLocPortId": tmnxLldpLocPortId,
       "tmnxLldpLocPortDesc": tmnxLldpLocPortDesc,
       "tmnxLldpRemoteSystemsData": tmnxLldpRemoteSystemsData,
       "tmnxLldpRemTable": tmnxLldpRemTable,
       "tmnxLldpRemEntry": tmnxLldpRemEntry,
       "tmnxLldpRemTimeMark": tmnxLldpRemTimeMark,
       "tmnxLldpRemLocalDestMACAddress": tmnxLldpRemLocalDestMACAddress,
       "tmnxLldpRemIndex": tmnxLldpRemIndex,
       "tmnxLldpRemChassisIdSubtype": tmnxLldpRemChassisIdSubtype,
       "tmnxLldpRemChassisId": tmnxLldpRemChassisId,
       "tmnxLldpRemPortIdSubtype": tmnxLldpRemPortIdSubtype,
       "tmnxLldpRemPortId": tmnxLldpRemPortId,
       "tmnxLldpRemPortDesc": tmnxLldpRemPortDesc,
       "tmnxLldpRemSysName": tmnxLldpRemSysName,
       "tmnxLldpRemSysDesc": tmnxLldpRemSysDesc,
       "tmnxLldpRemSysCapSupported": tmnxLldpRemSysCapSupported,
       "tmnxLldpRemSysCapEnabled": tmnxLldpRemSysCapEnabled,
       "tmnxLldpRemManAddrTable": tmnxLldpRemManAddrTable,
       "tmnxLldpRemManAddrEntry": tmnxLldpRemManAddrEntry,
       "tmnxLldpRemManAddrSubtype": tmnxLldpRemManAddrSubtype,
       "tmnxLldpRemManAddr": tmnxLldpRemManAddr,
       "tmnxLldpRemManAddrIfSubtype": tmnxLldpRemManAddrIfSubtype,
       "tmnxLldpRemManAddrIfId": tmnxLldpRemManAddrIfId,
       "tmnxLldpRemManAddrOID": tmnxLldpRemManAddrOID,
       "tmnxLldpNotifications": tmnxLldpNotifications}
)
