# SNMP MIB module (CERENT-OPTICAL-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-OPTICAL-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:28 2024
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

(CerentPeriod,) = mibBuilder.importSymbols(
    "CERENT-TC",
    "CerentPeriod")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cerentOpticalMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 70)
)
cerentOpticalMonitorMIB.setRevisions(
        ("1902-11-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OpticalParameterType(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("acPower", 2),
          ("addPower", 11),
          ("apdTemp", 3),
          ("biasCurrent", 5),
          ("gain", 9),
          ("laserTemp", 4),
          ("oscPower", 10),
          ("peltierCurrent", 6),
          ("power", 1),
          ("voa", 8),
          ("xcvrVoltage", 7))
    )



class OpticalParameterValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )



class OpticalIfDirection(Integer32, TextualConvention):
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
        *(("notApplicable", 3),
          ("receive", 1),
          ("transmit", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CerentOpticalMonitorMIBObjects_ObjectIdentity = ObjectIdentity
cerentOpticalMonitorMIBObjects = _CerentOpticalMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30)
)
_CerentOpticalMonGroup_ObjectIdentity = ObjectIdentity
cerentOpticalMonGroup = _CerentOpticalMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1)
)
_COpticalMonTable_Object = MibTable
cOpticalMonTable = _COpticalMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    cOpticalMonTable.setStatus("current")
_COpticalMonEntry_Object = MibTableRow
cOpticalMonEntry = _COpticalMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1)
)
cOpticalMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalMonDirection"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalMonParameterType"),
)
if mibBuilder.loadTexts:
    cOpticalMonEntry.setStatus("current")
_COpticalMonDirection_Type = OpticalIfDirection
_COpticalMonDirection_Object = MibTableColumn
cOpticalMonDirection = _COpticalMonDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 1),
    _COpticalMonDirection_Type()
)
cOpticalMonDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalMonDirection.setStatus("current")
_COpticalMonParameterType_Type = OpticalParameterType
_COpticalMonParameterType_Object = MibTableColumn
cOpticalMonParameterType = _COpticalMonParameterType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 2),
    _COpticalMonParameterType_Type()
)
cOpticalMonParameterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalMonParameterType.setStatus("current")
_COpticalParameterValue_Type = OpticalParameterValue
_COpticalParameterValue_Object = MibTableColumn
cOpticalParameterValue = _COpticalParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 3),
    _COpticalParameterValue_Type()
)
cOpticalParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParameterValue.setStatus("current")
_COpticalParamHighAlarmThresh_Type = OpticalParameterValue
_COpticalParamHighAlarmThresh_Object = MibTableColumn
cOpticalParamHighAlarmThresh = _COpticalParamHighAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 4),
    _COpticalParamHighAlarmThresh_Type()
)
cOpticalParamHighAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighAlarmThresh.setStatus("current")
_COpticalParamHighWarning15MinThresh_Type = OpticalParameterValue
_COpticalParamHighWarning15MinThresh_Object = MibTableColumn
cOpticalParamHighWarning15MinThresh = _COpticalParamHighWarning15MinThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 5),
    _COpticalParamHighWarning15MinThresh_Type()
)
cOpticalParamHighWarning15MinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighWarning15MinThresh.setStatus("current")
_COpticalParamHighWarning1DayThresh_Type = OpticalParameterValue
_COpticalParamHighWarning1DayThresh_Object = MibTableColumn
cOpticalParamHighWarning1DayThresh = _COpticalParamHighWarning1DayThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 6),
    _COpticalParamHighWarning1DayThresh_Type()
)
cOpticalParamHighWarning1DayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighWarning1DayThresh.setStatus("current")
_COpticalParamLowAlarmThresh_Type = OpticalParameterValue
_COpticalParamLowAlarmThresh_Object = MibTableColumn
cOpticalParamLowAlarmThresh = _COpticalParamLowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 7),
    _COpticalParamLowAlarmThresh_Type()
)
cOpticalParamLowAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowAlarmThresh.setStatus("current")
_COpticalParamLowWarning15MinThresh_Type = OpticalParameterValue
_COpticalParamLowWarning15MinThresh_Object = MibTableColumn
cOpticalParamLowWarning15MinThresh = _COpticalParamLowWarning15MinThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 8),
    _COpticalParamLowWarning15MinThresh_Type()
)
cOpticalParamLowWarning15MinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowWarning15MinThresh.setStatus("current")
_COpticalParamLowWarning1DayThresh_Type = OpticalParameterValue
_COpticalParamLowWarning1DayThresh_Object = MibTableColumn
cOpticalParamLowWarning1DayThresh = _COpticalParamLowWarning1DayThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 9),
    _COpticalParamLowWarning1DayThresh_Type()
)
cOpticalParamLowWarning1DayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowWarning1DayThresh.setStatus("current")
_COpticalParamLowDegradeThresh_Type = OpticalParameterValue
_COpticalParamLowDegradeThresh_Object = MibTableColumn
cOpticalParamLowDegradeThresh = _COpticalParamLowDegradeThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 10),
    _COpticalParamLowDegradeThresh_Type()
)
cOpticalParamLowDegradeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowDegradeThresh.setStatus("current")
_COpticalParamHighDegradeThresh_Type = OpticalParameterValue
_COpticalParamHighDegradeThresh_Object = MibTableColumn
cOpticalParamHighDegradeThresh = _COpticalParamHighDegradeThresh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 1, 1, 1, 11),
    _COpticalParamHighDegradeThresh_Type()
)
cOpticalParamHighDegradeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighDegradeThresh.setStatus("current")
_CerentOpticalPMGroup_ObjectIdentity = ObjectIdentity
cerentOpticalPMGroup = _CerentOpticalPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2)
)
_COpticalPMCurrentTable_Object = MibTable
cOpticalPMCurrentTable = _COpticalPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1)
)
if mibBuilder.loadTexts:
    cOpticalPMCurrentTable.setStatus("current")
_COpticalPMCurrentEntry_Object = MibTableRow
cOpticalPMCurrentEntry = _COpticalPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1)
)
cOpticalPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentDirection"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentParamType"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentPeriod"),
)
if mibBuilder.loadTexts:
    cOpticalPMCurrentEntry.setStatus("current")
_COpticalPMCurrentDirection_Type = OpticalIfDirection
_COpticalPMCurrentDirection_Object = MibTableColumn
cOpticalPMCurrentDirection = _COpticalPMCurrentDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 1),
    _COpticalPMCurrentDirection_Type()
)
cOpticalPMCurrentDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentDirection.setStatus("current")
_COpticalPMCurrentParamType_Type = OpticalParameterType
_COpticalPMCurrentParamType_Object = MibTableColumn
cOpticalPMCurrentParamType = _COpticalPMCurrentParamType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 2),
    _COpticalPMCurrentParamType_Type()
)
cOpticalPMCurrentParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentParamType.setStatus("current")
_COpticalPMCurrentPeriod_Type = CerentPeriod
_COpticalPMCurrentPeriod_Object = MibTableColumn
cOpticalPMCurrentPeriod = _COpticalPMCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 3),
    _COpticalPMCurrentPeriod_Type()
)
cOpticalPMCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentPeriod.setStatus("current")
_COpticalPMCurrentMaxParam_Type = OpticalParameterValue
_COpticalPMCurrentMaxParam_Object = MibTableColumn
cOpticalPMCurrentMaxParam = _COpticalPMCurrentMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 4),
    _COpticalPMCurrentMaxParam_Type()
)
cOpticalPMCurrentMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMaxParam.setStatus("current")
_COpticalPMCurrentMinParam_Type = OpticalParameterValue
_COpticalPMCurrentMinParam_Object = MibTableColumn
cOpticalPMCurrentMinParam = _COpticalPMCurrentMinParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 5),
    _COpticalPMCurrentMinParam_Type()
)
cOpticalPMCurrentMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMinParam.setStatus("current")
_COpticalPMCurrentMeanParam_Type = OpticalParameterValue
_COpticalPMCurrentMeanParam_Object = MibTableColumn
cOpticalPMCurrentMeanParam = _COpticalPMCurrentMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 1, 1, 6),
    _COpticalPMCurrentMeanParam_Type()
)
cOpticalPMCurrentMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMeanParam.setStatus("current")
_COpticalPMIntervalTable_Object = MibTable
cOpticalPMIntervalTable = _COpticalPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2)
)
if mibBuilder.loadTexts:
    cOpticalPMIntervalTable.setStatus("current")
_COpticalPMIntervalEntry_Object = MibTableRow
cOpticalPMIntervalEntry = _COpticalPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1)
)
cOpticalPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalDirection"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalParamType"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalPeriod"),
    (0, "CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    cOpticalPMIntervalEntry.setStatus("current")
_COpticalPMIntervalDirection_Type = OpticalIfDirection
_COpticalPMIntervalDirection_Object = MibTableColumn
cOpticalPMIntervalDirection = _COpticalPMIntervalDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 1),
    _COpticalPMIntervalDirection_Type()
)
cOpticalPMIntervalDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalDirection.setStatus("current")
_COpticalPMIntervalParamType_Type = OpticalParameterType
_COpticalPMIntervalParamType_Object = MibTableColumn
cOpticalPMIntervalParamType = _COpticalPMIntervalParamType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 2),
    _COpticalPMIntervalParamType_Type()
)
cOpticalPMIntervalParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalParamType.setStatus("current")
_COpticalPMIntervalPeriod_Type = CerentPeriod
_COpticalPMIntervalPeriod_Object = MibTableColumn
cOpticalPMIntervalPeriod = _COpticalPMIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 3),
    _COpticalPMIntervalPeriod_Type()
)
cOpticalPMIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalPeriod.setStatus("current")


class _COpticalPMIntervalNumber_Type(Integer32):
    """Custom type cOpticalPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_COpticalPMIntervalNumber_Type.__name__ = "Integer32"
_COpticalPMIntervalNumber_Object = MibTableColumn
cOpticalPMIntervalNumber = _COpticalPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 4),
    _COpticalPMIntervalNumber_Type()
)
cOpticalPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalNumber.setStatus("current")
_COpticalPMIntervalMaxParam_Type = OpticalParameterValue
_COpticalPMIntervalMaxParam_Object = MibTableColumn
cOpticalPMIntervalMaxParam = _COpticalPMIntervalMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 5),
    _COpticalPMIntervalMaxParam_Type()
)
cOpticalPMIntervalMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMaxParam.setStatus("current")
_COpticalPMIntervalMinParam_Type = OpticalParameterValue
_COpticalPMIntervalMinParam_Object = MibTableColumn
cOpticalPMIntervalMinParam = _COpticalPMIntervalMinParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 6),
    _COpticalPMIntervalMinParam_Type()
)
cOpticalPMIntervalMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMinParam.setStatus("current")
_COpticalPMIntervalMeanParam_Type = OpticalParameterValue
_COpticalPMIntervalMeanParam_Object = MibTableColumn
cOpticalPMIntervalMeanParam = _COpticalPMIntervalMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 7),
    _COpticalPMIntervalMeanParam_Type()
)
cOpticalPMIntervalMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMeanParam.setStatus("current")
_COpticalPMIntervalValidData_Type = TruthValue
_COpticalPMIntervalValidData_Object = MibTableColumn
cOpticalPMIntervalValidData = _COpticalPMIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 30, 2, 2, 1, 8),
    _COpticalPMIntervalValidData_Type()
)
cOpticalPMIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalValidData.setStatus("current")
_CerentOpticalMonitorMIBConformance_ObjectIdentity = ObjectIdentity
cerentOpticalMonitorMIBConformance = _CerentOpticalMonitorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20)
)
_CerentOpticalMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
cerentOpticalMonitorMIBCompliances = _CerentOpticalMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 1)
)
_CerentOpticalMonitorMIBGroups_ObjectIdentity = ObjectIdentity
cerentOpticalMonitorMIBGroups = _CerentOpticalMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 2)
)

# Managed Objects groups

cerentOpticalMIBMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 2, 1)
)
cerentOpticalMIBMonGroup.setObjects(
    ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParameterValue")
)
if mibBuilder.loadTexts:
    cerentOpticalMIBMonGroup.setStatus("current")

cerentOpticalMIBThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 2, 2)
)
cerentOpticalMIBThresholdGroup.setObjects(
      *(("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarning15MinThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarning1DayThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarning15MinThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarning1DayThresh"))
)
if mibBuilder.loadTexts:
    cerentOpticalMIBThresholdGroup.setStatus("current")

cerentOpticalMIBPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 2, 3)
)
cerentOpticalMIBPMGroup.setObjects(
      *(("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMaxParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMinParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMeanParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMaxParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMinParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMeanParam"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalValidData"))
)
if mibBuilder.loadTexts:
    cerentOpticalMIBPMGroup.setStatus("current")

cerentOpticalDwdmNetworkMIBThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 2, 4)
)
cerentOpticalDwdmNetworkMIBThresholdGroup.setObjects(
      *(("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarning15MinThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarning1DayThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarning15MinThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarning1DayThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamLowDegradeThresh"),
        ("CERENT-OPTICAL-MONITOR-MIB", "cOpticalParamHighDegradeThresh"))
)
if mibBuilder.loadTexts:
    cerentOpticalDwdmNetworkMIBThresholdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentOpticalMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 20, 1, 1)
)
if mibBuilder.loadTexts:
    cerentOpticalMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-OPTICAL-MONITOR-MIB",
    **{"OpticalParameterType": OpticalParameterType,
       "OpticalParameterValue": OpticalParameterValue,
       "OpticalIfDirection": OpticalIfDirection,
       "cerentOpticalMonitorMIB": cerentOpticalMonitorMIB,
       "cerentOpticalMonitorMIBObjects": cerentOpticalMonitorMIBObjects,
       "cerentOpticalMonGroup": cerentOpticalMonGroup,
       "cOpticalMonTable": cOpticalMonTable,
       "cOpticalMonEntry": cOpticalMonEntry,
       "cOpticalMonDirection": cOpticalMonDirection,
       "cOpticalMonParameterType": cOpticalMonParameterType,
       "cOpticalParameterValue": cOpticalParameterValue,
       "cOpticalParamHighAlarmThresh": cOpticalParamHighAlarmThresh,
       "cOpticalParamHighWarning15MinThresh": cOpticalParamHighWarning15MinThresh,
       "cOpticalParamHighWarning1DayThresh": cOpticalParamHighWarning1DayThresh,
       "cOpticalParamLowAlarmThresh": cOpticalParamLowAlarmThresh,
       "cOpticalParamLowWarning15MinThresh": cOpticalParamLowWarning15MinThresh,
       "cOpticalParamLowWarning1DayThresh": cOpticalParamLowWarning1DayThresh,
       "cOpticalParamLowDegradeThresh": cOpticalParamLowDegradeThresh,
       "cOpticalParamHighDegradeThresh": cOpticalParamHighDegradeThresh,
       "cerentOpticalPMGroup": cerentOpticalPMGroup,
       "cOpticalPMCurrentTable": cOpticalPMCurrentTable,
       "cOpticalPMCurrentEntry": cOpticalPMCurrentEntry,
       "cOpticalPMCurrentDirection": cOpticalPMCurrentDirection,
       "cOpticalPMCurrentParamType": cOpticalPMCurrentParamType,
       "cOpticalPMCurrentPeriod": cOpticalPMCurrentPeriod,
       "cOpticalPMCurrentMaxParam": cOpticalPMCurrentMaxParam,
       "cOpticalPMCurrentMinParam": cOpticalPMCurrentMinParam,
       "cOpticalPMCurrentMeanParam": cOpticalPMCurrentMeanParam,
       "cOpticalPMIntervalTable": cOpticalPMIntervalTable,
       "cOpticalPMIntervalEntry": cOpticalPMIntervalEntry,
       "cOpticalPMIntervalDirection": cOpticalPMIntervalDirection,
       "cOpticalPMIntervalParamType": cOpticalPMIntervalParamType,
       "cOpticalPMIntervalPeriod": cOpticalPMIntervalPeriod,
       "cOpticalPMIntervalNumber": cOpticalPMIntervalNumber,
       "cOpticalPMIntervalMaxParam": cOpticalPMIntervalMaxParam,
       "cOpticalPMIntervalMinParam": cOpticalPMIntervalMinParam,
       "cOpticalPMIntervalMeanParam": cOpticalPMIntervalMeanParam,
       "cOpticalPMIntervalValidData": cOpticalPMIntervalValidData,
       "cerentOpticalMonitorMIBConformance": cerentOpticalMonitorMIBConformance,
       "cerentOpticalMonitorMIBCompliances": cerentOpticalMonitorMIBCompliances,
       "cerentOpticalMonitorMIBCompliance": cerentOpticalMonitorMIBCompliance,
       "cerentOpticalMonitorMIBGroups": cerentOpticalMonitorMIBGroups,
       "cerentOpticalMIBMonGroup": cerentOpticalMIBMonGroup,
       "cerentOpticalMIBThresholdGroup": cerentOpticalMIBThresholdGroup,
       "cerentOpticalMIBPMGroup": cerentOpticalMIBPMGroup,
       "cerentOpticalDwdmNetworkMIBThresholdGroup": cerentOpticalDwdmNetworkMIBThresholdGroup}
)
