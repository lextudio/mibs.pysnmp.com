# SNMP MIB module (ALCATEL-IND1-PIM-BSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PIM-BSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:43 2024
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

(routingIND1Pim,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Pim")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alaPimBsrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3)
)
alaPimBsrMIB.setRevisions(
        ("2007-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaPimBsrNotifications_ObjectIdentity = ObjectIdentity
alaPimBsrNotifications = _AlaPimBsrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0)
)
_AlaPimBsrObjects_ObjectIdentity = ObjectIdentity
alaPimBsrObjects = _AlaPimBsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1)
)
_AlaPimBsrCandidateRPTable_Object = MibTable
alaPimBsrCandidateRPTable = _AlaPimBsrCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPTable.setStatus("current")
_AlaPimBsrCandidateRPEntry_Object = MibTableRow
alaPimBsrCandidateRPEntry = _AlaPimBsrCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1)
)
alaPimBsrCandidateRPEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAddressType"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAddress"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPGroupAddress"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPGroupPrefixLength"),
)
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPEntry.setStatus("current")
_AlaPimBsrCandidateRPAddressType_Type = InetAddressType
_AlaPimBsrCandidateRPAddressType_Object = MibTableColumn
alaPimBsrCandidateRPAddressType = _AlaPimBsrCandidateRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 1),
    _AlaPimBsrCandidateRPAddressType_Type()
)
alaPimBsrCandidateRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPAddressType.setStatus("current")


class _AlaPimBsrCandidateRPAddress_Type(InetAddress):
    """Custom type alaPimBsrCandidateRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimBsrCandidateRPAddress_Type.__name__ = "InetAddress"
_AlaPimBsrCandidateRPAddress_Object = MibTableColumn
alaPimBsrCandidateRPAddress = _AlaPimBsrCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 2),
    _AlaPimBsrCandidateRPAddress_Type()
)
alaPimBsrCandidateRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPAddress.setStatus("current")


class _AlaPimBsrCandidateRPGroupAddress_Type(InetAddress):
    """Custom type alaPimBsrCandidateRPGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimBsrCandidateRPGroupAddress_Type.__name__ = "InetAddress"
_AlaPimBsrCandidateRPGroupAddress_Object = MibTableColumn
alaPimBsrCandidateRPGroupAddress = _AlaPimBsrCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 3),
    _AlaPimBsrCandidateRPGroupAddress_Type()
)
alaPimBsrCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPGroupAddress.setStatus("current")


class _AlaPimBsrCandidateRPGroupPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaPimBsrCandidateRPGroupPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaPimBsrCandidateRPGroupPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaPimBsrCandidateRPGroupPrefixLength_Object = MibTableColumn
alaPimBsrCandidateRPGroupPrefixLength = _AlaPimBsrCandidateRPGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 4),
    _AlaPimBsrCandidateRPGroupPrefixLength_Type()
)
alaPimBsrCandidateRPGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPGroupPrefixLength.setStatus("current")


class _AlaPimBsrCandidateRPBidir_Type(TruthValue):
    """Custom type alaPimBsrCandidateRPBidir based on TruthValue"""


_AlaPimBsrCandidateRPBidir_Object = MibTableColumn
alaPimBsrCandidateRPBidir = _AlaPimBsrCandidateRPBidir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 5),
    _AlaPimBsrCandidateRPBidir_Type()
)
alaPimBsrCandidateRPBidir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPBidir.setStatus("current")
_AlaPimBsrCandidateRPAdvTimer_Type = TimeTicks
_AlaPimBsrCandidateRPAdvTimer_Object = MibTableColumn
alaPimBsrCandidateRPAdvTimer = _AlaPimBsrCandidateRPAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 6),
    _AlaPimBsrCandidateRPAdvTimer_Type()
)
alaPimBsrCandidateRPAdvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPAdvTimer.setStatus("current")


class _AlaPimBsrCandidateRPPriority_Type(Unsigned32):
    """Custom type alaPimBsrCandidateRPPriority based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimBsrCandidateRPPriority_Type.__name__ = "Unsigned32"
_AlaPimBsrCandidateRPPriority_Object = MibTableColumn
alaPimBsrCandidateRPPriority = _AlaPimBsrCandidateRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 7),
    _AlaPimBsrCandidateRPPriority_Type()
)
alaPimBsrCandidateRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPPriority.setStatus("current")


class _AlaPimBsrCandidateRPAdvInterval_Type(Unsigned32):
    """Custom type alaPimBsrCandidateRPAdvInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26214),
    )


_AlaPimBsrCandidateRPAdvInterval_Type.__name__ = "Unsigned32"
_AlaPimBsrCandidateRPAdvInterval_Object = MibTableColumn
alaPimBsrCandidateRPAdvInterval = _AlaPimBsrCandidateRPAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 8),
    _AlaPimBsrCandidateRPAdvInterval_Type()
)
alaPimBsrCandidateRPAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPAdvInterval.setStatus("current")


class _AlaPimBsrCandidateRPHoldtime_Type(Unsigned32):
    """Custom type alaPimBsrCandidateRPHoldtime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimBsrCandidateRPHoldtime_Type.__name__ = "Unsigned32"
_AlaPimBsrCandidateRPHoldtime_Object = MibTableColumn
alaPimBsrCandidateRPHoldtime = _AlaPimBsrCandidateRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 9),
    _AlaPimBsrCandidateRPHoldtime_Type()
)
alaPimBsrCandidateRPHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPHoldtime.setStatus("current")
_AlaPimBsrCandidateRPStatus_Type = RowStatus
_AlaPimBsrCandidateRPStatus_Object = MibTableColumn
alaPimBsrCandidateRPStatus = _AlaPimBsrCandidateRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 1, 1, 10),
    _AlaPimBsrCandidateRPStatus_Type()
)
alaPimBsrCandidateRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateRPStatus.setStatus("current")
_AlaPimBsrElectedBSRRPSetTable_Object = MibTable
alaPimBsrElectedBSRRPSetTable = _AlaPimBsrElectedBSRRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetTable.setStatus("current")
_AlaPimBsrElectedBSRRPSetEntry_Object = MibTableRow
alaPimBsrElectedBSRRPSetEntry = _AlaPimBsrElectedBSRRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1)
)
alaPimBsrElectedBSRRPSetEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingAddrType"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingGrpAddr"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingGrpPrefixLen"),
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRGrpMappingRPAddr"),
)
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetEntry.setStatus("current")
_AlaPimBsrElectedBSRGrpMappingAddrType_Type = InetAddressType
_AlaPimBsrElectedBSRGrpMappingAddrType_Object = MibTableColumn
alaPimBsrElectedBSRGrpMappingAddrType = _AlaPimBsrElectedBSRGrpMappingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 2),
    _AlaPimBsrElectedBSRGrpMappingAddrType_Type()
)
alaPimBsrElectedBSRGrpMappingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRGrpMappingAddrType.setStatus("current")


class _AlaPimBsrElectedBSRGrpMappingGrpAddr_Type(InetAddress):
    """Custom type alaPimBsrElectedBSRGrpMappingGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimBsrElectedBSRGrpMappingGrpAddr_Type.__name__ = "InetAddress"
_AlaPimBsrElectedBSRGrpMappingGrpAddr_Object = MibTableColumn
alaPimBsrElectedBSRGrpMappingGrpAddr = _AlaPimBsrElectedBSRGrpMappingGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 3),
    _AlaPimBsrElectedBSRGrpMappingGrpAddr_Type()
)
alaPimBsrElectedBSRGrpMappingGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRGrpMappingGrpAddr.setStatus("current")


class _AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type alaPimBsrElectedBSRGrpMappingGrpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Object = MibTableColumn
alaPimBsrElectedBSRGrpMappingGrpPrefixLen = _AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 4),
    _AlaPimBsrElectedBSRGrpMappingGrpPrefixLen_Type()
)
alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRGrpMappingGrpPrefixLen.setStatus("current")


class _AlaPimBsrElectedBSRGrpMappingRPAddr_Type(InetAddress):
    """Custom type alaPimBsrElectedBSRGrpMappingRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimBsrElectedBSRGrpMappingRPAddr_Type.__name__ = "InetAddress"
_AlaPimBsrElectedBSRGrpMappingRPAddr_Object = MibTableColumn
alaPimBsrElectedBSRGrpMappingRPAddr = _AlaPimBsrElectedBSRGrpMappingRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 5),
    _AlaPimBsrElectedBSRGrpMappingRPAddr_Type()
)
alaPimBsrElectedBSRGrpMappingRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRGrpMappingRPAddr.setStatus("current")


class _AlaPimBsrElectedBSRRPSetPriority_Type(Unsigned32):
    """Custom type alaPimBsrElectedBSRRPSetPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimBsrElectedBSRRPSetPriority_Type.__name__ = "Unsigned32"
_AlaPimBsrElectedBSRRPSetPriority_Object = MibTableColumn
alaPimBsrElectedBSRRPSetPriority = _AlaPimBsrElectedBSRRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 6),
    _AlaPimBsrElectedBSRRPSetPriority_Type()
)
alaPimBsrElectedBSRRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetPriority.setStatus("current")


class _AlaPimBsrElectedBSRRPSetHoldtime_Type(Unsigned32):
    """Custom type alaPimBsrElectedBSRRPSetHoldtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimBsrElectedBSRRPSetHoldtime_Type.__name__ = "Unsigned32"
_AlaPimBsrElectedBSRRPSetHoldtime_Object = MibTableColumn
alaPimBsrElectedBSRRPSetHoldtime = _AlaPimBsrElectedBSRRPSetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 7),
    _AlaPimBsrElectedBSRRPSetHoldtime_Type()
)
alaPimBsrElectedBSRRPSetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetHoldtime.setUnits("seconds")
_AlaPimBsrElectedBSRRPSetExpiryTime_Type = TimeTicks
_AlaPimBsrElectedBSRRPSetExpiryTime_Object = MibTableColumn
alaPimBsrElectedBSRRPSetExpiryTime = _AlaPimBsrElectedBSRRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 8),
    _AlaPimBsrElectedBSRRPSetExpiryTime_Type()
)
alaPimBsrElectedBSRRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetExpiryTime.setStatus("current")
_AlaPimBsrElectedBSRRPSetGrpBidir_Type = TruthValue
_AlaPimBsrElectedBSRRPSetGrpBidir_Object = MibTableColumn
alaPimBsrElectedBSRRPSetGrpBidir = _AlaPimBsrElectedBSRRPSetGrpBidir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 2, 1, 9),
    _AlaPimBsrElectedBSRRPSetGrpBidir_Type()
)
alaPimBsrElectedBSRRPSetGrpBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRRPSetGrpBidir.setStatus("current")
_AlaPimBsrCandidateBSRTable_Object = MibTable
alaPimBsrCandidateBSRTable = _AlaPimBsrCandidateBSRTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRTable.setStatus("current")
_AlaPimBsrCandidateBSREntry_Object = MibTableRow
alaPimBsrCandidateBSREntry = _AlaPimBsrCandidateBSREntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1)
)
alaPimBsrCandidateBSREntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRAddressType"),
)
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSREntry.setStatus("current")
_AlaPimBsrCandidateBSRAddressType_Type = InetAddressType
_AlaPimBsrCandidateBSRAddressType_Object = MibTableColumn
alaPimBsrCandidateBSRAddressType = _AlaPimBsrCandidateBSRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 1),
    _AlaPimBsrCandidateBSRAddressType_Type()
)
alaPimBsrCandidateBSRAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRAddressType.setStatus("current")
_AlaPimBsrCandidateBSRAddress_Type = InetAddress
_AlaPimBsrCandidateBSRAddress_Object = MibTableColumn
alaPimBsrCandidateBSRAddress = _AlaPimBsrCandidateBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 2),
    _AlaPimBsrCandidateBSRAddress_Type()
)
alaPimBsrCandidateBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRAddress.setStatus("current")


class _AlaPimBsrCandidateBSRPriority_Type(Unsigned32):
    """Custom type alaPimBsrCandidateBSRPriority based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimBsrCandidateBSRPriority_Type.__name__ = "Unsigned32"
_AlaPimBsrCandidateBSRPriority_Object = MibTableColumn
alaPimBsrCandidateBSRPriority = _AlaPimBsrCandidateBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 3),
    _AlaPimBsrCandidateBSRPriority_Type()
)
alaPimBsrCandidateBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRPriority.setStatus("current")


class _AlaPimBsrCandidateBSRHashMaskLength_Type(Unsigned32):
    """Custom type alaPimBsrCandidateBSRHashMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaPimBsrCandidateBSRHashMaskLength_Type.__name__ = "Unsigned32"
_AlaPimBsrCandidateBSRHashMaskLength_Object = MibTableColumn
alaPimBsrCandidateBSRHashMaskLength = _AlaPimBsrCandidateBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 4),
    _AlaPimBsrCandidateBSRHashMaskLength_Type()
)
alaPimBsrCandidateBSRHashMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRHashMaskLength.setStatus("current")
_AlaPimBsrCandidateBSRElectedBSR_Type = TruthValue
_AlaPimBsrCandidateBSRElectedBSR_Object = MibTableColumn
alaPimBsrCandidateBSRElectedBSR = _AlaPimBsrCandidateBSRElectedBSR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 5),
    _AlaPimBsrCandidateBSRElectedBSR_Type()
)
alaPimBsrCandidateBSRElectedBSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRElectedBSR.setStatus("current")
_AlaPimBsrCandidateBSRBootstrapTimer_Type = TimeTicks
_AlaPimBsrCandidateBSRBootstrapTimer_Object = MibTableColumn
alaPimBsrCandidateBSRBootstrapTimer = _AlaPimBsrCandidateBSRBootstrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 6),
    _AlaPimBsrCandidateBSRBootstrapTimer_Type()
)
alaPimBsrCandidateBSRBootstrapTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRBootstrapTimer.setStatus("current")
_AlaPimBsrCandidateBSRStatus_Type = RowStatus
_AlaPimBsrCandidateBSRStatus_Object = MibTableColumn
alaPimBsrCandidateBSRStatus = _AlaPimBsrCandidateBSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 3, 1, 7),
    _AlaPimBsrCandidateBSRStatus_Type()
)
alaPimBsrCandidateBSRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRStatus.setStatus("current")
_AlaPimBsrElectedBSRTable_Object = MibTable
alaPimBsrElectedBSRTable = _AlaPimBsrElectedBSRTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4)
)
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRTable.setStatus("current")
_AlaPimBsrElectedBSREntry_Object = MibTableRow
alaPimBsrElectedBSREntry = _AlaPimBsrElectedBSREntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1)
)
alaPimBsrElectedBSREntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRAddressType"),
)
if mibBuilder.loadTexts:
    alaPimBsrElectedBSREntry.setStatus("current")
_AlaPimBsrElectedBSRAddressType_Type = InetAddressType
_AlaPimBsrElectedBSRAddressType_Object = MibTableColumn
alaPimBsrElectedBSRAddressType = _AlaPimBsrElectedBSRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 1),
    _AlaPimBsrElectedBSRAddressType_Type()
)
alaPimBsrElectedBSRAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRAddressType.setStatus("current")


class _AlaPimBsrElectedBSRAddress_Type(InetAddress):
    """Custom type alaPimBsrElectedBSRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimBsrElectedBSRAddress_Type.__name__ = "InetAddress"
_AlaPimBsrElectedBSRAddress_Object = MibTableColumn
alaPimBsrElectedBSRAddress = _AlaPimBsrElectedBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 2),
    _AlaPimBsrElectedBSRAddress_Type()
)
alaPimBsrElectedBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRAddress.setStatus("current")


class _AlaPimBsrElectedBSRPriority_Type(Unsigned32):
    """Custom type alaPimBsrElectedBSRPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimBsrElectedBSRPriority_Type.__name__ = "Unsigned32"
_AlaPimBsrElectedBSRPriority_Object = MibTableColumn
alaPimBsrElectedBSRPriority = _AlaPimBsrElectedBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 3),
    _AlaPimBsrElectedBSRPriority_Type()
)
alaPimBsrElectedBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRPriority.setStatus("current")


class _AlaPimBsrElectedBSRHashMaskLength_Type(Unsigned32):
    """Custom type alaPimBsrElectedBSRHashMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaPimBsrElectedBSRHashMaskLength_Type.__name__ = "Unsigned32"
_AlaPimBsrElectedBSRHashMaskLength_Object = MibTableColumn
alaPimBsrElectedBSRHashMaskLength = _AlaPimBsrElectedBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 4),
    _AlaPimBsrElectedBSRHashMaskLength_Type()
)
alaPimBsrElectedBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRHashMaskLength.setStatus("current")
_AlaPimBsrElectedBSRExpiryTime_Type = TimeTicks
_AlaPimBsrElectedBSRExpiryTime_Object = MibTableColumn
alaPimBsrElectedBSRExpiryTime = _AlaPimBsrElectedBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 1, 4, 1, 5),
    _AlaPimBsrElectedBSRExpiryTime_Type()
)
alaPimBsrElectedBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRExpiryTime.setStatus("current")
_AlaPimBsrConformance_ObjectIdentity = ObjectIdentity
alaPimBsrConformance = _AlaPimBsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2)
)
_AlaPimBsrCompliances_ObjectIdentity = ObjectIdentity
alaPimBsrCompliances = _AlaPimBsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 1)
)
_AlaPimBsrGroups_ObjectIdentity = ObjectIdentity
alaPimBsrGroups = _AlaPimBsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2)
)

# Managed Objects groups

alaPimBsrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2, 1)
)
alaPimBsrObjectGroup.setObjects(
      *(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPBidir"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAdvTimer"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPPriority"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPAdvInterval"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPHoldtime"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateRPStatus"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetPriority"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetHoldtime"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetExpiryTime"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRRPSetGrpBidir"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRAddress"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRPriority"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRHashMaskLength"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRBootstrapTimer"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRStatus"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRAddress"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRPriority"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRHashMaskLength"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRExpiryTime"))
)
if mibBuilder.loadTexts:
    alaPimBsrObjectGroup.setStatus("current")


# Notification objects

alaPimBsrElectedBSRLostElection = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0, 1)
)
alaPimBsrElectedBSRLostElection.setObjects(
    ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR")
)
if mibBuilder.loadTexts:
    alaPimBsrElectedBSRLostElection.setStatus(
        "current"
    )

alaPimBsrCandidateBSRWinElection = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 0, 2)
)
alaPimBsrCandidateBSRWinElection.setObjects(
    ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRElectedBSR")
)
if mibBuilder.loadTexts:
    alaPimBsrCandidateBSRWinElection.setStatus(
        "current"
    )


# Notifications groups

alaPimBsrDiagnosticsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 2, 2)
)
alaPimBsrDiagnosticsGroup.setObjects(
      *(("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrElectedBSRLostElection"),
        ("ALCATEL-IND1-PIM-BSR-MIB", "alaPimBsrCandidateBSRWinElection"))
)
if mibBuilder.loadTexts:
    alaPimBsrDiagnosticsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaPimBsrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaPimBsrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PIM-BSR-MIB",
    **{"alaPimBsrMIB": alaPimBsrMIB,
       "alaPimBsrNotifications": alaPimBsrNotifications,
       "alaPimBsrElectedBSRLostElection": alaPimBsrElectedBSRLostElection,
       "alaPimBsrCandidateBSRWinElection": alaPimBsrCandidateBSRWinElection,
       "alaPimBsrObjects": alaPimBsrObjects,
       "alaPimBsrCandidateRPTable": alaPimBsrCandidateRPTable,
       "alaPimBsrCandidateRPEntry": alaPimBsrCandidateRPEntry,
       "alaPimBsrCandidateRPAddressType": alaPimBsrCandidateRPAddressType,
       "alaPimBsrCandidateRPAddress": alaPimBsrCandidateRPAddress,
       "alaPimBsrCandidateRPGroupAddress": alaPimBsrCandidateRPGroupAddress,
       "alaPimBsrCandidateRPGroupPrefixLength": alaPimBsrCandidateRPGroupPrefixLength,
       "alaPimBsrCandidateRPBidir": alaPimBsrCandidateRPBidir,
       "alaPimBsrCandidateRPAdvTimer": alaPimBsrCandidateRPAdvTimer,
       "alaPimBsrCandidateRPPriority": alaPimBsrCandidateRPPriority,
       "alaPimBsrCandidateRPAdvInterval": alaPimBsrCandidateRPAdvInterval,
       "alaPimBsrCandidateRPHoldtime": alaPimBsrCandidateRPHoldtime,
       "alaPimBsrCandidateRPStatus": alaPimBsrCandidateRPStatus,
       "alaPimBsrElectedBSRRPSetTable": alaPimBsrElectedBSRRPSetTable,
       "alaPimBsrElectedBSRRPSetEntry": alaPimBsrElectedBSRRPSetEntry,
       "alaPimBsrElectedBSRGrpMappingAddrType": alaPimBsrElectedBSRGrpMappingAddrType,
       "alaPimBsrElectedBSRGrpMappingGrpAddr": alaPimBsrElectedBSRGrpMappingGrpAddr,
       "alaPimBsrElectedBSRGrpMappingGrpPrefixLen": alaPimBsrElectedBSRGrpMappingGrpPrefixLen,
       "alaPimBsrElectedBSRGrpMappingRPAddr": alaPimBsrElectedBSRGrpMappingRPAddr,
       "alaPimBsrElectedBSRRPSetPriority": alaPimBsrElectedBSRRPSetPriority,
       "alaPimBsrElectedBSRRPSetHoldtime": alaPimBsrElectedBSRRPSetHoldtime,
       "alaPimBsrElectedBSRRPSetExpiryTime": alaPimBsrElectedBSRRPSetExpiryTime,
       "alaPimBsrElectedBSRRPSetGrpBidir": alaPimBsrElectedBSRRPSetGrpBidir,
       "alaPimBsrCandidateBSRTable": alaPimBsrCandidateBSRTable,
       "alaPimBsrCandidateBSREntry": alaPimBsrCandidateBSREntry,
       "alaPimBsrCandidateBSRAddressType": alaPimBsrCandidateBSRAddressType,
       "alaPimBsrCandidateBSRAddress": alaPimBsrCandidateBSRAddress,
       "alaPimBsrCandidateBSRPriority": alaPimBsrCandidateBSRPriority,
       "alaPimBsrCandidateBSRHashMaskLength": alaPimBsrCandidateBSRHashMaskLength,
       "alaPimBsrCandidateBSRElectedBSR": alaPimBsrCandidateBSRElectedBSR,
       "alaPimBsrCandidateBSRBootstrapTimer": alaPimBsrCandidateBSRBootstrapTimer,
       "alaPimBsrCandidateBSRStatus": alaPimBsrCandidateBSRStatus,
       "alaPimBsrElectedBSRTable": alaPimBsrElectedBSRTable,
       "alaPimBsrElectedBSREntry": alaPimBsrElectedBSREntry,
       "alaPimBsrElectedBSRAddressType": alaPimBsrElectedBSRAddressType,
       "alaPimBsrElectedBSRAddress": alaPimBsrElectedBSRAddress,
       "alaPimBsrElectedBSRPriority": alaPimBsrElectedBSRPriority,
       "alaPimBsrElectedBSRHashMaskLength": alaPimBsrElectedBSRHashMaskLength,
       "alaPimBsrElectedBSRExpiryTime": alaPimBsrElectedBSRExpiryTime,
       "alaPimBsrConformance": alaPimBsrConformance,
       "alaPimBsrCompliances": alaPimBsrCompliances,
       "alaPimBsrCompliance": alaPimBsrCompliance,
       "alaPimBsrGroups": alaPimBsrGroups,
       "alaPimBsrObjectGroup": alaPimBsrObjectGroup,
       "alaPimBsrDiagnosticsGroup": alaPimBsrDiagnosticsGroup}
)
