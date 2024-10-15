# SNMP MIB module (ALPHA-CONVERTER-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALPHA-CONVERTER-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:44 2024
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

converterSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2)
)
converterSystem.setRevisions(
        ("2015-07-28 00:00",
         "2015-07-23 00:00",
         "2015-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConvSysTotalOutputCurrent_Type = ScaledNumber
_ConvSysTotalOutputCurrent_Object = MibScalar
convSysTotalOutputCurrent = _ConvSysTotalOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 1),
    _ConvSysTotalOutputCurrent_Type()
)
convSysTotalOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysTotalOutputCurrent.setStatus("current")
_ConvSysTotalOutputPower_Type = ScaledNumber
_ConvSysTotalOutputPower_Object = MibScalar
convSysTotalOutputPower = _ConvSysTotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 2),
    _ConvSysTotalOutputPower_Type()
)
convSysTotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysTotalOutputPower.setStatus("current")
_ConvSysTotalCapacityInstalledAmps_Type = ScaledNumber
_ConvSysTotalCapacityInstalledAmps_Object = MibScalar
convSysTotalCapacityInstalledAmps = _ConvSysTotalCapacityInstalledAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 3),
    _ConvSysTotalCapacityInstalledAmps_Type()
)
convSysTotalCapacityInstalledAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysTotalCapacityInstalledAmps.setStatus("current")
_ConvSysTotalCapacityInstalledPower_Type = ScaledNumber
_ConvSysTotalCapacityInstalledPower_Object = MibScalar
convSysTotalCapacityInstalledPower = _ConvSysTotalCapacityInstalledPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 4),
    _ConvSysTotalCapacityInstalledPower_Type()
)
convSysTotalCapacityInstalledPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysTotalCapacityInstalledPower.setStatus("current")
_ConvSysAverageConverterOutputVoltage_Type = ScaledNumber
_ConvSysAverageConverterOutputVoltage_Object = MibScalar
convSysAverageConverterOutputVoltage = _ConvSysAverageConverterOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 5),
    _ConvSysAverageConverterOutputVoltage_Type()
)
convSysAverageConverterOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysAverageConverterOutputVoltage.setStatus("current")
_ConvSysAverageConverterInputVoltage_Type = ScaledNumber
_ConvSysAverageConverterInputVoltage_Object = MibScalar
convSysAverageConverterInputVoltage = _ConvSysAverageConverterInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 6),
    _ConvSysAverageConverterInputVoltage_Type()
)
convSysAverageConverterInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysAverageConverterInputVoltage.setStatus("current")
_ConvSysSystemVoltage_Type = ScaledNumber
_ConvSysSystemVoltage_Object = MibScalar
convSysSystemVoltage = _ConvSysSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 7),
    _ConvSysSystemVoltage_Type()
)
convSysSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysSystemVoltage.setStatus("current")
_ConvSysTotalLoadCurrent_Type = ScaledNumber
_ConvSysTotalLoadCurrent_Object = MibScalar
convSysTotalLoadCurrent = _ConvSysTotalLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 8),
    _ConvSysTotalLoadCurrent_Type()
)
convSysTotalLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysTotalLoadCurrent.setStatus("current")
_ConvSysSystemNumber_Type = ScaledNumber
_ConvSysSystemNumber_Object = MibScalar
convSysSystemNumber = _ConvSysSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 9),
    _ConvSysSystemNumber_Type()
)
convSysSystemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSysSystemNumber.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1)
)
_ConverterGroups_ObjectIdentity = ObjectIdentity
converterGroups = _ConverterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2)
)

# Managed Objects groups

converterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2, 1)
)
converterGroup.setObjects(
      *(("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputCurrent"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputPower"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledAmps"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledPower"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterOutputVoltage"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterInputVoltage"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemVoltage"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalLoadCurrent"),
        ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemNumber"))
)
if mibBuilder.loadTexts:
    converterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-CONVERTER-SYS-MIB",
    **{"converterSystem": converterSystem,
       "convSysTotalOutputCurrent": convSysTotalOutputCurrent,
       "convSysTotalOutputPower": convSysTotalOutputPower,
       "convSysTotalCapacityInstalledAmps": convSysTotalCapacityInstalledAmps,
       "convSysTotalCapacityInstalledPower": convSysTotalCapacityInstalledPower,
       "convSysAverageConverterOutputVoltage": convSysAverageConverterOutputVoltage,
       "convSysAverageConverterInputVoltage": convSysAverageConverterInputVoltage,
       "convSysSystemVoltage": convSysSystemVoltage,
       "convSysTotalLoadCurrent": convSysTotalLoadCurrent,
       "convSysSystemNumber": convSysSystemNumber,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "converterGroups": converterGroups,
       "converterGroup": converterGroup}
)
