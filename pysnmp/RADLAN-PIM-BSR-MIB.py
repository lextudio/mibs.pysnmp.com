# SNMP MIB module (RADLAN-PIM-BSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-PIM-BSR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:54 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )



class OperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlPimBsrCandidateRPTable_Object = MibTable
rlPimBsrCandidateRPTable = _RlPimBsrCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 220)
)
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPTable.setStatus("current")
_RlPimBsrCandidateRPEntry_Object = MibTableRow
rlPimBsrCandidateRPEntry = _RlPimBsrCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1)
)
rlPimBsrCandidateRPEntry.setIndexNames(
    (0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddressType"),
    (0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddress"),
)
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPEntry.setStatus("current")
_RlPimBsrCandidateRPAddressType_Type = InetAddressType
_RlPimBsrCandidateRPAddressType_Object = MibTableColumn
rlPimBsrCandidateRPAddressType = _RlPimBsrCandidateRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 1),
    _RlPimBsrCandidateRPAddressType_Type()
)
rlPimBsrCandidateRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPAddressType.setStatus("current")


class _RlPimBsrCandidateRPAddress_Type(InetAddress):
    """Custom type rlPimBsrCandidateRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_RlPimBsrCandidateRPAddress_Type.__name__ = "InetAddress"
_RlPimBsrCandidateRPAddress_Object = MibTableColumn
rlPimBsrCandidateRPAddress = _RlPimBsrCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 2),
    _RlPimBsrCandidateRPAddress_Type()
)
rlPimBsrCandidateRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPAddress.setStatus("current")
_RlPimBsrCandidateRPGroupPrefixList_Type = DisplayString
_RlPimBsrCandidateRPGroupPrefixList_Object = MibTableColumn
rlPimBsrCandidateRPGroupPrefixList = _RlPimBsrCandidateRPGroupPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 3),
    _RlPimBsrCandidateRPGroupPrefixList_Type()
)
rlPimBsrCandidateRPGroupPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPGroupPrefixList.setStatus("current")


class _RlPimBsrCandidateRPBidir_Type(TruthValue):
    """Custom type rlPimBsrCandidateRPBidir based on TruthValue"""


_RlPimBsrCandidateRPBidir_Object = MibTableColumn
rlPimBsrCandidateRPBidir = _RlPimBsrCandidateRPBidir_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 5),
    _RlPimBsrCandidateRPBidir_Type()
)
rlPimBsrCandidateRPBidir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPBidir.setStatus("current")
_RlPimBsrCandidateRPAdvTimer_Type = TimeTicks
_RlPimBsrCandidateRPAdvTimer_Object = MibTableColumn
rlPimBsrCandidateRPAdvTimer = _RlPimBsrCandidateRPAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 6),
    _RlPimBsrCandidateRPAdvTimer_Type()
)
rlPimBsrCandidateRPAdvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPAdvTimer.setStatus("current")


class _RlPimBsrCandidateRPPriority_Type(Unsigned32):
    """Custom type rlPimBsrCandidateRPPriority based on Unsigned32"""
    defaultValue = 192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPimBsrCandidateRPPriority_Type.__name__ = "Unsigned32"
_RlPimBsrCandidateRPPriority_Object = MibTableColumn
rlPimBsrCandidateRPPriority = _RlPimBsrCandidateRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 7),
    _RlPimBsrCandidateRPPriority_Type()
)
rlPimBsrCandidateRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPPriority.setStatus("current")


class _RlPimBsrCandidateRPAdvInterval_Type(Unsigned32):
    """Custom type rlPimBsrCandidateRPAdvInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26214),
    )


_RlPimBsrCandidateRPAdvInterval_Type.__name__ = "Unsigned32"
_RlPimBsrCandidateRPAdvInterval_Object = MibTableColumn
rlPimBsrCandidateRPAdvInterval = _RlPimBsrCandidateRPAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 8),
    _RlPimBsrCandidateRPAdvInterval_Type()
)
rlPimBsrCandidateRPAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPAdvInterval.setUnits("seconds")


class _RlPimBsrCandidateRPHoldtime_Type(Unsigned32):
    """Custom type rlPimBsrCandidateRPHoldtime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPimBsrCandidateRPHoldtime_Type.__name__ = "Unsigned32"
_RlPimBsrCandidateRPHoldtime_Object = MibTableColumn
rlPimBsrCandidateRPHoldtime = _RlPimBsrCandidateRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 9),
    _RlPimBsrCandidateRPHoldtime_Type()
)
rlPimBsrCandidateRPHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPHoldtime.setUnits("seconds")
_RlPimBsrCandidateRPStatus_Type = RowStatus
_RlPimBsrCandidateRPStatus_Object = MibTableColumn
rlPimBsrCandidateRPStatus = _RlPimBsrCandidateRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 220, 1, 10),
    _RlPimBsrCandidateRPStatus_Type()
)
rlPimBsrCandidateRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPimBsrCandidateRPStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-PIM-BSR-MIB",
    **{"AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "rlPimBsrCandidateRPTable": rlPimBsrCandidateRPTable,
       "rlPimBsrCandidateRPEntry": rlPimBsrCandidateRPEntry,
       "rlPimBsrCandidateRPAddressType": rlPimBsrCandidateRPAddressType,
       "rlPimBsrCandidateRPAddress": rlPimBsrCandidateRPAddress,
       "rlPimBsrCandidateRPGroupPrefixList": rlPimBsrCandidateRPGroupPrefixList,
       "rlPimBsrCandidateRPBidir": rlPimBsrCandidateRPBidir,
       "rlPimBsrCandidateRPAdvTimer": rlPimBsrCandidateRPAdvTimer,
       "rlPimBsrCandidateRPPriority": rlPimBsrCandidateRPPriority,
       "rlPimBsrCandidateRPAdvInterval": rlPimBsrCandidateRPAdvInterval,
       "rlPimBsrCandidateRPHoldtime": rlPimBsrCandidateRPHoldtime,
       "rlPimBsrCandidateRPStatus": rlPimBsrCandidateRPStatus}
)
