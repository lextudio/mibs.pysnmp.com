# SNMP MIB module (JNX-OPT-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-OPT-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(JnxoptIfDirectionality,
 jnxoptIfMibModule,
 jnxoptIfOChConfigEntry,
 jnxoptIfOChSinkCurrentEntry) = mibBuilder.importSymbols(
    "JNX-OPT-IF-MIB",
    "JnxoptIfDirectionality",
    "jnxoptIfMibModule",
    "jnxoptIfOChConfigEntry",
    "jnxoptIfOChSinkCurrentEntry")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxoptIfExtMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3)
)
jnxoptIfExtMibModule.setRevisions(
        ("2012-04-25 00:00",
         "2013-01-25 00:00",
         "2013-02-27 00:00",
         "2013-11-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxoptIfChannelSpacing(Integer32, TextualConvention):
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



class JnxoptIfBitRateLineCoding(Integer32, TextualConvention):
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
        *(("rate100G", 4),
          ("rate10G", 2),
          ("rate2point5G", 1),
          ("rate400G", 5),
          ("rate40G", 3))
    )



class JnxoptIfFiberTypeRecommendation(Integer32, TextualConvention):
    status = "current"
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
        *(("g652", 1),
          ("g653", 2),
          ("g654", 3),
          ("g655", 4),
          ("g656", 5),
          ("g657", 6))
    )



class JnxoptIfFiberTypeCategory(Integer32, TextualConvention):
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
        *(("categoryA", 1),
          ("categoryB", 2),
          ("categoryC", 3),
          ("categoryD", 4),
          ("categoryE", 5))
    )



class JnxoptIfOTNType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("farEnd", 2),
          ("nearEnd", 1))
    )



class JnxoptIfOTNDirection(Integer32, TextualConvention):
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



class JnxoptIfOTNLayer(Integer32, TextualConvention):
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
        *(("jnxoptIfODUkLayer", 2),
          ("jnxoptIfOTUkLayer", 1),
          ("jnxoptIfTCMSubLayer", 3))
    )



class JnxoptIfOTNOChAlarms(Integer32, TextualConvention):
    status = "current"
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("jnxoptIf15MinThUnCorrectedWordsTCA", 17),
          ("jnxoptIf15MinThreshBBETCA", 12),
          ("jnxoptIf15MinThreshBip8TCA", 16),
          ("jnxoptIf15MinThreshESTCA", 13),
          ("jnxoptIf15MinThreshPreFECBERTCA", 18),
          ("jnxoptIf15MinThreshSESTCA", 14),
          ("jnxoptIf15MinThreshUASTCA", 15),
          ("jnxoptIf24HourThreshBBETCA", 19),
          ("jnxoptIf24HourThreshBip8TCA", 23),
          ("jnxoptIf24HourThreshESTCA", 20),
          ("jnxoptIf24HourThreshPreFECBERTCA", 24),
          ("jnxoptIf24HourThreshSESTCA", 21),
          ("jnxoptIf24HourThreshUASTCA", 22),
          ("jnxoptIfOtnLofAlarm", 2),
          ("jnxoptIfOtnLomAlarm", 3),
          ("jnxoptIfOtnLosAlarm", 1),
          ("jnxoptIfOtnNoAlarm", 0),
          ("jnxoptIfOtuAisAlarm", 25),
          ("jnxoptIfOtuBdiAlarm", 5),
          ("jnxoptIfOtuBiaeAlarm", 8),
          ("jnxoptIfOtuDegAlarm", 10),
          ("jnxoptIfOtuFecExcessiveErrsAlarm", 11),
          ("jnxoptIfOtuIaeAlarm", 7),
          ("jnxoptIfOtuSsfAlarm", 4),
          ("jnxoptIfOtuTimAlarm", 6),
          ("jnxoptIfOtuTsfAlarm", 9))
    )



class JnxoptIfOTNODUkTcmAlarms(Integer32, TextualConvention):
    status = "current"
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("jnxoptIfOdukPtmAlarm", 17),
          ("jnxoptIfOdukTcm15MinThreshBBETCA", 11),
          ("jnxoptIfOdukTcm15MinThreshBip8TCA", 15),
          ("jnxoptIfOdukTcm15MinThreshESTCA", 12),
          ("jnxoptIfOdukTcm15MinThreshSESTCA", 13),
          ("jnxoptIfOdukTcm15MinThreshUASTCA", 14),
          ("jnxoptIfOdukTcm24HourThreshBBETCA", 18),
          ("jnxoptIfOdukTcm24HourThreshBip8TCA", 22),
          ("jnxoptIfOdukTcm24HourThreshESTCA", 19),
          ("jnxoptIfOdukTcm24HourThreshSESTCA", 20),
          ("jnxoptIfOdukTcm24HourThreshUASTCA", 21),
          ("jnxoptIfOdukTcmAisAlarm", 16),
          ("jnxoptIfOdukTcmBdiAlarm", 3),
          ("jnxoptIfOdukTcmCSfAlarm", 8),
          ("jnxoptIfOdukTcmDegAlarm", 5),
          ("jnxoptIfOdukTcmIaeAlarm", 6),
          ("jnxoptIfOdukTcmLTCAlarm", 7),
          ("jnxoptIfOdukTcmLckAlarm", 2),
          ("jnxoptIfOdukTcmOciAlarm", 1),
          ("jnxoptIfOdukTcmSSfAlarm", 9),
          ("jnxoptIfOdukTcmTSfAlarm", 10),
          ("jnxoptIfOdukTcmTimAlarm", 4),
          ("jnxoptIfOtnOdukTcmNoAlarm", 0))
    )



class JnxoptIfOTNAlarmSeverity(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_JnxoptIfOTNNotifications_ObjectIdentity = ObjectIdentity
jnxoptIfOTNNotifications = _JnxoptIfOTNNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 0)
)
_JnxoptIfOPSmEntry_ObjectIdentity = ObjectIdentity
jnxoptIfOPSmEntry = _JnxoptIfOPSmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1)
)
_JnxoptIfOPSmConfigTable_Object = MibTable
jnxoptIfOPSmConfigTable = _JnxoptIfOPSmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOPSmConfigTable.setStatus("current")
_JnxoptIfOPSmConfigEntry_Object = MibTableRow
jnxoptIfOPSmConfigEntry = _JnxoptIfOPSmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1, 1, 1)
)
jnxoptIfOPSmConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOPSmConfigEntry.setStatus("current")
_JnxoptIfOPSmDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOPSmDirectionality_Object = MibTableColumn
jnxoptIfOPSmDirectionality = _JnxoptIfOPSmDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1, 1, 1, 1),
    _JnxoptIfOPSmDirectionality_Type()
)
jnxoptIfOPSmDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOPSmDirectionality.setStatus("current")
_JnxoptIfOPSmFiberTypeRecommendation_Type = JnxoptIfFiberTypeRecommendation
_JnxoptIfOPSmFiberTypeRecommendation_Object = MibTableColumn
jnxoptIfOPSmFiberTypeRecommendation = _JnxoptIfOPSmFiberTypeRecommendation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1, 1, 1, 2),
    _JnxoptIfOPSmFiberTypeRecommendation_Type()
)
jnxoptIfOPSmFiberTypeRecommendation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOPSmFiberTypeRecommendation.setStatus("current")
_JnxoptIfOPSmFiberTypeCategory_Type = JnxoptIfFiberTypeCategory
_JnxoptIfOPSmFiberTypeCategory_Object = MibTableColumn
jnxoptIfOPSmFiberTypeCategory = _JnxoptIfOPSmFiberTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 1, 1, 1, 3),
    _JnxoptIfOPSmFiberTypeCategory_Type()
)
jnxoptIfOPSmFiberTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOPSmFiberTypeCategory.setStatus("current")
_JnxoptIfOChSrcSinkGroup_ObjectIdentity = ObjectIdentity
jnxoptIfOChSrcSinkGroup = _JnxoptIfOChSrcSinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2)
)
_JnxoptIfOChConfigExtTable_Object = MibTable
jnxoptIfOChConfigExtTable = _JnxoptIfOChConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChConfigExtTable.setStatus("current")
_JnxoptIfOChConfigExtEntry_Object = MibTableRow
jnxoptIfOChConfigExtEntry = _JnxoptIfOChConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChConfigExtEntry.setStatus("current")
_JnxoptIfOChMiminumChannelSpacing_Type = JnxoptIfChannelSpacing
_JnxoptIfOChMiminumChannelSpacing_Object = MibTableColumn
jnxoptIfOChMiminumChannelSpacing = _JnxoptIfOChMiminumChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 1),
    _JnxoptIfOChMiminumChannelSpacing_Type()
)
jnxoptIfOChMiminumChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMiminumChannelSpacing.setStatus("current")
_JnxoptIfOChBitRateLineCoding_Type = JnxoptIfBitRateLineCoding
_JnxoptIfOChBitRateLineCoding_Object = MibTableColumn
jnxoptIfOChBitRateLineCoding = _JnxoptIfOChBitRateLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 2),
    _JnxoptIfOChBitRateLineCoding_Type()
)
jnxoptIfOChBitRateLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChBitRateLineCoding.setStatus("current")
_JnxoptIfOChFEC_Type = Unsigned32
_JnxoptIfOChFEC_Object = MibTableColumn
jnxoptIfOChFEC = _JnxoptIfOChFEC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 3),
    _JnxoptIfOChFEC_Type()
)
jnxoptIfOChFEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChFEC.setStatus("current")
_JnxoptIfOChSinkMaximumBERMantissa_Type = Unsigned32
_JnxoptIfOChSinkMaximumBERMantissa_Object = MibTableColumn
jnxoptIfOChSinkMaximumBERMantissa = _JnxoptIfOChSinkMaximumBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 4),
    _JnxoptIfOChSinkMaximumBERMantissa_Type()
)
jnxoptIfOChSinkMaximumBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMaximumBERMantissa.setStatus("current")
_JnxoptIfOChSinkMaximumBERExponent_Type = Unsigned32
_JnxoptIfOChSinkMaximumBERExponent_Object = MibTableColumn
jnxoptIfOChSinkMaximumBERExponent = _JnxoptIfOChSinkMaximumBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 5),
    _JnxoptIfOChSinkMaximumBERExponent_Type()
)
jnxoptIfOChSinkMaximumBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMaximumBERExponent.setStatus("current")
_JnxoptIfOChMinWavelength_Type = Unsigned32
_JnxoptIfOChMinWavelength_Object = MibTableColumn
jnxoptIfOChMinWavelength = _JnxoptIfOChMinWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 6),
    _JnxoptIfOChMinWavelength_Type()
)
jnxoptIfOChMinWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMinWavelength.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMinWavelength.setUnits("0.01 nm")
_JnxoptIfOChMaxWavelength_Type = Unsigned32
_JnxoptIfOChMaxWavelength_Object = MibTableColumn
jnxoptIfOChMaxWavelength = _JnxoptIfOChMaxWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 7),
    _JnxoptIfOChMaxWavelength_Type()
)
jnxoptIfOChMaxWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMaxWavelength.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMaxWavelength.setUnits("0.01 nm")
_JnxoptIfOChWavelength_Type = Unsigned32
_JnxoptIfOChWavelength_Object = MibTableColumn
jnxoptIfOChWavelength = _JnxoptIfOChWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 8),
    _JnxoptIfOChWavelength_Type()
)
jnxoptIfOChWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChWavelength.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChWavelength.setUnits("0.01 nm")


class _JnxoptIfOChVendorTransceiverClass_Type(DisplayString):
    """Custom type jnxoptIfOChVendorTransceiverClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxoptIfOChVendorTransceiverClass_Type.__name__ = "DisplayString"
_JnxoptIfOChVendorTransceiverClass_Object = MibTableColumn
jnxoptIfOChVendorTransceiverClass = _JnxoptIfOChVendorTransceiverClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 9),
    _JnxoptIfOChVendorTransceiverClass_Type()
)
jnxoptIfOChVendorTransceiverClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChVendorTransceiverClass.setStatus("current")


class _JnxoptIfOChOpticalInterfaceApplicationCode_Type(DisplayString):
    """Custom type jnxoptIfOChOpticalInterfaceApplicationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxoptIfOChOpticalInterfaceApplicationCode_Type.__name__ = "DisplayString"
_JnxoptIfOChOpticalInterfaceApplicationCode_Object = MibTableColumn
jnxoptIfOChOpticalInterfaceApplicationCode = _JnxoptIfOChOpticalInterfaceApplicationCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 10),
    _JnxoptIfOChOpticalInterfaceApplicationCode_Type()
)
jnxoptIfOChOpticalInterfaceApplicationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChOpticalInterfaceApplicationCode.setStatus("current")


class _JnxoptIfOChLaserAdminState_Type(Integer32):
    """Custom type jnxoptIfOChLaserAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JnxoptIfOChLaserAdminState_Type.__name__ = "Integer32"
_JnxoptIfOChLaserAdminState_Object = MibTableColumn
jnxoptIfOChLaserAdminState = _JnxoptIfOChLaserAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 11),
    _JnxoptIfOChLaserAdminState_Type()
)
jnxoptIfOChLaserAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChLaserAdminState.setStatus("current")


class _JnxoptIfOChLaserOperationalState_Type(Integer32):
    """Custom type jnxoptIfOChLaserOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("disabled", 0),
          ("enabled", 1),
          ("fault", 2))
    )


_JnxoptIfOChLaserOperationalState_Type.__name__ = "Integer32"
_JnxoptIfOChLaserOperationalState_Object = MibTableColumn
jnxoptIfOChLaserOperationalState = _JnxoptIfOChLaserOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 12),
    _JnxoptIfOChLaserOperationalState_Type()
)
jnxoptIfOChLaserOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChLaserOperationalState.setStatus("current")


class _JnxoptIfOChAdminState_Type(Integer32):
    """Custom type jnxoptIfOChAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_JnxoptIfOChAdminState_Type.__name__ = "Integer32"
_JnxoptIfOChAdminState_Object = MibTableColumn
jnxoptIfOChAdminState = _JnxoptIfOChAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 13),
    _JnxoptIfOChAdminState_Type()
)
jnxoptIfOChAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChAdminState.setStatus("current")


class _JnxoptIfOChOperationalState_Type(Integer32):
    """Custom type jnxoptIfOChOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("disabled", 0),
          ("enabled", 1),
          ("fault", 2))
    )


_JnxoptIfOChOperationalState_Type.__name__ = "Integer32"
_JnxoptIfOChOperationalState_Object = MibTableColumn
jnxoptIfOChOperationalState = _JnxoptIfOChOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 1, 1, 14),
    _JnxoptIfOChOperationalState_Type()
)
jnxoptIfOChOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChOperationalState.setStatus("current")
_JnxoptIfOChSrcConfigTable_Object = MibTable
jnxoptIfOChSrcConfigTable = _JnxoptIfOChSrcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcConfigTable.setStatus("current")
_JnxoptIfOChSrcConfigEntry_Object = MibTableRow
jnxoptIfOChSrcConfigEntry = _JnxoptIfOChSrcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1)
)
jnxoptIfOChSrcConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcConfigEntry.setStatus("current")
_JnxoptIfOChMinimumMeanChannelOutputPower_Type = Integer32
_JnxoptIfOChMinimumMeanChannelOutputPower_Object = MibTableColumn
jnxoptIfOChMinimumMeanChannelOutputPower = _JnxoptIfOChMinimumMeanChannelOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 1),
    _JnxoptIfOChMinimumMeanChannelOutputPower_Type()
)
jnxoptIfOChMinimumMeanChannelOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMinimumMeanChannelOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMinimumMeanChannelOutputPower.setUnits("0.01 dbm")
_JnxoptIfOChMaximumMeanChannelOutputPower_Type = Integer32
_JnxoptIfOChMaximumMeanChannelOutputPower_Object = MibTableColumn
jnxoptIfOChMaximumMeanChannelOutputPower = _JnxoptIfOChMaximumMeanChannelOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 2),
    _JnxoptIfOChMaximumMeanChannelOutputPower_Type()
)
jnxoptIfOChMaximumMeanChannelOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumMeanChannelOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumMeanChannelOutputPower.setUnits("0.01 dbm")
_JnxoptIfOChMinimumCentralFrequency_Type = Unsigned32
_JnxoptIfOChMinimumCentralFrequency_Object = MibTableColumn
jnxoptIfOChMinimumCentralFrequency = _JnxoptIfOChMinimumCentralFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 3),
    _JnxoptIfOChMinimumCentralFrequency_Type()
)
jnxoptIfOChMinimumCentralFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMinimumCentralFrequency.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMinimumCentralFrequency.setUnits("0.01 THz")
_JnxoptIfOChMaximumCentralFrequency_Type = Unsigned32
_JnxoptIfOChMaximumCentralFrequency_Object = MibTableColumn
jnxoptIfOChMaximumCentralFrequency = _JnxoptIfOChMaximumCentralFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 4),
    _JnxoptIfOChMaximumCentralFrequency_Type()
)
jnxoptIfOChMaximumCentralFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumCentralFrequency.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumCentralFrequency.setUnits("0.01 THz")
_JnxoptIfOChMaximumSpectralExcursion_Type = Unsigned32
_JnxoptIfOChMaximumSpectralExcursion_Object = MibTableColumn
jnxoptIfOChMaximumSpectralExcursion = _JnxoptIfOChMaximumSpectralExcursion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 5),
    _JnxoptIfOChMaximumSpectralExcursion_Type()
)
jnxoptIfOChMaximumSpectralExcursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumSpectralExcursion.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumSpectralExcursion.setUnits("0.1 GHz")
_JnxoptIfOChMaximumTxDispersionOSNRPenalty_Type = Integer32
_JnxoptIfOChMaximumTxDispersionOSNRPenalty_Object = MibTableColumn
jnxoptIfOChMaximumTxDispersionOSNRPenalty = _JnxoptIfOChMaximumTxDispersionOSNRPenalty_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 2, 1, 6),
    _JnxoptIfOChMaximumTxDispersionOSNRPenalty_Type()
)
jnxoptIfOChMaximumTxDispersionOSNRPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumTxDispersionOSNRPenalty.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChMaximumTxDispersionOSNRPenalty.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkConfigTable_Object = MibTable
jnxoptIfOChSrcSinkConfigTable = _JnxoptIfOChSrcSinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkConfigTable.setStatus("current")
_JnxoptIfOChSrcSinkConfigEntry_Object = MibTableRow
jnxoptIfOChSrcSinkConfigEntry = _JnxoptIfOChSrcSinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1)
)
jnxoptIfOChSrcSinkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkConfigEntry.setStatus("current")
_JnxoptIfOChSrcSinkMinimumChromaticDispersion_Type = Integer32
_JnxoptIfOChSrcSinkMinimumChromaticDispersion_Object = MibTableColumn
jnxoptIfOChSrcSinkMinimumChromaticDispersion = _JnxoptIfOChSrcSinkMinimumChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 1),
    _JnxoptIfOChSrcSinkMinimumChromaticDispersion_Type()
)
jnxoptIfOChSrcSinkMinimumChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMinimumChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMinimumChromaticDispersion.setUnits("ps/nm")
_JnxoptIfOChSrcSinkMaximumChromaticDispersion_Type = Integer32
_JnxoptIfOChSrcSinkMaximumChromaticDispersion_Object = MibTableColumn
jnxoptIfOChSrcSinkMaximumChromaticDispersion = _JnxoptIfOChSrcSinkMaximumChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 2),
    _JnxoptIfOChSrcSinkMaximumChromaticDispersion_Type()
)
jnxoptIfOChSrcSinkMaximumChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumChromaticDispersion.setUnits("ps/nm")
_JnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss_Type = Integer32
_JnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss_Object = MibTableColumn
jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss = _JnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 3),
    _JnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss_Type()
)
jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink_Type = Integer32
_JnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink_Object = MibTableColumn
jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink = _JnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 4),
    _JnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink_Type()
)
jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkMaximumDifferentialGroupDelay_Type = Integer32
_JnxoptIfOChSrcSinkMaximumDifferentialGroupDelay_Object = MibTableColumn
jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay = _JnxoptIfOChSrcSinkMaximumDifferentialGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 5),
    _JnxoptIfOChSrcSinkMaximumDifferentialGroupDelay_Type()
)
jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay.setUnits("ps")
_JnxoptIfOChSrcSinkMaximumPolarisationDependentLoss_Type = Integer32
_JnxoptIfOChSrcSinkMaximumPolarisationDependentLoss_Object = MibTableColumn
jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss = _JnxoptIfOChSrcSinkMaximumPolarisationDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 6),
    _JnxoptIfOChSrcSinkMaximumPolarisationDependentLoss_Type()
)
jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkMaximumInterChannelCrosstalk_Type = Integer32
_JnxoptIfOChSrcSinkMaximumInterChannelCrosstalk_Object = MibTableColumn
jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk = _JnxoptIfOChSrcSinkMaximumInterChannelCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 7),
    _JnxoptIfOChSrcSinkMaximumInterChannelCrosstalk_Type()
)
jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkInterFerometricCrosstalk_Type = Integer32
_JnxoptIfOChSrcSinkInterFerometricCrosstalk_Object = MibTableColumn
jnxoptIfOChSrcSinkInterFerometricCrosstalk = _JnxoptIfOChSrcSinkInterFerometricCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 8),
    _JnxoptIfOChSrcSinkInterFerometricCrosstalk_Type()
)
jnxoptIfOChSrcSinkInterFerometricCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkInterFerometricCrosstalk.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkInterFerometricCrosstalk.setUnits("0.1 dB")
_JnxoptIfOChSrcSinkOpticalPathOSNRPenalty_Type = Integer32
_JnxoptIfOChSrcSinkOpticalPathOSNRPenalty_Object = MibTableColumn
jnxoptIfOChSrcSinkOpticalPathOSNRPenalty = _JnxoptIfOChSrcSinkOpticalPathOSNRPenalty_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 3, 1, 9),
    _JnxoptIfOChSrcSinkOpticalPathOSNRPenalty_Type()
)
jnxoptIfOChSrcSinkOpticalPathOSNRPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkOpticalPathOSNRPenalty.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcSinkOpticalPathOSNRPenalty.setUnits("0.1 dB")
_JnxoptIfOChSinkConfigTable_Object = MibTable
jnxoptIfOChSinkConfigTable = _JnxoptIfOChSinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkConfigTable.setStatus("current")
_JnxoptIfOChSinkConfigEntry_Object = MibTableRow
jnxoptIfOChSinkConfigEntry = _JnxoptIfOChSinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4, 1)
)
jnxoptIfOChSinkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkConfigEntry.setStatus("current")
_JnxoptIfOChSinkMinimumMeanIntputPower_Type = Integer32
_JnxoptIfOChSinkMinimumMeanIntputPower_Object = MibTableColumn
jnxoptIfOChSinkMinimumMeanIntputPower = _JnxoptIfOChSinkMinimumMeanIntputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4, 1, 1),
    _JnxoptIfOChSinkMinimumMeanIntputPower_Type()
)
jnxoptIfOChSinkMinimumMeanIntputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMinimumMeanIntputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMinimumMeanIntputPower.setUnits("0.01 dbm")
_JnxoptIfOChSinkMaximumMeanIntputPower_Type = Integer32
_JnxoptIfOChSinkMaximumMeanIntputPower_Object = MibTableColumn
jnxoptIfOChSinkMaximumMeanIntputPower = _JnxoptIfOChSinkMaximumMeanIntputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4, 1, 2),
    _JnxoptIfOChSinkMaximumMeanIntputPower_Type()
)
jnxoptIfOChSinkMaximumMeanIntputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMaximumMeanIntputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMaximumMeanIntputPower.setUnits("0.01 dbm")
_JnxoptIfOChSinkMinimumOSNR_Type = Integer32
_JnxoptIfOChSinkMinimumOSNR_Object = MibTableColumn
jnxoptIfOChSinkMinimumOSNR = _JnxoptIfOChSinkMinimumOSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4, 1, 3),
    _JnxoptIfOChSinkMinimumOSNR_Type()
)
jnxoptIfOChSinkMinimumOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMinimumOSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkMinimumOSNR.setUnits("0.1 dB")
_JnxoptIfOChSinkOSNRTolerance_Type = Integer32
_JnxoptIfOChSinkOSNRTolerance_Object = MibTableColumn
jnxoptIfOChSinkOSNRTolerance = _JnxoptIfOChSinkOSNRTolerance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 2, 4, 1, 4),
    _JnxoptIfOChSinkOSNRTolerance_Type()
)
jnxoptIfOChSinkOSNRTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkOSNRTolerance.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkOSNRTolerance.setUnits("0.1 dB")
_JnxoptIfOTNPMGroup_ObjectIdentity = ObjectIdentity
jnxoptIfOTNPMGroup = _JnxoptIfOTNPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3)
)
_JnxoptIfOChSinkCurrentExtTable_Object = MibTable
jnxoptIfOChSinkCurrentExtTable = _JnxoptIfOChSinkCurrentExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentExtTable.setStatus("current")
_JnxoptIfOChSinkCurrentExtEntry_Object = MibTableRow
jnxoptIfOChSinkCurrentExtEntry = _JnxoptIfOChSinkCurrentExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentExtEntry.setStatus("current")
_JnxoptIfOChSinkCurrentChromaticDispersion_Type = Integer32
_JnxoptIfOChSinkCurrentChromaticDispersion_Object = MibTableColumn
jnxoptIfOChSinkCurrentChromaticDispersion = _JnxoptIfOChSinkCurrentChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 1, 1, 1),
    _JnxoptIfOChSinkCurrentChromaticDispersion_Type()
)
jnxoptIfOChSinkCurrentChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentChromaticDispersion.setUnits("ps/nm")
_JnxoptIfOChSinkCurrentOSNR_Type = Integer32
_JnxoptIfOChSinkCurrentOSNR_Object = MibTableColumn
jnxoptIfOChSinkCurrentOSNR = _JnxoptIfOChSinkCurrentOSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 1, 1, 2),
    _JnxoptIfOChSinkCurrentOSNR_Type()
)
jnxoptIfOChSinkCurrentOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentOSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentOSNR.setUnits("0.1 dB")
_JnxoptIfOChSinkCurrentQ_Type = Integer32
_JnxoptIfOChSinkCurrentQ_Object = MibTableColumn
jnxoptIfOChSinkCurrentQ = _JnxoptIfOChSinkCurrentQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 1, 1, 3),
    _JnxoptIfOChSinkCurrentQ_Type()
)
jnxoptIfOChSinkCurrentQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentQ.setStatus("current")
_JnxoptIfOTNPMConfigTable_Object = MibTable
jnxoptIfOTNPMConfigTable = _JnxoptIfOTNPMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMConfigTable.setStatus("current")
_JnxoptIfOTNPMConfigEntry_Object = MibTableRow
jnxoptIfOTNPMConfigEntry = _JnxoptIfOTNPMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1)
)
jnxoptIfOTNPMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMConfigType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMConfigLayer"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMConfigTCMLevel"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMConfigEntry.setStatus("current")
_JnxoptIfOTNPMConfigType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMConfigType_Object = MibTableColumn
jnxoptIfOTNPMConfigType = _JnxoptIfOTNPMConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 1),
    _JnxoptIfOTNPMConfigType_Type()
)
jnxoptIfOTNPMConfigType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMConfigType.setStatus("current")
_JnxoptIfOTNPMConfigLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNPMConfigLayer_Object = MibTableColumn
jnxoptIfOTNPMConfigLayer = _JnxoptIfOTNPMConfigLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 2),
    _JnxoptIfOTNPMConfigLayer_Type()
)
jnxoptIfOTNPMConfigLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMConfigLayer.setStatus("current")


class _JnxoptIfOTNPMConfigTCMLevel_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMConfigTCMLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxoptIfOTNPMConfigTCMLevel_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMConfigTCMLevel_Object = MibTableColumn
jnxoptIfOTNPMConfigTCMLevel = _JnxoptIfOTNPMConfigTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 3),
    _JnxoptIfOTNPMConfigTCMLevel_Type()
)
jnxoptIfOTNPMConfigTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMConfigTCMLevel.setStatus("current")


class _JnxoptIfOTNPMESRInterval_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMESRInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxoptIfOTNPMESRInterval_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMESRInterval_Object = MibTableColumn
jnxoptIfOTNPMESRInterval = _JnxoptIfOTNPMESRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 4),
    _JnxoptIfOTNPMESRInterval_Type()
)
jnxoptIfOTNPMESRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMESRInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMESRInterval.setUnits("seconds")
_JnxoptIfOTNPMSESRInterval_Type = Unsigned32
_JnxoptIfOTNPMSESRInterval_Object = MibTableColumn
jnxoptIfOTNPMSESRInterval = _JnxoptIfOTNPMSESRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 5),
    _JnxoptIfOTNPMSESRInterval_Type()
)
jnxoptIfOTNPMSESRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMSESRInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMSESRInterval.setUnits("seconds")
_JnxoptIfOTNPMValidIntervals_Type = Unsigned32
_JnxoptIfOTNPMValidIntervals_Object = MibTableColumn
jnxoptIfOTNPMValidIntervals = _JnxoptIfOTNPMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 6),
    _JnxoptIfOTNPMValidIntervals_Type()
)
jnxoptIfOTNPMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMValidIntervals.setStatus("current")
_JnxoptIfOTNPM15MinBip8Threshold_Type = Unsigned32
_JnxoptIfOTNPM15MinBip8Threshold_Object = MibTableColumn
jnxoptIfOTNPM15MinBip8Threshold = _JnxoptIfOTNPM15MinBip8Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 7),
    _JnxoptIfOTNPM15MinBip8Threshold_Type()
)
jnxoptIfOTNPM15MinBip8Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinBip8Threshold.setStatus("current")
_JnxoptIfOTNPM15MinESsThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinESsThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinESsThreshold = _JnxoptIfOTNPM15MinESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 8),
    _JnxoptIfOTNPM15MinESsThreshold_Type()
)
jnxoptIfOTNPM15MinESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinESsThreshold.setStatus("current")
_JnxoptIfOTNPM15MinSESsThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinSESsThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinSESsThreshold = _JnxoptIfOTNPM15MinSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 9),
    _JnxoptIfOTNPM15MinSESsThreshold_Type()
)
jnxoptIfOTNPM15MinSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinSESsThreshold.setStatus("current")
_JnxoptIfOTNPM15MinUASsThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinUASsThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinUASsThreshold = _JnxoptIfOTNPM15MinUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 10),
    _JnxoptIfOTNPM15MinUASsThreshold_Type()
)
jnxoptIfOTNPM15MinUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinUASsThreshold.setStatus("current")
_JnxoptIfOTNPM15MinBBEsThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinBBEsThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinBBEsThreshold = _JnxoptIfOTNPM15MinBBEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 11),
    _JnxoptIfOTNPM15MinBBEsThreshold_Type()
)
jnxoptIfOTNPM15MinBBEsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinBBEsThreshold.setStatus("current")
_JnxoptIfOTNPM24HourBip8Threshold_Type = Unsigned32
_JnxoptIfOTNPM24HourBip8Threshold_Object = MibTableColumn
jnxoptIfOTNPM24HourBip8Threshold = _JnxoptIfOTNPM24HourBip8Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 12),
    _JnxoptIfOTNPM24HourBip8Threshold_Type()
)
jnxoptIfOTNPM24HourBip8Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourBip8Threshold.setStatus("current")
_JnxoptIfOTNPM24HourESsThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourESsThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourESsThreshold = _JnxoptIfOTNPM24HourESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 13),
    _JnxoptIfOTNPM24HourESsThreshold_Type()
)
jnxoptIfOTNPM24HourESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourESsThreshold.setStatus("current")
_JnxoptIfOTNPM24HourSESsThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourSESsThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourSESsThreshold = _JnxoptIfOTNPM24HourSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 14),
    _JnxoptIfOTNPM24HourSESsThreshold_Type()
)
jnxoptIfOTNPM24HourSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourSESsThreshold.setStatus("current")
_JnxoptIfOTNPM24HourUASsThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourUASsThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourUASsThreshold = _JnxoptIfOTNPM24HourUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 15),
    _JnxoptIfOTNPM24HourUASsThreshold_Type()
)
jnxoptIfOTNPM24HourUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourUASsThreshold.setStatus("current")
_JnxoptIfOTNPM24HourBBEsThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourBBEsThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourBBEsThreshold = _JnxoptIfOTNPM24HourBBEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 16),
    _JnxoptIfOTNPM24HourBBEsThreshold_Type()
)
jnxoptIfOTNPM24HourBBEsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourBBEsThreshold.setStatus("current")
_JnxoptIfOTNPMBip8EnableTCA_Type = TruthValue
_JnxoptIfOTNPMBip8EnableTCA_Object = MibTableColumn
jnxoptIfOTNPMBip8EnableTCA = _JnxoptIfOTNPMBip8EnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 17),
    _JnxoptIfOTNPMBip8EnableTCA_Type()
)
jnxoptIfOTNPMBip8EnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMBip8EnableTCA.setStatus("current")
_JnxoptIfOTNPMESsEnableTCA_Type = TruthValue
_JnxoptIfOTNPMESsEnableTCA_Object = MibTableColumn
jnxoptIfOTNPMESsEnableTCA = _JnxoptIfOTNPMESsEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 18),
    _JnxoptIfOTNPMESsEnableTCA_Type()
)
jnxoptIfOTNPMESsEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMESsEnableTCA.setStatus("current")
_JnxoptIfOTNPMSESsEnableTCA_Type = TruthValue
_JnxoptIfOTNPMSESsEnableTCA_Object = MibTableColumn
jnxoptIfOTNPMSESsEnableTCA = _JnxoptIfOTNPMSESsEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 19),
    _JnxoptIfOTNPMSESsEnableTCA_Type()
)
jnxoptIfOTNPMSESsEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMSESsEnableTCA.setStatus("current")
_JnxoptIfOTNPMUASsEnableTCA_Type = TruthValue
_JnxoptIfOTNPMUASsEnableTCA_Object = MibTableColumn
jnxoptIfOTNPMUASsEnableTCA = _JnxoptIfOTNPMUASsEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 20),
    _JnxoptIfOTNPMUASsEnableTCA_Type()
)
jnxoptIfOTNPMUASsEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMUASsEnableTCA.setStatus("current")
_JnxoptIfOTNPMBBEsEnableTCA_Type = TruthValue
_JnxoptIfOTNPMBBEsEnableTCA_Object = MibTableColumn
jnxoptIfOTNPMBBEsEnableTCA = _JnxoptIfOTNPMBBEsEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 2, 1, 21),
    _JnxoptIfOTNPMBBEsEnableTCA_Type()
)
jnxoptIfOTNPMBBEsEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMBBEsEnableTCA.setStatus("current")
_JnxoptIfOTNPMCurrentTable_Object = MibTable
jnxoptIfOTNPMCurrentTable = _JnxoptIfOTNPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentTable.setStatus("current")
_JnxoptIfOTNPMCurrentEntry_Object = MibTableRow
jnxoptIfOTNPMCurrentEntry = _JnxoptIfOTNPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1)
)
jnxoptIfOTNPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentLayer"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentTCMLevel"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentEntry.setStatus("current")
_JnxoptIfOTNPMCurrentType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMCurrentType_Object = MibTableColumn
jnxoptIfOTNPMCurrentType = _JnxoptIfOTNPMCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 1),
    _JnxoptIfOTNPMCurrentType_Type()
)
jnxoptIfOTNPMCurrentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentType.setStatus("current")
_JnxoptIfOTNPMCurrentLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNPMCurrentLayer_Object = MibTableColumn
jnxoptIfOTNPMCurrentLayer = _JnxoptIfOTNPMCurrentLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 2),
    _JnxoptIfOTNPMCurrentLayer_Type()
)
jnxoptIfOTNPMCurrentLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentLayer.setStatus("current")


class _JnxoptIfOTNPMCurrentTCMLevel_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMCurrentTCMLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxoptIfOTNPMCurrentTCMLevel_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMCurrentTCMLevel_Object = MibTableColumn
jnxoptIfOTNPMCurrentTCMLevel = _JnxoptIfOTNPMCurrentTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 3),
    _JnxoptIfOTNPMCurrentTCMLevel_Type()
)
jnxoptIfOTNPMCurrentTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentTCMLevel.setStatus("current")
_JnxoptIfOTNPMCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMCurrentSuspectedFlag = _JnxoptIfOTNPMCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 4),
    _JnxoptIfOTNPMCurrentSuspectedFlag_Type()
)
jnxoptIfOTNPMCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOTNPMCurrentBip8_Type = Unsigned32
_JnxoptIfOTNPMCurrentBip8_Object = MibTableColumn
jnxoptIfOTNPMCurrentBip8 = _JnxoptIfOTNPMCurrentBip8_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 5),
    _JnxoptIfOTNPMCurrentBip8_Type()
)
jnxoptIfOTNPMCurrentBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentBip8.setStatus("current")
_JnxoptIfOTNPMCurrentESs_Type = Unsigned32
_JnxoptIfOTNPMCurrentESs_Object = MibTableColumn
jnxoptIfOTNPMCurrentESs = _JnxoptIfOTNPMCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 6),
    _JnxoptIfOTNPMCurrentESs_Type()
)
jnxoptIfOTNPMCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentESs.setStatus("current")
_JnxoptIfOTNPMCurrentSESs_Type = Unsigned32
_JnxoptIfOTNPMCurrentSESs_Object = MibTableColumn
jnxoptIfOTNPMCurrentSESs = _JnxoptIfOTNPMCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 7),
    _JnxoptIfOTNPMCurrentSESs_Type()
)
jnxoptIfOTNPMCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentSESs.setStatus("current")
_JnxoptIfOTNPMCurrentUASs_Type = Unsigned32
_JnxoptIfOTNPMCurrentUASs_Object = MibTableColumn
jnxoptIfOTNPMCurrentUASs = _JnxoptIfOTNPMCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 8),
    _JnxoptIfOTNPMCurrentUASs_Type()
)
jnxoptIfOTNPMCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentUASs.setStatus("current")
_JnxoptIfOTNPMCurrentBBEs_Type = Unsigned32
_JnxoptIfOTNPMCurrentBBEs_Object = MibTableColumn
jnxoptIfOTNPMCurrentBBEs = _JnxoptIfOTNPMCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 9),
    _JnxoptIfOTNPMCurrentBBEs_Type()
)
jnxoptIfOTNPMCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentBBEs.setStatus("current")
_JnxoptIfOTNPMCurrentESR_Type = Unsigned32
_JnxoptIfOTNPMCurrentESR_Object = MibTableColumn
jnxoptIfOTNPMCurrentESR = _JnxoptIfOTNPMCurrentESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 10),
    _JnxoptIfOTNPMCurrentESR_Type()
)
jnxoptIfOTNPMCurrentESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentESR.setUnits(".001")
_JnxoptIfOTNPMCurrentSESR_Type = Unsigned32
_JnxoptIfOTNPMCurrentSESR_Object = MibTableColumn
jnxoptIfOTNPMCurrentSESR = _JnxoptIfOTNPMCurrentSESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 11),
    _JnxoptIfOTNPMCurrentSESR_Type()
)
jnxoptIfOTNPMCurrentSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentSESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentSESR.setUnits(".001")
_JnxoptIfOTNPMCurrentBBER_Type = Unsigned32
_JnxoptIfOTNPMCurrentBBER_Object = MibTableColumn
jnxoptIfOTNPMCurrentBBER = _JnxoptIfOTNPMCurrentBBER_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 12),
    _JnxoptIfOTNPMCurrentBBER_Type()
)
jnxoptIfOTNPMCurrentBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentBBER.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentBBER.setUnits(".001")
_JnxoptIfOTNPMCurrentElapsedTime_Type = Unsigned32
_JnxoptIfOTNPMCurrentElapsedTime_Object = MibTableColumn
jnxoptIfOTNPMCurrentElapsedTime = _JnxoptIfOTNPMCurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 13),
    _JnxoptIfOTNPMCurrentElapsedTime_Type()
)
jnxoptIfOTNPMCurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentElapsedTime.setUnits("seconds")
_JnxoptIfOTNPMCurSuspectReason_Type = Integer32
_JnxoptIfOTNPMCurSuspectReason_Object = MibTableColumn
jnxoptIfOTNPMCurSuspectReason = _JnxoptIfOTNPMCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 3, 1, 14),
    _JnxoptIfOTNPMCurSuspectReason_Type()
)
jnxoptIfOTNPMCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurSuspectReason.setStatus("current")
_JnxoptIfOTNPMIntervalTable_Object = MibTable
jnxoptIfOTNPMIntervalTable = _JnxoptIfOTNPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalTable.setStatus("current")
_JnxoptIfOTNPMIntervalEntry_Object = MibTableRow
jnxoptIfOTNPMIntervalEntry = _JnxoptIfOTNPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1)
)
jnxoptIfOTNPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMIntervalType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMIntervalLayer"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMIntervalTCMLevel"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalEntry.setStatus("current")
_JnxoptIfOTNPMIntervalType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMIntervalType_Object = MibTableColumn
jnxoptIfOTNPMIntervalType = _JnxoptIfOTNPMIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 1),
    _JnxoptIfOTNPMIntervalType_Type()
)
jnxoptIfOTNPMIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalType.setStatus("current")
_JnxoptIfOTNPMIntervalLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNPMIntervalLayer_Object = MibTableColumn
jnxoptIfOTNPMIntervalLayer = _JnxoptIfOTNPMIntervalLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 2),
    _JnxoptIfOTNPMIntervalLayer_Type()
)
jnxoptIfOTNPMIntervalLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalLayer.setStatus("current")


class _JnxoptIfOTNPMIntervalTCMLevel_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMIntervalTCMLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxoptIfOTNPMIntervalTCMLevel_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMIntervalTCMLevel_Object = MibTableColumn
jnxoptIfOTNPMIntervalTCMLevel = _JnxoptIfOTNPMIntervalTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 3),
    _JnxoptIfOTNPMIntervalTCMLevel_Type()
)
jnxoptIfOTNPMIntervalTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalTCMLevel.setStatus("current")


class _JnxoptIfOTNPMIntervalNumber_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxoptIfOTNPMIntervalNumber_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMIntervalNumber_Object = MibTableColumn
jnxoptIfOTNPMIntervalNumber = _JnxoptIfOTNPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 4),
    _JnxoptIfOTNPMIntervalNumber_Type()
)
jnxoptIfOTNPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalNumber.setStatus("current")
_JnxoptIfOTNPMIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMIntervalSuspectedFlag = _JnxoptIfOTNPMIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 5),
    _JnxoptIfOTNPMIntervalSuspectedFlag_Type()
)
jnxoptIfOTNPMIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOTNPMIntervalBip8_Type = Unsigned32
_JnxoptIfOTNPMIntervalBip8_Object = MibTableColumn
jnxoptIfOTNPMIntervalBip8 = _JnxoptIfOTNPMIntervalBip8_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 6),
    _JnxoptIfOTNPMIntervalBip8_Type()
)
jnxoptIfOTNPMIntervalBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalBip8.setStatus("current")
_JnxoptIfOTNPMIntervalESs_Type = Unsigned32
_JnxoptIfOTNPMIntervalESs_Object = MibTableColumn
jnxoptIfOTNPMIntervalESs = _JnxoptIfOTNPMIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 7),
    _JnxoptIfOTNPMIntervalESs_Type()
)
jnxoptIfOTNPMIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalESs.setStatus("current")
_JnxoptIfOTNPMIntervalSESs_Type = Unsigned32
_JnxoptIfOTNPMIntervalSESs_Object = MibTableColumn
jnxoptIfOTNPMIntervalSESs = _JnxoptIfOTNPMIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 8),
    _JnxoptIfOTNPMIntervalSESs_Type()
)
jnxoptIfOTNPMIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalSESs.setStatus("current")
_JnxoptIfOTNPMIntervalUASs_Type = Unsigned32
_JnxoptIfOTNPMIntervalUASs_Object = MibTableColumn
jnxoptIfOTNPMIntervalUASs = _JnxoptIfOTNPMIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 9),
    _JnxoptIfOTNPMIntervalUASs_Type()
)
jnxoptIfOTNPMIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalUASs.setStatus("current")
_JnxoptIfOTNPMIntervalBBEs_Type = Unsigned32
_JnxoptIfOTNPMIntervalBBEs_Object = MibTableColumn
jnxoptIfOTNPMIntervalBBEs = _JnxoptIfOTNPMIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 10),
    _JnxoptIfOTNPMIntervalBBEs_Type()
)
jnxoptIfOTNPMIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalBBEs.setStatus("current")
_JnxoptIfOTNPMIntervalESR_Type = Unsigned32
_JnxoptIfOTNPMIntervalESR_Object = MibTableColumn
jnxoptIfOTNPMIntervalESR = _JnxoptIfOTNPMIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 11),
    _JnxoptIfOTNPMIntervalESR_Type()
)
jnxoptIfOTNPMIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalESR.setUnits(".001")
_JnxoptIfOTNPMIntervalSESR_Type = Unsigned32
_JnxoptIfOTNPMIntervalSESR_Object = MibTableColumn
jnxoptIfOTNPMIntervalSESR = _JnxoptIfOTNPMIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 12),
    _JnxoptIfOTNPMIntervalSESR_Type()
)
jnxoptIfOTNPMIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalSESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalSESR.setUnits(".001")
_JnxoptIfOTNPMIntervalBBER_Type = Unsigned32
_JnxoptIfOTNPMIntervalBBER_Object = MibTableColumn
jnxoptIfOTNPMIntervalBBER = _JnxoptIfOTNPMIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 13),
    _JnxoptIfOTNPMIntervalBBER_Type()
)
jnxoptIfOTNPMIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalBBER.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalBBER.setUnits(".001")
_JnxoptIfOTNPMIntervalTimeStamp_Type = DateAndTime
_JnxoptIfOTNPMIntervalTimeStamp_Object = MibTableColumn
jnxoptIfOTNPMIntervalTimeStamp = _JnxoptIfOTNPMIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 14),
    _JnxoptIfOTNPMIntervalTimeStamp_Type()
)
jnxoptIfOTNPMIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalTimeStamp.setStatus("current")
_JnxoptIfOTNPMIntSuspectReason_Type = Integer32
_JnxoptIfOTNPMIntSuspectReason_Object = MibTableColumn
jnxoptIfOTNPMIntSuspectReason = _JnxoptIfOTNPMIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 4, 1, 15),
    _JnxoptIfOTNPMIntSuspectReason_Type()
)
jnxoptIfOTNPMIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntSuspectReason.setStatus("current")
_JnxoptIfOTNPMCurrentDayTable_Object = MibTable
jnxoptIfOTNPMCurrentDayTable = _JnxoptIfOTNPMCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayTable.setStatus("current")
_JnxoptIfOTNPMCurrentDayEntry_Object = MibTableRow
jnxoptIfOTNPMCurrentDayEntry = _JnxoptIfOTNPMCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1)
)
jnxoptIfOTNPMCurrentDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentDayType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentDayLayer"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMCurrentDayTCMLevel"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayEntry.setStatus("current")
_JnxoptIfOTNPMCurrentDayType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMCurrentDayType_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayType = _JnxoptIfOTNPMCurrentDayType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 1),
    _JnxoptIfOTNPMCurrentDayType_Type()
)
jnxoptIfOTNPMCurrentDayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayType.setStatus("current")
_JnxoptIfOTNPMCurrentDayLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNPMCurrentDayLayer_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayLayer = _JnxoptIfOTNPMCurrentDayLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 2),
    _JnxoptIfOTNPMCurrentDayLayer_Type()
)
jnxoptIfOTNPMCurrentDayLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayLayer.setStatus("current")


class _JnxoptIfOTNPMCurrentDayTCMLevel_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMCurrentDayTCMLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxoptIfOTNPMCurrentDayTCMLevel_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMCurrentDayTCMLevel_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayTCMLevel = _JnxoptIfOTNPMCurrentDayTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 3),
    _JnxoptIfOTNPMCurrentDayTCMLevel_Type()
)
jnxoptIfOTNPMCurrentDayTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayTCMLevel.setStatus("current")
_JnxoptIfOTNPMCurrentDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMCurrentDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMCurrentDaySuspectedFlag = _JnxoptIfOTNPMCurrentDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 4),
    _JnxoptIfOTNPMCurrentDaySuspectedFlag_Type()
)
jnxoptIfOTNPMCurrentDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDaySuspectedFlag.setStatus("current")
_JnxoptIfOTNPMCurrentDayBip8_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayBip8_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayBip8 = _JnxoptIfOTNPMCurrentDayBip8_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 5),
    _JnxoptIfOTNPMCurrentDayBip8_Type()
)
jnxoptIfOTNPMCurrentDayBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayBip8.setStatus("current")
_JnxoptIfOTNPMCurrentDayESs_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayESs_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayESs = _JnxoptIfOTNPMCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 6),
    _JnxoptIfOTNPMCurrentDayESs_Type()
)
jnxoptIfOTNPMCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayESs.setStatus("current")
_JnxoptIfOTNPMCurrentDaySESs_Type = Unsigned32
_JnxoptIfOTNPMCurrentDaySESs_Object = MibTableColumn
jnxoptIfOTNPMCurrentDaySESs = _JnxoptIfOTNPMCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 7),
    _JnxoptIfOTNPMCurrentDaySESs_Type()
)
jnxoptIfOTNPMCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDaySESs.setStatus("current")
_JnxoptIfOTNPMCurrentDayUASs_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayUASs_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayUASs = _JnxoptIfOTNPMCurrentDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 8),
    _JnxoptIfOTNPMCurrentDayUASs_Type()
)
jnxoptIfOTNPMCurrentDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayUASs.setStatus("current")
_JnxoptIfOTNPMCurrentDayBBEs_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayBBEs_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayBBEs = _JnxoptIfOTNPMCurrentDayBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 9),
    _JnxoptIfOTNPMCurrentDayBBEs_Type()
)
jnxoptIfOTNPMCurrentDayBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayBBEs.setStatus("current")
_JnxoptIfOTNPMCurrentDayESR_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayESR_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayESR = _JnxoptIfOTNPMCurrentDayESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 10),
    _JnxoptIfOTNPMCurrentDayESR_Type()
)
jnxoptIfOTNPMCurrentDayESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayESR.setUnits(".001")
_JnxoptIfOTNPMCurrentDaySESR_Type = Unsigned32
_JnxoptIfOTNPMCurrentDaySESR_Object = MibTableColumn
jnxoptIfOTNPMCurrentDaySESR = _JnxoptIfOTNPMCurrentDaySESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 11),
    _JnxoptIfOTNPMCurrentDaySESR_Type()
)
jnxoptIfOTNPMCurrentDaySESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDaySESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDaySESR.setUnits(".001")
_JnxoptIfOTNPMCurrentDayBBER_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayBBER_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayBBER = _JnxoptIfOTNPMCurrentDayBBER_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 12),
    _JnxoptIfOTNPMCurrentDayBBER_Type()
)
jnxoptIfOTNPMCurrentDayBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayBBER.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayBBER.setUnits(".001")
_JnxoptIfOTNPMCurrentDayElapsedTime_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayElapsedTime_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayElapsedTime = _JnxoptIfOTNPMCurrentDayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 13),
    _JnxoptIfOTNPMCurrentDayElapsedTime_Type()
)
jnxoptIfOTNPMCurrentDayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayElapsedTime.setUnits("seconds")
_JnxoptIfOTNPMCurDaySuspectReason_Type = Integer32
_JnxoptIfOTNPMCurDaySuspectReason_Object = MibTableColumn
jnxoptIfOTNPMCurDaySuspectReason = _JnxoptIfOTNPMCurDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 5, 1, 14),
    _JnxoptIfOTNPMCurDaySuspectReason_Type()
)
jnxoptIfOTNPMCurDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurDaySuspectReason.setStatus("current")
_JnxoptIfOTNPMPrevDayTable_Object = MibTable
jnxoptIfOTNPMPrevDayTable = _JnxoptIfOTNPMPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayTable.setStatus("current")
_JnxoptIfOTNPMPrevDayEntry_Object = MibTableRow
jnxoptIfOTNPMPrevDayEntry = _JnxoptIfOTNPMPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1)
)
jnxoptIfOTNPMPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMPrevDayType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMPrevDayLayer"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMPrevDayTCMLevel"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayEntry.setStatus("current")
_JnxoptIfOTNPMPrevDayType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMPrevDayType_Object = MibTableColumn
jnxoptIfOTNPMPrevDayType = _JnxoptIfOTNPMPrevDayType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 1),
    _JnxoptIfOTNPMPrevDayType_Type()
)
jnxoptIfOTNPMPrevDayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayType.setStatus("current")
_JnxoptIfOTNPMPrevDayLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNPMPrevDayLayer_Object = MibTableColumn
jnxoptIfOTNPMPrevDayLayer = _JnxoptIfOTNPMPrevDayLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 2),
    _JnxoptIfOTNPMPrevDayLayer_Type()
)
jnxoptIfOTNPMPrevDayLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayLayer.setStatus("current")


class _JnxoptIfOTNPMPrevDayTCMLevel_Type(Unsigned32):
    """Custom type jnxoptIfOTNPMPrevDayTCMLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxoptIfOTNPMPrevDayTCMLevel_Type.__name__ = "Unsigned32"
_JnxoptIfOTNPMPrevDayTCMLevel_Object = MibTableColumn
jnxoptIfOTNPMPrevDayTCMLevel = _JnxoptIfOTNPMPrevDayTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 3),
    _JnxoptIfOTNPMPrevDayTCMLevel_Type()
)
jnxoptIfOTNPMPrevDayTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayTCMLevel.setStatus("current")
_JnxoptIfOTNPMPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMPrevDaySuspectedFlag = _JnxoptIfOTNPMPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 4),
    _JnxoptIfOTNPMPrevDaySuspectedFlag_Type()
)
jnxoptIfOTNPMPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOTNPMPrevDayBip8_Type = Unsigned32
_JnxoptIfOTNPMPrevDayBip8_Object = MibTableColumn
jnxoptIfOTNPMPrevDayBip8 = _JnxoptIfOTNPMPrevDayBip8_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 5),
    _JnxoptIfOTNPMPrevDayBip8_Type()
)
jnxoptIfOTNPMPrevDayBip8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayBip8.setStatus("current")
_JnxoptIfOTNPMPrevDayESs_Type = Unsigned32
_JnxoptIfOTNPMPrevDayESs_Object = MibTableColumn
jnxoptIfOTNPMPrevDayESs = _JnxoptIfOTNPMPrevDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 6),
    _JnxoptIfOTNPMPrevDayESs_Type()
)
jnxoptIfOTNPMPrevDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayESs.setStatus("current")
_JnxoptIfOTNPMPrevDaySESs_Type = Unsigned32
_JnxoptIfOTNPMPrevDaySESs_Object = MibTableColumn
jnxoptIfOTNPMPrevDaySESs = _JnxoptIfOTNPMPrevDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 7),
    _JnxoptIfOTNPMPrevDaySESs_Type()
)
jnxoptIfOTNPMPrevDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDaySESs.setStatus("current")
_JnxoptIfOTNPMPrevDayUASs_Type = Unsigned32
_JnxoptIfOTNPMPrevDayUASs_Object = MibTableColumn
jnxoptIfOTNPMPrevDayUASs = _JnxoptIfOTNPMPrevDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 8),
    _JnxoptIfOTNPMPrevDayUASs_Type()
)
jnxoptIfOTNPMPrevDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayUASs.setStatus("current")
_JnxoptIfOTNPMPrevDayBBEs_Type = Unsigned32
_JnxoptIfOTNPMPrevDayBBEs_Object = MibTableColumn
jnxoptIfOTNPMPrevDayBBEs = _JnxoptIfOTNPMPrevDayBBEs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 9),
    _JnxoptIfOTNPMPrevDayBBEs_Type()
)
jnxoptIfOTNPMPrevDayBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayBBEs.setStatus("current")
_JnxoptIfOTNPMPrevDayESR_Type = Unsigned32
_JnxoptIfOTNPMPrevDayESR_Object = MibTableColumn
jnxoptIfOTNPMPrevDayESR = _JnxoptIfOTNPMPrevDayESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 10),
    _JnxoptIfOTNPMPrevDayESR_Type()
)
jnxoptIfOTNPMPrevDayESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayESR.setUnits(".001")
_JnxoptIfOTNPMPrevDaySESR_Type = Unsigned32
_JnxoptIfOTNPMPrevDaySESR_Object = MibTableColumn
jnxoptIfOTNPMPrevDaySESR = _JnxoptIfOTNPMPrevDaySESR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 11),
    _JnxoptIfOTNPMPrevDaySESR_Type()
)
jnxoptIfOTNPMPrevDaySESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDaySESR.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDaySESR.setUnits(".001")
_JnxoptIfOTNPMPrevDayBBER_Type = Unsigned32
_JnxoptIfOTNPMPrevDayBBER_Object = MibTableColumn
jnxoptIfOTNPMPrevDayBBER = _JnxoptIfOTNPMPrevDayBBER_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 12),
    _JnxoptIfOTNPMPrevDayBBER_Type()
)
jnxoptIfOTNPMPrevDayBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayBBER.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayBBER.setUnits(".001")
_JnxoptIfOTNPMPrevDayTimeStamp_Type = DateAndTime
_JnxoptIfOTNPMPrevDayTimeStamp_Object = MibTableColumn
jnxoptIfOTNPMPrevDayTimeStamp = _JnxoptIfOTNPMPrevDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 13),
    _JnxoptIfOTNPMPrevDayTimeStamp_Type()
)
jnxoptIfOTNPMPrevDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayTimeStamp.setStatus("current")
_JnxoptIfOTNPMPrevDaySuspectReason_Type = Integer32
_JnxoptIfOTNPMPrevDaySuspectReason_Object = MibTableColumn
jnxoptIfOTNPMPrevDaySuspectReason = _JnxoptIfOTNPMPrevDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 6, 1, 14),
    _JnxoptIfOTNPMPrevDaySuspectReason_Type()
)
jnxoptIfOTNPMPrevDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDaySuspectReason.setStatus("current")
_JnxoptIfOTNPMFECConfigTable_Object = MibTable
jnxoptIfOTNPMFECConfigTable = _JnxoptIfOTNPMFECConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECConfigTable.setStatus("current")
_JnxoptIfOTNPMFECConfigEntry_Object = MibTableRow
jnxoptIfOTNPMFECConfigEntry = _JnxoptIfOTNPMFECConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1)
)
jnxoptIfOTNPMFECConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECConfigType"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECConfigEntry.setStatus("current")
_JnxoptIfOTNPMFECConfigType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMFECConfigType_Object = MibTableColumn
jnxoptIfOTNPMFECConfigType = _JnxoptIfOTNPMFECConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 1),
    _JnxoptIfOTNPMFECConfigType_Type()
)
jnxoptIfOTNPMFECConfigType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECConfigType.setStatus("current")
_JnxoptIfOTNPMFECValidIntervals_Type = Unsigned32
_JnxoptIfOTNPMFECValidIntervals_Object = MibTableColumn
jnxoptIfOTNPMFECValidIntervals = _JnxoptIfOTNPMFECValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 2),
    _JnxoptIfOTNPMFECValidIntervals_Type()
)
jnxoptIfOTNPMFECValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECValidIntervals.setStatus("current")
_JnxoptIfOTNPM15MinPreFECBERMantissaThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinPreFECBERMantissaThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinPreFECBERMantissaThreshold = _JnxoptIfOTNPM15MinPreFECBERMantissaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 3),
    _JnxoptIfOTNPM15MinPreFECBERMantissaThreshold_Type()
)
jnxoptIfOTNPM15MinPreFECBERMantissaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinPreFECBERMantissaThreshold.setStatus("current")
_JnxoptIfOTNPM15MinPreFECBERExponentThreshold_Type = Unsigned32
_JnxoptIfOTNPM15MinPreFECBERExponentThreshold_Object = MibTableColumn
jnxoptIfOTNPM15MinPreFECBERExponentThreshold = _JnxoptIfOTNPM15MinPreFECBERExponentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 4),
    _JnxoptIfOTNPM15MinPreFECBERExponentThreshold_Type()
)
jnxoptIfOTNPM15MinPreFECBERExponentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM15MinPreFECBERExponentThreshold.setStatus("current")
_JnxoptIfOTNPM24HourPreFECBERMantissaThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourPreFECBERMantissaThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourPreFECBERMantissaThreshold = _JnxoptIfOTNPM24HourPreFECBERMantissaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 5),
    _JnxoptIfOTNPM24HourPreFECBERMantissaThreshold_Type()
)
jnxoptIfOTNPM24HourPreFECBERMantissaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourPreFECBERMantissaThreshold.setStatus("current")
_JnxoptIfOTNPM24HourPreFECBERExponentThreshold_Type = Unsigned32
_JnxoptIfOTNPM24HourPreFECBERExponentThreshold_Object = MibTableColumn
jnxoptIfOTNPM24HourPreFECBERExponentThreshold = _JnxoptIfOTNPM24HourPreFECBERExponentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 6),
    _JnxoptIfOTNPM24HourPreFECBERExponentThreshold_Type()
)
jnxoptIfOTNPM24HourPreFECBERExponentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPM24HourPreFECBERExponentThreshold.setStatus("current")
_JnxoptIfOTNPMFECBEREnableTCA_Type = TruthValue
_JnxoptIfOTNPMFECBEREnableTCA_Object = MibTableColumn
jnxoptIfOTNPMFECBEREnableTCA = _JnxoptIfOTNPMFECBEREnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 7, 1, 7),
    _JnxoptIfOTNPMFECBEREnableTCA_Type()
)
jnxoptIfOTNPMFECBEREnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECBEREnableTCA.setStatus("current")
_JnxoptIfOTNPMFECCurrentTable_Object = MibTable
jnxoptIfOTNPMFECCurrentTable = _JnxoptIfOTNPMFECCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentTable.setStatus("current")
_JnxoptIfOTNPMFECCurrentEntry_Object = MibTableRow
jnxoptIfOTNPMFECCurrentEntry = _JnxoptIfOTNPMFECCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1)
)
jnxoptIfOTNPMFECCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECCurrentType"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentEntry.setStatus("current")
_JnxoptIfOTNPMFECCurrentType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMFECCurrentType_Object = MibTableColumn
jnxoptIfOTNPMFECCurrentType = _JnxoptIfOTNPMFECCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 1),
    _JnxoptIfOTNPMFECCurrentType_Type()
)
jnxoptIfOTNPMFECCurrentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentType.setStatus("current")
_JnxoptIfOTNPMFECCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMFECCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMFECCurrentSuspectedFlag = _JnxoptIfOTNPMFECCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 2),
    _JnxoptIfOTNPMFECCurrentSuspectedFlag_Type()
)
jnxoptIfOTNPMFECCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOTNPMCurrentFECCorrectedErr_Type = Counter64
_JnxoptIfOTNPMCurrentFECCorrectedErr_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECCorrectedErr = _JnxoptIfOTNPMCurrentFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 3),
    _JnxoptIfOTNPMCurrentFECCorrectedErr_Type()
)
jnxoptIfOTNPMCurrentFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECCorrectedErr.setStatus("current")
_JnxoptIfOTNPMCurrentFECUncorrectedWords_Type = Counter64
_JnxoptIfOTNPMCurrentFECUncorrectedWords_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECUncorrectedWords = _JnxoptIfOTNPMCurrentFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 4),
    _JnxoptIfOTNPMCurrentFECUncorrectedWords_Type()
)
jnxoptIfOTNPMCurrentFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECUncorrectedWords.setStatus("current")
_JnxoptIfOTNPMCurrentFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECBERMantissa = _JnxoptIfOTNPMCurrentFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 5),
    _JnxoptIfOTNPMCurrentFECBERMantissa_Type()
)
jnxoptIfOTNPMCurrentFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECBERExponent = _JnxoptIfOTNPMCurrentFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 6),
    _JnxoptIfOTNPMCurrentFECBERExponent_Type()
)
jnxoptIfOTNPMCurrentFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentFECMinBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECMinBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECMinBERMantissa = _JnxoptIfOTNPMCurrentFECMinBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 7),
    _JnxoptIfOTNPMCurrentFECMinBERMantissa_Type()
)
jnxoptIfOTNPMCurrentFECMinBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECMinBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentFECMinBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECMinBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECMinBERExponent = _JnxoptIfOTNPMCurrentFECMinBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 8),
    _JnxoptIfOTNPMCurrentFECMinBERExponent_Type()
)
jnxoptIfOTNPMCurrentFECMinBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECMinBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentFECMaxBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECMaxBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECMaxBERMantissa = _JnxoptIfOTNPMCurrentFECMaxBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 9),
    _JnxoptIfOTNPMCurrentFECMaxBERMantissa_Type()
)
jnxoptIfOTNPMCurrentFECMaxBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECMaxBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentFECMaxBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECMaxBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECMaxBERExponent = _JnxoptIfOTNPMCurrentFECMaxBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 10),
    _JnxoptIfOTNPMCurrentFECMaxBERExponent_Type()
)
jnxoptIfOTNPMCurrentFECMaxBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECMaxBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentFECAvgBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECAvgBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECAvgBERMantissa = _JnxoptIfOTNPMCurrentFECAvgBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 11),
    _JnxoptIfOTNPMCurrentFECAvgBERMantissa_Type()
)
jnxoptIfOTNPMCurrentFECAvgBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECAvgBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentFECAvgBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECAvgBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECAvgBERExponent = _JnxoptIfOTNPMCurrentFECAvgBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 12),
    _JnxoptIfOTNPMCurrentFECAvgBERExponent_Type()
)
jnxoptIfOTNPMCurrentFECAvgBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECAvgBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentFECElapsedTime_Type = Unsigned32
_JnxoptIfOTNPMCurrentFECElapsedTime_Object = MibTableColumn
jnxoptIfOTNPMCurrentFECElapsedTime = _JnxoptIfOTNPMCurrentFECElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 13),
    _JnxoptIfOTNPMCurrentFECElapsedTime_Type()
)
jnxoptIfOTNPMCurrentFECElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentFECElapsedTime.setUnits("seconds")
_JnxoptIfOTNPMFECCurSuspectReason_Type = Integer32
_JnxoptIfOTNPMFECCurSuspectReason_Object = MibTableColumn
jnxoptIfOTNPMFECCurSuspectReason = _JnxoptIfOTNPMFECCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 8, 1, 14),
    _JnxoptIfOTNPMFECCurSuspectReason_Type()
)
jnxoptIfOTNPMFECCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurSuspectReason.setStatus("current")
_JnxoptIfOTNPMFECIntervalTable_Object = MibTable
jnxoptIfOTNPMFECIntervalTable = _JnxoptIfOTNPMFECIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalTable.setStatus("current")
_JnxoptIfOTNPMFECIntervalEntry_Object = MibTableRow
jnxoptIfOTNPMFECIntervalEntry = _JnxoptIfOTNPMFECIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1)
)
jnxoptIfOTNPMFECIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECIntervalType"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalEntry.setStatus("current")
_JnxoptIfOTNPMFECIntervalType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMFECIntervalType_Object = MibTableColumn
jnxoptIfOTNPMFECIntervalType = _JnxoptIfOTNPMFECIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 1),
    _JnxoptIfOTNPMFECIntervalType_Type()
)
jnxoptIfOTNPMFECIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalType.setStatus("current")
_JnxoptIfOTNPMFECIntervalNumber_Type = Unsigned32
_JnxoptIfOTNPMFECIntervalNumber_Object = MibTableColumn
jnxoptIfOTNPMFECIntervalNumber = _JnxoptIfOTNPMFECIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 2),
    _JnxoptIfOTNPMFECIntervalNumber_Type()
)
jnxoptIfOTNPMFECIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalNumber.setStatus("current")
_JnxoptIfOTNPMFECIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMFECIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMFECIntervalSuspectedFlag = _JnxoptIfOTNPMFECIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 3),
    _JnxoptIfOTNPMFECIntervalSuspectedFlag_Type()
)
jnxoptIfOTNPMFECIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOTNPMIntervalFECCorrectedErr_Type = Counter64
_JnxoptIfOTNPMIntervalFECCorrectedErr_Object = MibTableColumn
jnxoptIfOTNPMIntervalFECCorrectedErr = _JnxoptIfOTNPMIntervalFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 4),
    _JnxoptIfOTNPMIntervalFECCorrectedErr_Type()
)
jnxoptIfOTNPMIntervalFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalFECCorrectedErr.setStatus("current")
_JnxoptIfOTNPMIntervalFECUncorrectedWords_Type = Counter64
_JnxoptIfOTNPMIntervalFECUncorrectedWords_Object = MibTableColumn
jnxoptIfOTNPMIntervalFECUncorrectedWords = _JnxoptIfOTNPMIntervalFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 5),
    _JnxoptIfOTNPMIntervalFECUncorrectedWords_Type()
)
jnxoptIfOTNPMIntervalFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalFECUncorrectedWords.setStatus("current")
_JnxoptIfOTNPMIntervalMinFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMIntervalMinFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMIntervalMinFECBERMantissa = _JnxoptIfOTNPMIntervalMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 6),
    _JnxoptIfOTNPMIntervalMinFECBERMantissa_Type()
)
jnxoptIfOTNPMIntervalMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalMinFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMIntervalMinFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMIntervalMinFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMIntervalMinFECBERExponent = _JnxoptIfOTNPMIntervalMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 7),
    _JnxoptIfOTNPMIntervalMinFECBERExponent_Type()
)
jnxoptIfOTNPMIntervalMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalMinFECBERExponent.setStatus("current")
_JnxoptIfOTNPMIntervalMaxFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMIntervalMaxFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMIntervalMaxFECBERMantissa = _JnxoptIfOTNPMIntervalMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 8),
    _JnxoptIfOTNPMIntervalMaxFECBERMantissa_Type()
)
jnxoptIfOTNPMIntervalMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalMaxFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMIntervalMaxFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMIntervalMaxFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMIntervalMaxFECBERExponent = _JnxoptIfOTNPMIntervalMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 9),
    _JnxoptIfOTNPMIntervalMaxFECBERExponent_Type()
)
jnxoptIfOTNPMIntervalMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalMaxFECBERExponent.setStatus("current")
_JnxoptIfOTNPMIntervalAvgFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMIntervalAvgFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMIntervalAvgFECBERMantissa = _JnxoptIfOTNPMIntervalAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 10),
    _JnxoptIfOTNPMIntervalAvgFECBERMantissa_Type()
)
jnxoptIfOTNPMIntervalAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalAvgFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMIntervalAvgFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMIntervalAvgFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMIntervalAvgFECBERExponent = _JnxoptIfOTNPMIntervalAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 11),
    _JnxoptIfOTNPMIntervalAvgFECBERExponent_Type()
)
jnxoptIfOTNPMIntervalAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMIntervalAvgFECBERExponent.setStatus("current")
_JnxoptIfOTNPMFECIntervalTimeStamp_Type = DateAndTime
_JnxoptIfOTNPMFECIntervalTimeStamp_Object = MibTableColumn
jnxoptIfOTNPMFECIntervalTimeStamp = _JnxoptIfOTNPMFECIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 12),
    _JnxoptIfOTNPMFECIntervalTimeStamp_Type()
)
jnxoptIfOTNPMFECIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntervalTimeStamp.setStatus("current")
_JnxoptIfOTNPMFECIntSuspectReason_Type = Integer32
_JnxoptIfOTNPMFECIntSuspectReason_Object = MibTableColumn
jnxoptIfOTNPMFECIntSuspectReason = _JnxoptIfOTNPMFECIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 9, 1, 13),
    _JnxoptIfOTNPMFECIntSuspectReason_Type()
)
jnxoptIfOTNPMFECIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECIntSuspectReason.setStatus("current")
_JnxoptIfOTNPMFECCurrentDayTable_Object = MibTable
jnxoptIfOTNPMFECCurrentDayTable = _JnxoptIfOTNPMFECCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDayTable.setStatus("current")
_JnxoptIfOTNPMFECCurrentDayEntry_Object = MibTableRow
jnxoptIfOTNPMFECCurrentDayEntry = _JnxoptIfOTNPMFECCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1)
)
jnxoptIfOTNPMFECCurrentDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECCurrentDayType"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDayEntry.setStatus("current")
_JnxoptIfOTNPMFECCurrentDayType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMFECCurrentDayType_Object = MibTableColumn
jnxoptIfOTNPMFECCurrentDayType = _JnxoptIfOTNPMFECCurrentDayType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 1),
    _JnxoptIfOTNPMFECCurrentDayType_Type()
)
jnxoptIfOTNPMFECCurrentDayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDayType.setStatus("current")
_JnxoptIfOTNPMFECCurrentDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMFECCurrentDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMFECCurrentDaySuspectedFlag = _JnxoptIfOTNPMFECCurrentDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 2),
    _JnxoptIfOTNPMFECCurrentDaySuspectedFlag_Type()
)
jnxoptIfOTNPMFECCurrentDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDaySuspectedFlag.setStatus("current")
_JnxoptIfOTNPMCurrentDayFECCorrectedErr_Type = Counter64
_JnxoptIfOTNPMCurrentDayFECCorrectedErr_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayFECCorrectedErr = _JnxoptIfOTNPMCurrentDayFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 3),
    _JnxoptIfOTNPMCurrentDayFECCorrectedErr_Type()
)
jnxoptIfOTNPMCurrentDayFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayFECCorrectedErr.setStatus("current")
_JnxoptIfOTNPMCurrentDayFECUncorrectedWords_Type = Counter64
_JnxoptIfOTNPMCurrentDayFECUncorrectedWords_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayFECUncorrectedWords = _JnxoptIfOTNPMCurrentDayFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 4),
    _JnxoptIfOTNPMCurrentDayFECUncorrectedWords_Type()
)
jnxoptIfOTNPMCurrentDayFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayFECUncorrectedWords.setStatus("current")
_JnxoptIfOTNPMCurrentDayMinFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayMinFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayMinFECBERMantissa = _JnxoptIfOTNPMCurrentDayMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 5),
    _JnxoptIfOTNPMCurrentDayMinFECBERMantissa_Type()
)
jnxoptIfOTNPMCurrentDayMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayMinFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentDayMinFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayMinFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayMinFECBERExponent = _JnxoptIfOTNPMCurrentDayMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 6),
    _JnxoptIfOTNPMCurrentDayMinFECBERExponent_Type()
)
jnxoptIfOTNPMCurrentDayMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayMinFECBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentDayMaxFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayMaxFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayMaxFECBERMantissa = _JnxoptIfOTNPMCurrentDayMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 7),
    _JnxoptIfOTNPMCurrentDayMaxFECBERMantissa_Type()
)
jnxoptIfOTNPMCurrentDayMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayMaxFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentDayMaxFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayMaxFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayMaxFECBERExponent = _JnxoptIfOTNPMCurrentDayMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 8),
    _JnxoptIfOTNPMCurrentDayMaxFECBERExponent_Type()
)
jnxoptIfOTNPMCurrentDayMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayMaxFECBERExponent.setStatus("current")
_JnxoptIfOTNPMCurrentDayAvgFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayAvgFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayAvgFECBERMantissa = _JnxoptIfOTNPMCurrentDayAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 9),
    _JnxoptIfOTNPMCurrentDayAvgFECBERMantissa_Type()
)
jnxoptIfOTNPMCurrentDayAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayAvgFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMCurrentDayAvgFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMCurrentDayAvgFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMCurrentDayAvgFECBERExponent = _JnxoptIfOTNPMCurrentDayAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 10),
    _JnxoptIfOTNPMCurrentDayAvgFECBERExponent_Type()
)
jnxoptIfOTNPMCurrentDayAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMCurrentDayAvgFECBERExponent.setStatus("current")
_JnxoptIfOTNPMFECCurrentDayElapsedTime_Type = Unsigned32
_JnxoptIfOTNPMFECCurrentDayElapsedTime_Object = MibTableColumn
jnxoptIfOTNPMFECCurrentDayElapsedTime = _JnxoptIfOTNPMFECCurrentDayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 11),
    _JnxoptIfOTNPMFECCurrentDayElapsedTime_Type()
)
jnxoptIfOTNPMFECCurrentDayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDayElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurrentDayElapsedTime.setUnits("seconds")
_JnxoptIfOTNPMFECCurDaySuspectReason_Type = Integer32
_JnxoptIfOTNPMFECCurDaySuspectReason_Object = MibTableColumn
jnxoptIfOTNPMFECCurDaySuspectReason = _JnxoptIfOTNPMFECCurDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 10, 1, 12),
    _JnxoptIfOTNPMFECCurDaySuspectReason_Type()
)
jnxoptIfOTNPMFECCurDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECCurDaySuspectReason.setStatus("current")
_JnxoptIfOTNPMFECPrevDayTable_Object = MibTable
jnxoptIfOTNPMFECPrevDayTable = _JnxoptIfOTNPMFECPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDayTable.setStatus("current")
_JnxoptIfOTNPMFECPrevDayEntry_Object = MibTableRow
jnxoptIfOTNPMFECPrevDayEntry = _JnxoptIfOTNPMFECPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1)
)
jnxoptIfOTNPMFECPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNPMFECPrevDayType"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDayEntry.setStatus("current")
_JnxoptIfOTNPMFECPrevDayType_Type = JnxoptIfOTNType
_JnxoptIfOTNPMFECPrevDayType_Object = MibTableColumn
jnxoptIfOTNPMFECPrevDayType = _JnxoptIfOTNPMFECPrevDayType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 1),
    _JnxoptIfOTNPMFECPrevDayType_Type()
)
jnxoptIfOTNPMFECPrevDayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDayType.setStatus("current")
_JnxoptIfOTNPMFECPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTNPMFECPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTNPMFECPrevDaySuspectedFlag = _JnxoptIfOTNPMFECPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 2),
    _JnxoptIfOTNPMFECPrevDaySuspectedFlag_Type()
)
jnxoptIfOTNPMFECPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOTNPMPrevDayFECCorrectedErr_Type = Counter64
_JnxoptIfOTNPMPrevDayFECCorrectedErr_Object = MibTableColumn
jnxoptIfOTNPMPrevDayFECCorrectedErr = _JnxoptIfOTNPMPrevDayFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 3),
    _JnxoptIfOTNPMPrevDayFECCorrectedErr_Type()
)
jnxoptIfOTNPMPrevDayFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayFECCorrectedErr.setStatus("current")
_JnxoptIfOTNPMPrevDayFECUncorrectedWords_Type = Counter64
_JnxoptIfOTNPMPrevDayFECUncorrectedWords_Object = MibTableColumn
jnxoptIfOTNPMPrevDayFECUncorrectedWords = _JnxoptIfOTNPMPrevDayFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 4),
    _JnxoptIfOTNPMPrevDayFECUncorrectedWords_Type()
)
jnxoptIfOTNPMPrevDayFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayFECUncorrectedWords.setStatus("current")
_JnxoptIfOTNPMPrevDayMinFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMPrevDayMinFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMPrevDayMinFECBERMantissa = _JnxoptIfOTNPMPrevDayMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 5),
    _JnxoptIfOTNPMPrevDayMinFECBERMantissa_Type()
)
jnxoptIfOTNPMPrevDayMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayMinFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMPrevDayMinFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMPrevDayMinFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMPrevDayMinFECBERExponent = _JnxoptIfOTNPMPrevDayMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 6),
    _JnxoptIfOTNPMPrevDayMinFECBERExponent_Type()
)
jnxoptIfOTNPMPrevDayMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayMinFECBERExponent.setStatus("current")
_JnxoptIfOTNPMPrevDayMaxFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMPrevDayMaxFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMPrevDayMaxFECBERMantissa = _JnxoptIfOTNPMPrevDayMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 7),
    _JnxoptIfOTNPMPrevDayMaxFECBERMantissa_Type()
)
jnxoptIfOTNPMPrevDayMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayMaxFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMPrevDayMaxFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMPrevDayMaxFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMPrevDayMaxFECBERExponent = _JnxoptIfOTNPMPrevDayMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 8),
    _JnxoptIfOTNPMPrevDayMaxFECBERExponent_Type()
)
jnxoptIfOTNPMPrevDayMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayMaxFECBERExponent.setStatus("current")
_JnxoptIfOTNPMPrevDayAvgFECBERMantissa_Type = Unsigned32
_JnxoptIfOTNPMPrevDayAvgFECBERMantissa_Object = MibTableColumn
jnxoptIfOTNPMPrevDayAvgFECBERMantissa = _JnxoptIfOTNPMPrevDayAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 9),
    _JnxoptIfOTNPMPrevDayAvgFECBERMantissa_Type()
)
jnxoptIfOTNPMPrevDayAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayAvgFECBERMantissa.setStatus("current")
_JnxoptIfOTNPMPrevDayAvgFECBERExponent_Type = Unsigned32
_JnxoptIfOTNPMPrevDayAvgFECBERExponent_Object = MibTableColumn
jnxoptIfOTNPMPrevDayAvgFECBERExponent = _JnxoptIfOTNPMPrevDayAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 10),
    _JnxoptIfOTNPMPrevDayAvgFECBERExponent_Type()
)
jnxoptIfOTNPMPrevDayAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMPrevDayAvgFECBERExponent.setStatus("current")
_JnxoptIfOTNPMFECPrevDayTimeStamp_Type = DateAndTime
_JnxoptIfOTNPMFECPrevDayTimeStamp_Object = MibTableColumn
jnxoptIfOTNPMFECPrevDayTimeStamp = _JnxoptIfOTNPMFECPrevDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 11),
    _JnxoptIfOTNPMFECPrevDayTimeStamp_Type()
)
jnxoptIfOTNPMFECPrevDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDayTimeStamp.setStatus("current")
_JnxoptIfOTNPMFECPrevDaySuspectReason_Type = Integer32
_JnxoptIfOTNPMFECPrevDaySuspectReason_Object = MibTableColumn
jnxoptIfOTNPMFECPrevDaySuspectReason = _JnxoptIfOTNPMFECPrevDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 3, 11, 1, 12),
    _JnxoptIfOTNPMFECPrevDaySuspectReason_Type()
)
jnxoptIfOTNPMFECPrevDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTNPMFECPrevDaySuspectReason.setStatus("current")
_JnxoptIfOTNAlarm_ObjectIdentity = ObjectIdentity
jnxoptIfOTNAlarm = _JnxoptIfOTNAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4)
)
_JnxoptIfOTNAlarmTable_Object = MibTable
jnxoptIfOTNAlarmTable = _JnxoptIfOTNAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmTable.setStatus("current")
_JnxoptIfOTNAlarmEntry_Object = MibTableRow
jnxoptIfOTNAlarmEntry = _JnxoptIfOTNAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1)
)
jnxoptIfOTNAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmEntry.setStatus("current")
_JnxoptIfOTNAlarmLocation_Type = JnxoptIfOTNType
_JnxoptIfOTNAlarmLocation_Object = MibTableColumn
jnxoptIfOTNAlarmLocation = _JnxoptIfOTNAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 1),
    _JnxoptIfOTNAlarmLocation_Type()
)
jnxoptIfOTNAlarmLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmLocation.setStatus("current")
_JnxoptIfOTNAlarmDirection_Type = JnxoptIfOTNDirection
_JnxoptIfOTNAlarmDirection_Object = MibTableColumn
jnxoptIfOTNAlarmDirection = _JnxoptIfOTNAlarmDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 2),
    _JnxoptIfOTNAlarmDirection_Type()
)
jnxoptIfOTNAlarmDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmDirection.setStatus("current")
_JnxoptIfOTNAlarmLayer_Type = JnxoptIfOTNLayer
_JnxoptIfOTNAlarmLayer_Object = MibTableColumn
jnxoptIfOTNAlarmLayer = _JnxoptIfOTNAlarmLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 3),
    _JnxoptIfOTNAlarmLayer_Type()
)
jnxoptIfOTNAlarmLayer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmLayer.setStatus("current")
_JnxoptIfOTNAlarmTCMLevel_Type = Unsigned32
_JnxoptIfOTNAlarmTCMLevel_Object = MibTableColumn
jnxoptIfOTNAlarmTCMLevel = _JnxoptIfOTNAlarmTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 4),
    _JnxoptIfOTNAlarmTCMLevel_Type()
)
jnxoptIfOTNAlarmTCMLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmTCMLevel.setStatus("current")
_JnxoptIfOTNOChOTUkAlarmType_Type = JnxoptIfOTNOChAlarms
_JnxoptIfOTNOChOTUkAlarmType_Object = MibTableColumn
jnxoptIfOTNOChOTUkAlarmType = _JnxoptIfOTNOChOTUkAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 5),
    _JnxoptIfOTNOChOTUkAlarmType_Type()
)
jnxoptIfOTNOChOTUkAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNOChOTUkAlarmType.setStatus("current")
_JnxoptIfOTNAlarmSeverity_Type = JnxoptIfOTNAlarmSeverity
_JnxoptIfOTNAlarmSeverity_Object = MibTableColumn
jnxoptIfOTNAlarmSeverity = _JnxoptIfOTNAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 6),
    _JnxoptIfOTNAlarmSeverity_Type()
)
jnxoptIfOTNAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmSeverity.setStatus("current")
_JnxoptIfOTNAlarmDate_Type = DateAndTime
_JnxoptIfOTNAlarmDate_Object = MibTableColumn
jnxoptIfOTNAlarmDate = _JnxoptIfOTNAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 7),
    _JnxoptIfOTNAlarmDate_Type()
)
jnxoptIfOTNAlarmDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNAlarmDate.setStatus("current")
_JnxoptIfOTNODUkTcmAlarmType_Type = JnxoptIfOTNODUkTcmAlarms
_JnxoptIfOTNODUkTcmAlarmType_Object = MibTableColumn
jnxoptIfOTNODUkTcmAlarmType = _JnxoptIfOTNODUkTcmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 4, 1, 1, 8),
    _JnxoptIfOTNODUkTcmAlarmType_Type()
)
jnxoptIfOTNODUkTcmAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxoptIfOTNODUkTcmAlarmType.setStatus("current")
jnxoptIfOChConfigEntry.registerAugmentions(
    ("JNX-OPT-IF-EXT-MIB",
     "jnxoptIfOChConfigExtEntry")
)
jnxoptIfOChConfigExtEntry.setIndexNames(*jnxoptIfOChConfigEntry.getIndexNames())
jnxoptIfOChSinkCurrentEntry.registerAugmentions(
    ("JNX-OPT-IF-EXT-MIB",
     "jnxoptIfOChSinkCurrentExtEntry")
)
jnxoptIfOChSinkCurrentExtEntry.setIndexNames(*jnxoptIfOChSinkCurrentEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxoptIfOTNOChOTUkAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 0, 1)
)
jnxoptIfOTNOChOTUkAlarmSet.setObjects(
      *(("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLocation"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDirection"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLayer"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmTCMLevel"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNOChOTUkAlarmType"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmSeverity"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTNOChOTUkAlarmSet.setStatus(
        "current"
    )

jnxoptIfOTNOChOTUkAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 0, 2)
)
jnxoptIfOTNOChOTUkAlarmClear.setObjects(
      *(("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLocation"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDirection"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLayer"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmTCMLevel"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNOChOTUkAlarmType"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmSeverity"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTNOChOTUkAlarmClear.setStatus(
        "current"
    )

jnxoptIfOTNODUkTcmAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 0, 3)
)
jnxoptIfOTNODUkTcmAlarmSet.setObjects(
      *(("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLocation"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDirection"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLayer"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmTCMLevel"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNODUkTcmAlarmType"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmSeverity"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTNODUkTcmAlarmSet.setStatus(
        "current"
    )

jnxoptIfOTNODUkTcmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 3, 0, 4)
)
jnxoptIfOTNODUkTcmAlarmClear.setObjects(
      *(("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLocation"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDirection"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmLayer"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmTCMLevel"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNODUkTcmAlarmType"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmSeverity"),
        ("JNX-OPT-IF-EXT-MIB", "jnxoptIfOTNAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTNODUkTcmAlarmClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-OPT-IF-EXT-MIB",
    **{"JnxoptIfChannelSpacing": JnxoptIfChannelSpacing,
       "JnxoptIfBitRateLineCoding": JnxoptIfBitRateLineCoding,
       "JnxoptIfFiberTypeRecommendation": JnxoptIfFiberTypeRecommendation,
       "JnxoptIfFiberTypeCategory": JnxoptIfFiberTypeCategory,
       "JnxoptIfOTNType": JnxoptIfOTNType,
       "JnxoptIfOTNDirection": JnxoptIfOTNDirection,
       "JnxoptIfOTNLayer": JnxoptIfOTNLayer,
       "JnxoptIfOTNOChAlarms": JnxoptIfOTNOChAlarms,
       "JnxoptIfOTNODUkTcmAlarms": JnxoptIfOTNODUkTcmAlarms,
       "JnxoptIfOTNAlarmSeverity": JnxoptIfOTNAlarmSeverity,
       "jnxoptIfExtMibModule": jnxoptIfExtMibModule,
       "jnxoptIfOTNNotifications": jnxoptIfOTNNotifications,
       "jnxoptIfOTNOChOTUkAlarmSet": jnxoptIfOTNOChOTUkAlarmSet,
       "jnxoptIfOTNOChOTUkAlarmClear": jnxoptIfOTNOChOTUkAlarmClear,
       "jnxoptIfOTNODUkTcmAlarmSet": jnxoptIfOTNODUkTcmAlarmSet,
       "jnxoptIfOTNODUkTcmAlarmClear": jnxoptIfOTNODUkTcmAlarmClear,
       "jnxoptIfOPSmEntry": jnxoptIfOPSmEntry,
       "jnxoptIfOPSmConfigTable": jnxoptIfOPSmConfigTable,
       "jnxoptIfOPSmConfigEntry": jnxoptIfOPSmConfigEntry,
       "jnxoptIfOPSmDirectionality": jnxoptIfOPSmDirectionality,
       "jnxoptIfOPSmFiberTypeRecommendation": jnxoptIfOPSmFiberTypeRecommendation,
       "jnxoptIfOPSmFiberTypeCategory": jnxoptIfOPSmFiberTypeCategory,
       "jnxoptIfOChSrcSinkGroup": jnxoptIfOChSrcSinkGroup,
       "jnxoptIfOChConfigExtTable": jnxoptIfOChConfigExtTable,
       "jnxoptIfOChConfigExtEntry": jnxoptIfOChConfigExtEntry,
       "jnxoptIfOChMiminumChannelSpacing": jnxoptIfOChMiminumChannelSpacing,
       "jnxoptIfOChBitRateLineCoding": jnxoptIfOChBitRateLineCoding,
       "jnxoptIfOChFEC": jnxoptIfOChFEC,
       "jnxoptIfOChSinkMaximumBERMantissa": jnxoptIfOChSinkMaximumBERMantissa,
       "jnxoptIfOChSinkMaximumBERExponent": jnxoptIfOChSinkMaximumBERExponent,
       "jnxoptIfOChMinWavelength": jnxoptIfOChMinWavelength,
       "jnxoptIfOChMaxWavelength": jnxoptIfOChMaxWavelength,
       "jnxoptIfOChWavelength": jnxoptIfOChWavelength,
       "jnxoptIfOChVendorTransceiverClass": jnxoptIfOChVendorTransceiverClass,
       "jnxoptIfOChOpticalInterfaceApplicationCode": jnxoptIfOChOpticalInterfaceApplicationCode,
       "jnxoptIfOChLaserAdminState": jnxoptIfOChLaserAdminState,
       "jnxoptIfOChLaserOperationalState": jnxoptIfOChLaserOperationalState,
       "jnxoptIfOChAdminState": jnxoptIfOChAdminState,
       "jnxoptIfOChOperationalState": jnxoptIfOChOperationalState,
       "jnxoptIfOChSrcConfigTable": jnxoptIfOChSrcConfigTable,
       "jnxoptIfOChSrcConfigEntry": jnxoptIfOChSrcConfigEntry,
       "jnxoptIfOChMinimumMeanChannelOutputPower": jnxoptIfOChMinimumMeanChannelOutputPower,
       "jnxoptIfOChMaximumMeanChannelOutputPower": jnxoptIfOChMaximumMeanChannelOutputPower,
       "jnxoptIfOChMinimumCentralFrequency": jnxoptIfOChMinimumCentralFrequency,
       "jnxoptIfOChMaximumCentralFrequency": jnxoptIfOChMaximumCentralFrequency,
       "jnxoptIfOChMaximumSpectralExcursion": jnxoptIfOChMaximumSpectralExcursion,
       "jnxoptIfOChMaximumTxDispersionOSNRPenalty": jnxoptIfOChMaximumTxDispersionOSNRPenalty,
       "jnxoptIfOChSrcSinkConfigTable": jnxoptIfOChSrcSinkConfigTable,
       "jnxoptIfOChSrcSinkConfigEntry": jnxoptIfOChSrcSinkConfigEntry,
       "jnxoptIfOChSrcSinkMinimumChromaticDispersion": jnxoptIfOChSrcSinkMinimumChromaticDispersion,
       "jnxoptIfOChSrcSinkMaximumChromaticDispersion": jnxoptIfOChSrcSinkMaximumChromaticDispersion,
       "jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss": jnxoptIfOChSrcSinkMinimumSrcOpticalReturnLoss,
       "jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink": jnxoptIfOChSrcSinkMaximumDiscreteReflectanceSrcToSink,
       "jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay": jnxoptIfOChSrcSinkMaximumDifferentialGroupDelay,
       "jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss": jnxoptIfOChSrcSinkMaximumPolarisationDependentLoss,
       "jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk": jnxoptIfOChSrcSinkMaximumInterChannelCrosstalk,
       "jnxoptIfOChSrcSinkInterFerometricCrosstalk": jnxoptIfOChSrcSinkInterFerometricCrosstalk,
       "jnxoptIfOChSrcSinkOpticalPathOSNRPenalty": jnxoptIfOChSrcSinkOpticalPathOSNRPenalty,
       "jnxoptIfOChSinkConfigTable": jnxoptIfOChSinkConfigTable,
       "jnxoptIfOChSinkConfigEntry": jnxoptIfOChSinkConfigEntry,
       "jnxoptIfOChSinkMinimumMeanIntputPower": jnxoptIfOChSinkMinimumMeanIntputPower,
       "jnxoptIfOChSinkMaximumMeanIntputPower": jnxoptIfOChSinkMaximumMeanIntputPower,
       "jnxoptIfOChSinkMinimumOSNR": jnxoptIfOChSinkMinimumOSNR,
       "jnxoptIfOChSinkOSNRTolerance": jnxoptIfOChSinkOSNRTolerance,
       "jnxoptIfOTNPMGroup": jnxoptIfOTNPMGroup,
       "jnxoptIfOChSinkCurrentExtTable": jnxoptIfOChSinkCurrentExtTable,
       "jnxoptIfOChSinkCurrentExtEntry": jnxoptIfOChSinkCurrentExtEntry,
       "jnxoptIfOChSinkCurrentChromaticDispersion": jnxoptIfOChSinkCurrentChromaticDispersion,
       "jnxoptIfOChSinkCurrentOSNR": jnxoptIfOChSinkCurrentOSNR,
       "jnxoptIfOChSinkCurrentQ": jnxoptIfOChSinkCurrentQ,
       "jnxoptIfOTNPMConfigTable": jnxoptIfOTNPMConfigTable,
       "jnxoptIfOTNPMConfigEntry": jnxoptIfOTNPMConfigEntry,
       "jnxoptIfOTNPMConfigType": jnxoptIfOTNPMConfigType,
       "jnxoptIfOTNPMConfigLayer": jnxoptIfOTNPMConfigLayer,
       "jnxoptIfOTNPMConfigTCMLevel": jnxoptIfOTNPMConfigTCMLevel,
       "jnxoptIfOTNPMESRInterval": jnxoptIfOTNPMESRInterval,
       "jnxoptIfOTNPMSESRInterval": jnxoptIfOTNPMSESRInterval,
       "jnxoptIfOTNPMValidIntervals": jnxoptIfOTNPMValidIntervals,
       "jnxoptIfOTNPM15MinBip8Threshold": jnxoptIfOTNPM15MinBip8Threshold,
       "jnxoptIfOTNPM15MinESsThreshold": jnxoptIfOTNPM15MinESsThreshold,
       "jnxoptIfOTNPM15MinSESsThreshold": jnxoptIfOTNPM15MinSESsThreshold,
       "jnxoptIfOTNPM15MinUASsThreshold": jnxoptIfOTNPM15MinUASsThreshold,
       "jnxoptIfOTNPM15MinBBEsThreshold": jnxoptIfOTNPM15MinBBEsThreshold,
       "jnxoptIfOTNPM24HourBip8Threshold": jnxoptIfOTNPM24HourBip8Threshold,
       "jnxoptIfOTNPM24HourESsThreshold": jnxoptIfOTNPM24HourESsThreshold,
       "jnxoptIfOTNPM24HourSESsThreshold": jnxoptIfOTNPM24HourSESsThreshold,
       "jnxoptIfOTNPM24HourUASsThreshold": jnxoptIfOTNPM24HourUASsThreshold,
       "jnxoptIfOTNPM24HourBBEsThreshold": jnxoptIfOTNPM24HourBBEsThreshold,
       "jnxoptIfOTNPMBip8EnableTCA": jnxoptIfOTNPMBip8EnableTCA,
       "jnxoptIfOTNPMESsEnableTCA": jnxoptIfOTNPMESsEnableTCA,
       "jnxoptIfOTNPMSESsEnableTCA": jnxoptIfOTNPMSESsEnableTCA,
       "jnxoptIfOTNPMUASsEnableTCA": jnxoptIfOTNPMUASsEnableTCA,
       "jnxoptIfOTNPMBBEsEnableTCA": jnxoptIfOTNPMBBEsEnableTCA,
       "jnxoptIfOTNPMCurrentTable": jnxoptIfOTNPMCurrentTable,
       "jnxoptIfOTNPMCurrentEntry": jnxoptIfOTNPMCurrentEntry,
       "jnxoptIfOTNPMCurrentType": jnxoptIfOTNPMCurrentType,
       "jnxoptIfOTNPMCurrentLayer": jnxoptIfOTNPMCurrentLayer,
       "jnxoptIfOTNPMCurrentTCMLevel": jnxoptIfOTNPMCurrentTCMLevel,
       "jnxoptIfOTNPMCurrentSuspectedFlag": jnxoptIfOTNPMCurrentSuspectedFlag,
       "jnxoptIfOTNPMCurrentBip8": jnxoptIfOTNPMCurrentBip8,
       "jnxoptIfOTNPMCurrentESs": jnxoptIfOTNPMCurrentESs,
       "jnxoptIfOTNPMCurrentSESs": jnxoptIfOTNPMCurrentSESs,
       "jnxoptIfOTNPMCurrentUASs": jnxoptIfOTNPMCurrentUASs,
       "jnxoptIfOTNPMCurrentBBEs": jnxoptIfOTNPMCurrentBBEs,
       "jnxoptIfOTNPMCurrentESR": jnxoptIfOTNPMCurrentESR,
       "jnxoptIfOTNPMCurrentSESR": jnxoptIfOTNPMCurrentSESR,
       "jnxoptIfOTNPMCurrentBBER": jnxoptIfOTNPMCurrentBBER,
       "jnxoptIfOTNPMCurrentElapsedTime": jnxoptIfOTNPMCurrentElapsedTime,
       "jnxoptIfOTNPMCurSuspectReason": jnxoptIfOTNPMCurSuspectReason,
       "jnxoptIfOTNPMIntervalTable": jnxoptIfOTNPMIntervalTable,
       "jnxoptIfOTNPMIntervalEntry": jnxoptIfOTNPMIntervalEntry,
       "jnxoptIfOTNPMIntervalType": jnxoptIfOTNPMIntervalType,
       "jnxoptIfOTNPMIntervalLayer": jnxoptIfOTNPMIntervalLayer,
       "jnxoptIfOTNPMIntervalTCMLevel": jnxoptIfOTNPMIntervalTCMLevel,
       "jnxoptIfOTNPMIntervalNumber": jnxoptIfOTNPMIntervalNumber,
       "jnxoptIfOTNPMIntervalSuspectedFlag": jnxoptIfOTNPMIntervalSuspectedFlag,
       "jnxoptIfOTNPMIntervalBip8": jnxoptIfOTNPMIntervalBip8,
       "jnxoptIfOTNPMIntervalESs": jnxoptIfOTNPMIntervalESs,
       "jnxoptIfOTNPMIntervalSESs": jnxoptIfOTNPMIntervalSESs,
       "jnxoptIfOTNPMIntervalUASs": jnxoptIfOTNPMIntervalUASs,
       "jnxoptIfOTNPMIntervalBBEs": jnxoptIfOTNPMIntervalBBEs,
       "jnxoptIfOTNPMIntervalESR": jnxoptIfOTNPMIntervalESR,
       "jnxoptIfOTNPMIntervalSESR": jnxoptIfOTNPMIntervalSESR,
       "jnxoptIfOTNPMIntervalBBER": jnxoptIfOTNPMIntervalBBER,
       "jnxoptIfOTNPMIntervalTimeStamp": jnxoptIfOTNPMIntervalTimeStamp,
       "jnxoptIfOTNPMIntSuspectReason": jnxoptIfOTNPMIntSuspectReason,
       "jnxoptIfOTNPMCurrentDayTable": jnxoptIfOTNPMCurrentDayTable,
       "jnxoptIfOTNPMCurrentDayEntry": jnxoptIfOTNPMCurrentDayEntry,
       "jnxoptIfOTNPMCurrentDayType": jnxoptIfOTNPMCurrentDayType,
       "jnxoptIfOTNPMCurrentDayLayer": jnxoptIfOTNPMCurrentDayLayer,
       "jnxoptIfOTNPMCurrentDayTCMLevel": jnxoptIfOTNPMCurrentDayTCMLevel,
       "jnxoptIfOTNPMCurrentDaySuspectedFlag": jnxoptIfOTNPMCurrentDaySuspectedFlag,
       "jnxoptIfOTNPMCurrentDayBip8": jnxoptIfOTNPMCurrentDayBip8,
       "jnxoptIfOTNPMCurrentDayESs": jnxoptIfOTNPMCurrentDayESs,
       "jnxoptIfOTNPMCurrentDaySESs": jnxoptIfOTNPMCurrentDaySESs,
       "jnxoptIfOTNPMCurrentDayUASs": jnxoptIfOTNPMCurrentDayUASs,
       "jnxoptIfOTNPMCurrentDayBBEs": jnxoptIfOTNPMCurrentDayBBEs,
       "jnxoptIfOTNPMCurrentDayESR": jnxoptIfOTNPMCurrentDayESR,
       "jnxoptIfOTNPMCurrentDaySESR": jnxoptIfOTNPMCurrentDaySESR,
       "jnxoptIfOTNPMCurrentDayBBER": jnxoptIfOTNPMCurrentDayBBER,
       "jnxoptIfOTNPMCurrentDayElapsedTime": jnxoptIfOTNPMCurrentDayElapsedTime,
       "jnxoptIfOTNPMCurDaySuspectReason": jnxoptIfOTNPMCurDaySuspectReason,
       "jnxoptIfOTNPMPrevDayTable": jnxoptIfOTNPMPrevDayTable,
       "jnxoptIfOTNPMPrevDayEntry": jnxoptIfOTNPMPrevDayEntry,
       "jnxoptIfOTNPMPrevDayType": jnxoptIfOTNPMPrevDayType,
       "jnxoptIfOTNPMPrevDayLayer": jnxoptIfOTNPMPrevDayLayer,
       "jnxoptIfOTNPMPrevDayTCMLevel": jnxoptIfOTNPMPrevDayTCMLevel,
       "jnxoptIfOTNPMPrevDaySuspectedFlag": jnxoptIfOTNPMPrevDaySuspectedFlag,
       "jnxoptIfOTNPMPrevDayBip8": jnxoptIfOTNPMPrevDayBip8,
       "jnxoptIfOTNPMPrevDayESs": jnxoptIfOTNPMPrevDayESs,
       "jnxoptIfOTNPMPrevDaySESs": jnxoptIfOTNPMPrevDaySESs,
       "jnxoptIfOTNPMPrevDayUASs": jnxoptIfOTNPMPrevDayUASs,
       "jnxoptIfOTNPMPrevDayBBEs": jnxoptIfOTNPMPrevDayBBEs,
       "jnxoptIfOTNPMPrevDayESR": jnxoptIfOTNPMPrevDayESR,
       "jnxoptIfOTNPMPrevDaySESR": jnxoptIfOTNPMPrevDaySESR,
       "jnxoptIfOTNPMPrevDayBBER": jnxoptIfOTNPMPrevDayBBER,
       "jnxoptIfOTNPMPrevDayTimeStamp": jnxoptIfOTNPMPrevDayTimeStamp,
       "jnxoptIfOTNPMPrevDaySuspectReason": jnxoptIfOTNPMPrevDaySuspectReason,
       "jnxoptIfOTNPMFECConfigTable": jnxoptIfOTNPMFECConfigTable,
       "jnxoptIfOTNPMFECConfigEntry": jnxoptIfOTNPMFECConfigEntry,
       "jnxoptIfOTNPMFECConfigType": jnxoptIfOTNPMFECConfigType,
       "jnxoptIfOTNPMFECValidIntervals": jnxoptIfOTNPMFECValidIntervals,
       "jnxoptIfOTNPM15MinPreFECBERMantissaThreshold": jnxoptIfOTNPM15MinPreFECBERMantissaThreshold,
       "jnxoptIfOTNPM15MinPreFECBERExponentThreshold": jnxoptIfOTNPM15MinPreFECBERExponentThreshold,
       "jnxoptIfOTNPM24HourPreFECBERMantissaThreshold": jnxoptIfOTNPM24HourPreFECBERMantissaThreshold,
       "jnxoptIfOTNPM24HourPreFECBERExponentThreshold": jnxoptIfOTNPM24HourPreFECBERExponentThreshold,
       "jnxoptIfOTNPMFECBEREnableTCA": jnxoptIfOTNPMFECBEREnableTCA,
       "jnxoptIfOTNPMFECCurrentTable": jnxoptIfOTNPMFECCurrentTable,
       "jnxoptIfOTNPMFECCurrentEntry": jnxoptIfOTNPMFECCurrentEntry,
       "jnxoptIfOTNPMFECCurrentType": jnxoptIfOTNPMFECCurrentType,
       "jnxoptIfOTNPMFECCurrentSuspectedFlag": jnxoptIfOTNPMFECCurrentSuspectedFlag,
       "jnxoptIfOTNPMCurrentFECCorrectedErr": jnxoptIfOTNPMCurrentFECCorrectedErr,
       "jnxoptIfOTNPMCurrentFECUncorrectedWords": jnxoptIfOTNPMCurrentFECUncorrectedWords,
       "jnxoptIfOTNPMCurrentFECBERMantissa": jnxoptIfOTNPMCurrentFECBERMantissa,
       "jnxoptIfOTNPMCurrentFECBERExponent": jnxoptIfOTNPMCurrentFECBERExponent,
       "jnxoptIfOTNPMCurrentFECMinBERMantissa": jnxoptIfOTNPMCurrentFECMinBERMantissa,
       "jnxoptIfOTNPMCurrentFECMinBERExponent": jnxoptIfOTNPMCurrentFECMinBERExponent,
       "jnxoptIfOTNPMCurrentFECMaxBERMantissa": jnxoptIfOTNPMCurrentFECMaxBERMantissa,
       "jnxoptIfOTNPMCurrentFECMaxBERExponent": jnxoptIfOTNPMCurrentFECMaxBERExponent,
       "jnxoptIfOTNPMCurrentFECAvgBERMantissa": jnxoptIfOTNPMCurrentFECAvgBERMantissa,
       "jnxoptIfOTNPMCurrentFECAvgBERExponent": jnxoptIfOTNPMCurrentFECAvgBERExponent,
       "jnxoptIfOTNPMCurrentFECElapsedTime": jnxoptIfOTNPMCurrentFECElapsedTime,
       "jnxoptIfOTNPMFECCurSuspectReason": jnxoptIfOTNPMFECCurSuspectReason,
       "jnxoptIfOTNPMFECIntervalTable": jnxoptIfOTNPMFECIntervalTable,
       "jnxoptIfOTNPMFECIntervalEntry": jnxoptIfOTNPMFECIntervalEntry,
       "jnxoptIfOTNPMFECIntervalType": jnxoptIfOTNPMFECIntervalType,
       "jnxoptIfOTNPMFECIntervalNumber": jnxoptIfOTNPMFECIntervalNumber,
       "jnxoptIfOTNPMFECIntervalSuspectedFlag": jnxoptIfOTNPMFECIntervalSuspectedFlag,
       "jnxoptIfOTNPMIntervalFECCorrectedErr": jnxoptIfOTNPMIntervalFECCorrectedErr,
       "jnxoptIfOTNPMIntervalFECUncorrectedWords": jnxoptIfOTNPMIntervalFECUncorrectedWords,
       "jnxoptIfOTNPMIntervalMinFECBERMantissa": jnxoptIfOTNPMIntervalMinFECBERMantissa,
       "jnxoptIfOTNPMIntervalMinFECBERExponent": jnxoptIfOTNPMIntervalMinFECBERExponent,
       "jnxoptIfOTNPMIntervalMaxFECBERMantissa": jnxoptIfOTNPMIntervalMaxFECBERMantissa,
       "jnxoptIfOTNPMIntervalMaxFECBERExponent": jnxoptIfOTNPMIntervalMaxFECBERExponent,
       "jnxoptIfOTNPMIntervalAvgFECBERMantissa": jnxoptIfOTNPMIntervalAvgFECBERMantissa,
       "jnxoptIfOTNPMIntervalAvgFECBERExponent": jnxoptIfOTNPMIntervalAvgFECBERExponent,
       "jnxoptIfOTNPMFECIntervalTimeStamp": jnxoptIfOTNPMFECIntervalTimeStamp,
       "jnxoptIfOTNPMFECIntSuspectReason": jnxoptIfOTNPMFECIntSuspectReason,
       "jnxoptIfOTNPMFECCurrentDayTable": jnxoptIfOTNPMFECCurrentDayTable,
       "jnxoptIfOTNPMFECCurrentDayEntry": jnxoptIfOTNPMFECCurrentDayEntry,
       "jnxoptIfOTNPMFECCurrentDayType": jnxoptIfOTNPMFECCurrentDayType,
       "jnxoptIfOTNPMFECCurrentDaySuspectedFlag": jnxoptIfOTNPMFECCurrentDaySuspectedFlag,
       "jnxoptIfOTNPMCurrentDayFECCorrectedErr": jnxoptIfOTNPMCurrentDayFECCorrectedErr,
       "jnxoptIfOTNPMCurrentDayFECUncorrectedWords": jnxoptIfOTNPMCurrentDayFECUncorrectedWords,
       "jnxoptIfOTNPMCurrentDayMinFECBERMantissa": jnxoptIfOTNPMCurrentDayMinFECBERMantissa,
       "jnxoptIfOTNPMCurrentDayMinFECBERExponent": jnxoptIfOTNPMCurrentDayMinFECBERExponent,
       "jnxoptIfOTNPMCurrentDayMaxFECBERMantissa": jnxoptIfOTNPMCurrentDayMaxFECBERMantissa,
       "jnxoptIfOTNPMCurrentDayMaxFECBERExponent": jnxoptIfOTNPMCurrentDayMaxFECBERExponent,
       "jnxoptIfOTNPMCurrentDayAvgFECBERMantissa": jnxoptIfOTNPMCurrentDayAvgFECBERMantissa,
       "jnxoptIfOTNPMCurrentDayAvgFECBERExponent": jnxoptIfOTNPMCurrentDayAvgFECBERExponent,
       "jnxoptIfOTNPMFECCurrentDayElapsedTime": jnxoptIfOTNPMFECCurrentDayElapsedTime,
       "jnxoptIfOTNPMFECCurDaySuspectReason": jnxoptIfOTNPMFECCurDaySuspectReason,
       "jnxoptIfOTNPMFECPrevDayTable": jnxoptIfOTNPMFECPrevDayTable,
       "jnxoptIfOTNPMFECPrevDayEntry": jnxoptIfOTNPMFECPrevDayEntry,
       "jnxoptIfOTNPMFECPrevDayType": jnxoptIfOTNPMFECPrevDayType,
       "jnxoptIfOTNPMFECPrevDaySuspectedFlag": jnxoptIfOTNPMFECPrevDaySuspectedFlag,
       "jnxoptIfOTNPMPrevDayFECCorrectedErr": jnxoptIfOTNPMPrevDayFECCorrectedErr,
       "jnxoptIfOTNPMPrevDayFECUncorrectedWords": jnxoptIfOTNPMPrevDayFECUncorrectedWords,
       "jnxoptIfOTNPMPrevDayMinFECBERMantissa": jnxoptIfOTNPMPrevDayMinFECBERMantissa,
       "jnxoptIfOTNPMPrevDayMinFECBERExponent": jnxoptIfOTNPMPrevDayMinFECBERExponent,
       "jnxoptIfOTNPMPrevDayMaxFECBERMantissa": jnxoptIfOTNPMPrevDayMaxFECBERMantissa,
       "jnxoptIfOTNPMPrevDayMaxFECBERExponent": jnxoptIfOTNPMPrevDayMaxFECBERExponent,
       "jnxoptIfOTNPMPrevDayAvgFECBERMantissa": jnxoptIfOTNPMPrevDayAvgFECBERMantissa,
       "jnxoptIfOTNPMPrevDayAvgFECBERExponent": jnxoptIfOTNPMPrevDayAvgFECBERExponent,
       "jnxoptIfOTNPMFECPrevDayTimeStamp": jnxoptIfOTNPMFECPrevDayTimeStamp,
       "jnxoptIfOTNPMFECPrevDaySuspectReason": jnxoptIfOTNPMFECPrevDaySuspectReason,
       "jnxoptIfOTNAlarm": jnxoptIfOTNAlarm,
       "jnxoptIfOTNAlarmTable": jnxoptIfOTNAlarmTable,
       "jnxoptIfOTNAlarmEntry": jnxoptIfOTNAlarmEntry,
       "jnxoptIfOTNAlarmLocation": jnxoptIfOTNAlarmLocation,
       "jnxoptIfOTNAlarmDirection": jnxoptIfOTNAlarmDirection,
       "jnxoptIfOTNAlarmLayer": jnxoptIfOTNAlarmLayer,
       "jnxoptIfOTNAlarmTCMLevel": jnxoptIfOTNAlarmTCMLevel,
       "jnxoptIfOTNOChOTUkAlarmType": jnxoptIfOTNOChOTUkAlarmType,
       "jnxoptIfOTNAlarmSeverity": jnxoptIfOTNAlarmSeverity,
       "jnxoptIfOTNAlarmDate": jnxoptIfOTNAlarmDate,
       "jnxoptIfOTNODUkTcmAlarmType": jnxoptIfOTNODUkTcmAlarmType}
)
