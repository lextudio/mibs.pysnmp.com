# SNMP MIB module (HH3C-NDEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NDEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:19 2024
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

(hh3cmlsr,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cmlsr")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cNDEC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2)
)
hh3cNDEC.setRevisions(
        ("2004-09-15 10:52",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3chipsNDECSAListTable_Object = MibTable
hh3chipsNDECSAListTable = _Hh3chipsNDECSAListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1)
)
if mibBuilder.loadTexts:
    hh3chipsNDECSAListTable.setStatus("current")
_Hh3chipsNDECSAListEntry_Object = MibTableRow
hh3chipsNDECSAListEntry = _Hh3chipsNDECSAListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1)
)
hh3chipsNDECSAListEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chipsPeerIpAddr"),
    (0, "HH3C-NDEC-MIB", "hh3chipsProtocol"),
    (0, "HH3C-NDEC-MIB", "hh3chipsSPI"),
)
if mibBuilder.loadTexts:
    hh3chipsNDECSAListEntry.setStatus("current")
_Hh3chipsPeerIpAddr_Type = IpAddress
_Hh3chipsPeerIpAddr_Object = MibTableColumn
hh3chipsPeerIpAddr = _Hh3chipsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 1),
    _Hh3chipsPeerIpAddr_Type()
)
hh3chipsPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsPeerIpAddr.setStatus("current")


class _Hh3chipsProtocol_Type(Integer32):
    """Custom type hh3chipsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("ipsecAh", 51),
          ("ipsecEsp", 50))
    )


_Hh3chipsProtocol_Type.__name__ = "Integer32"
_Hh3chipsProtocol_Object = MibTableColumn
hh3chipsProtocol = _Hh3chipsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 2),
    _Hh3chipsProtocol_Type()
)
hh3chipsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsProtocol.setStatus("current")


class _Hh3chipsSPI_Type(Gauge32):
    """Custom type hh3chipsSPI based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_Hh3chipsSPI_Type.__name__ = "Gauge32"
_Hh3chipsSPI_Object = MibTableColumn
hh3chipsSPI = _Hh3chipsSPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 3),
    _Hh3chipsSPI_Type()
)
hh3chipsSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsSPI.setStatus("current")


class _Hh3chipsEncAlgorithm_Type(Integer32):
    """Custom type hh3chipsEncAlgorithm based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ealg3desCbc", 3),
          ("ealgDescbc", 2),
          ("ealgNone", 1),
          ("ealgXAes", 7),
          ("ealgXBlf", 4),
          ("ealgXCast", 5),
          ("ealgXNsa", 9),
          ("ealgXQc5", 8),
          ("ealgXSkipjack", 6))
    )


_Hh3chipsEncAlgorithm_Type.__name__ = "Integer32"
_Hh3chipsEncAlgorithm_Object = MibTableColumn
hh3chipsEncAlgorithm = _Hh3chipsEncAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 4),
    _Hh3chipsEncAlgorithm_Type()
)
hh3chipsEncAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsEncAlgorithm.setStatus("current")


class _Hh3chipsAuthAlgorithm_Type(Integer32):
    """Custom type hh3chipsAuthAlgorithm based on Integer32"""
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
        *(("aalgMd5Hmac", 2),
          ("aalgMd5Hmac96", 4),
          ("aalgNone", 1),
          ("aalgSha1Hmac", 3),
          ("aalgSha1Hmac96", 5),
          ("aalgXMd5", 7),
          ("aalgXRipeMd160Hmac96", 6),
          ("aalgXSha1", 8))
    )


_Hh3chipsAuthAlgorithm_Type.__name__ = "Integer32"
_Hh3chipsAuthAlgorithm_Object = MibTableColumn
hh3chipsAuthAlgorithm = _Hh3chipsAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 5),
    _Hh3chipsAuthAlgorithm_Type()
)
hh3chipsAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsAuthAlgorithm.setStatus("current")
_Hh3chipsLocalIpAddr_Type = IpAddress
_Hh3chipsLocalIpAddr_Object = MibTableColumn
hh3chipsLocalIpAddr = _Hh3chipsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 6),
    _Hh3chipsLocalIpAddr_Type()
)
hh3chipsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsLocalIpAddr.setStatus("current")
_Hh3chipsSaLifeKBytes_Type = Gauge32
_Hh3chipsSaLifeKBytes_Object = MibTableColumn
hh3chipsSaLifeKBytes = _Hh3chipsSaLifeKBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 7),
    _Hh3chipsSaLifeKBytes_Type()
)
hh3chipsSaLifeKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsSaLifeKBytes.setStatus("current")
_Hh3chipsSaLifeSecond_Type = Gauge32
_Hh3chipsSaLifeSecond_Object = MibTableColumn
hh3chipsSaLifeSecond = _Hh3chipsSaLifeSecond_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 8),
    _Hh3chipsSaLifeSecond_Type()
)
hh3chipsSaLifeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsSaLifeSecond.setStatus("current")
_Hh3chipsByCard_Type = TruthValue
_Hh3chipsByCard_Object = MibTableColumn
hh3chipsByCard = _Hh3chipsByCard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 9),
    _Hh3chipsByCard_Type()
)
hh3chipsByCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsByCard.setStatus("current")


class _Hh3chipsNegotiateSaMode_Type(Integer32):
    """Custom type hh3chipsNegotiateSaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isakmp", 2),
          ("manual", 3),
          ("none", 1))
    )


_Hh3chipsNegotiateSaMode_Type.__name__ = "Integer32"
_Hh3chipsNegotiateSaMode_Object = MibTableColumn
hh3chipsNegotiateSaMode = _Hh3chipsNegotiateSaMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 10),
    _Hh3chipsNegotiateSaMode_Type()
)
hh3chipsNegotiateSaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsNegotiateSaMode.setStatus("current")
_Hh3chipsExpBytes_Type = Gauge32
_Hh3chipsExpBytes_Object = MibTableColumn
hh3chipsExpBytes = _Hh3chipsExpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 11),
    _Hh3chipsExpBytes_Type()
)
hh3chipsExpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsExpBytes.setStatus("current")
_Hh3chipsSoftBytes_Type = Gauge32
_Hh3chipsSoftBytes_Object = MibTableColumn
hh3chipsSoftBytes = _Hh3chipsSoftBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 12),
    _Hh3chipsSoftBytes_Type()
)
hh3chipsSoftBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsSoftBytes.setStatus("current")
_Hh3chipsExpTimeout_Type = Gauge32
_Hh3chipsExpTimeout_Object = MibTableColumn
hh3chipsExpTimeout = _Hh3chipsExpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 13),
    _Hh3chipsExpTimeout_Type()
)
hh3chipsExpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsExpTimeout.setStatus("current")
_Hh3chipsSoftTimeout_Type = Gauge32
_Hh3chipsSoftTimeout_Object = MibTableColumn
hh3chipsSoftTimeout = _Hh3chipsSoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 1, 1, 14),
    _Hh3chipsSoftTimeout_Type()
)
hh3chipsSoftTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsSoftTimeout.setStatus("current")
_Hh3chikeSATable_Object = MibTable
hh3chikeSATable = _Hh3chikeSATable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2)
)
if mibBuilder.loadTexts:
    hh3chikeSATable.setStatus("current")
_Hh3chikeSAEntry_Object = MibTableRow
hh3chikeSAEntry = _Hh3chikeSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1)
)
hh3chikeSAEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chikeConnId"),
)
if mibBuilder.loadTexts:
    hh3chikeSAEntry.setStatus("current")


class _Hh3chikeConnId_Type(Integer32):
    """Custom type hh3chikeConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chikeConnId_Type.__name__ = "Integer32"
_Hh3chikeConnId_Object = MibTableColumn
hh3chikeConnId = _Hh3chikeConnId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 1),
    _Hh3chikeConnId_Type()
)
hh3chikeConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chikeConnId.setStatus("current")
_Hh3chikePeerIpAddr_Type = IpAddress
_Hh3chikePeerIpAddr_Object = MibTableColumn
hh3chikePeerIpAddr = _Hh3chikePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 2),
    _Hh3chikePeerIpAddr_Type()
)
hh3chikePeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chikePeerIpAddr.setStatus("current")
_Hh3chikeFlag_Type = DisplayString
_Hh3chikeFlag_Object = MibTableColumn
hh3chikeFlag = _Hh3chikeFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 3),
    _Hh3chikeFlag_Type()
)
hh3chikeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chikeFlag.setStatus("current")


class _Hh3chikePhase_Type(Integer32):
    """Custom type hh3chikePhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 2),
          ("phase2", 3),
          ("unkown", 1))
    )


_Hh3chikePhase_Type.__name__ = "Integer32"
_Hh3chikePhase_Object = MibTableColumn
hh3chikePhase = _Hh3chikePhase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 4),
    _Hh3chikePhase_Type()
)
hh3chikePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chikePhase.setStatus("current")


class _Hh3chikeDoi_Type(Integer32):
    """Custom type hh3chikeDoi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 2),
          ("unkown", 1))
    )


_Hh3chikeDoi_Type.__name__ = "Integer32"
_Hh3chikeDoi_Object = MibTableColumn
hh3chikeDoi = _Hh3chikeDoi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 5),
    _Hh3chikeDoi_Type()
)
hh3chikeDoi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chikeDoi.setStatus("current")
_Hh3chikeClearSA_Type = TruthValue
_Hh3chikeClearSA_Object = MibTableColumn
hh3chikeClearSA = _Hh3chikeClearSA_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 2, 1, 6),
    _Hh3chikeClearSA_Type()
)
hh3chikeClearSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chikeClearSA.setStatus("current")
_Hh3chipsIKEPolicyTable_Object = MibTable
hh3chipsIKEPolicyTable = _Hh3chipsIKEPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3)
)
if mibBuilder.loadTexts:
    hh3chipsIKEPolicyTable.setStatus("current")
_Hh3chipsIKEPolicyEntry_Object = MibTableRow
hh3chipsIKEPolicyEntry = _Hh3chipsIKEPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1)
)
hh3chipsIKEPolicyEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chipsIsakmpPolPriority"),
)
if mibBuilder.loadTexts:
    hh3chipsIKEPolicyEntry.setStatus("current")


class _Hh3chipsIsakmpPolPriority_Type(Integer32):
    """Custom type hh3chipsIsakmpPolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chipsIsakmpPolPriority_Type.__name__ = "Integer32"
_Hh3chipsIsakmpPolPriority_Object = MibTableColumn
hh3chipsIsakmpPolPriority = _Hh3chipsIsakmpPolPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 1),
    _Hh3chipsIsakmpPolPriority_Type()
)
hh3chipsIsakmpPolPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolPriority.setStatus("current")


class _Hh3chipsIsakmpPolEncr_Type(Integer32):
    """Custom type hh3chipsIsakmpPolEncr based on Integer32"""
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
        *(("ikeEncrypt3DesCbc", 6),
          ("ikeEncryptBlowfishcbc", 4),
          ("ikeEncryptCastCbc", 7),
          ("ikeEncryptDesCbc", 2),
          ("ikeEncryptIdeaCbc", 3),
          ("ikeEncryptNone", 1),
          ("ikeEncryptRc5R16B64cbc", 5))
    )


_Hh3chipsIsakmpPolEncr_Type.__name__ = "Integer32"
_Hh3chipsIsakmpPolEncr_Object = MibTableColumn
hh3chipsIsakmpPolEncr = _Hh3chipsIsakmpPolEncr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 2),
    _Hh3chipsIsakmpPolEncr_Type()
)
hh3chipsIsakmpPolEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolEncr.setStatus("current")


class _Hh3chipsIsakmpPolHash_Type(Integer32):
    """Custom type hh3chipsIsakmpPolHash based on Integer32"""
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
        *(("ikeHashMd5", 2),
          ("ikeHashNone", 1),
          ("ikeHashSha", 3),
          ("ikeHashTiger", 4))
    )


_Hh3chipsIsakmpPolHash_Type.__name__ = "Integer32"
_Hh3chipsIsakmpPolHash_Object = MibTableColumn
hh3chipsIsakmpPolHash = _Hh3chipsIsakmpPolHash_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 3),
    _Hh3chipsIsakmpPolHash_Type()
)
hh3chipsIsakmpPolHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolHash.setStatus("current")


class _Hh3chipsIsakmpPolAuth_Type(Integer32):
    """Custom type hh3chipsIsakmpPolAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ikeAuthDss", 3),
          ("ikeAuthPreNone", 1),
          ("ikeAuthPreShared", 2),
          ("ikeAuthRsaEnc", 5),
          ("ikeAuthRsaEncRev", 6),
          ("ikeAuthRsaSig", 4))
    )


_Hh3chipsIsakmpPolAuth_Type.__name__ = "Integer32"
_Hh3chipsIsakmpPolAuth_Object = MibTableColumn
hh3chipsIsakmpPolAuth = _Hh3chipsIsakmpPolAuth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 4),
    _Hh3chipsIsakmpPolAuth_Type()
)
hh3chipsIsakmpPolAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolAuth.setStatus("current")


class _Hh3chipsIsakmpPolGroup_Type(Integer32):
    """Custom type hh3chipsIsakmpPolGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhGroup1", 2),
          ("dhGroup2", 3),
          ("none", 1))
    )


_Hh3chipsIsakmpPolGroup_Type.__name__ = "Integer32"
_Hh3chipsIsakmpPolGroup_Object = MibTableColumn
hh3chipsIsakmpPolGroup = _Hh3chipsIsakmpPolGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 5),
    _Hh3chipsIsakmpPolGroup_Type()
)
hh3chipsIsakmpPolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolGroup.setStatus("current")
_Hh3chipsIsakmpPolLifetime_Type = Gauge32
_Hh3chipsIsakmpPolLifetime_Object = MibTableColumn
hh3chipsIsakmpPolLifetime = _Hh3chipsIsakmpPolLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 3, 1, 6),
    _Hh3chipsIsakmpPolLifetime_Type()
)
hh3chipsIsakmpPolLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsakmpPolLifetime.setStatus("current")
_Hh3chipsStaticCryptomapTable_Object = MibTable
hh3chipsStaticCryptomapTable = _Hh3chipsStaticCryptomapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4)
)
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapTable.setStatus("current")
_Hh3chipsStaticCryptomapEntry_Object = MibTableRow
hh3chipsStaticCryptomapEntry = _Hh3chipsStaticCryptomapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1)
)
hh3chipsStaticCryptomapEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chipsStaticCryptomapName"),
    (0, "HH3C-NDEC-MIB", "hh3chipsStaticCryptomapSN"),
)
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapEntry.setStatus("current")
_Hh3chipsStaticCryptomapName_Type = DisplayString
_Hh3chipsStaticCryptomapName_Object = MibTableColumn
hh3chipsStaticCryptomapName = _Hh3chipsStaticCryptomapName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 1),
    _Hh3chipsStaticCryptomapName_Type()
)
hh3chipsStaticCryptomapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapName.setStatus("current")


class _Hh3chipsStaticCryptomapSN_Type(Integer32):
    """Custom type hh3chipsStaticCryptomapSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3chipsStaticCryptomapSN_Type.__name__ = "Integer32"
_Hh3chipsStaticCryptomapSN_Object = MibTableColumn
hh3chipsStaticCryptomapSN = _Hh3chipsStaticCryptomapSN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 2),
    _Hh3chipsStaticCryptomapSN_Type()
)
hh3chipsStaticCryptomapSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapSN.setStatus("current")


class _Hh3chipsStaticCryptomapNegMode_Type(Integer32):
    """Custom type hh3chipsStaticCryptomapNegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isakmp", 2),
          ("manual", 3),
          ("none", 1))
    )


_Hh3chipsStaticCryptomapNegMode_Type.__name__ = "Integer32"
_Hh3chipsStaticCryptomapNegMode_Object = MibTableColumn
hh3chipsStaticCryptomapNegMode = _Hh3chipsStaticCryptomapNegMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 3),
    _Hh3chipsStaticCryptomapNegMode_Type()
)
hh3chipsStaticCryptomapNegMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapNegMode.setStatus("current")


class _Hh3chipsStaticCryptomapMatchAddr_Type(Integer32):
    """Custom type hh3chipsStaticCryptomapMatchAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Hh3chipsStaticCryptomapMatchAddr_Type.__name__ = "Integer32"
_Hh3chipsStaticCryptomapMatchAddr_Object = MibTableColumn
hh3chipsStaticCryptomapMatchAddr = _Hh3chipsStaticCryptomapMatchAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 4),
    _Hh3chipsStaticCryptomapMatchAddr_Type()
)
hh3chipsStaticCryptomapMatchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapMatchAddr.setStatus("current")
_Hh3chipsStaticCryptomapPeerIpAddr_Type = IpAddress
_Hh3chipsStaticCryptomapPeerIpAddr_Object = MibTableColumn
hh3chipsStaticCryptomapPeerIpAddr = _Hh3chipsStaticCryptomapPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 5),
    _Hh3chipsStaticCryptomapPeerIpAddr_Type()
)
hh3chipsStaticCryptomapPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapPeerIpAddr.setStatus("current")
_Hh3chipsStaticCryptomapTransforName_Type = DisplayString
_Hh3chipsStaticCryptomapTransforName_Object = MibTableColumn
hh3chipsStaticCryptomapTransforName = _Hh3chipsStaticCryptomapTransforName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 6),
    _Hh3chipsStaticCryptomapTransforName_Type()
)
hh3chipsStaticCryptomapTransforName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapTransforName.setStatus("current")
_Hh3chipsStaticCryptomapLifetime_Type = Gauge32
_Hh3chipsStaticCryptomapLifetime_Object = MibTableColumn
hh3chipsStaticCryptomapLifetime = _Hh3chipsStaticCryptomapLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 7),
    _Hh3chipsStaticCryptomapLifetime_Type()
)
hh3chipsStaticCryptomapLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapLifetime.setStatus("current")
_Hh3chipsStaticCryptomapLifesize_Type = Gauge32
_Hh3chipsStaticCryptomapLifesize_Object = MibTableColumn
hh3chipsStaticCryptomapLifesize = _Hh3chipsStaticCryptomapLifesize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 8),
    _Hh3chipsStaticCryptomapLifesize_Type()
)
hh3chipsStaticCryptomapLifesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapLifesize.setStatus("current")
_Hh3chipsStaticCryptomapLocalIpAddr_Type = IpAddress
_Hh3chipsStaticCryptomapLocalIpAddr_Object = MibTableColumn
hh3chipsStaticCryptomapLocalIpAddr = _Hh3chipsStaticCryptomapLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 9),
    _Hh3chipsStaticCryptomapLocalIpAddr_Type()
)
hh3chipsStaticCryptomapLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsStaticCryptomapLocalIpAddr.setStatus("current")
_Hh3chipsIfNameUsed_Type = DisplayString
_Hh3chipsIfNameUsed_Object = MibTableColumn
hh3chipsIfNameUsed = _Hh3chipsIfNameUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 10),
    _Hh3chipsIfNameUsed_Type()
)
hh3chipsIfNameUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIfNameUsed.setStatus("current")
_Hh3chipsInAHSPI_Type = Gauge32
_Hh3chipsInAHSPI_Object = MibTableColumn
hh3chipsInAHSPI = _Hh3chipsInAHSPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 11),
    _Hh3chipsInAHSPI_Type()
)
hh3chipsInAHSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInAHSPI.setStatus("current")
_Hh3chipsInESPSPI_Type = Gauge32
_Hh3chipsInESPSPI_Object = MibTableColumn
hh3chipsInESPSPI = _Hh3chipsInESPSPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 12),
    _Hh3chipsInESPSPI_Type()
)
hh3chipsInESPSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInESPSPI.setStatus("current")
_Hh3chipsOutAHSPI_Type = Gauge32
_Hh3chipsOutAHSPI_Object = MibTableColumn
hh3chipsOutAHSPI = _Hh3chipsOutAHSPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 13),
    _Hh3chipsOutAHSPI_Type()
)
hh3chipsOutAHSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutAHSPI.setStatus("current")
_Hh3chipsOutESPSPI_Type = Gauge32
_Hh3chipsOutESPSPI_Object = MibTableColumn
hh3chipsOutESPSPI = _Hh3chipsOutESPSPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 14),
    _Hh3chipsOutESPSPI_Type()
)
hh3chipsOutESPSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutESPSPI.setStatus("current")
_Hh3chipsInAhHexKeyString_Type = DisplayString
_Hh3chipsInAhHexKeyString_Object = MibTableColumn
hh3chipsInAhHexKeyString = _Hh3chipsInAhHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 15),
    _Hh3chipsInAhHexKeyString_Type()
)
hh3chipsInAhHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInAhHexKeyString.setStatus("current")
_Hh3chipsInEspCipherHexKeyString_Type = DisplayString
_Hh3chipsInEspCipherHexKeyString_Object = MibTableColumn
hh3chipsInEspCipherHexKeyString = _Hh3chipsInEspCipherHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 16),
    _Hh3chipsInEspCipherHexKeyString_Type()
)
hh3chipsInEspCipherHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInEspCipherHexKeyString.setStatus("current")
_Hh3chipsInEspAuthenHexKeyString_Type = DisplayString
_Hh3chipsInEspAuthenHexKeyString_Object = MibTableColumn
hh3chipsInEspAuthenHexKeyString = _Hh3chipsInEspAuthenHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 17),
    _Hh3chipsInEspAuthenHexKeyString_Type()
)
hh3chipsInEspAuthenHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInEspAuthenHexKeyString.setStatus("current")
_Hh3chipsInAhStringKeyString_Type = DisplayString
_Hh3chipsInAhStringKeyString_Object = MibTableColumn
hh3chipsInAhStringKeyString = _Hh3chipsInAhStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 18),
    _Hh3chipsInAhStringKeyString_Type()
)
hh3chipsInAhStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInAhStringKeyString.setStatus("current")
_Hh3chipsInEspStringKeyString_Type = DisplayString
_Hh3chipsInEspStringKeyString_Object = MibTableColumn
hh3chipsInEspStringKeyString = _Hh3chipsInEspStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 19),
    _Hh3chipsInEspStringKeyString_Type()
)
hh3chipsInEspStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInEspStringKeyString.setStatus("current")
_Hh3chipsOutAhHexKeyString_Type = DisplayString
_Hh3chipsOutAhHexKeyString_Object = MibTableColumn
hh3chipsOutAhHexKeyString = _Hh3chipsOutAhHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 20),
    _Hh3chipsOutAhHexKeyString_Type()
)
hh3chipsOutAhHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutAhHexKeyString.setStatus("current")
_Hh3chipsOutEspCipherHexKeyString_Type = DisplayString
_Hh3chipsOutEspCipherHexKeyString_Object = MibTableColumn
hh3chipsOutEspCipherHexKeyString = _Hh3chipsOutEspCipherHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 21),
    _Hh3chipsOutEspCipherHexKeyString_Type()
)
hh3chipsOutEspCipherHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutEspCipherHexKeyString.setStatus("current")
_Hh3chipsOutEspAuthenHexKeyString_Type = DisplayString
_Hh3chipsOutEspAuthenHexKeyString_Object = MibTableColumn
hh3chipsOutEspAuthenHexKeyString = _Hh3chipsOutEspAuthenHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 22),
    _Hh3chipsOutEspAuthenHexKeyString_Type()
)
hh3chipsOutEspAuthenHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutEspAuthenHexKeyString.setStatus("current")
_Hh3chipsOutAhStringKeyString_Type = DisplayString
_Hh3chipsOutAhStringKeyString_Object = MibTableColumn
hh3chipsOutAhStringKeyString = _Hh3chipsOutAhStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 23),
    _Hh3chipsOutAhStringKeyString_Type()
)
hh3chipsOutAhStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutAhStringKeyString.setStatus("current")
_Hh3chipsOutEspStringKeyString_Type = DisplayString
_Hh3chipsOutEspStringKeyString_Object = MibTableColumn
hh3chipsOutEspStringKeyString = _Hh3chipsOutEspStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 4, 1, 24),
    _Hh3chipsOutEspStringKeyString_Type()
)
hh3chipsOutEspStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutEspStringKeyString.setStatus("current")
_Hh3chipsTransformNameSetTable_Object = MibTable
hh3chipsTransformNameSetTable = _Hh3chipsTransformNameSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5)
)
if mibBuilder.loadTexts:
    hh3chipsTransformNameSetTable.setStatus("current")
_Hh3chipsTransformNameSetEntry_Object = MibTableRow
hh3chipsTransformNameSetEntry = _Hh3chipsTransformNameSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1)
)
hh3chipsTransformNameSetEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chipsTransformName"),
)
if mibBuilder.loadTexts:
    hh3chipsTransformNameSetEntry.setStatus("current")
_Hh3chipsTransformName_Type = DisplayString
_Hh3chipsTransformName_Object = MibTableColumn
hh3chipsTransformName = _Hh3chipsTransformName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 1),
    _Hh3chipsTransformName_Type()
)
hh3chipsTransformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsTransformName.setStatus("current")


class _Hh3chipsTransformMode_Type(Integer32):
    """Custom type hh3chipsTransformMode based on Integer32"""
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


_Hh3chipsTransformMode_Type.__name__ = "Integer32"
_Hh3chipsTransformMode_Object = MibTableColumn
hh3chipsTransformMode = _Hh3chipsTransformMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 2),
    _Hh3chipsTransformMode_Type()
)
hh3chipsTransformMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsTransformMode.setStatus("current")


class _Hh3chipsTransformProtocol_Type(Integer32):
    """Custom type hh3chipsTransformProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ipsecAhEspNew", 3),
          ("ipsecAhEspOld", 4),
          ("ipsecAhNew", 2),
          ("ipsecAhOld", 5),
          ("ipsecEspAhNew", 7),
          ("ipsecEspAhOld", 8),
          ("ipsecEspNew", 6),
          ("ipsecEspOld", 9),
          ("ipsecNone", 1))
    )


_Hh3chipsTransformProtocol_Type.__name__ = "Integer32"
_Hh3chipsTransformProtocol_Object = MibTableColumn
hh3chipsTransformProtocol = _Hh3chipsTransformProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 3),
    _Hh3chipsTransformProtocol_Type()
)
hh3chipsTransformProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsTransformProtocol.setStatus("current")


class _Hh3chipsAH_Type(Integer32):
    """Custom type hh3chipsAH based on Integer32"""
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
        *(("aalgMd5Hmac", 2),
          ("aalgMd5Hmac96", 4),
          ("aalgNone", 1),
          ("aalgSha1Hmac", 3),
          ("aalgSha1Hmac96", 5),
          ("aalgXMd5", 7),
          ("aalgXRipeMd160Hmac96", 6),
          ("aalgXSha1", 8))
    )


_Hh3chipsAH_Type.__name__ = "Integer32"
_Hh3chipsAH_Object = MibTableColumn
hh3chipsAH = _Hh3chipsAH_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 4),
    _Hh3chipsAH_Type()
)
hh3chipsAH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsAH.setStatus("current")


class _Hh3chipsEespEn_Type(Integer32):
    """Custom type hh3chipsEespEn based on Integer32"""
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
        *(("ealg3desCbc", 3),
          ("ealgDescbc", 2),
          ("ealgNone", 1),
          ("ealgXAes", 7),
          ("ealgXBlf", 4),
          ("ealgXCast", 5),
          ("ealgXQc5", 8),
          ("ealgXSkipjack", 6))
    )


_Hh3chipsEespEn_Type.__name__ = "Integer32"
_Hh3chipsEespEn_Object = MibTableColumn
hh3chipsEespEn = _Hh3chipsEespEn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 5),
    _Hh3chipsEespEn_Type()
)
hh3chipsEespEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsEespEn.setStatus("current")


class _Hh3chipsEspAu_Type(Integer32):
    """Custom type hh3chipsEspAu based on Integer32"""
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
        *(("aalgMd5Hmac", 2),
          ("aalgMd5Hmac96", 4),
          ("aalgNone", 1),
          ("aalgSha1Hmac", 3),
          ("aalgSha1Hmac96", 5),
          ("aalgXMd5", 7),
          ("aalgXRipeMd160Hmac96", 6),
          ("aalgXSha1", 8))
    )


_Hh3chipsEspAu_Type.__name__ = "Integer32"
_Hh3chipsEspAu_Object = MibTableColumn
hh3chipsEspAu = _Hh3chipsEspAu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 6),
    _Hh3chipsEspAu_Type()
)
hh3chipsEspAu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsEspAu.setStatus("current")
_Hh3chipsIsCardTransform_Type = TruthValue
_Hh3chipsIsCardTransform_Object = MibTableColumn
hh3chipsIsCardTransform = _Hh3chipsIsCardTransform_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 5, 1, 7),
    _Hh3chipsIsCardTransform_Type()
)
hh3chipsIsCardTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsIsCardTransform.setStatus("current")
_Hh3chipsNDECInfoTable_Object = MibTable
hh3chipsNDECInfoTable = _Hh3chipsNDECInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6)
)
if mibBuilder.loadTexts:
    hh3chipsNDECInfoTable.setStatus("current")
_Hh3chipsNDECInfoEntry_Object = MibTableRow
hh3chipsNDECInfoEntry = _Hh3chipsNDECInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1)
)
hh3chipsNDECInfoEntry.setIndexNames(
    (0, "HH3C-NDEC-MIB", "hh3chipsCardSlot"),
)
if mibBuilder.loadTexts:
    hh3chipsNDECInfoEntry.setStatus("current")


class _Hh3chipsCardSlot_Type(Integer32):
    """Custom type hh3chipsCardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3chipsCardSlot_Type.__name__ = "Integer32"
_Hh3chipsCardSlot_Object = MibTableColumn
hh3chipsCardSlot = _Hh3chipsCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 1),
    _Hh3chipsCardSlot_Type()
)
hh3chipsCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsCardSlot.setStatus("current")
_Hh3chipsInPac_Type = Counter32
_Hh3chipsInPac_Object = MibTableColumn
hh3chipsInPac = _Hh3chipsInPac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 2),
    _Hh3chipsInPac_Type()
)
hh3chipsInPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInPac.setStatus("current")
_Hh3chipsOutPac_Type = Counter32
_Hh3chipsOutPac_Object = MibTableColumn
hh3chipsOutPac = _Hh3chipsOutPac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 3),
    _Hh3chipsOutPac_Type()
)
hh3chipsOutPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutPac.setStatus("current")
_Hh3chipsInByte_Type = Counter32
_Hh3chipsInByte_Object = MibTableColumn
hh3chipsInByte = _Hh3chipsInByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 4),
    _Hh3chipsInByte_Type()
)
hh3chipsInByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsInByte.setStatus("current")
_Hh3chipsOutByte_Type = Counter32
_Hh3chipsOutByte_Object = MibTableColumn
hh3chipsOutByte = _Hh3chipsOutByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 5),
    _Hh3chipsOutByte_Type()
)
hh3chipsOutByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsOutByte.setStatus("current")
_Hh3chipsDropPac_Type = Counter32
_Hh3chipsDropPac_Object = MibTableColumn
hh3chipsDropPac = _Hh3chipsDropPac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 6),
    _Hh3chipsDropPac_Type()
)
hh3chipsDropPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsDropPac.setStatus("current")


class _Hh3chipsCardStatus_Type(Integer32):
    """Custom type hh3chipsCardStatus based on Integer32"""
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
        *(("ecStateDisable", 5),
          ("ecStateInvalid", 1),
          ("ecStateProgramUpdating", 4),
          ("ecStateReady", 2),
          ("ecStateResetting", 3))
    )


_Hh3chipsCardStatus_Type.__name__ = "Integer32"
_Hh3chipsCardStatus_Object = MibTableColumn
hh3chipsCardStatus = _Hh3chipsCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 7),
    _Hh3chipsCardStatus_Type()
)
hh3chipsCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsCardStatus.setStatus("current")
_Hh3chipsCardHardVer_Type = DisplayString
_Hh3chipsCardHardVer_Object = MibTableColumn
hh3chipsCardHardVer = _Hh3chipsCardHardVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 8),
    _Hh3chipsCardHardVer_Type()
)
hh3chipsCardHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsCardHardVer.setStatus("current")
_Hh3chipsCardSoftVer_Type = DisplayString
_Hh3chipsCardSoftVer_Object = MibTableColumn
hh3chipsCardSoftVer = _Hh3chipsCardSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 9),
    _Hh3chipsCardSoftVer_Type()
)
hh3chipsCardSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsCardSoftVer.setStatus("current")
_Hh3chipsCardCPLDVer_Type = DisplayString
_Hh3chipsCardCPLDVer_Object = MibTableColumn
hh3chipsCardCPLDVer = _Hh3chipsCardCPLDVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 10),
    _Hh3chipsCardCPLDVer_Type()
)
hh3chipsCardCPLDVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsCardCPLDVer.setStatus("current")


class _Hh3chipsCardOperate_Type(Integer32):
    """Custom type hh3chipsCardOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cardClearStatic", 1),
          ("cardReset", 2),
          ("cardSynTime", 3),
          ("cardSysLogClear", 6),
          ("cardSysLogOff", 5),
          ("cardSysLogOn", 4))
    )


_Hh3chipsCardOperate_Type.__name__ = "Integer32"
_Hh3chipsCardOperate_Object = MibTableColumn
hh3chipsCardOperate = _Hh3chipsCardOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 11),
    _Hh3chipsCardOperate_Type()
)
hh3chipsCardOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chipsCardOperate.setStatus("current")
_Hh3chipsDropPacInUnitTime_Type = Gauge32
_Hh3chipsDropPacInUnitTime_Object = MibTableColumn
hh3chipsDropPacInUnitTime = _Hh3chipsDropPacInUnitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 6, 1, 12),
    _Hh3chipsDropPacInUnitTime_Type()
)
hh3chipsDropPacInUnitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsDropPacInUnitTime.setStatus("current")
_Hh3chipsNDECLeaf_ObjectIdentity = ObjectIdentity
hh3chipsNDECLeaf = _Hh3chipsNDECLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 7)
)
_Hh3chipsNDECConnections_Type = Integer32
_Hh3chipsNDECConnections_Object = MibScalar
hh3chipsNDECConnections = _Hh3chipsNDECConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 7, 1),
    _Hh3chipsNDECConnections_Type()
)
hh3chipsNDECConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3chipsNDECConnections.setStatus("current")
_Hh3chipsNDECBackup_Type = Integer32
_Hh3chipsNDECBackup_Object = MibScalar
hh3chipsNDECBackup = _Hh3chipsNDECBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 7, 2),
    _Hh3chipsNDECBackup_Type()
)
hh3chipsNDECBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3chipsNDECBackup.setStatus("current")
_Hh3chipsTraps_ObjectIdentity = ObjectIdentity
hh3chipsTraps = _Hh3chipsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 8)
)

# Managed Objects groups


# Notification objects

hh3chipsNDECNormalResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 8, 1)
)
hh3chipsNDECNormalResetTrap.setObjects(
      *(("HH3C-NDEC-MIB", "hh3chipsCardSlot"),
        ("HH3C-NDEC-MIB", "hh3chipsCardHardVer"),
        ("HH3C-NDEC-MIB", "hh3chipsCardSoftVer"),
        ("HH3C-NDEC-MIB", "hh3chipsCardCPLDVer"))
)
if mibBuilder.loadTexts:
    hh3chipsNDECNormalResetTrap.setStatus(
        "current"
    )

hh3chipsNDECStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 8, 2)
)
hh3chipsNDECStateChangeTrap.setObjects(
      *(("HH3C-NDEC-MIB", "hh3chipsCardSlot"),
        ("HH3C-NDEC-MIB", "hh3chipsCardStatus"))
)
if mibBuilder.loadTexts:
    hh3chipsNDECStateChangeTrap.setStatus(
        "current"
    )

hh3chipsNDECFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2, 8, 3)
)
hh3chipsNDECFlowTrap.setObjects(
      *(("HH3C-NDEC-MIB", "hh3chipsCardSlot"),
        ("HH3C-NDEC-MIB", "hh3chipsDropPacInUnitTime"))
)
if mibBuilder.loadTexts:
    hh3chipsNDECFlowTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NDEC-MIB",
    **{"hh3cNDEC": hh3cNDEC,
       "hh3chipsNDECSAListTable": hh3chipsNDECSAListTable,
       "hh3chipsNDECSAListEntry": hh3chipsNDECSAListEntry,
       "hh3chipsPeerIpAddr": hh3chipsPeerIpAddr,
       "hh3chipsProtocol": hh3chipsProtocol,
       "hh3chipsSPI": hh3chipsSPI,
       "hh3chipsEncAlgorithm": hh3chipsEncAlgorithm,
       "hh3chipsAuthAlgorithm": hh3chipsAuthAlgorithm,
       "hh3chipsLocalIpAddr": hh3chipsLocalIpAddr,
       "hh3chipsSaLifeKBytes": hh3chipsSaLifeKBytes,
       "hh3chipsSaLifeSecond": hh3chipsSaLifeSecond,
       "hh3chipsByCard": hh3chipsByCard,
       "hh3chipsNegotiateSaMode": hh3chipsNegotiateSaMode,
       "hh3chipsExpBytes": hh3chipsExpBytes,
       "hh3chipsSoftBytes": hh3chipsSoftBytes,
       "hh3chipsExpTimeout": hh3chipsExpTimeout,
       "hh3chipsSoftTimeout": hh3chipsSoftTimeout,
       "hh3chikeSATable": hh3chikeSATable,
       "hh3chikeSAEntry": hh3chikeSAEntry,
       "hh3chikeConnId": hh3chikeConnId,
       "hh3chikePeerIpAddr": hh3chikePeerIpAddr,
       "hh3chikeFlag": hh3chikeFlag,
       "hh3chikePhase": hh3chikePhase,
       "hh3chikeDoi": hh3chikeDoi,
       "hh3chikeClearSA": hh3chikeClearSA,
       "hh3chipsIKEPolicyTable": hh3chipsIKEPolicyTable,
       "hh3chipsIKEPolicyEntry": hh3chipsIKEPolicyEntry,
       "hh3chipsIsakmpPolPriority": hh3chipsIsakmpPolPriority,
       "hh3chipsIsakmpPolEncr": hh3chipsIsakmpPolEncr,
       "hh3chipsIsakmpPolHash": hh3chipsIsakmpPolHash,
       "hh3chipsIsakmpPolAuth": hh3chipsIsakmpPolAuth,
       "hh3chipsIsakmpPolGroup": hh3chipsIsakmpPolGroup,
       "hh3chipsIsakmpPolLifetime": hh3chipsIsakmpPolLifetime,
       "hh3chipsStaticCryptomapTable": hh3chipsStaticCryptomapTable,
       "hh3chipsStaticCryptomapEntry": hh3chipsStaticCryptomapEntry,
       "hh3chipsStaticCryptomapName": hh3chipsStaticCryptomapName,
       "hh3chipsStaticCryptomapSN": hh3chipsStaticCryptomapSN,
       "hh3chipsStaticCryptomapNegMode": hh3chipsStaticCryptomapNegMode,
       "hh3chipsStaticCryptomapMatchAddr": hh3chipsStaticCryptomapMatchAddr,
       "hh3chipsStaticCryptomapPeerIpAddr": hh3chipsStaticCryptomapPeerIpAddr,
       "hh3chipsStaticCryptomapTransforName": hh3chipsStaticCryptomapTransforName,
       "hh3chipsStaticCryptomapLifetime": hh3chipsStaticCryptomapLifetime,
       "hh3chipsStaticCryptomapLifesize": hh3chipsStaticCryptomapLifesize,
       "hh3chipsStaticCryptomapLocalIpAddr": hh3chipsStaticCryptomapLocalIpAddr,
       "hh3chipsIfNameUsed": hh3chipsIfNameUsed,
       "hh3chipsInAHSPI": hh3chipsInAHSPI,
       "hh3chipsInESPSPI": hh3chipsInESPSPI,
       "hh3chipsOutAHSPI": hh3chipsOutAHSPI,
       "hh3chipsOutESPSPI": hh3chipsOutESPSPI,
       "hh3chipsInAhHexKeyString": hh3chipsInAhHexKeyString,
       "hh3chipsInEspCipherHexKeyString": hh3chipsInEspCipherHexKeyString,
       "hh3chipsInEspAuthenHexKeyString": hh3chipsInEspAuthenHexKeyString,
       "hh3chipsInAhStringKeyString": hh3chipsInAhStringKeyString,
       "hh3chipsInEspStringKeyString": hh3chipsInEspStringKeyString,
       "hh3chipsOutAhHexKeyString": hh3chipsOutAhHexKeyString,
       "hh3chipsOutEspCipherHexKeyString": hh3chipsOutEspCipherHexKeyString,
       "hh3chipsOutEspAuthenHexKeyString": hh3chipsOutEspAuthenHexKeyString,
       "hh3chipsOutAhStringKeyString": hh3chipsOutAhStringKeyString,
       "hh3chipsOutEspStringKeyString": hh3chipsOutEspStringKeyString,
       "hh3chipsTransformNameSetTable": hh3chipsTransformNameSetTable,
       "hh3chipsTransformNameSetEntry": hh3chipsTransformNameSetEntry,
       "hh3chipsTransformName": hh3chipsTransformName,
       "hh3chipsTransformMode": hh3chipsTransformMode,
       "hh3chipsTransformProtocol": hh3chipsTransformProtocol,
       "hh3chipsAH": hh3chipsAH,
       "hh3chipsEespEn": hh3chipsEespEn,
       "hh3chipsEspAu": hh3chipsEspAu,
       "hh3chipsIsCardTransform": hh3chipsIsCardTransform,
       "hh3chipsNDECInfoTable": hh3chipsNDECInfoTable,
       "hh3chipsNDECInfoEntry": hh3chipsNDECInfoEntry,
       "hh3chipsCardSlot": hh3chipsCardSlot,
       "hh3chipsInPac": hh3chipsInPac,
       "hh3chipsOutPac": hh3chipsOutPac,
       "hh3chipsInByte": hh3chipsInByte,
       "hh3chipsOutByte": hh3chipsOutByte,
       "hh3chipsDropPac": hh3chipsDropPac,
       "hh3chipsCardStatus": hh3chipsCardStatus,
       "hh3chipsCardHardVer": hh3chipsCardHardVer,
       "hh3chipsCardSoftVer": hh3chipsCardSoftVer,
       "hh3chipsCardCPLDVer": hh3chipsCardCPLDVer,
       "hh3chipsCardOperate": hh3chipsCardOperate,
       "hh3chipsDropPacInUnitTime": hh3chipsDropPacInUnitTime,
       "hh3chipsNDECLeaf": hh3chipsNDECLeaf,
       "hh3chipsNDECConnections": hh3chipsNDECConnections,
       "hh3chipsNDECBackup": hh3chipsNDECBackup,
       "hh3chipsTraps": hh3chipsTraps,
       "hh3chipsNDECNormalResetTrap": hh3chipsNDECNormalResetTrap,
       "hh3chipsNDECStateChangeTrap": hh3chipsNDECStateChangeTrap,
       "hh3chipsNDECFlowTrap": hh3chipsNDECFlowTrap}
)
