# SNMP MIB module (HPN-ICF-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:53 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfSSH = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22)
)
hpnicfSSH.setRevisions(
        ("2014-02-20 00:00",
         "2014-01-17 00:00",
         "2013-12-21 00:00",
         "2007-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSSHServerMIB_ObjectIdentity = ObjectIdentity
hpnicfSSHServerMIB = _HpnicfSSHServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1)
)
_HpnicfSSHServerMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfSSHServerMIBObjects = _HpnicfSSHServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1)
)
_HpnicfSSHServerGlobalConfig_ObjectIdentity = ObjectIdentity
hpnicfSSHServerGlobalConfig = _HpnicfSSHServerGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1)
)
_HpnicfSSHServerVersion_Type = DisplayString
_HpnicfSSHServerVersion_Object = MibScalar
hpnicfSSHServerVersion = _HpnicfSSHServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 1),
    _HpnicfSSHServerVersion_Type()
)
hpnicfSSHServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHServerVersion.setStatus("current")


class _HpnicfSSHServerCompatibleSSH1x_Type(Integer32):
    """Custom type hpnicfSSHServerCompatibleSSH1x based on Integer32"""
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


_HpnicfSSHServerCompatibleSSH1x_Type.__name__ = "Integer32"
_HpnicfSSHServerCompatibleSSH1x_Object = MibScalar
hpnicfSSHServerCompatibleSSH1x = _HpnicfSSHServerCompatibleSSH1x_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 2),
    _HpnicfSSHServerCompatibleSSH1x_Type()
)
hpnicfSSHServerCompatibleSSH1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSSHServerCompatibleSSH1x.setStatus("current")
_HpnicfSSHServerRekeyInterval_Type = Integer32
_HpnicfSSHServerRekeyInterval_Object = MibScalar
hpnicfSSHServerRekeyInterval = _HpnicfSSHServerRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 3),
    _HpnicfSSHServerRekeyInterval_Type()
)
hpnicfSSHServerRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSSHServerRekeyInterval.setStatus("current")
_HpnicfSSHServerAuthRetries_Type = Integer32
_HpnicfSSHServerAuthRetries_Object = MibScalar
hpnicfSSHServerAuthRetries = _HpnicfSSHServerAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 4),
    _HpnicfSSHServerAuthRetries_Type()
)
hpnicfSSHServerAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSSHServerAuthRetries.setStatus("current")
_HpnicfSSHServerAuthTimeout_Type = Integer32
_HpnicfSSHServerAuthTimeout_Object = MibScalar
hpnicfSSHServerAuthTimeout = _HpnicfSSHServerAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 5),
    _HpnicfSSHServerAuthTimeout_Type()
)
hpnicfSSHServerAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSSHServerAuthTimeout.setStatus("current")
_HpnicfSFTPServerIdleTimeout_Type = Integer32
_HpnicfSFTPServerIdleTimeout_Object = MibScalar
hpnicfSFTPServerIdleTimeout = _HpnicfSFTPServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 6),
    _HpnicfSFTPServerIdleTimeout_Type()
)
hpnicfSFTPServerIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSFTPServerIdleTimeout.setStatus("current")


class _HpnicfSSHServerEnable_Type(Integer32):
    """Custom type hpnicfSSHServerEnable based on Integer32"""
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


_HpnicfSSHServerEnable_Type.__name__ = "Integer32"
_HpnicfSSHServerEnable_Object = MibScalar
hpnicfSSHServerEnable = _HpnicfSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 7),
    _HpnicfSSHServerEnable_Type()
)
hpnicfSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSSHServerEnable.setStatus("current")


class _HpnicfSFTPServerEnable_Type(Integer32):
    """Custom type hpnicfSFTPServerEnable based on Integer32"""
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


_HpnicfSFTPServerEnable_Type.__name__ = "Integer32"
_HpnicfSFTPServerEnable_Object = MibScalar
hpnicfSFTPServerEnable = _HpnicfSFTPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 8),
    _HpnicfSFTPServerEnable_Type()
)
hpnicfSFTPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSFTPServerEnable.setStatus("current")


class _HpnicfSTelnetServerEnable_Type(Integer32):
    """Custom type hpnicfSTelnetServerEnable based on Integer32"""
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


_HpnicfSTelnetServerEnable_Type.__name__ = "Integer32"
_HpnicfSTelnetServerEnable_Object = MibScalar
hpnicfSTelnetServerEnable = _HpnicfSTelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 9),
    _HpnicfSTelnetServerEnable_Type()
)
hpnicfSTelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSTelnetServerEnable.setStatus("current")


class _HpnicfSCPServerEnable_Type(Integer32):
    """Custom type hpnicfSCPServerEnable based on Integer32"""
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


_HpnicfSCPServerEnable_Type.__name__ = "Integer32"
_HpnicfSCPServerEnable_Object = MibScalar
hpnicfSCPServerEnable = _HpnicfSCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 10),
    _HpnicfSCPServerEnable_Type()
)
hpnicfSCPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSCPServerEnable.setStatus("current")
_HpnicfSSHUserConfig_ObjectIdentity = ObjectIdentity
hpnicfSSHUserConfig = _HpnicfSSHUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2)
)
_HpnicfSSHUserConfigTable_Object = MibTable
hpnicfSSHUserConfigTable = _HpnicfSSHUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfSSHUserConfigTable.setStatus("current")
_HpnicfSSHUserConfigEntry_Object = MibTableRow
hpnicfSSHUserConfigEntry = _HpnicfSSHUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1)
)
hpnicfSSHUserConfigEntry.setIndexNames(
    (0, "HPN-ICF-SSH-MIB", "hpnicfSSHUserName"),
)
if mibBuilder.loadTexts:
    hpnicfSSHUserConfigEntry.setStatus("current")
_HpnicfSSHUserName_Type = DisplayString
_HpnicfSSHUserName_Object = MibTableColumn
hpnicfSSHUserName = _HpnicfSSHUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 1),
    _HpnicfSSHUserName_Type()
)
hpnicfSSHUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSSHUserName.setStatus("current")


class _HpnicfSSHUserServiceType_Type(Integer32):
    """Custom type hpnicfSSHUserServiceType based on Integer32"""
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


_HpnicfSSHUserServiceType_Type.__name__ = "Integer32"
_HpnicfSSHUserServiceType_Object = MibTableColumn
hpnicfSSHUserServiceType = _HpnicfSSHUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 2),
    _HpnicfSSHUserServiceType_Type()
)
hpnicfSSHUserServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSSHUserServiceType.setStatus("current")


class _HpnicfSSHUserAuthType_Type(Integer32):
    """Custom type hpnicfSSHUserAuthType based on Integer32"""
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


_HpnicfSSHUserAuthType_Type.__name__ = "Integer32"
_HpnicfSSHUserAuthType_Object = MibTableColumn
hpnicfSSHUserAuthType = _HpnicfSSHUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 3),
    _HpnicfSSHUserAuthType_Type()
)
hpnicfSSHUserAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSSHUserAuthType.setStatus("current")
_HpnicfSSHUserPublicKeyName_Type = DisplayString
_HpnicfSSHUserPublicKeyName_Object = MibTableColumn
hpnicfSSHUserPublicKeyName = _HpnicfSSHUserPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 4),
    _HpnicfSSHUserPublicKeyName_Type()
)
hpnicfSSHUserPublicKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSSHUserPublicKeyName.setStatus("current")
_HpnicfSSHUserWorkDirectory_Type = DisplayString
_HpnicfSSHUserWorkDirectory_Object = MibTableColumn
hpnicfSSHUserWorkDirectory = _HpnicfSSHUserWorkDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 5),
    _HpnicfSSHUserWorkDirectory_Type()
)
hpnicfSSHUserWorkDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSSHUserWorkDirectory.setStatus("current")
_HpnicfSSHUserRowStatus_Type = RowStatus
_HpnicfSSHUserRowStatus_Object = MibTableColumn
hpnicfSSHUserRowStatus = _HpnicfSSHUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 6),
    _HpnicfSSHUserRowStatus_Type()
)
hpnicfSSHUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSSHUserRowStatus.setStatus("current")
_HpnicfSSHSessionInfoTable_Object = MibTable
hpnicfSSHSessionInfoTable = _HpnicfSSHSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfSSHSessionInfoTable.setStatus("current")
_HpnicfSSHSessionInfoEntry_Object = MibTableRow
hpnicfSSHSessionInfoEntry = _HpnicfSSHSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1)
)
hpnicfSSHSessionInfoEntry.setIndexNames(
    (0, "HPN-ICF-SSH-MIB", "hpnicfSSHSessionID"),
)
if mibBuilder.loadTexts:
    hpnicfSSHSessionInfoEntry.setStatus("current")
_HpnicfSSHSessionID_Type = Integer32
_HpnicfSSHSessionID_Object = MibTableColumn
hpnicfSSHSessionID = _HpnicfSSHSessionID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 1),
    _HpnicfSSHSessionID_Type()
)
hpnicfSSHSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSSHSessionID.setStatus("current")
_HpnicfSSHSessionUserName_Type = DisplayString
_HpnicfSSHSessionUserName_Object = MibTableColumn
hpnicfSSHSessionUserName = _HpnicfSSHSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 2),
    _HpnicfSSHSessionUserName_Type()
)
hpnicfSSHSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionUserName.setStatus("current")
_HpnicfSSHSessionUserIpAddrType_Type = InetAddressType
_HpnicfSSHSessionUserIpAddrType_Object = MibTableColumn
hpnicfSSHSessionUserIpAddrType = _HpnicfSSHSessionUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 3),
    _HpnicfSSHSessionUserIpAddrType_Type()
)
hpnicfSSHSessionUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionUserIpAddrType.setStatus("current")
_HpnicfSSHSessionUserIpAddr_Type = InetAddress
_HpnicfSSHSessionUserIpAddr_Object = MibTableColumn
hpnicfSSHSessionUserIpAddr = _HpnicfSSHSessionUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 4),
    _HpnicfSSHSessionUserIpAddr_Type()
)
hpnicfSSHSessionUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionUserIpAddr.setStatus("current")
_HpnicfSSHSessionClientVersion_Type = DisplayString
_HpnicfSSHSessionClientVersion_Object = MibTableColumn
hpnicfSSHSessionClientVersion = _HpnicfSSHSessionClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 5),
    _HpnicfSSHSessionClientVersion_Type()
)
hpnicfSSHSessionClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionClientVersion.setStatus("current")


class _HpnicfSSHSessionServiceType_Type(Integer32):
    """Custom type hpnicfSSHSessionServiceType based on Integer32"""
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


_HpnicfSSHSessionServiceType_Type.__name__ = "Integer32"
_HpnicfSSHSessionServiceType_Object = MibTableColumn
hpnicfSSHSessionServiceType = _HpnicfSSHSessionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 6),
    _HpnicfSSHSessionServiceType_Type()
)
hpnicfSSHSessionServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionServiceType.setStatus("current")


class _HpnicfSSHSessionEncry_Type(Integer32):
    """Custom type hpnicfSSHSessionEncry based on Integer32"""
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


_HpnicfSSHSessionEncry_Type.__name__ = "Integer32"
_HpnicfSSHSessionEncry_Object = MibTableColumn
hpnicfSSHSessionEncry = _HpnicfSSHSessionEncry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 7),
    _HpnicfSSHSessionEncry_Type()
)
hpnicfSSHSessionEncry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionEncry.setStatus("current")


class _HpnicfSSHSessionState_Type(Integer32):
    """Custom type hpnicfSSHSessionState based on Integer32"""
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


_HpnicfSSHSessionState_Type.__name__ = "Integer32"
_HpnicfSSHSessionState_Object = MibTableColumn
hpnicfSSHSessionState = _HpnicfSSHSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 8),
    _HpnicfSSHSessionState_Type()
)
hpnicfSSHSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSSHSessionState.setStatus("current")
_HpnicfSSHServerObjForTrap_ObjectIdentity = ObjectIdentity
hpnicfSSHServerObjForTrap = _HpnicfSSHServerObjForTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2)
)
_HpnicfSSHAttemptUserName_Type = DisplayString
_HpnicfSSHAttemptUserName_Object = MibScalar
hpnicfSSHAttemptUserName = _HpnicfSSHAttemptUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 1),
    _HpnicfSSHAttemptUserName_Type()
)
hpnicfSSHAttemptUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSSHAttemptUserName.setStatus("current")
_HpnicfSSHAttemptIpAddrType_Type = InetAddressType
_HpnicfSSHAttemptIpAddrType_Object = MibScalar
hpnicfSSHAttemptIpAddrType = _HpnicfSSHAttemptIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 2),
    _HpnicfSSHAttemptIpAddrType_Type()
)
hpnicfSSHAttemptIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSSHAttemptIpAddrType.setStatus("current")
_HpnicfSSHAttemptIpAddr_Type = InetAddress
_HpnicfSSHAttemptIpAddr_Object = MibScalar
hpnicfSSHAttemptIpAddr = _HpnicfSSHAttemptIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 3),
    _HpnicfSSHAttemptIpAddr_Type()
)
hpnicfSSHAttemptIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSSHAttemptIpAddr.setStatus("current")


class _HpnicfSSHUserAuthFailureReason_Type(Integer32):
    """Custom type hpnicfSSHUserAuthFailureReason based on Integer32"""
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


_HpnicfSSHUserAuthFailureReason_Type.__name__ = "Integer32"
_HpnicfSSHUserAuthFailureReason_Object = MibScalar
hpnicfSSHUserAuthFailureReason = _HpnicfSSHUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 4),
    _HpnicfSSHUserAuthFailureReason_Type()
)
hpnicfSSHUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSSHUserAuthFailureReason.setStatus("current")
_HpnicfSSHServerNotifications_ObjectIdentity = ObjectIdentity
hpnicfSSHServerNotifications = _HpnicfSSHServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3)
)
_HpnicfSSHServerNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfSSHServerNotificationsPrefix = _HpnicfSSHServerNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfSSHUserAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 1)
)
hpnicfSSHUserAuthFailure.setObjects(
      *(("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptUserName"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddrType"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddr"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    hpnicfSSHUserAuthFailure.setStatus(
        "current"
    )

hpnicfSSHVersionNegotiationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 2)
)
hpnicfSSHVersionNegotiationFailure.setObjects(
      *(("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddrType"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddr"))
)
if mibBuilder.loadTexts:
    hpnicfSSHVersionNegotiationFailure.setStatus(
        "current"
    )

hpnicfSSHUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 3)
)
hpnicfSSHUserLogin.setObjects(
      *(("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserName"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddrType"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    hpnicfSSHUserLogin.setStatus(
        "current"
    )

hpnicfSSHUserLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 4)
)
hpnicfSSHUserLogoff.setObjects(
      *(("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserName"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddrType"),
        ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    hpnicfSSHUserLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SSH-MIB",
    **{"hpnicfSSH": hpnicfSSH,
       "hpnicfSSHServerMIB": hpnicfSSHServerMIB,
       "hpnicfSSHServerMIBObjects": hpnicfSSHServerMIBObjects,
       "hpnicfSSHServerGlobalConfig": hpnicfSSHServerGlobalConfig,
       "hpnicfSSHServerVersion": hpnicfSSHServerVersion,
       "hpnicfSSHServerCompatibleSSH1x": hpnicfSSHServerCompatibleSSH1x,
       "hpnicfSSHServerRekeyInterval": hpnicfSSHServerRekeyInterval,
       "hpnicfSSHServerAuthRetries": hpnicfSSHServerAuthRetries,
       "hpnicfSSHServerAuthTimeout": hpnicfSSHServerAuthTimeout,
       "hpnicfSFTPServerIdleTimeout": hpnicfSFTPServerIdleTimeout,
       "hpnicfSSHServerEnable": hpnicfSSHServerEnable,
       "hpnicfSFTPServerEnable": hpnicfSFTPServerEnable,
       "hpnicfSTelnetServerEnable": hpnicfSTelnetServerEnable,
       "hpnicfSCPServerEnable": hpnicfSCPServerEnable,
       "hpnicfSSHUserConfig": hpnicfSSHUserConfig,
       "hpnicfSSHUserConfigTable": hpnicfSSHUserConfigTable,
       "hpnicfSSHUserConfigEntry": hpnicfSSHUserConfigEntry,
       "hpnicfSSHUserName": hpnicfSSHUserName,
       "hpnicfSSHUserServiceType": hpnicfSSHUserServiceType,
       "hpnicfSSHUserAuthType": hpnicfSSHUserAuthType,
       "hpnicfSSHUserPublicKeyName": hpnicfSSHUserPublicKeyName,
       "hpnicfSSHUserWorkDirectory": hpnicfSSHUserWorkDirectory,
       "hpnicfSSHUserRowStatus": hpnicfSSHUserRowStatus,
       "hpnicfSSHSessionInfoTable": hpnicfSSHSessionInfoTable,
       "hpnicfSSHSessionInfoEntry": hpnicfSSHSessionInfoEntry,
       "hpnicfSSHSessionID": hpnicfSSHSessionID,
       "hpnicfSSHSessionUserName": hpnicfSSHSessionUserName,
       "hpnicfSSHSessionUserIpAddrType": hpnicfSSHSessionUserIpAddrType,
       "hpnicfSSHSessionUserIpAddr": hpnicfSSHSessionUserIpAddr,
       "hpnicfSSHSessionClientVersion": hpnicfSSHSessionClientVersion,
       "hpnicfSSHSessionServiceType": hpnicfSSHSessionServiceType,
       "hpnicfSSHSessionEncry": hpnicfSSHSessionEncry,
       "hpnicfSSHSessionState": hpnicfSSHSessionState,
       "hpnicfSSHServerObjForTrap": hpnicfSSHServerObjForTrap,
       "hpnicfSSHAttemptUserName": hpnicfSSHAttemptUserName,
       "hpnicfSSHAttemptIpAddrType": hpnicfSSHAttemptIpAddrType,
       "hpnicfSSHAttemptIpAddr": hpnicfSSHAttemptIpAddr,
       "hpnicfSSHUserAuthFailureReason": hpnicfSSHUserAuthFailureReason,
       "hpnicfSSHServerNotifications": hpnicfSSHServerNotifications,
       "hpnicfSSHServerNotificationsPrefix": hpnicfSSHServerNotificationsPrefix,
       "hpnicfSSHUserAuthFailure": hpnicfSSHUserAuthFailure,
       "hpnicfSSHVersionNegotiationFailure": hpnicfSSHVersionNegotiationFailure,
       "hpnicfSSHUserLogin": hpnicfSSHUserLogin,
       "hpnicfSSHUserLogoff": hpnicfSSHUserLogoff}
)
