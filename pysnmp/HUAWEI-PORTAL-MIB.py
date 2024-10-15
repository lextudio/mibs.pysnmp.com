# SNMP MIB module (HUAWEI-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PORTAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:34 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwPortal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPortalMibObjects_ObjectIdentity = ObjectIdentity
hwPortalMibObjects = _HwPortalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1)
)
_HwPortalConfigPara_ObjectIdentity = ObjectIdentity
hwPortalConfigPara = _HwPortalConfigPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1)
)


class _HwPortalConfigVersionSupport_Type(Integer32):
    """Custom type hwPortalConfigVersionSupport based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("v2", 2))
    )


_HwPortalConfigVersionSupport_Type.__name__ = "Integer32"
_HwPortalConfigVersionSupport_Object = MibScalar
hwPortalConfigVersionSupport = _HwPortalConfigVersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 1),
    _HwPortalConfigVersionSupport_Type()
)
hwPortalConfigVersionSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigVersionSupport.setStatus("current")


class _HwPortalConfigTextInfoSwitch_Type(TruthValue):
    """Custom type hwPortalConfigTextInfoSwitch based on TruthValue"""


_HwPortalConfigTextInfoSwitch_Object = MibScalar
hwPortalConfigTextInfoSwitch = _HwPortalConfigTextInfoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 2),
    _HwPortalConfigTextInfoSwitch_Type()
)
hwPortalConfigTextInfoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigTextInfoSwitch.setStatus("current")


class _HwPortalConfigServerUdpReceivePort_Type(Integer32):
    """Custom type hwPortalConfigServerUdpReceivePort based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwPortalConfigServerUdpReceivePort_Type.__name__ = "Integer32"
_HwPortalConfigServerUdpReceivePort_Object = MibScalar
hwPortalConfigServerUdpReceivePort = _HwPortalConfigServerUdpReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 3),
    _HwPortalConfigServerUdpReceivePort_Type()
)
hwPortalConfigServerUdpReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigServerUdpReceivePort.setStatus("current")


class _HwPortalConfigServerUdpSendPort_Type(Integer32):
    """Custom type hwPortalConfigServerUdpSendPort based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwPortalConfigServerUdpSendPort_Type.__name__ = "Integer32"
_HwPortalConfigServerUdpSendPort_Object = MibScalar
hwPortalConfigServerUdpSendPort = _HwPortalConfigServerUdpSendPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 4),
    _HwPortalConfigServerUdpSendPort_Type()
)
hwPortalConfigServerUdpSendPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigServerUdpSendPort.setStatus("current")


class _HwPortalConfigTrapUdpPort_Type(Integer32):
    """Custom type hwPortalConfigTrapUdpPort based on Integer32"""
    defaultValue = 50100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwPortalConfigTrapUdpPort_Type.__name__ = "Integer32"
_HwPortalConfigTrapUdpPort_Object = MibScalar
hwPortalConfigTrapUdpPort = _HwPortalConfigTrapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 5),
    _HwPortalConfigTrapUdpPort_Type()
)
hwPortalConfigTrapUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigTrapUdpPort.setStatus("current")
_HwPortalConfigSourecIfIndex_Type = InterfaceIndex
_HwPortalConfigSourecIfIndex_Object = MibScalar
hwPortalConfigSourecIfIndex = _HwPortalConfigSourecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 1, 6),
    _HwPortalConfigSourecIfIndex_Type()
)
hwPortalConfigSourecIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigSourecIfIndex.setStatus("current")
_HwPortalPacketStatisticsPara_ObjectIdentity = ObjectIdentity
hwPortalPacketStatisticsPara = _HwPortalPacketStatisticsPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2)
)
_HwPortalStatisticsBeginTime_Type = DateAndTime
_HwPortalStatisticsBeginTime_Object = MibScalar
hwPortalStatisticsBeginTime = _HwPortalStatisticsBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 1),
    _HwPortalStatisticsBeginTime_Type()
)
hwPortalStatisticsBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalStatisticsBeginTime.setStatus("current")
_HwPortalPacketStatisticsAuthenticatorError_Type = Counter64
_HwPortalPacketStatisticsAuthenticatorError_Object = MibScalar
hwPortalPacketStatisticsAuthenticatorError = _HwPortalPacketStatisticsAuthenticatorError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 2),
    _HwPortalPacketStatisticsAuthenticatorError_Type()
)
hwPortalPacketStatisticsAuthenticatorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsAuthenticatorError.setStatus("current")
_HwPortalPacketStatisticsAccessReqError_Type = Counter64
_HwPortalPacketStatisticsAccessReqError_Object = MibScalar
hwPortalPacketStatisticsAccessReqError = _HwPortalPacketStatisticsAccessReqError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 3),
    _HwPortalPacketStatisticsAccessReqError_Type()
)
hwPortalPacketStatisticsAccessReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsAccessReqError.setStatus("current")
_HwPortalPacketStatisticsLogoutReqError_Type = Counter64
_HwPortalPacketStatisticsLogoutReqError_Object = MibScalar
hwPortalPacketStatisticsLogoutReqError = _HwPortalPacketStatisticsLogoutReqError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 4),
    _HwPortalPacketStatisticsLogoutReqError_Type()
)
hwPortalPacketStatisticsLogoutReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLogoutReqError.setStatus("current")
_HwPortalPacketStatisticsInquiryReqError_Type = Counter64
_HwPortalPacketStatisticsInquiryReqError_Object = MibScalar
hwPortalPacketStatisticsInquiryReqError = _HwPortalPacketStatisticsInquiryReqError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 5),
    _HwPortalPacketStatisticsInquiryReqError_Type()
)
hwPortalPacketStatisticsInquiryReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsInquiryReqError.setStatus("current")
_HwPortalPacketStatisticsLoginConfirmError_Type = Counter64
_HwPortalPacketStatisticsLoginConfirmError_Object = MibScalar
hwPortalPacketStatisticsLoginConfirmError = _HwPortalPacketStatisticsLoginConfirmError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 6),
    _HwPortalPacketStatisticsLoginConfirmError_Type()
)
hwPortalPacketStatisticsLoginConfirmError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLoginConfirmError.setStatus("current")
_HwPortalPacketStatisticsAccessReqReceived_Type = Counter64
_HwPortalPacketStatisticsAccessReqReceived_Object = MibScalar
hwPortalPacketStatisticsAccessReqReceived = _HwPortalPacketStatisticsAccessReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 7),
    _HwPortalPacketStatisticsAccessReqReceived_Type()
)
hwPortalPacketStatisticsAccessReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsAccessReqReceived.setStatus("current")
_HwPortalPacketStatisticsLoginReqReceived_Type = Counter64
_HwPortalPacketStatisticsLoginReqReceived_Object = MibScalar
hwPortalPacketStatisticsLoginReqReceived = _HwPortalPacketStatisticsLoginReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 8),
    _HwPortalPacketStatisticsLoginReqReceived_Type()
)
hwPortalPacketStatisticsLoginReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLoginReqReceived.setStatus("current")
_HwPortalPacketStatisticsLogoutReqReceived_Type = Counter64
_HwPortalPacketStatisticsLogoutReqReceived_Object = MibScalar
hwPortalPacketStatisticsLogoutReqReceived = _HwPortalPacketStatisticsLogoutReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 9),
    _HwPortalPacketStatisticsLogoutReqReceived_Type()
)
hwPortalPacketStatisticsLogoutReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLogoutReqReceived.setStatus("current")
_HwPortalPacketStatisticsInquiryReqReceived_Type = Counter64
_HwPortalPacketStatisticsInquiryReqReceived_Object = MibScalar
hwPortalPacketStatisticsInquiryReqReceived = _HwPortalPacketStatisticsInquiryReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 10),
    _HwPortalPacketStatisticsInquiryReqReceived_Type()
)
hwPortalPacketStatisticsInquiryReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsInquiryReqReceived.setStatus("current")
_HwPortalPacketStatisticsLoginConfirmReceived_Type = Counter64
_HwPortalPacketStatisticsLoginConfirmReceived_Object = MibScalar
hwPortalPacketStatisticsLoginConfirmReceived = _HwPortalPacketStatisticsLoginConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 11),
    _HwPortalPacketStatisticsLoginConfirmReceived_Type()
)
hwPortalPacketStatisticsLoginConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLoginConfirmReceived.setStatus("current")
_HwPortalPacketStatisticsAccessACKFailed_Type = Counter64
_HwPortalPacketStatisticsAccessACKFailed_Object = MibScalar
hwPortalPacketStatisticsAccessACKFailed = _HwPortalPacketStatisticsAccessACKFailed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 12),
    _HwPortalPacketStatisticsAccessACKFailed_Type()
)
hwPortalPacketStatisticsAccessACKFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsAccessACKFailed.setStatus("current")
_HwPortalPacketStatisticsLoginACKFailed_Type = Counter64
_HwPortalPacketStatisticsLoginACKFailed_Object = MibScalar
hwPortalPacketStatisticsLoginACKFailed = _HwPortalPacketStatisticsLoginACKFailed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 13),
    _HwPortalPacketStatisticsLoginACKFailed_Type()
)
hwPortalPacketStatisticsLoginACKFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLoginACKFailed.setStatus("current")
_HwPortalPacketStatisticsLogoutACKFailed_Type = Counter64
_HwPortalPacketStatisticsLogoutACKFailed_Object = MibScalar
hwPortalPacketStatisticsLogoutACKFailed = _HwPortalPacketStatisticsLogoutACKFailed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 14),
    _HwPortalPacketStatisticsLogoutACKFailed_Type()
)
hwPortalPacketStatisticsLogoutACKFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLogoutACKFailed.setStatus("current")
_HwPortalPacketStatisticsInquiryACKFailed_Type = Counter64
_HwPortalPacketStatisticsInquiryACKFailed_Object = MibScalar
hwPortalPacketStatisticsInquiryACKFailed = _HwPortalPacketStatisticsInquiryACKFailed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 15),
    _HwPortalPacketStatisticsInquiryACKFailed_Type()
)
hwPortalPacketStatisticsInquiryACKFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsInquiryACKFailed.setStatus("current")
_HwPortalPacketStatisticsAccessAckSent_Type = Counter64
_HwPortalPacketStatisticsAccessAckSent_Object = MibScalar
hwPortalPacketStatisticsAccessAckSent = _HwPortalPacketStatisticsAccessAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 16),
    _HwPortalPacketStatisticsAccessAckSent_Type()
)
hwPortalPacketStatisticsAccessAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsAccessAckSent.setStatus("current")
_HwPortalPacketStatisticsLoginAckSent_Type = Counter64
_HwPortalPacketStatisticsLoginAckSent_Object = MibScalar
hwPortalPacketStatisticsLoginAckSent = _HwPortalPacketStatisticsLoginAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 17),
    _HwPortalPacketStatisticsLoginAckSent_Type()
)
hwPortalPacketStatisticsLoginAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLoginAckSent.setStatus("current")
_HwPortalPacketStatisticsLogoutAckSent_Type = Counter64
_HwPortalPacketStatisticsLogoutAckSent_Object = MibScalar
hwPortalPacketStatisticsLogoutAckSent = _HwPortalPacketStatisticsLogoutAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 18),
    _HwPortalPacketStatisticsLogoutAckSent_Type()
)
hwPortalPacketStatisticsLogoutAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsLogoutAckSent.setStatus("current")
_HwPortalPacketStatisticsInquiryAckSent_Type = Counter64
_HwPortalPacketStatisticsInquiryAckSent_Object = MibScalar
hwPortalPacketStatisticsInquiryAckSent = _HwPortalPacketStatisticsInquiryAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 2, 19),
    _HwPortalPacketStatisticsInquiryAckSent_Type()
)
hwPortalPacketStatisticsInquiryAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsInquiryAckSent.setStatus("current")
_HwPortalConfigSecretKeyTable_Object = MibTable
hwPortalConfigSecretKeyTable = _HwPortalConfigSecretKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyTable.setStatus("current")
_HwPortalConfigSecretKeyEntry_Object = MibTableRow
hwPortalConfigSecretKeyEntry = _HwPortalConfigSecretKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1)
)
hwPortalConfigSecretKeyEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpAddress"),
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyEntry.setStatus("current")
_HwPortalConfigPortalServerIpAddress_Type = IpAddress
_HwPortalConfigPortalServerIpAddress_Object = MibTableColumn
hwPortalConfigPortalServerIpAddress = _HwPortalConfigPortalServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 1),
    _HwPortalConfigPortalServerIpAddress_Type()
)
hwPortalConfigPortalServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerIpAddress.setStatus("current")
_HwPortalConfigPortalServerIpMask_Type = IpAddress
_HwPortalConfigPortalServerIpMask_Object = MibTableColumn
hwPortalConfigPortalServerIpMask = _HwPortalConfigPortalServerIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 2),
    _HwPortalConfigPortalServerIpMask_Type()
)
hwPortalConfigPortalServerIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerIpMask.setStatus("current")


class _HwPortalConfigSecretKey_Type(DisplayString):
    """Custom type hwPortalConfigSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPortalConfigSecretKey_Type.__name__ = "DisplayString"
_HwPortalConfigSecretKey_Object = MibTableColumn
hwPortalConfigSecretKey = _HwPortalConfigSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 3),
    _HwPortalConfigSecretKey_Type()
)
hwPortalConfigSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigSecretKey.setStatus("current")
_HwPortalConfigPortalServerPort_Type = Integer32
_HwPortalConfigPortalServerPort_Object = MibTableColumn
hwPortalConfigPortalServerPort = _HwPortalConfigPortalServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 4),
    _HwPortalConfigPortalServerPort_Type()
)
hwPortalConfigPortalServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerPort.setStatus("current")


class _HwPortalConfigPortalServerNasip_Type(TruthValue):
    """Custom type hwPortalConfigPortalServerNasip based on TruthValue"""


_HwPortalConfigPortalServerNasip_Object = MibTableColumn
hwPortalConfigPortalServerNasip = _HwPortalConfigPortalServerNasip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 5),
    _HwPortalConfigPortalServerNasip_Type()
)
hwPortalConfigPortalServerNasip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerNasip.setStatus("current")
_HwPortalConfigStatus_Type = RowStatus
_HwPortalConfigStatus_Object = MibTableColumn
hwPortalConfigStatus = _HwPortalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 3, 1, 6),
    _HwPortalConfigStatus_Type()
)
hwPortalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigStatus.setStatus("current")
_HwPortalServerTable_Object = MibTable
hwPortalServerTable = _HwPortalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hwPortalServerTable.setStatus("current")
_HwPortalServerEntry_Object = MibTableRow
hwPortalServerEntry = _HwPortalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 4, 1)
)
hwPortalServerEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-PORTAL-MIB", "hwPortalServerIpAddress"),
)
if mibBuilder.loadTexts:
    hwPortalServerEntry.setStatus("current")
_HwPortalServerIpAddress_Type = IpAddress
_HwPortalServerIpAddress_Object = MibTableColumn
hwPortalServerIpAddress = _HwPortalServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 4, 1, 1),
    _HwPortalServerIpAddress_Type()
)
hwPortalServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalServerIpAddress.setStatus("current")
_HwPortalServerUserNum_Type = Integer32
_HwPortalServerUserNum_Object = MibTableColumn
hwPortalServerUserNum = _HwPortalServerUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 4, 1, 2),
    _HwPortalServerUserNum_Type()
)
hwPortalServerUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalServerUserNum.setStatus("current")
_HwPortalUserTable_Object = MibTable
hwPortalUserTable = _HwPortalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5)
)
if mibBuilder.loadTexts:
    hwPortalUserTable.setStatus("current")
_HwPortalUserEntry_Object = MibTableRow
hwPortalUserEntry = _HwPortalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1)
)
hwPortalUserEntry.setIndexNames(
    (0, "HUAWEI-PORTAL-MIB", "hwPortalUserMACAddress"),
)
if mibBuilder.loadTexts:
    hwPortalUserEntry.setStatus("current")
_HwPortalUserMACAddress_Type = MacAddress
_HwPortalUserMACAddress_Object = MibTableColumn
hwPortalUserMACAddress = _HwPortalUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 1),
    _HwPortalUserMACAddress_Type()
)
hwPortalUserMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserMACAddress.setStatus("current")
_HwPortalUserIpAddress_Type = IpAddress
_HwPortalUserIpAddress_Object = MibTableColumn
hwPortalUserIpAddress = _HwPortalUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 2),
    _HwPortalUserIpAddress_Type()
)
hwPortalUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserIpAddress.setStatus("current")
_HwPortalUserPort_Type = OctetString
_HwPortalUserPort_Object = MibTableColumn
hwPortalUserPort = _HwPortalUserPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 3),
    _HwPortalUserPort_Type()
)
hwPortalUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserPort.setStatus("current")
_HwPortalUserUpFlow_Type = Integer32
_HwPortalUserUpFlow_Object = MibTableColumn
hwPortalUserUpFlow = _HwPortalUserUpFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 4),
    _HwPortalUserUpFlow_Type()
)
hwPortalUserUpFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserUpFlow.setStatus("current")
_HwPortalUserDownFlow_Type = Counter64
_HwPortalUserDownFlow_Object = MibTableColumn
hwPortalUserDownFlow = _HwPortalUserDownFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 5),
    _HwPortalUserDownFlow_Type()
)
hwPortalUserDownFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserDownFlow.setStatus("current")


class _HwPortalUserName_Type(OctetString):
    """Custom type hwPortalUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwPortalUserName_Type.__name__ = "OctetString"
_HwPortalUserName_Object = MibTableColumn
hwPortalUserName = _HwPortalUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 6),
    _HwPortalUserName_Type()
)
hwPortalUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserName.setStatus("current")
_HwPortalUserLoginTime_Type = Integer32
_HwPortalUserLoginTime_Object = MibTableColumn
hwPortalUserLoginTime = _HwPortalUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 7),
    _HwPortalUserLoginTime_Type()
)
hwPortalUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserLoginTime.setStatus("current")
_HwPortalUserServerIpAddress_Type = IpAddress
_HwPortalUserServerIpAddress_Object = MibTableColumn
hwPortalUserServerIpAddress = _HwPortalUserServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 5, 1, 8),
    _HwPortalUserServerIpAddress_Type()
)
hwPortalUserServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalUserServerIpAddress.setStatus("current")
_HwPortalConfigSecretKeyTableV2_Object = MibTable
hwPortalConfigSecretKeyTableV2 = _HwPortalConfigSecretKeyTableV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6)
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyTableV2.setStatus("current")
_HwPortalConfigSecretKeyEntryV2_Object = MibTableRow
hwPortalConfigSecretKeyEntryV2 = _HwPortalConfigSecretKeyEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1)
)
hwPortalConfigSecretKeyEntryV2.setIndexNames(
    (0, "HUAWEI-PORTAL-MIB", "hwPortalVrfNameV2"),
    (0, "HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpAddressV2"),
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyEntryV2.setStatus("current")
_HwPortalConfigPortalServerIpAddressV2_Type = IpAddress
_HwPortalConfigPortalServerIpAddressV2_Object = MibTableColumn
hwPortalConfigPortalServerIpAddressV2 = _HwPortalConfigPortalServerIpAddressV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 1),
    _HwPortalConfigPortalServerIpAddressV2_Type()
)
hwPortalConfigPortalServerIpAddressV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerIpAddressV2.setStatus("current")
_HwPortalConfigPortalServerIpMaskV2_Type = IpAddress
_HwPortalConfigPortalServerIpMaskV2_Object = MibTableColumn
hwPortalConfigPortalServerIpMaskV2 = _HwPortalConfigPortalServerIpMaskV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 2),
    _HwPortalConfigPortalServerIpMaskV2_Type()
)
hwPortalConfigPortalServerIpMaskV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerIpMaskV2.setStatus("current")


class _HwPortalConfigSecretKeyV2_Type(DisplayString):
    """Custom type hwPortalConfigSecretKeyV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPortalConfigSecretKeyV2_Type.__name__ = "DisplayString"
_HwPortalConfigSecretKeyV2_Object = MibTableColumn
hwPortalConfigSecretKeyV2 = _HwPortalConfigSecretKeyV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 3),
    _HwPortalConfigSecretKeyV2_Type()
)
hwPortalConfigSecretKeyV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyV2.setStatus("current")
_HwPortalConfigPortalServerPortV2_Type = Integer32
_HwPortalConfigPortalServerPortV2_Object = MibTableColumn
hwPortalConfigPortalServerPortV2 = _HwPortalConfigPortalServerPortV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 4),
    _HwPortalConfigPortalServerPortV2_Type()
)
hwPortalConfigPortalServerPortV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerPortV2.setStatus("current")


class _HwPortalConfigPortalServerNasipV2_Type(TruthValue):
    """Custom type hwPortalConfigPortalServerNasipV2 based on TruthValue"""


_HwPortalConfigPortalServerNasipV2_Object = MibTableColumn
hwPortalConfigPortalServerNasipV2 = _HwPortalConfigPortalServerNasipV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 5),
    _HwPortalConfigPortalServerNasipV2_Type()
)
hwPortalConfigPortalServerNasipV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigPortalServerNasipV2.setStatus("current")
_HwPortalConfigStatusV2_Type = RowStatus
_HwPortalConfigStatusV2_Object = MibTableColumn
hwPortalConfigStatusV2 = _HwPortalConfigStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 6),
    _HwPortalConfigStatusV2_Type()
)
hwPortalConfigStatusV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortalConfigStatusV2.setStatus("current")


class _HwPortalVrfNameV2_Type(DisplayString):
    """Custom type hwPortalVrfNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPortalVrfNameV2_Type.__name__ = "DisplayString"
_HwPortalVrfNameV2_Object = MibTableColumn
hwPortalVrfNameV2 = _HwPortalVrfNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 6, 1, 7),
    _HwPortalVrfNameV2_Type()
)
hwPortalVrfNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalVrfNameV2.setStatus("current")
_HwPortalServerTableV2_Object = MibTable
hwPortalServerTableV2 = _HwPortalServerTableV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 7)
)
if mibBuilder.loadTexts:
    hwPortalServerTableV2.setStatus("current")
_HwPortalServerEntryV2_Object = MibTableRow
hwPortalServerEntryV2 = _HwPortalServerEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 7, 1)
)
hwPortalServerEntryV2.setIndexNames(
    (0, "HUAWEI-PORTAL-MIB", "hwPortalVrfNameV2"),
    (0, "HUAWEI-PORTAL-MIB", "hwPortalServerIpAddressV2"),
)
if mibBuilder.loadTexts:
    hwPortalServerEntryV2.setStatus("current")
_HwPortalServerIpAddressV2_Type = IpAddress
_HwPortalServerIpAddressV2_Object = MibTableColumn
hwPortalServerIpAddressV2 = _HwPortalServerIpAddressV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 7, 1, 1),
    _HwPortalServerIpAddressV2_Type()
)
hwPortalServerIpAddressV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalServerIpAddressV2.setStatus("current")
_HwPortalServerUserNumV2_Type = Integer32
_HwPortalServerUserNumV2_Object = MibTableColumn
hwPortalServerUserNumV2 = _HwPortalServerUserNumV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 1, 7, 1, 2),
    _HwPortalServerUserNumV2_Type()
)
hwPortalServerUserNumV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalServerUserNumV2.setStatus("current")
_HwPortalConformance_ObjectIdentity = ObjectIdentity
hwPortalConformance = _HwPortalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3)
)
_HwPortalCompliances_ObjectIdentity = ObjectIdentity
hwPortalCompliances = _HwPortalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 1)
)
_HwPortalObjectGroups_ObjectIdentity = ObjectIdentity
hwPortalObjectGroups = _HwPortalObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2)
)

# Managed Objects groups

hwPortalConfigParaObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 1)
)
hwPortalConfigParaObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalConfigVersionSupport"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigTextInfoSwitch"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigServerUdpReceivePort"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigServerUdpSendPort"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigTrapUdpPort"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigSourecIfIndex"))
)
if mibBuilder.loadTexts:
    hwPortalConfigParaObjectGroup.setStatus("current")

hwPortalPacketStatisticsParaObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 2)
)
hwPortalPacketStatisticsParaObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalStatisticsBeginTime"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsAuthenticatorError"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsAccessReqError"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLogoutReqError"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsInquiryReqError"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLoginConfirmError"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsAccessReqReceived"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLoginReqReceived"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLogoutReqReceived"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsInquiryReqReceived"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLoginConfirmReceived"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsAccessACKFailed"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLoginACKFailed"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLogoutACKFailed"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsInquiryACKFailed"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsAccessAckSent"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLoginAckSent"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsLogoutAckSent"),
        ("HUAWEI-PORTAL-MIB", "hwPortalPacketStatisticsInquiryAckSent"))
)
if mibBuilder.loadTexts:
    hwPortalPacketStatisticsParaObjectGroup.setStatus("current")

hwPortalConfigSecretKeyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 3)
)
hwPortalConfigSecretKeyObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpAddress"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpMask"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigSecretKey"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerPort"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerNasip"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigStatus"))
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyObjectGroup.setStatus("current")

hwPortalServerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 4)
)
hwPortalServerObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalServerIpAddress"),
        ("HUAWEI-PORTAL-MIB", "hwPortalServerUserNum"))
)
if mibBuilder.loadTexts:
    hwPortalServerObjectGroup.setStatus("current")

hwPortalUserObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 5)
)
hwPortalUserObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalUserMACAddress"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserIpAddress"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserPort"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserUpFlow"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserDownFlow"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserName"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserLoginTime"),
        ("HUAWEI-PORTAL-MIB", "hwPortalUserServerIpAddress"))
)
if mibBuilder.loadTexts:
    hwPortalUserObjectGroup.setStatus("current")

hwPortalConfigSecretKeyV2ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 6)
)
hwPortalConfigSecretKeyV2ObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpAddressV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerIpMaskV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigSecretKeyV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerPortV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigPortalServerNasipV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalConfigStatusV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalVrfNameV2"))
)
if mibBuilder.loadTexts:
    hwPortalConfigSecretKeyV2ObjectGroup.setStatus("current")

hwPortalServerV2ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 2, 7)
)
hwPortalServerV2ObjectGroup.setObjects(
      *(("HUAWEI-PORTAL-MIB", "hwPortalServerIpAddressV2"),
        ("HUAWEI-PORTAL-MIB", "hwPortalServerUserNumV2"))
)
if mibBuilder.loadTexts:
    hwPortalServerV2ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPortalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwPortalCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PORTAL-MIB",
    **{"hwPortal": hwPortal,
       "hwPortalMibObjects": hwPortalMibObjects,
       "hwPortalConfigPara": hwPortalConfigPara,
       "hwPortalConfigVersionSupport": hwPortalConfigVersionSupport,
       "hwPortalConfigTextInfoSwitch": hwPortalConfigTextInfoSwitch,
       "hwPortalConfigServerUdpReceivePort": hwPortalConfigServerUdpReceivePort,
       "hwPortalConfigServerUdpSendPort": hwPortalConfigServerUdpSendPort,
       "hwPortalConfigTrapUdpPort": hwPortalConfigTrapUdpPort,
       "hwPortalConfigSourecIfIndex": hwPortalConfigSourecIfIndex,
       "hwPortalPacketStatisticsPara": hwPortalPacketStatisticsPara,
       "hwPortalStatisticsBeginTime": hwPortalStatisticsBeginTime,
       "hwPortalPacketStatisticsAuthenticatorError": hwPortalPacketStatisticsAuthenticatorError,
       "hwPortalPacketStatisticsAccessReqError": hwPortalPacketStatisticsAccessReqError,
       "hwPortalPacketStatisticsLogoutReqError": hwPortalPacketStatisticsLogoutReqError,
       "hwPortalPacketStatisticsInquiryReqError": hwPortalPacketStatisticsInquiryReqError,
       "hwPortalPacketStatisticsLoginConfirmError": hwPortalPacketStatisticsLoginConfirmError,
       "hwPortalPacketStatisticsAccessReqReceived": hwPortalPacketStatisticsAccessReqReceived,
       "hwPortalPacketStatisticsLoginReqReceived": hwPortalPacketStatisticsLoginReqReceived,
       "hwPortalPacketStatisticsLogoutReqReceived": hwPortalPacketStatisticsLogoutReqReceived,
       "hwPortalPacketStatisticsInquiryReqReceived": hwPortalPacketStatisticsInquiryReqReceived,
       "hwPortalPacketStatisticsLoginConfirmReceived": hwPortalPacketStatisticsLoginConfirmReceived,
       "hwPortalPacketStatisticsAccessACKFailed": hwPortalPacketStatisticsAccessACKFailed,
       "hwPortalPacketStatisticsLoginACKFailed": hwPortalPacketStatisticsLoginACKFailed,
       "hwPortalPacketStatisticsLogoutACKFailed": hwPortalPacketStatisticsLogoutACKFailed,
       "hwPortalPacketStatisticsInquiryACKFailed": hwPortalPacketStatisticsInquiryACKFailed,
       "hwPortalPacketStatisticsAccessAckSent": hwPortalPacketStatisticsAccessAckSent,
       "hwPortalPacketStatisticsLoginAckSent": hwPortalPacketStatisticsLoginAckSent,
       "hwPortalPacketStatisticsLogoutAckSent": hwPortalPacketStatisticsLogoutAckSent,
       "hwPortalPacketStatisticsInquiryAckSent": hwPortalPacketStatisticsInquiryAckSent,
       "hwPortalConfigSecretKeyTable": hwPortalConfigSecretKeyTable,
       "hwPortalConfigSecretKeyEntry": hwPortalConfigSecretKeyEntry,
       "hwPortalConfigPortalServerIpAddress": hwPortalConfigPortalServerIpAddress,
       "hwPortalConfigPortalServerIpMask": hwPortalConfigPortalServerIpMask,
       "hwPortalConfigSecretKey": hwPortalConfigSecretKey,
       "hwPortalConfigPortalServerPort": hwPortalConfigPortalServerPort,
       "hwPortalConfigPortalServerNasip": hwPortalConfigPortalServerNasip,
       "hwPortalConfigStatus": hwPortalConfigStatus,
       "hwPortalServerTable": hwPortalServerTable,
       "hwPortalServerEntry": hwPortalServerEntry,
       "hwPortalServerIpAddress": hwPortalServerIpAddress,
       "hwPortalServerUserNum": hwPortalServerUserNum,
       "hwPortalUserTable": hwPortalUserTable,
       "hwPortalUserEntry": hwPortalUserEntry,
       "hwPortalUserMACAddress": hwPortalUserMACAddress,
       "hwPortalUserIpAddress": hwPortalUserIpAddress,
       "hwPortalUserPort": hwPortalUserPort,
       "hwPortalUserUpFlow": hwPortalUserUpFlow,
       "hwPortalUserDownFlow": hwPortalUserDownFlow,
       "hwPortalUserName": hwPortalUserName,
       "hwPortalUserLoginTime": hwPortalUserLoginTime,
       "hwPortalUserServerIpAddress": hwPortalUserServerIpAddress,
       "hwPortalConfigSecretKeyTableV2": hwPortalConfigSecretKeyTableV2,
       "hwPortalConfigSecretKeyEntryV2": hwPortalConfigSecretKeyEntryV2,
       "hwPortalConfigPortalServerIpAddressV2": hwPortalConfigPortalServerIpAddressV2,
       "hwPortalConfigPortalServerIpMaskV2": hwPortalConfigPortalServerIpMaskV2,
       "hwPortalConfigSecretKeyV2": hwPortalConfigSecretKeyV2,
       "hwPortalConfigPortalServerPortV2": hwPortalConfigPortalServerPortV2,
       "hwPortalConfigPortalServerNasipV2": hwPortalConfigPortalServerNasipV2,
       "hwPortalConfigStatusV2": hwPortalConfigStatusV2,
       "hwPortalVrfNameV2": hwPortalVrfNameV2,
       "hwPortalServerTableV2": hwPortalServerTableV2,
       "hwPortalServerEntryV2": hwPortalServerEntryV2,
       "hwPortalServerIpAddressV2": hwPortalServerIpAddressV2,
       "hwPortalServerUserNumV2": hwPortalServerUserNumV2,
       "hwPortalConformance": hwPortalConformance,
       "hwPortalCompliances": hwPortalCompliances,
       "hwPortalCompliance": hwPortalCompliance,
       "hwPortalObjectGroups": hwPortalObjectGroups,
       "hwPortalConfigParaObjectGroup": hwPortalConfigParaObjectGroup,
       "hwPortalPacketStatisticsParaObjectGroup": hwPortalPacketStatisticsParaObjectGroup,
       "hwPortalConfigSecretKeyObjectGroup": hwPortalConfigSecretKeyObjectGroup,
       "hwPortalServerObjectGroup": hwPortalServerObjectGroup,
       "hwPortalUserObjectGroup": hwPortalUserObjectGroup,
       "hwPortalConfigSecretKeyV2ObjectGroup": hwPortalConfigSecretKeyV2ObjectGroup,
       "hwPortalServerV2ObjectGroup": hwPortalServerV2ObjectGroup}
)
