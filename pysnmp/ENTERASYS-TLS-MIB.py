# SNMP MIB module (ENTERASYS-TLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-TLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:39 2024
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

etsysTlsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30)
)
etsysTlsMIB.setRevisions(
        ("2002-11-14 15:34",
         "2002-11-01 21:09")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysTlsObjects_ObjectIdentity = ObjectIdentity
etsysTlsObjects = _EtsysTlsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1)
)
_EtsysTlsGeneralBranch_ObjectIdentity = ObjectIdentity
etsysTlsGeneralBranch = _EtsysTlsGeneralBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 1)
)


class _EtsysTlsEnabled_Type(Integer32):
    """Custom type etsysTlsEnabled based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("reinitialize", 3))
    )


_EtsysTlsEnabled_Type.__name__ = "Integer32"
_EtsysTlsEnabled_Object = MibScalar
etsysTlsEnabled = _EtsysTlsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 1, 1),
    _EtsysTlsEnabled_Type()
)
etsysTlsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsEnabled.setStatus("current")


class _EtsysTlsNumSoftConnects_Type(Integer32):
    """Custom type etsysTlsNumSoftConnects based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTlsNumSoftConnects_Type.__name__ = "Integer32"
_EtsysTlsNumSoftConnects_Object = MibScalar
etsysTlsNumSoftConnects = _EtsysTlsNumSoftConnects_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 1, 2),
    _EtsysTlsNumSoftConnects_Type()
)
etsysTlsNumSoftConnects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsNumSoftConnects.setStatus("current")


class _EtsysTlsNumHardConnects_Type(Integer32):
    """Custom type etsysTlsNumHardConnects based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTlsNumHardConnects_Type.__name__ = "Integer32"
_EtsysTlsNumHardConnects_Object = MibScalar
etsysTlsNumHardConnects = _EtsysTlsNumHardConnects_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 1, 3),
    _EtsysTlsNumHardConnects_Type()
)
etsysTlsNumHardConnects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsNumHardConnects.setStatus("current")


class _EtsysTlsMaxHardConnects_Type(Integer32):
    """Custom type etsysTlsMaxHardConnects based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTlsMaxHardConnects_Type.__name__ = "Integer32"
_EtsysTlsMaxHardConnects_Object = MibScalar
etsysTlsMaxHardConnects = _EtsysTlsMaxHardConnects_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 1, 4),
    _EtsysTlsMaxHardConnects_Type()
)
etsysTlsMaxHardConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTlsMaxHardConnects.setStatus("current")
_EtsysTlsNetworkBranch_ObjectIdentity = ObjectIdentity
etsysTlsNetworkBranch = _EtsysTlsNetworkBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 2)
)


class _EtsysTlsKeepOpenTimeout_Type(Integer32):
    """Custom type etsysTlsKeepOpenTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTlsKeepOpenTimeout_Type.__name__ = "Integer32"
_EtsysTlsKeepOpenTimeout_Object = MibScalar
etsysTlsKeepOpenTimeout = _EtsysTlsKeepOpenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 2, 1),
    _EtsysTlsKeepOpenTimeout_Type()
)
etsysTlsKeepOpenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsKeepOpenTimeout.setStatus("current")


class _EtsysTlsHttpsPort_Type(Integer32):
    """Custom type etsysTlsHttpsPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTlsHttpsPort_Type.__name__ = "Integer32"
_EtsysTlsHttpsPort_Object = MibScalar
etsysTlsHttpsPort = _EtsysTlsHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 2, 2),
    _EtsysTlsHttpsPort_Type()
)
etsysTlsHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsHttpsPort.setStatus("current")
_EtsysTlsServerKeyBranch_ObjectIdentity = ObjectIdentity
etsysTlsServerKeyBranch = _EtsysTlsServerKeyBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 3)
)


class _EtsysTlsGenerateKeys_Type(Integer32):
    """Custom type etsysTlsGenerateKeys based on Integer32"""
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


_EtsysTlsGenerateKeys_Type.__name__ = "Integer32"
_EtsysTlsGenerateKeys_Object = MibScalar
etsysTlsGenerateKeys = _EtsysTlsGenerateKeys_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 3, 1),
    _EtsysTlsGenerateKeys_Type()
)
etsysTlsGenerateKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsGenerateKeys.setStatus("current")


class _EtsysTlsAdminKeyType_Type(Integer32):
    """Custom type etsysTlsAdminKeyType based on Integer32"""
    defaultValue = 2

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
        *(("dsa1024", 5),
          ("dsa2048", 7),
          ("dsa3072", 9),
          ("dsa512", 1),
          ("dsa768", 3),
          ("rsa1024", 6),
          ("rsa2048", 8),
          ("rsa3072", 10),
          ("rsa512", 2),
          ("rsa768", 4))
    )


_EtsysTlsAdminKeyType_Type.__name__ = "Integer32"
_EtsysTlsAdminKeyType_Object = MibScalar
etsysTlsAdminKeyType = _EtsysTlsAdminKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 3, 2),
    _EtsysTlsAdminKeyType_Type()
)
etsysTlsAdminKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsAdminKeyType.setStatus("current")


class _EtsysTlsOperKeyType_Type(Integer32):
    """Custom type etsysTlsOperKeyType based on Integer32"""
    defaultValue = 2

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
        *(("dsa1024", 5),
          ("dsa2048", 7),
          ("dsa3072", 9),
          ("dsa512", 1),
          ("dsa768", 3),
          ("none", 99),
          ("rsa1024", 6),
          ("rsa2048", 8),
          ("rsa3072", 10),
          ("rsa512", 2),
          ("rsa768", 4))
    )


_EtsysTlsOperKeyType_Type.__name__ = "Integer32"
_EtsysTlsOperKeyType_Object = MibScalar
etsysTlsOperKeyType = _EtsysTlsOperKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 3, 3),
    _EtsysTlsOperKeyType_Type()
)
etsysTlsOperKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTlsOperKeyType.setStatus("current")


class _EtsysTlsSignatureType_Type(Integer32):
    """Custom type etsysTlsSignatureType based on Integer32"""
    defaultValue = 1

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
        *(("dhAnon", 1),
          ("dsaSha", 3),
          ("dsaSha1", 2),
          ("rsaMd2", 5),
          ("rsaMd5", 6),
          ("rsaSha1", 4))
    )


_EtsysTlsSignatureType_Type.__name__ = "Integer32"
_EtsysTlsSignatureType_Object = MibScalar
etsysTlsSignatureType = _EtsysTlsSignatureType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 1, 3, 4),
    _EtsysTlsSignatureType_Type()
)
etsysTlsSignatureType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTlsSignatureType.setStatus("current")
_EtsysTlsConformance_ObjectIdentity = ObjectIdentity
etsysTlsConformance = _EtsysTlsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 2)
)
_EtsysTlsGroups_ObjectIdentity = ObjectIdentity
etsysTlsGroups = _EtsysTlsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 2, 1)
)
_EtsysTlsCompliances_ObjectIdentity = ObjectIdentity
etsysTlsCompliances = _EtsysTlsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 2, 2)
)

# Managed Objects groups

etsysTlsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 2, 1, 1)
)
etsysTlsBaseGroup.setObjects(
      *(("ENTERASYS-TLS-MIB", "etsysTlsEnabled"),
        ("ENTERASYS-TLS-MIB", "etsysTlsNumSoftConnects"),
        ("ENTERASYS-TLS-MIB", "etsysTlsNumHardConnects"),
        ("ENTERASYS-TLS-MIB", "etsysTlsMaxHardConnects"),
        ("ENTERASYS-TLS-MIB", "etsysTlsKeepOpenTimeout"),
        ("ENTERASYS-TLS-MIB", "etsysTlsHttpsPort"),
        ("ENTERASYS-TLS-MIB", "etsysTlsGenerateKeys"),
        ("ENTERASYS-TLS-MIB", "etsysTlsAdminKeyType"),
        ("ENTERASYS-TLS-MIB", "etsysTlsOperKeyType"),
        ("ENTERASYS-TLS-MIB", "etsysTlsSignatureType"))
)
if mibBuilder.loadTexts:
    etsysTlsBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysTlsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 30, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTlsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-TLS-MIB",
    **{"etsysTlsMIB": etsysTlsMIB,
       "etsysTlsObjects": etsysTlsObjects,
       "etsysTlsGeneralBranch": etsysTlsGeneralBranch,
       "etsysTlsEnabled": etsysTlsEnabled,
       "etsysTlsNumSoftConnects": etsysTlsNumSoftConnects,
       "etsysTlsNumHardConnects": etsysTlsNumHardConnects,
       "etsysTlsMaxHardConnects": etsysTlsMaxHardConnects,
       "etsysTlsNetworkBranch": etsysTlsNetworkBranch,
       "etsysTlsKeepOpenTimeout": etsysTlsKeepOpenTimeout,
       "etsysTlsHttpsPort": etsysTlsHttpsPort,
       "etsysTlsServerKeyBranch": etsysTlsServerKeyBranch,
       "etsysTlsGenerateKeys": etsysTlsGenerateKeys,
       "etsysTlsAdminKeyType": etsysTlsAdminKeyType,
       "etsysTlsOperKeyType": etsysTlsOperKeyType,
       "etsysTlsSignatureType": etsysTlsSignatureType,
       "etsysTlsConformance": etsysTlsConformance,
       "etsysTlsGroups": etsysTlsGroups,
       "etsysTlsBaseGroup": etsysTlsBaseGroup,
       "etsysTlsCompliances": etsysTlsCompliances,
       "etsysTlsCompliance": etsysTlsCompliance}
)
