# SNMP MIB module (ALPHA-RECTIFIER-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALPHA-RECTIFIER-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:46 2024
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

(ScaledNumber,
 simple) = mibBuilder.importSymbols(
    "ALPHA-RESOURCE-MIB",
    "ScaledNumber",
    "simple")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rectifierSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1)
)
rectifierSystem.setRevisions(
        ("2015-07-28 00:00",
         "2015-07-23 00:00",
         "2015-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RectSysTotalOutputCurrent_Type = ScaledNumber
_RectSysTotalOutputCurrent_Object = MibScalar
rectSysTotalOutputCurrent = _RectSysTotalOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 1),
    _RectSysTotalOutputCurrent_Type()
)
rectSysTotalOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalOutputCurrent.setStatus("current")
_RectSysTotalOutputPower_Type = ScaledNumber
_RectSysTotalOutputPower_Object = MibScalar
rectSysTotalOutputPower = _RectSysTotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 2),
    _RectSysTotalOutputPower_Type()
)
rectSysTotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalOutputPower.setStatus("current")
_RectSysTotalCapacityInstalledAmps_Type = ScaledNumber
_RectSysTotalCapacityInstalledAmps_Object = MibScalar
rectSysTotalCapacityInstalledAmps = _RectSysTotalCapacityInstalledAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 3),
    _RectSysTotalCapacityInstalledAmps_Type()
)
rectSysTotalCapacityInstalledAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalCapacityInstalledAmps.setStatus("current")
_RectSysTotalCapacityInstalledPower_Type = ScaledNumber
_RectSysTotalCapacityInstalledPower_Object = MibScalar
rectSysTotalCapacityInstalledPower = _RectSysTotalCapacityInstalledPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 4),
    _RectSysTotalCapacityInstalledPower_Type()
)
rectSysTotalCapacityInstalledPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalCapacityInstalledPower.setStatus("current")
_RectSysAverageRectifierOutputVoltage_Type = ScaledNumber
_RectSysAverageRectifierOutputVoltage_Object = MibScalar
rectSysAverageRectifierOutputVoltage = _RectSysAverageRectifierOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 5),
    _RectSysAverageRectifierOutputVoltage_Type()
)
rectSysAverageRectifierOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAverageRectifierOutputVoltage.setStatus("current")
_RectSysAverageRectifierACInputVoltage_Type = ScaledNumber
_RectSysAverageRectifierACInputVoltage_Object = MibScalar
rectSysAverageRectifierACInputVoltage = _RectSysAverageRectifierACInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 6),
    _RectSysAverageRectifierACInputVoltage_Type()
)
rectSysAverageRectifierACInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAverageRectifierACInputVoltage.setStatus("current")
_RectSysAveragePhase1Voltage_Type = ScaledNumber
_RectSysAveragePhase1Voltage_Object = MibScalar
rectSysAveragePhase1Voltage = _RectSysAveragePhase1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 7),
    _RectSysAveragePhase1Voltage_Type()
)
rectSysAveragePhase1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase1Voltage.setStatus("current")
_RectSysAveragePhase2Voltage_Type = ScaledNumber
_RectSysAveragePhase2Voltage_Object = MibScalar
rectSysAveragePhase2Voltage = _RectSysAveragePhase2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 8),
    _RectSysAveragePhase2Voltage_Type()
)
rectSysAveragePhase2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase2Voltage.setStatus("current")
_RectSysAveragePhase3Voltage_Type = ScaledNumber
_RectSysAveragePhase3Voltage_Object = MibScalar
rectSysAveragePhase3Voltage = _RectSysAveragePhase3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 9),
    _RectSysAveragePhase3Voltage_Type()
)
rectSysAveragePhase3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase3Voltage.setStatus("current")
_RectSysSystemVoltage_Type = ScaledNumber
_RectSysSystemVoltage_Object = MibScalar
rectSysSystemVoltage = _RectSysSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 10),
    _RectSysSystemVoltage_Type()
)
rectSysSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysSystemVoltage.setStatus("current")
_RectSysTotalLoadCurrent_Type = ScaledNumber
_RectSysTotalLoadCurrent_Object = MibScalar
rectSysTotalLoadCurrent = _RectSysTotalLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 11),
    _RectSysTotalLoadCurrent_Type()
)
rectSysTotalLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalLoadCurrent.setStatus("current")
_RectSysBatteryVoltage_Type = ScaledNumber
_RectSysBatteryVoltage_Object = MibScalar
rectSysBatteryVoltage = _RectSysBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 12),
    _RectSysBatteryVoltage_Type()
)
rectSysBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryVoltage.setStatus("current")
_RectSysBatteryCurrent_Type = ScaledNumber
_RectSysBatteryCurrent_Object = MibScalar
rectSysBatteryCurrent = _RectSysBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 13),
    _RectSysBatteryCurrent_Type()
)
rectSysBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryCurrent.setStatus("current")
_RectSysBatteryTemperature_Type = ScaledNumber
_RectSysBatteryTemperature_Object = MibScalar
rectSysBatteryTemperature = _RectSysBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 14),
    _RectSysBatteryTemperature_Type()
)
rectSysBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryTemperature.setStatus("current")
_RectSysSystemNumber_Type = ScaledNumber
_RectSysSystemNumber_Object = MibScalar
rectSysSystemNumber = _RectSysSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 15),
    _RectSysSystemNumber_Type()
)
rectSysSystemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysSystemNumber.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1)
)
_RectifierGroups_ObjectIdentity = ObjectIdentity
rectifierGroups = _RectifierGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2)
)

# Managed Objects groups

rectifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2, 1)
)
rectifierGroup.setObjects(
      *(("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierOutputVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierACInputVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase1Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase2Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase3Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalLoadCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryTemperature"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemNumber"))
)
if mibBuilder.loadTexts:
    rectifierGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-RECTIFIER-SYS-MIB",
    **{"rectifierSystem": rectifierSystem,
       "rectSysTotalOutputCurrent": rectSysTotalOutputCurrent,
       "rectSysTotalOutputPower": rectSysTotalOutputPower,
       "rectSysTotalCapacityInstalledAmps": rectSysTotalCapacityInstalledAmps,
       "rectSysTotalCapacityInstalledPower": rectSysTotalCapacityInstalledPower,
       "rectSysAverageRectifierOutputVoltage": rectSysAverageRectifierOutputVoltage,
       "rectSysAverageRectifierACInputVoltage": rectSysAverageRectifierACInputVoltage,
       "rectSysAveragePhase1Voltage": rectSysAveragePhase1Voltage,
       "rectSysAveragePhase2Voltage": rectSysAveragePhase2Voltage,
       "rectSysAveragePhase3Voltage": rectSysAveragePhase3Voltage,
       "rectSysSystemVoltage": rectSysSystemVoltage,
       "rectSysTotalLoadCurrent": rectSysTotalLoadCurrent,
       "rectSysBatteryVoltage": rectSysBatteryVoltage,
       "rectSysBatteryCurrent": rectSysBatteryCurrent,
       "rectSysBatteryTemperature": rectSysBatteryTemperature,
       "rectSysSystemNumber": rectSysSystemNumber,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "rectifierGroups": rectifierGroups,
       "rectifierGroup": rectifierGroup}
)
