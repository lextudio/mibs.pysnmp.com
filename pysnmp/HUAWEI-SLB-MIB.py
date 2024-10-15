# SNMP MIB module (HUAWEI-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:55 2024
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

hwSLBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225)
)
hwSLBMIB.setRevisions(
        ("2009-11-30 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSlbMibObjects_ObjectIdentity = ObjectIdentity
hwSlbMibObjects = _HwSlbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1)
)
_HwSlbTrapObjects_ObjectIdentity = ObjectIdentity
hwSlbTrapObjects = _HwSlbTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1)
)
_HwIpAddress_Type = IpAddress
_HwIpAddress_Object = MibScalar
hwIpAddress = _HwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 1),
    _HwIpAddress_Type()
)
hwIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpAddress.setStatus("current")


class _HwMemberName_Type(OctetString):
    """Custom type hwMemberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwMemberName_Type.__name__ = "OctetString"
_HwMemberName_Object = MibScalar
hwMemberName = _HwMemberName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 2),
    _HwMemberName_Type()
)
hwMemberName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMemberName.setStatus("current")


class _HwGroupName_Type(OctetString):
    """Custom type hwGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwGroupName_Type.__name__ = "OctetString"
_HwGroupName_Object = MibScalar
hwGroupName = _HwGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 3),
    _HwGroupName_Type()
)
hwGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGroupName.setStatus("current")


class _HwPort_Type(Integer32):
    """Custom type hwPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwPort_Type.__name__ = "Integer32"
_HwPort_Object = MibScalar
hwPort = _HwPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 4),
    _HwPort_Type()
)
hwPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPort.setStatus("current")


class _HwProbeName_Type(OctetString):
    """Custom type hwProbeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwProbeName_Type.__name__ = "OctetString"
_HwProbeName_Object = MibScalar
hwProbeName = _HwProbeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 5),
    _HwProbeName_Type()
)
hwProbeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwProbeName.setStatus("current")


class _HwProbeType_Type(Integer32):
    """Custom type hwProbeType based on Integer32"""
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
        *(("http", 4),
          ("icmp", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_HwProbeType_Type.__name__ = "Integer32"
_HwProbeType_Object = MibScalar
hwProbeType = _HwProbeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 6),
    _HwProbeType_Type()
)
hwProbeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwProbeType.setStatus("current")


class _HwConnectionNum_Type(Integer32):
    """Custom type hwConnectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000000),
    )


_HwConnectionNum_Type.__name__ = "Integer32"
_HwConnectionNum_Object = MibScalar
hwConnectionNum = _HwConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 7),
    _HwConnectionNum_Type()
)
hwConnectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwConnectionNum.setStatus("current")


class _HwMasterGroup_Type(OctetString):
    """Custom type hwMasterGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwMasterGroup_Type.__name__ = "OctetString"
_HwMasterGroup_Object = MibScalar
hwMasterGroup = _HwMasterGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 8),
    _HwMasterGroup_Type()
)
hwMasterGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMasterGroup.setStatus("current")


class _HwMasterGroupActiveNum_Type(Integer32):
    """Custom type hwMasterGroupActiveNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMasterGroupActiveNum_Type.__name__ = "Integer32"
_HwMasterGroupActiveNum_Object = MibScalar
hwMasterGroupActiveNum = _HwMasterGroupActiveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 9),
    _HwMasterGroupActiveNum_Type()
)
hwMasterGroupActiveNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMasterGroupActiveNum.setStatus("current")


class _HwMasterGroupTotalNum_Type(Integer32):
    """Custom type hwMasterGroupTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMasterGroupTotalNum_Type.__name__ = "Integer32"
_HwMasterGroupTotalNum_Object = MibScalar
hwMasterGroupTotalNum = _HwMasterGroupTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 10),
    _HwMasterGroupTotalNum_Type()
)
hwMasterGroupTotalNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMasterGroupTotalNum.setStatus("current")


class _HwBackupGroup_Type(OctetString):
    """Custom type hwBackupGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwBackupGroup_Type.__name__ = "OctetString"
_HwBackupGroup_Object = MibScalar
hwBackupGroup = _HwBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 11),
    _HwBackupGroup_Type()
)
hwBackupGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBackupGroup.setStatus("current")


class _HwBackupGroupActiveNum_Type(Integer32):
    """Custom type hwBackupGroupActiveNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBackupGroupActiveNum_Type.__name__ = "Integer32"
_HwBackupGroupActiveNum_Object = MibScalar
hwBackupGroupActiveNum = _HwBackupGroupActiveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 12),
    _HwBackupGroupActiveNum_Type()
)
hwBackupGroupActiveNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBackupGroupActiveNum.setStatus("current")


class _HwBackupGroupTotalNum_Type(Integer32):
    """Custom type hwBackupGroupTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwBackupGroupTotalNum_Type.__name__ = "Integer32"
_HwBackupGroupTotalNum_Object = MibScalar
hwBackupGroupTotalNum = _HwBackupGroupTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 13),
    _HwBackupGroupTotalNum_Type()
)
hwBackupGroupTotalNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBackupGroupTotalNum.setStatus("current")


class _HwActionName_Type(OctetString):
    """Custom type hwActionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwActionName_Type.__name__ = "OctetString"
_HwActionName_Object = MibScalar
hwActionName = _HwActionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 14),
    _HwActionName_Type()
)
hwActionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwActionName.setStatus("current")


class _HwCurWorkGroupName_Type(OctetString):
    """Custom type hwCurWorkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwCurWorkGroupName_Type.__name__ = "OctetString"
_HwCurWorkGroupName_Object = MibScalar
hwCurWorkGroupName = _HwCurWorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 1, 15),
    _HwCurWorkGroupName_Type()
)
hwCurWorkGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCurWorkGroupName.setStatus("current")
_HwSlbNotifications_ObjectIdentity = ObjectIdentity
hwSlbNotifications = _HwSlbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2)
)
_HwSlbConformance_ObjectIdentity = ObjectIdentity
hwSlbConformance = _HwSlbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3)
)
_HwSlbGroups_ObjectIdentity = ObjectIdentity
hwSlbGroups = _HwSlbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3, 1)
)
_HwSlbCompliances_ObjectIdentity = ObjectIdentity
hwSlbCompliances = _HwSlbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3, 2)
)

# Managed Objects groups

hwSlbTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3, 1, 1)
)
hwSlbTrapObjectsGroup.setObjects(
      *(("HUAWEI-SLB-MIB", "hwIpAddress"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwPort"),
        ("HUAWEI-SLB-MIB", "hwProbeName"),
        ("HUAWEI-SLB-MIB", "hwProbeType"),
        ("HUAWEI-SLB-MIB", "hwConnectionNum"),
        ("HUAWEI-SLB-MIB", "hwActionName"),
        ("HUAWEI-SLB-MIB", "hwMasterGroup"),
        ("HUAWEI-SLB-MIB", "hwMasterGroupActiveNum"),
        ("HUAWEI-SLB-MIB", "hwMasterGroupTotalNum"),
        ("HUAWEI-SLB-MIB", "hwBackupGroup"),
        ("HUAWEI-SLB-MIB", "hwBackupGroupActiveNum"),
        ("HUAWEI-SLB-MIB", "hwBackupGroupTotalNum"),
        ("HUAWEI-SLB-MIB", "hwCurWorkGroupName"))
)
if mibBuilder.loadTexts:
    hwSlbTrapObjectsGroup.setStatus("current")


# Notification objects

hwMemberInstanceStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 1)
)
hwMemberInstanceStateUp.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwIpAddress"),
        ("HUAWEI-SLB-MIB", "hwPort"))
)
if mibBuilder.loadTexts:
    hwMemberInstanceStateUp.setStatus(
        "current"
    )

hwMemberInstanceStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 2)
)
hwMemberInstanceStateDown.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwIpAddress"),
        ("HUAWEI-SLB-MIB", "hwPort"))
)
if mibBuilder.loadTexts:
    hwMemberInstanceStateDown.setStatus(
        "current"
    )

hwGroupStateSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 3)
)
hwGroupStateSwitchover.setObjects(
      *(("HUAWEI-SLB-MIB", "hwActionName"),
        ("HUAWEI-SLB-MIB", "hwMasterGroup"),
        ("HUAWEI-SLB-MIB", "hwMasterGroupActiveNum"),
        ("HUAWEI-SLB-MIB", "hwMasterGroupTotalNum"),
        ("HUAWEI-SLB-MIB", "hwBackupGroup"),
        ("HUAWEI-SLB-MIB", "hwBackupGroupActiveNum"),
        ("HUAWEI-SLB-MIB", "hwBackupGroupTotalNum"),
        ("HUAWEI-SLB-MIB", "hwCurWorkGroupName"))
)
if mibBuilder.loadTexts:
    hwGroupStateSwitchover.setStatus(
        "current"
    )

hwMemberConnectionFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 4)
)
hwMemberConnectionFull.setObjects(
      *(("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwConnectionNum"))
)
if mibBuilder.loadTexts:
    hwMemberConnectionFull.setStatus(
        "current"
    )

hwMemberConnectionFullRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 5)
)
hwMemberConnectionFullRestore.setObjects(
      *(("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwConnectionNum"))
)
if mibBuilder.loadTexts:
    hwMemberConnectionFullRestore.setStatus(
        "current"
    )

hwMemberInstanceConnectionFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 6)
)
hwMemberInstanceConnectionFull.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwConnectionNum"))
)
if mibBuilder.loadTexts:
    hwMemberInstanceConnectionFull.setStatus(
        "current"
    )

hwMemberInstanceConnectionFullRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 7)
)
hwMemberInstanceConnectionFullRestore.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwConnectionNum"))
)
if mibBuilder.loadTexts:
    hwMemberInstanceConnectionFullRestore.setStatus(
        "current"
    )

hwProbeInstanceStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 8)
)
hwProbeInstanceStateUp.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwProbeName"),
        ("HUAWEI-SLB-MIB", "hwProbeType"),
        ("HUAWEI-SLB-MIB", "hwIpAddress"),
        ("HUAWEI-SLB-MIB", "hwPort"))
)
if mibBuilder.loadTexts:
    hwProbeInstanceStateUp.setStatus(
        "current"
    )

hwProbeInstanceStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 2, 9)
)
hwProbeInstanceStateDown.setObjects(
      *(("HUAWEI-SLB-MIB", "hwGroupName"),
        ("HUAWEI-SLB-MIB", "hwMemberName"),
        ("HUAWEI-SLB-MIB", "hwProbeName"),
        ("HUAWEI-SLB-MIB", "hwProbeType"),
        ("HUAWEI-SLB-MIB", "hwIpAddress"),
        ("HUAWEI-SLB-MIB", "hwPort"))
)
if mibBuilder.loadTexts:
    hwProbeInstanceStateDown.setStatus(
        "current"
    )


# Notifications groups

hwSlbNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3, 1, 2)
)
hwSlbNotificationsGroup.setObjects(
      *(("HUAWEI-SLB-MIB", "hwMemberInstanceStateUp"),
        ("HUAWEI-SLB-MIB", "hwMemberInstanceStateDown"),
        ("HUAWEI-SLB-MIB", "hwGroupStateSwitchover"),
        ("HUAWEI-SLB-MIB", "hwMemberInstanceConnectionFull"),
        ("HUAWEI-SLB-MIB", "hwMemberInstanceConnectionFullRestore"),
        ("HUAWEI-SLB-MIB", "hwProbeInstanceStateUp"),
        ("HUAWEI-SLB-MIB", "hwProbeInstanceStateDown"),
        ("HUAWEI-SLB-MIB", "hwMemberConnectionFull"),
        ("HUAWEI-SLB-MIB", "hwMemberConnectionFullRestore"))
)
if mibBuilder.loadTexts:
    hwSlbNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSlbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 225, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwSlbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SLB-MIB",
    **{"hwSLBMIB": hwSLBMIB,
       "hwSlbMibObjects": hwSlbMibObjects,
       "hwSlbTrapObjects": hwSlbTrapObjects,
       "hwIpAddress": hwIpAddress,
       "hwMemberName": hwMemberName,
       "hwGroupName": hwGroupName,
       "hwPort": hwPort,
       "hwProbeName": hwProbeName,
       "hwProbeType": hwProbeType,
       "hwConnectionNum": hwConnectionNum,
       "hwMasterGroup": hwMasterGroup,
       "hwMasterGroupActiveNum": hwMasterGroupActiveNum,
       "hwMasterGroupTotalNum": hwMasterGroupTotalNum,
       "hwBackupGroup": hwBackupGroup,
       "hwBackupGroupActiveNum": hwBackupGroupActiveNum,
       "hwBackupGroupTotalNum": hwBackupGroupTotalNum,
       "hwActionName": hwActionName,
       "hwCurWorkGroupName": hwCurWorkGroupName,
       "hwSlbNotifications": hwSlbNotifications,
       "hwMemberInstanceStateUp": hwMemberInstanceStateUp,
       "hwMemberInstanceStateDown": hwMemberInstanceStateDown,
       "hwGroupStateSwitchover": hwGroupStateSwitchover,
       "hwMemberConnectionFull": hwMemberConnectionFull,
       "hwMemberConnectionFullRestore": hwMemberConnectionFullRestore,
       "hwMemberInstanceConnectionFull": hwMemberInstanceConnectionFull,
       "hwMemberInstanceConnectionFullRestore": hwMemberInstanceConnectionFullRestore,
       "hwProbeInstanceStateUp": hwProbeInstanceStateUp,
       "hwProbeInstanceStateDown": hwProbeInstanceStateDown,
       "hwSlbConformance": hwSlbConformance,
       "hwSlbGroups": hwSlbGroups,
       "hwSlbTrapObjectsGroup": hwSlbTrapObjectsGroup,
       "hwSlbNotificationsGroup": hwSlbNotificationsGroup,
       "hwSlbCompliances": hwSlbCompliances,
       "hwSlbCompliance": hwSlbCompliance}
)
