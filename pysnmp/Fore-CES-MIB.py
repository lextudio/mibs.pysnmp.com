# SNMP MIB module (Fore-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-CES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:52 2024
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

(asxd,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asxd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TestAndIncr,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval")


# MODULE-IDENTITY

cesExtGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesExtTable_Type = TestAndIncr
_CesExtTable_Object = MibScalar
cesExtTable = _CesExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 1),
    _CesExtTable_Type()
)
cesExtTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesExtTable.setStatus("current")
_CbrctConfTable_Object = MibTable
cbrctConfTable = _CbrctConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cbrctConfTable.setStatus("current")
_CbrctConfEntry_Object = MibTableRow
cbrctConfEntry = _CbrctConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1)
)
cbrctConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cbrctConfEntry.setStatus("current")


class _CbrctState_Type(Integer32):
    """Custom type cbrctState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CbrctState_Type.__name__ = "Integer32"
_CbrctState_Object = MibTableColumn
cbrctState = _CbrctState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 1),
    _CbrctState_Type()
)
cbrctState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctState.setStatus("current")


class _CbrctIdleDetection_Type(Integer32):
    """Custom type cbrctIdleDetection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("idlePattern", 1))
    )


_CbrctIdleDetection_Type.__name__ = "Integer32"
_CbrctIdleDetection_Object = MibTableColumn
cbrctIdleDetection = _CbrctIdleDetection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 2),
    _CbrctIdleDetection_Type()
)
cbrctIdleDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleDetection.setStatus("current")


class _CbrctIdleMask_Type(Integer32):
    """Custom type cbrctIdleMask based on Integer32"""
    defaultHexValue = 255


_CbrctIdleMask_Object = MibTableColumn
cbrctIdleMask = _CbrctIdleMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 3),
    _CbrctIdleMask_Type()
)
cbrctIdleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleMask.setStatus("current")


class _CbrctNoOfIdlePatterns_Type(Integer32):
    """Custom type cbrctNoOfIdlePatterns based on Integer32"""
    defaultValue = 2


_CbrctNoOfIdlePatterns_Object = MibTableColumn
cbrctNoOfIdlePatterns = _CbrctNoOfIdlePatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 4),
    _CbrctNoOfIdlePatterns_Type()
)
cbrctNoOfIdlePatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctNoOfIdlePatterns.setStatus("current")


class _CbrctIdlePatterns_Type(Integer32):
    """Custom type cbrctIdlePatterns based on Integer32"""
    defaultHexValue = 32767


_CbrctIdlePatterns_Object = MibTableColumn
cbrctIdlePatterns = _CbrctIdlePatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 5),
    _CbrctIdlePatterns_Type()
)
cbrctIdlePatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdlePatterns.setStatus("current")


class _CbrctIdleIntPeriod_Type(TimeInterval):
    """Custom type cbrctIdleIntPeriod based on TimeInterval"""
    defaultValue = 6


_CbrctIdleIntPeriod_Object = MibTableColumn
cbrctIdleIntPeriod = _CbrctIdleIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 6),
    _CbrctIdleIntPeriod_Type()
)
cbrctIdleIntPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleIntPeriod.setStatus("current")


class _CbrctActiveIntPeriod_Type(TimeInterval):
    """Custom type cbrctActiveIntPeriod based on TimeInterval"""
    defaultValue = 6


_CbrctActiveIntPeriod_Object = MibTableColumn
cbrctActiveIntPeriod = _CbrctActiveIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 7),
    _CbrctActiveIntPeriod_Type()
)
cbrctActiveIntPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctActiveIntPeriod.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-CES-MIB",
    **{"cesExtGroup": cesExtGroup,
       "cesExtTable": cesExtTable,
       "cbrctConfTable": cbrctConfTable,
       "cbrctConfEntry": cbrctConfEntry,
       "cbrctState": cbrctState,
       "cbrctIdleDetection": cbrctIdleDetection,
       "cbrctIdleMask": cbrctIdleMask,
       "cbrctNoOfIdlePatterns": cbrctNoOfIdlePatterns,
       "cbrctIdlePatterns": cbrctIdlePatterns,
       "cbrctIdleIntPeriod": cbrctIdleIntPeriod,
       "cbrctActiveIntPeriod": cbrctActiveIntPeriod}
)
