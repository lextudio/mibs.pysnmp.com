# SNMP MIB module (HUAWEI-VPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:35 2024
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

(hwMpls,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwMpls")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwMplsVpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class L2VpnState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("l2VpnStateDown", 0),
          ("l2VpnStateUp", 1))
    )



class L2VpnEncapsType(Integer32, TextualConvention):
    status = "current"
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
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("l2VpnEncapsAtmAal5", 2),
          ("l2VpnEncapsAtmCellTransport", 3),
          ("l2VpnEncapsAtmCellVcc", 9),
          ("l2VpnEncapsAtmCellVpc", 10),
          ("l2VpnEncapsCem", 8),
          ("l2VpnEncapsEthernet", 5),
          ("l2VpnEncapsFr", 1),
          ("l2VpnEncapsHdlc", 6),
          ("l2VpnEncapsIpInterworking", 64),
          ("l2VpnEncapsMpls", 11),
          ("l2VpnEncapsPpp", 7),
          ("l2VpnEncapsUnsupported", 255),
          ("l2VpnEncapsVlan", 4),
          ("l2VpnEncapsVpls", 12))
    )



class L2VpnDownReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("l2VpnDeleteVC", 6),
          ("l2VpnEncapIfDown", 5),
          ("l2VpnLabelRelease", 4),
          ("l2VpnLabelWithdraw", 3),
          ("l2VpnReasonOk", 0),
          ("l2VpnSessionDown", 1),
          ("l2VpnTunnelDown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwVplsMIBObjects_ObjectIdentity = ObjectIdentity
hwVplsMIBObjects = _HwVplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1)
)
_HwVplsVCStateTable_Object = MibTable
hwVplsVCStateTable = _HwVplsVCStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsVCStateTable.setStatus("current")
_HwVplsVCStateEntry_Object = MibTableRow
hwVplsVCStateEntry = _HwVplsVCStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1)
)
hwVplsVCStateEntry.setIndexNames(
    (0, "HUAWEI-VPLS-MIB", "hwVplsVCId"),
    (0, "HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"),
)
if mibBuilder.loadTexts:
    hwVplsVCStateEntry.setStatus("current")


class _HwVplsVCId_Type(Gauge32):
    """Custom type hwVplsVCId based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwVplsVCId_Type.__name__ = "Gauge32"
_HwVplsVCId_Object = MibTableColumn
hwVplsVCId = _HwVplsVCId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 1),
    _HwVplsVCId_Type()
)
hwVplsVCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCId.setStatus("current")
_HwVplsVCEncapsType_Type = L2VpnEncapsType
_HwVplsVCEncapsType_Object = MibTableColumn
hwVplsVCEncapsType = _HwVplsVCEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 2),
    _HwVplsVCEncapsType_Type()
)
hwVplsVCEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCEncapsType.setStatus("current")
_HwVplsVCClientIf_Type = InterfaceIndex
_HwVplsVCClientIf_Object = MibTableColumn
hwVplsVCClientIf = _HwVplsVCClientIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 3),
    _HwVplsVCClientIf_Type()
)
hwVplsVCClientIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCClientIf.setStatus("current")
_HwVplsVCLocalLabel_Type = Gauge32
_HwVplsVCLocalLabel_Object = MibTableColumn
hwVplsVCLocalLabel = _HwVplsVCLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 4),
    _HwVplsVCLocalLabel_Type()
)
hwVplsVCLocalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCLocalLabel.setStatus("current")
_HwVplsVCRemoteLabel_Type = Gauge32
_HwVplsVCRemoteLabel_Object = MibTableColumn
hwVplsVCRemoteLabel = _HwVplsVCRemoteLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 5),
    _HwVplsVCRemoteLabel_Type()
)
hwVplsVCRemoteLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCRemoteLabel.setStatus("current")
_HwVplsVCTunnelLabel_Type = Gauge32
_HwVplsVCTunnelLabel_Object = MibTableColumn
hwVplsVCTunnelLabel = _HwVplsVCTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 6),
    _HwVplsVCTunnelLabel_Type()
)
hwVplsVCTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCTunnelLabel.setStatus("current")
_HwVplsVCL2Mtu_Type = Integer32
_HwVplsVCL2Mtu_Object = MibTableColumn
hwVplsVCL2Mtu = _HwVplsVCL2Mtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 7),
    _HwVplsVCL2Mtu_Type()
)
hwVplsVCL2Mtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCL2Mtu.setStatus("current")
_HwVplsVCState_Type = L2VpnState
_HwVplsVCState_Object = MibTableColumn
hwVplsVCState = _HwVplsVCState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 8),
    _HwVplsVCState_Type()
)
hwVplsVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCState.setStatus("current")
_HwVplsVCDownReason_Type = L2VpnDownReason
_HwVplsVCDownReason_Object = MibTableColumn
hwVplsVCDownReason = _HwVplsVCDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 9),
    _HwVplsVCDownReason_Type()
)
hwVplsVCDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVCDownReason.setStatus("current")
_HwVplsMIBTraps_ObjectIdentity = ObjectIdentity
hwVplsMIBTraps = _HwVplsMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2)
)
_HwVplsMIBConformance_ObjectIdentity = ObjectIdentity
hwVplsMIBConformance = _HwVplsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3)
)
_HwVplsMIBCompliances_ObjectIdentity = ObjectIdentity
hwVplsMIBCompliances = _HwVplsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1)
)
_HwVplsMIBGroups_ObjectIdentity = ObjectIdentity
hwVplsMIBGroups = _HwVplsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2)
)

# Managed Objects groups

hwVplsVCStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2, 1)
)
hwVplsVCStateGroup.setObjects(
      *(("HUAWEI-VPLS-MIB", "hwVplsVCId"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCClientIf"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCLocalLabel"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCRemoteLabel"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCTunnelLabel"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCL2Mtu"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCState"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
)
if mibBuilder.loadTexts:
    hwVplsVCStateGroup.setStatus("current")


# Notification objects

hwVplsVCStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 1)
)
hwVplsVCStateDown.setObjects(
      *(("HUAWEI-VPLS-MIB", "hwVplsVCId"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
)
if mibBuilder.loadTexts:
    hwVplsVCStateDown.setStatus(
        "current"
    )

hwVplsVCStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 2)
)
hwVplsVCStateUp.setObjects(
      *(("HUAWEI-VPLS-MIB", "hwVplsVCId"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"),
        ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
)
if mibBuilder.loadTexts:
    hwVplsVCStateUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hwVplsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVplsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VPLS-MIB",
    **{"L2VpnState": L2VpnState,
       "L2VpnEncapsType": L2VpnEncapsType,
       "L2VpnDownReason": L2VpnDownReason,
       "hwMplsVpls": hwMplsVpls,
       "hwVplsMIBObjects": hwVplsMIBObjects,
       "hwVplsVCStateTable": hwVplsVCStateTable,
       "hwVplsVCStateEntry": hwVplsVCStateEntry,
       "hwVplsVCId": hwVplsVCId,
       "hwVplsVCEncapsType": hwVplsVCEncapsType,
       "hwVplsVCClientIf": hwVplsVCClientIf,
       "hwVplsVCLocalLabel": hwVplsVCLocalLabel,
       "hwVplsVCRemoteLabel": hwVplsVCRemoteLabel,
       "hwVplsVCTunnelLabel": hwVplsVCTunnelLabel,
       "hwVplsVCL2Mtu": hwVplsVCL2Mtu,
       "hwVplsVCState": hwVplsVCState,
       "hwVplsVCDownReason": hwVplsVCDownReason,
       "hwVplsMIBTraps": hwVplsMIBTraps,
       "hwVplsVCStateDown": hwVplsVCStateDown,
       "hwVplsVCStateUp": hwVplsVCStateUp,
       "hwVplsMIBConformance": hwVplsMIBConformance,
       "hwVplsMIBCompliances": hwVplsMIBCompliances,
       "hwVplsMIBCompliance": hwVplsMIBCompliance,
       "hwVplsMIBGroups": hwVplsMIBGroups,
       "hwVplsVCStateGroup": hwVplsVCStateGroup}
)
