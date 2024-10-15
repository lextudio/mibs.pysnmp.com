# SNMP MIB module (NOKIA-ALCHEMYOS-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ALCHEMYOS-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:32 2024
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

(alchemyOSModules,
 alchemyOSProducts,
 hardware) = mibBuilder.importSymbols(
    "NOKIA-ALCHEMYOS-MIB",
    "alchemyOSModules",
    "alchemyOSProducts",
    "hardware")

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

nokiaAlchemyOSHardwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 5, 4)
)
nokiaAlchemyOSHardwareMIB.setRevisions(
        ("2001-01-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HardwarePrimaryCPU_Type = Integer32
_HardwarePrimaryCPU_Object = MibScalar
hardwarePrimaryCPU = _HardwarePrimaryCPU_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 1),
    _HardwarePrimaryCPU_Type()
)
hardwarePrimaryCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePrimaryCPU.setStatus("current")
_HardwareSecondaryCpu_Type = Integer32
_HardwareSecondaryCpu_Object = MibScalar
hardwareSecondaryCpu = _HardwareSecondaryCpu_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 2),
    _HardwareSecondaryCpu_Type()
)
hardwareSecondaryCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareSecondaryCpu.setStatus("current")
_HardwareHifnLoadAve_Type = Integer32
_HardwareHifnLoadAve_Object = MibScalar
hardwareHifnLoadAve = _HardwareHifnLoadAve_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 3),
    _HardwareHifnLoadAve_Type()
)
hardwareHifnLoadAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareHifnLoadAve.setStatus("current")
_HardwareMemoryUsage_Type = Integer32
_HardwareMemoryUsage_Object = MibScalar
hardwareMemoryUsage = _HardwareMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 4),
    _HardwareMemoryUsage_Type()
)
hardwareMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMemoryUsage.setStatus("current")
_HardwarIOLoad_Type = Integer32
_HardwarIOLoad_Object = MibScalar
hardwarIOLoad = _HardwarIOLoad_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 5),
    _HardwarIOLoad_Type()
)
hardwarIOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarIOLoad.setStatus("current")
_HardwareUpTime_Type = Integer32
_HardwareUpTime_Object = MibScalar
hardwareUpTime = _HardwareUpTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 6),
    _HardwareUpTime_Type()
)
hardwareUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareUpTime.setStatus("current")
_HardwareOSName_Type = DisplayString
_HardwareOSName_Object = MibScalar
hardwareOSName = _HardwareOSName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 7),
    _HardwareOSName_Type()
)
hardwareOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareOSName.setStatus("current")
_HardwareOSVersion_Type = DisplayString
_HardwareOSVersion_Object = MibScalar
hardwareOSVersion = _HardwareOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 8),
    _HardwareOSVersion_Type()
)
hardwareOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareOSVersion.setStatus("current")
_HardwareCompileUser_Type = DisplayString
_HardwareCompileUser_Object = MibScalar
hardwareCompileUser = _HardwareCompileUser_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 9),
    _HardwareCompileUser_Type()
)
hardwareCompileUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCompileUser.setStatus("current")
_HardwareCompileDate_Type = DisplayString
_HardwareCompileDate_Object = MibScalar
hardwareCompileDate = _HardwareCompileDate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 10),
    _HardwareCompileDate_Type()
)
hardwareCompileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCompileDate.setStatus("current")
_HardwareCompileHost_Type = DisplayString
_HardwareCompileHost_Object = MibScalar
hardwareCompileHost = _HardwareCompileHost_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 11),
    _HardwareCompileHost_Type()
)
hardwareCompileHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareCompileHost.setStatus("current")
_HardwareConfigVersion_Type = Integer32
_HardwareConfigVersion_Object = MibScalar
hardwareConfigVersion = _HardwareConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2, 12),
    _HardwareConfigVersion_Type()
)
hardwareConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareConfigVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ALCHEMYOS-HARDWARE-MIB",
    **{"hardwarePrimaryCPU": hardwarePrimaryCPU,
       "hardwareSecondaryCpu": hardwareSecondaryCpu,
       "hardwareHifnLoadAve": hardwareHifnLoadAve,
       "hardwareMemoryUsage": hardwareMemoryUsage,
       "hardwarIOLoad": hardwarIOLoad,
       "hardwareUpTime": hardwareUpTime,
       "hardwareOSName": hardwareOSName,
       "hardwareOSVersion": hardwareOSVersion,
       "hardwareCompileUser": hardwareCompileUser,
       "hardwareCompileDate": hardwareCompileDate,
       "hardwareCompileHost": hardwareCompileHost,
       "hardwareConfigVersion": hardwareConfigVersion,
       "nokiaAlchemyOSHardwareMIB": nokiaAlchemyOSHardwareMIB}
)
