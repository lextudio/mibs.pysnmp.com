# SNMP MIB module (AC-PSTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PSTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:37 2024
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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPSTN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPSTNConfiguration_ObjectIdentity = ObjectIdentity
acPSTNConfiguration = _AcPSTNConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1)
)
_AcTrunkConfig_ObjectIdentity = ObjectIdentity
acTrunkConfig = _AcTrunkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1)
)
_AcTrunk_ObjectIdentity = ObjectIdentity
acTrunk = _AcTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1)
)
_AcTrunkTable_Object = MibTable
acTrunkTable = _AcTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acTrunkTable.setStatus("current")
_AcTrunkEntry_Object = MibTableRow
acTrunkEntry = _AcTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1)
)
acTrunkEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkEntry.setStatus("current")


class _AcTrunkIndex_Type(Unsigned32):
    """Custom type acTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcTrunkIndex_Type.__name__ = "Unsigned32"
_AcTrunkIndex_Object = MibTableColumn
acTrunkIndex = _AcTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 1),
    _AcTrunkIndex_Type()
)
acTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkIndex.setStatus("current")


class _AcTrunkAdministrativeState_Type(Integer32):
    """Custom type acTrunkAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unLocked", 1))
    )


_AcTrunkAdministrativeState_Type.__name__ = "Integer32"
_AcTrunkAdministrativeState_Object = MibTableColumn
acTrunkAdministrativeState = _AcTrunkAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 2),
    _AcTrunkAdministrativeState_Type()
)
acTrunkAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkAdministrativeState.setStatus("current")


class _AcTrunkProtocolType_Type(Integer32):
    """Custom type acTrunkProtocolType based on Integer32"""
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
              43,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("bRI-5ESS", 53),
          ("bRI-DMS100", 52),
          ("bRI-EURO-ISDN", 50),
          ("bRI-IUA", 57),
          ("bRI-NI-2", 51),
          ("bRI-NTT", 56),
          ("bRI-QSIG", 54),
          ("bRI-VNG", 55),
          ("e1-AUSTEL-ISDN", 17),
          ("e1-CAS-R15", 41),
          ("e1-DUA", 37),
          ("e1-EXTRA-30", 30),
          ("e1-FRENCH-VN3-ISDN", 31),
          ("e1-HKT-ISDN", 18),
          ("e1-IUA", 29),
          ("e1-KOR-ISDN", 19),
          ("e1-NI2-ISDN", 40),
          ("e1-Q931-PACKETS", 38),
          ("e1-QSIG", 21),
          ("e1-TNZ-22", 22),
          ("e1CasR2", 8),
          ("e1EuroISDN", 1),
          ("e1Mfcr2", 7),
          ("e1RawCAS", 9),
          ("e1Transparent30", 6),
          ("e1Transparent31", 5),
          ("eXTRA-33", 33),
          ("j1-TRANSPARENT", 15),
          ("nONE", 0),
          ("t1-4EssISDN", 11),
          ("t1-5Ess-10-ISDN", 13),
          ("t1-5Ess-9-ISDN", 12),
          ("t1-DMS100-MERIDIAN-ISDN", 35),
          ("t1-Dms100-ISDN", 14),
          ("t1-EURO-ISDN", 34),
          ("t1-EXTRA-23", 23),
          ("t1-EXTRA-32", 32),
          ("t1-HKT-ISDN", 20),
          ("t1-IUA", 28),
          ("t1-NI1-ISDN", 36),
          ("t1-NI2ISDN", 10),
          ("t1-NTT-ISDN", 16),
          ("t1-Q931-PACKETS", 39),
          ("t1Cas", 2),
          ("t1RawCas", 3),
          ("t1Transparent", 4),
          ("v5", 43))
    )


_AcTrunkProtocolType_Type.__name__ = "Integer32"
_AcTrunkProtocolType_Object = MibTableColumn
acTrunkProtocolType = _AcTrunkProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 3),
    _AcTrunkProtocolType_Type()
)
acTrunkProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkProtocolType.setStatus("current")


class _AcTrunkClockMaster_Type(Integer32):
    """Custom type acTrunkClockMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acCLOCK-MASTER-OFF", 0),
          ("acCLOCK-MASTER-ON", 1))
    )


_AcTrunkClockMaster_Type.__name__ = "Integer32"
_AcTrunkClockMaster_Object = MibTableColumn
acTrunkClockMaster = _AcTrunkClockMaster_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 4),
    _AcTrunkClockMaster_Type()
)
acTrunkClockMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkClockMaster.setStatus("current")


class _AcTrunkFramingMethod_Type(Integer32):
    """Custom type acTrunkFramingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("e1-FRAMING-DDF", 2),
          ("e1-FRAMING-MFF-CRC4", 3),
          ("e1-FRAMING-MFF-CRC4-EXT", 4),
          ("eXTENDED-SUPER-FRAME", 0),
          ("sUPER-FRAME", 1),
          ("t1-FRAMING-ESF", 8),
          ("t1-FRAMING-ESF-CRC6", 9),
          ("t1-FRAMING-ESF-CRC6-JT", 11),
          ("t1-FRAMING-F12", 7),
          ("t1-FRAMING-F4", 6),
          ("t1-FRAMING-F72", 10))
    )


_AcTrunkFramingMethod_Type.__name__ = "Integer32"
_AcTrunkFramingMethod_Object = MibTableColumn
acTrunkFramingMethod = _AcTrunkFramingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 5),
    _AcTrunkFramingMethod_Type()
)
acTrunkFramingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkFramingMethod.setStatus("current")


class _AcTrunkLineCode_Type(Integer32):
    """Custom type acTrunkLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acAMI", 1),
          ("acB8ZS", 0),
          ("acHDB3", 2))
    )


_AcTrunkLineCode_Type.__name__ = "Integer32"
_AcTrunkLineCode_Object = MibTableColumn
acTrunkLineCode = _AcTrunkLineCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 6),
    _AcTrunkLineCode_Type()
)
acTrunkLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineCode.setStatus("current")


class _AcTrunkTraceLevel_Type(Integer32):
    """Custom type acTrunkTraceLevel based on Integer32"""
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
              10,
              11,
              12,
              15)
        )
    )
    namedValues = NamedValues(
        *(("acFULL-ISDN-TRACE", 1),
          ("acFULL-ISDN-TRACE-WITH-DUPLICATION", 5),
          ("acISDN-Q921-RAW-DATA-TRACE", 7),
          ("acISDN-Q931-Q921-RAW-DATA-TRACE", 8),
          ("acISDN-Q931-RAW-DATA-TRACE", 6),
          ("acLAYER3-ISDN-TRACE", 2),
          ("acLAYER3-ISDN-TRACE-NO-DUPLICATION", 4),
          ("acNO-TRACE", 0),
          ("acONLY-ISDN-Q931-MSGS-TRACE", 3),
          ("acSS7-AAL", 15),
          ("acSS7-MTP2", 10),
          ("acSS7-MTP2-AND-APPLI", 11),
          ("acSS7-MTP2-SL-L3-NO-MSU", 12))
    )


_AcTrunkTraceLevel_Type.__name__ = "Integer32"
_AcTrunkTraceLevel_Object = MibTableColumn
acTrunkTraceLevel = _AcTrunkTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 7),
    _AcTrunkTraceLevel_Type()
)
acTrunkTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkTraceLevel.setStatus("current")


class _AcTrunkDialPlanName_Type(SnmpAdminString):
    """Custom type acTrunkDialPlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AcTrunkDialPlanName_Type.__name__ = "SnmpAdminString"
_AcTrunkDialPlanName_Object = MibTableColumn
acTrunkDialPlanName = _AcTrunkDialPlanName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 8),
    _AcTrunkDialPlanName_Type()
)
acTrunkDialPlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkDialPlanName.setStatus("current")


class _AcTrunkLineType_Type(Integer32):
    """Custom type acTrunkLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              21)
        )
    )
    namedValues = NamedValues(
        *(("lineTypeBRI", 12),
          ("lineTypeE1", 10),
          ("lineTypeT1", 11),
          ("lineTypeUnknown", 21))
    )


_AcTrunkLineType_Type.__name__ = "Integer32"
_AcTrunkLineType_Object = MibTableColumn
acTrunkLineType = _AcTrunkLineType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 9),
    _AcTrunkLineType_Type()
)
acTrunkLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkLineType.setStatus("current")


class _AcTrunkAutoClockPriority_Type(Unsigned32):
    """Custom type acTrunkAutoClockPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcTrunkAutoClockPriority_Type.__name__ = "Unsigned32"
_AcTrunkAutoClockPriority_Object = MibTableColumn
acTrunkAutoClockPriority = _AcTrunkAutoClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 10),
    _AcTrunkAutoClockPriority_Type()
)
acTrunkAutoClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkAutoClockPriority.setStatus("current")


class _AcTrunkDeactivate_Type(Integer32):
    """Custom type acTrunkDeactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("deActivated", 1),
          ("notAvailable", 0))
    )


_AcTrunkDeactivate_Type.__name__ = "Integer32"
_AcTrunkDeactivate_Object = MibTableColumn
acTrunkDeactivate = _AcTrunkDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 1, 1, 1, 11),
    _AcTrunkDeactivate_Type()
)
acTrunkDeactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkDeactivate.setStatus("current")
_AcTrunkLine_ObjectIdentity = ObjectIdentity
acTrunkLine = _AcTrunkLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2)
)
_AcTrunkLineTable_Object = MibTable
acTrunkLineTable = _AcTrunkLineTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acTrunkLineTable.setStatus("current")
_AcTrunkLineEntry_Object = MibTableRow
acTrunkLineEntry = _AcTrunkLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1)
)
acTrunkLineEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkLineEntry.setStatus("current")


class _AcTrunkLineBuildOutLoss_Type(Integer32):
    """Custom type acTrunkLineBuildOutLoss based on Integer32"""
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
        *(("ac0DB", 0),
          ("ac15DB", 2),
          ("ac22-5DB", 3),
          ("ac7-5DB", 1))
    )


_AcTrunkLineBuildOutLoss_Type.__name__ = "Integer32"
_AcTrunkLineBuildOutLoss_Object = MibTableColumn
acTrunkLineBuildOutLoss = _AcTrunkLineBuildOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1, 1),
    _AcTrunkLineBuildOutLoss_Type()
)
acTrunkLineBuildOutLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineBuildOutLoss.setStatus("current")


class _AcTrunkLineBuildOutOverwrite_Type(Integer32):
    """Custom type acTrunkLineBuildOutOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acNO-OVER-WRITE", 0),
          ("acOVER-WRITE", 1))
    )


_AcTrunkLineBuildOutOverwrite_Type.__name__ = "Integer32"
_AcTrunkLineBuildOutOverwrite_Object = MibTableColumn
acTrunkLineBuildOutOverwrite = _AcTrunkLineBuildOutOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1, 2),
    _AcTrunkLineBuildOutOverwrite_Type()
)
acTrunkLineBuildOutOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineBuildOutOverwrite.setStatus("current")


class _AcTrunkLineBuildOutXPM0_Type(Unsigned32):
    """Custom type acTrunkLineBuildOutXPM0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcTrunkLineBuildOutXPM0_Type.__name__ = "Unsigned32"
_AcTrunkLineBuildOutXPM0_Object = MibTableColumn
acTrunkLineBuildOutXPM0 = _AcTrunkLineBuildOutXPM0_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1, 3),
    _AcTrunkLineBuildOutXPM0_Type()
)
acTrunkLineBuildOutXPM0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineBuildOutXPM0.setStatus("current")


class _AcTrunkLineBuildOutXPM1_Type(Unsigned32):
    """Custom type acTrunkLineBuildOutXPM1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcTrunkLineBuildOutXPM1_Type.__name__ = "Unsigned32"
_AcTrunkLineBuildOutXPM1_Object = MibTableColumn
acTrunkLineBuildOutXPM1 = _AcTrunkLineBuildOutXPM1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1, 4),
    _AcTrunkLineBuildOutXPM1_Type()
)
acTrunkLineBuildOutXPM1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineBuildOutXPM1.setStatus("current")


class _AcTrunkLineBuildOutXPM2_Type(Unsigned32):
    """Custom type acTrunkLineBuildOutXPM2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcTrunkLineBuildOutXPM2_Type.__name__ = "Unsigned32"
_AcTrunkLineBuildOutXPM2_Object = MibTableColumn
acTrunkLineBuildOutXPM2 = _AcTrunkLineBuildOutXPM2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 2, 1, 1, 5),
    _AcTrunkLineBuildOutXPM2_Type()
)
acTrunkLineBuildOutXPM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkLineBuildOutXPM2.setStatus("current")
_AcTrunkISDN_ObjectIdentity = ObjectIdentity
acTrunkISDN = _AcTrunkISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3)
)
_AcTrunkISDNCommon_ObjectIdentity = ObjectIdentity
acTrunkISDNCommon = _AcTrunkISDNCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1)
)
_AcTrunkISDNCommonTable_Object = MibTable
acTrunkISDNCommonTable = _AcTrunkISDNCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    acTrunkISDNCommonTable.setStatus("current")
_AcTrunkISDNCommonEntry_Object = MibTableRow
acTrunkISDNCommonEntry = _AcTrunkISDNCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1)
)
acTrunkISDNCommonEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkISDNCommonEntry.setStatus("current")


class _AcTrunkISDNCommonTerminationSide_Type(Integer32):
    """Custom type acTrunkISDNCommonTerminationSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acNETWORK-TERMINATION-SIDE", 1),
          ("acUSER-TERMINATION-SIDE", 0))
    )


_AcTrunkISDNCommonTerminationSide_Type.__name__ = "Integer32"
_AcTrunkISDNCommonTerminationSide_Object = MibTableColumn
acTrunkISDNCommonTerminationSide = _AcTrunkISDNCommonTerminationSide_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 1),
    _AcTrunkISDNCommonTerminationSide_Type()
)
acTrunkISDNCommonTerminationSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonTerminationSide.setStatus("current")


class _AcTrunkISDNCommonQ931LayerResponseBehavior_Type(Integer32):
    """Custom type acTrunkISDNCommonQ931LayerResponseBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_AcTrunkISDNCommonQ931LayerResponseBehavior_Type.__name__ = "Integer32"
_AcTrunkISDNCommonQ931LayerResponseBehavior_Object = MibTableColumn
acTrunkISDNCommonQ931LayerResponseBehavior = _AcTrunkISDNCommonQ931LayerResponseBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 2),
    _AcTrunkISDNCommonQ931LayerResponseBehavior_Type()
)
acTrunkISDNCommonQ931LayerResponseBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonQ931LayerResponseBehavior.setStatus("current")


class _AcTrunkISDNCommonIncomingCallsBehavior_Type(Unsigned32):
    """Custom type acTrunkISDNCommonIncomingCallsBehavior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcTrunkISDNCommonIncomingCallsBehavior_Type.__name__ = "Unsigned32"
_AcTrunkISDNCommonIncomingCallsBehavior_Object = MibTableColumn
acTrunkISDNCommonIncomingCallsBehavior = _AcTrunkISDNCommonIncomingCallsBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 3),
    _AcTrunkISDNCommonIncomingCallsBehavior_Type()
)
acTrunkISDNCommonIncomingCallsBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonIncomingCallsBehavior.setStatus("current")


class _AcTrunkISDNCommonOutgoingCallsBehavior_Type(Unsigned32):
    """Custom type acTrunkISDNCommonOutgoingCallsBehavior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcTrunkISDNCommonOutgoingCallsBehavior_Type.__name__ = "Unsigned32"
_AcTrunkISDNCommonOutgoingCallsBehavior_Object = MibTableColumn
acTrunkISDNCommonOutgoingCallsBehavior = _AcTrunkISDNCommonOutgoingCallsBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 4),
    _AcTrunkISDNCommonOutgoingCallsBehavior_Type()
)
acTrunkISDNCommonOutgoingCallsBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonOutgoingCallsBehavior.setStatus("current")


class _AcTrunkISDNCommonGeneralCCBehavior_Type(Unsigned32):
    """Custom type acTrunkISDNCommonGeneralCCBehavior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcTrunkISDNCommonGeneralCCBehavior_Type.__name__ = "Unsigned32"
_AcTrunkISDNCommonGeneralCCBehavior_Object = MibTableColumn
acTrunkISDNCommonGeneralCCBehavior = _AcTrunkISDNCommonGeneralCCBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 5),
    _AcTrunkISDNCommonGeneralCCBehavior_Type()
)
acTrunkISDNCommonGeneralCCBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonGeneralCCBehavior.setStatus("current")


class _AcTrunkISDNCommonIuaInterfaceId_Type(Integer32):
    """Custom type acTrunkISDNCommonIuaInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcTrunkISDNCommonIuaInterfaceId_Type.__name__ = "Integer32"
_AcTrunkISDNCommonIuaInterfaceId_Object = MibTableColumn
acTrunkISDNCommonIuaInterfaceId = _AcTrunkISDNCommonIuaInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 6),
    _AcTrunkISDNCommonIuaInterfaceId_Type()
)
acTrunkISDNCommonIuaInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkISDNCommonIuaInterfaceId.setStatus("current")


class _AcTrunkISDNCommonDuplicateQ931BuffMode_Type(Unsigned32):
    """Custom type acTrunkISDNCommonDuplicateQ931BuffMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcTrunkISDNCommonDuplicateQ931BuffMode_Type.__name__ = "Unsigned32"
_AcTrunkISDNCommonDuplicateQ931BuffMode_Object = MibTableColumn
acTrunkISDNCommonDuplicateQ931BuffMode = _AcTrunkISDNCommonDuplicateQ931BuffMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 7),
    _AcTrunkISDNCommonDuplicateQ931BuffMode_Type()
)
acTrunkISDNCommonDuplicateQ931BuffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonDuplicateQ931BuffMode.setStatus("current")


class _AcTrunkISDNCommonBRILayer2Mode_Type(Integer32):
    """Custom type acTrunkISDNCommonBRILayer2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bRI-L2-MODE-P2MP", 1),
          ("bRI-L2-MODE-P2P", 0))
    )


_AcTrunkISDNCommonBRILayer2Mode_Type.__name__ = "Integer32"
_AcTrunkISDNCommonBRILayer2Mode_Object = MibTableColumn
acTrunkISDNCommonBRILayer2Mode = _AcTrunkISDNCommonBRILayer2Mode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 1, 1, 1, 8),
    _AcTrunkISDNCommonBRILayer2Mode_Type()
)
acTrunkISDNCommonBRILayer2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNCommonBRILayer2Mode.setStatus("current")
_AcTrunkISDNNfas_ObjectIdentity = ObjectIdentity
acTrunkISDNNfas = _AcTrunkISDNNfas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2)
)
_AcTrunkISDNNfasTable_Object = MibTable
acTrunkISDNNfasTable = _AcTrunkISDNNfasTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    acTrunkISDNNfasTable.setStatus("current")
_AcTrunkISDNNfasEntry_Object = MibTableRow
acTrunkISDNNfasEntry = _AcTrunkISDNNfasEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2, 1, 1)
)
acTrunkISDNNfasEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkISDNNfasEntry.setStatus("current")


class _AcTrunkISDNNfasDchConfig_Type(Integer32):
    """Custom type acTrunkISDNNfasDchConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acDCH-CONFIG-BACKUP", 1),
          ("acDCH-CONFIG-NFAS", 2),
          ("acDCH-CONFIG-PRIMARY", 0))
    )


_AcTrunkISDNNfasDchConfig_Type.__name__ = "Integer32"
_AcTrunkISDNNfasDchConfig_Object = MibTableColumn
acTrunkISDNNfasDchConfig = _AcTrunkISDNNfasDchConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2, 1, 1, 1),
    _AcTrunkISDNNfasDchConfig_Type()
)
acTrunkISDNNfasDchConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNNfasDchConfig.setStatus("current")


class _AcTrunkISDNNfasInterfaceId_Type(Unsigned32):
    """Custom type acTrunkISDNNfasInterfaceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcTrunkISDNNfasInterfaceId_Type.__name__ = "Unsigned32"
_AcTrunkISDNNfasInterfaceId_Object = MibTableColumn
acTrunkISDNNfasInterfaceId = _AcTrunkISDNNfasInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2, 1, 1, 2),
    _AcTrunkISDNNfasInterfaceId_Type()
)
acTrunkISDNNfasInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNNfasInterfaceId.setStatus("current")


class _AcTrunkISDNNfasGroupNumber_Type(Unsigned32):
    """Custom type acTrunkISDNNfasGroupNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcTrunkISDNNfasGroupNumber_Type.__name__ = "Unsigned32"
_AcTrunkISDNNfasGroupNumber_Object = MibTableColumn
acTrunkISDNNfasGroupNumber = _AcTrunkISDNNfasGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 2, 1, 1, 3),
    _AcTrunkISDNNfasGroupNumber_Type()
)
acTrunkISDNNfasGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNNfasGroupNumber.setStatus("current")
_AcTrunkISDNDpnss_ObjectIdentity = ObjectIdentity
acTrunkISDNDpnss = _AcTrunkISDNDpnss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3)
)
_AcTrunkISDNDpnssTable_Object = MibTable
acTrunkISDNDpnssTable = _AcTrunkISDNDpnssTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    acTrunkISDNDpnssTable.setStatus("current")
_AcTrunkISDNDpnssEntry_Object = MibTableRow
acTrunkISDNDpnssEntry = _AcTrunkISDNDpnssEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3, 1, 1)
)
acTrunkISDNDpnssEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkISDNDpnssEntry.setStatus("current")


class _AcTrunkISDNDpnssBehavior_Type(Unsigned32):
    """Custom type acTrunkISDNDpnssBehavior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcTrunkISDNDpnssBehavior_Type.__name__ = "Unsigned32"
_AcTrunkISDNDpnssBehavior_Object = MibTableColumn
acTrunkISDNDpnssBehavior = _AcTrunkISDNDpnssBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3, 1, 1, 1),
    _AcTrunkISDNDpnssBehavior_Type()
)
acTrunkISDNDpnssBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNDpnssBehavior.setStatus("current")


class _AcTrunkISDNDpnssNumRealChannels_Type(Unsigned32):
    """Custom type acTrunkISDNDpnssNumRealChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AcTrunkISDNDpnssNumRealChannels_Type.__name__ = "Unsigned32"
_AcTrunkISDNDpnssNumRealChannels_Object = MibTableColumn
acTrunkISDNDpnssNumRealChannels = _AcTrunkISDNDpnssNumRealChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3, 1, 1, 2),
    _AcTrunkISDNDpnssNumRealChannels_Type()
)
acTrunkISDNDpnssNumRealChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNDpnssNumRealChannels.setStatus("current")


class _AcTrunkISDNDpnssNumVirtualChannels_Type(Unsigned32):
    """Custom type acTrunkISDNDpnssNumVirtualChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcTrunkISDNDpnssNumVirtualChannels_Type.__name__ = "Unsigned32"
_AcTrunkISDNDpnssNumVirtualChannels_Object = MibTableColumn
acTrunkISDNDpnssNumVirtualChannels = _AcTrunkISDNDpnssNumVirtualChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 3, 3, 1, 1, 3),
    _AcTrunkISDNDpnssNumVirtualChannels_Type()
)
acTrunkISDNDpnssNumVirtualChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkISDNDpnssNumVirtualChannels.setStatus("current")
_AcTrunkCAS_ObjectIdentity = ObjectIdentity
acTrunkCAS = _AcTrunkCAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 4)
)
_AcTrunkCASTable_Object = MibTable
acTrunkCASTable = _AcTrunkCASTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    acTrunkCASTable.setStatus("current")
_AcTrunkCASEntry_Object = MibTableRow
acTrunkCASEntry = _AcTrunkCASEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 4, 1, 1)
)
acTrunkCASEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkCASEntry.setStatus("current")


class _AcTrunkCASTablesIndex_Type(Unsigned32):
    """Custom type acTrunkCASTablesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcTrunkCASTablesIndex_Type.__name__ = "Unsigned32"
_AcTrunkCASTablesIndex_Object = MibTableColumn
acTrunkCASTablesIndex = _AcTrunkCASTablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 4, 1, 1, 1),
    _AcTrunkCASTablesIndex_Type()
)
acTrunkCASTablesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkCASTablesIndex.setStatus("current")


class _AcTrunkCASTablePerChannel_Type(SnmpAdminString):
    """Custom type acTrunkCASTablePerChannel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AcTrunkCASTablePerChannel_Type.__name__ = "SnmpAdminString"
_AcTrunkCASTablePerChannel_Object = MibTableColumn
acTrunkCASTablePerChannel = _AcTrunkCASTablePerChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 4, 1, 1, 2),
    _AcTrunkCASTablePerChannel_Type()
)
acTrunkCASTablePerChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkCASTablePerChannel.setStatus("current")
_AcTrunkV5_ObjectIdentity = ObjectIdentity
acTrunkV5 = _AcTrunkV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 5)
)
_AcTrunkV5Table_Object = MibTable
acTrunkV5Table = _AcTrunkV5Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    acTrunkV5Table.setStatus("current")
_AcTrunkV5Entry_Object = MibTableRow
acTrunkV5Entry = _AcTrunkV5Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 5, 1, 1)
)
acTrunkV5Entry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkV5Entry.setStatus("current")


class _AcTrunkV5NumberOfCChannels_Type(Unsigned32):
    """Custom type acTrunkV5NumberOfCChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcTrunkV5NumberOfCChannels_Type.__name__ = "Unsigned32"
_AcTrunkV5NumberOfCChannels_Object = MibTableColumn
acTrunkV5NumberOfCChannels = _AcTrunkV5NumberOfCChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 5, 1, 1, 1),
    _AcTrunkV5NumberOfCChannels_Type()
)
acTrunkV5NumberOfCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkV5NumberOfCChannels.setStatus("current")


class _AcTrunkV5ProtocolSide_Type(Integer32):
    """Custom type acTrunkV5ProtocolSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("an-Side", 0),
          ("le-Side", 1))
    )


_AcTrunkV5ProtocolSide_Type.__name__ = "Integer32"
_AcTrunkV5ProtocolSide_Object = MibTableColumn
acTrunkV5ProtocolSide = _AcTrunkV5ProtocolSide_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 5, 1, 1, 2),
    _AcTrunkV5ProtocolSide_Type()
)
acTrunkV5ProtocolSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkV5ProtocolSide.setStatus("current")
_AcTrunkGlobal_ObjectIdentity = ObjectIdentity
acTrunkGlobal = _AcTrunkGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 8)
)


class _AcTrunkGlobalLifeLineType_Type(Integer32):
    """Custom type acTrunkGlobalLifeLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hW-And-Link-And-Network-Detection", 2),
          ("hW-And-Link-Detection", 1),
          ("hW-Only", 0))
    )


_AcTrunkGlobalLifeLineType_Type.__name__ = "Integer32"
_AcTrunkGlobalLifeLineType_Object = MibScalar
acTrunkGlobalLifeLineType = _AcTrunkGlobalLifeLineType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 1, 8, 1),
    _AcTrunkGlobalLifeLineType_Type()
)
acTrunkGlobalLifeLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkGlobalLifeLineType.setStatus("current")
_AcISDNConfig_ObjectIdentity = ObjectIdentity
acISDNConfig = _AcISDNConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 2)
)
_AcMiscISDN_ObjectIdentity = ObjectIdentity
acMiscISDN = _AcMiscISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 2, 1)
)


class _AcMiscISDNQ931RelayMode_Type(Integer32):
    """Custom type acMiscISDNQ931RelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activateLAPDmessaging", 1),
          ("layer3-IS-IUA", 3),
          ("none", 0))
    )


_AcMiscISDNQ931RelayMode_Type.__name__ = "Integer32"
_AcMiscISDNQ931RelayMode_Object = MibScalar
acMiscISDNQ931RelayMode = _AcMiscISDNQ931RelayMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 2, 1, 1),
    _AcMiscISDNQ931RelayMode_Type()
)
acMiscISDNQ931RelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMiscISDNQ931RelayMode.setStatus("current")


class _AcMiscISDNDuplicateQ931BuffMode_Type(Unsigned32):
    """Custom type acMiscISDNDuplicateQ931BuffMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcMiscISDNDuplicateQ931BuffMode_Type.__name__ = "Unsigned32"
_AcMiscISDNDuplicateQ931BuffMode_Object = MibScalar
acMiscISDNDuplicateQ931BuffMode = _AcMiscISDNDuplicateQ931BuffMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 2, 1, 2),
    _AcMiscISDNDuplicateQ931BuffMode_Type()
)
acMiscISDNDuplicateQ931BuffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMiscISDNDuplicateQ931BuffMode.setStatus("obsolete")
_AcDS3Config_ObjectIdentity = ObjectIdentity
acDS3Config = _AcDS3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 3)
)


class _AcDS3ConfigFramingMethod_Type(Integer32):
    """Custom type acDS3ConfigFramingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dS3-C-BIT-PARITY", 1),
          ("dS3-M23", 0))
    )


_AcDS3ConfigFramingMethod_Type.__name__ = "Integer32"
_AcDS3ConfigFramingMethod_Object = MibScalar
acDS3ConfigFramingMethod = _AcDS3ConfigFramingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 3, 1),
    _AcDS3ConfigFramingMethod_Type()
)
acDS3ConfigFramingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDS3ConfigFramingMethod.setStatus("obsolete")


class _AcDS3ConfigClockSource_Type(Integer32):
    """Custom type acDS3ConfigClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acClock-Source-External", 0),
          ("acClock-Source-Local-Board", 1),
          ("acClock-Source-Local-PLL", 2))
    )


_AcDS3ConfigClockSource_Type.__name__ = "Integer32"
_AcDS3ConfigClockSource_Object = MibScalar
acDS3ConfigClockSource = _AcDS3ConfigClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 3, 2),
    _AcDS3ConfigClockSource_Type()
)
acDS3ConfigClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDS3ConfigClockSource.setStatus("obsolete")


class _AcDS3ConfigLineBuiltOut_Type(Integer32):
    """Custom type acDS3ConfigLineBuiltOut based on Integer32"""
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
        *(("acLINE-BUILT-OUT-LEVEL-1", 0),
          ("acLINE-BUILT-OUT-LEVEL-2", 1),
          ("acLINE-BUILT-OUT-LEVEL-3", 2),
          ("acLINE-BUILT-OUT-LEVEL-4", 3),
          ("acLINE-BUILT-OUT-LEVEL-5", 4),
          ("acLINE-BUILT-OUT-LEVEL-6", 5))
    )


_AcDS3ConfigLineBuiltOut_Type.__name__ = "Integer32"
_AcDS3ConfigLineBuiltOut_Object = MibScalar
acDS3ConfigLineBuiltOut = _AcDS3ConfigLineBuiltOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 3, 3),
    _AcDS3ConfigLineBuiltOut_Type()
)
acDS3ConfigLineBuiltOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDS3ConfigLineBuiltOut.setStatus("obsolete")
_AcCasConfig_ObjectIdentity = ObjectIdentity
acCasConfig = _AcCasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4)
)


class _AcCasConfigEnable_Type(Integer32):
    """Custom type acCasConfigEnable based on Integer32"""
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


_AcCasConfigEnable_Type.__name__ = "Integer32"
_AcCasConfigEnable_Object = MibScalar
acCasConfigEnable = _AcCasConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 1),
    _AcCasConfigEnable_Type()
)
acCasConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acCasConfigEnable.setStatus("current")
_AcCASFile_ObjectIdentity = ObjectIdentity
acCASFile = _AcCASFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 2)
)
_AcCASFileTable_Object = MibTable
acCASFileTable = _AcCASFileTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    acCASFileTable.setStatus("current")
_AcCASFileEntry_Object = MibTableRow
acCASFileEntry = _AcCASFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 2, 1, 1)
)
acCASFileEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acCASFileIndex"),
)
if mibBuilder.loadTexts:
    acCASFileEntry.setStatus("current")


class _AcCASFileIndex_Type(Unsigned32):
    """Custom type acCASFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcCASFileIndex_Type.__name__ = "Unsigned32"
_AcCASFileIndex_Object = MibTableColumn
acCASFileIndex = _AcCASFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 2, 1, 1, 1),
    _AcCASFileIndex_Type()
)
acCASFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCASFileIndex.setStatus("current")


class _AcCASFileName_Type(SnmpAdminString):
    """Custom type acCASFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcCASFileName_Type.__name__ = "SnmpAdminString"
_AcCASFileName_Object = MibTableColumn
acCASFileName = _AcCASFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 4, 2, 1, 1, 2),
    _AcCASFileName_Type()
)
acCASFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCASFileName.setStatus("current")
_AcSonetSDH_ObjectIdentity = ObjectIdentity
acSonetSDH = _AcSonetSDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5)
)
_AcSonetSDHTable_Object = MibTable
acSonetSDHTable = _AcSonetSDHTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    acSonetSDHTable.setStatus("current")
_AcSonetSDHEntry_Object = MibTableRow
acSonetSDHEntry = _AcSonetSDHEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1)
)
acSonetSDHEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acSonetSDHIndex"),
)
if mibBuilder.loadTexts:
    acSonetSDHEntry.setStatus("current")


class _AcSonetSDHIndex_Type(Unsigned32):
    """Custom type acSonetSDHIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSonetSDHIndex_Type.__name__ = "Unsigned32"
_AcSonetSDHIndex_Object = MibTableColumn
acSonetSDHIndex = _AcSonetSDHIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 1),
    _AcSonetSDHIndex_Type()
)
acSonetSDHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSonetSDHIndex.setStatus("current")


class _AcSonetSDHFbrGrpMappingType_Type(Integer32):
    """Custom type acSonetSDHFbrGrpMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              15)
        )
    )
    namedValues = NamedValues(
        *(("asynchronousTU12andE1", 1),
          ("asynchronousVT15andDS1", 0),
          ("sTS1asynchronousDS3", 3),
          ("undefined", 15))
    )


_AcSonetSDHFbrGrpMappingType_Type.__name__ = "Integer32"
_AcSonetSDHFbrGrpMappingType_Object = MibTableColumn
acSonetSDHFbrGrpMappingType = _AcSonetSDHFbrGrpMappingType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 2),
    _AcSonetSDHFbrGrpMappingType_Type()
)
acSonetSDHFbrGrpMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSDHFbrGrpMappingType.setStatus("current")


class _AcSonetSDHFbrGrpKlmNumberingScheme_Type(Integer32):
    """Custom type acSonetSDHFbrGrpKlmNumberingScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numberingScheme-KLM", 2),
          ("numberingScheme-LMK", 1),
          ("numberingScheme-MLK", 0))
    )


_AcSonetSDHFbrGrpKlmNumberingScheme_Type.__name__ = "Integer32"
_AcSonetSDHFbrGrpKlmNumberingScheme_Object = MibTableColumn
acSonetSDHFbrGrpKlmNumberingScheme = _AcSonetSDHFbrGrpKlmNumberingScheme_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 3),
    _AcSonetSDHFbrGrpKlmNumberingScheme_Type()
)
acSonetSDHFbrGrpKlmNumberingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSDHFbrGrpKlmNumberingScheme.setStatus("current")


class _AcSonetSDHFbrGrpAPSDirectionMode_Type(Integer32):
    """Custom type acSonetSDHFbrGrpAPSDirectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 0))
    )


_AcSonetSDHFbrGrpAPSDirectionMode_Type.__name__ = "Integer32"
_AcSonetSDHFbrGrpAPSDirectionMode_Object = MibTableColumn
acSonetSDHFbrGrpAPSDirectionMode = _AcSonetSDHFbrGrpAPSDirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 4),
    _AcSonetSDHFbrGrpAPSDirectionMode_Type()
)
acSonetSDHFbrGrpAPSDirectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSDHFbrGrpAPSDirectionMode.setStatus("current")


class _AcSonetSDHFbrGrpAPSRevertMode_Type(Integer32):
    """Custom type acSonetSDHFbrGrpAPSRevertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 0),
          ("revertive", 1))
    )


_AcSonetSDHFbrGrpAPSRevertMode_Type.__name__ = "Integer32"
_AcSonetSDHFbrGrpAPSRevertMode_Object = MibTableColumn
acSonetSDHFbrGrpAPSRevertMode = _AcSonetSDHFbrGrpAPSRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 5),
    _AcSonetSDHFbrGrpAPSRevertMode_Type()
)
acSonetSDHFbrGrpAPSRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSDHFbrGrpAPSRevertMode.setStatus("current")


class _AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type(Unsigned32):
    """Custom type acSonetSDHFbrGrpAPSWaitToRestoreTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type.__name__ = "Unsigned32"
_AcSonetSDHFbrGrpAPSWaitToRestoreTime_Object = MibTableColumn
acSonetSDHFbrGrpAPSWaitToRestoreTime = _AcSonetSDHFbrGrpAPSWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 1, 5, 1, 1, 6),
    _AcSonetSDHFbrGrpAPSWaitToRestoreTime_Type()
)
acSonetSDHFbrGrpAPSWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSDHFbrGrpAPSWaitToRestoreTime.setStatus("current")
_AcPSTNStatus_ObjectIdentity = ObjectIdentity
acPSTNStatus = _AcPSTNStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2)
)
_AcTrunkStatus_ObjectIdentity = ObjectIdentity
acTrunkStatus = _AcTrunkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1)
)
_AcTrunkStatusTable_Object = MibTable
acTrunkStatusTable = _AcTrunkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acTrunkStatusTable.setStatus("current")
_AcTrunkStatusEntry_Object = MibTableRow
acTrunkStatusEntry = _AcTrunkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1)
)
acTrunkStatusEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acTrunkIndex"),
)
if mibBuilder.loadTexts:
    acTrunkStatusEntry.setStatus("current")


class _AcTrunkStatusLedStatusColor_Type(Integer32):
    """Custom type acTrunkStatusLedStatusColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("off", 0),
          ("red", 1))
    )


_AcTrunkStatusLedStatusColor_Type.__name__ = "Integer32"
_AcTrunkStatusLedStatusColor_Object = MibTableColumn
acTrunkStatusLedStatusColor = _AcTrunkStatusLedStatusColor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 1),
    _AcTrunkStatusLedStatusColor_Type()
)
acTrunkStatusLedStatusColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusLedStatusColor.setStatus("current")


class _AcTrunkStatusLedStatusState_Type(Integer32):
    """Custom type acTrunkStatusLedStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blink", 1),
          ("steady", 0))
    )


_AcTrunkStatusLedStatusState_Type.__name__ = "Integer32"
_AcTrunkStatusLedStatusState_Object = MibTableColumn
acTrunkStatusLedStatusState = _AcTrunkStatusLedStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 2),
    _AcTrunkStatusLedStatusState_Type()
)
acTrunkStatusLedStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusLedStatusState.setStatus("current")


class _AcTrunkStatusChannels_Type(OctetString):
    """Custom type acTrunkStatusChannels based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcTrunkStatusChannels_Type.__name__ = "OctetString"
_AcTrunkStatusChannels_Object = MibTableColumn
acTrunkStatusChannels = _AcTrunkStatusChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 3),
    _AcTrunkStatusChannels_Type()
)
acTrunkStatusChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusChannels.setStatus("current")


class _AcTrunkStatusV5InterfaceNum_Type(Integer32):
    """Custom type acTrunkStatusV5InterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_AcTrunkStatusV5InterfaceNum_Type.__name__ = "Integer32"
_AcTrunkStatusV5InterfaceNum_Object = MibTableColumn
acTrunkStatusV5InterfaceNum = _AcTrunkStatusV5InterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 4),
    _AcTrunkStatusV5InterfaceNum_Type()
)
acTrunkStatusV5InterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusV5InterfaceNum.setStatus("current")


class _AcTrunkStatusV5LinkID_Type(Integer32):
    """Custom type acTrunkStatusV5LinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 62),
    )


_AcTrunkStatusV5LinkID_Type.__name__ = "Integer32"
_AcTrunkStatusV5LinkID_Object = MibTableColumn
acTrunkStatusV5LinkID = _AcTrunkStatusV5LinkID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 5),
    _AcTrunkStatusV5LinkID_Type()
)
acTrunkStatusV5LinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusV5LinkID.setStatus("current")


class _AcTrunkStatusDChannel_Type(Integer32):
    """Custom type acTrunkStatusDChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dChannelEstablished", 0),
          ("dChannelNotApplicable", 10),
          ("dChannelNotEstablished", 1))
    )


_AcTrunkStatusDChannel_Type.__name__ = "Integer32"
_AcTrunkStatusDChannel_Object = MibTableColumn
acTrunkStatusDChannel = _AcTrunkStatusDChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 6),
    _AcTrunkStatusDChannel_Type()
)
acTrunkStatusDChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusDChannel.setStatus("current")


class _AcTrunkStatusAlarm_Type(Integer32):
    """Custom type acTrunkStatusAlarm based on Integer32"""
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
        *(("blueAis", 3),
          ("greenActive", 1),
          ("greyDisabled", 0),
          ("orangeDChannel", 5),
          ("purpleLowerLayerDown", 6),
          ("redLosLof", 2),
          ("yellowRai", 4))
    )


_AcTrunkStatusAlarm_Type.__name__ = "Integer32"
_AcTrunkStatusAlarm_Object = MibTableColumn
acTrunkStatusAlarm = _AcTrunkStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 1, 1, 1, 7),
    _AcTrunkStatusAlarm_Type()
)
acTrunkStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkStatusAlarm.setStatus("current")
_AcDigitalLegs_ObjectIdentity = ObjectIdentity
acDigitalLegs = _AcDigitalLegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2)
)
_AcDigitalLegsTable_Object = MibTable
acDigitalLegsTable = _AcDigitalLegsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acDigitalLegsTable.setStatus("current")
_AcDigitalLegsEntry_Object = MibTableRow
acDigitalLegsEntry = _AcDigitalLegsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1)
)
acDigitalLegsEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acDigitalLegsLegIndex"),
)
if mibBuilder.loadTexts:
    acDigitalLegsEntry.setStatus("current")


class _AcDigitalLegsLegIndex_Type(Unsigned32):
    """Custom type acDigitalLegsLegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcDigitalLegsLegIndex_Type.__name__ = "Unsigned32"
_AcDigitalLegsLegIndex_Object = MibTableColumn
acDigitalLegsLegIndex = _AcDigitalLegsLegIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 1),
    _AcDigitalLegsLegIndex_Type()
)
acDigitalLegsLegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDigitalLegsLegIndex.setStatus("current")


class _AcDigitalLegsCallIndex_Type(Unsigned32):
    """Custom type acDigitalLegsCallIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcDigitalLegsCallIndex_Type.__name__ = "Unsigned32"
_AcDigitalLegsCallIndex_Object = MibTableColumn
acDigitalLegsCallIndex = _AcDigitalLegsCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 2),
    _AcDigitalLegsCallIndex_Type()
)
acDigitalLegsCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsCallIndex.setStatus("current")


class _AcDigitalLegsTrunk_Type(Unsigned32):
    """Custom type acDigitalLegsTrunk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDigitalLegsTrunk_Type.__name__ = "Unsigned32"
_AcDigitalLegsTrunk_Object = MibTableColumn
acDigitalLegsTrunk = _AcDigitalLegsTrunk_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 3),
    _AcDigitalLegsTrunk_Type()
)
acDigitalLegsTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsTrunk.setStatus("current")


class _AcDigitalLegsBchannel_Type(Unsigned32):
    """Custom type acDigitalLegsBchannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76500),
    )


_AcDigitalLegsBchannel_Type.__name__ = "Unsigned32"
_AcDigitalLegsBchannel_Object = MibTableColumn
acDigitalLegsBchannel = _AcDigitalLegsBchannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 4),
    _AcDigitalLegsBchannel_Type()
)
acDigitalLegsBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsBchannel.setStatus("current")


class _AcDigitalLegsEchoCanceller_Type(Integer32):
    """Custom type acDigitalLegsEchoCanceller based on Integer32"""
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


_AcDigitalLegsEchoCanceller_Type.__name__ = "Integer32"
_AcDigitalLegsEchoCanceller_Object = MibTableColumn
acDigitalLegsEchoCanceller = _AcDigitalLegsEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 5),
    _AcDigitalLegsEchoCanceller_Type()
)
acDigitalLegsEchoCanceller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsEchoCanceller.setStatus("current")


class _AcDigitalLegsDTMFDetection_Type(Integer32):
    """Custom type acDigitalLegsDTMFDetection based on Integer32"""
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


_AcDigitalLegsDTMFDetection_Type.__name__ = "Integer32"
_AcDigitalLegsDTMFDetection_Object = MibTableColumn
acDigitalLegsDTMFDetection = _AcDigitalLegsDTMFDetection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 6),
    _AcDigitalLegsDTMFDetection_Type()
)
acDigitalLegsDTMFDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsDTMFDetection.setStatus("current")


class _AcDigitalLegsVoiceVolume_Type(Unsigned32):
    """Custom type acDigitalLegsVoiceVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AcDigitalLegsVoiceVolume_Type.__name__ = "Unsigned32"
_AcDigitalLegsVoiceVolume_Object = MibTableColumn
acDigitalLegsVoiceVolume = _AcDigitalLegsVoiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 7),
    _AcDigitalLegsVoiceVolume_Type()
)
acDigitalLegsVoiceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsVoiceVolume.setStatus("current")


class _AcDigitalLegsHighPassFilter_Type(Integer32):
    """Custom type acDigitalLegsHighPassFilter based on Integer32"""
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


_AcDigitalLegsHighPassFilter_Type.__name__ = "Integer32"
_AcDigitalLegsHighPassFilter_Object = MibTableColumn
acDigitalLegsHighPassFilter = _AcDigitalLegsHighPassFilter_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 8),
    _AcDigitalLegsHighPassFilter_Type()
)
acDigitalLegsHighPassFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsHighPassFilter.setStatus("current")


class _AcDigitalLegsInputGain_Type(Integer32):
    """Custom type acDigitalLegsInputGain based on Integer32"""
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


_AcDigitalLegsInputGain_Type.__name__ = "Integer32"
_AcDigitalLegsInputGain_Object = MibTableColumn
acDigitalLegsInputGain = _AcDigitalLegsInputGain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 9),
    _AcDigitalLegsInputGain_Type()
)
acDigitalLegsInputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsInputGain.setStatus("current")


class _AcDigitalLegsDSPDevice_Type(Unsigned32):
    """Custom type acDigitalLegsDSPDevice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AcDigitalLegsDSPDevice_Type.__name__ = "Unsigned32"
_AcDigitalLegsDSPDevice_Object = MibTableColumn
acDigitalLegsDSPDevice = _AcDigitalLegsDSPDevice_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 10),
    _AcDigitalLegsDSPDevice_Type()
)
acDigitalLegsDSPDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsDSPDevice.setStatus("current")


class _AcDigitalLegsLegName_Type(SnmpAdminString):
    """Custom type acDigitalLegsLegName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcDigitalLegsLegName_Type.__name__ = "SnmpAdminString"
_AcDigitalLegsLegName_Object = MibTableColumn
acDigitalLegsLegName = _AcDigitalLegsLegName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 2, 1, 1, 11),
    _AcDigitalLegsLegName_Type()
)
acDigitalLegsLegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDigitalLegsLegName.setStatus("current")
_AcSDHKLMNumberingScheme_ObjectIdentity = ObjectIdentity
acSDHKLMNumberingScheme = _AcSDHKLMNumberingScheme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3)
)
_AcSDHKLMNumberingSchemeTable_Object = MibTable
acSDHKLMNumberingSchemeTable = _AcSDHKLMNumberingSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeTable.setStatus("current")
_AcSDHKLMNumberingSchemeEntry_Object = MibTableRow
acSDHKLMNumberingSchemeEntry = _AcSDHKLMNumberingSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1, 1)
)
acSDHKLMNumberingSchemeEntry.setIndexNames(
    (0, "AC-PSTN-MIB", "acSDHKLMNumberingSchemeTrunkIndex"),
)
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeEntry.setStatus("current")


class _AcSDHKLMNumberingSchemeTrunkIndex_Type(Unsigned32):
    """Custom type acSDHKLMNumberingSchemeTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcSDHKLMNumberingSchemeTrunkIndex_Type.__name__ = "Unsigned32"
_AcSDHKLMNumberingSchemeTrunkIndex_Object = MibTableColumn
acSDHKLMNumberingSchemeTrunkIndex = _AcSDHKLMNumberingSchemeTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1, 1, 1),
    _AcSDHKLMNumberingSchemeTrunkIndex_Type()
)
acSDHKLMNumberingSchemeTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeTrunkIndex.setStatus("current")


class _AcSDHKLMNumberingSchemeTUG3OrSTS1_Type(Unsigned32):
    """Custom type acSDHKLMNumberingSchemeTUG3OrSTS1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AcSDHKLMNumberingSchemeTUG3OrSTS1_Type.__name__ = "Unsigned32"
_AcSDHKLMNumberingSchemeTUG3OrSTS1_Object = MibTableColumn
acSDHKLMNumberingSchemeTUG3OrSTS1 = _AcSDHKLMNumberingSchemeTUG3OrSTS1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1, 1, 2),
    _AcSDHKLMNumberingSchemeTUG3OrSTS1_Type()
)
acSDHKLMNumberingSchemeTUG3OrSTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeTUG3OrSTS1.setStatus("current")


class _AcSDHKLMNumberingSchemeTUG2OrVTG_Type(Unsigned32):
    """Custom type acSDHKLMNumberingSchemeTUG2OrVTG based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AcSDHKLMNumberingSchemeTUG2OrVTG_Type.__name__ = "Unsigned32"
_AcSDHKLMNumberingSchemeTUG2OrVTG_Object = MibTableColumn
acSDHKLMNumberingSchemeTUG2OrVTG = _AcSDHKLMNumberingSchemeTUG2OrVTG_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1, 1, 3),
    _AcSDHKLMNumberingSchemeTUG2OrVTG_Type()
)
acSDHKLMNumberingSchemeTUG2OrVTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeTUG2OrVTG.setStatus("current")


class _AcSDHKLMNumberingSchemeTU12OrVT15_Type(Unsigned32):
    """Custom type acSDHKLMNumberingSchemeTU12OrVT15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSDHKLMNumberingSchemeTU12OrVT15_Type.__name__ = "Unsigned32"
_AcSDHKLMNumberingSchemeTU12OrVT15_Object = MibTableColumn
acSDHKLMNumberingSchemeTU12OrVT15 = _AcSDHKLMNumberingSchemeTU12OrVT15_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 3, 1, 1, 4),
    _AcSDHKLMNumberingSchemeTU12OrVT15_Type()
)
acSDHKLMNumberingSchemeTU12OrVT15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSDHKLMNumberingSchemeTU12OrVT15.setStatus("current")
_AcFiberGroupStatus_ObjectIdentity = ObjectIdentity
acFiberGroupStatus = _AcFiberGroupStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 4)
)


class _AcFiberGroupStatusActiveLink_Type(Unsigned32):
    """Custom type acFiberGroupStatusActiveLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcFiberGroupStatusActiveLink_Type.__name__ = "Unsigned32"
_AcFiberGroupStatusActiveLink_Object = MibScalar
acFiberGroupStatusActiveLink = _AcFiberGroupStatusActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 9, 2, 4, 1),
    _AcFiberGroupStatusActiveLink_Type()
)
acFiberGroupStatusActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFiberGroupStatusActiveLink.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PSTN-MIB",
    **{"acPSTN": acPSTN,
       "acPSTNConfiguration": acPSTNConfiguration,
       "acTrunkConfig": acTrunkConfig,
       "acTrunk": acTrunk,
       "acTrunkTable": acTrunkTable,
       "acTrunkEntry": acTrunkEntry,
       "acTrunkIndex": acTrunkIndex,
       "acTrunkAdministrativeState": acTrunkAdministrativeState,
       "acTrunkProtocolType": acTrunkProtocolType,
       "acTrunkClockMaster": acTrunkClockMaster,
       "acTrunkFramingMethod": acTrunkFramingMethod,
       "acTrunkLineCode": acTrunkLineCode,
       "acTrunkTraceLevel": acTrunkTraceLevel,
       "acTrunkDialPlanName": acTrunkDialPlanName,
       "acTrunkLineType": acTrunkLineType,
       "acTrunkAutoClockPriority": acTrunkAutoClockPriority,
       "acTrunkDeactivate": acTrunkDeactivate,
       "acTrunkLine": acTrunkLine,
       "acTrunkLineTable": acTrunkLineTable,
       "acTrunkLineEntry": acTrunkLineEntry,
       "acTrunkLineBuildOutLoss": acTrunkLineBuildOutLoss,
       "acTrunkLineBuildOutOverwrite": acTrunkLineBuildOutOverwrite,
       "acTrunkLineBuildOutXPM0": acTrunkLineBuildOutXPM0,
       "acTrunkLineBuildOutXPM1": acTrunkLineBuildOutXPM1,
       "acTrunkLineBuildOutXPM2": acTrunkLineBuildOutXPM2,
       "acTrunkISDN": acTrunkISDN,
       "acTrunkISDNCommon": acTrunkISDNCommon,
       "acTrunkISDNCommonTable": acTrunkISDNCommonTable,
       "acTrunkISDNCommonEntry": acTrunkISDNCommonEntry,
       "acTrunkISDNCommonTerminationSide": acTrunkISDNCommonTerminationSide,
       "acTrunkISDNCommonQ931LayerResponseBehavior": acTrunkISDNCommonQ931LayerResponseBehavior,
       "acTrunkISDNCommonIncomingCallsBehavior": acTrunkISDNCommonIncomingCallsBehavior,
       "acTrunkISDNCommonOutgoingCallsBehavior": acTrunkISDNCommonOutgoingCallsBehavior,
       "acTrunkISDNCommonGeneralCCBehavior": acTrunkISDNCommonGeneralCCBehavior,
       "acTrunkISDNCommonIuaInterfaceId": acTrunkISDNCommonIuaInterfaceId,
       "acTrunkISDNCommonDuplicateQ931BuffMode": acTrunkISDNCommonDuplicateQ931BuffMode,
       "acTrunkISDNCommonBRILayer2Mode": acTrunkISDNCommonBRILayer2Mode,
       "acTrunkISDNNfas": acTrunkISDNNfas,
       "acTrunkISDNNfasTable": acTrunkISDNNfasTable,
       "acTrunkISDNNfasEntry": acTrunkISDNNfasEntry,
       "acTrunkISDNNfasDchConfig": acTrunkISDNNfasDchConfig,
       "acTrunkISDNNfasInterfaceId": acTrunkISDNNfasInterfaceId,
       "acTrunkISDNNfasGroupNumber": acTrunkISDNNfasGroupNumber,
       "acTrunkISDNDpnss": acTrunkISDNDpnss,
       "acTrunkISDNDpnssTable": acTrunkISDNDpnssTable,
       "acTrunkISDNDpnssEntry": acTrunkISDNDpnssEntry,
       "acTrunkISDNDpnssBehavior": acTrunkISDNDpnssBehavior,
       "acTrunkISDNDpnssNumRealChannels": acTrunkISDNDpnssNumRealChannels,
       "acTrunkISDNDpnssNumVirtualChannels": acTrunkISDNDpnssNumVirtualChannels,
       "acTrunkCAS": acTrunkCAS,
       "acTrunkCASTable": acTrunkCASTable,
       "acTrunkCASEntry": acTrunkCASEntry,
       "acTrunkCASTablesIndex": acTrunkCASTablesIndex,
       "acTrunkCASTablePerChannel": acTrunkCASTablePerChannel,
       "acTrunkV5": acTrunkV5,
       "acTrunkV5Table": acTrunkV5Table,
       "acTrunkV5Entry": acTrunkV5Entry,
       "acTrunkV5NumberOfCChannels": acTrunkV5NumberOfCChannels,
       "acTrunkV5ProtocolSide": acTrunkV5ProtocolSide,
       "acTrunkGlobal": acTrunkGlobal,
       "acTrunkGlobalLifeLineType": acTrunkGlobalLifeLineType,
       "acISDNConfig": acISDNConfig,
       "acMiscISDN": acMiscISDN,
       "acMiscISDNQ931RelayMode": acMiscISDNQ931RelayMode,
       "acMiscISDNDuplicateQ931BuffMode": acMiscISDNDuplicateQ931BuffMode,
       "acDS3Config": acDS3Config,
       "acDS3ConfigFramingMethod": acDS3ConfigFramingMethod,
       "acDS3ConfigClockSource": acDS3ConfigClockSource,
       "acDS3ConfigLineBuiltOut": acDS3ConfigLineBuiltOut,
       "acCasConfig": acCasConfig,
       "acCasConfigEnable": acCasConfigEnable,
       "acCASFile": acCASFile,
       "acCASFileTable": acCASFileTable,
       "acCASFileEntry": acCASFileEntry,
       "acCASFileIndex": acCASFileIndex,
       "acCASFileName": acCASFileName,
       "acSonetSDH": acSonetSDH,
       "acSonetSDHTable": acSonetSDHTable,
       "acSonetSDHEntry": acSonetSDHEntry,
       "acSonetSDHIndex": acSonetSDHIndex,
       "acSonetSDHFbrGrpMappingType": acSonetSDHFbrGrpMappingType,
       "acSonetSDHFbrGrpKlmNumberingScheme": acSonetSDHFbrGrpKlmNumberingScheme,
       "acSonetSDHFbrGrpAPSDirectionMode": acSonetSDHFbrGrpAPSDirectionMode,
       "acSonetSDHFbrGrpAPSRevertMode": acSonetSDHFbrGrpAPSRevertMode,
       "acSonetSDHFbrGrpAPSWaitToRestoreTime": acSonetSDHFbrGrpAPSWaitToRestoreTime,
       "acPSTNStatus": acPSTNStatus,
       "acTrunkStatus": acTrunkStatus,
       "acTrunkStatusTable": acTrunkStatusTable,
       "acTrunkStatusEntry": acTrunkStatusEntry,
       "acTrunkStatusLedStatusColor": acTrunkStatusLedStatusColor,
       "acTrunkStatusLedStatusState": acTrunkStatusLedStatusState,
       "acTrunkStatusChannels": acTrunkStatusChannels,
       "acTrunkStatusV5InterfaceNum": acTrunkStatusV5InterfaceNum,
       "acTrunkStatusV5LinkID": acTrunkStatusV5LinkID,
       "acTrunkStatusDChannel": acTrunkStatusDChannel,
       "acTrunkStatusAlarm": acTrunkStatusAlarm,
       "acDigitalLegs": acDigitalLegs,
       "acDigitalLegsTable": acDigitalLegsTable,
       "acDigitalLegsEntry": acDigitalLegsEntry,
       "acDigitalLegsLegIndex": acDigitalLegsLegIndex,
       "acDigitalLegsCallIndex": acDigitalLegsCallIndex,
       "acDigitalLegsTrunk": acDigitalLegsTrunk,
       "acDigitalLegsBchannel": acDigitalLegsBchannel,
       "acDigitalLegsEchoCanceller": acDigitalLegsEchoCanceller,
       "acDigitalLegsDTMFDetection": acDigitalLegsDTMFDetection,
       "acDigitalLegsVoiceVolume": acDigitalLegsVoiceVolume,
       "acDigitalLegsHighPassFilter": acDigitalLegsHighPassFilter,
       "acDigitalLegsInputGain": acDigitalLegsInputGain,
       "acDigitalLegsDSPDevice": acDigitalLegsDSPDevice,
       "acDigitalLegsLegName": acDigitalLegsLegName,
       "acSDHKLMNumberingScheme": acSDHKLMNumberingScheme,
       "acSDHKLMNumberingSchemeTable": acSDHKLMNumberingSchemeTable,
       "acSDHKLMNumberingSchemeEntry": acSDHKLMNumberingSchemeEntry,
       "acSDHKLMNumberingSchemeTrunkIndex": acSDHKLMNumberingSchemeTrunkIndex,
       "acSDHKLMNumberingSchemeTUG3OrSTS1": acSDHKLMNumberingSchemeTUG3OrSTS1,
       "acSDHKLMNumberingSchemeTUG2OrVTG": acSDHKLMNumberingSchemeTUG2OrVTG,
       "acSDHKLMNumberingSchemeTU12OrVT15": acSDHKLMNumberingSchemeTU12OrVT15,
       "acFiberGroupStatus": acFiberGroupStatus,
       "acFiberGroupStatusActiveLink": acFiberGroupStatusActiveLink}
)
