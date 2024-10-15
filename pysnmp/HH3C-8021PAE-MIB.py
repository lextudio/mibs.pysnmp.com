# SNMP MIB module (HH3C-8021PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-8021PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:24 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cpaeExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6)
)
hh3cpaeExtMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cpaeExtMibObjects_ObjectIdentity = ObjectIdentity
hh3cpaeExtMibObjects = _Hh3cpaeExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1)
)
_Hh3cdot1xPaeTraps_ObjectIdentity = ObjectIdentity
hh3cdot1xPaeTraps = _Hh3cdot1xPaeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0)
)
_Hh3cproxycheckVlanId_Type = Integer32
_Hh3cproxycheckVlanId_Object = MibScalar
hh3cproxycheckVlanId = _Hh3cproxycheckVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 2),
    _Hh3cproxycheckVlanId_Type()
)
hh3cproxycheckVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cproxycheckVlanId.setStatus("current")
_Hh3cproxycheckPortName_Type = OctetString
_Hh3cproxycheckPortName_Object = MibScalar
hh3cproxycheckPortName = _Hh3cproxycheckPortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 3),
    _Hh3cproxycheckPortName_Type()
)
hh3cproxycheckPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cproxycheckPortName.setStatus("current")
_Hh3cproxycheckMacAddr_Type = MacAddress
_Hh3cproxycheckMacAddr_Object = MibScalar
hh3cproxycheckMacAddr = _Hh3cproxycheckMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 4),
    _Hh3cproxycheckMacAddr_Type()
)
hh3cproxycheckMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cproxycheckMacAddr.setStatus("current")
_Hh3cproxycheckIpaddr_Type = IpAddress
_Hh3cproxycheckIpaddr_Object = MibScalar
hh3cproxycheckIpaddr = _Hh3cproxycheckIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 5),
    _Hh3cproxycheckIpaddr_Type()
)
hh3cproxycheckIpaddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cproxycheckIpaddr.setStatus("current")
_Hh3cproxycheckUsrName_Type = OctetString
_Hh3cproxycheckUsrName_Object = MibScalar
hh3cproxycheckUsrName = _Hh3cproxycheckUsrName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 6),
    _Hh3cproxycheckUsrName_Type()
)
hh3cproxycheckUsrName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cproxycheckUsrName.setStatus("current")
_Hh3cdot1xPaeSystem_ObjectIdentity = ObjectIdentity
hh3cdot1xPaeSystem = _Hh3cdot1xPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1)
)


class _Hh3cdot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type hh3cdot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_Hh3cdot1xAuthQuietPeriod_Object = MibScalar
hh3cdot1xAuthQuietPeriod = _Hh3cdot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 1),
    _Hh3cdot1xAuthQuietPeriod_Type()
)
hh3cdot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthQuietPeriod.setStatus("current")


class _Hh3cdot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type hh3cdot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30


_Hh3cdot1xAuthTxPeriod_Object = MibScalar
hh3cdot1xAuthTxPeriod = _Hh3cdot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 2),
    _Hh3cdot1xAuthTxPeriod_Type()
)
hh3cdot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthTxPeriod.setStatus("current")


class _Hh3cdot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type hh3cdot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30


_Hh3cdot1xAuthSuppTimeout_Object = MibScalar
hh3cdot1xAuthSuppTimeout = _Hh3cdot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 3),
    _Hh3cdot1xAuthSuppTimeout_Type()
)
hh3cdot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthSuppTimeout.setStatus("current")


class _Hh3cdot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type hh3cdot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 100


_Hh3cdot1xAuthServerTimeout_Object = MibScalar
hh3cdot1xAuthServerTimeout = _Hh3cdot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 4),
    _Hh3cdot1xAuthServerTimeout_Type()
)
hh3cdot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthServerTimeout.setStatus("current")


class _Hh3cdot1xAuthMaxReq_Type(Unsigned32):
    """Custom type hh3cdot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2


_Hh3cdot1xAuthMaxReq_Object = MibScalar
hh3cdot1xAuthMaxReq = _Hh3cdot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 5),
    _Hh3cdot1xAuthMaxReq_Type()
)
hh3cdot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthMaxReq.setStatus("current")


class _Hh3cdot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type hh3cdot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_Hh3cdot1xAuthReAuthPeriod_Object = MibScalar
hh3cdot1xAuthReAuthPeriod = _Hh3cdot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 6),
    _Hh3cdot1xAuthReAuthPeriod_Type()
)
hh3cdot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthReAuthPeriod.setStatus("current")


class _Hh3cdot1xAuthMethod_Type(Integer32):
    """Custom type hh3cdot1xAuthMethod based on Integer32"""
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


_Hh3cdot1xAuthMethod_Type.__name__ = "Integer32"
_Hh3cdot1xAuthMethod_Object = MibScalar
hh3cdot1xAuthMethod = _Hh3cdot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 7),
    _Hh3cdot1xAuthMethod_Type()
)
hh3cdot1xAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xAuthMethod.setStatus("current")
_Hh3cdot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
hh3cdot1xPaeAuthenticator = _Hh3cdot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2)
)
_Hh3cdot1xAuthConfigExtTable_Object = MibTable
hh3cdot1xAuthConfigExtTable = _Hh3cdot1xAuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cdot1xAuthConfigExtTable.setStatus("current")
_Hh3cdot1xAuthConfigExtEntry_Object = MibTableRow
hh3cdot1xAuthConfigExtEntry = _Hh3cdot1xAuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1)
)
hh3cdot1xAuthConfigExtEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hh3cdot1xAuthConfigExtEntry.setStatus("current")


class _Hh3cdot1xpaeportAuthAdminStatus_Type(Integer32):
    """Custom type hh3cdot1xpaeportAuthAdminStatus based on Integer32"""
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


_Hh3cdot1xpaeportAuthAdminStatus_Type.__name__ = "Integer32"
_Hh3cdot1xpaeportAuthAdminStatus_Object = MibTableColumn
hh3cdot1xpaeportAuthAdminStatus = _Hh3cdot1xpaeportAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 1),
    _Hh3cdot1xpaeportAuthAdminStatus_Type()
)
hh3cdot1xpaeportAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportAuthAdminStatus.setStatus("current")


class _Hh3cdot1xpaeportControlledType_Type(Integer32):
    """Custom type hh3cdot1xpaeportControlledType based on Integer32"""
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


_Hh3cdot1xpaeportControlledType_Type.__name__ = "Integer32"
_Hh3cdot1xpaeportControlledType_Object = MibTableColumn
hh3cdot1xpaeportControlledType = _Hh3cdot1xpaeportControlledType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 2),
    _Hh3cdot1xpaeportControlledType_Type()
)
hh3cdot1xpaeportControlledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportControlledType.setStatus("current")


class _Hh3cdot1xpaeportMaxUserNum_Type(Integer32):
    """Custom type hh3cdot1xpaeportMaxUserNum based on Integer32"""
    defaultValue = 256


_Hh3cdot1xpaeportMaxUserNum_Object = MibTableColumn
hh3cdot1xpaeportMaxUserNum = _Hh3cdot1xpaeportMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 3),
    _Hh3cdot1xpaeportMaxUserNum_Type()
)
hh3cdot1xpaeportMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportMaxUserNum.setStatus("current")
_Hh3cdot1xpaeportUserNumNow_Type = Integer32
_Hh3cdot1xpaeportUserNumNow_Object = MibTableColumn
hh3cdot1xpaeportUserNumNow = _Hh3cdot1xpaeportUserNumNow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 4),
    _Hh3cdot1xpaeportUserNumNow_Type()
)
hh3cdot1xpaeportUserNumNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportUserNumNow.setStatus("current")


class _Hh3cdot1xpaeportClearStatistics_Type(Integer32):
    """Custom type hh3cdot1xpaeportClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hh3cdot1xpaeportClearStatistics_Type.__name__ = "Integer32"
_Hh3cdot1xpaeportClearStatistics_Object = MibTableColumn
hh3cdot1xpaeportClearStatistics = _Hh3cdot1xpaeportClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 5),
    _Hh3cdot1xpaeportClearStatistics_Type()
)
hh3cdot1xpaeportClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportClearStatistics.setStatus("current")


class _Hh3cdot1xpaeportMcastTrigStatus_Type(Integer32):
    """Custom type hh3cdot1xpaeportMcastTrigStatus based on Integer32"""
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


_Hh3cdot1xpaeportMcastTrigStatus_Type.__name__ = "Integer32"
_Hh3cdot1xpaeportMcastTrigStatus_Object = MibTableColumn
hh3cdot1xpaeportMcastTrigStatus = _Hh3cdot1xpaeportMcastTrigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 6),
    _Hh3cdot1xpaeportMcastTrigStatus_Type()
)
hh3cdot1xpaeportMcastTrigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportMcastTrigStatus.setStatus("current")


class _Hh3cdot1xpaeportHandshakeStatus_Type(Integer32):
    """Custom type hh3cdot1xpaeportHandshakeStatus based on Integer32"""
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


_Hh3cdot1xpaeportHandshakeStatus_Type.__name__ = "Integer32"
_Hh3cdot1xpaeportHandshakeStatus_Object = MibTableColumn
hh3cdot1xpaeportHandshakeStatus = _Hh3cdot1xpaeportHandshakeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 7),
    _Hh3cdot1xpaeportHandshakeStatus_Type()
)
hh3cdot1xpaeportHandshakeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1xpaeportHandshakeStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3csupplicantproxycheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 1)
)
hh3csupplicantproxycheck.setObjects(
      *(("HH3C-8021PAE-MIB", "hh3cproxycheckVlanId"),
        ("HH3C-8021PAE-MIB", "hh3cproxycheckPortName"),
        ("HH3C-8021PAE-MIB", "hh3cproxycheckMacAddr"),
        ("HH3C-8021PAE-MIB", "hh3cproxycheckIpaddr"),
        ("HH3C-8021PAE-MIB", "hh3cproxycheckUsrName"))
)
if mibBuilder.loadTexts:
    hh3csupplicantproxycheck.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-8021PAE-MIB",
    **{"hh3cpaeExtMib": hh3cpaeExtMib,
       "hh3cpaeExtMibObjects": hh3cpaeExtMibObjects,
       "hh3cdot1xPaeTraps": hh3cdot1xPaeTraps,
       "hh3csupplicantproxycheck": hh3csupplicantproxycheck,
       "hh3cproxycheckVlanId": hh3cproxycheckVlanId,
       "hh3cproxycheckPortName": hh3cproxycheckPortName,
       "hh3cproxycheckMacAddr": hh3cproxycheckMacAddr,
       "hh3cproxycheckIpaddr": hh3cproxycheckIpaddr,
       "hh3cproxycheckUsrName": hh3cproxycheckUsrName,
       "hh3cdot1xPaeSystem": hh3cdot1xPaeSystem,
       "hh3cdot1xAuthQuietPeriod": hh3cdot1xAuthQuietPeriod,
       "hh3cdot1xAuthTxPeriod": hh3cdot1xAuthTxPeriod,
       "hh3cdot1xAuthSuppTimeout": hh3cdot1xAuthSuppTimeout,
       "hh3cdot1xAuthServerTimeout": hh3cdot1xAuthServerTimeout,
       "hh3cdot1xAuthMaxReq": hh3cdot1xAuthMaxReq,
       "hh3cdot1xAuthReAuthPeriod": hh3cdot1xAuthReAuthPeriod,
       "hh3cdot1xAuthMethod": hh3cdot1xAuthMethod,
       "hh3cdot1xPaeAuthenticator": hh3cdot1xPaeAuthenticator,
       "hh3cdot1xAuthConfigExtTable": hh3cdot1xAuthConfigExtTable,
       "hh3cdot1xAuthConfigExtEntry": hh3cdot1xAuthConfigExtEntry,
       "hh3cdot1xpaeportAuthAdminStatus": hh3cdot1xpaeportAuthAdminStatus,
       "hh3cdot1xpaeportControlledType": hh3cdot1xpaeportControlledType,
       "hh3cdot1xpaeportMaxUserNum": hh3cdot1xpaeportMaxUserNum,
       "hh3cdot1xpaeportUserNumNow": hh3cdot1xpaeportUserNumNow,
       "hh3cdot1xpaeportClearStatistics": hh3cdot1xpaeportClearStatistics,
       "hh3cdot1xpaeportMcastTrigStatus": hh3cdot1xpaeportMcastTrigStatus,
       "hh3cdot1xpaeportHandshakeStatus": hh3cdot1xpaeportHandshakeStatus}
)
