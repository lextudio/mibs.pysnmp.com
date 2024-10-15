# SNMP MIB module (HH3C-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ENTITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:04 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cEntityExtend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cAdminState(Integer32, TextualConvention):
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



class Hh3cOperState(Integer32, TextualConvention):
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



class Hh3cAlarmStatus(Bits, TextualConvention):
    status = "current"


class Hh3cStandbyStatus(Integer32, TextualConvention):
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

_Hh3cEntityExtObjects_ObjectIdentity = ObjectIdentity
hh3cEntityExtObjects = _Hh3cEntityExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1)
)
_Hh3cEntityExtState_ObjectIdentity = ObjectIdentity
hh3cEntityExtState = _Hh3cEntityExtState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1)
)
_Hh3cEntityExtStateTable_Object = MibTable
hh3cEntityExtStateTable = _Hh3cEntityExtStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEntityExtStateTable.setStatus("current")
_Hh3cEntityExtStateEntry_Object = MibTableRow
hh3cEntityExtStateEntry = _Hh3cEntityExtStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1)
)
hh3cEntityExtStateEntry.setIndexNames(
    (0, "HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cEntityExtStateEntry.setStatus("current")
_Hh3cEntityExtPhysicalIndex_Type = Integer32
_Hh3cEntityExtPhysicalIndex_Object = MibTableColumn
hh3cEntityExtPhysicalIndex = _Hh3cEntityExtPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 1),
    _Hh3cEntityExtPhysicalIndex_Type()
)
hh3cEntityExtPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtPhysicalIndex.setStatus("current")
_Hh3cEntityExtAdminStatus_Type = Hh3cAdminState
_Hh3cEntityExtAdminStatus_Object = MibTableColumn
hh3cEntityExtAdminStatus = _Hh3cEntityExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 2),
    _Hh3cEntityExtAdminStatus_Type()
)
hh3cEntityExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtAdminStatus.setStatus("current")
_Hh3cEntityExtOperStatus_Type = Hh3cOperState
_Hh3cEntityExtOperStatus_Object = MibTableColumn
hh3cEntityExtOperStatus = _Hh3cEntityExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 3),
    _Hh3cEntityExtOperStatus_Type()
)
hh3cEntityExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtOperStatus.setStatus("current")
_Hh3cEntityExtStandbyStatus_Type = Hh3cStandbyStatus
_Hh3cEntityExtStandbyStatus_Object = MibTableColumn
hh3cEntityExtStandbyStatus = _Hh3cEntityExtStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 4),
    _Hh3cEntityExtStandbyStatus_Type()
)
hh3cEntityExtStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtStandbyStatus.setStatus("current")
_Hh3cEntityExtAlarmLight_Type = Hh3cAlarmStatus
_Hh3cEntityExtAlarmLight_Object = MibTableColumn
hh3cEntityExtAlarmLight = _Hh3cEntityExtAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 5),
    _Hh3cEntityExtAlarmLight_Type()
)
hh3cEntityExtAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtAlarmLight.setStatus("current")


class _Hh3cEntityExtCpuUsage_Type(Integer32):
    """Custom type hh3cEntityExtCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuUsage_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuUsage_Object = MibTableColumn
hh3cEntityExtCpuUsage = _Hh3cEntityExtCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 6),
    _Hh3cEntityExtCpuUsage_Type()
)
hh3cEntityExtCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsage.setStatus("current")


class _Hh3cEntityExtCpuUsageThreshold_Type(Integer32):
    """Custom type hh3cEntityExtCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuUsageThreshold_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuUsageThreshold_Object = MibTableColumn
hh3cEntityExtCpuUsageThreshold = _Hh3cEntityExtCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 7),
    _Hh3cEntityExtCpuUsageThreshold_Type()
)
hh3cEntityExtCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageThreshold.setStatus("current")


class _Hh3cEntityExtMemUsage_Type(Integer32):
    """Custom type hh3cEntityExtMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtMemUsage_Type.__name__ = "Integer32"
_Hh3cEntityExtMemUsage_Object = MibTableColumn
hh3cEntityExtMemUsage = _Hh3cEntityExtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 8),
    _Hh3cEntityExtMemUsage_Type()
)
hh3cEntityExtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsage.setStatus("current")


class _Hh3cEntityExtMemUsageThreshold_Type(Integer32):
    """Custom type hh3cEntityExtMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtMemUsageThreshold_Type.__name__ = "Integer32"
_Hh3cEntityExtMemUsageThreshold_Object = MibTableColumn
hh3cEntityExtMemUsageThreshold = _Hh3cEntityExtMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 9),
    _Hh3cEntityExtMemUsageThreshold_Type()
)
hh3cEntityExtMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsageThreshold.setStatus("current")
_Hh3cEntityExtMemSize_Type = Unsigned32
_Hh3cEntityExtMemSize_Object = MibTableColumn
hh3cEntityExtMemSize = _Hh3cEntityExtMemSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 10),
    _Hh3cEntityExtMemSize_Type()
)
hh3cEntityExtMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEntityExtMemSize.setUnits("bytes")
_Hh3cEntityExtUpTime_Type = Integer32
_Hh3cEntityExtUpTime_Object = MibTableColumn
hh3cEntityExtUpTime = _Hh3cEntityExtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 11),
    _Hh3cEntityExtUpTime_Type()
)
hh3cEntityExtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEntityExtUpTime.setUnits("seconds")
_Hh3cEntityExtTemperature_Type = Integer32
_Hh3cEntityExtTemperature_Object = MibTableColumn
hh3cEntityExtTemperature = _Hh3cEntityExtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 12),
    _Hh3cEntityExtTemperature_Type()
)
hh3cEntityExtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtTemperature.setStatus("current")
_Hh3cEntityExtTemperatureThreshold_Type = Integer32
_Hh3cEntityExtTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtTemperatureThreshold = _Hh3cEntityExtTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 13),
    _Hh3cEntityExtTemperatureThreshold_Type()
)
hh3cEntityExtTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureThreshold.setStatus("current")
_Hh3cEntityExtVoltage_Type = Integer32
_Hh3cEntityExtVoltage_Object = MibTableColumn
hh3cEntityExtVoltage = _Hh3cEntityExtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 14),
    _Hh3cEntityExtVoltage_Type()
)
hh3cEntityExtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltage.setStatus("current")
_Hh3cEntityExtVoltageLowThreshold_Type = Integer32
_Hh3cEntityExtVoltageLowThreshold_Object = MibTableColumn
hh3cEntityExtVoltageLowThreshold = _Hh3cEntityExtVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 15),
    _Hh3cEntityExtVoltageLowThreshold_Type()
)
hh3cEntityExtVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageLowThreshold.setStatus("current")
_Hh3cEntityExtVoltageHighThreshold_Type = Integer32
_Hh3cEntityExtVoltageHighThreshold_Object = MibTableColumn
hh3cEntityExtVoltageHighThreshold = _Hh3cEntityExtVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 16),
    _Hh3cEntityExtVoltageHighThreshold_Type()
)
hh3cEntityExtVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageHighThreshold.setStatus("current")
_Hh3cEntityExtCriticalTemperatureThreshold_Type = Integer32
_Hh3cEntityExtCriticalTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtCriticalTemperatureThreshold = _Hh3cEntityExtCriticalTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 17),
    _Hh3cEntityExtCriticalTemperatureThreshold_Type()
)
hh3cEntityExtCriticalTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtCriticalTemperatureThreshold.setStatus("current")
_Hh3cEntityExtMacAddress_Type = MacAddress
_Hh3cEntityExtMacAddress_Object = MibTableColumn
hh3cEntityExtMacAddress = _Hh3cEntityExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 18),
    _Hh3cEntityExtMacAddress_Type()
)
hh3cEntityExtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMacAddress.setStatus("current")


class _Hh3cEntityExtErrorStatus_Type(Integer32):
    """Custom type hh3cEntityExtErrorStatus based on Integer32"""
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


_Hh3cEntityExtErrorStatus_Type.__name__ = "Integer32"
_Hh3cEntityExtErrorStatus_Object = MibTableColumn
hh3cEntityExtErrorStatus = _Hh3cEntityExtErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 19),
    _Hh3cEntityExtErrorStatus_Type()
)
hh3cEntityExtErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtErrorStatus.setStatus("current")


class _Hh3cEntityExtCpuMaxUsage_Type(Integer32):
    """Custom type hh3cEntityExtCpuMaxUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuMaxUsage_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuMaxUsage_Object = MibTableColumn
hh3cEntityExtCpuMaxUsage = _Hh3cEntityExtCpuMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 20),
    _Hh3cEntityExtCpuMaxUsage_Type()
)
hh3cEntityExtCpuMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuMaxUsage.setStatus("current")
_Hh3cEntityExtLowerTemperatureThreshold_Type = Integer32
_Hh3cEntityExtLowerTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtLowerTemperatureThreshold = _Hh3cEntityExtLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 21),
    _Hh3cEntityExtLowerTemperatureThreshold_Type()
)
hh3cEntityExtLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtLowerTemperatureThreshold.setStatus("current")
_Hh3cEntityExtShutdownTemperatureThreshold_Type = Integer32
_Hh3cEntityExtShutdownTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtShutdownTemperatureThreshold = _Hh3cEntityExtShutdownTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 22),
    _Hh3cEntityExtShutdownTemperatureThreshold_Type()
)
hh3cEntityExtShutdownTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtShutdownTemperatureThreshold.setStatus("current")
_Hh3cEntityExtPhyMemSize_Type = Unsigned32
_Hh3cEntityExtPhyMemSize_Object = MibTableColumn
hh3cEntityExtPhyMemSize = _Hh3cEntityExtPhyMemSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 23),
    _Hh3cEntityExtPhyMemSize_Type()
)
hh3cEntityExtPhyMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtPhyMemSize.setStatus("current")
_Hh3cEntityExtPhyCpuFrequency_Type = Integer32
_Hh3cEntityExtPhyCpuFrequency_Object = MibTableColumn
hh3cEntityExtPhyCpuFrequency = _Hh3cEntityExtPhyCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 24),
    _Hh3cEntityExtPhyCpuFrequency_Type()
)
hh3cEntityExtPhyCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtPhyCpuFrequency.setStatus("current")


class _Hh3cEntityExtFirstUsedDate_Type(DateAndTime):
    """Custom type hh3cEntityExtFirstUsedDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cEntityExtFirstUsedDate_Type.__name__ = "DateAndTime"
_Hh3cEntityExtFirstUsedDate_Object = MibTableColumn
hh3cEntityExtFirstUsedDate = _Hh3cEntityExtFirstUsedDate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 25),
    _Hh3cEntityExtFirstUsedDate_Type()
)
hh3cEntityExtFirstUsedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtFirstUsedDate.setStatus("current")


class _Hh3cEntityExtCpuAvgUsage_Type(Integer32):
    """Custom type hh3cEntityExtCpuAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuAvgUsage_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuAvgUsage_Object = MibTableColumn
hh3cEntityExtCpuAvgUsage = _Hh3cEntityExtCpuAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 26),
    _Hh3cEntityExtCpuAvgUsage_Type()
)
hh3cEntityExtCpuAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuAvgUsage.setStatus("current")


class _Hh3cEntityExtMemAvgUsage_Type(Integer32):
    """Custom type hh3cEntityExtMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtMemAvgUsage_Type.__name__ = "Integer32"
_Hh3cEntityExtMemAvgUsage_Object = MibTableColumn
hh3cEntityExtMemAvgUsage = _Hh3cEntityExtMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 27),
    _Hh3cEntityExtMemAvgUsage_Type()
)
hh3cEntityExtMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMemAvgUsage.setStatus("current")


class _Hh3cEntityExtMemType_Type(OctetString):
    """Custom type hh3cEntityExtMemType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cEntityExtMemType_Type.__name__ = "OctetString"
_Hh3cEntityExtMemType_Object = MibTableColumn
hh3cEntityExtMemType = _Hh3cEntityExtMemType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 28),
    _Hh3cEntityExtMemType_Type()
)
hh3cEntityExtMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMemType.setStatus("current")
_Hh3cEntityExtCriticalLowerTemperatureThreshold_Type = Integer32
_Hh3cEntityExtCriticalLowerTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtCriticalLowerTemperatureThreshold = _Hh3cEntityExtCriticalLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 29),
    _Hh3cEntityExtCriticalLowerTemperatureThreshold_Type()
)
hh3cEntityExtCriticalLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtCriticalLowerTemperatureThreshold.setStatus("current")
_Hh3cEntityExtShutdownLowerTemperatureThreshold_Type = Integer32
_Hh3cEntityExtShutdownLowerTemperatureThreshold_Object = MibTableColumn
hh3cEntityExtShutdownLowerTemperatureThreshold = _Hh3cEntityExtShutdownLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 30),
    _Hh3cEntityExtShutdownLowerTemperatureThreshold_Type()
)
hh3cEntityExtShutdownLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtShutdownLowerTemperatureThreshold.setStatus("current")


class _Hh3cEntityExtCpuUsageRecoverThreshold_Type(Integer32):
    """Custom type hh3cEntityExtCpuUsageRecoverThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuUsageRecoverThreshold_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuUsageRecoverThreshold_Object = MibTableColumn
hh3cEntityExtCpuUsageRecoverThreshold = _Hh3cEntityExtCpuUsageRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 31),
    _Hh3cEntityExtCpuUsageRecoverThreshold_Type()
)
hh3cEntityExtCpuUsageRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageRecoverThreshold.setStatus("current")
_Hh3cEntityExtMemSizeRev_Type = CounterBasedGauge64
_Hh3cEntityExtMemSizeRev_Object = MibTableColumn
hh3cEntityExtMemSizeRev = _Hh3cEntityExtMemSizeRev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 32),
    _Hh3cEntityExtMemSizeRev_Type()
)
hh3cEntityExtMemSizeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMemSizeRev.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEntityExtMemSizeRev.setUnits("bytes")


class _Hh3cEntityExtCpuUsageIn1Minute_Type(Integer32):
    """Custom type hh3cEntityExtCpuUsageIn1Minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuUsageIn1Minute_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuUsageIn1Minute_Object = MibTableColumn
hh3cEntityExtCpuUsageIn1Minute = _Hh3cEntityExtCpuUsageIn1Minute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 33),
    _Hh3cEntityExtCpuUsageIn1Minute_Type()
)
hh3cEntityExtCpuUsageIn1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageIn1Minute.setStatus("current")


class _Hh3cEntityExtCpuUsageIn5Minutes_Type(Integer32):
    """Custom type hh3cEntityExtCpuUsageIn5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cEntityExtCpuUsageIn5Minutes_Type.__name__ = "Integer32"
_Hh3cEntityExtCpuUsageIn5Minutes_Object = MibTableColumn
hh3cEntityExtCpuUsageIn5Minutes = _Hh3cEntityExtCpuUsageIn5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 1, 1, 1, 34),
    _Hh3cEntityExtCpuUsageIn5Minutes_Type()
)
hh3cEntityExtCpuUsageIn5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageIn5Minutes.setStatus("current")
_Hh3cEntityExtManu_ObjectIdentity = ObjectIdentity
hh3cEntityExtManu = _Hh3cEntityExtManu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2)
)
_Hh3cEntityExtManuTable_Object = MibTable
hh3cEntityExtManuTable = _Hh3cEntityExtManuTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEntityExtManuTable.setStatus("current")
_Hh3cEntityExtManuEntry_Object = MibTableRow
hh3cEntityExtManuEntry = _Hh3cEntityExtManuEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1)
)
hh3cEntityExtManuEntry.setIndexNames(
    (0, "HH3C-ENTITY-EXT-MIB", "hh3cEntityExtManuPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cEntityExtManuEntry.setStatus("current")


class _Hh3cEntityExtManuPhysicalIndex_Type(Integer32):
    """Custom type hh3cEntityExtManuPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEntityExtManuPhysicalIndex_Type.__name__ = "Integer32"
_Hh3cEntityExtManuPhysicalIndex_Object = MibTableColumn
hh3cEntityExtManuPhysicalIndex = _Hh3cEntityExtManuPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1, 1),
    _Hh3cEntityExtManuPhysicalIndex_Type()
)
hh3cEntityExtManuPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtManuPhysicalIndex.setStatus("current")
_Hh3cEntityExtManuSerialNum_Type = SnmpAdminString
_Hh3cEntityExtManuSerialNum_Object = MibTableColumn
hh3cEntityExtManuSerialNum = _Hh3cEntityExtManuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1, 2),
    _Hh3cEntityExtManuSerialNum_Type()
)
hh3cEntityExtManuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtManuSerialNum.setStatus("current")
_Hh3cEntityExtManuBuildInfo_Type = SnmpAdminString
_Hh3cEntityExtManuBuildInfo_Object = MibTableColumn
hh3cEntityExtManuBuildInfo = _Hh3cEntityExtManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1, 3),
    _Hh3cEntityExtManuBuildInfo_Type()
)
hh3cEntityExtManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtManuBuildInfo.setStatus("current")
_Hh3cEntityExtManuBOM_Type = SnmpAdminString
_Hh3cEntityExtManuBOM_Object = MibTableColumn
hh3cEntityExtManuBOM = _Hh3cEntityExtManuBOM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1, 4),
    _Hh3cEntityExtManuBOM_Type()
)
hh3cEntityExtManuBOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtManuBOM.setStatus("current")
_Hh3cEntityExtMacAddressCount_Type = Unsigned32
_Hh3cEntityExtMacAddressCount_Object = MibTableColumn
hh3cEntityExtMacAddressCount = _Hh3cEntityExtMacAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 2, 1, 1, 5),
    _Hh3cEntityExtMacAddressCount_Type()
)
hh3cEntityExtMacAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtMacAddressCount.setStatus("current")
_Hh3cEntityExtPower_ObjectIdentity = ObjectIdentity
hh3cEntityExtPower = _Hh3cEntityExtPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3)
)
_Hh3cEntityExtPowerTable_Object = MibTable
hh3cEntityExtPowerTable = _Hh3cEntityExtPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cEntityExtPowerTable.setStatus("current")
_Hh3cEntityExtPowerEntry_Object = MibTableRow
hh3cEntityExtPowerEntry = _Hh3cEntityExtPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1)
)
hh3cEntityExtPowerEntry.setIndexNames(
    (0, "HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPowerPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cEntityExtPowerEntry.setStatus("current")


class _Hh3cEntityExtPowerPhysicalIndex_Type(Integer32):
    """Custom type hh3cEntityExtPowerPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEntityExtPowerPhysicalIndex_Type.__name__ = "Integer32"
_Hh3cEntityExtPowerPhysicalIndex_Object = MibTableColumn
hh3cEntityExtPowerPhysicalIndex = _Hh3cEntityExtPowerPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1, 1),
    _Hh3cEntityExtPowerPhysicalIndex_Type()
)
hh3cEntityExtPowerPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtPowerPhysicalIndex.setStatus("current")
_Hh3cEntityExtNominalPower_Type = Gauge32
_Hh3cEntityExtNominalPower_Object = MibTableColumn
hh3cEntityExtNominalPower = _Hh3cEntityExtNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1, 2),
    _Hh3cEntityExtNominalPower_Type()
)
hh3cEntityExtNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtNominalPower.setStatus("current")
_Hh3cEntityExtCurrentPower_Type = Gauge32
_Hh3cEntityExtCurrentPower_Object = MibTableColumn
hh3cEntityExtCurrentPower = _Hh3cEntityExtCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1, 3),
    _Hh3cEntityExtCurrentPower_Type()
)
hh3cEntityExtCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCurrentPower.setStatus("current")
_Hh3cEntityExtAveragePower_Type = Integer32
_Hh3cEntityExtAveragePower_Object = MibTableColumn
hh3cEntityExtAveragePower = _Hh3cEntityExtAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1, 4),
    _Hh3cEntityExtAveragePower_Type()
)
hh3cEntityExtAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtAveragePower.setStatus("current")
_Hh3cEntityExtPeakPower_Type = Integer32
_Hh3cEntityExtPeakPower_Object = MibTableColumn
hh3cEntityExtPeakPower = _Hh3cEntityExtPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 3, 1, 1, 5),
    _Hh3cEntityExtPeakPower_Type()
)
hh3cEntityExtPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEntityExtPeakPower.setStatus("current")
_Hh3cProcessObjects_ObjectIdentity = ObjectIdentity
hh3cProcessObjects = _Hh3cProcessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4)
)
_Hh3cProcessTable_Object = MibTable
hh3cProcessTable = _Hh3cProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cProcessTable.setStatus("current")
_Hh3cProcessEntry_Object = MibTableRow
hh3cProcessEntry = _Hh3cProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4, 1, 1)
)
hh3cProcessEntry.setIndexNames(
    (0, "HH3C-ENTITY-EXT-MIB", "hh3cProcessID"),
)
if mibBuilder.loadTexts:
    hh3cProcessEntry.setStatus("current")
_Hh3cProcessID_Type = Unsigned32
_Hh3cProcessID_Object = MibTableColumn
hh3cProcessID = _Hh3cProcessID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4, 1, 1, 1),
    _Hh3cProcessID_Type()
)
hh3cProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProcessID.setStatus("current")


class _Hh3cProcessName_Type(DisplayString):
    """Custom type hh3cProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cProcessName_Type.__name__ = "DisplayString"
_Hh3cProcessName_Object = MibTableColumn
hh3cProcessName = _Hh3cProcessName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4, 1, 1, 2),
    _Hh3cProcessName_Type()
)
hh3cProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProcessName.setStatus("current")


class _Hh3cProcessUtil5Min_Type(Unsigned32):
    """Custom type hh3cProcessUtil5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cProcessUtil5Min_Type.__name__ = "Unsigned32"
_Hh3cProcessUtil5Min_Object = MibTableColumn
hh3cProcessUtil5Min = _Hh3cProcessUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 4, 1, 1, 3),
    _Hh3cProcessUtil5Min_Type()
)
hh3cProcessUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cProcessUtil5Min.setStatus("current")
_Hh3cEntityExtVoltageObjects_ObjectIdentity = ObjectIdentity
hh3cEntityExtVoltageObjects = _Hh3cEntityExtVoltageObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5)
)
_Hh3cEntityExtVoltageTable_Object = MibTable
hh3cEntityExtVoltageTable = _Hh3cEntityExtVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageTable.setStatus("current")
_Hh3cEntityExtVoltageEntry_Object = MibTableRow
hh3cEntityExtVoltageEntry = _Hh3cEntityExtVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1)
)
hh3cEntityExtVoltageEntry.setIndexNames(
    (0, "HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageEntry.setStatus("current")
_Hh3cEntityExtCurrentVoltage_Type = Integer32
_Hh3cEntityExtCurrentVoltage_Object = MibTableColumn
hh3cEntityExtCurrentVoltage = _Hh3cEntityExtCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 1),
    _Hh3cEntityExtCurrentVoltage_Type()
)
hh3cEntityExtCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtCurrentVoltage.setStatus("current")
_Hh3cEntityExtNominalVoltage_Type = Integer32
_Hh3cEntityExtNominalVoltage_Object = MibTableColumn
hh3cEntityExtNominalVoltage = _Hh3cEntityExtNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 2),
    _Hh3cEntityExtNominalVoltage_Type()
)
hh3cEntityExtNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtNominalVoltage.setStatus("current")


class _Hh3cEntityExtVoltageState_Type(Integer32):
    """Custom type hh3cEntityExtVoltageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("normal", 0),
          ("tooHigh", 4),
          ("tooLow", 2))
    )


_Hh3cEntityExtVoltageState_Type.__name__ = "Integer32"
_Hh3cEntityExtVoltageState_Object = MibTableColumn
hh3cEntityExtVoltageState = _Hh3cEntityExtVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 3),
    _Hh3cEntityExtVoltageState_Type()
)
hh3cEntityExtVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageState.setStatus("current")
_Hh3cEntityExtVoltageMajorLowThreshold_Type = Integer32
_Hh3cEntityExtVoltageMajorLowThreshold_Object = MibTableColumn
hh3cEntityExtVoltageMajorLowThreshold = _Hh3cEntityExtVoltageMajorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 4),
    _Hh3cEntityExtVoltageMajorLowThreshold_Type()
)
hh3cEntityExtVoltageMajorLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageMajorLowThreshold.setStatus("current")
_Hh3cEntityExtVoltageFatalLowThreshold_Type = Integer32
_Hh3cEntityExtVoltageFatalLowThreshold_Object = MibTableColumn
hh3cEntityExtVoltageFatalLowThreshold = _Hh3cEntityExtVoltageFatalLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 5),
    _Hh3cEntityExtVoltageFatalLowThreshold_Type()
)
hh3cEntityExtVoltageFatalLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageFatalLowThreshold.setStatus("current")
_Hh3cEntityExtVoltageMajorHighThreshold_Type = Integer32
_Hh3cEntityExtVoltageMajorHighThreshold_Object = MibTableColumn
hh3cEntityExtVoltageMajorHighThreshold = _Hh3cEntityExtVoltageMajorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 6),
    _Hh3cEntityExtVoltageMajorHighThreshold_Type()
)
hh3cEntityExtVoltageMajorHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageMajorHighThreshold.setStatus("current")
_Hh3cEntityExtVoltageFatalHighThreshold_Type = Integer32
_Hh3cEntityExtVoltageFatalHighThreshold_Object = MibTableColumn
hh3cEntityExtVoltageFatalHighThreshold = _Hh3cEntityExtVoltageFatalHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 1, 5, 1, 1, 7),
    _Hh3cEntityExtVoltageFatalHighThreshold_Type()
)
hh3cEntityExtVoltageFatalHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageFatalHighThreshold.setStatus("current")
_Hh3cEntityExtTraps_ObjectIdentity = ObjectIdentity
hh3cEntityExtTraps = _Hh3cEntityExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2)
)
_Hh3cEntityExtTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cEntityExtTrapsPrefix = _Hh3cEntityExtTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0)
)
_Hh3cEntityExtTrapsInfor_ObjectIdentity = ObjectIdentity
hh3cEntityExtTrapsInfor = _Hh3cEntityExtTrapsInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 1)
)


class _Hh3cEntityExtTrapDescription_Type(SnmpAdminString):
    """Custom type hh3cEntityExtTrapDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEntityExtTrapDescription_Type.__name__ = "SnmpAdminString"
_Hh3cEntityExtTrapDescription_Object = MibScalar
hh3cEntityExtTrapDescription = _Hh3cEntityExtTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 1, 1),
    _Hh3cEntityExtTrapDescription_Type()
)
hh3cEntityExtTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtTrapDescription.setStatus("current")


class _Hh3cEntityExtECCParityAlarmStatus_Type(Integer32):
    """Custom type hh3cEntityExtECCParityAlarmStatus based on Integer32"""
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


_Hh3cEntityExtECCParityAlarmStatus_Type.__name__ = "Integer32"
_Hh3cEntityExtECCParityAlarmStatus_Object = MibScalar
hh3cEntityExtECCParityAlarmStatus = _Hh3cEntityExtECCParityAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 1, 2),
    _Hh3cEntityExtECCParityAlarmStatus_Type()
)
hh3cEntityExtECCParityAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtECCParityAlarmStatus.setStatus("current")
_Hh3cEntityExtSFPInvalidInDays_Type = Integer32
_Hh3cEntityExtSFPInvalidInDays_Object = MibScalar
hh3cEntityExtSFPInvalidInDays = _Hh3cEntityExtSFPInvalidInDays_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 1, 3),
    _Hh3cEntityExtSFPInvalidInDays_Type()
)
hh3cEntityExtSFPInvalidInDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtSFPInvalidInDays.setStatus("current")
_Hh3cEntityExtFirstTrapTime_Type = TimeTicks
_Hh3cEntityExtFirstTrapTime_Object = MibScalar
hh3cEntityExtFirstTrapTime = _Hh3cEntityExtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 1, 4),
    _Hh3cEntityExtFirstTrapTime_Type()
)
hh3cEntityExtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEntityExtFirstTrapTime.setStatus("current")
_Hh3cEntityExtConformance_ObjectIdentity = ObjectIdentity
hh3cEntityExtConformance = _Hh3cEntityExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3)
)
_Hh3cEntityExtCompliances_ObjectIdentity = ObjectIdentity
hh3cEntityExtCompliances = _Hh3cEntityExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 1)
)
_Hh3cEntityExtGroups_ObjectIdentity = ObjectIdentity
hh3cEntityExtGroups = _Hh3cEntityExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 2)
)

# Managed Objects groups

hh3cEntityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 2, 1)
)
hh3cEntityExtGroup.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtStandbyStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSize"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtUpTime"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageLowThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageHighThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMacAddress"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtErrorStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuMaxUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtLowerTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhyMemSize"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhyCpuFrequency"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFirstUsedDate"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuAvgUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemAvgUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemType"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalLowerTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownLowerTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageRecoverThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSizeRev"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageIn1Minute"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageIn5Minutes"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtGroup.setStatus("current")

hh3cEntityExtManuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 2, 3)
)
hh3cEntityExtManuGroup.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtManuPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtManuSerialNum"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtManuBuildInfo"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtManuBOM"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMacAddressCount"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtManuGroup.setStatus("current")

hh3cEntityExtPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 2, 4)
)
hh3cEntityExtPowerGroup.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPowerPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalPower"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentPower"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAveragePower"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPeakPower"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtPowerGroup.setStatus("current")


# Notification objects

hh3cEntityExtTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 1)
)
hh3cEntityExtTemperatureThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 2)
)
hh3cEntityExtVoltageLowThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageLowThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 3)
)
hh3cEntityExtVoltageHighThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageHighThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtCpuUsageThresholdNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 4)
)
hh3cEntityExtCpuUsageThresholdNotfication.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageRecoverThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageThresholdNotfication.setStatus(
        "current"
    )

hh3cEntityExtMemUsageThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 5)
)
hh3cEntityExtMemUsageThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSize"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsageThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtOperEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 6)
)
hh3cEntityExtOperEnabled.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtOperEnabled.setStatus(
        "current"
    )

hh3cEntityExtOperDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 7)
)
hh3cEntityExtOperDisabled.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtOperDisabled.setStatus(
        "current"
    )

hh3cEntityExtCriticalTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 8)
)
hh3cEntityExtCriticalTemperatureThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtCriticalTemperatureThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtSFPAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 9)
)
hh3cEntityExtSFPAlarmOn.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtErrorStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtSFPAlarmOn.setStatus(
        "current"
    )

hh3cEntityExtSFPAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 10)
)
hh3cEntityExtSFPAlarmOff.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtErrorStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtSFPAlarmOff.setStatus(
        "current"
    )

hh3cEntityExtSFPPhony = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 11)
)
hh3cEntityExtSFPPhony.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtSFPPhony.setStatus(
        "current"
    )

hh3cEntityInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 12)
)
hh3cEntityInsert.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cEntityInsert.setStatus(
        "current"
    )

hh3cEntityRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 13)
)
hh3cEntityRemove.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cEntityRemove.setStatus(
        "current"
    )

hh3cEntityExtForcedPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 14)
)
hh3cEntityExtForcedPowerOff.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtForcedPowerOff.setStatus(
        "current"
    )

hh3cEntityExtForcedPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 15)
)
hh3cEntityExtForcedPowerOn.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtForcedPowerOn.setStatus(
        "current"
    )

hh3cEntityExtFaultAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 16)
)
hh3cEntityExtFaultAlarmOn.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtErrorStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtFaultAlarmOn.setStatus(
        "current"
    )

hh3cEntityExtFaultAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 17)
)
hh3cEntityExtFaultAlarmOff.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtErrorStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtFaultAlarmOff.setStatus(
        "current"
    )

hh3cEntityExtResourceLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 18)
)
hh3cEntityExtResourceLack.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtResourceLack.setStatus(
        "current"
    )

hh3cEntityExtResourceEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 19)
)
hh3cEntityExtResourceEnough.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtResourceEnough.setStatus(
        "current"
    )

hh3cEntityExtTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 20)
)
hh3cEntityExtTemperatureLower.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtLowerTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureLower.setStatus(
        "current"
    )

hh3cEntityExtTemperatureTooUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 21)
)
hh3cEntityExtTemperatureTooUp.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureTooUp.setStatus(
        "current"
    )

hh3cEntityExtTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 22)
)
hh3cEntityExtTemperatureNormal.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtLowerTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureNormal.setStatus(
        "current"
    )

hh3cEntityExternalAlarmOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 23)
)
hh3cEntityExternalAlarmOccur.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExternalAlarmOccur.setStatus(
        "current"
    )

hh3cEntityExternalAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 24)
)
hh3cEntityExternalAlarmRecover.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExternalAlarmRecover.setStatus(
        "current"
    )

hh3cEntityExtCpuUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 25)
)
hh3cEntityExtCpuUsageThresholdRecover.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageRecoverThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtCpuUsageThresholdRecover.setStatus(
        "current"
    )

hh3cEntityExtMemUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 26)
)
hh3cEntityExtMemUsageThresholdRecover.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSize"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsageThresholdRecover.setStatus(
        "current"
    )

hh3cEntityExtMemAllocatedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 27)
)
hh3cEntityExtMemAllocatedFailed.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtMemAllocatedFailed.setStatus(
        "current"
    )

hh3cEntityExtECCParityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 28)
)
hh3cEntityExtECCParityAlarm.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtECCParityAlarmStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtECCParityAlarm.setStatus(
        "current"
    )

hh3cEntityExtCritLowerTempThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 29)
)
hh3cEntityExtCritLowerTempThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtCritLowerTempThresholdNotification.setStatus(
        "current"
    )

hh3cEntityExtTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 30)
)
hh3cEntityExtTemperatureTooLow.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtTemperatureTooLow.setStatus(
        "current"
    )

hh3cEntityExtFanDirectionNotPreferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 31)
)
hh3cEntityExtFanDirectionNotPreferred.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtFanDirectionNotPreferred.setStatus(
        "current"
    )

hh3cEntityExtFanDirectionNotAccord = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 32)
)
hh3cEntityExtFanDirectionNotAccord.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtFanDirectionNotAccord.setStatus(
        "current"
    )

hh3cEntityExtSFPInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 33)
)
hh3cEntityExtSFPInvalid.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPInvalidInDays"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtSFPInvalid.setStatus(
        "current"
    )

hh3cEntityExtSFPInvalidNow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 34)
)
hh3cEntityExtSFPInvalidNow.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtSFPInvalidNow.setStatus(
        "current"
    )

hh3cEntityExtMemUsageThresholdOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 35)
)
hh3cEntityExtMemUsageThresholdOverTrap.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSizeRev"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsageThresholdOverTrap.setStatus(
        "current"
    )

hh3cEntityExtMemUsageThresholdRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 36)
)
hh3cEntityExtMemUsageThresholdRecoverTrap.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemSizeRev"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAdminStatus"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtMemUsageThresholdRecoverTrap.setStatus(
        "current"
    )

hh3cEntityExtVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 37)
)
hh3cEntityExtVoltageNormal.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageMajorLowThreshold"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageMajorHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageNormal.setStatus(
        "current"
    )

hh3cEntityExtVoltageLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 38)
)
hh3cEntityExtVoltageLower.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageMajorLowThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageLower.setStatus(
        "current"
    )

hh3cEntityExtVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 39)
)
hh3cEntityExtVoltageTooLow.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageFatalLowThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageTooLow.setStatus(
        "current"
    )

hh3cEntityExtVoltageHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 40)
)
hh3cEntityExtVoltageHigher.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageMajorHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageHigher.setStatus(
        "current"
    )

hh3cEntityExtVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 2, 0, 41)
)
hh3cEntityExtVoltageTooHigh.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCurrentVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtNominalVoltage"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageFatalHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtVoltageTooHigh.setStatus(
        "current"
    )


# Notifications groups

hh3cEntityExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 2, 2)
)
hh3cEntityExtNotificationGroup.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageLowThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageHighThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageThresholdNotfication"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperEnabled"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperDisabled"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalTemperatureThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPAlarmOn"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPAlarmOff"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPPhony"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityInsert"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityRemove"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtForcedPowerOff"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtForcedPowerOn"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFaultAlarmOn"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFaultAlarmOff"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtResourceLack"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtResourceEnough"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureLower"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureTooUp"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureNormal"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExternalAlarmOccur"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExternalAlarmRecover"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCpuUsageThresholdRecover"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThresholdRecover"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemAllocatedFailed"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtECCParityAlarm"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCritLowerTempThresholdNotification"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperatureTooLow"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFanDirectionNotPreferred"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtFanDirectionNotAccord"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPInvalid"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtSFPInvalidNow"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThresholdOverTrap"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtMemUsageThresholdRecoverTrap"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageNormal"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageTooLow"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageLower"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageHigher"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtVoltageTooHigh"))
)
if mibBuilder.loadTexts:
    hh3cEntityExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cEntityExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEntityExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ENTITY-EXT-MIB",
    **{"Hh3cAdminState": Hh3cAdminState,
       "Hh3cOperState": Hh3cOperState,
       "Hh3cAlarmStatus": Hh3cAlarmStatus,
       "Hh3cStandbyStatus": Hh3cStandbyStatus,
       "hh3cEntityExtend": hh3cEntityExtend,
       "hh3cEntityExtObjects": hh3cEntityExtObjects,
       "hh3cEntityExtState": hh3cEntityExtState,
       "hh3cEntityExtStateTable": hh3cEntityExtStateTable,
       "hh3cEntityExtStateEntry": hh3cEntityExtStateEntry,
       "hh3cEntityExtPhysicalIndex": hh3cEntityExtPhysicalIndex,
       "hh3cEntityExtAdminStatus": hh3cEntityExtAdminStatus,
       "hh3cEntityExtOperStatus": hh3cEntityExtOperStatus,
       "hh3cEntityExtStandbyStatus": hh3cEntityExtStandbyStatus,
       "hh3cEntityExtAlarmLight": hh3cEntityExtAlarmLight,
       "hh3cEntityExtCpuUsage": hh3cEntityExtCpuUsage,
       "hh3cEntityExtCpuUsageThreshold": hh3cEntityExtCpuUsageThreshold,
       "hh3cEntityExtMemUsage": hh3cEntityExtMemUsage,
       "hh3cEntityExtMemUsageThreshold": hh3cEntityExtMemUsageThreshold,
       "hh3cEntityExtMemSize": hh3cEntityExtMemSize,
       "hh3cEntityExtUpTime": hh3cEntityExtUpTime,
       "hh3cEntityExtTemperature": hh3cEntityExtTemperature,
       "hh3cEntityExtTemperatureThreshold": hh3cEntityExtTemperatureThreshold,
       "hh3cEntityExtVoltage": hh3cEntityExtVoltage,
       "hh3cEntityExtVoltageLowThreshold": hh3cEntityExtVoltageLowThreshold,
       "hh3cEntityExtVoltageHighThreshold": hh3cEntityExtVoltageHighThreshold,
       "hh3cEntityExtCriticalTemperatureThreshold": hh3cEntityExtCriticalTemperatureThreshold,
       "hh3cEntityExtMacAddress": hh3cEntityExtMacAddress,
       "hh3cEntityExtErrorStatus": hh3cEntityExtErrorStatus,
       "hh3cEntityExtCpuMaxUsage": hh3cEntityExtCpuMaxUsage,
       "hh3cEntityExtLowerTemperatureThreshold": hh3cEntityExtLowerTemperatureThreshold,
       "hh3cEntityExtShutdownTemperatureThreshold": hh3cEntityExtShutdownTemperatureThreshold,
       "hh3cEntityExtPhyMemSize": hh3cEntityExtPhyMemSize,
       "hh3cEntityExtPhyCpuFrequency": hh3cEntityExtPhyCpuFrequency,
       "hh3cEntityExtFirstUsedDate": hh3cEntityExtFirstUsedDate,
       "hh3cEntityExtCpuAvgUsage": hh3cEntityExtCpuAvgUsage,
       "hh3cEntityExtMemAvgUsage": hh3cEntityExtMemAvgUsage,
       "hh3cEntityExtMemType": hh3cEntityExtMemType,
       "hh3cEntityExtCriticalLowerTemperatureThreshold": hh3cEntityExtCriticalLowerTemperatureThreshold,
       "hh3cEntityExtShutdownLowerTemperatureThreshold": hh3cEntityExtShutdownLowerTemperatureThreshold,
       "hh3cEntityExtCpuUsageRecoverThreshold": hh3cEntityExtCpuUsageRecoverThreshold,
       "hh3cEntityExtMemSizeRev": hh3cEntityExtMemSizeRev,
       "hh3cEntityExtCpuUsageIn1Minute": hh3cEntityExtCpuUsageIn1Minute,
       "hh3cEntityExtCpuUsageIn5Minutes": hh3cEntityExtCpuUsageIn5Minutes,
       "hh3cEntityExtManu": hh3cEntityExtManu,
       "hh3cEntityExtManuTable": hh3cEntityExtManuTable,
       "hh3cEntityExtManuEntry": hh3cEntityExtManuEntry,
       "hh3cEntityExtManuPhysicalIndex": hh3cEntityExtManuPhysicalIndex,
       "hh3cEntityExtManuSerialNum": hh3cEntityExtManuSerialNum,
       "hh3cEntityExtManuBuildInfo": hh3cEntityExtManuBuildInfo,
       "hh3cEntityExtManuBOM": hh3cEntityExtManuBOM,
       "hh3cEntityExtMacAddressCount": hh3cEntityExtMacAddressCount,
       "hh3cEntityExtPower": hh3cEntityExtPower,
       "hh3cEntityExtPowerTable": hh3cEntityExtPowerTable,
       "hh3cEntityExtPowerEntry": hh3cEntityExtPowerEntry,
       "hh3cEntityExtPowerPhysicalIndex": hh3cEntityExtPowerPhysicalIndex,
       "hh3cEntityExtNominalPower": hh3cEntityExtNominalPower,
       "hh3cEntityExtCurrentPower": hh3cEntityExtCurrentPower,
       "hh3cEntityExtAveragePower": hh3cEntityExtAveragePower,
       "hh3cEntityExtPeakPower": hh3cEntityExtPeakPower,
       "hh3cProcessObjects": hh3cProcessObjects,
       "hh3cProcessTable": hh3cProcessTable,
       "hh3cProcessEntry": hh3cProcessEntry,
       "hh3cProcessID": hh3cProcessID,
       "hh3cProcessName": hh3cProcessName,
       "hh3cProcessUtil5Min": hh3cProcessUtil5Min,
       "hh3cEntityExtVoltageObjects": hh3cEntityExtVoltageObjects,
       "hh3cEntityExtVoltageTable": hh3cEntityExtVoltageTable,
       "hh3cEntityExtVoltageEntry": hh3cEntityExtVoltageEntry,
       "hh3cEntityExtCurrentVoltage": hh3cEntityExtCurrentVoltage,
       "hh3cEntityExtNominalVoltage": hh3cEntityExtNominalVoltage,
       "hh3cEntityExtVoltageState": hh3cEntityExtVoltageState,
       "hh3cEntityExtVoltageMajorLowThreshold": hh3cEntityExtVoltageMajorLowThreshold,
       "hh3cEntityExtVoltageFatalLowThreshold": hh3cEntityExtVoltageFatalLowThreshold,
       "hh3cEntityExtVoltageMajorHighThreshold": hh3cEntityExtVoltageMajorHighThreshold,
       "hh3cEntityExtVoltageFatalHighThreshold": hh3cEntityExtVoltageFatalHighThreshold,
       "hh3cEntityExtTraps": hh3cEntityExtTraps,
       "hh3cEntityExtTrapsPrefix": hh3cEntityExtTrapsPrefix,
       "hh3cEntityExtTemperatureThresholdNotification": hh3cEntityExtTemperatureThresholdNotification,
       "hh3cEntityExtVoltageLowThresholdNotification": hh3cEntityExtVoltageLowThresholdNotification,
       "hh3cEntityExtVoltageHighThresholdNotification": hh3cEntityExtVoltageHighThresholdNotification,
       "hh3cEntityExtCpuUsageThresholdNotfication": hh3cEntityExtCpuUsageThresholdNotfication,
       "hh3cEntityExtMemUsageThresholdNotification": hh3cEntityExtMemUsageThresholdNotification,
       "hh3cEntityExtOperEnabled": hh3cEntityExtOperEnabled,
       "hh3cEntityExtOperDisabled": hh3cEntityExtOperDisabled,
       "hh3cEntityExtCriticalTemperatureThresholdNotification": hh3cEntityExtCriticalTemperatureThresholdNotification,
       "hh3cEntityExtSFPAlarmOn": hh3cEntityExtSFPAlarmOn,
       "hh3cEntityExtSFPAlarmOff": hh3cEntityExtSFPAlarmOff,
       "hh3cEntityExtSFPPhony": hh3cEntityExtSFPPhony,
       "hh3cEntityInsert": hh3cEntityInsert,
       "hh3cEntityRemove": hh3cEntityRemove,
       "hh3cEntityExtForcedPowerOff": hh3cEntityExtForcedPowerOff,
       "hh3cEntityExtForcedPowerOn": hh3cEntityExtForcedPowerOn,
       "hh3cEntityExtFaultAlarmOn": hh3cEntityExtFaultAlarmOn,
       "hh3cEntityExtFaultAlarmOff": hh3cEntityExtFaultAlarmOff,
       "hh3cEntityExtResourceLack": hh3cEntityExtResourceLack,
       "hh3cEntityExtResourceEnough": hh3cEntityExtResourceEnough,
       "hh3cEntityExtTemperatureLower": hh3cEntityExtTemperatureLower,
       "hh3cEntityExtTemperatureTooUp": hh3cEntityExtTemperatureTooUp,
       "hh3cEntityExtTemperatureNormal": hh3cEntityExtTemperatureNormal,
       "hh3cEntityExternalAlarmOccur": hh3cEntityExternalAlarmOccur,
       "hh3cEntityExternalAlarmRecover": hh3cEntityExternalAlarmRecover,
       "hh3cEntityExtCpuUsageThresholdRecover": hh3cEntityExtCpuUsageThresholdRecover,
       "hh3cEntityExtMemUsageThresholdRecover": hh3cEntityExtMemUsageThresholdRecover,
       "hh3cEntityExtMemAllocatedFailed": hh3cEntityExtMemAllocatedFailed,
       "hh3cEntityExtECCParityAlarm": hh3cEntityExtECCParityAlarm,
       "hh3cEntityExtCritLowerTempThresholdNotification": hh3cEntityExtCritLowerTempThresholdNotification,
       "hh3cEntityExtTemperatureTooLow": hh3cEntityExtTemperatureTooLow,
       "hh3cEntityExtFanDirectionNotPreferred": hh3cEntityExtFanDirectionNotPreferred,
       "hh3cEntityExtFanDirectionNotAccord": hh3cEntityExtFanDirectionNotAccord,
       "hh3cEntityExtSFPInvalid": hh3cEntityExtSFPInvalid,
       "hh3cEntityExtSFPInvalidNow": hh3cEntityExtSFPInvalidNow,
       "hh3cEntityExtMemUsageThresholdOverTrap": hh3cEntityExtMemUsageThresholdOverTrap,
       "hh3cEntityExtMemUsageThresholdRecoverTrap": hh3cEntityExtMemUsageThresholdRecoverTrap,
       "hh3cEntityExtVoltageNormal": hh3cEntityExtVoltageNormal,
       "hh3cEntityExtVoltageLower": hh3cEntityExtVoltageLower,
       "hh3cEntityExtVoltageTooLow": hh3cEntityExtVoltageTooLow,
       "hh3cEntityExtVoltageHigher": hh3cEntityExtVoltageHigher,
       "hh3cEntityExtVoltageTooHigh": hh3cEntityExtVoltageTooHigh,
       "hh3cEntityExtTrapsInfor": hh3cEntityExtTrapsInfor,
       "hh3cEntityExtTrapDescription": hh3cEntityExtTrapDescription,
       "hh3cEntityExtECCParityAlarmStatus": hh3cEntityExtECCParityAlarmStatus,
       "hh3cEntityExtSFPInvalidInDays": hh3cEntityExtSFPInvalidInDays,
       "hh3cEntityExtFirstTrapTime": hh3cEntityExtFirstTrapTime,
       "hh3cEntityExtConformance": hh3cEntityExtConformance,
       "hh3cEntityExtCompliances": hh3cEntityExtCompliances,
       "hh3cEntityExtCompliance": hh3cEntityExtCompliance,
       "hh3cEntityExtGroups": hh3cEntityExtGroups,
       "hh3cEntityExtGroup": hh3cEntityExtGroup,
       "hh3cEntityExtNotificationGroup": hh3cEntityExtNotificationGroup,
       "hh3cEntityExtManuGroup": hh3cEntityExtManuGroup,
       "hh3cEntityExtPowerGroup": hh3cEntityExtPowerGroup}
)
