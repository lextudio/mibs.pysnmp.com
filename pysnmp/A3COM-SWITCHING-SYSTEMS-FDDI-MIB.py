# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-FDDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-FDDI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:48 2024
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
    "FDDI-SMT73-MIB",
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
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsFddiMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsFddiMib = _A3ComSwitchingSystemsFddiMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10)
)
_A3ComFddiSMT_ObjectIdentity = ObjectIdentity
a3ComFddiSMT = _A3ComFddiSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1)
)
_A3ComFddiSMTTable_Object = MibTable
a3ComFddiSMTTable = _A3ComFddiSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1)
)
if mibBuilder.loadTexts:
    a3ComFddiSMTTable.setStatus("mandatory")
_A3ComFddiSMTEntry_Object = MibTableRow
a3ComFddiSMTEntry = _A3ComFddiSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1)
)
a3ComFddiSMTEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiSMTIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiSMTEntry.setStatus("mandatory")


class _A3ComFddiSMTIndex_Type(Integer32):
    """Custom type a3ComFddiSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiSMTIndex_Object = MibTableColumn
a3ComFddiSMTIndex = _A3ComFddiSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 1),
    _A3ComFddiSMTIndex_Type()
)
a3ComFddiSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTIndex.setStatus("mandatory")


class _A3ComFddiSMTManufacturerOUI_Type(OctetString):
    """Custom type a3ComFddiSMTManufacturerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_A3ComFddiSMTManufacturerOUI_Type.__name__ = "OctetString"
_A3ComFddiSMTManufacturerOUI_Object = MibTableColumn
a3ComFddiSMTManufacturerOUI = _A3ComFddiSMTManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 2),
    _A3ComFddiSMTManufacturerOUI_Type()
)
a3ComFddiSMTManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTManufacturerOUI.setStatus("mandatory")


class _A3ComFddiSMTManufacturerData_Type(OctetString):
    """Custom type a3ComFddiSMTManufacturerData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_A3ComFddiSMTManufacturerData_Type.__name__ = "OctetString"
_A3ComFddiSMTManufacturerData_Object = MibTableColumn
a3ComFddiSMTManufacturerData = _A3ComFddiSMTManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 3),
    _A3ComFddiSMTManufacturerData_Type()
)
a3ComFddiSMTManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTManufacturerData.setStatus("mandatory")


class _A3ComFddiSMTHoldState_Type(Integer32):
    """Custom type a3ComFddiSMTHoldState based on Integer32"""
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


_A3ComFddiSMTHoldState_Type.__name__ = "Integer32"
_A3ComFddiSMTHoldState_Object = MibTableColumn
a3ComFddiSMTHoldState = _A3ComFddiSMTHoldState_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 4),
    _A3ComFddiSMTHoldState_Type()
)
a3ComFddiSMTHoldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTHoldState.setStatus("mandatory")
_A3ComFddiSMTSetCount_Type = Integer32
_A3ComFddiSMTSetCount_Object = MibTableColumn
a3ComFddiSMTSetCount = _A3ComFddiSMTSetCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 5),
    _A3ComFddiSMTSetCount_Type()
)
a3ComFddiSMTSetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTSetCount.setStatus("mandatory")
_A3ComFddiSMTLastSetStationId_Type = FddiSMTStationIdType
_A3ComFddiSMTLastSetStationId_Object = MibTableColumn
a3ComFddiSMTLastSetStationId = _A3ComFddiSMTLastSetStationId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 1, 1, 1, 6),
    _A3ComFddiSMTLastSetStationId_Type()
)
a3ComFddiSMTLastSetStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiSMTLastSetStationId.setStatus("mandatory")
_A3ComFddiMAC_ObjectIdentity = ObjectIdentity
a3ComFddiMAC = _A3ComFddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2)
)
_A3ComFddiMACBridgeFunctionTable_Object = MibTable
a3ComFddiMACBridgeFunctionTable = _A3ComFddiMACBridgeFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComFddiMACBridgeFunctionTable.setStatus("mandatory")
_A3ComFddiMACBridgeFunctionEntry_Object = MibTableRow
a3ComFddiMACBridgeFunctionEntry = _A3ComFddiMACBridgeFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 1, 1)
)
a3ComFddiMACBridgeFunctionEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiMACBridgeFunctionSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiMACBridgeFunctionMACIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiMACBridgeFunctionEntry.setStatus("mandatory")


class _A3ComFddiMACBridgeFunctionSMTIndex_Type(Integer32):
    """Custom type a3ComFddiMACBridgeFunctionSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiMACBridgeFunctionSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiMACBridgeFunctionSMTIndex_Object = MibTableColumn
a3ComFddiMACBridgeFunctionSMTIndex = _A3ComFddiMACBridgeFunctionSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 1, 1, 1),
    _A3ComFddiMACBridgeFunctionSMTIndex_Type()
)
a3ComFddiMACBridgeFunctionSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACBridgeFunctionSMTIndex.setStatus("mandatory")


class _A3ComFddiMACBridgeFunctionMACIndex_Type(Integer32):
    """Custom type a3ComFddiMACBridgeFunctionMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiMACBridgeFunctionMACIndex_Type.__name__ = "Integer32"
_A3ComFddiMACBridgeFunctionMACIndex_Object = MibTableColumn
a3ComFddiMACBridgeFunctionMACIndex = _A3ComFddiMACBridgeFunctionMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 1, 1, 2),
    _A3ComFddiMACBridgeFunctionMACIndex_Type()
)
a3ComFddiMACBridgeFunctionMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACBridgeFunctionMACIndex.setStatus("mandatory")


class _A3ComFddiMACBridgeFunctions_Type(Integer32):
    """Custom type a3ComFddiMACBridgeFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_A3ComFddiMACBridgeFunctions_Type.__name__ = "Integer32"
_A3ComFddiMACBridgeFunctions_Object = MibTableColumn
a3ComFddiMACBridgeFunctions = _A3ComFddiMACBridgeFunctions_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 1, 1, 3),
    _A3ComFddiMACBridgeFunctions_Type()
)
a3ComFddiMACBridgeFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACBridgeFunctions.setStatus("mandatory")
_A3ComFddiMACTPriTable_Object = MibTable
a3ComFddiMACTPriTable = _A3ComFddiMACTPriTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComFddiMACTPriTable.setStatus("mandatory")
_A3ComFddiMACTPriEntry_Object = MibTableRow
a3ComFddiMACTPriEntry = _A3ComFddiMACTPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1)
)
a3ComFddiMACTPriEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiMACTPriSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiMACTPriMACIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiMACTPriEntry.setStatus("mandatory")


class _A3ComFddiMACTPriSMTIndex_Type(Integer32):
    """Custom type a3ComFddiMACTPriSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiMACTPriSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiMACTPriSMTIndex_Object = MibTableColumn
a3ComFddiMACTPriSMTIndex = _A3ComFddiMACTPriSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 1),
    _A3ComFddiMACTPriSMTIndex_Type()
)
a3ComFddiMACTPriSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPriSMTIndex.setStatus("mandatory")


class _A3ComFddiMACTPriMACIndex_Type(Integer32):
    """Custom type a3ComFddiMACTPriMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiMACTPriMACIndex_Type.__name__ = "Integer32"
_A3ComFddiMACTPriMACIndex_Object = MibTableColumn
a3ComFddiMACTPriMACIndex = _A3ComFddiMACTPriMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 2),
    _A3ComFddiMACTPriMACIndex_Type()
)
a3ComFddiMACTPriMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPriMACIndex.setStatus("mandatory")
_A3ComFddiMACTPri0_Type = FddiTimeNano
_A3ComFddiMACTPri0_Object = MibTableColumn
a3ComFddiMACTPri0 = _A3ComFddiMACTPri0_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 3),
    _A3ComFddiMACTPri0_Type()
)
a3ComFddiMACTPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri0.setStatus("mandatory")
_A3ComFddiMACTPri1_Type = FddiTimeNano
_A3ComFddiMACTPri1_Object = MibTableColumn
a3ComFddiMACTPri1 = _A3ComFddiMACTPri1_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 4),
    _A3ComFddiMACTPri1_Type()
)
a3ComFddiMACTPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri1.setStatus("mandatory")
_A3ComFddiMACTPri2_Type = FddiTimeNano
_A3ComFddiMACTPri2_Object = MibTableColumn
a3ComFddiMACTPri2 = _A3ComFddiMACTPri2_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 5),
    _A3ComFddiMACTPri2_Type()
)
a3ComFddiMACTPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri2.setStatus("mandatory")
_A3ComFddiMACTPri3_Type = FddiTimeNano
_A3ComFddiMACTPri3_Object = MibTableColumn
a3ComFddiMACTPri3 = _A3ComFddiMACTPri3_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 6),
    _A3ComFddiMACTPri3_Type()
)
a3ComFddiMACTPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri3.setStatus("mandatory")
_A3ComFddiMACTPri4_Type = FddiTimeNano
_A3ComFddiMACTPri4_Object = MibTableColumn
a3ComFddiMACTPri4 = _A3ComFddiMACTPri4_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 7),
    _A3ComFddiMACTPri4_Type()
)
a3ComFddiMACTPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri4.setStatus("mandatory")
_A3ComFddiMACTPri5_Type = FddiTimeNano
_A3ComFddiMACTPri5_Object = MibTableColumn
a3ComFddiMACTPri5 = _A3ComFddiMACTPri5_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 8),
    _A3ComFddiMACTPri5_Type()
)
a3ComFddiMACTPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri5.setStatus("mandatory")
_A3ComFddiMACTPri6_Type = FddiTimeNano
_A3ComFddiMACTPri6_Object = MibTableColumn
a3ComFddiMACTPri6 = _A3ComFddiMACTPri6_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 2, 2, 1, 9),
    _A3ComFddiMACTPri6_Type()
)
a3ComFddiMACTPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiMACTPri6.setStatus("mandatory")
_A3ComFddiPATH_ObjectIdentity = ObjectIdentity
a3ComFddiPATH = _A3ComFddiPATH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3)
)
_A3ComFddiPATHRingTable_Object = MibTable
a3ComFddiPATHRingTable = _A3ComFddiPATHRingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1)
)
if mibBuilder.loadTexts:
    a3ComFddiPATHRingTable.setStatus("mandatory")
_A3ComFddiPATHRingEntry_Object = MibTableRow
a3ComFddiPATHRingEntry = _A3ComFddiPATHRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1)
)
a3ComFddiPATHRingEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPATHRingSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPATHRingPATHIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiPATHRingEntry.setStatus("mandatory")


class _A3ComFddiPATHRingSMTIndex_Type(Integer32):
    """Custom type a3ComFddiPATHRingSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPATHRingSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiPATHRingSMTIndex_Object = MibTableColumn
a3ComFddiPATHRingSMTIndex = _A3ComFddiPATHRingSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1, 1),
    _A3ComFddiPATHRingSMTIndex_Type()
)
a3ComFddiPATHRingSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPATHRingSMTIndex.setStatus("mandatory")


class _A3ComFddiPATHRingPATHIndex_Type(Integer32):
    """Custom type a3ComFddiPATHRingPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComFddiPATHRingPATHIndex_Type.__name__ = "Integer32"
_A3ComFddiPATHRingPATHIndex_Object = MibTableColumn
a3ComFddiPATHRingPATHIndex = _A3ComFddiPATHRingPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1, 2),
    _A3ComFddiPATHRingPATHIndex_Type()
)
a3ComFddiPATHRingPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPATHRingPATHIndex.setStatus("mandatory")
_A3ComFddiPATHRingLatency_Type = FddiTimeNano
_A3ComFddiPATHRingLatency_Object = MibTableColumn
a3ComFddiPATHRingLatency = _A3ComFddiPATHRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1, 3),
    _A3ComFddiPATHRingLatency_Type()
)
a3ComFddiPATHRingLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPATHRingLatency.setStatus("mandatory")


class _A3ComFddiPATHTraceStatus_Type(Integer32):
    """Custom type a3ComFddiPATHTraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3ComFddiPATHTraceStatus_Type.__name__ = "Integer32"
_A3ComFddiPATHTraceStatus_Object = MibTableColumn
a3ComFddiPATHTraceStatus = _A3ComFddiPATHTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1, 4),
    _A3ComFddiPATHTraceStatus_Type()
)
a3ComFddiPATHTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPATHTraceStatus.setStatus("mandatory")
_A3ComFddiPATHT_Rmode_Type = FddiTimeNano
_A3ComFddiPATHT_Rmode_Object = MibScalar
a3ComFddiPATHT_Rmode = _A3ComFddiPATHT_Rmode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 1, 1, 5),
    _A3ComFddiPATHT_Rmode_Type()
)
a3ComFddiPATHT_Rmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPATHT_Rmode.setStatus("mandatory")
_A3ComFddiPATHSbaTable_Object = MibTable
a3ComFddiPATHSbaTable = _A3ComFddiPATHSbaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2)
)
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaTable.setStatus("mandatory")
_A3ComFddiPATHSbaEntry_Object = MibTableRow
a3ComFddiPATHSbaEntry = _A3ComFddiPATHSbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1)
)
a3ComFddiPATHSbaEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPATHSbaSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPATHSbaPATHIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaEntry.setStatus("mandatory")


class _A3ComFddiPATHSbaSMTIndex_Type(Integer32):
    """Custom type a3ComFddiPATHSbaSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPATHSbaSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiPATHSbaSMTIndex_Object = MibTableColumn
a3ComFddiPATHSbaSMTIndex = _A3ComFddiPATHSbaSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1, 1),
    _A3ComFddiPATHSbaSMTIndex_Type()
)
a3ComFddiPATHSbaSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaSMTIndex.setStatus("mandatory")


class _A3ComFddiPATHSbaPATHIndex_Type(Integer32):
    """Custom type a3ComFddiPATHSbaPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComFddiPATHSbaPATHIndex_Type.__name__ = "Integer32"
_A3ComFddiPATHSbaPATHIndex_Object = MibTableColumn
a3ComFddiPATHSbaPATHIndex = _A3ComFddiPATHSbaPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1, 2),
    _A3ComFddiPATHSbaPATHIndex_Type()
)
a3ComFddiPATHSbaPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaPATHIndex.setStatus("mandatory")


class _A3ComFddiPATHSbaPayload_Type(Integer32):
    """Custom type a3ComFddiPATHSbaPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1562),
    )


_A3ComFddiPATHSbaPayload_Type.__name__ = "Integer32"
_A3ComFddiPATHSbaPayload_Object = MibTableColumn
a3ComFddiPATHSbaPayload = _A3ComFddiPATHSbaPayload_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1, 3),
    _A3ComFddiPATHSbaPayload_Type()
)
a3ComFddiPATHSbaPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaPayload.setStatus("mandatory")
_A3ComFddiPATHSbaOverhead_Type = Integer32
_A3ComFddiPATHSbaOverhead_Object = MibTableColumn
a3ComFddiPATHSbaOverhead = _A3ComFddiPATHSbaOverhead_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1, 4),
    _A3ComFddiPATHSbaOverhead_Type()
)
a3ComFddiPATHSbaOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaOverhead.setStatus("mandatory")


class _A3ComFddiPATHSbaAvailable_Type(Integer32):
    """Custom type a3ComFddiPATHSbaAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12500000),
    )


_A3ComFddiPATHSbaAvailable_Type.__name__ = "Integer32"
_A3ComFddiPATHSbaAvailable_Object = MibTableColumn
a3ComFddiPATHSbaAvailable = _A3ComFddiPATHSbaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 3, 2, 1, 5),
    _A3ComFddiPATHSbaAvailable_Type()
)
a3ComFddiPATHSbaAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPATHSbaAvailable.setStatus("mandatory")
_A3ComFddiPORT_ObjectIdentity = ObjectIdentity
a3ComFddiPORT = _A3ComFddiPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4)
)
_A3ComFddiPORTTable_Object = MibTable
a3ComFddiPORTTable = _A3ComFddiPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1)
)
if mibBuilder.loadTexts:
    a3ComFddiPORTTable.setStatus("mandatory")
_A3ComFddiPORTEntry_Object = MibTableRow
a3ComFddiPORTEntry = _A3ComFddiPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1, 1)
)
a3ComFddiPORTEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPORTSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPORTIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiPORTEntry.setStatus("mandatory")


class _A3ComFddiPORTSMTIndex_Type(Integer32):
    """Custom type a3ComFddiPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPORTSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiPORTSMTIndex_Object = MibTableColumn
a3ComFddiPORTSMTIndex = _A3ComFddiPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1, 1, 1),
    _A3ComFddiPORTSMTIndex_Type()
)
a3ComFddiPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTSMTIndex.setStatus("mandatory")


class _A3ComFddiPORTIndex_Type(Integer32):
    """Custom type a3ComFddiPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPORTIndex_Type.__name__ = "Integer32"
_A3ComFddiPORTIndex_Object = MibTableColumn
a3ComFddiPORTIndex = _A3ComFddiPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1, 1, 2),
    _A3ComFddiPORTIndex_Type()
)
a3ComFddiPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTIndex.setStatus("mandatory")
_A3ComFddiPORTMACLoopTime_Type = FddiTimeNano
_A3ComFddiPORTMACLoopTime_Object = MibTableColumn
a3ComFddiPORTMACLoopTime = _A3ComFddiPORTMACLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1, 1, 3),
    _A3ComFddiPORTMACLoopTime_Type()
)
a3ComFddiPORTMACLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPORTMACLoopTime.setStatus("mandatory")
_A3ComFddiPORTEBErrorCt_Type = Counter32
_A3ComFddiPORTEBErrorCt_Object = MibTableColumn
a3ComFddiPORTEBErrorCt = _A3ComFddiPORTEBErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 1, 1, 4),
    _A3ComFddiPORTEBErrorCt_Type()
)
a3ComFddiPORTEBErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTEBErrorCt.setStatus("mandatory")
_A3ComFddiPORTLSTable_Object = MibTable
a3ComFddiPORTLSTable = _A3ComFddiPORTLSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2)
)
if mibBuilder.loadTexts:
    a3ComFddiPORTLSTable.setStatus("mandatory")
_A3ComFddiPORTLSEntry_Object = MibTableRow
a3ComFddiPORTLSEntry = _A3ComFddiPORTLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2, 1)
)
a3ComFddiPORTLSEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPORTLSSMTIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPORTLSPORTIndex"),
)
if mibBuilder.loadTexts:
    a3ComFddiPORTLSEntry.setStatus("mandatory")


class _A3ComFddiPORTLSSMTIndex_Type(Integer32):
    """Custom type a3ComFddiPORTLSSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPORTLSSMTIndex_Type.__name__ = "Integer32"
_A3ComFddiPORTLSSMTIndex_Object = MibTableColumn
a3ComFddiPORTLSSMTIndex = _A3ComFddiPORTLSSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2, 1, 1),
    _A3ComFddiPORTLSSMTIndex_Type()
)
a3ComFddiPORTLSSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTLSSMTIndex.setStatus("mandatory")


class _A3ComFddiPORTLSPORTIndex_Type(Integer32):
    """Custom type a3ComFddiPORTLSPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFddiPORTLSPORTIndex_Type.__name__ = "Integer32"
_A3ComFddiPORTLSPORTIndex_Object = MibTableColumn
a3ComFddiPORTLSPORTIndex = _A3ComFddiPORTLSPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2, 1, 2),
    _A3ComFddiPORTLSPORTIndex_Type()
)
a3ComFddiPORTLSPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTLSPORTIndex.setStatus("mandatory")


class _A3ComFddiPORTMaintLS_Type(Integer32):
    """Custom type a3ComFddiPORTMaintLS based on Integer32"""
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


_A3ComFddiPORTMaintLS_Type.__name__ = "Integer32"
_A3ComFddiPORTMaintLS_Object = MibTableColumn
a3ComFddiPORTMaintLS = _A3ComFddiPORTMaintLS_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2, 1, 3),
    _A3ComFddiPORTMaintLS_Type()
)
a3ComFddiPORTMaintLS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFddiPORTMaintLS.setStatus("mandatory")


class _A3ComFddiPORTPCLS_Type(Integer32):
    """Custom type a3ComFddiPORTPCLS based on Integer32"""
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


_A3ComFddiPORTPCLS_Type.__name__ = "Integer32"
_A3ComFddiPORTPCLS_Object = MibTableColumn
a3ComFddiPORTPCLS = _A3ComFddiPORTPCLS_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 4, 2, 1, 4),
    _A3ComFddiPORTPCLS_Type()
)
a3ComFddiPORTPCLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFddiPORTPCLS.setStatus("mandatory")

# Managed Objects groups


# Notification objects

a3ComFddiSMTHoldCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 1)
)
a3ComFddiSMTHoldCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiSMTHoldState"))
)
if mibBuilder.loadTexts:
    a3ComFddiSMTHoldCondition.setStatus(
        ""
    )

a3ComFddiSMTPeerWrapCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 2)
)
a3ComFddiSMTPeerWrapCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibSMTCFState"),
        ("FDDI-SMT73-MIB", "fddimibSMTPeerWrapFlag"))
)
if mibBuilder.loadTexts:
    a3ComFddiSMTPeerWrapCondition.setStatus(
        ""
    )

a3ComFddiMACDuplicateAddressCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 3)
)
a3ComFddiMACDuplicateAddressCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibMACSMTAddress"),
        ("FDDI-SMT73-MIB", "fddimibMACUpstreamNbr"),
        ("FDDI-SMT73-MIB", "fddimibMACDaFlag"),
        ("FDDI-SMT73-MIB", "fddimibMACUnaDaFlag"))
)
if mibBuilder.loadTexts:
    a3ComFddiMACDuplicateAddressCondition.setStatus(
        ""
    )

a3ComFddiMACFrameErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 4)
)
a3ComFddiMACFrameErrorCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibMACFrameErrorFlag"),
        ("FDDI-SMT73-MIB", "fddimibMACFrameCts"),
        ("FDDI-SMT73-MIB", "fddimibMACErrorCts"),
        ("FDDI-SMT73-MIB", "fddimibMACLostCts"),
        ("FDDI-SMT73-MIB", "fddimibMACFrameErrorRatio"))
)
if mibBuilder.loadTexts:
    a3ComFddiMACFrameErrorCondition.setStatus(
        ""
    )

a3ComFddiMACNotCopiedCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 5)
)
a3ComFddiMACNotCopiedCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibMACNotCopiedCts"),
        ("FDDI-SMT73-MIB", "fddimibMACCopiedCts"),
        ("FDDI-SMT73-MIB", "fddimibMACNotCopiedRatio"),
        ("FDDI-SMT73-MIB", "fddimibMACNotCopiedFlag"))
)
if mibBuilder.loadTexts:
    a3ComFddiMACNotCopiedCondition.setStatus(
        ""
    )

a3ComFddiMACNeighborChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 6)
)
a3ComFddiMACNeighborChangeEvent.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibMACUpstreamNbr"),
        ("FDDI-SMT73-MIB", "fddimibMACOldUpstreamNbr"),
        ("FDDI-SMT73-MIB", "fddimibMACDownstreamNbr"),
        ("FDDI-SMT73-MIB", "fddimibMACOldDownstreamNbr"),
        ("FDDI-SMT73-MIB", "fddimibMACCurrentPath"),
        ("FDDI-SMT73-MIB", "fddimibMACSMTAddress"))
)
if mibBuilder.loadTexts:
    a3ComFddiMACNeighborChangeEvent.setStatus(
        ""
    )

a3ComFddiMACPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 7)
)
a3ComFddiMACPathChangeEvent.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibMACAvailablePaths"),
        ("FDDI-SMT73-MIB", "fddimibMACCurrentPath"),
        ("FDDI-SMT73-MIB", "fddimibMACRequestedPaths"))
)
if mibBuilder.loadTexts:
    a3ComFddiMACPathChangeEvent.setStatus(
        ""
    )

a3ComFddiPORTLerCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 8)
)
a3ComFddiPORTLerCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibPORTLerCutoff"),
        ("FDDI-SMT73-MIB", "fddimibPORTLerAlarm"),
        ("FDDI-SMT73-MIB", "fddimibPORTLerEstimate"),
        ("FDDI-SMT73-MIB", "fddimibPORTLemRejectCts"),
        ("FDDI-SMT73-MIB", "fddimibPORTLemCts"),
        ("FDDI-SMT73-MIB", "fddimibPORTLerFlag"))
)
if mibBuilder.loadTexts:
    a3ComFddiPORTLerCondition.setStatus(
        ""
    )

a3ComFddiPORTUndesiredConnAttemptEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 9)
)
a3ComFddiPORTUndesiredConnAttemptEvent.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibPORTMyType"),
        ("FDDI-SMT73-MIB", "fddimibPORTConnectState"),
        ("FDDI-SMT73-MIB", "fddimibPORTNeighborType"),
        ("FDDI-SMT73-MIB", "fddimibPORTPCWithhold"))
)
if mibBuilder.loadTexts:
    a3ComFddiPORTUndesiredConnAttemptEvent.setStatus(
        ""
    )

a3ComFddiPORTEBErrorCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 10)
)
a3ComFddiPORTEBErrorCondition.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("A3COM-SWITCHING-SYSTEMS-FDDI-MIB", "a3ComFddiPORTEBErrorCt"))
)
if mibBuilder.loadTexts:
    a3ComFddiPORTEBErrorCondition.setStatus(
        ""
    )

a3ComFddiPORTPathChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 10, 0, 11)
)
a3ComFddiPORTPathChangeEvent.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTStationId"),
        ("FDDI-SMT73-MIB", "fddimibPORTAvailablePaths"),
        ("FDDI-SMT73-MIB", "fddimibPORTCurrentPath"),
        ("FDDI-SMT73-MIB", "fddimibPORTRequestedPaths"),
        ("FDDI-SMT73-MIB", "fddimibPORTMyType"),
        ("FDDI-SMT73-MIB", "fddimibPORTNeighborType"))
)
if mibBuilder.loadTexts:
    a3ComFddiPORTPathChangeEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-FDDI-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsFddiMib": a3ComSwitchingSystemsFddiMib,
       "a3ComFddiSMTHoldCondition": a3ComFddiSMTHoldCondition,
       "a3ComFddiSMTPeerWrapCondition": a3ComFddiSMTPeerWrapCondition,
       "a3ComFddiMACDuplicateAddressCondition": a3ComFddiMACDuplicateAddressCondition,
       "a3ComFddiMACFrameErrorCondition": a3ComFddiMACFrameErrorCondition,
       "a3ComFddiMACNotCopiedCondition": a3ComFddiMACNotCopiedCondition,
       "a3ComFddiMACNeighborChangeEvent": a3ComFddiMACNeighborChangeEvent,
       "a3ComFddiMACPathChangeEvent": a3ComFddiMACPathChangeEvent,
       "a3ComFddiPORTLerCondition": a3ComFddiPORTLerCondition,
       "a3ComFddiPORTUndesiredConnAttemptEvent": a3ComFddiPORTUndesiredConnAttemptEvent,
       "a3ComFddiPORTEBErrorCondition": a3ComFddiPORTEBErrorCondition,
       "a3ComFddiPORTPathChangeEvent": a3ComFddiPORTPathChangeEvent,
       "a3ComFddiSMT": a3ComFddiSMT,
       "a3ComFddiSMTTable": a3ComFddiSMTTable,
       "a3ComFddiSMTEntry": a3ComFddiSMTEntry,
       "a3ComFddiSMTIndex": a3ComFddiSMTIndex,
       "a3ComFddiSMTManufacturerOUI": a3ComFddiSMTManufacturerOUI,
       "a3ComFddiSMTManufacturerData": a3ComFddiSMTManufacturerData,
       "a3ComFddiSMTHoldState": a3ComFddiSMTHoldState,
       "a3ComFddiSMTSetCount": a3ComFddiSMTSetCount,
       "a3ComFddiSMTLastSetStationId": a3ComFddiSMTLastSetStationId,
       "a3ComFddiMAC": a3ComFddiMAC,
       "a3ComFddiMACBridgeFunctionTable": a3ComFddiMACBridgeFunctionTable,
       "a3ComFddiMACBridgeFunctionEntry": a3ComFddiMACBridgeFunctionEntry,
       "a3ComFddiMACBridgeFunctionSMTIndex": a3ComFddiMACBridgeFunctionSMTIndex,
       "a3ComFddiMACBridgeFunctionMACIndex": a3ComFddiMACBridgeFunctionMACIndex,
       "a3ComFddiMACBridgeFunctions": a3ComFddiMACBridgeFunctions,
       "a3ComFddiMACTPriTable": a3ComFddiMACTPriTable,
       "a3ComFddiMACTPriEntry": a3ComFddiMACTPriEntry,
       "a3ComFddiMACTPriSMTIndex": a3ComFddiMACTPriSMTIndex,
       "a3ComFddiMACTPriMACIndex": a3ComFddiMACTPriMACIndex,
       "a3ComFddiMACTPri0": a3ComFddiMACTPri0,
       "a3ComFddiMACTPri1": a3ComFddiMACTPri1,
       "a3ComFddiMACTPri2": a3ComFddiMACTPri2,
       "a3ComFddiMACTPri3": a3ComFddiMACTPri3,
       "a3ComFddiMACTPri4": a3ComFddiMACTPri4,
       "a3ComFddiMACTPri5": a3ComFddiMACTPri5,
       "a3ComFddiMACTPri6": a3ComFddiMACTPri6,
       "a3ComFddiPATH": a3ComFddiPATH,
       "a3ComFddiPATHRingTable": a3ComFddiPATHRingTable,
       "a3ComFddiPATHRingEntry": a3ComFddiPATHRingEntry,
       "a3ComFddiPATHRingSMTIndex": a3ComFddiPATHRingSMTIndex,
       "a3ComFddiPATHRingPATHIndex": a3ComFddiPATHRingPATHIndex,
       "a3ComFddiPATHRingLatency": a3ComFddiPATHRingLatency,
       "a3ComFddiPATHTraceStatus": a3ComFddiPATHTraceStatus,
       "a3ComFddiPATHT-Rmode": a3ComFddiPATHT_Rmode,
       "a3ComFddiPATHSbaTable": a3ComFddiPATHSbaTable,
       "a3ComFddiPATHSbaEntry": a3ComFddiPATHSbaEntry,
       "a3ComFddiPATHSbaSMTIndex": a3ComFddiPATHSbaSMTIndex,
       "a3ComFddiPATHSbaPATHIndex": a3ComFddiPATHSbaPATHIndex,
       "a3ComFddiPATHSbaPayload": a3ComFddiPATHSbaPayload,
       "a3ComFddiPATHSbaOverhead": a3ComFddiPATHSbaOverhead,
       "a3ComFddiPATHSbaAvailable": a3ComFddiPATHSbaAvailable,
       "a3ComFddiPORT": a3ComFddiPORT,
       "a3ComFddiPORTTable": a3ComFddiPORTTable,
       "a3ComFddiPORTEntry": a3ComFddiPORTEntry,
       "a3ComFddiPORTSMTIndex": a3ComFddiPORTSMTIndex,
       "a3ComFddiPORTIndex": a3ComFddiPORTIndex,
       "a3ComFddiPORTMACLoopTime": a3ComFddiPORTMACLoopTime,
       "a3ComFddiPORTEBErrorCt": a3ComFddiPORTEBErrorCt,
       "a3ComFddiPORTLSTable": a3ComFddiPORTLSTable,
       "a3ComFddiPORTLSEntry": a3ComFddiPORTLSEntry,
       "a3ComFddiPORTLSSMTIndex": a3ComFddiPORTLSSMTIndex,
       "a3ComFddiPORTLSPORTIndex": a3ComFddiPORTLSPORTIndex,
       "a3ComFddiPORTMaintLS": a3ComFddiPORTMaintLS,
       "a3ComFddiPORTPCLS": a3ComFddiPORTPCLS}
)
