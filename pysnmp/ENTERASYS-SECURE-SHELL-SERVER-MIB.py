# SNMP MIB module (ENTERASYS-SECURE-SHELL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SECURE-SHELL-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:32 2024
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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

etsysSecureShellServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36)
)
etsysSecureShellServerMIB.setRevisions(
        ("2003-02-12 17:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SshCipherList(Bits, TextualConvention):
    status = "current"


class SshMacList(Bits, TextualConvention):
    status = "current"


class HexString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysSecureShellServer_ObjectIdentity = ObjectIdentity
etsysSecureShellServer = _EtsysSecureShellServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1)
)
_EtsysSecureShellServerConfig_ObjectIdentity = ObjectIdentity
etsysSecureShellServerConfig = _EtsysSecureShellServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1)
)


class _EtsysSecureShellServerAdminStatus_Type(Integer32):
    """Custom type etsysSecureShellServerAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("reinitialize", 3))
    )


_EtsysSecureShellServerAdminStatus_Type.__name__ = "Integer32"
_EtsysSecureShellServerAdminStatus_Object = MibScalar
etsysSecureShellServerAdminStatus = _EtsysSecureShellServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 1),
    _EtsysSecureShellServerAdminStatus_Type()
)
etsysSecureShellServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSecureShellServerAdminStatus.setStatus("current")


class _EtsysSecureShellServerOperStatus_Type(Integer32):
    """Custom type etsysSecureShellServerOperStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_EtsysSecureShellServerOperStatus_Type.__name__ = "Integer32"
_EtsysSecureShellServerOperStatus_Object = MibScalar
etsysSecureShellServerOperStatus = _EtsysSecureShellServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 2),
    _EtsysSecureShellServerOperStatus_Type()
)
etsysSecureShellServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerOperStatus.setStatus("current")


class _EtsysSecureShellServerErrorStatus_Type(SnmpAdminString):
    """Custom type etsysSecureShellServerErrorStatus based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysSecureShellServerErrorStatus_Object = MibScalar
etsysSecureShellServerErrorStatus = _EtsysSecureShellServerErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 3),
    _EtsysSecureShellServerErrorStatus_Type()
)
etsysSecureShellServerErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerErrorStatus.setStatus("current")


class _EtsysSecureShellServerAdminPort_Type(Unsigned32):
    """Custom type etsysSecureShellServerAdminPort based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSecureShellServerAdminPort_Type.__name__ = "Unsigned32"
_EtsysSecureShellServerAdminPort_Object = MibScalar
etsysSecureShellServerAdminPort = _EtsysSecureShellServerAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 4),
    _EtsysSecureShellServerAdminPort_Type()
)
etsysSecureShellServerAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSecureShellServerAdminPort.setStatus("current")
_EtsysSecureShellServerOperPort_Type = Unsigned32
_EtsysSecureShellServerOperPort_Object = MibScalar
etsysSecureShellServerOperPort = _EtsysSecureShellServerOperPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 5),
    _EtsysSecureShellServerOperPort_Type()
)
etsysSecureShellServerOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerOperPort.setStatus("current")
_EtsysSecureShellServerMac_ObjectIdentity = ObjectIdentity
etsysSecureShellServerMac = _EtsysSecureShellServerMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2)
)
_EtsysSecureShellServerSupportedMacs_Type = SshMacList
_EtsysSecureShellServerSupportedMacs_Object = MibScalar
etsysSecureShellServerSupportedMacs = _EtsysSecureShellServerSupportedMacs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 1),
    _EtsysSecureShellServerSupportedMacs_Type()
)
etsysSecureShellServerSupportedMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerSupportedMacs.setStatus("current")
_EtsysSecureShellServerAdminMacs_Type = SshMacList
_EtsysSecureShellServerAdminMacs_Object = MibScalar
etsysSecureShellServerAdminMacs = _EtsysSecureShellServerAdminMacs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 2),
    _EtsysSecureShellServerAdminMacs_Type()
)
etsysSecureShellServerAdminMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSecureShellServerAdminMacs.setStatus("current")
_EtsysSecureShellServerOperMacs_Type = SshMacList
_EtsysSecureShellServerOperMacs_Object = MibScalar
etsysSecureShellServerOperMacs = _EtsysSecureShellServerOperMacs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 3),
    _EtsysSecureShellServerOperMacs_Type()
)
etsysSecureShellServerOperMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerOperMacs.setStatus("current")
_EtsysSecureShellServerCipher_ObjectIdentity = ObjectIdentity
etsysSecureShellServerCipher = _EtsysSecureShellServerCipher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3)
)
_EtsysSecureShellServerSupportedCiphers_Type = SshCipherList
_EtsysSecureShellServerSupportedCiphers_Object = MibScalar
etsysSecureShellServerSupportedCiphers = _EtsysSecureShellServerSupportedCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 1),
    _EtsysSecureShellServerSupportedCiphers_Type()
)
etsysSecureShellServerSupportedCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerSupportedCiphers.setStatus("current")
_EtsysSecureShellServerAdminCiphers_Type = SshCipherList
_EtsysSecureShellServerAdminCiphers_Object = MibScalar
etsysSecureShellServerAdminCiphers = _EtsysSecureShellServerAdminCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 2),
    _EtsysSecureShellServerAdminCiphers_Type()
)
etsysSecureShellServerAdminCiphers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSecureShellServerAdminCiphers.setStatus("current")
_EtsysSecureShellServerOperCiphers_Type = SshCipherList
_EtsysSecureShellServerOperCiphers_Object = MibScalar
etsysSecureShellServerOperCiphers = _EtsysSecureShellServerOperCiphers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 3),
    _EtsysSecureShellServerOperCiphers_Type()
)
etsysSecureShellServerOperCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerOperCiphers.setStatus("current")
_EtsysSecureShellServerHostKey_ObjectIdentity = ObjectIdentity
etsysSecureShellServerHostKey = _EtsysSecureShellServerHostKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4)
)
_EtsysSecureShellServerHostKeyTable_Object = MibTable
etsysSecureShellServerHostKeyTable = _EtsysSecureShellServerHostKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyTable.setStatus("current")
_EtsysSecureShellServerHostKeyEntry_Object = MibTableRow
etsysSecureShellServerHostKeyEntry = _EtsysSecureShellServerHostKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1)
)
etsysSecureShellServerHostKeyEntry.setIndexNames(
    (0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyType"),
    (0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeySize"),
)
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyEntry.setStatus("current")


class _EtsysSecureShellServerHostKeyType_Type(Integer32):
    """Custom type etsysSecureShellServerHostKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sshDss", 1),
          ("sshRsa", 2))
    )


_EtsysSecureShellServerHostKeyType_Type.__name__ = "Integer32"
_EtsysSecureShellServerHostKeyType_Object = MibTableColumn
etsysSecureShellServerHostKeyType = _EtsysSecureShellServerHostKeyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 1),
    _EtsysSecureShellServerHostKeyType_Type()
)
etsysSecureShellServerHostKeyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyType.setStatus("current")


class _EtsysSecureShellServerHostKeySize_Type(Integer32):
    """Custom type etsysSecureShellServerHostKeySize based on Integer32"""
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
        *(("bits1024", 3),
          ("bits2048", 4),
          ("bits512", 1),
          ("bits768", 2))
    )


_EtsysSecureShellServerHostKeySize_Type.__name__ = "Integer32"
_EtsysSecureShellServerHostKeySize_Object = MibTableColumn
etsysSecureShellServerHostKeySize = _EtsysSecureShellServerHostKeySize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 2),
    _EtsysSecureShellServerHostKeySize_Type()
)
etsysSecureShellServerHostKeySize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeySize.setStatus("current")
_EtsysSecureShellServerHostKeyDate_Type = DateAndTime
_EtsysSecureShellServerHostKeyDate_Object = MibTableColumn
etsysSecureShellServerHostKeyDate = _EtsysSecureShellServerHostKeyDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 3),
    _EtsysSecureShellServerHostKeyDate_Type()
)
etsysSecureShellServerHostKeyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyDate.setStatus("current")


class _EtsysSecureShellServerHostKeyOperStatus_Type(Bits):
    """Custom type etsysSecureShellServerHostKeyOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("completed", 2),
          ("failed", 4),
          ("initializing", 0),
          ("operational", 1),
          ("pending", 3))
    )

_EtsysSecureShellServerHostKeyOperStatus_Type.__name__ = "Bits"
_EtsysSecureShellServerHostKeyOperStatus_Object = MibTableColumn
etsysSecureShellServerHostKeyOperStatus = _EtsysSecureShellServerHostKeyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 4),
    _EtsysSecureShellServerHostKeyOperStatus_Type()
)
etsysSecureShellServerHostKeyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyOperStatus.setStatus("current")


class _EtsysSecureShellServerHostKeyAdminStatus_Type(Integer32):
    """Custom type etsysSecureShellServerHostKeyAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("reinitialize", 2))
    )


_EtsysSecureShellServerHostKeyAdminStatus_Type.__name__ = "Integer32"
_EtsysSecureShellServerHostKeyAdminStatus_Object = MibTableColumn
etsysSecureShellServerHostKeyAdminStatus = _EtsysSecureShellServerHostKeyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 5),
    _EtsysSecureShellServerHostKeyAdminStatus_Type()
)
etsysSecureShellServerHostKeyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyAdminStatus.setStatus("current")


class _EtsysSecureShellServerHostKeyFingerprint_Type(HexString):
    """Custom type etsysSecureShellServerHostKeyFingerprint based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtsysSecureShellServerHostKeyFingerprint_Type.__name__ = "HexString"
_EtsysSecureShellServerHostKeyFingerprint_Object = MibTableColumn
etsysSecureShellServerHostKeyFingerprint = _EtsysSecureShellServerHostKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 6),
    _EtsysSecureShellServerHostKeyFingerprint_Type()
)
etsysSecureShellServerHostKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyFingerprint.setStatus("current")


class _EtsysSecureShellServerHostKeyErrorStatus_Type(SnmpAdminString):
    """Custom type etsysSecureShellServerHostKeyErrorStatus based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysSecureShellServerHostKeyErrorStatus_Object = MibTableColumn
etsysSecureShellServerHostKeyErrorStatus = _EtsysSecureShellServerHostKeyErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 7),
    _EtsysSecureShellServerHostKeyErrorStatus_Type()
)
etsysSecureShellServerHostKeyErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyErrorStatus.setStatus("current")


class _EtsysSecureShellServerHostKeyStorageType_Type(StorageType):
    """Custom type etsysSecureShellServerHostKeyStorageType based on StorageType"""


_EtsysSecureShellServerHostKeyStorageType_Object = MibTableColumn
etsysSecureShellServerHostKeyStorageType = _EtsysSecureShellServerHostKeyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 8),
    _EtsysSecureShellServerHostKeyStorageType_Type()
)
etsysSecureShellServerHostKeyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyStorageType.setStatus("current")
_EtsysSecureShellServerHostKeyRowStatus_Type = RowStatus
_EtsysSecureShellServerHostKeyRowStatus_Object = MibTableColumn
etsysSecureShellServerHostKeyRowStatus = _EtsysSecureShellServerHostKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 9),
    _EtsysSecureShellServerHostKeyRowStatus_Type()
)
etsysSecureShellServerHostKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyRowStatus.setStatus("current")
_EtsysSecureShellServerConformance_ObjectIdentity = ObjectIdentity
etsysSecureShellServerConformance = _EtsysSecureShellServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2)
)
_EtsysSecureShellServerGroups_ObjectIdentity = ObjectIdentity
etsysSecureShellServerGroups = _EtsysSecureShellServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1)
)
_EtsysSecureShellServerCompliances_ObjectIdentity = ObjectIdentity
etsysSecureShellServerCompliances = _EtsysSecureShellServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2)
)

# Managed Objects groups

etsysSecureShellServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 1)
)
etsysSecureShellServerConfigGroup.setObjects(
      *(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminStatus"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperStatus"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminPort"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperPort"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedMacs"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminMacs"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperMacs"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedCiphers"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminCiphers"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperCiphers"))
)
if mibBuilder.loadTexts:
    etsysSecureShellServerConfigGroup.setStatus("current")

etsysSecureShellServerHostKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 2)
)
etsysSecureShellServerHostKeyGroup.setObjects(
      *(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyDate"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyOperStatus"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyAdminStatus"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyFingerprint"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyErrorStatus"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyStorageType"),
        ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyRowStatus"))
)
if mibBuilder.loadTexts:
    etsysSecureShellServerHostKeyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysSecureShellServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSecureShellServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SECURE-SHELL-SERVER-MIB",
    **{"SshCipherList": SshCipherList,
       "SshMacList": SshMacList,
       "HexString": HexString,
       "etsysSecureShellServerMIB": etsysSecureShellServerMIB,
       "etsysSecureShellServer": etsysSecureShellServer,
       "etsysSecureShellServerConfig": etsysSecureShellServerConfig,
       "etsysSecureShellServerAdminStatus": etsysSecureShellServerAdminStatus,
       "etsysSecureShellServerOperStatus": etsysSecureShellServerOperStatus,
       "etsysSecureShellServerErrorStatus": etsysSecureShellServerErrorStatus,
       "etsysSecureShellServerAdminPort": etsysSecureShellServerAdminPort,
       "etsysSecureShellServerOperPort": etsysSecureShellServerOperPort,
       "etsysSecureShellServerMac": etsysSecureShellServerMac,
       "etsysSecureShellServerSupportedMacs": etsysSecureShellServerSupportedMacs,
       "etsysSecureShellServerAdminMacs": etsysSecureShellServerAdminMacs,
       "etsysSecureShellServerOperMacs": etsysSecureShellServerOperMacs,
       "etsysSecureShellServerCipher": etsysSecureShellServerCipher,
       "etsysSecureShellServerSupportedCiphers": etsysSecureShellServerSupportedCiphers,
       "etsysSecureShellServerAdminCiphers": etsysSecureShellServerAdminCiphers,
       "etsysSecureShellServerOperCiphers": etsysSecureShellServerOperCiphers,
       "etsysSecureShellServerHostKey": etsysSecureShellServerHostKey,
       "etsysSecureShellServerHostKeyTable": etsysSecureShellServerHostKeyTable,
       "etsysSecureShellServerHostKeyEntry": etsysSecureShellServerHostKeyEntry,
       "etsysSecureShellServerHostKeyType": etsysSecureShellServerHostKeyType,
       "etsysSecureShellServerHostKeySize": etsysSecureShellServerHostKeySize,
       "etsysSecureShellServerHostKeyDate": etsysSecureShellServerHostKeyDate,
       "etsysSecureShellServerHostKeyOperStatus": etsysSecureShellServerHostKeyOperStatus,
       "etsysSecureShellServerHostKeyAdminStatus": etsysSecureShellServerHostKeyAdminStatus,
       "etsysSecureShellServerHostKeyFingerprint": etsysSecureShellServerHostKeyFingerprint,
       "etsysSecureShellServerHostKeyErrorStatus": etsysSecureShellServerHostKeyErrorStatus,
       "etsysSecureShellServerHostKeyStorageType": etsysSecureShellServerHostKeyStorageType,
       "etsysSecureShellServerHostKeyRowStatus": etsysSecureShellServerHostKeyRowStatus,
       "etsysSecureShellServerConformance": etsysSecureShellServerConformance,
       "etsysSecureShellServerGroups": etsysSecureShellServerGroups,
       "etsysSecureShellServerConfigGroup": etsysSecureShellServerConfigGroup,
       "etsysSecureShellServerHostKeyGroup": etsysSecureShellServerHostKeyGroup,
       "etsysSecureShellServerCompliances": etsysSecureShellServerCompliances,
       "etsysSecureShellServerCompliance": etsysSecureShellServerCompliance}
)
