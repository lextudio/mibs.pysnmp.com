# SNMP MIB module (FNKSBRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNKSBRTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:19 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Funk_ObjectIdentity = ObjectIdentity
funk = _Funk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411)
)
_FunkSbr_ObjectIdentity = ObjectIdentity
funkSbr = _FunkSbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411, 1)
)
_FunkSbrTraps_ObjectIdentity = ObjectIdentity
funkSbrTraps = _FunkSbrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1)
)
_FunkSbrTrapVars_ObjectIdentity = ObjectIdentity
funkSbrTrapVars = _FunkSbrTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1)
)


class _FunkSbrTrapVarComp_Type(Integer32):
    """Custom type funkSbrTrapVarComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authentication", 3),
          ("core", 1))
    )


_FunkSbrTrapVarComp_Type.__name__ = "Integer32"
_FunkSbrTrapVarComp_Object = MibScalar
funkSbrTrapVarComp = _FunkSbrTrapVarComp_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 1),
    _FunkSbrTrapVarComp_Type()
)
funkSbrTrapVarComp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarComp.setStatus("optional")


class _FunkSbrTrapVarSev_Type(Integer32):
    """Custom type funkSbrTrapVarSev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("informational", 1),
          ("warning", 2))
    )


_FunkSbrTrapVarSev_Type.__name__ = "Integer32"
_FunkSbrTrapVarSev_Object = MibScalar
funkSbrTrapVarSev = _FunkSbrTrapVarSev_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 2),
    _FunkSbrTrapVarSev_Type()
)
funkSbrTrapVarSev.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSev.setStatus("optional")


class _FunkSbrTrapVarSWName_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarSWName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarSWName_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarSWName_Object = MibScalar
funkSbrTrapVarSWName = _FunkSbrTrapVarSWName_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 3),
    _FunkSbrTrapVarSWName_Type()
)
funkSbrTrapVarSWName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSWName.setStatus("optional")


class _FunkSbrTrapVarThreadsAvail_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarThreadsAvail based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarThreadsAvail_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarThreadsAvail_Object = MibScalar
funkSbrTrapVarThreadsAvail = _FunkSbrTrapVarThreadsAvail_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 4),
    _FunkSbrTrapVarThreadsAvail_Type()
)
funkSbrTrapVarThreadsAvail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarThreadsAvail.setStatus("optional")


class _FunkSbrTrapVarBytesAvail_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarBytesAvail based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FunkSbrTrapVarBytesAvail_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarBytesAvail_Object = MibScalar
funkSbrTrapVarBytesAvail = _FunkSbrTrapVarBytesAvail_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 5),
    _FunkSbrTrapVarBytesAvail_Type()
)
funkSbrTrapVarBytesAvail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarBytesAvail.setStatus("optional")


class _FunkSbrTrapVarPrivateDir_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarPrivateDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarPrivateDir_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarPrivateDir_Object = MibScalar
funkSbrTrapVarPrivateDir = _FunkSbrTrapVarPrivateDir_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 6),
    _FunkSbrTrapVarPrivateDir_Type()
)
funkSbrTrapVarPrivateDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarPrivateDir.setStatus("optional")


class _FunkSbrTrapVarNumberOfOccurrences_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarNumberOfOccurrences based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarNumberOfOccurrences_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarNumberOfOccurrences_Object = MibScalar
funkSbrTrapVarNumberOfOccurrences = _FunkSbrTrapVarNumberOfOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 7),
    _FunkSbrTrapVarNumberOfOccurrences_Type()
)
funkSbrTrapVarNumberOfOccurrences.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarNumberOfOccurrences.setStatus("optional")


class _FunkSbrTrapVarSQLConnects_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarSQLConnects based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarSQLConnects_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarSQLConnects_Object = MibScalar
funkSbrTrapVarSQLConnects = _FunkSbrTrapVarSQLConnects_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 8),
    _FunkSbrTrapVarSQLConnects_Type()
)
funkSbrTrapVarSQLConnects.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSQLConnects.setStatus("optional")


class _FunkSbrTrapVarSQLDisconnects_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarSQLDisconnects based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarSQLDisconnects_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarSQLDisconnects_Object = MibScalar
funkSbrTrapVarSQLDisconnects = _FunkSbrTrapVarSQLDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 9),
    _FunkSbrTrapVarSQLDisconnects_Type()
)
funkSbrTrapVarSQLDisconnects.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSQLDisconnects.setStatus("optional")


class _FunkSbrTrapVarSQLTimeouts_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarSQLTimeouts based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarSQLTimeouts_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarSQLTimeouts_Object = MibScalar
funkSbrTrapVarSQLTimeouts = _FunkSbrTrapVarSQLTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 10),
    _FunkSbrTrapVarSQLTimeouts_Type()
)
funkSbrTrapVarSQLTimeouts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSQLTimeouts.setStatus("optional")


class _FunkSbrTrapVarServiceDispatcherErrCode_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarServiceDispatcherErrCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarServiceDispatcherErrCode_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarServiceDispatcherErrCode_Object = MibScalar
funkSbrTrapVarServiceDispatcherErrCode = _FunkSbrTrapVarServiceDispatcherErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 11),
    _FunkSbrTrapVarServiceDispatcherErrCode_Type()
)
funkSbrTrapVarServiceDispatcherErrCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarServiceDispatcherErrCode.setStatus("optional")


class _FunkSbrTrapVarSetStatusErrCode_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarSetStatusErrCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarSetStatusErrCode_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarSetStatusErrCode_Object = MibScalar
funkSbrTrapVarSetStatusErrCode = _FunkSbrTrapVarSetStatusErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 12),
    _FunkSbrTrapVarSetStatusErrCode_Type()
)
funkSbrTrapVarSetStatusErrCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarSetStatusErrCode.setStatus("optional")


class _FunkSbrTrapVarGetDiskFreeSpaceErrCode_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarGetDiskFreeSpaceErrCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FunkSbrTrapVarGetDiskFreeSpaceErrCode_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarGetDiskFreeSpaceErrCode_Object = MibScalar
funkSbrTrapVarGetDiskFreeSpaceErrCode = _FunkSbrTrapVarGetDiskFreeSpaceErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 13),
    _FunkSbrTrapVarGetDiskFreeSpaceErrCode_Type()
)
funkSbrTrapVarGetDiskFreeSpaceErrCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarGetDiskFreeSpaceErrCode.setStatus("optional")


class _FunkSbrTrapVarIniString_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarIniString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarIniString_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarIniString_Object = MibScalar
funkSbrTrapVarIniString = _FunkSbrTrapVarIniString_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 14),
    _FunkSbrTrapVarIniString_Type()
)
funkSbrTrapVarIniString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarIniString.setStatus("optional")


class _FunkSbrTrapVarDbType_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarDbType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarDbType_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarDbType_Object = MibScalar
funkSbrTrapVarDbType = _FunkSbrTrapVarDbType_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 15),
    _FunkSbrTrapVarDbType_Type()
)
funkSbrTrapVarDbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarDbType.setStatus("optional")


class _FunkSbrTrapVarFailedSystemName_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarFailedSystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarFailedSystemName_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarFailedSystemName_Object = MibScalar
funkSbrTrapVarFailedSystemName = _FunkSbrTrapVarFailedSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 16),
    _FunkSbrTrapVarFailedSystemName_Type()
)
funkSbrTrapVarFailedSystemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarFailedSystemName.setStatus("optional")


class _FunkSbrTrapVarUserName_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarUserName_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarUserName_Object = MibScalar
funkSbrTrapVarUserName = _FunkSbrTrapVarUserName_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 17),
    _FunkSbrTrapVarUserName_Type()
)
funkSbrTrapVarUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarUserName.setStatus("optional")


class _FunkSbrTrapVarPersistStoreName_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarPersistStoreName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarPersistStoreName_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarPersistStoreName_Object = MibScalar
funkSbrTrapVarPersistStoreName = _FunkSbrTrapVarPersistStoreName_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 18),
    _FunkSbrTrapVarPersistStoreName_Type()
)
funkSbrTrapVarPersistStoreName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarPersistStoreName.setStatus("optional")


class _FunkSbrTrapVarDiagnosticMessage_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarDiagnosticMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarDiagnosticMessage_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarDiagnosticMessage_Object = MibScalar
funkSbrTrapVarDiagnosticMessage = _FunkSbrTrapVarDiagnosticMessage_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 19),
    _FunkSbrTrapVarDiagnosticMessage_Type()
)
funkSbrTrapVarDiagnosticMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarDiagnosticMessage.setStatus("optional")


class _FunkSbrTrapVarIPAddrPoolName_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarIPAddrPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarIPAddrPoolName_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarIPAddrPoolName_Object = MibScalar
funkSbrTrapVarIPAddrPoolName = _FunkSbrTrapVarIPAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 20),
    _FunkSbrTrapVarIPAddrPoolName_Type()
)
funkSbrTrapVarIPAddrPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarIPAddrPoolName.setStatus("optional")


class _FunkSbrTrapVarIPAddrAvail_Type(SnmpAdminString):
    """Custom type funkSbrTrapVarIPAddrAvail based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FunkSbrTrapVarIPAddrAvail_Type.__name__ = "SnmpAdminString"
_FunkSbrTrapVarIPAddrAvail_Object = MibScalar
funkSbrTrapVarIPAddrAvail = _FunkSbrTrapVarIPAddrAvail_Object(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 1, 21),
    _FunkSbrTrapVarIPAddrAvail_Type()
)
funkSbrTrapVarIPAddrAvail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funkSbrTrapVarIPAddrAvail.setStatus("optional")

# Managed Objects groups


# Notification objects

funkSbrTrapServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 100)
)
funkSbrTrapServiceStarted.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSWName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapServiceStarted.setStatus(
        ""
    )

funkSbrTrapServiceStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 101)
)
funkSbrTrapServiceStopped.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSWName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapServiceStopped.setStatus(
        ""
    )

funkSbrTrapThreadsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 102)
)
funkSbrTrapThreadsNormal.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarThreadsAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapThreadsNormal.setStatus(
        ""
    )

funkSbrTrapFSNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 103)
)
funkSbrTrapFSNormal.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarBytesAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFSNormal.setStatus(
        ""
    )

funkSbrTrapConcurrencyReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 104)
)
funkSbrTrapConcurrencyReconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapConcurrencyReconnect.setStatus(
        ""
    )

funkSbrTrapSQLReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 105)
)
funkSbrTrapSQLReconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLReconnect.setStatus(
        ""
    )

funkSbrTrapLDAPReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 106)
)
funkSbrTrapLDAPReconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPReconnect.setStatus(
        ""
    )

funkSbrTrapUserAccountLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 107)
)
funkSbrTrapUserAccountLocked.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarUserName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapUserAccountLocked.setStatus(
        ""
    )

funkSbrTrapUserAccountReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 108)
)
funkSbrTrapUserAccountReleased.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarUserName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapUserAccountReleased.setStatus(
        ""
    )

funkSbrTrapProxySpoolReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 109)
)
funkSbrTrapProxySpoolReconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapProxySpoolReconnect.setStatus(
        ""
    )

funkSbrTrapIPAddrPoolNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 110)
)
funkSbrTrapIPAddrPoolNormal.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIPAddrPoolName"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIPAddrAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapIPAddrPoolNormal.setStatus(
        ""
    )

funkSbrTrapCmdArgBadPrivDir = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5000)
)
funkSbrTrapCmdArgBadPrivDir.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarPrivateDir"))
)
if mibBuilder.loadTexts:
    funkSbrTrapCmdArgBadPrivDir.setStatus(
        ""
    )

funkSbrTrapLowThreads = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5001)
)
funkSbrTrapLowThreads.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarThreadsAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLowThreads.setStatus(
        ""
    )

funkSbrTrapConcurrencyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5002)
)
funkSbrTrapConcurrencyFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapConcurrencyFailure.setStatus(
        ""
    )

funkSbrTrapConcurrencyTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5003)
)
funkSbrTrapConcurrencyTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapConcurrencyTimeout.setStatus(
        ""
    )

funkSbrTrapConcurrencyLocalProxyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5004)
)
funkSbrTrapConcurrencyLocalProxyFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapConcurrencyLocalProxyFailure.setStatus(
        ""
    )

funkSbrTrapStaticAcctProxyTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5005)
)
funkSbrTrapStaticAcctProxyTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapStaticAcctProxyTimeout.setStatus(
        ""
    )

funkSbrTrapStaticAcctProxyLocalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5006)
)
funkSbrTrapStaticAcctProxyLocalFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapStaticAcctProxyLocalFailure.setStatus(
        ""
    )

funkSbrTrapLowFSSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5007)
)
funkSbrTrapLowFSSpace.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarBytesAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLowFSSpace.setStatus(
        ""
    )

funkSbrTrapSQLConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5008)
)
funkSbrTrapSQLConnectFail.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSQLConnects"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLConnectFail.setStatus(
        ""
    )

funkSbrTrapSQLDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5009)
)
funkSbrTrapSQLDisconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSQLDisconnects"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLDisconnect.setStatus(
        ""
    )

funkSbrTrapSQLTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5010)
)
funkSbrTrapSQLTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSQLTimeouts"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLTimeout.setStatus(
        ""
    )

funkSbrTrapAcctDbTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5011)
)
funkSbrTrapAcctDbTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapAcctDbTimeout.setStatus(
        ""
    )

funkSbrTrapAcctDbFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5012)
)
funkSbrTrapAcctDbFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapAcctDbFailure.setStatus(
        ""
    )

funkSbrTrapVerifyServerTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5013)
)
funkSbrTrapVerifyServerTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapVerifyServerTimeout.setStatus(
        ""
    )

funkSbrTrapVerifyServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5014)
)
funkSbrTrapVerifyServerFail.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapVerifyServerFail.setStatus(
        ""
    )

funkSbrTrapLDAPConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5015)
)
funkSbrTrapLDAPConnectFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPConnectFailure.setStatus(
        ""
    )

funkSbrTrapLDAPConnectFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5016)
)
funkSbrTrapLDAPConnectFailures.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPConnectFailures.setStatus(
        ""
    )

funkSbrTrapLDAPDisconnects = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5017)
)
funkSbrTrapLDAPDisconnects.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPDisconnects.setStatus(
        ""
    )

funkSbrTrapLDAPRequestTimeouts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5018)
)
funkSbrTrapLDAPRequestTimeouts.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPRequestTimeouts.setStatus(
        ""
    )

funkSbrTrapLDAPDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5019)
)
funkSbrTrapLDAPDisconnect.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPDisconnect.setStatus(
        ""
    )

funkSbrTrapLDAPRequestTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5020)
)
funkSbrTrapLDAPRequestTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapLDAPRequestTimeout.setStatus(
        ""
    )

funkSbrTrapProxySpoolTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5021)
)
funkSbrTrapProxySpoolTimeout.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapProxySpoolTimeout.setStatus(
        ""
    )

funkSbrTrapProxySpoolTimeouts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5022)
)
funkSbrTrapProxySpoolTimeouts.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapProxySpoolTimeouts.setStatus(
        ""
    )

funkSbrTrapSoftLimitViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5023)
)
funkSbrTrapSoftLimitViolation.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSoftLimitViolation.setStatus(
        ""
    )

funkSbrTrapHardLimitViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5024)
)
funkSbrTrapHardLimitViolation.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapHardLimitViolation.setStatus(
        ""
    )

funkSbrTrapConcurrencyServerMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5025)
)
funkSbrTrapConcurrencyServerMisconfiguration.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapConcurrencyServerMisconfiguration.setStatus(
        ""
    )

funkSbrTrapACCTWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5026)
)
funkSbrTrapACCTWriteFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarPersistStoreName"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarDiagnosticMessage"))
)
if mibBuilder.loadTexts:
    funkSbrTrapACCTWriteFailure.setStatus(
        ""
    )

funkSbrTrapIPAddrPoolLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 5027)
)
funkSbrTrapIPAddrPoolLow.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIPAddrPoolName"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIPAddrAvail"))
)
if mibBuilder.loadTexts:
    funkSbrTrapIPAddrPoolLow.setStatus(
        ""
    )

funkSbrTrapStartServiceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10000)
)
funkSbrTrapStartServiceError.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarServiceDispatcherErrCode"))
)
if mibBuilder.loadTexts:
    funkSbrTrapStartServiceError.setStatus(
        ""
    )

funkSbrTrapSetStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10001)
)
funkSbrTrapSetStatusError.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSetStatusErrCode"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSetStatusError.setStatus(
        ""
    )

funkSbrTrapBadPrivDir = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10002)
)
funkSbrTrapBadPrivDir.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarPrivateDir"))
)
if mibBuilder.loadTexts:
    funkSbrTrapBadPrivDir.setStatus(
        ""
    )

funkSbrTrapFailedThreadCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10003)
)
funkSbrTrapFailedThreadCreate.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedThreadCreate.setStatus(
        ""
    )

funkSbrTrapFailedMutexCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10004)
)
funkSbrTrapFailedMutexCreate.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedMutexCreate.setStatus(
        ""
    )

funkSbrTrapFailedSignalInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10005)
)
funkSbrTrapFailedSignalInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedSignalInit.setStatus(
        ""
    )

funkSbrTrapFailedEventInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10006)
)
funkSbrTrapFailedEventInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedEventInit.setStatus(
        ""
    )

funkSbrTrapFailedLogFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10007)
)
funkSbrTrapFailedLogFile.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedLogFile.setStatus(
        ""
    )

funkSbrTrapFailedLDAPAdminInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10008)
)
funkSbrTrapFailedLDAPAdminInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedLDAPAdminInit.setStatus(
        ""
    )

funkSbrTrapFailedRPCInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10009)
)
funkSbrTrapFailedRPCInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedRPCInit.setStatus(
        ""
    )

funkSbrTrapFailedIPInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10010)
)
funkSbrTrapFailedIPInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedIPInit.setStatus(
        ""
    )

funkSbrTrapFailedCurrentSessionsInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10011)
)
funkSbrTrapFailedCurrentSessionsInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedCurrentSessionsInit.setStatus(
        ""
    )

funkSbrTrapFailedChallCacheInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10012)
)
funkSbrTrapFailedChallCacheInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedChallCacheInit.setStatus(
        ""
    )

funkSbrTrapFailedActiveRASInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10013)
)
funkSbrTrapFailedActiveRASInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedActiveRASInit.setStatus(
        ""
    )

funkSbrTrapFailedDictionaryInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10014)
)
funkSbrTrapFailedDictionaryInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedDictionaryInit.setStatus(
        ""
    )

funkSbrTrapFailedVendorInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10015)
)
funkSbrTrapFailedVendorInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedVendorInit.setStatus(
        ""
    )

funkSbrTrapFailedDBInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10016)
)
funkSbrTrapFailedDBInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarDbType"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedDBInit.setStatus(
        ""
    )

funkSbrTrapFailedUnixUserInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10017)
)
funkSbrTrapFailedUnixUserInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedUnixUserInit.setStatus(
        ""
    )

funkSbrTrapFailedAdminRightsInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10018)
)
funkSbrTrapFailedAdminRightsInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedAdminRightsInit.setStatus(
        ""
    )

funkSbrTrapFailedDbOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10019)
)
funkSbrTrapFailedDbOpen.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarDbType"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedDbOpen.setStatus(
        ""
    )

funkSbrTrapFailedDNISLookupInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10020)
)
funkSbrTrapFailedDNISLookupInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedDNISLookupInit.setStatus(
        ""
    )

funkSbrTrapFailedConfigCacheInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10021)
)
funkSbrTrapFailedConfigCacheInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedConfigCacheInit.setStatus(
        ""
    )

funkSbrTrapFailedDbCacheInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10022)
)
funkSbrTrapFailedDbCacheInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedDbCacheInit.setStatus(
        ""
    )

funkSbrTrapFailedLicenseInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10023)
)
funkSbrTrapFailedLicenseInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedLicenseInit.setStatus(
        ""
    )

funkSbrTrapFailedNDSTrusteeInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10024)
)
funkSbrTrapFailedNDSTrusteeInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedNDSTrusteeInit.setStatus(
        ""
    )

funkSbrTrapFailedHostLookupInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10025)
)
funkSbrTrapFailedHostLookupInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedHostLookupInit.setStatus(
        ""
    )

funkSbrTrapFailedAddrPoolInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10026)
)
funkSbrTrapFailedAddrPoolInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedAddrPoolInit.setStatus(
        ""
    )

funkSbrTrapFailedLoginLimitInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10027)
)
funkSbrTrapFailedLoginLimitInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedLoginLimitInit.setStatus(
        ""
    )

funkSbrTrapFailedPersistStoreCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10028)
)
funkSbrTrapFailedPersistStoreCreate.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedPersistStoreCreate.setStatus(
        ""
    )

funkSbrTrapFailedPersistStoreInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10029)
)
funkSbrTrapFailedPersistStoreInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedPersistStoreInit.setStatus(
        ""
    )

funkSbrTrapFailedPerfMonInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10030)
)
funkSbrTrapFailedPerfMonInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedPerfMonInit.setStatus(
        ""
    )

funkSbrTrapFailedLockInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10031)
)
funkSbrTrapFailedLockInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedLockInit.setStatus(
        ""
    )

funkSbrTrapFailedPlugInInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10032)
)
funkSbrTrapFailedPlugInInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedPlugInInit.setStatus(
        ""
    )

funkSbrTrapFailedPacketCacheInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10033)
)
funkSbrTrapFailedPacketCacheInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedPacketCacheInit.setStatus(
        ""
    )

funkSbrTrapFailedNameMangleInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10034)
)
funkSbrTrapFailedNameMangleInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedNameMangleInit.setStatus(
        ""
    )

funkSbrTrapFailedNameStripInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10035)
)
funkSbrTrapFailedNameStripInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedNameStripInit.setStatus(
        ""
    )

funkSbrTrapFailedFSSpaceChecking = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10036)
)
funkSbrTrapFailedFSSpaceChecking.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarGetDiskFreeSpaceErrCode"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedFSSpaceChecking.setStatus(
        ""
    )

funkSbrTrapFailedNameValidateInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10037)
)
funkSbrTrapFailedNameValidateInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedNameValidateInit.setStatus(
        ""
    )

funkSbrTrapFailedResourceCheckInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10038)
)
funkSbrTrapFailedResourceCheckInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedResourceCheckInit.setStatus(
        ""
    )

funkSbrTrapFailedSystemStatsInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10039)
)
funkSbrTrapFailedSystemStatsInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedSystemStatsInit.setStatus(
        ""
    )

funkSbrTrapSQLConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10040)
)
funkSbrTrapSQLConnectFailure.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLConnectFailure.setStatus(
        ""
    )

funkSbrTrapSQLDiscon = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10041)
)
funkSbrTrapSQLDiscon.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarFailedSystemName"))
)
if mibBuilder.loadTexts:
    funkSbrTrapSQLDiscon.setStatus(
        ""
    )

funkSbrTrapFailedReserveMemoryAlloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10043)
)
funkSbrTrapFailedReserveMemoryAlloc.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIniString"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedReserveMemoryAlloc.setStatus(
        ""
    )

funkSbrTrapReserveMemoryFreed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10044)
)
funkSbrTrapReserveMemoryFreed.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarIniString"))
)
if mibBuilder.loadTexts:
    funkSbrTrapReserveMemoryFreed.setStatus(
        ""
    )

funkSbrTrapMemoryAllocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10045)
)
funkSbrTrapMemoryAllocFail.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarNumberOfOccurrences"))
)
if mibBuilder.loadTexts:
    funkSbrTrapMemoryAllocFail.setStatus(
        ""
    )

funkSbrTrapFailedMibInfoCollectInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10048)
)
funkSbrTrapFailedMibInfoCollectInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedMibInfoCollectInit.setStatus(
        ""
    )

funkSbrTrapFailedMibInfoAccessInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10049)
)
funkSbrTrapFailedMibInfoAccessInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedMibInfoAccessInit.setStatus(
        ""
    )

funkSbrTrapFailedCommonIPInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1411, 1, 1, 0, 10050)
)
funkSbrTrapFailedCommonIPInit.setObjects(
      *(("FNKSBRTR-MIB", "funkSbrTrapVarComp"),
        ("FNKSBRTR-MIB", "funkSbrTrapVarSev"))
)
if mibBuilder.loadTexts:
    funkSbrTrapFailedCommonIPInit.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNKSBRTR-MIB",
    **{"funk": funk,
       "funkSbr": funkSbr,
       "funkSbrTraps": funkSbrTraps,
       "funkSbrTrapServiceStarted": funkSbrTrapServiceStarted,
       "funkSbrTrapServiceStopped": funkSbrTrapServiceStopped,
       "funkSbrTrapThreadsNormal": funkSbrTrapThreadsNormal,
       "funkSbrTrapFSNormal": funkSbrTrapFSNormal,
       "funkSbrTrapConcurrencyReconnect": funkSbrTrapConcurrencyReconnect,
       "funkSbrTrapSQLReconnect": funkSbrTrapSQLReconnect,
       "funkSbrTrapLDAPReconnect": funkSbrTrapLDAPReconnect,
       "funkSbrTrapUserAccountLocked": funkSbrTrapUserAccountLocked,
       "funkSbrTrapUserAccountReleased": funkSbrTrapUserAccountReleased,
       "funkSbrTrapProxySpoolReconnect": funkSbrTrapProxySpoolReconnect,
       "funkSbrTrapIPAddrPoolNormal": funkSbrTrapIPAddrPoolNormal,
       "funkSbrTrapCmdArgBadPrivDir": funkSbrTrapCmdArgBadPrivDir,
       "funkSbrTrapLowThreads": funkSbrTrapLowThreads,
       "funkSbrTrapConcurrencyFailure": funkSbrTrapConcurrencyFailure,
       "funkSbrTrapConcurrencyTimeout": funkSbrTrapConcurrencyTimeout,
       "funkSbrTrapConcurrencyLocalProxyFailure": funkSbrTrapConcurrencyLocalProxyFailure,
       "funkSbrTrapStaticAcctProxyTimeout": funkSbrTrapStaticAcctProxyTimeout,
       "funkSbrTrapStaticAcctProxyLocalFailure": funkSbrTrapStaticAcctProxyLocalFailure,
       "funkSbrTrapLowFSSpace": funkSbrTrapLowFSSpace,
       "funkSbrTrapSQLConnectFail": funkSbrTrapSQLConnectFail,
       "funkSbrTrapSQLDisconnect": funkSbrTrapSQLDisconnect,
       "funkSbrTrapSQLTimeout": funkSbrTrapSQLTimeout,
       "funkSbrTrapAcctDbTimeout": funkSbrTrapAcctDbTimeout,
       "funkSbrTrapAcctDbFailure": funkSbrTrapAcctDbFailure,
       "funkSbrTrapVerifyServerTimeout": funkSbrTrapVerifyServerTimeout,
       "funkSbrTrapVerifyServerFail": funkSbrTrapVerifyServerFail,
       "funkSbrTrapLDAPConnectFailure": funkSbrTrapLDAPConnectFailure,
       "funkSbrTrapLDAPConnectFailures": funkSbrTrapLDAPConnectFailures,
       "funkSbrTrapLDAPDisconnects": funkSbrTrapLDAPDisconnects,
       "funkSbrTrapLDAPRequestTimeouts": funkSbrTrapLDAPRequestTimeouts,
       "funkSbrTrapLDAPDisconnect": funkSbrTrapLDAPDisconnect,
       "funkSbrTrapLDAPRequestTimeout": funkSbrTrapLDAPRequestTimeout,
       "funkSbrTrapProxySpoolTimeout": funkSbrTrapProxySpoolTimeout,
       "funkSbrTrapProxySpoolTimeouts": funkSbrTrapProxySpoolTimeouts,
       "funkSbrTrapSoftLimitViolation": funkSbrTrapSoftLimitViolation,
       "funkSbrTrapHardLimitViolation": funkSbrTrapHardLimitViolation,
       "funkSbrTrapConcurrencyServerMisconfiguration": funkSbrTrapConcurrencyServerMisconfiguration,
       "funkSbrTrapACCTWriteFailure": funkSbrTrapACCTWriteFailure,
       "funkSbrTrapIPAddrPoolLow": funkSbrTrapIPAddrPoolLow,
       "funkSbrTrapStartServiceError": funkSbrTrapStartServiceError,
       "funkSbrTrapSetStatusError": funkSbrTrapSetStatusError,
       "funkSbrTrapBadPrivDir": funkSbrTrapBadPrivDir,
       "funkSbrTrapFailedThreadCreate": funkSbrTrapFailedThreadCreate,
       "funkSbrTrapFailedMutexCreate": funkSbrTrapFailedMutexCreate,
       "funkSbrTrapFailedSignalInit": funkSbrTrapFailedSignalInit,
       "funkSbrTrapFailedEventInit": funkSbrTrapFailedEventInit,
       "funkSbrTrapFailedLogFile": funkSbrTrapFailedLogFile,
       "funkSbrTrapFailedLDAPAdminInit": funkSbrTrapFailedLDAPAdminInit,
       "funkSbrTrapFailedRPCInit": funkSbrTrapFailedRPCInit,
       "funkSbrTrapFailedIPInit": funkSbrTrapFailedIPInit,
       "funkSbrTrapFailedCurrentSessionsInit": funkSbrTrapFailedCurrentSessionsInit,
       "funkSbrTrapFailedChallCacheInit": funkSbrTrapFailedChallCacheInit,
       "funkSbrTrapFailedActiveRASInit": funkSbrTrapFailedActiveRASInit,
       "funkSbrTrapFailedDictionaryInit": funkSbrTrapFailedDictionaryInit,
       "funkSbrTrapFailedVendorInit": funkSbrTrapFailedVendorInit,
       "funkSbrTrapFailedDBInit": funkSbrTrapFailedDBInit,
       "funkSbrTrapFailedUnixUserInit": funkSbrTrapFailedUnixUserInit,
       "funkSbrTrapFailedAdminRightsInit": funkSbrTrapFailedAdminRightsInit,
       "funkSbrTrapFailedDbOpen": funkSbrTrapFailedDbOpen,
       "funkSbrTrapFailedDNISLookupInit": funkSbrTrapFailedDNISLookupInit,
       "funkSbrTrapFailedConfigCacheInit": funkSbrTrapFailedConfigCacheInit,
       "funkSbrTrapFailedDbCacheInit": funkSbrTrapFailedDbCacheInit,
       "funkSbrTrapFailedLicenseInit": funkSbrTrapFailedLicenseInit,
       "funkSbrTrapFailedNDSTrusteeInit": funkSbrTrapFailedNDSTrusteeInit,
       "funkSbrTrapFailedHostLookupInit": funkSbrTrapFailedHostLookupInit,
       "funkSbrTrapFailedAddrPoolInit": funkSbrTrapFailedAddrPoolInit,
       "funkSbrTrapFailedLoginLimitInit": funkSbrTrapFailedLoginLimitInit,
       "funkSbrTrapFailedPersistStoreCreate": funkSbrTrapFailedPersistStoreCreate,
       "funkSbrTrapFailedPersistStoreInit": funkSbrTrapFailedPersistStoreInit,
       "funkSbrTrapFailedPerfMonInit": funkSbrTrapFailedPerfMonInit,
       "funkSbrTrapFailedLockInit": funkSbrTrapFailedLockInit,
       "funkSbrTrapFailedPlugInInit": funkSbrTrapFailedPlugInInit,
       "funkSbrTrapFailedPacketCacheInit": funkSbrTrapFailedPacketCacheInit,
       "funkSbrTrapFailedNameMangleInit": funkSbrTrapFailedNameMangleInit,
       "funkSbrTrapFailedNameStripInit": funkSbrTrapFailedNameStripInit,
       "funkSbrTrapFailedFSSpaceChecking": funkSbrTrapFailedFSSpaceChecking,
       "funkSbrTrapFailedNameValidateInit": funkSbrTrapFailedNameValidateInit,
       "funkSbrTrapFailedResourceCheckInit": funkSbrTrapFailedResourceCheckInit,
       "funkSbrTrapFailedSystemStatsInit": funkSbrTrapFailedSystemStatsInit,
       "funkSbrTrapSQLConnectFailure": funkSbrTrapSQLConnectFailure,
       "funkSbrTrapSQLDiscon": funkSbrTrapSQLDiscon,
       "funkSbrTrapFailedReserveMemoryAlloc": funkSbrTrapFailedReserveMemoryAlloc,
       "funkSbrTrapReserveMemoryFreed": funkSbrTrapReserveMemoryFreed,
       "funkSbrTrapMemoryAllocFail": funkSbrTrapMemoryAllocFail,
       "funkSbrTrapFailedMibInfoCollectInit": funkSbrTrapFailedMibInfoCollectInit,
       "funkSbrTrapFailedMibInfoAccessInit": funkSbrTrapFailedMibInfoAccessInit,
       "funkSbrTrapFailedCommonIPInit": funkSbrTrapFailedCommonIPInit,
       "funkSbrTrapVars": funkSbrTrapVars,
       "funkSbrTrapVarComp": funkSbrTrapVarComp,
       "funkSbrTrapVarSev": funkSbrTrapVarSev,
       "funkSbrTrapVarSWName": funkSbrTrapVarSWName,
       "funkSbrTrapVarThreadsAvail": funkSbrTrapVarThreadsAvail,
       "funkSbrTrapVarBytesAvail": funkSbrTrapVarBytesAvail,
       "funkSbrTrapVarPrivateDir": funkSbrTrapVarPrivateDir,
       "funkSbrTrapVarNumberOfOccurrences": funkSbrTrapVarNumberOfOccurrences,
       "funkSbrTrapVarSQLConnects": funkSbrTrapVarSQLConnects,
       "funkSbrTrapVarSQLDisconnects": funkSbrTrapVarSQLDisconnects,
       "funkSbrTrapVarSQLTimeouts": funkSbrTrapVarSQLTimeouts,
       "funkSbrTrapVarServiceDispatcherErrCode": funkSbrTrapVarServiceDispatcherErrCode,
       "funkSbrTrapVarSetStatusErrCode": funkSbrTrapVarSetStatusErrCode,
       "funkSbrTrapVarGetDiskFreeSpaceErrCode": funkSbrTrapVarGetDiskFreeSpaceErrCode,
       "funkSbrTrapVarIniString": funkSbrTrapVarIniString,
       "funkSbrTrapVarDbType": funkSbrTrapVarDbType,
       "funkSbrTrapVarFailedSystemName": funkSbrTrapVarFailedSystemName,
       "funkSbrTrapVarUserName": funkSbrTrapVarUserName,
       "funkSbrTrapVarPersistStoreName": funkSbrTrapVarPersistStoreName,
       "funkSbrTrapVarDiagnosticMessage": funkSbrTrapVarDiagnosticMessage,
       "funkSbrTrapVarIPAddrPoolName": funkSbrTrapVarIPAddrPoolName,
       "funkSbrTrapVarIPAddrAvail": funkSbrTrapVarIPAddrAvail}
)
