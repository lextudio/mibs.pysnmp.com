# SNMP MIB module (CERENT-GENERIC-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-GENERIC-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:24 2024
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

(CerentAlarmThresholdMonitorType,
 CerentLocation,
 CerentMonitorType,
 CerentPeriod) = mibBuilder.importSymbols(
    "CERENT-TC",
    "CerentAlarmThresholdMonitorType",
    "CerentLocation",
    "CerentMonitorType",
    "CerentPeriod")

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

cerentGenericPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 130)
)
cerentGenericPmMIB.setRevisions(
        ("2004-10-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentGenericPmMIBObjects_ObjectIdentity = ObjectIdentity
cerentGenericPmMIBObjects = _CerentGenericPmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90)
)
_CerentGenericPmThresholdTable_Object = MibTable
cerentGenericPmThresholdTable = _CerentGenericPmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10)
)
if mibBuilder.loadTexts:
    cerentGenericPmThresholdTable.setStatus("current")
_CerentGenericPmThresholdEntry_Object = MibTableRow
cerentGenericPmThresholdEntry = _CerentGenericPmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1)
)
cerentGenericPmThresholdEntry.setIndexNames(
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdIndex"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdMonitorType"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdLocation"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdPeriod"),
)
if mibBuilder.loadTexts:
    cerentGenericPmThresholdEntry.setStatus("current")


class _CerentGenericPmThresholdIndex_Type(Integer32):
    """Custom type cerentGenericPmThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentGenericPmThresholdIndex_Type.__name__ = "Integer32"
_CerentGenericPmThresholdIndex_Object = MibTableColumn
cerentGenericPmThresholdIndex = _CerentGenericPmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 10),
    _CerentGenericPmThresholdIndex_Type()
)
cerentGenericPmThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdIndex.setStatus("current")
_CerentGenericPmThresholdMonitorType_Type = CerentMonitorType
_CerentGenericPmThresholdMonitorType_Object = MibTableColumn
cerentGenericPmThresholdMonitorType = _CerentGenericPmThresholdMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 20),
    _CerentGenericPmThresholdMonitorType_Type()
)
cerentGenericPmThresholdMonitorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdMonitorType.setStatus("current")
_CerentGenericPmThresholdLocation_Type = CerentLocation
_CerentGenericPmThresholdLocation_Object = MibTableColumn
cerentGenericPmThresholdLocation = _CerentGenericPmThresholdLocation_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 30),
    _CerentGenericPmThresholdLocation_Type()
)
cerentGenericPmThresholdLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdLocation.setStatus("current")
_CerentGenericPmThresholdPeriod_Type = CerentPeriod
_CerentGenericPmThresholdPeriod_Object = MibTableColumn
cerentGenericPmThresholdPeriod = _CerentGenericPmThresholdPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 40),
    _CerentGenericPmThresholdPeriod_Type()
)
cerentGenericPmThresholdPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdPeriod.setStatus("current")
_CerentGenericPmThresholdValue_Type = Integer32
_CerentGenericPmThresholdValue_Object = MibTableColumn
cerentGenericPmThresholdValue = _CerentGenericPmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 50),
    _CerentGenericPmThresholdValue_Type()
)
cerentGenericPmThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdValue.setStatus("current")
_CerentGenericPmThresholdOverFlowValue_Type = Integer32
_CerentGenericPmThresholdOverFlowValue_Object = MibTableColumn
cerentGenericPmThresholdOverFlowValue = _CerentGenericPmThresholdOverFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 60),
    _CerentGenericPmThresholdOverFlowValue_Type()
)
cerentGenericPmThresholdOverFlowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdOverFlowValue.setStatus("current")
_CerentGenericPmThresholdHCValue_Type = Counter64
_CerentGenericPmThresholdHCValue_Object = MibTableColumn
cerentGenericPmThresholdHCValue = _CerentGenericPmThresholdHCValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 10, 1, 70),
    _CerentGenericPmThresholdHCValue_Type()
)
cerentGenericPmThresholdHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmThresholdHCValue.setStatus("current")
_CerentGenericPmStatsCurrentTable_Object = MibTable
cerentGenericPmStatsCurrentTable = _CerentGenericPmStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20)
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentTable.setStatus("current")
_CerentGenericPmStatsCurrentEntry_Object = MibTableRow
cerentGenericPmStatsCurrentEntry = _CerentGenericPmStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1)
)
cerentGenericPmStatsCurrentEntry.setIndexNames(
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentIndex"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentType"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentLocation"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentPeriod"),
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentEntry.setStatus("current")


class _CerentGenericPmStatsCurrentIndex_Type(Integer32):
    """Custom type cerentGenericPmStatsCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentGenericPmStatsCurrentIndex_Type.__name__ = "Integer32"
_CerentGenericPmStatsCurrentIndex_Object = MibTableColumn
cerentGenericPmStatsCurrentIndex = _CerentGenericPmStatsCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 10),
    _CerentGenericPmStatsCurrentIndex_Type()
)
cerentGenericPmStatsCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentIndex.setStatus("current")
_CerentGenericPmStatsCurrentType_Type = CerentMonitorType
_CerentGenericPmStatsCurrentType_Object = MibTableColumn
cerentGenericPmStatsCurrentType = _CerentGenericPmStatsCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 20),
    _CerentGenericPmStatsCurrentType_Type()
)
cerentGenericPmStatsCurrentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentType.setStatus("current")
_CerentGenericPmStatsCurrentLocation_Type = CerentLocation
_CerentGenericPmStatsCurrentLocation_Object = MibTableColumn
cerentGenericPmStatsCurrentLocation = _CerentGenericPmStatsCurrentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 30),
    _CerentGenericPmStatsCurrentLocation_Type()
)
cerentGenericPmStatsCurrentLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentLocation.setStatus("current")
_CerentGenericPmStatsCurrentPeriod_Type = CerentPeriod
_CerentGenericPmStatsCurrentPeriod_Object = MibTableColumn
cerentGenericPmStatsCurrentPeriod = _CerentGenericPmStatsCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 40),
    _CerentGenericPmStatsCurrentPeriod_Type()
)
cerentGenericPmStatsCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentPeriod.setStatus("current")
_CerentGenericPmStatsCurrentValue_Type = Integer32
_CerentGenericPmStatsCurrentValue_Object = MibTableColumn
cerentGenericPmStatsCurrentValue = _CerentGenericPmStatsCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 50),
    _CerentGenericPmStatsCurrentValue_Type()
)
cerentGenericPmStatsCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentValue.setStatus("current")
_CerentGenericPmStatsCurrentOverFlowValue_Type = Integer32
_CerentGenericPmStatsCurrentOverFlowValue_Object = MibTableColumn
cerentGenericPmStatsCurrentOverFlowValue = _CerentGenericPmStatsCurrentOverFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 60),
    _CerentGenericPmStatsCurrentOverFlowValue_Type()
)
cerentGenericPmStatsCurrentOverFlowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentOverFlowValue.setStatus("current")
_CerentGenericPmStatsCurrentHCValue_Type = Counter64
_CerentGenericPmStatsCurrentHCValue_Object = MibTableColumn
cerentGenericPmStatsCurrentHCValue = _CerentGenericPmStatsCurrentHCValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 70),
    _CerentGenericPmStatsCurrentHCValue_Type()
)
cerentGenericPmStatsCurrentHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentHCValue.setStatus("current")
_CerentGenericPmStatsCurrentValidData_Type = TruthValue
_CerentGenericPmStatsCurrentValidData_Object = MibTableColumn
cerentGenericPmStatsCurrentValidData = _CerentGenericPmStatsCurrentValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 80),
    _CerentGenericPmStatsCurrentValidData_Type()
)
cerentGenericPmStatsCurrentValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentValidData.setStatus("current")


class _CerentGenericPmStatsCurrentValidIntervals_Type(Integer32):
    """Custom type cerentGenericPmStatsCurrentValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CerentGenericPmStatsCurrentValidIntervals_Type.__name__ = "Integer32"
_CerentGenericPmStatsCurrentValidIntervals_Object = MibTableColumn
cerentGenericPmStatsCurrentValidIntervals = _CerentGenericPmStatsCurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 20, 1, 90),
    _CerentGenericPmStatsCurrentValidIntervals_Type()
)
cerentGenericPmStatsCurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentValidIntervals.setStatus("current")
_CerentGenericPmStatsIntervalTable_Object = MibTable
cerentGenericPmStatsIntervalTable = _CerentGenericPmStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30)
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalTable.setStatus("current")
_CerentGenericPmStatsIntervalEntry_Object = MibTableRow
cerentGenericPmStatsIntervalEntry = _CerentGenericPmStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1)
)
cerentGenericPmStatsIntervalEntry.setIndexNames(
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalIndex"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalType"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalLocation"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalPeriod"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalNumber"),
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalEntry.setStatus("current")


class _CerentGenericPmStatsIntervalIndex_Type(Integer32):
    """Custom type cerentGenericPmStatsIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentGenericPmStatsIntervalIndex_Type.__name__ = "Integer32"
_CerentGenericPmStatsIntervalIndex_Object = MibTableColumn
cerentGenericPmStatsIntervalIndex = _CerentGenericPmStatsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 10),
    _CerentGenericPmStatsIntervalIndex_Type()
)
cerentGenericPmStatsIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalIndex.setStatus("current")
_CerentGenericPmStatsIntervalType_Type = CerentMonitorType
_CerentGenericPmStatsIntervalType_Object = MibTableColumn
cerentGenericPmStatsIntervalType = _CerentGenericPmStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 20),
    _CerentGenericPmStatsIntervalType_Type()
)
cerentGenericPmStatsIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalType.setStatus("current")
_CerentGenericPmStatsIntervalLocation_Type = CerentLocation
_CerentGenericPmStatsIntervalLocation_Object = MibTableColumn
cerentGenericPmStatsIntervalLocation = _CerentGenericPmStatsIntervalLocation_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 30),
    _CerentGenericPmStatsIntervalLocation_Type()
)
cerentGenericPmStatsIntervalLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalLocation.setStatus("current")
_CerentGenericPmStatsIntervalPeriod_Type = CerentPeriod
_CerentGenericPmStatsIntervalPeriod_Object = MibTableColumn
cerentGenericPmStatsIntervalPeriod = _CerentGenericPmStatsIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 40),
    _CerentGenericPmStatsIntervalPeriod_Type()
)
cerentGenericPmStatsIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalPeriod.setStatus("current")


class _CerentGenericPmStatsIntervalNumber_Type(Integer32):
    """Custom type cerentGenericPmStatsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CerentGenericPmStatsIntervalNumber_Type.__name__ = "Integer32"
_CerentGenericPmStatsIntervalNumber_Object = MibTableColumn
cerentGenericPmStatsIntervalNumber = _CerentGenericPmStatsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 50),
    _CerentGenericPmStatsIntervalNumber_Type()
)
cerentGenericPmStatsIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalNumber.setStatus("current")
_CerentGenericPmStatsIntervalValue_Type = Integer32
_CerentGenericPmStatsIntervalValue_Object = MibTableColumn
cerentGenericPmStatsIntervalValue = _CerentGenericPmStatsIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 60),
    _CerentGenericPmStatsIntervalValue_Type()
)
cerentGenericPmStatsIntervalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalValue.setStatus("current")
_CerentGenericPmStatsIntervalOverFlowValue_Type = Integer32
_CerentGenericPmStatsIntervalOverFlowValue_Object = MibTableColumn
cerentGenericPmStatsIntervalOverFlowValue = _CerentGenericPmStatsIntervalOverFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 70),
    _CerentGenericPmStatsIntervalOverFlowValue_Type()
)
cerentGenericPmStatsIntervalOverFlowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalOverFlowValue.setStatus("current")
_CerentGenericPmStatsIntervalHCValue_Type = Counter64
_CerentGenericPmStatsIntervalHCValue_Object = MibTableColumn
cerentGenericPmStatsIntervalHCValue = _CerentGenericPmStatsIntervalHCValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 80),
    _CerentGenericPmStatsIntervalHCValue_Type()
)
cerentGenericPmStatsIntervalHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalHCValue.setStatus("current")
_CerentGenericPmStatsIntervalValidData_Type = TruthValue
_CerentGenericPmStatsIntervalValidData_Object = MibTableColumn
cerentGenericPmStatsIntervalValidData = _CerentGenericPmStatsIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 30, 1, 90),
    _CerentGenericPmStatsIntervalValidData_Type()
)
cerentGenericPmStatsIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalValidData.setStatus("current")
_CerentGenericPmAlarmThresholdTable_Object = MibTable
cerentGenericPmAlarmThresholdTable = _CerentGenericPmAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40)
)
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdTable.setStatus("current")
_CerentGenericPmAlarmThresholdEntry_Object = MibTableRow
cerentGenericPmAlarmThresholdEntry = _CerentGenericPmAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1)
)
cerentGenericPmAlarmThresholdEntry.setIndexNames(
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmAlarmThresholdIndex"),
    (0, "CERENT-GENERIC-PM-MIB", "cerentGenericPmAlarmThresholdMonitorType"),
)
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdEntry.setStatus("current")


class _CerentGenericPmAlarmThresholdIndex_Type(Integer32):
    """Custom type cerentGenericPmAlarmThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentGenericPmAlarmThresholdIndex_Type.__name__ = "Integer32"
_CerentGenericPmAlarmThresholdIndex_Object = MibTableColumn
cerentGenericPmAlarmThresholdIndex = _CerentGenericPmAlarmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1, 10),
    _CerentGenericPmAlarmThresholdIndex_Type()
)
cerentGenericPmAlarmThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdIndex.setStatus("current")
_CerentGenericPmAlarmThresholdMonitorType_Type = CerentAlarmThresholdMonitorType
_CerentGenericPmAlarmThresholdMonitorType_Object = MibTableColumn
cerentGenericPmAlarmThresholdMonitorType = _CerentGenericPmAlarmThresholdMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1, 20),
    _CerentGenericPmAlarmThresholdMonitorType_Type()
)
cerentGenericPmAlarmThresholdMonitorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdMonitorType.setStatus("current")
_CerentGenericPmAlarmThresholdValue_Type = Integer32
_CerentGenericPmAlarmThresholdValue_Object = MibTableColumn
cerentGenericPmAlarmThresholdValue = _CerentGenericPmAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1, 30),
    _CerentGenericPmAlarmThresholdValue_Type()
)
cerentGenericPmAlarmThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdValue.setStatus("current")
_CerentGenericPmAlarmThresholdOverFlowValue_Type = Integer32
_CerentGenericPmAlarmThresholdOverFlowValue_Object = MibTableColumn
cerentGenericPmAlarmThresholdOverFlowValue = _CerentGenericPmAlarmThresholdOverFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1, 40),
    _CerentGenericPmAlarmThresholdOverFlowValue_Type()
)
cerentGenericPmAlarmThresholdOverFlowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdOverFlowValue.setStatus("current")
_CerentGenericPmAlarmThresholdHCValue_Type = Counter64
_CerentGenericPmAlarmThresholdHCValue_Object = MibTableColumn
cerentGenericPmAlarmThresholdHCValue = _CerentGenericPmAlarmThresholdHCValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 90, 40, 1, 50),
    _CerentGenericPmAlarmThresholdHCValue_Type()
)
cerentGenericPmAlarmThresholdHCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdHCValue.setStatus("current")
_CerentGenericPmMIBConformance_ObjectIdentity = ObjectIdentity
cerentGenericPmMIBConformance = _CerentGenericPmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80)
)
_CerentGenericPmMIBCompliances_ObjectIdentity = ObjectIdentity
cerentGenericPmMIBCompliances = _CerentGenericPmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 1)
)
_CerentGenericPmMIBGroups_ObjectIdentity = ObjectIdentity
cerentGenericPmMIBGroups = _CerentGenericPmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 2)
)

# Managed Objects groups

cerentGenericPmThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 2, 10)
)
cerentGenericPmThresholdGroup.setObjects(
      *(("CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdOverFlowValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmThresholdHCValue"))
)
if mibBuilder.loadTexts:
    cerentGenericPmThresholdGroup.setStatus("current")

cerentGenericPmStatsCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 2, 20)
)
cerentGenericPmStatsCurrentGroup.setObjects(
      *(("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentOverFlowValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentHCValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentValidData"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsCurrentValidIntervals"))
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsCurrentGroup.setStatus("current")

cerentGenericPmStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 2, 30)
)
cerentGenericPmStatsIntervalGroup.setObjects(
      *(("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalOverFlowValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalHCValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmStatsIntervalValidData"))
)
if mibBuilder.loadTexts:
    cerentGenericPmStatsIntervalGroup.setStatus("current")

cerentGenericPmAlarmThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 2, 40)
)
cerentGenericPmAlarmThresholdGroup.setObjects(
      *(("CERENT-GENERIC-PM-MIB", "cerentGenericPmAlarmThresholdValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmAlarmThresholdOverFlowValue"),
        ("CERENT-GENERIC-PM-MIB", "cerentGenericPmAlarmThresholdHCValue"))
)
if mibBuilder.loadTexts:
    cerentGenericPmAlarmThresholdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentGenericPmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 80, 1, 1)
)
if mibBuilder.loadTexts:
    cerentGenericPmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-GENERIC-PM-MIB",
    **{"cerentGenericPmMIB": cerentGenericPmMIB,
       "cerentGenericPmMIBObjects": cerentGenericPmMIBObjects,
       "cerentGenericPmThresholdTable": cerentGenericPmThresholdTable,
       "cerentGenericPmThresholdEntry": cerentGenericPmThresholdEntry,
       "cerentGenericPmThresholdIndex": cerentGenericPmThresholdIndex,
       "cerentGenericPmThresholdMonitorType": cerentGenericPmThresholdMonitorType,
       "cerentGenericPmThresholdLocation": cerentGenericPmThresholdLocation,
       "cerentGenericPmThresholdPeriod": cerentGenericPmThresholdPeriod,
       "cerentGenericPmThresholdValue": cerentGenericPmThresholdValue,
       "cerentGenericPmThresholdOverFlowValue": cerentGenericPmThresholdOverFlowValue,
       "cerentGenericPmThresholdHCValue": cerentGenericPmThresholdHCValue,
       "cerentGenericPmStatsCurrentTable": cerentGenericPmStatsCurrentTable,
       "cerentGenericPmStatsCurrentEntry": cerentGenericPmStatsCurrentEntry,
       "cerentGenericPmStatsCurrentIndex": cerentGenericPmStatsCurrentIndex,
       "cerentGenericPmStatsCurrentType": cerentGenericPmStatsCurrentType,
       "cerentGenericPmStatsCurrentLocation": cerentGenericPmStatsCurrentLocation,
       "cerentGenericPmStatsCurrentPeriod": cerentGenericPmStatsCurrentPeriod,
       "cerentGenericPmStatsCurrentValue": cerentGenericPmStatsCurrentValue,
       "cerentGenericPmStatsCurrentOverFlowValue": cerentGenericPmStatsCurrentOverFlowValue,
       "cerentGenericPmStatsCurrentHCValue": cerentGenericPmStatsCurrentHCValue,
       "cerentGenericPmStatsCurrentValidData": cerentGenericPmStatsCurrentValidData,
       "cerentGenericPmStatsCurrentValidIntervals": cerentGenericPmStatsCurrentValidIntervals,
       "cerentGenericPmStatsIntervalTable": cerentGenericPmStatsIntervalTable,
       "cerentGenericPmStatsIntervalEntry": cerentGenericPmStatsIntervalEntry,
       "cerentGenericPmStatsIntervalIndex": cerentGenericPmStatsIntervalIndex,
       "cerentGenericPmStatsIntervalType": cerentGenericPmStatsIntervalType,
       "cerentGenericPmStatsIntervalLocation": cerentGenericPmStatsIntervalLocation,
       "cerentGenericPmStatsIntervalPeriod": cerentGenericPmStatsIntervalPeriod,
       "cerentGenericPmStatsIntervalNumber": cerentGenericPmStatsIntervalNumber,
       "cerentGenericPmStatsIntervalValue": cerentGenericPmStatsIntervalValue,
       "cerentGenericPmStatsIntervalOverFlowValue": cerentGenericPmStatsIntervalOverFlowValue,
       "cerentGenericPmStatsIntervalHCValue": cerentGenericPmStatsIntervalHCValue,
       "cerentGenericPmStatsIntervalValidData": cerentGenericPmStatsIntervalValidData,
       "cerentGenericPmAlarmThresholdTable": cerentGenericPmAlarmThresholdTable,
       "cerentGenericPmAlarmThresholdEntry": cerentGenericPmAlarmThresholdEntry,
       "cerentGenericPmAlarmThresholdIndex": cerentGenericPmAlarmThresholdIndex,
       "cerentGenericPmAlarmThresholdMonitorType": cerentGenericPmAlarmThresholdMonitorType,
       "cerentGenericPmAlarmThresholdValue": cerentGenericPmAlarmThresholdValue,
       "cerentGenericPmAlarmThresholdOverFlowValue": cerentGenericPmAlarmThresholdOverFlowValue,
       "cerentGenericPmAlarmThresholdHCValue": cerentGenericPmAlarmThresholdHCValue,
       "cerentGenericPmMIBConformance": cerentGenericPmMIBConformance,
       "cerentGenericPmMIBCompliances": cerentGenericPmMIBCompliances,
       "cerentGenericPmMIBCompliance": cerentGenericPmMIBCompliance,
       "cerentGenericPmMIBGroups": cerentGenericPmMIBGroups,
       "cerentGenericPmThresholdGroup": cerentGenericPmThresholdGroup,
       "cerentGenericPmStatsCurrentGroup": cerentGenericPmStatsCurrentGroup,
       "cerentGenericPmStatsIntervalGroup": cerentGenericPmStatsIntervalGroup,
       "cerentGenericPmAlarmThresholdGroup": cerentGenericPmAlarmThresholdGroup}
)
