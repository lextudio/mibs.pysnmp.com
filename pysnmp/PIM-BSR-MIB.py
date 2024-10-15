# SNMP MIB module (PIM-BSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PIM-BSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:52 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetZoneIndex")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pimBsrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 172)
)
pimBsrMIB.setRevisions(
        ("2008-05-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PimBsrNotifications_ObjectIdentity = ObjectIdentity
pimBsrNotifications = _PimBsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 172, 0)
)
_PimBsrObjects_ObjectIdentity = ObjectIdentity
pimBsrObjects = _PimBsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 172, 1)
)
_PimBsrCandidateRPTable_Object = MibTable
pimBsrCandidateRPTable = _PimBsrCandidateRPTable_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1)
)
if mibBuilder.loadTexts:
    pimBsrCandidateRPTable.setStatus("current")
_PimBsrCandidateRPEntry_Object = MibTableRow
pimBsrCandidateRPEntry = _PimBsrCandidateRPEntry_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1)
)
pimBsrCandidateRPEntry.setIndexNames(
    (0, "PIM-BSR-MIB", "pimBsrCandidateRPAddressType"),
    (0, "PIM-BSR-MIB", "pimBsrCandidateRPAddress"),
    (0, "PIM-BSR-MIB", "pimBsrCandidateRPGroupAddress"),
    (0, "PIM-BSR-MIB", "pimBsrCandidateRPGroupPrefixLength"),
)
if mibBuilder.loadTexts:
    pimBsrCandidateRPEntry.setStatus("current")
_PimBsrCandidateRPAddressType_Type = InetAddressType
_PimBsrCandidateRPAddressType_Object = MibTableColumn
pimBsrCandidateRPAddressType = _PimBsrCandidateRPAddressType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 1),
    _PimBsrCandidateRPAddressType_Type()
)
pimBsrCandidateRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrCandidateRPAddressType.setStatus("current")


class _PimBsrCandidateRPAddress_Type(InetAddress):
    """Custom type pimBsrCandidateRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBsrCandidateRPAddress_Type.__name__ = "InetAddress"
_PimBsrCandidateRPAddress_Object = MibTableColumn
pimBsrCandidateRPAddress = _PimBsrCandidateRPAddress_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 2),
    _PimBsrCandidateRPAddress_Type()
)
pimBsrCandidateRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrCandidateRPAddress.setStatus("current")


class _PimBsrCandidateRPGroupAddress_Type(InetAddress):
    """Custom type pimBsrCandidateRPGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBsrCandidateRPGroupAddress_Type.__name__ = "InetAddress"
_PimBsrCandidateRPGroupAddress_Object = MibTableColumn
pimBsrCandidateRPGroupAddress = _PimBsrCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 3),
    _PimBsrCandidateRPGroupAddress_Type()
)
pimBsrCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrCandidateRPGroupAddress.setStatus("current")


class _PimBsrCandidateRPGroupPrefixLength_Type(InetAddressPrefixLength):
    """Custom type pimBsrCandidateRPGroupPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_PimBsrCandidateRPGroupPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_PimBsrCandidateRPGroupPrefixLength_Object = MibTableColumn
pimBsrCandidateRPGroupPrefixLength = _PimBsrCandidateRPGroupPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 4),
    _PimBsrCandidateRPGroupPrefixLength_Type()
)
pimBsrCandidateRPGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrCandidateRPGroupPrefixLength.setStatus("current")


class _PimBsrCandidateRPBidir_Type(TruthValue):
    """Custom type pimBsrCandidateRPBidir based on TruthValue"""


_PimBsrCandidateRPBidir_Object = MibTableColumn
pimBsrCandidateRPBidir = _PimBsrCandidateRPBidir_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 5),
    _PimBsrCandidateRPBidir_Type()
)
pimBsrCandidateRPBidir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPBidir.setStatus("current")
_PimBsrCandidateRPAdvTimer_Type = TimeTicks
_PimBsrCandidateRPAdvTimer_Object = MibTableColumn
pimBsrCandidateRPAdvTimer = _PimBsrCandidateRPAdvTimer_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 6),
    _PimBsrCandidateRPAdvTimer_Type()
)
pimBsrCandidateRPAdvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrCandidateRPAdvTimer.setStatus("current")


class _PimBsrCandidateRPPriority_Type(Unsigned32):
    """Custom type pimBsrCandidateRPPriority based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimBsrCandidateRPPriority_Type.__name__ = "Unsigned32"
_PimBsrCandidateRPPriority_Object = MibTableColumn
pimBsrCandidateRPPriority = _PimBsrCandidateRPPriority_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 7),
    _PimBsrCandidateRPPriority_Type()
)
pimBsrCandidateRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPPriority.setStatus("current")


class _PimBsrCandidateRPAdvInterval_Type(Unsigned32):
    """Custom type pimBsrCandidateRPAdvInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26214),
    )


_PimBsrCandidateRPAdvInterval_Type.__name__ = "Unsigned32"
_PimBsrCandidateRPAdvInterval_Object = MibTableColumn
pimBsrCandidateRPAdvInterval = _PimBsrCandidateRPAdvInterval_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 8),
    _PimBsrCandidateRPAdvInterval_Type()
)
pimBsrCandidateRPAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimBsrCandidateRPAdvInterval.setUnits("seconds")


class _PimBsrCandidateRPHoldtime_Type(Unsigned32):
    """Custom type pimBsrCandidateRPHoldtime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimBsrCandidateRPHoldtime_Type.__name__ = "Unsigned32"
_PimBsrCandidateRPHoldtime_Object = MibTableColumn
pimBsrCandidateRPHoldtime = _PimBsrCandidateRPHoldtime_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 9),
    _PimBsrCandidateRPHoldtime_Type()
)
pimBsrCandidateRPHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    pimBsrCandidateRPHoldtime.setUnits("seconds")
_PimBsrCandidateRPStatus_Type = RowStatus
_PimBsrCandidateRPStatus_Object = MibTableColumn
pimBsrCandidateRPStatus = _PimBsrCandidateRPStatus_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 10),
    _PimBsrCandidateRPStatus_Type()
)
pimBsrCandidateRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPStatus.setStatus("current")


class _PimBsrCandidateRPStorageType_Type(StorageType):
    """Custom type pimBsrCandidateRPStorageType based on StorageType"""


_PimBsrCandidateRPStorageType_Object = MibTableColumn
pimBsrCandidateRPStorageType = _PimBsrCandidateRPStorageType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 11),
    _PimBsrCandidateRPStorageType_Type()
)
pimBsrCandidateRPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateRPStorageType.setStatus("current")
_PimBsrElectedBSRRPSetTable_Object = MibTable
pimBsrElectedBSRRPSetTable = _PimBsrElectedBSRRPSetTable_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2)
)
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetTable.setStatus("current")
_PimBsrElectedBSRRPSetEntry_Object = MibTableRow
pimBsrElectedBSRRPSetEntry = _PimBsrElectedBSRRPSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1)
)
pimBsrElectedBSRRPSetEntry.setIndexNames(
    (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingAddrType"),
    (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingGrpAddr"),
    (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingGrpPrefixLen"),
    (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingRPAddr"),
)
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetEntry.setStatus("current")
_PimBsrElectedBSRGrpMappingAddrType_Type = InetAddressType
_PimBsrElectedBSRGrpMappingAddrType_Object = MibTableColumn
pimBsrElectedBSRGrpMappingAddrType = _PimBsrElectedBSRGrpMappingAddrType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 2),
    _PimBsrElectedBSRGrpMappingAddrType_Type()
)
pimBsrElectedBSRGrpMappingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrElectedBSRGrpMappingAddrType.setStatus("current")


class _PimBsrElectedBSRGrpMappingGrpAddr_Type(InetAddress):
    """Custom type pimBsrElectedBSRGrpMappingGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBsrElectedBSRGrpMappingGrpAddr_Type.__name__ = "InetAddress"
_PimBsrElectedBSRGrpMappingGrpAddr_Object = MibTableColumn
pimBsrElectedBSRGrpMappingGrpAddr = _PimBsrElectedBSRGrpMappingGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 3),
    _PimBsrElectedBSRGrpMappingGrpAddr_Type()
)
pimBsrElectedBSRGrpMappingGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrElectedBSRGrpMappingGrpAddr.setStatus("current")


class _PimBsrElectedBSRGrpMappingGrpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type pimBsrElectedBSRGrpMappingGrpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_PimBsrElectedBSRGrpMappingGrpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_PimBsrElectedBSRGrpMappingGrpPrefixLen_Object = MibTableColumn
pimBsrElectedBSRGrpMappingGrpPrefixLen = _PimBsrElectedBSRGrpMappingGrpPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 4),
    _PimBsrElectedBSRGrpMappingGrpPrefixLen_Type()
)
pimBsrElectedBSRGrpMappingGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrElectedBSRGrpMappingGrpPrefixLen.setStatus("current")


class _PimBsrElectedBSRGrpMappingRPAddr_Type(InetAddress):
    """Custom type pimBsrElectedBSRGrpMappingRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBsrElectedBSRGrpMappingRPAddr_Type.__name__ = "InetAddress"
_PimBsrElectedBSRGrpMappingRPAddr_Object = MibTableColumn
pimBsrElectedBSRGrpMappingRPAddr = _PimBsrElectedBSRGrpMappingRPAddr_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 5),
    _PimBsrElectedBSRGrpMappingRPAddr_Type()
)
pimBsrElectedBSRGrpMappingRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrElectedBSRGrpMappingRPAddr.setStatus("current")


class _PimBsrElectedBSRRPSetPriority_Type(Unsigned32):
    """Custom type pimBsrElectedBSRRPSetPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimBsrElectedBSRRPSetPriority_Type.__name__ = "Unsigned32"
_PimBsrElectedBSRRPSetPriority_Object = MibTableColumn
pimBsrElectedBSRRPSetPriority = _PimBsrElectedBSRRPSetPriority_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 6),
    _PimBsrElectedBSRRPSetPriority_Type()
)
pimBsrElectedBSRRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetPriority.setStatus("current")


class _PimBsrElectedBSRRPSetHoldtime_Type(Unsigned32):
    """Custom type pimBsrElectedBSRRPSetHoldtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimBsrElectedBSRRPSetHoldtime_Type.__name__ = "Unsigned32"
_PimBsrElectedBSRRPSetHoldtime_Object = MibTableColumn
pimBsrElectedBSRRPSetHoldtime = _PimBsrElectedBSRRPSetHoldtime_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 7),
    _PimBsrElectedBSRRPSetHoldtime_Type()
)
pimBsrElectedBSRRPSetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetHoldtime.setUnits("seconds")
_PimBsrElectedBSRRPSetExpiryTime_Type = TimeTicks
_PimBsrElectedBSRRPSetExpiryTime_Object = MibTableColumn
pimBsrElectedBSRRPSetExpiryTime = _PimBsrElectedBSRRPSetExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 8),
    _PimBsrElectedBSRRPSetExpiryTime_Type()
)
pimBsrElectedBSRRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetExpiryTime.setStatus("current")
_PimBsrElectedBSRRPSetGrpBidir_Type = TruthValue
_PimBsrElectedBSRRPSetGrpBidir_Object = MibTableColumn
pimBsrElectedBSRRPSetGrpBidir = _PimBsrElectedBSRRPSetGrpBidir_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 9),
    _PimBsrElectedBSRRPSetGrpBidir_Type()
)
pimBsrElectedBSRRPSetGrpBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRRPSetGrpBidir.setStatus("current")
_PimBsrCandidateBSRTable_Object = MibTable
pimBsrCandidateBSRTable = _PimBsrCandidateBSRTable_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3)
)
if mibBuilder.loadTexts:
    pimBsrCandidateBSRTable.setStatus("current")
_PimBsrCandidateBSREntry_Object = MibTableRow
pimBsrCandidateBSREntry = _PimBsrCandidateBSREntry_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1)
)
pimBsrCandidateBSREntry.setIndexNames(
    (0, "PIM-BSR-MIB", "pimBsrCandidateBSRZoneIndex"),
)
if mibBuilder.loadTexts:
    pimBsrCandidateBSREntry.setStatus("current")


class _PimBsrCandidateBSRZoneIndex_Type(InetZoneIndex):
    """Custom type pimBsrCandidateBSRZoneIndex based on InetZoneIndex"""
    subtypeSpec = InetZoneIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PimBsrCandidateBSRZoneIndex_Type.__name__ = "InetZoneIndex"
_PimBsrCandidateBSRZoneIndex_Object = MibTableColumn
pimBsrCandidateBSRZoneIndex = _PimBsrCandidateBSRZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 1),
    _PimBsrCandidateBSRZoneIndex_Type()
)
pimBsrCandidateBSRZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRZoneIndex.setStatus("current")
_PimBsrCandidateBSRAddressType_Type = InetAddressType
_PimBsrCandidateBSRAddressType_Object = MibTableColumn
pimBsrCandidateBSRAddressType = _PimBsrCandidateBSRAddressType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 2),
    _PimBsrCandidateBSRAddressType_Type()
)
pimBsrCandidateBSRAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRAddressType.setStatus("current")
_PimBsrCandidateBSRAddress_Type = InetAddress
_PimBsrCandidateBSRAddress_Object = MibTableColumn
pimBsrCandidateBSRAddress = _PimBsrCandidateBSRAddress_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 3),
    _PimBsrCandidateBSRAddress_Type()
)
pimBsrCandidateBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRAddress.setStatus("current")


class _PimBsrCandidateBSRPriority_Type(Unsigned32):
    """Custom type pimBsrCandidateBSRPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimBsrCandidateBSRPriority_Type.__name__ = "Unsigned32"
_PimBsrCandidateBSRPriority_Object = MibTableColumn
pimBsrCandidateBSRPriority = _PimBsrCandidateBSRPriority_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 4),
    _PimBsrCandidateBSRPriority_Type()
)
pimBsrCandidateBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRPriority.setStatus("current")


class _PimBsrCandidateBSRHashMaskLength_Type(Unsigned32):
    """Custom type pimBsrCandidateBSRHashMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PimBsrCandidateBSRHashMaskLength_Type.__name__ = "Unsigned32"
_PimBsrCandidateBSRHashMaskLength_Object = MibTableColumn
pimBsrCandidateBSRHashMaskLength = _PimBsrCandidateBSRHashMaskLength_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 5),
    _PimBsrCandidateBSRHashMaskLength_Type()
)
pimBsrCandidateBSRHashMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRHashMaskLength.setStatus("current")
_PimBsrCandidateBSRElectedBSR_Type = TruthValue
_PimBsrCandidateBSRElectedBSR_Object = MibTableColumn
pimBsrCandidateBSRElectedBSR = _PimBsrCandidateBSRElectedBSR_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 6),
    _PimBsrCandidateBSRElectedBSR_Type()
)
pimBsrCandidateBSRElectedBSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRElectedBSR.setStatus("current")
_PimBsrCandidateBSRBootstrapTimer_Type = TimeTicks
_PimBsrCandidateBSRBootstrapTimer_Object = MibTableColumn
pimBsrCandidateBSRBootstrapTimer = _PimBsrCandidateBSRBootstrapTimer_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 7),
    _PimBsrCandidateBSRBootstrapTimer_Type()
)
pimBsrCandidateBSRBootstrapTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRBootstrapTimer.setStatus("current")
_PimBsrCandidateBSRStatus_Type = RowStatus
_PimBsrCandidateBSRStatus_Object = MibTableColumn
pimBsrCandidateBSRStatus = _PimBsrCandidateBSRStatus_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 8),
    _PimBsrCandidateBSRStatus_Type()
)
pimBsrCandidateBSRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRStatus.setStatus("current")


class _PimBsrCandidateBSRStorageType_Type(StorageType):
    """Custom type pimBsrCandidateBSRStorageType based on StorageType"""


_PimBsrCandidateBSRStorageType_Object = MibTableColumn
pimBsrCandidateBSRStorageType = _PimBsrCandidateBSRStorageType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 9),
    _PimBsrCandidateBSRStorageType_Type()
)
pimBsrCandidateBSRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRStorageType.setStatus("current")
_PimBsrElectedBSRTable_Object = MibTable
pimBsrElectedBSRTable = _PimBsrElectedBSRTable_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4)
)
if mibBuilder.loadTexts:
    pimBsrElectedBSRTable.setStatus("current")
_PimBsrElectedBSREntry_Object = MibTableRow
pimBsrElectedBSREntry = _PimBsrElectedBSREntry_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1)
)
pimBsrElectedBSREntry.setIndexNames(
    (0, "PIM-BSR-MIB", "pimBsrElectedBSRZoneIndex"),
)
if mibBuilder.loadTexts:
    pimBsrElectedBSREntry.setStatus("current")


class _PimBsrElectedBSRZoneIndex_Type(InetZoneIndex):
    """Custom type pimBsrElectedBSRZoneIndex based on InetZoneIndex"""
    subtypeSpec = InetZoneIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PimBsrElectedBSRZoneIndex_Type.__name__ = "InetZoneIndex"
_PimBsrElectedBSRZoneIndex_Object = MibTableColumn
pimBsrElectedBSRZoneIndex = _PimBsrElectedBSRZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 1),
    _PimBsrElectedBSRZoneIndex_Type()
)
pimBsrElectedBSRZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBsrElectedBSRZoneIndex.setStatus("current")
_PimBsrElectedBSRAddressType_Type = InetAddressType
_PimBsrElectedBSRAddressType_Object = MibTableColumn
pimBsrElectedBSRAddressType = _PimBsrElectedBSRAddressType_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 2),
    _PimBsrElectedBSRAddressType_Type()
)
pimBsrElectedBSRAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRAddressType.setStatus("current")


class _PimBsrElectedBSRAddress_Type(InetAddress):
    """Custom type pimBsrElectedBSRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBsrElectedBSRAddress_Type.__name__ = "InetAddress"
_PimBsrElectedBSRAddress_Object = MibTableColumn
pimBsrElectedBSRAddress = _PimBsrElectedBSRAddress_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 3),
    _PimBsrElectedBSRAddress_Type()
)
pimBsrElectedBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRAddress.setStatus("current")


class _PimBsrElectedBSRPriority_Type(Unsigned32):
    """Custom type pimBsrElectedBSRPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimBsrElectedBSRPriority_Type.__name__ = "Unsigned32"
_PimBsrElectedBSRPriority_Object = MibTableColumn
pimBsrElectedBSRPriority = _PimBsrElectedBSRPriority_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 4),
    _PimBsrElectedBSRPriority_Type()
)
pimBsrElectedBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRPriority.setStatus("current")


class _PimBsrElectedBSRHashMaskLength_Type(Unsigned32):
    """Custom type pimBsrElectedBSRHashMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PimBsrElectedBSRHashMaskLength_Type.__name__ = "Unsigned32"
_PimBsrElectedBSRHashMaskLength_Object = MibTableColumn
pimBsrElectedBSRHashMaskLength = _PimBsrElectedBSRHashMaskLength_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 5),
    _PimBsrElectedBSRHashMaskLength_Type()
)
pimBsrElectedBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRHashMaskLength.setStatus("current")
_PimBsrElectedBSRExpiryTime_Type = TimeTicks
_PimBsrElectedBSRExpiryTime_Object = MibTableColumn
pimBsrElectedBSRExpiryTime = _PimBsrElectedBSRExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 6),
    _PimBsrElectedBSRExpiryTime_Type()
)
pimBsrElectedBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBsrElectedBSRExpiryTime.setStatus("current")
_PimBsrConformance_ObjectIdentity = ObjectIdentity
pimBsrConformance = _PimBsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 172, 2)
)
_PimBsrCompliances_ObjectIdentity = ObjectIdentity
pimBsrCompliances = _PimBsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 172, 2, 1)
)
_PimBsrGroups_ObjectIdentity = ObjectIdentity
pimBsrGroups = _PimBsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 172, 2, 2)
)

# Managed Objects groups

pimBsrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 172, 2, 2, 1)
)
pimBsrObjectGroup.setObjects(
      *(("PIM-BSR-MIB", "pimBsrCandidateRPBidir"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPAdvTimer"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPPriority"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPAdvInterval"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPHoldtime"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPStatus"),
        ("PIM-BSR-MIB", "pimBsrCandidateRPStorageType"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetPriority"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetHoldtime"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetExpiryTime"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetGrpBidir"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRAddress"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRAddressType"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRPriority"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRHashMaskLength"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRElectedBSR"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRBootstrapTimer"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRStatus"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRStorageType"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRAddress"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRAddressType"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRPriority"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRHashMaskLength"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRExpiryTime"))
)
if mibBuilder.loadTexts:
    pimBsrObjectGroup.setStatus("current")


# Notification objects

pimBsrElectedBSRLostElection = NotificationType(
    (1, 3, 6, 1, 2, 1, 172, 0, 1)
)
pimBsrElectedBSRLostElection.setObjects(
      *(("PIM-BSR-MIB", "pimBsrElectedBSRAddressType"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRAddress"),
        ("PIM-BSR-MIB", "pimBsrElectedBSRPriority"))
)
if mibBuilder.loadTexts:
    pimBsrElectedBSRLostElection.setStatus(
        "current"
    )

pimBsrCandidateBSRWinElection = NotificationType(
    (1, 3, 6, 1, 2, 1, 172, 0, 2)
)
pimBsrCandidateBSRWinElection.setObjects(
    ("PIM-BSR-MIB", "pimBsrCandidateBSRElectedBSR")
)
if mibBuilder.loadTexts:
    pimBsrCandidateBSRWinElection.setStatus(
        "current"
    )


# Notifications groups

pimBsrDiagnosticsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 172, 2, 2, 2)
)
pimBsrDiagnosticsGroup.setObjects(
      *(("PIM-BSR-MIB", "pimBsrElectedBSRLostElection"),
        ("PIM-BSR-MIB", "pimBsrCandidateBSRWinElection"))
)
if mibBuilder.loadTexts:
    pimBsrDiagnosticsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pimBsrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 172, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pimBsrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIM-BSR-MIB",
    **{"pimBsrMIB": pimBsrMIB,
       "pimBsrNotifications": pimBsrNotifications,
       "pimBsrElectedBSRLostElection": pimBsrElectedBSRLostElection,
       "pimBsrCandidateBSRWinElection": pimBsrCandidateBSRWinElection,
       "pimBsrObjects": pimBsrObjects,
       "pimBsrCandidateRPTable": pimBsrCandidateRPTable,
       "pimBsrCandidateRPEntry": pimBsrCandidateRPEntry,
       "pimBsrCandidateRPAddressType": pimBsrCandidateRPAddressType,
       "pimBsrCandidateRPAddress": pimBsrCandidateRPAddress,
       "pimBsrCandidateRPGroupAddress": pimBsrCandidateRPGroupAddress,
       "pimBsrCandidateRPGroupPrefixLength": pimBsrCandidateRPGroupPrefixLength,
       "pimBsrCandidateRPBidir": pimBsrCandidateRPBidir,
       "pimBsrCandidateRPAdvTimer": pimBsrCandidateRPAdvTimer,
       "pimBsrCandidateRPPriority": pimBsrCandidateRPPriority,
       "pimBsrCandidateRPAdvInterval": pimBsrCandidateRPAdvInterval,
       "pimBsrCandidateRPHoldtime": pimBsrCandidateRPHoldtime,
       "pimBsrCandidateRPStatus": pimBsrCandidateRPStatus,
       "pimBsrCandidateRPStorageType": pimBsrCandidateRPStorageType,
       "pimBsrElectedBSRRPSetTable": pimBsrElectedBSRRPSetTable,
       "pimBsrElectedBSRRPSetEntry": pimBsrElectedBSRRPSetEntry,
       "pimBsrElectedBSRGrpMappingAddrType": pimBsrElectedBSRGrpMappingAddrType,
       "pimBsrElectedBSRGrpMappingGrpAddr": pimBsrElectedBSRGrpMappingGrpAddr,
       "pimBsrElectedBSRGrpMappingGrpPrefixLen": pimBsrElectedBSRGrpMappingGrpPrefixLen,
       "pimBsrElectedBSRGrpMappingRPAddr": pimBsrElectedBSRGrpMappingRPAddr,
       "pimBsrElectedBSRRPSetPriority": pimBsrElectedBSRRPSetPriority,
       "pimBsrElectedBSRRPSetHoldtime": pimBsrElectedBSRRPSetHoldtime,
       "pimBsrElectedBSRRPSetExpiryTime": pimBsrElectedBSRRPSetExpiryTime,
       "pimBsrElectedBSRRPSetGrpBidir": pimBsrElectedBSRRPSetGrpBidir,
       "pimBsrCandidateBSRTable": pimBsrCandidateBSRTable,
       "pimBsrCandidateBSREntry": pimBsrCandidateBSREntry,
       "pimBsrCandidateBSRZoneIndex": pimBsrCandidateBSRZoneIndex,
       "pimBsrCandidateBSRAddressType": pimBsrCandidateBSRAddressType,
       "pimBsrCandidateBSRAddress": pimBsrCandidateBSRAddress,
       "pimBsrCandidateBSRPriority": pimBsrCandidateBSRPriority,
       "pimBsrCandidateBSRHashMaskLength": pimBsrCandidateBSRHashMaskLength,
       "pimBsrCandidateBSRElectedBSR": pimBsrCandidateBSRElectedBSR,
       "pimBsrCandidateBSRBootstrapTimer": pimBsrCandidateBSRBootstrapTimer,
       "pimBsrCandidateBSRStatus": pimBsrCandidateBSRStatus,
       "pimBsrCandidateBSRStorageType": pimBsrCandidateBSRStorageType,
       "pimBsrElectedBSRTable": pimBsrElectedBSRTable,
       "pimBsrElectedBSREntry": pimBsrElectedBSREntry,
       "pimBsrElectedBSRZoneIndex": pimBsrElectedBSRZoneIndex,
       "pimBsrElectedBSRAddressType": pimBsrElectedBSRAddressType,
       "pimBsrElectedBSRAddress": pimBsrElectedBSRAddress,
       "pimBsrElectedBSRPriority": pimBsrElectedBSRPriority,
       "pimBsrElectedBSRHashMaskLength": pimBsrElectedBSRHashMaskLength,
       "pimBsrElectedBSRExpiryTime": pimBsrElectedBSRExpiryTime,
       "pimBsrConformance": pimBsrConformance,
       "pimBsrCompliances": pimBsrCompliances,
       "pimBsrCompliance": pimBsrCompliance,
       "pimBsrGroups": pimBsrGroups,
       "pimBsrObjectGroup": pimBsrObjectGroup,
       "pimBsrDiagnosticsGroup": pimBsrDiagnosticsGroup}
)
