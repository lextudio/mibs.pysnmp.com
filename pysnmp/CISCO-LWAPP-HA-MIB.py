# SNMP MIB module (CISCO-LWAPP-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-HA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:34 2024
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

(cRFStatusPeerUnitState,
 cRFStatusUnitState) = mibBuilder.importSymbols(
    "CISCO-RF-MIB",
    "cRFStatusPeerUnitState",
    "cRFStatusUnitState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappHaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888)
)
ciscoLwappHaMIB.setRevisions(
        ("2012-01-24 11:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappHaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBObjects = _CiscoLwappHaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0)
)
_CiscoLwappHaGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappHaGlobalConfig = _CiscoLwappHaGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1)
)
_CLHaApSsoConfig_Type = TruthValue
_CLHaApSsoConfig_Object = MibScalar
cLHaApSsoConfig = _CLHaApSsoConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 1),
    _CLHaApSsoConfig_Type()
)
cLHaApSsoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaApSsoConfig.setStatus("current")
_CLHaPeerIpAddressType_Type = InetAddressType
_CLHaPeerIpAddressType_Object = MibScalar
cLHaPeerIpAddressType = _CLHaPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 2),
    _CLHaPeerIpAddressType_Type()
)
cLHaPeerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPeerIpAddressType.setStatus("current")
_CLHaPeerIpAddress_Type = InetAddress
_CLHaPeerIpAddress_Object = MibScalar
cLHaPeerIpAddress = _CLHaPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 3),
    _CLHaPeerIpAddress_Type()
)
cLHaPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPeerIpAddress.setStatus("current")
_CLHaServicePortPeerIpAddressType_Type = InetAddressType
_CLHaServicePortPeerIpAddressType_Object = MibScalar
cLHaServicePortPeerIpAddressType = _CLHaServicePortPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 4),
    _CLHaServicePortPeerIpAddressType_Type()
)
cLHaServicePortPeerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpAddressType.setStatus("current")
_CLHaServicePortPeerIpAddress_Type = InetAddress
_CLHaServicePortPeerIpAddress_Object = MibScalar
cLHaServicePortPeerIpAddress = _CLHaServicePortPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 5),
    _CLHaServicePortPeerIpAddress_Type()
)
cLHaServicePortPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpAddress.setStatus("current")
_CLHaServicePortPeerIpNetMaskType_Type = InetAddressType
_CLHaServicePortPeerIpNetMaskType_Object = MibScalar
cLHaServicePortPeerIpNetMaskType = _CLHaServicePortPeerIpNetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 6),
    _CLHaServicePortPeerIpNetMaskType_Type()
)
cLHaServicePortPeerIpNetMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpNetMaskType.setStatus("current")
_CLHaServicePortPeerIpNetMask_Type = InetAddress
_CLHaServicePortPeerIpNetMask_Object = MibScalar
cLHaServicePortPeerIpNetMask = _CLHaServicePortPeerIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 7),
    _CLHaServicePortPeerIpNetMask_Type()
)
cLHaServicePortPeerIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpNetMask.setStatus("current")
_CLHaRedundancyIpAddressType_Type = InetAddressType
_CLHaRedundancyIpAddressType_Object = MibScalar
cLHaRedundancyIpAddressType = _CLHaRedundancyIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 8),
    _CLHaRedundancyIpAddressType_Type()
)
cLHaRedundancyIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRedundancyIpAddressType.setStatus("current")
_CLHaRedundancyIpAddress_Type = InetAddress
_CLHaRedundancyIpAddress_Object = MibScalar
cLHaRedundancyIpAddress = _CLHaRedundancyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 9),
    _CLHaRedundancyIpAddress_Type()
)
cLHaRedundancyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRedundancyIpAddress.setStatus("current")
_CLHaPeerMacAddress_Type = MacAddress
_CLHaPeerMacAddress_Object = MibScalar
cLHaPeerMacAddress = _CLHaPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 10),
    _CLHaPeerMacAddress_Type()
)
cLHaPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPeerMacAddress.setStatus("current")
_CLHaVirtualMacAddress_Type = MacAddress
_CLHaVirtualMacAddress_Object = MibScalar
cLHaVirtualMacAddress = _CLHaVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 11),
    _CLHaVirtualMacAddress_Type()
)
cLHaVirtualMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaVirtualMacAddress.setStatus("current")
_CLHaPrimaryUnit_Type = TruthValue
_CLHaPrimaryUnit_Object = MibScalar
cLHaPrimaryUnit = _CLHaPrimaryUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 12),
    _CLHaPrimaryUnit_Type()
)
cLHaPrimaryUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPrimaryUnit.setStatus("current")
_CLHaLinkEncryption_Type = TruthValue
_CLHaLinkEncryption_Object = MibScalar
cLHaLinkEncryption = _CLHaLinkEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 13),
    _CLHaLinkEncryption_Type()
)
cLHaLinkEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaLinkEncryption.setStatus("current")
_CLHaNetworkFailOver_Type = TruthValue
_CLHaNetworkFailOver_Object = MibScalar
cLHaNetworkFailOver = _CLHaNetworkFailOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 14),
    _CLHaNetworkFailOver_Type()
)
cLHaNetworkFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaNetworkFailOver.setStatus("current")
_CLHaRFStatusUnitIp_Type = InetAddress
_CLHaRFStatusUnitIp_Object = MibScalar
cLHaRFStatusUnitIp = _CLHaRFStatusUnitIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 1, 15),
    _CLHaRFStatusUnitIp_Type()
)
cLHaRFStatusUnitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRFStatusUnitIp.setStatus("current")
_CiscoLwappHaNetworkConfig_ObjectIdentity = ObjectIdentity
ciscoLwappHaNetworkConfig = _CiscoLwappHaNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2)
)
_CLHaNetworkRoutePeerConfigTable_Object = MibTable
cLHaNetworkRoutePeerConfigTable = _CLHaNetworkRoutePeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1)
)
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerConfigTable.setStatus("current")
_CLHaNetworkRoutePeerConfigEntry_Object = MibTableRow
cLHaNetworkRoutePeerConfigEntry = _CLHaNetworkRoutePeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1)
)
cLHaNetworkRoutePeerConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPAddressType"),
    (0, "CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPAddress"),
)
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerConfigEntry.setStatus("current")
_CLHaNetworkRoutePeerIPAddressType_Type = InetAddressType
_CLHaNetworkRoutePeerIPAddressType_Object = MibTableColumn
cLHaNetworkRoutePeerIPAddressType = _CLHaNetworkRoutePeerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 1),
    _CLHaNetworkRoutePeerIPAddressType_Type()
)
cLHaNetworkRoutePeerIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPAddressType.setStatus("current")
_CLHaNetworkRoutePeerIPAddress_Type = InetAddress
_CLHaNetworkRoutePeerIPAddress_Object = MibTableColumn
cLHaNetworkRoutePeerIPAddress = _CLHaNetworkRoutePeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 2),
    _CLHaNetworkRoutePeerIPAddress_Type()
)
cLHaNetworkRoutePeerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPAddress.setStatus("current")
_CLHaNetworkRoutePeerIPNetmaskType_Type = InetAddressType
_CLHaNetworkRoutePeerIPNetmaskType_Object = MibTableColumn
cLHaNetworkRoutePeerIPNetmaskType = _CLHaNetworkRoutePeerIPNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 3),
    _CLHaNetworkRoutePeerIPNetmaskType_Type()
)
cLHaNetworkRoutePeerIPNetmaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPNetmaskType.setStatus("current")
_CLHaNetworkRoutePeerIPNetmask_Type = InetAddress
_CLHaNetworkRoutePeerIPNetmask_Object = MibTableColumn
cLHaNetworkRoutePeerIPNetmask = _CLHaNetworkRoutePeerIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 4),
    _CLHaNetworkRoutePeerIPNetmask_Type()
)
cLHaNetworkRoutePeerIPNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPNetmask.setStatus("current")
_CLHaNetworkRoutePeerGatewayType_Type = InetAddressType
_CLHaNetworkRoutePeerGatewayType_Object = MibTableColumn
cLHaNetworkRoutePeerGatewayType = _CLHaNetworkRoutePeerGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 5),
    _CLHaNetworkRoutePeerGatewayType_Type()
)
cLHaNetworkRoutePeerGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerGatewayType.setStatus("current")
_CLHaNetworkRoutePeerGateway_Type = InetAddress
_CLHaNetworkRoutePeerGateway_Object = MibTableColumn
cLHaNetworkRoutePeerGateway = _CLHaNetworkRoutePeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 6),
    _CLHaNetworkRoutePeerGateway_Type()
)
cLHaNetworkRoutePeerGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerGateway.setStatus("current")


class _CLHaNetworkRoutePeerTransferStatus_Type(Integer32):
    """Custom type cLHaNetworkRoutePeerTransferStatus based on Integer32"""
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
        *(("failure", 4),
          ("inProgress", 2),
          ("initiate", 1),
          ("success", 3),
          ("timeout", 5))
    )


_CLHaNetworkRoutePeerTransferStatus_Type.__name__ = "Integer32"
_CLHaNetworkRoutePeerTransferStatus_Object = MibTableColumn
cLHaNetworkRoutePeerTransferStatus = _CLHaNetworkRoutePeerTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 7),
    _CLHaNetworkRoutePeerTransferStatus_Type()
)
cLHaNetworkRoutePeerTransferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerTransferStatus.setStatus("current")
_CLHaNetworkRoutePeerRowStatus_Type = RowStatus
_CLHaNetworkRoutePeerRowStatus_Object = MibTableColumn
cLHaNetworkRoutePeerRowStatus = _CLHaNetworkRoutePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 2, 1, 1, 8),
    _CLHaNetworkRoutePeerRowStatus_Type()
)
cLHaNetworkRoutePeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerRowStatus.setStatus("current")
_CiscoLwappHaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBNotifs = _CiscoLwappHaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 3)
)
_CiscoLwappHaNotificationVariable_ObjectIdentity = ObjectIdentity
ciscoLwappHaNotificationVariable = _CiscoLwappHaNotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 4)
)


class _CLHaSecondaryControllerUsageTrapType_Type(Integer32):
    """Custom type cLHaSecondaryControllerUsageTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("overUsage", 3),
          ("usageComplete", 2),
          ("usageStart", 1))
    )


_CLHaSecondaryControllerUsageTrapType_Type.__name__ = "Integer32"
_CLHaSecondaryControllerUsageTrapType_Object = MibScalar
cLHaSecondaryControllerUsageTrapType = _CLHaSecondaryControllerUsageTrapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 4, 1),
    _CLHaSecondaryControllerUsageTrapType_Type()
)
cLHaSecondaryControllerUsageTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageTrapType.setStatus("current")
_CLHaSecondaryControllerUsageDayCounter_Type = Counter32
_CLHaSecondaryControllerUsageDayCounter_Object = MibScalar
cLHaSecondaryControllerUsageDayCounter = _CLHaSecondaryControllerUsageDayCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 4, 2),
    _CLHaSecondaryControllerUsageDayCounter_Type()
)
cLHaSecondaryControllerUsageDayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageDayCounter.setStatus("current")

# Managed Objects groups


# Notification objects

cLHaSecondaryControllerUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 3, 1)
)
cLHaSecondaryControllerUsageTrap.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageTrapType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageDayCounter"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageTrap.setStatus(
        "current"
    )

cLHaRFSwapInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198888, 0, 3, 2)
)
cLHaRFSwapInfoTrap.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaRFStatusUnitIp"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerIpAddress"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitState"))
)
if mibBuilder.loadTexts:
    cLHaRFSwapInfoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-HA-MIB",
    **{"ciscoLwappHaMIB": ciscoLwappHaMIB,
       "ciscoLwappHaMIBObjects": ciscoLwappHaMIBObjects,
       "ciscoLwappHaGlobalConfig": ciscoLwappHaGlobalConfig,
       "cLHaApSsoConfig": cLHaApSsoConfig,
       "cLHaPeerIpAddressType": cLHaPeerIpAddressType,
       "cLHaPeerIpAddress": cLHaPeerIpAddress,
       "cLHaServicePortPeerIpAddressType": cLHaServicePortPeerIpAddressType,
       "cLHaServicePortPeerIpAddress": cLHaServicePortPeerIpAddress,
       "cLHaServicePortPeerIpNetMaskType": cLHaServicePortPeerIpNetMaskType,
       "cLHaServicePortPeerIpNetMask": cLHaServicePortPeerIpNetMask,
       "cLHaRedundancyIpAddressType": cLHaRedundancyIpAddressType,
       "cLHaRedundancyIpAddress": cLHaRedundancyIpAddress,
       "cLHaPeerMacAddress": cLHaPeerMacAddress,
       "cLHaVirtualMacAddress": cLHaVirtualMacAddress,
       "cLHaPrimaryUnit": cLHaPrimaryUnit,
       "cLHaLinkEncryption": cLHaLinkEncryption,
       "cLHaNetworkFailOver": cLHaNetworkFailOver,
       "cLHaRFStatusUnitIp": cLHaRFStatusUnitIp,
       "ciscoLwappHaNetworkConfig": ciscoLwappHaNetworkConfig,
       "cLHaNetworkRoutePeerConfigTable": cLHaNetworkRoutePeerConfigTable,
       "cLHaNetworkRoutePeerConfigEntry": cLHaNetworkRoutePeerConfigEntry,
       "cLHaNetworkRoutePeerIPAddressType": cLHaNetworkRoutePeerIPAddressType,
       "cLHaNetworkRoutePeerIPAddress": cLHaNetworkRoutePeerIPAddress,
       "cLHaNetworkRoutePeerIPNetmaskType": cLHaNetworkRoutePeerIPNetmaskType,
       "cLHaNetworkRoutePeerIPNetmask": cLHaNetworkRoutePeerIPNetmask,
       "cLHaNetworkRoutePeerGatewayType": cLHaNetworkRoutePeerGatewayType,
       "cLHaNetworkRoutePeerGateway": cLHaNetworkRoutePeerGateway,
       "cLHaNetworkRoutePeerTransferStatus": cLHaNetworkRoutePeerTransferStatus,
       "cLHaNetworkRoutePeerRowStatus": cLHaNetworkRoutePeerRowStatus,
       "ciscoLwappHaMIBNotifs": ciscoLwappHaMIBNotifs,
       "cLHaSecondaryControllerUsageTrap": cLHaSecondaryControllerUsageTrap,
       "cLHaRFSwapInfoTrap": cLHaRFSwapInfoTrap,
       "ciscoLwappHaNotificationVariable": ciscoLwappHaNotificationVariable,
       "cLHaSecondaryControllerUsageTrapType": cLHaSecondaryControllerUsageTrapType,
       "cLHaSecondaryControllerUsageDayCounter": cLHaSecondaryControllerUsageDayCounter}
)
