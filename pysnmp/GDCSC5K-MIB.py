# SNMP MIB module (GDCSC5K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCSC5K-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:18 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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
 enterprises,
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
    "enterprises",
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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Sc_ObjectIdentity = ObjectIdentity
sc = _Sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3)
)
_Sc5000_ObjectIdentity = ObjectIdentity
sc5000 = _Sc5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2)
)
_GdcSc5000Version_ObjectIdentity = ObjectIdentity
gdcSc5000Version = _GdcSc5000Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 1)
)


class _GdcSc5000MIBVersion_Type(DisplayString):
    """Custom type gdcSc5000MIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcSc5000MIBVersion_Type.__name__ = "DisplayString"
_GdcSc5000MIBVersion_Object = MibScalar
gdcSc5000MIBVersion = _GdcSc5000MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 1, 1),
    _GdcSc5000MIBVersion_Type()
)
gdcSc5000MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcSc5000MIBVersion.setStatus("mandatory")
_GdcSc5000Timing_ObjectIdentity = ObjectIdentity
gdcSc5000Timing = _GdcSc5000Timing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 2)
)
_GdcSc5000TimingTable_Object = MibTable
gdcSc5000TimingTable = _GdcSc5000TimingTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gdcSc5000TimingTable.setStatus("obsolete")
_GdcSc5000TimingEntry_Object = MibTableRow
gdcSc5000TimingEntry = _GdcSc5000TimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 2, 1, 1)
)
gdcSc5000TimingEntry.setIndexNames(
    (0, "GDCSC5K-MIB", "gdcSc5000TimingIndex"),
)
if mibBuilder.loadTexts:
    gdcSc5000TimingEntry.setStatus("obsolete")
_GdcSc5000TimingIndex_Type = SCinstance
_GdcSc5000TimingIndex_Object = MibTableColumn
gdcSc5000TimingIndex = _GdcSc5000TimingIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 2, 1, 1, 1),
    _GdcSc5000TimingIndex_Type()
)
gdcSc5000TimingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcSc5000TimingIndex.setStatus("obsolete")


class _GdcSc5000SrcShelfTiming_Type(Integer32):
    """Custom type gdcSc5000SrcShelfTiming based on Integer32"""
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
        *(("eightKiloClk", 3),
          ("fourMegAnd8kClk", 4),
          ("fourMegClk", 2),
          ("inhibit", 1))
    )


_GdcSc5000SrcShelfTiming_Type.__name__ = "Integer32"
_GdcSc5000SrcShelfTiming_Object = MibTableColumn
gdcSc5000SrcShelfTiming = _GdcSc5000SrcShelfTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 2, 1, 1, 2),
    _GdcSc5000SrcShelfTiming_Type()
)
gdcSc5000SrcShelfTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcSc5000SrcShelfTiming.setStatus("obsolete")
_GdcSc5000Shelf_ObjectIdentity = ObjectIdentity
gdcSc5000Shelf = _GdcSc5000Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3)
)


class _Sc5000ShelfNodeTypes_Type(OctetString):
    """Custom type sc5000ShelfNodeTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Sc5000ShelfNodeTypes_Type.__name__ = "OctetString"
_Sc5000ShelfNodeTypes_Object = MibScalar
sc5000ShelfNodeTypes = _Sc5000ShelfNodeTypes_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 1),
    _Sc5000ShelfNodeTypes_Type()
)
sc5000ShelfNodeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000ShelfNodeTypes.setStatus("mandatory")


class _Sc5000ShelfAdminStatus_Type(OctetString):
    """Custom type sc5000ShelfAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Sc5000ShelfAdminStatus_Type.__name__ = "OctetString"
_Sc5000ShelfAdminStatus_Object = MibScalar
sc5000ShelfAdminStatus = _Sc5000ShelfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 2),
    _Sc5000ShelfAdminStatus_Type()
)
sc5000ShelfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfAdminStatus.setStatus("mandatory")


class _Sc5000ShelfOperStatus_Type(OctetString):
    """Custom type sc5000ShelfOperStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Sc5000ShelfOperStatus_Type.__name__ = "OctetString"
_Sc5000ShelfOperStatus_Object = MibScalar
sc5000ShelfOperStatus = _Sc5000ShelfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 3),
    _Sc5000ShelfOperStatus_Type()
)
sc5000ShelfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000ShelfOperStatus.setStatus("mandatory")


class _Sc5000ShelfClockProvider_Type(OctetString):
    """Custom type sc5000ShelfClockProvider based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sc5000ShelfClockProvider_Type.__name__ = "OctetString"
_Sc5000ShelfClockProvider_Object = MibScalar
sc5000ShelfClockProvider = _Sc5000ShelfClockProvider_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 4),
    _Sc5000ShelfClockProvider_Type()
)
sc5000ShelfClockProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfClockProvider.setStatus("obsolete")


class _Sc5000ShelfLTUHwayAssgn_Type(OctetString):
    """Custom type sc5000ShelfLTUHwayAssgn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sc5000ShelfLTUHwayAssgn_Type.__name__ = "OctetString"
_Sc5000ShelfLTUHwayAssgn_Object = MibScalar
sc5000ShelfLTUHwayAssgn = _Sc5000ShelfLTUHwayAssgn_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 5),
    _Sc5000ShelfLTUHwayAssgn_Type()
)
sc5000ShelfLTUHwayAssgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfLTUHwayAssgn.setStatus("mandatory")


class _Sc5000ShelfClockMode_Type(Integer32):
    """Custom type sc5000ShelfClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallback", 2),
          ("none", 3),
          ("primary", 1))
    )


_Sc5000ShelfClockMode_Type.__name__ = "Integer32"
_Sc5000ShelfClockMode_Object = MibScalar
sc5000ShelfClockMode = _Sc5000ShelfClockMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 6),
    _Sc5000ShelfClockMode_Type()
)
sc5000ShelfClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000ShelfClockMode.setStatus("mandatory")


class _Sc5000ShelfClocks_Type(OctetString):
    """Custom type sc5000ShelfClocks based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5000ShelfClocks_Type.__name__ = "OctetString"
_Sc5000ShelfClocks_Object = MibScalar
sc5000ShelfClocks = _Sc5000ShelfClocks_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 7),
    _Sc5000ShelfClocks_Type()
)
sc5000ShelfClocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfClocks.setStatus("mandatory")


class _Sc5000ShelfAutoClockRevert_Type(Integer32):
    """Custom type sc5000ShelfAutoClockRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Sc5000ShelfAutoClockRevert_Type.__name__ = "Integer32"
_Sc5000ShelfAutoClockRevert_Object = MibScalar
sc5000ShelfAutoClockRevert = _Sc5000ShelfAutoClockRevert_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 8),
    _Sc5000ShelfAutoClockRevert_Type()
)
sc5000ShelfAutoClockRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfAutoClockRevert.setStatus("mandatory")


class _Sc5000ShelfRevertToPrimaryClk_Type(Integer32):
    """Custom type sc5000ShelfRevertToPrimaryClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("normal", 1))
    )


_Sc5000ShelfRevertToPrimaryClk_Type.__name__ = "Integer32"
_Sc5000ShelfRevertToPrimaryClk_Object = MibScalar
sc5000ShelfRevertToPrimaryClk = _Sc5000ShelfRevertToPrimaryClk_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 3, 9),
    _Sc5000ShelfRevertToPrimaryClk_Type()
)
sc5000ShelfRevertToPrimaryClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ShelfRevertToPrimaryClk.setStatus("mandatory")
_GdcSc5000Highways_ObjectIdentity = ObjectIdentity
gdcSc5000Highways = _GdcSc5000Highways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 4)
)
_Sc5000HighwayTable_Object = MibTable
sc5000HighwayTable = _Sc5000HighwayTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sc5000HighwayTable.setStatus("mandatory")
_Sc5000HighwayEntry_Object = MibTableRow
sc5000HighwayEntry = _Sc5000HighwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 4, 1, 1)
)
sc5000HighwayEntry.setIndexNames(
    (0, "GDCSC5K-MIB", "sc5000HighwayNumber"),
)
if mibBuilder.loadTexts:
    sc5000HighwayEntry.setStatus("mandatory")


class _Sc5000HighwayNumber_Type(Integer32):
    """Custom type sc5000HighwayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Sc5000HighwayNumber_Type.__name__ = "Integer32"
_Sc5000HighwayNumber_Object = MibTableColumn
sc5000HighwayNumber = _Sc5000HighwayNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 4, 1, 1, 1),
    _Sc5000HighwayNumber_Type()
)
sc5000HighwayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000HighwayNumber.setStatus("mandatory")


class _Sc5000HighwayAllocation_Type(OctetString):
    """Custom type sc5000HighwayAllocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )


_Sc5000HighwayAllocation_Type.__name__ = "OctetString"
_Sc5000HighwayAllocation_Object = MibTableColumn
sc5000HighwayAllocation = _Sc5000HighwayAllocation_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 4, 1, 1, 2),
    _Sc5000HighwayAllocation_Type()
)
sc5000HighwayAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000HighwayAllocation.setStatus("mandatory")
_GdcSc5000LTUConfig_ObjectIdentity = ObjectIdentity
gdcSc5000LTUConfig = _GdcSc5000LTUConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5)
)
_Sc5000LTUConfigTable_Object = MibTable
sc5000LTUConfigTable = _Sc5000LTUConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sc5000LTUConfigTable.setStatus("mandatory")
_Sc5000LTUConfigEntry_Object = MibTableRow
sc5000LTUConfigEntry = _Sc5000LTUConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5, 1, 1)
)
sc5000LTUConfigEntry.setIndexNames(
    (0, "GDCSC5K-MIB", "sc5000SlotNumber"),
)
if mibBuilder.loadTexts:
    sc5000LTUConfigEntry.setStatus("mandatory")


class _Sc5000SlotNumber_Type(Integer32):
    """Custom type sc5000SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Sc5000SlotNumber_Type.__name__ = "Integer32"
_Sc5000SlotNumber_Object = MibTableColumn
sc5000SlotNumber = _Sc5000SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5, 1, 1, 1),
    _Sc5000SlotNumber_Type()
)
sc5000SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000SlotNumber.setStatus("mandatory")


class _Sc5000DS0Assign_Type(OctetString):
    """Custom type sc5000DS0Assign based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Sc5000DS0Assign_Type.__name__ = "OctetString"
_Sc5000DS0Assign_Object = MibTableColumn
sc5000DS0Assign = _Sc5000DS0Assign_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5, 1, 1, 2),
    _Sc5000DS0Assign_Type()
)
sc5000DS0Assign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000DS0Assign.setStatus("mandatory")


class _Sc5000ConfigCSUMode_Type(Integer32):
    """Custom type sc5000ConfigCSUMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concentratorMode", 2),
          ("csuMode", 1))
    )


_Sc5000ConfigCSUMode_Type.__name__ = "Integer32"
_Sc5000ConfigCSUMode_Object = MibTableColumn
sc5000ConfigCSUMode = _Sc5000ConfigCSUMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 5, 1, 1, 3),
    _Sc5000ConfigCSUMode_Type()
)
sc5000ConfigCSUMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5000ConfigCSUMode.setStatus("mandatory")
_GdcSc5000Circuit_ObjectIdentity = ObjectIdentity
gdcSc5000Circuit = _GdcSc5000Circuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 6)
)
_Sc5000CircuitTable_Object = MibTable
sc5000CircuitTable = _Sc5000CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sc5000CircuitTable.setStatus("mandatory")
_Sc5000CircuitEntry_Object = MibTableRow
sc5000CircuitEntry = _Sc5000CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 6, 1, 1)
)
sc5000CircuitEntry.setIndexNames(
    (0, "GDCSC5K-MIB", "sc5000CircuitIndex"),
)
if mibBuilder.loadTexts:
    sc5000CircuitEntry.setStatus("mandatory")
_Sc5000CircuitIndex_Type = SCinstance
_Sc5000CircuitIndex_Object = MibTableColumn
sc5000CircuitIndex = _Sc5000CircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 6, 1, 1, 1),
    _Sc5000CircuitIndex_Type()
)
sc5000CircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000CircuitIndex.setStatus("mandatory")


class _Sc5000CircuitType_Type(Integer32):
    """Custom type sc5000CircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("point-to-point", 1))
    )


_Sc5000CircuitType_Type.__name__ = "Integer32"
_Sc5000CircuitType_Object = MibTableColumn
sc5000CircuitType = _Sc5000CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 2, 6, 1, 1, 2),
    _Sc5000CircuitType_Type()
)
sc5000CircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5000CircuitType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCSC5K-MIB",
    **{"gdc": gdc,
       "sc": sc,
       "sc5000": sc5000,
       "gdcSc5000Version": gdcSc5000Version,
       "gdcSc5000MIBVersion": gdcSc5000MIBVersion,
       "gdcSc5000Timing": gdcSc5000Timing,
       "gdcSc5000TimingTable": gdcSc5000TimingTable,
       "gdcSc5000TimingEntry": gdcSc5000TimingEntry,
       "gdcSc5000TimingIndex": gdcSc5000TimingIndex,
       "gdcSc5000SrcShelfTiming": gdcSc5000SrcShelfTiming,
       "gdcSc5000Shelf": gdcSc5000Shelf,
       "sc5000ShelfNodeTypes": sc5000ShelfNodeTypes,
       "sc5000ShelfAdminStatus": sc5000ShelfAdminStatus,
       "sc5000ShelfOperStatus": sc5000ShelfOperStatus,
       "sc5000ShelfClockProvider": sc5000ShelfClockProvider,
       "sc5000ShelfLTUHwayAssgn": sc5000ShelfLTUHwayAssgn,
       "sc5000ShelfClockMode": sc5000ShelfClockMode,
       "sc5000ShelfClocks": sc5000ShelfClocks,
       "sc5000ShelfAutoClockRevert": sc5000ShelfAutoClockRevert,
       "sc5000ShelfRevertToPrimaryClk": sc5000ShelfRevertToPrimaryClk,
       "gdcSc5000Highways": gdcSc5000Highways,
       "sc5000HighwayTable": sc5000HighwayTable,
       "sc5000HighwayEntry": sc5000HighwayEntry,
       "sc5000HighwayNumber": sc5000HighwayNumber,
       "sc5000HighwayAllocation": sc5000HighwayAllocation,
       "gdcSc5000LTUConfig": gdcSc5000LTUConfig,
       "sc5000LTUConfigTable": sc5000LTUConfigTable,
       "sc5000LTUConfigEntry": sc5000LTUConfigEntry,
       "sc5000SlotNumber": sc5000SlotNumber,
       "sc5000DS0Assign": sc5000DS0Assign,
       "sc5000ConfigCSUMode": sc5000ConfigCSUMode,
       "gdcSc5000Circuit": gdcSc5000Circuit,
       "sc5000CircuitTable": sc5000CircuitTable,
       "sc5000CircuitEntry": sc5000CircuitEntry,
       "sc5000CircuitIndex": sc5000CircuitIndex,
       "sc5000CircuitType": sc5000CircuitType}
)
