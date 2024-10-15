# SNMP MIB module (IPFIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:50 2024
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

(PhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ipfixMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 193)
)
ipfixMIB.setRevisions(
        ("2012-06-11 00:00",
         "2010-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpfixObjects_ObjectIdentity = ObjectIdentity
ipfixObjects = _IpfixObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 1)
)
_IpfixMainObjects_ObjectIdentity = ObjectIdentity
ipfixMainObjects = _IpfixMainObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 1, 1)
)
_IpfixTransportSessionTable_Object = MibTable
ipfixTransportSessionTable = _IpfixTransportSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixTransportSessionTable.setStatus("current")
_IpfixTransportSessionEntry_Object = MibTableRow
ipfixTransportSessionEntry = _IpfixTransportSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1)
)
ipfixTransportSessionEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixTransportSessionIndex"),
)
if mibBuilder.loadTexts:
    ipfixTransportSessionEntry.setStatus("current")


class _IpfixTransportSessionIndex_Type(Unsigned32):
    """Custom type ipfixTransportSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixTransportSessionIndex_Type.__name__ = "Unsigned32"
_IpfixTransportSessionIndex_Object = MibTableColumn
ipfixTransportSessionIndex = _IpfixTransportSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 1),
    _IpfixTransportSessionIndex_Type()
)
ipfixTransportSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTransportSessionIndex.setStatus("current")


class _IpfixTransportSessionProtocol_Type(Unsigned32):
    """Custom type ipfixTransportSessionProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpfixTransportSessionProtocol_Type.__name__ = "Unsigned32"
_IpfixTransportSessionProtocol_Object = MibTableColumn
ipfixTransportSessionProtocol = _IpfixTransportSessionProtocol_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 2),
    _IpfixTransportSessionProtocol_Type()
)
ipfixTransportSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionProtocol.setStatus("current")


class _IpfixTransportSessionSourceAddressType_Type(InetAddressType):
    """Custom type ipfixTransportSessionSourceAddressType based on InetAddressType"""
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


_IpfixTransportSessionSourceAddressType_Type.__name__ = "InetAddressType"
_IpfixTransportSessionSourceAddressType_Object = MibTableColumn
ipfixTransportSessionSourceAddressType = _IpfixTransportSessionSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 3),
    _IpfixTransportSessionSourceAddressType_Type()
)
ipfixTransportSessionSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionSourceAddressType.setStatus("current")
_IpfixTransportSessionSourceAddress_Type = InetAddress
_IpfixTransportSessionSourceAddress_Object = MibTableColumn
ipfixTransportSessionSourceAddress = _IpfixTransportSessionSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 4),
    _IpfixTransportSessionSourceAddress_Type()
)
ipfixTransportSessionSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionSourceAddress.setStatus("current")


class _IpfixTransportSessionDestinationAddressType_Type(InetAddressType):
    """Custom type ipfixTransportSessionDestinationAddressType based on InetAddressType"""
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


_IpfixTransportSessionDestinationAddressType_Type.__name__ = "InetAddressType"
_IpfixTransportSessionDestinationAddressType_Object = MibTableColumn
ipfixTransportSessionDestinationAddressType = _IpfixTransportSessionDestinationAddressType_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 5),
    _IpfixTransportSessionDestinationAddressType_Type()
)
ipfixTransportSessionDestinationAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDestinationAddressType.setStatus("current")
_IpfixTransportSessionDestinationAddress_Type = InetAddress
_IpfixTransportSessionDestinationAddress_Object = MibTableColumn
ipfixTransportSessionDestinationAddress = _IpfixTransportSessionDestinationAddress_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 6),
    _IpfixTransportSessionDestinationAddress_Type()
)
ipfixTransportSessionDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDestinationAddress.setStatus("current")
_IpfixTransportSessionSourcePort_Type = InetPortNumber
_IpfixTransportSessionSourcePort_Object = MibTableColumn
ipfixTransportSessionSourcePort = _IpfixTransportSessionSourcePort_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 7),
    _IpfixTransportSessionSourcePort_Type()
)
ipfixTransportSessionSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionSourcePort.setStatus("current")
_IpfixTransportSessionDestinationPort_Type = InetPortNumber
_IpfixTransportSessionDestinationPort_Object = MibTableColumn
ipfixTransportSessionDestinationPort = _IpfixTransportSessionDestinationPort_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 8),
    _IpfixTransportSessionDestinationPort_Type()
)
ipfixTransportSessionDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDestinationPort.setStatus("current")
_IpfixTransportSessionSctpAssocId_Type = Unsigned32
_IpfixTransportSessionSctpAssocId_Object = MibTableColumn
ipfixTransportSessionSctpAssocId = _IpfixTransportSessionSctpAssocId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 9),
    _IpfixTransportSessionSctpAssocId_Type()
)
ipfixTransportSessionSctpAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionSctpAssocId.setStatus("current")


class _IpfixTransportSessionDeviceMode_Type(Integer32):
    """Custom type ipfixTransportSessionDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("collecting", 2),
          ("exporting", 1))
    )


_IpfixTransportSessionDeviceMode_Type.__name__ = "Integer32"
_IpfixTransportSessionDeviceMode_Object = MibTableColumn
ipfixTransportSessionDeviceMode = _IpfixTransportSessionDeviceMode_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 10),
    _IpfixTransportSessionDeviceMode_Type()
)
ipfixTransportSessionDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDeviceMode.setStatus("current")
_IpfixTransportSessionTemplateRefreshTimeout_Type = Unsigned32
_IpfixTransportSessionTemplateRefreshTimeout_Object = MibTableColumn
ipfixTransportSessionTemplateRefreshTimeout = _IpfixTransportSessionTemplateRefreshTimeout_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 11),
    _IpfixTransportSessionTemplateRefreshTimeout_Type()
)
ipfixTransportSessionTemplateRefreshTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionTemplateRefreshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionTemplateRefreshTimeout.setUnits("seconds")
_IpfixTransportSessionOptionsTemplateRefreshTimeout_Type = Unsigned32
_IpfixTransportSessionOptionsTemplateRefreshTimeout_Object = MibTableColumn
ipfixTransportSessionOptionsTemplateRefreshTimeout = _IpfixTransportSessionOptionsTemplateRefreshTimeout_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 12),
    _IpfixTransportSessionOptionsTemplateRefreshTimeout_Type()
)
ipfixTransportSessionOptionsTemplateRefreshTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionOptionsTemplateRefreshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionOptionsTemplateRefreshTimeout.setUnits("seconds")
_IpfixTransportSessionTemplateRefreshPacket_Type = Unsigned32
_IpfixTransportSessionTemplateRefreshPacket_Object = MibTableColumn
ipfixTransportSessionTemplateRefreshPacket = _IpfixTransportSessionTemplateRefreshPacket_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 13),
    _IpfixTransportSessionTemplateRefreshPacket_Type()
)
ipfixTransportSessionTemplateRefreshPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionTemplateRefreshPacket.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionTemplateRefreshPacket.setUnits("packets")
_IpfixTransportSessionOptionsTemplateRefreshPacket_Type = Unsigned32
_IpfixTransportSessionOptionsTemplateRefreshPacket_Object = MibTableColumn
ipfixTransportSessionOptionsTemplateRefreshPacket = _IpfixTransportSessionOptionsTemplateRefreshPacket_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 14),
    _IpfixTransportSessionOptionsTemplateRefreshPacket_Type()
)
ipfixTransportSessionOptionsTemplateRefreshPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionOptionsTemplateRefreshPacket.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionOptionsTemplateRefreshPacket.setUnits("packets")


class _IpfixTransportSessionIpfixVersion_Type(Unsigned32):
    """Custom type ipfixTransportSessionIpfixVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpfixTransportSessionIpfixVersion_Type.__name__ = "Unsigned32"
_IpfixTransportSessionIpfixVersion_Object = MibTableColumn
ipfixTransportSessionIpfixVersion = _IpfixTransportSessionIpfixVersion_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 15),
    _IpfixTransportSessionIpfixVersion_Type()
)
ipfixTransportSessionIpfixVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionIpfixVersion.setStatus("current")


class _IpfixTransportSessionStatus_Type(Integer32):
    """Custom type ipfixTransportSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("unknown", 0))
    )


_IpfixTransportSessionStatus_Type.__name__ = "Integer32"
_IpfixTransportSessionStatus_Object = MibTableColumn
ipfixTransportSessionStatus = _IpfixTransportSessionStatus_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 1, 1, 16),
    _IpfixTransportSessionStatus_Type()
)
ipfixTransportSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionStatus.setStatus("current")
_IpfixTemplateTable_Object = MibTable
ipfixTemplateTable = _IpfixTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipfixTemplateTable.setStatus("current")
_IpfixTemplateEntry_Object = MibTableRow
ipfixTemplateEntry = _IpfixTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2, 1)
)
ipfixTemplateEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixTransportSessionIndex"),
    (0, "IPFIX-MIB", "ipfixTemplateObservationDomainId"),
    (0, "IPFIX-MIB", "ipfixTemplateId"),
)
if mibBuilder.loadTexts:
    ipfixTemplateEntry.setStatus("current")


class _IpfixTemplateObservationDomainId_Type(Unsigned32):
    """Custom type ipfixTemplateObservationDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpfixTemplateObservationDomainId_Type.__name__ = "Unsigned32"
_IpfixTemplateObservationDomainId_Object = MibTableColumn
ipfixTemplateObservationDomainId = _IpfixTemplateObservationDomainId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2, 1, 1),
    _IpfixTemplateObservationDomainId_Type()
)
ipfixTemplateObservationDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateObservationDomainId.setStatus("current")


class _IpfixTemplateId_Type(Unsigned32):
    """Custom type ipfixTemplateId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_IpfixTemplateId_Type.__name__ = "Unsigned32"
_IpfixTemplateId_Object = MibTableColumn
ipfixTemplateId = _IpfixTemplateId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2, 1, 2),
    _IpfixTemplateId_Type()
)
ipfixTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateId.setStatus("current")


class _IpfixTemplateSetId_Type(Unsigned32):
    """Custom type ipfixTemplateSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpfixTemplateSetId_Type.__name__ = "Unsigned32"
_IpfixTemplateSetId_Object = MibTableColumn
ipfixTemplateSetId = _IpfixTemplateSetId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2, 1, 3),
    _IpfixTemplateSetId_Type()
)
ipfixTemplateSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateSetId.setStatus("current")
_IpfixTemplateAccessTime_Type = DateAndTime
_IpfixTemplateAccessTime_Object = MibTableColumn
ipfixTemplateAccessTime = _IpfixTemplateAccessTime_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 2, 1, 4),
    _IpfixTemplateAccessTime_Type()
)
ipfixTemplateAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateAccessTime.setStatus("current")
_IpfixTemplateDefinitionTable_Object = MibTable
ipfixTemplateDefinitionTable = _IpfixTemplateDefinitionTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionTable.setStatus("current")
_IpfixTemplateDefinitionEntry_Object = MibTableRow
ipfixTemplateDefinitionEntry = _IpfixTemplateDefinitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1)
)
ipfixTemplateDefinitionEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixTransportSessionIndex"),
    (0, "IPFIX-MIB", "ipfixTemplateObservationDomainId"),
    (0, "IPFIX-MIB", "ipfixTemplateId"),
    (0, "IPFIX-MIB", "ipfixTemplateDefinitionIndex"),
)
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionEntry.setStatus("current")


class _IpfixTemplateDefinitionIndex_Type(Unsigned32):
    """Custom type ipfixTemplateDefinitionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpfixTemplateDefinitionIndex_Type.__name__ = "Unsigned32"
_IpfixTemplateDefinitionIndex_Object = MibTableColumn
ipfixTemplateDefinitionIndex = _IpfixTemplateDefinitionIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1, 1),
    _IpfixTemplateDefinitionIndex_Type()
)
ipfixTemplateDefinitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionIndex.setStatus("current")


class _IpfixTemplateDefinitionIeId_Type(Unsigned32):
    """Custom type ipfixTemplateDefinitionIeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpfixTemplateDefinitionIeId_Type.__name__ = "Unsigned32"
_IpfixTemplateDefinitionIeId_Object = MibTableColumn
ipfixTemplateDefinitionIeId = _IpfixTemplateDefinitionIeId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1, 2),
    _IpfixTemplateDefinitionIeId_Type()
)
ipfixTemplateDefinitionIeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionIeId.setStatus("current")


class _IpfixTemplateDefinitionIeLength_Type(Unsigned32):
    """Custom type ipfixTemplateDefinitionIeLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpfixTemplateDefinitionIeLength_Type.__name__ = "Unsigned32"
_IpfixTemplateDefinitionIeLength_Object = MibTableColumn
ipfixTemplateDefinitionIeLength = _IpfixTemplateDefinitionIeLength_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1, 3),
    _IpfixTemplateDefinitionIeLength_Type()
)
ipfixTemplateDefinitionIeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionIeLength.setStatus("current")
_IpfixTemplateDefinitionEnterpriseNumber_Type = Unsigned32
_IpfixTemplateDefinitionEnterpriseNumber_Object = MibTableColumn
ipfixTemplateDefinitionEnterpriseNumber = _IpfixTemplateDefinitionEnterpriseNumber_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1, 4),
    _IpfixTemplateDefinitionEnterpriseNumber_Type()
)
ipfixTemplateDefinitionEnterpriseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionEnterpriseNumber.setStatus("current")


class _IpfixTemplateDefinitionFlags_Type(Bits):
    """Custom type ipfixTemplateDefinitionFlags based on Bits"""
    namedValues = NamedValues(
        *(("flowKey", 1),
          ("scope", 0))
    )

_IpfixTemplateDefinitionFlags_Type.__name__ = "Bits"
_IpfixTemplateDefinitionFlags_Object = MibTableColumn
ipfixTemplateDefinitionFlags = _IpfixTemplateDefinitionFlags_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 3, 1, 5),
    _IpfixTemplateDefinitionFlags_Type()
)
ipfixTemplateDefinitionFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDefinitionFlags.setStatus("current")
_IpfixExportTable_Object = MibTable
ipfixExportTable = _IpfixExportTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipfixExportTable.setStatus("current")
_IpfixExportEntry_Object = MibTableRow
ipfixExportEntry = _IpfixExportEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 4, 1)
)
ipfixExportEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixExportIndex"),
    (0, "IPFIX-MIB", "ipfixMeteringProcessCacheId"),
    (0, "IPFIX-MIB", "ipfixTransportSessionIndex"),
)
if mibBuilder.loadTexts:
    ipfixExportEntry.setStatus("current")


class _IpfixExportIndex_Type(Unsigned32):
    """Custom type ipfixExportIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixExportIndex_Type.__name__ = "Unsigned32"
_IpfixExportIndex_Object = MibTableColumn
ipfixExportIndex = _IpfixExportIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 4, 1, 1),
    _IpfixExportIndex_Type()
)
ipfixExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixExportIndex.setStatus("current")


class _IpfixExportMemberType_Type(Integer32):
    """Custom type ipfixExportMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loadBalancing", 4),
          ("parallel", 3),
          ("primary", 1),
          ("secondary", 2),
          ("unknown", 0))
    )


_IpfixExportMemberType_Type.__name__ = "Integer32"
_IpfixExportMemberType_Object = MibTableColumn
ipfixExportMemberType = _IpfixExportMemberType_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 4, 1, 2),
    _IpfixExportMemberType_Type()
)
ipfixExportMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExportMemberType.setStatus("current")
_IpfixMeteringProcessTable_Object = MibTable
ipfixMeteringProcessTable = _IpfixMeteringProcessTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipfixMeteringProcessTable.setStatus("current")
_IpfixMeteringProcessEntry_Object = MibTableRow
ipfixMeteringProcessEntry = _IpfixMeteringProcessEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5, 1)
)
ipfixMeteringProcessEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixMeteringProcessCacheId"),
)
if mibBuilder.loadTexts:
    ipfixMeteringProcessEntry.setStatus("current")


class _IpfixMeteringProcessCacheId_Type(Unsigned32):
    """Custom type ipfixMeteringProcessCacheId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixMeteringProcessCacheId_Type.__name__ = "Unsigned32"
_IpfixMeteringProcessCacheId_Object = MibTableColumn
ipfixMeteringProcessCacheId = _IpfixMeteringProcessCacheId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5, 1, 1),
    _IpfixMeteringProcessCacheId_Type()
)
ipfixMeteringProcessCacheId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheId.setStatus("current")
_IpfixMeteringProcessObservationPointGroupRef_Type = Unsigned32
_IpfixMeteringProcessObservationPointGroupRef_Object = MibTableColumn
ipfixMeteringProcessObservationPointGroupRef = _IpfixMeteringProcessObservationPointGroupRef_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5, 1, 2),
    _IpfixMeteringProcessObservationPointGroupRef_Type()
)
ipfixMeteringProcessObservationPointGroupRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessObservationPointGroupRef.setStatus("current")
_IpfixMeteringProcessCacheActiveTimeout_Type = Unsigned32
_IpfixMeteringProcessCacheActiveTimeout_Object = MibTableColumn
ipfixMeteringProcessCacheActiveTimeout = _IpfixMeteringProcessCacheActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5, 1, 3),
    _IpfixMeteringProcessCacheActiveTimeout_Type()
)
ipfixMeteringProcessCacheActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheActiveTimeout.setUnits("seconds")
_IpfixMeteringProcessCacheIdleTimeout_Type = Unsigned32
_IpfixMeteringProcessCacheIdleTimeout_Object = MibTableColumn
ipfixMeteringProcessCacheIdleTimeout = _IpfixMeteringProcessCacheIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 5, 1, 4),
    _IpfixMeteringProcessCacheIdleTimeout_Type()
)
ipfixMeteringProcessCacheIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheIdleTimeout.setUnits("seconds")
_IpfixObservationPointTable_Object = MibTable
ipfixObservationPointTable = _IpfixObservationPointTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipfixObservationPointTable.setStatus("current")
_IpfixObservationPointEntry_Object = MibTableRow
ipfixObservationPointEntry = _IpfixObservationPointEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1)
)
ipfixObservationPointEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixObservationPointGroupId"),
    (0, "IPFIX-MIB", "ipfixObservationPointIndex"),
)
if mibBuilder.loadTexts:
    ipfixObservationPointEntry.setStatus("current")


class _IpfixObservationPointGroupId_Type(Unsigned32):
    """Custom type ipfixObservationPointGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixObservationPointGroupId_Type.__name__ = "Unsigned32"
_IpfixObservationPointGroupId_Object = MibTableColumn
ipfixObservationPointGroupId = _IpfixObservationPointGroupId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 1),
    _IpfixObservationPointGroupId_Type()
)
ipfixObservationPointGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixObservationPointGroupId.setStatus("current")


class _IpfixObservationPointIndex_Type(Unsigned32):
    """Custom type ipfixObservationPointIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixObservationPointIndex_Type.__name__ = "Unsigned32"
_IpfixObservationPointIndex_Object = MibTableColumn
ipfixObservationPointIndex = _IpfixObservationPointIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 2),
    _IpfixObservationPointIndex_Type()
)
ipfixObservationPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixObservationPointIndex.setStatus("current")
_IpfixObservationPointObservationDomainId_Type = Unsigned32
_IpfixObservationPointObservationDomainId_Object = MibTableColumn
ipfixObservationPointObservationDomainId = _IpfixObservationPointObservationDomainId_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 3),
    _IpfixObservationPointObservationDomainId_Type()
)
ipfixObservationPointObservationDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObservationPointObservationDomainId.setStatus("current")
_IpfixObservationPointPhysicalEntity_Type = PhysicalIndexOrZero
_IpfixObservationPointPhysicalEntity_Object = MibTableColumn
ipfixObservationPointPhysicalEntity = _IpfixObservationPointPhysicalEntity_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 4),
    _IpfixObservationPointPhysicalEntity_Type()
)
ipfixObservationPointPhysicalEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObservationPointPhysicalEntity.setStatus("current")
_IpfixObservationPointPhysicalInterface_Type = InterfaceIndexOrZero
_IpfixObservationPointPhysicalInterface_Object = MibTableColumn
ipfixObservationPointPhysicalInterface = _IpfixObservationPointPhysicalInterface_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 5),
    _IpfixObservationPointPhysicalInterface_Type()
)
ipfixObservationPointPhysicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObservationPointPhysicalInterface.setStatus("current")


class _IpfixObservationPointPhysicalEntityDirection_Type(Integer32):
    """Custom type ipfixObservationPointPhysicalEntityDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1),
          ("unknown", 0))
    )


_IpfixObservationPointPhysicalEntityDirection_Type.__name__ = "Integer32"
_IpfixObservationPointPhysicalEntityDirection_Object = MibTableColumn
ipfixObservationPointPhysicalEntityDirection = _IpfixObservationPointPhysicalEntityDirection_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 6, 1, 6),
    _IpfixObservationPointPhysicalEntityDirection_Type()
)
ipfixObservationPointPhysicalEntityDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObservationPointPhysicalEntityDirection.setStatus("current")
_IpfixSelectionProcessTable_Object = MibTable
ipfixSelectionProcessTable = _IpfixSelectionProcessTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ipfixSelectionProcessTable.setStatus("current")
_IpfixSelectionProcessEntry_Object = MibTableRow
ipfixSelectionProcessEntry = _IpfixSelectionProcessEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 7, 1)
)
ipfixSelectionProcessEntry.setIndexNames(
    (0, "IPFIX-MIB", "ipfixMeteringProcessCacheId"),
    (0, "IPFIX-MIB", "ipfixSelectionProcessIndex"),
    (0, "IPFIX-MIB", "ipfixSelectionProcessSelectorIndex"),
)
if mibBuilder.loadTexts:
    ipfixSelectionProcessEntry.setStatus("current")


class _IpfixSelectionProcessIndex_Type(Unsigned32):
    """Custom type ipfixSelectionProcessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixSelectionProcessIndex_Type.__name__ = "Unsigned32"
_IpfixSelectionProcessIndex_Object = MibTableColumn
ipfixSelectionProcessIndex = _IpfixSelectionProcessIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 7, 1, 1),
    _IpfixSelectionProcessIndex_Type()
)
ipfixSelectionProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixSelectionProcessIndex.setStatus("current")


class _IpfixSelectionProcessSelectorIndex_Type(Unsigned32):
    """Custom type ipfixSelectionProcessSelectorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpfixSelectionProcessSelectorIndex_Type.__name__ = "Unsigned32"
_IpfixSelectionProcessSelectorIndex_Object = MibTableColumn
ipfixSelectionProcessSelectorIndex = _IpfixSelectionProcessSelectorIndex_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 7, 1, 2),
    _IpfixSelectionProcessSelectorIndex_Type()
)
ipfixSelectionProcessSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixSelectionProcessSelectorIndex.setStatus("current")
_IpfixSelectionProcessSelectorFunction_Type = ObjectIdentifier
_IpfixSelectionProcessSelectorFunction_Object = MibTableColumn
ipfixSelectionProcessSelectorFunction = _IpfixSelectionProcessSelectorFunction_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 1, 7, 1, 3),
    _IpfixSelectionProcessSelectorFunction_Type()
)
ipfixSelectionProcessSelectorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSelectionProcessSelectorFunction.setStatus("current")
_IpfixStatistics_ObjectIdentity = ObjectIdentity
ipfixStatistics = _IpfixStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 1, 2)
)
_IpfixTransportSessionStatsTable_Object = MibTable
ipfixTransportSessionStatsTable = _IpfixTransportSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipfixTransportSessionStatsTable.setStatus("current")
_IpfixTransportSessionStatsEntry_Object = MibTableRow
ipfixTransportSessionStatsEntry = _IpfixTransportSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixTransportSessionStatsEntry.setStatus("current")
_IpfixTransportSessionRate_Type = Gauge32
_IpfixTransportSessionRate_Object = MibTableColumn
ipfixTransportSessionRate = _IpfixTransportSessionRate_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 1),
    _IpfixTransportSessionRate_Type()
)
ipfixTransportSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionRate.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionRate.setUnits("bytes/second")
_IpfixTransportSessionPackets_Type = Counter64
_IpfixTransportSessionPackets_Object = MibTableColumn
ipfixTransportSessionPackets = _IpfixTransportSessionPackets_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 2),
    _IpfixTransportSessionPackets_Type()
)
ipfixTransportSessionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionPackets.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionPackets.setUnits("packets")
_IpfixTransportSessionBytes_Type = Counter64
_IpfixTransportSessionBytes_Object = MibTableColumn
ipfixTransportSessionBytes = _IpfixTransportSessionBytes_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 3),
    _IpfixTransportSessionBytes_Type()
)
ipfixTransportSessionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionBytes.setStatus("current")
if mibBuilder.loadTexts:
    ipfixTransportSessionBytes.setUnits("bytes")
_IpfixTransportSessionMessages_Type = Counter64
_IpfixTransportSessionMessages_Object = MibTableColumn
ipfixTransportSessionMessages = _IpfixTransportSessionMessages_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 4),
    _IpfixTransportSessionMessages_Type()
)
ipfixTransportSessionMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionMessages.setStatus("current")
_IpfixTransportSessionDiscardedMessages_Type = Counter64
_IpfixTransportSessionDiscardedMessages_Object = MibTableColumn
ipfixTransportSessionDiscardedMessages = _IpfixTransportSessionDiscardedMessages_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 5),
    _IpfixTransportSessionDiscardedMessages_Type()
)
ipfixTransportSessionDiscardedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDiscardedMessages.setStatus("current")
_IpfixTransportSessionRecords_Type = Counter64
_IpfixTransportSessionRecords_Object = MibTableColumn
ipfixTransportSessionRecords = _IpfixTransportSessionRecords_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 6),
    _IpfixTransportSessionRecords_Type()
)
ipfixTransportSessionRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionRecords.setStatus("current")
_IpfixTransportSessionTemplates_Type = Counter64
_IpfixTransportSessionTemplates_Object = MibTableColumn
ipfixTransportSessionTemplates = _IpfixTransportSessionTemplates_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 7),
    _IpfixTransportSessionTemplates_Type()
)
ipfixTransportSessionTemplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionTemplates.setStatus("current")
_IpfixTransportSessionOptionsTemplates_Type = Counter64
_IpfixTransportSessionOptionsTemplates_Object = MibTableColumn
ipfixTransportSessionOptionsTemplates = _IpfixTransportSessionOptionsTemplates_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 8),
    _IpfixTransportSessionOptionsTemplates_Type()
)
ipfixTransportSessionOptionsTemplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionOptionsTemplates.setStatus("current")
_IpfixTransportSessionDiscontinuityTime_Type = TimeStamp
_IpfixTransportSessionDiscontinuityTime_Object = MibTableColumn
ipfixTransportSessionDiscontinuityTime = _IpfixTransportSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 1, 1, 9),
    _IpfixTransportSessionDiscontinuityTime_Type()
)
ipfixTransportSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTransportSessionDiscontinuityTime.setStatus("current")
_IpfixTemplateStatsTable_Object = MibTable
ipfixTemplateStatsTable = _IpfixTemplateStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipfixTemplateStatsTable.setStatus("current")
_IpfixTemplateStatsEntry_Object = MibTableRow
ipfixTemplateStatsEntry = _IpfixTemplateStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipfixTemplateStatsEntry.setStatus("current")
_IpfixTemplateDataRecords_Type = Counter64
_IpfixTemplateDataRecords_Object = MibTableColumn
ipfixTemplateDataRecords = _IpfixTemplateDataRecords_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 2, 1, 1),
    _IpfixTemplateDataRecords_Type()
)
ipfixTemplateDataRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDataRecords.setStatus("current")
_IpfixTemplateDiscontinuityTime_Type = TimeStamp
_IpfixTemplateDiscontinuityTime_Object = MibTableColumn
ipfixTemplateDiscontinuityTime = _IpfixTemplateDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 2, 1, 2),
    _IpfixTemplateDiscontinuityTime_Type()
)
ipfixTemplateDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateDiscontinuityTime.setStatus("current")
_IpfixMeteringProcessStatsTable_Object = MibTable
ipfixMeteringProcessStatsTable = _IpfixMeteringProcessStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipfixMeteringProcessStatsTable.setStatus("current")
_IpfixMeteringProcessStatsEntry_Object = MibTableRow
ipfixMeteringProcessStatsEntry = _IpfixMeteringProcessStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipfixMeteringProcessStatsEntry.setStatus("current")
_IpfixMeteringProcessCacheActiveFlows_Type = Gauge32
_IpfixMeteringProcessCacheActiveFlows_Object = MibTableColumn
ipfixMeteringProcessCacheActiveFlows = _IpfixMeteringProcessCacheActiveFlows_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3, 1, 1),
    _IpfixMeteringProcessCacheActiveFlows_Type()
)
ipfixMeteringProcessCacheActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheActiveFlows.setStatus("current")
_IpfixMeteringProcessCacheUnusedCacheEntries_Type = Gauge32
_IpfixMeteringProcessCacheUnusedCacheEntries_Object = MibTableColumn
ipfixMeteringProcessCacheUnusedCacheEntries = _IpfixMeteringProcessCacheUnusedCacheEntries_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3, 1, 2),
    _IpfixMeteringProcessCacheUnusedCacheEntries_Type()
)
ipfixMeteringProcessCacheUnusedCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheUnusedCacheEntries.setStatus("current")
_IpfixMeteringProcessCacheDataRecords_Type = Counter64
_IpfixMeteringProcessCacheDataRecords_Object = MibTableColumn
ipfixMeteringProcessCacheDataRecords = _IpfixMeteringProcessCacheDataRecords_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3, 1, 3),
    _IpfixMeteringProcessCacheDataRecords_Type()
)
ipfixMeteringProcessCacheDataRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheDataRecords.setStatus("current")
_IpfixMeteringProcessCacheDiscontinuityTime_Type = TimeStamp
_IpfixMeteringProcessCacheDiscontinuityTime_Object = MibTableColumn
ipfixMeteringProcessCacheDiscontinuityTime = _IpfixMeteringProcessCacheDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 3, 1, 4),
    _IpfixMeteringProcessCacheDiscontinuityTime_Type()
)
ipfixMeteringProcessCacheDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMeteringProcessCacheDiscontinuityTime.setStatus("current")
_IpfixSelectionProcessStatsTable_Object = MibTable
ipfixSelectionProcessStatsTable = _IpfixSelectionProcessStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ipfixSelectionProcessStatsTable.setStatus("current")
_IpfixSelectionProcessStatsEntry_Object = MibTableRow
ipfixSelectionProcessStatsEntry = _IpfixSelectionProcessStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ipfixSelectionProcessStatsEntry.setStatus("current")
_IpfixSelectionProcessStatsPacketsObserved_Type = Counter64
_IpfixSelectionProcessStatsPacketsObserved_Object = MibTableColumn
ipfixSelectionProcessStatsPacketsObserved = _IpfixSelectionProcessStatsPacketsObserved_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 4, 1, 1),
    _IpfixSelectionProcessStatsPacketsObserved_Type()
)
ipfixSelectionProcessStatsPacketsObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSelectionProcessStatsPacketsObserved.setStatus("current")
_IpfixSelectionProcessStatsPacketsDropped_Type = Counter64
_IpfixSelectionProcessStatsPacketsDropped_Object = MibTableColumn
ipfixSelectionProcessStatsPacketsDropped = _IpfixSelectionProcessStatsPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 4, 1, 2),
    _IpfixSelectionProcessStatsPacketsDropped_Type()
)
ipfixSelectionProcessStatsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSelectionProcessStatsPacketsDropped.setStatus("current")
_IpfixSelectionProcessStatsDiscontinuityTime_Type = TimeStamp
_IpfixSelectionProcessStatsDiscontinuityTime_Object = MibTableColumn
ipfixSelectionProcessStatsDiscontinuityTime = _IpfixSelectionProcessStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 193, 1, 2, 4, 1, 3),
    _IpfixSelectionProcessStatsDiscontinuityTime_Type()
)
ipfixSelectionProcessStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSelectionProcessStatsDiscontinuityTime.setStatus("current")
_IpfixConformance_ObjectIdentity = ObjectIdentity
ipfixConformance = _IpfixConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 2)
)
_IpfixCompliances_ObjectIdentity = ObjectIdentity
ipfixCompliances = _IpfixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 2, 1)
)
_IpfixGroups_ObjectIdentity = ObjectIdentity
ipfixGroups = _IpfixGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 193, 2, 2)
)
ipfixTransportSessionEntry.registerAugmentions(
    ("IPFIX-MIB",
     "ipfixTransportSessionStatsEntry")
)
ipfixTransportSessionStatsEntry.setIndexNames(*ipfixTransportSessionEntry.getIndexNames())
ipfixTemplateEntry.registerAugmentions(
    ("IPFIX-MIB",
     "ipfixTemplateStatsEntry")
)
ipfixTemplateStatsEntry.setIndexNames(*ipfixTemplateEntry.getIndexNames())
ipfixMeteringProcessEntry.registerAugmentions(
    ("IPFIX-MIB",
     "ipfixMeteringProcessStatsEntry")
)
ipfixMeteringProcessStatsEntry.setIndexNames(*ipfixMeteringProcessEntry.getIndexNames())
ipfixSelectionProcessEntry.registerAugmentions(
    ("IPFIX-MIB",
     "ipfixSelectionProcessStatsEntry")
)
ipfixSelectionProcessStatsEntry.setIndexNames(*ipfixSelectionProcessEntry.getIndexNames())

# Managed Objects groups

ipfixCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 193, 2, 2, 1)
)
ipfixCommonGroup.setObjects(
      *(("IPFIX-MIB", "ipfixTransportSessionProtocol"),
        ("IPFIX-MIB", "ipfixTransportSessionSourceAddressType"),
        ("IPFIX-MIB", "ipfixTransportSessionSourceAddress"),
        ("IPFIX-MIB", "ipfixTransportSessionDestinationAddressType"),
        ("IPFIX-MIB", "ipfixTransportSessionDestinationAddress"),
        ("IPFIX-MIB", "ipfixTransportSessionSourcePort"),
        ("IPFIX-MIB", "ipfixTransportSessionDestinationPort"),
        ("IPFIX-MIB", "ipfixTransportSessionSctpAssocId"),
        ("IPFIX-MIB", "ipfixTransportSessionDeviceMode"),
        ("IPFIX-MIB", "ipfixTransportSessionTemplateRefreshTimeout"),
        ("IPFIX-MIB", "ipfixTransportSessionOptionsTemplateRefreshTimeout"),
        ("IPFIX-MIB", "ipfixTransportSessionTemplateRefreshPacket"),
        ("IPFIX-MIB", "ipfixTransportSessionOptionsTemplateRefreshPacket"),
        ("IPFIX-MIB", "ipfixTransportSessionIpfixVersion"),
        ("IPFIX-MIB", "ipfixTransportSessionStatus"),
        ("IPFIX-MIB", "ipfixTemplateSetId"),
        ("IPFIX-MIB", "ipfixTemplateAccessTime"),
        ("IPFIX-MIB", "ipfixTemplateDefinitionIeId"),
        ("IPFIX-MIB", "ipfixTemplateDefinitionIeLength"),
        ("IPFIX-MIB", "ipfixTemplateDefinitionEnterpriseNumber"),
        ("IPFIX-MIB", "ipfixTemplateDefinitionFlags"))
)
if mibBuilder.loadTexts:
    ipfixCommonGroup.setStatus("current")

ipfixCommonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 193, 2, 2, 2)
)
ipfixCommonStatsGroup.setObjects(
      *(("IPFIX-MIB", "ipfixTransportSessionRate"),
        ("IPFIX-MIB", "ipfixTransportSessionPackets"),
        ("IPFIX-MIB", "ipfixTransportSessionBytes"),
        ("IPFIX-MIB", "ipfixTransportSessionMessages"),
        ("IPFIX-MIB", "ipfixTransportSessionDiscardedMessages"),
        ("IPFIX-MIB", "ipfixTransportSessionRecords"),
        ("IPFIX-MIB", "ipfixTransportSessionTemplates"),
        ("IPFIX-MIB", "ipfixTransportSessionOptionsTemplates"),
        ("IPFIX-MIB", "ipfixTransportSessionDiscontinuityTime"),
        ("IPFIX-MIB", "ipfixTemplateDataRecords"),
        ("IPFIX-MIB", "ipfixTemplateDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ipfixCommonStatsGroup.setStatus("current")

ipfixExporterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 193, 2, 2, 3)
)
ipfixExporterGroup.setObjects(
      *(("IPFIX-MIB", "ipfixExportMemberType"),
        ("IPFIX-MIB", "ipfixMeteringProcessObservationPointGroupRef"),
        ("IPFIX-MIB", "ipfixMeteringProcessCacheActiveTimeout"),
        ("IPFIX-MIB", "ipfixMeteringProcessCacheIdleTimeout"),
        ("IPFIX-MIB", "ipfixObservationPointObservationDomainId"),
        ("IPFIX-MIB", "ipfixObservationPointPhysicalEntity"),
        ("IPFIX-MIB", "ipfixObservationPointPhysicalInterface"),
        ("IPFIX-MIB", "ipfixObservationPointPhysicalEntityDirection"),
        ("IPFIX-MIB", "ipfixSelectionProcessSelectorFunction"))
)
if mibBuilder.loadTexts:
    ipfixExporterGroup.setStatus("current")

ipfixExporterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 193, 2, 2, 4)
)
ipfixExporterStatsGroup.setObjects(
      *(("IPFIX-MIB", "ipfixMeteringProcessCacheActiveFlows"),
        ("IPFIX-MIB", "ipfixMeteringProcessCacheUnusedCacheEntries"),
        ("IPFIX-MIB", "ipfixMeteringProcessCacheDataRecords"),
        ("IPFIX-MIB", "ipfixMeteringProcessCacheDiscontinuityTime"),
        ("IPFIX-MIB", "ipfixSelectionProcessStatsPacketsObserved"),
        ("IPFIX-MIB", "ipfixSelectionProcessStatsPacketsDropped"),
        ("IPFIX-MIB", "ipfixSelectionProcessStatsDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ipfixExporterStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipfixCollectorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 193, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixCollectorCompliance.setStatus(
        "current"
    )

ipfixExporterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 193, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipfixExporterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-MIB",
    **{"ipfixMIB": ipfixMIB,
       "ipfixObjects": ipfixObjects,
       "ipfixMainObjects": ipfixMainObjects,
       "ipfixTransportSessionTable": ipfixTransportSessionTable,
       "ipfixTransportSessionEntry": ipfixTransportSessionEntry,
       "ipfixTransportSessionIndex": ipfixTransportSessionIndex,
       "ipfixTransportSessionProtocol": ipfixTransportSessionProtocol,
       "ipfixTransportSessionSourceAddressType": ipfixTransportSessionSourceAddressType,
       "ipfixTransportSessionSourceAddress": ipfixTransportSessionSourceAddress,
       "ipfixTransportSessionDestinationAddressType": ipfixTransportSessionDestinationAddressType,
       "ipfixTransportSessionDestinationAddress": ipfixTransportSessionDestinationAddress,
       "ipfixTransportSessionSourcePort": ipfixTransportSessionSourcePort,
       "ipfixTransportSessionDestinationPort": ipfixTransportSessionDestinationPort,
       "ipfixTransportSessionSctpAssocId": ipfixTransportSessionSctpAssocId,
       "ipfixTransportSessionDeviceMode": ipfixTransportSessionDeviceMode,
       "ipfixTransportSessionTemplateRefreshTimeout": ipfixTransportSessionTemplateRefreshTimeout,
       "ipfixTransportSessionOptionsTemplateRefreshTimeout": ipfixTransportSessionOptionsTemplateRefreshTimeout,
       "ipfixTransportSessionTemplateRefreshPacket": ipfixTransportSessionTemplateRefreshPacket,
       "ipfixTransportSessionOptionsTemplateRefreshPacket": ipfixTransportSessionOptionsTemplateRefreshPacket,
       "ipfixTransportSessionIpfixVersion": ipfixTransportSessionIpfixVersion,
       "ipfixTransportSessionStatus": ipfixTransportSessionStatus,
       "ipfixTemplateTable": ipfixTemplateTable,
       "ipfixTemplateEntry": ipfixTemplateEntry,
       "ipfixTemplateObservationDomainId": ipfixTemplateObservationDomainId,
       "ipfixTemplateId": ipfixTemplateId,
       "ipfixTemplateSetId": ipfixTemplateSetId,
       "ipfixTemplateAccessTime": ipfixTemplateAccessTime,
       "ipfixTemplateDefinitionTable": ipfixTemplateDefinitionTable,
       "ipfixTemplateDefinitionEntry": ipfixTemplateDefinitionEntry,
       "ipfixTemplateDefinitionIndex": ipfixTemplateDefinitionIndex,
       "ipfixTemplateDefinitionIeId": ipfixTemplateDefinitionIeId,
       "ipfixTemplateDefinitionIeLength": ipfixTemplateDefinitionIeLength,
       "ipfixTemplateDefinitionEnterpriseNumber": ipfixTemplateDefinitionEnterpriseNumber,
       "ipfixTemplateDefinitionFlags": ipfixTemplateDefinitionFlags,
       "ipfixExportTable": ipfixExportTable,
       "ipfixExportEntry": ipfixExportEntry,
       "ipfixExportIndex": ipfixExportIndex,
       "ipfixExportMemberType": ipfixExportMemberType,
       "ipfixMeteringProcessTable": ipfixMeteringProcessTable,
       "ipfixMeteringProcessEntry": ipfixMeteringProcessEntry,
       "ipfixMeteringProcessCacheId": ipfixMeteringProcessCacheId,
       "ipfixMeteringProcessObservationPointGroupRef": ipfixMeteringProcessObservationPointGroupRef,
       "ipfixMeteringProcessCacheActiveTimeout": ipfixMeteringProcessCacheActiveTimeout,
       "ipfixMeteringProcessCacheIdleTimeout": ipfixMeteringProcessCacheIdleTimeout,
       "ipfixObservationPointTable": ipfixObservationPointTable,
       "ipfixObservationPointEntry": ipfixObservationPointEntry,
       "ipfixObservationPointGroupId": ipfixObservationPointGroupId,
       "ipfixObservationPointIndex": ipfixObservationPointIndex,
       "ipfixObservationPointObservationDomainId": ipfixObservationPointObservationDomainId,
       "ipfixObservationPointPhysicalEntity": ipfixObservationPointPhysicalEntity,
       "ipfixObservationPointPhysicalInterface": ipfixObservationPointPhysicalInterface,
       "ipfixObservationPointPhysicalEntityDirection": ipfixObservationPointPhysicalEntityDirection,
       "ipfixSelectionProcessTable": ipfixSelectionProcessTable,
       "ipfixSelectionProcessEntry": ipfixSelectionProcessEntry,
       "ipfixSelectionProcessIndex": ipfixSelectionProcessIndex,
       "ipfixSelectionProcessSelectorIndex": ipfixSelectionProcessSelectorIndex,
       "ipfixSelectionProcessSelectorFunction": ipfixSelectionProcessSelectorFunction,
       "ipfixStatistics": ipfixStatistics,
       "ipfixTransportSessionStatsTable": ipfixTransportSessionStatsTable,
       "ipfixTransportSessionStatsEntry": ipfixTransportSessionStatsEntry,
       "ipfixTransportSessionRate": ipfixTransportSessionRate,
       "ipfixTransportSessionPackets": ipfixTransportSessionPackets,
       "ipfixTransportSessionBytes": ipfixTransportSessionBytes,
       "ipfixTransportSessionMessages": ipfixTransportSessionMessages,
       "ipfixTransportSessionDiscardedMessages": ipfixTransportSessionDiscardedMessages,
       "ipfixTransportSessionRecords": ipfixTransportSessionRecords,
       "ipfixTransportSessionTemplates": ipfixTransportSessionTemplates,
       "ipfixTransportSessionOptionsTemplates": ipfixTransportSessionOptionsTemplates,
       "ipfixTransportSessionDiscontinuityTime": ipfixTransportSessionDiscontinuityTime,
       "ipfixTemplateStatsTable": ipfixTemplateStatsTable,
       "ipfixTemplateStatsEntry": ipfixTemplateStatsEntry,
       "ipfixTemplateDataRecords": ipfixTemplateDataRecords,
       "ipfixTemplateDiscontinuityTime": ipfixTemplateDiscontinuityTime,
       "ipfixMeteringProcessStatsTable": ipfixMeteringProcessStatsTable,
       "ipfixMeteringProcessStatsEntry": ipfixMeteringProcessStatsEntry,
       "ipfixMeteringProcessCacheActiveFlows": ipfixMeteringProcessCacheActiveFlows,
       "ipfixMeteringProcessCacheUnusedCacheEntries": ipfixMeteringProcessCacheUnusedCacheEntries,
       "ipfixMeteringProcessCacheDataRecords": ipfixMeteringProcessCacheDataRecords,
       "ipfixMeteringProcessCacheDiscontinuityTime": ipfixMeteringProcessCacheDiscontinuityTime,
       "ipfixSelectionProcessStatsTable": ipfixSelectionProcessStatsTable,
       "ipfixSelectionProcessStatsEntry": ipfixSelectionProcessStatsEntry,
       "ipfixSelectionProcessStatsPacketsObserved": ipfixSelectionProcessStatsPacketsObserved,
       "ipfixSelectionProcessStatsPacketsDropped": ipfixSelectionProcessStatsPacketsDropped,
       "ipfixSelectionProcessStatsDiscontinuityTime": ipfixSelectionProcessStatsDiscontinuityTime,
       "ipfixConformance": ipfixConformance,
       "ipfixCompliances": ipfixCompliances,
       "ipfixCollectorCompliance": ipfixCollectorCompliance,
       "ipfixExporterCompliance": ipfixExporterCompliance,
       "ipfixGroups": ipfixGroups,
       "ipfixCommonGroup": ipfixCommonGroup,
       "ipfixCommonStatsGroup": ipfixCommonStatsGroup,
       "ipfixExporterGroup": ipfixExporterGroup,
       "ipfixExporterStatsGroup": ipfixExporterStatsGroup}
)
