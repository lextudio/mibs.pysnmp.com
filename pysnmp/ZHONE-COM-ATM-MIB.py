# SNMP MIB module (ZHONE-COM-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:08 2024
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

(atmInterfaceDs3PlcpAlarmState,
 atmInterfaceTCAlarmState,
 atmInterfaceTCEntry,
 atmTrafficDescrParamEntry,
 atmVcCrossConnectEntry,
 atmVccAal5CpcsReceiveSduSize,
 atmVccAal5CpcsTransmitSduSize,
 atmVccAal5EncapsType,
 atmVccAalType,
 atmVclAdminStatus,
 atmVclCastType,
 atmVclConnKind,
 atmVclCrossConnectIdentifier,
 atmVclEntry,
 atmVclLastChange,
 atmVclOperStatus,
 atmVclReceiveTrafficDescrIndex,
 atmVclRowStatus,
 atmVclTransmitTrafficDescrIndex,
 atmVclVci,
 atmVclVpi,
 atmVplAdminStatus,
 atmVplCastType,
 atmVplConnKind,
 atmVplCrossConnectIdentifier,
 atmVplEntry,
 atmVplLastChange,
 atmVplOperStatus,
 atmVplReceiveTrafficDescrIndex,
 atmVplRowStatus,
 atmVplTransmitTrafficDescrIndex,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceDs3PlcpAlarmState",
    "atmInterfaceTCAlarmState",
    "atmInterfaceTCEntry",
    "atmTrafficDescrParamEntry",
    "atmVcCrossConnectEntry",
    "atmVccAal5CpcsReceiveSduSize",
    "atmVccAal5CpcsTransmitSduSize",
    "atmVccAal5EncapsType",
    "atmVccAalType",
    "atmVclAdminStatus",
    "atmVclCastType",
    "atmVclConnKind",
    "atmVclCrossConnectIdentifier",
    "atmVclEntry",
    "atmVclLastChange",
    "atmVclOperStatus",
    "atmVclReceiveTrafficDescrIndex",
    "atmVclRowStatus",
    "atmVclTransmitTrafficDescrIndex",
    "atmVclVci",
    "atmVclVpi",
    "atmVplAdminStatus",
    "atmVplCastType",
    "atmVplConnKind",
    "atmVplCrossConnectIdentifier",
    "atmVplEntry",
    "atmVplLastChange",
    "atmVplOperStatus",
    "atmVplReceiveTrafficDescrIndex",
    "atmVplRowStatus",
    "atmVplTransmitTrafficDescrIndex",
    "atmVplVpi")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(zhoneAtm,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneAtm",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comAtmExtension = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 25)
)
comAtmExtension.setRevisions(
        ("2005-04-05 16:44",
         "2005-02-28 13:18",
         "2004-09-07 10:44",
         "2004-06-19 10:15",
         "2004-01-28 12:42",
         "2003-12-04 15:23",
         "2003-09-09 14:11",
         "2003-04-16 16:04",
         "2003-03-11 13:46",
         "2003-02-14 16:55",
         "2003-02-11 13:30",
         "2002-08-23 10:36",
         "2002-08-13 16:14",
         "2002-06-04 20:13",
         "2002-05-28 12:12",
         "2002-05-21 17:29",
         "2002-05-15 17:29",
         "2002-03-20 20:19",
         "2001-12-19 15:24",
         "2001-11-02 17:22",
         "2001-10-29 17:34",
         "2001-09-20 10:54",
         "2001-08-30 17:15",
         "2001-08-14 12:00",
         "2001-07-11 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneAtmExtension_ObjectIdentity = ObjectIdentity
zhoneAtmExtension = _ZhoneAtmExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2)
)
if mibBuilder.loadTexts:
    zhoneAtmExtension.setStatus("current")
_ZhoneAtmVclExtTable_Object = MibTable
zhoneAtmVclExtTable = _ZhoneAtmVclExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmVclExtTable.setStatus("current")
_ZhoneAtmVclExtEntry_Object = MibTableRow
zhoneAtmVclExtEntry = _ZhoneAtmVclExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmVclExtEntry.setStatus("current")


class _ZhoneAtmVclExtFaultDetectionType_Type(Integer32):
    """Custom type zhoneAtmVclExtFaultDetectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("oamF5Loopback", 2))
    )


_ZhoneAtmVclExtFaultDetectionType_Type.__name__ = "Integer32"
_ZhoneAtmVclExtFaultDetectionType_Object = MibTableColumn
zhoneAtmVclExtFaultDetectionType = _ZhoneAtmVclExtFaultDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 1),
    _ZhoneAtmVclExtFaultDetectionType_Type()
)
zhoneAtmVclExtFaultDetectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVclExtFaultDetectionType.setStatus("current")


class _ZhoneAtmVclExtOamF5Ping_Type(Integer32):
    """Custom type zhoneAtmVclExtOamF5Ping based on Integer32"""
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
        *(("disabled", 1),
          ("endToEnd", 2),
          ("segment", 3))
    )


_ZhoneAtmVclExtOamF5Ping_Type.__name__ = "Integer32"
_ZhoneAtmVclExtOamF5Ping_Object = MibTableColumn
zhoneAtmVclExtOamF5Ping = _ZhoneAtmVclExtOamF5Ping_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 2),
    _ZhoneAtmVclExtOamF5Ping_Type()
)
zhoneAtmVclExtOamF5Ping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVclExtOamF5Ping.setStatus("current")
_ZhoneAtmVclExtOamF5PingStatus_Type = TruthValue
_ZhoneAtmVclExtOamF5PingStatus_Object = MibTableColumn
zhoneAtmVclExtOamF5PingStatus = _ZhoneAtmVclExtOamF5PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 3),
    _ZhoneAtmVclExtOamF5PingStatus_Type()
)
zhoneAtmVclExtOamF5PingStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneAtmVclExtOamF5PingStatus.setStatus("current")


class _ZhoneAtmVclExtTrafficContainerIndex_Type(Integer32):
    """Custom type zhoneAtmVclExtTrafficContainerIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneAtmVclExtTrafficContainerIndex_Type.__name__ = "Integer32"
_ZhoneAtmVclExtTrafficContainerIndex_Object = MibTableColumn
zhoneAtmVclExtTrafficContainerIndex = _ZhoneAtmVclExtTrafficContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 4),
    _ZhoneAtmVclExtTrafficContainerIndex_Type()
)
zhoneAtmVclExtTrafficContainerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVclExtTrafficContainerIndex.setStatus("current")


class _ZhoneAtmVclExtOamF4Ping_Type(Integer32):
    """Custom type zhoneAtmVclExtOamF4Ping based on Integer32"""
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
        *(("disabled", 1),
          ("endToEnd", 2),
          ("segment", 3))
    )


_ZhoneAtmVclExtOamF4Ping_Type.__name__ = "Integer32"
_ZhoneAtmVclExtOamF4Ping_Object = MibTableColumn
zhoneAtmVclExtOamF4Ping = _ZhoneAtmVclExtOamF4Ping_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 5),
    _ZhoneAtmVclExtOamF4Ping_Type()
)
zhoneAtmVclExtOamF4Ping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVclExtOamF4Ping.setStatus("current")
_ZhoneAtmVclExtOamF4PingStatus_Type = TruthValue
_ZhoneAtmVclExtOamF4PingStatus_Object = MibTableColumn
zhoneAtmVclExtOamF4PingStatus = _ZhoneAtmVclExtOamF4PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 1, 1, 6),
    _ZhoneAtmVclExtOamF4PingStatus_Type()
)
zhoneAtmVclExtOamF4PingStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneAtmVclExtOamF4PingStatus.setStatus("current")
_ZhoneAtmTraps_ObjectIdentity = ObjectIdentity
zhoneAtmTraps = _ZhoneAtmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zhoneAtmTraps.setStatus("current")
_ZhoneAtmV2Traps_ObjectIdentity = ObjectIdentity
zhoneAtmV2Traps = _ZhoneAtmV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0)
)
if mibBuilder.loadTexts:
    zhoneAtmV2Traps.setStatus("current")
_ZhoneAtmGroups_ObjectIdentity = ObjectIdentity
zhoneAtmGroups = _ZhoneAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zhoneAtmGroups.setStatus("current")
_ZhoneAtmTrafficDescrParamExtTable_Object = MibTable
zhoneAtmTrafficDescrParamExtTable = _ZhoneAtmTrafficDescrParamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtTable.setStatus("current")
_ZhoneAtmTrafficDescrParamExtEntry_Object = MibTableRow
zhoneAtmTrafficDescrParamExtEntry = _ZhoneAtmTrafficDescrParamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtEntry.setStatus("current")


class _ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type(Integer32):
    """Custom type zhoneAtmTrafficDescrParamExtTrnkVclRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 27),
          ("rate1280K", 19),
          ("rate128K", 6),
          ("rate128M", 33),
          ("rate12M", 14),
          ("rate14M", 28),
          ("rate1552K", 12),
          ("rate155M", 17),
          ("rate160K", 7),
          ("rate16K", 2),
          ("rate16M", 15),
          ("rate1760K", 20),
          ("rate2050K", 13),
          ("rate24M", 29),
          ("rate256K", 8),
          ("rate320K", 9),
          ("rate32K", 3),
          ("rate32M", 30),
          ("rate3M", 21),
          ("rate45M", 16),
          ("rate4M", 22),
          ("rate512K", 10),
          ("rate5M", 23),
          ("rate640K", 11),
          ("rate64K", 4),
          ("rate64M", 31),
          ("rate6M", 24),
          ("rate7M", 25),
          ("rate80K", 5),
          ("rate8M", 26),
          ("rate960K", 18),
          ("rate96M", 32),
          ("unused", 1))
    )


_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type.__name__ = "Integer32"
_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Object = MibTableColumn
zhoneAtmTrafficDescrParamExtTrnkVclRate = _ZhoneAtmTrafficDescrParamExtTrnkVclRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 4, 1, 1),
    _ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type()
)
zhoneAtmTrafficDescrParamExtTrnkVclRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtTrnkVclRate.setStatus("current")


class _ZhoneAtmTrafficDescrParamExtCacDivider_Type(Integer32):
    """Custom type zhoneAtmTrafficDescrParamExtCacDivider based on Integer32"""
    defaultBinValue = 1


_ZhoneAtmTrafficDescrParamExtCacDivider_Object = MibTableColumn
zhoneAtmTrafficDescrParamExtCacDivider = _ZhoneAtmTrafficDescrParamExtCacDivider_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 4, 1, 2),
    _ZhoneAtmTrafficDescrParamExtCacDivider_Type()
)
zhoneAtmTrafficDescrParamExtCacDivider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtCacDivider.setStatus("current")


class _ZhoneAtmTrafficDescrParamExtUsageParameterControl_Type(TruthValue):
    """Custom type zhoneAtmTrafficDescrParamExtUsageParameterControl based on TruthValue"""


_ZhoneAtmTrafficDescrParamExtUsageParameterControl_Object = MibTableColumn
zhoneAtmTrafficDescrParamExtUsageParameterControl = _ZhoneAtmTrafficDescrParamExtUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 4, 1, 3),
    _ZhoneAtmTrafficDescrParamExtUsageParameterControl_Type()
)
zhoneAtmTrafficDescrParamExtUsageParameterControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtUsageParameterControl.setStatus("current")
_ZhoneAtmStatsExtTable_Object = MibTable
zhoneAtmStatsExtTable = _ZhoneAtmStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    zhoneAtmStatsExtTable.setStatus("current")
_ZhoneAtmStatsExtEntry_Object = MibTableRow
zhoneAtmStatsExtEntry = _ZhoneAtmStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmStatsExtEntry.setStatus("current")
_ZhoneAtmStatsTotalInitialCellsRx_Type = Counter64
_ZhoneAtmStatsTotalInitialCellsRx_Object = MibTableColumn
zhoneAtmStatsTotalInitialCellsRx = _ZhoneAtmStatsTotalInitialCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 1),
    _ZhoneAtmStatsTotalInitialCellsRx_Type()
)
zhoneAtmStatsTotalInitialCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalInitialCellsRx.setStatus("current")
_ZhoneAtmStatsTotalFabricCellsRx_Type = Counter64
_ZhoneAtmStatsTotalFabricCellsRx_Object = MibTableColumn
zhoneAtmStatsTotalFabricCellsRx = _ZhoneAtmStatsTotalFabricCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 2),
    _ZhoneAtmStatsTotalFabricCellsRx_Type()
)
zhoneAtmStatsTotalFabricCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFabricCellsRx.setStatus("current")
_ZhoneAtmStatsTotalFinalCLP0CellsRx_Type = Counter64
_ZhoneAtmStatsTotalFinalCLP0CellsRx_Object = MibTableColumn
zhoneAtmStatsTotalFinalCLP0CellsRx = _ZhoneAtmStatsTotalFinalCLP0CellsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 3),
    _ZhoneAtmStatsTotalFinalCLP0CellsRx_Type()
)
zhoneAtmStatsTotalFinalCLP0CellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFinalCLP0CellsRx.setStatus("current")
_ZhoneAtmStatsTotalFinalCLP1CellsRx_Type = Counter64
_ZhoneAtmStatsTotalFinalCLP1CellsRx_Object = MibTableColumn
zhoneAtmStatsTotalFinalCLP1CellsRx = _ZhoneAtmStatsTotalFinalCLP1CellsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 4),
    _ZhoneAtmStatsTotalFinalCLP1CellsRx_Type()
)
zhoneAtmStatsTotalFinalCLP1CellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFinalCLP1CellsRx.setStatus("current")
_ZhoneAtmStatsTotalInitialCellsTx_Type = Counter64
_ZhoneAtmStatsTotalInitialCellsTx_Object = MibTableColumn
zhoneAtmStatsTotalInitialCellsTx = _ZhoneAtmStatsTotalInitialCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 5),
    _ZhoneAtmStatsTotalInitialCellsTx_Type()
)
zhoneAtmStatsTotalInitialCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalInitialCellsTx.setStatus("current")
_ZhoneAtmStatsTotalFabricCellsTx_Type = Counter64
_ZhoneAtmStatsTotalFabricCellsTx_Object = MibTableColumn
zhoneAtmStatsTotalFabricCellsTx = _ZhoneAtmStatsTotalFabricCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 6),
    _ZhoneAtmStatsTotalFabricCellsTx_Type()
)
zhoneAtmStatsTotalFabricCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFabricCellsTx.setStatus("current")
_ZhoneAtmStatsTotalFinalCLP0CellsTx_Type = Counter64
_ZhoneAtmStatsTotalFinalCLP0CellsTx_Object = MibTableColumn
zhoneAtmStatsTotalFinalCLP0CellsTx = _ZhoneAtmStatsTotalFinalCLP0CellsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 7),
    _ZhoneAtmStatsTotalFinalCLP0CellsTx_Type()
)
zhoneAtmStatsTotalFinalCLP0CellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFinalCLP0CellsTx.setStatus("current")
_ZhoneAtmStatsTotalFinalCLP1CellsTx_Type = Counter64
_ZhoneAtmStatsTotalFinalCLP1CellsTx_Object = MibTableColumn
zhoneAtmStatsTotalFinalCLP1CellsTx = _ZhoneAtmStatsTotalFinalCLP1CellsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 5, 1, 8),
    _ZhoneAtmStatsTotalFinalCLP1CellsTx_Type()
)
zhoneAtmStatsTotalFinalCLP1CellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmStatsTotalFinalCLP1CellsTx.setStatus("current")
_ZhoneAtmVclRateExtParam_ObjectIdentity = ObjectIdentity
zhoneAtmVclRateExtParam = _ZhoneAtmVclRateExtParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam.setStatus("current")


class _ZhoneAtmVclRateExtParam1_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam1 based on Integer32"""
    defaultValue = 38


_ZhoneAtmVclRateExtParam1_Object = MibScalar
zhoneAtmVclRateExtParam1 = _ZhoneAtmVclRateExtParam1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 1),
    _ZhoneAtmVclRateExtParam1_Type()
)
zhoneAtmVclRateExtParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam1.setStatus("current")


class _ZhoneAtmVclRateExtParam2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam2 based on Integer32"""
    defaultValue = 76


_ZhoneAtmVclRateExtParam2_Object = MibScalar
zhoneAtmVclRateExtParam2 = _ZhoneAtmVclRateExtParam2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 2),
    _ZhoneAtmVclRateExtParam2_Type()
)
zhoneAtmVclRateExtParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam2.setStatus("current")


class _ZhoneAtmVclRateExtParam3_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam3 based on Integer32"""
    defaultValue = 151


_ZhoneAtmVclRateExtParam3_Object = MibScalar
zhoneAtmVclRateExtParam3 = _ZhoneAtmVclRateExtParam3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 3),
    _ZhoneAtmVclRateExtParam3_Type()
)
zhoneAtmVclRateExtParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam3.setStatus("current")


class _ZhoneAtmVclRateExtParam4_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam4 based on Integer32"""
    defaultValue = 189


_ZhoneAtmVclRateExtParam4_Object = MibScalar
zhoneAtmVclRateExtParam4 = _ZhoneAtmVclRateExtParam4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 4),
    _ZhoneAtmVclRateExtParam4_Type()
)
zhoneAtmVclRateExtParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam4.setStatus("current")


class _ZhoneAtmVclRateExtParam5_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam5 based on Integer32"""
    defaultValue = 302


_ZhoneAtmVclRateExtParam5_Object = MibScalar
zhoneAtmVclRateExtParam5 = _ZhoneAtmVclRateExtParam5_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 5),
    _ZhoneAtmVclRateExtParam5_Type()
)
zhoneAtmVclRateExtParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam5.setStatus("current")


class _ZhoneAtmVclRateExtParam6_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam6 based on Integer32"""
    defaultValue = 378


_ZhoneAtmVclRateExtParam6_Object = MibScalar
zhoneAtmVclRateExtParam6 = _ZhoneAtmVclRateExtParam6_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 6),
    _ZhoneAtmVclRateExtParam6_Type()
)
zhoneAtmVclRateExtParam6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam6.setStatus("current")


class _ZhoneAtmVclRateExtParam7_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam7 based on Integer32"""
    defaultValue = 604


_ZhoneAtmVclRateExtParam7_Object = MibScalar
zhoneAtmVclRateExtParam7 = _ZhoneAtmVclRateExtParam7_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 7),
    _ZhoneAtmVclRateExtParam7_Type()
)
zhoneAtmVclRateExtParam7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam7.setStatus("current")


class _ZhoneAtmVclRateExtParam8_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam8 based on Integer32"""
    defaultValue = 755


_ZhoneAtmVclRateExtParam8_Object = MibScalar
zhoneAtmVclRateExtParam8 = _ZhoneAtmVclRateExtParam8_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 8),
    _ZhoneAtmVclRateExtParam8_Type()
)
zhoneAtmVclRateExtParam8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam8.setStatus("current")


class _ZhoneAtmVclRateExtParam9_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam9 based on Integer32"""
    defaultValue = 1208


_ZhoneAtmVclRateExtParam9_Object = MibScalar
zhoneAtmVclRateExtParam9 = _ZhoneAtmVclRateExtParam9_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 9),
    _ZhoneAtmVclRateExtParam9_Type()
)
zhoneAtmVclRateExtParam9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam9.setStatus("current")


class _ZhoneAtmVclRateExtParam10_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam10 based on Integer32"""
    defaultValue = 1510


_ZhoneAtmVclRateExtParam10_Object = MibScalar
zhoneAtmVclRateExtParam10 = _ZhoneAtmVclRateExtParam10_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 10),
    _ZhoneAtmVclRateExtParam10_Type()
)
zhoneAtmVclRateExtParam10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam10.setStatus("current")


class _ZhoneAtmVclRateExtParam11_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam11 based on Integer32"""
    defaultValue = 3661


_ZhoneAtmVclRateExtParam11_Object = MibScalar
zhoneAtmVclRateExtParam11 = _ZhoneAtmVclRateExtParam11_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 11),
    _ZhoneAtmVclRateExtParam11_Type()
)
zhoneAtmVclRateExtParam11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam11.setStatus("current")


class _ZhoneAtmVclRateExtParam12_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam12 based on Integer32"""
    defaultValue = 4825


_ZhoneAtmVclRateExtParam12_Object = MibScalar
zhoneAtmVclRateExtParam12 = _ZhoneAtmVclRateExtParam12_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 12),
    _ZhoneAtmVclRateExtParam12_Type()
)
zhoneAtmVclRateExtParam12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam12.setStatus("current")


class _ZhoneAtmVclRateExtParam13_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam13 based on Integer32"""
    defaultValue = 28302


_ZhoneAtmVclRateExtParam13_Object = MibScalar
zhoneAtmVclRateExtParam13 = _ZhoneAtmVclRateExtParam13_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 13),
    _ZhoneAtmVclRateExtParam13_Type()
)
zhoneAtmVclRateExtParam13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam13.setStatus("current")


class _ZhoneAtmVclRateExtParam14_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam14 based on Integer32"""
    defaultValue = 37736


_ZhoneAtmVclRateExtParam14_Object = MibScalar
zhoneAtmVclRateExtParam14 = _ZhoneAtmVclRateExtParam14_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 14),
    _ZhoneAtmVclRateExtParam14_Type()
)
zhoneAtmVclRateExtParam14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam14.setStatus("current")


class _ZhoneAtmVclRateExtParam15_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam15 based on Integer32"""
    defaultValue = 106133


_ZhoneAtmVclRateExtParam15_Object = MibScalar
zhoneAtmVclRateExtParam15 = _ZhoneAtmVclRateExtParam15_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 15),
    _ZhoneAtmVclRateExtParam15_Type()
)
zhoneAtmVclRateExtParam15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam15.setStatus("current")


class _ZhoneAtmVclRateExtParam16_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam16 based on Integer32"""
    defaultValue = 365567


_ZhoneAtmVclRateExtParam16_Object = MibScalar
zhoneAtmVclRateExtParam16 = _ZhoneAtmVclRateExtParam16_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 16),
    _ZhoneAtmVclRateExtParam16_Type()
)
zhoneAtmVclRateExtParam16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam16.setStatus("current")


class _ZhoneAtmVclRateExtParam1Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam1Grp2 based on Integer32"""
    defaultValue = 2264


_ZhoneAtmVclRateExtParam1Grp2_Object = MibScalar
zhoneAtmVclRateExtParam1Grp2 = _ZhoneAtmVclRateExtParam1Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 17),
    _ZhoneAtmVclRateExtParam1Grp2_Type()
)
zhoneAtmVclRateExtParam1Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam1Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam2Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam2Grp2 based on Integer32"""
    defaultValue = 3019


_ZhoneAtmVclRateExtParam2Grp2_Object = MibScalar
zhoneAtmVclRateExtParam2Grp2 = _ZhoneAtmVclRateExtParam2Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 18),
    _ZhoneAtmVclRateExtParam2Grp2_Type()
)
zhoneAtmVclRateExtParam2Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam2Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam3Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam3Grp2 based on Integer32"""
    defaultValue = 4151


_ZhoneAtmVclRateExtParam3Grp2_Object = MibScalar
zhoneAtmVclRateExtParam3Grp2 = _ZhoneAtmVclRateExtParam3Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 19),
    _ZhoneAtmVclRateExtParam3Grp2_Type()
)
zhoneAtmVclRateExtParam3Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam3Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam4Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam4Grp2 based on Integer32"""
    defaultValue = 7075


_ZhoneAtmVclRateExtParam4Grp2_Object = MibScalar
zhoneAtmVclRateExtParam4Grp2 = _ZhoneAtmVclRateExtParam4Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 20),
    _ZhoneAtmVclRateExtParam4Grp2_Type()
)
zhoneAtmVclRateExtParam4Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam4Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam5Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam5Grp2 based on Integer32"""
    defaultValue = 9434


_ZhoneAtmVclRateExtParam5Grp2_Object = MibScalar
zhoneAtmVclRateExtParam5Grp2 = _ZhoneAtmVclRateExtParam5Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 21),
    _ZhoneAtmVclRateExtParam5Grp2_Type()
)
zhoneAtmVclRateExtParam5Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam5Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam6Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam6Grp2 based on Integer32"""
    defaultValue = 11792


_ZhoneAtmVclRateExtParam6Grp2_Object = MibScalar
zhoneAtmVclRateExtParam6Grp2 = _ZhoneAtmVclRateExtParam6Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 22),
    _ZhoneAtmVclRateExtParam6Grp2_Type()
)
zhoneAtmVclRateExtParam6Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam6Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam7Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam7Grp2 based on Integer32"""
    defaultValue = 14151


_ZhoneAtmVclRateExtParam7Grp2_Object = MibScalar
zhoneAtmVclRateExtParam7Grp2 = _ZhoneAtmVclRateExtParam7Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 23),
    _ZhoneAtmVclRateExtParam7Grp2_Type()
)
zhoneAtmVclRateExtParam7Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam7Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam8Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam8Grp2 based on Integer32"""
    defaultValue = 16509


_ZhoneAtmVclRateExtParam8Grp2_Object = MibScalar
zhoneAtmVclRateExtParam8Grp2 = _ZhoneAtmVclRateExtParam8Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 24),
    _ZhoneAtmVclRateExtParam8Grp2_Type()
)
zhoneAtmVclRateExtParam8Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam8Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam9Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam9Grp2 based on Integer32"""
    defaultValue = 18868


_ZhoneAtmVclRateExtParam9Grp2_Object = MibScalar
zhoneAtmVclRateExtParam9Grp2 = _ZhoneAtmVclRateExtParam9Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 25),
    _ZhoneAtmVclRateExtParam9Grp2_Type()
)
zhoneAtmVclRateExtParam9Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam9Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam10Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam10Grp2 based on Integer32"""
    defaultValue = 23585


_ZhoneAtmVclRateExtParam10Grp2_Object = MibScalar
zhoneAtmVclRateExtParam10Grp2 = _ZhoneAtmVclRateExtParam10Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 26),
    _ZhoneAtmVclRateExtParam10Grp2_Type()
)
zhoneAtmVclRateExtParam10Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam10Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam11Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam11Grp2 based on Integer32"""
    defaultValue = 33019


_ZhoneAtmVclRateExtParam11Grp2_Object = MibScalar
zhoneAtmVclRateExtParam11Grp2 = _ZhoneAtmVclRateExtParam11Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 27),
    _ZhoneAtmVclRateExtParam11Grp2_Type()
)
zhoneAtmVclRateExtParam11Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam11Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam12Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam12Grp2 based on Integer32"""
    defaultValue = 56604


_ZhoneAtmVclRateExtParam12Grp2_Object = MibScalar
zhoneAtmVclRateExtParam12Grp2 = _ZhoneAtmVclRateExtParam12Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 28),
    _ZhoneAtmVclRateExtParam12Grp2_Type()
)
zhoneAtmVclRateExtParam12Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam12Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam13Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam13Grp2 based on Integer32"""
    defaultValue = 75472


_ZhoneAtmVclRateExtParam13Grp2_Object = MibScalar
zhoneAtmVclRateExtParam13Grp2 = _ZhoneAtmVclRateExtParam13Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 29),
    _ZhoneAtmVclRateExtParam13Grp2_Type()
)
zhoneAtmVclRateExtParam13Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam13Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam14Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam14Grp2 based on Integer32"""
    defaultValue = 150943


_ZhoneAtmVclRateExtParam14Grp2_Object = MibScalar
zhoneAtmVclRateExtParam14Grp2 = _ZhoneAtmVclRateExtParam14Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 30),
    _ZhoneAtmVclRateExtParam14Grp2_Type()
)
zhoneAtmVclRateExtParam14Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam14Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam15Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam15Grp2 based on Integer32"""
    defaultValue = 226415


_ZhoneAtmVclRateExtParam15Grp2_Object = MibScalar
zhoneAtmVclRateExtParam15Grp2 = _ZhoneAtmVclRateExtParam15Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 31),
    _ZhoneAtmVclRateExtParam15Grp2_Type()
)
zhoneAtmVclRateExtParam15Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam15Grp2.setStatus("current")


class _ZhoneAtmVclRateExtParam16Grp2_Type(Integer32):
    """Custom type zhoneAtmVclRateExtParam16Grp2 based on Integer32"""
    defaultValue = 301887


_ZhoneAtmVclRateExtParam16Grp2_Object = MibScalar
zhoneAtmVclRateExtParam16Grp2 = _ZhoneAtmVclRateExtParam16Grp2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 6, 32),
    _ZhoneAtmVclRateExtParam16Grp2_Type()
)
zhoneAtmVclRateExtParam16Grp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParam16Grp2.setStatus("current")
_ZhoneAtmVplExtTable_Object = MibTable
zhoneAtmVplExtTable = _ZhoneAtmVplExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 7)
)
if mibBuilder.loadTexts:
    zhoneAtmVplExtTable.setStatus("current")
_ZhoneAtmVplExtEntry_Object = MibTableRow
zhoneAtmVplExtEntry = _ZhoneAtmVplExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmVplExtEntry.setStatus("current")


class _ZhoneAtmVplExtFaultDetectionType_Type(Integer32):
    """Custom type zhoneAtmVplExtFaultDetectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("oamF4Loopback", 2))
    )


_ZhoneAtmVplExtFaultDetectionType_Type.__name__ = "Integer32"
_ZhoneAtmVplExtFaultDetectionType_Object = MibTableColumn
zhoneAtmVplExtFaultDetectionType = _ZhoneAtmVplExtFaultDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 7, 1, 1),
    _ZhoneAtmVplExtFaultDetectionType_Type()
)
zhoneAtmVplExtFaultDetectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVplExtFaultDetectionType.setStatus("current")


class _ZhoneAtmVplExtTrafficContainerIndex_Type(Integer32):
    """Custom type zhoneAtmVplExtTrafficContainerIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneAtmVplExtTrafficContainerIndex_Type.__name__ = "Integer32"
_ZhoneAtmVplExtTrafficContainerIndex_Object = MibTableColumn
zhoneAtmVplExtTrafficContainerIndex = _ZhoneAtmVplExtTrafficContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 7, 1, 2),
    _ZhoneAtmVplExtTrafficContainerIndex_Type()
)
zhoneAtmVplExtTrafficContainerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVplExtTrafficContainerIndex.setStatus("current")
_ZhoneAtmConnectionStatsTable_Object = MibTable
zhoneAtmConnectionStatsTable = _ZhoneAtmConnectionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 8)
)
if mibBuilder.loadTexts:
    zhoneAtmConnectionStatsTable.setStatus("current")
_ZhoneAtmConnectionStatsEntry_Object = MibTableRow
zhoneAtmConnectionStatsEntry = _ZhoneAtmConnectionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 8, 1)
)
zhoneAtmConnectionStatsEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    zhoneAtmConnectionStatsEntry.setStatus("current")
_ZhoneAtmConnectionsAvailable_Type = Integer32
_ZhoneAtmConnectionsAvailable_Object = MibTableColumn
zhoneAtmConnectionsAvailable = _ZhoneAtmConnectionsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 8, 1, 1),
    _ZhoneAtmConnectionsAvailable_Type()
)
zhoneAtmConnectionsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmConnectionsAvailable.setStatus("current")
_ZhoneAtmConnectionsAllocated_Type = Integer32
_ZhoneAtmConnectionsAllocated_Object = MibTableColumn
zhoneAtmConnectionsAllocated = _ZhoneAtmConnectionsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 8, 1, 2),
    _ZhoneAtmConnectionsAllocated_Type()
)
zhoneAtmConnectionsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmConnectionsAllocated.setStatus("current")
_ZhoneAtmVpiTable_Object = MibTable
zhoneAtmVpiTable = _ZhoneAtmVpiTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9)
)
if mibBuilder.loadTexts:
    zhoneAtmVpiTable.setStatus("current")
_ZhoneAtmVpiEntry_Object = MibTableRow
zhoneAtmVpiEntry = _ZhoneAtmVpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1)
)
zhoneAtmVpiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    zhoneAtmVpiEntry.setStatus("current")


class _ZhoneAtmVpiMaxVci_Type(Integer32):
    """Custom type zhoneAtmVpiMaxVci based on Integer32"""
    defaultValue = 0


_ZhoneAtmVpiMaxVci_Object = MibTableColumn
zhoneAtmVpiMaxVci = _ZhoneAtmVpiMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 1),
    _ZhoneAtmVpiMaxVci_Type()
)
zhoneAtmVpiMaxVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVpiMaxVci.setStatus("current")


class _ZhoneAtmVpiSwitched_Type(Integer32):
    """Custom type zhoneAtmVpiSwitched based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vc", 2),
          ("vp", 1))
    )


_ZhoneAtmVpiSwitched_Type.__name__ = "Integer32"
_ZhoneAtmVpiSwitched_Object = MibTableColumn
zhoneAtmVpiSwitched = _ZhoneAtmVpiSwitched_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 2),
    _ZhoneAtmVpiSwitched_Type()
)
zhoneAtmVpiSwitched.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVpiSwitched.setStatus("current")
_ZhoneAtmVpiRowStatus_Type = ZhoneRowStatus
_ZhoneAtmVpiRowStatus_Object = MibTableColumn
zhoneAtmVpiRowStatus = _ZhoneAtmVpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 3),
    _ZhoneAtmVpiRowStatus_Type()
)
zhoneAtmVpiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVpiRowStatus.setStatus("current")


class _ZhoneAtmVpiOamF4Ping_Type(Integer32):
    """Custom type zhoneAtmVpiOamF4Ping based on Integer32"""
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
        *(("disabled", 1),
          ("endToEnd", 2),
          ("segment", 3))
    )


_ZhoneAtmVpiOamF4Ping_Type.__name__ = "Integer32"
_ZhoneAtmVpiOamF4Ping_Object = MibTableColumn
zhoneAtmVpiOamF4Ping = _ZhoneAtmVpiOamF4Ping_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 4),
    _ZhoneAtmVpiOamF4Ping_Type()
)
zhoneAtmVpiOamF4Ping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVpiOamF4Ping.setStatus("current")
_ZhoneAtmVpiOamF4PingStatus_Type = TruthValue
_ZhoneAtmVpiOamF4PingStatus_Object = MibTableColumn
zhoneAtmVpiOamF4PingStatus = _ZhoneAtmVpiOamF4PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 5),
    _ZhoneAtmVpiOamF4PingStatus_Type()
)
zhoneAtmVpiOamF4PingStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneAtmVpiOamF4PingStatus.setStatus("current")
_ZhoneAtmVpiMaxVciPerVp_Type = Integer32
_ZhoneAtmVpiMaxVciPerVp_Object = MibTableColumn
zhoneAtmVpiMaxVciPerVp = _ZhoneAtmVpiMaxVciPerVp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 9, 1, 6),
    _ZhoneAtmVpiMaxVciPerVp_Type()
)
zhoneAtmVpiMaxVciPerVp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAtmVpiMaxVciPerVp.setStatus("current")
_AtmVpi_Type = AtmVpIdentifier
_AtmVpi_Object = MibScalar
atmVpi = _AtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 10),
    _AtmVpi_Type()
)
atmVpi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmVpi.setStatus("current")
_AtmVci_Type = AtmVcIdentifier
_AtmVci_Object = MibScalar
atmVci = _AtmVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 11),
    _AtmVci_Type()
)
atmVci.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmVci.setStatus("current")
_AtmVpiAutoCreateDone_Type = TruthValue
_AtmVpiAutoCreateDone_Object = MibScalar
atmVpiAutoCreateDone = _AtmVpiAutoCreateDone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 12),
    _AtmVpiAutoCreateDone_Type()
)
atmVpiAutoCreateDone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmVpiAutoCreateDone.setStatus("current")
_AtmVpiAutoCreateCount_Type = Integer32
_AtmVpiAutoCreateCount_Object = MibScalar
atmVpiAutoCreateCount = _AtmVpiAutoCreateCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 13),
    _AtmVpiAutoCreateCount_Type()
)
atmVpiAutoCreateCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmVpiAutoCreateCount.setStatus("current")
_AtmVclToMulticastMap_ObjectIdentity = ObjectIdentity
atmVclToMulticastMap = _AtmVclToMulticastMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16)
)


class _AtmVclToMulticastMapIndexNext_Type(Integer32):
    """Custom type atmVclToMulticastMapIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVclToMulticastMapIndexNext_Type.__name__ = "Integer32"
_AtmVclToMulticastMapIndexNext_Object = MibScalar
atmVclToMulticastMapIndexNext = _AtmVclToMulticastMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 1),
    _AtmVclToMulticastMapIndexNext_Type()
)
atmVclToMulticastMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclToMulticastMapIndexNext.setStatus("current")
_AtmVclToMulticastMapTable_Object = MibTable
atmVclToMulticastMapTable = _AtmVclToMulticastMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2)
)
if mibBuilder.loadTexts:
    atmVclToMulticastMapTable.setStatus("current")
_AtmVclToMulticastMapEntry_Object = MibTableRow
atmVclToMulticastMapEntry = _AtmVclToMulticastMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1)
)
atmVclToMulticastMapEntry.setIndexNames(
    (0, "ZHONE-COM-ATM-MIB", "atmVclToMulticastMapIndex"),
)
if mibBuilder.loadTexts:
    atmVclToMulticastMapEntry.setStatus("current")


class _AtmVclToMulticastMapIndex_Type(Integer32):
    """Custom type atmVclToMulticastMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmVclToMulticastMapIndex_Type.__name__ = "Integer32"
_AtmVclToMulticastMapIndex_Object = MibTableColumn
atmVclToMulticastMapIndex = _AtmVclToMulticastMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 1),
    _AtmVclToMulticastMapIndex_Type()
)
atmVclToMulticastMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclToMulticastMapIndex.setStatus("current")


class _AtmVclToMulticastMapRoutingDomain_Type(Integer32):
    """Custom type atmVclToMulticastMapRoutingDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVclToMulticastMapRoutingDomain_Type.__name__ = "Integer32"
_AtmVclToMulticastMapRoutingDomain_Object = MibTableColumn
atmVclToMulticastMapRoutingDomain = _AtmVclToMulticastMapRoutingDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 2),
    _AtmVclToMulticastMapRoutingDomain_Type()
)
atmVclToMulticastMapRoutingDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapRoutingDomain.setStatus("current")
_AtmVclToMulticastMapMulticastAddress_Type = IpAddress
_AtmVclToMulticastMapMulticastAddress_Object = MibTableColumn
atmVclToMulticastMapMulticastAddress = _AtmVclToMulticastMapMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 3),
    _AtmVclToMulticastMapMulticastAddress_Type()
)
atmVclToMulticastMapMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapMulticastAddress.setStatus("current")
_AtmVclToMulticastMapIfIndex_Type = InterfaceIndex
_AtmVclToMulticastMapIfIndex_Object = MibTableColumn
atmVclToMulticastMapIfIndex = _AtmVclToMulticastMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 4),
    _AtmVclToMulticastMapIfIndex_Type()
)
atmVclToMulticastMapIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapIfIndex.setStatus("current")
_AtmVclToMulticastMapVpi_Type = AtmVpIdentifier
_AtmVclToMulticastMapVpi_Object = MibTableColumn
atmVclToMulticastMapVpi = _AtmVclToMulticastMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 5),
    _AtmVclToMulticastMapVpi_Type()
)
atmVclToMulticastMapVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapVpi.setStatus("current")
_AtmVclToMulticastMapVci_Type = AtmVcIdentifier
_AtmVclToMulticastMapVci_Object = MibTableColumn
atmVclToMulticastMapVci = _AtmVclToMulticastMapVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 6),
    _AtmVclToMulticastMapVci_Type()
)
atmVclToMulticastMapVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapVci.setStatus("current")
_AtmVclToMulticastMapRowStatus_Type = ZhoneRowStatus
_AtmVclToMulticastMapRowStatus_Object = MibTableColumn
atmVclToMulticastMapRowStatus = _AtmVclToMulticastMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 16, 2, 1, 7),
    _AtmVclToMulticastMapRowStatus_Type()
)
atmVclToMulticastMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclToMulticastMapRowStatus.setStatus("current")
_ZhoneAtmPonExtTable_Object = MibTable
zhoneAtmPonExtTable = _ZhoneAtmPonExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 17)
)
if mibBuilder.loadTexts:
    zhoneAtmPonExtTable.setStatus("deprecated")
_ZhoneAtmPonExtEntry_Object = MibTableRow
zhoneAtmPonExtEntry = _ZhoneAtmPonExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmPonExtEntry.setStatus("deprecated")


class _ZhoneAtmVclPonTrafficContainerIndex_Type(Integer32):
    """Custom type zhoneAtmVclPonTrafficContainerIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneAtmVclPonTrafficContainerIndex_Type.__name__ = "Integer32"
_ZhoneAtmVclPonTrafficContainerIndex_Object = MibTableColumn
zhoneAtmVclPonTrafficContainerIndex = _ZhoneAtmVclPonTrafficContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 17, 1, 1),
    _ZhoneAtmVclPonTrafficContainerIndex_Type()
)
zhoneAtmVclPonTrafficContainerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVclPonTrafficContainerIndex.setStatus("deprecated")
_ZhoneAtmVplPonExtTable_Object = MibTable
zhoneAtmVplPonExtTable = _ZhoneAtmVplPonExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 18)
)
if mibBuilder.loadTexts:
    zhoneAtmVplPonExtTable.setStatus("deprecated")
_ZhoneAtmVplPonExtEntry_Object = MibTableRow
zhoneAtmVplPonExtEntry = _ZhoneAtmVplPonExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmVplPonExtEntry.setStatus("deprecated")


class _ZhoneAtmVplPonTrafficContainerIndex_Type(Integer32):
    """Custom type zhoneAtmVplPonTrafficContainerIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneAtmVplPonTrafficContainerIndex_Type.__name__ = "Integer32"
_ZhoneAtmVplPonTrafficContainerIndex_Object = MibTableColumn
zhoneAtmVplPonTrafficContainerIndex = _ZhoneAtmVplPonTrafficContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 18, 1, 1),
    _ZhoneAtmVplPonTrafficContainerIndex_Type()
)
zhoneAtmVplPonTrafficContainerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVplPonTrafficContainerIndex.setStatus("deprecated")
_ZhoneAtmInterfaceTcExtTable_Object = MibTable
zhoneAtmInterfaceTcExtTable = _ZhoneAtmInterfaceTcExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19)
)
if mibBuilder.loadTexts:
    zhoneAtmInterfaceTcExtTable.setStatus("current")
_ZhoneAtmInterfaceTcExtEntry_Object = MibTableRow
zhoneAtmInterfaceTcExtEntry = _ZhoneAtmInterfaceTcExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmInterfaceTcExtEntry.setStatus("current")
_ZhoneAtmInterfaceNCDEvents_Type = Counter32
_ZhoneAtmInterfaceNCDEvents_Object = MibTableColumn
zhoneAtmInterfaceNCDEvents = _ZhoneAtmInterfaceNCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1, 1),
    _ZhoneAtmInterfaceNCDEvents_Type()
)
zhoneAtmInterfaceNCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmInterfaceNCDEvents.setStatus("current")
_ZhoneAtmInterfaceHECEvents_Type = Counter32
_ZhoneAtmInterfaceHECEvents_Object = MibTableColumn
zhoneAtmInterfaceHECEvents = _ZhoneAtmInterfaceHECEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1, 2),
    _ZhoneAtmInterfaceHECEvents_Type()
)
zhoneAtmInterfaceHECEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmInterfaceHECEvents.setStatus("current")
_ZhoneAtmInterfaceFeOCDEvents_Type = Counter32
_ZhoneAtmInterfaceFeOCDEvents_Object = MibTableColumn
zhoneAtmInterfaceFeOCDEvents = _ZhoneAtmInterfaceFeOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1, 3),
    _ZhoneAtmInterfaceFeOCDEvents_Type()
)
zhoneAtmInterfaceFeOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmInterfaceFeOCDEvents.setStatus("current")
_ZhoneAtmInterfaceFeNCDEvents_Type = Counter32
_ZhoneAtmInterfaceFeNCDEvents_Object = MibTableColumn
zhoneAtmInterfaceFeNCDEvents = _ZhoneAtmInterfaceFeNCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1, 4),
    _ZhoneAtmInterfaceFeNCDEvents_Type()
)
zhoneAtmInterfaceFeNCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmInterfaceFeNCDEvents.setStatus("current")
_ZhoneAtmInterfaceFeHECEvents_Type = Counter32
_ZhoneAtmInterfaceFeHECEvents_Object = MibTableColumn
zhoneAtmInterfaceFeHECEvents = _ZhoneAtmInterfaceFeHECEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 19, 1, 5),
    _ZhoneAtmInterfaceFeHECEvents_Type()
)
zhoneAtmInterfaceFeHECEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAtmInterfaceFeHECEvents.setStatus("current")
_ZhoneAtmVcCrossConnectExtTable_Object = MibTable
zhoneAtmVcCrossConnectExtTable = _ZhoneAtmVcCrossConnectExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 20)
)
if mibBuilder.loadTexts:
    zhoneAtmVcCrossConnectExtTable.setStatus("current")
_ZhoneAtmVcCrossConnectExtEntry_Object = MibTableRow
zhoneAtmVcCrossConnectExtEntry = _ZhoneAtmVcCrossConnectExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 20, 1)
)
if mibBuilder.loadTexts:
    zhoneAtmVcCrossConnectExtEntry.setStatus("current")


class _ZhoneAtmVcCrossConnectExtHandleId_Type(OctetString):
    """Custom type zhoneAtmVcCrossConnectExtHandleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZhoneAtmVcCrossConnectExtHandleId_Type.__name__ = "OctetString"
_ZhoneAtmVcCrossConnectExtHandleId_Object = MibTableColumn
zhoneAtmVcCrossConnectExtHandleId = _ZhoneAtmVcCrossConnectExtHandleId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 20, 1, 1),
    _ZhoneAtmVcCrossConnectExtHandleId_Type()
)
zhoneAtmVcCrossConnectExtHandleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAtmVcCrossConnectExtHandleId.setStatus("current")
atmVclEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmVclExtEntry")
)
zhoneAtmVclExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmTrafficDescrParamExtEntry")
)
zhoneAtmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmStatsExtEntry")
)
zhoneAtmStatsExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmVplExtEntry")
)
zhoneAtmVplExtEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmPonExtEntry")
)
zhoneAtmPonExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmVplPonExtEntry")
)
zhoneAtmVplPonExtEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmInterfaceTCEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmInterfaceTcExtEntry")
)
zhoneAtmInterfaceTcExtEntry.setIndexNames(*atmInterfaceTCEntry.getIndexNames())
atmVcCrossConnectEntry.registerAugmentions(
    ("ZHONE-COM-ATM-MIB",
     "zhoneAtmVcCrossConnectExtEntry")
)
zhoneAtmVcCrossConnectExtEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())

# Managed Objects groups

zhoneAtmVclExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 1)
)
zhoneAtmVclExtGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtFaultDetectionType"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtOamF5Ping"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtOamF5PingStatus"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtTrafficContainerIndex"))
)
if mibBuilder.loadTexts:
    zhoneAtmVclExtGroup.setStatus("current")

zhoneAtmTrafficDescrParamExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 3)
)
zhoneAtmTrafficDescrParamExtGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmTrafficDescrParamExtTrnkVclRate"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmTrafficDescrParamExtCacDivider"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmTrafficDescrParamExtUsageParameterControl"))
)
if mibBuilder.loadTexts:
    zhoneAtmTrafficDescrParamExtGroup.setStatus("current")

zhoneAtmStatsExtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 4)
)
zhoneAtmStatsExtTableGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalInitialCellsRx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFabricCellsRx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFinalCLP0CellsRx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFinalCLP1CellsRx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFabricCellsTx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFinalCLP0CellsTx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalFinalCLP1CellsTx"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmStatsTotalInitialCellsTx"))
)
if mibBuilder.loadTexts:
    zhoneAtmStatsExtTableGroup.setStatus("current")

zhoneAtmVclRateExtParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 5)
)
zhoneAtmVclRateExtParamGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam1"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam3"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam4"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam5"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam6"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam7"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam8"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam9"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam10"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam11"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam12"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam13"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam14"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam15"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam16"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam1Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam2Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam3Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam4Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam5Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam6Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam7Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam8Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam9Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam10Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam11Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam12Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam13Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam14Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam15Grp2"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclRateExtParam16Grp2"))
)
if mibBuilder.loadTexts:
    zhoneAtmVclRateExtParamGroup.setStatus("current")

zhoneAtmVplExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 6)
)
zhoneAtmVplExtGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmVplExtFaultDetectionType"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVplExtTrafficContainerIndex"))
)
if mibBuilder.loadTexts:
    zhoneAtmVplExtGroup.setStatus("current")

zhoneAtmConnectionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 7)
)
zhoneAtmConnectionStatsGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmConnectionsAvailable"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmConnectionsAllocated"))
)
if mibBuilder.loadTexts:
    zhoneAtmConnectionStatsGroup.setStatus("current")

zhoneAtmVpiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 8)
)
zhoneAtmVpiGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmVpiMaxVci"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiSwitched"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiRowStatus"),
        ("ZHONE-COM-ATM-MIB", "atmVpi"),
        ("ZHONE-COM-ATM-MIB", "atmVci"),
        ("ZHONE-COM-ATM-MIB", "atmVpiAutoCreateDone"),
        ("ZHONE-COM-ATM-MIB", "atmVpiAutoCreateCount"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiOamF4Ping"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiOamF4PingStatus"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiMaxVciPerVp"))
)
if mibBuilder.loadTexts:
    zhoneAtmVpiGroup.setStatus("current")

zhoneAtmPonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 9)
)
zhoneAtmPonGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "zhoneAtmVclPonTrafficContainerIndex"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVplPonTrafficContainerIndex"))
)
if mibBuilder.loadTexts:
    zhoneAtmPonGroup.setStatus("deprecated")

zhoneAtmVclMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 10)
)
zhoneAtmVclMulticastGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapIndexNext"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapRoutingDomain"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapMulticastAddress"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapIfIndex"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapVpi"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapVci"),
        ("ZHONE-COM-ATM-MIB", "atmVclToMulticastMapRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneAtmVclMulticastGroup.setStatus("current")


# Notification objects

atmVclOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 1)
)
atmVclOperStatusChange.setObjects(
      *(("ATM-MIB", "atmVclAdminStatus"),
        ("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclLastChange"))
)
if mibBuilder.loadTexts:
    atmVclOperStatusChange.setStatus(
        "current"
    )

atmDsx3PlcpAlarmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 2)
)
atmDsx3PlcpAlarmStatusChange.setObjects(
    ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState")
)
if mibBuilder.loadTexts:
    atmDsx3PlcpAlarmStatusChange.setStatus(
        "current"
    )

atmInterfaceTCAlarmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 3)
)
atmInterfaceTCAlarmStateChange.setObjects(
    ("ATM-MIB", "atmInterfaceTCAlarmState")
)
if mibBuilder.loadTexts:
    atmInterfaceTCAlarmStateChange.setStatus(
        "current"
    )

atmVclBandwidthUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 4)
)
atmVclBandwidthUnavailable.setObjects(
      *(("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"))
)
if mibBuilder.loadTexts:
    atmVclBandwidthUnavailable.setStatus(
        "current"
    )

atmVplOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 5)
)
atmVplOperStatusChange.setObjects(
      *(("ATM-MIB", "atmVplAdminStatus"),
        ("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplLastChange"))
)
if mibBuilder.loadTexts:
    atmVplOperStatusChange.setStatus(
        "current"
    )

atmOamF5PingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 6)
)
atmOamF5PingStatus.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZHONE-COM-ATM-MIB", "atmVpi"),
        ("ZHONE-COM-ATM-MIB", "atmVci"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtOamF5PingStatus"))
)
if mibBuilder.loadTexts:
    atmOamF5PingStatus.setStatus(
        "current"
    )

atmVpiAutoCreateComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 7)
)
atmVpiAutoCreateComplete.setObjects(
      *(("ZHONE-COM-ATM-MIB", "atmVpiAutoCreateDone"),
        ("ZHONE-COM-ATM-MIB", "atmVpiAutoCreateCount"))
)
if mibBuilder.loadTexts:
    atmVpiAutoCreateComplete.setStatus(
        "current"
    )

atmOamF4PingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 8)
)
atmOamF4PingStatus.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZHONE-COM-ATM-MIB", "atmVpi"),
        ("ZHONE-COM-ATM-MIB", "atmVci"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVpiOamF4PingStatus"))
)
if mibBuilder.loadTexts:
    atmOamF4PingStatus.setStatus(
        "current"
    )

atmVclExtOamF4PingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 2, 0, 9)
)
atmVclExtOamF4PingStatus.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZHONE-COM-ATM-MIB", "atmVpi"),
        ("ZHONE-COM-ATM-MIB", "atmVci"),
        ("ZHONE-COM-ATM-MIB", "zhoneAtmVclExtOamF4PingStatus"))
)
if mibBuilder.loadTexts:
    atmVclExtOamF4PingStatus.setStatus(
        "current"
    )


# Notifications groups

zhoneAtmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 2, 2, 3, 2)
)
zhoneAtmTrapsGroup.setObjects(
      *(("ZHONE-COM-ATM-MIB", "atmVclOperStatusChange"),
        ("ZHONE-COM-ATM-MIB", "atmDsx3PlcpAlarmStatusChange"),
        ("ZHONE-COM-ATM-MIB", "atmInterfaceTCAlarmStateChange"),
        ("ZHONE-COM-ATM-MIB", "atmVclBandwidthUnavailable"),
        ("ZHONE-COM-ATM-MIB", "atmVplOperStatusChange"),
        ("ZHONE-COM-ATM-MIB", "atmOamF5PingStatus"),
        ("ZHONE-COM-ATM-MIB", "atmVpiAutoCreateComplete"),
        ("ZHONE-COM-ATM-MIB", "atmOamF4PingStatus"))
)
if mibBuilder.loadTexts:
    zhoneAtmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-ATM-MIB",
    **{"zhoneAtmExtension": zhoneAtmExtension,
       "zhoneAtmVclExtTable": zhoneAtmVclExtTable,
       "zhoneAtmVclExtEntry": zhoneAtmVclExtEntry,
       "zhoneAtmVclExtFaultDetectionType": zhoneAtmVclExtFaultDetectionType,
       "zhoneAtmVclExtOamF5Ping": zhoneAtmVclExtOamF5Ping,
       "zhoneAtmVclExtOamF5PingStatus": zhoneAtmVclExtOamF5PingStatus,
       "zhoneAtmVclExtTrafficContainerIndex": zhoneAtmVclExtTrafficContainerIndex,
       "zhoneAtmVclExtOamF4Ping": zhoneAtmVclExtOamF4Ping,
       "zhoneAtmVclExtOamF4PingStatus": zhoneAtmVclExtOamF4PingStatus,
       "zhoneAtmTraps": zhoneAtmTraps,
       "zhoneAtmV2Traps": zhoneAtmV2Traps,
       "atmVclOperStatusChange": atmVclOperStatusChange,
       "atmDsx3PlcpAlarmStatusChange": atmDsx3PlcpAlarmStatusChange,
       "atmInterfaceTCAlarmStateChange": atmInterfaceTCAlarmStateChange,
       "atmVclBandwidthUnavailable": atmVclBandwidthUnavailable,
       "atmVplOperStatusChange": atmVplOperStatusChange,
       "atmOamF5PingStatus": atmOamF5PingStatus,
       "atmVpiAutoCreateComplete": atmVpiAutoCreateComplete,
       "atmOamF4PingStatus": atmOamF4PingStatus,
       "atmVclExtOamF4PingStatus": atmVclExtOamF4PingStatus,
       "zhoneAtmGroups": zhoneAtmGroups,
       "zhoneAtmVclExtGroup": zhoneAtmVclExtGroup,
       "zhoneAtmTrapsGroup": zhoneAtmTrapsGroup,
       "zhoneAtmTrafficDescrParamExtGroup": zhoneAtmTrafficDescrParamExtGroup,
       "zhoneAtmStatsExtTableGroup": zhoneAtmStatsExtTableGroup,
       "zhoneAtmVclRateExtParamGroup": zhoneAtmVclRateExtParamGroup,
       "zhoneAtmVplExtGroup": zhoneAtmVplExtGroup,
       "zhoneAtmConnectionStatsGroup": zhoneAtmConnectionStatsGroup,
       "zhoneAtmVpiGroup": zhoneAtmVpiGroup,
       "zhoneAtmPonGroup": zhoneAtmPonGroup,
       "zhoneAtmVclMulticastGroup": zhoneAtmVclMulticastGroup,
       "zhoneAtmTrafficDescrParamExtTable": zhoneAtmTrafficDescrParamExtTable,
       "zhoneAtmTrafficDescrParamExtEntry": zhoneAtmTrafficDescrParamExtEntry,
       "zhoneAtmTrafficDescrParamExtTrnkVclRate": zhoneAtmTrafficDescrParamExtTrnkVclRate,
       "zhoneAtmTrafficDescrParamExtCacDivider": zhoneAtmTrafficDescrParamExtCacDivider,
       "zhoneAtmTrafficDescrParamExtUsageParameterControl": zhoneAtmTrafficDescrParamExtUsageParameterControl,
       "zhoneAtmStatsExtTable": zhoneAtmStatsExtTable,
       "zhoneAtmStatsExtEntry": zhoneAtmStatsExtEntry,
       "zhoneAtmStatsTotalInitialCellsRx": zhoneAtmStatsTotalInitialCellsRx,
       "zhoneAtmStatsTotalFabricCellsRx": zhoneAtmStatsTotalFabricCellsRx,
       "zhoneAtmStatsTotalFinalCLP0CellsRx": zhoneAtmStatsTotalFinalCLP0CellsRx,
       "zhoneAtmStatsTotalFinalCLP1CellsRx": zhoneAtmStatsTotalFinalCLP1CellsRx,
       "zhoneAtmStatsTotalInitialCellsTx": zhoneAtmStatsTotalInitialCellsTx,
       "zhoneAtmStatsTotalFabricCellsTx": zhoneAtmStatsTotalFabricCellsTx,
       "zhoneAtmStatsTotalFinalCLP0CellsTx": zhoneAtmStatsTotalFinalCLP0CellsTx,
       "zhoneAtmStatsTotalFinalCLP1CellsTx": zhoneAtmStatsTotalFinalCLP1CellsTx,
       "zhoneAtmVclRateExtParam": zhoneAtmVclRateExtParam,
       "zhoneAtmVclRateExtParam1": zhoneAtmVclRateExtParam1,
       "zhoneAtmVclRateExtParam2": zhoneAtmVclRateExtParam2,
       "zhoneAtmVclRateExtParam3": zhoneAtmVclRateExtParam3,
       "zhoneAtmVclRateExtParam4": zhoneAtmVclRateExtParam4,
       "zhoneAtmVclRateExtParam5": zhoneAtmVclRateExtParam5,
       "zhoneAtmVclRateExtParam6": zhoneAtmVclRateExtParam6,
       "zhoneAtmVclRateExtParam7": zhoneAtmVclRateExtParam7,
       "zhoneAtmVclRateExtParam8": zhoneAtmVclRateExtParam8,
       "zhoneAtmVclRateExtParam9": zhoneAtmVclRateExtParam9,
       "zhoneAtmVclRateExtParam10": zhoneAtmVclRateExtParam10,
       "zhoneAtmVclRateExtParam11": zhoneAtmVclRateExtParam11,
       "zhoneAtmVclRateExtParam12": zhoneAtmVclRateExtParam12,
       "zhoneAtmVclRateExtParam13": zhoneAtmVclRateExtParam13,
       "zhoneAtmVclRateExtParam14": zhoneAtmVclRateExtParam14,
       "zhoneAtmVclRateExtParam15": zhoneAtmVclRateExtParam15,
       "zhoneAtmVclRateExtParam16": zhoneAtmVclRateExtParam16,
       "zhoneAtmVclRateExtParam1Grp2": zhoneAtmVclRateExtParam1Grp2,
       "zhoneAtmVclRateExtParam2Grp2": zhoneAtmVclRateExtParam2Grp2,
       "zhoneAtmVclRateExtParam3Grp2": zhoneAtmVclRateExtParam3Grp2,
       "zhoneAtmVclRateExtParam4Grp2": zhoneAtmVclRateExtParam4Grp2,
       "zhoneAtmVclRateExtParam5Grp2": zhoneAtmVclRateExtParam5Grp2,
       "zhoneAtmVclRateExtParam6Grp2": zhoneAtmVclRateExtParam6Grp2,
       "zhoneAtmVclRateExtParam7Grp2": zhoneAtmVclRateExtParam7Grp2,
       "zhoneAtmVclRateExtParam8Grp2": zhoneAtmVclRateExtParam8Grp2,
       "zhoneAtmVclRateExtParam9Grp2": zhoneAtmVclRateExtParam9Grp2,
       "zhoneAtmVclRateExtParam10Grp2": zhoneAtmVclRateExtParam10Grp2,
       "zhoneAtmVclRateExtParam11Grp2": zhoneAtmVclRateExtParam11Grp2,
       "zhoneAtmVclRateExtParam12Grp2": zhoneAtmVclRateExtParam12Grp2,
       "zhoneAtmVclRateExtParam13Grp2": zhoneAtmVclRateExtParam13Grp2,
       "zhoneAtmVclRateExtParam14Grp2": zhoneAtmVclRateExtParam14Grp2,
       "zhoneAtmVclRateExtParam15Grp2": zhoneAtmVclRateExtParam15Grp2,
       "zhoneAtmVclRateExtParam16Grp2": zhoneAtmVclRateExtParam16Grp2,
       "zhoneAtmVplExtTable": zhoneAtmVplExtTable,
       "zhoneAtmVplExtEntry": zhoneAtmVplExtEntry,
       "zhoneAtmVplExtFaultDetectionType": zhoneAtmVplExtFaultDetectionType,
       "zhoneAtmVplExtTrafficContainerIndex": zhoneAtmVplExtTrafficContainerIndex,
       "zhoneAtmConnectionStatsTable": zhoneAtmConnectionStatsTable,
       "zhoneAtmConnectionStatsEntry": zhoneAtmConnectionStatsEntry,
       "zhoneAtmConnectionsAvailable": zhoneAtmConnectionsAvailable,
       "zhoneAtmConnectionsAllocated": zhoneAtmConnectionsAllocated,
       "zhoneAtmVpiTable": zhoneAtmVpiTable,
       "zhoneAtmVpiEntry": zhoneAtmVpiEntry,
       "zhoneAtmVpiMaxVci": zhoneAtmVpiMaxVci,
       "zhoneAtmVpiSwitched": zhoneAtmVpiSwitched,
       "zhoneAtmVpiRowStatus": zhoneAtmVpiRowStatus,
       "zhoneAtmVpiOamF4Ping": zhoneAtmVpiOamF4Ping,
       "zhoneAtmVpiOamF4PingStatus": zhoneAtmVpiOamF4PingStatus,
       "zhoneAtmVpiMaxVciPerVp": zhoneAtmVpiMaxVciPerVp,
       "atmVpi": atmVpi,
       "atmVci": atmVci,
       "atmVpiAutoCreateDone": atmVpiAutoCreateDone,
       "atmVpiAutoCreateCount": atmVpiAutoCreateCount,
       "atmVclToMulticastMap": atmVclToMulticastMap,
       "atmVclToMulticastMapIndexNext": atmVclToMulticastMapIndexNext,
       "atmVclToMulticastMapTable": atmVclToMulticastMapTable,
       "atmVclToMulticastMapEntry": atmVclToMulticastMapEntry,
       "atmVclToMulticastMapIndex": atmVclToMulticastMapIndex,
       "atmVclToMulticastMapRoutingDomain": atmVclToMulticastMapRoutingDomain,
       "atmVclToMulticastMapMulticastAddress": atmVclToMulticastMapMulticastAddress,
       "atmVclToMulticastMapIfIndex": atmVclToMulticastMapIfIndex,
       "atmVclToMulticastMapVpi": atmVclToMulticastMapVpi,
       "atmVclToMulticastMapVci": atmVclToMulticastMapVci,
       "atmVclToMulticastMapRowStatus": atmVclToMulticastMapRowStatus,
       "zhoneAtmPonExtTable": zhoneAtmPonExtTable,
       "zhoneAtmPonExtEntry": zhoneAtmPonExtEntry,
       "zhoneAtmVclPonTrafficContainerIndex": zhoneAtmVclPonTrafficContainerIndex,
       "zhoneAtmVplPonExtTable": zhoneAtmVplPonExtTable,
       "zhoneAtmVplPonExtEntry": zhoneAtmVplPonExtEntry,
       "zhoneAtmVplPonTrafficContainerIndex": zhoneAtmVplPonTrafficContainerIndex,
       "zhoneAtmInterfaceTcExtTable": zhoneAtmInterfaceTcExtTable,
       "zhoneAtmInterfaceTcExtEntry": zhoneAtmInterfaceTcExtEntry,
       "zhoneAtmInterfaceNCDEvents": zhoneAtmInterfaceNCDEvents,
       "zhoneAtmInterfaceHECEvents": zhoneAtmInterfaceHECEvents,
       "zhoneAtmInterfaceFeOCDEvents": zhoneAtmInterfaceFeOCDEvents,
       "zhoneAtmInterfaceFeNCDEvents": zhoneAtmInterfaceFeNCDEvents,
       "zhoneAtmInterfaceFeHECEvents": zhoneAtmInterfaceFeHECEvents,
       "zhoneAtmVcCrossConnectExtTable": zhoneAtmVcCrossConnectExtTable,
       "zhoneAtmVcCrossConnectExtEntry": zhoneAtmVcCrossConnectExtEntry,
       "zhoneAtmVcCrossConnectExtHandleId": zhoneAtmVcCrossConnectExtHandleId,
       "comAtmExtension": comAtmExtension}
)
