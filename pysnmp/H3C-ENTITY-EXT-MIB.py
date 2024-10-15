# SNMP MIB module (H3C-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-ENTITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:24 2024
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
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalName")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cEntityExtend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cAdminState(Integer32, TextualConvention):
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



class H3cOperState(Integer32, TextualConvention):
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



class H3cAlarmStatus(Bits, TextualConvention):
    status = "current"


class H3cStandbyStatus(Integer32, TextualConvention):
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

_H3cEntityExtObjects_ObjectIdentity = ObjectIdentity
h3cEntityExtObjects = _H3cEntityExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1)
)
_H3cEntityExtState_ObjectIdentity = ObjectIdentity
h3cEntityExtState = _H3cEntityExtState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1)
)
_H3cEntityExtStateTable_Object = MibTable
h3cEntityExtStateTable = _H3cEntityExtStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEntityExtStateTable.setStatus("current")
_H3cEntityExtStateEntry_Object = MibTableRow
h3cEntityExtStateEntry = _H3cEntityExtStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1)
)
h3cEntityExtStateEntry.setIndexNames(
    (0, "H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cEntityExtStateEntry.setStatus("current")
_H3cEntityExtPhysicalIndex_Type = Integer32
_H3cEntityExtPhysicalIndex_Object = MibTableColumn
h3cEntityExtPhysicalIndex = _H3cEntityExtPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 1),
    _H3cEntityExtPhysicalIndex_Type()
)
h3cEntityExtPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtPhysicalIndex.setStatus("current")
_H3cEntityExtAdminStatus_Type = H3cAdminState
_H3cEntityExtAdminStatus_Object = MibTableColumn
h3cEntityExtAdminStatus = _H3cEntityExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 2),
    _H3cEntityExtAdminStatus_Type()
)
h3cEntityExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtAdminStatus.setStatus("current")
_H3cEntityExtOperStatus_Type = H3cOperState
_H3cEntityExtOperStatus_Object = MibTableColumn
h3cEntityExtOperStatus = _H3cEntityExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 3),
    _H3cEntityExtOperStatus_Type()
)
h3cEntityExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtOperStatus.setStatus("current")
_H3cEntityExtStandbyStatus_Type = H3cStandbyStatus
_H3cEntityExtStandbyStatus_Object = MibTableColumn
h3cEntityExtStandbyStatus = _H3cEntityExtStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 4),
    _H3cEntityExtStandbyStatus_Type()
)
h3cEntityExtStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtStandbyStatus.setStatus("current")
_H3cEntityExtAlarmLight_Type = H3cAlarmStatus
_H3cEntityExtAlarmLight_Object = MibTableColumn
h3cEntityExtAlarmLight = _H3cEntityExtAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 5),
    _H3cEntityExtAlarmLight_Type()
)
h3cEntityExtAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtAlarmLight.setStatus("current")


class _H3cEntityExtCpuUsage_Type(Integer32):
    """Custom type h3cEntityExtCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtCpuUsage_Type.__name__ = "Integer32"
_H3cEntityExtCpuUsage_Object = MibTableColumn
h3cEntityExtCpuUsage = _H3cEntityExtCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 6),
    _H3cEntityExtCpuUsage_Type()
)
h3cEntityExtCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtCpuUsage.setStatus("current")


class _H3cEntityExtCpuUsageThreshold_Type(Integer32):
    """Custom type h3cEntityExtCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtCpuUsageThreshold_Type.__name__ = "Integer32"
_H3cEntityExtCpuUsageThreshold_Object = MibTableColumn
h3cEntityExtCpuUsageThreshold = _H3cEntityExtCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 7),
    _H3cEntityExtCpuUsageThreshold_Type()
)
h3cEntityExtCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtCpuUsageThreshold.setStatus("current")


class _H3cEntityExtMemUsage_Type(Integer32):
    """Custom type h3cEntityExtMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtMemUsage_Type.__name__ = "Integer32"
_H3cEntityExtMemUsage_Object = MibTableColumn
h3cEntityExtMemUsage = _H3cEntityExtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 8),
    _H3cEntityExtMemUsage_Type()
)
h3cEntityExtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMemUsage.setStatus("current")


class _H3cEntityExtMemUsageThreshold_Type(Integer32):
    """Custom type h3cEntityExtMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtMemUsageThreshold_Type.__name__ = "Integer32"
_H3cEntityExtMemUsageThreshold_Object = MibTableColumn
h3cEntityExtMemUsageThreshold = _H3cEntityExtMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 9),
    _H3cEntityExtMemUsageThreshold_Type()
)
h3cEntityExtMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtMemUsageThreshold.setStatus("current")
_H3cEntityExtMemSize_Type = Unsigned32
_H3cEntityExtMemSize_Object = MibTableColumn
h3cEntityExtMemSize = _H3cEntityExtMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 10),
    _H3cEntityExtMemSize_Type()
)
h3cEntityExtMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMemSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cEntityExtMemSize.setUnits("bytes")
_H3cEntityExtUpTime_Type = Integer32
_H3cEntityExtUpTime_Object = MibTableColumn
h3cEntityExtUpTime = _H3cEntityExtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 11),
    _H3cEntityExtUpTime_Type()
)
h3cEntityExtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtUpTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cEntityExtUpTime.setUnits("seconds")
_H3cEntityExtTemperature_Type = Integer32
_H3cEntityExtTemperature_Object = MibTableColumn
h3cEntityExtTemperature = _H3cEntityExtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 12),
    _H3cEntityExtTemperature_Type()
)
h3cEntityExtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtTemperature.setStatus("current")
_H3cEntityExtTemperatureThreshold_Type = Integer32
_H3cEntityExtTemperatureThreshold_Object = MibTableColumn
h3cEntityExtTemperatureThreshold = _H3cEntityExtTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 13),
    _H3cEntityExtTemperatureThreshold_Type()
)
h3cEntityExtTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureThreshold.setStatus("current")
_H3cEntityExtVoltage_Type = Integer32
_H3cEntityExtVoltage_Object = MibTableColumn
h3cEntityExtVoltage = _H3cEntityExtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 14),
    _H3cEntityExtVoltage_Type()
)
h3cEntityExtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtVoltage.setStatus("current")
_H3cEntityExtVoltageLowThreshold_Type = Integer32
_H3cEntityExtVoltageLowThreshold_Object = MibTableColumn
h3cEntityExtVoltageLowThreshold = _H3cEntityExtVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 15),
    _H3cEntityExtVoltageLowThreshold_Type()
)
h3cEntityExtVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtVoltageLowThreshold.setStatus("current")
_H3cEntityExtVoltageHighThreshold_Type = Integer32
_H3cEntityExtVoltageHighThreshold_Object = MibTableColumn
h3cEntityExtVoltageHighThreshold = _H3cEntityExtVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 16),
    _H3cEntityExtVoltageHighThreshold_Type()
)
h3cEntityExtVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtVoltageHighThreshold.setStatus("current")
_H3cEntityExtCriticalTemperatureThreshold_Type = Integer32
_H3cEntityExtCriticalTemperatureThreshold_Object = MibTableColumn
h3cEntityExtCriticalTemperatureThreshold = _H3cEntityExtCriticalTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 17),
    _H3cEntityExtCriticalTemperatureThreshold_Type()
)
h3cEntityExtCriticalTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtCriticalTemperatureThreshold.setStatus("current")
_H3cEntityExtMacAddress_Type = MacAddress
_H3cEntityExtMacAddress_Object = MibTableColumn
h3cEntityExtMacAddress = _H3cEntityExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 18),
    _H3cEntityExtMacAddress_Type()
)
h3cEntityExtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMacAddress.setStatus("current")


class _H3cEntityExtErrorStatus_Type(Integer32):
    """Custom type h3cEntityExtErrorStatus based on Integer32"""
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


_H3cEntityExtErrorStatus_Type.__name__ = "Integer32"
_H3cEntityExtErrorStatus_Object = MibTableColumn
h3cEntityExtErrorStatus = _H3cEntityExtErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 19),
    _H3cEntityExtErrorStatus_Type()
)
h3cEntityExtErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtErrorStatus.setStatus("current")


class _H3cEntityExtCpuMaxUsage_Type(Integer32):
    """Custom type h3cEntityExtCpuMaxUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtCpuMaxUsage_Type.__name__ = "Integer32"
_H3cEntityExtCpuMaxUsage_Object = MibTableColumn
h3cEntityExtCpuMaxUsage = _H3cEntityExtCpuMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 20),
    _H3cEntityExtCpuMaxUsage_Type()
)
h3cEntityExtCpuMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtCpuMaxUsage.setStatus("current")
_H3cEntityExtLowerTemperatureThreshold_Type = Integer32
_H3cEntityExtLowerTemperatureThreshold_Object = MibTableColumn
h3cEntityExtLowerTemperatureThreshold = _H3cEntityExtLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 21),
    _H3cEntityExtLowerTemperatureThreshold_Type()
)
h3cEntityExtLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtLowerTemperatureThreshold.setStatus("current")
_H3cEntityExtShutdownTemperatureThreshold_Type = Integer32
_H3cEntityExtShutdownTemperatureThreshold_Object = MibTableColumn
h3cEntityExtShutdownTemperatureThreshold = _H3cEntityExtShutdownTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 22),
    _H3cEntityExtShutdownTemperatureThreshold_Type()
)
h3cEntityExtShutdownTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtShutdownTemperatureThreshold.setStatus("current")
_H3cEntityExtPhyMemSize_Type = Unsigned32
_H3cEntityExtPhyMemSize_Object = MibTableColumn
h3cEntityExtPhyMemSize = _H3cEntityExtPhyMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 23),
    _H3cEntityExtPhyMemSize_Type()
)
h3cEntityExtPhyMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtPhyMemSize.setStatus("current")
_H3cEntityExtPhyCpuFrequency_Type = Integer32
_H3cEntityExtPhyCpuFrequency_Object = MibTableColumn
h3cEntityExtPhyCpuFrequency = _H3cEntityExtPhyCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 24),
    _H3cEntityExtPhyCpuFrequency_Type()
)
h3cEntityExtPhyCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtPhyCpuFrequency.setStatus("current")


class _H3cEntityExtFirstUsedDate_Type(DateAndTime):
    """Custom type h3cEntityExtFirstUsedDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cEntityExtFirstUsedDate_Type.__name__ = "DateAndTime"
_H3cEntityExtFirstUsedDate_Object = MibTableColumn
h3cEntityExtFirstUsedDate = _H3cEntityExtFirstUsedDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 25),
    _H3cEntityExtFirstUsedDate_Type()
)
h3cEntityExtFirstUsedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtFirstUsedDate.setStatus("current")


class _H3cEntityExtCpuAvgUsage_Type(Integer32):
    """Custom type h3cEntityExtCpuAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtCpuAvgUsage_Type.__name__ = "Integer32"
_H3cEntityExtCpuAvgUsage_Object = MibTableColumn
h3cEntityExtCpuAvgUsage = _H3cEntityExtCpuAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 26),
    _H3cEntityExtCpuAvgUsage_Type()
)
h3cEntityExtCpuAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtCpuAvgUsage.setStatus("current")


class _H3cEntityExtMemAvgUsage_Type(Integer32):
    """Custom type h3cEntityExtMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cEntityExtMemAvgUsage_Type.__name__ = "Integer32"
_H3cEntityExtMemAvgUsage_Object = MibTableColumn
h3cEntityExtMemAvgUsage = _H3cEntityExtMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 27),
    _H3cEntityExtMemAvgUsage_Type()
)
h3cEntityExtMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMemAvgUsage.setStatus("current")


class _H3cEntityExtMemType_Type(OctetString):
    """Custom type h3cEntityExtMemType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cEntityExtMemType_Type.__name__ = "OctetString"
_H3cEntityExtMemType_Object = MibTableColumn
h3cEntityExtMemType = _H3cEntityExtMemType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 28),
    _H3cEntityExtMemType_Type()
)
h3cEntityExtMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMemType.setStatus("current")
_H3cEntityExtCriticalLowerTemperatureThreshold_Type = Integer32
_H3cEntityExtCriticalLowerTemperatureThreshold_Object = MibTableColumn
h3cEntityExtCriticalLowerTemperatureThreshold = _H3cEntityExtCriticalLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 29),
    _H3cEntityExtCriticalLowerTemperatureThreshold_Type()
)
h3cEntityExtCriticalLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtCriticalLowerTemperatureThreshold.setStatus("current")
_H3cEntityExtShutdownLowerTemperatureThreshold_Type = Integer32
_H3cEntityExtShutdownLowerTemperatureThreshold_Object = MibTableColumn
h3cEntityExtShutdownLowerTemperatureThreshold = _H3cEntityExtShutdownLowerTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 1, 1, 1, 30),
    _H3cEntityExtShutdownLowerTemperatureThreshold_Type()
)
h3cEntityExtShutdownLowerTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtShutdownLowerTemperatureThreshold.setStatus("current")
_H3cEntityExtManu_ObjectIdentity = ObjectIdentity
h3cEntityExtManu = _H3cEntityExtManu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2)
)
_H3cEntityExtManuTable_Object = MibTable
h3cEntityExtManuTable = _H3cEntityExtManuTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEntityExtManuTable.setStatus("current")
_H3cEntityExtManuEntry_Object = MibTableRow
h3cEntityExtManuEntry = _H3cEntityExtManuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1)
)
h3cEntityExtManuEntry.setIndexNames(
    (0, "H3C-ENTITY-EXT-MIB", "h3cEntityExtManuPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cEntityExtManuEntry.setStatus("current")


class _H3cEntityExtManuPhysicalIndex_Type(Integer32):
    """Custom type h3cEntityExtManuPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cEntityExtManuPhysicalIndex_Type.__name__ = "Integer32"
_H3cEntityExtManuPhysicalIndex_Object = MibTableColumn
h3cEntityExtManuPhysicalIndex = _H3cEntityExtManuPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1, 1),
    _H3cEntityExtManuPhysicalIndex_Type()
)
h3cEntityExtManuPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtManuPhysicalIndex.setStatus("current")
_H3cEntityExtManuSerialNum_Type = SnmpAdminString
_H3cEntityExtManuSerialNum_Object = MibTableColumn
h3cEntityExtManuSerialNum = _H3cEntityExtManuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1, 2),
    _H3cEntityExtManuSerialNum_Type()
)
h3cEntityExtManuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtManuSerialNum.setStatus("current")
_H3cEntityExtManuBuildInfo_Type = SnmpAdminString
_H3cEntityExtManuBuildInfo_Object = MibTableColumn
h3cEntityExtManuBuildInfo = _H3cEntityExtManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1, 3),
    _H3cEntityExtManuBuildInfo_Type()
)
h3cEntityExtManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtManuBuildInfo.setStatus("current")
_H3cEntityExtManuBOM_Type = SnmpAdminString
_H3cEntityExtManuBOM_Object = MibTableColumn
h3cEntityExtManuBOM = _H3cEntityExtManuBOM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1, 4),
    _H3cEntityExtManuBOM_Type()
)
h3cEntityExtManuBOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtManuBOM.setStatus("current")
_H3cEntityExtMacAddressCount_Type = Unsigned32
_H3cEntityExtMacAddressCount_Object = MibTableColumn
h3cEntityExtMacAddressCount = _H3cEntityExtMacAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 2, 1, 1, 5),
    _H3cEntityExtMacAddressCount_Type()
)
h3cEntityExtMacAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtMacAddressCount.setStatus("current")
_H3cEntityExtPower_ObjectIdentity = ObjectIdentity
h3cEntityExtPower = _H3cEntityExtPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3)
)
_H3cEntityExtPowerTable_Object = MibTable
h3cEntityExtPowerTable = _H3cEntityExtPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cEntityExtPowerTable.setStatus("current")
_H3cEntityExtPowerEntry_Object = MibTableRow
h3cEntityExtPowerEntry = _H3cEntityExtPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1)
)
h3cEntityExtPowerEntry.setIndexNames(
    (0, "H3C-ENTITY-EXT-MIB", "h3cEntityExtPowerPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cEntityExtPowerEntry.setStatus("current")


class _H3cEntityExtPowerPhysicalIndex_Type(Integer32):
    """Custom type h3cEntityExtPowerPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cEntityExtPowerPhysicalIndex_Type.__name__ = "Integer32"
_H3cEntityExtPowerPhysicalIndex_Object = MibTableColumn
h3cEntityExtPowerPhysicalIndex = _H3cEntityExtPowerPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1, 1),
    _H3cEntityExtPowerPhysicalIndex_Type()
)
h3cEntityExtPowerPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtPowerPhysicalIndex.setStatus("current")
_H3cEntityExtNominalPower_Type = Gauge32
_H3cEntityExtNominalPower_Object = MibTableColumn
h3cEntityExtNominalPower = _H3cEntityExtNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1, 2),
    _H3cEntityExtNominalPower_Type()
)
h3cEntityExtNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtNominalPower.setStatus("current")
_H3cEntityExtCurrentPower_Type = Gauge32
_H3cEntityExtCurrentPower_Object = MibTableColumn
h3cEntityExtCurrentPower = _H3cEntityExtCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1, 3),
    _H3cEntityExtCurrentPower_Type()
)
h3cEntityExtCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEntityExtCurrentPower.setStatus("current")
_H3cEntityExtAveragePower_Type = Integer32
_H3cEntityExtAveragePower_Object = MibTableColumn
h3cEntityExtAveragePower = _H3cEntityExtAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1, 4),
    _H3cEntityExtAveragePower_Type()
)
h3cEntityExtAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtAveragePower.setStatus("current")
_H3cEntityExtPeakPower_Type = Integer32
_H3cEntityExtPeakPower_Object = MibTableColumn
h3cEntityExtPeakPower = _H3cEntityExtPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 3, 1, 1, 5),
    _H3cEntityExtPeakPower_Type()
)
h3cEntityExtPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEntityExtPeakPower.setStatus("current")
_H3cProcessObjects_ObjectIdentity = ObjectIdentity
h3cProcessObjects = _H3cProcessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4)
)
_H3cProcessTable_Object = MibTable
h3cProcessTable = _H3cProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cProcessTable.setStatus("current")
_H3cProcessEntry_Object = MibTableRow
h3cProcessEntry = _H3cProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4, 1, 1)
)
h3cProcessEntry.setIndexNames(
    (0, "H3C-ENTITY-EXT-MIB", "h3cProcessID"),
)
if mibBuilder.loadTexts:
    h3cProcessEntry.setStatus("current")
_H3cProcessID_Type = Unsigned32
_H3cProcessID_Object = MibTableColumn
h3cProcessID = _H3cProcessID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4, 1, 1, 1),
    _H3cProcessID_Type()
)
h3cProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProcessID.setStatus("current")


class _H3cProcessName_Type(DisplayString):
    """Custom type h3cProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cProcessName_Type.__name__ = "DisplayString"
_H3cProcessName_Object = MibTableColumn
h3cProcessName = _H3cProcessName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4, 1, 1, 2),
    _H3cProcessName_Type()
)
h3cProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProcessName.setStatus("current")


class _H3cProcessUtil5Min_Type(Unsigned32):
    """Custom type h3cProcessUtil5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cProcessUtil5Min_Type.__name__ = "Unsigned32"
_H3cProcessUtil5Min_Object = MibTableColumn
h3cProcessUtil5Min = _H3cProcessUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 1, 4, 1, 1, 3),
    _H3cProcessUtil5Min_Type()
)
h3cProcessUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cProcessUtil5Min.setStatus("current")
_H3cEntityExtTraps_ObjectIdentity = ObjectIdentity
h3cEntityExtTraps = _H3cEntityExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2)
)
_H3cEntityExtTrapsPrefix_ObjectIdentity = ObjectIdentity
h3cEntityExtTrapsPrefix = _H3cEntityExtTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0)
)
_H3cEntityExtTrapsInfor_ObjectIdentity = ObjectIdentity
h3cEntityExtTrapsInfor = _H3cEntityExtTrapsInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 1)
)


class _H3cEntityExtTrapDescription_Type(SnmpAdminString):
    """Custom type h3cEntityExtTrapDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEntityExtTrapDescription_Type.__name__ = "SnmpAdminString"
_H3cEntityExtTrapDescription_Object = MibScalar
h3cEntityExtTrapDescription = _H3cEntityExtTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 1, 1),
    _H3cEntityExtTrapDescription_Type()
)
h3cEntityExtTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtTrapDescription.setStatus("current")


class _H3cEntityExtECCParityAlarmStatus_Type(Integer32):
    """Custom type h3cEntityExtECCParityAlarmStatus based on Integer32"""
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


_H3cEntityExtECCParityAlarmStatus_Type.__name__ = "Integer32"
_H3cEntityExtECCParityAlarmStatus_Object = MibScalar
h3cEntityExtECCParityAlarmStatus = _H3cEntityExtECCParityAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 1, 2),
    _H3cEntityExtECCParityAlarmStatus_Type()
)
h3cEntityExtECCParityAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtECCParityAlarmStatus.setStatus("current")
_H3cEntityExtSFPInvalidInDays_Type = Integer32
_H3cEntityExtSFPInvalidInDays_Object = MibScalar
h3cEntityExtSFPInvalidInDays = _H3cEntityExtSFPInvalidInDays_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 1, 3),
    _H3cEntityExtSFPInvalidInDays_Type()
)
h3cEntityExtSFPInvalidInDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEntityExtSFPInvalidInDays.setStatus("current")
_H3cEntityExtConformance_ObjectIdentity = ObjectIdentity
h3cEntityExtConformance = _H3cEntityExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3)
)
_H3cEntityExtCompliances_ObjectIdentity = ObjectIdentity
h3cEntityExtCompliances = _H3cEntityExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 1)
)
_H3cEntityExtGroups_ObjectIdentity = ObjectIdentity
h3cEntityExtGroups = _H3cEntityExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 2)
)

# Managed Objects groups

h3cEntityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 2, 1)
)
h3cEntityExtGroup.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtStandbyStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemSize"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtUpTime"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageLowThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageHighThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMacAddress"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtErrorStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuMaxUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtLowerTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhyMemSize"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhyCpuFrequency"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtFirstUsedDate"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuAvgUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemAvgUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemType"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalLowerTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cEntityExtGroup.setStatus("current")

h3cEntityExtManuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 2, 3)
)
h3cEntityExtManuGroup.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtManuPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtManuSerialNum"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtManuBuildInfo"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtManuBOM"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMacAddressCount"))
)
if mibBuilder.loadTexts:
    h3cEntityExtManuGroup.setStatus("current")

h3cEntityExtPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 2, 4)
)
h3cEntityExtPowerGroup.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPowerPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtNominalPower"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCurrentPower"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAveragePower"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtPeakPower"))
)
if mibBuilder.loadTexts:
    h3cEntityExtPowerGroup.setStatus("current")


# Notification objects

h3cEntityExtTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 1)
)
h3cEntityExtTemperatureThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 2)
)
h3cEntityExtVoltageLowThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageLowThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 3)
)
h3cEntityExtVoltageHighThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageHighThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtCpuUsageThresholdNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 4)
)
h3cEntityExtCpuUsageThresholdNotfication.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtCpuUsageThresholdNotfication.setStatus(
        "current"
    )

h3cEntityExtMemUsageThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 5)
)
h3cEntityExtMemUsageThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemSize"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtMemUsageThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtOperEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 6)
)
h3cEntityExtOperEnabled.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtOperEnabled.setStatus(
        "current"
    )

h3cEntityExtOperDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 7)
)
h3cEntityExtOperDisabled.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtOperDisabled.setStatus(
        "current"
    )

h3cEntityExtCriticalTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 8)
)
h3cEntityExtCriticalTemperatureThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtCriticalTemperatureThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtSFPAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 9)
)
h3cEntityExtSFPAlarmOn.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtErrorStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtSFPAlarmOn.setStatus(
        "current"
    )

h3cEntityExtSFPAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 10)
)
h3cEntityExtSFPAlarmOff.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtErrorStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtSFPAlarmOff.setStatus(
        "current"
    )

h3cEntityExtSFPPhony = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 11)
)
h3cEntityExtSFPPhony.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtSFPPhony.setStatus(
        "current"
    )

h3cEntityInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 12)
)
h3cEntityInsert.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    h3cEntityInsert.setStatus(
        "current"
    )

h3cEntityRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 13)
)
h3cEntityRemove.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    h3cEntityRemove.setStatus(
        "current"
    )

h3cEntityExtForcedPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 14)
)
h3cEntityExtForcedPowerOff.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtForcedPowerOff.setStatus(
        "current"
    )

h3cEntityExtForcedPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 15)
)
h3cEntityExtForcedPowerOn.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtForcedPowerOn.setStatus(
        "current"
    )

h3cEntityExtFaultAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 16)
)
h3cEntityExtFaultAlarmOn.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtErrorStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtFaultAlarmOn.setStatus(
        "current"
    )

h3cEntityExtFaultAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 17)
)
h3cEntityExtFaultAlarmOff.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtErrorStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtFaultAlarmOff.setStatus(
        "current"
    )

h3cEntityExtResourceLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 18)
)
h3cEntityExtResourceLack.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExtResourceLack.setStatus(
        "current"
    )

h3cEntityExtResourceEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 19)
)
h3cEntityExtResourceEnough.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExtResourceEnough.setStatus(
        "current"
    )

h3cEntityExtTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 20)
)
h3cEntityExtTemperatureLower.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtLowerTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureLower.setStatus(
        "current"
    )

h3cEntityExtTemperatureTooUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 21)
)
h3cEntityExtTemperatureTooUp.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureTooUp.setStatus(
        "current"
    )

h3cEntityExtTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 22)
)
h3cEntityExtTemperatureNormal.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtLowerTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureNormal.setStatus(
        "current"
    )

h3cEntityExternalAlarmOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 23)
)
h3cEntityExternalAlarmOccur.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExternalAlarmOccur.setStatus(
        "current"
    )

h3cEntityExternalAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 24)
)
h3cEntityExternalAlarmRecover.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExternalAlarmRecover.setStatus(
        "current"
    )

h3cEntityExtCpuUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 25)
)
h3cEntityExtCpuUsageThresholdRecover.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtCpuUsageThresholdRecover.setStatus(
        "current"
    )

h3cEntityExtMemUsageThresholdRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 26)
)
h3cEntityExtMemUsageThresholdRecover.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsage"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsageThreshold"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemSize"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAdminStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtAlarmLight"))
)
if mibBuilder.loadTexts:
    h3cEntityExtMemUsageThresholdRecover.setStatus(
        "current"
    )

h3cEntityExtMemAllocatedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 27)
)
h3cEntityExtMemAllocatedFailed.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    h3cEntityExtMemAllocatedFailed.setStatus(
        "current"
    )

h3cEntityExtECCParityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 28)
)
h3cEntityExtECCParityAlarm.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtECCParityAlarmStatus"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTrapDescription"))
)
if mibBuilder.loadTexts:
    h3cEntityExtECCParityAlarm.setStatus(
        "current"
    )

h3cEntityExtCritLowerTempThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 29)
)
h3cEntityExtCritLowerTempThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cEntityExtCritLowerTempThresholdNotification.setStatus(
        "current"
    )

h3cEntityExtTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 30)
)
h3cEntityExtTemperatureTooLow.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cEntityExtTemperatureTooLow.setStatus(
        "current"
    )

h3cEntityExtFanDirectionNotPreferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 31)
)
h3cEntityExtFanDirectionNotPreferred.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExtFanDirectionNotPreferred.setStatus(
        "current"
    )

h3cEntityExtFanDirectionNotAccord = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 32)
)
h3cEntityExtFanDirectionNotAccord.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExtFanDirectionNotAccord.setStatus(
        "current"
    )

h3cEntityExtSFPInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 33)
)
h3cEntityExtSFPInvalid.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPInvalidInDays"))
)
if mibBuilder.loadTexts:
    h3cEntityExtSFPInvalid.setStatus(
        "current"
    )

h3cEntityExtSFPInvalidNow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 2, 0, 34)
)
h3cEntityExtSFPInvalidNow.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    h3cEntityExtSFPInvalidNow.setStatus(
        "current"
    )


# Notifications groups

h3cEntityExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 2, 2)
)
h3cEntityExtNotificationGroup.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageLowThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtVoltageHighThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsageThresholdNotfication"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsageThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperEnabled"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperDisabled"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalTemperatureThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPAlarmOn"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPAlarmOff"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPPhony"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityInsert"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityRemove"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtForcedPowerOff"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtForcedPowerOn"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtFaultAlarmOn"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtFaultAlarmOff"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtResourceLack"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtResourceEnough"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureLower"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureTooUp"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureNormal"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExternalAlarmOccur"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExternalAlarmRecover"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCpuUsageThresholdRecover"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemUsageThresholdRecover"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtMemAllocatedFailed"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtECCParityAlarm"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCritLowerTempThresholdNotification"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperatureTooLow"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtFanDirectionNotPreferred"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtFanDirectionNotAccord"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPInvalid"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtSFPInvalidNow"))
)
if mibBuilder.loadTexts:
    h3cEntityExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cEntityExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEntityExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ENTITY-EXT-MIB",
    **{"H3cAdminState": H3cAdminState,
       "H3cOperState": H3cOperState,
       "H3cAlarmStatus": H3cAlarmStatus,
       "H3cStandbyStatus": H3cStandbyStatus,
       "h3cEntityExtend": h3cEntityExtend,
       "h3cEntityExtObjects": h3cEntityExtObjects,
       "h3cEntityExtState": h3cEntityExtState,
       "h3cEntityExtStateTable": h3cEntityExtStateTable,
       "h3cEntityExtStateEntry": h3cEntityExtStateEntry,
       "h3cEntityExtPhysicalIndex": h3cEntityExtPhysicalIndex,
       "h3cEntityExtAdminStatus": h3cEntityExtAdminStatus,
       "h3cEntityExtOperStatus": h3cEntityExtOperStatus,
       "h3cEntityExtStandbyStatus": h3cEntityExtStandbyStatus,
       "h3cEntityExtAlarmLight": h3cEntityExtAlarmLight,
       "h3cEntityExtCpuUsage": h3cEntityExtCpuUsage,
       "h3cEntityExtCpuUsageThreshold": h3cEntityExtCpuUsageThreshold,
       "h3cEntityExtMemUsage": h3cEntityExtMemUsage,
       "h3cEntityExtMemUsageThreshold": h3cEntityExtMemUsageThreshold,
       "h3cEntityExtMemSize": h3cEntityExtMemSize,
       "h3cEntityExtUpTime": h3cEntityExtUpTime,
       "h3cEntityExtTemperature": h3cEntityExtTemperature,
       "h3cEntityExtTemperatureThreshold": h3cEntityExtTemperatureThreshold,
       "h3cEntityExtVoltage": h3cEntityExtVoltage,
       "h3cEntityExtVoltageLowThreshold": h3cEntityExtVoltageLowThreshold,
       "h3cEntityExtVoltageHighThreshold": h3cEntityExtVoltageHighThreshold,
       "h3cEntityExtCriticalTemperatureThreshold": h3cEntityExtCriticalTemperatureThreshold,
       "h3cEntityExtMacAddress": h3cEntityExtMacAddress,
       "h3cEntityExtErrorStatus": h3cEntityExtErrorStatus,
       "h3cEntityExtCpuMaxUsage": h3cEntityExtCpuMaxUsage,
       "h3cEntityExtLowerTemperatureThreshold": h3cEntityExtLowerTemperatureThreshold,
       "h3cEntityExtShutdownTemperatureThreshold": h3cEntityExtShutdownTemperatureThreshold,
       "h3cEntityExtPhyMemSize": h3cEntityExtPhyMemSize,
       "h3cEntityExtPhyCpuFrequency": h3cEntityExtPhyCpuFrequency,
       "h3cEntityExtFirstUsedDate": h3cEntityExtFirstUsedDate,
       "h3cEntityExtCpuAvgUsage": h3cEntityExtCpuAvgUsage,
       "h3cEntityExtMemAvgUsage": h3cEntityExtMemAvgUsage,
       "h3cEntityExtMemType": h3cEntityExtMemType,
       "h3cEntityExtCriticalLowerTemperatureThreshold": h3cEntityExtCriticalLowerTemperatureThreshold,
       "h3cEntityExtShutdownLowerTemperatureThreshold": h3cEntityExtShutdownLowerTemperatureThreshold,
       "h3cEntityExtManu": h3cEntityExtManu,
       "h3cEntityExtManuTable": h3cEntityExtManuTable,
       "h3cEntityExtManuEntry": h3cEntityExtManuEntry,
       "h3cEntityExtManuPhysicalIndex": h3cEntityExtManuPhysicalIndex,
       "h3cEntityExtManuSerialNum": h3cEntityExtManuSerialNum,
       "h3cEntityExtManuBuildInfo": h3cEntityExtManuBuildInfo,
       "h3cEntityExtManuBOM": h3cEntityExtManuBOM,
       "h3cEntityExtMacAddressCount": h3cEntityExtMacAddressCount,
       "h3cEntityExtPower": h3cEntityExtPower,
       "h3cEntityExtPowerTable": h3cEntityExtPowerTable,
       "h3cEntityExtPowerEntry": h3cEntityExtPowerEntry,
       "h3cEntityExtPowerPhysicalIndex": h3cEntityExtPowerPhysicalIndex,
       "h3cEntityExtNominalPower": h3cEntityExtNominalPower,
       "h3cEntityExtCurrentPower": h3cEntityExtCurrentPower,
       "h3cEntityExtAveragePower": h3cEntityExtAveragePower,
       "h3cEntityExtPeakPower": h3cEntityExtPeakPower,
       "h3cProcessObjects": h3cProcessObjects,
       "h3cProcessTable": h3cProcessTable,
       "h3cProcessEntry": h3cProcessEntry,
       "h3cProcessID": h3cProcessID,
       "h3cProcessName": h3cProcessName,
       "h3cProcessUtil5Min": h3cProcessUtil5Min,
       "h3cEntityExtTraps": h3cEntityExtTraps,
       "h3cEntityExtTrapsPrefix": h3cEntityExtTrapsPrefix,
       "h3cEntityExtTemperatureThresholdNotification": h3cEntityExtTemperatureThresholdNotification,
       "h3cEntityExtVoltageLowThresholdNotification": h3cEntityExtVoltageLowThresholdNotification,
       "h3cEntityExtVoltageHighThresholdNotification": h3cEntityExtVoltageHighThresholdNotification,
       "h3cEntityExtCpuUsageThresholdNotfication": h3cEntityExtCpuUsageThresholdNotfication,
       "h3cEntityExtMemUsageThresholdNotification": h3cEntityExtMemUsageThresholdNotification,
       "h3cEntityExtOperEnabled": h3cEntityExtOperEnabled,
       "h3cEntityExtOperDisabled": h3cEntityExtOperDisabled,
       "h3cEntityExtCriticalTemperatureThresholdNotification": h3cEntityExtCriticalTemperatureThresholdNotification,
       "h3cEntityExtSFPAlarmOn": h3cEntityExtSFPAlarmOn,
       "h3cEntityExtSFPAlarmOff": h3cEntityExtSFPAlarmOff,
       "h3cEntityExtSFPPhony": h3cEntityExtSFPPhony,
       "h3cEntityInsert": h3cEntityInsert,
       "h3cEntityRemove": h3cEntityRemove,
       "h3cEntityExtForcedPowerOff": h3cEntityExtForcedPowerOff,
       "h3cEntityExtForcedPowerOn": h3cEntityExtForcedPowerOn,
       "h3cEntityExtFaultAlarmOn": h3cEntityExtFaultAlarmOn,
       "h3cEntityExtFaultAlarmOff": h3cEntityExtFaultAlarmOff,
       "h3cEntityExtResourceLack": h3cEntityExtResourceLack,
       "h3cEntityExtResourceEnough": h3cEntityExtResourceEnough,
       "h3cEntityExtTemperatureLower": h3cEntityExtTemperatureLower,
       "h3cEntityExtTemperatureTooUp": h3cEntityExtTemperatureTooUp,
       "h3cEntityExtTemperatureNormal": h3cEntityExtTemperatureNormal,
       "h3cEntityExternalAlarmOccur": h3cEntityExternalAlarmOccur,
       "h3cEntityExternalAlarmRecover": h3cEntityExternalAlarmRecover,
       "h3cEntityExtCpuUsageThresholdRecover": h3cEntityExtCpuUsageThresholdRecover,
       "h3cEntityExtMemUsageThresholdRecover": h3cEntityExtMemUsageThresholdRecover,
       "h3cEntityExtMemAllocatedFailed": h3cEntityExtMemAllocatedFailed,
       "h3cEntityExtECCParityAlarm": h3cEntityExtECCParityAlarm,
       "h3cEntityExtCritLowerTempThresholdNotification": h3cEntityExtCritLowerTempThresholdNotification,
       "h3cEntityExtTemperatureTooLow": h3cEntityExtTemperatureTooLow,
       "h3cEntityExtFanDirectionNotPreferred": h3cEntityExtFanDirectionNotPreferred,
       "h3cEntityExtFanDirectionNotAccord": h3cEntityExtFanDirectionNotAccord,
       "h3cEntityExtSFPInvalid": h3cEntityExtSFPInvalid,
       "h3cEntityExtSFPInvalidNow": h3cEntityExtSFPInvalidNow,
       "h3cEntityExtTrapsInfor": h3cEntityExtTrapsInfor,
       "h3cEntityExtTrapDescription": h3cEntityExtTrapDescription,
       "h3cEntityExtECCParityAlarmStatus": h3cEntityExtECCParityAlarmStatus,
       "h3cEntityExtSFPInvalidInDays": h3cEntityExtSFPInvalidInDays,
       "h3cEntityExtConformance": h3cEntityExtConformance,
       "h3cEntityExtCompliances": h3cEntityExtCompliances,
       "h3cEntityExtCompliance": h3cEntityExtCompliance,
       "h3cEntityExtGroups": h3cEntityExtGroups,
       "h3cEntityExtGroup": h3cEntityExtGroup,
       "h3cEntityExtNotificationGroup": h3cEntityExtNotificationGroup,
       "h3cEntityExtManuGroup": h3cEntityExtManuGroup,
       "h3cEntityExtPowerGroup": h3cEntityExtPowerGroup}
)
