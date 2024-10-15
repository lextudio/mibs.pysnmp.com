# SNMP MIB module (CISCO-WIRELESS-P2MP-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-P2MP-PHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:39 2024
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

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

(CwrOscState,
 CwrRfFreqRange,
 CwrRfType) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-TC-MIB",
    "CwrOscState",
    "CwrRfFreqRange",
    "CwrRfType")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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


# MODULE-IDENTITY

ciscoWirelessPhyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170)
)
ciscoWirelessPhyMIB.setRevisions(
        ("2000-10-22 19:10",
         "2000-10-04 19:10",
         "2000-07-21 19:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_P2mpRadioObjects_ObjectIdentity = ObjectIdentity
p2mpRadioObjects = _P2mpRadioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1)
)
_P2mpRadioBaseObjects_ObjectIdentity = ObjectIdentity
p2mpRadioBaseObjects = _P2mpRadioBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1)
)
_P2mpPhyConfigGroup_ObjectIdentity = ObjectIdentity
p2mpPhyConfigGroup = _P2mpPhyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1)
)
_P2mpRadioPhyTable_Object = MibTable
p2mpRadioPhyTable = _P2mpRadioPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpRadioPhyTable.setStatus("current")
_P2mpRadioPhyEntry_Object = MibTableRow
p2mpRadioPhyEntry = _P2mpRadioPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1)
)
p2mpRadioPhyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpRadioPhyEntry.setStatus("current")
_P2mpSelfTest_Type = TruthValue
_P2mpSelfTest_Object = MibTableColumn
p2mpSelfTest = _P2mpSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 1),
    _P2mpSelfTest_Type()
)
p2mpSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSelfTest.setStatus("current")
_P2mpDiversityAntennaPresent_Type = TruthValue
_P2mpDiversityAntennaPresent_Object = MibTableColumn
p2mpDiversityAntennaPresent = _P2mpDiversityAntennaPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 2),
    _P2mpDiversityAntennaPresent_Type()
)
p2mpDiversityAntennaPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpDiversityAntennaPresent.setStatus("current")


class _P2mpCableLoss_Type(Unsigned32):
    """Custom type p2mpCableLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_P2mpCableLoss_Type.__name__ = "Unsigned32"
_P2mpCableLoss_Object = MibTableColumn
p2mpCableLoss = _P2mpCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 3),
    _P2mpCableLoss_Type()
)
p2mpCableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpCableLoss.setStatus("current")
if mibBuilder.loadTexts:
    p2mpCableLoss.setUnits("dB")


class _P2mpCableLossDiversity_Type(Unsigned32):
    """Custom type p2mpCableLossDiversity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_P2mpCableLossDiversity_Type.__name__ = "Unsigned32"
_P2mpCableLossDiversity_Object = MibTableColumn
p2mpCableLossDiversity = _P2mpCableLossDiversity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 4),
    _P2mpCableLossDiversity_Type()
)
p2mpCableLossDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpCableLossDiversity.setStatus("current")
if mibBuilder.loadTexts:
    p2mpCableLossDiversity.setUnits("dB")
_P2mpDenyService_Type = TruthValue
_P2mpDenyService_Object = MibTableColumn
p2mpDenyService = _P2mpDenyService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 5),
    _P2mpDenyService_Type()
)
p2mpDenyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDenyService.setStatus("current")
_P2mpClockRefExt_Type = TruthValue
_P2mpClockRefExt_Object = MibTableColumn
p2mpClockRefExt = _P2mpClockRefExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 6),
    _P2mpClockRefExt_Type()
)
p2mpClockRefExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpClockRefExt.setStatus("current")


class _P2mpCommonTrapEnable_Type(TruthValue):
    """Custom type p2mpCommonTrapEnable based on TruthValue"""


_P2mpCommonTrapEnable_Object = MibTableColumn
p2mpCommonTrapEnable = _P2mpCommonTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 7),
    _P2mpCommonTrapEnable_Type()
)
p2mpCommonTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpCommonTrapEnable.setStatus("current")


class _P2mpLastPhyFailureType_Type(Integer32):
    """Custom type p2mpLastPhyFailureType based on Integer32"""
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
        *(("none", 1),
          ("p2mpAutoCableCompFailure", 6),
          ("p2mpHostIfCommLinkError", 5),
          ("p2mpHwConfigMismatch", 3),
          ("p2mpHwConfigUnsupported", 2),
          ("p2mpHwInitFailure", 4))
    )


_P2mpLastPhyFailureType_Type.__name__ = "Integer32"
_P2mpLastPhyFailureType_Object = MibTableColumn
p2mpLastPhyFailureType = _P2mpLastPhyFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 8),
    _P2mpLastPhyFailureType_Type()
)
p2mpLastPhyFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLastPhyFailureType.setStatus("current")


class _P2mpLastPhyFailureReason_Type(DisplayString):
    """Custom type p2mpLastPhyFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P2mpLastPhyFailureReason_Type.__name__ = "DisplayString"
_P2mpLastPhyFailureReason_Object = MibTableColumn
p2mpLastPhyFailureReason = _P2mpLastPhyFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 1, 1, 1, 9),
    _P2mpLastPhyFailureReason_Type()
)
p2mpLastPhyFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLastPhyFailureReason.setStatus("current")
_P2mpFreqResourceGroup_ObjectIdentity = ObjectIdentity
p2mpFreqResourceGroup = _P2mpFreqResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2)
)
_P2mpRfTable_Object = MibTable
p2mpRfTable = _P2mpRfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    p2mpRfTable.setStatus("current")
_P2mpRfEntry_Object = MibTableRow
p2mpRfEntry = _P2mpRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1)
)
p2mpRfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfIndex"),
)
if mibBuilder.loadTexts:
    p2mpRfEntry.setStatus("current")


class _P2mpRfIndex_Type(Integer32):
    """Custom type p2mpRfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_P2mpRfIndex_Type.__name__ = "Integer32"
_P2mpRfIndex_Object = MibTableColumn
p2mpRfIndex = _P2mpRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 1),
    _P2mpRfIndex_Type()
)
p2mpRfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpRfIndex.setStatus("current")
_P2mpRfType_Type = CwrRfType
_P2mpRfType_Object = MibTableColumn
p2mpRfType = _P2mpRfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 2),
    _P2mpRfType_Type()
)
p2mpRfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfType.setStatus("current")


class _P2mpRfOpMode_Type(Integer32):
    """Custom type p2mpRfOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("receiveOnly", 1),
          ("transmitAndReceive", 3),
          ("transmitOnly", 2))
    )


_P2mpRfOpMode_Type.__name__ = "Integer32"
_P2mpRfOpMode_Object = MibTableColumn
p2mpRfOpMode = _P2mpRfOpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 3),
    _P2mpRfOpMode_Type()
)
p2mpRfOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfOpMode.setStatus("current")
_P2mpTxFreqRangeMin_Type = CwrRfFreqRange
_P2mpTxFreqRangeMin_Object = MibTableColumn
p2mpTxFreqRangeMin = _P2mpTxFreqRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 4),
    _P2mpTxFreqRangeMin_Type()
)
p2mpTxFreqRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTxFreqRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpTxFreqRangeMin.setUnits("KHz")
_P2mpTxFreqRangeMax_Type = CwrRfFreqRange
_P2mpTxFreqRangeMax_Object = MibTableColumn
p2mpTxFreqRangeMax = _P2mpTxFreqRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 5),
    _P2mpTxFreqRangeMax_Type()
)
p2mpTxFreqRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTxFreqRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpTxFreqRangeMax.setUnits("KHz")
_P2mpRxFreqRangeMin_Type = CwrRfFreqRange
_P2mpRxFreqRangeMin_Object = MibTableColumn
p2mpRxFreqRangeMin = _P2mpRxFreqRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 6),
    _P2mpRxFreqRangeMin_Type()
)
p2mpRxFreqRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRxFreqRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpRxFreqRangeMin.setUnits("KHz")
_P2mpRxFreqRangeMax_Type = CwrRfFreqRange
_P2mpRxFreqRangeMax_Object = MibTableColumn
p2mpRxFreqRangeMax = _P2mpRxFreqRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 7),
    _P2mpRxFreqRangeMax_Type()
)
p2mpRxFreqRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRxFreqRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpRxFreqRangeMax.setUnits("KHz")


class _P2mpMinTxPower_Type(Integer32):
    """Custom type p2mpMinTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_P2mpMinTxPower_Type.__name__ = "Integer32"
_P2mpMinTxPower_Object = MibTableColumn
p2mpMinTxPower = _P2mpMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 8),
    _P2mpMinTxPower_Type()
)
p2mpMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpMinTxPower.setStatus("current")
if mibBuilder.loadTexts:
    p2mpMinTxPower.setUnits("dBm")


class _P2mpMaxTxPower_Type(Integer32):
    """Custom type p2mpMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_P2mpMaxTxPower_Type.__name__ = "Integer32"
_P2mpMaxTxPower_Object = MibTableColumn
p2mpMaxTxPower = _P2mpMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 9),
    _P2mpMaxTxPower_Type()
)
p2mpMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    p2mpMaxTxPower.setUnits("dBm")


class _P2mpRfTemperature_Type(Integer32):
    """Custom type p2mpRfTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_P2mpRfTemperature_Type.__name__ = "Integer32"
_P2mpRfTemperature_Object = MibTableColumn
p2mpRfTemperature = _P2mpRfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 10),
    _P2mpRfTemperature_Type()
)
p2mpRfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfTemperature.setStatus("current")
if mibBuilder.loadTexts:
    p2mpRfTemperature.setUnits("Degrees Centigrade")
_P2mpRfTxOscState_Type = CwrOscState
_P2mpRfTxOscState_Object = MibTableColumn
p2mpRfTxOscState = _P2mpRfTxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 11),
    _P2mpRfTxOscState_Type()
)
p2mpRfTxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfTxOscState.setStatus("current")
_P2mpRfRxOscState_Type = CwrOscState
_P2mpRfRxOscState_Object = MibTableColumn
p2mpRfRxOscState = _P2mpRfRxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 12),
    _P2mpRfRxOscState_Type()
)
p2mpRfRxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfRxOscState.setStatus("current")


class _P2mpRfSupplyVoltageState_Type(Integer32):
    """Custom type p2mpRfSupplyVoltageState based on Integer32"""
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


_P2mpRfSupplyVoltageState_Type.__name__ = "Integer32"
_P2mpRfSupplyVoltageState_Object = MibTableColumn
p2mpRfSupplyVoltageState = _P2mpRfSupplyVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 13),
    _P2mpRfSupplyVoltageState_Type()
)
p2mpRfSupplyVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfSupplyVoltageState.setStatus("current")


class _P2mpRfStatus_Type(Integer32):
    """Custom type p2mpRfStatus based on Integer32"""
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


_P2mpRfStatus_Type.__name__ = "Integer32"
_P2mpRfStatus_Object = MibTableColumn
p2mpRfStatus = _P2mpRfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 14),
    _P2mpRfStatus_Type()
)
p2mpRfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfStatus.setStatus("current")
_P2mpRfLoopbackSupported_Type = TruthValue
_P2mpRfLoopbackSupported_Object = MibTableColumn
p2mpRfLoopbackSupported = _P2mpRfLoopbackSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 1, 1, 15),
    _P2mpRfLoopbackSupported_Type()
)
p2mpRfLoopbackSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfLoopbackSupported.setStatus("current")
_P2mpDuplexerTable_Object = MibTable
p2mpDuplexerTable = _P2mpDuplexerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    p2mpDuplexerTable.setStatus("current")
_P2mpDuplexerEntry_Object = MibTableRow
p2mpDuplexerEntry = _P2mpDuplexerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1)
)
p2mpDuplexerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerIndex"),
)
if mibBuilder.loadTexts:
    p2mpDuplexerEntry.setStatus("current")


class _P2mpDuplexerIndex_Type(Integer32):
    """Custom type p2mpDuplexerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_P2mpDuplexerIndex_Type.__name__ = "Integer32"
_P2mpDuplexerIndex_Object = MibTableColumn
p2mpDuplexerIndex = _P2mpDuplexerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 1),
    _P2mpDuplexerIndex_Type()
)
p2mpDuplexerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpDuplexerIndex.setStatus("current")
_P2mpDuplexerRF_Type = CwrRfType
_P2mpDuplexerRF_Object = MibTableColumn
p2mpDuplexerRF = _P2mpDuplexerRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 2),
    _P2mpDuplexerRF_Type()
)
p2mpDuplexerRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerRF.setStatus("current")
_P2mpDuplexerLoPassbandMinFreq_Type = CwrRfFreqRange
_P2mpDuplexerLoPassbandMinFreq_Object = MibTableColumn
p2mpDuplexerLoPassbandMinFreq = _P2mpDuplexerLoPassbandMinFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 3),
    _P2mpDuplexerLoPassbandMinFreq_Type()
)
p2mpDuplexerLoPassbandMinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerLoPassbandMinFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpDuplexerLoPassbandMinFreq.setUnits("MHz")
_P2mpDuplexerLoPassbandMaxFreq_Type = CwrRfFreqRange
_P2mpDuplexerLoPassbandMaxFreq_Object = MibTableColumn
p2mpDuplexerLoPassbandMaxFreq = _P2mpDuplexerLoPassbandMaxFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 4),
    _P2mpDuplexerLoPassbandMaxFreq_Type()
)
p2mpDuplexerLoPassbandMaxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerLoPassbandMaxFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpDuplexerLoPassbandMaxFreq.setUnits("MHz")
_P2mpDuplexerHiPassbandMinFreq_Type = CwrRfFreqRange
_P2mpDuplexerHiPassbandMinFreq_Object = MibTableColumn
p2mpDuplexerHiPassbandMinFreq = _P2mpDuplexerHiPassbandMinFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 5),
    _P2mpDuplexerHiPassbandMinFreq_Type()
)
p2mpDuplexerHiPassbandMinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerHiPassbandMinFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpDuplexerHiPassbandMinFreq.setUnits("MHz")
_P2mpDuplexerHiPassbandMaxFreq_Type = CwrRfFreqRange
_P2mpDuplexerHiPassbandMaxFreq_Object = MibTableColumn
p2mpDuplexerHiPassbandMaxFreq = _P2mpDuplexerHiPassbandMaxFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 6),
    _P2mpDuplexerHiPassbandMaxFreq_Type()
)
p2mpDuplexerHiPassbandMaxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerHiPassbandMaxFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpDuplexerHiPassbandMaxFreq.setUnits("MHz")


class _P2mpDuplexerReceivePassband_Type(Integer32):
    """Custom type p2mpDuplexerReceivePassband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hiPassband", 2),
          ("loPassband", 1))
    )


_P2mpDuplexerReceivePassband_Type.__name__ = "Integer32"
_P2mpDuplexerReceivePassband_Object = MibTableColumn
p2mpDuplexerReceivePassband = _P2mpDuplexerReceivePassband_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 7),
    _P2mpDuplexerReceivePassband_Type()
)
p2mpDuplexerReceivePassband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerReceivePassband.setStatus("current")
_P2mpDuplexerTxInsertionLoss_Type = Integer32
_P2mpDuplexerTxInsertionLoss_Object = MibTableColumn
p2mpDuplexerTxInsertionLoss = _P2mpDuplexerTxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 8),
    _P2mpDuplexerTxInsertionLoss_Type()
)
p2mpDuplexerTxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerTxInsertionLoss.setStatus("current")
if mibBuilder.loadTexts:
    p2mpDuplexerTxInsertionLoss.setUnits("dB")
_P2mpDuplexerBurnDate_Type = DisplayString
_P2mpDuplexerBurnDate_Object = MibTableColumn
p2mpDuplexerBurnDate = _P2mpDuplexerBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 2, 1, 9),
    _P2mpDuplexerBurnDate_Type()
)
p2mpDuplexerBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpDuplexerBurnDate.setStatus("current")
_P2mpAntennaTable_Object = MibTable
p2mpAntennaTable = _P2mpAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    p2mpAntennaTable.setStatus("current")
_P2mpAntennaEntry_Object = MibTableRow
p2mpAntennaEntry = _P2mpAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1)
)
p2mpAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaIndex"),
)
if mibBuilder.loadTexts:
    p2mpAntennaEntry.setStatus("current")
_P2mpAntennaIndex_Type = Unsigned32
_P2mpAntennaIndex_Object = MibTableColumn
p2mpAntennaIndex = _P2mpAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 1),
    _P2mpAntennaIndex_Type()
)
p2mpAntennaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpAntennaIndex.setStatus("current")
_P2mpRfResource_Type = CwrRfType
_P2mpRfResource_Object = MibTableColumn
p2mpRfResource = _P2mpRfResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 2),
    _P2mpRfResource_Type()
)
p2mpRfResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRfResource.setStatus("current")


class _P2mpAntennaXDim_Type(Unsigned32):
    """Custom type p2mpAntennaXDim based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_P2mpAntennaXDim_Type.__name__ = "Unsigned32"
_P2mpAntennaXDim_Object = MibTableColumn
p2mpAntennaXDim = _P2mpAntennaXDim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 3),
    _P2mpAntennaXDim_Type()
)
p2mpAntennaXDim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpAntennaXDim.setStatus("current")
if mibBuilder.loadTexts:
    p2mpAntennaXDim.setUnits("Inches")


class _P2mpAntennaYDim_Type(Unsigned32):
    """Custom type p2mpAntennaYDim based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_P2mpAntennaYDim_Type.__name__ = "Unsigned32"
_P2mpAntennaYDim_Object = MibTableColumn
p2mpAntennaYDim = _P2mpAntennaYDim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 4),
    _P2mpAntennaYDim_Type()
)
p2mpAntennaYDim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpAntennaYDim.setStatus("current")
if mibBuilder.loadTexts:
    p2mpAntennaYDim.setUnits("Inches")


class _P2mpAntennaType_Type(DisplayString):
    """Custom type p2mpAntennaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_P2mpAntennaType_Type.__name__ = "DisplayString"
_P2mpAntennaType_Object = MibTableColumn
p2mpAntennaType = _P2mpAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 5),
    _P2mpAntennaType_Type()
)
p2mpAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpAntennaType.setStatus("current")


class _P2mpAntennaDescr_Type(DisplayString):
    """Custom type p2mpAntennaDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_P2mpAntennaDescr_Type.__name__ = "DisplayString"
_P2mpAntennaDescr_Object = MibTableColumn
p2mpAntennaDescr = _P2mpAntennaDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 6),
    _P2mpAntennaDescr_Type()
)
p2mpAntennaDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpAntennaDescr.setStatus("current")


class _P2mpAntennaGain_Type(Unsigned32):
    """Custom type p2mpAntennaGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_P2mpAntennaGain_Type.__name__ = "Unsigned32"
_P2mpAntennaGain_Object = MibTableColumn
p2mpAntennaGain = _P2mpAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 7),
    _P2mpAntennaGain_Type()
)
p2mpAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    p2mpAntennaGain.setUnits("dBi : decibel Isotropic")


class _P2mpAntennaPolarization_Type(Integer32):
    """Custom type p2mpAntennaPolarization based on Integer32"""
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


_P2mpAntennaPolarization_Type.__name__ = "Integer32"
_P2mpAntennaPolarization_Object = MibTableColumn
p2mpAntennaPolarization = _P2mpAntennaPolarization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 2, 3, 1, 8),
    _P2mpAntennaPolarization_Type()
)
p2mpAntennaPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpAntennaPolarization.setStatus("current")
_P2mpRadioTestGroup_ObjectIdentity = ObjectIdentity
p2mpRadioTestGroup = _P2mpRadioTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3)
)
_P2mpLoopbackTable_Object = MibTable
p2mpLoopbackTable = _P2mpLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    p2mpLoopbackTable.setStatus("current")
_P2mpLoopbackEntry_Object = MibTableRow
p2mpLoopbackEntry = _P2mpLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3, 1, 1)
)
p2mpLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpLoopbackEntry.setStatus("current")


class _P2mpLocalLoopbackMode_Type(Integer32):
    """Custom type p2mpLocalLoopbackMode based on Integer32"""
    defaultValue = 1

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
        *(("fir", 2),
          ("if", 3),
          ("noLoopback", 1),
          ("rf", 4))
    )


_P2mpLocalLoopbackMode_Type.__name__ = "Integer32"
_P2mpLocalLoopbackMode_Object = MibTableColumn
p2mpLocalLoopbackMode = _P2mpLocalLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3, 1, 1, 1),
    _P2mpLocalLoopbackMode_Type()
)
p2mpLocalLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpLocalLoopbackMode.setStatus("current")
_P2mpLocalLoopbackAntenna_Type = CwrRfType
_P2mpLocalLoopbackAntenna_Object = MibTableColumn
p2mpLocalLoopbackAntenna = _P2mpLocalLoopbackAntenna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3, 1, 1, 2),
    _P2mpLocalLoopbackAntenna_Type()
)
p2mpLocalLoopbackAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpLocalLoopbackAntenna.setStatus("current")


class _P2mpLocalLoopbackChannel_Type(Unsigned32):
    """Custom type p2mpLocalLoopbackChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_P2mpLocalLoopbackChannel_Type.__name__ = "Unsigned32"
_P2mpLocalLoopbackChannel_Object = MibTableColumn
p2mpLocalLoopbackChannel = _P2mpLocalLoopbackChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 3, 1, 1, 3),
    _P2mpLocalLoopbackChannel_Type()
)
p2mpLocalLoopbackChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpLocalLoopbackChannel.setStatus("current")
_P2mpLedGroup_ObjectIdentity = ObjectIdentity
p2mpLedGroup = _P2mpLedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4)
)
_P2mpLedTable_Object = MibTable
p2mpLedTable = _P2mpLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    p2mpLedTable.setStatus("current")
_P2mpLedEntry_Object = MibTableRow
p2mpLedEntry = _P2mpLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4, 1, 1)
)
p2mpLedEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLedIndex"),
)
if mibBuilder.loadTexts:
    p2mpLedEntry.setStatus("current")


class _P2mpLedIndex_Type(Integer32):
    """Custom type p2mpLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_P2mpLedIndex_Type.__name__ = "Integer32"
_P2mpLedIndex_Object = MibTableColumn
p2mpLedIndex = _P2mpLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4, 1, 1, 1),
    _P2mpLedIndex_Type()
)
p2mpLedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpLedIndex.setStatus("current")


class _P2mpLedType_Type(Integer32):
    """Custom type p2mpLedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("carrier", 4),
          ("interfaceEnable", 0),
          ("majorAlarm", 1),
          ("minorAlarm", 2),
          ("outOfService", 3),
          ("receiveData", 6),
          ("transmitData", 5))
    )


_P2mpLedType_Type.__name__ = "Integer32"
_P2mpLedType_Object = MibTableColumn
p2mpLedType = _P2mpLedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4, 1, 1, 2),
    _P2mpLedType_Type()
)
p2mpLedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLedType.setStatus("current")


class _P2mpLedState_Type(Integer32):
    """Custom type p2mpLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("off", 0),
          ("yellow", 2))
    )


_P2mpLedState_Type.__name__ = "Integer32"
_P2mpLedState_Object = MibTableColumn
p2mpLedState = _P2mpLedState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 1, 4, 1, 1, 3),
    _P2mpLedState_Type()
)
p2mpLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLedState.setStatus("current")
_P2mpRadioSuObjects_ObjectIdentity = ObjectIdentity
p2mpRadioSuObjects = _P2mpRadioSuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2)
)
_P2mpSuRadioPhyTable_Object = MibTable
p2mpSuRadioPhyTable = _P2mpSuRadioPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 1)
)
if mibBuilder.loadTexts:
    p2mpSuRadioPhyTable.setStatus("current")
_P2mpSuRadioPhyEntry_Object = MibTableRow
p2mpSuRadioPhyEntry = _P2mpSuRadioPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 1, 1)
)
p2mpSuRadioPhyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpSuRadioPhyEntry.setStatus("current")
_P2mpSuTxMuteEnable_Type = TruthValue
_P2mpSuTxMuteEnable_Object = MibTableColumn
p2mpSuTxMuteEnable = _P2mpSuTxMuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 1, 1, 1),
    _P2mpSuTxMuteEnable_Type()
)
p2mpSuTxMuteEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuTxMuteEnable.setStatus("current")


class _P2mpSuTxMuteDuration_Type(Unsigned32):
    """Custom type p2mpSuTxMuteDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_P2mpSuTxMuteDuration_Type.__name__ = "Unsigned32"
_P2mpSuTxMuteDuration_Object = MibTableColumn
p2mpSuTxMuteDuration = _P2mpSuTxMuteDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 1, 1, 2),
    _P2mpSuTxMuteDuration_Type()
)
p2mpSuTxMuteDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuTxMuteDuration.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuTxMuteDuration.setUnits("minutes")
_P2mpSuPowerScanTable_Object = MibTable
p2mpSuPowerScanTable = _P2mpSuPowerScanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 2)
)
if mibBuilder.loadTexts:
    p2mpSuPowerScanTable.setStatus("current")
_P2mpSuPowerScanEntry_Object = MibTableRow
p2mpSuPowerScanEntry = _P2mpSuPowerScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 2, 1)
)
p2mpSuPowerScanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSuPowerScanIndex"),
)
if mibBuilder.loadTexts:
    p2mpSuPowerScanEntry.setStatus("current")


class _P2mpSuPowerScanIndex_Type(Integer32):
    """Custom type p2mpSuPowerScanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_P2mpSuPowerScanIndex_Type.__name__ = "Integer32"
_P2mpSuPowerScanIndex_Object = MibTableColumn
p2mpSuPowerScanIndex = _P2mpSuPowerScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 2, 1, 1),
    _P2mpSuPowerScanIndex_Type()
)
p2mpSuPowerScanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSuPowerScanIndex.setStatus("current")
_P2mpSuCenterFrequency_Type = CwrRfFreqRange
_P2mpSuCenterFrequency_Object = MibTableColumn
p2mpSuCenterFrequency = _P2mpSuCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 2, 1, 2),
    _P2mpSuCenterFrequency_Type()
)
p2mpSuCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuCenterFrequency.setUnits("KHz")


class _P2mpSuMeasuredPower_Type(Integer32):
    """Custom type p2mpSuMeasuredPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 50),
    )


_P2mpSuMeasuredPower_Type.__name__ = "Integer32"
_P2mpSuMeasuredPower_Object = MibTableColumn
p2mpSuMeasuredPower = _P2mpSuMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 2, 2, 1, 3),
    _P2mpSuMeasuredPower_Type()
)
p2mpSuMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuMeasuredPower.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuMeasuredPower.setUnits("dBm")
_P2mpRadioHeObjects_ObjectIdentity = ObjectIdentity
p2mpRadioHeObjects = _P2mpRadioHeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3)
)
_P2mpHeAlcTable_Object = MibTable
p2mpHeAlcTable = _P2mpHeAlcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 1)
)
if mibBuilder.loadTexts:
    p2mpHeAlcTable.setStatus("current")
_P2mpHeAlcEntry_Object = MibTableRow
p2mpHeAlcEntry = _P2mpHeAlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 1, 1)
)
p2mpHeAlcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpHeAlcEntry.setStatus("current")
_P2mpHeAlcEnable_Type = TruthValue
_P2mpHeAlcEnable_Object = MibTableColumn
p2mpHeAlcEnable = _P2mpHeAlcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 1, 1, 1),
    _P2mpHeAlcEnable_Type()
)
p2mpHeAlcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHeAlcEnable.setStatus("current")


class _P2mpHeAlcInterval_Type(Unsigned32):
    """Custom type p2mpHeAlcInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1024),
    )


_P2mpHeAlcInterval_Type.__name__ = "Unsigned32"
_P2mpHeAlcInterval_Object = MibTableColumn
p2mpHeAlcInterval = _P2mpHeAlcInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 1, 1, 2),
    _P2mpHeAlcInterval_Type()
)
p2mpHeAlcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHeAlcInterval.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHeAlcInterval.setUnits("milliseconds")


class _P2mpHeAlcNumMiniSlots_Type(Unsigned32):
    """Custom type p2mpHeAlcNumMiniSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P2mpHeAlcNumMiniSlots_Type.__name__ = "Unsigned32"
_P2mpHeAlcNumMiniSlots_Object = MibTableColumn
p2mpHeAlcNumMiniSlots = _P2mpHeAlcNumMiniSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 1, 1, 3),
    _P2mpHeAlcNumMiniSlots_Type()
)
p2mpHeAlcNumMiniSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHeAlcNumMiniSlots.setStatus("current")
_P2mpHeIntFreqTable_Object = MibTable
p2mpHeIntFreqTable = _P2mpHeIntFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2)
)
if mibBuilder.loadTexts:
    p2mpHeIntFreqTable.setStatus("current")
_P2mpHeIntFreqEntry_Object = MibTableRow
p2mpHeIntFreqEntry = _P2mpHeIntFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1)
)
p2mpHeIntFreqEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpHeIntFreqEntry.setStatus("current")
_P2mpHeIfTxOscState_Type = CwrOscState
_P2mpHeIfTxOscState_Object = MibTableColumn
p2mpHeIfTxOscState = _P2mpHeIfTxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 1),
    _P2mpHeIfTxOscState_Type()
)
p2mpHeIfTxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeIfTxOscState.setStatus("current")
_P2mpHeIfRxOscState_Type = CwrOscState
_P2mpHeIfRxOscState_Object = MibTableColumn
p2mpHeIfRxOscState = _P2mpHeIfRxOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 2),
    _P2mpHeIfRxOscState_Type()
)
p2mpHeIfRxOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeIfRxOscState.setStatus("current")
_P2mpHeIfRefOscState_Type = CwrOscState
_P2mpHeIfRefOscState_Object = MibTableColumn
p2mpHeIfRefOscState = _P2mpHeIfRefOscState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 3),
    _P2mpHeIfRefOscState_Type()
)
p2mpHeIfRefOscState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeIfRefOscState.setStatus("current")


class _P2mpHeIfInpFreq_Type(Unsigned32):
    """Custom type p2mpHeIfInpFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 500000),
    )


_P2mpHeIfInpFreq_Type.__name__ = "Unsigned32"
_P2mpHeIfInpFreq_Object = MibTableColumn
p2mpHeIfInpFreq = _P2mpHeIfInpFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 4),
    _P2mpHeIfInpFreq_Type()
)
p2mpHeIfInpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeIfInpFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHeIfInpFreq.setUnits("KHz")


class _P2mpHeIfOutFreq_Type(Unsigned32):
    """Custom type p2mpHeIfOutFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 500000),
    )


_P2mpHeIfOutFreq_Type.__name__ = "Unsigned32"
_P2mpHeIfOutFreq_Object = MibTableColumn
p2mpHeIfOutFreq = _P2mpHeIfOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 5),
    _P2mpHeIfOutFreq_Type()
)
p2mpHeIfOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeIfOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHeIfOutFreq.setUnits("KHz")


class _P2mpHeTrapEnable_Type(TruthValue):
    """Custom type p2mpHeTrapEnable based on TruthValue"""


_P2mpHeTrapEnable_Object = MibTableColumn
p2mpHeTrapEnable = _P2mpHeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 3, 2, 1, 6),
    _P2mpHeTrapEnable_Type()
)
p2mpHeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHeTrapEnable.setStatus("current")
_P2mpRadioPhyConformance_ObjectIdentity = ObjectIdentity
p2mpRadioPhyConformance = _P2mpRadioPhyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4)
)
_P2mpRadioPhyCompliances_ObjectIdentity = ObjectIdentity
p2mpRadioPhyCompliances = _P2mpRadioPhyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 1)
)
_P2mpRadioPhyGroups_ObjectIdentity = ObjectIdentity
p2mpRadioPhyGroups = _P2mpRadioPhyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2)
)
_P2mpPhyMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
p2mpPhyMIBNotificationPrefix = _P2mpPhyMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2)
)
_P2mpPhyMIBNotification_ObjectIdentity = ObjectIdentity
p2mpPhyMIBNotification = _P2mpPhyMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0)
)

# Managed Objects groups

p2mpCommonRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 1)
)
p2mpCommonRadioGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSelfTest"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDiversityAntennaPresent"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpCableLoss"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpCableLossDiversity"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDenyService"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpClockRefExt"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpCommonTrapEnable"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLastPhyFailureType"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLastPhyFailureReason"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLedType"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLedState"))
)
if mibBuilder.loadTexts:
    p2mpCommonRadioGroup.setStatus("current")

p2mpCommonRfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 2)
)
p2mpCommonRfGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfType"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfOpMode"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpTxFreqRangeMin"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpTxFreqRangeMax"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRxFreqRangeMin"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRxFreqRangeMax"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpMinTxPower"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpMaxTxPower"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfTxOscState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfRxOscState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfTemperature"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfSupplyVoltageState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfStatus"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfLoopbackSupported"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerRF"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerLoPassbandMinFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerLoPassbandMaxFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerHiPassbandMinFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerHiPassbandMaxFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerReceivePassband"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerTxInsertionLoss"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpDuplexerBurnDate"))
)
if mibBuilder.loadTexts:
    p2mpCommonRfGroup.setStatus("current")

p2mpCommonTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 3)
)
p2mpCommonTestGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLocalLoopbackMode"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLocalLoopbackAntenna"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLocalLoopbackChannel"))
)
if mibBuilder.loadTexts:
    p2mpCommonTestGroup.setStatus("current")

p2mpRadioSuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 5)
)
p2mpRadioSuGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSuTxMuteEnable"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSuTxMuteDuration"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSuCenterFrequency"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpSuMeasuredPower"))
)
if mibBuilder.loadTexts:
    p2mpRadioSuGroup.setStatus("current")

p2mpRadioHeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 6)
)
p2mpRadioHeGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeAlcEnable"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeAlcInterval"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeAlcNumMiniSlots"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfTxOscState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfRxOscState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfRefOscState"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfInpFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfOutFreq"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeTrapEnable"))
)
if mibBuilder.loadTexts:
    p2mpRadioHeGroup.setStatus("current")

p2mpRadioAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 2, 8)
)
p2mpRadioAntennaGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfResource"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaXDim"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaYDim"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaType"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaDescr"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaGain"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpAntennaPolarization"))
)
if mibBuilder.loadTexts:
    p2mpRadioAntennaGroup.setStatus("current")


# Notification objects

p2mpRadioPhyFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 1)
)
p2mpRadioPhyFailNotification.setObjects(
      *(("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLastPhyFailureType"),
        ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpLastPhyFailureReason"))
)
if mibBuilder.loadTexts:
    p2mpRadioPhyFailNotification.setStatus(
        "current"
    )

p2mpTrapRfSupplyVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 2)
)
p2mpTrapRfSupplyVoltage.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfSupplyVoltageState")
)
if mibBuilder.loadTexts:
    p2mpTrapRfSupplyVoltage.setStatus(
        "current"
    )

p2mpTrapRfRxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 3)
)
p2mpTrapRfRxOsc.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfRxOscState")
)
if mibBuilder.loadTexts:
    p2mpTrapRfRxOsc.setStatus(
        "current"
    )

p2mpTrapRfTxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 4)
)
p2mpTrapRfTxOsc.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfTxOscState")
)
if mibBuilder.loadTexts:
    p2mpTrapRfTxOsc.setStatus(
        "current"
    )

p2mpTrapRfTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 5)
)
p2mpTrapRfTemp.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfTemperature")
)
if mibBuilder.loadTexts:
    p2mpTrapRfTemp.setStatus(
        "current"
    )

p2mpTrapRfCommLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 6)
)
p2mpTrapRfCommLinkError.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfType")
)
if mibBuilder.loadTexts:
    p2mpTrapRfCommLinkError.setStatus(
        "current"
    )

p2mpTrapTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 7)
)
p2mpTrapTxPower.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfType")
)
if mibBuilder.loadTexts:
    p2mpTrapTxPower.setStatus(
        "current"
    )

p2mpTrapRfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 8)
)
p2mpTrapRfStatusChange.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpRfStatus")
)
if mibBuilder.loadTexts:
    p2mpTrapRfStatusChange.setStatus(
        "current"
    )

p2mpTrapHeIfRxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 9)
)
p2mpTrapHeIfRxOsc.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfRxOscState")
)
if mibBuilder.loadTexts:
    p2mpTrapHeIfRxOsc.setStatus(
        "current"
    )

p2mpTrapHeIfTxOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 10)
)
p2mpTrapHeIfTxOsc.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfTxOscState")
)
if mibBuilder.loadTexts:
    p2mpTrapHeIfTxOsc.setStatus(
        "current"
    )

p2mpTrapHeIfExtRefOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 2, 0, 11)
)
p2mpTrapHeIfExtRefOsc.setObjects(
    ("CISCO-WIRELESS-P2MP-PHY-MIB", "p2mpHeIfRefOscState")
)
if mibBuilder.loadTexts:
    p2mpTrapHeIfExtRefOsc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

p2mpRadioPhyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 170, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpRadioPhyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-P2MP-PHY-MIB",
    **{"ciscoWirelessPhyMIB": ciscoWirelessPhyMIB,
       "p2mpRadioObjects": p2mpRadioObjects,
       "p2mpRadioBaseObjects": p2mpRadioBaseObjects,
       "p2mpPhyConfigGroup": p2mpPhyConfigGroup,
       "p2mpRadioPhyTable": p2mpRadioPhyTable,
       "p2mpRadioPhyEntry": p2mpRadioPhyEntry,
       "p2mpSelfTest": p2mpSelfTest,
       "p2mpDiversityAntennaPresent": p2mpDiversityAntennaPresent,
       "p2mpCableLoss": p2mpCableLoss,
       "p2mpCableLossDiversity": p2mpCableLossDiversity,
       "p2mpDenyService": p2mpDenyService,
       "p2mpClockRefExt": p2mpClockRefExt,
       "p2mpCommonTrapEnable": p2mpCommonTrapEnable,
       "p2mpLastPhyFailureType": p2mpLastPhyFailureType,
       "p2mpLastPhyFailureReason": p2mpLastPhyFailureReason,
       "p2mpFreqResourceGroup": p2mpFreqResourceGroup,
       "p2mpRfTable": p2mpRfTable,
       "p2mpRfEntry": p2mpRfEntry,
       "p2mpRfIndex": p2mpRfIndex,
       "p2mpRfType": p2mpRfType,
       "p2mpRfOpMode": p2mpRfOpMode,
       "p2mpTxFreqRangeMin": p2mpTxFreqRangeMin,
       "p2mpTxFreqRangeMax": p2mpTxFreqRangeMax,
       "p2mpRxFreqRangeMin": p2mpRxFreqRangeMin,
       "p2mpRxFreqRangeMax": p2mpRxFreqRangeMax,
       "p2mpMinTxPower": p2mpMinTxPower,
       "p2mpMaxTxPower": p2mpMaxTxPower,
       "p2mpRfTemperature": p2mpRfTemperature,
       "p2mpRfTxOscState": p2mpRfTxOscState,
       "p2mpRfRxOscState": p2mpRfRxOscState,
       "p2mpRfSupplyVoltageState": p2mpRfSupplyVoltageState,
       "p2mpRfStatus": p2mpRfStatus,
       "p2mpRfLoopbackSupported": p2mpRfLoopbackSupported,
       "p2mpDuplexerTable": p2mpDuplexerTable,
       "p2mpDuplexerEntry": p2mpDuplexerEntry,
       "p2mpDuplexerIndex": p2mpDuplexerIndex,
       "p2mpDuplexerRF": p2mpDuplexerRF,
       "p2mpDuplexerLoPassbandMinFreq": p2mpDuplexerLoPassbandMinFreq,
       "p2mpDuplexerLoPassbandMaxFreq": p2mpDuplexerLoPassbandMaxFreq,
       "p2mpDuplexerHiPassbandMinFreq": p2mpDuplexerHiPassbandMinFreq,
       "p2mpDuplexerHiPassbandMaxFreq": p2mpDuplexerHiPassbandMaxFreq,
       "p2mpDuplexerReceivePassband": p2mpDuplexerReceivePassband,
       "p2mpDuplexerTxInsertionLoss": p2mpDuplexerTxInsertionLoss,
       "p2mpDuplexerBurnDate": p2mpDuplexerBurnDate,
       "p2mpAntennaTable": p2mpAntennaTable,
       "p2mpAntennaEntry": p2mpAntennaEntry,
       "p2mpAntennaIndex": p2mpAntennaIndex,
       "p2mpRfResource": p2mpRfResource,
       "p2mpAntennaXDim": p2mpAntennaXDim,
       "p2mpAntennaYDim": p2mpAntennaYDim,
       "p2mpAntennaType": p2mpAntennaType,
       "p2mpAntennaDescr": p2mpAntennaDescr,
       "p2mpAntennaGain": p2mpAntennaGain,
       "p2mpAntennaPolarization": p2mpAntennaPolarization,
       "p2mpRadioTestGroup": p2mpRadioTestGroup,
       "p2mpLoopbackTable": p2mpLoopbackTable,
       "p2mpLoopbackEntry": p2mpLoopbackEntry,
       "p2mpLocalLoopbackMode": p2mpLocalLoopbackMode,
       "p2mpLocalLoopbackAntenna": p2mpLocalLoopbackAntenna,
       "p2mpLocalLoopbackChannel": p2mpLocalLoopbackChannel,
       "p2mpLedGroup": p2mpLedGroup,
       "p2mpLedTable": p2mpLedTable,
       "p2mpLedEntry": p2mpLedEntry,
       "p2mpLedIndex": p2mpLedIndex,
       "p2mpLedType": p2mpLedType,
       "p2mpLedState": p2mpLedState,
       "p2mpRadioSuObjects": p2mpRadioSuObjects,
       "p2mpSuRadioPhyTable": p2mpSuRadioPhyTable,
       "p2mpSuRadioPhyEntry": p2mpSuRadioPhyEntry,
       "p2mpSuTxMuteEnable": p2mpSuTxMuteEnable,
       "p2mpSuTxMuteDuration": p2mpSuTxMuteDuration,
       "p2mpSuPowerScanTable": p2mpSuPowerScanTable,
       "p2mpSuPowerScanEntry": p2mpSuPowerScanEntry,
       "p2mpSuPowerScanIndex": p2mpSuPowerScanIndex,
       "p2mpSuCenterFrequency": p2mpSuCenterFrequency,
       "p2mpSuMeasuredPower": p2mpSuMeasuredPower,
       "p2mpRadioHeObjects": p2mpRadioHeObjects,
       "p2mpHeAlcTable": p2mpHeAlcTable,
       "p2mpHeAlcEntry": p2mpHeAlcEntry,
       "p2mpHeAlcEnable": p2mpHeAlcEnable,
       "p2mpHeAlcInterval": p2mpHeAlcInterval,
       "p2mpHeAlcNumMiniSlots": p2mpHeAlcNumMiniSlots,
       "p2mpHeIntFreqTable": p2mpHeIntFreqTable,
       "p2mpHeIntFreqEntry": p2mpHeIntFreqEntry,
       "p2mpHeIfTxOscState": p2mpHeIfTxOscState,
       "p2mpHeIfRxOscState": p2mpHeIfRxOscState,
       "p2mpHeIfRefOscState": p2mpHeIfRefOscState,
       "p2mpHeIfInpFreq": p2mpHeIfInpFreq,
       "p2mpHeIfOutFreq": p2mpHeIfOutFreq,
       "p2mpHeTrapEnable": p2mpHeTrapEnable,
       "p2mpRadioPhyConformance": p2mpRadioPhyConformance,
       "p2mpRadioPhyCompliances": p2mpRadioPhyCompliances,
       "p2mpRadioPhyCompliance": p2mpRadioPhyCompliance,
       "p2mpRadioPhyGroups": p2mpRadioPhyGroups,
       "p2mpCommonRadioGroup": p2mpCommonRadioGroup,
       "p2mpCommonRfGroup": p2mpCommonRfGroup,
       "p2mpCommonTestGroup": p2mpCommonTestGroup,
       "p2mpRadioSuGroup": p2mpRadioSuGroup,
       "p2mpRadioHeGroup": p2mpRadioHeGroup,
       "p2mpRadioAntennaGroup": p2mpRadioAntennaGroup,
       "p2mpPhyMIBNotificationPrefix": p2mpPhyMIBNotificationPrefix,
       "p2mpPhyMIBNotification": p2mpPhyMIBNotification,
       "p2mpRadioPhyFailNotification": p2mpRadioPhyFailNotification,
       "p2mpTrapRfSupplyVoltage": p2mpTrapRfSupplyVoltage,
       "p2mpTrapRfRxOsc": p2mpTrapRfRxOsc,
       "p2mpTrapRfTxOsc": p2mpTrapRfTxOsc,
       "p2mpTrapRfTemp": p2mpTrapRfTemp,
       "p2mpTrapRfCommLinkError": p2mpTrapRfCommLinkError,
       "p2mpTrapTxPower": p2mpTrapTxPower,
       "p2mpTrapRfStatusChange": p2mpTrapRfStatusChange,
       "p2mpTrapHeIfRxOsc": p2mpTrapHeIfRxOsc,
       "p2mpTrapHeIfTxOsc": p2mpTrapHeIfTxOsc,
       "p2mpTrapHeIfExtRefOsc": p2mpTrapHeIfExtRefOsc}
)
