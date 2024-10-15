# SNMP MIB module (ERI-DNX-PERF-MONT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-PERF-MONT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:28 2024
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

(LinkPortAddress,
 dnx) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "LinkPortAddress",
    "dnx")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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

eriDNXLinkPMStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PerformanceMonitoring_ObjectIdentity = ObjectIdentity
performanceMonitoring = _PerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4)
)
_Dsx1Esf_ObjectIdentity = ObjectIdentity
dsx1Esf = _Dsx1Esf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1)
)
_Dsx1EsfCurrTable_Object = MibTable
dsx1EsfCurrTable = _Dsx1EsfCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1EsfCurrTable.setStatus("current")
_Dsx1EsfCurrEntry_Object = MibTableRow
dsx1EsfCurrEntry = _Dsx1EsfCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1)
)
dsx1EsfCurrEntry.setIndexNames(
    (0, "ERI-DNX-PERF-MONT-MIB", "dsx1EsfCurrLinkAddr"),
)
if mibBuilder.loadTexts:
    dsx1EsfCurrEntry.setStatus("current")
_Dsx1EsfCurrLinkAddr_Type = LinkPortAddress
_Dsx1EsfCurrLinkAddr_Object = MibTableColumn
dsx1EsfCurrLinkAddr = _Dsx1EsfCurrLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 1),
    _Dsx1EsfCurrLinkAddr_Type()
)
dsx1EsfCurrLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrLinkAddr.setStatus("current")
_Dsx1EsfCurrResrcId_Type = Integer32
_Dsx1EsfCurrResrcId_Object = MibTableColumn
dsx1EsfCurrResrcId = _Dsx1EsfCurrResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 2),
    _Dsx1EsfCurrResrcId_Type()
)
dsx1EsfCurrResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrResrcId.setStatus("current")


class _Dsx1EsfCurrESs_Type(Gauge32):
    """Custom type dsx1EsfCurrESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrESs_Type.__name__ = "Gauge32"
_Dsx1EsfCurrESs_Object = MibTableColumn
dsx1EsfCurrESs = _Dsx1EsfCurrESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 3),
    _Dsx1EsfCurrESs_Type()
)
dsx1EsfCurrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrESs.setStatus("current")


class _Dsx1EsfCurrUASs_Type(Gauge32):
    """Custom type dsx1EsfCurrUASs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrUASs_Type.__name__ = "Gauge32"
_Dsx1EsfCurrUASs_Object = MibTableColumn
dsx1EsfCurrUASs = _Dsx1EsfCurrUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 4),
    _Dsx1EsfCurrUASs_Type()
)
dsx1EsfCurrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrUASs.setStatus("current")


class _Dsx1EsfCurrSESs_Type(Gauge32):
    """Custom type dsx1EsfCurrSESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrSESs_Type.__name__ = "Gauge32"
_Dsx1EsfCurrSESs_Object = MibTableColumn
dsx1EsfCurrSESs = _Dsx1EsfCurrSESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 5),
    _Dsx1EsfCurrSESs_Type()
)
dsx1EsfCurrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrSESs.setStatus("current")


class _Dsx1EsfCurrBESs_Type(Gauge32):
    """Custom type dsx1EsfCurrBESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrBESs_Type.__name__ = "Gauge32"
_Dsx1EsfCurrBESs_Object = MibTableColumn
dsx1EsfCurrBESs = _Dsx1EsfCurrBESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 6),
    _Dsx1EsfCurrBESs_Type()
)
dsx1EsfCurrBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrBESs.setStatus("current")


class _Dsx1EsfCurrLOFs_Type(Gauge32):
    """Custom type dsx1EsfCurrLOFs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrLOFs_Type.__name__ = "Gauge32"
_Dsx1EsfCurrLOFs_Object = MibTableColumn
dsx1EsfCurrLOFs = _Dsx1EsfCurrLOFs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 7),
    _Dsx1EsfCurrLOFs_Type()
)
dsx1EsfCurrLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrLOFs.setStatus("current")


class _Dsx1EsfCurrSeconds_Type(Gauge32):
    """Custom type dsx1EsfCurrSeconds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1EsfCurrSeconds_Type.__name__ = "Gauge32"
_Dsx1EsfCurrSeconds_Object = MibTableColumn
dsx1EsfCurrSeconds = _Dsx1EsfCurrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 8),
    _Dsx1EsfCurrSeconds_Type()
)
dsx1EsfCurrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrSeconds.setStatus("current")


class _Dsx1EsfCurrIntervals_Type(Gauge32):
    """Custom type dsx1EsfCurrIntervals based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx1EsfCurrIntervals_Type.__name__ = "Gauge32"
_Dsx1EsfCurrIntervals_Object = MibTableColumn
dsx1EsfCurrIntervals = _Dsx1EsfCurrIntervals_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 9),
    _Dsx1EsfCurrIntervals_Type()
)
dsx1EsfCurrIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrIntervals.setStatus("current")


class _Dsx1EsfCurrStatus_Type(DisplayString):
    """Custom type dsx1EsfCurrStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Dsx1EsfCurrStatus_Type.__name__ = "DisplayString"
_Dsx1EsfCurrStatus_Object = MibTableColumn
dsx1EsfCurrStatus = _Dsx1EsfCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 10),
    _Dsx1EsfCurrStatus_Type()
)
dsx1EsfCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EsfCurrStatus.setStatus("current")
_Dsx1Esf24HrTable_Object = MibTable
dsx1Esf24HrTable = _Dsx1Esf24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dsx1Esf24HrTable.setStatus("current")
_Dsx1Esf24HrEntry_Object = MibTableRow
dsx1Esf24HrEntry = _Dsx1Esf24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1)
)
dsx1Esf24HrEntry.setIndexNames(
    (0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf24HrLinkAddr"),
)
if mibBuilder.loadTexts:
    dsx1Esf24HrEntry.setStatus("current")
_Dsx1Esf24HrLinkAddr_Type = LinkPortAddress
_Dsx1Esf24HrLinkAddr_Object = MibTableColumn
dsx1Esf24HrLinkAddr = _Dsx1Esf24HrLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 1),
    _Dsx1Esf24HrLinkAddr_Type()
)
dsx1Esf24HrLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrLinkAddr.setStatus("current")
_Dsx1Esf24HrResrcId_Type = Integer32
_Dsx1Esf24HrResrcId_Object = MibTableColumn
dsx1Esf24HrResrcId = _Dsx1Esf24HrResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 2),
    _Dsx1Esf24HrResrcId_Type()
)
dsx1Esf24HrResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrResrcId.setStatus("current")


class _Dsx1Esf24HrESs_Type(Gauge32):
    """Custom type dsx1Esf24HrESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dsx1Esf24HrESs_Type.__name__ = "Gauge32"
_Dsx1Esf24HrESs_Object = MibTableColumn
dsx1Esf24HrESs = _Dsx1Esf24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 3),
    _Dsx1Esf24HrESs_Type()
)
dsx1Esf24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrESs.setStatus("current")


class _Dsx1Esf24HrUASs_Type(Gauge32):
    """Custom type dsx1Esf24HrUASs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dsx1Esf24HrUASs_Type.__name__ = "Gauge32"
_Dsx1Esf24HrUASs_Object = MibTableColumn
dsx1Esf24HrUASs = _Dsx1Esf24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 4),
    _Dsx1Esf24HrUASs_Type()
)
dsx1Esf24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrUASs.setStatus("current")


class _Dsx1Esf24HrSESs_Type(Gauge32):
    """Custom type dsx1Esf24HrSESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dsx1Esf24HrSESs_Type.__name__ = "Gauge32"
_Dsx1Esf24HrSESs_Object = MibTableColumn
dsx1Esf24HrSESs = _Dsx1Esf24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 5),
    _Dsx1Esf24HrSESs_Type()
)
dsx1Esf24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrSESs.setStatus("current")


class _Dsx1Esf24HrBESs_Type(Gauge32):
    """Custom type dsx1Esf24HrBESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dsx1Esf24HrBESs_Type.__name__ = "Gauge32"
_Dsx1Esf24HrBESs_Object = MibTableColumn
dsx1Esf24HrBESs = _Dsx1Esf24HrBESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 6),
    _Dsx1Esf24HrBESs_Type()
)
dsx1Esf24HrBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrBESs.setStatus("current")


class _Dsx1Esf24HrLOFs_Type(Gauge32):
    """Custom type dsx1Esf24HrLOFs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dsx1Esf24HrLOFs_Type.__name__ = "Gauge32"
_Dsx1Esf24HrLOFs_Object = MibTableColumn
dsx1Esf24HrLOFs = _Dsx1Esf24HrLOFs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 7),
    _Dsx1Esf24HrLOFs_Type()
)
dsx1Esf24HrLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf24HrLOFs.setStatus("current")
_Dsx1Esf96RegTable_Object = MibTable
dsx1Esf96RegTable = _Dsx1Esf96RegTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dsx1Esf96RegTable.setStatus("current")
_Dsx1Esf96RegEntry_Object = MibTableRow
dsx1Esf96RegEntry = _Dsx1Esf96RegEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1)
)
dsx1Esf96RegEntry.setIndexNames(
    (0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf96RegLinkAddr"),
    (0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf96RegInterval"),
)
if mibBuilder.loadTexts:
    dsx1Esf96RegEntry.setStatus("current")
_Dsx1Esf96RegLinkAddr_Type = LinkPortAddress
_Dsx1Esf96RegLinkAddr_Object = MibTableColumn
dsx1Esf96RegLinkAddr = _Dsx1Esf96RegLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 1),
    _Dsx1Esf96RegLinkAddr_Type()
)
dsx1Esf96RegLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegLinkAddr.setStatus("current")


class _Dsx1Esf96RegInterval_Type(Integer32):
    """Custom type dsx1Esf96RegInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx1Esf96RegInterval_Type.__name__ = "Integer32"
_Dsx1Esf96RegInterval_Object = MibTableColumn
dsx1Esf96RegInterval = _Dsx1Esf96RegInterval_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 2),
    _Dsx1Esf96RegInterval_Type()
)
dsx1Esf96RegInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegInterval.setStatus("current")


class _Dsx1Esf96RegESs_Type(Gauge32):
    """Custom type dsx1Esf96RegESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1Esf96RegESs_Type.__name__ = "Gauge32"
_Dsx1Esf96RegESs_Object = MibTableColumn
dsx1Esf96RegESs = _Dsx1Esf96RegESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 3),
    _Dsx1Esf96RegESs_Type()
)
dsx1Esf96RegESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegESs.setStatus("current")


class _Dsx1Esf96RegUASs_Type(Gauge32):
    """Custom type dsx1Esf96RegUASs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1Esf96RegUASs_Type.__name__ = "Gauge32"
_Dsx1Esf96RegUASs_Object = MibTableColumn
dsx1Esf96RegUASs = _Dsx1Esf96RegUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 4),
    _Dsx1Esf96RegUASs_Type()
)
dsx1Esf96RegUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegUASs.setStatus("current")


class _Dsx1Esf96RegSESs_Type(Gauge32):
    """Custom type dsx1Esf96RegSESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1Esf96RegSESs_Type.__name__ = "Gauge32"
_Dsx1Esf96RegSESs_Object = MibTableColumn
dsx1Esf96RegSESs = _Dsx1Esf96RegSESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 5),
    _Dsx1Esf96RegSESs_Type()
)
dsx1Esf96RegSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegSESs.setStatus("current")


class _Dsx1Esf96RegBESs_Type(Gauge32):
    """Custom type dsx1Esf96RegBESs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1Esf96RegBESs_Type.__name__ = "Gauge32"
_Dsx1Esf96RegBESs_Object = MibTableColumn
dsx1Esf96RegBESs = _Dsx1Esf96RegBESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 6),
    _Dsx1Esf96RegBESs_Type()
)
dsx1Esf96RegBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1Esf96RegBESs.setStatus("current")
_Dsx1G826_ObjectIdentity = ObjectIdentity
dsx1G826 = _Dsx1G826_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2)
)
_Dsx1G826Table_Object = MibTable
dsx1G826Table = _Dsx1G826Table_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsx1G826Table.setStatus("current")
_Dsx1G826Entry_Object = MibTableRow
dsx1G826Entry = _Dsx1G826Entry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1)
)
dsx1G826Entry.setIndexNames(
    (0, "ERI-DNX-PERF-MONT-MIB", "dsx1G826LinkAddr"),
)
if mibBuilder.loadTexts:
    dsx1G826Entry.setStatus("current")
_Dsx1G826LinkAddr_Type = LinkPortAddress
_Dsx1G826LinkAddr_Object = MibTableColumn
dsx1G826LinkAddr = _Dsx1G826LinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 1),
    _Dsx1G826LinkAddr_Type()
)
dsx1G826LinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826LinkAddr.setStatus("current")
_Dsx1G826ResrcId_Type = Integer32
_Dsx1G826ResrcId_Object = MibTableColumn
dsx1G826ResrcId = _Dsx1G826ResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 2),
    _Dsx1G826ResrcId_Type()
)
dsx1G826ResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ResrcId.setStatus("current")
_Dsx1G826TotalTime_Type = Integer32
_Dsx1G826TotalTime_Object = MibTableColumn
dsx1G826TotalTime = _Dsx1G826TotalTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 3),
    _Dsx1G826TotalTime_Type()
)
dsx1G826TotalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1G826TotalTime.setStatus("current")
_Dsx1G826ESs_Type = Gauge32
_Dsx1G826ESs_Object = MibTableColumn
dsx1G826ESs = _Dsx1G826ESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 4),
    _Dsx1G826ESs_Type()
)
dsx1G826ESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ESs.setStatus("current")
_Dsx1G826ErrFSs_Type = Gauge32
_Dsx1G826ErrFSs_Object = MibTableColumn
dsx1G826ErrFSs = _Dsx1G826ErrFSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 5),
    _Dsx1G826ErrFSs_Type()
)
dsx1G826ErrFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ErrFSs.setStatus("current")
_Dsx1G826SESs_Type = Gauge32
_Dsx1G826SESs_Object = MibTableColumn
dsx1G826SESs = _Dsx1G826SESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 6),
    _Dsx1G826SESs_Type()
)
dsx1G826SESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826SESs.setStatus("current")
_Dsx1G826ConsecSESs_Type = Gauge32
_Dsx1G826ConsecSESs_Object = MibTableColumn
dsx1G826ConsecSESs = _Dsx1G826ConsecSESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 7),
    _Dsx1G826ConsecSESs_Type()
)
dsx1G826ConsecSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ConsecSESs.setStatus("current")
_Dsx1G826ConsecErrFSs_Type = Gauge32
_Dsx1G826ConsecErrFSs_Object = MibTableColumn
dsx1G826ConsecErrFSs = _Dsx1G826ConsecErrFSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 8),
    _Dsx1G826ConsecErrFSs_Type()
)
dsx1G826ConsecErrFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ConsecErrFSs.setStatus("current")
_Dsx1G826BGErrBlocks_Type = Gauge32
_Dsx1G826BGErrBlocks_Object = MibTableColumn
dsx1G826BGErrBlocks = _Dsx1G826BGErrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 9),
    _Dsx1G826BGErrBlocks_Type()
)
dsx1G826BGErrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826BGErrBlocks.setStatus("current")
_Dsx1G826ESRatio_Type = DisplayString
_Dsx1G826ESRatio_Object = MibTableColumn
dsx1G826ESRatio = _Dsx1G826ESRatio_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 10),
    _Dsx1G826ESRatio_Type()
)
dsx1G826ESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826ESRatio.setStatus("current")
_Dsx1G826SESRatio_Type = DisplayString
_Dsx1G826SESRatio_Object = MibTableColumn
dsx1G826SESRatio = _Dsx1G826SESRatio_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 11),
    _Dsx1G826SESRatio_Type()
)
dsx1G826SESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826SESRatio.setStatus("current")
_Dsx1G826BgBERRatio_Type = DisplayString
_Dsx1G826BgBERRatio_Object = MibTableColumn
dsx1G826BgBERRatio = _Dsx1G826BgBERRatio_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 12),
    _Dsx1G826BgBERRatio_Type()
)
dsx1G826BgBERRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826BgBERRatio.setStatus("current")
_Dsx1G826UASs_Type = Gauge32
_Dsx1G826UASs_Object = MibTableColumn
dsx1G826UASs = _Dsx1G826UASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 13),
    _Dsx1G826UASs_Type()
)
dsx1G826UASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1G826UASs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-PERF-MONT-MIB",
    **{"performanceMonitoring": performanceMonitoring,
       "dsx1Esf": dsx1Esf,
       "dsx1EsfCurrTable": dsx1EsfCurrTable,
       "dsx1EsfCurrEntry": dsx1EsfCurrEntry,
       "dsx1EsfCurrLinkAddr": dsx1EsfCurrLinkAddr,
       "dsx1EsfCurrResrcId": dsx1EsfCurrResrcId,
       "dsx1EsfCurrESs": dsx1EsfCurrESs,
       "dsx1EsfCurrUASs": dsx1EsfCurrUASs,
       "dsx1EsfCurrSESs": dsx1EsfCurrSESs,
       "dsx1EsfCurrBESs": dsx1EsfCurrBESs,
       "dsx1EsfCurrLOFs": dsx1EsfCurrLOFs,
       "dsx1EsfCurrSeconds": dsx1EsfCurrSeconds,
       "dsx1EsfCurrIntervals": dsx1EsfCurrIntervals,
       "dsx1EsfCurrStatus": dsx1EsfCurrStatus,
       "dsx1Esf24HrTable": dsx1Esf24HrTable,
       "dsx1Esf24HrEntry": dsx1Esf24HrEntry,
       "dsx1Esf24HrLinkAddr": dsx1Esf24HrLinkAddr,
       "dsx1Esf24HrResrcId": dsx1Esf24HrResrcId,
       "dsx1Esf24HrESs": dsx1Esf24HrESs,
       "dsx1Esf24HrUASs": dsx1Esf24HrUASs,
       "dsx1Esf24HrSESs": dsx1Esf24HrSESs,
       "dsx1Esf24HrBESs": dsx1Esf24HrBESs,
       "dsx1Esf24HrLOFs": dsx1Esf24HrLOFs,
       "dsx1Esf96RegTable": dsx1Esf96RegTable,
       "dsx1Esf96RegEntry": dsx1Esf96RegEntry,
       "dsx1Esf96RegLinkAddr": dsx1Esf96RegLinkAddr,
       "dsx1Esf96RegInterval": dsx1Esf96RegInterval,
       "dsx1Esf96RegESs": dsx1Esf96RegESs,
       "dsx1Esf96RegUASs": dsx1Esf96RegUASs,
       "dsx1Esf96RegSESs": dsx1Esf96RegSESs,
       "dsx1Esf96RegBESs": dsx1Esf96RegBESs,
       "dsx1G826": dsx1G826,
       "dsx1G826Table": dsx1G826Table,
       "dsx1G826Entry": dsx1G826Entry,
       "dsx1G826LinkAddr": dsx1G826LinkAddr,
       "dsx1G826ResrcId": dsx1G826ResrcId,
       "dsx1G826TotalTime": dsx1G826TotalTime,
       "dsx1G826ESs": dsx1G826ESs,
       "dsx1G826ErrFSs": dsx1G826ErrFSs,
       "dsx1G826SESs": dsx1G826SESs,
       "dsx1G826ConsecSESs": dsx1G826ConsecSESs,
       "dsx1G826ConsecErrFSs": dsx1G826ConsecErrFSs,
       "dsx1G826BGErrBlocks": dsx1G826BGErrBlocks,
       "dsx1G826ESRatio": dsx1G826ESRatio,
       "dsx1G826SESRatio": dsx1G826SESRatio,
       "dsx1G826BgBERRatio": dsx1G826BgBERRatio,
       "dsx1G826UASs": dsx1G826UASs,
       "eriDNXLinkPMStatsMIB": eriDNXLinkPMStatsMIB}
)
