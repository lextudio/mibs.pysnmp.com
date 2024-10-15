# SNMP MIB module (HP-SN-MPLS-LSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:48 2024
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

(MplsBitRate,
 MplsBurstSize,
 MplsInitialCreationSource,
 MplsLSPID,
 MplsLabel,
 mplsMIB) = mibBuilder.importSymbols(
    "HP-SN-MPLS-TC-MIB",
    "MplsBitRate",
    "MplsBurstSize",
    "MplsInitialCreationSource",
    "MplsLSPID",
    "MplsLabel",
    "mplsMIB")

(snMpls,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snMpls")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLsrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2)
)
mplsLsrMIB.setRevisions(
        ("2002-01-04 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLsrObjects_ObjectIdentity = ObjectIdentity
mplsLsrObjects = _MplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1)
)
_MplsInterfaceConfTable_Object = MibTable
mplsInterfaceConfTable = _MplsInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsInterfaceConfTable.setStatus("current")
_MplsInterfaceConfEntry_Object = MibTableRow
mplsInterfaceConfEntry = _MplsInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1)
)
mplsInterfaceConfEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    mplsInterfaceConfEntry.setStatus("current")
_MplsInterfaceConfIndex_Type = InterfaceIndexOrZero
_MplsInterfaceConfIndex_Object = MibTableColumn
mplsInterfaceConfIndex = _MplsInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 1),
    _MplsInterfaceConfIndex_Type()
)
mplsInterfaceConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInterfaceConfIndex.setStatus("current")
_MplsInterfaceLabelMinIn_Type = MplsLabel
_MplsInterfaceLabelMinIn_Object = MibTableColumn
mplsInterfaceLabelMinIn = _MplsInterfaceLabelMinIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 2),
    _MplsInterfaceLabelMinIn_Type()
)
mplsInterfaceLabelMinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinIn.setStatus("current")
_MplsInterfaceLabelMaxIn_Type = MplsLabel
_MplsInterfaceLabelMaxIn_Object = MibTableColumn
mplsInterfaceLabelMaxIn = _MplsInterfaceLabelMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 3),
    _MplsInterfaceLabelMaxIn_Type()
)
mplsInterfaceLabelMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxIn.setStatus("current")
_MplsInterfaceLabelMinOut_Type = MplsLabel
_MplsInterfaceLabelMinOut_Object = MibTableColumn
mplsInterfaceLabelMinOut = _MplsInterfaceLabelMinOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 4),
    _MplsInterfaceLabelMinOut_Type()
)
mplsInterfaceLabelMinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinOut.setStatus("current")
_MplsInterfaceLabelMaxOut_Type = MplsLabel
_MplsInterfaceLabelMaxOut_Object = MibTableColumn
mplsInterfaceLabelMaxOut = _MplsInterfaceLabelMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 5),
    _MplsInterfaceLabelMaxOut_Type()
)
mplsInterfaceLabelMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxOut.setStatus("current")
_MplsInterfaceTotalBandwidth_Type = MplsBitRate
_MplsInterfaceTotalBandwidth_Object = MibTableColumn
mplsInterfaceTotalBandwidth = _MplsInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 6),
    _MplsInterfaceTotalBandwidth_Type()
)
mplsInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceTotalBandwidth.setStatus("current")
_MplsInterfaceAvailableBandwidth_Type = MplsBitRate
_MplsInterfaceAvailableBandwidth_Object = MibTableColumn
mplsInterfaceAvailableBandwidth = _MplsInterfaceAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 7),
    _MplsInterfaceAvailableBandwidth_Type()
)
mplsInterfaceAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceAvailableBandwidth.setStatus("current")


class _MplsInterfaceLabelParticipationType_Type(Bits):
    """Custom type mplsInterfaceLabelParticipationType based on Bits"""
    namedValues = NamedValues(
        *(("perInterface", 1),
          ("perPlatform", 0))
    )

_MplsInterfaceLabelParticipationType_Type.__name__ = "Bits"
_MplsInterfaceLabelParticipationType_Object = MibTableColumn
mplsInterfaceLabelParticipationType = _MplsInterfaceLabelParticipationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 1, 1, 8),
    _MplsInterfaceLabelParticipationType_Type()
)
mplsInterfaceLabelParticipationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelParticipationType.setStatus("current")
_MplsInterfacePerfTable_Object = MibTable
mplsInterfacePerfTable = _MplsInterfacePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfTable.setStatus("current")
_MplsInterfacePerfEntry_Object = MibTableRow
mplsInterfacePerfEntry = _MplsInterfacePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfEntry.setStatus("current")
_MplsInterfaceInLabelsUsed_Type = Gauge32
_MplsInterfaceInLabelsUsed_Object = MibTableColumn
mplsInterfaceInLabelsUsed = _MplsInterfaceInLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2, 1, 1),
    _MplsInterfaceInLabelsUsed_Type()
)
mplsInterfaceInLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceInLabelsUsed.setStatus("current")
_MplsInterfaceFailedLabelLookup_Type = Counter32
_MplsInterfaceFailedLabelLookup_Object = MibTableColumn
mplsInterfaceFailedLabelLookup = _MplsInterfaceFailedLabelLookup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2, 1, 2),
    _MplsInterfaceFailedLabelLookup_Type()
)
mplsInterfaceFailedLabelLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceFailedLabelLookup.setStatus("current")
_MplsInterfaceOutLabelsUsed_Type = Gauge32
_MplsInterfaceOutLabelsUsed_Object = MibTableColumn
mplsInterfaceOutLabelsUsed = _MplsInterfaceOutLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2, 1, 3),
    _MplsInterfaceOutLabelsUsed_Type()
)
mplsInterfaceOutLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutLabelsUsed.setStatus("current")
_MplsInterfaceOutFragments_Type = Counter32
_MplsInterfaceOutFragments_Object = MibTableColumn
mplsInterfaceOutFragments = _MplsInterfaceOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 2, 1, 4),
    _MplsInterfaceOutFragments_Type()
)
mplsInterfaceOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceOutFragments.setStatus("current")
_MplsInSegmentTable_Object = MibTable
mplsInSegmentTable = _MplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mplsInSegmentTable.setStatus("current")
_MplsInSegmentEntry_Object = MibTableRow
mplsInSegmentEntry = _MplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1)
)
mplsInSegmentEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
    (0, "HP-SN-MPLS-LSR-MIB", "mplsInSegmentLabel"),
)
if mibBuilder.loadTexts:
    mplsInSegmentEntry.setStatus("current")
_MplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_MplsInSegmentIfIndex_Object = MibTableColumn
mplsInSegmentIfIndex = _MplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 1),
    _MplsInSegmentIfIndex_Type()
)
mplsInSegmentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentIfIndex.setStatus("current")
_MplsInSegmentLabel_Type = MplsLabel
_MplsInSegmentLabel_Object = MibTableColumn
mplsInSegmentLabel = _MplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 2),
    _MplsInSegmentLabel_Type()
)
mplsInSegmentLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentLabel.setStatus("current")


class _MplsInSegmentNPop_Type(Integer32):
    """Custom type mplsInSegmentNPop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsInSegmentNPop_Type.__name__ = "Integer32"
_MplsInSegmentNPop_Object = MibTableColumn
mplsInSegmentNPop = _MplsInSegmentNPop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 3),
    _MplsInSegmentNPop_Type()
)
mplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentNPop.setStatus("current")


class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):
    """Custom type mplsInSegmentAddrFamily based on AddressFamilyNumbers"""


_MplsInSegmentAddrFamily_Object = MibTableColumn
mplsInSegmentAddrFamily = _MplsInSegmentAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 4),
    _MplsInSegmentAddrFamily_Type()
)
mplsInSegmentAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentAddrFamily.setStatus("current")


class _MplsInSegmentXCIndex_Type(Unsigned32):
    """Custom type mplsInSegmentXCIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsInSegmentXCIndex_Type.__name__ = "Unsigned32"
_MplsInSegmentXCIndex_Object = MibTableColumn
mplsInSegmentXCIndex = _MplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 5),
    _MplsInSegmentXCIndex_Type()
)
mplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentXCIndex.setStatus("current")


class _MplsInSegmentOwner_Type(MplsInitialCreationSource):
    """Custom type mplsInSegmentOwner based on MplsInitialCreationSource"""


_MplsInSegmentOwner_Object = MibTableColumn
mplsInSegmentOwner = _MplsInSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 6),
    _MplsInSegmentOwner_Type()
)
mplsInSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentOwner.setStatus("current")
_MplsInSegmentTrafficParamPtr_Type = RowPointer
_MplsInSegmentTrafficParamPtr_Object = MibTableColumn
mplsInSegmentTrafficParamPtr = _MplsInSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 7),
    _MplsInSegmentTrafficParamPtr_Type()
)
mplsInSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentTrafficParamPtr.setStatus("current")
_MplsInSegmentRowStatus_Type = RowStatus
_MplsInSegmentRowStatus_Object = MibTableColumn
mplsInSegmentRowStatus = _MplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 8),
    _MplsInSegmentRowStatus_Type()
)
mplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentRowStatus.setStatus("current")
_MplsInSegmentStorageType_Type = StorageType
_MplsInSegmentStorageType_Object = MibTableColumn
mplsInSegmentStorageType = _MplsInSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 3, 1, 9),
    _MplsInSegmentStorageType_Type()
)
mplsInSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentStorageType.setStatus("current")
_MplsInSegmentPerfTable_Object = MibTable
mplsInSegmentPerfTable = _MplsInSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfTable.setStatus("current")
_MplsInSegmentPerfEntry_Object = MibTableRow
mplsInSegmentPerfEntry = _MplsInSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfEntry.setStatus("current")
_MplsInSegmentOctets_Type = Counter32
_MplsInSegmentOctets_Object = MibTableColumn
mplsInSegmentOctets = _MplsInSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 1),
    _MplsInSegmentOctets_Type()
)
mplsInSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentOctets.setStatus("current")
_MplsInSegmentPackets_Type = Counter32
_MplsInSegmentPackets_Object = MibTableColumn
mplsInSegmentPackets = _MplsInSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 2),
    _MplsInSegmentPackets_Type()
)
mplsInSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPackets.setStatus("current")
_MplsInSegmentErrors_Type = Counter32
_MplsInSegmentErrors_Object = MibTableColumn
mplsInSegmentErrors = _MplsInSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 3),
    _MplsInSegmentErrors_Type()
)
mplsInSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentErrors.setStatus("current")
_MplsInSegmentDiscards_Type = Counter32
_MplsInSegmentDiscards_Object = MibTableColumn
mplsInSegmentDiscards = _MplsInSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 4),
    _MplsInSegmentDiscards_Type()
)
mplsInSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentDiscards.setStatus("current")
_MplsInSegmentHCOctets_Type = Counter64
_MplsInSegmentHCOctets_Object = MibTableColumn
mplsInSegmentHCOctets = _MplsInSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 5),
    _MplsInSegmentHCOctets_Type()
)
mplsInSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentHCOctets.setStatus("current")
_MplsInSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsInSegmentPerfDiscontinuityTime = _MplsInSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 4, 1, 6),
    _MplsInSegmentPerfDiscontinuityTime_Type()
)
mplsInSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfDiscontinuityTime.setStatus("current")


class _MplsOutSegmentIndexNext_Type(Unsigned32):
    """Custom type mplsOutSegmentIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsOutSegmentIndexNext_Type.__name__ = "Unsigned32"
_MplsOutSegmentIndexNext_Object = MibScalar
mplsOutSegmentIndexNext = _MplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 5),
    _MplsOutSegmentIndexNext_Type()
)
mplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentIndexNext.setStatus("current")
_MplsOutSegmentTable_Object = MibTable
mplsOutSegmentTable = _MplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6)
)
if mibBuilder.loadTexts:
    mplsOutSegmentTable.setStatus("current")
_MplsOutSegmentEntry_Object = MibTableRow
mplsOutSegmentEntry = _MplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1)
)
mplsOutSegmentEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsOutSegmentEntry.setStatus("current")


class _MplsOutSegmentIndex_Type(Unsigned32):
    """Custom type mplsOutSegmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOutSegmentIndex_Type.__name__ = "Unsigned32"
_MplsOutSegmentIndex_Object = MibTableColumn
mplsOutSegmentIndex = _MplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 1),
    _MplsOutSegmentIndex_Type()
)
mplsOutSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOutSegmentIndex.setStatus("current")


class _MplsOutSegmentIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mplsOutSegmentIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MplsOutSegmentIfIndex_Object = MibTableColumn
mplsOutSegmentIfIndex = _MplsOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 2),
    _MplsOutSegmentIfIndex_Type()
)
mplsOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentIfIndex.setStatus("current")
_MplsOutSegmentPushTopLabel_Type = TruthValue
_MplsOutSegmentPushTopLabel_Object = MibTableColumn
mplsOutSegmentPushTopLabel = _MplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 3),
    _MplsOutSegmentPushTopLabel_Type()
)
mplsOutSegmentPushTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentPushTopLabel.setStatus("current")


class _MplsOutSegmentTopLabel_Type(MplsLabel):
    """Custom type mplsOutSegmentTopLabel based on MplsLabel"""
    defaultValue = 0


_MplsOutSegmentTopLabel_Object = MibTableColumn
mplsOutSegmentTopLabel = _MplsOutSegmentTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 4),
    _MplsOutSegmentTopLabel_Type()
)
mplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTopLabel.setStatus("current")


class _MplsOutSegmentNextHopIpAddrType_Type(InetAddressType):
    """Custom type mplsOutSegmentNextHopIpAddrType based on InetAddressType"""


_MplsOutSegmentNextHopIpAddrType_Object = MibTableColumn
mplsOutSegmentNextHopIpAddrType = _MplsOutSegmentNextHopIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 5),
    _MplsOutSegmentNextHopIpAddrType_Type()
)
mplsOutSegmentNextHopIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpAddrType.setStatus("current")
_MplsOutSegmentNextHopIpv4Addr_Type = InetAddressIPv4
_MplsOutSegmentNextHopIpv4Addr_Object = MibTableColumn
mplsOutSegmentNextHopIpv4Addr = _MplsOutSegmentNextHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 6),
    _MplsOutSegmentNextHopIpv4Addr_Type()
)
mplsOutSegmentNextHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpv4Addr.setStatus("current")
_MplsOutSegmentNextHopIpv6Addr_Type = InetAddressIPv6
_MplsOutSegmentNextHopIpv6Addr_Object = MibTableColumn
mplsOutSegmentNextHopIpv6Addr = _MplsOutSegmentNextHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 7),
    _MplsOutSegmentNextHopIpv6Addr_Type()
)
mplsOutSegmentNextHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopIpv6Addr.setStatus("current")


class _MplsOutSegmentXCIndex_Type(Unsigned32):
    """Custom type mplsOutSegmentXCIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsOutSegmentXCIndex_Type.__name__ = "Unsigned32"
_MplsOutSegmentXCIndex_Object = MibTableColumn
mplsOutSegmentXCIndex = _MplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 8),
    _MplsOutSegmentXCIndex_Type()
)
mplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentXCIndex.setStatus("current")


class _MplsOutSegmentOwner_Type(MplsInitialCreationSource):
    """Custom type mplsOutSegmentOwner based on MplsInitialCreationSource"""


_MplsOutSegmentOwner_Object = MibTableColumn
mplsOutSegmentOwner = _MplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 9),
    _MplsOutSegmentOwner_Type()
)
mplsOutSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentOwner.setStatus("current")
_MplsOutSegmentTrafficParamPtr_Type = RowPointer
_MplsOutSegmentTrafficParamPtr_Object = MibTableColumn
mplsOutSegmentTrafficParamPtr = _MplsOutSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 10),
    _MplsOutSegmentTrafficParamPtr_Type()
)
mplsOutSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTrafficParamPtr.setStatus("current")
_MplsOutSegmentRowStatus_Type = RowStatus
_MplsOutSegmentRowStatus_Object = MibTableColumn
mplsOutSegmentRowStatus = _MplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 11),
    _MplsOutSegmentRowStatus_Type()
)
mplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentRowStatus.setStatus("current")
_MplsOutSegmentStorageType_Type = StorageType
_MplsOutSegmentStorageType_Object = MibTableColumn
mplsOutSegmentStorageType = _MplsOutSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 6, 1, 12),
    _MplsOutSegmentStorageType_Type()
)
mplsOutSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentStorageType.setStatus("current")
_MplsOutSegmentPerfTable_Object = MibTable
mplsOutSegmentPerfTable = _MplsOutSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfTable.setStatus("current")
_MplsOutSegmentPerfEntry_Object = MibTableRow
mplsOutSegmentPerfEntry = _MplsOutSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfEntry.setStatus("current")
_MplsOutSegmentOctets_Type = Counter32
_MplsOutSegmentOctets_Object = MibTableColumn
mplsOutSegmentOctets = _MplsOutSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 1),
    _MplsOutSegmentOctets_Type()
)
mplsOutSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentOctets.setStatus("current")
_MplsOutSegmentPackets_Type = Counter32
_MplsOutSegmentPackets_Object = MibTableColumn
mplsOutSegmentPackets = _MplsOutSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 2),
    _MplsOutSegmentPackets_Type()
)
mplsOutSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPackets.setStatus("current")
_MplsOutSegmentErrors_Type = Counter32
_MplsOutSegmentErrors_Object = MibTableColumn
mplsOutSegmentErrors = _MplsOutSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 3),
    _MplsOutSegmentErrors_Type()
)
mplsOutSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentErrors.setStatus("current")
_MplsOutSegmentDiscards_Type = Counter32
_MplsOutSegmentDiscards_Object = MibTableColumn
mplsOutSegmentDiscards = _MplsOutSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 4),
    _MplsOutSegmentDiscards_Type()
)
mplsOutSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentDiscards.setStatus("current")
_MplsOutSegmentHCOctets_Type = Counter64
_MplsOutSegmentHCOctets_Object = MibTableColumn
mplsOutSegmentHCOctets = _MplsOutSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 5),
    _MplsOutSegmentHCOctets_Type()
)
mplsOutSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentHCOctets.setStatus("current")
_MplsOutSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsOutSegmentPerfDiscontinuityTime = _MplsOutSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 7, 1, 6),
    _MplsOutSegmentPerfDiscontinuityTime_Type()
)
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfDiscontinuityTime.setStatus("current")


class _MplsXCIndexNext_Type(Unsigned32):
    """Custom type mplsXCIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsXCIndexNext_Type.__name__ = "Unsigned32"
_MplsXCIndexNext_Object = MibScalar
mplsXCIndexNext = _MplsXCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 8),
    _MplsXCIndexNext_Type()
)
mplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCIndexNext.setStatus("current")
_MplsXCTable_Object = MibTable
mplsXCTable = _MplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9)
)
if mibBuilder.loadTexts:
    mplsXCTable.setStatus("current")
_MplsXCEntry_Object = MibTableRow
mplsXCEntry = _MplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1)
)
mplsXCEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsXCIndex"),
    (0, "HP-SN-MPLS-LSR-MIB", "mplsInSegmentIfIndex"),
    (0, "HP-SN-MPLS-LSR-MIB", "mplsInSegmentLabel"),
    (0, "HP-SN-MPLS-LSR-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsXCEntry.setStatus("current")


class _MplsXCIndex_Type(Unsigned32):
    """Custom type mplsXCIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsXCIndex_Type.__name__ = "Unsigned32"
_MplsXCIndex_Object = MibTableColumn
mplsXCIndex = _MplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 1),
    _MplsXCIndex_Type()
)
mplsXCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsXCIndex.setStatus("current")
_MplsXCLspId_Type = MplsLSPID
_MplsXCLspId_Object = MibTableColumn
mplsXCLspId = _MplsXCLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 2),
    _MplsXCLspId_Type()
)
mplsXCLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLspId.setStatus("current")


class _MplsXCLabelStackIndex_Type(Unsigned32):
    """Custom type mplsXCLabelStackIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsXCLabelStackIndex_Type.__name__ = "Unsigned32"
_MplsXCLabelStackIndex_Object = MibTableColumn
mplsXCLabelStackIndex = _MplsXCLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 3),
    _MplsXCLabelStackIndex_Type()
)
mplsXCLabelStackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLabelStackIndex.setStatus("current")


class _MplsXCIsPersistent_Type(TruthValue):
    """Custom type mplsXCIsPersistent based on TruthValue"""


_MplsXCIsPersistent_Object = MibTableColumn
mplsXCIsPersistent = _MplsXCIsPersistent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 4),
    _MplsXCIsPersistent_Type()
)
mplsXCIsPersistent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCIsPersistent.setStatus("current")
_MplsXCOwner_Type = MplsInitialCreationSource
_MplsXCOwner_Object = MibTableColumn
mplsXCOwner = _MplsXCOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 5),
    _MplsXCOwner_Type()
)
mplsXCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCOwner.setStatus("current")
_MplsXCRowStatus_Type = RowStatus
_MplsXCRowStatus_Object = MibTableColumn
mplsXCRowStatus = _MplsXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 6),
    _MplsXCRowStatus_Type()
)
mplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCRowStatus.setStatus("current")
_MplsXCStorageType_Type = StorageType
_MplsXCStorageType_Object = MibTableColumn
mplsXCStorageType = _MplsXCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 7),
    _MplsXCStorageType_Type()
)
mplsXCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCStorageType.setStatus("current")


class _MplsXCAdminStatus_Type(Integer32):
    """Custom type mplsXCAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MplsXCAdminStatus_Type.__name__ = "Integer32"
_MplsXCAdminStatus_Object = MibTableColumn
mplsXCAdminStatus = _MplsXCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 8),
    _MplsXCAdminStatus_Type()
)
mplsXCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCAdminStatus.setStatus("current")


class _MplsXCOperStatus_Type(Integer32):
    """Custom type mplsXCOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_MplsXCOperStatus_Type.__name__ = "Integer32"
_MplsXCOperStatus_Object = MibTableColumn
mplsXCOperStatus = _MplsXCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 9, 1, 9),
    _MplsXCOperStatus_Type()
)
mplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCOperStatus.setStatus("current")


class _MplsMaxLabelStackDepth_Type(Integer32):
    """Custom type mplsMaxLabelStackDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsMaxLabelStackDepth_Type.__name__ = "Integer32"
_MplsMaxLabelStackDepth_Object = MibScalar
mplsMaxLabelStackDepth = _MplsMaxLabelStackDepth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 10),
    _MplsMaxLabelStackDepth_Type()
)
mplsMaxLabelStackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMaxLabelStackDepth.setStatus("current")


class _MplsLabelStackIndexNext_Type(Unsigned32):
    """Custom type mplsLabelStackIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLabelStackIndexNext_Type.__name__ = "Unsigned32"
_MplsLabelStackIndexNext_Object = MibScalar
mplsLabelStackIndexNext = _MplsLabelStackIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 11),
    _MplsLabelStackIndexNext_Type()
)
mplsLabelStackIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLabelStackIndexNext.setStatus("current")
_MplsLabelStackTable_Object = MibTable
mplsLabelStackTable = _MplsLabelStackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12)
)
if mibBuilder.loadTexts:
    mplsLabelStackTable.setStatus("current")
_MplsLabelStackEntry_Object = MibTableRow
mplsLabelStackEntry = _MplsLabelStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1)
)
mplsLabelStackEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsLabelStackIndex"),
    (0, "HP-SN-MPLS-LSR-MIB", "mplsLabelStackLabelIndex"),
)
if mibBuilder.loadTexts:
    mplsLabelStackEntry.setStatus("current")


class _MplsLabelStackIndex_Type(Unsigned32):
    """Custom type mplsLabelStackIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLabelStackIndex_Type.__name__ = "Unsigned32"
_MplsLabelStackIndex_Object = MibTableColumn
mplsLabelStackIndex = _MplsLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1, 1),
    _MplsLabelStackIndex_Type()
)
mplsLabelStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLabelStackIndex.setStatus("current")


class _MplsLabelStackLabelIndex_Type(Unsigned32):
    """Custom type mplsLabelStackLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLabelStackLabelIndex_Type.__name__ = "Unsigned32"
_MplsLabelStackLabelIndex_Object = MibTableColumn
mplsLabelStackLabelIndex = _MplsLabelStackLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1, 2),
    _MplsLabelStackLabelIndex_Type()
)
mplsLabelStackLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLabelStackLabelIndex.setStatus("current")
_MplsLabelStackLabel_Type = MplsLabel
_MplsLabelStackLabel_Object = MibTableColumn
mplsLabelStackLabel = _MplsLabelStackLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1, 3),
    _MplsLabelStackLabel_Type()
)
mplsLabelStackLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackLabel.setStatus("current")
_MplsLabelStackRowStatus_Type = RowStatus
_MplsLabelStackRowStatus_Object = MibTableColumn
mplsLabelStackRowStatus = _MplsLabelStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1, 4),
    _MplsLabelStackRowStatus_Type()
)
mplsLabelStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackRowStatus.setStatus("current")
_MplsLabelStackStorageType_Type = StorageType
_MplsLabelStackStorageType_Object = MibTableColumn
mplsLabelStackStorageType = _MplsLabelStackStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 12, 1, 5),
    _MplsLabelStackStorageType_Type()
)
mplsLabelStackStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackStorageType.setStatus("current")


class _MplsTrafficParamIndexNext_Type(Unsigned32):
    """Custom type mplsTrafficParamIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTrafficParamIndexNext_Type.__name__ = "Unsigned32"
_MplsTrafficParamIndexNext_Object = MibScalar
mplsTrafficParamIndexNext = _MplsTrafficParamIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 13),
    _MplsTrafficParamIndexNext_Type()
)
mplsTrafficParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrafficParamIndexNext.setStatus("current")
_MplsTrafficParamTable_Object = MibTable
mplsTrafficParamTable = _MplsTrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14)
)
if mibBuilder.loadTexts:
    mplsTrafficParamTable.setStatus("current")
_MplsTrafficParamEntry_Object = MibTableRow
mplsTrafficParamEntry = _MplsTrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1)
)
mplsTrafficParamEntry.setIndexNames(
    (0, "HP-SN-MPLS-LSR-MIB", "mplsTrafficParamIndex"),
)
if mibBuilder.loadTexts:
    mplsTrafficParamEntry.setStatus("current")


class _MplsTrafficParamIndex_Type(Unsigned32):
    """Custom type mplsTrafficParamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTrafficParamIndex_Type.__name__ = "Unsigned32"
_MplsTrafficParamIndex_Object = MibTableColumn
mplsTrafficParamIndex = _MplsTrafficParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 1),
    _MplsTrafficParamIndex_Type()
)
mplsTrafficParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTrafficParamIndex.setStatus("current")
_MplsTrafficParamMaxRate_Type = MplsBitRate
_MplsTrafficParamMaxRate_Object = MibTableColumn
mplsTrafficParamMaxRate = _MplsTrafficParamMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 2),
    _MplsTrafficParamMaxRate_Type()
)
mplsTrafficParamMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxRate.setUnits("kilobits per second")
_MplsTrafficParamMeanRate_Type = MplsBitRate
_MplsTrafficParamMeanRate_Object = MibTableColumn
mplsTrafficParamMeanRate = _MplsTrafficParamMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 3),
    _MplsTrafficParamMeanRate_Type()
)
mplsTrafficParamMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMeanRate.setUnits("kilobits per second")
_MplsTrafficParamMaxBurstSize_Type = MplsBurstSize
_MplsTrafficParamMaxBurstSize_Object = MibTableColumn
mplsTrafficParamMaxBurstSize = _MplsTrafficParamMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 4),
    _MplsTrafficParamMaxBurstSize_Type()
)
mplsTrafficParamMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrafficParamMaxBurstSize.setUnits("bytes")
_MplsTrafficParamRowStatus_Type = RowStatus
_MplsTrafficParamRowStatus_Object = MibTableColumn
mplsTrafficParamRowStatus = _MplsTrafficParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 5),
    _MplsTrafficParamRowStatus_Type()
)
mplsTrafficParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamRowStatus.setStatus("current")
_MplsTrafficParamStorageType_Type = StorageType
_MplsTrafficParamStorageType_Object = MibTableColumn
mplsTrafficParamStorageType = _MplsTrafficParamStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 14, 1, 6),
    _MplsTrafficParamStorageType_Type()
)
mplsTrafficParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTrafficParamStorageType.setStatus("current")


class _MplsXCTrapEnable_Type(TruthValue):
    """Custom type mplsXCTrapEnable based on TruthValue"""


_MplsXCTrapEnable_Object = MibScalar
mplsXCTrapEnable = _MplsXCTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 1, 15),
    _MplsXCTrapEnable_Type()
)
mplsXCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsXCTrapEnable.setStatus("current")
_MplsLsrNotifications_ObjectIdentity = ObjectIdentity
mplsLsrNotifications = _MplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 2)
)
_MplsLsrNotifyPrefix_ObjectIdentity = ObjectIdentity
mplsLsrNotifyPrefix = _MplsLsrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 2, 0)
)
_MplsLsrConformance_ObjectIdentity = ObjectIdentity
mplsLsrConformance = _MplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3)
)
_MplsLsrGroups_ObjectIdentity = ObjectIdentity
mplsLsrGroups = _MplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1)
)
_MplsLsrCompliances_ObjectIdentity = ObjectIdentity
mplsLsrCompliances = _MplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 2)
)
mplsInterfaceConfEntry.registerAugmentions(
    ("HP-SN-MPLS-LSR-MIB",
     "mplsInterfacePerfEntry")
)
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions(
    ("HP-SN-MPLS-LSR-MIB",
     "mplsInSegmentPerfEntry")
)
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("HP-SN-MPLS-LSR-MIB",
     "mplsOutSegmentPerfEntry")
)
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())

# Managed Objects groups

mplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 1)
)
mplsInterfaceGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsInterfaceLabelMinIn"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceLabelMaxIn"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceLabelMinOut"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceLabelMaxOut"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceTotalBandwidth"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceAvailableBandwidth"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceLabelParticipationType"))
)
if mibBuilder.loadTexts:
    mplsInterfaceGroup.setStatus("current")

mplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 2)
)
mplsInSegmentGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsInSegmentNPop"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentAddrFamily"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentXCIndex"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentOctets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentDiscards"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentOwner"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentRowStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentStorageType"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    mplsInSegmentGroup.setStatus("current")

mplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 3)
)
mplsOutSegmentGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentIndexNext"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentIfIndex"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentPushTopLabel"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentTopLabel"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentNextHopIpAddrType"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv4Addr"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv6Addr"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentXCIndex"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentOwner"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentOctets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentDiscards"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentErrors"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentRowStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentStorageType"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    mplsOutSegmentGroup.setStatus("current")

mplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 4)
)
mplsXCGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsXCIndexNext"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCLabelStackIndex"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCOwner"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCAdminStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCOperStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCRowStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCTrapEnable"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCStorageType"))
)
if mibBuilder.loadTexts:
    mplsXCGroup.setStatus("current")

mplsXCOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 5)
)
mplsXCOptionalGroup.setObjects(
    ("HP-SN-MPLS-LSR-MIB", "mplsXCLspId")
)
if mibBuilder.loadTexts:
    mplsXCOptionalGroup.setStatus("current")

mplsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 6)
)
mplsPerfGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsInSegmentOctets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentPackets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentErrors"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentDiscards"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentOctets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentPackets"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentDiscards"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceInLabelsUsed"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceFailedLabelLookup"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceOutFragments"),
        ("HP-SN-MPLS-LSR-MIB", "mplsInterfaceOutLabelsUsed"))
)
if mibBuilder.loadTexts:
    mplsPerfGroup.setStatus("current")

mplsHCInSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 7)
)
mplsHCInSegmentPerfGroup.setObjects(
    ("HP-SN-MPLS-LSR-MIB", "mplsInSegmentHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCInSegmentPerfGroup.setStatus("current")

mplsHCOutSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 8)
)
mplsHCOutSegmentPerfGroup.setObjects(
    ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCOutSegmentPerfGroup.setStatus("current")

mplsTrafficParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 9)
)
mplsTrafficParamGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamIndexNext"),
        ("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamMaxRate"),
        ("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamMeanRate"),
        ("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamMaxBurstSize"),
        ("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamRowStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsTrafficParamStorageType"))
)
if mibBuilder.loadTexts:
    mplsTrafficParamGroup.setStatus("current")

mplsXCIsPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 10)
)
mplsXCIsPersistentGroup.setObjects(
    ("HP-SN-MPLS-LSR-MIB", "mplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    mplsXCIsPersistentGroup.setStatus("current")

mplsXCIsNotPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 11)
)
mplsXCIsNotPersistentGroup.setObjects(
    ("HP-SN-MPLS-LSR-MIB", "mplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    mplsXCIsNotPersistentGroup.setStatus("current")

mplsLabelStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 12)
)
mplsLabelStackGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsLabelStackLabel"),
        ("HP-SN-MPLS-LSR-MIB", "mplsLabelStackRowStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsLabelStackStorageType"),
        ("HP-SN-MPLS-LSR-MIB", "mplsMaxLabelStackDepth"),
        ("HP-SN-MPLS-LSR-MIB", "mplsLabelStackIndexNext"))
)
if mibBuilder.loadTexts:
    mplsLabelStackGroup.setStatus("current")

mplsSegmentDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 13)
)
mplsSegmentDiscontinuityGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsInSegmentPerfDiscontinuityTime"),
        ("HP-SN-MPLS-LSR-MIB", "mplsOutSegmentPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mplsSegmentDiscontinuityGroup.setStatus("current")


# Notification objects

mplsXCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 2, 0, 1)
)
mplsXCUp.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsXCOperStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCUp.setStatus(
        "current"
    )

mplsXCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 2, 0, 2)
)
mplsXCDown.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsXCOperStatus"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCDown.setStatus(
        "current"
    )


# Notifications groups

mplsLsrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 1, 14)
)
mplsLsrNotificationGroup.setObjects(
      *(("HP-SN-MPLS-LSR-MIB", "mplsXCUp"),
        ("HP-SN-MPLS-LSR-MIB", "mplsXCDown"))
)
if mibBuilder.loadTexts:
    mplsLsrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLsrModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLsrModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-MPLS-LSR-MIB",
    **{"mplsLsrMIB": mplsLsrMIB,
       "mplsLsrObjects": mplsLsrObjects,
       "mplsInterfaceConfTable": mplsInterfaceConfTable,
       "mplsInterfaceConfEntry": mplsInterfaceConfEntry,
       "mplsInterfaceConfIndex": mplsInterfaceConfIndex,
       "mplsInterfaceLabelMinIn": mplsInterfaceLabelMinIn,
       "mplsInterfaceLabelMaxIn": mplsInterfaceLabelMaxIn,
       "mplsInterfaceLabelMinOut": mplsInterfaceLabelMinOut,
       "mplsInterfaceLabelMaxOut": mplsInterfaceLabelMaxOut,
       "mplsInterfaceTotalBandwidth": mplsInterfaceTotalBandwidth,
       "mplsInterfaceAvailableBandwidth": mplsInterfaceAvailableBandwidth,
       "mplsInterfaceLabelParticipationType": mplsInterfaceLabelParticipationType,
       "mplsInterfacePerfTable": mplsInterfacePerfTable,
       "mplsInterfacePerfEntry": mplsInterfacePerfEntry,
       "mplsInterfaceInLabelsUsed": mplsInterfaceInLabelsUsed,
       "mplsInterfaceFailedLabelLookup": mplsInterfaceFailedLabelLookup,
       "mplsInterfaceOutLabelsUsed": mplsInterfaceOutLabelsUsed,
       "mplsInterfaceOutFragments": mplsInterfaceOutFragments,
       "mplsInSegmentTable": mplsInSegmentTable,
       "mplsInSegmentEntry": mplsInSegmentEntry,
       "mplsInSegmentIfIndex": mplsInSegmentIfIndex,
       "mplsInSegmentLabel": mplsInSegmentLabel,
       "mplsInSegmentNPop": mplsInSegmentNPop,
       "mplsInSegmentAddrFamily": mplsInSegmentAddrFamily,
       "mplsInSegmentXCIndex": mplsInSegmentXCIndex,
       "mplsInSegmentOwner": mplsInSegmentOwner,
       "mplsInSegmentTrafficParamPtr": mplsInSegmentTrafficParamPtr,
       "mplsInSegmentRowStatus": mplsInSegmentRowStatus,
       "mplsInSegmentStorageType": mplsInSegmentStorageType,
       "mplsInSegmentPerfTable": mplsInSegmentPerfTable,
       "mplsInSegmentPerfEntry": mplsInSegmentPerfEntry,
       "mplsInSegmentOctets": mplsInSegmentOctets,
       "mplsInSegmentPackets": mplsInSegmentPackets,
       "mplsInSegmentErrors": mplsInSegmentErrors,
       "mplsInSegmentDiscards": mplsInSegmentDiscards,
       "mplsInSegmentHCOctets": mplsInSegmentHCOctets,
       "mplsInSegmentPerfDiscontinuityTime": mplsInSegmentPerfDiscontinuityTime,
       "mplsOutSegmentIndexNext": mplsOutSegmentIndexNext,
       "mplsOutSegmentTable": mplsOutSegmentTable,
       "mplsOutSegmentEntry": mplsOutSegmentEntry,
       "mplsOutSegmentIndex": mplsOutSegmentIndex,
       "mplsOutSegmentIfIndex": mplsOutSegmentIfIndex,
       "mplsOutSegmentPushTopLabel": mplsOutSegmentPushTopLabel,
       "mplsOutSegmentTopLabel": mplsOutSegmentTopLabel,
       "mplsOutSegmentNextHopIpAddrType": mplsOutSegmentNextHopIpAddrType,
       "mplsOutSegmentNextHopIpv4Addr": mplsOutSegmentNextHopIpv4Addr,
       "mplsOutSegmentNextHopIpv6Addr": mplsOutSegmentNextHopIpv6Addr,
       "mplsOutSegmentXCIndex": mplsOutSegmentXCIndex,
       "mplsOutSegmentOwner": mplsOutSegmentOwner,
       "mplsOutSegmentTrafficParamPtr": mplsOutSegmentTrafficParamPtr,
       "mplsOutSegmentRowStatus": mplsOutSegmentRowStatus,
       "mplsOutSegmentStorageType": mplsOutSegmentStorageType,
       "mplsOutSegmentPerfTable": mplsOutSegmentPerfTable,
       "mplsOutSegmentPerfEntry": mplsOutSegmentPerfEntry,
       "mplsOutSegmentOctets": mplsOutSegmentOctets,
       "mplsOutSegmentPackets": mplsOutSegmentPackets,
       "mplsOutSegmentErrors": mplsOutSegmentErrors,
       "mplsOutSegmentDiscards": mplsOutSegmentDiscards,
       "mplsOutSegmentHCOctets": mplsOutSegmentHCOctets,
       "mplsOutSegmentPerfDiscontinuityTime": mplsOutSegmentPerfDiscontinuityTime,
       "mplsXCIndexNext": mplsXCIndexNext,
       "mplsXCTable": mplsXCTable,
       "mplsXCEntry": mplsXCEntry,
       "mplsXCIndex": mplsXCIndex,
       "mplsXCLspId": mplsXCLspId,
       "mplsXCLabelStackIndex": mplsXCLabelStackIndex,
       "mplsXCIsPersistent": mplsXCIsPersistent,
       "mplsXCOwner": mplsXCOwner,
       "mplsXCRowStatus": mplsXCRowStatus,
       "mplsXCStorageType": mplsXCStorageType,
       "mplsXCAdminStatus": mplsXCAdminStatus,
       "mplsXCOperStatus": mplsXCOperStatus,
       "mplsMaxLabelStackDepth": mplsMaxLabelStackDepth,
       "mplsLabelStackIndexNext": mplsLabelStackIndexNext,
       "mplsLabelStackTable": mplsLabelStackTable,
       "mplsLabelStackEntry": mplsLabelStackEntry,
       "mplsLabelStackIndex": mplsLabelStackIndex,
       "mplsLabelStackLabelIndex": mplsLabelStackLabelIndex,
       "mplsLabelStackLabel": mplsLabelStackLabel,
       "mplsLabelStackRowStatus": mplsLabelStackRowStatus,
       "mplsLabelStackStorageType": mplsLabelStackStorageType,
       "mplsTrafficParamIndexNext": mplsTrafficParamIndexNext,
       "mplsTrafficParamTable": mplsTrafficParamTable,
       "mplsTrafficParamEntry": mplsTrafficParamEntry,
       "mplsTrafficParamIndex": mplsTrafficParamIndex,
       "mplsTrafficParamMaxRate": mplsTrafficParamMaxRate,
       "mplsTrafficParamMeanRate": mplsTrafficParamMeanRate,
       "mplsTrafficParamMaxBurstSize": mplsTrafficParamMaxBurstSize,
       "mplsTrafficParamRowStatus": mplsTrafficParamRowStatus,
       "mplsTrafficParamStorageType": mplsTrafficParamStorageType,
       "mplsXCTrapEnable": mplsXCTrapEnable,
       "mplsLsrNotifications": mplsLsrNotifications,
       "mplsLsrNotifyPrefix": mplsLsrNotifyPrefix,
       "mplsXCUp": mplsXCUp,
       "mplsXCDown": mplsXCDown,
       "mplsLsrConformance": mplsLsrConformance,
       "mplsLsrGroups": mplsLsrGroups,
       "mplsInterfaceGroup": mplsInterfaceGroup,
       "mplsInSegmentGroup": mplsInSegmentGroup,
       "mplsOutSegmentGroup": mplsOutSegmentGroup,
       "mplsXCGroup": mplsXCGroup,
       "mplsXCOptionalGroup": mplsXCOptionalGroup,
       "mplsPerfGroup": mplsPerfGroup,
       "mplsHCInSegmentPerfGroup": mplsHCInSegmentPerfGroup,
       "mplsHCOutSegmentPerfGroup": mplsHCOutSegmentPerfGroup,
       "mplsTrafficParamGroup": mplsTrafficParamGroup,
       "mplsXCIsPersistentGroup": mplsXCIsPersistentGroup,
       "mplsXCIsNotPersistentGroup": mplsXCIsNotPersistentGroup,
       "mplsLabelStackGroup": mplsLabelStackGroup,
       "mplsSegmentDiscontinuityGroup": mplsSegmentDiscontinuityGroup,
       "mplsLsrNotificationGroup": mplsLsrNotificationGroup,
       "mplsLsrCompliances": mplsLsrCompliances,
       "mplsLsrModuleCompliance": mplsLsrModuleCompliance}
)
