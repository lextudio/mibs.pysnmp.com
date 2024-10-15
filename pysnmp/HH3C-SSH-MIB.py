# SNMP MIB module (HH3C-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:57 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSSH = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22)
)
hh3cSSH.setRevisions(
        ("2014-02-20 00:00",
         "2014-01-17 00:00",
         "2013-12-21 00:00",
         "2007-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSSHServerMIB_ObjectIdentity = ObjectIdentity
hh3cSSHServerMIB = _Hh3cSSHServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1)
)
_Hh3cSSHServerMIBObjects_ObjectIdentity = ObjectIdentity
hh3cSSHServerMIBObjects = _Hh3cSSHServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1)
)
_Hh3cSSHServerGlobalConfig_ObjectIdentity = ObjectIdentity
hh3cSSHServerGlobalConfig = _Hh3cSSHServerGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1)
)
_Hh3cSSHServerVersion_Type = DisplayString
_Hh3cSSHServerVersion_Object = MibScalar
hh3cSSHServerVersion = _Hh3cSSHServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 1),
    _Hh3cSSHServerVersion_Type()
)
hh3cSSHServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHServerVersion.setStatus("current")


class _Hh3cSSHServerCompatibleSSH1x_Type(Integer32):
    """Custom type hh3cSSHServerCompatibleSSH1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableCompatibleSSH1x", 2),
          ("enableCompatibleSSH1x", 1))
    )


_Hh3cSSHServerCompatibleSSH1x_Type.__name__ = "Integer32"
_Hh3cSSHServerCompatibleSSH1x_Object = MibScalar
hh3cSSHServerCompatibleSSH1x = _Hh3cSSHServerCompatibleSSH1x_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 2),
    _Hh3cSSHServerCompatibleSSH1x_Type()
)
hh3cSSHServerCompatibleSSH1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSSHServerCompatibleSSH1x.setStatus("current")
_Hh3cSSHServerRekeyInterval_Type = Integer32
_Hh3cSSHServerRekeyInterval_Object = MibScalar
hh3cSSHServerRekeyInterval = _Hh3cSSHServerRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 3),
    _Hh3cSSHServerRekeyInterval_Type()
)
hh3cSSHServerRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSSHServerRekeyInterval.setStatus("current")
_Hh3cSSHServerAuthRetries_Type = Integer32
_Hh3cSSHServerAuthRetries_Object = MibScalar
hh3cSSHServerAuthRetries = _Hh3cSSHServerAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 4),
    _Hh3cSSHServerAuthRetries_Type()
)
hh3cSSHServerAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSSHServerAuthRetries.setStatus("current")
_Hh3cSSHServerAuthTimeout_Type = Integer32
_Hh3cSSHServerAuthTimeout_Object = MibScalar
hh3cSSHServerAuthTimeout = _Hh3cSSHServerAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 5),
    _Hh3cSSHServerAuthTimeout_Type()
)
hh3cSSHServerAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSSHServerAuthTimeout.setStatus("current")
_Hh3cSFTPServerIdleTimeout_Type = Integer32
_Hh3cSFTPServerIdleTimeout_Object = MibScalar
hh3cSFTPServerIdleTimeout = _Hh3cSFTPServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 6),
    _Hh3cSFTPServerIdleTimeout_Type()
)
hh3cSFTPServerIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSFTPServerIdleTimeout.setStatus("current")


class _Hh3cSSHServerEnable_Type(Integer32):
    """Custom type hh3cSSHServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSSHServer", 2),
          ("enableSSHServer", 1))
    )


_Hh3cSSHServerEnable_Type.__name__ = "Integer32"
_Hh3cSSHServerEnable_Object = MibScalar
hh3cSSHServerEnable = _Hh3cSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 7),
    _Hh3cSSHServerEnable_Type()
)
hh3cSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSSHServerEnable.setStatus("current")


class _Hh3cSFTPServerEnable_Type(Integer32):
    """Custom type hh3cSFTPServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSFTPService", 2),
          ("enableSFTPService", 1))
    )


_Hh3cSFTPServerEnable_Type.__name__ = "Integer32"
_Hh3cSFTPServerEnable_Object = MibScalar
hh3cSFTPServerEnable = _Hh3cSFTPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 8),
    _Hh3cSFTPServerEnable_Type()
)
hh3cSFTPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSFTPServerEnable.setStatus("current")


class _Hh3cSTelnetServerEnable_Type(Integer32):
    """Custom type hh3cSTelnetServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSTelnetServer", 2),
          ("enableSTelnetServer", 1))
    )


_Hh3cSTelnetServerEnable_Type.__name__ = "Integer32"
_Hh3cSTelnetServerEnable_Object = MibScalar
hh3cSTelnetServerEnable = _Hh3cSTelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 9),
    _Hh3cSTelnetServerEnable_Type()
)
hh3cSTelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSTelnetServerEnable.setStatus("current")


class _Hh3cSCPServerEnable_Type(Integer32):
    """Custom type hh3cSCPServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSCPService", 2),
          ("enableSCPService", 1))
    )


_Hh3cSCPServerEnable_Type.__name__ = "Integer32"
_Hh3cSCPServerEnable_Object = MibScalar
hh3cSCPServerEnable = _Hh3cSCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 10),
    _Hh3cSCPServerEnable_Type()
)
hh3cSCPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSCPServerEnable.setStatus("current")
_Hh3cSSHUserConfig_ObjectIdentity = ObjectIdentity
hh3cSSHUserConfig = _Hh3cSSHUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2)
)
_Hh3cSSHUserConfigTable_Object = MibTable
hh3cSSHUserConfigTable = _Hh3cSSHUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSSHUserConfigTable.setStatus("current")
_Hh3cSSHUserConfigEntry_Object = MibTableRow
hh3cSSHUserConfigEntry = _Hh3cSSHUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1)
)
hh3cSSHUserConfigEntry.setIndexNames(
    (0, "HH3C-SSH-MIB", "hh3cSSHUserName"),
)
if mibBuilder.loadTexts:
    hh3cSSHUserConfigEntry.setStatus("current")
_Hh3cSSHUserName_Type = DisplayString
_Hh3cSSHUserName_Object = MibTableColumn
hh3cSSHUserName = _Hh3cSSHUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 1),
    _Hh3cSSHUserName_Type()
)
hh3cSSHUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSSHUserName.setStatus("current")


class _Hh3cSSHUserServiceType_Type(Integer32):
    """Custom type hh3cSSHUserServiceType based on Integer32"""
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
        *(("all", 2),
          ("invalid", 1),
          ("scp", 5),
          ("sftp", 4),
          ("stelnet", 3))
    )


_Hh3cSSHUserServiceType_Type.__name__ = "Integer32"
_Hh3cSSHUserServiceType_Object = MibTableColumn
hh3cSSHUserServiceType = _Hh3cSSHUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 2),
    _Hh3cSSHUserServiceType_Type()
)
hh3cSSHUserServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSSHUserServiceType.setStatus("current")


class _Hh3cSSHUserAuthType_Type(Integer32):
    """Custom type hh3cSSHUserAuthType based on Integer32"""
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
        *(("any", 4),
          ("invalid", 1),
          ("password", 2),
          ("publicKey", 3),
          ("publicKeyPassword", 5))
    )


_Hh3cSSHUserAuthType_Type.__name__ = "Integer32"
_Hh3cSSHUserAuthType_Object = MibTableColumn
hh3cSSHUserAuthType = _Hh3cSSHUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 3),
    _Hh3cSSHUserAuthType_Type()
)
hh3cSSHUserAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSSHUserAuthType.setStatus("current")
_Hh3cSSHUserPublicKeyName_Type = DisplayString
_Hh3cSSHUserPublicKeyName_Object = MibTableColumn
hh3cSSHUserPublicKeyName = _Hh3cSSHUserPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 4),
    _Hh3cSSHUserPublicKeyName_Type()
)
hh3cSSHUserPublicKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSSHUserPublicKeyName.setStatus("current")
_Hh3cSSHUserWorkDirectory_Type = DisplayString
_Hh3cSSHUserWorkDirectory_Object = MibTableColumn
hh3cSSHUserWorkDirectory = _Hh3cSSHUserWorkDirectory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 5),
    _Hh3cSSHUserWorkDirectory_Type()
)
hh3cSSHUserWorkDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSSHUserWorkDirectory.setStatus("current")
_Hh3cSSHUserRowStatus_Type = RowStatus
_Hh3cSSHUserRowStatus_Object = MibTableColumn
hh3cSSHUserRowStatus = _Hh3cSSHUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 6),
    _Hh3cSSHUserRowStatus_Type()
)
hh3cSSHUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSSHUserRowStatus.setStatus("current")
_Hh3cSSHSessionInfoTable_Object = MibTable
hh3cSSHSessionInfoTable = _Hh3cSSHSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSSHSessionInfoTable.setStatus("current")
_Hh3cSSHSessionInfoEntry_Object = MibTableRow
hh3cSSHSessionInfoEntry = _Hh3cSSHSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1)
)
hh3cSSHSessionInfoEntry.setIndexNames(
    (0, "HH3C-SSH-MIB", "hh3cSSHSessionID"),
)
if mibBuilder.loadTexts:
    hh3cSSHSessionInfoEntry.setStatus("current")
_Hh3cSSHSessionID_Type = Integer32
_Hh3cSSHSessionID_Object = MibTableColumn
hh3cSSHSessionID = _Hh3cSSHSessionID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 1),
    _Hh3cSSHSessionID_Type()
)
hh3cSSHSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSSHSessionID.setStatus("current")
_Hh3cSSHSessionUserName_Type = DisplayString
_Hh3cSSHSessionUserName_Object = MibTableColumn
hh3cSSHSessionUserName = _Hh3cSSHSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 2),
    _Hh3cSSHSessionUserName_Type()
)
hh3cSSHSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionUserName.setStatus("current")
_Hh3cSSHSessionUserIpAddrType_Type = InetAddressType
_Hh3cSSHSessionUserIpAddrType_Object = MibTableColumn
hh3cSSHSessionUserIpAddrType = _Hh3cSSHSessionUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 3),
    _Hh3cSSHSessionUserIpAddrType_Type()
)
hh3cSSHSessionUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionUserIpAddrType.setStatus("current")
_Hh3cSSHSessionUserIpAddr_Type = InetAddress
_Hh3cSSHSessionUserIpAddr_Object = MibTableColumn
hh3cSSHSessionUserIpAddr = _Hh3cSSHSessionUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 4),
    _Hh3cSSHSessionUserIpAddr_Type()
)
hh3cSSHSessionUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionUserIpAddr.setStatus("current")
_Hh3cSSHSessionClientVersion_Type = DisplayString
_Hh3cSSHSessionClientVersion_Object = MibTableColumn
hh3cSSHSessionClientVersion = _Hh3cSSHSessionClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 5),
    _Hh3cSSHSessionClientVersion_Type()
)
hh3cSSHSessionClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionClientVersion.setStatus("current")


class _Hh3cSSHSessionServiceType_Type(Integer32):
    """Custom type hh3cSSHSessionServiceType based on Integer32"""
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
        *(("invalid", 1),
          ("scp", 4),
          ("sftp", 3),
          ("stelnet", 2))
    )


_Hh3cSSHSessionServiceType_Type.__name__ = "Integer32"
_Hh3cSSHSessionServiceType_Object = MibTableColumn
hh3cSSHSessionServiceType = _Hh3cSSHSessionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 6),
    _Hh3cSSHSessionServiceType_Type()
)
hh3cSSHSessionServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionServiceType.setStatus("current")


class _Hh3cSSHSessionEncry_Type(Integer32):
    """Custom type hh3cSSHSessionEncry based on Integer32"""
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
        *(("aes128CBC", 2),
          ("des3CBC", 4),
          ("desCBC", 3),
          ("invalid", 1))
    )


_Hh3cSSHSessionEncry_Type.__name__ = "Integer32"
_Hh3cSSHSessionEncry_Object = MibTableColumn
hh3cSSHSessionEncry = _Hh3cSSHSessionEncry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 7),
    _Hh3cSSHSessionEncry_Type()
)
hh3cSSHSessionEncry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionEncry.setStatus("current")


class _Hh3cSSHSessionState_Type(Integer32):
    """Custom type hh3cSSHSessionState based on Integer32"""
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
        *(("authRequest", 4),
          ("disconnect", 7),
          ("established", 6),
          ("init", 1),
          ("keysExchange", 3),
          ("serviceRequest", 5),
          ("verExchange", 2))
    )


_Hh3cSSHSessionState_Type.__name__ = "Integer32"
_Hh3cSSHSessionState_Object = MibTableColumn
hh3cSSHSessionState = _Hh3cSSHSessionState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 8),
    _Hh3cSSHSessionState_Type()
)
hh3cSSHSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSSHSessionState.setStatus("current")
_Hh3cSSHServerObjForTrap_ObjectIdentity = ObjectIdentity
hh3cSSHServerObjForTrap = _Hh3cSSHServerObjForTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2)
)
_Hh3cSSHAttemptUserName_Type = DisplayString
_Hh3cSSHAttemptUserName_Object = MibScalar
hh3cSSHAttemptUserName = _Hh3cSSHAttemptUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 1),
    _Hh3cSSHAttemptUserName_Type()
)
hh3cSSHAttemptUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSSHAttemptUserName.setStatus("current")
_Hh3cSSHAttemptIpAddrType_Type = InetAddressType
_Hh3cSSHAttemptIpAddrType_Object = MibScalar
hh3cSSHAttemptIpAddrType = _Hh3cSSHAttemptIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 2),
    _Hh3cSSHAttemptIpAddrType_Type()
)
hh3cSSHAttemptIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSSHAttemptIpAddrType.setStatus("current")
_Hh3cSSHAttemptIpAddr_Type = InetAddress
_Hh3cSSHAttemptIpAddr_Object = MibScalar
hh3cSSHAttemptIpAddr = _Hh3cSSHAttemptIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 3),
    _Hh3cSSHAttemptIpAddr_Type()
)
hh3cSSHAttemptIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSSHAttemptIpAddr.setStatus("current")


class _Hh3cSSHUserAuthFailureReason_Type(Integer32):
    """Custom type hh3cSSHUserAuthFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authTimeout", 2),
          ("exceedRetries", 1),
          ("otherReason", 3))
    )


_Hh3cSSHUserAuthFailureReason_Type.__name__ = "Integer32"
_Hh3cSSHUserAuthFailureReason_Object = MibScalar
hh3cSSHUserAuthFailureReason = _Hh3cSSHUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 4),
    _Hh3cSSHUserAuthFailureReason_Type()
)
hh3cSSHUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSSHUserAuthFailureReason.setStatus("current")
_Hh3cSSHServerNotifications_ObjectIdentity = ObjectIdentity
hh3cSSHServerNotifications = _Hh3cSSHServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3)
)
_Hh3cSSHServerNotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cSSHServerNotificationsPrefix = _Hh3cSSHServerNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cSSHUserAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 1)
)
hh3cSSHUserAuthFailure.setObjects(
      *(("HH3C-SSH-MIB", "hh3cSSHAttemptUserName"),
        ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddrType"),
        ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddr"),
        ("HH3C-SSH-MIB", "hh3cSSHUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    hh3cSSHUserAuthFailure.setStatus(
        "current"
    )

hh3cSSHVersionNegotiationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 2)
)
hh3cSSHVersionNegotiationFailure.setObjects(
      *(("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddrType"),
        ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddr"))
)
if mibBuilder.loadTexts:
    hh3cSSHVersionNegotiationFailure.setStatus(
        "current"
    )

hh3cSSHUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 3)
)
hh3cSSHUserLogin.setObjects(
      *(("HH3C-SSH-MIB", "hh3cSSHSessionUserName"),
        ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddrType"),
        ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    hh3cSSHUserLogin.setStatus(
        "current"
    )

hh3cSSHUserLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 4)
)
hh3cSSHUserLogoff.setObjects(
      *(("HH3C-SSH-MIB", "hh3cSSHSessionUserName"),
        ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddrType"),
        ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    hh3cSSHUserLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SSH-MIB",
    **{"hh3cSSH": hh3cSSH,
       "hh3cSSHServerMIB": hh3cSSHServerMIB,
       "hh3cSSHServerMIBObjects": hh3cSSHServerMIBObjects,
       "hh3cSSHServerGlobalConfig": hh3cSSHServerGlobalConfig,
       "hh3cSSHServerVersion": hh3cSSHServerVersion,
       "hh3cSSHServerCompatibleSSH1x": hh3cSSHServerCompatibleSSH1x,
       "hh3cSSHServerRekeyInterval": hh3cSSHServerRekeyInterval,
       "hh3cSSHServerAuthRetries": hh3cSSHServerAuthRetries,
       "hh3cSSHServerAuthTimeout": hh3cSSHServerAuthTimeout,
       "hh3cSFTPServerIdleTimeout": hh3cSFTPServerIdleTimeout,
       "hh3cSSHServerEnable": hh3cSSHServerEnable,
       "hh3cSFTPServerEnable": hh3cSFTPServerEnable,
       "hh3cSTelnetServerEnable": hh3cSTelnetServerEnable,
       "hh3cSCPServerEnable": hh3cSCPServerEnable,
       "hh3cSSHUserConfig": hh3cSSHUserConfig,
       "hh3cSSHUserConfigTable": hh3cSSHUserConfigTable,
       "hh3cSSHUserConfigEntry": hh3cSSHUserConfigEntry,
       "hh3cSSHUserName": hh3cSSHUserName,
       "hh3cSSHUserServiceType": hh3cSSHUserServiceType,
       "hh3cSSHUserAuthType": hh3cSSHUserAuthType,
       "hh3cSSHUserPublicKeyName": hh3cSSHUserPublicKeyName,
       "hh3cSSHUserWorkDirectory": hh3cSSHUserWorkDirectory,
       "hh3cSSHUserRowStatus": hh3cSSHUserRowStatus,
       "hh3cSSHSessionInfoTable": hh3cSSHSessionInfoTable,
       "hh3cSSHSessionInfoEntry": hh3cSSHSessionInfoEntry,
       "hh3cSSHSessionID": hh3cSSHSessionID,
       "hh3cSSHSessionUserName": hh3cSSHSessionUserName,
       "hh3cSSHSessionUserIpAddrType": hh3cSSHSessionUserIpAddrType,
       "hh3cSSHSessionUserIpAddr": hh3cSSHSessionUserIpAddr,
       "hh3cSSHSessionClientVersion": hh3cSSHSessionClientVersion,
       "hh3cSSHSessionServiceType": hh3cSSHSessionServiceType,
       "hh3cSSHSessionEncry": hh3cSSHSessionEncry,
       "hh3cSSHSessionState": hh3cSSHSessionState,
       "hh3cSSHServerObjForTrap": hh3cSSHServerObjForTrap,
       "hh3cSSHAttemptUserName": hh3cSSHAttemptUserName,
       "hh3cSSHAttemptIpAddrType": hh3cSSHAttemptIpAddrType,
       "hh3cSSHAttemptIpAddr": hh3cSSHAttemptIpAddr,
       "hh3cSSHUserAuthFailureReason": hh3cSSHUserAuthFailureReason,
       "hh3cSSHServerNotifications": hh3cSSHServerNotifications,
       "hh3cSSHServerNotificationsPrefix": hh3cSSHServerNotificationsPrefix,
       "hh3cSSHUserAuthFailure": hh3cSSHUserAuthFailure,
       "hh3cSSHVersionNegotiationFailure": hh3cSSHVersionNegotiationFailure,
       "hh3cSSHUserLogin": hh3cSSHUserLogin,
       "hh3cSSHUserLogoff": hh3cSSHUserLogoff}
)
