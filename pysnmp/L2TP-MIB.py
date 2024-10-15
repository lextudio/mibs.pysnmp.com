# SNMP MIB module (L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:46 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

l2tp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95)
)
l2tp.setRevisions(
        ("2002-08-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class L2tpMilliSeconds(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )



# MIB Managed Objects in the order of their OIDs

_L2tpNotifications_ObjectIdentity = ObjectIdentity
l2tpNotifications = _L2tpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 0)
)
_L2tpObjects_ObjectIdentity = ObjectIdentity
l2tpObjects = _L2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 1)
)
_L2tpScalar_ObjectIdentity = ObjectIdentity
l2tpScalar = _L2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1)
)
_L2tpConfig_ObjectIdentity = ObjectIdentity
l2tpConfig = _L2tpConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 1)
)


class _L2tpAdminState_Type(Integer32):
    """Custom type l2tpAdminState based on Integer32"""
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


_L2tpAdminState_Type.__name__ = "Integer32"
_L2tpAdminState_Object = MibScalar
l2tpAdminState = _L2tpAdminState_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 1, 1),
    _L2tpAdminState_Type()
)
l2tpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpAdminState.setStatus("current")
_L2tpDrainTunnels_Type = TruthValue
_L2tpDrainTunnels_Object = MibScalar
l2tpDrainTunnels = _L2tpDrainTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 1, 2),
    _L2tpDrainTunnels_Type()
)
l2tpDrainTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpDrainTunnels.setStatus("current")
_L2tpStats_ObjectIdentity = ObjectIdentity
l2tpStats = _L2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 2)
)


class _L2tpProtocolVersions_Type(OctetString):
    """Custom type l2tpProtocolVersions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_L2tpProtocolVersions_Type.__name__ = "OctetString"
_L2tpProtocolVersions_Object = MibScalar
l2tpProtocolVersions = _L2tpProtocolVersions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 2, 1),
    _L2tpProtocolVersions_Type()
)
l2tpProtocolVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpProtocolVersions.setStatus("current")
_L2tpVendorName_Type = SnmpAdminString
_L2tpVendorName_Object = MibScalar
l2tpVendorName = _L2tpVendorName_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 2, 2),
    _L2tpVendorName_Type()
)
l2tpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpVendorName.setStatus("current")
_L2tpFirmwareRev_Type = Integer32
_L2tpFirmwareRev_Object = MibScalar
l2tpFirmwareRev = _L2tpFirmwareRev_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 2, 3),
    _L2tpFirmwareRev_Type()
)
l2tpFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpFirmwareRev.setStatus("current")
_L2tpDrainingTunnels_Type = TruthValue
_L2tpDrainingTunnels_Object = MibScalar
l2tpDrainingTunnels = _L2tpDrainingTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 1, 2, 4),
    _L2tpDrainingTunnels_Type()
)
l2tpDrainingTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDrainingTunnels.setStatus("current")
_L2tpDomainConfigTable_Object = MibTable
l2tpDomainConfigTable = _L2tpDomainConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2)
)
if mibBuilder.loadTexts:
    l2tpDomainConfigTable.setStatus("current")
_L2tpDomainConfigEntry_Object = MibTableRow
l2tpDomainConfigEntry = _L2tpDomainConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1)
)
l2tpDomainConfigEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpDomainConfigId"),
)
if mibBuilder.loadTexts:
    l2tpDomainConfigEntry.setStatus("current")


class _L2tpDomainConfigId_Type(SnmpAdminString):
    """Custom type l2tpDomainConfigId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_L2tpDomainConfigId_Type.__name__ = "SnmpAdminString"
_L2tpDomainConfigId_Object = MibTableColumn
l2tpDomainConfigId = _L2tpDomainConfigId_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 1),
    _L2tpDomainConfigId_Type()
)
l2tpDomainConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpDomainConfigId.setStatus("current")


class _L2tpDomainConfigAdminState_Type(Integer32):
    """Custom type l2tpDomainConfigAdminState based on Integer32"""
    defaultValue = 1

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


_L2tpDomainConfigAdminState_Type.__name__ = "Integer32"
_L2tpDomainConfigAdminState_Object = MibTableColumn
l2tpDomainConfigAdminState = _L2tpDomainConfigAdminState_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 2),
    _L2tpDomainConfigAdminState_Type()
)
l2tpDomainConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigAdminState.setStatus("current")


class _L2tpDomainConfigDrainTunnels_Type(TruthValue):
    """Custom type l2tpDomainConfigDrainTunnels based on TruthValue"""


_L2tpDomainConfigDrainTunnels_Object = MibTableColumn
l2tpDomainConfigDrainTunnels = _L2tpDomainConfigDrainTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 3),
    _L2tpDomainConfigDrainTunnels_Type()
)
l2tpDomainConfigDrainTunnels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigDrainTunnels.setStatus("current")


class _L2tpDomainConfigAuth_Type(Integer32):
    """Custom type l2tpDomainConfigAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("challenge", 3),
          ("none", 1),
          ("simple", 2))
    )


_L2tpDomainConfigAuth_Type.__name__ = "Integer32"
_L2tpDomainConfigAuth_Object = MibTableColumn
l2tpDomainConfigAuth = _L2tpDomainConfigAuth_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 4),
    _L2tpDomainConfigAuth_Type()
)
l2tpDomainConfigAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigAuth.setStatus("current")


class _L2tpDomainConfigSecret_Type(SnmpAdminString):
    """Custom type l2tpDomainConfigSecret based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpDomainConfigSecret_Type.__name__ = "SnmpAdminString"
_L2tpDomainConfigSecret_Object = MibTableColumn
l2tpDomainConfigSecret = _L2tpDomainConfigSecret_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 5),
    _L2tpDomainConfigSecret_Type()
)
l2tpDomainConfigSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigSecret.setStatus("current")


class _L2tpDomainConfigTunnelSecurity_Type(Integer32):
    """Custom type l2tpDomainConfigTunnelSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipSec", 3),
          ("none", 1),
          ("other", 2))
    )


_L2tpDomainConfigTunnelSecurity_Type.__name__ = "Integer32"
_L2tpDomainConfigTunnelSecurity_Object = MibTableColumn
l2tpDomainConfigTunnelSecurity = _L2tpDomainConfigTunnelSecurity_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 6),
    _L2tpDomainConfigTunnelSecurity_Type()
)
l2tpDomainConfigTunnelSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigTunnelSecurity.setStatus("current")


class _L2tpDomainConfigTunnelHelloInt_Type(Integer32):
    """Custom type l2tpDomainConfigTunnelHelloInt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_L2tpDomainConfigTunnelHelloInt_Type.__name__ = "Integer32"
_L2tpDomainConfigTunnelHelloInt_Object = MibTableColumn
l2tpDomainConfigTunnelHelloInt = _L2tpDomainConfigTunnelHelloInt_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 7),
    _L2tpDomainConfigTunnelHelloInt_Type()
)
l2tpDomainConfigTunnelHelloInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigTunnelHelloInt.setStatus("current")
if mibBuilder.loadTexts:
    l2tpDomainConfigTunnelHelloInt.setUnits("seconds")


class _L2tpDomainConfigTunnelIdleTO_Type(Integer32):
    """Custom type l2tpDomainConfigTunnelIdleTO based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 86400),
    )


_L2tpDomainConfigTunnelIdleTO_Type.__name__ = "Integer32"
_L2tpDomainConfigTunnelIdleTO_Object = MibTableColumn
l2tpDomainConfigTunnelIdleTO = _L2tpDomainConfigTunnelIdleTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 8),
    _L2tpDomainConfigTunnelIdleTO_Type()
)
l2tpDomainConfigTunnelIdleTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigTunnelIdleTO.setStatus("current")
if mibBuilder.loadTexts:
    l2tpDomainConfigTunnelIdleTO.setUnits("seconds")


class _L2tpDomainConfigControlRWS_Type(Integer32):
    """Custom type l2tpDomainConfigControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpDomainConfigControlRWS_Type.__name__ = "Integer32"
_L2tpDomainConfigControlRWS_Object = MibTableColumn
l2tpDomainConfigControlRWS = _L2tpDomainConfigControlRWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 9),
    _L2tpDomainConfigControlRWS_Type()
)
l2tpDomainConfigControlRWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigControlRWS.setStatus("current")


class _L2tpDomainConfigControlMaxRetx_Type(Integer32):
    """Custom type l2tpDomainConfigControlMaxRetx based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_L2tpDomainConfigControlMaxRetx_Type.__name__ = "Integer32"
_L2tpDomainConfigControlMaxRetx_Object = MibTableColumn
l2tpDomainConfigControlMaxRetx = _L2tpDomainConfigControlMaxRetx_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 10),
    _L2tpDomainConfigControlMaxRetx_Type()
)
l2tpDomainConfigControlMaxRetx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigControlMaxRetx.setStatus("current")


class _L2tpDomainConfigControlMaxRetxTO_Type(Integer32):
    """Custom type l2tpDomainConfigControlMaxRetxTO based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_L2tpDomainConfigControlMaxRetxTO_Type.__name__ = "Integer32"
_L2tpDomainConfigControlMaxRetxTO_Object = MibTableColumn
l2tpDomainConfigControlMaxRetxTO = _L2tpDomainConfigControlMaxRetxTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 11),
    _L2tpDomainConfigControlMaxRetxTO_Type()
)
l2tpDomainConfigControlMaxRetxTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigControlMaxRetxTO.setStatus("current")
if mibBuilder.loadTexts:
    l2tpDomainConfigControlMaxRetxTO.setUnits("seconds")


class _L2tpDomainConfigPayloadSeq_Type(Integer32):
    """Custom type l2tpDomainConfigPayloadSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("never", 2),
          ("onDemand", 1))
    )


_L2tpDomainConfigPayloadSeq_Type.__name__ = "Integer32"
_L2tpDomainConfigPayloadSeq_Object = MibTableColumn
l2tpDomainConfigPayloadSeq = _L2tpDomainConfigPayloadSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 12),
    _L2tpDomainConfigPayloadSeq_Type()
)
l2tpDomainConfigPayloadSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigPayloadSeq.setStatus("current")


class _L2tpDomainConfigReassemblyTO_Type(L2tpMilliSeconds):
    """Custom type l2tpDomainConfigReassemblyTO based on L2tpMilliSeconds"""
    defaultValue = 0


_L2tpDomainConfigReassemblyTO_Object = MibTableColumn
l2tpDomainConfigReassemblyTO = _L2tpDomainConfigReassemblyTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 13),
    _L2tpDomainConfigReassemblyTO_Type()
)
l2tpDomainConfigReassemblyTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigReassemblyTO.setStatus("current")


class _L2tpDomainConfigProxyPPPAuth_Type(TruthValue):
    """Custom type l2tpDomainConfigProxyPPPAuth based on TruthValue"""


_L2tpDomainConfigProxyPPPAuth_Object = MibTableColumn
l2tpDomainConfigProxyPPPAuth = _L2tpDomainConfigProxyPPPAuth_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 14),
    _L2tpDomainConfigProxyPPPAuth_Type()
)
l2tpDomainConfigProxyPPPAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigProxyPPPAuth.setStatus("current")
_L2tpDomainConfigStorageType_Type = StorageType
_L2tpDomainConfigStorageType_Object = MibTableColumn
l2tpDomainConfigStorageType = _L2tpDomainConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 15),
    _L2tpDomainConfigStorageType_Type()
)
l2tpDomainConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigStorageType.setStatus("current")
_L2tpDomainConfigStatus_Type = RowStatus
_L2tpDomainConfigStatus_Object = MibTableColumn
l2tpDomainConfigStatus = _L2tpDomainConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 2, 1, 16),
    _L2tpDomainConfigStatus_Type()
)
l2tpDomainConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpDomainConfigStatus.setStatus("current")
_L2tpDomainStatsTable_Object = MibTable
l2tpDomainStatsTable = _L2tpDomainStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3)
)
if mibBuilder.loadTexts:
    l2tpDomainStatsTable.setStatus("current")
_L2tpDomainStatsEntry_Object = MibTableRow
l2tpDomainStatsEntry = _L2tpDomainStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1)
)
if mibBuilder.loadTexts:
    l2tpDomainStatsEntry.setStatus("current")
_L2tpDomainStatsTotalTunnels_Type = Counter32
_L2tpDomainStatsTotalTunnels_Object = MibTableColumn
l2tpDomainStatsTotalTunnels = _L2tpDomainStatsTotalTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 1),
    _L2tpDomainStatsTotalTunnels_Type()
)
l2tpDomainStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsTotalTunnels.setStatus("current")
_L2tpDomainStatsFailedTunnels_Type = Counter32
_L2tpDomainStatsFailedTunnels_Object = MibTableColumn
l2tpDomainStatsFailedTunnels = _L2tpDomainStatsFailedTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 2),
    _L2tpDomainStatsFailedTunnels_Type()
)
l2tpDomainStatsFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsFailedTunnels.setStatus("current")
_L2tpDomainStatsFailedAuths_Type = Counter32
_L2tpDomainStatsFailedAuths_Object = MibTableColumn
l2tpDomainStatsFailedAuths = _L2tpDomainStatsFailedAuths_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 3),
    _L2tpDomainStatsFailedAuths_Type()
)
l2tpDomainStatsFailedAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsFailedAuths.setStatus("current")
_L2tpDomainStatsActiveTunnels_Type = Gauge32
_L2tpDomainStatsActiveTunnels_Object = MibTableColumn
l2tpDomainStatsActiveTunnels = _L2tpDomainStatsActiveTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 4),
    _L2tpDomainStatsActiveTunnels_Type()
)
l2tpDomainStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsActiveTunnels.setStatus("current")
_L2tpDomainStatsTotalSessions_Type = Counter32
_L2tpDomainStatsTotalSessions_Object = MibTableColumn
l2tpDomainStatsTotalSessions = _L2tpDomainStatsTotalSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 5),
    _L2tpDomainStatsTotalSessions_Type()
)
l2tpDomainStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsTotalSessions.setStatus("current")
_L2tpDomainStatsFailedSessions_Type = Counter32
_L2tpDomainStatsFailedSessions_Object = MibTableColumn
l2tpDomainStatsFailedSessions = _L2tpDomainStatsFailedSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 6),
    _L2tpDomainStatsFailedSessions_Type()
)
l2tpDomainStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsFailedSessions.setStatus("current")
_L2tpDomainStatsActiveSessions_Type = Gauge32
_L2tpDomainStatsActiveSessions_Object = MibTableColumn
l2tpDomainStatsActiveSessions = _L2tpDomainStatsActiveSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 7),
    _L2tpDomainStatsActiveSessions_Type()
)
l2tpDomainStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsActiveSessions.setStatus("current")
_L2tpDomainStatsDrainingTunnels_Type = TruthValue
_L2tpDomainStatsDrainingTunnels_Object = MibTableColumn
l2tpDomainStatsDrainingTunnels = _L2tpDomainStatsDrainingTunnels_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 8),
    _L2tpDomainStatsDrainingTunnels_Type()
)
l2tpDomainStatsDrainingTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsDrainingTunnels.setStatus("current")
_L2tpDomainStatsControlRxOctets_Type = Counter32
_L2tpDomainStatsControlRxOctets_Object = MibTableColumn
l2tpDomainStatsControlRxOctets = _L2tpDomainStatsControlRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 9),
    _L2tpDomainStatsControlRxOctets_Type()
)
l2tpDomainStatsControlRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlRxOctets.setStatus("current")
_L2tpDomainStatsControlRxPkts_Type = Counter32
_L2tpDomainStatsControlRxPkts_Object = MibTableColumn
l2tpDomainStatsControlRxPkts = _L2tpDomainStatsControlRxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 10),
    _L2tpDomainStatsControlRxPkts_Type()
)
l2tpDomainStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlRxPkts.setStatus("current")
_L2tpDomainStatsControlTxOctets_Type = Counter32
_L2tpDomainStatsControlTxOctets_Object = MibTableColumn
l2tpDomainStatsControlTxOctets = _L2tpDomainStatsControlTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 11),
    _L2tpDomainStatsControlTxOctets_Type()
)
l2tpDomainStatsControlTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlTxOctets.setStatus("current")
_L2tpDomainStatsControlTxPkts_Type = Counter32
_L2tpDomainStatsControlTxPkts_Object = MibTableColumn
l2tpDomainStatsControlTxPkts = _L2tpDomainStatsControlTxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 12),
    _L2tpDomainStatsControlTxPkts_Type()
)
l2tpDomainStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlTxPkts.setStatus("current")
_L2tpDomainStatsPayloadRxOctets_Type = Counter32
_L2tpDomainStatsPayloadRxOctets_Object = MibTableColumn
l2tpDomainStatsPayloadRxOctets = _L2tpDomainStatsPayloadRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 13),
    _L2tpDomainStatsPayloadRxOctets_Type()
)
l2tpDomainStatsPayloadRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadRxOctets.setStatus("current")
_L2tpDomainStatsPayloadRxPkts_Type = Counter32
_L2tpDomainStatsPayloadRxPkts_Object = MibTableColumn
l2tpDomainStatsPayloadRxPkts = _L2tpDomainStatsPayloadRxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 14),
    _L2tpDomainStatsPayloadRxPkts_Type()
)
l2tpDomainStatsPayloadRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadRxPkts.setStatus("current")
_L2tpDomainStatsPayloadRxDiscs_Type = Counter32
_L2tpDomainStatsPayloadRxDiscs_Object = MibTableColumn
l2tpDomainStatsPayloadRxDiscs = _L2tpDomainStatsPayloadRxDiscs_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 15),
    _L2tpDomainStatsPayloadRxDiscs_Type()
)
l2tpDomainStatsPayloadRxDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadRxDiscs.setStatus("current")
_L2tpDomainStatsPayloadTxOctets_Type = Counter32
_L2tpDomainStatsPayloadTxOctets_Object = MibTableColumn
l2tpDomainStatsPayloadTxOctets = _L2tpDomainStatsPayloadTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 16),
    _L2tpDomainStatsPayloadTxOctets_Type()
)
l2tpDomainStatsPayloadTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadTxOctets.setStatus("current")
_L2tpDomainStatsPayloadTxPkts_Type = Counter32
_L2tpDomainStatsPayloadTxPkts_Object = MibTableColumn
l2tpDomainStatsPayloadTxPkts = _L2tpDomainStatsPayloadTxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 17),
    _L2tpDomainStatsPayloadTxPkts_Type()
)
l2tpDomainStatsPayloadTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadTxPkts.setStatus("current")
_L2tpDomainStatsControlHCRxOctets_Type = Counter64
_L2tpDomainStatsControlHCRxOctets_Object = MibTableColumn
l2tpDomainStatsControlHCRxOctets = _L2tpDomainStatsControlHCRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 18),
    _L2tpDomainStatsControlHCRxOctets_Type()
)
l2tpDomainStatsControlHCRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlHCRxOctets.setStatus("current")
_L2tpDomainStatsControlHCRxPkts_Type = Counter64
_L2tpDomainStatsControlHCRxPkts_Object = MibTableColumn
l2tpDomainStatsControlHCRxPkts = _L2tpDomainStatsControlHCRxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 19),
    _L2tpDomainStatsControlHCRxPkts_Type()
)
l2tpDomainStatsControlHCRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlHCRxPkts.setStatus("current")
_L2tpDomainStatsControlHCTxOctets_Type = Counter64
_L2tpDomainStatsControlHCTxOctets_Object = MibTableColumn
l2tpDomainStatsControlHCTxOctets = _L2tpDomainStatsControlHCTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 20),
    _L2tpDomainStatsControlHCTxOctets_Type()
)
l2tpDomainStatsControlHCTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlHCTxOctets.setStatus("current")
_L2tpDomainStatsControlHCTxPkts_Type = Counter64
_L2tpDomainStatsControlHCTxPkts_Object = MibTableColumn
l2tpDomainStatsControlHCTxPkts = _L2tpDomainStatsControlHCTxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 21),
    _L2tpDomainStatsControlHCTxPkts_Type()
)
l2tpDomainStatsControlHCTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsControlHCTxPkts.setStatus("current")
_L2tpDomainStatsPayloadHCRxOctets_Type = Counter64
_L2tpDomainStatsPayloadHCRxOctets_Object = MibTableColumn
l2tpDomainStatsPayloadHCRxOctets = _L2tpDomainStatsPayloadHCRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 22),
    _L2tpDomainStatsPayloadHCRxOctets_Type()
)
l2tpDomainStatsPayloadHCRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadHCRxOctets.setStatus("current")
_L2tpDomainStatsPayloadHCRxPkts_Type = Counter64
_L2tpDomainStatsPayloadHCRxPkts_Object = MibTableColumn
l2tpDomainStatsPayloadHCRxPkts = _L2tpDomainStatsPayloadHCRxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 23),
    _L2tpDomainStatsPayloadHCRxPkts_Type()
)
l2tpDomainStatsPayloadHCRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadHCRxPkts.setStatus("current")
_L2tpDomainStatsPayloadHCRxDiscs_Type = Counter64
_L2tpDomainStatsPayloadHCRxDiscs_Object = MibTableColumn
l2tpDomainStatsPayloadHCRxDiscs = _L2tpDomainStatsPayloadHCRxDiscs_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 24),
    _L2tpDomainStatsPayloadHCRxDiscs_Type()
)
l2tpDomainStatsPayloadHCRxDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadHCRxDiscs.setStatus("current")
_L2tpDomainStatsPayloadHCTxOctets_Type = Counter64
_L2tpDomainStatsPayloadHCTxOctets_Object = MibTableColumn
l2tpDomainStatsPayloadHCTxOctets = _L2tpDomainStatsPayloadHCTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 25),
    _L2tpDomainStatsPayloadHCTxOctets_Type()
)
l2tpDomainStatsPayloadHCTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadHCTxOctets.setStatus("current")
_L2tpDomainStatsPayloadHCTxPkts_Type = Counter64
_L2tpDomainStatsPayloadHCTxPkts_Object = MibTableColumn
l2tpDomainStatsPayloadHCTxPkts = _L2tpDomainStatsPayloadHCTxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 3, 1, 26),
    _L2tpDomainStatsPayloadHCTxPkts_Type()
)
l2tpDomainStatsPayloadHCTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpDomainStatsPayloadHCTxPkts.setStatus("current")
_L2tpTunnelConfigTable_Object = MibTable
l2tpTunnelConfigTable = _L2tpTunnelConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4)
)
if mibBuilder.loadTexts:
    l2tpTunnelConfigTable.setStatus("current")
_L2tpTunnelConfigEntry_Object = MibTableRow
l2tpTunnelConfigEntry = _L2tpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1)
)
l2tpTunnelConfigEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpTunnelConfigIfIndex"),
)
if mibBuilder.loadTexts:
    l2tpTunnelConfigEntry.setStatus("current")
_L2tpTunnelConfigIfIndex_Type = InterfaceIndex
_L2tpTunnelConfigIfIndex_Object = MibTableColumn
l2tpTunnelConfigIfIndex = _L2tpTunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 1),
    _L2tpTunnelConfigIfIndex_Type()
)
l2tpTunnelConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpTunnelConfigIfIndex.setStatus("current")


class _L2tpTunnelConfigDomainId_Type(SnmpAdminString):
    """Custom type l2tpTunnelConfigDomainId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_L2tpTunnelConfigDomainId_Type.__name__ = "SnmpAdminString"
_L2tpTunnelConfigDomainId_Object = MibTableColumn
l2tpTunnelConfigDomainId = _L2tpTunnelConfigDomainId_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 2),
    _L2tpTunnelConfigDomainId_Type()
)
l2tpTunnelConfigDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigDomainId.setStatus("current")


class _L2tpTunnelConfigAuth_Type(Integer32):
    """Custom type l2tpTunnelConfigAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("challenge", 3),
          ("none", 1),
          ("simple", 2))
    )


_L2tpTunnelConfigAuth_Type.__name__ = "Integer32"
_L2tpTunnelConfigAuth_Object = MibTableColumn
l2tpTunnelConfigAuth = _L2tpTunnelConfigAuth_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 3),
    _L2tpTunnelConfigAuth_Type()
)
l2tpTunnelConfigAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigAuth.setStatus("current")


class _L2tpTunnelConfigSecret_Type(SnmpAdminString):
    """Custom type l2tpTunnelConfigSecret based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelConfigSecret_Type.__name__ = "SnmpAdminString"
_L2tpTunnelConfigSecret_Object = MibTableColumn
l2tpTunnelConfigSecret = _L2tpTunnelConfigSecret_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 4),
    _L2tpTunnelConfigSecret_Type()
)
l2tpTunnelConfigSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigSecret.setStatus("current")


class _L2tpTunnelConfigSecurity_Type(Integer32):
    """Custom type l2tpTunnelConfigSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 3),
          ("none", 1),
          ("other", 2))
    )


_L2tpTunnelConfigSecurity_Type.__name__ = "Integer32"
_L2tpTunnelConfigSecurity_Object = MibTableColumn
l2tpTunnelConfigSecurity = _L2tpTunnelConfigSecurity_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 5),
    _L2tpTunnelConfigSecurity_Type()
)
l2tpTunnelConfigSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigSecurity.setStatus("current")


class _L2tpTunnelConfigHelloInterval_Type(Integer32):
    """Custom type l2tpTunnelConfigHelloInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_L2tpTunnelConfigHelloInterval_Type.__name__ = "Integer32"
_L2tpTunnelConfigHelloInterval_Object = MibTableColumn
l2tpTunnelConfigHelloInterval = _L2tpTunnelConfigHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 6),
    _L2tpTunnelConfigHelloInterval_Type()
)
l2tpTunnelConfigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    l2tpTunnelConfigHelloInterval.setUnits("seconds")


class _L2tpTunnelConfigIdleTimeout_Type(Integer32):
    """Custom type l2tpTunnelConfigIdleTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 86400),
    )


_L2tpTunnelConfigIdleTimeout_Type.__name__ = "Integer32"
_L2tpTunnelConfigIdleTimeout_Object = MibTableColumn
l2tpTunnelConfigIdleTimeout = _L2tpTunnelConfigIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 7),
    _L2tpTunnelConfigIdleTimeout_Type()
)
l2tpTunnelConfigIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    l2tpTunnelConfigIdleTimeout.setUnits("seconds")


class _L2tpTunnelConfigControlRWS_Type(Integer32):
    """Custom type l2tpTunnelConfigControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpTunnelConfigControlRWS_Type.__name__ = "Integer32"
_L2tpTunnelConfigControlRWS_Object = MibTableColumn
l2tpTunnelConfigControlRWS = _L2tpTunnelConfigControlRWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 8),
    _L2tpTunnelConfigControlRWS_Type()
)
l2tpTunnelConfigControlRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigControlRWS.setStatus("current")


class _L2tpTunnelConfigControlMaxRetx_Type(Integer32):
    """Custom type l2tpTunnelConfigControlMaxRetx based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_L2tpTunnelConfigControlMaxRetx_Type.__name__ = "Integer32"
_L2tpTunnelConfigControlMaxRetx_Object = MibTableColumn
l2tpTunnelConfigControlMaxRetx = _L2tpTunnelConfigControlMaxRetx_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 9),
    _L2tpTunnelConfigControlMaxRetx_Type()
)
l2tpTunnelConfigControlMaxRetx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigControlMaxRetx.setStatus("current")


class _L2tpTunnelConfigControlMaxRetxTO_Type(Integer32):
    """Custom type l2tpTunnelConfigControlMaxRetxTO based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_L2tpTunnelConfigControlMaxRetxTO_Type.__name__ = "Integer32"
_L2tpTunnelConfigControlMaxRetxTO_Object = MibTableColumn
l2tpTunnelConfigControlMaxRetxTO = _L2tpTunnelConfigControlMaxRetxTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 10),
    _L2tpTunnelConfigControlMaxRetxTO_Type()
)
l2tpTunnelConfigControlMaxRetxTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigControlMaxRetxTO.setStatus("current")
if mibBuilder.loadTexts:
    l2tpTunnelConfigControlMaxRetxTO.setUnits("seconds")


class _L2tpTunnelConfigPayloadSeq_Type(Integer32):
    """Custom type l2tpTunnelConfigPayloadSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("never", 2),
          ("onDemand", 1))
    )


_L2tpTunnelConfigPayloadSeq_Type.__name__ = "Integer32"
_L2tpTunnelConfigPayloadSeq_Object = MibTableColumn
l2tpTunnelConfigPayloadSeq = _L2tpTunnelConfigPayloadSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 11),
    _L2tpTunnelConfigPayloadSeq_Type()
)
l2tpTunnelConfigPayloadSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigPayloadSeq.setStatus("current")


class _L2tpTunnelConfigReassemblyTO_Type(L2tpMilliSeconds):
    """Custom type l2tpTunnelConfigReassemblyTO based on L2tpMilliSeconds"""
    defaultValue = 0


_L2tpTunnelConfigReassemblyTO_Object = MibTableColumn
l2tpTunnelConfigReassemblyTO = _L2tpTunnelConfigReassemblyTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 12),
    _L2tpTunnelConfigReassemblyTO_Type()
)
l2tpTunnelConfigReassemblyTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigReassemblyTO.setStatus("current")


class _L2tpTunnelConfigTransport_Type(Integer32):
    """Custom type l2tpTunnelConfigTransport based on Integer32"""
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
        *(("atm", 5),
          ("frameRelay", 4),
          ("none", 2),
          ("other", 1),
          ("udpIp", 3))
    )


_L2tpTunnelConfigTransport_Type.__name__ = "Integer32"
_L2tpTunnelConfigTransport_Object = MibTableColumn
l2tpTunnelConfigTransport = _L2tpTunnelConfigTransport_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 13),
    _L2tpTunnelConfigTransport_Type()
)
l2tpTunnelConfigTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigTransport.setStatus("current")


class _L2tpTunnelConfigDrainTunnel_Type(TruthValue):
    """Custom type l2tpTunnelConfigDrainTunnel based on TruthValue"""


_L2tpTunnelConfigDrainTunnel_Object = MibTableColumn
l2tpTunnelConfigDrainTunnel = _L2tpTunnelConfigDrainTunnel_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 14),
    _L2tpTunnelConfigDrainTunnel_Type()
)
l2tpTunnelConfigDrainTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigDrainTunnel.setStatus("current")


class _L2tpTunnelConfigProxyPPPAuth_Type(TruthValue):
    """Custom type l2tpTunnelConfigProxyPPPAuth based on TruthValue"""


_L2tpTunnelConfigProxyPPPAuth_Object = MibTableColumn
l2tpTunnelConfigProxyPPPAuth = _L2tpTunnelConfigProxyPPPAuth_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 4, 1, 15),
    _L2tpTunnelConfigProxyPPPAuth_Type()
)
l2tpTunnelConfigProxyPPPAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelConfigProxyPPPAuth.setStatus("current")
_L2tpTunnelStatsTable_Object = MibTable
l2tpTunnelStatsTable = _L2tpTunnelStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5)
)
if mibBuilder.loadTexts:
    l2tpTunnelStatsTable.setStatus("current")
_L2tpTunnelStatsEntry_Object = MibTableRow
l2tpTunnelStatsEntry = _L2tpTunnelStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1)
)
if mibBuilder.loadTexts:
    l2tpTunnelStatsEntry.setStatus("current")


class _L2tpTunnelStatsLocalTID_Type(Integer32):
    """Custom type l2tpTunnelStatsLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsLocalTID_Type.__name__ = "Integer32"
_L2tpTunnelStatsLocalTID_Object = MibTableColumn
l2tpTunnelStatsLocalTID = _L2tpTunnelStatsLocalTID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 1),
    _L2tpTunnelStatsLocalTID_Type()
)
l2tpTunnelStatsLocalTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsLocalTID.setStatus("current")


class _L2tpTunnelStatsRemoteTID_Type(Integer32):
    """Custom type l2tpTunnelStatsRemoteTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsRemoteTID_Type.__name__ = "Integer32"
_L2tpTunnelStatsRemoteTID_Object = MibTableColumn
l2tpTunnelStatsRemoteTID = _L2tpTunnelStatsRemoteTID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 2),
    _L2tpTunnelStatsRemoteTID_Type()
)
l2tpTunnelStatsRemoteTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRemoteTID.setStatus("current")


class _L2tpTunnelStatsState_Type(Integer32):
    """Custom type l2tpTunnelStatsState based on Integer32"""
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
        *(("tunnelConnecting", 2),
          ("tunnelDisconnecting", 4),
          ("tunnelEstablished", 3),
          ("tunnelIdle", 1))
    )


_L2tpTunnelStatsState_Type.__name__ = "Integer32"
_L2tpTunnelStatsState_Object = MibTableColumn
l2tpTunnelStatsState = _L2tpTunnelStatsState_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 3),
    _L2tpTunnelStatsState_Type()
)
l2tpTunnelStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsState.setStatus("current")


class _L2tpTunnelStatsInitiated_Type(Integer32):
    """Custom type l2tpTunnelStatsInitiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locally", 1),
          ("remotely", 2))
    )


_L2tpTunnelStatsInitiated_Type.__name__ = "Integer32"
_L2tpTunnelStatsInitiated_Object = MibTableColumn
l2tpTunnelStatsInitiated = _L2tpTunnelStatsInitiated_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 4),
    _L2tpTunnelStatsInitiated_Type()
)
l2tpTunnelStatsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsInitiated.setStatus("current")
_L2tpTunnelStatsRemoteHostName_Type = SnmpAdminString
_L2tpTunnelStatsRemoteHostName_Object = MibTableColumn
l2tpTunnelStatsRemoteHostName = _L2tpTunnelStatsRemoteHostName_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 5),
    _L2tpTunnelStatsRemoteHostName_Type()
)
l2tpTunnelStatsRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRemoteHostName.setStatus("current")
_L2tpTunnelStatsRemoteVendorName_Type = SnmpAdminString
_L2tpTunnelStatsRemoteVendorName_Object = MibTableColumn
l2tpTunnelStatsRemoteVendorName = _L2tpTunnelStatsRemoteVendorName_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 6),
    _L2tpTunnelStatsRemoteVendorName_Type()
)
l2tpTunnelStatsRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRemoteVendorName.setStatus("current")
_L2tpTunnelStatsRemoteFirmwareRev_Type = Integer32
_L2tpTunnelStatsRemoteFirmwareRev_Object = MibTableColumn
l2tpTunnelStatsRemoteFirmwareRev = _L2tpTunnelStatsRemoteFirmwareRev_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 7),
    _L2tpTunnelStatsRemoteFirmwareRev_Type()
)
l2tpTunnelStatsRemoteFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRemoteFirmwareRev.setStatus("current")


class _L2tpTunnelStatsRemoteProtocolVer_Type(OctetString):
    """Custom type l2tpTunnelStatsRemoteProtocolVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_L2tpTunnelStatsRemoteProtocolVer_Type.__name__ = "OctetString"
_L2tpTunnelStatsRemoteProtocolVer_Object = MibTableColumn
l2tpTunnelStatsRemoteProtocolVer = _L2tpTunnelStatsRemoteProtocolVer_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 8),
    _L2tpTunnelStatsRemoteProtocolVer_Type()
)
l2tpTunnelStatsRemoteProtocolVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRemoteProtocolVer.setStatus("current")


class _L2tpTunnelStatsInitialRemoteRWS_Type(Integer32):
    """Custom type l2tpTunnelStatsInitialRemoteRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsInitialRemoteRWS_Type.__name__ = "Integer32"
_L2tpTunnelStatsInitialRemoteRWS_Object = MibTableColumn
l2tpTunnelStatsInitialRemoteRWS = _L2tpTunnelStatsInitialRemoteRWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 9),
    _L2tpTunnelStatsInitialRemoteRWS_Type()
)
l2tpTunnelStatsInitialRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsInitialRemoteRWS.setStatus("current")


class _L2tpTunnelStatsBearerCaps_Type(Integer32):
    """Custom type l2tpTunnelStatsBearerCaps based on Integer32"""
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
        *(("analog", 3),
          ("digital", 2),
          ("digitalAnalog", 4),
          ("none", 1))
    )


_L2tpTunnelStatsBearerCaps_Type.__name__ = "Integer32"
_L2tpTunnelStatsBearerCaps_Object = MibTableColumn
l2tpTunnelStatsBearerCaps = _L2tpTunnelStatsBearerCaps_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 10),
    _L2tpTunnelStatsBearerCaps_Type()
)
l2tpTunnelStatsBearerCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsBearerCaps.setStatus("current")


class _L2tpTunnelStatsFramingCaps_Type(Integer32):
    """Custom type l2tpTunnelStatsFramingCaps based on Integer32"""
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
        *(("async", 3),
          ("none", 1),
          ("sync", 2),
          ("syncAsync", 4))
    )


_L2tpTunnelStatsFramingCaps_Type.__name__ = "Integer32"
_L2tpTunnelStatsFramingCaps_Object = MibTableColumn
l2tpTunnelStatsFramingCaps = _L2tpTunnelStatsFramingCaps_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 11),
    _L2tpTunnelStatsFramingCaps_Type()
)
l2tpTunnelStatsFramingCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsFramingCaps.setStatus("current")
_L2tpTunnelStatsControlRxPkts_Type = Counter32
_L2tpTunnelStatsControlRxPkts_Object = MibTableColumn
l2tpTunnelStatsControlRxPkts = _L2tpTunnelStatsControlRxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 12),
    _L2tpTunnelStatsControlRxPkts_Type()
)
l2tpTunnelStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlRxPkts.setStatus("current")
_L2tpTunnelStatsControlRxZLB_Type = Counter32
_L2tpTunnelStatsControlRxZLB_Object = MibTableColumn
l2tpTunnelStatsControlRxZLB = _L2tpTunnelStatsControlRxZLB_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 13),
    _L2tpTunnelStatsControlRxZLB_Type()
)
l2tpTunnelStatsControlRxZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlRxZLB.setStatus("current")
_L2tpTunnelStatsControlOutOfSeq_Type = Counter32
_L2tpTunnelStatsControlOutOfSeq_Object = MibTableColumn
l2tpTunnelStatsControlOutOfSeq = _L2tpTunnelStatsControlOutOfSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 14),
    _L2tpTunnelStatsControlOutOfSeq_Type()
)
l2tpTunnelStatsControlOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlOutOfSeq.setStatus("current")
_L2tpTunnelStatsControlOutOfWin_Type = Counter32
_L2tpTunnelStatsControlOutOfWin_Object = MibTableColumn
l2tpTunnelStatsControlOutOfWin = _L2tpTunnelStatsControlOutOfWin_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 15),
    _L2tpTunnelStatsControlOutOfWin_Type()
)
l2tpTunnelStatsControlOutOfWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlOutOfWin.setStatus("current")
_L2tpTunnelStatsControlTxPkts_Type = Counter32
_L2tpTunnelStatsControlTxPkts_Object = MibTableColumn
l2tpTunnelStatsControlTxPkts = _L2tpTunnelStatsControlTxPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 16),
    _L2tpTunnelStatsControlTxPkts_Type()
)
l2tpTunnelStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlTxPkts.setStatus("current")
_L2tpTunnelStatsControlTxZLB_Type = Counter32
_L2tpTunnelStatsControlTxZLB_Object = MibTableColumn
l2tpTunnelStatsControlTxZLB = _L2tpTunnelStatsControlTxZLB_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 17),
    _L2tpTunnelStatsControlTxZLB_Type()
)
l2tpTunnelStatsControlTxZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlTxZLB.setStatus("current")
_L2tpTunnelStatsControlAckTO_Type = Counter32
_L2tpTunnelStatsControlAckTO_Object = MibTableColumn
l2tpTunnelStatsControlAckTO = _L2tpTunnelStatsControlAckTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 18),
    _L2tpTunnelStatsControlAckTO_Type()
)
l2tpTunnelStatsControlAckTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsControlAckTO.setStatus("current")


class _L2tpTunnelStatsCurrentRemoteRWS_Type(Gauge32):
    """Custom type l2tpTunnelStatsCurrentRemoteRWS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsCurrentRemoteRWS_Type.__name__ = "Gauge32"
_L2tpTunnelStatsCurrentRemoteRWS_Object = MibTableColumn
l2tpTunnelStatsCurrentRemoteRWS = _L2tpTunnelStatsCurrentRemoteRWS_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 19),
    _L2tpTunnelStatsCurrentRemoteRWS_Type()
)
l2tpTunnelStatsCurrentRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsCurrentRemoteRWS.setStatus("current")


class _L2tpTunnelStatsTxSeq_Type(Integer32):
    """Custom type l2tpTunnelStatsTxSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsTxSeq_Type.__name__ = "Integer32"
_L2tpTunnelStatsTxSeq_Object = MibTableColumn
l2tpTunnelStatsTxSeq = _L2tpTunnelStatsTxSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 20),
    _L2tpTunnelStatsTxSeq_Type()
)
l2tpTunnelStatsTxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsTxSeq.setStatus("current")


class _L2tpTunnelStatsTxSeqAck_Type(Integer32):
    """Custom type l2tpTunnelStatsTxSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsTxSeqAck_Type.__name__ = "Integer32"
_L2tpTunnelStatsTxSeqAck_Object = MibTableColumn
l2tpTunnelStatsTxSeqAck = _L2tpTunnelStatsTxSeqAck_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 21),
    _L2tpTunnelStatsTxSeqAck_Type()
)
l2tpTunnelStatsTxSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsTxSeqAck.setStatus("current")


class _L2tpTunnelStatsRxSeq_Type(Integer32):
    """Custom type l2tpTunnelStatsRxSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsRxSeq_Type.__name__ = "Integer32"
_L2tpTunnelStatsRxSeq_Object = MibTableColumn
l2tpTunnelStatsRxSeq = _L2tpTunnelStatsRxSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 22),
    _L2tpTunnelStatsRxSeq_Type()
)
l2tpTunnelStatsRxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRxSeq.setStatus("current")


class _L2tpTunnelStatsRxSeqAck_Type(Integer32):
    """Custom type l2tpTunnelStatsRxSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsRxSeqAck_Type.__name__ = "Integer32"
_L2tpTunnelStatsRxSeqAck_Object = MibTableColumn
l2tpTunnelStatsRxSeqAck = _L2tpTunnelStatsRxSeqAck_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 23),
    _L2tpTunnelStatsRxSeqAck_Type()
)
l2tpTunnelStatsRxSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsRxSeqAck.setStatus("current")
_L2tpTunnelStatsTotalSessions_Type = Counter32
_L2tpTunnelStatsTotalSessions_Object = MibTableColumn
l2tpTunnelStatsTotalSessions = _L2tpTunnelStatsTotalSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 24),
    _L2tpTunnelStatsTotalSessions_Type()
)
l2tpTunnelStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsTotalSessions.setStatus("current")
_L2tpTunnelStatsFailedSessions_Type = Counter32
_L2tpTunnelStatsFailedSessions_Object = MibTableColumn
l2tpTunnelStatsFailedSessions = _L2tpTunnelStatsFailedSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 25),
    _L2tpTunnelStatsFailedSessions_Type()
)
l2tpTunnelStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsFailedSessions.setStatus("current")
_L2tpTunnelStatsActiveSessions_Type = Gauge32
_L2tpTunnelStatsActiveSessions_Object = MibTableColumn
l2tpTunnelStatsActiveSessions = _L2tpTunnelStatsActiveSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 26),
    _L2tpTunnelStatsActiveSessions_Type()
)
l2tpTunnelStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsActiveSessions.setStatus("current")


class _L2tpTunnelStatsLastResultCode_Type(Integer32):
    """Custom type l2tpTunnelStatsLastResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsLastResultCode_Type.__name__ = "Integer32"
_L2tpTunnelStatsLastResultCode_Object = MibTableColumn
l2tpTunnelStatsLastResultCode = _L2tpTunnelStatsLastResultCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 27),
    _L2tpTunnelStatsLastResultCode_Type()
)
l2tpTunnelStatsLastResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsLastResultCode.setStatus("current")


class _L2tpTunnelStatsLastErrorCode_Type(Integer32):
    """Custom type l2tpTunnelStatsLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelStatsLastErrorCode_Type.__name__ = "Integer32"
_L2tpTunnelStatsLastErrorCode_Object = MibTableColumn
l2tpTunnelStatsLastErrorCode = _L2tpTunnelStatsLastErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 28),
    _L2tpTunnelStatsLastErrorCode_Type()
)
l2tpTunnelStatsLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsLastErrorCode.setStatus("current")
_L2tpTunnelStatsLastErrorMessage_Type = SnmpAdminString
_L2tpTunnelStatsLastErrorMessage_Object = MibTableColumn
l2tpTunnelStatsLastErrorMessage = _L2tpTunnelStatsLastErrorMessage_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 29),
    _L2tpTunnelStatsLastErrorMessage_Type()
)
l2tpTunnelStatsLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsLastErrorMessage.setStatus("current")
_L2tpTunnelStatsDrainingTunnel_Type = TruthValue
_L2tpTunnelStatsDrainingTunnel_Object = MibTableColumn
l2tpTunnelStatsDrainingTunnel = _L2tpTunnelStatsDrainingTunnel_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 5, 1, 30),
    _L2tpTunnelStatsDrainingTunnel_Type()
)
l2tpTunnelStatsDrainingTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelStatsDrainingTunnel.setStatus("current")
_L2tpSessionStatsTable_Object = MibTable
l2tpSessionStatsTable = _L2tpSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7)
)
if mibBuilder.loadTexts:
    l2tpSessionStatsTable.setStatus("current")
_L2tpSessionStatsEntry_Object = MibTableRow
l2tpSessionStatsEntry = _L2tpSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1)
)
l2tpSessionStatsEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpSessionStatsTunnelIfIndex"),
    (0, "L2TP-MIB", "l2tpSessionStatsLocalSID"),
)
if mibBuilder.loadTexts:
    l2tpSessionStatsEntry.setStatus("current")
_L2tpSessionStatsTunnelIfIndex_Type = InterfaceIndex
_L2tpSessionStatsTunnelIfIndex_Object = MibTableColumn
l2tpSessionStatsTunnelIfIndex = _L2tpSessionStatsTunnelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 1),
    _L2tpSessionStatsTunnelIfIndex_Type()
)
l2tpSessionStatsTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpSessionStatsTunnelIfIndex.setStatus("current")
_L2tpSessionStatsIfIndex_Type = InterfaceIndex
_L2tpSessionStatsIfIndex_Object = MibTableColumn
l2tpSessionStatsIfIndex = _L2tpSessionStatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 2),
    _L2tpSessionStatsIfIndex_Type()
)
l2tpSessionStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsIfIndex.setStatus("current")


class _L2tpSessionStatsLocalSID_Type(Integer32):
    """Custom type l2tpSessionStatsLocalSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpSessionStatsLocalSID_Type.__name__ = "Integer32"
_L2tpSessionStatsLocalSID_Object = MibTableColumn
l2tpSessionStatsLocalSID = _L2tpSessionStatsLocalSID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 3),
    _L2tpSessionStatsLocalSID_Type()
)
l2tpSessionStatsLocalSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpSessionStatsLocalSID.setStatus("current")


class _L2tpSessionStatsRemoteSID_Type(Integer32):
    """Custom type l2tpSessionStatsRemoteSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionStatsRemoteSID_Type.__name__ = "Integer32"
_L2tpSessionStatsRemoteSID_Object = MibTableColumn
l2tpSessionStatsRemoteSID = _L2tpSessionStatsRemoteSID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 4),
    _L2tpSessionStatsRemoteSID_Type()
)
l2tpSessionStatsRemoteSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsRemoteSID.setStatus("current")
_L2tpSessionStatsUserName_Type = SnmpAdminString
_L2tpSessionStatsUserName_Object = MibTableColumn
l2tpSessionStatsUserName = _L2tpSessionStatsUserName_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 5),
    _L2tpSessionStatsUserName_Type()
)
l2tpSessionStatsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsUserName.setStatus("current")


class _L2tpSessionStatsState_Type(Integer32):
    """Custom type l2tpSessionStatsState based on Integer32"""
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
        *(("sessionConnecting", 2),
          ("sessionDisconnecting", 4),
          ("sessionEstablished", 3),
          ("sessionIdle", 1))
    )


_L2tpSessionStatsState_Type.__name__ = "Integer32"
_L2tpSessionStatsState_Object = MibTableColumn
l2tpSessionStatsState = _L2tpSessionStatsState_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 6),
    _L2tpSessionStatsState_Type()
)
l2tpSessionStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsState.setStatus("current")


class _L2tpSessionStatsCallType_Type(Integer32):
    """Custom type l2tpSessionStatsCallType based on Integer32"""
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
        *(("lacIncoming", 1),
          ("lacOutgoing", 3),
          ("lnsIncoming", 2),
          ("lnsOutgoing", 4))
    )


_L2tpSessionStatsCallType_Type.__name__ = "Integer32"
_L2tpSessionStatsCallType_Object = MibTableColumn
l2tpSessionStatsCallType = _L2tpSessionStatsCallType_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 7),
    _L2tpSessionStatsCallType_Type()
)
l2tpSessionStatsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsCallType.setStatus("current")
_L2tpSessionStatsCallSerialNumber_Type = Unsigned32
_L2tpSessionStatsCallSerialNumber_Object = MibTableColumn
l2tpSessionStatsCallSerialNumber = _L2tpSessionStatsCallSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 8),
    _L2tpSessionStatsCallSerialNumber_Type()
)
l2tpSessionStatsCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsCallSerialNumber.setStatus("current")
_L2tpSessionStatsTxConnectSpeed_Type = Unsigned32
_L2tpSessionStatsTxConnectSpeed_Object = MibTableColumn
l2tpSessionStatsTxConnectSpeed = _L2tpSessionStatsTxConnectSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 9),
    _L2tpSessionStatsTxConnectSpeed_Type()
)
l2tpSessionStatsTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsTxConnectSpeed.setStatus("current")
if mibBuilder.loadTexts:
    l2tpSessionStatsTxConnectSpeed.setUnits("bits per second")
_L2tpSessionStatsRxConnectSpeed_Type = Unsigned32
_L2tpSessionStatsRxConnectSpeed_Object = MibTableColumn
l2tpSessionStatsRxConnectSpeed = _L2tpSessionStatsRxConnectSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 10),
    _L2tpSessionStatsRxConnectSpeed_Type()
)
l2tpSessionStatsRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsRxConnectSpeed.setStatus("current")
if mibBuilder.loadTexts:
    l2tpSessionStatsRxConnectSpeed.setUnits("bits per second")


class _L2tpSessionStatsCallBearerType_Type(Integer32):
    """Custom type l2tpSessionStatsCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("digital", 2),
          ("none", 1))
    )


_L2tpSessionStatsCallBearerType_Type.__name__ = "Integer32"
_L2tpSessionStatsCallBearerType_Object = MibTableColumn
l2tpSessionStatsCallBearerType = _L2tpSessionStatsCallBearerType_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 11),
    _L2tpSessionStatsCallBearerType_Type()
)
l2tpSessionStatsCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsCallBearerType.setStatus("current")


class _L2tpSessionStatsFramingType_Type(Integer32):
    """Custom type l2tpSessionStatsFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 3),
          ("none", 1),
          ("sync", 2))
    )


_L2tpSessionStatsFramingType_Type.__name__ = "Integer32"
_L2tpSessionStatsFramingType_Object = MibTableColumn
l2tpSessionStatsFramingType = _L2tpSessionStatsFramingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 12),
    _L2tpSessionStatsFramingType_Type()
)
l2tpSessionStatsFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsFramingType.setStatus("current")
_L2tpSessionStatsPhysChanId_Type = Unsigned32
_L2tpSessionStatsPhysChanId_Object = MibTableColumn
l2tpSessionStatsPhysChanId = _L2tpSessionStatsPhysChanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 13),
    _L2tpSessionStatsPhysChanId_Type()
)
l2tpSessionStatsPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsPhysChanId.setStatus("current")
_L2tpSessionStatsDNIS_Type = SnmpAdminString
_L2tpSessionStatsDNIS_Object = MibTableColumn
l2tpSessionStatsDNIS = _L2tpSessionStatsDNIS_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 14),
    _L2tpSessionStatsDNIS_Type()
)
l2tpSessionStatsDNIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsDNIS.setStatus("current")
_L2tpSessionStatsCLID_Type = SnmpAdminString
_L2tpSessionStatsCLID_Object = MibTableColumn
l2tpSessionStatsCLID = _L2tpSessionStatsCLID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 15),
    _L2tpSessionStatsCLID_Type()
)
l2tpSessionStatsCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsCLID.setStatus("current")
_L2tpSessionStatsSubAddress_Type = SnmpAdminString
_L2tpSessionStatsSubAddress_Object = MibTableColumn
l2tpSessionStatsSubAddress = _L2tpSessionStatsSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 16),
    _L2tpSessionStatsSubAddress_Type()
)
l2tpSessionStatsSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsSubAddress.setStatus("current")
_L2tpSessionStatsPrivateGroupID_Type = SnmpAdminString
_L2tpSessionStatsPrivateGroupID_Object = MibTableColumn
l2tpSessionStatsPrivateGroupID = _L2tpSessionStatsPrivateGroupID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 17),
    _L2tpSessionStatsPrivateGroupID_Type()
)
l2tpSessionStatsPrivateGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsPrivateGroupID.setStatus("current")
_L2tpSessionStatsProxyLcp_Type = TruthValue
_L2tpSessionStatsProxyLcp_Object = MibTableColumn
l2tpSessionStatsProxyLcp = _L2tpSessionStatsProxyLcp_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 18),
    _L2tpSessionStatsProxyLcp_Type()
)
l2tpSessionStatsProxyLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsProxyLcp.setStatus("current")


class _L2tpSessionStatsAuthMethod_Type(Integer32):
    """Custom type l2tpSessionStatsAuthMethod based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 8),
          ("pppChap", 3),
          ("pppEap", 5),
          ("pppMsChapV1", 6),
          ("pppMsChapV2", 7),
          ("pppPap", 4),
          ("text", 2))
    )


_L2tpSessionStatsAuthMethod_Type.__name__ = "Integer32"
_L2tpSessionStatsAuthMethod_Object = MibTableColumn
l2tpSessionStatsAuthMethod = _L2tpSessionStatsAuthMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 19),
    _L2tpSessionStatsAuthMethod_Type()
)
l2tpSessionStatsAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsAuthMethod.setStatus("current")


class _L2tpSessionStatsSequencingState_Type(Integer32):
    """Custom type l2tpSessionStatsSequencingState based on Integer32"""
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
        *(("both", 4),
          ("local", 3),
          ("none", 1),
          ("remote", 2))
    )


_L2tpSessionStatsSequencingState_Type.__name__ = "Integer32"
_L2tpSessionStatsSequencingState_Object = MibTableColumn
l2tpSessionStatsSequencingState = _L2tpSessionStatsSequencingState_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 20),
    _L2tpSessionStatsSequencingState_Type()
)
l2tpSessionStatsSequencingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsSequencingState.setStatus("current")
_L2tpSessionStatsOutSequence_Type = Counter32
_L2tpSessionStatsOutSequence_Object = MibTableColumn
l2tpSessionStatsOutSequence = _L2tpSessionStatsOutSequence_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 21),
    _L2tpSessionStatsOutSequence_Type()
)
l2tpSessionStatsOutSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsOutSequence.setStatus("current")
_L2tpSessionStatsReassemblyTO_Type = Counter32
_L2tpSessionStatsReassemblyTO_Object = MibTableColumn
l2tpSessionStatsReassemblyTO = _L2tpSessionStatsReassemblyTO_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 22),
    _L2tpSessionStatsReassemblyTO_Type()
)
l2tpSessionStatsReassemblyTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsReassemblyTO.setStatus("current")


class _L2tpSessionStatsTxSeq_Type(Integer32):
    """Custom type l2tpSessionStatsTxSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionStatsTxSeq_Type.__name__ = "Integer32"
_L2tpSessionStatsTxSeq_Object = MibTableColumn
l2tpSessionStatsTxSeq = _L2tpSessionStatsTxSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 23),
    _L2tpSessionStatsTxSeq_Type()
)
l2tpSessionStatsTxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsTxSeq.setStatus("current")


class _L2tpSessionStatsRxSeq_Type(Integer32):
    """Custom type l2tpSessionStatsRxSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionStatsRxSeq_Type.__name__ = "Integer32"
_L2tpSessionStatsRxSeq_Object = MibTableColumn
l2tpSessionStatsRxSeq = _L2tpSessionStatsRxSeq_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 7, 1, 24),
    _L2tpSessionStatsRxSeq_Type()
)
l2tpSessionStatsRxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsRxSeq.setStatus("current")
_L2tpTunnelMapTable_Object = MibTable
l2tpTunnelMapTable = _L2tpTunnelMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 8)
)
if mibBuilder.loadTexts:
    l2tpTunnelMapTable.setStatus("current")
_L2tpTunnelMapEntry_Object = MibTableRow
l2tpTunnelMapEntry = _L2tpTunnelMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 8, 1)
)
l2tpTunnelMapEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpTunnelMapLocalTID"),
)
if mibBuilder.loadTexts:
    l2tpTunnelMapEntry.setStatus("current")


class _L2tpTunnelMapLocalTID_Type(Integer32):
    """Custom type l2tpTunnelMapLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpTunnelMapLocalTID_Type.__name__ = "Integer32"
_L2tpTunnelMapLocalTID_Object = MibTableColumn
l2tpTunnelMapLocalTID = _L2tpTunnelMapLocalTID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 8, 1, 1),
    _L2tpTunnelMapLocalTID_Type()
)
l2tpTunnelMapLocalTID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpTunnelMapLocalTID.setStatus("current")
_L2tpTunnelMapIfIndex_Type = InterfaceIndex
_L2tpTunnelMapIfIndex_Object = MibTableColumn
l2tpTunnelMapIfIndex = _L2tpTunnelMapIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 8, 1, 2),
    _L2tpTunnelMapIfIndex_Type()
)
l2tpTunnelMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelMapIfIndex.setStatus("current")
_L2tpSessionMapTable_Object = MibTable
l2tpSessionMapTable = _L2tpSessionMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9)
)
if mibBuilder.loadTexts:
    l2tpSessionMapTable.setStatus("current")
_L2tpSessionMapEntry_Object = MibTableRow
l2tpSessionMapEntry = _L2tpSessionMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9, 1)
)
l2tpSessionMapEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpSessionMapIfIndex"),
)
if mibBuilder.loadTexts:
    l2tpSessionMapEntry.setStatus("current")
_L2tpSessionMapIfIndex_Type = InterfaceIndex
_L2tpSessionMapIfIndex_Object = MibTableColumn
l2tpSessionMapIfIndex = _L2tpSessionMapIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9, 1, 1),
    _L2tpSessionMapIfIndex_Type()
)
l2tpSessionMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpSessionMapIfIndex.setStatus("current")
_L2tpSessionMapTunnelIfIndex_Type = InterfaceIndex
_L2tpSessionMapTunnelIfIndex_Object = MibTableColumn
l2tpSessionMapTunnelIfIndex = _L2tpSessionMapTunnelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9, 1, 2),
    _L2tpSessionMapTunnelIfIndex_Type()
)
l2tpSessionMapTunnelIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionMapTunnelIfIndex.setStatus("current")


class _L2tpSessionMapLocalSID_Type(Integer32):
    """Custom type l2tpSessionMapLocalSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpSessionMapLocalSID_Type.__name__ = "Integer32"
_L2tpSessionMapLocalSID_Object = MibTableColumn
l2tpSessionMapLocalSID = _L2tpSessionMapLocalSID_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9, 1, 3),
    _L2tpSessionMapLocalSID_Type()
)
l2tpSessionMapLocalSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionMapLocalSID.setStatus("current")
_L2tpSessionMapStatus_Type = RowStatus
_L2tpSessionMapStatus_Object = MibTableColumn
l2tpSessionMapStatus = _L2tpSessionMapStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 1, 9, 1, 4),
    _L2tpSessionMapStatus_Type()
)
l2tpSessionMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionMapStatus.setStatus("current")
_L2tpTransports_ObjectIdentity = ObjectIdentity
l2tpTransports = _L2tpTransports_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 3)
)
_L2tpTransportIpUdp_ObjectIdentity = ObjectIdentity
l2tpTransportIpUdp = _L2tpTransportIpUdp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1)
)
_L2tpIpUdpObjects_ObjectIdentity = ObjectIdentity
l2tpIpUdpObjects = _L2tpIpUdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1)
)
_L2tpUdpStatsTable_Object = MibTable
l2tpUdpStatsTable = _L2tpUdpStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    l2tpUdpStatsTable.setStatus("current")
_L2tpUdpStatsEntry_Object = MibTableRow
l2tpUdpStatsEntry = _L2tpUdpStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1, 2, 1)
)
l2tpUdpStatsEntry.setIndexNames(
    (0, "L2TP-MIB", "l2tpUdpStatsIfIndex"),
)
if mibBuilder.loadTexts:
    l2tpUdpStatsEntry.setStatus("current")
_L2tpUdpStatsIfIndex_Type = InterfaceIndex
_L2tpUdpStatsIfIndex_Object = MibTableColumn
l2tpUdpStatsIfIndex = _L2tpUdpStatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1, 2, 1, 1),
    _L2tpUdpStatsIfIndex_Type()
)
l2tpUdpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpUdpStatsIfIndex.setStatus("current")


class _L2tpUdpStatsPeerPort_Type(Integer32):
    """Custom type l2tpUdpStatsPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpUdpStatsPeerPort_Type.__name__ = "Integer32"
_L2tpUdpStatsPeerPort_Object = MibTableColumn
l2tpUdpStatsPeerPort = _L2tpUdpStatsPeerPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1, 2, 1, 2),
    _L2tpUdpStatsPeerPort_Type()
)
l2tpUdpStatsPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpUdpStatsPeerPort.setStatus("current")


class _L2tpUdpStatsLocalPort_Type(Integer32):
    """Custom type l2tpUdpStatsLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpUdpStatsLocalPort_Type.__name__ = "Integer32"
_L2tpUdpStatsLocalPort_Object = MibTableColumn
l2tpUdpStatsLocalPort = _L2tpUdpStatsLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 1, 2, 1, 3),
    _L2tpUdpStatsLocalPort_Type()
)
l2tpUdpStatsLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpUdpStatsLocalPort.setStatus("current")
_L2tpIpUdpTraps_ObjectIdentity = ObjectIdentity
l2tpIpUdpTraps = _L2tpIpUdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 3, 1, 2)
)
_L2tpConformance_ObjectIdentity = ObjectIdentity
l2tpConformance = _L2tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 4)
)
_L2tpGroups_ObjectIdentity = ObjectIdentity
l2tpGroups = _L2tpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1)
)
_L2tpCompliances_ObjectIdentity = ObjectIdentity
l2tpCompliances = _L2tpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 2)
)
l2tpDomainConfigEntry.registerAugmentions(
    ("L2TP-MIB",
     "l2tpDomainStatsEntry")
)
l2tpDomainStatsEntry.setIndexNames(*l2tpDomainConfigEntry.getIndexNames())
l2tpTunnelConfigEntry.registerAugmentions(
    ("L2TP-MIB",
     "l2tpTunnelStatsEntry")
)
l2tpTunnelStatsEntry.setIndexNames(*l2tpTunnelConfigEntry.getIndexNames())

# Managed Objects groups

l2tpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 1)
)
l2tpConfigGroup.setObjects(
      *(("L2TP-MIB", "l2tpAdminState"),
        ("L2TP-MIB", "l2tpDrainTunnels"),
        ("L2TP-MIB", "l2tpTunnelConfigDomainId"),
        ("L2TP-MIB", "l2tpTunnelConfigHelloInterval"),
        ("L2TP-MIB", "l2tpTunnelConfigIdleTimeout"),
        ("L2TP-MIB", "l2tpTunnelConfigControlRWS"),
        ("L2TP-MIB", "l2tpTunnelConfigControlMaxRetx"),
        ("L2TP-MIB", "l2tpTunnelConfigControlMaxRetxTO"),
        ("L2TP-MIB", "l2tpTunnelConfigPayloadSeq"),
        ("L2TP-MIB", "l2tpTunnelConfigReassemblyTO"),
        ("L2TP-MIB", "l2tpTunnelConfigTransport"),
        ("L2TP-MIB", "l2tpTunnelConfigDrainTunnel"),
        ("L2TP-MIB", "l2tpTunnelConfigProxyPPPAuth"))
)
if mibBuilder.loadTexts:
    l2tpConfigGroup.setStatus("current")

l2tpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 2)
)
l2tpStatsGroup.setObjects(
      *(("L2TP-MIB", "l2tpProtocolVersions"),
        ("L2TP-MIB", "l2tpVendorName"),
        ("L2TP-MIB", "l2tpFirmwareRev"),
        ("L2TP-MIB", "l2tpDrainingTunnels"),
        ("L2TP-MIB", "l2tpTunnelStatsLocalTID"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteTID"),
        ("L2TP-MIB", "l2tpTunnelStatsState"),
        ("L2TP-MIB", "l2tpTunnelStatsInitiated"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteHostName"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteVendorName"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteFirmwareRev"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteProtocolVer"),
        ("L2TP-MIB", "l2tpTunnelStatsInitialRemoteRWS"),
        ("L2TP-MIB", "l2tpTunnelStatsBearerCaps"),
        ("L2TP-MIB", "l2tpTunnelStatsFramingCaps"),
        ("L2TP-MIB", "l2tpTunnelStatsControlRxPkts"),
        ("L2TP-MIB", "l2tpTunnelStatsControlRxZLB"),
        ("L2TP-MIB", "l2tpTunnelStatsControlOutOfSeq"),
        ("L2TP-MIB", "l2tpTunnelStatsControlOutOfWin"),
        ("L2TP-MIB", "l2tpTunnelStatsControlTxPkts"),
        ("L2TP-MIB", "l2tpTunnelStatsControlTxZLB"),
        ("L2TP-MIB", "l2tpTunnelStatsControlAckTO"),
        ("L2TP-MIB", "l2tpTunnelStatsCurrentRemoteRWS"),
        ("L2TP-MIB", "l2tpTunnelStatsTxSeq"),
        ("L2TP-MIB", "l2tpTunnelStatsTxSeqAck"),
        ("L2TP-MIB", "l2tpTunnelStatsRxSeq"),
        ("L2TP-MIB", "l2tpTunnelStatsRxSeqAck"),
        ("L2TP-MIB", "l2tpTunnelStatsTotalSessions"),
        ("L2TP-MIB", "l2tpTunnelStatsFailedSessions"),
        ("L2TP-MIB", "l2tpTunnelStatsActiveSessions"),
        ("L2TP-MIB", "l2tpTunnelStatsLastResultCode"),
        ("L2TP-MIB", "l2tpTunnelStatsLastErrorCode"),
        ("L2TP-MIB", "l2tpTunnelStatsLastErrorMessage"),
        ("L2TP-MIB", "l2tpTunnelStatsDrainingTunnel"),
        ("L2TP-MIB", "l2tpSessionStatsIfIndex"),
        ("L2TP-MIB", "l2tpSessionStatsRemoteSID"),
        ("L2TP-MIB", "l2tpSessionStatsUserName"),
        ("L2TP-MIB", "l2tpSessionStatsState"),
        ("L2TP-MIB", "l2tpSessionStatsCallType"),
        ("L2TP-MIB", "l2tpSessionStatsCallSerialNumber"),
        ("L2TP-MIB", "l2tpSessionStatsTxConnectSpeed"),
        ("L2TP-MIB", "l2tpSessionStatsRxConnectSpeed"),
        ("L2TP-MIB", "l2tpSessionStatsCallBearerType"),
        ("L2TP-MIB", "l2tpSessionStatsFramingType"),
        ("L2TP-MIB", "l2tpSessionStatsPhysChanId"),
        ("L2TP-MIB", "l2tpSessionStatsDNIS"),
        ("L2TP-MIB", "l2tpSessionStatsCLID"),
        ("L2TP-MIB", "l2tpSessionStatsSubAddress"),
        ("L2TP-MIB", "l2tpSessionStatsPrivateGroupID"),
        ("L2TP-MIB", "l2tpSessionStatsProxyLcp"),
        ("L2TP-MIB", "l2tpSessionStatsAuthMethod"),
        ("L2TP-MIB", "l2tpSessionStatsSequencingState"),
        ("L2TP-MIB", "l2tpSessionStatsOutSequence"),
        ("L2TP-MIB", "l2tpSessionStatsReassemblyTO"),
        ("L2TP-MIB", "l2tpSessionStatsTxSeq"),
        ("L2TP-MIB", "l2tpSessionStatsRxSeq"))
)
if mibBuilder.loadTexts:
    l2tpStatsGroup.setStatus("current")

l2tpIpUdpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 3)
)
l2tpIpUdpGroup.setObjects(
      *(("L2TP-MIB", "l2tpUdpStatsPeerPort"),
        ("L2TP-MIB", "l2tpUdpStatsLocalPort"))
)
if mibBuilder.loadTexts:
    l2tpIpUdpGroup.setStatus("current")

l2tpDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 4)
)
l2tpDomainGroup.setObjects(
      *(("L2TP-MIB", "l2tpDomainConfigAdminState"),
        ("L2TP-MIB", "l2tpDomainConfigDrainTunnels"),
        ("L2TP-MIB", "l2tpDomainConfigTunnelHelloInt"),
        ("L2TP-MIB", "l2tpDomainConfigTunnelIdleTO"),
        ("L2TP-MIB", "l2tpDomainConfigControlRWS"),
        ("L2TP-MIB", "l2tpDomainConfigControlMaxRetx"),
        ("L2TP-MIB", "l2tpDomainConfigControlMaxRetxTO"),
        ("L2TP-MIB", "l2tpDomainConfigPayloadSeq"),
        ("L2TP-MIB", "l2tpDomainConfigReassemblyTO"),
        ("L2TP-MIB", "l2tpDomainConfigProxyPPPAuth"),
        ("L2TP-MIB", "l2tpDomainConfigStorageType"),
        ("L2TP-MIB", "l2tpDomainConfigStatus"),
        ("L2TP-MIB", "l2tpDomainStatsTotalTunnels"),
        ("L2TP-MIB", "l2tpDomainStatsFailedTunnels"),
        ("L2TP-MIB", "l2tpDomainStatsFailedAuths"),
        ("L2TP-MIB", "l2tpDomainStatsActiveTunnels"),
        ("L2TP-MIB", "l2tpDomainStatsTotalSessions"),
        ("L2TP-MIB", "l2tpDomainStatsFailedSessions"),
        ("L2TP-MIB", "l2tpDomainStatsActiveSessions"),
        ("L2TP-MIB", "l2tpDomainStatsDrainingTunnels"),
        ("L2TP-MIB", "l2tpDomainStatsControlRxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsControlRxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsControlTxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsControlTxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadRxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadRxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadRxDiscs"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadTxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadTxPkts"))
)
if mibBuilder.loadTexts:
    l2tpDomainGroup.setStatus("current")

l2tpMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 5)
)
l2tpMappingGroup.setObjects(
      *(("L2TP-MIB", "l2tpTunnelMapIfIndex"),
        ("L2TP-MIB", "l2tpSessionMapTunnelIfIndex"),
        ("L2TP-MIB", "l2tpSessionMapLocalSID"),
        ("L2TP-MIB", "l2tpSessionMapStatus"))
)
if mibBuilder.loadTexts:
    l2tpMappingGroup.setStatus("current")

l2tpSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 6)
)
l2tpSecurityGroup.setObjects(
      *(("L2TP-MIB", "l2tpDomainConfigAuth"),
        ("L2TP-MIB", "l2tpDomainConfigSecret"),
        ("L2TP-MIB", "l2tpDomainConfigTunnelSecurity"),
        ("L2TP-MIB", "l2tpTunnelConfigAuth"),
        ("L2TP-MIB", "l2tpTunnelConfigSecret"),
        ("L2TP-MIB", "l2tpTunnelConfigSecurity"))
)
if mibBuilder.loadTexts:
    l2tpSecurityGroup.setStatus("current")

l2tpHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 8)
)
l2tpHCPacketGroup.setObjects(
      *(("L2TP-MIB", "l2tpDomainStatsControlHCRxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsControlHCRxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsControlHCTxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsControlHCTxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadHCRxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadHCRxPkts"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadHCRxDiscs"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadHCTxOctets"),
        ("L2TP-MIB", "l2tpDomainStatsPayloadHCTxPkts"))
)
if mibBuilder.loadTexts:
    l2tpHCPacketGroup.setStatus("current")


# Notification objects

l2tpTunnelAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 95, 0, 1)
)
l2tpTunnelAuthFailure.setObjects(
      *(("L2TP-MIB", "l2tpTunnelStatsInitiated"),
        ("L2TP-MIB", "l2tpTunnelStatsRemoteHostName"))
)
if mibBuilder.loadTexts:
    l2tpTunnelAuthFailure.setStatus(
        "current"
    )


# Notifications groups

l2tpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 1, 7)
)
l2tpTrapGroup.setObjects(
    ("L2TP-MIB", "l2tpTunnelAuthFailure")
)
if mibBuilder.loadTexts:
    l2tpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

l2tpMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 2, 1)
)
if mibBuilder.loadTexts:
    l2tpMIBFullCompliance.setStatus(
        "current"
    )

l2tpMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 95, 4, 2, 2)
)
if mibBuilder.loadTexts:
    l2tpMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2TP-MIB",
    **{"L2tpMilliSeconds": L2tpMilliSeconds,
       "l2tp": l2tp,
       "l2tpNotifications": l2tpNotifications,
       "l2tpTunnelAuthFailure": l2tpTunnelAuthFailure,
       "l2tpObjects": l2tpObjects,
       "l2tpScalar": l2tpScalar,
       "l2tpConfig": l2tpConfig,
       "l2tpAdminState": l2tpAdminState,
       "l2tpDrainTunnels": l2tpDrainTunnels,
       "l2tpStats": l2tpStats,
       "l2tpProtocolVersions": l2tpProtocolVersions,
       "l2tpVendorName": l2tpVendorName,
       "l2tpFirmwareRev": l2tpFirmwareRev,
       "l2tpDrainingTunnels": l2tpDrainingTunnels,
       "l2tpDomainConfigTable": l2tpDomainConfigTable,
       "l2tpDomainConfigEntry": l2tpDomainConfigEntry,
       "l2tpDomainConfigId": l2tpDomainConfigId,
       "l2tpDomainConfigAdminState": l2tpDomainConfigAdminState,
       "l2tpDomainConfigDrainTunnels": l2tpDomainConfigDrainTunnels,
       "l2tpDomainConfigAuth": l2tpDomainConfigAuth,
       "l2tpDomainConfigSecret": l2tpDomainConfigSecret,
       "l2tpDomainConfigTunnelSecurity": l2tpDomainConfigTunnelSecurity,
       "l2tpDomainConfigTunnelHelloInt": l2tpDomainConfigTunnelHelloInt,
       "l2tpDomainConfigTunnelIdleTO": l2tpDomainConfigTunnelIdleTO,
       "l2tpDomainConfigControlRWS": l2tpDomainConfigControlRWS,
       "l2tpDomainConfigControlMaxRetx": l2tpDomainConfigControlMaxRetx,
       "l2tpDomainConfigControlMaxRetxTO": l2tpDomainConfigControlMaxRetxTO,
       "l2tpDomainConfigPayloadSeq": l2tpDomainConfigPayloadSeq,
       "l2tpDomainConfigReassemblyTO": l2tpDomainConfigReassemblyTO,
       "l2tpDomainConfigProxyPPPAuth": l2tpDomainConfigProxyPPPAuth,
       "l2tpDomainConfigStorageType": l2tpDomainConfigStorageType,
       "l2tpDomainConfigStatus": l2tpDomainConfigStatus,
       "l2tpDomainStatsTable": l2tpDomainStatsTable,
       "l2tpDomainStatsEntry": l2tpDomainStatsEntry,
       "l2tpDomainStatsTotalTunnels": l2tpDomainStatsTotalTunnels,
       "l2tpDomainStatsFailedTunnels": l2tpDomainStatsFailedTunnels,
       "l2tpDomainStatsFailedAuths": l2tpDomainStatsFailedAuths,
       "l2tpDomainStatsActiveTunnels": l2tpDomainStatsActiveTunnels,
       "l2tpDomainStatsTotalSessions": l2tpDomainStatsTotalSessions,
       "l2tpDomainStatsFailedSessions": l2tpDomainStatsFailedSessions,
       "l2tpDomainStatsActiveSessions": l2tpDomainStatsActiveSessions,
       "l2tpDomainStatsDrainingTunnels": l2tpDomainStatsDrainingTunnels,
       "l2tpDomainStatsControlRxOctets": l2tpDomainStatsControlRxOctets,
       "l2tpDomainStatsControlRxPkts": l2tpDomainStatsControlRxPkts,
       "l2tpDomainStatsControlTxOctets": l2tpDomainStatsControlTxOctets,
       "l2tpDomainStatsControlTxPkts": l2tpDomainStatsControlTxPkts,
       "l2tpDomainStatsPayloadRxOctets": l2tpDomainStatsPayloadRxOctets,
       "l2tpDomainStatsPayloadRxPkts": l2tpDomainStatsPayloadRxPkts,
       "l2tpDomainStatsPayloadRxDiscs": l2tpDomainStatsPayloadRxDiscs,
       "l2tpDomainStatsPayloadTxOctets": l2tpDomainStatsPayloadTxOctets,
       "l2tpDomainStatsPayloadTxPkts": l2tpDomainStatsPayloadTxPkts,
       "l2tpDomainStatsControlHCRxOctets": l2tpDomainStatsControlHCRxOctets,
       "l2tpDomainStatsControlHCRxPkts": l2tpDomainStatsControlHCRxPkts,
       "l2tpDomainStatsControlHCTxOctets": l2tpDomainStatsControlHCTxOctets,
       "l2tpDomainStatsControlHCTxPkts": l2tpDomainStatsControlHCTxPkts,
       "l2tpDomainStatsPayloadHCRxOctets": l2tpDomainStatsPayloadHCRxOctets,
       "l2tpDomainStatsPayloadHCRxPkts": l2tpDomainStatsPayloadHCRxPkts,
       "l2tpDomainStatsPayloadHCRxDiscs": l2tpDomainStatsPayloadHCRxDiscs,
       "l2tpDomainStatsPayloadHCTxOctets": l2tpDomainStatsPayloadHCTxOctets,
       "l2tpDomainStatsPayloadHCTxPkts": l2tpDomainStatsPayloadHCTxPkts,
       "l2tpTunnelConfigTable": l2tpTunnelConfigTable,
       "l2tpTunnelConfigEntry": l2tpTunnelConfigEntry,
       "l2tpTunnelConfigIfIndex": l2tpTunnelConfigIfIndex,
       "l2tpTunnelConfigDomainId": l2tpTunnelConfigDomainId,
       "l2tpTunnelConfigAuth": l2tpTunnelConfigAuth,
       "l2tpTunnelConfigSecret": l2tpTunnelConfigSecret,
       "l2tpTunnelConfigSecurity": l2tpTunnelConfigSecurity,
       "l2tpTunnelConfigHelloInterval": l2tpTunnelConfigHelloInterval,
       "l2tpTunnelConfigIdleTimeout": l2tpTunnelConfigIdleTimeout,
       "l2tpTunnelConfigControlRWS": l2tpTunnelConfigControlRWS,
       "l2tpTunnelConfigControlMaxRetx": l2tpTunnelConfigControlMaxRetx,
       "l2tpTunnelConfigControlMaxRetxTO": l2tpTunnelConfigControlMaxRetxTO,
       "l2tpTunnelConfigPayloadSeq": l2tpTunnelConfigPayloadSeq,
       "l2tpTunnelConfigReassemblyTO": l2tpTunnelConfigReassemblyTO,
       "l2tpTunnelConfigTransport": l2tpTunnelConfigTransport,
       "l2tpTunnelConfigDrainTunnel": l2tpTunnelConfigDrainTunnel,
       "l2tpTunnelConfigProxyPPPAuth": l2tpTunnelConfigProxyPPPAuth,
       "l2tpTunnelStatsTable": l2tpTunnelStatsTable,
       "l2tpTunnelStatsEntry": l2tpTunnelStatsEntry,
       "l2tpTunnelStatsLocalTID": l2tpTunnelStatsLocalTID,
       "l2tpTunnelStatsRemoteTID": l2tpTunnelStatsRemoteTID,
       "l2tpTunnelStatsState": l2tpTunnelStatsState,
       "l2tpTunnelStatsInitiated": l2tpTunnelStatsInitiated,
       "l2tpTunnelStatsRemoteHostName": l2tpTunnelStatsRemoteHostName,
       "l2tpTunnelStatsRemoteVendorName": l2tpTunnelStatsRemoteVendorName,
       "l2tpTunnelStatsRemoteFirmwareRev": l2tpTunnelStatsRemoteFirmwareRev,
       "l2tpTunnelStatsRemoteProtocolVer": l2tpTunnelStatsRemoteProtocolVer,
       "l2tpTunnelStatsInitialRemoteRWS": l2tpTunnelStatsInitialRemoteRWS,
       "l2tpTunnelStatsBearerCaps": l2tpTunnelStatsBearerCaps,
       "l2tpTunnelStatsFramingCaps": l2tpTunnelStatsFramingCaps,
       "l2tpTunnelStatsControlRxPkts": l2tpTunnelStatsControlRxPkts,
       "l2tpTunnelStatsControlRxZLB": l2tpTunnelStatsControlRxZLB,
       "l2tpTunnelStatsControlOutOfSeq": l2tpTunnelStatsControlOutOfSeq,
       "l2tpTunnelStatsControlOutOfWin": l2tpTunnelStatsControlOutOfWin,
       "l2tpTunnelStatsControlTxPkts": l2tpTunnelStatsControlTxPkts,
       "l2tpTunnelStatsControlTxZLB": l2tpTunnelStatsControlTxZLB,
       "l2tpTunnelStatsControlAckTO": l2tpTunnelStatsControlAckTO,
       "l2tpTunnelStatsCurrentRemoteRWS": l2tpTunnelStatsCurrentRemoteRWS,
       "l2tpTunnelStatsTxSeq": l2tpTunnelStatsTxSeq,
       "l2tpTunnelStatsTxSeqAck": l2tpTunnelStatsTxSeqAck,
       "l2tpTunnelStatsRxSeq": l2tpTunnelStatsRxSeq,
       "l2tpTunnelStatsRxSeqAck": l2tpTunnelStatsRxSeqAck,
       "l2tpTunnelStatsTotalSessions": l2tpTunnelStatsTotalSessions,
       "l2tpTunnelStatsFailedSessions": l2tpTunnelStatsFailedSessions,
       "l2tpTunnelStatsActiveSessions": l2tpTunnelStatsActiveSessions,
       "l2tpTunnelStatsLastResultCode": l2tpTunnelStatsLastResultCode,
       "l2tpTunnelStatsLastErrorCode": l2tpTunnelStatsLastErrorCode,
       "l2tpTunnelStatsLastErrorMessage": l2tpTunnelStatsLastErrorMessage,
       "l2tpTunnelStatsDrainingTunnel": l2tpTunnelStatsDrainingTunnel,
       "l2tpSessionStatsTable": l2tpSessionStatsTable,
       "l2tpSessionStatsEntry": l2tpSessionStatsEntry,
       "l2tpSessionStatsTunnelIfIndex": l2tpSessionStatsTunnelIfIndex,
       "l2tpSessionStatsIfIndex": l2tpSessionStatsIfIndex,
       "l2tpSessionStatsLocalSID": l2tpSessionStatsLocalSID,
       "l2tpSessionStatsRemoteSID": l2tpSessionStatsRemoteSID,
       "l2tpSessionStatsUserName": l2tpSessionStatsUserName,
       "l2tpSessionStatsState": l2tpSessionStatsState,
       "l2tpSessionStatsCallType": l2tpSessionStatsCallType,
       "l2tpSessionStatsCallSerialNumber": l2tpSessionStatsCallSerialNumber,
       "l2tpSessionStatsTxConnectSpeed": l2tpSessionStatsTxConnectSpeed,
       "l2tpSessionStatsRxConnectSpeed": l2tpSessionStatsRxConnectSpeed,
       "l2tpSessionStatsCallBearerType": l2tpSessionStatsCallBearerType,
       "l2tpSessionStatsFramingType": l2tpSessionStatsFramingType,
       "l2tpSessionStatsPhysChanId": l2tpSessionStatsPhysChanId,
       "l2tpSessionStatsDNIS": l2tpSessionStatsDNIS,
       "l2tpSessionStatsCLID": l2tpSessionStatsCLID,
       "l2tpSessionStatsSubAddress": l2tpSessionStatsSubAddress,
       "l2tpSessionStatsPrivateGroupID": l2tpSessionStatsPrivateGroupID,
       "l2tpSessionStatsProxyLcp": l2tpSessionStatsProxyLcp,
       "l2tpSessionStatsAuthMethod": l2tpSessionStatsAuthMethod,
       "l2tpSessionStatsSequencingState": l2tpSessionStatsSequencingState,
       "l2tpSessionStatsOutSequence": l2tpSessionStatsOutSequence,
       "l2tpSessionStatsReassemblyTO": l2tpSessionStatsReassemblyTO,
       "l2tpSessionStatsTxSeq": l2tpSessionStatsTxSeq,
       "l2tpSessionStatsRxSeq": l2tpSessionStatsRxSeq,
       "l2tpTunnelMapTable": l2tpTunnelMapTable,
       "l2tpTunnelMapEntry": l2tpTunnelMapEntry,
       "l2tpTunnelMapLocalTID": l2tpTunnelMapLocalTID,
       "l2tpTunnelMapIfIndex": l2tpTunnelMapIfIndex,
       "l2tpSessionMapTable": l2tpSessionMapTable,
       "l2tpSessionMapEntry": l2tpSessionMapEntry,
       "l2tpSessionMapIfIndex": l2tpSessionMapIfIndex,
       "l2tpSessionMapTunnelIfIndex": l2tpSessionMapTunnelIfIndex,
       "l2tpSessionMapLocalSID": l2tpSessionMapLocalSID,
       "l2tpSessionMapStatus": l2tpSessionMapStatus,
       "l2tpTransports": l2tpTransports,
       "l2tpTransportIpUdp": l2tpTransportIpUdp,
       "l2tpIpUdpObjects": l2tpIpUdpObjects,
       "l2tpUdpStatsTable": l2tpUdpStatsTable,
       "l2tpUdpStatsEntry": l2tpUdpStatsEntry,
       "l2tpUdpStatsIfIndex": l2tpUdpStatsIfIndex,
       "l2tpUdpStatsPeerPort": l2tpUdpStatsPeerPort,
       "l2tpUdpStatsLocalPort": l2tpUdpStatsLocalPort,
       "l2tpIpUdpTraps": l2tpIpUdpTraps,
       "l2tpConformance": l2tpConformance,
       "l2tpGroups": l2tpGroups,
       "l2tpConfigGroup": l2tpConfigGroup,
       "l2tpStatsGroup": l2tpStatsGroup,
       "l2tpIpUdpGroup": l2tpIpUdpGroup,
       "l2tpDomainGroup": l2tpDomainGroup,
       "l2tpMappingGroup": l2tpMappingGroup,
       "l2tpSecurityGroup": l2tpSecurityGroup,
       "l2tpTrapGroup": l2tpTrapGroup,
       "l2tpHCPacketGroup": l2tpHCPacketGroup,
       "l2tpCompliances": l2tpCompliances,
       "l2tpMIBFullCompliance": l2tpMIBFullCompliance,
       "l2tpMIBReadOnlyCompliance": l2tpMIBReadOnlyCompliance}
)
