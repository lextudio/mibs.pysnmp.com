# SNMP MIB module (HPN-ICF-MPLS-LSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLS-LSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:11 2024
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

(hpnicfMpls,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfMpls")

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

hpnicfMplsLsr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1)
)
hpnicfMplsLsr.setRevisions(
        ("2000-07-12 12:00",
         "2000-07-07 12:00",
         "2000-04-26 12:00",
         "2000-04-21 12:00",
         "2000-03-06 12:00",
         "2000-02-16 12:00",
         "1999-06-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMplsLSPID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class HpnicfMplsLabel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class HpnicfMplsBitRate(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class HpnicfMplsBurstSize(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class HpnicfMplsObjectOwner(Integer32, TextualConvention):
    status = "current"
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
        *(("crldp", 5),
          ("ldp", 3),
          ("other", 1),
          ("policyAgent", 6),
          ("rsvp", 4),
          ("snmp", 2),
          ("unknown", 7))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfmplsLsrObjects_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrObjects = _HpnicfmplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1)
)
_HpnicfmplsInterfaceConfTable_Object = MibTable
hpnicfmplsInterfaceConfTable = _HpnicfmplsInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceConfTable.setStatus("current")
_HpnicfmplsInterfaceConfEntry_Object = MibTableRow
hpnicfmplsInterfaceConfEntry = _HpnicfmplsInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1)
)
hpnicfmplsInterfaceConfEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceConfEntry.setStatus("current")
_HpnicfmplsInterfaceConfIndex_Type = InterfaceIndexOrZero
_HpnicfmplsInterfaceConfIndex_Object = MibTableColumn
hpnicfmplsInterfaceConfIndex = _HpnicfmplsInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 1),
    _HpnicfmplsInterfaceConfIndex_Type()
)
hpnicfmplsInterfaceConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceConfIndex.setStatus("current")
_HpnicfmplsInterfaceLabelMinIn_Type = HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMinIn_Object = MibTableColumn
hpnicfmplsInterfaceLabelMinIn = _HpnicfmplsInterfaceLabelMinIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 2),
    _HpnicfmplsInterfaceLabelMinIn_Type()
)
hpnicfmplsInterfaceLabelMinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceLabelMinIn.setStatus("current")
_HpnicfmplsInterfaceLabelMaxIn_Type = HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMaxIn_Object = MibTableColumn
hpnicfmplsInterfaceLabelMaxIn = _HpnicfmplsInterfaceLabelMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 3),
    _HpnicfmplsInterfaceLabelMaxIn_Type()
)
hpnicfmplsInterfaceLabelMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceLabelMaxIn.setStatus("current")
_HpnicfmplsInterfaceLabelMinOut_Type = HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMinOut_Object = MibTableColumn
hpnicfmplsInterfaceLabelMinOut = _HpnicfmplsInterfaceLabelMinOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 4),
    _HpnicfmplsInterfaceLabelMinOut_Type()
)
hpnicfmplsInterfaceLabelMinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceLabelMinOut.setStatus("current")
_HpnicfmplsInterfaceLabelMaxOut_Type = HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMaxOut_Object = MibTableColumn
hpnicfmplsInterfaceLabelMaxOut = _HpnicfmplsInterfaceLabelMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 5),
    _HpnicfmplsInterfaceLabelMaxOut_Type()
)
hpnicfmplsInterfaceLabelMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceLabelMaxOut.setStatus("current")
_HpnicfmplsInterfaceTotalBandwidth_Type = HpnicfMplsBitRate
_HpnicfmplsInterfaceTotalBandwidth_Object = MibTableColumn
hpnicfmplsInterfaceTotalBandwidth = _HpnicfmplsInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 6),
    _HpnicfmplsInterfaceTotalBandwidth_Type()
)
hpnicfmplsInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceTotalBandwidth.setStatus("current")
_HpnicfmplsInterfaceAvailableBandwidth_Type = HpnicfMplsBitRate
_HpnicfmplsInterfaceAvailableBandwidth_Object = MibTableColumn
hpnicfmplsInterfaceAvailableBandwidth = _HpnicfmplsInterfaceAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 7),
    _HpnicfmplsInterfaceAvailableBandwidth_Type()
)
hpnicfmplsInterfaceAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceAvailableBandwidth.setStatus("current")


class _HpnicfmplsInterfaceLabelParticipationType_Type(Bits):
    """Custom type hpnicfmplsInterfaceLabelParticipationType based on Bits"""
    namedValues = NamedValues(
        *(("perInterface", 1),
          ("perPlatform", 0))
    )

_HpnicfmplsInterfaceLabelParticipationType_Type.__name__ = "Bits"
_HpnicfmplsInterfaceLabelParticipationType_Object = MibTableColumn
hpnicfmplsInterfaceLabelParticipationType = _HpnicfmplsInterfaceLabelParticipationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 8),
    _HpnicfmplsInterfaceLabelParticipationType_Type()
)
hpnicfmplsInterfaceLabelParticipationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceLabelParticipationType.setStatus("current")
_HpnicfmplsInterfaceConfStorageType_Type = StorageType
_HpnicfmplsInterfaceConfStorageType_Object = MibTableColumn
hpnicfmplsInterfaceConfStorageType = _HpnicfmplsInterfaceConfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 1, 1, 9),
    _HpnicfmplsInterfaceConfStorageType_Type()
)
hpnicfmplsInterfaceConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceConfStorageType.setStatus("current")
_HpnicfmplsInterfacePerfTable_Object = MibTable
hpnicfmplsInterfacePerfTable = _HpnicfmplsInterfacePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfmplsInterfacePerfTable.setStatus("current")
_HpnicfmplsInterfacePerfEntry_Object = MibTableRow
hpnicfmplsInterfacePerfEntry = _HpnicfmplsInterfacePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsInterfacePerfEntry.setStatus("current")
_HpnicfmplsInterfaceInLabelsUsed_Type = Gauge32
_HpnicfmplsInterfaceInLabelsUsed_Object = MibTableColumn
hpnicfmplsInterfaceInLabelsUsed = _HpnicfmplsInterfaceInLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2, 1, 1),
    _HpnicfmplsInterfaceInLabelsUsed_Type()
)
hpnicfmplsInterfaceInLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceInLabelsUsed.setStatus("current")
_HpnicfmplsInterfaceFailedLabelLookup_Type = Counter32
_HpnicfmplsInterfaceFailedLabelLookup_Object = MibTableColumn
hpnicfmplsInterfaceFailedLabelLookup = _HpnicfmplsInterfaceFailedLabelLookup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2, 1, 2),
    _HpnicfmplsInterfaceFailedLabelLookup_Type()
)
hpnicfmplsInterfaceFailedLabelLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceFailedLabelLookup.setStatus("current")
_HpnicfmplsInterfaceOutLabelsUsed_Type = Gauge32
_HpnicfmplsInterfaceOutLabelsUsed_Object = MibTableColumn
hpnicfmplsInterfaceOutLabelsUsed = _HpnicfmplsInterfaceOutLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2, 1, 3),
    _HpnicfmplsInterfaceOutLabelsUsed_Type()
)
hpnicfmplsInterfaceOutLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceOutLabelsUsed.setStatus("current")
_HpnicfmplsInterfaceOutFragments_Type = Counter32
_HpnicfmplsInterfaceOutFragments_Object = MibTableColumn
hpnicfmplsInterfaceOutFragments = _HpnicfmplsInterfaceOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 2, 1, 4),
    _HpnicfmplsInterfaceOutFragments_Type()
)
hpnicfmplsInterfaceOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceOutFragments.setStatus("current")
_HpnicfmplsInSegmentTable_Object = MibTable
hpnicfmplsInSegmentTable = _HpnicfmplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentTable.setStatus("current")
_HpnicfmplsInSegmentEntry_Object = MibTableRow
hpnicfmplsInSegmentEntry = _HpnicfmplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1)
)
hpnicfmplsInSegmentEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentIfIndex"),
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentLabel"),
)
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentEntry.setStatus("current")
_HpnicfmplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_HpnicfmplsInSegmentIfIndex_Object = MibTableColumn
hpnicfmplsInSegmentIfIndex = _HpnicfmplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 1),
    _HpnicfmplsInSegmentIfIndex_Type()
)
hpnicfmplsInSegmentIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentIfIndex.setStatus("current")
_HpnicfmplsInSegmentLabel_Type = HpnicfMplsLabel
_HpnicfmplsInSegmentLabel_Object = MibTableColumn
hpnicfmplsInSegmentLabel = _HpnicfmplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 2),
    _HpnicfmplsInSegmentLabel_Type()
)
hpnicfmplsInSegmentLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentLabel.setStatus("current")


class _HpnicfmplsInSegmentNPop_Type(Integer32):
    """Custom type hpnicfmplsInSegmentNPop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsInSegmentNPop_Type.__name__ = "Integer32"
_HpnicfmplsInSegmentNPop_Object = MibTableColumn
hpnicfmplsInSegmentNPop = _HpnicfmplsInSegmentNPop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 3),
    _HpnicfmplsInSegmentNPop_Type()
)
hpnicfmplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentNPop.setStatus("current")


class _HpnicfmplsInSegmentAddrFamily_Type(AddressFamilyNumbers):
    """Custom type hpnicfmplsInSegmentAddrFamily based on AddressFamilyNumbers"""


_HpnicfmplsInSegmentAddrFamily_Object = MibTableColumn
hpnicfmplsInSegmentAddrFamily = _HpnicfmplsInSegmentAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 4),
    _HpnicfmplsInSegmentAddrFamily_Type()
)
hpnicfmplsInSegmentAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentAddrFamily.setStatus("current")


class _HpnicfmplsInSegmentXCIndex_Type(Integer32):
    """Custom type hpnicfmplsInSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsInSegmentXCIndex_Type.__name__ = "Integer32"
_HpnicfmplsInSegmentXCIndex_Object = MibTableColumn
hpnicfmplsInSegmentXCIndex = _HpnicfmplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 5),
    _HpnicfmplsInSegmentXCIndex_Type()
)
hpnicfmplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentXCIndex.setStatus("current")


class _HpnicfmplsInSegmentOwner_Type(HpnicfMplsObjectOwner):
    """Custom type hpnicfmplsInSegmentOwner based on HpnicfMplsObjectOwner"""


_HpnicfmplsInSegmentOwner_Object = MibTableColumn
hpnicfmplsInSegmentOwner = _HpnicfmplsInSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 6),
    _HpnicfmplsInSegmentOwner_Type()
)
hpnicfmplsInSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentOwner.setStatus("current")
_HpnicfmplsInSegmentTrafficParamPtr_Type = RowPointer
_HpnicfmplsInSegmentTrafficParamPtr_Object = MibTableColumn
hpnicfmplsInSegmentTrafficParamPtr = _HpnicfmplsInSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 7),
    _HpnicfmplsInSegmentTrafficParamPtr_Type()
)
hpnicfmplsInSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentTrafficParamPtr.setStatus("current")
_HpnicfmplsInSegmentRowStatus_Type = RowStatus
_HpnicfmplsInSegmentRowStatus_Object = MibTableColumn
hpnicfmplsInSegmentRowStatus = _HpnicfmplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 8),
    _HpnicfmplsInSegmentRowStatus_Type()
)
hpnicfmplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentRowStatus.setStatus("current")
_HpnicfmplsInSegmentStorageType_Type = StorageType
_HpnicfmplsInSegmentStorageType_Object = MibTableColumn
hpnicfmplsInSegmentStorageType = _HpnicfmplsInSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 3, 1, 9),
    _HpnicfmplsInSegmentStorageType_Type()
)
hpnicfmplsInSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentStorageType.setStatus("current")
_HpnicfmplsInSegmentPerfTable_Object = MibTable
hpnicfmplsInSegmentPerfTable = _HpnicfmplsInSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentPerfTable.setStatus("current")
_HpnicfmplsInSegmentPerfEntry_Object = MibTableRow
hpnicfmplsInSegmentPerfEntry = _HpnicfmplsInSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentPerfEntry.setStatus("current")
_HpnicfmplsInSegmentOctets_Type = Counter32
_HpnicfmplsInSegmentOctets_Object = MibTableColumn
hpnicfmplsInSegmentOctets = _HpnicfmplsInSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 1),
    _HpnicfmplsInSegmentOctets_Type()
)
hpnicfmplsInSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentOctets.setStatus("current")
_HpnicfmplsInSegmentPackets_Type = Counter32
_HpnicfmplsInSegmentPackets_Object = MibTableColumn
hpnicfmplsInSegmentPackets = _HpnicfmplsInSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 2),
    _HpnicfmplsInSegmentPackets_Type()
)
hpnicfmplsInSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentPackets.setStatus("current")
_HpnicfmplsInSegmentErrors_Type = Counter32
_HpnicfmplsInSegmentErrors_Object = MibTableColumn
hpnicfmplsInSegmentErrors = _HpnicfmplsInSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 3),
    _HpnicfmplsInSegmentErrors_Type()
)
hpnicfmplsInSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentErrors.setStatus("current")
_HpnicfmplsInSegmentDiscards_Type = Counter32
_HpnicfmplsInSegmentDiscards_Object = MibTableColumn
hpnicfmplsInSegmentDiscards = _HpnicfmplsInSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 4),
    _HpnicfmplsInSegmentDiscards_Type()
)
hpnicfmplsInSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentDiscards.setStatus("current")
_HpnicfmplsInSegmentHCOctets_Type = Counter64
_HpnicfmplsInSegmentHCOctets_Object = MibTableColumn
hpnicfmplsInSegmentHCOctets = _HpnicfmplsInSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 5),
    _HpnicfmplsInSegmentHCOctets_Type()
)
hpnicfmplsInSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentHCOctets.setStatus("current")
_HpnicfmplsInSegmentPerfDiscontinuityTime_Type = TimeStamp
_HpnicfmplsInSegmentPerfDiscontinuityTime_Object = MibTableColumn
hpnicfmplsInSegmentPerfDiscontinuityTime = _HpnicfmplsInSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 4, 1, 6),
    _HpnicfmplsInSegmentPerfDiscontinuityTime_Type()
)
hpnicfmplsInSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentPerfDiscontinuityTime.setStatus("current")


class _HpnicfmplsOutSegmentIndexNext_Type(Integer32):
    """Custom type hpnicfmplsOutSegmentIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsOutSegmentIndexNext_Type.__name__ = "Integer32"
_HpnicfmplsOutSegmentIndexNext_Object = MibScalar
hpnicfmplsOutSegmentIndexNext = _HpnicfmplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 5),
    _HpnicfmplsOutSegmentIndexNext_Type()
)
hpnicfmplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentIndexNext.setStatus("current")
_HpnicfmplsOutSegmentTable_Object = MibTable
hpnicfmplsOutSegmentTable = _HpnicfmplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentTable.setStatus("current")
_HpnicfmplsOutSegmentEntry_Object = MibTableRow
hpnicfmplsOutSegmentEntry = _HpnicfmplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1)
)
hpnicfmplsOutSegmentEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentEntry.setStatus("current")


class _HpnicfmplsOutSegmentIndex_Type(Integer32):
    """Custom type hpnicfmplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsOutSegmentIndex_Type.__name__ = "Integer32"
_HpnicfmplsOutSegmentIndex_Object = MibTableColumn
hpnicfmplsOutSegmentIndex = _HpnicfmplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 1),
    _HpnicfmplsOutSegmentIndex_Type()
)
hpnicfmplsOutSegmentIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentIndex.setStatus("current")
_HpnicfmplsOutSegmentIfIndex_Type = InterfaceIndex
_HpnicfmplsOutSegmentIfIndex_Object = MibTableColumn
hpnicfmplsOutSegmentIfIndex = _HpnicfmplsOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 2),
    _HpnicfmplsOutSegmentIfIndex_Type()
)
hpnicfmplsOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentIfIndex.setStatus("current")
_HpnicfmplsOutSegmentPushTopLabel_Type = TruthValue
_HpnicfmplsOutSegmentPushTopLabel_Object = MibTableColumn
hpnicfmplsOutSegmentPushTopLabel = _HpnicfmplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 3),
    _HpnicfmplsOutSegmentPushTopLabel_Type()
)
hpnicfmplsOutSegmentPushTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentPushTopLabel.setStatus("current")
_HpnicfmplsOutSegmentTopLabel_Type = HpnicfMplsLabel
_HpnicfmplsOutSegmentTopLabel_Object = MibTableColumn
hpnicfmplsOutSegmentTopLabel = _HpnicfmplsOutSegmentTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 4),
    _HpnicfmplsOutSegmentTopLabel_Type()
)
hpnicfmplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentTopLabel.setStatus("current")


class _HpnicfmplsOutSegmentNextHopIpAddrType_Type(InetAddressType):
    """Custom type hpnicfmplsOutSegmentNextHopIpAddrType based on InetAddressType"""


_HpnicfmplsOutSegmentNextHopIpAddrType_Object = MibTableColumn
hpnicfmplsOutSegmentNextHopIpAddrType = _HpnicfmplsOutSegmentNextHopIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 5),
    _HpnicfmplsOutSegmentNextHopIpAddrType_Type()
)
hpnicfmplsOutSegmentNextHopIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentNextHopIpAddrType.setStatus("current")
_HpnicfmplsOutSegmentNextHopIpv4Addr_Type = InetAddressIPv4
_HpnicfmplsOutSegmentNextHopIpv4Addr_Object = MibTableColumn
hpnicfmplsOutSegmentNextHopIpv4Addr = _HpnicfmplsOutSegmentNextHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 6),
    _HpnicfmplsOutSegmentNextHopIpv4Addr_Type()
)
hpnicfmplsOutSegmentNextHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentNextHopIpv4Addr.setStatus("current")
_HpnicfmplsOutSegmentNextHopIpv6Addr_Type = InetAddressIPv6
_HpnicfmplsOutSegmentNextHopIpv6Addr_Object = MibTableColumn
hpnicfmplsOutSegmentNextHopIpv6Addr = _HpnicfmplsOutSegmentNextHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 7),
    _HpnicfmplsOutSegmentNextHopIpv6Addr_Type()
)
hpnicfmplsOutSegmentNextHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentNextHopIpv6Addr.setStatus("current")


class _HpnicfmplsOutSegmentXCIndex_Type(Integer32):
    """Custom type hpnicfmplsOutSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsOutSegmentXCIndex_Type.__name__ = "Integer32"
_HpnicfmplsOutSegmentXCIndex_Object = MibTableColumn
hpnicfmplsOutSegmentXCIndex = _HpnicfmplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 8),
    _HpnicfmplsOutSegmentXCIndex_Type()
)
hpnicfmplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentXCIndex.setStatus("current")


class _HpnicfmplsOutSegmentOwner_Type(HpnicfMplsObjectOwner):
    """Custom type hpnicfmplsOutSegmentOwner based on HpnicfMplsObjectOwner"""


_HpnicfmplsOutSegmentOwner_Object = MibTableColumn
hpnicfmplsOutSegmentOwner = _HpnicfmplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 9),
    _HpnicfmplsOutSegmentOwner_Type()
)
hpnicfmplsOutSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentOwner.setStatus("current")
_HpnicfmplsOutSegmentTrafficParamPtr_Type = RowPointer
_HpnicfmplsOutSegmentTrafficParamPtr_Object = MibTableColumn
hpnicfmplsOutSegmentTrafficParamPtr = _HpnicfmplsOutSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 10),
    _HpnicfmplsOutSegmentTrafficParamPtr_Type()
)
hpnicfmplsOutSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentTrafficParamPtr.setStatus("current")
_HpnicfmplsOutSegmentRowStatus_Type = RowStatus
_HpnicfmplsOutSegmentRowStatus_Object = MibTableColumn
hpnicfmplsOutSegmentRowStatus = _HpnicfmplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 11),
    _HpnicfmplsOutSegmentRowStatus_Type()
)
hpnicfmplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentRowStatus.setStatus("current")
_HpnicfmplsOutSegmentStorageType_Type = StorageType
_HpnicfmplsOutSegmentStorageType_Object = MibTableColumn
hpnicfmplsOutSegmentStorageType = _HpnicfmplsOutSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 6, 1, 12),
    _HpnicfmplsOutSegmentStorageType_Type()
)
hpnicfmplsOutSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentStorageType.setStatus("current")
_HpnicfmplsOutSegmentPerfTable_Object = MibTable
hpnicfmplsOutSegmentPerfTable = _HpnicfmplsOutSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentPerfTable.setStatus("current")
_HpnicfmplsOutSegmentPerfEntry_Object = MibTableRow
hpnicfmplsOutSegmentPerfEntry = _HpnicfmplsOutSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentPerfEntry.setStatus("current")
_HpnicfmplsOutSegmentOctets_Type = Counter32
_HpnicfmplsOutSegmentOctets_Object = MibTableColumn
hpnicfmplsOutSegmentOctets = _HpnicfmplsOutSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 1),
    _HpnicfmplsOutSegmentOctets_Type()
)
hpnicfmplsOutSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentOctets.setStatus("current")
_HpnicfmplsOutSegmentPackets_Type = Counter32
_HpnicfmplsOutSegmentPackets_Object = MibTableColumn
hpnicfmplsOutSegmentPackets = _HpnicfmplsOutSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 2),
    _HpnicfmplsOutSegmentPackets_Type()
)
hpnicfmplsOutSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentPackets.setStatus("current")
_HpnicfmplsOutSegmentErrors_Type = Counter32
_HpnicfmplsOutSegmentErrors_Object = MibTableColumn
hpnicfmplsOutSegmentErrors = _HpnicfmplsOutSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 3),
    _HpnicfmplsOutSegmentErrors_Type()
)
hpnicfmplsOutSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentErrors.setStatus("current")
_HpnicfmplsOutSegmentDiscards_Type = Counter32
_HpnicfmplsOutSegmentDiscards_Object = MibTableColumn
hpnicfmplsOutSegmentDiscards = _HpnicfmplsOutSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 4),
    _HpnicfmplsOutSegmentDiscards_Type()
)
hpnicfmplsOutSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentDiscards.setStatus("current")
_HpnicfmplsOutSegmentHCOctets_Type = Counter64
_HpnicfmplsOutSegmentHCOctets_Object = MibTableColumn
hpnicfmplsOutSegmentHCOctets = _HpnicfmplsOutSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 5),
    _HpnicfmplsOutSegmentHCOctets_Type()
)
hpnicfmplsOutSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentHCOctets.setStatus("current")
_HpnicfmplsOutSegmentPerfDiscontinuityTime_Type = TimeStamp
_HpnicfmplsOutSegmentPerfDiscontinuityTime_Object = MibTableColumn
hpnicfmplsOutSegmentPerfDiscontinuityTime = _HpnicfmplsOutSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 7, 1, 6),
    _HpnicfmplsOutSegmentPerfDiscontinuityTime_Type()
)
hpnicfmplsOutSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentPerfDiscontinuityTime.setStatus("current")


class _HpnicfmplsXCIndexNext_Type(Integer32):
    """Custom type hpnicfmplsXCIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsXCIndexNext_Type.__name__ = "Integer32"
_HpnicfmplsXCIndexNext_Object = MibScalar
hpnicfmplsXCIndexNext = _HpnicfmplsXCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 8),
    _HpnicfmplsXCIndexNext_Type()
)
hpnicfmplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsXCIndexNext.setStatus("current")
_HpnicfmplsXCTable_Object = MibTable
hpnicfmplsXCTable = _HpnicfmplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfmplsXCTable.setStatus("current")
_HpnicfmplsXCEntry_Object = MibTableRow
hpnicfmplsXCEntry = _HpnicfmplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1)
)
hpnicfmplsXCEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIndex"),
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentIfIndex"),
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentLabel"),
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsXCEntry.setStatus("current")


class _HpnicfmplsXCIndex_Type(Integer32):
    """Custom type hpnicfmplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsXCIndex_Type.__name__ = "Integer32"
_HpnicfmplsXCIndex_Object = MibTableColumn
hpnicfmplsXCIndex = _HpnicfmplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 1),
    _HpnicfmplsXCIndex_Type()
)
hpnicfmplsXCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfmplsXCIndex.setStatus("current")
_HpnicfmplsXCLspId_Type = HpnicfMplsLSPID
_HpnicfmplsXCLspId_Object = MibTableColumn
hpnicfmplsXCLspId = _HpnicfmplsXCLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 2),
    _HpnicfmplsXCLspId_Type()
)
hpnicfmplsXCLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCLspId.setStatus("current")


class _HpnicfmplsXCLabelStackIndex_Type(Integer32):
    """Custom type hpnicfmplsXCLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsXCLabelStackIndex_Type.__name__ = "Integer32"
_HpnicfmplsXCLabelStackIndex_Object = MibTableColumn
hpnicfmplsXCLabelStackIndex = _HpnicfmplsXCLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 3),
    _HpnicfmplsXCLabelStackIndex_Type()
)
hpnicfmplsXCLabelStackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCLabelStackIndex.setStatus("current")


class _HpnicfmplsXCIsPersistent_Type(TruthValue):
    """Custom type hpnicfmplsXCIsPersistent based on TruthValue"""


_HpnicfmplsXCIsPersistent_Object = MibTableColumn
hpnicfmplsXCIsPersistent = _HpnicfmplsXCIsPersistent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 4),
    _HpnicfmplsXCIsPersistent_Type()
)
hpnicfmplsXCIsPersistent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCIsPersistent.setStatus("current")
_HpnicfmplsXCOwner_Type = HpnicfMplsObjectOwner
_HpnicfmplsXCOwner_Object = MibTableColumn
hpnicfmplsXCOwner = _HpnicfmplsXCOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 5),
    _HpnicfmplsXCOwner_Type()
)
hpnicfmplsXCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCOwner.setStatus("current")
_HpnicfmplsXCRowStatus_Type = RowStatus
_HpnicfmplsXCRowStatus_Object = MibTableColumn
hpnicfmplsXCRowStatus = _HpnicfmplsXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 6),
    _HpnicfmplsXCRowStatus_Type()
)
hpnicfmplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCRowStatus.setStatus("current")
_HpnicfmplsXCStorageType_Type = StorageType
_HpnicfmplsXCStorageType_Object = MibTableColumn
hpnicfmplsXCStorageType = _HpnicfmplsXCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 7),
    _HpnicfmplsXCStorageType_Type()
)
hpnicfmplsXCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCStorageType.setStatus("current")


class _HpnicfmplsXCAdminStatus_Type(Integer32):
    """Custom type hpnicfmplsXCAdminStatus based on Integer32"""
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


_HpnicfmplsXCAdminStatus_Type.__name__ = "Integer32"
_HpnicfmplsXCAdminStatus_Object = MibTableColumn
hpnicfmplsXCAdminStatus = _HpnicfmplsXCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 8),
    _HpnicfmplsXCAdminStatus_Type()
)
hpnicfmplsXCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsXCAdminStatus.setStatus("current")


class _HpnicfmplsXCOperStatus_Type(Integer32):
    """Custom type hpnicfmplsXCOperStatus based on Integer32"""
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


_HpnicfmplsXCOperStatus_Type.__name__ = "Integer32"
_HpnicfmplsXCOperStatus_Object = MibTableColumn
hpnicfmplsXCOperStatus = _HpnicfmplsXCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 9, 1, 9),
    _HpnicfmplsXCOperStatus_Type()
)
hpnicfmplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsXCOperStatus.setStatus("current")


class _HpnicfmplsMaxLabelStackDepth_Type(Integer32):
    """Custom type hpnicfmplsMaxLabelStackDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsMaxLabelStackDepth_Type.__name__ = "Integer32"
_HpnicfmplsMaxLabelStackDepth_Object = MibScalar
hpnicfmplsMaxLabelStackDepth = _HpnicfmplsMaxLabelStackDepth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 10),
    _HpnicfmplsMaxLabelStackDepth_Type()
)
hpnicfmplsMaxLabelStackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsMaxLabelStackDepth.setStatus("current")


class _HpnicfmplsLabelStackIndexNext_Type(Integer32):
    """Custom type hpnicfmplsLabelStackIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsLabelStackIndexNext_Type.__name__ = "Integer32"
_HpnicfmplsLabelStackIndexNext_Object = MibScalar
hpnicfmplsLabelStackIndexNext = _HpnicfmplsLabelStackIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 11),
    _HpnicfmplsLabelStackIndexNext_Type()
)
hpnicfmplsLabelStackIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackIndexNext.setStatus("current")
_HpnicfmplsLabelStackTable_Object = MibTable
hpnicfmplsLabelStackTable = _HpnicfmplsLabelStackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackTable.setStatus("current")
_HpnicfmplsLabelStackEntry_Object = MibTableRow
hpnicfmplsLabelStackEntry = _HpnicfmplsLabelStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1)
)
hpnicfmplsLabelStackEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackIndex"),
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackLabelIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackEntry.setStatus("current")


class _HpnicfmplsLabelStackIndex_Type(Integer32):
    """Custom type hpnicfmplsLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsLabelStackIndex_Type.__name__ = "Integer32"
_HpnicfmplsLabelStackIndex_Object = MibTableColumn
hpnicfmplsLabelStackIndex = _HpnicfmplsLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1, 1),
    _HpnicfmplsLabelStackIndex_Type()
)
hpnicfmplsLabelStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackIndex.setStatus("current")


class _HpnicfmplsLabelStackLabelIndex_Type(Integer32):
    """Custom type hpnicfmplsLabelStackLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsLabelStackLabelIndex_Type.__name__ = "Integer32"
_HpnicfmplsLabelStackLabelIndex_Object = MibTableColumn
hpnicfmplsLabelStackLabelIndex = _HpnicfmplsLabelStackLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1, 2),
    _HpnicfmplsLabelStackLabelIndex_Type()
)
hpnicfmplsLabelStackLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackLabelIndex.setStatus("current")
_HpnicfmplsLabelStackLabel_Type = HpnicfMplsLabel
_HpnicfmplsLabelStackLabel_Object = MibTableColumn
hpnicfmplsLabelStackLabel = _HpnicfmplsLabelStackLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1, 3),
    _HpnicfmplsLabelStackLabel_Type()
)
hpnicfmplsLabelStackLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackLabel.setStatus("current")
_HpnicfmplsLabelStackRowStatus_Type = RowStatus
_HpnicfmplsLabelStackRowStatus_Object = MibTableColumn
hpnicfmplsLabelStackRowStatus = _HpnicfmplsLabelStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1, 4),
    _HpnicfmplsLabelStackRowStatus_Type()
)
hpnicfmplsLabelStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackRowStatus.setStatus("current")
_HpnicfmplsLabelStackStorageType_Type = StorageType
_HpnicfmplsLabelStackStorageType_Object = MibTableColumn
hpnicfmplsLabelStackStorageType = _HpnicfmplsLabelStackStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 12, 1, 5),
    _HpnicfmplsLabelStackStorageType_Type()
)
hpnicfmplsLabelStackStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackStorageType.setStatus("current")


class _HpnicfmplsTrafficParamIndexNext_Type(Integer32):
    """Custom type hpnicfmplsTrafficParamIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfmplsTrafficParamIndexNext_Type.__name__ = "Integer32"
_HpnicfmplsTrafficParamIndexNext_Object = MibScalar
hpnicfmplsTrafficParamIndexNext = _HpnicfmplsTrafficParamIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 13),
    _HpnicfmplsTrafficParamIndexNext_Type()
)
hpnicfmplsTrafficParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamIndexNext.setStatus("current")
_HpnicfmplsTrafficParamTable_Object = MibTable
hpnicfmplsTrafficParamTable = _HpnicfmplsTrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamTable.setStatus("current")
_HpnicfmplsTrafficParamEntry_Object = MibTableRow
hpnicfmplsTrafficParamEntry = _HpnicfmplsTrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1)
)
hpnicfmplsTrafficParamEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamEntry.setStatus("current")


class _HpnicfmplsTrafficParamIndex_Type(Integer32):
    """Custom type hpnicfmplsTrafficParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfmplsTrafficParamIndex_Type.__name__ = "Integer32"
_HpnicfmplsTrafficParamIndex_Object = MibTableColumn
hpnicfmplsTrafficParamIndex = _HpnicfmplsTrafficParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 1),
    _HpnicfmplsTrafficParamIndex_Type()
)
hpnicfmplsTrafficParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamIndex.setStatus("current")
_HpnicfmplsTrafficParamMaxRate_Type = HpnicfMplsBitRate
_HpnicfmplsTrafficParamMaxRate_Object = MibTableColumn
hpnicfmplsTrafficParamMaxRate = _HpnicfmplsTrafficParamMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 2),
    _HpnicfmplsTrafficParamMaxRate_Type()
)
hpnicfmplsTrafficParamMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMaxRate.setUnits("kilobits per second")
_HpnicfmplsTrafficParamMeanRate_Type = HpnicfMplsBitRate
_HpnicfmplsTrafficParamMeanRate_Object = MibTableColumn
hpnicfmplsTrafficParamMeanRate = _HpnicfmplsTrafficParamMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 3),
    _HpnicfmplsTrafficParamMeanRate_Type()
)
hpnicfmplsTrafficParamMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMeanRate.setUnits("kilobits per second")
_HpnicfmplsTrafficParamMaxBurstSize_Type = HpnicfMplsBurstSize
_HpnicfmplsTrafficParamMaxBurstSize_Object = MibTableColumn
hpnicfmplsTrafficParamMaxBurstSize = _HpnicfmplsTrafficParamMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 4),
    _HpnicfmplsTrafficParamMaxBurstSize_Type()
)
hpnicfmplsTrafficParamMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamMaxBurstSize.setUnits("bytes")
_HpnicfmplsTrafficParamRowStatus_Type = RowStatus
_HpnicfmplsTrafficParamRowStatus_Object = MibTableColumn
hpnicfmplsTrafficParamRowStatus = _HpnicfmplsTrafficParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 5),
    _HpnicfmplsTrafficParamRowStatus_Type()
)
hpnicfmplsTrafficParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamRowStatus.setStatus("current")
_HpnicfmplsTrafficParamStorageType_Type = StorageType
_HpnicfmplsTrafficParamStorageType_Object = MibTableColumn
hpnicfmplsTrafficParamStorageType = _HpnicfmplsTrafficParamStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 14, 1, 6),
    _HpnicfmplsTrafficParamStorageType_Type()
)
hpnicfmplsTrafficParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamStorageType.setStatus("current")


class _HpnicfmplsXCTrapEnable_Type(TruthValue):
    """Custom type hpnicfmplsXCTrapEnable based on TruthValue"""


_HpnicfmplsXCTrapEnable_Object = MibScalar
hpnicfmplsXCTrapEnable = _HpnicfmplsXCTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 1, 15),
    _HpnicfmplsXCTrapEnable_Type()
)
hpnicfmplsXCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfmplsXCTrapEnable.setStatus("current")
_HpnicfmplsLsrNotifications_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrNotifications = _HpnicfmplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 2)
)
_HpnicfmplsLsrNotifyPrefix_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrNotifyPrefix = _HpnicfmplsLsrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 2, 0)
)
_HpnicfmplsLsrConformance_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrConformance = _HpnicfmplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3)
)
_HpnicfmplsLsrGroups_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrGroups = _HpnicfmplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1)
)
_HpnicfmplsLsrCompliances_ObjectIdentity = ObjectIdentity
hpnicfmplsLsrCompliances = _HpnicfmplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 2)
)
hpnicfmplsInterfaceConfEntry.registerAugmentions(
    ("HPN-ICF-MPLS-LSR-MIB",
     "hpnicfmplsInterfacePerfEntry")
)
hpnicfmplsInterfacePerfEntry.setIndexNames(*hpnicfmplsInterfaceConfEntry.getIndexNames())
hpnicfmplsInSegmentEntry.registerAugmentions(
    ("HPN-ICF-MPLS-LSR-MIB",
     "hpnicfmplsInSegmentPerfEntry")
)
hpnicfmplsInSegmentPerfEntry.setIndexNames(*hpnicfmplsInSegmentEntry.getIndexNames())
hpnicfmplsOutSegmentEntry.registerAugmentions(
    ("HPN-ICF-MPLS-LSR-MIB",
     "hpnicfmplsOutSegmentPerfEntry")
)
hpnicfmplsOutSegmentPerfEntry.setIndexNames(*hpnicfmplsOutSegmentEntry.getIndexNames())

# Managed Objects groups

hpnicfmplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 1)
)
hpnicfmplsInterfaceGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceLabelMinIn"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceLabelMaxIn"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceLabelMinOut"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceLabelMaxOut"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceTotalBandwidth"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceAvailableBandwidth"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceLabelParticipationType"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceConfStorageType"))
)
if mibBuilder.loadTexts:
    hpnicfmplsInterfaceGroup.setStatus("current")

hpnicfmplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 2)
)
hpnicfmplsInSegmentGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentNPop"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentAddrFamily"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentXCIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentOctets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentDiscards"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentOwner"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentRowStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentStorageType"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    hpnicfmplsInSegmentGroup.setStatus("current")

hpnicfmplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 3)
)
hpnicfmplsOutSegmentGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIndexNext"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIfIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentPushTopLabel"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentTopLabel"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentNextHopIpAddrType"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentNextHopIpv4Addr"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentNextHopIpv6Addr"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentXCIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentOwner"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentOctets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentDiscards"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentErrors"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentRowStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentStorageType"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    hpnicfmplsOutSegmentGroup.setStatus("current")

hpnicfmplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 4)
)
hpnicfmplsXCGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIndexNext"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCLabelStackIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCOwner"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCAdminStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCOperStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCRowStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCTrapEnable"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCStorageType"))
)
if mibBuilder.loadTexts:
    hpnicfmplsXCGroup.setStatus("current")

hpnicfmplsXCOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 5)
)
hpnicfmplsXCOptionalGroup.setObjects(
    ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCLspId")
)
if mibBuilder.loadTexts:
    hpnicfmplsXCOptionalGroup.setStatus("current")

hpnicfmplsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 6)
)
hpnicfmplsPerfGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentOctets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentPackets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentErrors"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentDiscards"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentOctets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentPackets"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentDiscards"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceInLabelsUsed"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceFailedLabelLookup"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceOutFragments"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInterfaceOutLabelsUsed"))
)
if mibBuilder.loadTexts:
    hpnicfmplsPerfGroup.setStatus("current")

hpnicfmplsHCInSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 7)
)
hpnicfmplsHCInSegmentPerfGroup.setObjects(
    ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentHCOctets")
)
if mibBuilder.loadTexts:
    hpnicfmplsHCInSegmentPerfGroup.setStatus("current")

hpnicfmplsHCOutSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 8)
)
hpnicfmplsHCOutSegmentPerfGroup.setObjects(
    ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentHCOctets")
)
if mibBuilder.loadTexts:
    hpnicfmplsHCOutSegmentPerfGroup.setStatus("current")

hpnicfmplsTrafficParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 9)
)
hpnicfmplsTrafficParamGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamIndexNext"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamMaxRate"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamMeanRate"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamMaxBurstSize"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamRowStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsTrafficParamStorageType"))
)
if mibBuilder.loadTexts:
    hpnicfmplsTrafficParamGroup.setStatus("current")

hpnicfmplsXCIsPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 10)
)
hpnicfmplsXCIsPersistentGroup.setObjects(
    ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    hpnicfmplsXCIsPersistentGroup.setStatus("current")

hpnicfmplsXCIsNotPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 11)
)
hpnicfmplsXCIsNotPersistentGroup.setObjects(
    ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    hpnicfmplsXCIsNotPersistentGroup.setStatus("current")

hpnicfmplsLabelStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 12)
)
hpnicfmplsLabelStackGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackLabel"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackRowStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackStorageType"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsMaxLabelStackDepth"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsLabelStackIndexNext"))
)
if mibBuilder.loadTexts:
    hpnicfmplsLabelStackGroup.setStatus("current")

hpnicfmplsSegmentDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 13)
)
hpnicfmplsSegmentDiscontinuityGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentPerfDiscontinuityTime"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    hpnicfmplsSegmentDiscontinuityGroup.setStatus("current")


# Notification objects

hpnicfmplsXCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 2, 0, 1)
)
hpnicfmplsXCUp.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentIfIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentLabel"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCAdminStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    hpnicfmplsXCUp.setStatus(
        "current"
    )

hpnicfmplsXCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 2, 0, 2)
)
hpnicfmplsXCDown.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentIfIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsInSegmentLabel"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsOutSegmentIndex"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCAdminStatus"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    hpnicfmplsXCDown.setStatus(
        "current"
    )


# Notifications groups

hpnicfmplsLsrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 1, 14)
)
hpnicfmplsLsrNotificationGroup.setObjects(
      *(("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCUp"),
        ("HPN-ICF-MPLS-LSR-MIB", "hpnicfmplsXCDown"))
)
if mibBuilder.loadTexts:
    hpnicfmplsLsrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfmplsLsrModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsLsrModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLS-LSR-MIB",
    **{"HpnicfMplsLSPID": HpnicfMplsLSPID,
       "HpnicfMplsLabel": HpnicfMplsLabel,
       "HpnicfMplsBitRate": HpnicfMplsBitRate,
       "HpnicfMplsBurstSize": HpnicfMplsBurstSize,
       "HpnicfMplsObjectOwner": HpnicfMplsObjectOwner,
       "hpnicfMplsLsr": hpnicfMplsLsr,
       "hpnicfmplsLsrObjects": hpnicfmplsLsrObjects,
       "hpnicfmplsInterfaceConfTable": hpnicfmplsInterfaceConfTable,
       "hpnicfmplsInterfaceConfEntry": hpnicfmplsInterfaceConfEntry,
       "hpnicfmplsInterfaceConfIndex": hpnicfmplsInterfaceConfIndex,
       "hpnicfmplsInterfaceLabelMinIn": hpnicfmplsInterfaceLabelMinIn,
       "hpnicfmplsInterfaceLabelMaxIn": hpnicfmplsInterfaceLabelMaxIn,
       "hpnicfmplsInterfaceLabelMinOut": hpnicfmplsInterfaceLabelMinOut,
       "hpnicfmplsInterfaceLabelMaxOut": hpnicfmplsInterfaceLabelMaxOut,
       "hpnicfmplsInterfaceTotalBandwidth": hpnicfmplsInterfaceTotalBandwidth,
       "hpnicfmplsInterfaceAvailableBandwidth": hpnicfmplsInterfaceAvailableBandwidth,
       "hpnicfmplsInterfaceLabelParticipationType": hpnicfmplsInterfaceLabelParticipationType,
       "hpnicfmplsInterfaceConfStorageType": hpnicfmplsInterfaceConfStorageType,
       "hpnicfmplsInterfacePerfTable": hpnicfmplsInterfacePerfTable,
       "hpnicfmplsInterfacePerfEntry": hpnicfmplsInterfacePerfEntry,
       "hpnicfmplsInterfaceInLabelsUsed": hpnicfmplsInterfaceInLabelsUsed,
       "hpnicfmplsInterfaceFailedLabelLookup": hpnicfmplsInterfaceFailedLabelLookup,
       "hpnicfmplsInterfaceOutLabelsUsed": hpnicfmplsInterfaceOutLabelsUsed,
       "hpnicfmplsInterfaceOutFragments": hpnicfmplsInterfaceOutFragments,
       "hpnicfmplsInSegmentTable": hpnicfmplsInSegmentTable,
       "hpnicfmplsInSegmentEntry": hpnicfmplsInSegmentEntry,
       "hpnicfmplsInSegmentIfIndex": hpnicfmplsInSegmentIfIndex,
       "hpnicfmplsInSegmentLabel": hpnicfmplsInSegmentLabel,
       "hpnicfmplsInSegmentNPop": hpnicfmplsInSegmentNPop,
       "hpnicfmplsInSegmentAddrFamily": hpnicfmplsInSegmentAddrFamily,
       "hpnicfmplsInSegmentXCIndex": hpnicfmplsInSegmentXCIndex,
       "hpnicfmplsInSegmentOwner": hpnicfmplsInSegmentOwner,
       "hpnicfmplsInSegmentTrafficParamPtr": hpnicfmplsInSegmentTrafficParamPtr,
       "hpnicfmplsInSegmentRowStatus": hpnicfmplsInSegmentRowStatus,
       "hpnicfmplsInSegmentStorageType": hpnicfmplsInSegmentStorageType,
       "hpnicfmplsInSegmentPerfTable": hpnicfmplsInSegmentPerfTable,
       "hpnicfmplsInSegmentPerfEntry": hpnicfmplsInSegmentPerfEntry,
       "hpnicfmplsInSegmentOctets": hpnicfmplsInSegmentOctets,
       "hpnicfmplsInSegmentPackets": hpnicfmplsInSegmentPackets,
       "hpnicfmplsInSegmentErrors": hpnicfmplsInSegmentErrors,
       "hpnicfmplsInSegmentDiscards": hpnicfmplsInSegmentDiscards,
       "hpnicfmplsInSegmentHCOctets": hpnicfmplsInSegmentHCOctets,
       "hpnicfmplsInSegmentPerfDiscontinuityTime": hpnicfmplsInSegmentPerfDiscontinuityTime,
       "hpnicfmplsOutSegmentIndexNext": hpnicfmplsOutSegmentIndexNext,
       "hpnicfmplsOutSegmentTable": hpnicfmplsOutSegmentTable,
       "hpnicfmplsOutSegmentEntry": hpnicfmplsOutSegmentEntry,
       "hpnicfmplsOutSegmentIndex": hpnicfmplsOutSegmentIndex,
       "hpnicfmplsOutSegmentIfIndex": hpnicfmplsOutSegmentIfIndex,
       "hpnicfmplsOutSegmentPushTopLabel": hpnicfmplsOutSegmentPushTopLabel,
       "hpnicfmplsOutSegmentTopLabel": hpnicfmplsOutSegmentTopLabel,
       "hpnicfmplsOutSegmentNextHopIpAddrType": hpnicfmplsOutSegmentNextHopIpAddrType,
       "hpnicfmplsOutSegmentNextHopIpv4Addr": hpnicfmplsOutSegmentNextHopIpv4Addr,
       "hpnicfmplsOutSegmentNextHopIpv6Addr": hpnicfmplsOutSegmentNextHopIpv6Addr,
       "hpnicfmplsOutSegmentXCIndex": hpnicfmplsOutSegmentXCIndex,
       "hpnicfmplsOutSegmentOwner": hpnicfmplsOutSegmentOwner,
       "hpnicfmplsOutSegmentTrafficParamPtr": hpnicfmplsOutSegmentTrafficParamPtr,
       "hpnicfmplsOutSegmentRowStatus": hpnicfmplsOutSegmentRowStatus,
       "hpnicfmplsOutSegmentStorageType": hpnicfmplsOutSegmentStorageType,
       "hpnicfmplsOutSegmentPerfTable": hpnicfmplsOutSegmentPerfTable,
       "hpnicfmplsOutSegmentPerfEntry": hpnicfmplsOutSegmentPerfEntry,
       "hpnicfmplsOutSegmentOctets": hpnicfmplsOutSegmentOctets,
       "hpnicfmplsOutSegmentPackets": hpnicfmplsOutSegmentPackets,
       "hpnicfmplsOutSegmentErrors": hpnicfmplsOutSegmentErrors,
       "hpnicfmplsOutSegmentDiscards": hpnicfmplsOutSegmentDiscards,
       "hpnicfmplsOutSegmentHCOctets": hpnicfmplsOutSegmentHCOctets,
       "hpnicfmplsOutSegmentPerfDiscontinuityTime": hpnicfmplsOutSegmentPerfDiscontinuityTime,
       "hpnicfmplsXCIndexNext": hpnicfmplsXCIndexNext,
       "hpnicfmplsXCTable": hpnicfmplsXCTable,
       "hpnicfmplsXCEntry": hpnicfmplsXCEntry,
       "hpnicfmplsXCIndex": hpnicfmplsXCIndex,
       "hpnicfmplsXCLspId": hpnicfmplsXCLspId,
       "hpnicfmplsXCLabelStackIndex": hpnicfmplsXCLabelStackIndex,
       "hpnicfmplsXCIsPersistent": hpnicfmplsXCIsPersistent,
       "hpnicfmplsXCOwner": hpnicfmplsXCOwner,
       "hpnicfmplsXCRowStatus": hpnicfmplsXCRowStatus,
       "hpnicfmplsXCStorageType": hpnicfmplsXCStorageType,
       "hpnicfmplsXCAdminStatus": hpnicfmplsXCAdminStatus,
       "hpnicfmplsXCOperStatus": hpnicfmplsXCOperStatus,
       "hpnicfmplsMaxLabelStackDepth": hpnicfmplsMaxLabelStackDepth,
       "hpnicfmplsLabelStackIndexNext": hpnicfmplsLabelStackIndexNext,
       "hpnicfmplsLabelStackTable": hpnicfmplsLabelStackTable,
       "hpnicfmplsLabelStackEntry": hpnicfmplsLabelStackEntry,
       "hpnicfmplsLabelStackIndex": hpnicfmplsLabelStackIndex,
       "hpnicfmplsLabelStackLabelIndex": hpnicfmplsLabelStackLabelIndex,
       "hpnicfmplsLabelStackLabel": hpnicfmplsLabelStackLabel,
       "hpnicfmplsLabelStackRowStatus": hpnicfmplsLabelStackRowStatus,
       "hpnicfmplsLabelStackStorageType": hpnicfmplsLabelStackStorageType,
       "hpnicfmplsTrafficParamIndexNext": hpnicfmplsTrafficParamIndexNext,
       "hpnicfmplsTrafficParamTable": hpnicfmplsTrafficParamTable,
       "hpnicfmplsTrafficParamEntry": hpnicfmplsTrafficParamEntry,
       "hpnicfmplsTrafficParamIndex": hpnicfmplsTrafficParamIndex,
       "hpnicfmplsTrafficParamMaxRate": hpnicfmplsTrafficParamMaxRate,
       "hpnicfmplsTrafficParamMeanRate": hpnicfmplsTrafficParamMeanRate,
       "hpnicfmplsTrafficParamMaxBurstSize": hpnicfmplsTrafficParamMaxBurstSize,
       "hpnicfmplsTrafficParamRowStatus": hpnicfmplsTrafficParamRowStatus,
       "hpnicfmplsTrafficParamStorageType": hpnicfmplsTrafficParamStorageType,
       "hpnicfmplsXCTrapEnable": hpnicfmplsXCTrapEnable,
       "hpnicfmplsLsrNotifications": hpnicfmplsLsrNotifications,
       "hpnicfmplsLsrNotifyPrefix": hpnicfmplsLsrNotifyPrefix,
       "hpnicfmplsXCUp": hpnicfmplsXCUp,
       "hpnicfmplsXCDown": hpnicfmplsXCDown,
       "hpnicfmplsLsrConformance": hpnicfmplsLsrConformance,
       "hpnicfmplsLsrGroups": hpnicfmplsLsrGroups,
       "hpnicfmplsInterfaceGroup": hpnicfmplsInterfaceGroup,
       "hpnicfmplsInSegmentGroup": hpnicfmplsInSegmentGroup,
       "hpnicfmplsOutSegmentGroup": hpnicfmplsOutSegmentGroup,
       "hpnicfmplsXCGroup": hpnicfmplsXCGroup,
       "hpnicfmplsXCOptionalGroup": hpnicfmplsXCOptionalGroup,
       "hpnicfmplsPerfGroup": hpnicfmplsPerfGroup,
       "hpnicfmplsHCInSegmentPerfGroup": hpnicfmplsHCInSegmentPerfGroup,
       "hpnicfmplsHCOutSegmentPerfGroup": hpnicfmplsHCOutSegmentPerfGroup,
       "hpnicfmplsTrafficParamGroup": hpnicfmplsTrafficParamGroup,
       "hpnicfmplsXCIsPersistentGroup": hpnicfmplsXCIsPersistentGroup,
       "hpnicfmplsXCIsNotPersistentGroup": hpnicfmplsXCIsNotPersistentGroup,
       "hpnicfmplsLabelStackGroup": hpnicfmplsLabelStackGroup,
       "hpnicfmplsSegmentDiscontinuityGroup": hpnicfmplsSegmentDiscontinuityGroup,
       "hpnicfmplsLsrNotificationGroup": hpnicfmplsLsrNotificationGroup,
       "hpnicfmplsLsrCompliances": hpnicfmplsLsrCompliances,
       "hpnicfmplsLsrModuleCompliance": hpnicfmplsLsrModuleCompliance}
)
