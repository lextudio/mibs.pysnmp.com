# SNMP MIB module (A3COM-HUAWEI-8021PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-8021PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:14 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiMgmt")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwpaeExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22)
)
hwpaeExtMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwpaeExtMibObjects_ObjectIdentity = ObjectIdentity
hwpaeExtMibObjects = _HwpaeExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1)
)
_Hwdot1xPaeTraps_ObjectIdentity = ObjectIdentity
hwdot1xPaeTraps = _Hwdot1xPaeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0)
)
_ProxycheckVlanId_Type = Integer32
_ProxycheckVlanId_Object = MibScalar
proxycheckVlanId = _ProxycheckVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 2),
    _ProxycheckVlanId_Type()
)
proxycheckVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proxycheckVlanId.setStatus("current")
_ProxycheckPortName_Type = OctetString
_ProxycheckPortName_Object = MibScalar
proxycheckPortName = _ProxycheckPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 3),
    _ProxycheckPortName_Type()
)
proxycheckPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proxycheckPortName.setStatus("current")
_ProxycheckMacAddr_Type = MacAddress
_ProxycheckMacAddr_Object = MibScalar
proxycheckMacAddr = _ProxycheckMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 4),
    _ProxycheckMacAddr_Type()
)
proxycheckMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proxycheckMacAddr.setStatus("current")
_ProxycheckIpaddr_Type = IpAddress
_ProxycheckIpaddr_Object = MibScalar
proxycheckIpaddr = _ProxycheckIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 5),
    _ProxycheckIpaddr_Type()
)
proxycheckIpaddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proxycheckIpaddr.setStatus("current")
_ProxycheckUsrName_Type = OctetString
_ProxycheckUsrName_Object = MibScalar
proxycheckUsrName = _ProxycheckUsrName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 6),
    _ProxycheckUsrName_Type()
)
proxycheckUsrName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proxycheckUsrName.setStatus("current")
_Hwdot1xPaeSystem_ObjectIdentity = ObjectIdentity
hwdot1xPaeSystem = _Hwdot1xPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1)
)


class _Hwdot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type hwdot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_Hwdot1xAuthQuietPeriod_Object = MibScalar
hwdot1xAuthQuietPeriod = _Hwdot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 1),
    _Hwdot1xAuthQuietPeriod_Type()
)
hwdot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthQuietPeriod.setStatus("current")


class _Hwdot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type hwdot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30


_Hwdot1xAuthTxPeriod_Object = MibScalar
hwdot1xAuthTxPeriod = _Hwdot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 2),
    _Hwdot1xAuthTxPeriod_Type()
)
hwdot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthTxPeriod.setStatus("current")


class _Hwdot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type hwdot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30


_Hwdot1xAuthSuppTimeout_Object = MibScalar
hwdot1xAuthSuppTimeout = _Hwdot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 3),
    _Hwdot1xAuthSuppTimeout_Type()
)
hwdot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthSuppTimeout.setStatus("current")


class _Hwdot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type hwdot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 100


_Hwdot1xAuthServerTimeout_Object = MibScalar
hwdot1xAuthServerTimeout = _Hwdot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 4),
    _Hwdot1xAuthServerTimeout_Type()
)
hwdot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthServerTimeout.setStatus("current")


class _Hwdot1xAuthMaxReq_Type(Unsigned32):
    """Custom type hwdot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2


_Hwdot1xAuthMaxReq_Object = MibScalar
hwdot1xAuthMaxReq = _Hwdot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 5),
    _Hwdot1xAuthMaxReq_Type()
)
hwdot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthMaxReq.setStatus("current")


class _Hwdot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type hwdot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_Hwdot1xAuthReAuthPeriod_Object = MibScalar
hwdot1xAuthReAuthPeriod = _Hwdot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 6),
    _Hwdot1xAuthReAuthPeriod_Type()
)
hwdot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthReAuthPeriod.setStatus("current")


class _Hwdot1xAuthMethod_Type(Integer32):
    """Custom type hwdot1xAuthMethod based on Integer32"""
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
        *(("chap", 1),
          ("eap", 3),
          ("pap", 2))
    )


_Hwdot1xAuthMethod_Type.__name__ = "Integer32"
_Hwdot1xAuthMethod_Object = MibScalar
hwdot1xAuthMethod = _Hwdot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 1, 7),
    _Hwdot1xAuthMethod_Type()
)
hwdot1xAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xAuthMethod.setStatus("current")
_Hwdot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
hwdot1xPaeAuthenticator = _Hwdot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2)
)
_Hwdot1xAuthConfigExtTable_Object = MibTable
hwdot1xAuthConfigExtTable = _Hwdot1xAuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwdot1xAuthConfigExtTable.setStatus("current")
_Hwdot1xAuthConfigExtEntry_Object = MibTableRow
hwdot1xAuthConfigExtEntry = _Hwdot1xAuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1)
)
hwdot1xAuthConfigExtEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hwdot1xAuthConfigExtEntry.setStatus("current")


class _Hwdot1xpaeportAuthAdminStatus_Type(Integer32):
    """Custom type hwdot1xpaeportAuthAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Hwdot1xpaeportAuthAdminStatus_Type.__name__ = "Integer32"
_Hwdot1xpaeportAuthAdminStatus_Object = MibTableColumn
hwdot1xpaeportAuthAdminStatus = _Hwdot1xpaeportAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 1),
    _Hwdot1xpaeportAuthAdminStatus_Type()
)
hwdot1xpaeportAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportAuthAdminStatus.setStatus("current")


class _Hwdot1xpaeportControlledType_Type(Integer32):
    """Custom type hwdot1xpaeportControlledType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("port", 1))
    )


_Hwdot1xpaeportControlledType_Type.__name__ = "Integer32"
_Hwdot1xpaeportControlledType_Object = MibTableColumn
hwdot1xpaeportControlledType = _Hwdot1xpaeportControlledType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 2),
    _Hwdot1xpaeportControlledType_Type()
)
hwdot1xpaeportControlledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportControlledType.setStatus("current")


class _Hwdot1xpaeportMaxUserNum_Type(Integer32):
    """Custom type hwdot1xpaeportMaxUserNum based on Integer32"""
    defaultValue = 256


_Hwdot1xpaeportMaxUserNum_Object = MibTableColumn
hwdot1xpaeportMaxUserNum = _Hwdot1xpaeportMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 3),
    _Hwdot1xpaeportMaxUserNum_Type()
)
hwdot1xpaeportMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportMaxUserNum.setStatus("current")
_Hwdot1xpaeportUserNumNow_Type = Integer32
_Hwdot1xpaeportUserNumNow_Object = MibTableColumn
hwdot1xpaeportUserNumNow = _Hwdot1xpaeportUserNumNow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 4),
    _Hwdot1xpaeportUserNumNow_Type()
)
hwdot1xpaeportUserNumNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1xpaeportUserNumNow.setStatus("current")


class _Hwdot1xpaeportClearStatistics_Type(Integer32):
    """Custom type hwdot1xpaeportClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hwdot1xpaeportClearStatistics_Type.__name__ = "Integer32"
_Hwdot1xpaeportClearStatistics_Object = MibTableColumn
hwdot1xpaeportClearStatistics = _Hwdot1xpaeportClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 5),
    _Hwdot1xpaeportClearStatistics_Type()
)
hwdot1xpaeportClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportClearStatistics.setStatus("current")


class _Hwdot1xpaeportMcastTrigStatus_Type(Integer32):
    """Custom type hwdot1xpaeportMcastTrigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Hwdot1xpaeportMcastTrigStatus_Type.__name__ = "Integer32"
_Hwdot1xpaeportMcastTrigStatus_Object = MibTableColumn
hwdot1xpaeportMcastTrigStatus = _Hwdot1xpaeportMcastTrigStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 6),
    _Hwdot1xpaeportMcastTrigStatus_Type()
)
hwdot1xpaeportMcastTrigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportMcastTrigStatus.setStatus("current")


class _Hwdot1xpaeportHandshakeStatus_Type(Integer32):
    """Custom type hwdot1xpaeportHandshakeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Hwdot1xpaeportHandshakeStatus_Type.__name__ = "Integer32"
_Hwdot1xpaeportHandshakeStatus_Object = MibTableColumn
hwdot1xpaeportHandshakeStatus = _Hwdot1xpaeportHandshakeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 2, 1, 1, 7),
    _Hwdot1xpaeportHandshakeStatus_Type()
)
hwdot1xpaeportHandshakeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1xpaeportHandshakeStatus.setStatus("current")

# Managed Objects groups


# Notification objects

supplicantproxycheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 22, 1, 0, 1)
)
supplicantproxycheck.setObjects(
      *(("A3COM-HUAWEI-8021PAE-MIB", "proxycheckVlanId"),
        ("A3COM-HUAWEI-8021PAE-MIB", "proxycheckPortName"),
        ("A3COM-HUAWEI-8021PAE-MIB", "proxycheckMacAddr"),
        ("A3COM-HUAWEI-8021PAE-MIB", "proxycheckIpaddr"),
        ("A3COM-HUAWEI-8021PAE-MIB", "proxycheckUsrName"))
)
if mibBuilder.loadTexts:
    supplicantproxycheck.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-8021PAE-MIB",
    **{"hwpaeExtMib": hwpaeExtMib,
       "hwpaeExtMibObjects": hwpaeExtMibObjects,
       "hwdot1xPaeTraps": hwdot1xPaeTraps,
       "supplicantproxycheck": supplicantproxycheck,
       "proxycheckVlanId": proxycheckVlanId,
       "proxycheckPortName": proxycheckPortName,
       "proxycheckMacAddr": proxycheckMacAddr,
       "proxycheckIpaddr": proxycheckIpaddr,
       "proxycheckUsrName": proxycheckUsrName,
       "hwdot1xPaeSystem": hwdot1xPaeSystem,
       "hwdot1xAuthQuietPeriod": hwdot1xAuthQuietPeriod,
       "hwdot1xAuthTxPeriod": hwdot1xAuthTxPeriod,
       "hwdot1xAuthSuppTimeout": hwdot1xAuthSuppTimeout,
       "hwdot1xAuthServerTimeout": hwdot1xAuthServerTimeout,
       "hwdot1xAuthMaxReq": hwdot1xAuthMaxReq,
       "hwdot1xAuthReAuthPeriod": hwdot1xAuthReAuthPeriod,
       "hwdot1xAuthMethod": hwdot1xAuthMethod,
       "hwdot1xPaeAuthenticator": hwdot1xPaeAuthenticator,
       "hwdot1xAuthConfigExtTable": hwdot1xAuthConfigExtTable,
       "hwdot1xAuthConfigExtEntry": hwdot1xAuthConfigExtEntry,
       "hwdot1xpaeportAuthAdminStatus": hwdot1xpaeportAuthAdminStatus,
       "hwdot1xpaeportControlledType": hwdot1xpaeportControlledType,
       "hwdot1xpaeportMaxUserNum": hwdot1xpaeportMaxUserNum,
       "hwdot1xpaeportUserNumNow": hwdot1xpaeportUserNumNow,
       "hwdot1xpaeportClearStatistics": hwdot1xpaeportClearStatistics,
       "hwdot1xpaeportMcastTrigStatus": hwdot1xpaeportMcastTrigStatus,
       "hwdot1xpaeportHandshakeStatus": hwdot1xpaeportHandshakeStatus}
)
