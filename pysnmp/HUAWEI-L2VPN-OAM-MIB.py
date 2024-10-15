# SNMP MIB module (HUAWEI-L2VPN-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2VPN-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:26 2024
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

(HWL2VpnVcEncapsType,) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWL2VpnVcEncapsType")

(InterfaceIndexOrZero,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifName")

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

hwL2vpnOamTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9)
)
hwL2vpnOamTrap.setRevisions(
        ("2013-09-05 14:00",
         "2013-05-13 13:30",
         "2013-03-25 14:52")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwL2vpnOamTrapMIBObjects_ObjectIdentity = ObjectIdentity
hwL2vpnOamTrapMIBObjects = _HwL2vpnOamTrapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1)
)


class _HwL2vpnServiceType_Type(Integer32):
    """Custom type hwL2vpnServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vplsPw", 1),
          ("vpwsPw", 0))
    )


_HwL2vpnServiceType_Type.__name__ = "Integer32"
_HwL2vpnServiceType_Object = MibScalar
hwL2vpnServiceType = _HwL2vpnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 1),
    _HwL2vpnServiceType_Type()
)
hwL2vpnServiceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnServiceType.setStatus("current")


class _HwL2vpnProtocolType_Type(Integer32):
    """Custom type hwL2vpnProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("ldp", 1),
          ("static", 0))
    )


_HwL2vpnProtocolType_Type.__name__ = "Integer32"
_HwL2vpnProtocolType_Object = MibScalar
hwL2vpnProtocolType = _HwL2vpnProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 2),
    _HwL2vpnProtocolType_Type()
)
hwL2vpnProtocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnProtocolType.setStatus("current")
_HwL2vpnVcID_Type = Unsigned32
_HwL2vpnVcID_Object = MibScalar
hwL2vpnVcID = _HwL2vpnVcID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 3),
    _HwL2vpnVcID_Type()
)
hwL2vpnVcID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnVcID.setStatus("current")
_HwL2vpnVcType_Type = HWL2VpnVcEncapsType
_HwL2vpnVcType_Object = MibScalar
hwL2vpnVcType = _HwL2vpnVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 4),
    _HwL2vpnVcType_Type()
)
hwL2vpnVcType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnVcType.setStatus("current")
_HwL2vpnPeerAddr_Type = IpAddress
_HwL2vpnPeerAddr_Object = MibScalar
hwL2vpnPeerAddr = _HwL2vpnPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 5),
    _HwL2vpnPeerAddr_Type()
)
hwL2vpnPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnPeerAddr.setStatus("current")
_HwL2vpnIfIndex_Type = InterfaceIndexOrZero
_HwL2vpnIfIndex_Object = MibScalar
hwL2vpnIfIndex = _HwL2vpnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 6),
    _HwL2vpnIfIndex_Type()
)
hwL2vpnIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnIfIndex.setStatus("current")


class _HwL2vpnPwMaster_Type(Integer32):
    """Custom type hwL2vpnPwMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("second", 2))
    )


_HwL2vpnPwMaster_Type.__name__ = "Integer32"
_HwL2vpnPwMaster_Object = MibScalar
hwL2vpnPwMaster = _HwL2vpnPwMaster_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 7),
    _HwL2vpnPwMaster_Type()
)
hwL2vpnPwMaster.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnPwMaster.setStatus("current")
_HwL2vpnRmtSiteID_Type = Unsigned32
_HwL2vpnRmtSiteID_Object = MibScalar
hwL2vpnRmtSiteID = _HwL2vpnRmtSiteID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 8),
    _HwL2vpnRmtSiteID_Type()
)
hwL2vpnRmtSiteID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnRmtSiteID.setStatus("current")
_HwL2vpnInLabel_Type = Unsigned32
_HwL2vpnInLabel_Object = MibScalar
hwL2vpnInLabel = _HwL2vpnInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 9),
    _HwL2vpnInLabel_Type()
)
hwL2vpnInLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnInLabel.setStatus("current")
_HwL2vpnOutLabel_Type = Unsigned32
_HwL2vpnOutLabel_Object = MibScalar
hwL2vpnOutLabel = _HwL2vpnOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 10),
    _HwL2vpnOutLabel_Type()
)
hwL2vpnOutLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnOutLabel.setStatus("current")
_HwL2vpnIfName_Type = OctetString
_HwL2vpnIfName_Object = MibScalar
hwL2vpnIfName = _HwL2vpnIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 11),
    _HwL2vpnIfName_Type()
)
hwL2vpnIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnIfName.setStatus("current")
_HwL2vpnVsiName_Type = OctetString
_HwL2vpnVsiName_Object = MibScalar
hwL2vpnVsiName = _HwL2vpnVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 1, 12),
    _HwL2vpnVsiName_Type()
)
hwL2vpnVsiName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2vpnVsiName.setStatus("current")
_HwL2vpnOamMIBTraps_ObjectIdentity = ObjectIdentity
hwL2vpnOamMIBTraps = _HwL2vpnOamMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2)
)
_HwL2vpnOamConformance_ObjectIdentity = ObjectIdentity
hwL2vpnOamConformance = _HwL2vpnOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3)
)
_HwL2vpnOamMIBCompliances_ObjectIdentity = ObjectIdentity
hwL2vpnOamMIBCompliances = _HwL2vpnOamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3, 1)
)
_HwL2vpnOamGroups_ObjectIdentity = ObjectIdentity
hwL2vpnOamGroups = _HwL2vpnOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3, 2)
)

# Managed Objects groups

hwL2vpnOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3, 2, 1)
)
hwL2vpnOamGroup.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamGroup.setStatus("current")


# Notification objects

hwL2vpnOamDloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 1)
)
hwL2vpnOamDloc.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamDloc.setStatus(
        "current"
    )

hwL2vpnOamDlocClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 2)
)
hwL2vpnOamDlocClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamDlocClear.setStatus(
        "current"
    )

hwL2vpnOamSd1Near = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 3)
)
hwL2vpnOamSd1Near.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd1Near.setStatus(
        "current"
    )

hwL2vpnOamSd1NearClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 4)
)
hwL2vpnOamSd1NearClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd1NearClear.setStatus(
        "current"
    )

hwL2vpnOamRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 5)
)
hwL2vpnOamRdi.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamRdi.setStatus(
        "current"
    )

hwL2vpnOamRdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 6)
)
hwL2vpnOamRdiClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamRdiClear.setStatus(
        "current"
    )

hwL2vpnOamMeg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 7)
)
hwL2vpnOamMeg.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMeg.setStatus(
        "current"
    )

hwL2vpnOamMegClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 8)
)
hwL2vpnOamMegClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMegClear.setStatus(
        "current"
    )

hwL2vpnOamMep = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 9)
)
hwL2vpnOamMep.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMep.setStatus(
        "current"
    )

hwL2vpnOamMepClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 10)
)
hwL2vpnOamMepClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMepClear.setStatus(
        "current"
    )

hwL2vpnOamPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 11)
)
hwL2vpnOamPeriod.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamPeriod.setStatus(
        "current"
    )

hwL2vpnOamPeriodClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 12)
)
hwL2vpnOamPeriodClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamPeriodClear.setStatus(
        "current"
    )

hwL2vpnOamAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 13)
)
hwL2vpnOamAis.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamAis.setStatus(
        "current"
    )

hwL2vpnOamAisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 14)
)
hwL2vpnOamAisClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamAisClear.setStatus(
        "current"
    )

hwL2vpnOamSd2Near = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 15)
)
hwL2vpnOamSd2Near.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd2Near.setStatus(
        "current"
    )

hwL2vpnOamSd2NearClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 16)
)
hwL2vpnOamSd2NearClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd2NearClear.setStatus(
        "current"
    )

hwL2vpnOamLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 17)
)
hwL2vpnOamLck.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamLck.setStatus(
        "current"
    )

hwL2vpnOamLckClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 18)
)
hwL2vpnOamLckClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamLckClear.setStatus(
        "current"
    )

hwL2vpnOamCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 19)
)
hwL2vpnOamCsf.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamCsf.setStatus(
        "current"
    )

hwL2vpnOamCsfClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 20)
)
hwL2vpnOamCsfClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamCsfClear.setStatus(
        "current"
    )

hwL2vpnOamExcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 21)
)
hwL2vpnOamExcess.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamExcess.setStatus(
        "current"
    )

hwL2vpnOamExcessClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 22)
)
hwL2vpnOamExcessClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamExcessClear.setStatus(
        "current"
    )

hwL2vpnOamMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 23)
)
hwL2vpnOamMismatch.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMismatch.setStatus(
        "current"
    )

hwL2vpnOamMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 24)
)
hwL2vpnOamMismatchClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMismatchClear.setStatus(
        "current"
    )

hwL2vpnOamMismerge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 25)
)
hwL2vpnOamMismerge.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMismerge.setStatus(
        "current"
    )

hwL2vpnOamMismergeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 26)
)
hwL2vpnOamMismergeClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamMismergeClear.setStatus(
        "current"
    )

hwL2vpnOamFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 27)
)
hwL2vpnOamFail.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamFail.setStatus(
        "current"
    )

hwL2vpnOamFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 28)
)
hwL2vpnOamFailClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamFailClear.setStatus(
        "current"
    )

hwL2vpnOamDbdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 29)
)
hwL2vpnOamDbdi.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamDbdi.setStatus(
        "current"
    )

hwL2vpnOamDbdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 30)
)
hwL2vpnOamDbdiClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamDbdiClear.setStatus(
        "current"
    )

hwL2vpnOamUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 31)
)
hwL2vpnOamUnknown.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamUnknown.setStatus(
        "current"
    )

hwL2vpnOamUnknownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 32)
)
hwL2vpnOamUnknownClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamUnknownClear.setStatus(
        "current"
    )

hwL2vpnOamLocalLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 33)
)
hwL2vpnOamLocalLock.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamLocalLock.setStatus(
        "current"
    )

hwL2vpnOamLocalLockClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 34)
)
hwL2vpnOamLocalLockClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamLocalLockClear.setStatus(
        "current"
    )

hwL2vpnOamSd1Far = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 35)
)
hwL2vpnOamSd1Far.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd1Far.setStatus(
        "current"
    )

hwL2vpnOamSd1FarClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 36)
)
hwL2vpnOamSd1FarClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd1FarClear.setStatus(
        "current"
    )

hwL2vpnOamSd2Far = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 37)
)
hwL2vpnOamSd2Far.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd2Far.setStatus(
        "current"
    )

hwL2vpnOamSd2FarClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 38)
)
hwL2vpnOamSd2FarClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamSd2FarClear.setStatus(
        "current"
    )

hwL2vpnOamFdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 39)
)
hwL2vpnOamFdi.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamFdi.setStatus(
        "current"
    )

hwL2vpnOamFdiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 2, 40)
)
hwL2vpnOamFdiClear.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnServiceType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnProtocolType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVcType"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPeerAddr"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfIndex"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnPwMaster"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnRmtSiteID"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnInLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOutLabel"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnIfName"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnVsiName"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamFdiClear.setStatus(
        "current"
    )


# Notifications groups

hwL2vpnOamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3, 2, 2)
)
hwL2vpnOamNotificationGroup.setObjects(
      *(("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamDloc"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamDlocClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd1Near"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd1NearClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamRdi"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamRdiClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMeg"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMegClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMep"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMepClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamPeriod"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamPeriodClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamAis"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamAisClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd2Near"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd2NearClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamLck"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamLckClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamCsf"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamCsfClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamExcess"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamExcessClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMismatch"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMismatchClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMismerge"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamMismergeClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamFail"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamFailClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamDbdi"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamDbdiClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamUnknown"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamUnknownClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamLocalLock"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamLocalLockClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd1Far"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd1FarClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd2Far"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamSd2FarClear"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamFdi"),
        ("HUAWEI-L2VPN-OAM-MIB", "hwL2vpnOamFdiClear"))
)
if mibBuilder.loadTexts:
    hwL2vpnOamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2vpnOamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwL2vpnOamMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2VPN-OAM-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2vpnOamTrap": hwL2vpnOamTrap,
       "hwL2vpnOamTrapMIBObjects": hwL2vpnOamTrapMIBObjects,
       "hwL2vpnServiceType": hwL2vpnServiceType,
       "hwL2vpnProtocolType": hwL2vpnProtocolType,
       "hwL2vpnVcID": hwL2vpnVcID,
       "hwL2vpnVcType": hwL2vpnVcType,
       "hwL2vpnPeerAddr": hwL2vpnPeerAddr,
       "hwL2vpnIfIndex": hwL2vpnIfIndex,
       "hwL2vpnPwMaster": hwL2vpnPwMaster,
       "hwL2vpnRmtSiteID": hwL2vpnRmtSiteID,
       "hwL2vpnInLabel": hwL2vpnInLabel,
       "hwL2vpnOutLabel": hwL2vpnOutLabel,
       "hwL2vpnIfName": hwL2vpnIfName,
       "hwL2vpnVsiName": hwL2vpnVsiName,
       "hwL2vpnOamMIBTraps": hwL2vpnOamMIBTraps,
       "hwL2vpnOamDloc": hwL2vpnOamDloc,
       "hwL2vpnOamDlocClear": hwL2vpnOamDlocClear,
       "hwL2vpnOamSd1Near": hwL2vpnOamSd1Near,
       "hwL2vpnOamSd1NearClear": hwL2vpnOamSd1NearClear,
       "hwL2vpnOamRdi": hwL2vpnOamRdi,
       "hwL2vpnOamRdiClear": hwL2vpnOamRdiClear,
       "hwL2vpnOamMeg": hwL2vpnOamMeg,
       "hwL2vpnOamMegClear": hwL2vpnOamMegClear,
       "hwL2vpnOamMep": hwL2vpnOamMep,
       "hwL2vpnOamMepClear": hwL2vpnOamMepClear,
       "hwL2vpnOamPeriod": hwL2vpnOamPeriod,
       "hwL2vpnOamPeriodClear": hwL2vpnOamPeriodClear,
       "hwL2vpnOamAis": hwL2vpnOamAis,
       "hwL2vpnOamAisClear": hwL2vpnOamAisClear,
       "hwL2vpnOamSd2Near": hwL2vpnOamSd2Near,
       "hwL2vpnOamSd2NearClear": hwL2vpnOamSd2NearClear,
       "hwL2vpnOamLck": hwL2vpnOamLck,
       "hwL2vpnOamLckClear": hwL2vpnOamLckClear,
       "hwL2vpnOamCsf": hwL2vpnOamCsf,
       "hwL2vpnOamCsfClear": hwL2vpnOamCsfClear,
       "hwL2vpnOamExcess": hwL2vpnOamExcess,
       "hwL2vpnOamExcessClear": hwL2vpnOamExcessClear,
       "hwL2vpnOamMismatch": hwL2vpnOamMismatch,
       "hwL2vpnOamMismatchClear": hwL2vpnOamMismatchClear,
       "hwL2vpnOamMismerge": hwL2vpnOamMismerge,
       "hwL2vpnOamMismergeClear": hwL2vpnOamMismergeClear,
       "hwL2vpnOamFail": hwL2vpnOamFail,
       "hwL2vpnOamFailClear": hwL2vpnOamFailClear,
       "hwL2vpnOamDbdi": hwL2vpnOamDbdi,
       "hwL2vpnOamDbdiClear": hwL2vpnOamDbdiClear,
       "hwL2vpnOamUnknown": hwL2vpnOamUnknown,
       "hwL2vpnOamUnknownClear": hwL2vpnOamUnknownClear,
       "hwL2vpnOamLocalLock": hwL2vpnOamLocalLock,
       "hwL2vpnOamLocalLockClear": hwL2vpnOamLocalLockClear,
       "hwL2vpnOamSd1Far": hwL2vpnOamSd1Far,
       "hwL2vpnOamSd1FarClear": hwL2vpnOamSd1FarClear,
       "hwL2vpnOamSd2Far": hwL2vpnOamSd2Far,
       "hwL2vpnOamSd2FarClear": hwL2vpnOamSd2FarClear,
       "hwL2vpnOamFdi": hwL2vpnOamFdi,
       "hwL2vpnOamFdiClear": hwL2vpnOamFdiClear,
       "hwL2vpnOamConformance": hwL2vpnOamConformance,
       "hwL2vpnOamMIBCompliances": hwL2vpnOamMIBCompliances,
       "hwL2vpnOamMIBCompliance": hwL2vpnOamMIBCompliance,
       "hwL2vpnOamGroups": hwL2vpnOamGroups,
       "hwL2vpnOamGroup": hwL2vpnOamGroup,
       "hwL2vpnOamNotificationGroup": hwL2vpnOamNotificationGroup}
)
