# SNMP MIB module (PDN-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:30 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_domain,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-domain")

(ClientState,
 SwitchState,
 VnidRange,
 VnidTaggingState) = mibBuilder.importSymbols(
    "PDN-TC",
    "ClientState",
    "SwitchState",
    "VnidRange",
    "VnidTaggingState")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDomainMIBObjects_ObjectIdentity = ObjectIdentity
pdnDomainMIBObjects = _PdnDomainMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1)
)
_PdnCardGeneralParams_ObjectIdentity = ObjectIdentity
pdnCardGeneralParams = _PdnCardGeneralParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 1)
)
_PdnCardGeneralParamsVNIDMode_Type = VnidTaggingState
_PdnCardGeneralParamsVNIDMode_Object = MibScalar
pdnCardGeneralParamsVNIDMode = _PdnCardGeneralParamsVNIDMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 1, 1),
    _PdnCardGeneralParamsVNIDMode_Type()
)
pdnCardGeneralParamsVNIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardGeneralParamsVNIDMode.setStatus("mandatory")
_PdnCardConfig_ObjectIdentity = ObjectIdentity
pdnCardConfig = _PdnCardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2)
)
_PdnCardConfigTable_Object = MibTable
pdnCardConfigTable = _PdnCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnCardConfigTable.setStatus("mandatory")
_PdnCardConfigEntry_Object = MibTableRow
pdnCardConfigEntry = _PdnCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1)
)
pdnCardConfigEntry.setIndexNames(
    (0, "PDN-DOMAIN-MIB", "pdnCardConfigVnidId"),
)
if mibBuilder.loadTexts:
    pdnCardConfigEntry.setStatus("mandatory")
_PdnCardConfigVnidId_Type = VnidRange
_PdnCardConfigVnidId_Object = MibTableColumn
pdnCardConfigVnidId = _PdnCardConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 1),
    _PdnCardConfigVnidId_Type()
)
pdnCardConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCardConfigVnidId.setStatus("mandatory")
_PdnCardConfigDomainName_Type = DisplayString
_PdnCardConfigDomainName_Object = MibTableColumn
pdnCardConfigDomainName = _PdnCardConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 2),
    _PdnCardConfigDomainName_Type()
)
pdnCardConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigDomainName.setStatus("mandatory")
_PdnCardConfigMuxFwd_Type = SwitchState
_PdnCardConfigMuxFwd_Object = MibTableColumn
pdnCardConfigMuxFwd = _PdnCardConfigMuxFwd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 3),
    _PdnCardConfigMuxFwd_Type()
)
pdnCardConfigMuxFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigMuxFwd.setStatus("mandatory")
_PdnCardConfigIPFiltering_Type = SwitchState
_PdnCardConfigIPFiltering_Object = MibTableColumn
pdnCardConfigIPFiltering = _PdnCardConfigIPFiltering_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 4),
    _PdnCardConfigIPFiltering_Type()
)
pdnCardConfigIPFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigIPFiltering.setStatus("mandatory")
_PdnCardConfigIPScoping_Type = SwitchState
_PdnCardConfigIPScoping_Object = MibTableColumn
pdnCardConfigIPScoping = _PdnCardConfigIPScoping_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 5),
    _PdnCardConfigIPScoping_Type()
)
pdnCardConfigIPScoping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigIPScoping.setStatus("mandatory")
_PdnCardConfigVnidAuth_Type = SwitchState
_PdnCardConfigVnidAuth_Object = MibTableColumn
pdnCardConfigVnidAuth = _PdnCardConfigVnidAuth_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 6),
    _PdnCardConfigVnidAuth_Type()
)
pdnCardConfigVnidAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigVnidAuth.setStatus("mandatory")
_PdnCardConfigRowStatus_Type = RowStatus
_PdnCardConfigRowStatus_Object = MibTableColumn
pdnCardConfigRowStatus = _PdnCardConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 7),
    _PdnCardConfigRowStatus_Type()
)
pdnCardConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigRowStatus.setStatus("mandatory")
_PdnClientConfig_ObjectIdentity = ObjectIdentity
pdnClientConfig = _PdnClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3)
)
_PdnClientConfigTable_Object = MibTable
pdnClientConfigTable = _PdnClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnClientConfigTable.setStatus("mandatory")
_PdnClientConfigEntry_Object = MibTableRow
pdnClientConfigEntry = _PdnClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1)
)
pdnClientConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-DOMAIN-MIB", "pdnClientConfigAddr"),
    (0, "PDN-DOMAIN-MIB", "pdnClientConfigSubnetMask"),
    (0, "PDN-DOMAIN-MIB", "pdnClientConfigVnidId"),
)
if mibBuilder.loadTexts:
    pdnClientConfigEntry.setStatus("mandatory")
_PdnClientConfigAddr_Type = IpAddress
_PdnClientConfigAddr_Object = MibTableColumn
pdnClientConfigAddr = _PdnClientConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 1),
    _PdnClientConfigAddr_Type()
)
pdnClientConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigAddr.setStatus("mandatory")
_PdnClientConfigSubnetMask_Type = IpAddress
_PdnClientConfigSubnetMask_Object = MibTableColumn
pdnClientConfigSubnetMask = _PdnClientConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 2),
    _PdnClientConfigSubnetMask_Type()
)
pdnClientConfigSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigSubnetMask.setStatus("mandatory")
_PdnClientConfigVnidId_Type = VnidRange
_PdnClientConfigVnidId_Object = MibTableColumn
pdnClientConfigVnidId = _PdnClientConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 3),
    _PdnClientConfigVnidId_Type()
)
pdnClientConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigVnidId.setStatus("mandatory")
_PdnClientConfigNHR_Type = IpAddress
_PdnClientConfigNHR_Object = MibTableColumn
pdnClientConfigNHR = _PdnClientConfigNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 4),
    _PdnClientConfigNHR_Type()
)
pdnClientConfigNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnClientConfigNHR.setStatus("mandatory")
_PdnClientConfigType_Type = ClientState
_PdnClientConfigType_Object = MibTableColumn
pdnClientConfigType = _PdnClientConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 5),
    _PdnClientConfigType_Type()
)
pdnClientConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigType.setStatus("mandatory")
_PdnClientConfigLeaseTime_Type = TimeTicks
_PdnClientConfigLeaseTime_Object = MibTableColumn
pdnClientConfigLeaseTime = _PdnClientConfigLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 6),
    _PdnClientConfigLeaseTime_Type()
)
pdnClientConfigLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigLeaseTime.setStatus("mandatory")
_PdnClientConfigLeaseRemainTime_Type = TimeTicks
_PdnClientConfigLeaseRemainTime_Object = MibTableColumn
pdnClientConfigLeaseRemainTime = _PdnClientConfigLeaseRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 7),
    _PdnClientConfigLeaseRemainTime_Type()
)
pdnClientConfigLeaseRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigLeaseRemainTime.setStatus("mandatory")
_PdnClientConfigMacAddr_Type = MacAddress
_PdnClientConfigMacAddr_Object = MibTableColumn
pdnClientConfigMacAddr = _PdnClientConfigMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 8),
    _PdnClientConfigMacAddr_Type()
)
pdnClientConfigMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigMacAddr.setStatus("mandatory")
_PdnClientConfigRowStatus_Type = RowStatus
_PdnClientConfigRowStatus_Object = MibTableColumn
pdnClientConfigRowStatus = _PdnClientConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 9),
    _PdnClientConfigRowStatus_Type()
)
pdnClientConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnClientConfigRowStatus.setStatus("mandatory")
_PdnMaxClientsTable_Object = MibTable
pdnMaxClientsTable = _PdnMaxClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pdnMaxClientsTable.setStatus("mandatory")
_PdnMaxClientsEntry_Object = MibTableRow
pdnMaxClientsEntry = _PdnMaxClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1)
)
pdnMaxClientsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnMaxClientsEntry.setStatus("mandatory")


class _PdnMaxClients_Type(Integer32):
    """Custom type pdnMaxClients based on Integer32"""
    defaultValue = 32


_PdnMaxClients_Object = MibTableColumn
pdnMaxClients = _PdnMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1, 1),
    _PdnMaxClients_Type()
)
pdnMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMaxClients.setStatus("mandatory")


class _PdnMaxDynamicClients_Type(Integer32):
    """Custom type pdnMaxDynamicClients based on Integer32"""
    defaultValue = 0


_PdnMaxDynamicClients_Object = MibTableColumn
pdnMaxDynamicClients = _PdnMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1, 2),
    _PdnMaxDynamicClients_Type()
)
pdnMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMaxDynamicClients.setStatus("mandatory")
_PdnClientAdditionalClientsAvailable_Type = Integer32
_PdnClientAdditionalClientsAvailable_Object = MibScalar
pdnClientAdditionalClientsAvailable = _PdnClientAdditionalClientsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 3),
    _PdnClientAdditionalClientsAvailable_Type()
)
pdnClientAdditionalClientsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientAdditionalClientsAvailable.setStatus("mandatory")
_PdnPortConfig_ObjectIdentity = ObjectIdentity
pdnPortConfig = _PdnPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4)
)
_PdnPortConfigTable_Object = MibTable
pdnPortConfigTable = _PdnPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigTable.setStatus("mandatory")
_PdnPortConfigEntry_Object = MibTableRow
pdnPortConfigEntry = _PdnPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1)
)
pdnPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-DOMAIN-MIB", "pdnPortConfigVnidId"),
)
if mibBuilder.loadTexts:
    pdnPortConfigEntry.setStatus("mandatory")
_PdnPortConfigVnidId_Type = VnidRange
_PdnPortConfigVnidId_Object = MibTableColumn
pdnPortConfigVnidId = _PdnPortConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 1),
    _PdnPortConfigVnidId_Type()
)
pdnPortConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPortConfigVnidId.setStatus("mandatory")


class _PdnPortConfigCfg_Type(Integer32):
    """Custom type pdnPortConfigCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bind", 2),
          ("un-bind", 1))
    )


_PdnPortConfigCfg_Type.__name__ = "Integer32"
_PdnPortConfigCfg_Object = MibTableColumn
pdnPortConfigCfg = _PdnPortConfigCfg_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 2),
    _PdnPortConfigCfg_Type()
)
pdnPortConfigCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigCfg.setStatus("mandatory")
_PdnPortConfigDefNHR_Type = IpAddress
_PdnPortConfigDefNHR_Object = MibTableColumn
pdnPortConfigDefNHR = _PdnPortConfigDefNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 3),
    _PdnPortConfigDefNHR_Type()
)
pdnPortConfigDefNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigDefNHR.setStatus("mandatory")
_PdnPortConfigOperStatus_Type = SwitchState
_PdnPortConfigOperStatus_Object = MibTableColumn
pdnPortConfigOperStatus = _PdnPortConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 4),
    _PdnPortConfigOperStatus_Type()
)
pdnPortConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPortConfigOperStatus.setStatus("mandatory")
_PdnDomainMIBTraps_ObjectIdentity = ObjectIdentity
pdnDomainMIBTraps = _PdnDomainMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2)
)

# Managed Objects groups


# Notification objects

dhcpClientHostTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2, 0, 1)
)
dhcpClientHostTableFull.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dhcpClientHostTableFull.setStatus(
        ""
    )

dhcpAddressInStaticSubnet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2, 0, 2)
)
dhcpAddressInStaticSubnet.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-DOMAIN-MIB", "pdnClientConfigSubnetMask"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    dhcpAddressInStaticSubnet.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DOMAIN-MIB",
    **{"pdnDomainMIBObjects": pdnDomainMIBObjects,
       "pdnCardGeneralParams": pdnCardGeneralParams,
       "pdnCardGeneralParamsVNIDMode": pdnCardGeneralParamsVNIDMode,
       "pdnCardConfig": pdnCardConfig,
       "pdnCardConfigTable": pdnCardConfigTable,
       "pdnCardConfigEntry": pdnCardConfigEntry,
       "pdnCardConfigVnidId": pdnCardConfigVnidId,
       "pdnCardConfigDomainName": pdnCardConfigDomainName,
       "pdnCardConfigMuxFwd": pdnCardConfigMuxFwd,
       "pdnCardConfigIPFiltering": pdnCardConfigIPFiltering,
       "pdnCardConfigIPScoping": pdnCardConfigIPScoping,
       "pdnCardConfigVnidAuth": pdnCardConfigVnidAuth,
       "pdnCardConfigRowStatus": pdnCardConfigRowStatus,
       "pdnClientConfig": pdnClientConfig,
       "pdnClientConfigTable": pdnClientConfigTable,
       "pdnClientConfigEntry": pdnClientConfigEntry,
       "pdnClientConfigAddr": pdnClientConfigAddr,
       "pdnClientConfigSubnetMask": pdnClientConfigSubnetMask,
       "pdnClientConfigVnidId": pdnClientConfigVnidId,
       "pdnClientConfigNHR": pdnClientConfigNHR,
       "pdnClientConfigType": pdnClientConfigType,
       "pdnClientConfigLeaseTime": pdnClientConfigLeaseTime,
       "pdnClientConfigLeaseRemainTime": pdnClientConfigLeaseRemainTime,
       "pdnClientConfigMacAddr": pdnClientConfigMacAddr,
       "pdnClientConfigRowStatus": pdnClientConfigRowStatus,
       "pdnMaxClientsTable": pdnMaxClientsTable,
       "pdnMaxClientsEntry": pdnMaxClientsEntry,
       "pdnMaxClients": pdnMaxClients,
       "pdnMaxDynamicClients": pdnMaxDynamicClients,
       "pdnClientAdditionalClientsAvailable": pdnClientAdditionalClientsAvailable,
       "pdnPortConfig": pdnPortConfig,
       "pdnPortConfigTable": pdnPortConfigTable,
       "pdnPortConfigEntry": pdnPortConfigEntry,
       "pdnPortConfigVnidId": pdnPortConfigVnidId,
       "pdnPortConfigCfg": pdnPortConfigCfg,
       "pdnPortConfigDefNHR": pdnPortConfigDefNHR,
       "pdnPortConfigOperStatus": pdnPortConfigOperStatus,
       "pdnDomainMIBTraps": pdnDomainMIBTraps,
       "dhcpClientHostTableFull": dhcpClientHostTableFull,
       "dhcpAddressInStaticSubnet": dhcpAddressInStaticSubnet}
)
