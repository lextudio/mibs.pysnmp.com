# SNMP MIB module (CISCO-CABLE-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-L2VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:37 2024
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

(CpwVcIDType,
 CpwVcType) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwVcIDType",
    "CpwVcType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCableL2vpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700)
)
ciscoCableL2vpnMIB.setRevisions(
        ("2009-06-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoCableL2vpnIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCableL2vpnMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableL2vpnMIBNotifs = _CiscoCableL2vpnMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 0)
)
_CiscoCableL2vpnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableL2vpnMIBObjects = _CiscoCableL2vpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1)
)
_Ccl2vpnMacVpnIdL2vpnIndexTable_Object = MibTable
ccl2vpnMacVpnIdL2vpnIndexTable = _Ccl2vpnMacVpnIdL2vpnIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 1)
)
if mibBuilder.loadTexts:
    ccl2vpnMacVpnIdL2vpnIndexTable.setStatus("current")
_Ccl2vpnMacVpnIdL2vpnIndexEntry_Object = MibTableRow
ccl2vpnMacVpnIdL2vpnIndexEntry = _Ccl2vpnMacVpnIdL2vpnIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 1, 1)
)
ccl2vpnMacVpnIdL2vpnIndexEntry.setIndexNames(
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnMac"),
    (1, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnVpnId"),
)
if mibBuilder.loadTexts:
    ccl2vpnMacVpnIdL2vpnIndexEntry.setStatus("current")
_Ccl2vpnMac_Type = MacAddress
_Ccl2vpnMac_Object = MibTableColumn
ccl2vpnMac = _Ccl2vpnMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 1, 1, 1),
    _Ccl2vpnMac_Type()
)
ccl2vpnMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnMac.setStatus("current")


class _Ccl2vpnVpnId_Type(OctetString):
    """Custom type ccl2vpnVpnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Ccl2vpnVpnId_Type.__name__ = "OctetString"
_Ccl2vpnVpnId_Object = MibTableColumn
ccl2vpnVpnId = _Ccl2vpnVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 1, 1, 2),
    _Ccl2vpnVpnId_Type()
)
ccl2vpnVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnVpnId.setStatus("current")
_Ccl2vpnMacVpnIdToL2vpnIndex_Type = CiscoCableL2vpnIndex
_Ccl2vpnMacVpnIdToL2vpnIndex_Object = MibTableColumn
ccl2vpnMacVpnIdToL2vpnIndex = _Ccl2vpnMacVpnIdToL2vpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 1, 1, 3),
    _Ccl2vpnMacVpnIdToL2vpnIndex_Type()
)
ccl2vpnMacVpnIdToL2vpnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnMacVpnIdToL2vpnIndex.setStatus("current")
_Ccl2vpnPWL2vpnIndexTable_Object = MibTable
ccl2vpnPWL2vpnIndexTable = _Ccl2vpnPWL2vpnIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2)
)
if mibBuilder.loadTexts:
    ccl2vpnPWL2vpnIndexTable.setStatus("current")
_Ccl2vpnPWL2vpnIndexEntry_Object = MibTableRow
ccl2vpnPWL2vpnIndexEntry = _Ccl2vpnPWL2vpnIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1)
)
ccl2vpnPWL2vpnIndexEntry.setIndexNames(
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnPseudoWireType"),
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnPeerIPAddressType"),
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnPeerIPAddress"),
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnVCID"),
)
if mibBuilder.loadTexts:
    ccl2vpnPWL2vpnIndexEntry.setStatus("current")
_Ccl2vpnPseudoWireType_Type = CpwVcType
_Ccl2vpnPseudoWireType_Object = MibTableColumn
ccl2vpnPseudoWireType = _Ccl2vpnPseudoWireType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1, 1),
    _Ccl2vpnPseudoWireType_Type()
)
ccl2vpnPseudoWireType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnPseudoWireType.setStatus("current")
_Ccl2vpnPeerIPAddressType_Type = InetAddressType
_Ccl2vpnPeerIPAddressType_Object = MibTableColumn
ccl2vpnPeerIPAddressType = _Ccl2vpnPeerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1, 2),
    _Ccl2vpnPeerIPAddressType_Type()
)
ccl2vpnPeerIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnPeerIPAddressType.setStatus("current")
_Ccl2vpnPeerIPAddress_Type = InetAddress
_Ccl2vpnPeerIPAddress_Object = MibTableColumn
ccl2vpnPeerIPAddress = _Ccl2vpnPeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1, 3),
    _Ccl2vpnPeerIPAddress_Type()
)
ccl2vpnPeerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnPeerIPAddress.setStatus("current")
_Ccl2vpnVCID_Type = CpwVcIDType
_Ccl2vpnVCID_Object = MibTableColumn
ccl2vpnVCID = _Ccl2vpnVCID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1, 4),
    _Ccl2vpnVCID_Type()
)
ccl2vpnVCID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnVCID.setStatus("current")
_Ccl2vpnPWToL2vpnIndex_Type = CiscoCableL2vpnIndex
_Ccl2vpnPWToL2vpnIndex_Object = MibTableColumn
ccl2vpnPWToL2vpnIndex = _Ccl2vpnPWToL2vpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 2, 1, 5),
    _Ccl2vpnPWToL2vpnIndex_Type()
)
ccl2vpnPWToL2vpnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWToL2vpnIndex.setStatus("current")
_Ccl2vpnL2vpnIndexPWTable_Object = MibTable
ccl2vpnL2vpnIndexPWTable = _Ccl2vpnL2vpnIndexPWTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3)
)
if mibBuilder.loadTexts:
    ccl2vpnL2vpnIndexPWTable.setStatus("current")
_Ccl2vpnL2vpnIndexPWEntry_Object = MibTableRow
ccl2vpnL2vpnIndexPWEntry = _Ccl2vpnL2vpnIndexPWEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1)
)
ccl2vpnL2vpnIndexPWEntry.setIndexNames(
    (0, "CISCO-CABLE-L2VPN-MIB", "ccl2vpnL2vpnIndex"),
)
if mibBuilder.loadTexts:
    ccl2vpnL2vpnIndexPWEntry.setStatus("current")
_Ccl2vpnL2vpnIndex_Type = CiscoCableL2vpnIndex
_Ccl2vpnL2vpnIndex_Object = MibTableColumn
ccl2vpnL2vpnIndex = _Ccl2vpnL2vpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 1),
    _Ccl2vpnL2vpnIndex_Type()
)
ccl2vpnL2vpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccl2vpnL2vpnIndex.setStatus("current")
_Ccl2vpnPWMAC_Type = MacAddress
_Ccl2vpnPWMAC_Object = MibTableColumn
ccl2vpnPWMAC = _Ccl2vpnPWMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 2),
    _Ccl2vpnPWMAC_Type()
)
ccl2vpnPWMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWMAC.setStatus("current")


class _Ccl2vpnPWVpnId_Type(OctetString):
    """Custom type ccl2vpnPWVpnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Ccl2vpnPWVpnId_Type.__name__ = "OctetString"
_Ccl2vpnPWVpnId_Object = MibTableColumn
ccl2vpnPWVpnId = _Ccl2vpnPWVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 3),
    _Ccl2vpnPWVpnId_Type()
)
ccl2vpnPWVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWVpnId.setStatus("current")
_Ccl2vpnPWPeerIPAddressType_Type = InetAddressType
_Ccl2vpnPWPeerIPAddressType_Object = MibTableColumn
ccl2vpnPWPeerIPAddressType = _Ccl2vpnPWPeerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 4),
    _Ccl2vpnPWPeerIPAddressType_Type()
)
ccl2vpnPWPeerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWPeerIPAddressType.setStatus("current")
_Ccl2vpnPWPeerIPAddress_Type = InetAddress
_Ccl2vpnPWPeerIPAddress_Object = MibTableColumn
ccl2vpnPWPeerIPAddress = _Ccl2vpnPWPeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 5),
    _Ccl2vpnPWPeerIPAddress_Type()
)
ccl2vpnPWPeerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWPeerIPAddress.setStatus("current")
_Ccl2vpnPWType_Type = CpwVcType
_Ccl2vpnPWType_Object = MibTableColumn
ccl2vpnPWType = _Ccl2vpnPWType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 6),
    _Ccl2vpnPWType_Type()
)
ccl2vpnPWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWType.setStatus("current")
_Ccl2vpnPWVCID_Type = CpwVcIDType
_Ccl2vpnPWVCID_Object = MibTableColumn
ccl2vpnPWVCID = _Ccl2vpnPWVCID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 1, 3, 1, 7),
    _Ccl2vpnPWVCID_Type()
)
ccl2vpnPWVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccl2vpnPWVCID.setStatus("current")
_CiscoCableL2vpnMIBConform_ObjectIdentity = ObjectIdentity
ciscoCableL2vpnMIBConform = _CiscoCableL2vpnMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 2)
)
_Ccl2vpnMIBCompliances_ObjectIdentity = ObjectIdentity
ccl2vpnMIBCompliances = _Ccl2vpnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 2, 1)
)
_Ccl2vpnMIBGroups_ObjectIdentity = ObjectIdentity
ccl2vpnMIBGroups = _Ccl2vpnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 2, 2)
)

# Managed Objects groups

ccl2vpnPWMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 2, 2, 1)
)
ccl2vpnPWMappingGroup.setObjects(
      *(("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWMAC"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWVpnId"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWPeerIPAddressType"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWPeerIPAddress"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWType"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWVCID"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnMacVpnIdToL2vpnIndex"),
        ("CISCO-CABLE-L2VPN-MIB", "ccl2vpnPWToL2vpnIndex"))
)
if mibBuilder.loadTexts:
    ccl2vpnPWMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccl2vpnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 700, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccl2vpnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-L2VPN-MIB",
    **{"CiscoCableL2vpnIndex": CiscoCableL2vpnIndex,
       "ciscoCableL2vpnMIB": ciscoCableL2vpnMIB,
       "ciscoCableL2vpnMIBNotifs": ciscoCableL2vpnMIBNotifs,
       "ciscoCableL2vpnMIBObjects": ciscoCableL2vpnMIBObjects,
       "ccl2vpnMacVpnIdL2vpnIndexTable": ccl2vpnMacVpnIdL2vpnIndexTable,
       "ccl2vpnMacVpnIdL2vpnIndexEntry": ccl2vpnMacVpnIdL2vpnIndexEntry,
       "ccl2vpnMac": ccl2vpnMac,
       "ccl2vpnVpnId": ccl2vpnVpnId,
       "ccl2vpnMacVpnIdToL2vpnIndex": ccl2vpnMacVpnIdToL2vpnIndex,
       "ccl2vpnPWL2vpnIndexTable": ccl2vpnPWL2vpnIndexTable,
       "ccl2vpnPWL2vpnIndexEntry": ccl2vpnPWL2vpnIndexEntry,
       "ccl2vpnPseudoWireType": ccl2vpnPseudoWireType,
       "ccl2vpnPeerIPAddressType": ccl2vpnPeerIPAddressType,
       "ccl2vpnPeerIPAddress": ccl2vpnPeerIPAddress,
       "ccl2vpnVCID": ccl2vpnVCID,
       "ccl2vpnPWToL2vpnIndex": ccl2vpnPWToL2vpnIndex,
       "ccl2vpnL2vpnIndexPWTable": ccl2vpnL2vpnIndexPWTable,
       "ccl2vpnL2vpnIndexPWEntry": ccl2vpnL2vpnIndexPWEntry,
       "ccl2vpnL2vpnIndex": ccl2vpnL2vpnIndex,
       "ccl2vpnPWMAC": ccl2vpnPWMAC,
       "ccl2vpnPWVpnId": ccl2vpnPWVpnId,
       "ccl2vpnPWPeerIPAddressType": ccl2vpnPWPeerIPAddressType,
       "ccl2vpnPWPeerIPAddress": ccl2vpnPWPeerIPAddress,
       "ccl2vpnPWType": ccl2vpnPWType,
       "ccl2vpnPWVCID": ccl2vpnPWVCID,
       "ciscoCableL2vpnMIBConform": ciscoCableL2vpnMIBConform,
       "ccl2vpnMIBCompliances": ccl2vpnMIBCompliances,
       "ccl2vpnMIBCompliance": ccl2vpnMIBCompliance,
       "ccl2vpnMIBGroups": ccl2vpnMIBGroups,
       "ccl2vpnPWMappingGroup": ccl2vpnPWMappingGroup}
)
