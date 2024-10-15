# SNMP MIB module (BSUWIRELESSIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUWIRELESSIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:44 2024
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aniBsuWirelessIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuWirelessPortTable_Object = MibTable
aniBsuWirelessPortTable = _AniBsuWirelessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aniBsuWirelessPortTable.setStatus("current")
_AniBsuWirelessPortEntry_Object = MibTableRow
aniBsuWirelessPortEntry = _AniBsuWirelessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1)
)
aniBsuWirelessPortEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuWirelessPortEntry.setStatus("current")


class _AniBsuWirelessPort_Type(Integer32):
    """Custom type aniBsuWirelessPort based on Integer32"""
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
        *(("wireless-port1", 1),
          ("wireless-port2", 2),
          ("wireless-port3", 3),
          ("wireless-port4", 4),
          ("wireless-port5", 5),
          ("wireless-port6", 6))
    )


_AniBsuWirelessPort_Type.__name__ = "Integer32"
_AniBsuWirelessPort_Object = MibTableColumn
aniBsuWirelessPort = _AniBsuWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1, 1),
    _AniBsuWirelessPort_Type()
)
aniBsuWirelessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPort.setStatus("current")
_AniBsuPortMacAddr_Type = MacAddress
_AniBsuPortMacAddr_Object = MibTableColumn
aniBsuPortMacAddr = _AniBsuPortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1, 2),
    _AniBsuPortMacAddr_Type()
)
aniBsuPortMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuPortMacAddr.setStatus("current")


class _AniBsuPortState_Type(Integer32):
    """Custom type aniBsuPortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("configured-no-radio-detected", 5),
          ("disabled", 9),
          ("initial", 2),
          ("operational-radio", 6),
          ("resetting", 8),
          ("starting", 4),
          ("stopped", 7),
          ("unavailable", 1),
          ("unconfig", 3))
    )


_AniBsuPortState_Type.__name__ = "Integer32"
_AniBsuPortState_Object = MibTableColumn
aniBsuPortState = _AniBsuPortState_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1, 3),
    _AniBsuPortState_Type()
)
aniBsuPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuPortState.setStatus("current")
_AniBsuPortReset_Type = TruthValue
_AniBsuPortReset_Object = MibTableColumn
aniBsuPortReset = _AniBsuPortReset_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1, 4),
    _AniBsuPortReset_Type()
)
aniBsuPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuPortReset.setStatus("current")


class _AniBsuPortFlag_Type(Integer32):
    """Custom type aniBsuPortFlag based on Integer32"""
    defaultValue = 1

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


_AniBsuPortFlag_Type.__name__ = "Integer32"
_AniBsuPortFlag_Object = MibTableColumn
aniBsuPortFlag = _AniBsuPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 1, 1, 5),
    _AniBsuPortFlag_Type()
)
aniBsuPortFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuPortFlag.setStatus("current")
_AniBsuChannelTable_Object = MibTable
aniBsuChannelTable = _AniBsuChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4)
)
if mibBuilder.loadTexts:
    aniBsuChannelTable.setStatus("current")
_AniBsuChannelEntry_Object = MibTableRow
aniBsuChannelEntry = _AniBsuChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1)
)
aniBsuChannelEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuChannelEntry.setStatus("current")
_AniBsuChannelFrequency_Type = DisplayString
_AniBsuChannelFrequency_Object = MibTableColumn
aniBsuChannelFrequency = _AniBsuChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 2),
    _AniBsuChannelFrequency_Type()
)
aniBsuChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuChannelFrequency.setUnits("MHz")


class _AniBsuFrequencyBand_Type(Integer32):
    """Custom type aniBsuFrequencyBand based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("etsi-3-5GHz-100", 8),
          ("etsi-3-5GHz-50", 7),
          ("fdd-3-5GHz", 11),
          ("general-2-6GHz", 5),
          ("general-3-5GHz", 6),
          ("general-5-3GHz", 12),
          ("general-5-8GHz", 3),
          ("ism-5-8GHz", 10),
          ("mmds-2-6GHz", 4),
          ("unii-5-3GHz", 1),
          ("unii-5-8GHz", 2))
    )


_AniBsuFrequencyBand_Type.__name__ = "Integer32"
_AniBsuFrequencyBand_Object = MibTableColumn
aniBsuFrequencyBand = _AniBsuFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 3),
    _AniBsuFrequencyBand_Type()
)
aniBsuFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuFrequencyBand.setStatus("current")
_AniBsuChannelWidth_Type = DisplayString
_AniBsuChannelWidth_Object = MibTableColumn
aniBsuChannelWidth = _AniBsuChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 4),
    _AniBsuChannelWidth_Type()
)
aniBsuChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuChannelWidth.setStatus("current")
_AniBsuNumServFlowsPerSu_Type = Integer32
_AniBsuNumServFlowsPerSu_Object = MibTableColumn
aniBsuNumServFlowsPerSu = _AniBsuNumServFlowsPerSu_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 6),
    _AniBsuNumServFlowsPerSu_Type()
)
aniBsuNumServFlowsPerSu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuNumServFlowsPerSu.setStatus("current")
_AniBsuNumSusSupported_Type = Integer32
_AniBsuNumSusSupported_Object = MibTableColumn
aniBsuNumSusSupported = _AniBsuNumSusSupported_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 7),
    _AniBsuNumSusSupported_Type()
)
aniBsuNumSusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuNumSusSupported.setStatus("current")
_AniBsuSuRadioRegPowerLimit_Type = Integer32
_AniBsuSuRadioRegPowerLimit_Object = MibTableColumn
aniBsuSuRadioRegPowerLimit = _AniBsuSuRadioRegPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 9),
    _AniBsuSuRadioRegPowerLimit_Type()
)
aniBsuSuRadioRegPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuRadioRegPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuSuRadioRegPowerLimit.setUnits("dBm")
_AniBsuTargetFrequency_Type = DisplayString
_AniBsuTargetFrequency_Object = MibTableColumn
aniBsuTargetFrequency = _AniBsuTargetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 4, 1, 10),
    _AniBsuTargetFrequency_Type()
)
aniBsuTargetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuTargetFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuTargetFrequency.setUnits("MHz")
_AniBsuQosLinkTable_Object = MibTable
aniBsuQosLinkTable = _AniBsuQosLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 6)
)
if mibBuilder.loadTexts:
    aniBsuQosLinkTable.setStatus("current")
_AniBsuQosLinkEntry_Object = MibTableRow
aniBsuQosLinkEntry = _AniBsuQosLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 6, 1)
)
aniBsuQosLinkEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuQosLinkEntry.setStatus("current")
_AniBsuBEBandwidth_Type = Integer32
_AniBsuBEBandwidth_Object = MibTableColumn
aniBsuBEBandwidth = _AniBsuBEBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 6, 1, 1),
    _AniBsuBEBandwidth_Type()
)
aniBsuBEBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuBEBandwidth.setStatus("current")
_AniBsuCIRBandwidth_Type = Integer32
_AniBsuCIRBandwidth_Object = MibTableColumn
aniBsuCIRBandwidth = _AniBsuCIRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 6, 1, 2),
    _AniBsuCIRBandwidth_Type()
)
aniBsuCIRBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuCIRBandwidth.setStatus("current")
_AniBsuCBRBandwidth_Type = Integer32
_AniBsuCBRBandwidth_Object = MibTableColumn
aniBsuCBRBandwidth = _AniBsuCBRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 6, 1, 3),
    _AniBsuCBRBandwidth_Type()
)
aniBsuCBRBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuCBRBandwidth.setStatus("current")
_AniBsuPowerControlTable_Object = MibTable
aniBsuPowerControlTable = _AniBsuPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 7)
)
if mibBuilder.loadTexts:
    aniBsuPowerControlTable.setStatus("current")
_AniBsuPowerControlEntry_Object = MibTableRow
aniBsuPowerControlEntry = _AniBsuPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 7, 1)
)
aniBsuPowerControlEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuPowerControlEntry.setStatus("current")


class _AniBsuReceivePower_Type(Integer32):
    """Custom type aniBsuReceivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_AniBsuReceivePower_Type.__name__ = "Integer32"
_AniBsuReceivePower_Object = MibTableColumn
aniBsuReceivePower = _AniBsuReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 7, 1, 2),
    _AniBsuReceivePower_Type()
)
aniBsuReceivePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuReceivePower.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuReceivePower.setUnits("dBm")
_AniBsuWssRadioRegPowerLimit_Type = Integer32
_AniBsuWssRadioRegPowerLimit_Object = MibTableColumn
aniBsuWssRadioRegPowerLimit = _AniBsuWssRadioRegPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 7, 1, 3),
    _AniBsuWssRadioRegPowerLimit_Type()
)
aniBsuWssRadioRegPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWssRadioRegPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWssRadioRegPowerLimit.setUnits("dBm")
_AniBsuAntennaTable_Object = MibTable
aniBsuAntennaTable = _AniBsuAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 8)
)
if mibBuilder.loadTexts:
    aniBsuAntennaTable.setStatus("current")
_AniBsuAntennaEntry_Object = MibTableRow
aniBsuAntennaEntry = _AniBsuAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 8, 1)
)
aniBsuAntennaEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuAntennaEntry.setStatus("current")


class _AniBsuAntennaDiversityFlag_Type(Integer32):
    """Custom type aniBsuAntennaDiversityFlag based on Integer32"""
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


_AniBsuAntennaDiversityFlag_Type.__name__ = "Integer32"
_AniBsuAntennaDiversityFlag_Object = MibTableColumn
aniBsuAntennaDiversityFlag = _AniBsuAntennaDiversityFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 8, 1, 1),
    _AniBsuAntennaDiversityFlag_Type()
)
aniBsuAntennaDiversityFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuAntennaDiversityFlag.setStatus("current")


class _AniBsuAntennaDiversityMode_Type(Integer32):
    """Custom type aniBsuAntennaDiversityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync-based", 1),
          ("training-seq-based", 2))
    )


_AniBsuAntennaDiversityMode_Type.__name__ = "Integer32"
_AniBsuAntennaDiversityMode_Object = MibTableColumn
aniBsuAntennaDiversityMode = _AniBsuAntennaDiversityMode_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 8, 1, 2),
    _AniBsuAntennaDiversityMode_Type()
)
aniBsuAntennaDiversityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuAntennaDiversityMode.setStatus("current")


class _AniBsuBcastAntennaPolarization_Type(Integer32):
    """Custom type aniBsuBcastAntennaPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("horizontal-and-vertical", 3),
          ("vertical", 2))
    )


_AniBsuBcastAntennaPolarization_Type.__name__ = "Integer32"
_AniBsuBcastAntennaPolarization_Object = MibTableColumn
aniBsuBcastAntennaPolarization = _AniBsuBcastAntennaPolarization_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 8, 1, 4),
    _AniBsuBcastAntennaPolarization_Type()
)
aniBsuBcastAntennaPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuBcastAntennaPolarization.setStatus("current")
_AniBsuSectorTable_Object = MibTable
aniBsuSectorTable = _AniBsuSectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 9)
)
if mibBuilder.loadTexts:
    aniBsuSectorTable.setStatus("current")
_AniBsuSectorEntry_Object = MibTableRow
aniBsuSectorEntry = _AniBsuSectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 9, 1)
)
aniBsuSectorEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuSectorEntry.setStatus("current")


class _AniBsuSectorName_Type(DisplayString):
    """Custom type aniBsuSectorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniBsuSectorName_Type.__name__ = "DisplayString"
_AniBsuSectorName_Object = MibTableColumn
aniBsuSectorName = _AniBsuSectorName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 9, 1, 2),
    _AniBsuSectorName_Type()
)
aniBsuSectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSectorName.setStatus("current")
_AniBsuWirelessPtPConfGroup_ObjectIdentity = ObjectIdentity
aniBsuWirelessPtPConfGroup = _AniBsuWirelessPtPConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10)
)


class _AniBsuWirelessPtPConfFrequencyBand_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfFrequencyBand based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("etsi-3-5GHz-100", 8),
          ("etsi-3-5GHz-50", 7),
          ("general-2-6GHz", 5),
          ("general-3-5GHz", 6),
          ("general-5-8GHz", 3),
          ("ism-5-8GHz", 10),
          ("mmds-2-6GHz", 4),
          ("unii-5-3GHz", 1),
          ("unii-5-8GHz", 2))
    )


_AniBsuWirelessPtPConfFrequencyBand_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfFrequencyBand_Object = MibScalar
aniBsuWirelessPtPConfFrequencyBand = _AniBsuWirelessPtPConfFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 1),
    _AniBsuWirelessPtPConfFrequencyBand_Type()
)
aniBsuWirelessPtPConfFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfFrequencyBand.setStatus("current")


class _AniBsuWirelessPtPConfChannelWidth_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2000,
              3000,
              3500,
              4000,
              5000,
              6000,
              7000)
        )
    )
    namedValues = NamedValues(
        *(("width-2", 2000),
          ("width-3", 3000),
          ("width-3-5", 3500),
          ("width-4", 4000),
          ("width-5", 5000),
          ("width-6", 6000),
          ("width-7", 7000))
    )


_AniBsuWirelessPtPConfChannelWidth_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfChannelWidth_Object = MibScalar
aniBsuWirelessPtPConfChannelWidth = _AniBsuWirelessPtPConfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 2),
    _AniBsuWirelessPtPConfChannelWidth_Type()
)
aniBsuWirelessPtPConfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfChannelWidth.setStatus("current")


class _AniBsuWirelessPtPConfTDDFrameSize_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfTDDFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-latency", 1),
          ("normal-mode", 2))
    )


_AniBsuWirelessPtPConfTDDFrameSize_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfTDDFrameSize_Object = MibScalar
aniBsuWirelessPtPConfTDDFrameSize = _AniBsuWirelessPtPConfTDDFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 3),
    _AniBsuWirelessPtPConfTDDFrameSize_Type()
)
aniBsuWirelessPtPConfTDDFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfTDDFrameSize.setStatus("current")


class _AniBsuWirelessPtPConfCellRadius_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfCellRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10000,
              20000,
              30000,
              40000,
              50000,
              60000,
              70000,
              80000,
              90000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("radius100km", 100000),
          ("radius10km", 10000),
          ("radius20km", 20000),
          ("radius30km", 30000),
          ("radius40km", 40000),
          ("radius50km", 50000),
          ("radius60km", 60000),
          ("radius70km", 70000),
          ("radius80km", 80000),
          ("radius90km", 90000))
    )


_AniBsuWirelessPtPConfCellRadius_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfCellRadius_Object = MibScalar
aniBsuWirelessPtPConfCellRadius = _AniBsuWirelessPtPConfCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 4),
    _AniBsuWirelessPtPConfCellRadius_Type()
)
aniBsuWirelessPtPConfCellRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfCellRadius.setStatus("current")


class _AniBsuWirelessPtPConfDSUSRatio_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfDSUSRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              40,
              50,
              60,
              70)
        )
    )
    namedValues = NamedValues(
        *(("ds30-us70", 30),
          ("ds40-us60", 40),
          ("ds50-us50", 50),
          ("ds60-us40", 60),
          ("ds70-us30", 70))
    )


_AniBsuWirelessPtPConfDSUSRatio_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfDSUSRatio_Object = MibScalar
aniBsuWirelessPtPConfDSUSRatio = _AniBsuWirelessPtPConfDSUSRatio_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 5),
    _AniBsuWirelessPtPConfDSUSRatio_Type()
)
aniBsuWirelessPtPConfDSUSRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfDSUSRatio.setStatus("current")


class _AniBsuWirelessPtPConfPolarization_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("vertical", 2)
    )


_AniBsuWirelessPtPConfPolarization_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfPolarization_Object = MibScalar
aniBsuWirelessPtPConfPolarization = _AniBsuWirelessPtPConfPolarization_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 6),
    _AniBsuWirelessPtPConfPolarization_Type()
)
aniBsuWirelessPtPConfPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfPolarization.setStatus("current")
_AniBsuWirelessPtPConfTargetFrequency_Type = DisplayString
_AniBsuWirelessPtPConfTargetFrequency_Object = MibScalar
aniBsuWirelessPtPConfTargetFrequency = _AniBsuWirelessPtPConfTargetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 7),
    _AniBsuWirelessPtPConfTargetFrequency_Type()
)
aniBsuWirelessPtPConfTargetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfTargetFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfTargetFrequency.setUnits("MHz")
_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Type = Integer32
_AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Object = MibScalar
aniBsuWirelessPtPConfBsuRadioRegPowerLimit = _AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 8),
    _AniBsuWirelessPtPConfBsuRadioRegPowerLimit_Type()
)
aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfBsuRadioRegPowerLimit.setUnits("dBm")
_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Type = Integer32
_AniBsuWirelessPtPConfSuRadioRegPowerLimit_Object = MibScalar
aniBsuWirelessPtPConfSuRadioRegPowerLimit = _AniBsuWirelessPtPConfSuRadioRegPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 9),
    _AniBsuWirelessPtPConfSuRadioRegPowerLimit_Type()
)
aniBsuWirelessPtPConfSuRadioRegPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfSuRadioRegPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfSuRadioRegPowerLimit.setUnits("dBm")
_AniBsuWirelessPtPConfModify_Type = TruthValue
_AniBsuWirelessPtPConfModify_Object = MibScalar
aniBsuWirelessPtPConfModify = _AniBsuWirelessPtPConfModify_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 10),
    _AniBsuWirelessPtPConfModify_Type()
)
aniBsuWirelessPtPConfModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfModify.setStatus("current")


class _AniBsuWirelessPtPConfBsuId_Type(DisplayString):
    """Custom type aniBsuWirelessPtPConfBsuId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AniBsuWirelessPtPConfBsuId_Type.__name__ = "DisplayString"
_AniBsuWirelessPtPConfBsuId_Object = MibScalar
aniBsuWirelessPtPConfBsuId = _AniBsuWirelessPtPConfBsuId_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 11),
    _AniBsuWirelessPtPConfBsuId_Type()
)
aniBsuWirelessPtPConfBsuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfBsuId.setStatus("current")
_AniBsuWirelessPtPConfVerifyAllSu_Type = DisplayString
_AniBsuWirelessPtPConfVerifyAllSu_Object = MibScalar
aniBsuWirelessPtPConfVerifyAllSu = _AniBsuWirelessPtPConfVerifyAllSu_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 12),
    _AniBsuWirelessPtPConfVerifyAllSu_Type()
)
aniBsuWirelessPtPConfVerifyAllSu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfVerifyAllSu.setStatus("current")
_AniBsuWirelessPtPConfSwitchToFrequency_Type = DisplayString
_AniBsuWirelessPtPConfSwitchToFrequency_Object = MibScalar
aniBsuWirelessPtPConfSwitchToFrequency = _AniBsuWirelessPtPConfSwitchToFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 13),
    _AniBsuWirelessPtPConfSwitchToFrequency_Type()
)
aniBsuWirelessPtPConfSwitchToFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfSwitchToFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfSwitchToFrequency.setUnits("MHz")


class _AniBsuWirelessPtPConfSuAFSTimeout_Type(Integer32):
    """Custom type aniBsuWirelessPtPConfSuAFSTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AniBsuWirelessPtPConfSuAFSTimeout_Type.__name__ = "Integer32"
_AniBsuWirelessPtPConfSuAFSTimeout_Object = MibScalar
aniBsuWirelessPtPConfSuAFSTimeout = _AniBsuWirelessPtPConfSuAFSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 10, 14),
    _AniBsuWirelessPtPConfSuAFSTimeout_Type()
)
aniBsuWirelessPtPConfSuAFSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPConfSuAFSTimeout.setStatus("current")
_AniBsuWirelessPtPStatusGroup_ObjectIdentity = ObjectIdentity
aniBsuWirelessPtPStatusGroup = _AniBsuWirelessPtPStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 11)
)
_AniBsuWirelessPtPStatusMaxDSAvailBW_Type = DisplayString
_AniBsuWirelessPtPStatusMaxDSAvailBW_Object = MibScalar
aniBsuWirelessPtPStatusMaxDSAvailBW = _AniBsuWirelessPtPStatusMaxDSAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 11, 1),
    _AniBsuWirelessPtPStatusMaxDSAvailBW_Type()
)
aniBsuWirelessPtPStatusMaxDSAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPStatusMaxDSAvailBW.setStatus("current")
_AniBsuWirelessPtPStatusMaxUSAvailBW_Type = DisplayString
_AniBsuWirelessPtPStatusMaxUSAvailBW_Object = MibScalar
aniBsuWirelessPtPStatusMaxUSAvailBW = _AniBsuWirelessPtPStatusMaxUSAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 11, 2),
    _AniBsuWirelessPtPStatusMaxUSAvailBW_Type()
)
aniBsuWirelessPtPStatusMaxUSAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPStatusMaxUSAvailBW.setStatus("current")


class _AniBsuWirelessPtPStatusTDDFrameSize_Type(Integer32):
    """Custom type aniBsuWirelessPtPStatusTDDFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-latency", 1),
          ("normal-mode", 2))
    )


_AniBsuWirelessPtPStatusTDDFrameSize_Type.__name__ = "Integer32"
_AniBsuWirelessPtPStatusTDDFrameSize_Object = MibScalar
aniBsuWirelessPtPStatusTDDFrameSize = _AniBsuWirelessPtPStatusTDDFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 11, 3),
    _AniBsuWirelessPtPStatusTDDFrameSize_Type()
)
aniBsuWirelessPtPStatusTDDFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessPtPStatusTDDFrameSize.setStatus("current")
_AniBsuWirelessFreqAdminTable_Object = MibTable
aniBsuWirelessFreqAdminTable = _AniBsuWirelessFreqAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 12)
)
if mibBuilder.loadTexts:
    aniBsuWirelessFreqAdminTable.setStatus("current")
_AniBsuWirelessFreqAdminEntry_Object = MibTableRow
aniBsuWirelessFreqAdminEntry = _AniBsuWirelessFreqAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 12, 1)
)
aniBsuWirelessFreqAdminEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessFreqAdminIndex"),
)
if mibBuilder.loadTexts:
    aniBsuWirelessFreqAdminEntry.setStatus("current")
_AniBsuWirelessFreqAdminIndex_Type = Integer32
_AniBsuWirelessFreqAdminIndex_Object = MibTableColumn
aniBsuWirelessFreqAdminIndex = _AniBsuWirelessFreqAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 12, 1, 1),
    _AniBsuWirelessFreqAdminIndex_Type()
)
aniBsuWirelessFreqAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqAdminIndex.setStatus("current")
_AniBsuWirelessFreqAdminFreqValue_Type = DisplayString
_AniBsuWirelessFreqAdminFreqValue_Object = MibTableColumn
aniBsuWirelessFreqAdminFreqValue = _AniBsuWirelessFreqAdminFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 12, 1, 2),
    _AniBsuWirelessFreqAdminFreqValue_Type()
)
aniBsuWirelessFreqAdminFreqValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqAdminFreqValue.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqAdminFreqValue.setUnits("MHz")
_AniBsuWirelessFreqOperTable_Object = MibTable
aniBsuWirelessFreqOperTable = _AniBsuWirelessFreqOperTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 13)
)
if mibBuilder.loadTexts:
    aniBsuWirelessFreqOperTable.setStatus("current")
_AniBsuWirelessFreqOperEntry_Object = MibTableRow
aniBsuWirelessFreqOperEntry = _AniBsuWirelessFreqOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 13, 1)
)
aniBsuWirelessFreqOperEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessFreqOperIndex"),
)
if mibBuilder.loadTexts:
    aniBsuWirelessFreqOperEntry.setStatus("current")
_AniBsuWirelessFreqOperIndex_Type = Integer32
_AniBsuWirelessFreqOperIndex_Object = MibTableColumn
aniBsuWirelessFreqOperIndex = _AniBsuWirelessFreqOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 13, 1, 1),
    _AniBsuWirelessFreqOperIndex_Type()
)
aniBsuWirelessFreqOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqOperIndex.setStatus("current")
_AniBsuWirelessFreqOperFreqValue_Type = DisplayString
_AniBsuWirelessFreqOperFreqValue_Object = MibTableColumn
aniBsuWirelessFreqOperFreqValue = _AniBsuWirelessFreqOperFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 13, 1, 2),
    _AniBsuWirelessFreqOperFreqValue_Type()
)
aniBsuWirelessFreqOperFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqOperFreqValue.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessFreqOperFreqValue.setUnits("MHz")
_AniBsuWirelessSysConfGroup_ObjectIdentity = ObjectIdentity
aniBsuWirelessSysConfGroup = _AniBsuWirelessSysConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14)
)


class _AniBsuWirelessSysConfBsuId_Type(DisplayString):
    """Custom type aniBsuWirelessSysConfBsuId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_AniBsuWirelessSysConfBsuId_Type.__name__ = "DisplayString"
_AniBsuWirelessSysConfBsuId_Object = MibScalar
aniBsuWirelessSysConfBsuId = _AniBsuWirelessSysConfBsuId_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14, 1),
    _AniBsuWirelessSysConfBsuId_Type()
)
aniBsuWirelessSysConfBsuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessSysConfBsuId.setStatus("current")
_AniBsuWirelessSysConfFrameSize_Type = Integer32
_AniBsuWirelessSysConfFrameSize_Object = MibScalar
aniBsuWirelessSysConfFrameSize = _AniBsuWirelessSysConfFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14, 2),
    _AniBsuWirelessSysConfFrameSize_Type()
)
aniBsuWirelessSysConfFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessSysConfFrameSize.setStatus("current")
_AniBsuWirelessSysConfFrameDownstreamSize_Type = Integer32
_AniBsuWirelessSysConfFrameDownstreamSize_Object = MibScalar
aniBsuWirelessSysConfFrameDownstreamSize = _AniBsuWirelessSysConfFrameDownstreamSize_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14, 3),
    _AniBsuWirelessSysConfFrameDownstreamSize_Type()
)
aniBsuWirelessSysConfFrameDownstreamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessSysConfFrameDownstreamSize.setStatus("current")
_AniBsuWirelessSysConfFrameUpstreamSize_Type = Integer32
_AniBsuWirelessSysConfFrameUpstreamSize_Object = MibScalar
aniBsuWirelessSysConfFrameUpstreamSize = _AniBsuWirelessSysConfFrameUpstreamSize_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14, 4),
    _AniBsuWirelessSysConfFrameUpstreamSize_Type()
)
aniBsuWirelessSysConfFrameUpstreamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessSysConfFrameUpstreamSize.setStatus("current")


class _AniBsuWirelessSysConfDSUSRatio_Type(Integer32):
    """Custom type aniBsuWirelessSysConfDSUSRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              40,
              50,
              60,
              70)
        )
    )
    namedValues = NamedValues(
        *(("ds30-us70", 30),
          ("ds40-us60", 40),
          ("ds50-us50", 50),
          ("ds60-us40", 60),
          ("ds70-us30", 70))
    )


_AniBsuWirelessSysConfDSUSRatio_Type.__name__ = "Integer32"
_AniBsuWirelessSysConfDSUSRatio_Object = MibScalar
aniBsuWirelessSysConfDSUSRatio = _AniBsuWirelessSysConfDSUSRatio_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 14, 5),
    _AniBsuWirelessSysConfDSUSRatio_Type()
)
aniBsuWirelessSysConfDSUSRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessSysConfDSUSRatio.setStatus("current")
_AniBsuWirelessIfConfTable_Object = MibTable
aniBsuWirelessIfConfTable = _AniBsuWirelessIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15)
)
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfTable.setStatus("current")
_AniBsuWirelessIfConfEntry_Object = MibTableRow
aniBsuWirelessIfConfEntry = _AniBsuWirelessIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15, 1)
)
aniBsuWirelessIfConfEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfEntry.setStatus("current")
_AniBsuWirelessIfConfTargetFrequency_Type = DisplayString
_AniBsuWirelessIfConfTargetFrequency_Object = MibTableColumn
aniBsuWirelessIfConfTargetFrequency = _AniBsuWirelessIfConfTargetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15, 1, 1),
    _AniBsuWirelessIfConfTargetFrequency_Type()
)
aniBsuWirelessIfConfTargetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfTargetFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfTargetFrequency.setUnits("MHz")
_AniBsuWirelessIfConfVerifyAllSu_Type = DisplayString
_AniBsuWirelessIfConfVerifyAllSu_Object = MibTableColumn
aniBsuWirelessIfConfVerifyAllSu = _AniBsuWirelessIfConfVerifyAllSu_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15, 1, 2),
    _AniBsuWirelessIfConfVerifyAllSu_Type()
)
aniBsuWirelessIfConfVerifyAllSu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfVerifyAllSu.setStatus("current")
_AniBsuWirelessIfConfSwitchToFrequency_Type = DisplayString
_AniBsuWirelessIfConfSwitchToFrequency_Object = MibTableColumn
aniBsuWirelessIfConfSwitchToFrequency = _AniBsuWirelessIfConfSwitchToFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15, 1, 3),
    _AniBsuWirelessIfConfSwitchToFrequency_Type()
)
aniBsuWirelessIfConfSwitchToFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfSwitchToFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfSwitchToFrequency.setUnits("MHz")
_AniBsuWirelessIfConfModify_Type = TruthValue
_AniBsuWirelessIfConfModify_Object = MibTableColumn
aniBsuWirelessIfConfModify = _AniBsuWirelessIfConfModify_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 15, 1, 50),
    _AniBsuWirelessIfConfModify_Type()
)
aniBsuWirelessIfConfModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessIfConfModify.setStatus("current")
_AniBsuWirelessAFSTable_Object = MibTable
aniBsuWirelessAFSTable = _AniBsuWirelessAFSTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16)
)
if mibBuilder.loadTexts:
    aniBsuWirelessAFSTable.setStatus("current")
_AniBsuWirelessAFSConfEntry_Object = MibTableRow
aniBsuWirelessAFSConfEntry = _AniBsuWirelessAFSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1)
)
aniBsuWirelessAFSConfEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuWirelessAFSConfEntry.setStatus("current")


class _AniBsuWirelessAFSFlag_Type(Integer32):
    """Custom type aniBsuWirelessAFSFlag based on Integer32"""
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


_AniBsuWirelessAFSFlag_Type.__name__ = "Integer32"
_AniBsuWirelessAFSFlag_Object = MibTableColumn
aniBsuWirelessAFSFlag = _AniBsuWirelessAFSFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1, 1),
    _AniBsuWirelessAFSFlag_Type()
)
aniBsuWirelessAFSFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessAFSFlag.setStatus("current")


class _AniBsuWirelessAFSMinSwitchDuration_Type(Integer32):
    """Custom type aniBsuWirelessAFSMinSwitchDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AniBsuWirelessAFSMinSwitchDuration_Type.__name__ = "Integer32"
_AniBsuWirelessAFSMinSwitchDuration_Object = MibTableColumn
aniBsuWirelessAFSMinSwitchDuration = _AniBsuWirelessAFSMinSwitchDuration_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1, 2),
    _AniBsuWirelessAFSMinSwitchDuration_Type()
)
aniBsuWirelessAFSMinSwitchDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessAFSMinSwitchDuration.setStatus("current")


class _AniBsuWirelessAFSMinNotificationDuration_Type(Integer32):
    """Custom type aniBsuWirelessAFSMinNotificationDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_AniBsuWirelessAFSMinNotificationDuration_Type.__name__ = "Integer32"
_AniBsuWirelessAFSMinNotificationDuration_Object = MibTableColumn
aniBsuWirelessAFSMinNotificationDuration = _AniBsuWirelessAFSMinNotificationDuration_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1, 3),
    _AniBsuWirelessAFSMinNotificationDuration_Type()
)
aniBsuWirelessAFSMinNotificationDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessAFSMinNotificationDuration.setStatus("current")


class _AniBsuWirelessAFSErrPercentage_Type(Integer32):
    """Custom type aniBsuWirelessAFSErrPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AniBsuWirelessAFSErrPercentage_Type.__name__ = "Integer32"
_AniBsuWirelessAFSErrPercentage_Object = MibTableColumn
aniBsuWirelessAFSErrPercentage = _AniBsuWirelessAFSErrPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1, 4),
    _AniBsuWirelessAFSErrPercentage_Type()
)
aniBsuWirelessAFSErrPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessAFSErrPercentage.setStatus("current")


class _AniBsuWirelessAFSMinSwitchBytes_Type(Integer32):
    """Custom type aniBsuWirelessAFSMinSwitchBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_AniBsuWirelessAFSMinSwitchBytes_Type.__name__ = "Integer32"
_AniBsuWirelessAFSMinSwitchBytes_Object = MibTableColumn
aniBsuWirelessAFSMinSwitchBytes = _AniBsuWirelessAFSMinSwitchBytes_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2, 16, 1, 5),
    _AniBsuWirelessAFSMinSwitchBytes_Type()
)
aniBsuWirelessAFSMinSwitchBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuWirelessAFSMinSwitchBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUWIRELESSIF-MIB",
    **{"aniBsuWirelessIf": aniBsuWirelessIf,
       "aniBsuWirelessPortTable": aniBsuWirelessPortTable,
       "aniBsuWirelessPortEntry": aniBsuWirelessPortEntry,
       "aniBsuWirelessPort": aniBsuWirelessPort,
       "aniBsuPortMacAddr": aniBsuPortMacAddr,
       "aniBsuPortState": aniBsuPortState,
       "aniBsuPortReset": aniBsuPortReset,
       "aniBsuPortFlag": aniBsuPortFlag,
       "aniBsuChannelTable": aniBsuChannelTable,
       "aniBsuChannelEntry": aniBsuChannelEntry,
       "aniBsuChannelFrequency": aniBsuChannelFrequency,
       "aniBsuFrequencyBand": aniBsuFrequencyBand,
       "aniBsuChannelWidth": aniBsuChannelWidth,
       "aniBsuNumServFlowsPerSu": aniBsuNumServFlowsPerSu,
       "aniBsuNumSusSupported": aniBsuNumSusSupported,
       "aniBsuSuRadioRegPowerLimit": aniBsuSuRadioRegPowerLimit,
       "aniBsuTargetFrequency": aniBsuTargetFrequency,
       "aniBsuQosLinkTable": aniBsuQosLinkTable,
       "aniBsuQosLinkEntry": aniBsuQosLinkEntry,
       "aniBsuBEBandwidth": aniBsuBEBandwidth,
       "aniBsuCIRBandwidth": aniBsuCIRBandwidth,
       "aniBsuCBRBandwidth": aniBsuCBRBandwidth,
       "aniBsuPowerControlTable": aniBsuPowerControlTable,
       "aniBsuPowerControlEntry": aniBsuPowerControlEntry,
       "aniBsuReceivePower": aniBsuReceivePower,
       "aniBsuWssRadioRegPowerLimit": aniBsuWssRadioRegPowerLimit,
       "aniBsuAntennaTable": aniBsuAntennaTable,
       "aniBsuAntennaEntry": aniBsuAntennaEntry,
       "aniBsuAntennaDiversityFlag": aniBsuAntennaDiversityFlag,
       "aniBsuAntennaDiversityMode": aniBsuAntennaDiversityMode,
       "aniBsuBcastAntennaPolarization": aniBsuBcastAntennaPolarization,
       "aniBsuSectorTable": aniBsuSectorTable,
       "aniBsuSectorEntry": aniBsuSectorEntry,
       "aniBsuSectorName": aniBsuSectorName,
       "aniBsuWirelessPtPConfGroup": aniBsuWirelessPtPConfGroup,
       "aniBsuWirelessPtPConfFrequencyBand": aniBsuWirelessPtPConfFrequencyBand,
       "aniBsuWirelessPtPConfChannelWidth": aniBsuWirelessPtPConfChannelWidth,
       "aniBsuWirelessPtPConfTDDFrameSize": aniBsuWirelessPtPConfTDDFrameSize,
       "aniBsuWirelessPtPConfCellRadius": aniBsuWirelessPtPConfCellRadius,
       "aniBsuWirelessPtPConfDSUSRatio": aniBsuWirelessPtPConfDSUSRatio,
       "aniBsuWirelessPtPConfPolarization": aniBsuWirelessPtPConfPolarization,
       "aniBsuWirelessPtPConfTargetFrequency": aniBsuWirelessPtPConfTargetFrequency,
       "aniBsuWirelessPtPConfBsuRadioRegPowerLimit": aniBsuWirelessPtPConfBsuRadioRegPowerLimit,
       "aniBsuWirelessPtPConfSuRadioRegPowerLimit": aniBsuWirelessPtPConfSuRadioRegPowerLimit,
       "aniBsuWirelessPtPConfModify": aniBsuWirelessPtPConfModify,
       "aniBsuWirelessPtPConfBsuId": aniBsuWirelessPtPConfBsuId,
       "aniBsuWirelessPtPConfVerifyAllSu": aniBsuWirelessPtPConfVerifyAllSu,
       "aniBsuWirelessPtPConfSwitchToFrequency": aniBsuWirelessPtPConfSwitchToFrequency,
       "aniBsuWirelessPtPConfSuAFSTimeout": aniBsuWirelessPtPConfSuAFSTimeout,
       "aniBsuWirelessPtPStatusGroup": aniBsuWirelessPtPStatusGroup,
       "aniBsuWirelessPtPStatusMaxDSAvailBW": aniBsuWirelessPtPStatusMaxDSAvailBW,
       "aniBsuWirelessPtPStatusMaxUSAvailBW": aniBsuWirelessPtPStatusMaxUSAvailBW,
       "aniBsuWirelessPtPStatusTDDFrameSize": aniBsuWirelessPtPStatusTDDFrameSize,
       "aniBsuWirelessFreqAdminTable": aniBsuWirelessFreqAdminTable,
       "aniBsuWirelessFreqAdminEntry": aniBsuWirelessFreqAdminEntry,
       "aniBsuWirelessFreqAdminIndex": aniBsuWirelessFreqAdminIndex,
       "aniBsuWirelessFreqAdminFreqValue": aniBsuWirelessFreqAdminFreqValue,
       "aniBsuWirelessFreqOperTable": aniBsuWirelessFreqOperTable,
       "aniBsuWirelessFreqOperEntry": aniBsuWirelessFreqOperEntry,
       "aniBsuWirelessFreqOperIndex": aniBsuWirelessFreqOperIndex,
       "aniBsuWirelessFreqOperFreqValue": aniBsuWirelessFreqOperFreqValue,
       "aniBsuWirelessSysConfGroup": aniBsuWirelessSysConfGroup,
       "aniBsuWirelessSysConfBsuId": aniBsuWirelessSysConfBsuId,
       "aniBsuWirelessSysConfFrameSize": aniBsuWirelessSysConfFrameSize,
       "aniBsuWirelessSysConfFrameDownstreamSize": aniBsuWirelessSysConfFrameDownstreamSize,
       "aniBsuWirelessSysConfFrameUpstreamSize": aniBsuWirelessSysConfFrameUpstreamSize,
       "aniBsuWirelessSysConfDSUSRatio": aniBsuWirelessSysConfDSUSRatio,
       "aniBsuWirelessIfConfTable": aniBsuWirelessIfConfTable,
       "aniBsuWirelessIfConfEntry": aniBsuWirelessIfConfEntry,
       "aniBsuWirelessIfConfTargetFrequency": aniBsuWirelessIfConfTargetFrequency,
       "aniBsuWirelessIfConfVerifyAllSu": aniBsuWirelessIfConfVerifyAllSu,
       "aniBsuWirelessIfConfSwitchToFrequency": aniBsuWirelessIfConfSwitchToFrequency,
       "aniBsuWirelessIfConfModify": aniBsuWirelessIfConfModify,
       "aniBsuWirelessAFSTable": aniBsuWirelessAFSTable,
       "aniBsuWirelessAFSConfEntry": aniBsuWirelessAFSConfEntry,
       "aniBsuWirelessAFSFlag": aniBsuWirelessAFSFlag,
       "aniBsuWirelessAFSMinSwitchDuration": aniBsuWirelessAFSMinSwitchDuration,
       "aniBsuWirelessAFSMinNotificationDuration": aniBsuWirelessAFSMinNotificationDuration,
       "aniBsuWirelessAFSErrPercentage": aniBsuWirelessAFSErrPercentage,
       "aniBsuWirelessAFSMinSwitchBytes": aniBsuWirelessAFSMinSwitchBytes}
)
