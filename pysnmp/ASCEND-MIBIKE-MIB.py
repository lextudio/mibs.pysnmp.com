# SNMP MIB module (ASCEND-MIBIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIKE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:38 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibmibProfIke_ObjectIdentity = ObjectIdentity
mibmibProfIke = _MibmibProfIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 165)
)
_MibmibProfIkeTable_Object = MibTable
mibmibProfIkeTable = _MibmibProfIkeTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1)
)
if mibBuilder.loadTexts:
    mibmibProfIkeTable.setStatus("mandatory")
_MibmibProfIkeEntry_Object = MibTableRow
mibmibProfIkeEntry = _MibmibProfIkeEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1)
)
mibmibProfIkeEntry.setIndexNames(
    (0, "ASCEND-MIBIKE-MIB", "mibProfIke-IkeProtectionSuiteName"),
)
if mibBuilder.loadTexts:
    mibmibProfIkeEntry.setStatus("mandatory")
_MibProfIke_IkeProtectionSuiteName_Type = DisplayString
_MibProfIke_IkeProtectionSuiteName_Object = MibScalar
mibProfIke_IkeProtectionSuiteName = _MibProfIke_IkeProtectionSuiteName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 1),
    _MibProfIke_IkeProtectionSuiteName_Type()
)
mibProfIke_IkeProtectionSuiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfIke_IkeProtectionSuiteName.setStatus("mandatory")


class _MibProfIke_Phase1Mode_Type(Integer32):
    """Custom type mibProfIke_Phase1Mode based on Integer32"""
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


_MibProfIke_Phase1Mode_Type.__name__ = "Integer32"
_MibProfIke_Phase1Mode_Object = MibScalar
mibProfIke_Phase1Mode = _MibProfIke_Phase1Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 2),
    _MibProfIke_Phase1Mode_Type()
)
mibProfIke_Phase1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_Phase1Mode.setStatus("mandatory")


class _MibProfIke_EncryptionAlgorithm_Type(Integer32):
    """Custom type mibProfIke_EncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("desCbc", 1),
          ("n-3desCbc", 2))
    )


_MibProfIke_EncryptionAlgorithm_Type.__name__ = "Integer32"
_MibProfIke_EncryptionAlgorithm_Object = MibScalar
mibProfIke_EncryptionAlgorithm = _MibProfIke_EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 3),
    _MibProfIke_EncryptionAlgorithm_Type()
)
mibProfIke_EncryptionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_EncryptionAlgorithm.setStatus("mandatory")


class _MibProfIke_HashAlgorithm_Type(Integer32):
    """Custom type mibProfIke_HashAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2),
          ("tiger", 3))
    )


_MibProfIke_HashAlgorithm_Type.__name__ = "Integer32"
_MibProfIke_HashAlgorithm_Object = MibScalar
mibProfIke_HashAlgorithm = _MibProfIke_HashAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 4),
    _MibProfIke_HashAlgorithm_Type()
)
mibProfIke_HashAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_HashAlgorithm.setStatus("mandatory")


class _MibProfIke_AuthenticationMethod_Type(Integer32):
    """Custom type mibProfIke_AuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("presharedKey", 1)
    )


_MibProfIke_AuthenticationMethod_Type.__name__ = "Integer32"
_MibProfIke_AuthenticationMethod_Object = MibScalar
mibProfIke_AuthenticationMethod = _MibProfIke_AuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 5),
    _MibProfIke_AuthenticationMethod_Type()
)
mibProfIke_AuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_AuthenticationMethod.setStatus("mandatory")


class _MibProfIke_DiffieHellmanGroup_Type(Integer32):
    """Custom type mibProfIke_DiffieHellmanGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-1", 1),
          ("n-2", 2))
    )


_MibProfIke_DiffieHellmanGroup_Type.__name__ = "Integer32"
_MibProfIke_DiffieHellmanGroup_Object = MibScalar
mibProfIke_DiffieHellmanGroup = _MibProfIke_DiffieHellmanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 6),
    _MibProfIke_DiffieHellmanGroup_Type()
)
mibProfIke_DiffieHellmanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_DiffieHellmanGroup.setStatus("mandatory")
_MibProfIke_SaLife_TimeLimit_Type = Integer32
_MibProfIke_SaLife_TimeLimit_Object = MibScalar
mibProfIke_SaLife_TimeLimit = _MibProfIke_SaLife_TimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 7),
    _MibProfIke_SaLife_TimeLimit_Type()
)
mibProfIke_SaLife_TimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLife_TimeLimit.setStatus("mandatory")
_MibProfIke_SaLife_SizeLimit_Type = Integer32
_MibProfIke_SaLife_SizeLimit_Object = MibScalar
mibProfIke_SaLife_SizeLimit = _MibProfIke_SaLife_SizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 8),
    _MibProfIke_SaLife_SizeLimit_Type()
)
mibProfIke_SaLife_SizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLife_SizeLimit.setStatus("mandatory")
_MibProfIke_SaLife_AnticipateRekey_Type = Integer32
_MibProfIke_SaLife_AnticipateRekey_Object = MibScalar
mibProfIke_SaLife_AnticipateRekey = _MibProfIke_SaLife_AnticipateRekey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 9),
    _MibProfIke_SaLife_AnticipateRekey_Type()
)
mibProfIke_SaLife_AnticipateRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLife_AnticipateRekey.setStatus("mandatory")


class _MibProfIke_SaLife_LifeNegotiationFallback_Type(Integer32):
    """Custom type mibProfIke_SaLife_LifeNegotiationFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("fail", 1),
          ("notification", 3))
    )


_MibProfIke_SaLife_LifeNegotiationFallback_Type.__name__ = "Integer32"
_MibProfIke_SaLife_LifeNegotiationFallback_Object = MibScalar
mibProfIke_SaLife_LifeNegotiationFallback = _MibProfIke_SaLife_LifeNegotiationFallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 10),
    _MibProfIke_SaLife_LifeNegotiationFallback_Type()
)
mibProfIke_SaLife_LifeNegotiationFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLife_LifeNegotiationFallback.setStatus("mandatory")
_MibProfIke_SaLife_IdleTimeout_Type = Integer32
_MibProfIke_SaLife_IdleTimeout_Object = MibScalar
mibProfIke_SaLife_IdleTimeout = _MibProfIke_SaLife_IdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 11),
    _MibProfIke_SaLife_IdleTimeout_Type()
)
mibProfIke_SaLife_IdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLife_IdleTimeout.setStatus("mandatory")
_MibProfIke_SaLimit_Type = Integer32
_MibProfIke_SaLimit_Object = MibScalar
mibProfIke_SaLimit = _MibProfIke_SaLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 12),
    _MibProfIke_SaLimit_Type()
)
mibProfIke_SaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_SaLimit.setStatus("mandatory")
_MibProfIke_Next_Type = DisplayString
_MibProfIke_Next_Object = MibScalar
mibProfIke_Next = _MibProfIke_Next_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 13),
    _MibProfIke_Next_Type()
)
mibProfIke_Next.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_Next.setStatus("mandatory")


class _MibProfIke_Action_o_Type(Integer32):
    """Custom type mibProfIke_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfIke_Action_o_Type.__name__ = "Integer32"
_MibProfIke_Action_o_Object = MibScalar
mibProfIke_Action_o = _MibProfIke_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 165, 1, 1, 14),
    _MibProfIke_Action_o_Type()
)
mibProfIke_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfIke_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIKE-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfIke": mibmibProfIke,
       "mibmibProfIkeTable": mibmibProfIkeTable,
       "mibmibProfIkeEntry": mibmibProfIkeEntry,
       "mibProfIke-IkeProtectionSuiteName": mibProfIke_IkeProtectionSuiteName,
       "mibProfIke-Phase1Mode": mibProfIke_Phase1Mode,
       "mibProfIke-EncryptionAlgorithm": mibProfIke_EncryptionAlgorithm,
       "mibProfIke-HashAlgorithm": mibProfIke_HashAlgorithm,
       "mibProfIke-AuthenticationMethod": mibProfIke_AuthenticationMethod,
       "mibProfIke-DiffieHellmanGroup": mibProfIke_DiffieHellmanGroup,
       "mibProfIke-SaLife-TimeLimit": mibProfIke_SaLife_TimeLimit,
       "mibProfIke-SaLife-SizeLimit": mibProfIke_SaLife_SizeLimit,
       "mibProfIke-SaLife-AnticipateRekey": mibProfIke_SaLife_AnticipateRekey,
       "mibProfIke-SaLife-LifeNegotiationFallback": mibProfIke_SaLife_LifeNegotiationFallback,
       "mibProfIke-SaLife-IdleTimeout": mibProfIke_SaLife_IdleTimeout,
       "mibProfIke-SaLimit": mibProfIke_SaLimit,
       "mibProfIke-Next": mibProfIke_Next,
       "mibProfIke-Action-o": mibProfIke_Action_o}
)
