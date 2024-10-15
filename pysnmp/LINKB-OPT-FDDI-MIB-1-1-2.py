# SNMP MIB module (LINKB-OPT-FDDI-MIB-1-1-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LINKB-OPT-FDDI-MIB-1-1-2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:17 2024
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

(FddiSMTStationIdType,
 FddiTimeNano,
 fddimibMACAvailablePaths,
 fddimibMACCopiedCts,
 fddimibMACCurrentPath,
 fddimibMACDaFlag,
 fddimibMACDownstreamNbr,
 fddimibMACErrorCts,
 fddimibMACFrameCts,
 fddimibMACFrameErrorFlag,
 fddimibMACFrameErrorRatio,
 fddimibMACLostCts,
 fddimibMACNotCopiedCts,
 fddimibMACNotCopiedFlag,
 fddimibMACNotCopiedRatio,
 fddimibMACOldDownstreamNbr,
 fddimibMACOldUpstreamNbr,
 fddimibMACRequestedPaths,
 fddimibMACSMTAddress,
 fddimibMACUnaDaFlag,
 fddimibMACUpstreamNbr,
 fddimibPORTAvailablePaths,
 fddimibPORTConnectState,
 fddimibPORTCurrentPath,
 fddimibPORTLemCts,
 fddimibPORTLemRejectCts,
 fddimibPORTLerAlarm,
 fddimibPORTLerCutoff,
 fddimibPORTLerEstimate,
 fddimibPORTLerFlag,
 fddimibPORTMyType,
 fddimibPORTNeighborType,
 fddimibPORTPCWithhold,
 fddimibPORTRequestedPaths,
 fddimibSMTCFState,
 fddimibSMTPeerWrapFlag,
 fddimibSMTStationId) = mibBuilder.importSymbols(
    "DRAFT-FDDI-MIB-VER-3-2",
    "FddiSMTStationIdType",
    "FddiTimeNano",
    "fddimibMACAvailablePaths",
    "fddimibMACCopiedCts",
    "fddimibMACCurrentPath",
    "fddimibMACDaFlag",
    "fddimibMACDownstreamNbr",
    "fddimibMACErrorCts",
    "fddimibMACFrameCts",
    "fddimibMACFrameErrorFlag",
    "fddimibMACFrameErrorRatio",
    "fddimibMACLostCts",
    "fddimibMACNotCopiedCts",
    "fddimibMACNotCopiedFlag",
    "fddimibMACNotCopiedRatio",
    "fddimibMACOldDownstreamNbr",
    "fddimibMACOldUpstreamNbr",
    "fddimibMACRequestedPaths",
    "fddimibMACSMTAddress",
    "fddimibMACUnaDaFlag",
    "fddimibMACUpstreamNbr",
    "fddimibPORTAvailablePaths",
    "fddimibPORTConnectState",
    "fddimibPORTCurrentPath",
    "fddimibPORTLemCts",
    "fddimibPORTLemRejectCts",
    "fddimibPORTLerAlarm",
    "fddimibPORTLerCutoff",
    "fddimibPORTLerEstimate",
    "fddimibPORTLerFlag",
    "fddimibPORTMyType",
    "fddimibPORTNeighborType",
    "fddimibPORTPCWithhold",
    "fddimibPORTRequestedPaths",
    "fddimibSMTCFState",
    "fddimibSMTPeerWrapFlag",
    "fddimibSMTStationId")

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
 NotificationType,
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
    "NotificationType",
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Lb3gh_ObjectIdentity = ObjectIdentity
lb3gh = _Lb3gh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_Lb3ghOptFddi_ObjectIdentity = ObjectIdentity
lb3ghOptFddi = _Lb3ghOptFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 2)
)
_LbOptSMT_ObjectIdentity = ObjectIdentity
lbOptSMT = _LbOptSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1)
)
_LbOptSMTTable_Object = MibTable
lbOptSMTTable = _LbOptSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lbOptSMTTable.setStatus("mandatory")
_LbOptSMTEntry_Object = MibTableRow
lbOptSMTEntry = _LbOptSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1)
)
lbOptSMTEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptSMTIndex"),
)
if mibBuilder.loadTexts:
    lbOptSMTEntry.setStatus("mandatory")


class _LbOptSMTIndex_Type(Integer32):
    """Custom type lbOptSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptSMTIndex_Type.__name__ = "Integer32"
_LbOptSMTIndex_Object = MibTableColumn
lbOptSMTIndex = _LbOptSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 1),
    _LbOptSMTIndex_Type()
)
lbOptSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTIndex.setStatus("mandatory")


class _LbOptSMTManufacturerOUI_Type(OctetString):
    """Custom type lbOptSMTManufacturerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LbOptSMTManufacturerOUI_Type.__name__ = "OctetString"
_LbOptSMTManufacturerOUI_Object = MibTableColumn
lbOptSMTManufacturerOUI = _LbOptSMTManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 2),
    _LbOptSMTManufacturerOUI_Type()
)
lbOptSMTManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTManufacturerOUI.setStatus("mandatory")


class _LbOptSMTManufacturerData_Type(OctetString):
    """Custom type lbOptSMTManufacturerData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_LbOptSMTManufacturerData_Type.__name__ = "OctetString"
_LbOptSMTManufacturerData_Object = MibTableColumn
lbOptSMTManufacturerData = _LbOptSMTManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 3),
    _LbOptSMTManufacturerData_Type()
)
lbOptSMTManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTManufacturerData.setStatus("mandatory")


class _LbOptSMTHoldState_Type(Integer32):
    """Custom type lbOptSMTHoldState based on Integer32"""
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
        *(("holding-prm", 3),
          ("holding-sec", 4),
          ("not-holding", 2),
          ("not-implemented", 1))
    )


_LbOptSMTHoldState_Type.__name__ = "Integer32"
_LbOptSMTHoldState_Object = MibTableColumn
lbOptSMTHoldState = _LbOptSMTHoldState_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 4),
    _LbOptSMTHoldState_Type()
)
lbOptSMTHoldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTHoldState.setStatus("mandatory")
_LbOptSMTSetCount_Type = Integer32
_LbOptSMTSetCount_Object = MibTableColumn
lbOptSMTSetCount = _LbOptSMTSetCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 5),
    _LbOptSMTSetCount_Type()
)
lbOptSMTSetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTSetCount.setStatus("mandatory")
_LbOptSMTLastSetStationId_Type = FddiSMTStationIdType
_LbOptSMTLastSetStationId_Object = MibTableColumn
lbOptSMTLastSetStationId = _LbOptSMTLastSetStationId_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 1, 1, 1, 6),
    _LbOptSMTLastSetStationId_Type()
)
lbOptSMTLastSetStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptSMTLastSetStationId.setStatus("mandatory")
_LbOptMAC_ObjectIdentity = ObjectIdentity
lbOptMAC = _LbOptMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2)
)
_LbOptMACBridgeFunctionTable_Object = MibTable
lbOptMACBridgeFunctionTable = _LbOptMACBridgeFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lbOptMACBridgeFunctionTable.setStatus("mandatory")
_LbOptMACBridgeFunctionEntry_Object = MibTableRow
lbOptMACBridgeFunctionEntry = _LbOptMACBridgeFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 1, 1)
)
lbOptMACBridgeFunctionEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptMACBridgeFunctionSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptMACBridgeFunctionMACIndex"),
)
if mibBuilder.loadTexts:
    lbOptMACBridgeFunctionEntry.setStatus("mandatory")


class _LbOptMACBridgeFunctionSMTIndex_Type(Integer32):
    """Custom type lbOptMACBridgeFunctionSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptMACBridgeFunctionSMTIndex_Type.__name__ = "Integer32"
_LbOptMACBridgeFunctionSMTIndex_Object = MibTableColumn
lbOptMACBridgeFunctionSMTIndex = _LbOptMACBridgeFunctionSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 1, 1, 1),
    _LbOptMACBridgeFunctionSMTIndex_Type()
)
lbOptMACBridgeFunctionSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACBridgeFunctionSMTIndex.setStatus("mandatory")


class _LbOptMACBridgeFunctionMACIndex_Type(Integer32):
    """Custom type lbOptMACBridgeFunctionMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptMACBridgeFunctionMACIndex_Type.__name__ = "Integer32"
_LbOptMACBridgeFunctionMACIndex_Object = MibTableColumn
lbOptMACBridgeFunctionMACIndex = _LbOptMACBridgeFunctionMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 1, 1, 2),
    _LbOptMACBridgeFunctionMACIndex_Type()
)
lbOptMACBridgeFunctionMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACBridgeFunctionMACIndex.setStatus("mandatory")


class _LbOptMACBridgeFunctions_Type(Integer32):
    """Custom type lbOptMACBridgeFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_LbOptMACBridgeFunctions_Type.__name__ = "Integer32"
_LbOptMACBridgeFunctions_Object = MibTableColumn
lbOptMACBridgeFunctions = _LbOptMACBridgeFunctions_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 1, 1, 3),
    _LbOptMACBridgeFunctions_Type()
)
lbOptMACBridgeFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACBridgeFunctions.setStatus("mandatory")
_LbOptMACTPriTable_Object = MibTable
lbOptMACTPriTable = _LbOptMACTPriTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lbOptMACTPriTable.setStatus("mandatory")
_LbOptMACTPriEntry_Object = MibTableRow
lbOptMACTPriEntry = _LbOptMACTPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1)
)
lbOptMACTPriEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptMACTPriSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptMACTPriMACIndex"),
)
if mibBuilder.loadTexts:
    lbOptMACTPriEntry.setStatus("mandatory")


class _LbOptMACTPriSMTIndex_Type(Integer32):
    """Custom type lbOptMACTPriSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptMACTPriSMTIndex_Type.__name__ = "Integer32"
_LbOptMACTPriSMTIndex_Object = MibTableColumn
lbOptMACTPriSMTIndex = _LbOptMACTPriSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 1),
    _LbOptMACTPriSMTIndex_Type()
)
lbOptMACTPriSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPriSMTIndex.setStatus("mandatory")


class _LbOptMACTPriMACIndex_Type(Integer32):
    """Custom type lbOptMACTPriMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptMACTPriMACIndex_Type.__name__ = "Integer32"
_LbOptMACTPriMACIndex_Object = MibTableColumn
lbOptMACTPriMACIndex = _LbOptMACTPriMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 2),
    _LbOptMACTPriMACIndex_Type()
)
lbOptMACTPriMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPriMACIndex.setStatus("mandatory")
_LbOptMACTPri0_Type = FddiTimeNano
_LbOptMACTPri0_Object = MibTableColumn
lbOptMACTPri0 = _LbOptMACTPri0_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 3),
    _LbOptMACTPri0_Type()
)
lbOptMACTPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri0.setStatus("mandatory")
_LbOptMACTPri1_Type = FddiTimeNano
_LbOptMACTPri1_Object = MibTableColumn
lbOptMACTPri1 = _LbOptMACTPri1_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 4),
    _LbOptMACTPri1_Type()
)
lbOptMACTPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri1.setStatus("mandatory")
_LbOptMACTPri2_Type = FddiTimeNano
_LbOptMACTPri2_Object = MibTableColumn
lbOptMACTPri2 = _LbOptMACTPri2_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 5),
    _LbOptMACTPri2_Type()
)
lbOptMACTPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri2.setStatus("mandatory")
_LbOptMACTPri3_Type = FddiTimeNano
_LbOptMACTPri3_Object = MibTableColumn
lbOptMACTPri3 = _LbOptMACTPri3_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 6),
    _LbOptMACTPri3_Type()
)
lbOptMACTPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri3.setStatus("mandatory")
_LbOptMACTPri4_Type = FddiTimeNano
_LbOptMACTPri4_Object = MibTableColumn
lbOptMACTPri4 = _LbOptMACTPri4_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 7),
    _LbOptMACTPri4_Type()
)
lbOptMACTPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri4.setStatus("mandatory")
_LbOptMACTPri5_Type = FddiTimeNano
_LbOptMACTPri5_Object = MibTableColumn
lbOptMACTPri5 = _LbOptMACTPri5_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 8),
    _LbOptMACTPri5_Type()
)
lbOptMACTPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri5.setStatus("mandatory")
_LbOptMACTPri6_Type = FddiTimeNano
_LbOptMACTPri6_Object = MibTableColumn
lbOptMACTPri6 = _LbOptMACTPri6_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 2, 2, 1, 9),
    _LbOptMACTPri6_Type()
)
lbOptMACTPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptMACTPri6.setStatus("mandatory")
_LbOptPATH_ObjectIdentity = ObjectIdentity
lbOptPATH = _LbOptPATH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3)
)
_LbOptPATHRingTable_Object = MibTable
lbOptPATHRingTable = _LbOptPATHRingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lbOptPATHRingTable.setStatus("mandatory")
_LbOptPATHRingEntry_Object = MibTableRow
lbOptPATHRingEntry = _LbOptPATHRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1)
)
lbOptPATHRingEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPATHRingSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPATHRingPATHIndex"),
)
if mibBuilder.loadTexts:
    lbOptPATHRingEntry.setStatus("mandatory")


class _LbOptPATHRingSMTIndex_Type(Integer32):
    """Custom type lbOptPATHRingSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPATHRingSMTIndex_Type.__name__ = "Integer32"
_LbOptPATHRingSMTIndex_Object = MibTableColumn
lbOptPATHRingSMTIndex = _LbOptPATHRingSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1, 1),
    _LbOptPATHRingSMTIndex_Type()
)
lbOptPATHRingSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPATHRingSMTIndex.setStatus("mandatory")


class _LbOptPATHRingPATHIndex_Type(Integer32):
    """Custom type lbOptPATHRingPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LbOptPATHRingPATHIndex_Type.__name__ = "Integer32"
_LbOptPATHRingPATHIndex_Object = MibTableColumn
lbOptPATHRingPATHIndex = _LbOptPATHRingPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1, 2),
    _LbOptPATHRingPATHIndex_Type()
)
lbOptPATHRingPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPATHRingPATHIndex.setStatus("mandatory")
_LbOptPATHRingLatency_Type = FddiTimeNano
_LbOptPATHRingLatency_Object = MibTableColumn
lbOptPATHRingLatency = _LbOptPATHRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1, 3),
    _LbOptPATHRingLatency_Type()
)
lbOptPATHRingLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPATHRingLatency.setStatus("mandatory")


class _LbOptPATHTraceStatus_Type(Integer32):
    """Custom type lbOptPATHTraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LbOptPATHTraceStatus_Type.__name__ = "Integer32"
_LbOptPATHTraceStatus_Object = MibTableColumn
lbOptPATHTraceStatus = _LbOptPATHTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1, 4),
    _LbOptPATHTraceStatus_Type()
)
lbOptPATHTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPATHTraceStatus.setStatus("mandatory")
_LbOptPATHT_Rmode_Type = FddiTimeNano
_LbOptPATHT_Rmode_Object = MibScalar
lbOptPATHT_Rmode = _LbOptPATHT_Rmode_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 1, 1, 5),
    _LbOptPATHT_Rmode_Type()
)
lbOptPATHT_Rmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPATHT_Rmode.setStatus("mandatory")
_LbOptPATHSbaTable_Object = MibTable
lbOptPATHSbaTable = _LbOptPATHSbaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lbOptPATHSbaTable.setStatus("mandatory")
_LbOptPATHSbaEntry_Object = MibTableRow
lbOptPATHSbaEntry = _LbOptPATHSbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1)
)
lbOptPATHSbaEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPATHSbaSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPATHSbaPATHIndex"),
)
if mibBuilder.loadTexts:
    lbOptPATHSbaEntry.setStatus("mandatory")


class _LbOptPATHSbaSMTIndex_Type(Integer32):
    """Custom type lbOptPATHSbaSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPATHSbaSMTIndex_Type.__name__ = "Integer32"
_LbOptPATHSbaSMTIndex_Object = MibTableColumn
lbOptPATHSbaSMTIndex = _LbOptPATHSbaSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1, 1),
    _LbOptPATHSbaSMTIndex_Type()
)
lbOptPATHSbaSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPATHSbaSMTIndex.setStatus("mandatory")


class _LbOptPATHSbaPATHIndex_Type(Integer32):
    """Custom type lbOptPATHSbaPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LbOptPATHSbaPATHIndex_Type.__name__ = "Integer32"
_LbOptPATHSbaPATHIndex_Object = MibTableColumn
lbOptPATHSbaPATHIndex = _LbOptPATHSbaPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1, 2),
    _LbOptPATHSbaPATHIndex_Type()
)
lbOptPATHSbaPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPATHSbaPATHIndex.setStatus("mandatory")


class _LbOptPATHSbaPayload_Type(Integer32):
    """Custom type lbOptPATHSbaPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1562),
    )


_LbOptPATHSbaPayload_Type.__name__ = "Integer32"
_LbOptPATHSbaPayload_Object = MibTableColumn
lbOptPATHSbaPayload = _LbOptPATHSbaPayload_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1, 3),
    _LbOptPATHSbaPayload_Type()
)
lbOptPATHSbaPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPATHSbaPayload.setStatus("mandatory")
_LbOptPATHSbaOverhead_Type = Integer32
_LbOptPATHSbaOverhead_Object = MibTableColumn
lbOptPATHSbaOverhead = _LbOptPATHSbaOverhead_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1, 4),
    _LbOptPATHSbaOverhead_Type()
)
lbOptPATHSbaOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPATHSbaOverhead.setStatus("mandatory")


class _LbOptPATHSbaAvailable_Type(Integer32):
    """Custom type lbOptPATHSbaAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12500000),
    )


_LbOptPATHSbaAvailable_Type.__name__ = "Integer32"
_LbOptPATHSbaAvailable_Object = MibTableColumn
lbOptPATHSbaAvailable = _LbOptPATHSbaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 3, 2, 1, 5),
    _LbOptPATHSbaAvailable_Type()
)
lbOptPATHSbaAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPATHSbaAvailable.setStatus("mandatory")
_LbOptPORT_ObjectIdentity = ObjectIdentity
lbOptPORT = _LbOptPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4)
)
_LbOptPORTTable_Object = MibTable
lbOptPORTTable = _LbOptPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lbOptPORTTable.setStatus("mandatory")
_LbOptPORTEntry_Object = MibTableRow
lbOptPORTEntry = _LbOptPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1, 1)
)
lbOptPORTEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPORTSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPORTIndex"),
)
if mibBuilder.loadTexts:
    lbOptPORTEntry.setStatus("mandatory")


class _LbOptPORTSMTIndex_Type(Integer32):
    """Custom type lbOptPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPORTSMTIndex_Type.__name__ = "Integer32"
_LbOptPORTSMTIndex_Object = MibTableColumn
lbOptPORTSMTIndex = _LbOptPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1, 1, 1),
    _LbOptPORTSMTIndex_Type()
)
lbOptPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTSMTIndex.setStatus("mandatory")


class _LbOptPORTIndex_Type(Integer32):
    """Custom type lbOptPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPORTIndex_Type.__name__ = "Integer32"
_LbOptPORTIndex_Object = MibTableColumn
lbOptPORTIndex = _LbOptPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1, 1, 2),
    _LbOptPORTIndex_Type()
)
lbOptPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTIndex.setStatus("mandatory")
_LbOptPORTMACLoopTime_Type = FddiTimeNano
_LbOptPORTMACLoopTime_Object = MibTableColumn
lbOptPORTMACLoopTime = _LbOptPORTMACLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1, 1, 3),
    _LbOptPORTMACLoopTime_Type()
)
lbOptPORTMACLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPORTMACLoopTime.setStatus("mandatory")
_LbOptPORTEBErrorCt_Type = Counter32
_LbOptPORTEBErrorCt_Object = MibTableColumn
lbOptPORTEBErrorCt = _LbOptPORTEBErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 1, 1, 4),
    _LbOptPORTEBErrorCt_Type()
)
lbOptPORTEBErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTEBErrorCt.setStatus("mandatory")
_LbOptPORTLSTable_Object = MibTable
lbOptPORTLSTable = _LbOptPORTLSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lbOptPORTLSTable.setStatus("mandatory")
_LbOptPORTLSEntry_Object = MibTableRow
lbOptPORTLSEntry = _LbOptPORTLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2, 1)
)
lbOptPORTLSEntry.setIndexNames(
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPORTLSSMTIndex"),
    (0, "LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPORTLSPORTIndex"),
)
if mibBuilder.loadTexts:
    lbOptPORTLSEntry.setStatus("mandatory")


class _LbOptPORTLSSMTIndex_Type(Integer32):
    """Custom type lbOptPORTLSSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPORTLSSMTIndex_Type.__name__ = "Integer32"
_LbOptPORTLSSMTIndex_Object = MibTableColumn
lbOptPORTLSSMTIndex = _LbOptPORTLSSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2, 1, 1),
    _LbOptPORTLSSMTIndex_Type()
)
lbOptPORTLSSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTLSSMTIndex.setStatus("mandatory")


class _LbOptPORTLSPORTIndex_Type(Integer32):
    """Custom type lbOptPORTLSPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LbOptPORTLSPORTIndex_Type.__name__ = "Integer32"
_LbOptPORTLSPORTIndex_Object = MibTableColumn
lbOptPORTLSPORTIndex = _LbOptPORTLSPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2, 1, 2),
    _LbOptPORTLSPORTIndex_Type()
)
lbOptPORTLSPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTLSPORTIndex.setStatus("mandatory")


class _LbOptPORTMaintLS_Type(Integer32):
    """Custom type lbOptPORTMaintLS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("halt", 4),
          ("idle", 2),
          ("master", 3),
          ("quiet", 1),
          ("receive-active", 5),
          ("receive-noise", 7),
          ("receive-unknown", 6))
    )


_LbOptPORTMaintLS_Type.__name__ = "Integer32"
_LbOptPORTMaintLS_Object = MibTableColumn
lbOptPORTMaintLS = _LbOptPORTMaintLS_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2, 1, 3),
    _LbOptPORTMaintLS_Type()
)
lbOptPORTMaintLS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbOptPORTMaintLS.setStatus("mandatory")


class _LbOptPORTPCLS_Type(Integer32):
    """Custom type lbOptPORTPCLS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("halt", 4),
          ("idle", 2),
          ("master", 3),
          ("quiet", 1),
          ("receive-active", 5),
          ("receive-noise", 7),
          ("receive-unknown", 6))
    )


_LbOptPORTPCLS_Type.__name__ = "Integer32"
_LbOptPORTPCLS_Object = MibTableColumn
lbOptPORTPCLS = _LbOptPORTPCLS_Object(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 4, 2, 1, 4),
    _LbOptPORTPCLS_Type()
)
lbOptPORTPCLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbOptPORTPCLS.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lbOptSMTHoldCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 1)
)
lbOptSMTHoldCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("LINKB-OPT-FDDI-MIB-1-1-2", "lbOptSMTHoldState"))
)
if mibBuilder.loadTexts:
    lbOptSMTHoldCondition.setStatus(
        ""
    )

lbOptSMTPeerWrapCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 2)
)
lbOptSMTPeerWrapCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTCFState"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTPeerWrapFlag"))
)
if mibBuilder.loadTexts:
    lbOptSMTPeerWrapCondition.setStatus(
        ""
    )

lbOptMACDuplicateAddressCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 3)
)
lbOptMACDuplicateAddressCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTAddress"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACDaFlag"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUnaDaFlag"))
)
if mibBuilder.loadTexts:
    lbOptMACDuplicateAddressCondition.setStatus(
        ""
    )

lbOptMACFrameErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 4)
)
lbOptMACFrameErrorCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameErrorFlag"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACErrorCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACLostCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameErrorRatio"))
)
if mibBuilder.loadTexts:
    lbOptMACFrameErrorCondition.setStatus(
        ""
    )

lbOptMACNotCopiedCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 5)
)
lbOptMACNotCopiedCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCopiedCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedRatio"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedFlag"))
)
if mibBuilder.loadTexts:
    lbOptMACNotCopiedCondition.setStatus(
        ""
    )

lbOptMACNeighborChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 6)
)
lbOptMACNeighborChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACOldUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACDownstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACOldDownstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTAddress"))
)
if mibBuilder.loadTexts:
    lbOptMACNeighborChangeEvent.setStatus(
        ""
    )

lbOptMACPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 7)
)
lbOptMACPathChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACAvailablePaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACRequestedPaths"))
)
if mibBuilder.loadTexts:
    lbOptMACPathChangeEvent.setStatus(
        ""
    )

lbOptPORTLerCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 8)
)
lbOptPORTLerCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerCutoff"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerAlarm"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerEstimate"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLemRejectCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLemCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerFlag"))
)
if mibBuilder.loadTexts:
    lbOptPORTLerCondition.setStatus(
        ""
    )

lbOptPORTUndesiredConnAttemptEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 9)
)
lbOptPORTUndesiredConnAttemptEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTMyType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTConnectState"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTNeighborType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTPCWithhold"))
)
if mibBuilder.loadTexts:
    lbOptPORTUndesiredConnAttemptEvent.setStatus(
        ""
    )

lbOptPORTEBErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 10)
)
lbOptPORTEBErrorCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("LINKB-OPT-FDDI-MIB-1-1-2", "lbOptPORTEBErrorCt"))
)
if mibBuilder.loadTexts:
    lbOptPORTEBErrorCondition.setStatus(
        ""
    )

lbOptPORTPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 7, 2, 0, 11)
)
lbOptPORTPathChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTAvailablePaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTRequestedPaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTMyType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTNeighborType"))
)
if mibBuilder.loadTexts:
    lbOptPORTPathChangeEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKB-OPT-FDDI-MIB-1-1-2",
    **{"a3Com": a3Com,
       "lb3gh": lb3gh,
       "lb3ghOptFddi": lb3ghOptFddi,
       "lbOptSMTHoldCondition": lbOptSMTHoldCondition,
       "lbOptSMTPeerWrapCondition": lbOptSMTPeerWrapCondition,
       "lbOptMACDuplicateAddressCondition": lbOptMACDuplicateAddressCondition,
       "lbOptMACFrameErrorCondition": lbOptMACFrameErrorCondition,
       "lbOptMACNotCopiedCondition": lbOptMACNotCopiedCondition,
       "lbOptMACNeighborChangeEvent": lbOptMACNeighborChangeEvent,
       "lbOptMACPathChangeEvent": lbOptMACPathChangeEvent,
       "lbOptPORTLerCondition": lbOptPORTLerCondition,
       "lbOptPORTUndesiredConnAttemptEvent": lbOptPORTUndesiredConnAttemptEvent,
       "lbOptPORTEBErrorCondition": lbOptPORTEBErrorCondition,
       "lbOptPORTPathChangeEvent": lbOptPORTPathChangeEvent,
       "lbOptSMT": lbOptSMT,
       "lbOptSMTTable": lbOptSMTTable,
       "lbOptSMTEntry": lbOptSMTEntry,
       "lbOptSMTIndex": lbOptSMTIndex,
       "lbOptSMTManufacturerOUI": lbOptSMTManufacturerOUI,
       "lbOptSMTManufacturerData": lbOptSMTManufacturerData,
       "lbOptSMTHoldState": lbOptSMTHoldState,
       "lbOptSMTSetCount": lbOptSMTSetCount,
       "lbOptSMTLastSetStationId": lbOptSMTLastSetStationId,
       "lbOptMAC": lbOptMAC,
       "lbOptMACBridgeFunctionTable": lbOptMACBridgeFunctionTable,
       "lbOptMACBridgeFunctionEntry": lbOptMACBridgeFunctionEntry,
       "lbOptMACBridgeFunctionSMTIndex": lbOptMACBridgeFunctionSMTIndex,
       "lbOptMACBridgeFunctionMACIndex": lbOptMACBridgeFunctionMACIndex,
       "lbOptMACBridgeFunctions": lbOptMACBridgeFunctions,
       "lbOptMACTPriTable": lbOptMACTPriTable,
       "lbOptMACTPriEntry": lbOptMACTPriEntry,
       "lbOptMACTPriSMTIndex": lbOptMACTPriSMTIndex,
       "lbOptMACTPriMACIndex": lbOptMACTPriMACIndex,
       "lbOptMACTPri0": lbOptMACTPri0,
       "lbOptMACTPri1": lbOptMACTPri1,
       "lbOptMACTPri2": lbOptMACTPri2,
       "lbOptMACTPri3": lbOptMACTPri3,
       "lbOptMACTPri4": lbOptMACTPri4,
       "lbOptMACTPri5": lbOptMACTPri5,
       "lbOptMACTPri6": lbOptMACTPri6,
       "lbOptPATH": lbOptPATH,
       "lbOptPATHRingTable": lbOptPATHRingTable,
       "lbOptPATHRingEntry": lbOptPATHRingEntry,
       "lbOptPATHRingSMTIndex": lbOptPATHRingSMTIndex,
       "lbOptPATHRingPATHIndex": lbOptPATHRingPATHIndex,
       "lbOptPATHRingLatency": lbOptPATHRingLatency,
       "lbOptPATHTraceStatus": lbOptPATHTraceStatus,
       "lbOptPATHT-Rmode": lbOptPATHT_Rmode,
       "lbOptPATHSbaTable": lbOptPATHSbaTable,
       "lbOptPATHSbaEntry": lbOptPATHSbaEntry,
       "lbOptPATHSbaSMTIndex": lbOptPATHSbaSMTIndex,
       "lbOptPATHSbaPATHIndex": lbOptPATHSbaPATHIndex,
       "lbOptPATHSbaPayload": lbOptPATHSbaPayload,
       "lbOptPATHSbaOverhead": lbOptPATHSbaOverhead,
       "lbOptPATHSbaAvailable": lbOptPATHSbaAvailable,
       "lbOptPORT": lbOptPORT,
       "lbOptPORTTable": lbOptPORTTable,
       "lbOptPORTEntry": lbOptPORTEntry,
       "lbOptPORTSMTIndex": lbOptPORTSMTIndex,
       "lbOptPORTIndex": lbOptPORTIndex,
       "lbOptPORTMACLoopTime": lbOptPORTMACLoopTime,
       "lbOptPORTEBErrorCt": lbOptPORTEBErrorCt,
       "lbOptPORTLSTable": lbOptPORTLSTable,
       "lbOptPORTLSEntry": lbOptPORTLSEntry,
       "lbOptPORTLSSMTIndex": lbOptPORTLSSMTIndex,
       "lbOptPORTLSPORTIndex": lbOptPORTLSPORTIndex,
       "lbOptPORTMaintLS": lbOptPORTMaintLS,
       "lbOptPORTPCLS": lbOptPORTPCLS}
)
