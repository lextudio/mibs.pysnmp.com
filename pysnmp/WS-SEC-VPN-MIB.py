# SNMP MIB module (WS-SEC-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-SEC-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:31 2024
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(wsSec,) = mibBuilder.importSymbols(
    "WS-SMI",
    "wsSec")


# MODULE-IDENTITY

wsSecVpnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1)
)
wsSecVpnMib.setRevisions(
        ("2006-07-14 18:26",)
)


# Types definitions



class AbbrRowStatus(Integer32):
    """Custom type AbbrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsSecIKEScalars_ObjectIdentity = ObjectIdentity
wsSecIKEScalars = _WsSecIKEScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 1)
)


class _WsSecIKEKeepAlive_Type(Unsigned32):
    """Custom type wsSecIKEKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_WsSecIKEKeepAlive_Type.__name__ = "Unsigned32"
_WsSecIKEKeepAlive_Object = MibScalar
wsSecIKEKeepAlive = _WsSecIKEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 1, 1),
    _WsSecIKEKeepAlive_Type()
)
wsSecIKEKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecIKEKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    wsSecIKEKeepAlive.setUnits("seconds")


class _WsSecISAKMPLocalIdentity_Type(Integer32):
    """Custom type wsSecISAKMPLocalIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("distinguishedName", 2),
          ("domainName", 3),
          ("ipAddress", 1))
    )


_WsSecISAKMPLocalIdentity_Type.__name__ = "Integer32"
_WsSecISAKMPLocalIdentity_Object = MibScalar
wsSecISAKMPLocalIdentity = _WsSecISAKMPLocalIdentity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 1, 2),
    _WsSecISAKMPLocalIdentity_Type()
)
wsSecISAKMPLocalIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecISAKMPLocalIdentity.setStatus("current")
_WsSecIKEPolicyTable_Object = MibTable
wsSecIKEPolicyTable = _WsSecIKEPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2)
)
if mibBuilder.loadTexts:
    wsSecIKEPolicyTable.setStatus("current")
_WsSecIKEPolicyEntry_Object = MibTableRow
wsSecIKEPolicyEntry = _WsSecIKEPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1)
)
wsSecIKEPolicyEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecIKEPolicyPriority"),
)
if mibBuilder.loadTexts:
    wsSecIKEPolicyEntry.setStatus("current")


class _WsSecIKEPolicyPriority_Type(Unsigned32):
    """Custom type wsSecIKEPolicyPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10001),
    )


_WsSecIKEPolicyPriority_Type.__name__ = "Unsigned32"
_WsSecIKEPolicyPriority_Object = MibTableColumn
wsSecIKEPolicyPriority = _WsSecIKEPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 1),
    _WsSecIKEPolicyPriority_Type()
)
wsSecIKEPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKEPolicyPriority.setStatus("current")


class _WsSecIKEPolicyEncryption_Type(Integer32):
    """Custom type wsSecIKEPolicyEncryption based on Integer32"""
    defaultValue = 1

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
        *(("aes", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("des", 1),
          ("tripleDes", 2))
    )


_WsSecIKEPolicyEncryption_Type.__name__ = "Integer32"
_WsSecIKEPolicyEncryption_Object = MibTableColumn
wsSecIKEPolicyEncryption = _WsSecIKEPolicyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 2),
    _WsSecIKEPolicyEncryption_Type()
)
wsSecIKEPolicyEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicyEncryption.setStatus("current")


class _WsSecIKEPolicyHash_Type(Integer32):
    """Custom type wsSecIKEPolicyHash based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha1", 1))
    )


_WsSecIKEPolicyHash_Type.__name__ = "Integer32"
_WsSecIKEPolicyHash_Object = MibTableColumn
wsSecIKEPolicyHash = _WsSecIKEPolicyHash_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 3),
    _WsSecIKEPolicyHash_Type()
)
wsSecIKEPolicyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicyHash.setStatus("current")


class _WsSecIKEPolicyAuthType_Type(Integer32):
    """Custom type wsSecIKEPolicyAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKey", 2),
          ("rsaSig", 1))
    )


_WsSecIKEPolicyAuthType_Type.__name__ = "Integer32"
_WsSecIKEPolicyAuthType_Object = MibTableColumn
wsSecIKEPolicyAuthType = _WsSecIKEPolicyAuthType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 4),
    _WsSecIKEPolicyAuthType_Type()
)
wsSecIKEPolicyAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicyAuthType.setStatus("current")


class _WsSecIKEPolicyDHGroup_Type(Integer32):
    """Custom type wsSecIKEPolicyDHGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5))
    )


_WsSecIKEPolicyDHGroup_Type.__name__ = "Integer32"
_WsSecIKEPolicyDHGroup_Object = MibTableColumn
wsSecIKEPolicyDHGroup = _WsSecIKEPolicyDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 5),
    _WsSecIKEPolicyDHGroup_Type()
)
wsSecIKEPolicyDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicyDHGroup.setStatus("current")


class _WsSecIKEPolicySaLifeTimeSec_Type(Unsigned32):
    """Custom type wsSecIKEPolicySaLifeTimeSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483646),
    )


_WsSecIKEPolicySaLifeTimeSec_Type.__name__ = "Unsigned32"
_WsSecIKEPolicySaLifeTimeSec_Object = MibTableColumn
wsSecIKEPolicySaLifeTimeSec = _WsSecIKEPolicySaLifeTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 6),
    _WsSecIKEPolicySaLifeTimeSec_Type()
)
wsSecIKEPolicySaLifeTimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicySaLifeTimeSec.setStatus("current")
if mibBuilder.loadTexts:
    wsSecIKEPolicySaLifeTimeSec.setUnits("seconds")
_WsSecIKEPolicyRowStatus_Type = AbbrRowStatus
_WsSecIKEPolicyRowStatus_Object = MibTableColumn
wsSecIKEPolicyRowStatus = _WsSecIKEPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 2, 1, 7),
    _WsSecIKEPolicyRowStatus_Type()
)
wsSecIKEPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecIKEPolicyRowStatus.setStatus("current")
_WsSecPreSharedKeyTable_Object = MibTable
wsSecPreSharedKeyTable = _WsSecPreSharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3)
)
if mibBuilder.loadTexts:
    wsSecPreSharedKeyTable.setStatus("current")
_WsSecPreSharedKeyEntry_Object = MibTableRow
wsSecPreSharedKeyEntry = _WsSecPreSharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1)
)
wsSecPreSharedKeyEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecPreSharedKeyIKEPeer"),
)
if mibBuilder.loadTexts:
    wsSecPreSharedKeyEntry.setStatus("current")
_WsSecPreSharedKeyIKEPeer_Type = DisplayString
_WsSecPreSharedKeyIKEPeer_Object = MibTableColumn
wsSecPreSharedKeyIKEPeer = _WsSecPreSharedKeyIKEPeer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1, 1),
    _WsSecPreSharedKeyIKEPeer_Type()
)
wsSecPreSharedKeyIKEPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecPreSharedKeyIKEPeer.setStatus("current")


class _WsSecPreSharedKeyIKEPeerIdentity_Type(Integer32):
    """Custom type wsSecPreSharedKeyIKEPeerIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("distinguishedName", 2),
          ("domainName", 3),
          ("ipAddress", 1))
    )


_WsSecPreSharedKeyIKEPeerIdentity_Type.__name__ = "Integer32"
_WsSecPreSharedKeyIKEPeerIdentity_Object = MibTableColumn
wsSecPreSharedKeyIKEPeerIdentity = _WsSecPreSharedKeyIKEPeerIdentity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1, 2),
    _WsSecPreSharedKeyIKEPeerIdentity_Type()
)
wsSecPreSharedKeyIKEPeerIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecPreSharedKeyIKEPeerIdentity.setStatus("current")


class _WsSecPreSharedKeyIKEPeerKey_Type(OctetString):
    """Custom type wsSecPreSharedKeyIKEPeerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 255),
    )


_WsSecPreSharedKeyIKEPeerKey_Type.__name__ = "OctetString"
_WsSecPreSharedKeyIKEPeerKey_Object = MibTableColumn
wsSecPreSharedKeyIKEPeerKey = _WsSecPreSharedKeyIKEPeerKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1, 3),
    _WsSecPreSharedKeyIKEPeerKey_Type()
)
wsSecPreSharedKeyIKEPeerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecPreSharedKeyIKEPeerKey.setStatus("current")
_WsSecPreSharedKeyIKEAggressive_Type = TruthValue
_WsSecPreSharedKeyIKEAggressive_Object = MibTableColumn
wsSecPreSharedKeyIKEAggressive = _WsSecPreSharedKeyIKEAggressive_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1, 4),
    _WsSecPreSharedKeyIKEAggressive_Type()
)
wsSecPreSharedKeyIKEAggressive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecPreSharedKeyIKEAggressive.setStatus("current")
_WsSecPreSharedKeyRowStatus_Type = AbbrRowStatus
_WsSecPreSharedKeyRowStatus_Object = MibTableColumn
wsSecPreSharedKeyRowStatus = _WsSecPreSharedKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 3, 1, 5),
    _WsSecPreSharedKeyRowStatus_Type()
)
wsSecPreSharedKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecPreSharedKeyRowStatus.setStatus("current")
_WsSecTransformSetTable_Object = MibTable
wsSecTransformSetTable = _WsSecTransformSetTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4)
)
if mibBuilder.loadTexts:
    wsSecTransformSetTable.setStatus("current")
_WsSecTransformSetEntry_Object = MibTableRow
wsSecTransformSetEntry = _WsSecTransformSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1)
)
wsSecTransformSetEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecTransformSetName"),
)
if mibBuilder.loadTexts:
    wsSecTransformSetEntry.setStatus("current")


class _WsSecTransformSetName_Type(DisplayString):
    """Custom type wsSecTransformSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WsSecTransformSetName_Type.__name__ = "DisplayString"
_WsSecTransformSetName_Object = MibTableColumn
wsSecTransformSetName = _WsSecTransformSetName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 1),
    _WsSecTransformSetName_Type()
)
wsSecTransformSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecTransformSetName.setStatus("current")


class _WsSecTransformSetMode_Type(Integer32):
    """Custom type wsSecTransformSetMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 1),
          ("tunnel", 2))
    )


_WsSecTransformSetMode_Type.__name__ = "Integer32"
_WsSecTransformSetMode_Object = MibTableColumn
wsSecTransformSetMode = _WsSecTransformSetMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 2),
    _WsSecTransformSetMode_Type()
)
wsSecTransformSetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecTransformSetMode.setStatus("current")


class _WsSecTransformSetAHAuth_Type(Integer32):
    """Custom type wsSecTransformSetAHAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ahMd5Hmac", 1),
          ("ahShaHmac", 2),
          ("none", 0))
    )


_WsSecTransformSetAHAuth_Type.__name__ = "Integer32"
_WsSecTransformSetAHAuth_Object = MibTableColumn
wsSecTransformSetAHAuth = _WsSecTransformSetAHAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 3),
    _WsSecTransformSetAHAuth_Type()
)
wsSecTransformSetAHAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecTransformSetAHAuth.setStatus("current")


class _WsSecTransformSetEspEncr_Type(Integer32):
    """Custom type wsSecTransformSetEspEncr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("esp3Des", 4),
          ("espAes", 5),
          ("espAes192", 6),
          ("espAes256", 7),
          ("espDes", 3),
          ("none", 0))
    )


_WsSecTransformSetEspEncr_Type.__name__ = "Integer32"
_WsSecTransformSetEspEncr_Object = MibTableColumn
wsSecTransformSetEspEncr = _WsSecTransformSetEspEncr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 4),
    _WsSecTransformSetEspEncr_Type()
)
wsSecTransformSetEspEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecTransformSetEspEncr.setStatus("current")


class _WsSecTransformSetEspAuth_Type(Integer32):
    """Custom type wsSecTransformSetEspAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("espMd5Hmac", 8),
          ("espShaHmac", 9),
          ("none", 0))
    )


_WsSecTransformSetEspAuth_Type.__name__ = "Integer32"
_WsSecTransformSetEspAuth_Object = MibTableColumn
wsSecTransformSetEspAuth = _WsSecTransformSetEspAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 5),
    _WsSecTransformSetEspAuth_Type()
)
wsSecTransformSetEspAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecTransformSetEspAuth.setStatus("current")
_WsSecTransformSetRowStatus_Type = AbbrRowStatus
_WsSecTransformSetRowStatus_Object = MibTableColumn
wsSecTransformSetRowStatus = _WsSecTransformSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 4, 1, 6),
    _WsSecTransformSetRowStatus_Type()
)
wsSecTransformSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecTransformSetRowStatus.setStatus("current")
_WsSecIPSecCfgScalars_ObjectIdentity = ObjectIdentity
wsSecIPSecCfgScalars = _WsSecIPSecCfgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 5)
)


class _WsSecVpnSALifeTimeSec_Type(Unsigned32):
    """Custom type wsSecVpnSALifeTimeSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 2147483646),
    )


_WsSecVpnSALifeTimeSec_Type.__name__ = "Unsigned32"
_WsSecVpnSALifeTimeSec_Object = MibScalar
wsSecVpnSALifeTimeSec = _WsSecVpnSALifeTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 5, 1),
    _WsSecVpnSALifeTimeSec_Type()
)
wsSecVpnSALifeTimeSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecVpnSALifeTimeSec.setStatus("current")
if mibBuilder.loadTexts:
    wsSecVpnSALifeTimeSec.setUnits("seconds")


class _WsSecVpnSALifeTimeKB_Type(Unsigned32):
    """Custom type wsSecVpnSALifeTimeKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2147483646),
    )


_WsSecVpnSALifeTimeKB_Type.__name__ = "Unsigned32"
_WsSecVpnSALifeTimeKB_Object = MibScalar
wsSecVpnSALifeTimeKB = _WsSecVpnSALifeTimeKB_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 5, 2),
    _WsSecVpnSALifeTimeKB_Type()
)
wsSecVpnSALifeTimeKB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecVpnSALifeTimeKB.setStatus("current")
if mibBuilder.loadTexts:
    wsSecVpnSALifeTimeKB.setUnits("KBytes")
_WsSecLocalIPAddrPoolTable_Object = MibTable
wsSecLocalIPAddrPoolTable = _WsSecLocalIPAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 6)
)
if mibBuilder.loadTexts:
    wsSecLocalIPAddrPoolTable.setStatus("current")
_WsSecLocalIPAddrPoolEntry_Object = MibTableRow
wsSecLocalIPAddrPoolEntry = _WsSecLocalIPAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 6, 1)
)
wsSecLocalIPAddrPoolEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecLocalIPAddrPoolAddrRangeStart"),
    (0, "WS-SEC-VPN-MIB", "wsSecLocalIPAddrPoolAddrRangeEnd"),
)
if mibBuilder.loadTexts:
    wsSecLocalIPAddrPoolEntry.setStatus("current")
_WsSecLocalIPAddrPoolAddrRangeStart_Type = IpAddress
_WsSecLocalIPAddrPoolAddrRangeStart_Object = MibTableColumn
wsSecLocalIPAddrPoolAddrRangeStart = _WsSecLocalIPAddrPoolAddrRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 6, 1, 1),
    _WsSecLocalIPAddrPoolAddrRangeStart_Type()
)
wsSecLocalIPAddrPoolAddrRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecLocalIPAddrPoolAddrRangeStart.setStatus("current")
_WsSecLocalIPAddrPoolAddrRangeEnd_Type = IpAddress
_WsSecLocalIPAddrPoolAddrRangeEnd_Object = MibTableColumn
wsSecLocalIPAddrPoolAddrRangeEnd = _WsSecLocalIPAddrPoolAddrRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 6, 1, 2),
    _WsSecLocalIPAddrPoolAddrRangeEnd_Type()
)
wsSecLocalIPAddrPoolAddrRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecLocalIPAddrPoolAddrRangeEnd.setStatus("current")
_WsSecLocalIPAddrPoolRowStatus_Type = AbbrRowStatus
_WsSecLocalIPAddrPoolRowStatus_Object = MibTableColumn
wsSecLocalIPAddrPoolRowStatus = _WsSecLocalIPAddrPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 6, 1, 3),
    _WsSecLocalIPAddrPoolRowStatus_Type()
)
wsSecLocalIPAddrPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecLocalIPAddrPoolRowStatus.setStatus("current")
_WsSecLocalIPAddressPoolScalars_ObjectIdentity = ObjectIdentity
wsSecLocalIPAddressPoolScalars = _WsSecLocalIPAddressPoolScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 7)
)
_WsSecClientDNSServerIP_Type = IpAddress
_WsSecClientDNSServerIP_Object = MibScalar
wsSecClientDNSServerIP = _WsSecClientDNSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 7, 1),
    _WsSecClientDNSServerIP_Type()
)
wsSecClientDNSServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecClientDNSServerIP.setStatus("current")
_WsSecClientWinServerIP_Type = IpAddress
_WsSecClientWinServerIP_Object = MibScalar
wsSecClientWinServerIP = _WsSecClientWinServerIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 7, 2),
    _WsSecClientWinServerIP_Type()
)
wsSecClientWinServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecClientWinServerIP.setStatus("current")
_WsSecCryptoMapTable_Object = MibTable
wsSecCryptoMapTable = _WsSecCryptoMapTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8)
)
if mibBuilder.loadTexts:
    wsSecCryptoMapTable.setStatus("current")
_WsSecCryptoMapEntry_Object = MibTableRow
wsSecCryptoMapEntry = _WsSecCryptoMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1)
)
wsSecCryptoMapEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapSequenceNum"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapName"),
)
if mibBuilder.loadTexts:
    wsSecCryptoMapEntry.setStatus("current")


class _WsSecCryptoMapSequenceNum_Type(Unsigned32):
    """Custom type wsSecCryptoMapSequenceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WsSecCryptoMapSequenceNum_Type.__name__ = "Unsigned32"
_WsSecCryptoMapSequenceNum_Object = MibTableColumn
wsSecCryptoMapSequenceNum = _WsSecCryptoMapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 1),
    _WsSecCryptoMapSequenceNum_Type()
)
wsSecCryptoMapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapSequenceNum.setStatus("current")
_WsSecCryptoMapName_Type = DisplayString
_WsSecCryptoMapName_Object = MibTableColumn
wsSecCryptoMapName = _WsSecCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 2),
    _WsSecCryptoMapName_Type()
)
wsSecCryptoMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapName.setStatus("current")


class _WsSecCryptoMapACLId_Type(DisplayString):
    """Custom type wsSecCryptoMapACLId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsSecCryptoMapACLId_Type.__name__ = "DisplayString"
_WsSecCryptoMapACLId_Object = MibTableColumn
wsSecCryptoMapACLId = _WsSecCryptoMapACLId_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 3),
    _WsSecCryptoMapACLId_Type()
)
wsSecCryptoMapACLId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapACLId.setStatus("current")


class _WsSecCryptoMapSALifeTimeSec_Type(Unsigned32):
    """Custom type wsSecCryptoMapSALifeTimeSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 2147483646),
    )


_WsSecCryptoMapSALifeTimeSec_Type.__name__ = "Unsigned32"
_WsSecCryptoMapSALifeTimeSec_Object = MibTableColumn
wsSecCryptoMapSALifeTimeSec = _WsSecCryptoMapSALifeTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 4),
    _WsSecCryptoMapSALifeTimeSec_Type()
)
wsSecCryptoMapSALifeTimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapSALifeTimeSec.setStatus("current")


class _WsSecCryptoMapSALifeTimeKB_Type(Unsigned32):
    """Custom type wsSecCryptoMapSALifeTimeKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2147483646),
    )


_WsSecCryptoMapSALifeTimeKB_Type.__name__ = "Unsigned32"
_WsSecCryptoMapSALifeTimeKB_Object = MibTableColumn
wsSecCryptoMapSALifeTimeKB = _WsSecCryptoMapSALifeTimeKB_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 5),
    _WsSecCryptoMapSALifeTimeKB_Type()
)
wsSecCryptoMapSALifeTimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapSALifeTimeKB.setStatus("current")


class _WsSecCryptoMapPFS_Type(Integer32):
    """Custom type wsSecCryptoMapPFS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("none", 0))
    )


_WsSecCryptoMapPFS_Type.__name__ = "Integer32"
_WsSecCryptoMapPFS_Object = MibTableColumn
wsSecCryptoMapPFS = _WsSecCryptoMapPFS_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 6),
    _WsSecCryptoMapPFS_Type()
)
wsSecCryptoMapPFS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapPFS.setStatus("current")
_WsSecCryptoMapSAPerHostEnable_Type = TruthValue
_WsSecCryptoMapSAPerHostEnable_Object = MibTableColumn
wsSecCryptoMapSAPerHostEnable = _WsSecCryptoMapSAPerHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 7),
    _WsSecCryptoMapSAPerHostEnable_Type()
)
wsSecCryptoMapSAPerHostEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapSAPerHostEnable.setStatus("current")
_WsSecCryptoMapModeCfgEnable_Type = TruthValue
_WsSecCryptoMapModeCfgEnable_Object = MibTableColumn
wsSecCryptoMapModeCfgEnable = _WsSecCryptoMapModeCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 8),
    _WsSecCryptoMapModeCfgEnable_Type()
)
wsSecCryptoMapModeCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapModeCfgEnable.setStatus("current")
_WsSecCryptoMapLocalId_Type = DisplayString
_WsSecCryptoMapLocalId_Object = MibTableColumn
wsSecCryptoMapLocalId = _WsSecCryptoMapLocalId_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 9),
    _WsSecCryptoMapLocalId_Type()
)
wsSecCryptoMapLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapLocalId.setStatus("current")


class _WsSecCryptoMapLocalIdType_Type(Integer32):
    """Custom type wsSecCryptoMapLocalIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dn", 2),
          ("hostName", 3),
          ("none", 0))
    )


_WsSecCryptoMapLocalIdType_Type.__name__ = "Integer32"
_WsSecCryptoMapLocalIdType_Object = MibTableColumn
wsSecCryptoMapLocalIdType = _WsSecCryptoMapLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 10),
    _WsSecCryptoMapLocalIdType_Type()
)
wsSecCryptoMapLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapLocalIdType.setStatus("current")


class _WsSecCryptoMapMode_Type(Integer32):
    """Custom type wsSecCryptoMapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_WsSecCryptoMapMode_Type.__name__ = "Integer32"
_WsSecCryptoMapMode_Object = MibTableColumn
wsSecCryptoMapMode = _WsSecCryptoMapMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 11),
    _WsSecCryptoMapMode_Type()
)
wsSecCryptoMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapMode.setStatus("current")


class _WsSecCryptoMapRemoteType_Type(Integer32):
    """Custom type wsSecCryptoMapRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2tp", 2),
          ("xauth", 1))
    )


_WsSecCryptoMapRemoteType_Type.__name__ = "Integer32"
_WsSecCryptoMapRemoteType_Object = MibTableColumn
wsSecCryptoMapRemoteType = _WsSecCryptoMapRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 12),
    _WsSecCryptoMapRemoteType_Type()
)
wsSecCryptoMapRemoteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapRemoteType.setStatus("current")
_WsSecCryptoMapRowStatus_Type = AbbrRowStatus
_WsSecCryptoMapRowStatus_Object = MibTableColumn
wsSecCryptoMapRowStatus = _WsSecCryptoMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 8, 1, 13),
    _WsSecCryptoMapRowStatus_Type()
)
wsSecCryptoMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapRowStatus.setStatus("current")
_WsSecCryptoMapPeerTable_Object = MibTable
wsSecCryptoMapPeerTable = _WsSecCryptoMapPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9)
)
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerTable.setStatus("current")
_WsSecCryptoMapPeerEntry_Object = MibTableRow
wsSecCryptoMapPeerEntry = _WsSecCryptoMapPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9, 1)
)
wsSecCryptoMapPeerEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapPeerSequenceNum"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapPeerName"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapPeerIKEPeer"),
)
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerEntry.setStatus("current")


class _WsSecCryptoMapPeerSequenceNum_Type(Unsigned32):
    """Custom type wsSecCryptoMapPeerSequenceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WsSecCryptoMapPeerSequenceNum_Type.__name__ = "Unsigned32"
_WsSecCryptoMapPeerSequenceNum_Object = MibTableColumn
wsSecCryptoMapPeerSequenceNum = _WsSecCryptoMapPeerSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9, 1, 1),
    _WsSecCryptoMapPeerSequenceNum_Type()
)
wsSecCryptoMapPeerSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerSequenceNum.setStatus("current")
_WsSecCryptoMapPeerName_Type = DisplayString
_WsSecCryptoMapPeerName_Object = MibTableColumn
wsSecCryptoMapPeerName = _WsSecCryptoMapPeerName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9, 1, 2),
    _WsSecCryptoMapPeerName_Type()
)
wsSecCryptoMapPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerName.setStatus("current")
_WsSecCryptoMapPeerIKEPeer_Type = DisplayString
_WsSecCryptoMapPeerIKEPeer_Object = MibTableColumn
wsSecCryptoMapPeerIKEPeer = _WsSecCryptoMapPeerIKEPeer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9, 1, 3),
    _WsSecCryptoMapPeerIKEPeer_Type()
)
wsSecCryptoMapPeerIKEPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerIKEPeer.setStatus("current")
_WsSecCryptoMapPeerRowStatus_Type = AbbrRowStatus
_WsSecCryptoMapPeerRowStatus_Object = MibTableColumn
wsSecCryptoMapPeerRowStatus = _WsSecCryptoMapPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 9, 1, 4),
    _WsSecCryptoMapPeerRowStatus_Type()
)
wsSecCryptoMapPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapPeerRowStatus.setStatus("current")
_WsSecCryptoMapManualSaTable_Object = MibTable
wsSecCryptoMapManualSaTable = _WsSecCryptoMapManualSaTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10)
)
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaTable.setStatus("current")
_WsSecCryptoMapManualSaEntry_Object = MibTableRow
wsSecCryptoMapManualSaEntry = _WsSecCryptoMapManualSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1)
)
wsSecCryptoMapManualSaEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaCryptoMapSeqNum"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaCryptoMapName"),
)
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaEntry.setStatus("current")


class _WsSecCryptoMapManualSaCryptoMapSeqNum_Type(Unsigned32):
    """Custom type wsSecCryptoMapManualSaCryptoMapSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WsSecCryptoMapManualSaCryptoMapSeqNum_Type.__name__ = "Unsigned32"
_WsSecCryptoMapManualSaCryptoMapSeqNum_Object = MibTableColumn
wsSecCryptoMapManualSaCryptoMapSeqNum = _WsSecCryptoMapManualSaCryptoMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 1),
    _WsSecCryptoMapManualSaCryptoMapSeqNum_Type()
)
wsSecCryptoMapManualSaCryptoMapSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaCryptoMapSeqNum.setStatus("current")
_WsSecCryptoMapManualSaCryptoMapName_Type = DisplayString
_WsSecCryptoMapManualSaCryptoMapName_Object = MibTableColumn
wsSecCryptoMapManualSaCryptoMapName = _WsSecCryptoMapManualSaCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 2),
    _WsSecCryptoMapManualSaCryptoMapName_Type()
)
wsSecCryptoMapManualSaCryptoMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaCryptoMapName.setStatus("current")
_WsSecCryptoMapManualSaIKEPeer_Type = DisplayString
_WsSecCryptoMapManualSaIKEPeer_Object = MibTableColumn
wsSecCryptoMapManualSaIKEPeer = _WsSecCryptoMapManualSaIKEPeer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 3),
    _WsSecCryptoMapManualSaIKEPeer_Type()
)
wsSecCryptoMapManualSaIKEPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaIKEPeer.setStatus("current")


class _WsSecCryptoMapManualSaAclId_Type(DisplayString):
    """Custom type wsSecCryptoMapManualSaAclId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsSecCryptoMapManualSaAclId_Type.__name__ = "DisplayString"
_WsSecCryptoMapManualSaAclId_Object = MibTableColumn
wsSecCryptoMapManualSaAclId = _WsSecCryptoMapManualSaAclId_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 4),
    _WsSecCryptoMapManualSaAclId_Type()
)
wsSecCryptoMapManualSaAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaAclId.setStatus("current")


class _WsSecCryptoMapManualSaInAhSpi_Type(Unsigned32):
    """Custom type wsSecCryptoMapManualSaInAhSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_WsSecCryptoMapManualSaInAhSpi_Type.__name__ = "Unsigned32"
_WsSecCryptoMapManualSaInAhSpi_Object = MibTableColumn
wsSecCryptoMapManualSaInAhSpi = _WsSecCryptoMapManualSaInAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 5),
    _WsSecCryptoMapManualSaInAhSpi_Type()
)
wsSecCryptoMapManualSaInAhSpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaInAhSpi.setStatus("current")
_WsSecCryptoMapManualSaInAuthKey_Type = OctetString
_WsSecCryptoMapManualSaInAuthKey_Object = MibTableColumn
wsSecCryptoMapManualSaInAuthKey = _WsSecCryptoMapManualSaInAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 6),
    _WsSecCryptoMapManualSaInAuthKey_Type()
)
wsSecCryptoMapManualSaInAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaInAuthKey.setStatus("current")


class _WsSecCryptoMapManualSaOutAhSpi_Type(Unsigned32):
    """Custom type wsSecCryptoMapManualSaOutAhSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_WsSecCryptoMapManualSaOutAhSpi_Type.__name__ = "Unsigned32"
_WsSecCryptoMapManualSaOutAhSpi_Object = MibTableColumn
wsSecCryptoMapManualSaOutAhSpi = _WsSecCryptoMapManualSaOutAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 7),
    _WsSecCryptoMapManualSaOutAhSpi_Type()
)
wsSecCryptoMapManualSaOutAhSpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaOutAhSpi.setStatus("current")
_WsSecCryptoMapManualSaOutAuthKey_Type = OctetString
_WsSecCryptoMapManualSaOutAuthKey_Object = MibTableColumn
wsSecCryptoMapManualSaOutAuthKey = _WsSecCryptoMapManualSaOutAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 8),
    _WsSecCryptoMapManualSaOutAuthKey_Type()
)
wsSecCryptoMapManualSaOutAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaOutAuthKey.setStatus("current")


class _WsSecCryptoMapManualSaInEspSpi_Type(Unsigned32):
    """Custom type wsSecCryptoMapManualSaInEspSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_WsSecCryptoMapManualSaInEspSpi_Type.__name__ = "Unsigned32"
_WsSecCryptoMapManualSaInEspSpi_Object = MibTableColumn
wsSecCryptoMapManualSaInEspSpi = _WsSecCryptoMapManualSaInEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 9),
    _WsSecCryptoMapManualSaInEspSpi_Type()
)
wsSecCryptoMapManualSaInEspSpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaInEspSpi.setStatus("current")
_WsSecCryptoMapManualSaInEspCipherKey_Type = OctetString
_WsSecCryptoMapManualSaInEspCipherKey_Object = MibTableColumn
wsSecCryptoMapManualSaInEspCipherKey = _WsSecCryptoMapManualSaInEspCipherKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 10),
    _WsSecCryptoMapManualSaInEspCipherKey_Type()
)
wsSecCryptoMapManualSaInEspCipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaInEspCipherKey.setStatus("current")


class _WsSecCryptoMapManualSaOutEspSpi_Type(Unsigned32):
    """Custom type wsSecCryptoMapManualSaOutEspSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_WsSecCryptoMapManualSaOutEspSpi_Type.__name__ = "Unsigned32"
_WsSecCryptoMapManualSaOutEspSpi_Object = MibTableColumn
wsSecCryptoMapManualSaOutEspSpi = _WsSecCryptoMapManualSaOutEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 11),
    _WsSecCryptoMapManualSaOutEspSpi_Type()
)
wsSecCryptoMapManualSaOutEspSpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaOutEspSpi.setStatus("current")
_WsSecCryptoMapManualSaOutEspCipherKey_Type = OctetString
_WsSecCryptoMapManualSaOutEspCipherKey_Object = MibTableColumn
wsSecCryptoMapManualSaOutEspCipherKey = _WsSecCryptoMapManualSaOutEspCipherKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 12),
    _WsSecCryptoMapManualSaOutEspCipherKey_Type()
)
wsSecCryptoMapManualSaOutEspCipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaOutEspCipherKey.setStatus("current")
_WsSecCryptoMapManualSaTSName_Type = DisplayString
_WsSecCryptoMapManualSaTSName_Object = MibTableColumn
wsSecCryptoMapManualSaTSName = _WsSecCryptoMapManualSaTSName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 13),
    _WsSecCryptoMapManualSaTSName_Type()
)
wsSecCryptoMapManualSaTSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaTSName.setStatus("current")


class _WsSecCryptoMapManualSaAhOrEsp_Type(Integer32):
    """Custom type wsSecCryptoMapManualSaAhOrEsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2),
          ("none", 0))
    )


_WsSecCryptoMapManualSaAhOrEsp_Type.__name__ = "Integer32"
_WsSecCryptoMapManualSaAhOrEsp_Object = MibTableColumn
wsSecCryptoMapManualSaAhOrEsp = _WsSecCryptoMapManualSaAhOrEsp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 14),
    _WsSecCryptoMapManualSaAhOrEsp_Type()
)
wsSecCryptoMapManualSaAhOrEsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaAhOrEsp.setStatus("current")
_WsSecCryptoMapManualSaRowStatus_Type = AbbrRowStatus
_WsSecCryptoMapManualSaRowStatus_Object = MibTableColumn
wsSecCryptoMapManualSaRowStatus = _WsSecCryptoMapManualSaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 10, 1, 15),
    _WsSecCryptoMapManualSaRowStatus_Type()
)
wsSecCryptoMapManualSaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapManualSaRowStatus.setStatus("current")
_WsSecCryptoMapTransformSetTable_Object = MibTable
wsSecCryptoMapTransformSetTable = _WsSecCryptoMapTransformSetTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11)
)
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformSetTable.setStatus("current")
_WsSecCryptoMapTransformSetEntry_Object = MibTableRow
wsSecCryptoMapTransformSetEntry = _WsSecCryptoMapTransformSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11, 1)
)
wsSecCryptoMapTransformSetEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapTransformCryptoMapSetSeqNum"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapTransformSetCryptoMapName"),
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapTransformSetName"),
)
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformSetEntry.setStatus("current")


class _WsSecCryptoMapTransformCryptoMapSetSeqNum_Type(Unsigned32):
    """Custom type wsSecCryptoMapTransformCryptoMapSetSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WsSecCryptoMapTransformCryptoMapSetSeqNum_Type.__name__ = "Unsigned32"
_WsSecCryptoMapTransformCryptoMapSetSeqNum_Object = MibTableColumn
wsSecCryptoMapTransformCryptoMapSetSeqNum = _WsSecCryptoMapTransformCryptoMapSetSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11, 1, 1),
    _WsSecCryptoMapTransformCryptoMapSetSeqNum_Type()
)
wsSecCryptoMapTransformCryptoMapSetSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformCryptoMapSetSeqNum.setStatus("current")
_WsSecCryptoMapTransformSetCryptoMapName_Type = DisplayString
_WsSecCryptoMapTransformSetCryptoMapName_Object = MibTableColumn
wsSecCryptoMapTransformSetCryptoMapName = _WsSecCryptoMapTransformSetCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11, 1, 2),
    _WsSecCryptoMapTransformSetCryptoMapName_Type()
)
wsSecCryptoMapTransformSetCryptoMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformSetCryptoMapName.setStatus("current")


class _WsSecCryptoMapTransformSetName_Type(DisplayString):
    """Custom type wsSecCryptoMapTransformSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsSecCryptoMapTransformSetName_Type.__name__ = "DisplayString"
_WsSecCryptoMapTransformSetName_Object = MibTableColumn
wsSecCryptoMapTransformSetName = _WsSecCryptoMapTransformSetName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11, 1, 3),
    _WsSecCryptoMapTransformSetName_Type()
)
wsSecCryptoMapTransformSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformSetName.setStatus("current")
_WsSecCryptoMapTransformSetRowStatus_Type = AbbrRowStatus
_WsSecCryptoMapTransformSetRowStatus_Object = MibTableColumn
wsSecCryptoMapTransformSetRowStatus = _WsSecCryptoMapTransformSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 11, 1, 4),
    _WsSecCryptoMapTransformSetRowStatus_Type()
)
wsSecCryptoMapTransformSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecCryptoMapTransformSetRowStatus.setStatus("current")
_WsSecCryptoMapIfMappingTable_Object = MibTable
wsSecCryptoMapIfMappingTable = _WsSecCryptoMapIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 12)
)
if mibBuilder.loadTexts:
    wsSecCryptoMapIfMappingTable.setStatus("current")
_WsSecCryptoMapIfMappingEntry_Object = MibTableRow
wsSecCryptoMapIfMappingEntry = _WsSecCryptoMapIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 12, 1)
)
wsSecCryptoMapIfMappingEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecCryptoMapIfMappingCryptoMapName"),
)
if mibBuilder.loadTexts:
    wsSecCryptoMapIfMappingEntry.setStatus("current")
_WsSecCryptoMapIfMappingCryptoMapName_Type = DisplayString
_WsSecCryptoMapIfMappingCryptoMapName_Object = MibTableColumn
wsSecCryptoMapIfMappingCryptoMapName = _WsSecCryptoMapIfMappingCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 12, 1, 1),
    _WsSecCryptoMapIfMappingCryptoMapName_Type()
)
wsSecCryptoMapIfMappingCryptoMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecCryptoMapIfMappingCryptoMapName.setStatus("current")
_WsSecCryptoMapIfMappingIfName_Type = DisplayString
_WsSecCryptoMapIfMappingIfName_Object = MibTableColumn
wsSecCryptoMapIfMappingIfName = _WsSecCryptoMapIfMappingIfName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 12, 1, 2),
    _WsSecCryptoMapIfMappingIfName_Type()
)
wsSecCryptoMapIfMappingIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecCryptoMapIfMappingIfName.setStatus("current")
_WsSecRadiusSvrTable_Object = MibTable
wsSecRadiusSvrTable = _WsSecRadiusSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13)
)
if mibBuilder.loadTexts:
    wsSecRadiusSvrTable.setStatus("current")
_WsSecRadiusSvrEntry_Object = MibTableRow
wsSecRadiusSvrEntry = _WsSecRadiusSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1)
)
wsSecRadiusSvrEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecRadiusSvrIPAddr"),
)
if mibBuilder.loadTexts:
    wsSecRadiusSvrEntry.setStatus("current")
_WsSecRadiusSvrIPAddr_Type = IpAddress
_WsSecRadiusSvrIPAddr_Object = MibTableColumn
wsSecRadiusSvrIPAddr = _WsSecRadiusSvrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1, 1),
    _WsSecRadiusSvrIPAddr_Type()
)
wsSecRadiusSvrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecRadiusSvrIPAddr.setStatus("current")


class _WsSecRadiusSvrType_Type(Integer32):
    """Custom type wsSecRadiusSvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WsSecRadiusSvrType_Type.__name__ = "Integer32"
_WsSecRadiusSvrType_Object = MibTableColumn
wsSecRadiusSvrType = _WsSecRadiusSvrType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1, 2),
    _WsSecRadiusSvrType_Type()
)
wsSecRadiusSvrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecRadiusSvrType.setStatus("current")


class _WsSecRadiusSvrPort_Type(Unsigned32):
    """Custom type wsSecRadiusSvrPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_WsSecRadiusSvrPort_Type.__name__ = "Unsigned32"
_WsSecRadiusSvrPort_Object = MibTableColumn
wsSecRadiusSvrPort = _WsSecRadiusSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1, 3),
    _WsSecRadiusSvrPort_Type()
)
wsSecRadiusSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecRadiusSvrPort.setStatus("current")


class _WsSecRadiusSvrSharedSecret_Type(OctetString):
    """Custom type wsSecRadiusSvrSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsSecRadiusSvrSharedSecret_Type.__name__ = "OctetString"
_WsSecRadiusSvrSharedSecret_Object = MibTableColumn
wsSecRadiusSvrSharedSecret = _WsSecRadiusSvrSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1, 4),
    _WsSecRadiusSvrSharedSecret_Type()
)
wsSecRadiusSvrSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecRadiusSvrSharedSecret.setStatus("current")
_WsSecRadiusSvrRowStatus_Type = AbbrRowStatus
_WsSecRadiusSvrRowStatus_Object = MibTableColumn
wsSecRadiusSvrRowStatus = _WsSecRadiusSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 13, 1, 5),
    _WsSecRadiusSvrRowStatus_Type()
)
wsSecRadiusSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecRadiusSvrRowStatus.setStatus("current")
_WsSecRadiusSvrScalars_ObjectIdentity = ObjectIdentity
wsSecRadiusSvrScalars = _WsSecRadiusSvrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 14)
)


class _WsSecRadiusSvrNasIdentifier_Type(DisplayString):
    """Custom type wsSecRadiusSvrNasIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsSecRadiusSvrNasIdentifier_Type.__name__ = "DisplayString"
_WsSecRadiusSvrNasIdentifier_Object = MibScalar
wsSecRadiusSvrNasIdentifier = _WsSecRadiusSvrNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 14, 1),
    _WsSecRadiusSvrNasIdentifier_Type()
)
wsSecRadiusSvrNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecRadiusSvrNasIdentifier.setStatus("current")
_WsSecVpnUserTable_Object = MibTable
wsSecVpnUserTable = _WsSecVpnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 15)
)
if mibBuilder.loadTexts:
    wsSecVpnUserTable.setStatus("current")
_WsSecVpnUserEntry_Object = MibTableRow
wsSecVpnUserEntry = _WsSecVpnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 15, 1)
)
wsSecVpnUserEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecVpnUserName"),
)
if mibBuilder.loadTexts:
    wsSecVpnUserEntry.setStatus("current")


class _WsSecVpnUserName_Type(DisplayString):
    """Custom type wsSecVpnUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WsSecVpnUserName_Type.__name__ = "DisplayString"
_WsSecVpnUserName_Object = MibTableColumn
wsSecVpnUserName = _WsSecVpnUserName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 15, 1, 1),
    _WsSecVpnUserName_Type()
)
wsSecVpnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecVpnUserName.setStatus("current")


class _WsSecVpnUserPassword_Type(DisplayString):
    """Custom type wsSecVpnUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 21),
    )


_WsSecVpnUserPassword_Type.__name__ = "DisplayString"
_WsSecVpnUserPassword_Object = MibTableColumn
wsSecVpnUserPassword = _WsSecVpnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 15, 1, 2),
    _WsSecVpnUserPassword_Type()
)
wsSecVpnUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecVpnUserPassword.setStatus("current")
_WsSecVpnUserRowStatus_Type = AbbrRowStatus
_WsSecVpnUserRowStatus_Object = MibTableColumn
wsSecVpnUserRowStatus = _WsSecVpnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 15, 1, 3),
    _WsSecVpnUserRowStatus_Type()
)
wsSecVpnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsSecVpnUserRowStatus.setStatus("current")
_WsSecVpnAuth_ObjectIdentity = ObjectIdentity
wsSecVpnAuth = _WsSecVpnAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 16)
)


class _WsSecVPNAuthMethod_Type(Integer32):
    """Custom type wsSecVPNAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localUserTable", 2),
          ("none", 1),
          ("radiusSvr", 3))
    )


_WsSecVPNAuthMethod_Type.__name__ = "Integer32"
_WsSecVPNAuthMethod_Object = MibScalar
wsSecVPNAuthMethod = _WsSecVPNAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 16, 1),
    _WsSecVPNAuthMethod_Type()
)
wsSecVPNAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecVPNAuthMethod.setStatus("current")
_WsSecIKESaStatsClearScalars_ObjectIdentity = ObjectIdentity
wsSecIKESaStatsClearScalars = _WsSecIKESaStatsClearScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 17)
)
_WsSecIpSecClearPeerIpAddr_Type = DisplayString
_WsSecIpSecClearPeerIpAddr_Object = MibScalar
wsSecIpSecClearPeerIpAddr = _WsSecIpSecClearPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 17, 1),
    _WsSecIpSecClearPeerIpAddr_Type()
)
wsSecIpSecClearPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecIpSecClearPeerIpAddr.setStatus("current")


class _WsSecClearAction_Type(Integer32):
    """Custom type wsSecClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearIKESa", 2),
          ("clearIPSecSa", 1),
          ("clearIPSecSaAndIKESa", 3))
    )


_WsSecClearAction_Type.__name__ = "Integer32"
_WsSecClearAction_Object = MibScalar
wsSecClearAction = _WsSecClearAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 17, 2),
    _WsSecClearAction_Type()
)
wsSecClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsSecClearAction.setStatus("current")
_WsSecIPSecSaStatusTable_Object = MibTable
wsSecIPSecSaStatusTable = _WsSecIPSecSaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18)
)
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusTable.setStatus("current")
_WsSecIPSecSaStatusEntry_Object = MibTableRow
wsSecIPSecSaStatusEntry = _WsSecIPSecSaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1)
)
wsSecIPSecSaStatusEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecIPSecSaStatusIndex"),
)
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusEntry.setStatus("current")


class _WsSecIPSecSaStatusIndex_Type(Unsigned32):
    """Custom type wsSecIPSecSaStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsSecIPSecSaStatusIndex_Type.__name__ = "Unsigned32"
_WsSecIPSecSaStatusIndex_Object = MibTableColumn
wsSecIPSecSaStatusIndex = _WsSecIPSecSaStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 1),
    _WsSecIPSecSaStatusIndex_Type()
)
wsSecIPSecSaStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusIndex.setStatus("current")
_WsSecIPSecSaStatusLocalPeer_Type = DisplayString
_WsSecIPSecSaStatusLocalPeer_Object = MibTableColumn
wsSecIPSecSaStatusLocalPeer = _WsSecIPSecSaStatusLocalPeer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 2),
    _WsSecIPSecSaStatusLocalPeer_Type()
)
wsSecIPSecSaStatusLocalPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusLocalPeer.setStatus("current")
_WsSecIPSecSaStatusRemotePeer_Type = DisplayString
_WsSecIPSecSaStatusRemotePeer_Object = MibTableColumn
wsSecIPSecSaStatusRemotePeer = _WsSecIPSecSaStatusRemotePeer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 3),
    _WsSecIPSecSaStatusRemotePeer_Type()
)
wsSecIPSecSaStatusRemotePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusRemotePeer.setStatus("current")
_WsSecIPSecSaStatusEspSpiIn_Type = Unsigned32
_WsSecIPSecSaStatusEspSpiIn_Object = MibTableColumn
wsSecIPSecSaStatusEspSpiIn = _WsSecIPSecSaStatusEspSpiIn_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 4),
    _WsSecIPSecSaStatusEspSpiIn_Type()
)
wsSecIPSecSaStatusEspSpiIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusEspSpiIn.setStatus("current")
_WsSecIPSecSaStatusEspSpiOut_Type = Unsigned32
_WsSecIPSecSaStatusEspSpiOut_Object = MibTableColumn
wsSecIPSecSaStatusEspSpiOut = _WsSecIPSecSaStatusEspSpiOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 5),
    _WsSecIPSecSaStatusEspSpiOut_Type()
)
wsSecIPSecSaStatusEspSpiOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusEspSpiOut.setStatus("current")
_WsSecIPSecSaStatusAhSpiIn_Type = Unsigned32
_WsSecIPSecSaStatusAhSpiIn_Object = MibTableColumn
wsSecIPSecSaStatusAhSpiIn = _WsSecIPSecSaStatusAhSpiIn_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 6),
    _WsSecIPSecSaStatusAhSpiIn_Type()
)
wsSecIPSecSaStatusAhSpiIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusAhSpiIn.setStatus("current")
_WsSecIPSecSaStatusAhSpiOut_Type = Unsigned32
_WsSecIPSecSaStatusAhSpiOut_Object = MibTableColumn
wsSecIPSecSaStatusAhSpiOut = _WsSecIPSecSaStatusAhSpiOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 7),
    _WsSecIPSecSaStatusAhSpiOut_Type()
)
wsSecIPSecSaStatusAhSpiOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusAhSpiOut.setStatus("current")
_WsSecIPSecSaStatusAlgthmCipher_Type = DisplayString
_WsSecIPSecSaStatusAlgthmCipher_Object = MibTableColumn
wsSecIPSecSaStatusAlgthmCipher = _WsSecIPSecSaStatusAlgthmCipher_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 8),
    _WsSecIPSecSaStatusAlgthmCipher_Type()
)
wsSecIPSecSaStatusAlgthmCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusAlgthmCipher.setStatus("current")
_WsSecIPSecSaStatusAlgthmMac_Type = DisplayString
_WsSecIPSecSaStatusAlgthmMac_Object = MibTableColumn
wsSecIPSecSaStatusAlgthmMac = _WsSecIPSecSaStatusAlgthmMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 18, 1, 9),
    _WsSecIPSecSaStatusAlgthmMac_Type()
)
wsSecIPSecSaStatusAlgthmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIPSecSaStatusAlgthmMac.setStatus("current")
_WsSecIKESaStatsTable_Object = MibTable
wsSecIKESaStatsTable = _WsSecIKESaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19)
)
if mibBuilder.loadTexts:
    wsSecIKESaStatsTable.setStatus("current")
_WsSecIKESaStatsEntry_Object = MibTableRow
wsSecIKESaStatsEntry = _WsSecIKESaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1)
)
wsSecIKESaStatsEntry.setIndexNames(
    (0, "WS-SEC-VPN-MIB", "wsSecIKESaStatIndex"),
)
if mibBuilder.loadTexts:
    wsSecIKESaStatsEntry.setStatus("current")


class _WsSecIKESaStatIndex_Type(Unsigned32):
    """Custom type wsSecIKESaStatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsSecIKESaStatIndex_Type.__name__ = "Unsigned32"
_WsSecIKESaStatIndex_Object = MibTableColumn
wsSecIKESaStatIndex = _WsSecIKESaStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 1),
    _WsSecIKESaStatIndex_Type()
)
wsSecIKESaStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatIndex.setStatus("current")
_WsSecIKESaStatsPhase1Done_Type = TruthValue
_WsSecIKESaStatsPhase1Done_Object = MibTableColumn
wsSecIKESaStatsPhase1Done = _WsSecIKESaStatsPhase1Done_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 2),
    _WsSecIKESaStatsPhase1Done_Type()
)
wsSecIKESaStatsPhase1Done.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsPhase1Done.setStatus("current")
_WsSecIKESaStatsNumOfNegotions_Type = Unsigned32
_WsSecIKESaStatsNumOfNegotions_Object = MibTableColumn
wsSecIKESaStatsNumOfNegotions = _WsSecIKESaStatsNumOfNegotions_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 3),
    _WsSecIKESaStatsNumOfNegotions_Type()
)
wsSecIKESaStatsNumOfNegotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsNumOfNegotions.setStatus("current")
_WsSecIKESaStatsNumOfBytes_Type = Unsigned32
_WsSecIKESaStatsNumOfBytes_Object = MibTableColumn
wsSecIKESaStatsNumOfBytes = _WsSecIKESaStatsNumOfBytes_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 4),
    _WsSecIKESaStatsNumOfBytes_Type()
)
wsSecIKESaStatsNumOfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsNumOfBytes.setStatus("current")
_WsSecIKESaStatsCreateDate_Type = DateAndTime
_WsSecIKESaStatsCreateDate_Object = MibTableColumn
wsSecIKESaStatsCreateDate = _WsSecIKESaStatsCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 5),
    _WsSecIKESaStatsCreateDate_Type()
)
wsSecIKESaStatsCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsCreateDate.setStatus("current")
_WsSecIKESaStatsEncrptAlgthm_Type = DisplayString
_WsSecIKESaStatsEncrptAlgthm_Object = MibTableColumn
wsSecIKESaStatsEncrptAlgthm = _WsSecIKESaStatsEncrptAlgthm_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 6),
    _WsSecIKESaStatsEncrptAlgthm_Type()
)
wsSecIKESaStatsEncrptAlgthm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsEncrptAlgthm.setStatus("current")
_WsSecIKESaStatsHashAlgthm_Type = DisplayString
_WsSecIKESaStatsHashAlgthm_Object = MibTableColumn
wsSecIKESaStatsHashAlgthm = _WsSecIKESaStatsHashAlgthm_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 7),
    _WsSecIKESaStatsHashAlgthm_Type()
)
wsSecIKESaStatsHashAlgthm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsHashAlgthm.setStatus("current")
_WsSecIKESaStatsPrfAlgthm_Type = DisplayString
_WsSecIKESaStatsPrfAlgthm_Object = MibTableColumn
wsSecIKESaStatsPrfAlgthm = _WsSecIKESaStatsPrfAlgthm_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 8),
    _WsSecIKESaStatsPrfAlgthm_Type()
)
wsSecIKESaStatsPrfAlgthm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsPrfAlgthm.setStatus("current")
_WsSecIKESaStatsLocalIdentity_Type = DisplayString
_WsSecIKESaStatsLocalIdentity_Object = MibTableColumn
wsSecIKESaStatsLocalIdentity = _WsSecIKESaStatsLocalIdentity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 9),
    _WsSecIKESaStatsLocalIdentity_Type()
)
wsSecIKESaStatsLocalIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsLocalIdentity.setStatus("current")
_WsSecIKESaStatsRemoteIdentity_Type = DisplayString
_WsSecIKESaStatsRemoteIdentity_Object = MibTableColumn
wsSecIKESaStatsRemoteIdentity = _WsSecIKESaStatsRemoteIdentity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 19, 1, 10),
    _WsSecIKESaStatsRemoteIdentity_Type()
)
wsSecIKESaStatsRemoteIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecIKESaStatsRemoteIdentity.setStatus("current")
_WsSecVPNScalars_ObjectIdentity = ObjectIdentity
wsSecVPNScalars = _WsSecVPNScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 20)
)
_WsSecVPNSetError_Type = DisplayString
_WsSecVPNSetError_Object = MibScalar
wsSecVPNSetError = _WsSecVPNSetError_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 20, 1),
    _WsSecVPNSetError_Type()
)
wsSecVPNSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSecVPNSetError.setStatus("current")
_WsSecVpnConformance_ObjectIdentity = ObjectIdentity
wsSecVpnConformance = _WsSecVpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 21)
)
_WsSecVpnCompliances_ObjectIdentity = ObjectIdentity
wsSecVpnCompliances = _WsSecVpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 21, 1)
)
_WsSecVpnGroups_ObjectIdentity = ObjectIdentity
wsSecVpnGroups = _WsSecVpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 22)
)

# Managed Objects groups

wsSecVpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 23)
)
wsSecVpnGroup.setObjects(
      *(("WS-SEC-VPN-MIB", "wsSecIKEPolicyRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecIKEKeepAlive"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetName"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetMode"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetEspEncr"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetEspAuth"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecVpnSALifeTimeSec"),
        ("WS-SEC-VPN-MIB", "wsSecVpnSALifeTimeKB"),
        ("WS-SEC-VPN-MIB", "wsSecClientDNSServerIP"),
        ("WS-SEC-VPN-MIB", "wsSecClientWinServerIP"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapSequenceNum"),
        ("WS-SEC-VPN-MIB", "wsSecPreSharedKeyRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecTransformSetAHAuth"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapACLId"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapPFS"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapSAPerHostEnable"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapPeerRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaCryptoMapSeqNum"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaCryptoMapName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaIKEPeer"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaAclId"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaInAhSpi"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaOutAhSpi"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaInEspSpi"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaOutEspSpi"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrIPAddr"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrType"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrPort"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrSharedSecret"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecVpnUserName"),
        ("WS-SEC-VPN-MIB", "wsSecVpnUserPassword"),
        ("WS-SEC-VPN-MIB", "wsSecVpnUserRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecClearAction"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusIndex"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusLocalPeer"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusRemotePeer"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusEspSpiOut"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusAhSpiIn"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusAhSpiOut"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusAlgthmCipher"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusAlgthmMac"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatIndex"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsNumOfNegotions"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsNumOfBytes"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsCreateDate"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsEncrptAlgthm"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsHashAlgthm"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsPrfAlgthm"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsLocalIdentity"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsRemoteIdentity"),
        ("WS-SEC-VPN-MIB", "wsSecIKESaStatsPhase1Done"),
        ("WS-SEC-VPN-MIB", "wsSecVPNAuthMethod"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaTSName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapModeCfgEnable"),
        ("WS-SEC-VPN-MIB", "wsSecVPNSetError"),
        ("WS-SEC-VPN-MIB", "wsSecRadiusSvrNasIdentifier"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicySaLifeTimeSec"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicyDHGroup"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicyAuthType"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicyHash"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicyEncryption"),
        ("WS-SEC-VPN-MIB", "wsSecIKEPolicyPriority"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapIfMappingCryptoMapName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapIfMappingIfName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapTransformSetRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapTransformSetName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapTransformSetCryptoMapName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapPeerIKEPeer"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapPeerName"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapPeerSequenceNum"),
        ("WS-SEC-VPN-MIB", "wsSecLocalIPAddrPoolRowStatus"),
        ("WS-SEC-VPN-MIB", "wsSecLocalIPAddrPoolAddrRangeEnd"),
        ("WS-SEC-VPN-MIB", "wsSecLocalIPAddrPoolAddrRangeStart"),
        ("WS-SEC-VPN-MIB", "wsSecPreSharedKeyIKEAggressive"),
        ("WS-SEC-VPN-MIB", "wsSecPreSharedKeyIKEPeerKey"),
        ("WS-SEC-VPN-MIB", "wsSecPreSharedKeyIKEPeerIdentity"),
        ("WS-SEC-VPN-MIB", "wsSecPreSharedKeyIKEPeer"),
        ("WS-SEC-VPN-MIB", "wsSecISAKMPLocalIdentity"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapTransformCryptoMapSetSeqNum"),
        ("WS-SEC-VPN-MIB", "wsSecIPSecSaStatusEspSpiIn"),
        ("WS-SEC-VPN-MIB", "wsSecIpSecClearPeerIpAddr"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaAhOrEsp"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaOutEspCipherKey"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaInEspCipherKey"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaOutAuthKey"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapSALifeTimeSec"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapSALifeTimeKB"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapManualSaInAuthKey"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapMode"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapRemoteType"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapLocalIdType"),
        ("WS-SEC-VPN-MIB", "wsSecCryptoMapLocalId"))
)
if mibBuilder.loadTexts:
    wsSecVpnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsSecVpnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 6, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    wsSecVpnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-SEC-VPN-MIB",
    **{"AbbrRowStatus": AbbrRowStatus,
       "wsSecVpnMib": wsSecVpnMib,
       "wsSecIKEScalars": wsSecIKEScalars,
       "wsSecIKEKeepAlive": wsSecIKEKeepAlive,
       "wsSecISAKMPLocalIdentity": wsSecISAKMPLocalIdentity,
       "wsSecIKEPolicyTable": wsSecIKEPolicyTable,
       "wsSecIKEPolicyEntry": wsSecIKEPolicyEntry,
       "wsSecIKEPolicyPriority": wsSecIKEPolicyPriority,
       "wsSecIKEPolicyEncryption": wsSecIKEPolicyEncryption,
       "wsSecIKEPolicyHash": wsSecIKEPolicyHash,
       "wsSecIKEPolicyAuthType": wsSecIKEPolicyAuthType,
       "wsSecIKEPolicyDHGroup": wsSecIKEPolicyDHGroup,
       "wsSecIKEPolicySaLifeTimeSec": wsSecIKEPolicySaLifeTimeSec,
       "wsSecIKEPolicyRowStatus": wsSecIKEPolicyRowStatus,
       "wsSecPreSharedKeyTable": wsSecPreSharedKeyTable,
       "wsSecPreSharedKeyEntry": wsSecPreSharedKeyEntry,
       "wsSecPreSharedKeyIKEPeer": wsSecPreSharedKeyIKEPeer,
       "wsSecPreSharedKeyIKEPeerIdentity": wsSecPreSharedKeyIKEPeerIdentity,
       "wsSecPreSharedKeyIKEPeerKey": wsSecPreSharedKeyIKEPeerKey,
       "wsSecPreSharedKeyIKEAggressive": wsSecPreSharedKeyIKEAggressive,
       "wsSecPreSharedKeyRowStatus": wsSecPreSharedKeyRowStatus,
       "wsSecTransformSetTable": wsSecTransformSetTable,
       "wsSecTransformSetEntry": wsSecTransformSetEntry,
       "wsSecTransformSetName": wsSecTransformSetName,
       "wsSecTransformSetMode": wsSecTransformSetMode,
       "wsSecTransformSetAHAuth": wsSecTransformSetAHAuth,
       "wsSecTransformSetEspEncr": wsSecTransformSetEspEncr,
       "wsSecTransformSetEspAuth": wsSecTransformSetEspAuth,
       "wsSecTransformSetRowStatus": wsSecTransformSetRowStatus,
       "wsSecIPSecCfgScalars": wsSecIPSecCfgScalars,
       "wsSecVpnSALifeTimeSec": wsSecVpnSALifeTimeSec,
       "wsSecVpnSALifeTimeKB": wsSecVpnSALifeTimeKB,
       "wsSecLocalIPAddrPoolTable": wsSecLocalIPAddrPoolTable,
       "wsSecLocalIPAddrPoolEntry": wsSecLocalIPAddrPoolEntry,
       "wsSecLocalIPAddrPoolAddrRangeStart": wsSecLocalIPAddrPoolAddrRangeStart,
       "wsSecLocalIPAddrPoolAddrRangeEnd": wsSecLocalIPAddrPoolAddrRangeEnd,
       "wsSecLocalIPAddrPoolRowStatus": wsSecLocalIPAddrPoolRowStatus,
       "wsSecLocalIPAddressPoolScalars": wsSecLocalIPAddressPoolScalars,
       "wsSecClientDNSServerIP": wsSecClientDNSServerIP,
       "wsSecClientWinServerIP": wsSecClientWinServerIP,
       "wsSecCryptoMapTable": wsSecCryptoMapTable,
       "wsSecCryptoMapEntry": wsSecCryptoMapEntry,
       "wsSecCryptoMapSequenceNum": wsSecCryptoMapSequenceNum,
       "wsSecCryptoMapName": wsSecCryptoMapName,
       "wsSecCryptoMapACLId": wsSecCryptoMapACLId,
       "wsSecCryptoMapSALifeTimeSec": wsSecCryptoMapSALifeTimeSec,
       "wsSecCryptoMapSALifeTimeKB": wsSecCryptoMapSALifeTimeKB,
       "wsSecCryptoMapPFS": wsSecCryptoMapPFS,
       "wsSecCryptoMapSAPerHostEnable": wsSecCryptoMapSAPerHostEnable,
       "wsSecCryptoMapModeCfgEnable": wsSecCryptoMapModeCfgEnable,
       "wsSecCryptoMapLocalId": wsSecCryptoMapLocalId,
       "wsSecCryptoMapLocalIdType": wsSecCryptoMapLocalIdType,
       "wsSecCryptoMapMode": wsSecCryptoMapMode,
       "wsSecCryptoMapRemoteType": wsSecCryptoMapRemoteType,
       "wsSecCryptoMapRowStatus": wsSecCryptoMapRowStatus,
       "wsSecCryptoMapPeerTable": wsSecCryptoMapPeerTable,
       "wsSecCryptoMapPeerEntry": wsSecCryptoMapPeerEntry,
       "wsSecCryptoMapPeerSequenceNum": wsSecCryptoMapPeerSequenceNum,
       "wsSecCryptoMapPeerName": wsSecCryptoMapPeerName,
       "wsSecCryptoMapPeerIKEPeer": wsSecCryptoMapPeerIKEPeer,
       "wsSecCryptoMapPeerRowStatus": wsSecCryptoMapPeerRowStatus,
       "wsSecCryptoMapManualSaTable": wsSecCryptoMapManualSaTable,
       "wsSecCryptoMapManualSaEntry": wsSecCryptoMapManualSaEntry,
       "wsSecCryptoMapManualSaCryptoMapSeqNum": wsSecCryptoMapManualSaCryptoMapSeqNum,
       "wsSecCryptoMapManualSaCryptoMapName": wsSecCryptoMapManualSaCryptoMapName,
       "wsSecCryptoMapManualSaIKEPeer": wsSecCryptoMapManualSaIKEPeer,
       "wsSecCryptoMapManualSaAclId": wsSecCryptoMapManualSaAclId,
       "wsSecCryptoMapManualSaInAhSpi": wsSecCryptoMapManualSaInAhSpi,
       "wsSecCryptoMapManualSaInAuthKey": wsSecCryptoMapManualSaInAuthKey,
       "wsSecCryptoMapManualSaOutAhSpi": wsSecCryptoMapManualSaOutAhSpi,
       "wsSecCryptoMapManualSaOutAuthKey": wsSecCryptoMapManualSaOutAuthKey,
       "wsSecCryptoMapManualSaInEspSpi": wsSecCryptoMapManualSaInEspSpi,
       "wsSecCryptoMapManualSaInEspCipherKey": wsSecCryptoMapManualSaInEspCipherKey,
       "wsSecCryptoMapManualSaOutEspSpi": wsSecCryptoMapManualSaOutEspSpi,
       "wsSecCryptoMapManualSaOutEspCipherKey": wsSecCryptoMapManualSaOutEspCipherKey,
       "wsSecCryptoMapManualSaTSName": wsSecCryptoMapManualSaTSName,
       "wsSecCryptoMapManualSaAhOrEsp": wsSecCryptoMapManualSaAhOrEsp,
       "wsSecCryptoMapManualSaRowStatus": wsSecCryptoMapManualSaRowStatus,
       "wsSecCryptoMapTransformSetTable": wsSecCryptoMapTransformSetTable,
       "wsSecCryptoMapTransformSetEntry": wsSecCryptoMapTransformSetEntry,
       "wsSecCryptoMapTransformCryptoMapSetSeqNum": wsSecCryptoMapTransformCryptoMapSetSeqNum,
       "wsSecCryptoMapTransformSetCryptoMapName": wsSecCryptoMapTransformSetCryptoMapName,
       "wsSecCryptoMapTransformSetName": wsSecCryptoMapTransformSetName,
       "wsSecCryptoMapTransformSetRowStatus": wsSecCryptoMapTransformSetRowStatus,
       "wsSecCryptoMapIfMappingTable": wsSecCryptoMapIfMappingTable,
       "wsSecCryptoMapIfMappingEntry": wsSecCryptoMapIfMappingEntry,
       "wsSecCryptoMapIfMappingCryptoMapName": wsSecCryptoMapIfMappingCryptoMapName,
       "wsSecCryptoMapIfMappingIfName": wsSecCryptoMapIfMappingIfName,
       "wsSecRadiusSvrTable": wsSecRadiusSvrTable,
       "wsSecRadiusSvrEntry": wsSecRadiusSvrEntry,
       "wsSecRadiusSvrIPAddr": wsSecRadiusSvrIPAddr,
       "wsSecRadiusSvrType": wsSecRadiusSvrType,
       "wsSecRadiusSvrPort": wsSecRadiusSvrPort,
       "wsSecRadiusSvrSharedSecret": wsSecRadiusSvrSharedSecret,
       "wsSecRadiusSvrRowStatus": wsSecRadiusSvrRowStatus,
       "wsSecRadiusSvrScalars": wsSecRadiusSvrScalars,
       "wsSecRadiusSvrNasIdentifier": wsSecRadiusSvrNasIdentifier,
       "wsSecVpnUserTable": wsSecVpnUserTable,
       "wsSecVpnUserEntry": wsSecVpnUserEntry,
       "wsSecVpnUserName": wsSecVpnUserName,
       "wsSecVpnUserPassword": wsSecVpnUserPassword,
       "wsSecVpnUserRowStatus": wsSecVpnUserRowStatus,
       "wsSecVpnAuth": wsSecVpnAuth,
       "wsSecVPNAuthMethod": wsSecVPNAuthMethod,
       "wsSecIKESaStatsClearScalars": wsSecIKESaStatsClearScalars,
       "wsSecIpSecClearPeerIpAddr": wsSecIpSecClearPeerIpAddr,
       "wsSecClearAction": wsSecClearAction,
       "wsSecIPSecSaStatusTable": wsSecIPSecSaStatusTable,
       "wsSecIPSecSaStatusEntry": wsSecIPSecSaStatusEntry,
       "wsSecIPSecSaStatusIndex": wsSecIPSecSaStatusIndex,
       "wsSecIPSecSaStatusLocalPeer": wsSecIPSecSaStatusLocalPeer,
       "wsSecIPSecSaStatusRemotePeer": wsSecIPSecSaStatusRemotePeer,
       "wsSecIPSecSaStatusEspSpiIn": wsSecIPSecSaStatusEspSpiIn,
       "wsSecIPSecSaStatusEspSpiOut": wsSecIPSecSaStatusEspSpiOut,
       "wsSecIPSecSaStatusAhSpiIn": wsSecIPSecSaStatusAhSpiIn,
       "wsSecIPSecSaStatusAhSpiOut": wsSecIPSecSaStatusAhSpiOut,
       "wsSecIPSecSaStatusAlgthmCipher": wsSecIPSecSaStatusAlgthmCipher,
       "wsSecIPSecSaStatusAlgthmMac": wsSecIPSecSaStatusAlgthmMac,
       "wsSecIKESaStatsTable": wsSecIKESaStatsTable,
       "wsSecIKESaStatsEntry": wsSecIKESaStatsEntry,
       "wsSecIKESaStatIndex": wsSecIKESaStatIndex,
       "wsSecIKESaStatsPhase1Done": wsSecIKESaStatsPhase1Done,
       "wsSecIKESaStatsNumOfNegotions": wsSecIKESaStatsNumOfNegotions,
       "wsSecIKESaStatsNumOfBytes": wsSecIKESaStatsNumOfBytes,
       "wsSecIKESaStatsCreateDate": wsSecIKESaStatsCreateDate,
       "wsSecIKESaStatsEncrptAlgthm": wsSecIKESaStatsEncrptAlgthm,
       "wsSecIKESaStatsHashAlgthm": wsSecIKESaStatsHashAlgthm,
       "wsSecIKESaStatsPrfAlgthm": wsSecIKESaStatsPrfAlgthm,
       "wsSecIKESaStatsLocalIdentity": wsSecIKESaStatsLocalIdentity,
       "wsSecIKESaStatsRemoteIdentity": wsSecIKESaStatsRemoteIdentity,
       "wsSecVPNScalars": wsSecVPNScalars,
       "wsSecVPNSetError": wsSecVPNSetError,
       "wsSecVpnConformance": wsSecVpnConformance,
       "wsSecVpnCompliances": wsSecVpnCompliances,
       "wsSecVpnCompliance": wsSecVpnCompliance,
       "wsSecVpnGroups": wsSecVpnGroups,
       "wsSecVpnGroup": wsSecVpnGroup}
)
