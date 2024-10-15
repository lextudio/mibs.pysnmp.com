# SNMP MIB module (IBMIROCAUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMIROCAUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:55 2024
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class RowDefinition(Integer32):
    """Custom type RowDefinition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notReady", 3))
    )





class Enabled(Integer32):
    """Custom type Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class DateAndTime2(OctetString):
    """Custom type DateAndTime2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )





class SecureOctetString(OctetString):
    """Custom type SecureOctetString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )





class SecureDisplayString(OctetString):
    """Custom type SecureDisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )





class SecureRowDefinition(OctetString):
    """Custom type SecureRowDefinition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2210_ObjectIdentity = ObjectIdentity
ibm2210 = _Ibm2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72)
)
_IbmIROC_ObjectIdentity = ObjectIdentity
ibmIROC = _IbmIROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119)
)
_IbmIROCconfig_ObjectIdentity = ObjectIdentity
ibmIROCconfig = _IbmIROCconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7)
)
_IbmIROCconfigAuth_ObjectIdentity = ObjectIdentity
ibmIROCconfigAuth = _IbmIROCconfigAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2)
)
_IbmAuthTraps_ObjectIdentity = ObjectIdentity
ibmAuthTraps = _IbmAuthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 0)
)
_IbmAuthMIB_ObjectIdentity = ObjectIdentity
ibmAuthMIB = _IbmAuthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1)
)
_IbmAuthGeneral_ObjectIdentity = ObjectIdentity
ibmAuthGeneral = _IbmAuthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 1)
)
_AuthUserProfileTable_Object = MibTable
authUserProfileTable = _AuthUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    authUserProfileTable.setStatus("mandatory")
_AuthUserProfileEntry_Object = MibTableRow
authUserProfileEntry = _AuthUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1)
)
authUserProfileEntry.setIndexNames(
    (1, "IBMIROCAUTH-MIB", "authUserProfileName"),
)
if mibBuilder.loadTexts:
    authUserProfileEntry.setStatus("mandatory")


class _AuthUserProfileName_Type(DisplayString):
    """Custom type authUserProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AuthUserProfileName_Type.__name__ = "DisplayString"
_AuthUserProfileName_Object = MibTableColumn
authUserProfileName = _AuthUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 1),
    _AuthUserProfileName_Type()
)
authUserProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authUserProfileName.setStatus("mandatory")
_AuthUserProfileRowDefinition_Type = SecureRowDefinition
_AuthUserProfileRowDefinition_Object = MibTableColumn
authUserProfileRowDefinition = _AuthUserProfileRowDefinition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 2),
    _AuthUserProfileRowDefinition_Type()
)
authUserProfileRowDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileRowDefinition.setStatus("mandatory")
_AuthUserProfilePassword_Type = SecureDisplayString
_AuthUserProfilePassword_Object = MibTableColumn
authUserProfilePassword = _AuthUserProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 3),
    _AuthUserProfilePassword_Type()
)
authUserProfilePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfilePassword.setStatus("mandatory")


class _AuthUserProfileType_Type(OctetString):
    """Custom type authUserProfileType based on OctetString"""
    defaultHexValue = "20"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AuthUserProfileType_Type.__name__ = "OctetString"
_AuthUserProfileType_Object = MibTableColumn
authUserProfileType = _AuthUserProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 4),
    _AuthUserProfileType_Type()
)
authUserProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileType.setStatus("mandatory")


class _AuthUserProfileMaxConnectTime_Type(Integer32):
    """Custom type authUserProfileMaxConnectTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AuthUserProfileMaxConnectTime_Type.__name__ = "Integer32"
_AuthUserProfileMaxConnectTime_Object = MibTableColumn
authUserProfileMaxConnectTime = _AuthUserProfileMaxConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 5),
    _AuthUserProfileMaxConnectTime_Type()
)
authUserProfileMaxConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileMaxConnectTime.setStatus("mandatory")


class _AuthUserProfileCallbackType_Type(Integer32):
    """Custom type authUserProfileCallbackType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 2),
          ("roaming", 1))
    )


_AuthUserProfileCallbackType_Type.__name__ = "Integer32"
_AuthUserProfileCallbackType_Object = MibTableColumn
authUserProfileCallbackType = _AuthUserProfileCallbackType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 6),
    _AuthUserProfileCallbackType_Type()
)
authUserProfileCallbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileCallbackType.setStatus("mandatory")


class _AuthUserProfileCallbackNum_Type(DisplayString):
    """Custom type authUserProfileCallbackNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AuthUserProfileCallbackNum_Type.__name__ = "DisplayString"
_AuthUserProfileCallbackNum_Object = MibTableColumn
authUserProfileCallbackNum = _AuthUserProfileCallbackNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 7),
    _AuthUserProfileCallbackNum_Type()
)
authUserProfileCallbackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileCallbackNum.setStatus("mandatory")


class _AuthUserProfileDialout_Type(Enabled):
    """Custom type authUserProfileDialout based on Enabled"""


_AuthUserProfileDialout_Object = MibTableColumn
authUserProfileDialout = _AuthUserProfileDialout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 8),
    _AuthUserProfileDialout_Type()
)
authUserProfileDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileDialout.setStatus("mandatory")


class _AuthUserProfileEncryptionKey_Type(SecureOctetString):
    """Custom type authUserProfileEncryptionKey based on SecureOctetString"""
    defaultHexValue = ""


_AuthUserProfileEncryptionKey_Object = MibTableColumn
authUserProfileEncryptionKey = _AuthUserProfileEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 9),
    _AuthUserProfileEncryptionKey_Type()
)
authUserProfileEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileEncryptionKey.setStatus("mandatory")


class _AuthUserProfileStatus_Type(Integer32):
    """Custom type authUserProfileStatus based on Integer32"""
    defaultValue = 1

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
          ("locked", 3))
    )


_AuthUserProfileStatus_Type.__name__ = "Integer32"
_AuthUserProfileStatus_Object = MibTableColumn
authUserProfileStatus = _AuthUserProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 10),
    _AuthUserProfileStatus_Type()
)
authUserProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileStatus.setStatus("mandatory")


class _AuthUserProfileExpirationDate_Type(DateAndTime2):
    """Custom type authUserProfileExpirationDate based on DateAndTime2"""
    defaultHexValue = ""


_AuthUserProfileExpirationDate_Object = MibTableColumn
authUserProfileExpirationDate = _AuthUserProfileExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 11),
    _AuthUserProfileExpirationDate_Type()
)
authUserProfileExpirationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileExpirationDate.setStatus("mandatory")


class _AuthUserProfileGLoginAllowed_Type(Integer32):
    """Custom type authUserProfileGLoginAllowed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuthUserProfileGLoginAllowed_Type.__name__ = "Integer32"
_AuthUserProfileGLoginAllowed_Object = MibTableColumn
authUserProfileGLoginAllowed = _AuthUserProfileGLoginAllowed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 12),
    _AuthUserProfileGLoginAllowed_Type()
)
authUserProfileGLoginAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileGLoginAllowed.setStatus("mandatory")


class _AuthUserProfileGLoginsAttempts_Type(Integer32):
    """Custom type authUserProfileGLoginsAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuthUserProfileGLoginsAttempts_Type.__name__ = "Integer32"
_AuthUserProfileGLoginsAttempts_Object = MibTableColumn
authUserProfileGLoginsAttempts = _AuthUserProfileGLoginsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 13),
    _AuthUserProfileGLoginsAttempts_Type()
)
authUserProfileGLoginsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserProfileGLoginsAttempts.setStatus("mandatory")


class _AuthUserProfileLoginAttempts_Type(Integer32):
    """Custom type authUserProfileLoginAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuthUserProfileLoginAttempts_Type.__name__ = "Integer32"
_AuthUserProfileLoginAttempts_Object = MibTableColumn
authUserProfileLoginAttempts = _AuthUserProfileLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 14),
    _AuthUserProfileLoginAttempts_Type()
)
authUserProfileLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserProfileLoginAttempts.setStatus("mandatory")


class _AuthUserProfileLoginFails_Type(Integer32):
    """Custom type authUserProfileLoginFails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuthUserProfileLoginFails_Type.__name__ = "Integer32"
_AuthUserProfileLoginFails_Object = MibTableColumn
authUserProfileLoginFails = _AuthUserProfileLoginFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 15),
    _AuthUserProfileLoginFails_Type()
)
authUserProfileLoginFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserProfileLoginFails.setStatus("mandatory")


class _AuthUserProfileLoginLock_Type(Integer32):
    """Custom type authUserProfileLoginLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuthUserProfileLoginLock_Type.__name__ = "Integer32"
_AuthUserProfileLoginLock_Object = MibTableColumn
authUserProfileLoginLock = _AuthUserProfileLoginLock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 16),
    _AuthUserProfileLoginLock_Type()
)
authUserProfileLoginLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserProfileLoginLock.setStatus("mandatory")


class _AuthUserProfileIpType_Type(Integer32):
    """Custom type authUserProfileIpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("networkDials", 3),
          ("single", 1),
          ("singleDials", 4))
    )


_AuthUserProfileIpType_Type.__name__ = "Integer32"
_AuthUserProfileIpType_Object = MibTableColumn
authUserProfileIpType = _AuthUserProfileIpType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 17),
    _AuthUserProfileIpType_Type()
)
authUserProfileIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileIpType.setStatus("mandatory")


class _AuthUserProfileIpAddr_Type(IpAddress):
    """Custom type authUserProfileIpAddr based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_AuthUserProfileIpAddr_Object = MibTableColumn
authUserProfileIpAddr = _AuthUserProfileIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 18),
    _AuthUserProfileIpAddr_Type()
)
authUserProfileIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileIpAddr.setStatus("mandatory")


class _AuthUserProfileIpMask_Type(IpAddress):
    """Custom type authUserProfileIpMask based on IpAddress"""
    defaultValue = OctetString("255.255.255.255")


_AuthUserProfileIpMask_Object = MibTableColumn
authUserProfileIpMask = _AuthUserProfileIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 19),
    _AuthUserProfileIpMask_Type()
)
authUserProfileIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileIpMask.setStatus("mandatory")


class _AuthUserProfileHostName_Type(DisplayString):
    """Custom type authUserProfileHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AuthUserProfileHostName_Type.__name__ = "DisplayString"
_AuthUserProfileHostName_Object = MibTableColumn
authUserProfileHostName = _AuthUserProfileHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 20),
    _AuthUserProfileHostName_Type()
)
authUserProfileHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileHostName.setStatus("mandatory")
_AuthUserProfileSharedSecurity_Type = SecureDisplayString
_AuthUserProfileSharedSecurity_Object = MibTableColumn
authUserProfileSharedSecurity = _AuthUserProfileSharedSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 21),
    _AuthUserProfileSharedSecurity_Type()
)
authUserProfileSharedSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileSharedSecurity.setStatus("mandatory")


class _AuthUserProfileTunneled_Type(Enabled):
    """Custom type authUserProfileTunneled based on Enabled"""


_AuthUserProfileTunneled_Object = MibTableColumn
authUserProfileTunneled = _AuthUserProfileTunneled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 22),
    _AuthUserProfileTunneled_Type()
)
authUserProfileTunneled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileTunneled.setStatus("mandatory")


class _AuthUserProfileTunnelType_Type(Integer32):
    """Custom type authUserProfileTunnelType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("l2tp", 3)
    )


_AuthUserProfileTunnelType_Type.__name__ = "Integer32"
_AuthUserProfileTunnelType_Object = MibTableColumn
authUserProfileTunnelType = _AuthUserProfileTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 23),
    _AuthUserProfileTunnelType_Type()
)
authUserProfileTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileTunnelType.setStatus("mandatory")


class _AuthUserProfileTunnelMediumType_Type(Integer32):
    """Custom type authUserProfileTunnelMediumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_AuthUserProfileTunnelMediumType_Type.__name__ = "Integer32"
_AuthUserProfileTunnelMediumType_Object = MibTableColumn
authUserProfileTunnelMediumType = _AuthUserProfileTunnelMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 24),
    _AuthUserProfileTunnelMediumType_Type()
)
authUserProfileTunnelMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileTunnelMediumType.setStatus("mandatory")


class _AuthUserProfileTunnelServer_Type(DisplayString):
    """Custom type authUserProfileTunnelServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuthUserProfileTunnelServer_Type.__name__ = "DisplayString"
_AuthUserProfileTunnelServer_Object = MibTableColumn
authUserProfileTunnelServer = _AuthUserProfileTunnelServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 25),
    _AuthUserProfileTunnelServer_Type()
)
authUserProfileTunnelServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileTunnelServer.setStatus("mandatory")


class _AuthUserProfileVcEnabled_Type(Enabled):
    """Custom type authUserProfileVcEnabled based on Enabled"""


_AuthUserProfileVcEnabled_Object = MibTableColumn
authUserProfileVcEnabled = _AuthUserProfileVcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 26),
    _AuthUserProfileVcEnabled_Type()
)
authUserProfileVcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileVcEnabled.setStatus("mandatory")


class _AuthUserProfileVcMaxSuspendTime_Type(Integer32):
    """Custom type authUserProfileVcMaxSuspendTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AuthUserProfileVcMaxSuspendTime_Type.__name__ = "Integer32"
_AuthUserProfileVcMaxSuspendTime_Object = MibTableColumn
authUserProfileVcMaxSuspendTime = _AuthUserProfileVcMaxSuspendTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 27),
    _AuthUserProfileVcMaxSuspendTime_Type()
)
authUserProfileVcMaxSuspendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileVcMaxSuspendTime.setStatus("mandatory")


class _AuthUserProfileVcIdleTime_Type(Integer32):
    """Custom type authUserProfileVcIdleTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AuthUserProfileVcIdleTime_Type.__name__ = "Integer32"
_AuthUserProfileVcIdleTime_Object = MibTableColumn
authUserProfileVcIdleTime = _AuthUserProfileVcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 28),
    _AuthUserProfileVcIdleTime_Type()
)
authUserProfileVcIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserProfileVcIdleTime.setStatus("mandatory")
_IbmAuthDomains_ObjectIdentity = ObjectIdentity
ibmAuthDomains = _IbmAuthDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 2)
)
_IbmAuthConformance_ObjectIdentity = ObjectIdentity
ibmAuthConformance = _IbmAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3)
)
_AuthCompliances_ObjectIdentity = ObjectIdentity
authCompliances = _AuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 1)
)
_AuthUserProfileCompliance_ObjectIdentity = ObjectIdentity
authUserProfileCompliance = _AuthUserProfileCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 1, 1)
)
_AuthGroups_ObjectIdentity = ObjectIdentity
authGroups = _AuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 2)
)
_AuthUserProfileGroup_ObjectIdentity = ObjectIdentity
authUserProfileGroup = _AuthUserProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMIROCAUTH-MIB",
    **{"RowDefinition": RowDefinition,
       "Enabled": Enabled,
       "DateAndTime2": DateAndTime2,
       "SecureOctetString": SecureOctetString,
       "SecureDisplayString": SecureDisplayString,
       "SecureRowDefinition": SecureRowDefinition,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2210": ibm2210,
       "ibmIROC": ibmIROC,
       "ibmIROCconfig": ibmIROCconfig,
       "ibmIROCconfigAuth": ibmIROCconfigAuth,
       "ibmAuthTraps": ibmAuthTraps,
       "ibmAuthMIB": ibmAuthMIB,
       "ibmAuthGeneral": ibmAuthGeneral,
       "authUserProfileTable": authUserProfileTable,
       "authUserProfileEntry": authUserProfileEntry,
       "authUserProfileName": authUserProfileName,
       "authUserProfileRowDefinition": authUserProfileRowDefinition,
       "authUserProfilePassword": authUserProfilePassword,
       "authUserProfileType": authUserProfileType,
       "authUserProfileMaxConnectTime": authUserProfileMaxConnectTime,
       "authUserProfileCallbackType": authUserProfileCallbackType,
       "authUserProfileCallbackNum": authUserProfileCallbackNum,
       "authUserProfileDialout": authUserProfileDialout,
       "authUserProfileEncryptionKey": authUserProfileEncryptionKey,
       "authUserProfileStatus": authUserProfileStatus,
       "authUserProfileExpirationDate": authUserProfileExpirationDate,
       "authUserProfileGLoginAllowed": authUserProfileGLoginAllowed,
       "authUserProfileGLoginsAttempts": authUserProfileGLoginsAttempts,
       "authUserProfileLoginAttempts": authUserProfileLoginAttempts,
       "authUserProfileLoginFails": authUserProfileLoginFails,
       "authUserProfileLoginLock": authUserProfileLoginLock,
       "authUserProfileIpType": authUserProfileIpType,
       "authUserProfileIpAddr": authUserProfileIpAddr,
       "authUserProfileIpMask": authUserProfileIpMask,
       "authUserProfileHostName": authUserProfileHostName,
       "authUserProfileSharedSecurity": authUserProfileSharedSecurity,
       "authUserProfileTunneled": authUserProfileTunneled,
       "authUserProfileTunnelType": authUserProfileTunnelType,
       "authUserProfileTunnelMediumType": authUserProfileTunnelMediumType,
       "authUserProfileTunnelServer": authUserProfileTunnelServer,
       "authUserProfileVcEnabled": authUserProfileVcEnabled,
       "authUserProfileVcMaxSuspendTime": authUserProfileVcMaxSuspendTime,
       "authUserProfileVcIdleTime": authUserProfileVcIdleTime,
       "ibmAuthDomains": ibmAuthDomains,
       "ibmAuthConformance": ibmAuthConformance,
       "authCompliances": authCompliances,
       "authUserProfileCompliance": authUserProfileCompliance,
       "authGroups": authGroups,
       "authUserProfileGroup": authUserProfileGroup}
)
