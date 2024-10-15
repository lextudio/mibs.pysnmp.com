# SNMP MIB module (JUNIPER-IFOPTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IFOPTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:07 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxOpticsMibRoot,
 jnxOpticsNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxOpticsMibRoot",
    "jnxOpticsNotifications")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxIfOpticsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1)
)
jnxIfOpticsMib.setRevisions(
        ("2012-01-26 00:00",
         "2012-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxOpticsLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxFarEnd", 2),
          ("jnxNearEnd", 1))
    )



class JnxOpticsDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jnxBiDir", 3),
          ("jnxRxDir", 2),
          ("jnxTxDir", 1))
    )



class JnxOpticsSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("jnxCritical", 1),
          ("jnxInfo", 4),
          ("jnxMajor", 2),
          ("jnxMinor", 3))
    )



class JnxOpticsServiceStateAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxNonServiceAffecting", 1),
          ("jnxNotSupported", 0),
          ("jnxServiceAffecting", 2))
    )



class JnxOpticsChannelSpacing(Integer32, TextualConvention):
    status = "current"
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
        *(("spacing100Ghz", 1),
          ("spacing12point5Ghz", 4),
          ("spacing25Ghz", 3),
          ("spacing50Ghz", 2),
          ("spacing6point5Ghz", 5))
    )



class JnxOpticsNotificationId(Integer32, TextualConvention):
    status = "current"
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
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("jnxOptics24HourCarrierFreqHighAlert", 42),
          ("jnxOptics24HourCarrierFreqLowAlert", 43),
          ("jnxOptics24HourModuleTempHighThreshAlert", 24),
          ("jnxOptics24HourModuleTempLowThreshAlert", 25),
          ("jnxOptics24HourRxPowerHighThreshAlert", 22),
          ("jnxOptics24HourRxPowerLowThreshAlert", 23),
          ("jnxOptics24HourTxPowerHighThreshAlert", 20),
          ("jnxOptics24HourTxPowerLowThreshAlert", 21),
          ("jnxOpticsAvgPowerAlarm", 11),
          ("jnxOpticsBiasCurrentHighAlarm", 5),
          ("jnxOpticsBiasCurrentLowAlarm", 6),
          ("jnxOpticsCarrierFreqHighAlert", 40),
          ("jnxOpticsCarrierFreqLowAlert", 41),
          ("jnxOpticsChromaticDispHighWarning", 36),
          ("jnxOpticsChromaticDispLowWarning", 37),
          ("jnxOpticsLOS", 1),
          ("jnxOpticsLossofACPowerAlarm", 13),
          ("jnxOpticsModuleTempHighThreshAlert", 18),
          ("jnxOpticsModuleTempHighWarning", 32),
          ("jnxOpticsModuleTempLowThreshAlert", 19),
          ("jnxOpticsModuleTempLowWarning", 33),
          ("jnxOpticsOSNRLowWarning", 39),
          ("jnxOpticsPowerHighAlarm", 3),
          ("jnxOpticsPowerLowAlarm", 4),
          ("jnxOpticsQLowWarning", 38),
          ("jnxOpticsRxCarrierFreqHigh", 34),
          ("jnxOpticsRxCarrierFreqLow", 35),
          ("jnxOpticsRxLossAvgPowerAlarm", 12),
          ("jnxOpticsRxPLLLockAlarm", 10),
          ("jnxOpticsRxPowerHighAlarm", 26),
          ("jnxOpticsRxPowerHighThreshAlert", 16),
          ("jnxOpticsRxPowerHighWarning", 30),
          ("jnxOpticsRxPowerLowAlarm", 27),
          ("jnxOpticsRxPowerLowThreshAlert", 17),
          ("jnxOpticsRxPowerLowWarning", 31),
          ("jnxOpticsTemperatureHighAlarm", 7),
          ("jnxOpticsTemperaturelowAlarm", 8),
          ("jnxOpticsTxPLLLockAlarm", 9),
          ("jnxOpticsTxPowerHighThreshAlert", 14),
          ("jnxOpticsTxPowerHighWarning", 28),
          ("jnxOpticsTxPowerLowThreshAlert", 15),
          ("jnxOpticsTxPowerLowWarning", 29),
          ("jnxOpticsWavelenthLockErr", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JnxOptics_ObjectIdentity = ObjectIdentity
jnxOptics = _JnxOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1)
)
_JnxOpticsConfigTable_Object = MibTable
jnxOpticsConfigTable = _JnxOpticsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsConfigTable.setStatus("current")
_JnxOpticsConfigEntry_Object = MibTableRow
jnxOpticsConfigEntry = _JnxOpticsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1)
)
jnxOpticsConfigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL3Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsConfigEntry.setStatus("current")


class _JnxOpticsConfigContainerIndex_Type(Integer32):
    """Custom type jnxOpticsConfigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsConfigContainerIndex_Object = MibTableColumn
jnxOpticsConfigContainerIndex = _JnxOpticsConfigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 1),
    _JnxOpticsConfigContainerIndex_Type()
)
jnxOpticsConfigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigContainerIndex.setStatus("current")


class _JnxOpticsConfigL1Index_Type(Integer32):
    """Custom type jnxOpticsConfigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL1Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL1Index_Object = MibTableColumn
jnxOpticsConfigL1Index = _JnxOpticsConfigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 2),
    _JnxOpticsConfigL1Index_Type()
)
jnxOpticsConfigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL1Index.setStatus("current")


class _JnxOpticsConfigL2Index_Type(Integer32):
    """Custom type jnxOpticsConfigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL2Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL2Index_Object = MibTableColumn
jnxOpticsConfigL2Index = _JnxOpticsConfigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 3),
    _JnxOpticsConfigL2Index_Type()
)
jnxOpticsConfigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL2Index.setStatus("current")


class _JnxOpticsConfigL3Index_Type(Integer32):
    """Custom type jnxOpticsConfigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL3Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL3Index_Object = MibTableColumn
jnxOpticsConfigL3Index = _JnxOpticsConfigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 4),
    _JnxOpticsConfigL3Index_Type()
)
jnxOpticsConfigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL3Index.setStatus("current")
_JnxOpticsType_Type = Integer32
_JnxOpticsType_Object = MibTableColumn
jnxOpticsType = _JnxOpticsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 5),
    _JnxOpticsType_Type()
)
jnxOpticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsType.setStatus("current")
_JnxLaserEnable_Type = TruthValue
_JnxLaserEnable_Object = MibTableColumn
jnxLaserEnable = _JnxLaserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 6),
    _JnxLaserEnable_Type()
)
jnxLaserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxLaserEnable.setStatus("current")
_JnxWavelength_Type = Unsigned32
_JnxWavelength_Object = MibTableColumn
jnxWavelength = _JnxWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 7),
    _JnxWavelength_Type()
)
jnxWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxWavelength.setStatus("current")
if mibBuilder.loadTexts:
    jnxWavelength.setUnits("0.01 nm")
_JnxSpacing_Type = JnxOpticsChannelSpacing
_JnxSpacing_Object = MibTableColumn
jnxSpacing = _JnxSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 8),
    _JnxSpacing_Type()
)
jnxSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpacing.setStatus("current")
_JnxModulation_Type = Unsigned32
_JnxModulation_Object = MibTableColumn
jnxModulation = _JnxModulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 9),
    _JnxModulation_Type()
)
jnxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModulation.setStatus("current")
_JnxTxOpticalPower_Type = Integer32
_JnxTxOpticalPower_Object = MibTableColumn
jnxTxOpticalPower = _JnxTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 10),
    _JnxTxOpticalPower_Type()
)
jnxTxOpticalPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxOpticalPower.setUnits("0.01 dbm")
_JnxRxOpticalPower_Type = Integer32
_JnxRxOpticalPower_Object = MibTableColumn
jnxRxOpticalPower = _JnxRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 11),
    _JnxRxOpticalPower_Type()
)
jnxRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxOpticalPower.setUnits("0.01 dbm")
_JnxModuleTempHighThresh_Type = Integer32
_JnxModuleTempHighThresh_Object = MibTableColumn
jnxModuleTempHighThresh = _JnxModuleTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 12),
    _JnxModuleTempHighThresh_Type()
)
jnxModuleTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModuleTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxModuleTempHighThresh.setUnits("Celsius (0.01 degrees C)")
_JnxModuleTempLowThresh_Type = Integer32
_JnxModuleTempLowThresh_Object = MibTableColumn
jnxModuleTempLowThresh = _JnxModuleTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 13),
    _JnxModuleTempLowThresh_Type()
)
jnxModuleTempLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModuleTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxModuleTempLowThresh.setUnits("Celsius (0.01 degrees C)")
_JnxTxPowerHighThresh_Type = Integer32
_JnxTxPowerHighThresh_Object = MibTableColumn
jnxTxPowerHighThresh = _JnxTxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 14),
    _JnxTxPowerHighThresh_Type()
)
jnxTxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxPowerHighThresh.setUnits("0.01 dbm")
_JnxTxPowerLowThresh_Type = Integer32
_JnxTxPowerLowThresh_Object = MibTableColumn
jnxTxPowerLowThresh = _JnxTxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 15),
    _JnxTxPowerLowThresh_Type()
)
jnxTxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxPowerLowThresh.setUnits("0.01 dbm")
_JnxRxPowerHighThresh_Type = Integer32
_JnxRxPowerHighThresh_Object = MibTableColumn
jnxRxPowerHighThresh = _JnxRxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 16),
    _JnxRxPowerHighThresh_Type()
)
jnxRxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxPowerHighThresh.setUnits("0.01 dbm")
_JnxRxPowerLowThresh_Type = Integer32
_JnxRxPowerLowThresh_Object = MibTableColumn
jnxRxPowerLowThresh = _JnxRxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 17),
    _JnxRxPowerLowThresh_Type()
)
jnxRxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxPowerLowThresh.setUnits("0.01 dbm")
_Jnx24HourModuleTempHighThresh_Type = Integer32
_Jnx24HourModuleTempHighThresh_Object = MibTableColumn
jnx24HourModuleTempHighThresh = _Jnx24HourModuleTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 18),
    _Jnx24HourModuleTempHighThresh_Type()
)
jnx24HourModuleTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnx24HourModuleTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourModuleTempHighThresh.setUnits("Celsius (0.01 degrees C)")
_Jnx24HourModuleTempLowThresh_Type = Integer32
_Jnx24HourModuleTempLowThresh_Object = MibTableColumn
jnx24HourModuleTempLowThresh = _Jnx24HourModuleTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 19),
    _Jnx24HourModuleTempLowThresh_Type()
)
jnx24HourModuleTempLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnx24HourModuleTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourModuleTempLowThresh.setUnits("Celsius (0.01 degrees C)")
_Jnx24HourTxPowerHighThresh_Type = Integer32
_Jnx24HourTxPowerHighThresh_Object = MibTableColumn
jnx24HourTxPowerHighThresh = _Jnx24HourTxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 20),
    _Jnx24HourTxPowerHighThresh_Type()
)
jnx24HourTxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourTxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourTxPowerHighThresh.setUnits("0.01 dbm")
_Jnx24HourTxPowerLowThresh_Type = Integer32
_Jnx24HourTxPowerLowThresh_Object = MibTableColumn
jnx24HourTxPowerLowThresh = _Jnx24HourTxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 21),
    _Jnx24HourTxPowerLowThresh_Type()
)
jnx24HourTxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourTxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourTxPowerLowThresh.setUnits("0.01 dbm")
_Jnx24HourRxPowerHighThresh_Type = Integer32
_Jnx24HourRxPowerHighThresh_Object = MibTableColumn
jnx24HourRxPowerHighThresh = _Jnx24HourRxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 22),
    _Jnx24HourRxPowerHighThresh_Type()
)
jnx24HourRxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourRxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourRxPowerHighThresh.setUnits("0.01 dbm")
_Jnx24HourRxPowerLowThresh_Type = Integer32
_Jnx24HourRxPowerLowThresh_Object = MibTableColumn
jnx24HourRxPowerLowThresh = _Jnx24HourRxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 23),
    _Jnx24HourRxPowerLowThresh_Type()
)
jnx24HourRxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourRxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourRxPowerLowThresh.setUnits("0.01 dbm")
_JnxRxLosPowerWarningThresh_Type = Integer32
_JnxRxLosPowerWarningThresh_Object = MibTableColumn
jnxRxLosPowerWarningThresh = _JnxRxLosPowerWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 24),
    _JnxRxLosPowerWarningThresh_Type()
)
jnxRxLosPowerWarningThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxLosPowerWarningThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxLosPowerWarningThresh.setUnits("0.01 dbm")
_JnxRxLosPowerAlarmThresh_Type = Integer32
_JnxRxLosPowerAlarmThresh_Object = MibTableColumn
jnxRxLosPowerAlarmThresh = _JnxRxLosPowerAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 25),
    _JnxRxLosPowerAlarmThresh_Type()
)
jnxRxLosPowerAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxLosPowerAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxLosPowerAlarmThresh.setUnits("0.01 dbm")


class _JnxOpticsCurrentStatus_Type(Bits):
    """Custom type jnxOpticsCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("avgPowerAlarm", 11),
          ("biasCurrentHighAlarm", 5),
          ("biasCurrentLowAlarm", 6),
          ("lossofACPowerAlarm", 13),
          ("moduleTempHigh24HourThreshAlert", 24),
          ("moduleTempHighThreshAlert", 18),
          ("moduleTempLow24HourThreshAlert", 25),
          ("moduleTempLowThreshAlert", 19),
          ("opticalLos", 1),
          ("powerHighAlarm", 3),
          ("powerLowAlarm", 4),
          ("powerRxHighAlarm", 26),
          ("powerRxHighWarning", 30),
          ("powerRxLowAlarm", 27),
          ("powerRxLowWarning", 31),
          ("powerTxHighWarning", 28),
          ("powerTxLowWarning", 29),
          ("rxLossAvgPowerAlarm", 12),
          ("rxPLLLockAlarm", 10),
          ("rxPowerHigh24HourThreshAlert", 22),
          ("rxPowerHighThreshAlert", 16),
          ("rxPowerLow24HourThreshAlert", 23),
          ("rxPowerLowThreshAlert", 17),
          ("temperatureHighAlarm", 7),
          ("temperatureHighWarning", 32),
          ("temperaturelowAlarm", 8),
          ("temperaturelowWarning", 33),
          ("txPLLLockAlarm", 9),
          ("txPowerHigh24HourThreshAlert", 20),
          ("txPowerHighThreshAlert", 14),
          ("txPowerLow24HourThreshAlert", 21),
          ("txPowerLowThreshAlert", 15),
          ("wavelenthLockErr", 2))
    )

_JnxOpticsCurrentStatus_Type.__name__ = "Bits"
_JnxOpticsCurrentStatus_Object = MibTableColumn
jnxOpticsCurrentStatus = _JnxOpticsCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 26),
    _JnxOpticsCurrentStatus_Type()
)
jnxOpticsCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsCurrentStatus.setStatus("current")
_JnxTxPowerHighEnableTCA_Type = TruthValue
_JnxTxPowerHighEnableTCA_Object = MibTableColumn
jnxTxPowerHighEnableTCA = _JnxTxPowerHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 27),
    _JnxTxPowerHighEnableTCA_Type()
)
jnxTxPowerHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerHighEnableTCA.setStatus("current")
_JnxTxPowerLowEnableTCA_Type = TruthValue
_JnxTxPowerLowEnableTCA_Object = MibTableColumn
jnxTxPowerLowEnableTCA = _JnxTxPowerLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 28),
    _JnxTxPowerLowEnableTCA_Type()
)
jnxTxPowerLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerLowEnableTCA.setStatus("current")
_JnxRxPowerHighEnableTCA_Type = TruthValue
_JnxRxPowerHighEnableTCA_Object = MibTableColumn
jnxRxPowerHighEnableTCA = _JnxRxPowerHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 29),
    _JnxRxPowerHighEnableTCA_Type()
)
jnxRxPowerHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerHighEnableTCA.setStatus("current")
_JnxRxPowerLowEnableTCA_Type = TruthValue
_JnxRxPowerLowEnableTCA_Object = MibTableColumn
jnxRxPowerLowEnableTCA = _JnxRxPowerLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 30),
    _JnxRxPowerLowEnableTCA_Type()
)
jnxRxPowerLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerLowEnableTCA.setStatus("current")
_JnxModuleTempHighEnableTCA_Type = TruthValue
_JnxModuleTempHighEnableTCA_Object = MibTableColumn
jnxModuleTempHighEnableTCA = _JnxModuleTempHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 31),
    _JnxModuleTempHighEnableTCA_Type()
)
jnxModuleTempHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxModuleTempHighEnableTCA.setStatus("current")
_JnxModuleTempLowEnableTCA_Type = TruthValue
_JnxModuleTempLowEnableTCA_Object = MibTableColumn
jnxModuleTempLowEnableTCA = _JnxModuleTempLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 32),
    _JnxModuleTempLowEnableTCA_Type()
)
jnxModuleTempLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxModuleTempLowEnableTCA.setStatus("current")
_JnxCarFreqOffsetHighEnableTCA_Type = TruthValue
_JnxCarFreqOffsetHighEnableTCA_Object = MibTableColumn
jnxCarFreqOffsetHighEnableTCA = _JnxCarFreqOffsetHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 33),
    _JnxCarFreqOffsetHighEnableTCA_Type()
)
jnxCarFreqOffsetHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighEnableTCA.setStatus("current")
_JnxCarFreqOffsetLowEnableTCA_Type = TruthValue
_JnxCarFreqOffsetLowEnableTCA_Object = MibTableColumn
jnxCarFreqOffsetLowEnableTCA = _JnxCarFreqOffsetLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 34),
    _JnxCarFreqOffsetLowEnableTCA_Type()
)
jnxCarFreqOffsetLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowEnableTCA.setStatus("current")
_JnxCarFreqOffsetHighThresh_Type = Integer32
_JnxCarFreqOffsetHighThresh_Object = MibTableColumn
jnxCarFreqOffsetHighThresh = _JnxCarFreqOffsetHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 35),
    _JnxCarFreqOffsetHighThresh_Type()
)
jnxCarFreqOffsetHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighThresh.setUnits("MHz")
_Jnx24HourCarFreqOffsetHighThresh_Type = Integer32
_Jnx24HourCarFreqOffsetHighThresh_Object = MibTableColumn
jnx24HourCarFreqOffsetHighThresh = _Jnx24HourCarFreqOffsetHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 36),
    _Jnx24HourCarFreqOffsetHighThresh_Type()
)
jnx24HourCarFreqOffsetHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetHighThresh.setUnits("MHz")
_JnxCarFreqOffsetLowThresh_Type = Integer32
_JnxCarFreqOffsetLowThresh_Object = MibTableColumn
jnxCarFreqOffsetLowThresh = _JnxCarFreqOffsetLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 37),
    _JnxCarFreqOffsetLowThresh_Type()
)
jnxCarFreqOffsetLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowThresh.setUnits("MHz")
_Jnx24HourCarFreqOffsetLowThresh_Type = Integer32
_Jnx24HourCarFreqOffsetLowThresh_Object = MibTableColumn
jnx24HourCarFreqOffsetLowThresh = _Jnx24HourCarFreqOffsetLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 38),
    _Jnx24HourCarFreqOffsetLowThresh_Type()
)
jnx24HourCarFreqOffsetLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetLowThresh.setUnits("MHz")
_JnxOpticsTraceToneCfgTable_Object = MibTable
jnxOpticsTraceToneCfgTable = _JnxOpticsTraceToneCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTable.setStatus("current")
_JnxOpticsTraceToneCfgEntry_Object = MibTableRow
jnxOpticsTraceToneCfgEntry = _JnxOpticsTraceToneCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1)
)
jnxOpticsTraceToneCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgEntry.setStatus("current")


class _JnxOpticsTraceToneCfgContainerIndex_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgContainerIndex_Object = MibTableColumn
jnxOpticsTraceToneCfgContainerIndex = _JnxOpticsTraceToneCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 1),
    _JnxOpticsTraceToneCfgContainerIndex_Type()
)
jnxOpticsTraceToneCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgContainerIndex.setStatus("current")


class _JnxOpticsTraceToneCfgL1Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL1Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL1Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL1Index = _JnxOpticsTraceToneCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 2),
    _JnxOpticsTraceToneCfgL1Index_Type()
)
jnxOpticsTraceToneCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL1Index.setStatus("current")


class _JnxOpticsTraceToneCfgL2Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL2Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL2Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL2Index = _JnxOpticsTraceToneCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 3),
    _JnxOpticsTraceToneCfgL2Index_Type()
)
jnxOpticsTraceToneCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL2Index.setStatus("current")


class _JnxOpticsTraceToneCfgL3Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL3Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL3Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL3Index = _JnxOpticsTraceToneCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 4),
    _JnxOpticsTraceToneCfgL3Index_Type()
)
jnxOpticsTraceToneCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL3Index.setStatus("current")
_JnxOpticsTraceToneCfgTxEnable_Type = TruthValue
_JnxOpticsTraceToneCfgTxEnable_Object = MibTableColumn
jnxOpticsTraceToneCfgTxEnable = _JnxOpticsTraceToneCfgTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 5),
    _JnxOpticsTraceToneCfgTxEnable_Type()
)
jnxOpticsTraceToneCfgTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTxEnable.setStatus("current")
_JnxOpticsTraceToneCfgRxEnable_Type = TruthValue
_JnxOpticsTraceToneCfgRxEnable_Object = MibTableColumn
jnxOpticsTraceToneCfgRxEnable = _JnxOpticsTraceToneCfgRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 6),
    _JnxOpticsTraceToneCfgRxEnable_Type()
)
jnxOpticsTraceToneCfgRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgRxEnable.setStatus("current")
_JnxOpticsTraceToneCfgDestId_Type = OctetString
_JnxOpticsTraceToneCfgDestId_Object = MibTableColumn
jnxOpticsTraceToneCfgDestId = _JnxOpticsTraceToneCfgDestId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 7),
    _JnxOpticsTraceToneCfgDestId_Type()
)
jnxOpticsTraceToneCfgDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgDestId.setStatus("current")
_JnxOpticsTraceToneCfgTxMsg_Type = OctetString
_JnxOpticsTraceToneCfgTxMsg_Object = MibTableColumn
jnxOpticsTraceToneCfgTxMsg = _JnxOpticsTraceToneCfgTxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 8),
    _JnxOpticsTraceToneCfgTxMsg_Type()
)
jnxOpticsTraceToneCfgTxMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTxMsg.setStatus("current")
_JnxOpticsTraceToneCfgRxMsg_Type = OctetString
_JnxOpticsTraceToneCfgRxMsg_Object = MibTableColumn
jnxOpticsTraceToneCfgRxMsg = _JnxOpticsTraceToneCfgRxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 9),
    _JnxOpticsTraceToneCfgRxMsg_Type()
)
jnxOpticsTraceToneCfgRxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgRxMsg.setStatus("current")
_JnxOpticsNotificationTrigDefaultHoldtimeUp_Type = Integer32
_JnxOpticsNotificationTrigDefaultHoldtimeUp_Object = MibScalar
jnxOpticsNotificationTrigDefaultHoldtimeUp = _JnxOpticsNotificationTrigDefaultHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 3),
    _JnxOpticsNotificationTrigDefaultHoldtimeUp_Type()
)
jnxOpticsNotificationTrigDefaultHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigDefaultHoldtimeUp.setStatus("current")
_JnxOpticsNotificationTrigDefaultHoldtimeDown_Type = Integer32
_JnxOpticsNotificationTrigDefaultHoldtimeDown_Object = MibScalar
jnxOpticsNotificationTrigDefaultHoldtimeDown = _JnxOpticsNotificationTrigDefaultHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 4),
    _JnxOpticsNotificationTrigDefaultHoldtimeDown_Type()
)
jnxOpticsNotificationTrigDefaultHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigDefaultHoldtimeDown.setStatus("current")
_JnxOpticsNotificationTrigTable_Object = MibTable
jnxOpticsNotificationTrigTable = _JnxOpticsNotificationTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigTable.setStatus("current")
_JnxOpticsNotificationTrigEntry_Object = MibTableRow
jnxOpticsNotificationTrigEntry = _JnxOpticsNotificationTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1)
)
jnxOpticsNotificationTrigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL3Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigAlmId"),
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigEntry.setStatus("current")


class _JnxOpticsNotificationTrigContainerIndex_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigContainerIndex_Object = MibTableColumn
jnxOpticsNotificationTrigContainerIndex = _JnxOpticsNotificationTrigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 1),
    _JnxOpticsNotificationTrigContainerIndex_Type()
)
jnxOpticsNotificationTrigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigContainerIndex.setStatus("current")


class _JnxOpticsNotificationTrigL1Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL1Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL1Index_Object = MibTableColumn
jnxOpticsNotificationTrigL1Index = _JnxOpticsNotificationTrigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 2),
    _JnxOpticsNotificationTrigL1Index_Type()
)
jnxOpticsNotificationTrigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL1Index.setStatus("current")


class _JnxOpticsNotificationTrigL2Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL2Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL2Index_Object = MibTableColumn
jnxOpticsNotificationTrigL2Index = _JnxOpticsNotificationTrigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 3),
    _JnxOpticsNotificationTrigL2Index_Type()
)
jnxOpticsNotificationTrigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL2Index.setStatus("current")


class _JnxOpticsNotificationTrigL3Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL3Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL3Index_Object = MibTableColumn
jnxOpticsNotificationTrigL3Index = _JnxOpticsNotificationTrigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 4),
    _JnxOpticsNotificationTrigL3Index_Type()
)
jnxOpticsNotificationTrigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL3Index.setStatus("current")
_JnxOpticsNotificationTrigAlmId_Type = JnxOpticsNotificationId
_JnxOpticsNotificationTrigAlmId_Object = MibTableColumn
jnxOpticsNotificationTrigAlmId = _JnxOpticsNotificationTrigAlmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 5),
    _JnxOpticsNotificationTrigAlmId_Type()
)
jnxOpticsNotificationTrigAlmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigAlmId.setStatus("current")
_JnxOpticsNotificationTrigSeverity_Type = JnxOpticsSeverity
_JnxOpticsNotificationTrigSeverity_Object = MibTableColumn
jnxOpticsNotificationTrigSeverity = _JnxOpticsNotificationTrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 6),
    _JnxOpticsNotificationTrigSeverity_Type()
)
jnxOpticsNotificationTrigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigSeverity.setStatus("current")
_JnxOpticsNotificationTrigIgnore_Type = TruthValue
_JnxOpticsNotificationTrigIgnore_Object = MibTableColumn
jnxOpticsNotificationTrigIgnore = _JnxOpticsNotificationTrigIgnore_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 7),
    _JnxOpticsNotificationTrigIgnore_Type()
)
jnxOpticsNotificationTrigIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigIgnore.setStatus("current")
_JnxOpticsNotificationTrigHoldtimeUp_Type = Integer32
_JnxOpticsNotificationTrigHoldtimeUp_Object = MibTableColumn
jnxOpticsNotificationTrigHoldtimeUp = _JnxOpticsNotificationTrigHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 8),
    _JnxOpticsNotificationTrigHoldtimeUp_Type()
)
jnxOpticsNotificationTrigHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigHoldtimeUp.setStatus("current")
_JnxOpticsNotificationTrigHoldtimeDown_Type = Integer32
_JnxOpticsNotificationTrigHoldtimeDown_Object = MibTableColumn
jnxOpticsNotificationTrigHoldtimeDown = _JnxOpticsNotificationTrigHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 9),
    _JnxOpticsNotificationTrigHoldtimeDown_Type()
)
jnxOpticsNotificationTrigHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigHoldtimeDown.setStatus("current")
_JnxOpticsTrigServiceStateAction_Type = JnxOpticsServiceStateAction
_JnxOpticsTrigServiceStateAction_Object = MibTableColumn
jnxOpticsTrigServiceStateAction = _JnxOpticsTrigServiceStateAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 10),
    _JnxOpticsTrigServiceStateAction_Type()
)
jnxOpticsTrigServiceStateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsTrigServiceStateAction.setStatus("current")
_JnxOpticsClearAllPMs_Type = TruthValue
_JnxOpticsClearAllPMs_Object = MibScalar
jnxOpticsClearAllPMs = _JnxOpticsClearAllPMs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 6),
    _JnxOpticsClearAllPMs_Type()
)
jnxOpticsClearAllPMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearAllPMs.setStatus("current")
_JnxOpticsClearIfPMsTable_Object = MibTable
jnxOpticsClearIfPMsTable = _JnxOpticsClearIfPMsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxOpticsClearIfPMsTable.setStatus("current")
_JnxOpticsClearIfPMsEntry_Object = MibTableRow
jnxOpticsClearIfPMsEntry = _JnxOpticsClearIfPMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1)
)
jnxOpticsClearIfPMsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsClearIfPMsEntry.setStatus("current")
_JnxOpticsClearCurrent_Type = TruthValue
_JnxOpticsClearCurrent_Object = MibTableColumn
jnxOpticsClearCurrent = _JnxOpticsClearCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 1),
    _JnxOpticsClearCurrent_Type()
)
jnxOpticsClearCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearCurrent.setStatus("current")
_JnxOpticsClearInterfaceInterval_Type = TruthValue
_JnxOpticsClearInterfaceInterval_Object = MibTableColumn
jnxOpticsClearInterfaceInterval = _JnxOpticsClearInterfaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 2),
    _JnxOpticsClearInterfaceInterval_Type()
)
jnxOpticsClearInterfaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceInterval.setStatus("current")
_JnxOpticsClearInterfaceDay_Type = TruthValue
_JnxOpticsClearInterfaceDay_Object = MibTableColumn
jnxOpticsClearInterfaceDay = _JnxOpticsClearInterfaceDay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 3),
    _JnxOpticsClearInterfaceDay_Type()
)
jnxOpticsClearInterfaceDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceDay.setStatus("current")
_JnxOpticsClearInterfaceAll_Type = TruthValue
_JnxOpticsClearInterfaceAll_Object = MibTableColumn
jnxOpticsClearInterfaceAll = _JnxOpticsClearInterfaceAll_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 4),
    _JnxOpticsClearInterfaceAll_Type()
)
jnxOpticsClearInterfaceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceAll.setStatus("current")
_JnxOpticsPerformanceMonitoring_ObjectIdentity = ObjectIdentity
jnxOpticsPerformanceMonitoring = _JnxOpticsPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2)
)
_JnxOpticsPMCurrentTable_Object = MibTable
jnxOpticsPMCurrentTable = _JnxOpticsPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsPMCurrentTable.setStatus("current")
_JnxOpticsPMCurrentEntry_Object = MibTableRow
jnxOpticsPMCurrentEntry = _JnxOpticsPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1)
)
jnxOpticsPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMCurrentEntry.setStatus("current")
_JnxPMCurChromaticDispersion_Type = Integer32
_JnxPMCurChromaticDispersion_Object = MibTableColumn
jnxPMCurChromaticDispersion = _JnxPMCurChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 1),
    _JnxPMCurChromaticDispersion_Type()
)
jnxPMCurChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurChromaticDispersion.setUnits("ps/nm")
_JnxPMCurDiffGroupDelay_Type = Integer32
_JnxPMCurDiffGroupDelay_Object = MibTableColumn
jnxPMCurDiffGroupDelay = _JnxPMCurDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 2),
    _JnxPMCurDiffGroupDelay_Type()
)
jnxPMCurDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurDiffGroupDelay.setUnits("ps")
_JnxPMCurPolarizationState_Type = Integer32
_JnxPMCurPolarizationState_Object = MibTableColumn
jnxPMCurPolarizationState = _JnxPMCurPolarizationState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 3),
    _JnxPMCurPolarizationState_Type()
)
jnxPMCurPolarizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurPolarizationState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurPolarizationState.setUnits("rad/s")
_JnxPMCurPolarDepLoss_Type = Integer32
_JnxPMCurPolarDepLoss_Object = MibTableColumn
jnxPMCurPolarDepLoss = _JnxPMCurPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 4),
    _JnxPMCurPolarDepLoss_Type()
)
jnxPMCurPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurQ_Type = Integer32
_JnxPMCurQ_Object = MibTableColumn
jnxPMCurQ = _JnxPMCurQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 5),
    _JnxPMCurQ_Type()
)
jnxPMCurQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurQ.setUnits("0.1 dB")
_JnxPMCurSNR_Type = Integer32
_JnxPMCurSNR_Object = MibTableColumn
jnxPMCurSNR = _JnxPMCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 6),
    _JnxPMCurSNR_Type()
)
jnxPMCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurSNR.setUnits("0.1 dB")
_JnxPMCurTxOutputPower_Type = Integer32
_JnxPMCurTxOutputPower_Object = MibTableColumn
jnxPMCurTxOutputPower = _JnxPMCurTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 7),
    _JnxPMCurTxOutputPower_Type()
)
jnxPMCurTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurRxInputPower_Type = Integer32
_JnxPMCurRxInputPower_Object = MibTableColumn
jnxPMCurRxInputPower = _JnxPMCurRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 8),
    _JnxPMCurRxInputPower_Type()
)
jnxPMCurRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurRxInputPower.setUnits("0.01 dbm")
_JnxPMCurMinChromaticDispersion_Type = Integer32
_JnxPMCurMinChromaticDispersion_Object = MibTableColumn
jnxPMCurMinChromaticDispersion = _JnxPMCurMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 9),
    _JnxPMCurMinChromaticDispersion_Type()
)
jnxPMCurMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinChromaticDispersion.setUnits("ps/nm")
_JnxPMCurMaxChromaticDispersion_Type = Integer32
_JnxPMCurMaxChromaticDispersion_Object = MibTableColumn
jnxPMCurMaxChromaticDispersion = _JnxPMCurMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 10),
    _JnxPMCurMaxChromaticDispersion_Type()
)
jnxPMCurMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMCurAvgChromaticDispersion_Type = Integer32
_JnxPMCurAvgChromaticDispersion_Object = MibTableColumn
jnxPMCurAvgChromaticDispersion = _JnxPMCurAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 11),
    _JnxPMCurAvgChromaticDispersion_Type()
)
jnxPMCurAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMCurMinDiffGroupDelay_Type = Integer32
_JnxPMCurMinDiffGroupDelay_Object = MibTableColumn
jnxPMCurMinDiffGroupDelay = _JnxPMCurMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 12),
    _JnxPMCurMinDiffGroupDelay_Type()
)
jnxPMCurMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinDiffGroupDelay.setUnits("ps")
_JnxPMCurMaxDiffGroupDelay_Type = Integer32
_JnxPMCurMaxDiffGroupDelay_Object = MibTableColumn
jnxPMCurMaxDiffGroupDelay = _JnxPMCurMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 13),
    _JnxPMCurMaxDiffGroupDelay_Type()
)
jnxPMCurMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxDiffGroupDelay.setUnits("ps")
_JnxPMCurAvgDiffGroupDelay_Type = Integer32
_JnxPMCurAvgDiffGroupDelay_Object = MibTableColumn
jnxPMCurAvgDiffGroupDelay = _JnxPMCurAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 14),
    _JnxPMCurAvgDiffGroupDelay_Type()
)
jnxPMCurAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgDiffGroupDelay.setUnits("ps")
_JnxPMCurMinPolarState_Type = Integer32
_JnxPMCurMinPolarState_Object = MibTableColumn
jnxPMCurMinPolarState = _JnxPMCurMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 15),
    _JnxPMCurMinPolarState_Type()
)
jnxPMCurMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarState.setUnits("rad/s")
_JnxPMCurMaxPolarState_Type = Integer32
_JnxPMCurMaxPolarState_Object = MibTableColumn
jnxPMCurMaxPolarState = _JnxPMCurMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 16),
    _JnxPMCurMaxPolarState_Type()
)
jnxPMCurMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarState.setUnits("rad/s")
_JnxPMCurAvgPolarState_Type = Integer32
_JnxPMCurAvgPolarState_Object = MibTableColumn
jnxPMCurAvgPolarState = _JnxPMCurAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 17),
    _JnxPMCurAvgPolarState_Type()
)
jnxPMCurAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarState.setUnits("rad/s")
_JnxPMCurMinPolarDepLoss_Type = Integer32
_JnxPMCurMinPolarDepLoss_Object = MibTableColumn
jnxPMCurMinPolarDepLoss = _JnxPMCurMinPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 18),
    _JnxPMCurMinPolarDepLoss_Type()
)
jnxPMCurMinPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurMaxPolarDepLoss_Type = Integer32
_JnxPMCurMaxPolarDepLoss_Object = MibTableColumn
jnxPMCurMaxPolarDepLoss = _JnxPMCurMaxPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 19),
    _JnxPMCurMaxPolarDepLoss_Type()
)
jnxPMCurMaxPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurAvgPolarDepLoss_Type = Integer32
_JnxPMCurAvgPolarDepLoss_Object = MibTableColumn
jnxPMCurAvgPolarDepLoss = _JnxPMCurAvgPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 20),
    _JnxPMCurAvgPolarDepLoss_Type()
)
jnxPMCurAvgPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurMinQ_Type = Integer32
_JnxPMCurMinQ_Object = MibTableColumn
jnxPMCurMinQ = _JnxPMCurMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 21),
    _JnxPMCurMinQ_Type()
)
jnxPMCurMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinQ.setUnits("0.1 dB")
_JnxPMCurMaxQ_Type = Integer32
_JnxPMCurMaxQ_Object = MibTableColumn
jnxPMCurMaxQ = _JnxPMCurMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 22),
    _JnxPMCurMaxQ_Type()
)
jnxPMCurMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxQ.setUnits("0.1 dB")
_JnxPMCurAvgQ_Type = Integer32
_JnxPMCurAvgQ_Object = MibTableColumn
jnxPMCurAvgQ = _JnxPMCurAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 23),
    _JnxPMCurAvgQ_Type()
)
jnxPMCurAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgQ.setUnits("0.1 dB")
_JnxPMCurMinSNR_Type = Integer32
_JnxPMCurMinSNR_Object = MibTableColumn
jnxPMCurMinSNR = _JnxPMCurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 24),
    _JnxPMCurMinSNR_Type()
)
jnxPMCurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinSNR.setUnits("0.1 dB")
_JnxPMCurMaxSNR_Type = Integer32
_JnxPMCurMaxSNR_Object = MibTableColumn
jnxPMCurMaxSNR = _JnxPMCurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 25),
    _JnxPMCurMaxSNR_Type()
)
jnxPMCurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxSNR.setUnits("0.1 dB")
_JnxPMCurAvgSNR_Type = Integer32
_JnxPMCurAvgSNR_Object = MibTableColumn
jnxPMCurAvgSNR = _JnxPMCurAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 26),
    _JnxPMCurAvgSNR_Type()
)
jnxPMCurAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgSNR.setUnits("0.1 dB")
_JnxPMCurMinTxOutputPower_Type = Integer32
_JnxPMCurMinTxOutputPower_Object = MibTableColumn
jnxPMCurMinTxOutputPower = _JnxPMCurMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 27),
    _JnxPMCurMinTxOutputPower_Type()
)
jnxPMCurMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurMaxTxOutputPower_Type = Integer32
_JnxPMCurMaxTxOutputPower_Object = MibTableColumn
jnxPMCurMaxTxOutputPower = _JnxPMCurMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 28),
    _JnxPMCurMaxTxOutputPower_Type()
)
jnxPMCurMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurAvgTxOutputPower_Type = Integer32
_JnxPMCurAvgTxOutputPower_Object = MibTableColumn
jnxPMCurAvgTxOutputPower = _JnxPMCurAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 29),
    _JnxPMCurAvgTxOutputPower_Type()
)
jnxPMCurAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurMinRxInputPower_Type = Integer32
_JnxPMCurMinRxInputPower_Object = MibTableColumn
jnxPMCurMinRxInputPower = _JnxPMCurMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 30),
    _JnxPMCurMinRxInputPower_Type()
)
jnxPMCurMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinRxInputPower.setUnits("0.01 dbm")
_JnxPMCurMaxRxInputPower_Type = Integer32
_JnxPMCurMaxRxInputPower_Object = MibTableColumn
jnxPMCurMaxRxInputPower = _JnxPMCurMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 31),
    _JnxPMCurMaxRxInputPower_Type()
)
jnxPMCurMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMCurAvgRxInputPower_Type = Integer32
_JnxPMCurAvgRxInputPower_Object = MibTableColumn
jnxPMCurAvgRxInputPower = _JnxPMCurAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 32),
    _JnxPMCurAvgRxInputPower_Type()
)
jnxPMCurAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMCurSuspectedFlag_Type = TruthValue
_JnxPMCurSuspectedFlag_Object = MibTableColumn
jnxPMCurSuspectedFlag = _JnxPMCurSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 33),
    _JnxPMCurSuspectedFlag_Type()
)
jnxPMCurSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSuspectedFlag.setStatus("current")
_JnxPMCurSuspectReason_Type = Integer32
_JnxPMCurSuspectReason_Object = MibTableColumn
jnxPMCurSuspectReason = _JnxPMCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 34),
    _JnxPMCurSuspectReason_Type()
)
jnxPMCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSuspectReason.setStatus("current")
_JnxPMCurTxLaserBiasCurrent_Type = Integer32
_JnxPMCurTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurTxLaserBiasCurrent = _JnxPMCurTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 35),
    _JnxPMCurTxLaserBiasCurrent_Type()
)
jnxPMCurTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMinTxLaserBiasCurrent_Type = Integer32
_JnxPMCurMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMinTxLaserBiasCurrent = _JnxPMCurMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 36),
    _JnxPMCurMinTxLaserBiasCurrent_Type()
)
jnxPMCurMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMCurMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMaxTxLaserBiasCurrent = _JnxPMCurMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 37),
    _JnxPMCurMaxTxLaserBiasCurrent_Type()
)
jnxPMCurMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMCurAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurAvgTxLaserBiasCurrent = _JnxPMCurAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 38),
    _JnxPMCurAvgTxLaserBiasCurrent_Type()
)
jnxPMCurAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurTemperature_Type = Integer32
_JnxPMCurTemperature_Object = MibTableColumn
jnxPMCurTemperature = _JnxPMCurTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 39),
    _JnxPMCurTemperature_Type()
)
jnxPMCurTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTemperature.setUnits(".1 Celcius")
_JnxPMCurMinTemperature_Type = Integer32
_JnxPMCurMinTemperature_Object = MibTableColumn
jnxPMCurMinTemperature = _JnxPMCurMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 40),
    _JnxPMCurMinTemperature_Type()
)
jnxPMCurMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTemperature.setUnits(".1 Celcius")
_JnxPMCurMaxTemperature_Type = Integer32
_JnxPMCurMaxTemperature_Object = MibTableColumn
jnxPMCurMaxTemperature = _JnxPMCurMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 41),
    _JnxPMCurMaxTemperature_Type()
)
jnxPMCurMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTemperature.setUnits(".1 Celcius")
_JnxPMCurAvgTemperature_Type = Integer32
_JnxPMCurAvgTemperature_Object = MibTableColumn
jnxPMCurAvgTemperature = _JnxPMCurAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 42),
    _JnxPMCurAvgTemperature_Type()
)
jnxPMCurAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTemperature.setUnits(".1 Celcius")
_JnxPMCurCarFreqOffset_Type = Integer32
_JnxPMCurCarFreqOffset_Object = MibTableColumn
jnxPMCurCarFreqOffset = _JnxPMCurCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 43),
    _JnxPMCurCarFreqOffset_Type()
)
jnxPMCurCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurCarFreqOffset.setUnits("MHz")
_JnxPMCurMinCarFreqOffset_Type = Integer32
_JnxPMCurMinCarFreqOffset_Object = MibTableColumn
jnxPMCurMinCarFreqOffset = _JnxPMCurMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 44),
    _JnxPMCurMinCarFreqOffset_Type()
)
jnxPMCurMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinCarFreqOffset.setUnits("MHz")
_JnxPMCurMaxCarFreqOffset_Type = Integer32
_JnxPMCurMaxCarFreqOffset_Object = MibTableColumn
jnxPMCurMaxCarFreqOffset = _JnxPMCurMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 45),
    _JnxPMCurMaxCarFreqOffset_Type()
)
jnxPMCurMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxCarFreqOffset.setUnits("MHz")
_JnxPMCurAvgCarFreqOffset_Type = Integer32
_JnxPMCurAvgCarFreqOffset_Object = MibTableColumn
jnxPMCurAvgCarFreqOffset = _JnxPMCurAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 46),
    _JnxPMCurAvgCarFreqOffset_Type()
)
jnxPMCurAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgCarFreqOffset.setUnits("MHz")
_JnxPMCurRxLaserBiasCurrent_Type = Integer32
_JnxPMCurRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurRxLaserBiasCurrent = _JnxPMCurRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 47),
    _JnxPMCurRxLaserBiasCurrent_Type()
)
jnxPMCurRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMinRxLaserBiasCurrent_Type = Integer32
_JnxPMCurMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMinRxLaserBiasCurrent = _JnxPMCurMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 48),
    _JnxPMCurMinRxLaserBiasCurrent_Type()
)
jnxPMCurMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMCurMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMaxRxLaserBiasCurrent = _JnxPMCurMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 49),
    _JnxPMCurMaxRxLaserBiasCurrent_Type()
)
jnxPMCurMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMCurAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurAvgRxLaserBiasCurrent = _JnxPMCurAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 50),
    _JnxPMCurAvgRxLaserBiasCurrent_Type()
)
jnxPMCurAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxOpticsPMIntervalTable_Object = MibTable
jnxOpticsPMIntervalTable = _JnxOpticsPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalTable.setStatus("current")
_JnxOpticsPMIntervalEntry_Object = MibTableRow
jnxOpticsPMIntervalEntry = _JnxOpticsPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1)
)
jnxOpticsPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalEntry.setStatus("current")


class _JnxOpticsPMIntervalNumber_Type(Unsigned32):
    """Custom type jnxOpticsPMIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOpticsPMIntervalNumber_Type.__name__ = "Unsigned32"
_JnxOpticsPMIntervalNumber_Object = MibTableColumn
jnxOpticsPMIntervalNumber = _JnxOpticsPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 1),
    _JnxOpticsPMIntervalNumber_Type()
)
jnxOpticsPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalNumber.setStatus("current")
_JnxPMIntMinChromaticDispersion_Type = Integer32
_JnxPMIntMinChromaticDispersion_Object = MibTableColumn
jnxPMIntMinChromaticDispersion = _JnxPMIntMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 2),
    _JnxPMIntMinChromaticDispersion_Type()
)
jnxPMIntMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinChromaticDispersion.setUnits("ps/nm")
_JnxPMIntMaxChromaticDispersion_Type = Integer32
_JnxPMIntMaxChromaticDispersion_Object = MibTableColumn
jnxPMIntMaxChromaticDispersion = _JnxPMIntMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 3),
    _JnxPMIntMaxChromaticDispersion_Type()
)
jnxPMIntMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMIntAvgChromaticDispersion_Type = Integer32
_JnxPMIntAvgChromaticDispersion_Object = MibTableColumn
jnxPMIntAvgChromaticDispersion = _JnxPMIntAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 4),
    _JnxPMIntAvgChromaticDispersion_Type()
)
jnxPMIntAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMIntMinDiffGroupDelay_Type = Integer32
_JnxPMIntMinDiffGroupDelay_Object = MibTableColumn
jnxPMIntMinDiffGroupDelay = _JnxPMIntMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 5),
    _JnxPMIntMinDiffGroupDelay_Type()
)
jnxPMIntMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinDiffGroupDelay.setUnits("ps")
_JnxPMIntMaxDiffGroupDelay_Type = Integer32
_JnxPMIntMaxDiffGroupDelay_Object = MibTableColumn
jnxPMIntMaxDiffGroupDelay = _JnxPMIntMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 6),
    _JnxPMIntMaxDiffGroupDelay_Type()
)
jnxPMIntMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxDiffGroupDelay.setUnits("ps")
_JnxPMIntAvgDiffGroupDelay_Type = Integer32
_JnxPMIntAvgDiffGroupDelay_Object = MibTableColumn
jnxPMIntAvgDiffGroupDelay = _JnxPMIntAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 7),
    _JnxPMIntAvgDiffGroupDelay_Type()
)
jnxPMIntAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgDiffGroupDelay.setUnits("ps")
_JnxPMIntMinPolarState_Type = Integer32
_JnxPMIntMinPolarState_Object = MibTableColumn
jnxPMIntMinPolarState = _JnxPMIntMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 8),
    _JnxPMIntMinPolarState_Type()
)
jnxPMIntMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarState.setUnits("rad/s")
_JnxPMIntMaxPolarState_Type = Integer32
_JnxPMIntMaxPolarState_Object = MibTableColumn
jnxPMIntMaxPolarState = _JnxPMIntMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 9),
    _JnxPMIntMaxPolarState_Type()
)
jnxPMIntMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarState.setUnits("rad/s")
_JnxPMIntAvgPolarState_Type = Integer32
_JnxPMIntAvgPolarState_Object = MibTableColumn
jnxPMIntAvgPolarState = _JnxPMIntAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 10),
    _JnxPMIntAvgPolarState_Type()
)
jnxPMIntAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarState.setUnits("rad/s")
_JnxPMIntMinPolarDependentLoss_Type = Integer32
_JnxPMIntMinPolarDependentLoss_Object = MibTableColumn
jnxPMIntMinPolarDependentLoss = _JnxPMIntMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 11),
    _JnxPMIntMinPolarDependentLoss_Type()
)
jnxPMIntMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntMaxPolarDependentLoss_Type = Integer32
_JnxPMIntMaxPolarDependentLoss_Object = MibTableColumn
jnxPMIntMaxPolarDependentLoss = _JnxPMIntMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 12),
    _JnxPMIntMaxPolarDependentLoss_Type()
)
jnxPMIntMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntAvgPolarDependentLoss_Type = Integer32
_JnxPMIntAvgPolarDependentLoss_Object = MibTableColumn
jnxPMIntAvgPolarDependentLoss = _JnxPMIntAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 13),
    _JnxPMIntAvgPolarDependentLoss_Type()
)
jnxPMIntAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntMinQ_Type = Integer32
_JnxPMIntMinQ_Object = MibTableColumn
jnxPMIntMinQ = _JnxPMIntMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 14),
    _JnxPMIntMinQ_Type()
)
jnxPMIntMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinQ.setUnits("0.1 dB")
_JnxPMIntMaxQ_Type = Integer32
_JnxPMIntMaxQ_Object = MibTableColumn
jnxPMIntMaxQ = _JnxPMIntMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 15),
    _JnxPMIntMaxQ_Type()
)
jnxPMIntMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxQ.setUnits("0.1 dB")
_JnxPMIntAvgQ_Type = Integer32
_JnxPMIntAvgQ_Object = MibTableColumn
jnxPMIntAvgQ = _JnxPMIntAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 16),
    _JnxPMIntAvgQ_Type()
)
jnxPMIntAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgQ.setUnits("0.1 dB")
_JnxPMIntMinSNR_Type = Integer32
_JnxPMIntMinSNR_Object = MibTableColumn
jnxPMIntMinSNR = _JnxPMIntMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 17),
    _JnxPMIntMinSNR_Type()
)
jnxPMIntMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinSNR.setUnits("0.1 dB")
_JnxPMIntMaxSNR_Type = Integer32
_JnxPMIntMaxSNR_Object = MibTableColumn
jnxPMIntMaxSNR = _JnxPMIntMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 18),
    _JnxPMIntMaxSNR_Type()
)
jnxPMIntMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxSNR.setUnits("0.1 dB")
_JnxPMIntAvgSNR_Type = Integer32
_JnxPMIntAvgSNR_Object = MibTableColumn
jnxPMIntAvgSNR = _JnxPMIntAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 19),
    _JnxPMIntAvgSNR_Type()
)
jnxPMIntAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgSNR.setUnits("0.1 dB")
_JnxPMIntMinTxOutputPower_Type = Integer32
_JnxPMIntMinTxOutputPower_Object = MibTableColumn
jnxPMIntMinTxOutputPower = _JnxPMIntMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 20),
    _JnxPMIntMinTxOutputPower_Type()
)
jnxPMIntMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntMaxTxOutputPower_Type = Integer32
_JnxPMIntMaxTxOutputPower_Object = MibTableColumn
jnxPMIntMaxTxOutputPower = _JnxPMIntMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 21),
    _JnxPMIntMaxTxOutputPower_Type()
)
jnxPMIntMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntAvgTxOutputPower_Type = Integer32
_JnxPMIntAvgTxOutputPower_Object = MibTableColumn
jnxPMIntAvgTxOutputPower = _JnxPMIntAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 22),
    _JnxPMIntAvgTxOutputPower_Type()
)
jnxPMIntAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntMinRxInputPower_Type = Integer32
_JnxPMIntMinRxInputPower_Object = MibTableColumn
jnxPMIntMinRxInputPower = _JnxPMIntMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 23),
    _JnxPMIntMinRxInputPower_Type()
)
jnxPMIntMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinRxInputPower.setUnits("0.01 dbm")
_JnxPMIntMaxRxInputPower_Type = Integer32
_JnxPMIntMaxRxInputPower_Object = MibTableColumn
jnxPMIntMaxRxInputPower = _JnxPMIntMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 24),
    _JnxPMIntMaxRxInputPower_Type()
)
jnxPMIntMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMIntAvgRxInputPower_Type = Integer32
_JnxPMIntAvgRxInputPower_Object = MibTableColumn
jnxPMIntAvgRxInputPower = _JnxPMIntAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 25),
    _JnxPMIntAvgRxInputPower_Type()
)
jnxPMIntAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMIntTimeStamp_Type = DateAndTime
_JnxPMIntTimeStamp_Object = MibTableColumn
jnxPMIntTimeStamp = _JnxPMIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 26),
    _JnxPMIntTimeStamp_Type()
)
jnxPMIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntTimeStamp.setStatus("current")
_JnxPMIntSuspectedFlag_Type = TruthValue
_JnxPMIntSuspectedFlag_Object = MibTableColumn
jnxPMIntSuspectedFlag = _JnxPMIntSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 27),
    _JnxPMIntSuspectedFlag_Type()
)
jnxPMIntSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntSuspectedFlag.setStatus("current")
_JnxPMIntSuspectReason_Type = Integer32
_JnxPMIntSuspectReason_Object = MibTableColumn
jnxPMIntSuspectReason = _JnxPMIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 28),
    _JnxPMIntSuspectReason_Type()
)
jnxPMIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntSuspectReason.setStatus("current")
_JnxPMIntMinTxLaserBiasCurrent_Type = Integer32
_JnxPMIntMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMinTxLaserBiasCurrent = _JnxPMIntMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 29),
    _JnxPMIntMinTxLaserBiasCurrent_Type()
)
jnxPMIntMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMIntMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMaxTxLaserBiasCurrent = _JnxPMIntMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 30),
    _JnxPMIntMaxTxLaserBiasCurrent_Type()
)
jnxPMIntMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMIntAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntAvgTxLaserBiasCurrent = _JnxPMIntAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 31),
    _JnxPMIntAvgTxLaserBiasCurrent_Type()
)
jnxPMIntAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMinTemperature_Type = Integer32
_JnxPMIntMinTemperature_Object = MibTableColumn
jnxPMIntMinTemperature = _JnxPMIntMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 32),
    _JnxPMIntMinTemperature_Type()
)
jnxPMIntMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTemperature.setUnits(".1 Celcius")
_JnxPMIntMaxTemperature_Type = Integer32
_JnxPMIntMaxTemperature_Object = MibTableColumn
jnxPMIntMaxTemperature = _JnxPMIntMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 33),
    _JnxPMIntMaxTemperature_Type()
)
jnxPMIntMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTemperature.setUnits(".1 Celcius")
_JnxPMIntAvgTemperature_Type = Integer32
_JnxPMIntAvgTemperature_Object = MibTableColumn
jnxPMIntAvgTemperature = _JnxPMIntAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 34),
    _JnxPMIntAvgTemperature_Type()
)
jnxPMIntAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTemperature.setUnits(".1 Celcius")
_JnxPMIntMinCarFreqOffset_Type = Integer32
_JnxPMIntMinCarFreqOffset_Object = MibTableColumn
jnxPMIntMinCarFreqOffset = _JnxPMIntMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 35),
    _JnxPMIntMinCarFreqOffset_Type()
)
jnxPMIntMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinCarFreqOffset.setUnits("Mhz")
_JnxPMIntMaxCarFreqOffset_Type = Integer32
_JnxPMIntMaxCarFreqOffset_Object = MibTableColumn
jnxPMIntMaxCarFreqOffset = _JnxPMIntMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 36),
    _JnxPMIntMaxCarFreqOffset_Type()
)
jnxPMIntMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxCarFreqOffset.setUnits("MHz")
_JnxPMIntAvgCarFreqOffset_Type = Integer32
_JnxPMIntAvgCarFreqOffset_Object = MibTableColumn
jnxPMIntAvgCarFreqOffset = _JnxPMIntAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 37),
    _JnxPMIntAvgCarFreqOffset_Type()
)
jnxPMIntAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgCarFreqOffset.setUnits("MHz")
_JnxPMIntMinRxLaserBiasCurrent_Type = Integer32
_JnxPMIntMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMinRxLaserBiasCurrent = _JnxPMIntMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 38),
    _JnxPMIntMinRxLaserBiasCurrent_Type()
)
jnxPMIntMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMIntMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMaxRxLaserBiasCurrent = _JnxPMIntMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 39),
    _JnxPMIntMaxRxLaserBiasCurrent_Type()
)
jnxPMIntMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMIntAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntAvgRxLaserBiasCurrent = _JnxPMIntAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 40),
    _JnxPMIntAvgRxLaserBiasCurrent_Type()
)
jnxPMIntAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxOpticsPMDayTable_Object = MibTable
jnxOpticsPMDayTable = _JnxOpticsPMDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxOpticsPMDayTable.setStatus("current")
_JnxOpticsPMDayEntry_Object = MibTableRow
jnxOpticsPMDayEntry = _JnxOpticsPMDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1)
)
jnxOpticsPMDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsPMDayIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMDayEntry.setStatus("current")


class _JnxOpticsPMDayIndex_Type(Unsigned32):
    """Custom type jnxOpticsPMDayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_JnxOpticsPMDayIndex_Type.__name__ = "Unsigned32"
_JnxOpticsPMDayIndex_Object = MibTableColumn
jnxOpticsPMDayIndex = _JnxOpticsPMDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 1),
    _JnxOpticsPMDayIndex_Type()
)
jnxOpticsPMDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsPMDayIndex.setStatus("current")
_JnxPMDayMinChromaticDispersion_Type = Integer32
_JnxPMDayMinChromaticDispersion_Object = MibTableColumn
jnxPMDayMinChromaticDispersion = _JnxPMDayMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 2),
    _JnxPMDayMinChromaticDispersion_Type()
)
jnxPMDayMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinChromaticDispersion.setUnits("ps/nm")
_JnxPMDayMaxChromaticDispersion_Type = Integer32
_JnxPMDayMaxChromaticDispersion_Object = MibTableColumn
jnxPMDayMaxChromaticDispersion = _JnxPMDayMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 3),
    _JnxPMDayMaxChromaticDispersion_Type()
)
jnxPMDayMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMDayAvgChromaticDispersion_Type = Integer32
_JnxPMDayAvgChromaticDispersion_Object = MibTableColumn
jnxPMDayAvgChromaticDispersion = _JnxPMDayAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 4),
    _JnxPMDayAvgChromaticDispersion_Type()
)
jnxPMDayAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMDayMinDiffGroupDelay_Type = Integer32
_JnxPMDayMinDiffGroupDelay_Object = MibTableColumn
jnxPMDayMinDiffGroupDelay = _JnxPMDayMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 5),
    _JnxPMDayMinDiffGroupDelay_Type()
)
jnxPMDayMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinDiffGroupDelay.setUnits("ps")
_JnxPMDayMaxDiffGroupDelay_Type = Integer32
_JnxPMDayMaxDiffGroupDelay_Object = MibTableColumn
jnxPMDayMaxDiffGroupDelay = _JnxPMDayMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 6),
    _JnxPMDayMaxDiffGroupDelay_Type()
)
jnxPMDayMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxDiffGroupDelay.setUnits("ps")
_JnxPMDayAvgDiffGroupDelay_Type = Integer32
_JnxPMDayAvgDiffGroupDelay_Object = MibTableColumn
jnxPMDayAvgDiffGroupDelay = _JnxPMDayAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 7),
    _JnxPMDayAvgDiffGroupDelay_Type()
)
jnxPMDayAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgDiffGroupDelay.setUnits("ps")
_JnxPMDayMinPolarState_Type = Integer32
_JnxPMDayMinPolarState_Object = MibTableColumn
jnxPMDayMinPolarState = _JnxPMDayMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 8),
    _JnxPMDayMinPolarState_Type()
)
jnxPMDayMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarState.setUnits("rad/s")
_JnxPMDayMaxPolarState_Type = Integer32
_JnxPMDayMaxPolarState_Object = MibTableColumn
jnxPMDayMaxPolarState = _JnxPMDayMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 9),
    _JnxPMDayMaxPolarState_Type()
)
jnxPMDayMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarState.setUnits("rad/s")
_JnxPMDayAvgPolarState_Type = Integer32
_JnxPMDayAvgPolarState_Object = MibTableColumn
jnxPMDayAvgPolarState = _JnxPMDayAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 10),
    _JnxPMDayAvgPolarState_Type()
)
jnxPMDayAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarState.setUnits("rad/s")
_JnxPMDayMinPolarDependentLoss_Type = Integer32
_JnxPMDayMinPolarDependentLoss_Object = MibTableColumn
jnxPMDayMinPolarDependentLoss = _JnxPMDayMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 11),
    _JnxPMDayMinPolarDependentLoss_Type()
)
jnxPMDayMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayMaxPolarDependentLoss_Type = Integer32
_JnxPMDayMaxPolarDependentLoss_Object = MibTableColumn
jnxPMDayMaxPolarDependentLoss = _JnxPMDayMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 12),
    _JnxPMDayMaxPolarDependentLoss_Type()
)
jnxPMDayMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayAvgPolarDependentLoss_Type = Integer32
_JnxPMDayAvgPolarDependentLoss_Object = MibTableColumn
jnxPMDayAvgPolarDependentLoss = _JnxPMDayAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 13),
    _JnxPMDayAvgPolarDependentLoss_Type()
)
jnxPMDayAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayMinQ_Type = Integer32
_JnxPMDayMinQ_Object = MibTableColumn
jnxPMDayMinQ = _JnxPMDayMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 14),
    _JnxPMDayMinQ_Type()
)
jnxPMDayMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinQ.setUnits("0.1 dB")
_JnxPMDayMaxQ_Type = Integer32
_JnxPMDayMaxQ_Object = MibTableColumn
jnxPMDayMaxQ = _JnxPMDayMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 15),
    _JnxPMDayMaxQ_Type()
)
jnxPMDayMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxQ.setUnits("0.1 dB")
_JnxPMDayAvgQ_Type = Integer32
_JnxPMDayAvgQ_Object = MibTableColumn
jnxPMDayAvgQ = _JnxPMDayAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 16),
    _JnxPMDayAvgQ_Type()
)
jnxPMDayAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgQ.setUnits("0.1 dB")
_JnxPMDayMinSNR_Type = Integer32
_JnxPMDayMinSNR_Object = MibTableColumn
jnxPMDayMinSNR = _JnxPMDayMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 17),
    _JnxPMDayMinSNR_Type()
)
jnxPMDayMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinSNR.setUnits("0.1 dB")
_JnxPMDayMaxSNR_Type = Integer32
_JnxPMDayMaxSNR_Object = MibTableColumn
jnxPMDayMaxSNR = _JnxPMDayMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 18),
    _JnxPMDayMaxSNR_Type()
)
jnxPMDayMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxSNR.setUnits("0.1 dB")
_JnxPMDayAvgSNR_Type = Integer32
_JnxPMDayAvgSNR_Object = MibTableColumn
jnxPMDayAvgSNR = _JnxPMDayAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 19),
    _JnxPMDayAvgSNR_Type()
)
jnxPMDayAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgSNR.setUnits("0.1 dB")
_JnxPMDayMinTxOutputPower_Type = Integer32
_JnxPMDayMinTxOutputPower_Object = MibTableColumn
jnxPMDayMinTxOutputPower = _JnxPMDayMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 20),
    _JnxPMDayMinTxOutputPower_Type()
)
jnxPMDayMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayMaxTxOutputPower_Type = Integer32
_JnxPMDayMaxTxOutputPower_Object = MibTableColumn
jnxPMDayMaxTxOutputPower = _JnxPMDayMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 21),
    _JnxPMDayMaxTxOutputPower_Type()
)
jnxPMDayMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayAvgTxOutputPower_Type = Integer32
_JnxPMDayAvgTxOutputPower_Object = MibTableColumn
jnxPMDayAvgTxOutputPower = _JnxPMDayAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 22),
    _JnxPMDayAvgTxOutputPower_Type()
)
jnxPMDayAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayMinRxInputPower_Type = Integer32
_JnxPMDayMinRxInputPower_Object = MibTableColumn
jnxPMDayMinRxInputPower = _JnxPMDayMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 23),
    _JnxPMDayMinRxInputPower_Type()
)
jnxPMDayMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinRxInputPower.setUnits("0.01 dbm")
_JnxPMDayMaxRxInputPower_Type = Integer32
_JnxPMDayMaxRxInputPower_Object = MibTableColumn
jnxPMDayMaxRxInputPower = _JnxPMDayMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 24),
    _JnxPMDayMaxRxInputPower_Type()
)
jnxPMDayMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMDayAvgRxInputPower_Type = Integer32
_JnxPMDayAvgRxInputPower_Object = MibTableColumn
jnxPMDayAvgRxInputPower = _JnxPMDayAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 25),
    _JnxPMDayAvgRxInputPower_Type()
)
jnxPMDayAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMDayTimeStamp_Type = DateAndTime
_JnxPMDayTimeStamp_Object = MibTableColumn
jnxPMDayTimeStamp = _JnxPMDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 26),
    _JnxPMDayTimeStamp_Type()
)
jnxPMDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayTimeStamp.setStatus("current")
_JnxPMDaySuspectedFlag_Type = TruthValue
_JnxPMDaySuspectedFlag_Object = MibTableColumn
jnxPMDaySuspectedFlag = _JnxPMDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 27),
    _JnxPMDaySuspectedFlag_Type()
)
jnxPMDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDaySuspectedFlag.setStatus("current")
_JnxPMDaySuspectReason_Type = Integer32
_JnxPMDaySuspectReason_Object = MibTableColumn
jnxPMDaySuspectReason = _JnxPMDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 28),
    _JnxPMDaySuspectReason_Type()
)
jnxPMDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDaySuspectReason.setStatus("current")
_JnxPMDayMinTxLaserBiasCurrent_Type = Integer32
_JnxPMDayMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMinTxLaserBiasCurrent = _JnxPMDayMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 29),
    _JnxPMDayMinTxLaserBiasCurrent_Type()
)
jnxPMDayMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMDayMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMaxTxLaserBiasCurrent = _JnxPMDayMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 30),
    _JnxPMDayMaxTxLaserBiasCurrent_Type()
)
jnxPMDayMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMDayAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayAvgTxLaserBiasCurrent = _JnxPMDayAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 31),
    _JnxPMDayAvgTxLaserBiasCurrent_Type()
)
jnxPMDayAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMinTemperature_Type = Integer32
_JnxPMDayMinTemperature_Object = MibTableColumn
jnxPMDayMinTemperature = _JnxPMDayMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 32),
    _JnxPMDayMinTemperature_Type()
)
jnxPMDayMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTemperature.setUnits(".1 Celcius")
_JnxPMDayMaxTemperature_Type = Integer32
_JnxPMDayMaxTemperature_Object = MibTableColumn
jnxPMDayMaxTemperature = _JnxPMDayMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 33),
    _JnxPMDayMaxTemperature_Type()
)
jnxPMDayMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTemperature.setUnits(".1 Celcius")
_JnxPMDayAvgTemperature_Type = Integer32
_JnxPMDayAvgTemperature_Object = MibTableColumn
jnxPMDayAvgTemperature = _JnxPMDayAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 34),
    _JnxPMDayAvgTemperature_Type()
)
jnxPMDayAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTemperature.setUnits(".1 Celcius")
_JnxPMDayMinCarFreqOffset_Type = Integer32
_JnxPMDayMinCarFreqOffset_Object = MibTableColumn
jnxPMDayMinCarFreqOffset = _JnxPMDayMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 35),
    _JnxPMDayMinCarFreqOffset_Type()
)
jnxPMDayMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinCarFreqOffset.setUnits("Mhz")
_JnxPMDayMaxCarFreqOffset_Type = Integer32
_JnxPMDayMaxCarFreqOffset_Object = MibTableColumn
jnxPMDayMaxCarFreqOffset = _JnxPMDayMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 36),
    _JnxPMDayMaxCarFreqOffset_Type()
)
jnxPMDayMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxCarFreqOffset.setUnits("MHz")
_JnxPMDayAvgCarFreqOffset_Type = Integer32
_JnxPMDayAvgCarFreqOffset_Object = MibTableColumn
jnxPMDayAvgCarFreqOffset = _JnxPMDayAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 37),
    _JnxPMDayAvgCarFreqOffset_Type()
)
jnxPMDayAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgCarFreqOffset.setUnits("MHz")
_JnxPMDayMinRxLaserBiasCurrent_Type = Integer32
_JnxPMDayMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMinRxLaserBiasCurrent = _JnxPMDayMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 38),
    _JnxPMDayMinRxLaserBiasCurrent_Type()
)
jnxPMDayMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMDayMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMaxRxLaserBiasCurrent = _JnxPMDayMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 39),
    _JnxPMDayMaxRxLaserBiasCurrent_Type()
)
jnxPMDayMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMDayAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayAvgRxLaserBiasCurrent = _JnxPMDayAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 40),
    _JnxPMDayAvgRxLaserBiasCurrent_Type()
)
jnxPMDayAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxOpticsAlarm_ObjectIdentity = ObjectIdentity
jnxOpticsAlarm = _JnxOpticsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3)
)
_JnxOpticsNotificationTable_Object = MibTable
jnxOpticsNotificationTable = _JnxOpticsNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTable.setStatus("current")
_JnxOpticsNotificationEntry_Object = MibTableRow
jnxOpticsNotificationEntry = _JnxOpticsNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1)
)
jnxOpticsNotificationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationEntry.setStatus("current")
_JnxOpticsNotificationLocation_Type = JnxOpticsLocation
_JnxOpticsNotificationLocation_Object = MibTableColumn
jnxOpticsNotificationLocation = _JnxOpticsNotificationLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 1),
    _JnxOpticsNotificationLocation_Type()
)
jnxOpticsNotificationLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationLocation.setStatus("current")
_JnxOpticsNotificationDirection_Type = JnxOpticsDirection
_JnxOpticsNotificationDirection_Object = MibTableColumn
jnxOpticsNotificationDirection = _JnxOpticsNotificationDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 2),
    _JnxOpticsNotificationDirection_Type()
)
jnxOpticsNotificationDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationDirection.setStatus("current")
_JnxOpticsLastNotificationId_Type = JnxOpticsNotificationId
_JnxOpticsLastNotificationId_Object = MibTableColumn
jnxOpticsLastNotificationId = _JnxOpticsLastNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 3),
    _JnxOpticsLastNotificationId_Type()
)
jnxOpticsLastNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsLastNotificationId.setStatus("current")
_JnxOpticsNotificationSeverity_Type = JnxOpticsSeverity
_JnxOpticsNotificationSeverity_Object = MibTableColumn
jnxOpticsNotificationSeverity = _JnxOpticsNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 4),
    _JnxOpticsNotificationSeverity_Type()
)
jnxOpticsNotificationSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationSeverity.setStatus("current")
_JnxOpticsNotificationDate_Type = DateAndTime
_JnxOpticsNotificationDate_Object = MibTableColumn
jnxOpticsNotificationDate = _JnxOpticsNotificationDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 5),
    _JnxOpticsNotificationDate_Type()
)
jnxOpticsNotificationDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationDate.setStatus("current")
_JnxOpticsNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxOpticsNotificationPrefix = _JnxOpticsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0)
)

# Managed Objects groups


# Notification objects

jnxOpticsNotificationSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 1)
)
jnxOpticsNotificationSet.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationSet.setStatus(
        "current"
    )

jnxOpticsNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 2)
)
jnxOpticsNotificationCleared.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IFOPTICS-MIB",
    **{"JnxOpticsLocation": JnxOpticsLocation,
       "JnxOpticsDirection": JnxOpticsDirection,
       "JnxOpticsSeverity": JnxOpticsSeverity,
       "JnxOpticsServiceStateAction": JnxOpticsServiceStateAction,
       "JnxOpticsChannelSpacing": JnxOpticsChannelSpacing,
       "JnxOpticsNotificationId": JnxOpticsNotificationId,
       "jnxIfOpticsMib": jnxIfOpticsMib,
       "jnxOptics": jnxOptics,
       "jnxOpticsConfigTable": jnxOpticsConfigTable,
       "jnxOpticsConfigEntry": jnxOpticsConfigEntry,
       "jnxOpticsConfigContainerIndex": jnxOpticsConfigContainerIndex,
       "jnxOpticsConfigL1Index": jnxOpticsConfigL1Index,
       "jnxOpticsConfigL2Index": jnxOpticsConfigL2Index,
       "jnxOpticsConfigL3Index": jnxOpticsConfigL3Index,
       "jnxOpticsType": jnxOpticsType,
       "jnxLaserEnable": jnxLaserEnable,
       "jnxWavelength": jnxWavelength,
       "jnxSpacing": jnxSpacing,
       "jnxModulation": jnxModulation,
       "jnxTxOpticalPower": jnxTxOpticalPower,
       "jnxRxOpticalPower": jnxRxOpticalPower,
       "jnxModuleTempHighThresh": jnxModuleTempHighThresh,
       "jnxModuleTempLowThresh": jnxModuleTempLowThresh,
       "jnxTxPowerHighThresh": jnxTxPowerHighThresh,
       "jnxTxPowerLowThresh": jnxTxPowerLowThresh,
       "jnxRxPowerHighThresh": jnxRxPowerHighThresh,
       "jnxRxPowerLowThresh": jnxRxPowerLowThresh,
       "jnx24HourModuleTempHighThresh": jnx24HourModuleTempHighThresh,
       "jnx24HourModuleTempLowThresh": jnx24HourModuleTempLowThresh,
       "jnx24HourTxPowerHighThresh": jnx24HourTxPowerHighThresh,
       "jnx24HourTxPowerLowThresh": jnx24HourTxPowerLowThresh,
       "jnx24HourRxPowerHighThresh": jnx24HourRxPowerHighThresh,
       "jnx24HourRxPowerLowThresh": jnx24HourRxPowerLowThresh,
       "jnxRxLosPowerWarningThresh": jnxRxLosPowerWarningThresh,
       "jnxRxLosPowerAlarmThresh": jnxRxLosPowerAlarmThresh,
       "jnxOpticsCurrentStatus": jnxOpticsCurrentStatus,
       "jnxTxPowerHighEnableTCA": jnxTxPowerHighEnableTCA,
       "jnxTxPowerLowEnableTCA": jnxTxPowerLowEnableTCA,
       "jnxRxPowerHighEnableTCA": jnxRxPowerHighEnableTCA,
       "jnxRxPowerLowEnableTCA": jnxRxPowerLowEnableTCA,
       "jnxModuleTempHighEnableTCA": jnxModuleTempHighEnableTCA,
       "jnxModuleTempLowEnableTCA": jnxModuleTempLowEnableTCA,
       "jnxCarFreqOffsetHighEnableTCA": jnxCarFreqOffsetHighEnableTCA,
       "jnxCarFreqOffsetLowEnableTCA": jnxCarFreqOffsetLowEnableTCA,
       "jnxCarFreqOffsetHighThresh": jnxCarFreqOffsetHighThresh,
       "jnx24HourCarFreqOffsetHighThresh": jnx24HourCarFreqOffsetHighThresh,
       "jnxCarFreqOffsetLowThresh": jnxCarFreqOffsetLowThresh,
       "jnx24HourCarFreqOffsetLowThresh": jnx24HourCarFreqOffsetLowThresh,
       "jnxOpticsTraceToneCfgTable": jnxOpticsTraceToneCfgTable,
       "jnxOpticsTraceToneCfgEntry": jnxOpticsTraceToneCfgEntry,
       "jnxOpticsTraceToneCfgContainerIndex": jnxOpticsTraceToneCfgContainerIndex,
       "jnxOpticsTraceToneCfgL1Index": jnxOpticsTraceToneCfgL1Index,
       "jnxOpticsTraceToneCfgL2Index": jnxOpticsTraceToneCfgL2Index,
       "jnxOpticsTraceToneCfgL3Index": jnxOpticsTraceToneCfgL3Index,
       "jnxOpticsTraceToneCfgTxEnable": jnxOpticsTraceToneCfgTxEnable,
       "jnxOpticsTraceToneCfgRxEnable": jnxOpticsTraceToneCfgRxEnable,
       "jnxOpticsTraceToneCfgDestId": jnxOpticsTraceToneCfgDestId,
       "jnxOpticsTraceToneCfgTxMsg": jnxOpticsTraceToneCfgTxMsg,
       "jnxOpticsTraceToneCfgRxMsg": jnxOpticsTraceToneCfgRxMsg,
       "jnxOpticsNotificationTrigDefaultHoldtimeUp": jnxOpticsNotificationTrigDefaultHoldtimeUp,
       "jnxOpticsNotificationTrigDefaultHoldtimeDown": jnxOpticsNotificationTrigDefaultHoldtimeDown,
       "jnxOpticsNotificationTrigTable": jnxOpticsNotificationTrigTable,
       "jnxOpticsNotificationTrigEntry": jnxOpticsNotificationTrigEntry,
       "jnxOpticsNotificationTrigContainerIndex": jnxOpticsNotificationTrigContainerIndex,
       "jnxOpticsNotificationTrigL1Index": jnxOpticsNotificationTrigL1Index,
       "jnxOpticsNotificationTrigL2Index": jnxOpticsNotificationTrigL2Index,
       "jnxOpticsNotificationTrigL3Index": jnxOpticsNotificationTrigL3Index,
       "jnxOpticsNotificationTrigAlmId": jnxOpticsNotificationTrigAlmId,
       "jnxOpticsNotificationTrigSeverity": jnxOpticsNotificationTrigSeverity,
       "jnxOpticsNotificationTrigIgnore": jnxOpticsNotificationTrigIgnore,
       "jnxOpticsNotificationTrigHoldtimeUp": jnxOpticsNotificationTrigHoldtimeUp,
       "jnxOpticsNotificationTrigHoldtimeDown": jnxOpticsNotificationTrigHoldtimeDown,
       "jnxOpticsTrigServiceStateAction": jnxOpticsTrigServiceStateAction,
       "jnxOpticsClearAllPMs": jnxOpticsClearAllPMs,
       "jnxOpticsClearIfPMsTable": jnxOpticsClearIfPMsTable,
       "jnxOpticsClearIfPMsEntry": jnxOpticsClearIfPMsEntry,
       "jnxOpticsClearCurrent": jnxOpticsClearCurrent,
       "jnxOpticsClearInterfaceInterval": jnxOpticsClearInterfaceInterval,
       "jnxOpticsClearInterfaceDay": jnxOpticsClearInterfaceDay,
       "jnxOpticsClearInterfaceAll": jnxOpticsClearInterfaceAll,
       "jnxOpticsPerformanceMonitoring": jnxOpticsPerformanceMonitoring,
       "jnxOpticsPMCurrentTable": jnxOpticsPMCurrentTable,
       "jnxOpticsPMCurrentEntry": jnxOpticsPMCurrentEntry,
       "jnxPMCurChromaticDispersion": jnxPMCurChromaticDispersion,
       "jnxPMCurDiffGroupDelay": jnxPMCurDiffGroupDelay,
       "jnxPMCurPolarizationState": jnxPMCurPolarizationState,
       "jnxPMCurPolarDepLoss": jnxPMCurPolarDepLoss,
       "jnxPMCurQ": jnxPMCurQ,
       "jnxPMCurSNR": jnxPMCurSNR,
       "jnxPMCurTxOutputPower": jnxPMCurTxOutputPower,
       "jnxPMCurRxInputPower": jnxPMCurRxInputPower,
       "jnxPMCurMinChromaticDispersion": jnxPMCurMinChromaticDispersion,
       "jnxPMCurMaxChromaticDispersion": jnxPMCurMaxChromaticDispersion,
       "jnxPMCurAvgChromaticDispersion": jnxPMCurAvgChromaticDispersion,
       "jnxPMCurMinDiffGroupDelay": jnxPMCurMinDiffGroupDelay,
       "jnxPMCurMaxDiffGroupDelay": jnxPMCurMaxDiffGroupDelay,
       "jnxPMCurAvgDiffGroupDelay": jnxPMCurAvgDiffGroupDelay,
       "jnxPMCurMinPolarState": jnxPMCurMinPolarState,
       "jnxPMCurMaxPolarState": jnxPMCurMaxPolarState,
       "jnxPMCurAvgPolarState": jnxPMCurAvgPolarState,
       "jnxPMCurMinPolarDepLoss": jnxPMCurMinPolarDepLoss,
       "jnxPMCurMaxPolarDepLoss": jnxPMCurMaxPolarDepLoss,
       "jnxPMCurAvgPolarDepLoss": jnxPMCurAvgPolarDepLoss,
       "jnxPMCurMinQ": jnxPMCurMinQ,
       "jnxPMCurMaxQ": jnxPMCurMaxQ,
       "jnxPMCurAvgQ": jnxPMCurAvgQ,
       "jnxPMCurMinSNR": jnxPMCurMinSNR,
       "jnxPMCurMaxSNR": jnxPMCurMaxSNR,
       "jnxPMCurAvgSNR": jnxPMCurAvgSNR,
       "jnxPMCurMinTxOutputPower": jnxPMCurMinTxOutputPower,
       "jnxPMCurMaxTxOutputPower": jnxPMCurMaxTxOutputPower,
       "jnxPMCurAvgTxOutputPower": jnxPMCurAvgTxOutputPower,
       "jnxPMCurMinRxInputPower": jnxPMCurMinRxInputPower,
       "jnxPMCurMaxRxInputPower": jnxPMCurMaxRxInputPower,
       "jnxPMCurAvgRxInputPower": jnxPMCurAvgRxInputPower,
       "jnxPMCurSuspectedFlag": jnxPMCurSuspectedFlag,
       "jnxPMCurSuspectReason": jnxPMCurSuspectReason,
       "jnxPMCurTxLaserBiasCurrent": jnxPMCurTxLaserBiasCurrent,
       "jnxPMCurMinTxLaserBiasCurrent": jnxPMCurMinTxLaserBiasCurrent,
       "jnxPMCurMaxTxLaserBiasCurrent": jnxPMCurMaxTxLaserBiasCurrent,
       "jnxPMCurAvgTxLaserBiasCurrent": jnxPMCurAvgTxLaserBiasCurrent,
       "jnxPMCurTemperature": jnxPMCurTemperature,
       "jnxPMCurMinTemperature": jnxPMCurMinTemperature,
       "jnxPMCurMaxTemperature": jnxPMCurMaxTemperature,
       "jnxPMCurAvgTemperature": jnxPMCurAvgTemperature,
       "jnxPMCurCarFreqOffset": jnxPMCurCarFreqOffset,
       "jnxPMCurMinCarFreqOffset": jnxPMCurMinCarFreqOffset,
       "jnxPMCurMaxCarFreqOffset": jnxPMCurMaxCarFreqOffset,
       "jnxPMCurAvgCarFreqOffset": jnxPMCurAvgCarFreqOffset,
       "jnxPMCurRxLaserBiasCurrent": jnxPMCurRxLaserBiasCurrent,
       "jnxPMCurMinRxLaserBiasCurrent": jnxPMCurMinRxLaserBiasCurrent,
       "jnxPMCurMaxRxLaserBiasCurrent": jnxPMCurMaxRxLaserBiasCurrent,
       "jnxPMCurAvgRxLaserBiasCurrent": jnxPMCurAvgRxLaserBiasCurrent,
       "jnxOpticsPMIntervalTable": jnxOpticsPMIntervalTable,
       "jnxOpticsPMIntervalEntry": jnxOpticsPMIntervalEntry,
       "jnxOpticsPMIntervalNumber": jnxOpticsPMIntervalNumber,
       "jnxPMIntMinChromaticDispersion": jnxPMIntMinChromaticDispersion,
       "jnxPMIntMaxChromaticDispersion": jnxPMIntMaxChromaticDispersion,
       "jnxPMIntAvgChromaticDispersion": jnxPMIntAvgChromaticDispersion,
       "jnxPMIntMinDiffGroupDelay": jnxPMIntMinDiffGroupDelay,
       "jnxPMIntMaxDiffGroupDelay": jnxPMIntMaxDiffGroupDelay,
       "jnxPMIntAvgDiffGroupDelay": jnxPMIntAvgDiffGroupDelay,
       "jnxPMIntMinPolarState": jnxPMIntMinPolarState,
       "jnxPMIntMaxPolarState": jnxPMIntMaxPolarState,
       "jnxPMIntAvgPolarState": jnxPMIntAvgPolarState,
       "jnxPMIntMinPolarDependentLoss": jnxPMIntMinPolarDependentLoss,
       "jnxPMIntMaxPolarDependentLoss": jnxPMIntMaxPolarDependentLoss,
       "jnxPMIntAvgPolarDependentLoss": jnxPMIntAvgPolarDependentLoss,
       "jnxPMIntMinQ": jnxPMIntMinQ,
       "jnxPMIntMaxQ": jnxPMIntMaxQ,
       "jnxPMIntAvgQ": jnxPMIntAvgQ,
       "jnxPMIntMinSNR": jnxPMIntMinSNR,
       "jnxPMIntMaxSNR": jnxPMIntMaxSNR,
       "jnxPMIntAvgSNR": jnxPMIntAvgSNR,
       "jnxPMIntMinTxOutputPower": jnxPMIntMinTxOutputPower,
       "jnxPMIntMaxTxOutputPower": jnxPMIntMaxTxOutputPower,
       "jnxPMIntAvgTxOutputPower": jnxPMIntAvgTxOutputPower,
       "jnxPMIntMinRxInputPower": jnxPMIntMinRxInputPower,
       "jnxPMIntMaxRxInputPower": jnxPMIntMaxRxInputPower,
       "jnxPMIntAvgRxInputPower": jnxPMIntAvgRxInputPower,
       "jnxPMIntTimeStamp": jnxPMIntTimeStamp,
       "jnxPMIntSuspectedFlag": jnxPMIntSuspectedFlag,
       "jnxPMIntSuspectReason": jnxPMIntSuspectReason,
       "jnxPMIntMinTxLaserBiasCurrent": jnxPMIntMinTxLaserBiasCurrent,
       "jnxPMIntMaxTxLaserBiasCurrent": jnxPMIntMaxTxLaserBiasCurrent,
       "jnxPMIntAvgTxLaserBiasCurrent": jnxPMIntAvgTxLaserBiasCurrent,
       "jnxPMIntMinTemperature": jnxPMIntMinTemperature,
       "jnxPMIntMaxTemperature": jnxPMIntMaxTemperature,
       "jnxPMIntAvgTemperature": jnxPMIntAvgTemperature,
       "jnxPMIntMinCarFreqOffset": jnxPMIntMinCarFreqOffset,
       "jnxPMIntMaxCarFreqOffset": jnxPMIntMaxCarFreqOffset,
       "jnxPMIntAvgCarFreqOffset": jnxPMIntAvgCarFreqOffset,
       "jnxPMIntMinRxLaserBiasCurrent": jnxPMIntMinRxLaserBiasCurrent,
       "jnxPMIntMaxRxLaserBiasCurrent": jnxPMIntMaxRxLaserBiasCurrent,
       "jnxPMIntAvgRxLaserBiasCurrent": jnxPMIntAvgRxLaserBiasCurrent,
       "jnxOpticsPMDayTable": jnxOpticsPMDayTable,
       "jnxOpticsPMDayEntry": jnxOpticsPMDayEntry,
       "jnxOpticsPMDayIndex": jnxOpticsPMDayIndex,
       "jnxPMDayMinChromaticDispersion": jnxPMDayMinChromaticDispersion,
       "jnxPMDayMaxChromaticDispersion": jnxPMDayMaxChromaticDispersion,
       "jnxPMDayAvgChromaticDispersion": jnxPMDayAvgChromaticDispersion,
       "jnxPMDayMinDiffGroupDelay": jnxPMDayMinDiffGroupDelay,
       "jnxPMDayMaxDiffGroupDelay": jnxPMDayMaxDiffGroupDelay,
       "jnxPMDayAvgDiffGroupDelay": jnxPMDayAvgDiffGroupDelay,
       "jnxPMDayMinPolarState": jnxPMDayMinPolarState,
       "jnxPMDayMaxPolarState": jnxPMDayMaxPolarState,
       "jnxPMDayAvgPolarState": jnxPMDayAvgPolarState,
       "jnxPMDayMinPolarDependentLoss": jnxPMDayMinPolarDependentLoss,
       "jnxPMDayMaxPolarDependentLoss": jnxPMDayMaxPolarDependentLoss,
       "jnxPMDayAvgPolarDependentLoss": jnxPMDayAvgPolarDependentLoss,
       "jnxPMDayMinQ": jnxPMDayMinQ,
       "jnxPMDayMaxQ": jnxPMDayMaxQ,
       "jnxPMDayAvgQ": jnxPMDayAvgQ,
       "jnxPMDayMinSNR": jnxPMDayMinSNR,
       "jnxPMDayMaxSNR": jnxPMDayMaxSNR,
       "jnxPMDayAvgSNR": jnxPMDayAvgSNR,
       "jnxPMDayMinTxOutputPower": jnxPMDayMinTxOutputPower,
       "jnxPMDayMaxTxOutputPower": jnxPMDayMaxTxOutputPower,
       "jnxPMDayAvgTxOutputPower": jnxPMDayAvgTxOutputPower,
       "jnxPMDayMinRxInputPower": jnxPMDayMinRxInputPower,
       "jnxPMDayMaxRxInputPower": jnxPMDayMaxRxInputPower,
       "jnxPMDayAvgRxInputPower": jnxPMDayAvgRxInputPower,
       "jnxPMDayTimeStamp": jnxPMDayTimeStamp,
       "jnxPMDaySuspectedFlag": jnxPMDaySuspectedFlag,
       "jnxPMDaySuspectReason": jnxPMDaySuspectReason,
       "jnxPMDayMinTxLaserBiasCurrent": jnxPMDayMinTxLaserBiasCurrent,
       "jnxPMDayMaxTxLaserBiasCurrent": jnxPMDayMaxTxLaserBiasCurrent,
       "jnxPMDayAvgTxLaserBiasCurrent": jnxPMDayAvgTxLaserBiasCurrent,
       "jnxPMDayMinTemperature": jnxPMDayMinTemperature,
       "jnxPMDayMaxTemperature": jnxPMDayMaxTemperature,
       "jnxPMDayAvgTemperature": jnxPMDayAvgTemperature,
       "jnxPMDayMinCarFreqOffset": jnxPMDayMinCarFreqOffset,
       "jnxPMDayMaxCarFreqOffset": jnxPMDayMaxCarFreqOffset,
       "jnxPMDayAvgCarFreqOffset": jnxPMDayAvgCarFreqOffset,
       "jnxPMDayMinRxLaserBiasCurrent": jnxPMDayMinRxLaserBiasCurrent,
       "jnxPMDayMaxRxLaserBiasCurrent": jnxPMDayMaxRxLaserBiasCurrent,
       "jnxPMDayAvgRxLaserBiasCurrent": jnxPMDayAvgRxLaserBiasCurrent,
       "jnxOpticsAlarm": jnxOpticsAlarm,
       "jnxOpticsNotificationTable": jnxOpticsNotificationTable,
       "jnxOpticsNotificationEntry": jnxOpticsNotificationEntry,
       "jnxOpticsNotificationLocation": jnxOpticsNotificationLocation,
       "jnxOpticsNotificationDirection": jnxOpticsNotificationDirection,
       "jnxOpticsLastNotificationId": jnxOpticsLastNotificationId,
       "jnxOpticsNotificationSeverity": jnxOpticsNotificationSeverity,
       "jnxOpticsNotificationDate": jnxOpticsNotificationDate,
       "jnxOpticsNotificationPrefix": jnxOpticsNotificationPrefix,
       "jnxOpticsNotificationSet": jnxOpticsNotificationSet,
       "jnxOpticsNotificationCleared": jnxOpticsNotificationCleared}
)
