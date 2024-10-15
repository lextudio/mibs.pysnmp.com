# SNMP MIB module (COM21-HCXSTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXSTU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:37 2024
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

(com21,
 com21Hcx,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxStu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 50)
)


# Types definitions



class FrequencyKhz(Integer32):
    """Custom type FrequencyKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800000),
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )





class StuGain(Integer32):
    """Custom type StuGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 58),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxStuStatusGroup_ObjectIdentity = ObjectIdentity
com21HcxStuStatusGroup = _Com21HcxStuStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51)
)
_Com21HcxStuStatusTable_Object = MibTable
com21HcxStuStatusTable = _Com21HcxStuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuStatusTable.setStatus("current")
_Com21HcxStuStatusEntry_Object = MibTableRow
com21HcxStuStatusEntry = _Com21HcxStuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1)
)
com21HcxStuStatusEntry.setIndexNames(
    (0, "COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"),
)
if mibBuilder.loadTexts:
    com21HcxStuStatusEntry.setStatus("current")
_HcxStuStatusMacAddr_Type = MacAddress
_HcxStuStatusMacAddr_Object = MibTableColumn
hcxStuStatusMacAddr = _HcxStuStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 1),
    _HcxStuStatusMacAddr_Type()
)
hcxStuStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuStatusMacAddr.setStatus("current")


class _HcxStuConfigured_Type(Integer32):
    """Custom type hcxStuConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuConfigured_Type.__name__ = "Integer32"
_HcxStuConfigured_Object = MibTableColumn
hcxStuConfigured = _HcxStuConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 2),
    _HcxStuConfigured_Type()
)
hcxStuConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxStuConfigured.setStatus("current")


class _HcxStuAcquired_Type(Integer32):
    """Custom type hcxStuAcquired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuAcquired_Type.__name__ = "Integer32"
_HcxStuAcquired_Object = MibTableColumn
hcxStuAcquired = _HcxStuAcquired_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 3),
    _HcxStuAcquired_Type()
)
hcxStuAcquired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuAcquired.setStatus("current")


class _HcxStuAcqFailInfo_Type(Integer32):
    """Custom type hcxStuAcqFailInfo based on Integer32"""
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
        *(("bandwidthUnavail", 4),
          ("noFailure", 1),
          ("servGrpInvalid", 3),
          ("unauthorized", 5),
          ("vlanFailure", 2))
    )


_HcxStuAcqFailInfo_Type.__name__ = "Integer32"
_HcxStuAcqFailInfo_Object = MibTableColumn
hcxStuAcqFailInfo = _HcxStuAcqFailInfo_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 4),
    _HcxStuAcqFailInfo_Type()
)
hcxStuAcqFailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuAcqFailInfo.setStatus("current")


class _HcxStuAuthorized_Type(Integer32):
    """Custom type hcxStuAuthorized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuAuthorized_Type.__name__ = "Integer32"
_HcxStuAuthorized_Object = MibTableColumn
hcxStuAuthorized = _HcxStuAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 5),
    _HcxStuAuthorized_Type()
)
hcxStuAuthorized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAuthorized.setStatus("current")


class _HcxStuLedFlashTest_Type(Integer32):
    """Custom type hcxStuLedFlashTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("start", 2),
          ("stop", 3))
    )


_HcxStuLedFlashTest_Type.__name__ = "Integer32"
_HcxStuLedFlashTest_Object = MibTableColumn
hcxStuLedFlashTest = _HcxStuLedFlashTest_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 6),
    _HcxStuLedFlashTest_Type()
)
hcxStuLedFlashTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuLedFlashTest.setStatus("current")


class _HcxStuUpstreamTest_Type(Integer32):
    """Custom type hcxStuUpstreamTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("start", 2),
          ("stop", 3))
    )


_HcxStuUpstreamTest_Type.__name__ = "Integer32"
_HcxStuUpstreamTest_Object = MibTableColumn
hcxStuUpstreamTest = _HcxStuUpstreamTest_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 7),
    _HcxStuUpstreamTest_Type()
)
hcxStuUpstreamTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuUpstreamTest.setStatus("current")


class _HcxStuVlanId_Type(Integer32):
    """Custom type hcxStuVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HcxStuVlanId_Type.__name__ = "Integer32"
_HcxStuVlanId_Object = MibTableColumn
hcxStuVlanId = _HcxStuVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 8),
    _HcxStuVlanId_Type()
)
hcxStuVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuVlanId.setStatus("current")


class _HcxStuRxShelfId_Type(Integer32):
    """Custom type hcxStuRxShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HcxStuRxShelfId_Type.__name__ = "Integer32"
_HcxStuRxShelfId_Object = MibTableColumn
hcxStuRxShelfId = _HcxStuRxShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 9),
    _HcxStuRxShelfId_Type()
)
hcxStuRxShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuRxShelfId.setStatus("current")


class _HcxStuRxSlotId_Type(Integer32):
    """Custom type hcxStuRxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HcxStuRxSlotId_Type.__name__ = "Integer32"
_HcxStuRxSlotId_Object = MibTableColumn
hcxStuRxSlotId = _HcxStuRxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 10),
    _HcxStuRxSlotId_Type()
)
hcxStuRxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuRxSlotId.setStatus("current")


class _HcxStuRxPortId_Type(Integer32):
    """Custom type hcxStuRxPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HcxStuRxPortId_Type.__name__ = "Integer32"
_HcxStuRxPortId_Object = MibTableColumn
hcxStuRxPortId = _HcxStuRxPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 11),
    _HcxStuRxPortId_Type()
)
hcxStuRxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuRxPortId.setStatus("current")
_HcxStuServiceType_Type = Integer32
_HcxStuServiceType_Object = MibTableColumn
hcxStuServiceType = _HcxStuServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 12),
    _HcxStuServiceType_Type()
)
hcxStuServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuServiceType.setStatus("current")


class _HcxStuConfSwImage_Type(DisplayString):
    """Custom type hcxStuConfSwImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxStuConfSwImage_Type.__name__ = "DisplayString"
_HcxStuConfSwImage_Object = MibTableColumn
hcxStuConfSwImage = _HcxStuConfSwImage_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 14),
    _HcxStuConfSwImage_Type()
)
hcxStuConfSwImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuConfSwImage.setStatus("current")


class _HcxStuPingTestAction_Type(Integer32):
    """Custom type hcxStuPingTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxStuPingTestAction_Type.__name__ = "Integer32"
_HcxStuPingTestAction_Object = MibTableColumn
hcxStuPingTestAction = _HcxStuPingTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 15),
    _HcxStuPingTestAction_Type()
)
hcxStuPingTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuPingTestAction.setStatus("current")


class _HcxStuPingTestResult_Type(Integer32):
    """Custom type hcxStuPingTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inprogress", 1),
          ("success", 2))
    )


_HcxStuPingTestResult_Type.__name__ = "Integer32"
_HcxStuPingTestResult_Object = MibTableColumn
hcxStuPingTestResult = _HcxStuPingTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 16),
    _HcxStuPingTestResult_Type()
)
hcxStuPingTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuPingTestResult.setStatus("current")


class _HcxStuEthTestAction_Type(Integer32):
    """Custom type hcxStuEthTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnStrmTest", 3),
          ("lpBkTest", 2),
          ("nil", 1))
    )


_HcxStuEthTestAction_Type.__name__ = "Integer32"
_HcxStuEthTestAction_Object = MibTableColumn
hcxStuEthTestAction = _HcxStuEthTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 17),
    _HcxStuEthTestAction_Type()
)
hcxStuEthTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuEthTestAction.setStatus("current")


class _HcxStuEthTestResult_Type(Integer32):
    """Custom type hcxStuEthTestResult based on Integer32"""
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
        *(("corruptPacket", 4),
          ("inprogress", 1),
          ("noResponse", 3),
          ("success", 2))
    )


_HcxStuEthTestResult_Type.__name__ = "Integer32"
_HcxStuEthTestResult_Object = MibTableColumn
hcxStuEthTestResult = _HcxStuEthTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 18),
    _HcxStuEthTestResult_Type()
)
hcxStuEthTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuEthTestResult.setStatus("current")


class _HcxStuRetPathSelect_Type(Integer32):
    """Custom type hcxStuRetPathSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("teleRet", 2),
          ("twoWay", 1))
    )


_HcxStuRetPathSelect_Type.__name__ = "Integer32"
_HcxStuRetPathSelect_Object = MibTableColumn
hcxStuRetPathSelect = _HcxStuRetPathSelect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 19),
    _HcxStuRetPathSelect_Type()
)
hcxStuRetPathSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuRetPathSelect.setStatus("current")


class _HcxStuEth8022Filter_Type(Integer32):
    """Custom type hcxStuEth8022Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuEth8022Filter_Type.__name__ = "Integer32"
_HcxStuEth8022Filter_Object = MibTableColumn
hcxStuEth8022Filter = _HcxStuEth8022Filter_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 20),
    _HcxStuEth8022Filter_Type()
)
hcxStuEth8022Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuEth8022Filter.setStatus("current")


class _HcxStuDnstrmFwdCntrl_Type(Integer32):
    """Custom type hcxStuDnstrmFwdCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuDnstrmFwdCntrl_Type.__name__ = "Integer32"
_HcxStuDnstrmFwdCntrl_Object = MibTableColumn
hcxStuDnstrmFwdCntrl = _HcxStuDnstrmFwdCntrl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 21),
    _HcxStuDnstrmFwdCntrl_Type()
)
hcxStuDnstrmFwdCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDnstrmFwdCntrl.setStatus("current")


class _HcxStuStatsCollect_Type(Integer32):
    """Custom type hcxStuStatsCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HcxStuStatsCollect_Type.__name__ = "Integer32"
_HcxStuStatsCollect_Object = MibTableColumn
hcxStuStatsCollect = _HcxStuStatsCollect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 22),
    _HcxStuStatsCollect_Type()
)
hcxStuStatsCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuStatsCollect.setStatus("current")


class _HcxStuPowerRangeState_Type(Integer32):
    """Custom type hcxStuPowerRangeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noProblem", 1),
          ("powerHigh", 3),
          ("powerLow", 2))
    )


_HcxStuPowerRangeState_Type.__name__ = "Integer32"
_HcxStuPowerRangeState_Object = MibTableColumn
hcxStuPowerRangeState = _HcxStuPowerRangeState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 23),
    _HcxStuPowerRangeState_Type()
)
hcxStuPowerRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuPowerRangeState.setStatus("current")


class _HcxStuRpmIPortId_Type(Integer32):
    """Custom type hcxStuRpmIPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HcxStuRpmIPortId_Type.__name__ = "Integer32"
_HcxStuRpmIPortId_Object = MibTableColumn
hcxStuRpmIPortId = _HcxStuRpmIPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 24),
    _HcxStuRpmIPortId_Type()
)
hcxStuRpmIPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuRpmIPortId.setStatus("current")
_HcxStuEthLpbkTestUpRate_Type = Integer32
_HcxStuEthLpbkTestUpRate_Object = MibTableColumn
hcxStuEthLpbkTestUpRate = _HcxStuEthLpbkTestUpRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 25),
    _HcxStuEthLpbkTestUpRate_Type()
)
hcxStuEthLpbkTestUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuEthLpbkTestUpRate.setStatus("current")
_HcxStuEthLpbkTestLatency_Type = Integer32
_HcxStuEthLpbkTestLatency_Object = MibTableColumn
hcxStuEthLpbkTestLatency = _HcxStuEthLpbkTestLatency_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 26),
    _HcxStuEthLpbkTestLatency_Type()
)
hcxStuEthLpbkTestLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuEthLpbkTestLatency.setStatus("current")


class _HcxStuModelName_Type(Integer32):
    """Custom type hcxStuModelName based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("cp1000", 3),
          ("cp1000A", 4),
          ("cp1000B", 5),
          ("cp1000C", 6),
          ("cp1000D", 7),
          ("cp1100", 8),
          ("cp1100A", 9),
          ("cp1100B", 10),
          ("cp1100C", 11),
          ("cp1100D", 12),
          ("cp2000", 13),
          ("cp2000A", 14),
          ("cp2100", 15),
          ("cp2100A", 16),
          ("cp5020", 17),
          ("cp5120", 18),
          ("invalid", 2),
          ("uninitialized", 1))
    )


_HcxStuModelName_Type.__name__ = "Integer32"
_HcxStuModelName_Object = MibTableColumn
hcxStuModelName = _HcxStuModelName_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 27),
    _HcxStuModelName_Type()
)
hcxStuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuModelName.setStatus("current")
_HcxStuEthTestDnRate_Type = Integer32
_HcxStuEthTestDnRate_Object = MibTableColumn
hcxStuEthTestDnRate = _HcxStuEthTestDnRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 28),
    _HcxStuEthTestDnRate_Type()
)
hcxStuEthTestDnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuEthTestDnRate.setStatus("current")


class _HcxStuEthLpbkTestDuration_Type(Integer32):
    """Custom type hcxStuEthLpbkTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 80),
    )


_HcxStuEthLpbkTestDuration_Type.__name__ = "Integer32"
_HcxStuEthLpbkTestDuration_Object = MibTableColumn
hcxStuEthLpbkTestDuration = _HcxStuEthLpbkTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 51, 1, 1, 30),
    _HcxStuEthLpbkTestDuration_Type()
)
hcxStuEthLpbkTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuEthLpbkTestDuration.setStatus("current")
_Com21HcxStuSrcIpAddrGroup_ObjectIdentity = ObjectIdentity
com21HcxStuSrcIpAddrGroup = _Com21HcxStuSrcIpAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52)
)
_Com21HcxStuSrcIpAddrTable_Object = MibTable
com21HcxStuSrcIpAddrTable = _Com21HcxStuSrcIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuSrcIpAddrTable.setStatus("current")
_Com21HcxStuSrcIpAddrEntry_Object = MibTableRow
com21HcxStuSrcIpAddrEntry = _Com21HcxStuSrcIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1)
)
com21HcxStuSrcIpAddrEntry.setIndexNames(
    (0, "COM21-HCXSTU-MIB", "hcxStuSrcIpAddrMacAddr"),
    (0, "COM21-HCXSTU-MIB", "hcxStuSrcIpAddrEntryId"),
)
if mibBuilder.loadTexts:
    com21HcxStuSrcIpAddrEntry.setStatus("current")
_HcxStuSrcIpAddrMacAddr_Type = MacAddress
_HcxStuSrcIpAddrMacAddr_Object = MibTableColumn
hcxStuSrcIpAddrMacAddr = _HcxStuSrcIpAddrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 1),
    _HcxStuSrcIpAddrMacAddr_Type()
)
hcxStuSrcIpAddrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrMacAddr.setStatus("current")
_HcxStuSrcIpAddrIPAddr_Type = IpAddress
_HcxStuSrcIpAddrIPAddr_Object = MibTableColumn
hcxStuSrcIpAddrIPAddr = _HcxStuSrcIpAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 2),
    _HcxStuSrcIpAddrIPAddr_Type()
)
hcxStuSrcIpAddrIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrIPAddr.setStatus("current")
_HcxStuSrcIpAddrIPMask_Type = IpAddress
_HcxStuSrcIpAddrIPMask_Object = MibTableColumn
hcxStuSrcIpAddrIPMask = _HcxStuSrcIpAddrIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 3),
    _HcxStuSrcIpAddrIPMask_Type()
)
hcxStuSrcIpAddrIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrIPMask.setStatus("current")
_HcxStuSrcIpAddrUserMacAddr_Type = MacAddress
_HcxStuSrcIpAddrUserMacAddr_Object = MibTableColumn
hcxStuSrcIpAddrUserMacAddr = _HcxStuSrcIpAddrUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 4),
    _HcxStuSrcIpAddrUserMacAddr_Type()
)
hcxStuSrcIpAddrUserMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrUserMacAddr.setStatus("current")
_HcxStuSrcIpAddrIPStatus_Type = Com21RowStatus
_HcxStuSrcIpAddrIPStatus_Object = MibTableColumn
hcxStuSrcIpAddrIPStatus = _HcxStuSrcIpAddrIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 5),
    _HcxStuSrcIpAddrIPStatus_Type()
)
hcxStuSrcIpAddrIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrIPStatus.setStatus("current")
_HcxStuSrcIpAddrEtherIPAddr_Type = IpAddress
_HcxStuSrcIpAddrEtherIPAddr_Object = MibTableColumn
hcxStuSrcIpAddrEtherIPAddr = _HcxStuSrcIpAddrEtherIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 6),
    _HcxStuSrcIpAddrEtherIPAddr_Type()
)
hcxStuSrcIpAddrEtherIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrEtherIPAddr.setStatus("current")


class _HcxStuSrcIpAddrEntryId_Type(Integer32):
    """Custom type hcxStuSrcIpAddrEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HcxStuSrcIpAddrEntryId_Type.__name__ = "Integer32"
_HcxStuSrcIpAddrEntryId_Object = MibTableColumn
hcxStuSrcIpAddrEntryId = _HcxStuSrcIpAddrEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 7),
    _HcxStuSrcIpAddrEntryId_Type()
)
hcxStuSrcIpAddrEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrEntryId.setStatus("current")


class _HcxStuSrcIpAddrType_Type(Integer32):
    """Custom type hcxStuSrcIpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HcxStuSrcIpAddrType_Type.__name__ = "Integer32"
_HcxStuSrcIpAddrType_Object = MibTableColumn
hcxStuSrcIpAddrType = _HcxStuSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 8),
    _HcxStuSrcIpAddrType_Type()
)
hcxStuSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrType.setStatus("current")
_HcxStuSrcIpAddrLeaseTimer_Type = Integer32
_HcxStuSrcIpAddrLeaseTimer_Object = MibTableColumn
hcxStuSrcIpAddrLeaseTimer = _HcxStuSrcIpAddrLeaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 52, 1, 1, 9),
    _HcxStuSrcIpAddrLeaseTimer_Type()
)
hcxStuSrcIpAddrLeaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuSrcIpAddrLeaseTimer.setStatus("current")
_Com21HcxStuIpFiltGroup_ObjectIdentity = ObjectIdentity
com21HcxStuIpFiltGroup = _Com21HcxStuIpFiltGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53)
)
_Com21HcxStuIpFiltTable_Object = MibTable
com21HcxStuIpFiltTable = _Com21HcxStuIpFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuIpFiltTable.setStatus("current")
_Com21HcxStuIpFiltEntry_Object = MibTableRow
com21HcxStuIpFiltEntry = _Com21HcxStuIpFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1)
)
com21HcxStuIpFiltEntry.setIndexNames(
    (0, "COM21-HCXSTU-MIB", "hcxStuIpFiltMacAddr"),
)
if mibBuilder.loadTexts:
    com21HcxStuIpFiltEntry.setStatus("current")
_HcxStuIpFiltMacAddr_Type = MacAddress
_HcxStuIpFiltMacAddr_Object = MibTableColumn
hcxStuIpFiltMacAddr = _HcxStuIpFiltMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 1),
    _HcxStuIpFiltMacAddr_Type()
)
hcxStuIpFiltMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpFiltMacAddr.setStatus("current")


class _HcxStuIpArpFiltEnable_Type(Integer32):
    """Custom type hcxStuIpArpFiltEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpArpFiltEnable_Type.__name__ = "Integer32"
_HcxStuIpArpFiltEnable_Object = MibTableColumn
hcxStuIpArpFiltEnable = _HcxStuIpArpFiltEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 2),
    _HcxStuIpArpFiltEnable_Type()
)
hcxStuIpArpFiltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpArpFiltEnable.setStatus("current")
_HcxStuIpArpFiltInvalidAddr_Type = IpAddress
_HcxStuIpArpFiltInvalidAddr_Object = MibTableColumn
hcxStuIpArpFiltInvalidAddr = _HcxStuIpArpFiltInvalidAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 3),
    _HcxStuIpArpFiltInvalidAddr_Type()
)
hcxStuIpArpFiltInvalidAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpArpFiltInvalidAddr.setStatus("current")
_HcxStuIpArpFiltBadServAddr_Type = IpAddress
_HcxStuIpArpFiltBadServAddr_Object = MibTableColumn
hcxStuIpArpFiltBadServAddr = _HcxStuIpArpFiltBadServAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 4),
    _HcxStuIpArpFiltBadServAddr_Type()
)
hcxStuIpArpFiltBadServAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpArpFiltBadServAddr.setStatus("current")


class _HcxStuIpSrcFiltEnable_Type(Integer32):
    """Custom type hcxStuIpSrcFiltEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpSrcFiltEnable_Type.__name__ = "Integer32"
_HcxStuIpSrcFiltEnable_Object = MibTableColumn
hcxStuIpSrcFiltEnable = _HcxStuIpSrcFiltEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 5),
    _HcxStuIpSrcFiltEnable_Type()
)
hcxStuIpSrcFiltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpSrcFiltEnable.setStatus("current")


class _HcxStuIpDstFiltEnable_Type(Integer32):
    """Custom type hcxStuIpDstFiltEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpDstFiltEnable_Type.__name__ = "Integer32"
_HcxStuIpDstFiltEnable_Object = MibTableColumn
hcxStuIpDstFiltEnable = _HcxStuIpDstFiltEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 6),
    _HcxStuIpDstFiltEnable_Type()
)
hcxStuIpDstFiltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpDstFiltEnable.setStatus("current")


class _HcxStuIpBootpReqFiltEnbl_Type(Integer32):
    """Custom type hcxStuIpBootpReqFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpBootpReqFiltEnbl_Type.__name__ = "Integer32"
_HcxStuIpBootpReqFiltEnbl_Object = MibTableColumn
hcxStuIpBootpReqFiltEnbl = _HcxStuIpBootpReqFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 7),
    _HcxStuIpBootpReqFiltEnbl_Type()
)
hcxStuIpBootpReqFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpBootpReqFiltEnbl.setStatus("deprecated")


class _HcxStuIpBootpReplyFiltEnbl_Type(Integer32):
    """Custom type hcxStuIpBootpReplyFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpBootpReplyFiltEnbl_Type.__name__ = "Integer32"
_HcxStuIpBootpReplyFiltEnbl_Object = MibTableColumn
hcxStuIpBootpReplyFiltEnbl = _HcxStuIpBootpReplyFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 8),
    _HcxStuIpBootpReplyFiltEnbl_Type()
)
hcxStuIpBootpReplyFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpBootpReplyFiltEnbl.setStatus("current")


class _HcxStuIpDhcpSnoopFiltEnbl_Type(Integer32):
    """Custom type hcxStuIpDhcpSnoopFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpDhcpSnoopFiltEnbl_Type.__name__ = "Integer32"
_HcxStuIpDhcpSnoopFiltEnbl_Object = MibTableColumn
hcxStuIpDhcpSnoopFiltEnbl = _HcxStuIpDhcpSnoopFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 9),
    _HcxStuIpDhcpSnoopFiltEnbl_Type()
)
hcxStuIpDhcpSnoopFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpDhcpSnoopFiltEnbl.setStatus("current")


class _HcxStuL2SnapFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2SnapFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2SnapFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2SnapFiltEnbl_Object = MibTableColumn
hcxStuL2SnapFiltEnbl = _HcxStuL2SnapFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 10),
    _HcxStuL2SnapFiltEnbl_Type()
)
hcxStuL2SnapFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2SnapFiltEnbl.setStatus("current")


class _HcxStuL2NonSnapFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2NonSnapFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2NonSnapFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2NonSnapFiltEnbl_Object = MibTableColumn
hcxStuL2NonSnapFiltEnbl = _HcxStuL2NonSnapFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 11),
    _HcxStuL2NonSnapFiltEnbl_Type()
)
hcxStuL2NonSnapFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2NonSnapFiltEnbl.setStatus("current")


class _HcxStuL2EnetFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2EnetFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2EnetFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2EnetFiltEnbl_Object = MibTableColumn
hcxStuL2EnetFiltEnbl = _HcxStuL2EnetFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 12),
    _HcxStuL2EnetFiltEnbl_Type()
)
hcxStuL2EnetFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2EnetFiltEnbl.setStatus("deprecated")


class _HcxStuL2ArpIpv4FiltEnbl_Type(Integer32):
    """Custom type hcxStuL2ArpIpv4FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2ArpIpv4FiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2ArpIpv4FiltEnbl_Object = MibTableColumn
hcxStuL2ArpIpv4FiltEnbl = _HcxStuL2ArpIpv4FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 13),
    _HcxStuL2ArpIpv4FiltEnbl_Type()
)
hcxStuL2ArpIpv4FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2ArpIpv4FiltEnbl.setStatus("deprecated")


class _HcxStuL2Ipv4FiltEnbl_Type(Integer32):
    """Custom type hcxStuL2Ipv4FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2Ipv4FiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2Ipv4FiltEnbl_Object = MibTableColumn
hcxStuL2Ipv4FiltEnbl = _HcxStuL2Ipv4FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 14),
    _HcxStuL2Ipv4FiltEnbl_Type()
)
hcxStuL2Ipv4FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2Ipv4FiltEnbl.setStatus("deprecated")


class _HcxStuL2Ipv6FiltEnbl_Type(Integer32):
    """Custom type hcxStuL2Ipv6FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2Ipv6FiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2Ipv6FiltEnbl_Object = MibTableColumn
hcxStuL2Ipv6FiltEnbl = _HcxStuL2Ipv6FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 15),
    _HcxStuL2Ipv6FiltEnbl_Type()
)
hcxStuL2Ipv6FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2Ipv6FiltEnbl.setStatus("deprecated")


class _HcxStuL2IpxFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2IpxFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2IpxFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2IpxFiltEnbl_Object = MibTableColumn
hcxStuL2IpxFiltEnbl = _HcxStuL2IpxFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 16),
    _HcxStuL2IpxFiltEnbl_Type()
)
hcxStuL2IpxFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2IpxFiltEnbl.setStatus("deprecated")


class _HcxStuL2AppletalkFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2AppletalkFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2AppletalkFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2AppletalkFiltEnbl_Object = MibTableColumn
hcxStuL2AppletalkFiltEnbl = _HcxStuL2AppletalkFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 17),
    _HcxStuL2AppletalkFiltEnbl_Type()
)
hcxStuL2AppletalkFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2AppletalkFiltEnbl.setStatus("deprecated")


class _HcxStuL2OthersFiltEnbl_Type(Integer32):
    """Custom type hcxStuL2OthersFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuL2OthersFiltEnbl_Type.__name__ = "Integer32"
_HcxStuL2OthersFiltEnbl_Object = MibTableColumn
hcxStuL2OthersFiltEnbl = _HcxStuL2OthersFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 18),
    _HcxStuL2OthersFiltEnbl_Type()
)
hcxStuL2OthersFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuL2OthersFiltEnbl.setStatus("deprecated")


class _HcxStuIpNetbiosFiltEnbl_Type(Integer32):
    """Custom type hcxStuIpNetbiosFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuIpNetbiosFiltEnbl_Type.__name__ = "Integer32"
_HcxStuIpNetbiosFiltEnbl_Object = MibTableColumn
hcxStuIpNetbiosFiltEnbl = _HcxStuIpNetbiosFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 53, 1, 1, 19),
    _HcxStuIpNetbiosFiltEnbl_Type()
)
hcxStuIpNetbiosFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpNetbiosFiltEnbl.setStatus("current")
_Com21HcxStuIpFiltStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxStuIpFiltStatsGroup = _Com21HcxStuIpFiltStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55)
)
_Com21HcxStuIpFiltStatsTable_Object = MibTable
com21HcxStuIpFiltStatsTable = _Com21HcxStuIpFiltStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuIpFiltStatsTable.setStatus("current")
_Com21HcxStuIpFiltStatsEntry_Object = MibTableRow
com21HcxStuIpFiltStatsEntry = _Com21HcxStuIpFiltStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1)
)
com21HcxStuIpFiltStatsEntry.setIndexNames(
    (0, "COM21-HCXSTU-MIB", "hcxStuIpFiltStatsMacAddr"),
)
if mibBuilder.loadTexts:
    com21HcxStuIpFiltStatsEntry.setStatus("current")
_HcxStuIpFiltStatsMacAddr_Type = MacAddress
_HcxStuIpFiltStatsMacAddr_Object = MibTableColumn
hcxStuIpFiltStatsMacAddr = _HcxStuIpFiltStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 1),
    _HcxStuIpFiltStatsMacAddr_Type()
)
hcxStuIpFiltStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpFiltStatsMacAddr.setStatus("current")
_HcxStuIpCurrArpFiltStat_Type = Gauge32
_HcxStuIpCurrArpFiltStat_Object = MibTableColumn
hcxStuIpCurrArpFiltStat = _HcxStuIpCurrArpFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 2),
    _HcxStuIpCurrArpFiltStat_Type()
)
hcxStuIpCurrArpFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrArpFiltStat.setStatus("current")
_HcxStuIpCurrSrcFiltStat_Type = Gauge32
_HcxStuIpCurrSrcFiltStat_Object = MibTableColumn
hcxStuIpCurrSrcFiltStat = _HcxStuIpCurrSrcFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 3),
    _HcxStuIpCurrSrcFiltStat_Type()
)
hcxStuIpCurrSrcFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrSrcFiltStat.setStatus("current")
_HcxStuIpCurrDstFiltStat_Type = Gauge32
_HcxStuIpCurrDstFiltStat_Object = MibTableColumn
hcxStuIpCurrDstFiltStat = _HcxStuIpCurrDstFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 4),
    _HcxStuIpCurrDstFiltStat_Type()
)
hcxStuIpCurrDstFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrDstFiltStat.setStatus("current")
_HcxStuIpCurrBootpReqFiltStat_Type = Gauge32
_HcxStuIpCurrBootpReqFiltStat_Object = MibTableColumn
hcxStuIpCurrBootpReqFiltStat = _HcxStuIpCurrBootpReqFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 5),
    _HcxStuIpCurrBootpReqFiltStat_Type()
)
hcxStuIpCurrBootpReqFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrBootpReqFiltStat.setStatus("current")
_HcxStuIpCurrBootpReplyFiltStat_Type = Gauge32
_HcxStuIpCurrBootpReplyFiltStat_Object = MibTableColumn
hcxStuIpCurrBootpReplyFiltStat = _HcxStuIpCurrBootpReplyFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 6),
    _HcxStuIpCurrBootpReplyFiltStat_Type()
)
hcxStuIpCurrBootpReplyFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrBootpReplyFiltStat.setStatus("current")
_HcxStuIpCurrDhcpSnoopFiltStat_Type = Gauge32
_HcxStuIpCurrDhcpSnoopFiltStat_Object = MibTableColumn
hcxStuIpCurrDhcpSnoopFiltStat = _HcxStuIpCurrDhcpSnoopFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 7),
    _HcxStuIpCurrDhcpSnoopFiltStat_Type()
)
hcxStuIpCurrDhcpSnoopFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrDhcpSnoopFiltStat.setStatus("current")
_HcxStuIpPrevArpFiltStat_Type = Gauge32
_HcxStuIpPrevArpFiltStat_Object = MibTableColumn
hcxStuIpPrevArpFiltStat = _HcxStuIpPrevArpFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 8),
    _HcxStuIpPrevArpFiltStat_Type()
)
hcxStuIpPrevArpFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevArpFiltStat.setStatus("current")
_HcxStuIpPrevSrcFiltStat_Type = Gauge32
_HcxStuIpPrevSrcFiltStat_Object = MibTableColumn
hcxStuIpPrevSrcFiltStat = _HcxStuIpPrevSrcFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 9),
    _HcxStuIpPrevSrcFiltStat_Type()
)
hcxStuIpPrevSrcFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevSrcFiltStat.setStatus("current")
_HcxStuIpPrevDstFiltStat_Type = Gauge32
_HcxStuIpPrevDstFiltStat_Object = MibTableColumn
hcxStuIpPrevDstFiltStat = _HcxStuIpPrevDstFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 10),
    _HcxStuIpPrevDstFiltStat_Type()
)
hcxStuIpPrevDstFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevDstFiltStat.setStatus("current")
_HcxStuIpPrevBootpReqFiltStat_Type = Gauge32
_HcxStuIpPrevBootpReqFiltStat_Object = MibTableColumn
hcxStuIpPrevBootpReqFiltStat = _HcxStuIpPrevBootpReqFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 11),
    _HcxStuIpPrevBootpReqFiltStat_Type()
)
hcxStuIpPrevBootpReqFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevBootpReqFiltStat.setStatus("current")
_HcxStuIpPrevBootpReplyFiltStat_Type = Gauge32
_HcxStuIpPrevBootpReplyFiltStat_Object = MibTableColumn
hcxStuIpPrevBootpReplyFiltStat = _HcxStuIpPrevBootpReplyFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 12),
    _HcxStuIpPrevBootpReplyFiltStat_Type()
)
hcxStuIpPrevBootpReplyFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevBootpReplyFiltStat.setStatus("current")
_HcxStuIpPrevDhcpSnoopFiltStat_Type = Gauge32
_HcxStuIpPrevDhcpSnoopFiltStat_Object = MibTableColumn
hcxStuIpPrevDhcpSnoopFiltStat = _HcxStuIpPrevDhcpSnoopFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 13),
    _HcxStuIpPrevDhcpSnoopFiltStat_Type()
)
hcxStuIpPrevDhcpSnoopFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevDhcpSnoopFiltStat.setStatus("current")


class _HcxStuIpClearStats_Type(Integer32):
    """Custom type hcxStuIpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxStuIpClearStats_Type.__name__ = "Integer32"
_HcxStuIpClearStats_Object = MibTableColumn
hcxStuIpClearStats = _HcxStuIpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 14),
    _HcxStuIpClearStats_Type()
)
hcxStuIpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuIpClearStats.setStatus("current")
_HcxStuL2CurrSnapFiltStat_Type = Gauge32
_HcxStuL2CurrSnapFiltStat_Object = MibTableColumn
hcxStuL2CurrSnapFiltStat = _HcxStuL2CurrSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 15),
    _HcxStuL2CurrSnapFiltStat_Type()
)
hcxStuL2CurrSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrSnapFiltStat.setStatus("current")
_HcxStuL2CurrNonSnapFiltStat_Type = Gauge32
_HcxStuL2CurrNonSnapFiltStat_Object = MibTableColumn
hcxStuL2CurrNonSnapFiltStat = _HcxStuL2CurrNonSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 16),
    _HcxStuL2CurrNonSnapFiltStat_Type()
)
hcxStuL2CurrNonSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrNonSnapFiltStat.setStatus("current")
_HcxStuL2CurrEnetFiltStat_Type = Gauge32
_HcxStuL2CurrEnetFiltStat_Object = MibTableColumn
hcxStuL2CurrEnetFiltStat = _HcxStuL2CurrEnetFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 17),
    _HcxStuL2CurrEnetFiltStat_Type()
)
hcxStuL2CurrEnetFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrEnetFiltStat.setStatus("deprecated")
_HcxStuL2CurrArpIpv4FiltStat_Type = Gauge32
_HcxStuL2CurrArpIpv4FiltStat_Object = MibTableColumn
hcxStuL2CurrArpIpv4FiltStat = _HcxStuL2CurrArpIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 18),
    _HcxStuL2CurrArpIpv4FiltStat_Type()
)
hcxStuL2CurrArpIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrArpIpv4FiltStat.setStatus("deprecated")
_HcxStuL2CurrIpv4FiltStat_Type = Gauge32
_HcxStuL2CurrIpv4FiltStat_Object = MibTableColumn
hcxStuL2CurrIpv4FiltStat = _HcxStuL2CurrIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 19),
    _HcxStuL2CurrIpv4FiltStat_Type()
)
hcxStuL2CurrIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrIpv4FiltStat.setStatus("deprecated")
_HcxStuL2CurrIpv6FiltStat_Type = Gauge32
_HcxStuL2CurrIpv6FiltStat_Object = MibTableColumn
hcxStuL2CurrIpv6FiltStat = _HcxStuL2CurrIpv6FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 20),
    _HcxStuL2CurrIpv6FiltStat_Type()
)
hcxStuL2CurrIpv6FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrIpv6FiltStat.setStatus("deprecated")
_HcxStuL2CurrIpxFiltStat_Type = Gauge32
_HcxStuL2CurrIpxFiltStat_Object = MibTableColumn
hcxStuL2CurrIpxFiltStat = _HcxStuL2CurrIpxFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 21),
    _HcxStuL2CurrIpxFiltStat_Type()
)
hcxStuL2CurrIpxFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrIpxFiltStat.setStatus("deprecated")
_HcxStuL2CurrAppletalkFiltStat_Type = Gauge32
_HcxStuL2CurrAppletalkFiltStat_Object = MibTableColumn
hcxStuL2CurrAppletalkFiltStat = _HcxStuL2CurrAppletalkFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 22),
    _HcxStuL2CurrAppletalkFiltStat_Type()
)
hcxStuL2CurrAppletalkFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrAppletalkFiltStat.setStatus("deprecated")
_HcxStuL2CurrOthersFiltStat_Type = Gauge32
_HcxStuL2CurrOthersFiltStat_Object = MibTableColumn
hcxStuL2CurrOthersFiltStat = _HcxStuL2CurrOthersFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 23),
    _HcxStuL2CurrOthersFiltStat_Type()
)
hcxStuL2CurrOthersFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2CurrOthersFiltStat.setStatus("deprecated")
_HcxStuIpCurrNetbiosFiltStat_Type = Gauge32
_HcxStuIpCurrNetbiosFiltStat_Object = MibTableColumn
hcxStuIpCurrNetbiosFiltStat = _HcxStuIpCurrNetbiosFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 24),
    _HcxStuIpCurrNetbiosFiltStat_Type()
)
hcxStuIpCurrNetbiosFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpCurrNetbiosFiltStat.setStatus("current")
_HcxStuL2PrevSnapFiltStat_Type = Gauge32
_HcxStuL2PrevSnapFiltStat_Object = MibTableColumn
hcxStuL2PrevSnapFiltStat = _HcxStuL2PrevSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 25),
    _HcxStuL2PrevSnapFiltStat_Type()
)
hcxStuL2PrevSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevSnapFiltStat.setStatus("current")
_HcxStuL2PrevNonSnapFiltStat_Type = Gauge32
_HcxStuL2PrevNonSnapFiltStat_Object = MibTableColumn
hcxStuL2PrevNonSnapFiltStat = _HcxStuL2PrevNonSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 26),
    _HcxStuL2PrevNonSnapFiltStat_Type()
)
hcxStuL2PrevNonSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevNonSnapFiltStat.setStatus("current")
_HcxStuL2PrevEnetFiltStat_Type = Gauge32
_HcxStuL2PrevEnetFiltStat_Object = MibTableColumn
hcxStuL2PrevEnetFiltStat = _HcxStuL2PrevEnetFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 27),
    _HcxStuL2PrevEnetFiltStat_Type()
)
hcxStuL2PrevEnetFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevEnetFiltStat.setStatus("deprecated")
_HcxStuL2PrevArpIpv4FiltStat_Type = Gauge32
_HcxStuL2PrevArpIpv4FiltStat_Object = MibTableColumn
hcxStuL2PrevArpIpv4FiltStat = _HcxStuL2PrevArpIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 28),
    _HcxStuL2PrevArpIpv4FiltStat_Type()
)
hcxStuL2PrevArpIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevArpIpv4FiltStat.setStatus("deprecated")
_HcxStuL2PrevIpv4FiltStat_Type = Gauge32
_HcxStuL2PrevIpv4FiltStat_Object = MibTableColumn
hcxStuL2PrevIpv4FiltStat = _HcxStuL2PrevIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 29),
    _HcxStuL2PrevIpv4FiltStat_Type()
)
hcxStuL2PrevIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevIpv4FiltStat.setStatus("deprecated")
_HcxStuL2PrevIpv6FiltStat_Type = Gauge32
_HcxStuL2PrevIpv6FiltStat_Object = MibTableColumn
hcxStuL2PrevIpv6FiltStat = _HcxStuL2PrevIpv6FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 30),
    _HcxStuL2PrevIpv6FiltStat_Type()
)
hcxStuL2PrevIpv6FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevIpv6FiltStat.setStatus("deprecated")
_HcxStuL2PrevIpxFiltStat_Type = Gauge32
_HcxStuL2PrevIpxFiltStat_Object = MibTableColumn
hcxStuL2PrevIpxFiltStat = _HcxStuL2PrevIpxFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 31),
    _HcxStuL2PrevIpxFiltStat_Type()
)
hcxStuL2PrevIpxFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevIpxFiltStat.setStatus("deprecated")
_HcxStuL2PrevAppletalkFiltStat_Type = Gauge32
_HcxStuL2PrevAppletalkFiltStat_Object = MibTableColumn
hcxStuL2PrevAppletalkFiltStat = _HcxStuL2PrevAppletalkFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 32),
    _HcxStuL2PrevAppletalkFiltStat_Type()
)
hcxStuL2PrevAppletalkFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevAppletalkFiltStat.setStatus("deprecated")
_HcxStuL2PrevOthersFiltStat_Type = Gauge32
_HcxStuL2PrevOthersFiltStat_Object = MibTableColumn
hcxStuL2PrevOthersFiltStat = _HcxStuL2PrevOthersFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 33),
    _HcxStuL2PrevOthersFiltStat_Type()
)
hcxStuL2PrevOthersFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuL2PrevOthersFiltStat.setStatus("deprecated")
_HcxStuIpPrevNetbiosFiltStat_Type = Gauge32
_HcxStuIpPrevNetbiosFiltStat_Object = MibTableColumn
hcxStuIpPrevNetbiosFiltStat = _HcxStuIpPrevNetbiosFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 55, 1, 1, 34),
    _HcxStuIpPrevNetbiosFiltStat_Type()
)
hcxStuIpPrevNetbiosFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuIpPrevNetbiosFiltStat.setStatus("current")
_Com21HcxStuDstIpAddrGroup_ObjectIdentity = ObjectIdentity
com21HcxStuDstIpAddrGroup = _Com21HcxStuDstIpAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57)
)
_Com21HcxStuDstIpAddrTable_Object = MibTable
com21HcxStuDstIpAddrTable = _Com21HcxStuDstIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1)
)
if mibBuilder.loadTexts:
    com21HcxStuDstIpAddrTable.setStatus("current")
_Com21HcxStuDstIpAddrEntry_Object = MibTableRow
com21HcxStuDstIpAddrEntry = _Com21HcxStuDstIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1)
)
com21HcxStuDstIpAddrEntry.setIndexNames(
    (0, "COM21-HCXSTU-MIB", "hcxStuDstIpAddrMacAddr"),
    (0, "COM21-HCXSTU-MIB", "hcxStuDstIpAddrEntryId"),
)
if mibBuilder.loadTexts:
    com21HcxStuDstIpAddrEntry.setStatus("current")
_HcxStuDstIpAddrMacAddr_Type = MacAddress
_HcxStuDstIpAddrMacAddr_Object = MibTableColumn
hcxStuDstIpAddrMacAddr = _HcxStuDstIpAddrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1, 1),
    _HcxStuDstIpAddrMacAddr_Type()
)
hcxStuDstIpAddrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuDstIpAddrMacAddr.setStatus("current")
_HcxStuDstIpAddrIPAddr_Type = IpAddress
_HcxStuDstIpAddrIPAddr_Object = MibTableColumn
hcxStuDstIpAddrIPAddr = _HcxStuDstIpAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1, 2),
    _HcxStuDstIpAddrIPAddr_Type()
)
hcxStuDstIpAddrIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDstIpAddrIPAddr.setStatus("current")
_HcxStuDstIpAddrIPMask_Type = IpAddress
_HcxStuDstIpAddrIPMask_Object = MibTableColumn
hcxStuDstIpAddrIPMask = _HcxStuDstIpAddrIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1, 3),
    _HcxStuDstIpAddrIPMask_Type()
)
hcxStuDstIpAddrIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDstIpAddrIPMask.setStatus("current")
_HcxStuDstIpAddrIPStatus_Type = Com21RowStatus
_HcxStuDstIpAddrIPStatus_Object = MibTableColumn
hcxStuDstIpAddrIPStatus = _HcxStuDstIpAddrIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1, 4),
    _HcxStuDstIpAddrIPStatus_Type()
)
hcxStuDstIpAddrIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxStuDstIpAddrIPStatus.setStatus("current")


class _HcxStuDstIpAddrEntryId_Type(Integer32):
    """Custom type hcxStuDstIpAddrEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HcxStuDstIpAddrEntryId_Type.__name__ = "Integer32"
_HcxStuDstIpAddrEntryId_Object = MibTableColumn
hcxStuDstIpAddrEntryId = _HcxStuDstIpAddrEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 57, 1, 1, 5),
    _HcxStuDstIpAddrEntryId_Type()
)
hcxStuDstIpAddrEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuDstIpAddrEntryId.setStatus("current")

# Managed Objects groups


# Notification objects

hcxStuAcqEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 90)
)
hcxStuAcqEvent.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuAcqEvent.setStatus(
        "current"
    )

hcxStuDeacqEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 91)
)
hcxStuDeacqEvent.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuDeacqEvent.setStatus(
        "current"
    )

hcxIncompSwVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 100)
)
hcxIncompSwVersion.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxIncompSwVersion.setStatus(
        "current"
    )

hcxUnavailSwVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 101)
)
hcxUnavailSwVersion.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxUnavailSwVersion.setStatus(
        "current"
    )

hcxStuPingTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 102)
)
hcxStuPingTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"),
        ("COM21-HCXSTU-MIB", "hcxStuPingTestResult"))
)
if mibBuilder.loadTexts:
    hcxStuPingTestComplete.setStatus(
        "current"
    )

hcxStuEthTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 103)
)
hcxStuEthTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"),
        ("COM21-HCXSTU-MIB", "hcxStuEthTestResult"))
)
if mibBuilder.loadTexts:
    hcxStuEthTestComplete.setStatus(
        "current"
    )

hcxStuAcqRangeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 104)
)
hcxStuAcqRangeFail.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuAcqRangeFail.setStatus(
        "current"
    )

hcxStuAcqOnlineFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 105)
)
hcxStuAcqOnlineFail.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuAcqOnlineFail.setStatus(
        "current"
    )

hcxStuArpInvalidAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 106)
)
hcxStuArpInvalidAddr.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuIpFiltMacAddr"),
        ("COM21-HCXSTU-MIB", "hcxStuIpArpFiltInvalidAddr"))
)
if mibBuilder.loadTexts:
    hcxStuArpInvalidAddr.setStatus(
        "current"
    )

hcxStuArpBadServerAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 107)
)
hcxStuArpBadServerAddr.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuIpFiltMacAddr"),
        ("COM21-HCXSTU-MIB", "hcxStuIpArpFiltBadServAddr"))
)
if mibBuilder.loadTexts:
    hcxStuArpBadServerAddr.setStatus(
        "current"
    )

hcxStuRangFailPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 108)
)
hcxStuRangFailPowerLow.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuRangFailPowerLow.setStatus(
        "current"
    )

hcxStuRangFailPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 109)
)
hcxStuRangFailPowerHigh.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuRangFailPowerHigh.setStatus(
        "current"
    )

hcxStuRangFailLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 140)
)
hcxStuRangFailLowClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuRangFailLowClear.setStatus(
        "current"
    )

hcxStuRangFailHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 141)
)
hcxStuRangFailHighClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXSTU-MIB", "hcxStuStatusMacAddr"))
)
if mibBuilder.loadTexts:
    hcxStuRangFailHighClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXSTU-MIB",
    **{"FrequencyKhz": FrequencyKhz,
       "Com21RowStatus": Com21RowStatus,
       "StuGain": StuGain,
       "com21HcxStu": com21HcxStu,
       "com21HcxStuStatusGroup": com21HcxStuStatusGroup,
       "com21HcxStuStatusTable": com21HcxStuStatusTable,
       "com21HcxStuStatusEntry": com21HcxStuStatusEntry,
       "hcxStuStatusMacAddr": hcxStuStatusMacAddr,
       "hcxStuConfigured": hcxStuConfigured,
       "hcxStuAcquired": hcxStuAcquired,
       "hcxStuAcqFailInfo": hcxStuAcqFailInfo,
       "hcxStuAuthorized": hcxStuAuthorized,
       "hcxStuLedFlashTest": hcxStuLedFlashTest,
       "hcxStuUpstreamTest": hcxStuUpstreamTest,
       "hcxStuVlanId": hcxStuVlanId,
       "hcxStuRxShelfId": hcxStuRxShelfId,
       "hcxStuRxSlotId": hcxStuRxSlotId,
       "hcxStuRxPortId": hcxStuRxPortId,
       "hcxStuServiceType": hcxStuServiceType,
       "hcxStuConfSwImage": hcxStuConfSwImage,
       "hcxStuPingTestAction": hcxStuPingTestAction,
       "hcxStuPingTestResult": hcxStuPingTestResult,
       "hcxStuEthTestAction": hcxStuEthTestAction,
       "hcxStuEthTestResult": hcxStuEthTestResult,
       "hcxStuRetPathSelect": hcxStuRetPathSelect,
       "hcxStuEth8022Filter": hcxStuEth8022Filter,
       "hcxStuDnstrmFwdCntrl": hcxStuDnstrmFwdCntrl,
       "hcxStuStatsCollect": hcxStuStatsCollect,
       "hcxStuPowerRangeState": hcxStuPowerRangeState,
       "hcxStuRpmIPortId": hcxStuRpmIPortId,
       "hcxStuEthLpbkTestUpRate": hcxStuEthLpbkTestUpRate,
       "hcxStuEthLpbkTestLatency": hcxStuEthLpbkTestLatency,
       "hcxStuModelName": hcxStuModelName,
       "hcxStuEthTestDnRate": hcxStuEthTestDnRate,
       "hcxStuEthLpbkTestDuration": hcxStuEthLpbkTestDuration,
       "com21HcxStuSrcIpAddrGroup": com21HcxStuSrcIpAddrGroup,
       "com21HcxStuSrcIpAddrTable": com21HcxStuSrcIpAddrTable,
       "com21HcxStuSrcIpAddrEntry": com21HcxStuSrcIpAddrEntry,
       "hcxStuSrcIpAddrMacAddr": hcxStuSrcIpAddrMacAddr,
       "hcxStuSrcIpAddrIPAddr": hcxStuSrcIpAddrIPAddr,
       "hcxStuSrcIpAddrIPMask": hcxStuSrcIpAddrIPMask,
       "hcxStuSrcIpAddrUserMacAddr": hcxStuSrcIpAddrUserMacAddr,
       "hcxStuSrcIpAddrIPStatus": hcxStuSrcIpAddrIPStatus,
       "hcxStuSrcIpAddrEtherIPAddr": hcxStuSrcIpAddrEtherIPAddr,
       "hcxStuSrcIpAddrEntryId": hcxStuSrcIpAddrEntryId,
       "hcxStuSrcIpAddrType": hcxStuSrcIpAddrType,
       "hcxStuSrcIpAddrLeaseTimer": hcxStuSrcIpAddrLeaseTimer,
       "com21HcxStuIpFiltGroup": com21HcxStuIpFiltGroup,
       "com21HcxStuIpFiltTable": com21HcxStuIpFiltTable,
       "com21HcxStuIpFiltEntry": com21HcxStuIpFiltEntry,
       "hcxStuIpFiltMacAddr": hcxStuIpFiltMacAddr,
       "hcxStuIpArpFiltEnable": hcxStuIpArpFiltEnable,
       "hcxStuIpArpFiltInvalidAddr": hcxStuIpArpFiltInvalidAddr,
       "hcxStuIpArpFiltBadServAddr": hcxStuIpArpFiltBadServAddr,
       "hcxStuIpSrcFiltEnable": hcxStuIpSrcFiltEnable,
       "hcxStuIpDstFiltEnable": hcxStuIpDstFiltEnable,
       "hcxStuIpBootpReqFiltEnbl": hcxStuIpBootpReqFiltEnbl,
       "hcxStuIpBootpReplyFiltEnbl": hcxStuIpBootpReplyFiltEnbl,
       "hcxStuIpDhcpSnoopFiltEnbl": hcxStuIpDhcpSnoopFiltEnbl,
       "hcxStuL2SnapFiltEnbl": hcxStuL2SnapFiltEnbl,
       "hcxStuL2NonSnapFiltEnbl": hcxStuL2NonSnapFiltEnbl,
       "hcxStuL2EnetFiltEnbl": hcxStuL2EnetFiltEnbl,
       "hcxStuL2ArpIpv4FiltEnbl": hcxStuL2ArpIpv4FiltEnbl,
       "hcxStuL2Ipv4FiltEnbl": hcxStuL2Ipv4FiltEnbl,
       "hcxStuL2Ipv6FiltEnbl": hcxStuL2Ipv6FiltEnbl,
       "hcxStuL2IpxFiltEnbl": hcxStuL2IpxFiltEnbl,
       "hcxStuL2AppletalkFiltEnbl": hcxStuL2AppletalkFiltEnbl,
       "hcxStuL2OthersFiltEnbl": hcxStuL2OthersFiltEnbl,
       "hcxStuIpNetbiosFiltEnbl": hcxStuIpNetbiosFiltEnbl,
       "com21HcxStuIpFiltStatsGroup": com21HcxStuIpFiltStatsGroup,
       "com21HcxStuIpFiltStatsTable": com21HcxStuIpFiltStatsTable,
       "com21HcxStuIpFiltStatsEntry": com21HcxStuIpFiltStatsEntry,
       "hcxStuIpFiltStatsMacAddr": hcxStuIpFiltStatsMacAddr,
       "hcxStuIpCurrArpFiltStat": hcxStuIpCurrArpFiltStat,
       "hcxStuIpCurrSrcFiltStat": hcxStuIpCurrSrcFiltStat,
       "hcxStuIpCurrDstFiltStat": hcxStuIpCurrDstFiltStat,
       "hcxStuIpCurrBootpReqFiltStat": hcxStuIpCurrBootpReqFiltStat,
       "hcxStuIpCurrBootpReplyFiltStat": hcxStuIpCurrBootpReplyFiltStat,
       "hcxStuIpCurrDhcpSnoopFiltStat": hcxStuIpCurrDhcpSnoopFiltStat,
       "hcxStuIpPrevArpFiltStat": hcxStuIpPrevArpFiltStat,
       "hcxStuIpPrevSrcFiltStat": hcxStuIpPrevSrcFiltStat,
       "hcxStuIpPrevDstFiltStat": hcxStuIpPrevDstFiltStat,
       "hcxStuIpPrevBootpReqFiltStat": hcxStuIpPrevBootpReqFiltStat,
       "hcxStuIpPrevBootpReplyFiltStat": hcxStuIpPrevBootpReplyFiltStat,
       "hcxStuIpPrevDhcpSnoopFiltStat": hcxStuIpPrevDhcpSnoopFiltStat,
       "hcxStuIpClearStats": hcxStuIpClearStats,
       "hcxStuL2CurrSnapFiltStat": hcxStuL2CurrSnapFiltStat,
       "hcxStuL2CurrNonSnapFiltStat": hcxStuL2CurrNonSnapFiltStat,
       "hcxStuL2CurrEnetFiltStat": hcxStuL2CurrEnetFiltStat,
       "hcxStuL2CurrArpIpv4FiltStat": hcxStuL2CurrArpIpv4FiltStat,
       "hcxStuL2CurrIpv4FiltStat": hcxStuL2CurrIpv4FiltStat,
       "hcxStuL2CurrIpv6FiltStat": hcxStuL2CurrIpv6FiltStat,
       "hcxStuL2CurrIpxFiltStat": hcxStuL2CurrIpxFiltStat,
       "hcxStuL2CurrAppletalkFiltStat": hcxStuL2CurrAppletalkFiltStat,
       "hcxStuL2CurrOthersFiltStat": hcxStuL2CurrOthersFiltStat,
       "hcxStuIpCurrNetbiosFiltStat": hcxStuIpCurrNetbiosFiltStat,
       "hcxStuL2PrevSnapFiltStat": hcxStuL2PrevSnapFiltStat,
       "hcxStuL2PrevNonSnapFiltStat": hcxStuL2PrevNonSnapFiltStat,
       "hcxStuL2PrevEnetFiltStat": hcxStuL2PrevEnetFiltStat,
       "hcxStuL2PrevArpIpv4FiltStat": hcxStuL2PrevArpIpv4FiltStat,
       "hcxStuL2PrevIpv4FiltStat": hcxStuL2PrevIpv4FiltStat,
       "hcxStuL2PrevIpv6FiltStat": hcxStuL2PrevIpv6FiltStat,
       "hcxStuL2PrevIpxFiltStat": hcxStuL2PrevIpxFiltStat,
       "hcxStuL2PrevAppletalkFiltStat": hcxStuL2PrevAppletalkFiltStat,
       "hcxStuL2PrevOthersFiltStat": hcxStuL2PrevOthersFiltStat,
       "hcxStuIpPrevNetbiosFiltStat": hcxStuIpPrevNetbiosFiltStat,
       "com21HcxStuDstIpAddrGroup": com21HcxStuDstIpAddrGroup,
       "com21HcxStuDstIpAddrTable": com21HcxStuDstIpAddrTable,
       "com21HcxStuDstIpAddrEntry": com21HcxStuDstIpAddrEntry,
       "hcxStuDstIpAddrMacAddr": hcxStuDstIpAddrMacAddr,
       "hcxStuDstIpAddrIPAddr": hcxStuDstIpAddrIPAddr,
       "hcxStuDstIpAddrIPMask": hcxStuDstIpAddrIPMask,
       "hcxStuDstIpAddrIPStatus": hcxStuDstIpAddrIPStatus,
       "hcxStuDstIpAddrEntryId": hcxStuDstIpAddrEntryId,
       "hcxStuAcqEvent": hcxStuAcqEvent,
       "hcxStuDeacqEvent": hcxStuDeacqEvent,
       "hcxIncompSwVersion": hcxIncompSwVersion,
       "hcxUnavailSwVersion": hcxUnavailSwVersion,
       "hcxStuPingTestComplete": hcxStuPingTestComplete,
       "hcxStuEthTestComplete": hcxStuEthTestComplete,
       "hcxStuAcqRangeFail": hcxStuAcqRangeFail,
       "hcxStuAcqOnlineFail": hcxStuAcqOnlineFail,
       "hcxStuArpInvalidAddr": hcxStuArpInvalidAddr,
       "hcxStuArpBadServerAddr": hcxStuArpBadServerAddr,
       "hcxStuRangFailPowerLow": hcxStuRangFailPowerLow,
       "hcxStuRangFailPowerHigh": hcxStuRangFailPowerHigh,
       "hcxStuRangFailLowClear": hcxStuRangFailLowClear,
       "hcxStuRangFailHighClear": hcxStuRangFailHighClear}
)
