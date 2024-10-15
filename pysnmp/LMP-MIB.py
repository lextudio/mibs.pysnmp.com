# SNMP MIB module (LMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:14 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TeLinkEncodingType,
 teLinkIncomingIfId,
 teLinkRemoteIpAddr) = mibBuilder.importSymbols(
    "TE-LINK-STD-MIB",
    "TeLinkEncodingType",
    "teLinkIncomingIfId",
    "teLinkRemoteIpAddr")


# MODULE-IDENTITY

lmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227)
)
lmpMIB.setRevisions(
        ("2006-08-14 00:00",
         "2006-01-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LmpInterval(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class LmpRetransmitInterval(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class LmpNodeId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_LmpNotifications_ObjectIdentity = ObjectIdentity
lmpNotifications = _LmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227, 0)
)
_LmpObjects_ObjectIdentity = ObjectIdentity
lmpObjects = _LmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227, 1)
)


class _LmpAdminStatus_Type(Integer32):
    """Custom type lmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LmpAdminStatus_Type.__name__ = "Integer32"
_LmpAdminStatus_Object = MibScalar
lmpAdminStatus = _LmpAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 1),
    _LmpAdminStatus_Type()
)
lmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpAdminStatus.setStatus("current")


class _LmpOperStatus_Type(Integer32):
    """Custom type lmpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LmpOperStatus_Type.__name__ = "Integer32"
_LmpOperStatus_Object = MibScalar
lmpOperStatus = _LmpOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 2),
    _LmpOperStatus_Type()
)
lmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpOperStatus.setStatus("current")
_LmpNbrTable_Object = MibTable
lmpNbrTable = _LmpNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3)
)
if mibBuilder.loadTexts:
    lmpNbrTable.setStatus("current")
_LmpNbrEntry_Object = MibTableRow
lmpNbrEntry = _LmpNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1)
)
lmpNbrEntry.setIndexNames(
    (0, "LMP-MIB", "lmpNbrNodeId"),
)
if mibBuilder.loadTexts:
    lmpNbrEntry.setStatus("current")
_LmpNbrNodeId_Type = LmpNodeId
_LmpNbrNodeId_Object = MibTableColumn
lmpNbrNodeId = _LmpNbrNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 1),
    _LmpNbrNodeId_Type()
)
lmpNbrNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmpNbrNodeId.setStatus("current")


class _LmpNbrRetransmitInterval_Type(LmpRetransmitInterval):
    """Custom type lmpNbrRetransmitInterval based on LmpRetransmitInterval"""
    defaultValue = 500


_LmpNbrRetransmitInterval_Object = MibTableColumn
lmpNbrRetransmitInterval = _LmpNbrRetransmitInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 2),
    _LmpNbrRetransmitInterval_Type()
)
lmpNbrRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrRetransmitInterval.setStatus("current")


class _LmpNbrRetryLimit_Type(Unsigned32):
    """Custom type lmpNbrRetryLimit based on Unsigned32"""
    defaultValue = 3


_LmpNbrRetryLimit_Object = MibTableColumn
lmpNbrRetryLimit = _LmpNbrRetryLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 3),
    _LmpNbrRetryLimit_Type()
)
lmpNbrRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrRetryLimit.setStatus("current")


class _LmpNbrRetransmitDelta_Type(Unsigned32):
    """Custom type lmpNbrRetransmitDelta based on Unsigned32"""
    defaultValue = 1


_LmpNbrRetransmitDelta_Object = MibTableColumn
lmpNbrRetransmitDelta = _LmpNbrRetransmitDelta_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 4),
    _LmpNbrRetransmitDelta_Type()
)
lmpNbrRetransmitDelta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrRetransmitDelta.setStatus("current")


class _LmpNbrAdminStatus_Type(Integer32):
    """Custom type lmpNbrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LmpNbrAdminStatus_Type.__name__ = "Integer32"
_LmpNbrAdminStatus_Object = MibTableColumn
lmpNbrAdminStatus = _LmpNbrAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 5),
    _LmpNbrAdminStatus_Type()
)
lmpNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrAdminStatus.setStatus("current")


class _LmpNbrOperStatus_Type(Integer32):
    """Custom type lmpNbrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LmpNbrOperStatus_Type.__name__ = "Integer32"
_LmpNbrOperStatus_Object = MibTableColumn
lmpNbrOperStatus = _LmpNbrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 6),
    _LmpNbrOperStatus_Type()
)
lmpNbrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpNbrOperStatus.setStatus("current")
_LmpNbrRowStatus_Type = RowStatus
_LmpNbrRowStatus_Object = MibTableColumn
lmpNbrRowStatus = _LmpNbrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 7),
    _LmpNbrRowStatus_Type()
)
lmpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrRowStatus.setStatus("current")


class _LmpNbrStorageType_Type(StorageType):
    """Custom type lmpNbrStorageType based on StorageType"""


_LmpNbrStorageType_Object = MibTableColumn
lmpNbrStorageType = _LmpNbrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 3, 1, 8),
    _LmpNbrStorageType_Type()
)
lmpNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpNbrStorageType.setStatus("current")
_LmpCcHelloIntervalDefault_Type = LmpInterval
_LmpCcHelloIntervalDefault_Object = MibScalar
lmpCcHelloIntervalDefault = _LmpCcHelloIntervalDefault_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 4),
    _LmpCcHelloIntervalDefault_Type()
)
lmpCcHelloIntervalDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalDefault.setStatus("current")
_LmpCcHelloIntervalDefaultMin_Type = LmpInterval
_LmpCcHelloIntervalDefaultMin_Object = MibScalar
lmpCcHelloIntervalDefaultMin = _LmpCcHelloIntervalDefaultMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 5),
    _LmpCcHelloIntervalDefaultMin_Type()
)
lmpCcHelloIntervalDefaultMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalDefaultMin.setStatus("current")
_LmpCcHelloIntervalDefaultMax_Type = LmpInterval
_LmpCcHelloIntervalDefaultMax_Object = MibScalar
lmpCcHelloIntervalDefaultMax = _LmpCcHelloIntervalDefaultMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 6),
    _LmpCcHelloIntervalDefaultMax_Type()
)
lmpCcHelloIntervalDefaultMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalDefaultMax.setStatus("current")
_LmpCcHelloDeadIntervalDefault_Type = LmpInterval
_LmpCcHelloDeadIntervalDefault_Object = MibScalar
lmpCcHelloDeadIntervalDefault = _LmpCcHelloDeadIntervalDefault_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 7),
    _LmpCcHelloDeadIntervalDefault_Type()
)
lmpCcHelloDeadIntervalDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalDefault.setStatus("current")
_LmpCcHelloDeadIntervalDefaultMin_Type = LmpInterval
_LmpCcHelloDeadIntervalDefaultMin_Object = MibScalar
lmpCcHelloDeadIntervalDefaultMin = _LmpCcHelloDeadIntervalDefaultMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 8),
    _LmpCcHelloDeadIntervalDefaultMin_Type()
)
lmpCcHelloDeadIntervalDefaultMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalDefaultMin.setStatus("current")
_LmpCcHelloDeadIntervalDefaultMax_Type = LmpInterval
_LmpCcHelloDeadIntervalDefaultMax_Object = MibScalar
lmpCcHelloDeadIntervalDefaultMax = _LmpCcHelloDeadIntervalDefaultMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 9),
    _LmpCcHelloDeadIntervalDefaultMax_Type()
)
lmpCcHelloDeadIntervalDefaultMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalDefaultMax.setStatus("current")
_LmpControlChannelTable_Object = MibTable
lmpControlChannelTable = _LmpControlChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10)
)
if mibBuilder.loadTexts:
    lmpControlChannelTable.setStatus("current")
_LmpControlChannelEntry_Object = MibTableRow
lmpControlChannelEntry = _LmpControlChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1)
)
lmpControlChannelEntry.setIndexNames(
    (0, "LMP-MIB", "lmpCcId"),
)
if mibBuilder.loadTexts:
    lmpControlChannelEntry.setStatus("current")


class _LmpCcId_Type(Unsigned32):
    """Custom type lmpCcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LmpCcId_Type.__name__ = "Unsigned32"
_LmpCcId_Object = MibTableColumn
lmpCcId = _LmpCcId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 1),
    _LmpCcId_Type()
)
lmpCcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmpCcId.setStatus("current")
_LmpCcUnderlyingIfIndex_Type = InterfaceIndexOrZero
_LmpCcUnderlyingIfIndex_Object = MibTableColumn
lmpCcUnderlyingIfIndex = _LmpCcUnderlyingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 2),
    _LmpCcUnderlyingIfIndex_Type()
)
lmpCcUnderlyingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcUnderlyingIfIndex.setStatus("current")
_LmpCcIsIf_Type = TruthValue
_LmpCcIsIf_Object = MibTableColumn
lmpCcIsIf = _LmpCcIsIf_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 3),
    _LmpCcIsIf_Type()
)
lmpCcIsIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcIsIf.setStatus("current")
_LmpCcNbrNodeId_Type = LmpNodeId
_LmpCcNbrNodeId_Object = MibTableColumn
lmpCcNbrNodeId = _LmpCcNbrNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 4),
    _LmpCcNbrNodeId_Type()
)
lmpCcNbrNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcNbrNodeId.setStatus("current")
_LmpCcRemoteId_Type = Unsigned32
_LmpCcRemoteId_Object = MibTableColumn
lmpCcRemoteId = _LmpCcRemoteId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 5),
    _LmpCcRemoteId_Type()
)
lmpCcRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcRemoteId.setStatus("current")
_LmpCcRemoteAddressType_Type = InetAddressType
_LmpCcRemoteAddressType_Object = MibTableColumn
lmpCcRemoteAddressType = _LmpCcRemoteAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 6),
    _LmpCcRemoteAddressType_Type()
)
lmpCcRemoteAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcRemoteAddressType.setStatus("current")
_LmpCcRemoteIpAddr_Type = InetAddress
_LmpCcRemoteIpAddr_Object = MibTableColumn
lmpCcRemoteIpAddr = _LmpCcRemoteIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 7),
    _LmpCcRemoteIpAddr_Type()
)
lmpCcRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcRemoteIpAddr.setStatus("current")


class _LmpCcSetupRole_Type(Integer32):
    """Custom type lmpCcSetupRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_LmpCcSetupRole_Type.__name__ = "Integer32"
_LmpCcSetupRole_Object = MibTableColumn
lmpCcSetupRole = _LmpCcSetupRole_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 8),
    _LmpCcSetupRole_Type()
)
lmpCcSetupRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcSetupRole.setStatus("current")
_LmpCcAuthentication_Type = TruthValue
_LmpCcAuthentication_Object = MibTableColumn
lmpCcAuthentication = _LmpCcAuthentication_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 9),
    _LmpCcAuthentication_Type()
)
lmpCcAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcAuthentication.setStatus("current")
_LmpCcHelloInterval_Type = LmpInterval
_LmpCcHelloInterval_Object = MibTableColumn
lmpCcHelloInterval = _LmpCcHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 10),
    _LmpCcHelloInterval_Type()
)
lmpCcHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloInterval.setStatus("current")
_LmpCcHelloIntervalMin_Type = LmpInterval
_LmpCcHelloIntervalMin_Object = MibTableColumn
lmpCcHelloIntervalMin = _LmpCcHelloIntervalMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 11),
    _LmpCcHelloIntervalMin_Type()
)
lmpCcHelloIntervalMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalMin.setStatus("current")
_LmpCcHelloIntervalMax_Type = LmpInterval
_LmpCcHelloIntervalMax_Object = MibTableColumn
lmpCcHelloIntervalMax = _LmpCcHelloIntervalMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 12),
    _LmpCcHelloIntervalMax_Type()
)
lmpCcHelloIntervalMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalMax.setStatus("current")
_LmpCcHelloIntervalNegotiated_Type = LmpInterval
_LmpCcHelloIntervalNegotiated_Object = MibTableColumn
lmpCcHelloIntervalNegotiated = _LmpCcHelloIntervalNegotiated_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 13),
    _LmpCcHelloIntervalNegotiated_Type()
)
lmpCcHelloIntervalNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcHelloIntervalNegotiated.setStatus("current")
_LmpCcHelloDeadInterval_Type = LmpInterval
_LmpCcHelloDeadInterval_Object = MibTableColumn
lmpCcHelloDeadInterval = _LmpCcHelloDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 14),
    _LmpCcHelloDeadInterval_Type()
)
lmpCcHelloDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloDeadInterval.setStatus("current")
_LmpCcHelloDeadIntervalMin_Type = LmpInterval
_LmpCcHelloDeadIntervalMin_Object = MibTableColumn
lmpCcHelloDeadIntervalMin = _LmpCcHelloDeadIntervalMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 15),
    _LmpCcHelloDeadIntervalMin_Type()
)
lmpCcHelloDeadIntervalMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalMin.setStatus("current")
_LmpCcHelloDeadIntervalMax_Type = LmpInterval
_LmpCcHelloDeadIntervalMax_Object = MibTableColumn
lmpCcHelloDeadIntervalMax = _LmpCcHelloDeadIntervalMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 16),
    _LmpCcHelloDeadIntervalMax_Type()
)
lmpCcHelloDeadIntervalMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalMax.setStatus("current")
_LmpCcHelloDeadIntervalNegotiated_Type = LmpInterval
_LmpCcHelloDeadIntervalNegotiated_Object = MibTableColumn
lmpCcHelloDeadIntervalNegotiated = _LmpCcHelloDeadIntervalNegotiated_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 17),
    _LmpCcHelloDeadIntervalNegotiated_Type()
)
lmpCcHelloDeadIntervalNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcHelloDeadIntervalNegotiated.setStatus("current")
_LmpCcLastChange_Type = TimeTicks
_LmpCcLastChange_Object = MibTableColumn
lmpCcLastChange = _LmpCcLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 18),
    _LmpCcLastChange_Type()
)
lmpCcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLastChange.setStatus("current")


class _LmpCcAdminStatus_Type(Integer32):
    """Custom type lmpCcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LmpCcAdminStatus_Type.__name__ = "Integer32"
_LmpCcAdminStatus_Object = MibTableColumn
lmpCcAdminStatus = _LmpCcAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 19),
    _LmpCcAdminStatus_Type()
)
lmpCcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcAdminStatus.setStatus("current")


class _LmpCcOperStatus_Type(Integer32):
    """Custom type lmpCcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("configRcv", 4),
          ("configSnd", 3),
          ("down", 2),
          ("goingDown", 6),
          ("up", 1))
    )


_LmpCcOperStatus_Type.__name__ = "Integer32"
_LmpCcOperStatus_Object = MibTableColumn
lmpCcOperStatus = _LmpCcOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 20),
    _LmpCcOperStatus_Type()
)
lmpCcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcOperStatus.setStatus("current")
_LmpCcRowStatus_Type = RowStatus
_LmpCcRowStatus_Object = MibTableColumn
lmpCcRowStatus = _LmpCcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 21),
    _LmpCcRowStatus_Type()
)
lmpCcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcRowStatus.setStatus("current")


class _LmpCcStorageType_Type(StorageType):
    """Custom type lmpCcStorageType based on StorageType"""


_LmpCcStorageType_Object = MibTableColumn
lmpCcStorageType = _LmpCcStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 10, 1, 22),
    _LmpCcStorageType_Type()
)
lmpCcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpCcStorageType.setStatus("current")
_LmpControlChannelPerfTable_Object = MibTable
lmpControlChannelPerfTable = _LmpControlChannelPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11)
)
if mibBuilder.loadTexts:
    lmpControlChannelPerfTable.setStatus("current")
_LmpControlChannelPerfEntry_Object = MibTableRow
lmpControlChannelPerfEntry = _LmpControlChannelPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1)
)
lmpControlChannelPerfEntry.setIndexNames(
    (0, "LMP-MIB", "lmpCcId"),
)
if mibBuilder.loadTexts:
    lmpControlChannelPerfEntry.setStatus("current")
_LmpCcInOctets_Type = Counter32
_LmpCcInOctets_Object = MibTableColumn
lmpCcInOctets = _LmpCcInOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 1),
    _LmpCcInOctets_Type()
)
lmpCcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcInOctets.setStatus("current")
_LmpCcInDiscards_Type = Counter32
_LmpCcInDiscards_Object = MibTableColumn
lmpCcInDiscards = _LmpCcInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 2),
    _LmpCcInDiscards_Type()
)
lmpCcInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcInDiscards.setStatus("current")
_LmpCcInErrors_Type = Counter32
_LmpCcInErrors_Object = MibTableColumn
lmpCcInErrors = _LmpCcInErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 3),
    _LmpCcInErrors_Type()
)
lmpCcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcInErrors.setStatus("current")
_LmpCcOutOctets_Type = Counter32
_LmpCcOutOctets_Object = MibTableColumn
lmpCcOutOctets = _LmpCcOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 4),
    _LmpCcOutOctets_Type()
)
lmpCcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcOutOctets.setStatus("current")
_LmpCcOutDiscards_Type = Counter32
_LmpCcOutDiscards_Object = MibTableColumn
lmpCcOutDiscards = _LmpCcOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 5),
    _LmpCcOutDiscards_Type()
)
lmpCcOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcOutDiscards.setStatus("current")
_LmpCcOutErrors_Type = Counter32
_LmpCcOutErrors_Object = MibTableColumn
lmpCcOutErrors = _LmpCcOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 6),
    _LmpCcOutErrors_Type()
)
lmpCcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcOutErrors.setStatus("current")
_LmpCcConfigReceived_Type = Counter32
_LmpCcConfigReceived_Object = MibTableColumn
lmpCcConfigReceived = _LmpCcConfigReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 7),
    _LmpCcConfigReceived_Type()
)
lmpCcConfigReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigReceived.setStatus("current")
_LmpCcConfigSent_Type = Counter32
_LmpCcConfigSent_Object = MibTableColumn
lmpCcConfigSent = _LmpCcConfigSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 8),
    _LmpCcConfigSent_Type()
)
lmpCcConfigSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigSent.setStatus("current")
_LmpCcConfigRetransmit_Type = Counter32
_LmpCcConfigRetransmit_Object = MibTableColumn
lmpCcConfigRetransmit = _LmpCcConfigRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 9),
    _LmpCcConfigRetransmit_Type()
)
lmpCcConfigRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigRetransmit.setStatus("current")
_LmpCcConfigAckReceived_Type = Counter32
_LmpCcConfigAckReceived_Object = MibTableColumn
lmpCcConfigAckReceived = _LmpCcConfigAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 10),
    _LmpCcConfigAckReceived_Type()
)
lmpCcConfigAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigAckReceived.setStatus("current")
_LmpCcConfigAckSent_Type = Counter32
_LmpCcConfigAckSent_Object = MibTableColumn
lmpCcConfigAckSent = _LmpCcConfigAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 11),
    _LmpCcConfigAckSent_Type()
)
lmpCcConfigAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigAckSent.setStatus("current")
_LmpCcConfigNackReceived_Type = Counter32
_LmpCcConfigNackReceived_Object = MibTableColumn
lmpCcConfigNackReceived = _LmpCcConfigNackReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 12),
    _LmpCcConfigNackReceived_Type()
)
lmpCcConfigNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigNackReceived.setStatus("current")
_LmpCcConfigNackSent_Type = Counter32
_LmpCcConfigNackSent_Object = MibTableColumn
lmpCcConfigNackSent = _LmpCcConfigNackSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 13),
    _LmpCcConfigNackSent_Type()
)
lmpCcConfigNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcConfigNackSent.setStatus("current")
_LmpCcHelloReceived_Type = Counter32
_LmpCcHelloReceived_Object = MibTableColumn
lmpCcHelloReceived = _LmpCcHelloReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 14),
    _LmpCcHelloReceived_Type()
)
lmpCcHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcHelloReceived.setStatus("current")
_LmpCcHelloSent_Type = Counter32
_LmpCcHelloSent_Object = MibTableColumn
lmpCcHelloSent = _LmpCcHelloSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 15),
    _LmpCcHelloSent_Type()
)
lmpCcHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcHelloSent.setStatus("current")
_LmpCcBeginVerifyReceived_Type = Counter32
_LmpCcBeginVerifyReceived_Object = MibTableColumn
lmpCcBeginVerifyReceived = _LmpCcBeginVerifyReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 16),
    _LmpCcBeginVerifyReceived_Type()
)
lmpCcBeginVerifyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyReceived.setStatus("current")
_LmpCcBeginVerifySent_Type = Counter32
_LmpCcBeginVerifySent_Object = MibTableColumn
lmpCcBeginVerifySent = _LmpCcBeginVerifySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 17),
    _LmpCcBeginVerifySent_Type()
)
lmpCcBeginVerifySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifySent.setStatus("current")
_LmpCcBeginVerifyRetransmit_Type = Counter32
_LmpCcBeginVerifyRetransmit_Object = MibTableColumn
lmpCcBeginVerifyRetransmit = _LmpCcBeginVerifyRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 18),
    _LmpCcBeginVerifyRetransmit_Type()
)
lmpCcBeginVerifyRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyRetransmit.setStatus("current")
_LmpCcBeginVerifyAckReceived_Type = Counter32
_LmpCcBeginVerifyAckReceived_Object = MibTableColumn
lmpCcBeginVerifyAckReceived = _LmpCcBeginVerifyAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 19),
    _LmpCcBeginVerifyAckReceived_Type()
)
lmpCcBeginVerifyAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyAckReceived.setStatus("current")
_LmpCcBeginVerifyAckSent_Type = Counter32
_LmpCcBeginVerifyAckSent_Object = MibTableColumn
lmpCcBeginVerifyAckSent = _LmpCcBeginVerifyAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 20),
    _LmpCcBeginVerifyAckSent_Type()
)
lmpCcBeginVerifyAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyAckSent.setStatus("current")
_LmpCcBeginVerifyNackReceived_Type = Counter32
_LmpCcBeginVerifyNackReceived_Object = MibTableColumn
lmpCcBeginVerifyNackReceived = _LmpCcBeginVerifyNackReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 21),
    _LmpCcBeginVerifyNackReceived_Type()
)
lmpCcBeginVerifyNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyNackReceived.setStatus("current")
_LmpCcBeginVerifyNackSent_Type = Counter32
_LmpCcBeginVerifyNackSent_Object = MibTableColumn
lmpCcBeginVerifyNackSent = _LmpCcBeginVerifyNackSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 22),
    _LmpCcBeginVerifyNackSent_Type()
)
lmpCcBeginVerifyNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcBeginVerifyNackSent.setStatus("current")
_LmpCcEndVerifyReceived_Type = Counter32
_LmpCcEndVerifyReceived_Object = MibTableColumn
lmpCcEndVerifyReceived = _LmpCcEndVerifyReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 23),
    _LmpCcEndVerifyReceived_Type()
)
lmpCcEndVerifyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcEndVerifyReceived.setStatus("current")
_LmpCcEndVerifySent_Type = Counter32
_LmpCcEndVerifySent_Object = MibTableColumn
lmpCcEndVerifySent = _LmpCcEndVerifySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 24),
    _LmpCcEndVerifySent_Type()
)
lmpCcEndVerifySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcEndVerifySent.setStatus("current")
_LmpCcEndVerifyRetransmit_Type = Counter32
_LmpCcEndVerifyRetransmit_Object = MibTableColumn
lmpCcEndVerifyRetransmit = _LmpCcEndVerifyRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 25),
    _LmpCcEndVerifyRetransmit_Type()
)
lmpCcEndVerifyRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcEndVerifyRetransmit.setStatus("current")
_LmpCcEndVerifyAckReceived_Type = Counter32
_LmpCcEndVerifyAckReceived_Object = MibTableColumn
lmpCcEndVerifyAckReceived = _LmpCcEndVerifyAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 26),
    _LmpCcEndVerifyAckReceived_Type()
)
lmpCcEndVerifyAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcEndVerifyAckReceived.setStatus("current")
_LmpCcEndVerifyAckSent_Type = Counter32
_LmpCcEndVerifyAckSent_Object = MibTableColumn
lmpCcEndVerifyAckSent = _LmpCcEndVerifyAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 27),
    _LmpCcEndVerifyAckSent_Type()
)
lmpCcEndVerifyAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcEndVerifyAckSent.setStatus("current")
_LmpCcTestStatusSuccessReceived_Type = Counter32
_LmpCcTestStatusSuccessReceived_Object = MibTableColumn
lmpCcTestStatusSuccessReceived = _LmpCcTestStatusSuccessReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 28),
    _LmpCcTestStatusSuccessReceived_Type()
)
lmpCcTestStatusSuccessReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusSuccessReceived.setStatus("current")
_LmpCcTestStatusSuccessSent_Type = Counter32
_LmpCcTestStatusSuccessSent_Object = MibTableColumn
lmpCcTestStatusSuccessSent = _LmpCcTestStatusSuccessSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 29),
    _LmpCcTestStatusSuccessSent_Type()
)
lmpCcTestStatusSuccessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusSuccessSent.setStatus("current")
_LmpCcTestStatusSuccessRetransmit_Type = Counter32
_LmpCcTestStatusSuccessRetransmit_Object = MibTableColumn
lmpCcTestStatusSuccessRetransmit = _LmpCcTestStatusSuccessRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 30),
    _LmpCcTestStatusSuccessRetransmit_Type()
)
lmpCcTestStatusSuccessRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusSuccessRetransmit.setStatus("current")
_LmpCcTestStatusFailureReceived_Type = Counter32
_LmpCcTestStatusFailureReceived_Object = MibTableColumn
lmpCcTestStatusFailureReceived = _LmpCcTestStatusFailureReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 31),
    _LmpCcTestStatusFailureReceived_Type()
)
lmpCcTestStatusFailureReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusFailureReceived.setStatus("current")
_LmpCcTestStatusFailureSent_Type = Counter32
_LmpCcTestStatusFailureSent_Object = MibTableColumn
lmpCcTestStatusFailureSent = _LmpCcTestStatusFailureSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 32),
    _LmpCcTestStatusFailureSent_Type()
)
lmpCcTestStatusFailureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusFailureSent.setStatus("current")
_LmpCcTestStatusFailureRetransmit_Type = Counter32
_LmpCcTestStatusFailureRetransmit_Object = MibTableColumn
lmpCcTestStatusFailureRetransmit = _LmpCcTestStatusFailureRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 33),
    _LmpCcTestStatusFailureRetransmit_Type()
)
lmpCcTestStatusFailureRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusFailureRetransmit.setStatus("current")
_LmpCcTestStatusAckReceived_Type = Counter32
_LmpCcTestStatusAckReceived_Object = MibTableColumn
lmpCcTestStatusAckReceived = _LmpCcTestStatusAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 34),
    _LmpCcTestStatusAckReceived_Type()
)
lmpCcTestStatusAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusAckReceived.setStatus("current")
_LmpCcTestStatusAckSent_Type = Counter32
_LmpCcTestStatusAckSent_Object = MibTableColumn
lmpCcTestStatusAckSent = _LmpCcTestStatusAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 35),
    _LmpCcTestStatusAckSent_Type()
)
lmpCcTestStatusAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcTestStatusAckSent.setStatus("current")
_LmpCcLinkSummaryReceived_Type = Counter32
_LmpCcLinkSummaryReceived_Object = MibTableColumn
lmpCcLinkSummaryReceived = _LmpCcLinkSummaryReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 36),
    _LmpCcLinkSummaryReceived_Type()
)
lmpCcLinkSummaryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryReceived.setStatus("current")
_LmpCcLinkSummarySent_Type = Counter32
_LmpCcLinkSummarySent_Object = MibTableColumn
lmpCcLinkSummarySent = _LmpCcLinkSummarySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 37),
    _LmpCcLinkSummarySent_Type()
)
lmpCcLinkSummarySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummarySent.setStatus("current")
_LmpCcLinkSummaryRetransmit_Type = Counter32
_LmpCcLinkSummaryRetransmit_Object = MibTableColumn
lmpCcLinkSummaryRetransmit = _LmpCcLinkSummaryRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 38),
    _LmpCcLinkSummaryRetransmit_Type()
)
lmpCcLinkSummaryRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryRetransmit.setStatus("current")
_LmpCcLinkSummaryAckReceived_Type = Counter32
_LmpCcLinkSummaryAckReceived_Object = MibTableColumn
lmpCcLinkSummaryAckReceived = _LmpCcLinkSummaryAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 39),
    _LmpCcLinkSummaryAckReceived_Type()
)
lmpCcLinkSummaryAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryAckReceived.setStatus("current")
_LmpCcLinkSummaryAckSent_Type = Counter32
_LmpCcLinkSummaryAckSent_Object = MibTableColumn
lmpCcLinkSummaryAckSent = _LmpCcLinkSummaryAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 40),
    _LmpCcLinkSummaryAckSent_Type()
)
lmpCcLinkSummaryAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryAckSent.setStatus("current")
_LmpCcLinkSummaryNackReceived_Type = Counter32
_LmpCcLinkSummaryNackReceived_Object = MibTableColumn
lmpCcLinkSummaryNackReceived = _LmpCcLinkSummaryNackReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 41),
    _LmpCcLinkSummaryNackReceived_Type()
)
lmpCcLinkSummaryNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryNackReceived.setStatus("current")
_LmpCcLinkSummaryNackSent_Type = Counter32
_LmpCcLinkSummaryNackSent_Object = MibTableColumn
lmpCcLinkSummaryNackSent = _LmpCcLinkSummaryNackSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 42),
    _LmpCcLinkSummaryNackSent_Type()
)
lmpCcLinkSummaryNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcLinkSummaryNackSent.setStatus("current")
_LmpCcChannelStatusReceived_Type = Counter32
_LmpCcChannelStatusReceived_Object = MibTableColumn
lmpCcChannelStatusReceived = _LmpCcChannelStatusReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 43),
    _LmpCcChannelStatusReceived_Type()
)
lmpCcChannelStatusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusReceived.setStatus("current")
_LmpCcChannelStatusSent_Type = Counter32
_LmpCcChannelStatusSent_Object = MibTableColumn
lmpCcChannelStatusSent = _LmpCcChannelStatusSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 44),
    _LmpCcChannelStatusSent_Type()
)
lmpCcChannelStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusSent.setStatus("current")
_LmpCcChannelStatusRetransmit_Type = Counter32
_LmpCcChannelStatusRetransmit_Object = MibTableColumn
lmpCcChannelStatusRetransmit = _LmpCcChannelStatusRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 45),
    _LmpCcChannelStatusRetransmit_Type()
)
lmpCcChannelStatusRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusRetransmit.setStatus("current")
_LmpCcChannelStatusAckReceived_Type = Counter32
_LmpCcChannelStatusAckReceived_Object = MibTableColumn
lmpCcChannelStatusAckReceived = _LmpCcChannelStatusAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 46),
    _LmpCcChannelStatusAckReceived_Type()
)
lmpCcChannelStatusAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusAckReceived.setStatus("current")
_LmpCcChannelStatusAckSent_Type = Counter32
_LmpCcChannelStatusAckSent_Object = MibTableColumn
lmpCcChannelStatusAckSent = _LmpCcChannelStatusAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 47),
    _LmpCcChannelStatusAckSent_Type()
)
lmpCcChannelStatusAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusAckSent.setStatus("current")
_LmpCcChannelStatusReqReceived_Type = Counter32
_LmpCcChannelStatusReqReceived_Object = MibTableColumn
lmpCcChannelStatusReqReceived = _LmpCcChannelStatusReqReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 48),
    _LmpCcChannelStatusReqReceived_Type()
)
lmpCcChannelStatusReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusReqReceived.setStatus("current")
_LmpCcChannelStatusReqSent_Type = Counter32
_LmpCcChannelStatusReqSent_Object = MibTableColumn
lmpCcChannelStatusReqSent = _LmpCcChannelStatusReqSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 49),
    _LmpCcChannelStatusReqSent_Type()
)
lmpCcChannelStatusReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusReqSent.setStatus("current")
_LmpCcChannelStatusReqRetransmit_Type = Counter32
_LmpCcChannelStatusReqRetransmit_Object = MibTableColumn
lmpCcChannelStatusReqRetransmit = _LmpCcChannelStatusReqRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 50),
    _LmpCcChannelStatusReqRetransmit_Type()
)
lmpCcChannelStatusReqRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusReqRetransmit.setStatus("current")
_LmpCcChannelStatusRspReceived_Type = Counter32
_LmpCcChannelStatusRspReceived_Object = MibTableColumn
lmpCcChannelStatusRspReceived = _LmpCcChannelStatusRspReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 51),
    _LmpCcChannelStatusRspReceived_Type()
)
lmpCcChannelStatusRspReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusRspReceived.setStatus("current")
_LmpCcChannelStatusRspSent_Type = Counter32
_LmpCcChannelStatusRspSent_Object = MibTableColumn
lmpCcChannelStatusRspSent = _LmpCcChannelStatusRspSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 52),
    _LmpCcChannelStatusRspSent_Type()
)
lmpCcChannelStatusRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcChannelStatusRspSent.setStatus("current")
_LmpCcCounterDiscontinuityTime_Type = TimeStamp
_LmpCcCounterDiscontinuityTime_Object = MibTableColumn
lmpCcCounterDiscontinuityTime = _LmpCcCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 11, 1, 53),
    _LmpCcCounterDiscontinuityTime_Type()
)
lmpCcCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpCcCounterDiscontinuityTime.setStatus("current")
_LmpTeLinkTable_Object = MibTable
lmpTeLinkTable = _LmpTeLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12)
)
if mibBuilder.loadTexts:
    lmpTeLinkTable.setStatus("current")
_LmpTeLinkEntry_Object = MibTableRow
lmpTeLinkEntry = _LmpTeLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1)
)
lmpTeLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmpTeLinkEntry.setStatus("current")
_LmpTeLinkNbrRemoteNodeId_Type = LmpNodeId
_LmpTeLinkNbrRemoteNodeId_Object = MibTableColumn
lmpTeLinkNbrRemoteNodeId = _LmpTeLinkNbrRemoteNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 1),
    _LmpTeLinkNbrRemoteNodeId_Type()
)
lmpTeLinkNbrRemoteNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkNbrRemoteNodeId.setStatus("current")
_LmpTeLinkVerification_Type = TruthValue
_LmpTeLinkVerification_Object = MibTableColumn
lmpTeLinkVerification = _LmpTeLinkVerification_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 2),
    _LmpTeLinkVerification_Type()
)
lmpTeLinkVerification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkVerification.setStatus("current")
_LmpTeLinkFaultManagement_Type = TruthValue
_LmpTeLinkFaultManagement_Object = MibTableColumn
lmpTeLinkFaultManagement = _LmpTeLinkFaultManagement_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 3),
    _LmpTeLinkFaultManagement_Type()
)
lmpTeLinkFaultManagement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkFaultManagement.setStatus("current")
_LmpTeLinkDwdm_Type = TruthValue
_LmpTeLinkDwdm_Object = MibTableColumn
lmpTeLinkDwdm = _LmpTeLinkDwdm_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 4),
    _LmpTeLinkDwdm_Type()
)
lmpTeLinkDwdm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkDwdm.setStatus("current")


class _LmpTeLinkOperStatus_Type(Integer32):
    """Custom type lmpTeLinkOperStatus based on Integer32"""
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
        *(("degraded", 5),
          ("down", 2),
          ("init", 4),
          ("testing", 3),
          ("up", 1))
    )


_LmpTeLinkOperStatus_Type.__name__ = "Integer32"
_LmpTeLinkOperStatus_Object = MibTableColumn
lmpTeLinkOperStatus = _LmpTeLinkOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 5),
    _LmpTeLinkOperStatus_Type()
)
lmpTeLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkOperStatus.setStatus("current")
_LmpTeLinkRowStatus_Type = RowStatus
_LmpTeLinkRowStatus_Object = MibTableColumn
lmpTeLinkRowStatus = _LmpTeLinkRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 6),
    _LmpTeLinkRowStatus_Type()
)
lmpTeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkRowStatus.setStatus("current")


class _LmpTeLinkStorageType_Type(StorageType):
    """Custom type lmpTeLinkStorageType based on StorageType"""


_LmpTeLinkStorageType_Object = MibTableColumn
lmpTeLinkStorageType = _LmpTeLinkStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 12, 1, 7),
    _LmpTeLinkStorageType_Type()
)
lmpTeLinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpTeLinkStorageType.setStatus("current")
_LmpGlobalLinkVerificationInterval_Type = Unsigned32
_LmpGlobalLinkVerificationInterval_Object = MibScalar
lmpGlobalLinkVerificationInterval = _LmpGlobalLinkVerificationInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 13),
    _LmpGlobalLinkVerificationInterval_Type()
)
lmpGlobalLinkVerificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpGlobalLinkVerificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    lmpGlobalLinkVerificationInterval.setUnits("milliseconds")
_LmpLinkVerificationTable_Object = MibTable
lmpLinkVerificationTable = _LmpLinkVerificationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14)
)
if mibBuilder.loadTexts:
    lmpLinkVerificationTable.setStatus("current")
_LmpLinkVerificationEntry_Object = MibTableRow
lmpLinkVerificationEntry = _LmpLinkVerificationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1)
)
lmpLinkVerificationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmpLinkVerificationEntry.setStatus("current")
_LmpLinkVerifyInterval_Type = LmpInterval
_LmpLinkVerifyInterval_Object = MibTableColumn
lmpLinkVerifyInterval = _LmpLinkVerifyInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 1),
    _LmpLinkVerifyInterval_Type()
)
lmpLinkVerifyInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyInterval.setStatus("current")
_LmpLinkVerifyDeadInterval_Type = LmpInterval
_LmpLinkVerifyDeadInterval_Object = MibTableColumn
lmpLinkVerifyDeadInterval = _LmpLinkVerifyDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 2),
    _LmpLinkVerifyDeadInterval_Type()
)
lmpLinkVerifyDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyDeadInterval.setStatus("current")


class _LmpLinkVerifyTransportMechanism_Type(Bits):
    """Custom type lmpLinkVerifyTransportMechanism based on Bits"""
    namedValues = NamedValues(
        *(("dccLineOverheadBytes", 2),
          ("dccSectionOverheadBytes", 1),
          ("j0Trace", 3),
          ("j1Trace", 4),
          ("j2Trace", 5),
          ("payload", 0))
    )

_LmpLinkVerifyTransportMechanism_Type.__name__ = "Bits"
_LmpLinkVerifyTransportMechanism_Object = MibTableColumn
lmpLinkVerifyTransportMechanism = _LmpLinkVerifyTransportMechanism_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 3),
    _LmpLinkVerifyTransportMechanism_Type()
)
lmpLinkVerifyTransportMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyTransportMechanism.setStatus("current")
_LmpLinkVerifyAllLinks_Type = TruthValue
_LmpLinkVerifyAllLinks_Object = MibTableColumn
lmpLinkVerifyAllLinks = _LmpLinkVerifyAllLinks_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 4),
    _LmpLinkVerifyAllLinks_Type()
)
lmpLinkVerifyAllLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyAllLinks.setStatus("current")
_LmpLinkVerifyTransmissionRate_Type = Unsigned32
_LmpLinkVerifyTransmissionRate_Object = MibTableColumn
lmpLinkVerifyTransmissionRate = _LmpLinkVerifyTransmissionRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 5),
    _LmpLinkVerifyTransmissionRate_Type()
)
lmpLinkVerifyTransmissionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyTransmissionRate.setStatus("current")
if mibBuilder.loadTexts:
    lmpLinkVerifyTransmissionRate.setUnits("bytes per second")
_LmpLinkVerifyWavelength_Type = Unsigned32
_LmpLinkVerifyWavelength_Object = MibTableColumn
lmpLinkVerifyWavelength = _LmpLinkVerifyWavelength_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 6),
    _LmpLinkVerifyWavelength_Type()
)
lmpLinkVerifyWavelength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyWavelength.setStatus("current")
if mibBuilder.loadTexts:
    lmpLinkVerifyWavelength.setUnits("nanometers")
_LmpLinkVerifyRowStatus_Type = RowStatus
_LmpLinkVerifyRowStatus_Object = MibTableColumn
lmpLinkVerifyRowStatus = _LmpLinkVerifyRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 7),
    _LmpLinkVerifyRowStatus_Type()
)
lmpLinkVerifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyRowStatus.setStatus("current")


class _LmpLinkVerifyStorageType_Type(StorageType):
    """Custom type lmpLinkVerifyStorageType based on StorageType"""


_LmpLinkVerifyStorageType_Object = MibTableColumn
lmpLinkVerifyStorageType = _LmpLinkVerifyStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 14, 1, 8),
    _LmpLinkVerifyStorageType_Type()
)
lmpLinkVerifyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpLinkVerifyStorageType.setStatus("current")
_LmpTeLinkPerfTable_Object = MibTable
lmpTeLinkPerfTable = _LmpTeLinkPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15)
)
if mibBuilder.loadTexts:
    lmpTeLinkPerfTable.setStatus("current")
_LmpTeLinkPerfEntry_Object = MibTableRow
lmpTeLinkPerfEntry = _LmpTeLinkPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1)
)
lmpTeLinkPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmpTeLinkPerfEntry.setStatus("current")
_LmpTeInOctets_Type = Counter32
_LmpTeInOctets_Object = MibTableColumn
lmpTeInOctets = _LmpTeInOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 1),
    _LmpTeInOctets_Type()
)
lmpTeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeInOctets.setStatus("current")
_LmpTeOutOctets_Type = Counter32
_LmpTeOutOctets_Object = MibTableColumn
lmpTeOutOctets = _LmpTeOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 2),
    _LmpTeOutOctets_Type()
)
lmpTeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeOutOctets.setStatus("current")
_LmpTeBeginVerifyReceived_Type = Counter32
_LmpTeBeginVerifyReceived_Object = MibTableColumn
lmpTeBeginVerifyReceived = _LmpTeBeginVerifyReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 3),
    _LmpTeBeginVerifyReceived_Type()
)
lmpTeBeginVerifyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyReceived.setStatus("current")
_LmpTeBeginVerifySent_Type = Counter32
_LmpTeBeginVerifySent_Object = MibTableColumn
lmpTeBeginVerifySent = _LmpTeBeginVerifySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 4),
    _LmpTeBeginVerifySent_Type()
)
lmpTeBeginVerifySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifySent.setStatus("current")
_LmpTeBeginVerifyRetransmit_Type = Counter32
_LmpTeBeginVerifyRetransmit_Object = MibTableColumn
lmpTeBeginVerifyRetransmit = _LmpTeBeginVerifyRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 5),
    _LmpTeBeginVerifyRetransmit_Type()
)
lmpTeBeginVerifyRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyRetransmit.setStatus("current")
_LmpTeBeginVerifyAckReceived_Type = Counter32
_LmpTeBeginVerifyAckReceived_Object = MibTableColumn
lmpTeBeginVerifyAckReceived = _LmpTeBeginVerifyAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 6),
    _LmpTeBeginVerifyAckReceived_Type()
)
lmpTeBeginVerifyAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyAckReceived.setStatus("current")
_LmpTeBeginVerifyAckSent_Type = Counter32
_LmpTeBeginVerifyAckSent_Object = MibTableColumn
lmpTeBeginVerifyAckSent = _LmpTeBeginVerifyAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 7),
    _LmpTeBeginVerifyAckSent_Type()
)
lmpTeBeginVerifyAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyAckSent.setStatus("current")
_LmpTeBeginVerifyNackReceived_Type = Counter32
_LmpTeBeginVerifyNackReceived_Object = MibTableColumn
lmpTeBeginVerifyNackReceived = _LmpTeBeginVerifyNackReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 8),
    _LmpTeBeginVerifyNackReceived_Type()
)
lmpTeBeginVerifyNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyNackReceived.setStatus("current")
_LmpTeBeginVerifyNackSent_Type = Counter32
_LmpTeBeginVerifyNackSent_Object = MibTableColumn
lmpTeBeginVerifyNackSent = _LmpTeBeginVerifyNackSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 9),
    _LmpTeBeginVerifyNackSent_Type()
)
lmpTeBeginVerifyNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeBeginVerifyNackSent.setStatus("current")
_LmpTeEndVerifyReceived_Type = Counter32
_LmpTeEndVerifyReceived_Object = MibTableColumn
lmpTeEndVerifyReceived = _LmpTeEndVerifyReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 10),
    _LmpTeEndVerifyReceived_Type()
)
lmpTeEndVerifyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeEndVerifyReceived.setStatus("current")
_LmpTeEndVerifySent_Type = Counter32
_LmpTeEndVerifySent_Object = MibTableColumn
lmpTeEndVerifySent = _LmpTeEndVerifySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 11),
    _LmpTeEndVerifySent_Type()
)
lmpTeEndVerifySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeEndVerifySent.setStatus("current")
_LmpTeEndVerifyRetransmit_Type = Counter32
_LmpTeEndVerifyRetransmit_Object = MibTableColumn
lmpTeEndVerifyRetransmit = _LmpTeEndVerifyRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 12),
    _LmpTeEndVerifyRetransmit_Type()
)
lmpTeEndVerifyRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeEndVerifyRetransmit.setStatus("current")
_LmpTeEndVerifyAckReceived_Type = Counter32
_LmpTeEndVerifyAckReceived_Object = MibTableColumn
lmpTeEndVerifyAckReceived = _LmpTeEndVerifyAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 13),
    _LmpTeEndVerifyAckReceived_Type()
)
lmpTeEndVerifyAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeEndVerifyAckReceived.setStatus("current")
_LmpTeEndVerifyAckSent_Type = Counter32
_LmpTeEndVerifyAckSent_Object = MibTableColumn
lmpTeEndVerifyAckSent = _LmpTeEndVerifyAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 14),
    _LmpTeEndVerifyAckSent_Type()
)
lmpTeEndVerifyAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeEndVerifyAckSent.setStatus("current")
_LmpTeTestStatusSuccessReceived_Type = Counter32
_LmpTeTestStatusSuccessReceived_Object = MibTableColumn
lmpTeTestStatusSuccessReceived = _LmpTeTestStatusSuccessReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 15),
    _LmpTeTestStatusSuccessReceived_Type()
)
lmpTeTestStatusSuccessReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusSuccessReceived.setStatus("current")
_LmpTeTestStatusSuccessSent_Type = Counter32
_LmpTeTestStatusSuccessSent_Object = MibTableColumn
lmpTeTestStatusSuccessSent = _LmpTeTestStatusSuccessSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 16),
    _LmpTeTestStatusSuccessSent_Type()
)
lmpTeTestStatusSuccessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusSuccessSent.setStatus("current")
_LmpTeTestStatusSuccessRetransmit_Type = Counter32
_LmpTeTestStatusSuccessRetransmit_Object = MibTableColumn
lmpTeTestStatusSuccessRetransmit = _LmpTeTestStatusSuccessRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 17),
    _LmpTeTestStatusSuccessRetransmit_Type()
)
lmpTeTestStatusSuccessRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusSuccessRetransmit.setStatus("current")
_LmpTeTestStatusFailureReceived_Type = Counter32
_LmpTeTestStatusFailureReceived_Object = MibTableColumn
lmpTeTestStatusFailureReceived = _LmpTeTestStatusFailureReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 18),
    _LmpTeTestStatusFailureReceived_Type()
)
lmpTeTestStatusFailureReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusFailureReceived.setStatus("current")
_LmpTeTestStatusFailureSent_Type = Counter32
_LmpTeTestStatusFailureSent_Object = MibTableColumn
lmpTeTestStatusFailureSent = _LmpTeTestStatusFailureSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 19),
    _LmpTeTestStatusFailureSent_Type()
)
lmpTeTestStatusFailureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusFailureSent.setStatus("current")
_LmpTeTestStatusFailureRetransmit_Type = Counter32
_LmpTeTestStatusFailureRetransmit_Object = MibTableColumn
lmpTeTestStatusFailureRetransmit = _LmpTeTestStatusFailureRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 20),
    _LmpTeTestStatusFailureRetransmit_Type()
)
lmpTeTestStatusFailureRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusFailureRetransmit.setStatus("current")
_LmpTeTestStatusAckReceived_Type = Counter32
_LmpTeTestStatusAckReceived_Object = MibTableColumn
lmpTeTestStatusAckReceived = _LmpTeTestStatusAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 21),
    _LmpTeTestStatusAckReceived_Type()
)
lmpTeTestStatusAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusAckReceived.setStatus("current")
_LmpTeTestStatusAckSent_Type = Counter32
_LmpTeTestStatusAckSent_Object = MibTableColumn
lmpTeTestStatusAckSent = _LmpTeTestStatusAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 22),
    _LmpTeTestStatusAckSent_Type()
)
lmpTeTestStatusAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeTestStatusAckSent.setStatus("current")
_LmpTeLinkSummaryReceived_Type = Counter32
_LmpTeLinkSummaryReceived_Object = MibTableColumn
lmpTeLinkSummaryReceived = _LmpTeLinkSummaryReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 23),
    _LmpTeLinkSummaryReceived_Type()
)
lmpTeLinkSummaryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryReceived.setStatus("current")
_LmpTeLinkSummarySent_Type = Counter32
_LmpTeLinkSummarySent_Object = MibTableColumn
lmpTeLinkSummarySent = _LmpTeLinkSummarySent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 24),
    _LmpTeLinkSummarySent_Type()
)
lmpTeLinkSummarySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummarySent.setStatus("current")
_LmpTeLinkSummaryRetransmit_Type = Counter32
_LmpTeLinkSummaryRetransmit_Object = MibTableColumn
lmpTeLinkSummaryRetransmit = _LmpTeLinkSummaryRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 25),
    _LmpTeLinkSummaryRetransmit_Type()
)
lmpTeLinkSummaryRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryRetransmit.setStatus("current")
_LmpTeLinkSummaryAckReceived_Type = Counter32
_LmpTeLinkSummaryAckReceived_Object = MibTableColumn
lmpTeLinkSummaryAckReceived = _LmpTeLinkSummaryAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 26),
    _LmpTeLinkSummaryAckReceived_Type()
)
lmpTeLinkSummaryAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryAckReceived.setStatus("current")
_LmpTeLinkSummaryAckSent_Type = Counter32
_LmpTeLinkSummaryAckSent_Object = MibTableColumn
lmpTeLinkSummaryAckSent = _LmpTeLinkSummaryAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 27),
    _LmpTeLinkSummaryAckSent_Type()
)
lmpTeLinkSummaryAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryAckSent.setStatus("current")
_LmpTeLinkSummaryNackReceived_Type = Counter32
_LmpTeLinkSummaryNackReceived_Object = MibTableColumn
lmpTeLinkSummaryNackReceived = _LmpTeLinkSummaryNackReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 28),
    _LmpTeLinkSummaryNackReceived_Type()
)
lmpTeLinkSummaryNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryNackReceived.setStatus("current")
_LmpTeLinkSummaryNackSent_Type = Counter32
_LmpTeLinkSummaryNackSent_Object = MibTableColumn
lmpTeLinkSummaryNackSent = _LmpTeLinkSummaryNackSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 29),
    _LmpTeLinkSummaryNackSent_Type()
)
lmpTeLinkSummaryNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeLinkSummaryNackSent.setStatus("current")
_LmpTeChannelStatusReceived_Type = Counter32
_LmpTeChannelStatusReceived_Object = MibTableColumn
lmpTeChannelStatusReceived = _LmpTeChannelStatusReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 30),
    _LmpTeChannelStatusReceived_Type()
)
lmpTeChannelStatusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusReceived.setStatus("current")
_LmpTeChannelStatusSent_Type = Counter32
_LmpTeChannelStatusSent_Object = MibTableColumn
lmpTeChannelStatusSent = _LmpTeChannelStatusSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 31),
    _LmpTeChannelStatusSent_Type()
)
lmpTeChannelStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusSent.setStatus("current")
_LmpTeChannelStatusRetransmit_Type = Counter32
_LmpTeChannelStatusRetransmit_Object = MibTableColumn
lmpTeChannelStatusRetransmit = _LmpTeChannelStatusRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 32),
    _LmpTeChannelStatusRetransmit_Type()
)
lmpTeChannelStatusRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusRetransmit.setStatus("current")
_LmpTeChannelStatusAckReceived_Type = Counter32
_LmpTeChannelStatusAckReceived_Object = MibTableColumn
lmpTeChannelStatusAckReceived = _LmpTeChannelStatusAckReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 33),
    _LmpTeChannelStatusAckReceived_Type()
)
lmpTeChannelStatusAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusAckReceived.setStatus("current")
_LmpTeChannelStatusAckSent_Type = Counter32
_LmpTeChannelStatusAckSent_Object = MibTableColumn
lmpTeChannelStatusAckSent = _LmpTeChannelStatusAckSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 34),
    _LmpTeChannelStatusAckSent_Type()
)
lmpTeChannelStatusAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusAckSent.setStatus("current")
_LmpTeChannelStatusReqReceived_Type = Counter32
_LmpTeChannelStatusReqReceived_Object = MibTableColumn
lmpTeChannelStatusReqReceived = _LmpTeChannelStatusReqReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 35),
    _LmpTeChannelStatusReqReceived_Type()
)
lmpTeChannelStatusReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusReqReceived.setStatus("current")
_LmpTeChannelStatusReqSent_Type = Counter32
_LmpTeChannelStatusReqSent_Object = MibTableColumn
lmpTeChannelStatusReqSent = _LmpTeChannelStatusReqSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 36),
    _LmpTeChannelStatusReqSent_Type()
)
lmpTeChannelStatusReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusReqSent.setStatus("current")
_LmpTeChannelStatusReqRetransmit_Type = Counter32
_LmpTeChannelStatusReqRetransmit_Object = MibTableColumn
lmpTeChannelStatusReqRetransmit = _LmpTeChannelStatusReqRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 37),
    _LmpTeChannelStatusReqRetransmit_Type()
)
lmpTeChannelStatusReqRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusReqRetransmit.setStatus("current")
_LmpTeChannelStatusRspReceived_Type = Counter32
_LmpTeChannelStatusRspReceived_Object = MibTableColumn
lmpTeChannelStatusRspReceived = _LmpTeChannelStatusRspReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 38),
    _LmpTeChannelStatusRspReceived_Type()
)
lmpTeChannelStatusRspReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusRspReceived.setStatus("current")
_LmpTeChannelStatusRspSent_Type = Counter32
_LmpTeChannelStatusRspSent_Object = MibTableColumn
lmpTeChannelStatusRspSent = _LmpTeChannelStatusRspSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 39),
    _LmpTeChannelStatusRspSent_Type()
)
lmpTeChannelStatusRspSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeChannelStatusRspSent.setStatus("current")
_LmpTeCounterDiscontinuityTime_Type = TimeStamp
_LmpTeCounterDiscontinuityTime_Object = MibTableColumn
lmpTeCounterDiscontinuityTime = _LmpTeCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 15, 1, 40),
    _LmpTeCounterDiscontinuityTime_Type()
)
lmpTeCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpTeCounterDiscontinuityTime.setStatus("current")
_LmpDataLinkTable_Object = MibTable
lmpDataLinkTable = _LmpDataLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16)
)
if mibBuilder.loadTexts:
    lmpDataLinkTable.setStatus("current")
_LmpDataLinkEntry_Object = MibTableRow
lmpDataLinkEntry = _LmpDataLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1)
)
lmpDataLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmpDataLinkEntry.setStatus("current")


class _LmpDataLinkType_Type(Integer32):
    """Custom type lmpDataLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("componentLink", 2),
          ("port", 1))
    )


_LmpDataLinkType_Type.__name__ = "Integer32"
_LmpDataLinkType_Object = MibTableColumn
lmpDataLinkType = _LmpDataLinkType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 1),
    _LmpDataLinkType_Type()
)
lmpDataLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkType.setStatus("current")
_LmpDataLinkAddressType_Type = InetAddressType
_LmpDataLinkAddressType_Object = MibTableColumn
lmpDataLinkAddressType = _LmpDataLinkAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 2),
    _LmpDataLinkAddressType_Type()
)
lmpDataLinkAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkAddressType.setStatus("current")
_LmpDataLinkIpAddr_Type = InetAddress
_LmpDataLinkIpAddr_Object = MibTableColumn
lmpDataLinkIpAddr = _LmpDataLinkIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 3),
    _LmpDataLinkIpAddr_Type()
)
lmpDataLinkIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkIpAddr.setStatus("current")
_LmpDataLinkRemoteIpAddress_Type = InetAddress
_LmpDataLinkRemoteIpAddress_Object = MibTableColumn
lmpDataLinkRemoteIpAddress = _LmpDataLinkRemoteIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 4),
    _LmpDataLinkRemoteIpAddress_Type()
)
lmpDataLinkRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkRemoteIpAddress.setStatus("current")
_LmpDataLinkRemoteIfId_Type = InterfaceIndexOrZero
_LmpDataLinkRemoteIfId_Object = MibTableColumn
lmpDataLinkRemoteIfId = _LmpDataLinkRemoteIfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 5),
    _LmpDataLinkRemoteIfId_Type()
)
lmpDataLinkRemoteIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkRemoteIfId.setStatus("current")
_LmpDataLinkEncodingType_Type = TeLinkEncodingType
_LmpDataLinkEncodingType_Object = MibTableColumn
lmpDataLinkEncodingType = _LmpDataLinkEncodingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 6),
    _LmpDataLinkEncodingType_Type()
)
lmpDataLinkEncodingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkEncodingType.setStatus("current")


class _LmpDataLinkActiveOperStatus_Type(Integer32):
    """Custom type lmpDataLinkActiveOperStatus based on Integer32"""
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
        *(("down", 3),
          ("testing", 4),
          ("upAlloc", 1),
          ("upFree", 2))
    )


_LmpDataLinkActiveOperStatus_Type.__name__ = "Integer32"
_LmpDataLinkActiveOperStatus_Object = MibTableColumn
lmpDataLinkActiveOperStatus = _LmpDataLinkActiveOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 7),
    _LmpDataLinkActiveOperStatus_Type()
)
lmpDataLinkActiveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkActiveOperStatus.setStatus("current")


class _LmpDataLinkPassiveOperStatus_Type(Integer32):
    """Custom type lmpDataLinkPassiveOperStatus based on Integer32"""
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
        *(("down", 3),
          ("psvTst", 4),
          ("upAlloc", 1),
          ("upFree", 2))
    )


_LmpDataLinkPassiveOperStatus_Type.__name__ = "Integer32"
_LmpDataLinkPassiveOperStatus_Object = MibTableColumn
lmpDataLinkPassiveOperStatus = _LmpDataLinkPassiveOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 8),
    _LmpDataLinkPassiveOperStatus_Type()
)
lmpDataLinkPassiveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkPassiveOperStatus.setStatus("current")
_LmpDataLinkRowStatus_Type = RowStatus
_LmpDataLinkRowStatus_Object = MibTableColumn
lmpDataLinkRowStatus = _LmpDataLinkRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 9),
    _LmpDataLinkRowStatus_Type()
)
lmpDataLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkRowStatus.setStatus("current")


class _LmpDataLinkStorageType_Type(StorageType):
    """Custom type lmpDataLinkStorageType based on StorageType"""


_LmpDataLinkStorageType_Object = MibTableColumn
lmpDataLinkStorageType = _LmpDataLinkStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 16, 1, 10),
    _LmpDataLinkStorageType_Type()
)
lmpDataLinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lmpDataLinkStorageType.setStatus("current")
_LmpDataLinkPerfTable_Object = MibTable
lmpDataLinkPerfTable = _LmpDataLinkPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17)
)
if mibBuilder.loadTexts:
    lmpDataLinkPerfTable.setStatus("current")
_LmpDataLinkPerfEntry_Object = MibTableRow
lmpDataLinkPerfEntry = _LmpDataLinkPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1)
)
lmpDataLinkPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmpDataLinkPerfEntry.setStatus("current")
_LmpDataLinkTestReceived_Type = Counter32
_LmpDataLinkTestReceived_Object = MibTableColumn
lmpDataLinkTestReceived = _LmpDataLinkTestReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 1),
    _LmpDataLinkTestReceived_Type()
)
lmpDataLinkTestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkTestReceived.setStatus("current")
_LmpDataLinkTestSent_Type = Counter32
_LmpDataLinkTestSent_Object = MibTableColumn
lmpDataLinkTestSent = _LmpDataLinkTestSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 2),
    _LmpDataLinkTestSent_Type()
)
lmpDataLinkTestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkTestSent.setStatus("current")
_LmpDataLinkActiveTestSuccess_Type = Counter32
_LmpDataLinkActiveTestSuccess_Object = MibTableColumn
lmpDataLinkActiveTestSuccess = _LmpDataLinkActiveTestSuccess_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 3),
    _LmpDataLinkActiveTestSuccess_Type()
)
lmpDataLinkActiveTestSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkActiveTestSuccess.setStatus("current")
_LmpDataLinkActiveTestFailure_Type = Counter32
_LmpDataLinkActiveTestFailure_Object = MibTableColumn
lmpDataLinkActiveTestFailure = _LmpDataLinkActiveTestFailure_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 4),
    _LmpDataLinkActiveTestFailure_Type()
)
lmpDataLinkActiveTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkActiveTestFailure.setStatus("current")
_LmpDataLinkPassiveTestSuccess_Type = Counter32
_LmpDataLinkPassiveTestSuccess_Object = MibTableColumn
lmpDataLinkPassiveTestSuccess = _LmpDataLinkPassiveTestSuccess_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 5),
    _LmpDataLinkPassiveTestSuccess_Type()
)
lmpDataLinkPassiveTestSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkPassiveTestSuccess.setStatus("current")
_LmpDataLinkPassiveTestFailure_Type = Counter32
_LmpDataLinkPassiveTestFailure_Object = MibTableColumn
lmpDataLinkPassiveTestFailure = _LmpDataLinkPassiveTestFailure_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 6),
    _LmpDataLinkPassiveTestFailure_Type()
)
lmpDataLinkPassiveTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkPassiveTestFailure.setStatus("current")
_LmpDataLinkDiscontinuityTime_Type = TimeStamp
_LmpDataLinkDiscontinuityTime_Object = MibTableColumn
lmpDataLinkDiscontinuityTime = _LmpDataLinkDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 17, 1, 7),
    _LmpDataLinkDiscontinuityTime_Type()
)
lmpDataLinkDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmpDataLinkDiscontinuityTime.setStatus("current")
_LmpNotificationMaxRate_Type = Unsigned32
_LmpNotificationMaxRate_Object = MibScalar
lmpNotificationMaxRate = _LmpNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 18),
    _LmpNotificationMaxRate_Type()
)
lmpNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpNotificationMaxRate.setStatus("current")


class _LmpLinkPropertyNotificationsEnabled_Type(TruthValue):
    """Custom type lmpLinkPropertyNotificationsEnabled based on TruthValue"""


_LmpLinkPropertyNotificationsEnabled_Object = MibScalar
lmpLinkPropertyNotificationsEnabled = _LmpLinkPropertyNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 19),
    _LmpLinkPropertyNotificationsEnabled_Type()
)
lmpLinkPropertyNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpLinkPropertyNotificationsEnabled.setStatus("current")


class _LmpUnprotectedNotificationsEnabled_Type(TruthValue):
    """Custom type lmpUnprotectedNotificationsEnabled based on TruthValue"""


_LmpUnprotectedNotificationsEnabled_Object = MibScalar
lmpUnprotectedNotificationsEnabled = _LmpUnprotectedNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 20),
    _LmpUnprotectedNotificationsEnabled_Type()
)
lmpUnprotectedNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpUnprotectedNotificationsEnabled.setStatus("current")


class _LmpCcUpDownNotificationsEnabled_Type(TruthValue):
    """Custom type lmpCcUpDownNotificationsEnabled based on TruthValue"""


_LmpCcUpDownNotificationsEnabled_Object = MibScalar
lmpCcUpDownNotificationsEnabled = _LmpCcUpDownNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 21),
    _LmpCcUpDownNotificationsEnabled_Type()
)
lmpCcUpDownNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpCcUpDownNotificationsEnabled.setStatus("current")


class _LmpTeLinkNotificationsEnabled_Type(TruthValue):
    """Custom type lmpTeLinkNotificationsEnabled based on TruthValue"""


_LmpTeLinkNotificationsEnabled_Object = MibScalar
lmpTeLinkNotificationsEnabled = _LmpTeLinkNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 22),
    _LmpTeLinkNotificationsEnabled_Type()
)
lmpTeLinkNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpTeLinkNotificationsEnabled.setStatus("current")


class _LmpDataLinkNotificationsEnabled_Type(TruthValue):
    """Custom type lmpDataLinkNotificationsEnabled based on TruthValue"""


_LmpDataLinkNotificationsEnabled_Object = MibScalar
lmpDataLinkNotificationsEnabled = _LmpDataLinkNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 227, 1, 23),
    _LmpDataLinkNotificationsEnabled_Type()
)
lmpDataLinkNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmpDataLinkNotificationsEnabled.setStatus("current")
_LmpConformance_ObjectIdentity = ObjectIdentity
lmpConformance = _LmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227, 2)
)
_LmpCompliances_ObjectIdentity = ObjectIdentity
lmpCompliances = _LmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 1)
)
_LmpGroups_ObjectIdentity = ObjectIdentity
lmpGroups = _LmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2)
)

# Managed Objects groups

lmpNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 1)
)
lmpNodeGroup.setObjects(
      *(("LMP-MIB", "lmpAdminStatus"),
        ("LMP-MIB", "lmpOperStatus"),
        ("LMP-MIB", "lmpNbrAdminStatus"),
        ("LMP-MIB", "lmpNbrOperStatus"),
        ("LMP-MIB", "lmpNbrRowStatus"),
        ("LMP-MIB", "lmpNbrStorageType"),
        ("LMP-MIB", "lmpUnprotectedNotificationsEnabled"),
        ("LMP-MIB", "lmpNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    lmpNodeGroup.setStatus("current")

lmpControlChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 2)
)
lmpControlChannelGroup.setObjects(
      *(("LMP-MIB", "lmpNbrRetransmitInterval"),
        ("LMP-MIB", "lmpNbrRetryLimit"),
        ("LMP-MIB", "lmpNbrRetransmitDelta"),
        ("LMP-MIB", "lmpNbrAdminStatus"),
        ("LMP-MIB", "lmpNbrOperStatus"),
        ("LMP-MIB", "lmpNbrRowStatus"),
        ("LMP-MIB", "lmpNbrStorageType"),
        ("LMP-MIB", "lmpCcHelloIntervalDefault"),
        ("LMP-MIB", "lmpCcHelloIntervalDefaultMin"),
        ("LMP-MIB", "lmpCcHelloIntervalDefaultMax"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalDefault"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalDefaultMin"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalDefaultMax"),
        ("LMP-MIB", "lmpCcNbrNodeId"),
        ("LMP-MIB", "lmpCcRemoteId"),
        ("LMP-MIB", "lmpCcRemoteAddressType"),
        ("LMP-MIB", "lmpCcRemoteIpAddr"),
        ("LMP-MIB", "lmpCcSetupRole"),
        ("LMP-MIB", "lmpCcAuthentication"),
        ("LMP-MIB", "lmpCcHelloInterval"),
        ("LMP-MIB", "lmpCcHelloIntervalMin"),
        ("LMP-MIB", "lmpCcHelloIntervalMax"),
        ("LMP-MIB", "lmpCcHelloIntervalNegotiated"),
        ("LMP-MIB", "lmpCcHelloDeadInterval"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalMin"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalMax"),
        ("LMP-MIB", "lmpCcHelloDeadIntervalNegotiated"),
        ("LMP-MIB", "lmpCcOperStatus"),
        ("LMP-MIB", "lmpCcRowStatus"),
        ("LMP-MIB", "lmpCcStorageType"),
        ("LMP-MIB", "lmpCcUpDownNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    lmpControlChannelGroup.setStatus("current")

lmpCcIsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 3)
)
lmpCcIsInterfaceGroup.setObjects(
    ("LMP-MIB", "lmpCcIsIf")
)
if mibBuilder.loadTexts:
    lmpCcIsInterfaceGroup.setStatus("current")

lmpCcIsNotInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 4)
)
lmpCcIsNotInterfaceGroup.setObjects(
      *(("LMP-MIB", "lmpCcUnderlyingIfIndex"),
        ("LMP-MIB", "lmpCcIsIf"),
        ("LMP-MIB", "lmpCcLastChange"),
        ("LMP-MIB", "lmpCcAdminStatus"))
)
if mibBuilder.loadTexts:
    lmpCcIsNotInterfaceGroup.setStatus("current")

lmpLinkPropertyCorrelationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 5)
)
lmpLinkPropertyCorrelationGroup.setObjects(
    ("LMP-MIB", "lmpLinkPropertyNotificationsEnabled")
)
if mibBuilder.loadTexts:
    lmpLinkPropertyCorrelationGroup.setStatus("current")

lmpLinkVerificationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 6)
)
lmpLinkVerificationGroup.setObjects(
      *(("LMP-MIB", "lmpGlobalLinkVerificationInterval"),
        ("LMP-MIB", "lmpLinkVerifyInterval"),
        ("LMP-MIB", "lmpLinkVerifyDeadInterval"),
        ("LMP-MIB", "lmpLinkVerifyTransportMechanism"),
        ("LMP-MIB", "lmpLinkVerifyAllLinks"),
        ("LMP-MIB", "lmpLinkVerifyTransmissionRate"),
        ("LMP-MIB", "lmpLinkVerifyWavelength"),
        ("LMP-MIB", "lmpLinkVerifyRowStatus"),
        ("LMP-MIB", "lmpLinkVerifyStorageType"),
        ("LMP-MIB", "lmpDataLinkNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    lmpLinkVerificationGroup.setStatus("current")

lmpPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 7)
)
lmpPerfGroup.setObjects(
      *(("LMP-MIB", "lmpCcInOctets"),
        ("LMP-MIB", "lmpCcInDiscards"),
        ("LMP-MIB", "lmpCcInErrors"),
        ("LMP-MIB", "lmpCcOutOctets"),
        ("LMP-MIB", "lmpCcOutDiscards"),
        ("LMP-MIB", "lmpCcOutErrors"),
        ("LMP-MIB", "lmpCcConfigReceived"),
        ("LMP-MIB", "lmpCcConfigSent"),
        ("LMP-MIB", "lmpCcConfigRetransmit"),
        ("LMP-MIB", "lmpCcConfigAckReceived"),
        ("LMP-MIB", "lmpCcConfigAckSent"),
        ("LMP-MIB", "lmpCcConfigNackSent"),
        ("LMP-MIB", "lmpCcConfigNackReceived"),
        ("LMP-MIB", "lmpCcHelloReceived"),
        ("LMP-MIB", "lmpCcHelloSent"),
        ("LMP-MIB", "lmpCcBeginVerifyReceived"),
        ("LMP-MIB", "lmpCcBeginVerifySent"),
        ("LMP-MIB", "lmpCcBeginVerifyRetransmit"),
        ("LMP-MIB", "lmpCcBeginVerifyAckReceived"),
        ("LMP-MIB", "lmpCcBeginVerifyAckSent"),
        ("LMP-MIB", "lmpCcBeginVerifyNackReceived"),
        ("LMP-MIB", "lmpCcBeginVerifyNackSent"),
        ("LMP-MIB", "lmpCcEndVerifyReceived"),
        ("LMP-MIB", "lmpCcEndVerifySent"),
        ("LMP-MIB", "lmpCcEndVerifyRetransmit"),
        ("LMP-MIB", "lmpCcEndVerifyAckReceived"),
        ("LMP-MIB", "lmpCcEndVerifyAckSent"),
        ("LMP-MIB", "lmpCcTestStatusSuccessReceived"),
        ("LMP-MIB", "lmpCcTestStatusSuccessSent"),
        ("LMP-MIB", "lmpCcTestStatusSuccessRetransmit"),
        ("LMP-MIB", "lmpCcTestStatusFailureReceived"),
        ("LMP-MIB", "lmpCcTestStatusFailureSent"),
        ("LMP-MIB", "lmpCcTestStatusFailureRetransmit"),
        ("LMP-MIB", "lmpCcTestStatusAckReceived"),
        ("LMP-MIB", "lmpCcTestStatusAckSent"),
        ("LMP-MIB", "lmpCcLinkSummaryReceived"),
        ("LMP-MIB", "lmpCcLinkSummarySent"),
        ("LMP-MIB", "lmpCcLinkSummaryRetransmit"),
        ("LMP-MIB", "lmpCcLinkSummaryAckReceived"),
        ("LMP-MIB", "lmpCcLinkSummaryAckSent"),
        ("LMP-MIB", "lmpCcLinkSummaryNackReceived"),
        ("LMP-MIB", "lmpCcLinkSummaryNackSent"),
        ("LMP-MIB", "lmpCcChannelStatusReceived"),
        ("LMP-MIB", "lmpCcChannelStatusSent"),
        ("LMP-MIB", "lmpCcChannelStatusRetransmit"),
        ("LMP-MIB", "lmpCcChannelStatusAckReceived"),
        ("LMP-MIB", "lmpCcChannelStatusAckSent"),
        ("LMP-MIB", "lmpCcChannelStatusReqReceived"),
        ("LMP-MIB", "lmpCcChannelStatusReqSent"),
        ("LMP-MIB", "lmpCcChannelStatusReqRetransmit"),
        ("LMP-MIB", "lmpCcChannelStatusRspReceived"),
        ("LMP-MIB", "lmpCcChannelStatusRspSent"),
        ("LMP-MIB", "lmpCcCounterDiscontinuityTime"),
        ("LMP-MIB", "lmpTeInOctets"),
        ("LMP-MIB", "lmpTeOutOctets"),
        ("LMP-MIB", "lmpTeBeginVerifyReceived"),
        ("LMP-MIB", "lmpTeBeginVerifySent"),
        ("LMP-MIB", "lmpTeBeginVerifyRetransmit"),
        ("LMP-MIB", "lmpTeBeginVerifyAckReceived"),
        ("LMP-MIB", "lmpTeBeginVerifyAckSent"),
        ("LMP-MIB", "lmpTeBeginVerifyNackReceived"),
        ("LMP-MIB", "lmpTeBeginVerifyNackSent"),
        ("LMP-MIB", "lmpTeEndVerifyReceived"),
        ("LMP-MIB", "lmpTeEndVerifySent"),
        ("LMP-MIB", "lmpTeEndVerifyRetransmit"),
        ("LMP-MIB", "lmpTeEndVerifyAckReceived"),
        ("LMP-MIB", "lmpTeEndVerifyAckSent"),
        ("LMP-MIB", "lmpTeTestStatusSuccessReceived"),
        ("LMP-MIB", "lmpTeTestStatusSuccessSent"),
        ("LMP-MIB", "lmpTeTestStatusSuccessRetransmit"),
        ("LMP-MIB", "lmpTeTestStatusFailureReceived"),
        ("LMP-MIB", "lmpTeTestStatusFailureSent"),
        ("LMP-MIB", "lmpTeTestStatusFailureRetransmit"),
        ("LMP-MIB", "lmpTeTestStatusAckReceived"),
        ("LMP-MIB", "lmpTeTestStatusAckSent"),
        ("LMP-MIB", "lmpTeLinkSummaryReceived"),
        ("LMP-MIB", "lmpTeLinkSummarySent"),
        ("LMP-MIB", "lmpTeLinkSummaryRetransmit"),
        ("LMP-MIB", "lmpTeLinkSummaryAckReceived"),
        ("LMP-MIB", "lmpTeLinkSummaryAckSent"),
        ("LMP-MIB", "lmpTeLinkSummaryNackReceived"),
        ("LMP-MIB", "lmpTeLinkSummaryNackSent"),
        ("LMP-MIB", "lmpTeChannelStatusReceived"),
        ("LMP-MIB", "lmpTeChannelStatusSent"),
        ("LMP-MIB", "lmpTeChannelStatusRetransmit"),
        ("LMP-MIB", "lmpTeChannelStatusAckReceived"),
        ("LMP-MIB", "lmpTeChannelStatusAckSent"),
        ("LMP-MIB", "lmpTeChannelStatusReqReceived"),
        ("LMP-MIB", "lmpTeChannelStatusReqSent"),
        ("LMP-MIB", "lmpTeChannelStatusReqRetransmit"),
        ("LMP-MIB", "lmpTeChannelStatusRspSent"),
        ("LMP-MIB", "lmpTeChannelStatusRspReceived"),
        ("LMP-MIB", "lmpTeCounterDiscontinuityTime"),
        ("LMP-MIB", "lmpDataLinkTestReceived"),
        ("LMP-MIB", "lmpDataLinkTestSent"),
        ("LMP-MIB", "lmpDataLinkActiveTestSuccess"),
        ("LMP-MIB", "lmpDataLinkActiveTestFailure"),
        ("LMP-MIB", "lmpDataLinkPassiveTestSuccess"),
        ("LMP-MIB", "lmpDataLinkPassiveTestFailure"),
        ("LMP-MIB", "lmpDataLinkDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    lmpPerfGroup.setStatus("current")

lmpTeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 8)
)
lmpTeLinkGroup.setObjects(
      *(("LMP-MIB", "lmpTeLinkNbrRemoteNodeId"),
        ("LMP-MIB", "lmpTeLinkVerification"),
        ("LMP-MIB", "lmpTeLinkFaultManagement"),
        ("LMP-MIB", "lmpTeLinkDwdm"),
        ("LMP-MIB", "lmpTeLinkOperStatus"),
        ("LMP-MIB", "lmpTeLinkRowStatus"),
        ("LMP-MIB", "lmpTeLinkStorageType"),
        ("LMP-MIB", "lmpTeLinkNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    lmpTeLinkGroup.setStatus("current")

lmpDataLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 9)
)
lmpDataLinkGroup.setObjects(
      *(("LMP-MIB", "lmpDataLinkType"),
        ("LMP-MIB", "lmpDataLinkAddressType"),
        ("LMP-MIB", "lmpDataLinkIpAddr"),
        ("LMP-MIB", "lmpDataLinkRemoteIpAddress"),
        ("LMP-MIB", "lmpDataLinkRemoteIfId"),
        ("LMP-MIB", "lmpDataLinkEncodingType"),
        ("LMP-MIB", "lmpDataLinkActiveOperStatus"),
        ("LMP-MIB", "lmpDataLinkPassiveOperStatus"),
        ("LMP-MIB", "lmpDataLinkRowStatus"),
        ("LMP-MIB", "lmpDataLinkStorageType"))
)
if mibBuilder.loadTexts:
    lmpDataLinkGroup.setStatus("current")


# Notification objects

lmpTeLinkPropertyMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 1)
)
lmpTeLinkPropertyMismatch.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkRemoteIpAddr"),
        ("TE-LINK-STD-MIB", "teLinkIncomingIfId"))
)
if mibBuilder.loadTexts:
    lmpTeLinkPropertyMismatch.setStatus(
        "current"
    )

lmpDataLinkPropertyMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 2)
)
lmpDataLinkPropertyMismatch.setObjects(
      *(("LMP-MIB", "lmpDataLinkType"),
        ("LMP-MIB", "lmpDataLinkRemoteIfId"))
)
if mibBuilder.loadTexts:
    lmpDataLinkPropertyMismatch.setStatus(
        "current"
    )

lmpUnprotected = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 3)
)
lmpUnprotected.setObjects(
    ("LMP-MIB", "lmpCcNbrNodeId")
)
if mibBuilder.loadTexts:
    lmpUnprotected.setStatus(
        "current"
    )

lmpControlChannelUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 4)
)
lmpControlChannelUp.setObjects(
      *(("LMP-MIB", "lmpCcAdminStatus"),
        ("LMP-MIB", "lmpCcOperStatus"))
)
if mibBuilder.loadTexts:
    lmpControlChannelUp.setStatus(
        "current"
    )

lmpControlChannelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 5)
)
lmpControlChannelDown.setObjects(
      *(("LMP-MIB", "lmpCcAdminStatus"),
        ("LMP-MIB", "lmpCcOperStatus"))
)
if mibBuilder.loadTexts:
    lmpControlChannelDown.setStatus(
        "current"
    )

lmpTeLinkDegraded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 6)
)
lmpTeLinkDegraded.setObjects(
    ("LMP-MIB", "lmpTeLinkOperStatus")
)
if mibBuilder.loadTexts:
    lmpTeLinkDegraded.setStatus(
        "current"
    )

lmpTeLinkNotDegraded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 7)
)
lmpTeLinkNotDegraded.setObjects(
    ("LMP-MIB", "lmpTeLinkOperStatus")
)
if mibBuilder.loadTexts:
    lmpTeLinkNotDegraded.setStatus(
        "current"
    )

lmpDataLinkVerificationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 227, 0, 8)
)
lmpDataLinkVerificationFailure.setObjects(
      *(("LMP-MIB", "lmpDataLinkActiveOperStatus"),
        ("LMP-MIB", "lmpDataLinkPassiveOperStatus"))
)
if mibBuilder.loadTexts:
    lmpDataLinkVerificationFailure.setStatus(
        "current"
    )


# Notifications groups

lmpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 2, 10)
)
lmpNotificationGroup.setObjects(
      *(("LMP-MIB", "lmpTeLinkPropertyMismatch"),
        ("LMP-MIB", "lmpDataLinkPropertyMismatch"),
        ("LMP-MIB", "lmpUnprotected"),
        ("LMP-MIB", "lmpControlChannelUp"),
        ("LMP-MIB", "lmpControlChannelDown"),
        ("LMP-MIB", "lmpTeLinkDegraded"),
        ("LMP-MIB", "lmpTeLinkNotDegraded"),
        ("LMP-MIB", "lmpDataLinkVerificationFailure"))
)
if mibBuilder.loadTexts:
    lmpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lmpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lmpModuleFullCompliance.setStatus(
        "current"
    )

lmpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 227, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lmpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LMP-MIB",
    **{"LmpInterval": LmpInterval,
       "LmpRetransmitInterval": LmpRetransmitInterval,
       "LmpNodeId": LmpNodeId,
       "lmpMIB": lmpMIB,
       "lmpNotifications": lmpNotifications,
       "lmpTeLinkPropertyMismatch": lmpTeLinkPropertyMismatch,
       "lmpDataLinkPropertyMismatch": lmpDataLinkPropertyMismatch,
       "lmpUnprotected": lmpUnprotected,
       "lmpControlChannelUp": lmpControlChannelUp,
       "lmpControlChannelDown": lmpControlChannelDown,
       "lmpTeLinkDegraded": lmpTeLinkDegraded,
       "lmpTeLinkNotDegraded": lmpTeLinkNotDegraded,
       "lmpDataLinkVerificationFailure": lmpDataLinkVerificationFailure,
       "lmpObjects": lmpObjects,
       "lmpAdminStatus": lmpAdminStatus,
       "lmpOperStatus": lmpOperStatus,
       "lmpNbrTable": lmpNbrTable,
       "lmpNbrEntry": lmpNbrEntry,
       "lmpNbrNodeId": lmpNbrNodeId,
       "lmpNbrRetransmitInterval": lmpNbrRetransmitInterval,
       "lmpNbrRetryLimit": lmpNbrRetryLimit,
       "lmpNbrRetransmitDelta": lmpNbrRetransmitDelta,
       "lmpNbrAdminStatus": lmpNbrAdminStatus,
       "lmpNbrOperStatus": lmpNbrOperStatus,
       "lmpNbrRowStatus": lmpNbrRowStatus,
       "lmpNbrStorageType": lmpNbrStorageType,
       "lmpCcHelloIntervalDefault": lmpCcHelloIntervalDefault,
       "lmpCcHelloIntervalDefaultMin": lmpCcHelloIntervalDefaultMin,
       "lmpCcHelloIntervalDefaultMax": lmpCcHelloIntervalDefaultMax,
       "lmpCcHelloDeadIntervalDefault": lmpCcHelloDeadIntervalDefault,
       "lmpCcHelloDeadIntervalDefaultMin": lmpCcHelloDeadIntervalDefaultMin,
       "lmpCcHelloDeadIntervalDefaultMax": lmpCcHelloDeadIntervalDefaultMax,
       "lmpControlChannelTable": lmpControlChannelTable,
       "lmpControlChannelEntry": lmpControlChannelEntry,
       "lmpCcId": lmpCcId,
       "lmpCcUnderlyingIfIndex": lmpCcUnderlyingIfIndex,
       "lmpCcIsIf": lmpCcIsIf,
       "lmpCcNbrNodeId": lmpCcNbrNodeId,
       "lmpCcRemoteId": lmpCcRemoteId,
       "lmpCcRemoteAddressType": lmpCcRemoteAddressType,
       "lmpCcRemoteIpAddr": lmpCcRemoteIpAddr,
       "lmpCcSetupRole": lmpCcSetupRole,
       "lmpCcAuthentication": lmpCcAuthentication,
       "lmpCcHelloInterval": lmpCcHelloInterval,
       "lmpCcHelloIntervalMin": lmpCcHelloIntervalMin,
       "lmpCcHelloIntervalMax": lmpCcHelloIntervalMax,
       "lmpCcHelloIntervalNegotiated": lmpCcHelloIntervalNegotiated,
       "lmpCcHelloDeadInterval": lmpCcHelloDeadInterval,
       "lmpCcHelloDeadIntervalMin": lmpCcHelloDeadIntervalMin,
       "lmpCcHelloDeadIntervalMax": lmpCcHelloDeadIntervalMax,
       "lmpCcHelloDeadIntervalNegotiated": lmpCcHelloDeadIntervalNegotiated,
       "lmpCcLastChange": lmpCcLastChange,
       "lmpCcAdminStatus": lmpCcAdminStatus,
       "lmpCcOperStatus": lmpCcOperStatus,
       "lmpCcRowStatus": lmpCcRowStatus,
       "lmpCcStorageType": lmpCcStorageType,
       "lmpControlChannelPerfTable": lmpControlChannelPerfTable,
       "lmpControlChannelPerfEntry": lmpControlChannelPerfEntry,
       "lmpCcInOctets": lmpCcInOctets,
       "lmpCcInDiscards": lmpCcInDiscards,
       "lmpCcInErrors": lmpCcInErrors,
       "lmpCcOutOctets": lmpCcOutOctets,
       "lmpCcOutDiscards": lmpCcOutDiscards,
       "lmpCcOutErrors": lmpCcOutErrors,
       "lmpCcConfigReceived": lmpCcConfigReceived,
       "lmpCcConfigSent": lmpCcConfigSent,
       "lmpCcConfigRetransmit": lmpCcConfigRetransmit,
       "lmpCcConfigAckReceived": lmpCcConfigAckReceived,
       "lmpCcConfigAckSent": lmpCcConfigAckSent,
       "lmpCcConfigNackReceived": lmpCcConfigNackReceived,
       "lmpCcConfigNackSent": lmpCcConfigNackSent,
       "lmpCcHelloReceived": lmpCcHelloReceived,
       "lmpCcHelloSent": lmpCcHelloSent,
       "lmpCcBeginVerifyReceived": lmpCcBeginVerifyReceived,
       "lmpCcBeginVerifySent": lmpCcBeginVerifySent,
       "lmpCcBeginVerifyRetransmit": lmpCcBeginVerifyRetransmit,
       "lmpCcBeginVerifyAckReceived": lmpCcBeginVerifyAckReceived,
       "lmpCcBeginVerifyAckSent": lmpCcBeginVerifyAckSent,
       "lmpCcBeginVerifyNackReceived": lmpCcBeginVerifyNackReceived,
       "lmpCcBeginVerifyNackSent": lmpCcBeginVerifyNackSent,
       "lmpCcEndVerifyReceived": lmpCcEndVerifyReceived,
       "lmpCcEndVerifySent": lmpCcEndVerifySent,
       "lmpCcEndVerifyRetransmit": lmpCcEndVerifyRetransmit,
       "lmpCcEndVerifyAckReceived": lmpCcEndVerifyAckReceived,
       "lmpCcEndVerifyAckSent": lmpCcEndVerifyAckSent,
       "lmpCcTestStatusSuccessReceived": lmpCcTestStatusSuccessReceived,
       "lmpCcTestStatusSuccessSent": lmpCcTestStatusSuccessSent,
       "lmpCcTestStatusSuccessRetransmit": lmpCcTestStatusSuccessRetransmit,
       "lmpCcTestStatusFailureReceived": lmpCcTestStatusFailureReceived,
       "lmpCcTestStatusFailureSent": lmpCcTestStatusFailureSent,
       "lmpCcTestStatusFailureRetransmit": lmpCcTestStatusFailureRetransmit,
       "lmpCcTestStatusAckReceived": lmpCcTestStatusAckReceived,
       "lmpCcTestStatusAckSent": lmpCcTestStatusAckSent,
       "lmpCcLinkSummaryReceived": lmpCcLinkSummaryReceived,
       "lmpCcLinkSummarySent": lmpCcLinkSummarySent,
       "lmpCcLinkSummaryRetransmit": lmpCcLinkSummaryRetransmit,
       "lmpCcLinkSummaryAckReceived": lmpCcLinkSummaryAckReceived,
       "lmpCcLinkSummaryAckSent": lmpCcLinkSummaryAckSent,
       "lmpCcLinkSummaryNackReceived": lmpCcLinkSummaryNackReceived,
       "lmpCcLinkSummaryNackSent": lmpCcLinkSummaryNackSent,
       "lmpCcChannelStatusReceived": lmpCcChannelStatusReceived,
       "lmpCcChannelStatusSent": lmpCcChannelStatusSent,
       "lmpCcChannelStatusRetransmit": lmpCcChannelStatusRetransmit,
       "lmpCcChannelStatusAckReceived": lmpCcChannelStatusAckReceived,
       "lmpCcChannelStatusAckSent": lmpCcChannelStatusAckSent,
       "lmpCcChannelStatusReqReceived": lmpCcChannelStatusReqReceived,
       "lmpCcChannelStatusReqSent": lmpCcChannelStatusReqSent,
       "lmpCcChannelStatusReqRetransmit": lmpCcChannelStatusReqRetransmit,
       "lmpCcChannelStatusRspReceived": lmpCcChannelStatusRspReceived,
       "lmpCcChannelStatusRspSent": lmpCcChannelStatusRspSent,
       "lmpCcCounterDiscontinuityTime": lmpCcCounterDiscontinuityTime,
       "lmpTeLinkTable": lmpTeLinkTable,
       "lmpTeLinkEntry": lmpTeLinkEntry,
       "lmpTeLinkNbrRemoteNodeId": lmpTeLinkNbrRemoteNodeId,
       "lmpTeLinkVerification": lmpTeLinkVerification,
       "lmpTeLinkFaultManagement": lmpTeLinkFaultManagement,
       "lmpTeLinkDwdm": lmpTeLinkDwdm,
       "lmpTeLinkOperStatus": lmpTeLinkOperStatus,
       "lmpTeLinkRowStatus": lmpTeLinkRowStatus,
       "lmpTeLinkStorageType": lmpTeLinkStorageType,
       "lmpGlobalLinkVerificationInterval": lmpGlobalLinkVerificationInterval,
       "lmpLinkVerificationTable": lmpLinkVerificationTable,
       "lmpLinkVerificationEntry": lmpLinkVerificationEntry,
       "lmpLinkVerifyInterval": lmpLinkVerifyInterval,
       "lmpLinkVerifyDeadInterval": lmpLinkVerifyDeadInterval,
       "lmpLinkVerifyTransportMechanism": lmpLinkVerifyTransportMechanism,
       "lmpLinkVerifyAllLinks": lmpLinkVerifyAllLinks,
       "lmpLinkVerifyTransmissionRate": lmpLinkVerifyTransmissionRate,
       "lmpLinkVerifyWavelength": lmpLinkVerifyWavelength,
       "lmpLinkVerifyRowStatus": lmpLinkVerifyRowStatus,
       "lmpLinkVerifyStorageType": lmpLinkVerifyStorageType,
       "lmpTeLinkPerfTable": lmpTeLinkPerfTable,
       "lmpTeLinkPerfEntry": lmpTeLinkPerfEntry,
       "lmpTeInOctets": lmpTeInOctets,
       "lmpTeOutOctets": lmpTeOutOctets,
       "lmpTeBeginVerifyReceived": lmpTeBeginVerifyReceived,
       "lmpTeBeginVerifySent": lmpTeBeginVerifySent,
       "lmpTeBeginVerifyRetransmit": lmpTeBeginVerifyRetransmit,
       "lmpTeBeginVerifyAckReceived": lmpTeBeginVerifyAckReceived,
       "lmpTeBeginVerifyAckSent": lmpTeBeginVerifyAckSent,
       "lmpTeBeginVerifyNackReceived": lmpTeBeginVerifyNackReceived,
       "lmpTeBeginVerifyNackSent": lmpTeBeginVerifyNackSent,
       "lmpTeEndVerifyReceived": lmpTeEndVerifyReceived,
       "lmpTeEndVerifySent": lmpTeEndVerifySent,
       "lmpTeEndVerifyRetransmit": lmpTeEndVerifyRetransmit,
       "lmpTeEndVerifyAckReceived": lmpTeEndVerifyAckReceived,
       "lmpTeEndVerifyAckSent": lmpTeEndVerifyAckSent,
       "lmpTeTestStatusSuccessReceived": lmpTeTestStatusSuccessReceived,
       "lmpTeTestStatusSuccessSent": lmpTeTestStatusSuccessSent,
       "lmpTeTestStatusSuccessRetransmit": lmpTeTestStatusSuccessRetransmit,
       "lmpTeTestStatusFailureReceived": lmpTeTestStatusFailureReceived,
       "lmpTeTestStatusFailureSent": lmpTeTestStatusFailureSent,
       "lmpTeTestStatusFailureRetransmit": lmpTeTestStatusFailureRetransmit,
       "lmpTeTestStatusAckReceived": lmpTeTestStatusAckReceived,
       "lmpTeTestStatusAckSent": lmpTeTestStatusAckSent,
       "lmpTeLinkSummaryReceived": lmpTeLinkSummaryReceived,
       "lmpTeLinkSummarySent": lmpTeLinkSummarySent,
       "lmpTeLinkSummaryRetransmit": lmpTeLinkSummaryRetransmit,
       "lmpTeLinkSummaryAckReceived": lmpTeLinkSummaryAckReceived,
       "lmpTeLinkSummaryAckSent": lmpTeLinkSummaryAckSent,
       "lmpTeLinkSummaryNackReceived": lmpTeLinkSummaryNackReceived,
       "lmpTeLinkSummaryNackSent": lmpTeLinkSummaryNackSent,
       "lmpTeChannelStatusReceived": lmpTeChannelStatusReceived,
       "lmpTeChannelStatusSent": lmpTeChannelStatusSent,
       "lmpTeChannelStatusRetransmit": lmpTeChannelStatusRetransmit,
       "lmpTeChannelStatusAckReceived": lmpTeChannelStatusAckReceived,
       "lmpTeChannelStatusAckSent": lmpTeChannelStatusAckSent,
       "lmpTeChannelStatusReqReceived": lmpTeChannelStatusReqReceived,
       "lmpTeChannelStatusReqSent": lmpTeChannelStatusReqSent,
       "lmpTeChannelStatusReqRetransmit": lmpTeChannelStatusReqRetransmit,
       "lmpTeChannelStatusRspReceived": lmpTeChannelStatusRspReceived,
       "lmpTeChannelStatusRspSent": lmpTeChannelStatusRspSent,
       "lmpTeCounterDiscontinuityTime": lmpTeCounterDiscontinuityTime,
       "lmpDataLinkTable": lmpDataLinkTable,
       "lmpDataLinkEntry": lmpDataLinkEntry,
       "lmpDataLinkType": lmpDataLinkType,
       "lmpDataLinkAddressType": lmpDataLinkAddressType,
       "lmpDataLinkIpAddr": lmpDataLinkIpAddr,
       "lmpDataLinkRemoteIpAddress": lmpDataLinkRemoteIpAddress,
       "lmpDataLinkRemoteIfId": lmpDataLinkRemoteIfId,
       "lmpDataLinkEncodingType": lmpDataLinkEncodingType,
       "lmpDataLinkActiveOperStatus": lmpDataLinkActiveOperStatus,
       "lmpDataLinkPassiveOperStatus": lmpDataLinkPassiveOperStatus,
       "lmpDataLinkRowStatus": lmpDataLinkRowStatus,
       "lmpDataLinkStorageType": lmpDataLinkStorageType,
       "lmpDataLinkPerfTable": lmpDataLinkPerfTable,
       "lmpDataLinkPerfEntry": lmpDataLinkPerfEntry,
       "lmpDataLinkTestReceived": lmpDataLinkTestReceived,
       "lmpDataLinkTestSent": lmpDataLinkTestSent,
       "lmpDataLinkActiveTestSuccess": lmpDataLinkActiveTestSuccess,
       "lmpDataLinkActiveTestFailure": lmpDataLinkActiveTestFailure,
       "lmpDataLinkPassiveTestSuccess": lmpDataLinkPassiveTestSuccess,
       "lmpDataLinkPassiveTestFailure": lmpDataLinkPassiveTestFailure,
       "lmpDataLinkDiscontinuityTime": lmpDataLinkDiscontinuityTime,
       "lmpNotificationMaxRate": lmpNotificationMaxRate,
       "lmpLinkPropertyNotificationsEnabled": lmpLinkPropertyNotificationsEnabled,
       "lmpUnprotectedNotificationsEnabled": lmpUnprotectedNotificationsEnabled,
       "lmpCcUpDownNotificationsEnabled": lmpCcUpDownNotificationsEnabled,
       "lmpTeLinkNotificationsEnabled": lmpTeLinkNotificationsEnabled,
       "lmpDataLinkNotificationsEnabled": lmpDataLinkNotificationsEnabled,
       "lmpConformance": lmpConformance,
       "lmpCompliances": lmpCompliances,
       "lmpModuleFullCompliance": lmpModuleFullCompliance,
       "lmpModuleReadOnlyCompliance": lmpModuleReadOnlyCompliance,
       "lmpGroups": lmpGroups,
       "lmpNodeGroup": lmpNodeGroup,
       "lmpControlChannelGroup": lmpControlChannelGroup,
       "lmpCcIsInterfaceGroup": lmpCcIsInterfaceGroup,
       "lmpCcIsNotInterfaceGroup": lmpCcIsNotInterfaceGroup,
       "lmpLinkPropertyCorrelationGroup": lmpLinkPropertyCorrelationGroup,
       "lmpLinkVerificationGroup": lmpLinkVerificationGroup,
       "lmpPerfGroup": lmpPerfGroup,
       "lmpTeLinkGroup": lmpTeLinkGroup,
       "lmpDataLinkGroup": lmpDataLinkGroup,
       "lmpNotificationGroup": lmpNotificationGroup}
)
