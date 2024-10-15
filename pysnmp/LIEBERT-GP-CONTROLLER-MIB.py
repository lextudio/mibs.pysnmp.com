# SNMP MIB module (LIEBERT-GP-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:54 2024
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

(lgpController,
 liebertControllerModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpController",
    "liebertControllerModuleReg")

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

liebertControllerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7, 1)
)
liebertControllerModule.setRevisions(
        ("2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpCtrlNumberInstalledControlModules_Type = Integer32
_LgpCtrlNumberInstalledControlModules_Object = MibScalar
lgpCtrlNumberInstalledControlModules = _LgpCtrlNumberInstalledControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 1),
    _LgpCtrlNumberInstalledControlModules_Type()
)
lgpCtrlNumberInstalledControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberInstalledControlModules.setStatus("current")
_LgpCtrlNumberFailedControlModules_Type = Integer32
_LgpCtrlNumberFailedControlModules_Object = MibScalar
lgpCtrlNumberFailedControlModules = _LgpCtrlNumberFailedControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 2),
    _LgpCtrlNumberFailedControlModules_Type()
)
lgpCtrlNumberFailedControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberFailedControlModules.setStatus("current")
_LgpCtrlNumberRedundantControlModules_Type = Integer32
_LgpCtrlNumberRedundantControlModules_Object = MibScalar
lgpCtrlNumberRedundantControlModules = _LgpCtrlNumberRedundantControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 3),
    _LgpCtrlNumberRedundantControlModules_Type()
)
lgpCtrlNumberRedundantControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberRedundantControlModules.setStatus("current")
_LgpCtrlNumberControlModuleWarnings_Type = Integer32
_LgpCtrlNumberControlModuleWarnings_Object = MibScalar
lgpCtrlNumberControlModuleWarnings = _LgpCtrlNumberControlModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 5),
    _LgpCtrlNumberControlModuleWarnings_Type()
)
lgpCtrlNumberControlModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberControlModuleWarnings.setStatus("current")
_LgpCtrlBoardBatteryVoltage_Type = Unsigned32
_LgpCtrlBoardBatteryVoltage_Object = MibScalar
lgpCtrlBoardBatteryVoltage = _LgpCtrlBoardBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 6),
    _LgpCtrlBoardBatteryVoltage_Type()
)
lgpCtrlBoardBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlBoardBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lgpCtrlBoardBatteryVoltage.setUnits(".01 Volts")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-CONTROLLER-MIB",
    **{"liebertControllerModule": liebertControllerModule,
       "lgpCtrlNumberInstalledControlModules": lgpCtrlNumberInstalledControlModules,
       "lgpCtrlNumberFailedControlModules": lgpCtrlNumberFailedControlModules,
       "lgpCtrlNumberRedundantControlModules": lgpCtrlNumberRedundantControlModules,
       "lgpCtrlNumberControlModuleWarnings": lgpCtrlNumberControlModuleWarnings,
       "lgpCtrlBoardBatteryVoltage": lgpCtrlBoardBatteryVoltage}
)
