# SNMP MIB module (PAIRGAIN-DSLAM-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-DSLAM-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:15 2024
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

(pgDSLAMChassis,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgDSLAMChassis")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PgDSLAMChassisType(Integer32):
    """Custom type PgDSLAMChassisType based on Integer32"""
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
        *(("dslam-as3", 4),
          ("dslam-as5", 3),
          ("dslam-co", 2),
          ("unknown", 1))
    )





class PgDSLAMUnitType(Integer32):
    """Custom type PgDSLAMUnitType based on Integer32"""
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
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("adsl-cap-cell-12", 11),
          ("adsl-cap-cell-8", 9),
          ("adsl-cap-cell-test", 34),
          ("adsl-cap-frame-12", 5),
          ("adsl-cap-frame-8", 3),
          ("adsl-cap-frame-test", 31),
          ("adsl-dmt-cell-12", 12),
          ("adsl-dmt-cell-8", 10),
          ("adsl-dmt-cell-test", 35),
          ("adsl-dmt-frame-12", 6),
          ("adsl-dmt-frame-8", 4),
          ("adsl-dmt-frame-test", 32),
          ("atm-oc12-line", 29),
          ("atm-oc3-channel", 40),
          ("atm-oc3-channel-6", 13),
          ("atm-oc3-line", 19),
          ("cell-line-test", 39),
          ("circuit-emul-test", 37),
          ("ds3-atm-channel", 45),
          ("ds3-atm-line", 20),
          ("ds3-circuit-emul-6", 16),
          ("ds3-fr-line", 22),
          ("e1-atm-imux-6", 26),
          ("e1-atm-imux-8-channel", 42),
          ("e1-atm-imux-8-line", 51),
          ("e1-circuit-emul-12", 15),
          ("e1-fr-imux-6", 28),
          ("e3-atm-line", 21),
          ("e3-circuit-emul-6", 17),
          ("e3-fr-line", 23),
          ("ethernet-10-100", 24),
          ("fr-line-test", 38),
          ("hdsl-frame-16", 7),
          ("hdsl-frame-24", 8),
          ("hissi-line", 30),
          ("idsl-frame-24", 46),
          ("management", 2),
          ("pot-splitter", 53),
          ("sdsl-cell-24", 47),
          ("sdsl-cell-test", 36),
          ("sdsl-frame-16", 43),
          ("sdsl-frame-24", 44),
          ("sdsl-frame-test", 33),
          ("t1-atm-imux-6", 25),
          ("t1-circuit-emul-12", 14),
          ("t1-dsx1-channel", 41),
          ("t1-dsx1-line", 50),
          ("t1-dsx1-linemgmt", 52),
          ("t1-fr-imux-6", 27),
          ("t1-higain-lu-12", 18),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



class TimeSeconds(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_PgDSLAMChassisType_Type = PgDSLAMChassisType
_PgDSLAMChassisType_Object = MibScalar
pgDSLAMChassisType = _PgDSLAMChassisType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 1),
    _PgDSLAMChassisType_Type()
)
pgDSLAMChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMChassisType.setStatus("mandatory")


class _PgDSLAMChassisPsStatus_Type(Integer32):
    """Custom type pgDSLAMChassisPsStatus based on Integer32"""
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
        *(("bothFail", 3),
          ("ok", 4),
          ("oneFail", 2),
          ("other", 1))
    )


_PgDSLAMChassisPsStatus_Type.__name__ = "Integer32"
_PgDSLAMChassisPsStatus_Object = MibScalar
pgDSLAMChassisPsStatus = _PgDSLAMChassisPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 2),
    _PgDSLAMChassisPsStatus_Type()
)
pgDSLAMChassisPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMChassisPsStatus.setStatus("mandatory")


class _PgDSLAMChassisFanStatus_Type(Integer32):
    """Custom type pgDSLAMChassisFanStatus based on Integer32"""
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
        *(("fail", 2),
          ("hightemp", 4),
          ("ok", 3),
          ("other", 1))
    )


_PgDSLAMChassisFanStatus_Type.__name__ = "Integer32"
_PgDSLAMChassisFanStatus_Object = MibScalar
pgDSLAMChassisFanStatus = _PgDSLAMChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 3),
    _PgDSLAMChassisFanStatus_Type()
)
pgDSLAMChassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMChassisFanStatus.setStatus("mandatory")
_PgDSLAMSlotConfigTable_Object = MibTable
pgDSLAMSlotConfigTable = _PgDSLAMSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    pgDSLAMSlotConfigTable.setStatus("mandatory")
_PgDSLAMSlotConfigEntry_Object = MibTableRow
pgDSLAMSlotConfigEntry = _PgDSLAMSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1)
)
pgDSLAMSlotConfigEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMSlotNumber"),
)
if mibBuilder.loadTexts:
    pgDSLAMSlotConfigEntry.setStatus("mandatory")


class _PgDSLAMSlotNumber_Type(Integer32):
    """Custom type pgDSLAMSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PgDSLAMSlotNumber_Type.__name__ = "Integer32"
_PgDSLAMSlotNumber_Object = MibTableColumn
pgDSLAMSlotNumber = _PgDSLAMSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 1),
    _PgDSLAMSlotNumber_Type()
)
pgDSLAMSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotNumber.setStatus("mandatory")
_PgDSLAMSlotUnitType_Type = PgDSLAMUnitType
_PgDSLAMSlotUnitType_Object = MibTableColumn
pgDSLAMSlotUnitType = _PgDSLAMSlotUnitType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 2),
    _PgDSLAMSlotUnitType_Type()
)
pgDSLAMSlotUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotUnitType.setStatus("mandatory")


class _PgDSLAMSlotUnitSerialNo_Type(DisplayString):
    """Custom type pgDSLAMSlotUnitSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_PgDSLAMSlotUnitSerialNo_Type.__name__ = "DisplayString"
_PgDSLAMSlotUnitSerialNo_Object = MibTableColumn
pgDSLAMSlotUnitSerialNo = _PgDSLAMSlotUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 3),
    _PgDSLAMSlotUnitSerialNo_Type()
)
pgDSLAMSlotUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotUnitSerialNo.setStatus("mandatory")


class _PgDSLAMSlotUnitDescr_Type(DisplayString):
    """Custom type pgDSLAMSlotUnitDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PgDSLAMSlotUnitDescr_Type.__name__ = "DisplayString"
_PgDSLAMSlotUnitDescr_Object = MibTableColumn
pgDSLAMSlotUnitDescr = _PgDSLAMSlotUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 4),
    _PgDSLAMSlotUnitDescr_Type()
)
pgDSLAMSlotUnitDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMSlotUnitDescr.setStatus("mandatory")


class _PgDSLAMSlotHwVer_Type(DisplayString):
    """Custom type pgDSLAMSlotHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_PgDSLAMSlotHwVer_Type.__name__ = "DisplayString"
_PgDSLAMSlotHwVer_Object = MibTableColumn
pgDSLAMSlotHwVer = _PgDSLAMSlotHwVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 5),
    _PgDSLAMSlotHwVer_Type()
)
pgDSLAMSlotHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotHwVer.setStatus("mandatory")


class _PgDSLAMSlotFwVer_Type(DisplayString):
    """Custom type pgDSLAMSlotFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_PgDSLAMSlotFwVer_Type.__name__ = "DisplayString"
_PgDSLAMSlotFwVer_Object = MibTableColumn
pgDSLAMSlotFwVer = _PgDSLAMSlotFwVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 6),
    _PgDSLAMSlotFwVer_Type()
)
pgDSLAMSlotFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotFwVer.setStatus("mandatory")


class _PgDSLAMSlotSwVer_Type(DisplayString):
    """Custom type pgDSLAMSlotSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_PgDSLAMSlotSwVer_Type.__name__ = "DisplayString"
_PgDSLAMSlotSwVer_Object = MibTableColumn
pgDSLAMSlotSwVer = _PgDSLAMSlotSwVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 7),
    _PgDSLAMSlotSwVer_Type()
)
pgDSLAMSlotSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotSwVer.setStatus("mandatory")


class _PgDSLAMSlotBoardReset_Type(Integer32):
    """Custom type pgDSLAMSlotBoardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_PgDSLAMSlotBoardReset_Type.__name__ = "Integer32"
_PgDSLAMSlotBoardReset_Object = MibTableColumn
pgDSLAMSlotBoardReset = _PgDSLAMSlotBoardReset_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 8),
    _PgDSLAMSlotBoardReset_Type()
)
pgDSLAMSlotBoardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMSlotBoardReset.setStatus("mandatory")


class _PgDSLAMSlotNmCntlStatus_Type(Integer32):
    """Custom type pgDSLAMSlotNmCntlStatus based on Integer32"""
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
        *(("nmControl", 2),
          ("notNmControl", 4),
          ("other", 1),
          ("testControl", 3))
    )


_PgDSLAMSlotNmCntlStatus_Type.__name__ = "Integer32"
_PgDSLAMSlotNmCntlStatus_Object = MibTableColumn
pgDSLAMSlotNmCntlStatus = _PgDSLAMSlotNmCntlStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 9),
    _PgDSLAMSlotNmCntlStatus_Type()
)
pgDSLAMSlotNmCntlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotNmCntlStatus.setStatus("mandatory")
_PgDSLAMSlotIfNumber_Type = Integer32
_PgDSLAMSlotIfNumber_Object = MibTableColumn
pgDSLAMSlotIfNumber = _PgDSLAMSlotIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 10),
    _PgDSLAMSlotIfNumber_Type()
)
pgDSLAMSlotIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotIfNumber.setStatus("mandatory")


class _PgDSLAMSlotHwID_Type(DisplayString):
    """Custom type pgDSLAMSlotHwID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_PgDSLAMSlotHwID_Type.__name__ = "DisplayString"
_PgDSLAMSlotHwID_Object = MibTableColumn
pgDSLAMSlotHwID = _PgDSLAMSlotHwID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 4, 1, 11),
    _PgDSLAMSlotHwID_Type()
)
pgDSLAMSlotHwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotHwID.setStatus("mandatory")
_PgDSLAMConfigChangeCnts_Type = Counter32
_PgDSLAMConfigChangeCnts_Object = MibScalar
pgDSLAMConfigChangeCnts = _PgDSLAMConfigChangeCnts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 5),
    _PgDSLAMConfigChangeCnts_Type()
)
pgDSLAMConfigChangeCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMConfigChangeCnts.setStatus("mandatory")
_PgDSLAMConfigLastChange_Type = TimeTicks
_PgDSLAMConfigLastChange_Object = MibScalar
pgDSLAMConfigLastChange = _PgDSLAMConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 6),
    _PgDSLAMConfigLastChange_Type()
)
pgDSLAMConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMConfigLastChange.setStatus("mandatory")
_PgDSLAMChassisAlarmStatTable_Object = MibTable
pgDSLAMChassisAlarmStatTable = _PgDSLAMChassisAlarmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7)
)
if mibBuilder.loadTexts:
    pgDSLAMChassisAlarmStatTable.setStatus("mandatory")
_DslamAlarmStatEntry_Object = MibTableRow
dslamAlarmStatEntry = _DslamAlarmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7, 1)
)
dslamAlarmStatEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMAlarmCardID"),
)
if mibBuilder.loadTexts:
    dslamAlarmStatEntry.setStatus("mandatory")


class _PgDSLAMAlarmCardID_Type(Integer32):
    """Custom type pgDSLAMAlarmCardID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PgDSLAMAlarmCardID_Type.__name__ = "Integer32"
_PgDSLAMAlarmCardID_Object = MibTableColumn
pgDSLAMAlarmCardID = _PgDSLAMAlarmCardID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7, 1, 1),
    _PgDSLAMAlarmCardID_Type()
)
pgDSLAMAlarmCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMAlarmCardID.setStatus("mandatory")


class _PgDSLAMAlarmPortNum_Type(Integer32):
    """Custom type pgDSLAMAlarmPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PgDSLAMAlarmPortNum_Type.__name__ = "Integer32"
_PgDSLAMAlarmPortNum_Object = MibTableColumn
pgDSLAMAlarmPortNum = _PgDSLAMAlarmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7, 1, 2),
    _PgDSLAMAlarmPortNum_Type()
)
pgDSLAMAlarmPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMAlarmPortNum.setStatus("mandatory")


class _PgDSLAMAlarmStatSeverity_Type(Integer32):
    """Custom type pgDSLAMAlarmStatSeverity based on Integer32"""
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("none", 1))
    )


_PgDSLAMAlarmStatSeverity_Type.__name__ = "Integer32"
_PgDSLAMAlarmStatSeverity_Object = MibTableColumn
pgDSLAMAlarmStatSeverity = _PgDSLAMAlarmStatSeverity_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7, 1, 3),
    _PgDSLAMAlarmStatSeverity_Type()
)
pgDSLAMAlarmStatSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMAlarmStatSeverity.setStatus("mandatory")
_PgDSLAMAlarmTrapOID_Type = ObjectIdentifier
_PgDSLAMAlarmTrapOID_Object = MibTableColumn
pgDSLAMAlarmTrapOID = _PgDSLAMAlarmTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 7, 1, 4),
    _PgDSLAMAlarmTrapOID_Type()
)
pgDSLAMAlarmTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMAlarmTrapOID.setStatus("mandatory")


class _PgDSLAMChassisLEDStat_Type(OctetString):
    """Custom type pgDSLAMChassisLEDStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PgDSLAMChassisLEDStat_Type.__name__ = "OctetString"
_PgDSLAMChassisLEDStat_Object = MibScalar
pgDSLAMChassisLEDStat = _PgDSLAMChassisLEDStat_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 8),
    _PgDSLAMChassisLEDStat_Type()
)
pgDSLAMChassisLEDStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMChassisLEDStat.setStatus("mandatory")
_PgDSLAMCalendarTime_Type = Counter32
_PgDSLAMCalendarTime_Object = MibScalar
pgDSLAMCalendarTime = _PgDSLAMCalendarTime_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 9),
    _PgDSLAMCalendarTime_Type()
)
pgDSLAMCalendarTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMCalendarTime.setStatus("mandatory")
_PgDSLAMSlotStatTable_Object = MibTable
pgDSLAMSlotStatTable = _PgDSLAMSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 10)
)
if mibBuilder.loadTexts:
    pgDSLAMSlotStatTable.setStatus("mandatory")
_PgDSLAMSlotStatEntry_Object = MibTableRow
pgDSLAMSlotStatEntry = _PgDSLAMSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 10, 1)
)
pgDSLAMSlotStatEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMSlotID"),
)
if mibBuilder.loadTexts:
    pgDSLAMSlotStatEntry.setStatus("mandatory")


class _PgDSLAMSlotID_Type(Integer32):
    """Custom type pgDSLAMSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PgDSLAMSlotID_Type.__name__ = "Integer32"
_PgDSLAMSlotID_Object = MibTableColumn
pgDSLAMSlotID = _PgDSLAMSlotID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 10, 1, 1),
    _PgDSLAMSlotID_Type()
)
pgDSLAMSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotID.setStatus("mandatory")


class _PgDSLAMSlotStatus_Type(Integer32):
    """Custom type pgDSLAMSlotStatus based on Integer32"""
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
        *(("down", 3),
          ("notPresent", 4),
          ("unknown", 1),
          ("up", 2))
    )


_PgDSLAMSlotStatus_Type.__name__ = "Integer32"
_PgDSLAMSlotStatus_Object = MibTableColumn
pgDSLAMSlotStatus = _PgDSLAMSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 10, 1, 2),
    _PgDSLAMSlotStatus_Type()
)
pgDSLAMSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMSlotStatus.setStatus("mandatory")
_PgDSLAMChassisTemperature_Type = Integer32
_PgDSLAMChassisTemperature_Object = MibScalar
pgDSLAMChassisTemperature = _PgDSLAMChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 11),
    _PgDSLAMChassisTemperature_Type()
)
pgDSLAMChassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMChassisTemperature.setStatus("mandatory")
_PgDSLAMFileDirectoryTable_Object = MibTable
pgDSLAMFileDirectoryTable = _PgDSLAMFileDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 12)
)
if mibBuilder.loadTexts:
    pgDSLAMFileDirectoryTable.setStatus("mandatory")
_PgDSLAMFileDirectoryEntry_Object = MibTableRow
pgDSLAMFileDirectoryEntry = _PgDSLAMFileDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 12, 1)
)
pgDSLAMFileDirectoryEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-CHASSIS-MIB", "pgDSLAMFileDirectorySlotID"),
)
if mibBuilder.loadTexts:
    pgDSLAMFileDirectoryEntry.setStatus("mandatory")


class _PgDSLAMFileDirectorySlotID_Type(Integer32):
    """Custom type pgDSLAMFileDirectorySlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PgDSLAMFileDirectorySlotID_Type.__name__ = "Integer32"
_PgDSLAMFileDirectorySlotID_Object = MibTableColumn
pgDSLAMFileDirectorySlotID = _PgDSLAMFileDirectorySlotID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 12, 1, 1),
    _PgDSLAMFileDirectorySlotID_Type()
)
pgDSLAMFileDirectorySlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMFileDirectorySlotID.setStatus("mandatory")


class _PgDSLAMFileDirectory_Type(OctetString):
    """Custom type pgDSLAMFileDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_PgDSLAMFileDirectory_Type.__name__ = "OctetString"
_PgDSLAMFileDirectory_Object = MibTableColumn
pgDSLAMFileDirectory = _PgDSLAMFileDirectory_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 12, 1, 2),
    _PgDSLAMFileDirectory_Type()
)
pgDSLAMFileDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMFileDirectory.setStatus("mandatory")


class _PgDSLAMFsSlotID_Type(Integer32):
    """Custom type pgDSLAMFsSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_PgDSLAMFsSlotID_Type.__name__ = "Integer32"
_PgDSLAMFsSlotID_Object = MibScalar
pgDSLAMFsSlotID = _PgDSLAMFsSlotID_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 13),
    _PgDSLAMFsSlotID_Type()
)
pgDSLAMFsSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFsSlotID.setStatus("mandatory")


class _PgDSLAMFsFileName_Type(OctetString):
    """Custom type pgDSLAMFsFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PgDSLAMFsFileName_Type.__name__ = "OctetString"
_PgDSLAMFsFileName_Object = MibScalar
pgDSLAMFsFileName = _PgDSLAMFsFileName_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 14),
    _PgDSLAMFsFileName_Type()
)
pgDSLAMFsFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFsFileName.setStatus("mandatory")


class _PgDSLAMFsAction_Type(Integer32):
    """Custom type pgDSLAMFsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("unknown", 1))
    )


_PgDSLAMFsAction_Type.__name__ = "Integer32"
_PgDSLAMFsAction_Object = MibScalar
pgDSLAMFsAction = _PgDSLAMFsAction_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 15),
    _PgDSLAMFsAction_Type()
)
pgDSLAMFsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFsAction.setStatus("mandatory")


class _PgDSLAMCalendarTimeOs_Type(OctetString):
    """Custom type pgDSLAMCalendarTimeOs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_PgDSLAMCalendarTimeOs_Type.__name__ = "OctetString"
_PgDSLAMCalendarTimeOs_Object = MibScalar
pgDSLAMCalendarTimeOs = _PgDSLAMCalendarTimeOs_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 16),
    _PgDSLAMCalendarTimeOs_Type()
)
pgDSLAMCalendarTimeOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMCalendarTimeOs.setStatus("mandatory")


class _PgDSLAMAllSlotLED_Type(OctetString):
    """Custom type pgDSLAMAllSlotLED based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 568),
    )


_PgDSLAMAllSlotLED_Type.__name__ = "OctetString"
_PgDSLAMAllSlotLED_Object = MibScalar
pgDSLAMAllSlotLED = _PgDSLAMAllSlotLED_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1, 17),
    _PgDSLAMAllSlotLED_Type()
)
pgDSLAMAllSlotLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMAllSlotLED.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-DSLAM-CHASSIS-MIB",
    **{"TimeSeconds": TimeSeconds,
       "DisplayString": DisplayString,
       "PgDSLAMChassisType": PgDSLAMChassisType,
       "PgDSLAMUnitType": PgDSLAMUnitType,
       "pgDSLAMChassisType": pgDSLAMChassisType,
       "pgDSLAMChassisPsStatus": pgDSLAMChassisPsStatus,
       "pgDSLAMChassisFanStatus": pgDSLAMChassisFanStatus,
       "pgDSLAMSlotConfigTable": pgDSLAMSlotConfigTable,
       "pgDSLAMSlotConfigEntry": pgDSLAMSlotConfigEntry,
       "pgDSLAMSlotNumber": pgDSLAMSlotNumber,
       "pgDSLAMSlotUnitType": pgDSLAMSlotUnitType,
       "pgDSLAMSlotUnitSerialNo": pgDSLAMSlotUnitSerialNo,
       "pgDSLAMSlotUnitDescr": pgDSLAMSlotUnitDescr,
       "pgDSLAMSlotHwVer": pgDSLAMSlotHwVer,
       "pgDSLAMSlotFwVer": pgDSLAMSlotFwVer,
       "pgDSLAMSlotSwVer": pgDSLAMSlotSwVer,
       "pgDSLAMSlotBoardReset": pgDSLAMSlotBoardReset,
       "pgDSLAMSlotNmCntlStatus": pgDSLAMSlotNmCntlStatus,
       "pgDSLAMSlotIfNumber": pgDSLAMSlotIfNumber,
       "pgDSLAMSlotHwID": pgDSLAMSlotHwID,
       "pgDSLAMConfigChangeCnts": pgDSLAMConfigChangeCnts,
       "pgDSLAMConfigLastChange": pgDSLAMConfigLastChange,
       "pgDSLAMChassisAlarmStatTable": pgDSLAMChassisAlarmStatTable,
       "dslamAlarmStatEntry": dslamAlarmStatEntry,
       "pgDSLAMAlarmCardID": pgDSLAMAlarmCardID,
       "pgDSLAMAlarmPortNum": pgDSLAMAlarmPortNum,
       "pgDSLAMAlarmStatSeverity": pgDSLAMAlarmStatSeverity,
       "pgDSLAMAlarmTrapOID": pgDSLAMAlarmTrapOID,
       "pgDSLAMChassisLEDStat": pgDSLAMChassisLEDStat,
       "pgDSLAMCalendarTime": pgDSLAMCalendarTime,
       "pgDSLAMSlotStatTable": pgDSLAMSlotStatTable,
       "pgDSLAMSlotStatEntry": pgDSLAMSlotStatEntry,
       "pgDSLAMSlotID": pgDSLAMSlotID,
       "pgDSLAMSlotStatus": pgDSLAMSlotStatus,
       "pgDSLAMChassisTemperature": pgDSLAMChassisTemperature,
       "pgDSLAMFileDirectoryTable": pgDSLAMFileDirectoryTable,
       "pgDSLAMFileDirectoryEntry": pgDSLAMFileDirectoryEntry,
       "pgDSLAMFileDirectorySlotID": pgDSLAMFileDirectorySlotID,
       "pgDSLAMFileDirectory": pgDSLAMFileDirectory,
       "pgDSLAMFsSlotID": pgDSLAMFsSlotID,
       "pgDSLAMFsFileName": pgDSLAMFsFileName,
       "pgDSLAMFsAction": pgDSLAMFsAction,
       "pgDSLAMCalendarTimeOs": pgDSLAMCalendarTimeOs,
       "pgDSLAMAllSlotLED": pgDSLAMAllSlotLED}
)
