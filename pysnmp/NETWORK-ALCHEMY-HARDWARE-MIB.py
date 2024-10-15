# SNMP MIB module (NETWORK-ALCHEMY-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-ALCHEMY-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:16 2024
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

(hardware,
 netalModules) = mibBuilder.importSymbols(
    "NETAL-SMI",
    "hardware",
    "netalModules")

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

networkAlchemyHardwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5, 4)
)
networkAlchemyHardwareMIB.setRevisions(
        ("2000-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HardwarePrimaryCPU_Type = Integer32
_HardwarePrimaryCPU_Object = MibScalar
hardwarePrimaryCPU = _HardwarePrimaryCPU_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 1),
    _HardwarePrimaryCPU_Type()
)
hardwarePrimaryCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePrimaryCPU.setStatus("current")
_Hardwaresecondarycpu_Type = Integer32
_Hardwaresecondarycpu_Object = MibScalar
hardwaresecondarycpu = _Hardwaresecondarycpu_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 2),
    _Hardwaresecondarycpu_Type()
)
hardwaresecondarycpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwaresecondarycpu.setStatus("current")
_Hardwarehifnloadave_Type = Integer32
_Hardwarehifnloadave_Object = MibScalar
hardwarehifnloadave = _Hardwarehifnloadave_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 3),
    _Hardwarehifnloadave_Type()
)
hardwarehifnloadave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarehifnloadave.setStatus("current")
_Hardwarememoryusage_Type = Integer32
_Hardwarememoryusage_Object = MibScalar
hardwarememoryusage = _Hardwarememoryusage_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 4),
    _Hardwarememoryusage_Type()
)
hardwarememoryusage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarememoryusage.setStatus("current")
_Hardwarioload_Type = Integer32
_Hardwarioload_Object = MibScalar
hardwarioload = _Hardwarioload_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 5),
    _Hardwarioload_Type()
)
hardwarioload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarioload.setStatus("current")
_Hardwareuptime_Type = Integer32
_Hardwareuptime_Object = MibScalar
hardwareuptime = _Hardwareuptime_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 6),
    _Hardwareuptime_Type()
)
hardwareuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareuptime.setStatus("current")
_Hardwareosname_Type = DisplayString
_Hardwareosname_Object = MibScalar
hardwareosname = _Hardwareosname_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 7),
    _Hardwareosname_Type()
)
hardwareosname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareosname.setStatus("current")
_Hardwareosversion_Type = DisplayString
_Hardwareosversion_Object = MibScalar
hardwareosversion = _Hardwareosversion_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 8),
    _Hardwareosversion_Type()
)
hardwareosversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareosversion.setStatus("current")
_Hardwarecompileuser_Type = DisplayString
_Hardwarecompileuser_Object = MibScalar
hardwarecompileuser = _Hardwarecompileuser_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 9),
    _Hardwarecompileuser_Type()
)
hardwarecompileuser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarecompileuser.setStatus("current")
_Hardwarecompiledate_Type = DisplayString
_Hardwarecompiledate_Object = MibScalar
hardwarecompiledate = _Hardwarecompiledate_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 10),
    _Hardwarecompiledate_Type()
)
hardwarecompiledate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarecompiledate.setStatus("current")
_Hardwarecompilehost_Type = DisplayString
_Hardwarecompilehost_Object = MibScalar
hardwarecompilehost = _Hardwarecompilehost_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 11),
    _Hardwarecompilehost_Type()
)
hardwarecompilehost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarecompilehost.setStatus("current")
_Hardwareconfigversion_Type = Integer32
_Hardwareconfigversion_Object = MibScalar
hardwareconfigversion = _Hardwareconfigversion_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3, 12),
    _Hardwareconfigversion_Type()
)
hardwareconfigversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareconfigversion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-ALCHEMY-HARDWARE-MIB",
    **{"hardwarePrimaryCPU": hardwarePrimaryCPU,
       "hardwaresecondarycpu": hardwaresecondarycpu,
       "hardwarehifnloadave": hardwarehifnloadave,
       "hardwarememoryusage": hardwarememoryusage,
       "hardwarioload": hardwarioload,
       "hardwareuptime": hardwareuptime,
       "hardwareosname": hardwareosname,
       "hardwareosversion": hardwareosversion,
       "hardwarecompileuser": hardwarecompileuser,
       "hardwarecompiledate": hardwarecompiledate,
       "hardwarecompilehost": hardwarecompilehost,
       "hardwareconfigversion": hardwareconfigversion,
       "networkAlchemyHardwareMIB": networkAlchemyHardwareMIB}
)
