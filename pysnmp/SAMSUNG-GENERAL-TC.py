# SNMP MIB module (SAMSUNG-GENERAL-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-GENERAL-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:39 2024
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

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmGeneralTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50)
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



class ScmFixedLocaleDisplayString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ScmFixedLocaleUtf8String(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ScmNamedLocaleUtf8String(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ScmGenGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmGenLogFullPolicy(Integer32, TextualConvention):
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



class ScmGenMessageMapStringLabel(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class ScmGenNotifyDetailType(Integer32, TextualConvention):
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



class ScmGenNotifySchemeSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmGenNotifySeverityFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmGenNotifyTrainingFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmGenOptionValueSyntax(Integer32, TextualConvention):
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



class ScmGenReconfOptionState(Integer32, TextualConvention):
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



class ScmGenRowPersistence(Integer32, TextualConvention):
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



class ScmGenSNMPDomain(Integer32, TextualConvention):
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("snmpCLNSDomain", 2),
          ("snmpCONSDomain", 3),
          ("snmpDDPDomain", 4),
          ("snmpIPXDomain", 5),
          ("snmpNetBEUIDomain", 11),
          ("snmpNetBIOSDomain", 10),
          ("snmpTCPDomain", 20),
          ("snmpUDPDomain", 1),
          ("uriNotifyDomain", 30))
    )



class ScmGenSNMPVersion(Integer32, TextualConvention):
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



class ScmGenSNMPv2ErrorStatus(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("authorizationError", 16),
          ("badValue", 3),
          ("commitFailed", 14),
          ("genErr", 5),
          ("inconsistentName", 18),
          ("inconsistentValue", 12),
          ("noAccess", 6),
          ("noCreation", 11),
          ("noError", 0),
          ("noSuchName", 2),
          ("notWritable", 17),
          ("readOnly", 4),
          ("resourceUnavailable", 13),
          ("tooBig", 1),
          ("undoFailed", 15),
          ("wrongEncoding", 9),
          ("wrongLength", 8),
          ("wrongType", 7),
          ("wrongValue", 10))
    )



class ScmGlobalUniqueID(OctetString, TextualConvention):
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
_ScmGenZeroDotZero_ObjectIdentity = ObjectIdentity
scmGenZeroDotZero = _ScmGenZeroDotZero_ObjectIdentity(
    (0, 0, 0)
)
if mibBuilder.loadTexts:
    scmGenZeroDotZero.setStatus("current")
_SCmGeneralDummy_ObjectIdentity = ObjectIdentity
sCmGeneralDummy = _SCmGeneralDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999)
)
_SCmGenCardinal16_Type = Cardinal16
_SCmGenCardinal16_Object = MibScalar
sCmGenCardinal16 = _SCmGenCardinal16_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 1),
    _SCmGenCardinal16_Type()
)
sCmGenCardinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCardinal16.setStatus("current")
_SCmGenCardinal32_Type = Cardinal32
_SCmGenCardinal32_Object = MibScalar
sCmGenCardinal32 = _SCmGenCardinal32_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 2),
    _SCmGenCardinal32_Type()
)
sCmGenCardinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCardinal32.setStatus("current")
_SCmGenCardinal64High_Type = Cardinal64High
_SCmGenCardinal64High_Object = MibScalar
sCmGenCardinal64High = _SCmGenCardinal64High_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 3),
    _SCmGenCardinal64High_Type()
)
sCmGenCardinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCardinal64High.setStatus("current")
_SCmGenCardinal64Low_Type = Cardinal64Low
_SCmGenCardinal64Low_Object = MibScalar
sCmGenCardinal64Low = _SCmGenCardinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 4),
    _SCmGenCardinal64Low_Type()
)
sCmGenCardinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCardinal64Low.setStatus("current")
_SCmGenCodedCountry_Type = CodedCountry
_SCmGenCodedCountry_Object = MibScalar
sCmGenCodedCountry = _SCmGenCodedCountry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 5),
    _SCmGenCodedCountry_Type()
)
sCmGenCodedCountry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCodedCountry.setStatus("current")
_SCmGenCodedLanguage_Type = CodedLanguage
_SCmGenCodedLanguage_Object = MibScalar
sCmGenCodedLanguage = _SCmGenCodedLanguage_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 6),
    _SCmGenCodedLanguage_Type()
)
sCmGenCodedLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCodedLanguage.setStatus("current")
_SCmGenCodeIndexedStringIndex_Type = CodeIndexedStringIndex
_SCmGenCodeIndexedStringIndex_Object = MibScalar
sCmGenCodeIndexedStringIndex = _SCmGenCodeIndexedStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 7),
    _SCmGenCodeIndexedStringIndex_Type()
)
sCmGenCodeIndexedStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCodeIndexedStringIndex.setStatus("current")
_SCmGenCounter64High_Type = Counter64High
_SCmGenCounter64High_Object = MibScalar
sCmGenCounter64High = _SCmGenCounter64High_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 8),
    _SCmGenCounter64High_Type()
)
sCmGenCounter64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCounter64High.setStatus("current")
_SCmGenCounter64Low_Type = Counter64Low
_SCmGenCounter64Low_Object = MibScalar
sCmGenCounter64Low = _SCmGenCounter64Low_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 9),
    _SCmGenCounter64Low_Type()
)
sCmGenCounter64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenCounter64Low.setStatus("current")
_SCmGenGauge64High_Type = Gauge64High
_SCmGenGauge64High_Object = MibScalar
sCmGenGauge64High = _SCmGenGauge64High_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 10),
    _SCmGenGauge64High_Type()
)
sCmGenGauge64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenGauge64High.setStatus("current")
_SCmGenGauge64Low_Type = Gauge64Low
_SCmGenGauge64Low_Object = MibScalar
sCmGenGauge64Low = _SCmGenGauge64Low_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 11),
    _SCmGenGauge64Low_Type()
)
sCmGenGauge64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenGauge64Low.setStatus("current")
_SCmGenInteger64High_Type = Integer64High
_SCmGenInteger64High_Object = MibScalar
sCmGenInteger64High = _SCmGenInteger64High_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 12),
    _SCmGenInteger64High_Type()
)
sCmGenInteger64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenInteger64High.setStatus("current")
_SCmGenInteger64Low_Type = Integer64Low
_SCmGenInteger64Low_Object = MibScalar
sCmGenInteger64Low = _SCmGenInteger64Low_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 13),
    _SCmGenInteger64Low_Type()
)
sCmGenInteger64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenInteger64Low.setStatus("current")
_SCmGenOrdinal16_Type = Ordinal16
_SCmGenOrdinal16_Object = MibScalar
sCmGenOrdinal16 = _SCmGenOrdinal16_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 14),
    _SCmGenOrdinal16_Type()
)
sCmGenOrdinal16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenOrdinal16.setStatus("current")
_SCmGenOrdinal32_Type = Ordinal32
_SCmGenOrdinal32_Object = MibScalar
sCmGenOrdinal32 = _SCmGenOrdinal32_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 15),
    _SCmGenOrdinal32_Type()
)
sCmGenOrdinal32.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenOrdinal32.setStatus("current")
_SCmGenOrdinal64High_Type = Ordinal64High
_SCmGenOrdinal64High_Object = MibScalar
sCmGenOrdinal64High = _SCmGenOrdinal64High_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 16),
    _SCmGenOrdinal64High_Type()
)
sCmGenOrdinal64High.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenOrdinal64High.setStatus("current")
_SCmGenOrdinal64Low_Type = Ordinal64Low
_SCmGenOrdinal64Low_Object = MibScalar
sCmGenOrdinal64Low = _SCmGenOrdinal64Low_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 17),
    _SCmGenOrdinal64Low_Type()
)
sCmGenOrdinal64Low.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenOrdinal64Low.setStatus("current")
_SCmGenFixedLocaleDisplayString_Type = ScmFixedLocaleDisplayString
_SCmGenFixedLocaleDisplayString_Object = MibScalar
sCmGenFixedLocaleDisplayString = _SCmGenFixedLocaleDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 18),
    _SCmGenFixedLocaleDisplayString_Type()
)
sCmGenFixedLocaleDisplayString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenFixedLocaleDisplayString.setStatus("current")
_SCmGenGroupSupport_Type = ScmGenGroupSupport
_SCmGenGroupSupport_Object = MibScalar
sCmGenGroupSupport = _SCmGenGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 19),
    _SCmGenGroupSupport_Type()
)
sCmGenGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenGroupSupport.setStatus("current")
_SCmGenLogFullPolicy_Type = ScmGenLogFullPolicy
_SCmGenLogFullPolicy_Object = MibScalar
sCmGenLogFullPolicy = _SCmGenLogFullPolicy_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 20),
    _SCmGenLogFullPolicy_Type()
)
sCmGenLogFullPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenLogFullPolicy.setStatus("current")
_SCmGenOptionValueSyntax_Type = ScmGenOptionValueSyntax
_SCmGenOptionValueSyntax_Object = MibScalar
sCmGenOptionValueSyntax = _SCmGenOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 21),
    _SCmGenOptionValueSyntax_Type()
)
sCmGenOptionValueSyntax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenOptionValueSyntax.setStatus("current")
_SCmGenReconfOptionState_Type = ScmGenReconfOptionState
_SCmGenReconfOptionState_Object = MibScalar
sCmGenReconfOptionState = _SCmGenReconfOptionState_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 22),
    _SCmGenReconfOptionState_Type()
)
sCmGenReconfOptionState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenReconfOptionState.setStatus("current")
_SCmGenRowPersistence_Type = ScmGenRowPersistence
_SCmGenRowPersistence_Object = MibScalar
sCmGenRowPersistence = _SCmGenRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 23),
    _SCmGenRowPersistence_Type()
)
sCmGenRowPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenRowPersistence.setStatus("current")
_SCmGenSNMPDomain_Type = ScmGenSNMPDomain
_SCmGenSNMPDomain_Object = MibScalar
sCmGenSNMPDomain = _SCmGenSNMPDomain_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 24),
    _SCmGenSNMPDomain_Type()
)
sCmGenSNMPDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenSNMPDomain.setStatus("current")
_SCmGenSNMPVersion_Type = ScmGenSNMPVersion
_SCmGenSNMPVersion_Object = MibScalar
sCmGenSNMPVersion = _SCmGenSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 25),
    _SCmGenSNMPVersion_Type()
)
sCmGenSNMPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenSNMPVersion.setStatus("current")
_SCmGenSNMPv2ErrorStatus_Type = ScmGenSNMPv2ErrorStatus
_SCmGenSNMPv2ErrorStatus_Object = MibScalar
sCmGenSNMPv2ErrorStatus = _SCmGenSNMPv2ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 26),
    _SCmGenSNMPv2ErrorStatus_Type()
)
sCmGenSNMPv2ErrorStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenSNMPv2ErrorStatus.setStatus("current")
_SCmGenGlobalUniqueID_Type = ScmGlobalUniqueID
_SCmGenGlobalUniqueID_Object = MibScalar
sCmGenGlobalUniqueID = _SCmGenGlobalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 27),
    _SCmGenGlobalUniqueID_Type()
)
sCmGenGlobalUniqueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenGlobalUniqueID.setStatus("current")
_SCmGenFixedLocaleUtf8String_Type = ScmFixedLocaleUtf8String
_SCmGenFixedLocaleUtf8String_Object = MibScalar
sCmGenFixedLocaleUtf8String = _SCmGenFixedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 28),
    _SCmGenFixedLocaleUtf8String_Type()
)
sCmGenFixedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenFixedLocaleUtf8String.setStatus("current")
_SCmGenMessageMapStringLabel_Type = ScmGenMessageMapStringLabel
_SCmGenMessageMapStringLabel_Object = MibScalar
sCmGenMessageMapStringLabel = _SCmGenMessageMapStringLabel_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 29),
    _SCmGenMessageMapStringLabel_Type()
)
sCmGenMessageMapStringLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenMessageMapStringLabel.setStatus("current")
_SCmGenNamedLocaleUtf8String_Type = ScmNamedLocaleUtf8String
_SCmGenNamedLocaleUtf8String_Object = MibScalar
sCmGenNamedLocaleUtf8String = _SCmGenNamedLocaleUtf8String_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 30),
    _SCmGenNamedLocaleUtf8String_Type()
)
sCmGenNamedLocaleUtf8String.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenNamedLocaleUtf8String.setStatus("current")
_SCmGenNotifySchemeSupport_Type = ScmGenNotifySchemeSupport
_SCmGenNotifySchemeSupport_Object = MibScalar
sCmGenNotifySchemeSupport = _SCmGenNotifySchemeSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 31),
    _SCmGenNotifySchemeSupport_Type()
)
sCmGenNotifySchemeSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenNotifySchemeSupport.setStatus("current")
_SCmGenNotifySeverityFilter_Type = ScmGenNotifySeverityFilter
_SCmGenNotifySeverityFilter_Object = MibScalar
sCmGenNotifySeverityFilter = _SCmGenNotifySeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 32),
    _SCmGenNotifySeverityFilter_Type()
)
sCmGenNotifySeverityFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenNotifySeverityFilter.setStatus("current")
_SCmGenNotifyTrainingFilter_Type = ScmGenNotifyTrainingFilter
_SCmGenNotifyTrainingFilter_Object = MibScalar
sCmGenNotifyTrainingFilter = _SCmGenNotifyTrainingFilter_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 33),
    _SCmGenNotifyTrainingFilter_Type()
)
sCmGenNotifyTrainingFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenNotifyTrainingFilter.setStatus("current")
_SCmGenNotifyDetailType_Type = ScmGenNotifyDetailType
_SCmGenNotifyDetailType_Object = MibScalar
sCmGenNotifyDetailType = _SCmGenNotifyDetailType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 34),
    _SCmGenNotifyDetailType_Type()
)
sCmGenNotifyDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmGenNotifyDetailType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-GENERAL-TC",
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
       "ScmFixedLocaleDisplayString": ScmFixedLocaleDisplayString,
       "ScmFixedLocaleUtf8String": ScmFixedLocaleUtf8String,
       "ScmNamedLocaleUtf8String": ScmNamedLocaleUtf8String,
       "ScmGenGroupSupport": ScmGenGroupSupport,
       "ScmGenLogFullPolicy": ScmGenLogFullPolicy,
       "ScmGenMessageMapStringLabel": ScmGenMessageMapStringLabel,
       "ScmGenNotifyDetailType": ScmGenNotifyDetailType,
       "ScmGenNotifySchemeSupport": ScmGenNotifySchemeSupport,
       "ScmGenNotifySeverityFilter": ScmGenNotifySeverityFilter,
       "ScmGenNotifyTrainingFilter": ScmGenNotifyTrainingFilter,
       "ScmGenOptionValueSyntax": ScmGenOptionValueSyntax,
       "ScmGenReconfOptionState": ScmGenReconfOptionState,
       "ScmGenRowPersistence": ScmGenRowPersistence,
       "ScmGenSNMPDomain": ScmGenSNMPDomain,
       "ScmGenSNMPVersion": ScmGenSNMPVersion,
       "ScmGenSNMPv2ErrorStatus": ScmGenSNMPv2ErrorStatus,
       "ScmGlobalUniqueID": ScmGlobalUniqueID,
       "zeroDotZero": zeroDotZero,
       "scmGenZeroDotZero": scmGenZeroDotZero,
       "scmGeneralTC": scmGeneralTC,
       "sCmGeneralDummy": sCmGeneralDummy,
       "sCmGenCardinal16": sCmGenCardinal16,
       "sCmGenCardinal32": sCmGenCardinal32,
       "sCmGenCardinal64High": sCmGenCardinal64High,
       "sCmGenCardinal64Low": sCmGenCardinal64Low,
       "sCmGenCodedCountry": sCmGenCodedCountry,
       "sCmGenCodedLanguage": sCmGenCodedLanguage,
       "sCmGenCodeIndexedStringIndex": sCmGenCodeIndexedStringIndex,
       "sCmGenCounter64High": sCmGenCounter64High,
       "sCmGenCounter64Low": sCmGenCounter64Low,
       "sCmGenGauge64High": sCmGenGauge64High,
       "sCmGenGauge64Low": sCmGenGauge64Low,
       "sCmGenInteger64High": sCmGenInteger64High,
       "sCmGenInteger64Low": sCmGenInteger64Low,
       "sCmGenOrdinal16": sCmGenOrdinal16,
       "sCmGenOrdinal32": sCmGenOrdinal32,
       "sCmGenOrdinal64High": sCmGenOrdinal64High,
       "sCmGenOrdinal64Low": sCmGenOrdinal64Low,
       "sCmGenFixedLocaleDisplayString": sCmGenFixedLocaleDisplayString,
       "sCmGenGroupSupport": sCmGenGroupSupport,
       "sCmGenLogFullPolicy": sCmGenLogFullPolicy,
       "sCmGenOptionValueSyntax": sCmGenOptionValueSyntax,
       "sCmGenReconfOptionState": sCmGenReconfOptionState,
       "sCmGenRowPersistence": sCmGenRowPersistence,
       "sCmGenSNMPDomain": sCmGenSNMPDomain,
       "sCmGenSNMPVersion": sCmGenSNMPVersion,
       "sCmGenSNMPv2ErrorStatus": sCmGenSNMPv2ErrorStatus,
       "sCmGenGlobalUniqueID": sCmGenGlobalUniqueID,
       "sCmGenFixedLocaleUtf8String": sCmGenFixedLocaleUtf8String,
       "sCmGenMessageMapStringLabel": sCmGenMessageMapStringLabel,
       "sCmGenNamedLocaleUtf8String": sCmGenNamedLocaleUtf8String,
       "sCmGenNotifySchemeSupport": sCmGenNotifySchemeSupport,
       "sCmGenNotifySeverityFilter": sCmGenNotifySeverityFilter,
       "sCmGenNotifyTrainingFilter": sCmGenNotifyTrainingFilter,
       "sCmGenNotifyDetailType": sCmGenNotifyDetailType}
)
