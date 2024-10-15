# SNMP MIB module (HUAWEI-WLAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:43 2024
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

(hwApIndex,
 hwApMac,
 hwApRegionIndex) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-DEVICE-MIB",
    "hwApIndex",
    "hwApMac",
    "hwApRegionIndex")

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

(hwRadioID,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-RADIO-MIB",
    "hwRadioID")

(hwWlanServiceEssSsid,
 hwWlanServiceStaMac) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-SERVICE-MIB",
    "hwWlanServiceEssSsid",
    "hwWlanServiceStaMac")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwWlanSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6)
)
hwWlanSecurity.setRevisions(
        ("2014-02-13 10:00",
         "2013-08-12 10:00",
         "2010-06-01 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWsecProfileTable_Object = MibTable
hwWsecProfileTable = _HwWsecProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1)
)
if mibBuilder.loadTexts:
    hwWsecProfileTable.setStatus("current")
_HwWsecProfileEntry_Object = MibTableRow
hwWsecProfileEntry = _HwWsecProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1)
)
hwWsecProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileName"),
)
if mibBuilder.loadTexts:
    hwWsecProfileEntry.setStatus("current")


class _HwWsecProfileName_Type(OctetString):
    """Custom type hwWsecProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWsecProfileName_Type.__name__ = "OctetString"
_HwWsecProfileName_Object = MibTableColumn
hwWsecProfileName = _HwWsecProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 1),
    _HwWsecProfileName_Type()
)
hwWsecProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileName.setStatus("current")
_HwWsecProfileWEPDataEncrypt_Type = TruthValue
_HwWsecProfileWEPDataEncrypt_Object = MibTableColumn
hwWsecProfileWEPDataEncrypt = _HwWsecProfileWEPDataEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 2),
    _HwWsecProfileWEPDataEncrypt_Type()
)
hwWsecProfileWEPDataEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWEPDataEncrypt.setStatus("current")


class _HwWsecProfileWEPDefaultKeyID_Type(Integer32):
    """Custom type hwWsecProfileWEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwWsecProfileWEPDefaultKeyID_Type.__name__ = "Integer32"
_HwWsecProfileWEPDefaultKeyID_Object = MibTableColumn
hwWsecProfileWEPDefaultKeyID = _HwWsecProfileWEPDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 3),
    _HwWsecProfileWEPDefaultKeyID_Type()
)
hwWsecProfileWEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWEPDefaultKeyID.setStatus("current")
_HwWsecProfileWEPKeyMappingLength_Type = Integer32
_HwWsecProfileWEPKeyMappingLength_Object = MibTableColumn
hwWsecProfileWEPKeyMappingLength = _HwWsecProfileWEPKeyMappingLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 4),
    _HwWsecProfileWEPKeyMappingLength_Type()
)
hwWsecProfileWEPKeyMappingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWEPKeyMappingLength.setStatus("current")
_HwWsecProfileAsuIpAddr_Type = IpAddress
_HwWsecProfileAsuIpAddr_Object = MibTableColumn
hwWsecProfileAsuIpAddr = _HwWsecProfileAsuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 5),
    _HwWsecProfileAsuIpAddr_Type()
)
hwWsecProfileAsuIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAsuIpAddr.setStatus("current")
_HwWsecProfileCaCertFileName_Type = OctetString
_HwWsecProfileCaCertFileName_Object = MibTableColumn
hwWsecProfileCaCertFileName = _HwWsecProfileCaCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 6),
    _HwWsecProfileCaCertFileName_Type()
)
hwWsecProfileCaCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileCaCertFileName.setStatus("current")
_HwWsecProfileAsuCertFileName_Type = OctetString
_HwWsecProfileAsuCertFileName_Object = MibTableColumn
hwWsecProfileAsuCertFileName = _HwWsecProfileAsuCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 7),
    _HwWsecProfileAsuCertFileName_Type()
)
hwWsecProfileAsuCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAsuCertFileName.setStatus("current")
_HwWsecProfileAcCertFileName_Type = OctetString
_HwWsecProfileAcCertFileName_Object = MibTableColumn
hwWsecProfileAcCertFileName = _HwWsecProfileAcCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 8),
    _HwWsecProfileAcCertFileName_Type()
)
hwWsecProfileAcCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAcCertFileName.setStatus("current")
_HwWsecProfileAcPrvKeyFileName_Type = OctetString
_HwWsecProfileAcPrvKeyFileName_Object = MibTableColumn
hwWsecProfileAcPrvKeyFileName = _HwWsecProfileAcPrvKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 9),
    _HwWsecProfileAcPrvKeyFileName_Type()
)
hwWsecProfileAcPrvKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAcPrvKeyFileName.setStatus("current")
_HwWsecProfileRsnaVersion_Type = Integer32
_HwWsecProfileRsnaVersion_Object = MibTableColumn
hwWsecProfileRsnaVersion = _HwWsecProfileRsnaVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 10),
    _HwWsecProfileRsnaVersion_Type()
)
hwWsecProfileRsnaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecProfileRsnaVersion.setStatus("current")
_HwWsecProfileWapiVersion_Type = Integer32
_HwWsecProfileWapiVersion_Object = MibTableColumn
hwWsecProfileWapiVersion = _HwWsecProfileWapiVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 11),
    _HwWsecProfileWapiVersion_Type()
)
hwWsecProfileWapiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecProfileWapiVersion.setStatus("current")
_HwWsecProfileRowStatus_Type = RowStatus
_HwWsecProfileRowStatus_Object = MibTableColumn
hwWsecProfileRowStatus = _HwWsecProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 12),
    _HwWsecProfileRowStatus_Type()
)
hwWsecProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWsecProfileRowStatus.setStatus("current")


class _HwWsecProfileCaPfxPassword_Type(OctetString):
    """Custom type hwWsecProfileCaPfxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWsecProfileCaPfxPassword_Type.__name__ = "OctetString"
_HwWsecProfileCaPfxPassword_Object = MibTableColumn
hwWsecProfileCaPfxPassword = _HwWsecProfileCaPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 13),
    _HwWsecProfileCaPfxPassword_Type()
)
hwWsecProfileCaPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileCaPfxPassword.setStatus("current")


class _HwWsecProfileCaCertState_Type(Integer32):
    """Custom type hwWsecProfileCaCertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwWsecProfileCaCertState_Type.__name__ = "Integer32"
_HwWsecProfileCaCertState_Object = MibTableColumn
hwWsecProfileCaCertState = _HwWsecProfileCaCertState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 14),
    _HwWsecProfileCaCertState_Type()
)
hwWsecProfileCaCertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecProfileCaCertState.setStatus("current")


class _HwWsecProfileAsuPfxPassword_Type(OctetString):
    """Custom type hwWsecProfileAsuPfxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWsecProfileAsuPfxPassword_Type.__name__ = "OctetString"
_HwWsecProfileAsuPfxPassword_Object = MibTableColumn
hwWsecProfileAsuPfxPassword = _HwWsecProfileAsuPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 15),
    _HwWsecProfileAsuPfxPassword_Type()
)
hwWsecProfileAsuPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAsuPfxPassword.setStatus("current")


class _HwWsecProfileAsuCertState_Type(Integer32):
    """Custom type hwWsecProfileAsuCertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwWsecProfileAsuCertState_Type.__name__ = "Integer32"
_HwWsecProfileAsuCertState_Object = MibTableColumn
hwWsecProfileAsuCertState = _HwWsecProfileAsuCertState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 16),
    _HwWsecProfileAsuCertState_Type()
)
hwWsecProfileAsuCertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecProfileAsuCertState.setStatus("current")


class _HwWsecProfileAcPfxPassword_Type(OctetString):
    """Custom type hwWsecProfileAcPfxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWsecProfileAcPfxPassword_Type.__name__ = "OctetString"
_HwWsecProfileAcPfxPassword_Object = MibTableColumn
hwWsecProfileAcPfxPassword = _HwWsecProfileAcPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 17),
    _HwWsecProfileAcPfxPassword_Type()
)
hwWsecProfileAcPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAcPfxPassword.setStatus("current")


class _HwWsecProfileAcCertState_Type(Integer32):
    """Custom type hwWsecProfileAcCertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_HwWsecProfileAcCertState_Type.__name__ = "Integer32"
_HwWsecProfileAcCertState_Object = MibTableColumn
hwWsecProfileAcCertState = _HwWsecProfileAcCertState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 18),
    _HwWsecProfileAcCertState_Type()
)
hwWsecProfileAcCertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecProfileAcCertState.setStatus("current")


class _HwWsecProfileKeyPfxPassword_Type(OctetString):
    """Custom type hwWsecProfileKeyPfxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWsecProfileKeyPfxPassword_Type.__name__ = "OctetString"
_HwWsecProfileKeyPfxPassword_Object = MibTableColumn
hwWsecProfileKeyPfxPassword = _HwWsecProfileKeyPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 19),
    _HwWsecProfileKeyPfxPassword_Type()
)
hwWsecProfileKeyPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileKeyPfxPassword.setStatus("current")


class _HwWsecProfileAsuType_Type(Integer32):
    """Custom type hwWsecProfileAsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 1))
    )


_HwWsecProfileAsuType_Type.__name__ = "Integer32"
_HwWsecProfileAsuType_Object = MibTableColumn
hwWsecProfileAsuType = _HwWsecProfileAsuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 20),
    _HwWsecProfileAsuType_Type()
)
hwWsecProfileAsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileAsuType.setStatus("current")


class _HwWsecProfileWpaPtkRekeySwitch_Type(Integer32):
    """Custom type hwWsecProfileWpaPtkRekeySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWsecProfileWpaPtkRekeySwitch_Type.__name__ = "Integer32"
_HwWsecProfileWpaPtkRekeySwitch_Object = MibTableColumn
hwWsecProfileWpaPtkRekeySwitch = _HwWsecProfileWpaPtkRekeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 21),
    _HwWsecProfileWpaPtkRekeySwitch_Type()
)
hwWsecProfileWpaPtkRekeySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpaPtkRekeySwitch.setStatus("current")


class _HwWsecProfileWpa2PtkRekeySwitch_Type(Integer32):
    """Custom type hwWsecProfileWpa2PtkRekeySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWsecProfileWpa2PtkRekeySwitch_Type.__name__ = "Integer32"
_HwWsecProfileWpa2PtkRekeySwitch_Object = MibTableColumn
hwWsecProfileWpa2PtkRekeySwitch = _HwWsecProfileWpa2PtkRekeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 22),
    _HwWsecProfileWpa2PtkRekeySwitch_Type()
)
hwWsecProfileWpa2PtkRekeySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpa2PtkRekeySwitch.setStatus("current")


class _HwWsecProfileWpaWpa2PtkRekeySwitch_Type(Integer32):
    """Custom type hwWsecProfileWpaWpa2PtkRekeySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWsecProfileWpaWpa2PtkRekeySwitch_Type.__name__ = "Integer32"
_HwWsecProfileWpaWpa2PtkRekeySwitch_Object = MibTableColumn
hwWsecProfileWpaWpa2PtkRekeySwitch = _HwWsecProfileWpaWpa2PtkRekeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 23),
    _HwWsecProfileWpaWpa2PtkRekeySwitch_Type()
)
hwWsecProfileWpaWpa2PtkRekeySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpaWpa2PtkRekeySwitch.setStatus("current")


class _HwWsecProfileWpaPtkRekeyInterval_Type(Integer32):
    """Custom type hwWsecProfileWpaPtkRekeyInterval based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_HwWsecProfileWpaPtkRekeyInterval_Type.__name__ = "Integer32"
_HwWsecProfileWpaPtkRekeyInterval_Object = MibTableColumn
hwWsecProfileWpaPtkRekeyInterval = _HwWsecProfileWpaPtkRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 24),
    _HwWsecProfileWpaPtkRekeyInterval_Type()
)
hwWsecProfileWpaPtkRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpaPtkRekeyInterval.setStatus("current")


class _HwWsecProfileWpa2PtkRekeyInterval_Type(Integer32):
    """Custom type hwWsecProfileWpa2PtkRekeyInterval based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_HwWsecProfileWpa2PtkRekeyInterval_Type.__name__ = "Integer32"
_HwWsecProfileWpa2PtkRekeyInterval_Object = MibTableColumn
hwWsecProfileWpa2PtkRekeyInterval = _HwWsecProfileWpa2PtkRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 25),
    _HwWsecProfileWpa2PtkRekeyInterval_Type()
)
hwWsecProfileWpa2PtkRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpa2PtkRekeyInterval.setStatus("current")


class _HwWsecProfileWpaWpa2PtkRekeyInterval_Type(Integer32):
    """Custom type hwWsecProfileWpaWpa2PtkRekeyInterval based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_HwWsecProfileWpaWpa2PtkRekeyInterval_Type.__name__ = "Integer32"
_HwWsecProfileWpaWpa2PtkRekeyInterval_Object = MibTableColumn
hwWsecProfileWpaWpa2PtkRekeyInterval = _HwWsecProfileWpaWpa2PtkRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 1, 1, 26),
    _HwWsecProfileWpaWpa2PtkRekeyInterval_Type()
)
hwWsecProfileWpaWpa2PtkRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecProfileWpaWpa2PtkRekeyInterval.setStatus("current")
_HwWsecWEPDefaultKeysTable_Object = MibTable
hwWsecWEPDefaultKeysTable = _HwWsecWEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 2)
)
if mibBuilder.loadTexts:
    hwWsecWEPDefaultKeysTable.setStatus("current")
_HwWsecWEPDefaultKeysEntry_Object = MibTableRow
hwWsecWEPDefaultKeysEntry = _HwWsecWEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 2, 1)
)
hwWsecWEPDefaultKeysEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileName"),
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    hwWsecWEPDefaultKeysEntry.setStatus("current")


class _HwWsecWEPDefaultKeyIndex_Type(Integer32):
    """Custom type hwWsecWEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwWsecWEPDefaultKeyIndex_Type.__name__ = "Integer32"
_HwWsecWEPDefaultKeyIndex_Object = MibTableColumn
hwWsecWEPDefaultKeyIndex = _HwWsecWEPDefaultKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 2, 1, 1),
    _HwWsecWEPDefaultKeyIndex_Type()
)
hwWsecWEPDefaultKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWsecWEPDefaultKeyIndex.setStatus("current")
_HwWsecWEPDefaultKeyValue_Type = OctetString
_HwWsecWEPDefaultKeyValue_Object = MibTableColumn
hwWsecWEPDefaultKeyValue = _HwWsecWEPDefaultKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 2, 1, 2),
    _HwWsecWEPDefaultKeyValue_Type()
)
hwWsecWEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecWEPDefaultKeyValue.setStatus("current")
_HwWsecWEPPassPhrase_Type = DisplayString
_HwWsecWEPPassPhrase_Object = MibTableColumn
hwWsecWEPPassPhrase = _HwWsecWEPPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 2, 1, 4),
    _HwWsecWEPPassPhrase_Type()
)
hwWsecWEPPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecWEPPassPhrase.setStatus("current")
_HwWsecWEPKeyMappingsTable_Object = MibTable
hwWsecWEPKeyMappingsTable = _HwWsecWEPKeyMappingsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3)
)
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingsTable.setStatus("current")
_HwWsecWEPKeyMappingsEntry_Object = MibTableRow
hwWsecWEPKeyMappingsEntry = _HwWsecWEPKeyMappingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1)
)
hwWsecWEPKeyMappingsEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileName"),
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPKeyMappingIndex"),
)
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingsEntry.setStatus("current")
_HwWsecWEPKeyMappingIndex_Type = Integer32
_HwWsecWEPKeyMappingIndex_Object = MibTableColumn
hwWsecWEPKeyMappingIndex = _HwWsecWEPKeyMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1, 1),
    _HwWsecWEPKeyMappingIndex_Type()
)
hwWsecWEPKeyMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingIndex.setStatus("current")
_HwWsecWEPKeyMappingAddress_Type = MacAddress
_HwWsecWEPKeyMappingAddress_Object = MibTableColumn
hwWsecWEPKeyMappingAddress = _HwWsecWEPKeyMappingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1, 2),
    _HwWsecWEPKeyMappingAddress_Type()
)
hwWsecWEPKeyMappingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingAddress.setStatus("current")
_HwWsecWEPKeyMappingWEPOn_Type = TruthValue
_HwWsecWEPKeyMappingWEPOn_Object = MibTableColumn
hwWsecWEPKeyMappingWEPOn = _HwWsecWEPKeyMappingWEPOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1, 3),
    _HwWsecWEPKeyMappingWEPOn_Type()
)
hwWsecWEPKeyMappingWEPOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingWEPOn.setStatus("current")
_HwWsecWEPKeyMappingValue_Type = OctetString
_HwWsecWEPKeyMappingValue_Object = MibTableColumn
hwWsecWEPKeyMappingValue = _HwWsecWEPKeyMappingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1, 4),
    _HwWsecWEPKeyMappingValue_Type()
)
hwWsecWEPKeyMappingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingValue.setStatus("current")


class _HwWsecWEPKeyMappingStatus_Type(RowStatus):
    """Custom type hwWsecWEPKeyMappingStatus based on RowStatus"""


_HwWsecWEPKeyMappingStatus_Object = MibTableColumn
hwWsecWEPKeyMappingStatus = _HwWsecWEPKeyMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 3, 1, 5),
    _HwWsecWEPKeyMappingStatus_Type()
)
hwWsecWEPKeyMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingStatus.setStatus("current")
_HwWsecAuthSuitesTable_Object = MibTable
hwWsecAuthSuitesTable = _HwWsecAuthSuitesTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4)
)
if mibBuilder.loadTexts:
    hwWsecAuthSuitesTable.setStatus("current")
_HwWsecAuthSuitesEntry_Object = MibTableRow
hwWsecAuthSuitesEntry = _HwWsecAuthSuitesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1)
)
hwWsecAuthSuitesEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileName"),
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthSuiteIndex"),
)
if mibBuilder.loadTexts:
    hwWsecAuthSuitesEntry.setStatus("current")


class _HwWsecAuthSuiteIndex_Type(Integer32):
    """Custom type hwWsecAuthSuiteIndex based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 8),
          ("shareKey", 7),
          ("wapiCertification", 1),
          ("wapiPreShareKey", 2),
          ("wpa18021x", 3),
          ("wpa1PreShareKey", 4),
          ("wpa1wpa28021x", 10),
          ("wpa1wpa2PreShareKey", 9),
          ("wpa28021x", 5),
          ("wpa2PreShareKey", 6))
    )


_HwWsecAuthSuiteIndex_Type.__name__ = "Integer32"
_HwWsecAuthSuiteIndex_Object = MibTableColumn
hwWsecAuthSuiteIndex = _HwWsecAuthSuiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 1),
    _HwWsecAuthSuiteIndex_Type()
)
hwWsecAuthSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWsecAuthSuiteIndex.setStatus("current")


class _HwWsecAuthSuite_Type(OctetString):
    """Custom type hwWsecAuthSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HwWsecAuthSuite_Type.__name__ = "OctetString"
_HwWsecAuthSuite_Object = MibTableColumn
hwWsecAuthSuite = _HwWsecAuthSuite_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 2),
    _HwWsecAuthSuite_Type()
)
hwWsecAuthSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthSuite.setStatus("current")
_HwWsecAuthSuiteEnabled_Type = TruthValue
_HwWsecAuthSuiteEnabled_Object = MibTableColumn
hwWsecAuthSuiteEnabled = _HwWsecAuthSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 3),
    _HwWsecAuthSuiteEnabled_Type()
)
hwWsecAuthSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthSuiteEnabled.setStatus("current")
_HwWsecAuthPreauthenticationImplemented_Type = TruthValue
_HwWsecAuthPreauthenticationImplemented_Object = MibTableColumn
hwWsecAuthPreauthenticationImplemented = _HwWsecAuthPreauthenticationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 4),
    _HwWsecAuthPreauthenticationImplemented_Type()
)
hwWsecAuthPreauthenticationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthPreauthenticationImplemented.setStatus("current")
_HwWsecAuthPreauthenticationEnabled_Type = TruthValue
_HwWsecAuthPreauthenticationEnabled_Object = MibTableColumn
hwWsecAuthPreauthenticationEnabled = _HwWsecAuthPreauthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 5),
    _HwWsecAuthPreauthenticationEnabled_Type()
)
hwWsecAuthPreauthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthPreauthenticationEnabled.setStatus("current")
_HwWsecAuthUnicastKeysSupported_Type = Integer32
_HwWsecAuthUnicastKeysSupported_Object = MibTableColumn
hwWsecAuthUnicastKeysSupported = _HwWsecAuthUnicastKeysSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 6),
    _HwWsecAuthUnicastKeysSupported_Type()
)
hwWsecAuthUnicastKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastKeysSupported.setStatus("current")


class _HwWsecAuthPairwiseCipher_Type(Integer32):
    """Custom type hwWsecAuthPairwiseCipher based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecAuthPairwiseCipher_Type.__name__ = "Integer32"
_HwWsecAuthPairwiseCipher_Object = MibTableColumn
hwWsecAuthPairwiseCipher = _HwWsecAuthPairwiseCipher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 7),
    _HwWsecAuthPairwiseCipher_Type()
)
hwWsecAuthPairwiseCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthPairwiseCipher.setStatus("current")
_HwWsecAuthPairwiseCipherSize_Type = Integer32
_HwWsecAuthPairwiseCipherSize_Object = MibTableColumn
hwWsecAuthPairwiseCipherSize = _HwWsecAuthPairwiseCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 8),
    _HwWsecAuthPairwiseCipherSize_Type()
)
hwWsecAuthPairwiseCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthPairwiseCipherSize.setStatus("current")


class _HwWsecAuthUnicastRekeyMethod_Type(Integer32):
    """Custom type hwWsecAuthUnicastRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2),
          ("timepacketBased", 4))
    )


_HwWsecAuthUnicastRekeyMethod_Type.__name__ = "Integer32"
_HwWsecAuthUnicastRekeyMethod_Object = MibTableColumn
hwWsecAuthUnicastRekeyMethod = _HwWsecAuthUnicastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 9),
    _HwWsecAuthUnicastRekeyMethod_Type()
)
hwWsecAuthUnicastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastRekeyMethod.setStatus("current")


class _HwWsecAuthUnicastRekeyTime_Type(Unsigned32):
    """Custom type hwWsecAuthUnicastRekeyTime based on Unsigned32"""
    defaultValue = 86400


_HwWsecAuthUnicastRekeyTime_Object = MibTableColumn
hwWsecAuthUnicastRekeyTime = _HwWsecAuthUnicastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 10),
    _HwWsecAuthUnicastRekeyTime_Type()
)
hwWsecAuthUnicastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastRekeyTime.setUnits("seconds")
_HwWsecAuthUnicastRekeyPackets_Type = Unsigned32
_HwWsecAuthUnicastRekeyPackets_Object = MibTableColumn
hwWsecAuthUnicastRekeyPackets = _HwWsecAuthUnicastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 11),
    _HwWsecAuthUnicastRekeyPackets_Type()
)
hwWsecAuthUnicastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastRekeyPackets.setUnits("1000 packets")


class _HwWsecAuthMulticastCipher_Type(Integer32):
    """Custom type hwWsecAuthMulticastCipher based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecAuthMulticastCipher_Type.__name__ = "Integer32"
_HwWsecAuthMulticastCipher_Object = MibTableColumn
hwWsecAuthMulticastCipher = _HwWsecAuthMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 12),
    _HwWsecAuthMulticastCipher_Type()
)
hwWsecAuthMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastCipher.setStatus("current")
_HwWsecAuthMulticastCipherSize_Type = Integer32
_HwWsecAuthMulticastCipherSize_Object = MibTableColumn
hwWsecAuthMulticastCipherSize = _HwWsecAuthMulticastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 13),
    _HwWsecAuthMulticastCipherSize_Type()
)
hwWsecAuthMulticastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastCipherSize.setStatus("current")


class _HwWsecAuthMulticastRekeyMethod_Type(Integer32):
    """Custom type hwWsecAuthMulticastRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2),
          ("timepacketBased", 4))
    )


_HwWsecAuthMulticastRekeyMethod_Type.__name__ = "Integer32"
_HwWsecAuthMulticastRekeyMethod_Object = MibTableColumn
hwWsecAuthMulticastRekeyMethod = _HwWsecAuthMulticastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 14),
    _HwWsecAuthMulticastRekeyMethod_Type()
)
hwWsecAuthMulticastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyMethod.setStatus("current")


class _HwWsecAuthMulticastRekeyTime_Type(Unsigned32):
    """Custom type hwWsecAuthMulticastRekeyTime based on Unsigned32"""
    defaultValue = 86400


_HwWsecAuthMulticastRekeyTime_Object = MibTableColumn
hwWsecAuthMulticastRekeyTime = _HwWsecAuthMulticastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 15),
    _HwWsecAuthMulticastRekeyTime_Type()
)
hwWsecAuthMulticastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyTime.setUnits("seconds")
_HwWsecAuthMulticastRekeyPackets_Type = Unsigned32
_HwWsecAuthMulticastRekeyPackets_Object = MibTableColumn
hwWsecAuthMulticastRekeyPackets = _HwWsecAuthMulticastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 16),
    _HwWsecAuthMulticastRekeyPackets_Type()
)
hwWsecAuthMulticastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyPackets.setUnits("1000 packets")
_HwWsecAuthMulticastRekeyStrict_Type = TruthValue
_HwWsecAuthMulticastRekeyStrict_Object = MibTableColumn
hwWsecAuthMulticastRekeyStrict = _HwWsecAuthMulticastRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 17),
    _HwWsecAuthMulticastRekeyStrict_Type()
)
hwWsecAuthMulticastRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastRekeyStrict.setStatus("current")
_HwWsecAuthPSKValue_Type = OctetString
_HwWsecAuthPSKValue_Object = MibTableColumn
hwWsecAuthPSKValue = _HwWsecAuthPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 18),
    _HwWsecAuthPSKValue_Type()
)
hwWsecAuthPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthPSKValue.setStatus("current")
_HwWsecAuthPSKPassPhrase_Type = DisplayString
_HwWsecAuthPSKPassPhrase_Object = MibTableColumn
hwWsecAuthPSKPassPhrase = _HwWsecAuthPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 19),
    _HwWsecAuthPSKPassPhrase_Type()
)
hwWsecAuthPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthPSKPassPhrase.setStatus("current")


class _HwWsecAuthCertificateUpdateCount_Type(Unsigned32):
    """Custom type hwWsecAuthCertificateUpdateCount based on Unsigned32"""
    defaultValue = 3


_HwWsecAuthCertificateUpdateCount_Object = MibTableColumn
hwWsecAuthCertificateUpdateCount = _HwWsecAuthCertificateUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 20),
    _HwWsecAuthCertificateUpdateCount_Type()
)
hwWsecAuthCertificateUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthCertificateUpdateCount.setStatus("current")


class _HwWsecAuthMulticastUpdateCount_Type(Unsigned32):
    """Custom type hwWsecAuthMulticastUpdateCount based on Unsigned32"""
    defaultValue = 3


_HwWsecAuthMulticastUpdateCount_Object = MibTableColumn
hwWsecAuthMulticastUpdateCount = _HwWsecAuthMulticastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 21),
    _HwWsecAuthMulticastUpdateCount_Type()
)
hwWsecAuthMulticastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthMulticastUpdateCount.setStatus("current")


class _HwWsecAuthUnicastUpdateCount_Type(Unsigned32):
    """Custom type hwWsecAuthUnicastUpdateCount based on Unsigned32"""
    defaultValue = 3


_HwWsecAuthUnicastUpdateCount_Object = MibTableColumn
hwWsecAuthUnicastUpdateCount = _HwWsecAuthUnicastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 22),
    _HwWsecAuthUnicastUpdateCount_Type()
)
hwWsecAuthUnicastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthUnicastUpdateCount.setStatus("current")


class _HwWsecAuthBKLifetime_Type(Unsigned32):
    """Custom type hwWsecAuthBKLifetime based on Unsigned32"""
    defaultValue = 43200


_HwWsecAuthBKLifetime_Object = MibTableColumn
hwWsecAuthBKLifetime = _HwWsecAuthBKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 23),
    _HwWsecAuthBKLifetime_Type()
)
hwWsecAuthBKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthBKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthBKLifetime.setUnits("seconds")


class _HwWsecAuthBKReauthThreshold_Type(Unsigned32):
    """Custom type hwWsecAuthBKReauthThreshold based on Unsigned32"""
    defaultValue = 70


_HwWsecAuthBKReauthThreshold_Object = MibTableColumn
hwWsecAuthBKReauthThreshold = _HwWsecAuthBKReauthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 24),
    _HwWsecAuthBKReauthThreshold_Type()
)
hwWsecAuthBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthBKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthBKReauthThreshold.setUnits("percentage")


class _HwWsecAuthSATimeout_Type(Unsigned32):
    """Custom type hwWsecAuthSATimeout based on Unsigned32"""
    defaultValue = 60


_HwWsecAuthSATimeout_Object = MibTableColumn
hwWsecAuthSATimeout = _HwWsecAuthSATimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 25),
    _HwWsecAuthSATimeout_Type()
)
hwWsecAuthSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthSATimeout.setStatus("current")
if mibBuilder.loadTexts:
    hwWsecAuthSATimeout.setUnits("seconds")
_HwWsecAuthExcludeUnencrypted_Type = TruthValue
_HwWsecAuthExcludeUnencrypted_Object = MibTableColumn
hwWsecAuthExcludeUnencrypted = _HwWsecAuthExcludeUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 26),
    _HwWsecAuthExcludeUnencrypted_Type()
)
hwWsecAuthExcludeUnencrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthExcludeUnencrypted.setStatus("current")
_HwWsecAuthDot1XMethod_Type = Integer32
_HwWsecAuthDot1XMethod_Object = MibTableColumn
hwWsecAuthDot1XMethod = _HwWsecAuthDot1XMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 27),
    _HwWsecAuthDot1XMethod_Type()
)
hwWsecAuthDot1XMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecAuthDot1XMethod.setStatus("current")
_HwWsecAuthControlledAuthControl_Type = TruthValue
_HwWsecAuthControlledAuthControl_Object = MibTableColumn
hwWsecAuthControlledAuthControl = _HwWsecAuthControlledAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 28),
    _HwWsecAuthControlledAuthControl_Type()
)
hwWsecAuthControlledAuthControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthControlledAuthControl.setStatus("current")
_HwWsecAuthControlledPortControl_Type = Integer32
_HwWsecAuthControlledPortControl_Object = MibTableColumn
hwWsecAuthControlledPortControl = _HwWsecAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 29),
    _HwWsecAuthControlledPortControl_Type()
)
hwWsecAuthControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthControlledPortControl.setStatus("current")
_HwWsecAuthOptionalImplemented_Type = TruthValue
_HwWsecAuthOptionalImplemented_Object = MibTableColumn
hwWsecAuthOptionalImplemented = _HwWsecAuthOptionalImplemented_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 4, 1, 30),
    _HwWsecAuthOptionalImplemented_Type()
)
hwWsecAuthOptionalImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecAuthOptionalImplemented.setStatus("current")
_HwWsecStatsTable_Object = MibTable
hwWsecStatsTable = _HwWsecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5)
)
if mibBuilder.loadTexts:
    hwWsecStatsTable.setStatus("current")
_HwWsecStatsEntry_Object = MibTableRow
hwWsecStatsEntry = _HwWsecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1)
)
hwWsecStatsEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsSTAAddress"),
)
if mibBuilder.loadTexts:
    hwWsecStatsEntry.setStatus("current")
_HwWsecStatsSTAAddress_Type = MacAddress
_HwWsecStatsSTAAddress_Object = MibTableColumn
hwWsecStatsSTAAddress = _HwWsecStatsSTAAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 1),
    _HwWsecStatsSTAAddress_Type()
)
hwWsecStatsSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsSTAAddress.setStatus("current")
_HwWsecStatsVersion_Type = Integer32
_HwWsecStatsVersion_Object = MibTableColumn
hwWsecStatsVersion = _HwWsecStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 2),
    _HwWsecStatsVersion_Type()
)
hwWsecStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsVersion.setStatus("current")
_HwWsecStatsBKIDUsed_Type = OctetString
_HwWsecStatsBKIDUsed_Object = MibTableColumn
hwWsecStatsBKIDUsed = _HwWsecStatsBKIDUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 3),
    _HwWsecStatsBKIDUsed_Type()
)
hwWsecStatsBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsBKIDUsed.setStatus("current")


class _HwWsecStatsAuthenticationSuiteSelected_Type(Integer32):
    """Custom type hwWsecStatsAuthenticationSuiteSelected based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 8),
          ("shareKey", 7),
          ("wapiCertification", 1),
          ("wapiPreShareKey", 2),
          ("wpa18021x", 3),
          ("wpa1PreShareKey", 4),
          ("wpa1wpa28021x", 10),
          ("wpa1wpa2PreShareKey", 9),
          ("wpa28021x", 5),
          ("wpa2PreShareKey", 6))
    )


_HwWsecStatsAuthenticationSuiteSelected_Type.__name__ = "Integer32"
_HwWsecStatsAuthenticationSuiteSelected_Object = MibTableColumn
hwWsecStatsAuthenticationSuiteSelected = _HwWsecStatsAuthenticationSuiteSelected_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 4),
    _HwWsecStatsAuthenticationSuiteSelected_Type()
)
hwWsecStatsAuthenticationSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsAuthenticationSuiteSelected.setStatus("current")


class _HwWsecStatsUnicastCipherSelected_Type(Integer32):
    """Custom type hwWsecStatsUnicastCipherSelected based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecStatsUnicastCipherSelected_Type.__name__ = "Integer32"
_HwWsecStatsUnicastCipherSelected_Object = MibTableColumn
hwWsecStatsUnicastCipherSelected = _HwWsecStatsUnicastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 5),
    _HwWsecStatsUnicastCipherSelected_Type()
)
hwWsecStatsUnicastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsUnicastCipherSelected.setStatus("current")


class _HwWsecStatsMulticastCipherSelected_Type(Integer32):
    """Custom type hwWsecStatsMulticastCipherSelected based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecStatsMulticastCipherSelected_Type.__name__ = "Integer32"
_HwWsecStatsMulticastCipherSelected_Object = MibTableColumn
hwWsecStatsMulticastCipherSelected = _HwWsecStatsMulticastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 6),
    _HwWsecStatsMulticastCipherSelected_Type()
)
hwWsecStatsMulticastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsMulticastCipherSelected.setStatus("current")


class _HwWsecStatsAuthenticationSuiteRequested_Type(Integer32):
    """Custom type hwWsecStatsAuthenticationSuiteRequested based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 8),
          ("shareKey", 7),
          ("wapiCertification", 1),
          ("wapiPreShareKey", 2),
          ("wpa18021x", 3),
          ("wpa1PreShareKey", 4),
          ("wpa1wpa28021x", 10),
          ("wpa1wpa2PreShareKey", 9),
          ("wpa28021x", 5),
          ("wpa2PreShareKey", 6))
    )


_HwWsecStatsAuthenticationSuiteRequested_Type.__name__ = "Integer32"
_HwWsecStatsAuthenticationSuiteRequested_Object = MibTableColumn
hwWsecStatsAuthenticationSuiteRequested = _HwWsecStatsAuthenticationSuiteRequested_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 7),
    _HwWsecStatsAuthenticationSuiteRequested_Type()
)
hwWsecStatsAuthenticationSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsAuthenticationSuiteRequested.setStatus("current")


class _HwWsecStatsUnicastCipherRequested_Type(Integer32):
    """Custom type hwWsecStatsUnicastCipherRequested based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecStatsUnicastCipherRequested_Type.__name__ = "Integer32"
_HwWsecStatsUnicastCipherRequested_Object = MibTableColumn
hwWsecStatsUnicastCipherRequested = _HwWsecStatsUnicastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 8),
    _HwWsecStatsUnicastCipherRequested_Type()
)
hwWsecStatsUnicastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsUnicastCipherRequested.setStatus("current")


class _HwWsecStatsMulticastCipherRequested_Type(Integer32):
    """Custom type hwWsecStatsMulticastCipherRequested based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ccmp", 5),
          ("null", 6),
          ("tkip", 4),
          ("tkipCcmp", 7),
          ("wep104", 3),
          ("wep128", 8),
          ("wep40", 2),
          ("wpiSms4", 1))
    )


_HwWsecStatsMulticastCipherRequested_Type.__name__ = "Integer32"
_HwWsecStatsMulticastCipherRequested_Object = MibTableColumn
hwWsecStatsMulticastCipherRequested = _HwWsecStatsMulticastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 9),
    _HwWsecStatsMulticastCipherRequested_Type()
)
hwWsecStatsMulticastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsMulticastCipherRequested.setStatus("current")
_HwWsecStatsWEPICVErrorCount_Type = Counter32
_HwWsecStatsWEPICVErrorCount_Object = MibTableColumn
hwWsecStatsWEPICVErrorCount = _HwWsecStatsWEPICVErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 10),
    _HwWsecStatsWEPICVErrorCount_Type()
)
hwWsecStatsWEPICVErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWEPICVErrorCount.setStatus("current")
_HwWsecStatsWEPExcludedCount_Type = Counter32
_HwWsecStatsWEPExcludedCount_Object = MibTableColumn
hwWsecStatsWEPExcludedCount = _HwWsecStatsWEPExcludedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 11),
    _HwWsecStatsWEPExcludedCount_Type()
)
hwWsecStatsWEPExcludedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWEPExcludedCount.setStatus("current")
_HwWsecStatsWEPUndecryptableCount_Type = Counter32
_HwWsecStatsWEPUndecryptableCount_Object = MibTableColumn
hwWsecStatsWEPUndecryptableCount = _HwWsecStatsWEPUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 12),
    _HwWsecStatsWEPUndecryptableCount_Type()
)
hwWsecStatsWEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWEPUndecryptableCount.setStatus("current")
_HwWsecStatsTKIPICVErrors_Type = Counter32
_HwWsecStatsTKIPICVErrors_Object = MibTableColumn
hwWsecStatsTKIPICVErrors = _HwWsecStatsTKIPICVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 13),
    _HwWsecStatsTKIPICVErrors_Type()
)
hwWsecStatsTKIPICVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsTKIPICVErrors.setStatus("current")
_HwWsecStatsTKIPLocalMICFailures_Type = Counter32
_HwWsecStatsTKIPLocalMICFailures_Object = MibTableColumn
hwWsecStatsTKIPLocalMICFailures = _HwWsecStatsTKIPLocalMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 14),
    _HwWsecStatsTKIPLocalMICFailures_Type()
)
hwWsecStatsTKIPLocalMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsTKIPLocalMICFailures.setStatus("current")
_HwWsecStatsTKIPRemoteMICFailures_Type = Counter32
_HwWsecStatsTKIPRemoteMICFailures_Object = MibTableColumn
hwWsecStatsTKIPRemoteMICFailures = _HwWsecStatsTKIPRemoteMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 15),
    _HwWsecStatsTKIPRemoteMICFailures_Type()
)
hwWsecStatsTKIPRemoteMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsTKIPRemoteMICFailures.setStatus("current")
_HwWsecStatsTKIPReplays_Type = Counter32
_HwWsecStatsTKIPReplays_Object = MibTableColumn
hwWsecStatsTKIPReplays = _HwWsecStatsTKIPReplays_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 16),
    _HwWsecStatsTKIPReplays_Type()
)
hwWsecStatsTKIPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsTKIPReplays.setStatus("current")
_HwWsecStatsCCMPReplays_Type = Counter32
_HwWsecStatsCCMPReplays_Object = MibTableColumn
hwWsecStatsCCMPReplays = _HwWsecStatsCCMPReplays_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 17),
    _HwWsecStatsCCMPReplays_Type()
)
hwWsecStatsCCMPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsCCMPReplays.setStatus("current")
_HwWsecStatsCCMPDecryptErrors_Type = Counter32
_HwWsecStatsCCMPDecryptErrors_Object = MibTableColumn
hwWsecStatsCCMPDecryptErrors = _HwWsecStatsCCMPDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 18),
    _HwWsecStatsCCMPDecryptErrors_Type()
)
hwWsecStatsCCMPDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsCCMPDecryptErrors.setStatus("current")
_HwWsecStatsWAISignatureErrors_Type = Counter32
_HwWsecStatsWAISignatureErrors_Object = MibTableColumn
hwWsecStatsWAISignatureErrors = _HwWsecStatsWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 19),
    _HwWsecStatsWAISignatureErrors_Type()
)
hwWsecStatsWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAISignatureErrors.setStatus("current")
_HwWsecStatsWAIHMACErrors_Type = Counter32
_HwWsecStatsWAIHMACErrors_Object = MibTableColumn
hwWsecStatsWAIHMACErrors = _HwWsecStatsWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 20),
    _HwWsecStatsWAIHMACErrors_Type()
)
hwWsecStatsWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIHMACErrors.setStatus("current")
_HwWsecStatsWAIAuthenticationResultFailures_Type = Counter32
_HwWsecStatsWAIAuthenticationResultFailures_Object = MibTableColumn
hwWsecStatsWAIAuthenticationResultFailures = _HwWsecStatsWAIAuthenticationResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 21),
    _HwWsecStatsWAIAuthenticationResultFailures_Type()
)
hwWsecStatsWAIAuthenticationResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIAuthenticationResultFailures.setStatus("current")
_HwWsecStatsWAIDiscardCounters_Type = Counter32
_HwWsecStatsWAIDiscardCounters_Object = MibTableColumn
hwWsecStatsWAIDiscardCounters = _HwWsecStatsWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 22),
    _HwWsecStatsWAIDiscardCounters_Type()
)
hwWsecStatsWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIDiscardCounters.setStatus("current")
_HwWsecStatsWAITimeoutCounters_Type = Counter32
_HwWsecStatsWAITimeoutCounters_Object = MibTableColumn
hwWsecStatsWAITimeoutCounters = _HwWsecStatsWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 23),
    _HwWsecStatsWAITimeoutCounters_Type()
)
hwWsecStatsWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAITimeoutCounters.setStatus("current")
_HwWsecStatsWAIFormatErrors_Type = Counter32
_HwWsecStatsWAIFormatErrors_Object = MibTableColumn
hwWsecStatsWAIFormatErrors = _HwWsecStatsWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 24),
    _HwWsecStatsWAIFormatErrors_Type()
)
hwWsecStatsWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIFormatErrors.setStatus("current")
_HwWsecStatsWAICertificateHandshakeFailures_Type = Counter32
_HwWsecStatsWAICertificateHandshakeFailures_Object = MibTableColumn
hwWsecStatsWAICertificateHandshakeFailures = _HwWsecStatsWAICertificateHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 25),
    _HwWsecStatsWAICertificateHandshakeFailures_Type()
)
hwWsecStatsWAICertificateHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAICertificateHandshakeFailures.setStatus("current")
_HwWsecStatsWAIUnicastHandshakeFailures_Type = Counter32
_HwWsecStatsWAIUnicastHandshakeFailures_Object = MibTableColumn
hwWsecStatsWAIUnicastHandshakeFailures = _HwWsecStatsWAIUnicastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 26),
    _HwWsecStatsWAIUnicastHandshakeFailures_Type()
)
hwWsecStatsWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIUnicastHandshakeFailures.setStatus("current")
_HwWsecStatsWAIMulticastHandshakeFailures_Type = Counter32
_HwWsecStatsWAIMulticastHandshakeFailures_Object = MibTableColumn
hwWsecStatsWAIMulticastHandshakeFailures = _HwWsecStatsWAIMulticastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 27),
    _HwWsecStatsWAIMulticastHandshakeFailures_Type()
)
hwWsecStatsWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWAIMulticastHandshakeFailures.setStatus("current")
_HwWsecStatsWPIReplayCounter_Type = Counter32
_HwWsecStatsWPIReplayCounter_Object = MibTableColumn
hwWsecStatsWPIReplayCounter = _HwWsecStatsWPIReplayCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 28),
    _HwWsecStatsWPIReplayCounter_Type()
)
hwWsecStatsWPIReplayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWPIReplayCounter.setStatus("current")
_HwWsecStatsWPIDecryptableErrors_Type = Counter32
_HwWsecStatsWPIDecryptableErrors_Object = MibTableColumn
hwWsecStatsWPIDecryptableErrors = _HwWsecStatsWPIDecryptableErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 29),
    _HwWsecStatsWPIDecryptableErrors_Type()
)
hwWsecStatsWPIDecryptableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWPIDecryptableErrors.setStatus("current")
_HwWsecStatsWPIMICErrors_Type = Counter32
_HwWsecStatsWPIMICErrors_Object = MibTableColumn
hwWsecStatsWPIMICErrors = _HwWsecStatsWPIMICErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 30),
    _HwWsecStatsWPIMICErrors_Type()
)
hwWsecStatsWPIMICErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWPIMICErrors.setStatus("current")
_HwWsecStatsControlledPortStatus_Type = TruthValue
_HwWsecStatsControlledPortStatus_Object = MibTableColumn
hwWsecStatsControlledPortStatus = _HwWsecStatsControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 31),
    _HwWsecStatsControlledPortStatus_Type()
)
hwWsecStatsControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsControlledPortStatus.setStatus("current")
_HwWsecStatsNumberOfPTKSAReplayCounters_Type = Integer32
_HwWsecStatsNumberOfPTKSAReplayCounters_Object = MibTableColumn
hwWsecStatsNumberOfPTKSAReplayCounters = _HwWsecStatsNumberOfPTKSAReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 32),
    _HwWsecStatsNumberOfPTKSAReplayCounters_Type()
)
hwWsecStatsNumberOfPTKSAReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsNumberOfPTKSAReplayCounters.setStatus("current")
_HwWsecStatsNumberOfGTKSAReplayCounters_Type = Integer32
_HwWsecStatsNumberOfGTKSAReplayCounters_Object = MibTableColumn
hwWsecStatsNumberOfGTKSAReplayCounters = _HwWsecStatsNumberOfGTKSAReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 33),
    _HwWsecStatsNumberOfGTKSAReplayCounters_Type()
)
hwWsecStatsNumberOfGTKSAReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsNumberOfGTKSAReplayCounters.setStatus("current")
_HwWsecStatsTKIPCounterMeasuresInvoked_Type = Integer32
_HwWsecStatsTKIPCounterMeasuresInvoked_Object = MibTableColumn
hwWsecStatsTKIPCounterMeasuresInvoked = _HwWsecStatsTKIPCounterMeasuresInvoked_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 34),
    _HwWsecStatsTKIPCounterMeasuresInvoked_Type()
)
hwWsecStatsTKIPCounterMeasuresInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsTKIPCounterMeasuresInvoked.setStatus("current")
_HwWsecStatsWpa4WayHandshakeFailures_Type = Integer32
_HwWsecStatsWpa4WayHandshakeFailures_Object = MibTableColumn
hwWsecStatsWpa4WayHandshakeFailures = _HwWsecStatsWpa4WayHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 5, 1, 35),
    _HwWsecStatsWpa4WayHandshakeFailures_Type()
)
hwWsecStatsWpa4WayHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecStatsWpa4WayHandshakeFailures.setStatus("current")
_HwWsecBatchProfileInfo_ObjectIdentity = ObjectIdentity
hwWsecBatchProfileInfo = _HwWsecBatchProfileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 6)
)
_HwWsecBatchProfileStartNumber_Type = Integer32
_HwWsecBatchProfileStartNumber_Object = MibScalar
hwWsecBatchProfileStartNumber = _HwWsecBatchProfileStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 6, 1),
    _HwWsecBatchProfileStartNumber_Type()
)
hwWsecBatchProfileStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecBatchProfileStartNumber.setStatus("current")
_HwWsecBatchProfileWantNumber_Type = Integer32
_HwWsecBatchProfileWantNumber_Object = MibScalar
hwWsecBatchProfileWantNumber = _HwWsecBatchProfileWantNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 6, 2),
    _HwWsecBatchProfileWantNumber_Type()
)
hwWsecBatchProfileWantNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWsecBatchProfileWantNumber.setStatus("current")
_HwWsecBatchProfileReturnNumber_Type = Integer32
_HwWsecBatchProfileReturnNumber_Object = MibScalar
hwWsecBatchProfileReturnNumber = _HwWsecBatchProfileReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 6, 3),
    _HwWsecBatchProfileReturnNumber_Type()
)
hwWsecBatchProfileReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecBatchProfileReturnNumber.setStatus("current")
_HwWsecBatchProfileName_Type = OctetString
_HwWsecBatchProfileName_Object = MibScalar
hwWsecBatchProfileName = _HwWsecBatchProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 6, 4),
    _HwWsecBatchProfileName_Type()
)
hwWsecBatchProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWsecBatchProfileName.setStatus("current")
_HwWsecNotifications_ObjectIdentity = ObjectIdentity
hwWsecNotifications = _HwWsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9)
)
_HwWsecNotify_ObjectIdentity = ObjectIdentity
hwWsecNotify = _HwWsecNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1)
)
_HwWsecNotifyObjects_ObjectIdentity = ObjectIdentity
hwWsecNotifyObjects = _HwWsecNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2)
)
_HwStaAuthenticationMode_Type = Integer32
_HwStaAuthenticationMode_Object = MibScalar
hwStaAuthenticationMode = _HwStaAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 1),
    _HwStaAuthenticationMode_Type()
)
hwStaAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenticationMode.setStatus("current")
_HwStaAuthenticationFailCause_Type = Integer32
_HwStaAuthenticationFailCause_Object = MibScalar
hwStaAuthenticationFailCause = _HwStaAuthenticationFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 2),
    _HwStaAuthenticationFailCause_Type()
)
hwStaAuthenticationFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenticationFailCause.setStatus("current")
_HwStaAssociationFailCause_Type = Integer32
_HwStaAssociationFailCause_Object = MibScalar
hwStaAssociationFailCause = _HwStaAssociationFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 3),
    _HwStaAssociationFailCause_Type()
)
hwStaAssociationFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAssociationFailCause.setStatus("current")
_HwStaAssocBssid_Type = MacAddress
_HwStaAssocBssid_Object = MibScalar
hwStaAssocBssid = _HwStaAssocBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 4),
    _HwStaAssocBssid_Type()
)
hwStaAssocBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAssocBssid.setStatus("current")


class _HwStaFailCodeType_Type(Integer32):
    """Custom type hwStaFailCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reasonCode", 1),
          ("statusCode", 2))
    )


_HwStaFailCodeType_Type.__name__ = "Integer32"
_HwStaFailCodeType_Object = MibScalar
hwStaFailCodeType = _HwStaFailCodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 5),
    _HwStaFailCodeType_Type()
)
hwStaFailCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaFailCodeType.setStatus("current")
_HwWepIDConflictTrapAPMAC_Type = MacAddress
_HwWepIDConflictTrapAPMAC_Object = MibScalar
hwWepIDConflictTrapAPMAC = _HwWepIDConflictTrapAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 6),
    _HwWepIDConflictTrapAPMAC_Type()
)
hwWepIDConflictTrapAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapAPMAC.setStatus("current")
_HwWepIDConflictTrapAPID_Type = Integer32
_HwWepIDConflictTrapAPID_Object = MibScalar
hwWepIDConflictTrapAPID = _HwWepIDConflictTrapAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 7),
    _HwWepIDConflictTrapAPID_Type()
)
hwWepIDConflictTrapAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapAPID.setStatus("current")
_HwWepIDConflictTrapRadioId_Type = Integer32
_HwWepIDConflictTrapRadioId_Object = MibScalar
hwWepIDConflictTrapRadioId = _HwWepIDConflictTrapRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 8),
    _HwWepIDConflictTrapRadioId_Type()
)
hwWepIDConflictTrapRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapRadioId.setStatus("current")


class _HwWepIDConflictTrapPreSSID_Type(OctetString):
    """Custom type hwWepIDConflictTrapPreSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWepIDConflictTrapPreSSID_Type.__name__ = "OctetString"
_HwWepIDConflictTrapPreSSID_Object = MibScalar
hwWepIDConflictTrapPreSSID = _HwWepIDConflictTrapPreSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 9),
    _HwWepIDConflictTrapPreSSID_Type()
)
hwWepIDConflictTrapPreSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapPreSSID.setStatus("current")


class _HwWepIDConflictTrapCurrSSID_Type(OctetString):
    """Custom type hwWepIDConflictTrapCurrSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwWepIDConflictTrapCurrSSID_Type.__name__ = "OctetString"
_HwWepIDConflictTrapCurrSSID_Object = MibScalar
hwWepIDConflictTrapCurrSSID = _HwWepIDConflictTrapCurrSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 10),
    _HwWepIDConflictTrapCurrSSID_Type()
)
hwWepIDConflictTrapCurrSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapCurrSSID.setStatus("current")
_HwWepIDConflictTrapCipherIdx_Type = Integer32
_HwWepIDConflictTrapCipherIdx_Object = MibScalar
hwWepIDConflictTrapCipherIdx = _HwWepIDConflictTrapCipherIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 11),
    _HwWepIDConflictTrapCipherIdx_Type()
)
hwWepIDConflictTrapCipherIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWepIDConflictTrapCipherIdx.setStatus("current")
_HwWlanStaAuthEncryptMode_Type = Integer32
_HwWlanStaAuthEncryptMode_Object = MibScalar
hwWlanStaAuthEncryptMode = _HwWlanStaAuthEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 12),
    _HwWlanStaAuthEncryptMode_Type()
)
hwWlanStaAuthEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanStaAuthEncryptMode.setStatus("current")
_HwWlanVapAuthEncryptMode_Type = Integer32
_HwWlanVapAuthEncryptMode_Object = MibScalar
hwWlanVapAuthEncryptMode = _HwWlanVapAuthEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 13),
    _HwWlanVapAuthEncryptMode_Type()
)
hwWlanVapAuthEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanVapAuthEncryptMode.setStatus("current")
_HwStaAuthenticationFailCauseStr_Type = OctetString
_HwStaAuthenticationFailCauseStr_Object = MibScalar
hwStaAuthenticationFailCauseStr = _HwStaAuthenticationFailCauseStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 14),
    _HwStaAuthenticationFailCauseStr_Type()
)
hwStaAuthenticationFailCauseStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenticationFailCauseStr.setStatus("current")
_HwStaAssociationFailCauseStr_Type = OctetString
_HwStaAssociationFailCauseStr_Object = MibScalar
hwStaAssociationFailCauseStr = _HwStaAssociationFailCauseStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 2, 15),
    _HwStaAssociationFailCauseStr_Type()
)
hwStaAssociationFailCauseStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAssociationFailCauseStr.setStatus("current")
_HwWlanSecurityObject_ObjectIdentity = ObjectIdentity
hwWlanSecurityObject = _HwWlanSecurityObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 10)
)
_HwWlanSecurityConformance_ObjectIdentity = ObjectIdentity
hwWlanSecurityConformance = _HwWlanSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11)
)
_HwWlanSecurityCompliances_ObjectIdentity = ObjectIdentity
hwWlanSecurityCompliances = _HwWlanSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 1)
)
_HwWlanSecurityObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanSecurityObjectGroups = _HwWlanSecurityObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2)
)

# Managed Objects groups

hwWsecProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 1)
)
hwWsecProfileGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileName"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWEPDataEncrypt"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWEPDefaultKeyID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWEPKeyMappingLength"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAsuIpAddr"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileCaCertFileName"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAsuCertFileName"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAcCertFileName"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAcPrvKeyFileName"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileRsnaVersion"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWapiVersion"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileRowStatus"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileCaPfxPassword"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileCaCertState"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAsuPfxPassword"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAsuCertState"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAcPfxPassword"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAcCertState"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileKeyPfxPassword"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileAsuType"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpaPtkRekeySwitch"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpa2PtkRekeySwitch"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpaWpa2PtkRekeySwitch"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpaPtkRekeyInterval"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpa2PtkRekeyInterval"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecProfileWpaWpa2PtkRekeyInterval"))
)
if mibBuilder.loadTexts:
    hwWsecProfileGroup.setStatus("current")

hwWsecWEPDefaultKeysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 2)
)
hwWsecWEPDefaultKeysGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPDefaultKeyValue"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPPassPhrase"))
)
if mibBuilder.loadTexts:
    hwWsecWEPDefaultKeysGroup.setStatus("current")

hwWsecWEPKeyMappingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 3)
)
hwWsecWEPKeyMappingsGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPKeyMappingAddress"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPKeyMappingWEPOn"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPKeyMappingValue"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecWEPKeyMappingStatus"))
)
if mibBuilder.loadTexts:
    hwWsecWEPKeyMappingsGroup.setStatus("current")

hwWsecAuthSuitesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 4)
)
hwWsecAuthSuitesGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthSuite"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthSuiteEnabled"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPreauthenticationImplemented"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPreauthenticationEnabled"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthUnicastKeysSupported"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPairwiseCipher"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPairwiseCipherSize"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthUnicastRekeyMethod"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthUnicastRekeyTime"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthUnicastRekeyPackets"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastCipher"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastCipherSize"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastRekeyMethod"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastRekeyTime"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastRekeyPackets"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastRekeyStrict"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPSKValue"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthPSKPassPhrase"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthCertificateUpdateCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthMulticastUpdateCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthUnicastUpdateCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthBKLifetime"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthBKReauthThreshold"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthSATimeout"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthExcludeUnencrypted"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthDot1XMethod"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthControlledAuthControl"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthControlledPortControl"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecAuthOptionalImplemented"))
)
if mibBuilder.loadTexts:
    hwWsecAuthSuitesGroup.setStatus("current")

hwWsecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 5)
)
hwWsecStatsGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsSTAAddress"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsVersion"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsBKIDUsed"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsAuthenticationSuiteSelected"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsUnicastCipherSelected"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsMulticastCipherSelected"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsAuthenticationSuiteRequested"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsUnicastCipherRequested"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsMulticastCipherRequested"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWEPICVErrorCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWEPExcludedCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWEPUndecryptableCount"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsTKIPICVErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsTKIPLocalMICFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsTKIPRemoteMICFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsTKIPReplays"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsCCMPReplays"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsCCMPDecryptErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAISignatureErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIHMACErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIAuthenticationResultFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIDiscardCounters"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAITimeoutCounters"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIFormatErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAICertificateHandshakeFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIUnicastHandshakeFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWAIMulticastHandshakeFailures"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWPIReplayCounter"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWPIDecryptableErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWPIMICErrors"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsControlledPortStatus"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsNumberOfPTKSAReplayCounters"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsNumberOfGTKSAReplayCounters"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsTKIPCounterMeasuresInvoked"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecStatsWpa4WayHandshakeFailures"))
)
if mibBuilder.loadTexts:
    hwWsecStatsGroup.setStatus("current")

hwWsecBatchProfileInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 6)
)
hwWsecBatchProfileInfoGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWsecBatchProfileStartNumber"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecBatchProfileWantNumber"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecBatchProfileReturnNumber"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWsecBatchProfileName"))
)
if mibBuilder.loadTexts:
    hwWsecBatchProfileInfoGroup.setStatus("current")

hwWsecNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 8)
)
hwWsecNotifyObjectsGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationMode"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationFailCause"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssociationFailCause"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaFailCodeType"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapAPMAC"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapAPID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapRadioId"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapPreSSID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapCurrSSID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapCipherIdx"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWlanStaAuthEncryptMode"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWlanVapAuthEncryptMode"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationFailCauseStr"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssociationFailCauseStr"))
)
if mibBuilder.loadTexts:
    hwWsecNotifyObjectsGroup.setStatus("current")


# Notification objects

hwStaAuthErrorNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 1)
)
hwStaAuthErrorNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationMode"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaFailCodeType"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationFailCause"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthenticationFailCauseStr"))
)
if mibBuilder.loadTexts:
    hwStaAuthErrorNotify.setStatus(
        "current"
    )

hwStaAssociationFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 2)
)
hwStaAssociationFailNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaFailCodeType"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssociationFailCause"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssociationFailCauseStr"))
)
if mibBuilder.loadTexts:
    hwStaAssociationFailNotify.setStatus(
        "current"
    )

hwUserWithInvalidCerficationInbreakNetworkNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 3)
)
hwUserWithInvalidCerficationInbreakNetworkNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"))
)
if mibBuilder.loadTexts:
    hwUserWithInvalidCerficationInbreakNetworkNotify.setStatus(
        "current"
    )

hwStationRepititiveAttackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 4)
)
hwStationRepititiveAttackNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"))
)
if mibBuilder.loadTexts:
    hwStationRepititiveAttackNotify.setStatus(
        "current"
    )

hwTamperAttackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 5)
)
hwTamperAttackNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"))
)
if mibBuilder.loadTexts:
    hwTamperAttackNotify.setStatus(
        "current"
    )

hwLowSafeLevelAttackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 6)
)
hwLowSafeLevelAttackNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"))
)
if mibBuilder.loadTexts:
    hwLowSafeLevelAttackNotify.setStatus(
        "current"
    )

hwAddressRedirectionAttackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 7)
)
hwAddressRedirectionAttackNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"))
)
if mibBuilder.loadTexts:
    hwAddressRedirectionAttackNotify.setStatus(
        "current"
    )

hwWepIDConflictNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 8)
)
hwWepIDConflictNotify.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapAPMAC"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapAPID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapRadioId"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapPreSSID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapCurrSSID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictTrapCipherIdx"))
)
if mibBuilder.loadTexts:
    hwWepIDConflictNotify.setStatus(
        "current"
    )

hwStaAuthEncryptModeNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 9, 1, 9)
)
hwStaAuthEncryptModeNotMatchNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-RADIO-MIB", "hwRadioID"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssocBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWlanStaAuthEncryptMode"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWlanVapAuthEncryptMode"))
)
if mibBuilder.loadTexts:
    hwStaAuthEncryptModeNotMatchNotify.setStatus(
        "current"
    )


# Notifications groups

hwWsecNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 2, 7)
)
hwWsecNotifyGroup.setObjects(
      *(("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthErrorNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAssociationFailNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwUserWithInvalidCerficationInbreakNetworkNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStationRepititiveAttackNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwTamperAttackNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwLowSafeLevelAttackNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwAddressRedirectionAttackNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwWepIDConflictNotify"),
        ("HUAWEI-WLAN-SECURITY-MIB", "hwStaAuthEncryptModeNotMatchNotify"))
)
if mibBuilder.loadTexts:
    hwWsecNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwWlanSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 6, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanSecurityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-SECURITY-MIB",
    **{"hwWlanSecurity": hwWlanSecurity,
       "hwWsecProfileTable": hwWsecProfileTable,
       "hwWsecProfileEntry": hwWsecProfileEntry,
       "hwWsecProfileName": hwWsecProfileName,
       "hwWsecProfileWEPDataEncrypt": hwWsecProfileWEPDataEncrypt,
       "hwWsecProfileWEPDefaultKeyID": hwWsecProfileWEPDefaultKeyID,
       "hwWsecProfileWEPKeyMappingLength": hwWsecProfileWEPKeyMappingLength,
       "hwWsecProfileAsuIpAddr": hwWsecProfileAsuIpAddr,
       "hwWsecProfileCaCertFileName": hwWsecProfileCaCertFileName,
       "hwWsecProfileAsuCertFileName": hwWsecProfileAsuCertFileName,
       "hwWsecProfileAcCertFileName": hwWsecProfileAcCertFileName,
       "hwWsecProfileAcPrvKeyFileName": hwWsecProfileAcPrvKeyFileName,
       "hwWsecProfileRsnaVersion": hwWsecProfileRsnaVersion,
       "hwWsecProfileWapiVersion": hwWsecProfileWapiVersion,
       "hwWsecProfileRowStatus": hwWsecProfileRowStatus,
       "hwWsecProfileCaPfxPassword": hwWsecProfileCaPfxPassword,
       "hwWsecProfileCaCertState": hwWsecProfileCaCertState,
       "hwWsecProfileAsuPfxPassword": hwWsecProfileAsuPfxPassword,
       "hwWsecProfileAsuCertState": hwWsecProfileAsuCertState,
       "hwWsecProfileAcPfxPassword": hwWsecProfileAcPfxPassword,
       "hwWsecProfileAcCertState": hwWsecProfileAcCertState,
       "hwWsecProfileKeyPfxPassword": hwWsecProfileKeyPfxPassword,
       "hwWsecProfileAsuType": hwWsecProfileAsuType,
       "hwWsecProfileWpaPtkRekeySwitch": hwWsecProfileWpaPtkRekeySwitch,
       "hwWsecProfileWpa2PtkRekeySwitch": hwWsecProfileWpa2PtkRekeySwitch,
       "hwWsecProfileWpaWpa2PtkRekeySwitch": hwWsecProfileWpaWpa2PtkRekeySwitch,
       "hwWsecProfileWpaPtkRekeyInterval": hwWsecProfileWpaPtkRekeyInterval,
       "hwWsecProfileWpa2PtkRekeyInterval": hwWsecProfileWpa2PtkRekeyInterval,
       "hwWsecProfileWpaWpa2PtkRekeyInterval": hwWsecProfileWpaWpa2PtkRekeyInterval,
       "hwWsecWEPDefaultKeysTable": hwWsecWEPDefaultKeysTable,
       "hwWsecWEPDefaultKeysEntry": hwWsecWEPDefaultKeysEntry,
       "hwWsecWEPDefaultKeyIndex": hwWsecWEPDefaultKeyIndex,
       "hwWsecWEPDefaultKeyValue": hwWsecWEPDefaultKeyValue,
       "hwWsecWEPPassPhrase": hwWsecWEPPassPhrase,
       "hwWsecWEPKeyMappingsTable": hwWsecWEPKeyMappingsTable,
       "hwWsecWEPKeyMappingsEntry": hwWsecWEPKeyMappingsEntry,
       "hwWsecWEPKeyMappingIndex": hwWsecWEPKeyMappingIndex,
       "hwWsecWEPKeyMappingAddress": hwWsecWEPKeyMappingAddress,
       "hwWsecWEPKeyMappingWEPOn": hwWsecWEPKeyMappingWEPOn,
       "hwWsecWEPKeyMappingValue": hwWsecWEPKeyMappingValue,
       "hwWsecWEPKeyMappingStatus": hwWsecWEPKeyMappingStatus,
       "hwWsecAuthSuitesTable": hwWsecAuthSuitesTable,
       "hwWsecAuthSuitesEntry": hwWsecAuthSuitesEntry,
       "hwWsecAuthSuiteIndex": hwWsecAuthSuiteIndex,
       "hwWsecAuthSuite": hwWsecAuthSuite,
       "hwWsecAuthSuiteEnabled": hwWsecAuthSuiteEnabled,
       "hwWsecAuthPreauthenticationImplemented": hwWsecAuthPreauthenticationImplemented,
       "hwWsecAuthPreauthenticationEnabled": hwWsecAuthPreauthenticationEnabled,
       "hwWsecAuthUnicastKeysSupported": hwWsecAuthUnicastKeysSupported,
       "hwWsecAuthPairwiseCipher": hwWsecAuthPairwiseCipher,
       "hwWsecAuthPairwiseCipherSize": hwWsecAuthPairwiseCipherSize,
       "hwWsecAuthUnicastRekeyMethod": hwWsecAuthUnicastRekeyMethod,
       "hwWsecAuthUnicastRekeyTime": hwWsecAuthUnicastRekeyTime,
       "hwWsecAuthUnicastRekeyPackets": hwWsecAuthUnicastRekeyPackets,
       "hwWsecAuthMulticastCipher": hwWsecAuthMulticastCipher,
       "hwWsecAuthMulticastCipherSize": hwWsecAuthMulticastCipherSize,
       "hwWsecAuthMulticastRekeyMethod": hwWsecAuthMulticastRekeyMethod,
       "hwWsecAuthMulticastRekeyTime": hwWsecAuthMulticastRekeyTime,
       "hwWsecAuthMulticastRekeyPackets": hwWsecAuthMulticastRekeyPackets,
       "hwWsecAuthMulticastRekeyStrict": hwWsecAuthMulticastRekeyStrict,
       "hwWsecAuthPSKValue": hwWsecAuthPSKValue,
       "hwWsecAuthPSKPassPhrase": hwWsecAuthPSKPassPhrase,
       "hwWsecAuthCertificateUpdateCount": hwWsecAuthCertificateUpdateCount,
       "hwWsecAuthMulticastUpdateCount": hwWsecAuthMulticastUpdateCount,
       "hwWsecAuthUnicastUpdateCount": hwWsecAuthUnicastUpdateCount,
       "hwWsecAuthBKLifetime": hwWsecAuthBKLifetime,
       "hwWsecAuthBKReauthThreshold": hwWsecAuthBKReauthThreshold,
       "hwWsecAuthSATimeout": hwWsecAuthSATimeout,
       "hwWsecAuthExcludeUnencrypted": hwWsecAuthExcludeUnencrypted,
       "hwWsecAuthDot1XMethod": hwWsecAuthDot1XMethod,
       "hwWsecAuthControlledAuthControl": hwWsecAuthControlledAuthControl,
       "hwWsecAuthControlledPortControl": hwWsecAuthControlledPortControl,
       "hwWsecAuthOptionalImplemented": hwWsecAuthOptionalImplemented,
       "hwWsecStatsTable": hwWsecStatsTable,
       "hwWsecStatsEntry": hwWsecStatsEntry,
       "hwWsecStatsSTAAddress": hwWsecStatsSTAAddress,
       "hwWsecStatsVersion": hwWsecStatsVersion,
       "hwWsecStatsBKIDUsed": hwWsecStatsBKIDUsed,
       "hwWsecStatsAuthenticationSuiteSelected": hwWsecStatsAuthenticationSuiteSelected,
       "hwWsecStatsUnicastCipherSelected": hwWsecStatsUnicastCipherSelected,
       "hwWsecStatsMulticastCipherSelected": hwWsecStatsMulticastCipherSelected,
       "hwWsecStatsAuthenticationSuiteRequested": hwWsecStatsAuthenticationSuiteRequested,
       "hwWsecStatsUnicastCipherRequested": hwWsecStatsUnicastCipherRequested,
       "hwWsecStatsMulticastCipherRequested": hwWsecStatsMulticastCipherRequested,
       "hwWsecStatsWEPICVErrorCount": hwWsecStatsWEPICVErrorCount,
       "hwWsecStatsWEPExcludedCount": hwWsecStatsWEPExcludedCount,
       "hwWsecStatsWEPUndecryptableCount": hwWsecStatsWEPUndecryptableCount,
       "hwWsecStatsTKIPICVErrors": hwWsecStatsTKIPICVErrors,
       "hwWsecStatsTKIPLocalMICFailures": hwWsecStatsTKIPLocalMICFailures,
       "hwWsecStatsTKIPRemoteMICFailures": hwWsecStatsTKIPRemoteMICFailures,
       "hwWsecStatsTKIPReplays": hwWsecStatsTKIPReplays,
       "hwWsecStatsCCMPReplays": hwWsecStatsCCMPReplays,
       "hwWsecStatsCCMPDecryptErrors": hwWsecStatsCCMPDecryptErrors,
       "hwWsecStatsWAISignatureErrors": hwWsecStatsWAISignatureErrors,
       "hwWsecStatsWAIHMACErrors": hwWsecStatsWAIHMACErrors,
       "hwWsecStatsWAIAuthenticationResultFailures": hwWsecStatsWAIAuthenticationResultFailures,
       "hwWsecStatsWAIDiscardCounters": hwWsecStatsWAIDiscardCounters,
       "hwWsecStatsWAITimeoutCounters": hwWsecStatsWAITimeoutCounters,
       "hwWsecStatsWAIFormatErrors": hwWsecStatsWAIFormatErrors,
       "hwWsecStatsWAICertificateHandshakeFailures": hwWsecStatsWAICertificateHandshakeFailures,
       "hwWsecStatsWAIUnicastHandshakeFailures": hwWsecStatsWAIUnicastHandshakeFailures,
       "hwWsecStatsWAIMulticastHandshakeFailures": hwWsecStatsWAIMulticastHandshakeFailures,
       "hwWsecStatsWPIReplayCounter": hwWsecStatsWPIReplayCounter,
       "hwWsecStatsWPIDecryptableErrors": hwWsecStatsWPIDecryptableErrors,
       "hwWsecStatsWPIMICErrors": hwWsecStatsWPIMICErrors,
       "hwWsecStatsControlledPortStatus": hwWsecStatsControlledPortStatus,
       "hwWsecStatsNumberOfPTKSAReplayCounters": hwWsecStatsNumberOfPTKSAReplayCounters,
       "hwWsecStatsNumberOfGTKSAReplayCounters": hwWsecStatsNumberOfGTKSAReplayCounters,
       "hwWsecStatsTKIPCounterMeasuresInvoked": hwWsecStatsTKIPCounterMeasuresInvoked,
       "hwWsecStatsWpa4WayHandshakeFailures": hwWsecStatsWpa4WayHandshakeFailures,
       "hwWsecBatchProfileInfo": hwWsecBatchProfileInfo,
       "hwWsecBatchProfileStartNumber": hwWsecBatchProfileStartNumber,
       "hwWsecBatchProfileWantNumber": hwWsecBatchProfileWantNumber,
       "hwWsecBatchProfileReturnNumber": hwWsecBatchProfileReturnNumber,
       "hwWsecBatchProfileName": hwWsecBatchProfileName,
       "hwWsecNotifications": hwWsecNotifications,
       "hwWsecNotify": hwWsecNotify,
       "hwStaAuthErrorNotify": hwStaAuthErrorNotify,
       "hwStaAssociationFailNotify": hwStaAssociationFailNotify,
       "hwUserWithInvalidCerficationInbreakNetworkNotify": hwUserWithInvalidCerficationInbreakNetworkNotify,
       "hwStationRepititiveAttackNotify": hwStationRepititiveAttackNotify,
       "hwTamperAttackNotify": hwTamperAttackNotify,
       "hwLowSafeLevelAttackNotify": hwLowSafeLevelAttackNotify,
       "hwAddressRedirectionAttackNotify": hwAddressRedirectionAttackNotify,
       "hwWepIDConflictNotify": hwWepIDConflictNotify,
       "hwStaAuthEncryptModeNotMatchNotify": hwStaAuthEncryptModeNotMatchNotify,
       "hwWsecNotifyObjects": hwWsecNotifyObjects,
       "hwStaAuthenticationMode": hwStaAuthenticationMode,
       "hwStaAuthenticationFailCause": hwStaAuthenticationFailCause,
       "hwStaAssociationFailCause": hwStaAssociationFailCause,
       "hwStaAssocBssid": hwStaAssocBssid,
       "hwStaFailCodeType": hwStaFailCodeType,
       "hwWepIDConflictTrapAPMAC": hwWepIDConflictTrapAPMAC,
       "hwWepIDConflictTrapAPID": hwWepIDConflictTrapAPID,
       "hwWepIDConflictTrapRadioId": hwWepIDConflictTrapRadioId,
       "hwWepIDConflictTrapPreSSID": hwWepIDConflictTrapPreSSID,
       "hwWepIDConflictTrapCurrSSID": hwWepIDConflictTrapCurrSSID,
       "hwWepIDConflictTrapCipherIdx": hwWepIDConflictTrapCipherIdx,
       "hwWlanStaAuthEncryptMode": hwWlanStaAuthEncryptMode,
       "hwWlanVapAuthEncryptMode": hwWlanVapAuthEncryptMode,
       "hwStaAuthenticationFailCauseStr": hwStaAuthenticationFailCauseStr,
       "hwStaAssociationFailCauseStr": hwStaAssociationFailCauseStr,
       "hwWlanSecurityObject": hwWlanSecurityObject,
       "hwWlanSecurityConformance": hwWlanSecurityConformance,
       "hwWlanSecurityCompliances": hwWlanSecurityCompliances,
       "hwWlanSecurityCompliance": hwWlanSecurityCompliance,
       "hwWlanSecurityObjectGroups": hwWlanSecurityObjectGroups,
       "hwWsecProfileGroup": hwWsecProfileGroup,
       "hwWsecWEPDefaultKeysGroup": hwWsecWEPDefaultKeysGroup,
       "hwWsecWEPKeyMappingsGroup": hwWsecWEPKeyMappingsGroup,
       "hwWsecAuthSuitesGroup": hwWsecAuthSuitesGroup,
       "hwWsecStatsGroup": hwWsecStatsGroup,
       "hwWsecBatchProfileInfoGroup": hwWsecBatchProfileInfoGroup,
       "hwWsecNotifyGroup": hwWsecNotifyGroup,
       "hwWsecNotifyObjectsGroup": hwWsecNotifyObjectsGroup}
)
