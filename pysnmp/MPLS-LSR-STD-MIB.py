# SNMP MIB module (MPLS-LSR-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LSR-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:43 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsBitRate,
 MplsLSPID,
 MplsLabel,
 MplsOwner,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "MplsLSPID",
    "MplsLabel",
    "MplsOwner",
    "mplsStdMIB")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

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

mplsLsrStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2)
)
mplsLsrStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsIndexType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )



class MplsIndexNextType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )



# MIB Managed Objects in the order of their OIDs

_MplsLsrNotifications_ObjectIdentity = ObjectIdentity
mplsLsrNotifications = _MplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 0)
)
_MplsLsrObjects_ObjectIdentity = ObjectIdentity
mplsLsrObjects = _MplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1)
)
_MplsInterfaceTable_Object = MibTable
mplsInterfaceTable = _MplsInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsInterfaceTable.setStatus("current")
_MplsInterfaceEntry_Object = MibTableRow
mplsInterfaceEntry = _MplsInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1)
)
mplsInterfaceEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mplsInterfaceEntry.setStatus("current")
_MplsInterfaceIndex_Type = InterfaceIndexOrZero
_MplsInterfaceIndex_Object = MibTableColumn
mplsInterfaceIndex = _MplsInterfaceIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 1),
    _MplsInterfaceIndex_Type()
)
mplsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInterfaceIndex.setStatus("current")
_MplsInterfaceLabelMinIn_Type = MplsLabel
_MplsInterfaceLabelMinIn_Object = MibTableColumn
mplsInterfaceLabelMinIn = _MplsInterfaceLabelMinIn_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 2),
    _MplsInterfaceLabelMinIn_Type()
)
mplsInterfaceLabelMinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinIn.setStatus("current")
_MplsInterfaceLabelMaxIn_Type = MplsLabel
_MplsInterfaceLabelMaxIn_Object = MibTableColumn
mplsInterfaceLabelMaxIn = _MplsInterfaceLabelMaxIn_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 3),
    _MplsInterfaceLabelMaxIn_Type()
)
mplsInterfaceLabelMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxIn.setStatus("current")
_MplsInterfaceLabelMinOut_Type = MplsLabel
_MplsInterfaceLabelMinOut_Object = MibTableColumn
mplsInterfaceLabelMinOut = _MplsInterfaceLabelMinOut_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 4),
    _MplsInterfaceLabelMinOut_Type()
)
mplsInterfaceLabelMinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMinOut.setStatus("current")
_MplsInterfaceLabelMaxOut_Type = MplsLabel
_MplsInterfaceLabelMaxOut_Object = MibTableColumn
mplsInterfaceLabelMaxOut = _MplsInterfaceLabelMaxOut_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 5),
    _MplsInterfaceLabelMaxOut_Type()
)
mplsInterfaceLabelMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelMaxOut.setStatus("current")
_MplsInterfaceTotalBandwidth_Type = MplsBitRate
_MplsInterfaceTotalBandwidth_Object = MibTableColumn
mplsInterfaceTotalBandwidth = _MplsInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 6),
    _MplsInterfaceTotalBandwidth_Type()
)
mplsInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mplsInterfaceTotalBandwidth.setUnits("kilobits per second")
_MplsInterfaceAvailableBandwidth_Type = MplsBitRate
_MplsInterfaceAvailableBandwidth_Object = MibTableColumn
mplsInterfaceAvailableBandwidth = _MplsInterfaceAvailableBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 8),
    _MplsInterfaceLabelParticipationType_Type()
)
mplsInterfaceLabelParticipationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfaceLabelParticipationType.setStatus("current")
_MplsInterfacePerfTable_Object = MibTable
mplsInterfacePerfTable = _MplsInterfacePerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfTable.setStatus("current")
_MplsInterfacePerfEntry_Object = MibTableRow
mplsInterfacePerfEntry = _MplsInterfacePerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsInterfacePerfEntry.setStatus("current")
_MplsInterfacePerfInLabelsInUse_Type = Gauge32
_MplsInterfacePerfInLabelsInUse_Object = MibTableColumn
mplsInterfacePerfInLabelsInUse = _MplsInterfacePerfInLabelsInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 1),
    _MplsInterfacePerfInLabelsInUse_Type()
)
mplsInterfacePerfInLabelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfacePerfInLabelsInUse.setStatus("current")
_MplsInterfacePerfInLabelLookupFailures_Type = Counter32
_MplsInterfacePerfInLabelLookupFailures_Object = MibTableColumn
mplsInterfacePerfInLabelLookupFailures = _MplsInterfacePerfInLabelLookupFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 2),
    _MplsInterfacePerfInLabelLookupFailures_Type()
)
mplsInterfacePerfInLabelLookupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfacePerfInLabelLookupFailures.setStatus("current")
_MplsInterfacePerfOutLabelsInUse_Type = Gauge32
_MplsInterfacePerfOutLabelsInUse_Object = MibTableColumn
mplsInterfacePerfOutLabelsInUse = _MplsInterfacePerfOutLabelsInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 3),
    _MplsInterfacePerfOutLabelsInUse_Type()
)
mplsInterfacePerfOutLabelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfacePerfOutLabelsInUse.setStatus("current")
_MplsInterfacePerfOutFragmentedPkts_Type = Counter32
_MplsInterfacePerfOutFragmentedPkts_Object = MibTableColumn
mplsInterfacePerfOutFragmentedPkts = _MplsInterfacePerfOutFragmentedPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 4),
    _MplsInterfacePerfOutFragmentedPkts_Type()
)
mplsInterfacePerfOutFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInterfacePerfOutFragmentedPkts.setStatus("current")
_MplsInSegmentIndexNext_Type = MplsIndexNextType
_MplsInSegmentIndexNext_Object = MibScalar
mplsInSegmentIndexNext = _MplsInSegmentIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 3),
    _MplsInSegmentIndexNext_Type()
)
mplsInSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentIndexNext.setStatus("current")
_MplsInSegmentTable_Object = MibTable
mplsInSegmentTable = _MplsInSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mplsInSegmentTable.setStatus("current")
_MplsInSegmentEntry_Object = MibTableRow
mplsInSegmentEntry = _MplsInSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1)
)
mplsInSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsInSegmentEntry.setStatus("current")
_MplsInSegmentIndex_Type = MplsIndexType
_MplsInSegmentIndex_Object = MibTableColumn
mplsInSegmentIndex = _MplsInSegmentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 1),
    _MplsInSegmentIndex_Type()
)
mplsInSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentIndex.setStatus("current")
_MplsInSegmentInterface_Type = InterfaceIndexOrZero
_MplsInSegmentInterface_Object = MibTableColumn
mplsInSegmentInterface = _MplsInSegmentInterface_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 2),
    _MplsInSegmentInterface_Type()
)
mplsInSegmentInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentInterface.setStatus("current")
_MplsInSegmentLabel_Type = MplsLabel
_MplsInSegmentLabel_Object = MibTableColumn
mplsInSegmentLabel = _MplsInSegmentLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 3),
    _MplsInSegmentLabel_Type()
)
mplsInSegmentLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentLabel.setStatus("current")


class _MplsInSegmentLabelPtr_Type(RowPointer):
    """Custom type mplsInSegmentLabelPtr based on RowPointer"""
    defaultValue = (0, 0)


_MplsInSegmentLabelPtr_Object = MibTableColumn
mplsInSegmentLabelPtr = _MplsInSegmentLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 4),
    _MplsInSegmentLabelPtr_Type()
)
mplsInSegmentLabelPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentLabelPtr.setStatus("current")


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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 5),
    _MplsInSegmentNPop_Type()
)
mplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentNPop.setStatus("current")


class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):
    """Custom type mplsInSegmentAddrFamily based on AddressFamilyNumbers"""


_MplsInSegmentAddrFamily_Object = MibTableColumn
mplsInSegmentAddrFamily = _MplsInSegmentAddrFamily_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 6),
    _MplsInSegmentAddrFamily_Type()
)
mplsInSegmentAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentAddrFamily.setStatus("current")
_MplsInSegmentXCIndex_Type = MplsIndexType
_MplsInSegmentXCIndex_Object = MibTableColumn
mplsInSegmentXCIndex = _MplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 7),
    _MplsInSegmentXCIndex_Type()
)
mplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentXCIndex.setStatus("current")
_MplsInSegmentOwner_Type = MplsOwner
_MplsInSegmentOwner_Object = MibTableColumn
mplsInSegmentOwner = _MplsInSegmentOwner_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 8),
    _MplsInSegmentOwner_Type()
)
mplsInSegmentOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentOwner.setStatus("current")


class _MplsInSegmentTrafficParamPtr_Type(RowPointer):
    """Custom type mplsInSegmentTrafficParamPtr based on RowPointer"""
    defaultValue = (0, 0)


_MplsInSegmentTrafficParamPtr_Object = MibTableColumn
mplsInSegmentTrafficParamPtr = _MplsInSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 9),
    _MplsInSegmentTrafficParamPtr_Type()
)
mplsInSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentTrafficParamPtr.setStatus("current")
_MplsInSegmentRowStatus_Type = RowStatus
_MplsInSegmentRowStatus_Object = MibTableColumn
mplsInSegmentRowStatus = _MplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 10),
    _MplsInSegmentRowStatus_Type()
)
mplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentRowStatus.setStatus("current")


class _MplsInSegmentStorageType_Type(StorageType):
    """Custom type mplsInSegmentStorageType based on StorageType"""


_MplsInSegmentStorageType_Object = MibTableColumn
mplsInSegmentStorageType = _MplsInSegmentStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 11),
    _MplsInSegmentStorageType_Type()
)
mplsInSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsInSegmentStorageType.setStatus("current")
_MplsInSegmentPerfTable_Object = MibTable
mplsInSegmentPerfTable = _MplsInSegmentPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfTable.setStatus("current")
_MplsInSegmentPerfEntry_Object = MibTableRow
mplsInSegmentPerfEntry = _MplsInSegmentPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mplsInSegmentPerfEntry.setStatus("current")
_MplsInSegmentPerfOctets_Type = Counter32
_MplsInSegmentPerfOctets_Object = MibTableColumn
mplsInSegmentPerfOctets = _MplsInSegmentPerfOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 1),
    _MplsInSegmentPerfOctets_Type()
)
mplsInSegmentPerfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfOctets.setStatus("current")
_MplsInSegmentPerfPackets_Type = Counter32
_MplsInSegmentPerfPackets_Object = MibTableColumn
mplsInSegmentPerfPackets = _MplsInSegmentPerfPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 2),
    _MplsInSegmentPerfPackets_Type()
)
mplsInSegmentPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfPackets.setStatus("current")
_MplsInSegmentPerfErrors_Type = Counter32
_MplsInSegmentPerfErrors_Object = MibTableColumn
mplsInSegmentPerfErrors = _MplsInSegmentPerfErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 3),
    _MplsInSegmentPerfErrors_Type()
)
mplsInSegmentPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfErrors.setStatus("current")
_MplsInSegmentPerfDiscards_Type = Counter32
_MplsInSegmentPerfDiscards_Object = MibTableColumn
mplsInSegmentPerfDiscards = _MplsInSegmentPerfDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 4),
    _MplsInSegmentPerfDiscards_Type()
)
mplsInSegmentPerfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfDiscards.setStatus("current")
_MplsInSegmentPerfHCOctets_Type = Counter64
_MplsInSegmentPerfHCOctets_Object = MibTableColumn
mplsInSegmentPerfHCOctets = _MplsInSegmentPerfHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 5),
    _MplsInSegmentPerfHCOctets_Type()
)
mplsInSegmentPerfHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfHCOctets.setStatus("current")
_MplsInSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsInSegmentPerfDiscontinuityTime = _MplsInSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 6),
    _MplsInSegmentPerfDiscontinuityTime_Type()
)
mplsInSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentPerfDiscontinuityTime.setStatus("current")
_MplsOutSegmentIndexNext_Type = MplsIndexNextType
_MplsOutSegmentIndexNext_Object = MibScalar
mplsOutSegmentIndexNext = _MplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 6),
    _MplsOutSegmentIndexNext_Type()
)
mplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentIndexNext.setStatus("current")
_MplsOutSegmentTable_Object = MibTable
mplsOutSegmentTable = _MplsOutSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7)
)
if mibBuilder.loadTexts:
    mplsOutSegmentTable.setStatus("current")
_MplsOutSegmentEntry_Object = MibTableRow
mplsOutSegmentEntry = _MplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1)
)
mplsOutSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsOutSegmentEntry.setStatus("current")
_MplsOutSegmentIndex_Type = MplsIndexType
_MplsOutSegmentIndex_Object = MibTableColumn
mplsOutSegmentIndex = _MplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 1),
    _MplsOutSegmentIndex_Type()
)
mplsOutSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOutSegmentIndex.setStatus("current")
_MplsOutSegmentInterface_Type = InterfaceIndexOrZero
_MplsOutSegmentInterface_Object = MibTableColumn
mplsOutSegmentInterface = _MplsOutSegmentInterface_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 2),
    _MplsOutSegmentInterface_Type()
)
mplsOutSegmentInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentInterface.setStatus("current")


class _MplsOutSegmentPushTopLabel_Type(TruthValue):
    """Custom type mplsOutSegmentPushTopLabel based on TruthValue"""


_MplsOutSegmentPushTopLabel_Object = MibTableColumn
mplsOutSegmentPushTopLabel = _MplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 3),
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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 4),
    _MplsOutSegmentTopLabel_Type()
)
mplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTopLabel.setStatus("current")


class _MplsOutSegmentTopLabelPtr_Type(RowPointer):
    """Custom type mplsOutSegmentTopLabelPtr based on RowPointer"""
    defaultValue = (0, 0)


_MplsOutSegmentTopLabelPtr_Object = MibTableColumn
mplsOutSegmentTopLabelPtr = _MplsOutSegmentTopLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 5),
    _MplsOutSegmentTopLabelPtr_Type()
)
mplsOutSegmentTopLabelPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTopLabelPtr.setStatus("current")
_MplsOutSegmentNextHopAddrType_Type = InetAddressType
_MplsOutSegmentNextHopAddrType_Object = MibTableColumn
mplsOutSegmentNextHopAddrType = _MplsOutSegmentNextHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 6),
    _MplsOutSegmentNextHopAddrType_Type()
)
mplsOutSegmentNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopAddrType.setStatus("current")
_MplsOutSegmentNextHopAddr_Type = InetAddress
_MplsOutSegmentNextHopAddr_Object = MibTableColumn
mplsOutSegmentNextHopAddr = _MplsOutSegmentNextHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 7),
    _MplsOutSegmentNextHopAddr_Type()
)
mplsOutSegmentNextHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentNextHopAddr.setStatus("current")
_MplsOutSegmentXCIndex_Type = MplsIndexType
_MplsOutSegmentXCIndex_Object = MibTableColumn
mplsOutSegmentXCIndex = _MplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 8),
    _MplsOutSegmentXCIndex_Type()
)
mplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentXCIndex.setStatus("current")
_MplsOutSegmentOwner_Type = MplsOwner
_MplsOutSegmentOwner_Object = MibTableColumn
mplsOutSegmentOwner = _MplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 9),
    _MplsOutSegmentOwner_Type()
)
mplsOutSegmentOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentOwner.setStatus("current")


class _MplsOutSegmentTrafficParamPtr_Type(RowPointer):
    """Custom type mplsOutSegmentTrafficParamPtr based on RowPointer"""
    defaultValue = (0, 0)


_MplsOutSegmentTrafficParamPtr_Object = MibTableColumn
mplsOutSegmentTrafficParamPtr = _MplsOutSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 10),
    _MplsOutSegmentTrafficParamPtr_Type()
)
mplsOutSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentTrafficParamPtr.setStatus("current")
_MplsOutSegmentRowStatus_Type = RowStatus
_MplsOutSegmentRowStatus_Object = MibTableColumn
mplsOutSegmentRowStatus = _MplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 11),
    _MplsOutSegmentRowStatus_Type()
)
mplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentRowStatus.setStatus("current")


class _MplsOutSegmentStorageType_Type(StorageType):
    """Custom type mplsOutSegmentStorageType based on StorageType"""


_MplsOutSegmentStorageType_Object = MibTableColumn
mplsOutSegmentStorageType = _MplsOutSegmentStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 12),
    _MplsOutSegmentStorageType_Type()
)
mplsOutSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOutSegmentStorageType.setStatus("current")
_MplsOutSegmentPerfTable_Object = MibTable
mplsOutSegmentPerfTable = _MplsOutSegmentPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfTable.setStatus("current")
_MplsOutSegmentPerfEntry_Object = MibTableRow
mplsOutSegmentPerfEntry = _MplsOutSegmentPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mplsOutSegmentPerfEntry.setStatus("current")
_MplsOutSegmentPerfOctets_Type = Counter32
_MplsOutSegmentPerfOctets_Object = MibTableColumn
mplsOutSegmentPerfOctets = _MplsOutSegmentPerfOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 1),
    _MplsOutSegmentPerfOctets_Type()
)
mplsOutSegmentPerfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfOctets.setStatus("current")
_MplsOutSegmentPerfPackets_Type = Counter32
_MplsOutSegmentPerfPackets_Object = MibTableColumn
mplsOutSegmentPerfPackets = _MplsOutSegmentPerfPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 2),
    _MplsOutSegmentPerfPackets_Type()
)
mplsOutSegmentPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfPackets.setStatus("current")
_MplsOutSegmentPerfErrors_Type = Counter32
_MplsOutSegmentPerfErrors_Object = MibTableColumn
mplsOutSegmentPerfErrors = _MplsOutSegmentPerfErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 3),
    _MplsOutSegmentPerfErrors_Type()
)
mplsOutSegmentPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfErrors.setStatus("current")
_MplsOutSegmentPerfDiscards_Type = Counter32
_MplsOutSegmentPerfDiscards_Object = MibTableColumn
mplsOutSegmentPerfDiscards = _MplsOutSegmentPerfDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 4),
    _MplsOutSegmentPerfDiscards_Type()
)
mplsOutSegmentPerfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfDiscards.setStatus("current")
_MplsOutSegmentPerfHCOctets_Type = Counter64
_MplsOutSegmentPerfHCOctets_Object = MibTableColumn
mplsOutSegmentPerfHCOctets = _MplsOutSegmentPerfHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 5),
    _MplsOutSegmentPerfHCOctets_Type()
)
mplsOutSegmentPerfHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfHCOctets.setStatus("current")
_MplsOutSegmentPerfDiscontinuityTime_Type = TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object = MibTableColumn
mplsOutSegmentPerfDiscontinuityTime = _MplsOutSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 6),
    _MplsOutSegmentPerfDiscontinuityTime_Type()
)
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentPerfDiscontinuityTime.setStatus("current")
_MplsXCIndexNext_Type = MplsIndexNextType
_MplsXCIndexNext_Object = MibScalar
mplsXCIndexNext = _MplsXCIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 9),
    _MplsXCIndexNext_Type()
)
mplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCIndexNext.setStatus("current")
_MplsXCTable_Object = MibTable
mplsXCTable = _MplsXCTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10)
)
if mibBuilder.loadTexts:
    mplsXCTable.setStatus("current")
_MplsXCEntry_Object = MibTableRow
mplsXCEntry = _MplsXCEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1)
)
mplsXCEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsXCIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    mplsXCEntry.setStatus("current")
_MplsXCIndex_Type = MplsIndexType
_MplsXCIndex_Object = MibTableColumn
mplsXCIndex = _MplsXCIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 1),
    _MplsXCIndex_Type()
)
mplsXCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsXCIndex.setStatus("current")
_MplsXCInSegmentIndex_Type = MplsIndexType
_MplsXCInSegmentIndex_Object = MibTableColumn
mplsXCInSegmentIndex = _MplsXCInSegmentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 2),
    _MplsXCInSegmentIndex_Type()
)
mplsXCInSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsXCInSegmentIndex.setStatus("current")
_MplsXCOutSegmentIndex_Type = MplsIndexType
_MplsXCOutSegmentIndex_Object = MibTableColumn
mplsXCOutSegmentIndex = _MplsXCOutSegmentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 3),
    _MplsXCOutSegmentIndex_Type()
)
mplsXCOutSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsXCOutSegmentIndex.setStatus("current")
_MplsXCLspId_Type = MplsLSPID
_MplsXCLspId_Object = MibTableColumn
mplsXCLspId = _MplsXCLspId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 4),
    _MplsXCLspId_Type()
)
mplsXCLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLspId.setStatus("current")
_MplsXCLabelStackIndex_Type = MplsIndexType
_MplsXCLabelStackIndex_Object = MibTableColumn
mplsXCLabelStackIndex = _MplsXCLabelStackIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 5),
    _MplsXCLabelStackIndex_Type()
)
mplsXCLabelStackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCLabelStackIndex.setStatus("current")
_MplsXCOwner_Type = MplsOwner
_MplsXCOwner_Object = MibTableColumn
mplsXCOwner = _MplsXCOwner_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 6),
    _MplsXCOwner_Type()
)
mplsXCOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCOwner.setStatus("current")
_MplsXCRowStatus_Type = RowStatus
_MplsXCRowStatus_Object = MibTableColumn
mplsXCRowStatus = _MplsXCRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 7),
    _MplsXCRowStatus_Type()
)
mplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCRowStatus.setStatus("current")


class _MplsXCStorageType_Type(StorageType):
    """Custom type mplsXCStorageType based on StorageType"""


_MplsXCStorageType_Object = MibTableColumn
mplsXCStorageType = _MplsXCStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 8),
    _MplsXCStorageType_Type()
)
mplsXCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsXCStorageType.setStatus("current")


class _MplsXCAdminStatus_Type(Integer32):
    """Custom type mplsXCAdminStatus based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 9),
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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 10),
    _MplsXCOperStatus_Type()
)
mplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCOperStatus.setStatus("current")


class _MplsMaxLabelStackDepth_Type(Unsigned32):
    """Custom type mplsMaxLabelStackDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsMaxLabelStackDepth_Type.__name__ = "Unsigned32"
_MplsMaxLabelStackDepth_Object = MibScalar
mplsMaxLabelStackDepth = _MplsMaxLabelStackDepth_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 11),
    _MplsMaxLabelStackDepth_Type()
)
mplsMaxLabelStackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMaxLabelStackDepth.setStatus("current")
_MplsLabelStackIndexNext_Type = MplsIndexNextType
_MplsLabelStackIndexNext_Object = MibScalar
mplsLabelStackIndexNext = _MplsLabelStackIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 12),
    _MplsLabelStackIndexNext_Type()
)
mplsLabelStackIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLabelStackIndexNext.setStatus("current")
_MplsLabelStackTable_Object = MibTable
mplsLabelStackTable = _MplsLabelStackTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13)
)
if mibBuilder.loadTexts:
    mplsLabelStackTable.setStatus("current")
_MplsLabelStackEntry_Object = MibTableRow
mplsLabelStackEntry = _MplsLabelStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1)
)
mplsLabelStackEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsLabelStackIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsLabelStackLabelIndex"),
)
if mibBuilder.loadTexts:
    mplsLabelStackEntry.setStatus("current")
_MplsLabelStackIndex_Type = MplsIndexType
_MplsLabelStackIndex_Object = MibTableColumn
mplsLabelStackIndex = _MplsLabelStackIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 1),
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
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 2),
    _MplsLabelStackLabelIndex_Type()
)
mplsLabelStackLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLabelStackLabelIndex.setStatus("current")
_MplsLabelStackLabel_Type = MplsLabel
_MplsLabelStackLabel_Object = MibTableColumn
mplsLabelStackLabel = _MplsLabelStackLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 3),
    _MplsLabelStackLabel_Type()
)
mplsLabelStackLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackLabel.setStatus("current")


class _MplsLabelStackLabelPtr_Type(RowPointer):
    """Custom type mplsLabelStackLabelPtr based on RowPointer"""
    defaultValue = (0, 0)


_MplsLabelStackLabelPtr_Object = MibTableColumn
mplsLabelStackLabelPtr = _MplsLabelStackLabelPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 4),
    _MplsLabelStackLabelPtr_Type()
)
mplsLabelStackLabelPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackLabelPtr.setStatus("current")
_MplsLabelStackRowStatus_Type = RowStatus
_MplsLabelStackRowStatus_Object = MibTableColumn
mplsLabelStackRowStatus = _MplsLabelStackRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 5),
    _MplsLabelStackRowStatus_Type()
)
mplsLabelStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackRowStatus.setStatus("current")


class _MplsLabelStackStorageType_Type(StorageType):
    """Custom type mplsLabelStackStorageType based on StorageType"""


_MplsLabelStackStorageType_Object = MibTableColumn
mplsLabelStackStorageType = _MplsLabelStackStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 6),
    _MplsLabelStackStorageType_Type()
)
mplsLabelStackStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLabelStackStorageType.setStatus("current")
_MplsInSegmentMapTable_Object = MibTable
mplsInSegmentMapTable = _MplsInSegmentMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14)
)
if mibBuilder.loadTexts:
    mplsInSegmentMapTable.setStatus("current")
_MplsInSegmentMapEntry_Object = MibTableRow
mplsInSegmentMapEntry = _MplsInSegmentMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1)
)
mplsInSegmentMapEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapInterface"),
    (0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapLabel"),
    (0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapLabelPtrIndex"),
)
if mibBuilder.loadTexts:
    mplsInSegmentMapEntry.setStatus("current")
_MplsInSegmentMapInterface_Type = InterfaceIndexOrZero
_MplsInSegmentMapInterface_Object = MibTableColumn
mplsInSegmentMapInterface = _MplsInSegmentMapInterface_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 1),
    _MplsInSegmentMapInterface_Type()
)
mplsInSegmentMapInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentMapInterface.setStatus("current")
_MplsInSegmentMapLabel_Type = MplsLabel
_MplsInSegmentMapLabel_Object = MibTableColumn
mplsInSegmentMapLabel = _MplsInSegmentMapLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 2),
    _MplsInSegmentMapLabel_Type()
)
mplsInSegmentMapLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentMapLabel.setStatus("current")
_MplsInSegmentMapLabelPtrIndex_Type = RowPointer
_MplsInSegmentMapLabelPtrIndex_Object = MibTableColumn
mplsInSegmentMapLabelPtrIndex = _MplsInSegmentMapLabelPtrIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 3),
    _MplsInSegmentMapLabelPtrIndex_Type()
)
mplsInSegmentMapLabelPtrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentMapLabelPtrIndex.setStatus("current")
_MplsInSegmentMapIndex_Type = MplsIndexType
_MplsInSegmentMapIndex_Object = MibTableColumn
mplsInSegmentMapIndex = _MplsInSegmentMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 4),
    _MplsInSegmentMapIndex_Type()
)
mplsInSegmentMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentMapIndex.setStatus("current")


class _MplsXCNotificationsEnable_Type(TruthValue):
    """Custom type mplsXCNotificationsEnable based on TruthValue"""


_MplsXCNotificationsEnable_Object = MibScalar
mplsXCNotificationsEnable = _MplsXCNotificationsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 15),
    _MplsXCNotificationsEnable_Type()
)
mplsXCNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsXCNotificationsEnable.setStatus("current")
_MplsLsrConformance_ObjectIdentity = ObjectIdentity
mplsLsrConformance = _MplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2)
)
_MplsLsrGroups_ObjectIdentity = ObjectIdentity
mplsLsrGroups = _MplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1)
)
_MplsLsrCompliances_ObjectIdentity = ObjectIdentity
mplsLsrCompliances = _MplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 2)
)
mplsInterfaceEntry.registerAugmentions(
    ("MPLS-LSR-STD-MIB",
     "mplsInterfacePerfEntry")
)
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions(
    ("MPLS-LSR-STD-MIB",
     "mplsInSegmentPerfEntry")
)
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(
    ("MPLS-LSR-STD-MIB",
     "mplsOutSegmentPerfEntry")
)
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())

# Managed Objects groups

mplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 1)
)
mplsInterfaceGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMinIn"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMaxIn"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMinOut"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMaxOut"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceTotalBandwidth"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceAvailableBandwidth"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelParticipationType"))
)
if mibBuilder.loadTexts:
    mplsInterfaceGroup.setStatus("current")

mplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 2)
)
mplsInSegmentGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsInSegmentIndexNext"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentInterface"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentLabel"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentLabelPtr"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentNPop"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentAddrFamily"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentXCIndex"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentOwner"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentRowStatus"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentStorageType"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentTrafficParamPtr"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentMapIndex"))
)
if mibBuilder.loadTexts:
    mplsInSegmentGroup.setStatus("current")

mplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 3)
)
mplsOutSegmentGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsOutSegmentIndexNext"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentInterface"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPushTopLabel"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentTopLabel"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentTopLabelPtr"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentNextHopAddrType"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentNextHopAddr"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentXCIndex"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentOwner"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfOctets"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscards"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfErrors"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentRowStatus"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentStorageType"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    mplsOutSegmentGroup.setStatus("current")

mplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 4)
)
mplsXCGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsXCIndexNext"),
        ("MPLS-LSR-STD-MIB", "mplsXCLspId"),
        ("MPLS-LSR-STD-MIB", "mplsXCLabelStackIndex"),
        ("MPLS-LSR-STD-MIB", "mplsXCOwner"),
        ("MPLS-LSR-STD-MIB", "mplsXCStorageType"),
        ("MPLS-LSR-STD-MIB", "mplsXCAdminStatus"),
        ("MPLS-LSR-STD-MIB", "mplsXCOperStatus"),
        ("MPLS-LSR-STD-MIB", "mplsXCRowStatus"),
        ("MPLS-LSR-STD-MIB", "mplsXCNotificationsEnable"))
)
if mibBuilder.loadTexts:
    mplsXCGroup.setStatus("current")

mplsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 5)
)
mplsPerfGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsInSegmentPerfOctets"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfPackets"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfErrors"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfDiscards"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfDiscontinuityTime"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfOctets"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfPackets"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscards"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscontinuityTime"),
        ("MPLS-LSR-STD-MIB", "mplsInterfacePerfInLabelsInUse"),
        ("MPLS-LSR-STD-MIB", "mplsInterfacePerfInLabelLookupFailures"),
        ("MPLS-LSR-STD-MIB", "mplsInterfacePerfOutFragmentedPkts"),
        ("MPLS-LSR-STD-MIB", "mplsInterfacePerfOutLabelsInUse"))
)
if mibBuilder.loadTexts:
    mplsPerfGroup.setStatus("current")

mplsHCInSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 6)
)
mplsHCInSegmentPerfGroup.setObjects(
    ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCInSegmentPerfGroup.setStatus("current")

mplsHCOutSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 7)
)
mplsHCOutSegmentPerfGroup.setObjects(
    ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfHCOctets")
)
if mibBuilder.loadTexts:
    mplsHCOutSegmentPerfGroup.setStatus("current")

mplsLabelStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 8)
)
mplsLabelStackGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsLabelStackLabel"),
        ("MPLS-LSR-STD-MIB", "mplsLabelStackLabelPtr"),
        ("MPLS-LSR-STD-MIB", "mplsLabelStackRowStatus"),
        ("MPLS-LSR-STD-MIB", "mplsLabelStackStorageType"),
        ("MPLS-LSR-STD-MIB", "mplsMaxLabelStackDepth"),
        ("MPLS-LSR-STD-MIB", "mplsLabelStackIndexNext"))
)
if mibBuilder.loadTexts:
    mplsLabelStackGroup.setStatus("current")


# Notification objects

mplsXCUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 0, 1)
)
mplsXCUp.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsXCOperStatus"),
        ("MPLS-LSR-STD-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCUp.setStatus(
        "current"
    )

mplsXCDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 0, 2)
)
mplsXCDown.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsXCOperStatus"),
        ("MPLS-LSR-STD-MIB", "mplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    mplsXCDown.setStatus(
        "current"
    )


# Notifications groups

mplsLsrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 9)
)
mplsLsrNotificationGroup.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsXCUp"),
        ("MPLS-LSR-STD-MIB", "mplsXCDown"))
)
if mibBuilder.loadTexts:
    mplsLsrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLsrModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLsrModuleFullCompliance.setStatus(
        "current"
    )

mplsLsrModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLsrModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LSR-STD-MIB",
    **{"MplsIndexType": MplsIndexType,
       "MplsIndexNextType": MplsIndexNextType,
       "mplsLsrStdMIB": mplsLsrStdMIB,
       "mplsLsrNotifications": mplsLsrNotifications,
       "mplsXCUp": mplsXCUp,
       "mplsXCDown": mplsXCDown,
       "mplsLsrObjects": mplsLsrObjects,
       "mplsInterfaceTable": mplsInterfaceTable,
       "mplsInterfaceEntry": mplsInterfaceEntry,
       "mplsInterfaceIndex": mplsInterfaceIndex,
       "mplsInterfaceLabelMinIn": mplsInterfaceLabelMinIn,
       "mplsInterfaceLabelMaxIn": mplsInterfaceLabelMaxIn,
       "mplsInterfaceLabelMinOut": mplsInterfaceLabelMinOut,
       "mplsInterfaceLabelMaxOut": mplsInterfaceLabelMaxOut,
       "mplsInterfaceTotalBandwidth": mplsInterfaceTotalBandwidth,
       "mplsInterfaceAvailableBandwidth": mplsInterfaceAvailableBandwidth,
       "mplsInterfaceLabelParticipationType": mplsInterfaceLabelParticipationType,
       "mplsInterfacePerfTable": mplsInterfacePerfTable,
       "mplsInterfacePerfEntry": mplsInterfacePerfEntry,
       "mplsInterfacePerfInLabelsInUse": mplsInterfacePerfInLabelsInUse,
       "mplsInterfacePerfInLabelLookupFailures": mplsInterfacePerfInLabelLookupFailures,
       "mplsInterfacePerfOutLabelsInUse": mplsInterfacePerfOutLabelsInUse,
       "mplsInterfacePerfOutFragmentedPkts": mplsInterfacePerfOutFragmentedPkts,
       "mplsInSegmentIndexNext": mplsInSegmentIndexNext,
       "mplsInSegmentTable": mplsInSegmentTable,
       "mplsInSegmentEntry": mplsInSegmentEntry,
       "mplsInSegmentIndex": mplsInSegmentIndex,
       "mplsInSegmentInterface": mplsInSegmentInterface,
       "mplsInSegmentLabel": mplsInSegmentLabel,
       "mplsInSegmentLabelPtr": mplsInSegmentLabelPtr,
       "mplsInSegmentNPop": mplsInSegmentNPop,
       "mplsInSegmentAddrFamily": mplsInSegmentAddrFamily,
       "mplsInSegmentXCIndex": mplsInSegmentXCIndex,
       "mplsInSegmentOwner": mplsInSegmentOwner,
       "mplsInSegmentTrafficParamPtr": mplsInSegmentTrafficParamPtr,
       "mplsInSegmentRowStatus": mplsInSegmentRowStatus,
       "mplsInSegmentStorageType": mplsInSegmentStorageType,
       "mplsInSegmentPerfTable": mplsInSegmentPerfTable,
       "mplsInSegmentPerfEntry": mplsInSegmentPerfEntry,
       "mplsInSegmentPerfOctets": mplsInSegmentPerfOctets,
       "mplsInSegmentPerfPackets": mplsInSegmentPerfPackets,
       "mplsInSegmentPerfErrors": mplsInSegmentPerfErrors,
       "mplsInSegmentPerfDiscards": mplsInSegmentPerfDiscards,
       "mplsInSegmentPerfHCOctets": mplsInSegmentPerfHCOctets,
       "mplsInSegmentPerfDiscontinuityTime": mplsInSegmentPerfDiscontinuityTime,
       "mplsOutSegmentIndexNext": mplsOutSegmentIndexNext,
       "mplsOutSegmentTable": mplsOutSegmentTable,
       "mplsOutSegmentEntry": mplsOutSegmentEntry,
       "mplsOutSegmentIndex": mplsOutSegmentIndex,
       "mplsOutSegmentInterface": mplsOutSegmentInterface,
       "mplsOutSegmentPushTopLabel": mplsOutSegmentPushTopLabel,
       "mplsOutSegmentTopLabel": mplsOutSegmentTopLabel,
       "mplsOutSegmentTopLabelPtr": mplsOutSegmentTopLabelPtr,
       "mplsOutSegmentNextHopAddrType": mplsOutSegmentNextHopAddrType,
       "mplsOutSegmentNextHopAddr": mplsOutSegmentNextHopAddr,
       "mplsOutSegmentXCIndex": mplsOutSegmentXCIndex,
       "mplsOutSegmentOwner": mplsOutSegmentOwner,
       "mplsOutSegmentTrafficParamPtr": mplsOutSegmentTrafficParamPtr,
       "mplsOutSegmentRowStatus": mplsOutSegmentRowStatus,
       "mplsOutSegmentStorageType": mplsOutSegmentStorageType,
       "mplsOutSegmentPerfTable": mplsOutSegmentPerfTable,
       "mplsOutSegmentPerfEntry": mplsOutSegmentPerfEntry,
       "mplsOutSegmentPerfOctets": mplsOutSegmentPerfOctets,
       "mplsOutSegmentPerfPackets": mplsOutSegmentPerfPackets,
       "mplsOutSegmentPerfErrors": mplsOutSegmentPerfErrors,
       "mplsOutSegmentPerfDiscards": mplsOutSegmentPerfDiscards,
       "mplsOutSegmentPerfHCOctets": mplsOutSegmentPerfHCOctets,
       "mplsOutSegmentPerfDiscontinuityTime": mplsOutSegmentPerfDiscontinuityTime,
       "mplsXCIndexNext": mplsXCIndexNext,
       "mplsXCTable": mplsXCTable,
       "mplsXCEntry": mplsXCEntry,
       "mplsXCIndex": mplsXCIndex,
       "mplsXCInSegmentIndex": mplsXCInSegmentIndex,
       "mplsXCOutSegmentIndex": mplsXCOutSegmentIndex,
       "mplsXCLspId": mplsXCLspId,
       "mplsXCLabelStackIndex": mplsXCLabelStackIndex,
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
       "mplsLabelStackLabelPtr": mplsLabelStackLabelPtr,
       "mplsLabelStackRowStatus": mplsLabelStackRowStatus,
       "mplsLabelStackStorageType": mplsLabelStackStorageType,
       "mplsInSegmentMapTable": mplsInSegmentMapTable,
       "mplsInSegmentMapEntry": mplsInSegmentMapEntry,
       "mplsInSegmentMapInterface": mplsInSegmentMapInterface,
       "mplsInSegmentMapLabel": mplsInSegmentMapLabel,
       "mplsInSegmentMapLabelPtrIndex": mplsInSegmentMapLabelPtrIndex,
       "mplsInSegmentMapIndex": mplsInSegmentMapIndex,
       "mplsXCNotificationsEnable": mplsXCNotificationsEnable,
       "mplsLsrConformance": mplsLsrConformance,
       "mplsLsrGroups": mplsLsrGroups,
       "mplsInterfaceGroup": mplsInterfaceGroup,
       "mplsInSegmentGroup": mplsInSegmentGroup,
       "mplsOutSegmentGroup": mplsOutSegmentGroup,
       "mplsXCGroup": mplsXCGroup,
       "mplsPerfGroup": mplsPerfGroup,
       "mplsHCInSegmentPerfGroup": mplsHCInSegmentPerfGroup,
       "mplsHCOutSegmentPerfGroup": mplsHCOutSegmentPerfGroup,
       "mplsLabelStackGroup": mplsLabelStackGroup,
       "mplsLsrNotificationGroup": mplsLsrNotificationGroup,
       "mplsLsrCompliances": mplsLsrCompliances,
       "mplsLsrModuleFullCompliance": mplsLsrModuleFullCompliance,
       "mplsLsrModuleReadOnlyCompliance": mplsLsrModuleReadOnlyCompliance}
)
