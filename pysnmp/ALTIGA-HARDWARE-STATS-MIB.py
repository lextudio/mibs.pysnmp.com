# SNMP MIB module (ALTIGA-HARDWARE-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-HARDWARE-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:12 2024
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

(alHardwareMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alHardwareMibModule")

(alHardwareGroup,
 alStatsHardware) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alHardwareGroup",
    "alStatsHardware")

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

altigaHardwareStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 27, 2)
)
altigaHardwareStatsMibModule.setRevisions(
        ("2003-03-27 13:00",
         "2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConcentratorCard(Integer32, TextualConvention):
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
        *(("dualT1Wan", 3),
          ("none", 1),
          ("sep", 2),
          ("sepE", 4))
    )



class ConcentratorType(Integer32, TextualConvention):
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
        *(("c1", 3),
          ("c5", 2),
          ("cxx", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AltigaHardwareStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaHardwareStatsMibConformance = _AltigaHardwareStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 27, 2, 1)
)
_AltigaHardwareStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaHardwareStatsMibCompliances = _AltigaHardwareStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 27, 2, 1, 1)
)
_AlStatsHardwareGlobal_ObjectIdentity = ObjectIdentity
alStatsHardwareGlobal = _AlStatsHardwareGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1)
)
_AlHardwareCpuVoltage_Type = Gauge32
_AlHardwareCpuVoltage_Object = MibScalar
alHardwareCpuVoltage = _AlHardwareCpuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 1),
    _AlHardwareCpuVoltage_Type()
)
alHardwareCpuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuVoltage.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareCpuVoltage.setUnits("centivolts")
_AlHardwareCpuVoltageAlarm_Type = TruthValue
_AlHardwareCpuVoltageAlarm_Object = MibScalar
alHardwareCpuVoltageAlarm = _AlHardwareCpuVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 2),
    _AlHardwareCpuVoltageAlarm_Type()
)
alHardwareCpuVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuVoltageAlarm.setStatus("current")
_AlHardwareCpuVoltageCount_Type = Counter32
_AlHardwareCpuVoltageCount_Object = MibScalar
alHardwareCpuVoltageCount = _AlHardwareCpuVoltageCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 3),
    _AlHardwareCpuVoltageCount_Type()
)
alHardwareCpuVoltageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuVoltageCount.setStatus("current")
_AlHardwareCpuVoltageTime_Type = TimeTicks
_AlHardwareCpuVoltageTime_Object = MibScalar
alHardwareCpuVoltageTime = _AlHardwareCpuVoltageTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 4),
    _AlHardwareCpuVoltageTime_Type()
)
alHardwareCpuVoltageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuVoltageTime.setStatus("current")
_AlHardwarePs1Voltage3v_Type = Gauge32
_AlHardwarePs1Voltage3v_Object = MibScalar
alHardwarePs1Voltage3v = _AlHardwarePs1Voltage3v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 5),
    _AlHardwarePs1Voltage3v_Type()
)
alHardwarePs1Voltage3v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage3v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage3v.setUnits("centivolts")
_AlHardwarePs1Voltage3vAlarm_Type = TruthValue
_AlHardwarePs1Voltage3vAlarm_Object = MibScalar
alHardwarePs1Voltage3vAlarm = _AlHardwarePs1Voltage3vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 6),
    _AlHardwarePs1Voltage3vAlarm_Type()
)
alHardwarePs1Voltage3vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage3vAlarm.setStatus("current")
_AlHardwarePs1Voltage3vCount_Type = Counter32
_AlHardwarePs1Voltage3vCount_Object = MibScalar
alHardwarePs1Voltage3vCount = _AlHardwarePs1Voltage3vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 7),
    _AlHardwarePs1Voltage3vCount_Type()
)
alHardwarePs1Voltage3vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage3vCount.setStatus("current")
_AlHardwarePs1Voltage3vTime_Type = TimeTicks
_AlHardwarePs1Voltage3vTime_Object = MibScalar
alHardwarePs1Voltage3vTime = _AlHardwarePs1Voltage3vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 8),
    _AlHardwarePs1Voltage3vTime_Type()
)
alHardwarePs1Voltage3vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage3vTime.setStatus("current")
_AlHardwarePs1Voltage5v_Type = Gauge32
_AlHardwarePs1Voltage5v_Object = MibScalar
alHardwarePs1Voltage5v = _AlHardwarePs1Voltage5v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 9),
    _AlHardwarePs1Voltage5v_Type()
)
alHardwarePs1Voltage5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage5v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage5v.setUnits("centivolts")
_AlHardwarePs1Voltage5vAlarm_Type = TruthValue
_AlHardwarePs1Voltage5vAlarm_Object = MibScalar
alHardwarePs1Voltage5vAlarm = _AlHardwarePs1Voltage5vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 10),
    _AlHardwarePs1Voltage5vAlarm_Type()
)
alHardwarePs1Voltage5vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage5vAlarm.setStatus("current")
_AlHardwarePs1Voltage5vCount_Type = Counter32
_AlHardwarePs1Voltage5vCount_Object = MibScalar
alHardwarePs1Voltage5vCount = _AlHardwarePs1Voltage5vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 11),
    _AlHardwarePs1Voltage5vCount_Type()
)
alHardwarePs1Voltage5vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage5vCount.setStatus("current")
_AlHardwarePs1Voltage5vTime_Type = TimeTicks
_AlHardwarePs1Voltage5vTime_Object = MibScalar
alHardwarePs1Voltage5vTime = _AlHardwarePs1Voltage5vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 12),
    _AlHardwarePs1Voltage5vTime_Type()
)
alHardwarePs1Voltage5vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Voltage5vTime.setStatus("current")
_AlHardwarePs2Voltage3v_Type = Gauge32
_AlHardwarePs2Voltage3v_Object = MibScalar
alHardwarePs2Voltage3v = _AlHardwarePs2Voltage3v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 13),
    _AlHardwarePs2Voltage3v_Type()
)
alHardwarePs2Voltage3v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage3v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage3v.setUnits("centivolts")
_AlHardwarePs2Voltage3vAlarm_Type = TruthValue
_AlHardwarePs2Voltage3vAlarm_Object = MibScalar
alHardwarePs2Voltage3vAlarm = _AlHardwarePs2Voltage3vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 14),
    _AlHardwarePs2Voltage3vAlarm_Type()
)
alHardwarePs2Voltage3vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage3vAlarm.setStatus("current")
_AlHardwarePs2Voltage3vCount_Type = Counter32
_AlHardwarePs2Voltage3vCount_Object = MibScalar
alHardwarePs2Voltage3vCount = _AlHardwarePs2Voltage3vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 15),
    _AlHardwarePs2Voltage3vCount_Type()
)
alHardwarePs2Voltage3vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage3vCount.setStatus("current")
_AlHardwarePs2Voltage3vTime_Type = TimeTicks
_AlHardwarePs2Voltage3vTime_Object = MibScalar
alHardwarePs2Voltage3vTime = _AlHardwarePs2Voltage3vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 16),
    _AlHardwarePs2Voltage3vTime_Type()
)
alHardwarePs2Voltage3vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage3vTime.setStatus("current")
_AlHardwarePs2Voltage5v_Type = Gauge32
_AlHardwarePs2Voltage5v_Object = MibScalar
alHardwarePs2Voltage5v = _AlHardwarePs2Voltage5v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 17),
    _AlHardwarePs2Voltage5v_Type()
)
alHardwarePs2Voltage5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage5v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage5v.setUnits("centivolts")
_AlHardwarePs2Voltage5vAlarm_Type = TruthValue
_AlHardwarePs2Voltage5vAlarm_Object = MibScalar
alHardwarePs2Voltage5vAlarm = _AlHardwarePs2Voltage5vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 18),
    _AlHardwarePs2Voltage5vAlarm_Type()
)
alHardwarePs2Voltage5vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage5vAlarm.setStatus("current")
_AlHardwarePs2Voltage5vCount_Type = Counter32
_AlHardwarePs2Voltage5vCount_Object = MibScalar
alHardwarePs2Voltage5vCount = _AlHardwarePs2Voltage5vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 19),
    _AlHardwarePs2Voltage5vCount_Type()
)
alHardwarePs2Voltage5vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage5vCount.setStatus("current")
_AlHardwarePs2Voltage5vTime_Type = TimeTicks
_AlHardwarePs2Voltage5vTime_Object = MibScalar
alHardwarePs2Voltage5vTime = _AlHardwarePs2Voltage5vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 20),
    _AlHardwarePs2Voltage5vTime_Type()
)
alHardwarePs2Voltage5vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Voltage5vTime.setStatus("current")
_AlHardwareBoardVoltage3v_Type = Gauge32
_AlHardwareBoardVoltage3v_Object = MibScalar
alHardwareBoardVoltage3v = _AlHardwareBoardVoltage3v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 21),
    _AlHardwareBoardVoltage3v_Type()
)
alHardwareBoardVoltage3v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage3v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage3v.setUnits("centivolts")
_AlHardwareBoardVoltage3vAlarm_Type = TruthValue
_AlHardwareBoardVoltage3vAlarm_Object = MibScalar
alHardwareBoardVoltage3vAlarm = _AlHardwareBoardVoltage3vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 22),
    _AlHardwareBoardVoltage3vAlarm_Type()
)
alHardwareBoardVoltage3vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage3vAlarm.setStatus("current")
_AlHardwareBoardVoltage3vCount_Type = Counter32
_AlHardwareBoardVoltage3vCount_Object = MibScalar
alHardwareBoardVoltage3vCount = _AlHardwareBoardVoltage3vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 23),
    _AlHardwareBoardVoltage3vCount_Type()
)
alHardwareBoardVoltage3vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage3vCount.setStatus("current")
_AlHardwareBoardVoltage3vTime_Type = TimeTicks
_AlHardwareBoardVoltage3vTime_Object = MibScalar
alHardwareBoardVoltage3vTime = _AlHardwareBoardVoltage3vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 24),
    _AlHardwareBoardVoltage3vTime_Type()
)
alHardwareBoardVoltage3vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage3vTime.setStatus("current")
_AlHardwareBoardVoltage5v_Type = Gauge32
_AlHardwareBoardVoltage5v_Object = MibScalar
alHardwareBoardVoltage5v = _AlHardwareBoardVoltage5v_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 25),
    _AlHardwareBoardVoltage5v_Type()
)
alHardwareBoardVoltage5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage5v.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage5v.setUnits("centivolts")
_AlHardwareBoardVoltage5vAlarm_Type = TruthValue
_AlHardwareBoardVoltage5vAlarm_Object = MibScalar
alHardwareBoardVoltage5vAlarm = _AlHardwareBoardVoltage5vAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 26),
    _AlHardwareBoardVoltage5vAlarm_Type()
)
alHardwareBoardVoltage5vAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage5vAlarm.setStatus("current")
_AlHardwareBoardVoltage5vCount_Type = Counter32
_AlHardwareBoardVoltage5vCount_Object = MibScalar
alHardwareBoardVoltage5vCount = _AlHardwareBoardVoltage5vCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 27),
    _AlHardwareBoardVoltage5vCount_Type()
)
alHardwareBoardVoltage5vCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage5vCount.setStatus("current")
_AlHardwareBoardVoltage5vTime_Type = TimeTicks
_AlHardwareBoardVoltage5vTime_Object = MibScalar
alHardwareBoardVoltage5vTime = _AlHardwareBoardVoltage5vTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 28),
    _AlHardwareBoardVoltage5vTime_Type()
)
alHardwareBoardVoltage5vTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareBoardVoltage5vTime.setStatus("current")


class _AlHardwareCpuTemp_Type(Integer32):
    """Custom type alHardwareCpuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 120),
    )


_AlHardwareCpuTemp_Type.__name__ = "Integer32"
_AlHardwareCpuTemp_Object = MibScalar
alHardwareCpuTemp = _AlHardwareCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 29),
    _AlHardwareCpuTemp_Type()
)
alHardwareCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuTemp.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareCpuTemp.setUnits("degrees Celsius")
_AlHardwareCpuTempAlarm_Type = TruthValue
_AlHardwareCpuTempAlarm_Object = MibScalar
alHardwareCpuTempAlarm = _AlHardwareCpuTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 30),
    _AlHardwareCpuTempAlarm_Type()
)
alHardwareCpuTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuTempAlarm.setStatus("current")
_AlHardwareCpuTempCount_Type = Counter32
_AlHardwareCpuTempCount_Object = MibScalar
alHardwareCpuTempCount = _AlHardwareCpuTempCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 31),
    _AlHardwareCpuTempCount_Type()
)
alHardwareCpuTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuTempCount.setStatus("current")
_AlHardwareCpuTempTime_Type = TimeTicks
_AlHardwareCpuTempTime_Object = MibScalar
alHardwareCpuTempTime = _AlHardwareCpuTempTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 32),
    _AlHardwareCpuTempTime_Type()
)
alHardwareCpuTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuTempTime.setStatus("current")


class _AlHardwareCageTemp_Type(Integer32):
    """Custom type alHardwareCageTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 120),
    )


_AlHardwareCageTemp_Type.__name__ = "Integer32"
_AlHardwareCageTemp_Object = MibScalar
alHardwareCageTemp = _AlHardwareCageTemp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 33),
    _AlHardwareCageTemp_Type()
)
alHardwareCageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCageTemp.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareCageTemp.setUnits("degrees Celsius")
_AlHardwareCageTempAlarm_Type = TruthValue
_AlHardwareCageTempAlarm_Object = MibScalar
alHardwareCageTempAlarm = _AlHardwareCageTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 34),
    _AlHardwareCageTempAlarm_Type()
)
alHardwareCageTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCageTempAlarm.setStatus("current")
_AlHardwareCageTempCount_Type = Counter32
_AlHardwareCageTempCount_Object = MibScalar
alHardwareCageTempCount = _AlHardwareCageTempCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 35),
    _AlHardwareCageTempCount_Type()
)
alHardwareCageTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCageTempCount.setStatus("current")
_AlHardwareCageTempTime_Type = TimeTicks
_AlHardwareCageTempTime_Object = MibScalar
alHardwareCageTempTime = _AlHardwareCageTempTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 36),
    _AlHardwareCageTempTime_Type()
)
alHardwareCageTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCageTempTime.setStatus("current")
_AlHardwareFan1Rpm_Type = Gauge32
_AlHardwareFan1Rpm_Object = MibScalar
alHardwareFan1Rpm = _AlHardwareFan1Rpm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 37),
    _AlHardwareFan1Rpm_Type()
)
alHardwareFan1Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan1Rpm.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareFan1Rpm.setUnits("RPM")
_AlHardwareFan1RpmAlarm_Type = TruthValue
_AlHardwareFan1RpmAlarm_Object = MibScalar
alHardwareFan1RpmAlarm = _AlHardwareFan1RpmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 38),
    _AlHardwareFan1RpmAlarm_Type()
)
alHardwareFan1RpmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan1RpmAlarm.setStatus("current")
_AlHardwareFan1RpmCount_Type = Counter32
_AlHardwareFan1RpmCount_Object = MibScalar
alHardwareFan1RpmCount = _AlHardwareFan1RpmCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 39),
    _AlHardwareFan1RpmCount_Type()
)
alHardwareFan1RpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan1RpmCount.setStatus("current")
_AlHardwareFan1RpmTime_Type = TimeTicks
_AlHardwareFan1RpmTime_Object = MibScalar
alHardwareFan1RpmTime = _AlHardwareFan1RpmTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 40),
    _AlHardwareFan1RpmTime_Type()
)
alHardwareFan1RpmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan1RpmTime.setStatus("current")
_AlHardwareFan2Rpm_Type = Gauge32
_AlHardwareFan2Rpm_Object = MibScalar
alHardwareFan2Rpm = _AlHardwareFan2Rpm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 41),
    _AlHardwareFan2Rpm_Type()
)
alHardwareFan2Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan2Rpm.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareFan2Rpm.setUnits("RPM")
_AlHardwareFan2RpmAlarm_Type = TruthValue
_AlHardwareFan2RpmAlarm_Object = MibScalar
alHardwareFan2RpmAlarm = _AlHardwareFan2RpmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 42),
    _AlHardwareFan2RpmAlarm_Type()
)
alHardwareFan2RpmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan2RpmAlarm.setStatus("current")
_AlHardwareFan2RpmCount_Type = Counter32
_AlHardwareFan2RpmCount_Object = MibScalar
alHardwareFan2RpmCount = _AlHardwareFan2RpmCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 43),
    _AlHardwareFan2RpmCount_Type()
)
alHardwareFan2RpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan2RpmCount.setStatus("current")
_AlHardwareFan2RpmTime_Type = TimeTicks
_AlHardwareFan2RpmTime_Object = MibScalar
alHardwareFan2RpmTime = _AlHardwareFan2RpmTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 44),
    _AlHardwareFan2RpmTime_Type()
)
alHardwareFan2RpmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan2RpmTime.setStatus("current")
_AlHardwareFan3Rpm_Type = Gauge32
_AlHardwareFan3Rpm_Object = MibScalar
alHardwareFan3Rpm = _AlHardwareFan3Rpm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 45),
    _AlHardwareFan3Rpm_Type()
)
alHardwareFan3Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan3Rpm.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareFan3Rpm.setUnits("RPM")
_AlHardwareFan3RpmAlarm_Type = TruthValue
_AlHardwareFan3RpmAlarm_Object = MibScalar
alHardwareFan3RpmAlarm = _AlHardwareFan3RpmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 46),
    _AlHardwareFan3RpmAlarm_Type()
)
alHardwareFan3RpmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan3RpmAlarm.setStatus("current")
_AlHardwareFan3RpmCount_Type = Counter32
_AlHardwareFan3RpmCount_Object = MibScalar
alHardwareFan3RpmCount = _AlHardwareFan3RpmCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 47),
    _AlHardwareFan3RpmCount_Type()
)
alHardwareFan3RpmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan3RpmCount.setStatus("current")
_AlHardwareFan3RpmTime_Type = TimeTicks
_AlHardwareFan3RpmTime_Object = MibScalar
alHardwareFan3RpmTime = _AlHardwareFan3RpmTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 48),
    _AlHardwareFan3RpmTime_Type()
)
alHardwareFan3RpmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareFan3RpmTime.setStatus("current")


class _AlHardwarePs1Type_Type(Integer32):
    """Custom type alHardwarePs1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("none", 1))
    )


_AlHardwarePs1Type_Type.__name__ = "Integer32"
_AlHardwarePs1Type_Object = MibScalar
alHardwarePs1Type = _AlHardwarePs1Type_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 49),
    _AlHardwarePs1Type_Type()
)
alHardwarePs1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs1Type.setStatus("current")


class _AlHardwarePs2Type_Type(Integer32):
    """Custom type alHardwarePs2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("none", 1))
    )


_AlHardwarePs2Type_Type.__name__ = "Integer32"
_AlHardwarePs2Type_Object = MibScalar
alHardwarePs2Type = _AlHardwarePs2Type_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 50),
    _AlHardwarePs2Type_Type()
)
alHardwarePs2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwarePs2Type.setStatus("current")
_AlHardwareSlot1Card_Type = ConcentratorCard
_AlHardwareSlot1Card_Object = MibScalar
alHardwareSlot1Card = _AlHardwareSlot1Card_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 51),
    _AlHardwareSlot1Card_Type()
)
alHardwareSlot1Card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot1Card.setStatus("current")
_AlHardwareSlot2Card_Type = ConcentratorCard
_AlHardwareSlot2Card_Object = MibScalar
alHardwareSlot2Card = _AlHardwareSlot2Card_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 52),
    _AlHardwareSlot2Card_Type()
)
alHardwareSlot2Card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot2Card.setStatus("current")
_AlHardwareSlot3Card_Type = ConcentratorCard
_AlHardwareSlot3Card_Object = MibScalar
alHardwareSlot3Card = _AlHardwareSlot3Card_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 53),
    _AlHardwareSlot3Card_Type()
)
alHardwareSlot3Card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot3Card.setStatus("current")
_AlHardwareSlot4Card_Type = ConcentratorCard
_AlHardwareSlot4Card_Object = MibScalar
alHardwareSlot4Card = _AlHardwareSlot4Card_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 54),
    _AlHardwareSlot4Card_Type()
)
alHardwareSlot4Card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot4Card.setStatus("current")
_AlHardwareSlot1Operational_Type = TruthValue
_AlHardwareSlot1Operational_Object = MibScalar
alHardwareSlot1Operational = _AlHardwareSlot1Operational_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 55),
    _AlHardwareSlot1Operational_Type()
)
alHardwareSlot1Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot1Operational.setStatus("current")
_AlHardwareSlot2Operational_Type = TruthValue
_AlHardwareSlot2Operational_Object = MibScalar
alHardwareSlot2Operational = _AlHardwareSlot2Operational_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 56),
    _AlHardwareSlot2Operational_Type()
)
alHardwareSlot2Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot2Operational.setStatus("current")
_AlHardwareSlot3Operational_Type = TruthValue
_AlHardwareSlot3Operational_Object = MibScalar
alHardwareSlot3Operational = _AlHardwareSlot3Operational_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 57),
    _AlHardwareSlot3Operational_Type()
)
alHardwareSlot3Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot3Operational.setStatus("current")
_AlHardwareSlot4Operational_Type = TruthValue
_AlHardwareSlot4Operational_Object = MibScalar
alHardwareSlot4Operational = _AlHardwareSlot4Operational_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 58),
    _AlHardwareSlot4Operational_Type()
)
alHardwareSlot4Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSlot4Operational.setStatus("current")
_AlHardwareRamSize_Type = Unsigned32
_AlHardwareRamSize_Object = MibScalar
alHardwareRamSize = _AlHardwareRamSize_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 59),
    _AlHardwareRamSize_Type()
)
alHardwareRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareRamSize.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareRamSize.setUnits("MB")
_AlHardwareChassis_Type = ConcentratorType
_AlHardwareChassis_Object = MibScalar
alHardwareChassis = _AlHardwareChassis_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 60),
    _AlHardwareChassis_Type()
)
alHardwareChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareChassis.setStatus("current")
_AlHardwareCpuVoltageNominal_Type = Gauge32
_AlHardwareCpuVoltageNominal_Object = MibScalar
alHardwareCpuVoltageNominal = _AlHardwareCpuVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 61),
    _AlHardwareCpuVoltageNominal_Type()
)
alHardwareCpuVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareCpuVoltageNominal.setStatus("current")
if mibBuilder.loadTexts:
    alHardwareCpuVoltageNominal.setUnits("centivolts")
_AlHardwareClientEthPrivSwitch_Type = TruthValue
_AlHardwareClientEthPrivSwitch_Object = MibScalar
alHardwareClientEthPrivSwitch = _AlHardwareClientEthPrivSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 62),
    _AlHardwareClientEthPrivSwitch_Type()
)
alHardwareClientEthPrivSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareClientEthPrivSwitch.setStatus("current")
_AlHardwareSerialNumber_Type = DisplayString
_AlHardwareSerialNumber_Object = MibScalar
alHardwareSerialNumber = _AlHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 22, 1, 63),
    _AlHardwareSerialNumber_Type()
)
alHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHardwareSerialNumber.setStatus("current")

# Managed Objects groups

altigaHardwareStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 22, 2)
)
altigaHardwareStatsGroup.setObjects(
      *(("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuVoltage"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuVoltageAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuVoltageCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuVoltageTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage3v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage3vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage3vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage3vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage5v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage5vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage5vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Voltage5vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage3v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage3vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage3vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage3vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage5v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage5vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage5vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Voltage5vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage3v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage3vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage3vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage3vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage5v"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage5vAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage5vCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareBoardVoltage5vTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuTemp"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuTempAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuTempCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuTempTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCageTemp"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCageTempAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCageTempCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCageTempTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan1Rpm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan1RpmAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan1RpmCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan1RpmTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan2Rpm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan2RpmAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan2RpmCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan2RpmTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan3Rpm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan3RpmAlarm"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan3RpmCount"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareFan3RpmTime"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs1Type"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwarePs2Type"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot1Card"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot2Card"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot3Card"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot4Card"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot1Operational"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot2Operational"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot3Operational"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSlot4Operational"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareRamSize"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareChassis"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareCpuVoltageNominal"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareClientEthPrivSwitch"),
        ("ALTIGA-HARDWARE-STATS-MIB", "alHardwareSerialNumber"))
)
if mibBuilder.loadTexts:
    altigaHardwareStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaHardwareStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 27, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaHardwareStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-HARDWARE-STATS-MIB",
    **{"ConcentratorCard": ConcentratorCard,
       "ConcentratorType": ConcentratorType,
       "altigaHardwareStatsMibModule": altigaHardwareStatsMibModule,
       "altigaHardwareStatsMibConformance": altigaHardwareStatsMibConformance,
       "altigaHardwareStatsMibCompliances": altigaHardwareStatsMibCompliances,
       "altigaHardwareStatsMibCompliance": altigaHardwareStatsMibCompliance,
       "altigaHardwareStatsGroup": altigaHardwareStatsGroup,
       "alStatsHardwareGlobal": alStatsHardwareGlobal,
       "alHardwareCpuVoltage": alHardwareCpuVoltage,
       "alHardwareCpuVoltageAlarm": alHardwareCpuVoltageAlarm,
       "alHardwareCpuVoltageCount": alHardwareCpuVoltageCount,
       "alHardwareCpuVoltageTime": alHardwareCpuVoltageTime,
       "alHardwarePs1Voltage3v": alHardwarePs1Voltage3v,
       "alHardwarePs1Voltage3vAlarm": alHardwarePs1Voltage3vAlarm,
       "alHardwarePs1Voltage3vCount": alHardwarePs1Voltage3vCount,
       "alHardwarePs1Voltage3vTime": alHardwarePs1Voltage3vTime,
       "alHardwarePs1Voltage5v": alHardwarePs1Voltage5v,
       "alHardwarePs1Voltage5vAlarm": alHardwarePs1Voltage5vAlarm,
       "alHardwarePs1Voltage5vCount": alHardwarePs1Voltage5vCount,
       "alHardwarePs1Voltage5vTime": alHardwarePs1Voltage5vTime,
       "alHardwarePs2Voltage3v": alHardwarePs2Voltage3v,
       "alHardwarePs2Voltage3vAlarm": alHardwarePs2Voltage3vAlarm,
       "alHardwarePs2Voltage3vCount": alHardwarePs2Voltage3vCount,
       "alHardwarePs2Voltage3vTime": alHardwarePs2Voltage3vTime,
       "alHardwarePs2Voltage5v": alHardwarePs2Voltage5v,
       "alHardwarePs2Voltage5vAlarm": alHardwarePs2Voltage5vAlarm,
       "alHardwarePs2Voltage5vCount": alHardwarePs2Voltage5vCount,
       "alHardwarePs2Voltage5vTime": alHardwarePs2Voltage5vTime,
       "alHardwareBoardVoltage3v": alHardwareBoardVoltage3v,
       "alHardwareBoardVoltage3vAlarm": alHardwareBoardVoltage3vAlarm,
       "alHardwareBoardVoltage3vCount": alHardwareBoardVoltage3vCount,
       "alHardwareBoardVoltage3vTime": alHardwareBoardVoltage3vTime,
       "alHardwareBoardVoltage5v": alHardwareBoardVoltage5v,
       "alHardwareBoardVoltage5vAlarm": alHardwareBoardVoltage5vAlarm,
       "alHardwareBoardVoltage5vCount": alHardwareBoardVoltage5vCount,
       "alHardwareBoardVoltage5vTime": alHardwareBoardVoltage5vTime,
       "alHardwareCpuTemp": alHardwareCpuTemp,
       "alHardwareCpuTempAlarm": alHardwareCpuTempAlarm,
       "alHardwareCpuTempCount": alHardwareCpuTempCount,
       "alHardwareCpuTempTime": alHardwareCpuTempTime,
       "alHardwareCageTemp": alHardwareCageTemp,
       "alHardwareCageTempAlarm": alHardwareCageTempAlarm,
       "alHardwareCageTempCount": alHardwareCageTempCount,
       "alHardwareCageTempTime": alHardwareCageTempTime,
       "alHardwareFan1Rpm": alHardwareFan1Rpm,
       "alHardwareFan1RpmAlarm": alHardwareFan1RpmAlarm,
       "alHardwareFan1RpmCount": alHardwareFan1RpmCount,
       "alHardwareFan1RpmTime": alHardwareFan1RpmTime,
       "alHardwareFan2Rpm": alHardwareFan2Rpm,
       "alHardwareFan2RpmAlarm": alHardwareFan2RpmAlarm,
       "alHardwareFan2RpmCount": alHardwareFan2RpmCount,
       "alHardwareFan2RpmTime": alHardwareFan2RpmTime,
       "alHardwareFan3Rpm": alHardwareFan3Rpm,
       "alHardwareFan3RpmAlarm": alHardwareFan3RpmAlarm,
       "alHardwareFan3RpmCount": alHardwareFan3RpmCount,
       "alHardwareFan3RpmTime": alHardwareFan3RpmTime,
       "alHardwarePs1Type": alHardwarePs1Type,
       "alHardwarePs2Type": alHardwarePs2Type,
       "alHardwareSlot1Card": alHardwareSlot1Card,
       "alHardwareSlot2Card": alHardwareSlot2Card,
       "alHardwareSlot3Card": alHardwareSlot3Card,
       "alHardwareSlot4Card": alHardwareSlot4Card,
       "alHardwareSlot1Operational": alHardwareSlot1Operational,
       "alHardwareSlot2Operational": alHardwareSlot2Operational,
       "alHardwareSlot3Operational": alHardwareSlot3Operational,
       "alHardwareSlot4Operational": alHardwareSlot4Operational,
       "alHardwareRamSize": alHardwareRamSize,
       "alHardwareChassis": alHardwareChassis,
       "alHardwareCpuVoltageNominal": alHardwareCpuVoltageNominal,
       "alHardwareClientEthPrivSwitch": alHardwareClientEthPrivSwitch,
       "alHardwareSerialNumber": alHardwareSerialNumber}
)
