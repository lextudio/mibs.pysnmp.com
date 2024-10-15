# SNMP MIB module (CISCO-IKE-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IKE-CONFIGURATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:18 2024
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

(CIKEIsakmpDoi,
 CIKELifesize,
 CIKELifetime,
 CIPsecControlProtocol,
 CIPsecDiffHellmanGrp,
 CIPsecEncryptAlgorithm,
 CIPsecIkeAuthMethod,
 CIPsecIkeHashAlgorithm,
 CIPsecIkePRFAlgorithm,
 CIPsecPhase1PeerIdentityType) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIKEIsakmpDoi",
    "CIKELifesize",
    "CIKELifetime",
    "CIPsecControlProtocol",
    "CIPsecDiffHellmanGrp",
    "CIPsecEncryptAlgorithm",
    "CIPsecIkeAuthMethod",
    "CIPsecIkeHashAlgorithm",
    "CIPsecIkePRFAlgorithm",
    "CIPsecPhase1PeerIdentityType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIkeConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423)
)
ciscoIkeConfigMIB.setRevisions(
        ("2004-09-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CicIkeConfigPskIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CicIkeConfigInitiatorIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CicIkeConfigMIBNotifs_ObjectIdentity = ObjectIdentity
cicIkeConfigMIBNotifs = _CicIkeConfigMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0)
)
_CicIkeConfigMIBObjects_ObjectIdentity = ObjectIdentity
cicIkeConfigMIBObjects = _CicIkeConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1)
)
_CicIkeCfgOperations_ObjectIdentity = ObjectIdentity
cicIkeCfgOperations = _CicIkeCfgOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1)
)
_CicIkeEnabled_Type = TruthValue
_CicIkeEnabled_Object = MibScalar
cicIkeEnabled = _CicIkeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1, 1),
    _CicIkeEnabled_Type()
)
cicIkeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeEnabled.setStatus("current")
_CicIkeAggressModeEnabled_Type = TruthValue
_CicIkeAggressModeEnabled_Object = MibScalar
cicIkeAggressModeEnabled = _CicIkeAggressModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1, 2),
    _CicIkeAggressModeEnabled_Type()
)
cicIkeAggressModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeAggressModeEnabled.setStatus("current")
_CicIkeCfgIdentities_ObjectIdentity = ObjectIdentity
cicIkeCfgIdentities = _CicIkeCfgIdentities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2)
)
_CicIkeCfgIdentityTable_Object = MibTable
cicIkeCfgIdentityTable = _CicIkeCfgIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgIdentityTable.setStatus("current")
_CicIkeCfgIdentityEntry_Object = MibTableRow
cicIkeCfgIdentityEntry = _CicIkeCfgIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1)
)
cicIkeCfgIdentityEntry.setIndexNames(
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"),
)
if mibBuilder.loadTexts:
    cicIkeCfgIdentityEntry.setStatus("current")
_CicIkeCfgIdentityDoi_Type = CIKEIsakmpDoi
_CicIkeCfgIdentityDoi_Object = MibTableColumn
cicIkeCfgIdentityDoi = _CicIkeCfgIdentityDoi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1, 1),
    _CicIkeCfgIdentityDoi_Type()
)
cicIkeCfgIdentityDoi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cicIkeCfgIdentityDoi.setStatus("current")
_CicIkeCfgIdentityType_Type = CIPsecPhase1PeerIdentityType
_CicIkeCfgIdentityType_Object = MibTableColumn
cicIkeCfgIdentityType = _CicIkeCfgIdentityType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1, 2),
    _CicIkeCfgIdentityType_Type()
)
cicIkeCfgIdentityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeCfgIdentityType.setStatus("current")
_CicIkeCfgInitiatorNextAvailTable_Object = MibTable
cicIkeCfgInitiatorNextAvailTable = _CicIkeCfgInitiatorNextAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorNextAvailTable.setStatus("current")
_CicIkeCfgInitiatorNextAvailEntry_Object = MibTableRow
cicIkeCfgInitiatorNextAvailEntry = _CicIkeCfgInitiatorNextAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorNextAvailEntry.setStatus("current")
_CicIkeCfgInitiatorNextAvailIndex_Type = CicIkeConfigInitiatorIndex
_CicIkeCfgInitiatorNextAvailIndex_Object = MibTableColumn
cicIkeCfgInitiatorNextAvailIndex = _CicIkeCfgInitiatorNextAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2, 1, 1),
    _CicIkeCfgInitiatorNextAvailIndex_Type()
)
cicIkeCfgInitiatorNextAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorNextAvailIndex.setStatus("current")
_CicIkeCfgInitiatorTable_Object = MibTable
cicIkeCfgInitiatorTable = _CicIkeCfgInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorTable.setStatus("current")
_CicIkeCfgInitiatorEntry_Object = MibTableRow
cicIkeCfgInitiatorEntry = _CicIkeCfgInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1)
)
cicIkeCfgInitiatorEntry.setIndexNames(
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"),
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorIndex"),
)
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorEntry.setStatus("current")
_CicIkeCfgInitiatorIndex_Type = CicIkeConfigInitiatorIndex
_CicIkeCfgInitiatorIndex_Object = MibTableColumn
cicIkeCfgInitiatorIndex = _CicIkeCfgInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 1),
    _CicIkeCfgInitiatorIndex_Type()
)
cicIkeCfgInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorIndex.setStatus("current")
_CicIkeCfgInitiatorPAddrType_Type = CIPsecPhase1PeerIdentityType
_CicIkeCfgInitiatorPAddrType_Object = MibTableColumn
cicIkeCfgInitiatorPAddrType = _CicIkeCfgInitiatorPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 2),
    _CicIkeCfgInitiatorPAddrType_Type()
)
cicIkeCfgInitiatorPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorPAddrType.setStatus("current")


class _CicIkeCfgInitiatorPAddr_Type(OctetString):
    """Custom type cicIkeCfgInitiatorPAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CicIkeCfgInitiatorPAddr_Type.__name__ = "OctetString"
_CicIkeCfgInitiatorPAddr_Object = MibTableColumn
cicIkeCfgInitiatorPAddr = _CicIkeCfgInitiatorPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 3),
    _CicIkeCfgInitiatorPAddr_Type()
)
cicIkeCfgInitiatorPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorPAddr.setStatus("current")
_CicIkeCfgInitiatorVer_Type = CIPsecControlProtocol
_CicIkeCfgInitiatorVer_Object = MibTableColumn
cicIkeCfgInitiatorVer = _CicIkeCfgInitiatorVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 4),
    _CicIkeCfgInitiatorVer_Type()
)
cicIkeCfgInitiatorVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorVer.setStatus("current")
_CicIkeCfgInitiatorStatus_Type = RowStatus
_CicIkeCfgInitiatorStatus_Object = MibTableColumn
cicIkeCfgInitiatorStatus = _CicIkeCfgInitiatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 5),
    _CicIkeCfgInitiatorStatus_Type()
)
cicIkeCfgInitiatorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgInitiatorStatus.setStatus("current")
_CicIkeCfgFailureRecovery_ObjectIdentity = ObjectIdentity
cicIkeCfgFailureRecovery = _CicIkeCfgFailureRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3)
)
_CicIkeCfgFailureRecovConfigTable_Object = MibTable
cicIkeCfgFailureRecovConfigTable = _CicIkeCfgFailureRecovConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgFailureRecovConfigTable.setStatus("current")
_CicIkeCfgFailureRecovConfigEntry_Object = MibTableRow
cicIkeCfgFailureRecovConfigEntry = _CicIkeCfgFailureRecovConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgFailureRecovConfigEntry.setStatus("current")
_CicIkeKeepAliveEnabled_Type = TruthValue
_CicIkeKeepAliveEnabled_Object = MibTableColumn
cicIkeKeepAliveEnabled = _CicIkeKeepAliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 1),
    _CicIkeKeepAliveEnabled_Type()
)
cicIkeKeepAliveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeKeepAliveEnabled.setStatus("current")


class _CicIkeKeepAliveType_Type(Integer32):
    """Custom type cicIkeKeepAliveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ondemand", 3),
          ("periodic", 2))
    )


_CicIkeKeepAliveType_Type.__name__ = "Integer32"
_CicIkeKeepAliveType_Object = MibTableColumn
cicIkeKeepAliveType = _CicIkeKeepAliveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 2),
    _CicIkeKeepAliveType_Type()
)
cicIkeKeepAliveType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeKeepAliveType.setStatus("current")


class _CicIkeKeepAliveInterval_Type(Unsigned32):
    """Custom type cicIkeKeepAliveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CicIkeKeepAliveInterval_Type.__name__ = "Unsigned32"
_CicIkeKeepAliveInterval_Object = MibTableColumn
cicIkeKeepAliveInterval = _CicIkeKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 3),
    _CicIkeKeepAliveInterval_Type()
)
cicIkeKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cicIkeKeepAliveInterval.setUnits("seconds")


class _CicIkeKeepAliveRetryInterval_Type(Unsigned32):
    """Custom type cicIkeKeepAliveRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CicIkeKeepAliveRetryInterval_Type.__name__ = "Unsigned32"
_CicIkeKeepAliveRetryInterval_Object = MibTableColumn
cicIkeKeepAliveRetryInterval = _CicIkeKeepAliveRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 4),
    _CicIkeKeepAliveRetryInterval_Type()
)
cicIkeKeepAliveRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeKeepAliveRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cicIkeKeepAliveRetryInterval.setUnits("seconds")
_CicIkeInvalidSpiNotify_Type = TruthValue
_CicIkeInvalidSpiNotify_Object = MibTableColumn
cicIkeInvalidSpiNotify = _CicIkeInvalidSpiNotify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 5),
    _CicIkeInvalidSpiNotify_Type()
)
cicIkeInvalidSpiNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicIkeInvalidSpiNotify.setStatus("current")
_CicIkeCfgPeerAuth_ObjectIdentity = ObjectIdentity
cicIkeCfgPeerAuth = _CicIkeCfgPeerAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4)
)
_CicIkeCfgPskAuthConfig_ObjectIdentity = ObjectIdentity
cicIkeCfgPskAuthConfig = _CicIkeCfgPskAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1)
)
_CicIkeCfgPskNextAvailTable_Object = MibTable
cicIkeCfgPskNextAvailTable = _CicIkeCfgPskNextAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgPskNextAvailTable.setStatus("current")
_CicIkeCfgPskNextAvailEntry_Object = MibTableRow
cicIkeCfgPskNextAvailEntry = _CicIkeCfgPskNextAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgPskNextAvailEntry.setStatus("current")
_CicIkeCfgPskNextAvailIndex_Type = CicIkeConfigPskIndex
_CicIkeCfgPskNextAvailIndex_Object = MibTableColumn
cicIkeCfgPskNextAvailIndex = _CicIkeCfgPskNextAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1, 1, 1),
    _CicIkeCfgPskNextAvailIndex_Type()
)
cicIkeCfgPskNextAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicIkeCfgPskNextAvailIndex.setStatus("current")
_CicIkeCfgPskTable_Object = MibTable
cicIkeCfgPskTable = _CicIkeCfgPskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cicIkeCfgPskTable.setStatus("current")
_CicIkeCfgPskEntry_Object = MibTableRow
cicIkeCfgPskEntry = _CicIkeCfgPskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1)
)
cicIkeCfgPskEntry.setIndexNames(
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"),
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskIndex"),
)
if mibBuilder.loadTexts:
    cicIkeCfgPskEntry.setStatus("current")
_CicIkeCfgPskIndex_Type = CicIkeConfigPskIndex
_CicIkeCfgPskIndex_Object = MibTableColumn
cicIkeCfgPskIndex = _CicIkeCfgPskIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 1),
    _CicIkeCfgPskIndex_Type()
)
cicIkeCfgPskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cicIkeCfgPskIndex.setStatus("current")


class _CicIkeCfgPskKey_Type(OctetString):
    """Custom type cicIkeCfgPskKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CicIkeCfgPskKey_Type.__name__ = "OctetString"
_CicIkeCfgPskKey_Object = MibTableColumn
cicIkeCfgPskKey = _CicIkeCfgPskKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 2),
    _CicIkeCfgPskKey_Type()
)
cicIkeCfgPskKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskKey.setStatus("current")
_CicIkeCfgPskRemIdentType_Type = CIPsecPhase1PeerIdentityType
_CicIkeCfgPskRemIdentType_Object = MibTableColumn
cicIkeCfgPskRemIdentType = _CicIkeCfgPskRemIdentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 3),
    _CicIkeCfgPskRemIdentType_Type()
)
cicIkeCfgPskRemIdentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdentType.setStatus("current")
_CicIkeCfgPskRemIdentTypeStand_Type = InetAddressType
_CicIkeCfgPskRemIdentTypeStand_Object = MibTableColumn
cicIkeCfgPskRemIdentTypeStand = _CicIkeCfgPskRemIdentTypeStand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 4),
    _CicIkeCfgPskRemIdentTypeStand_Type()
)
cicIkeCfgPskRemIdentTypeStand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdentTypeStand.setStatus("current")


class _CicIkeCfgPskRemIdentity_Type(OctetString):
    """Custom type cicIkeCfgPskRemIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CicIkeCfgPskRemIdentity_Type.__name__ = "OctetString"
_CicIkeCfgPskRemIdentity_Object = MibTableColumn
cicIkeCfgPskRemIdentity = _CicIkeCfgPskRemIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 5),
    _CicIkeCfgPskRemIdentity_Type()
)
cicIkeCfgPskRemIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdentity.setStatus("current")
_CicIkeCfgPskRemIdAddrOrRg1OrSn_Type = InetAddress
_CicIkeCfgPskRemIdAddrOrRg1OrSn_Object = MibTableColumn
cicIkeCfgPskRemIdAddrOrRg1OrSn = _CicIkeCfgPskRemIdAddrOrRg1OrSn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 6),
    _CicIkeCfgPskRemIdAddrOrRg1OrSn_Type()
)
cicIkeCfgPskRemIdAddrOrRg1OrSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdAddrOrRg1OrSn.setStatus("current")
_CicIkeCfgPskRemIdAddrRange2_Type = InetAddress
_CicIkeCfgPskRemIdAddrRange2_Object = MibTableColumn
cicIkeCfgPskRemIdAddrRange2 = _CicIkeCfgPskRemIdAddrRange2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 7),
    _CicIkeCfgPskRemIdAddrRange2_Type()
)
cicIkeCfgPskRemIdAddrRange2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdAddrRange2.setStatus("current")
_CicIkeCfgPskRemIdSubnetMask_Type = InetAddressPrefixLength
_CicIkeCfgPskRemIdSubnetMask_Object = MibTableColumn
cicIkeCfgPskRemIdSubnetMask = _CicIkeCfgPskRemIdSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 8),
    _CicIkeCfgPskRemIdSubnetMask_Type()
)
cicIkeCfgPskRemIdSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskRemIdSubnetMask.setStatus("current")
_CicIkeCfgPskStatus_Type = RowStatus
_CicIkeCfgPskStatus_Object = MibTableColumn
cicIkeCfgPskStatus = _CicIkeCfgPskStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 9),
    _CicIkeCfgPskStatus_Type()
)
cicIkeCfgPskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPskStatus.setStatus("current")
_CicIkeCfgNonceAuthConfig_ObjectIdentity = ObjectIdentity
cicIkeCfgNonceAuthConfig = _CicIkeCfgNonceAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 2)
)
_CicIkeCfgPkiAuthConfig_ObjectIdentity = ObjectIdentity
cicIkeCfgPkiAuthConfig = _CicIkeCfgPkiAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 3)
)
_CicIkeCfgPolicies_ObjectIdentity = ObjectIdentity
cicIkeCfgPolicies = _CicIkeCfgPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5)
)
_CicIkeCfgPolicyTable_Object = MibTable
cicIkeCfgPolicyTable = _CicIkeCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgPolicyTable.setStatus("current")
_CicIkeCfgPolicyEntry_Object = MibTableRow
cicIkeCfgPolicyEntry = _CicIkeCfgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1)
)
cicIkeCfgPolicyEntry.setIndexNames(
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"),
    (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyPriority"),
)
if mibBuilder.loadTexts:
    cicIkeCfgPolicyEntry.setStatus("current")


class _CicIkeCfgPolicyPriority_Type(Unsigned32):
    """Custom type cicIkeCfgPolicyPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CicIkeCfgPolicyPriority_Type.__name__ = "Unsigned32"
_CicIkeCfgPolicyPriority_Object = MibTableColumn
cicIkeCfgPolicyPriority = _CicIkeCfgPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 1),
    _CicIkeCfgPolicyPriority_Type()
)
cicIkeCfgPolicyPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyPriority.setStatus("current")


class _CicIkeCfgPolicyEncr_Type(CIPsecEncryptAlgorithm):
    """Custom type cicIkeCfgPolicyEncr based on CIPsecEncryptAlgorithm"""


_CicIkeCfgPolicyEncr_Object = MibTableColumn
cicIkeCfgPolicyEncr = _CicIkeCfgPolicyEncr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 2),
    _CicIkeCfgPolicyEncr_Type()
)
cicIkeCfgPolicyEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyEncr.setStatus("current")


class _CicIkeCfgPolicyHash_Type(CIPsecIkeHashAlgorithm):
    """Custom type cicIkeCfgPolicyHash based on CIPsecIkeHashAlgorithm"""


_CicIkeCfgPolicyHash_Object = MibTableColumn
cicIkeCfgPolicyHash = _CicIkeCfgPolicyHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 3),
    _CicIkeCfgPolicyHash_Type()
)
cicIkeCfgPolicyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyHash.setStatus("current")


class _CicIkeCfgPolicyPRF_Type(CIPsecIkePRFAlgorithm):
    """Custom type cicIkeCfgPolicyPRF based on CIPsecIkePRFAlgorithm"""


_CicIkeCfgPolicyPRF_Object = MibTableColumn
cicIkeCfgPolicyPRF = _CicIkeCfgPolicyPRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 4),
    _CicIkeCfgPolicyPRF_Type()
)
cicIkeCfgPolicyPRF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyPRF.setStatus("current")


class _CicIkeCfgPolicyAuth_Type(CIPsecIkeAuthMethod):
    """Custom type cicIkeCfgPolicyAuth based on CIPsecIkeAuthMethod"""


_CicIkeCfgPolicyAuth_Object = MibTableColumn
cicIkeCfgPolicyAuth = _CicIkeCfgPolicyAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 5),
    _CicIkeCfgPolicyAuth_Type()
)
cicIkeCfgPolicyAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyAuth.setStatus("current")


class _CicIkeCfgPolicyDHGroup_Type(CIPsecDiffHellmanGrp):
    """Custom type cicIkeCfgPolicyDHGroup based on CIPsecDiffHellmanGrp"""


_CicIkeCfgPolicyDHGroup_Object = MibTableColumn
cicIkeCfgPolicyDHGroup = _CicIkeCfgPolicyDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 6),
    _CicIkeCfgPolicyDHGroup_Type()
)
cicIkeCfgPolicyDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyDHGroup.setStatus("current")


class _CicIkeCfgPolicyLifetime_Type(CIKELifetime):
    """Custom type cicIkeCfgPolicyLifetime based on CIKELifetime"""
    defaultValue = 86400


_CicIkeCfgPolicyLifetime_Object = MibTableColumn
cicIkeCfgPolicyLifetime = _CicIkeCfgPolicyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 7),
    _CicIkeCfgPolicyLifetime_Type()
)
cicIkeCfgPolicyLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyLifetime.setUnits("seconds")


class _CicIkeCfgPolicyLifesize_Type(CIKELifesize):
    """Custom type cicIkeCfgPolicyLifesize based on CIKELifesize"""
    defaultValue = 2560


_CicIkeCfgPolicyLifesize_Object = MibTableColumn
cicIkeCfgPolicyLifesize = _CicIkeCfgPolicyLifesize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 8),
    _CicIkeCfgPolicyLifesize_Type()
)
cicIkeCfgPolicyLifesize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyLifesize.setStatus("current")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyLifesize.setUnits("kbytes")
_CicIkeCfgPolicyStatus_Type = RowStatus
_CicIkeCfgPolicyStatus_Object = MibTableColumn
cicIkeCfgPolicyStatus = _CicIkeCfgPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 9),
    _CicIkeCfgPolicyStatus_Type()
)
cicIkeCfgPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cicIkeCfgPolicyStatus.setStatus("current")
_CicIkeCfgServiceControl_ObjectIdentity = ObjectIdentity
cicIkeCfgServiceControl = _CicIkeCfgServiceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6)
)
_CicIkeCfgCallAdmssionnCtrl_ObjectIdentity = ObjectIdentity
cicIkeCfgCallAdmssionnCtrl = _CicIkeCfgCallAdmssionnCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6, 1)
)
_CicIkeCfgQoSControl_ObjectIdentity = ObjectIdentity
cicIkeCfgQoSControl = _CicIkeCfgQoSControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6, 2)
)
_CicIkeConfigMibNotifCntl_ObjectIdentity = ObjectIdentity
cicIkeConfigMibNotifCntl = _CicIkeConfigMibNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7)
)


class _CicNotifCntlIkeAllNotifs_Type(TruthValue):
    """Custom type cicNotifCntlIkeAllNotifs based on TruthValue"""


_CicNotifCntlIkeAllNotifs_Object = MibScalar
cicNotifCntlIkeAllNotifs = _CicNotifCntlIkeAllNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 1),
    _CicNotifCntlIkeAllNotifs_Type()
)
cicNotifCntlIkeAllNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkeAllNotifs.setStatus("current")


class _CicNotifCntlIkeOperStateChanged_Type(TruthValue):
    """Custom type cicNotifCntlIkeOperStateChanged based on TruthValue"""


_CicNotifCntlIkeOperStateChanged_Object = MibScalar
cicNotifCntlIkeOperStateChanged = _CicNotifCntlIkeOperStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 2),
    _CicNotifCntlIkeOperStateChanged_Type()
)
cicNotifCntlIkeOperStateChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkeOperStateChanged.setStatus("current")


class _CicNotifCntlIkePskAdded_Type(TruthValue):
    """Custom type cicNotifCntlIkePskAdded based on TruthValue"""


_CicNotifCntlIkePskAdded_Object = MibScalar
cicNotifCntlIkePskAdded = _CicNotifCntlIkePskAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 3),
    _CicNotifCntlIkePskAdded_Type()
)
cicNotifCntlIkePskAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkePskAdded.setStatus("current")


class _CicNotifCntlIkePskDeleted_Type(TruthValue):
    """Custom type cicNotifCntlIkePskDeleted based on TruthValue"""


_CicNotifCntlIkePskDeleted_Object = MibScalar
cicNotifCntlIkePskDeleted = _CicNotifCntlIkePskDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 4),
    _CicNotifCntlIkePskDeleted_Type()
)
cicNotifCntlIkePskDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkePskDeleted.setStatus("current")


class _CicNotifCntlIkePolicyAdded_Type(TruthValue):
    """Custom type cicNotifCntlIkePolicyAdded based on TruthValue"""


_CicNotifCntlIkePolicyAdded_Object = MibScalar
cicNotifCntlIkePolicyAdded = _CicNotifCntlIkePolicyAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 5),
    _CicNotifCntlIkePolicyAdded_Type()
)
cicNotifCntlIkePolicyAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkePolicyAdded.setStatus("current")


class _CicNotifCntlIkePolicyDeleted_Type(TruthValue):
    """Custom type cicNotifCntlIkePolicyDeleted based on TruthValue"""


_CicNotifCntlIkePolicyDeleted_Object = MibScalar
cicNotifCntlIkePolicyDeleted = _CicNotifCntlIkePolicyDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 6),
    _CicNotifCntlIkePolicyDeleted_Type()
)
cicNotifCntlIkePolicyDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicNotifCntlIkePolicyDeleted.setStatus("current")
_CicIkeConfigMIBConform_ObjectIdentity = ObjectIdentity
cicIkeConfigMIBConform = _CicIkeConfigMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2)
)
_CicIkeCfgMIBGroups_ObjectIdentity = ObjectIdentity
cicIkeCfgMIBGroups = _CicIkeCfgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1)
)
_CicIkeCfgMIBCompliances_ObjectIdentity = ObjectIdentity
cicIkeCfgMIBCompliances = _CicIkeCfgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 2)
)
cicIkeCfgIdentityEntry.registerAugmentions(
    ("CISCO-IKE-CONFIGURATION-MIB",
     "cicIkeCfgInitiatorNextAvailEntry")
)
cicIkeCfgInitiatorNextAvailEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())
cicIkeCfgIdentityEntry.registerAugmentions(
    ("CISCO-IKE-CONFIGURATION-MIB",
     "cicIkeCfgFailureRecovConfigEntry")
)
cicIkeCfgFailureRecovConfigEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())
cicIkeCfgIdentityEntry.registerAugmentions(
    ("CISCO-IKE-CONFIGURATION-MIB",
     "cicIkeCfgPskNextAvailEntry")
)
cicIkeCfgPskNextAvailEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())

# Managed Objects groups

cicIkeCfgOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 1)
)
cicIkeCfgOperGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeEnabled"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeAggressModeEnabled"))
)
if mibBuilder.loadTexts:
    cicIkeCfgOperGroup.setStatus("current")

cicIkeCfgIdentitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 2)
)
cicIkeCfgIdentitiesGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorNextAvailIndex"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorPAddrType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorPAddr"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorVer"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorStatus"))
)
if mibBuilder.loadTexts:
    cicIkeCfgIdentitiesGroup.setStatus("current")

cicIkeCfgFailureRecoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 3)
)
cicIkeCfgFailureRecoveryGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveEnabled"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveInterval"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveRetryInterval"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeInvalidSpiNotify"))
)
if mibBuilder.loadTexts:
    cicIkeCfgFailureRecoveryGroup.setStatus("current")

cicIkeCfgPskAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 4)
)
cicIkeCfgPskAuthGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskNextAvailIndex"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskKey"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentTypeStand"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdAddrOrRg1OrSn"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdAddrRange2"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdSubnetMask"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskStatus"))
)
if mibBuilder.loadTexts:
    cicIkeCfgPskAuthGroup.setStatus("current")

cicIkeCfgPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 5)
)
cicIkeCfgPolicyGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyPRF"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyLifetime"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyStatus"))
)
if mibBuilder.loadTexts:
    cicIkeCfgPolicyGroup.setStatus("current")

cicIkeCfgOptionalPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 6)
)
cicIkeCfgOptionalPolicyGroup.setObjects(
    ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyLifesize")
)
if mibBuilder.loadTexts:
    cicIkeCfgOptionalPolicyGroup.setStatus("current")

cicIkeCfgNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 7)
)
cicIkeCfgNotifCntlGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkeAllNotifs"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkeOperStateChanged"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePskAdded"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePskDeleted"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePolicyAdded"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePolicyDeleted"))
)
if mibBuilder.loadTexts:
    cicIkeCfgNotifCntlGroup.setStatus("current")


# Notification objects

ciscoIkeConfigOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 1)
)
ciscoIkeConfigOperStateChanged.setObjects(
    ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeEnabled")
)
if mibBuilder.loadTexts:
    ciscoIkeConfigOperStateChanged.setStatus(
        "current"
    )

ciscoIkeConfigPskAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 2)
)
ciscoIkeConfigPskAdded.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"))
)
if mibBuilder.loadTexts:
    ciscoIkeConfigPskAdded.setStatus(
        "current"
    )

ciscoIkeConfigPskDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 3)
)
ciscoIkeConfigPskDeleted.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"))
)
if mibBuilder.loadTexts:
    ciscoIkeConfigPskDeleted.setStatus(
        "current"
    )

ciscoIkeConfigPolicyAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 4)
)
ciscoIkeConfigPolicyAdded.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"))
)
if mibBuilder.loadTexts:
    ciscoIkeConfigPolicyAdded.setStatus(
        "current"
    )

ciscoIkeConfigPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 5)
)
ciscoIkeConfigPolicyDeleted.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"),
        ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"))
)
if mibBuilder.loadTexts:
    ciscoIkeConfigPolicyDeleted.setStatus(
        "current"
    )


# Notifications groups

cicIkeCfgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 8)
)
cicIkeCfgNotificationGroup.setObjects(
      *(("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigOperStateChanged"),
        ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPskAdded"),
        ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPskDeleted"),
        ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPolicyAdded"),
        ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPolicyDeleted"))
)
if mibBuilder.loadTexts:
    cicIkeCfgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cicIkeCfgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cicIkeCfgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IKE-CONFIGURATION-MIB",
    **{"CicIkeConfigPskIndex": CicIkeConfigPskIndex,
       "CicIkeConfigInitiatorIndex": CicIkeConfigInitiatorIndex,
       "ciscoIkeConfigMIB": ciscoIkeConfigMIB,
       "cicIkeConfigMIBNotifs": cicIkeConfigMIBNotifs,
       "ciscoIkeConfigOperStateChanged": ciscoIkeConfigOperStateChanged,
       "ciscoIkeConfigPskAdded": ciscoIkeConfigPskAdded,
       "ciscoIkeConfigPskDeleted": ciscoIkeConfigPskDeleted,
       "ciscoIkeConfigPolicyAdded": ciscoIkeConfigPolicyAdded,
       "ciscoIkeConfigPolicyDeleted": ciscoIkeConfigPolicyDeleted,
       "cicIkeConfigMIBObjects": cicIkeConfigMIBObjects,
       "cicIkeCfgOperations": cicIkeCfgOperations,
       "cicIkeEnabled": cicIkeEnabled,
       "cicIkeAggressModeEnabled": cicIkeAggressModeEnabled,
       "cicIkeCfgIdentities": cicIkeCfgIdentities,
       "cicIkeCfgIdentityTable": cicIkeCfgIdentityTable,
       "cicIkeCfgIdentityEntry": cicIkeCfgIdentityEntry,
       "cicIkeCfgIdentityDoi": cicIkeCfgIdentityDoi,
       "cicIkeCfgIdentityType": cicIkeCfgIdentityType,
       "cicIkeCfgInitiatorNextAvailTable": cicIkeCfgInitiatorNextAvailTable,
       "cicIkeCfgInitiatorNextAvailEntry": cicIkeCfgInitiatorNextAvailEntry,
       "cicIkeCfgInitiatorNextAvailIndex": cicIkeCfgInitiatorNextAvailIndex,
       "cicIkeCfgInitiatorTable": cicIkeCfgInitiatorTable,
       "cicIkeCfgInitiatorEntry": cicIkeCfgInitiatorEntry,
       "cicIkeCfgInitiatorIndex": cicIkeCfgInitiatorIndex,
       "cicIkeCfgInitiatorPAddrType": cicIkeCfgInitiatorPAddrType,
       "cicIkeCfgInitiatorPAddr": cicIkeCfgInitiatorPAddr,
       "cicIkeCfgInitiatorVer": cicIkeCfgInitiatorVer,
       "cicIkeCfgInitiatorStatus": cicIkeCfgInitiatorStatus,
       "cicIkeCfgFailureRecovery": cicIkeCfgFailureRecovery,
       "cicIkeCfgFailureRecovConfigTable": cicIkeCfgFailureRecovConfigTable,
       "cicIkeCfgFailureRecovConfigEntry": cicIkeCfgFailureRecovConfigEntry,
       "cicIkeKeepAliveEnabled": cicIkeKeepAliveEnabled,
       "cicIkeKeepAliveType": cicIkeKeepAliveType,
       "cicIkeKeepAliveInterval": cicIkeKeepAliveInterval,
       "cicIkeKeepAliveRetryInterval": cicIkeKeepAliveRetryInterval,
       "cicIkeInvalidSpiNotify": cicIkeInvalidSpiNotify,
       "cicIkeCfgPeerAuth": cicIkeCfgPeerAuth,
       "cicIkeCfgPskAuthConfig": cicIkeCfgPskAuthConfig,
       "cicIkeCfgPskNextAvailTable": cicIkeCfgPskNextAvailTable,
       "cicIkeCfgPskNextAvailEntry": cicIkeCfgPskNextAvailEntry,
       "cicIkeCfgPskNextAvailIndex": cicIkeCfgPskNextAvailIndex,
       "cicIkeCfgPskTable": cicIkeCfgPskTable,
       "cicIkeCfgPskEntry": cicIkeCfgPskEntry,
       "cicIkeCfgPskIndex": cicIkeCfgPskIndex,
       "cicIkeCfgPskKey": cicIkeCfgPskKey,
       "cicIkeCfgPskRemIdentType": cicIkeCfgPskRemIdentType,
       "cicIkeCfgPskRemIdentTypeStand": cicIkeCfgPskRemIdentTypeStand,
       "cicIkeCfgPskRemIdentity": cicIkeCfgPskRemIdentity,
       "cicIkeCfgPskRemIdAddrOrRg1OrSn": cicIkeCfgPskRemIdAddrOrRg1OrSn,
       "cicIkeCfgPskRemIdAddrRange2": cicIkeCfgPskRemIdAddrRange2,
       "cicIkeCfgPskRemIdSubnetMask": cicIkeCfgPskRemIdSubnetMask,
       "cicIkeCfgPskStatus": cicIkeCfgPskStatus,
       "cicIkeCfgNonceAuthConfig": cicIkeCfgNonceAuthConfig,
       "cicIkeCfgPkiAuthConfig": cicIkeCfgPkiAuthConfig,
       "cicIkeCfgPolicies": cicIkeCfgPolicies,
       "cicIkeCfgPolicyTable": cicIkeCfgPolicyTable,
       "cicIkeCfgPolicyEntry": cicIkeCfgPolicyEntry,
       "cicIkeCfgPolicyPriority": cicIkeCfgPolicyPriority,
       "cicIkeCfgPolicyEncr": cicIkeCfgPolicyEncr,
       "cicIkeCfgPolicyHash": cicIkeCfgPolicyHash,
       "cicIkeCfgPolicyPRF": cicIkeCfgPolicyPRF,
       "cicIkeCfgPolicyAuth": cicIkeCfgPolicyAuth,
       "cicIkeCfgPolicyDHGroup": cicIkeCfgPolicyDHGroup,
       "cicIkeCfgPolicyLifetime": cicIkeCfgPolicyLifetime,
       "cicIkeCfgPolicyLifesize": cicIkeCfgPolicyLifesize,
       "cicIkeCfgPolicyStatus": cicIkeCfgPolicyStatus,
       "cicIkeCfgServiceControl": cicIkeCfgServiceControl,
       "cicIkeCfgCallAdmssionnCtrl": cicIkeCfgCallAdmssionnCtrl,
       "cicIkeCfgQoSControl": cicIkeCfgQoSControl,
       "cicIkeConfigMibNotifCntl": cicIkeConfigMibNotifCntl,
       "cicNotifCntlIkeAllNotifs": cicNotifCntlIkeAllNotifs,
       "cicNotifCntlIkeOperStateChanged": cicNotifCntlIkeOperStateChanged,
       "cicNotifCntlIkePskAdded": cicNotifCntlIkePskAdded,
       "cicNotifCntlIkePskDeleted": cicNotifCntlIkePskDeleted,
       "cicNotifCntlIkePolicyAdded": cicNotifCntlIkePolicyAdded,
       "cicNotifCntlIkePolicyDeleted": cicNotifCntlIkePolicyDeleted,
       "cicIkeConfigMIBConform": cicIkeConfigMIBConform,
       "cicIkeCfgMIBGroups": cicIkeCfgMIBGroups,
       "cicIkeCfgOperGroup": cicIkeCfgOperGroup,
       "cicIkeCfgIdentitiesGroup": cicIkeCfgIdentitiesGroup,
       "cicIkeCfgFailureRecoveryGroup": cicIkeCfgFailureRecoveryGroup,
       "cicIkeCfgPskAuthGroup": cicIkeCfgPskAuthGroup,
       "cicIkeCfgPolicyGroup": cicIkeCfgPolicyGroup,
       "cicIkeCfgOptionalPolicyGroup": cicIkeCfgOptionalPolicyGroup,
       "cicIkeCfgNotifCntlGroup": cicIkeCfgNotifCntlGroup,
       "cicIkeCfgNotificationGroup": cicIkeCfgNotificationGroup,
       "cicIkeCfgMIBCompliances": cicIkeCfgMIBCompliances,
       "cicIkeCfgMIBCompliance": cicIkeCfgMIBCompliance}
)
