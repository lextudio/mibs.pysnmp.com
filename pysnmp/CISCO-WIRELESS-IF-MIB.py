# SNMP MIB module (CISCO-WIRELESS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:37 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CwrCollectionAction,
 CwrCollectionStatus,
 CwrCwConsecutiveSevErrSecond,
 CwrCwDegradedMinute,
 CwrCwDegradedSecond,
 CwrCwErrorFreeSecond,
 CwrCwErroredSecond,
 CwrCwSeverelyErroredSecond,
 CwrOscState,
 CwrRFZeroIndex,
 CwrRadioSignalAttribute,
 CwrThreshLimitType,
 WirelessGauge64) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-TC-MIB",
    "CwrCollectionAction",
    "CwrCollectionStatus",
    "CwrCwConsecutiveSevErrSecond",
    "CwrCwDegradedMinute",
    "CwrCwDegradedSecond",
    "CwrCwErrorFreeSecond",
    "CwrCwErroredSecond",
    "CwrCwSeverelyErroredSecond",
    "CwrOscState",
    "CwrRFZeroIndex",
    "CwrRadioSignalAttribute",
    "CwrThreshLimitType",
    "WirelessGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136)
)
ciscoWirelessIfMIB.setRevisions(
        ("2006-01-04 10:03",
         "2000-02-21 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwrRadioMibObjects_ObjectIdentity = ObjectIdentity
cwrRadioMibObjects = _CwrRadioMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1)
)
_CwrRadioInternal_ObjectIdentity = ObjectIdentity
cwrRadioInternal = _CwrRadioInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1)
)
_CwrTestGroup_ObjectIdentity = ObjectIdentity
cwrTestGroup = _CwrTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1)
)
_CwrLoopbackTable_Object = MibTable
cwrLoopbackTable = _CwrLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwrLoopbackTable.setStatus("current")
_CwrLoopbackEntry_Object = MibTableRow
cwrLoopbackEntry = _CwrLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 1, 1)
)
cwrLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrLoopbackEntry.setStatus("current")


class _CwrLocalLoopbackPoint_Type(Integer32):
    """Custom type cwrLocalLoopbackPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("codec", 1),
          ("fir", 3),
          ("framer", 2),
          ("if", 4),
          ("ifDiversity", 8),
          ("ifMain", 7),
          ("none", 0),
          ("rf", 5),
          ("rfDiversity", 6))
    )


_CwrLocalLoopbackPoint_Type.__name__ = "Integer32"
_CwrLocalLoopbackPoint_Object = MibTableColumn
cwrLocalLoopbackPoint = _CwrLocalLoopbackPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 1, 1, 1),
    _CwrLocalLoopbackPoint_Type()
)
cwrLocalLoopbackPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLocalLoopbackPoint.setStatus("current")
_CwrScopePortTable_Object = MibTable
cwrScopePortTable = _CwrScopePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwrScopePortTable.setStatus("current")
_CwrScopePortEntry_Object = MibTableRow
cwrScopePortEntry = _CwrScopePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 2, 1)
)
cwrScopePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrScopePortEntry.setStatus("current")
_CwrScopePortOn_Type = TruthValue
_CwrScopePortOn_Object = MibTableColumn
cwrScopePortOn = _CwrScopePortOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 2, 1, 1),
    _CwrScopePortOn_Type()
)
cwrScopePortOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrScopePortOn.setStatus("current")


class _CwrScopePortDsp_Type(Integer32):
    """Custom type cwrScopePortDsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CwrScopePortDsp_Type.__name__ = "Integer32"
_CwrScopePortDsp_Object = MibTableColumn
cwrScopePortDsp = _CwrScopePortDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 2, 1, 2),
    _CwrScopePortDsp_Type()
)
cwrScopePortDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrScopePortDsp.setStatus("current")


class _CwrScopePortAttribute_Type(Integer32):
    """Custom type cwrScopePortAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrScopePortAttribute_Type.__name__ = "Integer32"
_CwrScopePortAttribute_Object = MibTableColumn
cwrScopePortAttribute = _CwrScopePortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 1, 1, 2, 1, 3),
    _CwrScopePortAttribute_Type()
)
cwrScopePortAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrScopePortAttribute.setStatus("current")
_CwrRadioCommon_ObjectIdentity = ObjectIdentity
cwrRadioCommon = _CwrRadioCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 2)
)


class _CwrRadioNextIndex_Type(Integer32):
    """Custom type cwrRadioNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrRadioNextIndex_Type.__name__ = "Integer32"
_CwrRadioNextIndex_Object = MibScalar
cwrRadioNextIndex = _CwrRadioNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 2, 1),
    _CwrRadioNextIndex_Type()
)
cwrRadioNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRadioNextIndex.setStatus("current")
_CwrRadioBaseGroup_ObjectIdentity = ObjectIdentity
cwrRadioBaseGroup = _CwrRadioBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3)
)
_CwrRadioBaseTable_Object = MibTable
cwrRadioBaseTable = _CwrRadioBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwrRadioBaseTable.setStatus("current")
_CwrRadioBaseEntry_Object = MibTableRow
cwrRadioBaseEntry = _CwrRadioBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1)
)
cwrRadioBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrRadioBaseEntry.setStatus("current")


class _CwrAcquisitionMode_Type(Integer32):
    """Custom type cwrAcquisitionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_CwrAcquisitionMode_Type.__name__ = "Integer32"
_CwrAcquisitionMode_Object = MibTableColumn
cwrAcquisitionMode = _CwrAcquisitionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 2),
    _CwrAcquisitionMode_Type()
)
cwrAcquisitionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAcquisitionMode.setStatus("current")


class _CwrSelfTest_Type(Integer32):
    """Custom type cwrSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("off", 1),
          ("once", 2))
    )


_CwrSelfTest_Type.__name__ = "Integer32"
_CwrSelfTest_Object = MibTableColumn
cwrSelfTest = _CwrSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 3),
    _CwrSelfTest_Type()
)
cwrSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrSelfTest.setStatus("current")
_CwrBasePrivacySupport_Type = TruthValue
_CwrBasePrivacySupport_Object = MibTableColumn
cwrBasePrivacySupport = _CwrBasePrivacySupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 4),
    _CwrBasePrivacySupport_Type()
)
cwrBasePrivacySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBasePrivacySupport.setStatus("current")
_CwrTxRfIndex_Type = CwrRFZeroIndex
_CwrTxRfIndex_Object = MibTableColumn
cwrTxRfIndex = _CwrTxRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 5),
    _CwrTxRfIndex_Type()
)
cwrTxRfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTxRfIndex.setStatus("current")
_CwrRx1RfIndex_Type = CwrRFZeroIndex
_CwrRx1RfIndex_Object = MibTableColumn
cwrRx1RfIndex = _CwrRx1RfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 6),
    _CwrRx1RfIndex_Type()
)
cwrRx1RfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRx1RfIndex.setStatus("current")
_CwrRx2RfIndex_Type = CwrRFZeroIndex
_CwrRx2RfIndex_Object = MibTableColumn
cwrRx2RfIndex = _CwrRx2RfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 7),
    _CwrRx2RfIndex_Type()
)
cwrRx2RfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRx2RfIndex.setStatus("current")
_CwrClockRefExt_Type = TruthValue
_CwrClockRefExt_Object = MibTableColumn
cwrClockRefExt = _CwrClockRefExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 8),
    _CwrClockRefExt_Type()
)
cwrClockRefExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrClockRefExt.setStatus("current")
_CwrAntAlignment_Type = TruthValue
_CwrAntAlignment_Object = MibTableColumn
cwrAntAlignment = _CwrAntAlignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 1, 1, 9),
    _CwrAntAlignment_Type()
)
cwrAntAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntAlignment.setStatus("current")
_CwrRadioPhyTable_Object = MibTable
cwrRadioPhyTable = _CwrRadioPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cwrRadioPhyTable.setStatus("current")
_CwrRadioPhyEntry_Object = MibTableRow
cwrRadioPhyEntry = _CwrRadioPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1)
)
cwrRadioPhyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrRadioPhyEntry.setStatus("current")


class _CwrNumRxAntenna_Type(Integer32):
    """Custom type cwrNumRxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CwrNumRxAntenna_Type.__name__ = "Integer32"
_CwrNumRxAntenna_Object = MibTableColumn
cwrNumRxAntenna = _CwrNumRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 1),
    _CwrNumRxAntenna_Type()
)
cwrNumRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrNumRxAntenna.setStatus("current")


class _CwrBandwidth_Type(Integer32):
    """Custom type cwrBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000000),
    )


_CwrBandwidth_Type.__name__ = "Integer32"
_CwrBandwidth_Object = MibTableColumn
cwrBandwidth = _CwrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 2),
    _CwrBandwidth_Type()
)
cwrBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cwrBandwidth.setUnits("Hz")


class _CwrThroughput_Type(Integer32):
    """Custom type cwrThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_CwrThroughput_Type.__name__ = "Integer32"
_CwrThroughput_Object = MibTableColumn
cwrThroughput = _CwrThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 3),
    _CwrThroughput_Type()
)
cwrThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrThroughput.setStatus("current")


class _CwrOperatingBand_Type(Integer32):
    """Custom type cwrOperatingBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bandMMDS", 2),
          ("bandOther", 3),
          ("bandUNII", 1))
    )


_CwrOperatingBand_Type.__name__ = "Integer32"
_CwrOperatingBand_Object = MibTableColumn
cwrOperatingBand = _CwrOperatingBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 4),
    _CwrOperatingBand_Type()
)
cwrOperatingBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrOperatingBand.setStatus("current")


class _CwrTxFrequency_Type(Integer32):
    """Custom type cwrTxFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000000),
    )


_CwrTxFrequency_Type.__name__ = "Integer32"
_CwrTxFrequency_Object = MibTableColumn
cwrTxFrequency = _CwrTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 5),
    _CwrTxFrequency_Type()
)
cwrTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwrTxFrequency.setUnits("10Khz")


class _CwrRxFrequency_Type(Integer32):
    """Custom type cwrRxFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000000),
    )


_CwrRxFrequency_Type.__name__ = "Integer32"
_CwrRxFrequency_Object = MibTableColumn
cwrRxFrequency = _CwrRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 6),
    _CwrRxFrequency_Type()
)
cwrRxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwrRxFrequency.setUnits("10Khz")


class _CwrTxPower_Type(Integer32):
    """Custom type cwrTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_CwrTxPower_Type.__name__ = "Integer32"
_CwrTxPower_Object = MibTableColumn
cwrTxPower = _CwrTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 7),
    _CwrTxPower_Type()
)
cwrTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cwrTxPower.setUnits("dBm - decibel milliwatts")


class _CwrCableLoss_Type(Integer32):
    """Custom type cwrCableLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CwrCableLoss_Type.__name__ = "Integer32"
_CwrCableLoss_Object = MibTableColumn
cwrCableLoss = _CwrCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 8),
    _CwrCableLoss_Type()
)
cwrCableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrCableLoss.setStatus("current")
if mibBuilder.loadTexts:
    cwrCableLoss.setUnits("dB - decibel")


class _CwrOpStatus_Type(Integer32):
    """Custom type cwrOpStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 5),
          ("download", 3),
          ("linkOperational", 8),
          ("notOperational", 1),
          ("receiveUp", 6),
          ("selftest", 2),
          ("transmitUp", 7),
          ("txOnly", 4))
    )


_CwrOpStatus_Type.__name__ = "Integer32"
_CwrOpStatus_Object = MibTableColumn
cwrOpStatus = _CwrOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 9),
    _CwrOpStatus_Type()
)
cwrOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrOpStatus.setStatus("current")


class _CwrCableLossDiversity_Type(Integer32):
    """Custom type cwrCableLossDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CwrCableLossDiversity_Type.__name__ = "Integer32"
_CwrCableLossDiversity_Object = MibTableColumn
cwrCableLossDiversity = _CwrCableLossDiversity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 10),
    _CwrCableLossDiversity_Type()
)
cwrCableLossDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrCableLossDiversity.setStatus("current")
if mibBuilder.loadTexts:
    cwrCableLossDiversity.setUnits("dB - decibel")


class _CwrBurstSize_Type(Integer32):
    """Custom type cwrBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 3),
          ("medium", 2),
          ("small", 1))
    )


_CwrBurstSize_Type.__name__ = "Integer32"
_CwrBurstSize_Object = MibTableColumn
cwrBurstSize = _CwrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 3, 2, 1, 11),
    _CwrBurstSize_Type()
)
cwrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBurstSize.setStatus("current")
_CwrRadioPhyQualityGroup_ObjectIdentity = ObjectIdentity
cwrRadioPhyQualityGroup = _CwrRadioPhyQualityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4)
)
_CwrPhyQualityTable_Object = MibTable
cwrPhyQualityTable = _CwrPhyQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwrPhyQualityTable.setStatus("current")
_CwrPhyQualityEntry_Object = MibTableRow
cwrPhyQualityEntry = _CwrPhyQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1)
)
cwrPhyQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrPhyQualityEntry.setStatus("current")


class _CwrArqPctBw_Type(Integer32):
    """Custom type cwrArqPctBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrArqPctBw_Type.__name__ = "Integer32"
_CwrArqPctBw_Object = MibTableColumn
cwrArqPctBw = _CwrArqPctBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 1),
    _CwrArqPctBw_Type()
)
cwrArqPctBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrArqPctBw.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqPctBw.setUnits("0.01 percent")


class _CwrArqVoiceLatency_Type(Integer32):
    """Custom type cwrArqVoiceLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrArqVoiceLatency_Type.__name__ = "Integer32"
_CwrArqVoiceLatency_Object = MibTableColumn
cwrArqVoiceLatency = _CwrArqVoiceLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 2),
    _CwrArqVoiceLatency_Type()
)
cwrArqVoiceLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArqVoiceLatency.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqVoiceLatency.setUnits("milliseconds")


class _CwrArqDataLatency_Type(Integer32):
    """Custom type cwrArqDataLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrArqDataLatency_Type.__name__ = "Integer32"
_CwrArqDataLatency_Object = MibTableColumn
cwrArqDataLatency = _CwrArqDataLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 3),
    _CwrArqDataLatency_Type()
)
cwrArqDataLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrArqDataLatency.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqDataLatency.setUnits("milliseconds")


class _CwrArqBurstSize_Type(Integer32):
    """Custom type cwrArqBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_CwrArqBurstSize_Type.__name__ = "Integer32"
_CwrArqBurstSize_Object = MibTableColumn
cwrArqBurstSize = _CwrArqBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 4),
    _CwrArqBurstSize_Type()
)
cwrArqBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrArqBurstSize.setStatus("current")


class _CwrArqTypicalBitRate_Type(Integer32):
    """Custom type cwrArqTypicalBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45000000),
    )


_CwrArqTypicalBitRate_Type.__name__ = "Integer32"
_CwrArqTypicalBitRate_Object = MibTableColumn
cwrArqTypicalBitRate = _CwrArqTypicalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 5),
    _CwrArqTypicalBitRate_Type()
)
cwrArqTypicalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArqTypicalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqTypicalBitRate.setUnits("bits/sec")


class _CwrArqMinBitRate_Type(Integer32):
    """Custom type cwrArqMinBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45000000),
    )


_CwrArqMinBitRate_Type.__name__ = "Integer32"
_CwrArqMinBitRate_Object = MibTableColumn
cwrArqMinBitRate = _CwrArqMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 6),
    _CwrArqMinBitRate_Type()
)
cwrArqMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArqMinBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqMinBitRate.setUnits("bits/sec")


class _CwrArqMaxLatencyJitter_Type(Integer32):
    """Custom type cwrArqMaxLatencyJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22000),
    )


_CwrArqMaxLatencyJitter_Type.__name__ = "Integer32"
_CwrArqMaxLatencyJitter_Object = MibTableColumn
cwrArqMaxLatencyJitter = _CwrArqMaxLatencyJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 7),
    _CwrArqMaxLatencyJitter_Type()
)
cwrArqMaxLatencyJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArqMaxLatencyJitter.setStatus("current")
if mibBuilder.loadTexts:
    cwrArqMaxLatencyJitter.setUnits("microseconds")
_CwrArqReset_Type = TruthValue
_CwrArqReset_Object = MibTableColumn
cwrArqReset = _CwrArqReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 8),
    _CwrArqReset_Type()
)
cwrArqReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrArqReset.setStatus("current")
_CwrArqOn_Type = TruthValue
_CwrArqOn_Object = MibTableColumn
cwrArqOn = _CwrArqOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 1, 1, 9),
    _CwrArqOn_Type()
)
cwrArqOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrArqOn.setStatus("current")
_CwrPhyCorrectedBytesTable_Object = MibTable
cwrPhyCorrectedBytesTable = _CwrPhyCorrectedBytesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cwrPhyCorrectedBytesTable.setStatus("current")
_CwrPhyCorrectedBytesEntry_Object = MibTableRow
cwrPhyCorrectedBytesEntry = _CwrPhyCorrectedBytesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1)
)
cwrPhyCorrectedBytesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrPhyCorrectedBytesEntry.setStatus("current")
_CwrArq1ByteErrs_Type = Counter64
_CwrArq1ByteErrs_Object = MibTableColumn
cwrArq1ByteErrs = _CwrArq1ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 1),
    _CwrArq1ByteErrs_Type()
)
cwrArq1ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq1ByteErrs.setStatus("current")
_CwrArq2ByteErrs_Type = Counter64
_CwrArq2ByteErrs_Object = MibTableColumn
cwrArq2ByteErrs = _CwrArq2ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 2),
    _CwrArq2ByteErrs_Type()
)
cwrArq2ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq2ByteErrs.setStatus("current")
_CwrArq3ByteErrs_Type = Counter64
_CwrArq3ByteErrs_Object = MibTableColumn
cwrArq3ByteErrs = _CwrArq3ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 3),
    _CwrArq3ByteErrs_Type()
)
cwrArq3ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq3ByteErrs.setStatus("current")
_CwrArq4ByteErrs_Type = Counter64
_CwrArq4ByteErrs_Object = MibTableColumn
cwrArq4ByteErrs = _CwrArq4ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 4),
    _CwrArq4ByteErrs_Type()
)
cwrArq4ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq4ByteErrs.setStatus("current")
_CwrArq5ByteErrs_Type = Counter64
_CwrArq5ByteErrs_Object = MibTableColumn
cwrArq5ByteErrs = _CwrArq5ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 5),
    _CwrArq5ByteErrs_Type()
)
cwrArq5ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq5ByteErrs.setStatus("current")
_CwrArq6ByteErrs_Type = Counter64
_CwrArq6ByteErrs_Object = MibTableColumn
cwrArq6ByteErrs = _CwrArq6ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 6),
    _CwrArq6ByteErrs_Type()
)
cwrArq6ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq6ByteErrs.setStatus("current")
_CwrArq7ByteErrs_Type = Counter64
_CwrArq7ByteErrs_Object = MibTableColumn
cwrArq7ByteErrs = _CwrArq7ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 7),
    _CwrArq7ByteErrs_Type()
)
cwrArq7ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq7ByteErrs.setStatus("current")
_CwrArq8ByteErrs_Type = Counter64
_CwrArq8ByteErrs_Object = MibTableColumn
cwrArq8ByteErrs = _CwrArq8ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 8),
    _CwrArq8ByteErrs_Type()
)
cwrArq8ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq8ByteErrs.setStatus("current")
_CwrArq9ByteErrs_Type = Counter64
_CwrArq9ByteErrs_Object = MibTableColumn
cwrArq9ByteErrs = _CwrArq9ByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 4, 2, 1, 9),
    _CwrArq9ByteErrs_Type()
)
cwrArq9ByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrArq9ByteErrs.setStatus("current")
_CwrRadioFreqResGroup_ObjectIdentity = ObjectIdentity
cwrRadioFreqResGroup = _CwrRadioFreqResGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5)
)
_CwrRfTable_Object = MibTable
cwrRfTable = _CwrRfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cwrRfTable.setStatus("current")
_CwrRfEntry_Object = MibTableRow
cwrRfEntry = _CwrRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1)
)
cwrRfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrRfIndex"),
)
if mibBuilder.loadTexts:
    cwrRfEntry.setStatus("current")


class _CwrRfIndex_Type(Integer32):
    """Custom type cwrRfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CwrRfIndex_Type.__name__ = "Integer32"
_CwrRfIndex_Object = MibTableColumn
cwrRfIndex = _CwrRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 1),
    _CwrRfIndex_Type()
)
cwrRfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrRfIndex.setStatus("current")


class _CwrRfResIndex_Type(Integer32):
    """Custom type cwrRfResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrRfResIndex_Type.__name__ = "Integer32"
_CwrRfResIndex_Object = MibTableColumn
cwrRfResIndex = _CwrRfResIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 2),
    _CwrRfResIndex_Type()
)
cwrRfResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfResIndex.setStatus("current")


class _CwrRFOpMode_Type(Integer32):
    """Custom type cwrRFOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxAndTx", 2),
          ("rxOnly", 0),
          ("txOnly", 1))
    )


_CwrRFOpMode_Type.__name__ = "Integer32"
_CwrRFOpMode_Object = MibTableColumn
cwrRFOpMode = _CwrRFOpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 3),
    _CwrRFOpMode_Type()
)
cwrRFOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRFOpMode.setStatus("current")


class _CwrTxFreqRangeMin_Type(Integer32):
    """Custom type cwrTxFreqRangeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(215000, 582500),
    )


_CwrTxFreqRangeMin_Type.__name__ = "Integer32"
_CwrTxFreqRangeMin_Object = MibTableColumn
cwrTxFreqRangeMin = _CwrTxFreqRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 4),
    _CwrTxFreqRangeMin_Type()
)
cwrTxFreqRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTxFreqRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    cwrTxFreqRangeMin.setUnits("10 kHz")


class _CwrTxFreqRangeMax_Type(Integer32):
    """Custom type cwrTxFreqRangeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(215000, 582500),
    )


_CwrTxFreqRangeMax_Type.__name__ = "Integer32"
_CwrTxFreqRangeMax_Object = MibTableColumn
cwrTxFreqRangeMax = _CwrTxFreqRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 5),
    _CwrTxFreqRangeMax_Type()
)
cwrTxFreqRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTxFreqRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    cwrTxFreqRangeMax.setUnits("10 kHz")


class _CwrRxFreqRangeMin_Type(Integer32):
    """Custom type cwrRxFreqRangeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(215000, 582500),
    )


_CwrRxFreqRangeMin_Type.__name__ = "Integer32"
_CwrRxFreqRangeMin_Object = MibTableColumn
cwrRxFreqRangeMin = _CwrRxFreqRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 6),
    _CwrRxFreqRangeMin_Type()
)
cwrRxFreqRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRxFreqRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    cwrRxFreqRangeMin.setUnits("10 kHz")


class _CwrRxFreqRangeMax_Type(Integer32):
    """Custom type cwrRxFreqRangeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(215000, 582500),
    )


_CwrRxFreqRangeMax_Type.__name__ = "Integer32"
_CwrRxFreqRangeMax_Object = MibTableColumn
cwrRxFreqRangeMax = _CwrRxFreqRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 7),
    _CwrRxFreqRangeMax_Type()
)
cwrRxFreqRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRxFreqRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    cwrRxFreqRangeMax.setUnits("10 kHz")


class _CwrMinTxPower_Type(Integer32):
    """Custom type cwrMinTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 33),
    )


_CwrMinTxPower_Type.__name__ = "Integer32"
_CwrMinTxPower_Object = MibTableColumn
cwrMinTxPower = _CwrMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 8),
    _CwrMinTxPower_Type()
)
cwrMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrMinTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cwrMinTxPower.setUnits("dBm Decibel milliwatts")


class _CwrMaxTxPower_Type(Integer32):
    """Custom type cwrMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 33),
    )


_CwrMaxTxPower_Type.__name__ = "Integer32"
_CwrMaxTxPower_Object = MibTableColumn
cwrMaxTxPower = _CwrMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 9),
    _CwrMaxTxPower_Type()
)
cwrMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cwrMaxTxPower.setUnits("dBm Decibel milliwatts")
_CwrRfTxOscState_Type = CwrOscState
_CwrRfTxOscState_Object = MibTableColumn
cwrRfTxOscState = _CwrRfTxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 10),
    _CwrRfTxOscState_Type()
)
cwrRfTxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfTxOscState.setStatus("current")


class _CwrRfAntIndex_Type(Integer32):
    """Custom type cwrRfAntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwrRfAntIndex_Type.__name__ = "Integer32"
_CwrRfAntIndex_Object = MibTableColumn
cwrRfAntIndex = _CwrRfAntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 11),
    _CwrRfAntIndex_Type()
)
cwrRfAntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfAntIndex.setStatus("current")
_CwrRfRxOscState_Type = CwrOscState
_CwrRfRxOscState_Object = MibTableColumn
cwrRfRxOscState = _CwrRfRxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 12),
    _CwrRfRxOscState_Type()
)
cwrRfRxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfRxOscState.setStatus("current")


class _CwrRfTemperature_Type(Integer32):
    """Custom type cwrRfTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_CwrRfTemperature_Type.__name__ = "Integer32"
_CwrRfTemperature_Object = MibTableColumn
cwrRfTemperature = _CwrRfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 13),
    _CwrRfTemperature_Type()
)
cwrRfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cwrRfTemperature.setUnits("Degrees Centigrade")


class _CwrRfSupplyVoltageState_Type(Integer32):
    """Custom type cwrRfSupplyVoltageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outsideSpecification", 2),
          ("withinSpecification", 1))
    )


_CwrRfSupplyVoltageState_Type.__name__ = "Integer32"
_CwrRfSupplyVoltageState_Object = MibTableColumn
cwrRfSupplyVoltageState = _CwrRfSupplyVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 14),
    _CwrRfSupplyVoltageState_Type()
)
cwrRfSupplyVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfSupplyVoltageState.setStatus("current")


class _CwrRfStatus_Type(Integer32):
    """Custom type cwrRfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_CwrRfStatus_Type.__name__ = "Integer32"
_CwrRfStatus_Object = MibTableColumn
cwrRfStatus = _CwrRfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 15),
    _CwrRfStatus_Type()
)
cwrRfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfStatus.setStatus("current")


class _CwrRfControlChannelStatus_Type(Integer32):
    """Custom type cwrRfControlChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_CwrRfControlChannelStatus_Type.__name__ = "Integer32"
_CwrRfControlChannelStatus_Object = MibTableColumn
cwrRfControlChannelStatus = _CwrRfControlChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 16),
    _CwrRfControlChannelStatus_Type()
)
cwrRfControlChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRfControlChannelStatus.setStatus("current")


class _CwrBurstSizeGroup_Type(OctetString):
    """Custom type cwrBurstSizeGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CwrBurstSizeGroup_Type.__name__ = "OctetString"
_CwrBurstSizeGroup_Object = MibTableColumn
cwrBurstSizeGroup = _CwrBurstSizeGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 1, 1, 17),
    _CwrBurstSizeGroup_Type()
)
cwrBurstSizeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBurstSizeGroup.setStatus("current")
_CwrIntFreqTable_Object = MibTable
cwrIntFreqTable = _CwrIntFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cwrIntFreqTable.setStatus("current")
_CwrIntFreqEntry_Object = MibTableRow
cwrIntFreqEntry = _CwrIntFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1)
)
cwrIntFreqEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrIntFreqEntry.setStatus("current")
_CwrIfTxOscState_Type = CwrOscState
_CwrIfTxOscState_Object = MibTableColumn
cwrIfTxOscState = _CwrIfTxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 1),
    _CwrIfTxOscState_Type()
)
cwrIfTxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfTxOscState.setStatus("current")
_CwrIfRxOscState_Type = CwrOscState
_CwrIfRxOscState_Object = MibTableColumn
cwrIfRxOscState = _CwrIfRxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 2),
    _CwrIfRxOscState_Type()
)
cwrIfRxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfRxOscState.setStatus("current")
_CwrIfRefOscState_Type = CwrOscState
_CwrIfRefOscState_Object = MibTableColumn
cwrIfRefOscState = _CwrIfRefOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 3),
    _CwrIfRefOscState_Type()
)
cwrIfRefOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfRefOscState.setStatus("current")


class _CwrIfResIndex_Type(Integer32):
    """Custom type cwrIfResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrIfResIndex_Type.__name__ = "Integer32"
_CwrIfResIndex_Object = MibTableColumn
cwrIfResIndex = _CwrIfResIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 4),
    _CwrIfResIndex_Type()
)
cwrIfResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfResIndex.setStatus("current")


class _CwrIfInpFreq_Type(Integer32):
    """Custom type cwrIfInpFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CwrIfInpFreq_Type.__name__ = "Integer32"
_CwrIfInpFreq_Object = MibTableColumn
cwrIfInpFreq = _CwrIfInpFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 5),
    _CwrIfInpFreq_Type()
)
cwrIfInpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfInpFreq.setStatus("current")
if mibBuilder.loadTexts:
    cwrIfInpFreq.setUnits("10 kHz")


class _CwrIfOutFreq_Type(Integer32):
    """Custom type cwrIfOutFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 50000),
    )


_CwrIfOutFreq_Type.__name__ = "Integer32"
_CwrIfOutFreq_Object = MibTableColumn
cwrIfOutFreq = _CwrIfOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 5, 2, 1, 6),
    _CwrIfOutFreq_Type()
)
cwrIfOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrIfOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    cwrIfOutFreq.setUnits("10 kHz")
_CwrRadioMetricsGroup_ObjectIdentity = ObjectIdentity
cwrRadioMetricsGroup = _CwrRadioMetricsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6)
)
_CwrLinkMetricsThresholdTable_Object = MibTable
cwrLinkMetricsThresholdTable = _CwrLinkMetricsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cwrLinkMetricsThresholdTable.setStatus("current")
_CwrLinkMetricsThreshEntry_Object = MibTableRow
cwrLinkMetricsThreshEntry = _CwrLinkMetricsThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1)
)
cwrLinkMetricsThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrLinkMetricsThreshEntry.setStatus("current")
_CwrLinkCwESThresh_Type = Unsigned32
_CwrLinkCwESThresh_Object = MibTableColumn
cwrLinkCwESThresh = _CwrLinkCwESThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 1),
    _CwrLinkCwESThresh_Type()
)
cwrLinkCwESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLinkCwESThresh.setStatus("current")
_CwrLinkLowCwDSThresh_Type = Unsigned32
_CwrLinkLowCwDSThresh_Object = MibTableColumn
cwrLinkLowCwDSThresh = _CwrLinkLowCwDSThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 2),
    _CwrLinkLowCwDSThresh_Type()
)
cwrLinkLowCwDSThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLinkLowCwDSThresh.setStatus("current")
_CwrLinkHighCwDSThresh_Type = Unsigned32
_CwrLinkHighCwDSThresh_Object = MibTableColumn
cwrLinkHighCwDSThresh = _CwrLinkHighCwDSThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 3),
    _CwrLinkHighCwDSThresh_Type()
)
cwrLinkHighCwDSThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLinkHighCwDSThresh.setStatus("current")
_CwrLinkCSESThresh_Type = Unsigned32
_CwrLinkCSESThresh_Object = MibTableColumn
cwrLinkCSESThresh = _CwrLinkCSESThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 4),
    _CwrLinkCSESThresh_Type()
)
cwrLinkCSESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLinkCSESThresh.setStatus("current")
_CwrLink1HrESAlarmThresh_Type = Unsigned32
_CwrLink1HrESAlarmThresh_Object = MibTableColumn
cwrLink1HrESAlarmThresh = _CwrLink1HrESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 5),
    _CwrLink1HrESAlarmThresh_Type()
)
cwrLink1HrESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink1HrESAlarmThresh.setStatus("current")
_CwrLink1HrSESAlarmThresh_Type = Unsigned32
_CwrLink1HrSESAlarmThresh_Object = MibTableColumn
cwrLink1HrSESAlarmThresh = _CwrLink1HrSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 6),
    _CwrLink1HrSESAlarmThresh_Type()
)
cwrLink1HrSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink1HrSESAlarmThresh.setStatus("current")
_CwrLink1HrCSESAlarmThresh_Type = Unsigned32
_CwrLink1HrCSESAlarmThresh_Object = MibTableColumn
cwrLink1HrCSESAlarmThresh = _CwrLink1HrCSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 7),
    _CwrLink1HrCSESAlarmThresh_Type()
)
cwrLink1HrCSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink1HrCSESAlarmThresh.setStatus("current")
_CwrLink1HrDCMAlarmThresh_Type = Unsigned32
_CwrLink1HrDCMAlarmThresh_Object = MibTableColumn
cwrLink1HrDCMAlarmThresh = _CwrLink1HrDCMAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 8),
    _CwrLink1HrDCMAlarmThresh_Type()
)
cwrLink1HrDCMAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink1HrDCMAlarmThresh.setStatus("current")
_CwrLink24HrESAlarmThresh_Type = Unsigned32
_CwrLink24HrESAlarmThresh_Object = MibTableColumn
cwrLink24HrESAlarmThresh = _CwrLink24HrESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 9),
    _CwrLink24HrESAlarmThresh_Type()
)
cwrLink24HrESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink24HrESAlarmThresh.setStatus("current")
_CwrLink24HrSESAlarmThresh_Type = Unsigned32
_CwrLink24HrSESAlarmThresh_Object = MibTableColumn
cwrLink24HrSESAlarmThresh = _CwrLink24HrSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 10),
    _CwrLink24HrSESAlarmThresh_Type()
)
cwrLink24HrSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink24HrSESAlarmThresh.setStatus("current")
_CwrLink24HrCSESAlarmThresh_Type = Unsigned32
_CwrLink24HrCSESAlarmThresh_Object = MibTableColumn
cwrLink24HrCSESAlarmThresh = _CwrLink24HrCSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 11),
    _CwrLink24HrCSESAlarmThresh_Type()
)
cwrLink24HrCSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink24HrCSESAlarmThresh.setStatus("current")
_CwrLink24HrDCMAlarmThresh_Type = Unsigned32
_CwrLink24HrDCMAlarmThresh_Object = MibTableColumn
cwrLink24HrDCMAlarmThresh = _CwrLink24HrDCMAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 1, 1, 12),
    _CwrLink24HrDCMAlarmThresh_Type()
)
cwrLink24HrDCMAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrLink24HrDCMAlarmThresh.setStatus("current")
_CwrCumulativeMetricsTable_Object = MibTable
cwrCumulativeMetricsTable = _CwrCumulativeMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cwrCumulativeMetricsTable.setStatus("current")
_CwrCumulativeMetricsEntry_Object = MibTableRow
cwrCumulativeMetricsEntry = _CwrCumulativeMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1)
)
cwrCumulativeMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrCumulativeMetricsEntry.setStatus("current")
_CwrAvailableSeconds_Type = Counter32
_CwrAvailableSeconds_Object = MibTableColumn
cwrAvailableSeconds = _CwrAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 1),
    _CwrAvailableSeconds_Type()
)
cwrAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrAvailableSeconds.setStatus("current")
_CwrUnAvailableSeconds_Type = Counter32
_CwrUnAvailableSeconds_Object = MibTableColumn
cwrUnAvailableSeconds = _CwrUnAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 2),
    _CwrUnAvailableSeconds_Type()
)
cwrUnAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrUnAvailableSeconds.setStatus("current")
_CwrSyncLossSeconds_Type = Counter32
_CwrSyncLossSeconds_Object = MibTableColumn
cwrSyncLossSeconds = _CwrSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 3),
    _CwrSyncLossSeconds_Type()
)
cwrSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSyncLossSeconds.setStatus("current")


class _CwrPctErrorFreeSeconds_Type(Gauge32):
    """Custom type cwrPctErrorFreeSeconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctErrorFreeSeconds_Type.__name__ = "Gauge32"
_CwrPctErrorFreeSeconds_Object = MibTableColumn
cwrPctErrorFreeSeconds = _CwrPctErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 4),
    _CwrPctErrorFreeSeconds_Type()
)
cwrPctErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctErrorFreeSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctErrorFreeSeconds.setUnits("0.01 percent")


class _CwrPctErroredSeconds_Type(Gauge32):
    """Custom type cwrPctErroredSeconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctErroredSeconds_Type.__name__ = "Gauge32"
_CwrPctErroredSeconds_Object = MibTableColumn
cwrPctErroredSeconds = _CwrPctErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 5),
    _CwrPctErroredSeconds_Type()
)
cwrPctErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctErroredSeconds.setUnits("0.01 percent")


class _CwrPctSeverelyErroredSeconds_Type(Gauge32):
    """Custom type cwrPctSeverelyErroredSeconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctSeverelyErroredSeconds_Type.__name__ = "Gauge32"
_CwrPctSeverelyErroredSeconds_Object = MibTableColumn
cwrPctSeverelyErroredSeconds = _CwrPctSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 6),
    _CwrPctSeverelyErroredSeconds_Type()
)
cwrPctSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctSeverelyErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctSeverelyErroredSeconds.setUnits("0.01 percent")


class _CwrPctAvailSeconds_Type(Gauge32):
    """Custom type cwrPctAvailSeconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctAvailSeconds_Type.__name__ = "Gauge32"
_CwrPctAvailSeconds_Object = MibTableColumn
cwrPctAvailSeconds = _CwrPctAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 7),
    _CwrPctAvailSeconds_Type()
)
cwrPctAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctAvailSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctAvailSeconds.setUnits("0.01 percent")


class _CwrPctCwDegradedMinutes_Type(Gauge32):
    """Custom type cwrPctCwDegradedMinutes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctCwDegradedMinutes_Type.__name__ = "Gauge32"
_CwrPctCwDegradedMinutes_Object = MibTableColumn
cwrPctCwDegradedMinutes = _CwrPctCwDegradedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 8),
    _CwrPctCwDegradedMinutes_Type()
)
cwrPctCwDegradedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctCwDegradedMinutes.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctCwDegradedMinutes.setUnits("0.01 percent")
_CwrSyncSuccessCount_Type = Counter32
_CwrSyncSuccessCount_Object = MibTableColumn
cwrSyncSuccessCount = _CwrSyncSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 9),
    _CwrSyncSuccessCount_Type()
)
cwrSyncSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSyncSuccessCount.setStatus("current")
_CwrSyncFailureCount_Type = Counter32
_CwrSyncFailureCount_Object = MibTableColumn
cwrSyncFailureCount = _CwrSyncFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 10),
    _CwrSyncFailureCount_Type()
)
cwrSyncFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSyncFailureCount.setStatus("current")
_CwrManagedSyncLoss_Type = Counter32
_CwrManagedSyncLoss_Object = MibTableColumn
cwrManagedSyncLoss = _CwrManagedSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 11),
    _CwrManagedSyncLoss_Type()
)
cwrManagedSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrManagedSyncLoss.setStatus("current")
_CwrAutomaticSyncLoss_Type = Counter32
_CwrAutomaticSyncLoss_Object = MibTableColumn
cwrAutomaticSyncLoss = _CwrAutomaticSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 12),
    _CwrAutomaticSyncLoss_Type()
)
cwrAutomaticSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrAutomaticSyncLoss.setStatus("current")
_CwrLastSyncSuccessTime_Type = TimeInterval
_CwrLastSyncSuccessTime_Object = MibTableColumn
cwrLastSyncSuccessTime = _CwrLastSyncSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 13),
    _CwrLastSyncSuccessTime_Type()
)
cwrLastSyncSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLastSyncSuccessTime.setStatus("current")
_CwrLastSyncFailTime_Type = TimeInterval
_CwrLastSyncFailTime_Object = MibTableColumn
cwrLastSyncFailTime = _CwrLastSyncFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 14),
    _CwrLastSyncFailTime_Type()
)
cwrLastSyncFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrLastSyncFailTime.setStatus("current")
_CwrEffectivePhyDataRate_Type = Gauge32
_CwrEffectivePhyDataRate_Object = MibTableColumn
cwrEffectivePhyDataRate = _CwrEffectivePhyDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 15),
    _CwrEffectivePhyDataRate_Type()
)
cwrEffectivePhyDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrEffectivePhyDataRate.setStatus("current")


class _CwrPctEffectivePhyDataRate_Type(Gauge32):
    """Custom type cwrPctEffectivePhyDataRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwrPctEffectivePhyDataRate_Type.__name__ = "Gauge32"
_CwrPctEffectivePhyDataRate_Object = MibTableColumn
cwrPctEffectivePhyDataRate = _CwrPctEffectivePhyDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 2, 1, 16),
    _CwrPctEffectivePhyDataRate_Type()
)
cwrPctEffectivePhyDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrPctEffectivePhyDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cwrPctEffectivePhyDataRate.setUnits("0.01 percent")
_Cwr24HrMetricsTable_Object = MibTable
cwr24HrMetricsTable = _Cwr24HrMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cwr24HrMetricsTable.setStatus("current")
_Cwr24HrMetricsEntry_Object = MibTableRow
cwr24HrMetricsEntry = _Cwr24HrMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1)
)
cwr24HrMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwr24HrMetricsIndex"),
)
if mibBuilder.loadTexts:
    cwr24HrMetricsEntry.setStatus("current")


class _Cwr24HrMetricsIndex_Type(Integer32):
    """Custom type cwr24HrMetricsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cwr24HrMetricsIndex_Type.__name__ = "Integer32"
_Cwr24HrMetricsIndex_Object = MibTableColumn
cwr24HrMetricsIndex = _Cwr24HrMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 1),
    _Cwr24HrMetricsIndex_Type()
)
cwr24HrMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwr24HrMetricsIndex.setStatus("current")


class _Cwr24HrUpdateTime_Type(Integer32):
    """Custom type cwr24HrUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cwr24HrUpdateTime_Type.__name__ = "Integer32"
_Cwr24HrUpdateTime_Object = MibTableColumn
cwr24HrUpdateTime = _Cwr24HrUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 2),
    _Cwr24HrUpdateTime_Type()
)
cwr24HrUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwr24HrUpdateTime.setUnits("seconds")
_Cwr24HrErrorFreeSeconds_Type = CwrCwErrorFreeSecond
_Cwr24HrErrorFreeSeconds_Object = MibTableColumn
cwr24HrErrorFreeSeconds = _Cwr24HrErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 3),
    _Cwr24HrErrorFreeSeconds_Type()
)
cwr24HrErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrErrorFreeSeconds.setStatus("current")
_Cwr24HrErroredSeconds_Type = CwrCwErroredSecond
_Cwr24HrErroredSeconds_Object = MibTableColumn
cwr24HrErroredSeconds = _Cwr24HrErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 4),
    _Cwr24HrErroredSeconds_Type()
)
cwr24HrErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrErroredSeconds.setStatus("current")
_Cwr24HrSevErroredSeconds_Type = CwrCwSeverelyErroredSecond
_Cwr24HrSevErroredSeconds_Object = MibTableColumn
cwr24HrSevErroredSeconds = _Cwr24HrSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 5),
    _Cwr24HrSevErroredSeconds_Type()
)
cwr24HrSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrSevErroredSeconds.setStatus("current")
_Cwr24HrConsecSvErrSeconds_Type = CwrCwConsecutiveSevErrSecond
_Cwr24HrConsecSvErrSeconds_Object = MibTableColumn
cwr24HrConsecSvErrSeconds = _Cwr24HrConsecSvErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 6),
    _Cwr24HrConsecSvErrSeconds_Type()
)
cwr24HrConsecSvErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrConsecSvErrSeconds.setStatus("current")
_Cwr24HrDegradedMinutes_Type = CwrCwDegradedMinute
_Cwr24HrDegradedMinutes_Object = MibTableColumn
cwr24HrDegradedMinutes = _Cwr24HrDegradedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 7),
    _Cwr24HrDegradedMinutes_Type()
)
cwr24HrDegradedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrDegradedMinutes.setStatus("current")
_Cwr24HrTotalErroredCodewords_Type = WirelessGauge64
_Cwr24HrTotalErroredCodewords_Object = MibTableColumn
cwr24HrTotalErroredCodewords = _Cwr24HrTotalErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 8),
    _Cwr24HrTotalErroredCodewords_Type()
)
cwr24HrTotalErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrTotalErroredCodewords.setStatus("current")
_Cwr24HrTotalCodewords_Type = WirelessGauge64
_Cwr24HrTotalCodewords_Object = MibTableColumn
cwr24HrTotalCodewords = _Cwr24HrTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 3, 1, 9),
    _Cwr24HrTotalCodewords_Type()
)
cwr24HrTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr24HrTotalCodewords.setStatus("current")
_Cwr1HrMetricsTable_Object = MibTable
cwr1HrMetricsTable = _Cwr1HrMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cwr1HrMetricsTable.setStatus("current")
_Cwr1HrMetricsEntry_Object = MibTableRow
cwr1HrMetricsEntry = _Cwr1HrMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1)
)
cwr1HrMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwr1HrMetricsIndex"),
)
if mibBuilder.loadTexts:
    cwr1HrMetricsEntry.setStatus("current")


class _Cwr1HrMetricsIndex_Type(Integer32):
    """Custom type cwr1HrMetricsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cwr1HrMetricsIndex_Type.__name__ = "Integer32"
_Cwr1HrMetricsIndex_Object = MibTableColumn
cwr1HrMetricsIndex = _Cwr1HrMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 1),
    _Cwr1HrMetricsIndex_Type()
)
cwr1HrMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwr1HrMetricsIndex.setStatus("current")


class _Cwr1HrUpdateTime_Type(Integer32):
    """Custom type cwr1HrUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cwr1HrUpdateTime_Type.__name__ = "Integer32"
_Cwr1HrUpdateTime_Object = MibTableColumn
cwr1HrUpdateTime = _Cwr1HrUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 2),
    _Cwr1HrUpdateTime_Type()
)
cwr1HrUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwr1HrUpdateTime.setUnits("seconds")
_Cwr1HrErrorFreeSeconds_Type = CwrCwErrorFreeSecond
_Cwr1HrErrorFreeSeconds_Object = MibTableColumn
cwr1HrErrorFreeSeconds = _Cwr1HrErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 3),
    _Cwr1HrErrorFreeSeconds_Type()
)
cwr1HrErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrErrorFreeSeconds.setStatus("current")
_Cwr1HrErroredSeconds_Type = CwrCwErroredSecond
_Cwr1HrErroredSeconds_Object = MibTableColumn
cwr1HrErroredSeconds = _Cwr1HrErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 4),
    _Cwr1HrErroredSeconds_Type()
)
cwr1HrErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrErroredSeconds.setStatus("current")
_Cwr1HrSevErroredSeconds_Type = CwrCwSeverelyErroredSecond
_Cwr1HrSevErroredSeconds_Object = MibTableColumn
cwr1HrSevErroredSeconds = _Cwr1HrSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 5),
    _Cwr1HrSevErroredSeconds_Type()
)
cwr1HrSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrSevErroredSeconds.setStatus("current")
_Cwr1HrConsecSvErrSeconds_Type = CwrCwConsecutiveSevErrSecond
_Cwr1HrConsecSvErrSeconds_Object = MibTableColumn
cwr1HrConsecSvErrSeconds = _Cwr1HrConsecSvErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 6),
    _Cwr1HrConsecSvErrSeconds_Type()
)
cwr1HrConsecSvErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrConsecSvErrSeconds.setStatus("current")
_Cwr1HrDegradedMinutes_Type = CwrCwDegradedMinute
_Cwr1HrDegradedMinutes_Object = MibTableColumn
cwr1HrDegradedMinutes = _Cwr1HrDegradedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 7),
    _Cwr1HrDegradedMinutes_Type()
)
cwr1HrDegradedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrDegradedMinutes.setStatus("current")
_Cwr1HrErroredCodewords_Type = WirelessGauge64
_Cwr1HrErroredCodewords_Object = MibTableColumn
cwr1HrErroredCodewords = _Cwr1HrErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 8),
    _Cwr1HrErroredCodewords_Type()
)
cwr1HrErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrErroredCodewords.setStatus("current")
_Cwr1HrTotalCodewords_Type = WirelessGauge64
_Cwr1HrTotalCodewords_Object = MibTableColumn
cwr1HrTotalCodewords = _Cwr1HrTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 4, 1, 9),
    _Cwr1HrTotalCodewords_Type()
)
cwr1HrTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1HrTotalCodewords.setStatus("current")
_Cwr1MinMetricsTable_Object = MibTable
cwr1MinMetricsTable = _Cwr1MinMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cwr1MinMetricsTable.setStatus("current")
_Cwr1MinMetricsEntry_Object = MibTableRow
cwr1MinMetricsEntry = _Cwr1MinMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1)
)
cwr1MinMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwr1MinMetricsIndex"),
)
if mibBuilder.loadTexts:
    cwr1MinMetricsEntry.setStatus("current")


class _Cwr1MinMetricsIndex_Type(Integer32):
    """Custom type cwr1MinMetricsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cwr1MinMetricsIndex_Type.__name__ = "Integer32"
_Cwr1MinMetricsIndex_Object = MibTableColumn
cwr1MinMetricsIndex = _Cwr1MinMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 1),
    _Cwr1MinMetricsIndex_Type()
)
cwr1MinMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwr1MinMetricsIndex.setStatus("current")


class _Cwr1MinUpdateTime_Type(Integer32):
    """Custom type cwr1MinUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cwr1MinUpdateTime_Type.__name__ = "Integer32"
_Cwr1MinUpdateTime_Object = MibTableColumn
cwr1MinUpdateTime = _Cwr1MinUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 2),
    _Cwr1MinUpdateTime_Type()
)
cwr1MinUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwr1MinUpdateTime.setUnits("seconds")
_Cwr1MinErrorFreeSeconds_Type = CwrCwErrorFreeSecond
_Cwr1MinErrorFreeSeconds_Object = MibTableColumn
cwr1MinErrorFreeSeconds = _Cwr1MinErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 3),
    _Cwr1MinErrorFreeSeconds_Type()
)
cwr1MinErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinErrorFreeSeconds.setStatus("current")
_Cwr1MinErroredSeconds_Type = CwrCwErroredSecond
_Cwr1MinErroredSeconds_Object = MibTableColumn
cwr1MinErroredSeconds = _Cwr1MinErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 4),
    _Cwr1MinErroredSeconds_Type()
)
cwr1MinErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinErroredSeconds.setStatus("current")
_Cwr1MinSevErroredSeconds_Type = CwrCwSeverelyErroredSecond
_Cwr1MinSevErroredSeconds_Object = MibTableColumn
cwr1MinSevErroredSeconds = _Cwr1MinSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 5),
    _Cwr1MinSevErroredSeconds_Type()
)
cwr1MinSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinSevErroredSeconds.setStatus("current")
_Cwr1MinConsecSvCwErrSeconds_Type = CwrCwConsecutiveSevErrSecond
_Cwr1MinConsecSvCwErrSeconds_Object = MibTableColumn
cwr1MinConsecSvCwErrSeconds = _Cwr1MinConsecSvCwErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 6),
    _Cwr1MinConsecSvCwErrSeconds_Type()
)
cwr1MinConsecSvCwErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinConsecSvCwErrSeconds.setStatus("current")
_Cwr1MinDegradedSeconds_Type = CwrCwDegradedSecond
_Cwr1MinDegradedSeconds_Object = MibTableColumn
cwr1MinDegradedSeconds = _Cwr1MinDegradedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 7),
    _Cwr1MinDegradedSeconds_Type()
)
cwr1MinDegradedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinDegradedSeconds.setStatus("current")
_Cwr1MinErroredCodewords_Type = WirelessGauge64
_Cwr1MinErroredCodewords_Object = MibTableColumn
cwr1MinErroredCodewords = _Cwr1MinErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 8),
    _Cwr1MinErroredCodewords_Type()
)
cwr1MinErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinErroredCodewords.setStatus("current")
_Cwr1MinCodewords_Type = WirelessGauge64
_Cwr1MinCodewords_Object = MibTableColumn
cwr1MinCodewords = _Cwr1MinCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 5, 1, 9),
    _Cwr1MinCodewords_Type()
)
cwr1MinCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1MinCodewords.setStatus("current")
_Cwr1SecMetricsTable_Object = MibTable
cwr1SecMetricsTable = _Cwr1SecMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cwr1SecMetricsTable.setStatus("current")
_Cwr1SecMetricsEntry_Object = MibTableRow
cwr1SecMetricsEntry = _Cwr1SecMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1)
)
cwr1SecMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwr1SecIndex"),
)
if mibBuilder.loadTexts:
    cwr1SecMetricsEntry.setStatus("current")


class _Cwr1SecIndex_Type(Integer32):
    """Custom type cwr1SecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cwr1SecIndex_Type.__name__ = "Integer32"
_Cwr1SecIndex_Object = MibTableColumn
cwr1SecIndex = _Cwr1SecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 1),
    _Cwr1SecIndex_Type()
)
cwr1SecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwr1SecIndex.setStatus("current")


class _Cwr1SecUpdateTime_Type(Integer32):
    """Custom type cwr1SecUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cwr1SecUpdateTime_Type.__name__ = "Integer32"
_Cwr1SecUpdateTime_Object = MibTableColumn
cwr1SecUpdateTime = _Cwr1SecUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 2),
    _Cwr1SecUpdateTime_Type()
)
cwr1SecUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwr1SecUpdateTime.setUnits("seconds")
_Cwr1SecRxCodewords_Type = WirelessGauge64
_Cwr1SecRxCodewords_Object = MibTableColumn
cwr1SecRxCodewords = _Cwr1SecRxCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 3),
    _Cwr1SecRxCodewords_Type()
)
cwr1SecRxCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecRxCodewords.setStatus("current")
_Cwr1SecRSCodewordErrors_Type = WirelessGauge64
_Cwr1SecRSCodewordErrors_Object = MibTableColumn
cwr1SecRSCodewordErrors = _Cwr1SecRSCodewordErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 4),
    _Cwr1SecRSCodewordErrors_Type()
)
cwr1SecRSCodewordErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecRSCodewordErrors.setStatus("current")
_Cwr1SecArqCodewordErrors_Type = Gauge32
_Cwr1SecArqCodewordErrors_Object = MibTableColumn
cwr1SecArqCodewordErrors = _Cwr1SecArqCodewordErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 5),
    _Cwr1SecArqCodewordErrors_Type()
)
cwr1SecArqCodewordErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecArqCodewordErrors.setStatus("current")
_Cwr1SecRxRrCount_Type = Gauge32
_Cwr1SecRxRrCount_Object = MibTableColumn
cwr1SecRxRrCount = _Cwr1SecRxRrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 6),
    _Cwr1SecRxRrCount_Type()
)
cwr1SecRxRrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecRxRrCount.setStatus("current")
_Cwr1SecRxRrEventCount_Type = Gauge32
_Cwr1SecRxRrEventCount_Object = MibTableColumn
cwr1SecRxRrEventCount = _Cwr1SecRxRrEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 7),
    _Cwr1SecRxRrEventCount_Type()
)
cwr1SecRxRrEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecRxRrEventCount.setStatus("current")
_Cwr1SecTxArqCount_Type = Gauge32
_Cwr1SecTxArqCount_Object = MibTableColumn
cwr1SecTxArqCount = _Cwr1SecTxArqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 8),
    _Cwr1SecTxArqCount_Type()
)
cwr1SecTxArqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecTxArqCount.setStatus("current")
_Cwr1SecTxArqEventCount_Type = Gauge32
_Cwr1SecTxArqEventCount_Object = MibTableColumn
cwr1SecTxArqEventCount = _Cwr1SecTxArqEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 9),
    _Cwr1SecTxArqEventCount_Type()
)
cwr1SecTxArqEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecTxArqEventCount.setStatus("current")
_Cwr1SecCorrectedSyncByteErrs_Type = Gauge32
_Cwr1SecCorrectedSyncByteErrs_Object = MibTableColumn
cwr1SecCorrectedSyncByteErrs = _Cwr1SecCorrectedSyncByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 10),
    _Cwr1SecCorrectedSyncByteErrs_Type()
)
cwr1SecCorrectedSyncByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecCorrectedSyncByteErrs.setStatus("current")
_Cwr1SecConsecutiveCwErrs_Type = Gauge32
_Cwr1SecConsecutiveCwErrs_Object = MibTableColumn
cwr1SecConsecutiveCwErrs = _Cwr1SecConsecutiveCwErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 11),
    _Cwr1SecConsecutiveCwErrs_Type()
)
cwr1SecConsecutiveCwErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecConsecutiveCwErrs.setStatus("current")
_Cwr1SecPostARQGoodCodewords_Type = WirelessGauge64
_Cwr1SecPostARQGoodCodewords_Object = MibTableColumn
cwr1SecPostARQGoodCodewords = _Cwr1SecPostARQGoodCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 6, 6, 1, 12),
    _Cwr1SecPostARQGoodCodewords_Type()
)
cwr1SecPostARQGoodCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwr1SecPostARQGoodCodewords.setStatus("current")
_CwrRadioHistoryGroup_ObjectIdentity = ObjectIdentity
cwrRadioHistoryGroup = _CwrRadioHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7)
)
_CwrHistCtrlTable_Object = MibTable
cwrHistCtrlTable = _CwrHistCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cwrHistCtrlTable.setStatus("current")
_CwrHistCtrlEntry_Object = MibTableRow
cwrHistCtrlEntry = _CwrHistCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1)
)
cwrHistCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrHistIndex"),
)
if mibBuilder.loadTexts:
    cwrHistCtrlEntry.setStatus("current")


class _CwrHistIndex_Type(Integer32):
    """Custom type cwrHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrHistIndex_Type.__name__ = "Integer32"
_CwrHistIndex_Object = MibTableColumn
cwrHistIndex = _CwrHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 1),
    _CwrHistIndex_Type()
)
cwrHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrHistIndex.setStatus("current")
_CwrHistClass_Type = CwrRadioSignalAttribute
_CwrHistClass_Object = MibTableColumn
cwrHistClass = _CwrHistClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 2),
    _CwrHistClass_Type()
)
cwrHistClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistClass.setStatus("current")
_CwrRfResourceId_Type = CwrRFZeroIndex
_CwrRfResourceId_Object = MibTableColumn
cwrRfResourceId = _CwrRfResourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 3),
    _CwrRfResourceId_Type()
)
cwrRfResourceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrRfResourceId.setStatus("current")


class _CwrDspNumber_Type(Integer32):
    """Custom type cwrDspNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CwrDspNumber_Type.__name__ = "Integer32"
_CwrDspNumber_Object = MibTableColumn
cwrDspNumber = _CwrDspNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 4),
    _CwrDspNumber_Type()
)
cwrDspNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrDspNumber.setStatus("current")


class _CwrStartBinValue_Type(Integer32):
    """Custom type cwrStartBinValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CwrStartBinValue_Type.__name__ = "Integer32"
_CwrStartBinValue_Object = MibTableColumn
cwrStartBinValue = _CwrStartBinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 5),
    _CwrStartBinValue_Type()
)
cwrStartBinValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrStartBinValue.setStatus("current")


class _CwrBinDelta_Type(Integer32):
    """Custom type cwrBinDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2147483647),
    )


_CwrBinDelta_Type.__name__ = "Integer32"
_CwrBinDelta_Object = MibTableColumn
cwrBinDelta = _CwrBinDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 6),
    _CwrBinDelta_Type()
)
cwrBinDelta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrBinDelta.setStatus("current")
if mibBuilder.loadTexts:
    cwrBinDelta.setUnits("Powers of 2")


class _CwrNumHistBins_Type(Integer32):
    """Custom type cwrNumHistBins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 508),
    )


_CwrNumHistBins_Type.__name__ = "Integer32"
_CwrNumHistBins_Object = MibTableColumn
cwrNumHistBins = _CwrNumHistBins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 7),
    _CwrNumHistBins_Type()
)
cwrNumHistBins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrNumHistBins.setStatus("current")


class _CwrUpdateRate_Type(Integer32):
    """Custom type cwrUpdateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrUpdateRate_Type.__name__ = "Integer32"
_CwrUpdateRate_Object = MibTableColumn
cwrUpdateRate = _CwrUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 8),
    _CwrUpdateRate_Type()
)
cwrUpdateRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    cwrUpdateRate.setUnits("seconds")


class _CwrCollDuration_Type(Integer32):
    """Custom type cwrCollDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrCollDuration_Type.__name__ = "Integer32"
_CwrCollDuration_Object = MibTableColumn
cwrCollDuration = _CwrCollDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 9),
    _CwrCollDuration_Type()
)
cwrCollDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrCollDuration.setStatus("current")
if mibBuilder.loadTexts:
    cwrCollDuration.setUnits("seconds")
_CwrOwnerId_Type = OwnerString
_CwrOwnerId_Object = MibTableColumn
cwrOwnerId = _CwrOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 10),
    _CwrOwnerId_Type()
)
cwrOwnerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrOwnerId.setStatus("current")


class _CwrHistBitShift_Type(Integer32):
    """Custom type cwrHistBitShift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CwrHistBitShift_Type.__name__ = "Integer32"
_CwrHistBitShift_Object = MibTableColumn
cwrHistBitShift = _CwrHistBitShift_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 11),
    _CwrHistBitShift_Type()
)
cwrHistBitShift.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistBitShift.setStatus("current")


class _CwrHistToneSelection_Type(Integer32):
    """Custom type cwrHistToneSelection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cwrAverage", 2),
          ("cwrCirculate", 1),
          ("cwrSpecific", 3))
    )


_CwrHistToneSelection_Type.__name__ = "Integer32"
_CwrHistToneSelection_Object = MibTableColumn
cwrHistToneSelection = _CwrHistToneSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 12),
    _CwrHistToneSelection_Type()
)
cwrHistToneSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistToneSelection.setStatus("current")


class _CwrHistToneValue_Type(Integer32):
    """Custom type cwrHistToneValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
    )


_CwrHistToneValue_Type.__name__ = "Integer32"
_CwrHistToneValue_Object = MibTableColumn
cwrHistToneValue = _CwrHistToneValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 13),
    _CwrHistToneValue_Type()
)
cwrHistToneValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistToneValue.setStatus("current")
_CwrHistAction_Type = CwrCollectionAction
_CwrHistAction_Object = MibTableColumn
cwrHistAction = _CwrHistAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 14),
    _CwrHistAction_Type()
)
cwrHistAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistAction.setStatus("current")
_CwrHistStatus_Type = CwrCollectionStatus
_CwrHistStatus_Object = MibTableColumn
cwrHistStatus = _CwrHistStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 15),
    _CwrHistStatus_Type()
)
cwrHistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrHistStatus.setStatus("current")
_CwrHistRowStatus_Type = RowStatus
_CwrHistRowStatus_Object = MibTableColumn
cwrHistRowStatus = _CwrHistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 16),
    _CwrHistRowStatus_Type()
)
cwrHistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistRowStatus.setStatus("current")
_CwrHistPeriodicSum_Type = TruthValue
_CwrHistPeriodicSum_Object = MibTableColumn
cwrHistPeriodicSum = _CwrHistPeriodicSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 1, 1, 17),
    _CwrHistPeriodicSum_Type()
)
cwrHistPeriodicSum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrHistPeriodicSum.setStatus("current")
_CwrHistSummaryTable_Object = MibTable
cwrHistSummaryTable = _CwrHistSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cwrHistSummaryTable.setStatus("current")
_CwrHistSummaryEntry_Object = MibTableRow
cwrHistSummaryEntry = _CwrHistSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2, 1)
)
cwrHistSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrHistIndex"),
)
if mibBuilder.loadTexts:
    cwrHistSummaryEntry.setStatus("current")


class _CwrHistUpdateTime_Type(Integer32):
    """Custom type cwrHistUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrHistUpdateTime_Type.__name__ = "Integer32"
_CwrHistUpdateTime_Object = MibTableColumn
cwrHistUpdateTime = _CwrHistUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2, 1, 1),
    _CwrHistUpdateTime_Type()
)
cwrHistUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrHistUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwrHistUpdateTime.setUnits("seconds")


class _CwrHistMin_Type(Integer32):
    """Custom type cwrHistMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrHistMin_Type.__name__ = "Integer32"
_CwrHistMin_Object = MibTableColumn
cwrHistMin = _CwrHistMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2, 1, 2),
    _CwrHistMin_Type()
)
cwrHistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrHistMin.setStatus("current")


class _CwrHistMax_Type(Integer32):
    """Custom type cwrHistMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrHistMax_Type.__name__ = "Integer32"
_CwrHistMax_Object = MibTableColumn
cwrHistMax = _CwrHistMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2, 1, 3),
    _CwrHistMax_Type()
)
cwrHistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrHistMax.setStatus("current")


class _CwrHistMean_Type(Integer32):
    """Custom type cwrHistMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrHistMean_Type.__name__ = "Integer32"
_CwrHistMean_Object = MibTableColumn
cwrHistMean = _CwrHistMean_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 2, 1, 4),
    _CwrHistMean_Type()
)
cwrHistMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrHistMean.setStatus("current")
_CwrHistDataTable_Object = MibTable
cwrHistDataTable = _CwrHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cwrHistDataTable.setStatus("current")
_CwrHistDataEntry_Object = MibTableRow
cwrHistDataEntry = _CwrHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 3, 1)
)
cwrHistDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrHistIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrHistBinIndex"),
)
if mibBuilder.loadTexts:
    cwrHistDataEntry.setStatus("current")


class _CwrHistBinIndex_Type(Integer32):
    """Custom type cwrHistBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 508),
    )


_CwrHistBinIndex_Type.__name__ = "Integer32"
_CwrHistBinIndex_Object = MibTableColumn
cwrHistBinIndex = _CwrHistBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 3, 1, 1),
    _CwrHistBinIndex_Type()
)
cwrHistBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrHistBinIndex.setStatus("current")


class _CwrValue_Type(Integer32):
    """Custom type cwrValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwrValue_Type.__name__ = "Integer32"
_CwrValue_Object = MibTableColumn
cwrValue = _CwrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 7, 3, 1, 2),
    _CwrValue_Type()
)
cwrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrValue.setStatus("current")
_CwrRadioTimelineGroup_ObjectIdentity = ObjectIdentity
cwrRadioTimelineGroup = _CwrRadioTimelineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8)
)
_CwrThresholdTable_Object = MibTable
cwrThresholdTable = _CwrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cwrThresholdTable.setStatus("current")
_CwrThresholdEntry_Object = MibTableRow
cwrThresholdEntry = _CwrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1)
)
cwrThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrThreshIndex"),
)
if mibBuilder.loadTexts:
    cwrThresholdEntry.setStatus("current")


class _CwrThreshIndex_Type(Integer32):
    """Custom type cwrThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrThreshIndex_Type.__name__ = "Integer32"
_CwrThreshIndex_Object = MibTableColumn
cwrThreshIndex = _CwrThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 1),
    _CwrThreshIndex_Type()
)
cwrThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrThreshIndex.setStatus("current")
_CwrThreshAttribute_Type = CwrRadioSignalAttribute
_CwrThreshAttribute_Object = MibTableColumn
cwrThreshAttribute = _CwrThreshAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 2),
    _CwrThreshAttribute_Type()
)
cwrThreshAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshAttribute.setStatus("current")
_CwrThreshType_Type = CwrThreshLimitType
_CwrThreshType_Object = MibTableColumn
cwrThreshType = _CwrThreshType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 3),
    _CwrThreshType_Type()
)
cwrThreshType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshType.setStatus("current")
_CwrThreshAntId_Type = CwrRFZeroIndex
_CwrThreshAntId_Object = MibTableColumn
cwrThreshAntId = _CwrThreshAntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 4),
    _CwrThreshAntId_Type()
)
cwrThreshAntId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshAntId.setStatus("current")


class _CwrThreshValue_Type(Integer32):
    """Custom type cwrThreshValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CwrThreshValue_Type.__name__ = "Integer32"
_CwrThreshValue_Object = MibTableColumn
cwrThreshValue = _CwrThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 5),
    _CwrThreshValue_Type()
)
cwrThreshValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshValue.setStatus("current")
_CwrThreshHysteresisTime_Type = TimeInterval
_CwrThreshHysteresisTime_Object = MibTableColumn
cwrThreshHysteresisTime = _CwrThreshHysteresisTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 6),
    _CwrThreshHysteresisTime_Type()
)
cwrThreshHysteresisTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshHysteresisTime.setStatus("current")
_CwrThreshLimitTime_Type = TimeInterval
_CwrThreshLimitTime_Object = MibTableColumn
cwrThreshLimitTime = _CwrThreshLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 7),
    _CwrThreshLimitTime_Type()
)
cwrThreshLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshLimitTime.setStatus("current")


class _CwrThreshDspNum_Type(Integer32):
    """Custom type cwrThreshDspNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CwrThreshDspNum_Type.__name__ = "Integer32"
_CwrThreshDspNum_Object = MibTableColumn
cwrThreshDspNum = _CwrThreshDspNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 8),
    _CwrThreshDspNum_Type()
)
cwrThreshDspNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshDspNum.setStatus("current")
_CwrThreshRowStatus_Type = RowStatus
_CwrThreshRowStatus_Object = MibTableColumn
cwrThreshRowStatus = _CwrThreshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 1, 1, 9),
    _CwrThreshRowStatus_Type()
)
cwrThreshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrThreshRowStatus.setStatus("current")
_CwrTlCtrlTable_Object = MibTable
cwrTlCtrlTable = _CwrTlCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cwrTlCtrlTable.setStatus("current")
_CwrTlCtrlEntry_Object = MibTableRow
cwrTlCtrlEntry = _CwrTlCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1)
)
cwrTlCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrTlIndex"),
)
if mibBuilder.loadTexts:
    cwrTlCtrlEntry.setStatus("current")


class _CwrTlIndex_Type(Integer32):
    """Custom type cwrTlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrTlIndex_Type.__name__ = "Integer32"
_CwrTlIndex_Object = MibTableColumn
cwrTlIndex = _CwrTlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 1),
    _CwrTlIndex_Type()
)
cwrTlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrTlIndex.setStatus("current")
_CwrTlClass_Type = CwrRadioSignalAttribute
_CwrTlClass_Object = MibTableColumn
cwrTlClass = _CwrTlClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 2),
    _CwrTlClass_Type()
)
cwrTlClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlClass.setStatus("current")
_CwrTlRfResourceId_Type = CwrRFZeroIndex
_CwrTlRfResourceId_Object = MibTableColumn
cwrTlRfResourceId = _CwrTlRfResourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 3),
    _CwrTlRfResourceId_Type()
)
cwrTlRfResourceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlRfResourceId.setStatus("current")


class _CwrTlDspNum_Type(Integer32):
    """Custom type cwrTlDspNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CwrTlDspNum_Type.__name__ = "Integer32"
_CwrTlDspNum_Object = MibTableColumn
cwrTlDspNum = _CwrTlDspNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 4),
    _CwrTlDspNum_Type()
)
cwrTlDspNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlDspNum.setStatus("current")


class _CwrTlNumDataValues_Type(Integer32):
    """Custom type cwrTlNumDataValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrTlNumDataValues_Type.__name__ = "Integer32"
_CwrTlNumDataValues_Object = MibTableColumn
cwrTlNumDataValues = _CwrTlNumDataValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 5),
    _CwrTlNumDataValues_Type()
)
cwrTlNumDataValues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlNumDataValues.setStatus("current")
if mibBuilder.loadTexts:
    cwrTlNumDataValues.setUnits("number of data values")


class _CwrTlDecimationFactor_Type(Integer32):
    """Custom type cwrTlDecimationFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwrTlDecimationFactor_Type.__name__ = "Integer32"
_CwrTlDecimationFactor_Object = MibTableColumn
cwrTlDecimationFactor = _CwrTlDecimationFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 6),
    _CwrTlDecimationFactor_Type()
)
cwrTlDecimationFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlDecimationFactor.setStatus("current")


class _CwrTlPreSumShift_Type(Integer32):
    """Custom type cwrTlPreSumShift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CwrTlPreSumShift_Type.__name__ = "Integer32"
_CwrTlPreSumShift_Object = MibTableColumn
cwrTlPreSumShift = _CwrTlPreSumShift_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 7),
    _CwrTlPreSumShift_Type()
)
cwrTlPreSumShift.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlPreSumShift.setStatus("current")


class _CwrTlToneSelection_Type(Integer32):
    """Custom type cwrTlToneSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cwrAverage", 2),
          ("cwrCirculate", 1),
          ("cwrSpecific", 3))
    )


_CwrTlToneSelection_Type.__name__ = "Integer32"
_CwrTlToneSelection_Object = MibTableColumn
cwrTlToneSelection = _CwrTlToneSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 8),
    _CwrTlToneSelection_Type()
)
cwrTlToneSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlToneSelection.setStatus("current")


class _CwrTlToneValue_Type(Integer32):
    """Custom type cwrTlToneValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
    )


_CwrTlToneValue_Type.__name__ = "Integer32"
_CwrTlToneValue_Object = MibTableColumn
cwrTlToneValue = _CwrTlToneValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 9),
    _CwrTlToneValue_Type()
)
cwrTlToneValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlToneValue.setStatus("current")


class _CwrTlThreshIndex_Type(Integer32):
    """Custom type cwrTlThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwrTlThreshIndex_Type.__name__ = "Integer32"
_CwrTlThreshIndex_Object = MibTableColumn
cwrTlThreshIndex = _CwrTlThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 10),
    _CwrTlThreshIndex_Type()
)
cwrTlThreshIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlThreshIndex.setStatus("current")
_CwrTlAction_Type = CwrCollectionAction
_CwrTlAction_Object = MibTableColumn
cwrTlAction = _CwrTlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 11),
    _CwrTlAction_Type()
)
cwrTlAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlAction.setStatus("current")
_CwrTlStatus_Type = CwrCollectionStatus
_CwrTlStatus_Object = MibTableColumn
cwrTlStatus = _CwrTlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 12),
    _CwrTlStatus_Type()
)
cwrTlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTlStatus.setStatus("current")


class _CwrTlPostTrigBufMgmt_Type(Integer32):
    """Custom type cwrTlPostTrigBufMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("postTrigger", 2),
          ("preTrigger", 1))
    )


_CwrTlPostTrigBufMgmt_Type.__name__ = "Integer32"
_CwrTlPostTrigBufMgmt_Object = MibTableColumn
cwrTlPostTrigBufMgmt = _CwrTlPostTrigBufMgmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 13),
    _CwrTlPostTrigBufMgmt_Type()
)
cwrTlPostTrigBufMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlPostTrigBufMgmt.setStatus("current")
_CwrTlRowStatus_Type = RowStatus
_CwrTlRowStatus_Object = MibTableColumn
cwrTlRowStatus = _CwrTlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 2, 1, 14),
    _CwrTlRowStatus_Type()
)
cwrTlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrTlRowStatus.setStatus("current")
_CwrTlSummaryTable_Object = MibTable
cwrTlSummaryTable = _CwrTlSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cwrTlSummaryTable.setStatus("current")
_CwrTlSummaryEntry_Object = MibTableRow
cwrTlSummaryEntry = _CwrTlSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 3, 1)
)
cwrTlSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrTlIndex"),
)
if mibBuilder.loadTexts:
    cwrTlSummaryEntry.setStatus("current")


class _CwrTlUpdateTime_Type(Integer32):
    """Custom type cwrTlUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrTlUpdateTime_Type.__name__ = "Integer32"
_CwrTlUpdateTime_Object = MibTableColumn
cwrTlUpdateTime = _CwrTlUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 3, 1, 1),
    _CwrTlUpdateTime_Type()
)
cwrTlUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTlUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    cwrTlUpdateTime.setUnits("seconds")


class _CwrTlNumValues_Type(Integer32):
    """Custom type cwrTlNumValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwrTlNumValues_Type.__name__ = "Integer32"
_CwrTlNumValues_Object = MibTableColumn
cwrTlNumValues = _CwrTlNumValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 3, 1, 2),
    _CwrTlNumValues_Type()
)
cwrTlNumValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTlNumValues.setStatus("current")


class _CwrTlTriggerLoc_Type(Integer32):
    """Custom type cwrTlTriggerLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrTlTriggerLoc_Type.__name__ = "Integer32"
_CwrTlTriggerLoc_Object = MibTableColumn
cwrTlTriggerLoc = _CwrTlTriggerLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 3, 1, 3),
    _CwrTlTriggerLoc_Type()
)
cwrTlTriggerLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTlTriggerLoc.setStatus("current")
_CwrTlDataTable_Object = MibTable
cwrTlDataTable = _CwrTlDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cwrTlDataTable.setStatus("current")
_CwrTlDataEntry_Object = MibTableRow
cwrTlDataEntry = _CwrTlDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 4, 1)
)
cwrTlDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrTlIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrTlValueIndex"),
)
if mibBuilder.loadTexts:
    cwrTlDataEntry.setStatus("current")


class _CwrTlValueIndex_Type(Integer32):
    """Custom type cwrTlValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrTlValueIndex_Type.__name__ = "Integer32"
_CwrTlValueIndex_Object = MibTableColumn
cwrTlValueIndex = _CwrTlValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 4, 1, 1),
    _CwrTlValueIndex_Type()
)
cwrTlValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrTlValueIndex.setStatus("current")


class _CwrTlValue_Type(Integer32):
    """Custom type cwrTlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrTlValue_Type.__name__ = "Integer32"
_CwrTlValue_Object = MibTableColumn
cwrTlValue = _CwrTlValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 8, 4, 1, 2),
    _CwrTlValue_Type()
)
cwrTlValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTlValue.setStatus("current")
_CwrRadioSnapshotGroup_ObjectIdentity = ObjectIdentity
cwrRadioSnapshotGroup = _CwrRadioSnapshotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9)
)
_CwrSnapshotCtrlTable_Object = MibTable
cwrSnapshotCtrlTable = _CwrSnapshotCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cwrSnapshotCtrlTable.setStatus("current")
_CwrSnapshotCtrlEntry_Object = MibTableRow
cwrSnapshotCtrlEntry = _CwrSnapshotCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1)
)
cwrSnapshotCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrSnapshotDspNum"),
)
if mibBuilder.loadTexts:
    cwrSnapshotCtrlEntry.setStatus("current")


class _CwrSnapshotDspNum_Type(Integer32):
    """Custom type cwrSnapshotDspNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CwrSnapshotDspNum_Type.__name__ = "Integer32"
_CwrSnapshotDspNum_Object = MibTableColumn
cwrSnapshotDspNum = _CwrSnapshotDspNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1, 1),
    _CwrSnapshotDspNum_Type()
)
cwrSnapshotDspNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrSnapshotDspNum.setStatus("current")


class _CwrSnapshotType_Type(Integer32):
    """Custom type cwrSnapshotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrSnapshotType_Type.__name__ = "Integer32"
_CwrSnapshotType_Object = MibTableColumn
cwrSnapshotType = _CwrSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1, 2),
    _CwrSnapshotType_Type()
)
cwrSnapshotType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrSnapshotType.setStatus("current")
_CwrSnapshotAction_Type = CwrCollectionAction
_CwrSnapshotAction_Object = MibTableColumn
cwrSnapshotAction = _CwrSnapshotAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1, 3),
    _CwrSnapshotAction_Type()
)
cwrSnapshotAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrSnapshotAction.setStatus("current")
_CwrSnapshotStatus_Type = CwrCollectionStatus
_CwrSnapshotStatus_Object = MibTableColumn
cwrSnapshotStatus = _CwrSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1, 4),
    _CwrSnapshotStatus_Type()
)
cwrSnapshotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapshotStatus.setStatus("current")
_CwrSnapshotRowStatus_Type = RowStatus
_CwrSnapshotRowStatus_Object = MibTableColumn
cwrSnapshotRowStatus = _CwrSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 1, 1, 5),
    _CwrSnapshotRowStatus_Type()
)
cwrSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrSnapshotRowStatus.setStatus("current")
_CwrSnapSummaryTable_Object = MibTable
cwrSnapSummaryTable = _CwrSnapSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cwrSnapSummaryTable.setStatus("current")
_CwrSnapSummaryEntry_Object = MibTableRow
cwrSnapSummaryEntry = _CwrSnapSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1)
)
cwrSnapSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrSnapshotDspNum"),
)
if mibBuilder.loadTexts:
    cwrSnapSummaryEntry.setStatus("current")


class _CwrSnapAttr1Id_Type(Integer32):
    """Custom type cwrSnapAttr1Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrSnapAttr1Id_Type.__name__ = "Integer32"
_CwrSnapAttr1Id_Object = MibTableColumn
cwrSnapAttr1Id = _CwrSnapAttr1Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 2),
    _CwrSnapAttr1Id_Type()
)
cwrSnapAttr1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr1Id.setStatus("current")


class _CwrSnapAttr1Size_Type(Integer32):
    """Custom type cwrSnapAttr1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CwrSnapAttr1Size_Type.__name__ = "Integer32"
_CwrSnapAttr1Size_Object = MibTableColumn
cwrSnapAttr1Size = _CwrSnapAttr1Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 3),
    _CwrSnapAttr1Size_Type()
)
cwrSnapAttr1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr1Size.setStatus("current")


class _CwrSnapAttr2Id_Type(Integer32):
    """Custom type cwrSnapAttr2Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrSnapAttr2Id_Type.__name__ = "Integer32"
_CwrSnapAttr2Id_Object = MibTableColumn
cwrSnapAttr2Id = _CwrSnapAttr2Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 4),
    _CwrSnapAttr2Id_Type()
)
cwrSnapAttr2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr2Id.setStatus("current")


class _CwrSnapAttr2Size_Type(Integer32):
    """Custom type cwrSnapAttr2Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CwrSnapAttr2Size_Type.__name__ = "Integer32"
_CwrSnapAttr2Size_Object = MibTableColumn
cwrSnapAttr2Size = _CwrSnapAttr2Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 5),
    _CwrSnapAttr2Size_Type()
)
cwrSnapAttr2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr2Size.setStatus("current")


class _CwrSnapAttr3Id_Type(Integer32):
    """Custom type cwrSnapAttr3Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrSnapAttr3Id_Type.__name__ = "Integer32"
_CwrSnapAttr3Id_Object = MibTableColumn
cwrSnapAttr3Id = _CwrSnapAttr3Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 6),
    _CwrSnapAttr3Id_Type()
)
cwrSnapAttr3Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr3Id.setStatus("current")


class _CwrSnapAttr3Size_Type(Integer32):
    """Custom type cwrSnapAttr3Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CwrSnapAttr3Size_Type.__name__ = "Integer32"
_CwrSnapAttr3Size_Object = MibTableColumn
cwrSnapAttr3Size = _CwrSnapAttr3Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 7),
    _CwrSnapAttr3Size_Type()
)
cwrSnapAttr3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr3Size.setStatus("current")


class _CwrSnapAttr4Id_Type(Integer32):
    """Custom type cwrSnapAttr4Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwrSnapAttr4Id_Type.__name__ = "Integer32"
_CwrSnapAttr4Id_Object = MibTableColumn
cwrSnapAttr4Id = _CwrSnapAttr4Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 8),
    _CwrSnapAttr4Id_Type()
)
cwrSnapAttr4Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr4Id.setStatus("current")


class _CwrSnapAttr4Size_Type(Integer32):
    """Custom type cwrSnapAttr4Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CwrSnapAttr4Size_Type.__name__ = "Integer32"
_CwrSnapAttr4Size_Object = MibTableColumn
cwrSnapAttr4Size = _CwrSnapAttr4Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 2, 1, 9),
    _CwrSnapAttr4Size_Type()
)
cwrSnapAttr4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrSnapAttr4Size.setStatus("current")
_CwrSnapDataTable_Object = MibTable
cwrSnapDataTable = _CwrSnapDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 3)
)
if mibBuilder.loadTexts:
    cwrSnapDataTable.setStatus("current")
_CwrSnapDataEntry_Object = MibTableRow
cwrSnapDataEntry = _CwrSnapDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 3, 1)
)
cwrSnapDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrSnapshotDspNum"),
    (0, "CISCO-WIRELESS-IF-MIB", "cwrSnapValueIndex"),
)
if mibBuilder.loadTexts:
    cwrSnapDataEntry.setStatus("current")


class _CwrSnapValueIndex_Type(Integer32):
    """Custom type cwrSnapValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CwrSnapValueIndex_Type.__name__ = "Integer32"
_CwrSnapValueIndex_Object = MibTableColumn
cwrSnapValueIndex = _CwrSnapValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 3, 1, 1),
    _CwrSnapValueIndex_Type()
)
cwrSnapValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrSnapValueIndex.setStatus("current")


class _CwrRealPart_Type(Integer32):
    """Custom type cwrRealPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrRealPart_Type.__name__ = "Integer32"
_CwrRealPart_Object = MibTableColumn
cwrRealPart = _CwrRealPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 3, 1, 2),
    _CwrRealPart_Type()
)
cwrRealPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrRealPart.setStatus("current")


class _CwrImaginaryPart_Type(Integer32):
    """Custom type cwrImaginaryPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CwrImaginaryPart_Type.__name__ = "Integer32"
_CwrImaginaryPart_Object = MibTableColumn
cwrImaginaryPart = _CwrImaginaryPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 9, 3, 1, 3),
    _CwrImaginaryPart_Type()
)
cwrImaginaryPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrImaginaryPart.setStatus("current")
_CwrRadioAntennaGroup_ObjectIdentity = ObjectIdentity
cwrRadioAntennaGroup = _CwrRadioAntennaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10)
)
_CwrAntennaTable_Object = MibTable
cwrAntennaTable = _CwrAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cwrAntennaTable.setStatus("current")
_CwrAntennaEntry_Object = MibTableRow
cwrAntennaEntry = _CwrAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1)
)
cwrAntennaEntry.setIndexNames(
    (0, "CISCO-WIRELESS-IF-MIB", "cwrAntennaIndex"),
)
if mibBuilder.loadTexts:
    cwrAntennaEntry.setStatus("current")


class _CwrAntennaIndex_Type(Integer32):
    """Custom type cwrAntennaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CwrAntennaIndex_Type.__name__ = "Integer32"
_CwrAntennaIndex_Object = MibTableColumn
cwrAntennaIndex = _CwrAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 1),
    _CwrAntennaIndex_Type()
)
cwrAntennaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwrAntennaIndex.setStatus("current")


class _CwrAntennaXDim_Type(Integer32):
    """Custom type cwrAntennaXDim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwrAntennaXDim_Type.__name__ = "Integer32"
_CwrAntennaXDim_Object = MibTableColumn
cwrAntennaXDim = _CwrAntennaXDim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 2),
    _CwrAntennaXDim_Type()
)
cwrAntennaXDim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaXDim.setStatus("current")
if mibBuilder.loadTexts:
    cwrAntennaXDim.setUnits("Inches")


class _CwrAntennaYDim_Type(Integer32):
    """Custom type cwrAntennaYDim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwrAntennaYDim_Type.__name__ = "Integer32"
_CwrAntennaYDim_Object = MibTableColumn
cwrAntennaYDim = _CwrAntennaYDim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 3),
    _CwrAntennaYDim_Type()
)
cwrAntennaYDim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaYDim.setStatus("current")
if mibBuilder.loadTexts:
    cwrAntennaYDim.setUnits("Inches")


class _CwrAntennaType_Type(DisplayString):
    """Custom type cwrAntennaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwrAntennaType_Type.__name__ = "DisplayString"
_CwrAntennaType_Object = MibTableColumn
cwrAntennaType = _CwrAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 4),
    _CwrAntennaType_Type()
)
cwrAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaType.setStatus("current")


class _CwrAntennaDescr_Type(DisplayString):
    """Custom type cwrAntennaDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwrAntennaDescr_Type.__name__ = "DisplayString"
_CwrAntennaDescr_Object = MibTableColumn
cwrAntennaDescr = _CwrAntennaDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 5),
    _CwrAntennaDescr_Type()
)
cwrAntennaDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaDescr.setStatus("current")


class _CwrAntennaGain_Type(Integer32):
    """Custom type cwrAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CwrAntennaGain_Type.__name__ = "Integer32"
_CwrAntennaGain_Object = MibTableColumn
cwrAntennaGain = _CwrAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 6),
    _CwrAntennaGain_Type()
)
cwrAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    cwrAntennaGain.setUnits("dBi : decibel Isotropic")


class _CwrAntennaPolarization_Type(Integer32):
    """Custom type cwrAntennaPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 2),
          ("vertical", 1))
    )


_CwrAntennaPolarization_Type.__name__ = "Integer32"
_CwrAntennaPolarization_Object = MibTableColumn
cwrAntennaPolarization = _CwrAntennaPolarization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 1, 10, 1, 1, 7),
    _CwrAntennaPolarization_Type()
)
cwrAntennaPolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrAntennaPolarization.setStatus("current")
_CwrRadioNotification_ObjectIdentity = ObjectIdentity
cwrRadioNotification = _CwrRadioNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2)
)
_CwrRadioLatestTrap_ObjectIdentity = ObjectIdentity
cwrRadioLatestTrap = _CwrRadioLatestTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 1)
)
_CwrRadioTrapTable_Object = MibTable
cwrRadioTrapTable = _CwrRadioTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwrRadioTrapTable.setStatus("current")
_CwrRadioTrapEntry_Object = MibTableRow
cwrRadioTrapEntry = _CwrRadioTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 1, 1, 1)
)
cwrRadioTrapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrRadioTrapEntry.setStatus("current")


class _CwrTrapReason_Type(DisplayString):
    """Custom type cwrTrapReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwrTrapReason_Type.__name__ = "DisplayString"
_CwrTrapReason_Object = MibTableColumn
cwrTrapReason = _CwrTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 1, 1, 1, 1),
    _CwrTrapReason_Type()
)
cwrTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrTrapReason.setStatus("current")
_CwrRadioDevTraps_ObjectIdentity = ObjectIdentity
cwrRadioDevTraps = _CwrRadioDevTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2)
)
_CwrRadioThreshTraps_ObjectIdentity = ObjectIdentity
cwrRadioThreshTraps = _CwrRadioThreshTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 3)
)
_CwrRadioIfConformance_ObjectIdentity = ObjectIdentity
cwrRadioIfConformance = _CwrRadioIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3)
)
_CwrRadioIfCompliances_ObjectIdentity = ObjectIdentity
cwrRadioIfCompliances = _CwrRadioIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 1)
)
_CwrRadioIfGroups_ObjectIdentity = ObjectIdentity
cwrRadioIfGroups = _CwrRadioIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2)
)

# Managed Objects groups

cwrComplianceRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 1)
)
cwrComplianceRadioGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrRadioNextIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAcquisitionMode"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSelfTest"),
        ("CISCO-WIRELESS-IF-MIB", "cwrBasePrivacySupport"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTxRfIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRx1RfIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRx2RfIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrClockRefExt"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntAlignment"),
        ("CISCO-WIRELESS-IF-MIB", "cwrNumRxAntenna"),
        ("CISCO-WIRELESS-IF-MIB", "cwrBandwidth"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThroughput"),
        ("CISCO-WIRELESS-IF-MIB", "cwrOperatingBand"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTxFrequency"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRxFrequency"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTxPower"),
        ("CISCO-WIRELESS-IF-MIB", "cwrCableLoss"),
        ("CISCO-WIRELESS-IF-MIB", "cwrOpStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrCableLossDiversity"),
        ("CISCO-WIRELESS-IF-MIB", "cwrBurstSize"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioGroup.setStatus("current")

cwrComplianceRadioPhyQualityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 2)
)
cwrComplianceRadioPhyQualityGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrArqPctBw"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqVoiceLatency"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqDataLatency"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqBurstSize"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqTypicalBitRate"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqMinBitRate"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqMaxLatencyJitter"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqReset"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArqOn"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioPhyQualityGroup.setStatus("current")

cwrComplianceRadioRfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 3)
)
cwrComplianceRadioRfGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrRfResIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRFOpMode"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTxFreqRangeMin"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTxFreqRangeMax"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRxFreqRangeMin"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRxFreqRangeMax"),
        ("CISCO-WIRELESS-IF-MIB", "cwrMinTxPower"),
        ("CISCO-WIRELESS-IF-MIB", "cwrMaxTxPower"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfTxOscState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfAntIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfRxOscState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfTemperature"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfSupplyVoltageState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfControlChannelStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrBurstSizeGroup"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfTxOscState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfRxOscState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfRefOscState"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfResIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfInpFreq"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfOutFreq"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioRfGroup.setStatus("current")

cwrComplianceReqLinkMetrics = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 4)
)
cwrComplianceReqLinkMetrics.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrLinkCwESThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLinkLowCwDSThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLinkHighCwDSThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLinkCSESThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink1HrESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink1HrSESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink1HrCSESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink1HrDCMAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink24HrESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink24HrSESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink24HrCSESAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLink24HrDCMAlarmThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAvailableSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrUnAvailableSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSyncLossSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctErrorFreeSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctSeverelyErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctAvailSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctCwDegradedMinutes"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSyncSuccessCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSyncFailureCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwrManagedSyncLoss"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAutomaticSyncLoss"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLastSyncSuccessTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrLastSyncFailTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrEffectivePhyDataRate"),
        ("CISCO-WIRELESS-IF-MIB", "cwrPctEffectivePhyDataRate"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrErrorFreeSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrSevErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrConsecSvErrSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrDegradedMinutes"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrTotalErroredCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr24HrTotalCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrErrorFreeSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrSevErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrConsecSvErrSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrDegradedMinutes"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrErroredCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1HrTotalCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinErrorFreeSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinSevErroredSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinConsecSvCwErrSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinDegradedSeconds"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinErroredCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1MinCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecRxCodewords"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecRSCodewordErrors"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecArqCodewordErrors"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecRxRrCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecRxRrEventCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecTxArqCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecTxArqEventCount"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecCorrectedSyncByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecConsecutiveCwErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwr1SecPostARQGoodCodewords"))
)
if mibBuilder.loadTexts:
    cwrComplianceReqLinkMetrics.setStatus("current")

cwrComplianceRadioTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 5)
)
cwrComplianceRadioTestGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrLocalLoopbackPoint"),
        ("CISCO-WIRELESS-IF-MIB", "cwrScopePortOn"),
        ("CISCO-WIRELESS-IF-MIB", "cwrScopePortDsp"),
        ("CISCO-WIRELESS-IF-MIB", "cwrScopePortAttribute"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioTestGroup.setStatus("current")

cwrComplianceHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 6)
)
cwrComplianceHistoryGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrHistClass"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfResourceId"),
        ("CISCO-WIRELESS-IF-MIB", "cwrDspNumber"),
        ("CISCO-WIRELESS-IF-MIB", "cwrStartBinValue"),
        ("CISCO-WIRELESS-IF-MIB", "cwrBinDelta"),
        ("CISCO-WIRELESS-IF-MIB", "cwrNumHistBins"),
        ("CISCO-WIRELESS-IF-MIB", "cwrUpdateRate"),
        ("CISCO-WIRELESS-IF-MIB", "cwrCollDuration"),
        ("CISCO-WIRELESS-IF-MIB", "cwrOwnerId"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistBitShift"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistToneSelection"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistToneValue"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistAction"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistRowStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistPeriodicSum"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistMin"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistMax"),
        ("CISCO-WIRELESS-IF-MIB", "cwrHistMean"),
        ("CISCO-WIRELESS-IF-MIB", "cwrValue"))
)
if mibBuilder.loadTexts:
    cwrComplianceHistoryGroup.setStatus("current")

cwrComplianceRadioTlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 7)
)
cwrComplianceRadioTlGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrThreshAttribute"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshType"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshAntId"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshValue"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshHysteresisTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshLimitTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshRowStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshDspNum"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlClass"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlRfResourceId"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlDspNum"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlNumDataValues"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlDecimationFactor"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlPreSumShift"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlToneSelection"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlToneValue"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlThreshIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlAction"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlPostTrigBufMgmt"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlRowStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlUpdateTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlNumValues"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlTriggerLoc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTlValue"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioTlGroup.setStatus("current")

cwrComplianceRadioSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 8)
)
cwrComplianceRadioSnapshotGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrSnapshotType"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapshotAction"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapshotStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapshotRowStatus"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr1Id"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr1Size"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr2Id"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr2Size"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr3Id"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr3Size"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr4Id"),
        ("CISCO-WIRELESS-IF-MIB", "cwrSnapAttr4Size"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRealPart"),
        ("CISCO-WIRELESS-IF-MIB", "cwrImaginaryPart"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioSnapshotGroup.setStatus("current")

cwrComplianceRadioAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 9)
)
cwrComplianceRadioAntennaGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrAntennaXDim"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntennaYDim"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntennaType"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntennaDescr"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntennaGain"),
        ("CISCO-WIRELESS-IF-MIB", "cwrAntennaPolarization"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioAntennaGroup.setStatus("current")

cwrComplianceRadioPhyByteErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 10)
)
cwrComplianceRadioPhyByteErrGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrArq1ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq2ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq3ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq4ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq5ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq6ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq7ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq8ByteErrs"),
        ("CISCO-WIRELESS-IF-MIB", "cwrArq9ByteErrs"))
)
if mibBuilder.loadTexts:
    cwrComplianceRadioPhyByteErrGroup.setStatus("current")


# Notification objects

cwrTrapConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 1)
)
cwrTrapConfigMismatch.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrTrapConfigMismatch.setStatus(
        "current"
    )

cwrTrapInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 2)
)
cwrTrapInitFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrTrapInitFailure.setStatus(
        "current"
    )

cwrTrapLinkQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 3)
)
cwrTrapLinkQuality.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrTrapLinkQuality.setStatus(
        "current"
    )

cwrTrapLinkSyncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 4)
)
cwrTrapLinkSyncLost.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    cwrTrapLinkSyncLost.setStatus(
        "current"
    )

cwrTrapLinkSyncAcquired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 5)
)
cwrTrapLinkSyncAcquired.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    cwrTrapLinkSyncAcquired.setStatus(
        "current"
    )

cwrTrapIfRxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 6)
)
cwrTrapIfRxOsc.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfRxOscState"))
)
if mibBuilder.loadTexts:
    cwrTrapIfRxOsc.setStatus(
        "current"
    )

cwrTrapIfTxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 7)
)
cwrTrapIfTxOsc.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfTxOscState"))
)
if mibBuilder.loadTexts:
    cwrTrapIfTxOsc.setStatus(
        "current"
    )

cwrTrapIfRefOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 8)
)
cwrTrapIfRefOsc.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrIfRefOscState"))
)
if mibBuilder.loadTexts:
    cwrTrapIfRefOsc.setStatus(
        "current"
    )

cwrTrapRfSupplyVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 9)
)
cwrTrapRfSupplyVoltage.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfSupplyVoltageState"))
)
if mibBuilder.loadTexts:
    cwrTrapRfSupplyVoltage.setStatus(
        "current"
    )

cwrTrapRfRxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 10)
)
cwrTrapRfRxOsc.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfRxOscState"))
)
if mibBuilder.loadTexts:
    cwrTrapRfRxOsc.setStatus(
        "current"
    )

cwrTrapRfTxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 11)
)
cwrTrapRfTxOsc.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfTxOscState"))
)
if mibBuilder.loadTexts:
    cwrTrapRfTxOsc.setStatus(
        "current"
    )

cwrTrapRfTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 12)
)
cwrTrapRfTemp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfTemperature"))
)
if mibBuilder.loadTexts:
    cwrTrapRfTemp.setStatus(
        "current"
    )

cwrTrapRfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 13)
)
cwrTrapRfStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrRfStatus"))
)
if mibBuilder.loadTexts:
    cwrTrapRfStatusChange.setStatus(
        "current"
    )

cwrTrapLink1HrThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 14)
)
cwrTrapLink1HrThresh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrTrapLink1HrThresh.setStatus(
        "current"
    )

cwrTrapLink24HrThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 2, 15)
)
cwrTrapLink24HrThresh.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapReason"))
)
if mibBuilder.loadTexts:
    cwrTrapLink24HrThresh.setStatus(
        "current"
    )

cwrTrapThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 2, 3, 1)
)
cwrTrapThresh.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrThreshValue"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshHysteresisTime"),
        ("CISCO-WIRELESS-IF-MIB", "cwrThreshLimitTime"))
)
if mibBuilder.loadTexts:
    cwrTrapThresh.setStatus(
        "current"
    )


# Notifications groups

cwrComplianceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 2, 11)
)
cwrComplianceNotifGroup.setObjects(
      *(("CISCO-WIRELESS-IF-MIB", "cwrTrapConfigMismatch"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapInitFailure"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapLinkQuality"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapLinkSyncLost"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapLinkSyncAcquired"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapIfRxOsc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapIfTxOsc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapIfRefOsc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapRfSupplyVoltage"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapRfRxOsc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapRfTxOsc"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapRfTemp"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapRfStatusChange"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapLink1HrThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapLink24HrThresh"),
        ("CISCO-WIRELESS-IF-MIB", "cwrTrapThresh"))
)
if mibBuilder.loadTexts:
    cwrComplianceNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cwrRadioBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 136, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwrRadioBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-IF-MIB",
    **{"ciscoWirelessIfMIB": ciscoWirelessIfMIB,
       "cwrRadioMibObjects": cwrRadioMibObjects,
       "cwrRadioInternal": cwrRadioInternal,
       "cwrTestGroup": cwrTestGroup,
       "cwrLoopbackTable": cwrLoopbackTable,
       "cwrLoopbackEntry": cwrLoopbackEntry,
       "cwrLocalLoopbackPoint": cwrLocalLoopbackPoint,
       "cwrScopePortTable": cwrScopePortTable,
       "cwrScopePortEntry": cwrScopePortEntry,
       "cwrScopePortOn": cwrScopePortOn,
       "cwrScopePortDsp": cwrScopePortDsp,
       "cwrScopePortAttribute": cwrScopePortAttribute,
       "cwrRadioCommon": cwrRadioCommon,
       "cwrRadioNextIndex": cwrRadioNextIndex,
       "cwrRadioBaseGroup": cwrRadioBaseGroup,
       "cwrRadioBaseTable": cwrRadioBaseTable,
       "cwrRadioBaseEntry": cwrRadioBaseEntry,
       "cwrAcquisitionMode": cwrAcquisitionMode,
       "cwrSelfTest": cwrSelfTest,
       "cwrBasePrivacySupport": cwrBasePrivacySupport,
       "cwrTxRfIndex": cwrTxRfIndex,
       "cwrRx1RfIndex": cwrRx1RfIndex,
       "cwrRx2RfIndex": cwrRx2RfIndex,
       "cwrClockRefExt": cwrClockRefExt,
       "cwrAntAlignment": cwrAntAlignment,
       "cwrRadioPhyTable": cwrRadioPhyTable,
       "cwrRadioPhyEntry": cwrRadioPhyEntry,
       "cwrNumRxAntenna": cwrNumRxAntenna,
       "cwrBandwidth": cwrBandwidth,
       "cwrThroughput": cwrThroughput,
       "cwrOperatingBand": cwrOperatingBand,
       "cwrTxFrequency": cwrTxFrequency,
       "cwrRxFrequency": cwrRxFrequency,
       "cwrTxPower": cwrTxPower,
       "cwrCableLoss": cwrCableLoss,
       "cwrOpStatus": cwrOpStatus,
       "cwrCableLossDiversity": cwrCableLossDiversity,
       "cwrBurstSize": cwrBurstSize,
       "cwrRadioPhyQualityGroup": cwrRadioPhyQualityGroup,
       "cwrPhyQualityTable": cwrPhyQualityTable,
       "cwrPhyQualityEntry": cwrPhyQualityEntry,
       "cwrArqPctBw": cwrArqPctBw,
       "cwrArqVoiceLatency": cwrArqVoiceLatency,
       "cwrArqDataLatency": cwrArqDataLatency,
       "cwrArqBurstSize": cwrArqBurstSize,
       "cwrArqTypicalBitRate": cwrArqTypicalBitRate,
       "cwrArqMinBitRate": cwrArqMinBitRate,
       "cwrArqMaxLatencyJitter": cwrArqMaxLatencyJitter,
       "cwrArqReset": cwrArqReset,
       "cwrArqOn": cwrArqOn,
       "cwrPhyCorrectedBytesTable": cwrPhyCorrectedBytesTable,
       "cwrPhyCorrectedBytesEntry": cwrPhyCorrectedBytesEntry,
       "cwrArq1ByteErrs": cwrArq1ByteErrs,
       "cwrArq2ByteErrs": cwrArq2ByteErrs,
       "cwrArq3ByteErrs": cwrArq3ByteErrs,
       "cwrArq4ByteErrs": cwrArq4ByteErrs,
       "cwrArq5ByteErrs": cwrArq5ByteErrs,
       "cwrArq6ByteErrs": cwrArq6ByteErrs,
       "cwrArq7ByteErrs": cwrArq7ByteErrs,
       "cwrArq8ByteErrs": cwrArq8ByteErrs,
       "cwrArq9ByteErrs": cwrArq9ByteErrs,
       "cwrRadioFreqResGroup": cwrRadioFreqResGroup,
       "cwrRfTable": cwrRfTable,
       "cwrRfEntry": cwrRfEntry,
       "cwrRfIndex": cwrRfIndex,
       "cwrRfResIndex": cwrRfResIndex,
       "cwrRFOpMode": cwrRFOpMode,
       "cwrTxFreqRangeMin": cwrTxFreqRangeMin,
       "cwrTxFreqRangeMax": cwrTxFreqRangeMax,
       "cwrRxFreqRangeMin": cwrRxFreqRangeMin,
       "cwrRxFreqRangeMax": cwrRxFreqRangeMax,
       "cwrMinTxPower": cwrMinTxPower,
       "cwrMaxTxPower": cwrMaxTxPower,
       "cwrRfTxOscState": cwrRfTxOscState,
       "cwrRfAntIndex": cwrRfAntIndex,
       "cwrRfRxOscState": cwrRfRxOscState,
       "cwrRfTemperature": cwrRfTemperature,
       "cwrRfSupplyVoltageState": cwrRfSupplyVoltageState,
       "cwrRfStatus": cwrRfStatus,
       "cwrRfControlChannelStatus": cwrRfControlChannelStatus,
       "cwrBurstSizeGroup": cwrBurstSizeGroup,
       "cwrIntFreqTable": cwrIntFreqTable,
       "cwrIntFreqEntry": cwrIntFreqEntry,
       "cwrIfTxOscState": cwrIfTxOscState,
       "cwrIfRxOscState": cwrIfRxOscState,
       "cwrIfRefOscState": cwrIfRefOscState,
       "cwrIfResIndex": cwrIfResIndex,
       "cwrIfInpFreq": cwrIfInpFreq,
       "cwrIfOutFreq": cwrIfOutFreq,
       "cwrRadioMetricsGroup": cwrRadioMetricsGroup,
       "cwrLinkMetricsThresholdTable": cwrLinkMetricsThresholdTable,
       "cwrLinkMetricsThreshEntry": cwrLinkMetricsThreshEntry,
       "cwrLinkCwESThresh": cwrLinkCwESThresh,
       "cwrLinkLowCwDSThresh": cwrLinkLowCwDSThresh,
       "cwrLinkHighCwDSThresh": cwrLinkHighCwDSThresh,
       "cwrLinkCSESThresh": cwrLinkCSESThresh,
       "cwrLink1HrESAlarmThresh": cwrLink1HrESAlarmThresh,
       "cwrLink1HrSESAlarmThresh": cwrLink1HrSESAlarmThresh,
       "cwrLink1HrCSESAlarmThresh": cwrLink1HrCSESAlarmThresh,
       "cwrLink1HrDCMAlarmThresh": cwrLink1HrDCMAlarmThresh,
       "cwrLink24HrESAlarmThresh": cwrLink24HrESAlarmThresh,
       "cwrLink24HrSESAlarmThresh": cwrLink24HrSESAlarmThresh,
       "cwrLink24HrCSESAlarmThresh": cwrLink24HrCSESAlarmThresh,
       "cwrLink24HrDCMAlarmThresh": cwrLink24HrDCMAlarmThresh,
       "cwrCumulativeMetricsTable": cwrCumulativeMetricsTable,
       "cwrCumulativeMetricsEntry": cwrCumulativeMetricsEntry,
       "cwrAvailableSeconds": cwrAvailableSeconds,
       "cwrUnAvailableSeconds": cwrUnAvailableSeconds,
       "cwrSyncLossSeconds": cwrSyncLossSeconds,
       "cwrPctErrorFreeSeconds": cwrPctErrorFreeSeconds,
       "cwrPctErroredSeconds": cwrPctErroredSeconds,
       "cwrPctSeverelyErroredSeconds": cwrPctSeverelyErroredSeconds,
       "cwrPctAvailSeconds": cwrPctAvailSeconds,
       "cwrPctCwDegradedMinutes": cwrPctCwDegradedMinutes,
       "cwrSyncSuccessCount": cwrSyncSuccessCount,
       "cwrSyncFailureCount": cwrSyncFailureCount,
       "cwrManagedSyncLoss": cwrManagedSyncLoss,
       "cwrAutomaticSyncLoss": cwrAutomaticSyncLoss,
       "cwrLastSyncSuccessTime": cwrLastSyncSuccessTime,
       "cwrLastSyncFailTime": cwrLastSyncFailTime,
       "cwrEffectivePhyDataRate": cwrEffectivePhyDataRate,
       "cwrPctEffectivePhyDataRate": cwrPctEffectivePhyDataRate,
       "cwr24HrMetricsTable": cwr24HrMetricsTable,
       "cwr24HrMetricsEntry": cwr24HrMetricsEntry,
       "cwr24HrMetricsIndex": cwr24HrMetricsIndex,
       "cwr24HrUpdateTime": cwr24HrUpdateTime,
       "cwr24HrErrorFreeSeconds": cwr24HrErrorFreeSeconds,
       "cwr24HrErroredSeconds": cwr24HrErroredSeconds,
       "cwr24HrSevErroredSeconds": cwr24HrSevErroredSeconds,
       "cwr24HrConsecSvErrSeconds": cwr24HrConsecSvErrSeconds,
       "cwr24HrDegradedMinutes": cwr24HrDegradedMinutes,
       "cwr24HrTotalErroredCodewords": cwr24HrTotalErroredCodewords,
       "cwr24HrTotalCodewords": cwr24HrTotalCodewords,
       "cwr1HrMetricsTable": cwr1HrMetricsTable,
       "cwr1HrMetricsEntry": cwr1HrMetricsEntry,
       "cwr1HrMetricsIndex": cwr1HrMetricsIndex,
       "cwr1HrUpdateTime": cwr1HrUpdateTime,
       "cwr1HrErrorFreeSeconds": cwr1HrErrorFreeSeconds,
       "cwr1HrErroredSeconds": cwr1HrErroredSeconds,
       "cwr1HrSevErroredSeconds": cwr1HrSevErroredSeconds,
       "cwr1HrConsecSvErrSeconds": cwr1HrConsecSvErrSeconds,
       "cwr1HrDegradedMinutes": cwr1HrDegradedMinutes,
       "cwr1HrErroredCodewords": cwr1HrErroredCodewords,
       "cwr1HrTotalCodewords": cwr1HrTotalCodewords,
       "cwr1MinMetricsTable": cwr1MinMetricsTable,
       "cwr1MinMetricsEntry": cwr1MinMetricsEntry,
       "cwr1MinMetricsIndex": cwr1MinMetricsIndex,
       "cwr1MinUpdateTime": cwr1MinUpdateTime,
       "cwr1MinErrorFreeSeconds": cwr1MinErrorFreeSeconds,
       "cwr1MinErroredSeconds": cwr1MinErroredSeconds,
       "cwr1MinSevErroredSeconds": cwr1MinSevErroredSeconds,
       "cwr1MinConsecSvCwErrSeconds": cwr1MinConsecSvCwErrSeconds,
       "cwr1MinDegradedSeconds": cwr1MinDegradedSeconds,
       "cwr1MinErroredCodewords": cwr1MinErroredCodewords,
       "cwr1MinCodewords": cwr1MinCodewords,
       "cwr1SecMetricsTable": cwr1SecMetricsTable,
       "cwr1SecMetricsEntry": cwr1SecMetricsEntry,
       "cwr1SecIndex": cwr1SecIndex,
       "cwr1SecUpdateTime": cwr1SecUpdateTime,
       "cwr1SecRxCodewords": cwr1SecRxCodewords,
       "cwr1SecRSCodewordErrors": cwr1SecRSCodewordErrors,
       "cwr1SecArqCodewordErrors": cwr1SecArqCodewordErrors,
       "cwr1SecRxRrCount": cwr1SecRxRrCount,
       "cwr1SecRxRrEventCount": cwr1SecRxRrEventCount,
       "cwr1SecTxArqCount": cwr1SecTxArqCount,
       "cwr1SecTxArqEventCount": cwr1SecTxArqEventCount,
       "cwr1SecCorrectedSyncByteErrs": cwr1SecCorrectedSyncByteErrs,
       "cwr1SecConsecutiveCwErrs": cwr1SecConsecutiveCwErrs,
       "cwr1SecPostARQGoodCodewords": cwr1SecPostARQGoodCodewords,
       "cwrRadioHistoryGroup": cwrRadioHistoryGroup,
       "cwrHistCtrlTable": cwrHistCtrlTable,
       "cwrHistCtrlEntry": cwrHistCtrlEntry,
       "cwrHistIndex": cwrHistIndex,
       "cwrHistClass": cwrHistClass,
       "cwrRfResourceId": cwrRfResourceId,
       "cwrDspNumber": cwrDspNumber,
       "cwrStartBinValue": cwrStartBinValue,
       "cwrBinDelta": cwrBinDelta,
       "cwrNumHistBins": cwrNumHistBins,
       "cwrUpdateRate": cwrUpdateRate,
       "cwrCollDuration": cwrCollDuration,
       "cwrOwnerId": cwrOwnerId,
       "cwrHistBitShift": cwrHistBitShift,
       "cwrHistToneSelection": cwrHistToneSelection,
       "cwrHistToneValue": cwrHistToneValue,
       "cwrHistAction": cwrHistAction,
       "cwrHistStatus": cwrHistStatus,
       "cwrHistRowStatus": cwrHistRowStatus,
       "cwrHistPeriodicSum": cwrHistPeriodicSum,
       "cwrHistSummaryTable": cwrHistSummaryTable,
       "cwrHistSummaryEntry": cwrHistSummaryEntry,
       "cwrHistUpdateTime": cwrHistUpdateTime,
       "cwrHistMin": cwrHistMin,
       "cwrHistMax": cwrHistMax,
       "cwrHistMean": cwrHistMean,
       "cwrHistDataTable": cwrHistDataTable,
       "cwrHistDataEntry": cwrHistDataEntry,
       "cwrHistBinIndex": cwrHistBinIndex,
       "cwrValue": cwrValue,
       "cwrRadioTimelineGroup": cwrRadioTimelineGroup,
       "cwrThresholdTable": cwrThresholdTable,
       "cwrThresholdEntry": cwrThresholdEntry,
       "cwrThreshIndex": cwrThreshIndex,
       "cwrThreshAttribute": cwrThreshAttribute,
       "cwrThreshType": cwrThreshType,
       "cwrThreshAntId": cwrThreshAntId,
       "cwrThreshValue": cwrThreshValue,
       "cwrThreshHysteresisTime": cwrThreshHysteresisTime,
       "cwrThreshLimitTime": cwrThreshLimitTime,
       "cwrThreshDspNum": cwrThreshDspNum,
       "cwrThreshRowStatus": cwrThreshRowStatus,
       "cwrTlCtrlTable": cwrTlCtrlTable,
       "cwrTlCtrlEntry": cwrTlCtrlEntry,
       "cwrTlIndex": cwrTlIndex,
       "cwrTlClass": cwrTlClass,
       "cwrTlRfResourceId": cwrTlRfResourceId,
       "cwrTlDspNum": cwrTlDspNum,
       "cwrTlNumDataValues": cwrTlNumDataValues,
       "cwrTlDecimationFactor": cwrTlDecimationFactor,
       "cwrTlPreSumShift": cwrTlPreSumShift,
       "cwrTlToneSelection": cwrTlToneSelection,
       "cwrTlToneValue": cwrTlToneValue,
       "cwrTlThreshIndex": cwrTlThreshIndex,
       "cwrTlAction": cwrTlAction,
       "cwrTlStatus": cwrTlStatus,
       "cwrTlPostTrigBufMgmt": cwrTlPostTrigBufMgmt,
       "cwrTlRowStatus": cwrTlRowStatus,
       "cwrTlSummaryTable": cwrTlSummaryTable,
       "cwrTlSummaryEntry": cwrTlSummaryEntry,
       "cwrTlUpdateTime": cwrTlUpdateTime,
       "cwrTlNumValues": cwrTlNumValues,
       "cwrTlTriggerLoc": cwrTlTriggerLoc,
       "cwrTlDataTable": cwrTlDataTable,
       "cwrTlDataEntry": cwrTlDataEntry,
       "cwrTlValueIndex": cwrTlValueIndex,
       "cwrTlValue": cwrTlValue,
       "cwrRadioSnapshotGroup": cwrRadioSnapshotGroup,
       "cwrSnapshotCtrlTable": cwrSnapshotCtrlTable,
       "cwrSnapshotCtrlEntry": cwrSnapshotCtrlEntry,
       "cwrSnapshotDspNum": cwrSnapshotDspNum,
       "cwrSnapshotType": cwrSnapshotType,
       "cwrSnapshotAction": cwrSnapshotAction,
       "cwrSnapshotStatus": cwrSnapshotStatus,
       "cwrSnapshotRowStatus": cwrSnapshotRowStatus,
       "cwrSnapSummaryTable": cwrSnapSummaryTable,
       "cwrSnapSummaryEntry": cwrSnapSummaryEntry,
       "cwrSnapAttr1Id": cwrSnapAttr1Id,
       "cwrSnapAttr1Size": cwrSnapAttr1Size,
       "cwrSnapAttr2Id": cwrSnapAttr2Id,
       "cwrSnapAttr2Size": cwrSnapAttr2Size,
       "cwrSnapAttr3Id": cwrSnapAttr3Id,
       "cwrSnapAttr3Size": cwrSnapAttr3Size,
       "cwrSnapAttr4Id": cwrSnapAttr4Id,
       "cwrSnapAttr4Size": cwrSnapAttr4Size,
       "cwrSnapDataTable": cwrSnapDataTable,
       "cwrSnapDataEntry": cwrSnapDataEntry,
       "cwrSnapValueIndex": cwrSnapValueIndex,
       "cwrRealPart": cwrRealPart,
       "cwrImaginaryPart": cwrImaginaryPart,
       "cwrRadioAntennaGroup": cwrRadioAntennaGroup,
       "cwrAntennaTable": cwrAntennaTable,
       "cwrAntennaEntry": cwrAntennaEntry,
       "cwrAntennaIndex": cwrAntennaIndex,
       "cwrAntennaXDim": cwrAntennaXDim,
       "cwrAntennaYDim": cwrAntennaYDim,
       "cwrAntennaType": cwrAntennaType,
       "cwrAntennaDescr": cwrAntennaDescr,
       "cwrAntennaGain": cwrAntennaGain,
       "cwrAntennaPolarization": cwrAntennaPolarization,
       "cwrRadioNotification": cwrRadioNotification,
       "cwrRadioLatestTrap": cwrRadioLatestTrap,
       "cwrRadioTrapTable": cwrRadioTrapTable,
       "cwrRadioTrapEntry": cwrRadioTrapEntry,
       "cwrTrapReason": cwrTrapReason,
       "cwrRadioDevTraps": cwrRadioDevTraps,
       "cwrTrapConfigMismatch": cwrTrapConfigMismatch,
       "cwrTrapInitFailure": cwrTrapInitFailure,
       "cwrTrapLinkQuality": cwrTrapLinkQuality,
       "cwrTrapLinkSyncLost": cwrTrapLinkSyncLost,
       "cwrTrapLinkSyncAcquired": cwrTrapLinkSyncAcquired,
       "cwrTrapIfRxOsc": cwrTrapIfRxOsc,
       "cwrTrapIfTxOsc": cwrTrapIfTxOsc,
       "cwrTrapIfRefOsc": cwrTrapIfRefOsc,
       "cwrTrapRfSupplyVoltage": cwrTrapRfSupplyVoltage,
       "cwrTrapRfRxOsc": cwrTrapRfRxOsc,
       "cwrTrapRfTxOsc": cwrTrapRfTxOsc,
       "cwrTrapRfTemp": cwrTrapRfTemp,
       "cwrTrapRfStatusChange": cwrTrapRfStatusChange,
       "cwrTrapLink1HrThresh": cwrTrapLink1HrThresh,
       "cwrTrapLink24HrThresh": cwrTrapLink24HrThresh,
       "cwrRadioThreshTraps": cwrRadioThreshTraps,
       "cwrTrapThresh": cwrTrapThresh,
       "cwrRadioIfConformance": cwrRadioIfConformance,
       "cwrRadioIfCompliances": cwrRadioIfCompliances,
       "cwrRadioBasicCompliance": cwrRadioBasicCompliance,
       "cwrRadioIfGroups": cwrRadioIfGroups,
       "cwrComplianceRadioGroup": cwrComplianceRadioGroup,
       "cwrComplianceRadioPhyQualityGroup": cwrComplianceRadioPhyQualityGroup,
       "cwrComplianceRadioRfGroup": cwrComplianceRadioRfGroup,
       "cwrComplianceReqLinkMetrics": cwrComplianceReqLinkMetrics,
       "cwrComplianceRadioTestGroup": cwrComplianceRadioTestGroup,
       "cwrComplianceHistoryGroup": cwrComplianceHistoryGroup,
       "cwrComplianceRadioTlGroup": cwrComplianceRadioTlGroup,
       "cwrComplianceRadioSnapshotGroup": cwrComplianceRadioSnapshotGroup,
       "cwrComplianceRadioAntennaGroup": cwrComplianceRadioAntennaGroup,
       "cwrComplianceRadioPhyByteErrGroup": cwrComplianceRadioPhyByteErrGroup,
       "cwrComplianceNotifGroup": cwrComplianceNotifGroup}
)
