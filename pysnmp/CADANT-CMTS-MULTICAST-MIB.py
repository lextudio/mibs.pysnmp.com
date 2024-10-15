# SNMP MIB module (CADANT-CMTS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:39 2024
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

(cadIfMacDomainIfIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadIfMacDomainIfIndex")

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

(mgmdPmStaticGroupAddressType,
 mgmdPmStaticGroupEntityType,
 mgmdPmStaticGroupIfIndex) = mibBuilder.importSymbols(
    "DC-MGMD-MIB",
    "mgmdPmStaticGroupAddressType",
    "mgmdPmStaticGroupEntityType",
    "mgmdPmStaticGroupIfIndex")

(ChSetId,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId")

(Dsid,
 dsgIfClassId,
 dsgIfTunnelGrpIndex,
 dsgIfTunnelIndex) = mibBuilder.importSymbols(
    "DSG-IF-MIB",
    "Dsid",
    "dsgIfClassId",
    "dsgIfTunnelGrpIndex",
    "dsgIfTunnelIndex")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadMcastStdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10)
)
cadMcastStdMib.setRevisions(
        ("2015-01-28 00:00",
         "2014-09-22 00:00",
         "2014-06-04 00:00",
         "2014-04-08 00:00",
         "2013-07-18 00:00",
         "2013-01-28 00:00",
         "2012-10-08 00:00",
         "2011-11-08 00:00",
         "2011-04-05 00:00",
         "2011-04-04 00:00",
         "2011-03-21 00:00",
         "2011-03-08 00:00",
         "2005-08-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadMcastStaticMacIpBindingTable_Object = MibTable
cadMcastStaticMacIpBindingTable = _CadMcastStaticMacIpBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1)
)
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingTable.setStatus("current")
_CadMcastStaticMacIpBindingEntry_Object = MibTableRow
cadMcastStaticMacIpBindingEntry = _CadMcastStaticMacIpBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1)
)
cadMcastStaticMacIpBindingEntry.setIndexNames(
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStaticMacIpBindingAddressType"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStaticMacIpBindingAddress"),
)
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingEntry.setStatus("current")
_CadMcastStaticMacIpBindingAddressType_Type = InetAddressType
_CadMcastStaticMacIpBindingAddressType_Object = MibTableColumn
cadMcastStaticMacIpBindingAddressType = _CadMcastStaticMacIpBindingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 1),
    _CadMcastStaticMacIpBindingAddressType_Type()
)
cadMcastStaticMacIpBindingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingAddressType.setStatus("current")
_CadMcastStaticMacIpBindingAddress_Type = InetAddress
_CadMcastStaticMacIpBindingAddress_Object = MibTableColumn
cadMcastStaticMacIpBindingAddress = _CadMcastStaticMacIpBindingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 2),
    _CadMcastStaticMacIpBindingAddress_Type()
)
cadMcastStaticMacIpBindingAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingAddress.setStatus("current")
_CadMcastStaticMacIpBindingMacAddress_Type = MacAddress
_CadMcastStaticMacIpBindingMacAddress_Object = MibTableColumn
cadMcastStaticMacIpBindingMacAddress = _CadMcastStaticMacIpBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 3),
    _CadMcastStaticMacIpBindingMacAddress_Type()
)
cadMcastStaticMacIpBindingMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingMacAddress.setStatus("current")
_CadMcastStaticMacIpBindingStatus_Type = RowStatus
_CadMcastStaticMacIpBindingStatus_Object = MibTableColumn
cadMcastStaticMacIpBindingStatus = _CadMcastStaticMacIpBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 1, 1, 4),
    _CadMcastStaticMacIpBindingStatus_Type()
)
cadMcastStaticMacIpBindingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMcastStaticMacIpBindingStatus.setStatus("current")
_CadMcastMrouteTable_Object = MibTable
cadMcastMrouteTable = _CadMcastMrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2)
)
if mibBuilder.loadTexts:
    cadMcastMrouteTable.setStatus("current")
_CadMcastMrouteEntry_Object = MibTableRow
cadMcastMrouteEntry = _CadMcastMrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1)
)
cadMcastMrouteEntry.setIndexNames(
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteType"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteSourceAddress"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastMrouteSourcePrefix"),
)
if mibBuilder.loadTexts:
    cadMcastMrouteEntry.setStatus("current")
_CadMcastMrouteType_Type = InetAddressType
_CadMcastMrouteType_Object = MibTableColumn
cadMcastMrouteType = _CadMcastMrouteType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 1),
    _CadMcastMrouteType_Type()
)
cadMcastMrouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastMrouteType.setStatus("current")
_CadMcastMrouteSourceAddress_Type = InetAddress
_CadMcastMrouteSourceAddress_Object = MibTableColumn
cadMcastMrouteSourceAddress = _CadMcastMrouteSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 2),
    _CadMcastMrouteSourceAddress_Type()
)
cadMcastMrouteSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastMrouteSourceAddress.setStatus("current")
_CadMcastMrouteSourcePrefix_Type = InetAddressPrefixLength
_CadMcastMrouteSourcePrefix_Object = MibTableColumn
cadMcastMrouteSourcePrefix = _CadMcastMrouteSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 3),
    _CadMcastMrouteSourcePrefix_Type()
)
cadMcastMrouteSourcePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastMrouteSourcePrefix.setStatus("current")
_CadMcastMrouteRpfAddress_Type = InetAddress
_CadMcastMrouteRpfAddress_Object = MibTableColumn
cadMcastMrouteRpfAddress = _CadMcastMrouteRpfAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 4),
    _CadMcastMrouteRpfAddress_Type()
)
cadMcastMrouteRpfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMcastMrouteRpfAddress.setStatus("current")


class _CadMcastMrouteDistance_Type(Integer32):
    """Custom type cadMcastMrouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadMcastMrouteDistance_Type.__name__ = "Integer32"
_CadMcastMrouteDistance_Object = MibTableColumn
cadMcastMrouteDistance = _CadMcastMrouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 5),
    _CadMcastMrouteDistance_Type()
)
cadMcastMrouteDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMcastMrouteDistance.setStatus("current")
_CadMcastMrouteStatus_Type = RowStatus
_CadMcastMrouteStatus_Object = MibTableColumn
cadMcastMrouteStatus = _CadMcastMrouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 2, 1, 6),
    _CadMcastMrouteStatus_Type()
)
cadMcastMrouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMcastMrouteStatus.setStatus("current")
_CadMcastForwardTable_Object = MibTable
cadMcastForwardTable = _CadMcastForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3)
)
if mibBuilder.loadTexts:
    cadMcastForwardTable.setStatus("current")
_CadMcastForwardEntry_Object = MibTableRow
cadMcastForwardEntry = _CadMcastForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1)
)
cadMcastForwardEntry.setIndexNames(
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardAddressType"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardGroupAddress"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardSourceAddress"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardSourceIf"),
)
if mibBuilder.loadTexts:
    cadMcastForwardEntry.setStatus("current")
_CadMcastForwardAddressType_Type = InetAddressType
_CadMcastForwardAddressType_Object = MibTableColumn
cadMcastForwardAddressType = _CadMcastForwardAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 1),
    _CadMcastForwardAddressType_Type()
)
cadMcastForwardAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastForwardAddressType.setStatus("current")
_CadMcastForwardGroupAddress_Type = InetAddress
_CadMcastForwardGroupAddress_Object = MibTableColumn
cadMcastForwardGroupAddress = _CadMcastForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 2),
    _CadMcastForwardGroupAddress_Type()
)
cadMcastForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastForwardGroupAddress.setStatus("current")
_CadMcastForwardSourceAddress_Type = InetAddress
_CadMcastForwardSourceAddress_Object = MibTableColumn
cadMcastForwardSourceAddress = _CadMcastForwardSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 3),
    _CadMcastForwardSourceAddress_Type()
)
cadMcastForwardSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastForwardSourceAddress.setStatus("current")
_CadMcastForwardSourceIf_Type = InterfaceIndexOrZero
_CadMcastForwardSourceIf_Object = MibTableColumn
cadMcastForwardSourceIf = _CadMcastForwardSourceIf_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 4),
    _CadMcastForwardSourceIf_Type()
)
cadMcastForwardSourceIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastForwardSourceIf.setStatus("current")
_CadMcastForwardDestIfList_Type = Unsigned32
_CadMcastForwardDestIfList_Object = MibTableColumn
cadMcastForwardDestIfList = _CadMcastForwardDestIfList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 5),
    _CadMcastForwardDestIfList_Type()
)
cadMcastForwardDestIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastForwardDestIfList.setStatus("current")
_CadMcastForwardCount_Type = Counter64
_CadMcastForwardCount_Object = MibTableColumn
cadMcastForwardCount = _CadMcastForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 3, 1, 6),
    _CadMcastForwardCount_Type()
)
cadMcastForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastForwardCount.setStatus("current")
_CadMcastForwardDestTable_Object = MibTable
cadMcastForwardDestTable = _CadMcastForwardDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4)
)
if mibBuilder.loadTexts:
    cadMcastForwardDestTable.setStatus("current")
_CadMcastForwardDestEntry_Object = MibTableRow
cadMcastForwardDestEntry = _CadMcastForwardDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1)
)
cadMcastForwardDestEntry.setIndexNames(
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIfListId"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIfType"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastForwardDestIf"),
)
if mibBuilder.loadTexts:
    cadMcastForwardDestEntry.setStatus("current")
_CadMcastForwardDestIfListId_Type = Unsigned32
_CadMcastForwardDestIfListId_Object = MibTableColumn
cadMcastForwardDestIfListId = _CadMcastForwardDestIfListId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 1),
    _CadMcastForwardDestIfListId_Type()
)
cadMcastForwardDestIfListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastForwardDestIfListId.setStatus("current")
_CadMcastForwardDestIf_Type = Unsigned32
_CadMcastForwardDestIf_Object = MibTableColumn
cadMcastForwardDestIf = _CadMcastForwardDestIf_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 2),
    _CadMcastForwardDestIf_Type()
)
cadMcastForwardDestIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastForwardDestIf.setStatus("current")


class _CadMcastForwardDestIfType_Type(Integer32):
    """Custom type cadMcastForwardDestIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis", 1),
          ("sdv", 2))
    )


_CadMcastForwardDestIfType_Type.__name__ = "Integer32"
_CadMcastForwardDestIfType_Object = MibTableColumn
cadMcastForwardDestIfType = _CadMcastForwardDestIfType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 4, 1, 3),
    _CadMcastForwardDestIfType_Type()
)
cadMcastForwardDestIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastForwardDestIfType.setStatus("current")
_CadMcastGlobals_ObjectIdentity = ObjectIdentity
cadMcastGlobals = _CadMcastGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5)
)


class _CadMcastClearForwardCounts_Type(TruthValue):
    """Custom type cadMcastClearForwardCounts based on TruthValue"""


_CadMcastClearForwardCounts_Object = MibScalar
cadMcastClearForwardCounts = _CadMcastClearForwardCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 1),
    _CadMcastClearForwardCounts_Type()
)
cadMcastClearForwardCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastClearForwardCounts.setStatus("current")


class _CadMcastForwardUseDefaultFlow_Type(TruthValue):
    """Custom type cadMcastForwardUseDefaultFlow based on TruthValue"""


_CadMcastForwardUseDefaultFlow_Object = MibScalar
cadMcastForwardUseDefaultFlow = _CadMcastForwardUseDefaultFlow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 2),
    _CadMcastForwardUseDefaultFlow_Type()
)
cadMcastForwardUseDefaultFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastForwardUseDefaultFlow.setStatus("current")


class _CadMcastDeleteDsg_Type(TruthValue):
    """Custom type cadMcastDeleteDsg based on TruthValue"""


_CadMcastDeleteDsg_Object = MibScalar
cadMcastDeleteDsg = _CadMcastDeleteDsg_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 3),
    _CadMcastDeleteDsg_Type()
)
cadMcastDeleteDsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastDeleteDsg.setStatus("current")


class _CadMcastIgmpThrottleEnable_Type(TruthValue):
    """Custom type cadMcastIgmpThrottleEnable based on TruthValue"""


_CadMcastIgmpThrottleEnable_Object = MibScalar
cadMcastIgmpThrottleEnable = _CadMcastIgmpThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 4),
    _CadMcastIgmpThrottleEnable_Type()
)
cadMcastIgmpThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastIgmpThrottleEnable.setStatus("current")


class _CadMcastIgmpThrottleBurstSize_Type(Unsigned32):
    """Custom type cadMcastIgmpThrottleBurstSize based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_CadMcastIgmpThrottleBurstSize_Type.__name__ = "Unsigned32"
_CadMcastIgmpThrottleBurstSize_Object = MibScalar
cadMcastIgmpThrottleBurstSize = _CadMcastIgmpThrottleBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 5),
    _CadMcastIgmpThrottleBurstSize_Type()
)
cadMcastIgmpThrottleBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastIgmpThrottleBurstSize.setStatus("current")


class _CadMcastIgmpThrottleInterval_Type(Unsigned32):
    """Custom type cadMcastIgmpThrottleInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CadMcastIgmpThrottleInterval_Type.__name__ = "Unsigned32"
_CadMcastIgmpThrottleInterval_Object = MibScalar
cadMcastIgmpThrottleInterval = _CadMcastIgmpThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 6),
    _CadMcastIgmpThrottleInterval_Type()
)
cadMcastIgmpThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastIgmpThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadMcastIgmpThrottleInterval.setUnits("seconds")


class _CadMcastIgmpThrottleIncrement_Type(Unsigned32):
    """Custom type cadMcastIgmpThrottleIncrement based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CadMcastIgmpThrottleIncrement_Type.__name__ = "Unsigned32"
_CadMcastIgmpThrottleIncrement_Object = MibScalar
cadMcastIgmpThrottleIncrement = _CadMcastIgmpThrottleIncrement_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 7),
    _CadMcastIgmpThrottleIncrement_Type()
)
cadMcastIgmpThrottleIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastIgmpThrottleIncrement.setStatus("current")


class _CadMcastClearVideoForwardCounts_Type(TruthValue):
    """Custom type cadMcastClearVideoForwardCounts based on TruthValue"""


_CadMcastClearVideoForwardCounts_Object = MibScalar
cadMcastClearVideoForwardCounts = _CadMcastClearVideoForwardCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 5, 8),
    _CadMcastClearVideoForwardCounts_Type()
)
cadMcastClearVideoForwardCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadMcastClearVideoForwardCounts.setStatus("current")
_CadFqdnCfgGroup_ObjectIdentity = ObjectIdentity
cadFqdnCfgGroup = _CadFqdnCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6)
)


class _CadFqdnCacheEnable_Type(TruthValue):
    """Custom type cadFqdnCacheEnable based on TruthValue"""


_CadFqdnCacheEnable_Object = MibScalar
cadFqdnCacheEnable = _CadFqdnCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 1),
    _CadFqdnCacheEnable_Type()
)
cadFqdnCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadFqdnCacheEnable.setStatus("current")


class _CadFqdnCachePollInterval_Type(Unsigned32):
    """Custom type cadFqdnCachePollInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_CadFqdnCachePollInterval_Type.__name__ = "Unsigned32"
_CadFqdnCachePollInterval_Object = MibScalar
cadFqdnCachePollInterval = _CadFqdnCachePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 2),
    _CadFqdnCachePollInterval_Type()
)
cadFqdnCachePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadFqdnCachePollInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadFqdnCachePollInterval.setUnits("seconds")


class _CadFqdnCacheRefresh_Type(TruthValue):
    """Custom type cadFqdnCacheRefresh based on TruthValue"""


_CadFqdnCacheRefresh_Object = MibScalar
cadFqdnCacheRefresh = _CadFqdnCacheRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 6, 3),
    _CadFqdnCacheRefresh_Type()
)
cadFqdnCacheRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadFqdnCacheRefresh.setStatus("current")
_CadFqdnCacheTable_Object = MibTable
cadFqdnCacheTable = _CadFqdnCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7)
)
if mibBuilder.loadTexts:
    cadFqdnCacheTable.setStatus("current")
_CadFqdnCacheEntry_Object = MibTableRow
cadFqdnCacheEntry = _CadFqdnCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1)
)
cadFqdnCacheEntry.setIndexNames(
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadFqdnCacheName"),
)
if mibBuilder.loadTexts:
    cadFqdnCacheEntry.setStatus("current")


class _CadFqdnCacheName_Type(SnmpAdminString):
    """Custom type cadFqdnCacheName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 154),
    )


_CadFqdnCacheName_Type.__name__ = "SnmpAdminString"
_CadFqdnCacheName_Object = MibTableColumn
cadFqdnCacheName = _CadFqdnCacheName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 1),
    _CadFqdnCacheName_Type()
)
cadFqdnCacheName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadFqdnCacheName.setStatus("current")


class _CadFqdnCacheFqdn_Type(SnmpAdminString):
    """Custom type cadFqdnCacheFqdn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CadFqdnCacheFqdn_Type.__name__ = "SnmpAdminString"
_CadFqdnCacheFqdn_Object = MibTableColumn
cadFqdnCacheFqdn = _CadFqdnCacheFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 2),
    _CadFqdnCacheFqdn_Type()
)
cadFqdnCacheFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFqdnCacheFqdn.setStatus("current")


class _CadFqdnCacheIpAddrType_Type(InetAddressType):
    """Custom type cadFqdnCacheIpAddrType based on InetAddressType"""


_CadFqdnCacheIpAddrType_Object = MibTableColumn
cadFqdnCacheIpAddrType = _CadFqdnCacheIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 3),
    _CadFqdnCacheIpAddrType_Type()
)
cadFqdnCacheIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFqdnCacheIpAddrType.setStatus("current")


class _CadFqdnCacheIpAddress_Type(InetAddress):
    """Custom type cadFqdnCacheIpAddress based on InetAddress"""
    defaultHexValue = ""


_CadFqdnCacheIpAddress_Object = MibTableColumn
cadFqdnCacheIpAddress = _CadFqdnCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 4),
    _CadFqdnCacheIpAddress_Type()
)
cadFqdnCacheIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFqdnCacheIpAddress.setStatus("current")
_CadFqdnCacheLastUpdateTime_Type = TimeTicks
_CadFqdnCacheLastUpdateTime_Object = MibTableColumn
cadFqdnCacheLastUpdateTime = _CadFqdnCacheLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 5),
    _CadFqdnCacheLastUpdateTime_Type()
)
cadFqdnCacheLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFqdnCacheLastUpdateTime.setStatus("current")


class _CadFqdnCacheStatus_Type(Integer32):
    """Custom type cadFqdnCacheStatus based on Integer32"""
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
        *(("genError", 5),
          ("invalidIp", 3),
          ("timeout", 4),
          ("unknownIp", 2),
          ("validIp", 1))
    )


_CadFqdnCacheStatus_Type.__name__ = "Integer32"
_CadFqdnCacheStatus_Object = MibTableColumn
cadFqdnCacheStatus = _CadFqdnCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 7, 1, 6),
    _CadFqdnCacheStatus_Type()
)
cadFqdnCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFqdnCacheStatus.setStatus("current")
_CadDsgIfClassifierCfgTable_Object = MibTable
cadDsgIfClassifierCfgTable = _CadDsgIfClassifierCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8)
)
if mibBuilder.loadTexts:
    cadDsgIfClassifierCfgTable.setStatus("current")
_CadDsgIfClassifierCfgEntry_Object = MibTableRow
cadDsgIfClassifierCfgEntry = _CadDsgIfClassifierCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1)
)
cadDsgIfClassifierCfgEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTunnelIndex"),
    (0, "DSG-IF-MIB", "dsgIfClassId"),
)
if mibBuilder.loadTexts:
    cadDsgIfClassifierCfgEntry.setStatus("current")


class _CadDsgIfSrcName_Type(SnmpAdminString):
    """Custom type cadDsgIfSrcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 154),
    )


_CadDsgIfSrcName_Type.__name__ = "SnmpAdminString"
_CadDsgIfSrcName_Object = MibTableColumn
cadDsgIfSrcName = _CadDsgIfSrcName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1, 1),
    _CadDsgIfSrcName_Type()
)
cadDsgIfSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsgIfSrcName.setStatus("current")
_CadDsgIfClassifierCfgRowStatus_Type = RowStatus
_CadDsgIfClassifierCfgRowStatus_Object = MibTableColumn
cadDsgIfClassifierCfgRowStatus = _CadDsgIfClassifierCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 8, 1, 2),
    _CadDsgIfClassifierCfgRowStatus_Type()
)
cadDsgIfClassifierCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDsgIfClassifierCfgRowStatus.setStatus("current")
_CadMgmdPmStaticGroupCfgTable_Object = MibTable
cadMgmdPmStaticGroupCfgTable = _CadMgmdPmStaticGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9)
)
if mibBuilder.loadTexts:
    cadMgmdPmStaticGroupCfgTable.setStatus("current")
_CadMgmdPmStaticGroupCfgEntry_Object = MibTableRow
cadMgmdPmStaticGroupCfgEntry = _CadMgmdPmStaticGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1)
)
cadMgmdPmStaticGroupCfgEntry.setIndexNames(
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupEntityType"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupIfIndex"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddressType"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMgmdPmStaticGroupAddress"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMgmdPmStaticGroupSourceName"),
)
if mibBuilder.loadTexts:
    cadMgmdPmStaticGroupCfgEntry.setStatus("current")
_CadMgmdPmStaticGroupAddress_Type = InetAddress
_CadMgmdPmStaticGroupAddress_Object = MibTableColumn
cadMgmdPmStaticGroupAddress = _CadMgmdPmStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 1),
    _CadMgmdPmStaticGroupAddress_Type()
)
cadMgmdPmStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMgmdPmStaticGroupAddress.setStatus("current")


class _CadMgmdPmStaticGroupSourceName_Type(SnmpAdminString):
    """Custom type cadMgmdPmStaticGroupSourceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 154),
    )


_CadMgmdPmStaticGroupSourceName_Type.__name__ = "SnmpAdminString"
_CadMgmdPmStaticGroupSourceName_Object = MibTableColumn
cadMgmdPmStaticGroupSourceName = _CadMgmdPmStaticGroupSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 2),
    _CadMgmdPmStaticGroupSourceName_Type()
)
cadMgmdPmStaticGroupSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMgmdPmStaticGroupSourceName.setStatus("current")
_CadMgmdPmStaticGroupCfgRowStatus_Type = RowStatus
_CadMgmdPmStaticGroupCfgRowStatus_Object = MibTableColumn
cadMgmdPmStaticGroupCfgRowStatus = _CadMgmdPmStaticGroupCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 9, 1, 3),
    _CadMgmdPmStaticGroupCfgRowStatus_Type()
)
cadMgmdPmStaticGroupCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMgmdPmStaticGroupCfgRowStatus.setStatus("current")
_CadMcastStatsTable_Object = MibTable
cadMcastStatsTable = _CadMcastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10)
)
if mibBuilder.loadTexts:
    cadMcastStatsTable.setStatus("current")
_CadMcastStatsEntry_Object = MibTableRow
cadMcastStatsEntry = _CadMcastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1)
)
cadMcastStatsEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadMcastStatsDsid"),
)
if mibBuilder.loadTexts:
    cadMcastStatsEntry.setStatus("current")
_CadMcastStatsDsid_Type = Dsid
_CadMcastStatsDsid_Object = MibTableColumn
cadMcastStatsDsid = _CadMcastStatsDsid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 1),
    _CadMcastStatsDsid_Type()
)
cadMcastStatsDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMcastStatsDsid.setStatus("current")
_CadMcastStatsSentPkts_Type = Counter64
_CadMcastStatsSentPkts_Object = MibTableColumn
cadMcastStatsSentPkts = _CadMcastStatsSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 2),
    _CadMcastStatsSentPkts_Type()
)
cadMcastStatsSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsSentPkts.setStatus("current")
if mibBuilder.loadTexts:
    cadMcastStatsSentPkts.setUnits("packets")
_CadMcastStatsSentOctets_Type = Counter64
_CadMcastStatsSentOctets_Object = MibTableColumn
cadMcastStatsSentOctets = _CadMcastStatsSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 3),
    _CadMcastStatsSentOctets_Type()
)
cadMcastStatsSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    cadMcastStatsSentOctets.setUnits("bytes")
_CadMcastStatsDroppedPkts_Type = Counter64
_CadMcastStatsDroppedPkts_Object = MibTableColumn
cadMcastStatsDroppedPkts = _CadMcastStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 4),
    _CadMcastStatsDroppedPkts_Type()
)
cadMcastStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cadMcastStatsDroppedPkts.setUnits("packets")
_CadMcastStatsDroppedOctets_Type = Counter64
_CadMcastStatsDroppedOctets_Object = MibTableColumn
cadMcastStatsDroppedOctets = _CadMcastStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 5),
    _CadMcastStatsDroppedOctets_Type()
)
cadMcastStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsDroppedOctets.setStatus("current")
if mibBuilder.loadTexts:
    cadMcastStatsDroppedOctets.setUnits("bytes")
_CadMcastStatsDsIfIndex_Type = InterfaceIndexOrZero
_CadMcastStatsDsIfIndex_Object = MibTableColumn
cadMcastStatsDsIfIndex = _CadMcastStatsDsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 6),
    _CadMcastStatsDsIfIndex_Type()
)
cadMcastStatsDsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsDsIfIndex.setStatus("current")
_CadMcastStatsTunnelIndex_Type = Unsigned32
_CadMcastStatsTunnelIndex_Object = MibTableColumn
cadMcastStatsTunnelIndex = _CadMcastStatsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 7),
    _CadMcastStatsTunnelIndex_Type()
)
cadMcastStatsTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsTunnelIndex.setStatus("current")
_CadMcastStatsDsChSetId_Type = ChSetId
_CadMcastStatsDsChSetId_Object = MibTableColumn
cadMcastStatsDsChSetId = _CadMcastStatsDsChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 8),
    _CadMcastStatsDsChSetId_Type()
)
cadMcastStatsDsChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsDsChSetId.setStatus("current")


class _CadMcastStatsGSFID_Type(Unsigned32):
    """Custom type cadMcastStatsGSFID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadMcastStatsGSFID_Type.__name__ = "Unsigned32"
_CadMcastStatsGSFID_Object = MibTableColumn
cadMcastStatsGSFID = _CadMcastStatsGSFID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 10, 1, 9),
    _CadMcastStatsGSFID_Type()
)
cadMcastStatsGSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMcastStatsGSFID.setStatus("current")
_CadDsgIfTunnelChToGroupTable_Object = MibTable
cadDsgIfTunnelChToGroupTable = _CadDsgIfTunnelChToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11)
)
if mibBuilder.loadTexts:
    cadDsgIfTunnelChToGroupTable.setStatus("current")
_CadDsgIfTunnelChToGroupEntry_Object = MibTableRow
cadDsgIfTunnelChToGroupEntry = _CadDsgIfTunnelChToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11, 1)
)
cadDsgIfTunnelChToGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-CMTS-MULTICAST-MIB", "cadDsgIfTunnelGrpIndex"),
)
if mibBuilder.loadTexts:
    cadDsgIfTunnelChToGroupEntry.setStatus("current")
_CadDsgIfTunnelGrpIndex_Type = Unsigned32
_CadDsgIfTunnelGrpIndex_Object = MibTableColumn
cadDsgIfTunnelGrpIndex = _CadDsgIfTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 10, 11, 1, 1),
    _CadDsgIfTunnelGrpIndex_Type()
)
cadDsgIfTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDsgIfTunnelGrpIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-MULTICAST-MIB",
    **{"cadMcastStdMib": cadMcastStdMib,
       "cadMcastStaticMacIpBindingTable": cadMcastStaticMacIpBindingTable,
       "cadMcastStaticMacIpBindingEntry": cadMcastStaticMacIpBindingEntry,
       "cadMcastStaticMacIpBindingAddressType": cadMcastStaticMacIpBindingAddressType,
       "cadMcastStaticMacIpBindingAddress": cadMcastStaticMacIpBindingAddress,
       "cadMcastStaticMacIpBindingMacAddress": cadMcastStaticMacIpBindingMacAddress,
       "cadMcastStaticMacIpBindingStatus": cadMcastStaticMacIpBindingStatus,
       "cadMcastMrouteTable": cadMcastMrouteTable,
       "cadMcastMrouteEntry": cadMcastMrouteEntry,
       "cadMcastMrouteType": cadMcastMrouteType,
       "cadMcastMrouteSourceAddress": cadMcastMrouteSourceAddress,
       "cadMcastMrouteSourcePrefix": cadMcastMrouteSourcePrefix,
       "cadMcastMrouteRpfAddress": cadMcastMrouteRpfAddress,
       "cadMcastMrouteDistance": cadMcastMrouteDistance,
       "cadMcastMrouteStatus": cadMcastMrouteStatus,
       "cadMcastForwardTable": cadMcastForwardTable,
       "cadMcastForwardEntry": cadMcastForwardEntry,
       "cadMcastForwardAddressType": cadMcastForwardAddressType,
       "cadMcastForwardGroupAddress": cadMcastForwardGroupAddress,
       "cadMcastForwardSourceAddress": cadMcastForwardSourceAddress,
       "cadMcastForwardSourceIf": cadMcastForwardSourceIf,
       "cadMcastForwardDestIfList": cadMcastForwardDestIfList,
       "cadMcastForwardCount": cadMcastForwardCount,
       "cadMcastForwardDestTable": cadMcastForwardDestTable,
       "cadMcastForwardDestEntry": cadMcastForwardDestEntry,
       "cadMcastForwardDestIfListId": cadMcastForwardDestIfListId,
       "cadMcastForwardDestIf": cadMcastForwardDestIf,
       "cadMcastForwardDestIfType": cadMcastForwardDestIfType,
       "cadMcastGlobals": cadMcastGlobals,
       "cadMcastClearForwardCounts": cadMcastClearForwardCounts,
       "cadMcastForwardUseDefaultFlow": cadMcastForwardUseDefaultFlow,
       "cadMcastDeleteDsg": cadMcastDeleteDsg,
       "cadMcastIgmpThrottleEnable": cadMcastIgmpThrottleEnable,
       "cadMcastIgmpThrottleBurstSize": cadMcastIgmpThrottleBurstSize,
       "cadMcastIgmpThrottleInterval": cadMcastIgmpThrottleInterval,
       "cadMcastIgmpThrottleIncrement": cadMcastIgmpThrottleIncrement,
       "cadMcastClearVideoForwardCounts": cadMcastClearVideoForwardCounts,
       "cadFqdnCfgGroup": cadFqdnCfgGroup,
       "cadFqdnCacheEnable": cadFqdnCacheEnable,
       "cadFqdnCachePollInterval": cadFqdnCachePollInterval,
       "cadFqdnCacheRefresh": cadFqdnCacheRefresh,
       "cadFqdnCacheTable": cadFqdnCacheTable,
       "cadFqdnCacheEntry": cadFqdnCacheEntry,
       "cadFqdnCacheName": cadFqdnCacheName,
       "cadFqdnCacheFqdn": cadFqdnCacheFqdn,
       "cadFqdnCacheIpAddrType": cadFqdnCacheIpAddrType,
       "cadFqdnCacheIpAddress": cadFqdnCacheIpAddress,
       "cadFqdnCacheLastUpdateTime": cadFqdnCacheLastUpdateTime,
       "cadFqdnCacheStatus": cadFqdnCacheStatus,
       "cadDsgIfClassifierCfgTable": cadDsgIfClassifierCfgTable,
       "cadDsgIfClassifierCfgEntry": cadDsgIfClassifierCfgEntry,
       "cadDsgIfSrcName": cadDsgIfSrcName,
       "cadDsgIfClassifierCfgRowStatus": cadDsgIfClassifierCfgRowStatus,
       "cadMgmdPmStaticGroupCfgTable": cadMgmdPmStaticGroupCfgTable,
       "cadMgmdPmStaticGroupCfgEntry": cadMgmdPmStaticGroupCfgEntry,
       "cadMgmdPmStaticGroupAddress": cadMgmdPmStaticGroupAddress,
       "cadMgmdPmStaticGroupSourceName": cadMgmdPmStaticGroupSourceName,
       "cadMgmdPmStaticGroupCfgRowStatus": cadMgmdPmStaticGroupCfgRowStatus,
       "cadMcastStatsTable": cadMcastStatsTable,
       "cadMcastStatsEntry": cadMcastStatsEntry,
       "cadMcastStatsDsid": cadMcastStatsDsid,
       "cadMcastStatsSentPkts": cadMcastStatsSentPkts,
       "cadMcastStatsSentOctets": cadMcastStatsSentOctets,
       "cadMcastStatsDroppedPkts": cadMcastStatsDroppedPkts,
       "cadMcastStatsDroppedOctets": cadMcastStatsDroppedOctets,
       "cadMcastStatsDsIfIndex": cadMcastStatsDsIfIndex,
       "cadMcastStatsTunnelIndex": cadMcastStatsTunnelIndex,
       "cadMcastStatsDsChSetId": cadMcastStatsDsChSetId,
       "cadMcastStatsGSFID": cadMcastStatsGSFID,
       "cadDsgIfTunnelChToGroupTable": cadDsgIfTunnelChToGroupTable,
       "cadDsgIfTunnelChToGroupEntry": cadDsgIfTunnelChToGroupEntry,
       "cadDsgIfTunnelGrpIndex": cadDsgIfTunnelGrpIndex}
)
