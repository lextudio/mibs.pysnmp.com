# SNMP MIB module (HH3C-RSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:49 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cRSA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23)
)
hh3cRSA.setRevisions(
        ("2004-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RSAKeyErrorCode(Integer32, TextualConvention):
    status = "current"
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("rsaErrHostEncKeyBackup", 9),
          ("rsaErrHostEncKeyDestroy", 12),
          ("rsaErrHostEncKeyGenerate", 11),
          ("rsaErrHostEncKeySave", 10),
          ("rsaErrHostSigKeyBackup", 13),
          ("rsaErrHostSigKeyDestroy", 16),
          ("rsaErrHostSigKeyGenerate", 15),
          ("rsaErrHostSigKeySave", 14),
          ("rsaErrKeyBackup", 5),
          ("rsaErrKeyDestroy", 8),
          ("rsaErrKeyGenerate", 7),
          ("rsaErrKeyNotReplaced", 4),
          ("rsaErrKeySaved", 6),
          ("rsaErrNoMemory", 3),
          ("rsaErrPeerKeyNotExist", 24),
          ("rsaErrPeerKeyNotRemoved", 23),
          ("rsaErrPeerKeyNotReplaced", 21),
          ("rsaErrPeerKeyNumArriveMax", 22),
          ("rsaErrServerKeyBackup", 17),
          ("rsaErrServerKeyDestroy", 20),
          ("rsaErrServerKeyGenerate", 19),
          ("rsaErrServerKeySave", 18),
          ("rsaFailure", 2),
          ("rsaStatusHostEncKeyExist", 28),
          ("rsaStatusHostEncKeyInvalid", 30),
          ("rsaStatusHostEncKeyNotExist", 29),
          ("rsaStatusHostSigKeyExist", 31),
          ("rsaStatusHostSigKeyInvalid", 33),
          ("rsaStatusHostSigKeyNotExist", 32),
          ("rsaStatusKeyExist", 25),
          ("rsaStatusKeyInvalid", 27),
          ("rsaStatusKeyNotExist", 26),
          ("rsaStatusServerKeyExist", 34),
          ("rsaStatusServerKeyInvalid", 36),
          ("rsaStatusServerKeyNotExist", 35),
          ("rsaSuccess", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cRSAMIBObjects_ObjectIdentity = ObjectIdentity
hh3cRSAMIBObjects = _Hh3cRSAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1)
)
_Hh3cRSAPeerPublicKeyTable_Object = MibTable
hh3cRSAPeerPublicKeyTable = _Hh3cRSAPeerPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRSAPeerPublicKeyTable.setStatus("current")
_Hh3cRSAPeerPublicKeyEntry_Object = MibTableRow
hh3cRSAPeerPublicKeyEntry = _Hh3cRSAPeerPublicKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1)
)
hh3cRSAPeerPublicKeyEntry.setIndexNames(
    (0, "HH3C-RSA-MIB", "hh3cRSAPeerPublicKeyName"),
)
if mibBuilder.loadTexts:
    hh3cRSAPeerPublicKeyEntry.setStatus("current")


class _Hh3cRSAPeerPublicKeyName_Type(OctetString):
    """Custom type hh3cRSAPeerPublicKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cRSAPeerPublicKeyName_Type.__name__ = "OctetString"
_Hh3cRSAPeerPublicKeyName_Object = MibTableColumn
hh3cRSAPeerPublicKeyName = _Hh3cRSAPeerPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1, 1),
    _Hh3cRSAPeerPublicKeyName_Type()
)
hh3cRSAPeerPublicKeyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRSAPeerPublicKeyName.setStatus("current")
_Hh3cRSAPeerIpAddress_Type = IpAddress
_Hh3cRSAPeerIpAddress_Object = MibTableColumn
hh3cRSAPeerIpAddress = _Hh3cRSAPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1, 2),
    _Hh3cRSAPeerIpAddress_Type()
)
hh3cRSAPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRSAPeerIpAddress.setStatus("current")
_Hh3cRSAPeerFQDN_Type = DisplayString
_Hh3cRSAPeerFQDN_Object = MibTableColumn
hh3cRSAPeerFQDN = _Hh3cRSAPeerFQDN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1, 3),
    _Hh3cRSAPeerFQDN_Type()
)
hh3cRSAPeerFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRSAPeerFQDN.setStatus("current")


class _Hh3cRSAPeerPublicKeyCode_Type(OctetString):
    """Custom type hh3cRSAPeerPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_Hh3cRSAPeerPublicKeyCode_Type.__name__ = "OctetString"
_Hh3cRSAPeerPublicKeyCode_Object = MibTableColumn
hh3cRSAPeerPublicKeyCode = _Hh3cRSAPeerPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1, 4),
    _Hh3cRSAPeerPublicKeyCode_Type()
)
hh3cRSAPeerPublicKeyCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRSAPeerPublicKeyCode.setStatus("current")
_Hh3cRSAPeerPublicKeyStatus_Type = RowStatus
_Hh3cRSAPeerPublicKeyStatus_Object = MibTableColumn
hh3cRSAPeerPublicKeyStatus = _Hh3cRSAPeerPublicKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 1, 1, 5),
    _Hh3cRSAPeerPublicKeyStatus_Type()
)
hh3cRSAPeerPublicKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRSAPeerPublicKeyStatus.setStatus("current")
_Hh3cRSALocalKeyPairTable_Object = MibTable
hh3cRSALocalKeyPairTable = _Hh3cRSALocalKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cRSALocalKeyPairTable.setStatus("current")
_Hh3cRSALocalKeyPairEntry_Object = MibTableRow
hh3cRSALocalKeyPairEntry = _Hh3cRSALocalKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1)
)
hh3cRSALocalKeyPairEntry.setIndexNames(
    (0, "HH3C-RSA-MIB", "hh3cRSALocalKeyIndex"),
)
if mibBuilder.loadTexts:
    hh3cRSALocalKeyPairEntry.setStatus("current")


class _Hh3cRSALocalKeyIndex_Type(Integer32):
    """Custom type hh3cRSALocalKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Hh3cRSALocalKeyIndex_Type.__name__ = "Integer32"
_Hh3cRSALocalKeyIndex_Object = MibTableColumn
hh3cRSALocalKeyIndex = _Hh3cRSALocalKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 1),
    _Hh3cRSALocalKeyIndex_Type()
)
hh3cRSALocalKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRSALocalKeyIndex.setStatus("current")
_Hh3cRSALocalHostKeyName_Type = DisplayString
_Hh3cRSALocalHostKeyName_Object = MibTableColumn
hh3cRSALocalHostKeyName = _Hh3cRSALocalHostKeyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 2),
    _Hh3cRSALocalHostKeyName_Type()
)
hh3cRSALocalHostKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalHostKeyName.setStatus("current")


class _Hh3cRSALocalHostKeyCode_Type(OctetString):
    """Custom type hh3cRSALocalHostKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_Hh3cRSALocalHostKeyCode_Type.__name__ = "OctetString"
_Hh3cRSALocalHostKeyCode_Object = MibTableColumn
hh3cRSALocalHostKeyCode = _Hh3cRSALocalHostKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 3),
    _Hh3cRSALocalHostKeyCode_Type()
)
hh3cRSALocalHostKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalHostKeyCode.setStatus("current")
_Hh3cRSALocalHostKeyCreatedTime_Type = DateAndTime
_Hh3cRSALocalHostKeyCreatedTime_Object = MibTableColumn
hh3cRSALocalHostKeyCreatedTime = _Hh3cRSALocalHostKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 4),
    _Hh3cRSALocalHostKeyCreatedTime_Type()
)
hh3cRSALocalHostKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalHostKeyCreatedTime.setStatus("current")
_Hh3cRSALocalServerKeyName_Type = DisplayString
_Hh3cRSALocalServerKeyName_Object = MibTableColumn
hh3cRSALocalServerKeyName = _Hh3cRSALocalServerKeyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 5),
    _Hh3cRSALocalServerKeyName_Type()
)
hh3cRSALocalServerKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalServerKeyName.setStatus("current")


class _Hh3cRSALocalServerKeyCode_Type(OctetString):
    """Custom type hh3cRSALocalServerKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_Hh3cRSALocalServerKeyCode_Type.__name__ = "OctetString"
_Hh3cRSALocalServerKeyCode_Object = MibTableColumn
hh3cRSALocalServerKeyCode = _Hh3cRSALocalServerKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 6),
    _Hh3cRSALocalServerKeyCode_Type()
)
hh3cRSALocalServerKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalServerKeyCode.setStatus("current")
_Hh3cRSALocalServerKeyCreatedTime_Type = DateAndTime
_Hh3cRSALocalServerKeyCreatedTime_Object = MibTableColumn
hh3cRSALocalServerKeyCreatedTime = _Hh3cRSALocalServerKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 7),
    _Hh3cRSALocalServerKeyCreatedTime_Type()
)
hh3cRSALocalServerKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRSALocalServerKeyCreatedTime.setStatus("current")


class _Hh3cRSALocalKeyPairBits_Type(Integer32):
    """Custom type hh3cRSALocalKeyPairBits based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_Hh3cRSALocalKeyPairBits_Type.__name__ = "Integer32"
_Hh3cRSALocalKeyPairBits_Object = MibTableColumn
hh3cRSALocalKeyPairBits = _Hh3cRSALocalKeyPairBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 8),
    _Hh3cRSALocalKeyPairBits_Type()
)
hh3cRSALocalKeyPairBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRSALocalKeyPairBits.setStatus("current")
_Hh3cRSALocalKeyStatus_Type = RowStatus
_Hh3cRSALocalKeyStatus_Object = MibTableColumn
hh3cRSALocalKeyStatus = _Hh3cRSALocalKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 2, 1, 9),
    _Hh3cRSALocalKeyStatus_Type()
)
hh3cRSALocalKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRSALocalKeyStatus.setStatus("current")
_Hh3cRSAPeerKeyConfigFailReason_Type = RSAKeyErrorCode
_Hh3cRSAPeerKeyConfigFailReason_Object = MibScalar
hh3cRSAPeerKeyConfigFailReason = _Hh3cRSAPeerKeyConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 3),
    _Hh3cRSAPeerKeyConfigFailReason_Type()
)
hh3cRSAPeerKeyConfigFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRSAPeerKeyConfigFailReason.setStatus("current")
_Hh3cRSALocalKeyFailReason_Type = RSAKeyErrorCode
_Hh3cRSALocalKeyFailReason_Object = MibScalar
hh3cRSALocalKeyFailReason = _Hh3cRSALocalKeyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 1, 4),
    _Hh3cRSALocalKeyFailReason_Type()
)
hh3cRSALocalKeyFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRSALocalKeyFailReason.setStatus("current")
_Hh3cRSANotifications_ObjectIdentity = ObjectIdentity
hh3cRSANotifications = _Hh3cRSANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 2)
)

# Managed Objects groups


# Notification objects

hh3cRSALocalKeyPairOpeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 2, 1)
)
hh3cRSALocalKeyPairOpeFail.setObjects(
    ("HH3C-RSA-MIB", "hh3cRSALocalKeyFailReason")
)
if mibBuilder.loadTexts:
    hh3cRSALocalKeyPairOpeFail.setStatus(
        "current"
    )

hh3cRSAPeerKeyConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23, 2, 2)
)
hh3cRSAPeerKeyConfigFail.setObjects(
    ("HH3C-RSA-MIB", "hh3cRSAPeerKeyConfigFailReason")
)
if mibBuilder.loadTexts:
    hh3cRSAPeerKeyConfigFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RSA-MIB",
    **{"RSAKeyErrorCode": RSAKeyErrorCode,
       "hh3cRSA": hh3cRSA,
       "hh3cRSAMIBObjects": hh3cRSAMIBObjects,
       "hh3cRSAPeerPublicKeyTable": hh3cRSAPeerPublicKeyTable,
       "hh3cRSAPeerPublicKeyEntry": hh3cRSAPeerPublicKeyEntry,
       "hh3cRSAPeerPublicKeyName": hh3cRSAPeerPublicKeyName,
       "hh3cRSAPeerIpAddress": hh3cRSAPeerIpAddress,
       "hh3cRSAPeerFQDN": hh3cRSAPeerFQDN,
       "hh3cRSAPeerPublicKeyCode": hh3cRSAPeerPublicKeyCode,
       "hh3cRSAPeerPublicKeyStatus": hh3cRSAPeerPublicKeyStatus,
       "hh3cRSALocalKeyPairTable": hh3cRSALocalKeyPairTable,
       "hh3cRSALocalKeyPairEntry": hh3cRSALocalKeyPairEntry,
       "hh3cRSALocalKeyIndex": hh3cRSALocalKeyIndex,
       "hh3cRSALocalHostKeyName": hh3cRSALocalHostKeyName,
       "hh3cRSALocalHostKeyCode": hh3cRSALocalHostKeyCode,
       "hh3cRSALocalHostKeyCreatedTime": hh3cRSALocalHostKeyCreatedTime,
       "hh3cRSALocalServerKeyName": hh3cRSALocalServerKeyName,
       "hh3cRSALocalServerKeyCode": hh3cRSALocalServerKeyCode,
       "hh3cRSALocalServerKeyCreatedTime": hh3cRSALocalServerKeyCreatedTime,
       "hh3cRSALocalKeyPairBits": hh3cRSALocalKeyPairBits,
       "hh3cRSALocalKeyStatus": hh3cRSALocalKeyStatus,
       "hh3cRSAPeerKeyConfigFailReason": hh3cRSAPeerKeyConfigFailReason,
       "hh3cRSALocalKeyFailReason": hh3cRSALocalKeyFailReason,
       "hh3cRSANotifications": hh3cRSANotifications,
       "hh3cRSALocalKeyPairOpeFail": hh3cRSALocalKeyPairOpeFail,
       "hh3cRSAPeerKeyConfigFail": hh3cRSAPeerKeyConfigFail}
)
