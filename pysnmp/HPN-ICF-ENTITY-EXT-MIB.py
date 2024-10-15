# SNMP MIB module (HPN-ICF-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-ENTITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:04 2024
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

(entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfEntityExtend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfAdminState(Integer32, TextualConvention):
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
        *(("locked", 2),
          ("notSupported", 1),
          ("shuttingDown", 3),
          ("unlocked", 4))
    )



class HpnicfOperState(Integer32, TextualConvention):
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
        *(("dangerous", 4),
          ("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )



class HpnicfAlarmStatus(Bits, TextualConvention):
    status = "current"


class HpnicfStandbyStatus(Integer32, TextualConvention):
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
        *(("coldStandby", 3),
          ("hotStandby", 2),
          ("notSupported", 1),
          ("providingService", 4))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfEntityExtObjects_ObjectIdentity = ObjectIdentity
hpnicfEntityExtObjects = _HpnicfEntityExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1)
)
_HpnicfEntityExtState_ObjectIdentity = ObjectIdentity
hpnicfEntityExtState = _HpnicfEntityExtState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1)
)
_HpnicfEntityExtStateTable_Object = MibTable
hpnicfEntityExtStateTable = _HpnicfEntityExtStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntityExtStateTable.setStatus("current")
_HpnicfEntityExtStateEntry_Object = MibTableRow
hpnicfEntityExtStateEntry = _HpnicfEntityExtStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1)
)
hpnicfEntityExtStateEntry.setIndexNames(
    (0, "HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEntityExtStateEntry.setStatus("current")
_HpnicfEntityExtPhysicalIndex_Type = Integer32
_HpnicfEntityExtPhysicalIndex_Object = MibTableColumn
hpnicfEntityExtPhysicalIndex = _HpnicfEntityExtPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 1),
    _HpnicfEntityExtPhysicalIndex_Type()
)
hpnicfEntityExtPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtPhysicalIndex.setStatus("current")
_HpnicfEntityExtAdminStatus_Type = HpnicfAdminState
_HpnicfEntityExtAdminStatus_Object = MibTableColumn
hpnicfEntityExtAdminStatus = _HpnicfEntityExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 2),
    _HpnicfEntityExtAdminStatus_Type()
)
hpnicfEntityExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtAdminStatus.setStatus("current")
_HpnicfEntityExtOperStatus_Type = HpnicfOperState
_HpnicfEntityExtOperStatus_Object = MibTableColumn
hpnicfEntityExtOperStatus = _HpnicfEntityExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 3),
    _HpnicfEntityExtOperStatus_Type()
)
hpnicfEntityExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtOperStatus.setStatus("current")
_HpnicfEntityExtStandbyStatus_Type = HpnicfStandbyStatus
_HpnicfEntityExtStandbyStatus_Object = MibTableColumn
hpnicfEntityExtStandbyStatus = _HpnicfEntityExtStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 4),
    _HpnicfEntityExtStandbyStatus_Type()
)
hpnicfEntityExtStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtStandbyStatus.setStatus("current")
_HpnicfEntityExtAlarmLight_Type = HpnicfAlarmStatus
_HpnicfEntityExtAlarmLight_Object = MibTableColumn
hpnicfEntityExtAlarmLight = _HpnicfEntityExtAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 5),
    _HpnicfEntityExtAlarmLight_Type()
)
hpnicfEntityExtAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtAlarmLight.setStatus("current")


class _HpnicfEntityExtCpuUsage_Type(Integer32):
    """Custom type hpnicfEntityExtCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuUsage_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuUsage_Object = MibTableColumn
hpnicfEntityExtCpuUsage = _HpnicfEntityExtCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 6),
    _HpnicfEntityExtCpuUsage_Type()
)
hpnicfEntityExtCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsage.setStatus("current")


class _HpnicfEntityExtCpuUsageThreshold_Type(Integer32):
    """Custom type hpnicfEntityExtCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuUsageThreshold_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuUsageThreshold_Object = MibTableColumn
hpnicfEntityExtCpuUsageThreshold = _HpnicfEntityExtCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 7),
    _HpnicfEntityExtCpuUsageThreshold_Type()
)
hpnicfEntityExtCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageThreshold.setStatus("current")


class _HpnicfEntityExtMemUsage_Type(Integer32):
    """Custom type hpnicfEntityExtMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtMemUsage_Type.__name__ = "Integer32"
_HpnicfEntityExtMemUsage_Object = MibTableColumn
hpnicfEntityExtMemUsage = _HpnicfEntityExtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 8),
    _HpnicfEntityExtMemUsage_Type()
)
hpnicfEntityExtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsage.setStatus("current")


class _HpnicfEntityExtMemUsageThreshold_Type(Integer32):
    """Custom type hpnicfEntityExtMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtMemUsageThreshold_Type.__name__ = "Integer32"
_HpnicfEntityExtMemUsageThreshold_Object = MibTableColumn
hpnicfEntityExtMemUsageThreshold = _HpnicfEntityExtMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 9),
    _HpnicfEntityExtMemUsageThreshold_Type()
)
hpnicfEntityExtMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsageThreshold.setStatus("current")
_HpnicfEntityExtMemSize_Type = Unsigned32
_HpnicfEntityExtMemSize_Object = MibTableColumn
hpnicfEntityExtMemSize = _HpnicfEntityExtMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 10),
    _HpnicfEntityExtMemSize_Type()
)
hpnicfEntityExtMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemSize.setUnits("bytes")
_HpnicfEntityExtUpTime_Type = Integer32
_HpnicfEntityExtUpTime_Object = MibTableColumn
hpnicfEntityExtUpTime = _HpnicfEntityExtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 11),
    _HpnicfEntityExtUpTime_Type()
)
hpnicfEntityExtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEntityExtUpTime.setUnits("seconds")
_HpnicfEntityExtTemperature_Type = Integer32
_HpnicfEntityExtTemperature_Object = MibTableColumn
hpnicfEntityExtTemperature = _HpnicfEntityExtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 12),
    _HpnicfEntityExtTemperature_Type()
)
hpnicfEntityExtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperature.setStatus("current")
_HpnicfEntityExtTemperatureThreshold_Type = Integer32
_HpnicfEntityExtTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtTemperatureThreshold = _HpnicfEntityExtTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 13),
    _HpnicfEntityExtTemperatureThreshold_Type()
)
hpnicfEntityExtTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureThreshold.setStatus("current")
_HpnicfEntityExtVoltage_Type = Integer32
_HpnicfEntityExtVoltage_Object = MibTableColumn
hpnicfEntityExtVoltage = _HpnicfEntityExtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 14),
    _HpnicfEntityExtVoltage_Type()
)
hpnicfEntityExtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtVoltage.setStatus("current")
_HpnicfEntityExtVoltageLowThreshold_Type = Integer32
_HpnicfEntityExtVoltageLowThreshold_Object = MibTableColumn
hpnicfEntityExtVoltageLowThreshold = _HpnicfEntityExtVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 15),
    _HpnicfEntityExtVoltageLowThreshold_Type()
)
hpnicfEntityExtVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtVoltageLowThreshold.setStatus("current")
_HpnicfEntityExtVoltageHighThreshold_Type = Integer32
_HpnicfEntityExtVoltageHighThreshold_Object = MibTableColumn
hpnicfEntityExtVoltageHighThreshold = _HpnicfEntityExtVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 16),
    _HpnicfEntityExtVoltageHighThreshold_Type()
)
hpnicfEntityExtVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtVoltageHighThreshold.setStatus("current")
_HpnicfEntityExtCriticalTemperatureThreshold_Type = Integer32
_HpnicfEntityExtCriticalTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtCriticalTemperatureThreshold = _HpnicfEntityExtCriticalTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 17),
    _HpnicfEntityExtCriticalTemperatureThreshold_Type()
)
hpnicfEntityExtCriticalTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtCriticalTemperatureThreshold.setStatus("current")
_HpnicfEntityExtMacAddress_Type = MacAddress
_HpnicfEntityExtMacAddress_Object = MibTableColumn
hpnicfEntityExtMacAddress = _HpnicfEntityExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 18),
    _HpnicfEntityExtMacAddress_Type()
)
hpnicfEntityExtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMacAddress.setStatus("current")


class _HpnicfEntityExtErrorStatus_Type(Integer32):
    """Custom type hpnicfEntityExtErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              21,
              22,
              23,
              31,
              32,
              33,
              41,
              51,
              61,
              71,
              81,
              91)
        )
    )
    namedValues = NamedValues(
        *(("entityAbsent", 4),
          ("fanError", 41),
          ("hardwareFaulty", 91),
          ("moduleFaulty", 71),
          ("normal", 2),
          ("notSupported", 1),
          ("poeError", 11),
          ("postFailure", 3),
          ("psuError", 51),
          ("rpsError", 61),
          ("sensorError", 81),
          ("sfpBothError", 33),
          ("sfpRecvError", 31),
          ("sfpSendError", 32),
          ("stackError", 21),
          ("stackPortBlocked", 22),
          ("stackPortFailed", 23))
    )


_HpnicfEntityExtErrorStatus_Type.__name__ = "Integer32"
_HpnicfEntityExtErrorStatus_Object = MibTableColumn
hpnicfEntityExtErrorStatus = _HpnicfEntityExtErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 19),
    _HpnicfEntityExtErrorStatus_Type()
)
hpnicfEntityExtErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtErrorStatus.setStatus("current")


class _HpnicfEntityExtCpuMaxUsage_Type(Integer32):
    """Custom type hpnicfEntityExtCpuMaxUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuMaxUsage_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuMaxUsage_Object = MibTableColumn
hpnicfEntityExtCpuMaxUsage = _HpnicfEntityExtCpuMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 20),
    _HpnicfEntityExtCpuMaxUsage_Type()
)
hpnicfEntityExtCpuMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuMaxUsage.setStatus("current")
_HpnicfEntityExtLowerTemperatureThreshold_Type = Integer32
_HpnicfEntityExtLowerTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtLowerTemperatureThreshold = _HpnicfEntityExtLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 21),
    _HpnicfEntityExtLowerTemperatureThreshold_Type()
)
hpnicfEntityExtLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtLowerTemperatureThreshold.setStatus("current")
_HpnicfEntityExtShutdownTemperatureThreshold_Type = Integer32
_HpnicfEntityExtShutdownTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtShutdownTemperatureThreshold = _HpnicfEntityExtShutdownTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 22),
    _HpnicfEntityExtShutdownTemperatureThreshold_Type()
)
hpnicfEntityExtShutdownTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtShutdownTemperatureThreshold.setStatus("current")
_HpnicfEntityExtPhyMemSize_Type = Unsigned32
_HpnicfEntityExtPhyMemSize_Object = MibTableColumn
hpnicfEntityExtPhyMemSize = _HpnicfEntityExtPhyMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 23),
    _HpnicfEntityExtPhyMemSize_Type()
)
hpnicfEntityExtPhyMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtPhyMemSize.setStatus("current")
_HpnicfEntityExtPhyCpuFrequency_Type = Integer32
_HpnicfEntityExtPhyCpuFrequency_Object = MibTableColumn
hpnicfEntityExtPhyCpuFrequency = _HpnicfEntityExtPhyCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 24),
    _HpnicfEntityExtPhyCpuFrequency_Type()
)
hpnicfEntityExtPhyCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtPhyCpuFrequency.setStatus("current")


class _HpnicfEntityExtFirstUsedDate_Type(DateAndTime):
    """Custom type hpnicfEntityExtFirstUsedDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfEntityExtFirstUsedDate_Type.__name__ = "DateAndTime"
_HpnicfEntityExtFirstUsedDate_Object = MibTableColumn
hpnicfEntityExtFirstUsedDate = _HpnicfEntityExtFirstUsedDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 25),
    _HpnicfEntityExtFirstUsedDate_Type()
)
hpnicfEntityExtFirstUsedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtFirstUsedDate.setStatus("current")


class _HpnicfEntityExtCpuAvgUsage_Type(Integer32):
    """Custom type hpnicfEntityExtCpuAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuAvgUsage_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuAvgUsage_Object = MibTableColumn
hpnicfEntityExtCpuAvgUsage = _HpnicfEntityExtCpuAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 26),
    _HpnicfEntityExtCpuAvgUsage_Type()
)
hpnicfEntityExtCpuAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuAvgUsage.setStatus("current")


class _HpnicfEntityExtMemAvgUsage_Type(Integer32):
    """Custom type hpnicfEntityExtMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtMemAvgUsage_Type.__name__ = "Integer32"
_HpnicfEntityExtMemAvgUsage_Object = MibTableColumn
hpnicfEntityExtMemAvgUsage = _HpnicfEntityExtMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 27),
    _HpnicfEntityExtMemAvgUsage_Type()
)
hpnicfEntityExtMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemAvgUsage.setStatus("current")


class _HpnicfEntityExtMemType_Type(OctetString):
    """Custom type hpnicfEntityExtMemType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfEntityExtMemType_Type.__name__ = "OctetString"
_HpnicfEntityExtMemType_Object = MibTableColumn
hpnicfEntityExtMemType = _HpnicfEntityExtMemType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 28),
    _HpnicfEntityExtMemType_Type()
)
hpnicfEntityExtMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemType.setStatus("current")
_HpnicfEntityExtCriticalLowerTemperatureThreshold_Type = Integer32
_HpnicfEntityExtCriticalLowerTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtCriticalLowerTemperatureThreshold = _HpnicfEntityExtCriticalLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 29),
    _HpnicfEntityExtCriticalLowerTemperatureThreshold_Type()
)
hpnicfEntityExtCriticalLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtCriticalLowerTemperatureThreshold.setStatus("current")
_HpnicfEntityExtShutdownLowerTemperatureThreshold_Type = Integer32
_HpnicfEntityExtShutdownLowerTemperatureThreshold_Object = MibTableColumn
hpnicfEntityExtShutdownLowerTemperatureThreshold = _HpnicfEntityExtShutdownLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 30),
    _HpnicfEntityExtShutdownLowerTemperatureThreshold_Type()
)
hpnicfEntityExtShutdownLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtShutdownLowerTemperatureThreshold.setStatus("current")


class _HpnicfEntityExtCpuUsageRecoverThreshold_Type(Integer32):
    """Custom type hpnicfEntityExtCpuUsageRecoverThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuUsageRecoverThreshold_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuUsageRecoverThreshold_Object = MibTableColumn
hpnicfEntityExtCpuUsageRecoverThreshold = _HpnicfEntityExtCpuUsageRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 31),
    _HpnicfEntityExtCpuUsageRecoverThreshold_Type()
)
hpnicfEntityExtCpuUsageRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageRecoverThreshold.setStatus("current")
_HpnicfEntityExtMemSizeRev_Type = CounterBasedGauge64
_HpnicfEntityExtMemSizeRev_Object = MibTableColumn
hpnicfEntityExtMemSizeRev = _HpnicfEntityExtMemSizeRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 32),
    _HpnicfEntityExtMemSizeRev_Type()
)
hpnicfEntityExtMemSizeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemSizeRev.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEntityExtMemSizeRev.setUnits("bytes")


class _HpnicfEntityExtCpuUsageIn1Minute_Type(Integer32):
    """Custom type hpnicfEntityExtCpuUsageIn1Minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuUsageIn1Minute_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuUsageIn1Minute_Object = MibTableColumn
hpnicfEntityExtCpuUsageIn1Minute = _HpnicfEntityExtCpuUsageIn1Minute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 33),
    _HpnicfEntityExtCpuUsageIn1Minute_Type()
)
hpnicfEntityExtCpuUsageIn1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageIn1Minute.setStatus("current")


class _HpnicfEntityExtCpuUsageIn5Minutes_Type(Integer32):
    """Custom type hpnicfEntityExtCpuUsageIn5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfEntityExtCpuUsageIn5Minutes_Type.__name__ = "Integer32"
_HpnicfEntityExtCpuUsageIn5Minutes_Object = MibTableColumn
hpnicfEntityExtCpuUsageIn5Minutes = _HpnicfEntityExtCpuUsageIn5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 1, 1, 1, 34),
    _HpnicfEntityExtCpuUsageIn5Minutes_Type()
)
hpnicfEntityExtCpuUsageIn5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageIn5Minutes.setStatus("current")
_HpnicfEntityExtManu_ObjectIdentity = ObjectIdentity
hpnicfEntityExtManu = _HpnicfEntityExtManu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2)
)
_HpnicfEntityExtManuTable_Object = MibTable
hpnicfEntityExtManuTable = _HpnicfEntityExtManuTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntityExtManuTable.setStatus("current")
_HpnicfEntityExtManuEntry_Object = MibTableRow
hpnicfEntityExtManuEntry = _HpnicfEntityExtManuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1)
)
hpnicfEntityExtManuEntry.setIndexNames(
    (0, "HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtManuPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEntityExtManuEntry.setStatus("current")


class _HpnicfEntityExtManuPhysicalIndex_Type(Integer32):
    """Custom type hpnicfEntityExtManuPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfEntityExtManuPhysicalIndex_Type.__name__ = "Integer32"
_HpnicfEntityExtManuPhysicalIndex_Object = MibTableColumn
hpnicfEntityExtManuPhysicalIndex = _HpnicfEntityExtManuPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1, 1),
    _HpnicfEntityExtManuPhysicalIndex_Type()
)
hpnicfEntityExtManuPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtManuPhysicalIndex.setStatus("current")
_HpnicfEntityExtManuSerialNum_Type = SnmpAdminString
_HpnicfEntityExtManuSerialNum_Object = MibTableColumn
hpnicfEntityExtManuSerialNum = _HpnicfEntityExtManuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1, 2),
    _HpnicfEntityExtManuSerialNum_Type()
)
hpnicfEntityExtManuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtManuSerialNum.setStatus("current")
_HpnicfEntityExtManuBuildInfo_Type = SnmpAdminString
_HpnicfEntityExtManuBuildInfo_Object = MibTableColumn
hpnicfEntityExtManuBuildInfo = _HpnicfEntityExtManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1, 3),
    _HpnicfEntityExtManuBuildInfo_Type()
)
hpnicfEntityExtManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtManuBuildInfo.setStatus("current")
_HpnicfEntityExtManuBOM_Type = SnmpAdminString
_HpnicfEntityExtManuBOM_Object = MibTableColumn
hpnicfEntityExtManuBOM = _HpnicfEntityExtManuBOM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1, 4),
    _HpnicfEntityExtManuBOM_Type()
)
hpnicfEntityExtManuBOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtManuBOM.setStatus("current")
_HpnicfEntityExtMacAddressCount_Type = Unsigned32
_HpnicfEntityExtMacAddressCount_Object = MibTableColumn
hpnicfEntityExtMacAddressCount = _HpnicfEntityExtMacAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 2, 1, 1, 5),
    _HpnicfEntityExtMacAddressCount_Type()
)
hpnicfEntityExtMacAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtMacAddressCount.setStatus("current")
_HpnicfEntityExtPower_ObjectIdentity = ObjectIdentity
hpnicfEntityExtPower = _HpnicfEntityExtPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3)
)
_HpnicfEntityExtPowerTable_Object = MibTable
hpnicfEntityExtPowerTable = _HpnicfEntityExtPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntityExtPowerTable.setStatus("current")
_HpnicfEntityExtPowerEntry_Object = MibTableRow
hpnicfEntityExtPowerEntry = _HpnicfEntityExtPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1)
)
hpnicfEntityExtPowerEntry.setIndexNames(
    (0, "HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPowerPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEntityExtPowerEntry.setStatus("current")


class _HpnicfEntityExtPowerPhysicalIndex_Type(Integer32):
    """Custom type hpnicfEntityExtPowerPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfEntityExtPowerPhysicalIndex_Type.__name__ = "Integer32"
_HpnicfEntityExtPowerPhysicalIndex_Object = MibTableColumn
hpnicfEntityExtPowerPhysicalIndex = _HpnicfEntityExtPowerPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1, 1),
    _HpnicfEntityExtPowerPhysicalIndex_Type()
)
hpnicfEntityExtPowerPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtPowerPhysicalIndex.setStatus("current")
_HpnicfEntityExtNominalPower_Type = Gauge32
_HpnicfEntityExtNominalPower_Object = MibTableColumn
hpnicfEntityExtNominalPower = _HpnicfEntityExtNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1, 2),
    _HpnicfEntityExtNominalPower_Type()
)
hpnicfEntityExtNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtNominalPower.setStatus("current")
_HpnicfEntityExtCurrentPower_Type = Gauge32
_HpnicfEntityExtCurrentPower_Object = MibTableColumn
hpnicfEntityExtCurrentPower = _HpnicfEntityExtCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1, 3),
    _HpnicfEntityExtCurrentPower_Type()
)
hpnicfEntityExtCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEntityExtCurrentPower.setStatus("current")
_HpnicfEntityExtAveragePower_Type = Integer32
_HpnicfEntityExtAveragePower_Object = MibTableColumn
hpnicfEntityExtAveragePower = _HpnicfEntityExtAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1, 4),
    _HpnicfEntityExtAveragePower_Type()
)
hpnicfEntityExtAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtAveragePower.setStatus("current")
_HpnicfEntityExtPeakPower_Type = Integer32
_HpnicfEntityExtPeakPower_Object = MibTableColumn
hpnicfEntityExtPeakPower = _HpnicfEntityExtPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 3, 1, 1, 5),
    _HpnicfEntityExtPeakPower_Type()
)
hpnicfEntityExtPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEntityExtPeakPower.setStatus("current")
_HpnicfProcessObjects_ObjectIdentity = ObjectIdentity
hpnicfProcessObjects = _HpnicfProcessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4)
)
_HpnicfProcessTable_Object = MibTable
hpnicfProcessTable = _HpnicfProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfProcessTable.setStatus("current")
_HpnicfProcessEntry_Object = MibTableRow
hpnicfProcessEntry = _HpnicfProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4, 1, 1)
)
hpnicfProcessEntry.setIndexNames(
    (0, "HPN-ICF-ENTITY-EXT-MIB", "hpnicfProcessID"),
)
if mibBuilder.loadTexts:
    hpnicfProcessEntry.setStatus("current")
_HpnicfProcessID_Type = Unsigned32
_HpnicfProcessID_Object = MibTableColumn
hpnicfProcessID = _HpnicfProcessID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4, 1, 1, 1),
    _HpnicfProcessID_Type()
)
hpnicfProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProcessID.setStatus("current")


class _HpnicfProcessName_Type(DisplayString):
    """Custom type hpnicfProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfProcessName_Type.__name__ = "DisplayString"
_HpnicfProcessName_Object = MibTableColumn
hpnicfProcessName = _HpnicfProcessName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4, 1, 1, 2),
    _HpnicfProcessName_Type()
)
hpnicfProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProcessName.setStatus("current")


class _HpnicfProcessUtil5Min_Type(Unsigned32):
    """Custom type hpnicfProcessUtil5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfProcessUtil5Min_Type.__name__ = "Unsigned32"
_HpnicfProcessUtil5Min_Object = MibTableColumn
hpnicfProcessUtil5Min = _HpnicfProcessUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 1, 4, 1, 1, 3),
    _HpnicfProcessUtil5Min_Type()
)
hpnicfProcessUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfProcessUtil5Min.setStatus("current")
_HpnicfEntityExtTraps_ObjectIdentity = ObjectIdentity
hpnicfEntityExtTraps = _HpnicfEntityExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2)
)
_HpnicfEntityExtTrapsPrefix_ObjectIdentity = ObjectIdentity
hpnicfEntityExtTrapsPrefix = _HpnicfEntityExtTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0)
)
_HpnicfEntityExtTrapsInfor_ObjectIdentity = ObjectIdentity
hpnicfEntityExtTrapsInfor = _HpnicfEntityExtTrapsInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 1)
)


class _HpnicfEntityExtTrapDescription_Type(SnmpAdminString):
    """Custom type hpnicfEntityExtTrapDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEntityExtTrapDescription_Type.__name__ = "SnmpAdminString"
_HpnicfEntityExtTrapDescription_Object = MibScalar
hpnicfEntityExtTrapDescription = _HpnicfEntityExtTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 1, 1),
    _HpnicfEntityExtTrapDescription_Type()
)
hpnicfEntityExtTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtTrapDescription.setStatus("current")


class _HpnicfEntityExtECCParityAlarmStatus_Type(Integer32):
    """Custom type hpnicfEntityExtECCParityAlarmStatus based on Integer32"""
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
        *(("controlmemory", 10),
          ("egressbuffer", 8),
          ("ingressbuffer", 7),
          ("l1cache", 2),
          ("l2cache", 3),
          ("lpm", 9),
          ("mac", 5),
          ("other", 1),
          ("sdram", 4),
          ("tcam", 6))
    )


_HpnicfEntityExtECCParityAlarmStatus_Type.__name__ = "Integer32"
_HpnicfEntityExtECCParityAlarmStatus_Object = MibScalar
hpnicfEntityExtECCParityAlarmStatus = _HpnicfEntityExtECCParityAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 1, 2),
    _HpnicfEntityExtECCParityAlarmStatus_Type()
)
hpnicfEntityExtECCParityAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtECCParityAlarmStatus.setStatus("current")
_HpnicfEntityExtSFPInvalidInDays_Type = Integer32
_HpnicfEntityExtSFPInvalidInDays_Object = MibScalar
hpnicfEntityExtSFPInvalidInDays = _HpnicfEntityExtSFPInvalidInDays_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 1, 3),
    _HpnicfEntityExtSFPInvalidInDays_Type()
)
hpnicfEntityExtSFPInvalidInDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPInvalidInDays.setStatus("current")
_HpnicfEntityExtFirstTrapTime_Type = TimeTicks
_HpnicfEntityExtFirstTrapTime_Object = MibScalar
hpnicfEntityExtFirstTrapTime = _HpnicfEntityExtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 1, 4),
    _HpnicfEntityExtFirstTrapTime_Type()
)
hpnicfEntityExtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEntityExtFirstTrapTime.setStatus("current")
_HpnicfEntityExtConformance_ObjectIdentity = ObjectIdentity
hpnicfEntityExtConformance = _HpnicfEntityExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3)
)
_HpnicfEntityExtCompliances_ObjectIdentity = ObjectIdentity
hpnicfEntityExtCompliances = _HpnicfEntityExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 1)
)
_HpnicfEntityExtGroups_ObjectIdentity = ObjectIdentity
hpnicfEntityExtGroups = _HpnicfEntityExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 2)
)

# Managed Objects groups

hpnicfEntityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 2, 1)
)
hpnicfEntityExtGroup.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtOperStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtStandbyStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSize"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtUpTime"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageLowThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageHighThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCriticalTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMacAddress"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtErrorStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuMaxUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtLowerTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtShutdownTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhyMemSize"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhyCpuFrequency"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFirstUsedDate"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuAvgUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemAvgUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemType"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCriticalLowerTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtShutdownLowerTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageRecoverThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSizeRev"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageIn1Minute"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageIn5Minutes"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtGroup.setStatus("current")

hpnicfEntityExtManuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 2, 3)
)
hpnicfEntityExtManuGroup.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtManuPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtManuSerialNum"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtManuBuildInfo"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtManuBOM"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMacAddressCount"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtManuGroup.setStatus("current")

hpnicfEntityExtPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 2, 4)
)
hpnicfEntityExtPowerGroup.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPowerPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtNominalPower"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCurrentPower"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAveragePower"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPeakPower"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtPowerGroup.setStatus("current")


# Notification objects

hpnicfEntityExtTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 1)
)
hpnicfEntityExtTemperatureThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 2)
)
hpnicfEntityExtVoltageLowThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageLowThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 3)
)
hpnicfEntityExtVoltageHighThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageHighThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtCpuUsageThresholdNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 4)
)
hpnicfEntityExtCpuUsageThresholdNotfication.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageRecoverThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageThresholdNotfication.setStatus(
        "current"
    )

hpnicfEntityExtMemUsageThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 5)
)
hpnicfEntityExtMemUsageThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSize"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsageThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtOperEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 6)
)
hpnicfEntityExtOperEnabled.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtOperEnabled.setStatus(
        "current"
    )

hpnicfEntityExtOperDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 7)
)
hpnicfEntityExtOperDisabled.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtOperDisabled.setStatus(
        "current"
    )

hpnicfEntityExtCriticalTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 8)
)
hpnicfEntityExtCriticalTemperatureThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCriticalTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtCriticalTemperatureThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtSFPAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 9)
)
hpnicfEntityExtSFPAlarmOn.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtErrorStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPAlarmOn.setStatus(
        "current"
    )

hpnicfEntityExtSFPAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 10)
)
hpnicfEntityExtSFPAlarmOff.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtErrorStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPAlarmOff.setStatus(
        "current"
    )

hpnicfEntityExtSFPPhony = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 11)
)
hpnicfEntityExtSFPPhony.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPPhony.setStatus(
        "current"
    )

hpnicfEntityInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 12)
)
hpnicfEntityInsert.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEntityInsert.setStatus(
        "current"
    )

hpnicfEntityRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 13)
)
hpnicfEntityRemove.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEntityRemove.setStatus(
        "current"
    )

hpnicfEntityExtForcedPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 14)
)
hpnicfEntityExtForcedPowerOff.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtForcedPowerOff.setStatus(
        "current"
    )

hpnicfEntityExtForcedPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 15)
)
hpnicfEntityExtForcedPowerOn.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtForcedPowerOn.setStatus(
        "current"
    )

hpnicfEntityExtFaultAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 16)
)
hpnicfEntityExtFaultAlarmOn.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtErrorStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtFaultAlarmOn.setStatus(
        "current"
    )

hpnicfEntityExtFaultAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 17)
)
hpnicfEntityExtFaultAlarmOff.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtErrorStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtFaultAlarmOff.setStatus(
        "current"
    )

hpnicfEntityExtResourceLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 18)
)
hpnicfEntityExtResourceLack.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtResourceLack.setStatus(
        "current"
    )

hpnicfEntityExtResourceEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 19)
)
hpnicfEntityExtResourceEnough.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtResourceEnough.setStatus(
        "current"
    )

hpnicfEntityExtTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 20)
)
hpnicfEntityExtTemperatureLower.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtLowerTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureLower.setStatus(
        "current"
    )

hpnicfEntityExtTemperatureTooUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 21)
)
hpnicfEntityExtTemperatureTooUp.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtShutdownTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureTooUp.setStatus(
        "current"
    )

hpnicfEntityExtTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 22)
)
hpnicfEntityExtTemperatureNormal.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtLowerTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureNormal.setStatus(
        "current"
    )

hpnicfEntityExternalAlarmOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 23)
)
hpnicfEntityExternalAlarmOccur.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExternalAlarmOccur.setStatus(
        "current"
    )

hpnicfEntityExternalAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 24)
)
hpnicfEntityExternalAlarmRecover.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExternalAlarmRecover.setStatus(
        "current"
    )

hpnicfEntityExtCpuUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 25)
)
hpnicfEntityExtCpuUsageThresholdRecover.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageRecoverThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtCpuUsageThresholdRecover.setStatus(
        "current"
    )

hpnicfEntityExtMemUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 26)
)
hpnicfEntityExtMemUsageThresholdRecover.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSize"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsageThresholdRecover.setStatus(
        "current"
    )

hpnicfEntityExtMemAllocatedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 27)
)
hpnicfEntityExtMemAllocatedFailed.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtMemAllocatedFailed.setStatus(
        "current"
    )

hpnicfEntityExtECCParityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 28)
)
hpnicfEntityExtECCParityAlarm.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtECCParityAlarmStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtECCParityAlarm.setStatus(
        "current"
    )

hpnicfEntityExtCritLowerTempThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 29)
)
hpnicfEntityExtCritLowerTempThresholdNotification.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCriticalLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtCritLowerTempThresholdNotification.setStatus(
        "current"
    )

hpnicfEntityExtTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 30)
)
hpnicfEntityExtTemperatureTooLow.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperature"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtTemperatureTooLow.setStatus(
        "current"
    )

hpnicfEntityExtFanDirectionNotPreferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 31)
)
hpnicfEntityExtFanDirectionNotPreferred.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtFanDirectionNotPreferred.setStatus(
        "current"
    )

hpnicfEntityExtFanDirectionNotAccord = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 32)
)
hpnicfEntityExtFanDirectionNotAccord.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtFanDirectionNotAccord.setStatus(
        "current"
    )

hpnicfEntityExtSFPInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 33)
)
hpnicfEntityExtSFPInvalid.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPInvalidInDays"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPInvalid.setStatus(
        "current"
    )

hpnicfEntityExtSFPInvalidNow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 34)
)
hpnicfEntityExtSFPInvalidNow.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtSFPInvalidNow.setStatus(
        "current"
    )

hpnicfEntityExtMemUsageThresholdOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 35)
)
hpnicfEntityExtMemUsageThresholdOverTrap.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSizeRev"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsageThresholdOverTrap.setStatus(
        "current"
    )

hpnicfEntityExtMemUsageThresholdRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 2, 0, 36)
)
hpnicfEntityExtMemUsageThresholdRecoverTrap.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtPhysicalIndex"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsage"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThreshold"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemSizeRev"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAdminStatus"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtMemUsageThresholdRecoverTrap.setStatus(
        "current"
    )


# Notifications groups

hpnicfEntityExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 2, 2)
)
hpnicfEntityExtNotificationGroup.setObjects(
      *(("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageLowThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtVoltageHighThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageThresholdNotfication"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtOperEnabled"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtOperDisabled"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCriticalTemperatureThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPAlarmOn"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPAlarmOff"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPPhony"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityInsert"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityRemove"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtForcedPowerOff"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtForcedPowerOn"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFaultAlarmOn"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFaultAlarmOff"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtResourceLack"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtResourceEnough"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureLower"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureTooUp"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureNormal"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExternalAlarmOccur"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExternalAlarmRecover"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCpuUsageThresholdRecover"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThresholdRecover"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemAllocatedFailed"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtECCParityAlarm"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtCritLowerTempThresholdNotification"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtTemperatureTooLow"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFanDirectionNotPreferred"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtFanDirectionNotAccord"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPInvalid"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtSFPInvalidNow"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThresholdOverTrap"),
        ("HPN-ICF-ENTITY-EXT-MIB", "hpnicfEntityExtMemUsageThresholdRecoverTrap"))
)
if mibBuilder.loadTexts:
    hpnicfEntityExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfEntityExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntityExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ENTITY-EXT-MIB",
    **{"HpnicfAdminState": HpnicfAdminState,
       "HpnicfOperState": HpnicfOperState,
       "HpnicfAlarmStatus": HpnicfAlarmStatus,
       "HpnicfStandbyStatus": HpnicfStandbyStatus,
       "hpnicfEntityExtend": hpnicfEntityExtend,
       "hpnicfEntityExtObjects": hpnicfEntityExtObjects,
       "hpnicfEntityExtState": hpnicfEntityExtState,
       "hpnicfEntityExtStateTable": hpnicfEntityExtStateTable,
       "hpnicfEntityExtStateEntry": hpnicfEntityExtStateEntry,
       "hpnicfEntityExtPhysicalIndex": hpnicfEntityExtPhysicalIndex,
       "hpnicfEntityExtAdminStatus": hpnicfEntityExtAdminStatus,
       "hpnicfEntityExtOperStatus": hpnicfEntityExtOperStatus,
       "hpnicfEntityExtStandbyStatus": hpnicfEntityExtStandbyStatus,
       "hpnicfEntityExtAlarmLight": hpnicfEntityExtAlarmLight,
       "hpnicfEntityExtCpuUsage": hpnicfEntityExtCpuUsage,
       "hpnicfEntityExtCpuUsageThreshold": hpnicfEntityExtCpuUsageThreshold,
       "hpnicfEntityExtMemUsage": hpnicfEntityExtMemUsage,
       "hpnicfEntityExtMemUsageThreshold": hpnicfEntityExtMemUsageThreshold,
       "hpnicfEntityExtMemSize": hpnicfEntityExtMemSize,
       "hpnicfEntityExtUpTime": hpnicfEntityExtUpTime,
       "hpnicfEntityExtTemperature": hpnicfEntityExtTemperature,
       "hpnicfEntityExtTemperatureThreshold": hpnicfEntityExtTemperatureThreshold,
       "hpnicfEntityExtVoltage": hpnicfEntityExtVoltage,
       "hpnicfEntityExtVoltageLowThreshold": hpnicfEntityExtVoltageLowThreshold,
       "hpnicfEntityExtVoltageHighThreshold": hpnicfEntityExtVoltageHighThreshold,
       "hpnicfEntityExtCriticalTemperatureThreshold": hpnicfEntityExtCriticalTemperatureThreshold,
       "hpnicfEntityExtMacAddress": hpnicfEntityExtMacAddress,
       "hpnicfEntityExtErrorStatus": hpnicfEntityExtErrorStatus,
       "hpnicfEntityExtCpuMaxUsage": hpnicfEntityExtCpuMaxUsage,
       "hpnicfEntityExtLowerTemperatureThreshold": hpnicfEntityExtLowerTemperatureThreshold,
       "hpnicfEntityExtShutdownTemperatureThreshold": hpnicfEntityExtShutdownTemperatureThreshold,
       "hpnicfEntityExtPhyMemSize": hpnicfEntityExtPhyMemSize,
       "hpnicfEntityExtPhyCpuFrequency": hpnicfEntityExtPhyCpuFrequency,
       "hpnicfEntityExtFirstUsedDate": hpnicfEntityExtFirstUsedDate,
       "hpnicfEntityExtCpuAvgUsage": hpnicfEntityExtCpuAvgUsage,
       "hpnicfEntityExtMemAvgUsage": hpnicfEntityExtMemAvgUsage,
       "hpnicfEntityExtMemType": hpnicfEntityExtMemType,
       "hpnicfEntityExtCriticalLowerTemperatureThreshold": hpnicfEntityExtCriticalLowerTemperatureThreshold,
       "hpnicfEntityExtShutdownLowerTemperatureThreshold": hpnicfEntityExtShutdownLowerTemperatureThreshold,
       "hpnicfEntityExtCpuUsageRecoverThreshold": hpnicfEntityExtCpuUsageRecoverThreshold,
       "hpnicfEntityExtMemSizeRev": hpnicfEntityExtMemSizeRev,
       "hpnicfEntityExtCpuUsageIn1Minute": hpnicfEntityExtCpuUsageIn1Minute,
       "hpnicfEntityExtCpuUsageIn5Minutes": hpnicfEntityExtCpuUsageIn5Minutes,
       "hpnicfEntityExtManu": hpnicfEntityExtManu,
       "hpnicfEntityExtManuTable": hpnicfEntityExtManuTable,
       "hpnicfEntityExtManuEntry": hpnicfEntityExtManuEntry,
       "hpnicfEntityExtManuPhysicalIndex": hpnicfEntityExtManuPhysicalIndex,
       "hpnicfEntityExtManuSerialNum": hpnicfEntityExtManuSerialNum,
       "hpnicfEntityExtManuBuildInfo": hpnicfEntityExtManuBuildInfo,
       "hpnicfEntityExtManuBOM": hpnicfEntityExtManuBOM,
       "hpnicfEntityExtMacAddressCount": hpnicfEntityExtMacAddressCount,
       "hpnicfEntityExtPower": hpnicfEntityExtPower,
       "hpnicfEntityExtPowerTable": hpnicfEntityExtPowerTable,
       "hpnicfEntityExtPowerEntry": hpnicfEntityExtPowerEntry,
       "hpnicfEntityExtPowerPhysicalIndex": hpnicfEntityExtPowerPhysicalIndex,
       "hpnicfEntityExtNominalPower": hpnicfEntityExtNominalPower,
       "hpnicfEntityExtCurrentPower": hpnicfEntityExtCurrentPower,
       "hpnicfEntityExtAveragePower": hpnicfEntityExtAveragePower,
       "hpnicfEntityExtPeakPower": hpnicfEntityExtPeakPower,
       "hpnicfProcessObjects": hpnicfProcessObjects,
       "hpnicfProcessTable": hpnicfProcessTable,
       "hpnicfProcessEntry": hpnicfProcessEntry,
       "hpnicfProcessID": hpnicfProcessID,
       "hpnicfProcessName": hpnicfProcessName,
       "hpnicfProcessUtil5Min": hpnicfProcessUtil5Min,
       "hpnicfEntityExtTraps": hpnicfEntityExtTraps,
       "hpnicfEntityExtTrapsPrefix": hpnicfEntityExtTrapsPrefix,
       "hpnicfEntityExtTemperatureThresholdNotification": hpnicfEntityExtTemperatureThresholdNotification,
       "hpnicfEntityExtVoltageLowThresholdNotification": hpnicfEntityExtVoltageLowThresholdNotification,
       "hpnicfEntityExtVoltageHighThresholdNotification": hpnicfEntityExtVoltageHighThresholdNotification,
       "hpnicfEntityExtCpuUsageThresholdNotfication": hpnicfEntityExtCpuUsageThresholdNotfication,
       "hpnicfEntityExtMemUsageThresholdNotification": hpnicfEntityExtMemUsageThresholdNotification,
       "hpnicfEntityExtOperEnabled": hpnicfEntityExtOperEnabled,
       "hpnicfEntityExtOperDisabled": hpnicfEntityExtOperDisabled,
       "hpnicfEntityExtCriticalTemperatureThresholdNotification": hpnicfEntityExtCriticalTemperatureThresholdNotification,
       "hpnicfEntityExtSFPAlarmOn": hpnicfEntityExtSFPAlarmOn,
       "hpnicfEntityExtSFPAlarmOff": hpnicfEntityExtSFPAlarmOff,
       "hpnicfEntityExtSFPPhony": hpnicfEntityExtSFPPhony,
       "hpnicfEntityInsert": hpnicfEntityInsert,
       "hpnicfEntityRemove": hpnicfEntityRemove,
       "hpnicfEntityExtForcedPowerOff": hpnicfEntityExtForcedPowerOff,
       "hpnicfEntityExtForcedPowerOn": hpnicfEntityExtForcedPowerOn,
       "hpnicfEntityExtFaultAlarmOn": hpnicfEntityExtFaultAlarmOn,
       "hpnicfEntityExtFaultAlarmOff": hpnicfEntityExtFaultAlarmOff,
       "hpnicfEntityExtResourceLack": hpnicfEntityExtResourceLack,
       "hpnicfEntityExtResourceEnough": hpnicfEntityExtResourceEnough,
       "hpnicfEntityExtTemperatureLower": hpnicfEntityExtTemperatureLower,
       "hpnicfEntityExtTemperatureTooUp": hpnicfEntityExtTemperatureTooUp,
       "hpnicfEntityExtTemperatureNormal": hpnicfEntityExtTemperatureNormal,
       "hpnicfEntityExternalAlarmOccur": hpnicfEntityExternalAlarmOccur,
       "hpnicfEntityExternalAlarmRecover": hpnicfEntityExternalAlarmRecover,
       "hpnicfEntityExtCpuUsageThresholdRecover": hpnicfEntityExtCpuUsageThresholdRecover,
       "hpnicfEntityExtMemUsageThresholdRecover": hpnicfEntityExtMemUsageThresholdRecover,
       "hpnicfEntityExtMemAllocatedFailed": hpnicfEntityExtMemAllocatedFailed,
       "hpnicfEntityExtECCParityAlarm": hpnicfEntityExtECCParityAlarm,
       "hpnicfEntityExtCritLowerTempThresholdNotification": hpnicfEntityExtCritLowerTempThresholdNotification,
       "hpnicfEntityExtTemperatureTooLow": hpnicfEntityExtTemperatureTooLow,
       "hpnicfEntityExtFanDirectionNotPreferred": hpnicfEntityExtFanDirectionNotPreferred,
       "hpnicfEntityExtFanDirectionNotAccord": hpnicfEntityExtFanDirectionNotAccord,
       "hpnicfEntityExtSFPInvalid": hpnicfEntityExtSFPInvalid,
       "hpnicfEntityExtSFPInvalidNow": hpnicfEntityExtSFPInvalidNow,
       "hpnicfEntityExtMemUsageThresholdOverTrap": hpnicfEntityExtMemUsageThresholdOverTrap,
       "hpnicfEntityExtMemUsageThresholdRecoverTrap": hpnicfEntityExtMemUsageThresholdRecoverTrap,
       "hpnicfEntityExtTrapsInfor": hpnicfEntityExtTrapsInfor,
       "hpnicfEntityExtTrapDescription": hpnicfEntityExtTrapDescription,
       "hpnicfEntityExtECCParityAlarmStatus": hpnicfEntityExtECCParityAlarmStatus,
       "hpnicfEntityExtSFPInvalidInDays": hpnicfEntityExtSFPInvalidInDays,
       "hpnicfEntityExtFirstTrapTime": hpnicfEntityExtFirstTrapTime,
       "hpnicfEntityExtConformance": hpnicfEntityExtConformance,
       "hpnicfEntityExtCompliances": hpnicfEntityExtCompliances,
       "hpnicfEntityExtCompliance": hpnicfEntityExtCompliance,
       "hpnicfEntityExtGroups": hpnicfEntityExtGroups,
       "hpnicfEntityExtGroup": hpnicfEntityExtGroup,
       "hpnicfEntityExtNotificationGroup": hpnicfEntityExtNotificationGroup,
       "hpnicfEntityExtManuGroup": hpnicfEntityExtManuGroup,
       "hpnicfEntityExtPowerGroup": hpnicfEntityExtPowerGroup}
)
