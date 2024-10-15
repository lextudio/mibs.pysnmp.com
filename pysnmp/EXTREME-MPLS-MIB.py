# SNMP MIB module (EXTREME-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:52 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsExtendedTunnelId,
 MplsLdpIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsLdpIdentifier",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

(PwIndexType,
 PwOperStatusTC,
 PwStatus) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType",
    "PwOperStatusTC",
    "PwStatus")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

extremeMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IndexInteger(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeMplsNotifications_ObjectIdentity = ObjectIdentity
extremeMplsNotifications = _ExtremeMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0)
)
_ExtremeMplsScalars_ObjectIdentity = ObjectIdentity
extremeMplsScalars = _ExtremeMplsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1)
)


class _ExtremePwUpDownNotificationEnable_Type(TruthValue):
    """Custom type extremePwUpDownNotificationEnable based on TruthValue"""


_ExtremePwUpDownNotificationEnable_Object = MibScalar
extremePwUpDownNotificationEnable = _ExtremePwUpDownNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 5),
    _ExtremePwUpDownNotificationEnable_Type()
)
extremePwUpDownNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePwUpDownNotificationEnable.setStatus("current")


class _ExtremePwDeletedNotificationEnable_Type(TruthValue):
    """Custom type extremePwDeletedNotificationEnable based on TruthValue"""


_ExtremePwDeletedNotificationEnable_Object = MibScalar
extremePwDeletedNotificationEnable = _ExtremePwDeletedNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 6),
    _ExtremePwDeletedNotificationEnable_Type()
)
extremePwDeletedNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePwDeletedNotificationEnable.setStatus("current")


class _ExtremePwNotificationMaxRate_Type(Unsigned32):
    """Custom type extremePwNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_ExtremePwNotificationMaxRate_Object = MibScalar
extremePwNotificationMaxRate = _ExtremePwNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 7),
    _ExtremePwNotificationMaxRate_Type()
)
extremePwNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePwNotificationMaxRate.setStatus("current")
_ExtremePwNotificationPwIndex_Type = PwIndexType
_ExtremePwNotificationPwIndex_Object = MibScalar
extremePwNotificationPwIndex = _ExtremePwNotificationPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 8),
    _ExtremePwNotificationPwIndex_Type()
)
extremePwNotificationPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremePwNotificationPwIndex.setStatus("current")
_ExtremePwNotificationPwOperStatus_Type = PwOperStatusTC
_ExtremePwNotificationPwOperStatus_Object = MibScalar
extremePwNotificationPwOperStatus = _ExtremePwNotificationPwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 9),
    _ExtremePwNotificationPwOperStatus_Type()
)
extremePwNotificationPwOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremePwNotificationPwOperStatus.setStatus("current")
_ExtremePwNotificationPeerAddrType_Type = InetAddressType
_ExtremePwNotificationPeerAddrType_Object = MibScalar
extremePwNotificationPeerAddrType = _ExtremePwNotificationPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 10),
    _ExtremePwNotificationPeerAddrType_Type()
)
extremePwNotificationPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremePwNotificationPeerAddrType.setStatus("current")
_ExtremePwNotificationPeerAddr_Type = InetAddress
_ExtremePwNotificationPeerAddr_Object = MibScalar
extremePwNotificationPeerAddr = _ExtremePwNotificationPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 11),
    _ExtremePwNotificationPeerAddr_Type()
)
extremePwNotificationPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremePwNotificationPeerAddr.setStatus("current")
_ExtremeMplsNotifTunnelIndex_Type = MplsTunnelIndex
_ExtremeMplsNotifTunnelIndex_Object = MibScalar
extremeMplsNotifTunnelIndex = _ExtremeMplsNotifTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 12),
    _ExtremeMplsNotifTunnelIndex_Type()
)
extremeMplsNotifTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelIndex.setStatus("current")
_ExtremeMplsNotifTunnelInstance_Type = MplsTunnelInstanceIndex
_ExtremeMplsNotifTunnelInstance_Object = MibScalar
extremeMplsNotifTunnelInstance = _ExtremeMplsNotifTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 13),
    _ExtremeMplsNotifTunnelInstance_Type()
)
extremeMplsNotifTunnelInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelInstance.setStatus("current")
_ExtremeMplsNotifTunnelIngressLSRId_Type = MplsExtendedTunnelId
_ExtremeMplsNotifTunnelIngressLSRId_Object = MibScalar
extremeMplsNotifTunnelIngressLSRId = _ExtremeMplsNotifTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 14),
    _ExtremeMplsNotifTunnelIngressLSRId_Type()
)
extremeMplsNotifTunnelIngressLSRId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelIngressLSRId.setStatus("current")
_ExtremeMplsNotifTunnelEgressLSRId_Type = MplsExtendedTunnelId
_ExtremeMplsNotifTunnelEgressLSRId_Object = MibScalar
extremeMplsNotifTunnelEgressLSRId = _ExtremeMplsNotifTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 15),
    _ExtremeMplsNotifTunnelEgressLSRId_Type()
)
extremeMplsNotifTunnelEgressLSRId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelEgressLSRId.setStatus("current")


class _ExtremeMplsNotifTunnelAdminStatus_Type(Integer32):
    """Custom type extremeMplsNotifTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ExtremeMplsNotifTunnelAdminStatus_Type.__name__ = "Integer32"
_ExtremeMplsNotifTunnelAdminStatus_Object = MibScalar
extremeMplsNotifTunnelAdminStatus = _ExtremeMplsNotifTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 16),
    _ExtremeMplsNotifTunnelAdminStatus_Type()
)
extremeMplsNotifTunnelAdminStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelAdminStatus.setStatus("current")


class _ExtremeMplsNotifTunnelOperStatus_Type(Integer32):
    """Custom type extremeMplsNotifTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_ExtremeMplsNotifTunnelOperStatus_Type.__name__ = "Integer32"
_ExtremeMplsNotifTunnelOperStatus_Object = MibScalar
extremeMplsNotifTunnelOperStatus = _ExtremeMplsNotifTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 17),
    _ExtremeMplsNotifTunnelOperStatus_Type()
)
extremeMplsNotifTunnelOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifTunnelOperStatus.setStatus("current")
_ExtremeMplsNotifLdpEntityLdpId_Type = MplsLdpIdentifier
_ExtremeMplsNotifLdpEntityLdpId_Object = MibScalar
extremeMplsNotifLdpEntityLdpId = _ExtremeMplsNotifLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 18),
    _ExtremeMplsNotifLdpEntityLdpId_Type()
)
extremeMplsNotifLdpEntityLdpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifLdpEntityLdpId.setStatus("current")
_ExtremeMplsNotifLdpEntityIndex_Type = IndexInteger
_ExtremeMplsNotifLdpEntityIndex_Object = MibScalar
extremeMplsNotifLdpEntityIndex = _ExtremeMplsNotifLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 19),
    _ExtremeMplsNotifLdpEntityIndex_Type()
)
extremeMplsNotifLdpEntityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifLdpEntityIndex.setStatus("current")
_ExtremeMplsNotifLdpPeerLdpId_Type = MplsLdpIdentifier
_ExtremeMplsNotifLdpPeerLdpId_Object = MibScalar
extremeMplsNotifLdpPeerLdpId = _ExtremeMplsNotifLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 20),
    _ExtremeMplsNotifLdpPeerLdpId_Type()
)
extremeMplsNotifLdpPeerLdpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifLdpPeerLdpId.setStatus("current")


class _ExtremeMplsNotifLdpSessionState_Type(Integer32):
    """Custom type extremeMplsNotifLdpSessionState based on Integer32"""
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
        *(("initialized", 2),
          ("nonexistent", 1),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_ExtremeMplsNotifLdpSessionState_Type.__name__ = "Integer32"
_ExtremeMplsNotifLdpSessionState_Object = MibScalar
extremeMplsNotifLdpSessionState = _ExtremeMplsNotifLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 21),
    _ExtremeMplsNotifLdpSessionState_Type()
)
extremeMplsNotifLdpSessionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifLdpSessionState.setStatus("current")
_ExtremeMplsNotifLdpSessionDiscontinuityTime_Type = TimeStamp
_ExtremeMplsNotifLdpSessionDiscontinuityTime_Object = MibScalar
extremeMplsNotifLdpSessionDiscontinuityTime = _ExtremeMplsNotifLdpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 22),
    _ExtremeMplsNotifLdpSessionDiscontinuityTime_Type()
)
extremeMplsNotifLdpSessionDiscontinuityTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMplsNotifLdpSessionDiscontinuityTime.setStatus("current")


class _ExtremeVplsNotifConfigIndex_Type(Unsigned32):
    """Custom type extremeVplsNotifConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremeVplsNotifConfigIndex_Type.__name__ = "Unsigned32"
_ExtremeVplsNotifConfigIndex_Object = MibScalar
extremeVplsNotifConfigIndex = _ExtremeVplsNotifConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 23),
    _ExtremeVplsNotifConfigIndex_Type()
)
extremeVplsNotifConfigIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVplsNotifConfigIndex.setStatus("current")
_ExtremeVplsNotifConfigVpnId_Type = VPNIdOrZero
_ExtremeVplsNotifConfigVpnId_Object = MibScalar
extremeVplsNotifConfigVpnId = _ExtremeVplsNotifConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 24),
    _ExtremeVplsNotifConfigVpnId_Type()
)
extremeVplsNotifConfigVpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVplsNotifConfigVpnId.setStatus("current")


class _ExtremeVplsNotifConfigAdminStatus_Type(Integer32):
    """Custom type extremeVplsNotifConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_ExtremeVplsNotifConfigAdminStatus_Type.__name__ = "Integer32"
_ExtremeVplsNotifConfigAdminStatus_Object = MibScalar
extremeVplsNotifConfigAdminStatus = _ExtremeVplsNotifConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 25),
    _ExtremeVplsNotifConfigAdminStatus_Type()
)
extremeVplsNotifConfigAdminStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVplsNotifConfigAdminStatus.setStatus("current")


class _ExtremeVplsNotifStatusOperStatus_Type(Integer32):
    """Custom type extremeVplsNotifStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("down", 3),
          ("up", 1))
    )


_ExtremeVplsNotifStatusOperStatus_Type.__name__ = "Integer32"
_ExtremeVplsNotifStatusOperStatus_Object = MibScalar
extremeVplsNotifStatusOperStatus = _ExtremeVplsNotifStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 1, 26),
    _ExtremeVplsNotifStatusOperStatus_Type()
)
extremeVplsNotifStatusOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeVplsNotifStatusOperStatus.setStatus("current")
_ExtremeVplsObjects_ObjectIdentity = ObjectIdentity
extremeVplsObjects = _ExtremeVplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3)
)
_ExtremeVplsConfigTable_Object = MibTable
extremeVplsConfigTable = _ExtremeVplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1)
)
if mibBuilder.loadTexts:
    extremeVplsConfigTable.setStatus("current")
_ExtremeVplsConfigEntry_Object = MibTableRow
extremeVplsConfigEntry = _ExtremeVplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1, 1)
)
extremeVplsConfigEntry.setIndexNames(
    (0, "EXTREME-MPLS-MIB", "extremeVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    extremeVplsConfigEntry.setStatus("current")


class _ExtremeVplsConfigIndex_Type(Unsigned32):
    """Custom type extremeVplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremeVplsConfigIndex_Type.__name__ = "Unsigned32"
_ExtremeVplsConfigIndex_Object = MibTableColumn
extremeVplsConfigIndex = _ExtremeVplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1, 1, 1),
    _ExtremeVplsConfigIndex_Type()
)
extremeVplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVplsConfigIndex.setStatus("current")


class _ExtremeVplsConfigRedunType_Type(Integer32):
    """Custom type extremeVplsConfigRedunType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eaps", 2),
          ("esrp", 1),
          ("none", 0),
          ("stp", 3))
    )


_ExtremeVplsConfigRedunType_Type.__name__ = "Integer32"
_ExtremeVplsConfigRedunType_Object = MibTableColumn
extremeVplsConfigRedunType = _ExtremeVplsConfigRedunType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1, 1, 2),
    _ExtremeVplsConfigRedunType_Type()
)
extremeVplsConfigRedunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVplsConfigRedunType.setStatus("current")
_ExtremeVplsConfigEAPSStatus_Type = SnmpAdminString
_ExtremeVplsConfigEAPSStatus_Object = MibTableColumn
extremeVplsConfigEAPSStatus = _ExtremeVplsConfigEAPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1, 1, 3),
    _ExtremeVplsConfigEAPSStatus_Type()
)
extremeVplsConfigEAPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVplsConfigEAPSStatus.setStatus("current")
_ExtremeVplsConfigESRPState_Type = SnmpAdminString
_ExtremeVplsConfigESRPState_Object = MibTableColumn
extremeVplsConfigESRPState = _ExtremeVplsConfigESRPState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 1, 1, 4),
    _ExtremeVplsConfigESRPState_Type()
)
extremeVplsConfigESRPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVplsConfigESRPState.setStatus("current")
_ExtremeVplsStatusTable_Object = MibTable
extremeVplsStatusTable = _ExtremeVplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 2)
)
if mibBuilder.loadTexts:
    extremeVplsStatusTable.setStatus("current")
_ExtremeVplsStatusEntry_Object = MibTableRow
extremeVplsStatusEntry = _ExtremeVplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 2, 1)
)
extremeVplsStatusEntry.setIndexNames(
    (0, "EXTREME-MPLS-MIB", "extremeVplsStatusIndex"),
)
if mibBuilder.loadTexts:
    extremeVplsStatusEntry.setStatus("current")


class _ExtremeVplsStatusIndex_Type(Unsigned32):
    """Custom type extremeVplsStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremeVplsStatusIndex_Type.__name__ = "Unsigned32"
_ExtremeVplsStatusIndex_Object = MibTableColumn
extremeVplsStatusIndex = _ExtremeVplsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 2, 1, 1),
    _ExtremeVplsStatusIndex_Type()
)
extremeVplsStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVplsStatusIndex.setStatus("current")


class _ExtremeVplsOperStatus_Type(Integer32):
    """Custom type extremeVplsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("down", 3),
          ("up", 1))
    )


_ExtremeVplsOperStatus_Type.__name__ = "Integer32"
_ExtremeVplsOperStatus_Object = MibTableColumn
extremeVplsOperStatus = _ExtremeVplsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 2, 1, 2),
    _ExtremeVplsOperStatus_Type()
)
extremeVplsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVplsOperStatus.setStatus("current")
_ExtremeVplsPeerTable_Object = MibTable
extremeVplsPeerTable = _ExtremeVplsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3)
)
if mibBuilder.loadTexts:
    extremeVplsPeerTable.setStatus("current")
_ExtremeVplsPeerEntry_Object = MibTableRow
extremeVplsPeerEntry = _ExtremeVplsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1)
)
extremeVplsPeerEntry.setIndexNames(
    (0, "EXTREME-MPLS-MIB", "extremeVplsIndex"),
    (0, "EXTREME-MPLS-MIB", "extremeVplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    extremeVplsPeerEntry.setStatus("current")


class _ExtremeVplsIndex_Type(Unsigned32):
    """Custom type extremeVplsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExtremeVplsIndex_Type.__name__ = "Unsigned32"
_ExtremeVplsIndex_Object = MibTableColumn
extremeVplsIndex = _ExtremeVplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1, 1),
    _ExtremeVplsIndex_Type()
)
extremeVplsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVplsIndex.setStatus("current")
_ExtremeVplsPwBindIndex_Type = PwIndexType
_ExtremeVplsPwBindIndex_Object = MibTableColumn
extremeVplsPwBindIndex = _ExtremeVplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1, 2),
    _ExtremeVplsPwBindIndex_Type()
)
extremeVplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeVplsPwBindIndex.setStatus("current")


class _ExtremePwInstalled_Type(Integer32):
    """Custom type extremePwInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ExtremePwInstalled_Type.__name__ = "Integer32"
_ExtremePwInstalled_Object = MibTableColumn
extremePwInstalled = _ExtremePwInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1, 3),
    _ExtremePwInstalled_Type()
)
extremePwInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePwInstalled.setStatus("current")


class _ExtremePwMode_Type(Integer32):
    """Custom type extremePwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coretocore", 1),
          ("coretospoke", 2),
          ("spoketocore", 3))
    )


_ExtremePwMode_Type.__name__ = "Integer32"
_ExtremePwMode_Object = MibTableColumn
extremePwMode = _ExtremePwMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1, 4),
    _ExtremePwMode_Type()
)
extremePwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePwMode.setStatus("current")


class _ExtremePwConfiguredRole_Type(Integer32):
    """Custom type extremePwConfiguredRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_ExtremePwConfiguredRole_Type.__name__ = "Integer32"
_ExtremePwConfiguredRole_Object = MibTableColumn
extremePwConfiguredRole = _ExtremePwConfiguredRole_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 3, 3, 1, 5),
    _ExtremePwConfiguredRole_Type()
)
extremePwConfiguredRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePwConfiguredRole.setStatus("current")
_ExtremeL2VpnMplsNotificationHandler_ObjectIdentity = ObjectIdentity
extremeL2VpnMplsNotificationHandler = _ExtremeL2VpnMplsNotificationHandler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 4)
)


class _ExtremeMPLSTrapsEnable_Type(Integer32):
    """Custom type extremeMPLSTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ExtremeMPLSTrapsEnable_Type.__name__ = "Integer32"
_ExtremeMPLSTrapsEnable_Object = MibScalar
extremeMPLSTrapsEnable = _ExtremeMPLSTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 4, 1),
    _ExtremeMPLSTrapsEnable_Type()
)
extremeMPLSTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMPLSTrapsEnable.setStatus("current")


class _ExtremeL2VpnTrapsEnable_Type(Integer32):
    """Custom type extremeL2VpnTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ExtremeL2VpnTrapsEnable_Type.__name__ = "Integer32"
_ExtremeL2VpnTrapsEnable_Object = MibScalar
extremeL2VpnTrapsEnable = _ExtremeL2VpnTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 4, 2),
    _ExtremeL2VpnTrapsEnable_Type()
)
extremeL2VpnTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeL2VpnTrapsEnable.setStatus("current")

# Managed Objects groups


# Notification objects

extremePwStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0, 1)
)
extremePwStatusChange.setObjects(
      *(("EXTREME-MPLS-MIB", "extremePwNotificationPwIndex"),
        ("EXTREME-MPLS-MIB", "extremePwNotificationPwOperStatus"))
)
if mibBuilder.loadTexts:
    extremePwStatusChange.setStatus(
        "current"
    )

extremePwDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0, 2)
)
extremePwDeleted.setObjects(
      *(("EXTREME-MPLS-MIB", "extremePwNotificationPwIndex"),
        ("EXTREME-MPLS-MIB", "extremePwNotificationPeerAddrType"),
        ("EXTREME-MPLS-MIB", "extremePwNotificationPeerAddr"))
)
if mibBuilder.loadTexts:
    extremePwDeleted.setStatus(
        "current"
    )

extremeMplsTunnelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0, 3)
)
extremeMplsTunnelStatusChange.setObjects(
      *(("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelIndex"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelInstance"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelIngressLSRId"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelEgressLSRId"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelAdminStatus"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    extremeMplsTunnelStatusChange.setStatus(
        "current"
    )

extremeMplsLdpSessionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0, 4)
)
extremeMplsLdpSessionStatusChange.setObjects(
      *(("EXTREME-MPLS-MIB", "extremeMplsNotifLdpEntityLdpId"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifLdpEntityIndex"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifLdpPeerLdpId"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifLdpSessionState"),
        ("EXTREME-MPLS-MIB", "extremeMplsNotifLdpSessionDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    extremeMplsLdpSessionStatusChange.setStatus(
        "current"
    )

extremeVplsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 0, 5)
)
extremeVplsStatusChange.setObjects(
      *(("EXTREME-MPLS-MIB", "extremeVplsNotifConfigIndex"),
        ("EXTREME-MPLS-MIB", "extremeVplsNotifConfigVpnId"),
        ("EXTREME-MPLS-MIB", "extremeVplsNotifConfigAdminStatus"),
        ("EXTREME-MPLS-MIB", "extremeVplsNotifStatusOperStatus"))
)
if mibBuilder.loadTexts:
    extremeVplsStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MPLS-MIB",
    **{"IndexInteger": IndexInteger,
       "extremeMplsMIB": extremeMplsMIB,
       "extremeMplsNotifications": extremeMplsNotifications,
       "extremePwStatusChange": extremePwStatusChange,
       "extremePwDeleted": extremePwDeleted,
       "extremeMplsTunnelStatusChange": extremeMplsTunnelStatusChange,
       "extremeMplsLdpSessionStatusChange": extremeMplsLdpSessionStatusChange,
       "extremeVplsStatusChange": extremeVplsStatusChange,
       "extremeMplsScalars": extremeMplsScalars,
       "extremePwUpDownNotificationEnable": extremePwUpDownNotificationEnable,
       "extremePwDeletedNotificationEnable": extremePwDeletedNotificationEnable,
       "extremePwNotificationMaxRate": extremePwNotificationMaxRate,
       "extremePwNotificationPwIndex": extremePwNotificationPwIndex,
       "extremePwNotificationPwOperStatus": extremePwNotificationPwOperStatus,
       "extremePwNotificationPeerAddrType": extremePwNotificationPeerAddrType,
       "extremePwNotificationPeerAddr": extremePwNotificationPeerAddr,
       "extremeMplsNotifTunnelIndex": extremeMplsNotifTunnelIndex,
       "extremeMplsNotifTunnelInstance": extremeMplsNotifTunnelInstance,
       "extremeMplsNotifTunnelIngressLSRId": extremeMplsNotifTunnelIngressLSRId,
       "extremeMplsNotifTunnelEgressLSRId": extremeMplsNotifTunnelEgressLSRId,
       "extremeMplsNotifTunnelAdminStatus": extremeMplsNotifTunnelAdminStatus,
       "extremeMplsNotifTunnelOperStatus": extremeMplsNotifTunnelOperStatus,
       "extremeMplsNotifLdpEntityLdpId": extremeMplsNotifLdpEntityLdpId,
       "extremeMplsNotifLdpEntityIndex": extremeMplsNotifLdpEntityIndex,
       "extremeMplsNotifLdpPeerLdpId": extremeMplsNotifLdpPeerLdpId,
       "extremeMplsNotifLdpSessionState": extremeMplsNotifLdpSessionState,
       "extremeMplsNotifLdpSessionDiscontinuityTime": extremeMplsNotifLdpSessionDiscontinuityTime,
       "extremeVplsNotifConfigIndex": extremeVplsNotifConfigIndex,
       "extremeVplsNotifConfigVpnId": extremeVplsNotifConfigVpnId,
       "extremeVplsNotifConfigAdminStatus": extremeVplsNotifConfigAdminStatus,
       "extremeVplsNotifStatusOperStatus": extremeVplsNotifStatusOperStatus,
       "extremeVplsObjects": extremeVplsObjects,
       "extremeVplsConfigTable": extremeVplsConfigTable,
       "extremeVplsConfigEntry": extremeVplsConfigEntry,
       "extremeVplsConfigIndex": extremeVplsConfigIndex,
       "extremeVplsConfigRedunType": extremeVplsConfigRedunType,
       "extremeVplsConfigEAPSStatus": extremeVplsConfigEAPSStatus,
       "extremeVplsConfigESRPState": extremeVplsConfigESRPState,
       "extremeVplsStatusTable": extremeVplsStatusTable,
       "extremeVplsStatusEntry": extremeVplsStatusEntry,
       "extremeVplsStatusIndex": extremeVplsStatusIndex,
       "extremeVplsOperStatus": extremeVplsOperStatus,
       "extremeVplsPeerTable": extremeVplsPeerTable,
       "extremeVplsPeerEntry": extremeVplsPeerEntry,
       "extremeVplsIndex": extremeVplsIndex,
       "extremeVplsPwBindIndex": extremeVplsPwBindIndex,
       "extremePwInstalled": extremePwInstalled,
       "extremePwMode": extremePwMode,
       "extremePwConfiguredRole": extremePwConfiguredRole,
       "extremeL2VpnMplsNotificationHandler": extremeL2VpnMplsNotificationHandler,
       "extremeMPLSTrapsEnable": extremeMPLSTrapsEnable,
       "extremeL2VpnTrapsEnable": extremeL2VpnTrapsEnable}
)
