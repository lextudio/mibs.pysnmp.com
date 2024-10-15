# SNMP MIB module (ALVARION-DOT11-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-DOT11-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:36 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

breezeAccessVLMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1)
)
breezeAccessVLMib.setRevisions(
        ("1910-09-23 11:30",)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alvarion_ObjectIdentity = ObjectIdentity
alvarion = _Alvarion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1)
)
_BrzaccVLSysInfo_ObjectIdentity = ObjectIdentity
brzaccVLSysInfo = _BrzaccVLSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1)
)


class _BrzaccVLUnitHwVersion_Type(DisplayString):
    """Custom type brzaccVLUnitHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLUnitHwVersion_Type.__name__ = "DisplayString"
_BrzaccVLUnitHwVersion_Object = MibScalar
brzaccVLUnitHwVersion = _BrzaccVLUnitHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 1),
    _BrzaccVLUnitHwVersion_Type()
)
brzaccVLUnitHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnitHwVersion.setStatus("current")


class _BrzaccVLRunningSoftwareVersion_Type(DisplayString):
    """Custom type brzaccVLRunningSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLRunningSoftwareVersion_Type.__name__ = "DisplayString"
_BrzaccVLRunningSoftwareVersion_Object = MibScalar
brzaccVLRunningSoftwareVersion = _BrzaccVLRunningSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 2),
    _BrzaccVLRunningSoftwareVersion_Type()
)
brzaccVLRunningSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunningSoftwareVersion.setStatus("current")


class _BrzaccVLRunningFrom_Type(Integer32):
    """Custom type brzaccVLRunningFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainVersion", 1),
          ("shadowVersion", 2))
    )


_BrzaccVLRunningFrom_Type.__name__ = "Integer32"
_BrzaccVLRunningFrom_Object = MibScalar
brzaccVLRunningFrom = _BrzaccVLRunningFrom_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 3),
    _BrzaccVLRunningFrom_Type()
)
brzaccVLRunningFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunningFrom.setStatus("current")


class _BrzaccVLMainVersionNumber_Type(DisplayString):
    """Custom type brzaccVLMainVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLMainVersionNumber_Type.__name__ = "DisplayString"
_BrzaccVLMainVersionNumber_Object = MibScalar
brzaccVLMainVersionNumber = _BrzaccVLMainVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 4),
    _BrzaccVLMainVersionNumber_Type()
)
brzaccVLMainVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMainVersionNumber.setStatus("current")


class _BrzaccVLMainVersionFileName_Type(DisplayString):
    """Custom type brzaccVLMainVersionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLMainVersionFileName_Type.__name__ = "DisplayString"
_BrzaccVLMainVersionFileName_Object = MibScalar
brzaccVLMainVersionFileName = _BrzaccVLMainVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 5),
    _BrzaccVLMainVersionFileName_Type()
)
brzaccVLMainVersionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMainVersionFileName.setStatus("current")


class _BrzaccVLShadowVersionNumber_Type(DisplayString):
    """Custom type brzaccVLShadowVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLShadowVersionNumber_Type.__name__ = "DisplayString"
_BrzaccVLShadowVersionNumber_Object = MibScalar
brzaccVLShadowVersionNumber = _BrzaccVLShadowVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 6),
    _BrzaccVLShadowVersionNumber_Type()
)
brzaccVLShadowVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLShadowVersionNumber.setStatus("current")


class _BrzaccVLShadowVersionFileName_Type(DisplayString):
    """Custom type brzaccVLShadowVersionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLShadowVersionFileName_Type.__name__ = "DisplayString"
_BrzaccVLShadowVersionFileName_Object = MibScalar
brzaccVLShadowVersionFileName = _BrzaccVLShadowVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 7),
    _BrzaccVLShadowVersionFileName_Type()
)
brzaccVLShadowVersionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLShadowVersionFileName.setStatus("current")
_BrzaccVLUnitMacAddress_Type = MacAddress
_BrzaccVLUnitMacAddress_Object = MibScalar
brzaccVLUnitMacAddress = _BrzaccVLUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 8),
    _BrzaccVLUnitMacAddress_Type()
)
brzaccVLUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnitMacAddress.setStatus("current")


class _BrzaccVLUnitType_Type(Integer32):
    """Custom type brzaccVLUnitType based on Integer32"""
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
        *(("au", 32),
          ("au-EZ", 22),
          ("auBS", 1),
          ("auBS4900", 16),
          ("auSA", 2),
          ("auSA4900", 17),
          ("ausBS", 14),
          ("ausSA", 15),
          ("bu-B10", 25),
          ("bu-B100", 19),
          ("bu-B14", 6),
          ("bu-B28", 7),
          ("rb-B10", 26),
          ("rb-B100", 20),
          ("rb-B14", 8),
          ("rb-B28", 9),
          ("su", 33),
          ("su-1-BD", 28),
          ("su-12-L", 31),
          ("su-24-BD", 5),
          ("su-3-1D", 12),
          ("su-3-4D", 13),
          ("su-3-L", 29),
          ("su-54-BD", 11),
          ("su-6-1D", 3),
          ("su-6-BD", 4),
          ("su-6-L", 30),
          ("su-8-BD", 27),
          ("su-BD", 10),
          ("su-EZ", 23),
          ("su-I", 21),
          ("su-V", 24),
          ("su4900", 18))
    )


_BrzaccVLUnitType_Type.__name__ = "Integer32"
_BrzaccVLUnitType_Object = MibScalar
brzaccVLUnitType = _BrzaccVLUnitType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 9),
    _BrzaccVLUnitType_Type()
)
brzaccVLUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnitType.setStatus("current")
_BrzaccVLAssociatedAU_Type = MacAddress
_BrzaccVLAssociatedAU_Object = MibScalar
brzaccVLAssociatedAU = _BrzaccVLAssociatedAU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 10),
    _BrzaccVLAssociatedAU_Type()
)
brzaccVLAssociatedAU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAssociatedAU.setStatus("current")
_BrzaccVLNumOfAssociationsSinceLastReset_Type = Integer32
_BrzaccVLNumOfAssociationsSinceLastReset_Object = MibScalar
brzaccVLNumOfAssociationsSinceLastReset = _BrzaccVLNumOfAssociationsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 11),
    _BrzaccVLNumOfAssociationsSinceLastReset_Type()
)
brzaccVLNumOfAssociationsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNumOfAssociationsSinceLastReset.setStatus("current")
_BrzaccVLCurrentNumOfAssociations_Type = Integer32
_BrzaccVLCurrentNumOfAssociations_Object = MibScalar
brzaccVLCurrentNumOfAssociations = _BrzaccVLCurrentNumOfAssociations_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 13),
    _BrzaccVLCurrentNumOfAssociations_Type()
)
brzaccVLCurrentNumOfAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentNumOfAssociations.setStatus("current")


class _BrzaccVLUnitBootVersion_Type(DisplayString):
    """Custom type brzaccVLUnitBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLUnitBootVersion_Type.__name__ = "DisplayString"
_BrzaccVLUnitBootVersion_Object = MibScalar
brzaccVLUnitBootVersion = _BrzaccVLUnitBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 14),
    _BrzaccVLUnitBootVersion_Type()
)
brzaccVLUnitBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnitBootVersion.setStatus("current")


class _BrzaccVLRadioBand_Type(Integer32):
    """Custom type brzaccVLRadioBand based on Integer32"""
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
        *(("band-2-4GHz", 5),
          ("band-4-9GHz", 3),
          ("band-4-9GHzJapan", 7),
          ("band-5-2GHz", 4),
          ("band-5-3GHz", 6),
          ("band-5-4GHz", 2),
          ("band-5-8GHz", 1),
          ("band-900MHz", 8))
    )


_BrzaccVLRadioBand_Type.__name__ = "Integer32"
_BrzaccVLRadioBand_Object = MibScalar
brzaccVLRadioBand = _BrzaccVLRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 15),
    _BrzaccVLRadioBand_Type()
)
brzaccVLRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRadioBand.setStatus("current")


class _BrzaccVLCurrentEthernetPortState_Type(Integer32):
    """Custom type brzaccVLCurrentEthernetPortState based on Integer32"""
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
        *(("fullDuplexAnd100Mbps", 4),
          ("fullDuplexAnd10Mbps", 2),
          ("halfDuplexAnd100Mbps", 3),
          ("halfDuplexAnd10Mbps", 1),
          ("linkDown", 5))
    )


_BrzaccVLCurrentEthernetPortState_Type.__name__ = "Integer32"
_BrzaccVLCurrentEthernetPortState_Object = MibScalar
brzaccVLCurrentEthernetPortState = _BrzaccVLCurrentEthernetPortState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 16),
    _BrzaccVLCurrentEthernetPortState_Type()
)
brzaccVLCurrentEthernetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentEthernetPortState.setStatus("current")


class _BrzaccVLTimeSinceLastReset_Type(DisplayString):
    """Custom type brzaccVLTimeSinceLastReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLTimeSinceLastReset_Type.__name__ = "DisplayString"
_BrzaccVLTimeSinceLastReset_Object = MibScalar
brzaccVLTimeSinceLastReset = _BrzaccVLTimeSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 17),
    _BrzaccVLTimeSinceLastReset_Type()
)
brzaccVLTimeSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTimeSinceLastReset.setStatus("current")
_BrzaccVLCountryDependentParameters_ObjectIdentity = ObjectIdentity
brzaccVLCountryDependentParameters = _BrzaccVLCountryDependentParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18)
)


class _BrzaccVLCountryCode_Type(DisplayString):
    """Custom type brzaccVLCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLCountryCode_Type.__name__ = "DisplayString"
_BrzaccVLCountryCode_Object = MibScalar
brzaccVLCountryCode = _BrzaccVLCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 1),
    _BrzaccVLCountryCode_Type()
)
brzaccVLCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCountryCode.setStatus("current")
_BrzaccVLCountryDependentParamsTable_Object = MibTable
brzaccVLCountryDependentParamsTable = _BrzaccVLCountryDependentParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    brzaccVLCountryDependentParamsTable.setStatus("current")
_BrzaccVLCountryDependentParameterEntry_Object = MibTableRow
brzaccVLCountryDependentParameterEntry = _BrzaccVLCountryDependentParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1)
)
brzaccVLCountryDependentParameterEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLCountryDependentParameterTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLCountryDependentParameterEntry.setStatus("current")


class _BrzaccVLCountryDependentParameterTableIdx_Type(Integer32):
    """Custom type brzaccVLCountryDependentParameterTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BrzaccVLCountryDependentParameterTableIdx_Type.__name__ = "Integer32"
_BrzaccVLCountryDependentParameterTableIdx_Object = MibTableColumn
brzaccVLCountryDependentParameterTableIdx = _BrzaccVLCountryDependentParameterTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 1),
    _BrzaccVLCountryDependentParameterTableIdx_Type()
)
brzaccVLCountryDependentParameterTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCountryDependentParameterTableIdx.setStatus("current")
_BrzaccVLCountryDependentParameterFrequencies_Type = DisplayString
_BrzaccVLCountryDependentParameterFrequencies_Object = MibTableColumn
brzaccVLCountryDependentParameterFrequencies = _BrzaccVLCountryDependentParameterFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 2),
    _BrzaccVLCountryDependentParameterFrequencies_Type()
)
brzaccVLCountryDependentParameterFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCountryDependentParameterFrequencies.setStatus("current")
_BrzaccVLAllowedBandwidth_Type = Integer32
_BrzaccVLAllowedBandwidth_Object = MibTableColumn
brzaccVLAllowedBandwidth = _BrzaccVLAllowedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 3),
    _BrzaccVLAllowedBandwidth_Type()
)
brzaccVLAllowedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAllowedBandwidth.setStatus("current")
_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Type = Integer32
_BrzaccVLRegulationMaxTxPowerAtAntennaPort_Object = MibTableColumn
brzaccVLRegulationMaxTxPowerAtAntennaPort = _BrzaccVLRegulationMaxTxPowerAtAntennaPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 4),
    _BrzaccVLRegulationMaxTxPowerAtAntennaPort_Type()
)
brzaccVLRegulationMaxTxPowerAtAntennaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRegulationMaxTxPowerAtAntennaPort.setStatus("current")
_BrzaccVLRegulationMaxEIRP_Type = Integer32
_BrzaccVLRegulationMaxEIRP_Object = MibTableColumn
brzaccVLRegulationMaxEIRP = _BrzaccVLRegulationMaxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 5),
    _BrzaccVLRegulationMaxEIRP_Type()
)
brzaccVLRegulationMaxEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRegulationMaxEIRP.setStatus("current")


class _BrzaccVLMinModulationLevel_Type(Integer32):
    """Custom type brzaccVLMinModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLMinModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLMinModulationLevel_Object = MibTableColumn
brzaccVLMinModulationLevel = _BrzaccVLMinModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 6),
    _BrzaccVLMinModulationLevel_Type()
)
brzaccVLMinModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMinModulationLevel.setStatus("current")


class _BrzaccVLMaxModulationLevel_Type(Integer32):
    """Custom type brzaccVLMaxModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLMaxModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLMaxModulationLevel_Object = MibTableColumn
brzaccVLMaxModulationLevel = _BrzaccVLMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 7),
    _BrzaccVLMaxModulationLevel_Type()
)
brzaccVLMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaxModulationLevel.setStatus("current")


class _BrzaccVLBurstModeSupport_Type(Integer32):
    """Custom type brzaccVLBurstModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLBurstModeSupport_Type.__name__ = "Integer32"
_BrzaccVLBurstModeSupport_Object = MibTableColumn
brzaccVLBurstModeSupport = _BrzaccVLBurstModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 8),
    _BrzaccVLBurstModeSupport_Type()
)
brzaccVLBurstModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLBurstModeSupport.setStatus("current")
_BrzaccVLMaximumBurstDuration_Type = Integer32
_BrzaccVLMaximumBurstDuration_Object = MibTableColumn
brzaccVLMaximumBurstDuration = _BrzaccVLMaximumBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 9),
    _BrzaccVLMaximumBurstDuration_Type()
)
brzaccVLMaximumBurstDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaximumBurstDuration.setStatus("current")


class _BrzaccVLDfsSupport_Type(Integer32):
    """Custom type brzaccVLDfsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLDfsSupport_Type.__name__ = "Integer32"
_BrzaccVLDfsSupport_Object = MibTableColumn
brzaccVLDfsSupport = _BrzaccVLDfsSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 10),
    _BrzaccVLDfsSupport_Type()
)
brzaccVLDfsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDfsSupport.setStatus("current")


class _BrzaccVLMinimumHwRevision_Type(Integer32):
    """Custom type brzaccVLMinimumHwRevision based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("hwRevisionF", 6),
          ("hwRevisionG", 7),
          ("na", 255))
    )


_BrzaccVLMinimumHwRevision_Type.__name__ = "Integer32"
_BrzaccVLMinimumHwRevision_Object = MibTableColumn
brzaccVLMinimumHwRevision = _BrzaccVLMinimumHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 11),
    _BrzaccVLMinimumHwRevision_Type()
)
brzaccVLMinimumHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMinimumHwRevision.setStatus("current")


class _BrzaccVLAuthenticationEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLAuthenticationEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLAuthenticationEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLAuthenticationEncryptionSupport_Object = MibScalar
brzaccVLAuthenticationEncryptionSupport = _BrzaccVLAuthenticationEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 3),
    _BrzaccVLAuthenticationEncryptionSupport_Type()
)
brzaccVLAuthenticationEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAuthenticationEncryptionSupport.setStatus("current")


class _BrzaccVLDataEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLDataEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLDataEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLDataEncryptionSupport_Object = MibScalar
brzaccVLDataEncryptionSupport = _BrzaccVLDataEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 4),
    _BrzaccVLDataEncryptionSupport_Type()
)
brzaccVLDataEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDataEncryptionSupport.setStatus("current")


class _BrzaccVLAESEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLAESEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLAESEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLAESEncryptionSupport_Object = MibScalar
brzaccVLAESEncryptionSupport = _BrzaccVLAESEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 5),
    _BrzaccVLAESEncryptionSupport_Type()
)
brzaccVLAESEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAESEncryptionSupport.setStatus("current")


class _BrzaccVLAntennaGainChange_Type(Integer32):
    """Custom type brzaccVLAntennaGainChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLAntennaGainChange_Type.__name__ = "Integer32"
_BrzaccVLAntennaGainChange_Object = MibScalar
brzaccVLAntennaGainChange = _BrzaccVLAntennaGainChange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 19),
    _BrzaccVLAntennaGainChange_Type()
)
brzaccVLAntennaGainChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAntennaGainChange.setStatus("current")


class _BrzaccVLAteTestResults_Type(Integer32):
    """Custom type brzaccVLAteTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("none", 0),
          ("pass", 1))
    )


_BrzaccVLAteTestResults_Type.__name__ = "Integer32"
_BrzaccVLAteTestResults_Object = MibScalar
brzaccVLAteTestResults = _BrzaccVLAteTestResults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 20),
    _BrzaccVLAteTestResults_Type()
)
brzaccVLAteTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAteTestResults.setStatus("current")


class _BrzaccVLSerialNumber_Type(DisplayString):
    """Custom type brzaccVLSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_BrzaccVLSerialNumber_Type.__name__ = "DisplayString"
_BrzaccVLSerialNumber_Object = MibScalar
brzaccVLSerialNumber = _BrzaccVLSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 21),
    _BrzaccVLSerialNumber_Type()
)
brzaccVLSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSerialNumber.setStatus("current")


class _BrzaccVLAUSSupportSU54_Type(Integer32):
    """Custom type brzaccVLAUSSupportSU54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("na", 255),
          ("true", 1))
    )


_BrzaccVLAUSSupportSU54_Type.__name__ = "Integer32"
_BrzaccVLAUSSupportSU54_Object = MibScalar
brzaccVLAUSSupportSU54 = _BrzaccVLAUSSupportSU54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 22),
    _BrzaccVLAUSSupportSU54_Type()
)
brzaccVLAUSSupportSU54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAUSSupportSU54.setStatus("current")
_BrzaccVLNumOfRejectionsSinceLastReset_Type = Integer32
_BrzaccVLNumOfRejectionsSinceLastReset_Object = MibScalar
brzaccVLNumOfRejectionsSinceLastReset = _BrzaccVLNumOfRejectionsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 23),
    _BrzaccVLNumOfRejectionsSinceLastReset_Type()
)
brzaccVLNumOfRejectionsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNumOfRejectionsSinceLastReset.setStatus("current")


class _BrzaccVLAUSSupportSU8_Type(Integer32):
    """Custom type brzaccVLAUSSupportSU8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("na", 255),
          ("true", 1))
    )


_BrzaccVLAUSSupportSU8_Type.__name__ = "Integer32"
_BrzaccVLAUSSupportSU8_Object = MibScalar
brzaccVLAUSSupportSU8 = _BrzaccVLAUSSupportSU8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 24),
    _BrzaccVLAUSSupportSU8_Type()
)
brzaccVLAUSSupportSU8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAUSSupportSU8.setStatus("current")
_BrzaccVLUnitControl_ObjectIdentity = ObjectIdentity
brzaccVLUnitControl = _BrzaccVLUnitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2)
)


class _BrzaccVLResetUnit_Type(Integer32):
    """Custom type brzaccVLResetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("resetSystemNow", 2))
    )


_BrzaccVLResetUnit_Type.__name__ = "Integer32"
_BrzaccVLResetUnit_Object = MibScalar
brzaccVLResetUnit = _BrzaccVLResetUnit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 1),
    _BrzaccVLResetUnit_Type()
)
brzaccVLResetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLResetUnit.setStatus("current")


class _BrzaccVLSetDefaults_Type(Integer32):
    """Custom type brzaccVLSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cancelCurrentPendingRequest", 5),
          ("completeFactory", 1),
          ("completeOperator", 3),
          ("noDefaultSettingRequested", 0),
          ("partialFactory", 2),
          ("partialOperator", 4))
    )


_BrzaccVLSetDefaults_Type.__name__ = "Integer32"
_BrzaccVLSetDefaults_Object = MibScalar
brzaccVLSetDefaults = _BrzaccVLSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 2),
    _BrzaccVLSetDefaults_Type()
)
brzaccVLSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSetDefaults.setStatus("current")


class _BrzaccVLUnitName_Type(DisplayString):
    """Custom type brzaccVLUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLUnitName_Type.__name__ = "DisplayString"
_BrzaccVLUnitName_Object = MibScalar
brzaccVLUnitName = _BrzaccVLUnitName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 3),
    _BrzaccVLUnitName_Type()
)
brzaccVLUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUnitName.setStatus("current")


class _BrzaccVLFlashMemoryControl_Type(Integer32):
    """Custom type brzaccVLFlashMemoryControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("resetAndBootFromShadowVersion", 1),
          ("useRunningVersionAfterReset", 2))
    )


_BrzaccVLFlashMemoryControl_Type.__name__ = "Integer32"
_BrzaccVLFlashMemoryControl_Object = MibScalar
brzaccVLFlashMemoryControl = _BrzaccVLFlashMemoryControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 4),
    _BrzaccVLFlashMemoryControl_Type()
)
brzaccVLFlashMemoryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFlashMemoryControl.setStatus("current")
_BrzaccVLTelnetLogoutTimer_Type = Integer32
_BrzaccVLTelnetLogoutTimer_Object = MibScalar
brzaccVLTelnetLogoutTimer = _BrzaccVLTelnetLogoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 5),
    _BrzaccVLTelnetLogoutTimer_Type()
)
brzaccVLTelnetLogoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTelnetLogoutTimer.setStatus("current")


class _BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type(Integer32):
    """Custom type brzaccVLSaveCurrentConfigurationAsOperatorDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("saveAsDefaults", 1))
    )


_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type.__name__ = "Integer32"
_BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Object = MibScalar
brzaccVLSaveCurrentConfigurationAsOperatorDefaults = _BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 6),
    _BrzaccVLSaveCurrentConfigurationAsOperatorDefaults_Type()
)
brzaccVLSaveCurrentConfigurationAsOperatorDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSaveCurrentConfigurationAsOperatorDefaults.setStatus("current")


class _BrzaccVLExitTelnet_Type(Integer32):
    """Custom type brzaccVLExitTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("exit", 2))
    )


_BrzaccVLExitTelnet_Type.__name__ = "Integer32"
_BrzaccVLExitTelnet_Object = MibScalar
brzaccVLExitTelnet = _BrzaccVLExitTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 7),
    _BrzaccVLExitTelnet_Type()
)
brzaccVLExitTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLExitTelnet.setStatus("current")
_BrzaccVLUnitPasswords_ObjectIdentity = ObjectIdentity
brzaccVLUnitPasswords = _BrzaccVLUnitPasswords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8)
)


class _BrzaccVLReadOnlyPassword_Type(DisplayString):
    """Custom type brzaccVLReadOnlyPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BrzaccVLReadOnlyPassword_Type.__name__ = "DisplayString"
_BrzaccVLReadOnlyPassword_Object = MibScalar
brzaccVLReadOnlyPassword = _BrzaccVLReadOnlyPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 1),
    _BrzaccVLReadOnlyPassword_Type()
)
brzaccVLReadOnlyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLReadOnlyPassword.setStatus("current")


class _BrzaccVLInstallerPassword_Type(DisplayString):
    """Custom type brzaccVLInstallerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BrzaccVLInstallerPassword_Type.__name__ = "DisplayString"
_BrzaccVLInstallerPassword_Object = MibScalar
brzaccVLInstallerPassword = _BrzaccVLInstallerPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 2),
    _BrzaccVLInstallerPassword_Type()
)
brzaccVLInstallerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInstallerPassword.setStatus("current")


class _BrzaccVLAdminPassword_Type(DisplayString):
    """Custom type brzaccVLAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BrzaccVLAdminPassword_Type.__name__ = "DisplayString"
_BrzaccVLAdminPassword_Object = MibScalar
brzaccVLAdminPassword = _BrzaccVLAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 3),
    _BrzaccVLAdminPassword_Type()
)
brzaccVLAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdminPassword.setStatus("current")


class _BrzaccVLEthernetNegotiationMode_Type(Integer32):
    """Custom type brzaccVLEthernetNegotiationMode based on Integer32"""
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
        *(("autoNegotiationMode", 5),
          ("force100MbpsAndFullDuplex", 4),
          ("force100MbpsAndHalfDuplex", 3),
          ("force10MbpsAndFullDuplex", 2),
          ("force10MbpsAndHalfDuplex", 1))
    )


_BrzaccVLEthernetNegotiationMode_Type.__name__ = "Integer32"
_BrzaccVLEthernetNegotiationMode_Object = MibScalar
brzaccVLEthernetNegotiationMode = _BrzaccVLEthernetNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 9),
    _BrzaccVLEthernetNegotiationMode_Type()
)
brzaccVLEthernetNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthernetNegotiationMode.setStatus("current")
_BrzaccVLFTPParameters_ObjectIdentity = ObjectIdentity
brzaccVLFTPParameters = _BrzaccVLFTPParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10)
)
_BrzaccVLFTPServerParams_ObjectIdentity = ObjectIdentity
brzaccVLFTPServerParams = _BrzaccVLFTPServerParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1)
)


class _BrzaccVLFTPServerUserName_Type(DisplayString):
    """Custom type brzaccVLFTPServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_BrzaccVLFTPServerUserName_Type.__name__ = "DisplayString"
_BrzaccVLFTPServerUserName_Object = MibScalar
brzaccVLFTPServerUserName = _BrzaccVLFTPServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 1),
    _BrzaccVLFTPServerUserName_Type()
)
brzaccVLFTPServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPServerUserName.setStatus("current")


class _BrzaccVLFTPServerPassword_Type(DisplayString):
    """Custom type brzaccVLFTPServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_BrzaccVLFTPServerPassword_Type.__name__ = "DisplayString"
_BrzaccVLFTPServerPassword_Object = MibScalar
brzaccVLFTPServerPassword = _BrzaccVLFTPServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 2),
    _BrzaccVLFTPServerPassword_Type()
)
brzaccVLFTPServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPServerPassword.setStatus("current")
_BrzaccVLFTPClientIPAddress_Type = IpAddress
_BrzaccVLFTPClientIPAddress_Object = MibScalar
brzaccVLFTPClientIPAddress = _BrzaccVLFTPClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 3),
    _BrzaccVLFTPClientIPAddress_Type()
)
brzaccVLFTPClientIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPClientIPAddress.setStatus("current")
_BrzaccVLFTPServerIpAddress_Type = IpAddress
_BrzaccVLFTPServerIpAddress_Object = MibScalar
brzaccVLFTPServerIpAddress = _BrzaccVLFTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 4),
    _BrzaccVLFTPServerIpAddress_Type()
)
brzaccVLFTPServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPServerIpAddress.setStatus("current")
_BrzaccVLFTPClientMask_Type = IpAddress
_BrzaccVLFTPClientMask_Object = MibScalar
brzaccVLFTPClientMask = _BrzaccVLFTPClientMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 5),
    _BrzaccVLFTPClientMask_Type()
)
brzaccVLFTPClientMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPClientMask.setStatus("current")
_BrzaccVLFTPGatewayIpAddress_Type = IpAddress
_BrzaccVLFTPGatewayIpAddress_Object = MibScalar
brzaccVLFTPGatewayIpAddress = _BrzaccVLFTPGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 6),
    _BrzaccVLFTPGatewayIpAddress_Type()
)
brzaccVLFTPGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPGatewayIpAddress.setStatus("current")
_BrzaccVLFTPSwDownload_ObjectIdentity = ObjectIdentity
brzaccVLFTPSwDownload = _BrzaccVLFTPSwDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2)
)


class _BrzaccVLFTPSwFileName_Type(DisplayString):
    """Custom type brzaccVLFTPSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BrzaccVLFTPSwFileName_Type.__name__ = "DisplayString"
_BrzaccVLFTPSwFileName_Object = MibScalar
brzaccVLFTPSwFileName = _BrzaccVLFTPSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 1),
    _BrzaccVLFTPSwFileName_Type()
)
brzaccVLFTPSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPSwFileName.setStatus("current")


class _BrzaccVLFTPSwSourceDir_Type(DisplayString):
    """Custom type brzaccVLFTPSwSourceDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BrzaccVLFTPSwSourceDir_Type.__name__ = "DisplayString"
_BrzaccVLFTPSwSourceDir_Object = MibScalar
brzaccVLFTPSwSourceDir = _BrzaccVLFTPSwSourceDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 2),
    _BrzaccVLFTPSwSourceDir_Type()
)
brzaccVLFTPSwSourceDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPSwSourceDir.setStatus("current")


class _BrzaccVLFTPDownloadSwFile_Type(Integer32):
    """Custom type brzaccVLFTPDownloadSwFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("downloadFile", 1))
    )


_BrzaccVLFTPDownloadSwFile_Type.__name__ = "Integer32"
_BrzaccVLFTPDownloadSwFile_Object = MibScalar
brzaccVLFTPDownloadSwFile = _BrzaccVLFTPDownloadSwFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 3),
    _BrzaccVLFTPDownloadSwFile_Type()
)
brzaccVLFTPDownloadSwFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPDownloadSwFile.setStatus("current")
_BrzaccVLConfigurationFileLoading_ObjectIdentity = ObjectIdentity
brzaccVLConfigurationFileLoading = _BrzaccVLConfigurationFileLoading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3)
)


class _BrzaccVLConfigurationFileName_Type(DisplayString):
    """Custom type brzaccVLConfigurationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BrzaccVLConfigurationFileName_Type.__name__ = "DisplayString"
_BrzaccVLConfigurationFileName_Object = MibScalar
brzaccVLConfigurationFileName = _BrzaccVLConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 1),
    _BrzaccVLConfigurationFileName_Type()
)
brzaccVLConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLConfigurationFileName.setStatus("current")


class _BrzaccVLOperatorDefaultsFileName_Type(DisplayString):
    """Custom type brzaccVLOperatorDefaultsFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BrzaccVLOperatorDefaultsFileName_Type.__name__ = "DisplayString"
_BrzaccVLOperatorDefaultsFileName_Object = MibScalar
brzaccVLOperatorDefaultsFileName = _BrzaccVLOperatorDefaultsFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 2),
    _BrzaccVLOperatorDefaultsFileName_Type()
)
brzaccVLOperatorDefaultsFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLOperatorDefaultsFileName.setStatus("current")


class _BrzaccVLFTPConfigurationFileSourceDir_Type(DisplayString):
    """Custom type brzaccVLFTPConfigurationFileSourceDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BrzaccVLFTPConfigurationFileSourceDir_Type.__name__ = "DisplayString"
_BrzaccVLFTPConfigurationFileSourceDir_Object = MibScalar
brzaccVLFTPConfigurationFileSourceDir = _BrzaccVLFTPConfigurationFileSourceDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 3),
    _BrzaccVLFTPConfigurationFileSourceDir_Type()
)
brzaccVLFTPConfigurationFileSourceDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFTPConfigurationFileSourceDir.setStatus("current")


class _BrzaccVLExecuteFTPConfigurationFileLoading_Type(Integer32):
    """Custom type brzaccVLExecuteFTPConfigurationFileLoading based on Integer32"""
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
        *(("cancel", 5),
          ("executeFTPGetConfigurationFile", 1),
          ("executeFTPGetOperatorDefaults", 3),
          ("executeFTPPutConfigurationFile", 2),
          ("executeFTPPutOperatorDefaults", 4))
    )


_BrzaccVLExecuteFTPConfigurationFileLoading_Type.__name__ = "Integer32"
_BrzaccVLExecuteFTPConfigurationFileLoading_Object = MibScalar
brzaccVLExecuteFTPConfigurationFileLoading = _BrzaccVLExecuteFTPConfigurationFileLoading_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 4),
    _BrzaccVLExecuteFTPConfigurationFileLoading_Type()
)
brzaccVLExecuteFTPConfigurationFileLoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLExecuteFTPConfigurationFileLoading.setStatus("current")
_BrzaccVLEventLogFileUploading_ObjectIdentity = ObjectIdentity
brzaccVLEventLogFileUploading = _BrzaccVLEventLogFileUploading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4)
)


class _BrzaccVLEventLogFileName_Type(DisplayString):
    """Custom type brzaccVLEventLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BrzaccVLEventLogFileName_Type.__name__ = "DisplayString"
_BrzaccVLEventLogFileName_Object = MibScalar
brzaccVLEventLogFileName = _BrzaccVLEventLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 1),
    _BrzaccVLEventLogFileName_Type()
)
brzaccVLEventLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEventLogFileName.setStatus("current")


class _BrzaccVLEventLogDestinationDir_Type(DisplayString):
    """Custom type brzaccVLEventLogDestinationDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BrzaccVLEventLogDestinationDir_Type.__name__ = "DisplayString"
_BrzaccVLEventLogDestinationDir_Object = MibScalar
brzaccVLEventLogDestinationDir = _BrzaccVLEventLogDestinationDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 2),
    _BrzaccVLEventLogDestinationDir_Type()
)
brzaccVLEventLogDestinationDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEventLogDestinationDir.setStatus("current")


class _BrzaccVLUploadEventLogFile_Type(Integer32):
    """Custom type brzaccVLUploadEventLogFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("uploadFile", 1))
    )


_BrzaccVLUploadEventLogFile_Type.__name__ = "Integer32"
_BrzaccVLUploadEventLogFile_Object = MibScalar
brzaccVLUploadEventLogFile = _BrzaccVLUploadEventLogFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 3),
    _BrzaccVLUploadEventLogFile_Type()
)
brzaccVLUploadEventLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUploadEventLogFile.setStatus("current")


class _BrzaccVLLoadingStatus_Type(Integer32):
    """Custom type brzaccVLLoadingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProcess", 1),
          ("successful", 2))
    )


_BrzaccVLLoadingStatus_Type.__name__ = "Integer32"
_BrzaccVLLoadingStatus_Object = MibScalar
brzaccVLLoadingStatus = _BrzaccVLLoadingStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 11),
    _BrzaccVLLoadingStatus_Type()
)
brzaccVLLoadingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLLoadingStatus.setStatus("current")
_BrzaccVLEventLogFileParams_ObjectIdentity = ObjectIdentity
brzaccVLEventLogFileParams = _BrzaccVLEventLogFileParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12)
)


class _BrzaccVLEventLogPolicy_Type(Integer32):
    """Custom type brzaccVLEventLogPolicy based on Integer32"""
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
        *(("error", 3),
          ("fatal", 4),
          ("logNone", 5),
          ("message", 1),
          ("warning", 2))
    )


_BrzaccVLEventLogPolicy_Type.__name__ = "Integer32"
_BrzaccVLEventLogPolicy_Object = MibScalar
brzaccVLEventLogPolicy = _BrzaccVLEventLogPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12, 1),
    _BrzaccVLEventLogPolicy_Type()
)
brzaccVLEventLogPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEventLogPolicy.setStatus("current")


class _BrzaccVLEraseEventLog_Type(Integer32):
    """Custom type brzaccVLEraseEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("eraseEventLog", 1))
    )


_BrzaccVLEraseEventLog_Type.__name__ = "Integer32"
_BrzaccVLEraseEventLog_Object = MibScalar
brzaccVLEraseEventLog = _BrzaccVLEraseEventLog_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12, 2),
    _BrzaccVLEraseEventLog_Type()
)
brzaccVLEraseEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEraseEventLog.setStatus("current")


class _BrzaccVLSystemLocation_Type(DisplayString):
    """Custom type brzaccVLSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_BrzaccVLSystemLocation_Type.__name__ = "DisplayString"
_BrzaccVLSystemLocation_Object = MibScalar
brzaccVLSystemLocation = _BrzaccVLSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 13),
    _BrzaccVLSystemLocation_Type()
)
brzaccVLSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSystemLocation.setStatus("current")
_BrzaccVLFeatureUpgrade_ObjectIdentity = ObjectIdentity
brzaccVLFeatureUpgrade = _BrzaccVLFeatureUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 14)
)


class _BrzaccVLFeatureUpgradeManually_Type(DisplayString):
    """Custom type brzaccVLFeatureUpgradeManually based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 64),
    )


_BrzaccVLFeatureUpgradeManually_Type.__name__ = "DisplayString"
_BrzaccVLFeatureUpgradeManually_Object = MibScalar
brzaccVLFeatureUpgradeManually = _BrzaccVLFeatureUpgradeManually_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 14, 1),
    _BrzaccVLFeatureUpgradeManually_Type()
)
brzaccVLFeatureUpgradeManually.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFeatureUpgradeManually.setStatus("current")


class _BrzaccVLChangeUnitType_Type(Integer32):
    """Custom type brzaccVLChangeUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bu", 1),
          ("cancel", 3),
          ("rb", 2))
    )


_BrzaccVLChangeUnitType_Type.__name__ = "Integer32"
_BrzaccVLChangeUnitType_Object = MibScalar
brzaccVLChangeUnitType = _BrzaccVLChangeUnitType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 15),
    _BrzaccVLChangeUnitType_Type()
)
brzaccVLChangeUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLChangeUnitType.setStatus("current")


class _BrzaccVLApWorkingMode_Type(Integer32):
    """Custom type brzaccVLApWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ezMode", 1),
          ("na", 255))
    )


_BrzaccVLApWorkingMode_Type.__name__ = "Integer32"
_BrzaccVLApWorkingMode_Object = MibScalar
brzaccVLApWorkingMode = _BrzaccVLApWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 16),
    _BrzaccVLApWorkingMode_Type()
)
brzaccVLApWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLApWorkingMode.setStatus("current")
_BrzaccVLLEDsettings_ObjectIdentity = ObjectIdentity
brzaccVLLEDsettings = _BrzaccVLLEDsettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17)
)


class _BrzaccVLLEDmode_Type(Integer32):
    """Custom type brzaccVLLEDmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("threshold", 2))
    )


_BrzaccVLLEDmode_Type.__name__ = "Integer32"
_BrzaccVLLEDmode_Object = MibScalar
brzaccVLLEDmode = _BrzaccVLLEDmode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 1),
    _BrzaccVLLEDmode_Type()
)
brzaccVLLEDmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLLEDmode.setStatus("current")
_BrzaccVLThresholdTable_Object = MibTable
brzaccVLThresholdTable = _BrzaccVLThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    brzaccVLThresholdTable.setStatus("current")
_BrzaccVLThresholdTableEntry_Object = MibTableRow
brzaccVLThresholdTableEntry = _BrzaccVLThresholdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2, 1)
)
brzaccVLThresholdTableEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLThresholdLEDnum"),
)
if mibBuilder.loadTexts:
    brzaccVLThresholdTableEntry.setStatus("current")


class _BrzaccVLThresholdLEDnum_Type(Integer32):
    """Custom type brzaccVLThresholdLEDnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLThresholdLEDnum_Type.__name__ = "Integer32"
_BrzaccVLThresholdLEDnum_Object = MibTableColumn
brzaccVLThresholdLEDnum = _BrzaccVLThresholdLEDnum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2, 1, 1),
    _BrzaccVLThresholdLEDnum_Type()
)
brzaccVLThresholdLEDnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLThresholdLEDnum.setStatus("current")


class _BrzaccVLThresholdLEDtype_Type(Integer32):
    """Custom type brzaccVLThresholdLEDtype based on Integer32"""
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
        *(("typeAverageModulation", 5),
          ("typeCRC", 3),
          ("typeDisabled", 1),
          ("typeRSSI", 2),
          ("typeSNR", 4))
    )


_BrzaccVLThresholdLEDtype_Type.__name__ = "Integer32"
_BrzaccVLThresholdLEDtype_Object = MibTableColumn
brzaccVLThresholdLEDtype = _BrzaccVLThresholdLEDtype_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2, 1, 2),
    _BrzaccVLThresholdLEDtype_Type()
)
brzaccVLThresholdLEDtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLThresholdLEDtype.setStatus("current")


class _BrzaccVLThresholdLEDmode_Type(Integer32):
    """Custom type brzaccVLThresholdLEDmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("equalOrHigher", 2),
          ("equalOrLower", 1))
    )


_BrzaccVLThresholdLEDmode_Type.__name__ = "Integer32"
_BrzaccVLThresholdLEDmode_Object = MibTableColumn
brzaccVLThresholdLEDmode = _BrzaccVLThresholdLEDmode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2, 1, 3),
    _BrzaccVLThresholdLEDmode_Type()
)
brzaccVLThresholdLEDmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLThresholdLEDmode.setStatus("current")


class _BrzaccVLThresholdLEDtarget_Type(Integer32):
    """Custom type brzaccVLThresholdLEDtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-108, 100),
    )


_BrzaccVLThresholdLEDtarget_Type.__name__ = "Integer32"
_BrzaccVLThresholdLEDtarget_Object = MibTableColumn
brzaccVLThresholdLEDtarget = _BrzaccVLThresholdLEDtarget_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 17, 2, 1, 4),
    _BrzaccVLThresholdLEDtarget_Type()
)
brzaccVLThresholdLEDtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLThresholdLEDtarget.setStatus("current")
_BrzaccVLNwMngParameters_ObjectIdentity = ObjectIdentity
brzaccVLNwMngParameters = _BrzaccVLNwMngParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3)
)


class _BrzaccVLAccessToNwMng_Type(Integer32):
    """Custom type brzaccVLAccessToNwMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fromBothWirelessAndEthernet", 3),
          ("fromEthernetOnly", 2),
          ("fromWirelessOnly", 1),
          ("na", 255))
    )


_BrzaccVLAccessToNwMng_Type.__name__ = "Integer32"
_BrzaccVLAccessToNwMng_Object = MibScalar
brzaccVLAccessToNwMng = _BrzaccVLAccessToNwMng_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 1),
    _BrzaccVLAccessToNwMng_Type()
)
brzaccVLAccessToNwMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAccessToNwMng.setStatus("current")


class _BrzaccVLNwMngFilter_Type(Integer32):
    """Custom type brzaccVLNwMngFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("activateOnBothWirelessAndEthernet", 4),
          ("activateOnEthernetPort", 2),
          ("activateOnWirelessPort", 3),
          ("disable", 1),
          ("na", 255))
    )


_BrzaccVLNwMngFilter_Type.__name__ = "Integer32"
_BrzaccVLNwMngFilter_Object = MibScalar
brzaccVLNwMngFilter = _BrzaccVLNwMngFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 2),
    _BrzaccVLNwMngFilter_Type()
)
brzaccVLNwMngFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNwMngFilter.setStatus("current")
_MngIpFilterTable_Object = MibTable
mngIpFilterTable = _MngIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mngIpFilterTable.setStatus("current")
_MngIpFilterEntry_Object = MibTableRow
mngIpFilterEntry = _MngIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1)
)
mngIpFilterEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNwMngIpTableIdx"),
)
if mibBuilder.loadTexts:
    mngIpFilterEntry.setStatus("current")
_BrzaccVLNwMngIpAddress_Type = IpAddress
_BrzaccVLNwMngIpAddress_Object = MibTableColumn
brzaccVLNwMngIpAddress = _BrzaccVLNwMngIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1, 1),
    _BrzaccVLNwMngIpAddress_Type()
)
brzaccVLNwMngIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNwMngIpAddress.setStatus("current")


class _BrzaccVLNwMngIpTableIdx_Type(Integer32):
    """Custom type brzaccVLNwMngIpTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BrzaccVLNwMngIpTableIdx_Type.__name__ = "Integer32"
_BrzaccVLNwMngIpTableIdx_Object = MibTableColumn
brzaccVLNwMngIpTableIdx = _BrzaccVLNwMngIpTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1, 2),
    _BrzaccVLNwMngIpTableIdx_Type()
)
brzaccVLNwMngIpTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNwMngIpTableIdx.setStatus("current")


class _BrzaccVLDeleteOneNwIpAddr_Type(Integer32):
    """Custom type brzaccVLDeleteOneNwIpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLDeleteOneNwIpAddr_Type.__name__ = "Integer32"
_BrzaccVLDeleteOneNwIpAddr_Object = MibScalar
brzaccVLDeleteOneNwIpAddr = _BrzaccVLDeleteOneNwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 4),
    _BrzaccVLDeleteOneNwIpAddr_Type()
)
brzaccVLDeleteOneNwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteOneNwIpAddr.setStatus("current")


class _BrzaccVLDeleteAllNwIpAddrs_Type(Integer32):
    """Custom type brzaccVLDeleteAllNwIpAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1),
          ("na", 255))
    )


_BrzaccVLDeleteAllNwIpAddrs_Type.__name__ = "Integer32"
_BrzaccVLDeleteAllNwIpAddrs_Object = MibScalar
brzaccVLDeleteAllNwIpAddrs = _BrzaccVLDeleteAllNwIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 5),
    _BrzaccVLDeleteAllNwIpAddrs_Type()
)
brzaccVLDeleteAllNwIpAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteAllNwIpAddrs.setStatus("current")


class _BrzaccVLAccessToNwTrap_Type(Integer32):
    """Custom type brzaccVLAccessToNwTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLAccessToNwTrap_Type.__name__ = "Integer32"
_BrzaccVLAccessToNwTrap_Object = MibScalar
brzaccVLAccessToNwTrap = _BrzaccVLAccessToNwTrap_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 6),
    _BrzaccVLAccessToNwTrap_Type()
)
brzaccVLAccessToNwTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAccessToNwTrap.setStatus("current")
_MngTrapTable_Object = MibTable
mngTrapTable = _MngTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mngTrapTable.setStatus("current")
_MngTrapEntry_Object = MibTableRow
mngTrapEntry = _MngTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1)
)
mngTrapEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNwTrapTableIdx"),
)
if mibBuilder.loadTexts:
    mngTrapEntry.setStatus("current")


class _BrzaccVLNwMngTrapCommunity_Type(DisplayString):
    """Custom type brzaccVLNwMngTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_BrzaccVLNwMngTrapCommunity_Type.__name__ = "DisplayString"
_BrzaccVLNwMngTrapCommunity_Object = MibTableColumn
brzaccVLNwMngTrapCommunity = _BrzaccVLNwMngTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 1),
    _BrzaccVLNwMngTrapCommunity_Type()
)
brzaccVLNwMngTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNwMngTrapCommunity.setStatus("current")
_BrzaccVLNwMngTrapAddress_Type = IpAddress
_BrzaccVLNwMngTrapAddress_Object = MibTableColumn
brzaccVLNwMngTrapAddress = _BrzaccVLNwMngTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 2),
    _BrzaccVLNwMngTrapAddress_Type()
)
brzaccVLNwMngTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNwMngTrapAddress.setStatus("current")


class _BrzaccVLNwTrapTableIdx_Type(Integer32):
    """Custom type brzaccVLNwTrapTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BrzaccVLNwTrapTableIdx_Type.__name__ = "Integer32"
_BrzaccVLNwTrapTableIdx_Object = MibTableColumn
brzaccVLNwTrapTableIdx = _BrzaccVLNwTrapTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 3),
    _BrzaccVLNwTrapTableIdx_Type()
)
brzaccVLNwTrapTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNwTrapTableIdx.setStatus("current")


class _BrzaccVLDeleteOneTrapAddr_Type(Integer32):
    """Custom type brzaccVLDeleteOneTrapAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLDeleteOneTrapAddr_Type.__name__ = "Integer32"
_BrzaccVLDeleteOneTrapAddr_Object = MibScalar
brzaccVLDeleteOneTrapAddr = _BrzaccVLDeleteOneTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 8),
    _BrzaccVLDeleteOneTrapAddr_Type()
)
brzaccVLDeleteOneTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteOneTrapAddr.setStatus("current")


class _BrzaccVLDeleteAllTrapAddrs_Type(Integer32):
    """Custom type brzaccVLDeleteAllTrapAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1),
          ("na", 255))
    )


_BrzaccVLDeleteAllTrapAddrs_Type.__name__ = "Integer32"
_BrzaccVLDeleteAllTrapAddrs_Object = MibScalar
brzaccVLDeleteAllTrapAddrs = _BrzaccVLDeleteAllTrapAddrs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 9),
    _BrzaccVLDeleteAllTrapAddrs_Type()
)
brzaccVLDeleteAllTrapAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteAllTrapAddrs.setStatus("current")
_BrzaccVLMngIpRangesTable_Object = MibTable
brzaccVLMngIpRangesTable = _BrzaccVLMngIpRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    brzaccVLMngIpRangesTable.setStatus("current")
_BrzaccVLMngIpRangeEntry_Object = MibTableRow
brzaccVLMngIpRangeEntry = _BrzaccVLMngIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1)
)
brzaccVLMngIpRangeEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLMngIpRangeIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeEntry.setStatus("current")


class _BrzaccVLMngIpRangeIdx_Type(Integer32):
    """Custom type brzaccVLMngIpRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BrzaccVLMngIpRangeIdx_Type.__name__ = "Integer32"
_BrzaccVLMngIpRangeIdx_Object = MibTableColumn
brzaccVLMngIpRangeIdx = _BrzaccVLMngIpRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 1),
    _BrzaccVLMngIpRangeIdx_Type()
)
brzaccVLMngIpRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeIdx.setStatus("current")


class _BrzaccVLMngIpRangeFlag_Type(Integer32):
    """Custom type brzaccVLMngIpRangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rangeDefinedByStartAddrMask", 2),
          ("rangeDefinedByStartEndAddr", 1))
    )


_BrzaccVLMngIpRangeFlag_Type.__name__ = "Integer32"
_BrzaccVLMngIpRangeFlag_Object = MibTableColumn
brzaccVLMngIpRangeFlag = _BrzaccVLMngIpRangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 2),
    _BrzaccVLMngIpRangeFlag_Type()
)
brzaccVLMngIpRangeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeFlag.setStatus("current")
_BrzaccVLMngIpRangeStart_Type = IpAddress
_BrzaccVLMngIpRangeStart_Object = MibTableColumn
brzaccVLMngIpRangeStart = _BrzaccVLMngIpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 3),
    _BrzaccVLMngIpRangeStart_Type()
)
brzaccVLMngIpRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeStart.setStatus("current")
_BrzaccVLMngIpRangeEnd_Type = IpAddress
_BrzaccVLMngIpRangeEnd_Object = MibTableColumn
brzaccVLMngIpRangeEnd = _BrzaccVLMngIpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 4),
    _BrzaccVLMngIpRangeEnd_Type()
)
brzaccVLMngIpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeEnd.setStatus("current")
_BrzaccVLMngIpRangeMask_Type = IpAddress
_BrzaccVLMngIpRangeMask_Object = MibTableColumn
brzaccVLMngIpRangeMask = _BrzaccVLMngIpRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 5),
    _BrzaccVLMngIpRangeMask_Type()
)
brzaccVLMngIpRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMngIpRangeMask.setStatus("current")


class _BrzaccVLDeleteOneNwIpRange_Type(Integer32):
    """Custom type brzaccVLDeleteOneNwIpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLDeleteOneNwIpRange_Type.__name__ = "Integer32"
_BrzaccVLDeleteOneNwIpRange_Object = MibScalar
brzaccVLDeleteOneNwIpRange = _BrzaccVLDeleteOneNwIpRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 11),
    _BrzaccVLDeleteOneNwIpRange_Type()
)
brzaccVLDeleteOneNwIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteOneNwIpRange.setStatus("current")


class _BrzaccVLDeleteAllNwIpRanges_Type(Integer32):
    """Custom type brzaccVLDeleteAllNwIpRanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1),
          ("na", 255))
    )


_BrzaccVLDeleteAllNwIpRanges_Type.__name__ = "Integer32"
_BrzaccVLDeleteAllNwIpRanges_Object = MibScalar
brzaccVLDeleteAllNwIpRanges = _BrzaccVLDeleteAllNwIpRanges_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 12),
    _BrzaccVLDeleteAllNwIpRanges_Type()
)
brzaccVLDeleteAllNwIpRanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteAllNwIpRanges.setStatus("current")
_BrzaccVLWi2IpAddress_Type = IpAddress
_BrzaccVLWi2IpAddress_Object = MibScalar
brzaccVLWi2IpAddress = _BrzaccVLWi2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 13),
    _BrzaccVLWi2IpAddress_Type()
)
brzaccVLWi2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLWi2IpAddress.setStatus("current")
_BrzaccVLNewNMngSystem_ObjectIdentity = ObjectIdentity
brzaccVLNewNMngSystem = _BrzaccVLNewNMngSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14)
)
_BrzaccVLErrorHandling_ObjectIdentity = ObjectIdentity
brzaccVLErrorHandling = _BrzaccVLErrorHandling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1)
)
_BrzaccVLErrHandlingSetNMSId_Type = Integer32
_BrzaccVLErrHandlingSetNMSId_Object = MibScalar
brzaccVLErrHandlingSetNMSId = _BrzaccVLErrHandlingSetNMSId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 1),
    _BrzaccVLErrHandlingSetNMSId_Type()
)
brzaccVLErrHandlingSetNMSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingSetNMSId.setStatus("current")
_BrzaccVLErrHandlingTable_Object = MibTable
brzaccVLErrHandlingTable = _BrzaccVLErrHandlingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2)
)
if mibBuilder.loadTexts:
    brzaccVLErrHandlingTable.setStatus("current")
_BrzaccVLErrHandlingEntry_Object = MibTableRow
brzaccVLErrHandlingEntry = _BrzaccVLErrHandlingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1)
)
brzaccVLErrHandlingEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLErrHandlingNMSId"),
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLErrHandlingRequestId"),
)
if mibBuilder.loadTexts:
    brzaccVLErrHandlingEntry.setStatus("current")


class _BrzaccVLErrHandlingNMSId_Type(Unsigned32):
    """Custom type brzaccVLErrHandlingNMSId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BrzaccVLErrHandlingNMSId_Type.__name__ = "Unsigned32"
_BrzaccVLErrHandlingNMSId_Object = MibTableColumn
brzaccVLErrHandlingNMSId = _BrzaccVLErrHandlingNMSId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 1),
    _BrzaccVLErrHandlingNMSId_Type()
)
brzaccVLErrHandlingNMSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingNMSId.setStatus("current")


class _BrzaccVLErrHandlingRequestId_Type(Unsigned32):
    """Custom type brzaccVLErrHandlingRequestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BrzaccVLErrHandlingRequestId_Type.__name__ = "Unsigned32"
_BrzaccVLErrHandlingRequestId_Object = MibTableColumn
brzaccVLErrHandlingRequestId = _BrzaccVLErrHandlingRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 2),
    _BrzaccVLErrHandlingRequestId_Type()
)
brzaccVLErrHandlingRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingRequestId.setStatus("current")
_BrzaccVLErrHandlingErrorCode_Type = Integer32
_BrzaccVLErrHandlingErrorCode_Object = MibTableColumn
brzaccVLErrHandlingErrorCode = _BrzaccVLErrHandlingErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 3),
    _BrzaccVLErrHandlingErrorCode_Type()
)
brzaccVLErrHandlingErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingErrorCode.setStatus("current")
_BrzaccVLErrHandlingParameter1_Type = Integer32
_BrzaccVLErrHandlingParameter1_Object = MibTableColumn
brzaccVLErrHandlingParameter1 = _BrzaccVLErrHandlingParameter1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 4),
    _BrzaccVLErrHandlingParameter1_Type()
)
brzaccVLErrHandlingParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingParameter1.setStatus("current")
_BrzaccVLErrHandlingParameter2_Type = Integer32
_BrzaccVLErrHandlingParameter2_Object = MibTableColumn
brzaccVLErrHandlingParameter2 = _BrzaccVLErrHandlingParameter2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 5),
    _BrzaccVLErrHandlingParameter2_Type()
)
brzaccVLErrHandlingParameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingParameter2.setStatus("current")
_BrzaccVLErrHandlingParameter3_Type = Integer32
_BrzaccVLErrHandlingParameter3_Object = MibTableColumn
brzaccVLErrHandlingParameter3 = _BrzaccVLErrHandlingParameter3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 6),
    _BrzaccVLErrHandlingParameter3_Type()
)
brzaccVLErrHandlingParameter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingParameter3.setStatus("current")
_BrzaccVLErrHandlingParameter4_Type = Integer32
_BrzaccVLErrHandlingParameter4_Object = MibTableColumn
brzaccVLErrHandlingParameter4 = _BrzaccVLErrHandlingParameter4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 7),
    _BrzaccVLErrHandlingParameter4_Type()
)
brzaccVLErrHandlingParameter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingParameter4.setStatus("current")
_BrzaccVLErrHandlingParameter5_Type = Integer32
_BrzaccVLErrHandlingParameter5_Object = MibTableColumn
brzaccVLErrHandlingParameter5 = _BrzaccVLErrHandlingParameter5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 1, 2, 1, 8),
    _BrzaccVLErrHandlingParameter5_Type()
)
brzaccVLErrHandlingParameter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLErrHandlingParameter5.setStatus("current")
_BrzaccVLTrapHistory_ObjectIdentity = ObjectIdentity
brzaccVLTrapHistory = _BrzaccVLTrapHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2)
)
_BrzaccVLLastTrapSequenceNumber_Type = Integer32
_BrzaccVLLastTrapSequenceNumber_Object = MibScalar
brzaccVLLastTrapSequenceNumber = _BrzaccVLLastTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 1),
    _BrzaccVLLastTrapSequenceNumber_Type()
)
brzaccVLLastTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLLastTrapSequenceNumber.setStatus("current")
_BrzaccVLTrapHistoryTable_Object = MibTable
brzaccVLTrapHistoryTable = _BrzaccVLTrapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2)
)
if mibBuilder.loadTexts:
    brzaccVLTrapHistoryTable.setStatus("current")
_BrzaccVLTrapHistoryEntry_Object = MibTableRow
brzaccVLTrapHistoryEntry = _BrzaccVLTrapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1)
)
brzaccVLTrapHistoryEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapHistorySequenceNumber"),
)
if mibBuilder.loadTexts:
    brzaccVLTrapHistoryEntry.setStatus("current")


class _BrzaccVLTrapHistorySequenceNumber_Type(Integer32):
    """Custom type brzaccVLTrapHistorySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrzaccVLTrapHistorySequenceNumber_Type.__name__ = "Integer32"
_BrzaccVLTrapHistorySequenceNumber_Object = MibTableColumn
brzaccVLTrapHistorySequenceNumber = _BrzaccVLTrapHistorySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 1),
    _BrzaccVLTrapHistorySequenceNumber_Type()
)
brzaccVLTrapHistorySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapHistorySequenceNumber.setStatus("current")
_BrzaccVLTrapType_Type = Integer32
_BrzaccVLTrapType_Object = MibTableColumn
brzaccVLTrapType = _BrzaccVLTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 2),
    _BrzaccVLTrapType_Type()
)
brzaccVLTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapType.setStatus("current")
_BrzaccVLTrapMacAddrParam_Type = MacAddress
_BrzaccVLTrapMacAddrParam_Object = MibTableColumn
brzaccVLTrapMacAddrParam = _BrzaccVLTrapMacAddrParam_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 3),
    _BrzaccVLTrapMacAddrParam_Type()
)
brzaccVLTrapMacAddrParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapMacAddrParam.setStatus("current")
_BrzaccVLTrapIntParam1_Type = Integer32
_BrzaccVLTrapIntParam1_Object = MibTableColumn
brzaccVLTrapIntParam1 = _BrzaccVLTrapIntParam1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 4),
    _BrzaccVLTrapIntParam1_Type()
)
brzaccVLTrapIntParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapIntParam1.setStatus("current")
_BrzaccVLTrapIntParam2_Type = Integer32
_BrzaccVLTrapIntParam2_Object = MibTableColumn
brzaccVLTrapIntParam2 = _BrzaccVLTrapIntParam2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 5),
    _BrzaccVLTrapIntParam2_Type()
)
brzaccVLTrapIntParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapIntParam2.setStatus("current")
_BrzaccVLTrapIntParam3_Type = Integer32
_BrzaccVLTrapIntParam3_Object = MibTableColumn
brzaccVLTrapIntParam3 = _BrzaccVLTrapIntParam3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 6),
    _BrzaccVLTrapIntParam3_Type()
)
brzaccVLTrapIntParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapIntParam3.setStatus("current")
_BrzaccVLTrapStrParam_Type = DisplayString
_BrzaccVLTrapStrParam_Object = MibTableColumn
brzaccVLTrapStrParam = _BrzaccVLTrapStrParam_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 14, 2, 2, 1, 7),
    _BrzaccVLTrapStrParam_Type()
)
brzaccVLTrapStrParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapStrParam.setStatus("current")
_NewMngIpFilterTable_Object = MibTable
newMngIpFilterTable = _NewMngIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    newMngIpFilterTable.setStatus("current")
_NewMngIpFilterEntry_Object = MibTableRow
newMngIpFilterEntry = _NewMngIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 15, 1)
)
newMngIpFilterEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewNwMngIpAddress"),
)
if mibBuilder.loadTexts:
    newMngIpFilterEntry.setStatus("current")
_BrzaccVLNewNwMngIpAddress_Type = IpAddress
_BrzaccVLNewNwMngIpAddress_Object = MibTableColumn
brzaccVLNewNwMngIpAddress = _BrzaccVLNewNwMngIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 15, 1, 1),
    _BrzaccVLNewNwMngIpAddress_Type()
)
brzaccVLNewNwMngIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewNwMngIpAddress.setStatus("current")


class _BrzaccVLNewNwMngIpAddressCommand_Type(Integer32):
    """Custom type brzaccVLNewNwMngIpAddressCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewNwMngIpAddressCommand_Type.__name__ = "Integer32"
_BrzaccVLNewNwMngIpAddressCommand_Object = MibTableColumn
brzaccVLNewNwMngIpAddressCommand = _BrzaccVLNewNwMngIpAddressCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 15, 1, 2),
    _BrzaccVLNewNwMngIpAddressCommand_Type()
)
brzaccVLNewNwMngIpAddressCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewNwMngIpAddressCommand.setStatus("current")
_NewMngTrapTable_Object = MibTable
newMngTrapTable = _NewMngTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    newMngTrapTable.setStatus("current")
_NewMngTrapEntry_Object = MibTableRow
newMngTrapEntry = _NewMngTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 16, 1)
)
newMngTrapEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewNwMngTrapAddress"),
)
if mibBuilder.loadTexts:
    newMngTrapEntry.setStatus("current")


class _BrzaccVLNewNwMngTrapCommunity_Type(DisplayString):
    """Custom type brzaccVLNewNwMngTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_BrzaccVLNewNwMngTrapCommunity_Type.__name__ = "DisplayString"
_BrzaccVLNewNwMngTrapCommunity_Object = MibTableColumn
brzaccVLNewNwMngTrapCommunity = _BrzaccVLNewNwMngTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 16, 1, 1),
    _BrzaccVLNewNwMngTrapCommunity_Type()
)
brzaccVLNewNwMngTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewNwMngTrapCommunity.setStatus("current")
_BrzaccVLNewNwMngTrapAddress_Type = IpAddress
_BrzaccVLNewNwMngTrapAddress_Object = MibTableColumn
brzaccVLNewNwMngTrapAddress = _BrzaccVLNewNwMngTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 16, 1, 2),
    _BrzaccVLNewNwMngTrapAddress_Type()
)
brzaccVLNewNwMngTrapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewNwMngTrapAddress.setStatus("current")


class _BrzaccVLNewNwTrapCommand_Type(Integer32):
    """Custom type brzaccVLNewNwTrapCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewNwTrapCommand_Type.__name__ = "Integer32"
_BrzaccVLNewNwTrapCommand_Object = MibTableColumn
brzaccVLNewNwTrapCommand = _BrzaccVLNewNwTrapCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 16, 1, 3),
    _BrzaccVLNewNwTrapCommand_Type()
)
brzaccVLNewNwTrapCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewNwTrapCommand.setStatus("current")
_BrzaccVLNewMngIpRangesTable_Object = MibTable
brzaccVLNewMngIpRangesTable = _BrzaccVLNewMngIpRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangesTable.setStatus("current")
_BrzaccVLNewMngIpRangeEntry_Object = MibTableRow
brzaccVLNewMngIpRangeEntry = _BrzaccVLNewMngIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1)
)
brzaccVLNewMngIpRangeEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewMngIpRangeStart"),
)
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeEntry.setStatus("current")
_BrzaccVLNewMngIpRangeStart_Type = IpAddress
_BrzaccVLNewMngIpRangeStart_Object = MibTableColumn
brzaccVLNewMngIpRangeStart = _BrzaccVLNewMngIpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1, 1),
    _BrzaccVLNewMngIpRangeStart_Type()
)
brzaccVLNewMngIpRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeStart.setStatus("current")
_BrzaccVLNewMngIpRangeEnd_Type = IpAddress
_BrzaccVLNewMngIpRangeEnd_Object = MibTableColumn
brzaccVLNewMngIpRangeEnd = _BrzaccVLNewMngIpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1, 2),
    _BrzaccVLNewMngIpRangeEnd_Type()
)
brzaccVLNewMngIpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeEnd.setStatus("current")
_BrzaccVLNewMngIpRangeMask_Type = IpAddress
_BrzaccVLNewMngIpRangeMask_Object = MibTableColumn
brzaccVLNewMngIpRangeMask = _BrzaccVLNewMngIpRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1, 3),
    _BrzaccVLNewMngIpRangeMask_Type()
)
brzaccVLNewMngIpRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeMask.setStatus("current")


class _BrzaccVLNewMngIpRangeFlag_Type(Integer32):
    """Custom type brzaccVLNewMngIpRangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rangeDefinedByStartAddrMask", 2),
          ("rangeDefinedByStartEndAddr", 1))
    )


_BrzaccVLNewMngIpRangeFlag_Type.__name__ = "Integer32"
_BrzaccVLNewMngIpRangeFlag_Object = MibTableColumn
brzaccVLNewMngIpRangeFlag = _BrzaccVLNewMngIpRangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1, 4),
    _BrzaccVLNewMngIpRangeFlag_Type()
)
brzaccVLNewMngIpRangeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeFlag.setStatus("current")


class _BrzaccVLNewMngIpRangeCommand_Type(Integer32):
    """Custom type brzaccVLNewMngIpRangeCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewMngIpRangeCommand_Type.__name__ = "Integer32"
_BrzaccVLNewMngIpRangeCommand_Object = MibTableColumn
brzaccVLNewMngIpRangeCommand = _BrzaccVLNewMngIpRangeCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 17, 1, 5),
    _BrzaccVLNewMngIpRangeCommand_Type()
)
brzaccVLNewMngIpRangeCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMngIpRangeCommand.setStatus("current")
_BrzaccVLIpParams_ObjectIdentity = ObjectIdentity
brzaccVLIpParams = _BrzaccVLIpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4)
)
_BrzaccVLUnitIpAddress_Type = IpAddress
_BrzaccVLUnitIpAddress_Object = MibScalar
brzaccVLUnitIpAddress = _BrzaccVLUnitIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 1),
    _BrzaccVLUnitIpAddress_Type()
)
brzaccVLUnitIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUnitIpAddress.setStatus("current")
_BrzaccVLSubNetMask_Type = IpAddress
_BrzaccVLSubNetMask_Object = MibScalar
brzaccVLSubNetMask = _BrzaccVLSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 2),
    _BrzaccVLSubNetMask_Type()
)
brzaccVLSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSubNetMask.setStatus("current")
_BrzaccVLDefaultGWAddress_Type = IpAddress
_BrzaccVLDefaultGWAddress_Object = MibScalar
brzaccVLDefaultGWAddress = _BrzaccVLDefaultGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 3),
    _BrzaccVLDefaultGWAddress_Type()
)
brzaccVLDefaultGWAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDefaultGWAddress.setStatus("current")


class _BrzaccVLUseDhcp_Type(Integer32):
    """Custom type brzaccVLUseDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("dhcpOnly", 2),
          ("disable", 1))
    )


_BrzaccVLUseDhcp_Type.__name__ = "Integer32"
_BrzaccVLUseDhcp_Object = MibScalar
brzaccVLUseDhcp = _BrzaccVLUseDhcp_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 4),
    _BrzaccVLUseDhcp_Type()
)
brzaccVLUseDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUseDhcp.setStatus("current")


class _BrzaccVLAccessToDHCP_Type(Integer32):
    """Custom type brzaccVLAccessToDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromBothWirelessAndEthernet", 3),
          ("fromEthernetOnly", 2),
          ("fromWirelessOnly", 1))
    )


_BrzaccVLAccessToDHCP_Type.__name__ = "Integer32"
_BrzaccVLAccessToDHCP_Object = MibScalar
brzaccVLAccessToDHCP = _BrzaccVLAccessToDHCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 5),
    _BrzaccVLAccessToDHCP_Type()
)
brzaccVLAccessToDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAccessToDHCP.setStatus("current")
_BrzaccVLRunTimeIPaddr_Type = IpAddress
_BrzaccVLRunTimeIPaddr_Object = MibScalar
brzaccVLRunTimeIPaddr = _BrzaccVLRunTimeIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 6),
    _BrzaccVLRunTimeIPaddr_Type()
)
brzaccVLRunTimeIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunTimeIPaddr.setStatus("current")
_BrzaccVLRunTimeSubNetMask_Type = IpAddress
_BrzaccVLRunTimeSubNetMask_Object = MibScalar
brzaccVLRunTimeSubNetMask = _BrzaccVLRunTimeSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 7),
    _BrzaccVLRunTimeSubNetMask_Type()
)
brzaccVLRunTimeSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunTimeSubNetMask.setStatus("current")
_BrzaccVLRunTimeDefaultIPGateway_Type = IpAddress
_BrzaccVLRunTimeDefaultIPGateway_Object = MibScalar
brzaccVLRunTimeDefaultIPGateway = _BrzaccVLRunTimeDefaultIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 8),
    _BrzaccVLRunTimeDefaultIPGateway_Type()
)
brzaccVLRunTimeDefaultIPGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunTimeDefaultIPGateway.setStatus("current")
_BrzaccVLBridgeParameters_ObjectIdentity = ObjectIdentity
brzaccVLBridgeParameters = _BrzaccVLBridgeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5)
)
_BrzaccVLVLANSupport_ObjectIdentity = ObjectIdentity
brzaccVLVLANSupport = _BrzaccVLVLANSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1)
)
_BrzaccVLVlanID_Type = Integer32
_BrzaccVLVlanID_Object = MibScalar
brzaccVLVlanID = _BrzaccVLVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 1),
    _BrzaccVLVlanID_Type()
)
brzaccVLVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanID.setStatus("current")


class _BrzaccVLEthernetLinkType_Type(Integer32):
    """Custom type brzaccVLEthernetLinkType based on Integer32"""
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
        *(("accessLink", 1),
          ("extAccessLink", 5),
          ("extTrunkLink", 6),
          ("hybridLink", 3),
          ("serviceProviderLink", 4),
          ("trunkLink", 2))
    )


_BrzaccVLEthernetLinkType_Type.__name__ = "Integer32"
_BrzaccVLEthernetLinkType_Object = MibScalar
brzaccVLEthernetLinkType = _BrzaccVLEthernetLinkType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 2),
    _BrzaccVLEthernetLinkType_Type()
)
brzaccVLEthernetLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthernetLinkType.setStatus("current")
_BrzaccVLManagementVlanID_Type = Integer32
_BrzaccVLManagementVlanID_Object = MibScalar
brzaccVLManagementVlanID = _BrzaccVLManagementVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 3),
    _BrzaccVLManagementVlanID_Type()
)
brzaccVLManagementVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLManagementVlanID.setStatus("current")
_BrzaccVLVLANForwarding_ObjectIdentity = ObjectIdentity
brzaccVLVLANForwarding = _BrzaccVLVLANForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4)
)


class _BrzaccVLVlanForwardingSupport_Type(Integer32):
    """Custom type brzaccVLVlanForwardingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLVlanForwardingSupport_Type.__name__ = "Integer32"
_BrzaccVLVlanForwardingSupport_Object = MibScalar
brzaccVLVlanForwardingSupport = _BrzaccVLVlanForwardingSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 1),
    _BrzaccVLVlanForwardingSupport_Type()
)
brzaccVLVlanForwardingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanForwardingSupport.setStatus("current")
_BrzaccVLVlanForwardingTable_Object = MibTable
brzaccVLVlanForwardingTable = _BrzaccVLVlanForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    brzaccVLVlanForwardingTable.setStatus("current")
_BrzaccVLVlanForwardingEntry_Object = MibTableRow
brzaccVLVlanForwardingEntry = _BrzaccVLVlanForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1)
)
brzaccVLVlanForwardingEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLVlanForwardingTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLVlanForwardingEntry.setStatus("current")


class _BrzaccVLVlanForwardingTableIdx_Type(Integer32):
    """Custom type brzaccVLVlanForwardingTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BrzaccVLVlanForwardingTableIdx_Type.__name__ = "Integer32"
_BrzaccVLVlanForwardingTableIdx_Object = MibTableColumn
brzaccVLVlanForwardingTableIdx = _BrzaccVLVlanForwardingTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1, 1),
    _BrzaccVLVlanForwardingTableIdx_Type()
)
brzaccVLVlanForwardingTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLVlanForwardingTableIdx.setStatus("current")
_BrzaccVLVlanIdForwarding_Type = Integer32
_BrzaccVLVlanIdForwarding_Object = MibTableColumn
brzaccVLVlanIdForwarding = _BrzaccVLVlanIdForwarding_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1, 2),
    _BrzaccVLVlanIdForwarding_Type()
)
brzaccVLVlanIdForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanIdForwarding.setStatus("current")
_BrzaccVLNewVlanForwardingTable_Object = MibTable
brzaccVLNewVlanForwardingTable = _BrzaccVLNewVlanForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    brzaccVLNewVlanForwardingTable.setStatus("current")
_BrzaccVLNewVlanForwardingEntry_Object = MibTableRow
brzaccVLNewVlanForwardingEntry = _BrzaccVLNewVlanForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 3, 1)
)
brzaccVLNewVlanForwardingEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewVlanIdForwarding"),
)
if mibBuilder.loadTexts:
    brzaccVLNewVlanForwardingEntry.setStatus("current")


class _BrzaccVLNewVlanIdForwarding_Type(Integer32):
    """Custom type brzaccVLNewVlanIdForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BrzaccVLNewVlanIdForwarding_Type.__name__ = "Integer32"
_BrzaccVLNewVlanIdForwarding_Object = MibTableColumn
brzaccVLNewVlanIdForwarding = _BrzaccVLNewVlanIdForwarding_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 3, 1, 1),
    _BrzaccVLNewVlanIdForwarding_Type()
)
brzaccVLNewVlanIdForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewVlanIdForwarding.setStatus("current")


class _BrzaccVLNewVlanForwardingCommand_Type(Integer32):
    """Custom type brzaccVLNewVlanForwardingCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewVlanForwardingCommand_Type.__name__ = "Integer32"
_BrzaccVLNewVlanForwardingCommand_Object = MibTableColumn
brzaccVLNewVlanForwardingCommand = _BrzaccVLNewVlanForwardingCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 3, 1, 2),
    _BrzaccVLNewVlanForwardingCommand_Type()
)
brzaccVLNewVlanForwardingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewVlanForwardingCommand.setStatus("current")
_BrzaccVLVlanRelaying_ObjectIdentity = ObjectIdentity
brzaccVLVlanRelaying = _BrzaccVLVlanRelaying_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5)
)


class _BrzaccVLVlanRelayingSupport_Type(Integer32):
    """Custom type brzaccVLVlanRelayingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLVlanRelayingSupport_Type.__name__ = "Integer32"
_BrzaccVLVlanRelayingSupport_Object = MibScalar
brzaccVLVlanRelayingSupport = _BrzaccVLVlanRelayingSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 1),
    _BrzaccVLVlanRelayingSupport_Type()
)
brzaccVLVlanRelayingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanRelayingSupport.setStatus("current")
_BrzaccVLVlanRelayingTable_Object = MibTable
brzaccVLVlanRelayingTable = _BrzaccVLVlanRelayingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    brzaccVLVlanRelayingTable.setStatus("current")
_BrzaccVLVlanRelayingEntry_Object = MibTableRow
brzaccVLVlanRelayingEntry = _BrzaccVLVlanRelayingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1)
)
brzaccVLVlanRelayingEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLVlanRelayingTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLVlanRelayingEntry.setStatus("current")


class _BrzaccVLVlanRelayingTableIdx_Type(Integer32):
    """Custom type brzaccVLVlanRelayingTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BrzaccVLVlanRelayingTableIdx_Type.__name__ = "Integer32"
_BrzaccVLVlanRelayingTableIdx_Object = MibTableColumn
brzaccVLVlanRelayingTableIdx = _BrzaccVLVlanRelayingTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1, 1),
    _BrzaccVLVlanRelayingTableIdx_Type()
)
brzaccVLVlanRelayingTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLVlanRelayingTableIdx.setStatus("current")
_BrzaccVLVlanIdRelaying_Type = Integer32
_BrzaccVLVlanIdRelaying_Object = MibTableColumn
brzaccVLVlanIdRelaying = _BrzaccVLVlanIdRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1, 2),
    _BrzaccVLVlanIdRelaying_Type()
)
brzaccVLVlanIdRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanIdRelaying.setStatus("current")
_BrzaccVLNewVlanRelayingTable_Object = MibTable
brzaccVLNewVlanRelayingTable = _BrzaccVLNewVlanRelayingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 3)
)
if mibBuilder.loadTexts:
    brzaccVLNewVlanRelayingTable.setStatus("current")
_BrzaccVLNewVlanRelayingEntry_Object = MibTableRow
brzaccVLNewVlanRelayingEntry = _BrzaccVLNewVlanRelayingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 3, 1)
)
brzaccVLNewVlanRelayingEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewVlanIdRelaying"),
)
if mibBuilder.loadTexts:
    brzaccVLNewVlanRelayingEntry.setStatus("current")


class _BrzaccVLNewVlanIdRelaying_Type(Integer32):
    """Custom type brzaccVLNewVlanIdRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BrzaccVLNewVlanIdRelaying_Type.__name__ = "Integer32"
_BrzaccVLNewVlanIdRelaying_Object = MibTableColumn
brzaccVLNewVlanIdRelaying = _BrzaccVLNewVlanIdRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 3, 1, 1),
    _BrzaccVLNewVlanIdRelaying_Type()
)
brzaccVLNewVlanIdRelaying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewVlanIdRelaying.setStatus("current")


class _BrzaccVLNewVlanRelayingTableCommand_Type(Integer32):
    """Custom type brzaccVLNewVlanRelayingTableCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewVlanRelayingTableCommand_Type.__name__ = "Integer32"
_BrzaccVLNewVlanRelayingTableCommand_Object = MibTableColumn
brzaccVLNewVlanRelayingTableCommand = _BrzaccVLNewVlanRelayingTableCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 3, 1, 2),
    _BrzaccVLNewVlanRelayingTableCommand_Type()
)
brzaccVLNewVlanRelayingTableCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewVlanRelayingTableCommand.setStatus("current")
_BrzaccVLVLANTrafficPriority_ObjectIdentity = ObjectIdentity
brzaccVLVLANTrafficPriority = _BrzaccVLVLANTrafficPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6)
)


class _BrzaccVLVlanDataPriority_Type(Integer32):
    """Custom type brzaccVLVlanDataPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLVlanDataPriority_Type.__name__ = "Integer32"
_BrzaccVLVlanDataPriority_Object = MibScalar
brzaccVLVlanDataPriority = _BrzaccVLVlanDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 1),
    _BrzaccVLVlanDataPriority_Type()
)
brzaccVLVlanDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanDataPriority.setStatus("current")


class _BrzaccVLVlanManagementPriority_Type(Integer32):
    """Custom type brzaccVLVlanManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrzaccVLVlanManagementPriority_Type.__name__ = "Integer32"
_BrzaccVLVlanManagementPriority_Object = MibScalar
brzaccVLVlanManagementPriority = _BrzaccVLVlanManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 2),
    _BrzaccVLVlanManagementPriority_Type()
)
brzaccVLVlanManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanManagementPriority.setStatus("current")


class _BrzaccVLVlanPriorityThreshold_Type(Integer32):
    """Custom type brzaccVLVlanPriorityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLVlanPriorityThreshold_Type.__name__ = "Integer32"
_BrzaccVLVlanPriorityThreshold_Object = MibScalar
brzaccVLVlanPriorityThreshold = _BrzaccVLVlanPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 3),
    _BrzaccVLVlanPriorityThreshold_Type()
)
brzaccVLVlanPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanPriorityThreshold.setStatus("current")
_BrzaccVLVLANQinQ_ObjectIdentity = ObjectIdentity
brzaccVLVLANQinQ = _BrzaccVLVLANQinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7)
)


class _BrzaccVLQinQEthertype_Type(Integer32):
    """Custom type brzaccVLQinQEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 36864),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_BrzaccVLQinQEthertype_Type.__name__ = "Integer32"
_BrzaccVLQinQEthertype_Object = MibScalar
brzaccVLQinQEthertype = _BrzaccVLQinQEthertype_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7, 1),
    _BrzaccVLQinQEthertype_Type()
)
brzaccVLQinQEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLQinQEthertype.setStatus("current")


class _BrzaccVLQinQProviderVlanID_Type(Integer32):
    """Custom type brzaccVLQinQProviderVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BrzaccVLQinQProviderVlanID_Type.__name__ = "Integer32"
_BrzaccVLQinQProviderVlanID_Object = MibScalar
brzaccVLQinQProviderVlanID = _BrzaccVLQinQProviderVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7, 2),
    _BrzaccVLQinQProviderVlanID_Type()
)
brzaccVLQinQProviderVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLQinQProviderVlanID.setStatus("current")
_BrzaccVLVlanExtendedAccessRulesTable_Object = MibTable
brzaccVLVlanExtendedAccessRulesTable = _BrzaccVLVlanExtendedAccessRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRulesTable.setStatus("current")
_BrzaccVLVlanExtendedAccessRulesEntry_Object = MibTableRow
brzaccVLVlanExtendedAccessRulesEntry = _BrzaccVLVlanExtendedAccessRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1)
)
brzaccVLVlanExtendedAccessRulesEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLVlanExtendedAccessRulesTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRulesEntry.setStatus("current")


class _BrzaccVLVlanExtendedAccessRulesTableIdx_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRulesTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLVlanExtendedAccessRulesTableIdx_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRulesTableIdx_Object = MibTableColumn
brzaccVLVlanExtendedAccessRulesTableIdx = _BrzaccVLVlanExtendedAccessRulesTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 1),
    _BrzaccVLVlanExtendedAccessRulesTableIdx_Type()
)
brzaccVLVlanExtendedAccessRulesTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRulesTableIdx.setStatus("current")


class _BrzaccVLVlanExtendedAccessRuleId_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRuleId based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("default", 11),
          ("destinationIpAddress", 5),
          ("destinationMacAddress", 3),
          ("destinationTcpPort", 9),
          ("destinationUdpPort", 7),
          ("ipProtocol", 10),
          ("noRule", 1),
          ("sourceIpAddress", 4),
          ("sourceMacAddress", 2),
          ("sourceTcpPort", 8),
          ("sourceUdpPort", 6))
    )


_BrzaccVLVlanExtendedAccessRuleId_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRuleId_Object = MibTableColumn
brzaccVLVlanExtendedAccessRuleId = _BrzaccVLVlanExtendedAccessRuleId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 2),
    _BrzaccVLVlanExtendedAccessRuleId_Type()
)
brzaccVLVlanExtendedAccessRuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRuleId.setStatus("current")


class _BrzaccVLVlanExtendedAccessRuleVlanId_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BrzaccVLVlanExtendedAccessRuleVlanId_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRuleVlanId_Object = MibTableColumn
brzaccVLVlanExtendedAccessRuleVlanId = _BrzaccVLVlanExtendedAccessRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 3),
    _BrzaccVLVlanExtendedAccessRuleVlanId_Type()
)
brzaccVLVlanExtendedAccessRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRuleVlanId.setStatus("current")


class _BrzaccVLVlanExtendedAccessRulePriority_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLVlanExtendedAccessRulePriority_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRulePriority_Object = MibTableColumn
brzaccVLVlanExtendedAccessRulePriority = _BrzaccVLVlanExtendedAccessRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 4),
    _BrzaccVLVlanExtendedAccessRulePriority_Type()
)
brzaccVLVlanExtendedAccessRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRulePriority.setStatus("current")


class _BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRuleMulticastAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("na", 255),
          ("notAllowed", 2))
    )


_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Object = MibTableColumn
brzaccVLVlanExtendedAccessRuleMulticastAllowed = _BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 5),
    _BrzaccVLVlanExtendedAccessRuleMulticastAllowed_Type()
)
brzaccVLVlanExtendedAccessRuleMulticastAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRuleMulticastAllowed.setStatus("current")


class _BrzaccVLVlanExtendedAccessRuleOpType_Type(Integer32):
    """Custom type brzaccVLVlanExtendedAccessRuleOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enumeration", 4),
          ("mask", 3),
          ("na", 255),
          ("range", 2),
          ("value", 1))
    )


_BrzaccVLVlanExtendedAccessRuleOpType_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedAccessRuleOpType_Object = MibTableColumn
brzaccVLVlanExtendedAccessRuleOpType = _BrzaccVLVlanExtendedAccessRuleOpType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 6),
    _BrzaccVLVlanExtendedAccessRuleOpType_Type()
)
brzaccVLVlanExtendedAccessRuleOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRuleOpType.setStatus("current")


class _BrzaccVLVlanExtendedAccessRuleOperands_Type(DisplayString):
    """Custom type brzaccVLVlanExtendedAccessRuleOperands based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BrzaccVLVlanExtendedAccessRuleOperands_Type.__name__ = "DisplayString"
_BrzaccVLVlanExtendedAccessRuleOperands_Object = MibTableColumn
brzaccVLVlanExtendedAccessRuleOperands = _BrzaccVLVlanExtendedAccessRuleOperands_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 8, 1, 7),
    _BrzaccVLVlanExtendedAccessRuleOperands_Type()
)
brzaccVLVlanExtendedAccessRuleOperands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedAccessRuleOperands.setStatus("current")


class _BrzaccVLVlanExtendedTrunkVlanID_Type(Integer32):
    """Custom type brzaccVLVlanExtendedTrunkVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BrzaccVLVlanExtendedTrunkVlanID_Type.__name__ = "Integer32"
_BrzaccVLVlanExtendedTrunkVlanID_Object = MibScalar
brzaccVLVlanExtendedTrunkVlanID = _BrzaccVLVlanExtendedTrunkVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 9),
    _BrzaccVLVlanExtendedTrunkVlanID_Type()
)
brzaccVLVlanExtendedTrunkVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVlanExtendedTrunkVlanID.setStatus("current")
_BrzaccVLBridgeAgingTime_Type = Integer32
_BrzaccVLBridgeAgingTime_Object = MibScalar
brzaccVLBridgeAgingTime = _BrzaccVLBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 2),
    _BrzaccVLBridgeAgingTime_Type()
)
brzaccVLBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBridgeAgingTime.setStatus("current")


class _BrzaccVLBroadcastRelaying_Type(Integer32):
    """Custom type brzaccVLBroadcastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcastEnable", 3),
          ("broadcastMulticastEnable", 2),
          ("disable", 1),
          ("multicastEnable", 4),
          ("na", 255))
    )


_BrzaccVLBroadcastRelaying_Type.__name__ = "Integer32"
_BrzaccVLBroadcastRelaying_Object = MibScalar
brzaccVLBroadcastRelaying = _BrzaccVLBroadcastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 4),
    _BrzaccVLBroadcastRelaying_Type()
)
brzaccVLBroadcastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBroadcastRelaying.setStatus("current")


class _BrzaccVLUnicastRelaying_Type(Integer32):
    """Custom type brzaccVLUnicastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLUnicastRelaying_Type.__name__ = "Integer32"
_BrzaccVLUnicastRelaying_Object = MibScalar
brzaccVLUnicastRelaying = _BrzaccVLUnicastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 5),
    _BrzaccVLUnicastRelaying_Type()
)
brzaccVLUnicastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUnicastRelaying.setStatus("current")


class _BrzaccVLEthBroadcastFiltering_Type(Integer32):
    """Custom type brzaccVLEthBroadcastFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("na", 255),
          ("onBothWirelessAndEthernet", 4),
          ("onEthernetOnly", 2),
          ("onWirelessOnly", 3))
    )


_BrzaccVLEthBroadcastFiltering_Type.__name__ = "Integer32"
_BrzaccVLEthBroadcastFiltering_Object = MibScalar
brzaccVLEthBroadcastFiltering = _BrzaccVLEthBroadcastFiltering_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 6),
    _BrzaccVLEthBroadcastFiltering_Type()
)
brzaccVLEthBroadcastFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastFiltering.setStatus("current")
_BrzaccVLEthBroadcastingParameters_ObjectIdentity = ObjectIdentity
brzaccVLEthBroadcastingParameters = _BrzaccVLEthBroadcastingParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7)
)


class _BrzaccVLDHCPBroadcastOverrideFilter_Type(Integer32):
    """Custom type brzaccVLDHCPBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDHCPBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BrzaccVLDHCPBroadcastOverrideFilter_Object = MibScalar
brzaccVLDHCPBroadcastOverrideFilter = _BrzaccVLDHCPBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 1),
    _BrzaccVLDHCPBroadcastOverrideFilter_Type()
)
brzaccVLDHCPBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDHCPBroadcastOverrideFilter.setStatus("current")


class _BrzaccVLPPPoEBroadcastOverrideFilter_Type(Integer32):
    """Custom type brzaccVLPPPoEBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLPPPoEBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BrzaccVLPPPoEBroadcastOverrideFilter_Object = MibScalar
brzaccVLPPPoEBroadcastOverrideFilter = _BrzaccVLPPPoEBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 2),
    _BrzaccVLPPPoEBroadcastOverrideFilter_Type()
)
brzaccVLPPPoEBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLPPPoEBroadcastOverrideFilter.setStatus("current")


class _BrzaccVLARPBroadcastOverrideFilter_Type(Integer32):
    """Custom type brzaccVLARPBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLARPBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BrzaccVLARPBroadcastOverrideFilter_Object = MibScalar
brzaccVLARPBroadcastOverrideFilter = _BrzaccVLARPBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 3),
    _BrzaccVLARPBroadcastOverrideFilter_Type()
)
brzaccVLARPBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLARPBroadcastOverrideFilter.setStatus("current")


class _BrzaccVLEthBroadcastMulticastLimiterOption_Type(Integer32):
    """Custom type brzaccVLEthBroadcastMulticastLimiterOption based on Integer32"""
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
        *(("disable", 1),
          ("limitAllMulticasts", 4),
          ("limitMulticastsExceptBroadcasts", 3),
          ("limitOnlyBroadcasts", 2))
    )


_BrzaccVLEthBroadcastMulticastLimiterOption_Type.__name__ = "Integer32"
_BrzaccVLEthBroadcastMulticastLimiterOption_Object = MibScalar
brzaccVLEthBroadcastMulticastLimiterOption = _BrzaccVLEthBroadcastMulticastLimiterOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 4),
    _BrzaccVLEthBroadcastMulticastLimiterOption_Type()
)
brzaccVLEthBroadcastMulticastLimiterOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastMulticastLimiterOption.setStatus("current")
_BrzaccVLEthBroadcastMulticastLimiterThreshold_Type = Integer32
_BrzaccVLEthBroadcastMulticastLimiterThreshold_Object = MibScalar
brzaccVLEthBroadcastMulticastLimiterThreshold = _BrzaccVLEthBroadcastMulticastLimiterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 5),
    _BrzaccVLEthBroadcastMulticastLimiterThreshold_Type()
)
brzaccVLEthBroadcastMulticastLimiterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastMulticastLimiterThreshold.setStatus("current")
_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Type = Integer32
_BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Object = MibScalar
brzaccVLEthBroadcastMulticastLimiterSendTrapInterval = _BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 6),
    _BrzaccVLEthBroadcastMulticastLimiterSendTrapInterval_Type()
)
brzaccVLEthBroadcastMulticastLimiterSendTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastMulticastLimiterSendTrapInterval.setStatus("current")
_BrzaccVLToSPriorityParameters_ObjectIdentity = ObjectIdentity
brzaccVLToSPriorityParameters = _BrzaccVLToSPriorityParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 8)
)
_BrzaccVLToSPrecedenceThreshold_Type = Integer32
_BrzaccVLToSPrecedenceThreshold_Object = MibScalar
brzaccVLToSPrecedenceThreshold = _BrzaccVLToSPrecedenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 8, 1),
    _BrzaccVLToSPrecedenceThreshold_Type()
)
brzaccVLToSPrecedenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLToSPrecedenceThreshold.setStatus("current")


class _BrzaccVLRoamingOption_Type(Integer32):
    """Custom type brzaccVLRoamingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLRoamingOption_Type.__name__ = "Integer32"
_BrzaccVLRoamingOption_Object = MibScalar
brzaccVLRoamingOption = _BrzaccVLRoamingOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 9),
    _BrzaccVLRoamingOption_Type()
)
brzaccVLRoamingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLRoamingOption.setStatus("current")
_BrzaccVLMacAddressDenyList_ObjectIdentity = ObjectIdentity
brzaccVLMacAddressDenyList = _BrzaccVLMacAddressDenyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10)
)
_BrzaccVLMacAddressDenyListTable_Object = MibTable
brzaccVLMacAddressDenyListTable = _BrzaccVLMacAddressDenyListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1)
)
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListTable.setStatus("current")
_BrzaccVLMacAddressDenyListEntry_Object = MibTableRow
brzaccVLMacAddressDenyListEntry = _BrzaccVLMacAddressDenyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1)
)
brzaccVLMacAddressDenyListEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLMacAddressDenyListTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListEntry.setStatus("current")


class _BrzaccVLMacAddressDenyListTableIdx_Type(Integer32):
    """Custom type brzaccVLMacAddressDenyListTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BrzaccVLMacAddressDenyListTableIdx_Type.__name__ = "Integer32"
_BrzaccVLMacAddressDenyListTableIdx_Object = MibTableColumn
brzaccVLMacAddressDenyListTableIdx = _BrzaccVLMacAddressDenyListTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1, 1),
    _BrzaccVLMacAddressDenyListTableIdx_Type()
)
brzaccVLMacAddressDenyListTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListTableIdx.setStatus("current")
_BrzaccVLMacAddressDenyListId_Type = MacAddress
_BrzaccVLMacAddressDenyListId_Object = MibTableColumn
brzaccVLMacAddressDenyListId = _BrzaccVLMacAddressDenyListId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1, 2),
    _BrzaccVLMacAddressDenyListId_Type()
)
brzaccVLMacAddressDenyListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListId.setStatus("current")
_BrzaccVLMacAddressDenyListAdd_Type = MacAddress
_BrzaccVLMacAddressDenyListAdd_Object = MibScalar
brzaccVLMacAddressDenyListAdd = _BrzaccVLMacAddressDenyListAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 2),
    _BrzaccVLMacAddressDenyListAdd_Type()
)
brzaccVLMacAddressDenyListAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListAdd.setStatus("current")
_BrzaccVLMacAddressDenyListRemove_Type = MacAddress
_BrzaccVLMacAddressDenyListRemove_Object = MibScalar
brzaccVLMacAddressDenyListRemove = _BrzaccVLMacAddressDenyListRemove_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 3),
    _BrzaccVLMacAddressDenyListRemove_Type()
)
brzaccVLMacAddressDenyListRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListRemove.setStatus("current")


class _BrzaccVLNumberOfMacAddressesInDenyList_Type(Integer32):
    """Custom type brzaccVLNumberOfMacAddressesInDenyList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLNumberOfMacAddressesInDenyList_Type.__name__ = "Integer32"
_BrzaccVLNumberOfMacAddressesInDenyList_Object = MibScalar
brzaccVLNumberOfMacAddressesInDenyList = _BrzaccVLNumberOfMacAddressesInDenyList_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 4),
    _BrzaccVLNumberOfMacAddressesInDenyList_Type()
)
brzaccVLNumberOfMacAddressesInDenyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNumberOfMacAddressesInDenyList.setStatus("current")


class _BrzaccVLMacAddressDenyListAction_Type(Integer32):
    """Custom type brzaccVLMacAddressDenyListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allowedList", 2),
          ("denyList", 1),
          ("na", 255))
    )


_BrzaccVLMacAddressDenyListAction_Type.__name__ = "Integer32"
_BrzaccVLMacAddressDenyListAction_Object = MibScalar
brzaccVLMacAddressDenyListAction = _BrzaccVLMacAddressDenyListAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 5),
    _BrzaccVLMacAddressDenyListAction_Type()
)
brzaccVLMacAddressDenyListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMacAddressDenyListAction.setStatus("current")
_BrzaccVLNewMacAddressDenyListTable_Object = MibTable
brzaccVLNewMacAddressDenyListTable = _BrzaccVLNewMacAddressDenyListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 6)
)
if mibBuilder.loadTexts:
    brzaccVLNewMacAddressDenyListTable.setStatus("current")
_BrzaccVLNewMacAddressDenyListEntry_Object = MibTableRow
brzaccVLNewMacAddressDenyListEntry = _BrzaccVLNewMacAddressDenyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 6, 1)
)
brzaccVLNewMacAddressDenyListEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewMacAddressDenyListId"),
)
if mibBuilder.loadTexts:
    brzaccVLNewMacAddressDenyListEntry.setStatus("current")
_BrzaccVLNewMacAddressDenyListId_Type = MacAddress
_BrzaccVLNewMacAddressDenyListId_Object = MibTableColumn
brzaccVLNewMacAddressDenyListId = _BrzaccVLNewMacAddressDenyListId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 6, 1, 1),
    _BrzaccVLNewMacAddressDenyListId_Type()
)
brzaccVLNewMacAddressDenyListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewMacAddressDenyListId.setStatus("current")


class _BrzaccVLNewMacAddressDenyListCommand_Type(Integer32):
    """Custom type brzaccVLNewMacAddressDenyListCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewMacAddressDenyListCommand_Type.__name__ = "Integer32"
_BrzaccVLNewMacAddressDenyListCommand_Object = MibTableColumn
brzaccVLNewMacAddressDenyListCommand = _BrzaccVLNewMacAddressDenyListCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 6, 1, 2),
    _BrzaccVLNewMacAddressDenyListCommand_Type()
)
brzaccVLNewMacAddressDenyListCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMacAddressDenyListCommand.setStatus("current")
_BrzAccVLPortsControl_ObjectIdentity = ObjectIdentity
brzAccVLPortsControl = _BrzAccVLPortsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 11)
)


class _BrzaccVLEthernetPortControl_Type(Integer32):
    """Custom type brzaccVLEthernetPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLEthernetPortControl_Type.__name__ = "Integer32"
_BrzaccVLEthernetPortControl_Object = MibScalar
brzaccVLEthernetPortControl = _BrzaccVLEthernetPortControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 11, 1),
    _BrzaccVLEthernetPortControl_Type()
)
brzaccVLEthernetPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthernetPortControl.setStatus("current")


class _BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type(Integer32):
    """Custom type brzaccVLSendBroadcastsMulticastsAsUnicasts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type.__name__ = "Integer32"
_BrzaccVLSendBroadcastsMulticastsAsUnicasts_Object = MibScalar
brzaccVLSendBroadcastsMulticastsAsUnicasts = _BrzaccVLSendBroadcastsMulticastsAsUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 12),
    _BrzaccVLSendBroadcastsMulticastsAsUnicasts_Type()
)
brzaccVLSendBroadcastsMulticastsAsUnicasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSendBroadcastsMulticastsAsUnicasts.setStatus("current")
_BrzaccVLAirInterface_ObjectIdentity = ObjectIdentity
brzaccVLAirInterface = _BrzaccVLAirInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6)
)
_BrzaccVLESSIDParameters_ObjectIdentity = ObjectIdentity
brzaccVLESSIDParameters = _BrzaccVLESSIDParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1)
)


class _BrzaccVLESSID_Type(DisplayString):
    """Custom type brzaccVLESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BrzaccVLESSID_Type.__name__ = "DisplayString"
_BrzaccVLESSID_Object = MibScalar
brzaccVLESSID = _BrzaccVLESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 1),
    _BrzaccVLESSID_Type()
)
brzaccVLESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLESSID.setStatus("current")


class _BrzaccVLOperatorESSIDOption_Type(Integer32):
    """Custom type brzaccVLOperatorESSIDOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLOperatorESSIDOption_Type.__name__ = "Integer32"
_BrzaccVLOperatorESSIDOption_Object = MibScalar
brzaccVLOperatorESSIDOption = _BrzaccVLOperatorESSIDOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 2),
    _BrzaccVLOperatorESSIDOption_Type()
)
brzaccVLOperatorESSIDOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLOperatorESSIDOption.setStatus("current")


class _BrzaccVLOperatorESSID_Type(DisplayString):
    """Custom type brzaccVLOperatorESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BrzaccVLOperatorESSID_Type.__name__ = "DisplayString"
_BrzaccVLOperatorESSID_Object = MibScalar
brzaccVLOperatorESSID = _BrzaccVLOperatorESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 3),
    _BrzaccVLOperatorESSID_Type()
)
brzaccVLOperatorESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLOperatorESSID.setStatus("current")


class _BrzaccVLRunTimeESSID_Type(DisplayString):
    """Custom type brzaccVLRunTimeESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_BrzaccVLRunTimeESSID_Type.__name__ = "DisplayString"
_BrzaccVLRunTimeESSID_Object = MibScalar
brzaccVLRunTimeESSID = _BrzaccVLRunTimeESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 4),
    _BrzaccVLRunTimeESSID_Type()
)
brzaccVLRunTimeESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunTimeESSID.setStatus("current")
_BrzaccVLHiddenESSIDParameters_ObjectIdentity = ObjectIdentity
brzaccVLHiddenESSIDParameters = _BrzaccVLHiddenESSIDParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 5)
)


class _BrzaccVLAUHiddenESSIDOption_Type(Integer32):
    """Custom type brzaccVLAUHiddenESSIDOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("na", 255))
    )


_BrzaccVLAUHiddenESSIDOption_Type.__name__ = "Integer32"
_BrzaccVLAUHiddenESSIDOption_Object = MibScalar
brzaccVLAUHiddenESSIDOption = _BrzaccVLAUHiddenESSIDOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 5, 1),
    _BrzaccVLAUHiddenESSIDOption_Type()
)
brzaccVLAUHiddenESSIDOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUHiddenESSIDOption.setStatus("current")


class _BrzaccVLSUHiddenESSIDSupport_Type(Integer32):
    """Custom type brzaccVLSUHiddenESSIDSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("na", 255))
    )


_BrzaccVLSUHiddenESSIDSupport_Type.__name__ = "Integer32"
_BrzaccVLSUHiddenESSIDSupport_Object = MibScalar
brzaccVLSUHiddenESSIDSupport = _BrzaccVLSUHiddenESSIDSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 5, 2),
    _BrzaccVLSUHiddenESSIDSupport_Type()
)
brzaccVLSUHiddenESSIDSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUHiddenESSIDSupport.setStatus("current")


class _BrzaccVLSUHiddenESSIDTimeout_Type(Integer32):
    """Custom type brzaccVLSUHiddenESSIDTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_BrzaccVLSUHiddenESSIDTimeout_Type.__name__ = "Integer32"
_BrzaccVLSUHiddenESSIDTimeout_Object = MibScalar
brzaccVLSUHiddenESSIDTimeout = _BrzaccVLSUHiddenESSIDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 5, 3),
    _BrzaccVLSUHiddenESSIDTimeout_Type()
)
brzaccVLSUHiddenESSIDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUHiddenESSIDTimeout.setStatus("current")
_BrzaccVLMaximumCellRadius_Type = Integer32
_BrzaccVLMaximumCellRadius_Object = MibScalar
brzaccVLMaximumCellRadius = _BrzaccVLMaximumCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 2),
    _BrzaccVLMaximumCellRadius_Type()
)
brzaccVLMaximumCellRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaximumCellRadius.setStatus("current")


class _BrzaccVLAIFS_Type(Integer32):
    """Custom type brzaccVLAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_BrzaccVLAIFS_Type.__name__ = "Integer32"
_BrzaccVLAIFS_Object = MibScalar
brzaccVLAIFS = _BrzaccVLAIFS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 3),
    _BrzaccVLAIFS_Type()
)
brzaccVLAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAIFS.setStatus("current")
_BrzaccVLWirelessTrapThreshold_Type = Integer32
_BrzaccVLWirelessTrapThreshold_Object = MibScalar
brzaccVLWirelessTrapThreshold = _BrzaccVLWirelessTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 4),
    _BrzaccVLWirelessTrapThreshold_Type()
)
brzaccVLWirelessTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLWirelessTrapThreshold.setStatus("current")
_BrzaccVLTransmitPowerTable_Object = MibTable
brzaccVLTransmitPowerTable = _BrzaccVLTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    brzaccVLTransmitPowerTable.setStatus("current")
_BrzaccVLTransmitPowerEntry_Object = MibTableRow
brzaccVLTransmitPowerEntry = _BrzaccVLTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1)
)
brzaccVLTransmitPowerEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLTransmitPowerIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLTransmitPowerEntry.setStatus("current")


class _BrzaccVLTransmitPowerIdx_Type(Integer32):
    """Custom type brzaccVLTransmitPowerIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrzaccVLTransmitPowerIdx_Type.__name__ = "Integer32"
_BrzaccVLTransmitPowerIdx_Object = MibTableColumn
brzaccVLTransmitPowerIdx = _BrzaccVLTransmitPowerIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 1),
    _BrzaccVLTransmitPowerIdx_Type()
)
brzaccVLTransmitPowerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTransmitPowerIdx.setStatus("current")


class _BrzaccVLApplicableModulationLevel_Type(Integer32):
    """Custom type brzaccVLApplicableModulationLevel based on Integer32"""
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
        *(("level1to5", 1),
          ("level6", 2),
          ("level7", 3),
          ("level8", 4))
    )


_BrzaccVLApplicableModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLApplicableModulationLevel_Object = MibTableColumn
brzaccVLApplicableModulationLevel = _BrzaccVLApplicableModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 2),
    _BrzaccVLApplicableModulationLevel_Type()
)
brzaccVLApplicableModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLApplicableModulationLevel.setStatus("current")
_BrzaccVLMaximumTxPowerRange_Type = DisplayString
_BrzaccVLMaximumTxPowerRange_Object = MibTableColumn
brzaccVLMaximumTxPowerRange = _BrzaccVLMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 3),
    _BrzaccVLMaximumTxPowerRange_Type()
)
brzaccVLMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaximumTxPowerRange.setStatus("current")
_BrzaccVLTxPower_Type = DisplayString
_BrzaccVLTxPower_Object = MibTableColumn
brzaccVLTxPower = _BrzaccVLTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 4),
    _BrzaccVLTxPower_Type()
)
brzaccVLTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTxPower.setStatus("current")
_BrzaccVLCurrentTxPower_Type = DisplayString
_BrzaccVLCurrentTxPower_Object = MibTableColumn
brzaccVLCurrentTxPower = _BrzaccVLCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 5),
    _BrzaccVLCurrentTxPower_Type()
)
brzaccVLCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentTxPower.setStatus("current")
_BrzaccVLMaximumTransmitPowerTable_Object = MibTable
brzaccVLMaximumTransmitPowerTable = _BrzaccVLMaximumTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    brzaccVLMaximumTransmitPowerTable.setStatus("current")
_BrzaccVLMaximumTransmitPowerEntry_Object = MibTableRow
brzaccVLMaximumTransmitPowerEntry = _BrzaccVLMaximumTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1)
)
brzaccVLMaximumTransmitPowerEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLMaximumTransmitPowerIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLMaximumTransmitPowerEntry.setStatus("current")


class _BrzaccVLMaximumTransmitPowerIdx_Type(Integer32):
    """Custom type brzaccVLMaximumTransmitPowerIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BrzaccVLMaximumTransmitPowerIdx_Type.__name__ = "Integer32"
_BrzaccVLMaximumTransmitPowerIdx_Object = MibTableColumn
brzaccVLMaximumTransmitPowerIdx = _BrzaccVLMaximumTransmitPowerIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 1),
    _BrzaccVLMaximumTransmitPowerIdx_Type()
)
brzaccVLMaximumTransmitPowerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaximumTransmitPowerIdx.setStatus("current")


class _BrzaccVLMaxTxApplicableModulationLevel_Type(Integer32):
    """Custom type brzaccVLMaxTxApplicableModulationLevel based on Integer32"""
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
        *(("level1to5", 1),
          ("level6", 2),
          ("level7", 3),
          ("level8", 4))
    )


_BrzaccVLMaxTxApplicableModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLMaxTxApplicableModulationLevel_Object = MibTableColumn
brzaccVLMaxTxApplicableModulationLevel = _BrzaccVLMaxTxApplicableModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 2),
    _BrzaccVLMaxTxApplicableModulationLevel_Type()
)
brzaccVLMaxTxApplicableModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaxTxApplicableModulationLevel.setStatus("current")
_BrzaccVLDefinedMaximumTxPowerRange_Type = DisplayString
_BrzaccVLDefinedMaximumTxPowerRange_Object = MibTableColumn
brzaccVLDefinedMaximumTxPowerRange = _BrzaccVLDefinedMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 3),
    _BrzaccVLDefinedMaximumTxPowerRange_Type()
)
brzaccVLDefinedMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDefinedMaximumTxPowerRange.setStatus("current")
_BrzaccVLMaxTxPower_Type = DisplayString
_BrzaccVLMaxTxPower_Object = MibTableColumn
brzaccVLMaxTxPower = _BrzaccVLMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 4),
    _BrzaccVLMaxTxPower_Type()
)
brzaccVLMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxTxPower.setStatus("current")
_BrzaccVLMaxNumOfAssociations_Type = Integer32
_BrzaccVLMaxNumOfAssociations_Object = MibScalar
brzaccVLMaxNumOfAssociations = _BrzaccVLMaxNumOfAssociations_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 10),
    _BrzaccVLMaxNumOfAssociations_Type()
)
brzaccVLMaxNumOfAssociations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxNumOfAssociations.setStatus("current")
_BrzaccVLBestAu_ObjectIdentity = ObjectIdentity
brzaccVLBestAu = _BrzaccVLBestAu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11)
)


class _BrzaccVLBestAuSupport_Type(Integer32):
    """Custom type brzaccVLBestAuSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLBestAuSupport_Type.__name__ = "Integer32"
_BrzaccVLBestAuSupport_Object = MibScalar
brzaccVLBestAuSupport = _BrzaccVLBestAuSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 1),
    _BrzaccVLBestAuSupport_Type()
)
brzaccVLBestAuSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBestAuSupport.setStatus("current")
_BrzaccVLBestAuNoOfScanningAttempts_Type = Integer32
_BrzaccVLBestAuNoOfScanningAttempts_Object = MibScalar
brzaccVLBestAuNoOfScanningAttempts = _BrzaccVLBestAuNoOfScanningAttempts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 2),
    _BrzaccVLBestAuNoOfScanningAttempts_Type()
)
brzaccVLBestAuNoOfScanningAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBestAuNoOfScanningAttempts.setStatus("current")
_BrzaccVLPreferredAuMacAddress_Type = MacAddress
_BrzaccVLPreferredAuMacAddress_Object = MibScalar
brzaccVLPreferredAuMacAddress = _BrzaccVLPreferredAuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 3),
    _BrzaccVLPreferredAuMacAddress_Type()
)
brzaccVLPreferredAuMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLPreferredAuMacAddress.setStatus("current")
_BrzaccVLNeighborAuTable_Object = MibTable
brzaccVLNeighborAuTable = _BrzaccVLNeighborAuTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4)
)
if mibBuilder.loadTexts:
    brzaccVLNeighborAuTable.setStatus("current")
_BrzaccVLNeighborAuEntry_Object = MibTableRow
brzaccVLNeighborAuEntry = _BrzaccVLNeighborAuEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1)
)
brzaccVLNeighborAuEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNeighborAuIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLNeighborAuEntry.setStatus("current")


class _BrzaccVLNeighborAuIdx_Type(Integer32):
    """Custom type brzaccVLNeighborAuIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BrzaccVLNeighborAuIdx_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuIdx_Object = MibTableColumn
brzaccVLNeighborAuIdx = _BrzaccVLNeighborAuIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 1),
    _BrzaccVLNeighborAuIdx_Type()
)
brzaccVLNeighborAuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuIdx.setStatus("current")
_BrzaccVLNeighborAuMacAdd_Type = MacAddress
_BrzaccVLNeighborAuMacAdd_Object = MibTableColumn
brzaccVLNeighborAuMacAdd = _BrzaccVLNeighborAuMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 2),
    _BrzaccVLNeighborAuMacAdd_Type()
)
brzaccVLNeighborAuMacAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuMacAdd.setStatus("current")
_BrzaccVLNeighborAuESSID_Type = DisplayString
_BrzaccVLNeighborAuESSID_Object = MibTableColumn
brzaccVLNeighborAuESSID = _BrzaccVLNeighborAuESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 3),
    _BrzaccVLNeighborAuESSID_Type()
)
brzaccVLNeighborAuESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuESSID.setStatus("current")


class _BrzaccVLNeighborAuSNR_Type(Integer32):
    """Custom type brzaccVLNeighborAuSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLNeighborAuSNR_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuSNR_Object = MibTableColumn
brzaccVLNeighborAuSNR = _BrzaccVLNeighborAuSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 4),
    _BrzaccVLNeighborAuSNR_Type()
)
brzaccVLNeighborAuSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuSNR.setStatus("current")


class _BrzaccVLNeighborAuAssocLoadStatus_Type(Integer32):
    """Custom type brzaccVLNeighborAuAssocLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("na", 255),
          ("notFull", 2))
    )


_BrzaccVLNeighborAuAssocLoadStatus_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuAssocLoadStatus_Object = MibTableColumn
brzaccVLNeighborAuAssocLoadStatus = _BrzaccVLNeighborAuAssocLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 5),
    _BrzaccVLNeighborAuAssocLoadStatus_Type()
)
brzaccVLNeighborAuAssocLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuAssocLoadStatus.setStatus("current")
_BrzaccVLNeighborAuMark_Type = Integer32
_BrzaccVLNeighborAuMark_Object = MibTableColumn
brzaccVLNeighborAuMark = _BrzaccVLNeighborAuMark_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 6),
    _BrzaccVLNeighborAuMark_Type()
)
brzaccVLNeighborAuMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuMark.setStatus("current")


class _BrzaccVLNeighborAuHwRevision_Type(Integer32):
    """Custom type brzaccVLNeighborAuHwRevision based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("hwRevisionF", 6),
          ("hwRevisionG", 7),
          ("na", 255))
    )


_BrzaccVLNeighborAuHwRevision_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuHwRevision_Object = MibTableColumn
brzaccVLNeighborAuHwRevision = _BrzaccVLNeighborAuHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 7),
    _BrzaccVLNeighborAuHwRevision_Type()
)
brzaccVLNeighborAuHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuHwRevision.setStatus("current")
_BrzaccVLNeighborAuCountryCode_Type = Integer32
_BrzaccVLNeighborAuCountryCode_Object = MibTableColumn
brzaccVLNeighborAuCountryCode = _BrzaccVLNeighborAuCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 8),
    _BrzaccVLNeighborAuCountryCode_Type()
)
brzaccVLNeighborAuCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuCountryCode.setStatus("current")
_BrzaccVLNeighborAuSwVer_Type = DisplayString
_BrzaccVLNeighborAuSwVer_Object = MibTableColumn
brzaccVLNeighborAuSwVer = _BrzaccVLNeighborAuSwVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 9),
    _BrzaccVLNeighborAuSwVer_Type()
)
brzaccVLNeighborAuSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuSwVer.setStatus("current")


class _BrzaccVLNeighborAuAtpcOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuAtpcOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuAtpcOption_Object = MibTableColumn
brzaccVLNeighborAuAtpcOption = _BrzaccVLNeighborAuAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 10),
    _BrzaccVLNeighborAuAtpcOption_Type()
)
brzaccVLNeighborAuAtpcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuAtpcOption.setStatus("current")


class _BrzaccVLNeighborAuAdapModOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuAdapModOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuAdapModOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuAdapModOption_Object = MibTableColumn
brzaccVLNeighborAuAdapModOption = _BrzaccVLNeighborAuAdapModOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 11),
    _BrzaccVLNeighborAuAdapModOption_Type()
)
brzaccVLNeighborAuAdapModOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuAdapModOption.setStatus("current")


class _BrzaccVLNeighborAuBurstModeOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuBurstModeOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuBurstModeOption_Object = MibTableColumn
brzaccVLNeighborAuBurstModeOption = _BrzaccVLNeighborAuBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 12),
    _BrzaccVLNeighborAuBurstModeOption_Type()
)
brzaccVLNeighborAuBurstModeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuBurstModeOption.setStatus("current")


class _BrzaccVLNeighborAuDfsOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuDfsOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuDfsOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuDfsOption_Object = MibTableColumn
brzaccVLNeighborAuDfsOption = _BrzaccVLNeighborAuDfsOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 14),
    _BrzaccVLNeighborAuDfsOption_Type()
)
brzaccVLNeighborAuDfsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuDfsOption.setStatus("current")


class _BrzaccVLNeighborAuConcatenationOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuConcatenationOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuConcatenationOption_Object = MibTableColumn
brzaccVLNeighborAuConcatenationOption = _BrzaccVLNeighborAuConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 15),
    _BrzaccVLNeighborAuConcatenationOption_Type()
)
brzaccVLNeighborAuConcatenationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuConcatenationOption.setStatus("current")


class _BrzaccVLNeighborAuLearnCountryCodeBySU_Type(Integer32):
    """Custom type brzaccVLNeighborAuLearnCountryCodeBySU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuLearnCountryCodeBySU_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuLearnCountryCodeBySU_Object = MibTableColumn
brzaccVLNeighborAuLearnCountryCodeBySU = _BrzaccVLNeighborAuLearnCountryCodeBySU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 17),
    _BrzaccVLNeighborAuLearnCountryCodeBySU_Type()
)
brzaccVLNeighborAuLearnCountryCodeBySU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuLearnCountryCodeBySU.setStatus("current")


class _BrzaccVLNeighborAuSecurityMode_Type(Integer32):
    """Custom type brzaccVLNeighborAuSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aesOCB", 2),
          ("fips197", 3),
          ("na", 255),
          ("wep", 1))
    )


_BrzaccVLNeighborAuSecurityMode_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuSecurityMode_Object = MibTableColumn
brzaccVLNeighborAuSecurityMode = _BrzaccVLNeighborAuSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 18),
    _BrzaccVLNeighborAuSecurityMode_Type()
)
brzaccVLNeighborAuSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuSecurityMode.setStatus("current")


class _BrzaccVLNeighborAuAuthOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuAuthOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("openSystem", 1),
          ("sharedKey", 2))
    )


_BrzaccVLNeighborAuAuthOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuAuthOption_Object = MibTableColumn
brzaccVLNeighborAuAuthOption = _BrzaccVLNeighborAuAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 19),
    _BrzaccVLNeighborAuAuthOption_Type()
)
brzaccVLNeighborAuAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuAuthOption.setStatus("current")


class _BrzaccVLNeighborAuDataEncyptOption_Type(Integer32):
    """Custom type brzaccVLNeighborAuDataEncyptOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuDataEncyptOption_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuDataEncyptOption_Object = MibTableColumn
brzaccVLNeighborAuDataEncyptOption = _BrzaccVLNeighborAuDataEncyptOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 20),
    _BrzaccVLNeighborAuDataEncyptOption_Type()
)
brzaccVLNeighborAuDataEncyptOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuDataEncyptOption.setStatus("current")


class _BrzaccVLNeighborAuPerSuDistanceLearning_Type(Integer32):
    """Custom type brzaccVLNeighborAuPerSuDistanceLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNeighborAuPerSuDistanceLearning_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuPerSuDistanceLearning_Object = MibTableColumn
brzaccVLNeighborAuPerSuDistanceLearning = _BrzaccVLNeighborAuPerSuDistanceLearning_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 21),
    _BrzaccVLNeighborAuPerSuDistanceLearning_Type()
)
brzaccVLNeighborAuPerSuDistanceLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuPerSuDistanceLearning.setStatus("current")


class _BrzaccVLNeighborAuRSSI_Type(Integer32):
    """Custom type brzaccVLNeighborAuRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLNeighborAuRSSI_Type.__name__ = "Integer32"
_BrzaccVLNeighborAuRSSI_Object = MibTableColumn
brzaccVLNeighborAuRSSI = _BrzaccVLNeighborAuRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 22),
    _BrzaccVLNeighborAuRSSI_Type()
)
brzaccVLNeighborAuRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNeighborAuRSSI.setStatus("current")
_BrzaccVLFrequencyDefinition_ObjectIdentity = ObjectIdentity
brzaccVLFrequencyDefinition = _BrzaccVLFrequencyDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12)
)
_BrzaccVLSubBandLowerFrequency_Type = Integer32
_BrzaccVLSubBandLowerFrequency_Object = MibScalar
brzaccVLSubBandLowerFrequency = _BrzaccVLSubBandLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 1),
    _BrzaccVLSubBandLowerFrequency_Type()
)
brzaccVLSubBandLowerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSubBandLowerFrequency.setStatus("obsolete")
_BrzaccVLSubBandUpperFrequency_Type = Integer32
_BrzaccVLSubBandUpperFrequency_Object = MibScalar
brzaccVLSubBandUpperFrequency = _BrzaccVLSubBandUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 2),
    _BrzaccVLSubBandUpperFrequency_Type()
)
brzaccVLSubBandUpperFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSubBandUpperFrequency.setStatus("obsolete")


class _BrzaccVLScanningStep_Type(Integer32):
    """Custom type brzaccVLScanningStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("khz-500", 4),
          ("mhz-1", 5),
          ("mhz-10", 2),
          ("mhz-20", 3),
          ("mhz-5", 1),
          ("na", 255))
    )


_BrzaccVLScanningStep_Type.__name__ = "Integer32"
_BrzaccVLScanningStep_Object = MibScalar
brzaccVLScanningStep = _BrzaccVLScanningStep_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 3),
    _BrzaccVLScanningStep_Type()
)
brzaccVLScanningStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLScanningStep.setStatus("current")
_BrzaccVLFrequencySubsetTable_Object = MibTable
brzaccVLFrequencySubsetTable = _BrzaccVLFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4)
)
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetTable.setStatus("current")
_BrzaccVLFrequencySubsetEntry_Object = MibTableRow
brzaccVLFrequencySubsetEntry = _BrzaccVLFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1)
)
brzaccVLFrequencySubsetEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLFrequencySubsetTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetEntry.setStatus("current")


class _BrzaccVLFrequencySubsetTableIdx_Type(Integer32):
    """Custom type brzaccVLFrequencySubsetTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BrzaccVLFrequencySubsetTableIdx_Type.__name__ = "Integer32"
_BrzaccVLFrequencySubsetTableIdx_Object = MibTableColumn
brzaccVLFrequencySubsetTableIdx = _BrzaccVLFrequencySubsetTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 1),
    _BrzaccVLFrequencySubsetTableIdx_Type()
)
brzaccVLFrequencySubsetTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetTableIdx.setStatus("current")
_BrzaccVLFrequencySubsetFrequency_Type = Integer32
_BrzaccVLFrequencySubsetFrequency_Object = MibTableColumn
brzaccVLFrequencySubsetFrequency = _BrzaccVLFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 2),
    _BrzaccVLFrequencySubsetFrequency_Type()
)
brzaccVLFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetFrequency.setStatus("current")


class _BrzaccVLFrequencySubsetActive_Type(Integer32):
    """Custom type brzaccVLFrequencySubsetActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_BrzaccVLFrequencySubsetActive_Type.__name__ = "Integer32"
_BrzaccVLFrequencySubsetActive_Object = MibTableColumn
brzaccVLFrequencySubsetActive = _BrzaccVLFrequencySubsetActive_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 3),
    _BrzaccVLFrequencySubsetActive_Type()
)
brzaccVLFrequencySubsetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetActive.setStatus("current")
_BrzaccVLFrequencySubsetFrequencyNew_Type = DisplayString
_BrzaccVLFrequencySubsetFrequencyNew_Object = MibTableColumn
brzaccVLFrequencySubsetFrequencyNew = _BrzaccVLFrequencySubsetFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 4),
    _BrzaccVLFrequencySubsetFrequencyNew_Type()
)
brzaccVLFrequencySubsetFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFrequencySubsetFrequencyNew.setStatus("current")


class _BrzaccVLSetSelectedFreqSubset_Type(Integer32):
    """Custom type brzaccVLSetSelectedFreqSubset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("setSelectedFreqsSubset", 1))
    )


_BrzaccVLSetSelectedFreqSubset_Type.__name__ = "Integer32"
_BrzaccVLSetSelectedFreqSubset_Object = MibScalar
brzaccVLSetSelectedFreqSubset = _BrzaccVLSetSelectedFreqSubset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 5),
    _BrzaccVLSetSelectedFreqSubset_Type()
)
brzaccVLSetSelectedFreqSubset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSetSelectedFreqSubset.setStatus("current")
_BrzaccVLCurrentFrequencySubsetTable_Object = MibTable
brzaccVLCurrentFrequencySubsetTable = _BrzaccVLCurrentFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6)
)
if mibBuilder.loadTexts:
    brzaccVLCurrentFrequencySubsetTable.setStatus("current")
_BrzaccVLCurrentFrequencySubsetEntry_Object = MibTableRow
brzaccVLCurrentFrequencySubsetEntry = _BrzaccVLCurrentFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1)
)
brzaccVLCurrentFrequencySubsetEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLCurrentFrequencySubsetTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLCurrentFrequencySubsetEntry.setStatus("current")


class _BrzaccVLCurrentFrequencySubsetTableIdx_Type(Integer32):
    """Custom type brzaccVLCurrentFrequencySubsetTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BrzaccVLCurrentFrequencySubsetTableIdx_Type.__name__ = "Integer32"
_BrzaccVLCurrentFrequencySubsetTableIdx_Object = MibTableColumn
brzaccVLCurrentFrequencySubsetTableIdx = _BrzaccVLCurrentFrequencySubsetTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 1),
    _BrzaccVLCurrentFrequencySubsetTableIdx_Type()
)
brzaccVLCurrentFrequencySubsetTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentFrequencySubsetTableIdx.setStatus("current")
_BrzaccVLCurrentFrequencySubsetFrequency_Type = Integer32
_BrzaccVLCurrentFrequencySubsetFrequency_Object = MibTableColumn
brzaccVLCurrentFrequencySubsetFrequency = _BrzaccVLCurrentFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 2),
    _BrzaccVLCurrentFrequencySubsetFrequency_Type()
)
brzaccVLCurrentFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentFrequencySubsetFrequency.setStatus("current")
_BrzaccVLCurrentFrequencySubsetFrequencyNew_Type = DisplayString
_BrzaccVLCurrentFrequencySubsetFrequencyNew_Object = MibTableColumn
brzaccVLCurrentFrequencySubsetFrequencyNew = _BrzaccVLCurrentFrequencySubsetFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 3),
    _BrzaccVLCurrentFrequencySubsetFrequencyNew_Type()
)
brzaccVLCurrentFrequencySubsetFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentFrequencySubsetFrequencyNew.setStatus("current")
_BrzaccVLCurrentAUOperatingFrequency_Type = Integer32
_BrzaccVLCurrentAUOperatingFrequency_Object = MibScalar
brzaccVLCurrentAUOperatingFrequency = _BrzaccVLCurrentAUOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 7),
    _BrzaccVLCurrentAUOperatingFrequency_Type()
)
brzaccVLCurrentAUOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentAUOperatingFrequency.setStatus("current")
_BrzaccVLAUDefinedFrequency_Type = Integer32
_BrzaccVLAUDefinedFrequency_Object = MibScalar
brzaccVLAUDefinedFrequency = _BrzaccVLAUDefinedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 8),
    _BrzaccVLAUDefinedFrequency_Type()
)
brzaccVLAUDefinedFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUDefinedFrequency.setStatus("current")
_BrzaccVLCurrentSUOperatingFrequency_Type = DisplayString
_BrzaccVLCurrentSUOperatingFrequency_Object = MibScalar
brzaccVLCurrentSUOperatingFrequency = _BrzaccVLCurrentSUOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 9),
    _BrzaccVLCurrentSUOperatingFrequency_Type()
)
brzaccVLCurrentSUOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentSUOperatingFrequency.setStatus("current")
_BrzaccVLSubBandSelect_ObjectIdentity = ObjectIdentity
brzaccVLSubBandSelect = _BrzaccVLSubBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 10)
)
_BrzaccVLSelectSubBandIndex_Type = Integer32
_BrzaccVLSelectSubBandIndex_Object = MibScalar
brzaccVLSelectSubBandIndex = _BrzaccVLSelectSubBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 10, 1),
    _BrzaccVLSelectSubBandIndex_Type()
)
brzaccVLSelectSubBandIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSelectSubBandIndex.setStatus("current")
_BrzaccVLDFSParameters_ObjectIdentity = ObjectIdentity
brzaccVLDFSParameters = _BrzaccVLDFSParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11)
)


class _BrzaccVLDFSOption_Type(Integer32):
    """Custom type brzaccVLDFSOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDFSOption_Type.__name__ = "Integer32"
_BrzaccVLDFSOption_Object = MibScalar
brzaccVLDFSOption = _BrzaccVLDFSOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 1),
    _BrzaccVLDFSOption_Type()
)
brzaccVLDFSOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSOption.setStatus("current")
_BrzaccVLDFSChannelCheckTime_Type = Integer32
_BrzaccVLDFSChannelCheckTime_Object = MibScalar
brzaccVLDFSChannelCheckTime = _BrzaccVLDFSChannelCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 3),
    _BrzaccVLDFSChannelCheckTime_Type()
)
brzaccVLDFSChannelCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelCheckTime.setStatus("current")
_BrzaccVLDFSChannelAvoidancePeriod_Type = Integer32
_BrzaccVLDFSChannelAvoidancePeriod_Object = MibScalar
brzaccVLDFSChannelAvoidancePeriod = _BrzaccVLDFSChannelAvoidancePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 4),
    _BrzaccVLDFSChannelAvoidancePeriod_Type()
)
brzaccVLDFSChannelAvoidancePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelAvoidancePeriod.setStatus("current")


class _BrzaccVLDFSSuWaitingOption_Type(Integer32):
    """Custom type brzaccVLDFSSuWaitingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDFSSuWaitingOption_Type.__name__ = "Integer32"
_BrzaccVLDFSSuWaitingOption_Object = MibScalar
brzaccVLDFSSuWaitingOption = _BrzaccVLDFSSuWaitingOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 5),
    _BrzaccVLDFSSuWaitingOption_Type()
)
brzaccVLDFSSuWaitingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSSuWaitingOption.setStatus("current")


class _BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type(Integer32):
    """Custom type brzaccVLDFSClearRadarDetectedChannelsAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("clearRadarChannels", 2),
          ("na", 255))
    )


_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type.__name__ = "Integer32"
_BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Object = MibScalar
brzaccVLDFSClearRadarDetectedChannelsAfterReset = _BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 6),
    _BrzaccVLDFSClearRadarDetectedChannelsAfterReset_Type()
)
brzaccVLDFSClearRadarDetectedChannelsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSClearRadarDetectedChannelsAfterReset.setStatus("current")
_BrzaccVLDFSRadarDetectionChannelsTable_Object = MibTable
brzaccVLDFSRadarDetectionChannelsTable = _BrzaccVLDFSRadarDetectionChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7)
)
if mibBuilder.loadTexts:
    brzaccVLDFSRadarDetectionChannelsTable.setStatus("current")
_BrzaccVLDFSRadarDetectionChannelsEntry_Object = MibTableRow
brzaccVLDFSRadarDetectionChannelsEntry = _BrzaccVLDFSRadarDetectionChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1)
)
brzaccVLDFSRadarDetectionChannelsEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLDFSChannelIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLDFSRadarDetectionChannelsEntry.setStatus("current")


class _BrzaccVLDFSChannelIdx_Type(Integer32):
    """Custom type brzaccVLDFSChannelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BrzaccVLDFSChannelIdx_Type.__name__ = "Integer32"
_BrzaccVLDFSChannelIdx_Object = MibTableColumn
brzaccVLDFSChannelIdx = _BrzaccVLDFSChannelIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 1),
    _BrzaccVLDFSChannelIdx_Type()
)
brzaccVLDFSChannelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelIdx.setStatus("current")
_BrzaccVLDFSChannelFrequency_Type = Integer32
_BrzaccVLDFSChannelFrequency_Object = MibTableColumn
brzaccVLDFSChannelFrequency = _BrzaccVLDFSChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 2),
    _BrzaccVLDFSChannelFrequency_Type()
)
brzaccVLDFSChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelFrequency.setStatus("current")


class _BrzaccVLDFSChannelRadarStatus_Type(Integer32):
    """Custom type brzaccVLDFSChannelRadarStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adjacentToRadar", 2),
          ("radarDetected", 3),
          ("radarFree", 1))
    )


_BrzaccVLDFSChannelRadarStatus_Type.__name__ = "Integer32"
_BrzaccVLDFSChannelRadarStatus_Object = MibTableColumn
brzaccVLDFSChannelRadarStatus = _BrzaccVLDFSChannelRadarStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 3),
    _BrzaccVLDFSChannelRadarStatus_Type()
)
brzaccVLDFSChannelRadarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelRadarStatus.setStatus("current")
_BrzaccVLDFSChannelFrequencyNew_Type = DisplayString
_BrzaccVLDFSChannelFrequencyNew_Object = MibTableColumn
brzaccVLDFSChannelFrequencyNew = _BrzaccVLDFSChannelFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 4),
    _BrzaccVLDFSChannelFrequencyNew_Type()
)
brzaccVLDFSChannelFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelFrequencyNew.setStatus("current")
_BrzaccVLDFSMinimumPulsesToDetect_Type = Integer32
_BrzaccVLDFSMinimumPulsesToDetect_Object = MibScalar
brzaccVLDFSMinimumPulsesToDetect = _BrzaccVLDFSMinimumPulsesToDetect_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 8),
    _BrzaccVLDFSMinimumPulsesToDetect_Type()
)
brzaccVLDFSMinimumPulsesToDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSMinimumPulsesToDetect.setStatus("current")
_BrzaccVLDFSChannelReuseParameters_ObjectIdentity = ObjectIdentity
brzaccVLDFSChannelReuseParameters = _BrzaccVLDFSChannelReuseParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9)
)


class _BrzaccVLDFSChannelReuseOption_Type(Integer32):
    """Custom type brzaccVLDFSChannelReuseOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDFSChannelReuseOption_Type.__name__ = "Integer32"
_BrzaccVLDFSChannelReuseOption_Object = MibScalar
brzaccVLDFSChannelReuseOption = _BrzaccVLDFSChannelReuseOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 1),
    _BrzaccVLDFSChannelReuseOption_Type()
)
brzaccVLDFSChannelReuseOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSChannelReuseOption.setStatus("current")
_BrzaccVLDFSRadarActivityAssessmentPeriod_Type = Integer32
_BrzaccVLDFSRadarActivityAssessmentPeriod_Object = MibScalar
brzaccVLDFSRadarActivityAssessmentPeriod = _BrzaccVLDFSRadarActivityAssessmentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 2),
    _BrzaccVLDFSRadarActivityAssessmentPeriod_Type()
)
brzaccVLDFSRadarActivityAssessmentPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSRadarActivityAssessmentPeriod.setStatus("current")
_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type = Integer32
_BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object = MibScalar
brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod = _BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 3),
    _BrzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type()
)
brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setStatus("current")


class _BrzaccVLDFSDetectionAlgorithm_Type(Integer32):
    """Custom type brzaccVLDFSDetectionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("etsi", 1),
          ("fcc", 2),
          ("na", 255))
    )


_BrzaccVLDFSDetectionAlgorithm_Type.__name__ = "Integer32"
_BrzaccVLDFSDetectionAlgorithm_Object = MibScalar
brzaccVLDFSDetectionAlgorithm = _BrzaccVLDFSDetectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 10),
    _BrzaccVLDFSDetectionAlgorithm_Type()
)
brzaccVLDFSDetectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSDetectionAlgorithm.setStatus("current")
_BrzaccVLDFSRemoteRadarEventReports_Type = Integer32
_BrzaccVLDFSRemoteRadarEventReports_Object = MibScalar
brzaccVLDFSRemoteRadarEventReports = _BrzaccVLDFSRemoteRadarEventReports_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 11),
    _BrzaccVLDFSRemoteRadarEventReports_Type()
)
brzaccVLDFSRemoteRadarEventReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSRemoteRadarEventReports.setStatus("current")
_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Type = Integer32
_BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Object = MibScalar
brzaccVLDFSRemoteRadarEventMonitoringPeriod = _BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 12),
    _BrzaccVLDFSRemoteRadarEventMonitoringPeriod_Type()
)
brzaccVLDFSRemoteRadarEventMonitoringPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDFSRemoteRadarEventMonitoringPeriod.setStatus("current")


class _BrzaccVLEnhancedETSIRadarDetection_Type(Integer32):
    """Custom type brzaccVLEnhancedETSIRadarDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrzaccVLEnhancedETSIRadarDetection_Type.__name__ = "Integer32"
_BrzaccVLEnhancedETSIRadarDetection_Object = MibScalar
brzaccVLEnhancedETSIRadarDetection = _BrzaccVLEnhancedETSIRadarDetection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 13),
    _BrzaccVLEnhancedETSIRadarDetection_Type()
)
brzaccVLEnhancedETSIRadarDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEnhancedETSIRadarDetection.setStatus("current")


class _BrzaccVLCountryCodeLearningBySU_Type(Integer32):
    """Custom type brzaccVLCountryCodeLearningBySU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLCountryCodeLearningBySU_Type.__name__ = "Integer32"
_BrzaccVLCountryCodeLearningBySU_Object = MibScalar
brzaccVLCountryCodeLearningBySU = _BrzaccVLCountryCodeLearningBySU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 12),
    _BrzaccVLCountryCodeLearningBySU_Type()
)
brzaccVLCountryCodeLearningBySU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCountryCodeLearningBySU.setStatus("current")
_BrzaccVLCurrentAUOperatingFrequencyNew_Type = DisplayString
_BrzaccVLCurrentAUOperatingFrequencyNew_Object = MibScalar
brzaccVLCurrentAUOperatingFrequencyNew = _BrzaccVLCurrentAUOperatingFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 13),
    _BrzaccVLCurrentAUOperatingFrequencyNew_Type()
)
brzaccVLCurrentAUOperatingFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentAUOperatingFrequencyNew.setStatus("current")
_BrzaccVLAUDefinedFrequencyNew_Type = DisplayString
_BrzaccVLAUDefinedFrequencyNew_Object = MibScalar
brzaccVLAUDefinedFrequencyNew = _BrzaccVLAUDefinedFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 14),
    _BrzaccVLAUDefinedFrequencyNew_Type()
)
brzaccVLAUDefinedFrequencyNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUDefinedFrequencyNew.setStatus("current")
_BrzaccVLAutoSubBandSelect_ObjectIdentity = ObjectIdentity
brzaccVLAutoSubBandSelect = _BrzaccVLAutoSubBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15)
)


class _BrzaccVLAutoSubBandSelectedFreqSubset_Type(Integer32):
    """Custom type brzaccVLAutoSubBandSelectedFreqSubset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("setAllSelectedFreqsSubset", 1))
    )


_BrzaccVLAutoSubBandSelectedFreqSubset_Type.__name__ = "Integer32"
_BrzaccVLAutoSubBandSelectedFreqSubset_Object = MibScalar
brzaccVLAutoSubBandSelectedFreqSubset = _BrzaccVLAutoSubBandSelectedFreqSubset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 1),
    _BrzaccVLAutoSubBandSelectedFreqSubset_Type()
)
brzaccVLAutoSubBandSelectedFreqSubset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandSelectedFreqSubset.setStatus("current")
_BrzaccVLAutoSubBandFrequencySubsetTable_Object = MibTable
brzaccVLAutoSubBandFrequencySubsetTable = _BrzaccVLAutoSubBandFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2)
)
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetTable.setStatus("current")
_BrzaccVLAutoSubBandFrequencySubsetEntry_Object = MibTableRow
brzaccVLAutoSubBandFrequencySubsetEntry = _BrzaccVLAutoSubBandFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1)
)
brzaccVLAutoSubBandFrequencySubsetEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLAutoSubBandFrequencySubsetBandIdx"),
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLAutoSubBandFrequencySubsetFrequencyIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetEntry.setStatus("current")


class _BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type(Integer32):
    """Custom type brzaccVLAutoSubBandFrequencySubsetBandIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type.__name__ = "Integer32"
_BrzaccVLAutoSubBandFrequencySubsetBandIdx_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetBandIdx = _BrzaccVLAutoSubBandFrequencySubsetBandIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 1),
    _BrzaccVLAutoSubBandFrequencySubsetBandIdx_Type()
)
brzaccVLAutoSubBandFrequencySubsetBandIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetBandIdx.setStatus("current")


class _BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type(Integer32):
    """Custom type brzaccVLAutoSubBandFrequencySubsetFrequencyIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type.__name__ = "Integer32"
_BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetFrequencyIdx = _BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 2),
    _BrzaccVLAutoSubBandFrequencySubsetFrequencyIdx_Type()
)
brzaccVLAutoSubBandFrequencySubsetFrequencyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetFrequencyIdx.setStatus("current")


class _BrzaccVLAutoSubBandFrequencySubsetActive_Type(Integer32):
    """Custom type brzaccVLAutoSubBandFrequencySubsetActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_BrzaccVLAutoSubBandFrequencySubsetActive_Type.__name__ = "Integer32"
_BrzaccVLAutoSubBandFrequencySubsetActive_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetActive = _BrzaccVLAutoSubBandFrequencySubsetActive_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 3),
    _BrzaccVLAutoSubBandFrequencySubsetActive_Type()
)
brzaccVLAutoSubBandFrequencySubsetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetActive.setStatus("current")
_BrzaccVLAutoSubBandFrequencySubsetFrequency_Type = DisplayString
_BrzaccVLAutoSubBandFrequencySubsetFrequency_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetFrequency = _BrzaccVLAutoSubBandFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 4),
    _BrzaccVLAutoSubBandFrequencySubsetFrequency_Type()
)
brzaccVLAutoSubBandFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetFrequency.setStatus("current")
_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Type = Integer32
_BrzaccVLAutoSubBandFrequencySubsetBandwidth_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetBandwidth = _BrzaccVLAutoSubBandFrequencySubsetBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 5),
    _BrzaccVLAutoSubBandFrequencySubsetBandwidth_Type()
)
brzaccVLAutoSubBandFrequencySubsetBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetBandwidth.setStatus("current")


class _BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type(Integer32):
    """Custom type brzaccVLAutoSubBandFrequencySubsetDFSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adjacentToRadar", 2),
          ("radarDetected", 3),
          ("radarFree", 1))
    )


_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type.__name__ = "Integer32"
_BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Object = MibTableColumn
brzaccVLAutoSubBandFrequencySubsetDFSStatus = _BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 6),
    _BrzaccVLAutoSubBandFrequencySubsetDFSStatus_Type()
)
brzaccVLAutoSubBandFrequencySubsetDFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAutoSubBandFrequencySubsetDFSStatus.setStatus("current")
_BrzaccVLATPC_ObjectIdentity = ObjectIdentity
brzaccVLATPC = _BrzaccVLATPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13)
)


class _BrzaccVLAtpcOption_Type(Integer32):
    """Custom type brzaccVLAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAtpcOption_Type.__name__ = "Integer32"
_BrzaccVLAtpcOption_Object = MibScalar
brzaccVLAtpcOption = _BrzaccVLAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 1),
    _BrzaccVLAtpcOption_Type()
)
brzaccVLAtpcOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAtpcOption.setStatus("current")
_BrzaccVLDeltaFromMinSNRLevel_Type = Integer32
_BrzaccVLDeltaFromMinSNRLevel_Object = MibScalar
brzaccVLDeltaFromMinSNRLevel = _BrzaccVLDeltaFromMinSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 2),
    _BrzaccVLDeltaFromMinSNRLevel_Type()
)
brzaccVLDeltaFromMinSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeltaFromMinSNRLevel.setStatus("current")
_BrzaccVLMinimumSNRLevel_Type = Integer32
_BrzaccVLMinimumSNRLevel_Object = MibScalar
brzaccVLMinimumSNRLevel = _BrzaccVLMinimumSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 3),
    _BrzaccVLMinimumSNRLevel_Type()
)
brzaccVLMinimumSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMinimumSNRLevel.setStatus("current")
_BrzaccVLMinimumIntervalBetweenATPCMessages_Type = Integer32
_BrzaccVLMinimumIntervalBetweenATPCMessages_Object = MibScalar
brzaccVLMinimumIntervalBetweenATPCMessages = _BrzaccVLMinimumIntervalBetweenATPCMessages_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 4),
    _BrzaccVLMinimumIntervalBetweenATPCMessages_Type()
)
brzaccVLMinimumIntervalBetweenATPCMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMinimumIntervalBetweenATPCMessages.setStatus("current")
_BrzaccVLPowerLevelSteps_Type = Integer32
_BrzaccVLPowerLevelSteps_Object = MibScalar
brzaccVLPowerLevelSteps = _BrzaccVLPowerLevelSteps_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 6),
    _BrzaccVLPowerLevelSteps_Type()
)
brzaccVLPowerLevelSteps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLPowerLevelSteps.setStatus("current")


class _BrzaccVLAtpcOptionEZ_Type(Integer32):
    """Custom type brzaccVLAtpcOptionEZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAtpcOptionEZ_Type.__name__ = "Integer32"
_BrzaccVLAtpcOptionEZ_Object = MibScalar
brzaccVLAtpcOptionEZ = _BrzaccVLAtpcOptionEZ_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 7),
    _BrzaccVLAtpcOptionEZ_Type()
)
brzaccVLAtpcOptionEZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAtpcOptionEZ.setStatus("current")
_BrzaccVLCellDistanceParameters_ObjectIdentity = ObjectIdentity
brzaccVLCellDistanceParameters = _BrzaccVLCellDistanceParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15)
)


class _BrzaccVLCellDistanceMode_Type(Integer32):
    """Custom type brzaccVLCellDistanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("na", 255))
    )


_BrzaccVLCellDistanceMode_Type.__name__ = "Integer32"
_BrzaccVLCellDistanceMode_Object = MibScalar
brzaccVLCellDistanceMode = _BrzaccVLCellDistanceMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 1),
    _BrzaccVLCellDistanceMode_Type()
)
brzaccVLCellDistanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCellDistanceMode.setStatus("current")
_BrzaccVLFairnessFactor_Type = Integer32
_BrzaccVLFairnessFactor_Object = MibScalar
brzaccVLFairnessFactor = _BrzaccVLFairnessFactor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 2),
    _BrzaccVLFairnessFactor_Type()
)
brzaccVLFairnessFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLFairnessFactor.setStatus("current")


class _BrzaccVLMeasuredCellDistance_Type(Integer32):
    """Custom type brzaccVLMeasuredCellDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("below-2-Km", 1)
    )


_BrzaccVLMeasuredCellDistance_Type.__name__ = "Integer32"
_BrzaccVLMeasuredCellDistance_Object = MibScalar
brzaccVLMeasuredCellDistance = _BrzaccVLMeasuredCellDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 3),
    _BrzaccVLMeasuredCellDistance_Type()
)
brzaccVLMeasuredCellDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMeasuredCellDistance.setStatus("current")
_BrzaccVLUnitWithMaxDistance_Type = MacAddress
_BrzaccVLUnitWithMaxDistance_Object = MibScalar
brzaccVLUnitWithMaxDistance = _BrzaccVLUnitWithMaxDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 4),
    _BrzaccVLUnitWithMaxDistance_Type()
)
brzaccVLUnitWithMaxDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnitWithMaxDistance.setStatus("current")


class _BrzaccVLPerSuDistanceLearning_Type(Integer32):
    """Custom type brzaccVLPerSuDistanceLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLPerSuDistanceLearning_Type.__name__ = "Integer32"
_BrzaccVLPerSuDistanceLearning_Object = MibScalar
brzaccVLPerSuDistanceLearning = _BrzaccVLPerSuDistanceLearning_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 5),
    _BrzaccVLPerSuDistanceLearning_Type()
)
brzaccVLPerSuDistanceLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLPerSuDistanceLearning.setStatus("current")


class _BrzaccVLScanningMode_Type(Integer32):
    """Custom type brzaccVLScanningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_BrzaccVLScanningMode_Type.__name__ = "Integer32"
_BrzaccVLScanningMode_Object = MibScalar
brzaccVLScanningMode = _BrzaccVLScanningMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 16),
    _BrzaccVLScanningMode_Type()
)
brzaccVLScanningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLScanningMode.setStatus("current")
_BrzaccVLAntennaGain_Type = DisplayString
_BrzaccVLAntennaGain_Object = MibScalar
brzaccVLAntennaGain = _BrzaccVLAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 17),
    _BrzaccVLAntennaGain_Type()
)
brzaccVLAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAntennaGain.setStatus("current")
_BrzaccVLSpectrumAnalysisParameters_ObjectIdentity = ObjectIdentity
brzaccVLSpectrumAnalysisParameters = _BrzaccVLSpectrumAnalysisParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18)
)
_BrzaccVLSpectrumAnalysisChannelScanPeriod_Type = Integer32
_BrzaccVLSpectrumAnalysisChannelScanPeriod_Object = MibScalar
brzaccVLSpectrumAnalysisChannelScanPeriod = _BrzaccVLSpectrumAnalysisChannelScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 1),
    _BrzaccVLSpectrumAnalysisChannelScanPeriod_Type()
)
brzaccVLSpectrumAnalysisChannelScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisChannelScanPeriod.setStatus("current")
_BrzaccVLSpectrumAnalysisScanCycles_Type = Integer32
_BrzaccVLSpectrumAnalysisScanCycles_Object = MibScalar
brzaccVLSpectrumAnalysisScanCycles = _BrzaccVLSpectrumAnalysisScanCycles_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 2),
    _BrzaccVLSpectrumAnalysisScanCycles_Type()
)
brzaccVLSpectrumAnalysisScanCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisScanCycles.setStatus("current")


class _BrzaccVLAutomaticChannelSelection_Type(Integer32):
    """Custom type brzaccVLAutomaticChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAutomaticChannelSelection_Type.__name__ = "Integer32"
_BrzaccVLAutomaticChannelSelection_Object = MibScalar
brzaccVLAutomaticChannelSelection = _BrzaccVLAutomaticChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 3),
    _BrzaccVLAutomaticChannelSelection_Type()
)
brzaccVLAutomaticChannelSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAutomaticChannelSelection.setStatus("current")


class _BrzaccVLSpectrumAnalysisActivation_Type(Integer32):
    """Custom type brzaccVLSpectrumAnalysisActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activateNow", 2),
          ("cancelOperation", 1))
    )


_BrzaccVLSpectrumAnalysisActivation_Type.__name__ = "Integer32"
_BrzaccVLSpectrumAnalysisActivation_Object = MibScalar
brzaccVLSpectrumAnalysisActivation = _BrzaccVLSpectrumAnalysisActivation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 4),
    _BrzaccVLSpectrumAnalysisActivation_Type()
)
brzaccVLSpectrumAnalysisActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisActivation.setStatus("current")


class _BrzaccVLSpectrumAnalysisStatus_Type(Integer32):
    """Custom type brzaccVLSpectrumAnalysisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentlyActive", 2),
          ("currentlyBlocked", 3),
          ("inactive", 1))
    )


_BrzaccVLSpectrumAnalysisStatus_Type.__name__ = "Integer32"
_BrzaccVLSpectrumAnalysisStatus_Object = MibScalar
brzaccVLSpectrumAnalysisStatus = _BrzaccVLSpectrumAnalysisStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 5),
    _BrzaccVLSpectrumAnalysisStatus_Type()
)
brzaccVLSpectrumAnalysisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisStatus.setStatus("current")


class _BrzaccVLResetSpectrumCounters_Type(Integer32):
    """Custom type brzaccVLResetSpectrumCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("resetCounters", 2))
    )


_BrzaccVLResetSpectrumCounters_Type.__name__ = "Integer32"
_BrzaccVLResetSpectrumCounters_Object = MibScalar
brzaccVLResetSpectrumCounters = _BrzaccVLResetSpectrumCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 6),
    _BrzaccVLResetSpectrumCounters_Type()
)
brzaccVLResetSpectrumCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLResetSpectrumCounters.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationTable_Object = MibTable
brzaccVLSpectrumAnalysisInformationTable = _BrzaccVLSpectrumAnalysisInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7)
)
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationTable.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationEntry_Object = MibTableRow
brzaccVLSpectrumAnalysisInformationEntry = _BrzaccVLSpectrumAnalysisInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1)
)
brzaccVLSpectrumAnalysisInformationEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLSpectrumAnalysisInformationTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationEntry.setStatus("current")


class _BrzaccVLSpectrumAnalysisInformationTableIdx_Type(Integer32):
    """Custom type brzaccVLSpectrumAnalysisInformationTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_BrzaccVLSpectrumAnalysisInformationTableIdx_Type.__name__ = "Integer32"
_BrzaccVLSpectrumAnalysisInformationTableIdx_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationTableIdx = _BrzaccVLSpectrumAnalysisInformationTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 1),
    _BrzaccVLSpectrumAnalysisInformationTableIdx_Type()
)
brzaccVLSpectrumAnalysisInformationTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationTableIdx.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationChannel_Type = DisplayString
_BrzaccVLSpectrumAnalysisInformationChannel_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationChannel = _BrzaccVLSpectrumAnalysisInformationChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 2),
    _BrzaccVLSpectrumAnalysisInformationChannel_Type()
)
brzaccVLSpectrumAnalysisInformationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationChannel.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationSignalCount_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationSignalCount_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalCount = _BrzaccVLSpectrumAnalysisInformationSignalCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 3),
    _BrzaccVLSpectrumAnalysisInformationSignalCount_Type()
)
brzaccVLSpectrumAnalysisInformationSignalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationSignalCount.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationSignalSNR_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationSignalSNR_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalSNR = _BrzaccVLSpectrumAnalysisInformationSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 4),
    _BrzaccVLSpectrumAnalysisInformationSignalSNR_Type()
)
brzaccVLSpectrumAnalysisInformationSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationSignalSNR.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationSignalWidth_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationSignalWidth_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalWidth = _BrzaccVLSpectrumAnalysisInformationSignalWidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 5),
    _BrzaccVLSpectrumAnalysisInformationSignalWidth_Type()
)
brzaccVLSpectrumAnalysisInformationSignalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationSignalWidth.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMFrames_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMFrames = _BrzaccVLSpectrumAnalysisInformationOFDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 6),
    _BrzaccVLSpectrumAnalysisInformationOFDMFrames_Type()
)
brzaccVLSpectrumAnalysisInformationOFDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationOFDMFrames.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMAvgSnr = _BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 7),
    _BrzaccVLSpectrumAnalysisInformationOFDMAvgSnr_Type()
)
brzaccVLSpectrumAnalysisInformationOFDMAvgSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationOFDMAvgSnr.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationAvgNoiseFloor = _BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 8),
    _BrzaccVLSpectrumAnalysisInformationAvgNoiseFloor_Type()
)
brzaccVLSpectrumAnalysisInformationAvgNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationAvgNoiseFloor.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationMaxNoiseFloor = _BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 9),
    _BrzaccVLSpectrumAnalysisInformationMaxNoiseFloor_Type()
)
brzaccVLSpectrumAnalysisInformationMaxNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationMaxNoiseFloor.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationSignalMaxSNR = _BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 10),
    _BrzaccVLSpectrumAnalysisInformationSignalMaxSNR_Type()
)
brzaccVLSpectrumAnalysisInformationSignalMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationSignalMaxSNR.setStatus("current")
_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Type = Integer32
_BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Object = MibTableColumn
brzaccVLSpectrumAnalysisInformationOFDMMaxSNR = _BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 11),
    _BrzaccVLSpectrumAnalysisInformationOFDMMaxSNR_Type()
)
brzaccVLSpectrumAnalysisInformationOFDMMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSpectrumAnalysisInformationOFDMMaxSNR.setStatus("current")
_BrzaccVLMaxNumOfAssociationsLimit_Type = Integer32
_BrzaccVLMaxNumOfAssociationsLimit_Object = MibScalar
brzaccVLMaxNumOfAssociationsLimit = _BrzaccVLMaxNumOfAssociationsLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 19),
    _BrzaccVLMaxNumOfAssociationsLimit_Type()
)
brzaccVLMaxNumOfAssociationsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLMaxNumOfAssociationsLimit.setStatus("current")
_BrzaccVLDisassociate_ObjectIdentity = ObjectIdentity
brzaccVLDisassociate = _BrzaccVLDisassociate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20)
)


class _BrzaccVLDisassociateAllSUs_Type(Integer32):
    """Custom type brzaccVLDisassociateAllSUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("disassociateAllSUs", 2))
    )


_BrzaccVLDisassociateAllSUs_Type.__name__ = "Integer32"
_BrzaccVLDisassociateAllSUs_Object = MibScalar
brzaccVLDisassociateAllSUs = _BrzaccVLDisassociateAllSUs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20, 1),
    _BrzaccVLDisassociateAllSUs_Type()
)
brzaccVLDisassociateAllSUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDisassociateAllSUs.setStatus("current")
_BrzaccVLDisassociateSuByMacAddress_Type = MacAddress
_BrzaccVLDisassociateSuByMacAddress_Object = MibScalar
brzaccVLDisassociateSuByMacAddress = _BrzaccVLDisassociateSuByMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20, 2),
    _BrzaccVLDisassociateSuByMacAddress_Type()
)
brzaccVLDisassociateSuByMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDisassociateSuByMacAddress.setStatus("current")


class _BrzaccVLTxControl_Type(Integer32):
    """Custom type brzaccVLTxControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernetStatusControl", 3),
          ("off", 2),
          ("on", 1))
    )


_BrzaccVLTxControl_Type.__name__ = "Integer32"
_BrzaccVLTxControl_Object = MibScalar
brzaccVLTxControl = _BrzaccVLTxControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 21),
    _BrzaccVLTxControl_Type()
)
brzaccVLTxControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTxControl.setStatus("current")


class _BrzaccVLLostBeaconsWatchdogThreshold_Type(Integer32):
    """Custom type brzaccVLLostBeaconsWatchdogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 1000),
    )


_BrzaccVLLostBeaconsWatchdogThreshold_Type.__name__ = "Integer32"
_BrzaccVLLostBeaconsWatchdogThreshold_Object = MibScalar
brzaccVLLostBeaconsWatchdogThreshold = _BrzaccVLLostBeaconsWatchdogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 22),
    _BrzaccVLLostBeaconsWatchdogThreshold_Type()
)
brzaccVLLostBeaconsWatchdogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLLostBeaconsWatchdogThreshold.setStatus("current")
_BrzaccVLTransmitPower_Type = Integer32
_BrzaccVLTransmitPower_Object = MibScalar
brzaccVLTransmitPower = _BrzaccVLTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 23),
    _BrzaccVLTransmitPower_Type()
)
brzaccVLTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTransmitPower.setStatus("current")
_BrzaccVLMaximumTxPower_Type = Integer32
_BrzaccVLMaximumTxPower_Object = MibScalar
brzaccVLMaximumTxPower = _BrzaccVLMaximumTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 24),
    _BrzaccVLMaximumTxPower_Type()
)
brzaccVLMaximumTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaximumTxPower.setStatus("current")
_BrzaccVLCountryCodeParameters_ObjectIdentity = ObjectIdentity
brzaccVLCountryCodeParameters = _BrzaccVLCountryCodeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25)
)


class _BrzaccVLCountryCodeReApply_Type(Integer32):
    """Custom type brzaccVLCountryCodeReApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("na", 255),
          ("reapply", 1))
    )


_BrzaccVLCountryCodeReApply_Type.__name__ = "Integer32"
_BrzaccVLCountryCodeReApply_Object = MibScalar
brzaccVLCountryCodeReApply = _BrzaccVLCountryCodeReApply_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 1),
    _BrzaccVLCountryCodeReApply_Type()
)
brzaccVLCountryCodeReApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCountryCodeReApply.setStatus("current")
_BrzaccVLCountryCodeTable_Object = MibTable
brzaccVLCountryCodeTable = _BrzaccVLCountryCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2)
)
if mibBuilder.loadTexts:
    brzaccVLCountryCodeTable.setStatus("current")
_BrzaccVLCountryCodeEntry_Object = MibTableRow
brzaccVLCountryCodeEntry = _BrzaccVLCountryCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1)
)
brzaccVLCountryCodeEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLCCNumber"),
)
if mibBuilder.loadTexts:
    brzaccVLCountryCodeEntry.setStatus("current")


class _BrzaccVLCCNumber_Type(Integer32):
    """Custom type brzaccVLCCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrzaccVLCCNumber_Type.__name__ = "Integer32"
_BrzaccVLCCNumber_Object = MibTableColumn
brzaccVLCCNumber = _BrzaccVLCCNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1, 1),
    _BrzaccVLCCNumber_Type()
)
brzaccVLCCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCNumber.setStatus("current")


class _BrzaccVLCCName_Type(DisplayString):
    """Custom type brzaccVLCCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BrzaccVLCCName_Type.__name__ = "DisplayString"
_BrzaccVLCCName_Object = MibTableColumn
brzaccVLCCName = _BrzaccVLCCName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1, 2),
    _BrzaccVLCCName_Type()
)
brzaccVLCCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCName.setStatus("current")


class _BrzaccVLCCAuthenticationEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLCCAuthenticationEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLCCAuthenticationEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLCCAuthenticationEncryptionSupport_Object = MibTableColumn
brzaccVLCCAuthenticationEncryptionSupport = _BrzaccVLCCAuthenticationEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1, 3),
    _BrzaccVLCCAuthenticationEncryptionSupport_Type()
)
brzaccVLCCAuthenticationEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCAuthenticationEncryptionSupport.setStatus("current")


class _BrzaccVLCCDataEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLCCDataEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLCCDataEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLCCDataEncryptionSupport_Object = MibTableColumn
brzaccVLCCDataEncryptionSupport = _BrzaccVLCCDataEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1, 4),
    _BrzaccVLCCDataEncryptionSupport_Type()
)
brzaccVLCCDataEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCDataEncryptionSupport.setStatus("current")


class _BrzaccVLCCAESEncryptionSupport_Type(Integer32):
    """Custom type brzaccVLCCAESEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLCCAESEncryptionSupport_Type.__name__ = "Integer32"
_BrzaccVLCCAESEncryptionSupport_Object = MibTableColumn
brzaccVLCCAESEncryptionSupport = _BrzaccVLCCAESEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 2, 1, 5),
    _BrzaccVLCCAESEncryptionSupport_Type()
)
brzaccVLCCAESEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCAESEncryptionSupport.setStatus("current")
_BrzaccVLCCParamsTable_Object = MibTable
brzaccVLCCParamsTable = _BrzaccVLCCParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3)
)
if mibBuilder.loadTexts:
    brzaccVLCCParamsTable.setStatus("current")
_BrzaccVLCCParamsEntry_Object = MibTableRow
brzaccVLCCParamsEntry = _BrzaccVLCCParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1)
)
brzaccVLCCParamsEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLCCNumberIdx"),
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLCCParamsIndex"),
)
if mibBuilder.loadTexts:
    brzaccVLCCParamsEntry.setStatus("current")


class _BrzaccVLCCNumberIdx_Type(Integer32):
    """Custom type brzaccVLCCNumberIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrzaccVLCCNumberIdx_Type.__name__ = "Integer32"
_BrzaccVLCCNumberIdx_Object = MibTableColumn
brzaccVLCCNumberIdx = _BrzaccVLCCNumberIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 1),
    _BrzaccVLCCNumberIdx_Type()
)
brzaccVLCCNumberIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCNumberIdx.setStatus("current")


class _BrzaccVLCCParamsIndex_Type(Integer32):
    """Custom type brzaccVLCCParamsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BrzaccVLCCParamsIndex_Type.__name__ = "Integer32"
_BrzaccVLCCParamsIndex_Object = MibTableColumn
brzaccVLCCParamsIndex = _BrzaccVLCCParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 2),
    _BrzaccVLCCParamsIndex_Type()
)
brzaccVLCCParamsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCParamsIndex.setStatus("current")
_BrzaccVLCCParamsFrequencies_Type = DisplayString
_BrzaccVLCCParamsFrequencies_Object = MibTableColumn
brzaccVLCCParamsFrequencies = _BrzaccVLCCParamsFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 3),
    _BrzaccVLCCParamsFrequencies_Type()
)
brzaccVLCCParamsFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCParamsFrequencies.setStatus("current")
_BrzaccVLCCAllowedBandwidth_Type = Integer32
_BrzaccVLCCAllowedBandwidth_Object = MibTableColumn
brzaccVLCCAllowedBandwidth = _BrzaccVLCCAllowedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 4),
    _BrzaccVLCCAllowedBandwidth_Type()
)
brzaccVLCCAllowedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCAllowedBandwidth.setStatus("current")
_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Type = Integer32
_BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Object = MibTableColumn
brzaccVLCCRegulationMaxTxPowerAtAntennaPort = _BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 5),
    _BrzaccVLCCRegulationMaxTxPowerAtAntennaPort_Type()
)
brzaccVLCCRegulationMaxTxPowerAtAntennaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCRegulationMaxTxPowerAtAntennaPort.setStatus("current")
_BrzaccVLCCRegulationMaxEIRP_Type = Integer32
_BrzaccVLCCRegulationMaxEIRP_Object = MibTableColumn
brzaccVLCCRegulationMaxEIRP = _BrzaccVLCCRegulationMaxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 6),
    _BrzaccVLCCRegulationMaxEIRP_Type()
)
brzaccVLCCRegulationMaxEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCRegulationMaxEIRP.setStatus("current")


class _BrzaccVLCCMinModulationLevel_Type(Integer32):
    """Custom type brzaccVLCCMinModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLCCMinModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLCCMinModulationLevel_Object = MibTableColumn
brzaccVLCCMinModulationLevel = _BrzaccVLCCMinModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 7),
    _BrzaccVLCCMinModulationLevel_Type()
)
brzaccVLCCMinModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCMinModulationLevel.setStatus("current")


class _BrzaccVLCCMaxModulationLevel_Type(Integer32):
    """Custom type brzaccVLCCMaxModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLCCMaxModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLCCMaxModulationLevel_Object = MibTableColumn
brzaccVLCCMaxModulationLevel = _BrzaccVLCCMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 8),
    _BrzaccVLCCMaxModulationLevel_Type()
)
brzaccVLCCMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCMaxModulationLevel.setStatus("current")


class _BrzaccVLCCBurstModeSupport_Type(Integer32):
    """Custom type brzaccVLCCBurstModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLCCBurstModeSupport_Type.__name__ = "Integer32"
_BrzaccVLCCBurstModeSupport_Object = MibTableColumn
brzaccVLCCBurstModeSupport = _BrzaccVLCCBurstModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 9),
    _BrzaccVLCCBurstModeSupport_Type()
)
brzaccVLCCBurstModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCBurstModeSupport.setStatus("current")
_BrzaccVLCCMaximumBurstDuration_Type = Integer32
_BrzaccVLCCMaximumBurstDuration_Object = MibTableColumn
brzaccVLCCMaximumBurstDuration = _BrzaccVLCCMaximumBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 10),
    _BrzaccVLCCMaximumBurstDuration_Type()
)
brzaccVLCCMaximumBurstDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCMaximumBurstDuration.setStatus("current")


class _BrzaccVLCCDfsSupport_Type(Integer32):
    """Custom type brzaccVLCCDfsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_BrzaccVLCCDfsSupport_Type.__name__ = "Integer32"
_BrzaccVLCCDfsSupport_Object = MibTableColumn
brzaccVLCCDfsSupport = _BrzaccVLCCDfsSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 11),
    _BrzaccVLCCDfsSupport_Type()
)
brzaccVLCCDfsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCDfsSupport.setStatus("current")


class _BrzaccVLCCMinimumHwRevision_Type(Integer32):
    """Custom type brzaccVLCCMinimumHwRevision based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("hwRevisionF", 6),
          ("hwRevisionG", 7),
          ("na", 255))
    )


_BrzaccVLCCMinimumHwRevision_Type.__name__ = "Integer32"
_BrzaccVLCCMinimumHwRevision_Object = MibTableColumn
brzaccVLCCMinimumHwRevision = _BrzaccVLCCMinimumHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 3, 1, 12),
    _BrzaccVLCCMinimumHwRevision_Type()
)
brzaccVLCCMinimumHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCCMinimumHwRevision.setStatus("current")
_BrzaccVLCountryCodeSelect_Type = Integer32
_BrzaccVLCountryCodeSelect_Object = MibScalar
brzaccVLCountryCodeSelect = _BrzaccVLCountryCodeSelect_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 4),
    _BrzaccVLCountryCodeSelect_Type()
)
brzaccVLCountryCodeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCountryCodeSelect.setStatus("current")
_BrzaccVLNoiseImmunityParameters_ObjectIdentity = ObjectIdentity
brzaccVLNoiseImmunityParameters = _BrzaccVLNoiseImmunityParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26)
)


class _BrzaccVLNoiseImmunityAlgorithm_Type(Integer32):
    """Custom type brzaccVLNoiseImmunityAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1),
          ("na", 255))
    )


_BrzaccVLNoiseImmunityAlgorithm_Type.__name__ = "Integer32"
_BrzaccVLNoiseImmunityAlgorithm_Object = MibScalar
brzaccVLNoiseImmunityAlgorithm = _BrzaccVLNoiseImmunityAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26, 1),
    _BrzaccVLNoiseImmunityAlgorithm_Type()
)
brzaccVLNoiseImmunityAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseImmunityAlgorithm.setStatus("current")


class _BrzaccVLNoiseImmunityLevel_Type(Integer32):
    """Custom type brzaccVLNoiseImmunityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLNoiseImmunityLevel_Type.__name__ = "Integer32"
_BrzaccVLNoiseImmunityLevel_Object = MibScalar
brzaccVLNoiseImmunityLevel = _BrzaccVLNoiseImmunityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26, 2),
    _BrzaccVLNoiseImmunityLevel_Type()
)
brzaccVLNoiseImmunityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseImmunityLevel.setStatus("current")


class _BrzaccVLSpuriousImmunityLevel_Type(Integer32):
    """Custom type brzaccVLSpuriousImmunityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_BrzaccVLSpuriousImmunityLevel_Type.__name__ = "Integer32"
_BrzaccVLSpuriousImmunityLevel_Object = MibScalar
brzaccVLSpuriousImmunityLevel = _BrzaccVLSpuriousImmunityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26, 3),
    _BrzaccVLSpuriousImmunityLevel_Type()
)
brzaccVLSpuriousImmunityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSpuriousImmunityLevel.setStatus("current")


class _BrzaccVLOFDMWeakSignal_Type(Integer32):
    """Custom type brzaccVLOFDMWeakSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("na", 255))
    )


_BrzaccVLOFDMWeakSignal_Type.__name__ = "Integer32"
_BrzaccVLOFDMWeakSignal_Object = MibScalar
brzaccVLOFDMWeakSignal = _BrzaccVLOFDMWeakSignal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26, 4),
    _BrzaccVLOFDMWeakSignal_Type()
)
brzaccVLOFDMWeakSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLOFDMWeakSignal.setStatus("current")


class _BrzaccVLPulseDetectionSensitivity_Type(Integer32):
    """Custom type brzaccVLPulseDetectionSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_BrzaccVLPulseDetectionSensitivity_Type.__name__ = "Integer32"
_BrzaccVLPulseDetectionSensitivity_Object = MibScalar
brzaccVLPulseDetectionSensitivity = _BrzaccVLPulseDetectionSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 26, 5),
    _BrzaccVLPulseDetectionSensitivity_Type()
)
brzaccVLPulseDetectionSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLPulseDetectionSensitivity.setStatus("current")
_BrzaccVLNewTransmitPowerTable_Object = MibTable
brzaccVLNewTransmitPowerTable = _BrzaccVLNewTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27)
)
if mibBuilder.loadTexts:
    brzaccVLNewTransmitPowerTable.setStatus("current")
_BrzaccVLNewTransmitPowerEntry_Object = MibTableRow
brzaccVLNewTransmitPowerEntry = _BrzaccVLNewTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27, 1)
)
brzaccVLNewTransmitPowerEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewModulationLevelIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLNewTransmitPowerEntry.setStatus("current")


class _BrzaccVLNewModulationLevelIdx_Type(Integer32):
    """Custom type brzaccVLNewModulationLevelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLNewModulationLevelIdx_Type.__name__ = "Integer32"
_BrzaccVLNewModulationLevelIdx_Object = MibTableColumn
brzaccVLNewModulationLevelIdx = _BrzaccVLNewModulationLevelIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27, 1, 1),
    _BrzaccVLNewModulationLevelIdx_Type()
)
brzaccVLNewModulationLevelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewModulationLevelIdx.setStatus("current")
_BrzaccVLNewMaximumTxPowerRange_Type = DisplayString
_BrzaccVLNewMaximumTxPowerRange_Object = MibTableColumn
brzaccVLNewMaximumTxPowerRange = _BrzaccVLNewMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27, 1, 2),
    _BrzaccVLNewMaximumTxPowerRange_Type()
)
brzaccVLNewMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewMaximumTxPowerRange.setStatus("current")
_BrzaccVLNewTxPower_Type = DisplayString
_BrzaccVLNewTxPower_Object = MibTableColumn
brzaccVLNewTxPower = _BrzaccVLNewTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27, 1, 3),
    _BrzaccVLNewTxPower_Type()
)
brzaccVLNewTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewTxPower.setStatus("current")
_BrzaccVLNewCurrentTxPower_Type = DisplayString
_BrzaccVLNewCurrentTxPower_Object = MibTableColumn
brzaccVLNewCurrentTxPower = _BrzaccVLNewCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 27, 1, 4),
    _BrzaccVLNewCurrentTxPower_Type()
)
brzaccVLNewCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewCurrentTxPower.setStatus("current")
_BrzaccVLNewMaximumTransmitPowerTable_Object = MibTable
brzaccVLNewMaximumTransmitPowerTable = _BrzaccVLNewMaximumTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 28)
)
if mibBuilder.loadTexts:
    brzaccVLNewMaximumTransmitPowerTable.setStatus("current")
_BrzaccVLNewMaximumTransmitPowerEntry_Object = MibTableRow
brzaccVLNewMaximumTransmitPowerEntry = _BrzaccVLNewMaximumTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 28, 1)
)
brzaccVLNewMaximumTransmitPowerEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewMaxModulationLevelIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLNewMaximumTransmitPowerEntry.setStatus("current")


class _BrzaccVLNewMaxModulationLevelIdx_Type(Integer32):
    """Custom type brzaccVLNewMaxModulationLevelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLNewMaxModulationLevelIdx_Type.__name__ = "Integer32"
_BrzaccVLNewMaxModulationLevelIdx_Object = MibTableColumn
brzaccVLNewMaxModulationLevelIdx = _BrzaccVLNewMaxModulationLevelIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 28, 1, 1),
    _BrzaccVLNewMaxModulationLevelIdx_Type()
)
brzaccVLNewMaxModulationLevelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewMaxModulationLevelIdx.setStatus("current")
_BrzaccVLNewDefinedMaximumTxPowerRange_Type = DisplayString
_BrzaccVLNewDefinedMaximumTxPowerRange_Object = MibTableColumn
brzaccVLNewDefinedMaximumTxPowerRange = _BrzaccVLNewDefinedMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 28, 1, 2),
    _BrzaccVLNewDefinedMaximumTxPowerRange_Type()
)
brzaccVLNewDefinedMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewDefinedMaximumTxPowerRange.setStatus("current")
_BrzaccVLNewMaxTxPower_Type = DisplayString
_BrzaccVLNewMaxTxPower_Object = MibTableColumn
brzaccVLNewMaxTxPower = _BrzaccVLNewMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 28, 1, 3),
    _BrzaccVLNewMaxTxPower_Type()
)
brzaccVLNewMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMaxTxPower.setStatus("current")
_BrzaccVLNoiseFloorCalculationParameters_ObjectIdentity = ObjectIdentity
brzaccVLNoiseFloorCalculationParameters = _BrzaccVLNoiseFloorCalculationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 29)
)


class _BrzaccVLNoiseFloorCalculationMode_Type(Integer32):
    """Custom type brzaccVLNoiseFloorCalculationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("forced", 2),
          ("minimumlevel", 3))
    )


_BrzaccVLNoiseFloorCalculationMode_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorCalculationMode_Object = MibScalar
brzaccVLNoiseFloorCalculationMode = _BrzaccVLNoiseFloorCalculationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 29, 1),
    _BrzaccVLNoiseFloorCalculationMode_Type()
)
brzaccVLNoiseFloorCalculationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorCalculationMode.setStatus("current")
_BrzaccVLNoiseFloorForcedValue_Type = Integer32
_BrzaccVLNoiseFloorForcedValue_Object = MibScalar
brzaccVLNoiseFloorForcedValue = _BrzaccVLNoiseFloorForcedValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 29, 2),
    _BrzaccVLNoiseFloorForcedValue_Type()
)
brzaccVLNoiseFloorForcedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorForcedValue.setStatus("current")
_BrzaccVLNoiseFloorCalibrationParameters_ObjectIdentity = ObjectIdentity
brzaccVLNoiseFloorCalibrationParameters = _BrzaccVLNoiseFloorCalibrationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30)
)


class _BrzaccVLNoiseFloorRunCalibration_Type(Integer32):
    """Custom type brzaccVLNoiseFloorRunCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("na", 255),
          ("run", 1))
    )


_BrzaccVLNoiseFloorRunCalibration_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorRunCalibration_Object = MibScalar
brzaccVLNoiseFloorRunCalibration = _BrzaccVLNoiseFloorRunCalibration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 1),
    _BrzaccVLNoiseFloorRunCalibration_Type()
)
brzaccVLNoiseFloorRunCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorRunCalibration.setStatus("current")


class _BrzaccVLNoiseFloorFieldCalibrationStatus_Type(Integer32):
    """Custom type brzaccVLNoiseFloorFieldCalibrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentlyActive", 2),
          ("inactive", 1))
    )


_BrzaccVLNoiseFloorFieldCalibrationStatus_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorFieldCalibrationStatus_Object = MibScalar
brzaccVLNoiseFloorFieldCalibrationStatus = _BrzaccVLNoiseFloorFieldCalibrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 2),
    _BrzaccVLNoiseFloorFieldCalibrationStatus_Type()
)
brzaccVLNoiseFloorFieldCalibrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorFieldCalibrationStatus.setStatus("current")


class _BrzaccVLNoiseFloorLastFieldCalibrationResult_Type(Integer32):
    """Custom type brzaccVLNoiseFloorLastFieldCalibrationResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("none", 3),
          ("passed", 1))
    )


_BrzaccVLNoiseFloorLastFieldCalibrationResult_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorLastFieldCalibrationResult_Object = MibScalar
brzaccVLNoiseFloorLastFieldCalibrationResult = _BrzaccVLNoiseFloorLastFieldCalibrationResult_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 3),
    _BrzaccVLNoiseFloorLastFieldCalibrationResult_Type()
)
brzaccVLNoiseFloorLastFieldCalibrationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorLastFieldCalibrationResult.setStatus("current")


class _BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type(Integer32):
    """Custom type brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              20,
              40)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-10MHz", 10),
          ("bandwidth-20MHz", 20),
          ("bandwidth-40MHz", 40),
          ("bandwidth-5MHz", 5),
          ("none", 0))
    )


_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Object = MibScalar
brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration = _BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 4),
    _BrzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration_Type()
)
brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration.setStatus("current")


class _BrzaccVLNoiseFloorAvailableCalibrationOptions_Type(Integer32):
    """Custom type brzaccVLNoiseFloorAvailableCalibrationOptions based on Integer32"""
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
        *(("factoryAndField", 4),
          ("factoryOnly", 2),
          ("fieldOnly", 3),
          ("notCalibrated", 1))
    )


_BrzaccVLNoiseFloorAvailableCalibrationOptions_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorAvailableCalibrationOptions_Object = MibScalar
brzaccVLNoiseFloorAvailableCalibrationOptions = _BrzaccVLNoiseFloorAvailableCalibrationOptions_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 5),
    _BrzaccVLNoiseFloorAvailableCalibrationOptions_Type()
)
brzaccVLNoiseFloorAvailableCalibrationOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorAvailableCalibrationOptions.setStatus("current")


class _BrzaccVLNoiseFloorUseCalibration_Type(Integer32):
    """Custom type brzaccVLNoiseFloorUseCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryCalibration", 3),
          ("fieldCalibration", 2),
          ("none", 1))
    )


_BrzaccVLNoiseFloorUseCalibration_Type.__name__ = "Integer32"
_BrzaccVLNoiseFloorUseCalibration_Object = MibScalar
brzaccVLNoiseFloorUseCalibration = _BrzaccVLNoiseFloorUseCalibration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 30, 6),
    _BrzaccVLNoiseFloorUseCalibration_Type()
)
brzaccVLNoiseFloorUseCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNoiseFloorUseCalibration.setStatus("current")
_BrzaccVLInterferenceMitigationParameters_ObjectIdentity = ObjectIdentity
brzaccVLInterferenceMitigationParameters = _BrzaccVLInterferenceMitigationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31)
)
_BrzaccVLInterferenceMitigationChannelScanPeriod_Type = Integer32
_BrzaccVLInterferenceMitigationChannelScanPeriod_Object = MibScalar
brzaccVLInterferenceMitigationChannelScanPeriod = _BrzaccVLInterferenceMitigationChannelScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 1),
    _BrzaccVLInterferenceMitigationChannelScanPeriod_Type()
)
brzaccVLInterferenceMitigationChannelScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationChannelScanPeriod.setStatus("current")
_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Type = Integer32
_BrzaccVLInterferenceMitigationAutomaticScanPeriod_Object = MibScalar
brzaccVLInterferenceMitigationAutomaticScanPeriod = _BrzaccVLInterferenceMitigationAutomaticScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 2),
    _BrzaccVLInterferenceMitigationAutomaticScanPeriod_Type()
)
brzaccVLInterferenceMitigationAutomaticScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationAutomaticScanPeriod.setStatus("current")


class _BrzaccVLInterferenceMitigationScanType_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationScanType based on Integer32"""
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
        *(("automaticNoiseFloorSelectionOnly", 2),
          ("clearChannelAndAutomaticNoiseFloorSelection", 1),
          ("clearChannelSelectionOnly", 3),
          ("statisticsOnly", 4))
    )


_BrzaccVLInterferenceMitigationScanType_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationScanType_Object = MibScalar
brzaccVLInterferenceMitigationScanType = _BrzaccVLInterferenceMitigationScanType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 3),
    _BrzaccVLInterferenceMitigationScanType_Type()
)
brzaccVLInterferenceMitigationScanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationScanType.setStatus("current")


class _BrzaccVLInterferenceMitigationScanMode_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optimizeDistanceForMinimumDesiredPerformance", 2),
          ("optimizePerformanceForMinimumDesiredDistance", 1))
    )


_BrzaccVLInterferenceMitigationScanMode_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationScanMode_Object = MibScalar
brzaccVLInterferenceMitigationScanMode = _BrzaccVLInterferenceMitigationScanMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 4),
    _BrzaccVLInterferenceMitigationScanMode_Type()
)
brzaccVLInterferenceMitigationScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationScanMode.setStatus("current")
_BrzaccVLInterferenceMitigationDistance_Type = Integer32
_BrzaccVLInterferenceMitigationDistance_Object = MibScalar
brzaccVLInterferenceMitigationDistance = _BrzaccVLInterferenceMitigationDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 5),
    _BrzaccVLInterferenceMitigationDistance_Type()
)
brzaccVLInterferenceMitigationDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationDistance.setStatus("current")
_BrzaccVLInterferenceMitigationThroughput_Type = Integer32
_BrzaccVLInterferenceMitigationThroughput_Object = MibScalar
brzaccVLInterferenceMitigationThroughput = _BrzaccVLInterferenceMitigationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 6),
    _BrzaccVLInterferenceMitigationThroughput_Type()
)
brzaccVLInterferenceMitigationThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationThroughput.setStatus("current")


class _BrzaccVLInterferenceMitigationActivation_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activateNow", 2),
          ("cancelOperation", 1),
          ("notAvailable", 3))
    )


_BrzaccVLInterferenceMitigationActivation_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationActivation_Object = MibScalar
brzaccVLInterferenceMitigationActivation = _BrzaccVLInterferenceMitigationActivation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 8),
    _BrzaccVLInterferenceMitigationActivation_Type()
)
brzaccVLInterferenceMitigationActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationActivation.setStatus("current")


class _BrzaccVLInterferenceMitigationStatus_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentlyActive", 2),
          ("currentlyBlocked", 3),
          ("inactive", 1))
    )


_BrzaccVLInterferenceMitigationStatus_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationStatus_Object = MibScalar
brzaccVLInterferenceMitigationStatus = _BrzaccVLInterferenceMitigationStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 9),
    _BrzaccVLInterferenceMitigationStatus_Type()
)
brzaccVLInterferenceMitigationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationStatus.setStatus("current")


class _BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationDeleteStatisticsFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("delete", 2))
    )


_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationDeleteStatisticsFile_Object = MibScalar
brzaccVLInterferenceMitigationDeleteStatisticsFile = _BrzaccVLInterferenceMitigationDeleteStatisticsFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 10),
    _BrzaccVLInterferenceMitigationDeleteStatisticsFile_Type()
)
brzaccVLInterferenceMitigationDeleteStatisticsFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationDeleteStatisticsFile.setStatus("current")


class _BrzaccVLInterferenceMitigationModel_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("typeLOS", 1),
          ("typeNoLOS", 3),
          ("typenLOS", 2))
    )


_BrzaccVLInterferenceMitigationModel_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationModel_Object = MibScalar
brzaccVLInterferenceMitigationModel = _BrzaccVLInterferenceMitigationModel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 11),
    _BrzaccVLInterferenceMitigationModel_Type()
)
brzaccVLInterferenceMitigationModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationModel.setStatus("current")
_BrzaccVLInterferenceMitigationScanTime_Type = Integer32
_BrzaccVLInterferenceMitigationScanTime_Object = MibScalar
brzaccVLInterferenceMitigationScanTime = _BrzaccVLInterferenceMitigationScanTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 12),
    _BrzaccVLInterferenceMitigationScanTime_Type()
)
brzaccVLInterferenceMitigationScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationScanTime.setStatus("current")
_BrzaccVLInterferenceMitigationAUheight_Type = Integer32
_BrzaccVLInterferenceMitigationAUheight_Object = MibScalar
brzaccVLInterferenceMitigationAUheight = _BrzaccVLInterferenceMitigationAUheight_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 13),
    _BrzaccVLInterferenceMitigationAUheight_Type()
)
brzaccVLInterferenceMitigationAUheight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationAUheight.setStatus("current")
_BrzaccVLInterferenceMitigationAntennaGain_Type = Integer32
_BrzaccVLInterferenceMitigationAntennaGain_Object = MibScalar
brzaccVLInterferenceMitigationAntennaGain = _BrzaccVLInterferenceMitigationAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 14),
    _BrzaccVLInterferenceMitigationAntennaGain_Type()
)
brzaccVLInterferenceMitigationAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationAntennaGain.setStatus("current")
_BrzaccVLInterferenceMitigationMaxModulation_Type = Integer32
_BrzaccVLInterferenceMitigationMaxModulation_Object = MibScalar
brzaccVLInterferenceMitigationMaxModulation = _BrzaccVLInterferenceMitigationMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 15),
    _BrzaccVLInterferenceMitigationMaxModulation_Type()
)
brzaccVLInterferenceMitigationMaxModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationMaxModulation.setStatus("current")


class _BrzaccVLInterferenceMitigationKeepLink_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationKeepLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BrzaccVLInterferenceMitigationKeepLink_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationKeepLink_Object = MibScalar
brzaccVLInterferenceMitigationKeepLink = _BrzaccVLInterferenceMitigationKeepLink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 16),
    _BrzaccVLInterferenceMitigationKeepLink_Type()
)
brzaccVLInterferenceMitigationKeepLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationKeepLink.setStatus("current")
_BrzaccVLInterferenceMitigationOutputTable_Object = MibTable
brzaccVLInterferenceMitigationOutputTable = _BrzaccVLInterferenceMitigationOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17)
)
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputTable.setStatus("current")
_BrzaccVLInterferenceMitigationOutputEntry_Object = MibTableRow
brzaccVLInterferenceMitigationOutputEntry = _BrzaccVLInterferenceMitigationOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1)
)
brzaccVLInterferenceMitigationOutputEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLInterferenceMitigationOutputFrequency"),
)
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputEntry.setStatus("current")


class _BrzaccVLInterferenceMitigationOutputFrequency_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(905, 925),
    )


_BrzaccVLInterferenceMitigationOutputFrequency_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationOutputFrequency_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputFrequency = _BrzaccVLInterferenceMitigationOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 1),
    _BrzaccVLInterferenceMitigationOutputFrequency_Type()
)
brzaccVLInterferenceMitigationOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputFrequency.setStatus("current")


class _BrzaccVLInterferenceMitigationOutputScanningType_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationOutputScanningType based on Integer32"""
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
        *(("typeANFS", 2),
          ("typeCCS", 3),
          ("typeCCSandANFS", 1),
          ("typeStatistics", 4))
    )


_BrzaccVLInterferenceMitigationOutputScanningType_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationOutputScanningType_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputScanningType = _BrzaccVLInterferenceMitigationOutputScanningType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 2),
    _BrzaccVLInterferenceMitigationOutputScanningType_Type()
)
brzaccVLInterferenceMitigationOutputScanningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputScanningType.setStatus("current")


class _BrzaccVLInterferenceMitigationOutputInstallationModel_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationOutputInstallationModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("typeLOS", 1),
          ("typeNearLOS", 2),
          ("typeNoLOS", 3))
    )


_BrzaccVLInterferenceMitigationOutputInstallationModel_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationOutputInstallationModel_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputInstallationModel = _BrzaccVLInterferenceMitigationOutputInstallationModel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 3),
    _BrzaccVLInterferenceMitigationOutputInstallationModel_Type()
)
brzaccVLInterferenceMitigationOutputInstallationModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputInstallationModel.setStatus("current")


class _BrzaccVLInterferenceMitigationOutputNoiseFloor_Type(Integer32):
    """Custom type brzaccVLInterferenceMitigationOutputNoiseFloor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -55),
    )


_BrzaccVLInterferenceMitigationOutputNoiseFloor_Type.__name__ = "Integer32"
_BrzaccVLInterferenceMitigationOutputNoiseFloor_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputNoiseFloor = _BrzaccVLInterferenceMitigationOutputNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 4),
    _BrzaccVLInterferenceMitigationOutputNoiseFloor_Type()
)
brzaccVLInterferenceMitigationOutputNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputNoiseFloor.setStatus("current")
_BrzaccVLInterferenceMitigationOutputDistance_Type = Integer32
_BrzaccVLInterferenceMitigationOutputDistance_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputDistance = _BrzaccVLInterferenceMitigationOutputDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 5),
    _BrzaccVLInterferenceMitigationOutputDistance_Type()
)
brzaccVLInterferenceMitigationOutputDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputDistance.setStatus("current")
_BrzaccVLInterferenceMitigationOutputPerformance_Type = Integer32
_BrzaccVLInterferenceMitigationOutputPerformance_Object = MibTableColumn
brzaccVLInterferenceMitigationOutputPerformance = _BrzaccVLInterferenceMitigationOutputPerformance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 31, 17, 1, 6),
    _BrzaccVLInterferenceMitigationOutputPerformance_Type()
)
brzaccVLInterferenceMitigationOutputPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLInterferenceMitigationOutputPerformance.setStatus("current")
_BrzaccVLBeaconPeriod_Type = Integer32
_BrzaccVLBeaconPeriod_Object = MibScalar
brzaccVLBeaconPeriod = _BrzaccVLBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 32),
    _BrzaccVLBeaconPeriod_Type()
)
brzaccVLBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBeaconPeriod.setStatus("current")
_BrzaccVLMaxBeaconsLost_Type = Integer32
_BrzaccVLMaxBeaconsLost_Object = MibScalar
brzaccVLMaxBeaconsLost = _BrzaccVLMaxBeaconsLost_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 33),
    _BrzaccVLMaxBeaconsLost_Type()
)
brzaccVLMaxBeaconsLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxBeaconsLost.setStatus("current")
_BrzaccVLServiceParameters_ObjectIdentity = ObjectIdentity
brzaccVLServiceParameters = _BrzaccVLServiceParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7)
)
_BrzaccVLMirDownlink_Type = Integer32
_BrzaccVLMirDownlink_Object = MibScalar
brzaccVLMirDownlink = _BrzaccVLMirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 2),
    _BrzaccVLMirDownlink_Type()
)
brzaccVLMirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMirDownlink.setStatus("current")
_BrzaccVLMirUplink_Type = Integer32
_BrzaccVLMirUplink_Object = MibScalar
brzaccVLMirUplink = _BrzaccVLMirUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 3),
    _BrzaccVLMirUplink_Type()
)
brzaccVLMirUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMirUplink.setStatus("current")
_BrzaccVLCirDownlink_Type = Integer32
_BrzaccVLCirDownlink_Object = MibScalar
brzaccVLCirDownlink = _BrzaccVLCirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 4),
    _BrzaccVLCirDownlink_Type()
)
brzaccVLCirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCirDownlink.setStatus("current")
_BrzaccVLCirUplink_Type = Integer32
_BrzaccVLCirUplink_Object = MibScalar
brzaccVLCirUplink = _BrzaccVLCirUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 5),
    _BrzaccVLCirUplink_Type()
)
brzaccVLCirUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLCirUplink.setStatus("current")
_BrzaccVLMaxDelay_Type = Integer32
_BrzaccVLMaxDelay_Object = MibScalar
brzaccVLMaxDelay = _BrzaccVLMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 6),
    _BrzaccVLMaxDelay_Type()
)
brzaccVLMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxDelay.setStatus("current")
_BrzaccVLMaxBurstDuration_Type = Integer32
_BrzaccVLMaxBurstDuration_Object = MibScalar
brzaccVLMaxBurstDuration = _BrzaccVLMaxBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 7),
    _BrzaccVLMaxBurstDuration_Type()
)
brzaccVLMaxBurstDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxBurstDuration.setStatus("current")
_BrzaccVLGracefulDegradationLimit_Type = Integer32
_BrzaccVLGracefulDegradationLimit_Object = MibScalar
brzaccVLGracefulDegradationLimit = _BrzaccVLGracefulDegradationLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 8),
    _BrzaccVLGracefulDegradationLimit_Type()
)
brzaccVLGracefulDegradationLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLGracefulDegradationLimit.setStatus("current")


class _BrzaccVLMirOnlyOption_Type(Integer32):
    """Custom type brzaccVLMirOnlyOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLMirOnlyOption_Type.__name__ = "Integer32"
_BrzaccVLMirOnlyOption_Object = MibScalar
brzaccVLMirOnlyOption = _BrzaccVLMirOnlyOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 9),
    _BrzaccVLMirOnlyOption_Type()
)
brzaccVLMirOnlyOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMirOnlyOption.setStatus("current")
_BrzaccVLTrafficPrioritization_ObjectIdentity = ObjectIdentity
brzaccVLTrafficPrioritization = _BrzaccVLTrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10)
)
_BrzaccVLTrafficPriVLAN_ObjectIdentity = ObjectIdentity
brzaccVLTrafficPriVLAN = _BrzaccVLTrafficPriVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 1)
)


class _BrzaccVLVLANPriorityThreshold_Type(Integer32):
    """Custom type brzaccVLVLANPriorityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_BrzaccVLVLANPriorityThreshold_Type.__name__ = "Integer32"
_BrzaccVLVLANPriorityThreshold_Object = MibScalar
brzaccVLVLANPriorityThreshold = _BrzaccVLVLANPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 1, 1),
    _BrzaccVLVLANPriorityThreshold_Type()
)
brzaccVLVLANPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLVLANPriorityThreshold.setStatus("current")
_BrzaccVLTrafficPriIPToS_ObjectIdentity = ObjectIdentity
brzaccVLTrafficPriIPToS = _BrzaccVLTrafficPriIPToS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2)
)


class _BrzaccVLToSPrioritizationOption_Type(Integer32):
    """Custom type brzaccVLToSPrioritizationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dSCP", 3),
          ("disable", 1),
          ("ipPrecedence", 2))
    )


_BrzaccVLToSPrioritizationOption_Type.__name__ = "Integer32"
_BrzaccVLToSPrioritizationOption_Object = MibScalar
brzaccVLToSPrioritizationOption = _BrzaccVLToSPrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 1),
    _BrzaccVLToSPrioritizationOption_Type()
)
brzaccVLToSPrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLToSPrioritizationOption.setStatus("current")


class _BrzaccVLIPPrecedenceThreshold_Type(Integer32):
    """Custom type brzaccVLIPPrecedenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrzaccVLIPPrecedenceThreshold_Type.__name__ = "Integer32"
_BrzaccVLIPPrecedenceThreshold_Object = MibScalar
brzaccVLIPPrecedenceThreshold = _BrzaccVLIPPrecedenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 2),
    _BrzaccVLIPPrecedenceThreshold_Type()
)
brzaccVLIPPrecedenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLIPPrecedenceThreshold.setStatus("current")


class _BrzaccVLIPDSCPThreshold_Type(Integer32):
    """Custom type brzaccVLIPDSCPThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BrzaccVLIPDSCPThreshold_Type.__name__ = "Integer32"
_BrzaccVLIPDSCPThreshold_Object = MibScalar
brzaccVLIPDSCPThreshold = _BrzaccVLIPDSCPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 3),
    _BrzaccVLIPDSCPThreshold_Type()
)
brzaccVLIPDSCPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLIPDSCPThreshold.setStatus("current")
_BrzaccVLTrafficPriUdpTcpPortRange_ObjectIdentity = ObjectIdentity
brzaccVLTrafficPriUdpTcpPortRange = _BrzaccVLTrafficPriUdpTcpPortRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3)
)


class _BrzaccVLUdpTcpPortRangePrioritizationOption_Type(Integer32):
    """Custom type brzaccVLUdpTcpPortRangePrioritizationOption based on Integer32"""
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
        *(("disable", 1),
          ("tcpOnly", 3),
          ("udpANDtcp", 4),
          ("udpOnly", 2))
    )


_BrzaccVLUdpTcpPortRangePrioritizationOption_Type.__name__ = "Integer32"
_BrzaccVLUdpTcpPortRangePrioritizationOption_Object = MibScalar
brzaccVLUdpTcpPortRangePrioritizationOption = _BrzaccVLUdpTcpPortRangePrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 1),
    _BrzaccVLUdpTcpPortRangePrioritizationOption_Type()
)
brzaccVLUdpTcpPortRangePrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUdpTcpPortRangePrioritizationOption.setStatus("current")
_BrzaccVLUdpPortRangeConfig_ObjectIdentity = ObjectIdentity
brzaccVLUdpPortRangeConfig = _BrzaccVLUdpPortRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2)
)


class _BrzaccVLUdpPortPriRTPRTCP_Type(Integer32):
    """Custom type brzaccVLUdpPortPriRTPRTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtpANDrtcp", 1),
          ("rtpOnly", 2))
    )


_BrzaccVLUdpPortPriRTPRTCP_Type.__name__ = "Integer32"
_BrzaccVLUdpPortPriRTPRTCP_Object = MibScalar
brzaccVLUdpPortPriRTPRTCP = _BrzaccVLUdpPortPriRTPRTCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 1),
    _BrzaccVLUdpPortPriRTPRTCP_Type()
)
brzaccVLUdpPortPriRTPRTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUdpPortPriRTPRTCP.setStatus("current")
_BrzaccVLUdpPortRangeNum_Type = Integer32
_BrzaccVLUdpPortRangeNum_Object = MibScalar
brzaccVLUdpPortRangeNum = _BrzaccVLUdpPortRangeNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 2),
    _BrzaccVLUdpPortRangeNum_Type()
)
brzaccVLUdpPortRangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeNum.setStatus("current")
_BrzaccVLUdpPortRangeTable_Object = MibTable
brzaccVLUdpPortRangeTable = _BrzaccVLUdpPortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3)
)
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeTable.setStatus("current")
_BrzaccVLUdpPortRangeEntry_Object = MibTableRow
brzaccVLUdpPortRangeEntry = _BrzaccVLUdpPortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1)
)
brzaccVLUdpPortRangeEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLUdpPortRangeIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeEntry.setStatus("current")


class _BrzaccVLUdpPortRangeStart_Type(Integer32):
    """Custom type brzaccVLUdpPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrzaccVLUdpPortRangeStart_Type.__name__ = "Integer32"
_BrzaccVLUdpPortRangeStart_Object = MibTableColumn
brzaccVLUdpPortRangeStart = _BrzaccVLUdpPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 1),
    _BrzaccVLUdpPortRangeStart_Type()
)
brzaccVLUdpPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeStart.setStatus("current")


class _BrzaccVLUdpPortRangeEnd_Type(Integer32):
    """Custom type brzaccVLUdpPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrzaccVLUdpPortRangeEnd_Type.__name__ = "Integer32"
_BrzaccVLUdpPortRangeEnd_Object = MibTableColumn
brzaccVLUdpPortRangeEnd = _BrzaccVLUdpPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 2),
    _BrzaccVLUdpPortRangeEnd_Type()
)
brzaccVLUdpPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeEnd.setStatus("current")


class _BrzaccVLUdpPortRangeIdx_Type(Integer32):
    """Custom type brzaccVLUdpPortRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BrzaccVLUdpPortRangeIdx_Type.__name__ = "Integer32"
_BrzaccVLUdpPortRangeIdx_Object = MibTableColumn
brzaccVLUdpPortRangeIdx = _BrzaccVLUdpPortRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 3),
    _BrzaccVLUdpPortRangeIdx_Type()
)
brzaccVLUdpPortRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeIdx.setStatus("current")


class _BrzaccVLUdpPortRangeAdd_Type(DisplayString):
    """Custom type brzaccVLUdpPortRangeAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BrzaccVLUdpPortRangeAdd_Type.__name__ = "DisplayString"
_BrzaccVLUdpPortRangeAdd_Object = MibScalar
brzaccVLUdpPortRangeAdd = _BrzaccVLUdpPortRangeAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 4),
    _BrzaccVLUdpPortRangeAdd_Type()
)
brzaccVLUdpPortRangeAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeAdd.setStatus("current")


class _BrzaccVLUdpPortRangeDelete_Type(DisplayString):
    """Custom type brzaccVLUdpPortRangeDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BrzaccVLUdpPortRangeDelete_Type.__name__ = "DisplayString"
_BrzaccVLUdpPortRangeDelete_Object = MibScalar
brzaccVLUdpPortRangeDelete = _BrzaccVLUdpPortRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 5),
    _BrzaccVLUdpPortRangeDelete_Type()
)
brzaccVLUdpPortRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeDelete.setStatus("current")


class _BrzaccVLUdpPortRangeDeleteAll_Type(Integer32):
    """Custom type brzaccVLUdpPortRangeDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1))
    )


_BrzaccVLUdpPortRangeDeleteAll_Type.__name__ = "Integer32"
_BrzaccVLUdpPortRangeDeleteAll_Object = MibScalar
brzaccVLUdpPortRangeDeleteAll = _BrzaccVLUdpPortRangeDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 6),
    _BrzaccVLUdpPortRangeDeleteAll_Type()
)
brzaccVLUdpPortRangeDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUdpPortRangeDeleteAll.setStatus("current")
_BrzaccVLTcpPortRangeConfig_ObjectIdentity = ObjectIdentity
brzaccVLTcpPortRangeConfig = _BrzaccVLTcpPortRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3)
)


class _BrzaccVLTcpPortPriRTPRTCP_Type(Integer32):
    """Custom type brzaccVLTcpPortPriRTPRTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtpANDrtcp", 1),
          ("rtpOnly", 2))
    )


_BrzaccVLTcpPortPriRTPRTCP_Type.__name__ = "Integer32"
_BrzaccVLTcpPortPriRTPRTCP_Object = MibScalar
brzaccVLTcpPortPriRTPRTCP = _BrzaccVLTcpPortPriRTPRTCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 1),
    _BrzaccVLTcpPortPriRTPRTCP_Type()
)
brzaccVLTcpPortPriRTPRTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTcpPortPriRTPRTCP.setStatus("current")
_BrzaccVLTcpPortRangeNum_Type = Integer32
_BrzaccVLTcpPortRangeNum_Object = MibScalar
brzaccVLTcpPortRangeNum = _BrzaccVLTcpPortRangeNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 2),
    _BrzaccVLTcpPortRangeNum_Type()
)
brzaccVLTcpPortRangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeNum.setStatus("current")
_BrzaccVLTcpPortRangeTable_Object = MibTable
brzaccVLTcpPortRangeTable = _BrzaccVLTcpPortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3)
)
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeTable.setStatus("current")
_BrzaccVLTcpPortRangeEntry_Object = MibTableRow
brzaccVLTcpPortRangeEntry = _BrzaccVLTcpPortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1)
)
brzaccVLTcpPortRangeEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLTcpPortRangeIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeEntry.setStatus("current")


class _BrzaccVLTcpPortRangeStart_Type(Integer32):
    """Custom type brzaccVLTcpPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrzaccVLTcpPortRangeStart_Type.__name__ = "Integer32"
_BrzaccVLTcpPortRangeStart_Object = MibTableColumn
brzaccVLTcpPortRangeStart = _BrzaccVLTcpPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 1),
    _BrzaccVLTcpPortRangeStart_Type()
)
brzaccVLTcpPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeStart.setStatus("current")


class _BrzaccVLTcpPortRangeEnd_Type(Integer32):
    """Custom type brzaccVLTcpPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrzaccVLTcpPortRangeEnd_Type.__name__ = "Integer32"
_BrzaccVLTcpPortRangeEnd_Object = MibTableColumn
brzaccVLTcpPortRangeEnd = _BrzaccVLTcpPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 2),
    _BrzaccVLTcpPortRangeEnd_Type()
)
brzaccVLTcpPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeEnd.setStatus("current")


class _BrzaccVLTcpPortRangeIdx_Type(Integer32):
    """Custom type brzaccVLTcpPortRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BrzaccVLTcpPortRangeIdx_Type.__name__ = "Integer32"
_BrzaccVLTcpPortRangeIdx_Object = MibTableColumn
brzaccVLTcpPortRangeIdx = _BrzaccVLTcpPortRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 3),
    _BrzaccVLTcpPortRangeIdx_Type()
)
brzaccVLTcpPortRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeIdx.setStatus("current")


class _BrzaccVLTcpPortRangeAdd_Type(DisplayString):
    """Custom type brzaccVLTcpPortRangeAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BrzaccVLTcpPortRangeAdd_Type.__name__ = "DisplayString"
_BrzaccVLTcpPortRangeAdd_Object = MibScalar
brzaccVLTcpPortRangeAdd = _BrzaccVLTcpPortRangeAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 4),
    _BrzaccVLTcpPortRangeAdd_Type()
)
brzaccVLTcpPortRangeAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeAdd.setStatus("current")


class _BrzaccVLTcpPortRangeDelete_Type(DisplayString):
    """Custom type brzaccVLTcpPortRangeDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BrzaccVLTcpPortRangeDelete_Type.__name__ = "DisplayString"
_BrzaccVLTcpPortRangeDelete_Object = MibScalar
brzaccVLTcpPortRangeDelete = _BrzaccVLTcpPortRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 5),
    _BrzaccVLTcpPortRangeDelete_Type()
)
brzaccVLTcpPortRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeDelete.setStatus("current")


class _BrzaccVLTcpPortRangeDeleteAll_Type(Integer32):
    """Custom type brzaccVLTcpPortRangeDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1))
    )


_BrzaccVLTcpPortRangeDeleteAll_Type.__name__ = "Integer32"
_BrzaccVLTcpPortRangeDeleteAll_Object = MibScalar
brzaccVLTcpPortRangeDeleteAll = _BrzaccVLTcpPortRangeDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 6),
    _BrzaccVLTcpPortRangeDeleteAll_Type()
)
brzaccVLTcpPortRangeDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTcpPortRangeDeleteAll.setStatus("current")
_BrzaccVLWirelessLinkPrioritization_ObjectIdentity = ObjectIdentity
brzaccVLWirelessLinkPrioritization = _BrzaccVLWirelessLinkPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4)
)


class _BrzaccVLWirelessLinkPrioritizationOption_Type(Integer32):
    """Custom type brzaccVLWirelessLinkPrioritizationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLWirelessLinkPrioritizationOption_Type.__name__ = "Integer32"
_BrzaccVLWirelessLinkPrioritizationOption_Object = MibScalar
brzaccVLWirelessLinkPrioritizationOption = _BrzaccVLWirelessLinkPrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 1),
    _BrzaccVLWirelessLinkPrioritizationOption_Type()
)
brzaccVLWirelessLinkPrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLWirelessLinkPrioritizationOption.setStatus("current")


class _BrzaccVLlowPriorityAIFS_Type(Integer32):
    """Custom type brzaccVLlowPriorityAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_BrzaccVLlowPriorityAIFS_Type.__name__ = "Integer32"
_BrzaccVLlowPriorityAIFS_Object = MibScalar
brzaccVLlowPriorityAIFS = _BrzaccVLlowPriorityAIFS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 2),
    _BrzaccVLlowPriorityAIFS_Type()
)
brzaccVLlowPriorityAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLlowPriorityAIFS.setStatus("current")


class _BrzaccVLHWRetriesHighPriority_Type(Integer32):
    """Custom type brzaccVLHWRetriesHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_BrzaccVLHWRetriesHighPriority_Type.__name__ = "Integer32"
_BrzaccVLHWRetriesHighPriority_Object = MibScalar
brzaccVLHWRetriesHighPriority = _BrzaccVLHWRetriesHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 3),
    _BrzaccVLHWRetriesHighPriority_Type()
)
brzaccVLHWRetriesHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLHWRetriesHighPriority.setStatus("current")


class _BrzaccVLHWRetriesLowPriority_Type(Integer32):
    """Custom type brzaccVLHWRetriesLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_BrzaccVLHWRetriesLowPriority_Type.__name__ = "Integer32"
_BrzaccVLHWRetriesLowPriority_Object = MibScalar
brzaccVLHWRetriesLowPriority = _BrzaccVLHWRetriesLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 4),
    _BrzaccVLHWRetriesLowPriority_Type()
)
brzaccVLHWRetriesLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLHWRetriesLowPriority.setStatus("current")


class _BrzaccVLAUBurstDurationHighPriority_Type(Integer32):
    """Custom type brzaccVLAUBurstDurationHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BrzaccVLAUBurstDurationHighPriority_Type.__name__ = "Integer32"
_BrzaccVLAUBurstDurationHighPriority_Object = MibScalar
brzaccVLAUBurstDurationHighPriority = _BrzaccVLAUBurstDurationHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 5),
    _BrzaccVLAUBurstDurationHighPriority_Type()
)
brzaccVLAUBurstDurationHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUBurstDurationHighPriority.setStatus("current")


class _BrzaccVLAUBurstDurationLowPriority_Type(Integer32):
    """Custom type brzaccVLAUBurstDurationLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BrzaccVLAUBurstDurationLowPriority_Type.__name__ = "Integer32"
_BrzaccVLAUBurstDurationLowPriority_Object = MibScalar
brzaccVLAUBurstDurationLowPriority = _BrzaccVLAUBurstDurationLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 6),
    _BrzaccVLAUBurstDurationLowPriority_Type()
)
brzaccVLAUBurstDurationLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUBurstDurationLowPriority.setStatus("current")


class _BrzaccVLSUBurstDurationHighPriority_Type(Integer32):
    """Custom type brzaccVLSUBurstDurationHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BrzaccVLSUBurstDurationHighPriority_Type.__name__ = "Integer32"
_BrzaccVLSUBurstDurationHighPriority_Object = MibScalar
brzaccVLSUBurstDurationHighPriority = _BrzaccVLSUBurstDurationHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 7),
    _BrzaccVLSUBurstDurationHighPriority_Type()
)
brzaccVLSUBurstDurationHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUBurstDurationHighPriority.setStatus("current")


class _BrzaccVLSUBurstDurationLowPriority_Type(Integer32):
    """Custom type brzaccVLSUBurstDurationLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BrzaccVLSUBurstDurationLowPriority_Type.__name__ = "Integer32"
_BrzaccVLSUBurstDurationLowPriority_Object = MibScalar
brzaccVLSUBurstDurationLowPriority = _BrzaccVLSUBurstDurationLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 8),
    _BrzaccVLSUBurstDurationLowPriority_Type()
)
brzaccVLSUBurstDurationLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUBurstDurationLowPriority.setStatus("current")
_BrzaccVLTrafficPriIpRange_ObjectIdentity = ObjectIdentity
brzaccVLTrafficPriIpRange = _BrzaccVLTrafficPriIpRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 5)
)


class _BrzaccVLTrafficPriIpRangeOption_Type(Integer32):
    """Custom type brzaccVLTrafficPriIpRangeOption based on Integer32"""
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
        *(("disable", 1),
          ("ipDestination", 3),
          ("ipSource", 2),
          ("ipSourceOrDestination", 4))
    )


_BrzaccVLTrafficPriIpRangeOption_Type.__name__ = "Integer32"
_BrzaccVLTrafficPriIpRangeOption_Object = MibScalar
brzaccVLTrafficPriIpRangeOption = _BrzaccVLTrafficPriIpRangeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 5, 1),
    _BrzaccVLTrafficPriIpRangeOption_Type()
)
brzaccVLTrafficPriIpRangeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTrafficPriIpRangeOption.setStatus("current")
_BrzaccVLTrafficPriIpRangeIpAddress_Type = IpAddress
_BrzaccVLTrafficPriIpRangeIpAddress_Object = MibScalar
brzaccVLTrafficPriIpRangeIpAddress = _BrzaccVLTrafficPriIpRangeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 5, 2),
    _BrzaccVLTrafficPriIpRangeIpAddress_Type()
)
brzaccVLTrafficPriIpRangeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTrafficPriIpRangeIpAddress.setStatus("current")
_BrzaccVLTrafficPriIpRangeIpMask_Type = IpAddress
_BrzaccVLTrafficPriIpRangeIpMask_Object = MibScalar
brzaccVLTrafficPriIpRangeIpMask = _BrzaccVLTrafficPriIpRangeIpMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 5, 3),
    _BrzaccVLTrafficPriIpRangeIpMask_Type()
)
brzaccVLTrafficPriIpRangeIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLTrafficPriIpRangeIpMask.setStatus("current")
_BrzaccVLDrap_ObjectIdentity = ObjectIdentity
brzaccVLDrap = _BrzaccVLDrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11)
)


class _BrzaccVLDrapSupport_Type(Integer32):
    """Custom type brzaccVLDrapSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDrapSupport_Type.__name__ = "Integer32"
_BrzaccVLDrapSupport_Object = MibScalar
brzaccVLDrapSupport = _BrzaccVLDrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 1),
    _BrzaccVLDrapSupport_Type()
)
brzaccVLDrapSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDrapSupport.setStatus("current")


class _BrzaccVLDrapUdpPort_Type(Integer32):
    """Custom type brzaccVLDrapUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 8200),
    )


_BrzaccVLDrapUdpPort_Type.__name__ = "Integer32"
_BrzaccVLDrapUdpPort_Object = MibScalar
brzaccVLDrapUdpPort = _BrzaccVLDrapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 2),
    _BrzaccVLDrapUdpPort_Type()
)
brzaccVLDrapUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDrapUdpPort.setStatus("current")


class _BrzaccVLDrapMaxNumberOfVoiceCalls_Type(Integer32):
    """Custom type brzaccVLDrapMaxNumberOfVoiceCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrzaccVLDrapMaxNumberOfVoiceCalls_Type.__name__ = "Integer32"
_BrzaccVLDrapMaxNumberOfVoiceCalls_Object = MibScalar
brzaccVLDrapMaxNumberOfVoiceCalls = _BrzaccVLDrapMaxNumberOfVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 3),
    _BrzaccVLDrapMaxNumberOfVoiceCalls_Type()
)
brzaccVLDrapMaxNumberOfVoiceCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDrapMaxNumberOfVoiceCalls.setStatus("current")


class _BrzaccVLDrapTTL_Type(Integer32):
    """Custom type brzaccVLDrapTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrzaccVLDrapTTL_Type.__name__ = "Integer32"
_BrzaccVLDrapTTL_Object = MibScalar
brzaccVLDrapTTL = _BrzaccVLDrapTTL_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 4),
    _BrzaccVLDrapTTL_Type()
)
brzaccVLDrapTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDrapTTL.setStatus("current")
_BrzaccVLDrapNoOfActiveVoiceCalls_Type = Integer32
_BrzaccVLDrapNoOfActiveVoiceCalls_Object = MibScalar
brzaccVLDrapNoOfActiveVoiceCalls = _BrzaccVLDrapNoOfActiveVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 5),
    _BrzaccVLDrapNoOfActiveVoiceCalls_Type()
)
brzaccVLDrapNoOfActiveVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDrapNoOfActiveVoiceCalls.setStatus("current")


class _BrzaccVLLowPriorityTrafficMinimumPercent_Type(Integer32):
    """Custom type brzaccVLLowPriorityTrafficMinimumPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrzaccVLLowPriorityTrafficMinimumPercent_Type.__name__ = "Integer32"
_BrzaccVLLowPriorityTrafficMinimumPercent_Object = MibScalar
brzaccVLLowPriorityTrafficMinimumPercent = _BrzaccVLLowPriorityTrafficMinimumPercent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 12),
    _BrzaccVLLowPriorityTrafficMinimumPercent_Type()
)
brzaccVLLowPriorityTrafficMinimumPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLLowPriorityTrafficMinimumPercent.setStatus("current")
_BrzaccVLSUEZMirDownlink_Type = Integer32
_BrzaccVLSUEZMirDownlink_Object = MibScalar
brzaccVLSUEZMirDownlink = _BrzaccVLSUEZMirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 13),
    _BrzaccVLSUEZMirDownlink_Type()
)
brzaccVLSUEZMirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUEZMirDownlink.setStatus("current")


class _BrzaccVLMIRThresholdPercent_Type(Integer32):
    """Custom type brzaccVLMIRThresholdPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrzaccVLMIRThresholdPercent_Type.__name__ = "Integer32"
_BrzaccVLMIRThresholdPercent_Object = MibScalar
brzaccVLMIRThresholdPercent = _BrzaccVLMIRThresholdPercent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 14),
    _BrzaccVLMIRThresholdPercent_Type()
)
brzaccVLMIRThresholdPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMIRThresholdPercent.setStatus("current")
_BrzaccVLProportionalIRParameters_ObjectIdentity = ObjectIdentity
brzaccVLProportionalIRParameters = _BrzaccVLProportionalIRParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 15)
)


class _BrzaccVLProportionalIRFactor_Type(Integer32):
    """Custom type brzaccVLProportionalIRFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrzaccVLProportionalIRFactor_Type.__name__ = "Integer32"
_BrzaccVLProportionalIRFactor_Object = MibScalar
brzaccVLProportionalIRFactor = _BrzaccVLProportionalIRFactor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 15, 1),
    _BrzaccVLProportionalIRFactor_Type()
)
brzaccVLProportionalIRFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLProportionalIRFactor.setStatus("current")


class _BrzaccVLProportionalIRUpdatePeriod_Type(Integer32):
    """Custom type brzaccVLProportionalIRUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BrzaccVLProportionalIRUpdatePeriod_Type.__name__ = "Integer32"
_BrzaccVLProportionalIRUpdatePeriod_Object = MibScalar
brzaccVLProportionalIRUpdatePeriod = _BrzaccVLProportionalIRUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 15, 2),
    _BrzaccVLProportionalIRUpdatePeriod_Type()
)
brzaccVLProportionalIRUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLProportionalIRUpdatePeriod.setStatus("current")


class _BrzaccVLProportionalIRThresholdPercentage_Type(Integer32):
    """Custom type brzaccVLProportionalIRThresholdPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BrzaccVLProportionalIRThresholdPercentage_Type.__name__ = "Integer32"
_BrzaccVLProportionalIRThresholdPercentage_Object = MibScalar
brzaccVLProportionalIRThresholdPercentage = _BrzaccVLProportionalIRThresholdPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 15, 3),
    _BrzaccVLProportionalIRThresholdPercentage_Type()
)
brzaccVLProportionalIRThresholdPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLProportionalIRThresholdPercentage.setStatus("current")


class _BrzaccVLProportionalIRThresholdRate_Type(Integer32):
    """Custom type brzaccVLProportionalIRThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLProportionalIRThresholdRate_Type.__name__ = "Integer32"
_BrzaccVLProportionalIRThresholdRate_Object = MibScalar
brzaccVLProportionalIRThresholdRate = _BrzaccVLProportionalIRThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 15, 4),
    _BrzaccVLProportionalIRThresholdRate_Type()
)
brzaccVLProportionalIRThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLProportionalIRThresholdRate.setStatus("current")
_BrzaccVLUserFilterParams_ObjectIdentity = ObjectIdentity
brzaccVLUserFilterParams = _BrzaccVLUserFilterParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8)
)


class _BrzaccVLUserFilterOption_Type(Integer32):
    """Custom type brzaccVLUserFilterOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ipOnly", 2),
          ("na", 255),
          ("pPPoEOnly", 4),
          ("userDefinedAddrOnly", 3))
    )


_BrzaccVLUserFilterOption_Type.__name__ = "Integer32"
_BrzaccVLUserFilterOption_Object = MibScalar
brzaccVLUserFilterOption = _BrzaccVLUserFilterOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 1),
    _BrzaccVLUserFilterOption_Type()
)
brzaccVLUserFilterOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLUserFilterOption.setStatus("current")
_BrzaccVLIpFilterTable_Object = MibTable
brzaccVLIpFilterTable = _BrzaccVLIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    brzaccVLIpFilterTable.setStatus("current")
_BrzaccVLIpFilterEntry_Object = MibTableRow
brzaccVLIpFilterEntry = _BrzaccVLIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1)
)
brzaccVLIpFilterEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLIpFilterIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLIpFilterEntry.setStatus("current")
_BrzaccVLIpID_Type = IpAddress
_BrzaccVLIpID_Object = MibTableColumn
brzaccVLIpID = _BrzaccVLIpID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 1),
    _BrzaccVLIpID_Type()
)
brzaccVLIpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLIpID.setStatus("current")
_BrzaccVLMaskID_Type = IpAddress
_BrzaccVLMaskID_Object = MibTableColumn
brzaccVLMaskID = _BrzaccVLMaskID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 2),
    _BrzaccVLMaskID_Type()
)
brzaccVLMaskID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaskID.setStatus("current")
_BrzaccVLIpFilterRange_Type = Integer32
_BrzaccVLIpFilterRange_Object = MibTableColumn
brzaccVLIpFilterRange = _BrzaccVLIpFilterRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 3),
    _BrzaccVLIpFilterRange_Type()
)
brzaccVLIpFilterRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLIpFilterRange.setStatus("current")


class _BrzaccVLIpFilterIdx_Type(Integer32):
    """Custom type brzaccVLIpFilterIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLIpFilterIdx_Type.__name__ = "Integer32"
_BrzaccVLIpFilterIdx_Object = MibTableColumn
brzaccVLIpFilterIdx = _BrzaccVLIpFilterIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 4),
    _BrzaccVLIpFilterIdx_Type()
)
brzaccVLIpFilterIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLIpFilterIdx.setStatus("current")


class _BrzaccVLDeleteOneUserFilter_Type(Integer32):
    """Custom type brzaccVLDeleteOneUserFilter based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 9),
          ("deleteeighthEntry", 8),
          ("deletefifthEntry", 5),
          ("deletefirstEntry", 1),
          ("deletefourthEntry", 4),
          ("deletesecondEntry", 2),
          ("deleteseventhEntry", 7),
          ("deletesixthEntry", 6),
          ("deletethirdEntry", 3),
          ("na", 255))
    )


_BrzaccVLDeleteOneUserFilter_Type.__name__ = "Integer32"
_BrzaccVLDeleteOneUserFilter_Object = MibScalar
brzaccVLDeleteOneUserFilter = _BrzaccVLDeleteOneUserFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 3),
    _BrzaccVLDeleteOneUserFilter_Type()
)
brzaccVLDeleteOneUserFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteOneUserFilter.setStatus("current")


class _BrzaccVLDeleteAllUserFilters_Type(Integer32):
    """Custom type brzaccVLDeleteAllUserFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 2),
          ("deleteAll", 1),
          ("na", 255))
    )


_BrzaccVLDeleteAllUserFilters_Type.__name__ = "Integer32"
_BrzaccVLDeleteAllUserFilters_Object = MibScalar
brzaccVLDeleteAllUserFilters = _BrzaccVLDeleteAllUserFilters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 4),
    _BrzaccVLDeleteAllUserFilters_Type()
)
brzaccVLDeleteAllUserFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDeleteAllUserFilters.setStatus("current")


class _BrzaccVLDHCPUnicastOverrideFilter_Type(Integer32):
    """Custom type brzaccVLDHCPUnicastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDHCPUnicastOverrideFilter_Type.__name__ = "Integer32"
_BrzaccVLDHCPUnicastOverrideFilter_Object = MibScalar
brzaccVLDHCPUnicastOverrideFilter = _BrzaccVLDHCPUnicastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 5),
    _BrzaccVLDHCPUnicastOverrideFilter_Type()
)
brzaccVLDHCPUnicastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDHCPUnicastOverrideFilter.setStatus("current")
_BrzaccVLNewIpFilterTable_Object = MibTable
brzaccVLNewIpFilterTable = _BrzaccVLNewIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    brzaccVLNewIpFilterTable.setStatus("current")
_BrzaccVLNewIpFilterEntry_Object = MibTableRow
brzaccVLNewIpFilterEntry = _BrzaccVLNewIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6, 1)
)
brzaccVLNewIpFilterEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewIpID"),
)
if mibBuilder.loadTexts:
    brzaccVLNewIpFilterEntry.setStatus("current")
_BrzaccVLNewIpID_Type = IpAddress
_BrzaccVLNewIpID_Object = MibTableColumn
brzaccVLNewIpID = _BrzaccVLNewIpID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6, 1, 1),
    _BrzaccVLNewIpID_Type()
)
brzaccVLNewIpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewIpID.setStatus("current")
_BrzaccVLNewMaskID_Type = IpAddress
_BrzaccVLNewMaskID_Object = MibTableColumn
brzaccVLNewMaskID = _BrzaccVLNewMaskID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6, 1, 2),
    _BrzaccVLNewMaskID_Type()
)
brzaccVLNewMaskID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewMaskID.setStatus("current")
_BrzaccVLNewIpFilterRange_Type = Integer32
_BrzaccVLNewIpFilterRange_Object = MibTableColumn
brzaccVLNewIpFilterRange = _BrzaccVLNewIpFilterRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6, 1, 3),
    _BrzaccVLNewIpFilterRange_Type()
)
brzaccVLNewIpFilterRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewIpFilterRange.setStatus("current")


class _BrzaccVLNewIpFilterCommand_Type(Integer32):
    """Custom type brzaccVLNewIpFilterCommand based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_BrzaccVLNewIpFilterCommand_Type.__name__ = "Integer32"
_BrzaccVLNewIpFilterCommand_Object = MibTableColumn
brzaccVLNewIpFilterCommand = _BrzaccVLNewIpFilterCommand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 6, 1, 4),
    _BrzaccVLNewIpFilterCommand_Type()
)
brzaccVLNewIpFilterCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNewIpFilterCommand.setStatus("current")


class _BrzaccVLDHCPPPPoEOverrideFilter_Type(Integer32):
    """Custom type brzaccVLDHCPPPPoEOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLDHCPPPPoEOverrideFilter_Type.__name__ = "Integer32"
_BrzaccVLDHCPPPPoEOverrideFilter_Object = MibScalar
brzaccVLDHCPPPPoEOverrideFilter = _BrzaccVLDHCPPPPoEOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 7),
    _BrzaccVLDHCPPPPoEOverrideFilter_Type()
)
brzaccVLDHCPPPPoEOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDHCPPPPoEOverrideFilter.setStatus("current")
_BrzaccVLSecurityParameters_ObjectIdentity = ObjectIdentity
brzaccVLSecurityParameters = _BrzaccVLSecurityParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9)
)


class _BrzaccVLAuthenticationAlgorithm_Type(Integer32):
    """Custom type brzaccVLAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_BrzaccVLAuthenticationAlgorithm_Type.__name__ = "Integer32"
_BrzaccVLAuthenticationAlgorithm_Object = MibScalar
brzaccVLAuthenticationAlgorithm = _BrzaccVLAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 1),
    _BrzaccVLAuthenticationAlgorithm_Type()
)
brzaccVLAuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAuthenticationAlgorithm.setStatus("current")
_BrzaccVLSUDefaultKeyID_Type = Integer32
_BrzaccVLSUDefaultKeyID_Object = MibScalar
brzaccVLSUDefaultKeyID = _BrzaccVLSUDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 2),
    _BrzaccVLSUDefaultKeyID_Type()
)
brzaccVLSUDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSUDefaultKeyID.setStatus("current")


class _BrzaccVLDataEncryptionOption_Type(Integer32):
    """Custom type brzaccVLDataEncryptionOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLDataEncryptionOption_Type.__name__ = "Integer32"
_BrzaccVLDataEncryptionOption_Object = MibScalar
brzaccVLDataEncryptionOption = _BrzaccVLDataEncryptionOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 3),
    _BrzaccVLDataEncryptionOption_Type()
)
brzaccVLDataEncryptionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLDataEncryptionOption.setStatus("current")
_BrzaccVLAUDefaultMulticastKeyID_Type = Integer32
_BrzaccVLAUDefaultMulticastKeyID_Object = MibScalar
brzaccVLAUDefaultMulticastKeyID = _BrzaccVLAUDefaultMulticastKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 4),
    _BrzaccVLAUDefaultMulticastKeyID_Type()
)
brzaccVLAUDefaultMulticastKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUDefaultMulticastKeyID.setStatus("current")


class _BrzaccVLSecurityMode_Type(Integer32):
    """Custom type brzaccVLSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aesOCB", 2),
          ("fips197", 3),
          ("wep", 1))
    )


_BrzaccVLSecurityMode_Type.__name__ = "Integer32"
_BrzaccVLSecurityMode_Object = MibScalar
brzaccVLSecurityMode = _BrzaccVLSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 5),
    _BrzaccVLSecurityMode_Type()
)
brzaccVLSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSecurityMode.setStatus("current")


class _BrzaccVLAuthenticationPromiscuousMode_Type(Integer32):
    """Custom type brzaccVLAuthenticationPromiscuousMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLAuthenticationPromiscuousMode_Type.__name__ = "Integer32"
_BrzaccVLAuthenticationPromiscuousMode_Object = MibScalar
brzaccVLAuthenticationPromiscuousMode = _BrzaccVLAuthenticationPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 6),
    _BrzaccVLAuthenticationPromiscuousMode_Type()
)
brzaccVLAuthenticationPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAuthenticationPromiscuousMode.setStatus("current")


class _BrzaccVLKey1_Type(DisplayString):
    """Custom type brzaccVLKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrzaccVLKey1_Type.__name__ = "DisplayString"
_BrzaccVLKey1_Object = MibScalar
brzaccVLKey1 = _BrzaccVLKey1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 7),
    _BrzaccVLKey1_Type()
)
brzaccVLKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLKey1.setStatus("current")


class _BrzaccVLKey2_Type(DisplayString):
    """Custom type brzaccVLKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrzaccVLKey2_Type.__name__ = "DisplayString"
_BrzaccVLKey2_Object = MibScalar
brzaccVLKey2 = _BrzaccVLKey2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 8),
    _BrzaccVLKey2_Type()
)
brzaccVLKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLKey2.setStatus("current")


class _BrzaccVLKey3_Type(DisplayString):
    """Custom type brzaccVLKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrzaccVLKey3_Type.__name__ = "DisplayString"
_BrzaccVLKey3_Object = MibScalar
brzaccVLKey3 = _BrzaccVLKey3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 9),
    _BrzaccVLKey3_Type()
)
brzaccVLKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLKey3.setStatus("current")


class _BrzaccVLKey4_Type(DisplayString):
    """Custom type brzaccVLKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrzaccVLKey4_Type.__name__ = "DisplayString"
_BrzaccVLKey4_Object = MibScalar
brzaccVLKey4 = _BrzaccVLKey4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 10),
    _BrzaccVLKey4_Type()
)
brzaccVLKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLKey4.setStatus("current")


class _BrzaccVLSecurityModeSupport_Type(Integer32):
    """Custom type brzaccVLSecurityModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BrzaccVLSecurityModeSupport_Type.__name__ = "Integer32"
_BrzaccVLSecurityModeSupport_Object = MibScalar
brzaccVLSecurityModeSupport = _BrzaccVLSecurityModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 12),
    _BrzaccVLSecurityModeSupport_Type()
)
brzaccVLSecurityModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSecurityModeSupport.setStatus("current")
_BrzaccVLPerformanceParams_ObjectIdentity = ObjectIdentity
brzaccVLPerformanceParams = _BrzaccVLPerformanceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10)
)
_BrzaccVLRTSThreshold_Type = Integer32
_BrzaccVLRTSThreshold_Object = MibScalar
brzaccVLRTSThreshold = _BrzaccVLRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 1),
    _BrzaccVLRTSThreshold_Type()
)
brzaccVLRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLRTSThreshold.setStatus("current")
_BrzaccVLMinContentionWindow_Type = Integer32
_BrzaccVLMinContentionWindow_Object = MibScalar
brzaccVLMinContentionWindow = _BrzaccVLMinContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 3),
    _BrzaccVLMinContentionWindow_Type()
)
brzaccVLMinContentionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMinContentionWindow.setStatus("current")
_BrzaccVLMaxContentionWindow_Type = Integer32
_BrzaccVLMaxContentionWindow_Object = MibScalar
brzaccVLMaxContentionWindow = _BrzaccVLMaxContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 4),
    _BrzaccVLMaxContentionWindow_Type()
)
brzaccVLMaxContentionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaxContentionWindow.setStatus("current")


class _BrzaccVLMaximumModulationLevel_Type(Integer32):
    """Custom type brzaccVLMaximumModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLMaximumModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLMaximumModulationLevel_Object = MibScalar
brzaccVLMaximumModulationLevel = _BrzaccVLMaximumModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 5),
    _BrzaccVLMaximumModulationLevel_Type()
)
brzaccVLMaximumModulationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMaximumModulationLevel.setStatus("current")


class _BrzaccVLMulticastModulationLevel_Type(Integer32):
    """Custom type brzaccVLMulticastModulationLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BrzaccVLMulticastModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLMulticastModulationLevel_Object = MibScalar
brzaccVLMulticastModulationLevel = _BrzaccVLMulticastModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 6),
    _BrzaccVLMulticastModulationLevel_Type()
)
brzaccVLMulticastModulationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMulticastModulationLevel.setStatus("current")
_BrzaccVLAvgSNRMemoryFactor_Type = DisplayString
_BrzaccVLAvgSNRMemoryFactor_Object = MibScalar
brzaccVLAvgSNRMemoryFactor = _BrzaccVLAvgSNRMemoryFactor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 7),
    _BrzaccVLAvgSNRMemoryFactor_Type()
)
brzaccVLAvgSNRMemoryFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAvgSNRMemoryFactor.setStatus("current")
_BrzaccVLHardwareRetries_Type = Integer32
_BrzaccVLHardwareRetries_Object = MibScalar
brzaccVLHardwareRetries = _BrzaccVLHardwareRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 8),
    _BrzaccVLHardwareRetries_Type()
)
brzaccVLHardwareRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLHardwareRetries.setStatus("current")
_BrzaccVLAdaptiveModulationParams_ObjectIdentity = ObjectIdentity
brzaccVLAdaptiveModulationParams = _BrzaccVLAdaptiveModulationParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9)
)


class _BrzaccVLAdaptiveModulationAlgorithmOption_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationAlgorithmOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdaptiveModulationAlgorithmOption_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationAlgorithmOption_Object = MibScalar
brzaccVLAdaptiveModulationAlgorithmOption = _BrzaccVLAdaptiveModulationAlgorithmOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 1),
    _BrzaccVLAdaptiveModulationAlgorithmOption_Type()
)
brzaccVLAdaptiveModulationAlgorithmOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationAlgorithmOption.setStatus("current")


class _BrzaccVLSoftwareRetrySupport_Type(Integer32):
    """Custom type brzaccVLSoftwareRetrySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLSoftwareRetrySupport_Type.__name__ = "Integer32"
_BrzaccVLSoftwareRetrySupport_Object = MibScalar
brzaccVLSoftwareRetrySupport = _BrzaccVLSoftwareRetrySupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 2),
    _BrzaccVLSoftwareRetrySupport_Type()
)
brzaccVLSoftwareRetrySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLSoftwareRetrySupport.setStatus("current")


class _BrzaccVLNumOfSoftwareRetries_Type(Integer32):
    """Custom type brzaccVLNumOfSoftwareRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzaccVLNumOfSoftwareRetries_Type.__name__ = "Integer32"
_BrzaccVLNumOfSoftwareRetries_Object = MibScalar
brzaccVLNumOfSoftwareRetries = _BrzaccVLNumOfSoftwareRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 3),
    _BrzaccVLNumOfSoftwareRetries_Type()
)
brzaccVLNumOfSoftwareRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLNumOfSoftwareRetries.setStatus("current")
_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type = Integer32
_BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object = MibScalar
brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages = _BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 4),
    _BrzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type()
)
brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setStatus("current")


class _BrzaccVLAdaptiveModulationDecisionThresholds_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationDecisionThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("na", 255),
          ("normal", 1))
    )


_BrzaccVLAdaptiveModulationDecisionThresholds_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationDecisionThresholds_Object = MibScalar
brzaccVLAdaptiveModulationDecisionThresholds = _BrzaccVLAdaptiveModulationDecisionThresholds_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 5),
    _BrzaccVLAdaptiveModulationDecisionThresholds_Type()
)
brzaccVLAdaptiveModulationDecisionThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationDecisionThresholds.setStatus("current")


class _BrzaccVLAdaptiveModulationHistorySize_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 25),
    )


_BrzaccVLAdaptiveModulationHistorySize_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationHistorySize_Object = MibScalar
brzaccVLAdaptiveModulationHistorySize = _BrzaccVLAdaptiveModulationHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 7),
    _BrzaccVLAdaptiveModulationHistorySize_Type()
)
brzaccVLAdaptiveModulationHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationHistorySize.setStatus("current")


class _BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationPacketThresholdToTestUpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Object = MibScalar
brzaccVLAdaptiveModulationPacketThresholdToTestUpRate = _BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 8),
    _BrzaccVLAdaptiveModulationPacketThresholdToTestUpRate_Type()
)
brzaccVLAdaptiveModulationPacketThresholdToTestUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationPacketThresholdToTestUpRate.setStatus("current")


class _BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationPacketNoOnUpperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Object = MibScalar
brzaccVLAdaptiveModulationPacketNoOnUpperRate = _BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 9),
    _BrzaccVLAdaptiveModulationPacketNoOnUpperRate_Type()
)
brzaccVLAdaptiveModulationPacketNoOnUpperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationPacketNoOnUpperRate.setStatus("current")


class _BrzaccVLAdaptiveModulationAlgorithm_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveModulation", 1),
          ("na", 255),
          ("statisticsBasedRateControl", 2))
    )


_BrzaccVLAdaptiveModulationAlgorithm_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationAlgorithm_Object = MibScalar
brzaccVLAdaptiveModulationAlgorithm = _BrzaccVLAdaptiveModulationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 10),
    _BrzaccVLAdaptiveModulationAlgorithm_Type()
)
brzaccVLAdaptiveModulationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationAlgorithm.setStatus("current")


class _BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationRetriesOnLowerModulations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Object = MibScalar
brzaccVLAdaptiveModulationRetriesOnLowerModulations = _BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 11),
    _BrzaccVLAdaptiveModulationRetriesOnLowerModulations_Type()
)
brzaccVLAdaptiveModulationRetriesOnLowerModulations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationRetriesOnLowerModulations.setStatus("current")


class _BrzaccVLAdaptiveModulationRTSDurationMode_Type(Integer32):
    """Custom type brzaccVLAdaptiveModulationRTSDurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longRTSDuration", 2),
          ("shortRTSDuration", 1))
    )


_BrzaccVLAdaptiveModulationRTSDurationMode_Type.__name__ = "Integer32"
_BrzaccVLAdaptiveModulationRTSDurationMode_Object = MibScalar
brzaccVLAdaptiveModulationRTSDurationMode = _BrzaccVLAdaptiveModulationRTSDurationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 12),
    _BrzaccVLAdaptiveModulationRTSDurationMode_Type()
)
brzaccVLAdaptiveModulationRTSDurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAdaptiveModulationRTSDurationMode.setStatus("current")
_BrzaccVLBurstMode_ObjectIdentity = ObjectIdentity
brzaccVLBurstMode = _BrzaccVLBurstMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10)
)


class _BrzaccVLBurstModeOption_Type(Integer32):
    """Custom type brzaccVLBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLBurstModeOption_Type.__name__ = "Integer32"
_BrzaccVLBurstModeOption_Object = MibScalar
brzaccVLBurstModeOption = _BrzaccVLBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10, 1),
    _BrzaccVLBurstModeOption_Type()
)
brzaccVLBurstModeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBurstModeOption.setStatus("current")
_BrzaccVLBurstInterval_Type = Integer32
_BrzaccVLBurstInterval_Object = MibScalar
brzaccVLBurstInterval = _BrzaccVLBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10, 2),
    _BrzaccVLBurstInterval_Type()
)
brzaccVLBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLBurstInterval.setStatus("current")
_BrzaccVLConcatenationParameters_ObjectIdentity = ObjectIdentity
brzaccVLConcatenationParameters = _BrzaccVLConcatenationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11)
)


class _BrzaccVLConcatenationOption_Type(Integer32):
    """Custom type brzaccVLConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLConcatenationOption_Type.__name__ = "Integer32"
_BrzaccVLConcatenationOption_Object = MibScalar
brzaccVLConcatenationOption = _BrzaccVLConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 1),
    _BrzaccVLConcatenationOption_Type()
)
brzaccVLConcatenationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLConcatenationOption.setStatus("current")


class _BrzaccVLConcatenationMaximumNumberOfFrames_Type(Integer32):
    """Custom type brzaccVLConcatenationMaximumNumberOfFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_BrzaccVLConcatenationMaximumNumberOfFrames_Type.__name__ = "Integer32"
_BrzaccVLConcatenationMaximumNumberOfFrames_Object = MibScalar
brzaccVLConcatenationMaximumNumberOfFrames = _BrzaccVLConcatenationMaximumNumberOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 2),
    _BrzaccVLConcatenationMaximumNumberOfFrames_Type()
)
brzaccVLConcatenationMaximumNumberOfFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLConcatenationMaximumNumberOfFrames.setStatus("current")
_BrzaccVLConcatenationMaxFrameSize_Type = Integer32
_BrzaccVLConcatenationMaxFrameSize_Object = MibScalar
brzaccVLConcatenationMaxFrameSize = _BrzaccVLConcatenationMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 3),
    _BrzaccVLConcatenationMaxFrameSize_Type()
)
brzaccVLConcatenationMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLConcatenationMaxFrameSize.setStatus("current")


class _BrzaccVLControlModulationLevel_Type(Integer32):
    """Custom type brzaccVLControlModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicRate", 1),
          ("modulationLevel1", 2))
    )


_BrzaccVLControlModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLControlModulationLevel_Object = MibScalar
brzaccVLControlModulationLevel = _BrzaccVLControlModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 13),
    _BrzaccVLControlModulationLevel_Type()
)
brzaccVLControlModulationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLControlModulationLevel.setStatus("current")


class _BrzaccVLEthernetFrameSize_Type(Integer32):
    """Custom type brzaccVLEthernetFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size1600", 1),
          ("size2000", 2))
    )


_BrzaccVLEthernetFrameSize_Type.__name__ = "Integer32"
_BrzaccVLEthernetFrameSize_Object = MibScalar
brzaccVLEthernetFrameSize = _BrzaccVLEthernetFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 14),
    _BrzaccVLEthernetFrameSize_Type()
)
brzaccVLEthernetFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLEthernetFrameSize.setStatus("current")
_BrzaccVLRunningEthernetFrameSize_Type = Integer32
_BrzaccVLRunningEthernetFrameSize_Object = MibScalar
brzaccVLRunningEthernetFrameSize = _BrzaccVLRunningEthernetFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 15),
    _BrzaccVLRunningEthernetFrameSize_Type()
)
brzaccVLRunningEthernetFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRunningEthernetFrameSize.setStatus("current")
_BrzaccVLSiteSurvey_ObjectIdentity = ObjectIdentity
brzaccVLSiteSurvey = _BrzaccVLSiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11)
)
_BrzaccVLAverageReceiveSNR_Type = Integer32
_BrzaccVLAverageReceiveSNR_Object = MibScalar
brzaccVLAverageReceiveSNR = _BrzaccVLAverageReceiveSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 1),
    _BrzaccVLAverageReceiveSNR_Type()
)
brzaccVLAverageReceiveSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAverageReceiveSNR.setStatus("current")
_BrzaccVLTrafficStatistics_ObjectIdentity = ObjectIdentity
brzaccVLTrafficStatistics = _BrzaccVLTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2)
)


class _BrzaccVLResetTrafficCounters_Type(Integer32):
    """Custom type brzaccVLResetTrafficCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("reset", 1))
    )


_BrzaccVLResetTrafficCounters_Type.__name__ = "Integer32"
_BrzaccVLResetTrafficCounters_Object = MibScalar
brzaccVLResetTrafficCounters = _BrzaccVLResetTrafficCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 1),
    _BrzaccVLResetTrafficCounters_Type()
)
brzaccVLResetTrafficCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLResetTrafficCounters.setStatus("current")
_BrzaccVLEthCounters_ObjectIdentity = ObjectIdentity
brzaccVLEthCounters = _BrzaccVLEthCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2)
)
_BrzaccVLTotalRxFramesViaEthernet_Type = Counter32
_BrzaccVLTotalRxFramesViaEthernet_Object = MibScalar
brzaccVLTotalRxFramesViaEthernet = _BrzaccVLTotalRxFramesViaEthernet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2, 1),
    _BrzaccVLTotalRxFramesViaEthernet_Type()
)
brzaccVLTotalRxFramesViaEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxFramesViaEthernet.setStatus("current")
_BrzaccVLTxWirelessToEthernet_Type = Counter32
_BrzaccVLTxWirelessToEthernet_Object = MibScalar
brzaccVLTxWirelessToEthernet = _BrzaccVLTxWirelessToEthernet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2, 2),
    _BrzaccVLTxWirelessToEthernet_Type()
)
brzaccVLTxWirelessToEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTxWirelessToEthernet.setStatus("current")
_BrzaccVLWirelessLinkCounters_ObjectIdentity = ObjectIdentity
brzaccVLWirelessLinkCounters = _BrzaccVLWirelessLinkCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3)
)
_BrzaccVLTxFramesToWireless_ObjectIdentity = ObjectIdentity
brzaccVLTxFramesToWireless = _BrzaccVLTxFramesToWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1)
)
_BrzaccVLAUBeaconsToWireless_Type = Counter32
_BrzaccVLAUBeaconsToWireless_Object = MibScalar
brzaccVLAUBeaconsToWireless = _BrzaccVLAUBeaconsToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 1),
    _BrzaccVLAUBeaconsToWireless_Type()
)
brzaccVLAUBeaconsToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAUBeaconsToWireless.setStatus("current")
_BrzaccVLDataAndOtherMngFramesToWireless_Type = Counter32
_BrzaccVLDataAndOtherMngFramesToWireless_Object = MibScalar
brzaccVLDataAndOtherMngFramesToWireless = _BrzaccVLDataAndOtherMngFramesToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 3),
    _BrzaccVLDataAndOtherMngFramesToWireless_Type()
)
brzaccVLDataAndOtherMngFramesToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDataAndOtherMngFramesToWireless.setStatus("current")
_BrzaccVLTotalTxFramesToWireless_Type = Counter32
_BrzaccVLTotalTxFramesToWireless_Object = MibScalar
brzaccVLTotalTxFramesToWireless = _BrzaccVLTotalTxFramesToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 4),
    _BrzaccVLTotalTxFramesToWireless_Type()
)
brzaccVLTotalTxFramesToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTxFramesToWireless.setStatus("current")
_BrzaccVLTotalTransmittedUnicasts_Type = Counter32
_BrzaccVLTotalTransmittedUnicasts_Object = MibScalar
brzaccVLTotalTransmittedUnicasts = _BrzaccVLTotalTransmittedUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 5),
    _BrzaccVLTotalTransmittedUnicasts_Type()
)
brzaccVLTotalTransmittedUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTransmittedUnicasts.setStatus("current")
_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Type = Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesDouble_Object = MibScalar
brzaccVLTotalTransmittedConcatenatedFramesDouble = _BrzaccVLTotalTransmittedConcatenatedFramesDouble_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 6),
    _BrzaccVLTotalTransmittedConcatenatedFramesDouble_Type()
)
brzaccVLTotalTransmittedConcatenatedFramesDouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTransmittedConcatenatedFramesDouble.setStatus("current")
_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Type = Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesSingle_Object = MibScalar
brzaccVLTotalTransmittedConcatenatedFramesSingle = _BrzaccVLTotalTransmittedConcatenatedFramesSingle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 7),
    _BrzaccVLTotalTransmittedConcatenatedFramesSingle_Type()
)
brzaccVLTotalTransmittedConcatenatedFramesSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTransmittedConcatenatedFramesSingle.setStatus("current")
_BrzaccVLTotalTransmittedConcatenatedFramesMore_Type = Counter32
_BrzaccVLTotalTransmittedConcatenatedFramesMore_Object = MibScalar
brzaccVLTotalTransmittedConcatenatedFramesMore = _BrzaccVLTotalTransmittedConcatenatedFramesMore_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 8),
    _BrzaccVLTotalTransmittedConcatenatedFramesMore_Type()
)
brzaccVLTotalTransmittedConcatenatedFramesMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTransmittedConcatenatedFramesMore.setStatus("current")
_BrzaccVLTotalRxFramesFromWireless_Type = Counter32
_BrzaccVLTotalRxFramesFromWireless_Object = MibScalar
brzaccVLTotalRxFramesFromWireless = _BrzaccVLTotalRxFramesFromWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 2),
    _BrzaccVLTotalRxFramesFromWireless_Type()
)
brzaccVLTotalRxFramesFromWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxFramesFromWireless.setStatus("current")
_BrzaccVLTotalRetransmittedFrames_Type = Counter32
_BrzaccVLTotalRetransmittedFrames_Object = MibScalar
brzaccVLTotalRetransmittedFrames = _BrzaccVLTotalRetransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 3),
    _BrzaccVLTotalRetransmittedFrames_Type()
)
brzaccVLTotalRetransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRetransmittedFrames.setStatus("current")
_BrzaccVLFramesDropped_Type = Counter32
_BrzaccVLFramesDropped_Object = MibScalar
brzaccVLFramesDropped = _BrzaccVLFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 4),
    _BrzaccVLFramesDropped_Type()
)
brzaccVLFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFramesDropped.setStatus("current")
_BrzaccVLDataFramesSubmittedToBridge_ObjectIdentity = ObjectIdentity
brzaccVLDataFramesSubmittedToBridge = _BrzaccVLDataFramesSubmittedToBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5)
)
_BrzaccVLFramesSubmittedViaHighQueue_Type = Counter32
_BrzaccVLFramesSubmittedViaHighQueue_Object = MibScalar
brzaccVLFramesSubmittedViaHighQueue = _BrzaccVLFramesSubmittedViaHighQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 1),
    _BrzaccVLFramesSubmittedViaHighQueue_Type()
)
brzaccVLFramesSubmittedViaHighQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFramesSubmittedViaHighQueue.setStatus("current")
_BrzaccVLFramesSubmittedViaMidQueue_Type = Counter32
_BrzaccVLFramesSubmittedViaMidQueue_Object = MibScalar
brzaccVLFramesSubmittedViaMidQueue = _BrzaccVLFramesSubmittedViaMidQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 2),
    _BrzaccVLFramesSubmittedViaMidQueue_Type()
)
brzaccVLFramesSubmittedViaMidQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFramesSubmittedViaMidQueue.setStatus("current")
_BrzaccVLFramesSubmittedViaLowQueue_Type = Counter32
_BrzaccVLFramesSubmittedViaLowQueue_Object = MibScalar
brzaccVLFramesSubmittedViaLowQueue = _BrzaccVLFramesSubmittedViaLowQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 3),
    _BrzaccVLFramesSubmittedViaLowQueue_Type()
)
brzaccVLFramesSubmittedViaLowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFramesSubmittedViaLowQueue.setStatus("current")
_BrzaccVLTotalNoOfDataFramesSubmitted_Type = Counter32
_BrzaccVLTotalNoOfDataFramesSubmitted_Object = MibScalar
brzaccVLTotalNoOfDataFramesSubmitted = _BrzaccVLTotalNoOfDataFramesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 4),
    _BrzaccVLTotalNoOfDataFramesSubmitted_Type()
)
brzaccVLTotalNoOfDataFramesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalNoOfDataFramesSubmitted.setStatus("current")
_BrzaccVLTotalRecievedDataFrames_Type = Counter32
_BrzaccVLTotalRecievedDataFrames_Object = MibScalar
brzaccVLTotalRecievedDataFrames = _BrzaccVLTotalRecievedDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 6),
    _BrzaccVLTotalRecievedDataFrames_Type()
)
brzaccVLTotalRecievedDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRecievedDataFrames.setStatus("current")
_BrzaccVLRecievedBadFrames_Type = Counter32
_BrzaccVLRecievedBadFrames_Object = MibScalar
brzaccVLRecievedBadFrames = _BrzaccVLRecievedBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 7),
    _BrzaccVLRecievedBadFrames_Type()
)
brzaccVLRecievedBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRecievedBadFrames.setStatus("current")
_BrzaccVLNoOfDuplicateFramesDiscarded_Type = Counter32
_BrzaccVLNoOfDuplicateFramesDiscarded_Object = MibScalar
brzaccVLNoOfDuplicateFramesDiscarded = _BrzaccVLNoOfDuplicateFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 8),
    _BrzaccVLNoOfDuplicateFramesDiscarded_Type()
)
brzaccVLNoOfDuplicateFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoOfDuplicateFramesDiscarded.setStatus("current")
_BrzaccVLNoOfInternallyDiscardedMirCir_Type = Counter32
_BrzaccVLNoOfInternallyDiscardedMirCir_Object = MibScalar
brzaccVLNoOfInternallyDiscardedMirCir = _BrzaccVLNoOfInternallyDiscardedMirCir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 9),
    _BrzaccVLNoOfInternallyDiscardedMirCir_Type()
)
brzaccVLNoOfInternallyDiscardedMirCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNoOfInternallyDiscardedMirCir.setStatus("current")
_BrzaccVLTotalRxConcatenatedFramesDouble_Type = Counter32
_BrzaccVLTotalRxConcatenatedFramesDouble_Object = MibScalar
brzaccVLTotalRxConcatenatedFramesDouble = _BrzaccVLTotalRxConcatenatedFramesDouble_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 10),
    _BrzaccVLTotalRxConcatenatedFramesDouble_Type()
)
brzaccVLTotalRxConcatenatedFramesDouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxConcatenatedFramesDouble.setStatus("current")
_BrzaccVLTotalRxConcatenatedFramesSingle_Type = Counter32
_BrzaccVLTotalRxConcatenatedFramesSingle_Object = MibScalar
brzaccVLTotalRxConcatenatedFramesSingle = _BrzaccVLTotalRxConcatenatedFramesSingle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 11),
    _BrzaccVLTotalRxConcatenatedFramesSingle_Type()
)
brzaccVLTotalRxConcatenatedFramesSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxConcatenatedFramesSingle.setStatus("current")
_BrzaccVLTotalRxConcatenatedFramesMore_Type = Counter32
_BrzaccVLTotalRxConcatenatedFramesMore_Object = MibScalar
brzaccVLTotalRxConcatenatedFramesMore = _BrzaccVLTotalRxConcatenatedFramesMore_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 12),
    _BrzaccVLTotalRxConcatenatedFramesMore_Type()
)
brzaccVLTotalRxConcatenatedFramesMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxConcatenatedFramesMore.setStatus("current")
_BrzaccVLTXRetransmissionPercentage_Type = Counter32
_BrzaccVLTXRetransmissionPercentage_Object = MibScalar
brzaccVLTXRetransmissionPercentage = _BrzaccVLTXRetransmissionPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 13),
    _BrzaccVLTXRetransmissionPercentage_Type()
)
brzaccVLTXRetransmissionPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTXRetransmissionPercentage.setStatus("current")
_BrzaccVLRXCRCPercentage_Type = Counter32
_BrzaccVLRXCRCPercentage_Object = MibScalar
brzaccVLRXCRCPercentage = _BrzaccVLRXCRCPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 14),
    _BrzaccVLRXCRCPercentage_Type()
)
brzaccVLRXCRCPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRXCRCPercentage.setStatus("current")
_BrzaccVLWirelessLinkEvents_ObjectIdentity = ObjectIdentity
brzaccVLWirelessLinkEvents = _BrzaccVLWirelessLinkEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4)
)
_BrzaccVLTxEvents_ObjectIdentity = ObjectIdentity
brzaccVLTxEvents = _BrzaccVLTxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1)
)
_BrzaccVLDroppedFrameEvents_Type = Counter32
_BrzaccVLDroppedFrameEvents_Object = MibScalar
brzaccVLDroppedFrameEvents = _BrzaccVLDroppedFrameEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 1),
    _BrzaccVLDroppedFrameEvents_Type()
)
brzaccVLDroppedFrameEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDroppedFrameEvents.setStatus("current")
_BrzaccVLFramesDelayedDueToSwRetry_Type = Counter32
_BrzaccVLFramesDelayedDueToSwRetry_Object = MibScalar
brzaccVLFramesDelayedDueToSwRetry = _BrzaccVLFramesDelayedDueToSwRetry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 2),
    _BrzaccVLFramesDelayedDueToSwRetry_Type()
)
brzaccVLFramesDelayedDueToSwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLFramesDelayedDueToSwRetry.setStatus("current")
_BrzaccVLUnderrunEvents_Type = Counter32
_BrzaccVLUnderrunEvents_Object = MibScalar
brzaccVLUnderrunEvents = _BrzaccVLUnderrunEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 3),
    _BrzaccVLUnderrunEvents_Type()
)
brzaccVLUnderrunEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUnderrunEvents.setStatus("current")
_BrzaccVLOthersTxEvents_Type = Counter32
_BrzaccVLOthersTxEvents_Object = MibScalar
brzaccVLOthersTxEvents = _BrzaccVLOthersTxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 4),
    _BrzaccVLOthersTxEvents_Type()
)
brzaccVLOthersTxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLOthersTxEvents.setStatus("current")
_BrzaccVLTotalTxEvents_Type = Counter32
_BrzaccVLTotalTxEvents_Object = MibScalar
brzaccVLTotalTxEvents = _BrzaccVLTotalTxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 5),
    _BrzaccVLTotalTxEvents_Type()
)
brzaccVLTotalTxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalTxEvents.setStatus("current")
_BrzaccVLRxEvents_ObjectIdentity = ObjectIdentity
brzaccVLRxEvents = _BrzaccVLRxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2)
)
_BrzaccVLPhyErrors_Type = Counter32
_BrzaccVLPhyErrors_Object = MibScalar
brzaccVLPhyErrors = _BrzaccVLPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 1),
    _BrzaccVLPhyErrors_Type()
)
brzaccVLPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLPhyErrors.setStatus("current")
_BrzaccVLCRCErrors_Type = Counter32
_BrzaccVLCRCErrors_Object = MibScalar
brzaccVLCRCErrors = _BrzaccVLCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 2),
    _BrzaccVLCRCErrors_Type()
)
brzaccVLCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCRCErrors.setStatus("current")
_BrzaccVLOverrunEvents_Type = Counter32
_BrzaccVLOverrunEvents_Object = MibScalar
brzaccVLOverrunEvents = _BrzaccVLOverrunEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 3),
    _BrzaccVLOverrunEvents_Type()
)
brzaccVLOverrunEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLOverrunEvents.setStatus("current")
_BrzaccVLRxDecryptEvents_Type = Counter32
_BrzaccVLRxDecryptEvents_Object = MibScalar
brzaccVLRxDecryptEvents = _BrzaccVLRxDecryptEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 4),
    _BrzaccVLRxDecryptEvents_Type()
)
brzaccVLRxDecryptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLRxDecryptEvents.setStatus("current")
_BrzaccVLTotalRxEvents_Type = Counter32
_BrzaccVLTotalRxEvents_Object = MibScalar
brzaccVLTotalRxEvents = _BrzaccVLTotalRxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 5),
    _BrzaccVLTotalRxEvents_Type()
)
brzaccVLTotalRxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTotalRxEvents.setStatus("current")
_BrzaccVLPerModulationLevelCounters_ObjectIdentity = ObjectIdentity
brzaccVLPerModulationLevelCounters = _BrzaccVLPerModulationLevelCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5)
)


class _BrzaccVLResetPerModulationLevelCounters_Type(Integer32):
    """Custom type brzaccVLResetPerModulationLevelCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("resetCounters", 1))
    )


_BrzaccVLResetPerModulationLevelCounters_Type.__name__ = "Integer32"
_BrzaccVLResetPerModulationLevelCounters_Object = MibScalar
brzaccVLResetPerModulationLevelCounters = _BrzaccVLResetPerModulationLevelCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 1),
    _BrzaccVLResetPerModulationLevelCounters_Type()
)
brzaccVLResetPerModulationLevelCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLResetPerModulationLevelCounters.setStatus("current")
_BrzaccVLSUPerModulationLevelCountersTable_Object = MibTable
brzaccVLSUPerModulationLevelCountersTable = _BrzaccVLSUPerModulationLevelCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2)
)
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersTable.setStatus("current")
_BrzaccVLSUPerModulationLevelCountersEntry_Object = MibTableRow
brzaccVLSUPerModulationLevelCountersEntry = _BrzaccVLSUPerModulationLevelCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1)
)
brzaccVLSUPerModulationLevelCountersEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLSUPerModulationLevelCountersTableIdx"),
)
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersEntry.setStatus("current")


class _BrzaccVLSUPerModulationLevelCountersTableIdx_Type(Integer32):
    """Custom type brzaccVLSUPerModulationLevelCountersTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BrzaccVLSUPerModulationLevelCountersTableIdx_Type.__name__ = "Integer32"
_BrzaccVLSUPerModulationLevelCountersTableIdx_Object = MibTableColumn
brzaccVLSUPerModulationLevelCountersTableIdx = _BrzaccVLSUPerModulationLevelCountersTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 1),
    _BrzaccVLSUPerModulationLevelCountersTableIdx_Type()
)
brzaccVLSUPerModulationLevelCountersTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersTableIdx.setStatus("current")


class _BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type(Integer32):
    """Custom type brzaccVLSUPerModulationLevelCountersApplicableModLevel based on Integer32"""
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
        *(("modLevel-1", 1),
          ("modLevel-2", 2),
          ("modLevel-3", 3),
          ("modLevel-4", 4),
          ("modLevel-5", 5),
          ("modLevel-6", 6),
          ("modLevel-7", 7),
          ("modLevel-8", 8))
    )


_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type.__name__ = "Integer32"
_BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Object = MibTableColumn
brzaccVLSUPerModulationLevelCountersApplicableModLevel = _BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 2),
    _BrzaccVLSUPerModulationLevelCountersApplicableModLevel_Type()
)
brzaccVLSUPerModulationLevelCountersApplicableModLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersApplicableModLevel.setStatus("current")
_BrzaccVLSUPerModulationLevelCountersTxSuccess_Type = Counter32
_BrzaccVLSUPerModulationLevelCountersTxSuccess_Object = MibTableColumn
brzaccVLSUPerModulationLevelCountersTxSuccess = _BrzaccVLSUPerModulationLevelCountersTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 3),
    _BrzaccVLSUPerModulationLevelCountersTxSuccess_Type()
)
brzaccVLSUPerModulationLevelCountersTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersTxSuccess.setStatus("current")
_BrzaccVLSUPerModulationLevelCountersTxFailed_Type = Counter32
_BrzaccVLSUPerModulationLevelCountersTxFailed_Object = MibTableColumn
brzaccVLSUPerModulationLevelCountersTxFailed = _BrzaccVLSUPerModulationLevelCountersTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 4),
    _BrzaccVLSUPerModulationLevelCountersTxFailed_Type()
)
brzaccVLSUPerModulationLevelCountersTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLSUPerModulationLevelCountersTxFailed.setStatus("current")
_BrzaccVLAverageModulationLevel_Type = Integer32
_BrzaccVLAverageModulationLevel_Object = MibScalar
brzaccVLAverageModulationLevel = _BrzaccVLAverageModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 3),
    _BrzaccVLAverageModulationLevel_Type()
)
brzaccVLAverageModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAverageModulationLevel.setStatus("current")
_BrzaccVLMacAddressDatabase_ObjectIdentity = ObjectIdentity
brzaccVLMacAddressDatabase = _BrzaccVLMacAddressDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5)
)
_BrzaccVLAUMacAddressDatabase_ObjectIdentity = ObjectIdentity
brzaccVLAUMacAddressDatabase = _BrzaccVLAUMacAddressDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1)
)


class _BrzaccVLAUAdbResetAllModulationLevelCounters_Type(Integer32):
    """Custom type brzaccVLAUAdbResetAllModulationLevelCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("reset", 1))
    )


_BrzaccVLAUAdbResetAllModulationLevelCounters_Type.__name__ = "Integer32"
_BrzaccVLAUAdbResetAllModulationLevelCounters_Object = MibScalar
brzaccVLAUAdbResetAllModulationLevelCounters = _BrzaccVLAUAdbResetAllModulationLevelCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 1),
    _BrzaccVLAUAdbResetAllModulationLevelCounters_Type()
)
brzaccVLAUAdbResetAllModulationLevelCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLAUAdbResetAllModulationLevelCounters.setStatus("current")
_BrzaccVLAUAdbTable_Object = MibTable
brzaccVLAUAdbTable = _BrzaccVLAUAdbTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2)
)
if mibBuilder.loadTexts:
    brzaccVLAUAdbTable.setStatus("current")
_BrzaccVLAUAdbEntry_Object = MibTableRow
brzaccVLAUAdbEntry = _BrzaccVLAUAdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1)
)
brzaccVLAUAdbEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLAdbIndex"),
)
if mibBuilder.loadTexts:
    brzaccVLAUAdbEntry.setStatus("current")


class _BrzaccVLAdbIndex_Type(Integer32):
    """Custom type brzaccVLAdbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BrzaccVLAdbIndex_Type.__name__ = "Integer32"
_BrzaccVLAdbIndex_Object = MibTableColumn
brzaccVLAdbIndex = _BrzaccVLAdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 1),
    _BrzaccVLAdbIndex_Type()
)
brzaccVLAdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbIndex.setStatus("current")
_BrzaccVLAdbMacAddress_Type = MacAddress
_BrzaccVLAdbMacAddress_Object = MibTableColumn
brzaccVLAdbMacAddress = _BrzaccVLAdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 2),
    _BrzaccVLAdbMacAddress_Type()
)
brzaccVLAdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbMacAddress.setStatus("current")


class _BrzaccVLAdbStatus_Type(Integer32):
    """Custom type brzaccVLAdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("authenticated", 2),
          ("notAuthenticated", 3))
    )


_BrzaccVLAdbStatus_Type.__name__ = "Integer32"
_BrzaccVLAdbStatus_Object = MibTableColumn
brzaccVLAdbStatus = _BrzaccVLAdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 3),
    _BrzaccVLAdbStatus_Type()
)
brzaccVLAdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbStatus.setStatus("current")
_BrzaccVLAdbSwVersion_Type = DisplayString
_BrzaccVLAdbSwVersion_Object = MibTableColumn
brzaccVLAdbSwVersion = _BrzaccVLAdbSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 4),
    _BrzaccVLAdbSwVersion_Type()
)
brzaccVLAdbSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbSwVersion.setStatus("current")
_BrzaccVLAdbSNR_Type = Integer32
_BrzaccVLAdbSNR_Object = MibTableColumn
brzaccVLAdbSNR = _BrzaccVLAdbSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 5),
    _BrzaccVLAdbSNR_Type()
)
brzaccVLAdbSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbSNR.setStatus("current")


class _BrzaccVLAdbMaxModulationLevel_Type(Integer32):
    """Custom type brzaccVLAdbMaxModulationLevel based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modLevel-1", 1),
          ("modLevel-2", 2),
          ("modLevel-3", 3),
          ("modLevel-4", 4),
          ("modLevel-5", 5),
          ("modLevel-6", 6),
          ("modLevel-7", 7),
          ("modLevel-8", 8),
          ("na", 255))
    )


_BrzaccVLAdbMaxModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLAdbMaxModulationLevel_Object = MibTableColumn
brzaccVLAdbMaxModulationLevel = _BrzaccVLAdbMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 6),
    _BrzaccVLAdbMaxModulationLevel_Type()
)
brzaccVLAdbMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbMaxModulationLevel.setStatus("current")
_BrzaccVLAdbTxFramesTotal_Type = Counter32
_BrzaccVLAdbTxFramesTotal_Object = MibTableColumn
brzaccVLAdbTxFramesTotal = _BrzaccVLAdbTxFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 7),
    _BrzaccVLAdbTxFramesTotal_Type()
)
brzaccVLAdbTxFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFramesTotal.setStatus("current")
_BrzaccVLAdbDroppedFramesTotal_Type = Counter32
_BrzaccVLAdbDroppedFramesTotal_Object = MibTableColumn
brzaccVLAdbDroppedFramesTotal = _BrzaccVLAdbDroppedFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 8),
    _BrzaccVLAdbDroppedFramesTotal_Type()
)
brzaccVLAdbDroppedFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbDroppedFramesTotal.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel1_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel1_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel1 = _BrzaccVLAdbTxSuccessModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 9),
    _BrzaccVLAdbTxSuccessModLevel1_Type()
)
brzaccVLAdbTxSuccessModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel1.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel2_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel2_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel2 = _BrzaccVLAdbTxSuccessModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 10),
    _BrzaccVLAdbTxSuccessModLevel2_Type()
)
brzaccVLAdbTxSuccessModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel2.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel3_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel3_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel3 = _BrzaccVLAdbTxSuccessModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 11),
    _BrzaccVLAdbTxSuccessModLevel3_Type()
)
brzaccVLAdbTxSuccessModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel3.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel4_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel4_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel4 = _BrzaccVLAdbTxSuccessModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 12),
    _BrzaccVLAdbTxSuccessModLevel4_Type()
)
brzaccVLAdbTxSuccessModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel4.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel5_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel5_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel5 = _BrzaccVLAdbTxSuccessModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 13),
    _BrzaccVLAdbTxSuccessModLevel5_Type()
)
brzaccVLAdbTxSuccessModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel5.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel6_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel6_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel6 = _BrzaccVLAdbTxSuccessModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 14),
    _BrzaccVLAdbTxSuccessModLevel6_Type()
)
brzaccVLAdbTxSuccessModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel6.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel7_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel7_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel7 = _BrzaccVLAdbTxSuccessModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 15),
    _BrzaccVLAdbTxSuccessModLevel7_Type()
)
brzaccVLAdbTxSuccessModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel7.setStatus("current")
_BrzaccVLAdbTxSuccessModLevel8_Type = Counter32
_BrzaccVLAdbTxSuccessModLevel8_Object = MibTableColumn
brzaccVLAdbTxSuccessModLevel8 = _BrzaccVLAdbTxSuccessModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 16),
    _BrzaccVLAdbTxSuccessModLevel8_Type()
)
brzaccVLAdbTxSuccessModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxSuccessModLevel8.setStatus("current")
_BrzaccVLAdbTxFailedModLevel1_Type = Counter32
_BrzaccVLAdbTxFailedModLevel1_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel1 = _BrzaccVLAdbTxFailedModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 17),
    _BrzaccVLAdbTxFailedModLevel1_Type()
)
brzaccVLAdbTxFailedModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel1.setStatus("current")
_BrzaccVLAdbTxFailedModLevel2_Type = Counter32
_BrzaccVLAdbTxFailedModLevel2_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel2 = _BrzaccVLAdbTxFailedModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 18),
    _BrzaccVLAdbTxFailedModLevel2_Type()
)
brzaccVLAdbTxFailedModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel2.setStatus("current")
_BrzaccVLAdbTxFailedModLevel3_Type = Counter32
_BrzaccVLAdbTxFailedModLevel3_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel3 = _BrzaccVLAdbTxFailedModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 19),
    _BrzaccVLAdbTxFailedModLevel3_Type()
)
brzaccVLAdbTxFailedModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel3.setStatus("current")
_BrzaccVLAdbTxFailedModLevel4_Type = Counter32
_BrzaccVLAdbTxFailedModLevel4_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel4 = _BrzaccVLAdbTxFailedModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 20),
    _BrzaccVLAdbTxFailedModLevel4_Type()
)
brzaccVLAdbTxFailedModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel4.setStatus("current")
_BrzaccVLAdbTxFailedModLevel5_Type = Counter32
_BrzaccVLAdbTxFailedModLevel5_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel5 = _BrzaccVLAdbTxFailedModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 21),
    _BrzaccVLAdbTxFailedModLevel5_Type()
)
brzaccVLAdbTxFailedModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel5.setStatus("current")
_BrzaccVLAdbTxFailedModLevel6_Type = Counter32
_BrzaccVLAdbTxFailedModLevel6_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel6 = _BrzaccVLAdbTxFailedModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 22),
    _BrzaccVLAdbTxFailedModLevel6_Type()
)
brzaccVLAdbTxFailedModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel6.setStatus("current")
_BrzaccVLAdbTxFailedModLevel7_Type = Counter32
_BrzaccVLAdbTxFailedModLevel7_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel7 = _BrzaccVLAdbTxFailedModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 23),
    _BrzaccVLAdbTxFailedModLevel7_Type()
)
brzaccVLAdbTxFailedModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel7.setStatus("current")
_BrzaccVLAdbTxFailedModLevel8_Type = Counter32
_BrzaccVLAdbTxFailedModLevel8_Object = MibTableColumn
brzaccVLAdbTxFailedModLevel8 = _BrzaccVLAdbTxFailedModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 24),
    _BrzaccVLAdbTxFailedModLevel8_Type()
)
brzaccVLAdbTxFailedModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbTxFailedModLevel8.setStatus("current")
_BrzaccVLAdbCirTx_Type = Integer32
_BrzaccVLAdbCirTx_Object = MibTableColumn
brzaccVLAdbCirTx = _BrzaccVLAdbCirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 25),
    _BrzaccVLAdbCirTx_Type()
)
brzaccVLAdbCirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbCirTx.setStatus("current")
_BrzaccVLAdbMirTx_Type = Integer32
_BrzaccVLAdbMirTx_Object = MibTableColumn
brzaccVLAdbMirTx = _BrzaccVLAdbMirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 26),
    _BrzaccVLAdbMirTx_Type()
)
brzaccVLAdbMirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbMirTx.setStatus("current")
_BrzaccVLAdbCirRx_Type = Integer32
_BrzaccVLAdbCirRx_Object = MibTableColumn
brzaccVLAdbCirRx = _BrzaccVLAdbCirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 27),
    _BrzaccVLAdbCirRx_Type()
)
brzaccVLAdbCirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbCirRx.setStatus("current")
_BrzaccVLAdbMirRx_Type = Integer32
_BrzaccVLAdbMirRx_Object = MibTableColumn
brzaccVLAdbMirRx = _BrzaccVLAdbMirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 28),
    _BrzaccVLAdbMirRx_Type()
)
brzaccVLAdbMirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbMirRx.setStatus("current")
_BrzaccVLAdbCirMaxDelay_Type = Integer32
_BrzaccVLAdbCirMaxDelay_Object = MibTableColumn
brzaccVLAdbCirMaxDelay = _BrzaccVLAdbCirMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 29),
    _BrzaccVLAdbCirMaxDelay_Type()
)
brzaccVLAdbCirMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbCirMaxDelay.setStatus("current")


class _BrzaccVLAdbDistance_Type(Integer32):
    """Custom type brzaccVLAdbDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("below-2-Km", 1)
    )


_BrzaccVLAdbDistance_Type.__name__ = "Integer32"
_BrzaccVLAdbDistance_Object = MibTableColumn
brzaccVLAdbDistance = _BrzaccVLAdbDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 30),
    _BrzaccVLAdbDistance_Type()
)
brzaccVLAdbDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbDistance.setStatus("current")


class _BrzaccVLAdbHwRevision_Type(Integer32):
    """Custom type brzaccVLAdbHwRevision based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("hwRevisionF", 6),
          ("hwRevisionG", 7),
          ("na", 255))
    )


_BrzaccVLAdbHwRevision_Type.__name__ = "Integer32"
_BrzaccVLAdbHwRevision_Object = MibTableColumn
brzaccVLAdbHwRevision = _BrzaccVLAdbHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 31),
    _BrzaccVLAdbHwRevision_Type()
)
brzaccVLAdbHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbHwRevision.setStatus("current")
_BrzaccVLAdbCpldVer_Type = DisplayString
_BrzaccVLAdbCpldVer_Object = MibTableColumn
brzaccVLAdbCpldVer = _BrzaccVLAdbCpldVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 32),
    _BrzaccVLAdbCpldVer_Type()
)
brzaccVLAdbCpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbCpldVer.setStatus("current")
_BrzaccVLAdbCountryCode_Type = Integer32
_BrzaccVLAdbCountryCode_Object = MibTableColumn
brzaccVLAdbCountryCode = _BrzaccVLAdbCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 33),
    _BrzaccVLAdbCountryCode_Type()
)
brzaccVLAdbCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbCountryCode.setStatus("current")
_BrzaccVLAdbBootVer_Type = DisplayString
_BrzaccVLAdbBootVer_Object = MibTableColumn
brzaccVLAdbBootVer = _BrzaccVLAdbBootVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 34),
    _BrzaccVLAdbBootVer_Type()
)
brzaccVLAdbBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbBootVer.setStatus("current")


class _BrzaccVLAdbAtpcOption_Type(Integer32):
    """Custom type brzaccVLAdbAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdbAtpcOption_Type.__name__ = "Integer32"
_BrzaccVLAdbAtpcOption_Object = MibTableColumn
brzaccVLAdbAtpcOption = _BrzaccVLAdbAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 35),
    _BrzaccVLAdbAtpcOption_Type()
)
brzaccVLAdbAtpcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbAtpcOption.setStatus("current")


class _BrzaccVLAdbAdapModOption_Type(Integer32):
    """Custom type brzaccVLAdbAdapModOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdbAdapModOption_Type.__name__ = "Integer32"
_BrzaccVLAdbAdapModOption_Object = MibTableColumn
brzaccVLAdbAdapModOption = _BrzaccVLAdbAdapModOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 36),
    _BrzaccVLAdbAdapModOption_Type()
)
brzaccVLAdbAdapModOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbAdapModOption.setStatus("current")


class _BrzaccVLAdbBurstModeOption_Type(Integer32):
    """Custom type brzaccVLAdbBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdbBurstModeOption_Type.__name__ = "Integer32"
_BrzaccVLAdbBurstModeOption_Object = MibTableColumn
brzaccVLAdbBurstModeOption = _BrzaccVLAdbBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 37),
    _BrzaccVLAdbBurstModeOption_Type()
)
brzaccVLAdbBurstModeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbBurstModeOption.setStatus("current")


class _BrzaccVLAdbConcatenationOption_Type(Integer32):
    """Custom type brzaccVLAdbConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdbConcatenationOption_Type.__name__ = "Integer32"
_BrzaccVLAdbConcatenationOption_Object = MibTableColumn
brzaccVLAdbConcatenationOption = _BrzaccVLAdbConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 39),
    _BrzaccVLAdbConcatenationOption_Type()
)
brzaccVLAdbConcatenationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbConcatenationOption.setStatus("current")


class _BrzaccVLAdbSecurityMode_Type(Integer32):
    """Custom type brzaccVLAdbSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("fips197", 3),
          ("na", 255),
          ("wep", 1))
    )


_BrzaccVLAdbSecurityMode_Type.__name__ = "Integer32"
_BrzaccVLAdbSecurityMode_Object = MibTableColumn
brzaccVLAdbSecurityMode = _BrzaccVLAdbSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 41),
    _BrzaccVLAdbSecurityMode_Type()
)
brzaccVLAdbSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbSecurityMode.setStatus("current")


class _BrzaccVLAdbAuthOption_Type(Integer32):
    """Custom type brzaccVLAdbAuthOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("openSystem", 1),
          ("sharedKey", 2))
    )


_BrzaccVLAdbAuthOption_Type.__name__ = "Integer32"
_BrzaccVLAdbAuthOption_Object = MibTableColumn
brzaccVLAdbAuthOption = _BrzaccVLAdbAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 42),
    _BrzaccVLAdbAuthOption_Type()
)
brzaccVLAdbAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbAuthOption.setStatus("current")


class _BrzaccVLAdbDataEncyptOption_Type(Integer32):
    """Custom type brzaccVLAdbDataEncyptOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLAdbDataEncyptOption_Type.__name__ = "Integer32"
_BrzaccVLAdbDataEncyptOption_Object = MibTableColumn
brzaccVLAdbDataEncyptOption = _BrzaccVLAdbDataEncyptOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 43),
    _BrzaccVLAdbDataEncyptOption_Type()
)
brzaccVLAdbDataEncyptOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbDataEncyptOption.setStatus("current")
_BrzaccVLAdbAge_Type = Integer32
_BrzaccVLAdbAge_Object = MibTableColumn
brzaccVLAdbAge = _BrzaccVLAdbAge_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 44),
    _BrzaccVLAdbAge_Type()
)
brzaccVLAdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbAge.setStatus("current")
_BrzaccVLAdbUnitName_Type = DisplayString
_BrzaccVLAdbUnitName_Object = MibTableColumn
brzaccVLAdbUnitName = _BrzaccVLAdbUnitName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 45),
    _BrzaccVLAdbUnitName_Type()
)
brzaccVLAdbUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbUnitName.setStatus("current")
_BrzaccVLAdbRSSI_Type = Integer32
_BrzaccVLAdbRSSI_Object = MibTableColumn
brzaccVLAdbRSSI = _BrzaccVLAdbRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 46),
    _BrzaccVLAdbRSSI_Type()
)
brzaccVLAdbRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbRSSI.setStatus("current")
_BrzaccVLAdbIpAddress_Type = IpAddress
_BrzaccVLAdbIpAddress_Object = MibTableColumn
brzaccVLAdbIpAddress = _BrzaccVLAdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 47),
    _BrzaccVLAdbIpAddress_Type()
)
brzaccVLAdbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbIpAddress.setStatus("current")
_BrzaccVLAUNewAdbTable_Object = MibTable
brzaccVLAUNewAdbTable = _BrzaccVLAUNewAdbTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3)
)
if mibBuilder.loadTexts:
    brzaccVLAUNewAdbTable.setStatus("current")
_BrzaccVLAUNewAdbEntry_Object = MibTableRow
brzaccVLAUNewAdbEntry = _BrzaccVLAUNewAdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1)
)
brzaccVLAUNewAdbEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLNewAdbMacAddress"),
)
if mibBuilder.loadTexts:
    brzaccVLAUNewAdbEntry.setStatus("current")
_BrzaccVLNewAdbMacAddress_Type = MacAddress
_BrzaccVLNewAdbMacAddress_Object = MibTableColumn
brzaccVLNewAdbMacAddress = _BrzaccVLNewAdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 1),
    _BrzaccVLNewAdbMacAddress_Type()
)
brzaccVLNewAdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMacAddress.setStatus("current")
_BrzaccVLNewAdbIPaddress_Type = IpAddress
_BrzaccVLNewAdbIPaddress_Object = MibTableColumn
brzaccVLNewAdbIPaddress = _BrzaccVLNewAdbIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 2),
    _BrzaccVLNewAdbIPaddress_Type()
)
brzaccVLNewAdbIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbIPaddress.setStatus("current")
_BrzaccVLNewAdbUnitName_Type = DisplayString
_BrzaccVLNewAdbUnitName_Object = MibTableColumn
brzaccVLNewAdbUnitName = _BrzaccVLNewAdbUnitName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 3),
    _BrzaccVLNewAdbUnitName_Type()
)
brzaccVLNewAdbUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbUnitName.setStatus("current")


class _BrzaccVLNewAdbUnitType_Type(Integer32):
    """Custom type brzaccVLNewAdbUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              8,
              9,
              10,
              11,
              12,
              13,
              18,
              20,
              21,
              23,
              24,
              26,
              27,
              28,
              29,
              30,
              31,
              33,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("rb-B10", 26),
          ("rb-B100", 20),
          ("rb-B14", 8),
          ("rb-B28", 9),
          ("su", 33),
          ("su-1-BD", 28),
          ("su-12-L", 31),
          ("su-24-BD", 5),
          ("su-3-1D", 12),
          ("su-3-4D", 13),
          ("su-3-L", 29),
          ("su-54-BD", 11),
          ("su-6-1D", 3),
          ("su-6-BD", 4),
          ("su-6-L", 30),
          ("su-8-BD", 27),
          ("su-BD", 10),
          ("su-EZ", 23),
          ("su-I", 21),
          ("su-V", 24),
          ("su4900", 18))
    )


_BrzaccVLNewAdbUnitType_Type.__name__ = "Integer32"
_BrzaccVLNewAdbUnitType_Object = MibTableColumn
brzaccVLNewAdbUnitType = _BrzaccVLNewAdbUnitType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 4),
    _BrzaccVLNewAdbUnitType_Type()
)
brzaccVLNewAdbUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbUnitType.setStatus("current")
_BrzaccVLNewAdbSwVersion_Type = DisplayString
_BrzaccVLNewAdbSwVersion_Object = MibTableColumn
brzaccVLNewAdbSwVersion = _BrzaccVLNewAdbSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 5),
    _BrzaccVLNewAdbSwVersion_Type()
)
brzaccVLNewAdbSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbSwVersion.setStatus("current")


class _BrzaccVLNewAdbHwRevision_Type(Integer32):
    """Custom type brzaccVLNewAdbHwRevision based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("hwRevisionF", 6),
          ("hwRevisionG", 7),
          ("na", 255))
    )


_BrzaccVLNewAdbHwRevision_Type.__name__ = "Integer32"
_BrzaccVLNewAdbHwRevision_Object = MibTableColumn
brzaccVLNewAdbHwRevision = _BrzaccVLNewAdbHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 6),
    _BrzaccVLNewAdbHwRevision_Type()
)
brzaccVLNewAdbHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbHwRevision.setStatus("current")
_BrzaccVLNewAdbCpldVer_Type = DisplayString
_BrzaccVLNewAdbCpldVer_Object = MibTableColumn
brzaccVLNewAdbCpldVer = _BrzaccVLNewAdbCpldVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 7),
    _BrzaccVLNewAdbCpldVer_Type()
)
brzaccVLNewAdbCpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbCpldVer.setStatus("current")
_BrzaccVLNewAdbBootVer_Type = DisplayString
_BrzaccVLNewAdbBootVer_Object = MibTableColumn
brzaccVLNewAdbBootVer = _BrzaccVLNewAdbBootVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 8),
    _BrzaccVLNewAdbBootVer_Type()
)
brzaccVLNewAdbBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbBootVer.setStatus("current")
_BrzaccVLNewAdbCountryCode_Type = Integer32
_BrzaccVLNewAdbCountryCode_Object = MibTableColumn
brzaccVLNewAdbCountryCode = _BrzaccVLNewAdbCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 9),
    _BrzaccVLNewAdbCountryCode_Type()
)
brzaccVLNewAdbCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbCountryCode.setStatus("current")
_BrzaccVLNewAdbCirTx_Type = Integer32
_BrzaccVLNewAdbCirTx_Object = MibTableColumn
brzaccVLNewAdbCirTx = _BrzaccVLNewAdbCirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 10),
    _BrzaccVLNewAdbCirTx_Type()
)
brzaccVLNewAdbCirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbCirTx.setStatus("current")
_BrzaccVLNewAdbMirTx_Type = Integer32
_BrzaccVLNewAdbMirTx_Object = MibTableColumn
brzaccVLNewAdbMirTx = _BrzaccVLNewAdbMirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 11),
    _BrzaccVLNewAdbMirTx_Type()
)
brzaccVLNewAdbMirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMirTx.setStatus("current")
_BrzaccVLNewAdbCirRx_Type = Integer32
_BrzaccVLNewAdbCirRx_Object = MibTableColumn
brzaccVLNewAdbCirRx = _BrzaccVLNewAdbCirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 12),
    _BrzaccVLNewAdbCirRx_Type()
)
brzaccVLNewAdbCirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbCirRx.setStatus("current")
_BrzaccVLNewAdbMirRx_Type = Integer32
_BrzaccVLNewAdbMirRx_Object = MibTableColumn
brzaccVLNewAdbMirRx = _BrzaccVLNewAdbMirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 13),
    _BrzaccVLNewAdbMirRx_Type()
)
brzaccVLNewAdbMirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMirRx.setStatus("current")
_BrzaccVLNewAdbCirMaxDelay_Type = Integer32
_BrzaccVLNewAdbCirMaxDelay_Object = MibTableColumn
brzaccVLNewAdbCirMaxDelay = _BrzaccVLNewAdbCirMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 14),
    _BrzaccVLNewAdbCirMaxDelay_Type()
)
brzaccVLNewAdbCirMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbCirMaxDelay.setStatus("current")


class _BrzaccVLNewAdbAtpcOption_Type(Integer32):
    """Custom type brzaccVLNewAdbAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNewAdbAtpcOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbAtpcOption_Object = MibTableColumn
brzaccVLNewAdbAtpcOption = _BrzaccVLNewAdbAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 15),
    _BrzaccVLNewAdbAtpcOption_Type()
)
brzaccVLNewAdbAtpcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbAtpcOption.setStatus("current")


class _BrzaccVLNewAdbAdapModOption_Type(Integer32):
    """Custom type brzaccVLNewAdbAdapModOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNewAdbAdapModOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbAdapModOption_Object = MibTableColumn
brzaccVLNewAdbAdapModOption = _BrzaccVLNewAdbAdapModOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 16),
    _BrzaccVLNewAdbAdapModOption_Type()
)
brzaccVLNewAdbAdapModOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbAdapModOption.setStatus("current")


class _BrzaccVLNewAdbBurstModeOption_Type(Integer32):
    """Custom type brzaccVLNewAdbBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNewAdbBurstModeOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbBurstModeOption_Object = MibTableColumn
brzaccVLNewAdbBurstModeOption = _BrzaccVLNewAdbBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 17),
    _BrzaccVLNewAdbBurstModeOption_Type()
)
brzaccVLNewAdbBurstModeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbBurstModeOption.setStatus("current")


class _BrzaccVLNewAdbConcatenationOption_Type(Integer32):
    """Custom type brzaccVLNewAdbConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNewAdbConcatenationOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbConcatenationOption_Object = MibTableColumn
brzaccVLNewAdbConcatenationOption = _BrzaccVLNewAdbConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 18),
    _BrzaccVLNewAdbConcatenationOption_Type()
)
brzaccVLNewAdbConcatenationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbConcatenationOption.setStatus("current")


class _BrzaccVLNewAdbSecurityMode_Type(Integer32):
    """Custom type brzaccVLNewAdbSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("fips197", 3),
          ("na", 255),
          ("wep", 1))
    )


_BrzaccVLNewAdbSecurityMode_Type.__name__ = "Integer32"
_BrzaccVLNewAdbSecurityMode_Object = MibTableColumn
brzaccVLNewAdbSecurityMode = _BrzaccVLNewAdbSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 19),
    _BrzaccVLNewAdbSecurityMode_Type()
)
brzaccVLNewAdbSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbSecurityMode.setStatus("current")


class _BrzaccVLNewAdbAuthOption_Type(Integer32):
    """Custom type brzaccVLNewAdbAuthOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("openSystem", 1),
          ("sharedKey", 2))
    )


_BrzaccVLNewAdbAuthOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbAuthOption_Object = MibTableColumn
brzaccVLNewAdbAuthOption = _BrzaccVLNewAdbAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 20),
    _BrzaccVLNewAdbAuthOption_Type()
)
brzaccVLNewAdbAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbAuthOption.setStatus("current")


class _BrzaccVLNewAdbDataEncyptOption_Type(Integer32):
    """Custom type brzaccVLNewAdbDataEncyptOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BrzaccVLNewAdbDataEncyptOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbDataEncyptOption_Object = MibTableColumn
brzaccVLNewAdbDataEncyptOption = _BrzaccVLNewAdbDataEncyptOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 21),
    _BrzaccVLNewAdbDataEncyptOption_Type()
)
brzaccVLNewAdbDataEncyptOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbDataEncyptOption.setStatus("current")
_BrzaccVLAdbWi2IPaddress_Type = IpAddress
_BrzaccVLAdbWi2IPaddress_Object = MibTableColumn
brzaccVLAdbWi2IPaddress = _BrzaccVLAdbWi2IPaddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 22),
    _BrzaccVLAdbWi2IPaddress_Type()
)
brzaccVLAdbWi2IPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAdbWi2IPaddress.setStatus("current")


class _BrzaccVLNewAdbStatus_Type(Integer32):
    """Custom type brzaccVLNewAdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("authenticated", 2),
          ("notAuthenticated", 3))
    )


_BrzaccVLNewAdbStatus_Type.__name__ = "Integer32"
_BrzaccVLNewAdbStatus_Object = MibTableColumn
brzaccVLNewAdbStatus = _BrzaccVLNewAdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 23),
    _BrzaccVLNewAdbStatus_Type()
)
brzaccVLNewAdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbStatus.setStatus("current")
_BrzaccVLNewAdbAge_Type = Integer32
_BrzaccVLNewAdbAge_Object = MibTableColumn
brzaccVLNewAdbAge = _BrzaccVLNewAdbAge_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 24),
    _BrzaccVLNewAdbAge_Type()
)
brzaccVLNewAdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbAge.setStatus("current")


class _BrzaccVLNewAdbDistance_Type(Integer32):
    """Custom type brzaccVLNewAdbDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("below-2-Km", 1)
    )


_BrzaccVLNewAdbDistance_Type.__name__ = "Integer32"
_BrzaccVLNewAdbDistance_Object = MibTableColumn
brzaccVLNewAdbDistance = _BrzaccVLNewAdbDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 25),
    _BrzaccVLNewAdbDistance_Type()
)
brzaccVLNewAdbDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbDistance.setStatus("current")
_BrzaccVLNewAdbSNR_Type = Integer32
_BrzaccVLNewAdbSNR_Object = MibTableColumn
brzaccVLNewAdbSNR = _BrzaccVLNewAdbSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 26),
    _BrzaccVLNewAdbSNR_Type()
)
brzaccVLNewAdbSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbSNR.setStatus("current")


class _BrzaccVLNewAdbMaxModulationLevel_Type(Integer32):
    """Custom type brzaccVLNewAdbMaxModulationLevel based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modLevel-1", 1),
          ("modLevel-2", 2),
          ("modLevel-3", 3),
          ("modLevel-4", 4),
          ("modLevel-5", 5),
          ("modLevel-6", 6),
          ("modLevel-7", 7),
          ("modLevel-8", 8),
          ("na", 255))
    )


_BrzaccVLNewAdbMaxModulationLevel_Type.__name__ = "Integer32"
_BrzaccVLNewAdbMaxModulationLevel_Object = MibTableColumn
brzaccVLNewAdbMaxModulationLevel = _BrzaccVLNewAdbMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 27),
    _BrzaccVLNewAdbMaxModulationLevel_Type()
)
brzaccVLNewAdbMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMaxModulationLevel.setStatus("current")
_BrzaccVLNewAdbTxFramesTotal_Type = Counter32
_BrzaccVLNewAdbTxFramesTotal_Object = MibTableColumn
brzaccVLNewAdbTxFramesTotal = _BrzaccVLNewAdbTxFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 28),
    _BrzaccVLNewAdbTxFramesTotal_Type()
)
brzaccVLNewAdbTxFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFramesTotal.setStatus("current")
_BrzaccVLNewAdbDroppedFramesTotal_Type = Counter32
_BrzaccVLNewAdbDroppedFramesTotal_Object = MibTableColumn
brzaccVLNewAdbDroppedFramesTotal = _BrzaccVLNewAdbDroppedFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 29),
    _BrzaccVLNewAdbDroppedFramesTotal_Type()
)
brzaccVLNewAdbDroppedFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbDroppedFramesTotal.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel1_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel1_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel1 = _BrzaccVLNewAdbTxSuccessModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 30),
    _BrzaccVLNewAdbTxSuccessModLevel1_Type()
)
brzaccVLNewAdbTxSuccessModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel1.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel2_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel2_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel2 = _BrzaccVLNewAdbTxSuccessModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 31),
    _BrzaccVLNewAdbTxSuccessModLevel2_Type()
)
brzaccVLNewAdbTxSuccessModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel2.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel3_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel3_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel3 = _BrzaccVLNewAdbTxSuccessModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 32),
    _BrzaccVLNewAdbTxSuccessModLevel3_Type()
)
brzaccVLNewAdbTxSuccessModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel3.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel4_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel4_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel4 = _BrzaccVLNewAdbTxSuccessModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 33),
    _BrzaccVLNewAdbTxSuccessModLevel4_Type()
)
brzaccVLNewAdbTxSuccessModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel4.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel5_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel5_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel5 = _BrzaccVLNewAdbTxSuccessModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 34),
    _BrzaccVLNewAdbTxSuccessModLevel5_Type()
)
brzaccVLNewAdbTxSuccessModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel5.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel6_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel6_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel6 = _BrzaccVLNewAdbTxSuccessModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 35),
    _BrzaccVLNewAdbTxSuccessModLevel6_Type()
)
brzaccVLNewAdbTxSuccessModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel6.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel7_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel7_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel7 = _BrzaccVLNewAdbTxSuccessModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 36),
    _BrzaccVLNewAdbTxSuccessModLevel7_Type()
)
brzaccVLNewAdbTxSuccessModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel7.setStatus("current")
_BrzaccVLNewAdbTxSuccessModLevel8_Type = Counter32
_BrzaccVLNewAdbTxSuccessModLevel8_Object = MibTableColumn
brzaccVLNewAdbTxSuccessModLevel8 = _BrzaccVLNewAdbTxSuccessModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 37),
    _BrzaccVLNewAdbTxSuccessModLevel8_Type()
)
brzaccVLNewAdbTxSuccessModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxSuccessModLevel8.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel1_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel1_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel1 = _BrzaccVLNewAdbTxFailedModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 38),
    _BrzaccVLNewAdbTxFailedModLevel1_Type()
)
brzaccVLNewAdbTxFailedModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel1.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel2_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel2_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel2 = _BrzaccVLNewAdbTxFailedModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 39),
    _BrzaccVLNewAdbTxFailedModLevel2_Type()
)
brzaccVLNewAdbTxFailedModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel2.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel3_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel3_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel3 = _BrzaccVLNewAdbTxFailedModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 40),
    _BrzaccVLNewAdbTxFailedModLevel3_Type()
)
brzaccVLNewAdbTxFailedModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel3.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel4_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel4_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel4 = _BrzaccVLNewAdbTxFailedModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 41),
    _BrzaccVLNewAdbTxFailedModLevel4_Type()
)
brzaccVLNewAdbTxFailedModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel4.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel5_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel5_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel5 = _BrzaccVLNewAdbTxFailedModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 42),
    _BrzaccVLNewAdbTxFailedModLevel5_Type()
)
brzaccVLNewAdbTxFailedModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel5.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel6_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel6_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel6 = _BrzaccVLNewAdbTxFailedModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 43),
    _BrzaccVLNewAdbTxFailedModLevel6_Type()
)
brzaccVLNewAdbTxFailedModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel6.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel7_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel7_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel7 = _BrzaccVLNewAdbTxFailedModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 44),
    _BrzaccVLNewAdbTxFailedModLevel7_Type()
)
brzaccVLNewAdbTxFailedModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel7.setStatus("current")
_BrzaccVLNewAdbTxFailedModLevel8_Type = Counter32
_BrzaccVLNewAdbTxFailedModLevel8_Object = MibTableColumn
brzaccVLNewAdbTxFailedModLevel8 = _BrzaccVLNewAdbTxFailedModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 45),
    _BrzaccVLNewAdbTxFailedModLevel8_Type()
)
brzaccVLNewAdbTxFailedModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbTxFailedModLevel8.setStatus("current")


class _BrzaccVLNewAdbMainSwVersion_Type(DisplayString):
    """Custom type brzaccVLNewAdbMainSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_BrzaccVLNewAdbMainSwVersion_Type.__name__ = "DisplayString"
_BrzaccVLNewAdbMainSwVersion_Object = MibTableColumn
brzaccVLNewAdbMainSwVersion = _BrzaccVLNewAdbMainSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 46),
    _BrzaccVLNewAdbMainSwVersion_Type()
)
brzaccVLNewAdbMainSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMainSwVersion.setStatus("current")


class _BrzaccVLNewAdbShadowSwVersion_Type(DisplayString):
    """Custom type brzaccVLNewAdbShadowSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_BrzaccVLNewAdbShadowSwVersion_Type.__name__ = "DisplayString"
_BrzaccVLNewAdbShadowSwVersion_Object = MibTableColumn
brzaccVLNewAdbShadowSwVersion = _BrzaccVLNewAdbShadowSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 47),
    _BrzaccVLNewAdbShadowSwVersion_Type()
)
brzaccVLNewAdbShadowSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbShadowSwVersion.setStatus("current")


class _BrzaccVLNewAdbReadOnlyCommunity_Type(DisplayString):
    """Custom type brzaccVLNewAdbReadOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BrzaccVLNewAdbReadOnlyCommunity_Type.__name__ = "DisplayString"
_BrzaccVLNewAdbReadOnlyCommunity_Object = MibTableColumn
brzaccVLNewAdbReadOnlyCommunity = _BrzaccVLNewAdbReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 48),
    _BrzaccVLNewAdbReadOnlyCommunity_Type()
)
brzaccVLNewAdbReadOnlyCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbReadOnlyCommunity.setStatus("current")


class _BrzaccVLNewAdbWriteCommunity_Type(DisplayString):
    """Custom type brzaccVLNewAdbWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BrzaccVLNewAdbWriteCommunity_Type.__name__ = "DisplayString"
_BrzaccVLNewAdbWriteCommunity_Object = MibTableColumn
brzaccVLNewAdbWriteCommunity = _BrzaccVLNewAdbWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 49),
    _BrzaccVLNewAdbWriteCommunity_Type()
)
brzaccVLNewAdbWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbWriteCommunity.setStatus("current")
_BrzaccVLNewAdbAIFS_Type = Integer32
_BrzaccVLNewAdbAIFS_Object = MibTableColumn
brzaccVLNewAdbAIFS = _BrzaccVLNewAdbAIFS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 50),
    _BrzaccVLNewAdbAIFS_Type()
)
brzaccVLNewAdbAIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbAIFS.setStatus("current")
_BrzaccVLNewAdbMinimumCW_Type = Integer32
_BrzaccVLNewAdbMinimumCW_Object = MibTableColumn
brzaccVLNewAdbMinimumCW = _BrzaccVLNewAdbMinimumCW_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 51),
    _BrzaccVLNewAdbMinimumCW_Type()
)
brzaccVLNewAdbMinimumCW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMinimumCW.setStatus("current")
_BrzaccVLNewAdbMaximumCW_Type = Integer32
_BrzaccVLNewAdbMaximumCW_Object = MibTableColumn
brzaccVLNewAdbMaximumCW = _BrzaccVLNewAdbMaximumCW_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 52),
    _BrzaccVLNewAdbMaximumCW_Type()
)
brzaccVLNewAdbMaximumCW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbMaximumCW.setStatus("current")


class _BrzaccVLNewAdbESSID_Type(DisplayString):
    """Custom type brzaccVLNewAdbESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BrzaccVLNewAdbESSID_Type.__name__ = "DisplayString"
_BrzaccVLNewAdbESSID_Object = MibTableColumn
brzaccVLNewAdbESSID = _BrzaccVLNewAdbESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 53),
    _BrzaccVLNewAdbESSID_Type()
)
brzaccVLNewAdbESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbESSID.setStatus("current")
_BrzaccVLNewAdbRSSI_Type = Integer32
_BrzaccVLNewAdbRSSI_Object = MibTableColumn
brzaccVLNewAdbRSSI = _BrzaccVLNewAdbRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 54),
    _BrzaccVLNewAdbRSSI_Type()
)
brzaccVLNewAdbRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbRSSI.setStatus("current")


class _BrzaccVLNewAdbDfsOption_Type(Integer32):
    """Custom type brzaccVLNewAdbDfsOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BrzaccVLNewAdbDfsOption_Type.__name__ = "Integer32"
_BrzaccVLNewAdbDfsOption_Object = MibTableColumn
brzaccVLNewAdbDfsOption = _BrzaccVLNewAdbDfsOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 3, 1, 55),
    _BrzaccVLNewAdbDfsOption_Type()
)
brzaccVLNewAdbDfsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewAdbDfsOption.setStatus("current")
_BrzaccVLAggregateMIRCIR_ObjectIdentity = ObjectIdentity
brzaccVLAggregateMIRCIR = _BrzaccVLAggregateMIRCIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 4)
)
_BrzaccVLAggregateMIRUplink_Type = Integer32
_BrzaccVLAggregateMIRUplink_Object = MibScalar
brzaccVLAggregateMIRUplink = _BrzaccVLAggregateMIRUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 4, 1),
    _BrzaccVLAggregateMIRUplink_Type()
)
brzaccVLAggregateMIRUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAggregateMIRUplink.setStatus("current")
_BrzaccVLAggregateMIRDownlink_Type = Integer32
_BrzaccVLAggregateMIRDownlink_Object = MibScalar
brzaccVLAggregateMIRDownlink = _BrzaccVLAggregateMIRDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 4, 2),
    _BrzaccVLAggregateMIRDownlink_Type()
)
brzaccVLAggregateMIRDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAggregateMIRDownlink.setStatus("current")
_BrzaccVLAggregateCIRUplink_Type = Integer32
_BrzaccVLAggregateCIRUplink_Object = MibScalar
brzaccVLAggregateCIRUplink = _BrzaccVLAggregateCIRUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 4, 3),
    _BrzaccVLAggregateCIRUplink_Type()
)
brzaccVLAggregateCIRUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAggregateCIRUplink.setStatus("current")
_BrzaccVLAggregateCIRDownlink_Type = Integer32
_BrzaccVLAggregateCIRDownlink_Object = MibScalar
brzaccVLAggregateCIRDownlink = _BrzaccVLAggregateCIRDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 4, 4),
    _BrzaccVLAggregateCIRDownlink_Type()
)
brzaccVLAggregateCIRDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAggregateCIRDownlink.setStatus("current")
_BrzaccVLUpLinkQualityIndicator_ObjectIdentity = ObjectIdentity
brzaccVLUpLinkQualityIndicator = _BrzaccVLUpLinkQualityIndicator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6)
)


class _BrzaccVLMeasureUpLinkQualityIndicator_Type(Integer32):
    """Custom type brzaccVLMeasureUpLinkQualityIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("start", 1))
    )


_BrzaccVLMeasureUpLinkQualityIndicator_Type.__name__ = "Integer32"
_BrzaccVLMeasureUpLinkQualityIndicator_Object = MibScalar
brzaccVLMeasureUpLinkQualityIndicator = _BrzaccVLMeasureUpLinkQualityIndicator_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 1),
    _BrzaccVLMeasureUpLinkQualityIndicator_Type()
)
brzaccVLMeasureUpLinkQualityIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzaccVLMeasureUpLinkQualityIndicator.setStatus("current")
_BrzaccVLReadUpLinkQualityIndicator_Type = Integer32
_BrzaccVLReadUpLinkQualityIndicator_Object = MibScalar
brzaccVLReadUpLinkQualityIndicator = _BrzaccVLReadUpLinkQualityIndicator_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 2),
    _BrzaccVLReadUpLinkQualityIndicator_Type()
)
brzaccVLReadUpLinkQualityIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLReadUpLinkQualityIndicator.setStatus("current")


class _BrzaccVLUpLinkQualityIndicatorStatus_Type(Integer32):
    """Custom type brzaccVLUpLinkQualityIndicatorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullTest", 1),
          ("limitedTest", 2))
    )


_BrzaccVLUpLinkQualityIndicatorStatus_Type.__name__ = "Integer32"
_BrzaccVLUpLinkQualityIndicatorStatus_Object = MibScalar
brzaccVLUpLinkQualityIndicatorStatus = _BrzaccVLUpLinkQualityIndicatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 3),
    _BrzaccVLUpLinkQualityIndicatorStatus_Type()
)
brzaccVLUpLinkQualityIndicatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLUpLinkQualityIndicatorStatus.setStatus("current")
_BrzaccVLMacPinpoint_ObjectIdentity = ObjectIdentity
brzaccVLMacPinpoint = _BrzaccVLMacPinpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7)
)
_BrzaccVLMacPinpointTable_Object = MibTable
brzaccVLMacPinpointTable = _BrzaccVLMacPinpointTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1)
)
if mibBuilder.loadTexts:
    brzaccVLMacPinpointTable.setStatus("current")
_BrzaccVLMacPinpointEntry_Object = MibTableRow
brzaccVLMacPinpointEntry = _BrzaccVLMacPinpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1)
)
brzaccVLMacPinpointEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "mptEthernetStationMACAddress"),
)
if mibBuilder.loadTexts:
    brzaccVLMacPinpointEntry.setStatus("current")
_MptEthernetStationMACAddress_Type = MacAddress
_MptEthernetStationMACAddress_Object = MibTableColumn
mptEthernetStationMACAddress = _MptEthernetStationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1, 1),
    _MptEthernetStationMACAddress_Type()
)
mptEthernetStationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptEthernetStationMACAddress.setStatus("current")
_MptUnitMACAddress_Type = MacAddress
_MptUnitMACAddress_Object = MibTableColumn
mptUnitMACAddress = _MptUnitMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1, 2),
    _MptUnitMACAddress_Type()
)
mptUnitMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptUnitMACAddress.setStatus("current")
_BrzaccVLDrapGatewaysTable_Object = MibTable
brzaccVLDrapGatewaysTable = _BrzaccVLDrapGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8)
)
if mibBuilder.loadTexts:
    brzaccVLDrapGatewaysTable.setStatus("current")
_BrzaccVLDrapGatewayEntry_Object = MibTableRow
brzaccVLDrapGatewayEntry = _BrzaccVLDrapGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1)
)
brzaccVLDrapGatewayEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLDrapGatewayIndex"),
)
if mibBuilder.loadTexts:
    brzaccVLDrapGatewayEntry.setStatus("current")


class _BrzaccVLDrapGatewayIndex_Type(Integer32):
    """Custom type brzaccVLDrapGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BrzaccVLDrapGatewayIndex_Type.__name__ = "Integer32"
_BrzaccVLDrapGatewayIndex_Object = MibTableColumn
brzaccVLDrapGatewayIndex = _BrzaccVLDrapGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 1),
    _BrzaccVLDrapGatewayIndex_Type()
)
brzaccVLDrapGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDrapGatewayIndex.setStatus("current")
_BrzaccVLDrapGatewayIP_Type = IpAddress
_BrzaccVLDrapGatewayIP_Object = MibTableColumn
brzaccVLDrapGatewayIP = _BrzaccVLDrapGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 2),
    _BrzaccVLDrapGatewayIP_Type()
)
brzaccVLDrapGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDrapGatewayIP.setStatus("current")


class _BrzaccVLDrapGatewayType_Type(Integer32):
    """Custom type brzaccVLDrapGatewayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ngData4Wireless", 11),
          ("vgData1Voice1", 5),
          ("vgData4Voice2", 6),
          ("vgDataVoice", 4),
          ("vgDataVoice2", 7),
          ("vgUnknown", 255))
    )


_BrzaccVLDrapGatewayType_Type.__name__ = "Integer32"
_BrzaccVLDrapGatewayType_Object = MibTableColumn
brzaccVLDrapGatewayType = _BrzaccVLDrapGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 3),
    _BrzaccVLDrapGatewayType_Type()
)
brzaccVLDrapGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDrapGatewayType.setStatus("current")
_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Type = Integer32
_BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Object = MibTableColumn
brzaccVLDrapGatewayNoOfActiveVoiceCalls = _BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 4),
    _BrzaccVLDrapGatewayNoOfActiveVoiceCalls_Type()
)
brzaccVLDrapGatewayNoOfActiveVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDrapGatewayNoOfActiveVoiceCalls.setStatus("current")
_BrzaccVLHiddenESSIDTable_Object = MibTable
brzaccVLHiddenESSIDTable = _BrzaccVLHiddenESSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 9)
)
if mibBuilder.loadTexts:
    brzaccVLHiddenESSIDTable.setStatus("current")
_BrzaccVLHiddenESSIDEntry_Object = MibTableRow
brzaccVLHiddenESSIDEntry = _BrzaccVLHiddenESSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 9, 1)
)
brzaccVLHiddenESSIDEntry.setIndexNames(
    (0, "ALVARION-DOT11-WLAN-MIB", "brzaccVLHiddenESSIDMacAddress"),
)
if mibBuilder.loadTexts:
    brzaccVLHiddenESSIDEntry.setStatus("current")
_BrzaccVLHiddenESSIDMacAddress_Type = MacAddress
_BrzaccVLHiddenESSIDMacAddress_Object = MibTableColumn
brzaccVLHiddenESSIDMacAddress = _BrzaccVLHiddenESSIDMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 9, 1, 1),
    _BrzaccVLHiddenESSIDMacAddress_Type()
)
brzaccVLHiddenESSIDMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLHiddenESSIDMacAddress.setStatus("current")
_BrzaccVLHiddenESSIDAge_Type = Integer32
_BrzaccVLHiddenESSIDAge_Object = MibTableColumn
brzaccVLHiddenESSIDAge = _BrzaccVLHiddenESSIDAge_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 9, 1, 2),
    _BrzaccVLHiddenESSIDAge_Type()
)
brzaccVLHiddenESSIDAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLHiddenESSIDAge.setStatus("current")
_BrzaccVLAverageReceiveRSSI_Type = Integer32
_BrzaccVLAverageReceiveRSSI_Object = MibScalar
brzaccVLAverageReceiveRSSI = _BrzaccVLAverageReceiveRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 10),
    _BrzaccVLAverageReceiveRSSI_Type()
)
brzaccVLAverageReceiveRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAverageReceiveRSSI.setStatus("current")
_BrzaccVLCurrentNoiseFloor_Type = Integer32
_BrzaccVLCurrentNoiseFloor_Object = MibScalar
brzaccVLCurrentNoiseFloor = _BrzaccVLCurrentNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 11),
    _BrzaccVLCurrentNoiseFloor_Type()
)
brzaccVLCurrentNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLCurrentNoiseFloor.setStatus("current")
_BrzaccVLAverageSignalInterferenceRatio_Type = Integer32
_BrzaccVLAverageSignalInterferenceRatio_Object = MibScalar
brzaccVLAverageSignalInterferenceRatio = _BrzaccVLAverageSignalInterferenceRatio_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 12),
    _BrzaccVLAverageSignalInterferenceRatio_Type()
)
brzaccVLAverageSignalInterferenceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLAverageSignalInterferenceRatio.setStatus("current")
_BrzaccVLTraps_ObjectIdentity = ObjectIdentity
brzaccVLTraps = _BrzaccVLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14)
)
_BrzaccVLTrapSUMacAddr_Type = MacAddress
_BrzaccVLTrapSUMacAddr_Object = MibScalar
brzaccVLTrapSUMacAddr = _BrzaccVLTrapSUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 1),
    _BrzaccVLTrapSUMacAddr_Type()
)
brzaccVLTrapSUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapSUMacAddr.setStatus("current")
_BrzaccVLTrapText_Type = DisplayString
_BrzaccVLTrapText_Object = MibScalar
brzaccVLTrapText = _BrzaccVLTrapText_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 3),
    _BrzaccVLTrapText_Type()
)
brzaccVLTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapText.setStatus("current")


class _BrzaccVLTrapToggle_Type(Integer32):
    """Custom type brzaccVLTrapToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrzaccVLTrapToggle_Type.__name__ = "Integer32"
_BrzaccVLTrapToggle_Object = MibScalar
brzaccVLTrapToggle = _BrzaccVLTrapToggle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 4),
    _BrzaccVLTrapToggle_Type()
)
brzaccVLTrapToggle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapToggle.setStatus("current")


class _BrzaccVLTrapParameterChanged_Type(Integer32):
    """Custom type brzaccVLTrapParameterChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cirOrMir", 1),
          ("ipFilter", 2),
          ("vlan", 4))
    )


_BrzaccVLTrapParameterChanged_Type.__name__ = "Integer32"
_BrzaccVLTrapParameterChanged_Object = MibScalar
brzaccVLTrapParameterChanged = _BrzaccVLTrapParameterChanged_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 5),
    _BrzaccVLTrapParameterChanged_Type()
)
brzaccVLTrapParameterChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapParameterChanged.setStatus("current")


class _BrzaccVLTrapAccessRights_Type(Integer32):
    """Custom type brzaccVLTrapAccessRights based on Integer32"""
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
        *(("administrator", 4),
          ("factory", 5),
          ("installer", 3),
          ("notLoggedIn", 1),
          ("readOnly", 2))
    )


_BrzaccVLTrapAccessRights_Type.__name__ = "Integer32"
_BrzaccVLTrapAccessRights_Object = MibScalar
brzaccVLTrapAccessRights = _BrzaccVLTrapAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 6),
    _BrzaccVLTrapAccessRights_Type()
)
brzaccVLTrapAccessRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapAccessRights.setStatus("current")


class _BrzaccVLTrapLog_Type(Integer32):
    """Custom type brzaccVLTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telnetLogin", 3),
          ("telnetLogout", 4))
    )


_BrzaccVLTrapLog_Type.__name__ = "Integer32"
_BrzaccVLTrapLog_Object = MibScalar
brzaccVLTrapLog = _BrzaccVLTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 7),
    _BrzaccVLTrapLog_Type()
)
brzaccVLTrapLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapLog.setStatus("current")
_BrzaccVLTrapTelnetUserIpAddress_Type = IpAddress
_BrzaccVLTrapTelnetUserIpAddress_Object = MibScalar
brzaccVLTrapTelnetUserIpAddress = _BrzaccVLTrapTelnetUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 8),
    _BrzaccVLTrapTelnetUserIpAddress_Type()
)
brzaccVLTrapTelnetUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapTelnetUserIpAddress.setStatus("current")
_BrzaccVLTrapRTx_Type = Integer32
_BrzaccVLTrapRTx_Object = MibScalar
brzaccVLTrapRTx = _BrzaccVLTrapRTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 9),
    _BrzaccVLTrapRTx_Type()
)
brzaccVLTrapRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapRTx.setStatus("current")


class _BrzaccVLTrapFtpOrTftpStatus_Type(Integer32):
    """Custom type brzaccVLTrapFtpOrTftpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("successful", 1))
    )


_BrzaccVLTrapFtpOrTftpStatus_Type.__name__ = "Integer32"
_BrzaccVLTrapFtpOrTftpStatus_Object = MibScalar
brzaccVLTrapFtpOrTftpStatus = _BrzaccVLTrapFtpOrTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 10),
    _BrzaccVLTrapFtpOrTftpStatus_Type()
)
brzaccVLTrapFtpOrTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapFtpOrTftpStatus.setStatus("current")
_BrzaccVLDFSMoveFreq_Type = Integer32
_BrzaccVLDFSMoveFreq_Object = MibScalar
brzaccVLDFSMoveFreq = _BrzaccVLDFSMoveFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 11),
    _BrzaccVLDFSMoveFreq_Type()
)
brzaccVLDFSMoveFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSMoveFreq.setStatus("current")
_BrzaccVLDFSMoveFreqNew_Type = DisplayString
_BrzaccVLDFSMoveFreqNew_Object = MibScalar
brzaccVLDFSMoveFreqNew = _BrzaccVLDFSMoveFreqNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 12),
    _BrzaccVLDFSMoveFreqNew_Type()
)
brzaccVLDFSMoveFreqNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLDFSMoveFreqNew.setStatus("current")
_BrzaccVLEthBroadcastThresholdExceeded_Type = Integer32
_BrzaccVLEthBroadcastThresholdExceeded_Object = MibScalar
brzaccVLEthBroadcastThresholdExceeded = _BrzaccVLEthBroadcastThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 13),
    _BrzaccVLEthBroadcastThresholdExceeded_Type()
)
brzaccVLEthBroadcastThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastThresholdExceeded.setStatus("current")


class _BrzaccVLTrapSubscriberType_Type(Integer32):
    """Custom type brzaccVLTrapSubscriberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              8,
              14,
              24,
              28,
              54,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rb-100", 100),
          ("rb-14", 14),
          ("rb-28", 28),
          ("su-24", 24),
          ("su-3", 3),
          ("su-54", 54),
          ("su-6", 6),
          ("su-8", 8),
          ("unknownSubscriberType", 0))
    )


_BrzaccVLTrapSubscriberType_Type.__name__ = "Integer32"
_BrzaccVLTrapSubscriberType_Object = MibScalar
brzaccVLTrapSubscriberType = _BrzaccVLTrapSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 14),
    _BrzaccVLTrapSubscriberType_Type()
)
brzaccVLTrapSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapSubscriberType.setStatus("current")
_BrzaccVLTrapMACAddress_Type = MacAddress
_BrzaccVLTrapMACAddress_Object = MibScalar
brzaccVLTrapMACAddress = _BrzaccVLTrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 15),
    _BrzaccVLTrapMACAddress_Type()
)
brzaccVLTrapMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapMACAddress.setStatus("current")


class _BrzaccVLNewUnitTypeTrap_Type(Integer32):
    """Custom type brzaccVLNewUnitTypeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bu", 1),
          ("rb", 2))
    )


_BrzaccVLNewUnitTypeTrap_Type.__name__ = "Integer32"
_BrzaccVLNewUnitTypeTrap_Object = MibScalar
brzaccVLNewUnitTypeTrap = _BrzaccVLNewUnitTypeTrap_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 16),
    _BrzaccVLNewUnitTypeTrap_Type()
)
brzaccVLNewUnitTypeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLNewUnitTypeTrap.setStatus("current")
_BrzaccVLTrapSWVersion_Type = DisplayString
_BrzaccVLTrapSWVersion_Object = MibScalar
brzaccVLTrapSWVersion = _BrzaccVLTrapSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 17),
    _BrzaccVLTrapSWVersion_Type()
)
brzaccVLTrapSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapSWVersion.setStatus("current")
_BrzaccVLTrapSequenceNumber_Type = Integer32
_BrzaccVLTrapSequenceNumber_Object = MibScalar
brzaccVLTrapSequenceNumber = _BrzaccVLTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 18),
    _BrzaccVLTrapSequenceNumber_Type()
)
brzaccVLTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapSequenceNumber.setStatus("current")
_BrzaccVLTrapUnitMacAddr_Type = MacAddress
_BrzaccVLTrapUnitMacAddr_Object = MibScalar
brzaccVLTrapUnitMacAddr = _BrzaccVLTrapUnitMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 19),
    _BrzaccVLTrapUnitMacAddr_Type()
)
brzaccVLTrapUnitMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapUnitMacAddr.setStatus("current")
_BrzaccVLTrapParameterGroupCode_Type = Integer32
_BrzaccVLTrapParameterGroupCode_Object = MibScalar
brzaccVLTrapParameterGroupCode = _BrzaccVLTrapParameterGroupCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 20),
    _BrzaccVLTrapParameterGroupCode_Type()
)
brzaccVLTrapParameterGroupCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapParameterGroupCode.setStatus("current")
_BrzaccVLTrapNewIP_Type = IpAddress
_BrzaccVLTrapNewIP_Object = MibScalar
brzaccVLTrapNewIP = _BrzaccVLTrapNewIP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 21),
    _BrzaccVLTrapNewIP_Type()
)
brzaccVLTrapNewIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzaccVLTrapNewIP.setStatus("current")
_AlvarionOID_ObjectIdentity = ObjectIdentity
alvarionOID = _AlvarionOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4)
)
_BrzAccessVLOID_ObjectIdentity = ObjectIdentity
brzAccessVLOID = _BrzAccessVLOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1)
)
_BrzAccessVLAU_ObjectIdentity = ObjectIdentity
brzAccessVLAU = _BrzAccessVLAU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 1)
)
_BrzAccessVLSU_ObjectIdentity = ObjectIdentity
brzAccessVLSU = _BrzAccessVLSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 2)
)
_BrzAccessVLProducts_ObjectIdentity = ObjectIdentity
brzAccessVLProducts = _BrzAccessVLProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3)
)
_BrzAccessVLAU_BS_ObjectIdentity = ObjectIdentity
brzAccessVLAU_BS = _BrzAccessVLAU_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 4)
)
_BrzAccessVLAU_SA_ObjectIdentity = ObjectIdentity
brzAccessVLAU_SA = _BrzAccessVLAU_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 5)
)
_BrzAccessVLAUS_BS_ObjectIdentity = ObjectIdentity
brzAccessVLAUS_BS = _BrzAccessVLAUS_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 6)
)
_BrzAccessVLAUS_SA_ObjectIdentity = ObjectIdentity
brzAccessVLAUS_SA = _BrzAccessVLAUS_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 7)
)
_BrzAccessAU_EZ_ObjectIdentity = ObjectIdentity
brzAccessAU_EZ = _BrzAccessAU_EZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 8)
)
_BrzAccessVLSU_6_1D_ObjectIdentity = ObjectIdentity
brzAccessVLSU_6_1D = _BrzAccessVLSU_6_1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 11)
)
_BrzAccessVLSU_6_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_6_BD = _BrzAccessVLSU_6_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 12)
)
_BrzAccessVLSU_24_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_24_BD = _BrzAccessVLSU_24_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 13)
)
_BrzAccessVLSU_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_BD = _BrzAccessVLSU_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 14)
)
_BrzAccessVLSU_54_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_54_BD = _BrzAccessVLSU_54_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 15)
)
_BrzAccessVLSU_3_1D_ObjectIdentity = ObjectIdentity
brzAccessVLSU_3_1D = _BrzAccessVLSU_3_1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 16)
)
_BrzAccessVLSU_3_4D_ObjectIdentity = ObjectIdentity
brzAccessVLSU_3_4D = _BrzAccessVLSU_3_4D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 17)
)
_BrzAccessVLSU_I_ObjectIdentity = ObjectIdentity
brzAccessVLSU_I = _BrzAccessVLSU_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 18)
)
_BrzAccessVLSU_EZ_ObjectIdentity = ObjectIdentity
brzAccessVLSU_EZ = _BrzAccessVLSU_EZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 19)
)
_BrzAccessVLSU_V_ObjectIdentity = ObjectIdentity
brzAccessVLSU_V = _BrzAccessVLSU_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 20)
)
_BrzNetB_BU_B14_ObjectIdentity = ObjectIdentity
brzNetB_BU_B14 = _BrzNetB_BU_B14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 21)
)
_BrzNetB_BU_B28_ObjectIdentity = ObjectIdentity
brzNetB_BU_B28 = _BrzNetB_BU_B28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 22)
)
_BrzNetB_BU_B100_ObjectIdentity = ObjectIdentity
brzNetB_BU_B100 = _BrzNetB_BU_B100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 23)
)
_BrzNetB_BU_B10_ObjectIdentity = ObjectIdentity
brzNetB_BU_B10 = _BrzNetB_BU_B10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 24)
)
_BrzNetB_RB_B14_ObjectIdentity = ObjectIdentity
brzNetB_RB_B14 = _BrzNetB_RB_B14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 31)
)
_BrzNetB_RB_B28_ObjectIdentity = ObjectIdentity
brzNetB_RB_B28 = _BrzNetB_RB_B28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 32)
)
_BrzNetB_RB_B100_ObjectIdentity = ObjectIdentity
brzNetB_RB_B100 = _BrzNetB_RB_B100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 33)
)
_BrzNetB_RB_B10_ObjectIdentity = ObjectIdentity
brzNetB_RB_B10 = _BrzNetB_RB_B10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 34)
)
_BrzAccess4900_AU_BS_ObjectIdentity = ObjectIdentity
brzAccess4900_AU_BS = _BrzAccess4900_AU_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 41)
)
_BrzAccess4900_AU_SA_ObjectIdentity = ObjectIdentity
brzAccess4900_AU_SA = _BrzAccess4900_AU_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 42)
)
_BrzAccess4900_SU_BD_ObjectIdentity = ObjectIdentity
brzAccess4900_SU_BD = _BrzAccess4900_SU_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 51)
)
_BrzAccessVLSU_8_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_8_BD = _BrzAccessVLSU_8_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 61)
)
_BrzAccessVLSU_1_BD_ObjectIdentity = ObjectIdentity
brzAccessVLSU_1_BD = _BrzAccessVLSU_1_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 62)
)
_BrzAccessVLSU_3_L_ObjectIdentity = ObjectIdentity
brzAccessVLSU_3_L = _BrzAccessVLSU_3_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 63)
)
_BrzAccessVLSU_6_L_ObjectIdentity = ObjectIdentity
brzAccessVLSU_6_L = _BrzAccessVLSU_6_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 64)
)
_BrzAccessVLSU_12_L_ObjectIdentity = ObjectIdentity
brzAccessVLSU_12_L = _BrzAccessVLSU_12_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 65)
)
_BrzAccessVL_AU_ObjectIdentity = ObjectIdentity
brzAccessVL_AU = _BrzAccessVL_AU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 70)
)
_BrzAccessVL_SU_ObjectIdentity = ObjectIdentity
brzAccessVL_SU = _BrzAccessVL_SU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 75)
)

# Managed Objects groups


# Notification objects

brzaccVLSUassociatedAUTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 2)
)
brzaccVLSUassociatedAUTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSUMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLSUassociatedAUTRAP.setStatus(
        "current"
    )

brzaccVLAUdisassociatedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 3)
)
brzaccVLAUdisassociatedTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSUMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLAUdisassociatedTRAP.setStatus(
        "current"
    )

brzaccVLAUagingTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 4)
)
brzaccVLAUagingTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSUMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLAUagingTRAP.setStatus(
        "current"
    )

brzaccVLSUassociatedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 6)
)
brzaccVLSUassociatedTRAP.setObjects(
    ("ALVARION-DOT11-WLAN-MIB", "brzaccVLAssociatedAU")
)
if mibBuilder.loadTexts:
    brzaccVLSUassociatedTRAP.setStatus(
        "current"
    )

brzaccVLAUwirelessQualityTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 20)
)
brzaccVLAUwirelessQualityTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapToggle"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapUnitMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapRTx"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLAUwirelessQualityTRAP.setStatus(
        "current"
    )

brzaccVLPowerUpFromReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 101)
)
brzaccVLPowerUpFromReset.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLUnitMacAddress"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLPowerUpFromReset.setStatus(
        "current"
    )

brzaccVLTelnetStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 102)
)
brzaccVLTelnetStatusTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapLog"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapTelnetUserIpAddress"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapAccessRights"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapUnitMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLTelnetStatusTRAP.setStatus(
        "current"
    )

brzaccVLParameterChangedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 103)
)
brzaccVLParameterChangedTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapParameterChanged"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLParameterChangedTRAP.setStatus(
        "current"
    )

brzaccVLLoadingStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 104)
)
brzaccVLLoadingStatusTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapFtpOrTftpStatus"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLUnitMacAddress"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLLoadingStatusTRAP.setStatus(
        "current"
    )

brzaccVLPromiscuousModeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 105)
)
brzaccVLPromiscuousModeTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapToggle"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLUnitMacAddress"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLPromiscuousModeTRAP.setStatus(
        "current"
    )

brzaccVLDFSRadarDetectedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 106)
)
brzaccVLDFSRadarDetectedTRAP.setObjects(
    ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber")
)
if mibBuilder.loadTexts:
    brzaccVLDFSRadarDetectedTRAP.setStatus(
        "current"
    )

brzaccVLDFSFrequencyTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 107)
)
brzaccVLDFSFrequencyTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLDFSMoveFreq"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLDFSMoveFreqNew"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLDFSFrequencyTRAP.setStatus(
        "current"
    )

brzaccVLDFSNoFreeChannelsExistsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 108)
)
brzaccVLDFSNoFreeChannelsExistsTRAP.setObjects(
    ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber")
)
if mibBuilder.loadTexts:
    brzaccVLDFSNoFreeChannelsExistsTRAP.setStatus(
        "current"
    )

brzaccVLEthBroadcastMulticastLimiterTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 109)
)
brzaccVLEthBroadcastMulticastLimiterTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLEthBroadcastThresholdExceeded"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapUnitMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLEthBroadcastMulticastLimiterTRAP.setStatus(
        "current"
    )

brzaccVLAUSUnsupportedSubscriberTypeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 110)
)
brzaccVLAUSUnsupportedSubscriberTypeTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSUMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSubscriberType"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLAUSUnsupportedSubscriberTypeTRAP.setStatus(
        "current"
    )

brzaccVLUnitTypeChangedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 111)
)
brzaccVLUnitTypeChangedTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapMACAddress"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLNewUnitTypeTrap"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLUnitTypeChangedTRAP.setStatus(
        "current"
    )

brzaccVLWLPrioritizationNotSupportedBySUTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 112)
)
brzaccVLWLPrioritizationNotSupportedBySUTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSUMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSWVersion"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLWLPrioritizationNotSupportedBySUTRAP.setStatus(
        "current"
    )

brzaccVLParameterChangeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 113)
)
brzaccVLParameterChangeTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapUnitMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapParameterGroupCode"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLParameterChangeTRAP.setStatus(
        "current"
    )

brzaccVLRunTimeIPChangeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 114)
)
brzaccVLRunTimeIPChangeTRAP.setObjects(
      *(("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapUnitMacAddr"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapNewIP"),
        ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber"))
)
if mibBuilder.loadTexts:
    brzaccVLRunTimeIPChangeTRAP.setStatus(
        "current"
    )

brzaccVLDisassociateAllStationsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 115)
)
brzaccVLDisassociateAllStationsTRAP.setObjects(
    ("ALVARION-DOT11-WLAN-MIB", "brzaccVLTrapSequenceNumber")
)
if mibBuilder.loadTexts:
    brzaccVLDisassociateAllStationsTRAP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-DOT11-WLAN-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "alvarion": alvarion,
       "products": products,
       "breezeAccessVLMib": breezeAccessVLMib,
       "brzaccVLSysInfo": brzaccVLSysInfo,
       "brzaccVLUnitHwVersion": brzaccVLUnitHwVersion,
       "brzaccVLRunningSoftwareVersion": brzaccVLRunningSoftwareVersion,
       "brzaccVLRunningFrom": brzaccVLRunningFrom,
       "brzaccVLMainVersionNumber": brzaccVLMainVersionNumber,
       "brzaccVLMainVersionFileName": brzaccVLMainVersionFileName,
       "brzaccVLShadowVersionNumber": brzaccVLShadowVersionNumber,
       "brzaccVLShadowVersionFileName": brzaccVLShadowVersionFileName,
       "brzaccVLUnitMacAddress": brzaccVLUnitMacAddress,
       "brzaccVLUnitType": brzaccVLUnitType,
       "brzaccVLAssociatedAU": brzaccVLAssociatedAU,
       "brzaccVLNumOfAssociationsSinceLastReset": brzaccVLNumOfAssociationsSinceLastReset,
       "brzaccVLCurrentNumOfAssociations": brzaccVLCurrentNumOfAssociations,
       "brzaccVLUnitBootVersion": brzaccVLUnitBootVersion,
       "brzaccVLRadioBand": brzaccVLRadioBand,
       "brzaccVLCurrentEthernetPortState": brzaccVLCurrentEthernetPortState,
       "brzaccVLTimeSinceLastReset": brzaccVLTimeSinceLastReset,
       "brzaccVLCountryDependentParameters": brzaccVLCountryDependentParameters,
       "brzaccVLCountryCode": brzaccVLCountryCode,
       "brzaccVLCountryDependentParamsTable": brzaccVLCountryDependentParamsTable,
       "brzaccVLCountryDependentParameterEntry": brzaccVLCountryDependentParameterEntry,
       "brzaccVLCountryDependentParameterTableIdx": brzaccVLCountryDependentParameterTableIdx,
       "brzaccVLCountryDependentParameterFrequencies": brzaccVLCountryDependentParameterFrequencies,
       "brzaccVLAllowedBandwidth": brzaccVLAllowedBandwidth,
       "brzaccVLRegulationMaxTxPowerAtAntennaPort": brzaccVLRegulationMaxTxPowerAtAntennaPort,
       "brzaccVLRegulationMaxEIRP": brzaccVLRegulationMaxEIRP,
       "brzaccVLMinModulationLevel": brzaccVLMinModulationLevel,
       "brzaccVLMaxModulationLevel": brzaccVLMaxModulationLevel,
       "brzaccVLBurstModeSupport": brzaccVLBurstModeSupport,
       "brzaccVLMaximumBurstDuration": brzaccVLMaximumBurstDuration,
       "brzaccVLDfsSupport": brzaccVLDfsSupport,
       "brzaccVLMinimumHwRevision": brzaccVLMinimumHwRevision,
       "brzaccVLAuthenticationEncryptionSupport": brzaccVLAuthenticationEncryptionSupport,
       "brzaccVLDataEncryptionSupport": brzaccVLDataEncryptionSupport,
       "brzaccVLAESEncryptionSupport": brzaccVLAESEncryptionSupport,
       "brzaccVLAntennaGainChange": brzaccVLAntennaGainChange,
       "brzaccVLAteTestResults": brzaccVLAteTestResults,
       "brzaccVLSerialNumber": brzaccVLSerialNumber,
       "brzaccVLAUSSupportSU54": brzaccVLAUSSupportSU54,
       "brzaccVLNumOfRejectionsSinceLastReset": brzaccVLNumOfRejectionsSinceLastReset,
       "brzaccVLAUSSupportSU8": brzaccVLAUSSupportSU8,
       "brzaccVLUnitControl": brzaccVLUnitControl,
       "brzaccVLResetUnit": brzaccVLResetUnit,
       "brzaccVLSetDefaults": brzaccVLSetDefaults,
       "brzaccVLUnitName": brzaccVLUnitName,
       "brzaccVLFlashMemoryControl": brzaccVLFlashMemoryControl,
       "brzaccVLTelnetLogoutTimer": brzaccVLTelnetLogoutTimer,
       "brzaccVLSaveCurrentConfigurationAsOperatorDefaults": brzaccVLSaveCurrentConfigurationAsOperatorDefaults,
       "brzaccVLExitTelnet": brzaccVLExitTelnet,
       "brzaccVLUnitPasswords": brzaccVLUnitPasswords,
       "brzaccVLReadOnlyPassword": brzaccVLReadOnlyPassword,
       "brzaccVLInstallerPassword": brzaccVLInstallerPassword,
       "brzaccVLAdminPassword": brzaccVLAdminPassword,
       "brzaccVLEthernetNegotiationMode": brzaccVLEthernetNegotiationMode,
       "brzaccVLFTPParameters": brzaccVLFTPParameters,
       "brzaccVLFTPServerParams": brzaccVLFTPServerParams,
       "brzaccVLFTPServerUserName": brzaccVLFTPServerUserName,
       "brzaccVLFTPServerPassword": brzaccVLFTPServerPassword,
       "brzaccVLFTPClientIPAddress": brzaccVLFTPClientIPAddress,
       "brzaccVLFTPServerIpAddress": brzaccVLFTPServerIpAddress,
       "brzaccVLFTPClientMask": brzaccVLFTPClientMask,
       "brzaccVLFTPGatewayIpAddress": brzaccVLFTPGatewayIpAddress,
       "brzaccVLFTPSwDownload": brzaccVLFTPSwDownload,
       "brzaccVLFTPSwFileName": brzaccVLFTPSwFileName,
       "brzaccVLFTPSwSourceDir": brzaccVLFTPSwSourceDir,
       "brzaccVLFTPDownloadSwFile": brzaccVLFTPDownloadSwFile,
       "brzaccVLConfigurationFileLoading": brzaccVLConfigurationFileLoading,
       "brzaccVLConfigurationFileName": brzaccVLConfigurationFileName,
       "brzaccVLOperatorDefaultsFileName": brzaccVLOperatorDefaultsFileName,
       "brzaccVLFTPConfigurationFileSourceDir": brzaccVLFTPConfigurationFileSourceDir,
       "brzaccVLExecuteFTPConfigurationFileLoading": brzaccVLExecuteFTPConfigurationFileLoading,
       "brzaccVLEventLogFileUploading": brzaccVLEventLogFileUploading,
       "brzaccVLEventLogFileName": brzaccVLEventLogFileName,
       "brzaccVLEventLogDestinationDir": brzaccVLEventLogDestinationDir,
       "brzaccVLUploadEventLogFile": brzaccVLUploadEventLogFile,
       "brzaccVLLoadingStatus": brzaccVLLoadingStatus,
       "brzaccVLEventLogFileParams": brzaccVLEventLogFileParams,
       "brzaccVLEventLogPolicy": brzaccVLEventLogPolicy,
       "brzaccVLEraseEventLog": brzaccVLEraseEventLog,
       "brzaccVLSystemLocation": brzaccVLSystemLocation,
       "brzaccVLFeatureUpgrade": brzaccVLFeatureUpgrade,
       "brzaccVLFeatureUpgradeManually": brzaccVLFeatureUpgradeManually,
       "brzaccVLChangeUnitType": brzaccVLChangeUnitType,
       "brzaccVLApWorkingMode": brzaccVLApWorkingMode,
       "brzaccVLLEDsettings": brzaccVLLEDsettings,
       "brzaccVLLEDmode": brzaccVLLEDmode,
       "brzaccVLThresholdTable": brzaccVLThresholdTable,
       "brzaccVLThresholdTableEntry": brzaccVLThresholdTableEntry,
       "brzaccVLThresholdLEDnum": brzaccVLThresholdLEDnum,
       "brzaccVLThresholdLEDtype": brzaccVLThresholdLEDtype,
       "brzaccVLThresholdLEDmode": brzaccVLThresholdLEDmode,
       "brzaccVLThresholdLEDtarget": brzaccVLThresholdLEDtarget,
       "brzaccVLNwMngParameters": brzaccVLNwMngParameters,
       "brzaccVLAccessToNwMng": brzaccVLAccessToNwMng,
       "brzaccVLNwMngFilter": brzaccVLNwMngFilter,
       "mngIpFilterTable": mngIpFilterTable,
       "mngIpFilterEntry": mngIpFilterEntry,
       "brzaccVLNwMngIpAddress": brzaccVLNwMngIpAddress,
       "brzaccVLNwMngIpTableIdx": brzaccVLNwMngIpTableIdx,
       "brzaccVLDeleteOneNwIpAddr": brzaccVLDeleteOneNwIpAddr,
       "brzaccVLDeleteAllNwIpAddrs": brzaccVLDeleteAllNwIpAddrs,
       "brzaccVLAccessToNwTrap": brzaccVLAccessToNwTrap,
       "mngTrapTable": mngTrapTable,
       "mngTrapEntry": mngTrapEntry,
       "brzaccVLNwMngTrapCommunity": brzaccVLNwMngTrapCommunity,
       "brzaccVLNwMngTrapAddress": brzaccVLNwMngTrapAddress,
       "brzaccVLNwTrapTableIdx": brzaccVLNwTrapTableIdx,
       "brzaccVLDeleteOneTrapAddr": brzaccVLDeleteOneTrapAddr,
       "brzaccVLDeleteAllTrapAddrs": brzaccVLDeleteAllTrapAddrs,
       "brzaccVLMngIpRangesTable": brzaccVLMngIpRangesTable,
       "brzaccVLMngIpRangeEntry": brzaccVLMngIpRangeEntry,
       "brzaccVLMngIpRangeIdx": brzaccVLMngIpRangeIdx,
       "brzaccVLMngIpRangeFlag": brzaccVLMngIpRangeFlag,
       "brzaccVLMngIpRangeStart": brzaccVLMngIpRangeStart,
       "brzaccVLMngIpRangeEnd": brzaccVLMngIpRangeEnd,
       "brzaccVLMngIpRangeMask": brzaccVLMngIpRangeMask,
       "brzaccVLDeleteOneNwIpRange": brzaccVLDeleteOneNwIpRange,
       "brzaccVLDeleteAllNwIpRanges": brzaccVLDeleteAllNwIpRanges,
       "brzaccVLWi2IpAddress": brzaccVLWi2IpAddress,
       "brzaccVLNewNMngSystem": brzaccVLNewNMngSystem,
       "brzaccVLErrorHandling": brzaccVLErrorHandling,
       "brzaccVLErrHandlingSetNMSId": brzaccVLErrHandlingSetNMSId,
       "brzaccVLErrHandlingTable": brzaccVLErrHandlingTable,
       "brzaccVLErrHandlingEntry": brzaccVLErrHandlingEntry,
       "brzaccVLErrHandlingNMSId": brzaccVLErrHandlingNMSId,
       "brzaccVLErrHandlingRequestId": brzaccVLErrHandlingRequestId,
       "brzaccVLErrHandlingErrorCode": brzaccVLErrHandlingErrorCode,
       "brzaccVLErrHandlingParameter1": brzaccVLErrHandlingParameter1,
       "brzaccVLErrHandlingParameter2": brzaccVLErrHandlingParameter2,
       "brzaccVLErrHandlingParameter3": brzaccVLErrHandlingParameter3,
       "brzaccVLErrHandlingParameter4": brzaccVLErrHandlingParameter4,
       "brzaccVLErrHandlingParameter5": brzaccVLErrHandlingParameter5,
       "brzaccVLTrapHistory": brzaccVLTrapHistory,
       "brzaccVLLastTrapSequenceNumber": brzaccVLLastTrapSequenceNumber,
       "brzaccVLTrapHistoryTable": brzaccVLTrapHistoryTable,
       "brzaccVLTrapHistoryEntry": brzaccVLTrapHistoryEntry,
       "brzaccVLTrapHistorySequenceNumber": brzaccVLTrapHistorySequenceNumber,
       "brzaccVLTrapType": brzaccVLTrapType,
       "brzaccVLTrapMacAddrParam": brzaccVLTrapMacAddrParam,
       "brzaccVLTrapIntParam1": brzaccVLTrapIntParam1,
       "brzaccVLTrapIntParam2": brzaccVLTrapIntParam2,
       "brzaccVLTrapIntParam3": brzaccVLTrapIntParam3,
       "brzaccVLTrapStrParam": brzaccVLTrapStrParam,
       "newMngIpFilterTable": newMngIpFilterTable,
       "newMngIpFilterEntry": newMngIpFilterEntry,
       "brzaccVLNewNwMngIpAddress": brzaccVLNewNwMngIpAddress,
       "brzaccVLNewNwMngIpAddressCommand": brzaccVLNewNwMngIpAddressCommand,
       "newMngTrapTable": newMngTrapTable,
       "newMngTrapEntry": newMngTrapEntry,
       "brzaccVLNewNwMngTrapCommunity": brzaccVLNewNwMngTrapCommunity,
       "brzaccVLNewNwMngTrapAddress": brzaccVLNewNwMngTrapAddress,
       "brzaccVLNewNwTrapCommand": brzaccVLNewNwTrapCommand,
       "brzaccVLNewMngIpRangesTable": brzaccVLNewMngIpRangesTable,
       "brzaccVLNewMngIpRangeEntry": brzaccVLNewMngIpRangeEntry,
       "brzaccVLNewMngIpRangeStart": brzaccVLNewMngIpRangeStart,
       "brzaccVLNewMngIpRangeEnd": brzaccVLNewMngIpRangeEnd,
       "brzaccVLNewMngIpRangeMask": brzaccVLNewMngIpRangeMask,
       "brzaccVLNewMngIpRangeFlag": brzaccVLNewMngIpRangeFlag,
       "brzaccVLNewMngIpRangeCommand": brzaccVLNewMngIpRangeCommand,
       "brzaccVLIpParams": brzaccVLIpParams,
       "brzaccVLUnitIpAddress": brzaccVLUnitIpAddress,
       "brzaccVLSubNetMask": brzaccVLSubNetMask,
       "brzaccVLDefaultGWAddress": brzaccVLDefaultGWAddress,
       "brzaccVLUseDhcp": brzaccVLUseDhcp,
       "brzaccVLAccessToDHCP": brzaccVLAccessToDHCP,
       "brzaccVLRunTimeIPaddr": brzaccVLRunTimeIPaddr,
       "brzaccVLRunTimeSubNetMask": brzaccVLRunTimeSubNetMask,
       "brzaccVLRunTimeDefaultIPGateway": brzaccVLRunTimeDefaultIPGateway,
       "brzaccVLBridgeParameters": brzaccVLBridgeParameters,
       "brzaccVLVLANSupport": brzaccVLVLANSupport,
       "brzaccVLVlanID": brzaccVLVlanID,
       "brzaccVLEthernetLinkType": brzaccVLEthernetLinkType,
       "brzaccVLManagementVlanID": brzaccVLManagementVlanID,
       "brzaccVLVLANForwarding": brzaccVLVLANForwarding,
       "brzaccVLVlanForwardingSupport": brzaccVLVlanForwardingSupport,
       "brzaccVLVlanForwardingTable": brzaccVLVlanForwardingTable,
       "brzaccVLVlanForwardingEntry": brzaccVLVlanForwardingEntry,
       "brzaccVLVlanForwardingTableIdx": brzaccVLVlanForwardingTableIdx,
       "brzaccVLVlanIdForwarding": brzaccVLVlanIdForwarding,
       "brzaccVLNewVlanForwardingTable": brzaccVLNewVlanForwardingTable,
       "brzaccVLNewVlanForwardingEntry": brzaccVLNewVlanForwardingEntry,
       "brzaccVLNewVlanIdForwarding": brzaccVLNewVlanIdForwarding,
       "brzaccVLNewVlanForwardingCommand": brzaccVLNewVlanForwardingCommand,
       "brzaccVLVlanRelaying": brzaccVLVlanRelaying,
       "brzaccVLVlanRelayingSupport": brzaccVLVlanRelayingSupport,
       "brzaccVLVlanRelayingTable": brzaccVLVlanRelayingTable,
       "brzaccVLVlanRelayingEntry": brzaccVLVlanRelayingEntry,
       "brzaccVLVlanRelayingTableIdx": brzaccVLVlanRelayingTableIdx,
       "brzaccVLVlanIdRelaying": brzaccVLVlanIdRelaying,
       "brzaccVLNewVlanRelayingTable": brzaccVLNewVlanRelayingTable,
       "brzaccVLNewVlanRelayingEntry": brzaccVLNewVlanRelayingEntry,
       "brzaccVLNewVlanIdRelaying": brzaccVLNewVlanIdRelaying,
       "brzaccVLNewVlanRelayingTableCommand": brzaccVLNewVlanRelayingTableCommand,
       "brzaccVLVLANTrafficPriority": brzaccVLVLANTrafficPriority,
       "brzaccVLVlanDataPriority": brzaccVLVlanDataPriority,
       "brzaccVLVlanManagementPriority": brzaccVLVlanManagementPriority,
       "brzaccVLVlanPriorityThreshold": brzaccVLVlanPriorityThreshold,
       "brzaccVLVLANQinQ": brzaccVLVLANQinQ,
       "brzaccVLQinQEthertype": brzaccVLQinQEthertype,
       "brzaccVLQinQProviderVlanID": brzaccVLQinQProviderVlanID,
       "brzaccVLVlanExtendedAccessRulesTable": brzaccVLVlanExtendedAccessRulesTable,
       "brzaccVLVlanExtendedAccessRulesEntry": brzaccVLVlanExtendedAccessRulesEntry,
       "brzaccVLVlanExtendedAccessRulesTableIdx": brzaccVLVlanExtendedAccessRulesTableIdx,
       "brzaccVLVlanExtendedAccessRuleId": brzaccVLVlanExtendedAccessRuleId,
       "brzaccVLVlanExtendedAccessRuleVlanId": brzaccVLVlanExtendedAccessRuleVlanId,
       "brzaccVLVlanExtendedAccessRulePriority": brzaccVLVlanExtendedAccessRulePriority,
       "brzaccVLVlanExtendedAccessRuleMulticastAllowed": brzaccVLVlanExtendedAccessRuleMulticastAllowed,
       "brzaccVLVlanExtendedAccessRuleOpType": brzaccVLVlanExtendedAccessRuleOpType,
       "brzaccVLVlanExtendedAccessRuleOperands": brzaccVLVlanExtendedAccessRuleOperands,
       "brzaccVLVlanExtendedTrunkVlanID": brzaccVLVlanExtendedTrunkVlanID,
       "brzaccVLBridgeAgingTime": brzaccVLBridgeAgingTime,
       "brzaccVLBroadcastRelaying": brzaccVLBroadcastRelaying,
       "brzaccVLUnicastRelaying": brzaccVLUnicastRelaying,
       "brzaccVLEthBroadcastFiltering": brzaccVLEthBroadcastFiltering,
       "brzaccVLEthBroadcastingParameters": brzaccVLEthBroadcastingParameters,
       "brzaccVLDHCPBroadcastOverrideFilter": brzaccVLDHCPBroadcastOverrideFilter,
       "brzaccVLPPPoEBroadcastOverrideFilter": brzaccVLPPPoEBroadcastOverrideFilter,
       "brzaccVLARPBroadcastOverrideFilter": brzaccVLARPBroadcastOverrideFilter,
       "brzaccVLEthBroadcastMulticastLimiterOption": brzaccVLEthBroadcastMulticastLimiterOption,
       "brzaccVLEthBroadcastMulticastLimiterThreshold": brzaccVLEthBroadcastMulticastLimiterThreshold,
       "brzaccVLEthBroadcastMulticastLimiterSendTrapInterval": brzaccVLEthBroadcastMulticastLimiterSendTrapInterval,
       "brzaccVLToSPriorityParameters": brzaccVLToSPriorityParameters,
       "brzaccVLToSPrecedenceThreshold": brzaccVLToSPrecedenceThreshold,
       "brzaccVLRoamingOption": brzaccVLRoamingOption,
       "brzaccVLMacAddressDenyList": brzaccVLMacAddressDenyList,
       "brzaccVLMacAddressDenyListTable": brzaccVLMacAddressDenyListTable,
       "brzaccVLMacAddressDenyListEntry": brzaccVLMacAddressDenyListEntry,
       "brzaccVLMacAddressDenyListTableIdx": brzaccVLMacAddressDenyListTableIdx,
       "brzaccVLMacAddressDenyListId": brzaccVLMacAddressDenyListId,
       "brzaccVLMacAddressDenyListAdd": brzaccVLMacAddressDenyListAdd,
       "brzaccVLMacAddressDenyListRemove": brzaccVLMacAddressDenyListRemove,
       "brzaccVLNumberOfMacAddressesInDenyList": brzaccVLNumberOfMacAddressesInDenyList,
       "brzaccVLMacAddressDenyListAction": brzaccVLMacAddressDenyListAction,
       "brzaccVLNewMacAddressDenyListTable": brzaccVLNewMacAddressDenyListTable,
       "brzaccVLNewMacAddressDenyListEntry": brzaccVLNewMacAddressDenyListEntry,
       "brzaccVLNewMacAddressDenyListId": brzaccVLNewMacAddressDenyListId,
       "brzaccVLNewMacAddressDenyListCommand": brzaccVLNewMacAddressDenyListCommand,
       "brzAccVLPortsControl": brzAccVLPortsControl,
       "brzaccVLEthernetPortControl": brzaccVLEthernetPortControl,
       "brzaccVLSendBroadcastsMulticastsAsUnicasts": brzaccVLSendBroadcastsMulticastsAsUnicasts,
       "brzaccVLAirInterface": brzaccVLAirInterface,
       "brzaccVLESSIDParameters": brzaccVLESSIDParameters,
       "brzaccVLESSID": brzaccVLESSID,
       "brzaccVLOperatorESSIDOption": brzaccVLOperatorESSIDOption,
       "brzaccVLOperatorESSID": brzaccVLOperatorESSID,
       "brzaccVLRunTimeESSID": brzaccVLRunTimeESSID,
       "brzaccVLHiddenESSIDParameters": brzaccVLHiddenESSIDParameters,
       "brzaccVLAUHiddenESSIDOption": brzaccVLAUHiddenESSIDOption,
       "brzaccVLSUHiddenESSIDSupport": brzaccVLSUHiddenESSIDSupport,
       "brzaccVLSUHiddenESSIDTimeout": brzaccVLSUHiddenESSIDTimeout,
       "brzaccVLMaximumCellRadius": brzaccVLMaximumCellRadius,
       "brzaccVLAIFS": brzaccVLAIFS,
       "brzaccVLWirelessTrapThreshold": brzaccVLWirelessTrapThreshold,
       "brzaccVLTransmitPowerTable": brzaccVLTransmitPowerTable,
       "brzaccVLTransmitPowerEntry": brzaccVLTransmitPowerEntry,
       "brzaccVLTransmitPowerIdx": brzaccVLTransmitPowerIdx,
       "brzaccVLApplicableModulationLevel": brzaccVLApplicableModulationLevel,
       "brzaccVLMaximumTxPowerRange": brzaccVLMaximumTxPowerRange,
       "brzaccVLTxPower": brzaccVLTxPower,
       "brzaccVLCurrentTxPower": brzaccVLCurrentTxPower,
       "brzaccVLMaximumTransmitPowerTable": brzaccVLMaximumTransmitPowerTable,
       "brzaccVLMaximumTransmitPowerEntry": brzaccVLMaximumTransmitPowerEntry,
       "brzaccVLMaximumTransmitPowerIdx": brzaccVLMaximumTransmitPowerIdx,
       "brzaccVLMaxTxApplicableModulationLevel": brzaccVLMaxTxApplicableModulationLevel,
       "brzaccVLDefinedMaximumTxPowerRange": brzaccVLDefinedMaximumTxPowerRange,
       "brzaccVLMaxTxPower": brzaccVLMaxTxPower,
       "brzaccVLMaxNumOfAssociations": brzaccVLMaxNumOfAssociations,
       "brzaccVLBestAu": brzaccVLBestAu,
       "brzaccVLBestAuSupport": brzaccVLBestAuSupport,
       "brzaccVLBestAuNoOfScanningAttempts": brzaccVLBestAuNoOfScanningAttempts,
       "brzaccVLPreferredAuMacAddress": brzaccVLPreferredAuMacAddress,
       "brzaccVLNeighborAuTable": brzaccVLNeighborAuTable,
       "brzaccVLNeighborAuEntry": brzaccVLNeighborAuEntry,
       "brzaccVLNeighborAuIdx": brzaccVLNeighborAuIdx,
       "brzaccVLNeighborAuMacAdd": brzaccVLNeighborAuMacAdd,
       "brzaccVLNeighborAuESSID": brzaccVLNeighborAuESSID,
       "brzaccVLNeighborAuSNR": brzaccVLNeighborAuSNR,
       "brzaccVLNeighborAuAssocLoadStatus": brzaccVLNeighborAuAssocLoadStatus,
       "brzaccVLNeighborAuMark": brzaccVLNeighborAuMark,
       "brzaccVLNeighborAuHwRevision": brzaccVLNeighborAuHwRevision,
       "brzaccVLNeighborAuCountryCode": brzaccVLNeighborAuCountryCode,
       "brzaccVLNeighborAuSwVer": brzaccVLNeighborAuSwVer,
       "brzaccVLNeighborAuAtpcOption": brzaccVLNeighborAuAtpcOption,
       "brzaccVLNeighborAuAdapModOption": brzaccVLNeighborAuAdapModOption,
       "brzaccVLNeighborAuBurstModeOption": brzaccVLNeighborAuBurstModeOption,
       "brzaccVLNeighborAuDfsOption": brzaccVLNeighborAuDfsOption,
       "brzaccVLNeighborAuConcatenationOption": brzaccVLNeighborAuConcatenationOption,
       "brzaccVLNeighborAuLearnCountryCodeBySU": brzaccVLNeighborAuLearnCountryCodeBySU,
       "brzaccVLNeighborAuSecurityMode": brzaccVLNeighborAuSecurityMode,
       "brzaccVLNeighborAuAuthOption": brzaccVLNeighborAuAuthOption,
       "brzaccVLNeighborAuDataEncyptOption": brzaccVLNeighborAuDataEncyptOption,
       "brzaccVLNeighborAuPerSuDistanceLearning": brzaccVLNeighborAuPerSuDistanceLearning,
       "brzaccVLNeighborAuRSSI": brzaccVLNeighborAuRSSI,
       "brzaccVLFrequencyDefinition": brzaccVLFrequencyDefinition,
       "brzaccVLSubBandLowerFrequency": brzaccVLSubBandLowerFrequency,
       "brzaccVLSubBandUpperFrequency": brzaccVLSubBandUpperFrequency,
       "brzaccVLScanningStep": brzaccVLScanningStep,
       "brzaccVLFrequencySubsetTable": brzaccVLFrequencySubsetTable,
       "brzaccVLFrequencySubsetEntry": brzaccVLFrequencySubsetEntry,
       "brzaccVLFrequencySubsetTableIdx": brzaccVLFrequencySubsetTableIdx,
       "brzaccVLFrequencySubsetFrequency": brzaccVLFrequencySubsetFrequency,
       "brzaccVLFrequencySubsetActive": brzaccVLFrequencySubsetActive,
       "brzaccVLFrequencySubsetFrequencyNew": brzaccVLFrequencySubsetFrequencyNew,
       "brzaccVLSetSelectedFreqSubset": brzaccVLSetSelectedFreqSubset,
       "brzaccVLCurrentFrequencySubsetTable": brzaccVLCurrentFrequencySubsetTable,
       "brzaccVLCurrentFrequencySubsetEntry": brzaccVLCurrentFrequencySubsetEntry,
       "brzaccVLCurrentFrequencySubsetTableIdx": brzaccVLCurrentFrequencySubsetTableIdx,
       "brzaccVLCurrentFrequencySubsetFrequency": brzaccVLCurrentFrequencySubsetFrequency,
       "brzaccVLCurrentFrequencySubsetFrequencyNew": brzaccVLCurrentFrequencySubsetFrequencyNew,
       "brzaccVLCurrentAUOperatingFrequency": brzaccVLCurrentAUOperatingFrequency,
       "brzaccVLAUDefinedFrequency": brzaccVLAUDefinedFrequency,
       "brzaccVLCurrentSUOperatingFrequency": brzaccVLCurrentSUOperatingFrequency,
       "brzaccVLSubBandSelect": brzaccVLSubBandSelect,
       "brzaccVLSelectSubBandIndex": brzaccVLSelectSubBandIndex,
       "brzaccVLDFSParameters": brzaccVLDFSParameters,
       "brzaccVLDFSOption": brzaccVLDFSOption,
       "brzaccVLDFSChannelCheckTime": brzaccVLDFSChannelCheckTime,
       "brzaccVLDFSChannelAvoidancePeriod": brzaccVLDFSChannelAvoidancePeriod,
       "brzaccVLDFSSuWaitingOption": brzaccVLDFSSuWaitingOption,
       "brzaccVLDFSClearRadarDetectedChannelsAfterReset": brzaccVLDFSClearRadarDetectedChannelsAfterReset,
       "brzaccVLDFSRadarDetectionChannelsTable": brzaccVLDFSRadarDetectionChannelsTable,
       "brzaccVLDFSRadarDetectionChannelsEntry": brzaccVLDFSRadarDetectionChannelsEntry,
       "brzaccVLDFSChannelIdx": brzaccVLDFSChannelIdx,
       "brzaccVLDFSChannelFrequency": brzaccVLDFSChannelFrequency,
       "brzaccVLDFSChannelRadarStatus": brzaccVLDFSChannelRadarStatus,
       "brzaccVLDFSChannelFrequencyNew": brzaccVLDFSChannelFrequencyNew,
       "brzaccVLDFSMinimumPulsesToDetect": brzaccVLDFSMinimumPulsesToDetect,
       "brzaccVLDFSChannelReuseParameters": brzaccVLDFSChannelReuseParameters,
       "brzaccVLDFSChannelReuseOption": brzaccVLDFSChannelReuseOption,
       "brzaccVLDFSRadarActivityAssessmentPeriod": brzaccVLDFSRadarActivityAssessmentPeriod,
       "brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod": brzaccVLDFSMaximumNumberOfDetectionsInAssessmentPeriod,
       "brzaccVLDFSDetectionAlgorithm": brzaccVLDFSDetectionAlgorithm,
       "brzaccVLDFSRemoteRadarEventReports": brzaccVLDFSRemoteRadarEventReports,
       "brzaccVLDFSRemoteRadarEventMonitoringPeriod": brzaccVLDFSRemoteRadarEventMonitoringPeriod,
       "brzaccVLEnhancedETSIRadarDetection": brzaccVLEnhancedETSIRadarDetection,
       "brzaccVLCountryCodeLearningBySU": brzaccVLCountryCodeLearningBySU,
       "brzaccVLCurrentAUOperatingFrequencyNew": brzaccVLCurrentAUOperatingFrequencyNew,
       "brzaccVLAUDefinedFrequencyNew": brzaccVLAUDefinedFrequencyNew,
       "brzaccVLAutoSubBandSelect": brzaccVLAutoSubBandSelect,
       "brzaccVLAutoSubBandSelectedFreqSubset": brzaccVLAutoSubBandSelectedFreqSubset,
       "brzaccVLAutoSubBandFrequencySubsetTable": brzaccVLAutoSubBandFrequencySubsetTable,
       "brzaccVLAutoSubBandFrequencySubsetEntry": brzaccVLAutoSubBandFrequencySubsetEntry,
       "brzaccVLAutoSubBandFrequencySubsetBandIdx": brzaccVLAutoSubBandFrequencySubsetBandIdx,
       "brzaccVLAutoSubBandFrequencySubsetFrequencyIdx": brzaccVLAutoSubBandFrequencySubsetFrequencyIdx,
       "brzaccVLAutoSubBandFrequencySubsetActive": brzaccVLAutoSubBandFrequencySubsetActive,
       "brzaccVLAutoSubBandFrequencySubsetFrequency": brzaccVLAutoSubBandFrequencySubsetFrequency,
       "brzaccVLAutoSubBandFrequencySubsetBandwidth": brzaccVLAutoSubBandFrequencySubsetBandwidth,
       "brzaccVLAutoSubBandFrequencySubsetDFSStatus": brzaccVLAutoSubBandFrequencySubsetDFSStatus,
       "brzaccVLATPC": brzaccVLATPC,
       "brzaccVLAtpcOption": brzaccVLAtpcOption,
       "brzaccVLDeltaFromMinSNRLevel": brzaccVLDeltaFromMinSNRLevel,
       "brzaccVLMinimumSNRLevel": brzaccVLMinimumSNRLevel,
       "brzaccVLMinimumIntervalBetweenATPCMessages": brzaccVLMinimumIntervalBetweenATPCMessages,
       "brzaccVLPowerLevelSteps": brzaccVLPowerLevelSteps,
       "brzaccVLAtpcOptionEZ": brzaccVLAtpcOptionEZ,
       "brzaccVLCellDistanceParameters": brzaccVLCellDistanceParameters,
       "brzaccVLCellDistanceMode": brzaccVLCellDistanceMode,
       "brzaccVLFairnessFactor": brzaccVLFairnessFactor,
       "brzaccVLMeasuredCellDistance": brzaccVLMeasuredCellDistance,
       "brzaccVLUnitWithMaxDistance": brzaccVLUnitWithMaxDistance,
       "brzaccVLPerSuDistanceLearning": brzaccVLPerSuDistanceLearning,
       "brzaccVLScanningMode": brzaccVLScanningMode,
       "brzaccVLAntennaGain": brzaccVLAntennaGain,
       "brzaccVLSpectrumAnalysisParameters": brzaccVLSpectrumAnalysisParameters,
       "brzaccVLSpectrumAnalysisChannelScanPeriod": brzaccVLSpectrumAnalysisChannelScanPeriod,
       "brzaccVLSpectrumAnalysisScanCycles": brzaccVLSpectrumAnalysisScanCycles,
       "brzaccVLAutomaticChannelSelection": brzaccVLAutomaticChannelSelection,
       "brzaccVLSpectrumAnalysisActivation": brzaccVLSpectrumAnalysisActivation,
       "brzaccVLSpectrumAnalysisStatus": brzaccVLSpectrumAnalysisStatus,
       "brzaccVLResetSpectrumCounters": brzaccVLResetSpectrumCounters,
       "brzaccVLSpectrumAnalysisInformationTable": brzaccVLSpectrumAnalysisInformationTable,
       "brzaccVLSpectrumAnalysisInformationEntry": brzaccVLSpectrumAnalysisInformationEntry,
       "brzaccVLSpectrumAnalysisInformationTableIdx": brzaccVLSpectrumAnalysisInformationTableIdx,
       "brzaccVLSpectrumAnalysisInformationChannel": brzaccVLSpectrumAnalysisInformationChannel,
       "brzaccVLSpectrumAnalysisInformationSignalCount": brzaccVLSpectrumAnalysisInformationSignalCount,
       "brzaccVLSpectrumAnalysisInformationSignalSNR": brzaccVLSpectrumAnalysisInformationSignalSNR,
       "brzaccVLSpectrumAnalysisInformationSignalWidth": brzaccVLSpectrumAnalysisInformationSignalWidth,
       "brzaccVLSpectrumAnalysisInformationOFDMFrames": brzaccVLSpectrumAnalysisInformationOFDMFrames,
       "brzaccVLSpectrumAnalysisInformationOFDMAvgSnr": brzaccVLSpectrumAnalysisInformationOFDMAvgSnr,
       "brzaccVLSpectrumAnalysisInformationAvgNoiseFloor": brzaccVLSpectrumAnalysisInformationAvgNoiseFloor,
       "brzaccVLSpectrumAnalysisInformationMaxNoiseFloor": brzaccVLSpectrumAnalysisInformationMaxNoiseFloor,
       "brzaccVLSpectrumAnalysisInformationSignalMaxSNR": brzaccVLSpectrumAnalysisInformationSignalMaxSNR,
       "brzaccVLSpectrumAnalysisInformationOFDMMaxSNR": brzaccVLSpectrumAnalysisInformationOFDMMaxSNR,
       "brzaccVLMaxNumOfAssociationsLimit": brzaccVLMaxNumOfAssociationsLimit,
       "brzaccVLDisassociate": brzaccVLDisassociate,
       "brzaccVLDisassociateAllSUs": brzaccVLDisassociateAllSUs,
       "brzaccVLDisassociateSuByMacAddress": brzaccVLDisassociateSuByMacAddress,
       "brzaccVLTxControl": brzaccVLTxControl,
       "brzaccVLLostBeaconsWatchdogThreshold": brzaccVLLostBeaconsWatchdogThreshold,
       "brzaccVLTransmitPower": brzaccVLTransmitPower,
       "brzaccVLMaximumTxPower": brzaccVLMaximumTxPower,
       "brzaccVLCountryCodeParameters": brzaccVLCountryCodeParameters,
       "brzaccVLCountryCodeReApply": brzaccVLCountryCodeReApply,
       "brzaccVLCountryCodeTable": brzaccVLCountryCodeTable,
       "brzaccVLCountryCodeEntry": brzaccVLCountryCodeEntry,
       "brzaccVLCCNumber": brzaccVLCCNumber,
       "brzaccVLCCName": brzaccVLCCName,
       "brzaccVLCCAuthenticationEncryptionSupport": brzaccVLCCAuthenticationEncryptionSupport,
       "brzaccVLCCDataEncryptionSupport": brzaccVLCCDataEncryptionSupport,
       "brzaccVLCCAESEncryptionSupport": brzaccVLCCAESEncryptionSupport,
       "brzaccVLCCParamsTable": brzaccVLCCParamsTable,
       "brzaccVLCCParamsEntry": brzaccVLCCParamsEntry,
       "brzaccVLCCNumberIdx": brzaccVLCCNumberIdx,
       "brzaccVLCCParamsIndex": brzaccVLCCParamsIndex,
       "brzaccVLCCParamsFrequencies": brzaccVLCCParamsFrequencies,
       "brzaccVLCCAllowedBandwidth": brzaccVLCCAllowedBandwidth,
       "brzaccVLCCRegulationMaxTxPowerAtAntennaPort": brzaccVLCCRegulationMaxTxPowerAtAntennaPort,
       "brzaccVLCCRegulationMaxEIRP": brzaccVLCCRegulationMaxEIRP,
       "brzaccVLCCMinModulationLevel": brzaccVLCCMinModulationLevel,
       "brzaccVLCCMaxModulationLevel": brzaccVLCCMaxModulationLevel,
       "brzaccVLCCBurstModeSupport": brzaccVLCCBurstModeSupport,
       "brzaccVLCCMaximumBurstDuration": brzaccVLCCMaximumBurstDuration,
       "brzaccVLCCDfsSupport": brzaccVLCCDfsSupport,
       "brzaccVLCCMinimumHwRevision": brzaccVLCCMinimumHwRevision,
       "brzaccVLCountryCodeSelect": brzaccVLCountryCodeSelect,
       "brzaccVLNoiseImmunityParameters": brzaccVLNoiseImmunityParameters,
       "brzaccVLNoiseImmunityAlgorithm": brzaccVLNoiseImmunityAlgorithm,
       "brzaccVLNoiseImmunityLevel": brzaccVLNoiseImmunityLevel,
       "brzaccVLSpuriousImmunityLevel": brzaccVLSpuriousImmunityLevel,
       "brzaccVLOFDMWeakSignal": brzaccVLOFDMWeakSignal,
       "brzaccVLPulseDetectionSensitivity": brzaccVLPulseDetectionSensitivity,
       "brzaccVLNewTransmitPowerTable": brzaccVLNewTransmitPowerTable,
       "brzaccVLNewTransmitPowerEntry": brzaccVLNewTransmitPowerEntry,
       "brzaccVLNewModulationLevelIdx": brzaccVLNewModulationLevelIdx,
       "brzaccVLNewMaximumTxPowerRange": brzaccVLNewMaximumTxPowerRange,
       "brzaccVLNewTxPower": brzaccVLNewTxPower,
       "brzaccVLNewCurrentTxPower": brzaccVLNewCurrentTxPower,
       "brzaccVLNewMaximumTransmitPowerTable": brzaccVLNewMaximumTransmitPowerTable,
       "brzaccVLNewMaximumTransmitPowerEntry": brzaccVLNewMaximumTransmitPowerEntry,
       "brzaccVLNewMaxModulationLevelIdx": brzaccVLNewMaxModulationLevelIdx,
       "brzaccVLNewDefinedMaximumTxPowerRange": brzaccVLNewDefinedMaximumTxPowerRange,
       "brzaccVLNewMaxTxPower": brzaccVLNewMaxTxPower,
       "brzaccVLNoiseFloorCalculationParameters": brzaccVLNoiseFloorCalculationParameters,
       "brzaccVLNoiseFloorCalculationMode": brzaccVLNoiseFloorCalculationMode,
       "brzaccVLNoiseFloorForcedValue": brzaccVLNoiseFloorForcedValue,
       "brzaccVLNoiseFloorCalibrationParameters": brzaccVLNoiseFloorCalibrationParameters,
       "brzaccVLNoiseFloorRunCalibration": brzaccVLNoiseFloorRunCalibration,
       "brzaccVLNoiseFloorFieldCalibrationStatus": brzaccVLNoiseFloorFieldCalibrationStatus,
       "brzaccVLNoiseFloorLastFieldCalibrationResult": brzaccVLNoiseFloorLastFieldCalibrationResult,
       "brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration": brzaccVLNoiseFloorBandwidthUsedForLastFieldCalibration,
       "brzaccVLNoiseFloorAvailableCalibrationOptions": brzaccVLNoiseFloorAvailableCalibrationOptions,
       "brzaccVLNoiseFloorUseCalibration": brzaccVLNoiseFloorUseCalibration,
       "brzaccVLInterferenceMitigationParameters": brzaccVLInterferenceMitigationParameters,
       "brzaccVLInterferenceMitigationChannelScanPeriod": brzaccVLInterferenceMitigationChannelScanPeriod,
       "brzaccVLInterferenceMitigationAutomaticScanPeriod": brzaccVLInterferenceMitigationAutomaticScanPeriod,
       "brzaccVLInterferenceMitigationScanType": brzaccVLInterferenceMitigationScanType,
       "brzaccVLInterferenceMitigationScanMode": brzaccVLInterferenceMitigationScanMode,
       "brzaccVLInterferenceMitigationDistance": brzaccVLInterferenceMitigationDistance,
       "brzaccVLInterferenceMitigationThroughput": brzaccVLInterferenceMitigationThroughput,
       "brzaccVLInterferenceMitigationActivation": brzaccVLInterferenceMitigationActivation,
       "brzaccVLInterferenceMitigationStatus": brzaccVLInterferenceMitigationStatus,
       "brzaccVLInterferenceMitigationDeleteStatisticsFile": brzaccVLInterferenceMitigationDeleteStatisticsFile,
       "brzaccVLInterferenceMitigationModel": brzaccVLInterferenceMitigationModel,
       "brzaccVLInterferenceMitigationScanTime": brzaccVLInterferenceMitigationScanTime,
       "brzaccVLInterferenceMitigationAUheight": brzaccVLInterferenceMitigationAUheight,
       "brzaccVLInterferenceMitigationAntennaGain": brzaccVLInterferenceMitigationAntennaGain,
       "brzaccVLInterferenceMitigationMaxModulation": brzaccVLInterferenceMitigationMaxModulation,
       "brzaccVLInterferenceMitigationKeepLink": brzaccVLInterferenceMitigationKeepLink,
       "brzaccVLInterferenceMitigationOutputTable": brzaccVLInterferenceMitigationOutputTable,
       "brzaccVLInterferenceMitigationOutputEntry": brzaccVLInterferenceMitigationOutputEntry,
       "brzaccVLInterferenceMitigationOutputFrequency": brzaccVLInterferenceMitigationOutputFrequency,
       "brzaccVLInterferenceMitigationOutputScanningType": brzaccVLInterferenceMitigationOutputScanningType,
       "brzaccVLInterferenceMitigationOutputInstallationModel": brzaccVLInterferenceMitigationOutputInstallationModel,
       "brzaccVLInterferenceMitigationOutputNoiseFloor": brzaccVLInterferenceMitigationOutputNoiseFloor,
       "brzaccVLInterferenceMitigationOutputDistance": brzaccVLInterferenceMitigationOutputDistance,
       "brzaccVLInterferenceMitigationOutputPerformance": brzaccVLInterferenceMitigationOutputPerformance,
       "brzaccVLBeaconPeriod": brzaccVLBeaconPeriod,
       "brzaccVLMaxBeaconsLost": brzaccVLMaxBeaconsLost,
       "brzaccVLServiceParameters": brzaccVLServiceParameters,
       "brzaccVLMirDownlink": brzaccVLMirDownlink,
       "brzaccVLMirUplink": brzaccVLMirUplink,
       "brzaccVLCirDownlink": brzaccVLCirDownlink,
       "brzaccVLCirUplink": brzaccVLCirUplink,
       "brzaccVLMaxDelay": brzaccVLMaxDelay,
       "brzaccVLMaxBurstDuration": brzaccVLMaxBurstDuration,
       "brzaccVLGracefulDegradationLimit": brzaccVLGracefulDegradationLimit,
       "brzaccVLMirOnlyOption": brzaccVLMirOnlyOption,
       "brzaccVLTrafficPrioritization": brzaccVLTrafficPrioritization,
       "brzaccVLTrafficPriVLAN": brzaccVLTrafficPriVLAN,
       "brzaccVLVLANPriorityThreshold": brzaccVLVLANPriorityThreshold,
       "brzaccVLTrafficPriIPToS": brzaccVLTrafficPriIPToS,
       "brzaccVLToSPrioritizationOption": brzaccVLToSPrioritizationOption,
       "brzaccVLIPPrecedenceThreshold": brzaccVLIPPrecedenceThreshold,
       "brzaccVLIPDSCPThreshold": brzaccVLIPDSCPThreshold,
       "brzaccVLTrafficPriUdpTcpPortRange": brzaccVLTrafficPriUdpTcpPortRange,
       "brzaccVLUdpTcpPortRangePrioritizationOption": brzaccVLUdpTcpPortRangePrioritizationOption,
       "brzaccVLUdpPortRangeConfig": brzaccVLUdpPortRangeConfig,
       "brzaccVLUdpPortPriRTPRTCP": brzaccVLUdpPortPriRTPRTCP,
       "brzaccVLUdpPortRangeNum": brzaccVLUdpPortRangeNum,
       "brzaccVLUdpPortRangeTable": brzaccVLUdpPortRangeTable,
       "brzaccVLUdpPortRangeEntry": brzaccVLUdpPortRangeEntry,
       "brzaccVLUdpPortRangeStart": brzaccVLUdpPortRangeStart,
       "brzaccVLUdpPortRangeEnd": brzaccVLUdpPortRangeEnd,
       "brzaccVLUdpPortRangeIdx": brzaccVLUdpPortRangeIdx,
       "brzaccVLUdpPortRangeAdd": brzaccVLUdpPortRangeAdd,
       "brzaccVLUdpPortRangeDelete": brzaccVLUdpPortRangeDelete,
       "brzaccVLUdpPortRangeDeleteAll": brzaccVLUdpPortRangeDeleteAll,
       "brzaccVLTcpPortRangeConfig": brzaccVLTcpPortRangeConfig,
       "brzaccVLTcpPortPriRTPRTCP": brzaccVLTcpPortPriRTPRTCP,
       "brzaccVLTcpPortRangeNum": brzaccVLTcpPortRangeNum,
       "brzaccVLTcpPortRangeTable": brzaccVLTcpPortRangeTable,
       "brzaccVLTcpPortRangeEntry": brzaccVLTcpPortRangeEntry,
       "brzaccVLTcpPortRangeStart": brzaccVLTcpPortRangeStart,
       "brzaccVLTcpPortRangeEnd": brzaccVLTcpPortRangeEnd,
       "brzaccVLTcpPortRangeIdx": brzaccVLTcpPortRangeIdx,
       "brzaccVLTcpPortRangeAdd": brzaccVLTcpPortRangeAdd,
       "brzaccVLTcpPortRangeDelete": brzaccVLTcpPortRangeDelete,
       "brzaccVLTcpPortRangeDeleteAll": brzaccVLTcpPortRangeDeleteAll,
       "brzaccVLWirelessLinkPrioritization": brzaccVLWirelessLinkPrioritization,
       "brzaccVLWirelessLinkPrioritizationOption": brzaccVLWirelessLinkPrioritizationOption,
       "brzaccVLlowPriorityAIFS": brzaccVLlowPriorityAIFS,
       "brzaccVLHWRetriesHighPriority": brzaccVLHWRetriesHighPriority,
       "brzaccVLHWRetriesLowPriority": brzaccVLHWRetriesLowPriority,
       "brzaccVLAUBurstDurationHighPriority": brzaccVLAUBurstDurationHighPriority,
       "brzaccVLAUBurstDurationLowPriority": brzaccVLAUBurstDurationLowPriority,
       "brzaccVLSUBurstDurationHighPriority": brzaccVLSUBurstDurationHighPriority,
       "brzaccVLSUBurstDurationLowPriority": brzaccVLSUBurstDurationLowPriority,
       "brzaccVLTrafficPriIpRange": brzaccVLTrafficPriIpRange,
       "brzaccVLTrafficPriIpRangeOption": brzaccVLTrafficPriIpRangeOption,
       "brzaccVLTrafficPriIpRangeIpAddress": brzaccVLTrafficPriIpRangeIpAddress,
       "brzaccVLTrafficPriIpRangeIpMask": brzaccVLTrafficPriIpRangeIpMask,
       "brzaccVLDrap": brzaccVLDrap,
       "brzaccVLDrapSupport": brzaccVLDrapSupport,
       "brzaccVLDrapUdpPort": brzaccVLDrapUdpPort,
       "brzaccVLDrapMaxNumberOfVoiceCalls": brzaccVLDrapMaxNumberOfVoiceCalls,
       "brzaccVLDrapTTL": brzaccVLDrapTTL,
       "brzaccVLDrapNoOfActiveVoiceCalls": brzaccVLDrapNoOfActiveVoiceCalls,
       "brzaccVLLowPriorityTrafficMinimumPercent": brzaccVLLowPriorityTrafficMinimumPercent,
       "brzaccVLSUEZMirDownlink": brzaccVLSUEZMirDownlink,
       "brzaccVLMIRThresholdPercent": brzaccVLMIRThresholdPercent,
       "brzaccVLProportionalIRParameters": brzaccVLProportionalIRParameters,
       "brzaccVLProportionalIRFactor": brzaccVLProportionalIRFactor,
       "brzaccVLProportionalIRUpdatePeriod": brzaccVLProportionalIRUpdatePeriod,
       "brzaccVLProportionalIRThresholdPercentage": brzaccVLProportionalIRThresholdPercentage,
       "brzaccVLProportionalIRThresholdRate": brzaccVLProportionalIRThresholdRate,
       "brzaccVLUserFilterParams": brzaccVLUserFilterParams,
       "brzaccVLUserFilterOption": brzaccVLUserFilterOption,
       "brzaccVLIpFilterTable": brzaccVLIpFilterTable,
       "brzaccVLIpFilterEntry": brzaccVLIpFilterEntry,
       "brzaccVLIpID": brzaccVLIpID,
       "brzaccVLMaskID": brzaccVLMaskID,
       "brzaccVLIpFilterRange": brzaccVLIpFilterRange,
       "brzaccVLIpFilterIdx": brzaccVLIpFilterIdx,
       "brzaccVLDeleteOneUserFilter": brzaccVLDeleteOneUserFilter,
       "brzaccVLDeleteAllUserFilters": brzaccVLDeleteAllUserFilters,
       "brzaccVLDHCPUnicastOverrideFilter": brzaccVLDHCPUnicastOverrideFilter,
       "brzaccVLNewIpFilterTable": brzaccVLNewIpFilterTable,
       "brzaccVLNewIpFilterEntry": brzaccVLNewIpFilterEntry,
       "brzaccVLNewIpID": brzaccVLNewIpID,
       "brzaccVLNewMaskID": brzaccVLNewMaskID,
       "brzaccVLNewIpFilterRange": brzaccVLNewIpFilterRange,
       "brzaccVLNewIpFilterCommand": brzaccVLNewIpFilterCommand,
       "brzaccVLDHCPPPPoEOverrideFilter": brzaccVLDHCPPPPoEOverrideFilter,
       "brzaccVLSecurityParameters": brzaccVLSecurityParameters,
       "brzaccVLAuthenticationAlgorithm": brzaccVLAuthenticationAlgorithm,
       "brzaccVLSUDefaultKeyID": brzaccVLSUDefaultKeyID,
       "brzaccVLDataEncryptionOption": brzaccVLDataEncryptionOption,
       "brzaccVLAUDefaultMulticastKeyID": brzaccVLAUDefaultMulticastKeyID,
       "brzaccVLSecurityMode": brzaccVLSecurityMode,
       "brzaccVLAuthenticationPromiscuousMode": brzaccVLAuthenticationPromiscuousMode,
       "brzaccVLKey1": brzaccVLKey1,
       "brzaccVLKey2": brzaccVLKey2,
       "brzaccVLKey3": brzaccVLKey3,
       "brzaccVLKey4": brzaccVLKey4,
       "brzaccVLSecurityModeSupport": brzaccVLSecurityModeSupport,
       "brzaccVLPerformanceParams": brzaccVLPerformanceParams,
       "brzaccVLRTSThreshold": brzaccVLRTSThreshold,
       "brzaccVLMinContentionWindow": brzaccVLMinContentionWindow,
       "brzaccVLMaxContentionWindow": brzaccVLMaxContentionWindow,
       "brzaccVLMaximumModulationLevel": brzaccVLMaximumModulationLevel,
       "brzaccVLMulticastModulationLevel": brzaccVLMulticastModulationLevel,
       "brzaccVLAvgSNRMemoryFactor": brzaccVLAvgSNRMemoryFactor,
       "brzaccVLHardwareRetries": brzaccVLHardwareRetries,
       "brzaccVLAdaptiveModulationParams": brzaccVLAdaptiveModulationParams,
       "brzaccVLAdaptiveModulationAlgorithmOption": brzaccVLAdaptiveModulationAlgorithmOption,
       "brzaccVLSoftwareRetrySupport": brzaccVLSoftwareRetrySupport,
       "brzaccVLNumOfSoftwareRetries": brzaccVLNumOfSoftwareRetries,
       "brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages": brzaccVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages,
       "brzaccVLAdaptiveModulationDecisionThresholds": brzaccVLAdaptiveModulationDecisionThresholds,
       "brzaccVLAdaptiveModulationHistorySize": brzaccVLAdaptiveModulationHistorySize,
       "brzaccVLAdaptiveModulationPacketThresholdToTestUpRate": brzaccVLAdaptiveModulationPacketThresholdToTestUpRate,
       "brzaccVLAdaptiveModulationPacketNoOnUpperRate": brzaccVLAdaptiveModulationPacketNoOnUpperRate,
       "brzaccVLAdaptiveModulationAlgorithm": brzaccVLAdaptiveModulationAlgorithm,
       "brzaccVLAdaptiveModulationRetriesOnLowerModulations": brzaccVLAdaptiveModulationRetriesOnLowerModulations,
       "brzaccVLAdaptiveModulationRTSDurationMode": brzaccVLAdaptiveModulationRTSDurationMode,
       "brzaccVLBurstMode": brzaccVLBurstMode,
       "brzaccVLBurstModeOption": brzaccVLBurstModeOption,
       "brzaccVLBurstInterval": brzaccVLBurstInterval,
       "brzaccVLConcatenationParameters": brzaccVLConcatenationParameters,
       "brzaccVLConcatenationOption": brzaccVLConcatenationOption,
       "brzaccVLConcatenationMaximumNumberOfFrames": brzaccVLConcatenationMaximumNumberOfFrames,
       "brzaccVLConcatenationMaxFrameSize": brzaccVLConcatenationMaxFrameSize,
       "brzaccVLControlModulationLevel": brzaccVLControlModulationLevel,
       "brzaccVLEthernetFrameSize": brzaccVLEthernetFrameSize,
       "brzaccVLRunningEthernetFrameSize": brzaccVLRunningEthernetFrameSize,
       "brzaccVLSiteSurvey": brzaccVLSiteSurvey,
       "brzaccVLAverageReceiveSNR": brzaccVLAverageReceiveSNR,
       "brzaccVLTrafficStatistics": brzaccVLTrafficStatistics,
       "brzaccVLResetTrafficCounters": brzaccVLResetTrafficCounters,
       "brzaccVLEthCounters": brzaccVLEthCounters,
       "brzaccVLTotalRxFramesViaEthernet": brzaccVLTotalRxFramesViaEthernet,
       "brzaccVLTxWirelessToEthernet": brzaccVLTxWirelessToEthernet,
       "brzaccVLWirelessLinkCounters": brzaccVLWirelessLinkCounters,
       "brzaccVLTxFramesToWireless": brzaccVLTxFramesToWireless,
       "brzaccVLAUBeaconsToWireless": brzaccVLAUBeaconsToWireless,
       "brzaccVLDataAndOtherMngFramesToWireless": brzaccVLDataAndOtherMngFramesToWireless,
       "brzaccVLTotalTxFramesToWireless": brzaccVLTotalTxFramesToWireless,
       "brzaccVLTotalTransmittedUnicasts": brzaccVLTotalTransmittedUnicasts,
       "brzaccVLTotalTransmittedConcatenatedFramesDouble": brzaccVLTotalTransmittedConcatenatedFramesDouble,
       "brzaccVLTotalTransmittedConcatenatedFramesSingle": brzaccVLTotalTransmittedConcatenatedFramesSingle,
       "brzaccVLTotalTransmittedConcatenatedFramesMore": brzaccVLTotalTransmittedConcatenatedFramesMore,
       "brzaccVLTotalRxFramesFromWireless": brzaccVLTotalRxFramesFromWireless,
       "brzaccVLTotalRetransmittedFrames": brzaccVLTotalRetransmittedFrames,
       "brzaccVLFramesDropped": brzaccVLFramesDropped,
       "brzaccVLDataFramesSubmittedToBridge": brzaccVLDataFramesSubmittedToBridge,
       "brzaccVLFramesSubmittedViaHighQueue": brzaccVLFramesSubmittedViaHighQueue,
       "brzaccVLFramesSubmittedViaMidQueue": brzaccVLFramesSubmittedViaMidQueue,
       "brzaccVLFramesSubmittedViaLowQueue": brzaccVLFramesSubmittedViaLowQueue,
       "brzaccVLTotalNoOfDataFramesSubmitted": brzaccVLTotalNoOfDataFramesSubmitted,
       "brzaccVLTotalRecievedDataFrames": brzaccVLTotalRecievedDataFrames,
       "brzaccVLRecievedBadFrames": brzaccVLRecievedBadFrames,
       "brzaccVLNoOfDuplicateFramesDiscarded": brzaccVLNoOfDuplicateFramesDiscarded,
       "brzaccVLNoOfInternallyDiscardedMirCir": brzaccVLNoOfInternallyDiscardedMirCir,
       "brzaccVLTotalRxConcatenatedFramesDouble": brzaccVLTotalRxConcatenatedFramesDouble,
       "brzaccVLTotalRxConcatenatedFramesSingle": brzaccVLTotalRxConcatenatedFramesSingle,
       "brzaccVLTotalRxConcatenatedFramesMore": brzaccVLTotalRxConcatenatedFramesMore,
       "brzaccVLTXRetransmissionPercentage": brzaccVLTXRetransmissionPercentage,
       "brzaccVLRXCRCPercentage": brzaccVLRXCRCPercentage,
       "brzaccVLWirelessLinkEvents": brzaccVLWirelessLinkEvents,
       "brzaccVLTxEvents": brzaccVLTxEvents,
       "brzaccVLDroppedFrameEvents": brzaccVLDroppedFrameEvents,
       "brzaccVLFramesDelayedDueToSwRetry": brzaccVLFramesDelayedDueToSwRetry,
       "brzaccVLUnderrunEvents": brzaccVLUnderrunEvents,
       "brzaccVLOthersTxEvents": brzaccVLOthersTxEvents,
       "brzaccVLTotalTxEvents": brzaccVLTotalTxEvents,
       "brzaccVLRxEvents": brzaccVLRxEvents,
       "brzaccVLPhyErrors": brzaccVLPhyErrors,
       "brzaccVLCRCErrors": brzaccVLCRCErrors,
       "brzaccVLOverrunEvents": brzaccVLOverrunEvents,
       "brzaccVLRxDecryptEvents": brzaccVLRxDecryptEvents,
       "brzaccVLTotalRxEvents": brzaccVLTotalRxEvents,
       "brzaccVLPerModulationLevelCounters": brzaccVLPerModulationLevelCounters,
       "brzaccVLResetPerModulationLevelCounters": brzaccVLResetPerModulationLevelCounters,
       "brzaccVLSUPerModulationLevelCountersTable": brzaccVLSUPerModulationLevelCountersTable,
       "brzaccVLSUPerModulationLevelCountersEntry": brzaccVLSUPerModulationLevelCountersEntry,
       "brzaccVLSUPerModulationLevelCountersTableIdx": brzaccVLSUPerModulationLevelCountersTableIdx,
       "brzaccVLSUPerModulationLevelCountersApplicableModLevel": brzaccVLSUPerModulationLevelCountersApplicableModLevel,
       "brzaccVLSUPerModulationLevelCountersTxSuccess": brzaccVLSUPerModulationLevelCountersTxSuccess,
       "brzaccVLSUPerModulationLevelCountersTxFailed": brzaccVLSUPerModulationLevelCountersTxFailed,
       "brzaccVLAverageModulationLevel": brzaccVLAverageModulationLevel,
       "brzaccVLMacAddressDatabase": brzaccVLMacAddressDatabase,
       "brzaccVLAUMacAddressDatabase": brzaccVLAUMacAddressDatabase,
       "brzaccVLAUAdbResetAllModulationLevelCounters": brzaccVLAUAdbResetAllModulationLevelCounters,
       "brzaccVLAUAdbTable": brzaccVLAUAdbTable,
       "brzaccVLAUAdbEntry": brzaccVLAUAdbEntry,
       "brzaccVLAdbIndex": brzaccVLAdbIndex,
       "brzaccVLAdbMacAddress": brzaccVLAdbMacAddress,
       "brzaccVLAdbStatus": brzaccVLAdbStatus,
       "brzaccVLAdbSwVersion": brzaccVLAdbSwVersion,
       "brzaccVLAdbSNR": brzaccVLAdbSNR,
       "brzaccVLAdbMaxModulationLevel": brzaccVLAdbMaxModulationLevel,
       "brzaccVLAdbTxFramesTotal": brzaccVLAdbTxFramesTotal,
       "brzaccVLAdbDroppedFramesTotal": brzaccVLAdbDroppedFramesTotal,
       "brzaccVLAdbTxSuccessModLevel1": brzaccVLAdbTxSuccessModLevel1,
       "brzaccVLAdbTxSuccessModLevel2": brzaccVLAdbTxSuccessModLevel2,
       "brzaccVLAdbTxSuccessModLevel3": brzaccVLAdbTxSuccessModLevel3,
       "brzaccVLAdbTxSuccessModLevel4": brzaccVLAdbTxSuccessModLevel4,
       "brzaccVLAdbTxSuccessModLevel5": brzaccVLAdbTxSuccessModLevel5,
       "brzaccVLAdbTxSuccessModLevel6": brzaccVLAdbTxSuccessModLevel6,
       "brzaccVLAdbTxSuccessModLevel7": brzaccVLAdbTxSuccessModLevel7,
       "brzaccVLAdbTxSuccessModLevel8": brzaccVLAdbTxSuccessModLevel8,
       "brzaccVLAdbTxFailedModLevel1": brzaccVLAdbTxFailedModLevel1,
       "brzaccVLAdbTxFailedModLevel2": brzaccVLAdbTxFailedModLevel2,
       "brzaccVLAdbTxFailedModLevel3": brzaccVLAdbTxFailedModLevel3,
       "brzaccVLAdbTxFailedModLevel4": brzaccVLAdbTxFailedModLevel4,
       "brzaccVLAdbTxFailedModLevel5": brzaccVLAdbTxFailedModLevel5,
       "brzaccVLAdbTxFailedModLevel6": brzaccVLAdbTxFailedModLevel6,
       "brzaccVLAdbTxFailedModLevel7": brzaccVLAdbTxFailedModLevel7,
       "brzaccVLAdbTxFailedModLevel8": brzaccVLAdbTxFailedModLevel8,
       "brzaccVLAdbCirTx": brzaccVLAdbCirTx,
       "brzaccVLAdbMirTx": brzaccVLAdbMirTx,
       "brzaccVLAdbCirRx": brzaccVLAdbCirRx,
       "brzaccVLAdbMirRx": brzaccVLAdbMirRx,
       "brzaccVLAdbCirMaxDelay": brzaccVLAdbCirMaxDelay,
       "brzaccVLAdbDistance": brzaccVLAdbDistance,
       "brzaccVLAdbHwRevision": brzaccVLAdbHwRevision,
       "brzaccVLAdbCpldVer": brzaccVLAdbCpldVer,
       "brzaccVLAdbCountryCode": brzaccVLAdbCountryCode,
       "brzaccVLAdbBootVer": brzaccVLAdbBootVer,
       "brzaccVLAdbAtpcOption": brzaccVLAdbAtpcOption,
       "brzaccVLAdbAdapModOption": brzaccVLAdbAdapModOption,
       "brzaccVLAdbBurstModeOption": brzaccVLAdbBurstModeOption,
       "brzaccVLAdbConcatenationOption": brzaccVLAdbConcatenationOption,
       "brzaccVLAdbSecurityMode": brzaccVLAdbSecurityMode,
       "brzaccVLAdbAuthOption": brzaccVLAdbAuthOption,
       "brzaccVLAdbDataEncyptOption": brzaccVLAdbDataEncyptOption,
       "brzaccVLAdbAge": brzaccVLAdbAge,
       "brzaccVLAdbUnitName": brzaccVLAdbUnitName,
       "brzaccVLAdbRSSI": brzaccVLAdbRSSI,
       "brzaccVLAdbIpAddress": brzaccVLAdbIpAddress,
       "brzaccVLAUNewAdbTable": brzaccVLAUNewAdbTable,
       "brzaccVLAUNewAdbEntry": brzaccVLAUNewAdbEntry,
       "brzaccVLNewAdbMacAddress": brzaccVLNewAdbMacAddress,
       "brzaccVLNewAdbIPaddress": brzaccVLNewAdbIPaddress,
       "brzaccVLNewAdbUnitName": brzaccVLNewAdbUnitName,
       "brzaccVLNewAdbUnitType": brzaccVLNewAdbUnitType,
       "brzaccVLNewAdbSwVersion": brzaccVLNewAdbSwVersion,
       "brzaccVLNewAdbHwRevision": brzaccVLNewAdbHwRevision,
       "brzaccVLNewAdbCpldVer": brzaccVLNewAdbCpldVer,
       "brzaccVLNewAdbBootVer": brzaccVLNewAdbBootVer,
       "brzaccVLNewAdbCountryCode": brzaccVLNewAdbCountryCode,
       "brzaccVLNewAdbCirTx": brzaccVLNewAdbCirTx,
       "brzaccVLNewAdbMirTx": brzaccVLNewAdbMirTx,
       "brzaccVLNewAdbCirRx": brzaccVLNewAdbCirRx,
       "brzaccVLNewAdbMirRx": brzaccVLNewAdbMirRx,
       "brzaccVLNewAdbCirMaxDelay": brzaccVLNewAdbCirMaxDelay,
       "brzaccVLNewAdbAtpcOption": brzaccVLNewAdbAtpcOption,
       "brzaccVLNewAdbAdapModOption": brzaccVLNewAdbAdapModOption,
       "brzaccVLNewAdbBurstModeOption": brzaccVLNewAdbBurstModeOption,
       "brzaccVLNewAdbConcatenationOption": brzaccVLNewAdbConcatenationOption,
       "brzaccVLNewAdbSecurityMode": brzaccVLNewAdbSecurityMode,
       "brzaccVLNewAdbAuthOption": brzaccVLNewAdbAuthOption,
       "brzaccVLNewAdbDataEncyptOption": brzaccVLNewAdbDataEncyptOption,
       "brzaccVLAdbWi2IPaddress": brzaccVLAdbWi2IPaddress,
       "brzaccVLNewAdbStatus": brzaccVLNewAdbStatus,
       "brzaccVLNewAdbAge": brzaccVLNewAdbAge,
       "brzaccVLNewAdbDistance": brzaccVLNewAdbDistance,
       "brzaccVLNewAdbSNR": brzaccVLNewAdbSNR,
       "brzaccVLNewAdbMaxModulationLevel": brzaccVLNewAdbMaxModulationLevel,
       "brzaccVLNewAdbTxFramesTotal": brzaccVLNewAdbTxFramesTotal,
       "brzaccVLNewAdbDroppedFramesTotal": brzaccVLNewAdbDroppedFramesTotal,
       "brzaccVLNewAdbTxSuccessModLevel1": brzaccVLNewAdbTxSuccessModLevel1,
       "brzaccVLNewAdbTxSuccessModLevel2": brzaccVLNewAdbTxSuccessModLevel2,
       "brzaccVLNewAdbTxSuccessModLevel3": brzaccVLNewAdbTxSuccessModLevel3,
       "brzaccVLNewAdbTxSuccessModLevel4": brzaccVLNewAdbTxSuccessModLevel4,
       "brzaccVLNewAdbTxSuccessModLevel5": brzaccVLNewAdbTxSuccessModLevel5,
       "brzaccVLNewAdbTxSuccessModLevel6": brzaccVLNewAdbTxSuccessModLevel6,
       "brzaccVLNewAdbTxSuccessModLevel7": brzaccVLNewAdbTxSuccessModLevel7,
       "brzaccVLNewAdbTxSuccessModLevel8": brzaccVLNewAdbTxSuccessModLevel8,
       "brzaccVLNewAdbTxFailedModLevel1": brzaccVLNewAdbTxFailedModLevel1,
       "brzaccVLNewAdbTxFailedModLevel2": brzaccVLNewAdbTxFailedModLevel2,
       "brzaccVLNewAdbTxFailedModLevel3": brzaccVLNewAdbTxFailedModLevel3,
       "brzaccVLNewAdbTxFailedModLevel4": brzaccVLNewAdbTxFailedModLevel4,
       "brzaccVLNewAdbTxFailedModLevel5": brzaccVLNewAdbTxFailedModLevel5,
       "brzaccVLNewAdbTxFailedModLevel6": brzaccVLNewAdbTxFailedModLevel6,
       "brzaccVLNewAdbTxFailedModLevel7": brzaccVLNewAdbTxFailedModLevel7,
       "brzaccVLNewAdbTxFailedModLevel8": brzaccVLNewAdbTxFailedModLevel8,
       "brzaccVLNewAdbMainSwVersion": brzaccVLNewAdbMainSwVersion,
       "brzaccVLNewAdbShadowSwVersion": brzaccVLNewAdbShadowSwVersion,
       "brzaccVLNewAdbReadOnlyCommunity": brzaccVLNewAdbReadOnlyCommunity,
       "brzaccVLNewAdbWriteCommunity": brzaccVLNewAdbWriteCommunity,
       "brzaccVLNewAdbAIFS": brzaccVLNewAdbAIFS,
       "brzaccVLNewAdbMinimumCW": brzaccVLNewAdbMinimumCW,
       "brzaccVLNewAdbMaximumCW": brzaccVLNewAdbMaximumCW,
       "brzaccVLNewAdbESSID": brzaccVLNewAdbESSID,
       "brzaccVLNewAdbRSSI": brzaccVLNewAdbRSSI,
       "brzaccVLNewAdbDfsOption": brzaccVLNewAdbDfsOption,
       "brzaccVLAggregateMIRCIR": brzaccVLAggregateMIRCIR,
       "brzaccVLAggregateMIRUplink": brzaccVLAggregateMIRUplink,
       "brzaccVLAggregateMIRDownlink": brzaccVLAggregateMIRDownlink,
       "brzaccVLAggregateCIRUplink": brzaccVLAggregateCIRUplink,
       "brzaccVLAggregateCIRDownlink": brzaccVLAggregateCIRDownlink,
       "brzaccVLUpLinkQualityIndicator": brzaccVLUpLinkQualityIndicator,
       "brzaccVLMeasureUpLinkQualityIndicator": brzaccVLMeasureUpLinkQualityIndicator,
       "brzaccVLReadUpLinkQualityIndicator": brzaccVLReadUpLinkQualityIndicator,
       "brzaccVLUpLinkQualityIndicatorStatus": brzaccVLUpLinkQualityIndicatorStatus,
       "brzaccVLMacPinpoint": brzaccVLMacPinpoint,
       "brzaccVLMacPinpointTable": brzaccVLMacPinpointTable,
       "brzaccVLMacPinpointEntry": brzaccVLMacPinpointEntry,
       "mptEthernetStationMACAddress": mptEthernetStationMACAddress,
       "mptUnitMACAddress": mptUnitMACAddress,
       "brzaccVLDrapGatewaysTable": brzaccVLDrapGatewaysTable,
       "brzaccVLDrapGatewayEntry": brzaccVLDrapGatewayEntry,
       "brzaccVLDrapGatewayIndex": brzaccVLDrapGatewayIndex,
       "brzaccVLDrapGatewayIP": brzaccVLDrapGatewayIP,
       "brzaccVLDrapGatewayType": brzaccVLDrapGatewayType,
       "brzaccVLDrapGatewayNoOfActiveVoiceCalls": brzaccVLDrapGatewayNoOfActiveVoiceCalls,
       "brzaccVLHiddenESSIDTable": brzaccVLHiddenESSIDTable,
       "brzaccVLHiddenESSIDEntry": brzaccVLHiddenESSIDEntry,
       "brzaccVLHiddenESSIDMacAddress": brzaccVLHiddenESSIDMacAddress,
       "brzaccVLHiddenESSIDAge": brzaccVLHiddenESSIDAge,
       "brzaccVLAverageReceiveRSSI": brzaccVLAverageReceiveRSSI,
       "brzaccVLCurrentNoiseFloor": brzaccVLCurrentNoiseFloor,
       "brzaccVLAverageSignalInterferenceRatio": brzaccVLAverageSignalInterferenceRatio,
       "brzaccVLTraps": brzaccVLTraps,
       "brzaccVLTrapSUMacAddr": brzaccVLTrapSUMacAddr,
       "brzaccVLTrapText": brzaccVLTrapText,
       "brzaccVLTrapToggle": brzaccVLTrapToggle,
       "brzaccVLTrapParameterChanged": brzaccVLTrapParameterChanged,
       "brzaccVLTrapAccessRights": brzaccVLTrapAccessRights,
       "brzaccVLTrapLog": brzaccVLTrapLog,
       "brzaccVLTrapTelnetUserIpAddress": brzaccVLTrapTelnetUserIpAddress,
       "brzaccVLTrapRTx": brzaccVLTrapRTx,
       "brzaccVLTrapFtpOrTftpStatus": brzaccVLTrapFtpOrTftpStatus,
       "brzaccVLDFSMoveFreq": brzaccVLDFSMoveFreq,
       "brzaccVLDFSMoveFreqNew": brzaccVLDFSMoveFreqNew,
       "brzaccVLEthBroadcastThresholdExceeded": brzaccVLEthBroadcastThresholdExceeded,
       "brzaccVLTrapSubscriberType": brzaccVLTrapSubscriberType,
       "brzaccVLTrapMACAddress": brzaccVLTrapMACAddress,
       "brzaccVLNewUnitTypeTrap": brzaccVLNewUnitTypeTrap,
       "brzaccVLTrapSWVersion": brzaccVLTrapSWVersion,
       "brzaccVLTrapSequenceNumber": brzaccVLTrapSequenceNumber,
       "brzaccVLTrapUnitMacAddr": brzaccVLTrapUnitMacAddr,
       "brzaccVLTrapParameterGroupCode": brzaccVLTrapParameterGroupCode,
       "brzaccVLTrapNewIP": brzaccVLTrapNewIP,
       "alvarionOID": alvarionOID,
       "brzAccessVLOID": brzAccessVLOID,
       "brzAccessVLAU": brzAccessVLAU,
       "brzAccessVLSU": brzAccessVLSU,
       "brzAccessVLProducts": brzAccessVLProducts,
       "brzaccVLSUassociatedAUTRAP": brzaccVLSUassociatedAUTRAP,
       "brzaccVLAUdisassociatedTRAP": brzaccVLAUdisassociatedTRAP,
       "brzaccVLAUagingTRAP": brzaccVLAUagingTRAP,
       "brzaccVLSUassociatedTRAP": brzaccVLSUassociatedTRAP,
       "brzaccVLAUwirelessQualityTRAP": brzaccVLAUwirelessQualityTRAP,
       "brzaccVLPowerUpFromReset": brzaccVLPowerUpFromReset,
       "brzaccVLTelnetStatusTRAP": brzaccVLTelnetStatusTRAP,
       "brzaccVLParameterChangedTRAP": brzaccVLParameterChangedTRAP,
       "brzaccVLLoadingStatusTRAP": brzaccVLLoadingStatusTRAP,
       "brzaccVLPromiscuousModeTRAP": brzaccVLPromiscuousModeTRAP,
       "brzaccVLDFSRadarDetectedTRAP": brzaccVLDFSRadarDetectedTRAP,
       "brzaccVLDFSFrequencyTRAP": brzaccVLDFSFrequencyTRAP,
       "brzaccVLDFSNoFreeChannelsExistsTRAP": brzaccVLDFSNoFreeChannelsExistsTRAP,
       "brzaccVLEthBroadcastMulticastLimiterTRAP": brzaccVLEthBroadcastMulticastLimiterTRAP,
       "brzaccVLAUSUnsupportedSubscriberTypeTRAP": brzaccVLAUSUnsupportedSubscriberTypeTRAP,
       "brzaccVLUnitTypeChangedTRAP": brzaccVLUnitTypeChangedTRAP,
       "brzaccVLWLPrioritizationNotSupportedBySUTRAP": brzaccVLWLPrioritizationNotSupportedBySUTRAP,
       "brzaccVLParameterChangeTRAP": brzaccVLParameterChangeTRAP,
       "brzaccVLRunTimeIPChangeTRAP": brzaccVLRunTimeIPChangeTRAP,
       "brzaccVLDisassociateAllStationsTRAP": brzaccVLDisassociateAllStationsTRAP,
       "brzAccessVLAU-BS": brzAccessVLAU_BS,
       "brzAccessVLAU-SA": brzAccessVLAU_SA,
       "brzAccessVLAUS-BS": brzAccessVLAUS_BS,
       "brzAccessVLAUS-SA": brzAccessVLAUS_SA,
       "brzAccessAU-EZ": brzAccessAU_EZ,
       "brzAccessVLSU-6-1D": brzAccessVLSU_6_1D,
       "brzAccessVLSU-6-BD": brzAccessVLSU_6_BD,
       "brzAccessVLSU-24-BD": brzAccessVLSU_24_BD,
       "brzAccessVLSU-BD": brzAccessVLSU_BD,
       "brzAccessVLSU-54-BD": brzAccessVLSU_54_BD,
       "brzAccessVLSU-3-1D": brzAccessVLSU_3_1D,
       "brzAccessVLSU-3-4D": brzAccessVLSU_3_4D,
       "brzAccessVLSU-I": brzAccessVLSU_I,
       "brzAccessVLSU-EZ": brzAccessVLSU_EZ,
       "brzAccessVLSU-V": brzAccessVLSU_V,
       "brzNetB-BU-B14": brzNetB_BU_B14,
       "brzNetB-BU-B28": brzNetB_BU_B28,
       "brzNetB-BU-B100": brzNetB_BU_B100,
       "brzNetB-BU-B10": brzNetB_BU_B10,
       "brzNetB-RB-B14": brzNetB_RB_B14,
       "brzNetB-RB-B28": brzNetB_RB_B28,
       "brzNetB-RB-B100": brzNetB_RB_B100,
       "brzNetB-RB-B10": brzNetB_RB_B10,
       "brzAccess4900-AU-BS": brzAccess4900_AU_BS,
       "brzAccess4900-AU-SA": brzAccess4900_AU_SA,
       "brzAccess4900-SU-BD": brzAccess4900_SU_BD,
       "brzAccessVLSU-8-BD": brzAccessVLSU_8_BD,
       "brzAccessVLSU-1-BD": brzAccessVLSU_1_BD,
       "brzAccessVLSU-3-L": brzAccessVLSU_3_L,
       "brzAccessVLSU-6-L": brzAccessVLSU_6_L,
       "brzAccessVLSU-12-L": brzAccessVLSU_12_L,
       "brzAccessVL-AU": brzAccessVL_AU,
       "brzAccessVL-SU": brzAccessVL_SU}
)
