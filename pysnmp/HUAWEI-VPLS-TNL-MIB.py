# SNMP MIB module (HUAWEI-VPLS-TNL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VPLS-TNL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:36 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hwL2VpnVplsTnlExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwVplsTunnelMIBObjects_ObjectIdentity = ObjectIdentity
hwVplsTunnelMIBObjects = _HwVplsTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1)
)
_HwVplsTunnelTable_Object = MibTable
hwVplsTunnelTable = _HwVplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsTunnelTable.setStatus("current")
_HwVplsTunnelEntry_Object = MibTableRow
hwVplsTunnelEntry = _HwVplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1)
)
hwVplsTunnelEntry.setIndexNames(
    (0, "HUAWEI-VPLS-TNL-MIB", "hwVplsVsiName"),
    (0, "HUAWEI-VPLS-TNL-MIB", "hwVplsNexthopPeer"),
    (0, "HUAWEI-VPLS-TNL-MIB", "hwVplsSiteOrPwId"),
    (0, "HUAWEI-VPLS-TNL-MIB", "hwVplsPeerTnlId"),
)
if mibBuilder.loadTexts:
    hwVplsTunnelEntry.setStatus("current")


class _HwVplsVsiName_Type(DisplayString):
    """Custom type hwVplsVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVplsVsiName_Type.__name__ = "DisplayString"
_HwVplsVsiName_Object = MibTableColumn
hwVplsVsiName = _HwVplsVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 1),
    _HwVplsVsiName_Type()
)
hwVplsVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsVsiName.setStatus("current")
_HwVplsNexthopPeer_Type = IpAddress
_HwVplsNexthopPeer_Object = MibTableColumn
hwVplsNexthopPeer = _HwVplsNexthopPeer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 2),
    _HwVplsNexthopPeer_Type()
)
hwVplsNexthopPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsNexthopPeer.setStatus("current")
_HwVplsSiteOrPwId_Type = Unsigned32
_HwVplsSiteOrPwId_Object = MibTableColumn
hwVplsSiteOrPwId = _HwVplsSiteOrPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 3),
    _HwVplsSiteOrPwId_Type()
)
hwVplsSiteOrPwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsSiteOrPwId.setStatus("current")
_HwVplsPeerTnlId_Type = Unsigned32
_HwVplsPeerTnlId_Object = MibTableColumn
hwVplsPeerTnlId = _HwVplsPeerTnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 4),
    _HwVplsPeerTnlId_Type()
)
hwVplsPeerTnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsPeerTnlId.setStatus("current")
_HwVplsTnlName_Type = OctetString
_HwVplsTnlName_Object = MibTableColumn
hwVplsTnlName = _HwVplsTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 5),
    _HwVplsTnlName_Type()
)
hwVplsTnlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsTnlName.setStatus("current")


class _HwVplsTnlType_Type(Integer32):
    """Custom type hwVplsTnlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crlsp", 2),
          ("lsp", 1),
          ("other", 3))
    )


_HwVplsTnlType_Type.__name__ = "Integer32"
_HwVplsTnlType_Object = MibTableColumn
hwVplsTnlType = _HwVplsTnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 6),
    _HwVplsTnlType_Type()
)
hwVplsTnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsTnlType.setStatus("current")
_HwVplsTnlSrcAddress_Type = IpAddress
_HwVplsTnlSrcAddress_Object = MibTableColumn
hwVplsTnlSrcAddress = _HwVplsTnlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 7),
    _HwVplsTnlSrcAddress_Type()
)
hwVplsTnlSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsTnlSrcAddress.setStatus("current")
_HwVplsTnlDestAddress_Type = IpAddress
_HwVplsTnlDestAddress_Object = MibTableColumn
hwVplsTnlDestAddress = _HwVplsTnlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 8),
    _HwVplsTnlDestAddress_Type()
)
hwVplsTnlDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsTnlDestAddress.setStatus("current")
_HwVplsLspIndex_Type = Integer32
_HwVplsLspIndex_Object = MibTableColumn
hwVplsLspIndex = _HwVplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 9),
    _HwVplsLspIndex_Type()
)
hwVplsLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspIndex.setStatus("current")
_HwVplsLspOutIf_Type = OctetString
_HwVplsLspOutIf_Object = MibTableColumn
hwVplsLspOutIf = _HwVplsLspOutIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 10),
    _HwVplsLspOutIf_Type()
)
hwVplsLspOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspOutIf.setStatus("current")


class _HwVplsLspOutLabel_Type(Integer32):
    """Custom type hwVplsLspOutLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVplsLspOutLabel_Type.__name__ = "Integer32"
_HwVplsLspOutLabel_Object = MibTableColumn
hwVplsLspOutLabel = _HwVplsLspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 11),
    _HwVplsLspOutLabel_Type()
)
hwVplsLspOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspOutLabel.setStatus("current")
_HwVplsLspNextHop_Type = IpAddress
_HwVplsLspNextHop_Object = MibTableColumn
hwVplsLspNextHop = _HwVplsLspNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 12),
    _HwVplsLspNextHop_Type()
)
hwVplsLspNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspNextHop.setStatus("current")
_HwVplsLspFec_Type = IpAddress
_HwVplsLspFec_Object = MibTableColumn
hwVplsLspFec = _HwVplsLspFec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 13),
    _HwVplsLspFec_Type()
)
hwVplsLspFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspFec.setStatus("current")
_HwVplsLspFecPfxLen_Type = Integer32
_HwVplsLspFecPfxLen_Object = MibTableColumn
hwVplsLspFecPfxLen = _HwVplsLspFecPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 14),
    _HwVplsLspFecPfxLen_Type()
)
hwVplsLspFecPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspFecPfxLen.setStatus("current")
_HwVplsLspIsBackup_Type = TruthValue
_HwVplsLspIsBackup_Object = MibTableColumn
hwVplsLspIsBackup = _HwVplsLspIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 15),
    _HwVplsLspIsBackup_Type()
)
hwVplsLspIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspIsBackup.setStatus("current")
_HwVplsIsBalance_Type = TruthValue
_HwVplsIsBalance_Object = MibTableColumn
hwVplsIsBalance = _HwVplsIsBalance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 16),
    _HwVplsIsBalance_Type()
)
hwVplsIsBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsIsBalance.setStatus("current")
_HwVplsLspTunnelId_Type = Integer32
_HwVplsLspTunnelId_Object = MibTableColumn
hwVplsLspTunnelId = _HwVplsLspTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 17),
    _HwVplsLspTunnelId_Type()
)
hwVplsLspTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspTunnelId.setStatus("current")


class _HwVplsLspSignType_Type(Integer32):
    """Custom type hwVplsLspSignType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 4),
          ("bgpIpv6", 8),
          ("crLdp", 2),
          ("crStatic", 7),
          ("l2vpnIpv6", 10),
          ("l3vpn", 5),
          ("ldp", 1),
          ("maxSignal", 20),
          ("rsvp", 3),
          ("static", 6),
          ("staticHa", 9))
    )


_HwVplsLspSignType_Type.__name__ = "Integer32"
_HwVplsLspSignType_Object = MibTableColumn
hwVplsLspSignType = _HwVplsLspSignType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 18),
    _HwVplsLspSignType_Type()
)
hwVplsLspSignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsLspSignType.setStatus("current")
_HwVplsTnlRowStatus_Type = RowStatus
_HwVplsTnlRowStatus_Object = MibTableColumn
hwVplsTnlRowStatus = _HwVplsTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 1, 1, 1, 50),
    _HwVplsTnlRowStatus_Type()
)
hwVplsTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVplsTnlRowStatus.setStatus("current")
_HwVplsTunnelMIBTraps_ObjectIdentity = ObjectIdentity
hwVplsTunnelMIBTraps = _HwVplsTunnelMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 2)
)
_HwVplsTunnelMIBConformance_ObjectIdentity = ObjectIdentity
hwVplsTunnelMIBConformance = _HwVplsTunnelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 3)
)
_HwVplsTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
hwVplsTunnelMIBCompliances = _HwVplsTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 3, 1)
)
_HwVplsTunnelMIBGroups_ObjectIdentity = ObjectIdentity
hwVplsTunnelMIBGroups = _HwVplsTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 3, 2)
)

# Managed Objects groups

hwVplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 3, 2, 1)
)
hwVplsTunnelGroup.setObjects(
      *(("HUAWEI-VPLS-TNL-MIB", "hwVplsTnlName"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsTnlType"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsTnlSrcAddress"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsTnlDestAddress"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspOutIf"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspOutLabel"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspNextHop"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspFec"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspFecPfxLen"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspIsBackup"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsIsBalance"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspTunnelId"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsLspSignType"),
        ("HUAWEI-VPLS-TNL-MIB", "hwVplsTnlRowStatus"))
)
if mibBuilder.loadTexts:
    hwVplsTunnelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwVplsTunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsTunnelMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VPLS-TNL-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2VpnVplsTnlExt": hwL2VpnVplsTnlExt,
       "hwVplsTunnelMIBObjects": hwVplsTunnelMIBObjects,
       "hwVplsTunnelTable": hwVplsTunnelTable,
       "hwVplsTunnelEntry": hwVplsTunnelEntry,
       "hwVplsVsiName": hwVplsVsiName,
       "hwVplsNexthopPeer": hwVplsNexthopPeer,
       "hwVplsSiteOrPwId": hwVplsSiteOrPwId,
       "hwVplsPeerTnlId": hwVplsPeerTnlId,
       "hwVplsTnlName": hwVplsTnlName,
       "hwVplsTnlType": hwVplsTnlType,
       "hwVplsTnlSrcAddress": hwVplsTnlSrcAddress,
       "hwVplsTnlDestAddress": hwVplsTnlDestAddress,
       "hwVplsLspIndex": hwVplsLspIndex,
       "hwVplsLspOutIf": hwVplsLspOutIf,
       "hwVplsLspOutLabel": hwVplsLspOutLabel,
       "hwVplsLspNextHop": hwVplsLspNextHop,
       "hwVplsLspFec": hwVplsLspFec,
       "hwVplsLspFecPfxLen": hwVplsLspFecPfxLen,
       "hwVplsLspIsBackup": hwVplsLspIsBackup,
       "hwVplsIsBalance": hwVplsIsBalance,
       "hwVplsLspTunnelId": hwVplsLspTunnelId,
       "hwVplsLspSignType": hwVplsLspSignType,
       "hwVplsTnlRowStatus": hwVplsTnlRowStatus,
       "hwVplsTunnelMIBTraps": hwVplsTunnelMIBTraps,
       "hwVplsTunnelMIBConformance": hwVplsTunnelMIBConformance,
       "hwVplsTunnelMIBCompliances": hwVplsTunnelMIBCompliances,
       "hwVplsTunnelMIBCompliance": hwVplsTunnelMIBCompliance,
       "hwVplsTunnelMIBGroups": hwVplsTunnelMIBGroups,
       "hwVplsTunnelGroup": hwVplsTunnelGroup}
)
