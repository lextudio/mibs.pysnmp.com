# SNMP MIB module (CXACTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXACTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:02 2024
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

(cxACTE,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxACTE")

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

_ActeDebugTable_Object = MibTable
acteDebugTable = _ActeDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30)
)
if mibBuilder.loadTexts:
    acteDebugTable.setStatus("mandatory")
_ActeDebugEntry_Object = MibTableRow
acteDebugEntry = _ActeDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1)
)
acteDebugEntry.setIndexNames(
    (0, "CXACTE-MIB", "acteDebugLinkIndex"),
    (0, "CXACTE-MIB", "acteDebugIndex"),
)
if mibBuilder.loadTexts:
    acteDebugEntry.setStatus("mandatory")


class _ActeDebugLinkIndex_Type(Integer32):
    """Custom type acteDebugLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ActeDebugLinkIndex_Type.__name__ = "Integer32"
_ActeDebugLinkIndex_Object = MibTableColumn
acteDebugLinkIndex = _ActeDebugLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 1),
    _ActeDebugLinkIndex_Type()
)
acteDebugLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acteDebugLinkIndex.setStatus("mandatory")


class _ActeDebugIndex_Type(Integer32):
    """Custom type acteDebugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ActeDebugIndex_Type.__name__ = "Integer32"
_ActeDebugIndex_Object = MibTableColumn
acteDebugIndex = _ActeDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 2),
    _ActeDebugIndex_Type()
)
acteDebugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acteDebugIndex.setStatus("mandatory")


class _ActeDebugRegister_Type(DisplayString):
    """Custom type acteDebugRegister based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ActeDebugRegister_Type.__name__ = "DisplayString"
_ActeDebugRegister_Object = MibTableColumn
acteDebugRegister = _ActeDebugRegister_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 10),
    _ActeDebugRegister_Type()
)
acteDebugRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acteDebugRegister.setStatus("mandatory")


class _ActeDebugResult_Type(DisplayString):
    """Custom type acteDebugResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ActeDebugResult_Type.__name__ = "DisplayString"
_ActeDebugResult_Object = MibTableColumn
acteDebugResult = _ActeDebugResult_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 50),
    _ActeDebugResult_Type()
)
acteDebugResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acteDebugResult.setStatus("mandatory")


class _ActeDebugWrite_Type(DisplayString):
    """Custom type acteDebugWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_ActeDebugWrite_Type.__name__ = "DisplayString"
_ActeDebugWrite_Object = MibTableColumn
acteDebugWrite = _ActeDebugWrite_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 80),
    _ActeDebugWrite_Type()
)
acteDebugWrite.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acteDebugWrite.setStatus("mandatory")


class _ActeDebugTvdStat_Type(Integer32):
    """Custom type acteDebugTvdStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ActeDebugTvdStat_Type.__name__ = "Integer32"
_ActeDebugTvdStat_Object = MibTableColumn
acteDebugTvdStat = _ActeDebugTvdStat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 81),
    _ActeDebugTvdStat_Type()
)
acteDebugTvdStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acteDebugTvdStat.setStatus("mandatory")


class _ActeDebugDs1Stat_Type(Integer32):
    """Custom type acteDebugDs1Stat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ActeDebugDs1Stat_Type.__name__ = "Integer32"
_ActeDebugDs1Stat_Object = MibTableColumn
acteDebugDs1Stat = _ActeDebugDs1Stat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 82),
    _ActeDebugDs1Stat_Type()
)
acteDebugDs1Stat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acteDebugDs1Stat.setStatus("mandatory")


class _ActeDebugSvdStat_Type(Integer32):
    """Custom type acteDebugSvdStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ActeDebugSvdStat_Type.__name__ = "Integer32"
_ActeDebugSvdStat_Object = MibTableColumn
acteDebugSvdStat = _ActeDebugSvdStat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 83),
    _ActeDebugSvdStat_Type()
)
acteDebugSvdStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acteDebugSvdStat.setStatus("mandatory")


class _ActeDebugSvdEvt_Type(Integer32):
    """Custom type acteDebugSvdEvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ActeDebugSvdEvt_Type.__name__ = "Integer32"
_ActeDebugSvdEvt_Object = MibTableColumn
acteDebugSvdEvt = _ActeDebugSvdEvt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 84),
    _ActeDebugSvdEvt_Type()
)
acteDebugSvdEvt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acteDebugSvdEvt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXACTE-MIB",
    **{"acteDebugTable": acteDebugTable,
       "acteDebugEntry": acteDebugEntry,
       "acteDebugLinkIndex": acteDebugLinkIndex,
       "acteDebugIndex": acteDebugIndex,
       "acteDebugRegister": acteDebugRegister,
       "acteDebugResult": acteDebugResult,
       "acteDebugWrite": acteDebugWrite,
       "acteDebugTvdStat": acteDebugTvdStat,
       "acteDebugDs1Stat": acteDebugDs1Stat,
       "acteDebugSvdStat": acteDebugSvdStat,
       "acteDebugSvdEvt": acteDebugSvdEvt}
)
