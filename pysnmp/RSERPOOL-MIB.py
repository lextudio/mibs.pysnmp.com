# SNMP MIB module (RSERPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RSERPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:26 2024
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rserpoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 125)
)
rserpoolMIB.setRevisions(
        ("2009-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RSerPoolENRPServerIdentifierTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RSerPoolOperationScopeTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class RSerPoolPoolHandleTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class RserpoolPoolElementIdentifierTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RSerPoolPolicyIdentifierTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RSerPoolPolicyLoadTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class RSerPoolPolicyWeightTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class RSerPoolTransportUseTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dataOnly", 0),
          ("dataPlusControl", 1))
    )



class RSerPoolOpaqueAddressTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_RserpoolMIBObjects_ObjectIdentity = ObjectIdentity
rserpoolMIBObjects = _RserpoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 1)
)
_RserpoolENRPServers_ObjectIdentity = ObjectIdentity
rserpoolENRPServers = _RserpoolENRPServers_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 1, 1)
)
_RserpoolENRPTable_Object = MibTable
rserpoolENRPTable = _RserpoolENRPTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rserpoolENRPTable.setStatus("current")
_RserpoolENRPEntry_Object = MibTableRow
rserpoolENRPEntry = _RserpoolENRPEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1)
)
rserpoolENRPEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPEntry.setStatus("current")


class _RserpoolENRPIndex_Type(Unsigned32):
    """Custom type rserpoolENRPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPIndex_Object = MibTableColumn
rserpoolENRPIndex = _RserpoolENRPIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 1),
    _RserpoolENRPIndex_Type()
)
rserpoolENRPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPIndex.setStatus("current")
_RserpoolENRPOperationScope_Type = RSerPoolOperationScopeTC
_RserpoolENRPOperationScope_Object = MibTableColumn
rserpoolENRPOperationScope = _RserpoolENRPOperationScope_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 2),
    _RserpoolENRPOperationScope_Type()
)
rserpoolENRPOperationScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPOperationScope.setStatus("current")
_RserpoolENRPIdentifier_Type = RSerPoolENRPServerIdentifierTC
_RserpoolENRPIdentifier_Object = MibTableColumn
rserpoolENRPIdentifier = _RserpoolENRPIdentifier_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 3),
    _RserpoolENRPIdentifier_Type()
)
rserpoolENRPIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPIdentifier.setStatus("current")


class _RserpoolENRPDescription_Type(OctetString):
    """Custom type rserpoolENRPDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RserpoolENRPDescription_Type.__name__ = "OctetString"
_RserpoolENRPDescription_Object = MibTableColumn
rserpoolENRPDescription = _RserpoolENRPDescription_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 4),
    _RserpoolENRPDescription_Type()
)
rserpoolENRPDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolENRPDescription.setStatus("current")
_RserpoolENRPUptime_Type = TimeTicks
_RserpoolENRPUptime_Object = MibTableColumn
rserpoolENRPUptime = _RserpoolENRPUptime_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 5),
    _RserpoolENRPUptime_Type()
)
rserpoolENRPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUptime.setStatus("current")
_RserpoolENRPPort_Type = InetPortNumber
_RserpoolENRPPort_Object = MibTableColumn
rserpoolENRPPort = _RserpoolENRPPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 6),
    _RserpoolENRPPort_Type()
)
rserpoolENRPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPort.setStatus("current")
_RserpoolENRPASAPAnnouncePort_Type = InetPortNumber
_RserpoolENRPASAPAnnouncePort_Object = MibTableColumn
rserpoolENRPASAPAnnouncePort = _RserpoolENRPASAPAnnouncePort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 7),
    _RserpoolENRPASAPAnnouncePort_Type()
)
rserpoolENRPASAPAnnouncePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPAnnouncePort.setStatus("current")


class _RserpoolENRPASAPAnnounceAddrType_Type(InetAddressType):
    """Custom type rserpoolENRPASAPAnnounceAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolENRPASAPAnnounceAddrType_Type.__name__ = "InetAddressType"
_RserpoolENRPASAPAnnounceAddrType_Object = MibTableColumn
rserpoolENRPASAPAnnounceAddrType = _RserpoolENRPASAPAnnounceAddrType_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 8),
    _RserpoolENRPASAPAnnounceAddrType_Type()
)
rserpoolENRPASAPAnnounceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPAnnounceAddrType.setStatus("current")


class _RserpoolENRPASAPAnnounceAddr_Type(InetAddress):
    """Custom type rserpoolENRPASAPAnnounceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPASAPAnnounceAddr_Type.__name__ = "InetAddress"
_RserpoolENRPASAPAnnounceAddr_Object = MibTableColumn
rserpoolENRPASAPAnnounceAddr = _RserpoolENRPASAPAnnounceAddr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 9),
    _RserpoolENRPASAPAnnounceAddr_Type()
)
rserpoolENRPASAPAnnounceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPAnnounceAddr.setStatus("current")
_RserpoolENRPENRPAnnouncePort_Type = InetPortNumber
_RserpoolENRPENRPAnnouncePort_Object = MibTableColumn
rserpoolENRPENRPAnnouncePort = _RserpoolENRPENRPAnnouncePort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 10),
    _RserpoolENRPENRPAnnouncePort_Type()
)
rserpoolENRPENRPAnnouncePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPENRPAnnouncePort.setStatus("current")


class _RserpoolENRPENRPAnnounceAddrType_Type(InetAddressType):
    """Custom type rserpoolENRPENRPAnnounceAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolENRPENRPAnnounceAddrType_Type.__name__ = "InetAddressType"
_RserpoolENRPENRPAnnounceAddrType_Object = MibTableColumn
rserpoolENRPENRPAnnounceAddrType = _RserpoolENRPENRPAnnounceAddrType_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 11),
    _RserpoolENRPENRPAnnounceAddrType_Type()
)
rserpoolENRPENRPAnnounceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPENRPAnnounceAddrType.setStatus("current")


class _RserpoolENRPENRPAnnounceAddr_Type(InetAddress):
    """Custom type rserpoolENRPENRPAnnounceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPENRPAnnounceAddr_Type.__name__ = "InetAddress"
_RserpoolENRPENRPAnnounceAddr_Object = MibTableColumn
rserpoolENRPENRPAnnounceAddr = _RserpoolENRPENRPAnnounceAddr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 1, 1, 12),
    _RserpoolENRPENRPAnnounceAddr_Type()
)
rserpoolENRPENRPAnnounceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPENRPAnnounceAddr.setStatus("current")
_RserpoolENRPPoolTable_Object = MibTable
rserpoolENRPPoolTable = _RserpoolENRPPoolTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rserpoolENRPPoolTable.setStatus("current")
_RserpoolENRPPoolEntry_Object = MibTableRow
rserpoolENRPPoolEntry = _RserpoolENRPPoolEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 3, 1)
)
rserpoolENRPPoolEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPPoolEntry.setStatus("current")


class _RserpoolENRPPoolIndex_Type(Unsigned32):
    """Custom type rserpoolENRPPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPPoolIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPPoolIndex_Object = MibTableColumn
rserpoolENRPPoolIndex = _RserpoolENRPPoolIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 3, 1, 1),
    _RserpoolENRPPoolIndex_Type()
)
rserpoolENRPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPPoolIndex.setStatus("current")
_RserpoolENRPPoolHandle_Type = RSerPoolPoolHandleTC
_RserpoolENRPPoolHandle_Object = MibTableColumn
rserpoolENRPPoolHandle = _RserpoolENRPPoolHandle_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 3, 1, 2),
    _RserpoolENRPPoolHandle_Type()
)
rserpoolENRPPoolHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPoolHandle.setStatus("current")
_RserpoolENRPPoolElementTable_Object = MibTable
rserpoolENRPPoolElementTable = _RserpoolENRPPoolElementTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rserpoolENRPPoolElementTable.setStatus("current")
_RserpoolENRPPoolElementEntry_Object = MibTableRow
rserpoolENRPPoolElementEntry = _RserpoolENRPPoolElementEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1)
)
rserpoolENRPPoolElementEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolElementIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPPoolElementEntry.setStatus("current")


class _RserpoolENRPPoolElementIndex_Type(Unsigned32):
    """Custom type rserpoolENRPPoolElementIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPPoolElementIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPPoolElementIndex_Object = MibTableColumn
rserpoolENRPPoolElementIndex = _RserpoolENRPPoolElementIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 1),
    _RserpoolENRPPoolElementIndex_Type()
)
rserpoolENRPPoolElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPPoolElementIndex.setStatus("current")
_RserpoolENRPPoolElementID_Type = RserpoolPoolElementIdentifierTC
_RserpoolENRPPoolElementID_Object = MibTableColumn
rserpoolENRPPoolElementID = _RserpoolENRPPoolElementID_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 2),
    _RserpoolENRPPoolElementID_Type()
)
rserpoolENRPPoolElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPoolElementID.setStatus("current")
_RserpoolENRPASAPTransportPort_Type = InetPortNumber
_RserpoolENRPASAPTransportPort_Object = MibTableColumn
rserpoolENRPASAPTransportPort = _RserpoolENRPASAPTransportPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 3),
    _RserpoolENRPASAPTransportPort_Type()
)
rserpoolENRPASAPTransportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPTransportPort.setStatus("current")


class _RserpoolENRPUserTransportProto_Type(Unsigned32):
    """Custom type rserpoolENRPUserTransportProto based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RserpoolENRPUserTransportProto_Type.__name__ = "Unsigned32"
_RserpoolENRPUserTransportProto_Object = MibTableColumn
rserpoolENRPUserTransportProto = _RserpoolENRPUserTransportProto_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 4),
    _RserpoolENRPUserTransportProto_Type()
)
rserpoolENRPUserTransportProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserTransportProto.setStatus("current")
_RserpoolENRPUserTransportPort_Type = InetPortNumber
_RserpoolENRPUserTransportPort_Object = MibTableColumn
rserpoolENRPUserTransportPort = _RserpoolENRPUserTransportPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 5),
    _RserpoolENRPUserTransportPort_Type()
)
rserpoolENRPUserTransportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserTransportPort.setStatus("current")
_RserpoolENRPUserTransportUse_Type = RSerPoolTransportUseTypeTC
_RserpoolENRPUserTransportUse_Object = MibTableColumn
rserpoolENRPUserTransportUse = _RserpoolENRPUserTransportUse_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 6),
    _RserpoolENRPUserTransportUse_Type()
)
rserpoolENRPUserTransportUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserTransportUse.setStatus("current")
_RserpoolENRPPolicyID_Type = RSerPoolPolicyIdentifierTC
_RserpoolENRPPolicyID_Object = MibTableColumn
rserpoolENRPPolicyID = _RserpoolENRPPolicyID_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 7),
    _RserpoolENRPPolicyID_Type()
)
rserpoolENRPPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPolicyID.setStatus("current")


class _RserpoolENRPPolicyDescription_Type(OctetString):
    """Custom type rserpoolENRPPolicyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RserpoolENRPPolicyDescription_Type.__name__ = "OctetString"
_RserpoolENRPPolicyDescription_Object = MibTableColumn
rserpoolENRPPolicyDescription = _RserpoolENRPPolicyDescription_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 8),
    _RserpoolENRPPolicyDescription_Type()
)
rserpoolENRPPolicyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPolicyDescription.setStatus("current")
_RserpoolENRPPolicyWeight_Type = RSerPoolPolicyWeightTC
_RserpoolENRPPolicyWeight_Object = MibTableColumn
rserpoolENRPPolicyWeight = _RserpoolENRPPolicyWeight_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 9),
    _RserpoolENRPPolicyWeight_Type()
)
rserpoolENRPPolicyWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPolicyWeight.setStatus("current")
_RserpoolENRPPolicyLoad_Type = RSerPoolPolicyLoadTC
_RserpoolENRPPolicyLoad_Object = MibTableColumn
rserpoolENRPPolicyLoad = _RserpoolENRPPolicyLoad_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 10),
    _RserpoolENRPPolicyLoad_Type()
)
rserpoolENRPPolicyLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPolicyLoad.setStatus("current")
_RserpoolENRPPolicyLoadDeg_Type = RSerPoolPolicyLoadTC
_RserpoolENRPPolicyLoadDeg_Object = MibTableColumn
rserpoolENRPPolicyLoadDeg = _RserpoolENRPPolicyLoadDeg_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 11),
    _RserpoolENRPPolicyLoadDeg_Type()
)
rserpoolENRPPolicyLoadDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPolicyLoadDeg.setStatus("current")
_RserpoolENRPRegistrationLife_Type = TimeTicks
_RserpoolENRPRegistrationLife_Object = MibTableColumn
rserpoolENRPRegistrationLife = _RserpoolENRPRegistrationLife_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 12),
    _RserpoolENRPRegistrationLife_Type()
)
rserpoolENRPRegistrationLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPRegistrationLife.setStatus("current")
_RserpoolENRPHomeENRPServer_Type = RSerPoolENRPServerIdentifierTC
_RserpoolENRPHomeENRPServer_Object = MibTableColumn
rserpoolENRPHomeENRPServer = _RserpoolENRPHomeENRPServer_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 4, 1, 13),
    _RserpoolENRPHomeENRPServer_Type()
)
rserpoolENRPHomeENRPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPHomeENRPServer.setStatus("current")
_RserpoolENRPASAPAddrTable_Object = MibTable
rserpoolENRPASAPAddrTable = _RserpoolENRPASAPAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rserpoolENRPASAPAddrTable.setStatus("current")
_RserpoolENRPASAPAddrTableEntry_Object = MibTableRow
rserpoolENRPASAPAddrTableEntry = _RserpoolENRPASAPAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 5, 1)
)
rserpoolENRPASAPAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolElementIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPASAPAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPASAPAddrTableEntry.setStatus("current")


class _RserpoolENRPASAPAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolENRPASAPAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPASAPAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPASAPAddrTableIndex_Object = MibTableColumn
rserpoolENRPASAPAddrTableIndex = _RserpoolENRPASAPAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 5, 1, 1),
    _RserpoolENRPASAPAddrTableIndex_Type()
)
rserpoolENRPASAPAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPASAPAddrTableIndex.setStatus("current")


class _RserpoolENRPASAPL3Type_Type(InetAddressType):
    """Custom type rserpoolENRPASAPL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolENRPASAPL3Type_Type.__name__ = "InetAddressType"
_RserpoolENRPASAPL3Type_Object = MibTableColumn
rserpoolENRPASAPL3Type = _RserpoolENRPASAPL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 5, 1, 2),
    _RserpoolENRPASAPL3Type_Type()
)
rserpoolENRPASAPL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPL3Type.setStatus("current")


class _RserpoolENRPASAPL3Addr_Type(InetAddress):
    """Custom type rserpoolENRPASAPL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPASAPL3Addr_Type.__name__ = "InetAddress"
_RserpoolENRPASAPL3Addr_Object = MibTableColumn
rserpoolENRPASAPL3Addr = _RserpoolENRPASAPL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 5, 1, 3),
    _RserpoolENRPASAPL3Addr_Type()
)
rserpoolENRPASAPL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPASAPL3Addr.setStatus("current")
_RserpoolENRPUserAddrTable_Object = MibTable
rserpoolENRPUserAddrTable = _RserpoolENRPUserAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rserpoolENRPUserAddrTable.setStatus("current")
_RserpoolENRPUserAddrTableEntry_Object = MibTableRow
rserpoolENRPUserAddrTableEntry = _RserpoolENRPUserAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6, 1)
)
rserpoolENRPUserAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPoolElementIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPUserAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPUserAddrTableEntry.setStatus("current")


class _RserpoolENRPUserAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolENRPUserAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPUserAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPUserAddrTableIndex_Object = MibTableColumn
rserpoolENRPUserAddrTableIndex = _RserpoolENRPUserAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6, 1, 1),
    _RserpoolENRPUserAddrTableIndex_Type()
)
rserpoolENRPUserAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPUserAddrTableIndex.setStatus("current")


class _RserpoolENRPUserL3Type_Type(InetAddressType):
    """Custom type rserpoolENRPUserL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )


_RserpoolENRPUserL3Type_Type.__name__ = "InetAddressType"
_RserpoolENRPUserL3Type_Object = MibTableColumn
rserpoolENRPUserL3Type = _RserpoolENRPUserL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6, 1, 2),
    _RserpoolENRPUserL3Type_Type()
)
rserpoolENRPUserL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserL3Type.setStatus("current")


class _RserpoolENRPUserL3Addr_Type(InetAddress):
    """Custom type rserpoolENRPUserL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPUserL3Addr_Type.__name__ = "InetAddress"
_RserpoolENRPUserL3Addr_Object = MibTableColumn
rserpoolENRPUserL3Addr = _RserpoolENRPUserL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6, 1, 3),
    _RserpoolENRPUserL3Addr_Type()
)
rserpoolENRPUserL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserL3Addr.setStatus("current")
_RserpoolENRPUserL3Opaque_Type = RSerPoolOpaqueAddressTC
_RserpoolENRPUserL3Opaque_Object = MibTableColumn
rserpoolENRPUserL3Opaque = _RserpoolENRPUserL3Opaque_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 6, 1, 4),
    _RserpoolENRPUserL3Opaque_Type()
)
rserpoolENRPUserL3Opaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPUserL3Opaque.setStatus("current")
_RserpoolENRPENRPAddrTable_Object = MibTable
rserpoolENRPENRPAddrTable = _RserpoolENRPENRPAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rserpoolENRPENRPAddrTable.setStatus("current")
_RserpoolENRPENRPAddrTableEntry_Object = MibTableRow
rserpoolENRPENRPAddrTableEntry = _RserpoolENRPENRPAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 7, 1)
)
rserpoolENRPENRPAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPENRPAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPENRPAddrTableEntry.setStatus("current")


class _RserpoolENRPENRPAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolENRPENRPAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPENRPAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPENRPAddrTableIndex_Object = MibTableColumn
rserpoolENRPENRPAddrTableIndex = _RserpoolENRPENRPAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 7, 1, 1),
    _RserpoolENRPENRPAddrTableIndex_Type()
)
rserpoolENRPENRPAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPENRPAddrTableIndex.setStatus("current")


class _RserpoolENRPENRPL3Type_Type(InetAddressType):
    """Custom type rserpoolENRPENRPL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolENRPENRPL3Type_Type.__name__ = "InetAddressType"
_RserpoolENRPENRPL3Type_Object = MibTableColumn
rserpoolENRPENRPL3Type = _RserpoolENRPENRPL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 7, 1, 2),
    _RserpoolENRPENRPL3Type_Type()
)
rserpoolENRPENRPL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPENRPL3Type.setStatus("current")


class _RserpoolENRPENRPL3Addr_Type(InetAddress):
    """Custom type rserpoolENRPENRPL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPENRPL3Addr_Type.__name__ = "InetAddress"
_RserpoolENRPENRPL3Addr_Object = MibTableColumn
rserpoolENRPENRPL3Addr = _RserpoolENRPENRPL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 7, 1, 3),
    _RserpoolENRPENRPL3Addr_Type()
)
rserpoolENRPENRPL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPENRPL3Addr.setStatus("current")
_RserpoolENRPPeerTable_Object = MibTable
rserpoolENRPPeerTable = _RserpoolENRPPeerTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rserpoolENRPPeerTable.setStatus("current")
_RserpoolENRPPeerEntry_Object = MibTableRow
rserpoolENRPPeerEntry = _RserpoolENRPPeerEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8, 1)
)
rserpoolENRPPeerEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPPeerIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPPeerEntry.setStatus("current")


class _RserpoolENRPPeerIndex_Type(Unsigned32):
    """Custom type rserpoolENRPPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPPeerIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPPeerIndex_Object = MibTableColumn
rserpoolENRPPeerIndex = _RserpoolENRPPeerIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8, 1, 1),
    _RserpoolENRPPeerIndex_Type()
)
rserpoolENRPPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPPeerIndex.setStatus("current")
_RserpoolENRPPeerIdentifier_Type = RSerPoolENRPServerIdentifierTC
_RserpoolENRPPeerIdentifier_Object = MibTableColumn
rserpoolENRPPeerIdentifier = _RserpoolENRPPeerIdentifier_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8, 1, 2),
    _RserpoolENRPPeerIdentifier_Type()
)
rserpoolENRPPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPeerIdentifier.setStatus("current")
_RserpoolENRPPeerPort_Type = InetPortNumber
_RserpoolENRPPeerPort_Object = MibTableColumn
rserpoolENRPPeerPort = _RserpoolENRPPeerPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8, 1, 3),
    _RserpoolENRPPeerPort_Type()
)
rserpoolENRPPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPeerPort.setStatus("current")
_RserpoolENRPPeerLastHeard_Type = TimeTicks
_RserpoolENRPPeerLastHeard_Object = MibTableColumn
rserpoolENRPPeerLastHeard = _RserpoolENRPPeerLastHeard_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 8, 1, 4),
    _RserpoolENRPPeerLastHeard_Type()
)
rserpoolENRPPeerLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPeerLastHeard.setStatus("current")
_RserpoolENRPPeerAddrTable_Object = MibTable
rserpoolENRPPeerAddrTable = _RserpoolENRPPeerAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rserpoolENRPPeerAddrTable.setStatus("current")
_RserpoolENRPPeerAddrTableEntry_Object = MibTableRow
rserpoolENRPPeerAddrTableEntry = _RserpoolENRPPeerAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 9, 1)
)
rserpoolENRPPeerAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolENRPPeerIndex"),
    (0, "RSERPOOL-MIB", "rserpoolENRPPeerAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolENRPPeerAddrTableEntry.setStatus("current")


class _RserpoolENRPPeerAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolENRPPeerAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolENRPPeerAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolENRPPeerAddrTableIndex_Object = MibTableColumn
rserpoolENRPPeerAddrTableIndex = _RserpoolENRPPeerAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 9, 1, 1),
    _RserpoolENRPPeerAddrTableIndex_Type()
)
rserpoolENRPPeerAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolENRPPeerAddrTableIndex.setStatus("current")


class _RserpoolENRPPeerL3Type_Type(InetAddressType):
    """Custom type rserpoolENRPPeerL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolENRPPeerL3Type_Type.__name__ = "InetAddressType"
_RserpoolENRPPeerL3Type_Object = MibTableColumn
rserpoolENRPPeerL3Type = _RserpoolENRPPeerL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 9, 1, 2),
    _RserpoolENRPPeerL3Type_Type()
)
rserpoolENRPPeerL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPeerL3Type.setStatus("current")


class _RserpoolENRPPeerL3Addr_Type(InetAddress):
    """Custom type rserpoolENRPPeerL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolENRPPeerL3Addr_Type.__name__ = "InetAddress"
_RserpoolENRPPeerL3Addr_Object = MibTableColumn
rserpoolENRPPeerL3Addr = _RserpoolENRPPeerL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 1, 9, 1, 3),
    _RserpoolENRPPeerL3Addr_Type()
)
rserpoolENRPPeerL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolENRPPeerL3Addr.setStatus("current")
_RserpoolPoolElements_ObjectIdentity = ObjectIdentity
rserpoolPoolElements = _RserpoolPoolElements_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 1, 2)
)
_RserpoolPETable_Object = MibTable
rserpoolPETable = _RserpoolPETable_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rserpoolPETable.setStatus("current")
_RserpoolPEEntry_Object = MibTableRow
rserpoolPEEntry = _RserpoolPEEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1)
)
rserpoolPEEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolPEIndex"),
)
if mibBuilder.loadTexts:
    rserpoolPEEntry.setStatus("current")


class _RserpoolPEIndex_Type(Unsigned32):
    """Custom type rserpoolPEIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolPEIndex_Type.__name__ = "Unsigned32"
_RserpoolPEIndex_Object = MibTableColumn
rserpoolPEIndex = _RserpoolPEIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 1),
    _RserpoolPEIndex_Type()
)
rserpoolPEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolPEIndex.setStatus("current")
_RserpoolPEOperationScope_Type = RSerPoolOperationScopeTC
_RserpoolPEOperationScope_Object = MibTableColumn
rserpoolPEOperationScope = _RserpoolPEOperationScope_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 2),
    _RserpoolPEOperationScope_Type()
)
rserpoolPEOperationScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEOperationScope.setStatus("current")
_RserpoolPEPoolHandle_Type = RSerPoolPoolHandleTC
_RserpoolPEPoolHandle_Object = MibTableColumn
rserpoolPEPoolHandle = _RserpoolPEPoolHandle_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 3),
    _RserpoolPEPoolHandle_Type()
)
rserpoolPEPoolHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEPoolHandle.setStatus("current")
_RserpoolPEIdentifier_Type = RserpoolPoolElementIdentifierTC
_RserpoolPEIdentifier_Object = MibTableColumn
rserpoolPEIdentifier = _RserpoolPEIdentifier_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 4),
    _RserpoolPEIdentifier_Type()
)
rserpoolPEIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEIdentifier.setStatus("current")


class _RserpoolPEDescription_Type(OctetString):
    """Custom type rserpoolPEDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RserpoolPEDescription_Type.__name__ = "OctetString"
_RserpoolPEDescription_Object = MibTableColumn
rserpoolPEDescription = _RserpoolPEDescription_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 5),
    _RserpoolPEDescription_Type()
)
rserpoolPEDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEDescription.setStatus("current")
_RserpoolPEUptime_Type = TimeTicks
_RserpoolPEUptime_Object = MibTableColumn
rserpoolPEUptime = _RserpoolPEUptime_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 6),
    _RserpoolPEUptime_Type()
)
rserpoolPEUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUptime.setStatus("current")
_RserpoolPEASAPTransportPort_Type = InetPortNumber
_RserpoolPEASAPTransportPort_Object = MibTableColumn
rserpoolPEASAPTransportPort = _RserpoolPEASAPTransportPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 7),
    _RserpoolPEASAPTransportPort_Type()
)
rserpoolPEASAPTransportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEASAPTransportPort.setStatus("current")


class _RserpoolPEUserTransportProto_Type(Unsigned32):
    """Custom type rserpoolPEUserTransportProto based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RserpoolPEUserTransportProto_Type.__name__ = "Unsigned32"
_RserpoolPEUserTransportProto_Object = MibTableColumn
rserpoolPEUserTransportProto = _RserpoolPEUserTransportProto_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 8),
    _RserpoolPEUserTransportProto_Type()
)
rserpoolPEUserTransportProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserTransportProto.setStatus("current")
_RserpoolPEUserTransportPort_Type = InetPortNumber
_RserpoolPEUserTransportPort_Object = MibTableColumn
rserpoolPEUserTransportPort = _RserpoolPEUserTransportPort_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 9),
    _RserpoolPEUserTransportPort_Type()
)
rserpoolPEUserTransportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserTransportPort.setStatus("current")
_RserpoolPEUserTransportUse_Type = RSerPoolTransportUseTypeTC
_RserpoolPEUserTransportUse_Object = MibTableColumn
rserpoolPEUserTransportUse = _RserpoolPEUserTransportUse_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 10),
    _RserpoolPEUserTransportUse_Type()
)
rserpoolPEUserTransportUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserTransportUse.setStatus("current")
_RserpoolPEPolicyID_Type = RSerPoolPolicyIdentifierTC
_RserpoolPEPolicyID_Object = MibTableColumn
rserpoolPEPolicyID = _RserpoolPEPolicyID_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 11),
    _RserpoolPEPolicyID_Type()
)
rserpoolPEPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEPolicyID.setStatus("current")


class _RserpoolPEPolicyDescription_Type(OctetString):
    """Custom type rserpoolPEPolicyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RserpoolPEPolicyDescription_Type.__name__ = "OctetString"
_RserpoolPEPolicyDescription_Object = MibTableColumn
rserpoolPEPolicyDescription = _RserpoolPEPolicyDescription_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 12),
    _RserpoolPEPolicyDescription_Type()
)
rserpoolPEPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEPolicyDescription.setStatus("current")
_RserpoolPEPolicyWeight_Type = RSerPoolPolicyWeightTC
_RserpoolPEPolicyWeight_Object = MibTableColumn
rserpoolPEPolicyWeight = _RserpoolPEPolicyWeight_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 13),
    _RserpoolPEPolicyWeight_Type()
)
rserpoolPEPolicyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEPolicyWeight.setStatus("current")
_RserpoolPEPolicyLoad_Type = RSerPoolPolicyLoadTC
_RserpoolPEPolicyLoad_Object = MibTableColumn
rserpoolPEPolicyLoad = _RserpoolPEPolicyLoad_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 14),
    _RserpoolPEPolicyLoad_Type()
)
rserpoolPEPolicyLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEPolicyLoad.setStatus("current")
_RserpoolPEPolicyLoadDeg_Type = RSerPoolPolicyLoadTC
_RserpoolPEPolicyLoadDeg_Object = MibTableColumn
rserpoolPEPolicyLoadDeg = _RserpoolPEPolicyLoadDeg_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 15),
    _RserpoolPEPolicyLoadDeg_Type()
)
rserpoolPEPolicyLoadDeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPEPolicyLoadDeg.setStatus("current")
_RserpoolPERegistrationLife_Type = TimeTicks
_RserpoolPERegistrationLife_Object = MibTableColumn
rserpoolPERegistrationLife = _RserpoolPERegistrationLife_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 16),
    _RserpoolPERegistrationLife_Type()
)
rserpoolPERegistrationLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPERegistrationLife.setStatus("current")
_RserpoolPEHomeENRPServer_Type = RSerPoolENRPServerIdentifierTC
_RserpoolPEHomeENRPServer_Object = MibTableColumn
rserpoolPEHomeENRPServer = _RserpoolPEHomeENRPServer_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 1, 1, 17),
    _RserpoolPEHomeENRPServer_Type()
)
rserpoolPEHomeENRPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEHomeENRPServer.setStatus("current")
_RserpoolPEASAPAddrTable_Object = MibTable
rserpoolPEASAPAddrTable = _RserpoolPEASAPAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rserpoolPEASAPAddrTable.setStatus("current")
_RserpoolPEASAPAddrTableEntry_Object = MibTableRow
rserpoolPEASAPAddrTableEntry = _RserpoolPEASAPAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 2, 1)
)
rserpoolPEASAPAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolPEIndex"),
    (0, "RSERPOOL-MIB", "rserpoolPEASAPAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolPEASAPAddrTableEntry.setStatus("current")


class _RserpoolPEASAPAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolPEASAPAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolPEASAPAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolPEASAPAddrTableIndex_Object = MibTableColumn
rserpoolPEASAPAddrTableIndex = _RserpoolPEASAPAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 2, 1, 1),
    _RserpoolPEASAPAddrTableIndex_Type()
)
rserpoolPEASAPAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolPEASAPAddrTableIndex.setStatus("current")


class _RserpoolPEASAPL3Type_Type(InetAddressType):
    """Custom type rserpoolPEASAPL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RserpoolPEASAPL3Type_Type.__name__ = "InetAddressType"
_RserpoolPEASAPL3Type_Object = MibTableColumn
rserpoolPEASAPL3Type = _RserpoolPEASAPL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 2, 1, 2),
    _RserpoolPEASAPL3Type_Type()
)
rserpoolPEASAPL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEASAPL3Type.setStatus("current")


class _RserpoolPEASAPL3Addr_Type(InetAddress):
    """Custom type rserpoolPEASAPL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolPEASAPL3Addr_Type.__name__ = "InetAddress"
_RserpoolPEASAPL3Addr_Object = MibTableColumn
rserpoolPEASAPL3Addr = _RserpoolPEASAPL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 2, 1, 3),
    _RserpoolPEASAPL3Addr_Type()
)
rserpoolPEASAPL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEASAPL3Addr.setStatus("current")
_RserpoolPEUserAddrTable_Object = MibTable
rserpoolPEUserAddrTable = _RserpoolPEUserAddrTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rserpoolPEUserAddrTable.setStatus("current")
_RserpoolPEUserAddrTableEntry_Object = MibTableRow
rserpoolPEUserAddrTableEntry = _RserpoolPEUserAddrTableEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6, 1)
)
rserpoolPEUserAddrTableEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolPEIndex"),
    (0, "RSERPOOL-MIB", "rserpoolPEUserAddrTableIndex"),
)
if mibBuilder.loadTexts:
    rserpoolPEUserAddrTableEntry.setStatus("current")


class _RserpoolPEUserAddrTableIndex_Type(Unsigned32):
    """Custom type rserpoolPEUserAddrTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolPEUserAddrTableIndex_Type.__name__ = "Unsigned32"
_RserpoolPEUserAddrTableIndex_Object = MibTableColumn
rserpoolPEUserAddrTableIndex = _RserpoolPEUserAddrTableIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6, 1, 1),
    _RserpoolPEUserAddrTableIndex_Type()
)
rserpoolPEUserAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolPEUserAddrTableIndex.setStatus("current")


class _RserpoolPEUserL3Type_Type(InetAddressType):
    """Custom type rserpoolPEUserL3Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )


_RserpoolPEUserL3Type_Type.__name__ = "InetAddressType"
_RserpoolPEUserL3Type_Object = MibTableColumn
rserpoolPEUserL3Type = _RserpoolPEUserL3Type_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6, 1, 2),
    _RserpoolPEUserL3Type_Type()
)
rserpoolPEUserL3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserL3Type.setStatus("current")


class _RserpoolPEUserL3Addr_Type(InetAddress):
    """Custom type rserpoolPEUserL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RserpoolPEUserL3Addr_Type.__name__ = "InetAddress"
_RserpoolPEUserL3Addr_Object = MibTableColumn
rserpoolPEUserL3Addr = _RserpoolPEUserL3Addr_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6, 1, 3),
    _RserpoolPEUserL3Addr_Type()
)
rserpoolPEUserL3Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserL3Addr.setStatus("current")
_RserpoolPEUserL3Opaque_Type = RSerPoolOpaqueAddressTC
_RserpoolPEUserL3Opaque_Object = MibTableColumn
rserpoolPEUserL3Opaque = _RserpoolPEUserL3Opaque_Object(
    (1, 3, 6, 1, 3, 125, 1, 2, 6, 1, 4),
    _RserpoolPEUserL3Opaque_Type()
)
rserpoolPEUserL3Opaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPEUserL3Opaque.setStatus("current")
_RserpoolPoolUsers_ObjectIdentity = ObjectIdentity
rserpoolPoolUsers = _RserpoolPoolUsers_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 1, 3)
)
_RserpoolPUTable_Object = MibTable
rserpoolPUTable = _RserpoolPUTable_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rserpoolPUTable.setStatus("current")
_RserpoolPUEntry_Object = MibTableRow
rserpoolPUEntry = _RserpoolPUEntry_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1)
)
rserpoolPUEntry.setIndexNames(
    (0, "RSERPOOL-MIB", "rserpoolPUIndex"),
)
if mibBuilder.loadTexts:
    rserpoolPUEntry.setStatus("current")


class _RserpoolPUIndex_Type(Unsigned32):
    """Custom type rserpoolPUIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RserpoolPUIndex_Type.__name__ = "Unsigned32"
_RserpoolPUIndex_Object = MibTableColumn
rserpoolPUIndex = _RserpoolPUIndex_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1, 1),
    _RserpoolPUIndex_Type()
)
rserpoolPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rserpoolPUIndex.setStatus("current")
_RserpoolPUOperationScope_Type = RSerPoolOperationScopeTC
_RserpoolPUOperationScope_Object = MibTableColumn
rserpoolPUOperationScope = _RserpoolPUOperationScope_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1, 2),
    _RserpoolPUOperationScope_Type()
)
rserpoolPUOperationScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPUOperationScope.setStatus("current")
_RserpoolPUPoolHandle_Type = RSerPoolPoolHandleTC
_RserpoolPUPoolHandle_Object = MibTableColumn
rserpoolPUPoolHandle = _RserpoolPUPoolHandle_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1, 3),
    _RserpoolPUPoolHandle_Type()
)
rserpoolPUPoolHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPUPoolHandle.setStatus("current")


class _RserpoolPUDescription_Type(OctetString):
    """Custom type rserpoolPUDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RserpoolPUDescription_Type.__name__ = "OctetString"
_RserpoolPUDescription_Object = MibTableColumn
rserpoolPUDescription = _RserpoolPUDescription_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1, 4),
    _RserpoolPUDescription_Type()
)
rserpoolPUDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rserpoolPUDescription.setStatus("current")
_RserpoolPUUptime_Type = TimeTicks
_RserpoolPUUptime_Object = MibTableColumn
rserpoolPUUptime = _RserpoolPUUptime_Object(
    (1, 3, 6, 1, 3, 125, 1, 3, 1, 1, 5),
    _RserpoolPUUptime_Type()
)
rserpoolPUUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rserpoolPUUptime.setStatus("current")
_RserpoolMIBConformance_ObjectIdentity = ObjectIdentity
rserpoolMIBConformance = _RserpoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 2)
)
_RserpoolMIBCompliances_ObjectIdentity = ObjectIdentity
rserpoolMIBCompliances = _RserpoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 2, 1)
)
_RserpoolMIBGroups_ObjectIdentity = ObjectIdentity
rserpoolMIBGroups = _RserpoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 125, 2, 2)
)

# Managed Objects groups

rserpoolENRPGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 125, 2, 2, 1)
)
rserpoolENRPGroup.setObjects(
      *(("RSERPOOL-MIB", "rserpoolENRPOperationScope"),
        ("RSERPOOL-MIB", "rserpoolENRPIdentifier"),
        ("RSERPOOL-MIB", "rserpoolENRPDescription"),
        ("RSERPOOL-MIB", "rserpoolENRPUptime"),
        ("RSERPOOL-MIB", "rserpoolENRPPort"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPAnnouncePort"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPAnnounceAddr"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPAnnounceAddrType"),
        ("RSERPOOL-MIB", "rserpoolENRPENRPAnnounceAddrType"),
        ("RSERPOOL-MIB", "rserpoolENRPENRPAnnouncePort"),
        ("RSERPOOL-MIB", "rserpoolENRPENRPAnnounceAddr"),
        ("RSERPOOL-MIB", "rserpoolENRPPoolHandle"),
        ("RSERPOOL-MIB", "rserpoolENRPPoolElementID"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPTransportPort"),
        ("RSERPOOL-MIB", "rserpoolENRPUserTransportProto"),
        ("RSERPOOL-MIB", "rserpoolENRPUserTransportUse"),
        ("RSERPOOL-MIB", "rserpoolENRPUserTransportPort"),
        ("RSERPOOL-MIB", "rserpoolENRPPolicyID"),
        ("RSERPOOL-MIB", "rserpoolENRPPolicyDescription"),
        ("RSERPOOL-MIB", "rserpoolENRPPolicyWeight"),
        ("RSERPOOL-MIB", "rserpoolENRPPolicyLoad"),
        ("RSERPOOL-MIB", "rserpoolENRPPolicyLoadDeg"),
        ("RSERPOOL-MIB", "rserpoolENRPRegistrationLife"),
        ("RSERPOOL-MIB", "rserpoolENRPHomeENRPServer"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPL3Type"),
        ("RSERPOOL-MIB", "rserpoolENRPASAPL3Addr"),
        ("RSERPOOL-MIB", "rserpoolENRPUserL3Type"),
        ("RSERPOOL-MIB", "rserpoolENRPUserL3Addr"),
        ("RSERPOOL-MIB", "rserpoolENRPUserL3Opaque"),
        ("RSERPOOL-MIB", "rserpoolENRPENRPL3Type"),
        ("RSERPOOL-MIB", "rserpoolENRPENRPL3Addr"),
        ("RSERPOOL-MIB", "rserpoolENRPPeerIdentifier"),
        ("RSERPOOL-MIB", "rserpoolENRPPeerPort"),
        ("RSERPOOL-MIB", "rserpoolENRPPeerLastHeard"),
        ("RSERPOOL-MIB", "rserpoolENRPPeerL3Type"),
        ("RSERPOOL-MIB", "rserpoolENRPPeerL3Addr"))
)
if mibBuilder.loadTexts:
    rserpoolENRPGroup.setStatus("current")

rserpoolPEGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 125, 2, 2, 2)
)
rserpoolPEGroup.setObjects(
      *(("RSERPOOL-MIB", "rserpoolPEOperationScope"),
        ("RSERPOOL-MIB", "rserpoolPEPoolHandle"),
        ("RSERPOOL-MIB", "rserpoolPEIdentifier"),
        ("RSERPOOL-MIB", "rserpoolPEDescription"),
        ("RSERPOOL-MIB", "rserpoolPEUptime"),
        ("RSERPOOL-MIB", "rserpoolPEASAPTransportPort"),
        ("RSERPOOL-MIB", "rserpoolPEUserTransportProto"),
        ("RSERPOOL-MIB", "rserpoolPEUserTransportPort"),
        ("RSERPOOL-MIB", "rserpoolPEUserTransportUse"),
        ("RSERPOOL-MIB", "rserpoolPEPolicyID"),
        ("RSERPOOL-MIB", "rserpoolPEPolicyDescription"),
        ("RSERPOOL-MIB", "rserpoolPEPolicyWeight"),
        ("RSERPOOL-MIB", "rserpoolPEPolicyLoad"),
        ("RSERPOOL-MIB", "rserpoolPEPolicyLoadDeg"),
        ("RSERPOOL-MIB", "rserpoolPERegistrationLife"),
        ("RSERPOOL-MIB", "rserpoolPEHomeENRPServer"),
        ("RSERPOOL-MIB", "rserpoolPEASAPL3Type"),
        ("RSERPOOL-MIB", "rserpoolPEASAPL3Addr"),
        ("RSERPOOL-MIB", "rserpoolPEUserL3Type"),
        ("RSERPOOL-MIB", "rserpoolPEUserL3Addr"),
        ("RSERPOOL-MIB", "rserpoolPEUserL3Opaque"))
)
if mibBuilder.loadTexts:
    rserpoolPEGroup.setStatus("current")

rserpoolPUGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 125, 2, 2, 3)
)
rserpoolPUGroup.setObjects(
      *(("RSERPOOL-MIB", "rserpoolPUOperationScope"),
        ("RSERPOOL-MIB", "rserpoolPUPoolHandle"),
        ("RSERPOOL-MIB", "rserpoolPUDescription"),
        ("RSERPOOL-MIB", "rserpoolPUUptime"))
)
if mibBuilder.loadTexts:
    rserpoolPUGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rserpoolMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 125, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rserpoolMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RSERPOOL-MIB",
    **{"RSerPoolENRPServerIdentifierTC": RSerPoolENRPServerIdentifierTC,
       "RSerPoolOperationScopeTC": RSerPoolOperationScopeTC,
       "RSerPoolPoolHandleTC": RSerPoolPoolHandleTC,
       "RserpoolPoolElementIdentifierTC": RserpoolPoolElementIdentifierTC,
       "RSerPoolPolicyIdentifierTC": RSerPoolPolicyIdentifierTC,
       "RSerPoolPolicyLoadTC": RSerPoolPolicyLoadTC,
       "RSerPoolPolicyWeightTC": RSerPoolPolicyWeightTC,
       "RSerPoolTransportUseTypeTC": RSerPoolTransportUseTypeTC,
       "RSerPoolOpaqueAddressTC": RSerPoolOpaqueAddressTC,
       "rserpoolMIB": rserpoolMIB,
       "rserpoolMIBObjects": rserpoolMIBObjects,
       "rserpoolENRPServers": rserpoolENRPServers,
       "rserpoolENRPTable": rserpoolENRPTable,
       "rserpoolENRPEntry": rserpoolENRPEntry,
       "rserpoolENRPIndex": rserpoolENRPIndex,
       "rserpoolENRPOperationScope": rserpoolENRPOperationScope,
       "rserpoolENRPIdentifier": rserpoolENRPIdentifier,
       "rserpoolENRPDescription": rserpoolENRPDescription,
       "rserpoolENRPUptime": rserpoolENRPUptime,
       "rserpoolENRPPort": rserpoolENRPPort,
       "rserpoolENRPASAPAnnouncePort": rserpoolENRPASAPAnnouncePort,
       "rserpoolENRPASAPAnnounceAddrType": rserpoolENRPASAPAnnounceAddrType,
       "rserpoolENRPASAPAnnounceAddr": rserpoolENRPASAPAnnounceAddr,
       "rserpoolENRPENRPAnnouncePort": rserpoolENRPENRPAnnouncePort,
       "rserpoolENRPENRPAnnounceAddrType": rserpoolENRPENRPAnnounceAddrType,
       "rserpoolENRPENRPAnnounceAddr": rserpoolENRPENRPAnnounceAddr,
       "rserpoolENRPPoolTable": rserpoolENRPPoolTable,
       "rserpoolENRPPoolEntry": rserpoolENRPPoolEntry,
       "rserpoolENRPPoolIndex": rserpoolENRPPoolIndex,
       "rserpoolENRPPoolHandle": rserpoolENRPPoolHandle,
       "rserpoolENRPPoolElementTable": rserpoolENRPPoolElementTable,
       "rserpoolENRPPoolElementEntry": rserpoolENRPPoolElementEntry,
       "rserpoolENRPPoolElementIndex": rserpoolENRPPoolElementIndex,
       "rserpoolENRPPoolElementID": rserpoolENRPPoolElementID,
       "rserpoolENRPASAPTransportPort": rserpoolENRPASAPTransportPort,
       "rserpoolENRPUserTransportProto": rserpoolENRPUserTransportProto,
       "rserpoolENRPUserTransportPort": rserpoolENRPUserTransportPort,
       "rserpoolENRPUserTransportUse": rserpoolENRPUserTransportUse,
       "rserpoolENRPPolicyID": rserpoolENRPPolicyID,
       "rserpoolENRPPolicyDescription": rserpoolENRPPolicyDescription,
       "rserpoolENRPPolicyWeight": rserpoolENRPPolicyWeight,
       "rserpoolENRPPolicyLoad": rserpoolENRPPolicyLoad,
       "rserpoolENRPPolicyLoadDeg": rserpoolENRPPolicyLoadDeg,
       "rserpoolENRPRegistrationLife": rserpoolENRPRegistrationLife,
       "rserpoolENRPHomeENRPServer": rserpoolENRPHomeENRPServer,
       "rserpoolENRPASAPAddrTable": rserpoolENRPASAPAddrTable,
       "rserpoolENRPASAPAddrTableEntry": rserpoolENRPASAPAddrTableEntry,
       "rserpoolENRPASAPAddrTableIndex": rserpoolENRPASAPAddrTableIndex,
       "rserpoolENRPASAPL3Type": rserpoolENRPASAPL3Type,
       "rserpoolENRPASAPL3Addr": rserpoolENRPASAPL3Addr,
       "rserpoolENRPUserAddrTable": rserpoolENRPUserAddrTable,
       "rserpoolENRPUserAddrTableEntry": rserpoolENRPUserAddrTableEntry,
       "rserpoolENRPUserAddrTableIndex": rserpoolENRPUserAddrTableIndex,
       "rserpoolENRPUserL3Type": rserpoolENRPUserL3Type,
       "rserpoolENRPUserL3Addr": rserpoolENRPUserL3Addr,
       "rserpoolENRPUserL3Opaque": rserpoolENRPUserL3Opaque,
       "rserpoolENRPENRPAddrTable": rserpoolENRPENRPAddrTable,
       "rserpoolENRPENRPAddrTableEntry": rserpoolENRPENRPAddrTableEntry,
       "rserpoolENRPENRPAddrTableIndex": rserpoolENRPENRPAddrTableIndex,
       "rserpoolENRPENRPL3Type": rserpoolENRPENRPL3Type,
       "rserpoolENRPENRPL3Addr": rserpoolENRPENRPL3Addr,
       "rserpoolENRPPeerTable": rserpoolENRPPeerTable,
       "rserpoolENRPPeerEntry": rserpoolENRPPeerEntry,
       "rserpoolENRPPeerIndex": rserpoolENRPPeerIndex,
       "rserpoolENRPPeerIdentifier": rserpoolENRPPeerIdentifier,
       "rserpoolENRPPeerPort": rserpoolENRPPeerPort,
       "rserpoolENRPPeerLastHeard": rserpoolENRPPeerLastHeard,
       "rserpoolENRPPeerAddrTable": rserpoolENRPPeerAddrTable,
       "rserpoolENRPPeerAddrTableEntry": rserpoolENRPPeerAddrTableEntry,
       "rserpoolENRPPeerAddrTableIndex": rserpoolENRPPeerAddrTableIndex,
       "rserpoolENRPPeerL3Type": rserpoolENRPPeerL3Type,
       "rserpoolENRPPeerL3Addr": rserpoolENRPPeerL3Addr,
       "rserpoolPoolElements": rserpoolPoolElements,
       "rserpoolPETable": rserpoolPETable,
       "rserpoolPEEntry": rserpoolPEEntry,
       "rserpoolPEIndex": rserpoolPEIndex,
       "rserpoolPEOperationScope": rserpoolPEOperationScope,
       "rserpoolPEPoolHandle": rserpoolPEPoolHandle,
       "rserpoolPEIdentifier": rserpoolPEIdentifier,
       "rserpoolPEDescription": rserpoolPEDescription,
       "rserpoolPEUptime": rserpoolPEUptime,
       "rserpoolPEASAPTransportPort": rserpoolPEASAPTransportPort,
       "rserpoolPEUserTransportProto": rserpoolPEUserTransportProto,
       "rserpoolPEUserTransportPort": rserpoolPEUserTransportPort,
       "rserpoolPEUserTransportUse": rserpoolPEUserTransportUse,
       "rserpoolPEPolicyID": rserpoolPEPolicyID,
       "rserpoolPEPolicyDescription": rserpoolPEPolicyDescription,
       "rserpoolPEPolicyWeight": rserpoolPEPolicyWeight,
       "rserpoolPEPolicyLoad": rserpoolPEPolicyLoad,
       "rserpoolPEPolicyLoadDeg": rserpoolPEPolicyLoadDeg,
       "rserpoolPERegistrationLife": rserpoolPERegistrationLife,
       "rserpoolPEHomeENRPServer": rserpoolPEHomeENRPServer,
       "rserpoolPEASAPAddrTable": rserpoolPEASAPAddrTable,
       "rserpoolPEASAPAddrTableEntry": rserpoolPEASAPAddrTableEntry,
       "rserpoolPEASAPAddrTableIndex": rserpoolPEASAPAddrTableIndex,
       "rserpoolPEASAPL3Type": rserpoolPEASAPL3Type,
       "rserpoolPEASAPL3Addr": rserpoolPEASAPL3Addr,
       "rserpoolPEUserAddrTable": rserpoolPEUserAddrTable,
       "rserpoolPEUserAddrTableEntry": rserpoolPEUserAddrTableEntry,
       "rserpoolPEUserAddrTableIndex": rserpoolPEUserAddrTableIndex,
       "rserpoolPEUserL3Type": rserpoolPEUserL3Type,
       "rserpoolPEUserL3Addr": rserpoolPEUserL3Addr,
       "rserpoolPEUserL3Opaque": rserpoolPEUserL3Opaque,
       "rserpoolPoolUsers": rserpoolPoolUsers,
       "rserpoolPUTable": rserpoolPUTable,
       "rserpoolPUEntry": rserpoolPUEntry,
       "rserpoolPUIndex": rserpoolPUIndex,
       "rserpoolPUOperationScope": rserpoolPUOperationScope,
       "rserpoolPUPoolHandle": rserpoolPUPoolHandle,
       "rserpoolPUDescription": rserpoolPUDescription,
       "rserpoolPUUptime": rserpoolPUUptime,
       "rserpoolMIBConformance": rserpoolMIBConformance,
       "rserpoolMIBCompliances": rserpoolMIBCompliances,
       "rserpoolMIBCompliance": rserpoolMIBCompliance,
       "rserpoolMIBGroups": rserpoolMIBGroups,
       "rserpoolENRPGroup": rserpoolENRPGroup,
       "rserpoolPEGroup": rserpoolPEGroup,
       "rserpoolPUGroup": rserpoolPUGroup}
)
