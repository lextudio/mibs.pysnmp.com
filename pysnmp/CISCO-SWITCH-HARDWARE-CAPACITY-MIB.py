# SNMP MIB module (CISCO-SWITCH-HARDWARE-CAPACITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-HARDWARE-CAPACITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:09 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoInterfaceIndexList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInterfaceIndexList")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchHardwareCapacityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663)
)
ciscoSwitchHardwareCapacityMIB.setRevisions(
        ("2014-09-16 00:00",
         "2014-01-24 00:00",
         "2013-05-08 00:00",
         "2010-11-22 00:00",
         "2008-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CshcInternalChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eobc", 1),
          ("ibc", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchHardwareCapacityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchHardwareCapacityMIBNotifs = _CiscoSwitchHardwareCapacityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 0)
)
_CiscoSwitchHardwareCapacityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchHardwareCapacityMIBObjects = _CiscoSwitchHardwareCapacityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1)
)
_CshcForwarding_ObjectIdentity = ObjectIdentity
cshcForwarding = _CshcForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1)
)
_CshcL2Forwarding_ObjectIdentity = ObjectIdentity
cshcL2Forwarding = _CshcL2Forwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1)
)
_CshcMacUsageTable_Object = MibTable
cshcMacUsageTable = _CshcMacUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cshcMacUsageTable.setStatus("current")
_CshcMacUsageEntry_Object = MibTableRow
cshcMacUsageEntry = _CshcMacUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1)
)
cshcMacUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcMacUsageEntry.setStatus("current")
_CshcMacCollisions_Type = Counter32
_CshcMacCollisions_Object = MibTableColumn
cshcMacCollisions = _CshcMacCollisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 1),
    _CshcMacCollisions_Type()
)
cshcMacCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacCollisions.setStatus("current")
_CshcMacUsed_Type = Unsigned32
_CshcMacUsed_Object = MibTableColumn
cshcMacUsed = _CshcMacUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 2),
    _CshcMacUsed_Type()
)
cshcMacUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacUsed.setStatus("current")
_CshcMacTotal_Type = Unsigned32
_CshcMacTotal_Object = MibTableColumn
cshcMacTotal = _CshcMacTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 3),
    _CshcMacTotal_Type()
)
cshcMacTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacTotal.setStatus("current")
_CshcMacMcast_Type = Unsigned32
_CshcMacMcast_Object = MibTableColumn
cshcMacMcast = _CshcMacMcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 4),
    _CshcMacMcast_Type()
)
cshcMacMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacMcast.setStatus("current")
_CshcMacUcast_Type = Unsigned32
_CshcMacUcast_Object = MibTableColumn
cshcMacUcast = _CshcMacUcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 5),
    _CshcMacUcast_Type()
)
cshcMacUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacUcast.setStatus("current")
_CshcMacLines_Type = Unsigned32
_CshcMacLines_Object = MibTableColumn
cshcMacLines = _CshcMacLines_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 6),
    _CshcMacLines_Type()
)
cshcMacLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacLines.setStatus("current")
_CshcMacLinesFull_Type = Unsigned32
_CshcMacLinesFull_Object = MibTableColumn
cshcMacLinesFull = _CshcMacLinesFull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 1, 1, 7),
    _CshcMacLinesFull_Type()
)
cshcMacLinesFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMacLinesFull.setStatus("current")
_CshcVpnCamUsageTable_Object = MibTable
cshcVpnCamUsageTable = _CshcVpnCamUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cshcVpnCamUsageTable.setStatus("current")
_CshcVpnCamUsageEntry_Object = MibTableRow
cshcVpnCamUsageEntry = _CshcVpnCamUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 2, 1)
)
cshcVpnCamUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcVpnCamUsageEntry.setStatus("current")
_CshcVpnCamUsed_Type = Unsigned32
_CshcVpnCamUsed_Object = MibTableColumn
cshcVpnCamUsed = _CshcVpnCamUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 2, 1, 1),
    _CshcVpnCamUsed_Type()
)
cshcVpnCamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcVpnCamUsed.setStatus("current")
_CshcVpnCamTotal_Type = Unsigned32
_CshcVpnCamTotal_Object = MibTableColumn
cshcVpnCamTotal = _CshcVpnCamTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 1, 2, 1, 2),
    _CshcVpnCamTotal_Type()
)
cshcVpnCamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcVpnCamTotal.setStatus("current")
_CshcL3Forwarding_ObjectIdentity = ObjectIdentity
cshcL3Forwarding = _CshcL3Forwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2)
)
_CshcFibTcamUsageTable_Object = MibTable
cshcFibTcamUsageTable = _CshcFibTcamUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cshcFibTcamUsageTable.setStatus("current")
_CshcFibTcamUsageEntry_Object = MibTableRow
cshcFibTcamUsageEntry = _CshcFibTcamUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1)
)
cshcFibTcamUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcFibTcamUsageEntry.setStatus("current")
_Cshc72bitsFibTcamUsed_Type = Unsigned32
_Cshc72bitsFibTcamUsed_Object = MibTableColumn
cshc72bitsFibTcamUsed = _Cshc72bitsFibTcamUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 1),
    _Cshc72bitsFibTcamUsed_Type()
)
cshc72bitsFibTcamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc72bitsFibTcamUsed.setStatus("current")
_Cshc72bitsFibTcamTotal_Type = Unsigned32
_Cshc72bitsFibTcamTotal_Object = MibTableColumn
cshc72bitsFibTcamTotal = _Cshc72bitsFibTcamTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 2),
    _Cshc72bitsFibTcamTotal_Type()
)
cshc72bitsFibTcamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc72bitsFibTcamTotal.setStatus("current")
_Cshc144bitsFibTcamUsed_Type = Unsigned32
_Cshc144bitsFibTcamUsed_Object = MibTableColumn
cshc144bitsFibTcamUsed = _Cshc144bitsFibTcamUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 3),
    _Cshc144bitsFibTcamUsed_Type()
)
cshc144bitsFibTcamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc144bitsFibTcamUsed.setStatus("current")
_Cshc144bitsFibTcamTotal_Type = Unsigned32
_Cshc144bitsFibTcamTotal_Object = MibTableColumn
cshc144bitsFibTcamTotal = _Cshc144bitsFibTcamTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 4),
    _Cshc144bitsFibTcamTotal_Type()
)
cshc144bitsFibTcamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc144bitsFibTcamTotal.setStatus("current")
_Cshc288bitsFibTcamUsed_Type = Unsigned32
_Cshc288bitsFibTcamUsed_Object = MibTableColumn
cshc288bitsFibTcamUsed = _Cshc288bitsFibTcamUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 5),
    _Cshc288bitsFibTcamUsed_Type()
)
cshc288bitsFibTcamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc288bitsFibTcamUsed.setStatus("current")
_Cshc288bitsFibTcamTotal_Type = Unsigned32
_Cshc288bitsFibTcamTotal_Object = MibTableColumn
cshc288bitsFibTcamTotal = _Cshc288bitsFibTcamTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 1, 1, 6),
    _Cshc288bitsFibTcamTotal_Type()
)
cshc288bitsFibTcamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshc288bitsFibTcamTotal.setStatus("current")
_CshcProtocolFibTcamUsageTable_Object = MibTable
cshcProtocolFibTcamUsageTable = _CshcProtocolFibTcamUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cshcProtocolFibTcamUsageTable.setStatus("current")
_CshcProtocolFibTcamUsageEntry_Object = MibTableRow
cshcProtocolFibTcamUsageEntry = _CshcProtocolFibTcamUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1)
)
cshcProtocolFibTcamUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamProtocol"),
)
if mibBuilder.loadTexts:
    cshcProtocolFibTcamUsageEntry.setStatus("current")


class _CshcProtocolFibTcamProtocol_Type(Integer32):
    """Custom type cshcProtocolFibTcamProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("allProtocols", 14),
          ("eom", 3),
          ("fcMpls", 12),
          ("fcoe", 10),
          ("ipv4", 1),
          ("ipv4Multicast", 5),
          ("ipv6", 4),
          ("ipv6LocalLink", 13),
          ("ipv6Multicast", 6),
          ("l2VpnIpv4Multicast", 8),
          ("l2VpnIpv6Multicast", 9),
          ("l2VpnPeer", 7),
          ("mpls", 2),
          ("mplsVpn", 11))
    )


_CshcProtocolFibTcamProtocol_Type.__name__ = "Integer32"
_CshcProtocolFibTcamProtocol_Object = MibTableColumn
cshcProtocolFibTcamProtocol = _CshcProtocolFibTcamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 1),
    _CshcProtocolFibTcamProtocol_Type()
)
cshcProtocolFibTcamProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamProtocol.setStatus("current")
_CshcProtocolFibTcamUsed_Type = Unsigned32
_CshcProtocolFibTcamUsed_Object = MibTableColumn
cshcProtocolFibTcamUsed = _CshcProtocolFibTcamUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 2),
    _CshcProtocolFibTcamUsed_Type()
)
cshcProtocolFibTcamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamUsed.setStatus("current")
_CshcProtocolFibTcamTotal_Type = Unsigned32
_CshcProtocolFibTcamTotal_Object = MibTableColumn
cshcProtocolFibTcamTotal = _CshcProtocolFibTcamTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 3),
    _CshcProtocolFibTcamTotal_Type()
)
cshcProtocolFibTcamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamTotal.setStatus("current")
_CshcProtocolFibTcamLogicalUsed_Type = Unsigned32
_CshcProtocolFibTcamLogicalUsed_Object = MibTableColumn
cshcProtocolFibTcamLogicalUsed = _CshcProtocolFibTcamLogicalUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 4),
    _CshcProtocolFibTcamLogicalUsed_Type()
)
cshcProtocolFibTcamLogicalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamLogicalUsed.setStatus("current")
_CshcProtocolFibTcamLogicalTotal_Type = Unsigned32
_CshcProtocolFibTcamLogicalTotal_Object = MibTableColumn
cshcProtocolFibTcamLogicalTotal = _CshcProtocolFibTcamLogicalTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 5),
    _CshcProtocolFibTcamLogicalTotal_Type()
)
cshcProtocolFibTcamLogicalTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamLogicalTotal.setStatus("current")


class _CshcProtocolFibTcamWidthType_Type(Integer32):
    """Custom type cshcProtocolFibTcamWidthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doubleWidth", 2),
          ("quadWidth", 3),
          ("singleWidth", 1))
    )


_CshcProtocolFibTcamWidthType_Type.__name__ = "Integer32"
_CshcProtocolFibTcamWidthType_Object = MibTableColumn
cshcProtocolFibTcamWidthType = _CshcProtocolFibTcamWidthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 2, 1, 6),
    _CshcProtocolFibTcamWidthType_Type()
)
cshcProtocolFibTcamWidthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcProtocolFibTcamWidthType.setStatus("current")
_CshcAdjacencyUsageTable_Object = MibTable
cshcAdjacencyUsageTable = _CshcAdjacencyUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cshcAdjacencyUsageTable.setStatus("current")
_CshcAdjacencyUsageEntry_Object = MibTableRow
cshcAdjacencyUsageEntry = _CshcAdjacencyUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 3, 1)
)
cshcAdjacencyUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcAdjacencyUsageEntry.setStatus("current")
_CshcAdjacencyUsed_Type = Unsigned32
_CshcAdjacencyUsed_Object = MibTableColumn
cshcAdjacencyUsed = _CshcAdjacencyUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 3, 1, 1),
    _CshcAdjacencyUsed_Type()
)
cshcAdjacencyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcAdjacencyUsed.setStatus("current")
_CshcAdjacencyTotal_Type = Unsigned32
_CshcAdjacencyTotal_Object = MibTableColumn
cshcAdjacencyTotal = _CshcAdjacencyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 3, 1, 2),
    _CshcAdjacencyTotal_Type()
)
cshcAdjacencyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcAdjacencyTotal.setStatus("current")
_CshcForwardingLoadTable_Object = MibTable
cshcForwardingLoadTable = _CshcForwardingLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cshcForwardingLoadTable.setStatus("current")
_CshcForwardingLoadEntry_Object = MibTableRow
cshcForwardingLoadEntry = _CshcForwardingLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 4, 1)
)
cshcForwardingLoadEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcForwardingLoadEntry.setStatus("current")
_CshcForwardingLoadPktRate_Type = CounterBasedGauge64
_CshcForwardingLoadPktRate_Object = MibTableColumn
cshcForwardingLoadPktRate = _CshcForwardingLoadPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 4, 1, 1),
    _CshcForwardingLoadPktRate_Type()
)
cshcForwardingLoadPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcForwardingLoadPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cshcForwardingLoadPktRate.setUnits("pps")
_CshcForwardingLoadPktPeakRate_Type = CounterBasedGauge64
_CshcForwardingLoadPktPeakRate_Object = MibTableColumn
cshcForwardingLoadPktPeakRate = _CshcForwardingLoadPktPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 4, 1, 2),
    _CshcForwardingLoadPktPeakRate_Type()
)
cshcForwardingLoadPktPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcForwardingLoadPktPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    cshcForwardingLoadPktPeakRate.setUnits("pps")
_CshcForwardingLoadPktPeakTime_Type = DateAndTime
_CshcForwardingLoadPktPeakTime_Object = MibTableColumn
cshcForwardingLoadPktPeakTime = _CshcForwardingLoadPktPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 4, 1, 3),
    _CshcForwardingLoadPktPeakTime_Type()
)
cshcForwardingLoadPktPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcForwardingLoadPktPeakTime.setStatus("current")
_CshcAdjacencyResourceUsageTable_Object = MibTable
cshcAdjacencyResourceUsageTable = _CshcAdjacencyResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cshcAdjacencyResourceUsageTable.setStatus("current")
_CshcAdjacencyResourceUsageEntry_Object = MibTableRow
cshcAdjacencyResourceUsageEntry = _CshcAdjacencyResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5, 1)
)
cshcAdjacencyResourceUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyResourceIndex"),
)
if mibBuilder.loadTexts:
    cshcAdjacencyResourceUsageEntry.setStatus("current")
_CshcAdjacencyResourceIndex_Type = Unsigned32
_CshcAdjacencyResourceIndex_Object = MibTableColumn
cshcAdjacencyResourceIndex = _CshcAdjacencyResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5, 1, 1),
    _CshcAdjacencyResourceIndex_Type()
)
cshcAdjacencyResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcAdjacencyResourceIndex.setStatus("current")
_CshcAdjacencyResourceDescr_Type = SnmpAdminString
_CshcAdjacencyResourceDescr_Object = MibTableColumn
cshcAdjacencyResourceDescr = _CshcAdjacencyResourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5, 1, 2),
    _CshcAdjacencyResourceDescr_Type()
)
cshcAdjacencyResourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcAdjacencyResourceDescr.setStatus("current")
_CshcAdjacencyResourceUsed_Type = Unsigned32
_CshcAdjacencyResourceUsed_Object = MibTableColumn
cshcAdjacencyResourceUsed = _CshcAdjacencyResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5, 1, 3),
    _CshcAdjacencyResourceUsed_Type()
)
cshcAdjacencyResourceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcAdjacencyResourceUsed.setStatus("current")
_CshcAdjacencyResourceTotal_Type = Unsigned32
_CshcAdjacencyResourceTotal_Object = MibTableColumn
cshcAdjacencyResourceTotal = _CshcAdjacencyResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 5, 1, 4),
    _CshcAdjacencyResourceTotal_Type()
)
cshcAdjacencyResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcAdjacencyResourceTotal.setStatus("current")
_CshcMetResourceUsageTable_Object = MibTable
cshcMetResourceUsageTable = _CshcMetResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cshcMetResourceUsageTable.setStatus("current")
_CshcMetResourceUsageEntry_Object = MibTableRow
cshcMetResourceUsageEntry = _CshcMetResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1)
)
cshcMetResourceUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMetResourceIndex"),
)
if mibBuilder.loadTexts:
    cshcMetResourceUsageEntry.setStatus("current")
_CshcMetResourceIndex_Type = Unsigned32
_CshcMetResourceIndex_Object = MibTableColumn
cshcMetResourceIndex = _CshcMetResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1, 1),
    _CshcMetResourceIndex_Type()
)
cshcMetResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcMetResourceIndex.setStatus("current")
_CshcMetResourceDescr_Type = SnmpAdminString
_CshcMetResourceDescr_Object = MibTableColumn
cshcMetResourceDescr = _CshcMetResourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1, 2),
    _CshcMetResourceDescr_Type()
)
cshcMetResourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMetResourceDescr.setStatus("current")
_CshcMetResourceUsed_Type = Gauge32
_CshcMetResourceUsed_Object = MibTableColumn
cshcMetResourceUsed = _CshcMetResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1, 3),
    _CshcMetResourceUsed_Type()
)
cshcMetResourceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMetResourceUsed.setStatus("current")
_CshcMetResourceTotal_Type = Gauge32
_CshcMetResourceTotal_Object = MibTableColumn
cshcMetResourceTotal = _CshcMetResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1, 4),
    _CshcMetResourceTotal_Type()
)
cshcMetResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMetResourceTotal.setStatus("current")


class _CshcMetResourceMcastGrp_Type(Integer32):
    """Custom type cshcMetResourceMcastGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CshcMetResourceMcastGrp_Type.__name__ = "Integer32"
_CshcMetResourceMcastGrp_Object = MibTableColumn
cshcMetResourceMcastGrp = _CshcMetResourceMcastGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 1, 2, 6, 1, 5),
    _CshcMetResourceMcastGrp_Type()
)
cshcMetResourceMcastGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcMetResourceMcastGrp.setStatus("current")
_CshcInterface_ObjectIdentity = ObjectIdentity
cshcInterface = _CshcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2)
)
_CshcModuleInterfaceDropsTable_Object = MibTable
cshcModuleInterfaceDropsTable = _CshcModuleInterfaceDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cshcModuleInterfaceDropsTable.setStatus("current")
_CshcModuleInterfaceDropsEntry_Object = MibTableRow
cshcModuleInterfaceDropsEntry = _CshcModuleInterfaceDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1)
)
cshcModuleInterfaceDropsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcModuleInterfaceDropsEntry.setStatus("current")
_CshcModTxTotalDroppedPackets_Type = Counter64
_CshcModTxTotalDroppedPackets_Object = MibTableColumn
cshcModTxTotalDroppedPackets = _CshcModTxTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 1),
    _CshcModTxTotalDroppedPackets_Type()
)
cshcModTxTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModTxTotalDroppedPackets.setStatus("current")
_CshcModRxTotalDroppedPackets_Type = Counter64
_CshcModRxTotalDroppedPackets_Object = MibTableColumn
cshcModRxTotalDroppedPackets = _CshcModRxTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 2),
    _CshcModRxTotalDroppedPackets_Type()
)
cshcModRxTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModRxTotalDroppedPackets.setStatus("current")
_CshcModTxTopDropPort_Type = InterfaceIndexOrZero
_CshcModTxTopDropPort_Object = MibTableColumn
cshcModTxTopDropPort = _CshcModTxTopDropPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 3),
    _CshcModTxTopDropPort_Type()
)
cshcModTxTopDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModTxTopDropPort.setStatus("current")
_CshcModRxTopDropPort_Type = InterfaceIndexOrZero
_CshcModRxTopDropPort_Object = MibTableColumn
cshcModRxTopDropPort = _CshcModRxTopDropPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 4),
    _CshcModRxTopDropPort_Type()
)
cshcModRxTopDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModRxTopDropPort.setStatus("current")
_CshcModTxTopDropIfIndexList_Type = CiscoInterfaceIndexList
_CshcModTxTopDropIfIndexList_Object = MibTableColumn
cshcModTxTopDropIfIndexList = _CshcModTxTopDropIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 5),
    _CshcModTxTopDropIfIndexList_Type()
)
cshcModTxTopDropIfIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModTxTopDropIfIndexList.setStatus("current")
_CshcModRxTopDropIfIndexList_Type = CiscoInterfaceIndexList
_CshcModRxTopDropIfIndexList_Object = MibTableColumn
cshcModRxTopDropIfIndexList = _CshcModRxTopDropIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 1, 1, 6),
    _CshcModRxTopDropIfIndexList_Type()
)
cshcModRxTopDropIfIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcModRxTopDropIfIndexList.setStatus("current")
_CshcInterfaceBufferTable_Object = MibTable
cshcInterfaceBufferTable = _CshcInterfaceBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cshcInterfaceBufferTable.setStatus("current")
_CshcInterfaceBufferEntry_Object = MibTableRow
cshcInterfaceBufferEntry = _CshcInterfaceBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 2, 1)
)
cshcInterfaceBufferEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cshcInterfaceBufferEntry.setStatus("current")
_CshcInterfaceTransmitBufferSize_Type = Unsigned32
_CshcInterfaceTransmitBufferSize_Object = MibTableColumn
cshcInterfaceTransmitBufferSize = _CshcInterfaceTransmitBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 2, 1, 1),
    _CshcInterfaceTransmitBufferSize_Type()
)
cshcInterfaceTransmitBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcInterfaceTransmitBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cshcInterfaceTransmitBufferSize.setUnits("bytes")
_CshcInterfaceReceiveBufferSize_Type = Unsigned32
_CshcInterfaceReceiveBufferSize_Object = MibTableColumn
cshcInterfaceReceiveBufferSize = _CshcInterfaceReceiveBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 2, 1, 2),
    _CshcInterfaceReceiveBufferSize_Type()
)
cshcInterfaceReceiveBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcInterfaceReceiveBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cshcInterfaceReceiveBufferSize.setUnits("bytes")
_CshcInternalChannelTable_Object = MibTable
cshcInternalChannelTable = _CshcInternalChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cshcInternalChannelTable.setStatus("current")
_CshcInternalChannelEntry_Object = MibTableRow
cshcInternalChannelEntry = _CshcInternalChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1)
)
cshcInternalChannelEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlType"),
)
if mibBuilder.loadTexts:
    cshcInternalChannelEntry.setStatus("current")
_CshcIntlChnlType_Type = CshcInternalChannelType
_CshcIntlChnlType_Object = MibTableColumn
cshcIntlChnlType = _CshcIntlChnlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 1),
    _CshcIntlChnlType_Type()
)
cshcIntlChnlType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcIntlChnlType.setStatus("current")
_CshcIntlChnlRxPacketRate_Type = CounterBasedGauge64
_CshcIntlChnlRxPacketRate_Object = MibTableColumn
cshcIntlChnlRxPacketRate = _CshcIntlChnlRxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 2),
    _CshcIntlChnlRxPacketRate_Type()
)
cshcIntlChnlRxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlRxPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cshcIntlChnlRxPacketRate.setUnits("packets per second")
_CshcIntlChnlRxTotalPackets_Type = Counter64
_CshcIntlChnlRxTotalPackets_Object = MibTableColumn
cshcIntlChnlRxTotalPackets = _CshcIntlChnlRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 3),
    _CshcIntlChnlRxTotalPackets_Type()
)
cshcIntlChnlRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlRxTotalPackets.setStatus("current")
_CshcIntlChnlRxDroppedPackets_Type = Counter64
_CshcIntlChnlRxDroppedPackets_Object = MibTableColumn
cshcIntlChnlRxDroppedPackets = _CshcIntlChnlRxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 4),
    _CshcIntlChnlRxDroppedPackets_Type()
)
cshcIntlChnlRxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlRxDroppedPackets.setStatus("current")
_CshcIntlChnlTxPacketRate_Type = CounterBasedGauge64
_CshcIntlChnlTxPacketRate_Object = MibTableColumn
cshcIntlChnlTxPacketRate = _CshcIntlChnlTxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 5),
    _CshcIntlChnlTxPacketRate_Type()
)
cshcIntlChnlTxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlTxPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cshcIntlChnlTxPacketRate.setUnits("packets per second")
_CshcIntlChnlTxTotalPackets_Type = Counter64
_CshcIntlChnlTxTotalPackets_Object = MibTableColumn
cshcIntlChnlTxTotalPackets = _CshcIntlChnlTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 6),
    _CshcIntlChnlTxTotalPackets_Type()
)
cshcIntlChnlTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlTxTotalPackets.setStatus("current")
_CshcIntlChnlTxDroppedPackets_Type = Counter64
_CshcIntlChnlTxDroppedPackets_Object = MibTableColumn
cshcIntlChnlTxDroppedPackets = _CshcIntlChnlTxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 2, 3, 1, 7),
    _CshcIntlChnlTxDroppedPackets_Type()
)
cshcIntlChnlTxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIntlChnlTxDroppedPackets.setStatus("current")
_CshcCPURateLimiterResources_ObjectIdentity = ObjectIdentity
cshcCPURateLimiterResources = _CshcCPURateLimiterResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3)
)
_CshcCPURateLimiterResourcesTable_Object = MibTable
cshcCPURateLimiterResourcesTable = _CshcCPURateLimiterResourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cshcCPURateLimiterResourcesTable.setStatus("current")
_CshcCPURateLimiterResourcesEntry_Object = MibTableRow
cshcCPURateLimiterResourcesEntry = _CshcCPURateLimiterResourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1, 1)
)
cshcCPURateLimiterResourcesEntry.setIndexNames(
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcCPURateLimiterNetworkLayer"),
)
if mibBuilder.loadTexts:
    cshcCPURateLimiterResourcesEntry.setStatus("current")


class _CshcCPURateLimiterNetworkLayer_Type(Integer32):
    """Custom type cshcCPURateLimiterNetworkLayer based on Integer32"""
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
        *(("layer2", 1),
          ("layer2Input", 3),
          ("layer2Output", 4),
          ("layer3", 2))
    )


_CshcCPURateLimiterNetworkLayer_Type.__name__ = "Integer32"
_CshcCPURateLimiterNetworkLayer_Object = MibTableColumn
cshcCPURateLimiterNetworkLayer = _CshcCPURateLimiterNetworkLayer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1, 1, 1),
    _CshcCPURateLimiterNetworkLayer_Type()
)
cshcCPURateLimiterNetworkLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcCPURateLimiterNetworkLayer.setStatus("current")
_CshcCPURateLimiterTotal_Type = Unsigned32
_CshcCPURateLimiterTotal_Object = MibTableColumn
cshcCPURateLimiterTotal = _CshcCPURateLimiterTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1, 1, 2),
    _CshcCPURateLimiterTotal_Type()
)
cshcCPURateLimiterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcCPURateLimiterTotal.setStatus("current")
_CshcCPURateLimiterUsed_Type = Unsigned32
_CshcCPURateLimiterUsed_Object = MibTableColumn
cshcCPURateLimiterUsed = _CshcCPURateLimiterUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1, 1, 3),
    _CshcCPURateLimiterUsed_Type()
)
cshcCPURateLimiterUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcCPURateLimiterUsed.setStatus("current")
_CshcCPURateLimiterReserved_Type = Unsigned32
_CshcCPURateLimiterReserved_Object = MibTableColumn
cshcCPURateLimiterReserved = _CshcCPURateLimiterReserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 3, 1, 1, 4),
    _CshcCPURateLimiterReserved_Type()
)
cshcCPURateLimiterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcCPURateLimiterReserved.setStatus("current")
_CshcIcamResources_ObjectIdentity = ObjectIdentity
cshcIcamResources = _CshcIcamResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4)
)
_CshcIcamUtilizationTable_Object = MibTable
cshcIcamUtilizationTable = _CshcIcamUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cshcIcamUtilizationTable.setStatus("current")
_CshcIcamUtilizationEntry_Object = MibTableRow
cshcIcamUtilizationEntry = _CshcIcamUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4, 1, 1)
)
cshcIcamUtilizationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cshcIcamUtilizationEntry.setStatus("current")
_CshcIcamCreated_Type = Unsigned32
_CshcIcamCreated_Object = MibTableColumn
cshcIcamCreated = _CshcIcamCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4, 1, 1, 1),
    _CshcIcamCreated_Type()
)
cshcIcamCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIcamCreated.setStatus("current")
_CshcIcamFailed_Type = Unsigned32
_CshcIcamFailed_Object = MibTableColumn
cshcIcamFailed = _CshcIcamFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4, 1, 1, 2),
    _CshcIcamFailed_Type()
)
cshcIcamFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIcamFailed.setStatus("current")
_CshcIcamUtilization_Type = Percent
_CshcIcamUtilization_Object = MibTableColumn
cshcIcamUtilization = _CshcIcamUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 4, 1, 1, 3),
    _CshcIcamUtilization_Type()
)
cshcIcamUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcIcamUtilization.setStatus("current")
_CshcNetflowFlowMaskResources_ObjectIdentity = ObjectIdentity
cshcNetflowFlowMaskResources = _CshcNetflowFlowMaskResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5)
)
_CshcNetflowFlowMaskTable_Object = MibTable
cshcNetflowFlowMaskTable = _CshcNetflowFlowMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskTable.setStatus("current")
_CshcNetflowFlowMaskEntry_Object = MibTableRow
cshcNetflowFlowMaskEntry = _CshcNetflowFlowMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1, 1)
)
cshcNetflowFlowMaskEntry.setIndexNames(
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowFlowMaskAddrType"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowFlowMaskIndex"),
)
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskEntry.setStatus("current")
_CshcNetflowFlowMaskAddrType_Type = InetAddressType
_CshcNetflowFlowMaskAddrType_Object = MibTableColumn
cshcNetflowFlowMaskAddrType = _CshcNetflowFlowMaskAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1, 1, 1),
    _CshcNetflowFlowMaskAddrType_Type()
)
cshcNetflowFlowMaskAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskAddrType.setStatus("current")
_CshcNetflowFlowMaskIndex_Type = Unsigned32
_CshcNetflowFlowMaskIndex_Object = MibTableColumn
cshcNetflowFlowMaskIndex = _CshcNetflowFlowMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1, 1, 2),
    _CshcNetflowFlowMaskIndex_Type()
)
cshcNetflowFlowMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskIndex.setStatus("current")


class _CshcNetflowFlowMaskType_Type(Integer32):
    """Custom type cshcNetflowFlowMaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("atleastDst", 13),
          ("atleastFullFlow", 10),
          ("atleastInterfaceDest", 20),
          ("atleastInterfaceFullFlow", 11),
          ("atleastInterfaceSrc", 22),
          ("atleastInterfaceSrcDest", 9),
          ("atleastSrc", 12),
          ("atleastSrcDst", 14),
          ("conflict", 28),
          ("destOnly", 3),
          ("dstOnlyCR", 24),
          ("err", 29),
          ("exceptFullFlow", 17),
          ("exceptInterfaceFullFlow", 18),
          ("fullFlow", 6),
          ("fullFlow1", 31),
          ("fullFlow2", 32),
          ("fullFlow3", 33),
          ("fullFlowCR", 25),
          ("interfaceDest", 19),
          ("interfaceFullFlow", 7),
          ("interfaceFullFlowCR", 26),
          ("interfaceFullFlowOrFullFlow", 8),
          ("interfaceSrc", 21),
          ("interfaceSrcDest", 5),
          ("lessThanFullFlow", 16),
          ("max", 27),
          ("null", 1),
          ("reserved", 37),
          ("shortest", 15),
          ("srcDest", 4),
          ("srcOnly", 2),
          ("srcOnlyCR", 23),
          ("unused", 30),
          ("vlanFullFlow1", 34),
          ("vlanFullFlow2", 35),
          ("vlanFullFlow3", 36))
    )


_CshcNetflowFlowMaskType_Type.__name__ = "Integer32"
_CshcNetflowFlowMaskType_Object = MibTableColumn
cshcNetflowFlowMaskType = _CshcNetflowFlowMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1, 1, 3),
    _CshcNetflowFlowMaskType_Type()
)
cshcNetflowFlowMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskType.setStatus("current")


class _CshcNetflowFlowMaskFeature_Type(Bits):
    """Custom type cshcNetflowFlowMaskFeature based on Bits"""
    namedValues = NamedValues(
        *(("authProxy", 27),
          ("cryptoEgress", 8),
          ("cryptoIngress", 7),
          ("cryptoRedirectIngress", 49),
          ("dai", 37),
          ("dot1ad", 73),
          ("eomIw", 64),
          ("eomIw2", 65),
          ("erSpanTermination", 45),
          ("guardian", 12),
          ("iPAdmissionL2Eou", 53),
          ("iPAdmissionL2EouArp", 54),
          ("iPAdmissionL3Eou", 52),
          ("idsIngress", 10),
          ("inspDummyEgress", 32),
          ("inspDummyIngress", 31),
          ("inspEgress", 26),
          ("inspIngress", 25),
          ("ipAcgEgress", 2),
          ("ipAcgIngress", 1),
          ("ipAdmissionL2Http", 55),
          ("ipAdmissionL2HttpArp", 56),
          ("ipDot1xAcl", 71),
          ("ipDot1xAclArp", 72),
          ("ipDsEgress", 20),
          ("ipDsIngress", 19),
          ("ipDsL3Egress", 48),
          ("ipDsL3Ingress", 47),
          ("ipPaclIngress", 38),
          ("ipRecir", 51),
          ("ipSguardIngress", 59),
          ("ipSlb", 41),
          ("ipSpanPcap", 74),
          ("ipVaclEgress", 22),
          ("ipVaclIngress", 21),
          ("ipv4Default", 42),
          ("ipv4L2IntfNde", 58),
          ("ipv4L3IntfNde", 57),
          ("ipv4VrfNdeEgress", 66),
          ("ipv6AcgEgress", 14),
          ("ipv6AcgIngress", 13),
          ("ipv6CryptoRedirectIngress", 75),
          ("ipv6Default", 43),
          ("ipv6GlobalDefault", 36),
          ("ipv6Guardian", 80),
          ("ipv6Mcast", 46),
          ("ipv6Qos", 81),
          ("ipv6Rpf", 35),
          ("ipv6SvcAcclrtIngress", 77),
          ("l1Egress", 67),
          ("l1GlobalEgress", 69),
          ("l1GlobalIngress", 70),
          ("l1Ingress", 68),
          ("macPaclIngress", 39),
          ("macVaclEgress", 24),
          ("macVaclIngress", 23),
          ("mcastAcgEgress", 16),
          ("mcastAcgIngress", 15),
          ("mcastStub", 17),
          ("mcastUrd", 18),
          ("mplsDefault", 44),
          ("mplsIcmpBridge", 40),
          ("natEngress", 4),
          ("natIngress", 3),
          ("natInside", 5),
          ("nbarEgress", 34),
          ("nbarIngress", 33),
          ("nfAggregation", 78),
          ("nfSampling", 79),
          ("none", 82),
          ("null", 0),
          ("otherDefault", 50),
          ("pbr", 6),
          ("pvtHostsIngress", 60),
          ("qos", 9),
          ("rpf", 28),
          ("svcAcclrtIngress", 76),
          ("tcpAdjustMssEgress", 63),
          ("tcpAdjustMssIngress", 62),
          ("tcpIntrcptEgress", 11),
          ("vrfNatIngress", 61),
          ("wccpEgress", 30),
          ("wccpIngress", 29))
    )

_CshcNetflowFlowMaskFeature_Type.__name__ = "Bits"
_CshcNetflowFlowMaskFeature_Object = MibTableColumn
cshcNetflowFlowMaskFeature = _CshcNetflowFlowMaskFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 5, 1, 1, 4),
    _CshcNetflowFlowMaskFeature_Type()
)
cshcNetflowFlowMaskFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskFeature.setStatus("current")
_CshcNetflowResourceUsage_ObjectIdentity = ObjectIdentity
cshcNetflowResourceUsage = _CshcNetflowResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6)
)
_CshcNetflowResourceUsageTable_Object = MibTable
cshcNetflowResourceUsageTable = _CshcNetflowResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageTable.setStatus("current")
_CshcNetflowResourceUsageEntry_Object = MibTableRow
cshcNetflowResourceUsageEntry = _CshcNetflowResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1)
)
cshcNetflowResourceUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageIndex"),
)
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageEntry.setStatus("current")


class _CshcNetflowResourceUsageIndex_Type(Unsigned32):
    """Custom type cshcNetflowResourceUsageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CshcNetflowResourceUsageIndex_Type.__name__ = "Unsigned32"
_CshcNetflowResourceUsageIndex_Object = MibTableColumn
cshcNetflowResourceUsageIndex = _CshcNetflowResourceUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 1),
    _CshcNetflowResourceUsageIndex_Type()
)
cshcNetflowResourceUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageIndex.setStatus("current")
_CshcNetflowResourceUsageDescr_Type = SnmpAdminString
_CshcNetflowResourceUsageDescr_Object = MibTableColumn
cshcNetflowResourceUsageDescr = _CshcNetflowResourceUsageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 2),
    _CshcNetflowResourceUsageDescr_Type()
)
cshcNetflowResourceUsageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageDescr.setStatus("current")
_CshcNetflowResourceUsageUtil_Type = Percent
_CshcNetflowResourceUsageUtil_Object = MibTableColumn
cshcNetflowResourceUsageUtil = _CshcNetflowResourceUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 3),
    _CshcNetflowResourceUsageUtil_Type()
)
cshcNetflowResourceUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageUtil.setStatus("current")
_CshcNetflowResourceUsageUsed_Type = Gauge32
_CshcNetflowResourceUsageUsed_Object = MibTableColumn
cshcNetflowResourceUsageUsed = _CshcNetflowResourceUsageUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 4),
    _CshcNetflowResourceUsageUsed_Type()
)
cshcNetflowResourceUsageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageUsed.setStatus("current")
_CshcNetflowResourceUsageFree_Type = Gauge32
_CshcNetflowResourceUsageFree_Object = MibTableColumn
cshcNetflowResourceUsageFree = _CshcNetflowResourceUsageFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 5),
    _CshcNetflowResourceUsageFree_Type()
)
cshcNetflowResourceUsageFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageFree.setStatus("current")


class _CshcNetflowResourceUsageFail_Type(Integer32):
    """Custom type cshcNetflowResourceUsageFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_CshcNetflowResourceUsageFail_Type.__name__ = "Integer32"
_CshcNetflowResourceUsageFail_Object = MibTableColumn
cshcNetflowResourceUsageFail = _CshcNetflowResourceUsageFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 6, 1, 1, 6),
    _CshcNetflowResourceUsageFail_Type()
)
cshcNetflowResourceUsageFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcNetflowResourceUsageFail.setStatus("current")
_CshcQosResourceUsage_ObjectIdentity = ObjectIdentity
cshcQosResourceUsage = _CshcQosResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7)
)
_CshcQosResourceUsageTable_Object = MibTable
cshcQosResourceUsageTable = _CshcQosResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cshcQosResourceUsageTable.setStatus("current")
_CshcQosResourceUsageEntry_Object = MibTableRow
cshcQosResourceUsageEntry = _CshcQosResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7, 1, 1)
)
cshcQosResourceUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcQosResourceType"),
)
if mibBuilder.loadTexts:
    cshcQosResourceUsageEntry.setStatus("current")


class _CshcQosResourceType_Type(Integer32):
    """Custom type cshcQosResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregatePolicers", 1),
          ("distributedPolicers", 2),
          ("policerProfiles", 3))
    )


_CshcQosResourceType_Type.__name__ = "Integer32"
_CshcQosResourceType_Object = MibTableColumn
cshcQosResourceType = _CshcQosResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7, 1, 1, 1),
    _CshcQosResourceType_Type()
)
cshcQosResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshcQosResourceType.setStatus("current")
_CshcQosResourceUsed_Type = Unsigned32
_CshcQosResourceUsed_Object = MibTableColumn
cshcQosResourceUsed = _CshcQosResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7, 1, 1, 2),
    _CshcQosResourceUsed_Type()
)
cshcQosResourceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcQosResourceUsed.setStatus("current")
_CshcQosResourceTotal_Type = Unsigned32
_CshcQosResourceTotal_Object = MibTableColumn
cshcQosResourceTotal = _CshcQosResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 1, 7, 1, 1, 3),
    _CshcQosResourceTotal_Type()
)
cshcQosResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshcQosResourceTotal.setStatus("current")
_CiscoSwitchHardwareCapacityMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSwitchHardwareCapacityMIBConformance = _CiscoSwitchHardwareCapacityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2)
)
_CiscoSwitchHardwareCapacityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSwitchHardwareCapacityMIBCompliances = _CiscoSwitchHardwareCapacityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 1)
)
_CiscoSwitchHardwareCapacityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSwitchHardwareCapacityMIBGroups = _CiscoSwitchHardwareCapacityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2)
)

# Managed Objects groups

cshcMacUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 1)
)
cshcMacUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacCollisions"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacTotal"))
)
if mibBuilder.loadTexts:
    cshcMacUsageGroup.setStatus("current")

cshcVpnCamUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 2)
)
cshcVpnCamUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcVpnCamUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcVpnCamTotal"))
)
if mibBuilder.loadTexts:
    cshcVpnCamUsageGroup.setStatus("current")

cshcFibTcamUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 3)
)
cshcFibTcamUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc72bitsFibTcamUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc72bitsFibTcamTotal"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc144bitsFibTcamUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc144bitsFibTcamTotal"))
)
if mibBuilder.loadTexts:
    cshcFibTcamUsageGroup.setStatus("current")

cshcProtocolFibTcamUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 4)
)
cshcProtocolFibTcamUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamTotal"))
)
if mibBuilder.loadTexts:
    cshcProtocolFibTcamUsageGroup.setStatus("current")

cshcAdjacencyUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 5)
)
cshcAdjacencyUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyTotal"))
)
if mibBuilder.loadTexts:
    cshcAdjacencyUsageGroup.setStatus("current")

cshcForwardingLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 6)
)
cshcForwardingLoadGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcForwardingLoadPktRate"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcForwardingLoadPktPeakRate"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcForwardingLoadPktPeakTime"))
)
if mibBuilder.loadTexts:
    cshcForwardingLoadGroup.setStatus("current")

cshcModuleInterfaceDropsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 7)
)
cshcModuleInterfaceDropsGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModTxTotalDroppedPackets"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModRxTotalDroppedPackets"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModTxTopDropPort"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModRxTopDropPort"))
)
if mibBuilder.loadTexts:
    cshcModuleInterfaceDropsGroup.setStatus("current")

cshcInterfaceBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 8)
)
cshcInterfaceBufferGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcInterfaceTransmitBufferSize"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcInterfaceReceiveBufferSize"))
)
if mibBuilder.loadTexts:
    cshcInterfaceBufferGroup.setStatus("current")

cshcInternalChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 9)
)
cshcInternalChannelGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlRxPacketRate"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlRxTotalPackets"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlRxDroppedPackets"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlTxPacketRate"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlTxTotalPackets"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIntlChnlTxDroppedPackets"))
)
if mibBuilder.loadTexts:
    cshcInternalChannelGroup.setStatus("current")

cshcCPURateLimiterResourcesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 10)
)
cshcCPURateLimiterResourcesGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcCPURateLimiterTotal"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcCPURateLimiterUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcCPURateLimiterReserved"))
)
if mibBuilder.loadTexts:
    cshcCPURateLimiterResourcesGroup.setStatus("current")

cshcIcamResourcesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 11)
)
cshcIcamResourcesGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIcamCreated"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIcamFailed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcIcamUtilization"))
)
if mibBuilder.loadTexts:
    cshcIcamResourcesGroup.setStatus("current")

cshcNetflowFlowMaskResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 12)
)
cshcNetflowFlowMaskResourceGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowFlowMaskType"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowFlowMaskFeature"))
)
if mibBuilder.loadTexts:
    cshcNetflowFlowMaskResourceGroup.setStatus("current")

cshcFibTcamUsageExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 13)
)
cshcFibTcamUsageExtGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc288bitsFibTcamUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshc288bitsFibTcamTotal"))
)
if mibBuilder.loadTexts:
    cshcFibTcamUsageExtGroup.setStatus("current")

cshcNetflowFlowResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 14)
)
cshcNetflowFlowResourceUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageDescr"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageUtil"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageFree"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcNetflowResourceUsageFail"))
)
if mibBuilder.loadTexts:
    cshcNetflowFlowResourceUsageGroup.setStatus("current")

cshcMacUsageExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 15)
)
cshcMacUsageExtGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacMcast"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacUcast"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacLines"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMacLinesFull"))
)
if mibBuilder.loadTexts:
    cshcMacUsageExtGroup.setStatus("current")

cshcProtocolFibTcamUsageExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 16)
)
cshcProtocolFibTcamUsageExtGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamLogicalUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamLogicalTotal"))
)
if mibBuilder.loadTexts:
    cshcProtocolFibTcamUsageExtGroup.setStatus("current")

cshcAdjacencyResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 17)
)
cshcAdjacencyResourceUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyResourceDescr"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyResourceUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcAdjacencyResourceTotal"))
)
if mibBuilder.loadTexts:
    cshcAdjacencyResourceUsageGroup.setStatus("current")

cshcQosResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 18)
)
cshcQosResourceUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcQosResourceUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcQosResourceTotal"))
)
if mibBuilder.loadTexts:
    cshcQosResourceUsageGroup.setStatus("current")

cshcModTopDropIfIndexListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 19)
)
cshcModTopDropIfIndexListGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModTxTopDropIfIndexList"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcModRxTopDropIfIndexList"))
)
if mibBuilder.loadTexts:
    cshcModTopDropIfIndexListGroup.setStatus("current")

cshcMetResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 20)
)
cshcMetResourceUsageGroup.setObjects(
      *(("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMetResourceDescr"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMetResourceUsed"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMetResourceTotal"),
        ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcMetResourceMcastGrp"))
)
if mibBuilder.loadTexts:
    cshcMetResourceUsageGroup.setStatus("current")

cshcProtocolFibTcamWidthTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 2, 21)
)
cshcProtocolFibTcamWidthTypeGroup.setObjects(
    ("CISCO-SWITCH-HARDWARE-CAPACITY-MIB", "cshcProtocolFibTcamWidthType")
)
if mibBuilder.loadTexts:
    cshcProtocolFibTcamWidthTypeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSwitchHardwareCapacityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSwitchHardwareCapacityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSwitchHardwareCapacityMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSwitchHardwareCapacityMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoSwitchHardwareCapacityMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSwitchHardwareCapacityMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoSwitchHardwareCapacityMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 663, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSwitchHardwareCapacityMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-HARDWARE-CAPACITY-MIB",
    **{"CshcInternalChannelType": CshcInternalChannelType,
       "ciscoSwitchHardwareCapacityMIB": ciscoSwitchHardwareCapacityMIB,
       "ciscoSwitchHardwareCapacityMIBNotifs": ciscoSwitchHardwareCapacityMIBNotifs,
       "ciscoSwitchHardwareCapacityMIBObjects": ciscoSwitchHardwareCapacityMIBObjects,
       "cshcForwarding": cshcForwarding,
       "cshcL2Forwarding": cshcL2Forwarding,
       "cshcMacUsageTable": cshcMacUsageTable,
       "cshcMacUsageEntry": cshcMacUsageEntry,
       "cshcMacCollisions": cshcMacCollisions,
       "cshcMacUsed": cshcMacUsed,
       "cshcMacTotal": cshcMacTotal,
       "cshcMacMcast": cshcMacMcast,
       "cshcMacUcast": cshcMacUcast,
       "cshcMacLines": cshcMacLines,
       "cshcMacLinesFull": cshcMacLinesFull,
       "cshcVpnCamUsageTable": cshcVpnCamUsageTable,
       "cshcVpnCamUsageEntry": cshcVpnCamUsageEntry,
       "cshcVpnCamUsed": cshcVpnCamUsed,
       "cshcVpnCamTotal": cshcVpnCamTotal,
       "cshcL3Forwarding": cshcL3Forwarding,
       "cshcFibTcamUsageTable": cshcFibTcamUsageTable,
       "cshcFibTcamUsageEntry": cshcFibTcamUsageEntry,
       "cshc72bitsFibTcamUsed": cshc72bitsFibTcamUsed,
       "cshc72bitsFibTcamTotal": cshc72bitsFibTcamTotal,
       "cshc144bitsFibTcamUsed": cshc144bitsFibTcamUsed,
       "cshc144bitsFibTcamTotal": cshc144bitsFibTcamTotal,
       "cshc288bitsFibTcamUsed": cshc288bitsFibTcamUsed,
       "cshc288bitsFibTcamTotal": cshc288bitsFibTcamTotal,
       "cshcProtocolFibTcamUsageTable": cshcProtocolFibTcamUsageTable,
       "cshcProtocolFibTcamUsageEntry": cshcProtocolFibTcamUsageEntry,
       "cshcProtocolFibTcamProtocol": cshcProtocolFibTcamProtocol,
       "cshcProtocolFibTcamUsed": cshcProtocolFibTcamUsed,
       "cshcProtocolFibTcamTotal": cshcProtocolFibTcamTotal,
       "cshcProtocolFibTcamLogicalUsed": cshcProtocolFibTcamLogicalUsed,
       "cshcProtocolFibTcamLogicalTotal": cshcProtocolFibTcamLogicalTotal,
       "cshcProtocolFibTcamWidthType": cshcProtocolFibTcamWidthType,
       "cshcAdjacencyUsageTable": cshcAdjacencyUsageTable,
       "cshcAdjacencyUsageEntry": cshcAdjacencyUsageEntry,
       "cshcAdjacencyUsed": cshcAdjacencyUsed,
       "cshcAdjacencyTotal": cshcAdjacencyTotal,
       "cshcForwardingLoadTable": cshcForwardingLoadTable,
       "cshcForwardingLoadEntry": cshcForwardingLoadEntry,
       "cshcForwardingLoadPktRate": cshcForwardingLoadPktRate,
       "cshcForwardingLoadPktPeakRate": cshcForwardingLoadPktPeakRate,
       "cshcForwardingLoadPktPeakTime": cshcForwardingLoadPktPeakTime,
       "cshcAdjacencyResourceUsageTable": cshcAdjacencyResourceUsageTable,
       "cshcAdjacencyResourceUsageEntry": cshcAdjacencyResourceUsageEntry,
       "cshcAdjacencyResourceIndex": cshcAdjacencyResourceIndex,
       "cshcAdjacencyResourceDescr": cshcAdjacencyResourceDescr,
       "cshcAdjacencyResourceUsed": cshcAdjacencyResourceUsed,
       "cshcAdjacencyResourceTotal": cshcAdjacencyResourceTotal,
       "cshcMetResourceUsageTable": cshcMetResourceUsageTable,
       "cshcMetResourceUsageEntry": cshcMetResourceUsageEntry,
       "cshcMetResourceIndex": cshcMetResourceIndex,
       "cshcMetResourceDescr": cshcMetResourceDescr,
       "cshcMetResourceUsed": cshcMetResourceUsed,
       "cshcMetResourceTotal": cshcMetResourceTotal,
       "cshcMetResourceMcastGrp": cshcMetResourceMcastGrp,
       "cshcInterface": cshcInterface,
       "cshcModuleInterfaceDropsTable": cshcModuleInterfaceDropsTable,
       "cshcModuleInterfaceDropsEntry": cshcModuleInterfaceDropsEntry,
       "cshcModTxTotalDroppedPackets": cshcModTxTotalDroppedPackets,
       "cshcModRxTotalDroppedPackets": cshcModRxTotalDroppedPackets,
       "cshcModTxTopDropPort": cshcModTxTopDropPort,
       "cshcModRxTopDropPort": cshcModRxTopDropPort,
       "cshcModTxTopDropIfIndexList": cshcModTxTopDropIfIndexList,
       "cshcModRxTopDropIfIndexList": cshcModRxTopDropIfIndexList,
       "cshcInterfaceBufferTable": cshcInterfaceBufferTable,
       "cshcInterfaceBufferEntry": cshcInterfaceBufferEntry,
       "cshcInterfaceTransmitBufferSize": cshcInterfaceTransmitBufferSize,
       "cshcInterfaceReceiveBufferSize": cshcInterfaceReceiveBufferSize,
       "cshcInternalChannelTable": cshcInternalChannelTable,
       "cshcInternalChannelEntry": cshcInternalChannelEntry,
       "cshcIntlChnlType": cshcIntlChnlType,
       "cshcIntlChnlRxPacketRate": cshcIntlChnlRxPacketRate,
       "cshcIntlChnlRxTotalPackets": cshcIntlChnlRxTotalPackets,
       "cshcIntlChnlRxDroppedPackets": cshcIntlChnlRxDroppedPackets,
       "cshcIntlChnlTxPacketRate": cshcIntlChnlTxPacketRate,
       "cshcIntlChnlTxTotalPackets": cshcIntlChnlTxTotalPackets,
       "cshcIntlChnlTxDroppedPackets": cshcIntlChnlTxDroppedPackets,
       "cshcCPURateLimiterResources": cshcCPURateLimiterResources,
       "cshcCPURateLimiterResourcesTable": cshcCPURateLimiterResourcesTable,
       "cshcCPURateLimiterResourcesEntry": cshcCPURateLimiterResourcesEntry,
       "cshcCPURateLimiterNetworkLayer": cshcCPURateLimiterNetworkLayer,
       "cshcCPURateLimiterTotal": cshcCPURateLimiterTotal,
       "cshcCPURateLimiterUsed": cshcCPURateLimiterUsed,
       "cshcCPURateLimiterReserved": cshcCPURateLimiterReserved,
       "cshcIcamResources": cshcIcamResources,
       "cshcIcamUtilizationTable": cshcIcamUtilizationTable,
       "cshcIcamUtilizationEntry": cshcIcamUtilizationEntry,
       "cshcIcamCreated": cshcIcamCreated,
       "cshcIcamFailed": cshcIcamFailed,
       "cshcIcamUtilization": cshcIcamUtilization,
       "cshcNetflowFlowMaskResources": cshcNetflowFlowMaskResources,
       "cshcNetflowFlowMaskTable": cshcNetflowFlowMaskTable,
       "cshcNetflowFlowMaskEntry": cshcNetflowFlowMaskEntry,
       "cshcNetflowFlowMaskAddrType": cshcNetflowFlowMaskAddrType,
       "cshcNetflowFlowMaskIndex": cshcNetflowFlowMaskIndex,
       "cshcNetflowFlowMaskType": cshcNetflowFlowMaskType,
       "cshcNetflowFlowMaskFeature": cshcNetflowFlowMaskFeature,
       "cshcNetflowResourceUsage": cshcNetflowResourceUsage,
       "cshcNetflowResourceUsageTable": cshcNetflowResourceUsageTable,
       "cshcNetflowResourceUsageEntry": cshcNetflowResourceUsageEntry,
       "cshcNetflowResourceUsageIndex": cshcNetflowResourceUsageIndex,
       "cshcNetflowResourceUsageDescr": cshcNetflowResourceUsageDescr,
       "cshcNetflowResourceUsageUtil": cshcNetflowResourceUsageUtil,
       "cshcNetflowResourceUsageUsed": cshcNetflowResourceUsageUsed,
       "cshcNetflowResourceUsageFree": cshcNetflowResourceUsageFree,
       "cshcNetflowResourceUsageFail": cshcNetflowResourceUsageFail,
       "cshcQosResourceUsage": cshcQosResourceUsage,
       "cshcQosResourceUsageTable": cshcQosResourceUsageTable,
       "cshcQosResourceUsageEntry": cshcQosResourceUsageEntry,
       "cshcQosResourceType": cshcQosResourceType,
       "cshcQosResourceUsed": cshcQosResourceUsed,
       "cshcQosResourceTotal": cshcQosResourceTotal,
       "ciscoSwitchHardwareCapacityMIBConformance": ciscoSwitchHardwareCapacityMIBConformance,
       "ciscoSwitchHardwareCapacityMIBCompliances": ciscoSwitchHardwareCapacityMIBCompliances,
       "ciscoSwitchHardwareCapacityMIBCompliance": ciscoSwitchHardwareCapacityMIBCompliance,
       "ciscoSwitchHardwareCapacityMIBCompliance1": ciscoSwitchHardwareCapacityMIBCompliance1,
       "ciscoSwitchHardwareCapacityMIBCompliance2": ciscoSwitchHardwareCapacityMIBCompliance2,
       "ciscoSwitchHardwareCapacityMIBCompliance3": ciscoSwitchHardwareCapacityMIBCompliance3,
       "ciscoSwitchHardwareCapacityMIBGroups": ciscoSwitchHardwareCapacityMIBGroups,
       "cshcMacUsageGroup": cshcMacUsageGroup,
       "cshcVpnCamUsageGroup": cshcVpnCamUsageGroup,
       "cshcFibTcamUsageGroup": cshcFibTcamUsageGroup,
       "cshcProtocolFibTcamUsageGroup": cshcProtocolFibTcamUsageGroup,
       "cshcAdjacencyUsageGroup": cshcAdjacencyUsageGroup,
       "cshcForwardingLoadGroup": cshcForwardingLoadGroup,
       "cshcModuleInterfaceDropsGroup": cshcModuleInterfaceDropsGroup,
       "cshcInterfaceBufferGroup": cshcInterfaceBufferGroup,
       "cshcInternalChannelGroup": cshcInternalChannelGroup,
       "cshcCPURateLimiterResourcesGroup": cshcCPURateLimiterResourcesGroup,
       "cshcIcamResourcesGroup": cshcIcamResourcesGroup,
       "cshcNetflowFlowMaskResourceGroup": cshcNetflowFlowMaskResourceGroup,
       "cshcFibTcamUsageExtGroup": cshcFibTcamUsageExtGroup,
       "cshcNetflowFlowResourceUsageGroup": cshcNetflowFlowResourceUsageGroup,
       "cshcMacUsageExtGroup": cshcMacUsageExtGroup,
       "cshcProtocolFibTcamUsageExtGroup": cshcProtocolFibTcamUsageExtGroup,
       "cshcAdjacencyResourceUsageGroup": cshcAdjacencyResourceUsageGroup,
       "cshcQosResourceUsageGroup": cshcQosResourceUsageGroup,
       "cshcModTopDropIfIndexListGroup": cshcModTopDropIfIndexListGroup,
       "cshcMetResourceUsageGroup": cshcMetResourceUsageGroup,
       "cshcProtocolFibTcamWidthTypeGroup": cshcProtocolFibTcamWidthTypeGroup}
)
