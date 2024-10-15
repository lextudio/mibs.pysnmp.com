# SNMP MIB module (IPAD-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:39 2024
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

(ipad,) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipad")

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


# MODULE-IDENTITY

ipadAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadAtmParms_ObjectIdentity = ObjectIdentity
ipadAtmParms = _IpadAtmParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1)
)
_IpadAtmTable_Object = MibTable
ipadAtmTable = _IpadAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    ipadAtmTable.setStatus("current")
_IpadAtmTableEntry_Object = MibTableRow
ipadAtmTableEntry = _IpadAtmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1)
)
ipadAtmTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmIfIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmTableEntry.setStatus("current")
_IpadAtmIfIndex_Type = Integer32
_IpadAtmIfIndex_Object = MibTableColumn
ipadAtmIfIndex = _IpadAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 1),
    _IpadAtmIfIndex_Type()
)
ipadAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmIfIndex.setStatus("current")


class _IpadAtmOperStatus_Type(Integer32):
    """Custom type ipadAtmOperStatus based on Integer32"""
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
        *(("down", 2),
          ("other", 1),
          ("upCellSync", 4),
          ("upNoCellSync", 3))
    )


_IpadAtmOperStatus_Type.__name__ = "Integer32"
_IpadAtmOperStatus_Object = MibTableColumn
ipadAtmOperStatus = _IpadAtmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 2),
    _IpadAtmOperStatus_Type()
)
ipadAtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmOperStatus.setStatus("current")
_IpadAtmVccsOpenedOK_Type = Integer32
_IpadAtmVccsOpenedOK_Object = MibTableColumn
ipadAtmVccsOpenedOK = _IpadAtmVccsOpenedOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 3),
    _IpadAtmVccsOpenedOK_Type()
)
ipadAtmVccsOpenedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccsOpenedOK.setStatus("current")
_IpadAtmVccsNotOpened_Type = Integer32
_IpadAtmVccsNotOpened_Object = MibTableColumn
ipadAtmVccsNotOpened = _IpadAtmVccsNotOpened_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 4),
    _IpadAtmVccsNotOpened_Type()
)
ipadAtmVccsNotOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccsNotOpened.setStatus("current")


class _IpadAtmAlarmReset_Type(Integer32):
    """Custom type ipadAtmAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarms", 2),
          ("clearStats", 3),
          ("other", 1))
    )


_IpadAtmAlarmReset_Type.__name__ = "Integer32"
_IpadAtmAlarmReset_Object = MibTableColumn
ipadAtmAlarmReset = _IpadAtmAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 5),
    _IpadAtmAlarmReset_Type()
)
ipadAtmAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmAlarmReset.setStatus("current")


class _IpadAtmOverSubscriptionFactor_Type(Integer32):
    """Custom type ipadAtmOverSubscriptionFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpadAtmOverSubscriptionFactor_Type.__name__ = "Integer32"
_IpadAtmOverSubscriptionFactor_Object = MibTableColumn
ipadAtmOverSubscriptionFactor = _IpadAtmOverSubscriptionFactor_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 6),
    _IpadAtmOverSubscriptionFactor_Type()
)
ipadAtmOverSubscriptionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmOverSubscriptionFactor.setStatus("current")
_IpadAtmLineBandwidth_Type = Integer32
_IpadAtmLineBandwidth_Object = MibTableColumn
ipadAtmLineBandwidth = _IpadAtmLineBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 7),
    _IpadAtmLineBandwidth_Type()
)
ipadAtmLineBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmLineBandwidth.setStatus("current")
_IpadAtmAAL5Bandwidth_Type = Integer32
_IpadAtmAAL5Bandwidth_Object = MibTableColumn
ipadAtmAAL5Bandwidth = _IpadAtmAAL5Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 8),
    _IpadAtmAAL5Bandwidth_Type()
)
ipadAtmAAL5Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmAAL5Bandwidth.setStatus("current")
_IpadAtmOverSubBandwidth_Type = Integer32
_IpadAtmOverSubBandwidth_Object = MibTableColumn
ipadAtmOverSubBandwidth = _IpadAtmOverSubBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 9),
    _IpadAtmOverSubBandwidth_Type()
)
ipadAtmOverSubBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmOverSubBandwidth.setStatus("current")
_IpadAtmCbrUsedBandwidth_Type = Integer32
_IpadAtmCbrUsedBandwidth_Object = MibTableColumn
ipadAtmCbrUsedBandwidth = _IpadAtmCbrUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 10),
    _IpadAtmCbrUsedBandwidth_Type()
)
ipadAtmCbrUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmCbrUsedBandwidth.setStatus("current")
_IpadAtmVbrUsedBandwidth_Type = Integer32
_IpadAtmVbrUsedBandwidth_Object = MibTableColumn
ipadAtmVbrUsedBandwidth = _IpadAtmVbrUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 11),
    _IpadAtmVbrUsedBandwidth_Type()
)
ipadAtmVbrUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVbrUsedBandwidth.setStatus("current")
_IpadAtmUbrUsedBandwidth_Type = Integer32
_IpadAtmUbrUsedBandwidth_Object = MibTableColumn
ipadAtmUbrUsedBandwidth = _IpadAtmUbrUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 12),
    _IpadAtmUbrUsedBandwidth_Type()
)
ipadAtmUbrUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmUbrUsedBandwidth.setStatus("current")
_IpadAtmQos0Pcr_Type = Integer32
_IpadAtmQos0Pcr_Object = MibTableColumn
ipadAtmQos0Pcr = _IpadAtmQos0Pcr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 1, 1, 1, 13),
    _IpadAtmQos0Pcr_Type()
)
ipadAtmQos0Pcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmQos0Pcr.setStatus("current")
_IpadAtmStatsParms_ObjectIdentity = ObjectIdentity
ipadAtmStatsParms = _IpadAtmStatsParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2)
)
_IpadAtmStatsTable_Object = MibTable
ipadAtmStatsTable = _IpadAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    ipadAtmStatsTable.setStatus("current")
_IpadAtmStatsTableEntry_Object = MibTableRow
ipadAtmStatsTableEntry = _IpadAtmStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1)
)
ipadAtmStatsTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmStatsIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmStatsPeriodIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmStatsTableEntry.setStatus("current")
_IpadAtmStatsIndex_Type = Integer32
_IpadAtmStatsIndex_Object = MibTableColumn
ipadAtmStatsIndex = _IpadAtmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 1),
    _IpadAtmStatsIndex_Type()
)
ipadAtmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsIndex.setStatus("current")
_IpadAtmStatsPeriodIndex_Type = Integer32
_IpadAtmStatsPeriodIndex_Object = MibTableColumn
ipadAtmStatsPeriodIndex = _IpadAtmStatsPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 2),
    _IpadAtmStatsPeriodIndex_Type()
)
ipadAtmStatsPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsPeriodIndex.setStatus("current")
_IpadAtmStatsTimeStamp_Type = TimeTicks
_IpadAtmStatsTimeStamp_Object = MibTableColumn
ipadAtmStatsTimeStamp = _IpadAtmStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 3),
    _IpadAtmStatsTimeStamp_Type()
)
ipadAtmStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsTimeStamp.setStatus("current")
_IpadAtmStatsRxFramesOK_Type = Integer32
_IpadAtmStatsRxFramesOK_Object = MibTableColumn
ipadAtmStatsRxFramesOK = _IpadAtmStatsRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 4),
    _IpadAtmStatsRxFramesOK_Type()
)
ipadAtmStatsRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsRxFramesOK.setStatus("current")
_IpadAtmStatsTxFramesOK_Type = Integer32
_IpadAtmStatsTxFramesOK_Object = MibTableColumn
ipadAtmStatsTxFramesOK = _IpadAtmStatsTxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 5),
    _IpadAtmStatsTxFramesOK_Type()
)
ipadAtmStatsTxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsTxFramesOK.setStatus("current")
_IpadAtmStatsRxFramesError_Type = Integer32
_IpadAtmStatsRxFramesError_Object = MibTableColumn
ipadAtmStatsRxFramesError = _IpadAtmStatsRxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 6),
    _IpadAtmStatsRxFramesError_Type()
)
ipadAtmStatsRxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsRxFramesError.setStatus("current")
_IpadAtmStatsTxFramesError_Type = Integer32
_IpadAtmStatsTxFramesError_Object = MibTableColumn
ipadAtmStatsTxFramesError = _IpadAtmStatsTxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 7),
    _IpadAtmStatsTxFramesError_Type()
)
ipadAtmStatsTxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsTxFramesError.setStatus("current")
_IpadAtmStatsRxBytesOK_Type = Integer32
_IpadAtmStatsRxBytesOK_Object = MibTableColumn
ipadAtmStatsRxBytesOK = _IpadAtmStatsRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 8),
    _IpadAtmStatsRxBytesOK_Type()
)
ipadAtmStatsRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsRxBytesOK.setStatus("current")
_IpadAtmStatsTxBytesOK_Type = Integer32
_IpadAtmStatsTxBytesOK_Object = MibTableColumn
ipadAtmStatsTxBytesOK = _IpadAtmStatsTxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 9),
    _IpadAtmStatsTxBytesOK_Type()
)
ipadAtmStatsTxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsTxBytesOK.setStatus("current")
_IpadAtmStatsLostSync_Type = Integer32
_IpadAtmStatsLostSync_Object = MibTableColumn
ipadAtmStatsLostSync = _IpadAtmStatsLostSync_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 10),
    _IpadAtmStatsLostSync_Type()
)
ipadAtmStatsLostSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsLostSync.setStatus("current")
_IpadAtmStatsOamCellsRx_Type = Integer32
_IpadAtmStatsOamCellsRx_Object = MibTableColumn
ipadAtmStatsOamCellsRx = _IpadAtmStatsOamCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 11),
    _IpadAtmStatsOamCellsRx_Type()
)
ipadAtmStatsOamCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsOamCellsRx.setStatus("current")
_IpadAtmStatsOamCellsTx_Type = Integer32
_IpadAtmStatsOamCellsTx_Object = MibTableColumn
ipadAtmStatsOamCellsTx = _IpadAtmStatsOamCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 2, 1, 1, 12),
    _IpadAtmStatsOamCellsTx_Type()
)
ipadAtmStatsOamCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmStatsOamCellsTx.setStatus("current")
_IpadAtmVccParms_ObjectIdentity = ObjectIdentity
ipadAtmVccParms = _IpadAtmVccParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3)
)
_IpadAtmVccTable_Object = MibTable
ipadAtmVccTable = _IpadAtmVccTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1)
)
if mibBuilder.loadTexts:
    ipadAtmVccTable.setStatus("current")
_IpadAtmVccTableEntry_Object = MibTableRow
ipadAtmVccTableEntry = _IpadAtmVccTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1)
)
ipadAtmVccTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmVccIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmVccVpiIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmVccVciIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmVccTableEntry.setStatus("current")
_IpadAtmVccIndex_Type = Integer32
_IpadAtmVccIndex_Object = MibTableColumn
ipadAtmVccIndex = _IpadAtmVccIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 1),
    _IpadAtmVccIndex_Type()
)
ipadAtmVccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccIndex.setStatus("current")
_IpadAtmVccVpiIndex_Type = Integer32
_IpadAtmVccVpiIndex_Object = MibTableColumn
ipadAtmVccVpiIndex = _IpadAtmVccVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 2),
    _IpadAtmVccVpiIndex_Type()
)
ipadAtmVccVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccVpiIndex.setStatus("current")
_IpadAtmVccVciIndex_Type = Integer32
_IpadAtmVccVciIndex_Object = MibTableColumn
ipadAtmVccVciIndex = _IpadAtmVccVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 3),
    _IpadAtmVccVciIndex_Type()
)
ipadAtmVccVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccVciIndex.setStatus("current")


class _IpadAtmVccEncapsulationType_Type(Integer32):
    """Custom type ipadAtmVccEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("frf5", 6),
          ("frf8", 7),
          ("llcMux", 4),
          ("other", 1),
          ("serialHDLCoA", 5),
          ("serialPPPoA", 2),
          ("vcMux", 3))
    )


_IpadAtmVccEncapsulationType_Type.__name__ = "Integer32"
_IpadAtmVccEncapsulationType_Object = MibTableColumn
ipadAtmVccEncapsulationType = _IpadAtmVccEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 4),
    _IpadAtmVccEncapsulationType_Type()
)
ipadAtmVccEncapsulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccEncapsulationType.setStatus("current")


class _IpadAtmVccTrafficType_Type(Integer32):
    """Custom type ipadAtmVccTrafficType based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_IpadAtmVccTrafficType_Type.__name__ = "Integer32"
_IpadAtmVccTrafficType_Object = MibTableColumn
ipadAtmVccTrafficType = _IpadAtmVccTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 5),
    _IpadAtmVccTrafficType_Type()
)
ipadAtmVccTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccTrafficType.setStatus("current")
_IpadAtmVccChannelRate_Type = Integer32
_IpadAtmVccChannelRate_Object = MibTableColumn
ipadAtmVccChannelRate = _IpadAtmVccChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 6),
    _IpadAtmVccChannelRate_Type()
)
ipadAtmVccChannelRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccChannelRate.setStatus("current")


class _IpadAtmVccAlarmReset_Type(Integer32):
    """Custom type ipadAtmVccAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarms", 2),
          ("clearStats", 3),
          ("other", 1))
    )


_IpadAtmVccAlarmReset_Type.__name__ = "Integer32"
_IpadAtmVccAlarmReset_Object = MibTableColumn
ipadAtmVccAlarmReset = _IpadAtmVccAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 7),
    _IpadAtmVccAlarmReset_Type()
)
ipadAtmVccAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccAlarmReset.setStatus("current")
_IpadAtmVccSLATimer_Type = Integer32
_IpadAtmVccSLATimer_Object = MibTableColumn
ipadAtmVccSLATimer = _IpadAtmVccSLATimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 8),
    _IpadAtmVccSLATimer_Type()
)
ipadAtmVccSLATimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccSLATimer.setStatus("current")
_IpadAtmVccRemoteFramesOffered_Type = Integer32
_IpadAtmVccRemoteFramesOffered_Object = MibTableColumn
ipadAtmVccRemoteFramesOffered = _IpadAtmVccRemoteFramesOffered_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 9),
    _IpadAtmVccRemoteFramesOffered_Type()
)
ipadAtmVccRemoteFramesOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteFramesOffered.setStatus("current")
_IpadAtmVccFramesReceived_Type = Integer32
_IpadAtmVccFramesReceived_Object = MibTableColumn
ipadAtmVccFramesReceived = _IpadAtmVccFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 10),
    _IpadAtmVccFramesReceived_Type()
)
ipadAtmVccFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccFramesReceived.setStatus("current")
_IpadAtmVccRemoteDataOffered_Type = Integer32
_IpadAtmVccRemoteDataOffered_Object = MibTableColumn
ipadAtmVccRemoteDataOffered = _IpadAtmVccRemoteDataOffered_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 11),
    _IpadAtmVccRemoteDataOffered_Type()
)
ipadAtmVccRemoteDataOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteDataOffered.setStatus("current")
_IpadAtmVccDataReceived_Type = Integer32
_IpadAtmVccDataReceived_Object = MibTableColumn
ipadAtmVccDataReceived = _IpadAtmVccDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 12),
    _IpadAtmVccDataReceived_Type()
)
ipadAtmVccDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccDataReceived.setStatus("current")


class _IpadAtmVccRemoteActive_Type(Integer32):
    """Custom type ipadAtmVccRemoteActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("other", 1))
    )


_IpadAtmVccRemoteActive_Type.__name__ = "Integer32"
_IpadAtmVccRemoteActive_Object = MibTableColumn
ipadAtmVccRemoteActive = _IpadAtmVccRemoteActive_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 13),
    _IpadAtmVccRemoteActive_Type()
)
ipadAtmVccRemoteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteActive.setStatus("current")
_IpadAtmVccRemoteVpi_Type = Integer32
_IpadAtmVccRemoteVpi_Object = MibTableColumn
ipadAtmVccRemoteVpi = _IpadAtmVccRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 14),
    _IpadAtmVccRemoteVpi_Type()
)
ipadAtmVccRemoteVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteVpi.setStatus("current")
_IpadAtmVccRemoteVci_Type = Integer32
_IpadAtmVccRemoteVci_Object = MibTableColumn
ipadAtmVccRemoteVci = _IpadAtmVccRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 15),
    _IpadAtmVccRemoteVci_Type()
)
ipadAtmVccRemoteVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteVci.setStatus("current")
_IpadAtmVccRemoteIPAddress_Type = IpAddress
_IpadAtmVccRemoteIPAddress_Object = MibTableColumn
ipadAtmVccRemoteIPAddress = _IpadAtmVccRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 16),
    _IpadAtmVccRemoteIPAddress_Type()
)
ipadAtmVccRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteIPAddress.setStatus("current")
_IpadAtmVccRemoteUnitId_Type = DisplayString
_IpadAtmVccRemoteUnitId_Object = MibTableColumn
ipadAtmVccRemoteUnitId = _IpadAtmVccRemoteUnitId_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 17),
    _IpadAtmVccRemoteUnitId_Type()
)
ipadAtmVccRemoteUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccRemoteUnitId.setStatus("current")


class _IpadAtmVccEtoeLoopbackCommand_Type(Integer32):
    """Custom type ipadAtmVccEtoeLoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2),
          ("stop", 3))
    )


_IpadAtmVccEtoeLoopbackCommand_Type.__name__ = "Integer32"
_IpadAtmVccEtoeLoopbackCommand_Object = MibTableColumn
ipadAtmVccEtoeLoopbackCommand = _IpadAtmVccEtoeLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 18),
    _IpadAtmVccEtoeLoopbackCommand_Type()
)
ipadAtmVccEtoeLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackCommand.setStatus("current")


class _IpadAtmVccEtoeLoopbackState_Type(Integer32):
    """Custom type ipadAtmVccEtoeLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("loopback", 3))
    )


_IpadAtmVccEtoeLoopbackState_Type.__name__ = "Integer32"
_IpadAtmVccEtoeLoopbackState_Object = MibTableColumn
ipadAtmVccEtoeLoopbackState = _IpadAtmVccEtoeLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 19),
    _IpadAtmVccEtoeLoopbackState_Type()
)
ipadAtmVccEtoeLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackState.setStatus("current")
_IpadAtmVccEtoeLoopbackCellsTx_Type = Integer32
_IpadAtmVccEtoeLoopbackCellsTx_Object = MibTableColumn
ipadAtmVccEtoeLoopbackCellsTx = _IpadAtmVccEtoeLoopbackCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 20),
    _IpadAtmVccEtoeLoopbackCellsTx_Type()
)
ipadAtmVccEtoeLoopbackCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackCellsTx.setStatus("current")
_IpadAtmVccEtoeLoopbackCellsRx_Type = Integer32
_IpadAtmVccEtoeLoopbackCellsRx_Object = MibTableColumn
ipadAtmVccEtoeLoopbackCellsRx = _IpadAtmVccEtoeLoopbackCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 21),
    _IpadAtmVccEtoeLoopbackCellsRx_Type()
)
ipadAtmVccEtoeLoopbackCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackCellsRx.setStatus("current")
_IpadAtmVccEtoeLoopbackRttMin_Type = Integer32
_IpadAtmVccEtoeLoopbackRttMin_Object = MibTableColumn
ipadAtmVccEtoeLoopbackRttMin = _IpadAtmVccEtoeLoopbackRttMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 22),
    _IpadAtmVccEtoeLoopbackRttMin_Type()
)
ipadAtmVccEtoeLoopbackRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackRttMin.setStatus("current")
_IpadAtmVccEtoeLoopbackRttMax_Type = Integer32
_IpadAtmVccEtoeLoopbackRttMax_Object = MibTableColumn
ipadAtmVccEtoeLoopbackRttMax = _IpadAtmVccEtoeLoopbackRttMax_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 23),
    _IpadAtmVccEtoeLoopbackRttMax_Type()
)
ipadAtmVccEtoeLoopbackRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackRttMax.setStatus("current")
_IpadAtmVccEtoeLoopbackRttAvg_Type = Integer32
_IpadAtmVccEtoeLoopbackRttAvg_Object = MibTableColumn
ipadAtmVccEtoeLoopbackRttAvg = _IpadAtmVccEtoeLoopbackRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 24),
    _IpadAtmVccEtoeLoopbackRttAvg_Type()
)
ipadAtmVccEtoeLoopbackRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeLoopbackRttAvg.setStatus("current")


class _IpadAtmVccSegLoopbackCommand_Type(Integer32):
    """Custom type ipadAtmVccSegLoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2),
          ("stop", 3))
    )


_IpadAtmVccSegLoopbackCommand_Type.__name__ = "Integer32"
_IpadAtmVccSegLoopbackCommand_Object = MibTableColumn
ipadAtmVccSegLoopbackCommand = _IpadAtmVccSegLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 25),
    _IpadAtmVccSegLoopbackCommand_Type()
)
ipadAtmVccSegLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackCommand.setStatus("current")


class _IpadAtmVccSegLoopbackState_Type(Integer32):
    """Custom type ipadAtmVccSegLoopbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("loopback", 3))
    )


_IpadAtmVccSegLoopbackState_Type.__name__ = "Integer32"
_IpadAtmVccSegLoopbackState_Object = MibTableColumn
ipadAtmVccSegLoopbackState = _IpadAtmVccSegLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 26),
    _IpadAtmVccSegLoopbackState_Type()
)
ipadAtmVccSegLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackState.setStatus("current")
_IpadAtmVccSegLoopbackCellsTx_Type = Integer32
_IpadAtmVccSegLoopbackCellsTx_Object = MibTableColumn
ipadAtmVccSegLoopbackCellsTx = _IpadAtmVccSegLoopbackCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 27),
    _IpadAtmVccSegLoopbackCellsTx_Type()
)
ipadAtmVccSegLoopbackCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackCellsTx.setStatus("current")
_IpadAtmVccSegLoopbackCellsRx_Type = Integer32
_IpadAtmVccSegLoopbackCellsRx_Object = MibTableColumn
ipadAtmVccSegLoopbackCellsRx = _IpadAtmVccSegLoopbackCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 28),
    _IpadAtmVccSegLoopbackCellsRx_Type()
)
ipadAtmVccSegLoopbackCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackCellsRx.setStatus("current")
_IpadAtmVccSegLoopbackRttMin_Type = Integer32
_IpadAtmVccSegLoopbackRttMin_Object = MibTableColumn
ipadAtmVccSegLoopbackRttMin = _IpadAtmVccSegLoopbackRttMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 29),
    _IpadAtmVccSegLoopbackRttMin_Type()
)
ipadAtmVccSegLoopbackRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackRttMin.setStatus("current")
_IpadAtmVccSegLoopbackRttMax_Type = Integer32
_IpadAtmVccSegLoopbackRttMax_Object = MibTableColumn
ipadAtmVccSegLoopbackRttMax = _IpadAtmVccSegLoopbackRttMax_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 30),
    _IpadAtmVccSegLoopbackRttMax_Type()
)
ipadAtmVccSegLoopbackRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackRttMax.setStatus("current")
_IpadAtmVccSegLoopbackRttAvg_Type = Integer32
_IpadAtmVccSegLoopbackRttAvg_Object = MibTableColumn
ipadAtmVccSegLoopbackRttAvg = _IpadAtmVccSegLoopbackRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 31),
    _IpadAtmVccSegLoopbackRttAvg_Type()
)
ipadAtmVccSegLoopbackRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccSegLoopbackRttAvg.setStatus("current")


class _IpadAtmVccEtoeContCheckCommand_Type(Integer32):
    """Custom type ipadAtmVccEtoeContCheckCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("deactivate", 3),
          ("other", 1))
    )


_IpadAtmVccEtoeContCheckCommand_Type.__name__ = "Integer32"
_IpadAtmVccEtoeContCheckCommand_Object = MibTableColumn
ipadAtmVccEtoeContCheckCommand = _IpadAtmVccEtoeContCheckCommand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 32),
    _IpadAtmVccEtoeContCheckCommand_Type()
)
ipadAtmVccEtoeContCheckCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckCommand.setStatus("current")


class _IpadAtmVccEtoeContCheckAutoActivate_Type(Integer32):
    """Custom type ipadAtmVccEtoeContCheckAutoActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadAtmVccEtoeContCheckAutoActivate_Type.__name__ = "Integer32"
_IpadAtmVccEtoeContCheckAutoActivate_Object = MibTableColumn
ipadAtmVccEtoeContCheckAutoActivate = _IpadAtmVccEtoeContCheckAutoActivate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 33),
    _IpadAtmVccEtoeContCheckAutoActivate_Type()
)
ipadAtmVccEtoeContCheckAutoActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckAutoActivate.setStatus("current")


class _IpadAtmVccEtoeContCheckType_Type(Integer32):
    """Custom type ipadAtmVccEtoeContCheckType based on Integer32"""
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
        *(("none", 1),
          ("sink", 2),
          ("sinkAndSource", 4),
          ("source", 3))
    )


_IpadAtmVccEtoeContCheckType_Type.__name__ = "Integer32"
_IpadAtmVccEtoeContCheckType_Object = MibTableColumn
ipadAtmVccEtoeContCheckType = _IpadAtmVccEtoeContCheckType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 34),
    _IpadAtmVccEtoeContCheckType_Type()
)
ipadAtmVccEtoeContCheckType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckType.setStatus("current")


class _IpadAtmVccEtoeContCheckTypeInUse_Type(Integer32):
    """Custom type ipadAtmVccEtoeContCheckTypeInUse based on Integer32"""
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
        *(("none", 1),
          ("sink", 2),
          ("sinkAndSource", 4),
          ("source", 3))
    )


_IpadAtmVccEtoeContCheckTypeInUse_Type.__name__ = "Integer32"
_IpadAtmVccEtoeContCheckTypeInUse_Object = MibTableColumn
ipadAtmVccEtoeContCheckTypeInUse = _IpadAtmVccEtoeContCheckTypeInUse_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 35),
    _IpadAtmVccEtoeContCheckTypeInUse_Type()
)
ipadAtmVccEtoeContCheckTypeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckTypeInUse.setStatus("current")


class _IpadAtmVccEtoeContCheckStatus_Type(Integer32):
    """Custom type ipadAtmVccEtoeContCheckStatus based on Integer32"""
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
        *(("activating", 4),
          ("activationFailed", 3),
          ("active", 2),
          ("deactivating", 5),
          ("ready", 1))
    )


_IpadAtmVccEtoeContCheckStatus_Type.__name__ = "Integer32"
_IpadAtmVccEtoeContCheckStatus_Object = MibTableColumn
ipadAtmVccEtoeContCheckStatus = _IpadAtmVccEtoeContCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 36),
    _IpadAtmVccEtoeContCheckStatus_Type()
)
ipadAtmVccEtoeContCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckStatus.setStatus("current")
_IpadAtmVccEtoeContCheckCellsTx_Type = Integer32
_IpadAtmVccEtoeContCheckCellsTx_Object = MibTableColumn
ipadAtmVccEtoeContCheckCellsTx = _IpadAtmVccEtoeContCheckCellsTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 37),
    _IpadAtmVccEtoeContCheckCellsTx_Type()
)
ipadAtmVccEtoeContCheckCellsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckCellsTx.setStatus("current")
_IpadAtmVccEtoeContCheckCellsRx_Type = Integer32
_IpadAtmVccEtoeContCheckCellsRx_Object = MibTableColumn
ipadAtmVccEtoeContCheckCellsRx = _IpadAtmVccEtoeContCheckCellsRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 38),
    _IpadAtmVccEtoeContCheckCellsRx_Type()
)
ipadAtmVccEtoeContCheckCellsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeContCheckCellsRx.setStatus("current")


class _IpadAtmVccEtoeAisStatus_Type(Integer32):
    """Custom type ipadAtmVccEtoeAisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("noAis", 1))
    )


_IpadAtmVccEtoeAisStatus_Type.__name__ = "Integer32"
_IpadAtmVccEtoeAisStatus_Object = MibTableColumn
ipadAtmVccEtoeAisStatus = _IpadAtmVccEtoeAisStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 39),
    _IpadAtmVccEtoeAisStatus_Type()
)
ipadAtmVccEtoeAisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeAisStatus.setStatus("current")


class _IpadAtmVccEtoeRdiStatus_Type(Integer32):
    """Custom type ipadAtmVccEtoeRdiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRdi", 1),
          ("rdi", 2))
    )


_IpadAtmVccEtoeRdiStatus_Type.__name__ = "Integer32"
_IpadAtmVccEtoeRdiStatus_Object = MibTableColumn
ipadAtmVccEtoeRdiStatus = _IpadAtmVccEtoeRdiStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 3, 1, 1, 40),
    _IpadAtmVccEtoeRdiStatus_Type()
)
ipadAtmVccEtoeRdiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccEtoeRdiStatus.setStatus("current")
_IpadAtmVccStatsParms_ObjectIdentity = ObjectIdentity
ipadAtmVccStatsParms = _IpadAtmVccStatsParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4)
)
_IpadAtmVccStatsTable_Object = MibTable
ipadAtmVccStatsTable = _IpadAtmVccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1)
)
if mibBuilder.loadTexts:
    ipadAtmVccStatsTable.setStatus("current")
_IpadAtmVccStatsTableEntry_Object = MibTableRow
ipadAtmVccStatsTableEntry = _IpadAtmVccStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1)
)
ipadAtmVccStatsTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmVccStatsIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmVccStatsVpiIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmVccStatsVciIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmVccStatsPeriodIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmVccStatsTableEntry.setStatus("current")
_IpadAtmVccStatsIndex_Type = Integer32
_IpadAtmVccStatsIndex_Object = MibTableColumn
ipadAtmVccStatsIndex = _IpadAtmVccStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 1),
    _IpadAtmVccStatsIndex_Type()
)
ipadAtmVccStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsIndex.setStatus("current")
_IpadAtmVccStatsVpiIndex_Type = Integer32
_IpadAtmVccStatsVpiIndex_Object = MibTableColumn
ipadAtmVccStatsVpiIndex = _IpadAtmVccStatsVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 2),
    _IpadAtmVccStatsVpiIndex_Type()
)
ipadAtmVccStatsVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsVpiIndex.setStatus("current")
_IpadAtmVccStatsVciIndex_Type = Integer32
_IpadAtmVccStatsVciIndex_Object = MibTableColumn
ipadAtmVccStatsVciIndex = _IpadAtmVccStatsVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 3),
    _IpadAtmVccStatsVciIndex_Type()
)
ipadAtmVccStatsVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsVciIndex.setStatus("current")
_IpadAtmVccStatsPeriodIndex_Type = Integer32
_IpadAtmVccStatsPeriodIndex_Object = MibTableColumn
ipadAtmVccStatsPeriodIndex = _IpadAtmVccStatsPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 4),
    _IpadAtmVccStatsPeriodIndex_Type()
)
ipadAtmVccStatsPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsPeriodIndex.setStatus("current")
_IpadAtmVccStatsTimeStamp_Type = TimeTicks
_IpadAtmVccStatsTimeStamp_Object = MibTableColumn
ipadAtmVccStatsTimeStamp = _IpadAtmVccStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 5),
    _IpadAtmVccStatsTimeStamp_Type()
)
ipadAtmVccStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsTimeStamp.setStatus("current")
_IpadAtmVccStatsRxFramesOK_Type = Integer32
_IpadAtmVccStatsRxFramesOK_Object = MibTableColumn
ipadAtmVccStatsRxFramesOK = _IpadAtmVccStatsRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 6),
    _IpadAtmVccStatsRxFramesOK_Type()
)
ipadAtmVccStatsRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesOK.setStatus("current")
_IpadAtmVccStatsTxFramesOK_Type = Integer32
_IpadAtmVccStatsTxFramesOK_Object = MibTableColumn
ipadAtmVccStatsTxFramesOK = _IpadAtmVccStatsTxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 7),
    _IpadAtmVccStatsTxFramesOK_Type()
)
ipadAtmVccStatsTxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsTxFramesOK.setStatus("current")
_IpadAtmVccStatsRxFramesError_Type = Integer32
_IpadAtmVccStatsRxFramesError_Object = MibTableColumn
ipadAtmVccStatsRxFramesError = _IpadAtmVccStatsRxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 8),
    _IpadAtmVccStatsRxFramesError_Type()
)
ipadAtmVccStatsRxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesError.setStatus("current")
_IpadAtmVccStatsTxFramesError_Type = Integer32
_IpadAtmVccStatsTxFramesError_Object = MibTableColumn
ipadAtmVccStatsTxFramesError = _IpadAtmVccStatsTxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 9),
    _IpadAtmVccStatsTxFramesError_Type()
)
ipadAtmVccStatsTxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsTxFramesError.setStatus("current")
_IpadAtmVccStatsRxFramesCLP_Type = Integer32
_IpadAtmVccStatsRxFramesCLP_Object = MibTableColumn
ipadAtmVccStatsRxFramesCLP = _IpadAtmVccStatsRxFramesCLP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 10),
    _IpadAtmVccStatsRxFramesCLP_Type()
)
ipadAtmVccStatsRxFramesCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesCLP.setStatus("current")
_IpadAtmVccStatsRxFramesCI_Type = Integer32
_IpadAtmVccStatsRxFramesCI_Object = MibTableColumn
ipadAtmVccStatsRxFramesCI = _IpadAtmVccStatsRxFramesCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 11),
    _IpadAtmVccStatsRxFramesCI_Type()
)
ipadAtmVccStatsRxFramesCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesCI.setStatus("current")
_IpadAtmVccStatsRxFramesAbort_Type = Integer32
_IpadAtmVccStatsRxFramesAbort_Object = MibTableColumn
ipadAtmVccStatsRxFramesAbort = _IpadAtmVccStatsRxFramesAbort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 12),
    _IpadAtmVccStatsRxFramesAbort_Type()
)
ipadAtmVccStatsRxFramesAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesAbort.setStatus("current")
_IpadAtmVccStatsRxFramesLenViolation_Type = Integer32
_IpadAtmVccStatsRxFramesLenViolation_Object = MibTableColumn
ipadAtmVccStatsRxFramesLenViolation = _IpadAtmVccStatsRxFramesLenViolation_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 13),
    _IpadAtmVccStatsRxFramesLenViolation_Type()
)
ipadAtmVccStatsRxFramesLenViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesLenViolation.setStatus("current")
_IpadAtmVccStatsRxFramesCRCError_Type = Integer32
_IpadAtmVccStatsRxFramesCRCError_Object = MibTableColumn
ipadAtmVccStatsRxFramesCRCError = _IpadAtmVccStatsRxFramesCRCError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 14),
    _IpadAtmVccStatsRxFramesCRCError_Type()
)
ipadAtmVccStatsRxFramesCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesCRCError.setStatus("current")
_IpadAtmVccStatsRxFramesTimeout_Type = Integer32
_IpadAtmVccStatsRxFramesTimeout_Object = MibTableColumn
ipadAtmVccStatsRxFramesTimeout = _IpadAtmVccStatsRxFramesTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 15),
    _IpadAtmVccStatsRxFramesTimeout_Type()
)
ipadAtmVccStatsRxFramesTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesTimeout.setStatus("current")
_IpadAtmVccStatsRxFramesHCSError_Type = Integer32
_IpadAtmVccStatsRxFramesHCSError_Object = MibTableColumn
ipadAtmVccStatsRxFramesHCSError = _IpadAtmVccStatsRxFramesHCSError_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 16),
    _IpadAtmVccStatsRxFramesHCSError_Type()
)
ipadAtmVccStatsRxFramesHCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesHCSError.setStatus("current")
_IpadAtmVccStatsRxFramesNoBuffer_Type = Integer32
_IpadAtmVccStatsRxFramesNoBuffer_Object = MibTableColumn
ipadAtmVccStatsRxFramesNoBuffer = _IpadAtmVccStatsRxFramesNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 17),
    _IpadAtmVccStatsRxFramesNoBuffer_Type()
)
ipadAtmVccStatsRxFramesNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxFramesNoBuffer.setStatus("current")
_IpadAtmVccStatsRxCellsOK_Type = Integer32
_IpadAtmVccStatsRxCellsOK_Object = MibTableColumn
ipadAtmVccStatsRxCellsOK = _IpadAtmVccStatsRxCellsOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 18),
    _IpadAtmVccStatsRxCellsOK_Type()
)
ipadAtmVccStatsRxCellsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxCellsOK.setStatus("current")
_IpadAtmVccStatsTxCellsOK_Type = Integer32
_IpadAtmVccStatsTxCellsOK_Object = MibTableColumn
ipadAtmVccStatsTxCellsOK = _IpadAtmVccStatsTxCellsOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 19),
    _IpadAtmVccStatsTxCellsOK_Type()
)
ipadAtmVccStatsTxCellsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsTxCellsOK.setStatus("current")
_IpadAtmVccStatsRxBytesOK_Type = Integer32
_IpadAtmVccStatsRxBytesOK_Object = MibTableColumn
ipadAtmVccStatsRxBytesOK = _IpadAtmVccStatsRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 20),
    _IpadAtmVccStatsRxBytesOK_Type()
)
ipadAtmVccStatsRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRxBytesOK.setStatus("current")
_IpadAtmVccStatsTxBytesOK_Type = Integer32
_IpadAtmVccStatsTxBytesOK_Object = MibTableColumn
ipadAtmVccStatsTxBytesOK = _IpadAtmVccStatsTxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 21),
    _IpadAtmVccStatsTxBytesOK_Type()
)
ipadAtmVccStatsTxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsTxBytesOK.setStatus("current")
_IpadAtmVccStatsDelayPeak_Type = Integer32
_IpadAtmVccStatsDelayPeak_Object = MibTableColumn
ipadAtmVccStatsDelayPeak = _IpadAtmVccStatsDelayPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 22),
    _IpadAtmVccStatsDelayPeak_Type()
)
ipadAtmVccStatsDelayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsDelayPeak.setStatus("current")
_IpadAtmVccStatsDelayAverage_Type = Integer32
_IpadAtmVccStatsDelayAverage_Object = MibTableColumn
ipadAtmVccStatsDelayAverage = _IpadAtmVccStatsDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 23),
    _IpadAtmVccStatsDelayAverage_Type()
)
ipadAtmVccStatsDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsDelayAverage.setStatus("current")
_IpadAtmVccStatsRoundTripTimeouts_Type = Integer32
_IpadAtmVccStatsRoundTripTimeouts_Object = MibTableColumn
ipadAtmVccStatsRoundTripTimeouts = _IpadAtmVccStatsRoundTripTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 24),
    _IpadAtmVccStatsRoundTripTimeouts_Type()
)
ipadAtmVccStatsRoundTripTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRoundTripTimeouts.setStatus("current")
_IpadAtmVccStatsRemoteFramesOffered_Type = Integer32
_IpadAtmVccStatsRemoteFramesOffered_Object = MibTableColumn
ipadAtmVccStatsRemoteFramesOffered = _IpadAtmVccStatsRemoteFramesOffered_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 25),
    _IpadAtmVccStatsRemoteFramesOffered_Type()
)
ipadAtmVccStatsRemoteFramesOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRemoteFramesOffered.setStatus("current")
_IpadAtmVccStatsFramesReceived_Type = Integer32
_IpadAtmVccStatsFramesReceived_Object = MibTableColumn
ipadAtmVccStatsFramesReceived = _IpadAtmVccStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 26),
    _IpadAtmVccStatsFramesReceived_Type()
)
ipadAtmVccStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsFramesReceived.setStatus("current")
_IpadAtmVccStatsFDR_Type = DisplayString
_IpadAtmVccStatsFDR_Object = MibTableColumn
ipadAtmVccStatsFDR = _IpadAtmVccStatsFDR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 27),
    _IpadAtmVccStatsFDR_Type()
)
ipadAtmVccStatsFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsFDR.setStatus("current")
_IpadAtmVccStatsRemoteDataOffered_Type = Integer32
_IpadAtmVccStatsRemoteDataOffered_Object = MibTableColumn
ipadAtmVccStatsRemoteDataOffered = _IpadAtmVccStatsRemoteDataOffered_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 28),
    _IpadAtmVccStatsRemoteDataOffered_Type()
)
ipadAtmVccStatsRemoteDataOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsRemoteDataOffered.setStatus("current")
_IpadAtmVccStatsDataReceived_Type = Integer32
_IpadAtmVccStatsDataReceived_Object = MibTableColumn
ipadAtmVccStatsDataReceived = _IpadAtmVccStatsDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 29),
    _IpadAtmVccStatsDataReceived_Type()
)
ipadAtmVccStatsDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsDataReceived.setStatus("current")
_IpadAtmVccStatsDDR_Type = DisplayString
_IpadAtmVccStatsDDR_Object = MibTableColumn
ipadAtmVccStatsDDR = _IpadAtmVccStatsDDR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 30),
    _IpadAtmVccStatsDDR_Type()
)
ipadAtmVccStatsDDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsDDR.setStatus("current")
_IpadAtmVccStatsUAS_Type = Integer32
_IpadAtmVccStatsUAS_Object = MibTableColumn
ipadAtmVccStatsUAS = _IpadAtmVccStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 4, 1, 1, 31),
    _IpadAtmVccStatsUAS_Type()
)
ipadAtmVccStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmVccStatsUAS.setStatus("current")
_IpadAtmCesParms_ObjectIdentity = ObjectIdentity
ipadAtmCesParms = _IpadAtmCesParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5)
)
_IpadAtmCesTable_Object = MibTable
ipadAtmCesTable = _IpadAtmCesTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    ipadAtmCesTable.setStatus("current")
_IpadAtmCesTableEntry_Object = MibTableRow
ipadAtmCesTableEntry = _IpadAtmCesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5, 1, 1)
)
ipadAtmCesTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmCesIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmCesTableEntry.setStatus("current")
_IpadAtmCesIndex_Type = Integer32
_IpadAtmCesIndex_Object = MibTableColumn
ipadAtmCesIndex = _IpadAtmCesIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5, 1, 1, 1),
    _IpadAtmCesIndex_Type()
)
ipadAtmCesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmCesIndex.setStatus("current")


class _IpadAtmCesPayloadScrambling_Type(Integer32):
    """Custom type ipadAtmCesPayloadScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadAtmCesPayloadScrambling_Type.__name__ = "Integer32"
_IpadAtmCesPayloadScrambling_Object = MibTableColumn
ipadAtmCesPayloadScrambling = _IpadAtmCesPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5, 1, 1, 2),
    _IpadAtmCesPayloadScrambling_Type()
)
ipadAtmCesPayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmCesPayloadScrambling.setStatus("current")


class _IpadAtmCesAutoChannelConfiguration_Type(Integer32):
    """Custom type ipadAtmCesAutoChannelConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadAtmCesAutoChannelConfiguration_Type.__name__ = "Integer32"
_IpadAtmCesAutoChannelConfiguration_Object = MibTableColumn
ipadAtmCesAutoChannelConfiguration = _IpadAtmCesAutoChannelConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 5, 1, 1, 3),
    _IpadAtmCesAutoChannelConfiguration_Type()
)
ipadAtmCesAutoChannelConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmCesAutoChannelConfiguration.setStatus("current")
_IpadAtmFrParms_ObjectIdentity = ObjectIdentity
ipadAtmFrParms = _IpadAtmFrParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6)
)
_IpadAtmFrf5SvcTable_Object = MibTable
ipadAtmFrf5SvcTable = _IpadAtmFrf5SvcTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1)
)
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcTable.setStatus("current")
_IpadAtmFrf5SvcTableEntry_Object = MibTableRow
ipadAtmFrf5SvcTableEntry = _IpadAtmFrf5SvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1)
)
ipadAtmFrf5SvcTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5SvcIfIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5SvcVpiIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5SvcVciIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcTableEntry.setStatus("current")
_IpadAtmFrf5SvcIfIndex_Type = Integer32
_IpadAtmFrf5SvcIfIndex_Object = MibTableColumn
ipadAtmFrf5SvcIfIndex = _IpadAtmFrf5SvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 1),
    _IpadAtmFrf5SvcIfIndex_Type()
)
ipadAtmFrf5SvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcIfIndex.setStatus("current")
_IpadAtmFrf5SvcVpiIndex_Type = Integer32
_IpadAtmFrf5SvcVpiIndex_Object = MibTableColumn
ipadAtmFrf5SvcVpiIndex = _IpadAtmFrf5SvcVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 2),
    _IpadAtmFrf5SvcVpiIndex_Type()
)
ipadAtmFrf5SvcVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcVpiIndex.setStatus("current")
_IpadAtmFrf5SvcVciIndex_Type = Integer32
_IpadAtmFrf5SvcVciIndex_Object = MibTableColumn
ipadAtmFrf5SvcVciIndex = _IpadAtmFrf5SvcVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 3),
    _IpadAtmFrf5SvcVciIndex_Type()
)
ipadAtmFrf5SvcVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcVciIndex.setStatus("current")


class _IpadAtmFrf5SvcDeToClpMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf5SvcDeToClpMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2Const0", 2),
          ("mode2Const1", 3))
    )


_IpadAtmFrf5SvcDeToClpMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcDeToClpMappingMode_Object = MibTableColumn
ipadAtmFrf5SvcDeToClpMappingMode = _IpadAtmFrf5SvcDeToClpMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 4),
    _IpadAtmFrf5SvcDeToClpMappingMode_Type()
)
ipadAtmFrf5SvcDeToClpMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcDeToClpMappingMode.setStatus("current")


class _IpadAtmFrf5SvcClpToDeMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf5SvcClpToDeMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_IpadAtmFrf5SvcClpToDeMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcClpToDeMappingMode_Object = MibTableColumn
ipadAtmFrf5SvcClpToDeMappingMode = _IpadAtmFrf5SvcClpToDeMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 5),
    _IpadAtmFrf5SvcClpToDeMappingMode_Type()
)
ipadAtmFrf5SvcClpToDeMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcClpToDeMappingMode.setStatus("current")


class _IpadAtmFrf5SvcN1_Type(Integer32):
    """Custom type ipadAtmFrf5SvcN1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpadAtmFrf5SvcN1_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcN1_Object = MibTableColumn
ipadAtmFrf5SvcN1 = _IpadAtmFrf5SvcN1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 6),
    _IpadAtmFrf5SvcN1_Type()
)
ipadAtmFrf5SvcN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcN1.setStatus("current")


class _IpadAtmFrf5SvcN2_Type(Integer32):
    """Custom type ipadAtmFrf5SvcN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpadAtmFrf5SvcN2_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcN2_Object = MibTableColumn
ipadAtmFrf5SvcN2 = _IpadAtmFrf5SvcN2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 7),
    _IpadAtmFrf5SvcN2_Type()
)
ipadAtmFrf5SvcN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcN2.setStatus("current")


class _IpadAtmFrf5SvcN3_Type(Integer32):
    """Custom type ipadAtmFrf5SvcN3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IpadAtmFrf5SvcN3_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcN3_Object = MibTableColumn
ipadAtmFrf5SvcN3 = _IpadAtmFrf5SvcN3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 8),
    _IpadAtmFrf5SvcN3_Type()
)
ipadAtmFrf5SvcN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcN3.setStatus("current")


class _IpadAtmFrf5SvcT1_Type(Integer32):
    """Custom type ipadAtmFrf5SvcT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 240),
    )


_IpadAtmFrf5SvcT1_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcT1_Object = MibTableColumn
ipadAtmFrf5SvcT1 = _IpadAtmFrf5SvcT1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 9),
    _IpadAtmFrf5SvcT1_Type()
)
ipadAtmFrf5SvcT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcT1.setStatus("current")


class _IpadAtmFrf5SvcT2_Type(Integer32):
    """Custom type ipadAtmFrf5SvcT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 245),
    )


_IpadAtmFrf5SvcT2_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcT2_Object = MibTableColumn
ipadAtmFrf5SvcT2 = _IpadAtmFrf5SvcT2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 10),
    _IpadAtmFrf5SvcT2_Type()
)
ipadAtmFrf5SvcT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcT2.setStatus("current")


class _IpadAtmFrf5SvcActive_Type(Integer32):
    """Custom type ipadAtmFrf5SvcActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadAtmFrf5SvcActive_Type.__name__ = "Integer32"
_IpadAtmFrf5SvcActive_Object = MibTableColumn
ipadAtmFrf5SvcActive = _IpadAtmFrf5SvcActive_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 11),
    _IpadAtmFrf5SvcActive_Type()
)
ipadAtmFrf5SvcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcActive.setStatus("current")
_IpadAtmFrf5SvcAddDLCI_Type = Integer32
_IpadAtmFrf5SvcAddDLCI_Object = MibTableColumn
ipadAtmFrf5SvcAddDLCI = _IpadAtmFrf5SvcAddDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 12),
    _IpadAtmFrf5SvcAddDLCI_Type()
)
ipadAtmFrf5SvcAddDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcAddDLCI.setStatus("current")
_IpadAtmFrf5SvcDeleteDLCI_Type = Integer32
_IpadAtmFrf5SvcDeleteDLCI_Object = MibTableColumn
ipadAtmFrf5SvcDeleteDLCI = _IpadAtmFrf5SvcDeleteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 1, 1, 13),
    _IpadAtmFrf5SvcDeleteDLCI_Type()
)
ipadAtmFrf5SvcDeleteDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5SvcDeleteDLCI.setStatus("current")
_IpadAtmFrf5DlciTable_Object = MibTable
ipadAtmFrf5DlciTable = _IpadAtmFrf5DlciTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2)
)
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciTable.setStatus("current")
_IpadAtmFrf5DlciTableEntry_Object = MibTableRow
ipadAtmFrf5DlciTableEntry = _IpadAtmFrf5DlciTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1)
)
ipadAtmFrf5DlciTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5DlciIfIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5DlciVpiIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5DlciVciIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf5DlciIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciTableEntry.setStatus("current")
_IpadAtmFrf5DlciIfIndex_Type = Integer32
_IpadAtmFrf5DlciIfIndex_Object = MibTableColumn
ipadAtmFrf5DlciIfIndex = _IpadAtmFrf5DlciIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 1),
    _IpadAtmFrf5DlciIfIndex_Type()
)
ipadAtmFrf5DlciIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciIfIndex.setStatus("current")
_IpadAtmFrf5DlciVpiIndex_Type = Integer32
_IpadAtmFrf5DlciVpiIndex_Object = MibTableColumn
ipadAtmFrf5DlciVpiIndex = _IpadAtmFrf5DlciVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 2),
    _IpadAtmFrf5DlciVpiIndex_Type()
)
ipadAtmFrf5DlciVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciVpiIndex.setStatus("current")
_IpadAtmFrf5DlciVciIndex_Type = Integer32
_IpadAtmFrf5DlciVciIndex_Object = MibTableColumn
ipadAtmFrf5DlciVciIndex = _IpadAtmFrf5DlciVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 3),
    _IpadAtmFrf5DlciVciIndex_Type()
)
ipadAtmFrf5DlciVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciVciIndex.setStatus("current")
_IpadAtmFrf5DlciIndex_Type = Integer32
_IpadAtmFrf5DlciIndex_Object = MibTableColumn
ipadAtmFrf5DlciIndex = _IpadAtmFrf5DlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 4),
    _IpadAtmFrf5DlciIndex_Type()
)
ipadAtmFrf5DlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciIndex.setStatus("current")


class _IpadAtmFrf5DlciEndpointName_Type(DisplayString):
    """Custom type ipadAtmFrf5DlciEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadAtmFrf5DlciEndpointName_Type.__name__ = "DisplayString"
_IpadAtmFrf5DlciEndpointName_Object = MibTableColumn
ipadAtmFrf5DlciEndpointName = _IpadAtmFrf5DlciEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 5),
    _IpadAtmFrf5DlciEndpointName_Type()
)
ipadAtmFrf5DlciEndpointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciEndpointName.setStatus("current")


class _IpadAtmFrf5DlciStatus_Type(Integer32):
    """Custom type ipadAtmFrf5DlciStatus based on Integer32"""
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
        *(("active", 3),
          ("activeLearned", 4),
          ("inactive", 1),
          ("inactiveLearned", 2))
    )


_IpadAtmFrf5DlciStatus_Type.__name__ = "Integer32"
_IpadAtmFrf5DlciStatus_Object = MibTableColumn
ipadAtmFrf5DlciStatus = _IpadAtmFrf5DlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 6),
    _IpadAtmFrf5DlciStatus_Type()
)
ipadAtmFrf5DlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciStatus.setStatus("current")


class _IpadAtmFrf5DlciCongestion_Type(Integer32):
    """Custom type ipadAtmFrf5DlciCongestion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadAtmFrf5DlciCongestion_Type.__name__ = "Integer32"
_IpadAtmFrf5DlciCongestion_Object = MibTableColumn
ipadAtmFrf5DlciCongestion = _IpadAtmFrf5DlciCongestion_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 2, 1, 7),
    _IpadAtmFrf5DlciCongestion_Type()
)
ipadAtmFrf5DlciCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf5DlciCongestion.setStatus("current")
_IpadAtmFrf8SvcTable_Object = MibTable
ipadAtmFrf8SvcTable = _IpadAtmFrf8SvcTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3)
)
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcTable.setStatus("current")
_IpadAtmFrf8SvcTableEntry_Object = MibTableRow
ipadAtmFrf8SvcTableEntry = _IpadAtmFrf8SvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1)
)
ipadAtmFrf8SvcTableEntry.setIndexNames(
    (0, "IPAD-ATM-MIB", "ipadAtmFrf8SvcIfIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf8SvcVpiIndex"),
    (0, "IPAD-ATM-MIB", "ipadAtmFrf8SvcVciIndex"),
)
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcTableEntry.setStatus("current")
_IpadAtmFrf8SvcIfIndex_Type = Integer32
_IpadAtmFrf8SvcIfIndex_Object = MibTableColumn
ipadAtmFrf8SvcIfIndex = _IpadAtmFrf8SvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 1),
    _IpadAtmFrf8SvcIfIndex_Type()
)
ipadAtmFrf8SvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcIfIndex.setStatus("current")
_IpadAtmFrf8SvcVpiIndex_Type = Integer32
_IpadAtmFrf8SvcVpiIndex_Object = MibTableColumn
ipadAtmFrf8SvcVpiIndex = _IpadAtmFrf8SvcVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 2),
    _IpadAtmFrf8SvcVpiIndex_Type()
)
ipadAtmFrf8SvcVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcVpiIndex.setStatus("current")
_IpadAtmFrf8SvcVciIndex_Type = Integer32
_IpadAtmFrf8SvcVciIndex_Object = MibTableColumn
ipadAtmFrf8SvcVciIndex = _IpadAtmFrf8SvcVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 3),
    _IpadAtmFrf8SvcVciIndex_Type()
)
ipadAtmFrf8SvcVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcVciIndex.setStatus("current")


class _IpadAtmFrf8SvcDeToClpMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf8SvcDeToClpMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2Const0", 2),
          ("mode2Const1", 3))
    )


_IpadAtmFrf8SvcDeToClpMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf8SvcDeToClpMappingMode_Object = MibTableColumn
ipadAtmFrf8SvcDeToClpMappingMode = _IpadAtmFrf8SvcDeToClpMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 4),
    _IpadAtmFrf8SvcDeToClpMappingMode_Type()
)
ipadAtmFrf8SvcDeToClpMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcDeToClpMappingMode.setStatus("current")


class _IpadAtmFrf8SvcClpToDeMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf8SvcClpToDeMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2Const0", 2),
          ("mode2Const1", 3))
    )


_IpadAtmFrf8SvcClpToDeMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf8SvcClpToDeMappingMode_Object = MibTableColumn
ipadAtmFrf8SvcClpToDeMappingMode = _IpadAtmFrf8SvcClpToDeMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 5),
    _IpadAtmFrf8SvcClpToDeMappingMode_Type()
)
ipadAtmFrf8SvcClpToDeMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcClpToDeMappingMode.setStatus("current")


class _IpadAtmFrf8SvcCongestionMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf8SvcCongestionMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_IpadAtmFrf8SvcCongestionMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf8SvcCongestionMappingMode_Object = MibTableColumn
ipadAtmFrf8SvcCongestionMappingMode = _IpadAtmFrf8SvcCongestionMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 6),
    _IpadAtmFrf8SvcCongestionMappingMode_Type()
)
ipadAtmFrf8SvcCongestionMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcCongestionMappingMode.setStatus("current")


class _IpadAtmFrf8SvcEncapsulationMappingMode_Type(Integer32):
    """Custom type ipadAtmFrf8SvcEncapsulationMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("translationMode", 2),
          ("transparentMode", 1))
    )


_IpadAtmFrf8SvcEncapsulationMappingMode_Type.__name__ = "Integer32"
_IpadAtmFrf8SvcEncapsulationMappingMode_Object = MibTableColumn
ipadAtmFrf8SvcEncapsulationMappingMode = _IpadAtmFrf8SvcEncapsulationMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 7),
    _IpadAtmFrf8SvcEncapsulationMappingMode_Type()
)
ipadAtmFrf8SvcEncapsulationMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcEncapsulationMappingMode.setStatus("current")


class _IpadAtmFrf8SvcEndpointName_Type(DisplayString):
    """Custom type ipadAtmFrf8SvcEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadAtmFrf8SvcEndpointName_Type.__name__ = "DisplayString"
_IpadAtmFrf8SvcEndpointName_Object = MibTableColumn
ipadAtmFrf8SvcEndpointName = _IpadAtmFrf8SvcEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25, 6, 3, 1, 8),
    _IpadAtmFrf8SvcEndpointName_Type()
)
ipadAtmFrf8SvcEndpointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAtmFrf8SvcEndpointName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-ATM-MIB",
    **{"ipadAtm": ipadAtm,
       "ipadAtmParms": ipadAtmParms,
       "ipadAtmTable": ipadAtmTable,
       "ipadAtmTableEntry": ipadAtmTableEntry,
       "ipadAtmIfIndex": ipadAtmIfIndex,
       "ipadAtmOperStatus": ipadAtmOperStatus,
       "ipadAtmVccsOpenedOK": ipadAtmVccsOpenedOK,
       "ipadAtmVccsNotOpened": ipadAtmVccsNotOpened,
       "ipadAtmAlarmReset": ipadAtmAlarmReset,
       "ipadAtmOverSubscriptionFactor": ipadAtmOverSubscriptionFactor,
       "ipadAtmLineBandwidth": ipadAtmLineBandwidth,
       "ipadAtmAAL5Bandwidth": ipadAtmAAL5Bandwidth,
       "ipadAtmOverSubBandwidth": ipadAtmOverSubBandwidth,
       "ipadAtmCbrUsedBandwidth": ipadAtmCbrUsedBandwidth,
       "ipadAtmVbrUsedBandwidth": ipadAtmVbrUsedBandwidth,
       "ipadAtmUbrUsedBandwidth": ipadAtmUbrUsedBandwidth,
       "ipadAtmQos0Pcr": ipadAtmQos0Pcr,
       "ipadAtmStatsParms": ipadAtmStatsParms,
       "ipadAtmStatsTable": ipadAtmStatsTable,
       "ipadAtmStatsTableEntry": ipadAtmStatsTableEntry,
       "ipadAtmStatsIndex": ipadAtmStatsIndex,
       "ipadAtmStatsPeriodIndex": ipadAtmStatsPeriodIndex,
       "ipadAtmStatsTimeStamp": ipadAtmStatsTimeStamp,
       "ipadAtmStatsRxFramesOK": ipadAtmStatsRxFramesOK,
       "ipadAtmStatsTxFramesOK": ipadAtmStatsTxFramesOK,
       "ipadAtmStatsRxFramesError": ipadAtmStatsRxFramesError,
       "ipadAtmStatsTxFramesError": ipadAtmStatsTxFramesError,
       "ipadAtmStatsRxBytesOK": ipadAtmStatsRxBytesOK,
       "ipadAtmStatsTxBytesOK": ipadAtmStatsTxBytesOK,
       "ipadAtmStatsLostSync": ipadAtmStatsLostSync,
       "ipadAtmStatsOamCellsRx": ipadAtmStatsOamCellsRx,
       "ipadAtmStatsOamCellsTx": ipadAtmStatsOamCellsTx,
       "ipadAtmVccParms": ipadAtmVccParms,
       "ipadAtmVccTable": ipadAtmVccTable,
       "ipadAtmVccTableEntry": ipadAtmVccTableEntry,
       "ipadAtmVccIndex": ipadAtmVccIndex,
       "ipadAtmVccVpiIndex": ipadAtmVccVpiIndex,
       "ipadAtmVccVciIndex": ipadAtmVccVciIndex,
       "ipadAtmVccEncapsulationType": ipadAtmVccEncapsulationType,
       "ipadAtmVccTrafficType": ipadAtmVccTrafficType,
       "ipadAtmVccChannelRate": ipadAtmVccChannelRate,
       "ipadAtmVccAlarmReset": ipadAtmVccAlarmReset,
       "ipadAtmVccSLATimer": ipadAtmVccSLATimer,
       "ipadAtmVccRemoteFramesOffered": ipadAtmVccRemoteFramesOffered,
       "ipadAtmVccFramesReceived": ipadAtmVccFramesReceived,
       "ipadAtmVccRemoteDataOffered": ipadAtmVccRemoteDataOffered,
       "ipadAtmVccDataReceived": ipadAtmVccDataReceived,
       "ipadAtmVccRemoteActive": ipadAtmVccRemoteActive,
       "ipadAtmVccRemoteVpi": ipadAtmVccRemoteVpi,
       "ipadAtmVccRemoteVci": ipadAtmVccRemoteVci,
       "ipadAtmVccRemoteIPAddress": ipadAtmVccRemoteIPAddress,
       "ipadAtmVccRemoteUnitId": ipadAtmVccRemoteUnitId,
       "ipadAtmVccEtoeLoopbackCommand": ipadAtmVccEtoeLoopbackCommand,
       "ipadAtmVccEtoeLoopbackState": ipadAtmVccEtoeLoopbackState,
       "ipadAtmVccEtoeLoopbackCellsTx": ipadAtmVccEtoeLoopbackCellsTx,
       "ipadAtmVccEtoeLoopbackCellsRx": ipadAtmVccEtoeLoopbackCellsRx,
       "ipadAtmVccEtoeLoopbackRttMin": ipadAtmVccEtoeLoopbackRttMin,
       "ipadAtmVccEtoeLoopbackRttMax": ipadAtmVccEtoeLoopbackRttMax,
       "ipadAtmVccEtoeLoopbackRttAvg": ipadAtmVccEtoeLoopbackRttAvg,
       "ipadAtmVccSegLoopbackCommand": ipadAtmVccSegLoopbackCommand,
       "ipadAtmVccSegLoopbackState": ipadAtmVccSegLoopbackState,
       "ipadAtmVccSegLoopbackCellsTx": ipadAtmVccSegLoopbackCellsTx,
       "ipadAtmVccSegLoopbackCellsRx": ipadAtmVccSegLoopbackCellsRx,
       "ipadAtmVccSegLoopbackRttMin": ipadAtmVccSegLoopbackRttMin,
       "ipadAtmVccSegLoopbackRttMax": ipadAtmVccSegLoopbackRttMax,
       "ipadAtmVccSegLoopbackRttAvg": ipadAtmVccSegLoopbackRttAvg,
       "ipadAtmVccEtoeContCheckCommand": ipadAtmVccEtoeContCheckCommand,
       "ipadAtmVccEtoeContCheckAutoActivate": ipadAtmVccEtoeContCheckAutoActivate,
       "ipadAtmVccEtoeContCheckType": ipadAtmVccEtoeContCheckType,
       "ipadAtmVccEtoeContCheckTypeInUse": ipadAtmVccEtoeContCheckTypeInUse,
       "ipadAtmVccEtoeContCheckStatus": ipadAtmVccEtoeContCheckStatus,
       "ipadAtmVccEtoeContCheckCellsTx": ipadAtmVccEtoeContCheckCellsTx,
       "ipadAtmVccEtoeContCheckCellsRx": ipadAtmVccEtoeContCheckCellsRx,
       "ipadAtmVccEtoeAisStatus": ipadAtmVccEtoeAisStatus,
       "ipadAtmVccEtoeRdiStatus": ipadAtmVccEtoeRdiStatus,
       "ipadAtmVccStatsParms": ipadAtmVccStatsParms,
       "ipadAtmVccStatsTable": ipadAtmVccStatsTable,
       "ipadAtmVccStatsTableEntry": ipadAtmVccStatsTableEntry,
       "ipadAtmVccStatsIndex": ipadAtmVccStatsIndex,
       "ipadAtmVccStatsVpiIndex": ipadAtmVccStatsVpiIndex,
       "ipadAtmVccStatsVciIndex": ipadAtmVccStatsVciIndex,
       "ipadAtmVccStatsPeriodIndex": ipadAtmVccStatsPeriodIndex,
       "ipadAtmVccStatsTimeStamp": ipadAtmVccStatsTimeStamp,
       "ipadAtmVccStatsRxFramesOK": ipadAtmVccStatsRxFramesOK,
       "ipadAtmVccStatsTxFramesOK": ipadAtmVccStatsTxFramesOK,
       "ipadAtmVccStatsRxFramesError": ipadAtmVccStatsRxFramesError,
       "ipadAtmVccStatsTxFramesError": ipadAtmVccStatsTxFramesError,
       "ipadAtmVccStatsRxFramesCLP": ipadAtmVccStatsRxFramesCLP,
       "ipadAtmVccStatsRxFramesCI": ipadAtmVccStatsRxFramesCI,
       "ipadAtmVccStatsRxFramesAbort": ipadAtmVccStatsRxFramesAbort,
       "ipadAtmVccStatsRxFramesLenViolation": ipadAtmVccStatsRxFramesLenViolation,
       "ipadAtmVccStatsRxFramesCRCError": ipadAtmVccStatsRxFramesCRCError,
       "ipadAtmVccStatsRxFramesTimeout": ipadAtmVccStatsRxFramesTimeout,
       "ipadAtmVccStatsRxFramesHCSError": ipadAtmVccStatsRxFramesHCSError,
       "ipadAtmVccStatsRxFramesNoBuffer": ipadAtmVccStatsRxFramesNoBuffer,
       "ipadAtmVccStatsRxCellsOK": ipadAtmVccStatsRxCellsOK,
       "ipadAtmVccStatsTxCellsOK": ipadAtmVccStatsTxCellsOK,
       "ipadAtmVccStatsRxBytesOK": ipadAtmVccStatsRxBytesOK,
       "ipadAtmVccStatsTxBytesOK": ipadAtmVccStatsTxBytesOK,
       "ipadAtmVccStatsDelayPeak": ipadAtmVccStatsDelayPeak,
       "ipadAtmVccStatsDelayAverage": ipadAtmVccStatsDelayAverage,
       "ipadAtmVccStatsRoundTripTimeouts": ipadAtmVccStatsRoundTripTimeouts,
       "ipadAtmVccStatsRemoteFramesOffered": ipadAtmVccStatsRemoteFramesOffered,
       "ipadAtmVccStatsFramesReceived": ipadAtmVccStatsFramesReceived,
       "ipadAtmVccStatsFDR": ipadAtmVccStatsFDR,
       "ipadAtmVccStatsRemoteDataOffered": ipadAtmVccStatsRemoteDataOffered,
       "ipadAtmVccStatsDataReceived": ipadAtmVccStatsDataReceived,
       "ipadAtmVccStatsDDR": ipadAtmVccStatsDDR,
       "ipadAtmVccStatsUAS": ipadAtmVccStatsUAS,
       "ipadAtmCesParms": ipadAtmCesParms,
       "ipadAtmCesTable": ipadAtmCesTable,
       "ipadAtmCesTableEntry": ipadAtmCesTableEntry,
       "ipadAtmCesIndex": ipadAtmCesIndex,
       "ipadAtmCesPayloadScrambling": ipadAtmCesPayloadScrambling,
       "ipadAtmCesAutoChannelConfiguration": ipadAtmCesAutoChannelConfiguration,
       "ipadAtmFrParms": ipadAtmFrParms,
       "ipadAtmFrf5SvcTable": ipadAtmFrf5SvcTable,
       "ipadAtmFrf5SvcTableEntry": ipadAtmFrf5SvcTableEntry,
       "ipadAtmFrf5SvcIfIndex": ipadAtmFrf5SvcIfIndex,
       "ipadAtmFrf5SvcVpiIndex": ipadAtmFrf5SvcVpiIndex,
       "ipadAtmFrf5SvcVciIndex": ipadAtmFrf5SvcVciIndex,
       "ipadAtmFrf5SvcDeToClpMappingMode": ipadAtmFrf5SvcDeToClpMappingMode,
       "ipadAtmFrf5SvcClpToDeMappingMode": ipadAtmFrf5SvcClpToDeMappingMode,
       "ipadAtmFrf5SvcN1": ipadAtmFrf5SvcN1,
       "ipadAtmFrf5SvcN2": ipadAtmFrf5SvcN2,
       "ipadAtmFrf5SvcN3": ipadAtmFrf5SvcN3,
       "ipadAtmFrf5SvcT1": ipadAtmFrf5SvcT1,
       "ipadAtmFrf5SvcT2": ipadAtmFrf5SvcT2,
       "ipadAtmFrf5SvcActive": ipadAtmFrf5SvcActive,
       "ipadAtmFrf5SvcAddDLCI": ipadAtmFrf5SvcAddDLCI,
       "ipadAtmFrf5SvcDeleteDLCI": ipadAtmFrf5SvcDeleteDLCI,
       "ipadAtmFrf5DlciTable": ipadAtmFrf5DlciTable,
       "ipadAtmFrf5DlciTableEntry": ipadAtmFrf5DlciTableEntry,
       "ipadAtmFrf5DlciIfIndex": ipadAtmFrf5DlciIfIndex,
       "ipadAtmFrf5DlciVpiIndex": ipadAtmFrf5DlciVpiIndex,
       "ipadAtmFrf5DlciVciIndex": ipadAtmFrf5DlciVciIndex,
       "ipadAtmFrf5DlciIndex": ipadAtmFrf5DlciIndex,
       "ipadAtmFrf5DlciEndpointName": ipadAtmFrf5DlciEndpointName,
       "ipadAtmFrf5DlciStatus": ipadAtmFrf5DlciStatus,
       "ipadAtmFrf5DlciCongestion": ipadAtmFrf5DlciCongestion,
       "ipadAtmFrf8SvcTable": ipadAtmFrf8SvcTable,
       "ipadAtmFrf8SvcTableEntry": ipadAtmFrf8SvcTableEntry,
       "ipadAtmFrf8SvcIfIndex": ipadAtmFrf8SvcIfIndex,
       "ipadAtmFrf8SvcVpiIndex": ipadAtmFrf8SvcVpiIndex,
       "ipadAtmFrf8SvcVciIndex": ipadAtmFrf8SvcVciIndex,
       "ipadAtmFrf8SvcDeToClpMappingMode": ipadAtmFrf8SvcDeToClpMappingMode,
       "ipadAtmFrf8SvcClpToDeMappingMode": ipadAtmFrf8SvcClpToDeMappingMode,
       "ipadAtmFrf8SvcCongestionMappingMode": ipadAtmFrf8SvcCongestionMappingMode,
       "ipadAtmFrf8SvcEncapsulationMappingMode": ipadAtmFrf8SvcEncapsulationMappingMode,
       "ipadAtmFrf8SvcEndpointName": ipadAtmFrf8SvcEndpointName}
)
