# SNMP MIB module (ENTERASYS-SSH-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SSH-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:36 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysSshServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26)
)
etsysSshServerMIB.setRevisions(
        ("2003-02-19 19:03",
         "2002-11-14 15:41",
         "2002-09-27 17:48",
         "2002-09-18 20:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysSshObjects_ObjectIdentity = ObjectIdentity
etsysSshObjects = _EtsysSshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1)
)
_EtsysSshGeneralBranch_ObjectIdentity = ObjectIdentity
etsysSshGeneralBranch = _EtsysSshGeneralBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1)
)


class _EtsysSshEnabled_Type(TruthValue):
    """Custom type etsysSshEnabled based on TruthValue"""


_EtsysSshEnabled_Object = MibScalar
etsysSshEnabled = _EtsysSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 1),
    _EtsysSshEnabled_Type()
)
etsysSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshEnabled.setStatus("deprecated")


class _EtsysSshEventLogFilter_Type(Integer32):
    """Custom type etsysSshEventLogFilter based on Integer32"""
    defaultValue = 4

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
        *(("error", 4),
          ("information", 2),
          ("none", 1),
          ("warning", 3))
    )


_EtsysSshEventLogFilter_Type.__name__ = "Integer32"
_EtsysSshEventLogFilter_Object = MibScalar
etsysSshEventLogFilter = _EtsysSshEventLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 2),
    _EtsysSshEventLogFilter_Type()
)
etsysSshEventLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshEventLogFilter.setStatus("deprecated")


class _EtsysSshMaxConnections_Type(Integer32):
    """Custom type etsysSshMaxConnections based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysSshMaxConnections_Type.__name__ = "Integer32"
_EtsysSshMaxConnections_Object = MibScalar
etsysSshMaxConnections = _EtsysSshMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 3),
    _EtsysSshMaxConnections_Type()
)
etsysSshMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSshMaxConnections.setStatus("deprecated")


class _EtsysSshNumConnections_Type(Integer32):
    """Custom type etsysSshNumConnections based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EtsysSshNumConnections_Type.__name__ = "Integer32"
_EtsysSshNumConnections_Object = MibScalar
etsysSshNumConnections = _EtsysSshNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 4),
    _EtsysSshNumConnections_Type()
)
etsysSshNumConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshNumConnections.setStatus("deprecated")
_EtsysSshNetworkBranch_ObjectIdentity = ObjectIdentity
etsysSshNetworkBranch = _EtsysSshNetworkBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 2)
)
_EtsysSshCryptoBranch_ObjectIdentity = ObjectIdentity
etsysSshCryptoBranch = _EtsysSshCryptoBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3)
)


class _EtsysSshCiphers_Type(Integer32):
    """Custom type etsysSshCiphers based on Integer32"""
    defaultValue = 1

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
        *(("aes", 9),
          ("anyCipher", 2),
          ("anyStdCipher", 1),
          ("arcFour", 6),
          ("blowfish", 5),
          ("cast128", 8),
          ("des", 3),
          ("tripleDes", 4),
          ("twofish", 7))
    )


_EtsysSshCiphers_Type.__name__ = "Integer32"
_EtsysSshCiphers_Object = MibScalar
etsysSshCiphers = _EtsysSshCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 1),
    _EtsysSshCiphers_Type()
)
etsysSshCiphers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshCiphers.setStatus("deprecated")


class _EtsysSshMACs_Type(Integer32):
    """Custom type etsysSshMACs based on Integer32"""
    defaultValue = 1

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
        *(("anyMac", 2),
          ("anyStdMac", 1),
          ("hmacMd5", 5),
          ("hmacMd5Dash96", 6),
          ("hmacRipemd160", 7),
          ("hmacRipemd160Dash96", 8),
          ("hmacSha1", 3),
          ("hmacSha1Dash96", 4))
    )


_EtsysSshMACs_Type.__name__ = "Integer32"
_EtsysSshMACs_Object = MibScalar
etsysSshMACs = _EtsysSshMACs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 2),
    _EtsysSshMACs_Type()
)
etsysSshMACs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshMACs.setStatus("deprecated")


class _EtsysSshRekeyIntervalSeconds_Type(Integer32):
    """Custom type etsysSshRekeyIntervalSeconds based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysSshRekeyIntervalSeconds_Type.__name__ = "Integer32"
_EtsysSshRekeyIntervalSeconds_Object = MibScalar
etsysSshRekeyIntervalSeconds = _EtsysSshRekeyIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 3),
    _EtsysSshRekeyIntervalSeconds_Type()
)
etsysSshRekeyIntervalSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshRekeyIntervalSeconds.setStatus("deprecated")
if mibBuilder.loadTexts:
    etsysSshRekeyIntervalSeconds.setUnits("seconds")


class _EtsysSshRandomSeed_Type(OctetString):
    """Custom type etsysSshRandomSeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EtsysSshRandomSeed_Type.__name__ = "OctetString"
_EtsysSshRandomSeed_Object = MibScalar
etsysSshRandomSeed = _EtsysSshRandomSeed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 4),
    _EtsysSshRandomSeed_Type()
)
etsysSshRandomSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshRandomSeed.setStatus("deprecated")
_EtsysSshLoginBranch_ObjectIdentity = ObjectIdentity
etsysSshLoginBranch = _EtsysSshLoginBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4)
)


class _EtsysSshLoginGraceTime_Type(Integer32):
    """Custom type etsysSshLoginGraceTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_EtsysSshLoginGraceTime_Type.__name__ = "Integer32"
_EtsysSshLoginGraceTime_Object = MibScalar
etsysSshLoginGraceTime = _EtsysSshLoginGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 1),
    _EtsysSshLoginGraceTime_Type()
)
etsysSshLoginGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshLoginGraceTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    etsysSshLoginGraceTime.setUnits("seconds")


class _EtsysSshIdleTimeout_Type(Integer32):
    """Custom type etsysSshIdleTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysSshIdleTimeout_Type.__name__ = "Integer32"
_EtsysSshIdleTimeout_Object = MibScalar
etsysSshIdleTimeout = _EtsysSshIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 2),
    _EtsysSshIdleTimeout_Type()
)
etsysSshIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    etsysSshIdleTimeout.setUnits("minutes")


class _EtsysSshBannerMessage_Type(DisplayString):
    """Custom type etsysSshBannerMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysSshBannerMessage_Type.__name__ = "DisplayString"
_EtsysSshBannerMessage_Object = MibScalar
etsysSshBannerMessage = _EtsysSshBannerMessage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 3),
    _EtsysSshBannerMessage_Type()
)
etsysSshBannerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshBannerMessage.setStatus("deprecated")
_EtsysSshServerKeyBranch_ObjectIdentity = ObjectIdentity
etsysSshServerKeyBranch = _EtsysSshServerKeyBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5)
)


class _EtsysSshGenerateHostKeys_Type(Integer32):
    """Custom type etsysSshGenerateHostKeys based on Integer32"""
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
        *(("completed", 2),
          ("completedPending", 5),
          ("failed", 3),
          ("generate", 4),
          ("notInitiated", 1))
    )


_EtsysSshGenerateHostKeys_Type.__name__ = "Integer32"
_EtsysSshGenerateHostKeys_Object = MibScalar
etsysSshGenerateHostKeys = _EtsysSshGenerateHostKeys_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 1),
    _EtsysSshGenerateHostKeys_Type()
)
etsysSshGenerateHostKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshGenerateHostKeys.setStatus("deprecated")


class _EtsysSshPublicHostKey_Type(OctetString):
    """Custom type etsysSshPublicHostKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EtsysSshPublicHostKey_Type.__name__ = "OctetString"
_EtsysSshPublicHostKey_Object = MibScalar
etsysSshPublicHostKey = _EtsysSshPublicHostKey_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 2),
    _EtsysSshPublicHostKey_Type()
)
etsysSshPublicHostKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSshPublicHostKey.setStatus("deprecated")


class _EtsysSshAdminKeyType_Type(Integer32):
    """Custom type etsysSshAdminKeyType based on Integer32"""
    defaultValue = 4

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsa1024", 3),
          ("dsa2048", 5),
          ("dsa3072", 7),
          ("dsa512", 9),
          ("dsa768", 1),
          ("rsa1024", 4),
          ("rsa2048", 6),
          ("rsa3072", 8),
          ("rsa512", 10),
          ("rsa768", 2))
    )


_EtsysSshAdminKeyType_Type.__name__ = "Integer32"
_EtsysSshAdminKeyType_Object = MibScalar
etsysSshAdminKeyType = _EtsysSshAdminKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 3),
    _EtsysSshAdminKeyType_Type()
)
etsysSshAdminKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshAdminKeyType.setStatus("deprecated")


class _EtsysSshOperKeyType_Type(Integer32):
    """Custom type etsysSshOperKeyType based on Integer32"""
    defaultValue = 4

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
              99)
        )
    )
    namedValues = NamedValues(
        *(("dsa1024", 3),
          ("dsa2048", 5),
          ("dsa3072", 7),
          ("dsa512", 9),
          ("dsa768", 1),
          ("none", 99),
          ("rsa1024", 4),
          ("rsa2048", 6),
          ("rsa3072", 8),
          ("rsa512", 10),
          ("rsa768", 2))
    )


_EtsysSshOperKeyType_Type.__name__ = "Integer32"
_EtsysSshOperKeyType_Object = MibScalar
etsysSshOperKeyType = _EtsysSshOperKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 4),
    _EtsysSshOperKeyType_Type()
)
etsysSshOperKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSshOperKeyType.setStatus("deprecated")
_EtsysSshAuthBranch_ObjectIdentity = ObjectIdentity
etsysSshAuthBranch = _EtsysSshAuthBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6)
)


class _EtsysSshPasswordGuesses_Type(Integer32):
    """Custom type etsysSshPasswordGuesses based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EtsysSshPasswordGuesses_Type.__name__ = "Integer32"
_EtsysSshPasswordGuesses_Object = MibScalar
etsysSshPasswordGuesses = _EtsysSshPasswordGuesses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 1),
    _EtsysSshPasswordGuesses_Type()
)
etsysSshPasswordGuesses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshPasswordGuesses.setStatus("deprecated")


class _EtsysSshAllowedAuthentications_Type(Integer32):
    """Custom type etsysSshAllowedAuthentications based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allAuth", 1),
          ("password", 2),
          ("publickey", 3))
    )


_EtsysSshAllowedAuthentications_Type.__name__ = "Integer32"
_EtsysSshAllowedAuthentications_Object = MibScalar
etsysSshAllowedAuthentications = _EtsysSshAllowedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 2),
    _EtsysSshAllowedAuthentications_Type()
)
etsysSshAllowedAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshAllowedAuthentications.setStatus("deprecated")


class _EtsysSshRequiredAuthentications_Type(Integer32):
    """Custom type etsysSshRequiredAuthentications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("password", 2),
          ("publickey", 3))
    )


_EtsysSshRequiredAuthentications_Type.__name__ = "Integer32"
_EtsysSshRequiredAuthentications_Object = MibScalar
etsysSshRequiredAuthentications = _EtsysSshRequiredAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 3),
    _EtsysSshRequiredAuthentications_Type()
)
etsysSshRequiredAuthentications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSshRequiredAuthentications.setStatus("deprecated")
_EtsysSshConformance_ObjectIdentity = ObjectIdentity
etsysSshConformance = _EtsysSshConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2)
)
_EtsysSshGroups_ObjectIdentity = ObjectIdentity
etsysSshGroups = _EtsysSshGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1)
)
_EtsysSshCompliances_ObjectIdentity = ObjectIdentity
etsysSshCompliances = _EtsysSshCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 2)
)

# Managed Objects groups

etsysSshBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 1)
)
etsysSshBaseGroup.setObjects(
      *(("ENTERASYS-SSH-SERVER-MIB", "etsysSshEnabled"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshMaxConnections"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshNumConnections"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshCiphers"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshMACs"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRekeyIntervalSeconds"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRandomSeed"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshGenerateHostKeys"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshPublicHostKey"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshAdminKeyType"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshOperKeyType"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshAllowedAuthentications"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRequiredAuthentications"))
)
if mibBuilder.loadTexts:
    etsysSshBaseGroup.setStatus("deprecated")

etsysSshAdvancedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 2)
)
etsysSshAdvancedGroup.setObjects(
      *(("ENTERASYS-SSH-SERVER-MIB", "etsysSshBannerMessage"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshLoginGraceTime"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshIdleTimeout"),
        ("ENTERASYS-SSH-SERVER-MIB", "etsysSshPasswordGuesses"))
)
if mibBuilder.loadTexts:
    etsysSshAdvancedGroup.setStatus("deprecated")

etsysSshEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 3)
)
etsysSshEventLogGroup.setObjects(
    ("ENTERASYS-SSH-SERVER-MIB", "etsysSshEventLogFilter")
)
if mibBuilder.loadTexts:
    etsysSshEventLogGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysSshCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSshCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SSH-SERVER-MIB",
    **{"etsysSshServerMIB": etsysSshServerMIB,
       "etsysSshObjects": etsysSshObjects,
       "etsysSshGeneralBranch": etsysSshGeneralBranch,
       "etsysSshEnabled": etsysSshEnabled,
       "etsysSshEventLogFilter": etsysSshEventLogFilter,
       "etsysSshMaxConnections": etsysSshMaxConnections,
       "etsysSshNumConnections": etsysSshNumConnections,
       "etsysSshNetworkBranch": etsysSshNetworkBranch,
       "etsysSshCryptoBranch": etsysSshCryptoBranch,
       "etsysSshCiphers": etsysSshCiphers,
       "etsysSshMACs": etsysSshMACs,
       "etsysSshRekeyIntervalSeconds": etsysSshRekeyIntervalSeconds,
       "etsysSshRandomSeed": etsysSshRandomSeed,
       "etsysSshLoginBranch": etsysSshLoginBranch,
       "etsysSshLoginGraceTime": etsysSshLoginGraceTime,
       "etsysSshIdleTimeout": etsysSshIdleTimeout,
       "etsysSshBannerMessage": etsysSshBannerMessage,
       "etsysSshServerKeyBranch": etsysSshServerKeyBranch,
       "etsysSshGenerateHostKeys": etsysSshGenerateHostKeys,
       "etsysSshPublicHostKey": etsysSshPublicHostKey,
       "etsysSshAdminKeyType": etsysSshAdminKeyType,
       "etsysSshOperKeyType": etsysSshOperKeyType,
       "etsysSshAuthBranch": etsysSshAuthBranch,
       "etsysSshPasswordGuesses": etsysSshPasswordGuesses,
       "etsysSshAllowedAuthentications": etsysSshAllowedAuthentications,
       "etsysSshRequiredAuthentications": etsysSshRequiredAuthentications,
       "etsysSshConformance": etsysSshConformance,
       "etsysSshGroups": etsysSshGroups,
       "etsysSshBaseGroup": etsysSshBaseGroup,
       "etsysSshAdvancedGroup": etsysSshAdvancedGroup,
       "etsysSshEventLogGroup": etsysSshEventLogGroup,
       "etsysSshCompliances": etsysSshCompliances,
       "etsysSshCompliance": etsysSshCompliance}
)
