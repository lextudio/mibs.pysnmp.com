# SNMP MIB module (PAIRGAIN-DSLAM-ALARM-SEVERITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-DSLAM-ALARM-SEVERITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:19 2024
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

(pgDSLAMAlarm,
 pgDSLAMAlarmSeverity) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgDSLAMAlarm",
    "pgDSLAMAlarmSeverity")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pgdsalsvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1)
)


# Types definitions



class PgDSLAMAlarmSeverity(Integer32):
    """Custom type PgDSLAMAlarmSeverity based on Integer32"""
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
          ("disable", 1),
          ("major", 3),
          ("minor", 2))
    )





class PgDSLAMAlarmStatus(Integer32):
    """Custom type PgDSLAMAlarmStatus based on Integer32"""
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
        *(("alarm", 5),
          ("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("noalarm", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext_Object = MibScalar
pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext = _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 7),
    _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext_Type()
)
pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext.setStatus("current")
_PgDSLAMHDSLSpanAlarmThresholdConfProfileTable_Object = MibTable
pgDSLAMHDSLSpanAlarmThresholdConfProfileTable = _PgDSLAMHDSLSpanAlarmThresholdConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8)
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmThresholdConfProfileTable.setStatus("current")
_PgDSLAMHDSLSpanAlarmThresholdConfProfileEntry_Object = MibTableRow
pgDSLAMHDSLSpanAlarmThresholdConfProfileEntry = _PgDSLAMHDSLSpanAlarmThresholdConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1)
)
pgDSLAMHDSLSpanAlarmThresholdConfProfileEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-ALARM-SEVERITY-MIB", "pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex"),
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmThresholdConfProfileEntry.setStatus("current")


class _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndex_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanAlarmThresholdConfProfileIndex_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanAlarmThresholdConfProfileIndex_Object = MibTableColumn
pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex = _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1, 1),
    _PgDSLAMHDSLSpanAlarmThresholdConfProfileIndex_Type()
)
pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex.setStatus("current")


class _PgDSLAMHDSLSpanMarginThreshold_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanMarginThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanMarginThreshold_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanMarginThreshold_Object = MibTableColumn
pgDSLAMHDSLSpanMarginThreshold = _PgDSLAMHDSLSpanMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1, 2),
    _PgDSLAMHDSLSpanMarginThreshold_Type()
)
pgDSLAMHDSLSpanMarginThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanMarginThreshold.setStatus("current")


class _PgDSLAMHDSLSpanESThreshold_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanESThreshold_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanESThreshold_Object = MibTableColumn
pgDSLAMHDSLSpanESThreshold = _PgDSLAMHDSLSpanESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1, 3),
    _PgDSLAMHDSLSpanESThreshold_Type()
)
pgDSLAMHDSLSpanESThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanESThreshold.setStatus("current")


class _PgDSLAMHDSLSpanUASThreshold_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanUASThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanUASThreshold_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanUASThreshold_Object = MibTableColumn
pgDSLAMHDSLSpanUASThreshold = _PgDSLAMHDSLSpanUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1, 4),
    _PgDSLAMHDSLSpanUASThreshold_Type()
)
pgDSLAMHDSLSpanUASThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanUASThreshold.setStatus("current")
_PgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus_Type = RowStatus
_PgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus_Object = MibTableColumn
pgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus = _PgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 8, 1, 5),
    _PgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus_Type()
)
pgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus.setStatus("current")


class _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext_Object = MibScalar
pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext = _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 9),
    _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext_Type()
)
pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext.setStatus("current")
_PgDSLAMHDSLSpanAlarmSeverityConfProfileTable_Object = MibTable
pgDSLAMHDSLSpanAlarmSeverityConfProfileTable = _PgDSLAMHDSLSpanAlarmSeverityConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10)
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmSeverityConfProfileTable.setStatus("current")
_PgDSLAMHDSLSpanAlarmSeverityConfProfileEntry_Object = MibTableRow
pgDSLAMHDSLSpanAlarmSeverityConfProfileEntry = _PgDSLAMHDSLSpanAlarmSeverityConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1)
)
pgDSLAMHDSLSpanAlarmSeverityConfProfileEntry.setIndexNames(
    (0, "PAIRGAIN-DSLAM-ALARM-SEVERITY-MIB", "pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex"),
)
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmSeverityConfProfileEntry.setStatus("current")


class _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndex_Type(Integer32):
    """Custom type pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgDSLAMHDSLSpanAlarmSeverityConfProfileIndex_Type.__name__ = "Integer32"
_PgDSLAMHDSLSpanAlarmSeverityConfProfileIndex_Object = MibTableColumn
pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex = _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 1),
    _PgDSLAMHDSLSpanAlarmSeverityConfProfileIndex_Type()
)
pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex.setStatus("current")
_PgDSLAMHDSLSpanLOSWAlarmSetting_Type = PgDSLAMAlarmSeverity
_PgDSLAMHDSLSpanLOSWAlarmSetting_Object = MibTableColumn
pgDSLAMHDSLSpanLOSWAlarmSetting = _PgDSLAMHDSLSpanLOSWAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 2),
    _PgDSLAMHDSLSpanLOSWAlarmSetting_Type()
)
pgDSLAMHDSLSpanLOSWAlarmSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanLOSWAlarmSetting.setStatus("current")
_PgDSLAMHDSLSpanMarginAlarmSetting_Type = PgDSLAMAlarmSeverity
_PgDSLAMHDSLSpanMarginAlarmSetting_Object = MibTableColumn
pgDSLAMHDSLSpanMarginAlarmSetting = _PgDSLAMHDSLSpanMarginAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 3),
    _PgDSLAMHDSLSpanMarginAlarmSetting_Type()
)
pgDSLAMHDSLSpanMarginAlarmSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanMarginAlarmSetting.setStatus("current")
_PgDSLAMHDSLSpanESAlarmSetting_Type = PgDSLAMAlarmSeverity
_PgDSLAMHDSLSpanESAlarmSetting_Object = MibTableColumn
pgDSLAMHDSLSpanESAlarmSetting = _PgDSLAMHDSLSpanESAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 4),
    _PgDSLAMHDSLSpanESAlarmSetting_Type()
)
pgDSLAMHDSLSpanESAlarmSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanESAlarmSetting.setStatus("current")
_PgDSLAMHDSLSpanUASAlarmSetting_Type = PgDSLAMAlarmSeverity
_PgDSLAMHDSLSpanUASAlarmSetting_Object = MibTableColumn
pgDSLAMHDSLSpanUASAlarmSetting = _PgDSLAMHDSLSpanUASAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 5),
    _PgDSLAMHDSLSpanUASAlarmSetting_Type()
)
pgDSLAMHDSLSpanUASAlarmSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanUASAlarmSetting.setStatus("current")
_PgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus_Type = RowStatus
_PgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus_Object = MibTableColumn
pgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus = _PgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 1, 10, 1, 6),
    _PgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus_Type()
)
pgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus.setStatus("current")
_PgDSLAMChassisAlarmSeverity_ObjectIdentity = ObjectIdentity
pgDSLAMChassisAlarmSeverity = _PgDSLAMChassisAlarmSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 2)
)
_PgDSLAMChassisPsAlarmSeverity_Type = PgDSLAMAlarmSeverity
_PgDSLAMChassisPsAlarmSeverity_Object = MibScalar
pgDSLAMChassisPsAlarmSeverity = _PgDSLAMChassisPsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 2, 1),
    _PgDSLAMChassisPsAlarmSeverity_Type()
)
pgDSLAMChassisPsAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMChassisPsAlarmSeverity.setStatus("current")
_PgDSLAMChassisFanAlarmSeverity_Type = PgDSLAMAlarmSeverity
_PgDSLAMChassisFanAlarmSeverity_Object = MibScalar
pgDSLAMChassisFanAlarmSeverity = _PgDSLAMChassisFanAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 2, 2),
    _PgDSLAMChassisFanAlarmSeverity_Type()
)
pgDSLAMChassisFanAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMChassisFanAlarmSeverity.setStatus("current")
_PgDSLAMChassisConfigChangeAlarmSeverity_Type = PgDSLAMAlarmSeverity
_PgDSLAMChassisConfigChangeAlarmSeverity_Object = MibScalar
pgDSLAMChassisConfigChangeAlarmSeverity = _PgDSLAMChassisConfigChangeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 2, 3),
    _PgDSLAMChassisConfigChangeAlarmSeverity_Type()
)
pgDSLAMChassisConfigChangeAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMChassisConfigChangeAlarmSeverity.setStatus("current")
_PgDSLAMChassisTempAlarmSeverity_Type = PgDSLAMAlarmSeverity
_PgDSLAMChassisTempAlarmSeverity_Object = MibScalar
pgDSLAMChassisTempAlarmSeverity = _PgDSLAMChassisTempAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3, 2, 4),
    _PgDSLAMChassisTempAlarmSeverity_Type()
)
pgDSLAMChassisTempAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgDSLAMChassisTempAlarmSeverity.setStatus("current")
_PgDSLAMADSLAtucAlarmTable_Object = MibTable
pgDSLAMADSLAtucAlarmTable = _PgDSLAMADSLAtucAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucAlarmTable.setStatus("current")
_PgDSLAMADSLAtucAlarmEntry_Object = MibTableRow
pgDSLAMADSLAtucAlarmEntry = _PgDSLAMADSLAtucAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1)
)
pgDSLAMADSLAtucAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucAlarmEntry.setStatus("current")
_PgDSLAMADSLAtucLofAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucLofAlarm_Object = MibTableColumn
pgDSLAMADSLAtucLofAlarm = _PgDSLAMADSLAtucLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 1),
    _PgDSLAMADSLAtucLofAlarm_Type()
)
pgDSLAMADSLAtucLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucLofAlarm.setStatus("current")
_PgDSLAMADSLAtucLosAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucLosAlarm_Object = MibTableColumn
pgDSLAMADSLAtucLosAlarm = _PgDSLAMADSLAtucLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 2),
    _PgDSLAMADSLAtucLosAlarm_Type()
)
pgDSLAMADSLAtucLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucLosAlarm.setStatus("current")
_PgDSLAMADSLAtucLprAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucLprAlarm_Object = MibTableColumn
pgDSLAMADSLAtucLprAlarm = _PgDSLAMADSLAtucLprAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 3),
    _PgDSLAMADSLAtucLprAlarm_Type()
)
pgDSLAMADSLAtucLprAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucLprAlarm.setStatus("current")
_PgDSLAMADSLAtucESAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucESAlarm_Object = MibTableColumn
pgDSLAMADSLAtucESAlarm = _PgDSLAMADSLAtucESAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 4),
    _PgDSLAMADSLAtucESAlarm_Type()
)
pgDSLAMADSLAtucESAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucESAlarm.setStatus("current")
_PgDSLAMADSLAtucRateChangeAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucRateChangeAlarm_Object = MibTableColumn
pgDSLAMADSLAtucRateChangeAlarm = _PgDSLAMADSLAtucRateChangeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 5),
    _PgDSLAMADSLAtucRateChangeAlarm_Type()
)
pgDSLAMADSLAtucRateChangeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucRateChangeAlarm.setStatus("current")
_PgDSLAMADSLAtucInitFailureAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAtucInitFailureAlarm_Object = MibTableColumn
pgDSLAMADSLAtucInitFailureAlarm = _PgDSLAMADSLAtucInitFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 1, 1, 6),
    _PgDSLAMADSLAtucInitFailureAlarm_Type()
)
pgDSLAMADSLAtucInitFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAtucInitFailureAlarm.setStatus("current")
_PgDSLAMADSLAturAlarmTable_Object = MibTable
pgDSLAMADSLAturAlarmTable = _PgDSLAMADSLAturAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pgDSLAMADSLAturAlarmTable.setStatus("current")
_PgDSLAMADSLAturAlarmEntry_Object = MibTableRow
pgDSLAMADSLAturAlarmEntry = _PgDSLAMADSLAturAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1)
)
pgDSLAMADSLAturAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgDSLAMADSLAturAlarmEntry.setStatus("current")
_PgDSLAMADSLAturLofAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturLofAlarm_Object = MibTableColumn
pgDSLAMADSLAturLofAlarm = _PgDSLAMADSLAturLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 1),
    _PgDSLAMADSLAturLofAlarm_Type()
)
pgDSLAMADSLAturLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturLofAlarm.setStatus("current")
_PgDSLAMADSLAturLosAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturLosAlarm_Object = MibTableColumn
pgDSLAMADSLAturLosAlarm = _PgDSLAMADSLAturLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 2),
    _PgDSLAMADSLAturLosAlarm_Type()
)
pgDSLAMADSLAturLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturLosAlarm.setStatus("current")
_PgDSLAMADSLAturLprAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturLprAlarm_Object = MibTableColumn
pgDSLAMADSLAturLprAlarm = _PgDSLAMADSLAturLprAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 3),
    _PgDSLAMADSLAturLprAlarm_Type()
)
pgDSLAMADSLAturLprAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturLprAlarm.setStatus("current")
_PgDSLAMADSLAturESAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturESAlarm_Object = MibTableColumn
pgDSLAMADSLAturESAlarm = _PgDSLAMADSLAturESAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 4),
    _PgDSLAMADSLAturESAlarm_Type()
)
pgDSLAMADSLAturESAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturESAlarm.setStatus("current")
_PgDSLAMADSLAturRateChangeAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturRateChangeAlarm_Object = MibTableColumn
pgDSLAMADSLAturRateChangeAlarm = _PgDSLAMADSLAturRateChangeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 5),
    _PgDSLAMADSLAturRateChangeAlarm_Type()
)
pgDSLAMADSLAturRateChangeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturRateChangeAlarm.setStatus("current")
_PgDSLAMADSLAturInitFailureAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMADSLAturInitFailureAlarm_Object = MibTableColumn
pgDSLAMADSLAturInitFailureAlarm = _PgDSLAMADSLAturInitFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 2, 1, 6),
    _PgDSLAMADSLAturInitFailureAlarm_Type()
)
pgDSLAMADSLAturInitFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMADSLAturInitFailureAlarm.setStatus("current")
_PgDSLAMChassisAlarmTable_Object = MibTable
pgDSLAMChassisAlarmTable = _PgDSLAMChassisAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3)
)
if mibBuilder.loadTexts:
    pgDSLAMChassisAlarmTable.setStatus("current")
_PgDSLAMChassisAlarmEntry_Object = MibTableRow
pgDSLAMChassisAlarmEntry = _PgDSLAMChassisAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1)
)
pgDSLAMChassisAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgDSLAMChassisAlarmEntry.setStatus("current")
_PgDSLAMPSFailureAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMPSFailureAlarm_Object = MibTableColumn
pgDSLAMPSFailureAlarm = _PgDSLAMPSFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 1),
    _PgDSLAMPSFailureAlarm_Type()
)
pgDSLAMPSFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMPSFailureAlarm.setStatus("current")
_PgDSLAMFanFailureAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMFanFailureAlarm_Object = MibTableColumn
pgDSLAMFanFailureAlarm = _PgDSLAMFanFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 2),
    _PgDSLAMFanFailureAlarm_Type()
)
pgDSLAMFanFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMFanFailureAlarm.setStatus("current")
_PgDSLAMConfigChangeAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMConfigChangeAlarm_Object = MibTableColumn
pgDSLAMConfigChangeAlarm = _PgDSLAMConfigChangeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 3),
    _PgDSLAMConfigChangeAlarm_Type()
)
pgDSLAMConfigChangeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMConfigChangeAlarm.setStatus("current")
_PgDSLAMTempExceedThreshAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMTempExceedThreshAlarm_Object = MibTableColumn
pgDSLAMTempExceedThreshAlarm = _PgDSLAMTempExceedThreshAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 4),
    _PgDSLAMTempExceedThreshAlarm_Type()
)
pgDSLAMTempExceedThreshAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMTempExceedThreshAlarm.setStatus("current")
_PgDSLAMLineCardDownAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMLineCardDownAlarm_Object = MibTableColumn
pgDSLAMLineCardDownAlarm = _PgDSLAMLineCardDownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 5),
    _PgDSLAMLineCardDownAlarm_Type()
)
pgDSLAMLineCardDownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMLineCardDownAlarm.setStatus("current")
_PgDSLAMCellBusDownAlarm_Type = PgDSLAMAlarmStatus
_PgDSLAMCellBusDownAlarm_Object = MibTableColumn
pgDSLAMCellBusDownAlarm = _PgDSLAMCellBusDownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4, 3, 1, 6),
    _PgDSLAMCellBusDownAlarm_Type()
)
pgDSLAMCellBusDownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMCellBusDownAlarm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-DSLAM-ALARM-SEVERITY-MIB",
    **{"PgDSLAMAlarmSeverity": PgDSLAMAlarmSeverity,
       "PgDSLAMAlarmStatus": PgDSLAMAlarmStatus,
       "pgdsalsvMIB": pgdsalsvMIB,
       "pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext": pgDSLAMHDSLSpanAlarmThresholdConfProfileIndexNext,
       "pgDSLAMHDSLSpanAlarmThresholdConfProfileTable": pgDSLAMHDSLSpanAlarmThresholdConfProfileTable,
       "pgDSLAMHDSLSpanAlarmThresholdConfProfileEntry": pgDSLAMHDSLSpanAlarmThresholdConfProfileEntry,
       "pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex": pgDSLAMHDSLSpanAlarmThresholdConfProfileIndex,
       "pgDSLAMHDSLSpanMarginThreshold": pgDSLAMHDSLSpanMarginThreshold,
       "pgDSLAMHDSLSpanESThreshold": pgDSLAMHDSLSpanESThreshold,
       "pgDSLAMHDSLSpanUASThreshold": pgDSLAMHDSLSpanUASThreshold,
       "pgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus": pgDSLAMHDSLSpanAlarmThresholdConfProfileRowStatus,
       "pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext": pgDSLAMHDSLSpanAlarmSeverityConfProfileIndexNext,
       "pgDSLAMHDSLSpanAlarmSeverityConfProfileTable": pgDSLAMHDSLSpanAlarmSeverityConfProfileTable,
       "pgDSLAMHDSLSpanAlarmSeverityConfProfileEntry": pgDSLAMHDSLSpanAlarmSeverityConfProfileEntry,
       "pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex": pgDSLAMHDSLSpanAlarmSeverityConfProfileIndex,
       "pgDSLAMHDSLSpanLOSWAlarmSetting": pgDSLAMHDSLSpanLOSWAlarmSetting,
       "pgDSLAMHDSLSpanMarginAlarmSetting": pgDSLAMHDSLSpanMarginAlarmSetting,
       "pgDSLAMHDSLSpanESAlarmSetting": pgDSLAMHDSLSpanESAlarmSetting,
       "pgDSLAMHDSLSpanUASAlarmSetting": pgDSLAMHDSLSpanUASAlarmSetting,
       "pgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus": pgDSLAMHDSLSpanAlarmSeverityConfProfileRowStatus,
       "pgDSLAMChassisAlarmSeverity": pgDSLAMChassisAlarmSeverity,
       "pgDSLAMChassisPsAlarmSeverity": pgDSLAMChassisPsAlarmSeverity,
       "pgDSLAMChassisFanAlarmSeverity": pgDSLAMChassisFanAlarmSeverity,
       "pgDSLAMChassisConfigChangeAlarmSeverity": pgDSLAMChassisConfigChangeAlarmSeverity,
       "pgDSLAMChassisTempAlarmSeverity": pgDSLAMChassisTempAlarmSeverity,
       "pgDSLAMADSLAtucAlarmTable": pgDSLAMADSLAtucAlarmTable,
       "pgDSLAMADSLAtucAlarmEntry": pgDSLAMADSLAtucAlarmEntry,
       "pgDSLAMADSLAtucLofAlarm": pgDSLAMADSLAtucLofAlarm,
       "pgDSLAMADSLAtucLosAlarm": pgDSLAMADSLAtucLosAlarm,
       "pgDSLAMADSLAtucLprAlarm": pgDSLAMADSLAtucLprAlarm,
       "pgDSLAMADSLAtucESAlarm": pgDSLAMADSLAtucESAlarm,
       "pgDSLAMADSLAtucRateChangeAlarm": pgDSLAMADSLAtucRateChangeAlarm,
       "pgDSLAMADSLAtucInitFailureAlarm": pgDSLAMADSLAtucInitFailureAlarm,
       "pgDSLAMADSLAturAlarmTable": pgDSLAMADSLAturAlarmTable,
       "pgDSLAMADSLAturAlarmEntry": pgDSLAMADSLAturAlarmEntry,
       "pgDSLAMADSLAturLofAlarm": pgDSLAMADSLAturLofAlarm,
       "pgDSLAMADSLAturLosAlarm": pgDSLAMADSLAturLosAlarm,
       "pgDSLAMADSLAturLprAlarm": pgDSLAMADSLAturLprAlarm,
       "pgDSLAMADSLAturESAlarm": pgDSLAMADSLAturESAlarm,
       "pgDSLAMADSLAturRateChangeAlarm": pgDSLAMADSLAturRateChangeAlarm,
       "pgDSLAMADSLAturInitFailureAlarm": pgDSLAMADSLAturInitFailureAlarm,
       "pgDSLAMChassisAlarmTable": pgDSLAMChassisAlarmTable,
       "pgDSLAMChassisAlarmEntry": pgDSLAMChassisAlarmEntry,
       "pgDSLAMPSFailureAlarm": pgDSLAMPSFailureAlarm,
       "pgDSLAMFanFailureAlarm": pgDSLAMFanFailureAlarm,
       "pgDSLAMConfigChangeAlarm": pgDSLAMConfigChangeAlarm,
       "pgDSLAMTempExceedThreshAlarm": pgDSLAMTempExceedThreshAlarm,
       "pgDSLAMLineCardDownAlarm": pgDSLAMLineCardDownAlarm,
       "pgDSLAMCellBusDownAlarm": pgDSLAMCellBusDownAlarm}
)
