# SNMP MIB module (XEROX-GENERAL-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-GENERAL-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:14 2024
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

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmGeneralTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cardinal16(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class Cardinal32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Cardinal64High(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Cardinal64Low(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CodedCountry(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class CodedLanguage(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class CodeIndexedStringIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Counter64High(Counter32, TextualConvention):
    status = "current"


class Counter64Low(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Gauge64High(Gauge32, TextualConvention):
    status = "current"


class Gauge64Low(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Integer64High(Integer32, TextualConvention):
    status = "current"


class Integer64Low(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Ordinal16(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )



class Ordinal32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Ordinal64High(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Ordinal64Low(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmFixedLocaleDisplayString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmFixedLocaleUtf8String(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmNamedLocaleUtf8String(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmGenGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmGenLogFullPolicy(Integer32, TextualConvention):
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
        *(("disableAndPauseService", 4),
          ("disableService", 3),
          ("enableServiceAndFlushLog", 5),
          ("enableServiceAndFlushOldest", 6),
          ("other", 1),
          ("unknown", 2))
    )



class XcmGenMessageMapStringLabel(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class XcmGenNotifyDetailType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("notifyEventDelay", 21),
          ("notifyEventNames", 20),
          ("notifyMessageContentKeys", 32),
          ("notifyMessageContentText", 33),
          ("notifyMessageHeaderKeys", 30),
          ("notifyMessageHeaderText", 31),
          ("notifyRecipientURI", 10),
          ("notifySeverityFilter", 22),
          ("notifyTrainingFilter", 23),
          ("other", 1),
          ("unknown", 2))
    )



class XcmGenNotifySchemeSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmGenNotifySeverityFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmGenNotifyTrainingFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmGenOptionValueSyntax(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("integerCounter", 4),
          ("integerEnum", 5),
          ("integerGauge", 6),
          ("integerIndex", 7),
          ("integerNumber", 3),
          ("integerTruthValue", 8),
          ("oidAutonomous", 10),
          ("oidObject", 9),
          ("other", 1),
          ("stringBinary", 11),
          ("stringCodedCharSet", 14),
          ("stringDisplay", 12),
          ("stringDynamicLocalization", 15),
          ("stringLocalization", 13),
          ("stringUtf8Localization", 16),
          ("unknown", 2))
    )



class XcmGenReconfOptionState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("activateForImmediateChange", 6),
          ("activateForImmediateReboot", 8),
          ("activateForRebootChange", 7),
          ("activateInProgress", 9),
          ("idle", 1),
          ("validateForImmediateChange", 2),
          ("validateForImmediateReboot", 4),
          ("validateForRebootChange", 3),
          ("validateInProgress", 5))
    )



class XcmGenRowPersistence(Integer32, TextualConvention):
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
        *(("nonvolatile", 4),
          ("other", 1),
          ("permanent", 5),
          ("readonly", 6),
          ("unknown", 2),
          ("volatile", 3))
    )



class XcmGenSNMPDomain(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              20,
              21,
              30)
        )
    )
    namedValues = NamedValues(
        *(("snmpCLNSDomain", 2),
          ("snmpCONSDomain", 3),
          ("snmpDDPDomain", 4),
          ("snmpIPHostNameDomain", 21),
          ("snmpIPXDomain", 5),
          ("snmpNetBEUIDomain", 11),
          ("snmpNetBIOSDomain", 10),
          ("snmpTCPDomain", 20),
          ("snmpUDPDomain", 1),
          ("uriNotifyDomain", 30))
    )



class XcmGenSNMPVersion(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("snmpV1Community", 3),
          ("snmpV1Party", 4),
          ("snmpV2Community", 6),
          ("snmpV2Party", 5),
          ("snmpV2Secure", 9),
          ("snmpV2Star", 8),
          ("snmpV2Usec", 7),
          ("snmpV3Secure", 10),
          ("unknown", 1))
    )



class XcmGenSNMPv2ErrorStatus(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("authorizationError", 16),
          ("badValue", 3),
          ("commitFailed", 14),
          ("failedDueToPowerSaverState", 19),
          ("genErr", 5),
          ("inconsistentName", 18),
          ("inconsistentValue", 12),
          ("noAccess", 6),
          ("noCreation", 11),
          ("noError", 0),
          ("noSuchName", 2),
          ("notWritable", 17),
          ("readOnly", 4),
          ("requestTimedOut", 20),
          ("resourceUnavailable", 13),
          ("tooBig", 1),
          ("undoFailed", 15),
          ("wrongEncoding", 9),
          ("wrongLength", 8),
          ("wrongType", 7),
          ("wrongValue", 10))
    )



class XcmGlobalUniqueID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ZeroDotZero_ObjectIdentity = ObjectIdentity
zeroDotZero = _ZeroDotZero_ObjectIdentity(
    (0, 0)
)
_XcmGenZeroDotZero_ObjectIdentity = ObjectIdentity
xcmGenZeroDotZero = _XcmGenZeroDotZero_ObjectIdentity(
    (0, 0, 0)
)
if mibBuilder.loadTexts:
    xcmGenZeroDotZero.setStatus("current")
_XCmGeneralDummy_ObjectIdentity = ObjectIdentity
xCmGeneralDummy = _XCmGeneralDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999)
)
_XCmGenCardinal16_Type = Cardinal16
_XCmGenCardinal16_Object = MibScalar
xCmGenCardinal16 = _XCmGenCardinal16_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 1),
    _XCmGenCardinal16_Type()
)
xCmGenCardinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal16.setStatus("current")
_XCmGenCardinal32_Type = Cardinal32
_XCmGenCardinal32_Object = MibScalar
xCmGenCardinal32 = _XCmGenCardinal32_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 2),
    _XCmGenCardinal32_Type()
)
xCmGenCardinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal32.setStatus("current")
_XCmGenCardinal64High_Type = Cardinal64High
_XCmGenCardinal64High_Object = MibScalar
xCmGenCardinal64High = _XCmGenCardinal64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 3),
    _XCmGenCardinal64High_Type()
)
xCmGenCardinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal64High.setStatus("current")
_XCmGenCardinal64Low_Type = Cardinal64Low
_XCmGenCardinal64Low_Object = MibScalar
xCmGenCardinal64Low = _XCmGenCardinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 4),
    _XCmGenCardinal64Low_Type()
)
xCmGenCardinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCardinal64Low.setStatus("current")
_XCmGenCodedCountry_Type = CodedCountry
_XCmGenCodedCountry_Object = MibScalar
xCmGenCodedCountry = _XCmGenCodedCountry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 5),
    _XCmGenCodedCountry_Type()
)
xCmGenCodedCountry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodedCountry.setStatus("current")
_XCmGenCodedLanguage_Type = CodedLanguage
_XCmGenCodedLanguage_Object = MibScalar
xCmGenCodedLanguage = _XCmGenCodedLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 6),
    _XCmGenCodedLanguage_Type()
)
xCmGenCodedLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodedLanguage.setStatus("current")
_XCmGenCodeIndexedStringIndex_Type = CodeIndexedStringIndex
_XCmGenCodeIndexedStringIndex_Object = MibScalar
xCmGenCodeIndexedStringIndex = _XCmGenCodeIndexedStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 7),
    _XCmGenCodeIndexedStringIndex_Type()
)
xCmGenCodeIndexedStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCodeIndexedStringIndex.setStatus("current")
_XCmGenCounter64High_Type = Counter64High
_XCmGenCounter64High_Object = MibScalar
xCmGenCounter64High = _XCmGenCounter64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 8),
    _XCmGenCounter64High_Type()
)
xCmGenCounter64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCounter64High.setStatus("current")
_XCmGenCounter64Low_Type = Counter64Low
_XCmGenCounter64Low_Object = MibScalar
xCmGenCounter64Low = _XCmGenCounter64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 9),
    _XCmGenCounter64Low_Type()
)
xCmGenCounter64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenCounter64Low.setStatus("current")
_XCmGenGauge64High_Type = Gauge64High
_XCmGenGauge64High_Object = MibScalar
xCmGenGauge64High = _XCmGenGauge64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 10),
    _XCmGenGauge64High_Type()
)
xCmGenGauge64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGauge64High.setStatus("current")
_XCmGenGauge64Low_Type = Gauge64Low
_XCmGenGauge64Low_Object = MibScalar
xCmGenGauge64Low = _XCmGenGauge64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 11),
    _XCmGenGauge64Low_Type()
)
xCmGenGauge64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGauge64Low.setStatus("current")
_XCmGenInteger64High_Type = Integer64High
_XCmGenInteger64High_Object = MibScalar
xCmGenInteger64High = _XCmGenInteger64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 12),
    _XCmGenInteger64High_Type()
)
xCmGenInteger64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenInteger64High.setStatus("current")
_XCmGenInteger64Low_Type = Integer64Low
_XCmGenInteger64Low_Object = MibScalar
xCmGenInteger64Low = _XCmGenInteger64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 13),
    _XCmGenInteger64Low_Type()
)
xCmGenInteger64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenInteger64Low.setStatus("current")
_XCmGenOrdinal16_Type = Ordinal16
_XCmGenOrdinal16_Object = MibScalar
xCmGenOrdinal16 = _XCmGenOrdinal16_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 14),
    _XCmGenOrdinal16_Type()
)
xCmGenOrdinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal16.setStatus("current")
_XCmGenOrdinal32_Type = Ordinal32
_XCmGenOrdinal32_Object = MibScalar
xCmGenOrdinal32 = _XCmGenOrdinal32_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 15),
    _XCmGenOrdinal32_Type()
)
xCmGenOrdinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal32.setStatus("current")
_XCmGenOrdinal64High_Type = Ordinal64High
_XCmGenOrdinal64High_Object = MibScalar
xCmGenOrdinal64High = _XCmGenOrdinal64High_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 16),
    _XCmGenOrdinal64High_Type()
)
xCmGenOrdinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal64High.setStatus("current")
_XCmGenOrdinal64Low_Type = Ordinal64Low
_XCmGenOrdinal64Low_Object = MibScalar
xCmGenOrdinal64Low = _XCmGenOrdinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 17),
    _XCmGenOrdinal64Low_Type()
)
xCmGenOrdinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOrdinal64Low.setStatus("current")
_XCmGenFixedLocaleDisplayString_Type = XcmFixedLocaleDisplayString
_XCmGenFixedLocaleDisplayString_Object = MibScalar
xCmGenFixedLocaleDisplayString = _XCmGenFixedLocaleDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 18),
    _XCmGenFixedLocaleDisplayString_Type()
)
xCmGenFixedLocaleDisplayString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleDisplayString.setStatus("current")
_XCmGenGroupSupport_Type = XcmGenGroupSupport
_XCmGenGroupSupport_Object = MibScalar
xCmGenGroupSupport = _XCmGenGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 19),
    _XCmGenGroupSupport_Type()
)
xCmGenGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGroupSupport.setStatus("current")
_XCmGenLogFullPolicy_Type = XcmGenLogFullPolicy
_XCmGenLogFullPolicy_Object = MibScalar
xCmGenLogFullPolicy = _XCmGenLogFullPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 20),
    _XCmGenLogFullPolicy_Type()
)
xCmGenLogFullPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenLogFullPolicy.setStatus("current")
_XCmGenOptionValueSyntax_Type = XcmGenOptionValueSyntax
_XCmGenOptionValueSyntax_Object = MibScalar
xCmGenOptionValueSyntax = _XCmGenOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 21),
    _XCmGenOptionValueSyntax_Type()
)
xCmGenOptionValueSyntax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenOptionValueSyntax.setStatus("current")
_XCmGenReconfOptionState_Type = XcmGenReconfOptionState
_XCmGenReconfOptionState_Object = MibScalar
xCmGenReconfOptionState = _XCmGenReconfOptionState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 22),
    _XCmGenReconfOptionState_Type()
)
xCmGenReconfOptionState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenReconfOptionState.setStatus("current")
_XCmGenRowPersistence_Type = XcmGenRowPersistence
_XCmGenRowPersistence_Object = MibScalar
xCmGenRowPersistence = _XCmGenRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 23),
    _XCmGenRowPersistence_Type()
)
xCmGenRowPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenRowPersistence.setStatus("current")
_XCmGenSNMPDomain_Type = XcmGenSNMPDomain
_XCmGenSNMPDomain_Object = MibScalar
xCmGenSNMPDomain = _XCmGenSNMPDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 24),
    _XCmGenSNMPDomain_Type()
)
xCmGenSNMPDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPDomain.setStatus("current")
_XCmGenSNMPVersion_Type = XcmGenSNMPVersion
_XCmGenSNMPVersion_Object = MibScalar
xCmGenSNMPVersion = _XCmGenSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 25),
    _XCmGenSNMPVersion_Type()
)
xCmGenSNMPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPVersion.setStatus("current")
_XCmGenSNMPv2ErrorStatus_Type = XcmGenSNMPv2ErrorStatus
_XCmGenSNMPv2ErrorStatus_Object = MibScalar
xCmGenSNMPv2ErrorStatus = _XCmGenSNMPv2ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 26),
    _XCmGenSNMPv2ErrorStatus_Type()
)
xCmGenSNMPv2ErrorStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenSNMPv2ErrorStatus.setStatus("current")
_XCmGenGlobalUniqueID_Type = XcmGlobalUniqueID
_XCmGenGlobalUniqueID_Object = MibScalar
xCmGenGlobalUniqueID = _XCmGenGlobalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 27),
    _XCmGenGlobalUniqueID_Type()
)
xCmGenGlobalUniqueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenGlobalUniqueID.setStatus("current")
_XCmGenFixedLocaleUtf8String_Type = XcmFixedLocaleUtf8String
_XCmGenFixedLocaleUtf8String_Object = MibScalar
xCmGenFixedLocaleUtf8String = _XCmGenFixedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 28),
    _XCmGenFixedLocaleUtf8String_Type()
)
xCmGenFixedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenFixedLocaleUtf8String.setStatus("current")
_XCmGenMessageMapStringLabel_Type = XcmGenMessageMapStringLabel
_XCmGenMessageMapStringLabel_Object = MibScalar
xCmGenMessageMapStringLabel = _XCmGenMessageMapStringLabel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 29),
    _XCmGenMessageMapStringLabel_Type()
)
xCmGenMessageMapStringLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenMessageMapStringLabel.setStatus("current")
_XCmGenNamedLocaleUtf8String_Type = XcmNamedLocaleUtf8String
_XCmGenNamedLocaleUtf8String_Object = MibScalar
xCmGenNamedLocaleUtf8String = _XCmGenNamedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 30),
    _XCmGenNamedLocaleUtf8String_Type()
)
xCmGenNamedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNamedLocaleUtf8String.setStatus("current")
_XCmGenNotifySchemeSupport_Type = XcmGenNotifySchemeSupport
_XCmGenNotifySchemeSupport_Object = MibScalar
xCmGenNotifySchemeSupport = _XCmGenNotifySchemeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 31),
    _XCmGenNotifySchemeSupport_Type()
)
xCmGenNotifySchemeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifySchemeSupport.setStatus("current")
_XCmGenNotifySeverityFilter_Type = XcmGenNotifySeverityFilter
_XCmGenNotifySeverityFilter_Object = MibScalar
xCmGenNotifySeverityFilter = _XCmGenNotifySeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 32),
    _XCmGenNotifySeverityFilter_Type()
)
xCmGenNotifySeverityFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifySeverityFilter.setStatus("current")
_XCmGenNotifyTrainingFilter_Type = XcmGenNotifyTrainingFilter
_XCmGenNotifyTrainingFilter_Object = MibScalar
xCmGenNotifyTrainingFilter = _XCmGenNotifyTrainingFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 33),
    _XCmGenNotifyTrainingFilter_Type()
)
xCmGenNotifyTrainingFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifyTrainingFilter.setStatus("current")
_XCmGenNotifyDetailType_Type = XcmGenNotifyDetailType
_XCmGenNotifyDetailType_Object = MibScalar
xCmGenNotifyDetailType = _XCmGenNotifyDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 50, 999, 34),
    _XCmGenNotifyDetailType_Type()
)
xCmGenNotifyDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmGenNotifyDetailType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-GENERAL-TC",
    **{"Cardinal16": Cardinal16,
       "Cardinal32": Cardinal32,
       "Cardinal64High": Cardinal64High,
       "Cardinal64Low": Cardinal64Low,
       "CodedCountry": CodedCountry,
       "CodedLanguage": CodedLanguage,
       "CodeIndexedStringIndex": CodeIndexedStringIndex,
       "Counter64High": Counter64High,
       "Counter64Low": Counter64Low,
       "Gauge64High": Gauge64High,
       "Gauge64Low": Gauge64Low,
       "Integer64High": Integer64High,
       "Integer64Low": Integer64Low,
       "Ordinal16": Ordinal16,
       "Ordinal32": Ordinal32,
       "Ordinal64High": Ordinal64High,
       "Ordinal64Low": Ordinal64Low,
       "XcmFixedLocaleDisplayString": XcmFixedLocaleDisplayString,
       "XcmFixedLocaleUtf8String": XcmFixedLocaleUtf8String,
       "XcmNamedLocaleUtf8String": XcmNamedLocaleUtf8String,
       "XcmGenGroupSupport": XcmGenGroupSupport,
       "XcmGenLogFullPolicy": XcmGenLogFullPolicy,
       "XcmGenMessageMapStringLabel": XcmGenMessageMapStringLabel,
       "XcmGenNotifyDetailType": XcmGenNotifyDetailType,
       "XcmGenNotifySchemeSupport": XcmGenNotifySchemeSupport,
       "XcmGenNotifySeverityFilter": XcmGenNotifySeverityFilter,
       "XcmGenNotifyTrainingFilter": XcmGenNotifyTrainingFilter,
       "XcmGenOptionValueSyntax": XcmGenOptionValueSyntax,
       "XcmGenReconfOptionState": XcmGenReconfOptionState,
       "XcmGenRowPersistence": XcmGenRowPersistence,
       "XcmGenSNMPDomain": XcmGenSNMPDomain,
       "XcmGenSNMPVersion": XcmGenSNMPVersion,
       "XcmGenSNMPv2ErrorStatus": XcmGenSNMPv2ErrorStatus,
       "XcmGlobalUniqueID": XcmGlobalUniqueID,
       "zeroDotZero": zeroDotZero,
       "xcmGenZeroDotZero": xcmGenZeroDotZero,
       "xcmGeneralTC": xcmGeneralTC,
       "xCmGeneralDummy": xCmGeneralDummy,
       "xCmGenCardinal16": xCmGenCardinal16,
       "xCmGenCardinal32": xCmGenCardinal32,
       "xCmGenCardinal64High": xCmGenCardinal64High,
       "xCmGenCardinal64Low": xCmGenCardinal64Low,
       "xCmGenCodedCountry": xCmGenCodedCountry,
       "xCmGenCodedLanguage": xCmGenCodedLanguage,
       "xCmGenCodeIndexedStringIndex": xCmGenCodeIndexedStringIndex,
       "xCmGenCounter64High": xCmGenCounter64High,
       "xCmGenCounter64Low": xCmGenCounter64Low,
       "xCmGenGauge64High": xCmGenGauge64High,
       "xCmGenGauge64Low": xCmGenGauge64Low,
       "xCmGenInteger64High": xCmGenInteger64High,
       "xCmGenInteger64Low": xCmGenInteger64Low,
       "xCmGenOrdinal16": xCmGenOrdinal16,
       "xCmGenOrdinal32": xCmGenOrdinal32,
       "xCmGenOrdinal64High": xCmGenOrdinal64High,
       "xCmGenOrdinal64Low": xCmGenOrdinal64Low,
       "xCmGenFixedLocaleDisplayString": xCmGenFixedLocaleDisplayString,
       "xCmGenGroupSupport": xCmGenGroupSupport,
       "xCmGenLogFullPolicy": xCmGenLogFullPolicy,
       "xCmGenOptionValueSyntax": xCmGenOptionValueSyntax,
       "xCmGenReconfOptionState": xCmGenReconfOptionState,
       "xCmGenRowPersistence": xCmGenRowPersistence,
       "xCmGenSNMPDomain": xCmGenSNMPDomain,
       "xCmGenSNMPVersion": xCmGenSNMPVersion,
       "xCmGenSNMPv2ErrorStatus": xCmGenSNMPv2ErrorStatus,
       "xCmGenGlobalUniqueID": xCmGenGlobalUniqueID,
       "xCmGenFixedLocaleUtf8String": xCmGenFixedLocaleUtf8String,
       "xCmGenMessageMapStringLabel": xCmGenMessageMapStringLabel,
       "xCmGenNamedLocaleUtf8String": xCmGenNamedLocaleUtf8String,
       "xCmGenNotifySchemeSupport": xCmGenNotifySchemeSupport,
       "xCmGenNotifySeverityFilter": xCmGenNotifySeverityFilter,
       "xCmGenNotifyTrainingFilter": xCmGenNotifyTrainingFilter,
       "xCmGenNotifyDetailType": xCmGenNotifyDetailType}
)
