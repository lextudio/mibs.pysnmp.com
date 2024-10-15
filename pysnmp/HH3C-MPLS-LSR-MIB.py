# SNMP MIB module (HH3C-MPLS-LSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLS-LSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:11 2024
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

(hh3cMpls,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cMpls")

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

hh3cMplsLsr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1)
)
hh3cMplsLsr.setRevisions(
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



class Hh3cMplsLSPID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class Hh3cMplsLabel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Hh3cMplsBitRate(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Hh3cMplsBurstSize(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Hh3cMplsObjectOwner(Integer32, TextualConvention):
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

_Hh3cmplsLsrObjects_ObjectIdentity = ObjectIdentity
hh3cmplsLsrObjects = _Hh3cmplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1)
)
_Hh3cmplsInterfaceConfTable_Object = MibTable
hh3cmplsInterfaceConfTable = _Hh3cmplsInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsInterfaceConfTable.setStatus("current")
_Hh3cmplsInterfaceConfEntry_Object = MibTableRow
hh3cmplsInterfaceConfEntry = _Hh3cmplsInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1)
)
hh3cmplsInterfaceConfEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsInterfaceConfEntry.setStatus("current")
_Hh3cmplsInterfaceConfIndex_Type = InterfaceIndexOrZero
_Hh3cmplsInterfaceConfIndex_Object = MibTableColumn
hh3cmplsInterfaceConfIndex = _Hh3cmplsInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 1),
    _Hh3cmplsInterfaceConfIndex_Type()
)
hh3cmplsInterfaceConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceConfIndex.setStatus("current")
_Hh3cmplsInterfaceLabelMinIn_Type = Hh3cMplsLabel
_Hh3cmplsInterfaceLabelMinIn_Object = MibTableColumn
hh3cmplsInterfaceLabelMinIn = _Hh3cmplsInterfaceLabelMinIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 2),
    _Hh3cmplsInterfaceLabelMinIn_Type()
)
hh3cmplsInterfaceLabelMinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceLabelMinIn.setStatus("current")
_Hh3cmplsInterfaceLabelMaxIn_Type = Hh3cMplsLabel
_Hh3cmplsInterfaceLabelMaxIn_Object = MibTableColumn
hh3cmplsInterfaceLabelMaxIn = _Hh3cmplsInterfaceLabelMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 3),
    _Hh3cmplsInterfaceLabelMaxIn_Type()
)
hh3cmplsInterfaceLabelMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceLabelMaxIn.setStatus("current")
_Hh3cmplsInterfaceLabelMinOut_Type = Hh3cMplsLabel
_Hh3cmplsInterfaceLabelMinOut_Object = MibTableColumn
hh3cmplsInterfaceLabelMinOut = _Hh3cmplsInterfaceLabelMinOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 4),
    _Hh3cmplsInterfaceLabelMinOut_Type()
)
hh3cmplsInterfaceLabelMinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceLabelMinOut.setStatus("current")
_Hh3cmplsInterfaceLabelMaxOut_Type = Hh3cMplsLabel
_Hh3cmplsInterfaceLabelMaxOut_Object = MibTableColumn
hh3cmplsInterfaceLabelMaxOut = _Hh3cmplsInterfaceLabelMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 5),
    _Hh3cmplsInterfaceLabelMaxOut_Type()
)
hh3cmplsInterfaceLabelMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceLabelMaxOut.setStatus("current")
_Hh3cmplsInterfaceTotalBandwidth_Type = Hh3cMplsBitRate
_Hh3cmplsInterfaceTotalBandwidth_Object = MibTableColumn
hh3cmplsInterfaceTotalBandwidth = _Hh3cmplsInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 6),
    _Hh3cmplsInterfaceTotalBandwidth_Type()
)
hh3cmplsInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceTotalBandwidth.setStatus("current")
_Hh3cmplsInterfaceAvailableBandwidth_Type = Hh3cMplsBitRate
_Hh3cmplsInterfaceAvailableBandwidth_Object = MibTableColumn
hh3cmplsInterfaceAvailableBandwidth = _Hh3cmplsInterfaceAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 7),
    _Hh3cmplsInterfaceAvailableBandwidth_Type()
)
hh3cmplsInterfaceAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceAvailableBandwidth.setStatus("current")


class _Hh3cmplsInterfaceLabelParticipationType_Type(Bits):
    """Custom type hh3cmplsInterfaceLabelParticipationType based on Bits"""
    namedValues = NamedValues(
        *(("perInterface", 1),
          ("perPlatform", 0))
    )

_Hh3cmplsInterfaceLabelParticipationType_Type.__name__ = "Bits"
_Hh3cmplsInterfaceLabelParticipationType_Object = MibTableColumn
hh3cmplsInterfaceLabelParticipationType = _Hh3cmplsInterfaceLabelParticipationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 8),
    _Hh3cmplsInterfaceLabelParticipationType_Type()
)
hh3cmplsInterfaceLabelParticipationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceLabelParticipationType.setStatus("current")
_Hh3cmplsInterfaceConfStorageType_Type = StorageType
_Hh3cmplsInterfaceConfStorageType_Object = MibTableColumn
hh3cmplsInterfaceConfStorageType = _Hh3cmplsInterfaceConfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 1, 1, 9),
    _Hh3cmplsInterfaceConfStorageType_Type()
)
hh3cmplsInterfaceConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceConfStorageType.setStatus("current")
_Hh3cmplsInterfacePerfTable_Object = MibTable
hh3cmplsInterfacePerfTable = _Hh3cmplsInterfacePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cmplsInterfacePerfTable.setStatus("current")
_Hh3cmplsInterfacePerfEntry_Object = MibTableRow
hh3cmplsInterfacePerfEntry = _Hh3cmplsInterfacePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsInterfacePerfEntry.setStatus("current")
_Hh3cmplsInterfaceInLabelsUsed_Type = Gauge32
_Hh3cmplsInterfaceInLabelsUsed_Object = MibTableColumn
hh3cmplsInterfaceInLabelsUsed = _Hh3cmplsInterfaceInLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2, 1, 1),
    _Hh3cmplsInterfaceInLabelsUsed_Type()
)
hh3cmplsInterfaceInLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceInLabelsUsed.setStatus("current")
_Hh3cmplsInterfaceFailedLabelLookup_Type = Counter32
_Hh3cmplsInterfaceFailedLabelLookup_Object = MibTableColumn
hh3cmplsInterfaceFailedLabelLookup = _Hh3cmplsInterfaceFailedLabelLookup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2, 1, 2),
    _Hh3cmplsInterfaceFailedLabelLookup_Type()
)
hh3cmplsInterfaceFailedLabelLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceFailedLabelLookup.setStatus("current")
_Hh3cmplsInterfaceOutLabelsUsed_Type = Gauge32
_Hh3cmplsInterfaceOutLabelsUsed_Object = MibTableColumn
hh3cmplsInterfaceOutLabelsUsed = _Hh3cmplsInterfaceOutLabelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2, 1, 3),
    _Hh3cmplsInterfaceOutLabelsUsed_Type()
)
hh3cmplsInterfaceOutLabelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceOutLabelsUsed.setStatus("current")
_Hh3cmplsInterfaceOutFragments_Type = Counter32
_Hh3cmplsInterfaceOutFragments_Object = MibTableColumn
hh3cmplsInterfaceOutFragments = _Hh3cmplsInterfaceOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 2, 1, 4),
    _Hh3cmplsInterfaceOutFragments_Type()
)
hh3cmplsInterfaceOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInterfaceOutFragments.setStatus("current")
_Hh3cmplsInSegmentTable_Object = MibTable
hh3cmplsInSegmentTable = _Hh3cmplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cmplsInSegmentTable.setStatus("current")
_Hh3cmplsInSegmentEntry_Object = MibTableRow
hh3cmplsInSegmentEntry = _Hh3cmplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1)
)
hh3cmplsInSegmentEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentIfIndex"),
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentLabel"),
)
if mibBuilder.loadTexts:
    hh3cmplsInSegmentEntry.setStatus("current")
_Hh3cmplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_Hh3cmplsInSegmentIfIndex_Object = MibTableColumn
hh3cmplsInSegmentIfIndex = _Hh3cmplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 1),
    _Hh3cmplsInSegmentIfIndex_Type()
)
hh3cmplsInSegmentIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentIfIndex.setStatus("current")
_Hh3cmplsInSegmentLabel_Type = Hh3cMplsLabel
_Hh3cmplsInSegmentLabel_Object = MibTableColumn
hh3cmplsInSegmentLabel = _Hh3cmplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 2),
    _Hh3cmplsInSegmentLabel_Type()
)
hh3cmplsInSegmentLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentLabel.setStatus("current")


class _Hh3cmplsInSegmentNPop_Type(Integer32):
    """Custom type hh3cmplsInSegmentNPop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsInSegmentNPop_Type.__name__ = "Integer32"
_Hh3cmplsInSegmentNPop_Object = MibTableColumn
hh3cmplsInSegmentNPop = _Hh3cmplsInSegmentNPop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 3),
    _Hh3cmplsInSegmentNPop_Type()
)
hh3cmplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentNPop.setStatus("current")


class _Hh3cmplsInSegmentAddrFamily_Type(AddressFamilyNumbers):
    """Custom type hh3cmplsInSegmentAddrFamily based on AddressFamilyNumbers"""


_Hh3cmplsInSegmentAddrFamily_Object = MibTableColumn
hh3cmplsInSegmentAddrFamily = _Hh3cmplsInSegmentAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 4),
    _Hh3cmplsInSegmentAddrFamily_Type()
)
hh3cmplsInSegmentAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentAddrFamily.setStatus("current")


class _Hh3cmplsInSegmentXCIndex_Type(Integer32):
    """Custom type hh3cmplsInSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsInSegmentXCIndex_Type.__name__ = "Integer32"
_Hh3cmplsInSegmentXCIndex_Object = MibTableColumn
hh3cmplsInSegmentXCIndex = _Hh3cmplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 5),
    _Hh3cmplsInSegmentXCIndex_Type()
)
hh3cmplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentXCIndex.setStatus("current")


class _Hh3cmplsInSegmentOwner_Type(Hh3cMplsObjectOwner):
    """Custom type hh3cmplsInSegmentOwner based on Hh3cMplsObjectOwner"""


_Hh3cmplsInSegmentOwner_Object = MibTableColumn
hh3cmplsInSegmentOwner = _Hh3cmplsInSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 6),
    _Hh3cmplsInSegmentOwner_Type()
)
hh3cmplsInSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentOwner.setStatus("current")
_Hh3cmplsInSegmentTrafficParamPtr_Type = RowPointer
_Hh3cmplsInSegmentTrafficParamPtr_Object = MibTableColumn
hh3cmplsInSegmentTrafficParamPtr = _Hh3cmplsInSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 7),
    _Hh3cmplsInSegmentTrafficParamPtr_Type()
)
hh3cmplsInSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentTrafficParamPtr.setStatus("current")
_Hh3cmplsInSegmentRowStatus_Type = RowStatus
_Hh3cmplsInSegmentRowStatus_Object = MibTableColumn
hh3cmplsInSegmentRowStatus = _Hh3cmplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 8),
    _Hh3cmplsInSegmentRowStatus_Type()
)
hh3cmplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentRowStatus.setStatus("current")
_Hh3cmplsInSegmentStorageType_Type = StorageType
_Hh3cmplsInSegmentStorageType_Object = MibTableColumn
hh3cmplsInSegmentStorageType = _Hh3cmplsInSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 3, 1, 9),
    _Hh3cmplsInSegmentStorageType_Type()
)
hh3cmplsInSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentStorageType.setStatus("current")
_Hh3cmplsInSegmentPerfTable_Object = MibTable
hh3cmplsInSegmentPerfTable = _Hh3cmplsInSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cmplsInSegmentPerfTable.setStatus("current")
_Hh3cmplsInSegmentPerfEntry_Object = MibTableRow
hh3cmplsInSegmentPerfEntry = _Hh3cmplsInSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsInSegmentPerfEntry.setStatus("current")
_Hh3cmplsInSegmentOctets_Type = Counter32
_Hh3cmplsInSegmentOctets_Object = MibTableColumn
hh3cmplsInSegmentOctets = _Hh3cmplsInSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 1),
    _Hh3cmplsInSegmentOctets_Type()
)
hh3cmplsInSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentOctets.setStatus("current")
_Hh3cmplsInSegmentPackets_Type = Counter32
_Hh3cmplsInSegmentPackets_Object = MibTableColumn
hh3cmplsInSegmentPackets = _Hh3cmplsInSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 2),
    _Hh3cmplsInSegmentPackets_Type()
)
hh3cmplsInSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentPackets.setStatus("current")
_Hh3cmplsInSegmentErrors_Type = Counter32
_Hh3cmplsInSegmentErrors_Object = MibTableColumn
hh3cmplsInSegmentErrors = _Hh3cmplsInSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 3),
    _Hh3cmplsInSegmentErrors_Type()
)
hh3cmplsInSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentErrors.setStatus("current")
_Hh3cmplsInSegmentDiscards_Type = Counter32
_Hh3cmplsInSegmentDiscards_Object = MibTableColumn
hh3cmplsInSegmentDiscards = _Hh3cmplsInSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 4),
    _Hh3cmplsInSegmentDiscards_Type()
)
hh3cmplsInSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentDiscards.setStatus("current")
_Hh3cmplsInSegmentHCOctets_Type = Counter64
_Hh3cmplsInSegmentHCOctets_Object = MibTableColumn
hh3cmplsInSegmentHCOctets = _Hh3cmplsInSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 5),
    _Hh3cmplsInSegmentHCOctets_Type()
)
hh3cmplsInSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentHCOctets.setStatus("current")
_Hh3cmplsInSegmentPerfDiscontinuityTime_Type = TimeStamp
_Hh3cmplsInSegmentPerfDiscontinuityTime_Object = MibTableColumn
hh3cmplsInSegmentPerfDiscontinuityTime = _Hh3cmplsInSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 4, 1, 6),
    _Hh3cmplsInSegmentPerfDiscontinuityTime_Type()
)
hh3cmplsInSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsInSegmentPerfDiscontinuityTime.setStatus("current")


class _Hh3cmplsOutSegmentIndexNext_Type(Integer32):
    """Custom type hh3cmplsOutSegmentIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsOutSegmentIndexNext_Type.__name__ = "Integer32"
_Hh3cmplsOutSegmentIndexNext_Object = MibScalar
hh3cmplsOutSegmentIndexNext = _Hh3cmplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 5),
    _Hh3cmplsOutSegmentIndexNext_Type()
)
hh3cmplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentIndexNext.setStatus("current")
_Hh3cmplsOutSegmentTable_Object = MibTable
hh3cmplsOutSegmentTable = _Hh3cmplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentTable.setStatus("current")
_Hh3cmplsOutSegmentEntry_Object = MibTableRow
hh3cmplsOutSegmentEntry = _Hh3cmplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1)
)
hh3cmplsOutSegmentEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentEntry.setStatus("current")


class _Hh3cmplsOutSegmentIndex_Type(Integer32):
    """Custom type hh3cmplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsOutSegmentIndex_Type.__name__ = "Integer32"
_Hh3cmplsOutSegmentIndex_Object = MibTableColumn
hh3cmplsOutSegmentIndex = _Hh3cmplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 1),
    _Hh3cmplsOutSegmentIndex_Type()
)
hh3cmplsOutSegmentIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentIndex.setStatus("current")
_Hh3cmplsOutSegmentIfIndex_Type = InterfaceIndex
_Hh3cmplsOutSegmentIfIndex_Object = MibTableColumn
hh3cmplsOutSegmentIfIndex = _Hh3cmplsOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 2),
    _Hh3cmplsOutSegmentIfIndex_Type()
)
hh3cmplsOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentIfIndex.setStatus("current")
_Hh3cmplsOutSegmentPushTopLabel_Type = TruthValue
_Hh3cmplsOutSegmentPushTopLabel_Object = MibTableColumn
hh3cmplsOutSegmentPushTopLabel = _Hh3cmplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 3),
    _Hh3cmplsOutSegmentPushTopLabel_Type()
)
hh3cmplsOutSegmentPushTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentPushTopLabel.setStatus("current")
_Hh3cmplsOutSegmentTopLabel_Type = Hh3cMplsLabel
_Hh3cmplsOutSegmentTopLabel_Object = MibTableColumn
hh3cmplsOutSegmentTopLabel = _Hh3cmplsOutSegmentTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 4),
    _Hh3cmplsOutSegmentTopLabel_Type()
)
hh3cmplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentTopLabel.setStatus("current")


class _Hh3cmplsOutSegmentNextHopIpAddrType_Type(InetAddressType):
    """Custom type hh3cmplsOutSegmentNextHopIpAddrType based on InetAddressType"""


_Hh3cmplsOutSegmentNextHopIpAddrType_Object = MibTableColumn
hh3cmplsOutSegmentNextHopIpAddrType = _Hh3cmplsOutSegmentNextHopIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 5),
    _Hh3cmplsOutSegmentNextHopIpAddrType_Type()
)
hh3cmplsOutSegmentNextHopIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentNextHopIpAddrType.setStatus("current")
_Hh3cmplsOutSegmentNextHopIpv4Addr_Type = InetAddressIPv4
_Hh3cmplsOutSegmentNextHopIpv4Addr_Object = MibTableColumn
hh3cmplsOutSegmentNextHopIpv4Addr = _Hh3cmplsOutSegmentNextHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 6),
    _Hh3cmplsOutSegmentNextHopIpv4Addr_Type()
)
hh3cmplsOutSegmentNextHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentNextHopIpv4Addr.setStatus("current")
_Hh3cmplsOutSegmentNextHopIpv6Addr_Type = InetAddressIPv6
_Hh3cmplsOutSegmentNextHopIpv6Addr_Object = MibTableColumn
hh3cmplsOutSegmentNextHopIpv6Addr = _Hh3cmplsOutSegmentNextHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 7),
    _Hh3cmplsOutSegmentNextHopIpv6Addr_Type()
)
hh3cmplsOutSegmentNextHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentNextHopIpv6Addr.setStatus("current")


class _Hh3cmplsOutSegmentXCIndex_Type(Integer32):
    """Custom type hh3cmplsOutSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsOutSegmentXCIndex_Type.__name__ = "Integer32"
_Hh3cmplsOutSegmentXCIndex_Object = MibTableColumn
hh3cmplsOutSegmentXCIndex = _Hh3cmplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 8),
    _Hh3cmplsOutSegmentXCIndex_Type()
)
hh3cmplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentXCIndex.setStatus("current")


class _Hh3cmplsOutSegmentOwner_Type(Hh3cMplsObjectOwner):
    """Custom type hh3cmplsOutSegmentOwner based on Hh3cMplsObjectOwner"""


_Hh3cmplsOutSegmentOwner_Object = MibTableColumn
hh3cmplsOutSegmentOwner = _Hh3cmplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 9),
    _Hh3cmplsOutSegmentOwner_Type()
)
hh3cmplsOutSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentOwner.setStatus("current")
_Hh3cmplsOutSegmentTrafficParamPtr_Type = RowPointer
_Hh3cmplsOutSegmentTrafficParamPtr_Object = MibTableColumn
hh3cmplsOutSegmentTrafficParamPtr = _Hh3cmplsOutSegmentTrafficParamPtr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 10),
    _Hh3cmplsOutSegmentTrafficParamPtr_Type()
)
hh3cmplsOutSegmentTrafficParamPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentTrafficParamPtr.setStatus("current")
_Hh3cmplsOutSegmentRowStatus_Type = RowStatus
_Hh3cmplsOutSegmentRowStatus_Object = MibTableColumn
hh3cmplsOutSegmentRowStatus = _Hh3cmplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 11),
    _Hh3cmplsOutSegmentRowStatus_Type()
)
hh3cmplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentRowStatus.setStatus("current")
_Hh3cmplsOutSegmentStorageType_Type = StorageType
_Hh3cmplsOutSegmentStorageType_Object = MibTableColumn
hh3cmplsOutSegmentStorageType = _Hh3cmplsOutSegmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 6, 1, 12),
    _Hh3cmplsOutSegmentStorageType_Type()
)
hh3cmplsOutSegmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentStorageType.setStatus("current")
_Hh3cmplsOutSegmentPerfTable_Object = MibTable
hh3cmplsOutSegmentPerfTable = _Hh3cmplsOutSegmentPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentPerfTable.setStatus("current")
_Hh3cmplsOutSegmentPerfEntry_Object = MibTableRow
hh3cmplsOutSegmentPerfEntry = _Hh3cmplsOutSegmentPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentPerfEntry.setStatus("current")
_Hh3cmplsOutSegmentOctets_Type = Counter32
_Hh3cmplsOutSegmentOctets_Object = MibTableColumn
hh3cmplsOutSegmentOctets = _Hh3cmplsOutSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 1),
    _Hh3cmplsOutSegmentOctets_Type()
)
hh3cmplsOutSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentOctets.setStatus("current")
_Hh3cmplsOutSegmentPackets_Type = Counter32
_Hh3cmplsOutSegmentPackets_Object = MibTableColumn
hh3cmplsOutSegmentPackets = _Hh3cmplsOutSegmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 2),
    _Hh3cmplsOutSegmentPackets_Type()
)
hh3cmplsOutSegmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentPackets.setStatus("current")
_Hh3cmplsOutSegmentErrors_Type = Counter32
_Hh3cmplsOutSegmentErrors_Object = MibTableColumn
hh3cmplsOutSegmentErrors = _Hh3cmplsOutSegmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 3),
    _Hh3cmplsOutSegmentErrors_Type()
)
hh3cmplsOutSegmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentErrors.setStatus("current")
_Hh3cmplsOutSegmentDiscards_Type = Counter32
_Hh3cmplsOutSegmentDiscards_Object = MibTableColumn
hh3cmplsOutSegmentDiscards = _Hh3cmplsOutSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 4),
    _Hh3cmplsOutSegmentDiscards_Type()
)
hh3cmplsOutSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentDiscards.setStatus("current")
_Hh3cmplsOutSegmentHCOctets_Type = Counter64
_Hh3cmplsOutSegmentHCOctets_Object = MibTableColumn
hh3cmplsOutSegmentHCOctets = _Hh3cmplsOutSegmentHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 5),
    _Hh3cmplsOutSegmentHCOctets_Type()
)
hh3cmplsOutSegmentHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentHCOctets.setStatus("current")
_Hh3cmplsOutSegmentPerfDiscontinuityTime_Type = TimeStamp
_Hh3cmplsOutSegmentPerfDiscontinuityTime_Object = MibTableColumn
hh3cmplsOutSegmentPerfDiscontinuityTime = _Hh3cmplsOutSegmentPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 7, 1, 6),
    _Hh3cmplsOutSegmentPerfDiscontinuityTime_Type()
)
hh3cmplsOutSegmentPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentPerfDiscontinuityTime.setStatus("current")


class _Hh3cmplsXCIndexNext_Type(Integer32):
    """Custom type hh3cmplsXCIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsXCIndexNext_Type.__name__ = "Integer32"
_Hh3cmplsXCIndexNext_Object = MibScalar
hh3cmplsXCIndexNext = _Hh3cmplsXCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 8),
    _Hh3cmplsXCIndexNext_Type()
)
hh3cmplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsXCIndexNext.setStatus("current")
_Hh3cmplsXCTable_Object = MibTable
hh3cmplsXCTable = _Hh3cmplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cmplsXCTable.setStatus("current")
_Hh3cmplsXCEntry_Object = MibTableRow
hh3cmplsXCEntry = _Hh3cmplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1)
)
hh3cmplsXCEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsXCIndex"),
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentIfIndex"),
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentLabel"),
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsXCEntry.setStatus("current")


class _Hh3cmplsXCIndex_Type(Integer32):
    """Custom type hh3cmplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsXCIndex_Type.__name__ = "Integer32"
_Hh3cmplsXCIndex_Object = MibTableColumn
hh3cmplsXCIndex = _Hh3cmplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 1),
    _Hh3cmplsXCIndex_Type()
)
hh3cmplsXCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cmplsXCIndex.setStatus("current")
_Hh3cmplsXCLspId_Type = Hh3cMplsLSPID
_Hh3cmplsXCLspId_Object = MibTableColumn
hh3cmplsXCLspId = _Hh3cmplsXCLspId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 2),
    _Hh3cmplsXCLspId_Type()
)
hh3cmplsXCLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCLspId.setStatus("current")


class _Hh3cmplsXCLabelStackIndex_Type(Integer32):
    """Custom type hh3cmplsXCLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsXCLabelStackIndex_Type.__name__ = "Integer32"
_Hh3cmplsXCLabelStackIndex_Object = MibTableColumn
hh3cmplsXCLabelStackIndex = _Hh3cmplsXCLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 3),
    _Hh3cmplsXCLabelStackIndex_Type()
)
hh3cmplsXCLabelStackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCLabelStackIndex.setStatus("current")


class _Hh3cmplsXCIsPersistent_Type(TruthValue):
    """Custom type hh3cmplsXCIsPersistent based on TruthValue"""


_Hh3cmplsXCIsPersistent_Object = MibTableColumn
hh3cmplsXCIsPersistent = _Hh3cmplsXCIsPersistent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 4),
    _Hh3cmplsXCIsPersistent_Type()
)
hh3cmplsXCIsPersistent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCIsPersistent.setStatus("current")
_Hh3cmplsXCOwner_Type = Hh3cMplsObjectOwner
_Hh3cmplsXCOwner_Object = MibTableColumn
hh3cmplsXCOwner = _Hh3cmplsXCOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 5),
    _Hh3cmplsXCOwner_Type()
)
hh3cmplsXCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCOwner.setStatus("current")
_Hh3cmplsXCRowStatus_Type = RowStatus
_Hh3cmplsXCRowStatus_Object = MibTableColumn
hh3cmplsXCRowStatus = _Hh3cmplsXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 6),
    _Hh3cmplsXCRowStatus_Type()
)
hh3cmplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCRowStatus.setStatus("current")
_Hh3cmplsXCStorageType_Type = StorageType
_Hh3cmplsXCStorageType_Object = MibTableColumn
hh3cmplsXCStorageType = _Hh3cmplsXCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 7),
    _Hh3cmplsXCStorageType_Type()
)
hh3cmplsXCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCStorageType.setStatus("current")


class _Hh3cmplsXCAdminStatus_Type(Integer32):
    """Custom type hh3cmplsXCAdminStatus based on Integer32"""
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


_Hh3cmplsXCAdminStatus_Type.__name__ = "Integer32"
_Hh3cmplsXCAdminStatus_Object = MibTableColumn
hh3cmplsXCAdminStatus = _Hh3cmplsXCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 8),
    _Hh3cmplsXCAdminStatus_Type()
)
hh3cmplsXCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsXCAdminStatus.setStatus("current")


class _Hh3cmplsXCOperStatus_Type(Integer32):
    """Custom type hh3cmplsXCOperStatus based on Integer32"""
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


_Hh3cmplsXCOperStatus_Type.__name__ = "Integer32"
_Hh3cmplsXCOperStatus_Object = MibTableColumn
hh3cmplsXCOperStatus = _Hh3cmplsXCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 9, 1, 9),
    _Hh3cmplsXCOperStatus_Type()
)
hh3cmplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsXCOperStatus.setStatus("current")


class _Hh3cmplsMaxLabelStackDepth_Type(Integer32):
    """Custom type hh3cmplsMaxLabelStackDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsMaxLabelStackDepth_Type.__name__ = "Integer32"
_Hh3cmplsMaxLabelStackDepth_Object = MibScalar
hh3cmplsMaxLabelStackDepth = _Hh3cmplsMaxLabelStackDepth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 10),
    _Hh3cmplsMaxLabelStackDepth_Type()
)
hh3cmplsMaxLabelStackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsMaxLabelStackDepth.setStatus("current")


class _Hh3cmplsLabelStackIndexNext_Type(Integer32):
    """Custom type hh3cmplsLabelStackIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsLabelStackIndexNext_Type.__name__ = "Integer32"
_Hh3cmplsLabelStackIndexNext_Object = MibScalar
hh3cmplsLabelStackIndexNext = _Hh3cmplsLabelStackIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 11),
    _Hh3cmplsLabelStackIndexNext_Type()
)
hh3cmplsLabelStackIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackIndexNext.setStatus("current")
_Hh3cmplsLabelStackTable_Object = MibTable
hh3cmplsLabelStackTable = _Hh3cmplsLabelStackTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cmplsLabelStackTable.setStatus("current")
_Hh3cmplsLabelStackEntry_Object = MibTableRow
hh3cmplsLabelStackEntry = _Hh3cmplsLabelStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1)
)
hh3cmplsLabelStackEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackIndex"),
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackLabelIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsLabelStackEntry.setStatus("current")


class _Hh3cmplsLabelStackIndex_Type(Integer32):
    """Custom type hh3cmplsLabelStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsLabelStackIndex_Type.__name__ = "Integer32"
_Hh3cmplsLabelStackIndex_Object = MibTableColumn
hh3cmplsLabelStackIndex = _Hh3cmplsLabelStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1, 1),
    _Hh3cmplsLabelStackIndex_Type()
)
hh3cmplsLabelStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackIndex.setStatus("current")


class _Hh3cmplsLabelStackLabelIndex_Type(Integer32):
    """Custom type hh3cmplsLabelStackLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsLabelStackLabelIndex_Type.__name__ = "Integer32"
_Hh3cmplsLabelStackLabelIndex_Object = MibTableColumn
hh3cmplsLabelStackLabelIndex = _Hh3cmplsLabelStackLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1, 2),
    _Hh3cmplsLabelStackLabelIndex_Type()
)
hh3cmplsLabelStackLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackLabelIndex.setStatus("current")
_Hh3cmplsLabelStackLabel_Type = Hh3cMplsLabel
_Hh3cmplsLabelStackLabel_Object = MibTableColumn
hh3cmplsLabelStackLabel = _Hh3cmplsLabelStackLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1, 3),
    _Hh3cmplsLabelStackLabel_Type()
)
hh3cmplsLabelStackLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackLabel.setStatus("current")
_Hh3cmplsLabelStackRowStatus_Type = RowStatus
_Hh3cmplsLabelStackRowStatus_Object = MibTableColumn
hh3cmplsLabelStackRowStatus = _Hh3cmplsLabelStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1, 4),
    _Hh3cmplsLabelStackRowStatus_Type()
)
hh3cmplsLabelStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackRowStatus.setStatus("current")
_Hh3cmplsLabelStackStorageType_Type = StorageType
_Hh3cmplsLabelStackStorageType_Object = MibTableColumn
hh3cmplsLabelStackStorageType = _Hh3cmplsLabelStackStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 12, 1, 5),
    _Hh3cmplsLabelStackStorageType_Type()
)
hh3cmplsLabelStackStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsLabelStackStorageType.setStatus("current")


class _Hh3cmplsTrafficParamIndexNext_Type(Integer32):
    """Custom type hh3cmplsTrafficParamIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cmplsTrafficParamIndexNext_Type.__name__ = "Integer32"
_Hh3cmplsTrafficParamIndexNext_Object = MibScalar
hh3cmplsTrafficParamIndexNext = _Hh3cmplsTrafficParamIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 13),
    _Hh3cmplsTrafficParamIndexNext_Type()
)
hh3cmplsTrafficParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamIndexNext.setStatus("current")
_Hh3cmplsTrafficParamTable_Object = MibTable
hh3cmplsTrafficParamTable = _Hh3cmplsTrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamTable.setStatus("current")
_Hh3cmplsTrafficParamEntry_Object = MibTableRow
hh3cmplsTrafficParamEntry = _Hh3cmplsTrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1)
)
hh3cmplsTrafficParamEntry.setIndexNames(
    (0, "HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamEntry.setStatus("current")


class _Hh3cmplsTrafficParamIndex_Type(Integer32):
    """Custom type hh3cmplsTrafficParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cmplsTrafficParamIndex_Type.__name__ = "Integer32"
_Hh3cmplsTrafficParamIndex_Object = MibTableColumn
hh3cmplsTrafficParamIndex = _Hh3cmplsTrafficParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 1),
    _Hh3cmplsTrafficParamIndex_Type()
)
hh3cmplsTrafficParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamIndex.setStatus("current")
_Hh3cmplsTrafficParamMaxRate_Type = Hh3cMplsBitRate
_Hh3cmplsTrafficParamMaxRate_Object = MibTableColumn
hh3cmplsTrafficParamMaxRate = _Hh3cmplsTrafficParamMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 2),
    _Hh3cmplsTrafficParamMaxRate_Type()
)
hh3cmplsTrafficParamMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMaxRate.setUnits("kilobits per second")
_Hh3cmplsTrafficParamMeanRate_Type = Hh3cMplsBitRate
_Hh3cmplsTrafficParamMeanRate_Object = MibTableColumn
hh3cmplsTrafficParamMeanRate = _Hh3cmplsTrafficParamMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 3),
    _Hh3cmplsTrafficParamMeanRate_Type()
)
hh3cmplsTrafficParamMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMeanRate.setUnits("kilobits per second")
_Hh3cmplsTrafficParamMaxBurstSize_Type = Hh3cMplsBurstSize
_Hh3cmplsTrafficParamMaxBurstSize_Object = MibTableColumn
hh3cmplsTrafficParamMaxBurstSize = _Hh3cmplsTrafficParamMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 4),
    _Hh3cmplsTrafficParamMaxBurstSize_Type()
)
hh3cmplsTrafficParamMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamMaxBurstSize.setUnits("bytes")
_Hh3cmplsTrafficParamRowStatus_Type = RowStatus
_Hh3cmplsTrafficParamRowStatus_Object = MibTableColumn
hh3cmplsTrafficParamRowStatus = _Hh3cmplsTrafficParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 5),
    _Hh3cmplsTrafficParamRowStatus_Type()
)
hh3cmplsTrafficParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamRowStatus.setStatus("current")
_Hh3cmplsTrafficParamStorageType_Type = StorageType
_Hh3cmplsTrafficParamStorageType_Object = MibTableColumn
hh3cmplsTrafficParamStorageType = _Hh3cmplsTrafficParamStorageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 14, 1, 6),
    _Hh3cmplsTrafficParamStorageType_Type()
)
hh3cmplsTrafficParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamStorageType.setStatus("current")


class _Hh3cmplsXCTrapEnable_Type(TruthValue):
    """Custom type hh3cmplsXCTrapEnable based on TruthValue"""


_Hh3cmplsXCTrapEnable_Object = MibScalar
hh3cmplsXCTrapEnable = _Hh3cmplsXCTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 1, 15),
    _Hh3cmplsXCTrapEnable_Type()
)
hh3cmplsXCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cmplsXCTrapEnable.setStatus("current")
_Hh3cmplsLsrNotifications_ObjectIdentity = ObjectIdentity
hh3cmplsLsrNotifications = _Hh3cmplsLsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 2)
)
_Hh3cmplsLsrNotifyPrefix_ObjectIdentity = ObjectIdentity
hh3cmplsLsrNotifyPrefix = _Hh3cmplsLsrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 2, 0)
)
_Hh3cmplsLsrConformance_ObjectIdentity = ObjectIdentity
hh3cmplsLsrConformance = _Hh3cmplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3)
)
_Hh3cmplsLsrGroups_ObjectIdentity = ObjectIdentity
hh3cmplsLsrGroups = _Hh3cmplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1)
)
_Hh3cmplsLsrCompliances_ObjectIdentity = ObjectIdentity
hh3cmplsLsrCompliances = _Hh3cmplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 2)
)
hh3cmplsInterfaceConfEntry.registerAugmentions(
    ("HH3C-MPLS-LSR-MIB",
     "hh3cmplsInterfacePerfEntry")
)
hh3cmplsInterfacePerfEntry.setIndexNames(*hh3cmplsInterfaceConfEntry.getIndexNames())
hh3cmplsInSegmentEntry.registerAugmentions(
    ("HH3C-MPLS-LSR-MIB",
     "hh3cmplsInSegmentPerfEntry")
)
hh3cmplsInSegmentPerfEntry.setIndexNames(*hh3cmplsInSegmentEntry.getIndexNames())
hh3cmplsOutSegmentEntry.registerAugmentions(
    ("HH3C-MPLS-LSR-MIB",
     "hh3cmplsOutSegmentPerfEntry")
)
hh3cmplsOutSegmentPerfEntry.setIndexNames(*hh3cmplsOutSegmentEntry.getIndexNames())

# Managed Objects groups

hh3cmplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 1)
)
hh3cmplsInterfaceGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceLabelMinIn"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceLabelMaxIn"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceLabelMinOut"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceLabelMaxOut"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceTotalBandwidth"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceAvailableBandwidth"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceLabelParticipationType"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceConfStorageType"))
)
if mibBuilder.loadTexts:
    hh3cmplsInterfaceGroup.setStatus("current")

hh3cmplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 2)
)
hh3cmplsInSegmentGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentNPop"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentAddrFamily"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentXCIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentOctets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentDiscards"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentOwner"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentRowStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentStorageType"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    hh3cmplsInSegmentGroup.setStatus("current")

hh3cmplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 3)
)
hh3cmplsOutSegmentGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIndexNext"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIfIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentPushTopLabel"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentTopLabel"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentNextHopIpAddrType"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentNextHopIpv4Addr"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentNextHopIpv6Addr"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentXCIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentOwner"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentOctets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentDiscards"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentErrors"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentRowStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentStorageType"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentTrafficParamPtr"))
)
if mibBuilder.loadTexts:
    hh3cmplsOutSegmentGroup.setStatus("current")

hh3cmplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 4)
)
hh3cmplsXCGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsXCIndexNext"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCLabelStackIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCOwner"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCAdminStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCOperStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCRowStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCTrapEnable"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCStorageType"))
)
if mibBuilder.loadTexts:
    hh3cmplsXCGroup.setStatus("current")

hh3cmplsXCOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 5)
)
hh3cmplsXCOptionalGroup.setObjects(
    ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCLspId")
)
if mibBuilder.loadTexts:
    hh3cmplsXCOptionalGroup.setStatus("current")

hh3cmplsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 6)
)
hh3cmplsPerfGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentOctets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentPackets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentErrors"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentDiscards"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentOctets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentPackets"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentDiscards"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceInLabelsUsed"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceFailedLabelLookup"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceOutFragments"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInterfaceOutLabelsUsed"))
)
if mibBuilder.loadTexts:
    hh3cmplsPerfGroup.setStatus("current")

hh3cmplsHCInSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 7)
)
hh3cmplsHCInSegmentPerfGroup.setObjects(
    ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentHCOctets")
)
if mibBuilder.loadTexts:
    hh3cmplsHCInSegmentPerfGroup.setStatus("current")

hh3cmplsHCOutSegmentPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 8)
)
hh3cmplsHCOutSegmentPerfGroup.setObjects(
    ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentHCOctets")
)
if mibBuilder.loadTexts:
    hh3cmplsHCOutSegmentPerfGroup.setStatus("current")

hh3cmplsTrafficParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 9)
)
hh3cmplsTrafficParamGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamIndexNext"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamMaxRate"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamMeanRate"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamMaxBurstSize"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamRowStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsTrafficParamStorageType"))
)
if mibBuilder.loadTexts:
    hh3cmplsTrafficParamGroup.setStatus("current")

hh3cmplsXCIsPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 10)
)
hh3cmplsXCIsPersistentGroup.setObjects(
    ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    hh3cmplsXCIsPersistentGroup.setStatus("current")

hh3cmplsXCIsNotPersistentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 11)
)
hh3cmplsXCIsNotPersistentGroup.setObjects(
    ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCIsPersistent")
)
if mibBuilder.loadTexts:
    hh3cmplsXCIsNotPersistentGroup.setStatus("current")

hh3cmplsLabelStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 12)
)
hh3cmplsLabelStackGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackLabel"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackRowStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackStorageType"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsMaxLabelStackDepth"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsLabelStackIndexNext"))
)
if mibBuilder.loadTexts:
    hh3cmplsLabelStackGroup.setStatus("current")

hh3cmplsSegmentDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 13)
)
hh3cmplsSegmentDiscontinuityGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentPerfDiscontinuityTime"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    hh3cmplsSegmentDiscontinuityGroup.setStatus("current")


# Notification objects

hh3cmplsXCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 2, 0, 1)
)
hh3cmplsXCUp.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsXCIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentIfIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentLabel"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCAdminStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cmplsXCUp.setStatus(
        "current"
    )

hh3cmplsXCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 2, 0, 2)
)
hh3cmplsXCDown.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsXCIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentIfIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsInSegmentLabel"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsOutSegmentIndex"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCAdminStatus"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cmplsXCDown.setStatus(
        "current"
    )


# Notifications groups

hh3cmplsLsrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 1, 14)
)
hh3cmplsLsrNotificationGroup.setObjects(
      *(("HH3C-MPLS-LSR-MIB", "hh3cmplsXCUp"),
        ("HH3C-MPLS-LSR-MIB", "hh3cmplsXCDown"))
)
if mibBuilder.loadTexts:
    hh3cmplsLsrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cmplsLsrModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsLsrModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLS-LSR-MIB",
    **{"Hh3cMplsLSPID": Hh3cMplsLSPID,
       "Hh3cMplsLabel": Hh3cMplsLabel,
       "Hh3cMplsBitRate": Hh3cMplsBitRate,
       "Hh3cMplsBurstSize": Hh3cMplsBurstSize,
       "Hh3cMplsObjectOwner": Hh3cMplsObjectOwner,
       "hh3cMplsLsr": hh3cMplsLsr,
       "hh3cmplsLsrObjects": hh3cmplsLsrObjects,
       "hh3cmplsInterfaceConfTable": hh3cmplsInterfaceConfTable,
       "hh3cmplsInterfaceConfEntry": hh3cmplsInterfaceConfEntry,
       "hh3cmplsInterfaceConfIndex": hh3cmplsInterfaceConfIndex,
       "hh3cmplsInterfaceLabelMinIn": hh3cmplsInterfaceLabelMinIn,
       "hh3cmplsInterfaceLabelMaxIn": hh3cmplsInterfaceLabelMaxIn,
       "hh3cmplsInterfaceLabelMinOut": hh3cmplsInterfaceLabelMinOut,
       "hh3cmplsInterfaceLabelMaxOut": hh3cmplsInterfaceLabelMaxOut,
       "hh3cmplsInterfaceTotalBandwidth": hh3cmplsInterfaceTotalBandwidth,
       "hh3cmplsInterfaceAvailableBandwidth": hh3cmplsInterfaceAvailableBandwidth,
       "hh3cmplsInterfaceLabelParticipationType": hh3cmplsInterfaceLabelParticipationType,
       "hh3cmplsInterfaceConfStorageType": hh3cmplsInterfaceConfStorageType,
       "hh3cmplsInterfacePerfTable": hh3cmplsInterfacePerfTable,
       "hh3cmplsInterfacePerfEntry": hh3cmplsInterfacePerfEntry,
       "hh3cmplsInterfaceInLabelsUsed": hh3cmplsInterfaceInLabelsUsed,
       "hh3cmplsInterfaceFailedLabelLookup": hh3cmplsInterfaceFailedLabelLookup,
       "hh3cmplsInterfaceOutLabelsUsed": hh3cmplsInterfaceOutLabelsUsed,
       "hh3cmplsInterfaceOutFragments": hh3cmplsInterfaceOutFragments,
       "hh3cmplsInSegmentTable": hh3cmplsInSegmentTable,
       "hh3cmplsInSegmentEntry": hh3cmplsInSegmentEntry,
       "hh3cmplsInSegmentIfIndex": hh3cmplsInSegmentIfIndex,
       "hh3cmplsInSegmentLabel": hh3cmplsInSegmentLabel,
       "hh3cmplsInSegmentNPop": hh3cmplsInSegmentNPop,
       "hh3cmplsInSegmentAddrFamily": hh3cmplsInSegmentAddrFamily,
       "hh3cmplsInSegmentXCIndex": hh3cmplsInSegmentXCIndex,
       "hh3cmplsInSegmentOwner": hh3cmplsInSegmentOwner,
       "hh3cmplsInSegmentTrafficParamPtr": hh3cmplsInSegmentTrafficParamPtr,
       "hh3cmplsInSegmentRowStatus": hh3cmplsInSegmentRowStatus,
       "hh3cmplsInSegmentStorageType": hh3cmplsInSegmentStorageType,
       "hh3cmplsInSegmentPerfTable": hh3cmplsInSegmentPerfTable,
       "hh3cmplsInSegmentPerfEntry": hh3cmplsInSegmentPerfEntry,
       "hh3cmplsInSegmentOctets": hh3cmplsInSegmentOctets,
       "hh3cmplsInSegmentPackets": hh3cmplsInSegmentPackets,
       "hh3cmplsInSegmentErrors": hh3cmplsInSegmentErrors,
       "hh3cmplsInSegmentDiscards": hh3cmplsInSegmentDiscards,
       "hh3cmplsInSegmentHCOctets": hh3cmplsInSegmentHCOctets,
       "hh3cmplsInSegmentPerfDiscontinuityTime": hh3cmplsInSegmentPerfDiscontinuityTime,
       "hh3cmplsOutSegmentIndexNext": hh3cmplsOutSegmentIndexNext,
       "hh3cmplsOutSegmentTable": hh3cmplsOutSegmentTable,
       "hh3cmplsOutSegmentEntry": hh3cmplsOutSegmentEntry,
       "hh3cmplsOutSegmentIndex": hh3cmplsOutSegmentIndex,
       "hh3cmplsOutSegmentIfIndex": hh3cmplsOutSegmentIfIndex,
       "hh3cmplsOutSegmentPushTopLabel": hh3cmplsOutSegmentPushTopLabel,
       "hh3cmplsOutSegmentTopLabel": hh3cmplsOutSegmentTopLabel,
       "hh3cmplsOutSegmentNextHopIpAddrType": hh3cmplsOutSegmentNextHopIpAddrType,
       "hh3cmplsOutSegmentNextHopIpv4Addr": hh3cmplsOutSegmentNextHopIpv4Addr,
       "hh3cmplsOutSegmentNextHopIpv6Addr": hh3cmplsOutSegmentNextHopIpv6Addr,
       "hh3cmplsOutSegmentXCIndex": hh3cmplsOutSegmentXCIndex,
       "hh3cmplsOutSegmentOwner": hh3cmplsOutSegmentOwner,
       "hh3cmplsOutSegmentTrafficParamPtr": hh3cmplsOutSegmentTrafficParamPtr,
       "hh3cmplsOutSegmentRowStatus": hh3cmplsOutSegmentRowStatus,
       "hh3cmplsOutSegmentStorageType": hh3cmplsOutSegmentStorageType,
       "hh3cmplsOutSegmentPerfTable": hh3cmplsOutSegmentPerfTable,
       "hh3cmplsOutSegmentPerfEntry": hh3cmplsOutSegmentPerfEntry,
       "hh3cmplsOutSegmentOctets": hh3cmplsOutSegmentOctets,
       "hh3cmplsOutSegmentPackets": hh3cmplsOutSegmentPackets,
       "hh3cmplsOutSegmentErrors": hh3cmplsOutSegmentErrors,
       "hh3cmplsOutSegmentDiscards": hh3cmplsOutSegmentDiscards,
       "hh3cmplsOutSegmentHCOctets": hh3cmplsOutSegmentHCOctets,
       "hh3cmplsOutSegmentPerfDiscontinuityTime": hh3cmplsOutSegmentPerfDiscontinuityTime,
       "hh3cmplsXCIndexNext": hh3cmplsXCIndexNext,
       "hh3cmplsXCTable": hh3cmplsXCTable,
       "hh3cmplsXCEntry": hh3cmplsXCEntry,
       "hh3cmplsXCIndex": hh3cmplsXCIndex,
       "hh3cmplsXCLspId": hh3cmplsXCLspId,
       "hh3cmplsXCLabelStackIndex": hh3cmplsXCLabelStackIndex,
       "hh3cmplsXCIsPersistent": hh3cmplsXCIsPersistent,
       "hh3cmplsXCOwner": hh3cmplsXCOwner,
       "hh3cmplsXCRowStatus": hh3cmplsXCRowStatus,
       "hh3cmplsXCStorageType": hh3cmplsXCStorageType,
       "hh3cmplsXCAdminStatus": hh3cmplsXCAdminStatus,
       "hh3cmplsXCOperStatus": hh3cmplsXCOperStatus,
       "hh3cmplsMaxLabelStackDepth": hh3cmplsMaxLabelStackDepth,
       "hh3cmplsLabelStackIndexNext": hh3cmplsLabelStackIndexNext,
       "hh3cmplsLabelStackTable": hh3cmplsLabelStackTable,
       "hh3cmplsLabelStackEntry": hh3cmplsLabelStackEntry,
       "hh3cmplsLabelStackIndex": hh3cmplsLabelStackIndex,
       "hh3cmplsLabelStackLabelIndex": hh3cmplsLabelStackLabelIndex,
       "hh3cmplsLabelStackLabel": hh3cmplsLabelStackLabel,
       "hh3cmplsLabelStackRowStatus": hh3cmplsLabelStackRowStatus,
       "hh3cmplsLabelStackStorageType": hh3cmplsLabelStackStorageType,
       "hh3cmplsTrafficParamIndexNext": hh3cmplsTrafficParamIndexNext,
       "hh3cmplsTrafficParamTable": hh3cmplsTrafficParamTable,
       "hh3cmplsTrafficParamEntry": hh3cmplsTrafficParamEntry,
       "hh3cmplsTrafficParamIndex": hh3cmplsTrafficParamIndex,
       "hh3cmplsTrafficParamMaxRate": hh3cmplsTrafficParamMaxRate,
       "hh3cmplsTrafficParamMeanRate": hh3cmplsTrafficParamMeanRate,
       "hh3cmplsTrafficParamMaxBurstSize": hh3cmplsTrafficParamMaxBurstSize,
       "hh3cmplsTrafficParamRowStatus": hh3cmplsTrafficParamRowStatus,
       "hh3cmplsTrafficParamStorageType": hh3cmplsTrafficParamStorageType,
       "hh3cmplsXCTrapEnable": hh3cmplsXCTrapEnable,
       "hh3cmplsLsrNotifications": hh3cmplsLsrNotifications,
       "hh3cmplsLsrNotifyPrefix": hh3cmplsLsrNotifyPrefix,
       "hh3cmplsXCUp": hh3cmplsXCUp,
       "hh3cmplsXCDown": hh3cmplsXCDown,
       "hh3cmplsLsrConformance": hh3cmplsLsrConformance,
       "hh3cmplsLsrGroups": hh3cmplsLsrGroups,
       "hh3cmplsInterfaceGroup": hh3cmplsInterfaceGroup,
       "hh3cmplsInSegmentGroup": hh3cmplsInSegmentGroup,
       "hh3cmplsOutSegmentGroup": hh3cmplsOutSegmentGroup,
       "hh3cmplsXCGroup": hh3cmplsXCGroup,
       "hh3cmplsXCOptionalGroup": hh3cmplsXCOptionalGroup,
       "hh3cmplsPerfGroup": hh3cmplsPerfGroup,
       "hh3cmplsHCInSegmentPerfGroup": hh3cmplsHCInSegmentPerfGroup,
       "hh3cmplsHCOutSegmentPerfGroup": hh3cmplsHCOutSegmentPerfGroup,
       "hh3cmplsTrafficParamGroup": hh3cmplsTrafficParamGroup,
       "hh3cmplsXCIsPersistentGroup": hh3cmplsXCIsPersistentGroup,
       "hh3cmplsXCIsNotPersistentGroup": hh3cmplsXCIsNotPersistentGroup,
       "hh3cmplsLabelStackGroup": hh3cmplsLabelStackGroup,
       "hh3cmplsSegmentDiscontinuityGroup": hh3cmplsSegmentDiscontinuityGroup,
       "hh3cmplsLsrNotificationGroup": hh3cmplsLsrNotificationGroup,
       "hh3cmplsLsrCompliances": hh3cmplsLsrCompliances,
       "hh3cmplsLsrModuleCompliance": hh3cmplsLsrModuleCompliance}
)
