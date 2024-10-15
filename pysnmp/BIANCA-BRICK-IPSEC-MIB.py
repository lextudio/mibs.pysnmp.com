# SNMP MIB module (BIANCA-BRICK-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:30 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26)
)
_IpsecGlobals_ObjectIdentity = ObjectIdentity
ipsecGlobals = _IpsecGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1)
)
_IpsecGlobPeerIndex_Type = Integer32
_IpsecGlobPeerIndex_Object = MibScalar
ipsecGlobPeerIndex = _IpsecGlobPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 1),
    _IpsecGlobPeerIndex_Type()
)
ipsecGlobPeerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobPeerIndex.setStatus("mandatory")


class _IpsecGlobDefaultAuthMethod_Type(Integer32):
    """Custom type ipsecGlobDefaultAuthMethod based on Integer32"""
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
        *(("dss-sig", 2),
          ("pre-sh-key", 1),
          ("rsa-enc", 4),
          ("rsa-sig", 3))
    )


_IpsecGlobDefaultAuthMethod_Type.__name__ = "Integer32"
_IpsecGlobDefaultAuthMethod_Object = MibScalar
ipsecGlobDefaultAuthMethod = _IpsecGlobDefaultAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 2),
    _IpsecGlobDefaultAuthMethod_Type()
)
ipsecGlobDefaultAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultAuthMethod.setStatus("mandatory")
_IpsecGlobDefaultCertificate_Type = Integer32
_IpsecGlobDefaultCertificate_Object = MibScalar
ipsecGlobDefaultCertificate = _IpsecGlobDefaultCertificate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 3),
    _IpsecGlobDefaultCertificate_Type()
)
ipsecGlobDefaultCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultCertificate.setStatus("mandatory")
_IpsecGlobDefaultLocalId_Type = DisplayString
_IpsecGlobDefaultLocalId_Object = MibScalar
ipsecGlobDefaultLocalId = _IpsecGlobDefaultLocalId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 4),
    _IpsecGlobDefaultLocalId_Type()
)
ipsecGlobDefaultLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultLocalId.setStatus("mandatory")
_IpsecGlobDefaultIpsecProposal_Type = Integer32
_IpsecGlobDefaultIpsecProposal_Object = MibScalar
ipsecGlobDefaultIpsecProposal = _IpsecGlobDefaultIpsecProposal_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 5),
    _IpsecGlobDefaultIpsecProposal_Type()
)
ipsecGlobDefaultIpsecProposal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultIpsecProposal.setStatus("mandatory")
_IpsecGlobDefaultIkeProposal_Type = Integer32
_IpsecGlobDefaultIkeProposal_Object = MibScalar
ipsecGlobDefaultIkeProposal = _IpsecGlobDefaultIkeProposal_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 6),
    _IpsecGlobDefaultIkeProposal_Type()
)
ipsecGlobDefaultIkeProposal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultIkeProposal.setStatus("mandatory")
_IpsecGlobDefaultIpsecLifeTime_Type = Integer32
_IpsecGlobDefaultIpsecLifeTime_Object = MibScalar
ipsecGlobDefaultIpsecLifeTime = _IpsecGlobDefaultIpsecLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 7),
    _IpsecGlobDefaultIpsecLifeTime_Type()
)
ipsecGlobDefaultIpsecLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultIpsecLifeTime.setStatus("mandatory")
_IpsecGlobDefaultIkeLifeTime_Type = Integer32
_IpsecGlobDefaultIkeLifeTime_Object = MibScalar
ipsecGlobDefaultIkeLifeTime = _IpsecGlobDefaultIkeLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 8),
    _IpsecGlobDefaultIkeLifeTime_Type()
)
ipsecGlobDefaultIkeLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultIkeLifeTime.setStatus("mandatory")
_IpsecGlobDefaultIkeGroup_Type = Integer32
_IpsecGlobDefaultIkeGroup_Object = MibScalar
ipsecGlobDefaultIkeGroup = _IpsecGlobDefaultIkeGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 9),
    _IpsecGlobDefaultIkeGroup_Type()
)
ipsecGlobDefaultIkeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultIkeGroup.setStatus("mandatory")


class _IpsecGlobMaxSysLogLevel_Type(Integer32):
    """Custom type ipsecGlobMaxSysLogLevel based on Integer32"""
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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_IpsecGlobMaxSysLogLevel_Type.__name__ = "Integer32"
_IpsecGlobMaxSysLogLevel_Object = MibScalar
ipsecGlobMaxSysLogLevel = _IpsecGlobMaxSysLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 10),
    _IpsecGlobMaxSysLogLevel_Type()
)
ipsecGlobMaxSysLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobMaxSysLogLevel.setStatus("mandatory")


class _IpsecGlobDefaultGranularity_Type(Integer32):
    """Custom type ipsecGlobDefaultGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("coarse", 2),
          ("ip", 3),
          ("port", 5),
          ("proto", 4))
    )


_IpsecGlobDefaultGranularity_Type.__name__ = "Integer32"
_IpsecGlobDefaultGranularity_Object = MibScalar
ipsecGlobDefaultGranularity = _IpsecGlobDefaultGranularity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 11),
    _IpsecGlobDefaultGranularity_Type()
)
ipsecGlobDefaultGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultGranularity.setStatus("mandatory")


class _IpsecGlobDefaultPh1Mode_Type(Integer32):
    """Custom type ipsecGlobDefaultPh1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("id-protect", 1))
    )


_IpsecGlobDefaultPh1Mode_Type.__name__ = "Integer32"
_IpsecGlobDefaultPh1Mode_Object = MibScalar
ipsecGlobDefaultPh1Mode = _IpsecGlobDefaultPh1Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 12),
    _IpsecGlobDefaultPh1Mode_Type()
)
ipsecGlobDefaultPh1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultPh1Mode.setStatus("mandatory")
_IpsecGlobDefaultPfsGroup_Type = Integer32
_IpsecGlobDefaultPfsGroup_Object = MibScalar
ipsecGlobDefaultPfsGroup = _IpsecGlobDefaultPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 13),
    _IpsecGlobDefaultPfsGroup_Type()
)
ipsecGlobDefaultPfsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobDefaultPfsGroup.setStatus("mandatory")
_IpsecGlobIkePort_Type = Integer32
_IpsecGlobIkePort_Object = MibScalar
ipsecGlobIkePort = _IpsecGlobIkePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 20),
    _IpsecGlobIkePort_Type()
)
ipsecGlobIkePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobIkePort.setStatus("mandatory")
_IpsecGlobMaxRetries_Type = Integer32
_IpsecGlobMaxRetries_Object = MibScalar
ipsecGlobMaxRetries = _IpsecGlobMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 21),
    _IpsecGlobMaxRetries_Type()
)
ipsecGlobMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobMaxRetries.setStatus("mandatory")
_IpsecGlobRetryTimeout0milli_Type = Integer32
_IpsecGlobRetryTimeout0milli_Object = MibScalar
ipsecGlobRetryTimeout0milli = _IpsecGlobRetryTimeout0milli_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 22),
    _IpsecGlobRetryTimeout0milli_Type()
)
ipsecGlobRetryTimeout0milli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobRetryTimeout0milli.setStatus("mandatory")
_IpsecGlobRetryTimeoutMaxsec_Type = Integer32
_IpsecGlobRetryTimeoutMaxsec_Object = MibScalar
ipsecGlobRetryTimeoutMaxsec = _IpsecGlobRetryTimeoutMaxsec_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 23),
    _IpsecGlobRetryTimeoutMaxsec_Type()
)
ipsecGlobRetryTimeoutMaxsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobRetryTimeoutMaxsec.setStatus("mandatory")
_IpsecGlobMaxNegotiationTimeoutsec_Type = Integer32
_IpsecGlobMaxNegotiationTimeoutsec_Object = MibScalar
ipsecGlobMaxNegotiationTimeoutsec = _IpsecGlobMaxNegotiationTimeoutsec_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 24),
    _IpsecGlobMaxNegotiationTimeoutsec_Type()
)
ipsecGlobMaxNegotiationTimeoutsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobMaxNegotiationTimeoutsec.setStatus("mandatory")
_IpsecGlobMaxIkeSas_Type = Integer32
_IpsecGlobMaxIkeSas_Object = MibScalar
ipsecGlobMaxIkeSas = _IpsecGlobMaxIkeSas_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 25),
    _IpsecGlobMaxIkeSas_Type()
)
ipsecGlobMaxIkeSas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobMaxIkeSas.setStatus("mandatory")
_IpsecGlobAntiCloggingLength_Type = Integer32
_IpsecGlobAntiCloggingLength_Object = MibScalar
ipsecGlobAntiCloggingLength = _IpsecGlobAntiCloggingLength_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 26),
    _IpsecGlobAntiCloggingLength_Type()
)
ipsecGlobAntiCloggingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobAntiCloggingLength.setStatus("mandatory")


class _IpsecGlobAntiCloggingHash_Type(Integer32):
    """Custom type ipsecGlobAntiCloggingHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("sha1", 4))
    )


_IpsecGlobAntiCloggingHash_Type.__name__ = "Integer32"
_IpsecGlobAntiCloggingHash_Object = MibScalar
ipsecGlobAntiCloggingHash = _IpsecGlobAntiCloggingHash_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 27),
    _IpsecGlobAntiCloggingHash_Type()
)
ipsecGlobAntiCloggingHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobAntiCloggingHash.setStatus("mandatory")
_IpsecGlobLocalSecretPeriodsec_Type = Integer32
_IpsecGlobLocalSecretPeriodsec_Object = MibScalar
ipsecGlobLocalSecretPeriodsec = _IpsecGlobLocalSecretPeriodsec_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 28),
    _IpsecGlobLocalSecretPeriodsec_Type()
)
ipsecGlobLocalSecretPeriodsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobLocalSecretPeriodsec.setStatus("mandatory")


class _IpsecGlobIgnoreCrPayloads_Type(Integer32):
    """Custom type ipsecGlobIgnoreCrPayloads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobIgnoreCrPayloads_Type.__name__ = "Integer32"
_IpsecGlobIgnoreCrPayloads_Object = MibScalar
ipsecGlobIgnoreCrPayloads = _IpsecGlobIgnoreCrPayloads_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 29),
    _IpsecGlobIgnoreCrPayloads_Type()
)
ipsecGlobIgnoreCrPayloads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobIgnoreCrPayloads.setStatus("mandatory")


class _IpsecGlobNoCrPayloads_Type(Integer32):
    """Custom type ipsecGlobNoCrPayloads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobNoCrPayloads_Type.__name__ = "Integer32"
_IpsecGlobNoCrPayloads_Object = MibScalar
ipsecGlobNoCrPayloads = _IpsecGlobNoCrPayloads_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 30),
    _IpsecGlobNoCrPayloads_Type()
)
ipsecGlobNoCrPayloads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobNoCrPayloads.setStatus("mandatory")


class _IpsecGlobNoKeyHashPayloads_Type(Integer32):
    """Custom type ipsecGlobNoKeyHashPayloads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobNoKeyHashPayloads_Type.__name__ = "Integer32"
_IpsecGlobNoKeyHashPayloads_Object = MibScalar
ipsecGlobNoKeyHashPayloads = _IpsecGlobNoKeyHashPayloads_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 31),
    _IpsecGlobNoKeyHashPayloads_Type()
)
ipsecGlobNoKeyHashPayloads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobNoKeyHashPayloads.setStatus("mandatory")


class _IpsecGlobNoCrls_Type(Integer32):
    """Custom type ipsecGlobNoCrls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobNoCrls_Type.__name__ = "Integer32"
_IpsecGlobNoCrls_Object = MibScalar
ipsecGlobNoCrls = _IpsecGlobNoCrls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 32),
    _IpsecGlobNoCrls_Type()
)
ipsecGlobNoCrls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobNoCrls.setStatus("mandatory")


class _IpsecGlobSendFullCertChains_Type(Integer32):
    """Custom type ipsecGlobSendFullCertChains based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobSendFullCertChains_Type.__name__ = "Integer32"
_IpsecGlobSendFullCertChains_Object = MibScalar
ipsecGlobSendFullCertChains = _IpsecGlobSendFullCertChains_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 33),
    _IpsecGlobSendFullCertChains_Type()
)
ipsecGlobSendFullCertChains.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobSendFullCertChains.setStatus("mandatory")


class _IpsecGlobTrustIcmpMsg_Type(Integer32):
    """Custom type ipsecGlobTrustIcmpMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobTrustIcmpMsg_Type.__name__ = "Integer32"
_IpsecGlobTrustIcmpMsg_Object = MibScalar
ipsecGlobTrustIcmpMsg = _IpsecGlobTrustIcmpMsg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 34),
    _IpsecGlobTrustIcmpMsg_Type()
)
ipsecGlobTrustIcmpMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobTrustIcmpMsg.setStatus("mandatory")
_IpsecGlobSpiSize_Type = Integer32
_IpsecGlobSpiSize_Object = MibScalar
ipsecGlobSpiSize = _IpsecGlobSpiSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 35),
    _IpsecGlobSpiSize_Type()
)
ipsecGlobSpiSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobSpiSize.setStatus("mandatory")


class _IpsecGlobZeroIsakmpCookies_Type(Integer32):
    """Custom type ipsecGlobZeroIsakmpCookies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobZeroIsakmpCookies_Type.__name__ = "Integer32"
_IpsecGlobZeroIsakmpCookies_Object = MibScalar
ipsecGlobZeroIsakmpCookies = _IpsecGlobZeroIsakmpCookies_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 36),
    _IpsecGlobZeroIsakmpCookies_Type()
)
ipsecGlobZeroIsakmpCookies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobZeroIsakmpCookies.setStatus("mandatory")
_IpsecGlobMaxKeyLength_Type = Integer32
_IpsecGlobMaxKeyLength_Object = MibScalar
ipsecGlobMaxKeyLength = _IpsecGlobMaxKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 37),
    _IpsecGlobMaxKeyLength_Type()
)
ipsecGlobMaxKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobMaxKeyLength.setStatus("mandatory")


class _IpsecGlobNoInitialContact_Type(Integer32):
    """Custom type ipsecGlobNoInitialContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecGlobNoInitialContact_Type.__name__ = "Integer32"
_IpsecGlobNoInitialContact_Object = MibScalar
ipsecGlobNoInitialContact = _IpsecGlobNoInitialContact_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 1, 38),
    _IpsecGlobNoInitialContact_Type()
)
ipsecGlobNoInitialContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobNoInitialContact.setStatus("mandatory")
_IpsecPublicKeyTable_Object = MibTable
ipsecPublicKeyTable = _IpsecPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2)
)
if mibBuilder.loadTexts:
    ipsecPublicKeyTable.setStatus("mandatory")
_IpsecPubKeyEntry_Object = MibTableRow
ipsecPubKeyEntry = _IpsecPubKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2, 1)
)
ipsecPubKeyEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecPubKeyAlgorithm"),
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecPubKeyKeyLength"),
)
if mibBuilder.loadTexts:
    ipsecPubKeyEntry.setStatus("mandatory")
_IpsecPubKeyIndex_Type = Integer32
_IpsecPubKeyIndex_Object = MibTableColumn
ipsecPubKeyIndex = _IpsecPubKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2, 1, 1),
    _IpsecPubKeyIndex_Type()
)
ipsecPubKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPubKeyIndex.setStatus("mandatory")
_IpsecPubKeyDescription_Type = DisplayString
_IpsecPubKeyDescription_Object = MibTableColumn
ipsecPubKeyDescription = _IpsecPubKeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2, 1, 2),
    _IpsecPubKeyDescription_Type()
)
ipsecPubKeyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPubKeyDescription.setStatus("mandatory")


class _IpsecPubKeyAlgorithm_Type(Integer32):
    """Custom type ipsecPubKeyAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 3),
          ("rsa", 2))
    )


_IpsecPubKeyAlgorithm_Type.__name__ = "Integer32"
_IpsecPubKeyAlgorithm_Object = MibTableColumn
ipsecPubKeyAlgorithm = _IpsecPubKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2, 1, 3),
    _IpsecPubKeyAlgorithm_Type()
)
ipsecPubKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPubKeyAlgorithm.setStatus("mandatory")
_IpsecPubKeyKeyLength_Type = Integer32
_IpsecPubKeyKeyLength_Object = MibTableColumn
ipsecPubKeyKeyLength = _IpsecPubKeyKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 2, 1, 4),
    _IpsecPubKeyKeyLength_Type()
)
ipsecPubKeyKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPubKeyKeyLength.setStatus("mandatory")
_IpsecSaTable_Object = MibTable
ipsecSaTable = _IpsecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3)
)
if mibBuilder.loadTexts:
    ipsecSaTable.setStatus("mandatory")
_IpsecSaEntry_Object = MibTableRow
ipsecSaEntry = _IpsecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1)
)
ipsecSaEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecSaIndex"),
)
if mibBuilder.loadTexts:
    ipsecSaEntry.setStatus("mandatory")
_IpsecSaIndex_Type = Integer32
_IpsecSaIndex_Object = MibTableColumn
ipsecSaIndex = _IpsecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 1),
    _IpsecSaIndex_Type()
)
ipsecSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIndex.setStatus("mandatory")


class _IpsecSaState_Type(Integer32):
    """Custom type ipsecSaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("delete", 3),
          ("expired", 2))
    )


_IpsecSaState_Type.__name__ = "Integer32"
_IpsecSaState_Object = MibTableColumn
ipsecSaState = _IpsecSaState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 3),
    _IpsecSaState_Type()
)
ipsecSaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSaState.setStatus("mandatory")


class _IpsecSaCreator_Type(Integer32):
    """Custom type ipsecSaCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 2),
          ("manual", 1))
    )


_IpsecSaCreator_Type.__name__ = "Integer32"
_IpsecSaCreator_Object = MibTableColumn
ipsecSaCreator = _IpsecSaCreator_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 4),
    _IpsecSaCreator_Type()
)
ipsecSaCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaCreator.setStatus("mandatory")


class _IpsecSaDir_Type(Integer32):
    """Custom type ipsecSaDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_IpsecSaDir_Type.__name__ = "Integer32"
_IpsecSaDir_Object = MibTableColumn
ipsecSaDir = _IpsecSaDir_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 5),
    _IpsecSaDir_Type()
)
ipsecSaDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDir.setStatus("mandatory")


class _IpsecSaMode_Type(Integer32):
    """Custom type ipsecSaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_IpsecSaMode_Type.__name__ = "Integer32"
_IpsecSaMode_Object = MibTableColumn
ipsecSaMode = _IpsecSaMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 6),
    _IpsecSaMode_Type()
)
ipsecSaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaMode.setStatus("mandatory")


class _IpsecSaSecProto_Type(Integer32):
    """Custom type ipsecSaSecProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51,
              108)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("esp", 50),
          ("ipcomp", 108))
    )


_IpsecSaSecProto_Type.__name__ = "Integer32"
_IpsecSaSecProto_Object = MibTableColumn
ipsecSaSecProto = _IpsecSaSecProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 7),
    _IpsecSaSecProto_Type()
)
ipsecSaSecProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSecProto.setStatus("mandatory")
_IpsecSaLocalIp_Type = IpAddress
_IpsecSaLocalIp_Object = MibTableColumn
ipsecSaLocalIp = _IpsecSaLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 8),
    _IpsecSaLocalIp_Type()
)
ipsecSaLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaLocalIp.setStatus("mandatory")
_IpsecSaPeerIp_Type = IpAddress
_IpsecSaPeerIp_Object = MibTableColumn
ipsecSaPeerIp = _IpsecSaPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 9),
    _IpsecSaPeerIp_Type()
)
ipsecSaPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaPeerIp.setStatus("mandatory")
_IpsecSaSrcAddress_Type = IpAddress
_IpsecSaSrcAddress_Object = MibTableColumn
ipsecSaSrcAddress = _IpsecSaSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 10),
    _IpsecSaSrcAddress_Type()
)
ipsecSaSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSrcAddress.setStatus("mandatory")
_IpsecSaSrcMaskLen_Type = Integer32
_IpsecSaSrcMaskLen_Object = MibTableColumn
ipsecSaSrcMaskLen = _IpsecSaSrcMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 11),
    _IpsecSaSrcMaskLen_Type()
)
ipsecSaSrcMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSrcMaskLen.setStatus("mandatory")
_IpsecSaSrcRange_Type = IpAddress
_IpsecSaSrcRange_Object = MibTableColumn
ipsecSaSrcRange = _IpsecSaSrcRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 12),
    _IpsecSaSrcRange_Type()
)
ipsecSaSrcRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSrcRange.setStatus("mandatory")
_IpsecSaDstAddress_Type = IpAddress
_IpsecSaDstAddress_Object = MibTableColumn
ipsecSaDstAddress = _IpsecSaDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 13),
    _IpsecSaDstAddress_Type()
)
ipsecSaDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDstAddress.setStatus("mandatory")
_IpsecSaDstMaskLen_Type = Integer32
_IpsecSaDstMaskLen_Object = MibTableColumn
ipsecSaDstMaskLen = _IpsecSaDstMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 14),
    _IpsecSaDstMaskLen_Type()
)
ipsecSaDstMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDstMaskLen.setStatus("mandatory")
_IpsecSaDstRange_Type = IpAddress
_IpsecSaDstRange_Object = MibTableColumn
ipsecSaDstRange = _IpsecSaDstRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 15),
    _IpsecSaDstRange_Type()
)
ipsecSaDstRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDstRange.setStatus("mandatory")
_IpsecSaSpi_Type = HexValue
_IpsecSaSpi_Object = MibTableColumn
ipsecSaSpi = _IpsecSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 17),
    _IpsecSaSpi_Type()
)
ipsecSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSpi.setStatus("mandatory")


class _IpsecSaAuthAlg_Type(Integer32):
    """Custom type ipsecSaAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("md5-96", 4),
          ("none", 2),
          ("sha1-96", 6))
    )


_IpsecSaAuthAlg_Type.__name__ = "Integer32"
_IpsecSaAuthAlg_Object = MibTableColumn
ipsecSaAuthAlg = _IpsecSaAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 18),
    _IpsecSaAuthAlg_Type()
)
ipsecSaAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAuthAlg.setStatus("mandatory")


class _IpsecSaEncAlg_Type(Integer32):
    """Custom type ipsecSaEncAlg based on Integer32"""
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
        *(("blowfish-cbc", 4),
          ("cast128-cbc", 5),
          ("des-cbc", 2),
          ("des3-cbc", 3),
          ("none", 1))
    )


_IpsecSaEncAlg_Type.__name__ = "Integer32"
_IpsecSaEncAlg_Object = MibTableColumn
ipsecSaEncAlg = _IpsecSaEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 19),
    _IpsecSaEncAlg_Type()
)
ipsecSaEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEncAlg.setStatus("mandatory")
_IpsecSaAuthKeyLen_Type = Integer32
_IpsecSaAuthKeyLen_Object = MibTableColumn
ipsecSaAuthKeyLen = _IpsecSaAuthKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 21),
    _IpsecSaAuthKeyLen_Type()
)
ipsecSaAuthKeyLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAuthKeyLen.setStatus("mandatory")
_IpsecSaEncKeyLen_Type = Integer32
_IpsecSaEncKeyLen_Object = MibTableColumn
ipsecSaEncKeyLen = _IpsecSaEncKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 22),
    _IpsecSaEncKeyLen_Type()
)
ipsecSaEncKeyLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEncKeyLen.setStatus("mandatory")
_IpsecSaLifeSeconds_Type = Integer32
_IpsecSaLifeSeconds_Object = MibTableColumn
ipsecSaLifeSeconds = _IpsecSaLifeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 25),
    _IpsecSaLifeSeconds_Type()
)
ipsecSaLifeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaLifeSeconds.setStatus("mandatory")
_IpsecSaLifeKBytes_Type = Integer32
_IpsecSaLifeKBytes_Object = MibTableColumn
ipsecSaLifeKBytes = _IpsecSaLifeKBytes_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 26),
    _IpsecSaLifeKBytes_Type()
)
ipsecSaLifeKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaLifeKBytes.setStatus("mandatory")


class _IpsecSaProto_Type(Integer32):
    """Custom type ipsecSaProto based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("an", 107),
          ("argus", 13),
          ("aris", 104),
          ("ax25", 93),
          ("bbn", 10),
          ("bna", 49),
          ("brsatmon", 76),
          ("cbt", 7),
          ("cftp", 62),
          ("chaos", 16),
          ("compaq", 110),
          ("cphb", 73),
          ("cpnx", 72),
          ("dcn", 19),
          ("ddp", 37),
          ("dgp", 86),
          ("distfs", 68),
          ("dont-verify", 255),
          ("egp", 8),
          ("eigrp", 88),
          ("emcon", 14),
          ("encap", 98),
          ("encrypt", 99),
          ("esp", 50),
          ("etherip", 97),
          ("ggp", 3),
          ("gmtp", 100),
          ("gre", 47),
          ("hmp", 20),
          ("hop0", 114),
          ("icmp", 1),
          ("idpr", 35),
          ("idprc", 38),
          ("idrp", 45),
          ("ifmp", 101),
          ("igmp", 2),
          ("igp", 9),
          ("il", 40),
          ("inlsp", 52),
          ("ipcv", 71),
          ("ipip", 4),
          ("ippc", 67),
          ("ippcp", 108),
          ("ipproto-116", 116),
          ("ipproto-117", 117),
          ("ipproto-118", 118),
          ("ipproto-119", 119),
          ("ipproto-120", 120),
          ("ipproto-121", 121),
          ("ipproto-122", 122),
          ("ipproto-123", 123),
          ("ipproto-124", 124),
          ("ipproto-125", 125),
          ("ipproto-126", 126),
          ("ipproto-127", 127),
          ("ipproto-128", 128),
          ("ipproto-129", 129),
          ("ipproto-130", 130),
          ("ipproto-131", 131),
          ("ipproto-132", 132),
          ("ipproto-133", 133),
          ("ipproto-134", 134),
          ("ipproto-135", 135),
          ("ipproto-136", 136),
          ("ipproto-137", 137),
          ("ipproto-138", 138),
          ("ipproto-139", 139),
          ("ipproto-140", 140),
          ("ipproto-141", 141),
          ("ipproto-142", 142),
          ("ipproto-143", 143),
          ("ipproto-144", 144),
          ("ipproto-145", 145),
          ("ipproto-146", 146),
          ("ipproto-147", 147),
          ("ipproto-148", 148),
          ("ipproto-149", 149),
          ("ipproto-150", 150),
          ("ipproto-151", 151),
          ("ipproto-152", 152),
          ("ipproto-153", 153),
          ("ipproto-154", 154),
          ("ipproto-155", 155),
          ("ipproto-156", 156),
          ("ipproto-157", 157),
          ("ipproto-158", 158),
          ("ipproto-159", 159),
          ("ipproto-160", 160),
          ("ipproto-161", 161),
          ("ipproto-162", 162),
          ("ipproto-163", 163),
          ("ipproto-164", 164),
          ("ipproto-165", 165),
          ("ipproto-166", 166),
          ("ipproto-167", 167),
          ("ipproto-168", 168),
          ("ipproto-169", 169),
          ("ipproto-170", 170),
          ("ipproto-171", 171),
          ("ipproto-172", 172),
          ("ipproto-173", 173),
          ("ipproto-174", 174),
          ("ipproto-175", 175),
          ("ipproto-176", 176),
          ("ipproto-177", 177),
          ("ipproto-178", 178),
          ("ipproto-179", 179),
          ("ipproto-180", 180),
          ("ipproto-181", 181),
          ("ipproto-182", 182),
          ("ipproto-183", 183),
          ("ipproto-184", 184),
          ("ipproto-185", 185),
          ("ipproto-186", 186),
          ("ipproto-187", 187),
          ("ipproto-188", 188),
          ("ipproto-189", 189),
          ("ipproto-190", 190),
          ("ipproto-191", 191),
          ("ipproto-192", 192),
          ("ipproto-193", 193),
          ("ipproto-194", 194),
          ("ipproto-195", 195),
          ("ipproto-196", 196),
          ("ipproto-197", 197),
          ("ipproto-198", 198),
          ("ipproto-199", 199),
          ("ipproto-200", 200),
          ("ipproto-201", 201),
          ("ipproto-202", 202),
          ("ipproto-203", 203),
          ("ipproto-204", 204),
          ("ipproto-205", 205),
          ("ipproto-206", 206),
          ("ipproto-207", 207),
          ("ipproto-208", 208),
          ("ipproto-209", 209),
          ("ipproto-210", 210),
          ("ipproto-211", 211),
          ("ipproto-212", 212),
          ("ipproto-213", 213),
          ("ipproto-214", 214),
          ("ipproto-215", 215),
          ("ipproto-216", 216),
          ("ipproto-217", 217),
          ("ipproto-218", 218),
          ("ipproto-219", 219),
          ("ipproto-220", 220),
          ("ipproto-221", 221),
          ("ipproto-222", 222),
          ("ipproto-223", 223),
          ("ipproto-224", 224),
          ("ipproto-225", 225),
          ("ipproto-226", 226),
          ("ipproto-227", 227),
          ("ipproto-228", 228),
          ("ipproto-229", 229),
          ("ipproto-230", 230),
          ("ipproto-231", 231),
          ("ipproto-232", 232),
          ("ipproto-233", 233),
          ("ipproto-234", 234),
          ("ipproto-235", 235),
          ("ipproto-236", 236),
          ("ipproto-237", 237),
          ("ipproto-238", 238),
          ("ipproto-239", 239),
          ("ipproto-240", 240),
          ("ipproto-241", 241),
          ("ipproto-242", 242),
          ("ipproto-243", 243),
          ("ipproto-244", 244),
          ("ipproto-245", 245),
          ("ipproto-246", 246),
          ("ipproto-247", 247),
          ("ipproto-248", 248),
          ("ipproto-249", 249),
          ("ipproto-250", 250),
          ("ipproto-251", 251),
          ("ipproto-252", 252),
          ("ipproto-253", 253),
          ("ipproto-254", 254),
          ("ipproto-61", 61),
          ("ipv6", 41),
          ("ipv6frag", 44),
          ("ipv6icmp", 58),
          ("ipv6nonxt", 59),
          ("ipv6opts", 60),
          ("ipv6route", 43),
          ("ipwip", 94),
          ("ipxip", 111),
          ("irtp", 28),
          ("isoip", 80),
          ("isotp4", 29),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("larp", 91),
          ("leaf1", 25),
          ("leaf2", 26),
          ("local", 63),
          ("merit", 32),
          ("mfe", 31),
          ("mhrp", 48),
          ("micp", 95),
          ("mobile", 55),
          ("mtp", 92),
          ("mux", 18),
          ("narp", 54),
          ("netblt", 30),
          ("nsfnet", 85),
          ("nvp", 11),
          ("ospfigp", 89),
          ("pc3", 34),
          ("pgm", 113),
          ("pim", 103),
          ("pnni", 102),
          ("prm", 21),
          ("pup", 12),
          ("pvp", 75),
          ("qnx", 106),
          ("rdp", 27),
          ("rsvp", 46),
          ("rvd", 66),
          ("sat", 64),
          ("satmon", 69),
          ("scc", 96),
          ("scps", 105),
          ("sdrp", 42),
          ("securevmtp", 82),
          ("sep", 33),
          ("skip", 57),
          ("snp", 109),
          ("sprite", 90),
          ("st", 5),
          ("sunnd", 77),
          ("swipe", 53),
          ("tcf", 87),
          ("tcp", 6),
          ("tlsp", 56),
          ("tp", 39),
          ("trunk1", 23),
          ("trunk2", 24),
          ("ttp", 84),
          ("udp", 17),
          ("vines", 83),
          ("visa", 70),
          ("vmtp", 81),
          ("vrrp", 112),
          ("wbexpak", 79),
          ("wbmon", 78),
          ("wsn", 74),
          ("xnet", 15),
          ("xns", 22),
          ("xtp", 36))
    )


_IpsecSaProto_Type.__name__ = "Integer32"
_IpsecSaProto_Object = MibTableColumn
ipsecSaProto = _IpsecSaProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 27),
    _IpsecSaProto_Type()
)
ipsecSaProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaProto.setStatus("mandatory")
_IpsecSaSrcPort_Type = Integer32
_IpsecSaSrcPort_Object = MibTableColumn
ipsecSaSrcPort = _IpsecSaSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 28),
    _IpsecSaSrcPort_Type()
)
ipsecSaSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSrcPort.setStatus("mandatory")
_IpsecSaDstPort_Type = Integer32
_IpsecSaDstPort_Object = MibTableColumn
ipsecSaDstPort = _IpsecSaDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 29),
    _IpsecSaDstPort_Type()
)
ipsecSaDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDstPort.setStatus("mandatory")
_IpsecSaSeconds_Type = Integer32
_IpsecSaSeconds_Object = MibTableColumn
ipsecSaSeconds = _IpsecSaSeconds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 30),
    _IpsecSaSeconds_Type()
)
ipsecSaSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSeconds.setStatus("mandatory")
_IpsecSaBytes_Type = Integer32
_IpsecSaBytes_Object = MibTableColumn
ipsecSaBytes = _IpsecSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 31),
    _IpsecSaBytes_Type()
)
ipsecSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaBytes.setStatus("mandatory")
_IpsecSaPackets_Type = Integer32
_IpsecSaPackets_Object = MibTableColumn
ipsecSaPackets = _IpsecSaPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 32),
    _IpsecSaPackets_Type()
)
ipsecSaPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaPackets.setStatus("mandatory")
_IpsecSaReplayErrors_Type = Integer32
_IpsecSaReplayErrors_Object = MibTableColumn
ipsecSaReplayErrors = _IpsecSaReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 33),
    _IpsecSaReplayErrors_Type()
)
ipsecSaReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaReplayErrors.setStatus("mandatory")
_IpsecSaRecvErrors_Type = Integer32
_IpsecSaRecvErrors_Object = MibTableColumn
ipsecSaRecvErrors = _IpsecSaRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 34),
    _IpsecSaRecvErrors_Type()
)
ipsecSaRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaRecvErrors.setStatus("mandatory")
_IpsecSaDecryptErrors_Type = Integer32
_IpsecSaDecryptErrors_Object = MibTableColumn
ipsecSaDecryptErrors = _IpsecSaDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 3, 1, 35),
    _IpsecSaDecryptErrors_Type()
)
ipsecSaDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDecryptErrors.setStatus("mandatory")
_IkeSaTable_Object = MibTable
ikeSaTable = _IkeSaTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4)
)
if mibBuilder.loadTexts:
    ikeSaTable.setStatus("mandatory")
_IkeSaEntry_Object = MibTableRow
ikeSaEntry = _IkeSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1)
)
ikeSaEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ikeSaIndex"),
)
if mibBuilder.loadTexts:
    ikeSaEntry.setStatus("mandatory")
_IkeSaIndex_Type = Integer32
_IkeSaIndex_Object = MibTableColumn
ikeSaIndex = _IkeSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 1),
    _IkeSaIndex_Type()
)
ikeSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaIndex.setStatus("mandatory")


class _IkeSaState_Type(Integer32):
    """Custom type ikeSaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delete", 7),
          ("established", 2),
          ("negotiating", 1),
          ("waiting-for-remove", 3))
    )


_IkeSaState_Type.__name__ = "Integer32"
_IkeSaState_Object = MibTableColumn
ikeSaState = _IkeSaState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 3),
    _IkeSaState_Type()
)
ikeSaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikeSaState.setStatus("mandatory")


class _IkeSaXchType_Type(Integer32):
    """Custom type ikeSaXchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              256)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 4),
          ("any", 256),
          ("authentication-only", 3),
          ("base", 1),
          ("id-protect", 2),
          ("info", 5),
          ("new-group", 33),
          ("quick", 32))
    )


_IkeSaXchType_Type.__name__ = "Integer32"
_IkeSaXchType_Object = MibTableColumn
ikeSaXchType = _IkeSaXchType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 4),
    _IkeSaXchType_Type()
)
ikeSaXchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaXchType.setStatus("mandatory")


class _IkeSaAuthMethod_Type(Integer32):
    """Custom type ikeSaAuthMethod based on Integer32"""
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
        *(("dss-sig", 2),
          ("pre-sh-key", 1),
          ("rsa-enc", 4),
          ("rsa-sig", 3))
    )


_IkeSaAuthMethod_Type.__name__ = "Integer32"
_IkeSaAuthMethod_Object = MibTableColumn
ikeSaAuthMethod = _IkeSaAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 5),
    _IkeSaAuthMethod_Type()
)
ikeSaAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaAuthMethod.setStatus("mandatory")
_IkeSaAlgs_Type = DisplayString
_IkeSaAlgs_Object = MibTableColumn
ikeSaAlgs = _IkeSaAlgs_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 6),
    _IkeSaAlgs_Type()
)
ikeSaAlgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaAlgs.setStatus("mandatory")


class _IkeSaRole_Type(Integer32):
    """Custom type ikeSaRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )


_IkeSaRole_Type.__name__ = "Integer32"
_IkeSaRole_Object = MibTableColumn
ikeSaRole = _IkeSaRole_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 7),
    _IkeSaRole_Type()
)
ikeSaRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaRole.setStatus("mandatory")
_IkeSaLocalId_Type = DisplayString
_IkeSaLocalId_Object = MibTableColumn
ikeSaLocalId = _IkeSaLocalId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 8),
    _IkeSaLocalId_Type()
)
ikeSaLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaLocalId.setStatus("mandatory")
_IkeSaRemoteId_Type = DisplayString
_IkeSaRemoteId_Object = MibTableColumn
ikeSaRemoteId = _IkeSaRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 9),
    _IkeSaRemoteId_Type()
)
ikeSaRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaRemoteId.setStatus("mandatory")
_IkeSaRemoteIp_Type = IpAddress
_IkeSaRemoteIp_Object = MibTableColumn
ikeSaRemoteIp = _IkeSaRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 11),
    _IkeSaRemoteIp_Type()
)
ikeSaRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaRemoteIp.setStatus("mandatory")
_IkeSaCookieI_Type = OctetString
_IkeSaCookieI_Object = MibTableColumn
ikeSaCookieI = _IkeSaCookieI_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 12),
    _IkeSaCookieI_Type()
)
ikeSaCookieI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaCookieI.setStatus("mandatory")
_IkeSaCookieR_Type = OctetString
_IkeSaCookieR_Object = MibTableColumn
ikeSaCookieR = _IkeSaCookieR_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 13),
    _IkeSaCookieR_Type()
)
ikeSaCookieR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaCookieR.setStatus("mandatory")
_IkeSaTimes_Type = DisplayString
_IkeSaTimes_Object = MibTableColumn
ikeSaTimes = _IkeSaTimes_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 14),
    _IkeSaTimes_Type()
)
ikeSaTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaTimes.setStatus("mandatory")
_IkeSaNumCerts_Type = Integer32
_IkeSaNumCerts_Object = MibTableColumn
ikeSaNumCerts = _IkeSaNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 15),
    _IkeSaNumCerts_Type()
)
ikeSaNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaNumCerts.setStatus("mandatory")
_IkeSaNumNegotiations_Type = Integer32
_IkeSaNumNegotiations_Object = MibTableColumn
ikeSaNumNegotiations = _IkeSaNumNegotiations_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 16),
    _IkeSaNumNegotiations_Type()
)
ikeSaNumNegotiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaNumNegotiations.setStatus("mandatory")
_IkeSaBytes_Type = Integer32
_IkeSaBytes_Object = MibTableColumn
ikeSaBytes = _IkeSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 17),
    _IkeSaBytes_Type()
)
ikeSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaBytes.setStatus("mandatory")
_IkeSaMajVersion_Type = Integer32
_IkeSaMajVersion_Object = MibTableColumn
ikeSaMajVersion = _IkeSaMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 18),
    _IkeSaMajVersion_Type()
)
ikeSaMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaMajVersion.setStatus("mandatory")
_IkeSaMinVersion_Type = Integer32
_IkeSaMinVersion_Object = MibTableColumn
ikeSaMinVersion = _IkeSaMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 4, 1, 19),
    _IkeSaMinVersion_Type()
)
ikeSaMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikeSaMinVersion.setStatus("mandatory")
_IpsecPeerTable_Object = MibTable
ipsecPeerTable = _IpsecPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5)
)
if mibBuilder.loadTexts:
    ipsecPeerTable.setStatus("mandatory")
_IpsecPeerEntry_Object = MibTableRow
ipsecPeerEntry = _IpsecPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1)
)
ipsecPeerEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecPeerTrafficList"),
)
if mibBuilder.loadTexts:
    ipsecPeerEntry.setStatus("mandatory")
_IpsecPeerIndex_Type = Integer32
_IpsecPeerIndex_Object = MibTableColumn
ipsecPeerIndex = _IpsecPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 1),
    _IpsecPeerIndex_Type()
)
ipsecPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPeerIndex.setStatus("mandatory")
_IpsecPeerNextIndex_Type = Integer32
_IpsecPeerNextIndex_Object = MibTableColumn
ipsecPeerNextIndex = _IpsecPeerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 2),
    _IpsecPeerNextIndex_Type()
)
ipsecPeerNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerNextIndex.setStatus("mandatory")
_IpsecPeerDescription_Type = DisplayString
_IpsecPeerDescription_Object = MibTableColumn
ipsecPeerDescription = _IpsecPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 3),
    _IpsecPeerDescription_Type()
)
ipsecPeerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerDescription.setStatus("mandatory")
_IpsecPeerPeerIds_Type = DisplayString
_IpsecPeerPeerIds_Object = MibTableColumn
ipsecPeerPeerIds = _IpsecPeerPeerIds_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 5),
    _IpsecPeerPeerIds_Type()
)
ipsecPeerPeerIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPeerIds.setStatus("mandatory")
_IpsecPeerPeerAddress_Type = IpAddress
_IpsecPeerPeerAddress_Object = MibTableColumn
ipsecPeerPeerAddress = _IpsecPeerPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 6),
    _IpsecPeerPeerAddress_Type()
)
ipsecPeerPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPeerAddress.setStatus("mandatory")
_IpsecPeerLocalId_Type = DisplayString
_IpsecPeerLocalId_Object = MibTableColumn
ipsecPeerLocalId = _IpsecPeerLocalId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 7),
    _IpsecPeerLocalId_Type()
)
ipsecPeerLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerLocalId.setStatus("mandatory")
_IpsecPeerLocalAddress_Type = IpAddress
_IpsecPeerLocalAddress_Object = MibTableColumn
ipsecPeerLocalAddress = _IpsecPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 8),
    _IpsecPeerLocalAddress_Type()
)
ipsecPeerLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerLocalAddress.setStatus("mandatory")
_IpsecPeerLocalCert_Type = Integer32
_IpsecPeerLocalCert_Object = MibTableColumn
ipsecPeerLocalCert = _IpsecPeerLocalCert_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 9),
    _IpsecPeerLocalCert_Type()
)
ipsecPeerLocalCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerLocalCert.setStatus("mandatory")
_IpsecPeerIkeProposals_Type = Integer32
_IpsecPeerIkeProposals_Object = MibTableColumn
ipsecPeerIkeProposals = _IpsecPeerIkeProposals_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 10),
    _IpsecPeerIkeProposals_Type()
)
ipsecPeerIkeProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerIkeProposals.setStatus("mandatory")
_IpsecPeerTrafficList_Type = Integer32
_IpsecPeerTrafficList_Object = MibTableColumn
ipsecPeerTrafficList = _IpsecPeerTrafficList_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 11),
    _IpsecPeerTrafficList_Type()
)
ipsecPeerTrafficList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerTrafficList.setStatus("mandatory")


class _IpsecPeerAuthMethod_Type(Integer32):
    """Custom type ipsecPeerAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("default", 14),
          ("delete", 15),
          ("dss-sig", 2),
          ("pre-sh-key", 1),
          ("rsa-enc", 4),
          ("rsa-sig", 3))
    )


_IpsecPeerAuthMethod_Type.__name__ = "Integer32"
_IpsecPeerAuthMethod_Object = MibTableColumn
ipsecPeerAuthMethod = _IpsecPeerAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 20),
    _IpsecPeerAuthMethod_Type()
)
ipsecPeerAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerAuthMethod.setStatus("mandatory")
_IpsecPeerPreSharedKey_Type = DisplayString
_IpsecPeerPreSharedKey_Object = MibTableColumn
ipsecPeerPreSharedKey = _IpsecPeerPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 21),
    _IpsecPeerPreSharedKey_Type()
)
ipsecPeerPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPreSharedKey.setStatus("mandatory")
_IpsecPeerIkeGroup_Type = Integer32
_IpsecPeerIkeGroup_Object = MibTableColumn
ipsecPeerIkeGroup = _IpsecPeerIkeGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 22),
    _IpsecPeerIkeGroup_Type()
)
ipsecPeerIkeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerIkeGroup.setStatus("mandatory")
_IpsecPeerPfsGroup_Type = Integer32
_IpsecPeerPfsGroup_Object = MibTableColumn
ipsecPeerPfsGroup = _IpsecPeerPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 23),
    _IpsecPeerPfsGroup_Type()
)
ipsecPeerPfsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPfsGroup.setStatus("mandatory")


class _IpsecPeerPh1Mode_Type(Integer32):
    """Custom type ipsecPeerPh1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("default", 3),
          ("id-protect", 1))
    )


_IpsecPeerPh1Mode_Type.__name__ = "Integer32"
_IpsecPeerPh1Mode_Object = MibTableColumn
ipsecPeerPh1Mode = _IpsecPeerPh1Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 24),
    _IpsecPeerPh1Mode_Type()
)
ipsecPeerPh1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerPh1Mode.setStatus("mandatory")
_IpsecPeerIkeLifeTime_Type = Integer32
_IpsecPeerIkeLifeTime_Object = MibTableColumn
ipsecPeerIkeLifeTime = _IpsecPeerIkeLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 25),
    _IpsecPeerIkeLifeTime_Type()
)
ipsecPeerIkeLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerIkeLifeTime.setStatus("mandatory")
_IpsecPeerIpsecLifeTime_Type = Integer32
_IpsecPeerIpsecLifeTime_Object = MibTableColumn
ipsecPeerIpsecLifeTime = _IpsecPeerIpsecLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 26),
    _IpsecPeerIpsecLifeTime_Type()
)
ipsecPeerIpsecLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerIpsecLifeTime.setStatus("mandatory")


class _IpsecPeerKeepAlive_Type(Integer32):
    """Custom type ipsecPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecPeerKeepAlive_Type.__name__ = "Integer32"
_IpsecPeerKeepAlive_Object = MibTableColumn
ipsecPeerKeepAlive = _IpsecPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 29),
    _IpsecPeerKeepAlive_Type()
)
ipsecPeerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerKeepAlive.setStatus("mandatory")


class _IpsecPeerGranularity_Type(Integer32):
    """Custom type ipsecPeerGranularity based on Integer32"""
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
        *(("coarse", 2),
          ("default", 1),
          ("ip", 3),
          ("port", 5),
          ("proto", 4))
    )


_IpsecPeerGranularity_Type.__name__ = "Integer32"
_IpsecPeerGranularity_Object = MibTableColumn
ipsecPeerGranularity = _IpsecPeerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 30),
    _IpsecPeerGranularity_Type()
)
ipsecPeerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerGranularity.setStatus("mandatory")


class _IpsecPeerDontVerifyPad_Type(Integer32):
    """Custom type ipsecPeerDontVerifyPad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_IpsecPeerDontVerifyPad_Type.__name__ = "Integer32"
_IpsecPeerDontVerifyPad_Object = MibTableColumn
ipsecPeerDontVerifyPad = _IpsecPeerDontVerifyPad_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 31),
    _IpsecPeerDontVerifyPad_Type()
)
ipsecPeerDontVerifyPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerDontVerifyPad.setStatus("mandatory")
_IpsecPeerDefaultIpsecProposals_Type = Integer32
_IpsecPeerDefaultIpsecProposals_Object = MibTableColumn
ipsecPeerDefaultIpsecProposals = _IpsecPeerDefaultIpsecProposals_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 42),
    _IpsecPeerDefaultIpsecProposals_Type()
)
ipsecPeerDefaultIpsecProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPeerDefaultIpsecProposals.setStatus("mandatory")
_IpsecPeerPreSharedKeyData_Type = OctetString
_IpsecPeerPreSharedKeyData_Object = MibTableColumn
ipsecPeerPreSharedKeyData = _IpsecPeerPreSharedKeyData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 5, 1, 63),
    _IpsecPeerPreSharedKeyData_Type()
)
ipsecPeerPreSharedKeyData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecPeerPreSharedKeyData.setStatus("mandatory")
_IkeProposalTable_Object = MibTable
ikeProposalTable = _IkeProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6)
)
if mibBuilder.loadTexts:
    ikeProposalTable.setStatus("mandatory")
_IkeProposalEntry_Object = MibTableRow
ikeProposalEntry = _IkeProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1)
)
ikeProposalEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ikePropEncAlg"),
)
if mibBuilder.loadTexts:
    ikeProposalEntry.setStatus("mandatory")
_IkePropIndex_Type = Integer32
_IkePropIndex_Object = MibTableColumn
ikePropIndex = _IkePropIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1, 1),
    _IkePropIndex_Type()
)
ikePropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePropIndex.setStatus("mandatory")
_IkePropNextChoice_Type = Integer32
_IkePropNextChoice_Object = MibTableColumn
ikePropNextChoice = _IkePropNextChoice_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1, 2),
    _IkePropNextChoice_Type()
)
ikePropNextChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikePropNextChoice.setStatus("mandatory")
_IkePropDescription_Type = DisplayString
_IkePropDescription_Object = MibTableColumn
ikePropDescription = _IkePropDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1, 3),
    _IkePropDescription_Type()
)
ikePropDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikePropDescription.setStatus("mandatory")


class _IkePropEncAlg_Type(Integer32):
    """Custom type ikePropEncAlg based on Integer32"""
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
        *(("blowfish-cbc", 4),
          ("cast128-cbc", 5),
          ("des-cbc", 2),
          ("des3-cbc", 3),
          ("none", 1))
    )


_IkePropEncAlg_Type.__name__ = "Integer32"
_IkePropEncAlg_Object = MibTableColumn
ikePropEncAlg = _IkePropEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1, 4),
    _IkePropEncAlg_Type()
)
ikePropEncAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikePropEncAlg.setStatus("mandatory")


class _IkePropHashAlg_Type(Integer32):
    """Custom type ikePropHashAlg based on Integer32"""
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
        *(("delete", 1),
          ("md5", 3),
          ("none", 2),
          ("sha1", 4))
    )


_IkePropHashAlg_Type.__name__ = "Integer32"
_IkePropHashAlg_Object = MibTableColumn
ikePropHashAlg = _IkePropHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 6, 1, 5),
    _IkePropHashAlg_Type()
)
ikePropHashAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ikePropHashAlg.setStatus("mandatory")
_IpsecTrafficTable_Object = MibTable
ipsecTrafficTable = _IpsecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7)
)
if mibBuilder.loadTexts:
    ipsecTrafficTable.setStatus("mandatory")
_IpsecTrafficEntry_Object = MibTableRow
ipsecTrafficEntry = _IpsecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1)
)
ipsecTrafficEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecTrProto"),
)
if mibBuilder.loadTexts:
    ipsecTrafficEntry.setStatus("mandatory")
_IpsecTrIndex_Type = Integer32
_IpsecTrIndex_Object = MibTableColumn
ipsecTrIndex = _IpsecTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 1),
    _IpsecTrIndex_Type()
)
ipsecTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTrIndex.setStatus("mandatory")
_IpsecTrNextIndex_Type = Integer32
_IpsecTrNextIndex_Object = MibTableColumn
ipsecTrNextIndex = _IpsecTrNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 2),
    _IpsecTrNextIndex_Type()
)
ipsecTrNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrNextIndex.setStatus("mandatory")
_IpsecTrDescription_Type = DisplayString
_IpsecTrDescription_Object = MibTableColumn
ipsecTrDescription = _IpsecTrDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 3),
    _IpsecTrDescription_Type()
)
ipsecTrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrDescription.setStatus("mandatory")
_IpsecTrLocalAddress_Type = IpAddress
_IpsecTrLocalAddress_Object = MibTableColumn
ipsecTrLocalAddress = _IpsecTrLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 4),
    _IpsecTrLocalAddress_Type()
)
ipsecTrLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrLocalAddress.setStatus("mandatory")
_IpsecTrLocalMaskLen_Type = Integer32
_IpsecTrLocalMaskLen_Object = MibTableColumn
ipsecTrLocalMaskLen = _IpsecTrLocalMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 5),
    _IpsecTrLocalMaskLen_Type()
)
ipsecTrLocalMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrLocalMaskLen.setStatus("mandatory")
_IpsecTrLocalRange_Type = IpAddress
_IpsecTrLocalRange_Object = MibTableColumn
ipsecTrLocalRange = _IpsecTrLocalRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 6),
    _IpsecTrLocalRange_Type()
)
ipsecTrLocalRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrLocalRange.setStatus("mandatory")
_IpsecTrRemoteAddress_Type = IpAddress
_IpsecTrRemoteAddress_Object = MibTableColumn
ipsecTrRemoteAddress = _IpsecTrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 7),
    _IpsecTrRemoteAddress_Type()
)
ipsecTrRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrRemoteAddress.setStatus("mandatory")
_IpsecTrRemoteMaskLen_Type = Integer32
_IpsecTrRemoteMaskLen_Object = MibTableColumn
ipsecTrRemoteMaskLen = _IpsecTrRemoteMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 8),
    _IpsecTrRemoteMaskLen_Type()
)
ipsecTrRemoteMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrRemoteMaskLen.setStatus("mandatory")
_IpsecTrRemoteRange_Type = IpAddress
_IpsecTrRemoteRange_Object = MibTableColumn
ipsecTrRemoteRange = _IpsecTrRemoteRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 9),
    _IpsecTrRemoteRange_Type()
)
ipsecTrRemoteRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrRemoteRange.setStatus("mandatory")


class _IpsecTrProto_Type(Integer32):
    """Custom type ipsecTrProto based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("an", 107),
          ("argus", 13),
          ("aris", 104),
          ("ax25", 93),
          ("bbn", 10),
          ("bna", 49),
          ("brsatmon", 76),
          ("cbt", 7),
          ("cftp", 62),
          ("chaos", 16),
          ("compaq", 110),
          ("cphb", 73),
          ("cpnx", 72),
          ("dcn", 19),
          ("ddp", 37),
          ("dgp", 86),
          ("distfs", 68),
          ("dont-verify", 255),
          ("egp", 8),
          ("eigrp", 88),
          ("emcon", 14),
          ("encap", 98),
          ("encrypt", 99),
          ("esp", 50),
          ("etherip", 97),
          ("ggp", 3),
          ("gmtp", 100),
          ("gre", 47),
          ("hmp", 20),
          ("hop0", 114),
          ("icmp", 1),
          ("idpr", 35),
          ("idprc", 38),
          ("idrp", 45),
          ("ifmp", 101),
          ("igmp", 2),
          ("igp", 9),
          ("il", 40),
          ("inlsp", 52),
          ("ipcv", 71),
          ("ipip", 4),
          ("ippc", 67),
          ("ippcp", 108),
          ("ipproto-116", 116),
          ("ipproto-117", 117),
          ("ipproto-118", 118),
          ("ipproto-119", 119),
          ("ipproto-120", 120),
          ("ipproto-121", 121),
          ("ipproto-122", 122),
          ("ipproto-123", 123),
          ("ipproto-124", 124),
          ("ipproto-125", 125),
          ("ipproto-126", 126),
          ("ipproto-127", 127),
          ("ipproto-128", 128),
          ("ipproto-129", 129),
          ("ipproto-130", 130),
          ("ipproto-131", 131),
          ("ipproto-132", 132),
          ("ipproto-133", 133),
          ("ipproto-134", 134),
          ("ipproto-135", 135),
          ("ipproto-136", 136),
          ("ipproto-137", 137),
          ("ipproto-138", 138),
          ("ipproto-139", 139),
          ("ipproto-140", 140),
          ("ipproto-141", 141),
          ("ipproto-142", 142),
          ("ipproto-143", 143),
          ("ipproto-144", 144),
          ("ipproto-145", 145),
          ("ipproto-146", 146),
          ("ipproto-147", 147),
          ("ipproto-148", 148),
          ("ipproto-149", 149),
          ("ipproto-150", 150),
          ("ipproto-151", 151),
          ("ipproto-152", 152),
          ("ipproto-153", 153),
          ("ipproto-154", 154),
          ("ipproto-155", 155),
          ("ipproto-156", 156),
          ("ipproto-157", 157),
          ("ipproto-158", 158),
          ("ipproto-159", 159),
          ("ipproto-160", 160),
          ("ipproto-161", 161),
          ("ipproto-162", 162),
          ("ipproto-163", 163),
          ("ipproto-164", 164),
          ("ipproto-165", 165),
          ("ipproto-166", 166),
          ("ipproto-167", 167),
          ("ipproto-168", 168),
          ("ipproto-169", 169),
          ("ipproto-170", 170),
          ("ipproto-171", 171),
          ("ipproto-172", 172),
          ("ipproto-173", 173),
          ("ipproto-174", 174),
          ("ipproto-175", 175),
          ("ipproto-176", 176),
          ("ipproto-177", 177),
          ("ipproto-178", 178),
          ("ipproto-179", 179),
          ("ipproto-180", 180),
          ("ipproto-181", 181),
          ("ipproto-182", 182),
          ("ipproto-183", 183),
          ("ipproto-184", 184),
          ("ipproto-185", 185),
          ("ipproto-186", 186),
          ("ipproto-187", 187),
          ("ipproto-188", 188),
          ("ipproto-189", 189),
          ("ipproto-190", 190),
          ("ipproto-191", 191),
          ("ipproto-192", 192),
          ("ipproto-193", 193),
          ("ipproto-194", 194),
          ("ipproto-195", 195),
          ("ipproto-196", 196),
          ("ipproto-197", 197),
          ("ipproto-198", 198),
          ("ipproto-199", 199),
          ("ipproto-200", 200),
          ("ipproto-201", 201),
          ("ipproto-202", 202),
          ("ipproto-203", 203),
          ("ipproto-204", 204),
          ("ipproto-205", 205),
          ("ipproto-206", 206),
          ("ipproto-207", 207),
          ("ipproto-208", 208),
          ("ipproto-209", 209),
          ("ipproto-210", 210),
          ("ipproto-211", 211),
          ("ipproto-212", 212),
          ("ipproto-213", 213),
          ("ipproto-214", 214),
          ("ipproto-215", 215),
          ("ipproto-216", 216),
          ("ipproto-217", 217),
          ("ipproto-218", 218),
          ("ipproto-219", 219),
          ("ipproto-220", 220),
          ("ipproto-221", 221),
          ("ipproto-222", 222),
          ("ipproto-223", 223),
          ("ipproto-224", 224),
          ("ipproto-225", 225),
          ("ipproto-226", 226),
          ("ipproto-227", 227),
          ("ipproto-228", 228),
          ("ipproto-229", 229),
          ("ipproto-230", 230),
          ("ipproto-231", 231),
          ("ipproto-232", 232),
          ("ipproto-233", 233),
          ("ipproto-234", 234),
          ("ipproto-235", 235),
          ("ipproto-236", 236),
          ("ipproto-237", 237),
          ("ipproto-238", 238),
          ("ipproto-239", 239),
          ("ipproto-240", 240),
          ("ipproto-241", 241),
          ("ipproto-242", 242),
          ("ipproto-243", 243),
          ("ipproto-244", 244),
          ("ipproto-245", 245),
          ("ipproto-246", 246),
          ("ipproto-247", 247),
          ("ipproto-248", 248),
          ("ipproto-249", 249),
          ("ipproto-250", 250),
          ("ipproto-251", 251),
          ("ipproto-252", 252),
          ("ipproto-253", 253),
          ("ipproto-254", 254),
          ("ipproto-61", 61),
          ("ipv6", 41),
          ("ipv6frag", 44),
          ("ipv6icmp", 58),
          ("ipv6nonxt", 59),
          ("ipv6opts", 60),
          ("ipv6route", 43),
          ("ipwip", 94),
          ("ipxip", 111),
          ("irtp", 28),
          ("isoip", 80),
          ("isotp4", 29),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("larp", 91),
          ("leaf1", 25),
          ("leaf2", 26),
          ("local", 63),
          ("merit", 32),
          ("mfe", 31),
          ("mhrp", 48),
          ("micp", 95),
          ("mobile", 55),
          ("mtp", 92),
          ("mux", 18),
          ("narp", 54),
          ("netblt", 30),
          ("nsfnet", 85),
          ("nvp", 11),
          ("ospfigp", 89),
          ("pc3", 34),
          ("pgm", 113),
          ("pim", 103),
          ("pnni", 102),
          ("prm", 21),
          ("pup", 12),
          ("pvp", 75),
          ("qnx", 106),
          ("rdp", 27),
          ("rsvp", 46),
          ("rvd", 66),
          ("sat", 64),
          ("satmon", 69),
          ("scc", 96),
          ("scps", 105),
          ("sdrp", 42),
          ("securevmtp", 82),
          ("sep", 33),
          ("skip", 57),
          ("snp", 109),
          ("sprite", 90),
          ("st", 5),
          ("sunnd", 77),
          ("swipe", 53),
          ("tcf", 87),
          ("tcp", 6),
          ("tlsp", 56),
          ("tp", 39),
          ("trunk1", 23),
          ("trunk2", 24),
          ("ttp", 84),
          ("udp", 17),
          ("vines", 83),
          ("visa", 70),
          ("vmtp", 81),
          ("vrrp", 112),
          ("wbexpak", 79),
          ("wbmon", 78),
          ("wsn", 74),
          ("xnet", 15),
          ("xns", 22),
          ("xtp", 36))
    )


_IpsecTrProto_Type.__name__ = "Integer32"
_IpsecTrProto_Object = MibTableColumn
ipsecTrProto = _IpsecTrProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 10),
    _IpsecTrProto_Type()
)
ipsecTrProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrProto.setStatus("mandatory")
_IpsecTrLocalPort_Type = Integer32
_IpsecTrLocalPort_Object = MibTableColumn
ipsecTrLocalPort = _IpsecTrLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 11),
    _IpsecTrLocalPort_Type()
)
ipsecTrLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrLocalPort.setStatus("mandatory")
_IpsecTrRemotePort_Type = Integer32
_IpsecTrRemotePort_Object = MibTableColumn
ipsecTrRemotePort = _IpsecTrRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 12),
    _IpsecTrRemotePort_Type()
)
ipsecTrRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrRemotePort.setStatus("mandatory")


class _IpsecTrAction_Type(Integer32):
    """Custom type ipsecTrAction based on Integer32"""
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
        *(("always-plain", 2),
          ("delete", 1),
          ("drop", 5),
          ("pass", 3),
          ("protect", 4))
    )


_IpsecTrAction_Type.__name__ = "Integer32"
_IpsecTrAction_Object = MibTableColumn
ipsecTrAction = _IpsecTrAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 13),
    _IpsecTrAction_Type()
)
ipsecTrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrAction.setStatus("mandatory")
_IpsecTrProposal_Type = Integer32
_IpsecTrProposal_Object = MibTableColumn
ipsecTrProposal = _IpsecTrProposal_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 14),
    _IpsecTrProposal_Type()
)
ipsecTrProposal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrProposal.setStatus("mandatory")


class _IpsecTrForceTunnelMode_Type(Integer32):
    """Custom type ipsecTrForceTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IpsecTrForceTunnelMode_Type.__name__ = "Integer32"
_IpsecTrForceTunnelMode_Object = MibTableColumn
ipsecTrForceTunnelMode = _IpsecTrForceTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 15),
    _IpsecTrForceTunnelMode_Type()
)
ipsecTrForceTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrForceTunnelMode.setStatus("mandatory")
_IpsecTrLifeTime_Type = Integer32
_IpsecTrLifeTime_Object = MibTableColumn
ipsecTrLifeTime = _IpsecTrLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 16),
    _IpsecTrLifeTime_Type()
)
ipsecTrLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrLifeTime.setStatus("mandatory")


class _IpsecTrGranularity_Type(Integer32):
    """Custom type ipsecTrGranularity based on Integer32"""
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
        *(("coarse", 2),
          ("default", 1),
          ("ip", 3),
          ("port", 5),
          ("proto", 4))
    )


_IpsecTrGranularity_Type.__name__ = "Integer32"
_IpsecTrGranularity_Object = MibTableColumn
ipsecTrGranularity = _IpsecTrGranularity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 17),
    _IpsecTrGranularity_Type()
)
ipsecTrGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrGranularity.setStatus("mandatory")


class _IpsecTrKeepAlive_Type(Integer32):
    """Custom type ipsecTrKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("false", 2),
          ("true", 1))
    )


_IpsecTrKeepAlive_Type.__name__ = "Integer32"
_IpsecTrKeepAlive_Object = MibTableColumn
ipsecTrKeepAlive = _IpsecTrKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 7, 1, 18),
    _IpsecTrKeepAlive_Type()
)
ipsecTrKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTrKeepAlive.setStatus("mandatory")
_IpsecProposalTable_Object = MibTable
ipsecProposalTable = _IpsecProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8)
)
if mibBuilder.loadTexts:
    ipsecProposalTable.setStatus("mandatory")
_IpsecProposalEntry_Object = MibTableRow
ipsecProposalEntry = _IpsecProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1)
)
ipsecProposalEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecPropProto"),
)
if mibBuilder.loadTexts:
    ipsecProposalEntry.setStatus("mandatory")
_IpsecPropIndex_Type = Integer32
_IpsecPropIndex_Object = MibTableColumn
ipsecPropIndex = _IpsecPropIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 1),
    _IpsecPropIndex_Type()
)
ipsecPropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPropIndex.setStatus("mandatory")
_IpsecPropNext_Type = Integer32
_IpsecPropNext_Object = MibTableColumn
ipsecPropNext = _IpsecPropNext_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 2),
    _IpsecPropNext_Type()
)
ipsecPropNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropNext.setStatus("mandatory")


class _IpsecPropBoolOp_Type(Integer32):
    """Custom type ipsecPropBoolOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("and", 3),
          ("delete", 1),
          ("or", 2))
    )


_IpsecPropBoolOp_Type.__name__ = "Integer32"
_IpsecPropBoolOp_Object = MibTableColumn
ipsecPropBoolOp = _IpsecPropBoolOp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 3),
    _IpsecPropBoolOp_Type()
)
ipsecPropBoolOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropBoolOp.setStatus("mandatory")
_IpsecPropDescription_Type = DisplayString
_IpsecPropDescription_Object = MibTableColumn
ipsecPropDescription = _IpsecPropDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 4),
    _IpsecPropDescription_Type()
)
ipsecPropDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropDescription.setStatus("mandatory")


class _IpsecPropProto_Type(Integer32):
    """Custom type ipsecPropProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("esp", 1))
    )


_IpsecPropProto_Type.__name__ = "Integer32"
_IpsecPropProto_Object = MibTableColumn
ipsecPropProto = _IpsecPropProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 6),
    _IpsecPropProto_Type()
)
ipsecPropProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropProto.setStatus("mandatory")


class _IpsecPropEncAlg_Type(Integer32):
    """Custom type ipsecPropEncAlg based on Integer32"""
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
        *(("blowfish-cbc", 4),
          ("cast128-cbc", 5),
          ("des-cbc", 2),
          ("des3-cbc", 3),
          ("none", 1))
    )


_IpsecPropEncAlg_Type.__name__ = "Integer32"
_IpsecPropEncAlg_Object = MibTableColumn
ipsecPropEncAlg = _IpsecPropEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 7),
    _IpsecPropEncAlg_Type()
)
ipsecPropEncAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropEncAlg.setStatus("mandatory")


class _IpsecPropAuthAlg_Type(Integer32):
    """Custom type ipsecPropAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("md5-96", 4),
          ("none", 2),
          ("sha1-96", 6))
    )


_IpsecPropAuthAlg_Type.__name__ = "Integer32"
_IpsecPropAuthAlg_Object = MibTableColumn
ipsecPropAuthAlg = _IpsecPropAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 8),
    _IpsecPropAuthAlg_Type()
)
ipsecPropAuthAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropAuthAlg.setStatus("mandatory")
_IpsecPropLifeTime_Type = Integer32
_IpsecPropLifeTime_Object = MibTableColumn
ipsecPropLifeTime = _IpsecPropLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 10),
    _IpsecPropLifeTime_Type()
)
ipsecPropLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropLifeTime.setStatus("mandatory")
_IpsecPropInSpi_Type = HexValue
_IpsecPropInSpi_Object = MibTableColumn
ipsecPropInSpi = _IpsecPropInSpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 11),
    _IpsecPropInSpi_Type()
)
ipsecPropInSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropInSpi.setStatus("mandatory")
_IpsecPropOutSpi_Type = HexValue
_IpsecPropOutSpi_Object = MibTableColumn
ipsecPropOutSpi = _IpsecPropOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 12),
    _IpsecPropOutSpi_Type()
)
ipsecPropOutSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropOutSpi.setStatus("mandatory")
_IpsecPropEncKeyIn_Type = DisplayString
_IpsecPropEncKeyIn_Object = MibTableColumn
ipsecPropEncKeyIn = _IpsecPropEncKeyIn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 14),
    _IpsecPropEncKeyIn_Type()
)
ipsecPropEncKeyIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropEncKeyIn.setStatus("mandatory")
_IpsecPropEncKeyOut_Type = DisplayString
_IpsecPropEncKeyOut_Object = MibTableColumn
ipsecPropEncKeyOut = _IpsecPropEncKeyOut_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 15),
    _IpsecPropEncKeyOut_Type()
)
ipsecPropEncKeyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropEncKeyOut.setStatus("mandatory")
_IpsecPropAuthKeyIn_Type = DisplayString
_IpsecPropAuthKeyIn_Object = MibTableColumn
ipsecPropAuthKeyIn = _IpsecPropAuthKeyIn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 17),
    _IpsecPropAuthKeyIn_Type()
)
ipsecPropAuthKeyIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropAuthKeyIn.setStatus("mandatory")
_IpsecPropAuthKeyOut_Type = DisplayString
_IpsecPropAuthKeyOut_Object = MibTableColumn
ipsecPropAuthKeyOut = _IpsecPropAuthKeyOut_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 18),
    _IpsecPropAuthKeyOut_Type()
)
ipsecPropAuthKeyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPropAuthKeyOut.setStatus("mandatory")
_IpsecPropEncKeyDataIn_Type = OctetString
_IpsecPropEncKeyDataIn_Object = MibTableColumn
ipsecPropEncKeyDataIn = _IpsecPropEncKeyDataIn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 33),
    _IpsecPropEncKeyDataIn_Type()
)
ipsecPropEncKeyDataIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecPropEncKeyDataIn.setStatus("mandatory")
_IpsecPropEncKeyDataOut_Type = OctetString
_IpsecPropEncKeyDataOut_Object = MibTableColumn
ipsecPropEncKeyDataOut = _IpsecPropEncKeyDataOut_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 34),
    _IpsecPropEncKeyDataOut_Type()
)
ipsecPropEncKeyDataOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecPropEncKeyDataOut.setStatus("mandatory")
_IpsecPropAuthKeyDataIn_Type = OctetString
_IpsecPropAuthKeyDataIn_Object = MibTableColumn
ipsecPropAuthKeyDataIn = _IpsecPropAuthKeyDataIn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 35),
    _IpsecPropAuthKeyDataIn_Type()
)
ipsecPropAuthKeyDataIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecPropAuthKeyDataIn.setStatus("mandatory")
_IpsecPropAuthKeyDataOut_Type = OctetString
_IpsecPropAuthKeyDataOut_Object = MibTableColumn
ipsecPropAuthKeyDataOut = _IpsecPropAuthKeyDataOut_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 8, 1, 36),
    _IpsecPropAuthKeyDataOut_Type()
)
ipsecPropAuthKeyDataOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecPropAuthKeyDataOut.setStatus("mandatory")
_IpsecLifeTimeTable_Object = MibTable
ipsecLifeTimeTable = _IpsecLifeTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9)
)
if mibBuilder.loadTexts:
    ipsecLifeTimeTable.setStatus("mandatory")
_IpsecLifeTimeEntry_Object = MibTableRow
ipsecLifeTimeEntry = _IpsecLifeTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1)
)
ipsecLifeTimeEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPSEC-MIB", "ipsecLifeType"),
)
if mibBuilder.loadTexts:
    ipsecLifeTimeEntry.setStatus("mandatory")
_IpsecLifeIndex_Type = Integer32
_IpsecLifeIndex_Object = MibTableColumn
ipsecLifeIndex = _IpsecLifeIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 1),
    _IpsecLifeIndex_Type()
)
ipsecLifeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLifeIndex.setStatus("mandatory")


class _IpsecLifeType_Type(Integer32):
    """Custom type ipsecLifeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("generic", 2))
    )


_IpsecLifeType_Type.__name__ = "Integer32"
_IpsecLifeType_Object = MibTableColumn
ipsecLifeType = _IpsecLifeType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 2),
    _IpsecLifeType_Type()
)
ipsecLifeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLifeType.setStatus("mandatory")
_IpsecLifeSoftKb_Type = Integer32
_IpsecLifeSoftKb_Object = MibTableColumn
ipsecLifeSoftKb = _IpsecLifeSoftKb_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 3),
    _IpsecLifeSoftKb_Type()
)
ipsecLifeSoftKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLifeSoftKb.setStatus("mandatory")
_IpsecLifeSoftSec_Type = Integer32
_IpsecLifeSoftSec_Object = MibTableColumn
ipsecLifeSoftSec = _IpsecLifeSoftSec_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 4),
    _IpsecLifeSoftSec_Type()
)
ipsecLifeSoftSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLifeSoftSec.setStatus("mandatory")
_IpsecLifeHardKb_Type = Integer32
_IpsecLifeHardKb_Object = MibTableColumn
ipsecLifeHardKb = _IpsecLifeHardKb_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 5),
    _IpsecLifeHardKb_Type()
)
ipsecLifeHardKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLifeHardKb.setStatus("mandatory")
_IpsecLifeHardSec_Type = Integer32
_IpsecLifeHardSec_Object = MibTableColumn
ipsecLifeHardSec = _IpsecLifeHardSec_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 9, 1, 6),
    _IpsecLifeHardSec_Type()
)
ipsecLifeHardSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLifeHardSec.setStatus("mandatory")
_IpsecStats_ObjectIdentity = ObjectIdentity
ipsecStats = _IpsecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10)
)
_IpsecStatsCurrentIkeSas_Type = Integer32
_IpsecStatsCurrentIkeSas_Object = MibScalar
ipsecStatsCurrentIkeSas = _IpsecStatsCurrentIkeSas_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 1),
    _IpsecStatsCurrentIkeSas_Type()
)
ipsecStatsCurrentIkeSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsCurrentIkeSas.setStatus("mandatory")
_IpsecStatsCurrentIpsecSas_Type = Integer32
_IpsecStatsCurrentIpsecSas_Object = MibScalar
ipsecStatsCurrentIpsecSas = _IpsecStatsCurrentIpsecSas_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 2),
    _IpsecStatsCurrentIpsecSas_Type()
)
ipsecStatsCurrentIpsecSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsCurrentIpsecSas.setStatus("mandatory")
_IpsecStatsIp_Type = Integer32
_IpsecStatsIp_Object = MibScalar
ipsecStatsIp = _IpsecStatsIp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 3),
    _IpsecStatsIp_Type()
)
ipsecStatsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsIp.setStatus("mandatory")
_IpsecStatsNonIp_Type = Integer32
_IpsecStatsNonIp_Object = MibScalar
ipsecStatsNonIp = _IpsecStatsNonIp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 4),
    _IpsecStatsNonIp_Type()
)
ipsecStatsNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsNonIp.setStatus("mandatory")
_IpsecStatsAh_Type = Integer32
_IpsecStatsAh_Object = MibScalar
ipsecStatsAh = _IpsecStatsAh_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 5),
    _IpsecStatsAh_Type()
)
ipsecStatsAh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsAh.setStatus("mandatory")
_IpsecStatsEsp_Type = Integer32
_IpsecStatsEsp_Object = MibScalar
ipsecStatsEsp = _IpsecStatsEsp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 6),
    _IpsecStatsEsp_Type()
)
ipsecStatsEsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsEsp.setStatus("mandatory")
_IpsecStatsDrop_Type = Integer32
_IpsecStatsDrop_Object = MibScalar
ipsecStatsDrop = _IpsecStatsDrop_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 7),
    _IpsecStatsDrop_Type()
)
ipsecStatsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsDrop.setStatus("mandatory")
_IpsecStatsPass_Type = Integer32
_IpsecStatsPass_Object = MibScalar
ipsecStatsPass = _IpsecStatsPass_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 8),
    _IpsecStatsPass_Type()
)
ipsecStatsPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsPass.setStatus("mandatory")
_IpsecStatsTrig_Type = Integer32
_IpsecStatsTrig_Object = MibScalar
ipsecStatsTrig = _IpsecStatsTrig_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 9),
    _IpsecStatsTrig_Type()
)
ipsecStatsTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsTrig.setStatus("mandatory")
_IpsecStatsFragPkt_Type = Integer32
_IpsecStatsFragPkt_Object = MibScalar
ipsecStatsFragPkt = _IpsecStatsFragPkt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 10),
    _IpsecStatsFragPkt_Type()
)
ipsecStatsFragPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsFragPkt.setStatus("mandatory")
_IpsecStatsFragBytes_Type = Integer32
_IpsecStatsFragBytes_Object = MibScalar
ipsecStatsFragBytes = _IpsecStatsFragBytes_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 11),
    _IpsecStatsFragBytes_Type()
)
ipsecStatsFragBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsFragBytes.setStatus("mandatory")
_IpsecStatsFragNonfirst_Type = Integer32
_IpsecStatsFragNonfirst_Object = MibScalar
ipsecStatsFragNonfirst = _IpsecStatsFragNonfirst_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 10, 12),
    _IpsecStatsFragNonfirst_Type()
)
ipsecStatsFragNonfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecStatsFragNonfirst.setStatus("mandatory")
_IpsecGlobalsContinued_ObjectIdentity = ObjectIdentity
ipsecGlobalsContinued = _IpsecGlobalsContinued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 11)
)
_IpsecGlobContPreIpsecRules_Type = Integer32
_IpsecGlobContPreIpsecRules_Object = MibScalar
ipsecGlobContPreIpsecRules = _IpsecGlobContPreIpsecRules_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 11, 1),
    _IpsecGlobContPreIpsecRules_Type()
)
ipsecGlobContPreIpsecRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobContPreIpsecRules.setStatus("mandatory")


class _IpsecGlobContDefaultRule_Type(Integer32):
    """Custom type ipsecGlobContDefaultRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_IpsecGlobContDefaultRule_Type.__name__ = "Integer32"
_IpsecGlobContDefaultRule_Object = MibScalar
ipsecGlobContDefaultRule = _IpsecGlobContDefaultRule_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 11, 2),
    _IpsecGlobContDefaultRule_Type()
)
ipsecGlobContDefaultRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecGlobContDefaultRule.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IPSEC-MIB",
    **{"DisplayString": DisplayString,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "ipsec": ipsec,
       "ipsecGlobals": ipsecGlobals,
       "ipsecGlobPeerIndex": ipsecGlobPeerIndex,
       "ipsecGlobDefaultAuthMethod": ipsecGlobDefaultAuthMethod,
       "ipsecGlobDefaultCertificate": ipsecGlobDefaultCertificate,
       "ipsecGlobDefaultLocalId": ipsecGlobDefaultLocalId,
       "ipsecGlobDefaultIpsecProposal": ipsecGlobDefaultIpsecProposal,
       "ipsecGlobDefaultIkeProposal": ipsecGlobDefaultIkeProposal,
       "ipsecGlobDefaultIpsecLifeTime": ipsecGlobDefaultIpsecLifeTime,
       "ipsecGlobDefaultIkeLifeTime": ipsecGlobDefaultIkeLifeTime,
       "ipsecGlobDefaultIkeGroup": ipsecGlobDefaultIkeGroup,
       "ipsecGlobMaxSysLogLevel": ipsecGlobMaxSysLogLevel,
       "ipsecGlobDefaultGranularity": ipsecGlobDefaultGranularity,
       "ipsecGlobDefaultPh1Mode": ipsecGlobDefaultPh1Mode,
       "ipsecGlobDefaultPfsGroup": ipsecGlobDefaultPfsGroup,
       "ipsecGlobIkePort": ipsecGlobIkePort,
       "ipsecGlobMaxRetries": ipsecGlobMaxRetries,
       "ipsecGlobRetryTimeout0milli": ipsecGlobRetryTimeout0milli,
       "ipsecGlobRetryTimeoutMaxsec": ipsecGlobRetryTimeoutMaxsec,
       "ipsecGlobMaxNegotiationTimeoutsec": ipsecGlobMaxNegotiationTimeoutsec,
       "ipsecGlobMaxIkeSas": ipsecGlobMaxIkeSas,
       "ipsecGlobAntiCloggingLength": ipsecGlobAntiCloggingLength,
       "ipsecGlobAntiCloggingHash": ipsecGlobAntiCloggingHash,
       "ipsecGlobLocalSecretPeriodsec": ipsecGlobLocalSecretPeriodsec,
       "ipsecGlobIgnoreCrPayloads": ipsecGlobIgnoreCrPayloads,
       "ipsecGlobNoCrPayloads": ipsecGlobNoCrPayloads,
       "ipsecGlobNoKeyHashPayloads": ipsecGlobNoKeyHashPayloads,
       "ipsecGlobNoCrls": ipsecGlobNoCrls,
       "ipsecGlobSendFullCertChains": ipsecGlobSendFullCertChains,
       "ipsecGlobTrustIcmpMsg": ipsecGlobTrustIcmpMsg,
       "ipsecGlobSpiSize": ipsecGlobSpiSize,
       "ipsecGlobZeroIsakmpCookies": ipsecGlobZeroIsakmpCookies,
       "ipsecGlobMaxKeyLength": ipsecGlobMaxKeyLength,
       "ipsecGlobNoInitialContact": ipsecGlobNoInitialContact,
       "ipsecPublicKeyTable": ipsecPublicKeyTable,
       "ipsecPubKeyEntry": ipsecPubKeyEntry,
       "ipsecPubKeyIndex": ipsecPubKeyIndex,
       "ipsecPubKeyDescription": ipsecPubKeyDescription,
       "ipsecPubKeyAlgorithm": ipsecPubKeyAlgorithm,
       "ipsecPubKeyKeyLength": ipsecPubKeyKeyLength,
       "ipsecSaTable": ipsecSaTable,
       "ipsecSaEntry": ipsecSaEntry,
       "ipsecSaIndex": ipsecSaIndex,
       "ipsecSaState": ipsecSaState,
       "ipsecSaCreator": ipsecSaCreator,
       "ipsecSaDir": ipsecSaDir,
       "ipsecSaMode": ipsecSaMode,
       "ipsecSaSecProto": ipsecSaSecProto,
       "ipsecSaLocalIp": ipsecSaLocalIp,
       "ipsecSaPeerIp": ipsecSaPeerIp,
       "ipsecSaSrcAddress": ipsecSaSrcAddress,
       "ipsecSaSrcMaskLen": ipsecSaSrcMaskLen,
       "ipsecSaSrcRange": ipsecSaSrcRange,
       "ipsecSaDstAddress": ipsecSaDstAddress,
       "ipsecSaDstMaskLen": ipsecSaDstMaskLen,
       "ipsecSaDstRange": ipsecSaDstRange,
       "ipsecSaSpi": ipsecSaSpi,
       "ipsecSaAuthAlg": ipsecSaAuthAlg,
       "ipsecSaEncAlg": ipsecSaEncAlg,
       "ipsecSaAuthKeyLen": ipsecSaAuthKeyLen,
       "ipsecSaEncKeyLen": ipsecSaEncKeyLen,
       "ipsecSaLifeSeconds": ipsecSaLifeSeconds,
       "ipsecSaLifeKBytes": ipsecSaLifeKBytes,
       "ipsecSaProto": ipsecSaProto,
       "ipsecSaSrcPort": ipsecSaSrcPort,
       "ipsecSaDstPort": ipsecSaDstPort,
       "ipsecSaSeconds": ipsecSaSeconds,
       "ipsecSaBytes": ipsecSaBytes,
       "ipsecSaPackets": ipsecSaPackets,
       "ipsecSaReplayErrors": ipsecSaReplayErrors,
       "ipsecSaRecvErrors": ipsecSaRecvErrors,
       "ipsecSaDecryptErrors": ipsecSaDecryptErrors,
       "ikeSaTable": ikeSaTable,
       "ikeSaEntry": ikeSaEntry,
       "ikeSaIndex": ikeSaIndex,
       "ikeSaState": ikeSaState,
       "ikeSaXchType": ikeSaXchType,
       "ikeSaAuthMethod": ikeSaAuthMethod,
       "ikeSaAlgs": ikeSaAlgs,
       "ikeSaRole": ikeSaRole,
       "ikeSaLocalId": ikeSaLocalId,
       "ikeSaRemoteId": ikeSaRemoteId,
       "ikeSaRemoteIp": ikeSaRemoteIp,
       "ikeSaCookieI": ikeSaCookieI,
       "ikeSaCookieR": ikeSaCookieR,
       "ikeSaTimes": ikeSaTimes,
       "ikeSaNumCerts": ikeSaNumCerts,
       "ikeSaNumNegotiations": ikeSaNumNegotiations,
       "ikeSaBytes": ikeSaBytes,
       "ikeSaMajVersion": ikeSaMajVersion,
       "ikeSaMinVersion": ikeSaMinVersion,
       "ipsecPeerTable": ipsecPeerTable,
       "ipsecPeerEntry": ipsecPeerEntry,
       "ipsecPeerIndex": ipsecPeerIndex,
       "ipsecPeerNextIndex": ipsecPeerNextIndex,
       "ipsecPeerDescription": ipsecPeerDescription,
       "ipsecPeerPeerIds": ipsecPeerPeerIds,
       "ipsecPeerPeerAddress": ipsecPeerPeerAddress,
       "ipsecPeerLocalId": ipsecPeerLocalId,
       "ipsecPeerLocalAddress": ipsecPeerLocalAddress,
       "ipsecPeerLocalCert": ipsecPeerLocalCert,
       "ipsecPeerIkeProposals": ipsecPeerIkeProposals,
       "ipsecPeerTrafficList": ipsecPeerTrafficList,
       "ipsecPeerAuthMethod": ipsecPeerAuthMethod,
       "ipsecPeerPreSharedKey": ipsecPeerPreSharedKey,
       "ipsecPeerIkeGroup": ipsecPeerIkeGroup,
       "ipsecPeerPfsGroup": ipsecPeerPfsGroup,
       "ipsecPeerPh1Mode": ipsecPeerPh1Mode,
       "ipsecPeerIkeLifeTime": ipsecPeerIkeLifeTime,
       "ipsecPeerIpsecLifeTime": ipsecPeerIpsecLifeTime,
       "ipsecPeerKeepAlive": ipsecPeerKeepAlive,
       "ipsecPeerGranularity": ipsecPeerGranularity,
       "ipsecPeerDontVerifyPad": ipsecPeerDontVerifyPad,
       "ipsecPeerDefaultIpsecProposals": ipsecPeerDefaultIpsecProposals,
       "ipsecPeerPreSharedKeyData": ipsecPeerPreSharedKeyData,
       "ikeProposalTable": ikeProposalTable,
       "ikeProposalEntry": ikeProposalEntry,
       "ikePropIndex": ikePropIndex,
       "ikePropNextChoice": ikePropNextChoice,
       "ikePropDescription": ikePropDescription,
       "ikePropEncAlg": ikePropEncAlg,
       "ikePropHashAlg": ikePropHashAlg,
       "ipsecTrafficTable": ipsecTrafficTable,
       "ipsecTrafficEntry": ipsecTrafficEntry,
       "ipsecTrIndex": ipsecTrIndex,
       "ipsecTrNextIndex": ipsecTrNextIndex,
       "ipsecTrDescription": ipsecTrDescription,
       "ipsecTrLocalAddress": ipsecTrLocalAddress,
       "ipsecTrLocalMaskLen": ipsecTrLocalMaskLen,
       "ipsecTrLocalRange": ipsecTrLocalRange,
       "ipsecTrRemoteAddress": ipsecTrRemoteAddress,
       "ipsecTrRemoteMaskLen": ipsecTrRemoteMaskLen,
       "ipsecTrRemoteRange": ipsecTrRemoteRange,
       "ipsecTrProto": ipsecTrProto,
       "ipsecTrLocalPort": ipsecTrLocalPort,
       "ipsecTrRemotePort": ipsecTrRemotePort,
       "ipsecTrAction": ipsecTrAction,
       "ipsecTrProposal": ipsecTrProposal,
       "ipsecTrForceTunnelMode": ipsecTrForceTunnelMode,
       "ipsecTrLifeTime": ipsecTrLifeTime,
       "ipsecTrGranularity": ipsecTrGranularity,
       "ipsecTrKeepAlive": ipsecTrKeepAlive,
       "ipsecProposalTable": ipsecProposalTable,
       "ipsecProposalEntry": ipsecProposalEntry,
       "ipsecPropIndex": ipsecPropIndex,
       "ipsecPropNext": ipsecPropNext,
       "ipsecPropBoolOp": ipsecPropBoolOp,
       "ipsecPropDescription": ipsecPropDescription,
       "ipsecPropProto": ipsecPropProto,
       "ipsecPropEncAlg": ipsecPropEncAlg,
       "ipsecPropAuthAlg": ipsecPropAuthAlg,
       "ipsecPropLifeTime": ipsecPropLifeTime,
       "ipsecPropInSpi": ipsecPropInSpi,
       "ipsecPropOutSpi": ipsecPropOutSpi,
       "ipsecPropEncKeyIn": ipsecPropEncKeyIn,
       "ipsecPropEncKeyOut": ipsecPropEncKeyOut,
       "ipsecPropAuthKeyIn": ipsecPropAuthKeyIn,
       "ipsecPropAuthKeyOut": ipsecPropAuthKeyOut,
       "ipsecPropEncKeyDataIn": ipsecPropEncKeyDataIn,
       "ipsecPropEncKeyDataOut": ipsecPropEncKeyDataOut,
       "ipsecPropAuthKeyDataIn": ipsecPropAuthKeyDataIn,
       "ipsecPropAuthKeyDataOut": ipsecPropAuthKeyDataOut,
       "ipsecLifeTimeTable": ipsecLifeTimeTable,
       "ipsecLifeTimeEntry": ipsecLifeTimeEntry,
       "ipsecLifeIndex": ipsecLifeIndex,
       "ipsecLifeType": ipsecLifeType,
       "ipsecLifeSoftKb": ipsecLifeSoftKb,
       "ipsecLifeSoftSec": ipsecLifeSoftSec,
       "ipsecLifeHardKb": ipsecLifeHardKb,
       "ipsecLifeHardSec": ipsecLifeHardSec,
       "ipsecStats": ipsecStats,
       "ipsecStatsCurrentIkeSas": ipsecStatsCurrentIkeSas,
       "ipsecStatsCurrentIpsecSas": ipsecStatsCurrentIpsecSas,
       "ipsecStatsIp": ipsecStatsIp,
       "ipsecStatsNonIp": ipsecStatsNonIp,
       "ipsecStatsAh": ipsecStatsAh,
       "ipsecStatsEsp": ipsecStatsEsp,
       "ipsecStatsDrop": ipsecStatsDrop,
       "ipsecStatsPass": ipsecStatsPass,
       "ipsecStatsTrig": ipsecStatsTrig,
       "ipsecStatsFragPkt": ipsecStatsFragPkt,
       "ipsecStatsFragBytes": ipsecStatsFragBytes,
       "ipsecStatsFragNonfirst": ipsecStatsFragNonfirst,
       "ipsecGlobalsContinued": ipsecGlobalsContinued,
       "ipsecGlobContPreIpsecRules": ipsecGlobContPreIpsecRules,
       "ipsecGlobContDefaultRule": ipsecGlobContDefaultRule}
)
