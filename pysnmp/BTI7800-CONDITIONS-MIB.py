# SNMP MIB module (BTI7800-CONDITIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI7800-CONDITIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:54 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bTI7800_CONDITIONS_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1)
)
bTI7800_CONDITIONS_MIB.setRevisions(
        ("2013-02-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class String(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class Severity(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("not-alarmed", 4),
          ("not-reported", 5))
    )



class ConditionCode(Integer32, TextualConvention):
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135)
        )
    )
    namedValues = NamedValues(
        *(("airfilterAbsense", 119),
          ("ais-l", 19),
          ("aisO", 53),
          ("apr", 65),
          ("apsData", 109),
          ("apsd", 50),
          ("bdi", 16),
          ("berTh-l", 87),
          ("berTh-s", 86),
          ("cfgFail", 38),
          ("cfgUnsupp", 37),
          ("chnDfc", 57),
          ("cnxMea", 59),
          ("cnxVldTmout", 60),
          ("contComE", 44),
          ("contComS", 43),
          ("defBfdDown", 107),
          ("defErrorCCM", 105),
          ("defMACStatus", 103),
          ("defRDICCM", 102),
          ("defRemoteCCM", 104),
          ("defXconCCM", 106),
          ("diskHighUsage", 116),
          ("envCurrentHighTh", 91),
          ("envCurrentLowTh", 92),
          ("envTempFail", 71),
          ("envTempHighTh", 69),
          ("envTempLowTh", 70),
          ("envVoltFail", 74),
          ("envVoltHighTh", 72),
          ("envVoltLowTh", 73),
          ("eqptBrownout", 135),
          ("eqptComm", 6),
          ("eqptDgrd", 5),
          ("eqptFail", 4),
          ("eqptLatchOpen", 77),
          ("eqptMism", 3),
          ("eqptMiss", 1),
          ("eqptUnkn", 2),
          ("fanSpeedLowTh", 79),
          ("feci", 42),
          ("feim", 41),
          ("firmUpgrdFail", 130),
          ("firmUpgrdInProg", 129),
          ("firmUpgrdReqd", 82),
          ("forced", 94),
          ("highBer", 25),
          ("iaocb", 49),
          ("iaocm", 48),
          ("iaocp", 47),
          ("invUnknown", 118),
          ("inventoryUnsupp", 134),
          ("isisAdjDown", 113),
          ("isisAdjRejected", 114),
          ("isisDbOvrld", 111),
          ("isisXDown", 112),
          ("laserFail", 36),
          ("laserTempHighTh", 34),
          ("laserTempLowTh", 35),
          ("lck", 23),
          ("lf", 26),
          ("lf-tx", 108),
          ("loSpecRx", 45),
          ("loSync", 11),
          ("lockout", 95),
          ("lof", 10),
          ("lola", 12),
          ("lolck", 133),
          ("lolightRx", 39),
          ("lolightTx", 40),
          ("lom", 13),
          ("los", 9),
          ("lpbk", 8),
          ("memHighUsage", 117),
          ("modTempHighTh", 66),
          ("modTempLowTh", 67),
          ("modTempShutdown", 68),
          ("ms-ais", 20),
          ("ms-berTh", 89),
          ("ms-rdi", 29),
          ("nonCoLocatedController", 80),
          ("obrHt", 64),
          ("obros", 56),
          ("ochAis", 98),
          ("ochOci", 101),
          ("ochRdi", 99),
          ("ochUeq", 100),
          ("oci", 24),
          ("odtgMism", 18),
          ("odu-ais", 22),
          ("oduBerTh", 84),
          ("omsAis", 110),
          ("omsBdi", 97),
          ("oneCableDisconnected", 90),
          ("oom", 132),
          ("oprHighFail", 63),
          ("oprHighTh", 30),
          ("oprLowTh", 31),
          ("optHighTh", 32),
          ("optLowTh", 33),
          ("otu-ais", 21),
          ("otuBerTh", 83),
          ("partitionFault", 131),
          ("pcsBerTh", 85),
          ("pmi", 51),
          ("posRx", 54),
          ("posRxHigh", 61),
          ("posRxLow", 62),
          ("posTx", 55),
          ("powerAbsent", 78),
          ("prbs", 93),
          ("preFecBerTh", 81),
          ("pyldMism", 17),
          ("rdi-l", 28),
          ("replUnitDegrade", 58),
          ("rf", 27),
          ("rs-berTh", 88),
          ("rsvpAdjDown", 115),
          ("scmNmiDown", 75),
          ("scmNoNmConn", 76),
          ("sd", 15),
          ("tLossRxHt", 46),
          ("tLossRxLt", 96),
          ("tim", 14),
          ("tx-aisl", 122),
          ("tx-msais", 120),
          ("tx-msrdi", 121),
          ("tx-oduAis", 125),
          ("tx-oduLck", 126),
          ("tx-oduOci", 127),
          ("tx-opucsf", 128),
          ("tx-rdil", 123),
          ("tx-rf", 124),
          ("uneqO", 52),
          ("upgr", 7))
    )



# MIB Managed Objects in the order of their OIDs

_ConditionsTable_Object = MibTable
conditionsTable = _ConditionsTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    conditionsTable.setStatus("current")
_ConditionsEntry_Object = MibTableRow
conditionsEntry = _ConditionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1)
)
conditionsEntry.setIndexNames(
    (0, "BTI7800-CONDITIONS-MIB", "conditionsEntityName"),
    (0, "BTI7800-CONDITIONS-MIB", "conditionsCode"),
)
if mibBuilder.loadTexts:
    conditionsEntry.setStatus("current")
_ConditionsEntityName_Type = String
_ConditionsEntityName_Object = MibTableColumn
conditionsEntityName = _ConditionsEntityName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 1),
    _ConditionsEntityName_Type()
)
conditionsEntityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    conditionsEntityName.setStatus("current")
_ConditionsCode_Type = ConditionCode
_ConditionsCode_Object = MibTableColumn
conditionsCode = _ConditionsCode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 2),
    _ConditionsCode_Type()
)
conditionsCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    conditionsCode.setStatus("current")


class _ConditionsReportType_Type(Integer32):
    """Custom type conditionsReportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmed", 2),
          ("non-alarmed", 1))
    )


_ConditionsReportType_Type.__name__ = "Integer32"
_ConditionsReportType_Object = MibTableColumn
conditionsReportType = _ConditionsReportType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 3),
    _ConditionsReportType_Type()
)
conditionsReportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionsReportType.setStatus("current")
_ConditionsTimeStamp_Type = DateAndTime
_ConditionsTimeStamp_Object = MibTableColumn
conditionsTimeStamp = _ConditionsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 4),
    _ConditionsTimeStamp_Type()
)
conditionsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionsTimeStamp.setStatus("current")
_ConditionsSeverity_Type = Severity
_ConditionsSeverity_Object = MibTableColumn
conditionsSeverity = _ConditionsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 5),
    _ConditionsSeverity_Type()
)
conditionsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionsSeverity.setStatus("current")
_ConditionsServiceAffecting_Type = TruthValue
_ConditionsServiceAffecting_Object = MibTableColumn
conditionsServiceAffecting = _ConditionsServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 6),
    _ConditionsServiceAffecting_Type()
)
conditionsServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionsServiceAffecting.setStatus("current")
_ConditionsDescription_Type = String
_ConditionsDescription_Object = MibTableColumn
conditionsDescription = _ConditionsDescription_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 7),
    _ConditionsDescription_Type()
)
conditionsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conditionsDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI7800-CONDITIONS-MIB",
    **{"ConfdString": ConfdString,
       "String": String,
       "Severity": Severity,
       "ConditionCode": ConditionCode,
       "bTI7800-CONDITIONS-MIB": bTI7800_CONDITIONS_MIB,
       "conditionsTable": conditionsTable,
       "conditionsEntry": conditionsEntry,
       "conditionsEntityName": conditionsEntityName,
       "conditionsCode": conditionsCode,
       "conditionsReportType": conditionsReportType,
       "conditionsTimeStamp": conditionsTimeStamp,
       "conditionsSeverity": conditionsSeverity,
       "conditionsServiceAffecting": conditionsServiceAffecting,
       "conditionsDescription": conditionsDescription}
)
