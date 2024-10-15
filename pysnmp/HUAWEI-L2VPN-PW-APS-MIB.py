# SNMP MIB module (HUAWEI-L2VPN-PW-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2VPN-PW-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:27 2024
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

(hwPWInterfaceIndex,) = mibBuilder.importSymbols(
    "HUAWEI-PWE3-MIB",
    "hwPWInterfaceIndex")

(HWL2VpnVcEncapsType,) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWL2VpnVcEncapsType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwL2vpnPwAps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10)
)
hwL2vpnPwAps.setRevisions(
        ("2013-05-13 12:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwPwApsObjects_ObjectIdentity = ObjectIdentity
hwPwApsObjects = _HwPwApsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1)
)
_HwPwApsTable_Object = MibTable
hwPwApsTable = _HwPwApsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hwPwApsTable.setStatus("current")
_HwPwApsEntry_Object = MibTableRow
hwPwApsEntry = _HwPwApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1)
)
hwPwApsEntry.setIndexNames(
    (0, "HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
)
if mibBuilder.loadTexts:
    hwPwApsEntry.setStatus("current")
_HwPwApsId_Type = Unsigned32
_HwPwApsId_Object = MibTableColumn
hwPwApsId = _HwPwApsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 1),
    _HwPwApsId_Type()
)
hwPwApsId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPwApsId.setStatus("current")


class _HwPwApsRole_Type(Integer32):
    """Custom type hwPwApsRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 255))
    )


_HwPwApsRole_Type.__name__ = "Integer32"
_HwPwApsRole_Object = MibTableColumn
hwPwApsRole = _HwPwApsRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 2),
    _HwPwApsRole_Type()
)
hwPwApsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwApsRole.setStatus("current")


class _HwPwApsRequestResult_Type(Integer32):
    """Custom type hwPwApsRequestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protect", 2),
          ("work", 1))
    )


_HwPwApsRequestResult_Type.__name__ = "Integer32"
_HwPwApsRequestResult_Object = MibTableColumn
hwPwApsRequestResult = _HwPwApsRequestResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 3),
    _HwPwApsRequestResult_Type()
)
hwPwApsRequestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwApsRequestResult.setStatus("current")


class _HwPwApsState_Type(Integer32):
    """Custom type hwPwApsState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("dnr", 11),
          ("exer", 9),
          ("fs", 3),
          ("lo", 1),
          ("ms", 7),
          ("nr", 12),
          ("rr", 10),
          ("sd", 6),
          ("sdp", 5),
          ("sf", 4),
          ("sfp", 2),
          ("unknown", 255),
          ("wtr", 8))
    )


_HwPwApsState_Type.__name__ = "Integer32"
_HwPwApsState_Object = MibTableColumn
hwPwApsState = _HwPwApsState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 4),
    _HwPwApsState_Type()
)
hwPwApsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwApsState.setStatus("current")


class _HwPwApsWorkState_Type(Integer32):
    """Custom type hwPwApsWorkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defect", 2),
          ("defectsd", 3),
          ("nondefect", 1),
          ("unknown", 255))
    )


_HwPwApsWorkState_Type.__name__ = "Integer32"
_HwPwApsWorkState_Object = MibTableColumn
hwPwApsWorkState = _HwPwApsWorkState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 5),
    _HwPwApsWorkState_Type()
)
hwPwApsWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwApsWorkState.setStatus("current")


class _HwPwApsProtectState_Type(Integer32):
    """Custom type hwPwApsProtectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defect", 2),
          ("defectsd", 3),
          ("nondefect", 1),
          ("unknown", 255))
    )


_HwPwApsProtectState_Type.__name__ = "Integer32"
_HwPwApsProtectState_Object = MibTableColumn
hwPwApsProtectState = _HwPwApsProtectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 6),
    _HwPwApsProtectState_Type()
)
hwPwApsProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwApsProtectState.setStatus("current")
_HwL2vpnPwApsTraps_ObjectIdentity = ObjectIdentity
hwL2vpnPwApsTraps = _HwL2vpnPwApsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2)
)
_HwL2vpnPwApsScalarsObject_ObjectIdentity = ObjectIdentity
hwL2vpnPwApsScalarsObject = _HwL2vpnPwApsScalarsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 3)
)
_HwPwApsMIBConformance_ObjectIdentity = ObjectIdentity
hwPwApsMIBConformance = _HwPwApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4)
)
_HwPwApsMIBCompliances_ObjectIdentity = ObjectIdentity
hwPwApsMIBCompliances = _HwPwApsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 1)
)
_HwPwApsMIBGroups_ObjectIdentity = ObjectIdentity
hwPwApsMIBGroups = _HwPwApsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2)
)

# Managed Objects groups

hwPwApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2, 1)
)
hwPwApsGroup.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRole"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRequestResult"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsState"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsWorkState"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsProtectState"))
)
if mibBuilder.loadTexts:
    hwPwApsGroup.setStatus("current")


# Notification objects

hwPwApsTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 1)
)
hwPwApsTypeMismatch.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsTypeMismatch.setStatus(
        "current"
    )

hwPwApsTypeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 2)
)
hwPwApsTypeMismatchClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsTypeMismatchClear.setStatus(
        "current"
    )

hwPwApsPathMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 3)
)
hwPwApsPathMismatch.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsPathMismatch.setStatus(
        "current"
    )

hwPwApsPathMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 4)
)
hwPwApsPathMismatchClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsPathMismatchClear.setStatus(
        "current"
    )

hwPwApsSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 5)
)
hwPwApsSwitchFail.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsSwitchFail.setStatus(
        "current"
    )

hwPwApsSwitchFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 6)
)
hwPwApsSwitchFailClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsSwitchFailClear.setStatus(
        "current"
    )

hwPwApsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 7)
)
hwPwApsLost.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsLost.setStatus(
        "current"
    )

hwPwApsLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 8)
)
hwPwApsLostClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsLostClear.setStatus(
        "current"
    )

hwPwApsIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 9)
)
hwPwApsIdMismatch.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsIdMismatch.setStatus(
        "current"
    )

hwPwApsIdMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 10)
)
hwPwApsIdMismatchClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsIdMismatchClear.setStatus(
        "current"
    )

hwPwApsBypassPwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 11)
)
hwPwApsBypassPwMismatch.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsBypassPwMismatch.setStatus(
        "current"
    )

hwPwApsBypssPwMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 12)
)
hwPwApsBypssPwMismatchClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsBypssPwMismatchClear.setStatus(
        "current"
    )

hwPwApsSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 13)
)
hwPwApsSwitchEvent.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRole"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRequestResult"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsState"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsWorkState"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsProtectState"))
)
if mibBuilder.loadTexts:
    hwPwApsSwitchEvent.setStatus(
        "current"
    )

hwPwApsOutAge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 14)
)
hwPwApsOutAge.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsOutAge.setStatus(
        "current"
    )

hwPwApsOutAgeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 15)
)
hwPwApsOutAgeClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsOutAgeClear.setStatus(
        "current"
    )

hwPwApsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 16)
)
hwPwApsDegraded.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsDegraded.setStatus(
        "current"
    )

hwPwApsDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 17)
)
hwPwApsDegradedClear.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"),
        ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hwPwApsDegradedClear.setStatus(
        "current"
    )


# Notifications groups

hwPwApsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2, 2)
)
hwPwApsNotificationGroup.setObjects(
      *(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsTypeMismatch"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsTypeMismatchClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsPathMismatch"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsPathMismatchClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchFail"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchFailClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsLost"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsLostClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsIdMismatch"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsIdMismatchClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsBypassPwMismatch"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsBypssPwMismatchClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchEvent"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsOutAge"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsOutAgeClear"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsDegraded"),
        ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsDegradedClear"))
)
if mibBuilder.loadTexts:
    hwPwApsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwPwApsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwPwApsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2VPN-PW-APS-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2vpnPwAps": hwL2vpnPwAps,
       "hwPwApsObjects": hwPwApsObjects,
       "hwPwApsTable": hwPwApsTable,
       "hwPwApsEntry": hwPwApsEntry,
       "hwPwApsId": hwPwApsId,
       "hwPwApsRole": hwPwApsRole,
       "hwPwApsRequestResult": hwPwApsRequestResult,
       "hwPwApsState": hwPwApsState,
       "hwPwApsWorkState": hwPwApsWorkState,
       "hwPwApsProtectState": hwPwApsProtectState,
       "hwL2vpnPwApsTraps": hwL2vpnPwApsTraps,
       "hwPwApsTypeMismatch": hwPwApsTypeMismatch,
       "hwPwApsTypeMismatchClear": hwPwApsTypeMismatchClear,
       "hwPwApsPathMismatch": hwPwApsPathMismatch,
       "hwPwApsPathMismatchClear": hwPwApsPathMismatchClear,
       "hwPwApsSwitchFail": hwPwApsSwitchFail,
       "hwPwApsSwitchFailClear": hwPwApsSwitchFailClear,
       "hwPwApsLost": hwPwApsLost,
       "hwPwApsLostClear": hwPwApsLostClear,
       "hwPwApsIdMismatch": hwPwApsIdMismatch,
       "hwPwApsIdMismatchClear": hwPwApsIdMismatchClear,
       "hwPwApsBypassPwMismatch": hwPwApsBypassPwMismatch,
       "hwPwApsBypssPwMismatchClear": hwPwApsBypssPwMismatchClear,
       "hwPwApsSwitchEvent": hwPwApsSwitchEvent,
       "hwPwApsOutAge": hwPwApsOutAge,
       "hwPwApsOutAgeClear": hwPwApsOutAgeClear,
       "hwPwApsDegraded": hwPwApsDegraded,
       "hwPwApsDegradedClear": hwPwApsDegradedClear,
       "hwL2vpnPwApsScalarsObject": hwL2vpnPwApsScalarsObject,
       "hwPwApsMIBConformance": hwPwApsMIBConformance,
       "hwPwApsMIBCompliances": hwPwApsMIBCompliances,
       "hwPwApsMIBCompliance": hwPwApsMIBCompliance,
       "hwPwApsMIBGroups": hwPwApsMIBGroups,
       "hwPwApsGroup": hwPwApsGroup,
       "hwPwApsNotificationGroup": hwPwApsNotificationGroup}
)
