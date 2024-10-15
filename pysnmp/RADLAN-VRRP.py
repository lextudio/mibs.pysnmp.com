# SNMP MIB module (RADLAN-VRRP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-VRRP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:58 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipSpec,) = mibBuilder.importSymbols(
    "RADLAN-IP",
    "ipSpec")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")

(vrrpv3AssociatedIpAddrEntry,
 vrrpv3OperationsEntry) = mibBuilder.importSymbols(
    "VRRPV3-MIB",
    "vrrpv3AssociatedIpAddrEntry",
    "vrrpv3OperationsEntry")


# MODULE-IDENTITY

rlVrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 26)
)
rlVrrp.setRevisions(
        ("2010-12-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlVrrpv3OperationsTable_Object = MibTable
rlVrrpv3OperationsTable = _RlVrrpv3OperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1)
)
if mibBuilder.loadTexts:
    rlVrrpv3OperationsTable.setStatus("current")
_RlVrrpv3OperationsEntry_Object = MibTableRow
rlVrrpv3OperationsEntry = _RlVrrpv3OperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1)
)
if mibBuilder.loadTexts:
    rlVrrpv3OperationsEntry.setStatus("current")
_RlVrrpv3OperationsDefaultPrimaryIpAddr_Type = InetAddress
_RlVrrpv3OperationsDefaultPrimaryIpAddr_Object = MibTableColumn
rlVrrpv3OperationsDefaultPrimaryIpAddr = _RlVrrpv3OperationsDefaultPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 1),
    _RlVrrpv3OperationsDefaultPrimaryIpAddr_Type()
)
rlVrrpv3OperationsDefaultPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsDefaultPrimaryIpAddr.setStatus("current")


class _RlVrrpv3OperationsPrimaryIpAddrState_Type(Integer32):
    """Custom type rlVrrpv3OperationsPrimaryIpAddrState based on Integer32"""
    defaultValue = 2

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


_RlVrrpv3OperationsPrimaryIpAddrState_Type.__name__ = "Integer32"
_RlVrrpv3OperationsPrimaryIpAddrState_Object = MibTableColumn
rlVrrpv3OperationsPrimaryIpAddrState = _RlVrrpv3OperationsPrimaryIpAddrState_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 2),
    _RlVrrpv3OperationsPrimaryIpAddrState_Type()
)
rlVrrpv3OperationsPrimaryIpAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsPrimaryIpAddrState.setStatus("current")
_RlVrrpv3OperationsVrDescription_Type = DisplayString
_RlVrrpv3OperationsVrDescription_Object = MibTableColumn
rlVrrpv3OperationsVrDescription = _RlVrrpv3OperationsVrDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 3),
    _RlVrrpv3OperationsVrDescription_Type()
)
rlVrrpv3OperationsVrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsVrDescription.setStatus("current")


class _RlVrrpv3OperationsAdminState_Type(Integer32):
    """Custom type rlVrrpv3OperationsAdminState based on Integer32"""
    defaultValue = 2

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


_RlVrrpv3OperationsAdminState_Type.__name__ = "Integer32"
_RlVrrpv3OperationsAdminState_Object = MibTableColumn
rlVrrpv3OperationsAdminState = _RlVrrpv3OperationsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 4),
    _RlVrrpv3OperationsAdminState_Type()
)
rlVrrpv3OperationsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsAdminState.setStatus("current")


class _RlVrrpv3OperationsVrrpVersion_Type(Integer32):
    """Custom type rlVrrpv3OperationsVrrpVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version2", 2),
          ("version2and3", 1),
          ("version3", 3))
    )


_RlVrrpv3OperationsVrrpVersion_Type.__name__ = "Integer32"
_RlVrrpv3OperationsVrrpVersion_Object = MibTableColumn
rlVrrpv3OperationsVrrpVersion = _RlVrrpv3OperationsVrrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 5),
    _RlVrrpv3OperationsVrrpVersion_Type()
)
rlVrrpv3OperationsVrrpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsVrrpVersion.setStatus("current")


class _RlVrrpv3OperationsMasterPriority_Type(Unsigned32):
    """Custom type rlVrrpv3OperationsMasterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlVrrpv3OperationsMasterPriority_Type.__name__ = "Unsigned32"
_RlVrrpv3OperationsMasterPriority_Object = MibTableColumn
rlVrrpv3OperationsMasterPriority = _RlVrrpv3OperationsMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 6),
    _RlVrrpv3OperationsMasterPriority_Type()
)
rlVrrpv3OperationsMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsMasterPriority.setStatus("current")


class _RlVrrpv3OperationsMasterAdvInterval_Type(TimeInterval):
    """Custom type rlVrrpv3OperationsMasterAdvInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RlVrrpv3OperationsMasterAdvInterval_Type.__name__ = "TimeInterval"
_RlVrrpv3OperationsMasterAdvInterval_Object = MibTableColumn
rlVrrpv3OperationsMasterAdvInterval = _RlVrrpv3OperationsMasterAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 7),
    _RlVrrpv3OperationsMasterAdvInterval_Type()
)
rlVrrpv3OperationsMasterAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsMasterAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsMasterAdvInterval.setUnits("centiseconds")
_RlVrrpv3OperationsMasterDownInterval_Type = TimeInterval
_RlVrrpv3OperationsMasterDownInterval_Object = MibTableColumn
rlVrrpv3OperationsMasterDownInterval = _RlVrrpv3OperationsMasterDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 8),
    _RlVrrpv3OperationsMasterDownInterval_Type()
)
rlVrrpv3OperationsMasterDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsMasterDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsMasterDownInterval.setUnits("centiseconds")
_RlVrrpv3OperationsSkewTime_Type = TimeInterval
_RlVrrpv3OperationsSkewTime_Object = MibTableColumn
rlVrrpv3OperationsSkewTime = _RlVrrpv3OperationsSkewTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 9),
    _RlVrrpv3OperationsSkewTime_Type()
)
rlVrrpv3OperationsSkewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsSkewTime.setStatus("current")
if mibBuilder.loadTexts:
    rlVrrpv3OperationsSkewTime.setUnits("centiseconds")
_RlVrrpv3AssociatedIpAddrTable_Object = MibTable
rlVrrpv3AssociatedIpAddrTable = _RlVrrpv3AssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 2)
)
if mibBuilder.loadTexts:
    rlVrrpv3AssociatedIpAddrTable.setStatus("current")
_RlVrrpv3AssociatedIpAddrEntry_Object = MibTableRow
rlVrrpv3AssociatedIpAddrEntry = _RlVrrpv3AssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 2, 1)
)
if mibBuilder.loadTexts:
    rlVrrpv3AssociatedIpAddrEntry.setStatus("current")


class _RlVrrpv3AssociatedIpAddrState_Type(Integer32):
    """Custom type rlVrrpv3AssociatedIpAddrState based on Integer32"""
    defaultValue = 2

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


_RlVrrpv3AssociatedIpAddrState_Type.__name__ = "Integer32"
_RlVrrpv3AssociatedIpAddrState_Object = MibTableColumn
rlVrrpv3AssociatedIpAddrState = _RlVrrpv3AssociatedIpAddrState_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 2, 1, 1),
    _RlVrrpv3AssociatedIpAddrState_Type()
)
rlVrrpv3AssociatedIpAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3AssociatedIpAddrState.setStatus("current")
_RlVrrpv3CountersTable_Object = MibTable
rlVrrpv3CountersTable = _RlVrrpv3CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3)
)
if mibBuilder.loadTexts:
    rlVrrpv3CountersTable.setStatus("current")
_RlVrrpv3CountersEntry_Object = MibTableRow
rlVrrpv3CountersEntry = _RlVrrpv3CountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1)
)
rlVrrpv3CountersEntry.setIndexNames(
    (0, "RADLAN-VRRP", "rlVrrpv3CountersIfIndex"),
)
if mibBuilder.loadTexts:
    rlVrrpv3CountersEntry.setStatus("current")
_RlVrrpv3CountersIfIndex_Type = InterfaceIndexOrZero
_RlVrrpv3CountersIfIndex_Object = MibTableColumn
rlVrrpv3CountersIfIndex = _RlVrrpv3CountersIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 1),
    _RlVrrpv3CountersIfIndex_Type()
)
rlVrrpv3CountersIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlVrrpv3CountersIfIndex.setStatus("current")
_RlVrrpv3CountersChecksumErrors_Type = Counter32
_RlVrrpv3CountersChecksumErrors_Object = MibTableColumn
rlVrrpv3CountersChecksumErrors = _RlVrrpv3CountersChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 2),
    _RlVrrpv3CountersChecksumErrors_Type()
)
rlVrrpv3CountersChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersChecksumErrors.setStatus("current")
_RlVrrpv3CountersRcvdPacketsLength_Type = Counter32
_RlVrrpv3CountersRcvdPacketsLength_Object = MibTableColumn
rlVrrpv3CountersRcvdPacketsLength = _RlVrrpv3CountersRcvdPacketsLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 3),
    _RlVrrpv3CountersRcvdPacketsLength_Type()
)
rlVrrpv3CountersRcvdPacketsLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersRcvdPacketsLength.setStatus("current")
_RlVrrpv3CountersIpTtlErrors_Type = Counter32
_RlVrrpv3CountersIpTtlErrors_Object = MibTableColumn
rlVrrpv3CountersIpTtlErrors = _RlVrrpv3CountersIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 4),
    _RlVrrpv3CountersIpTtlErrors_Type()
)
rlVrrpv3CountersIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersIpTtlErrors.setStatus("current")
_RlVrrpv3CountersRcvdInvalidTypePackets_Type = Counter32
_RlVrrpv3CountersRcvdInvalidTypePackets_Object = MibTableColumn
rlVrrpv3CountersRcvdInvalidTypePackets = _RlVrrpv3CountersRcvdInvalidTypePackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 5),
    _RlVrrpv3CountersRcvdInvalidTypePackets_Type()
)
rlVrrpv3CountersRcvdInvalidTypePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersRcvdInvalidTypePackets.setStatus("current")
_RlVrrpv3CountersRcvdInvalidVrrpId_Type = Counter32
_RlVrrpv3CountersRcvdInvalidVrrpId_Object = MibTableColumn
rlVrrpv3CountersRcvdInvalidVrrpId = _RlVrrpv3CountersRcvdInvalidVrrpId_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 6),
    _RlVrrpv3CountersRcvdInvalidVrrpId_Type()
)
rlVrrpv3CountersRcvdInvalidVrrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersRcvdInvalidVrrpId.setStatus("current")
_RlVrrpv3CountersProtoErrors_Type = Counter32
_RlVrrpv3CountersProtoErrors_Object = MibTableColumn
rlVrrpv3CountersProtoErrors = _RlVrrpv3CountersProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 7),
    _RlVrrpv3CountersProtoErrors_Type()
)
rlVrrpv3CountersProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersProtoErrors.setStatus("current")
_RlVrrpv3CountersAddressListErrors_Type = Counter32
_RlVrrpv3CountersAddressListErrors_Object = MibTableColumn
rlVrrpv3CountersAddressListErrors = _RlVrrpv3CountersAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 8),
    _RlVrrpv3CountersAddressListErrors_Type()
)
rlVrrpv3CountersAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersAddressListErrors.setStatus("current")
_RlVrrpv3CountersAdvIntervalErrors_Type = Counter32
_RlVrrpv3CountersAdvIntervalErrors_Object = MibTableColumn
rlVrrpv3CountersAdvIntervalErrors = _RlVrrpv3CountersAdvIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 9),
    _RlVrrpv3CountersAdvIntervalErrors_Type()
)
rlVrrpv3CountersAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersAdvIntervalErrors.setStatus("current")
_RlVrrpv3CountersAuthErrors_Type = Counter32
_RlVrrpv3CountersAuthErrors_Object = MibTableColumn
rlVrrpv3CountersAuthErrors = _RlVrrpv3CountersAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 10),
    _RlVrrpv3CountersAuthErrors_Type()
)
rlVrrpv3CountersAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlVrrpv3CountersAuthErrors.setStatus("current")
_RlVrrpv3CountersRowStatus_Type = RowStatus
_RlVrrpv3CountersRowStatus_Object = MibTableColumn
rlVrrpv3CountersRowStatus = _RlVrrpv3CountersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 11),
    _RlVrrpv3CountersRowStatus_Type()
)
rlVrrpv3CountersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVrrpv3CountersRowStatus.setStatus("current")
vrrpv3OperationsEntry.registerAugmentions(
    ("RADLAN-VRRP",
     "rlVrrpv3OperationsEntry")
)
rlVrrpv3OperationsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
vrrpv3AssociatedIpAddrEntry.registerAugmentions(
    ("RADLAN-VRRP",
     "rlVrrpv3AssociatedIpAddrEntry")
)
rlVrrpv3AssociatedIpAddrEntry.setIndexNames(*vrrpv3AssociatedIpAddrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-VRRP",
    **{"rlVrrp": rlVrrp,
       "rlVrrpv3OperationsTable": rlVrrpv3OperationsTable,
       "rlVrrpv3OperationsEntry": rlVrrpv3OperationsEntry,
       "rlVrrpv3OperationsDefaultPrimaryIpAddr": rlVrrpv3OperationsDefaultPrimaryIpAddr,
       "rlVrrpv3OperationsPrimaryIpAddrState": rlVrrpv3OperationsPrimaryIpAddrState,
       "rlVrrpv3OperationsVrDescription": rlVrrpv3OperationsVrDescription,
       "rlVrrpv3OperationsAdminState": rlVrrpv3OperationsAdminState,
       "rlVrrpv3OperationsVrrpVersion": rlVrrpv3OperationsVrrpVersion,
       "rlVrrpv3OperationsMasterPriority": rlVrrpv3OperationsMasterPriority,
       "rlVrrpv3OperationsMasterAdvInterval": rlVrrpv3OperationsMasterAdvInterval,
       "rlVrrpv3OperationsMasterDownInterval": rlVrrpv3OperationsMasterDownInterval,
       "rlVrrpv3OperationsSkewTime": rlVrrpv3OperationsSkewTime,
       "rlVrrpv3AssociatedIpAddrTable": rlVrrpv3AssociatedIpAddrTable,
       "rlVrrpv3AssociatedIpAddrEntry": rlVrrpv3AssociatedIpAddrEntry,
       "rlVrrpv3AssociatedIpAddrState": rlVrrpv3AssociatedIpAddrState,
       "rlVrrpv3CountersTable": rlVrrpv3CountersTable,
       "rlVrrpv3CountersEntry": rlVrrpv3CountersEntry,
       "rlVrrpv3CountersIfIndex": rlVrrpv3CountersIfIndex,
       "rlVrrpv3CountersChecksumErrors": rlVrrpv3CountersChecksumErrors,
       "rlVrrpv3CountersRcvdPacketsLength": rlVrrpv3CountersRcvdPacketsLength,
       "rlVrrpv3CountersIpTtlErrors": rlVrrpv3CountersIpTtlErrors,
       "rlVrrpv3CountersRcvdInvalidTypePackets": rlVrrpv3CountersRcvdInvalidTypePackets,
       "rlVrrpv3CountersRcvdInvalidVrrpId": rlVrrpv3CountersRcvdInvalidVrrpId,
       "rlVrrpv3CountersProtoErrors": rlVrrpv3CountersProtoErrors,
       "rlVrrpv3CountersAddressListErrors": rlVrrpv3CountersAddressListErrors,
       "rlVrrpv3CountersAdvIntervalErrors": rlVrrpv3CountersAdvIntervalErrors,
       "rlVrrpv3CountersAuthErrors": rlVrrpv3CountersAuthErrors,
       "rlVrrpv3CountersRowStatus": rlVrrpv3CountersRowStatus}
)
