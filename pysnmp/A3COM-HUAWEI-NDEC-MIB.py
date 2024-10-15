# SNMP MIB module (A3COM-HUAWEI-NDEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-NDEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:42 2024
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

(mlsr,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "mlsr")

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

huaweiNDEC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2)
)
huaweiNDEC.setRevisions(
        ("2004-09-15 10:52",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HipsNDECSAListTable_Object = MibTable
hipsNDECSAListTable = _HipsNDECSAListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1)
)
if mibBuilder.loadTexts:
    hipsNDECSAListTable.setStatus("current")
_HipsNDECSAListEntry_Object = MibTableRow
hipsNDECSAListEntry = _HipsNDECSAListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1)
)
hipsNDECSAListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsPeerIpAddr"),
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsProtocol"),
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsSPI"),
)
if mibBuilder.loadTexts:
    hipsNDECSAListEntry.setStatus("current")
_HipsPeerIpAddr_Type = IpAddress
_HipsPeerIpAddr_Object = MibTableColumn
hipsPeerIpAddr = _HipsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 1),
    _HipsPeerIpAddr_Type()
)
hipsPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsPeerIpAddr.setStatus("current")


class _HipsProtocol_Type(Integer32):
    """Custom type hipsProtocol based on Integer32"""
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


_HipsProtocol_Type.__name__ = "Integer32"
_HipsProtocol_Object = MibTableColumn
hipsProtocol = _HipsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 2),
    _HipsProtocol_Type()
)
hipsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsProtocol.setStatus("current")


class _HipsSPI_Type(Gauge32):
    """Custom type hipsSPI based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_HipsSPI_Type.__name__ = "Gauge32"
_HipsSPI_Object = MibTableColumn
hipsSPI = _HipsSPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 3),
    _HipsSPI_Type()
)
hipsSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsSPI.setStatus("current")


class _HipsEncAlgorithm_Type(Integer32):
    """Custom type hipsEncAlgorithm based on Integer32"""
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


_HipsEncAlgorithm_Type.__name__ = "Integer32"
_HipsEncAlgorithm_Object = MibTableColumn
hipsEncAlgorithm = _HipsEncAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 4),
    _HipsEncAlgorithm_Type()
)
hipsEncAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsEncAlgorithm.setStatus("current")


class _HipsAuthAlgorithm_Type(Integer32):
    """Custom type hipsAuthAlgorithm based on Integer32"""
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


_HipsAuthAlgorithm_Type.__name__ = "Integer32"
_HipsAuthAlgorithm_Object = MibTableColumn
hipsAuthAlgorithm = _HipsAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 5),
    _HipsAuthAlgorithm_Type()
)
hipsAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsAuthAlgorithm.setStatus("current")
_HipsLocalIpAddr_Type = IpAddress
_HipsLocalIpAddr_Object = MibTableColumn
hipsLocalIpAddr = _HipsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 6),
    _HipsLocalIpAddr_Type()
)
hipsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsLocalIpAddr.setStatus("current")
_HipsSaLifeKBytes_Type = Gauge32
_HipsSaLifeKBytes_Object = MibTableColumn
hipsSaLifeKBytes = _HipsSaLifeKBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 7),
    _HipsSaLifeKBytes_Type()
)
hipsSaLifeKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsSaLifeKBytes.setStatus("current")
_HipsSaLifeSecond_Type = Gauge32
_HipsSaLifeSecond_Object = MibTableColumn
hipsSaLifeSecond = _HipsSaLifeSecond_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 8),
    _HipsSaLifeSecond_Type()
)
hipsSaLifeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsSaLifeSecond.setStatus("current")
_HipsByCard_Type = TruthValue
_HipsByCard_Object = MibTableColumn
hipsByCard = _HipsByCard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 9),
    _HipsByCard_Type()
)
hipsByCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsByCard.setStatus("current")


class _HipsNegotiateSaMode_Type(Integer32):
    """Custom type hipsNegotiateSaMode based on Integer32"""
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


_HipsNegotiateSaMode_Type.__name__ = "Integer32"
_HipsNegotiateSaMode_Object = MibTableColumn
hipsNegotiateSaMode = _HipsNegotiateSaMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 10),
    _HipsNegotiateSaMode_Type()
)
hipsNegotiateSaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsNegotiateSaMode.setStatus("current")
_HipsExpBytes_Type = Gauge32
_HipsExpBytes_Object = MibTableColumn
hipsExpBytes = _HipsExpBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 11),
    _HipsExpBytes_Type()
)
hipsExpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsExpBytes.setStatus("current")
_HipsSoftBytes_Type = Gauge32
_HipsSoftBytes_Object = MibTableColumn
hipsSoftBytes = _HipsSoftBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 12),
    _HipsSoftBytes_Type()
)
hipsSoftBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsSoftBytes.setStatus("current")
_HipsExpTimeout_Type = Gauge32
_HipsExpTimeout_Object = MibTableColumn
hipsExpTimeout = _HipsExpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 13),
    _HipsExpTimeout_Type()
)
hipsExpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsExpTimeout.setStatus("current")
_HipsSoftTimeout_Type = Gauge32
_HipsSoftTimeout_Object = MibTableColumn
hipsSoftTimeout = _HipsSoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 14),
    _HipsSoftTimeout_Type()
)
hipsSoftTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsSoftTimeout.setStatus("current")
_HikeSATable_Object = MibTable
hikeSATable = _HikeSATable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2)
)
if mibBuilder.loadTexts:
    hikeSATable.setStatus("current")
_HikeSAEntry_Object = MibTableRow
hikeSAEntry = _HikeSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1)
)
hikeSAEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hikeConnId"),
)
if mibBuilder.loadTexts:
    hikeSAEntry.setStatus("current")


class _HikeConnId_Type(Integer32):
    """Custom type hikeConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HikeConnId_Type.__name__ = "Integer32"
_HikeConnId_Object = MibTableColumn
hikeConnId = _HikeConnId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 1),
    _HikeConnId_Type()
)
hikeConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hikeConnId.setStatus("current")
_HikePeerIpAddr_Type = IpAddress
_HikePeerIpAddr_Object = MibTableColumn
hikePeerIpAddr = _HikePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 2),
    _HikePeerIpAddr_Type()
)
hikePeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hikePeerIpAddr.setStatus("current")
_HikeFlag_Type = DisplayString
_HikeFlag_Object = MibTableColumn
hikeFlag = _HikeFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 3),
    _HikeFlag_Type()
)
hikeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hikeFlag.setStatus("current")


class _HikePhase_Type(Integer32):
    """Custom type hikePhase based on Integer32"""
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


_HikePhase_Type.__name__ = "Integer32"
_HikePhase_Object = MibTableColumn
hikePhase = _HikePhase_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 4),
    _HikePhase_Type()
)
hikePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hikePhase.setStatus("current")


class _HikeDoi_Type(Integer32):
    """Custom type hikeDoi based on Integer32"""
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


_HikeDoi_Type.__name__ = "Integer32"
_HikeDoi_Object = MibTableColumn
hikeDoi = _HikeDoi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 5),
    _HikeDoi_Type()
)
hikeDoi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hikeDoi.setStatus("current")
_HikeClearSA_Type = TruthValue
_HikeClearSA_Object = MibTableColumn
hikeClearSA = _HikeClearSA_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 6),
    _HikeClearSA_Type()
)
hikeClearSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hikeClearSA.setStatus("current")
_HipsIKEPolicyTable_Object = MibTable
hipsIKEPolicyTable = _HipsIKEPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3)
)
if mibBuilder.loadTexts:
    hipsIKEPolicyTable.setStatus("current")
_HipsIKEPolicyEntry_Object = MibTableRow
hipsIKEPolicyEntry = _HipsIKEPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1)
)
hipsIKEPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsIsakmpPolPriority"),
)
if mibBuilder.loadTexts:
    hipsIKEPolicyEntry.setStatus("current")


class _HipsIsakmpPolPriority_Type(Integer32):
    """Custom type hipsIsakmpPolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HipsIsakmpPolPriority_Type.__name__ = "Integer32"
_HipsIsakmpPolPriority_Object = MibTableColumn
hipsIsakmpPolPriority = _HipsIsakmpPolPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 1),
    _HipsIsakmpPolPriority_Type()
)
hipsIsakmpPolPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolPriority.setStatus("current")


class _HipsIsakmpPolEncr_Type(Integer32):
    """Custom type hipsIsakmpPolEncr based on Integer32"""
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


_HipsIsakmpPolEncr_Type.__name__ = "Integer32"
_HipsIsakmpPolEncr_Object = MibTableColumn
hipsIsakmpPolEncr = _HipsIsakmpPolEncr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 2),
    _HipsIsakmpPolEncr_Type()
)
hipsIsakmpPolEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolEncr.setStatus("current")


class _HipsIsakmpPolHash_Type(Integer32):
    """Custom type hipsIsakmpPolHash based on Integer32"""
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


_HipsIsakmpPolHash_Type.__name__ = "Integer32"
_HipsIsakmpPolHash_Object = MibTableColumn
hipsIsakmpPolHash = _HipsIsakmpPolHash_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 3),
    _HipsIsakmpPolHash_Type()
)
hipsIsakmpPolHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolHash.setStatus("current")


class _HipsIsakmpPolAuth_Type(Integer32):
    """Custom type hipsIsakmpPolAuth based on Integer32"""
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


_HipsIsakmpPolAuth_Type.__name__ = "Integer32"
_HipsIsakmpPolAuth_Object = MibTableColumn
hipsIsakmpPolAuth = _HipsIsakmpPolAuth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 4),
    _HipsIsakmpPolAuth_Type()
)
hipsIsakmpPolAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolAuth.setStatus("current")


class _HipsIsakmpPolGroup_Type(Integer32):
    """Custom type hipsIsakmpPolGroup based on Integer32"""
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


_HipsIsakmpPolGroup_Type.__name__ = "Integer32"
_HipsIsakmpPolGroup_Object = MibTableColumn
hipsIsakmpPolGroup = _HipsIsakmpPolGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 5),
    _HipsIsakmpPolGroup_Type()
)
hipsIsakmpPolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolGroup.setStatus("current")
_HipsIsakmpPolLifetime_Type = Gauge32
_HipsIsakmpPolLifetime_Object = MibTableColumn
hipsIsakmpPolLifetime = _HipsIsakmpPolLifetime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 6),
    _HipsIsakmpPolLifetime_Type()
)
hipsIsakmpPolLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsakmpPolLifetime.setStatus("current")
_HipsStaticCryptomapTable_Object = MibTable
hipsStaticCryptomapTable = _HipsStaticCryptomapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4)
)
if mibBuilder.loadTexts:
    hipsStaticCryptomapTable.setStatus("current")
_HipsStaticCryptomapEntry_Object = MibTableRow
hipsStaticCryptomapEntry = _HipsStaticCryptomapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1)
)
hipsStaticCryptomapEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsStaticCryptomapName"),
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsStaticCryptomapSN"),
)
if mibBuilder.loadTexts:
    hipsStaticCryptomapEntry.setStatus("current")
_HipsStaticCryptomapName_Type = DisplayString
_HipsStaticCryptomapName_Object = MibTableColumn
hipsStaticCryptomapName = _HipsStaticCryptomapName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 1),
    _HipsStaticCryptomapName_Type()
)
hipsStaticCryptomapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapName.setStatus("current")


class _HipsStaticCryptomapSN_Type(Integer32):
    """Custom type hipsStaticCryptomapSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HipsStaticCryptomapSN_Type.__name__ = "Integer32"
_HipsStaticCryptomapSN_Object = MibTableColumn
hipsStaticCryptomapSN = _HipsStaticCryptomapSN_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 2),
    _HipsStaticCryptomapSN_Type()
)
hipsStaticCryptomapSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapSN.setStatus("current")


class _HipsStaticCryptomapNegMode_Type(Integer32):
    """Custom type hipsStaticCryptomapNegMode based on Integer32"""
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


_HipsStaticCryptomapNegMode_Type.__name__ = "Integer32"
_HipsStaticCryptomapNegMode_Object = MibTableColumn
hipsStaticCryptomapNegMode = _HipsStaticCryptomapNegMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 3),
    _HipsStaticCryptomapNegMode_Type()
)
hipsStaticCryptomapNegMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapNegMode.setStatus("current")


class _HipsStaticCryptomapMatchAddr_Type(Integer32):
    """Custom type hipsStaticCryptomapMatchAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_HipsStaticCryptomapMatchAddr_Type.__name__ = "Integer32"
_HipsStaticCryptomapMatchAddr_Object = MibTableColumn
hipsStaticCryptomapMatchAddr = _HipsStaticCryptomapMatchAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 4),
    _HipsStaticCryptomapMatchAddr_Type()
)
hipsStaticCryptomapMatchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapMatchAddr.setStatus("current")
_HipsStaticCryptomapPeerIpAddr_Type = IpAddress
_HipsStaticCryptomapPeerIpAddr_Object = MibTableColumn
hipsStaticCryptomapPeerIpAddr = _HipsStaticCryptomapPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 5),
    _HipsStaticCryptomapPeerIpAddr_Type()
)
hipsStaticCryptomapPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapPeerIpAddr.setStatus("current")
_HipsStaticCryptomapTransforName_Type = DisplayString
_HipsStaticCryptomapTransforName_Object = MibTableColumn
hipsStaticCryptomapTransforName = _HipsStaticCryptomapTransforName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 6),
    _HipsStaticCryptomapTransforName_Type()
)
hipsStaticCryptomapTransforName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapTransforName.setStatus("current")
_HipsStaticCryptomapLifetime_Type = Gauge32
_HipsStaticCryptomapLifetime_Object = MibTableColumn
hipsStaticCryptomapLifetime = _HipsStaticCryptomapLifetime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 7),
    _HipsStaticCryptomapLifetime_Type()
)
hipsStaticCryptomapLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapLifetime.setStatus("current")
_HipsStaticCryptomapLifesize_Type = Gauge32
_HipsStaticCryptomapLifesize_Object = MibTableColumn
hipsStaticCryptomapLifesize = _HipsStaticCryptomapLifesize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 8),
    _HipsStaticCryptomapLifesize_Type()
)
hipsStaticCryptomapLifesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapLifesize.setStatus("current")
_HipsStaticCryptomapLocalIpAddr_Type = IpAddress
_HipsStaticCryptomapLocalIpAddr_Object = MibTableColumn
hipsStaticCryptomapLocalIpAddr = _HipsStaticCryptomapLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 9),
    _HipsStaticCryptomapLocalIpAddr_Type()
)
hipsStaticCryptomapLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsStaticCryptomapLocalIpAddr.setStatus("current")
_HipsIfNameUsed_Type = DisplayString
_HipsIfNameUsed_Object = MibTableColumn
hipsIfNameUsed = _HipsIfNameUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 10),
    _HipsIfNameUsed_Type()
)
hipsIfNameUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIfNameUsed.setStatus("current")
_HipsInAHSPI_Type = Gauge32
_HipsInAHSPI_Object = MibTableColumn
hipsInAHSPI = _HipsInAHSPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 11),
    _HipsInAHSPI_Type()
)
hipsInAHSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInAHSPI.setStatus("current")
_HipsInESPSPI_Type = Gauge32
_HipsInESPSPI_Object = MibTableColumn
hipsInESPSPI = _HipsInESPSPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 12),
    _HipsInESPSPI_Type()
)
hipsInESPSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInESPSPI.setStatus("current")
_HipsOutAHSPI_Type = Gauge32
_HipsOutAHSPI_Object = MibTableColumn
hipsOutAHSPI = _HipsOutAHSPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 13),
    _HipsOutAHSPI_Type()
)
hipsOutAHSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutAHSPI.setStatus("current")
_HipsOutESPSPI_Type = Gauge32
_HipsOutESPSPI_Object = MibTableColumn
hipsOutESPSPI = _HipsOutESPSPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 14),
    _HipsOutESPSPI_Type()
)
hipsOutESPSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutESPSPI.setStatus("current")
_HipsInAhHexKeyString_Type = DisplayString
_HipsInAhHexKeyString_Object = MibTableColumn
hipsInAhHexKeyString = _HipsInAhHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 15),
    _HipsInAhHexKeyString_Type()
)
hipsInAhHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInAhHexKeyString.setStatus("current")
_HipsInEspCipherHexKeyString_Type = DisplayString
_HipsInEspCipherHexKeyString_Object = MibTableColumn
hipsInEspCipherHexKeyString = _HipsInEspCipherHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 16),
    _HipsInEspCipherHexKeyString_Type()
)
hipsInEspCipherHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInEspCipherHexKeyString.setStatus("current")
_HipsInEspAuthenHexKeyString_Type = DisplayString
_HipsInEspAuthenHexKeyString_Object = MibTableColumn
hipsInEspAuthenHexKeyString = _HipsInEspAuthenHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 17),
    _HipsInEspAuthenHexKeyString_Type()
)
hipsInEspAuthenHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInEspAuthenHexKeyString.setStatus("current")
_HipsInAhStringKeyString_Type = DisplayString
_HipsInAhStringKeyString_Object = MibTableColumn
hipsInAhStringKeyString = _HipsInAhStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 18),
    _HipsInAhStringKeyString_Type()
)
hipsInAhStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInAhStringKeyString.setStatus("current")
_HipsInEspStringKeyString_Type = DisplayString
_HipsInEspStringKeyString_Object = MibTableColumn
hipsInEspStringKeyString = _HipsInEspStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 19),
    _HipsInEspStringKeyString_Type()
)
hipsInEspStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInEspStringKeyString.setStatus("current")
_HipsOutAhHexKeyString_Type = DisplayString
_HipsOutAhHexKeyString_Object = MibTableColumn
hipsOutAhHexKeyString = _HipsOutAhHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 20),
    _HipsOutAhHexKeyString_Type()
)
hipsOutAhHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutAhHexKeyString.setStatus("current")
_HipsOutEspCipherHexKeyString_Type = DisplayString
_HipsOutEspCipherHexKeyString_Object = MibTableColumn
hipsOutEspCipherHexKeyString = _HipsOutEspCipherHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 21),
    _HipsOutEspCipherHexKeyString_Type()
)
hipsOutEspCipherHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutEspCipherHexKeyString.setStatus("current")
_HipsOutEspAuthenHexKeyString_Type = DisplayString
_HipsOutEspAuthenHexKeyString_Object = MibTableColumn
hipsOutEspAuthenHexKeyString = _HipsOutEspAuthenHexKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 22),
    _HipsOutEspAuthenHexKeyString_Type()
)
hipsOutEspAuthenHexKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutEspAuthenHexKeyString.setStatus("current")
_HipsOutAhStringKeyString_Type = DisplayString
_HipsOutAhStringKeyString_Object = MibTableColumn
hipsOutAhStringKeyString = _HipsOutAhStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 23),
    _HipsOutAhStringKeyString_Type()
)
hipsOutAhStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutAhStringKeyString.setStatus("current")
_HipsOutEspStringKeyString_Type = DisplayString
_HipsOutEspStringKeyString_Object = MibTableColumn
hipsOutEspStringKeyString = _HipsOutEspStringKeyString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 24),
    _HipsOutEspStringKeyString_Type()
)
hipsOutEspStringKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutEspStringKeyString.setStatus("current")
_HipsTransformNameSetTable_Object = MibTable
hipsTransformNameSetTable = _HipsTransformNameSetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5)
)
if mibBuilder.loadTexts:
    hipsTransformNameSetTable.setStatus("current")
_HipsTransformNameSetEntry_Object = MibTableRow
hipsTransformNameSetEntry = _HipsTransformNameSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1)
)
hipsTransformNameSetEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsTransformName"),
)
if mibBuilder.loadTexts:
    hipsTransformNameSetEntry.setStatus("current")
_HipsTransformName_Type = DisplayString
_HipsTransformName_Object = MibTableColumn
hipsTransformName = _HipsTransformName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 1),
    _HipsTransformName_Type()
)
hipsTransformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsTransformName.setStatus("current")


class _HipsTransformMode_Type(Integer32):
    """Custom type hipsTransformMode based on Integer32"""
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


_HipsTransformMode_Type.__name__ = "Integer32"
_HipsTransformMode_Object = MibTableColumn
hipsTransformMode = _HipsTransformMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 2),
    _HipsTransformMode_Type()
)
hipsTransformMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsTransformMode.setStatus("current")


class _HipsTransformProtocol_Type(Integer32):
    """Custom type hipsTransformProtocol based on Integer32"""
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


_HipsTransformProtocol_Type.__name__ = "Integer32"
_HipsTransformProtocol_Object = MibTableColumn
hipsTransformProtocol = _HipsTransformProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 3),
    _HipsTransformProtocol_Type()
)
hipsTransformProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsTransformProtocol.setStatus("current")


class _HipsAH_Type(Integer32):
    """Custom type hipsAH based on Integer32"""
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


_HipsAH_Type.__name__ = "Integer32"
_HipsAH_Object = MibTableColumn
hipsAH = _HipsAH_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 4),
    _HipsAH_Type()
)
hipsAH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsAH.setStatus("current")


class _HipsEespEn_Type(Integer32):
    """Custom type hipsEespEn based on Integer32"""
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


_HipsEespEn_Type.__name__ = "Integer32"
_HipsEespEn_Object = MibTableColumn
hipsEespEn = _HipsEespEn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 5),
    _HipsEespEn_Type()
)
hipsEespEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsEespEn.setStatus("current")


class _HipsEspAu_Type(Integer32):
    """Custom type hipsEspAu based on Integer32"""
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


_HipsEspAu_Type.__name__ = "Integer32"
_HipsEspAu_Object = MibTableColumn
hipsEspAu = _HipsEspAu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 6),
    _HipsEspAu_Type()
)
hipsEspAu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsEspAu.setStatus("current")
_HipsIsCardTransform_Type = TruthValue
_HipsIsCardTransform_Object = MibTableColumn
hipsIsCardTransform = _HipsIsCardTransform_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 7),
    _HipsIsCardTransform_Type()
)
hipsIsCardTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsIsCardTransform.setStatus("current")
_HipsNDECInfoTable_Object = MibTable
hipsNDECInfoTable = _HipsNDECInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6)
)
if mibBuilder.loadTexts:
    hipsNDECInfoTable.setStatus("current")
_HipsNDECInfoEntry_Object = MibTableRow
hipsNDECInfoEntry = _HipsNDECInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1)
)
hipsNDECInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"),
)
if mibBuilder.loadTexts:
    hipsNDECInfoEntry.setStatus("current")


class _HipsCardSlot_Type(Integer32):
    """Custom type hipsCardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HipsCardSlot_Type.__name__ = "Integer32"
_HipsCardSlot_Object = MibTableColumn
hipsCardSlot = _HipsCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 1),
    _HipsCardSlot_Type()
)
hipsCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsCardSlot.setStatus("current")
_HipsInPac_Type = Counter32
_HipsInPac_Object = MibTableColumn
hipsInPac = _HipsInPac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 2),
    _HipsInPac_Type()
)
hipsInPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInPac.setStatus("current")
_HipsOutPac_Type = Counter32
_HipsOutPac_Object = MibTableColumn
hipsOutPac = _HipsOutPac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 3),
    _HipsOutPac_Type()
)
hipsOutPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutPac.setStatus("current")
_HipsInByte_Type = Counter32
_HipsInByte_Object = MibTableColumn
hipsInByte = _HipsInByte_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 4),
    _HipsInByte_Type()
)
hipsInByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsInByte.setStatus("current")
_HipsOutByte_Type = Counter32
_HipsOutByte_Object = MibTableColumn
hipsOutByte = _HipsOutByte_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 5),
    _HipsOutByte_Type()
)
hipsOutByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsOutByte.setStatus("current")
_HipsDropPac_Type = Counter32
_HipsDropPac_Object = MibTableColumn
hipsDropPac = _HipsDropPac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 6),
    _HipsDropPac_Type()
)
hipsDropPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsDropPac.setStatus("current")


class _HipsCardStatus_Type(Integer32):
    """Custom type hipsCardStatus based on Integer32"""
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


_HipsCardStatus_Type.__name__ = "Integer32"
_HipsCardStatus_Object = MibTableColumn
hipsCardStatus = _HipsCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 7),
    _HipsCardStatus_Type()
)
hipsCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsCardStatus.setStatus("current")
_HipsCardHardVer_Type = DisplayString
_HipsCardHardVer_Object = MibTableColumn
hipsCardHardVer = _HipsCardHardVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 8),
    _HipsCardHardVer_Type()
)
hipsCardHardVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsCardHardVer.setStatus("current")
_HipsCardSoftVer_Type = DisplayString
_HipsCardSoftVer_Object = MibTableColumn
hipsCardSoftVer = _HipsCardSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 9),
    _HipsCardSoftVer_Type()
)
hipsCardSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsCardSoftVer.setStatus("current")
_HipsCardCPLDVer_Type = DisplayString
_HipsCardCPLDVer_Object = MibTableColumn
hipsCardCPLDVer = _HipsCardCPLDVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 10),
    _HipsCardCPLDVer_Type()
)
hipsCardCPLDVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsCardCPLDVer.setStatus("current")


class _HipsCardOperate_Type(Integer32):
    """Custom type hipsCardOperate based on Integer32"""
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


_HipsCardOperate_Type.__name__ = "Integer32"
_HipsCardOperate_Object = MibTableColumn
hipsCardOperate = _HipsCardOperate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 11),
    _HipsCardOperate_Type()
)
hipsCardOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hipsCardOperate.setStatus("current")
_HipsDropPacInUnitTime_Type = Gauge32
_HipsDropPacInUnitTime_Object = MibTableColumn
hipsDropPacInUnitTime = _HipsDropPacInUnitTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 12),
    _HipsDropPacInUnitTime_Type()
)
hipsDropPacInUnitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsDropPacInUnitTime.setStatus("current")
_HipsNDECLeaf_ObjectIdentity = ObjectIdentity
hipsNDECLeaf = _HipsNDECLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7)
)
_HipsNDECConnections_Type = Integer32
_HipsNDECConnections_Object = MibScalar
hipsNDECConnections = _HipsNDECConnections_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7, 1),
    _HipsNDECConnections_Type()
)
hipsNDECConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipsNDECConnections.setStatus("current")
_HipsNDECBackup_Type = Integer32
_HipsNDECBackup_Object = MibScalar
hipsNDECBackup = _HipsNDECBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7, 2),
    _HipsNDECBackup_Type()
)
hipsNDECBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hipsNDECBackup.setStatus("current")
_HipsTraps_ObjectIdentity = ObjectIdentity
hipsTraps = _HipsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8)
)

# Managed Objects groups


# Notification objects

hipsNDECNormalResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 1)
)
hipsNDECNormalResetTrap.setObjects(
      *(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"),
        ("A3COM-HUAWEI-NDEC-MIB", "hipsCardHardVer"),
        ("A3COM-HUAWEI-NDEC-MIB", "hipsCardSoftVer"),
        ("A3COM-HUAWEI-NDEC-MIB", "hipsCardCPLDVer"))
)
if mibBuilder.loadTexts:
    hipsNDECNormalResetTrap.setStatus(
        "current"
    )

hipsNDECStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 2)
)
hipsNDECStateChangeTrap.setObjects(
      *(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"),
        ("A3COM-HUAWEI-NDEC-MIB", "hipsCardStatus"))
)
if mibBuilder.loadTexts:
    hipsNDECStateChangeTrap.setStatus(
        "current"
    )

hipsNDECFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 3)
)
hipsNDECFlowTrap.setObjects(
      *(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"),
        ("A3COM-HUAWEI-NDEC-MIB", "hipsDropPacInUnitTime"))
)
if mibBuilder.loadTexts:
    hipsNDECFlowTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-NDEC-MIB",
    **{"huaweiNDEC": huaweiNDEC,
       "hipsNDECSAListTable": hipsNDECSAListTable,
       "hipsNDECSAListEntry": hipsNDECSAListEntry,
       "hipsPeerIpAddr": hipsPeerIpAddr,
       "hipsProtocol": hipsProtocol,
       "hipsSPI": hipsSPI,
       "hipsEncAlgorithm": hipsEncAlgorithm,
       "hipsAuthAlgorithm": hipsAuthAlgorithm,
       "hipsLocalIpAddr": hipsLocalIpAddr,
       "hipsSaLifeKBytes": hipsSaLifeKBytes,
       "hipsSaLifeSecond": hipsSaLifeSecond,
       "hipsByCard": hipsByCard,
       "hipsNegotiateSaMode": hipsNegotiateSaMode,
       "hipsExpBytes": hipsExpBytes,
       "hipsSoftBytes": hipsSoftBytes,
       "hipsExpTimeout": hipsExpTimeout,
       "hipsSoftTimeout": hipsSoftTimeout,
       "hikeSATable": hikeSATable,
       "hikeSAEntry": hikeSAEntry,
       "hikeConnId": hikeConnId,
       "hikePeerIpAddr": hikePeerIpAddr,
       "hikeFlag": hikeFlag,
       "hikePhase": hikePhase,
       "hikeDoi": hikeDoi,
       "hikeClearSA": hikeClearSA,
       "hipsIKEPolicyTable": hipsIKEPolicyTable,
       "hipsIKEPolicyEntry": hipsIKEPolicyEntry,
       "hipsIsakmpPolPriority": hipsIsakmpPolPriority,
       "hipsIsakmpPolEncr": hipsIsakmpPolEncr,
       "hipsIsakmpPolHash": hipsIsakmpPolHash,
       "hipsIsakmpPolAuth": hipsIsakmpPolAuth,
       "hipsIsakmpPolGroup": hipsIsakmpPolGroup,
       "hipsIsakmpPolLifetime": hipsIsakmpPolLifetime,
       "hipsStaticCryptomapTable": hipsStaticCryptomapTable,
       "hipsStaticCryptomapEntry": hipsStaticCryptomapEntry,
       "hipsStaticCryptomapName": hipsStaticCryptomapName,
       "hipsStaticCryptomapSN": hipsStaticCryptomapSN,
       "hipsStaticCryptomapNegMode": hipsStaticCryptomapNegMode,
       "hipsStaticCryptomapMatchAddr": hipsStaticCryptomapMatchAddr,
       "hipsStaticCryptomapPeerIpAddr": hipsStaticCryptomapPeerIpAddr,
       "hipsStaticCryptomapTransforName": hipsStaticCryptomapTransforName,
       "hipsStaticCryptomapLifetime": hipsStaticCryptomapLifetime,
       "hipsStaticCryptomapLifesize": hipsStaticCryptomapLifesize,
       "hipsStaticCryptomapLocalIpAddr": hipsStaticCryptomapLocalIpAddr,
       "hipsIfNameUsed": hipsIfNameUsed,
       "hipsInAHSPI": hipsInAHSPI,
       "hipsInESPSPI": hipsInESPSPI,
       "hipsOutAHSPI": hipsOutAHSPI,
       "hipsOutESPSPI": hipsOutESPSPI,
       "hipsInAhHexKeyString": hipsInAhHexKeyString,
       "hipsInEspCipherHexKeyString": hipsInEspCipherHexKeyString,
       "hipsInEspAuthenHexKeyString": hipsInEspAuthenHexKeyString,
       "hipsInAhStringKeyString": hipsInAhStringKeyString,
       "hipsInEspStringKeyString": hipsInEspStringKeyString,
       "hipsOutAhHexKeyString": hipsOutAhHexKeyString,
       "hipsOutEspCipherHexKeyString": hipsOutEspCipherHexKeyString,
       "hipsOutEspAuthenHexKeyString": hipsOutEspAuthenHexKeyString,
       "hipsOutAhStringKeyString": hipsOutAhStringKeyString,
       "hipsOutEspStringKeyString": hipsOutEspStringKeyString,
       "hipsTransformNameSetTable": hipsTransformNameSetTable,
       "hipsTransformNameSetEntry": hipsTransformNameSetEntry,
       "hipsTransformName": hipsTransformName,
       "hipsTransformMode": hipsTransformMode,
       "hipsTransformProtocol": hipsTransformProtocol,
       "hipsAH": hipsAH,
       "hipsEespEn": hipsEespEn,
       "hipsEspAu": hipsEspAu,
       "hipsIsCardTransform": hipsIsCardTransform,
       "hipsNDECInfoTable": hipsNDECInfoTable,
       "hipsNDECInfoEntry": hipsNDECInfoEntry,
       "hipsCardSlot": hipsCardSlot,
       "hipsInPac": hipsInPac,
       "hipsOutPac": hipsOutPac,
       "hipsInByte": hipsInByte,
       "hipsOutByte": hipsOutByte,
       "hipsDropPac": hipsDropPac,
       "hipsCardStatus": hipsCardStatus,
       "hipsCardHardVer": hipsCardHardVer,
       "hipsCardSoftVer": hipsCardSoftVer,
       "hipsCardCPLDVer": hipsCardCPLDVer,
       "hipsCardOperate": hipsCardOperate,
       "hipsDropPacInUnitTime": hipsDropPacInUnitTime,
       "hipsNDECLeaf": hipsNDECLeaf,
       "hipsNDECConnections": hipsNDECConnections,
       "hipsNDECBackup": hipsNDECBackup,
       "hipsTraps": hipsTraps,
       "hipsNDECNormalResetTrap": hipsNDECNormalResetTrap,
       "hipsNDECStateChangeTrap": hipsNDECStateChangeTrap,
       "hipsNDECFlowTrap": hipsNDECFlowTrap}
)
