# SNMP MIB module (CISCOSB-rlIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-rlIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:17 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

(IpAddressOriginTC,
 IpAddressStatusTC) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC",
    "IpAddressStatusTC")

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
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rlIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250)
)
rlIp.setRevisions(
        ("2013-06-16 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlIpAddressOriginTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 7),
          ("dhcp", 4),
          ("eui64", 8),
          ("generalPrefix", 11),
          ("linklayer", 5),
          ("manual", 2),
          ("other", 1),
          ("random", 6),
          ("tunnel6to4", 10),
          ("tunnelIsatap", 9))
    )



# MIB Managed Objects in the order of their OIDs

_RlIpAddressTable_Object = MibTable
rlIpAddressTable = _RlIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1)
)
if mibBuilder.loadTexts:
    rlIpAddressTable.setStatus("current")
_RlIpAddressEntry_Object = MibTableRow
rlIpAddressEntry = _RlIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1)
)
rlIpAddressEntry.setIndexNames(
    (0, "CISCOSB-rlIP-MIB", "rlIpAddressAddrType"),
    (0, "CISCOSB-rlIP-MIB", "rlIpAddressAddr"),
    (0, "CISCOSB-rlIP-MIB", "rlIpAddressOrigin"),
    (0, "CISCOSB-rlIP-MIB", "rlIpAddressGeneralPrefixName"),
)
if mibBuilder.loadTexts:
    rlIpAddressEntry.setStatus("current")
_RlIpAddressAddrType_Type = InetAddressType
_RlIpAddressAddrType_Object = MibTableColumn
rlIpAddressAddrType = _RlIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 1),
    _RlIpAddressAddrType_Type()
)
rlIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpAddressAddrType.setStatus("current")
_RlIpAddressAddr_Type = InetAddress
_RlIpAddressAddr_Object = MibTableColumn
rlIpAddressAddr = _RlIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 2),
    _RlIpAddressAddr_Type()
)
rlIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpAddressAddr.setStatus("current")
_RlIpAddressOrigin_Type = RlIpAddressOriginTC
_RlIpAddressOrigin_Object = MibTableColumn
rlIpAddressOrigin = _RlIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 3),
    _RlIpAddressOrigin_Type()
)
rlIpAddressOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpAddressOrigin.setStatus("current")
_RlIpAddressGeneralPrefixName_Type = DisplayString
_RlIpAddressGeneralPrefixName_Object = MibTableColumn
rlIpAddressGeneralPrefixName = _RlIpAddressGeneralPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 4),
    _RlIpAddressGeneralPrefixName_Type()
)
rlIpAddressGeneralPrefixName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpAddressGeneralPrefixName.setStatus("current")
_RlIpAddressIfIndex_Type = InterfaceIndex
_RlIpAddressIfIndex_Object = MibTableColumn
rlIpAddressIfIndex = _RlIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 5),
    _RlIpAddressIfIndex_Type()
)
rlIpAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressIfIndex.setStatus("current")


class _RlIpAddressExtdType_Type(Integer32):
    """Custom type rlIpAddressExtdType based on Integer32"""
    defaultValue = 1

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
        *(("anycast", 2),
          ("broadcast", 3),
          ("multicast", 4),
          ("unicast", 1))
    )


_RlIpAddressExtdType_Type.__name__ = "Integer32"
_RlIpAddressExtdType_Object = MibTableColumn
rlIpAddressExtdType = _RlIpAddressExtdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 6),
    _RlIpAddressExtdType_Type()
)
rlIpAddressExtdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressExtdType.setStatus("current")


class _RlIpAddressPrefix_Type(RowPointer):
    """Custom type rlIpAddressPrefix based on RowPointer"""
    defaultValue = (0, 0)


_RlIpAddressPrefix_Object = MibTableColumn
rlIpAddressPrefix = _RlIpAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 7),
    _RlIpAddressPrefix_Type()
)
rlIpAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddressPrefix.setStatus("current")


class _RlIpAddressStatus_Type(IpAddressStatusTC):
    """Custom type rlIpAddressStatus based on IpAddressStatusTC"""


_RlIpAddressStatus_Object = MibTableColumn
rlIpAddressStatus = _RlIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 8),
    _RlIpAddressStatus_Type()
)
rlIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressStatus.setStatus("current")
_RlIpAddressCreated_Type = TimeStamp
_RlIpAddressCreated_Object = MibTableColumn
rlIpAddressCreated = _RlIpAddressCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 9),
    _RlIpAddressCreated_Type()
)
rlIpAddressCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddressCreated.setStatus("current")
_RlIpAddressLastChanged_Type = TimeStamp
_RlIpAddressLastChanged_Object = MibTableColumn
rlIpAddressLastChanged = _RlIpAddressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 10),
    _RlIpAddressLastChanged_Type()
)
rlIpAddressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddressLastChanged.setStatus("current")
_RlIpAddressRowStatus_Type = RowStatus
_RlIpAddressRowStatus_Object = MibTableColumn
rlIpAddressRowStatus = _RlIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 11),
    _RlIpAddressRowStatus_Type()
)
rlIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressRowStatus.setStatus("current")


class _RlIpAddressStorageType_Type(StorageType):
    """Custom type rlIpAddressStorageType based on StorageType"""


_RlIpAddressStorageType_Object = MibTableColumn
rlIpAddressStorageType = _RlIpAddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 12),
    _RlIpAddressStorageType_Type()
)
rlIpAddressStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressStorageType.setStatus("current")


class _RlIpAddressExtdPrefixLength_Type(InetAddressPrefixLength):
    """Custom type rlIpAddressExtdPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 64


_RlIpAddressExtdPrefixLength_Object = MibTableColumn
rlIpAddressExtdPrefixLength = _RlIpAddressExtdPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 13),
    _RlIpAddressExtdPrefixLength_Type()
)
rlIpAddressExtdPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressExtdPrefixLength.setStatus("current")
_RlIpAddressCompleteAddr_Type = InetAddress
_RlIpAddressCompleteAddr_Object = MibTableColumn
rlIpAddressCompleteAddr = _RlIpAddressCompleteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 14),
    _RlIpAddressCompleteAddr_Type()
)
rlIpAddressCompleteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddressCompleteAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rlIP-MIB",
    **{"RlIpAddressOriginTC": RlIpAddressOriginTC,
       "rlIp": rlIp,
       "rlIpAddressTable": rlIpAddressTable,
       "rlIpAddressEntry": rlIpAddressEntry,
       "rlIpAddressAddrType": rlIpAddressAddrType,
       "rlIpAddressAddr": rlIpAddressAddr,
       "rlIpAddressOrigin": rlIpAddressOrigin,
       "rlIpAddressGeneralPrefixName": rlIpAddressGeneralPrefixName,
       "rlIpAddressIfIndex": rlIpAddressIfIndex,
       "rlIpAddressExtdType": rlIpAddressExtdType,
       "rlIpAddressPrefix": rlIpAddressPrefix,
       "rlIpAddressStatus": rlIpAddressStatus,
       "rlIpAddressCreated": rlIpAddressCreated,
       "rlIpAddressLastChanged": rlIpAddressLastChanged,
       "rlIpAddressRowStatus": rlIpAddressRowStatus,
       "rlIpAddressStorageType": rlIpAddressStorageType,
       "rlIpAddressExtdPrefixLength": rlIpAddressExtdPrefixLength,
       "rlIpAddressCompleteAddr": rlIpAddressCompleteAddr}
)
