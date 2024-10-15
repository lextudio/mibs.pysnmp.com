# SNMP MIB module (LANPLEX-OPT-FDDI-MIB-1-1-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANPLEX-OPT-FDDI-MIB-1-1-2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:17 2024
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

_Synernetics_ObjectIdentity = ObjectIdentity
synernetics = _Synernetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114)
)
_Lanplex_ObjectIdentity = ObjectIdentity
lanplex = _Lanplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1)
)
_LanplexOptFddi_ObjectIdentity = ObjectIdentity
lanplexOptFddi = _LanplexOptFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10)
)
_LpOptSMT_ObjectIdentity = ObjectIdentity
lpOptSMT = _LpOptSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1)
)
_LpOptSMTTable_Object = MibTable
lpOptSMTTable = _LpOptSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    lpOptSMTTable.setStatus("mandatory")
_LpOptSMTEntry_Object = MibTableRow
lpOptSMTEntry = _LpOptSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1)
)
lpOptSMTEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptSMTIndex"),
)
if mibBuilder.loadTexts:
    lpOptSMTEntry.setStatus("mandatory")


class _LpOptSMTIndex_Type(Integer32):
    """Custom type lpOptSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptSMTIndex_Type.__name__ = "Integer32"
_LpOptSMTIndex_Object = MibTableColumn
lpOptSMTIndex = _LpOptSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 1),
    _LpOptSMTIndex_Type()
)
lpOptSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTIndex.setStatus("mandatory")


class _LpOptSMTManufacturerOUI_Type(OctetString):
    """Custom type lpOptSMTManufacturerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LpOptSMTManufacturerOUI_Type.__name__ = "OctetString"
_LpOptSMTManufacturerOUI_Object = MibTableColumn
lpOptSMTManufacturerOUI = _LpOptSMTManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 2),
    _LpOptSMTManufacturerOUI_Type()
)
lpOptSMTManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTManufacturerOUI.setStatus("mandatory")


class _LpOptSMTManufacturerData_Type(OctetString):
    """Custom type lpOptSMTManufacturerData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_LpOptSMTManufacturerData_Type.__name__ = "OctetString"
_LpOptSMTManufacturerData_Object = MibTableColumn
lpOptSMTManufacturerData = _LpOptSMTManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 3),
    _LpOptSMTManufacturerData_Type()
)
lpOptSMTManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTManufacturerData.setStatus("mandatory")


class _LpOptSMTHoldState_Type(Integer32):
    """Custom type lpOptSMTHoldState based on Integer32"""
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


_LpOptSMTHoldState_Type.__name__ = "Integer32"
_LpOptSMTHoldState_Object = MibTableColumn
lpOptSMTHoldState = _LpOptSMTHoldState_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 4),
    _LpOptSMTHoldState_Type()
)
lpOptSMTHoldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTHoldState.setStatus("mandatory")
_LpOptSMTSetCount_Type = Integer32
_LpOptSMTSetCount_Object = MibTableColumn
lpOptSMTSetCount = _LpOptSMTSetCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 5),
    _LpOptSMTSetCount_Type()
)
lpOptSMTSetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTSetCount.setStatus("mandatory")
_LpOptSMTLastSetStationId_Type = FddiSMTStationIdType
_LpOptSMTLastSetStationId_Object = MibTableColumn
lpOptSMTLastSetStationId = _LpOptSMTLastSetStationId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 1, 1, 1, 6),
    _LpOptSMTLastSetStationId_Type()
)
lpOptSMTLastSetStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptSMTLastSetStationId.setStatus("mandatory")
_LpOptMAC_ObjectIdentity = ObjectIdentity
lpOptMAC = _LpOptMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2)
)
_LpOptMACBridgeFunctionTable_Object = MibTable
lpOptMACBridgeFunctionTable = _LpOptMACBridgeFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    lpOptMACBridgeFunctionTable.setStatus("mandatory")
_LpOptMACBridgeFunctionEntry_Object = MibTableRow
lpOptMACBridgeFunctionEntry = _LpOptMACBridgeFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 1, 1)
)
lpOptMACBridgeFunctionEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptMACBridgeFunctionSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptMACBridgeFunctionMACIndex"),
)
if mibBuilder.loadTexts:
    lpOptMACBridgeFunctionEntry.setStatus("mandatory")


class _LpOptMACBridgeFunctionSMTIndex_Type(Integer32):
    """Custom type lpOptMACBridgeFunctionSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptMACBridgeFunctionSMTIndex_Type.__name__ = "Integer32"
_LpOptMACBridgeFunctionSMTIndex_Object = MibTableColumn
lpOptMACBridgeFunctionSMTIndex = _LpOptMACBridgeFunctionSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 1, 1, 1),
    _LpOptMACBridgeFunctionSMTIndex_Type()
)
lpOptMACBridgeFunctionSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACBridgeFunctionSMTIndex.setStatus("mandatory")


class _LpOptMACBridgeFunctionMACIndex_Type(Integer32):
    """Custom type lpOptMACBridgeFunctionMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptMACBridgeFunctionMACIndex_Type.__name__ = "Integer32"
_LpOptMACBridgeFunctionMACIndex_Object = MibTableColumn
lpOptMACBridgeFunctionMACIndex = _LpOptMACBridgeFunctionMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 1, 1, 2),
    _LpOptMACBridgeFunctionMACIndex_Type()
)
lpOptMACBridgeFunctionMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACBridgeFunctionMACIndex.setStatus("mandatory")


class _LpOptMACBridgeFunctions_Type(Integer32):
    """Custom type lpOptMACBridgeFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_LpOptMACBridgeFunctions_Type.__name__ = "Integer32"
_LpOptMACBridgeFunctions_Object = MibTableColumn
lpOptMACBridgeFunctions = _LpOptMACBridgeFunctions_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 1, 1, 3),
    _LpOptMACBridgeFunctions_Type()
)
lpOptMACBridgeFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACBridgeFunctions.setStatus("mandatory")
_LpOptMACTPriTable_Object = MibTable
lpOptMACTPriTable = _LpOptMACTPriTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    lpOptMACTPriTable.setStatus("mandatory")
_LpOptMACTPriEntry_Object = MibTableRow
lpOptMACTPriEntry = _LpOptMACTPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1)
)
lpOptMACTPriEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptMACTPriSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptMACTPriMACIndex"),
)
if mibBuilder.loadTexts:
    lpOptMACTPriEntry.setStatus("mandatory")


class _LpOptMACTPriSMTIndex_Type(Integer32):
    """Custom type lpOptMACTPriSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptMACTPriSMTIndex_Type.__name__ = "Integer32"
_LpOptMACTPriSMTIndex_Object = MibTableColumn
lpOptMACTPriSMTIndex = _LpOptMACTPriSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 1),
    _LpOptMACTPriSMTIndex_Type()
)
lpOptMACTPriSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPriSMTIndex.setStatus("mandatory")


class _LpOptMACTPriMACIndex_Type(Integer32):
    """Custom type lpOptMACTPriMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptMACTPriMACIndex_Type.__name__ = "Integer32"
_LpOptMACTPriMACIndex_Object = MibTableColumn
lpOptMACTPriMACIndex = _LpOptMACTPriMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 2),
    _LpOptMACTPriMACIndex_Type()
)
lpOptMACTPriMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPriMACIndex.setStatus("mandatory")
_LpOptMACTPri0_Type = FddiTimeNano
_LpOptMACTPri0_Object = MibTableColumn
lpOptMACTPri0 = _LpOptMACTPri0_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 3),
    _LpOptMACTPri0_Type()
)
lpOptMACTPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri0.setStatus("mandatory")
_LpOptMACTPri1_Type = FddiTimeNano
_LpOptMACTPri1_Object = MibTableColumn
lpOptMACTPri1 = _LpOptMACTPri1_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 4),
    _LpOptMACTPri1_Type()
)
lpOptMACTPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri1.setStatus("mandatory")
_LpOptMACTPri2_Type = FddiTimeNano
_LpOptMACTPri2_Object = MibTableColumn
lpOptMACTPri2 = _LpOptMACTPri2_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 5),
    _LpOptMACTPri2_Type()
)
lpOptMACTPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri2.setStatus("mandatory")
_LpOptMACTPri3_Type = FddiTimeNano
_LpOptMACTPri3_Object = MibTableColumn
lpOptMACTPri3 = _LpOptMACTPri3_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 6),
    _LpOptMACTPri3_Type()
)
lpOptMACTPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri3.setStatus("mandatory")
_LpOptMACTPri4_Type = FddiTimeNano
_LpOptMACTPri4_Object = MibTableColumn
lpOptMACTPri4 = _LpOptMACTPri4_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 7),
    _LpOptMACTPri4_Type()
)
lpOptMACTPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri4.setStatus("mandatory")
_LpOptMACTPri5_Type = FddiTimeNano
_LpOptMACTPri5_Object = MibTableColumn
lpOptMACTPri5 = _LpOptMACTPri5_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 8),
    _LpOptMACTPri5_Type()
)
lpOptMACTPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri5.setStatus("mandatory")
_LpOptMACTPri6_Type = FddiTimeNano
_LpOptMACTPri6_Object = MibTableColumn
lpOptMACTPri6 = _LpOptMACTPri6_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 2, 2, 1, 9),
    _LpOptMACTPri6_Type()
)
lpOptMACTPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptMACTPri6.setStatus("mandatory")
_LpOptPATH_ObjectIdentity = ObjectIdentity
lpOptPATH = _LpOptPATH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3)
)
_LpOptPATHRingTable_Object = MibTable
lpOptPATHRingTable = _LpOptPATHRingTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    lpOptPATHRingTable.setStatus("mandatory")
_LpOptPATHRingEntry_Object = MibTableRow
lpOptPATHRingEntry = _LpOptPATHRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1)
)
lpOptPATHRingEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPATHRingSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPATHRingPATHIndex"),
)
if mibBuilder.loadTexts:
    lpOptPATHRingEntry.setStatus("mandatory")


class _LpOptPATHRingSMTIndex_Type(Integer32):
    """Custom type lpOptPATHRingSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPATHRingSMTIndex_Type.__name__ = "Integer32"
_LpOptPATHRingSMTIndex_Object = MibTableColumn
lpOptPATHRingSMTIndex = _LpOptPATHRingSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1, 1),
    _LpOptPATHRingSMTIndex_Type()
)
lpOptPATHRingSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPATHRingSMTIndex.setStatus("mandatory")


class _LpOptPATHRingPATHIndex_Type(Integer32):
    """Custom type lpOptPATHRingPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LpOptPATHRingPATHIndex_Type.__name__ = "Integer32"
_LpOptPATHRingPATHIndex_Object = MibTableColumn
lpOptPATHRingPATHIndex = _LpOptPATHRingPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1, 2),
    _LpOptPATHRingPATHIndex_Type()
)
lpOptPATHRingPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPATHRingPATHIndex.setStatus("mandatory")
_LpOptPATHRingLatency_Type = FddiTimeNano
_LpOptPATHRingLatency_Object = MibTableColumn
lpOptPATHRingLatency = _LpOptPATHRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1, 3),
    _LpOptPATHRingLatency_Type()
)
lpOptPATHRingLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPATHRingLatency.setStatus("mandatory")


class _LpOptPATHTraceStatus_Type(Integer32):
    """Custom type lpOptPATHTraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LpOptPATHTraceStatus_Type.__name__ = "Integer32"
_LpOptPATHTraceStatus_Object = MibTableColumn
lpOptPATHTraceStatus = _LpOptPATHTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1, 4),
    _LpOptPATHTraceStatus_Type()
)
lpOptPATHTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPATHTraceStatus.setStatus("mandatory")
_LpOptPATHT_Rmode_Type = FddiTimeNano
_LpOptPATHT_Rmode_Object = MibScalar
lpOptPATHT_Rmode = _LpOptPATHT_Rmode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 1, 1, 5),
    _LpOptPATHT_Rmode_Type()
)
lpOptPATHT_Rmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPATHT_Rmode.setStatus("mandatory")
_LpOptPATHSbaTable_Object = MibTable
lpOptPATHSbaTable = _LpOptPATHSbaTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2)
)
if mibBuilder.loadTexts:
    lpOptPATHSbaTable.setStatus("mandatory")
_LpOptPATHSbaEntry_Object = MibTableRow
lpOptPATHSbaEntry = _LpOptPATHSbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1)
)
lpOptPATHSbaEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPATHSbaSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPATHSbaPATHIndex"),
)
if mibBuilder.loadTexts:
    lpOptPATHSbaEntry.setStatus("mandatory")


class _LpOptPATHSbaSMTIndex_Type(Integer32):
    """Custom type lpOptPATHSbaSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPATHSbaSMTIndex_Type.__name__ = "Integer32"
_LpOptPATHSbaSMTIndex_Object = MibTableColumn
lpOptPATHSbaSMTIndex = _LpOptPATHSbaSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1, 1),
    _LpOptPATHSbaSMTIndex_Type()
)
lpOptPATHSbaSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPATHSbaSMTIndex.setStatus("mandatory")


class _LpOptPATHSbaPATHIndex_Type(Integer32):
    """Custom type lpOptPATHSbaPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LpOptPATHSbaPATHIndex_Type.__name__ = "Integer32"
_LpOptPATHSbaPATHIndex_Object = MibTableColumn
lpOptPATHSbaPATHIndex = _LpOptPATHSbaPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1, 2),
    _LpOptPATHSbaPATHIndex_Type()
)
lpOptPATHSbaPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPATHSbaPATHIndex.setStatus("mandatory")


class _LpOptPATHSbaPayload_Type(Integer32):
    """Custom type lpOptPATHSbaPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1562),
    )


_LpOptPATHSbaPayload_Type.__name__ = "Integer32"
_LpOptPATHSbaPayload_Object = MibTableColumn
lpOptPATHSbaPayload = _LpOptPATHSbaPayload_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1, 3),
    _LpOptPATHSbaPayload_Type()
)
lpOptPATHSbaPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPATHSbaPayload.setStatus("mandatory")
_LpOptPATHSbaOverhead_Type = Integer32
_LpOptPATHSbaOverhead_Object = MibTableColumn
lpOptPATHSbaOverhead = _LpOptPATHSbaOverhead_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1, 4),
    _LpOptPATHSbaOverhead_Type()
)
lpOptPATHSbaOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPATHSbaOverhead.setStatus("mandatory")


class _LpOptPATHSbaAvailable_Type(Integer32):
    """Custom type lpOptPATHSbaAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12500000),
    )


_LpOptPATHSbaAvailable_Type.__name__ = "Integer32"
_LpOptPATHSbaAvailable_Object = MibTableColumn
lpOptPATHSbaAvailable = _LpOptPATHSbaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 3, 2, 1, 5),
    _LpOptPATHSbaAvailable_Type()
)
lpOptPATHSbaAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPATHSbaAvailable.setStatus("mandatory")
_LpOptPORT_ObjectIdentity = ObjectIdentity
lpOptPORT = _LpOptPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4)
)
_LpOptPORTTable_Object = MibTable
lpOptPORTTable = _LpOptPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    lpOptPORTTable.setStatus("mandatory")
_LpOptPORTEntry_Object = MibTableRow
lpOptPORTEntry = _LpOptPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1, 1)
)
lpOptPORTEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPORTSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPORTIndex"),
)
if mibBuilder.loadTexts:
    lpOptPORTEntry.setStatus("mandatory")


class _LpOptPORTSMTIndex_Type(Integer32):
    """Custom type lpOptPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPORTSMTIndex_Type.__name__ = "Integer32"
_LpOptPORTSMTIndex_Object = MibTableColumn
lpOptPORTSMTIndex = _LpOptPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1, 1, 1),
    _LpOptPORTSMTIndex_Type()
)
lpOptPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTSMTIndex.setStatus("mandatory")


class _LpOptPORTIndex_Type(Integer32):
    """Custom type lpOptPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPORTIndex_Type.__name__ = "Integer32"
_LpOptPORTIndex_Object = MibTableColumn
lpOptPORTIndex = _LpOptPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1, 1, 2),
    _LpOptPORTIndex_Type()
)
lpOptPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTIndex.setStatus("mandatory")
_LpOptPORTMACLoopTime_Type = FddiTimeNano
_LpOptPORTMACLoopTime_Object = MibTableColumn
lpOptPORTMACLoopTime = _LpOptPORTMACLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1, 1, 3),
    _LpOptPORTMACLoopTime_Type()
)
lpOptPORTMACLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPORTMACLoopTime.setStatus("mandatory")
_LpOptPORTEBErrorCt_Type = Counter32
_LpOptPORTEBErrorCt_Object = MibTableColumn
lpOptPORTEBErrorCt = _LpOptPORTEBErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 1, 1, 4),
    _LpOptPORTEBErrorCt_Type()
)
lpOptPORTEBErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTEBErrorCt.setStatus("mandatory")
_LpOptPORTLSTable_Object = MibTable
lpOptPORTLSTable = _LpOptPORTLSTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2)
)
if mibBuilder.loadTexts:
    lpOptPORTLSTable.setStatus("mandatory")
_LpOptPORTLSEntry_Object = MibTableRow
lpOptPORTLSEntry = _LpOptPORTLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2, 1)
)
lpOptPORTLSEntry.setIndexNames(
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPORTLSSMTIndex"),
    (0, "LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPORTLSPORTIndex"),
)
if mibBuilder.loadTexts:
    lpOptPORTLSEntry.setStatus("mandatory")


class _LpOptPORTLSSMTIndex_Type(Integer32):
    """Custom type lpOptPORTLSSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPORTLSSMTIndex_Type.__name__ = "Integer32"
_LpOptPORTLSSMTIndex_Object = MibTableColumn
lpOptPORTLSSMTIndex = _LpOptPORTLSSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2, 1, 1),
    _LpOptPORTLSSMTIndex_Type()
)
lpOptPORTLSSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTLSSMTIndex.setStatus("mandatory")


class _LpOptPORTLSPORTIndex_Type(Integer32):
    """Custom type lpOptPORTLSPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOptPORTLSPORTIndex_Type.__name__ = "Integer32"
_LpOptPORTLSPORTIndex_Object = MibTableColumn
lpOptPORTLSPORTIndex = _LpOptPORTLSPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2, 1, 2),
    _LpOptPORTLSPORTIndex_Type()
)
lpOptPORTLSPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTLSPORTIndex.setStatus("mandatory")


class _LpOptPORTMaintLS_Type(Integer32):
    """Custom type lpOptPORTMaintLS based on Integer32"""
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


_LpOptPORTMaintLS_Type.__name__ = "Integer32"
_LpOptPORTMaintLS_Object = MibTableColumn
lpOptPORTMaintLS = _LpOptPORTMaintLS_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2, 1, 3),
    _LpOptPORTMaintLS_Type()
)
lpOptPORTMaintLS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOptPORTMaintLS.setStatus("mandatory")


class _LpOptPORTPCLS_Type(Integer32):
    """Custom type lpOptPORTPCLS based on Integer32"""
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


_LpOptPORTPCLS_Type.__name__ = "Integer32"
_LpOptPORTPCLS_Object = MibTableColumn
lpOptPORTPCLS = _LpOptPORTPCLS_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 4, 2, 1, 4),
    _LpOptPORTPCLS_Type()
)
lpOptPORTPCLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOptPORTPCLS.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lpOptSMTHoldCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 1)
)
lpOptSMTHoldCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptSMTHoldState"))
)
if mibBuilder.loadTexts:
    lpOptSMTHoldCondition.setStatus(
        ""
    )

lpOptSMTPeerWrapCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 2)
)
lpOptSMTPeerWrapCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTCFState"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTPeerWrapFlag"))
)
if mibBuilder.loadTexts:
    lpOptSMTPeerWrapCondition.setStatus(
        ""
    )

lpOptMACDuplicateAddressCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 3)
)
lpOptMACDuplicateAddressCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTAddress"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACDaFlag"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUnaDaFlag"))
)
if mibBuilder.loadTexts:
    lpOptMACDuplicateAddressCondition.setStatus(
        ""
    )

lpOptMACFrameErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 4)
)
lpOptMACFrameErrorCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameErrorFlag"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACErrorCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACLostCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACFrameErrorRatio"))
)
if mibBuilder.loadTexts:
    lpOptMACFrameErrorCondition.setStatus(
        ""
    )

lpOptMACNotCopiedCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 5)
)
lpOptMACNotCopiedCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCopiedCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedRatio"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACNotCopiedFlag"))
)
if mibBuilder.loadTexts:
    lpOptMACNotCopiedCondition.setStatus(
        ""
    )

lpOptMACNeighborChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 6)
)
lpOptMACNeighborChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACOldUpstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACDownstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACOldDownstreamNbr"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTAddress"))
)
if mibBuilder.loadTexts:
    lpOptMACNeighborChangeEvent.setStatus(
        ""
    )

lpOptMACPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 7)
)
lpOptMACPathChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACAvailablePaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibMACRequestedPaths"))
)
if mibBuilder.loadTexts:
    lpOptMACPathChangeEvent.setStatus(
        ""
    )

lpOptPORTLerCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 8)
)
lpOptPORTLerCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerCutoff"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerAlarm"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerEstimate"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLemRejectCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLemCts"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTLerFlag"))
)
if mibBuilder.loadTexts:
    lpOptPORTLerCondition.setStatus(
        ""
    )

lpOptPORTUndesiredConnAttemptEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 9)
)
lpOptPORTUndesiredConnAttemptEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTMyType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTConnectState"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTNeighborType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTPCWithhold"))
)
if mibBuilder.loadTexts:
    lpOptPORTUndesiredConnAttemptEvent.setStatus(
        ""
    )

lpOptPORTEBErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 10)
)
lpOptPORTEBErrorCondition.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("LANPLEX-OPT-FDDI-MIB-1-1-2", "lpOptPORTEBErrorCt"))
)
if mibBuilder.loadTexts:
    lpOptPORTEBErrorCondition.setStatus(
        ""
    )

lpOptPORTPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 10, 0, 11)
)
lpOptPORTPathChangeEvent.setObjects(
      *(("DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTStationId"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTAvailablePaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTCurrentPath"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTRequestedPaths"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTMyType"),
        ("DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTNeighborType"))
)
if mibBuilder.loadTexts:
    lpOptPORTPathChangeEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANPLEX-OPT-FDDI-MIB-1-1-2",
    **{"synernetics": synernetics,
       "lanplex": lanplex,
       "lanplexOptFddi": lanplexOptFddi,
       "lpOptSMTHoldCondition": lpOptSMTHoldCondition,
       "lpOptSMTPeerWrapCondition": lpOptSMTPeerWrapCondition,
       "lpOptMACDuplicateAddressCondition": lpOptMACDuplicateAddressCondition,
       "lpOptMACFrameErrorCondition": lpOptMACFrameErrorCondition,
       "lpOptMACNotCopiedCondition": lpOptMACNotCopiedCondition,
       "lpOptMACNeighborChangeEvent": lpOptMACNeighborChangeEvent,
       "lpOptMACPathChangeEvent": lpOptMACPathChangeEvent,
       "lpOptPORTLerCondition": lpOptPORTLerCondition,
       "lpOptPORTUndesiredConnAttemptEvent": lpOptPORTUndesiredConnAttemptEvent,
       "lpOptPORTEBErrorCondition": lpOptPORTEBErrorCondition,
       "lpOptPORTPathChangeEvent": lpOptPORTPathChangeEvent,
       "lpOptSMT": lpOptSMT,
       "lpOptSMTTable": lpOptSMTTable,
       "lpOptSMTEntry": lpOptSMTEntry,
       "lpOptSMTIndex": lpOptSMTIndex,
       "lpOptSMTManufacturerOUI": lpOptSMTManufacturerOUI,
       "lpOptSMTManufacturerData": lpOptSMTManufacturerData,
       "lpOptSMTHoldState": lpOptSMTHoldState,
       "lpOptSMTSetCount": lpOptSMTSetCount,
       "lpOptSMTLastSetStationId": lpOptSMTLastSetStationId,
       "lpOptMAC": lpOptMAC,
       "lpOptMACBridgeFunctionTable": lpOptMACBridgeFunctionTable,
       "lpOptMACBridgeFunctionEntry": lpOptMACBridgeFunctionEntry,
       "lpOptMACBridgeFunctionSMTIndex": lpOptMACBridgeFunctionSMTIndex,
       "lpOptMACBridgeFunctionMACIndex": lpOptMACBridgeFunctionMACIndex,
       "lpOptMACBridgeFunctions": lpOptMACBridgeFunctions,
       "lpOptMACTPriTable": lpOptMACTPriTable,
       "lpOptMACTPriEntry": lpOptMACTPriEntry,
       "lpOptMACTPriSMTIndex": lpOptMACTPriSMTIndex,
       "lpOptMACTPriMACIndex": lpOptMACTPriMACIndex,
       "lpOptMACTPri0": lpOptMACTPri0,
       "lpOptMACTPri1": lpOptMACTPri1,
       "lpOptMACTPri2": lpOptMACTPri2,
       "lpOptMACTPri3": lpOptMACTPri3,
       "lpOptMACTPri4": lpOptMACTPri4,
       "lpOptMACTPri5": lpOptMACTPri5,
       "lpOptMACTPri6": lpOptMACTPri6,
       "lpOptPATH": lpOptPATH,
       "lpOptPATHRingTable": lpOptPATHRingTable,
       "lpOptPATHRingEntry": lpOptPATHRingEntry,
       "lpOptPATHRingSMTIndex": lpOptPATHRingSMTIndex,
       "lpOptPATHRingPATHIndex": lpOptPATHRingPATHIndex,
       "lpOptPATHRingLatency": lpOptPATHRingLatency,
       "lpOptPATHTraceStatus": lpOptPATHTraceStatus,
       "lpOptPATHT-Rmode": lpOptPATHT_Rmode,
       "lpOptPATHSbaTable": lpOptPATHSbaTable,
       "lpOptPATHSbaEntry": lpOptPATHSbaEntry,
       "lpOptPATHSbaSMTIndex": lpOptPATHSbaSMTIndex,
       "lpOptPATHSbaPATHIndex": lpOptPATHSbaPATHIndex,
       "lpOptPATHSbaPayload": lpOptPATHSbaPayload,
       "lpOptPATHSbaOverhead": lpOptPATHSbaOverhead,
       "lpOptPATHSbaAvailable": lpOptPATHSbaAvailable,
       "lpOptPORT": lpOptPORT,
       "lpOptPORTTable": lpOptPORTTable,
       "lpOptPORTEntry": lpOptPORTEntry,
       "lpOptPORTSMTIndex": lpOptPORTSMTIndex,
       "lpOptPORTIndex": lpOptPORTIndex,
       "lpOptPORTMACLoopTime": lpOptPORTMACLoopTime,
       "lpOptPORTEBErrorCt": lpOptPORTEBErrorCt,
       "lpOptPORTLSTable": lpOptPORTLSTable,
       "lpOptPORTLSEntry": lpOptPORTLSEntry,
       "lpOptPORTLSSMTIndex": lpOptPORTLSSMTIndex,
       "lpOptPORTLSPORTIndex": lpOptPORTLSPORTIndex,
       "lpOptPORTMaintLS": lpOptPORTMaintLS,
       "lpOptPORTPCLS": lpOptPORTPCLS}
)
