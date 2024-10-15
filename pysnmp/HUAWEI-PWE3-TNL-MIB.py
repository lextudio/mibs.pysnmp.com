# SNMP MIB module (HUAWEI-PWE3-TNL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PWE3-TNL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:40 2024
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

(HWEnableValue,
 HWL2VpnStateChangeReason,
 HWL2VpnVcEncapsType) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWEnableValue",
    "HWL2VpnStateChangeReason",
    "HWL2VpnVcEncapsType")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

(Bits,
 Bits,
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

hwL2VpnPwe3TnlExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwPwe3TunnelMIBObjects_ObjectIdentity = ObjectIdentity
hwPwe3TunnelMIBObjects = _HwPwe3TunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1)
)
_HwPwe3TunnelTable_Object = MibTable
hwPwe3TunnelTable = _HwPwe3TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwPwe3TunnelTable.setStatus("current")
_HwPwe3TunnelEntry_Object = MibTableRow
hwPwe3TunnelEntry = _HwPwe3TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1)
)
hwPwe3TunnelEntry.setIndexNames(
    (0, "HUAWEI-PWE3-TNL-MIB", "hwPwVcId"),
    (0, "HUAWEI-PWE3-TNL-MIB", "hwPwVcType"),
    (0, "HUAWEI-PWE3-TNL-MIB", "hwPwe3PeerTnlId"),
    (0, "HUAWEI-PWE3-TNL-MIB", "hwPwe3PwInlabel"),
)
if mibBuilder.loadTexts:
    hwPwe3TunnelEntry.setStatus("current")
_HwPwVcId_Type = Unsigned32
_HwPwVcId_Object = MibTableColumn
hwPwVcId = _HwPwVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 1),
    _HwPwVcId_Type()
)
hwPwVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwVcId.setStatus("current")
_HwPwVcType_Type = HWL2VpnVcEncapsType
_HwPwVcType_Object = MibTableColumn
hwPwVcType = _HwPwVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 2),
    _HwPwVcType_Type()
)
hwPwVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwVcType.setStatus("current")
_HwPwe3PwInlabel_Type = Unsigned32
_HwPwe3PwInlabel_Object = MibTableColumn
hwPwe3PwInlabel = _HwPwe3PwInlabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 3),
    _HwPwe3PwInlabel_Type()
)
hwPwe3PwInlabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwe3PwInlabel.setStatus("current")
_HwPwe3PeerTnlId_Type = Unsigned32
_HwPwe3PeerTnlId_Object = MibTableColumn
hwPwe3PeerTnlId = _HwPwe3PeerTnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 4),
    _HwPwe3PeerTnlId_Type()
)
hwPwe3PeerTnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwe3PeerTnlId.setStatus("current")
_HwPwe3TnlName_Type = OctetString
_HwPwe3TnlName_Object = MibTableColumn
hwPwe3TnlName = _HwPwe3TnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 5),
    _HwPwe3TnlName_Type()
)
hwPwe3TnlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3TnlName.setStatus("current")


class _HwPwe3TnlType_Type(Integer32):
    """Custom type hwPwe3TnlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPwe3TnlType_Type.__name__ = "Integer32"
_HwPwe3TnlType_Object = MibTableColumn
hwPwe3TnlType = _HwPwe3TnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 6),
    _HwPwe3TnlType_Type()
)
hwPwe3TnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3TnlType.setStatus("current")
_HwPwe3TnlSrcAddress_Type = IpAddress
_HwPwe3TnlSrcAddress_Object = MibTableColumn
hwPwe3TnlSrcAddress = _HwPwe3TnlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 7),
    _HwPwe3TnlSrcAddress_Type()
)
hwPwe3TnlSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3TnlSrcAddress.setStatus("current")
_HwPwe3TnlDestAddress_Type = IpAddress
_HwPwe3TnlDestAddress_Object = MibTableColumn
hwPwe3TnlDestAddress = _HwPwe3TnlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 8),
    _HwPwe3TnlDestAddress_Type()
)
hwPwe3TnlDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3TnlDestAddress.setStatus("current")
_HwPwe3LspIndex_Type = Integer32
_HwPwe3LspIndex_Object = MibTableColumn
hwPwe3LspIndex = _HwPwe3LspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 9),
    _HwPwe3LspIndex_Type()
)
hwPwe3LspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspIndex.setStatus("current")
_HwPwe3LspOutIf_Type = OctetString
_HwPwe3LspOutIf_Object = MibTableColumn
hwPwe3LspOutIf = _HwPwe3LspOutIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 10),
    _HwPwe3LspOutIf_Type()
)
hwPwe3LspOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspOutIf.setStatus("current")


class _HwPwe3LspOutLabel_Type(Integer32):
    """Custom type hwPwe3LspOutLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPwe3LspOutLabel_Type.__name__ = "Integer32"
_HwPwe3LspOutLabel_Object = MibTableColumn
hwPwe3LspOutLabel = _HwPwe3LspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 11),
    _HwPwe3LspOutLabel_Type()
)
hwPwe3LspOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspOutLabel.setStatus("current")
_HwPwe3LspNextHop_Type = IpAddress
_HwPwe3LspNextHop_Object = MibTableColumn
hwPwe3LspNextHop = _HwPwe3LspNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 12),
    _HwPwe3LspNextHop_Type()
)
hwPwe3LspNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspNextHop.setStatus("current")
_HwPwe3LspFec_Type = IpAddress
_HwPwe3LspFec_Object = MibTableColumn
hwPwe3LspFec = _HwPwe3LspFec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 13),
    _HwPwe3LspFec_Type()
)
hwPwe3LspFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspFec.setStatus("current")
_HwPwe3LspFecPfxLen_Type = Integer32
_HwPwe3LspFecPfxLen_Object = MibTableColumn
hwPwe3LspFecPfxLen = _HwPwe3LspFecPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 14),
    _HwPwe3LspFecPfxLen_Type()
)
hwPwe3LspFecPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspFecPfxLen.setStatus("current")
_HwPwe3LspIsBackup_Type = TruthValue
_HwPwe3LspIsBackup_Object = MibTableColumn
hwPwe3LspIsBackup = _HwPwe3LspIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 15),
    _HwPwe3LspIsBackup_Type()
)
hwPwe3LspIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspIsBackup.setStatus("current")
_HwPwe3PwOutLabel_Type = Integer32
_HwPwe3PwOutLabel_Object = MibTableColumn
hwPwe3PwOutLabel = _HwPwe3PwOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 16),
    _HwPwe3PwOutLabel_Type()
)
hwPwe3PwOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3PwOutLabel.setStatus("current")
_HwPwe3IsBalance_Type = TruthValue
_HwPwe3IsBalance_Object = MibTableColumn
hwPwe3IsBalance = _HwPwe3IsBalance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 17),
    _HwPwe3IsBalance_Type()
)
hwPwe3IsBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3IsBalance.setStatus("current")
_HwPwe3LspTunnelId_Type = Integer32
_HwPwe3LspTunnelId_Object = MibTableColumn
hwPwe3LspTunnelId = _HwPwe3LspTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 18),
    _HwPwe3LspTunnelId_Type()
)
hwPwe3LspTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspTunnelId.setStatus("current")


class _HwPwe3LspSignType_Type(Integer32):
    """Custom type hwPwe3LspSignType based on Integer32"""
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


_HwPwe3LspSignType_Type.__name__ = "Integer32"
_HwPwe3LspSignType_Object = MibTableColumn
hwPwe3LspSignType = _HwPwe3LspSignType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 19),
    _HwPwe3LspSignType_Type()
)
hwPwe3LspSignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3LspSignType.setStatus("current")
_HwPwe3TnlRowStatus_Type = RowStatus
_HwPwe3TnlRowStatus_Object = MibTableColumn
hwPwe3TnlRowStatus = _HwPwe3TnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 1, 1, 1, 50),
    _HwPwe3TnlRowStatus_Type()
)
hwPwe3TnlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwe3TnlRowStatus.setStatus("current")
_HwPwe3TunnelMIBTraps_ObjectIdentity = ObjectIdentity
hwPwe3TunnelMIBTraps = _HwPwe3TunnelMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 2)
)
_HwPwe3TunnelMIBConformance_ObjectIdentity = ObjectIdentity
hwPwe3TunnelMIBConformance = _HwPwe3TunnelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 3)
)
_HwPwe3TunnelMIBCompliances_ObjectIdentity = ObjectIdentity
hwPwe3TunnelMIBCompliances = _HwPwe3TunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 3, 1)
)
_HwPwe3TunnelMIBGroups_ObjectIdentity = ObjectIdentity
hwPwe3TunnelMIBGroups = _HwPwe3TunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 3, 2)
)

# Managed Objects groups

hwPwe3TunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 3, 2, 1)
)
hwPwe3TunnelGroup.setObjects(
      *(("HUAWEI-PWE3-TNL-MIB", "hwPwe3TnlName"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3TnlType"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3TnlSrcAddress"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3TnlDestAddress"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspIndex"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspOutIf"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspOutLabel"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspNextHop"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspFec"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspFecPfxLen"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspIsBackup"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3PwOutLabel"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3IsBalance"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspTunnelId"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3LspSignType"),
        ("HUAWEI-PWE3-TNL-MIB", "hwPwe3TnlRowStatus"))
)
if mibBuilder.loadTexts:
    hwPwe3TunnelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPwe3TunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwPwe3TunnelMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PWE3-TNL-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2VpnPwe3TnlExt": hwL2VpnPwe3TnlExt,
       "hwPwe3TunnelMIBObjects": hwPwe3TunnelMIBObjects,
       "hwPwe3TunnelTable": hwPwe3TunnelTable,
       "hwPwe3TunnelEntry": hwPwe3TunnelEntry,
       "hwPwVcId": hwPwVcId,
       "hwPwVcType": hwPwVcType,
       "hwPwe3PwInlabel": hwPwe3PwInlabel,
       "hwPwe3PeerTnlId": hwPwe3PeerTnlId,
       "hwPwe3TnlName": hwPwe3TnlName,
       "hwPwe3TnlType": hwPwe3TnlType,
       "hwPwe3TnlSrcAddress": hwPwe3TnlSrcAddress,
       "hwPwe3TnlDestAddress": hwPwe3TnlDestAddress,
       "hwPwe3LspIndex": hwPwe3LspIndex,
       "hwPwe3LspOutIf": hwPwe3LspOutIf,
       "hwPwe3LspOutLabel": hwPwe3LspOutLabel,
       "hwPwe3LspNextHop": hwPwe3LspNextHop,
       "hwPwe3LspFec": hwPwe3LspFec,
       "hwPwe3LspFecPfxLen": hwPwe3LspFecPfxLen,
       "hwPwe3LspIsBackup": hwPwe3LspIsBackup,
       "hwPwe3PwOutLabel": hwPwe3PwOutLabel,
       "hwPwe3IsBalance": hwPwe3IsBalance,
       "hwPwe3LspTunnelId": hwPwe3LspTunnelId,
       "hwPwe3LspSignType": hwPwe3LspSignType,
       "hwPwe3TnlRowStatus": hwPwe3TnlRowStatus,
       "hwPwe3TunnelMIBTraps": hwPwe3TunnelMIBTraps,
       "hwPwe3TunnelMIBConformance": hwPwe3TunnelMIBConformance,
       "hwPwe3TunnelMIBCompliances": hwPwe3TunnelMIBCompliances,
       "hwPwe3TunnelMIBCompliance": hwPwe3TunnelMIBCompliance,
       "hwPwe3TunnelMIBGroups": hwPwe3TunnelMIBGroups,
       "hwPwe3TunnelGroup": hwPwe3TunnelGroup}
)
