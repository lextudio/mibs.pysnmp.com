# SNMP MIB module (HPN-ICF-RSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:45 2024
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

hpnicfRSA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23)
)
hpnicfRSA.setRevisions(
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

_HpnicfRSAMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfRSAMIBObjects = _HpnicfRSAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1)
)
_HpnicfRSAPeerPublicKeyTable_Object = MibTable
hpnicfRSAPeerPublicKeyTable = _HpnicfRSAPeerPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRSAPeerPublicKeyTable.setStatus("current")
_HpnicfRSAPeerPublicKeyEntry_Object = MibTableRow
hpnicfRSAPeerPublicKeyEntry = _HpnicfRSAPeerPublicKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1)
)
hpnicfRSAPeerPublicKeyEntry.setIndexNames(
    (0, "HPN-ICF-RSA-MIB", "hpnicfRSAPeerPublicKeyName"),
)
if mibBuilder.loadTexts:
    hpnicfRSAPeerPublicKeyEntry.setStatus("current")


class _HpnicfRSAPeerPublicKeyName_Type(OctetString):
    """Custom type hpnicfRSAPeerPublicKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfRSAPeerPublicKeyName_Type.__name__ = "OctetString"
_HpnicfRSAPeerPublicKeyName_Object = MibTableColumn
hpnicfRSAPeerPublicKeyName = _HpnicfRSAPeerPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1, 1),
    _HpnicfRSAPeerPublicKeyName_Type()
)
hpnicfRSAPeerPublicKeyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRSAPeerPublicKeyName.setStatus("current")
_HpnicfRSAPeerIpAddress_Type = IpAddress
_HpnicfRSAPeerIpAddress_Object = MibTableColumn
hpnicfRSAPeerIpAddress = _HpnicfRSAPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1, 2),
    _HpnicfRSAPeerIpAddress_Type()
)
hpnicfRSAPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRSAPeerIpAddress.setStatus("current")
_HpnicfRSAPeerFQDN_Type = DisplayString
_HpnicfRSAPeerFQDN_Object = MibTableColumn
hpnicfRSAPeerFQDN = _HpnicfRSAPeerFQDN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1, 3),
    _HpnicfRSAPeerFQDN_Type()
)
hpnicfRSAPeerFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRSAPeerFQDN.setStatus("current")


class _HpnicfRSAPeerPublicKeyCode_Type(OctetString):
    """Custom type hpnicfRSAPeerPublicKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HpnicfRSAPeerPublicKeyCode_Type.__name__ = "OctetString"
_HpnicfRSAPeerPublicKeyCode_Object = MibTableColumn
hpnicfRSAPeerPublicKeyCode = _HpnicfRSAPeerPublicKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1, 4),
    _HpnicfRSAPeerPublicKeyCode_Type()
)
hpnicfRSAPeerPublicKeyCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRSAPeerPublicKeyCode.setStatus("current")
_HpnicfRSAPeerPublicKeyStatus_Type = RowStatus
_HpnicfRSAPeerPublicKeyStatus_Object = MibTableColumn
hpnicfRSAPeerPublicKeyStatus = _HpnicfRSAPeerPublicKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 1, 1, 5),
    _HpnicfRSAPeerPublicKeyStatus_Type()
)
hpnicfRSAPeerPublicKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRSAPeerPublicKeyStatus.setStatus("current")
_HpnicfRSALocalKeyPairTable_Object = MibTable
hpnicfRSALocalKeyPairTable = _HpnicfRSALocalKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyPairTable.setStatus("current")
_HpnicfRSALocalKeyPairEntry_Object = MibTableRow
hpnicfRSALocalKeyPairEntry = _HpnicfRSALocalKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1)
)
hpnicfRSALocalKeyPairEntry.setIndexNames(
    (0, "HPN-ICF-RSA-MIB", "hpnicfRSALocalKeyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyPairEntry.setStatus("current")


class _HpnicfRSALocalKeyIndex_Type(Integer32):
    """Custom type hpnicfRSALocalKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HpnicfRSALocalKeyIndex_Type.__name__ = "Integer32"
_HpnicfRSALocalKeyIndex_Object = MibTableColumn
hpnicfRSALocalKeyIndex = _HpnicfRSALocalKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 1),
    _HpnicfRSALocalKeyIndex_Type()
)
hpnicfRSALocalKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyIndex.setStatus("current")
_HpnicfRSALocalHostKeyName_Type = DisplayString
_HpnicfRSALocalHostKeyName_Object = MibTableColumn
hpnicfRSALocalHostKeyName = _HpnicfRSALocalHostKeyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 2),
    _HpnicfRSALocalHostKeyName_Type()
)
hpnicfRSALocalHostKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalHostKeyName.setStatus("current")


class _HpnicfRSALocalHostKeyCode_Type(OctetString):
    """Custom type hpnicfRSALocalHostKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_HpnicfRSALocalHostKeyCode_Type.__name__ = "OctetString"
_HpnicfRSALocalHostKeyCode_Object = MibTableColumn
hpnicfRSALocalHostKeyCode = _HpnicfRSALocalHostKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 3),
    _HpnicfRSALocalHostKeyCode_Type()
)
hpnicfRSALocalHostKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalHostKeyCode.setStatus("current")
_HpnicfRSALocalHostKeyCreatedTime_Type = DateAndTime
_HpnicfRSALocalHostKeyCreatedTime_Object = MibTableColumn
hpnicfRSALocalHostKeyCreatedTime = _HpnicfRSALocalHostKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 4),
    _HpnicfRSALocalHostKeyCreatedTime_Type()
)
hpnicfRSALocalHostKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalHostKeyCreatedTime.setStatus("current")
_HpnicfRSALocalServerKeyName_Type = DisplayString
_HpnicfRSALocalServerKeyName_Object = MibTableColumn
hpnicfRSALocalServerKeyName = _HpnicfRSALocalServerKeyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 5),
    _HpnicfRSALocalServerKeyName_Type()
)
hpnicfRSALocalServerKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalServerKeyName.setStatus("current")


class _HpnicfRSALocalServerKeyCode_Type(OctetString):
    """Custom type hpnicfRSALocalServerKeyCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 1024),
    )


_HpnicfRSALocalServerKeyCode_Type.__name__ = "OctetString"
_HpnicfRSALocalServerKeyCode_Object = MibTableColumn
hpnicfRSALocalServerKeyCode = _HpnicfRSALocalServerKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 6),
    _HpnicfRSALocalServerKeyCode_Type()
)
hpnicfRSALocalServerKeyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalServerKeyCode.setStatus("current")
_HpnicfRSALocalServerKeyCreatedTime_Type = DateAndTime
_HpnicfRSALocalServerKeyCreatedTime_Object = MibTableColumn
hpnicfRSALocalServerKeyCreatedTime = _HpnicfRSALocalServerKeyCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 7),
    _HpnicfRSALocalServerKeyCreatedTime_Type()
)
hpnicfRSALocalServerKeyCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRSALocalServerKeyCreatedTime.setStatus("current")


class _HpnicfRSALocalKeyPairBits_Type(Integer32):
    """Custom type hpnicfRSALocalKeyPairBits based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_HpnicfRSALocalKeyPairBits_Type.__name__ = "Integer32"
_HpnicfRSALocalKeyPairBits_Object = MibTableColumn
hpnicfRSALocalKeyPairBits = _HpnicfRSALocalKeyPairBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 8),
    _HpnicfRSALocalKeyPairBits_Type()
)
hpnicfRSALocalKeyPairBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyPairBits.setStatus("current")
_HpnicfRSALocalKeyStatus_Type = RowStatus
_HpnicfRSALocalKeyStatus_Object = MibTableColumn
hpnicfRSALocalKeyStatus = _HpnicfRSALocalKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 2, 1, 9),
    _HpnicfRSALocalKeyStatus_Type()
)
hpnicfRSALocalKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyStatus.setStatus("current")
_HpnicfRSAPeerKeyConfigFailReason_Type = RSAKeyErrorCode
_HpnicfRSAPeerKeyConfigFailReason_Object = MibScalar
hpnicfRSAPeerKeyConfigFailReason = _HpnicfRSAPeerKeyConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 3),
    _HpnicfRSAPeerKeyConfigFailReason_Type()
)
hpnicfRSAPeerKeyConfigFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRSAPeerKeyConfigFailReason.setStatus("current")
_HpnicfRSALocalKeyFailReason_Type = RSAKeyErrorCode
_HpnicfRSALocalKeyFailReason_Object = MibScalar
hpnicfRSALocalKeyFailReason = _HpnicfRSALocalKeyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 1, 4),
    _HpnicfRSALocalKeyFailReason_Type()
)
hpnicfRSALocalKeyFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyFailReason.setStatus("current")
_HpnicfRSANotifications_ObjectIdentity = ObjectIdentity
hpnicfRSANotifications = _HpnicfRSANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 2)
)

# Managed Objects groups


# Notification objects

hpnicfRSALocalKeyPairOpeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 2, 1)
)
hpnicfRSALocalKeyPairOpeFail.setObjects(
    ("HPN-ICF-RSA-MIB", "hpnicfRSALocalKeyFailReason")
)
if mibBuilder.loadTexts:
    hpnicfRSALocalKeyPairOpeFail.setStatus(
        "current"
    )

hpnicfRSAPeerKeyConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23, 2, 2)
)
hpnicfRSAPeerKeyConfigFail.setObjects(
    ("HPN-ICF-RSA-MIB", "hpnicfRSAPeerKeyConfigFailReason")
)
if mibBuilder.loadTexts:
    hpnicfRSAPeerKeyConfigFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RSA-MIB",
    **{"RSAKeyErrorCode": RSAKeyErrorCode,
       "hpnicfRSA": hpnicfRSA,
       "hpnicfRSAMIBObjects": hpnicfRSAMIBObjects,
       "hpnicfRSAPeerPublicKeyTable": hpnicfRSAPeerPublicKeyTable,
       "hpnicfRSAPeerPublicKeyEntry": hpnicfRSAPeerPublicKeyEntry,
       "hpnicfRSAPeerPublicKeyName": hpnicfRSAPeerPublicKeyName,
       "hpnicfRSAPeerIpAddress": hpnicfRSAPeerIpAddress,
       "hpnicfRSAPeerFQDN": hpnicfRSAPeerFQDN,
       "hpnicfRSAPeerPublicKeyCode": hpnicfRSAPeerPublicKeyCode,
       "hpnicfRSAPeerPublicKeyStatus": hpnicfRSAPeerPublicKeyStatus,
       "hpnicfRSALocalKeyPairTable": hpnicfRSALocalKeyPairTable,
       "hpnicfRSALocalKeyPairEntry": hpnicfRSALocalKeyPairEntry,
       "hpnicfRSALocalKeyIndex": hpnicfRSALocalKeyIndex,
       "hpnicfRSALocalHostKeyName": hpnicfRSALocalHostKeyName,
       "hpnicfRSALocalHostKeyCode": hpnicfRSALocalHostKeyCode,
       "hpnicfRSALocalHostKeyCreatedTime": hpnicfRSALocalHostKeyCreatedTime,
       "hpnicfRSALocalServerKeyName": hpnicfRSALocalServerKeyName,
       "hpnicfRSALocalServerKeyCode": hpnicfRSALocalServerKeyCode,
       "hpnicfRSALocalServerKeyCreatedTime": hpnicfRSALocalServerKeyCreatedTime,
       "hpnicfRSALocalKeyPairBits": hpnicfRSALocalKeyPairBits,
       "hpnicfRSALocalKeyStatus": hpnicfRSALocalKeyStatus,
       "hpnicfRSAPeerKeyConfigFailReason": hpnicfRSAPeerKeyConfigFailReason,
       "hpnicfRSALocalKeyFailReason": hpnicfRSALocalKeyFailReason,
       "hpnicfRSANotifications": hpnicfRSANotifications,
       "hpnicfRSALocalKeyPairOpeFail": hpnicfRSALocalKeyPairOpeFail,
       "hpnicfRSAPeerKeyConfigFail": hpnicfRSAPeerKeyConfigFail}
)
