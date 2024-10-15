# SNMP MIB module (H3C-RSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-RSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:21 2024
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
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cRSA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23)
)
h3cRSA.setRevisions(
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

_H3cRSAMIBObjects_ObjectIdentity = ObjectIdentity
h3cRSAMIBObjects = _H3cRSAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1)
)
_H3cRSAPeerPublicKeyTable_Object = MibTable
h3cRSAPeerPublicKeyTable = _H3cRSAPeerPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRSAPeerPublicKeyTable.setStatus("current")
_H3cRSAPeerPublicKeyEntry_Object = MibTableRow
h3cRSAPeerPublicKeyEntry = _H3cRSAPeerPublicKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1)
)
h3cRSAPeerPublicKeyEntry.setIndexNames(
    (0, "H3C-RSA-MIB", "h3cRSAPeerPublicKeyName"),
)
if mibBuilder.loadTexts:
    h3cRSAPeerPublicKeyEntry.setStatus("current")


class _H3cRSAPeerPublicKeyName_Type(OctetString):
    """Custom type h3cRSAPeerPublicKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRSAPeerPublicKeyName_Type.__name__ = "OctetString"
_H3cRSAPeerPublicKeyName_Object = MibTableColumn
h3cRSAPeerPublicKeyName = _H3cRSAPeerPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1, 1),
    _H3cRSAPeerPublicKeyName_Type()
)
h3cRSAPeerPublicKeyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRSAPeerPublicKeyName.setStatus("current")
_H3cRSAPeerIpAddress_Type = IpAddress
_H3cRSAPeerIpAddress_Object = MibTableColumn
h3cRSAPeerIpAddress = _H3cRSAPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1, 2),
    _H3cRSAPeerIpAddress_Type()
)
h3cRSAPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRSAPeerIpAddress.setStatus("current")
_H3cRSAPeerFQDN_Type = DisplayString
_H3cRSAPeerFQDN_Object = MibTableColumn
h3cRSAPeerFQDN = _H3cRSAPeerFQDN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1, 3),
    _H3cRSAPeerFQDN_Type()
)
h3cRSAPeerFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRSAPeerFQDN.setStatus("current")


class _H3cRSAPeerPublicKeyCode_Type(OctetString):
    """Custom type h3cRSAPeerPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_H3cRSAPeerPublicKeyCode_Type.__name__ = "OctetString"
_H3cRSAPeerPublicKeyCode_Object = MibTableColumn
h3cRSAPeerPublicKeyCode = _H3cRSAPeerPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1, 4),
    _H3cRSAPeerPublicKeyCode_Type()
)
h3cRSAPeerPublicKeyCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRSAPeerPublicKeyCode.setStatus("current")
_H3cRSAPeerPublicKeyStatus_Type = RowStatus
_H3cRSAPeerPublicKeyStatus_Object = MibTableColumn
h3cRSAPeerPublicKeyStatus = _H3cRSAPeerPublicKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 1, 1, 5),
    _H3cRSAPeerPublicKeyStatus_Type()
)
h3cRSAPeerPublicKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRSAPeerPublicKeyStatus.setStatus("current")
_H3cRSALocalKeyPairTable_Object = MibTable
h3cRSALocalKeyPairTable = _H3cRSALocalKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    h3cRSALocalKeyPairTable.setStatus("current")
_H3cRSALocalKeyPairEntry_Object = MibTableRow
h3cRSALocalKeyPairEntry = _H3cRSALocalKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1)
)
h3cRSALocalKeyPairEntry.setIndexNames(
    (0, "H3C-RSA-MIB", "h3cRSALocalKeyIndex"),
)
if mibBuilder.loadTexts:
    h3cRSALocalKeyPairEntry.setStatus("current")


class _H3cRSALocalKeyIndex_Type(Integer32):
    """Custom type h3cRSALocalKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_H3cRSALocalKeyIndex_Type.__name__ = "Integer32"
_H3cRSALocalKeyIndex_Object = MibTableColumn
h3cRSALocalKeyIndex = _H3cRSALocalKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 1),
    _H3cRSALocalKeyIndex_Type()
)
h3cRSALocalKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRSALocalKeyIndex.setStatus("current")
_H3cRSALocalHostKeyName_Type = DisplayString
_H3cRSALocalHostKeyName_Object = MibTableColumn
h3cRSALocalHostKeyName = _H3cRSALocalHostKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 2),
    _H3cRSALocalHostKeyName_Type()
)
h3cRSALocalHostKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalHostKeyName.setStatus("current")


class _H3cRSALocalHostKeyCode_Type(OctetString):
    """Custom type h3cRSALocalHostKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_H3cRSALocalHostKeyCode_Type.__name__ = "OctetString"
_H3cRSALocalHostKeyCode_Object = MibTableColumn
h3cRSALocalHostKeyCode = _H3cRSALocalHostKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 3),
    _H3cRSALocalHostKeyCode_Type()
)
h3cRSALocalHostKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalHostKeyCode.setStatus("current")
_H3cRSALocalHostKeyCreatedTime_Type = DateAndTime
_H3cRSALocalHostKeyCreatedTime_Object = MibTableColumn
h3cRSALocalHostKeyCreatedTime = _H3cRSALocalHostKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 4),
    _H3cRSALocalHostKeyCreatedTime_Type()
)
h3cRSALocalHostKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalHostKeyCreatedTime.setStatus("current")
_H3cRSALocalServerKeyName_Type = DisplayString
_H3cRSALocalServerKeyName_Object = MibTableColumn
h3cRSALocalServerKeyName = _H3cRSALocalServerKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 5),
    _H3cRSALocalServerKeyName_Type()
)
h3cRSALocalServerKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalServerKeyName.setStatus("current")


class _H3cRSALocalServerKeyCode_Type(OctetString):
    """Custom type h3cRSALocalServerKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_H3cRSALocalServerKeyCode_Type.__name__ = "OctetString"
_H3cRSALocalServerKeyCode_Object = MibTableColumn
h3cRSALocalServerKeyCode = _H3cRSALocalServerKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 6),
    _H3cRSALocalServerKeyCode_Type()
)
h3cRSALocalServerKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalServerKeyCode.setStatus("current")
_H3cRSALocalServerKeyCreatedTime_Type = DateAndTime
_H3cRSALocalServerKeyCreatedTime_Object = MibTableColumn
h3cRSALocalServerKeyCreatedTime = _H3cRSALocalServerKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 7),
    _H3cRSALocalServerKeyCreatedTime_Type()
)
h3cRSALocalServerKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRSALocalServerKeyCreatedTime.setStatus("current")


class _H3cRSALocalKeyPairBits_Type(Integer32):
    """Custom type h3cRSALocalKeyPairBits based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_H3cRSALocalKeyPairBits_Type.__name__ = "Integer32"
_H3cRSALocalKeyPairBits_Object = MibTableColumn
h3cRSALocalKeyPairBits = _H3cRSALocalKeyPairBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 8),
    _H3cRSALocalKeyPairBits_Type()
)
h3cRSALocalKeyPairBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRSALocalKeyPairBits.setStatus("current")
_H3cRSALocalKeyStatus_Type = RowStatus
_H3cRSALocalKeyStatus_Object = MibTableColumn
h3cRSALocalKeyStatus = _H3cRSALocalKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 2, 1, 9),
    _H3cRSALocalKeyStatus_Type()
)
h3cRSALocalKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRSALocalKeyStatus.setStatus("current")
_H3cRSAPeerKeyConfigFailReason_Type = RSAKeyErrorCode
_H3cRSAPeerKeyConfigFailReason_Object = MibScalar
h3cRSAPeerKeyConfigFailReason = _H3cRSAPeerKeyConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 3),
    _H3cRSAPeerKeyConfigFailReason_Type()
)
h3cRSAPeerKeyConfigFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRSAPeerKeyConfigFailReason.setStatus("current")
_H3cRSALocalKeyFailReason_Type = RSAKeyErrorCode
_H3cRSALocalKeyFailReason_Object = MibScalar
h3cRSALocalKeyFailReason = _H3cRSALocalKeyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 1, 4),
    _H3cRSALocalKeyFailReason_Type()
)
h3cRSALocalKeyFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRSALocalKeyFailReason.setStatus("current")
_H3cRSANotifications_ObjectIdentity = ObjectIdentity
h3cRSANotifications = _H3cRSANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 2)
)

# Managed Objects groups


# Notification objects

h3cRSALocalKeyPairOpeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 2, 1)
)
h3cRSALocalKeyPairOpeFail.setObjects(
    ("H3C-RSA-MIB", "h3cRSALocalKeyFailReason")
)
if mibBuilder.loadTexts:
    h3cRSALocalKeyPairOpeFail.setStatus(
        "current"
    )

h3cRSAPeerKeyConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 23, 2, 2)
)
h3cRSAPeerKeyConfigFail.setObjects(
    ("H3C-RSA-MIB", "h3cRSAPeerKeyConfigFailReason")
)
if mibBuilder.loadTexts:
    h3cRSAPeerKeyConfigFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-RSA-MIB",
    **{"RSAKeyErrorCode": RSAKeyErrorCode,
       "h3cRSA": h3cRSA,
       "h3cRSAMIBObjects": h3cRSAMIBObjects,
       "h3cRSAPeerPublicKeyTable": h3cRSAPeerPublicKeyTable,
       "h3cRSAPeerPublicKeyEntry": h3cRSAPeerPublicKeyEntry,
       "h3cRSAPeerPublicKeyName": h3cRSAPeerPublicKeyName,
       "h3cRSAPeerIpAddress": h3cRSAPeerIpAddress,
       "h3cRSAPeerFQDN": h3cRSAPeerFQDN,
       "h3cRSAPeerPublicKeyCode": h3cRSAPeerPublicKeyCode,
       "h3cRSAPeerPublicKeyStatus": h3cRSAPeerPublicKeyStatus,
       "h3cRSALocalKeyPairTable": h3cRSALocalKeyPairTable,
       "h3cRSALocalKeyPairEntry": h3cRSALocalKeyPairEntry,
       "h3cRSALocalKeyIndex": h3cRSALocalKeyIndex,
       "h3cRSALocalHostKeyName": h3cRSALocalHostKeyName,
       "h3cRSALocalHostKeyCode": h3cRSALocalHostKeyCode,
       "h3cRSALocalHostKeyCreatedTime": h3cRSALocalHostKeyCreatedTime,
       "h3cRSALocalServerKeyName": h3cRSALocalServerKeyName,
       "h3cRSALocalServerKeyCode": h3cRSALocalServerKeyCode,
       "h3cRSALocalServerKeyCreatedTime": h3cRSALocalServerKeyCreatedTime,
       "h3cRSALocalKeyPairBits": h3cRSALocalKeyPairBits,
       "h3cRSALocalKeyStatus": h3cRSALocalKeyStatus,
       "h3cRSAPeerKeyConfigFailReason": h3cRSAPeerKeyConfigFailReason,
       "h3cRSALocalKeyFailReason": h3cRSALocalKeyFailReason,
       "h3cRSANotifications": h3cRSANotifications,
       "h3cRSALocalKeyPairOpeFail": h3cRSALocalKeyPairOpeFail,
       "h3cRSAPeerKeyConfigFail": h3cRSAPeerKeyConfigFail}
)
