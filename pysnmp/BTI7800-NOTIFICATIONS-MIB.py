# SNMP MIB module (BTI7800-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI7800-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:57 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bTI7800_NOTIFICATIONS_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2)
)
bTI7800_NOTIFICATIONS_MIB.setRevisions(
        ("2014-02-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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
              134)
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
          ("tx-opuCsf", 128),
          ("tx-rdil", 123),
          ("tx-rf", 124),
          ("uneqO", 52),
          ("upgr", 7))
    )



# MIB Managed Objects in the order of their OIDs

_NotificationObjects_ObjectIdentity = ObjectIdentity
notificationObjects = _NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1)
)
_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1)
)
_EntityName_Type = String
_EntityName_Object = MibScalar
entityName = _EntityName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 1),
    _EntityName_Type()
)
entityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityName.setStatus("current")
_Code_Type = ConditionCode
_Code_Object = MibScalar
code = _Code_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 2),
    _Code_Type()
)
code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    code.setStatus("current")


class _ReportType_Type(Integer32):
    """Custom type reportType based on Integer32"""
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


_ReportType_Type.__name__ = "Integer32"
_ReportType_Object = MibScalar
reportType = _ReportType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 3),
    _ReportType_Type()
)
reportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reportType.setStatus("current")
_TimeStamp_Type = DateAndTime
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 4),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_Severity_Type = Severity
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 5),
    _Severity_Type()
)
severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_ServiceAffecting_Type = TruthValue
_ServiceAffecting_Object = MibScalar
serviceAffecting = _ServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 6),
    _ServiceAffecting_Type()
)
serviceAffecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceAffecting.setStatus("current")
_Description_Type = String
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 1, 7),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1)
)

# Managed Objects groups


# Notification objects

eqptMissRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 1)
)
eqptMissRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptMissRaise.setStatus(
        "current"
    )

eqptMissClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 2)
)
eqptMissClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptMissClear.setStatus(
        "current"
    )

eqptUnknRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 3)
)
eqptUnknRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptUnknRaise.setStatus(
        "current"
    )

eqptUnknClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 4)
)
eqptUnknClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptUnknClear.setStatus(
        "current"
    )

eqptMismRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 5)
)
eqptMismRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptMismRaise.setStatus(
        "current"
    )

eqptMismClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 6)
)
eqptMismClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptMismClear.setStatus(
        "current"
    )

eqptFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 7)
)
eqptFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptFailRaise.setStatus(
        "current"
    )

eqptFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 8)
)
eqptFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptFailClear.setStatus(
        "current"
    )

eqptDgrdRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 9)
)
eqptDgrdRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptDgrdRaise.setStatus(
        "current"
    )

eqptDgrdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 10)
)
eqptDgrdClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptDgrdClear.setStatus(
        "current"
    )

eqptCommRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 11)
)
eqptCommRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptCommRaise.setStatus(
        "current"
    )

eqptCommClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 12)
)
eqptCommClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptCommClear.setStatus(
        "current"
    )

upgrRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 13)
)
upgrRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    upgrRaise.setStatus(
        "current"
    )

upgrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 14)
)
upgrClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    upgrClear.setStatus(
        "current"
    )

lpbkRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 15)
)
lpbkRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lpbkRaise.setStatus(
        "current"
    )

lpbkClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 16)
)
lpbkClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lpbkClear.setStatus(
        "current"
    )

losRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 17)
)
losRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    losRaise.setStatus(
        "current"
    )

losClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 18)
)
losClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    losClear.setStatus(
        "current"
    )

lofRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 19)
)
lofRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lofRaise.setStatus(
        "current"
    )

lofClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 20)
)
lofClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lofClear.setStatus(
        "current"
    )

loSyncRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 21)
)
loSyncRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    loSyncRaise.setStatus(
        "current"
    )

loSyncClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 22)
)
loSyncClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    loSyncClear.setStatus(
        "current"
    )

lolaRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 23)
)
lolaRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolaRaise.setStatus(
        "current"
    )

lolaClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 24)
)
lolaClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolaClear.setStatus(
        "current"
    )

lomRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 25)
)
lomRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lomRaise.setStatus(
        "current"
    )

lomClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 26)
)
lomClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lomClear.setStatus(
        "current"
    )

timRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 27)
)
timRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    timRaise.setStatus(
        "current"
    )

timClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 28)
)
timClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    timClear.setStatus(
        "current"
    )

sdRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 29)
)
sdRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    sdRaise.setStatus(
        "current"
    )

sdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 30)
)
sdClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    sdClear.setStatus(
        "current"
    )

bdiRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 31)
)
bdiRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    bdiRaise.setStatus(
        "current"
    )

bdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 32)
)
bdiClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    bdiClear.setStatus(
        "current"
    )

pyldMismRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 33)
)
pyldMismRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pyldMismRaise.setStatus(
        "current"
    )

pyldMismClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 34)
)
pyldMismClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pyldMismClear.setStatus(
        "current"
    )

odtgMismRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 35)
)
odtgMismRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    odtgMismRaise.setStatus(
        "current"
    )

odtgMismClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 36)
)
odtgMismClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    odtgMismClear.setStatus(
        "current"
    )

ais_lRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 37)
)
ais_lRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ais_lRaise.setStatus(
        "current"
    )

ais_lClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 38)
)
ais_lClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ais_lClear.setStatus(
        "current"
    )

ms_aisRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 39)
)
ms_aisRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_aisRaise.setStatus(
        "current"
    )

ms_aisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 40)
)
ms_aisClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_aisClear.setStatus(
        "current"
    )

otu_aisRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 41)
)
otu_aisRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    otu_aisRaise.setStatus(
        "current"
    )

otu_aisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 42)
)
otu_aisClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    otu_aisClear.setStatus(
        "current"
    )

odu_aisRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 43)
)
odu_aisRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    odu_aisRaise.setStatus(
        "current"
    )

odu_aisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 44)
)
odu_aisClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    odu_aisClear.setStatus(
        "current"
    )

lckRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 45)
)
lckRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lckRaise.setStatus(
        "current"
    )

lckClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 46)
)
lckClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lckClear.setStatus(
        "current"
    )

ociRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 47)
)
ociRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ociRaise.setStatus(
        "current"
    )

ociClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 48)
)
ociClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ociClear.setStatus(
        "current"
    )

highBerRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 49)
)
highBerRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    highBerRaise.setStatus(
        "current"
    )

highBerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 50)
)
highBerClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    highBerClear.setStatus(
        "current"
    )

lfRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 51)
)
lfRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lfRaise.setStatus(
        "current"
    )

lfClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 52)
)
lfClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lfClear.setStatus(
        "current"
    )

rfRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 53)
)
rfRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rfRaise.setStatus(
        "current"
    )

rfClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 54)
)
rfClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rfClear.setStatus(
        "current"
    )

rdi_lRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 55)
)
rdi_lRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rdi_lRaise.setStatus(
        "current"
    )

rdi_lClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 56)
)
rdi_lClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rdi_lClear.setStatus(
        "current"
    )

ms_rdiRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 57)
)
ms_rdiRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_rdiRaise.setStatus(
        "current"
    )

ms_rdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 58)
)
ms_rdiClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_rdiClear.setStatus(
        "current"
    )

oprHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 59)
)
oprHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprHighThRaise.setStatus(
        "current"
    )

oprHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 60)
)
oprHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprHighThClear.setStatus(
        "current"
    )

oprLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 61)
)
oprLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprLowThRaise.setStatus(
        "current"
    )

oprLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 62)
)
oprLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprLowThClear.setStatus(
        "current"
    )

optHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 63)
)
optHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    optHighThRaise.setStatus(
        "current"
    )

optHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 64)
)
optHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    optHighThClear.setStatus(
        "current"
    )

optLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 65)
)
optLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    optLowThRaise.setStatus(
        "current"
    )

optLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 66)
)
optLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    optLowThClear.setStatus(
        "current"
    )

laserTempHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 67)
)
laserTempHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserTempHighThRaise.setStatus(
        "current"
    )

laserTempHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 68)
)
laserTempHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserTempHighThClear.setStatus(
        "current"
    )

laserTempLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 69)
)
laserTempLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserTempLowThRaise.setStatus(
        "current"
    )

laserTempLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 70)
)
laserTempLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserTempLowThClear.setStatus(
        "current"
    )

laserFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 71)
)
laserFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserFailRaise.setStatus(
        "current"
    )

laserFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 72)
)
laserFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    laserFailClear.setStatus(
        "current"
    )

cfgUnsuppRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 73)
)
cfgUnsuppRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cfgUnsuppRaise.setStatus(
        "current"
    )

cfgUnsuppClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 74)
)
cfgUnsuppClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cfgUnsuppClear.setStatus(
        "current"
    )

cfgFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 75)
)
cfgFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cfgFailRaise.setStatus(
        "current"
    )

cfgFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 76)
)
cfgFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cfgFailClear.setStatus(
        "current"
    )

lolightRxRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 77)
)
lolightRxRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolightRxRaise.setStatus(
        "current"
    )

lolightRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 78)
)
lolightRxClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolightRxClear.setStatus(
        "current"
    )

lolightTxRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 79)
)
lolightTxRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolightTxRaise.setStatus(
        "current"
    )

lolightTxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 80)
)
lolightTxClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolightTxClear.setStatus(
        "current"
    )

feimRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 81)
)
feimRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    feimRaise.setStatus(
        "current"
    )

feimClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 82)
)
feimClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    feimClear.setStatus(
        "current"
    )

feciRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 83)
)
feciRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    feciRaise.setStatus(
        "current"
    )

feciClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 84)
)
feciClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    feciClear.setStatus(
        "current"
    )

contComSRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 85)
)
contComSRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    contComSRaise.setStatus(
        "current"
    )

contComSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 86)
)
contComSClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    contComSClear.setStatus(
        "current"
    )

contComERaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 87)
)
contComERaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    contComERaise.setStatus(
        "current"
    )

contComEClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 88)
)
contComEClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    contComEClear.setStatus(
        "current"
    )

loSpecRxRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 89)
)
loSpecRxRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    loSpecRxRaise.setStatus(
        "current"
    )

loSpecRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 90)
)
loSpecRxClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    loSpecRxClear.setStatus(
        "current"
    )

tLossRxHtRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 91)
)
tLossRxHtRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    tLossRxHtRaise.setStatus(
        "current"
    )

tLossRxHtClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 92)
)
tLossRxHtClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    tLossRxHtClear.setStatus(
        "current"
    )

iaocpRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 93)
)
iaocpRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocpRaise.setStatus(
        "current"
    )

iaocpClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 94)
)
iaocpClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocpClear.setStatus(
        "current"
    )

iaocmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 95)
)
iaocmRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocmRaise.setStatus(
        "current"
    )

iaocmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 96)
)
iaocmClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocmClear.setStatus(
        "current"
    )

iaocbRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 97)
)
iaocbRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocbRaise.setStatus(
        "current"
    )

iaocbClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 98)
)
iaocbClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    iaocbClear.setStatus(
        "current"
    )

apsdRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 99)
)
apsdRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    apsdRaise.setStatus(
        "current"
    )

apsdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 100)
)
apsdClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    apsdClear.setStatus(
        "current"
    )

pmiRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 101)
)
pmiRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pmiRaise.setStatus(
        "current"
    )

pmiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 102)
)
pmiClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pmiClear.setStatus(
        "current"
    )

uneqORaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 103)
)
uneqORaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    uneqORaise.setStatus(
        "current"
    )

uneqOClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 104)
)
uneqOClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    uneqOClear.setStatus(
        "current"
    )

aisORaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 105)
)
aisORaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    aisORaise.setStatus(
        "current"
    )

aisOClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 106)
)
aisOClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    aisOClear.setStatus(
        "current"
    )

posRxRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 107)
)
posRxRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxRaise.setStatus(
        "current"
    )

posRxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 108)
)
posRxClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxClear.setStatus(
        "current"
    )

posTxRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 109)
)
posTxRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posTxRaise.setStatus(
        "current"
    )

posTxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 110)
)
posTxClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posTxClear.setStatus(
        "current"
    )

obrosRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 111)
)
obrosRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    obrosRaise.setStatus(
        "current"
    )

obrosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 112)
)
obrosClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    obrosClear.setStatus(
        "current"
    )

chnDfcRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 113)
)
chnDfcRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    chnDfcRaise.setStatus(
        "current"
    )

chnDfcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 114)
)
chnDfcClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    chnDfcClear.setStatus(
        "current"
    )

replUnitDegradeRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 115)
)
replUnitDegradeRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    replUnitDegradeRaise.setStatus(
        "current"
    )

replUnitDegradeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 116)
)
replUnitDegradeClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    replUnitDegradeClear.setStatus(
        "current"
    )

cnxMeaRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 117)
)
cnxMeaRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cnxMeaRaise.setStatus(
        "current"
    )

cnxMeaClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 118)
)
cnxMeaClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cnxMeaClear.setStatus(
        "current"
    )

cnxVldTmoutRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 119)
)
cnxVldTmoutRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cnxVldTmoutRaise.setStatus(
        "current"
    )

cnxVldTmoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 120)
)
cnxVldTmoutClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    cnxVldTmoutClear.setStatus(
        "current"
    )

posRxHighRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 121)
)
posRxHighRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxHighRaise.setStatus(
        "current"
    )

posRxHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 122)
)
posRxHighClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxHighClear.setStatus(
        "current"
    )

posRxLowRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 123)
)
posRxLowRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxLowRaise.setStatus(
        "current"
    )

posRxLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 124)
)
posRxLowClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    posRxLowClear.setStatus(
        "current"
    )

oprHighFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 125)
)
oprHighFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprHighFailRaise.setStatus(
        "current"
    )

oprHighFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 126)
)
oprHighFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oprHighFailClear.setStatus(
        "current"
    )

obrHtRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 127)
)
obrHtRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    obrHtRaise.setStatus(
        "current"
    )

obrHtClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 128)
)
obrHtClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    obrHtClear.setStatus(
        "current"
    )

aprRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 129)
)
aprRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    aprRaise.setStatus(
        "current"
    )

aprClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 130)
)
aprClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    aprClear.setStatus(
        "current"
    )

modTempHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 131)
)
modTempHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempHighThRaise.setStatus(
        "current"
    )

modTempHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 132)
)
modTempHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempHighThClear.setStatus(
        "current"
    )

modTempLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 133)
)
modTempLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempLowThRaise.setStatus(
        "current"
    )

modTempLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 134)
)
modTempLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempLowThClear.setStatus(
        "current"
    )

modTempShutdownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 135)
)
modTempShutdownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempShutdownRaise.setStatus(
        "current"
    )

modTempShutdownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 136)
)
modTempShutdownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    modTempShutdownClear.setStatus(
        "current"
    )

envTempHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 137)
)
envTempHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempHighThRaise.setStatus(
        "current"
    )

envTempHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 138)
)
envTempHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempHighThClear.setStatus(
        "current"
    )

envTempLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 139)
)
envTempLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempLowThRaise.setStatus(
        "current"
    )

envTempLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 140)
)
envTempLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempLowThClear.setStatus(
        "current"
    )

envTempFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 141)
)
envTempFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempFailRaise.setStatus(
        "current"
    )

envTempFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 142)
)
envTempFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envTempFailClear.setStatus(
        "current"
    )

envVoltHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 143)
)
envVoltHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltHighThRaise.setStatus(
        "current"
    )

envVoltHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 144)
)
envVoltHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltHighThClear.setStatus(
        "current"
    )

envVoltLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 145)
)
envVoltLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltLowThRaise.setStatus(
        "current"
    )

envVoltLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 146)
)
envVoltLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltLowThClear.setStatus(
        "current"
    )

envVoltFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 147)
)
envVoltFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltFailRaise.setStatus(
        "current"
    )

envVoltFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 148)
)
envVoltFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envVoltFailClear.setStatus(
        "current"
    )

scmNmiDownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 149)
)
scmNmiDownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    scmNmiDownRaise.setStatus(
        "current"
    )

scmNmiDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 150)
)
scmNmiDownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    scmNmiDownClear.setStatus(
        "current"
    )

scmNoNmConnRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 151)
)
scmNoNmConnRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    scmNoNmConnRaise.setStatus(
        "current"
    )

scmNoNmConnClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 152)
)
scmNoNmConnClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    scmNoNmConnClear.setStatus(
        "current"
    )

eqptLatchOpenRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 153)
)
eqptLatchOpenRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptLatchOpenRaise.setStatus(
        "current"
    )

eqptLatchOpenClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 154)
)
eqptLatchOpenClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    eqptLatchOpenClear.setStatus(
        "current"
    )

powerAbsentRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 155)
)
powerAbsentRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    powerAbsentRaise.setStatus(
        "current"
    )

powerAbsentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 156)
)
powerAbsentClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    powerAbsentClear.setStatus(
        "current"
    )

fanSpeedLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 157)
)
fanSpeedLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    fanSpeedLowThRaise.setStatus(
        "current"
    )

fanSpeedLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 158)
)
fanSpeedLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    fanSpeedLowThClear.setStatus(
        "current"
    )

nonCoLocatedControllerRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 159)
)
nonCoLocatedControllerRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    nonCoLocatedControllerRaise.setStatus(
        "current"
    )

nonCoLocatedControllerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 160)
)
nonCoLocatedControllerClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    nonCoLocatedControllerClear.setStatus(
        "current"
    )

preFecBerThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 161)
)
preFecBerThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    preFecBerThRaise.setStatus(
        "current"
    )

preFecBerThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 162)
)
preFecBerThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    preFecBerThClear.setStatus(
        "current"
    )

firmUpgrdReqdRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 163)
)
firmUpgrdReqdRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    firmUpgrdReqdRaise.setStatus(
        "current"
    )

firmUpgrdReqdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 164)
)
firmUpgrdReqdClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    firmUpgrdReqdClear.setStatus(
        "current"
    )

otuBerThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 165)
)
otuBerThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    otuBerThRaise.setStatus(
        "current"
    )

otuBerThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 166)
)
otuBerThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    otuBerThClear.setStatus(
        "current"
    )

oduBerThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 167)
)
oduBerThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oduBerThRaise.setStatus(
        "current"
    )

oduBerThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 168)
)
oduBerThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oduBerThClear.setStatus(
        "current"
    )

pcsBerThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 169)
)
pcsBerThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pcsBerThRaise.setStatus(
        "current"
    )

pcsBerThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 170)
)
pcsBerThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    pcsBerThClear.setStatus(
        "current"
    )

berTh_sRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 171)
)
berTh_sRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    berTh_sRaise.setStatus(
        "current"
    )

berTh_sClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 172)
)
berTh_sClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    berTh_sClear.setStatus(
        "current"
    )

berTh_lRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 173)
)
berTh_lRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    berTh_lRaise.setStatus(
        "current"
    )

berTh_lClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 174)
)
berTh_lClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    berTh_lClear.setStatus(
        "current"
    )

rs_berThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 175)
)
rs_berThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rs_berThRaise.setStatus(
        "current"
    )

rs_berThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 176)
)
rs_berThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rs_berThClear.setStatus(
        "current"
    )

ms_berThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 177)
)
ms_berThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_berThRaise.setStatus(
        "current"
    )

ms_berThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 178)
)
ms_berThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    ms_berThClear.setStatus(
        "current"
    )

oneCableDisconnectedRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 179)
)
oneCableDisconnectedRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oneCableDisconnectedRaise.setStatus(
        "current"
    )

oneCableDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 180)
)
oneCableDisconnectedClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    oneCableDisconnectedClear.setStatus(
        "current"
    )

envCurrentHighThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 181)
)
envCurrentHighThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envCurrentHighThRaise.setStatus(
        "current"
    )

envCurrentHighThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 182)
)
envCurrentHighThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envCurrentHighThClear.setStatus(
        "current"
    )

envCurrentLowThRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 183)
)
envCurrentLowThRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envCurrentLowThRaise.setStatus(
        "current"
    )

envCurrentLowThClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 184)
)
envCurrentLowThClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    envCurrentLowThClear.setStatus(
        "current"
    )

prbsRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 185)
)
prbsRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    prbsRaise.setStatus(
        "current"
    )

prbsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 186)
)
prbsClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    prbsClear.setStatus(
        "current"
    )

forcedRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 187)
)
forcedRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    forcedRaise.setStatus(
        "current"
    )

forcedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 188)
)
forcedClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    forcedClear.setStatus(
        "current"
    )

defRDICCMRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 189)
)
defRDICCMRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defRDICCMRaise.setStatus(
        "current"
    )

defRDICCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 190)
)
defRDICCMClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defRDICCMClear.setStatus(
        "current"
    )

defMACStatusRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 191)
)
defMACStatusRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defMACStatusRaise.setStatus(
        "current"
    )

defMACStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 192)
)
defMACStatusClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defMACStatusClear.setStatus(
        "current"
    )

defRemoteCCMRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 193)
)
defRemoteCCMRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defRemoteCCMRaise.setStatus(
        "current"
    )

defRemoteCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 194)
)
defRemoteCCMClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defRemoteCCMClear.setStatus(
        "current"
    )

defErrorCCMRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 195)
)
defErrorCCMRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defErrorCCMRaise.setStatus(
        "current"
    )

defErrorCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 196)
)
defErrorCCMClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defErrorCCMClear.setStatus(
        "current"
    )

defXconCCMRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 197)
)
defXconCCMRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defXconCCMRaise.setStatus(
        "current"
    )

defXconCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 198)
)
defXconCCMClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defXconCCMClear.setStatus(
        "current"
    )

defBfdDownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 199)
)
defBfdDownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defBfdDownRaise.setStatus(
        "current"
    )

defBfdDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 200)
)
defBfdDownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    defBfdDownClear.setStatus(
        "current"
    )

isisDbOvrldRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 201)
)
isisDbOvrldRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisDbOvrldRaise.setStatus(
        "current"
    )

isisDbOvrldClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 202)
)
isisDbOvrldClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisDbOvrldClear.setStatus(
        "current"
    )

isisXDownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 203)
)
isisXDownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisXDownRaise.setStatus(
        "current"
    )

isisXDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 204)
)
isisXDownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisXDownClear.setStatus(
        "current"
    )

isisAdjDownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 205)
)
isisAdjDownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisAdjDownRaise.setStatus(
        "current"
    )

isisAdjDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 206)
)
isisAdjDownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisAdjDownClear.setStatus(
        "current"
    )

isisAdjRejectedRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 207)
)
isisAdjRejectedRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisAdjRejectedRaise.setStatus(
        "current"
    )

isisAdjRejectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 208)
)
isisAdjRejectedClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    isisAdjRejectedClear.setStatus(
        "current"
    )

rsvpAdjDownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 209)
)
rsvpAdjDownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rsvpAdjDownRaise.setStatus(
        "current"
    )

rsvpAdjDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 210)
)
rsvpAdjDownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    rsvpAdjDownClear.setStatus(
        "current"
    )

diskHighUsageRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 211)
)
diskHighUsageRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    diskHighUsageRaise.setStatus(
        "current"
    )

diskHighUsageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 212)
)
diskHighUsageClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    diskHighUsageClear.setStatus(
        "current"
    )

memHighUsageRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 213)
)
memHighUsageRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    memHighUsageRaise.setStatus(
        "current"
    )

memHighUsageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 214)
)
memHighUsageClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    memHighUsageClear.setStatus(
        "current"
    )

lockoutRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 215)
)
lockoutRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lockoutRaise.setStatus(
        "current"
    )

lockoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 216)
)
lockoutClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lockoutClear.setStatus(
        "current"
    )

invUnknownRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 217)
)
invUnknownRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    invUnknownRaise.setStatus(
        "current"
    )

invUnknownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 218)
)
invUnknownClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    invUnknownClear.setStatus(
        "current"
    )

airfilterAbsenseRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 219)
)
airfilterAbsenseRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    airfilterAbsenseRaise.setStatus(
        "current"
    )

airfilterAbsenseClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 220)
)
airfilterAbsenseClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    airfilterAbsenseClear.setStatus(
        "current"
    )

firmUpgrdFailRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 221)
)
firmUpgrdFailRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    firmUpgrdFailRaise.setStatus(
        "current"
    )

firmUpgrdFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 222)
)
firmUpgrdFailClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    firmUpgrdFailClear.setStatus(
        "current"
    )

partitionFaultRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 223)
)
partitionFaultRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    partitionFaultRaise.setStatus(
        "current"
    )

partitionFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 224)
)
partitionFaultClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    partitionFaultClear.setStatus(
        "current"
    )

lolckRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 225)
)
lolckRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolckRaise.setStatus(
        "current"
    )

lolckClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 226)
)
lolckClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    lolckClear.setStatus(
        "current"
    )

inventoryUnsuppRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 227)
)
inventoryUnsuppRaise.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    inventoryUnsuppRaise.setStatus(
        "current"
    )

inventoryUnsuppClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 2, 1, 2, 1, 228)
)
inventoryUnsuppClear.setObjects(
      *(("BTI7800-NOTIFICATIONS-MIB", "entityName"),
        ("BTI7800-NOTIFICATIONS-MIB", "code"),
        ("BTI7800-NOTIFICATIONS-MIB", "reportType"),
        ("BTI7800-NOTIFICATIONS-MIB", "timeStamp"),
        ("BTI7800-NOTIFICATIONS-MIB", "severity"),
        ("BTI7800-NOTIFICATIONS-MIB", "serviceAffecting"),
        ("BTI7800-NOTIFICATIONS-MIB", "description"))
)
if mibBuilder.loadTexts:
    inventoryUnsuppClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI7800-NOTIFICATIONS-MIB",
    **{"String": String,
       "Severity": Severity,
       "ConditionCode": ConditionCode,
       "bTI7800-NOTIFICATIONS-MIB": bTI7800_NOTIFICATIONS_MIB,
       "notificationObjects": notificationObjects,
       "variables": variables,
       "entityName": entityName,
       "code": code,
       "reportType": reportType,
       "timeStamp": timeStamp,
       "severity": severity,
       "serviceAffecting": serviceAffecting,
       "description": description,
       "notifications": notifications,
       "traps": traps,
       "eqptMissRaise": eqptMissRaise,
       "eqptMissClear": eqptMissClear,
       "eqptUnknRaise": eqptUnknRaise,
       "eqptUnknClear": eqptUnknClear,
       "eqptMismRaise": eqptMismRaise,
       "eqptMismClear": eqptMismClear,
       "eqptFailRaise": eqptFailRaise,
       "eqptFailClear": eqptFailClear,
       "eqptDgrdRaise": eqptDgrdRaise,
       "eqptDgrdClear": eqptDgrdClear,
       "eqptCommRaise": eqptCommRaise,
       "eqptCommClear": eqptCommClear,
       "upgrRaise": upgrRaise,
       "upgrClear": upgrClear,
       "lpbkRaise": lpbkRaise,
       "lpbkClear": lpbkClear,
       "losRaise": losRaise,
       "losClear": losClear,
       "lofRaise": lofRaise,
       "lofClear": lofClear,
       "loSyncRaise": loSyncRaise,
       "loSyncClear": loSyncClear,
       "lolaRaise": lolaRaise,
       "lolaClear": lolaClear,
       "lomRaise": lomRaise,
       "lomClear": lomClear,
       "timRaise": timRaise,
       "timClear": timClear,
       "sdRaise": sdRaise,
       "sdClear": sdClear,
       "bdiRaise": bdiRaise,
       "bdiClear": bdiClear,
       "pyldMismRaise": pyldMismRaise,
       "pyldMismClear": pyldMismClear,
       "odtgMismRaise": odtgMismRaise,
       "odtgMismClear": odtgMismClear,
       "ais-lRaise": ais_lRaise,
       "ais-lClear": ais_lClear,
       "ms-aisRaise": ms_aisRaise,
       "ms-aisClear": ms_aisClear,
       "otu-aisRaise": otu_aisRaise,
       "otu-aisClear": otu_aisClear,
       "odu-aisRaise": odu_aisRaise,
       "odu-aisClear": odu_aisClear,
       "lckRaise": lckRaise,
       "lckClear": lckClear,
       "ociRaise": ociRaise,
       "ociClear": ociClear,
       "highBerRaise": highBerRaise,
       "highBerClear": highBerClear,
       "lfRaise": lfRaise,
       "lfClear": lfClear,
       "rfRaise": rfRaise,
       "rfClear": rfClear,
       "rdi-lRaise": rdi_lRaise,
       "rdi-lClear": rdi_lClear,
       "ms-rdiRaise": ms_rdiRaise,
       "ms-rdiClear": ms_rdiClear,
       "oprHighThRaise": oprHighThRaise,
       "oprHighThClear": oprHighThClear,
       "oprLowThRaise": oprLowThRaise,
       "oprLowThClear": oprLowThClear,
       "optHighThRaise": optHighThRaise,
       "optHighThClear": optHighThClear,
       "optLowThRaise": optLowThRaise,
       "optLowThClear": optLowThClear,
       "laserTempHighThRaise": laserTempHighThRaise,
       "laserTempHighThClear": laserTempHighThClear,
       "laserTempLowThRaise": laserTempLowThRaise,
       "laserTempLowThClear": laserTempLowThClear,
       "laserFailRaise": laserFailRaise,
       "laserFailClear": laserFailClear,
       "cfgUnsuppRaise": cfgUnsuppRaise,
       "cfgUnsuppClear": cfgUnsuppClear,
       "cfgFailRaise": cfgFailRaise,
       "cfgFailClear": cfgFailClear,
       "lolightRxRaise": lolightRxRaise,
       "lolightRxClear": lolightRxClear,
       "lolightTxRaise": lolightTxRaise,
       "lolightTxClear": lolightTxClear,
       "feimRaise": feimRaise,
       "feimClear": feimClear,
       "feciRaise": feciRaise,
       "feciClear": feciClear,
       "contComSRaise": contComSRaise,
       "contComSClear": contComSClear,
       "contComERaise": contComERaise,
       "contComEClear": contComEClear,
       "loSpecRxRaise": loSpecRxRaise,
       "loSpecRxClear": loSpecRxClear,
       "tLossRxHtRaise": tLossRxHtRaise,
       "tLossRxHtClear": tLossRxHtClear,
       "iaocpRaise": iaocpRaise,
       "iaocpClear": iaocpClear,
       "iaocmRaise": iaocmRaise,
       "iaocmClear": iaocmClear,
       "iaocbRaise": iaocbRaise,
       "iaocbClear": iaocbClear,
       "apsdRaise": apsdRaise,
       "apsdClear": apsdClear,
       "pmiRaise": pmiRaise,
       "pmiClear": pmiClear,
       "uneqORaise": uneqORaise,
       "uneqOClear": uneqOClear,
       "aisORaise": aisORaise,
       "aisOClear": aisOClear,
       "posRxRaise": posRxRaise,
       "posRxClear": posRxClear,
       "posTxRaise": posTxRaise,
       "posTxClear": posTxClear,
       "obrosRaise": obrosRaise,
       "obrosClear": obrosClear,
       "chnDfcRaise": chnDfcRaise,
       "chnDfcClear": chnDfcClear,
       "replUnitDegradeRaise": replUnitDegradeRaise,
       "replUnitDegradeClear": replUnitDegradeClear,
       "cnxMeaRaise": cnxMeaRaise,
       "cnxMeaClear": cnxMeaClear,
       "cnxVldTmoutRaise": cnxVldTmoutRaise,
       "cnxVldTmoutClear": cnxVldTmoutClear,
       "posRxHighRaise": posRxHighRaise,
       "posRxHighClear": posRxHighClear,
       "posRxLowRaise": posRxLowRaise,
       "posRxLowClear": posRxLowClear,
       "oprHighFailRaise": oprHighFailRaise,
       "oprHighFailClear": oprHighFailClear,
       "obrHtRaise": obrHtRaise,
       "obrHtClear": obrHtClear,
       "aprRaise": aprRaise,
       "aprClear": aprClear,
       "modTempHighThRaise": modTempHighThRaise,
       "modTempHighThClear": modTempHighThClear,
       "modTempLowThRaise": modTempLowThRaise,
       "modTempLowThClear": modTempLowThClear,
       "modTempShutdownRaise": modTempShutdownRaise,
       "modTempShutdownClear": modTempShutdownClear,
       "envTempHighThRaise": envTempHighThRaise,
       "envTempHighThClear": envTempHighThClear,
       "envTempLowThRaise": envTempLowThRaise,
       "envTempLowThClear": envTempLowThClear,
       "envTempFailRaise": envTempFailRaise,
       "envTempFailClear": envTempFailClear,
       "envVoltHighThRaise": envVoltHighThRaise,
       "envVoltHighThClear": envVoltHighThClear,
       "envVoltLowThRaise": envVoltLowThRaise,
       "envVoltLowThClear": envVoltLowThClear,
       "envVoltFailRaise": envVoltFailRaise,
       "envVoltFailClear": envVoltFailClear,
       "scmNmiDownRaise": scmNmiDownRaise,
       "scmNmiDownClear": scmNmiDownClear,
       "scmNoNmConnRaise": scmNoNmConnRaise,
       "scmNoNmConnClear": scmNoNmConnClear,
       "eqptLatchOpenRaise": eqptLatchOpenRaise,
       "eqptLatchOpenClear": eqptLatchOpenClear,
       "powerAbsentRaise": powerAbsentRaise,
       "powerAbsentClear": powerAbsentClear,
       "fanSpeedLowThRaise": fanSpeedLowThRaise,
       "fanSpeedLowThClear": fanSpeedLowThClear,
       "nonCoLocatedControllerRaise": nonCoLocatedControllerRaise,
       "nonCoLocatedControllerClear": nonCoLocatedControllerClear,
       "preFecBerThRaise": preFecBerThRaise,
       "preFecBerThClear": preFecBerThClear,
       "firmUpgrdReqdRaise": firmUpgrdReqdRaise,
       "firmUpgrdReqdClear": firmUpgrdReqdClear,
       "otuBerThRaise": otuBerThRaise,
       "otuBerThClear": otuBerThClear,
       "oduBerThRaise": oduBerThRaise,
       "oduBerThClear": oduBerThClear,
       "pcsBerThRaise": pcsBerThRaise,
       "pcsBerThClear": pcsBerThClear,
       "berTh-sRaise": berTh_sRaise,
       "berTh-sClear": berTh_sClear,
       "berTh-lRaise": berTh_lRaise,
       "berTh-lClear": berTh_lClear,
       "rs-berThRaise": rs_berThRaise,
       "rs-berThClear": rs_berThClear,
       "ms-berThRaise": ms_berThRaise,
       "ms-berThClear": ms_berThClear,
       "oneCableDisconnectedRaise": oneCableDisconnectedRaise,
       "oneCableDisconnectedClear": oneCableDisconnectedClear,
       "envCurrentHighThRaise": envCurrentHighThRaise,
       "envCurrentHighThClear": envCurrentHighThClear,
       "envCurrentLowThRaise": envCurrentLowThRaise,
       "envCurrentLowThClear": envCurrentLowThClear,
       "prbsRaise": prbsRaise,
       "prbsClear": prbsClear,
       "forcedRaise": forcedRaise,
       "forcedClear": forcedClear,
       "defRDICCMRaise": defRDICCMRaise,
       "defRDICCMClear": defRDICCMClear,
       "defMACStatusRaise": defMACStatusRaise,
       "defMACStatusClear": defMACStatusClear,
       "defRemoteCCMRaise": defRemoteCCMRaise,
       "defRemoteCCMClear": defRemoteCCMClear,
       "defErrorCCMRaise": defErrorCCMRaise,
       "defErrorCCMClear": defErrorCCMClear,
       "defXconCCMRaise": defXconCCMRaise,
       "defXconCCMClear": defXconCCMClear,
       "defBfdDownRaise": defBfdDownRaise,
       "defBfdDownClear": defBfdDownClear,
       "isisDbOvrldRaise": isisDbOvrldRaise,
       "isisDbOvrldClear": isisDbOvrldClear,
       "isisXDownRaise": isisXDownRaise,
       "isisXDownClear": isisXDownClear,
       "isisAdjDownRaise": isisAdjDownRaise,
       "isisAdjDownClear": isisAdjDownClear,
       "isisAdjRejectedRaise": isisAdjRejectedRaise,
       "isisAdjRejectedClear": isisAdjRejectedClear,
       "rsvpAdjDownRaise": rsvpAdjDownRaise,
       "rsvpAdjDownClear": rsvpAdjDownClear,
       "diskHighUsageRaise": diskHighUsageRaise,
       "diskHighUsageClear": diskHighUsageClear,
       "memHighUsageRaise": memHighUsageRaise,
       "memHighUsageClear": memHighUsageClear,
       "lockoutRaise": lockoutRaise,
       "lockoutClear": lockoutClear,
       "invUnknownRaise": invUnknownRaise,
       "invUnknownClear": invUnknownClear,
       "airfilterAbsenseRaise": airfilterAbsenseRaise,
       "airfilterAbsenseClear": airfilterAbsenseClear,
       "firmUpgrdFailRaise": firmUpgrdFailRaise,
       "firmUpgrdFailClear": firmUpgrdFailClear,
       "partitionFaultRaise": partitionFaultRaise,
       "partitionFaultClear": partitionFaultClear,
       "lolckRaise": lolckRaise,
       "lolckClear": lolckClear,
       "inventoryUnsuppRaise": inventoryUnsuppRaise,
       "inventoryUnsuppClear": inventoryUnsuppClear}
)
