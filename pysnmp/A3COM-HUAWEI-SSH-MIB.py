# SNMP MIB module (A3COM-HUAWEI-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:06 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cSSH = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22)
)
h3cSSH.setRevisions(
        ("2007-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSSHServerMIB_ObjectIdentity = ObjectIdentity
h3cSSHServerMIB = _H3cSSHServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1)
)
_H3cSSHServerMIBObjects_ObjectIdentity = ObjectIdentity
h3cSSHServerMIBObjects = _H3cSSHServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1)
)
_H3cSSHServerGlobalConfig_ObjectIdentity = ObjectIdentity
h3cSSHServerGlobalConfig = _H3cSSHServerGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1)
)
_H3cSSHServerVersion_Type = DisplayString
_H3cSSHServerVersion_Object = MibScalar
h3cSSHServerVersion = _H3cSSHServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 1),
    _H3cSSHServerVersion_Type()
)
h3cSSHServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHServerVersion.setStatus("current")


class _H3cSSHServerCompatibleSSH1x_Type(Integer32):
    """Custom type h3cSSHServerCompatibleSSH1x based on Integer32"""
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


_H3cSSHServerCompatibleSSH1x_Type.__name__ = "Integer32"
_H3cSSHServerCompatibleSSH1x_Object = MibScalar
h3cSSHServerCompatibleSSH1x = _H3cSSHServerCompatibleSSH1x_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 2),
    _H3cSSHServerCompatibleSSH1x_Type()
)
h3cSSHServerCompatibleSSH1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSSHServerCompatibleSSH1x.setStatus("current")
_H3cSSHServerRekeyInterval_Type = Integer32
_H3cSSHServerRekeyInterval_Object = MibScalar
h3cSSHServerRekeyInterval = _H3cSSHServerRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 3),
    _H3cSSHServerRekeyInterval_Type()
)
h3cSSHServerRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSSHServerRekeyInterval.setStatus("current")
_H3cSSHServerAuthRetries_Type = Integer32
_H3cSSHServerAuthRetries_Object = MibScalar
h3cSSHServerAuthRetries = _H3cSSHServerAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 4),
    _H3cSSHServerAuthRetries_Type()
)
h3cSSHServerAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSSHServerAuthRetries.setStatus("current")
_H3cSSHServerAuthTimeout_Type = Integer32
_H3cSSHServerAuthTimeout_Object = MibScalar
h3cSSHServerAuthTimeout = _H3cSSHServerAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 5),
    _H3cSSHServerAuthTimeout_Type()
)
h3cSSHServerAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSSHServerAuthTimeout.setStatus("current")
_H3cSFTPServerIdleTimeout_Type = Integer32
_H3cSFTPServerIdleTimeout_Object = MibScalar
h3cSFTPServerIdleTimeout = _H3cSFTPServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 6),
    _H3cSFTPServerIdleTimeout_Type()
)
h3cSFTPServerIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSFTPServerIdleTimeout.setStatus("current")


class _H3cSSHServerEnable_Type(Integer32):
    """Custom type h3cSSHServerEnable based on Integer32"""
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


_H3cSSHServerEnable_Type.__name__ = "Integer32"
_H3cSSHServerEnable_Object = MibScalar
h3cSSHServerEnable = _H3cSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 7),
    _H3cSSHServerEnable_Type()
)
h3cSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSSHServerEnable.setStatus("current")


class _H3cSFTPServerEnable_Type(Integer32):
    """Custom type h3cSFTPServerEnable based on Integer32"""
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


_H3cSFTPServerEnable_Type.__name__ = "Integer32"
_H3cSFTPServerEnable_Object = MibScalar
h3cSFTPServerEnable = _H3cSFTPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 8),
    _H3cSFTPServerEnable_Type()
)
h3cSFTPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSFTPServerEnable.setStatus("current")
_H3cSSHUserConfig_ObjectIdentity = ObjectIdentity
h3cSSHUserConfig = _H3cSSHUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2)
)
_H3cSSHUserConfigTable_Object = MibTable
h3cSSHUserConfigTable = _H3cSSHUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cSSHUserConfigTable.setStatus("current")
_H3cSSHUserConfigEntry_Object = MibTableRow
h3cSSHUserConfigEntry = _H3cSSHUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1)
)
h3cSSHUserConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SSH-MIB", "h3cSSHUserName"),
)
if mibBuilder.loadTexts:
    h3cSSHUserConfigEntry.setStatus("current")
_H3cSSHUserName_Type = DisplayString
_H3cSSHUserName_Object = MibTableColumn
h3cSSHUserName = _H3cSSHUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 1),
    _H3cSSHUserName_Type()
)
h3cSSHUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSSHUserName.setStatus("current")


class _H3cSSHUserServiceType_Type(Integer32):
    """Custom type h3cSSHUserServiceType based on Integer32"""
    defaultValue = 1

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
        *(("all", 2),
          ("invalid", 1),
          ("sftp", 4),
          ("stelnet", 3))
    )


_H3cSSHUserServiceType_Type.__name__ = "Integer32"
_H3cSSHUserServiceType_Object = MibTableColumn
h3cSSHUserServiceType = _H3cSSHUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 2),
    _H3cSSHUserServiceType_Type()
)
h3cSSHUserServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSSHUserServiceType.setStatus("current")


class _H3cSSHUserAuthType_Type(Integer32):
    """Custom type h3cSSHUserAuthType based on Integer32"""
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


_H3cSSHUserAuthType_Type.__name__ = "Integer32"
_H3cSSHUserAuthType_Object = MibTableColumn
h3cSSHUserAuthType = _H3cSSHUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 3),
    _H3cSSHUserAuthType_Type()
)
h3cSSHUserAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSSHUserAuthType.setStatus("current")
_H3cSSHUserPublicKeyName_Type = DisplayString
_H3cSSHUserPublicKeyName_Object = MibTableColumn
h3cSSHUserPublicKeyName = _H3cSSHUserPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 4),
    _H3cSSHUserPublicKeyName_Type()
)
h3cSSHUserPublicKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSSHUserPublicKeyName.setStatus("current")
_H3cSSHUserWorkDirectory_Type = DisplayString
_H3cSSHUserWorkDirectory_Object = MibTableColumn
h3cSSHUserWorkDirectory = _H3cSSHUserWorkDirectory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 5),
    _H3cSSHUserWorkDirectory_Type()
)
h3cSSHUserWorkDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSSHUserWorkDirectory.setStatus("current")
_H3cSSHUserRowStatus_Type = RowStatus
_H3cSSHUserRowStatus_Object = MibTableColumn
h3cSSHUserRowStatus = _H3cSSHUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 6),
    _H3cSSHUserRowStatus_Type()
)
h3cSSHUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSSHUserRowStatus.setStatus("current")
_H3cSSHSessionInfoTable_Object = MibTable
h3cSSHSessionInfoTable = _H3cSSHSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cSSHSessionInfoTable.setStatus("current")
_H3cSSHSessionInfoEntry_Object = MibTableRow
h3cSSHSessionInfoEntry = _H3cSSHSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1)
)
h3cSSHSessionInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionID"),
)
if mibBuilder.loadTexts:
    h3cSSHSessionInfoEntry.setStatus("current")
_H3cSSHSessionID_Type = Integer32
_H3cSSHSessionID_Object = MibTableColumn
h3cSSHSessionID = _H3cSSHSessionID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 1),
    _H3cSSHSessionID_Type()
)
h3cSSHSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSSHSessionID.setStatus("current")
_H3cSSHSessionUserName_Type = DisplayString
_H3cSSHSessionUserName_Object = MibTableColumn
h3cSSHSessionUserName = _H3cSSHSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 2),
    _H3cSSHSessionUserName_Type()
)
h3cSSHSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionUserName.setStatus("current")
_H3cSSHSessionUserIpAddrType_Type = InetAddressType
_H3cSSHSessionUserIpAddrType_Object = MibTableColumn
h3cSSHSessionUserIpAddrType = _H3cSSHSessionUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 3),
    _H3cSSHSessionUserIpAddrType_Type()
)
h3cSSHSessionUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionUserIpAddrType.setStatus("current")
_H3cSSHSessionUserIpAddr_Type = InetAddress
_H3cSSHSessionUserIpAddr_Object = MibTableColumn
h3cSSHSessionUserIpAddr = _H3cSSHSessionUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 4),
    _H3cSSHSessionUserIpAddr_Type()
)
h3cSSHSessionUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionUserIpAddr.setStatus("current")
_H3cSSHSessionClientVersion_Type = DisplayString
_H3cSSHSessionClientVersion_Object = MibTableColumn
h3cSSHSessionClientVersion = _H3cSSHSessionClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 5),
    _H3cSSHSessionClientVersion_Type()
)
h3cSSHSessionClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionClientVersion.setStatus("current")


class _H3cSSHSessionServiceType_Type(Integer32):
    """Custom type h3cSSHSessionServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("sftp", 3),
          ("stelnet", 2))
    )


_H3cSSHSessionServiceType_Type.__name__ = "Integer32"
_H3cSSHSessionServiceType_Object = MibTableColumn
h3cSSHSessionServiceType = _H3cSSHSessionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 6),
    _H3cSSHSessionServiceType_Type()
)
h3cSSHSessionServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionServiceType.setStatus("current")


class _H3cSSHSessionEncry_Type(Integer32):
    """Custom type h3cSSHSessionEncry based on Integer32"""
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


_H3cSSHSessionEncry_Type.__name__ = "Integer32"
_H3cSSHSessionEncry_Object = MibTableColumn
h3cSSHSessionEncry = _H3cSSHSessionEncry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 7),
    _H3cSSHSessionEncry_Type()
)
h3cSSHSessionEncry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionEncry.setStatus("current")


class _H3cSSHSessionState_Type(Integer32):
    """Custom type h3cSSHSessionState based on Integer32"""
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


_H3cSSHSessionState_Type.__name__ = "Integer32"
_H3cSSHSessionState_Object = MibTableColumn
h3cSSHSessionState = _H3cSSHSessionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 8),
    _H3cSSHSessionState_Type()
)
h3cSSHSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSSHSessionState.setStatus("current")
_H3cSSHServerObjForTrap_ObjectIdentity = ObjectIdentity
h3cSSHServerObjForTrap = _H3cSSHServerObjForTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2)
)
_H3cSSHAttemptUserName_Type = DisplayString
_H3cSSHAttemptUserName_Object = MibScalar
h3cSSHAttemptUserName = _H3cSSHAttemptUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 1),
    _H3cSSHAttemptUserName_Type()
)
h3cSSHAttemptUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSSHAttemptUserName.setStatus("current")
_H3cSSHAttemptIpAddrType_Type = InetAddressType
_H3cSSHAttemptIpAddrType_Object = MibScalar
h3cSSHAttemptIpAddrType = _H3cSSHAttemptIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 2),
    _H3cSSHAttemptIpAddrType_Type()
)
h3cSSHAttemptIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSSHAttemptIpAddrType.setStatus("current")
_H3cSSHAttemptIpAddr_Type = InetAddress
_H3cSSHAttemptIpAddr_Object = MibScalar
h3cSSHAttemptIpAddr = _H3cSSHAttemptIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 3),
    _H3cSSHAttemptIpAddr_Type()
)
h3cSSHAttemptIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSSHAttemptIpAddr.setStatus("current")


class _H3cSSHUserAuthFailureReason_Type(Integer32):
    """Custom type h3cSSHUserAuthFailureReason based on Integer32"""
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


_H3cSSHUserAuthFailureReason_Type.__name__ = "Integer32"
_H3cSSHUserAuthFailureReason_Object = MibScalar
h3cSSHUserAuthFailureReason = _H3cSSHUserAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 4),
    _H3cSSHUserAuthFailureReason_Type()
)
h3cSSHUserAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSSHUserAuthFailureReason.setStatus("current")
_H3cSSHServerNotifications_ObjectIdentity = ObjectIdentity
h3cSSHServerNotifications = _H3cSSHServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3)
)
_H3cSSHServerNotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cSSHServerNotificationsPrefix = _H3cSSHServerNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cSSHUserAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 1)
)
h3cSSHUserAuthFailure.setObjects(
      *(("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptUserName"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddrType"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddr"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHUserAuthFailureReason"))
)
if mibBuilder.loadTexts:
    h3cSSHUserAuthFailure.setStatus(
        "current"
    )

h3cSSHVersionNegotiationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 2)
)
h3cSSHVersionNegotiationFailure.setObjects(
      *(("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddrType"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddr"))
)
if mibBuilder.loadTexts:
    h3cSSHVersionNegotiationFailure.setStatus(
        "current"
    )

h3cSSHUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 3)
)
h3cSSHUserLogin.setObjects(
      *(("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserName"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddrType"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    h3cSSHUserLogin.setStatus(
        "current"
    )

h3cSSHUserLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 4)
)
h3cSSHUserLogoff.setObjects(
      *(("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserName"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddrType"),
        ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddr"))
)
if mibBuilder.loadTexts:
    h3cSSHUserLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-SSH-MIB",
    **{"h3cSSH": h3cSSH,
       "h3cSSHServerMIB": h3cSSHServerMIB,
       "h3cSSHServerMIBObjects": h3cSSHServerMIBObjects,
       "h3cSSHServerGlobalConfig": h3cSSHServerGlobalConfig,
       "h3cSSHServerVersion": h3cSSHServerVersion,
       "h3cSSHServerCompatibleSSH1x": h3cSSHServerCompatibleSSH1x,
       "h3cSSHServerRekeyInterval": h3cSSHServerRekeyInterval,
       "h3cSSHServerAuthRetries": h3cSSHServerAuthRetries,
       "h3cSSHServerAuthTimeout": h3cSSHServerAuthTimeout,
       "h3cSFTPServerIdleTimeout": h3cSFTPServerIdleTimeout,
       "h3cSSHServerEnable": h3cSSHServerEnable,
       "h3cSFTPServerEnable": h3cSFTPServerEnable,
       "h3cSSHUserConfig": h3cSSHUserConfig,
       "h3cSSHUserConfigTable": h3cSSHUserConfigTable,
       "h3cSSHUserConfigEntry": h3cSSHUserConfigEntry,
       "h3cSSHUserName": h3cSSHUserName,
       "h3cSSHUserServiceType": h3cSSHUserServiceType,
       "h3cSSHUserAuthType": h3cSSHUserAuthType,
       "h3cSSHUserPublicKeyName": h3cSSHUserPublicKeyName,
       "h3cSSHUserWorkDirectory": h3cSSHUserWorkDirectory,
       "h3cSSHUserRowStatus": h3cSSHUserRowStatus,
       "h3cSSHSessionInfoTable": h3cSSHSessionInfoTable,
       "h3cSSHSessionInfoEntry": h3cSSHSessionInfoEntry,
       "h3cSSHSessionID": h3cSSHSessionID,
       "h3cSSHSessionUserName": h3cSSHSessionUserName,
       "h3cSSHSessionUserIpAddrType": h3cSSHSessionUserIpAddrType,
       "h3cSSHSessionUserIpAddr": h3cSSHSessionUserIpAddr,
       "h3cSSHSessionClientVersion": h3cSSHSessionClientVersion,
       "h3cSSHSessionServiceType": h3cSSHSessionServiceType,
       "h3cSSHSessionEncry": h3cSSHSessionEncry,
       "h3cSSHSessionState": h3cSSHSessionState,
       "h3cSSHServerObjForTrap": h3cSSHServerObjForTrap,
       "h3cSSHAttemptUserName": h3cSSHAttemptUserName,
       "h3cSSHAttemptIpAddrType": h3cSSHAttemptIpAddrType,
       "h3cSSHAttemptIpAddr": h3cSSHAttemptIpAddr,
       "h3cSSHUserAuthFailureReason": h3cSSHUserAuthFailureReason,
       "h3cSSHServerNotifications": h3cSSHServerNotifications,
       "h3cSSHServerNotificationsPrefix": h3cSSHServerNotificationsPrefix,
       "h3cSSHUserAuthFailure": h3cSSHUserAuthFailure,
       "h3cSSHVersionNegotiationFailure": h3cSSHVersionNegotiationFailure,
       "h3cSSHUserLogin": h3cSSHUserLogin,
       "h3cSSHUserLogoff": h3cSSHUserLogoff}
)
