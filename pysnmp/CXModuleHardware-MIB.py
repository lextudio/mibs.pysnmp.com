# SNMP MIB module (CXModuleHardware-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXModuleHardware-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:26 2024
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

(Alias,
 cxModuleHardware) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxModuleHardware")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxModuleHwAlias_Type = Alias
_CxModuleHwAlias_Object = MibScalar
cxModuleHwAlias = _CxModuleHwAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 1),
    _CxModuleHwAlias_Type()
)
cxModuleHwAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxModuleHwAlias.setStatus("mandatory")
_CxModuleHwRevAssemblyAndEco_Type = Integer32
_CxModuleHwRevAssemblyAndEco_Object = MibScalar
cxModuleHwRevAssemblyAndEco = _CxModuleHwRevAssemblyAndEco_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 2),
    _CxModuleHwRevAssemblyAndEco_Type()
)
cxModuleHwRevAssemblyAndEco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwRevAssemblyAndEco.setStatus("mandatory")
_CxModuleHwPhysSlot_Type = Integer32
_CxModuleHwPhysSlot_Object = MibScalar
cxModuleHwPhysSlot = _CxModuleHwPhysSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 3),
    _CxModuleHwPhysSlot_Type()
)
cxModuleHwPhysSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwPhysSlot.setStatus("mandatory")
_CxModuleHwCpuClockSpeed_Type = Integer32
_CxModuleHwCpuClockSpeed_Object = MibScalar
cxModuleHwCpuClockSpeed = _CxModuleHwCpuClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 4),
    _CxModuleHwCpuClockSpeed_Type()
)
cxModuleHwCpuClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwCpuClockSpeed.setStatus("mandatory")
_CxModuleHwLedsDisplay_Type = Integer32
_CxModuleHwLedsDisplay_Object = MibScalar
cxModuleHwLedsDisplay = _CxModuleHwLedsDisplay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 5),
    _CxModuleHwLedsDisplay_Type()
)
cxModuleHwLedsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwLedsDisplay.setStatus("mandatory")
_CxModuleHwFlashEpromSize_Type = Integer32
_CxModuleHwFlashEpromSize_Object = MibScalar
cxModuleHwFlashEpromSize = _CxModuleHwFlashEpromSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 7),
    _CxModuleHwFlashEpromSize_Type()
)
cxModuleHwFlashEpromSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwFlashEpromSize.setStatus("mandatory")
_CxModuleHwPrivateDramSize_Type = Integer32
_CxModuleHwPrivateDramSize_Object = MibScalar
cxModuleHwPrivateDramSize = _CxModuleHwPrivateDramSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 8),
    _CxModuleHwPrivateDramSize_Type()
)
cxModuleHwPrivateDramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwPrivateDramSize.setStatus("mandatory")
_CxModuleHwSharedDramSize_Type = Integer32
_CxModuleHwSharedDramSize_Object = MibScalar
cxModuleHwSharedDramSize = _CxModuleHwSharedDramSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 9),
    _CxModuleHwSharedDramSize_Type()
)
cxModuleHwSharedDramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwSharedDramSize.setStatus("mandatory")
_CxModuleHwUpTimeTicks_Type = TimeTicks
_CxModuleHwUpTimeTicks_Object = MibScalar
cxModuleHwUpTimeTicks = _CxModuleHwUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 12),
    _CxModuleHwUpTimeTicks_Type()
)
cxModuleHwUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwUpTimeTicks.setStatus("mandatory")
_CxModuleHwResetTimeOut_Type = Integer32
_CxModuleHwResetTimeOut_Object = MibScalar
cxModuleHwResetTimeOut = _CxModuleHwResetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 13),
    _CxModuleHwResetTimeOut_Type()
)
cxModuleHwResetTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxModuleHwResetTimeOut.setStatus("mandatory")
_CxModuleHwSwVersion_Type = DisplayString
_CxModuleHwSwVersion_Object = MibScalar
cxModuleHwSwVersion = _CxModuleHwSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 14),
    _CxModuleHwSwVersion_Type()
)
cxModuleHwSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxModuleHwSwVersion.setStatus("mandatory")


class _CxModuleHwNodeId_Type(Integer32):
    """Custom type cxModuleHwNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxModuleHwNodeId_Type.__name__ = "Integer32"
_CxModuleHwNodeId_Object = MibScalar
cxModuleHwNodeId = _CxModuleHwNodeId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1, 15),
    _CxModuleHwNodeId_Type()
)
cxModuleHwNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxModuleHwNodeId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXModuleHardware-MIB",
    **{"cxModuleHwAlias": cxModuleHwAlias,
       "cxModuleHwRevAssemblyAndEco": cxModuleHwRevAssemblyAndEco,
       "cxModuleHwPhysSlot": cxModuleHwPhysSlot,
       "cxModuleHwCpuClockSpeed": cxModuleHwCpuClockSpeed,
       "cxModuleHwLedsDisplay": cxModuleHwLedsDisplay,
       "cxModuleHwFlashEpromSize": cxModuleHwFlashEpromSize,
       "cxModuleHwPrivateDramSize": cxModuleHwPrivateDramSize,
       "cxModuleHwSharedDramSize": cxModuleHwSharedDramSize,
       "cxModuleHwUpTimeTicks": cxModuleHwUpTimeTicks,
       "cxModuleHwResetTimeOut": cxModuleHwResetTimeOut,
       "cxModuleHwSwVersion": cxModuleHwSwVersion,
       "cxModuleHwNodeId": cxModuleHwNodeId}
)
