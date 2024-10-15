# SNMP MIB module (Dell-rlBrgMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-rlBrgMulticast-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:34 2024
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

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlBrgMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 116)
)
rlBrgMulticast.setRevisions(
        ("2013-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DynamicCmdType(Integer32, TextualConvention):
    status = "current"
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
        *(("addPorts", 2),
          ("createEntry", 0),
          ("deleteEntry", 1),
          ("deletePorts", 3))
    )



class VidxIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 32767),
    )



# MIB Managed Objects in the order of their OIDs

_RlBrgMulticastMibVersion_Type = Integer32
_RlBrgMulticastMibVersion_Object = MibScalar
rlBrgMulticastMibVersion = _RlBrgMulticastMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 1),
    _RlBrgMulticastMibVersion_Type()
)
rlBrgMulticastMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMulticastMibVersion.setStatus("current")
_RlBrgStaticIpMulticastTable_Object = MibTable
rlBrgStaticIpMulticastTable = _RlBrgStaticIpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3)
)
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastTable.setStatus("current")
_RlBrgStaticIpMulticastEntry_Object = MibTableRow
rlBrgStaticIpMulticastEntry = _RlBrgStaticIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1)
)
rlBrgStaticIpMulticastEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastVlanTag"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastGroupAddress"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastEntry.setStatus("current")
_RlBrgStaticIpMulticastVlanTag_Type = VlanIndex
_RlBrgStaticIpMulticastVlanTag_Object = MibTableColumn
rlBrgStaticIpMulticastVlanTag = _RlBrgStaticIpMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 1),
    _RlBrgStaticIpMulticastVlanTag_Type()
)
rlBrgStaticIpMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastVlanTag.setStatus("current")
_RlBrgStaticIpMulticastGroupAddress_Type = IpAddress
_RlBrgStaticIpMulticastGroupAddress_Object = MibTableColumn
rlBrgStaticIpMulticastGroupAddress = _RlBrgStaticIpMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 2),
    _RlBrgStaticIpMulticastGroupAddress_Type()
)
rlBrgStaticIpMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastGroupAddress.setStatus("current")
_RlBrgStaticIpMulticastSourceAddress_Type = IpAddress
_RlBrgStaticIpMulticastSourceAddress_Object = MibTableColumn
rlBrgStaticIpMulticastSourceAddress = _RlBrgStaticIpMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 3),
    _RlBrgStaticIpMulticastSourceAddress_Type()
)
rlBrgStaticIpMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastSourceAddress.setStatus("current")
_RlBrgStaticIpMulticastFrwPorts_Type = PortList
_RlBrgStaticIpMulticastFrwPorts_Object = MibTableColumn
rlBrgStaticIpMulticastFrwPorts = _RlBrgStaticIpMulticastFrwPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 4),
    _RlBrgStaticIpMulticastFrwPorts_Type()
)
rlBrgStaticIpMulticastFrwPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastFrwPorts.setStatus("current")
_RlBrgStaticIpMulticastForbiddenPorts_Type = PortList
_RlBrgStaticIpMulticastForbiddenPorts_Object = MibTableColumn
rlBrgStaticIpMulticastForbiddenPorts = _RlBrgStaticIpMulticastForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 5),
    _RlBrgStaticIpMulticastForbiddenPorts_Type()
)
rlBrgStaticIpMulticastForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastForbiddenPorts.setStatus("current")
_RlBrgStaticIpMulticastStatus_Type = RowStatus
_RlBrgStaticIpMulticastStatus_Object = MibTableColumn
rlBrgStaticIpMulticastStatus = _RlBrgStaticIpMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 3, 1, 6),
    _RlBrgStaticIpMulticastStatus_Type()
)
rlBrgStaticIpMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastStatus.setStatus("current")
_RlBrgIpMulticastTable_Object = MibTable
rlBrgIpMulticastTable = _RlBrgIpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4)
)
if mibBuilder.loadTexts:
    rlBrgIpMulticastTable.setStatus("current")
_RlBrgIpMulticastEntry_Object = MibTableRow
rlBrgIpMulticastEntry = _RlBrgIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1)
)
rlBrgIpMulticastEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpMulticastVlanTag"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpMulticastGroupAddress"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgIpMulticastEntry.setStatus("current")
_RlBrgIpMulticastVlanTag_Type = VlanIndex
_RlBrgIpMulticastVlanTag_Object = MibTableColumn
rlBrgIpMulticastVlanTag = _RlBrgIpMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 1),
    _RlBrgIpMulticastVlanTag_Type()
)
rlBrgIpMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastVlanTag.setStatus("current")
_RlBrgIpMulticastGroupAddress_Type = IpAddress
_RlBrgIpMulticastGroupAddress_Object = MibTableColumn
rlBrgIpMulticastGroupAddress = _RlBrgIpMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 2),
    _RlBrgIpMulticastGroupAddress_Type()
)
rlBrgIpMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastGroupAddress.setStatus("current")
_RlBrgIpMulticastSourceAddress_Type = IpAddress
_RlBrgIpMulticastSourceAddress_Object = MibTableColumn
rlBrgIpMulticastSourceAddress = _RlBrgIpMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 3),
    _RlBrgIpMulticastSourceAddress_Type()
)
rlBrgIpMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastSourceAddress.setStatus("current")
_RlBrgIpMulticastEgressPorts_Type = PortList
_RlBrgIpMulticastEgressPorts_Object = MibTableColumn
rlBrgIpMulticastEgressPorts = _RlBrgIpMulticastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 4),
    _RlBrgIpMulticastEgressPorts_Type()
)
rlBrgIpMulticastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpMulticastEgressPorts.setStatus("current")
_RlBrgIpMulticastLearntPorts_Type = PortList
_RlBrgIpMulticastLearntPorts_Object = MibTableColumn
rlBrgIpMulticastLearntPorts = _RlBrgIpMulticastLearntPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 4, 1, 5),
    _RlBrgIpMulticastLearntPorts_Type()
)
rlBrgIpMulticastLearntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpMulticastLearntPorts.setStatus("current")
_RlBrgStaticInetMulticastTable_Object = MibTable
rlBrgStaticInetMulticastTable = _RlBrgStaticInetMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5)
)
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastTable.setStatus("current")
_RlBrgStaticInetMulticastEntry_Object = MibTableRow
rlBrgStaticInetMulticastEntry = _RlBrgStaticInetMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1)
)
rlBrgStaticInetMulticastEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastVlanTag"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddress"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastEntry.setStatus("current")
_RlBrgStaticInetMulticastVlanTag_Type = VlanIndex
_RlBrgStaticInetMulticastVlanTag_Object = MibTableColumn
rlBrgStaticInetMulticastVlanTag = _RlBrgStaticInetMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 1),
    _RlBrgStaticInetMulticastVlanTag_Type()
)
rlBrgStaticInetMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastVlanTag.setStatus("current")
_RlBrgStaticInetMulticastGroupAddressType_Type = InetAddressType
_RlBrgStaticInetMulticastGroupAddressType_Object = MibTableColumn
rlBrgStaticInetMulticastGroupAddressType = _RlBrgStaticInetMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 2),
    _RlBrgStaticInetMulticastGroupAddressType_Type()
)
rlBrgStaticInetMulticastGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastGroupAddressType.setStatus("current")
_RlBrgStaticInetMulticastGroupAddress_Type = InetAddress
_RlBrgStaticInetMulticastGroupAddress_Object = MibTableColumn
rlBrgStaticInetMulticastGroupAddress = _RlBrgStaticInetMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 3),
    _RlBrgStaticInetMulticastGroupAddress_Type()
)
rlBrgStaticInetMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastGroupAddress.setStatus("current")
_RlBrgStaticInetMulticastSourceAddressType_Type = InetAddressType
_RlBrgStaticInetMulticastSourceAddressType_Object = MibTableColumn
rlBrgStaticInetMulticastSourceAddressType = _RlBrgStaticInetMulticastSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 4),
    _RlBrgStaticInetMulticastSourceAddressType_Type()
)
rlBrgStaticInetMulticastSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastSourceAddressType.setStatus("current")
_RlBrgStaticInetMulticastSourceAddress_Type = InetAddress
_RlBrgStaticInetMulticastSourceAddress_Object = MibTableColumn
rlBrgStaticInetMulticastSourceAddress = _RlBrgStaticInetMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 5),
    _RlBrgStaticInetMulticastSourceAddress_Type()
)
rlBrgStaticInetMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastSourceAddress.setStatus("current")
_RlBrgStaticInetMulticastFrwPorts_Type = PortList
_RlBrgStaticInetMulticastFrwPorts_Object = MibTableColumn
rlBrgStaticInetMulticastFrwPorts = _RlBrgStaticInetMulticastFrwPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 6),
    _RlBrgStaticInetMulticastFrwPorts_Type()
)
rlBrgStaticInetMulticastFrwPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastFrwPorts.setStatus("current")
_RlBrgStaticInetMulticastForbiddenPorts_Type = PortList
_RlBrgStaticInetMulticastForbiddenPorts_Object = MibTableColumn
rlBrgStaticInetMulticastForbiddenPorts = _RlBrgStaticInetMulticastForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 7),
    _RlBrgStaticInetMulticastForbiddenPorts_Type()
)
rlBrgStaticInetMulticastForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastForbiddenPorts.setStatus("current")
_RlBrgStaticInetMulticastStatus_Type = RowStatus
_RlBrgStaticInetMulticastStatus_Object = MibTableColumn
rlBrgStaticInetMulticastStatus = _RlBrgStaticInetMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 5, 1, 8),
    _RlBrgStaticInetMulticastStatus_Type()
)
rlBrgStaticInetMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastStatus.setStatus("current")
_RlBrgInetMulticastTable_Object = MibTable
rlBrgInetMulticastTable = _RlBrgInetMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6)
)
if mibBuilder.loadTexts:
    rlBrgInetMulticastTable.setStatus("current")
_RlBrgInetMulticastEntry_Object = MibTableRow
rlBrgInetMulticastEntry = _RlBrgInetMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1)
)
rlBrgInetMulticastEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgInetMulticastVlanTag"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddress"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgInetMulticastEntry.setStatus("current")
_RlBrgInetMulticastVlanTag_Type = VlanIndex
_RlBrgInetMulticastVlanTag_Object = MibTableColumn
rlBrgInetMulticastVlanTag = _RlBrgInetMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 1),
    _RlBrgInetMulticastVlanTag_Type()
)
rlBrgInetMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastVlanTag.setStatus("current")
_RlBrgInetMulticastGroupAddressType_Type = InetAddressType
_RlBrgInetMulticastGroupAddressType_Object = MibTableColumn
rlBrgInetMulticastGroupAddressType = _RlBrgInetMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 2),
    _RlBrgInetMulticastGroupAddressType_Type()
)
rlBrgInetMulticastGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastGroupAddressType.setStatus("current")
_RlBrgInetMulticastGroupAddress_Type = InetAddress
_RlBrgInetMulticastGroupAddress_Object = MibTableColumn
rlBrgInetMulticastGroupAddress = _RlBrgInetMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 3),
    _RlBrgInetMulticastGroupAddress_Type()
)
rlBrgInetMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastGroupAddress.setStatus("current")
_RlBrgInetMulticastSourceAddressType_Type = InetAddressType
_RlBrgInetMulticastSourceAddressType_Object = MibTableColumn
rlBrgInetMulticastSourceAddressType = _RlBrgInetMulticastSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 4),
    _RlBrgInetMulticastSourceAddressType_Type()
)
rlBrgInetMulticastSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastSourceAddressType.setStatus("current")
_RlBrgInetMulticastSourceAddress_Type = InetAddress
_RlBrgInetMulticastSourceAddress_Object = MibTableColumn
rlBrgInetMulticastSourceAddress = _RlBrgInetMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 5),
    _RlBrgInetMulticastSourceAddress_Type()
)
rlBrgInetMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastSourceAddress.setStatus("current")
_RlBrgInetMulticastEgressPorts_Type = PortList
_RlBrgInetMulticastEgressPorts_Object = MibTableColumn
rlBrgInetMulticastEgressPorts = _RlBrgInetMulticastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 6),
    _RlBrgInetMulticastEgressPorts_Type()
)
rlBrgInetMulticastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastEgressPorts.setStatus("current")
_RlBrgInetMulticastLearntPorts_Type = PortList
_RlBrgInetMulticastLearntPorts_Object = MibTableColumn
rlBrgInetMulticastLearntPorts = _RlBrgInetMulticastLearntPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 6, 1, 7),
    _RlBrgInetMulticastLearntPorts_Type()
)
rlBrgInetMulticastLearntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastLearntPorts.setStatus("current")
_RlBrgIpmFdbRefTable_Object = MibTable
rlBrgIpmFdbRefTable = _RlBrgIpmFdbRefTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7)
)
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefTable.setStatus("current")
_RlBrgIpmFdbRefEntry_Object = MibTableRow
rlBrgIpmFdbRefEntry = _RlBrgIpmFdbRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1)
)
rlBrgIpmFdbRefEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpmFdbRefVlanTag"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddress"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddressType"),
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefEntry.setStatus("current")
_RlBrgIpmFdbRefVlanTag_Type = VlanIndex
_RlBrgIpmFdbRefVlanTag_Object = MibTableColumn
rlBrgIpmFdbRefVlanTag = _RlBrgIpmFdbRefVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 1),
    _RlBrgIpmFdbRefVlanTag_Type()
)
rlBrgIpmFdbRefVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefVlanTag.setStatus("current")
_RlBrgIpmFdbRefGroupAddressType_Type = InetAddressType
_RlBrgIpmFdbRefGroupAddressType_Object = MibTableColumn
rlBrgIpmFdbRefGroupAddressType = _RlBrgIpmFdbRefGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 2),
    _RlBrgIpmFdbRefGroupAddressType_Type()
)
rlBrgIpmFdbRefGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefGroupAddressType.setStatus("current")
_RlBrgIpmFdbRefGroupAddress_Type = InetAddress
_RlBrgIpmFdbRefGroupAddress_Object = MibTableColumn
rlBrgIpmFdbRefGroupAddress = _RlBrgIpmFdbRefGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 3),
    _RlBrgIpmFdbRefGroupAddress_Type()
)
rlBrgIpmFdbRefGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefGroupAddress.setStatus("current")
_RlBrgIpmFdbRefSourceAddressType_Type = InetAddressType
_RlBrgIpmFdbRefSourceAddressType_Object = MibTableColumn
rlBrgIpmFdbRefSourceAddressType = _RlBrgIpmFdbRefSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 4),
    _RlBrgIpmFdbRefSourceAddressType_Type()
)
rlBrgIpmFdbRefSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefSourceAddressType.setStatus("current")
_RlBrgIpmFdbRefSourceAddress_Type = InetAddress
_RlBrgIpmFdbRefSourceAddress_Object = MibTableColumn
rlBrgIpmFdbRefSourceAddress = _RlBrgIpmFdbRefSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 5),
    _RlBrgIpmFdbRefSourceAddress_Type()
)
rlBrgIpmFdbRefSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefSourceAddress.setStatus("current")
_RlBrgIpmFdbRefPorts_Type = PortList
_RlBrgIpmFdbRefPorts_Object = MibTableColumn
rlBrgIpmFdbRefPorts = _RlBrgIpmFdbRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 7, 1, 6),
    _RlBrgIpmFdbRefPorts_Type()
)
rlBrgIpmFdbRefPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefPorts.setStatus("current")
_RlBrgDynamicCmdTable_Object = MibTable
rlBrgDynamicCmdTable = _RlBrgDynamicCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8)
)
if mibBuilder.loadTexts:
    rlBrgDynamicCmdTable.setStatus("current")
_RlBrgDynamicCmdEntry_Object = MibTableRow
rlBrgDynamicCmdEntry = _RlBrgDynamicCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1)
)
rlBrgDynamicCmdEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlBrgDynamicCmdKey"),
)
if mibBuilder.loadTexts:
    rlBrgDynamicCmdEntry.setStatus("current")


class _RlBrgDynamicCmdKey_Type(Integer32):
    """Custom type rlBrgDynamicCmdKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlBrgDynamicCmdKey_Type.__name__ = "Integer32"
_RlBrgDynamicCmdKey_Object = MibTableColumn
rlBrgDynamicCmdKey = _RlBrgDynamicCmdKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 1),
    _RlBrgDynamicCmdKey_Type()
)
rlBrgDynamicCmdKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdKey.setStatus("current")
_RlBrgDynamicCmdVlanTag_Type = VlanIndex
_RlBrgDynamicCmdVlanTag_Object = MibTableColumn
rlBrgDynamicCmdVlanTag = _RlBrgDynamicCmdVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 2),
    _RlBrgDynamicCmdVlanTag_Type()
)
rlBrgDynamicCmdVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdVlanTag.setStatus("current")
_RlBrgDynamicCmdGroupAddressType_Type = InetAddressType
_RlBrgDynamicCmdGroupAddressType_Object = MibTableColumn
rlBrgDynamicCmdGroupAddressType = _RlBrgDynamicCmdGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 3),
    _RlBrgDynamicCmdGroupAddressType_Type()
)
rlBrgDynamicCmdGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdGroupAddressType.setStatus("current")
_RlBrgDynamicCmdGroupAddress_Type = InetAddress
_RlBrgDynamicCmdGroupAddress_Object = MibTableColumn
rlBrgDynamicCmdGroupAddress = _RlBrgDynamicCmdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 4),
    _RlBrgDynamicCmdGroupAddress_Type()
)
rlBrgDynamicCmdGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdGroupAddress.setStatus("current")
_RlBrgDynamicCmdSourceAddressType_Type = InetAddressType
_RlBrgDynamicCmdSourceAddressType_Object = MibTableColumn
rlBrgDynamicCmdSourceAddressType = _RlBrgDynamicCmdSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 5),
    _RlBrgDynamicCmdSourceAddressType_Type()
)
rlBrgDynamicCmdSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdSourceAddressType.setStatus("current")
_RlBrgDynamicCmdSourceAddress_Type = InetAddress
_RlBrgDynamicCmdSourceAddress_Object = MibTableColumn
rlBrgDynamicCmdSourceAddress = _RlBrgDynamicCmdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 6),
    _RlBrgDynamicCmdSourceAddress_Type()
)
rlBrgDynamicCmdSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdSourceAddress.setStatus("current")
_RlBrgDynamicCmdPorts_Type = PortList
_RlBrgDynamicCmdPorts_Object = MibTableColumn
rlBrgDynamicCmdPorts = _RlBrgDynamicCmdPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 7),
    _RlBrgDynamicCmdPorts_Type()
)
rlBrgDynamicCmdPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdPorts.setStatus("current")
_RlBrgDynamicCmdType_Type = DynamicCmdType
_RlBrgDynamicCmdType_Object = MibTableColumn
rlBrgDynamicCmdType = _RlBrgDynamicCmdType_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 8, 1, 8),
    _RlBrgDynamicCmdType_Type()
)
rlBrgDynamicCmdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdType.setStatus("current")
_RlUserAssignedVidx_ObjectIdentity = ObjectIdentity
rlUserAssignedVidx = _RlUserAssignedVidx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 116, 9)
)
_RlUserAssignedVidxConfigTable_Object = MibTable
rlUserAssignedVidxConfigTable = _RlUserAssignedVidxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 1)
)
if mibBuilder.loadTexts:
    rlUserAssignedVidxConfigTable.setStatus("current")
_RlUserAssignedVidxConfigEntry_Object = MibTableRow
rlUserAssignedVidxConfigEntry = _RlUserAssignedVidxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1)
)
rlUserAssignedVidxConfigEntry.setIndexNames(
    (0, "Dell-rlBrgMulticast-MIB", "rlUserAssignedVidxConfigIndex"),
)
if mibBuilder.loadTexts:
    rlUserAssignedVidxConfigEntry.setStatus("current")
_RlUserAssignedVidxConfigIndex_Type = VidxIndex
_RlUserAssignedVidxConfigIndex_Object = MibTableColumn
rlUserAssignedVidxConfigIndex = _RlUserAssignedVidxConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 1),
    _RlUserAssignedVidxConfigIndex_Type()
)
rlUserAssignedVidxConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUserAssignedVidxConfigIndex.setStatus("current")
_RlUserAssignedVidxConfigPorts_Type = PortList
_RlUserAssignedVidxConfigPorts_Object = MibTableColumn
rlUserAssignedVidxConfigPorts = _RlUserAssignedVidxConfigPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 2),
    _RlUserAssignedVidxConfigPorts_Type()
)
rlUserAssignedVidxConfigPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUserAssignedVidxConfigPorts.setStatus("current")
_RlUserAssignedVidxConfigRowStatus_Type = RowStatus
_RlUserAssignedVidxConfigRowStatus_Object = MibTableColumn
rlUserAssignedVidxConfigRowStatus = _RlUserAssignedVidxConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 1, 1, 3),
    _RlUserAssignedVidxConfigRowStatus_Type()
)
rlUserAssignedVidxConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlUserAssignedVidxConfigRowStatus.setStatus("current")
_RlUserAssignedVidxGetNextFreeIndex_Type = VidxIndex
_RlUserAssignedVidxGetNextFreeIndex_Object = MibScalar
rlUserAssignedVidxGetNextFreeIndex = _RlUserAssignedVidxGetNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 9, 2),
    _RlUserAssignedVidxGetNextFreeIndex_Type()
)
rlUserAssignedVidxGetNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUserAssignedVidxGetNextFreeIndex.setStatus("current")
_RlBrgMulticastCurrentNumberOfEntries_Type = Unsigned32
_RlBrgMulticastCurrentNumberOfEntries_Object = MibScalar
rlBrgMulticastCurrentNumberOfEntries = _RlBrgMulticastCurrentNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 116, 10),
    _RlBrgMulticastCurrentNumberOfEntries_Type()
)
rlBrgMulticastCurrentNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMulticastCurrentNumberOfEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-rlBrgMulticast-MIB",
    **{"DynamicCmdType": DynamicCmdType,
       "VidxIndex": VidxIndex,
       "rlBrgMulticast": rlBrgMulticast,
       "rlBrgMulticastMibVersion": rlBrgMulticastMibVersion,
       "rlBrgStaticIpMulticastTable": rlBrgStaticIpMulticastTable,
       "rlBrgStaticIpMulticastEntry": rlBrgStaticIpMulticastEntry,
       "rlBrgStaticIpMulticastVlanTag": rlBrgStaticIpMulticastVlanTag,
       "rlBrgStaticIpMulticastGroupAddress": rlBrgStaticIpMulticastGroupAddress,
       "rlBrgStaticIpMulticastSourceAddress": rlBrgStaticIpMulticastSourceAddress,
       "rlBrgStaticIpMulticastFrwPorts": rlBrgStaticIpMulticastFrwPorts,
       "rlBrgStaticIpMulticastForbiddenPorts": rlBrgStaticIpMulticastForbiddenPorts,
       "rlBrgStaticIpMulticastStatus": rlBrgStaticIpMulticastStatus,
       "rlBrgIpMulticastTable": rlBrgIpMulticastTable,
       "rlBrgIpMulticastEntry": rlBrgIpMulticastEntry,
       "rlBrgIpMulticastVlanTag": rlBrgIpMulticastVlanTag,
       "rlBrgIpMulticastGroupAddress": rlBrgIpMulticastGroupAddress,
       "rlBrgIpMulticastSourceAddress": rlBrgIpMulticastSourceAddress,
       "rlBrgIpMulticastEgressPorts": rlBrgIpMulticastEgressPorts,
       "rlBrgIpMulticastLearntPorts": rlBrgIpMulticastLearntPorts,
       "rlBrgStaticInetMulticastTable": rlBrgStaticInetMulticastTable,
       "rlBrgStaticInetMulticastEntry": rlBrgStaticInetMulticastEntry,
       "rlBrgStaticInetMulticastVlanTag": rlBrgStaticInetMulticastVlanTag,
       "rlBrgStaticInetMulticastGroupAddressType": rlBrgStaticInetMulticastGroupAddressType,
       "rlBrgStaticInetMulticastGroupAddress": rlBrgStaticInetMulticastGroupAddress,
       "rlBrgStaticInetMulticastSourceAddressType": rlBrgStaticInetMulticastSourceAddressType,
       "rlBrgStaticInetMulticastSourceAddress": rlBrgStaticInetMulticastSourceAddress,
       "rlBrgStaticInetMulticastFrwPorts": rlBrgStaticInetMulticastFrwPorts,
       "rlBrgStaticInetMulticastForbiddenPorts": rlBrgStaticInetMulticastForbiddenPorts,
       "rlBrgStaticInetMulticastStatus": rlBrgStaticInetMulticastStatus,
       "rlBrgInetMulticastTable": rlBrgInetMulticastTable,
       "rlBrgInetMulticastEntry": rlBrgInetMulticastEntry,
       "rlBrgInetMulticastVlanTag": rlBrgInetMulticastVlanTag,
       "rlBrgInetMulticastGroupAddressType": rlBrgInetMulticastGroupAddressType,
       "rlBrgInetMulticastGroupAddress": rlBrgInetMulticastGroupAddress,
       "rlBrgInetMulticastSourceAddressType": rlBrgInetMulticastSourceAddressType,
       "rlBrgInetMulticastSourceAddress": rlBrgInetMulticastSourceAddress,
       "rlBrgInetMulticastEgressPorts": rlBrgInetMulticastEgressPorts,
       "rlBrgInetMulticastLearntPorts": rlBrgInetMulticastLearntPorts,
       "rlBrgIpmFdbRefTable": rlBrgIpmFdbRefTable,
       "rlBrgIpmFdbRefEntry": rlBrgIpmFdbRefEntry,
       "rlBrgIpmFdbRefVlanTag": rlBrgIpmFdbRefVlanTag,
       "rlBrgIpmFdbRefGroupAddressType": rlBrgIpmFdbRefGroupAddressType,
       "rlBrgIpmFdbRefGroupAddress": rlBrgIpmFdbRefGroupAddress,
       "rlBrgIpmFdbRefSourceAddressType": rlBrgIpmFdbRefSourceAddressType,
       "rlBrgIpmFdbRefSourceAddress": rlBrgIpmFdbRefSourceAddress,
       "rlBrgIpmFdbRefPorts": rlBrgIpmFdbRefPorts,
       "rlBrgDynamicCmdTable": rlBrgDynamicCmdTable,
       "rlBrgDynamicCmdEntry": rlBrgDynamicCmdEntry,
       "rlBrgDynamicCmdKey": rlBrgDynamicCmdKey,
       "rlBrgDynamicCmdVlanTag": rlBrgDynamicCmdVlanTag,
       "rlBrgDynamicCmdGroupAddressType": rlBrgDynamicCmdGroupAddressType,
       "rlBrgDynamicCmdGroupAddress": rlBrgDynamicCmdGroupAddress,
       "rlBrgDynamicCmdSourceAddressType": rlBrgDynamicCmdSourceAddressType,
       "rlBrgDynamicCmdSourceAddress": rlBrgDynamicCmdSourceAddress,
       "rlBrgDynamicCmdPorts": rlBrgDynamicCmdPorts,
       "rlBrgDynamicCmdType": rlBrgDynamicCmdType,
       "rlUserAssignedVidx": rlUserAssignedVidx,
       "rlUserAssignedVidxConfigTable": rlUserAssignedVidxConfigTable,
       "rlUserAssignedVidxConfigEntry": rlUserAssignedVidxConfigEntry,
       "rlUserAssignedVidxConfigIndex": rlUserAssignedVidxConfigIndex,
       "rlUserAssignedVidxConfigPorts": rlUserAssignedVidxConfigPorts,
       "rlUserAssignedVidxConfigRowStatus": rlUserAssignedVidxConfigRowStatus,
       "rlUserAssignedVidxGetNextFreeIndex": rlUserAssignedVidxGetNextFreeIndex,
       "rlBrgMulticastCurrentNumberOfEntries": rlBrgMulticastCurrentNumberOfEntries}
)
